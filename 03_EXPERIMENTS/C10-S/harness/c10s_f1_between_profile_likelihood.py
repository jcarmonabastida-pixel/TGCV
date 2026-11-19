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
class F1NuisanceOptimizerDiagnostic:
    status: str
    bounded_optimizer_loglik: float | None
    independent_loglik: float | None
    absolute_loglik_difference: float | None
    stationary_points: int
    independent_boundary_sensitive: bool
    optimizer_error: str | None


@dataclass(frozen=True)
class F1NuisanceStabilityDiagnostic:
    status: str
    configurations: tuple[tuple[int, float], ...]
    stationary_point_counts: tuple[int, ...]
    optimizer_statuses: tuple[str, ...]
    maximum_loglik_spread: float | None


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


def f1_profile_nuisance_optimizer_diagnostic(
    rows: Sequence[Sequence[float]], *, between_variance: float,
    grid_points: int = 241, log_span: float = 36.0,
    loglik_tolerance: float = 1e-7,
) -> F1NuisanceOptimizerDiagnostic:
    """Compare the production bounded optimizer with an independent score-root scan.

    The independent route scans the nuisance score over log(within variance),
    brackets every detected sign change, solves each stationary point, and
    compares their likelihoods with the bounded production optimizer. This is
    a numerical diagnostic only: it does not select an LR cutoff or certify
    interval coverage.
    """
    if isinstance(between_variance, bool) or not isinstance(between_variance, (int, float)):
        raise F1ProfileError("BETWEEN_VARIANCE_MUST_BE_NUMERIC")
    tau = float(between_variance)
    if not math.isfinite(tau) or tau < 0.0:
        raise F1ProfileError("BETWEEN_VARIANCE_MUST_BE_FINITE_AND_NONNEGATIVE")
    if type(grid_points) is not int or grid_points < 41:
        raise F1ProfileError("NUISANCE_GRID_POINTS_MUST_BE_INTEGER_GE_41")
    if (isinstance(log_span, bool) or not isinstance(log_span, (int, float))
            or not math.isfinite(log_span) or log_span <= 0.0):
        raise F1ProfileError("NUISANCE_LOG_SPAN_MUST_BE_FINITE_AND_POSITIVE")
    if (isinstance(loglik_tolerance, bool)
            or not isinstance(loglik_tolerance, (int, float))
            or not math.isfinite(loglik_tolerance) or loglik_tolerance <= 0.0):
        raise F1ProfileError("NUISANCE_LOGLIK_TOLERANCE_MUST_BE_FINITE_AND_POSITIVE")

    r, df_w, df_b, ssw, s2_means, within = _sufficient_statistics(rows)
    scale = max(within, s2_means, tau, 1e-12)
    center = max(scale, 1e-300)
    lo, hi = math.log(center) - float(log_span), math.log(center) + float(log_span)

    def loglik(log_s: float) -> float:
        s = math.exp(log_s)
        q = tau + s / r
        return (
            -0.5 * df_w * (_LOG2PI + log_s)
            -0.5 * ssw / s
            -0.5 * df_b * (_LOG2PI + math.log(q))
            -0.5 * df_b * s2_means / q
        )

    def score(log_s: float) -> float:
        s = math.exp(log_s)
        q = tau + s / r
        return (
            -0.5 * df_w + 0.5 * ssw / s
            -0.5 * df_b * (s / r) / q
            +0.5 * df_b * s2_means * (s / r) / (q * q)
        )

    xs = [lo + (hi - lo) * i / (grid_points - 1) for i in range(grid_points)]
    roots = []
    for left, right in zip(xs, xs[1:]):
        fl, fr = score(left), score(right)
        if fl == 0.0:
            roots.append(left)
        if fl * fr < 0.0:
            roots.append(brentq(score, left, right, xtol=1e-12, rtol=1e-12))
    if score(hi) == 0.0:
        roots.append(hi)
    roots = sorted({round(value, 12) for value in roots})
    candidates = [(loglik(value), value) for value in roots]
    if not candidates:
        independent_value = None
        independent_boundary = True
    else:
        independent_value, independent_arg = max(candidates)
        independent_boundary = (
            independent_arg - lo <= 1e-7 or hi - independent_arg <= 1e-7
        )

    try:
        bounded_value = _profile_at_tau(
            tau, r=r, df_w=df_w, df_b=df_b, ssw=ssw,
            s2_means=s2_means, scale=scale,
        )
        optimizer_error = None
    except F1ProfileError as exc:
        bounded_value = None
        optimizer_error = str(exc)

    if bounded_value is None or independent_value is None:
        status = "OPTIMIZATION_INSUFFICIENT"
        difference = None
    else:
        difference = abs(bounded_value - independent_value)
        if independent_boundary:
            status = "OPTIMIZATION_BOUNDARY_SENSITIVE"
        elif difference > float(loglik_tolerance):
            status = "OPTIMIZATION_DISCORDANT"
        else:
            status = "OPTIMIZATION_CONCORDANT"

    return F1NuisanceOptimizerDiagnostic(
        status=status,
        bounded_optimizer_loglik=bounded_value,
        independent_loglik=independent_value,
        absolute_loglik_difference=difference,
        stationary_points=len(roots),
        independent_boundary_sensitive=independent_boundary,
        optimizer_error=optimizer_error,
    )


def f1_profile_nuisance_stability_diagnostic(
    rows: Sequence[Sequence[float]], *, between_variance: float,
    grid_resolutions: Sequence[int] = (241, 481, 961),
    log_spans: Sequence[float] = (30.0, 36.0, 42.0),
    loglik_tolerance: float = 1e-7,
) -> F1NuisanceStabilityDiagnostic:
    """Cross-check nuisance score-root diagnostics across grids and log spans.

    Concordance means only that this finite family of scans found the same
    number of sign-changing stationary roots, no boundary/insufficient status,
    and a sufficiently small spread in the best stationary log-likelihood.
    It cannot detect every even-multiplicity score root or prove globality.
    """
    grids = tuple(grid_resolutions)
    spans = tuple(float(value) for value in log_spans)
    if not grids or any(type(value) is not int or value < 41 for value in grids):
        raise F1ProfileError("NUISANCE_GRID_RESOLUTIONS_MUST_BE_INTEGER_GE_41")
    if not spans or any(not math.isfinite(value) or value <= 0.0 for value in spans):
        raise F1ProfileError("NUISANCE_LOG_SPANS_MUST_BE_FINITE_AND_POSITIVE")
    if (isinstance(loglik_tolerance, bool)
            or not isinstance(loglik_tolerance, (int, float))
            or not math.isfinite(loglik_tolerance) or loglik_tolerance <= 0.0):
        raise F1ProfileError("NUISANCE_LOGLIK_TOLERANCE_MUST_BE_FINITE_AND_POSITIVE")

    configurations = tuple((grid, span) for span in spans for grid in grids)
    results = tuple(
        f1_profile_nuisance_optimizer_diagnostic(
            rows, between_variance=between_variance,
            grid_points=grid, log_span=span,
            loglik_tolerance=float(loglik_tolerance),
        )
        for grid, span in configurations
    )
    counts = tuple(item.stationary_points for item in results)
    statuses = tuple(item.status for item in results)
    values = tuple(
        item.independent_loglik for item in results
        if item.independent_loglik is not None
    )
    spread = max(values) - min(values) if len(values) == len(results) and values else None

    if any(status == "OPTIMIZATION_INSUFFICIENT" for status in statuses):
        status = "OPTIMIZATION_INSUFFICIENT"
    elif any(status == "OPTIMIZATION_BOUNDARY_SENSITIVE" for status in statuses):
        status = "OPTIMIZATION_BOUNDARY_SENSITIVE"
    elif len(set(counts)) != 1:
        status = "OPTIMIZATION_DISCORDANT"
    elif spread is None or spread > float(loglik_tolerance):
        status = "OPTIMIZATION_DISCORDANT"
    elif any(status == "OPTIMIZATION_DISCORDANT" for status in statuses):
        status = "OPTIMIZATION_DISCORDANT"
    else:
        status = "OPTIMIZATION_CONCORDANT"

    return F1NuisanceStabilityDiagnostic(
        status=status,
        configurations=configurations,
        stationary_point_counts=counts,
        optimizer_statuses=statuses,
        maximum_loglik_spread=spread,
    )
