"""Numerical F1 profile likelihood for the raw between-world variance.

Research-only alternative to the exact/pivotal C1 interval. The likelihood
ratio cutoff is caller-supplied: this module deliberately does not select or
calibrate it. Grid inversion is diagnostic, not a certified confidence set.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Sequence

from scipy.optimize import minimize_scalar

from c10s_variance_comparison_interface import observed_nested_mr_result


METHOD_ID = "F1_BETWEEN_PROFILE_LIKELIHOOD_0.1"
MODEL_SCOPE = "BALANCED_GAUSSIAN_RANDOM_INTERCEPT"
_LOG2PI = math.log(2.0 * math.pi)


class F1ProfileError(ValueError):
    """Invalid input or numerical profile-likelihood request."""


@dataclass(frozen=True)
class F1ProfileSet:
    likelihood_ratio_cutoff: float
    grid_points: int
    tau_grid: tuple[float, ...]
    profile_loglik: tuple[float, ...]
    mle_tau_grid: float
    max_profile_loglik: float
    accepted_components: tuple[tuple[float, float], ...]
    lower_boundary_included: bool
    upper_grid_truncated: bool
    status: str
    method_id: str = METHOD_ID


def _profile_at_tau(
    tau: float, *, ssw: float, s2_means: float, df_w: int,
    df_b: int, r: int, log_s_bounds: tuple[float, float],
) -> float:
    def negative_loglik(log_s: float) -> float:
        s = math.exp(log_s)
        q = tau + s / r
        if q <= 0.0:
            return math.inf
        value = (
            -0.5 * df_w * (math.log(2.0 * math.pi) + math.log(s))
            -0.5 * ssw / s
            -0.5 * df_b * (math.log(2.0 * math.pi) + math.log(q))
            -0.5 * df_b * s2_means / q
        )
        return -value

    result = minimize_scalar(
        negative_loglik, bounds=log_s_bounds, method="bounded",
        options={"xatol": 1e-11, "maxiter": 1000},
    )
    candidates = [negative_loglik(log_s_bounds[0]),
                  negative_loglik(log_s_bounds[1])]
    if result.success and math.isfinite(result.fun):
        candidates.append(float(result.fun))
    best = min(candidates)
    return -best if math.isfinite(best) else -math.inf


def f1_profile_loglik(
    rows: Sequence[Sequence[float]], *, between_variance: float,
) -> float:
    """Profile log-likelihood at fixed tau>=0, profiling within variance."""
    if isinstance(between_variance, bool) or not isinstance(between_variance, (int, float)):
        raise F1ProfileError("BETWEEN_VARIANCE_MUST_BE_NUMERIC")
    tau = float(between_variance)
    if not math.isfinite(tau) or tau < 0.0:
        raise F1ProfileError("BETWEEN_VARIANCE_MUST_BE_FINITE_AND_NONNEGATIVE")
    observed = observed_nested_mr_result(rows)
    m, r = len(rows), len(rows[0])
    if m < 3:
        raise F1ProfileError("F1_PROFILE_REQUIRES_M_AT_LEAST_3")
    df_w, df_b = m * (r - 1), m - 1
    ssw = observed.within_estimate * df_w
    s2_means = observed.observed_world_variance
    scale = max(observed.within_estimate, s2_means, 1e-12)
    bounds = (math.log(scale) - 28.0, math.log(scale) + 28.0)
    if ssw == 0.0:
        raise F1ProfileError("ZERO_WITHIN_SUM_OF_SQUARES_REQUIRES_SEPARATE_BOUNDARY_MODEL")
    return _profile_at_tau(
        tau, ssw=ssw, s2_means=s2_means, df_w=df_w, df_b=df_b,
        r=r, log_s_bounds=bounds,
    )


def f1_profile_between_confidence_set(
    rows: Sequence[Sequence[float]], *,
    likelihood_ratio_cutoff: float,
    grid_points: int = 401,
    upper_variance: float | None = None,
) -> F1ProfileSet:
    """Invert a caller-cutoff LR rule on a nonnegative tau grid.

    Accepted points satisfy 2*(max_profile_loglik - profile_loglik)<=cutoff.
    Returned components are grid-resolution approximations. No critical value
    is prescribed, no calibration is performed, and endpoint interpolation is
    intentionally omitted pending numerical validation.
    """
    if (isinstance(likelihood_ratio_cutoff, bool)
            or not isinstance(likelihood_ratio_cutoff, (int, float))
            or not math.isfinite(likelihood_ratio_cutoff)
            or likelihood_ratio_cutoff <= 0.0):
        raise F1ProfileError("LR_CUTOFF_MUST_BE_FINITE_AND_POSITIVE")
    if type(grid_points) is not int or grid_points < 51:
        raise F1ProfileError("GRID_POINTS_MUST_BE_INTEGER_GE_51")
    observed = observed_nested_mr_result(rows)
    m, r = len(rows), len(rows[0])
    if m < 3:
        raise F1ProfileError("F1_PROFILE_REQUIRES_M_AT_LEAST_3")
    scale = max(observed.within_estimate, observed.observed_world_variance, 1e-12)
    upper = float(upper_variance) if upper_variance is not None else 10.0 * scale
    if not math.isfinite(upper) or upper <= 0.0:
        raise F1ProfileError("UPPER_VARIANCE_MUST_BE_FINITE_AND_POSITIVE")
    tau_grid = tuple(upper * i / (grid_points - 1) for i in range(grid_points))
    df_w, df_b = m * (r - 1), m - 1
    ssw = observed.within_estimate * df_w
    if ssw == 0.0:
        raise F1ProfileError("ZERO_WITHIN_SUM_OF_SQUARES_REQUIRES_SEPARATE_BOUNDARY_MODEL")
    bounds = (math.log(scale) - 28.0, math.log(scale) + 28.0)
    profile = tuple(_profile_at_tau(
        tau, ssw=ssw, s2_means=observed.observed_world_variance,
        df_w=df_w, df_b=df_b, r=r, log_s_bounds=bounds,
    ) for tau in tau_grid)
    finite = [value for value in profile if math.isfinite(value)]
    if not finite:
        raise F1ProfileError("PROFILE_LIKELIHOOD_NUMERIC_FAILURE")
    maximum = max(finite)
    mle_index = max(range(len(profile)), key=lambda i: profile[i])
    accepted = [
        2.0 * (maximum - value) <= float(likelihood_ratio_cutoff) + 1e-10
        for value in profile
    ]
    components = []
    start = None
    for index, keep in enumerate(accepted + [False]):
        if keep and start is None:
            start = index
        elif not keep and start is not None:
            components.append((tau_grid[start], tau_grid[index - 1]))
            start = None
    lower_included = accepted[0]
    upper_truncated = accepted[-1]
    status = "GRID_SET_UPPER_TRUNCATED" if upper_truncated else (
        "GRID_SET_EMPTY" if not components else "GRID_SET_APPROXIMATION"
    )
    return F1ProfileSet(
        likelihood_ratio_cutoff=float(likelihood_ratio_cutoff),
        grid_points=grid_points, tau_grid=tau_grid, profile_loglik=profile,
        mle_tau_grid=tau_grid[mle_index], max_profile_loglik=maximum,
        accepted_components=tuple(components),
        lower_boundary_included=lower_included,
        upper_grid_truncated=upper_truncated, status=status,
    )
