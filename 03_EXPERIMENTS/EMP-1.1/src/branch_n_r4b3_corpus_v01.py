"""Branch N R4B.3 controlled corpus generator/conformance support.

Prospective controlled reconstruction only. This module generates sealed
N-R4A snapshots plus N-R4B trajectories/outcomes. It does not fit a learner,
compute confirmatory statistics, or recover historical EMP-1.1 execution.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import platform
import sys
from pathlib import Path
from typing import Any, Iterable

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src"
R4A_PATH = SRC / "branch_n_r4a_generator_v01.py"
R4B_PATH = SRC / "branch_n_r4b_trajectory_v01.py"
R_PATH = SRC / "branch_n_r_v02.py"


def _load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"MODULE_SPEC_FAILED:{path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


# R4B imports branch_n_r_v02 by module name. Load and register that
# dependency explicitly before loading R4B, so the corpus generator is
# independent of the caller's working directory / sys.path configuration.
r_core = _load_module("branch_n_r_v02", R_PATH)
r4a = _load_module("branch_n_r4a_generator_v01", R4A_PATH)
r4b = _load_module("branch_n_r4b_trajectory_v01", R4B_PATH)

TRAIN_COUNT = 30_000
TEST_COUNT = 10_000
DATASET_SEEDS = {"train": 3_100_000, "test": 4_100_000}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def canonical_json_line(obj: dict[str, Any]) -> bytes:
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode("utf-8")


def snapshot_to_state(record: dict[str, Any]):
    return r4b.State.make(
        record["components"],
        [tuple(e) for e in record["edges"]],
        record["resources"],
        record["objective"],
    )


def snapshot_record(record: dict[str, Any]) -> dict[str, Any]:
    return {
        "components": list(record["components"]),
        "edges": [list(e) for e in record["edges"]],
        "episode_id": int(record["episode_id"]),
        "objective": record["objective"],
        "resources": list(record["resources"]),
    }


def canonical_snapshot_json(record: dict[str, Any]) -> bytes:
    return canonical_json_line(snapshot_record(record))


def snapshot_sha256(record: dict[str, Any]) -> str:
    return sha256_bytes(canonical_state_bytes_from_snapshot(record))


def canonical_state_bytes_from_snapshot(record: dict[str, Any]) -> bytes:
    obj = {
        "components": list(record["components"]),
        "edges": [list(e) for e in record["edges"]],
        "objective": record["objective"],
        "resources": list(record["resources"]),
    }
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def trajectory_record_dict(rec) -> dict[str, Any]:
    return {
        "dataset_seed": rec.dataset_seed,
        "dataset_split": rec.dataset_split,
        "episode_id": rec.episode_id,
        "horizon": rec.horizon,
        "initial_snapshot_sha256": rec.initial_snapshot_sha256,
        "objective": rec.objective,
        "outcome": rec.outcome,
        "steps": [
            {
                "state_sha256_after": s.state_sha256_after,
                "state_sha256_before": s.state_sha256_before,
                "step": s.step,
                "transformation_id": s.transformation_id,
            }
            for s in rec.steps
        ],
        "terminal_reason": rec.terminal_reason,
        "terminal_step": rec.terminal_step,
        "trajectory_seed": rec.trajectory_seed,
    }


def generate_partition(split: str, count: int, seed: int) -> tuple[list[dict[str, Any]], list[Any]]:
    if split not in DATASET_SEEDS or DATASET_SEEDS[split] != seed:
        raise ValueError("INVALID_DATASET_SEED")
    snapshots = r4a.generate_dataset(count, seed)
    trajectories = []
    for rec in snapshots:
        state = snapshot_to_state(rec)
        trajectories.append(r4b.generate_trajectory(state, split, seed, rec["episode_id"]))
    return snapshots, trajectories


def write_jsonl(path: Path, records: Iterable[dict[str, Any]]) -> str:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as f:
        for record in records:
            f.write(canonical_json_line(record))
    return file_sha256(path)


def write_partition(output_dir: Path, split: str, snapshots: list[dict[str, Any]], trajectories: list[Any]) -> dict[str, Any]:
    snap_path = output_dir / f"{split}_snapshots.jsonl"
    traj_path = output_dir / f"{split}_trajectories.jsonl"
    snapshot_hash = write_jsonl(snap_path, (snapshot_record(r) for r in snapshots))
    trajectory_hash = write_jsonl(traj_path, (trajectory_record_dict(r) for r in trajectories))
    return {
        "dataset_split": split,
        "dataset_seed": DATASET_SEEDS[split],
        "episode_count": len(snapshots),
        "snapshots_path": snap_path.name,
        "snapshots_sha256": snapshot_hash,
        "trajectories_path": traj_path.name,
        "trajectories_sha256": trajectory_hash,
    }


def provenance(output_dir: Path, partitions: list[dict[str, Any]], generator_path: Path, trajectory_path: Path) -> dict[str, Any]:
    return {
        "artifact": "N-R4B.3_CONTROLLED_TRAJECTORY_OUTCOME_CORPUS",
        "status": "CONTROLLED_GENERATION",
        "historical_recovery": False,
        "specification": "N-R4B.3 v0.1",
        "parent_semantics": "N-R4B.1 v0.1",
        "r4a_implementation_sha256": file_sha256(R4A_PATH),
        "r4b_implementation_sha256": file_sha256(trajectory_path),
        "corpus_support_implementation_sha256": file_sha256(generator_path),
        "python_version": platform.python_version(),
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "partitions": partitions,
        "learner_executed": False,
        "confirmatory_inference_executed": False,
        "historical_result_used_as_tuning_target": False,
    }


def generate_controlled_corpus(output_dir: Path) -> dict[str, Any]:
    output_dir.mkdir(parents=True, exist_ok=True)
    partitions = []
    for split, count in (("train", TRAIN_COUNT), ("test", TEST_COUNT)):
        snapshots, trajectories = generate_partition(split, count, DATASET_SEEDS[split])
        partitions.append(write_partition(output_dir, split, snapshots, trajectories))
    manifest = provenance(output_dir, partitions, Path(__file__), R4B_PATH)
    manifest_path = output_dir / "PROVENANCE.json"
    manifest_path.write_bytes(canonical_json_line(manifest))
    return manifest
