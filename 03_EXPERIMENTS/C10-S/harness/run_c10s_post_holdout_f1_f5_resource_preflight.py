"""Bounded F1/F5 post-holdout resource preflight; no coverage adjudication."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import resource
import subprocess
import sys
import time
from pathlib import Path

import numpy as np

from c10s_f1_between_profile_likelihood import (
    F1ProfileError,
    f1_profile_between_confidence_set,
    f1_profile_loglik,
)
from c10s_nested_mr_comparative_inference_engine import compare_dataset
from c10s_variance_comparison_interface import observed_nested_mr_result
from c10s_nested_mr_fixtures import tier_a_specs
from run_c10s_nested_mr_comparative_holdout import generate_holdout_dataset

PREFLIGHT_ID = "C10S-POST-HOLDOUT-F1-F5-RESOURCE-PREFLIGHT-001"
SEED_SCHEDULE_ID = "C10S_POST_HOLDOUT_F1_F5_DEV_PREFLIGHT_SEEDS_1.0"
SEED_NAMESPACE = "c10s_post_holdout_f1_f5_dev_preflight_v1"
REPRESENTATIVE_CELLS = ("F1_balanced_M30_R20", "F5_beta22_M30_R20")
K_PER_CELL = 100
C0_B = 1000
C5_B_PRIMARY = 1000
C5_B_SENSITIVITY = 4000
# Computational benchmark only. This conventional reference value is NOT a
# calibrated cutoff and is never used for coverage or scientific adjudication.
F1_PROFILE_BENCHMARK_CUTOFF = 3.841458820694124
SPEC_PATH = "03_EXPERIMENTS/C10-S/diagnostics/C10S_POST_HOLDOUT_F1_F5_DEVELOPMENT_CALIBRATION_SPEC_001.md"
LOCK_PATH = "03_EXPERIMENTS/C10-S/harness/requirements-vcont-integrated.lock"
HASH_PATHS = (
    SPEC_PATH,
    LOCK_PATH,
    "03_EXPERIMENTS/C10-S/harness/c10s_nested_mr_fixtures.py",
    "03_EXPERIMENTS/C10-S/harness/run_c10s_nested_mr_comparative_holdout.py",
    "03_EXPERIMENTS/C10-S/harness/c10s_nested_mr_comparative_inference_engine.py",
    "03_EXPERIMENTS/C10-S/harness/c10s_variance_comparison_interface.py",
    "03_EXPERIMENTS/C10-S/harness/c10s_f1_exact_pivotal_candidate.py",
    "03_EXPERIMENTS/C10-S/harness/c10s_f1_root_adjudication.py",
    "03_EXPERIMENTS/C10-S/harness/c10s_gaussian_variance_oracles.py",
    "03_EXPERIMENTS/C10-S/harness/c10s_f5_beta_binomial_mcse_profile.py",
    "03_EXPERIMENTS/C10-S/harness/theta_a_nested_mc_precision.py",
    "03_EXPERIMENTS/C10-S/harness/c10s_f1_between_profile_likelihood.py",
    "03_EXPERIMENTS/C10-S/harness/c10s_fitted_beta_binomial_bootstrap.py",
    "03_EXPERIMENTS/C10-S/harness/c10s_f5_beta_binomial_likelihood_diagnostics.py",
    "03_EXPERIMENTS/C10-S/harness/run_c10s_post_holdout_f1_f5_resource_preflight.py",
)

def derive_seed(stream: str, cell_id: str, replicate: int) -> int:
    if stream not in {
        "dataset", "C0_bootstrap", "C5_bootstrap_B1000",
        "C5_bootstrap_B4000",
    }:
        raise ValueError("UNKNOWN_PREFLIGHT_SEED_STREAM")
    if type(replicate) is not int or replicate < 0:
        raise ValueError("REPLICATE_MUST_BE_NONNEGATIVE_INTEGER")
    payload = (
        f"{SEED_SCHEDULE_ID}|{SEED_NAMESPACE}|{stream}|{cell_id}|{replicate}"
    ).encode("utf-8")
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big")

def _historical_seeds(cell_id: str, replicate: int) -> set[int]:
    """Reconstruct known v002 fixture, executed v1.0 and old preflight streams."""
    result = set()
    fixture_version = "C10S_NESTED_MR_SEED_SCHEDULE_1.0"
    for stream in ("fixture_dataset", "bootstrap"):
        payload = f"{fixture_version}|{stream}|{cell_id}|{replicate}".encode()
        result.add(int.from_bytes(hashlib.sha256(payload).digest()[:8], "big"))
    holdout_prefix = (
        "C10S_NESTED_MR_COMPARATIVE_HOLDOUT_SEEDS_1.0|"
        "c10s_nested_mr_comparative_holdout_v1|"
    )
    for stream in ("dataset", "C0_bootstrap", "C5_bootstrap"):
        payload = f"{holdout_prefix}{stream}|{cell_id}|{replicate}".encode()
        result.add(int.from_bytes(hashlib.sha256(payload).digest()[:8], "big"))
    old_prefix = "C10S-COMPARATIVE-RESOURCE-PREFLIGHT-1.0|"
    for stream in ("dataset", "C0", "C5"):
        payload = f"{old_prefix}{stream}|{cell_id}|{replicate}".encode()
        result.add(int.from_bytes(hashlib.sha256(payload).digest()[:8], "big"))
    return result

def validate_seed_separation() -> dict:
    # Compare against the complete historical Tier A/v1.0/old-preflight
    # inventories, not only matching replicate indices or the two sample cells.
    historical_values: set[int] = set()
    historical_count = 0
    historical_cells = tuple(spec.cell_id for spec in tier_a_specs())
    for cell_id in historical_cells:
        for replicate in range(1000):
            for value in _historical_seeds(cell_id, replicate):
                historical_count += 1
                historical_values.add(value)

    preflight_values: dict[int, tuple[str, str, int]] = {}
    for cell_id in REPRESENTATIVE_CELLS:
        streams = ["dataset", "C0_bootstrap"]
        if cell_id.startswith("F5_"):
            streams += ["C5_bootstrap_B1000", "C5_bootstrap_B4000"]
        for replicate in range(K_PER_CELL):
            for stream in streams:
                value = derive_seed(stream, cell_id, replicate)
                if value in historical_values:
                    raise RuntimeError(
                        f"PREFLIGHT_SEED_COLLIDES_WITH_HISTORICAL_SCHEDULE:{cell_id}:{replicate}:{stream}"
                    )
                previous = preflight_values.get(value)
                if previous is not None:
                    raise RuntimeError(
                        f"PREFLIGHT_SEED_COLLISION:{previous}:{(cell_id, stream, replicate)}"
                    )
                preflight_values[value] = (cell_id, stream, replicate)
    return {
        "status": "PASS",
        "preflight_seed_count": len(preflight_values),
        "historical_seed_values_checked": historical_count,
        "historical_replicates_per_cell_checked": 1000,
        "historical_cell_count": len(historical_cells),
        "historical_schedules": [
            "C10S_NESTED_MR_SEED_SCHEDULE_1.0",
            "C10S_NESTED_MR_COMPARATIVE_HOLDOUT_SEEDS_1.0",
            "C10S-COMPARATIVE-RESOURCE-PREFLIGHT-1.0",
        ],
    }

def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def peak_rss_bytes() -> int:
    # Ubuntu GitHub runner: ru_maxrss is KiB.
    return int(resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024)

def _specs():
    specs = {item.cell_id: item for item in tier_a_specs()}
    return [specs[cell] for cell in REPRESENTATIVE_CELLS]

def run_preflight(output: Path, *, execution_authorized: bool = False) -> dict:
    if execution_authorized is not True:
        raise RuntimeError("RESOURCE_PREFLIGHT_REQUIRES_VALIDATED_ONE_USE_AUTHORIZATION")
    seed_audit = validate_seed_separation()
    results = []
    all_records = []
    for spec in _specs():
        cell_started = time.perf_counter()
        profile_calibration_seconds = 0.0
        profile_validation_seconds = 0.0
        comparison_seconds = 0.0
        c5_sensitivity_seconds = 0.0
        typed_abstentions: dict[str, int] = {}
        untyped_failures = 0
        fit_statuses: dict[str, int] = {}
        for replicate in range(K_PER_CELL):
            cell_id = spec.cell_id
            dataset_id = f"{PREFLIGHT_ID}:{SEED_SCHEDULE_ID}:{cell_id}:{replicate:04d}"
            dataset_seed = derive_seed("dataset", cell_id, replicate)
            c0_seed = derive_seed("C0_bootstrap", cell_id, replicate)
            c5_seed = derive_seed("C5_bootstrap_B1000", cell_id, replicate) if spec.family == "F5" else None
            rows = generate_holdout_dataset(spec, replicate, seed_override=dataset_seed)
            row_digest = hashlib.sha256(
                json.dumps(rows, separators=(",", ":"), allow_nan=False).encode()
            ).hexdigest()
            record = {
                "dataset_id": dataset_id,
                "dataset_seed": dataset_seed,
                "rows_sha256": row_digest,
                "C0_bootstrap_seed": c0_seed,
                "C0_bootstrap_B": C0_B,
                "C5_bootstrap_seed_B1000": c5_seed,
                "C5_bootstrap_B1000": C5_B_PRIMARY if spec.family == "F5" else None,
                "F1_profile_status": None,
                "F1_profile_reason": None,
                "F5_fit_status": None,
                "F5_fit_reason": None,
            }
            try:
                if spec.family == "F1":
                    # A2 calibration statistic: profile log-likelihood at the
                    # known truth and at the data-derived constrained MLE.
                    t0 = time.perf_counter()
                    observed = observed_nested_mr_result(rows)
                    tau_hat = max(
                        0.0,
                        observed.observed_world_variance - observed.within_estimate / spec.r,
                    )
                    f1_profile_loglik(rows, between_variance=spec.true_between)
                    f1_profile_loglik(rows, between_variance=tau_hat)
                    profile_calibration_seconds += time.perf_counter() - t0

                t0 = time.perf_counter()
                comparison = compare_dataset(
                    rows, dataset_id=dataset_id, family=spec.family,
                    target_m=spec.m, target_r=spec.r,
                    baseline_bootstrap_replicates=C0_B,
                    baseline_bootstrap_seed=c0_seed,
                    confidence_level=0.95,
                    bootstrap_replicates=C5_B_PRIMARY if spec.family == "F5" else None,
                    bootstrap_seed=c5_seed,
                    include_profile_diagnostics=False,
                    include_f5_concentration_profile_audit=False,
                )
                comparison_seconds += time.perf_counter() - t0
                roster = {comparison.baseline.method_id}
                roster.update(item.method_id for item in comparison.candidates)
                expected = {
                    "C0_FROZEN_V002_NESTED_PERCENTILE_1.2",
                    "C1_F1_EXACT_PIVOTAL_1.0" if spec.family == "F1"
                    else "F5_FITTED_BETA_BINOMIAL_PARAMETRIC_1.0",
                }
                if roster != expected:
                    raise RuntimeError("METHOD_ROSTER_MISMATCH")
                if spec.family == "F1":
                    # Measure the full inversion path. The supplied cutoff is
                    # computational-only; no interval is scored or interpreted.
                    t0 = time.perf_counter()
                    profile = f1_profile_between_confidence_set(
                        rows, family="F1",
                        likelihood_ratio_cutoff=F1_PROFILE_BENCHMARK_CUTOFF,
                    )
                    profile_validation_seconds += time.perf_counter() - t0
                    record["F1_profile_status"] = profile.status
                    record["F1_profile_topology_status"] = profile.topology_status
                    record["F1_profile_nuisance_status"] = profile.nuisance_certification_status
                else:
                    candidate = comparison.candidates[0]
                    diagnostics = dict(candidate.diagnostics)
                    record["F5_fit_status"] = diagnostics.get("fit_status")
                    record["F5_fit_reason"] = diagnostics.get("failure_reason")
                    fit_statuses[record["F5_fit_status"] or "MISSING"] = fit_statuses.get(record["F5_fit_status"] or "MISSING", 0) + 1
                    # B=4,000 is measured on the same fixed preflight rows,
                    # with an independent stream, solely to project B3 cost.
                    t0 = time.perf_counter()
                    from c10s_fitted_beta_binomial_bootstrap import fitted_beta_binomial_parametric_bootstrap
                    sensitivity_seed = derive_seed("C5_bootstrap_B4000", cell_id, replicate)
                    record["C5_bootstrap_seed_B4000"] = sensitivity_seed
                    record["C5_bootstrap_B4000"] = C5_B_SENSITIVITY
                    sensitivity_result = fitted_beta_binomial_parametric_bootstrap(
                        rows, target_m=spec.m, target_r=spec.r,
                        bootstrap_replicates=C5_B_SENSITIVITY,
                        bootstrap_seed=sensitivity_seed,
                        confidence_level=0.95,
                    )
                    record["C5_B4000_fit_status"] = (
                        "ABSTAINED" if sensitivity_result.fit is None
                        else "BOUNDARY" if sensitivity_result.fit.boundary else "INTERIOR"
                    )
                    record["C5_B4000_failure_reason"] = sensitivity_result.failure_reason
                    c5_sensitivity_seconds += time.perf_counter() - t0
            except F1ProfileError as exc:
                record["F1_profile_status"] = "TYPED_ABSTENTION"
                record["F1_profile_reason"] = str(exc)
                typed_abstentions[str(exc)] = typed_abstentions.get(str(exc), 0) + 1
            except Exception as exc:
                untyped_failures += 1
                record["execution_error"] = f"{type(exc).__name__}:{exc}"
            all_records.append(record)
        elapsed = time.perf_counter() - cell_started
        results.append({
            "cell_id": spec.cell_id, "family": spec.family,
            "m": spec.m, "r": spec.r,
            "datasets": K_PER_CELL,
            "C0_bootstrap_B": C0_B,
            "C5_bootstrap_B_primary": C5_B_PRIMARY if spec.family == "F5" else None,
            "C5_bootstrap_B_sensitivity": C5_B_SENSITIVITY if spec.family == "F5" else None,
            "elapsed_seconds": elapsed,
            "seconds_per_dataset": elapsed / K_PER_CELL,
            "F1_profile_calibration_seconds": profile_calibration_seconds if spec.family == "F1" else None,
            "F1_profile_validation_seconds": profile_validation_seconds if spec.family == "F1" else None,
            "comparison_seconds": comparison_seconds,
            "C5_B4000_incremental_seconds": c5_sensitivity_seconds if spec.family == "F5" else None,
            "peak_process_rss_bytes": peak_rss_bytes(),
            "peak_rss_scope": "PROCESS_LIFETIME_HIGH_WATERMARK_CUMULATIVE",
            "typed_abstentions": dict(sorted(typed_abstentions.items())),
            "fit_statuses": dict(sorted(fit_statuses.items())),
            "untyped_execution_failures": untyped_failures,
            "coverage_adjudication": "NOT_RUN",
            "coverage_metrics_emitted": False,
            "results_used_for_calibration": False,
            "results_used_for_validation": False,
        })
    # Extrapolation follows the frozen v1.0 bank sizes. F1 A2 uses only
    # the profile LR statistic; A3 adds C0/C1 comparison and interval inversion.
    # F5 B2 uses C0/C5 at B=1,000; B3 adds B=4,000 on 500 selected datasets.
    by_family = {item["family"]: item for item in results}
    f1 = by_family["F1"]
    f5 = by_family["F5"]
    f1_cal_per_dataset = f1["F1_profile_calibration_seconds"] / K_PER_CELL
    f1_validation_per_dataset = (
        f1["elapsed_seconds"] - f1["F1_profile_calibration_seconds"]
    ) / K_PER_CELL
    f5_base_per_dataset = (
        f5["elapsed_seconds"] - f5["C5_B4000_incremental_seconds"]
    ) / K_PER_CELL
    f5_b4000_per_dataset = f5["C5_B4000_incremental_seconds"] / K_PER_CELL
    projection = {
        "basis": "linear_per_dataset_extrapolation_from_one_representative_M30_R20_cell_per_family",
        "F1_A2_calibration_datasets": 30000,
        "F1_A3_validation_datasets": 30000,
        "F5_B2_calibration_validation_datasets": 20000,
        "F5_B3_selected_datasets": 500,
        "F1_A2_projected_seconds": f1_cal_per_dataset * 30000,
        "F1_A3_projected_seconds": f1_validation_per_dataset * 30000,
        "F5_B2_projected_seconds": f5_base_per_dataset * 20000,
        "F5_B3_B4000_incremental_projected_seconds": f5_b4000_per_dataset * 500,
    }
    projection["total_projected_seconds"] = sum(
        value for key, value in projection.items()
        if key.endswith("_projected_seconds")
    )
    projection["total_projected_hours"] = projection["total_projected_seconds"] / 3600.0
    projection["B4000_projection_basis"] = (
        "directly benchmarked on the same 100 representative F5 preflight datasets"
    )
    root = Path(__file__).resolve().parents[3]
    try:
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=root, text=True).strip()
    except Exception:
        commit = os.environ.get("GITHUB_SHA")
    output.mkdir(parents=True, exist_ok=True)
    payload = {
        "schema": "TGCV-C10S-POST-HOLDOUT-RESOURCE-PREFLIGHT-1",
        "preflight_id": PREFLIGHT_ID,
        "seed_schedule_id": SEED_SCHEDULE_ID,
        "seed_namespace": SEED_NAMESPACE,
        "representative_cells": list(REPRESENTATIVE_CELLS),
        "k_per_cell": K_PER_CELL,
        "bootstrap": {"C0": C0_B, "C5_primary": C5_B_PRIMARY, "C5_sensitivity": C5_B_SENSITIVITY},
        "f1_profile_benchmark_cutoff": {
            "value": F1_PROFILE_BENCHMARK_CUTOFF,
            "status": "NON_CALIBRATED_COMPUTATIONAL_BENCHMARK_ONLY",
            "used_for_coverage_or_calibration": False,
        },
        "environment": {
            "python_version": sys.version,
            "numpy_version": np.__version__,
            "platform": platform.platform(),
            "workflow_run_id": os.environ.get("GITHUB_RUN_ID"),
            "workflow_run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT"),
            "workflow_commit": commit,
            "authorization_commit": os.environ.get("C10S_AUTHORIZATION_COMMIT"),
            "authorization_id": os.environ.get("C10S_AUTHORIZATION_ID"),
            "approved_code_commit": os.environ.get("C10S_APPROVED_CODE_COMMIT") or commit,
            "dependency_lock_sha256": sha256_file(root / LOCK_PATH),
            "source_sha256": {path: sha256_file(root / path) for path in HASH_PATHS},
        },
        "seed_collision_audit": seed_audit,
        "cells": results,
        "resource_projection": projection,
        "records": all_records,
        "total_datasets": len(all_records),
        "coverage_adjudication": "NOT_RUN",
        "coverage_metrics_emitted": False,
        "calibration_or_validation_data_generated": False,
        "scientific_c10_execution": False,
        "interpretation": "Bounded resource-only sample; no coverage scoring, calibration, validation, holdout or causal inference.",
    }
    (output / "post_holdout_resource_preflight.json").write_text(
        json.dumps(payload, sort_keys=True, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    summary = {
        "preflight_id": PREFLIGHT_ID,
        "total_datasets": payload["total_datasets"],
        "cells": results,
        "resource_projection": projection,
        "coverage_adjudication": "NOT_RUN",
        "scientific_c10_execution": False,
    }
    (output / "post_holdout_resource_preflight_summary.json").write_text(
        json.dumps(summary, sort_keys=True, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    return payload

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    if os.environ.get("C10S_POST_HOLDOUT_RESOURCE_PREFLIGHT_AUTHORIZED") != "1":
        raise SystemExit("BLOCKED: validated one-use resource-preflight authorization required")
    result = run_preflight(args.output_dir, execution_authorized=True)
    print(json.dumps({
        "preflight_id": result["preflight_id"],
        "total_datasets": result["total_datasets"],
        "coverage_adjudication": "NOT_RUN",
        "scientific_c10_execution": False,
    }, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
