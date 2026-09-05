"""Bounded identifiability probe for frozen N-R8-C2 vNext.

This probe is result-blind with respect to the target comparison: the frozen
C2 key is computed only from state variables, while O_T is computed separately.
No corpus generation or scientific execution is performed here.
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
    ops = load_module(OPS, "branch_n_r8_operationalisation_v01_probe")
    key = load_module(KEY, "branch_n_r8c2_vnext_key_v01_probe")
    return ops, key


def transformation_organisation_graph(state, ops):
    """Construct O_T: transformations as nodes, commutation as edges."""
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
    """Result observable O_T, kept independent of the C2 key."""
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
    """Bounded exhaustive fixture family: fixed 4-component states with all edge subsets."""
    components = ("A1", "A2", "B1", "B2")
    possible = tuple((a, b) for a in components for b in components if a != b)
    resources = (0, 1, 2)
    objective = "O01"
    for mask in range(1 << len(possible)):
        edges = tuple(possible[i] for i in range(len(possible)) if mask & (1 << i))
        yield ops.canonical_state(components, edges, resources, objective)


def main():
    ops, keymod = load_modules()
    buckets = defaultdict(list)
    states_examined = 0
    key_collision_pairs_examined = 0

    for state in fixture_states(ops):
        states_examined += 1
        key = keymod.c2_vnext_key(state)
        buckets[key].append(state)

    for key, states in buckets.items():
        if len(states) < 2:
            continue
        graphs = {}
        for state in states:
            graphs[state.sha256()] = graph_signature(transformation_organisation_graph(state, ops))
        items = list(graphs.items())
        key_collision_pairs_examined += len(items) * (len(items) - 1) // 2
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                if items[i][1] != items[j][1]:
                    result = {
                        "corpus_generation": "NOT_PERFORMED",
                        "decision": "IDENTIFIABLE",
                        "fixture_family": "fixed_4_component_all_directed_edge_subsets",
                        "key_collision_pairs_examined": key_collision_pairs_examined,
                        "n_r7": "INTACT",
                        "states_examined": states_examined,
                        "scientific_execution": "NOT_PERFORMED",
                        "status": "PASS",
                        "witness": {"state_a_sha256": items[i][0], "state_b_sha256": items[j][0]},
                    }
                    print(json.dumps(result, indent=2, sort_keys=True))
                    return

    result = {
        "corpus_generation": "NOT_PERFORMED",
        "decision": "UNRESOLVED_OR_DERIVED",
        "fixture_family": "fixed_4_component_all_directed_edge_subsets",
        "key_collision_pairs_examined": key_collision_pairs_examined,
        "n_r7": "INTACT",
        "states_examined": states_examined,
        "scientific_execution": "NOT_PERFORMED",
        "status": "FAIL",
        "note": "No equal-K_C2_vNext / unequal-O_T pair was found in the bounded fixture search.",
    }
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
