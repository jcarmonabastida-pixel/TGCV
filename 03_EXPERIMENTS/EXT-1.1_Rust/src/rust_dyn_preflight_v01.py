#!/usr/bin/env python3
"""RUST-DYN-EXEC-1A local preflight — no experiment execution.

Checks only the frozen input container and execution metadata required before
real-data authorization. It does not parse package/dependency records into
T_acc, construct temporal pairs, compute Reach/Trajectory, or read outcomes.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
import zipfile
from pathlib import Path

PACKAGE_VERSIONS_MEMBER = "rust_repos_2022_09_07/dumps/postgresql/data/package_versions.csv"
PACKAGE_DEPENDENCIES_MEMBER = "rust_repos_2022_09_07/dumps/postgresql/data/package_dependencies.csv"
TEMPORAL_RULE_ID = "DR-035-v0.1-ADJACENT-CREATED-AT"
HORIZON = 1
REAL_EXECUTION_AUTHORIZED = False

EXPECTED_PACKAGE_VERSION_COLUMNS = {"id", "package_id", "version_str", "created_at"}
EXPECTED_PACKAGE_DEPENDENCY_COLUMNS = {"depending_version", "depending_on_package", "semver_str"}


def sha256_file(path: Path, chunk_size: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            h.update(chunk)
    return h.hexdigest()


def header_from_zip(zf: zipfile.ZipFile, member: str) -> list[str]:
    import csv
    with zf.open(member, "r") as raw:
        line = raw.readline()
    text = line.decode("utf-8-sig")
    return next(csv.reader([text]))


def inspect_member(zf: zipfile.ZipFile, member: str, expected: set[str]) -> dict:
    present = member in set(zf.namelist())
    if not present:
        return {
            "member": member,
            "present": False,
            "header": [],
            "duplicate_columns": [],
            "missing_expected": sorted(expected),
            "schema_pass": False,
        }
    header = header_from_zip(zf, member)
    duplicates = sorted({c for c in header if header.count(c) > 1})
    normalized = {c.strip().lower() for c in header}
    missing = sorted(expected - normalized)
    return {
        "member": member,
        "present": True,
        "header": header,
        "duplicate_columns": duplicates,
        "missing_expected": missing,
        "schema_pass": not missing and not duplicates,
    }


def preflight(dataset: Path) -> dict:
    if not dataset.is_file():
        raise FileNotFoundError(f"DATASET_NOT_FOUND:{dataset}")

    dataset_sha256 = sha256_file(dataset)
    with zipfile.ZipFile(dataset, "r") as zf:
        versions = inspect_member(zf, PACKAGE_VERSIONS_MEMBER, EXPECTED_PACKAGE_VERSION_COLUMNS)
        dependencies = inspect_member(zf, PACKAGE_DEPENDENCIES_MEMBER, EXPECTED_PACKAGE_DEPENDENCY_COLUMNS)

    return {
        "MODE": "LOCAL_PREFLIGHT_ONLY",
        "dataset_path": str(dataset),
        "dataset_sha256": dataset_sha256,
        "zip_opened": True,
        "package_versions": versions,
        "package_dependencies": dependencies,
        "temporal_rule_id": TEMPORAL_RULE_ID,
        "horizon": HORIZON,
        "sampling": False,
        "outcome_read": False,
        "predictive_metrics": False,
        "future_activity_read": False,
        "tacc_constructed": False,
        "delta_tacc_computed": False,
        "reach_computed": False,
        "trajectory_computed": False,
        "real_dataset_execution": False,
        "execution_authorization": REAL_EXECUTION_AUTHORIZED,
        "python": sys.version,
        "platform": platform.platform(),
        "implementation_scope": "INPUT_AND_SCHEMA_PREFLIGHT_ONLY",
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--dataset", required=True)
    args = p.parse_args()
    try:
        result = preflight(Path(args.dataset))
    except Exception as exc:
        print(json.dumps({"MODE": "PREFLIGHT_FAIL_CLOSED", "pass": False, "error": str(exc), "real_dataset_execution": False, "execution_authorization": False}, indent=2))
        return 2
    result["pass"] = bool(
        result["zip_opened"]
        and result["package_versions"]["present"]
        and result["package_versions"]["schema_pass"]
        and result["package_dependencies"]["present"]
        and result["package_dependencies"]["schema_pass"]
    )
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
