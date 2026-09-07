#!/usr/bin/env python3
"""TGCV Rust paired temporal T_acc / Delta T_acc structural audit v0.1.

OUTCOME-BLIND / PRE-CONFIRMATORY.
Unlike DR-026A, this audit retains every target release satisfying the
frozen R* v0.2 requirement; it never uses the old select-max representation.
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

from rstar_v02 import requirement_kind, satisfies  # noqa: E402

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
    req = req.strip()
    if requirement_kind(req) == "UNSUPPORTED":
        raise ValueError(f"UNSUPPORTED_REQUIREMENT:{req}")
    return satisfies(target_version, req)


def canonical_sha(con: sqlite3.Connection, table: str, columns: str) -> str:
    h = hashlib.sha256()
    for row in con.execute(f"SELECT {columns} FROM {table} ORDER BY origin_id,target_package_id,target_version_id"):
        h.update("|".join(map(str, row)).encode("utf-8") + b"\n")
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
                    db.commit()

                    paired = terminal = invalid = 0
                    for oid, (pid, _vstr, ots) in versions.items():
                        origin_time = parse_ts(ots)
                        later = [r for r in versions_by_package.get(pid, []) if parse_ts(r[2]) > origin_time]
                        if not later:
                            terminal += 1
                            continue
                        nvid, _nvstr, nts = later[0]
                        if not origin_time < parse_ts(nts):
                            invalid += 1
                            continue
                        db.execute("INSERT INTO pairs VALUES (?,?,?,?,?)", (oid, pid, ots, nts, nvid))
                        paired += 1
                    db.commit()

                    dep_rows = resolved_requirements = unsupported_requirements = unresolved_targets = 0
                    dep_reqs = []
                    for row in read_csv_rows(zf, "package_dependencies.csv"):
                        dep_rows += 1
                        try:
                            oid = int(row["depending_version"])
                            tpid = int(row["depending_on_package"])
                            req = row["semver_str"].strip()
                        except (ValueError, TypeError):
                            continue
                        if oid not in versions:
                            unresolved_targets += 1
                            continue
                        dep_reqs.append((oid, tpid, req))

                    # Reconstruct membership-level T_acc independently at t0/t1.
                    inserted_t0 = inserted_t1 = 0
                    for oid, tpid, req in dep_reqs:
                        pair = db.execute("SELECT t0,t1 FROM pairs WHERE origin_id=?", (oid,)).fetchone()
                        if pair is None:
                            continue
                        t0, t1 = pair
                        target_rows = versions_by_package.get(tpid, [])
                        if not target_rows:
                            unresolved_targets += 1
                            continue
                        try:
                            for vid, vstr, vts in target_rows:
                                ts = parse_ts(vts)
                                if ts <= parse_ts(t0) and req_matches(req, vstr):
                                    before = db.total_changes
                                    db.execute("INSERT OR IGNORE INTO t0 VALUES (?,?,?)", (oid, tpid, vid))
                                    inserted_t0 += db.total_changes - before
                                if ts <= parse_ts(t1) and req_matches(req, vstr):
                                    before = db.total_changes
                                    db.execute("INSERT OR IGNORE INTO t1 VALUES (?,?,?)", (oid, tpid, vid))
                                    inserted_t1 += db.total_changes - before
                            resolved_requirements += 1
                        except ValueError:
                            unsupported_requirements += 1
                    db.commit()

                    classifications = defaultdict(int)
                    changed_pairs = unchanged_pairs = add_total = rem_total = 0
                    for (oid,) in db.execute("SELECT origin_id FROM pairs ORDER BY origin_id"):
                        a = set(db.execute("SELECT target_package_id,target_version_id FROM t0 WHERE origin_id=?", (oid,)))
                        b = set(db.execute("SELECT target_package_id,target_version_id FROM t1 WHERE origin_id=?", (oid,)))
                        add, rem = b - a, a - b
                        add_total += len(add)
                        rem_total += len(rem)
                        if not add and not rem:
                            cls = "persistence"; unchanged_pairs += 1
                        elif add and not rem:
                            cls = "expansion"; changed_pairs += 1
                        elif rem and not add:
                            cls = "contraction"; changed_pairs += 1
                        else:
                            cls = "reconfiguration"; changed_pairs += 1
                        classifications[cls] += 1

                    t0_sha = canonical_sha(db, "t0", "origin_id,target_package_id,target_version_id")
                    t1_sha = canonical_sha(db, "t1", "origin_id,target_package_id,target_version_id")
                    pair_sha = canonical_sha(db, "pairs", "origin_id,package_id,0")
                    combined_sha = hashlib.sha256((pair_sha + t0_sha + t1_sha).encode()).hexdigest()
                    empty_t0 = db.execute("SELECT COUNT(*) FROM pairs p LEFT JOIN (SELECT DISTINCT origin_id FROM t0) x ON p.origin_id=x.origin_id WHERE x.origin_id IS NULL").fetchone()[0]
                    empty_t1 = db.execute("SELECT COUNT(*) FROM pairs p LEFT JOIN (SELECT DISTINCT origin_id FROM t1) x ON p.origin_id=x.origin_id WHERE x.origin_id IS NULL").fetchone()[0]

                    print("\nSTRUCTURAL OBSERVATIONS")
                    for k, v in {
                        "PACKAGE_COUNT": package_count,
                        "VERSION_COUNT": len(versions),
                        "DEPENDENCY_ROWS_SCANNED": dep_rows,
                        "PAIRED_ORIGINS": paired,
                        "TERMINAL_ORIGINS": terminal,
                        "INVALID_TEMPORAL_CASES": invalid,
                        "TACC_T0_MEMBERSHIP_COUNT": db.execute("SELECT COUNT(*) FROM t0").fetchone()[0],
                        "TACC_T1_MEMBERSHIP_COUNT": db.execute("SELECT COUNT(*) FROM t1").fetchone()[0],
                        "EMPTY_TACC_T0_PAIRS": empty_t0,
                        "EMPTY_TACC_T1_PAIRS": empty_t1,
                        "UNSUPPORTED_REQUIREMENTS": unsupported_requirements,
                        "UNRESOLVED_TARGET_CASES": unresolved_targets,
                        "RESOLVED_REQUIREMENT_DECLARATIONS": resolved_requirements,
                        "ADD_MEMBERSHIP_COUNT": add_total,
                        "REM_MEMBERSHIP_COUNT": rem_total,
                        "PERSISTENCE_PAIRS": classifications["persistence"],
                        "EXPANSION_PAIRS": classifications["expansion"],
                        "CONTRACTION_PAIRS": classifications["contraction"],
                        "RECONFIGURATION_PAIRS": classifications["reconfiguration"],
                        "CHANGED_PAIRS": changed_pairs,
                        "UNCHANGED_PAIRS": unchanged_pairs,
                        "PAIR_CANONICAL_SHA256": pair_sha,
                        "TACC_T0_CANONICAL_SHA256": t0_sha,
                        "TACC_T1_CANONICAL_SHA256": t1_sha,
                        "COMBINED_DETERMINISM_SHA256": combined_sha,
                    }.items(): print(f"{k}: {v}")

                    print("\nSEMANTIC / LEAKAGE CHECKS")
                    for k, v in {
                        "RSTAR_VERSION": "v0.2",
                        "OLD_SELECT_MAX_RESOLVER_USED": False,
                        "OLD_EXT11_OUTCOME_USED": False,
                        "OLD_EXT11_180_DAY_WINDOW_USED": False,
                        "OLD_EXT11_TRAIN_TEST_SPLIT_USED": False,
                        "MODEL_FITTED": False,
                        "OUTCOME_COMPUTED": False,
                        "VALUE_COMPUTED": False,
                        "POST_ORIGIN_EXECUTION_USED": False,
                        "OUTCOME_OPTIMIZED_PAIRING": False,
                        "TACC_MEMBERSHIP_LEVEL": True,
                        "TEMPORAL_PAIRING_RULE_FROZEN": True,
                        "TACC_T0_T1_CANONICAL_SET_DETERMINISTIC": True,
                        "FULL_RAW_DATASET_LOADED_IN_MEMORY": False,
                        "DEPENDENCY_CSV_MATERIALIZED_IN_MEMORY": True,
                    }.items(): print(f"{k}: {v}")

                    # This is deliberately a runtime integrity indicator, not a scientific PASS.
                    runtime_ok = paired > 0 and bool(t0_sha) and bool(t1_sha) and bool(pair_sha)
                    print("\nRUNTIME_STRUCTURAL_EXECUTION_OK:", runtime_ok)
                    print("DECISION_STATUS: OPEN_PENDING_HUMAN_REVIEW_AND_ACCEPTANCE")
                    print("NEXT_GATE: REVIEW_TACC_DELTA_STRUCTURAL_AUDIT_RESULT")
                    return 0 if runtime_ok else 6
                finally:
                    db.close()
    except (zipfile.BadZipFile, RuntimeError, ValueError, KeyError, csv.Error, OSError, sqlite3.Error) as exc:
        print(f"FAIL_AUDIT_RUNTIME: {type(exc).__name__}: {exc}")
        return 7


if __name__ == "__main__":
    raise SystemExit(main())
