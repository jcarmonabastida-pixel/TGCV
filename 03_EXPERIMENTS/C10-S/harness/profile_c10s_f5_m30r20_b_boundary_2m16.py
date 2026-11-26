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
INTERIOR = {0: 1, 2: 2, 5: 4, 8: 5, 10: 6, 12: 5, 15: 4, 18: 2, 20: 1}
BOUNDARY_ONLY = {0: 15, 20: 15}


def _run_case(name, histogram, component):
    started = perf_counter()
    certificate = rational.beta_binomial_global_mle_certificate(
        R, histogram, max_refinements=1, projection_bits=12,
        max_projection_depth=40, max_lift_intervals=100,
        max_lift_depth=20, max_mu_depth=10,
        source_revision="0123456789abcdef0123456789abcdef01234567",
    )
    certificate_seconds = perf_counter() - started
    record = {
        "fixture": name,
        "component": component,
        "global_certificate_seconds": round(certificate_seconds, 6),
        "global_certificate_status": certificate.get("status"),
    }
    if certificate.get("status") not in {
        "GLOBAL_INTERIOR_MAXIMUM_CERTIFIED",
        "GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED",
        "GLOBAL_CO_MAXIMIZERS_CERTIFIED",
    }:
        record["profile_status"] = "SKIPPED_GLOBAL_CERTIFICATE_UNRESOLVED"
        return record

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
            R, histogram, component=component, target=Fraction(1, 20),
            global_certificate=certificate,
            root_isolation_width=Fraction(1, 2**8),
            max_depth=140, max_intervals=5000,
            log_series_terms=80,
        )
        profile_seconds = perf_counter() - started
    finally:
        restore()
        rational._uni_sturm_sequence = original_sturm
        rational._uni_sturm_integer_sequence = original_integer

    profile_result = result.get("profile", {})
    record.update({
        "profile_seconds": round(profile_seconds, 6),
        "lr_status": result.get("status"),
        "profile_status": profile_result.get("status"),
        "candidate_count": profile_result.get("candidate_count"),
        "interior_stationary_count": profile_result.get("interior_stationary_count"),
        "root_isolation_calls": records,
    })
    return record


def main() -> None:
    cases = [
        _run_case("M30_R20_INTERIOR", INTERIOR, "B"),
        _run_case("M30_R20_BOUNDARY_ONLY", BOUNDARY_ONLY, "W"),
        _run_case("M30_R20_BOUNDARY_ONLY", BOUNDARY_ONLY, "B"),
    ]
    payload = {
        "stage": "M30_R20_B_and_boundary_robustness_at_2^-8",
        "root_isolation_width": "2^-8",
        "cases": cases,
    }
    print(json.dumps(payload, sort_keys=True), flush=True)
    if cases[0].get("lr_status") != "LR_STATISTIC_ENCLOSED":
        raise RuntimeError(f"M30_R20_B_NOT_ENCLOSED: {cases[0]}")
    if cases[0].get("profile_status") != "PROFILE_MAXIMUM_ENCLOSED":
        raise RuntimeError(f"M30_R20_B_PROFILE_NOT_ENCLOSED: {cases[0]}")
    for case in cases[1:]:
        if case.get("profile_status") == "SKIPPED_GLOBAL_CERTIFICATE_UNRESOLVED":
            continue
        if not case.get("profile_status"):
            raise RuntimeError(f"BOUNDARY_CASE_MISSING_TYPED_PROFILE_STATUS: {case}")
    for case in cases:
        for call in case.get("root_isolation_calls", []):
            if call.get("status") != "ISOLATION_COMPLETE":
                raise RuntimeError(f"ROOT_ISOLATION_INCOMPLETE: {case}")


if __name__ == "__main__":
    main()
