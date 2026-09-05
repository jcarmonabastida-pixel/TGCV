"""Prospective Branch N R4B trajectory/outcome generator v0.1.

This is a controlled reconstruction, not historical MVE-1.0 recovery.
"""

from __future__ import annotations

import hashlib
import json
import random
from dataclasses import dataclass
from typing import Iterable

from branch_n_r_v02 import State, Transformation, apply_transformation, enumerate_transformations

HORIZON = 6
DATASET_SEEDS = {"train": 3_100_000, "test": 4_100_000}
OBJECTIVES = tuple(f"O{i:02d}" for i in range(1, 13))


def goal(state: State, objective: str) -> bool:
    if objective == "O01":
        return "A1" in state.components
    if objective == "O02":
        return "A2" in state.components
    if objective == "O03":
        return "B1" in state.components
    if objective == "O04":
        return "B2" in state.components
    if objective == "O05":
        return "C1" in state.components
    if objective == "O06":
        return "C2" in state.components
    if objective == "O07":
        return state.resources[0] == 3
    if objective == "O08":
        return state.resources[1] == 3
    if objective == "O09":
        return state.resources[2] == 3
    if objective == "O10":
        return state.resources[0] == 0
    if objective == "O11":
        return state.resources[1] == 0
    if objective == "O12":
        return state.resources[2] == 0
    raise ValueError(f"UNKNOWN_OBJECTIVE:{objective}")


def trajectory_seed(dataset_seed: int, episode_id: int) -> int:
    return dataset_seed + episode_id


def canonical_state_bytes(state: State) -> bytes:
    obj = {
        "components": list(state.components),
        "edges": [list(e) for e in state.edges],
        "objective": state.objective,
        "resources": list(state.resources),
    }
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")


def state_sha256(state: State) -> str:
    return hashlib.sha256(canonical_state_bytes(state)).hexdigest()


def transformation_id(t: Transformation) -> str:
    return repr(t)


@dataclass(frozen=True)
class StepRecord:
    step: int
    state_sha256_before: str
    transformation_id: str
    state_sha256_after: str


@dataclass(frozen=True)
class TrajectoryRecord:
    episode_id: int
    dataset_split: str
    dataset_seed: int
    trajectory_seed: int
    initial_snapshot_sha256: str
    objective: str
    horizon: int
    steps: tuple[StepRecord, ...]
    terminal_step: int
    terminal_reason: str
    outcome: int


def generate_trajectory(state: State, dataset_split: str, dataset_seed: int, episode_id: int) -> TrajectoryRecord:
    if dataset_split not in DATASET_SEEDS or DATASET_SEEDS[dataset_split] != dataset_seed:
        raise ValueError("INVALID_DATASET_SEED")
    if episode_id < 0:
        raise ValueError("INVALID_EPISODE_ID")

    seed = trajectory_seed(dataset_seed, episode_id)
    rng = random.Random(seed)
    current = state
    records: list[StepRecord] = []

    for h in range(HORIZON + 1):
        if goal(current, state.objective):
            return TrajectoryRecord(
                episode_id, dataset_split, dataset_seed, seed,
                state_sha256(state), state.objective, HORIZON,
                tuple(records), h, "GOAL_REACHED", 1,
            )
        if h == HORIZON:
            return TrajectoryRecord(
                episode_id, dataset_split, dataset_seed, seed,
                state_sha256(state), state.objective, HORIZON,
                tuple(records), h, "HORIZON_EXHAUSTED", 0,
            )

        tacc = enumerate_transformations(current)
        if not tacc:
            return TrajectoryRecord(
                episode_id, dataset_split, dataset_seed, seed,
                state_sha256(state), state.objective, HORIZON,
                tuple(records), h, "NO_ACCESSIBLE_TRANSFORMATION", 0,
            )

        selected = tacc[rng.randrange(len(tacc))]
        before = state_sha256(current)
        nxt = apply_transformation(current, selected)
        after = state_sha256(nxt)
        records.append(StepRecord(h, before, transformation_id(selected), after))
        current = nxt

    raise AssertionError("UNREACHABLE")


def canonical_trajectory_json(record: TrajectoryRecord) -> bytes:
    obj = {
        "dataset_seed": record.dataset_seed,
        "dataset_split": record.dataset_split,
        "episode_id": record.episode_id,
        "horizon": record.horizon,
        "initial_snapshot_sha256": record.initial_snapshot_sha256,
        "objective": record.objective,
        "outcome": record.outcome,
        "steps": [
            {
                "state_sha256_after": s.state_sha256_after,
                "state_sha256_before": s.state_sha256_before,
                "step": s.step,
                "transformation_id": s.transformation_id,
            }
            for s in record.steps
        ],
        "terminal_reason": record.terminal_reason,
        "terminal_step": record.terminal_step,
        "trajectory_seed": record.trajectory_seed,
    }
    return (json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode("utf-8")


def canonical_trajectory_jsonl(records: Iterable[TrajectoryRecord]) -> bytes:
    ordered = sorted(records, key=lambda r: r.episode_id)
    return b"".join(canonical_trajectory_json(r) for r in ordered)
