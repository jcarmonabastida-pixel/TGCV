#!/usr/bin/env python3
"""Independent deterministic executor for TGCV C09 Operational Bundle 001."""
import hashlib, json, sys
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


def s0(unit_id):
    return int(hashlib.sha256(unit_id.encode()).hexdigest()[:8], 16) % 10


def rng_key(seed, i):
    return hashlib.sha256(f"{seed}:{i}".encode()).digest()


def assignment():
    a = UNIT_IDS[:]
    # Deterministic Fisher-Yates. The exact integer conversion is part of the protocol.
    for i in range(len(a) - 1, 0, -1):
        j = int.from_bytes(rng_key(SEED, i)[:8], "big") % (i + 1)
        a[i], a[j] = a[j], a[i]
    return {uid: (0 if k < N // 2 else 1) for k, uid in enumerate(a)}


def t_acc(r1):
    return [u for u in U if TRANSFORMS[u]["requires"] in (None, "R1" if r1 else None)] if r1 else ["A", "C"]


def policy(tacc):
    return sorted(tacc, key=lambda u: (-TRANSFORMS[u]["score"], U.index(u)))[0]


def run(r1_by_arm):
    rows = []
    for uid in UNIT_IDS:
        z = ASSIGNMENT[uid]
        r1 = r1_by_arm[z]
        ta = t_acc(r1)
        chosen = policy(ta)
        y = s0(uid) + TRANSFORMS[chosen]["delta"]
        rows.append({"unit_id": uid, "Z": z, "S0": s0(uid), "T_acc": ta, "selected": chosen, "Y": y})
    return rows


def mean(xs):
    return sum(xs) / len(xs)


def main():
    global ASSIGNMENT
    ASSIGNMENT = assignment()
    assert list(ASSIGNMENT.values()).count(0) == 128
    assert list(ASSIGNMENT.values()).count(1) == 128
    assert t_acc(False) == ["A", "C"]
    assert t_acc(True) == ["A", "B", "C"]
    assert t_acc(False) != t_acc(True)

    primary = run({0: False, 1: True})
    null = run({0: False, 1: False})
    yt = [r["Y"] for r in primary if r["Z"] == 1]
    yc = [r["Y"] for r in primary if r["Z"] == 0]
    null_diff = mean([r["Y"] for r in null if r["Z"] == 1]) - mean([r["Y"] for r in null if r["Z"] == 0])
    result = {
        "bundle": "C09_OPERATIONAL_BUNDLE_001",
        "status": "PASS_PREANALYTIC_EXECUTION" if null_diff == 0 else "BLOCKED",
        "n_control": len(yc), "n_treatment": len(yt),
        "mean_control": mean(yc), "mean_treatment": mean(yt),
        "tau_hat": mean(yt) - mean(yc),
        "null_tau_hat": null_diff,
        "accessibility_control": t_acc(False),
        "accessibility_treatment": t_acc(True),
        "rows": primary,
    }
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("c09_execution_result.json")
    out.write_text(json.dumps(result, sort_keys=True, separators=(",", ":")), encoding="utf-8")
    print(json.dumps({k: result[k] for k in result if k != "rows"}, sort_keys=True))


if __name__ == "__main__":
    main()
