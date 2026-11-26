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


R = 20
HISTOGRAM = {0: 1, 2: 2, 5: 4, 8: 5, 10: 6, 12: 5, 15: 4, 18: 2, 20: 1}


def _fraction_summary(values):
    if values is None:
        return None
    output = []
    for value in values:
        output.append({
            "approx_decimal": format(float(value), ".16g"),
            "numerator_bits": abs(value.numerator).bit_length(),
            "denominator_bits": value.denominator.bit_length(),
        })
    return output


def main() -> None:
    certificate = rational.beta_binomial_global_mle_certificate(
        R, HISTOGRAM, max_refinements=1, projection_bits=12,
        max_projection_depth=40, max_lift_intervals=100,
        max_lift_depth=20, max_mu_depth=10,
        source_revision="0123456789abcdef0123456789abcdef01234567",
    )
    if certificate.get("status") not in {
        "GLOBAL_INTERIOR_MAXIMUM_CERTIFIED",
        "GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED",
        "GLOBAL_CO_MAXIMIZERS_CERTIFIED",
    }:
        raise RuntimeError(f"GLOBAL_CERTIFICATE_UNRESOLVED: {certificate.get('status')}")

    original_sturm = rational._uni_sturm_sequence
    original_integer = rational._uni_sturm_integer_sequence
    rational._uni_sturm_sequence = primitive_integer_sturm_sequence
    rational._uni_sturm_integer_sequence = lambda sequence: sequence
    records, restore = install_sturm_call_instrumentation(
        profile, rational,
        variation_evaluator=sign_variations_integer_certified_fixedpoint,
    )
    started = perf_counter()
    try:
        result = profile.f5_component_profile_lr_statistic(
            R, HISTOGRAM, component="W", target=Fraction(1, 20),
            global_certificate=certificate,
            root_isolation_width=Fraction(1, 2**16),
            max_depth=140, max_intervals=5000,
            log_series_terms=80,
        )
        total_seconds = perf_counter() - started
    finally:
        restore()
        rational._uni_sturm_sequence = original_sturm
        rational._uni_sturm_integer_sequence = original_integer

    payload = {
        "stage": "M30_R20_W_coarsest_exact_isolation_width",
        "fixture": "M30_R20",
        "component": "W",
        "target": "1/20",
        "root_isolation_width": "2^-16",
        "profile_seconds": round(total_seconds, 6),
        "root_isolation_calls": records,
        "lr_status": result.get("status"),
        "lr_statistic_bounds": _fraction_summary(result.get("lr_statistic_bounds")),
        "profile_status": result.get("profile", {}).get("status"),
        "profile_likelihood_bounds": _fraction_summary(result.get("profile_likelihood_bounds")),
        "candidate_count": result.get("profile", {}).get("candidate_count"),
        "interior_stationary_count": result.get("profile", {}).get("interior_stationary_count"),
        "sturm_builder": "SIGNED_PRIMITIVE_INTEGER_PSEUDO_REMAINDER_SEQUENCE",
        "sign_evaluation": "CERTIFIED_FIXED_POINT_INTERVAL_WITH_EXACT_FALLBACK",
    }
    print(json.dumps(payload, sort_keys=True), flush=True)
    if result.get("status") != "LR_STATISTIC_ENCLOSED":
        raise RuntimeError(f"PROFILE_LR_NOT_ENCLOSED: {result.get('status')}")
    if result.get("profile", {}).get("status") != "PROFILE_MAXIMUM_ENCLOSED":
        raise RuntimeError("PROFILE_MAXIMUM_NOT_ENCLOSED")
    if len(records) != 4:
        raise RuntimeError(f"EXPECTED_FOUR_ROOT_ISOLATION_CALLS_GOT_{len(records)}")
    if any(item.get("status") != "ISOLATION_COMPLETE" for item in records):
        raise RuntimeError("ROOT_ISOLATION_NOT_COMPLETE")


if __name__ == "__main__":
    main()
