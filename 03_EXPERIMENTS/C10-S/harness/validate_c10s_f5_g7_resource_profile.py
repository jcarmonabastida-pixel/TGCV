"""Validate and schedule from one immutable resource-only G7 profile artifact."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import subprocess
from pathlib import Path

import run_c10s_f5_g7_tiera_calibration as g7

PROFILE_SCHEMA = "C10S-F5-G7-RESOURCE-PREFLIGHT-PARALLEL-PROFILE-002"
PROFILE_SCOPE = "RESOURCE_NAMESPACE_ONLY_K100_PER_CELL_TIMING_ONLY_NO_OUTCOME_INSPECTION_NO_COVERAGE_NO_HOLDOUT"
from c10s_f5_g7_source_inventory import compute_path_paths, build_manifests

PROFILE_SOURCE_PATHS = compute_path_paths()

MAX_PARALLEL = 20
JOB_SETUP_OVERHEAD_SECONDS = 300
JOB_BUDGET_SECONDS = 9000  # 150 minutes; workflow hard timeout is 165 minutes.
CANDIDATE_SHARD_SIZES = (10, 20, 25, 40, 50, 100)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def validate(profile_path: Path, manifest_path: Path, root: Path) -> dict:
    profile_bytes = profile_path.read_bytes()
    profile_sha = sha256_bytes(profile_bytes)
    profile = json.loads(profile_bytes)
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    if manifest.get("schema") != "C10S-F5-G7-RESOURCE-PROFILE-MANIFEST-002":
        raise ValueError("G7_RESOURCE_PROFILE_MANIFEST_SCHEMA_MISMATCH")
    if manifest.get("profile_json_sha256") != profile_sha:
        raise ValueError("G7_RESOURCE_PROFILE_JSON_DIGEST_MISMATCH")
    source_commit = manifest.get("profile_source_commit")
    if not isinstance(source_commit, str) or not re.fullmatch(r"[0-9a-f]{40}", source_commit):
        raise ValueError("G7_RESOURCE_PROFILE_SOURCE_COMMIT_INVALID")
    if type(manifest.get("profile_run_id")) is not int or manifest["profile_run_id"] <= 0:
        raise ValueError("G7_RESOURCE_PROFILE_RUN_ID_INVALID")
    if type(manifest.get("profile_artifact_id")) is not int or manifest["profile_artifact_id"] <= 0:
        raise ValueError("G7_RESOURCE_PROFILE_ARTIFACT_ID_INVALID")
    if not re.fullmatch(r"[0-9a-f]{64}", manifest.get("profile_artifact_archive_sha256", "")):
        raise ValueError("G7_RESOURCE_PROFILE_ARCHIVE_DIGEST_INVALID")
    if not re.fullmatch(r"[0-9a-f]{64}", manifest.get("profile_json_sha256", "")):
        raise ValueError("G7_RESOURCE_PROFILE_JSON_DIGEST_INVALID")
    if (
        profile.get("schema") != PROFILE_SCHEMA
        or profile.get("scope") != PROFILE_SCOPE
        or profile.get("seed_namespace") != g7.RESOURCE_NAMESPACE
        or profile.get("K_per_cell") != g7.RESOURCE_K_PER_CELL
        or profile.get("C0_B") != g7.C0_B
        or profile.get("C5_B") != g7.C5_B
        or profile.get("coverage_adjudication") != "NOT_PERFORMED"
        or profile.get("source_commit") != source_commit
    ):
        raise ValueError("G7_RESOURCE_PROFILE_PROTOCOL_MISMATCH")
    if profile.get("wall_elapsed_seconds", JOB_BUDGET_SECONDS + 1) > JOB_BUDGET_SECONDS:
        raise ValueError("G7_RESOURCE_PROFILE_EXECUTION_EXCEEDED_150_MINUTES")
    cells = {item.get("cell_id"): item for item in profile.get("cells", [])}
    if set(cells) != set(g7.EXPECTED_CELLS):
        raise ValueError("G7_RESOURCE_PROFILE_CELL_ROSTER_MISMATCH")
    for cell_id in g7.EXPECTED_CELLS:
        cell = cells[cell_id]
        if cell.get("datasets_completed") != g7.RESOURCE_K_PER_CELL:
            raise ValueError(f"G7_RESOURCE_PROFILE_DENOMINATOR_INCOMPLETE:{cell_id}")
        latency = cell.get("latency_seconds", {})
        if not all(isinstance(latency.get(key), (int, float)) and latency[key] > 0 for key in ("mean", "p95", "p99", "max")):
            raise ValueError(f"G7_RESOURCE_PROFILE_LATENCY_SUMMARY_INVALID:{cell_id}")

    # Compare compute-path manifests generated from immutable Git trees.
    current_commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    current_compute = build_manifests(root, current_commit, roles=("compute_path",), inventory_commit=current_commit)["compute_path"]
    measured_compute = build_manifests(root, source_commit, roles=("compute_path",), inventory_commit=current_commit)["compute_path"]
    if tuple(item["path"] for item in current_compute["entries"]) != PROFILE_SOURCE_PATHS:
        raise ValueError("G7_COMPUTE_PATH_INVENTORY_MANIFEST_MISMATCH")
    ancestor = subprocess.run(
        ["git", "merge-base", "--is-ancestor", source_commit, "HEAD"],
        cwd=root, check=False,
    )
    if ancestor.returncode != 0:
        raise ValueError("G7_RESOURCE_PROFILE_SOURCE_NOT_ANCESTOR")
    if measured_compute["content_sha256"] != current_compute["content_sha256"]:
        raise ValueError("G7_RESOURCE_PROFILE_COMPUTE_PATH_CHANGED")

    # Use the worst observed per-dataset latency, not only the mean or p95.
    max_observed_dataset_seconds = max(
        cells[cell_id]["latency_seconds"]["max"] for cell_id in g7.EXPECTED_CELLS
    )
    candidate_projections = []
    for size in CANDIDATE_SHARD_SIZES:
        per_cell = {}
        total_jobs = 0
        total_runner_compute_seconds = 0.0
        paired_job_runtimes = []
        safe = True
        for cell_id in g7.EXPECTED_CELLS:
            shard_count = math.ceil(g7.K_PER_CELL / size)
            phase_shard_runtime = (
                size * cells[cell_id]["latency_seconds"]["max"]
                + JOB_SETUP_OVERHEAD_SECONDS
            )
            # Each matrix job runs primary and clean-source replay sequentially.
            # max-parallel is shared by the entire matrix, not reset per cell.
            paired_job_runtime = 2 * phase_shard_runtime
            safe = safe and paired_job_runtime <= JOB_BUDGET_SECONDS
            total_jobs += shard_count
            total_runner_compute_seconds += shard_count * paired_job_runtime
            paired_job_runtimes.append(paired_job_runtime)
            per_cell[cell_id] = {
                "shards": shard_count,
                "max_observed_phase_shard_runtime_seconds": phase_shard_runtime,
                "max_observed_primary_replay_job_runtime_seconds": paired_job_runtime,
                "aggregate_primary_replay_compute_seconds": shard_count * paired_job_runtime,
            }

        # Graham's list-scheduling bound: W/m + (1 - 1/m) * p_max.
        # This is conservative for a single shared pool of MAX_PARALLEL matrix
        # jobs and avoids incorrectly granting each cell its own 20 runners.
        max_paired_job_runtime = max(paired_job_runtimes)
        wall_lower_bound = total_runner_compute_seconds / MAX_PARALLEL
        wall_scheduling_tail = (1 - 1 / MAX_PARALLEL) * max_paired_job_runtime
        conservative_wall = wall_lower_bound + wall_scheduling_tail
        candidate_projections.append({
            "datasets_per_shard": size,
            "safe_primary_replay_pair_under_150_minute_job_budget": safe,
            "shard_tasks_per_phase": total_jobs,
            "primary_replay_aggregate_compute_hours": total_runner_compute_seconds / 3600,
            "shared_matrix_wall_workload_lower_bound_seconds": wall_lower_bound,
            "shared_matrix_list_scheduling_tail_bound_seconds": wall_scheduling_tail,
            "conservative_primary_plus_replay_wall_seconds": conservative_wall,
            "per_cell": per_cell,
        })
    safe_projections = [
        item for item in candidate_projections
        if item["safe_primary_replay_pair_under_150_minute_job_budget"]
    ]
    if not safe_projections:
        raise ValueError("G7_NO_PRIMARY_REPLAY_SHARD_PAIR_MEETS_150_MINUTE_JOB_BUDGET")
    # Minimize the conservative end-to-end wall estimate, not the number of jobs.
    selected = min(
        safe_projections,
        key=lambda item: (
            item["conservative_primary_plus_replay_wall_seconds"],
            -item["datasets_per_shard"],
        ),
    )
    shard_size = selected["datasets_per_shard"]

    # Explicitly expose the unmeasured setup allowance as an assumption.
    # Sensitivity is computed from the already-frozen K=100 resource sample;
    # it does not run or inspect any scientific datasets.
    setup_sensitivity = []
    for overhead in (300, 600, 900):
        scenario_jobs = []
        scenario_work = 0.0
        scenario_safe = True
        for cell_id in g7.EXPECTED_CELLS:
            shard_count = math.ceil(g7.K_PER_CELL / shard_size)
            paired = 2 * (
                shard_size * cells[cell_id]["latency_seconds"]["max"] + overhead
            )
            scenario_safe = scenario_safe and paired <= JOB_BUDGET_SECONDS
            scenario_jobs.append(paired)
            scenario_work += shard_count * paired
        scenario_tail = (1 - 1 / MAX_PARALLEL) * max(scenario_jobs)
        setup_sensitivity.append({
            "per_phase_setup_allowance_seconds": overhead,
            "max_paired_job_seconds": max(scenario_jobs),
            "within_150_minute_job_budget": scenario_safe,
            "shared_pool_list_scheduling_bound_seconds": scenario_work / MAX_PARALLEL + scenario_tail,
            "interpretation": "ENGINEERING_ASSUMPTION_NOT_MEASURED" if overhead == JOB_SETUP_OVERHEAD_SECONDS else "SENSITIVITY_SCENARIO",
        })

    profile_k = profile["K_per_cell"]
    p99_sample_max_exceedance_probability = 1 - (0.99 ** profile_k)

    shard_matrix = []
    for cell_id in g7.EXPECTED_CELLS:
        for start in range(0, g7.K_PER_CELL, shard_size):
            shard_matrix.append({
                "cell_id": cell_id,
                "replicate_start": start,
                "replicate_count": min(shard_size, g7.K_PER_CELL - start),
            })

    primary_replay_upper = selected["conservative_primary_plus_replay_wall_seconds"]
    resource_wall = float(profile["wall_elapsed_seconds"])
    aggregate_compute_hours = (
        2 * sum(
            g7.K_PER_CELL * cells[cell_id]["latency_seconds"]["mean"]
            for cell_id in g7.EXPECTED_CELLS
        ) / 3600
    )
    return {
        "schema": "TGCV-C10S-F5-G7-RESOURCE-PROFILE-VALIDATION-001",
        "compute_path_manifest_sha256": current_compute["root_sha256"],
        "compute_path_content_sha256": current_compute["content_sha256"],
        "profile_run_id": manifest["profile_run_id"],
        "profile_source_commit": source_commit,
        "profile_json_sha256": profile_sha,
        "profile_artifact_archive_sha256": manifest["profile_artifact_archive_sha256"],
        "resource_preflight_wall_seconds": resource_wall,
        "max_observed_dataset_seconds": max_observed_dataset_seconds,
        "datasets_per_shard": shard_size,
        "max_parallel_jobs": MAX_PARALLEL,
        "job_budget_seconds": JOB_BUDGET_SECONDS,
        "job_setup_overhead_seconds": JOB_SETUP_OVERHEAD_SECONDS,
        "job_setup_overhead_status": "ENGINEERING_RESERVE_NOT_EMPIRICALLY_MEASURED",
        "job_setup_overhead_sensitivity": setup_sensitivity,
        "resource_sample_k_per_cell": profile_k,
        "probability_sample_max_exceeds_true_p99_under_iid_assumption": p99_sample_max_exceedance_probability,
        "runtime_extrapolation_status": "CONDITIONAL_K100_SAMPLE_MAX_IS_NOT_A_K1000_HARD_BOUND",
        "shard_matrix": shard_matrix,
        "shard_tasks_per_phase": len(shard_matrix),
        "matrix_job_count": len(shard_matrix),
        "job_topology": "ONE_MATRIX_JOB_EXECUTES_PRIMARY_AND_CLEAN_SOURCE_REPLAY_SEQUENTIALLY",
        "candidate_shard_projections": candidate_projections,
        "selected_shard_projection": selected,
        "primary_plus_replay_conservative_wall_seconds": primary_replay_upper,
        "end_to_end_conservative_wall_seconds": resource_wall + primary_replay_upper,
        "primary_plus_replay_aggregate_compute_hours": aggregate_compute_hours,
        "cells": profile["cells"],
        "seed_separation_validation": "RECHECKED",
        "coverage_adjudication": "NOT_PERFORMED",
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--output-json", type=Path, required=True)
    args = parser.parse_args()
    g7.validate_seed_separation()
    result = validate(args.profile, args.manifest, args.root)
    args.output_json.write_text(
        json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
