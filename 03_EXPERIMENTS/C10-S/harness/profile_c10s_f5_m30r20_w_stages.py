from __future__ import annotations

import json
from fractions import Fraction
from time import perf_counter

import c10s_f5_component_profile_score as profile
from c10s_f5_rational_score_polynomials import beta_binomial_global_mle_certificate


R = 20
HISTOGRAM = {0: 1, 2: 2, 5: 4, 8: 5, 10: 6, 12: 5, 15: 4, 18: 2, 20: 1}
TIMINGS = {
    "score_polynomial_seconds": 0.0,
    "root_isolation_seconds": 0.0,
    "likelihood_enclosure_seconds": 0.0,
    "boundary_profile_seconds": 0.0,
    "log_enclosure_seconds": 0.0,
}
COUNTS = {
    "score_polynomial_calls": 0,
    "root_isolation_calls": 0,
    "likelihood_enclosure_calls": 0,
    "boundary_profile_calls": 0,
    "log_enclosure_calls": 0,
}


def timed(name, counter, original):
    def wrapper(*args, **kwargs):
        started = perf_counter()
        try:
            return original(*args, **kwargs)
        finally:
            TIMINGS[name] += perf_counter() - started
            COUNTS[counter] += 1
    return wrapper


def main() -> None:
    started = perf_counter()
    certificate = beta_binomial_global_mle_certificate(
        R, HISTOGRAM, max_refinements=1, projection_bits=12,
        max_projection_depth=40, max_lift_intervals=100,
        max_lift_depth=20, max_mu_depth=10,
        source_revision="0123456789abcdef0123456789abcdef01234567",
    )
    certificate_seconds = perf_counter() - started
    print(json.dumps({
        "stage": "global_certificate",
        "seconds": round(certificate_seconds, 6),
        "status": certificate.get("status"),
        "fixture": "M30_R20",
        "n": sum(HISTOGRAM.values()),
    }, sort_keys=True), flush=True)

    # Instrument the actual stage boundaries called by the production API.
    # Timers are disjoint: score construction, all Sturm isolations,
    # candidate likelihood enclosures, analytic boundary profiles, and LR logs.
    profile.f5_component_profile_score_polynomial = timed(
        "score_polynomial_seconds", "score_polynomial_calls",
        profile.f5_component_profile_score_polynomial,
    )
    profile._uni_isolate_squarefree_unit_roots = timed(
        "root_isolation_seconds", "root_isolation_calls",
        profile._uni_isolate_squarefree_unit_roots,
    )
    profile._beta_binomial_likelihood_enclosure = timed(
        "likelihood_enclosure_seconds", "likelihood_enclosure_calls",
        profile._beta_binomial_likelihood_enclosure,
    )
    profile._boundary_profile_likelihood = timed(
        "boundary_profile_seconds", "boundary_profile_calls",
        profile._boundary_profile_likelihood,
    )
    profile._log_positive_fraction_interval = timed(
        "log_enclosure_seconds", "log_enclosure_calls",
        profile._log_positive_fraction_interval,
    )

    started = perf_counter()
    result = profile.f5_component_profile_lr_statistic(
        R, HISTOGRAM, component="W",
        target=Fraction(1, 20),
        global_certificate=certificate,
        root_isolation_width=Fraction(1, 2**40),
        max_depth=140, max_intervals=5000,
        log_series_terms=80,
    )
    total_seconds = perf_counter() - started
    accounted = sum(TIMINGS.values())
    print(json.dumps({
        "stage": "M30_R20_W_profile_instrumentation",
        "fixture": "M30_R20",
        "component": "W",
        "target": "1/20",
        "total_seconds": round(total_seconds, 6),
        "instrumented_seconds": round(accounted, 6),
        "unattributed_seconds": round(total_seconds - accounted, 6),
        "timings": {k: round(v, 6) for k, v in TIMINGS.items()},
        "calls": COUNTS,
        "lr_status": result.get("status"),
        "profile_status": result.get("profile", {}).get("status"),
        "candidate_count": result.get("profile", {}).get("candidate_count"),
        "interior_stationary_count": result.get("profile", {}).get("interior_stationary_count"),
    }, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
