#!/usr/bin/env python3
"""RUST-DYN-2 temporal population reconciliation audit v0.1.

Compares the historical temporal population (created_at, id ordering) with
current DR-035 (created_at ordering, exact timestamp ties excluded).
No T_acc, Reach, Trajectory, outcome, value, prediction, or experiment execution.
"""
from __future__ import annotations
import argparse, csv, hashlib, io, json, zipfile
from collections import defaultdict
from pathlib import Path

EXPECTED_SHA256 = "823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224"
VERSIONS_MEMBER = "rust_repos_2022_09_07/dumps/postgresql/data/package_versions.csv"
TEMPORAL_RULE_ID = "DR-035-v0.1-ADJACENT-CREATED-AT"
HISTORICAL_RULE_ID = "HISTORICAL-v0.1-CREATED-AT-ID"

def sha256_file(p: Path) -> str:
    h = hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda: f.read(1024 * 1024), b""):
            h.update(b)
    return h.hexdigest()

def canon_pair(a: str, b: str) -> tuple[str, str]:
    return (a, b)

def set_hash(xs: set[tuple[str, str]]) -> str:
    payload = [[a, b] for a, b in sorted(xs)]
    return hashlib.sha256(json.dumps(payload, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()

def load_versions(p: Path):
    with zipfile.ZipFile(p) as z:
        names = [n.replace("\\", "/") for n in z.namelist()]
        if VERSIONS_MEMBER not in names:
            raise RuntimeError("FROZEN_MEMBER_MISSING:" + VERSIONS_MEMBER)
        with z.open(VERSIONS_MEMBER, "r") as raw:
            rows = list(csv.DictReader(io.TextIOWrapper(raw, encoding="utf-8", errors="strict", newline="")))
    expected = {"id", "package_id", "version_str", "created_at"}
    if set(rows[0]) != expected if rows else True:
        raise RuntimeError("PACKAGE_VERSIONS_SCHEMA_ERROR")
    return rows

def historical_pairs(rows):
    by_pkg = defaultdict(list)
    for r in rows:
        by_pkg[r["package_id"]].append(r)
    out = set()
    tie_origin_count = 0
    affected_packages = set()
    for pkg, arr in by_pkg.items():
        arr.sort(key=lambda r: (r["created_at"], r["id"]))
        for i in range(len(arr) - 1):
            a, b = arr[i], arr[i + 1]
            out.add(canon_pair(a["id"], b["id"]))
        # Historical implementation did not exclude ties; count origins in tied groups.
        by_time = defaultdict(list)
        for r in arr:
            by_time[r["created_at"]].append(r)
        for ts, group in by_time.items():
            if len(group) > 1:
                tie_origin_count += len(group)
                affected_packages.add(pkg)
    return out, tie_origin_count, affected_packages

def dr035_pairs(rows):
    by_pkg = defaultdict(list)
    for r in rows:
        by_pkg[r["package_id"]].append(r)
    out = set()
    tie_origin_count = 0
    excluded_origin_count = 0
    affected_packages = set()
    for pkg, arr in by_pkg.items():
        by_time = defaultdict(list)
        for r in arr:
            by_time[r["created_at"]].append(r)
        clean = []
        for ts, group in by_time.items():
            if len(group) == 1:
                clean.append(group[0])
            else:
                tie_origin_count += len(group)
                excluded_origin_count += len(group)
                affected_packages.add(pkg)
        clean.sort(key=lambda r: r["created_at"])
        for i in range(len(clean) - 1):
            out.add(canon_pair(clean[i]["id"], clean[i + 1]["id"]))
    return out, tie_origin_count, excluded_origin_count, affected_packages

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dataset", required=True)
    ap.add_argument("--output", required=True)
    args = ap.parse_args()
    p = Path(args.dataset)
    actual = sha256_file(p)
    if actual != EXPECTED_SHA256:
        raise RuntimeError(f"DATASET_SHA256_MISMATCH:{actual}")
    rows = load_versions(p)
    hist, hist_ties, hist_affected = historical_pairs(rows)
    cur, cur_ties, cur_excluded, cur_affected = dr035_pairs(rows)
    inter = hist & cur
    hist_only = hist - cur
    cur_only = cur - hist
    result = {
        "MODE": "TEMPORAL_POPULATION_RECONCILIATION_ONLY",
        "pass": True,
        "dataset_sha256": actual,
        "historical_rule_id": HISTORICAL_RULE_ID,
        "current_rule_id": TEMPORAL_RULE_ID,
        "row_count_package_versions": len(rows),
        "historical": {
            "pair_count": len(hist),
            "timestamp_tie_origin_count": hist_ties,
            "affected_package_count": len(hist_affected),
            "pair_set_sha256": set_hash(hist),
        },
        "dr035": {
            "pair_count": len(cur),
            "timestamp_tie_origin_count": cur_ties,
            "excluded_origin_count_due_to_ties": cur_excluded,
            "affected_package_count": len(cur_affected),
            "pair_set_sha256": set_hash(cur),
        },
        "comparison": {
            "intersection_count": len(inter),
            "historical_only_count": len(hist_only),
            "dr035_only_count": len(cur_only),
            "exact_set_equality": hist == cur,
        },
        "firewall": {
            "tacc_computed": False,
            "delta_tacc_computed": False,
            "reach_computed": False,
            "trajectory_computed": False,
            "outcome_read": False,
            "value_computed": False,
            "predictive_metrics": False,
            "future_activity_read": False,
            "sampling": False,
            "experiment_execution": False,
        },
        "real_rust_dyn2_execution_authorized": False,
    }
    result["reconciliation_status"] = "EXACT" if hist == cur else "PARTIAL"
    out = Path(args.output)
    out.write_text(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
