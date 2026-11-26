from __future__ import annotations

import cProfile
import io
import json
from fractions import Fraction
from pstats import Stats
from time import perf_counter

from c10s_f5_component_profile_score import f5_component_profile_lr_statistic
from c10s_f5_rational_score_polynomials import beta_binomial_global_mle_certificate


def main() -> None:
    r = 5
    histogram = {0: 1, 1: 2, 2: 2, 3: 2, 4: 2, 5: 1}

    started = perf_counter()
    certificate = beta_binomial_global_mle_certificate(
        r, histogram, max_refinements=1, projection_bits=12,
        max_projection_depth=40, max_lift_intervals=100,
        max_lift_depth=20, max_mu_depth=10,
        source_revision="0123456789abcdef0123456789abcdef01234567",
    )
    certificate_seconds = perf_counter() - started
    print(json.dumps({
        "stage": "unrestricted_global_mle_certificate",
        "seconds": round(certificate_seconds, 6),
        "status": certificate.get("status"),
    }, sort_keys=True), flush=True)

    for component in ("W", "B"):
        profiler = cProfile.Profile()
        started = perf_counter()
        profiler.enable()
        result = f5_component_profile_lr_statistic(
            r, histogram, component=component,
            target=Fraction(1, 20),
            global_certificate=certificate,
            root_isolation_width=Fraction(1, 2**40),
            max_depth=140, max_intervals=5000,
            log_series_terms=80,
        )
        profiler.disable()
        elapsed = perf_counter() - started

        stream = io.StringIO()
        Stats(profiler, stream=stream).strip_dirs().sort_stats("cumtime").print_stats(14)
        print(json.dumps({
            "stage": "fixed_target_lr_statistic",
            "component": component,
            "seconds": round(elapsed, 6),
            "status": result.get("status"),
            "profile_status": result.get("profile", {}).get("status"),
            "candidate_count": result.get("profile", {}).get("candidate_count"),
            "cprofile_top_cumulative": stream.getvalue(),
        }, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
