"""F1-only exact/pivotal candidate for the shared nested M/R comparator.

Additive research candidate. Does not modify the production Analyzer, protocol
v002, or the frozen Tier-A baseline. No simulation or calibration is performed.
"""
from __future__ import annotations

from dataclasses import replace
import math
from typing import Sequence

from scipy.stats import chi2

from c10s_variance_comparison_interface import (
    ComparisonInputError,
    VarianceComparisonResult,
    observed_nested_mr_result,
)


METHOD_ID = "C1_F1_EXACT_PIVOTAL_1.0"
MODEL_SCOPE = "F1_BALANCED_GAUSSIAN_RANDOM_INTERCEPT"


class F1PivotalError(ValueError):
    """Invalid F1 candidate input or confidence-set construction."""


def _interval(scale: float, df: int, tail: float) -> tuple[float, float]:
    if scale == 0.0:
        return (0.0, 0.0)
    return (
        df * scale / float(chi2.ppf(1.0 - tail, df)),
        df * scale / float(chi2.ppf(tail, df)),
    )


def _joint_region_vertices(
    tau_interval: tuple[float, float],
    within_interval: tuple[float, float],
    observed_r: int,
) -> tuple[tuple[float, float], ...]:
    """Vertices of rectangle intersected with tau >= within/R and within>=0."""
    tl, tu = tau_interval
    wl, wu = within_interval
    candidates = {
        (tl, wl), (tl, wu), (tu, wl), (tu, wu),
        (tl, observed_r * tl), (tu, observed_r * tu),
        (wl / observed_r, wl), (wu / observed_r, wu),
    }
    feasible = []
    for tau, within in candidates:
        if (
            math.isfinite(tau) and math.isfinite(within)
            and tl - 1e-12 <= tau <= tu + 1e-12
            and wl - 1e-12 <= within <= wu + 1e-12
            and within >= -1e-12
            and tau >= within / observed_r - 1e-12
        ):
            point = (max(0.0, tau), max(0.0, within))
            if point not in feasible:
                feasible.append(point)
    return tuple(feasible)


def f1_exact_pivotal_result(
    rows: Sequence[Sequence[float]], *,
    target_m: int, target_r: int, family: str,
    confidence_level: float = 0.95,
) -> VarianceComparisonResult:
    """Return exact within, conservative raw-between and joint-set MCSE intervals.

    Exactness is restricted to independent, balanced Gaussian random-intercept
    F1 data. The raw between estimate and interval are never clipped. MCSE is
    obtained by projecting one Bonferroni joint confidence region onto the
    target functional; no Wilks cutoff or bootstrap B is involved.
    """
    if family != "F1":
        raise F1PivotalError("C1_F1_ONLY_METHOD_REJECTS_NON_F1_FAMILY")
    if type(target_m) is not int or target_m < 2:
        raise F1PivotalError("target_m must be an integer >= 2")
    if type(target_r) is not int or target_r < 2:
        raise F1PivotalError("target_r must be an integer >= 2")
    if (
        isinstance(confidence_level, bool)
        or not isinstance(confidence_level, (int, float))
        or not math.isfinite(confidence_level)
        or not 0.0 < confidence_level < 1.0
    ):
        raise F1PivotalError("confidence_level must lie strictly between 0 and 1")

    observed = observed_nested_mr_result(rows, target_m=target_m, target_r=target_r)
    m, r = len(rows), len(rows[0])
    if m < 3:
        raise F1PivotalError("F1 exact/pivotal candidate requires M >= 3")
    df_w, df_b = m * (r - 1), m - 1
    alpha = 1.0 - float(confidence_level)

    # Reconstruct sufficient statistics from the common, immutable-data result.
    msw = observed.within_estimate
    s2_world_means = observed.observed_world_variance
    if msw < 0.0 or s2_world_means < 0.0:
        raise F1PivotalError("NEGATIVE_SUFFICIENT_STATISTIC")

    within_exact = _interval(msw, df_w, alpha / 2.0)
    # Each marginal interval has error alpha/2; their intersection has
    # simultaneous coverage >= 1-alpha by Bonferroni.
    tail_joint = alpha / 4.0
    within_joint = _interval(msw, df_w, tail_joint)
    tau_joint = _interval(s2_world_means, df_b, tail_joint)
    between_raw = (
        tau_joint[0] - within_joint[1] / r,
        tau_joint[1] - within_joint[0] / r,
    )

    vertices = _joint_region_vertices(tau_joint, within_joint, r)
    mcse_interval = None
    abstention = None
    flags = list(observed.boundary_flags)
    if not vertices:
        abstention = "EMPTY_FEASIBLE_JOINT_CONFIDENCE_SET"
    else:
        coefficient = (1.0 / target_r) - (1.0 / r)
        projected = [
            (tau + within * coefficient) / target_m
            for tau, within in vertices
        ]
        low2, high2 = min(projected), max(projected)
        if low2 < -1e-10 or high2 < -1e-10:
            abstention = "PROFILE_PROJECTION_NUMERICAL_FAILURE"
        else:
            mcse_interval = (
                math.sqrt(max(0.0, low2)),
                math.sqrt(max(0.0, high2)),
            )
            if any(
                abs(tau - within / r) <= 1e-10 * max(1.0, abs(tau), abs(within))
                for tau, within in vertices
            ):
                flags.append("JOINT_SET_TOUCHED_BETWEEN_ZERO_BOUNDARY")

    provenance = observed.provenance + (
        ("method_id", METHOD_ID),
        ("model_scope", MODEL_SCOPE),
        ("confidence_level", format(float(confidence_level), ".17g")),
        ("within_df", str(df_w)),
        ("between_df", str(df_b)),
        ("MSW", format(msw, ".17g")),
        ("S2bar", format(s2_world_means, ".17g")),
        ("raw_between_interval", repr(between_raw)),
        ("joint_tau_interval", repr(tau_joint)),
        ("joint_within_interval", repr(within_joint)),
        ("joint_region_vertices", repr(vertices)),
        ("target_Mstar", str(target_m)),
        ("target_Rstar", str(target_r)),
        ("joint_region", "BONFERRONI_RECTANGLE_INTERSECT_PHYSICAL_PARAMETER_SPACE"),
    )
    return replace(
        observed,
        method_id=METHOD_ID,
        within_interval=within_exact,
        between_interval=between_raw,
        mcse_interval=mcse_interval,
        boundary_flags=tuple(flags),
        abstention_reason=abstention,
        provenance=provenance,
    )
