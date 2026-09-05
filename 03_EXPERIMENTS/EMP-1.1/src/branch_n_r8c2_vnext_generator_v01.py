"""N-R8-C2 vNext prospective corpus generator.

Preparation-stage implementation only. It constructs candidate states result-blind,
buckets by the frozen K_C2_vNext key, and applies O_T only post hoc for acceptance.
It does not consume the Rust dataset or execute the scientific experiment.
"""
from __future__ import annotations

import hashlib
import json
import random
from pathlib import Path
from typing import Iterable

from branch_n_r8_operationalisation_v01 import canonical_state
from branch_n_r8c2_vnext_key_v01 import c2_vnext_key

TARGET_PAIRS = 5000
SEED = 582031
COMPONENTS = ("A1", "A2", "B1", "B2", "C1", "C2")
OBJECTIVES = tuple(f"O{i:02d}" for i in range(1, 13))


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def pair_id(state_a, state_b) -> str:
    """Deterministic unordered-pair identity from canonical state hashes."""
    hashes = sorted((state_a.sha256(), state_b.sha256()))
    return hashlib.sha256(canonical_json(hashes).encode("utf-8")).hexdigest()


def state_record(state) -> dict:
    return {"components": list(state.components), "edges": [list(e) for e in state.edges],
            "resources": list(state.resources), "objective": state.objective}


def generate_candidate(rng: random.Random):
    """Result-blind candidate construction from the frozen state representation."""
    n = rng.choice((4, 5, 6))
    components = rng.sample(list(COMPONENTS), n)
    possible = [(a, b) for a in components for b in components if a != b]
    density = rng.choice((0.10, 0.25, 0.50, 0.75))
    k = round(density * len(possible))
    edges = rng.sample(possible, k)
    resources = tuple(rng.randrange(4) for _ in range(3))
    objective = rng.choice(OBJECTIVES)
    return canonical_state(components, edges, resources, objective)


def build_candidate_buckets(candidates: Iterable) -> dict[tuple, list]:
    """Bucket solely by frozen K; O_T is intentionally absent from this stage."""
    buckets: dict[tuple, list] = {}
    for state in candidates:
        key = c2_vnext_key(state)
        buckets.setdefault(key, []).append(state)
    return buckets


def ordered_pairs(bucket: list):
    """Deterministic pair ordering; acceptance is deliberately deferred."""
    states = sorted(bucket, key=lambda s: s.sha256())
    for i, a in enumerate(states):
        for b in states[i + 1:]:
            yield a, b


def acceptance_signature(state):
    """Placeholder boundary for the authoritative O_T implementation.

    This generator scaffold intentionally does not duplicate or redefine O_T.
    The preflight must bind this boundary to the authoritative probe implementation
    before any corpus generation is authorised.
    """
    raise RuntimeError("O_T binding required by preflight before generation")


def manifest(config: dict, input_shas: dict[str, str]) -> dict:
    return {
        "contract_version": "N-R8-C2_vNEXT_CORPUS_GENERATION_CONTRACT_v0.1",
        "generator_version": "branch_n_r8c2_vnext_generator_v01",
        "seed": SEED,
        "target_pair_count": TARGET_PAIRS,
        "frozen_input_shas": dict(sorted(input_shas.items())),
        "configuration": config,
        "status": "PREPARATION_ONLY",
        "corpus_generation": "NOT_PERFORMED",
        "scientific_execution": "NOT_PERFORMED",
    }
