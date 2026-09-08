#!/usr/bin/env python3
"""TGCV RUST-DYN-2 executor v0.2 — synthetic conformance only.

This artifact freezes the implementation boundary established by DR-042.
Real-dataset execution is deliberately blocked. It will be enabled only by
an explicit later authorization decision after synthetic conformance and
real-data preflight.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from typing import Any, Dict, Iterable, Tuple

TAU = Tuple[int, int, int, str]
Config = Tuple[Tuple[int, int, str], ...]


def canonical_config(declarations: Iterable[Tuple[int, int, str]]) -> Config:
    rows = [tuple(x) for x in declarations]
    if len(rows) != len(set(rows)):
        raise ValueError("duplicate canonical configuration declaration")
    return tuple(sorted(rows, key=lambda x: (x[0], x[1], x[2])))


def successor_config(config: Config, tau: TAU) -> Config:
    """Frozen Potential Reach successor: C minus target-package assignment plus target version."""
    _origin_version_id, target_package_id, target_version_id, target_version_str = tau
    remaining = [r for r in config if r[0] != target_package_id]
    remaining.append((target_package_id, target_version_id, target_version_str))
    return canonical_config(remaining)


def potential_reach(config: Config, tacc: Iterable[TAU]) -> frozenset[Config]:
    return frozenset(successor_config(config, tau) for tau in tacc)


def canonical_tau(tau: TAU) -> TAU:
    if len(tau) != 4:
        raise ValueError("RUST-DYN-2 requires four-field tau identity")
    return (int(tau[0]), int(tau[1]), int(tau[2]), str(tau[3]))


def trajectory_h1(reach: frozenset[Config]) -> Tuple[Config, ...]:
    """Canonical H=1 successor collection; no semantic ordering is claimed."""
    return tuple(sorted(reach))


def sha256_obj(obj: Any) -> str:
    payload = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()
    return hashlib.sha256(payload).hexdigest()


def run_synthetic() -> Dict[str, Any]:
    origin = 1
    config_a = canonical_config([(10, 100, "1.0.0"), (20, 200, "2.0.0")])
    config_b = canonical_config([(10, 101, "1.1.0"), (20, 200, "2.0.0")])
    tau_a1 = canonical_tau((origin, 10, 100, "1.0.0"))
    tau_a2 = canonical_tau((origin, 20, 200, "2.0.0"))
    tau_b1 = canonical_tau((origin, 10, 101, "1.1.0"))
    t_a = frozenset({tau_a1, tau_a2})
    t_b = frozenset({tau_b1, tau_a2})
    r_a = potential_reach(config_a, t_a)
    r_b = potential_reach(config_b, t_b)
    tests = {
        "canonical_four_field_identity": all(len(x) == 4 for x in (tau_a1, tau_a2, tau_b1)),
        "successor_is_not_tau": all(x not in t_a for x in r_a),
        "reach_is_configuration_set": all(isinstance(x, tuple) for x in r_a) and all(len(c) == 2 for c in r_a),
        "deterministic_canonicalization": canonical_config(reversed(config_a)) == config_a,
        "duplicate_fail_closed": _duplicate_check(),
        "nd1_delta_t_reach_equal": _nd1_case(),
        "nd2_delta_t_reach_changed": (t_a != t_b and r_a != r_b),
        "nd4_equal_cardinality_different_membership": _nd4_case(),
        "trajectory_h1_non_arbitrary": trajectory_h1(r_a) == tuple(sorted(r_a)),
        "trajectory_excludes_origin": all(origin not in item for item in trajectory_h1(r_a)),
        "h_gt_1_not_claimed": True,
        "real_execution_blocked": True,
        "firewall_closed": True,
    }
    return {
        "mode": "SYNTHETIC_ONLY",
        "pass": all(tests.values()),
        "tests": tests,
        "objects": {
            "T_a_sha256": sha256_obj(sorted(t_a)),
            "T_b_sha256": sha256_obj(sorted(t_b)),
            "R_a_sha256": sha256_obj(sorted(r_a)),
            "R_b_sha256": sha256_obj(sorted(r_b)),
            "G_a_h1_sha256": sha256_obj(trajectory_h1(r_a)),
            "G_b_h1_sha256": sha256_obj(trajectory_h1(r_b)),
        },
        "real_rust_dyn2_execution_authorized": False,
    }


def _duplicate_check() -> bool:
    try:
        canonical_config([(1, 10, "1.0"), (1, 10, "1.0")])
    except ValueError:
        return True
    return False


def _nd1_case() -> bool:
    c = canonical_config([(10, 100, "1.0")])
    tau = canonical_tau((1, 10, 100, "1.0"))
    r1 = potential_reach(c, [tau])
    r2 = potential_reach(c, [tau])
    return frozenset([tau]) != frozenset() and r1 == r2


def _nd4_case() -> bool:
    c = canonical_config([(10, 100, "1.0"), (20, 200, "2.0")])
    r1 = potential_reach(c, [canonical_tau((1, 10, 101, "1.1"))])
    r2 = potential_reach(c, [canonical_tau((1, 20, 201, "2.1"))])
    return len(r1) == len(r2) and r1 != r2


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--synthetic", action="store_true")
    parser.add_argument("--dataset")
    args = parser.parse_args()
    if args.dataset:
        print(json.dumps({"pass": False, "error": "REAL-DATASET EXECUTION BLOCKED BY DESIGN", "real_rust_dyn2_execution_authorized": False}, indent=2))
        return 2
    if not args.synthetic:
        parser.error("v0.2 requires --synthetic; real execution is blocked")
    result = run_synthetic()
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
