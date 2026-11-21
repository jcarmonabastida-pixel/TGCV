"""Bounded resource-only component profiler for the frozen F5 G7 workload.

This diagnostic executes two RESOURCE_NAMESPACE datasets per cell with the
frozen C0/C5 bootstrap counts. It never uses holdout seeds or adjudicates
coverage. Timings are observational and do not enter scientific outputs.
"""
from __future__ import annotations

import argparse
import json
import os
import resource
import statistics
import time
from collections import Counter, defaultdict
from pathlib import Path

import c10s_fitted_beta_binomial_bootstrap as c5
import c10s_nested_mr_comparative_inference_engine as engine
import run_c10s_f5_g7_tiera_calibration as g7


def _instrument(module, name: str, key: str, timings: dict[str, list[float]]) -> None:
    original = getattr(module, name)

    def wrapped(*args, **kwargs):
        started = time.perf_counter()
        try:
            return original(*args, **kwargs)
        finally:
            timings[key].append(time.perf_counter() - started)

    setattr(module, name, wrapped)


def profile() -> dict:
    timings: dict[str, list[float]] = defaultdict(list)
    _instrument(engine, "_frozen_v002_baseline", "C0_baseline_total", timings)
    _instrument(engine, "fitted_beta_binomial_parametric_bootstrap", "C5_total", timings)
    _instrument(g7, "generate_holdout_dataset", "dataset_generation", timings)
    _instrument(g7, "compare_dataset", "comparison_total", timings)
    _instrument(c5, "audit_beta_binomial_count_fit", "analytic_optimizer_audit", timings)
    _instrument(c5, "fit_beta_binomial_counts", "production_multistart_fit", timings)
    _instrument(c5, "beta_binomial_global_mle_certificate", "exact_global_certificate", timings)
    _instrument(c5, "_vectorized_bernoulli_bootstrap_components", "C5_vectorized_bootstrap_kernel", timings)

    cells = []
    wall_started = time.perf_counter()
    cpu_started = time.process_time()
    for spec in g7.f5_specs():
        result = g7.run_cell(
            spec,
            k=2,
            c0_b=g7.C0_B,
            c5_b=g7.C5_B,
            seed_namespace=g7.RESOURCE_NAMESPACE,
            adjudicate=False,
        )
        statuses = Counter()
        for record in result["records"]:
            candidate = record["comparison"]["candidates"][0]["comparison"]
            status = dict(candidate.get("provenance", [])).get(
                "global_mle_certificate_status", "MISSING"
            )
            statuses[status] += 1
        cells.append({
            "cell_id": spec.cell_id,
            "datasets": result["datasets_completed"],
            "global_mle_certificate_status_counts": dict(sorted(statuses.items())),
        })

    wall_elapsed = time.perf_counter() - wall_started
    cpu_elapsed = time.process_time() - cpu_started
    component_timings = {}
    for key, values in sorted(timings.items()):
        component_timings[key] = {
            "calls": len(values),
            "total_wall_seconds": sum(values),
            "mean_wall_seconds": statistics.fmean(values) if values else 0.0,
            "max_wall_seconds": max(values) if values else 0.0,
        }
    return {
        "schema": "C10S-F5-G7-RESOURCE-COMPONENT-PROFILE-001",
        "profile_scope": "RESOURCE_ONLY_NO_COVERAGE_ADJUDICATION_NO_HOLDOUT",
        "seed_namespace": g7.RESOURCE_NAMESPACE,
        "datasets_per_cell": 2,
        "c0_bootstrap_replicates_per_dataset": g7.C0_B,
        "c5_bootstrap_replicates_per_dataset": g7.C5_B,
        "wall_elapsed_seconds": wall_elapsed,
        "process_cpu_seconds": cpu_elapsed,
        "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "cells": cells,
        "component_timings": component_timings,
        "interpretation": "Diagnostic timing only; no coverage or calibration claim.",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = profile()
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(
        json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, sort_keys=True, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
