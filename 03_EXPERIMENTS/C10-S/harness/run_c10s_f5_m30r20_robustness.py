from __future__ import annotations

import json
from fractions import Fraction
from time import perf_counter

from c10s_f5_component_profile_score import f5_component_profile_lr_statistic
from c10s_f5_rational_score_polynomials import beta_binomial_global_mle_certificate


def main() -> None:
    r = 20
    histogram = {0: 1, 2: 2, 5: 4, 8: 5, 10: 6, 12: 5, 15: 4, 18: 2, 20: 1}
    started = perf_counter()
    certificate = beta_binomial_global_mle_certificate(
        r, histogram, max_refinements=1, projection_bits=12,
        max_projection_depth=40, max_lift_intervals=100,
        max_lift_depth=20, max_mu_depth=10,
        source_revision="0123456789abcdef0123456789abcdef01234567",
    )
    print(json.dumps({
        "stage": "global_certificate",
        "seconds": round(perf_counter() - started, 6),
        "status": certificate.get("status"),
        "fixture": "M30_R20",
        "n": sum(histogram.values()),
    }), flush=True)
    for component in ("W", "B"):
        t0 = perf_counter()
        result = f5_component_profile_lr_statistic(
            r, histogram, component=component,
            target=Fraction(1, 20), global_certificate=certificate,
            root_isolation_width=Fraction(1, 2**40),
            max_depth=140, max_intervals=5000, log_series_terms=80,
        )
        print(json.dumps({
            "stage": "fixed_target_lr",
            "component": component,
            "seconds": round(perf_counter() - t0, 6),
            "status": result.get("status"),
            "profile_status": result.get("profile", {}).get("status"),
            "candidate_count": result.get("profile", {}).get("candidate_count"),
            "fixture": "M30_R20",
        }), flush=True)


if __name__ == "__main__":
    main()
