#!/usr/bin/env python3
"""TGCV RUST-DYN-2 real-data executor v0.1.

Frozen for the single authorized primary run under DR-043.
Structural/counterfactual only; no outcome, future-activity, predictive,
sampling or Cargo-runtime path exists in this executor.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import io
import json
import platform
import sys
import zipfile
from collections import defaultdict
from pathlib import Path
from typing import Iterable

SRC_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from rstar_v02 import resolve_edge

DATASET_SHA256 = "823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224"
RSTAR_GIT_BLOB_SHA = "669d4f01131af518f32b1b4b3da27f676ae4ae55"
TEMPORAL_RULE_ID = "DR-035-v0.1-ADJACENT-CREATED-AT"
HORIZON = 1
VERSIONS_MEMBER = "rust_repos_2022_09_07/dumps/postgresql/data/package_versions.csv"
DEPENDENCIES_MEMBER = "rust_repos_2022_09_07/dumps/postgresql/data/package_dependencies.csv"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def git_blob_sha(path: Path) -> str:
    data = path.read_bytes()
    header = f"blob {len(data)}\\0".encode("utf-8")
    return hashlib.sha1(header + data).hexdigest()


def canonical_json_sha(obj) -> str:
    payload = json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def parse_time(value: str) -> dt.datetime:
    if not value or not isinstance(value, str):
        raise ValueError("INVALID_CREATED_AT")
    return dt.datetime.fromisoformat(value.strip().replace("Z", "+00:00")).replace(tzinfo=None)


def read_member(zf: zipfile.ZipFile, member: str):
    names = {n.replace("\\", "/") for n in zf.namelist()}
    member = member.replace("\\", "/")
    if member not in names:
        raise RuntimeError(f"FROZEN_ARCHIVE_MEMBER_MISSING:{member}")
    with zf.open(member, "r") as raw:
        text = io.TextIOWrapper(raw, encoding="utf-8", errors="strict", newline="")
        yield from csv.DictReader(text)


def canonical_config(rows: Iterable[tuple[int, int, str]]) -> tuple[tuple[int, int, str], ...]:
    rows = [tuple(x) for x in rows]
    if len(rows) != len(set(rows)):
        raise ValueError("DUPLICATE_CANONICAL_CONFIGURATION")
    return tuple(sorted(rows, key=lambda x: (x[0], x[1], x[2])))


def successor_config(config, tau):
    _origin_id, target_package, target_version_id, target_version_str = tau
    remaining = [r for r in config if r[0] != target_package]
    remaining.append((target_package, target_version_id, target_version_str))
    return canonical_config(remaining)


def potential_reach(config, tacc):
    return frozenset(successor_config(config, tau) for tau in tacc)


def canonical_tacc(rows):
    rows = [tuple(x) for x in rows]
    ordered = sorted(rows, key=lambda x: (x[0], x[1], x[2], x[3]))
    if any(a == b for a, b in zip(ordered, ordered[1:])):
        raise ValueError("DUPLICATE_TACC_TRANSFORMATION")
    return tuple(ordered)


def classify(t0, t1):
    a, b = set(t0), set(t1)
    if a == b:
        return "PERSISTENCE"
    if a < b:
        return "EXPANSION"
    if b < a:
        return "CONTRACTION"
    return "RECONFIGURATION"


def run(dataset: Path):
    if sha256_file(dataset) != DATASET_SHA256:
        raise RuntimeError("DATASET_SHA256_MISMATCH")
    rstar_path = SRC_DIR / "rstar_v02.py"
    if git_blob_sha(rstar_path) != RSTAR_GIT_BLOB_SHA:
        raise RuntimeError("RSTAR_GIT_BLOB_SHA_MISMATCH")

    versions = {}
    by_package = defaultdict(list)
    deps = defaultdict(list)
    with zipfile.ZipFile(dataset, "r") as zf:
        for row in read_member(zf, VERSIONS_MEMBER):
            required = ("id", "package_id", "version_str", "created_at")
            if any(row.get(k) in (None, "") for k in required):
                raise ValueError("MALFORMED_PACKAGE_VERSION_ROW")
            vid = int(row["id"]); pid = int(row["package_id"])
            created = row["created_at"].strip(); parse_time(created)
            if vid in versions:
                raise ValueError(f"DUPLICATE_ORIGIN_ID:{vid}")
            item = (vid, pid, row["version_str"].strip(), created)
            versions[vid] = item
            by_package[pid].append(item)
        for pid in by_package:
            by_package[pid].sort(key=lambda x: parse_time(x[3]))
        for row in read_member(zf, DEPENDENCIES_MEMBER):
            required = ("depending_version", "depending_on_package", "semver_str")
            if any(row.get(k) in (None, "") for k in required):
                raise ValueError("MALFORMED_PACKAGE_DEPENDENCY_ROW")
            oid = int(row["depending_version"]); tpid = int(row["depending_on_package"])
            if oid not in versions:
                raise ValueError(f"MISSING_ORIGIN:{oid}")
            deps[oid].append((tpid, row["semver_str"].strip()))

    for oid, rows in deps.items():
        targets = [p for p, _ in rows]
        if len(targets) != len(set(targets)):
            raise RuntimeError(f"CONFIGURATION_MULTIPLICITY_VIOLATION:{oid}")

    tacc_by_origin = {}
    config_by_origin = {}
    for oid in sorted(versions):
        _, pid, version_str, created = versions[oid]
        tacc_rows = []
        config_rows = []
        for target_pid, req in deps.get(oid, []):
            candidates = [(v[0], v[2], v[3]) for v in by_package.get(target_pid, [])]
            resolved = resolve_edge(oid, "", created, target_pid, "", req, candidates)
            selected_id = resolved["selected_version_id"]
            if selected_id is None:
                continue
            selected_version = resolved["selected_version"]
            tacc_rows.append((oid, target_pid, int(selected_id), selected_version))
            config_rows.append((target_pid, int(selected_id), selected_version))
        tacc_by_origin[oid] = canonical_tacc(tacc_rows)
        config_by_origin[oid] = canonical_config(config_rows)

    pairs = []
    zero_pair_packages = 0
    tie_origin_count = 0
    excluded_origin_count = 0
    for pid in sorted(by_package):
        ordered = by_package[pid]
        unique = []
        i = 0
        while i < len(ordered):
            j = i + 1
            ts = parse_time(ordered[i][3])
            while j < len(ordered) and parse_time(ordered[j][3]) == ts:
                j += 1
            block = ordered[i:j]
            if len(block) > 1:
                tie_origin_count += len(block)
                excluded_origin_count += len(block)
            else:
                unique.append(block[0])
            i = j
        pp = list(zip(unique, unique[1:]))
        if not pp:
            zero_pair_packages += 1
        pairs.extend(pp)

    counts = {k: 0 for k in ("PERSISTENCE", "EXPANSION", "CONTRACTION", "RECONFIGURATION")}
    nd1 = nd2 = nd4 = 0
    pair_evidence_hash = hashlib.sha256()
    witnesses = {}

    for left, right in pairs:
        a_id, b_id = left[0], right[0]
        t0, t1 = tacc_by_origin[a_id], tacc_by_origin[b_id]
        c0, c1 = config_by_origin[a_id], config_by_origin[b_id]
        r0 = potential_reach(c0, t0)
        r1 = potential_reach(c1, t1)
        classification = classify(t0, t1)
        counts[classification] += 1
        delta_t = t0 != t1
        delta_r = r0 != r1
        if delta_t and not delta_r:
            nd1 += 1
            key = "ND-1"
        elif delta_t and delta_r:
            nd2 += 1
            key = "ND-2"
        else:
            key = None
        if len(r0) == len(r1) and r0 != r1:
            nd4 += 1
            if "ND-4" not in witnesses:
                witnesses["ND-4"] = {"origin_a": a_id, "origin_b": b_id, "reach_a": sorted(r0), "reach_b": sorted(r1)}
        if key and key not in witnesses:
            witnesses[key] = {"origin_a": a_id, "origin_b": b_id, "tacc_a": list(t0), "tacc_b": list(t1), "reach_a": sorted(r0), "reach_b": sorted(r1)}
        evidence = {"a": a_id, "b": b_id, "tacc_a": canonical_json_sha(list(t0)), "tacc_b": canonical_json_sha(list(t1)), "reach_a": canonical_json_sha(sorted(r0)), "reach_b": canonical_json_sha(sorted(r1)), "classification": classification}
        pair_evidence_hash.update(json.dumps(evidence, sort_keys=True, separators=(",", ":")).encode("utf-8"))
        pair_evidence_hash.update(b"\n")

    summary = {
        "mode": "RUST_DYN_2_REAL_PRIMARY",
        "dataset_sha256": DATASET_SHA256,
        "rstar_git_blob_sha": RSTAR_GIT_BLOB_SHA,
        "temporal_rule_id": TEMPORAL_RULE_ID,
        "horizon": HORIZON,
        "eligible_origin_count": len(versions),
        "timestamp_tie_origin_count": tie_origin_count,
        "excluded_origin_count_due_to_ties": excluded_origin_count,
        "temporal_pair_count": len(pairs),
        "zero_pair_package_count": zero_pair_packages,
        "classification_counts": counts,
        "nd1_delta_tacc_without_delta_reach": nd1,
        "nd2_delta_tacc_with_delta_reach": nd2,
        "nd4_equal_reach_cardinality_different_membership": nd4,
        "pair_evidence_sha256": pair_evidence_hash.hexdigest(),
        "firewall": {"sampling": False, "outcome_read": False, "future_activity_read": False, "predictive_metrics": False, "cargo_execution": False, "runtime_outcomes": False, "lockfile_read": False, "value_read": False},
        "platform": platform.platform(),
        "python": sys.version,
        "execution_authorized": True,
    }
    return {"summary": summary, "witnesses": witnesses}


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--dataset", type=Path, required=True)
    args = p.parse_args()
    result = run(args.dataset)
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
