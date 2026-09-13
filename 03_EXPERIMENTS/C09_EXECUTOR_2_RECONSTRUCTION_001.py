#!/usr/bin/env python3
"""Independent Executor-2 reconstruction for TGCV C09 Bundle 003.

This implementation is deliberately separate from Executor-1. It reconstructs
only the frozen experimental definitions and writes no Bundle-003 files.
"""
import hashlib
import json
import platform
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUNDLE = ROOT / "C09_OPERATIONAL_BUNDLE_003"
SEED = 130917
N = 256
IDS = tuple(f"u-{i:04d}" for i in range(N))
TRANSFORM = {
    "A": (1, None, 1.0),
    "B": (3, "R1", 2.0),
    "C": (0, None, 0.5),
}
EXPECTED = {
    "fixture.json": "3E3AC9601F893B7E01F75813499BB3F539D7B192AE18F0332DC6365AAA5EBD49",
    "EXECUTION_SPEC.md": "D1621DBBCB9DD840828D0F3C431949D7DDA2B73F3E4B43EA86F35FC07A87E10B",
    "execute_c09_bundle_003.py": "94534CC29FA31E86A9936DE8615D8B0114D44F183942C2126E817E507BF62AC3",
}


def digest(data):
    return hashlib.sha256(data).hexdigest().upper()


def state0(uid):
    return int(hashlib.sha256(uid.encode()).hexdigest()[0:8], 16) % 10


def permute(values):
    values = list(values)
    for i in range(len(values) - 1, 0, -1):
        raw = hashlib.sha256(f"{SEED}:{i}".encode()).digest()
        j = int.from_bytes(raw[:8], "big") % (i + 1)
        values[i], values[j] = values[j], values[i]
    return values


def assignment_map():
    shuffled = permute(IDS)
    return {uid: int(position >= N // 2) for position, uid in enumerate(shuffled)}


def accessible(has_r1):
    return ("A", "B", "C") if has_r1 else ("A", "C")


def choose(candidates):
    return min(candidates, key=lambda name: (-TRANSFORM[name][2], name))


def final_state(initial, chosen):
    return initial + TRANSFORM[chosen][0]


def declared_hashes():
    lines = (BUNDLE / "HASH_MANIFEST.md").read_text(encoding="utf-8").splitlines()
    found = {}
    for line in lines:
        cells = [x.strip().strip("`") for x in line.strip().strip("|").split("|")]
        if len(cells) == 3 and cells[0] in EXPECTED:
            found[cells[0]] = cells[2].upper()
    return found


def integrity_hashes():
    actual = {name: digest((BUNDLE / name).read_bytes()) for name in EXPECTED}
    declared = declared_hashes()
    return actual, declared, actual == declared == EXPECTED


def build(z, amap):
    has_r1 = z == 1
    acc = accessible(has_r1)
    result = []
    for uid in IDS:
        s = state0(uid)
        chosen = choose(acc)
        result.append({"unit_id": uid, "Z": amap[uid], "S0": s,
                       "T_acc": list(acc), "selected": chosen,
                       "Y": final_state(s, chosen)})
    return result


def mean(values):
    return sum(values) / len(values)


def main():
    amap = assignment_map()
    primary = build(None, amap)  # assignment Z is metadata; accessibility is evaluated separately below
    for row in primary:
        z = row["Z"]
        acc = accessible(z == 1)
        row["T_acc"] = list(acc)
        row["selected"] = choose(acc)
        row["Y"] = final_state(row["S0"], row["selected"])
    null = build(0, amap)

    actual, declared, hashes_ok = integrity_hashes()
    checks = {
        "bundle_hashes": hashes_ok,
        "accessibility": accessible(False) == ("A", "C") and accessible(True) == ("A", "B", "C"),
        "balanced_assignment": len(amap) == N and sum(v == 0 for v in amap.values()) == 128 and sum(v == 1 for v in amap.values()) == 128,
        "baseline": all(0 <= state0(uid) <= 9 for uid in IDS),
        "policy": choose(("A", "C")) == "A" and choose(("A", "B", "C")) == "B",
        "transition": final_state(4, "A") == 5 and final_state(4, "B") == 7,
        "null_accessibility": all(row["T_acc"] == ["A", "C"] and row["selected"] == "A" for row in null),
        "null_same_baseline": [(r["unit_id"], r["Z"], r["S0"]) for r in primary] == [(r["unit_id"], r["Z"], r["S0"]) for r in null],
        "row_schema": all(set(r) == {"unit_id", "Z", "S0", "T_acc", "selected", "Y"} for r in primary + null),
    }
    yt = [r["Y"] for r in primary if r["Z"] == 1]
    yc = [r["Y"] for r in primary if r["Z"] == 0]
    nt = [r["Y"] for r in null if r["Z"] == 1]
    nc = [r["Y"] for r in null if r["Z"] == 0]
    result = {
        "bundle": "C09_OPERATIONAL_BUNDLE_003",
        "executor": "EXECUTOR-2",
        "status": "PASS_RECONSTRUCTION" if all(checks.values()) else "BLOCKED",
        "runtime": {"python": sys.version, "platform": platform.platform(), "implementation": platform.python_implementation()},
        "bundle_sha256": actual,
        "integrity_checks": checks,
        "n_control": len(yc), "n_treatment": len(yt),
        "mean_control": mean(yc), "mean_treatment": mean(yt),
        "tau_hat": mean(yt) - mean(yc),
        "null_tau_hat": mean(nt) - mean(nc),
        "accessibility_control": list(accessible(False)),
        "accessibility_treatment": list(accessible(True)),
        "rows": primary,
    }
    text = json.dumps(result, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    print(text)


if __name__ == "__main__":
    main()
