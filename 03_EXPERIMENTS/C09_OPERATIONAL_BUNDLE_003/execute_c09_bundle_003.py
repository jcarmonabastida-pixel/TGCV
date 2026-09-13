#!/usr/bin/env python3
"""Deterministic Executor-1 implementation for TGCV C09 Operational Bundle 003.

Corrective successor to Bundle 002. The null is reported but is not an
exact-zero gate. Bundle integrity is authorized only when the three frozen
components match the SHA-256 values declared in HASH_MANIFEST.md.
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
EXPECTED_FILES = ("fixture.json", "EXECUTION_SPEC.md", "execute_c09_bundle_003.py")
EXPECTED_ROW_KEYS = {"unit_id", "Z", "S0", "T_acc", "selected", "Y"}


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


def t_acc(z):
    return ["A", "B", "C"] if z == 1 else ["A", "C"]


def policy(tacc):
    return sorted(tacc, key=lambda u: (-TRANSFORMS[u]["score"], U.index(u)))[0]


def transition(s0_value, selected):
    return s0_value + TRANSFORMS[selected]["delta"]


def endpoint(s1):
    return s1


def build_rows(accessibility_by_unit, assignment_map):
    rows = []
    for uid in UNIT_IDS:
        ta = accessibility_by_unit[uid]
        chosen = policy(ta)
        s0_value = s0(uid)
        rows.append({"unit_id": uid, "Z": assignment_map[uid], "S0": s0_value,
                     "T_acc": ta, "selected": chosen, "Y": endpoint(transition(s0_value, chosen))})
    return rows


def mean(xs):
    return sum(xs) / len(xs)


def actual_hashes(root):
    return {name: sha256_bytes((root / name).read_bytes()) for name in EXPECTED_FILES}


def manifest_hashes(root):
    manifest = (root / "HASH_MANIFEST.md").read_text(encoding="utf-8")
    hashes = {}
    for line in manifest.splitlines():
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        if len(parts) == 3 and parts[0] in EXPECTED_FILES:
            hashes[parts[0]] = parts[2]
    return hashes


def canonical_json(value):
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def integrity_checks(primary, null, assignment_map, root):
    checks = {}
    actual = actual_hashes(root)
    declared = manifest_hashes(root)
    checks["accessibility_exact"] = t_acc(0) == ["A", "C"] and t_acc(1) == ["A", "B", "C"] and t_acc(0) != t_acc(1)
    checks["assignment_balanced"] = len(assignment_map) == N and list(assignment_map.values()).count(0) == N // 2 and list(assignment_map.values()).count(1) == N // 2
    checks["baseline_definition_frozen"] = UNIT_IDS == [f"u-{i:04d}" for i in range(N)] and all(0 <= s0(uid) <= 9 for uid in UNIT_IDS) and C0 == {"capacity": 1, "policy_version": "C09-001"} and U == ["A", "B", "C"]
    checks["transition_and_scores_frozen"] = TRANSFORMS == {"A": {"delta": 1, "requires": None, "score": 1.0}, "B": {"delta": 3, "requires": "R1", "score": 2.0}, "C": {"delta": 0, "requires": None, "score": 0.5}}
    checks["policy_frozen"] = policy(["A", "C"]) == "A" and policy(["A", "B", "C"]) == "B"
    checks["treatment_flag_isolation"] = (
        policy(["A", "C"]) == policy(["A", "C"]) and
        transition(4, "A") == transition(4, "A") and
        endpoint(5) == 5 and
        policy(["A", "B", "C"]) == "B" and
        transition(4, "B") == 7 and
        endpoint(7) == 7
    )
    checks["null_no_accessibility_change"] = all(row["T_acc"] == ["A", "C"] and row["selected"] == "A" for row in null)
    checks["null_same_units_and_assignment"] = [(r["unit_id"], r["Z"], r["S0"]) for r in primary] == [(r["unit_id"], r["Z"], r["S0"]) for r in null]
    checks["canonical_output_schema"] = all(set(row.keys()) == EXPECTED_ROW_KEYS for row in primary + null)
    checks["bundle_sha256_matches_manifest"] = declared == actual and set(declared) == set(EXPECTED_FILES) and all(len(v) == 64 and all(c in "0123456789abcdef" for c in v.lower()) for v in declared.values())
    return checks, actual


def main():
    assignment_map = assignment()
    primary_accessibility = {uid: t_acc(assignment_map[uid]) for uid in UNIT_IDS}
    null_accessibility = {uid: t_acc(0) for uid in UNIT_IDS}
    primary = build_rows(primary_accessibility, assignment_map)
    null = build_rows(null_accessibility, assignment_map)
    root = Path(__file__).resolve().parent
    checks, hashes = integrity_checks(primary, null, assignment_map, root)
    yt = [r["Y"] for r in primary if r["Z"] == 1]
    yc = [r["Y"] for r in primary if r["Z"] == 0]
    ny_t = [r["Y"] for r in null if r["Z"] == 1]
    ny_c = [r["Y"] for r in null if r["Z"] == 0]
    null_diff = mean(ny_t) - mean(ny_c)
    result = {
        "bundle": "C09_OPERATIONAL_BUNDLE_003",
        "status": "PASS_PREANALYTIC_EXECUTION" if all(checks.values()) else "BLOCKED",
        "runtime_fingerprint": {"python": sys.version, "platform": platform.platform(), "implementation": platform.python_implementation()},
        "bundle_sha256": hashes,
        "integrity_checks": checks,
        "n_control": len(yc), "n_treatment": len(yt),
        "mean_control": mean(yc), "mean_treatment": mean(yt),
        "tau_hat": mean(yt) - mean(yc), "null_tau_hat": null_diff,
        "accessibility_control": t_acc(0), "accessibility_treatment": t_acc(1),
        "rows": primary,
    }
    output_text = canonical_json(result)
    if json.loads(output_text) != result or canonical_json(json.loads(output_text)) != output_text:
        raise RuntimeError("BLOCKED: canonical JSON serialization check failed")
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else root / "c09_execution_result.json"
    out.write_text(output_text, encoding="utf-8")
    print(canonical_json({k: result[k] for k in result if k != "rows"}))


if __name__ == "__main__":
    main()
