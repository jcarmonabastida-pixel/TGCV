#!/usr/bin/env python3
"""TR-131 VisitAll Dynamic Transformation Space exhaustive depth-2 runner.

Scientific runner implementation only. Authorization is governed externally
by the package freeze/audit gates. This runner performs no planner search,
optimization, goal-directed selection, value evaluation, or TGCV inference.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from TR131_VISITALL_SOURCE_DEFINED_TRANSITION_ADAPTER_001 import Move, applicable_moves, apply_move

ROOT = Path(__file__).resolve().parent
LOCK = ROOT / "TR131_EXACT_FIXTURE_SOURCE_LOCK_v01.json"
DEPTH = 2


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_value(value):
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def state_key(state):
    return canonical_json(state)


def tacc_ids(state, connected):
    return tuple(sorted(m.identity for m in applicable_moves(state, connected)))


def delta_tacc(t0, t1):
    a, b = set(t0), set(t1)
    return {
        "Added": sorted(b - a),
        "Removed": sorted(a - b),
        "Retained": sorted(a & b),
    }


def load_fixture():
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    va = lock["visitall"]
    s0 = {
        "at-robot": va["initial_state"]["at_robot"],
        "visited": sorted(va["initial_state"]["visited"]),
    }
    return lock, s0


def build_connected_grid():
    connected = set()
    for x in range(5):
        for y in range(5):
            here = f"loc-x{x}-y{y}"
            for nx, ny in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                if 0 <= nx < 5 and 0 <= ny < 5:
                    connected.add((here, f"loc-x{nx}-y{ny}"))
    return connected


def make_node(branch, depth, state, connected, parent_tacc=None, realized=None):
    tacc = tacc_ids(state, connected)
    node = {
        "branch": branch,
        "depth": depth,
        "S_t": state,
        "T_acc_t": list(tacc),
        "T_acc_hash": sha256_value(tacc),
    }
    if realized is not None:
        node["T_real_t"] = realized.identity
        node["S_parent"] = None
        node["T_acc_parent"] = list(parent_tacc)
        node["Delta_T_acc_from_parent"] = delta_tacc(parent_tacc, tacc)
        node["baseline"] = {
            "S_t": None,
            "T_real_t": realized.identity,
            "S_t1": state,
        }
    return node


def main():
    lock, s0 = load_fixture()
    connected = build_connected_grid()

    root_tacc = tacc_ids(s0, connected)
    expected = set(lock["visitall"]["t_acc"]["transformations"])
    if set(root_tacc) != expected:
        raise RuntimeError("locked initial T_acc does not match source-defined adapter construction")

    nodes = [make_node("root", 0, s0, connected)]
    leaves = []

    frontier = [("root", s0, root_tacc, [])]

    while frontier:
        branch, state, parent_tacc, trajectory = frontier.pop(0)
        depth = len(trajectory)
        if depth >= DEPTH:
            leaves.append(branch)
            continue

        actions = applicable_moves(state, connected)
        for index, action in enumerate(actions):
            child_branch = f"{branch}.{index}"
            successor = apply_move(state, action, connected)
            child_tacc = tacc_ids(successor, connected)
            node = make_node(
                child_branch, depth + 1, successor, connected,
                parent_tacc=parent_tacc, realized=action
            )
            node["baseline"]["S_t"] = state
            nodes.append(node)
            frontier.append((
                child_branch,
                successor,
                child_tacc,
                trajectory + [action.identity],
            ))

    edges = [n for n in nodes if "T_real_t" in n]

    report = {
        "record_type": "TGCV_TR131_VISITALL_DYNAMIC_SPACE_DEPTH2_RUN",
        "status": "COMPLETED",
        "scientific_execution_authorized": False,
        "scientific_execution_performed": True,
        "source_repository": lock["visitall"]["repository"],
        "source_revision": lock["visitall"]["revision"],
        "source_blob_sha": lock["visitall"]["blob_sha"],
        "problem": lock["visitall"]["problem"],
        "depth": DEPTH,
        "root_tacc_cardinality": len(root_tacc),
        "node_count": len(nodes),
        "edge_count": len(edges),
        "leaf_count": len(leaves),
        "nodes": nodes,
        "cases": {
            "C1": "NOT_TESTABLE",
            "C2": "enumerated at root",
            "C3": "enumerated through depth 2",
            "C4": "computed on every realized edge"
        },
        "overall_representation_result": "NOT_EVALUATED_BY_RUNNER",
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
