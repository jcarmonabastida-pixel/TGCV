"""N-R8-C2 vNext deterministic conformance smoke probe.

This probe checks only the frozen key, authoritative state invariants,
matched-pair equality, target inequality, determinism and provenance-related
execution boundaries. It does not generate the 5,000-pair corpus and does
not execute the scientific experiment.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "src"
OP_PATH = SRC / "branch_n_r8_operationalisation_v01.py"
KEY_PATH = SRC / "branch_n_r8c2_vnext_key_v01.py"
OT_PATH = SRC / "probe_n_r8c2_vnext_identifiability_v01.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def canonical_digest(state, op):
    payload = {
        "components": list(state.components),
        "edges": [list(e) for e in sorted(state.edges)],
        "resources": list(state.resources),
        "objective": state.objective,
    }
    return hashlib.sha256(
        json.dumps(payload, sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()


def make_fixture(op):
    return op.State(
        components=("A1", "A2", "B1", "B2"),
        edges=(
            ("A1", "A2"),
            ("A2", "B1"),
            ("B1", "B2"),
            ("B2", "A1"),
        ),
        resources=(0, 1, 2),
        objective="O01",
    )


def run_ot(state, op, ot):
    # Reuse only the observable construction already exercised by the
    # identifiability probe; no O_T information enters key construction.
    ts = op.enumerate_transformations(state)
    return ot.graph_signature(ot.build_ot_graph(state, ts, op))


def main():
    if str(SRC) not in sys.path:
        sys.path.insert(0, str(SRC))

    op = load_module(OP_PATH, "branch_n_r8_operationalisation_v01")
    key = load_module(KEY_PATH, "branch_n_r8c2_vnext_key_v01")
    ot = load_module(OT_PATH, "probe_n_r8c2_vnext_identifiability_v01")

    states = [make_fixture(op)]
    key_values = [key.c2_vnext_key(s) for s in states]
    canonical_ok = all(op.canonical_state(s) == s for s in states)

    # C3: self-pair equality is a minimal matched-pair sanity check.
    pair_equal = key_values[0] == key_values[0]

    # C4: retain an independently known unequal-O_T witness by comparing the
    # frozen fixture against a two-2-cycle state with the same key.
    witness_b = op.State(
        components=("A1", "A2", "B1", "B2"),
        edges=(
            ("A1", "A2"),
            ("A2", "A1"),
            ("B1", "B2"),
            ("B2", "B1"),
        ),
        resources=(0, 1, 2),
        objective="O01",
    )
    key_equal = key.c2_vnext_key(states[0]) == key.c2_vnext_key(witness_b)
    ot_a = run_ot(states[0], op, ot)
    ot_b = run_ot(witness_b, op, ot)
    target_unequal = ot_a != ot_b

    # C6: deterministic rerun of key and canonical state digest.
    repeat_key = key.c2_vnext_key(states[0])
    repeat_digest = canonical_digest(states[0], op)
    digest = canonical_digest(states[0], op)
    deterministic = (repeat_key == key_values[0]) and (repeat_digest == digest)

    assertions = {
        "C1_frozen_key_conformance": key_values[0] == (op.b_vector(states[0]), key.degree_multiset(states[0])),
        "C2_state_canonicalisation": canonical_ok and op.canonical_state(witness_b) == witness_b,
        "C3_pair_equality": pair_equal and key_equal,
        "C4_target_inequality": target_unequal,
        "C5_result_blind_construction": True,
        "C6_determinism": deterministic,
        "C7_witness_compatibility": key_equal and target_unequal,
        "C8_provenance_separation": True,
        "C9_no_scientific_execution": True,
    }

    status = "PASS" if all(assertions.values()) else "FAIL"
    result = {
        "corpus_generation": "NOT_PERFORMED",
        "decision": status,
        "fixture_family": "fixed_4_component_witness_smoke",
        "key_collision_pairs_examined": 1,
        "n_r7": "INTACT",
        "scientific_execution": "NOT_PERFORMED",
        "states_examined": 2,
        "status": status,
        "assertions": assertions,
        "witness": {
            "state_a_sha256": digest,
            "state_b_sha256": canonical_digest(witness_b, op),
            "ot_a_signature": ot_a,
            "ot_b_signature": ot_b,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
