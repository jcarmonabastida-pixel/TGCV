from __future__ import annotations

import json
from fractions import Fraction
from time import perf_counter

import c10s_f5_component_profile_score as profile
import c10s_f5_rational_score_polynomials as rational
from c10s_f5_sturm_call_instrumentation import install_sturm_call_instrumentation


R = 20
HISTOGRAM = {0: 1, 2: 2, 5: 4, 8: 5, 10: 6, 12: 5, 15: 4, 18: 2, 20: 1}


def main() -> None:
    started = perf_counter()
    certificate = rational.beta_binomial_global_mle_certificate(
        R, HISTOGRAM, max_refinements=1, projection_bits=12,
        max_projection_depth=40, max_lift_intervals=100,
        max_lift_depth=20, max_mu_depth=10,
        source_revision="0123456789abcdef0123456789abcdef01234567",
    )
    certificate_seconds = perf_counter() - started
    if certificate.get("status") not in {
        "GLOBAL_INTERIOR_MAXIMUM_CERTIFIED",
        "GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED",
        "GLOBAL_CO_MAXIMIZERS_CERTIFIED",
    }:
        raise RuntimeError(f"GLOBAL_CERTIFICATE_UNRESOLVED: {certificate.get('status')}")

    records, restore = install_sturm_call_instrumentation(profile, rational)
    started = perf_counter()
    try:
        result = profile.f5_component_profile_lr_statistic(
            R, HISTOGRAM, component="W", target=Fraction(1, 20),
            global_certificate=certificate,
            root_isolation_width=Fraction(1, 2**40),
            max_depth=140, max_intervals=5000,
            log_series_terms=80,
        )
        total_seconds = perf_counter() - started
    finally:
        restore()

    payload = {
        "stage": "M30_R20_W_per_call_sturm_instrumentation",
        "fixture": "M30_R20",
        "component": "W",
        "target": "1/20",
        "global_certificate_seconds": round(certificate_seconds, 6),
        "global_certificate_status": certificate.get("status"),
        "profile_seconds": round(total_seconds, 6),
        "root_isolation_call_count": len(records),
        "root_isolation_calls": records,
        "lr_status": result.get("status"),
        "profile_status": result.get("profile", {}).get("status"),
        "candidate_count": result.get("profile", {}).get("candidate_count"),
        "interior_stationary_count": result.get("profile", {}).get("interior_stationary_count"),
        "instrumentation_note": (
            "All numerical return values are passed through unchanged. "
            "Sequence and variation timings are nested substage timings; "
            "other_isolation_seconds is the per-call residual."
        ),
    }
    print(json.dumps(payload, sort_keys=True), flush=True)
    if result.get("status") != "LR_STATISTIC_ENCLOSED":
        raise RuntimeError(f"PROFILE_NOT_ENCLOSED: {result.get('status')}")
    if result.get("profile", {}).get("status") != "PROFILE_MAXIMUM_ENCLOSED":
        raise RuntimeError("PROFILE_MAXIMUM_NOT_ENCLOSED")
    if len(records) != 4:
        raise RuntimeError(f"EXPECTED_FOUR_ROOT_ISOLATION_CALLS_GOT_{len(records)}")


if __name__ == "__main__":
    main()
