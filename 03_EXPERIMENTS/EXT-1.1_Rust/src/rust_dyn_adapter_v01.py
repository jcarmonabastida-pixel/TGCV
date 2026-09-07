#!/usr/bin/env python3
"""RUST-DYN-EXEC-1A — deterministic Rust dynamic data adapter v0.2.

Implements the frozen structural loading layer only. Real dataset execution
remains fail-closed until a separate governance authorization explicitly
permits it.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import io
import json
import sys
import zipfile
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

SRC_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from rstar_v02 import resolve_edge

HORIZON_DEFAULT = 1
TEMPORAL_RULE_ID = "DR-035-v0.1-ADJACENT-CREATED-AT"
REAL_EXECUTION_AUTHORIZED = False
VERSIONS_MEMBER = "rust_repos_2022_09_07/dumps/postgresql/data/package_versions.csv"
DEPENDENCIES_MEMBER = "rust_repos_2022_09_07/dumps/postgresql/data/package_dependencies.csv"


@dataclass(frozen=True, order=True)
class Origin:
    version_id: int
    package_id: int
    version_str: str
    created_at: str


def parse_created_at(value: str) -> dt.datetime:
    if not isinstance(value, str) or not value.strip():
        raise ValueError("INVALID_CREATED_AT")
    try:
        return dt.datetime.fromisoformat(value.strip().replace("Z", "+00:00")).replace(tzinfo=None)
    except ValueError as exc:
        raise ValueError(f"INVALID_CREATED_AT:{value!r}") from exc


def build_adjacent_pairs(origins: Iterable[Origin]) -> tuple[list[tuple[Origin, Origin]], dict]:
    groups: dict[int, list[Origin]] = defaultdict(list)
    materialized = list(origins)
    for origin in materialized:
        parse_created_at(origin.created_at)
        groups[origin.package_id].append(origin)

    pairs: list[tuple[Origin, Origin]] = []
    tie_origin_count = 0
    excluded_origin_count = 0
    zero_pair_package_count = 0

    for package_id in sorted(groups):
        ordered = sorted(groups[package_id], key=lambda o: parse_created_at(o.created_at))
        unique: list[Origin] = []
        i = 0
        while i < len(ordered):
            timestamp = parse_created_at(ordered[i].created_at)
            j = i + 1
            while j < len(ordered) and parse_created_at(ordered[j].created_at) == timestamp:
                j += 1
            block = ordered[i:j]
            if len(block) > 1:
                tie_origin_count += len(block)
                excluded_origin_count += len(block)
            else:
                unique.append(block[0])
            i = j
        package_pairs = list(zip(unique, unique[1:]))
        if not package_pairs:
            zero_pair_package_count += 1
        pairs.extend(package_pairs)

    return pairs, {
        "temporal_rule_id": TEMPORAL_RULE_ID,
        "eligible_origin_count": len(materialized),
        "timestamp_tie_origin_count": tie_origin_count,
        "excluded_origin_count_due_to_ties": excluded_origin_count,
        "temporal_pair_count": len(pairs),
        "pair_count_by_package": _pair_counts(pairs),
        "zero_pair_package_count": zero_pair_package_count,
        "real_execution_authorized": REAL_EXECUTION_AUTHORIZED,
    }


def _pair_counts(pairs: Sequence[tuple[Origin, Origin]]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for left, right in pairs:
        if left.package_id != right.package_id:
            raise RuntimeError("CROSS_PACKAGE_TEMPORAL_PAIR")
        key = str(left.package_id)
        counts[key] = counts.get(key, 0) + 1
    return dict(sorted(counts.items(), key=lambda x: int(x[0])))


def canonical_tacc(rows: Iterable[tuple[int, int, int, str]]) -> tuple[tuple[int, int, int, str], ...]:
    materialized = list(rows)
    ordered = sorted(materialized, key=lambda r: (r[0], r[1], r[2], r[3]))
    for previous, current in zip(ordered, ordered[1:]):
        if previous == current:
            raise ValueError(f"DUPLICATE_TACC_TRANSFORMATION:{current}")
    return tuple(ordered)


def _member_by_basename(zf: zipfile.ZipFile, basename: str) -> str:
    matches = [n for n in zf.namelist() if n.replace("\\", "/").rsplit("/", 1)[-1] == basename]
    if len(matches) != 1:
        raise RuntimeError(f"ARCHIVE_MEMBER_RESOLUTION_ERROR:{basename}:{len(matches)}")
    return matches[0]


def _read_rows(zf: zipfile.ZipFile, basename: str):
    member = _member_by_basename(zf, basename)
    with zf.open(member, "r") as raw:
        text = io.TextIOWrapper(raw, encoding="utf-8", errors="strict", newline="")
        yield from csv.DictReader(text)


def load_structural_origins_and_tacc(dataset: Path):
    """Load only frozen package/version/dependency structure and construct T_acc."""
    with zipfile.ZipFile(dataset, "r") as zf:
        versions: dict[int, Origin] = {}
        by_package: dict[int, list[Origin]] = defaultdict(list)
        for row in _read_rows(zf, "package_versions.csv"):
            required = ("id", "package_id", "version_str", "created_at")
            if any(k not in row or row[k] is None for k in required):
                raise ValueError("MALFORMED_PACKAGE_VERSION_ROW")
            origin = Origin(int(row["id"]), int(row["package_id"]), row["version_str"].strip(), row["created_at"].strip())
            parse_created_at(origin.created_at)
            if origin.version_id in versions:
                raise ValueError(f"DUPLICATE_ORIGIN_ID:{origin.version_id}")
            versions[origin.version_id] = origin
            by_package[origin.package_id].append(origin)

        for package_id in by_package:
            by_package[package_id].sort(key=lambda o: (parse_created_at(o.created_at), o.version_id))

        deps_by_origin: dict[int, list[tuple[int, int, str]]] = defaultdict(list)
        for row in _read_rows(zf, "package_dependencies.csv"):
            required = ("depending_version", "depending_on_package", "semver_str")
            if any(k not in row or row[k] is None for k in required):
                raise ValueError("MALFORMED_PACKAGE_DEPENDENCY_ROW")
            oid = int(row["depending_version"])
            tpid = int(row["depending_on_package"])
            req = row["semver_str"].strip()
            if oid not in versions:
                raise ValueError(f"MISSING_ORIGIN:{oid}")
            deps_by_origin[oid].append((oid, tpid, req))

        records = []
        for oid in sorted(versions):
            origin = versions[oid]
            same_pkg = by_package[origin.package_id]
            origin_ts = parse_created_at(origin.created_at)
            earlier_count = sum(parse_created_at(o.created_at) < origin_ts for o in same_pkg)
            first_ts = parse_created_at(same_pkg[0].created_at)
            age_days = (origin_ts - first_ts).total_seconds() / 86400.0
            tacc_rows = []
            for _, target_package_id, req in deps_by_origin.get(oid, []):
                target_versions = by_package.get(target_package_id, [])
                target_rows = [(o.version_id, o.version_str, o.created_at) for o in target_versions]
                result = resolve_edge(oid, "", origin.created_at, target_package_id, "", req, target_rows)
                selected_id = result["selected_version_id"]
                if selected_id is not None:
                    tacc_rows.append((oid, target_package_id, int(selected_id), result["selected_version"]))
            records.append({
                "origin": origin,
                "prior_release_count": earlier_count,
                "package_age_days": age_days,
                "dependency_count": len(deps_by_origin.get(oid, [])),
                "tacc": canonical_tacc(tacc_rows),
            })
        return records


def _sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _tacc_hash(tacc: Iterable[tuple[int, int, int, str]]) -> str:
    h = hashlib.sha256()
    for origin_id, target_pid, target_vid, target_version in canonical_tacc(tacc):
        h.update(f"{origin_id}|{target_pid}|{target_vid}|{target_version}\n".encode("utf-8"))
    return h.hexdigest()


def synthetic_conformance() -> dict:
    a = Origin(1, 10, "1.0.0", "2020-01-01T00:00:00Z")
    b = Origin(2, 10, "1.1.0", "2020-02-01T00:00:00Z")
    c = Origin(3, 10, "1.2.0", "2020-03-01T00:00:00Z")
    tie1 = Origin(4, 20, "1.0.0", "2020-01-01T00:00:00Z")
    tie2 = Origin(5, 20, "1.1.0", "2020-01-01T00:00:00Z")
    pairs, manifest = build_adjacent_pairs([c, a, b, tie1, tie2])
    pair_ids = [(x.version_id, y.version_id) for x, y in pairs]

    tests = {
        "adjacent_only": pair_ids == [(1, 2), (2, 3)],
        "created_at_order_only": pair_ids == [(1, 2), (2, 3)],
        "timestamp_ties_excluded": manifest["timestamp_tie_origin_count"] == 2,
        "no_cross_package_pairs": all(x.package_id == y.package_id for x, y in pairs),
        "deterministic": build_adjacent_pairs([b, tie2, a, c, tie1])[0] == pairs,
        "tacc_duplicate_fail_closed": _duplicate_test(),
        "real_execution_blocked": REAL_EXECUTION_AUTHORIZED is False,
    }
    return {
        "MODE": "SYNTHETIC_CONFORMANCE_ONLY",
        "TEMPORAL_RULE_ID": TEMPORAL_RULE_ID,
        "HORIZON_DEFAULT": HORIZON_DEFAULT,
        "pass": all(tests.values()),
        "tests": tests,
        "manifest": manifest,
        "REAL_DATASET_EXECUTION": False,
        "EXECUTION_AUTHORIZATION": False,
    }


def _duplicate_test() -> bool:
    row = (1, 10, 100, "1.0.0")
    try:
        canonical_tacc([row, row])
    except ValueError as exc:
        return str(exc).startswith("DUPLICATE_TACC_TRANSFORMATION:")
    return False


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--synthetic", action="store_true")
    parser.add_argument("--dataset", type=Path)
    args = parser.parse_args(argv)

    if args.dataset is not None:
        print(json.dumps({
            "MODE": "FAIL_CLOSED",
            "REAL_DATASET_EXECUTION": False,
            "EXECUTION_AUTHORIZATION": False,
            "reason": "Real dataset execution is not authorized; adapter is construction-only until governance authorization.",
        }, indent=2))
        return 2
    if args.synthetic:
        result = synthetic_conformance()
        print(json.dumps(result, indent=2, sort_keys=True))
        return 0 if result["pass"] else 1
    parser.error("Use --synthetic. Real dataset execution is blocked.")


if __name__ == "__main__":
    raise SystemExit(main())
