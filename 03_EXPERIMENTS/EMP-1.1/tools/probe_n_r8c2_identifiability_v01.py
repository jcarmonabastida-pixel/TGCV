"""Bounded, fail-closed identifiability probe for N-R8-C2.

This probe is NOT corpus generation and performs no scientific execution.
It searches only microscopic fixed-component directed-edge fixtures and asks
whether equal K_C2 states can have different transformation-organisation
structure O_T.

It deliberately does not modify the authoritative Branch N module or the
existing N-R8 constructor.
"""
from __future__ import annotations

import hashlib
import importlib.util
import json
from itertools import combinations
from pathlib import Path
from statistics import mean, pstdev

ROOT = Path(__file__).resolve().parents[1]
SRC = ROOT / "src" / "branch_n_r_v02.py"
OLD_CONSTRUCTOR = ROOT / "src" / "branch_n_r8b_corpus_v01.py"

COMPONENTS = ("A1", "A2", "B1", "B2", "C1", "C2")
FIXTURE_COMPONENT_SETS = (("A1", "A2", "B1"), ("A1", "A2", "B1", "B2"))
FIXTURE_RESOURCES = (1, 1, 1)
FIXTURE_OBJECTIVE = "O01"
MAX_FIXTURE_STATES = 1 << 12


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"CANNOT_LOAD_MODULE:{path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_constructor_module():
    return load_module(OLD_CONSTRUCTOR, "branch_n_r8b_constructor_probe")


def transformation_organisation(nr, state):
    """Return canonical G_T and integer O_T audit features."""
    t_acc = nr.enumerate_transformations(state)
    n = len(t_acc)
    edges = []

    for i, j in combinations(range(n), 2):
        tau, sigma = t_acc[i], t_acc[j]
        try:
            s_tau = nr.apply_transformation(state, tau)
            s_sigma = nr.apply_transformation(state, sigma)
            nr.apply_transformation(s_tau, sigma)
            nr.apply_transformation(s_sigma, tau)
            left = nr.apply_transformation(s_tau, sigma)
            right = nr.apply_transformation(s_sigma, tau)
        except ValueError:
            continue
        if left == right:
            edges.append((i, j))

    adjacency = [set() for _ in range(n)]
    for i, j in edges:
        adjacency[i].add(j)
        adjacency[j].add(i)

    degrees = tuple(len(a) for a in adjacency)
    visited = set()
    component_sizes = []
    for root in range(n):
        if root in visited:
            continue
        stack = [root]
        visited.add(root)
        size = 0
        while stack:
            v = stack.pop()
            size += 1
            for w in adjacency[v]:
                if w not in visited:
                    visited.add(w)
                    stack.append(w)
        component_sizes.append(size)

    triangles = sum(
        1
        for i, j in edges
        for k in adjacency[i].intersection(adjacency[j])
        if j < k
    )

    # Integer-only core is used for the identifiability decision. Floating
    # statistics are reported but never used to select a fixture.
    o_core = (
        n,
        len(edges),
        len(component_sizes),
        max(component_sizes) if component_sizes else 0,
        triangles,
        sum(1 for d in degrees if d == 0),
        sum(1 for d in degrees if d == 1),
        sum(1 for d in degrees if d == 2),
        sum(1 for d in degrees if d >= 3),
    )
    density = (2.0 * len(edges) / (n * (n - 1))) if n >= 2 else 0.0
    o_report = o_core + (density, mean(degrees) if degrees else 0.0, pstdev(degrees) if degrees else 0.0)
    graph_serial = json.dumps({"n": n, "edges": edges}, separators=(",", ":"), sort_keys=True).encode("ascii")
    graph_hash = hashlib.sha256(graph_serial).hexdigest()
    return o_core, o_report, graph_hash, len(edges), n * (n - 1) // 2


def main() -> int:
    nr = load_module(SRC, "branch_n_r_v02_probe")
    op = load_constructor_module()

    # The existing constructor's C key is the authoritative K_C2 implementation.
    if not hasattr(op, "_c_match_key"):
        raise AssertionError("C_MATCH_KEY_NOT_FOUND")

    fixtures = []
    pair_checks = 0
    by_key = {}

    for comps in FIXTURE_COMPONENT_SETS:
        possible = tuple((u, v) for u in comps for v in comps if u != v)
        if (1 << len(possible)) > MAX_FIXTURE_STATES:
            raise AssertionError("FIXTURE_BOUND_EXCEEDED")
        for mask in range(1 << len(possible)):
            edges = tuple(possible[i] for i in range(len(possible)) if mask & (1 << i))
            state = nr.State.make(comps, edges, FIXTURE_RESOURCES, FIXTURE_OBJECTIVE)
            key = op._c_match_key(state)
            o_core, o_report, graph_hash, edge_count, candidate_pairs = transformation_organisation(nr, state)
            rec = (state, o_core, o_report, graph_hash, edge_count, candidate_pairs)
            by_key.setdefault(key, []).append(rec)
            fixtures.append(rec)

    for key, records in by_key.items():
        if len(records) < 2:
            continue
        for a, b in combinations(records, 2):
            pair_checks += 1
            sa, oa, _, gha, _, _ = a
            sb, ob, _, ghb, _, _ = b
            if oa != ob:
                result = {
                    "status": "PASS",
                    "decision": "IDENTIFIABLE",
                    "fixture_family": "fixed_components_directed_edge_subsets",
                    "states_examined": len(fixtures),
                    "key_collision_pairs_examined": pair_checks,
                    "state_a": repr(sa),
                    "state_b": repr(sb),
                    "o_core_a": oa,
                    "o_core_b": ob,
                    "graph_hash_a": gha,
                    "graph_hash_b": ghb,
                    "scientific_execution": "NOT_PERFORMED",
                    "corpus_generation": "NOT_PERFORMED",
                    "n_r7": "INTACT",
                }
                print(json.dumps(result, indent=2, sort_keys=True))
                return 0

    result = {
        "status": "FAIL",
        "decision": "UNRESOLVED_OR_DERIVED",
        "fixture_family": "fixed_components_directed_edge_subsets",
        "states_examined": len(fixtures),
        "key_collision_pairs_examined": pair_checks,
        "note": "No equal-K_C2 / unequal-O_T pair was found in the bounded fixture search.",
        "scientific_execution": "NOT_PERFORMED",
        "corpus_generation": "NOT_PERFORMED",
        "n_r7": "INTACT",
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
