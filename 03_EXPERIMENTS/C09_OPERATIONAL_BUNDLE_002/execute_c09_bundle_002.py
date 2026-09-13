#!/usr/bin/env python3
"""Deterministic Executor-1 implementation for TGCV C09 Operational Bundle 002.

Corrective version of Bundle 001: the predeclared null is reported as a
measurement/control check and is not used as an exact-zero authorization gate.
"""
import hashlib
import json
import platform
import sys
from pathlib import Path

SEED = 130917
N = 256
UNIT_IDS = [f"u-{i:04d}" for i in range(N)]
U = ["A", "B", "C"]
TRANSFORMS = {
    "A": {"delta": 1, "requires": None, "score": 1.0},
    "B": {"delta": 3, "requires": "R1", "score": 2.0},
    "C": {"delta": 0, "requires": None, "score": 0.5},
}
C0 = {"capacity": 1, "policy_version": "C09-001"}


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def s0(unit_id):
    return int(hashlib.sha256(unit_id.encode()).hexdigest()[:8], 16) % 10


def rng_key(seed, i):
    return hashlib.sha256(f"{seed}:{i}".encode()).digest()


def assignment():
    a = UNIT_IDS[:]
    for i in range(len(a) - 1, 0, -1):
        j = int.from_bytes(rng_key(SEED, i)[:8], "big") % (i + 1)
        a[i], a[j] = a[j], a[i]
    return {uid: (0 if k < N // 2 else 1) for k, uid in enumerate(a)}


def t_acc(r1):
    return ["A", "B", "C"] if r1 else ["A", "C"]


def policy(tacc):
    return sorted(tacc, key=lambda u: (-TRANSFORMS[u]["score"], U.index(u)))[0]


def run(r1_by_arm):
    rows = []
    for uid in UNIT_IDS:
        z = ASSIGNMENT[uid]
        ta = t_acc(r1_by_arm[z])
        chosen = policy(ta)
        rows.append({
            "unit_id": uid,
            "Z": z,
            "S0": s0(uid),
            "T_acc": ta,
            "selected": chosen,
            "Y": s0(uid) + TRANSFORMS[chosen]["delta"],
        })
    return rows


def mean(xs):
    return sum(xs) / len(xs)


def bundle_hashes(root):
    names = ["fixture.json", "EXECUTION_SPEC.md", "execute_c09_bundle_002.py"]
    return {name: sha256_bytes((root / name).read_bytes()) for name in names}


def integrity_checks(primary, null, assignment_map):
    expected_keys = {"unit_id", "Z", "S0", "T_acc", "selected", "Y"}
    checks = {}

    checks["accessibility_exact"] = (
        t_acc(False) == ["A", "C"]
        and t_acc(True) == ["A", "B", "C"]
        and t_acc(False) != t_acc(True)
    )
    checks["assignment_balanced"] = (
        len(assignment_map) == N
        and list(assignment_map.values()).count(0) == N // 2
        and list(assignment_map.values()).count(1) == N // 2
    )
    checks["baseline_definition_frozen"] = (
        UNIT_IDS == [f"u-{i:04d}" for i in range(N)]
        and all(0 <= s0(uid) <= 9 for uid in UNIT_IDS)
        and C0 == {"capacity": 1, "policy_version": "C09-001"}
        and U == ["A", "B", "C"]
    )
    checks["transition_and_scores_frozen"] = (
        TRANSFORMS == {
            "A": {"delta": 1, "requires": None, "score": 1.0},
            "B": {"delta": 3, "requires": "R1", "score": 2.0},
            "C": {"delta": 0, "requires": None, "score": 0.5},
        }
    )
    checks["policy_frozen"] = (
        policy(["A", "C"]) == "A"
        and policy(["A", "B", "C"]) == "B"
    )
    checks["null_no_accessibility_change"] = all(
        row["T_acc"] == ["A", "C"] and row["selected"] == "A"
        for row in null
    )
    checks["null_same_units_and_assignment"] = (
        [(r["unit_id"], r["Z"], r["S0"]) for r in primary]
        == [(r["unit_id"], r["Z"], r["S0"]) for r in null]
    )
    checks["canonical_output_schema"] = all(
        set(row.keys()) == expected_keys for row in primary + null
    )
    return checks


def main():
    global ASSIGNMENT
    root = Path(__file__).resolve().parent
    ASSIGNMENT = assignment()

    primary = run({0: False, 1: True})
    null = run({0: False, 1: False})
    checks = integrity_checks(primary, null, ASSIGNMENT)

    yt = [r["Y"] for r in primary if r["Z"] == 1]
    yc = [r["Y"] for r in primary if r["Z"] == 0]
    ny_t = [r["Y"] for r in null if r["Z"] == 1]
    ny_c = [r["Y"] for r in null if r["Z"] == 0]
    null_diff = mean(ny_t) - mean(ny_c)

    result = {
        "bundle": "C09_OPERATIONAL_BUNDLE_002",
        "status": "PASS_PREANALYTIC_EXECUTION" if all(checks.values()) else "BLOCKED",
        "runtime_fingerprint": {
            "python": sys.version,
            "platform": platform.platform(),
            "implementation": platform.python_implementation(),
        },
        "bundle_sha256": bundle_hashes(root),
        "integrity_checks": checks,
        "n_control": len(yc),
        "n_treatment": len(yt),
        "mean_control": mean(yc),
        "mean_treatment": mean(yt),
        "tau_hat": mean(yt) - mean(yc),
        "null_tau_hat": null_diff,
        "accessibility_control": t_acc(False),
        "accessibility_treatment": t_acc(True),
        "rows": primary,
    }
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "c09_execution_result.json"
    out.write_text(json.dumps(result, sort_keys=True, separators=(",", ":")), encoding="utf-8")
    print(json.dumps({k: result[k] for k in result if k != "rows"}, sort_keys=True))


if __name__ == "__main__":
    main()
