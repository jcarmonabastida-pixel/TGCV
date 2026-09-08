#!/usr/bin/env python3
"""RUST-DYN-2 configuration multiplicity audit v0.1.

Structural-only audit. It deliberately does NOT construct T_acc, Reach,
Trajectory, outcomes, or predictive metrics. Real experimental execution
remains unauthorized.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import zipfile
from collections import defaultdict
from pathlib import Path

EXPECTED_SHA256 = "823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224"
DEPENDENCIES_MEMBER = "rust_repos_2022_09_07/dumps/postgresql/data/package_dependencies.csv"
EXPECTED_HEADER = ("depending_version", "depending_on_package", "semver_str")


def file_sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def read_exact_member(zf: zipfile.ZipFile, member: str):
    names = {n.replace("\\", "/") for n in zf.namelist()}
    normalized = member.replace("\\", "/")
    if normalized not in names:
        raise RuntimeError(f"FROZEN_ARCHIVE_MEMBER_MISSING:{normalized}")
    with zf.open(normalized, "r") as raw:
        text = io.TextIOWrapper(raw, encoding="utf-8", errors="strict", newline="")
        reader = csv.DictReader(text)
        header = tuple(reader.fieldnames or ())
        if len(header) != len(set(header)):
            raise ValueError("DUPLICATE_CSV_HEADERS")
        if header != EXPECTED_HEADER:
            raise ValueError(f"UNEXPECTED_HEADER:{header!r}")
        yield from reader


def audit(dataset: Path) -> dict:
    actual_sha = file_sha256(dataset)
    if actual_sha != EXPECTED_SHA256:
        raise RuntimeError(f"DATASET_SHA256_MISMATCH:{actual_sha}")

    groups: dict[tuple[int, int], list[str]] = defaultdict(list)
    total_rows = 0
    affected_rows = 0
    with zipfile.ZipFile(dataset, "r") as zf:
        for row in read_exact_member(zf, DEPENDENCIES_MEMBER):
            if any(row.get(k) is None for k in EXPECTED_HEADER):
                raise ValueError("MALFORMED_DEPENDENCY_ROW")
            origin = int(row["depending_version"])
            target = int(row["depending_on_package"])
            req = row["semver_str"].strip()
            groups[(origin, target)].append(req)
            total_rows += 1

    repeated = {k: v for k, v in groups.items() if len(v) > 1}
    distinct_req = {k: v for k, v in repeated.items() if len(set(v)) > 1}
    identical_only = {k: v for k, v in repeated.items() if len(set(v)) == 1}
    affected_origins = {origin for origin, _ in repeated}
    affected_distinct_origins = {origin for origin, _ in distinct_req}
    affected_rows = sum(len(v) for v in repeated.values())

    summary = {
        "dataset_sha256": actual_sha,
        "member": DEPENDENCIES_MEMBER,
        "total_dependency_rows": total_rows,
        "unique_origin_target_groups": len(groups),
        "repeated_origin_target_groups": len(repeated),
        "origins_with_repeated_target_package": len(affected_origins),
        "origins_with_distinct_requirements_same_target": len(affected_distinct_origins),
        "identical_repetition_groups": len(identical_only),
        "distinct_requirement_groups": len(distinct_req),
        "affected_repeated_declaration_rows": affected_rows,
        "max_declaration_multiplicity": max((len(v) for v in groups.values()), default=0),
        "firewall": {
            "tacc_constructed": False,
            "delta_tacc_computed": False,
            "resolver_selected_version": False,
            "successor_constructed": False,
            "reach_computed": False,
            "trajectory_computed": False,
            "future_activity_read": False,
            "outcome_read": False,
            "predictive_metrics": False,
            "sampling": False,
            "cargo_execution": False,
            "execution_authorization": False,
        },
    }
    canonical = json.dumps(summary, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    summary["audit_summary_sha256"] = hashlib.sha256(canonical).hexdigest()

    if distinct_req:
        summary["decision"] = "C_BLOCKER_LOSSY_ASSIGNMENT_REPRESENTATION"
    elif identical_only:
        summary["decision"] = "B_CONDITIONAL_EXPLICIT_DEDUPLICATION_REQUIRED"
    else:
        summary["decision"] = "A_LOSSLESS_FOR_CURRENT_ASSIGNMENT_REPRESENTATION"
    summary["pass"] = True
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=Path, required=True)
    args = parser.parse_args()
    result = audit(args.dataset)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
