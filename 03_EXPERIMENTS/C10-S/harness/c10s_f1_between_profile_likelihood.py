"""F1 profile likelihood for the between-world variance component.

Research-only numerical inversion. The likelihood-ratio cutoff is supplied by
the caller and is neither selected nor calibrated here. The interval is
obtained by root finding, not by classifying a finite parameter grid.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Sequence

from scipy.optimize import brentq, minimize_scalar

from c10s_variance_comparison_interface import observed_nested_mr_result


METHOD_ID = "F1_BETWEEN_PROFILE_LIKELIHOOD_0.2"
MODEL_SCOPE = "BALANCED_GAUSSIAN_RANDOM_INTERCEPT"
_LOG2PI = math.log(2.0 * math.pi)


class F1ProfileError(ValueError):
    """Invalid input or numerical profile-likelihood request."""


@dataclass(frozen=True)
class F1ProfileSet:
    likelihood_ratio_cutoff: float
    mle_between_variance: float
    max_profile_loglik: float
    confidence_components: tuple[tuple[float, float], ...]
    lower_boundary_included: bool
    upper_endpoint_bracket_expansions: int
    status: str
    method_id: str = METHOD_ID


def _sufficient_statistics(rows: Sequence[Sequence[float]]):
    observed = observed_nested_mr_result(rows)
    m, r = len(rows), len(rows[0])
    if m < 3:
        raise F1ProfileError("F1_PROFILE_REQUIRES_M_AT_LEAST_3")
    df_w, df_b = m * (r - 1), m - 1
    ssw = observed.within_estimate * df_w
    s2_means = observed.observed_world_variance
    if ssw <= 0.0:
        raise F1ProfileError(
            "ZERO_WITHIN_SUM_OF_SQUARES_REQUIRES_SEPARATE_BOUNDARY_MODEL"
        )
    if not math.isfinite(ssw) or not math.isfinite(s2_means) or s2_means < 0.0:
        raise F1ProfileError("INVALID_GAUSSIAN_SUFFICIENT_STATISTICS")
    return r, df_w, df_b, ssw, s2_means, observed.within_estimate


def _profile_at_tau(
    tau: float, *, r: int, df_w: int, df_b: int,
    ssw: float, s2_means: float, scale: float,
) -> float:
    if not math.isfinite(tau) or tau < 0.0:
        raise F1ProfileError("TAU_MUST_BE_FINITE_AND_NONNEGATIVE")

    # Optimize log(sigma_within^2), ensuring positivity over a scale-adaptive
    # interval. Endpoints are included as candidates to avoid trusting a
    # bounded optimizer's interior result without comparison.
    center = max(scale, 1e-300)
    lo, hi = math.log(center) - 36.0, math.log(center) + 36.0

    def negative_loglik(log_s: float) -> float:
        s = math.exp(log_s)
        q = tau + s / r
        if not (s > 0.0 and q > 0.0):
            return math.inf
        ll = (
            -0.5 * df_w * (_LOG2PI + math.log(s))
            -0.5 * ssw / s
            -0.5 * df_b * (_LOG2PI + math.log(q))
            -0.5 * df_b * s2_means / q
        )
        return -ll

    result = minimize_scalar(
        negative_loglik, bounds=(lo, hi), method="bounded",
        options={"xatol": 1e-12, "maxiter": 2000},
    )
    candidates = [(negative_loglik(lo), lo), (negative_loglik(hi), hi)]
    if result.success and math.isfinite(result.fun):
        candidates.append((float(result.fun), float(result.x)))
    best_value, best_log_s = min(candidates)
    if not math.isfinite(best_value):
        raise F1ProfileError("PROFILE_LIKELIHOOD_NONFINITE")
    # A boundary optimum signals that the nuisance-parameter search range was
    # insufficient; fail closed rather than silently returning a false max.
    if best_log_s in (lo, hi):
        raise F1ProfileError("WITHIN_VARIANCE_PROFILE_OPTIMUM_AT_SEARCH_BOUND")
    return -best_value


def f1_profile_loglik(
    rows: Sequence[Sequence[float]], *, between_variance: float,
) -> float:
    """Profile log-likelihood at fixed tau>=0, profiling within variance."""
    if isinstance(between_variance, bool) or not isinstance(between_variance, (int, float)):
        raise F1ProfileError("BETWEEN_VARIANCE_MUST_BE_NUMERIC")
    tau = float(between_variance)
    if not math.isfinite(tau) or tau < 0.0:
        raise F1ProfileError("BETWEEN_VARIANCE_MUST_BE_FINITE_AND_NONNEGATIVE")
    r, df_w, df_b, ssw, s2_means, within = _sufficient_statistics(rows)
    scale = max(within, s2_means, tau, 1e-12)
    return _profile_at_tau(
        tau, r=r, df_w=df_w, df_b=df_b, ssw=ssw,
        s2_means=s2_means, scale=scale,
    )


def f1_profile_between_confidence_set(
    rows: Sequence[Sequence[float]], *,
    likelihood_ratio_cutoff: float,
    max_bracket_expansions: int = 80,
) -> F1ProfileSet:
    """Invert the caller-supplied LR rule by bracketing and root finding.

    The profile MLE is max(0, S2(world means)-MSW/R). The lower endpoint is
    zero when zero lies in the LR set; otherwise it is solved between zero and
    the MLE. The upper endpoint is solved after geometric bracket expansion.
    No critical value is selected and no calibration is performed.
    """
    if (isinstance(likelihood_ratio_cutoff, bool)
            or not isinstance(likelihood_ratio_cutoff, (int, float))
            or not math.isfinite(likelihood_ratio_cutoff)
            or likelihood_ratio_cutoff <= 0.0):
        raise F1ProfileError("LR_CUTOFF_MUST_BE_FINITE_AND_POSITIVE")
    if type(max_bracket_expansions) is not int or max_bracket_expansions < 1:
        raise F1ProfileError("MAX_BRACKET_EXPANSIONS_MUST_BE_POSITIVE_INTEGER")

    r, df_w, df_b, ssw, s2_means, within = _sufficient_statistics(rows)
    tau_hat = max(0.0, s2_means - within / r)
    scale = max(within, s2_means, 1e-12)

    def profile(tau: float) -> float:
        return _profile_at_tau(
            tau, r=r, df_w=df_w, df_b=df_b, ssw=ssw,
            s2_means=s2_means, scale=max(scale, tau, 1e-12),
        )

    maximum = profile(tau_hat)
    if not math.isfinite(maximum):
        raise F1ProfileError("PROFILE_MLE_NONFINITE")

    def lr_excess(tau: float) -> float:
        value = profile(tau)
        return 2.0 * (maximum - value) - float(likelihood_ratio_cutoff)

    at_zero = lr_excess(0.0)
    lower_included = at_zero <= 0.0
    if lower_included:
        lower = 0.0
    else:
        if tau_hat <= 0.0:
            raise F1ProfileError("INCONSISTENT_PROFILE_MLE_AND_LOWER_ENDPOINT")
        lower = brentq(lr_excess, 0.0, tau_hat, xtol=1e-12, rtol=1e-12)

    step = max(scale, tau_hat, 1e-12)
    upper = max(tau_hat + step, 2.0 * step)
    expansions = 0
    upper_value = lr_excess(upper)
    while upper_value <= 0.0 and expansions < max_bracket_expansions:
        upper *= 2.0
        expansions += 1
        upper_value = lr_excess(upper)
    if upper_value <= 0.0:
        raise F1ProfileError("UPPER_PROFILE_ENDPOINT_NOT_BRACKETED")
    upper_endpoint = brentq(
        lr_excess, tau_hat, upper, xtol=1e-12, rtol=1e-12,
    )
    return F1ProfileSet(
        likelihood_ratio_cutoff=float(likelihood_ratio_cutoff),
        mle_between_variance=tau_hat,
        max_profile_loglik=maximum,
        confidence_components=((lower, upper_endpoint),),
        lower_boundary_included=lower_included,
        upper_endpoint_bracket_expansions=expansions,
        status="PROFILE_LR_INTERVAL_ROOT_SOLVED",
    )
