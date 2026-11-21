"""Integrity-first aggregation of G7 primary/replay shards and full-bank adjudication."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any

import run_c10s_f5_g7_tiera_calibration as g7
from c10s_nested_mr_fixtures import tier_a_specs
from c10s_f5_g7_shard_execution import adjudicate_serialized_records, records_digest

PROFILE_SCHEMA = "C10S-F5-G7-RESOURCE-PREFLIGHT-PARALLEL-PROFILE-001"
PROFILE_SCOPE = "RESOURCE_NAMESPACE_ONLY_K100_PER_CELL_NO_COVERAGE_NO_HOLDOUT"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load_profile(path: Path, expected_sha256: str | None) -> dict[str, Any]:
    if not path.is_file():
        raise ValueError("G7_RESOURCE_PREFLIGHT_ARTIFACT_MISSING")
    actual = sha256_file(path)
    if expected_sha256 and actual != expected_sha256:
        raise ValueError("G7_RESOURCE_PREFLIGHT_ARTIFACT_SHA256_MISMATCH")
    profile = json.loads(path.read_text(encoding="utf-8"))
    if (
        profile.get("schema") != PROFILE_SCHEMA
        or profile.get("scope") != PROFILE_SCOPE
        or profile.get("seed_namespace") != g7.RESOURCE_NAMESPACE
        or profile.get("K_per_cell") != g7.RESOURCE_K_PER_CELL
        or profile.get("C0_B") != g7.C0_B
        or profile.get("C5_B") != g7.C5_B
        or profile.get("coverage_adjudication") != "NOT_PERFORMED"
    ):
        raise ValueError("G7_RESOURCE_PREFLIGHT_PROTOCOL_MISMATCH")
    cells = {cell.get("cell_id"): cell for cell in profile.get("cells", [])}
    if set(cells) != set(g7.EXPECTED_CELLS):
        raise ValueError("G7_RESOURCE_PREFLIGHT_CELL_ROSTER_MISMATCH")
    if any(cells[cell]["datasets_completed"] != g7.RESOURCE_K_PER_CELL for cell in g7.EXPECTED_CELLS):
        raise ValueError("G7_RESOURCE_PREFLIGHT_DENOMINATOR_INCOMPLETE")
    return {"profile": profile, "sha256": actual}


def _load_phase(directory: Path, phase: str, source_commit: str) -> dict[str, dict[tuple[int, int], dict]]:
    if not directory.is_dir():
        raise ValueError(f"G7_{phase.upper()}_SHARD_DIRECTORY_MISSING")
    output: dict[str, dict[tuple[int, int], dict]] = {
        cell: {} for cell in g7.EXPECTED_CELLS
    }
    files = sorted(directory.glob("*.json"))
    all_seed_values = set()
    if not files:
        raise ValueError(f"G7_{phase.upper()}_SHARDS_MISSING")
    for path in files:
        shard = json.loads(path.read_text(encoding="utf-8"))
        if (
            shard.get("schema") != "TGCV-C10S-F5-G7-SHARD-001"
            or shard.get("phase") != phase
            or shard.get("protocol_id") != g7.PROTOCOL_ID
            or shard.get("protocol_version") != g7.PROTOCOL_VERSION
            or shard.get("seed_schedule_id") != g7.SEED_SCHEDULE_ID
            or shard.get("seed_namespace") != g7.HOLDOUT_NAMESPACE
            or shard.get("source_commit") != source_commit
            or shard.get("coverage_adjudication") != "NOT_PERFORMED_SHARD_LEVEL"
        ):
            raise ValueError(f"G7_{phase.upper()}_SHARD_METADATA_MISMATCH:{path.name}")
        cell_id = shard.get("cell_id")
        if cell_id not in output:
            raise ValueError(f"G7_{phase.upper()}_SHARD_UNKNOWN_CELL:{path.name}")
        start = shard.get("replicate_start")
        count = shard.get("replicate_count")
        if type(start) is not int or type(count) is not int or start < 0 or count < 1 or start + count > g7.K_PER_CELL:
            raise ValueError(f"G7_{phase.upper()}_SHARD_RANGE_INVALID:{path.name}")
        key = (start, count)
        if key in output[cell_id]:
            raise ValueError(f"G7_{phase.upper()}_DUPLICATE_SHARD_RANGE:{cell_id}:{key}")
        records = shard.get("records")
        if not isinstance(records, list) or len(records) != count or shard.get("datasets_completed") != count:
            raise ValueError(f"G7_{phase.upper()}_SHARD_DENOMINATOR_INVALID:{path.name}")
        if shard.get("records_digest") != records_digest(records):
            raise ValueError(f"G7_{phase.upper()}_SHARD_RECORD_DIGEST_MISMATCH:{path.name}")
        spec = next(item for item in g7.f5_specs() if item.cell_id == cell_id)
        expected_cell_manifest = json.loads(json.dumps(spec.manifest(), sort_keys=True))
        if shard.get("cell") != expected_cell_manifest:
            raise ValueError(f"G7_{phase.upper()}_SHARD_CELL_MANIFEST_MISMATCH:{path.name}")
        if shard.get("method_roster") != sorted(g7.IMPLEMENTED_METHODS["F5"]):
            raise ValueError(f"G7_{phase.upper()}_SHARD_METHOD_ROSTER_MISMATCH:{path.name}")
        for offset, record in enumerate(records):
            replicate = start + offset
            expected_id = (
                f"{g7.PROTOCOL_VERSION}:{g7.HOLDOUT_NAMESPACE}:"
                f"{cell_id}:{replicate:06d}"
            )
            if record.get("dataset_id") != expected_id:
                raise ValueError(f"G7_{phase.upper()}_SHARD_DATASET_ID_MISMATCH:{expected_id}")
            expected_seeds = {
                "dataset_seed": g7.derive_seed(g7.HOLDOUT_NAMESPACE, "dataset", cell_id, replicate),
                "C0_bootstrap_seed": g7.derive_seed(g7.HOLDOUT_NAMESPACE, "C0_bootstrap", cell_id, replicate),
                "C5_bootstrap_seed": g7.derive_seed(g7.HOLDOUT_NAMESPACE, "C5_bootstrap", cell_id, replicate),
            }
            for seed_field, expected_seed in expected_seeds.items():
                actual_seed = record.get(seed_field)
                if actual_seed != expected_seed:
                    raise ValueError(f"G7_{phase.upper()}_{seed_field.upper()}_MISMATCH:{expected_id}")
                if actual_seed in all_seed_values:
                    raise ValueError(f"G7_{phase.upper()}_CROSS_STREAM_OR_DATASET_SEED_COLLISION:{expected_id}")
                all_seed_values.add(actual_seed)
            row_digest = record.get("rows_sha256")
            if not isinstance(row_digest, str) or not re.fullmatch(r"[0-9a-f]{64}", row_digest):
                raise ValueError(f"G7_{phase.upper()}_ROW_DIGEST_INVALID:{expected_id}")
            comparison = record.get("comparison", {})
            truth = record.get("truth", {})
            roster = {comparison.get("baseline", {}).get("method_id")}
            roster.update(item.get("method_id") for item in comparison.get("candidates", []))
            expected_truth = g7._jsonable(g7._truth(spec, expected_id))
            if (
                comparison.get("dataset_id") != expected_id
                or comparison.get("family") != "F5"
                or (comparison.get("input_m"), comparison.get("input_r")) != (spec.m, spec.r)
                or (comparison.get("target_m"), comparison.get("target_r")) != (spec.m, spec.r)
                or roster != set(g7.IMPLEMENTED_METHODS["F5"])
                or truth != expected_truth
            ):
                raise ValueError(f"G7_{phase.upper()}_COMPARISON_TRUTH_PAIRING_MISMATCH:{expected_id}")
        output[cell_id][key] = {
            "shard": shard,
            "path": path,
            "file_sha256": sha256_file(path),
        }

    for cell_id, shards in output.items():
        ranges = sorted(shards)
        cursor = 0
        for start, count in ranges:
            if start != cursor:
                raise ValueError(f"G7_{phase.upper()}_SHARD_GAP_OR_OVERLAP:{cell_id}:expected_{cursor}_got_{start}")
            cursor += count
        if cursor != g7.K_PER_CELL:
            raise ValueError(f"G7_{phase.upper()}_CELL_DENOMINATOR_INCOMPLETE:{cell_id}:{cursor}")
    return output


def aggregate(
    *,
    primary_dir: Path,
    replay_dir: Path,
    preflight_path: Path,
    output_dir: Path,
    source_commit: str,
    authorization_id: str,
    expected_preflight_sha256: str | None = None,
) -> dict[str, Any]:
    if not re.fullmatch(r"[0-9a-f]{40}", source_commit):
        raise ValueError("G7_AGGREGATOR_SOURCE_COMMIT_INVALID")
    preflight = _load_profile(preflight_path, expected_preflight_sha256)
    primary_shards = _load_phase(primary_dir, "primary", source_commit)
    replay_shards = _load_phase(replay_dir, "replay", source_commit)

    shard_manifest = []
    primary_cells = {}
    replay_cells = {}
    for cell_id in g7.EXPECTED_CELLS:
        primary_records = []
        replay_records = []
        if set(primary_shards[cell_id]) != set(replay_shards[cell_id]):
            raise ValueError(f"G7_PRIMARY_REPLAY_SHARD_ROSTER_MISMATCH:{cell_id}")
        for key in sorted(primary_shards[cell_id]):
            p = primary_shards[cell_id][key]
            r = replay_shards[cell_id][key]
            ps = p["shard"]
            rs = r["shard"]
            if ps["records_digest"] != rs["records_digest"]:
                raise ValueError(f"G7_PRIMARY_REPLAY_SHARD_DIGEST_MISMATCH:{cell_id}:{key}")
            primary_records.extend(ps["records"])
            replay_records.extend(rs["records"])
            shard_manifest.extend([
                {
                    "phase": "primary", "cell_id": cell_id,
                    "replicate_start": key[0], "replicate_count": key[1],
                    "records_digest": ps["records_digest"],
                    "artifact_file_sha256": p["file_sha256"],
                },
                {
                    "phase": "replay", "cell_id": cell_id,
                    "replicate_start": key[0], "replicate_count": key[1],
                    "records_digest": rs["records_digest"],
                    "artifact_file_sha256": r["file_sha256"],
                },
            ])
        primary_records.sort(key=lambda item: item["dataset_id"])
        replay_records.sort(key=lambda item: item["dataset_id"])
        if primary_records != replay_records:
            raise ValueError(f"G7_PRIMARY_REPLAY_RECORDS_DIFFER:{cell_id}")
        metrics = adjudicate_serialized_records(primary_records)
        spec = next(item for item in g7.f5_specs() if item.cell_id == cell_id)
        common = {
            "protocol_id": g7.PROTOCOL_ID,
            "protocol_version": g7.PROTOCOL_VERSION,
            "seed_schedule_id": g7.SEED_SCHEDULE_ID,
            "seed_namespace": g7.HOLDOUT_NAMESPACE,
            "cell": spec.manifest(),
            "datasets_completed": len(primary_records),
            "method_roster": sorted(g7.IMPLEMENTED_METHODS["F5"]),
            "records": primary_records,
            "metrics": metrics,
            "coverage_adjudication": "PERFORMED",
        }
        if common["datasets_completed"] != g7.K_PER_CELL:
            raise ValueError(f"G7_FULL_CELL_DENOMINATOR_INVALID:{cell_id}")
        primary_cells[cell_id] = dict(common)
        replay_cells[cell_id] = dict(common)

    primary_bank = {
        "protocol_id": g7.PROTOCOL_ID,
        "protocol_version": g7.PROTOCOL_VERSION,
        "seed_schedule_id": g7.SEED_SCHEDULE_ID,
        "seed_namespace": g7.HOLDOUT_NAMESPACE,
        "cells": primary_cells,
    }
    replay_bank = {
        "protocol_id": g7.PROTOCOL_ID,
        "protocol_version": g7.PROTOCOL_VERSION,
        "seed_schedule_id": g7.SEED_SCHEDULE_ID,
        "seed_namespace": g7.HOLDOUT_NAMESPACE,
        "cells": replay_cells,
    }
    primary_digest = g7.deterministic_result_digest(primary_bank)
    replay_digest = g7.deterministic_result_digest(replay_bank)
    if primary_digest != replay_digest:
        raise ValueError("G7_PRIMARY_REPLAY_FULL_BANK_DIGEST_MISMATCH")

    primary_summary = {
        cell_id: {"datasets_completed": value["datasets_completed"], "metrics": value["metrics"]}
        for cell_id, value in primary_cells.items()
    }
    replay_summary = {
        cell_id: {"datasets_completed": value["datasets_completed"], "metrics": value["metrics"]}
        for cell_id, value in replay_cells.items()
    }
    adjudication = g7.adjudicate_g7_metrics(primary_summary)
    status = (
        "G7_PASS_PRIMARY_REPLAY_EXACT_MATCH"
        if adjudication["status"] == "PASS"
        else "G7_NOT_VALIDATED_PRIMARY_REPLAY_EXACT_MATCH"
    )

    output_dir.mkdir(parents=True, exist_ok=True)
    for phase, cells in (("primary", primary_cells), ("replay", replay_cells)):
        phase_dir = output_dir / phase
        phase_dir.mkdir(exist_ok=True)
        for cell_id, value in cells.items():
            (phase_dir / f"{cell_id}.json").write_text(
                json.dumps(value, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n",
                encoding="utf-8",
            )

    final = {
        "schema": "TGCV-C10S-F5-G7-RESULT-002",
        "protocol_id": g7.PROTOCOL_ID,
        "protocol_version": g7.PROTOCOL_VERSION,
        "authorization_id": authorization_id,
        "code_commit": source_commit,
        "status": status,
        "g7_adjudication": adjudication,
        "primary_replay_digest": primary_digest,
        "resource_preflight": preflight["profile"],
        "resource_preflight_sha256": preflight["sha256"],
        "primary": primary_summary,
        "replay": replay_summary,
    }
    result_bytes = json.dumps(final, sort_keys=True, indent=2, allow_nan=False) + "\n"
    result_path = output_dir / "g7_result.json"
    result_path.write_text(result_bytes, encoding="utf-8")
    result_sha256 = hashlib.sha256(result_bytes.encode("utf-8")).hexdigest()
    manifest = {
        "schema": "TGCV-C10S-F5-G7-MANIFEST-002",
        "protocol_id": g7.PROTOCOL_ID,
        "protocol_version": g7.PROTOCOL_VERSION,
        "authorization_id": authorization_id,
        "code_commit": source_commit,
        "status": status,
        "primary_replay_digest": primary_digest,
        "result_sha256": result_sha256,
        "resource_preflight_sha256": preflight["sha256"],
        "shards": shard_manifest,
    }
    (output_dir / "run_manifest.json").write_text(
        json.dumps(manifest, sort_keys=True, indent=2, allow_nan=False) + "\n",
        encoding="utf-8",
    )
    return {
        "status": status,
        "primary_replay_digest": primary_digest,
        "result_sha256": result_sha256,
        "g7_adjudication": adjudication,
        "resource_preflight_sha256": preflight["sha256"],
        "shards": len(shard_manifest),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--primary-dir", type=Path, required=True)
    parser.add_argument("--replay-dir", type=Path, required=True)
    parser.add_argument("--preflight", type=Path, required=True)
    parser.add_argument("--expected-preflight-sha256")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--source-commit", required=True)
    parser.add_argument("--authorization-id", required=True)
    args = parser.parse_args()
    result = aggregate(
        primary_dir=args.primary_dir,
        replay_dir=args.replay_dir,
        preflight_path=args.preflight,
        output_dir=args.output_dir,
        source_commit=args.source_commit,
        authorization_id=args.authorization_id,
        expected_preflight_sha256=args.expected_preflight_sha256,
    )
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
