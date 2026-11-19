"""Deterministic adversarial fixture generator and non-executing stress harness.

This module defines fixtures and callable runners only. Importing it does not
execute the stress suite. The polynomial fixture lane exercises the exact-
rational Sturm isolator independently. The F1 end-to-end lane exercises the
existing data-derived F1 pipeline under observation-scale transformations.

Important boundary: the current F1 root adjudicator accepts observed rows and
reconstructs its own score polynomial; it has no public API for injecting an
arbitrary polynomial fixture. Therefore N1-N3/N5-N6 do not claim to compare an
arbitrary polynomial against F1. They characterize Sturm's exact-rational
reference and its fail-closed boundary. N4 is the F1 end-to-end lane.
"""
from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
import math
from typing import Iterable, Sequence

from c10s_f1_independent_root_isolator import isolate_real_roots


Q = Fraction
GENERATOR_VERSION = "C10S_F1_NUMERICAL_STRESS_GENERATOR_001"
ROOT_SEPARATION_EXPONENTS = (4, 8, 16, 24, 32, 40, 48, 52, 54)
SCALE_EXPONENTS = (-500, -200, -50, 0, 50, 200, 500)
ULP_STEPS = (-2, -1, 1, 2)
ISOLATION_WIDTHS = (Q(1, 10**6), Q(1, 10**12), Q(1, 10**20))
ISOLATION_DEPTHS = (1, 4, 16, 64, 256)


@dataclass(frozen=True)
class PolynomialFixture:
    fixture_id: str
    block: str
    ideal_coefficients: tuple[Q, ...]
    ideal_real_roots: tuple[Q, ...]
    transformation: str = "IDENTITY"
    perturbation: str = "NONE"
    domain_lower: Q | None = None
    domain_upper: Q | None = None
    coefficient_override: tuple[Q, ...] | None = None


def _trim(coefficients: Iterable[Q]) -> tuple[Q, ...]:
    values = list(coefficients)
    while len(values) > 1 and values[-1] == 0:
        values.pop()
    return tuple(values or [Q(0)])


def _multiply_linear_factors(roots: Sequence[Q]) -> tuple[Q, ...]:
    """Return ascending coefficients for product(x - root)."""
    coefficients = [Q(1)]
    for root in roots:
        out = [Q(0)] * (len(coefficients) + 1)
        for index, value in enumerate(coefficients):
            out[index] -= root * value
            out[index + 1] += value
        coefficients = out
    return _trim(coefficients)


def _float_vector(coefficients: Sequence[Q]) -> tuple[float, ...] | None:
    converted: list[float] = []
    for value in coefficients:
        try:
            number = float(value)
        except OverflowError:
            return None
        if not math.isfinite(number) or (value != 0 and number == 0.0):
            return None
        converted.append(number)
    return tuple(converted)


def _exact_float_vector(values: Sequence[float]) -> tuple[Q, ...]:
    return tuple(Q.from_float(value) for value in values)


def _step_ulp(value: float, steps: int) -> float:
    direction = math.inf if steps > 0 else -math.inf
    result = value
    for _ in range(abs(steps)):
        result = math.nextafter(result, direction)
    return result


def _fixture(
    fixture_id: str, block: str, roots: Sequence[Q], *,
    transformation: str = "IDENTITY", perturbation: str = "NONE",
    domain: tuple[Q, Q] | None = None,
) -> PolynomialFixture:
    root_tuple = tuple(Q(root) for root in roots)
    return PolynomialFixture(
        fixture_id=fixture_id,
        block=block,
        ideal_coefficients=_multiply_linear_factors(root_tuple),
        ideal_real_roots=tuple(sorted(root_tuple)),
        transformation=transformation,
        perturbation=perturbation,
        domain_lower=domain[0] if domain else None,
        domain_upper=domain[1] if domain else None,
    )


def _scale_fixture(
    fixture: PolynomialFixture, exponent: int, *, variable: bool,
) -> PolynomialFixture:
    factor = Q(2) ** exponent
    if variable:
        coefficients = tuple(
            coefficient / (factor ** index)
            for index, coefficient in enumerate(fixture.ideal_coefficients)
        )
        roots = tuple(root * factor for root in fixture.ideal_real_roots)
        label = f"VARIABLE_SCALE_2^{exponent}"
    else:
        coefficients = tuple(
            coefficient * factor for coefficient in fixture.ideal_coefficients
        )
        roots = fixture.ideal_real_roots
        label = f"AMPLITUDE_SCALE_2^{exponent}"
    return PolynomialFixture(
        fixture_id=f"{fixture.fixture_id}_{label}",
        block="N3",
        ideal_coefficients=_trim(coefficients),
        ideal_real_roots=tuple(sorted(roots)),
        transformation=label,
    )


def build_polynomial_fixtures() -> tuple[PolynomialFixture, ...]:
    """Build the complete deterministic N1-N3, N5 and N6 fixture roster."""
    fixtures: list[PolynomialFixture] = []

    # N1: approach binary64 root coalescence from well-resolved separations.
    for exponent in ROOT_SEPARATION_EXPONENTS:
        delta = Q(1, 2**exponent)
        fixtures.append(_fixture(
            f"N1_SIMPLE_PAIR_E{exponent}", "N1", (Q(1), Q(1) + delta),
        ))
        fixtures.append(_fixture(
            f"N1_PAIR_PLUS_NEGATIVE_E{exponent}", "N1",
            (Q(1), Q(1) + delta, Q(-2)),
        ))
    fixtures.extend((
        _fixture("N1_DOUBLE_PLUS_SIMPLE", "N1", (Q(1), Q(1), Q(2))),
        _fixture("N1_TRIPLE", "N1", (Q(1), Q(1), Q(1))),
    ))

    # N2: one- and two-ULP coefficient perturbations. Each coefficient is
    # perturbed independently; no combinatorial cross-product is implied.
    ulp_base = _fixture(
        "N2_BASE_SIMPLE_CUBIC", "N2", (Q(1, 2), Q(3, 2), Q(5, 2)),
    )
    base_float = _float_vector(ulp_base.ideal_coefficients)
    assert base_float is not None
    for coefficient_index, value in enumerate(base_float):
        if value == 0.0:
            continue
        for steps in ULP_STEPS:
            changed = list(base_float)
            changed[coefficient_index] = _step_ulp(value, steps)
            exact_changed = _exact_float_vector(changed)
            fixtures.append(PolynomialFixture(
                fixture_id=f"N2_C{coefficient_index}_ULP{steps:+d}",
                block="N2",
                ideal_coefficients=ulp_base.ideal_coefficients,
                ideal_real_roots=ulp_base.ideal_real_roots,
                transformation="BINARY64_COEFFICIENT_PERTURBATION",
                perturbation=f"COEFFICIENT_{coefficient_index}_ULP_{steps:+d}",
                coefficient_override=exact_changed,
            ))

    # N3: exact amplitude and variable-coordinate transformations.
    scale_base = _fixture(
        "N3_BASE", "N3", (Q(1, 2), Q(3, 2), Q(5, 2)),
    )
    for exponent in SCALE_EXPONENTS:
        fixtures.append(_scale_fixture(scale_base, exponent, variable=False))
        fixtures.append(_scale_fixture(scale_base, exponent, variable=True))

    # N5: fixed polynomial under predeclared isolation widths/depths.
    resolution_base = _fixture(
        "N5_CLOSE_PAIR", "N5", (Q(1), Q(1) + Q(1, 10**8)),
    )
    fixtures.append(resolution_base)

    # N6: zero and finite-domain endpoint roots, degree reduction and constants.
    fixtures.extend((
        _fixture("N6_ZERO_AND_POSITIVE", "N6", (Q(0), Q(1)), domain=(Q(0), Q(1))),
        _fixture("N6_NEGATIVE_AND_UPPER_EDGE", "N6", (Q(-1), Q(2)), domain=(Q(-1), Q(2))),
        PolynomialFixture("N6_NONZERO_CONSTANT", "N6", (Q(7),), ()),
        PolynomialFixture("N6_IDENTICALLY_ZERO", "N6", (Q(0),), ()),
        PolynomialFixture("N6_LINEAR", "N6", (Q(-2), Q(1)), (Q(2),)),
    ))
    return tuple(fixtures)


def _domain_for(fixture: PolynomialFixture) -> tuple[Q, Q]:
    if fixture.domain_lower is not None and fixture.domain_upper is not None:
        return fixture.domain_lower, fixture.domain_upper
    if fixture.ideal_real_roots:
        low = min(fixture.ideal_real_roots)
        high = max(fixture.ideal_real_roots)
        margin = max(Q(1), abs(low) / 10, abs(high) / 10)
        return low - margin, high + margin
    return Q(-2), Q(2)


def _root_payload(result) -> list[dict[str, object]]:
    return [
        {
            "lower": f"{root.lower.numerator}/{root.lower.denominator}",
            "upper": f"{root.upper.numerator}/{root.upper.denominator}",
            "multiplicity": root.multiplicity,
            "distinct_root_count": root.distinct_root_count,
        }
        for root in result.roots
    ]


def evaluate_polynomial_fixture(
    fixture: PolynomialFixture, *,
    max_width: Q = Q(1, 10**12), max_depth: int = 256,
) -> dict[str, object]:
    """Evaluate one fixture against Sturm; does not execute F1 or mutate inputs."""
    actual_coefficients = (
        fixture.coefficient_override
        if fixture.coefficient_override is not None
        else fixture.ideal_coefficients
    )
    binary64 = _float_vector(actual_coefficients)
    base: dict[str, object] = {
        "generator_version": GENERATOR_VERSION,
        "fixture_id": fixture.fixture_id,
        "block": fixture.block,
        "transformation": fixture.transformation,
        "perturbation": fixture.perturbation,
        "domain": [str(v) for v in _domain_for(fixture)],
        "ideal_coefficients": [
            f"{v.numerator}/{v.denominator}" for v in fixture.ideal_coefficients
        ],
        "actual_preconversion_coefficients": [
            f"{v.numerator}/{v.denominator}" for v in actual_coefficients
        ],
        "ideal_real_roots": [
            f"{v.numerator}/{v.denominator}" for v in fixture.ideal_real_roots
        ],
        "binary64_representable": binary64 is not None,
        "binary64_hex": (
            [value.hex() for value in binary64] if binary64 is not None else None
        ),
        "exact_binary64_coefficients": (
            [f"{v.numerator}/{v.denominator}" for v in _exact_float_vector(binary64)]
            if binary64 is not None else None
        ),
        "max_width": f"{max_width.numerator}/{max_width.denominator}",
        "max_depth": max_depth,
        "f1_root_result": "NOT_EVALUATED_ARBITRARY_POLYNOMIAL_API_UNAVAILABLE",
    }
    if binary64 is None:
        base.update({
            "sturm_status": "REPRESENTATION_UNRESOLVED",
            "sturm_roots": [],
            "abstention_reason": "NONFINITE_OR_ERASED_NONZERO_BINARY64_COEFFICIENT",
        })
        return base

    lower, upper = _domain_for(fixture)
    try:
        result = isolate_real_roots(
            binary64, lower=lower, upper=upper,
            max_depth=max_depth, max_width=max_width,
        )
    except (ArithmeticError, OverflowError, ValueError) as exc:
        base.update({
            "sturm_status": "INVALID_OR_UNRESOLVED",
            "sturm_roots": [],
            "abstention_reason": type(exc).__name__ + ":" + str(exc),
        })
        return base

    base.update({
        "sturm_status": result.status,
        "sturm_degree": result.degree,
        "sturm_roots": _root_payload(result),
        "sturm_coefficient_semantics": result.coefficient_semantics,
        "abstention_reason": (
            "ISOLATION_NOT_RESOLVED" if result.status == "ROOTS_UNRESOLVED" else None
        ),
    })
    return base


def run_polynomial_stress_grid() -> dict[str, object]:
    """Return deterministic records and complete denominators; never writes files."""
    fixtures = build_polynomial_fixtures()
    records: list[dict[str, object]] = []
    for fixture in fixtures:
        if fixture.block == "N5":
            for width in ISOLATION_WIDTHS:
                for depth in ISOLATION_DEPTHS:
                    records.append(evaluate_polynomial_fixture(
                        fixture, max_width=width, max_depth=depth,
                    ))
        else:
            records.append(evaluate_polynomial_fixture(fixture))

    statuses: dict[str, int] = {}
    for record in records:
        key = str(record["sturm_status"])
        statuses[key] = statuses.get(key, 0) + 1
    return {
        "generator_version": GENERATOR_VERSION,
        "execution_performed": True,
        "scientific_execution": False,
        "f1_arbitrary_polynomial_comparison_performed": False,
        "fixture_count": len(records),
        "binary64_representable_count": sum(
            bool(record["binary64_representable"]) for record in records
        ),
        "sturm_status_counts": statuses,
        "agreement_discrepancy_metrics": "NOT_APPLICABLE_WITHOUT_GENERIC_F1_POLYNOMIAL_SOLVER",
        "records": records,
    }


def run_f1_observation_scale_ladder() -> dict[str, object]:
    """Exercise the real F1 row->score-polynomial->Sturm path at fixed scales."""
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
    records: list[dict[str, object]] = []
    for exponent in (-100, -50, -20, 0, 20, 50, 100):
        factor = math.ldexp(1.0, exponent)
        scaled_rows = tuple(
            tuple(factor * value for value in row) for row in rows
        )
        scaled_tau = tau * factor * factor
        record: dict[str, object] = {
            "exponent": exponent,
            "scale_factor_hex": factor.hex(),
            "observation_scale": "2^" + str(exponent),
            "variance_scale": "2^" + str(2 * exponent),
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
            inverse_variance_scale = math.ldexp(1.0, -2 * exponent)
            record.update({
                "status": "RETURNED",
                "profile_status": profile.status,
                "mle_variance_in_base_units": profile.mle_between_variance * inverse_variance_scale,
                "lr_lower_in_base_units": low * inverse_variance_scale,
                "lr_upper_in_base_units": high * inverse_variance_scale,
                "polynomial_status": diagnostic.status,
                "polynomial_degree": diagnostic.degree,
                "polynomial_roots_in_base_units": [
                    value / factor for value in diagnostic.positive_roots
                ],
                "adjudication_status": adjudication.status,
                "adjudication_reason": adjudication.reason,
                "sturm_status": adjudication.independent_status,
            })
        except (ArithmeticError, OverflowError, ValueError) as exc:
            record.update({
                "status": "FAIL_CLOSED_EXCEPTION",
                "exception": type(exc).__name__ + ":" + str(exc),
            })
        records.append(record)

    returned = [r for r in records if r["status"] == "RETURNED"]
    baseline = next((r for r in returned if r["exponent"] == 0), None)
    return {
        "generator_version": GENERATOR_VERSION,
        "execution_performed": True,
        "scientific_execution": False,
        "scale_exponents": [-100, -50, -20, 0, 20, 50, 100],
        "record_count": len(records),
        "baseline_exponent_zero": baseline,
        "returned_count": len(returned),
        "fail_closed_count": len(records) - len(returned),
        "records": records,
    }


def stress_design_manifest() -> dict[str, object]:
    """Return the frozen, deterministic design constants without running it."""
    fixtures = build_polynomial_fixtures()
    return {
        "generator_version": GENERATOR_VERSION,
        "fixture_count_before_N5_resolution_cross_product": len(fixtures),
        "root_separation_exponents": list(ROOT_SEPARATION_EXPONENTS),
        "scale_exponents": list(SCALE_EXPONENTS),
        "ulp_steps": list(ULP_STEPS),
        "isolation_widths": [
            f"{v.numerator}/{v.denominator}" for v in ISOLATION_WIDTHS
        ],
        "isolation_depths": list(ISOLATION_DEPTHS),
        "f1_observation_scale_exponents": [-100, -50, -20, 0, 20, 50, 100],
        "f1_arbitrary_polynomial_injection": False,
        "randomness": "NONE",
        "automatic_execution_on_import": False,
    }
