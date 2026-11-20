"""Prospective F5 Tier-A G7 calibration; isolated from consumed Tier-A seeds."""
from __future__ import annotations

import hashlib
import json
import resource
import time
from pathlib import Path
from typing import Any

from c10s_nested_mr_fixtures import tier_a_specs
from c10s_nested_mr_comparative_inference_engine import (
    IMPLEMENTED_METHODS,
    adjudicate_matched_datasets,
    compare_dataset,
)
from run_c10s_nested_mr_comparative_holdout import (
    _jsonable,
    _truth,
    deterministic_result_digest,
    derive_holdout_seed,
    generate_holdout_dataset,
)

PROTOCOL_ID = "C10S-F5-G7-TIERA-PROSPECTIVE-001"
PROTOCOL_VERSION = "1.0"
SEED_SCHEDULE_ID = "C10S_F5_G7_TIERA_SEEDS_1.0"
HOLDOUT_NAMESPACE = "c10s_f5_g7_holdout_v1"
RESOURCE_NAMESPACE = "c10s_f5_g7_resource_v1"
EXPECTED_CELLS = ("F5_beta22_M10_R5", "F5_beta22_M30_R20")
K_PER_CELL = 1000
C0_B = 1000
C5_B = 1000
RESOURCE_K_PER_CELL = 100
CONFIDENCE_LEVEL = 0.95


class F5G7Error(RuntimeError):
    pass


def derive_seed(namespace: str, stream: str, cell_id: str, replicate: int) -> int:
    if namespace not in {HOLDOUT_NAMESPACE, RESOURCE_NAMESPACE}:
        raise F5G7Error("UNKNOWN_G7_SEED_NAMESPACE")
    if stream not in {"dataset", "C0_bootstrap", "C5_bootstrap"}:
        raise F5G7Error("UNKNOWN_G7_SEED_STREAM")
    if type(replicate) is not int or replicate < 0:
        raise F5G7Error("INVALID_G7_REPLICATE_INDEX")
    payload = (
        f"{SEED_SCHEDULE_ID}|{namespace}|{stream}|{cell_id}|{replicate}"
    ).encode("utf-8")
    return int.from_bytes(hashlib.sha256(payload).digest()[:8], "big")


def f5_specs():
    by_id = {spec.cell_id: spec for spec in tier_a_specs()}
    if not set(EXPECTED_CELLS).issubset(by_id):
        raise F5G7Error("FROZEN_F5_TIERA_CELL_ROSTER_UNAVAILABLE")
    return tuple(by_id[cell_id] for cell_id in EXPECTED_CELLS)


def validate_seed_separation(k: int = K_PER_CELL) -> None:
    seen: set[int] = set()
    for cell_id in EXPECTED_CELLS:
        for replicate in range(k):
            for stream in ("dataset", "C0_bootstrap", "C5_bootstrap"):
                value = derive_seed(HOLDOUT_NAMESPACE, stream, cell_id, replicate)
                if value in seen:
                    raise F5G7Error("G7_SEED_COLLISION_WITHIN_HOLDOUT_NAMESPACE")
                seen.add(value)
                legacy_stream = stream
                legacy = derive_holdout_seed(legacy_stream, cell_id, replicate)
                if value == legacy:
                    raise F5G7Error("G7_SEED_COLLISION_WITH_CONSUMED_V1_HOLDOUT")
    resource_seen: set[int] = set()
    for cell_id in EXPECTED_CELLS:
        for replicate in range(RESOURCE_K_PER_CELL):
            for stream in ("dataset", "C0_bootstrap", "C5_bootstrap"):
                value = derive_seed(RESOURCE_NAMESPACE, stream, cell_id, replicate)
                if value in resource_seen or value in seen:
                    raise F5G7Error("G7_RESOURCE_SEED_COLLISION")
                resource_seen.add(value)


def run_cell(spec, *, k: int, c0_b: int, c5_b: int,
             seed_namespace: str, adjudicate: bool) -> dict[str, Any]:
    if spec.family != "F5" or spec.cell_id not in EXPECTED_CELLS:
        raise F5G7Error("G7_ACCEPTS_ONLY_FROZEN_F5_BETA22_CELLS")
    if type(k) is not int or k < 1 or type(c0_b) is not int or c0_b < 100:
        raise F5G7Error("INVALID_G7_K_OR_C0_B")
    if type(c5_b) is not int or c5_b < 100:
        raise F5G7Error("INVALID_G7_C5_B")
    comparisons, truths, records = [], [], []
    seed_sets = {name: set() for name in ("dataset", "C0_bootstrap", "C5_bootstrap")}
    for replicate in range(k):
        dataset_id = f"{PROTOCOL_VERSION}:{spec.cell_id}:{replicate:06d}"
        seeds = {
            name: derive_seed(seed_namespace, name, spec.cell_id, replicate)
            for name in seed_sets
        }
        for name, value in seeds.items():
            if value in seed_sets[name]:
                raise F5G7Error(f"DUPLICATE_G7_{name.upper()}_SEED")
            seed_sets[name].add(value)
        rows = generate_holdout_dataset(spec, replicate, seed_override=seeds["dataset"])
        comparison = compare_dataset(
            rows, dataset_id=dataset_id, family="F5",
            target_m=spec.m, target_r=spec.r,
            baseline_bootstrap_replicates=c0_b,
            baseline_bootstrap_seed=seeds["C0_bootstrap"],
            confidence_level=CONFIDENCE_LEVEL,
            bootstrap_replicates=c5_b,
            bootstrap_seed=seeds["C5_bootstrap"],
            include_profile_diagnostics=False,
            require_f5_global_mle_certificate=True,
        )
        roster = {comparison.baseline.method_id}
        roster.update(candidate.method_id for candidate in comparison.candidates)
        if roster != set(IMPLEMENTED_METHODS["F5"]):
            raise F5G7Error("G7_METHOD_ROSTER_MISMATCH")
        if comparison.dataset_id != dataset_id or (comparison.input_m, comparison.input_r) != (spec.m, spec.r):
            raise F5G7Error("G7_DATASET_OR_DESIGN_IDENTITY_MISMATCH")
        truth = _truth(spec, dataset_id)
        comparisons.append(comparison)
        truths.append(truth)
        records.append({
            "dataset_id": dataset_id,
            "dataset_seed": seeds["dataset"],
            "C0_bootstrap_seed": seeds["C0_bootstrap"],
            "C5_bootstrap_seed": seeds["C5_bootstrap"],
            "rows_sha256": hashlib.sha256(
                json.dumps(rows, separators=(",", ":"), allow_nan=False).encode()
            ).hexdigest(),
            "comparison": _jsonable(comparison),
            "truth": _jsonable(truth),
        })
    metrics = []
    if adjudicate:
        metrics = [
            _jsonable(metric)
            for metric in adjudicate_matched_datasets(comparisons, truths)
            if metric.target in {"within", "between"}
        ]
    if len(records) != k or len({item["dataset_id"] for item in records}) != k:
        raise F5G7Error("G7_DATASET_DENOMINATOR_INCOMPLETE")
    return {
        "protocol_id": PROTOCOL_ID,
        "protocol_version": PROTOCOL_VERSION,
        "seed_schedule_id": SEED_SCHEDULE_ID,
        "seed_namespace": seed_namespace,
        "cell": spec.manifest(),
        "datasets_completed": len(records),
        "method_roster": sorted(IMPLEMENTED_METHODS["F5"]),
        "records": records,
        "metrics": metrics,
        "coverage_adjudication": "PERFORMED" if adjudicate else "NOT_PERFORMED_RESOURCE_ONLY",
    }


def run_resource_preflight() -> dict[str, Any]:
    validate_seed_separation()
    start = time.perf_counter()
    peak_before = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    cells = []
    for spec in f5_specs():
        result = run_cell(
            spec, k=RESOURCE_K_PER_CELL, c0_b=C0_B, c5_b=C5_B,
            seed_namespace=RESOURCE_NAMESPACE, adjudicate=False,
        )
        statuses = {}
        for record in result["records"]:
            candidate = record["comparison"]["candidates"][0]["comparison"]
            status = dict(candidate.get("provenance", [])).get(
                "global_mle_certificate_status", "MISSING"
            )
            statuses[status] = statuses.get(status, 0) + 1
        cells.append({
            "cell_id": spec.cell_id,
            "datasets": result["datasets_completed"],
            "global_mle_certificate_status_counts": statuses,
        })
        del result
    elapsed = time.perf_counter() - start
    peak_after = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    projected = elapsed * (2 * K_PER_CELL * len(EXPECTED_CELLS)) / (
        RESOURCE_K_PER_CELL * len(EXPECTED_CELLS)
    )
    if projected > 16200:
        raise F5G7Error("G7_RESOURCE_PREFLIGHT_PROJECTS_OVER_4_5_HOURS")
    return {
        "status": "RESOURCE_PREFLIGHT_PASS",
        "datasets": RESOURCE_K_PER_CELL * len(EXPECTED_CELLS),
        "elapsed_seconds": elapsed,
        "projected_primary_plus_replay_seconds": projected,
        "peak_rss_kib": max(peak_before, peak_after),
        "cells": cells,
        "coverage_adjudication": "NOT_PERFORMED",
    }


def run_bank(*, seed_namespace: str) -> dict[str, Any]:
    validate_seed_separation()
    return {
        "protocol_id": PROTOCOL_ID,
        "protocol_version": PROTOCOL_VERSION,
        "seed_schedule_id": SEED_SCHEDULE_ID,
        "seed_namespace": seed_namespace,
        "cells": {
            spec.cell_id: run_cell(
                spec, k=K_PER_CELL, c0_b=C0_B, c5_b=C5_B,
                seed_namespace=seed_namespace, adjudicate=True,
            )
            for spec in f5_specs()
        },
    }


def execute_g7(output_dir: Path, *, code_commit: str) -> dict[str, Any]:
    if not isinstance(code_commit, str) or len(code_commit) != 40:
        raise F5G7Error("FULL_CODE_COMMIT_REQUIRED")
    output_dir.mkdir(parents=True, exist_ok=True)
    preflight = run_resource_preflight()
    (output_dir / "resource_preflight.json").write_text(
        json.dumps(preflight, sort_keys=True, indent=2) + "\n", encoding="utf-8"
    )
    primary = run_bank(seed_namespace=HOLDOUT_NAMESPACE)
    primary_digest = deterministic_result_digest(primary)
    primary_dir = output_dir / "primary"
    primary_dir.mkdir(exist_ok=True)
    for cell_id, value in primary["cells"].items():
        (primary_dir / f"{cell_id}.json").write_text(
            json.dumps(_jsonable(value), sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n",
            encoding="utf-8",
        )
    primary_summary = {
        cell_id: {"datasets_completed": value["datasets_completed"], "metrics": value["metrics"]}
        for cell_id, value in primary["cells"].items()
    }
    del primary
    replay = run_bank(seed_namespace=HOLDOUT_NAMESPACE)
    replay_digest = deterministic_result_digest(replay)
    if primary_digest != replay_digest:
        raise F5G7Error("G7_PRIMARY_REPLAY_DIGEST_MISMATCH")
    replay_dir = output_dir / "replay"
    replay_dir.mkdir(exist_ok=True)
    for cell_id, value in replay["cells"].items():
        (replay_dir / f"{cell_id}.json").write_text(
            json.dumps(_jsonable(value), sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n",
            encoding="utf-8",
        )
    replay_summary = {
        cell_id: {"datasets_completed": value["datasets_completed"], "metrics": value["metrics"]}
        for cell_id, value in replay["cells"].items()
    }
    final = {
        "schema": "TGCV-C10S-F5-G7-RESULT-001",
        "protocol_id": PROTOCOL_ID,
        "protocol_version": PROTOCOL_VERSION,
        "code_commit": code_commit,
        "status": "EXECUTED_PRIMARY_REPLAY_EXACT_MATCH",
        "primary_replay_digest": primary_digest,
        "resource_preflight": preflight,
        "primary": primary_summary,
        "replay": replay_summary,
    }
    result_bytes = json.dumps(final, sort_keys=True, indent=2, allow_nan=False) + "\n"
    result_path = output_dir / "g7_result.json"
    result_path.write_text(result_bytes, encoding="utf-8")
    digest = hashlib.sha256(result_bytes.encode("utf-8")).hexdigest()
    manifest = {
        "schema": "TGCV-C10S-F5-G7-MANIFEST-001",
        "protocol_id": PROTOCOL_ID,
        "protocol_version": PROTOCOL_VERSION,
        "code_commit": code_commit,
        "status": final["status"],
        "primary_replay_digest": primary_digest,
        "result_sha256": digest,
        "resource_preflight": preflight,
    }
    manifest_bytes = json.dumps(manifest, sort_keys=True, indent=2) + "\n"
    (output_dir / "run_manifest.json").write_text(manifest_bytes, encoding="utf-8")
    return {
        "status": final["status"],
        "primary_replay_digest": primary_digest,
        "result_sha256": digest,
        "cells": primary_summary,
        "resource_preflight": preflight,
    }
