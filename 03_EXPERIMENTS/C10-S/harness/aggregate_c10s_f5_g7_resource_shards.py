"""Verify and aggregate the complete timing-only G7 resource shard roster."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import statistics
from datetime import datetime
from pathlib import Path

import run_c10s_f5_g7_tiera_calibration as g7


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def aggregate(shard_dir: Path, output: Path) -> dict:
    files = sorted(shard_dir.glob("*.json"))
    expected = {
        (cell, start, 10)
        for cell in g7.EXPECTED_CELLS
        for start in range(0, g7.RESOURCE_K_PER_CELL, 10)
    }
    observed = set()
    all_timings = {cell: [] for cell in g7.EXPECTED_CELLS}
    shard_hashes = []
    source_commits = set()
    shard_starts = []
    shard_completions = []
    cpu_seconds = []
    peak_rss_values = []
    for path in files:
        raw = path.read_bytes()
        item = json.loads(raw)
        digest = item.pop("payload_sha256", None)
        canonical = json.dumps(item, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
        if digest != sha256(canonical):
            raise ValueError(f"RESOURCE_SHARD_DIGEST_MISMATCH:{path.name}")
        key = (item.get("cell_id"), item.get("replicate_start"), item.get("replicate_count"))
        if key not in expected or key in observed:
            raise ValueError(f"UNEXPECTED_OR_DUPLICATE_RESOURCE_SHARD:{key}")
        if (
            item.get("schema") != "C10S-F5-G7-RESOURCE-SHARD-001"
            or item.get("protocol_version") != g7.PROTOCOL_VERSION
            or item.get("seed_schedule_id") != g7.SEED_SCHEDULE_ID
            or item.get("seed_namespace") != g7.RESOURCE_NAMESPACE
            or item.get("datasets_completed") != item.get("replicate_count")
            or item.get("coverage_adjudication") != "NOT_PERFORMED"
            or item.get("retained_scope") != "TIMING_AND_REPLICA_IDENTITY_ONLY"
        ):
            raise ValueError(f"RESOURCE_SHARD_CONTRACT_MISMATCH:{path.name}")
        source_commits.add(item.get("source_commit"))
        shard_starts.append(datetime.fromisoformat(item["shard_started_at_utc"]))
        shard_completions.append(datetime.fromisoformat(item["shard_completed_at_utc"]))
        cpu = item.get("process_cpu_seconds")
        rss = item.get("peak_rss_kib")
        if not isinstance(cpu, (int, float)) or cpu <= 0 or not isinstance(rss, int) or rss <= 0:
            raise ValueError(f"RESOURCE_SHARD_TELEMETRY_INVALID:{path.name}")
        cpu_seconds.append(cpu)
        peak_rss_values.append(rss)
        timings = item.get("dataset_timings", [])
        if len(timings) != item["replicate_count"]:
            raise ValueError(f"RESOURCE_SHARD_TIMING_DENOMINATOR_MISMATCH:{path.name}")
        expected_ids = [
            f"{g7.PROTOCOL_VERSION}:{g7.RESOURCE_NAMESPACE}:{key[0]}:{i:06d}"
            for i in range(key[1], key[1] + key[2])
        ]
        if [row.get("dataset_id") for row in timings] != expected_ids:
            raise ValueError(f"RESOURCE_SHARD_REPLICA_IDENTITY_MISMATCH:{path.name}")
        for row in timings:
            value = row.get("wall_seconds")
            if not isinstance(value, (int, float)) or value <= 0:
                raise ValueError(f"INVALID_RESOURCE_TIMING:{path.name}")
            all_timings[key[0]].append(value)
        observed.add(key)
        shard_hashes.append({"file": path.name, "sha256": sha256(raw)})

    if observed != expected:
        missing = sorted(expected - observed)
        raise ValueError(f"RESOURCE_SHARD_ROSTER_INCOMPLETE:{missing}")
    if len(source_commits) != 1 or not next(iter(source_commits)) or len(shard_starts) != len(expected):
        raise ValueError("RESOURCE_SHARD_SOURCE_COMMIT_MISMATCH")
    source_commit = next(iter(source_commits))
    if len(source_commit) != 40 or any(ch not in "0123456789abcdef" for ch in source_commit):
        raise ValueError("RESOURCE_SHARD_SOURCE_COMMIT_INVALID")
    wall_elapsed = (max(shard_completions) - min(shard_starts)).total_seconds()
    if wall_elapsed <= 0:
        raise ValueError("RESOURCE_PROFILE_WALL_TIME_INVALID")
    cells = []
    dataset_timings = {}
    for cell, values in all_timings.items():
        if len(values) != g7.RESOURCE_K_PER_CELL:
            raise ValueError(f"RESOURCE_CELL_DENOMINATOR_MISMATCH:{cell}")
        ordered = sorted(values)
        def pct(p):
            return ordered[max(0, min(len(ordered)-1, math.ceil(p*len(ordered))-1))]
        cells.append({
            "cell_id": cell,
            "datasets_completed": len(values),
            "latency_seconds": {
                "mean": statistics.fmean(values),
                "median": statistics.median(values),
                "p90": pct(.90),
                "p95": pct(.95),
                "p99": pct(.99),
                "max": max(values),
                "total": sum(values),
            },
        })
        dataset_timings[cell] = [
            row for shard_path in files
            for row in json.loads(shard_path.read_text(encoding="utf-8")).get("dataset_timings", [])
            if row.get("dataset_id", "").split(":")[-2] == cell
        ]
    p95_max = max(
        sorted(all_timings[cell])[max(0, math.ceil(0.95 * len(all_timings[cell])) - 1)]
        for cell in g7.EXPECTED_CELLS
    )
    p99_max = max(
        sorted(all_timings[cell])[max(0, math.ceil(0.99 * len(all_timings[cell])) - 1)]
        for cell in g7.EXPECTED_CELLS
    )
    projections = []
    for shard_size in (25, 40, 50, 100):
        shards_per_cell = math.ceil(g7.K_PER_CELL / shard_size)
        jobs_per_phase = len(g7.EXPECTED_CELLS) * shards_per_cell
        waves = math.ceil(jobs_per_phase / 20)
        p95_job = shard_size * p95_max
        p99_job = shard_size * p99_max
        projections.append({
            "datasets_per_shard": shard_size,
            "shards_per_cell": shards_per_cell,
            "jobs_per_phase": jobs_per_phase,
            "max_parallel_jobs": 20,
            "conservative_waves_per_phase": waves,
            "p95_shard_runtime_seconds": p95_job,
            "p99_shard_runtime_seconds": p99_job,
            "primary_plus_replay_p95_wall_seconds": 2 * waves * p95_job,
            "primary_plus_replay_p99_wall_seconds": 2 * waves * p99_job,
            "single_shard_under_150_minutes_at_p99": p99_job <= 9000,
        })
    payload = {
        "schema": "C10S-F5-G7-RESOURCE-PREFLIGHT-PARALLEL-PROFILE-002",
        "scope": "RESOURCE_NAMESPACE_ONLY_K100_PER_CELL_TIMING_ONLY_NO_OUTCOME_INSPECTION_NO_COVERAGE_NO_HOLDOUT",
        "seed_namespace": g7.RESOURCE_NAMESPACE,
        "source_commit": source_commit,
        "wall_elapsed_seconds": wall_elapsed,
        "process_cpu_seconds": sum(cpu_seconds),
        "peak_rss_kib": max(peak_rss_values),
        "K_per_cell": g7.RESOURCE_K_PER_CELL,
        "C0_B": g7.C0_B,
        "C5_B": g7.C5_B,
        "shards_verified": len(observed),
        "dataset_count": sum(len(values) for values in all_timings.values()),
        "cells": cells,
        "dataset_timings": dataset_timings,
        "shard_hashes": sorted(shard_hashes, key=lambda x: x["file"]),
        "conservative_shard_projections": projections,
        "seed_separation_validation": "PASS",
        "coverage_adjudication": "NOT_PERFORMED",
        "interpretation": "Resource-only timing and shard scheduling evidence. No certificate status, interval emission, coverage outcome or method-selection result is inspected or retained. No holdout or calibration claim.",
    }
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, sort_keys=True, indent=2, allow_nan=False)+"\n", encoding="utf-8")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--shard-dir", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    result = aggregate(args.shard_dir, args.output)
    print(json.dumps({"shards_verified": result["shards_verified"], "dataset_count": result["dataset_count"]}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
