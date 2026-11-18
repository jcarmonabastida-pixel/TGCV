"""Pure nested M/R Monte Carlo precision analysis.

This module consumes already-adjudicated per-assignment metric contributions.
It does not run a DGP, Analyzer, Evaluator, bank builder, or workflow.
"""
from __future__ import annotations

from dataclasses import dataclass
from math import isfinite, sqrt
import numpy as np
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
    method_version: str = "1.2"
    within_world_sampling_mode: str = "UNVERIFIED"
    within_world_sampling_contract_id: str | None = None
    within_world_sampling_contract_version: str | None = None
    within_world_sampling_independence_basis: str | None = None
    outer_world_sampling_contract_id: str | None = None
    outer_world_sampling_contract_version: str | None = None
    outer_world_sampling_independence_basis: str | None = None
    bootstrap_degenerate: bool = False


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
    within_world_sampling_mode: str = "UNVERIFIED",
    within_world_sampling_contract_id: str | None = None,
    within_world_sampling_contract_version: str | None = None,
    within_world_sampling_independence_basis: str | None = None,
    outer_world_sampling_contract_id: str | None = None,
    outer_world_sampling_contract_version: str | None = None,
    outer_world_sampling_independence_basis: str | None = None,
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
    if type(bootstrap_seed) is not int or bootstrap_seed < 0 or bootstrap_seed > (2**64 - 1):
        raise NestedPrecisionError("bootstrap_seed must be an unsigned 64-bit integer")
    if not projections or any(
        type(mm) is not int or type(rr) is not int or mm < 2 or rr < 2
        for mm, rr in projections
    ):
        raise NestedPrecisionError("projection grid must contain integer M>=2 and R>=2 pairs")
    if outer_world_sampling_mode not in {
        "UNVERIFIED", "FIXED_FINITE_SET", "DEPENDENT", "DECLARED_IID_PSEUDORANDOM"
    }:
        raise NestedPrecisionError("unsupported outer-world sampling mode")
    if within_world_sampling_mode not in {
        "UNVERIFIED", "FIXED_FINITE_SET", "DEPENDENT", "DECLARED_IID_PSEUDORANDOM"
    }:
        raise NestedPrecisionError("unsupported within-world replicate sampling mode")
    if outer_world_sampling_mode == "DECLARED_IID_PSEUDORANDOM":
        if not all(
            isinstance(value, str) and value.strip()
            for value in (
                outer_world_sampling_contract_id,
                outer_world_sampling_contract_version,
                outer_world_sampling_independence_basis,
            )
        ):
            raise NestedPrecisionError(
                "declared IID outer-world sampling requires a versioned contract identity"
            )
    elif any(value is not None for value in (
        outer_world_sampling_contract_id,
        outer_world_sampling_contract_version,
        outer_world_sampling_independence_basis,
    )):
        raise NestedPrecisionError(
            "non-IID outer-world modes cannot claim an IID sampling contract identity"
        )
    if within_world_sampling_mode == "DECLARED_IID_PSEUDORANDOM":
        if not all(
            isinstance(value, str) and value.strip()
            for value in (
                within_world_sampling_contract_id,
                within_world_sampling_contract_version,
                within_world_sampling_independence_basis,
            )
        ):
            raise NestedPrecisionError(
                "declared IID within-world sampling requires a versioned contract identity"
            )
    elif any(value is not None for value in (
        within_world_sampling_contract_id,
        within_world_sampling_contract_version,
        within_world_sampling_independence_basis,
    )):
        raise NestedPrecisionError(
            "non-IID within-world modes cannot claim an IID sampling contract identity"
        )
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
    legacy_mcse = getattr(summary_metric, "mcse", None)
    if not is_rmse and observed_mcse is not None and legacy_mcse is not None:
        if (
            isinstance(legacy_mcse, bool)
            or not isinstance(legacy_mcse, (int, float))
            or not isfinite(legacy_mcse)
            or abs(observed_mcse - legacy_mcse) > 1e-10
        ):
            raise NestedPrecisionError(
                "observed MCSE does not reconcile to the legacy outer-world summary"
            )
    status = (
        "INSUFFICIENT_OUTER_SUPPORT" if m < 3
        else "DESCRIPTIVE_ONLY_NO_IID_OUTER_INFERENCE"
        if outer_world_sampling_mode != "DECLARED_IID_PSEUDORANDOM"
        else "DESCRIPTIVE_ONLY_NO_IID_WITHIN_R_INFERENCE"
        if within_world_sampling_mode != "DECLARED_IID_PSEUDORANDOM"
        else "ESTIMABLE_UNDER_DECLARED_SAMPLING"
    )
    # Vectorized implementation of the same ordinary two-stage cluster
    # bootstrap law. Chunking bounds peak memory at O(batch*M*R), while every
    # outer cluster draw (including all-same-source draws) is retained.
    matrix = np.asarray(rows, dtype=np.float64)
    rng = np.random.Generator(np.random.PCG64(bootstrap_seed))
    boot: list[tuple[float, float, float, float]] = []
    boundary = 0
    batch_size = 64
    for start in range(0, bootstrap_replicates, batch_size):
        count = min(batch_size, bootstrap_replicates - start)
        selected_indices = rng.integers(0, m, size=(count, m))
        selected = matrix[selected_indices]
        inner_indices = rng.integers(0, r, size=(count, m, r))
        nested = np.take_along_axis(selected, inner_indices, axis=2)
        world_means = nested.mean(axis=2)
        b_msw_values = nested.var(axis=2, ddof=1).mean(axis=1)
        world_variance_values = world_means.var(axis=1, ddof=1)
        b_between_values = world_variance_values - b_msw_values / r
        sampled_means = nested.mean(axis=(1, 2))
        for b_msw, b_between, world_variance, sampled_mean in zip(
            b_msw_values.tolist(),
            b_between_values.tolist(),
            world_variance_values.tolist(),
            sampled_means.tolist(),
        ):
            boot.append((b_msw, b_between, world_variance, sampled_mean))
        boundary += int(np.count_nonzero(b_between_values < 0.0))
    if not boot:
        raise NestedPrecisionError("bootstrap produced no replicate")

    bootstrap_degenerate = all(
        len({row[index] for row in boot}) == 1 for index in range(4)
    )
    if status == "ESTIMABLE_UNDER_DECLARED_SAMPLING" and bootstrap_degenerate:
        status = "DEGENERATE_BOOTSTRAP_DISTRIBUTION"

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
        boundary_draws = 0
        rmse_nonregular_draws = 0
        for b_msw, b_between, _, sampled_mean_mse in boot:
            # §382.3: never condition the bootstrap distribution on a
            # nonnegative between component. Preserve raw draws and abstain
            # from a regular projection when any draw reaches the boundary.
            if b_between < 0:
                boundary_draws += 1
                continue
            projected_variance = b_between / target_m + b_msw / (target_m * target_r)
            if projected_variance < 0:
                boundary_draws += 1
                continue
            projected_mcse = sqrt(projected_variance)
            if is_rmse:
                # The delta method is non-regular at zero MSE. Do not silently
                # drop such bootstrap draws and report a conditional interval.
                if sampled_mean_mse <= 0:
                    rmse_nonregular_draws += 1
                    continue
                projected_mcse /= 2.0 * sqrt(sampled_mean_mse)
            values.append(projected_mcse)
        if m < 3:
            projection_status = "INSUFFICIENT_OUTER_SUPPORT"
        elif outer_world_sampling_mode != "DECLARED_IID_PSEUDORANDOM":
            projection_status = "DESCRIPTIVE_ONLY_NO_IID_OUTER_INFERENCE"
        elif within_world_sampling_mode != "DECLARED_IID_PSEUDORANDOM":
            projection_status = "DESCRIPTIVE_ONLY_NO_IID_WITHIN_R_INFERENCE"
        elif is_rmse and grand_mean <= 0:
            projection_status = "RMSE_DELTA_NONREGULAR"
        elif bootstrap_degenerate:
            projection_status = "DEGENERATE_BOOTSTRAP_DISTRIBUTION"
        elif len(boot) < bootstrap_replicates * 0.95:
            projection_status = "SENSITIVITY_REQUIRED"
        elif boundary_draws:
            projection_status = "SENSITIVITY_REQUIRED"
        elif rmse_nonregular_draws:
            projection_status = "RMSE_DELTA_NONREGULAR"
        elif len(values) != len(boot):
            projection_status = "SENSITIVITY_REQUIRED"
        else:
            projection_status = status
        if projection_status == "ESTIMABLE_UNDER_DECLARED_SAMPLING":
            projections_out.append((
                target_m, target_r, percentile(values, alpha / 2),
                percentile(values, 1 - alpha / 2), projection_status,
            ))
        else:
            projections_out.append((target_m, target_r, None, None, projection_status))
    return NestedPrecisionResult(
        metric, status, m, r, msw, max(0.0, between_raw), between_raw,
        world_var, observed_mcse, bootstrap_replicates, len(boot),
        boundary / len(boot), intervals, tuple(projections_out),
        within_world_sampling_mode=within_world_sampling_mode,
        within_world_sampling_contract_id=within_world_sampling_contract_id,
        within_world_sampling_contract_version=within_world_sampling_contract_version,
        within_world_sampling_independence_basis=within_world_sampling_independence_basis,
        outer_world_sampling_contract_id=outer_world_sampling_contract_id,
        outer_world_sampling_contract_version=outer_world_sampling_contract_version,
        outer_world_sampling_independence_basis=outer_world_sampling_independence_basis,
        bootstrap_degenerate=bootstrap_degenerate,
    )
