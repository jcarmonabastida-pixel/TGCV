from __future__ import annotations

import json
from fractions import Fraction
from time import perf_counter

import c10s_f5_component_profile_score as profile
import c10s_f5_rational_score_polynomials as rational
from c10s_f5_sturm_call_instrumentation import (
    install_sturm_call_instrumentation,
    primitive_integer_sturm_sequence,
    sign_variations_integer_certified_fixedpoint,
)

WIDTH = Fraction(1, 2**8)
TARGET = Fraction(1, 20)
CERTIFIED_GLOBAL_STATES = {
    "GLOBAL_INTERIOR_MAXIMUM_CERTIFIED",
    "GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED",
    "GLOBAL_CO_MAXIMIZERS_CERTIFIED",
}
M30_INTERIOR = {0: 1, 2: 2, 5: 4, 8: 5, 10: 6, 12: 5, 15: 4, 18: 2, 20: 1}
M30_BOUNDARY = {0: 15, 20: 15}
M10_INTERIOR = {0: 1, 1: 2, 2: 2, 3: 2, 4: 2, 5: 1}
M10_BOUNDARY = {0: 5, 5: 5}


def _fraction_summary(values):
    if values is None:
        return None
    return [{
        "approx_decimal": format(float(value), ".16g"),
        "numerator_bits": abs(value.numerator).bit_length(),
        "denominator_bits": value.denominator.bit_length(),
    } for value in values]


def _run_case(name, r, histogram, component):
    started = perf_counter()
    certificate = rational.beta_binomial_global_mle_certificate(
        r, histogram, max_refinements=1, projection_bits=12,
        max_projection_depth=40, max_lift_intervals=100,
        max_lift_depth=20, max_mu_depth=10,
        source_revision="0123456789abcdef0123456789abcdef01234567",
    )
    certificate_seconds = perf_counter() - started
    record = {
        "fixture": name,
        "R": r,
        "component": component,
        "global_certificate_seconds": round(certificate_seconds, 6),
        "global_certificate_status": certificate.get("status"),
    }
    if certificate.get("status") not in CERTIFIED_GLOBAL_STATES:
        record["status"] = "SKIPPED_GLOBAL_CERTIFICATE_UNRESOLVED"
        raise RuntimeError(f"GLOBAL_CERTIFICATE_UNRESOLVED: {record}")

    original_sturm = rational._uni_sturm_sequence
    original_integer = rational._uni_sturm_integer_sequence
    rational._uni_sturm_sequence = primitive_integer_sturm_sequence
    rational._uni_sturm_integer_sequence = lambda sequence: sequence
    calls, restore = install_sturm_call_instrumentation(
        profile, rational,
        variation_evaluator=sign_variations_integer_certified_fixedpoint,
    )
    started = perf_counter()
    try:
        result = profile.f5_component_profile_lr_statistic(
            r, histogram, component=component, target=TARGET,
            global_certificate=certificate,
            root_isolation_width=WIDTH,
            max_depth=140, max_intervals=5000,
            log_series_terms=80,
        )
        profile_seconds = perf_counter() - started
    finally:
        restore()
        rational._uni_sturm_sequence = original_sturm
        rational._uni_sturm_integer_sequence = original_integer

    prof = result.get("profile", {})
    record.update({
        "profile_seconds": round(profile_seconds, 6),
        "lr_status": result.get("status"),
        "lr_statistic_bounds": _fraction_summary(result.get("lr_statistic_bounds")),
        "profile_status": prof.get("status"),
        "profile_likelihood_bounds": _fraction_summary(result.get("profile_likelihood_bounds")),
        "candidate_count": prof.get("candidate_count"),
        "interior_stationary_count": prof.get("interior_stationary_count"),
        "root_isolation_calls": calls,
    })
    if result.get("status") != "LR_STATISTIC_ENCLOSED":
        raise RuntimeError(f"LR_NOT_ENCLOSED: {record}")
    if prof.get("status") != "PROFILE_MAXIMUM_ENCLOSED":
        raise RuntimeError(f"PROFILE_MAXIMUM_NOT_ENCLOSED: {record}")
    if not calls or any(call.get("status") != "ISOLATION_COMPLETE" for call in calls):
        raise RuntimeError(f"ROOT_ISOLATION_INCOMPLETE: {record}")
    return record


def main():
    cases = [
        _run_case("M30_R20_INTERIOR", 20, M30_INTERIOR, "B"),
        _run_case("M30_R20_BOUNDARY_ONLY", 20, M30_BOUNDARY, "W"),
        _run_case("M30_R20_BOUNDARY_ONLY", 20, M30_BOUNDARY, "B"),
        _run_case("M10_R5_INTERIOR", 5, M10_INTERIOR, "W"),
        _run_case("M10_R5_INTERIOR", 5, M10_INTERIOR, "B"),
        _run_case("M10_R5_ENDPOINT_ONLY", 5, M10_BOUNDARY, "W"),
        _run_case("M10_R5_ENDPOINT_ONLY", 5, M10_BOUNDARY, "B"),
    ]
    payload = {
        "stage": "F5_WIDTH_2M8_CROSS_CELL_COMPONENT_BOUNDARY_ROBUSTNESS",
        "root_isolation_width": "2^-8",
        "sturm_builder": "SIGNED_PRIMITIVE_INTEGER_PSEUDO_REMAINDER_SEQUENCE",
        "sign_evaluation": "CERTIFIED_FIXED_POINT_INTERVAL_WITH_EXACT_FALLBACK",
        "cases": cases,
    }
    print(json.dumps(payload, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
