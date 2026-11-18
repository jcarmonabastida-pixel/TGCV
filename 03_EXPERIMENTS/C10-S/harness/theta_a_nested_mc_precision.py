"""Pure nested M/R Monte Carlo precision analysis.

This module consumes already-adjudicated per-assignment metric contributions.
It does not run a DGP, Analyzer, Evaluator, bank builder, or workflow.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, sqrt
import random
from statistics import mean, stdev
from typing import Mapping, Sequence


class NestedPrecisionError(ValueError):
    """Invalid nested contribution data or projection request."""


@dataclass(frozen=True)
class NestedPrecisionResult:
    metric: str
    status: str
    m_observed: int
    r_observed: int
    within_ms: float | None
    between_ms: float | None
    between_raw: float | None
    observed_world_mean_variance: float | None
    observed_mcse: float | None
    bootstrap_replicates: int
    valid_bootstrap_replicates: int
    boundary_fraction: float | None
    component_intervals: tuple[tuple[str, float, float], ...]
    projections: tuple[tuple[int, int, float | None, float | None, str], ...]
    method_id: str = "TGCV_NESTED_MR_BOOTSTRAP"
    method_version: str = "1.0"


def _finite_rows(rows: Sequence[Sequence[float]]) -> tuple[tuple[float, ...], ...]:
    if not rows or len(rows) < 2:
        raise NestedPrecisionError("at least two outer worlds are required")
    normalized = tuple(tuple(row) for row in rows)
    if any(not row for row in normalized):
        raise NestedPrecisionError("every outer world must contain at least one R contribution")
    sizes = {len(row) for row in normalized}
    if len(sizes) != 1 or next(iter(sizes)) < 2:
        raise NestedPrecisionError("balanced nested design requires the same R>=2 in every world")
    if any(isinstance(x, bool) or not isinstance(x, (int, float)) or not isfinite(x)
           for row in normalized for x in row):
        raise NestedPrecisionError("all replicate contributions must be finite real numbers")
    return normalized


def _components(rows: Sequence[Sequence[float]]) -> tuple[float, float, float, float]:
    m, r = len(rows), len(rows[0])
    world_means = tuple(mean(row) for row in rows)
    grand_mean = mean(world_means)
    msw = sum(sum((x - mean(row)) ** 2 for x in row) / (r - 1)
              for row in rows) / m
    msb = r * sum((x - grand_mean) ** 2 for x in world_means) / (m - 1)
    between_raw = (msb - msw) / r
    world_mean_variance = stdev(world_means) ** 2
    return msw, msb, between_raw, world_mean_variance


def analyze_nested_precision(
    *,
    metric: str,
    replicate_contributions: Sequence[Sequence[float]],
    summary_metric,
    outer_world_sampling_mode: str,
    projections: Sequence[tuple[int, int]],
    bootstrap_replicates: int = 2000,
    bootstrap_seed: int = 0,
) -> NestedPrecisionResult:
    """Estimate nested variance components and bootstrap their M/R projections.

    The caller must supply the exact scalar q_mr for each complete R record,
    in the same world order as summary_metric.outer_world_contributions.
    No missing/NOT_EVALUABLE contribution may be dropped or imputed.
    """
    if not isinstance(metric, str) or not metric.strip():
        raise NestedPrecisionError("metric identity is required")
    rows = _finite_rows(replicate_contributions)
    m, r = len(rows), len(rows[0])
    if type(bootstrap_replicates) is not int or bootstrap_replicates < 100:
        raise NestedPrecisionError("bootstrap_replicates must be an integer >=100")
    if type(bootstrap_seed) is not int:
        raise NestedPrecisionError("bootstrap_seed must be an exact integer")
    if not projections or any(
        type(mm) is not int or type(rr) is not int or mm < 2 or rr < 2
        for mm, rr in projections
    ):
        raise NestedPrecisionError("projection grid must contain integer M>=2 and R>=2 pairs")
    if getattr(summary_metric, "metric", None) != metric:
        raise NestedPrecisionError("summary metric identity does not match replicate contributions")
    summary_rows = tuple(getattr(summary_metric, "outer_world_contributions", ()))
    if len(summary_rows) != m:
        raise NestedPrecisionError("summary must contain one outer contribution per supplied world")
    for index, (world_id, expected_mean) in enumerate(summary_rows):
        if not isinstance(world_id, str) or not world_id:
            raise NestedPrecisionError("summary world identities must be nonempty")
        if not isfinite(expected_mean) or abs(mean(rows[index]) - expected_mean) > 1e-10:
            raise NestedPrecisionError("within-world R contributions do not reconcile to legacy summary")
    grand_mean = mean(mean(row) for row in rows)
    is_rmse = metric == "point_rmse"
    reported_mean = sqrt(grand_mean) if is_rmse else grand_mean
    if getattr(summary_metric, "mean", None) is not None:
        if abs(reported_mean - summary_metric.mean) > 1e-10:
            raise NestedPrecisionError("grand mean does not reconcile to legacy summary")

    msw, msb, between_raw, world_var = _components(rows)
    observed_mcse = (
        getattr(summary_metric, "mcse", None) if is_rmse
        else sqrt(world_var / m) if outer_world_sampling_mode == "DECLARED_IID_PSEUDORANDOM"
        else None
    )
    status = (
        "INSUFFICIENT_OUTER_SUPPORT" if m < 3
        else "DESCRIPTIVE_ONLY" if outer_world_sampling_mode != "DECLARED_IID_PSEUDORANDOM"
        else "ESTIMABLE_UNDER_DECLARED_SAMPLING"
    )
    rng = random.Random(bootstrap_seed)
    boot: list[tuple[float, float, float, float]] = []
    boundary = 0
    for _ in range(bootstrap_replicates):
        selected_indices = [rng.randrange(m) for _ in range(m)]
        if len(set(selected_indices)) < 2:
            continue
        selected = [rows[index] for index in selected_indices]
        nested = tuple(tuple(row[rng.randrange(r)] for _ in range(r)) for row in selected)
        b_msw, _, b_between, _ = _components(nested)
        boot.append((b_msw, b_between, b_between + b_msw / r, mean(mean(row) for row in nested)))
        boundary += b_between < 0.0
    if not boot:
        raise NestedPrecisionError("bootstrap produced no replicate with at least two distinct outer worlds")

    def percentile(values: Sequence[float], probability: float) -> float:
        ordered = sorted(values)
        position = (len(ordered) - 1) * probability
        lower = int(position)
        upper = min(lower + 1, len(ordered) - 1)
        fraction = position - lower
        return ordered[lower] * (1.0 - fraction) + ordered[upper] * fraction

    alpha = 0.05
    intervals = tuple(
        (name, percentile([row[index] for row in boot], alpha / 2),
         percentile([row[index] for row in boot], 1 - alpha / 2))
        for name, index in (("within_ms", 0), ("between_raw", 1), ("world_mean_variance", 2))
    )
    projections_out = []
    for target_m, target_r in projections:
        values = []
        for b_msw, b_between, _, sampled_mean_mse in boot:
            if b_between < 0:
                continue
            projected_variance = b_between / target_m + b_msw / (target_m * target_r)
            projected_mcse = sqrt(projected_variance)
            if is_rmse:
                if sampled_mean_mse <= 0:
                    continue
                projected_mcse /= 2.0 * sqrt(sampled_mean_mse)
            values.append(projected_mcse)
        if m < 3:
            projections_out.append((target_m, target_r, None, None, "INSUFFICIENT_OUTER_SUPPORT"))
        elif len(values) < bootstrap_replicates * 0.95:
            projections_out.append((target_m, target_r, None, None, "SENSITIVITY_REQUIRED"))
        else:
            projections_out.append((
                target_m, target_r, percentile(values, alpha / 2),
                percentile(values, 1 - alpha / 2), status,
            ))
    return NestedPrecisionResult(
        metric, status, m, r, msw, max(0.0, between_raw), between_raw,
        world_var, observed_mcse, bootstrap_replicates, len(boot),
        boundary / len(boot), intervals, tuple(projections_out),
    )
