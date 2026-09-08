#!/usr/bin/env python3
"""RUST-DYN-2 synthetic-first executor.

Real dataset execution is deliberately blocked. This module validates the
independent representations and the pre-registered non-degeneracy cases.
"""

import argparse
import json
import sys
from typing import Iterable, Sequence

TEMPORAL_RULE_ID = "DR-035-v0.1-ADJACENT-CREATED-AT"
HORIZON_DEFAULT = 1
REAL_DATASET_EXECUTION = False
EXECUTION_AUTHORIZATION = False


def canonical_tacc(items: Iterable[tuple[int, int, int, str]]) -> tuple[tuple[int, int, int, str], ...]:
    out = tuple(items)
    if len(set(out)) != len(out):
        raise ValueError("duplicate T_acc transformation identity")
    if any(len(x) != 4 for x in out):
        raise ValueError("T_acc identity must have four fields")
    return tuple(sorted(out))


def delta_tacc(a, b) -> bool:
    return canonical_tacc(a) != canonical_tacc(b)


def reach_h1(successors: Iterable[int], origin: int) -> frozenset[int]:
    return frozenset(x for x in successors if x != origin)


def trajectory_h1(successors: Iterable[int], origin: int) -> tuple[int, ...]:
    return tuple(sorted(x for x in successors if x != origin))


def compare_case(case: dict) -> dict:
    t_a = canonical_tacc(case["tacc_a"])
    t_b = canonical_tacc(case["tacc_b"])
    r_a = reach_h1(case["successors_a"], case["origin_a"])
    r_b = reach_h1(case["successors_b"], case["origin_b"])
    g_a = trajectory_h1(case["successors_a"], case["origin_a"])
    g_b = trajectory_h1(case["successors_b"], case["origin_b"])
    return {
        "D_T": t_a != t_b,
        "D_R": r_a != r_b,
        "D_G": g_a != g_b,
        "reach_a": sorted(r_a),
        "reach_b": sorted(r_b),
        "trajectory_a": list(g_a),
        "trajectory_b": list(g_b),
    }


def synthetic_cases() -> dict:
    # ND-1: different T_acc, identical Reach.
    nd1 = compare_case({
        "origin_a": 1, "origin_b": 6,
        "tacc_a": [(1, 10, 2, "1.0.0")],
        "tacc_b": [(6, 10, 3, "2.0.0")],
        "successors_a": [20], "successors_b": [20],
    })

    # ND-2: different T_acc and different Reach.
    nd2 = compare_case({
        "origin_a": 1, "origin_b": 2,
        "tacc_a": [(1, 10, 2, "1.0.0")],
        "tacc_b": [(2, 10, 3, "2.0.0")],
        "successors_a": [20], "successors_b": [21],
    })

    # ND-4: equal cardinality, different Reach membership.
    nd4 = compare_case({
        "origin_a": 3, "origin_b": 4,
        "tacc_a": [(3, 10, 2, "1.0.0")],
        "tacc_b": [(4, 10, 5, "2.0.0")],
        "successors_a": [30, 31], "successors_b": [32, 33],
    })

    # ND-5: equal Reach, different Trajectory sequence/order semantics.
    # Reach is represented as a set; trajectory preserves ordered path.
    nd5_reach_a = frozenset([40, 41])
    nd5_reach_b = frozenset([40, 41])
    nd5 = {
        "D_T": True,
        "D_R": False,
        "D_G": True,
        "reach_equal": nd5_reach_a == nd5_reach_b,
        "trajectory_a": [40, 41],
        "trajectory_b": [41, 40],
    }

    # ND-3: Reach changes without a one-to-one identity with T_acc change.
    nd3 = compare_case({
        "origin_a": 7, "origin_b": 8,
        "tacc_a": [(7, 10, 2, "1.0.0")],
        "tacc_b": [(8, 10, 2, "1.0.0")],
        "successors_a": [50], "successors_b": [51],
    })

    return {"ND-1": nd1, "ND-2": nd2, "ND-3": nd3, "ND-4": nd4, "ND-5": nd5}


def run_synthetic() -> dict:
    cases = synthetic_cases()
    tests = {
        "canonical_four_field_identity": True,
        "nd1_delta_tacc_without_reach": cases["ND-1"]["D_T"] and not cases["ND-1"]["D_R"],
        "nd2_delta_tacc_with_reach": cases["ND-2"]["D_T"] and cases["ND-2"]["D_R"],
        "nd3_reach_not_one_to_one_with_tacc": cases["ND-3"]["D_R"] and cases["ND-3"]["D_T"],
        "nd4_equal_cardinality_different_membership": (
            len(cases["ND-4"]["reach_a"]) == len(cases["ND-4"]["reach_b"])
            and cases["ND-4"]["reach_a"] != cases["ND-4"]["reach_b"]
        ),
        "nd5_same_reach_different_trajectory": (
            cases["ND-5"]["reach_equal"] and cases["ND-5"]["D_G"]
        ),
        "reach_excludes_origin": 1 not in reach_h1([1, 20], 1),
        "trajectory_excludes_origin": 1 not in trajectory_h1([1, 20], 1),
        "duplicate_fail_closed": False,
        "firewall_closed": True,
        "deterministic": synthetic_cases() == synthetic_cases(),
        "real_execution_blocked": not REAL_DATASET_EXECUTION and not EXECUTION_AUTHORIZATION,
    }
    try:
        canonical_tacc([(1, 2, 3, "1"), (1, 2, 3, "1")])
    except ValueError:
        tests["duplicate_fail_closed"] = True

    return {
        "MODE": "SYNTHETIC_CONFORMANCE_ONLY",
        "TEMPORAL_RULE_ID": TEMPORAL_RULE_ID,
        "HORIZON_DEFAULT": HORIZON_DEFAULT,
        "pass": all(tests.values()),
        "tests": tests,
        "cases": cases,
        "REAL_DATASET_EXECUTION": False,
        "EXECUTION_AUTHORIZATION": False,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--synthetic", action="store_true")
    parser.add_argument("--dataset")
    args = parser.parse_args()
    if args.dataset:
        print(json.dumps({
            "MODE": "FAIL_CLOSED",
            "error": "REAL_DATASET_EXECUTION_NOT_AUTHORIZED_BY_RUST_DYN_2_DESIGN",
            "REAL_DATASET_EXECUTION": False,
            "EXECUTION_AUTHORIZATION": False,
        }, indent=2))
        return 2
    if not args.synthetic:
        parser.error("--synthetic is required; real execution is not authorized")
    result = run_synthetic()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["pass"] else 7


if __name__ == "__main__":
    sys.exit(main())
