"""Deterministic witness search for N-R8-C2 vNext C4 conformance.

Purpose
-------
Recover an exact equal-K_C2_vNext / unequal-O_T witness from the same bounded
4-component fixture family used by the prior identifiability probe.

This is a preparation/conformance step only. It does not generate the 5,000-
pair corpus and does not perform scientific execution.

Methodological constraints
--------------------------
* K_C2_vNext is imported unchanged from the frozen key module.
* O_T is constructed independently from transformations and commutation.
* Candidate states are bucketed by K only; O_T is evaluated only inside
  collision buckets.
* The search is deterministic: fixture mask order is preserved and the first
  unequal-O_T pair is returned.
* No criterion is modified to force a witness.
"""
from __future__ import annotations

import importlib.util
import itertools
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "src"
OPS = SRC / "branch_n_r8_operationalisation_v01.py"
KEY = SRC / "branch_n_r8c2_vnext_key_v01.py"


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load module: {path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


def load_modules():
    src_dir = str(SRC)
    if src_dir not in sys.path:
        sys.path.insert(0, src_dir)
    ops = load_module(OPS, "branch_n_r8_operationalisation_v01_c4_probe")
    key = load_module(KEY, "branch_n_r8c2_vnext_key_v01_c4_probe")
    return ops, key


def transformation_organisation_graph(state, ops):
    """Construct O_T with transformations as nodes and commutation as edges."""
    transformations = ops.enumerate_transformations(state)
    successors = {t: ops.apply(state, t) for t in transformations}
    graph = {t: set() for t in transformations}
    for a, b in itertools.combinations(transformations, 2):
        try:
            ab = ops.apply(successors[a], b)
            ba = ops.apply(successors[b], a)
        except (ValueError, KeyError):
            continue
        if ab == ba:
            graph[a].add(b)
            graph[b].add(a)
    return graph


def graph_signature(graph):
    """Compact observable signature for O_T."""
    n = len(graph)
    degrees = tuple(sorted(len(v) for v in graph.values()))
    seen = set()
    components = []
    for node in graph:
        if node in seen:
            continue
        stack = [node]
        seen.add(node)
        size = 0
        while stack:
            x = stack.pop()
            size += 1
            for y in graph[x]:
                if y not in seen:
                    seen.add(y)
                    stack.append(y)
        components.append(size)
    triangles_twice = sum(
        sum(1 for b in graph[a] for c in graph[b] if c in graph[a])
        for a in graph
    )
    triangles = triangles_twice // 6
    return (n, tuple(sorted(components)), degrees, triangles)


def fixture_states(ops):
    """Yield (mask, state) for the frozen bounded fixture family."""
    components = ("A1", "A2", "B1", "B2")
    possible = tuple((a, b) for a in components for b in components if a != b)
    resources = (0, 1, 2)
    objective = "O01"
    for mask in range(1 << len(possible)):
        edges = tuple(possible[i] for i in range(len(possible)) if mask & (1 << i))
        yield mask, ops.canonical_state(components, edges, resources, objective)


def state_record(mask, state):
    return {
        "mask": mask,
        "sha256": state.sha256(),
        "components": list(state.components),
        "edges": [list(edge) for edge in state.edges],
        "resources": list(state.resources),
        "objective": state.objective,
    }


def main():
    ops, keymod = load_modules()
    buckets = defaultdict(list)
    states_examined = 0

    # Phase 1: result-blind bucketing by the frozen state-derived key only.
    for mask, state in fixture_states(ops):
        states_examined += 1
        buckets[keymod.c2_vnext_key(state)].append((mask, state))

    key_collision_pairs_examined = 0

    # Phase 2: evaluate O_T only inside equal-key buckets.
    for key, states in buckets.items():
        if len(states) < 2:
            continue

        key_collision_pairs_examined += len(states) * (len(states) - 1) // 2
        signatures = []
        for mask, state in states:
            signature = graph_signature(transformation_organisation_graph(state, ops))
            signatures.append((mask, state, signature))

        for i in range(len(signatures)):
            for j in range(i + 1, len(signatures)):
                a_mask, state_a, sig_a = signatures[i]
                b_mask, state_b, sig_b = signatures[j]
                if sig_a == sig_b:
                    continue

                result = {
                    "corpus_generation": "NOT_PERFORMED",
                    "decision": "IDENTIFIABLE",
                    "fixture_family": "fixed_4_component_all_directed_edge_subsets",
                    "key_collision_pairs_examined": key_collision_pairs_examined,
                    "n_r7": "INTACT",
                    "scientific_execution": "NOT_PERFORMED",
                    "states_examined": states_examined,
                    "status": "PASS",
                    "witness": {
                        "key": repr(key),
                        "state_a": state_record(a_mask, state_a),
                        "state_b": state_record(b_mask, state_b),
                        "ot_a_signature": sig_a,
                        "ot_b_signature": sig_b,
                    },
                }
                print(json.dumps(result, indent=2, sort_keys=True))
                return

    result = {
        "corpus_generation": "NOT_PERFORMED",
        "decision": "UNRESOLVED_OR_DERIVED",
        "fixture_family": "fixed_4_component_all_directed_edge_subsets",
        "key_collision_pairs_examined": key_collision_pairs_examined,
        "n_r7": "INTACT",
        "scientific_execution": "NOT_PERFORMED",
        "states_examined": states_examined,
        "status": "FAIL",
        "note": "No equal-K_C2_vNext / unequal-O_T pair was found in the bounded fixture search.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
