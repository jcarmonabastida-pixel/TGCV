"""Full resource-only G7 timing sample with per-dataset latency and shard projections.

Runs the frozen RESOURCE_K_PER_CELL datasets in each G7 cell, with C0/C5 B=1000.
It never uses holdout seeds and never performs coverage adjudication.
"""
from __future__ import annotations

import json
import math
import resource
import statistics
import time
from collections import Counter, defaultdict
from pathlib import Path

import run_c10s_f5_g7_tiera_calibration as g7

METHOD_ID = "F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.0"
MAX_PARALLEL = 20
SHARD_SIZES = (25, 40, 50, 100)


def percentile(values: list[float], probability: float) -> float:
    ordered = sorted(values)
    if not ordered:
        raise ValueError("EMPTY_RESOURCE_SAMPLE")
    index = max(0, min(len(ordered) - 1, math.ceil(probability * len(ordered)) - 1))
    return ordered[index]


def profile(output: Path) -> dict:
    timings: dict[str, list[float]] = defaultdict(list)
    observations: dict[str, list[dict]] = defaultdict(list)
    current = {"cell_id": "UNSET"}

    original = g7.compare_dataset

    def measured_compare(*args, **kwargs):
        started = time.perf_counter()
        result = original(*args, **kwargs)
        elapsed = time.perf_counter() - started
        cell_id = current["cell_id"]
        candidate = next(
            item for item in result.candidates if item.method_id == METHOD_ID
        )
        comparison = candidate.comparison
        provenance = dict(comparison.provenance)
        dataset_id = kwargs.get("dataset_id")
        if dataset_id is None and len(args) > 1:
            dataset_id = args[1]
        timings[cell_id].append(elapsed)
        observations[cell_id].append({
            "dataset_id": dataset_id,
            "wall_seconds": elapsed,
            "global_mle_certificate_status": provenance.get(
                "global_mle_certificate_status", "MISSING"
            ),
            "within_interval_emitted": comparison.within_interval is not None,
            "between_interval_emitted": comparison.between_interval is not None,
            "abstention_reason": comparison.abstention_reason,
        })
        return result

    g7.compare_dataset = measured_compare
    try:
        g7.validate_seed_separation()
        wall_started = time.perf_counter()
        cpu_started = time.process_time()
        cell_summaries = []
        for spec in g7.f5_specs():
            current["cell_id"] = spec.cell_id
            result = g7.run_cell(
                spec,
                k=g7.RESOURCE_K_PER_CELL,
                c0_b=g7.C0_B,
                c5_b=g7.C5_B,
                seed_namespace=g7.RESOURCE_NAMESPACE,
                adjudicate=False,
            )
            cell_summaries.append({
                "cell_id": spec.cell_id,
                "datasets_completed": result["datasets_completed"],
                "coverage_adjudication": result["coverage_adjudication"],
                "certificate_status_counts": dict(Counter(
                    row["global_mle_certificate_status"]
                    for row in observations[spec.cell_id]
                )),
                "interval_emission_counts": {
                    "within": sum(row["within_interval_emitted"] for row in observations[spec.cell_id]),
                    "between": sum(row["between_interval_emitted"] for row in observations[spec.cell_id]),
                },
                "latency_seconds": {
                    "mean": statistics.fmean(timings[spec.cell_id]),
                    "median": statistics.median(timings[spec.cell_id]),
                    "p90": percentile(timings[spec.cell_id], 0.90),
                    "p95": percentile(timings[spec.cell_id], 0.95),
                    "p99": percentile(timings[spec.cell_id], 0.99),
                    "max": max(timings[spec.cell_id]),
                    "total": sum(timings[spec.cell_id]),
                },
            })
            del result
        wall_elapsed = time.perf_counter() - wall_started
        cpu_elapsed = time.process_time() - cpu_started
    finally:
        g7.compare_dataset = original

    p95_max = max(percentile(timings[cell], 0.95) for cell in timings)
    p99_max = max(percentile(timings[cell], 0.99) for cell in timings)
    shard_projections = []
    for shard_size in SHARD_SIZES:
        shards_per_cell = math.ceil(g7.K_PER_CELL / shard_size)
        total_jobs_per_phase = len(g7.EXPECTED_CELLS) * shards_per_cell
        waves = math.ceil(total_jobs_per_phase / MAX_PARALLEL)
        p95_job_seconds = shard_size * p95_max
        p99_job_seconds = shard_size * p99_max
        phase_p95_seconds = waves * p95_job_seconds
        phase_p99_seconds = waves * p99_job_seconds
        shard_projections.append({
            "datasets_per_shard": shard_size,
            "shards_per_cell": shards_per_cell,
            "jobs_per_phase": total_jobs_per_phase,
            "max_parallel_jobs": MAX_PARALLEL,
            "conservative_waves_per_phase": waves,
            "p95_shard_runtime_seconds": p95_job_seconds,
            "p99_shard_runtime_seconds": p99_job_seconds,
            "primary_plus_replay_p95_wall_seconds": 2 * phase_p95_seconds,
            "primary_plus_replay_p99_wall_seconds": 2 * phase_p99_seconds,
            "single_shard_under_150_minutes_at_p99": p99_job_seconds <= 9000,
        })

    payload = {
        "schema": "C10S-F5-G7-RESOURCE-PREFLIGHT-PARALLEL-PROFILE-001",
        "scope": "RESOURCE_NAMESPACE_ONLY_K100_PER_CELL_NO_COVERAGE_NO_HOLDOUT",
        "seed_namespace": g7.RESOURCE_NAMESPACE,
        "K_per_cell": g7.RESOURCE_K_PER_CELL,
        "C0_B": g7.C0_B,
        "C5_B": g7.C5_B,
        "wall_elapsed_seconds": wall_elapsed,
        "process_cpu_seconds": cpu_elapsed,
        "peak_rss_kib": resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
        "cells": cell_summaries,
        "conservative_shard_projections": shard_projections,
        "dataset_timings": {
            cell: rows for cell, rows in observations.items()
        },
        "coverage_adjudication": "NOT_PERFORMED",
        "interpretation": (
            "Resource-only timing and shard scheduling evidence. Certificate statuses "
            "and interval emission are recorded as execution diagnostics, not coverage. "
            "No holdout, method selection, or calibration claim."
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
