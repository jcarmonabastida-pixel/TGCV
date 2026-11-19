"""Independent finite-sample Gaussian variance-component oracles.

Development comparator only. This module does not alter or replace the
production nested bootstrap or protocol-v002 scoring.
"""
from __future__ import annotations

from dataclasses import dataclass
import math

from scipy.optimize import minimize_scalar
from scipy.stats import chi2


class GaussianOracleError(ValueError):
    """Invalid sufficient statistics or target projection."""


@dataclass(frozen=True)
class GaussianVarianceReference:
    within_interval: tuple[float, float]
    tau_interval: tuple[float, float]
    between_raw_conservative_interval: tuple[float, float]
    within_df: int
    between_df: int


def gaussian_f1_reference(
    *, m: int, r: int, msw: float, world_mean_variance: float,
    confidence: float = 0.95,
) -> GaussianVarianceReference:
    """Exact within pivot and Bonferroni joint-pivot between reference.

    world_mean_variance is the unbiased sample variance of the M world means.
    The between interval is deliberately left untruncated; it is a conservative
    interval for sigma_between^2, not a nonnegative convenience estimate.
    """
    _validate(m, r, msw, world_mean_variance, confidence)
    df_w = m * (r - 1)
    df_b = m - 1
    alpha = 1.0 - confidence
    # Bonferroni: each two-sided marginal interval has error alpha/2.
    tail = alpha / 4.0
    # The two marginal intervals must each have error alpha/2 for the
    # joint Bonferroni coverage to be at least 1-alpha.
    within = (
        df_w * msw / chi2.ppf(1.0 - tail, df_w),
        df_w * msw / chi2.ppf(tail, df_w),
    )
    tau = (
        df_b * world_mean_variance / chi2.ppf(1.0 - tail, df_b),
        df_b * world_mean_variance / chi2.ppf(tail, df_b),
    )
    between = (tau[0] - within[1] / r, tau[1] - within[0] / r)
    return GaussianVarianceReference(within, tau, between, df_w, df_b)


def _validate(m, r, msw, world_mean_variance, confidence):
    if type(m) is not int or m < 3:
        raise GaussianOracleError("m must be an integer >= 3")
    if type(r) is not int or r < 2:
        raise GaussianOracleError("r must be an integer >= 2")
    for name, value in (("msw", msw), ("world_mean_variance", world_mean_variance)):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise GaussianOracleError(f"{name} must be finite and nonnegative")
        if not math.isfinite(value) or value < 0:
            raise GaussianOracleError(f"{name} must be finite and nonnegative")
    if not isinstance(confidence, (int, float)) or not 0.0 < confidence < 1.0:
        raise GaussianOracleError("confidence must lie strictly between 0 and 1")


def _loglik_from_sufficient(
    variance_within: float, tau: float, *, ss_within: float,
    ss_world_means: float, df_within: int, df_between: int,
) -> float:
    if variance_within <= 0.0 or tau <= 0.0:
        return -math.inf
    return (
        -0.5 * df_within * math.log(variance_within)
        - ss_within / (2.0 * variance_within)
        - 0.5 * df_between * math.log(tau)
        - ss_world_means / (2.0 * tau)
    )


def gaussian_constrained_loglik(
    *, m: int, r: int, msw: float, world_mean_variance: float,
    variance_within: float, variance_between: float,
) -> float:
    """Gaussian random-intercept log likelihood, omitting constants."""
    _validate(m, r, msw, world_mean_variance, 0.95)
    if variance_within <= 0 or variance_between < 0:
        return -math.inf
    tau = variance_between + variance_within / r
    return _loglik_from_sufficient(
        variance_within, tau,
        ss_within=m * (r - 1) * msw,
        ss_world_means=(m - 1) * world_mean_variance,
        df_within=m * (r - 1), df_between=m - 1,
    )


def gaussian_constrained_mle(
    *, m: int, r: int, msw: float, world_mean_variance: float,
) -> tuple[float, float, float]:
    """Return (sigma2_within_hat, sigma2_between_hat, maximized loglik)."""
    _validate(m, r, msw, world_mean_variance, 0.95)
    if msw <= 0 or world_mean_variance <= 0:
        raise GaussianOracleError("profile likelihood currently requires positive sufficient statistics")
    df_w, df_b = m * (r - 1), m - 1
    ss_w, ss_b = df_w * msw, df_b * world_mean_variance
    tau_unconstrained = world_mean_variance
    if tau_unconstrained >= msw / r:
        ll = _loglik_from_sufficient(
            msw, tau_unconstrained, ss_within=ss_w,
            ss_world_means=ss_b, df_within=df_w, df_between=df_b,
        )
        return msw, tau_unconstrained - msw / r, ll
    # The constrained maximum lies on sigma_between^2 = 0, tau = sigma_within/R.
    within = (ss_w + r * ss_b) / (df_w + df_b)
    tau = within / r
    ll = _loglik_from_sufficient(
        within, tau, ss_within=ss_w, ss_world_means=ss_b,
        df_within=df_w, df_between=df_b,
    )
    return within, 0.0, ll


def gaussian_profile_loglik_mcse(
    *, m: int, r: int, msw: float, world_mean_variance: float,
    target_m: int, target_r: int, mcse: float,
) -> float:
    """Profile log likelihood for MCSE, respecting sigma_between^2 >= 0.

    Returns -inf for an infeasible/nonpositive target. Constants common to
    candidate MCSE values are omitted. No Wilks cutoff is asserted here.
    """
    _validate(m, r, msw, world_mean_variance, 0.95)
    if type(target_m) is not int or target_m < 2:
        raise GaussianOracleError("target_m must be an integer >= 2")
    if type(target_r) is not int or target_r < 2:
        raise GaussianOracleError("target_r must be an integer >= 2")
    if not isinstance(mcse, (int, float)) or not math.isfinite(mcse) or mcse <= 0:
        return -math.inf
    if msw <= 0 or world_mean_variance <= 0:
        raise GaussianOracleError("profile likelihood currently requires positive sufficient statistics")

    df_w, df_b = m * (r - 1), m - 1
    ss_w, ss_b = df_w * msw, df_b * world_mean_variance
    target_variance = target_m * mcse * mcse
    # tau = target_variance - sigma_w^2*(1/R* - 1/R).
    coefficient = (1.0 / target_r) - (1.0 / r)
    upper = target_variance * target_r
    if upper <= 0:
        return -math.inf

    def objective(within):
        tau = target_variance - within * coefficient
        if within <= 0 or tau <= 0 or tau < within / r:
            return math.inf
        ll = _loglik_from_sufficient(
            within, tau, ss_within=ss_w, ss_world_means=ss_b,
            df_within=df_w, df_between=df_b,
        )
        return -ll

    result = minimize_scalar(
        objective, bounds=(max(upper * 1e-12, 1e-300), upper),
        method="bounded", options={"xatol": max(upper * 1e-10, 1e-14)},
    )
    candidates = [objective(result.x), objective(upper)]
    finite = [value for value in candidates if math.isfinite(value)]
    return -min(finite) if finite else -math.inf


def gaussian_mcse_profile_lr(
    *, m: int, r: int, msw: float, world_mean_variance: float,
    target_m: int, target_r: int, mcse: float,
) -> float:
    """Profile likelihood-ratio statistic; its cutoff must be calibrated."""
    _, _, maximum = gaussian_constrained_mle(
        m=m, r=r, msw=msw, world_mean_variance=world_mean_variance,
    )
    profile = gaussian_profile_loglik_mcse(
        m=m, r=r, msw=msw, world_mean_variance=world_mean_variance,
        target_m=target_m, target_r=target_r, mcse=mcse,
    )
    if not math.isfinite(profile):
        return math.inf
    return max(0.0, 2.0 * (maximum - profile))
