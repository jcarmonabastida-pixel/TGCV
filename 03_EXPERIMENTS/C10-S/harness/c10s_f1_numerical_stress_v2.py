"""Successor numerical stress design v002.

This module composes the frozen v001 fixture roster and solver APIs. It is
side-effect free on import. The callable runners execute numerical work only
when explicitly invoked by a separately authorized CLI.
"""
from __future__ import annotations

from fractions import Fraction
import math
from typing import Any

from c10s_f1_numerical_stress import (
    GENERATOR_VERSION as V1_GENERATOR_VERSION,
    SCALE_EXPONENTS,
    ISOLATION_WIDTHS,
    ISOLATION_DEPTHS,
    PolynomialFixture,
    build_polynomial_fixtures,
    run_polynomial_stress_grid,
    _domain_for,
    _float_vector,
)
from c10s_f1_independent_root_isolator import isolate_real_roots

Q = Fraction
GENERATOR_VERSION = "C10S_F1_NUMERICAL_STRESS_GENERATOR_002"
N4_EXponents = (-100, -50, -20, 0, 20, 24, 28, 32, 36, 40, 44, 48, 50, 100)


def _qtext(value: Q) -> str:
    return f"{value.numerator}/{value.denominator}"


def _root_payload(result: Any) -> list[dict[str, Any]]:
    return [
        {
            "lower": _qtext(root.lower),
            "upper": _qtext(root.upper),
            "multiplicity": root.multiplicity,
            "distinct_root_count": root.distinct_root_count,
        }
        for root in result.roots
    ]


def _isolate(coefficients: tuple[Q, ...], lower: Q, upper: Q,
             width: Q, depth: int) -> Any:
    return isolate_real_roots(
        coefficients, lower=lower, upper=upper,
        max_width=width, max_depth=depth,
    )


def _topology_comparison(ideal: Any, represented: Any) -> tuple[str, str]:
    if ideal.status != "ROOTS_ISOLATED" or represented.status != "ROOTS_ISOLATED":
        return "UNRESOLVED", "ONE_OR_BOTH_EXACT_RATIONAL_ISOLATIONS_INCOMPLETE"
    ideal_mult = tuple(root.multiplicity for root in ideal.roots)
    represented_mult = tuple(root.multiplicity for root in represented.roots)
    if len(ideal.roots) != len(represented.roots) or ideal_mult != represented_mult:
        return "CHANGED", "DISTINCT_ROOT_COUNT_OR_MULTIPLICITY_STRUCTURE_CHANGED"
    return "PRESERVED", "ROOT_COUNT_AND_ORDERED_MULTIPLICITY_STRUCTURE_MATCH"


def _annotate_topology(record: dict[str, Any], fixture: PolynomialFixture) -> dict[str, Any]:
    width = Q(record["max_width"])
    depth = int(record["max_depth"])
    lower_text, upper_text = record["domain"]
    lower, upper = Q(lower_text), Q(upper_text)
    ideal = _isolate(fixture.ideal_coefficients, lower, upper, width, depth)
    if not record["binary64_representable"]:
        record.update({
            "ideal_sturm_status": ideal.status,
            "ideal_sturm_roots": _root_payload(ideal),
            "represented_sturm_status": "REPRESENTATION_UNRESOLVED",
            "represented_sturm_roots": [],
            "topology_comparison_status": "UNRESOLVED",
            "topology_comparison_reason": "BINARY64_COEFFICIENT_REPRESENTATION_LOST",
        })
        return record
    represented_coefficients = tuple(
        Q.from_float(float.fromhex(value)) for value in record["binary64_hex"]
    )
    represented = _isolate(represented_coefficients, lower, upper, width, depth)
    status, reason = _topology_comparison(ideal, represented)
    record.update({
        "ideal_sturm_status": ideal.status,
        "ideal_sturm_roots": _root_payload(ideal),
        "represented_sturm_status": represented.status,
        "represented_sturm_roots": _root_payload(represented),
        "topology_comparison_status": status,
        "topology_comparison_reason": reason,
    })
    return record


def _fixture_map() -> dict[str, PolynomialFixture]:
    return {fixture.fixture_id: fixture for fixture in build_polynomial_fixtures()}


def run_polynomial_stress_v2() -> dict[str, Any]:
    """Run the historical 115-record grid with explicit topology comparison."""
    v1 = run_polynomial_stress_grid()
    fixtures = _fixture_map()
    records: list[dict[str, Any]] = []
    for original in v1["records"]:
        record = dict(original)
        fixture_id = str(record["fixture_id"])
        fixture = fixtures[fixture_id]
        records.append(_annotate_topology(record, fixture))
    status_counts: dict[str, int] = {}
    for record in records:
        key = str(record["topology_comparison_status"])
        status_counts[key] = status_counts.get(key, 0) + 1
    return {
        "generator_version": GENERATOR_VERSION,
        "execution_performed": True,
        "scientific_execution": False,
        "historical_v1_fixture_grid_reused": True,
        "record_count": len(records),
        "topology_comparison_counts": status_counts,
        "sturm_status_counts": v1["sturm_status_counts"],
        "records": records,
    }


def run_n3_covariant_lane() -> dict[str, Any]:
    """Run a separate variable-scale lane with covariant domain and width."""
    fixtures = _fixture_map()
    base = fixtures["N3_BASE"]
    base_lower, base_upper = _domain_for(base)
    base_width = Q(1, 10**12)
    base_depth = 256
    base_binary64 = _float_vector(base.ideal_coefficients)
    if base_binary64 is None:
        raise ArithmeticError("N3_BASE_REPRESENTATION_UNRESOLVED")
    base_represented = tuple(Q.from_float(value) for value in base_binary64)
    base_reference = _isolate(
        base_represented, base_lower, base_upper, base_width, base_depth,
    )
    records: list[dict[str, Any]] = []
    for exponent in SCALE_EXPONENTS:
        fixture_id = f"N3_BASE_VARIABLE_SCALE_2^{exponent}"
        fixture = fixtures[fixture_id]
        factor = Q(2) ** exponent
        lower, upper = base_lower * factor, base_upper * factor
        width = base_width * factor
        actual = fixture.coefficient_override or fixture.ideal_coefficients
        binary64 = _float_vector(actual)
        record: dict[str, Any] = {
            "lane": "N3_COVARIANT",
            "fixture_id": fixture_id,
            "exponent": exponent,
            "ideal_coefficients": [_qtext(v) for v in fixture.ideal_coefficients],
            "domain_transformed": [_qtext(lower), _qtext(upper)],
            "max_width_transformed": _qtext(width),
            "max_depth": base_depth,
            "binary64_representable": binary64 is not None,
        }
        if binary64 is None:
            record.update({
                "sturm_status": "REPRESENTATION_UNRESOLVED",
                "inverse_mapped_intervals": [],
                "topology_comparison_status": "UNRESOLVED",
            })
        else:
            represented = tuple(Q.from_float(v) for v in binary64)
            ideal_result = _isolate(fixture.ideal_coefficients, lower, upper, width, base_depth)
            represented_result = _isolate(represented, lower, upper, width, base_depth)
            topology, reason = _topology_comparison(ideal_result, represented_result)
            inverse = Q(1, 1) / factor
            record.update({
                "sturm_status": represented_result.status,
                "ideal_sturm_status": ideal_result.status,
                "ideal_sturm_roots": _root_payload(ideal_result),
                "represented_sturm_roots": _root_payload(represented_result),
                "topology_comparison_status": topology,
                "topology_comparison_reason": reason,
                "inverse_mapped_intervals": [
                    {
                        "lower": _qtext(root.lower * inverse),
                        "upper": _qtext(root.upper * inverse),
                        "multiplicity": root.multiplicity,
                    }
                    for root in represented_result.roots
                ],
            })
            if (
                base_reference.status != "ROOTS_ISOLATED"
                or represented_result.status != "ROOTS_ISOLATED"
            ):
                record["base_equivariance_status"] = "UNRESOLVED"
                record["base_equivariance_reason"] = "BASE_OR_TRANSFORMED_ISOLATION_INCOMPLETE"
            else:
                mapped = [
                    (root.lower * inverse, root.upper * inverse, root.multiplicity)
                    for root in represented_result.roots
                ]
                base_roots = [
                    (root.lower, root.upper, root.multiplicity)
                    for root in base_reference.roots
                ]
                same_count = len(mapped) == len(base_roots)
                same_multiplicity = (
                    same_count
                    and tuple(item[2] for item in mapped)
                    == tuple(item[2] for item in base_roots)
                )
                intervals_overlap = (
                    same_count
                    and all(
                        max(left[0], right[0]) <= min(left[1], right[1])
                        for left, right in zip(mapped, base_roots)
                    )
                )
                passed = same_count and same_multiplicity and intervals_overlap
                record["base_equivariance_status"] = "PASS" if passed else "FAIL"
                record["base_equivariance_reason"] = (
                    "INVERSE_MAPPED_INTERVALS_MATCH_BASE"
                    if passed else "ROOT_COUNT_MULTIPLICITY_OR_INTERVAL_MATCH_FAILED"
                )
        records.append(record)
    return {
        "generator_version": GENERATOR_VERSION,
        "execution_performed": True,
        "scientific_execution": False,
        "lane": "N3_COVARIANT",
        "scale_exponents": list(SCALE_EXPONENTS),
        "base_domain": [_qtext(base_lower), _qtext(base_upper)],
        "base_max_width": _qtext(base_width),
        "max_depth": base_depth,
        "record_count": len(records),
        "records": records,
    }


def run_f1_observation_scale_ladder_v2() -> dict[str, Any]:
    """Run the fixed 14-scale N4 ladder, retaining every pipeline stage."""
    from c10s_f1_between_profile_likelihood import (
        f1_profile_between_confidence_set,
        f1_score_polynomial_diagnostic,
    )
    from c10s_f1_root_adjudication import adjudicate_f1_roots

    rows = (
        (0.0, 1.0, 2.0, 1.0),
        (1.0, 2.0, 3.0, 2.0),
        (2.0, 3.0, 4.0, 3.0),
        (3.0, 4.0, 5.0, 4.0),
    )
    tau = 0.25
    records: list[dict[str, Any]] = []
    for exponent in N4_EXponents:
        factor = math.ldexp(1.0, exponent)
        scaled_rows = tuple(tuple(factor * value for value in row) for row in rows)
        scaled_tau = tau * factor * factor
        record: dict[str, Any] = {
            "exponent": exponent,
            "observation_scale": f"2^{exponent}",
            "scale_factor_hex": factor.hex(),
            "variance_scale": f"2^{2 * exponent}",
        }
        try:
            profile = f1_profile_between_confidence_set(
                scaled_rows, likelihood_ratio_cutoff=3.841458820694124,
            )
            diagnostic = f1_score_polynomial_diagnostic(
                scaled_rows, between_variance=scaled_tau,
            )
            adjudication = adjudicate_f1_roots(
                scaled_rows, between_variance=scaled_tau,
            )
            low, high = profile.confidence_components[0]
            inverse = math.ldexp(1.0, -2 * exponent)
            record.update({
                "record_status": "RETURNED",
                "profile_status": profile.status,
                "profile_loglik": profile.max_profile_loglik,
                "mle_base_variance": profile.mle_between_variance * inverse,
                "lr_lower_base_variance": low * inverse,
                "lr_upper_base_variance": high * inverse,
                "score_polynomial_status": diagnostic.status,
                "score_polynomial_degree": diagnostic.degree,
                "score_polynomial_roots_base_variance": [
                    value * inverse for value in diagnostic.positive_roots
                ],
                "sturm_status": adjudication.independent_status,
                "adjudication_status": adjudication.status,
                "adjudication_reason": adjudication.reason,
            })
        except (ArithmeticError, OverflowError, ValueError) as exc:
            record.update({
                "record_status": "FAIL_CLOSED_EXCEPTION",
                "exception": type(exc).__name__ + ":" + str(exc),
            })
        records.append(record)

    baseline = next((r for r in records if r["exponent"] == 0 and
                     r["record_status"] == "RETURNED"), None)
    if baseline is not None:
        df_total = len(rows) * (len(rows[0]) - 1) + len(rows) - 1
        for record in records:
            if record["record_status"] != "RETURNED":
                record["equivariance_status"] = "UNRESOLVED"
                continue
            factor = math.ldexp(1.0, int(record["exponent"]))
            expected = baseline["profile_loglik"] - df_total * math.log(factor * factor) / 2.0
            record["profile_loglik_abs_error"] = abs(record["profile_loglik"] - expected)
            record["mle_abs_error"] = abs(record["mle_base_variance"] - baseline["mle_base_variance"])
            record["lr_lower_abs_error"] = abs(record["lr_lower_base_variance"] - baseline["lr_lower_base_variance"])
            record["lr_upper_abs_error"] = abs(record["lr_upper_base_variance"] - baseline["lr_upper_base_variance"])
            baseline_roots = list(baseline["score_polynomial_roots_base_variance"])
            current_roots = list(record["score_polynomial_roots_base_variance"])
            root_count_equal = len(current_roots) == len(baseline_roots)
            root_error = (
                max(abs(a - b) for a, b in zip(current_roots, baseline_roots))
                if root_count_equal and current_roots else
                (0.0 if root_count_equal else None)
            )
            root_scale = max([1.0, *(abs(value) for value in baseline_roots)])
            root_relative_error = (
                root_error / root_scale if root_error is not None else None
            )
            record["score_root_count_equal"] = root_count_equal
            record["score_root_max_relative_error"] = root_relative_error
            record["equivariance_status"] = (
                "PASS" if (
                    record["profile_loglik_abs_error"] <= 1e-7
                    and record["mle_abs_error"] <= 1e-10
                    and record["lr_lower_abs_error"] <= 1e-8
                    and record["lr_upper_abs_error"] <= 1e-8
                    and root_count_equal
                    and root_relative_error is not None
                    and root_relative_error <= 1e-7
                    and record["score_polynomial_status"] == baseline["score_polynomial_status"]
                    and record["sturm_status"] == baseline["sturm_status"]
                    and record["adjudication_status"] == baseline["adjudication_status"]
                ) else "FAIL"
            )
    else:
        for record in records:
            record["equivariance_status"] = "UNRESOLVED_BASELINE"

    return {
        "generator_version": GENERATOR_VERSION,
        "execution_performed": True,
        "scientific_execution": False,
        "scale_exponents": list(N4_EXponents),
        "record_count": len(records),
        "returned_count": sum(r["record_status"] == "RETURNED" for r in records),
        "equivariance_counts": {
            status: sum(r.get("equivariance_status") == status for r in records)
            for status in ("PASS", "FAIL", "UNRESOLVED", "UNRESOLVED_BASELINE")
        },
        "records": records,
    }


def run_stress_v2() -> dict[str, Any]:
    """Execute the deterministic v002 lanes when explicitly called."""
    polynomial = run_polynomial_stress_v2()
    covariant = run_n3_covariant_lane()
    f1 = run_f1_observation_scale_ladder_v2()
    return {
        "generator_version": GENERATOR_VERSION,
        "execution_performed": True,
        "scientific_execution": False,
        "polynomial": polynomial,
        "n3_covariant": covariant,
        "f1_n4": f1,
    }
