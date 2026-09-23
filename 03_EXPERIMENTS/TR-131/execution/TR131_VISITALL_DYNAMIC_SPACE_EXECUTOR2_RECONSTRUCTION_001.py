#!/usr/bin/env python3
"""TR-131 VisitAll Dynamic Transformation Space independent Executor-2 reconstruction.

Independent reconstruction only. This script does not read Executor-1 output
or any derived scientific dataset.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path

from TR131_VISITALL_SOURCE_DEFINED_TRANSITION_ADAPTER_001 import Move, applicable_moves, apply_move

ROOT = Path(__file__).resolve().parent
LOCK = ROOT / "TR131_EXACT_FIXTURE_SOURCE_LOCK_v01.json"
DEPTH = 2


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_value(value):
    return hashlib.sha256(canonical_json(value).encode("utf-8")).hexdigest()


def delta_tacc(before, after):
    a, b = set(before), set(after)
    return {
        "Added": sorted(b - a),
        "Removed": sorted(a - b),
        "Retained": sorted(a & b),
    }


def tacc(state, connected):
    return tuple(sorted(m.identity for m in applicable_moves(state, connected)))


def build_connected():
    edges = set()
    for x in range(5):
        for y in range(5):
            here = f"loc-x{x}-y{y}"
            for nx, ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
                if 0 <= nx < 5 and 0 <= ny < 5:
                    edges.add((here, f"loc-x{nx}-y{ny}"))
    return edges


def main():
    authorized = os.environ.get("TGCV_TR131_SCIENTIFIC_AUTHORIZED") == "YES"
    if not authorized:
        print(json.dumps({
            "record_type": "TGCV_TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR2_AUTHORIZATION_REFUSAL",
            "status": "NOT_AUTHORIZED",
            "executor": "EXECUTOR_2",
            "scientific_execution_authorized": False,
            "scientific_execution_performed": False,
            "authorization_mechanism": "TGCV_TR131_SCIENTIFIC_AUTHORIZED=YES",
        }, indent=2, ensure_ascii=False))
        return 3
    lock = json.loads(LOCK.read_text(encoding="utf-8"))
    va = lock["visitall"]
    connected = build_connected()
    state = {
        "at-robot": va["initial_state"]["at_robot"],
        "visited": sorted(va["initial_state"]["visited"]),
    }

    root_tacc = tacc(state, connected)
    expected = set(va["t_acc"]["transformations"])
    if set(root_tacc) != expected:
        raise RuntimeError("Executor-2 source reconstruction mismatch at root T_acc")

    nodes = [{
        "branch": "root",
        "depth": 0,
        "S_t": state,
        "T_acc_t": list(root_tacc),
        "T_acc_hash": sha256_value(root_tacc),
    }]

    frontier = [("root", state, root_tacc, [])]

    while frontier:
        branch, current, current_tacc, trajectory = frontier.pop(0)
        if len(trajectory) >= DEPTH:
            continue

        actions = applicable_moves(current, connected)
        for index, action in enumerate(actions):
            successor = apply_move(current, action, connected)
            successor_tacc = tacc(successor, connected)
            child = f"{branch}.{index}"
            nodes.append({
                "branch": child,
                "depth": len(trajectory) + 1,
                "S_t": successor,
                "T_acc_t": list(successor_tacc),
                "T_acc_hash": sha256_value(successor_tacc),
                "T_real_t": action.identity,
                "S_parent": current,
                "T_acc_parent": list(current_tacc),
                "Delta_T_acc_from_parent": delta_tacc(current_tacc, successor_tacc),
                "baseline": {
                    "S_t": current,
                    "T_real_t": action.identity,
                    "S_t1": successor,
                },
            })
            frontier.append((
                child,
                successor,
                successor_tacc,
                trajectory + [action.identity],
            ))

    report = {
        "record_type": "TGCV_TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR2_RECONSTRUCTION",
        "status": "COMPLETED",
        "executor": "EXECUTOR_2",
        "independent": True,
        "source_repository": va["repository"],
        "source_revision": va["revision"],
        "source_blob_sha": va["blob_sha"],
        "problem": va["problem"],
        "depth": DEPTH,
        "node_count": len(nodes),
        "root_tacc": list(root_tacc),
        "nodes": nodes,
        "scientific_execution_authorized": authorized,
        "scientific_execution_performed": True,
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
