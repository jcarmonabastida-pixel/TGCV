"""N-R8-C2 vNext prospective corpus generator.

Preparation-stage implementation. Candidate construction is result-blind:
K_C2_vNext is computed before any O_T evaluation. O_T is imported only through
the authoritative identifiability implementation and evaluated post hoc.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import random
import sys
from pathlib import Path
from typing import Iterable

from branch_n_r8_operationalisation_v01 import canonical_state
from branch_n_r8c2_vnext_key_v01 import c2_vnext_key

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "src"
OPS_PATH = SRC / "branch_n_r8_operationalisation_v01.py"
KEY_PATH = SRC / "branch_n_r8c2_vnext_key_v01.py"
OT_PATH = SRC / "probe_n_r8c2_vnext_identifiability_v01.py"
CONFIG_PATH = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "N-R8-C2_vNEXT_GENERATION_CONFIG_v0.1.json"
CONTRACT_PATH = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "N-R8-C2_vNEXT_CORPUS_GENERATION_CONTRACT_v0.1.md"

TARGET_PAIRS = 5000
SEED = 582031
COMPONENTS = ("A1", "A2", "B1", "B2", "C1", "C2")
OBJECTIVES = tuple(f"O{i:02d}" for i in range(1, 13))
EXPECTED_SHA256 = {
    "operationalisation": "0cc01c7afb051b44f010a798a1b8a256dff286c9",
    "key": "40a8cfa6c74cbdf253285b3073372e6c42d262e3",
    "ot": "095cff6c69adfba19b1722a5a355b58f7e2cbe1a",
    "config": "48c00a16fb50d2258e50920b3bd283810c60d149",
    "contract": "62e0ad9b5b075276af4a8716f8ac824e14a47021",
}


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=True)


def file_sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify_frozen_inputs() -> dict[str, bool]:
    paths = {"operationalisation": OPS_PATH, "key": KEY_PATH, "ot": OT_PATH,
             "config": CONFIG_PATH, "contract": CONTRACT_PATH}
    return {name: path.exists() and file_sha256(path) == expected
            for (name, path), expected in zip(paths.items(), EXPECTED_SHA256.values())}


def load_ot_module():
    src_dir = str(SRC)
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)
    spec = importlib.util.spec_from_file_location("tgcv_r8c2_ot_authoritative", OT_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load authoritative O_T: {OT_PATH}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def canonical_state_from_rng(rng: random.Random):
    """Result-blind candidate construction from frozen state variables only."""
    n = rng.choice((4, 5, 6))
    components = rng.sample(list(COMPONENTS), n)
    possible = [(a, b) for a in components for b in components if a != b]
    density = rng.choice((0.10, 0.25, 0.50, 0.75))
    k = round(density * len(possible))
    edges = rng.sample(possible, k)
    resources = tuple(rng.randrange(4) for _ in range(3))
    objective = rng.choice(OBJECTIVES)
    return canonical_state(components, edges, resources, objective)


def generate_candidate(rng: random.Random):
    return canonical_state_from_rng(rng)


def build_candidate_buckets(candidates: Iterable) -> dict[tuple, list]:
    """Bucket solely by frozen K; O_T is absent from this construction stage."""
    buckets: dict[tuple, list] = {}
    for state in candidates:
        key = c2_vnext_key(state)
        buckets.setdefault(key, []).append(state)
    return buckets


def ordered_pairs(bucket: list):
    states = sorted(bucket, key=lambda s: s.sha256())
    for i, a in enumerate(states):
        for b in states[i + 1:]:
            yield a, b


def evaluate_ot_after_key_equality(state_a, state_b):
    """Evaluate authoritative O_T only after exact K equality has been checked."""
    if c2_vnext_key(state_a) != c2_vnext_key(state_b):
        raise ValueError("O_T evaluation forbidden before key equality")
    ot = load_ot_module()
    ga = ot.transformation_organisation_graph(state_a, ot.load_modules()[0])
    gb = ot.transformation_organisation_graph(state_b, ot.load_modules()[0])
    return ot.graph_signature(ga), ot.graph_signature(gb)


def pair_id(state_a, state_b) -> str:
    hashes = sorted((state_a.sha256(), state_b.sha256()))
    return hashlib.sha256(canonical_json(hashes).encode("utf-8")).hexdigest()


def state_record(state) -> dict:
    return {"components": list(state.components), "edges": [list(e) for e in state.edges],
            "resources": list(state.resources), "objective": state.objective}


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
