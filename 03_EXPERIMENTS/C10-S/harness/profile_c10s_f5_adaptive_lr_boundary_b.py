from __future__ import annotations

import json
from fractions import Fraction
from time import perf_counter

import c10s_f5_component_profile_score as profile
import c10s_f5_rational_score_polynomials as rational
from c10s_f5_adaptive_profile_lr import adaptive_refine_lr_results
from c10s_f5_sturm_call_instrumentation import (
    install_sturm_call_instrumentation,
    primitive_integer_sturm_sequence,
    sign_variations_integer_certified_fixedpoint,
)


WIDTHS = tuple(Fraction(1, 2**power) for power in (8, 16, 24, 40))
CASES = [
    ("M30_R20_BOUNDARY_ONLY_B", 20, {0: 15, 20: 15}, "B", Fraction(483, 10)),
    ("M10_R5_ENDPOINT_ONLY_B", 5, {0: 5, 5: 5}, "B", Fraction(161, 10)),
]


def _summary_fraction_pair(values):
    if values is None:
        return None
    return [{
        "approx_decimal": format(float(value), ".16g"),
        "numerator_bits": abs(value.numerator).bit_length(),
        "denominator_bits": value.denominator.bit_length(),
    } for value in values]


def _run_case(name, r, histogram, component, cutoff):
    certificate = rational.beta_binomial_global_mle_certificate(
        r, histogram, max_refinements=1, projection_bits=12,
        max_projection_depth=40, max_lift_intervals=100,
        max_lift_depth=20, max_mu_depth=10,
        source_revision="0123456789abcdef0123456789abcdef01234567",
    )
    if certificate.get("status") not in {
        "GLOBAL_INTERIOR_MAXIMUM_CERTIFIED",
        "GLOBAL_BOUNDARY_SUPREMUM_CERTIFIED",
        "GLOBAL_CO_MAXIMIZERS_CERTIFIED",
    }:
        raise RuntimeError(f"GLOBAL_CERTIFICATE_UNRESOLVED:{name}:{certificate.get('status')}")

    original_sturm = rational._uni_sturm_sequence
    original_integer = rational._uni_sturm_integer_sequence
    diagnostics = []

    def evaluate(width):
        rational._uni_sturm_sequence = primitive_integer_sturm_sequence
        rational._uni_sturm_integer_sequence = lambda sequence: sequence
        calls, restore = install_sturm_call_instrumentation(
            profile, rational,
            variation_evaluator=sign_variations_integer_certified_fixedpoint,
        )
        started = perf_counter()
        try:
            result = profile.f5_component_profile_lr_statistic(
                r, histogram, component=component, target=Fraction(1, 20),
                global_certificate=certificate,
                root_isolation_width=width,
                max_depth=140, max_intervals=5000,
                log_series_terms=80,
            )
            elapsed = perf_counter() - started
        finally:
            restore()
            rational._uni_sturm_sequence = original_sturm
            rational._uni_sturm_integer_sequence = original_integer
        diagnostics.append({
            "width": str(width),
            "seconds": round(elapsed, 6),
            "root_calls": [{
                "degree": call.get("input_degree"),
                "status": call.get("status"),
                "processed_intervals": call.get("processed_intervals"),
                "exact_roots": call.get("exact_roots"),
                "isolating_intervals": call.get("isolating_intervals"),
                "unresolved_intervals": call.get("unresolved_intervals"),
            } for call in calls],
        })
        return result

    adaptive = adaptive_refine_lr_results(
        evaluate, cutoff=cutoff, widths=WIDTHS,
        classifier=profile._classify_profile_lr_result,
    )
    final_result = adaptive.get("last_result", {})
    return {
        "fixture": name,
        "R": r,
        "component": component,
        "cutoff": str(cutoff),
        "global_certificate_status": certificate.get("status"),
        "adaptive_status": adaptive.get("status"),
        "classification": adaptive.get("classification"),
        "selected_width": str(adaptive.get("selected_width")),
        "step_count": adaptive.get("step_count"),
        "lr_bounds": _summary_fraction_pair(adaptive.get("lr_statistic_bounds")),
        "history": [{
            "width": str(item["width"]),
            "classification": item["classification"],
            "lr_bounds": _summary_fraction_pair(item["lr_statistic_bounds"]),
        } for item in adaptive.get("history", [])],
        "final_profile_status": final_result.get("profile", {}).get("status"),
        "final_candidate_count": final_result.get("profile", {}).get("candidate_count"),
        "diagnostics": diagnostics,
    }


def main():
    cases = [_run_case(*case) for case in CASES]
    payload = {
        "stage": "F5_ADAPTIVE_LR_BOUNDARY_B_DIAGNOSTIC",
        "scope": "pointwise exact interval refinement only; not cutoff calibration or confidence-set topology",
        "width_schedule": [str(width) for width in WIDTHS],
        "cases": cases,
    }
    print(json.dumps(payload, sort_keys=True), flush=True)
    for case in cases:
        if case["adaptive_status"] != "ADAPTIVE_CLASSIFIED":
            raise RuntimeError(f"ADAPTIVE_CASE_NOT_CLASSIFIED:{case}")
        if case["classification"] not in {"IN", "OUT"}:
            raise RuntimeError(f"ADAPTIVE_BAD_CLASSIFICATION:{case}")


if __name__ == "__main__":
    main()
