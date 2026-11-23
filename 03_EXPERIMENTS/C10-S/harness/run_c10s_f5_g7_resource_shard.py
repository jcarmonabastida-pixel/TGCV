"""Execute one deterministic, timing-only G7 resource shard."""
from __future__ import annotations

import argparse
import hashlib
import json
import time
from pathlib import Path

import run_c10s_f5_g7_tiera_calibration as g7


def execute(cell_id: str, replicate_start: int, replicate_count: int, output: Path) -> dict:
    if cell_id not in g7.EXPECTED_CELLS:
        raise ValueError("UNKNOWN_RESOURCE_PROFILE_CELL")
    if type(replicate_start) is not int or type(replicate_count) is not int:
        raise ValueError("INVALID_REPLICATE_RANGE")
    if replicate_start < 0 or replicate_count < 1 or replicate_start + replicate_count > g7.RESOURCE_K_PER_CELL:
        raise ValueError("RESOURCE_REPLICATE_RANGE_OUT_OF_BOUNDS")

    spec = next(item for item in g7.f5_specs() if item.cell_id == cell_id)
    observations = []
    original = g7.compare_dataset

    def timed_compare(*args, **kwargs):
        started = time.perf_counter()
        result = original(*args, **kwargs)
        elapsed = time.perf_counter() - started
        dataset_id = kwargs.get("dataset_id")
        if dataset_id is None and len(args) > 1:
            dataset_id = args[1]
        observations.append({"dataset_id": dataset_id, "wall_seconds": elapsed})
        return result

    g7.compare_dataset = timed_compare
    started = time.perf_counter()
    try:
        result = g7.run_cell(
            spec, k=replicate_count, c0_b=g7.C0_B, c5_b=g7.C5_B,
            seed_namespace=g7.RESOURCE_NAMESPACE, adjudicate=False,
            replicate_start=replicate_start,
        )
    finally:
        g7.compare_dataset = original
    elapsed = time.perf_counter() - started

    expected_ids = [
        f"{g7.PROTOCOL_VERSION}:{g7.RESOURCE_NAMESPACE}:{cell_id}:{i:06d}"
        for i in range(replicate_start, replicate_start + replicate_count)
    ]
    observed_ids = [item["dataset_id"] for item in observations]
    if result["datasets_completed"] != replicate_count or observed_ids != expected_ids:
        raise ValueError("RESOURCE_SHARD_DENOMINATOR_OR_IDENTITY_MISMATCH")
    if any(not isinstance(item["wall_seconds"], (int, float)) or item["wall_seconds"] <= 0 for item in observations):
        raise ValueError("INVALID_RESOURCE_SHARD_TIMING")

    payload = {
        "schema": "C10S-F5-G7-RESOURCE-SHARD-001",
        "protocol_version": g7.PROTOCOL_VERSION,
        "seed_schedule_id": g7.SEED_SCHEDULE_ID,
        "seed_namespace": g7.RESOURCE_NAMESPACE,
        "cell_id": cell_id,
        "replicate_start": replicate_start,
        "replicate_count": replicate_count,
        "datasets_completed": result["datasets_completed"],
        "wall_elapsed_seconds": elapsed,
        "dataset_timings": observations,
        "coverage_adjudication": "NOT_PERFORMED",
        "retained_scope": "TIMING_AND_REPLICA_IDENTITY_ONLY",
    }
    encoded = json.dumps(payload, sort_keys=True, separators=(",", ":"), allow_nan=False).encode()
    payload["payload_sha256"] = hashlib.sha256(encoded).hexdigest()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(payload, sort_keys=True, indent=2, allow_nan=False) + "\n", encoding="utf-8")
    return payload


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--cell-id", required=True)
    parser.add_argument("--replicate-start", required=True, type=int)
    parser.add_argument("--replicate-count", required=True, type=int)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()
    g7.validate_seed_separation()
    payload = execute(args.cell_id, args.replicate_start, args.replicate_count, args.output)
    print(json.dumps({key: payload[key] for key in (
        "cell_id", "replicate_start", "replicate_count", "datasets_completed",
        "wall_elapsed_seconds", "payload_sha256"
    )}, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
