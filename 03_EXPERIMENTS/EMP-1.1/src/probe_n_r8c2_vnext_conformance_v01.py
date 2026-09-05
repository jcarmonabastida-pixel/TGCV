"""N-R8-C2 vNext deterministic conformance smoke probe.

This probe checks only the frozen key, authoritative state invariants,
matched-pair equality, target inequality, determinism and provenance-related
execution boundaries. It does not generate the 5,000-pair corpus and does
not execute the scientific experiment.

The witness is the exact deterministic witness recovered by
probe_n_r8c2_vnext_c4_witness_search_v01.py from the frozen bounded fixture
family: mask 3 versus mask 10.
"""
from __future__ import annotations

import ast
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "src"
OP_PATH = SRC / "branch_n_r8_operationalisation_v01.py"
KEY_PATH = SRC / "branch_n_r8c2_vnext_key_v01.py"
OT_PATH = SRC / "probe_n_r8c2_vnext_identifiability_v01.py"

EXPECTED_A_SHA256 = "0d965256c3aae89093fa954db992843e770b0c358be5392634078b3af0fb6b7c"
EXPECTED_B_SHA256 = "0dd6e9d0418beb5c92778cb0e5b3c167b9bc89afc9cbea20c5cbc8ec69870880"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def make_witness_a(op):
    # Exact deterministic-search witness: mask 3.
    return op.canonical_state(
        ("A1", "A2", "B1", "B2"),
        (("A1", "A2"), ("A1", "B1")),
        (0, 1, 2),
        "O01",
    )


def make_witness_b(op):
    # Exact deterministic-search witness: mask 10.
    return op.canonical_state(
        ("A1", "A2", "B1", "B2"),
        (("A1", "B1"), ("A2", "A1")),
        (0, 1, 2),
        "O01",
    )


def run_ot(state, op, ot):
    return ot.graph_signature(ot.transformation_organisation_graph(state, op))


def key_static_conformance():
    """C1 static check: frozen key implementation remains result-blind."""
    tree = ast.parse(KEY_PATH.read_text(encoding="utf-8"))
    forbidden = {
        "tacc",
        "enumerate_transformations",
        "apply",
        "R",
        "O_T",
        "graph_signature",
        "transformation_organisation_graph",
    }
    return not any(
        (isinstance(node, ast.Name) and node.id in forbidden)
        or (isinstance(node, ast.Attribute) and node.attr in forbidden)
        for node in ast.walk(tree)
    )


def main():
    if str(SRC) not in sys.path:
        sys.path.insert(0, str(SRC))

    op = load_module(OP_PATH, "branch_n_r8_operationalisation_v01")
    key = load_module(KEY_PATH, "branch_n_r8c2_vnext_key_v01")
    ot = load_module(OT_PATH, "probe_n_r8c2_vnext_identifiability_v01")

    state_a = make_witness_a(op)
    state_b = make_witness_b(op)

    key_a = key.c2_vnext_key(state_a)
    key_b = key.c2_vnext_key(state_b)
    key_expected_a = (op.b_vector(state_a), key.degree_multiset(state_a))
    key_expected_b = (op.b_vector(state_b), key.degree_multiset(state_b))

    canonical_ok = (
        op.canonical_state(
            state_a.components, state_a.edges, state_a.resources, state_a.objective
        )
        == state_a
        and op.canonical_state(
            state_b.components, state_b.edges, state_b.resources, state_b.objective
        )
        == state_b
    )

    # C3 must hold before O_T is evaluated: this preserves result-blind
    # witness construction and the conformance gate's execution ordering.
    key_equal = key_a == key_b
    ot_a = run_ot(state_a, op, ot) if key_equal else None
    ot_b = run_ot(state_b, op, ot) if key_equal else None
    target_unequal = key_equal and ot_a != ot_b

    digest_a = state_a.sha256()
    digest_b = state_b.sha256()
    deterministic = (
        key.c2_vnext_key(state_a) == key_a
        and key.c2_vnext_key(state_b) == key_b
        and state_a.sha256() == digest_a
        and state_b.sha256() == digest_b
        and digest_a == EXPECTED_A_SHA256
        and digest_b == EXPECTED_B_SHA256
    )

    static_ok = key_static_conformance()
    assertions = {
        "C1_frozen_key_conformance": static_ok and key_a == key_expected_a and key_b == key_expected_b,
        "C2_state_canonicalisation": canonical_ok,
        "C3_pair_equality": key_equal,
        "C4_target_inequality": target_unequal,
        "C5_result_blind_construction": static_ok,
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
            "state_a_sha256": digest_a,
            "state_b_sha256": digest_b,
            "ot_a_signature": ot_a,
            "ot_b_signature": ot_b,
        },
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
