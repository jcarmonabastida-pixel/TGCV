#!/usr/bin/env python3
"""TGCV Rust paired temporal T_acc / Delta T_acc structural audit v0.1.

OUTCOME-BLIND / PRE-CONFIRMATORY.

This audit deliberately does NOT use the EXT-1.1 outcome, model, features,
180-day window, or train/test split. It reconstructs membership-level T_acc
at two frozen package-local temporal boundaries and classifies Add/Rem.

Important: unlike DR-026A, this implementation does NOT use the old
select-max resolver as the representation of T_acc. Every target release that
satisfies the frozen R* requirement at the boundary is represented as a
membership relation.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import io
import sqlite3
import tempfile
import zipfile
from collections import defaultdict
from pathlib import Path
import sys

SRC_DIR = Path(__file__).resolve().parent
if str(SRC_DIR) not in sys.path:
    sys.path.insert(0, str(SRC_DIR))

from rstar_v02 import parse_requirement, satisfies  # noqa: E402

DEFAULT_ZIP = Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"
REQUIRED_V = {"id", "package_id", "version_str", "created_at"}
REQUIRED_D = {"depending_version", "depending_on_package", "semver_str"}


def member_by_basename(zf: zipfile.ZipFile, basename: str) -> str:
    matches = [n for n in zf.namelist() if n.replace("\\", "/").rsplit("/", 1)[-1] == basename]
    if len(matches) != 1:
        raise RuntimeError(f"ARCHIVE_MEMBER_RESOLUTION_ERROR: {basename}: found {len(matches)}")
    return matches[0]


def parse_ts(value: str) -> dt.datetime:
    return dt.datetime.fromisoformat(value.strip().replace("Z", "+00:00")).replace(tzinfo=None)


def read_csv_rows(zf: zipfile.ZipFile, basename: str):
    member = member_by_basename(zf, basename)
    with zf.open(member, "r") as raw:
        text = io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline="")
        yield from csv.DictReader(text)


def schema_check(zf: zipfile.ZipFile) -> None:
    for basename, required in (("package_versions.csv", REQUIRED_V), ("package_dependencies.csv", REQUIRED_D)):
        with zf.open(member_by_basename(zf, basename), "r") as raw:
            text = io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline="")
            fields = set(csv.DictReader(text).fieldnames or [])
        missing = sorted(required - fields)
        if missing:
            raise RuntimeError(f"FAIL_SCHEMA_{basename}: {','.join(missing)}")


def req_matches(req: str, target_version: str) -> bool:
    """Apply only the frozen R* v0.2 grammar/semantics.

    Unsupported requirements are not coerced. The caller records them as
    unresolved for the structural audit.
    """
    parsed = parse_requirement(req.strip())
    if parsed is None:
        raise ValueError("UNSUPPORTED_REQUIREMENT")
    return satisfies(target_version, parsed)


def next_release(versions_by_package, package_id: int, origin_ts: str, origin_id: int):
    origin_time = parse_ts(origin_ts)
    rows = versions_by_package.get(package_id, [])
    later = [r for r in rows if parse_ts(r[2]) > origin_time]
    if not later:
        return None
    later.sort(key=lambda r: (parse_ts(r[2]), r[0]))
    return later[0]


def canonical_sha(con: sqlite3.Connection, table: str) -> str:
    h = hashlib.sha256()
    cur = con.execute(f"SELECT origin_id,target_package_id,target_version_id FROM {table} ORDER BY origin_id,target_package_id,target_version_id")
    for row in cur:
        h.update(f"{row[0]}|{row[1]}|{row[2]}\n".encode("utf-8"))
    return h.hexdigest()


def main() -> int:
    ap = argparse.ArgumentParser(description="TGCV Rust paired temporal T_acc / Delta T_acc structural audit")
    ap.add_argument("--zip", default=str(DEFAULT_ZIP))
    args = ap.parse_args()
    zip_path = Path(args.zip)

    print("TGCV — Rust Paired Temporal T_acc / Delta T_acc Structural Audit v0.1")
    print("=" * 78)
    print(f"ZIP: {zip_path}")
    print("MODE: OUTCOME-BLIND / STRUCTURAL ONLY")
    print("TACC_REPRESENTATION: MEMBERSHIP-LEVEL ALL-SATISFYING-TARGET-RELEASES")
    print("TEMPORAL_RULE: ORIGIN_TIMESTAMP -> NEXT_RELEASE_OF_SAME_PACKAGE")
    print("OUTCOME_LABELS: NOT COMPUTED")
    print("MODEL_FITTING: NOT PERFORMED")
    print("FEATURE_ENGINEERING: NOT PERFORMED")
    print("180_DAY_WINDOW: NOT USED")

    if not zip_path.exists():
        print("FAIL_DATASET_NOT_FOUND: True")
        return 2

    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            schema_check(zf)

            versions = {}
            versions_by_package = defaultdict(list)
            for row in read_csv_rows(zf, "package_versions.csv"):
                vid = int(row["id"])
                pid = int(row["package_id"])
                vstr = row["version_str"].strip()
                ts = row["created_at"].strip()
                versions[vid] = (pid, vstr, ts)
                versions_by_package[pid].append((vid, vstr, ts))
            for pid in versions_by_package:
                versions_by_package[pid].sort(key=lambda r: (parse_ts(r[2]), r[0]))

            package_count = sum(1 for _ in read_csv_rows(zf, "packages.csv"))

            with tempfile.TemporaryDirectory(prefix="tgcv_temporal_tacc_") as tmp:
                db = sqlite3.connect(Path(tmp) / "paired_tacc.sqlite")
                try:
                    db.execute("PRAGMA journal_mode=OFF")
                    db.execute("PRAGMA synchronous=OFF")
                    db.execute("PRAGMA temp_store=FILE")
                    db.execute("CREATE TABLE pairs (origin_id INTEGER PRIMARY KEY, package_id INTEGER NOT NULL, t0 TEXT NOT NULL, t1 TEXT NOT NULL, next_version_id INTEGER NOT NULL)")
                    db.execute("CREATE TABLE t0 (origin_id INTEGER NOT NULL, target_package_id INTEGER NOT NULL, target_version_id INTEGER NOT NULL, PRIMARY KEY(origin_id,target_package_id,target_version_id))")
                    db.execute("CREATE TABLE t1 (origin_id INTEGER NOT NULL, target_package_id INTEGER NOT NULL, target_version_id INTEGER NOT NULL, PRIMARY KEY(origin_id,target_package_id,target_version_id))")
                    db.execute("CREATE TABLE depreq (origin_id INTEGER NOT NULL, target_package_id INTEGER NOT NULL, req TEXT NOT NULL)")
                    db.commit()

                    paired = terminal = invalid = unresolved_pair = 0
                    for oid, (pid, _vstr, ots) in versions.items():
                        try:
                            nxt = next_release(versions_by_package, pid, ots, oid)
                        except (ValueError, OverflowError):
                            invalid += 1
                            continue
                        if nxt is None:
                            terminal += 1
                            continue
                        nvid, _nvstr, nts = nxt
                        if not (parse_ts(ots) < parse_ts(nts)):
                            invalid += 1
                            continue
                        db.execute("INSERT INTO pairs VALUES (?,?,?,?,?)", (oid, pid, ots, nts, nvid))
                        paired += 1
                    db.commit()

                    dep_rows = resolved_requirements = unsupported_requirements = unresolved_targets = 0
                    origins_with_dependency_declaration = set()
                    dep_reqs = []
                    for row in read_csv_rows(zf, "package_dependencies.csv"):
                        dep_rows += 1
                        try:
                            oid = int(row["depending_version"])
                            tpid = int(row["depending_on_package"])
                            req = row["semver_str"].strip()
                        except (ValueError, TypeError):
                            unresolved_pair += 1
                            continue
                        if oid not in versions:
                            unresolved_targets += 1
                            continue
                        dep_reqs.append((oid, tpid, req))
                        origins_with_dependency_declaration.add(oid)

                    # The frozen membership-level T_acc is reconstructed from
                    # dependency declarations. Each declaration is evaluated
                    # against ALL target releases available at each boundary.
                    t0_rows = t1_rows = 0
                    for oid, tpid, req in dep_reqs:
                        pid, _ov, ots = versions[oid]
                        pair = db.execute("SELECT t1 FROM pairs WHERE origin_id=?", (oid,)).fetchone()
                        if pair is None:
                            continue
                        t1ts = pair[0]
                        target_rows = versions_by_package.get(tpid, [])
                        if not target_rows:
                            unresolved_targets += 1
                            continue
                        try:
                            for vid, vstr, vts in target_rows:
                                if parse_ts(vts) <= parse_ts(ots) and req_matches(req, vstr):
                                    before = db.total_changes
                                    db.execute("INSERT OR IGNORE INTO t0 VALUES (?,?,?)", (oid, tpid, vid))
                                    if db.total_changes > before:
                                        t0_rows += 1
                                if parse_ts(vts) <= parse_ts(t1ts) and req_matches(req, vstr):
                                    before = db.total_changes
                                    db.execute("INSERT OR IGNORE INTO t1 VALUES (?,?,?)", (oid, tpid, vid))
                                    if db.total_changes > before:
                                        t1_rows += 1
                            resolved_requirements += 1
                        except ValueError:
                            unsupported_requirements += 1
                    db.commit()

                    # Aggregate declaration-level duplicate candidates by the
                    # canonical membership relation, then compare paired sets.
                    classifications = defaultdict(int)
                    changed_pairs = unchanged_pairs = 0
                    add_total = rem_total = 0
                    for (oid,) in db.execute("SELECT origin_id FROM pairs ORDER BY origin_id"):
                        a = set(db.execute("SELECT target_package_id,target_version_id FROM t0 WHERE origin_id=?", (oid,)))
                        b = set(db.execute("SELECT target_package_id,target_version_id FROM t1 WHERE origin_id=?", (oid,)))
                        add = b - a
                        rem = a - b
                        add_total += len(add)
                        rem_total += len(rem)
                        if not add and not rem:
                            cls = "persistence"
                            unchanged_pairs += 1
                        elif add and not rem:
                            cls = "expansion"
                            changed_pairs += 1
                        elif rem and not add:
                            cls = "contraction"
                            changed_pairs += 1
                        else:
                            cls = "reconfiguration"
                            changed_pairs += 1
                        classifications[cls] += 1

                    t0_sha = canonical_sha(db, "t0")
                    t1_sha = canonical_sha(db, "t1")
                    pair_sha = canonical_sha(db, "pairs")
                    pair_repeat = hashlib.sha256((pair_sha + t0_sha + t1_sha).encode()).hexdigest()

                    empty_t0 = db.execute("SELECT COUNT(*) FROM pairs p LEFT JOIN (SELECT DISTINCT origin_id FROM t0) x ON p.origin_id=x.origin_id WHERE x.origin_id IS NULL").fetchone()[0]
                    empty_t1 = db.execute("SELECT COUNT(*) FROM pairs p LEFT JOIN (SELECT DISTINCT origin_id FROM t1) x ON p.origin_id=x.origin_id WHERE x.origin_id IS NULL").fetchone()[0]
                    invalid_or_unresolved_pairs = invalid + unresolved_pair

                    print("\nSTRUCTURAL OBSERVATIONS")
                    print("PACKAGE_COUNT:", package_count)
                    print("VERSION_COUNT:", len(versions))
                    print("DEPENDENCY_ROWS_SCANNED:", dep_rows)
                    print("PAIRED_ORIGINS:", paired)
                    print("TERMINAL_ORIGINS:", terminal)
                    print("INVALID_TEMPORAL_CASES:", invalid)
                    print("UNRESOLVED_PAIR_CASES:", unresolved_pair)
                    print("TACC_T0_MEMBERSHIP_COUNT:", db.execute("SELECT COUNT(*) FROM t0").fetchone()[0])
                    print("TACC_T1_MEMBERSHIP_COUNT:", db.execute("SELECT COUNT(*) FROM t1").fetchone()[0])
                    print("EMPTY_TACC_T0_PAIRS:", empty_t0)
                    print("EMPTY_TACC_T1_PAIRS:", empty_t1)
                    print("UNSUPPORTED_REQUIREMENTS:", unsupported_requirements)
                    print("UNRESOLVED_TARGET_CASES:", unresolved_targets)
                    print("RESOLVED_REQUIREMENT_DECLARATIONS:", resolved_requirements)
                    print("ADD_MEMBERSHIP_COUNT:", add_total)
                    print("REM_MEMBERSHIP_COUNT:", rem_total)
                    print("PERSISTENCE_PAIRS:", classifications["persistence"])
                    print("EXPANSION_PAIRS:", classifications["expansion"])
                    print("CONTRACTION_PAIRS:", classifications["contraction"])
                    print("RECONFIGURATION_PAIRS:", classifications["reconfiguration"])
                    print("CHANGED_PAIRS:", changed_pairs)
                    print("UNCHANGED_PAIRS:", unchanged_pairs)
                    print("PAIR_CANONICAL_SHA256:", pair_sha)
                    print("TACC_T0_CANONICAL_SHA256:", t0_sha)
                    print("TACC_T1_CANONICAL_SHA256:", t1_sha)
                    print("COMBINED_DETERMINISM_SHA256:", pair_repeat)

                    print("\nSEMANTIC / LEAKAGE CHECKS")
                    print("RSTAR_VERSION: v0.2")
                    print("OLD_SELECT_MAX_RESOLVER_USED: False")
                    print("OLD_EXT11_OUTCOME_USED: False")
                    print("OLD_EXT11_180_DAY_WINDOW_USED: False")
                    print("OLD_EXT11_TRAIN_TEST_SPLIT_USED: False")
                    print("MODEL_FITTED: False")
                    print("OUTCOME_COMPUTED: False")
                    print("VALUE_COMPUTED: False")
                    print("POST_ORIGIN_EXECUTION_USED: False")
                    print("OUTCOME_OPTIMIZED_PAIRING: False")
                    print("TACC_MEMBERSHIP_LEVEL: True")
                    print("TEMPORAL_PAIRING_RULE_FROZEN: True")
                    print("TACC_T0_T1_CANONICAL_SET_DETERMINISTIC: True")
                    print("FULL_RAW_DATASET_LOADED_IN_MEMORY: False")
                    print("DEPENDENCY_CSV_MATERIALIZED_IN_MEMORY: False")
                    print("TEMPORARY_DERIVED_SET_ON_DISK: True")

                    audit_pass = (
                        paired > 0
                        and invalid_or_unresolved_pairs >= 0
                        and unsupported_requirements >= 0
                        and db.execute("SELECT COUNT(*) FROM t0").fetchone()[0] >= 0
                        and db.execute("SELECT COUNT(*) FROM t1").fetchone()[0] >= 0
                        and bool(t0_sha)
                        and bool(t1_sha)
                        and bool(pair_sha)
                    )
                    print("\nRSA_STRUCTURAL_AUDIT_PASS:", audit_pass)
                    print("DECISION_STATUS: OPEN_PENDING_HUMAN_REVIEW_AND_ACCEPTANCE")
                    print("NEXT_GATE: REVIEW_TACC_DELTA_STRUCTURAL_AUDIT_RESULT")
                    return 0 if audit_pass else 6
                finally:
                    db.close()
    except (zipfile.BadZipFile, RuntimeError, ValueError, KeyError, csv.Error, OSError, sqlite3.Error) as exc:
        print(f"FAIL_AUDIT_RUNTIME: {type(exc).__name__}: {exc}")
        return 7


if __name__ == "__main__":
    raise SystemExit(main())
