"""Common immutable-data interface for nested M/R variance comparisons.

This layer computes the shared observed-data targets only. Candidate interval
methods must plug into the typed result without changing the dataset or raw
between-component estimand. It does not run calibration or Monte Carlo studies.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Sequence


class ComparisonInputError(ValueError):
    """Invalid nested M/R comparison input."""


@dataclass(frozen=True)
class VarianceComparisonResult:
    method_id: str
    within_estimate: float
    observed_world_variance: float
    between_estimate_raw: float
    mcse_estimate: float | None
    within_interval: tuple[float, float] | None
    between_interval: tuple[float, float] | None
    mcse_interval: tuple[float, float] | None
    boundary_flags: tuple[str, ...]
    abstention_reason: str | None
    provenance: tuple[tuple[str, str], ...]


def observed_nested_mr_result(
    rows: Sequence[Sequence[float]], *,
    target_m: int | None = None, target_r: int | None = None,
) -> VarianceComparisonResult:
    """Compute common point targets from one immutable rectangular q[m,r] data set.

    Within is the average of unbiased within-world sample variances.
    Between is S²(world means) - within/R and is never truncated.
    The optional MCSE projection is sqrt(between/M* + within/(M*R*)).
    A negative projection returns a typed abstention, not a clipped value.
    """
    matrix = _coerce_matrix(rows)
    m, r = len(matrix), len(matrix[0])
    if (target_m is None) != (target_r is None):
        raise ComparisonInputError("target_m and target_r must be supplied together")
    if target_m is not None:
        if type(target_m) is not int or target_m < 2:
            raise ComparisonInputError("target_m must be an integer >= 2")
        if type(target_r) is not int or target_r < 2:
            raise ComparisonInputError("target_r must be an integer >= 2")

    world_means = [math.fsum(row) / r for row in matrix]
    within_by_world = []
    for row, mean in zip(matrix, world_means):
        ss = math.fsum((value - mean) ** 2 for value in row)
        within_by_world.append(ss / (r - 1))
    within = math.fsum(within_by_world) / m
    mean_of_means = math.fsum(world_means) / m
    world_variance = math.fsum(
        (value - mean_of_means) ** 2 for value in world_means
    ) / (m - 1)
    between_raw = world_variance - within / r

    flags: list[str] = []
    if within == 0.0:
        flags.append("WITHIN_ZERO")
    if between_raw < 0.0:
        flags.append("BETWEEN_NEGATIVE_RAW")
    elif between_raw == 0.0:
        flags.append("BETWEEN_ZERO")

    mcse = None
    abstention = None
    if target_m is not None and target_r is not None:
        projected_variance = between_raw / target_m + within / (target_m * target_r)
        if projected_variance < 0.0:
            abstention = "NONPOSITIVE_PROJECTED_VARIANCE"
        else:
            mcse = math.sqrt(projected_variance)
            if projected_variance == 0.0:
                flags.append("MCSE_ZERO_DEGENERATE")

    return VarianceComparisonResult(
        method_id="RAW_NESTED_MR_COMPONENTS_1.0",
        within_estimate=within,
        observed_world_variance=world_variance,
        between_estimate_raw=between_raw,
        mcse_estimate=mcse,
        within_interval=None,
        between_interval=None,
        mcse_interval=None,
        boundary_flags=tuple(flags),
        abstention_reason=abstention,
        provenance=(
            ("input_shape", f"M={m},R={r}"),
            ("within_definition", "mean_unbiased_within_world_sample_variance"),
            ("between_definition", "sample_variance_world_means_minus_within_over_R"),
            ("truncation", "none"),
        ),
    )


def _coerce_matrix(rows: Sequence[Sequence[float]]) -> tuple[tuple[float, ...], ...]:
    try:
        matrix = tuple(tuple(row) for row in rows)
    except TypeError as exc:
        raise ComparisonInputError("rows must be a rectangular M by R sequence") from exc
    if len(matrix) < 2:
        raise ComparisonInputError("at least two outer worlds are required")
    if not matrix or len(matrix[0]) < 2:
        raise ComparisonInputError("at least two inner observations per world are required")
    width = len(matrix[0])
    for i, row in enumerate(matrix):
        if len(row) != width:
            raise ComparisonInputError(f"ragged input at world index {i}")
        for j, value in enumerate(row):
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ComparisonInputError(f"non-numeric contribution at [{i},{j}]")
            if not math.isfinite(value):
                raise ComparisonInputError(f"non-finite contribution at [{i},{j}]")
    return tuple(tuple(float(value) for value in row) for row in matrix)
