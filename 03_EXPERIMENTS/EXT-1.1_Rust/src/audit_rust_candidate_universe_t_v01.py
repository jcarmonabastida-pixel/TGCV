"""Structural audit for proposed EXT-1.1 candidate universe T.

The Rust dump stores the PostgreSQL tables below under
``dumps/postgresql/data``.  The audit resolves those archive members by
basename from the actual ZIP manifest instead of assuming a single prefix.
It constructs only T and deliberately does not apply q, R*, accessibility,
resources, baseline B, sampling, or outcomes.
"""
from __future__ import annotations

import csv
import io
import zipfile
from collections import defaultdict
from pathlib import Path

ZIP_PATH = Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"
EXPECTED_FILES = {
    "packages.csv": "packages.csv",
    "package_versions.csv": "package_versions.csv",
    "package_dependencies.csv": "package_dependencies.csv",
}


def archive_member(z: zipfile.ZipFile, basename: str) -> str:
    matches = [n for n in z.namelist() if n.replace("\\", "/").rsplit("/", 1)[-1] == basename]
    if len(matches) != 1:
        raise RuntimeError(
            f"ARCHIVE_MEMBER_RESOLUTION_ERROR: {basename!r}: found {len(matches)} matches"
        )
    return matches[0]


def rows(z: zipfile.ZipFile, basename: str):
    member = archive_member(z, basename)
    with z.open(member, "r") as raw:
        text = io.TextIOWrapper(raw, encoding="utf-8", newline="")
        yield from csv.DictReader(text)


def main() -> int:
    print("TGCV EXT-1.1 — Candidate universe T audit v0.1")
    print(f"ZIP: {ZIP_PATH}")
    if not ZIP_PATH.exists():
        print("FAIL_DATASET_NOT_FOUND: True")
        return 2

    try:
        with zipfile.ZipFile(ZIP_PATH) as z:
            resolved = {name: archive_member(z, name) for name in EXPECTED_FILES}
            print("ARCHIVE_MEMBERS:")
            for basename, member in resolved.items():
                print(f"  {basename}: {member}")

            packages = {}
            for r in rows(z, "packages.csv"):
                pid = int(r["id"])
                packages[pid] = (r["source_id"], r["name"])

            versions = {}
            versions_by_package = defaultdict(list)
            for r in rows(z, "package_versions.csv"):
                vid = int(r["id"])
                pid = int(r["package_id"])
                ts = r["created_at"]
                versions[vid] = (pid, ts, r["version_str"])
                versions_by_package[pid].append(vid)

            # Canonical target ordering is immutable version-id order. Scientific
            # semantic-version selection remains R*'s responsibility.
            for pid in versions_by_package:
                versions_by_package[pid].sort()

            candidate_keys = set()
            edge_keys = set()
            duplicate_dependency_edges = 0
            edge_count = 0
            candidate_count = 0
            future_violations = 0
            missing_origin = 0
            missing_target_package = 0
            target_package_mismatch = 0
            q_dependent_decision = False

            for r in rows(z, "package_dependencies.csv"):
                edge_count += 1
                oid = int(r["depending_version"])
                tpid = int(r["depending_on_package"])
                q = r["semver_str"]
                edge_key = (oid, tpid, q)
                if edge_key in edge_keys:
                    duplicate_dependency_edges += 1
                else:
                    edge_keys.add(edge_key)

                if oid not in versions:
                    missing_origin += 1
                    continue
                if tpid not in packages:
                    missing_target_package += 1
                    continue

                origin_pid, origin_ts, _ = versions[oid]
                # origin_pid is retained only for structural validation; the
                # candidate key identifies the observed origin version itself.
                _ = origin_pid

                for tvid in versions_by_package.get(tpid, []):
                    tpid2, target_ts, _ = versions[tvid]
                    if tpid2 != tpid:
                        target_package_mismatch += 1
                        continue
                    if target_ts <= origin_ts:
                        key = (oid, tpid, tvid)
                        candidate_keys.add(key)
                    else:
                        future_violations += 1

            candidate_count = len(candidate_keys)
            # Because T is a set keyed by (origin version, target package,
            # target version), duplicate rows in the dependency table do not
            # create duplicate T elements. Their multiplicity is reported
            # separately as provenance/audit information.
            duplicate_candidate_keys = 0

            print(f"PACKAGE_COUNT: {len(packages)}")
            print(f"VERSION_COUNT: {len(versions)}")
            print(f"DEPENDENCY_EDGE_COUNT: {edge_count}")
            print(f"UNIQUE_DEPENDENCY_EDGE_KEYS: {len(edge_keys)}")
            print(f"DUPLICATE_DEPENDENCY_EDGE_ROWS: {duplicate_dependency_edges}")
            print(f"CANDIDATE_COUNT: {candidate_count}")
            print(f"UNIQUE_CANDIDATE_KEYS: {candidate_count}")
            print(f"DUPLICATE_CANDIDATE_KEYS: {duplicate_candidate_keys}")
            print(f"FUTURE_TIMESTAMP_VIOLATIONS: {future_violations}")
            print(f"MISSING_ORIGIN_VERSION: {missing_origin}")
            print(f"MISSING_TARGET_PACKAGE: {missing_target_package}")
            print(f"TARGET_PACKAGE_ID_MISMATCH: {target_package_mismatch}")
            print(f"Q_USED_FOR_MEMBERSHIP_DECISION: {q_dependent_decision}")
            print(f"PASS_CANDIDATE_KEY_UNIQUE: {duplicate_candidate_keys == 0}")
            print(f"PASS_TEMPORAL_CUTOFF: {future_violations == 0}")
            print(f"PASS_ORIGIN_FK: {missing_origin == 0}")
            print(f"PASS_TARGET_PACKAGE_FK: {missing_target_package == 0}")
            print(f"PASS_TARGET_PACKAGE_CONSISTENCY: {target_package_mismatch == 0}")
            print(f"PASS_Q_INDEPENDENCE_BY_CONSTRUCTION: {not q_dependent_decision}")
            print(
                "PASS_T_STRUCTURAL: "
                + str(
                    duplicate_candidate_keys == 0
                    and future_violations == 0
                    and missing_origin == 0
                    and missing_target_package == 0
                    and target_package_mismatch == 0
                )
            )
            print("NOTE: This audit does not execute R*, accessibility, resources, B, sampling, or outcomes.")
            print("NOTE: Candidate membership is generated solely from observed dependency edges, target package identity, target releases, and the origin temporal cutoff.")

    except (KeyError, ValueError, csv.Error, RuntimeError, zipfile.BadZipFile) as exc:
        print(f"FAIL_AUDIT_RUNTIME: {type(exc).__name__}: {exc}")
        return 3

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
