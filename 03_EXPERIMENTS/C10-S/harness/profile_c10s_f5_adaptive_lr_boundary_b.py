from __future__ import annotations

import json
from fractions import Fraction
from time import perf_counter

from c10s_f5_component_profile_score import (
    f5_component_profile_lr_statistic_adaptive,
)
from c10s_f5_rational_score_polynomials import beta_binomial_global_mle_certificate

TARGET = Fraction(1, 20)
WIDTHS = (Fraction(1, 2**8), Fraction(1, 2**16), Fraction(1, 2**24))
CASES = (
    ("M30_R20_BOUNDARY_ONLY_B", 20, {0: 15, 20: 15}, Fraction(483, 10)),
    ("M10_R5_ENDPOINT_ONLY_B", 5, {0: 5, 5: 5}, Fraction(161, 10)),
)


def main():
    outputs = []
    for name, r, histogram, cutoff in CASES:
        started = perf_counter()
        certificate = beta_binomial_global_mle_certificate(
            r, histogram, max_refinements=1, projection_bits=12,
            max_projection_depth=40, max_lift_intervals=100,
            max_lift_depth=20, max_mu_depth=10,
            source_revision="0123456789abcdef0123456789abcdef01234567",
        )
        result = f5_component_profile_lr_statistic_adaptive(
            r, histogram, component="B", target=TARGET, cutoff=cutoff,
            global_certificate=certificate, isolation_widths=WIDTHS,
            max_depth=180, max_intervals=10000, log_series_terms=100,
        )
        elapsed = perf_counter() - started
        adaptive = result.get("adaptive_refinement", {})
        record = {
            "fixture": name,
            "cutoff_diagnostic_only": str(cutoff),
            "global_mle_status": certificate.get("status"),
            "status": result.get("status"),
            "classification": adaptive.get("classification"),
            "adaptive_status": adaptive.get("status"),
            "lr_statistic_bounds": [
                format(float(x), ".16g") if isinstance(x, Fraction) else str(x)
                for x in (result.get("lr_statistic_bounds") or ())
            ],
            "history": [{
                "width": str(item["width"]),
                "status": item["status"],
                "classification": item.get("classification"),
                "lr_bounds": [
                    format(float(x), ".16g") if isinstance(x, Fraction) else str(x)
                    for x in item.get("lr_statistic_bounds", ())
                ],
            } for item in adaptive.get("history", ())],
            "elapsed_seconds": round(elapsed, 6),
            "candidate_count": result.get("profile", {}).get("candidate_count"),
            "interior_stationary_count": result.get("profile", {}).get("interior_stationary_count"),
        }
        outputs.append(record)
        print(json.dumps(record, sort_keys=True), flush=True)
        if adaptive.get("classification") not in {"IN", "OUT"}:
            raise RuntimeError(f"ADAPTIVE_CLASSIFICATION_UNRESOLVED: {name}: {record}")
    print(json.dumps({
        "stage": "F5_ADAPTIVE_LR_BOUNDARY_B_DIAGNOSTIC",
        "scope": "pointwise exact interval refinement only; not cutoff calibration or confidence-set topology",
        "cases": outputs,
    }, sort_keys=True), flush=True)


if __name__ == "__main__":
    main()
