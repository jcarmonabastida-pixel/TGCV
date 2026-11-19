"""Adjudicate F1 roots against the exact-rational Sturm reference.

The comparison is restricted to strictly positive roots. Exact zero roots are
retained separately as boundary diagnostics. Rational Sturm intervals remain
authoritative; no float projection is used for interval comparison or storage.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
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
    independent_intervals: tuple[tuple[str, str, int], ...]
    reason: str
    boundary_roots: tuple[tuple[str, str, int], ...] = ()
    root_domain: str = "(0,+infinity)"


def _q(value: int | float | Fraction) -> Fraction:
    if isinstance(value, bool) or not isinstance(value, (int, float, Fraction)):
        raise F1ProfileError("ROOT_MATCH_VALUES_MUST_BE_REAL")
    if isinstance(value, float):
        if not math.isfinite(value):
            raise F1ProfileError("ROOT_MATCH_VALUES_MUST_BE_FINITE")
        return Fraction.from_float(value)
    return Fraction(value)


def _rational_text(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def _serialize_roots(roots) -> tuple[tuple[str, str, int], ...]:
    return tuple(
        (_rational_text(root.lower), _rational_text(root.upper), root.multiplicity)
        for root in roots
    )


def adjudicate_f1_roots(
    rows: Sequence[Sequence[float]],
    *,
    between_variance: float,
    match_tolerance: float = 1e-8,
    relative_tolerance: float = 1e-8,
    isolation_width: float = 1e-12,
    max_depth: int = 256,
) -> F1RootAdjudication:
    """Compare F1's binary64 roots with exact rational Sturm enclosures.

    Matching uses exact rational arithmetic and a declared mixed tolerance:
    max(absolute_tolerance, relative_tolerance * max(|candidate|, |interval|)).
    A candidate must map uniquely to one isolator and vice versa. The Sturm
    result certifies only the exact binary-rational polynomial supplied by F1.
    """
    for name, value in (
        ("ROOT_MATCH_TOLERANCE", match_tolerance),
        ("ROOT_MATCH_RELATIVE_TOLERANCE", relative_tolerance),
        ("ROOT_ISOLATION_WIDTH", isolation_width),
    ):
        if (isinstance(value, bool) or not isinstance(value, (int, float))
                or not math.isfinite(value) or value <= 0.0):
            raise F1ProfileError(f"{name}_MUST_BE_FINITE_AND_POSITIVE")
    if type(max_depth) is not int or max_depth < 1:
        raise F1ProfileError("ROOT_ISOLATION_MAX_DEPTH_MUST_BE_POSITIVE_INTEGER")

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
    if independent.status != "ROOTS_ISOLATED":
        return F1RootAdjudication(
            "ROOTS_UNRESOLVED", f1.status, independent.status,
            len(f1.positive_roots), len(independent.roots), 0, False,
            tuple(f1.positive_roots), _serialize_roots(independent.roots),
            "STURM_REFERENCE_UNRESOLVED",
        )

    # Sturm's API uses a closed [0,+infinity) domain. Preserve exact zero
    # roots separately, then compare only the strictly-positive subset.
    boundary = tuple(
        root for root in independent.roots
        if root.lower == 0 and root.upper == 0
    )
    certified = tuple(
        root for root in independent.roots
        if not (root.lower == 0 and root.upper == 0)
    )
    intervals = _serialize_roots(certified)
    boundary_intervals = _serialize_roots(boundary)
    candidates = tuple(sorted(float(root) for root in f1.positive_roots))

    if len(candidates) != len(certified):
        return F1RootAdjudication(
            "ROOTS_DISCREPANT", f1.status, independent.status,
            len(candidates), len(certified), 0,
            any(root.multiplicity != 1 for root in certified),
            candidates, intervals, "ROOT_COUNT_MISMATCH",
            boundary_intervals,
        )

    abs_tol = _q(match_tolerance)
    rel_tol = _q(relative_tolerance)
    eligible_by_candidate: list[list[int]] = []
    eligible_by_interval: list[list[int]] = [[] for _ in certified]
    for candidate_index, candidate in enumerate(candidates):
        candidate_q = _q(candidate)
        eligible: list[int] = []
        for interval_index, root in enumerate(certified):
            scale = max(abs(candidate_q), abs(root.lower), abs(root.upper))
            tolerance = max(abs_tol, rel_tol * scale)
            if root.lower - tolerance <= candidate_q <= root.upper + tolerance:
                eligible.append(interval_index)
                eligible_by_interval[interval_index].append(candidate_index)
        eligible_by_candidate.append(eligible)

    # Only a one-to-one singleton correspondence is certifiable. Ambiguous
    # or missing matches are unresolved rather than resolved greedily.
    if (any(len(matches) != 1 for matches in eligible_by_candidate)
            or any(len(matches) != 1 for matches in eligible_by_interval)):
        return F1RootAdjudication(
            "ROOTS_UNRESOLVED", f1.status, independent.status,
            len(candidates), len(certified), 0,
            any(root.multiplicity != 1 for root in certified),
            candidates, intervals,
            "ROOT_MATCHING_NOT_UNIQUELY_IDENTIFIED_UNDER_MIXED_TOLERANCE",
            boundary_intervals,
        )

    matched = len(candidates)
    multiplicity_review = any(root.multiplicity != 1 for root in certified)
    if multiplicity_review:
        status = "ROOTS_UNRESOLVED"
        reason = "F1_REFERENCE_DOES_NOT_CERTIFY_MULTIPLE_ROOT_MULTIPLICITY"
    else:
        status = "ROOTS_AGREE"
        reason = "ALL_STRICTLY_POSITIVE_ROOTS_MATCH_SIMPLE_STURM_ISOLATORS"

    return F1RootAdjudication(
        status, f1.status, independent.status,
        len(candidates), len(certified), matched, multiplicity_review,
        candidates, intervals, reason, boundary_intervals,
    )
