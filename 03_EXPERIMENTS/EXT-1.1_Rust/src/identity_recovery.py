"""Bounded identity-recovery helper for EXT-1.1 Rust.

This module does not assert that current crates.io IDs are historically valid.
It extracts the current versions/crates tables needed for a later identity
cross-check against the historical 2022-08-31 index and the 2022-09-07
version-download CSV.

The input database dump is the current crates.io db-dump.tar.gz. The script
streams only the relevant CSV members and only retains requested version IDs.
This is an acquisition aid, not confirmatory analysis.
"""
from __future__ import annotations

import csv
import io
import tarfile
from pathlib import Path


def read_version_ids(path: str | Path) -> set[int]:
    ids: set[int] = set()
    with open(path, newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh)
        if "version_id" not in reader.fieldnames:
            raise ValueError("downloads CSV must contain version_id")
        for row in reader:
            ids.add(int(row["version_id"]))
    return ids


def extract_current_identity(db_dump: str | Path, wanted_ids: set[int]):
    """Return current (id, crate_id, version, checksum) records for wanted IDs."""
    versions = {}
    crates = {}
    with tarfile.open(db_dump, "r:gz") as tar:
        for member in tar:
            name = member.name.rsplit("/", 1)[-1]
            if name not in {"versions.csv", "crates.csv"}:
                continue
            stream = tar.extractfile(member)
            if stream is None:
                continue
            text = io.TextIOWrapper(stream, encoding="utf-8", newline="")
            reader = csv.DictReader(text)
            if name == "versions.csv":
                for row in reader:
                    vid = int(row["id"])
                    if vid in wanted_ids:
                        versions[vid] = {
                            "version_id": vid,
                            "crate_id": int(row["crate_id"]),
                            "version": row["num"],
                            "checksum": row.get("checksum"),
                        }
            else:
                needed = {v["crate_id"] for v in versions.values()}
                for row in reader:
                    cid = int(row["id"])
                    if cid in needed:
                        crates[cid] = row["name"]
    return [
        {**record, "crate": crates.get(record["crate_id"])}
        for record in versions.values()
    ]


def classify_against_historical_index(records, historical_pairs, historical_checksums):
    """Classify mappings without silently accepting temporal identity."""
    result = []
    for record in records:
        pair = (record["crate"], record["version"])
        if pair not in historical_pairs:
            status = "FAIL_NOT_IN_HISTORICAL_INDEX"
        elif historical_checksums.get(pair) and record.get("checksum"):
            status = (
                "CANDIDATE_MATCH"
                if historical_checksums[pair] == record["checksum"]
                else "FAIL_CHECKSUM_MISMATCH"
            )
        else:
            status = "UNRESOLVED_NO_CHECKSUM"
        result.append({**record, "identity_status": status})
    return result
