"""Execute the frozen Tier A or Tier B nested M/R numerical validation.

Execution is fail-closed behind a separate authorization manifest. The CLI is
not a C10-S scientific workflow and never invokes Generator/Analyzer/Evaluator.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import platform
import sys
from statistics import mean
from types import SimpleNamespace
from typing import Any

from c10s_nested_mr_fixtures import (
    FIXTURE_GENERATOR_VERSION,
    SEED_SCHEDULE_VERSION,
    deterministic_guard_specs,
    generate_deterministic_guard,
    generate_fixture,
    tier_a_specs,
    tier_b_specs,
)
from theta_a_nested_mc_precision import analyze_nested_precision

PROTOCOL_ID = "C10S-NESTED-MR-BOOTSTRAP-VALIDATION-001"
PROTOCOL_VERSION = "002"
METHOD_ID = "TGCV_NESTED_MR_BOOTSTRAP"
METHOD_VERSION = "1.2"
AUTH_SCHEMA = "TGCV-C10S-NESTED-MR-EXECUTION-AUTH-001"
AUTH_RELATIVE_PATH = "00_GOVERNANCE/authorizations/C10S_NESTED_MR_NUMERICAL_EXECUTION_AUTHORIZATION.json"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def wilson_interval(successes: int, trials: int, z: float = 1.959963984540054) -> tuple[float, float]:
    if trials <= 0:
        raise ValueError("Wilson interval requires at least one trial")
    p = successes / trials
    denominator = 1.0 + z * z / trials
    center = (p + z * z / (2.0 * trials)) / denominator
    half = z * math.sqrt((p * (1.0 - p) / trials) + z * z / (4.0 * trials * trials)) / denominator
    return center - half, center + half


def coverage_summary(successes: int, trials: int, nominal: float = 0.95) -> dict[str, Any]:
    if trials <= 0:
        return {
            "successes": successes, "trials": trials, "coverage": None,
            "mcse": None, "wilson_95": None, "status": "NOT_EVALUABLE",
        }
    p = successes / trials
    wilson = wilson_interval(successes, trials)
    passed = 0.93 <= p <= 0.97 and wilson[0] <= nominal <= wilson[1]
    return {
        "successes": successes,
        "trials": trials,
        "coverage": p,
        "mcse": math.sqrt(p * (1.0 - p) / trials),
        "wilson_95": [wilson[0], wilson[1]],
        "acceptance_interval": [0.93, 0.97],
        "nominal": nominal,
        "status": "PASS_BOUNDED_NUMERICAL_VALIDATION" if passed else "NOT_VALIDATED",
    }


def _summary_for(dataset):
    world_means = tuple(sum(row) / len(row) for row in dataset.rows)
    grand = sum(world_means) / len(world_means)
    reported = math.sqrt(grand) if dataset.metric == "point_rmse" else grand
    return SimpleNamespace(
        metric=dataset.metric,
        mean=reported,
        mcse=None,
        outer_world_contributions=tuple(zip(dataset.world_ids, world_means)),
    )


def analyze_fixture(dataset, bootstrap_replicates: int | None = None) -> dict[str, Any]:
    spec = dataset.spec
    b = spec.b if bootstrap_replicates is None else bootstrap_replicates
    result = analyze_nested_precision(
        metric=dataset.metric,
        replicate_contributions=dataset.rows,
        summary_metric=_summary_for(dataset),
        outer_world_sampling_mode="DECLARED_IID_PSEUDORANDOM",
        outer_world_sampling_contract_id=f"C10S-FIXTURE-M-{spec.cell_id}",
        outer_world_sampling_contract_version="1.0",
        outer_world_sampling_independence_basis=(
            "Fixture truth: independent outer-world draws from the declared distribution."
        ),
        within_world_sampling_mode="DECLARED_IID_PSEUDORANDOM",
        within_world_sampling_contract_id=f"C10S-FIXTURE-R-{spec.cell_id}",
        within_world_sampling_contract_version="1.0",
        within_world_sampling_independence_basis=(
            "Fixture truth: independent R draws conditional on each selected world state."
        ),
        projections=((spec.m, spec.r),),
        bootstrap_replicates=b,
        bootstrap_seed=dataset.bootstrap_seed,
    )
    intervals = {name: [lower, upper] for name, lower, upper in result.component_intervals}
    projection = result.projections[0]
    return {
        "cell_id": spec.cell_id,
        "family": spec.family,
        "m": spec.m,
        "r": spec.r,
        "dataset_seed": dataset.dataset_seed,
        "bootstrap_seed": dataset.bootstrap_seed,
        "true_within": spec.true_within,
        "true_between": spec.true_between,
        "estimate_within": result.within_ms,
        "estimate_between_raw": result.between_raw,
        "intervals_95": intervals,
        "projected_mcse_interval": [projection[2], projection[3]],
        "projected_mcse_status": projection[4],
        "true_mcse": math.sqrt(
            spec.true_between / spec.m
            + spec.true_within / (spec.m * spec.r)
        ),
        "boundary_fraction": result.boundary_fraction,
        "bootstrap_replicates": result.bootstrap_replicates,
        "valid_bootstrap_replicates": result.valid_bootstrap_replicates,
        "bootstrap_degenerate": result.bootstrap_degenerate,
        "analysis_status": result.status,
    }


def _finite_record(record: dict[str, Any]) -> bool:
    for key in (
        "estimate_within", "estimate_between_raw", "true_within",
        "true_between", "boundary_fraction",
    ):
        value = record.get(key)
        if value is not None and not math.isfinite(float(value)):
            return False
    for interval in record["intervals_95"].values():
        if not all(math.isfinite(float(x)) for x in interval):
            return False
    return True


def _component_cell_summary(records: list[dict[str, Any]], component: str) -> dict[str, Any]:
    estimate_key = "estimate_" + component
    truth_key = "true_" + component
    interval_key = "within_ms" if component == "within" else "between_raw"
    estimates = [float(row[estimate_key]) for row in records]
    truths = [float(row[truth_key]) for row in records]
    errors = [estimate - truth for estimate, truth in zip(estimates, truths)]
    widths = [
        row["intervals_95"][interval_key][1] - row["intervals_95"][interval_key][0]
        for row in records
    ]
    covered = sum(
        row["intervals_95"][interval_key][0] <= row[truth_key]
        <= row["intervals_95"][interval_key][1]
        for row in records
    )
    result = coverage_summary(covered, len(records))
    result.update({
        "bias": mean(errors),
        "rmse": math.sqrt(mean(error * error for error in errors)),
        "median_absolute_error": sorted(abs(error) for error in errors)[len(errors) // 2],
        "mean_interval_width": mean(widths),
        "mean_estimate": mean(estimates),
        "analytical_truth": truths[0],
    })
    return result


def _summarize_tier_a(spec, records: list[dict[str, Any]]) -> dict[str, Any]:
    within = _component_cell_summary(records, "within")
    between = _component_cell_summary(records, "between")
    available = [
        row for row in records
        if row["projected_mcse_status"] == "ESTIMABLE_UNDER_DECLARED_SAMPLING"
        and row["projected_mcse_interval"][0] is not None
        and row["projected_mcse_interval"][1] is not None
    ]
    mcse_covered = sum(
        row["projected_mcse_interval"][0] <= row["true_mcse"]
        <= row["projected_mcse_interval"][1]
        for row in available
    )
    availability = len(available) / len(records)
    mcse = coverage_summary(mcse_covered, len(available))
    mcse["availability"] = availability
    mcse["available_datasets"] = len(available)
    mcse["total_datasets"] = len(records)
    if availability < 0.95:
        mcse["status"] = "CONDITIONAL_NOT_CALIBRATED"
    return {
        "cell": spec.manifest(),
        "datasets_completed": len(records),
        "finite_records": sum(_finite_record(row) for row in records),
        "within_component": within,
        "between_component_raw": between,
        "projected_mcse": mcse,
        "mean_boundary_fraction": mean(row["boundary_fraction"] for row in records),
        "mean_valid_bootstrap_replicates": mean(row["valid_bootstrap_replicates"] for row in records),
        "disposition": (
            "PASS_BOUNDED_NUMERICAL_VALIDATION"
            if within["status"] == "PASS_BOUNDED_NUMERICAL_VALIDATION"
            and between["status"] == "PASS_BOUNDED_NUMERICAL_VALIDATION"
            and mcse["status"] == "PASS_BOUNDED_NUMERICAL_VALIDATION"
            else "NOT_VALIDATED"
        ),
    }


def _summarize_tier_b(spec, records: list[dict[str, Any]]) -> dict[str, Any]:
    status_counts: dict[str, int] = {}
    projection_counts: dict[str, int] = {}
    for row in records:
        status_counts[row["analysis_status"]] = status_counts.get(row["analysis_status"], 0) + 1
        projection_counts[row["projected_mcse_status"]] = projection_counts.get(
            row["projected_mcse_status"], 0
        ) + 1
    support_ok = True
    if spec.m == 2:
        support_ok = all(
            row["projected_mcse_status"] == "INSUFFICIENT_OUTER_SUPPORT"
            and row["projected_mcse_interval"] == [None, None]
            for row in records
        )
    finite_count = sum(_finite_record(row) for row in records)
    valid_count = sum(
        row["valid_bootstrap_replicates"] == spec.b
        and row["bootstrap_replicates"] == spec.b
        for row in records
    )
    return {
        "cell": spec.manifest(),
        "datasets_completed": len(records),
        "finite_records": finite_count,
        "full_bootstrap_records": valid_count,
        "analysis_status_counts": status_counts,
        "projection_status_counts": projection_counts,
        "negative_raw_between_count": sum(row["estimate_between_raw"] < 0 for row in records),
        "mean_boundary_fraction": mean(row["boundary_fraction"] for row in records),
        "support_negative_control_pass": support_ok,
        "disposition": (
            "PASS_DIAGNOSTIC_CONTRACT"
            if finite_count == len(records) and valid_count == len(records) and support_ok
            else "NOT_VALIDATED"
        ),
    }


def _run_deterministic_guards(output_dir: Path, root: Path, code_commit: str) -> list[dict[str, Any]]:
    guards = []
    for spec in deterministic_guard_specs():
        dataset = generate_deterministic_guard(spec)
        b = 100
        record = analyze_fixture(dataset, bootstrap_replicates=b)
        if spec.family == "F6":
            passed = (
                record["bootstrap_degenerate"]
                and record["projected_mcse_status"] == "RMSE_DELTA_NONREGULAR"
                and record["projected_mcse_interval"] == [None, None]
            )
        else:
            passed = (
                record["bootstrap_degenerate"]
                and record["analysis_status"] == "DEGENERATE_BOOTSTRAP_DISTRIBUTION"
                and record["projected_mcse_status"] == "DEGENERATE_BOOTSTRAP_DISTRIBUTION"
                and record["projected_mcse_interval"] == [None, None]
            )
        guards.append({
            "cell": spec.manifest(),
            "analysis": record,
            "direct_invariant_pass": passed,
        })
    if not all(item["direct_invariant_pass"] for item in guards):
        raise RuntimeError("one or more deterministic degeneracy guards failed")
    path = output_dir / "deterministic_guards.json"
    path.write_text(json.dumps(guards, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return guards


def _load_authorization(path: Path, *, tier: str, code_commit: str, protocol_sha256: str) -> dict[str, Any]:
    if not path.is_file():
        raise RuntimeError(f"execution authorization is absent: {path}")
    auth = json.loads(path.read_text(encoding="utf-8"))
    if auth.get("schema") != AUTH_SCHEMA or auth.get("status") != "APPROVED":
        raise RuntimeError("execution authorization schema/status is not APPROVED")
    if auth.get("protocol_id") != PROTOCOL_ID or auth.get("protocol_version") != PROTOCOL_VERSION:
        raise RuntimeError("authorization does not bind frozen protocol version 002")
    if auth.get("method_id") != METHOD_ID or auth.get("method_version") != METHOD_VERSION:
        raise RuntimeError("authorization does not bind nested M/R method version 1.2")
    if auth.get("approved_code_commit") != code_commit:
        raise RuntimeError("authorization code commit does not match checked-out code")
    if auth.get("protocol_sha256") != protocol_sha256:
        raise RuntimeError("authorization protocol hash does not match")
    if auth.get("tier") != tier:
        raise RuntimeError("authorization tier does not match requested tier")
    expected_k, expected_b = (1000, 1000) if tier == "A" else (500, 500)
    if auth.get("k_per_cell") != expected_k or auth.get("b_per_dataset") != expected_b:
        raise RuntimeError("authorization K/B differ from the frozen protocol")
    if auth.get("seed_schedule_version") != SEED_SCHEDULE_VERSION:
        raise RuntimeError("authorization seed schedule version does not match")
    if not isinstance(auth.get("authorization_id"), str) or not auth["authorization_id"].strip():
        raise RuntimeError("authorization_id is required")
    return auth


def run_tier(
    tier: str,
    output_dir: Path,
    *,
    root: Path,
    code_commit: str,
    authorization: dict[str, Any],
) -> dict[str, Any]:
    if tier not in {"A", "B"}:
        raise ValueError("tier must be A or B")
    output_dir.mkdir(parents=True, exist_ok=True)
    protocol_path = root / "00_GOVERNANCE/SIP/C10_S_NESTED_MR_BOOTSTRAP_NUMERICAL_VALIDATION_PROTOCOL_DRAFT_001.md"
    protocol_hash = sha256_file(protocol_path)
    source_paths = [
        protocol_path,
        root / "03_EXPERIMENTS/C10-S/harness/c10s_nested_mr_fixtures.py",
        root / "03_EXPERIMENTS/C10-S/harness/run_c10s_nested_mr_validation.py",
        root / "03_EXPERIMENTS/C10-S/harness/theta_a_nested_mc_precision.py",
        root / "03_EXPERIMENTS/C10-S/harness/requirements-vcont-integrated.lock",
    ]
    source_hashes = {
        str(path.relative_to(root)): {"sha256": sha256_file(path), "bytes": path.stat().st_size}
        for path in source_paths
    }
    specs = tier_a_specs() if tier == "A" else tier_b_specs()
    summaries = []
    records_index = []
    for spec in specs:
        cell_path = output_dir / f"{spec.cell_id}.jsonl"
        summary_path = output_dir / f"{spec.cell_id}.summary.json"
        if cell_path.exists() and summary_path.exists():
            cached = json.loads(summary_path.read_text(encoding="utf-8"))
            if (
                cached.get("code_commit") == code_commit
                and cached.get("protocol_sha256") == protocol_hash
                and cached.get("cell", {}).get("cell_id") == spec.cell_id
                and cached.get("datasets_completed") == spec.k
                and cached.get("cell", {}).get("b") == spec.b
            ):
                summaries.append(cached)
                records_index.append({"cell_id": spec.cell_id, "records": cell_path.name, "reused": True})
                continue
        temp_path = cell_path.with_suffix(".jsonl.tmp")
        if temp_path.exists():
            temp_path.unlink()
        records: list[dict[str, Any]] = []
        with temp_path.open("w", encoding="utf-8") as stream:
            for replicate in range(spec.k):
                dataset = generate_fixture(spec, replicate)
                record = analyze_fixture(dataset)
                record["replicate_index"] = replicate
                record["run_id"] = os.environ.get("GITHUB_RUN_ID", "UNASSIGNED")
                record["code_commit"] = code_commit
                record["protocol_sha256"] = protocol_hash
                stream.write(json.dumps(record, sort_keys=True, allow_nan=False) + "\n")
                records.append(record)
        temp_path.replace(cell_path)
        summary = (
            _summarize_tier_a(spec, records)
            if tier == "A" else _summarize_tier_b(spec, records)
        )
        summary["code_commit"] = code_commit
        summary["protocol_sha256"] = protocol_hash
        summary["authorization_id"] = authorization["authorization_id"]
        summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
        summaries.append(summary)
        records_index.append({"cell_id": spec.cell_id, "records": cell_path.name, "reused": False})

    guards = _run_deterministic_guards(output_dir, root, code_commit) if tier == "B" else []
    manifest = {
        "schema": "TGCV-C10S-NESTED-MR-NUMERICAL-VALIDATION-001",
        "protocol": {"id": PROTOCOL_ID, "version": PROTOCOL_VERSION, "sha256": protocol_hash},
        "method": {"id": METHOD_ID, "version": METHOD_VERSION},
        "authorization": {
            "authorization_id": authorization["authorization_id"],
            "authorization_status": authorization["status"],
            "approved_code_commit": authorization["approved_code_commit"],
        },
        "repository": os.environ.get("GITHUB_REPOSITORY", "jcarmonabastida-pixel/TGCV"),
        "branch": os.environ.get("GITHUB_REF_NAME", "research/c10-s-consolidation-draft"),
        "code_commit": code_commit,
        "run_id": os.environ.get("GITHUB_RUN_ID", "UNASSIGNED"),
        "run_attempt": os.environ.get("GITHUB_RUN_ATTEMPT", "UNASSIGNED"),
        "tier": tier,
        "k_per_cell": 1000 if tier == "A" else 500,
        "b_per_dataset": 1000 if tier == "A" else 500,
        "seed_schedule_version": SEED_SCHEDULE_VERSION,
        "fixture_generator_version": FIXTURE_GENERATOR_VERSION,
        "python": sys.version,
        "platform": platform.platform(),
        "architecture": platform.machine(),
        "source_hashes": source_hashes,
        "cells": summaries,
        "record_files": records_index,
        "deterministic_guards": guards,
        "scope_exclusions": [
            "no C10-S Generator, Analyzer or Evaluator execution",
            "no C10 DGP, calibration bank, seed bank or scientific workflow",
            "no paired A-B or cross-scenario contrasts",
            "no N-coupling comparisons",
            "no causal, Value or confirmatory claim",
        ],
    }
    manifest_path = output_dir / "run_manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    manifest["output_manifest_sha256"] = sha256_file(manifest_path)
    manifest_path.write_text(json.dumps(manifest, indent=2, sort_keys=True, allow_nan=False) + "\n", encoding="utf-8")
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--tier", choices=("A", "B"), required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--code-commit", required=True)
    parser.add_argument("--authorization-file", type=Path, default=Path(AUTH_RELATIVE_PATH))
    args = parser.parse_args()
    protocol_path = args.root / "00_GOVERNANCE/SIP/C10_S_NESTED_MR_BOOTSTRAP_NUMERICAL_VALIDATION_PROTOCOL_DRAFT_001.md"
    authorization = _load_authorization(
        args.authorization_file,
        tier=args.tier,
        code_commit=args.code_commit,
        protocol_sha256=sha256_file(protocol_path),
    )
    run_tier(
        args.tier, args.output, root=args.root,
        code_commit=args.code_commit, authorization=authorization,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
