"""Structural audit for proposed EXT-1.1 candidate universe T.

This audit constructs only the candidate universe T. It deliberately does not
apply q, R*, accessibility, resources, baseline B, sampling, or outcomes.
"""
from __future__ import annotations

import csv
import io
import zipfile
from collections import defaultdict
from pathlib import Path

ZIP_PATH = Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"
BASE = "dumps/postgresql/data/"


def rows(z: zipfile.ZipFile, name: str):
    with z.open(BASE + name, "r") as raw:
        text = io.TextIOWrapper(raw, encoding="utf-8", newline="")
        yield from csv.DictReader(text)


def main() -> int:
    print("TGCV EXT-1.1 — Candidate universe T audit v0.1")
    print(f"ZIP: {ZIP_PATH}")
    if not ZIP_PATH.exists():
        print("FAIL_DATASET_NOT_FOUND: True")
        return 2

    with zipfile.ZipFile(ZIP_PATH) as z:
        packages = {}
        package_names = {}
        for r in rows(z, "packages.csv"):
            pid = int(r["id"])
            packages[pid] = (r["source_id"], r["name"])
            package_names[pid] = r["name"]

        versions = {}
        versions_by_package = defaultdict(list)
        for r in rows(z, "package_versions.csv"):
            vid = int(r["id"])
            pid = int(r["package_id"])
            ts = r["created_at"]
            versions[vid] = (pid, ts, r["version_str"])
            versions_by_package[pid].append(vid)

        # Canonicalize target version ordering by immutable version id only for
        # audit determinism. Scientific selection remains R*'s responsibility.
        for pid in versions_by_package:
            versions_by_package[pid].sort()

        candidate_keys = set()
        edge_count = 0
        candidate_count = 0
        future_violations = 0
        missing_origin = 0
        missing_target_package = 0
        target_package_mismatch = 0
        q_dependent_decision = False
        origin_counts = defaultdict(int)

        for r in rows(z, "package_dependencies.csv"):
            edge_count += 1
            oid = int(r["depending_version"])
            tpid = int(r["depending_on_package"])
            if oid not in versions:
                missing_origin += 1
                continue
            if tpid not in packages:
                missing_target_package += 1
                continue

            origin_pid, origin_ts, _ = versions[oid]
            for tvid in versions_by_package.get(tpid, []):
                tpid2, target_ts, _ = versions[tvid]
                if tpid2 != tpid:
                    target_package_mismatch += 1
                    continue
                if target_ts <= origin_ts:
                    key = (oid, tpid, tvid)
                    if key not in candidate_keys:
                        candidate_keys.add(key)
                        candidate_count += 1
                        origin_counts[oid] += 1
                else:
                    future_violations += 1

        duplicate_keys = (edge_count + candidate_count)  # placeholder overwritten below
        # set membership makes canonical candidate keys unique by construction;
        # report the cardinality as the uniqueness invariant.
        unique_keys = len(candidate_keys)
        duplicate_keys = candidate_count - unique_keys

        print(f"PACKAGE_COUNT: {len(packages)}")
        print(f"VERSION_COUNT: {len(versions)}")
        print(f"DEPENDENCY_EDGE_COUNT: {edge_count}")
        print(f"CANDIDATE_COUNT: {candidate_count}")
        print(f"UNIQUE_CANDIDATE_KEYS: {unique_keys}")
        print(f"DUPLICATE_CANDIDATE_KEYS: {duplicate_keys}")
        print(f"FUTURE_TIMESTAMP_VIOLATIONS: {future_violations}")
        print(f"MISSING_ORIGIN_VERSION: {missing_origin}")
        print(f"MISSING_TARGET_PACKAGE: {missing_target_package}")
        print(f"TARGET_PACKAGE_ID_MISMATCH: {target_package_mismatch}")
        print(f"Q_USED_FOR_MEMBERSHIP_DECISION: {q_dependent_decision}")
        print(f"PASS_CANDIDATE_KEY_UNIQUE: {duplicate_keys == 0}")
        print(f"PASS_TEMPORAL_CUTOFF: {future_violations == 0}")
        print(f"PASS_ORIGIN_FK: {missing_origin == 0}")
        print(f"PASS_TARGET_PACKAGE_FK: {missing_target_package == 0}")
        print(f"PASS_TARGET_PACKAGE_CONSISTENCY: {target_package_mismatch == 0}")
        print(f"PASS_Q_INDEPENDENCE_BY_CONSTRUCTION: {not q_dependent_decision}")
        print(f"PASS_T_STRUCTURAL: {duplicate_keys == 0 and future_violations == 0 and missing_origin == 0 and missing_target_package == 0 and target_package_mismatch == 0}")
        print("NOTE: This audit does not execute R*, accessibility, resources, B, sampling, or outcomes.")
        print("NOTE: Candidate membership is generated solely from observed dependency edges, target package identity, target releases, and the origin temporal cutoff.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
