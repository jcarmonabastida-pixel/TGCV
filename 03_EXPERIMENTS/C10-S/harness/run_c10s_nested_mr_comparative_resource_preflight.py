"""Bounded resource-only benchmark; never adjudicates or scores coverage."""
from __future__ import annotations

import argparse
import hashlib
import json
import resource
import time
from pathlib import Path

from c10s_nested_mr_fixtures import tier_a_specs
from c10s_nested_mr_comparative_inference_engine import compare_dataset
from run_c10s_nested_mr_comparative_holdout import (
    IMPLEMENTED_METHODS,
    generate_holdout_dataset,
)

PREFLIGHT_ID = "C10S-NESTED-MR-COMPARATIVE-RESOURCE-PREFLIGHT-001"
PREFLIGHT_NAMESPACE = "C10S-COMPARATIVE-RESOURCE-PREFLIGHT-1.0"
REPRESENTATIVE_CELLS = ("F1_balanced_M30_R20", "F5_beta22_M30_R20")
K_PER_CELL = 1000
C0_B = 1000
C5_B = 1000


def seed(namespace: str, cell_id: str, replicate: int) -> int:
    payload = f"{PREFLIGHT_NAMESPACE}|{namespace}|{cell_id}|{replicate}".encode()
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big")


def peak_rss_bytes() -> int:
    # Linux ru_maxrss is KiB; workflow is pinned to Ubuntu.
    return int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024)


def run_preflight(output: Path) -> dict:
    specs = {spec.cell_id: spec for spec in tier_a_specs()}
    results = []
    for cell_id in REPRESENTATIVE_CELLS:
        spec = specs[cell_id]
        comparisons = []
        truths = []
        records = []
        started = time.perf_counter()
        for replicate in range(K_PER_CELL):
            dataset_id = f"{PREFLIGHT_NAMESPACE}:{cell_id}:{replicate:06d}"
            dataset_seed = seed("dataset", cell_id, replicate)
            c0_seed = seed("C0", cell_id, replicate)
            c5_seed = seed("C5", cell_id, replicate)
            rows = generate_holdout_dataset(
                spec, replicate, seed_override=dataset_seed
            )
            comparison = compare_dataset(
                rows,
                dataset_id=dataset_id,
                family=spec.family,
                target_m=spec.m,
                target_r=spec.r,
                baseline_bootstrap_replicates=C0_B,
                baseline_bootstrap_seed=c0_seed,
                confidence_level=0.95,
                bootstrap_replicates=C5_B if spec.family == "F5" else None,
                bootstrap_seed=c5_seed if spec.family == "F5" else None,
                include_profile_diagnostics=False,
            )
            comparisons.append(comparison)
            truths.append((spec.true_within, spec.true_between))
            records.append({
                "dataset_id": dataset_id,
                "dataset_seed": dataset_seed,
                "C0_seed": c0_seed,
                "C5_seed": c5_seed if spec.family == "F5" else None,
            })
        elapsed = time.perf_counter() - started
        roster = {comparisons[0].baseline.method_id}
        roster.update(item.method_id for item in comparisons[0].candidates)
        if roster != set(IMPLEMENTED_METHODS[spec.family]):
            raise RuntimeError(f"method roster mismatch for {cell_id}")
        results.append({
            "cell_id": cell_id,
            "family": spec.family,
            "m": spec.m,
            "r": spec.r,
            "datasets": len(records),
            "C0_bootstrap_replicates_per_dataset": C0_B,
            "C5_bootstrap_replicates_per_dataset": C5_B if spec.family == "F5" else None,
            "method_roster": sorted(roster),
            "elapsed_seconds": elapsed,
            "seconds_per_dataset": elapsed / len(records),
            "peak_process_rss_bytes": peak_rss_bytes(),
            "records_retained_for_peak_memory_measurement": len(records),
            "coverage_adjudication": "NOT_RUN",
            "adjudicate_matched_datasets_called": False,
            "results_not_retained": True,
        })
        del comparisons, truths, records
    total_sampled = sum(item["datasets"] for item in results)
    output.mkdir(parents=True, exist_ok=True)
    payload = {
        "preflight_id": PREFLIGHT_ID,
        "namespace": PREFLIGHT_NAMESPACE,
        "cells": results,
        "total_datasets": total_sampled,
        "full_holdout_datasets": 8000,
        "coverage_adjudication": "NOT_RUN",
        "scientific_holdout_executed": False,
        "interpretation": "resource-only sample; extrapolation is advisory, not a coverage result",
    }
    (output / "resource_preflight.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    result = run_preflight(args.output_dir)
    print(json.dumps({
        "preflight_id": result["preflight_id"],
        "datasets": result["total_datasets"],
        "coverage_adjudication": "NOT_RUN",
        "scientific_holdout_executed": False,
    }, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
