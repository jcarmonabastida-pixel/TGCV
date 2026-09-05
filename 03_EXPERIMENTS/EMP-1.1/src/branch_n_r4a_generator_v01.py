"""Prospective Branch N-R4A snapshot generator.

This is a NEW RECONSTRUCTION. It is not historical EMP-1.1 generator code.
No learner, outcome, or future trajectory information is generated here.
"""
from __future__ import annotations

from dataclasses import dataclass
import hashlib
import json
import random
from typing import Any

COMPONENTS = ("A1", "A2", "B1", "B2", "C1", "C2")
RESOURCE_VALUES = (0, 1, 2, 3)
OBJECTIVES = tuple(f"O{i:02d}" for i in range(1, 13))

@dataclass(frozen=True)
class Snapshot:
    episode_id: int
    components: tuple[str, ...]
    edges: tuple[tuple[str, str], ...]
    resources: tuple[int, int, int]
    objective: str

    def to_record(self) -> dict[str, Any]:
        return {
            "episode_id": self.episode_id,
            "components": list(self.components),
            "edges": [[u, v] for u, v in self.edges],
            "resources": list(self.resources),
            "objective": self.objective,
        }


def generate_snapshot(episode_id: int, rng: random.Random) -> Snapshot:
    n = rng.randint(3, 5)
    components = tuple(sorted(rng.sample(COMPONENTS, n), key=COMPONENTS.index))
    possible_edges = [(u, v) for u in components for v in components if u != v]
    edge_count = rng.randint(0, len(possible_edges))
    edges = tuple(sorted(rng.sample(possible_edges, edge_count), key=lambda e: (COMPONENTS.index(e[0]), COMPONENTS.index(e[1]))))
    resources = tuple(rng.choice(RESOURCE_VALUES) for _ in range(3))
    objective = rng.choice(OBJECTIVES)
    return Snapshot(episode_id, components, edges, resources, objective)


def generate_dataset(count: int, seed: int) -> list[dict[str, Any]]:
    if count < 0:
        raise ValueError("count must be non-negative")
    rng = random.Random(seed)
    return [generate_snapshot(i, rng).to_record() for i in range(count)]


def canonical_json_bytes(records: list[dict[str, Any]]) -> bytes:
    return (json.dumps(records, sort_keys=True, separators=(",", ":"), ensure_ascii=True) + "\n").encode("ascii")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def validate_record(record: dict[str, Any]) -> None:
    comps = tuple(record["components"])
    assert 3 <= len(comps) <= 5
    assert len(set(comps)) == len(comps)
    assert all(c in COMPONENTS for c in comps)
    active = set(comps)
    edges = [tuple(e) for e in record["edges"]]
    assert len(edges) == len(set(edges))
    assert all(u != v and u in active and v in active for u, v in edges)
    assert len(record["resources"]) == 3
    assert all(x in RESOURCE_VALUES for x in record["resources"])
    assert record["objective"] in OBJECTIVES
