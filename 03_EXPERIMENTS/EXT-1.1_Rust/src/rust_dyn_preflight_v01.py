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

DATASET_MEMBER = "rust_repos_2022_09_07/dumps/postgresql/data/package_versions.csv"
TEMPORAL_RULE_ID = "DR-035-v0.1-ADJACENT-CREATED-AT"
HORIZON = 1
REAL_EXECUTION_AUTHORIZED = False

EXPECTED_PACKAGE_VERSION_COLUMNS = {
    "id", "package_id", "version", "created_at"
}


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


def preflight(dataset: Path) -> dict:
    if not dataset.is_file():
        raise FileNotFoundError(f"DATASET_NOT_FOUND:{dataset}")

    dataset_sha256 = sha256_file(dataset)
    with zipfile.ZipFile(dataset, "r") as zf:
        names = set(zf.namelist())
        member_present = DATASET_MEMBER in names
        if not member_present:
            raise RuntimeError(f"REQUIRED_MEMBER_NOT_FOUND:{DATASET_MEMBER}")
        header = header_from_zip(zf, DATASET_MEMBER)
        duplicates = sorted({c for c in header if header.count(c) > 1})

    # This is intentionally a schema observation only. The exact final schema
    # is frozen by D-OPS-1 after inspection; no structural execution follows.
    normalized = {c.strip().lower() for c in header}
    missing_expected = sorted(EXPECTED_PACKAGE_VERSION_COLUMNS - normalized)

    return {
        "MODE": "LOCAL_PREFLIGHT_ONLY",
        "dataset_path": str(dataset),
        "dataset_sha256": dataset_sha256,
        "zip_opened": True,
        "required_member": DATASET_MEMBER,
        "required_member_present": member_present,
        "package_versions_header": header,
        "duplicate_header_columns": duplicates,
        "expected_column_presence_check": {
            "expected": sorted(EXPECTED_PACKAGE_VERSION_COLUMNS),
            "missing": missing_expected,
            "pass": not missing_expected and not duplicates,
        },
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
    result["pass"] = bool(result["zip_opened"] and result["required_member_present"] and result["expected_column_presence_check"]["pass"])
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
