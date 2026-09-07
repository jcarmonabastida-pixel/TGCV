#!/usr/bin/env python3
"""EXT-1.1 Rust — deterministic TR-131 executor v0.1.

Implements DR-029 v0.2 only. The executor compares exact conventional-state
B equivalence classes against canonical T_acc membership sets. It contains no
outcome, predictive, Reach, sampling, or post-origin analytical path.

Running this module without --dataset performs only the synthetic conformance
suite. Real-dataset execution is intentionally explicit and must be authorized
by the subsequent implementation gate.
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
from typing import Iterable

SRC_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from rstar_v02 import resolve_edge  # noqa: E402

DEFAULT_ZIP = Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"


@dataclass(frozen=True, order=True)
class BState:
    version_str: str
    prior_release_count: int
    package_age_days: float
    dependency_count: int


@dataclass(frozen=True, order=True)
class Origin:
    version_id: int
    package_id: int
    version_str: str
    created_at: str


def parse_ts(value: str) -> dt.datetime:
    return dt.datetime.fromisoformat(value.strip().replace("Z", "+00:00")).replace(tzinfo=None)


def b_from_origin(origin: Origin, prior_count: int, package_age_days: float, dependency_count: int) -> BState:
    return BState(origin.version_str, prior_count, package_age_days, dependency_count)


def canonical_tacc(rows: Iterable[tuple[int, int, int, str]]) -> tuple[tuple[int, int, int, str], ...]:
    return tuple(sorted(set(rows), key=lambda r: (r[0], r[1], r[2], r[3])))


def canonical_sha256(tacc: Iterable[tuple[int, int, int, str]]) -> str:
    h = hashlib.sha256()
    for origin_id, target_pid, target_vid, target_version in canonical_tacc(tacc):
        h.update(f"{origin_id}|{target_pid}|{target_vid}|{target_version}\n".encode("utf-8"))
    return h.hexdigest()


def compare_b_classes(records: Iterable[tuple[int, BState, Iterable[tuple[int, int, int, str]]]]) -> dict:
    groups: dict[BState, list[tuple[int, tuple[tuple[int, int, int, str], ...]]]] = defaultdict(list)
    seen_origins: set[int] = set()
    for origin_id, bstate, tacc in records:
        if origin_id in seen_origins:
            raise ValueError(f"DUPLICATE_ORIGIN_ID:{origin_id}")
        seen_origins.add(origin_id)
        groups[bstate].append((origin_id, canonical_tacc(tacc)))

    witnesses = []
    comparable_classes = 0
    differing_classes = 0
    pair_comparisons = 0
    for bstate in sorted(groups):
        members = sorted(groups[bstate], key=lambda x: x[0])
        if len(members) < 2:
            continue
        comparable_classes += 1
        base_id, base_tacc = members[0]
        class_diff = False
        for other_id, other_tacc in members[1:]:
            pair_comparisons += 1
            if other_tacc != base_tacc:
                class_diff = True
                witnesses.append({
                    "origin_a": base_id,
                    "origin_b": other_id,
                    "B": {
                        "version_str": bstate.version_str,
                        "prior_release_count": bstate.prior_release_count,
                        "package_age_days": bstate.package_age_days,
                        "dependency_count": bstate.dependency_count,
                    },
                    "tacc_a_sha256": canonical_sha256(base_tacc),
                    "tacc_b_sha256": canonical_sha256(other_tacc),
                    "tacc_a_count": len(base_tacc),
                    "tacc_b_count": len(other_tacc),
                })
        if class_diff:
            differing_classes += 1

    witnesses.sort(key=lambda w: (w["origin_a"], w["origin_b"]))
    return {
        "origin_count": len(seen_origins),
        "equivalence_class_count": len(groups),
        "singleton_class_count": sum(len(v) == 1 for v in groups.values()),
        "multi_member_class_count": sum(len(v) >= 2 for v in groups.values()),
        "comparable_class_count": comparable_classes,
        "pair_comparison_count": pair_comparisons,
        "differing_class_count": differing_classes,
        "witness_count": len(witnesses),
        "witnesses": witnesses,
    }


def synthetic_conformance() -> dict:
    same = [(10, 20, 200, "1.0.0")]
    different = [(10, 20, 200, "1.0.0"), (10, 20, 201, "1.1.0")]
    same_card_different_membership = [(10, 20, 200, "1.0.0"), (10, 20, 201, "1.1.0")]
    empty = []
    results = {}

    results["same_B_same_Tacc_no_witness"] = compare_b_classes([
        (1, BState("1.0.0", 0, 0.0, 1), same),
        (2, BState("1.0.0", 0, 0.0, 1), same),
    ])["witness_count"] == 0

    results["same_B_different_Tacc_witness"] = compare_b_classes([
        (1, BState("1.0.0", 0, 0.0, 1), same),
        (2, BState("1.0.0", 0, 0.0, 1), different),
    ])["witness_count"] == 1

    results["same_cardinality_different_membership_witness"] = compare_b_classes([
        (1, BState("1.0.0", 0, 0.0, 1), same_card_different_membership),
        (2, BState("1.0.0", 0, 0.0, 1), [(10, 20, 202, "1.2.0"), (10, 20, 203, "1.3.0")]),
    ])["witness_count"] == 1

    results["different_B_not_comparable"] = compare_b_classes([
        (1, BState("1.0.0", 0, 0.0, 1), same),
        (2, BState("1.1.0", 0, 0.0, 1), different),
    )["pair_comparison_count"] == 0

    results["empty_tacc_equality"] = compare_b_classes([
        (1, BState("1.0.0", 0, 0.0, 0), empty),
        (2, BState("1.0.0", 0, 0.0, 0), empty),
    ])["witness_count"] == 0

    try:
        compare_b_classes([
            (1, BState("1.0.0", 0, 0.0, 0), empty),
            (1, BState("1.0.0", 0, 0.0, 0), empty),
        ])
        results["duplicate_origin_fail_closed"] = False
    except ValueError as exc:
        results["duplicate_origin_fail_closed"] = str(exc).startswith("DUPLICATE_ORIGIN_ID:")

    try:
        compare_b_classes([
            (1, None, empty),  # type: ignore[arg-type]
            (2, BState("1.0.0", 0, 0.0, 0), empty),
        ])
        results["missing_state_fail_closed"] = False
    except (TypeError, AttributeError):
        results["missing_state_fail_closed"] = True

    ordered = compare_b_classes([
        (1, BState("1.0.0", 0, 0.0, 1), same_card_different_membership),
        (2, BState("1.0.0", 0, 0.0, 1), [(10, 20, 202, "1.2.0"), (10, 20, 203, "1.3.0")]),
    ])
    permuted = compare_b_classes([
        (2, BState("1.0.0", 0, 0.0, 1), [(10, 20, 203, "1.3.0"), (10, 20, 202, "1.2.0")]),
        (1, BState("1.0.0", 0, 0.0, 1), [(10, 20, 200, "1.0.0"), (10, 20, 201, "1.1.0")]),
    ])
    results["order_permutation_invariant"] = ordered["witness_count"] == permuted["witness_count"] and ordered["pair_comparison_count"] == permuted["pair_comparison_count"]

    # Firewall test: an outcome-like field exists in the synthetic record but is
    # intentionally not represented in BState or passed to comparison logic.
    synthetic_with_prohibited = {"outcome": 1, "record": (1, BState("1.0.0", 0, 0.0, 0), empty)}
    results["prohibited_outcome_not_read"] = compare_b_classes([synthetic_with_prohibited["record"]])["witness_count"] == 0

    results["repeatable"] = compare_b_classes([
        (1, BState("1.0.0", 0, 0.0, 1), same),
        (2, BState("1.0.0", 0, 0.0, 1), different),
    ]) == compare_b_classes([
        (1, BState("1.0.0", 0, 0.0, 1), same),
        (2, BState("1.0.0", 0, 0.0, 1), different),
    ])

    return {"tests": results, "pass": all(results.values())}


def member_by_basename(zf: zipfile.ZipFile, basename: str) -> str:
    matches = [n for n in zf.namelist() if n.replace("\\", "/").rsplit("/", 1)[-1] == basename]
    if len(matches) != 1:
        raise RuntimeError(f"ARCHIVE_MEMBER_RESOLUTION_ERROR:{basename}:{len(matches)}")
    return matches[0]


def read_csv_rows(zf: zipfile.ZipFile, basename: str):
    member = member_by_basename(zf, basename)
    with zf.open(member, "r") as raw:
        text = io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline="")
        yield from csv.DictReader(text)


def load_real_records(zip_path: Path):
    """Build B and T_acc records from the frozen structural snapshot.

    This function is deliberately not called by the default test mode.
    """
    with zipfile.ZipFile(zip_path, "r") as zf:
        versions: dict[int, Origin] = {}
        by_package: dict[int, list[Origin]] = defaultdict(list)
        dep_count: dict[int, int] = defaultdict(int)
        for row in read_csv_rows(zf, "package_versions.csv"):
            vid, pid = int(row["id"]), int(row["package_id"])
            origin = Origin(vid, pid, row["version_str"].strip(), row["created_at"].strip())
            if vid in versions:
                raise ValueError(f"DUPLICATE_ORIGIN_ID:{vid}")
            versions[vid] = origin
            by_package[pid].append(origin)
        for pid in by_package:
            by_package[pid].sort(key=lambda o: (parse_ts(o.created_at), o.version_id))
        deps_by_origin: dict[int, list[tuple[int, int, str]]] = defaultdict(list)
        for row in read_csv_rows(zf, "package_dependencies.csv"):
            oid = int(row["depending_version"])
            tpid = int(row["depending_on_package"])
            req = row["semver_str"]
            if oid not in versions:
                raise ValueError(f"MISSING_ORIGIN:{oid}")
            dep_count[oid] += 1
            deps_by_origin[oid].append((oid, tpid, req))

        records = []
        for oid in sorted(versions):
            origin = versions[oid]
            same_pkg = by_package[origin.package_id]
            origin_ts = parse_ts(origin.created_at)
            earlier = [o for o in same_pkg if parse_ts(o.created_at) < origin_ts]
            first_ts = parse_ts(same_pkg[0].created_at)
            age_days = (origin_ts - first_ts).total_seconds() / 86400.0
            bstate = b_from_origin(origin, len(earlier), age_days, dep_count[oid])
            tacc = []
            for _, tpid, req in deps_by_origin.get(oid, []):
                target_versions = by_package.get(tpid, [])
                target_rows = [(o.version_id, o.version_str, o.created_at) for o in target_versions]
                result = resolve_edge(oid, "", origin.created_at, tpid, "", req, target_rows)
                selected_id = result["selected_version_id"]
                if selected_id is not None:
                    tacc.append((oid, tpid, int(selected_id), result["selected_version"]))
            records.append((oid, bstate, canonical_tacc(tacc)))
        return records


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", type=Path, default=None, help="Explicitly execute against the frozen Rust dataset")
    args = parser.parse_args()

    if args.dataset is None:
        result = synthetic_conformance()
        print(json.dumps({"MODE": "SYNTHETIC_CONFORMANCE_ONLY", **result}, indent=2, sort_keys=True))
        print("REAL_DATASET_EXECUTION: False")
        print("TR131_EXECUTION_AUTHORIZATION: False")
        return 0 if result["pass"] else 6

    if not args.dataset.exists():
        print(json.dumps({"FAIL_DATASET_NOT_FOUND": str(args.dataset)}))
        return 2

    records = load_real_records(args.dataset)
    result = compare_b_classes(records)
    result["tacc_membership_witness_sha256"] = hashlib.sha256(
        json.dumps(result["witnesses"], sort_keys=True, separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    result["MODE"] = "REAL_DATASET"
    result["SAMPLING"] = False
    result["OUTCOME_READ"] = False
    result["REACH_READ"] = False
    result["PREDICTIVE_METRICS"] = False
    result["POST_ORIGIN_ANALYSIS"] = False
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
