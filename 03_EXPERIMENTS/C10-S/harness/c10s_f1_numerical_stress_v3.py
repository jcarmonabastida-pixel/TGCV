"""Deterministic F1 numerical diagnostics v003.

This module is side-effect free on import. Numerical work occurs only when
run_stress_v3() is explicitly called by the separately governed CLI.
Frozen v001/v002 sources are imported read-only and are not modified.
"""
from __future__ import annotations

from fractions import Fraction
import json
import math
import struct
from pathlib import Path
from typing import Any, Sequence

from c10s_f1_independent_root_isolator import (
    _cauchy_bound,
    isolate_real_roots,
)
from c10s_f1_numerical_stress import (
    PolynomialFixture,
    evaluate_polynomial_fixture,
)
from c10s_f1_numerical_stress_v2 import (
    _annotate_topology,
    _multiply_roots,
    _qtext,
)

Q = Fraction
GENERATOR_VERSION = "C10S_F1_NUMERICAL_STRESS_GENERATOR_003"
N2_GAP_EXPONENTS = (28, 32, 36, 40)
ULP_STEPS = (-2, -1, 1, 2)
N4_MAX_DEPTH = 256
N4_MAX_WIDTH = Q(1, 10**12)
N5_N = 2**120


def _discriminant_quadratic(coefficients: Sequence[Q]) -> Q:
    if len(coefficients) != 3:
        raise ValueError("QUADRATIC_COEFFICIENT_VECTOR_REQUIRED")
    a, b, c = coefficients
    return b * b - 4 * a * c


def _discriminant_cubic(coefficients: Sequence[Q]) -> Q:
    if len(coefficients) != 4:
        raise ValueError("CUBIC_COEFFICIENT_VECTOR_REQUIRED")
    a, b, c, d = coefficients
    return (
        c * c * b * b - 4 * d * b * b * b
        - 4 * c * c * c * a - 27 * d * d * a * a
        + 18 * d * c * b * a
    )


def _sign(value: Q) -> str:
    return "POSITIVE" if value > 0 else "NEGATIVE" if value < 0 else "ZERO"


def _ulp_step(value: float, steps: int) -> float:
    direction = math.inf if steps > 0 else -math.inf
    result = value
    for _ in range(abs(steps)):
        result = math.nextafter(result, direction)
    if not math.isfinite(result):
        raise ArithmeticError("ULP_STEP_NONFINITE")
    return result


def _n2_discriminant_ulp_lane() -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for exponent in N2_GAP_EXPONENTS:
        roots = (Q(1), Q(1) + Q(1, 2**exponent), Q(-2))
        ideal = _multiply_roots(roots)
        base_float = tuple(float(value) for value in ideal)
        if len(base_float) != 4 or not all(math.isfinite(v) for v in base_float):
            raise ArithmeticError("N2_BASE_BINARY64_REPRESENTATION_FAILED")
        for coefficient_index, original in enumerate(base_float):
            for steps in ULP_STEPS:
                changed = list(base_float)
                changed[coefficient_index] = _ulp_step(original, steps)
                override = tuple(Q.from_float(value) for value in changed)
                fixture = PolynomialFixture(
                    fixture_id=f"N2_V3_GAP_E{exponent}_C{coefficient_index}_ULP{steps:+d}",
                    block="N2_DISCRIMINANT_ULP_V3",
                    ideal_coefficients=ideal,
                    ideal_real_roots=tuple(sorted(roots)),
                    transformation="BINARY64_COEFFICIENT_PERTURBATION_NEAR_DISCRIMINANT_BOUNDARY",
                    perturbation=f"GAP_2^-{exponent}_COEFFICIENT_{coefficient_index}_ULP_{steps:+d}",
                    coefficient_override=override,
                )
                record = evaluate_polynomial_fixture(fixture)
                record = _annotate_topology(record, fixture)
                represented = tuple(
                    Q.from_float(float.fromhex(value))
                    for value in record["binary64_hex"]
                )
                ideal_discriminant = _discriminant_cubic(ideal)
                represented_discriminant = _discriminant_cubic(represented)
                record.update({
                    "lane": "N2_DISCRIMINANT_ULP_V3",
                    "gap_exponent": exponent,
                    "coefficient_index": coefficient_index,
                    "ulp_steps": steps,
                    "ideal_discriminant": _qtext(ideal_discriminant),
                    "ideal_discriminant_sign": _sign(ideal_discriminant),
                    "represented_discriminant": _qtext(represented_discriminant),
                    "represented_discriminant_sign": _sign(represented_discriminant),
                })
                records.append(record)
    return records


def _rounding_cell(value: float) -> dict[str, Any]:
    if not math.isfinite(value):
        raise ValueError("FINITE_BINARY64_VALUE_REQUIRED")
    previous = math.nextafter(value, -math.inf)
    following = math.nextafter(value, math.inf)
    if not math.isfinite(previous) or not math.isfinite(following):
        raise ArithmeticError("FINITE_ADJACENT_BINARY64_VALUES_REQUIRED")
    bits = struct.unpack(">Q", struct.pack(">d", value))[0]
    ties_to_even = (bits & 1) == 0
    q_previous = Q.from_float(previous)
    q_value = Q.from_float(value)
    q_following = Q.from_float(following)
    lower = (q_previous + q_value) / 2
    upper = (q_value + q_following) / 2
    return {
        "binary64_hex": value.hex(),
        "exact_binary64_rational": _qtext(q_value),
        "lower": _qtext(lower),
        "upper": _qtext(upper),
        "lower_closed": ties_to_even,
        "upper_closed": ties_to_even,
        "ties_to_even_significand": ties_to_even,
    }


def _interval_multiply(
    left: tuple[Q, Q], right: tuple[Q, Q],
) -> tuple[Q, Q]:
    products = (
        left[0] * right[0], left[0] * right[1],
        left[1] * right[0], left[1] * right[1],
    )
    return min(products), max(products)


def _interval_square(interval: tuple[Q, Q]) -> tuple[Q, Q]:
    lower, upper = interval
    if lower <= 0 <= upper:
        return Q(0), max(lower * lower, upper * upper)
    values = (lower * lower, upper * upper)
    return min(values), max(values)


def _n5_rounding_cell_diagnostic() -> dict[str, Any]:
    n = Q(N5_N)
    ideal = (n * (n + 1), -(2 * n + 1), Q(1))
    rounded = tuple(float(value) for value in ideal)
    if not all(math.isfinite(value) for value in rounded):
        raise ArithmeticError("N5_BINARY64_REPRESENTATION_FAILED")
    represented = tuple(Q.from_float(value) for value in rounded)
    cells = tuple(_rounding_cell(value) for value in rounded)
    intervals = tuple((Q(cell["lower"]), Q(cell["upper"])) for cell in cells)

    a_interval, b_interval, c_interval = intervals
    b_squared = _interval_square(b_interval)
    ac = _interval_multiply(a_interval, c_interval)
    discriminant_interval = (
        b_squared[0] - 4 * ac[1],
        b_squared[1] - 4 * ac[0],
    )
    if discriminant_interval[0] > 0:
        interval_status = "ROBUST_TWO_REAL"
    elif discriminant_interval[1] < 0:
        interval_status = "ROBUST_NO_REAL_PAIR"
    else:
        interval_status = "TOPOLOGY_UNCERTAIN_AT_ROUNDING_RESOLUTION"

    ideal_discriminant = _discriminant_quadratic(ideal)
    represented_discriminant = _discriminant_quadratic(represented)
    domain_lower, domain_upper = n - 1, n + 2
    ideal_roots = isolate_real_roots(
        ideal, lower=domain_lower, upper=domain_upper,
        max_width=Q(1, 10**12), max_depth=256,
    )
    represented_roots = isolate_real_roots(
        represented, lower=domain_lower, upper=domain_upper,
        max_width=Q(1, 10**12), max_depth=256,
    )
    return {
        "lane": "N5_ROUNDING_CELL_V3",
        "fixture_id": "N5_CLOSE_PAIR_LARGE_MAGNITUDE",
        "N": str(N5_N),
        "ideal_coefficients_ascending": [_qtext(v) for v in ideal],
        "rounded_binary64_hex": [v.hex() for v in rounded],
        "represented_coefficients_exact": [_qtext(v) for v in represented],
        "coefficient_rounding_cells": list(cells),
        "coefficient_exactly_representable": [
            ideal_value == represented_value
            for ideal_value, represented_value in zip(ideal, represented)
        ],
        "coefficient_rounding_errors": [
            _qtext(represented_value - ideal_value)
            for ideal_value, represented_value in zip(ideal, represented)
        ],
        "ideal_discriminant": _qtext(ideal_discriminant),
        "ideal_discriminant_sign": _sign(ideal_discriminant),
        "represented_discriminant": _qtext(represented_discriminant),
        "represented_discriminant_sign": _sign(represented_discriminant),
        "rounding_cell_discriminant_enclosure": [
            _qtext(discriminant_interval[0]), _qtext(discriminant_interval[1]),
        ],
        "rounding_cell_topology_status": interval_status,
        "ideal_sturm_status": ideal_roots.status,
        "ideal_sturm_root_multiplicities": [r.multiplicity for r in ideal_roots.roots],
        "represented_sturm_status": represented_roots.status,
        "represented_sturm_root_multiplicities": [
            r.multiplicity for r in represented_roots.roots
        ],
        "domain": [_qtext(domain_lower), _qtext(domain_upper)],
        "max_width": _qtext(Q(1, 10**12)),
        "max_depth": 256,
    }


def _ceil_nth_root_fraction(value: Q, degree: int) -> int:
    if value < 0 or degree < 1:
        raise ValueError("NONNEGATIVE_VALUE_AND_POSITIVE_ROOT_DEGREE_REQUIRED")
    if value == 0:
        return 0
    low, high = 0, 1
    while Q(high**degree) < value:
        high *= 2
    while low + 1 < high:
        middle = (low + high) // 2
        if Q(middle**degree) >= value:
            high = middle
        else:
            low = middle
    return high


def _fujiwara_integer_bound(coefficients: Sequence[Q]) -> int:
    if len(coefficients) != 4 or coefficients[-1] == 0:
        raise ValueError("NONDEGENERATE_CUBIC_REQUIRED")
    leading = abs(coefficients[-1])
    terms = (
        _ceil_nth_root_fraction(abs(coefficients[0]) / leading, 3),
        _ceil_nth_root_fraction(abs(coefficients[1]) / leading, 2),
        _ceil_nth_root_fraction(abs(coefficients[2]) / leading, 1),
    )
    return 2 * max(terms)


def _ceil_log2_ratio(numerator: Q, denominator: Q) -> int:
    if numerator <= 0 or denominator <= 0:
        raise ValueError("POSITIVE_RATIO_REQUIRED")
    ratio = numerator / denominator
    if ratio <= 1:
        return 0
    exponent = 0
    while Q(2**exponent) < ratio:
        exponent += 1
    return exponent


def _n4_fujiwara_bound_lane(frozen_inputs: dict[str, Any]) -> list[dict[str, Any]]:
    if frozen_inputs.get("schema") != "C10S-F1-N4-V002-FROZEN-INPUTS-1":
        raise ValueError("UNEXPECTED_N4_FROZEN_INPUT_SCHEMA")
    if frozen_inputs.get("record_count") != 14 or len(frozen_inputs.get("records", [])) != 14:
        raise ValueError("N4_FROZEN_INPUT_DENOMINATOR_MISMATCH")
    records: list[dict[str, Any]] = []
    for item in frozen_inputs["records"]:
        exponent = int(item["exponent"])
        coefficients = tuple(
            Q.from_float(float.fromhex(value))
            for value in item["score_polynomial_coefficients_binary64_hex"]
        )
        if len(coefficients) != 4:
            raise ValueError("N4_CUBIC_COEFFICIENT_VECTOR_REQUIRED")
        cauchy = _cauchy_bound(coefficients)
        fujiwara = _fujiwara_integer_bound(coefficients)
        base_root = Q.from_float(float(item["score_polynomial_roots_base_variance"][0]))
        scale = Q(2) ** (2 * exponent)
        candidate_root = base_root * scale
        coarse_depth = _ceil_log2_ratio(Q(cauchy), candidate_root)
        local_depth = _ceil_log2_ratio(candidate_root, N4_MAX_WIDTH)
        alternative = isolate_real_roots(
            coefficients, lower=0, upper=Q(fujiwara),
            max_depth=N4_MAX_DEPTH, max_width=N4_MAX_WIDTH,
        )
        records.append({
            "lane": "N4_FUJIWARA_BOUND_V3",
            "exponent": exponent,
            "observation_scale": f"2^{exponent}",
            "coefficients_binary64_hex": item["score_polynomial_coefficients_binary64_hex"],
            "coefficients_exact_rational": [_qtext(v) for v in coefficients],
            "v002_cauchy_sturm_status": item["v002_sturm_status"],
            "v002_cauchy_adjudication_status": item["v002_adjudication_status"],
            "cauchy_upper_bound_exact": _qtext(cauchy),
            "fujiwara_upper_bound_integer": str(fujiwara),
            "cauchy_to_fujiwara_ratio": _qtext(Q(cauchy, fujiwara)),
            "f1_candidate_root_base_variance": _qtext(base_root),
            "f1_candidate_root_at_scale": _qtext(candidate_root),
            "max_width": _qtext(N4_MAX_WIDTH),
            "max_depth": N4_MAX_DEPTH,
            "midpoint_depth_estimate": {
                "coarse_bound_to_root_scale": coarse_depth,
                "local_root_to_width": local_depth,
                "sum": coarse_depth + local_depth,
                "interpretation": "APPROXIMATE_BUDGET_NOT_ACTUAL_SUBDIVISION_TRACE",
            },
            "fujiwara_sturm_status": alternative.status,
            "fujiwara_sturm_intervals": [
                [_qtext(root.lower), _qtext(root.upper), root.multiplicity]
                for root in alternative.roots
            ],
            "fujiwara_sturm_root_count": len(alternative.roots),
            "fujiwara_vs_v002": (
                "RESOLVED_AFTER_TIGHTER_BOUND"
                if item["v002_sturm_status"] != "ROOTS_ISOLATED"
                and alternative.status == "ROOTS_ISOLATED"
                else "UNRESOLVED_AFTER_TIGHTER_BOUND"
                if item["v002_sturm_status"] != "ROOTS_ISOLATED"
                else "BOTH_RESOLVED"
                if alternative.status == "ROOTS_ISOLATED"
                else "ALTERNATIVE_BOUND_REGRESSION"
            ),
        })
    return records


def run_stress_v3(frozen_inputs_path: str | Path | None = None) -> dict[str, Any]:
    """Run the three deterministic diagnostic lanes when separately authorized."""
    if frozen_inputs_path is None:
        frozen_inputs_path = Path(__file__).with_name(
            "C10S_F1_N4_V002_FROZEN_INPUTS_001.json"
        )
    frozen_inputs = json.loads(Path(frozen_inputs_path).read_text(encoding="utf-8"))
    n2 = _n2_discriminant_ulp_lane()
    n5 = _n5_rounding_cell_diagnostic()
    n4 = _n4_fujiwara_bound_lane(frozen_inputs)
    total = len(n2) + 1 + len(n4)
    if (len(n2), len(n4), total) != (64, 14, 79):
        raise ArithmeticError("V003_PREDECLARED_DENOMINATOR_MISMATCH")
    def counts(rows: Sequence[dict[str, Any]], field: str) -> dict[str, int]:
        result: dict[str, int] = {}
        for row in rows:
            key = str(row.get(field, "MISSING"))
            result[key] = result.get(key, 0) + 1
        return dict(sorted(result.items()))

    n2_sign_changes = sum(
        row["ideal_discriminant_sign"] != row["represented_discriminant_sign"]
        for row in n2
    )
    return {
        "schema": "C10S-F1-NUMERICAL-STRESS-SUMMARY-003",
        "generator_version": GENERATOR_VERSION,
        "scientific_execution": False,
        "dgp_execution": False,
        "monte_carlo_calibration": False,
        "lane_counts": {
            "N2_DISCRIMINANT_ULP_V3": len(n2),
            "N5_ROUNDING_CELL_V3": 1,
            "N4_FUJIWARA_BOUND_V3": len(n4),
        },
        "diagnostic_counts": {
            "n2_topology_comparison": counts(n2, "topology_comparison_status"),
            "n2_ideal_vs_represented_discriminant_sign_changes": n2_sign_changes,
            "n5_rounding_cell_topology": n5["rounding_cell_topology_status"],
            "n5_ideal_sturm": n5["ideal_sturm_status"],
            "n5_represented_sturm": n5["represented_sturm_status"],
            "n4_fujiwara_sturm": counts(n4, "fujiwara_sturm_status"),
            "n4_comparison_to_v002": counts(n4, "fujiwara_vs_v002"),
        },
        "combined_record_count": total,
        "records": n2 + [n5] + n4,
    }
