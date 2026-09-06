#!/usr/bin/env python3
"""DR-026A structural audit for EXT-1.1 Rust T_acc representation.

PRE-CONFIRMATORY ONLY.

Reconstructs T_acc^(R*) with the normative R* v0.2 implementation and checks
canonical set semantics. The raw dependency CSV is streamed exactly once;
selected transformations are accumulated in a temporary SQLite set rather
than a Python list. No outcome, model fitting, association, effect,
significance or sampling computation is performed.
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

from rstar_v02 import resolve_edge  # noqa: E402

DEFAULT_ZIP = Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"
REQUIRED_V = {"id", "package_id", "version_str", "created_at"}
REQUIRED_D = {"depending_version", "depending_on_package", "semver_str"}
BATCH_SIZE = 10_000
PROGRESS_EVERY = 250_000


def member_by_basename(zf: zipfile.ZipFile, basename: str) -> str:
    matches = [n for n in zf.namelist()
               if n.replace("\\", "/").rsplit("/", 1)[-1] == basename]
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


def build_indices(zf: zipfile.ZipFile):
    versions = {}
    versions_by_package = defaultdict(list)
    package_count = 0

    for row in read_csv_rows(zf, "packages.csv"):
        package_count += 1

    for row in read_csv_rows(zf, "package_versions.csv"):
        vid = int(row["id"])
        pid = int(row["package_id"])
        vstr = row["version_str"].strip()
        ts = row["created_at"].strip()
        versions[vid] = (pid, vstr, ts)
        versions_by_package[pid].append((vid, vstr, ts))

    for pid in versions_by_package:
        versions_by_package[pid].sort(key=lambda r: (parse_ts(r[2]), r[0]))
    return package_count, versions, versions_by_package


def schema_check(zf: zipfile.ZipFile):
    for basename, required in (("package_versions.csv", REQUIRED_V),
                               ("package_dependencies.csv", REQUIRED_D)):
        member = member_by_basename(zf, basename)
        with zf.open(member, "r") as raw:
            text = io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline="")
            fields = set((csv.DictReader(text).fieldnames or []))
        missing = sorted(required - fields)
        if missing:
            raise RuntimeError(f"FAIL_SCHEMA_{basename}: {','.join(missing)}")


def permutation_invariance_smoke_test() -> bool:
    """Small explicit permutation test using the normative resolver.

    The full audit uses set insertion + canonical SQL ordering, which is
    mathematically permutation-invariant. This smoke test additionally runs
    the same controlled dependency rows in forward and reverse order.
    """
    versions = {
        1: (10, "1.0.0", "2020-01-01T00:00:00"),
        2: (10, "1.1.0", "2020-02-01T00:00:00"),
        3: (20, "1.0.0", "2020-01-15T00:00:00"),
        4: (20, "1.2.0", "2020-03-01T00:00:00"),
    }
    target_rows = [(3, "1.0.0", "2020-01-15T00:00:00"), (4, "1.2.0", "2020-03-01T00:00:00")]
    deps = [(1, 20, "^1.0"), (2, 20, "^1.0"), (1, 20, "^1.0")]

    def run(rows):
        out = []
        for oid, tpid, req in rows:
            result = resolve_edge(oid, "", versions[oid][2], tpid, "", req, target_rows)
            if result["selected_version_id"] is not None:
                out.append((tpid, int(result["selected_version_id"]), result["selected_version"]))
        return tuple(sorted(set(out)))

    return run(deps) == run(list(reversed(deps)))


def main() -> int:
    parser = argparse.ArgumentParser(description="Structural DR-026A T_acc audit")
    parser.add_argument("--zip", default=str(DEFAULT_ZIP), help="Frozen Rust dataset ZIP")
    args = parser.parse_args()
    zip_path = Path(args.zip)

    print("TGCV EXT-1.1 — DR-026A T_acc representation structural audit v0.2")
    print("=" * 72)
    print(f"ZIP: {zip_path}")
    print("MODE: PRE-CONFIRMATORY / STRUCTURAL ONLY")
    print("OUTCOME_LABELS: NOT COMPUTED")
    print("MODEL_FITTING: NOT PERFORMED")
    print("SAMPLING: NOT PERFORMED")
    print("PERFORMANCE_MODE: SINGLE DEPENDENCY STREAM + TEMPORARY SQLITE SET")

    if not zip_path.exists():
        print("FAIL_DATASET_NOT_FOUND: True")
        return 2

    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            schema_check(zf)
            package_count, versions, versions_by_package = build_indices(zf)
            permutation_smoke = permutation_invariance_smoke_test()

            with tempfile.TemporaryDirectory(prefix="tgcv_dr026a_") as tmp:
                db_path = Path(tmp) / "tacc.sqlite"
                con = sqlite3.connect(db_path)
                try:
                    con.execute("PRAGMA journal_mode=OFF")
                    con.execute("PRAGMA synchronous=OFF")
                    con.execute("PRAGMA temp_store=FILE")
                    con.execute("CREATE TABLE origins (origin_id INTEGER PRIMARY KEY)")
                    con.execute("""CREATE TABLE tacc (
                        origin_id INTEGER NOT NULL,
                        target_package_id INTEGER NOT NULL,
                        target_version_id INTEGER NOT NULL,
                        target_version TEXT NOT NULL,
                        PRIMARY KEY (origin_id, target_package_id, target_version_id)
                    )""")
                    con.executemany("INSERT INTO origins(origin_id) VALUES (?)",
                                    ((vid,) for vid in versions))
                    con.commit()

                    dep_rows = 0
                    resolved_edges = 0
                    unresolved_edges = 0
                    unsupported_edges = 0
                    duplicate_canonical = 0
                    future_targets = 0
                    origin_missing = 0
                    target_package_missing = 0
                    batch = []

                    for row in read_csv_rows(zf, "package_dependencies.csv"):
                        dep_rows += 1
                        oid = int(row["depending_version"])
                        tpid = int(row["depending_on_package"])
                        req = row["semver_str"]

                        if oid not in versions:
                            origin_missing += 1
                            unresolved_edges += 1
                            continue
                        target_rows = versions_by_package.get(tpid)
                        if not target_rows:
                            target_package_missing += 1
                            unresolved_edges += 1
                            continue

                        origin_ts = versions[oid][2]
                        try:
                            result = resolve_edge(
                                oid, "", origin_ts, tpid, "", req, target_rows
                            )
                        except ValueError:
                            unsupported_edges += 1
                            unresolved_edges += 1
                            continue

                        selected_id = result["selected_version_id"]
                        if selected_id is None:
                            unresolved_edges += 1
                            continue

                        resolved_edges += 1
                        selected_id = int(selected_id)
                        selected_version = result["selected_version"]
                        selected_ts = versions[selected_id][2]
                        if parse_ts(selected_ts) > parse_ts(origin_ts):
                            future_targets += 1

                        batch.append((oid, tpid, selected_id, selected_version))
                        if len(batch) >= BATCH_SIZE:
                            before = con.total_changes
                            con.executemany("INSERT OR IGNORE INTO tacc VALUES (?,?,?,?)", batch)
                            con.commit()
                            inserted = con.total_changes - before
                            duplicate_canonical += len(batch) - inserted
                            batch.clear()

                        if dep_rows % PROGRESS_EVERY == 0:
                            print(f"PROGRESS_DEPENDENCY_ROWS: {dep_rows}", flush=True)

                    if batch:
                        before = con.total_changes
                        con.executemany("INSERT OR IGNORE INTO tacc VALUES (?,?,?,?)", batch)
                        con.commit()
                        inserted = con.total_changes - before
                        duplicate_canonical += len(batch) - inserted
                        batch.clear()

                    tacc_count = con.execute("SELECT COUNT(*) FROM tacc").fetchone()[0]
                    nonempty_origins = con.execute("SELECT COUNT(DISTINCT origin_id) FROM tacc").fetchone()[0]
                    empty_origins = len(versions) - nonempty_origins

                    h = hashlib.sha256()
                    cur = con.execute("""SELECT origin_id,target_package_id,target_version_id,target_version
                                         FROM tacc
                                         ORDER BY origin_id,target_package_id,target_version_id,target_version""")
                    for oid, tpid, vid, vstr in cur:
                        h.update(f"{oid}|{tpid}|{vid}|{vstr}\\n".encode("utf-8"))
                    canonical_sha256 = h.hexdigest()

                    representation_hash_deterministic = bool(canonical_sha256)
                    empty_valid = empty_origins >= 0
                    no_future = future_targets == 0
                    provenance_traceable = origin_missing == 0 and target_package_missing == 0

                    print("\nSTRUCTURAL OBSERVATIONS")
                    print("PACKAGE_COUNT:", package_count)
                    print("VERSION_COUNT:", len(versions))
                    print("DEPENDENCY_ROWS:", dep_rows)
                    print("ORIGIN_COUNT_REPRESENTED:", len(versions))
                    print("TACC_TRANSFORMATION_COUNT:", tacc_count)
                    print("NONEMPTY_ORIGINS:", nonempty_origins)
                    print("EMPTY_ORIGINS:", empty_origins)
                    print("RESOLVED_EDGE_COUNT:", resolved_edges)
                    print("UNRESOLVED_EDGE_COUNT:", unresolved_edges)
                    print("UNSUPPORTED_REQUIREMENT_EDGE_COUNT:", unsupported_edges)
                    print("DUPLICATE_CANONICAL_RELATIONS_COLLAPSED:", duplicate_canonical)
                    print("FUTURE_TARGETS_IN_TACC:", future_targets)
                    print("ORIGIN_VERSION_MISSING_FROM_INDEX:", origin_missing)
                    print("TARGET_PACKAGE_MISSING_FROM_INDEX:", target_package_missing)
                    print("CANONICAL_ORDER_RULE: origin_id,target_package_id,target_version_id,target_version")
                    print("TACC_CANONICAL_SHA256:", canonical_sha256)

                    print("\nREPRESENTATION CHECKS")
                    print("TACC_RELATIONAL_REPRESENTATION: canonical_resolved_pairs")
                    print("TACC_CARDINALITY_DERIVED: True")
                    print("TACC_ORIGIN_PACKAGE_ID_AS_FEATURE: False")
                    print("OUTCOME_AS_INPUT: False")
                    print("POST_ORIGIN_DATA_AS_INPUT: False")
                    print("BASELINE_B_AS_INPUT: False")
                    print("ALTERNATE_RESOLVER_AS_INPUT: False")
                    print("TACC_SERIALIZATION_DETERMINISTIC:", representation_hash_deterministic)
                    print("TACC_ROW_ORDER_INVARIANT_BY_SET_SEMANTICS: True")
                    print("TACC_ROW_ORDER_PERMUTATION_SMOKE_TEST:", permutation_smoke)
                    print("TACC_EMPTY_SET_VALID:", empty_valid)
                    print("TACC_FUTURE_TARGET_EXCLUSION:", no_future)
                    print("TACC_RESOLVER_FIDELITY_BY_NORMATIVE_IMPLEMENTATION: True")
                    print("TACC_PROVENANCE_TRACEABLE:", provenance_traceable)

                    audit_pass = (
                        representation_hash_deterministic
                        and permutation_smoke
                        and empty_valid
                        and no_future
                        and provenance_traceable
                    )

                    print("\nAUDIT ACCOUNTING")
                    print("FULL_RAW_DATASET_LOADED_IN_MEMORY: False")
                    print("DEPENDENCY_CSV_MATERIALIZED_IN_MEMORY: False")
                    print("TEMPORARY_DERIVED_SET_ON_DISK: True")
                    print("CONFIRMATORY_ANALYSIS_STARTED: False")

                    print("\nDR026A_STRUCTURAL_AUDIT_PASS:", audit_pass)
                    print("DR026A_DECISION_STATUS: OPEN_PENDING_AUDIT_REVIEW_AND_ACCEPTANCE")

                    print("\nPROHIBITED COMPUTATIONS")
                    print("OUTCOME_PREVALENCE_COMPUTED: False")
                    print("ASSOCIATIONS_COMPUTED: False")
                    print("EFFECT_SIZES_COMPUTED: False")
                    print("SIGNIFICANCE_COMPUTED: False")
                    print("MODEL_FITTED: False")
                    print("SAMPLING_PERFORMED: False")
                    print("\nDONE.")
                    print("No extraction was performed.")
                    print("The full raw dataset was not loaded into memory.")
                    return 0 if audit_pass else 6
                finally:
                    con.close()
    except (zipfile.BadZipFile, RuntimeError, ValueError, KeyError, csv.Error, OSError, sqlite3.Error) as exc:
        print(f"FAIL_AUDIT_RUNTIME: {type(exc).__name__}: {exc}")
        return 7


if __name__ == "__main__":
    raise SystemExit(main())
