#!/usr/bin/env python3
"""RUST-DYN deterministic downstream engine v0.2.

Synthetic-first implementation of the frozen RUST-DYN-1 semantics with the
RUST-DYN-STATE-1 normalization: Reach and Trajectory exclude the initial
origin identity from comparative downstream representations.

No dataset loading, outcome access, sampling, or predictive path exists here.
A real-data adapter requires a later execution-authorization gate.
"""
from __future__ import annotations

import argparse
import json
from typing import Iterable

Tau = tuple[int, int, int, str]
TAccMap = dict[int, tuple[Tau, ...]]


def canonical_tacc(rows: Iterable[Tau]) -> tuple[Tau, ...]:
    materialized = list(rows)
    ordered = sorted(materialized, key=lambda r: (r[0], r[1], r[2], r[3]))
    if any(a == b for a, b in zip(ordered, ordered[1:])):
        raise ValueError("DUPLICATE_TACC_TRANSFORMATION")
    return tuple(ordered)


def delta_tacc(t0: Iterable[Tau], t1: Iterable[Tau]) -> dict:
    a, b = set(canonical_tacc(t0)), set(canonical_tacc(t1))
    return {
        "changed": a != b,
        "expansion": sorted(b - a),
        "contraction": sorted(a - b),
        "persistent": sorted(a & b),
        "classification": (
            "PERSISTENCE" if a == b else
            "EXPANSION" if a < b else
            "CONTRACTION" if b < a else
            "RECONFIGURATION"
        ),
    }


def _successors(origin_id: int, tacc_by_origin: TAccMap) -> tuple[int, ...]:
    rows = canonical_tacc(tacc_by_origin.get(origin_id, ()))
    return tuple(sorted({tau[2] for tau in rows}))


def reach_h(origin_id: int, tacc_by_origin: TAccMap, horizon: int) -> tuple[int, ...]:
    """Finite-horizon successor set, excluding the initial origin node."""
    if horizon < 0:
        raise ValueError("NEGATIVE_HORIZON")
    seen = {origin_id}
    frontier = {origin_id}
    reached = set()
    for _ in range(horizon):
        nxt = set()
        for node in sorted(frontier):
            nxt.update(_successors(node, tacc_by_origin))
        nxt -= seen
        reached.update(nxt)
        seen.update(nxt)
        frontier = nxt
        if not frontier:
            break
    return tuple(sorted(reached))


def trajectories_h(origin_id: int, tacc_by_origin: TAccMap, horizon: int) -> tuple[tuple[int, ...], ...]:
    """Finite-horizon ordered successor sequences, excluding the origin."""
    if horizon < 0:
        raise ValueError("NEGATIVE_HORIZON")
    paths: list[tuple[int, ...]] = [()]
    for _ in range(horizon):
        expanded: list[tuple[int, ...]] = []
        for path in paths:
            node = origin_id if not path else path[-1]
            successors = _successors(node, tacc_by_origin)
            if not successors:
                expanded.append(path)
            else:
                for nxt in successors:
                    expanded.append(path + (nxt,))
        paths = sorted(set(expanded))
        if not paths or all(not p for p in paths):
            break
    return tuple(paths)


def classify_temporal_pair(origin_a: int, origin_b: int, tacc_by_origin: TAccMap, horizon: int) -> dict:
    t0 = canonical_tacc(tacc_by_origin.get(origin_a, ()))
    t1 = canonical_tacc(tacc_by_origin.get(origin_b, ()))
    d = delta_tacc(t0, t1)
    r0, r1 = reach_h(origin_a, tacc_by_origin, horizon), reach_h(origin_b, tacc_by_origin, horizon)
    tr0, tr1 = trajectories_h(origin_a, tacc_by_origin, horizon), trajectories_h(origin_b, tacc_by_origin, horizon)
    return {"origin_a": origin_a, "origin_b": origin_b, "horizon": horizon, "delta_tacc": d,
            "reach_equal": r0 == r1, "reach_a": r0, "reach_b": r1,
            "trajectory_equal": tr0 == tr1, "trajectory_a": tr0, "trajectory_b": tr1,
            "outcome_read": False, "future_activity_read": False, "sampling": False, "predictive_metrics": False}


def synthetic_conformance() -> dict:
    tau12 = (1, 10, 2, "1.0.0")
    tau13 = (1, 10, 3, "1.1.0")
    tau62 = (6, 10, 2, "1.0.0")
    tau24 = (2, 20, 4, "1.0.0")
    tau34 = (3, 20, 4, "1.0.0")
    tau35 = (3, 20, 5, "1.1.0")
    tau45 = (4, 20, 5, "1.1.0")
    graph = {1: (tau12,), 2: (tau24,), 3: (tau34, tau35), 4: (tau45,), 5: (), 6: (tau62,)}
    tests: dict[str, bool] = {}
    tests["delta_reconfiguration_equal_cardinality"] = delta_tacc((tau12,), (tau13,))["classification"] == "RECONFIGURATION"
    tests["delta_persistence"] = delta_tacc((tau12,), (tau12,))["classification"] == "PERSISTENCE"
    tests["reach_excludes_origin"] = reach_h(1, graph, 1) == (2,)
    pair = classify_temporal_pair(1, 6, graph, 1)
    tests["pair_reports_delta"] = pair["delta_tacc"]["changed"]
    tests["origin_difference_does_not_force_reach_difference"] = pair["reach_equal"]
    tests["trajectory_excludes_origin"] = trajectories_h(1, graph, 1) == ((2,),)
    tests["trajectory_deterministic"] = trajectories_h(1, graph, 1) == trajectories_h(1, graph, 1)
    tests["firewall_closed"] = not pair["outcome_read"] and not pair["future_activity_read"] and not pair["sampling"] and not pair["predictive_metrics"]
    repeat = classify_temporal_pair(1, 6, graph, 1)
    tests["repeatable"] = pair == repeat
    try:
        canonical_tacc((tau12, tau12))
        tests["duplicate_fail_closed"] = False
    except ValueError:
        tests["duplicate_fail_closed"] = True
    try:
        reach_h(1, graph, -1)
        tests["negative_horizon_fail_closed"] = False
    except ValueError:
        tests["negative_horizon_fail_closed"] = True
    return {"MODE": "SYNTHETIC_CONFORMANCE_ONLY", "tests": tests, "pass": all(tests.values())}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--horizon", type=int, default=1)
    parser.add_argument("--dataset", default=None, help="Reserved; real execution is not implemented/authorized.")
    args = parser.parse_args()
    if args.dataset is not None:
        print(json.dumps({"ERROR": "REAL_DATASET_EXECUTION_NOT_IMPLEMENTED", "EXECUTION_AUTHORIZATION": False}, indent=2))
        return 3
    result = synthetic_conformance()
    result["horizon_default"] = args.horizon
    print(json.dumps(result, indent=2, sort_keys=True))
    print("REAL_DATASET_EXECUTION: False")
    print("EXECUTION_AUTHORIZATION: False")
    return 0 if result["pass"] else 6


if __name__ == "__main__":
    raise SystemExit(main())
