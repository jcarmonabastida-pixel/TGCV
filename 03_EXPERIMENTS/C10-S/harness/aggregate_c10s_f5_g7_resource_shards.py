"""Verify and aggregate the complete timing-only G7 resource shard roster."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import statistics
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
        ):
            raise ValueError(f"RESOURCE_SHARD_CONTRACT_MISMATCH:{path.name}")
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
    cells = []
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
                "p95": pct(.95),
                "p99": pct(.99),
                "max": max(values),
                "total": sum(values),
            },
        })
    payload = {
        "schema": "C10S-F5-G7-RESOURCE-PREFLIGHT-PARALLEL-PROFILE-002",
        "scope": "RESOURCE_NAMESPACE_ONLY_K100_PER_CELL_TIMING_ONLY_NO_OUTCOME_INSPECTION_NO_COVERAGE_NO_HOLDOUT",
        "seed_namespace": g7.RESOURCE_NAMESPACE,
        "K_per_cell": g7.RESOURCE_K_PER_CELL,
        "C0_B": g7.C0_B,
        "C5_B": g7.C5_B,
        "shards_verified": len(observed),
        "dataset_count": sum(len(values) for values in all_timings.values()),
        "cells": cells,
        "shard_hashes": sorted(shard_hashes, key=lambda x: x["file"]),
        "coverage_adjudication": "NOT_PERFORMED",
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
