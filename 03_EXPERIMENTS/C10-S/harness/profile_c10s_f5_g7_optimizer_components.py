"""Resource-only timing decomposition of the F5 G7 per-dataset execution path.

Runs one dataset in each frozen G7 cell with the disjoint RESOURCE_NAMESPACE.
No holdout seeds, coverage adjudication, K/B changes, or method selection.
"""
from __future__ import annotations

import json
import resource
import statistics
import time
from collections import Counter, defaultdict
from pathlib import Path

import c10s_f5_beta_binomial_likelihood_diagnostics as diagnostic
import c10s_fitted_beta_binomial_bootstrap as fitted
import c10s_nested_mr_comparative_inference_engine as engine
import run_c10s_f5_g7_tiera_calibration as g7


def profile(output: Path) -> dict:
    timings: dict[str, list[float]] = defaultdict(list)
    calls: Counter[str] = Counter()
    current = {"cell": "UNSET", "replicate": -1}

    def wrap(module, name: str, key: str, *, method_key=None):
        original = getattr(module, name)

        def measured(*args, **kwargs):
            label = key
            if method_key is not None:
                method = kwargs.get("method")
                if method is None and len(args) >= 3:
                    method = args[2]
                label = method_key(method)
            started = time.perf_counter()
            try:
                return original(*args, **kwargs)
            finally:
                elapsed = time.perf_counter() - started
                dataset = f'{current["cell"]}:{current["replicate"]:06d}'
                timings[f"{dataset}/{label}"].append(elapsed)
                calls[label] += 1
        setattr(module, name, measured)

    # P: production finite-difference L-BFGS-B (three starts).
    wrap(fitted, "minimize", "unused", method_key=lambda method: (
        "P_production_LBFGSB" if method == "L-BFGS-B" else f"P_other_{method}"
    ))
    # A and I: analytic-gradient L-BFGS-B (three starts), then log(alpha)/log(beta) BFGS.
    wrap(diagnostic, "minimize", "unused", method_key=lambda method: (
        "A_analytic_gradient_LBFGSB" if method == "L-BFGS-B"
        else "I_independent_coordinate_BFGS" if method == "BFGS"
        else f"diagnostic_other_{method}"
    ))
    wrap(fitted, "beta_binomial_global_mle_certificate", "exact_global_certificate")
    wrap(fitted, "_vectorized_bernoulli_bootstrap_components", "C5_vectorized_bootstrap")
    wrap(engine, "_frozen_v002_baseline", "C0_frozen_baseline")
    wrap(g7, "generate_holdout_dataset", "dataset_generation")
    wrap(g7, "compare_dataset", "full_compare_dataset")

    g7.validate_seed_separation()
    dataset_records = []
    wall_started = time.perf_counter()
    cpu_started = time.process_time()

    for spec in g7.f5_specs():
        current["cell"] = spec.cell_id
        current["replicate"] = 0
        started = time.perf_counter()
        result = g7.run_cell(
            spec, k=1, c0_b=g7.C0_B, c5_b=g7.C5_B,
            seed_namespace=g7.RESOURCE_NAMESPACE, adjudicate=False,
        )
        wall = time.perf_counter() - started
        for record in result["records"]:
            candidate = record["comparison"]["candidates"][0]["comparison"]
            provenance = dict(candidate.get("provenance", []))
            dataset_records.append({
                "cell_id": spec.cell_id,
                "replicate": 0,
                "dataset_id": record["dataset_id"],
                "global_mle_certificate_status": provenance.get(
                    "global_mle_certificate_status", "MISSING"
                ),
                "interval_emitted_within": candidate.get("within_interval") is not None,
                "interval_emitted_raw_between": candidate.get("between_interval") is not None,
                "abstention_reason": candidate.get("abstention_reason"),
                "wall_seconds": wall,
            })
        del result

    wall_elapsed = time.perf_counter() - wall_started
    cpu_elapsed = time.process_time() - cpu_started
    component_rows = []
    for key, values in sorted(timings.items()):
        component_rows.append({
            "dataset": key.split("/", 1)[0],
            "component": key.split("/", 1)[1],
            "calls": len(values),
            "total_wall_seconds": sum(values),
            "mean_wall_seconds": statistics.fmean(values),
            "max_wall_seconds": max(values),
        })

    payload = {
        "schema": "C10S-F5-G7-OPTIMIZER-COMPONENT-PROFILE-001",
        "scope": "RESOURCE_ONLY_TWO_DATASETS_NO_COVERAGE_NO_HOLDOUT",
        "seed_namespace": g7.RESOURCE_NAMESPACE,
        "k_per_cell": 1,
        "C0_bootstrap_replicates": g7.C0_B,
        "C5_bootstrap_replicates": g7.C5_B,
        "wall_elapsed_seconds": wall_elapsed,
        "process_cpu_seconds": cpu_elapsed,
        "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "call_counts_by_component": dict(sorted(calls.items())),
        "dataset_results": dataset_records,
        "component_timings": component_rows,
        "interpretation": (
            "Timing decomposition only. P is the production fit; A and I are "
            "diagnostic-only paths. No coverage, calibration, or method-selection claim."
        ),
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(payload, sort_keys=True, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(payload, sort_keys=True, indent=2, allow_nan=False))
    return payload


def main() -> int:
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    profile(args.output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
