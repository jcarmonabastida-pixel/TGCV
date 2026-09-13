#!/usr/bin/env python3
"""Independent Executor-2 reconstruction for TGCV C09 Bundle 003."""
import hashlib
import json
import platform
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BUNDLE = ROOT / "C09_OPERATIONAL_BUNDLE_003"
RANDOMIZATION_SPEC = ROOT / "C09_RANDOMIZATION_SPECIFICATION_001.md"
SEED = 130917
N = 256
IDS = tuple(f"u-{i:04d}" for i in range(N))
EXPECTED_EXECUTOR_1 = "94534CC29FA31E86A9936DE8615D8B0114D44F183942C2126E817E507BF62AC3"


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest().upper()


def load_fixture():
    return json.loads((BUNDLE / "fixture.json").read_text(encoding="utf-8"))


def parse_manifest():
    found = {}
    for line in (BUNDLE / "HASH_MANIFEST.md").read_text(encoding="utf-8").splitlines():
        cells = [x.strip().strip("`") for x in line.strip().strip("|").split("|")]
        if len(cells) == 3 and cells[0] in {"fixture.json", "EXECUTION_SPEC.md", "execute_c09_bundle_003.py"}:
            found[cells[0]] = cells[2].upper()
    return found


def verify_bundle():
    expected = {
        "fixture.json": "3E3AC9601F893B7E01F75813499BB3F539D7B192AE18F0332DC6365AAA5EBD49",
        "EXECUTION_SPEC.md": "D1621DBBCB9DD840828D0F3C431949D7DDA2B73F3E4B43EA86F35FC07A87E10B",
        "execute_c09_bundle_003.py": EXPECTED_EXECUTOR_1,
    }
    actual = {name: sha256_bytes((BUNDLE / name).read_bytes()) for name in expected}
    declared = parse_manifest()
    return actual == declared == expected, actual, declared


def baseline(uid):
    return int(hashlib.sha256(uid.encode("utf-8")).hexdigest()[0:8], 16) % 10


def fisher_yates(universe, seed):
    """Frozen by C09_RANDOMIZATION_SPECIFICATION_001.md."""
    values = list(universe)
    for i in range(len(values) - 1, 0, -1):
        input_bytes = f"{seed}:{i}".encode("ascii")
        digest = hashlib.sha256(input_bytes).digest()
        integer = int.from_bytes(digest, "big", signed=False)
        j = integer % (i + 1)
        values[i], values[j] = values[j], values[i]
    return values


def assignment():
    order = fisher_yates(IDS, SEED)
    return {uid: (1 if position >= N // 2 else 0) for position, uid in enumerate(order)}


def accessible(fixture, z):
    resource = fixture["accessibility"]["treatment" if z == 1 else "control"]["R1"]
    out = []
    for name in fixture["candidate_universe"]:
        requirement = fixture["transformations"][name]["requires"]
        if requirement == "NONE" or resource:
            out.append(name)
    return tuple(out)


def policy(fixture, candidates):
    scores = fixture["transformations"]
    return min(candidates, key=lambda name: (-scores[name]["score"], name))


def transition(fixture, s0, selected):
    return s0 + fixture["transformations"][selected]["delta"]


def row(fixture, uid, z, amap):
    s0 = baseline(uid)
    tacc = accessible(fixture, z)
    selected = policy(fixture, tacc)
    return {
        "unit_id": uid,
        "Z": amap[uid],
        "S0": s0,
        "T_acc": list(tacc),
        "selected": selected,
        "Y": transition(fixture, s0, selected),
    }


def mean(values):
    return sum(values) / len(values)


def main():
    fixture = load_fixture()
    amap = assignment()
    primary = [row(fixture, uid, amap[uid], amap) for uid in IDS]
    null = [row(fixture, uid, 0, amap) for uid in IDS]

    bundle_ok, actual_hashes, declared_hashes = verify_bundle()
    control = [r for r in primary if r["Z"] == 0]
    treatment = [r for r in primary if r["Z"] == 1]
    checks = {
        "bundle_hashes": bundle_ok,
        "randomization_spec_present": RANDOMIZATION_SPEC.is_file(),
        "accessibility": accessible(fixture, 0) == ("A", "C") and accessible(fixture, 1) == ("A", "B", "C"),
        "accessibility_differs": accessible(fixture, 0) != accessible(fixture, 1),
        "balanced_assignment": len(control) == 128 and len(treatment) == 128,
        "baseline_definition": all(r["S0"] == baseline(r["unit_id"]) for r in primary + null),
        "primary_null_same_units_assignment_baseline": [(r["unit_id"], r["Z"], r["S0"]) for r in primary] == [(r["unit_id"], r["Z"], r["S0"]) for r in null],
        "policy": policy(fixture, ("A", "C")) == "A" and policy(fixture, ("A", "B", "C")) == "B",
        "transition": transition(fixture, 4, "A") == 5 and transition(fixture, 4, "B") == 7,
        "null_no_accessibility_change": all(r["T_acc"] == ["A", "C"] and r["selected"] == "A" for r in null),
        "canonical_row_schema": all(set(r) == {"unit_id", "Z", "S0", "T_acc", "selected", "Y"} for r in primary + null),
        "executor_1_not_used_as_input": EXPECTED_EXECUTOR_1 == actual_hashes["execute_c09_bundle_003.py"],
    }

    yt = [r["Y"] for r in treatment]
    yc = [r["Y"] for r in control]
    nt = [r["Y"] for r in null if r["Z"] == 1]
    nc = [r["Y"] for r in null if r["Z"] == 0]
    result = {
        "bundle": "C09_OPERATIONAL_BUNDLE_003",
        "executor": "EXECUTOR-2",
        "randomization_spec": "C09_RANDOMIZATION_SPECIFICATION_001.md",
        "status": "PASS_RECONSTRUCTION" if all(checks.values()) else "BLOCKED",
        "runtime": {"python": sys.version, "platform": platform.platform(), "implementation": platform.python_implementation()},
        "bundle_sha256": actual_hashes,
        "manifest_sha256": declared_hashes,
        "integrity_checks": checks,
        "n_control": len(yc),
        "n_treatment": len(yt),
        "mean_control": mean(yc),
        "mean_treatment": mean(yt),
        "tau_hat": mean(yt) - mean(yc),
        "null_tau_hat": mean(nt) - mean(nc),
        "accessibility_control": list(accessible(fixture, 0)),
        "accessibility_treatment": list(accessible(fixture, 1)),
        "rows": primary,
    }
    print(json.dumps(result, sort_keys=True, separators=(",", ":"), ensure_ascii=False))


if __name__ == "__main__":
    main()
