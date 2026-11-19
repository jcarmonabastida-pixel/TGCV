"""Adjudicate F1's floating-point roots against the exact-rational Sturm reference.

This adapter is diagnostic only. It does not alter the optimizer or infer
coefficient uncertainty. ROOTS_AGREE is deliberately withheld when the
independent method finds a multiple root because the legacy F1 diagnostic
does not expose a certified multiplicity for its floating-point candidates.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
from typing import Sequence

from c10s_f1_between_profile_likelihood import (
    F1ProfileError,
    f1_score_polynomial_diagnostic,
)
from c10s_f1_independent_root_isolator import isolate_real_roots


@dataclass(frozen=True)
class F1RootAdjudication:
    status: str
    f1_status: str
    independent_status: str
    f1_root_count: int
    independent_root_count: int
    matched_root_count: int
    multiplicity_review_required: bool
    f1_roots: tuple[float, ...]
    independent_intervals: tuple[tuple[float, float, int], ...]
    reason: str


def adjudicate_f1_roots(
    rows: Sequence[Sequence[float]],
    *,
    between_variance: float,
    match_tolerance: float = 1e-8,
    isolation_width: float = 1e-12,
    max_depth: int = 256,
) -> F1RootAdjudication:
    """Compare the existing F1 reconstruction with independent Sturm isolation.

    The exact-rational method certifies roots of the exact binary-rational
    coefficient values emitted by F1. It does not cover uncertainty in the
    underlying statistical quantities.
    """
    if (isinstance(match_tolerance, bool) or not isinstance(match_tolerance, (int, float))
            or not math.isfinite(match_tolerance) or not (match_tolerance > 0.0)):
        raise F1ProfileError("ROOT_MATCH_TOLERANCE_MUST_BE_POSITIVE")
    if (isinstance(isolation_width, bool) or not isinstance(isolation_width, (int, float))
            or not math.isfinite(isolation_width) or not (isolation_width > 0.0)):
        raise F1ProfileError("ROOT_ISOLATION_WIDTH_MUST_BE_POSITIVE")

    f1 = f1_score_polynomial_diagnostic(
        rows, between_variance=between_variance,
    )
    if f1.status != "POLYNOMIAL_ROOTS_ISOLATED":
        return F1RootAdjudication(
            "ROOTS_UNRESOLVED", f1.status, "NOT_RUN",
            len(f1.positive_roots), 0, 0, False,
            tuple(f1.positive_roots), (), "F1_POLYNOMIAL_DIAGNOSTIC_UNRESOLVED",
        )

    independent = isolate_real_roots(
        f1.coefficients_ascending,
        lower=0,
        max_depth=max_depth,
        max_width=isolation_width,
    )
    intervals = tuple(
        (float(root.lower), float(root.upper), root.multiplicity)
        for root in independent.roots
    )
    if independent.status != "ROOTS_ISOLATED":
        return F1RootAdjudication(
            "ROOTS_UNRESOLVED", f1.status, independent.status,
            len(f1.positive_roots), len(independent.roots), 0, False,
            tuple(f1.positive_roots), intervals, "STURM_REFERENCE_UNRESOLVED",
        )

    candidates = sorted(float(root) for root in f1.positive_roots)
    certified = list(independent.roots)
    used: set[int] = set()
    matched = 0
    for interval in certified:
        midpoint = (float(interval.lower) + float(interval.upper)) / 2.0
        eligible = [
            (abs(value - midpoint), index)
            for index, value in enumerate(candidates)
            if index not in used
            and interval.lower - match_tolerance <= value <= interval.upper + match_tolerance
        ]
        if eligible:
            _, index = min(eligible)
            used.add(index)
            matched += 1

    multiplicity_review = any(root.multiplicity != 1 for root in certified)
    if len(candidates) != len(certified) or matched != len(certified):
        status = "ROOTS_DISCREPANT"
        reason = "ROOT_COUNT_OR_LOCATION_MISMATCH"
    elif multiplicity_review:
        status = "ROOTS_UNRESOLVED"
        reason = "F1_REFERENCE_DOES_NOT_CERTIFY_MULTIPLE_ROOT_MULTIPLICITY"
    else:
        status = "ROOTS_AGREE"
        reason = "ALL_POSITIVE_ROOTS_MATCH_SIMPLE_STURM_ISOLATORS"

    return F1RootAdjudication(
        status, f1.status, independent.status,
        len(candidates), len(certified), matched, multiplicity_review,
        tuple(candidates), intervals, reason,
    )
