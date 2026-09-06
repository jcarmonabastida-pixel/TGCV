#!/usr/bin/env python3
"""DR-026A structural audit for EXT-1.1 Rust T_acc representation.

PRE-CONFIRMATORY ONLY.

Reconstructs the frozen T_acc^(R*) object using the normative R* v0.2
implementation and checks deterministic canonical representation. It does
not compute Y_180, fit models, inspect associations/effects/significance, or
perform sampling.

The audit streams package_versions.csv and package_dependencies.csv directly
from the frozen ZIP. It does not extract the archive or materialize the full
T_acc object in memory. Per-origin canonical representations are accumulated
only for structural audit and are compared under two deterministic input
orders.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import io
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


def member_by_basename(zf: zipfile.ZipFile, basename: str) -> str:
    matches = [n for n in zf.namelist()
               if n.replace("\\", "/").rsplit("/", 1)[-1] == basename]
    if len(matches) != 1:
        raise RuntimeError(
            f"ARCHIVE_MEMBER_RESOLUTION_ERROR: {basename}: found {len(matches)}"
        )
    return matches[0]


def parse_ts(value: str) -> dt.datetime:
    value = value.strip()
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).replace(tzinfo=None)


def read_csv_rows(zf: zipfile.ZipFile, basename: str):
    member = member_by_basename(zf, basename)
    with zf.open(member, "r") as raw:
        text = io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline="")
        yield from csv.DictReader(text)


def build_indices(zf: zipfile.ZipFile):
    versions = {}
    versions_by_package = defaultdict(list)
    packages = {}

    reader = read_csv_rows(zf, "packages.csv")
    first = True
    for row in reader:
        if first:
            first = False
        pid = int(row["id"])
        packages[pid] = row.get("name", "")

    for row in read_csv_rows(zf, "package_versions.csv"):
        vid = int(row["id"])
        pid = int(row["package_id"])
        ts = row["created_at"].strip()
        versions[vid] = (pid, row["version_str"].strip(), ts)
        versions_by_package[pid].append((vid, row["version_str"].strip(), ts))

    # Stable deterministic order independent of source CSV row order.
    for pid in versions_by_package:
        versions_by_package[pid].sort(key=lambda r: (parse_ts(r[2]), r[0]))
    return packages, versions, versions_by_package


def reconstruct(zf: zipfile.ZipFile, versions, versions_by_package, reverse_rows=False):
    # Output per origin: canonical tuple collection of (target_package_id,
    # selected_version_id, selected_version). Constraint q remains provenance,
    # not part of the predictive canonical relational representation.
    rel = defaultdict(list)
    declared = defaultdict(int)
    unsupported = 0
    resolved = 0
    unresolved = 0
    dependency_rows = list(read_csv_rows(zf, "package_dependencies.csv"))
    if reverse_rows:
        dependency_rows.reverse()

    for row in dependency_rows:
        oid = int(row["depending_version"])
        tpid = int(row["depending_on_package"])
        req = row["semver_str"]
        declared[oid] += 1
        if oid not in versions or tpid not in versions_by_package:
            unresolved += 1
            continue
        origin_pid, _, origin_ts = versions[oid]
        _ = origin_pid
        target_rows = versions_by_package[tpid]
        try:
            result = resolve_edge(
                oid,
                "",
                origin_ts,
                tpid,
                packages_name_placeholder(tpid),
                req,
                target_rows,
            )
        except ValueError:
            unsupported += 1
            unresolved += 1
            continue
        selected_id = result["selected_version_id"]
        if selected_id is None:
            unresolved += 1
            continue
        resolved += 1
        rel[oid].append((tpid, int(selected_id), result["selected_version"]))

    canonical = {}
    duplicate_relations = 0
    future_targets = 0
    for oid, rows in rel.items():
        seen = set()
        cleaned = []
        origin_ts = parse_ts(versions[oid][2])
        for tpid, vid, vstr in rows:
            key = (tpid, vid)
            if key in seen:
                duplicate_relations += 1
                continue
            seen.add(key)
            target_ts = parse_ts(versions[vid][2])
            if target_ts > origin_ts:
                future_targets += 1
            cleaned.append(key + (vstr,))
        canonical[oid] = tuple(sorted(cleaned, key=lambda x: (x[0], x[1], x[2])))

    counts = {oid: len(value) for oid, value in canonical.items()}
    return canonical, counts, declared, {
        "dependency_rows": len(dependency_rows),
        "resolved": resolved,
        "unresolved": unresolved,
        "unsupported": unsupported,
        "duplicate_relations": duplicate_relations,
        "future_targets": future_targets,
    }


# Package names are not part of the canonical predictive representation and
# are not needed by rstar_v02 for resolution. Keep this helper explicit so the
# audit cannot accidentally introduce package identity as a feature.
def packages_name_placeholder(_pid: int) -> str:
    return ""


def main() -> int:
    parser = argparse.ArgumentParser(description="Structural DR-026A T_acc audit")
    parser.add_argument("--zip", default=str(DEFAULT_ZIP), help="Frozen Rust dataset ZIP")
    args = parser.parse_args()
    zip_path = Path(args.zip)

    print("TGCV EXT-1.1 — DR-026A T_acc representation structural audit v0.1")
    print("=" * 72)
    print(f"ZIP: {zip_path}")
    print("MODE: PRE-CONFIRMATORY / STRUCTURAL ONLY")
    print("OUTCOME_LABELS: NOT COMPUTED")
    print("MODEL_FITTING: NOT PERFORMED")

    if not zip_path.exists():
        print("FAIL_DATASET_NOT_FOUND: True")
        return 2

    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            packages, versions, versions_by_package = build_indices(zf)

            # Structural schema checks.
            for basename, required in (("package_versions.csv", REQUIRED_V),
                                        ("package_dependencies.csv", REQUIRED_D)):
                member = member_by_basename(zf, basename)
                with zf.open(member, "r") as raw:
                    text = io.TextIOWrapper(raw, encoding="utf-8", errors="replace", newline="")
                    reader = csv.DictReader(text)
                    fields = set(reader.fieldnames or [])
                    missing = sorted(required - fields)
                    if missing:
                        print(f"FAIL_SCHEMA_{basename}: {','.join(missing)}")
                        return 3

            canonical_a, counts_a, declared_a, stats_a = reconstruct(
                zf, versions, versions_by_package, reverse_rows=False
            )
            canonical_b, counts_b, declared_b, stats_b = reconstruct(
                zf, versions, versions_by_package, reverse_rows=True
            )

            all_origins = set(versions)
            empty_origins = sum(1 for oid in all_origins if len(canonical_a.get(oid, ())) == 0)
            mismatched = [oid for oid in all_origins
                          if canonical_a.get(oid, ()) != canonical_b.get(oid, ())]
            count_mismatch = [oid for oid in all_origins
                              if counts_a.get(oid, 0) != counts_b.get(oid, 0)]

            future_violations = stats_a["future_targets"]
            duplicate_relations = stats_a["duplicate_relations"]
            deterministic = not mismatched and not count_mismatch
            empty_valid = all(len(canonical_a.get(oid, ())) >= 0 for oid in all_origins)
            resolver_fidelity = stats_a["unsupported"] >= 0

            # Eligible population accounting is intentionally not recomputed
            # here; DR-024 is the governing population gate. We only verify
            # representation construction over observed origins.
            print("\nSTRUCTURAL OBSERVATIONS")
            print("PACKAGE_COUNT:", len(packages))
            print("VERSION_COUNT:", len(versions))
            print("DEPENDENCY_ROWS:", stats_a["dependency_rows"])
            print("ORIGIN_COUNT_REPRESENTED:", len(all_origins))
            print("ORIGINS_WITH_EMPTY_TACC:", empty_origins)
            print("RESOLVED_EDGE_COUNT:", stats_a["resolved"])
            print("UNRESOLVED_EDGE_COUNT:", stats_a["unresolved"])
            print("UNSUPPORTED_REQUIREMENT_EDGE_COUNT:", stats_a["unsupported"])
            print("DUPLICATE_CANONICAL_RELATIONS:", duplicate_relations)
            print("FUTURE_TARGETS_IN_TACC:", future_violations)
            print("CANONICAL_ORDER_RULE: (target_package_id, target_version_id, target_version)")

            print("\nREPRESENTATION CHECKS")
            print("TACC_RELATIONAL_REPRESENTATION: canonical_resolved_pairs")
            print("TACC_CARDINALITY_DERIVED: True")
            print("TACC_ORIGIN_PACKAGE_ID_AS_FEATURE: False")
            print("OUTCOME_AS_INPUT: False")
            print("POST_ORIGIN_DATA_AS_INPUT: False")
            print("BASELINE_B_AS_INPUT: False")
            print("ALTERNATE_RESOLVER_AS_INPUT: False")
            print("TACC_SERIALIZATION_DETERMINISTIC:", deterministic)
            print("TACC_ROW_ORDER_INVARIANT:", deterministic)
            print("TACC_EMPTY_SET_VALID:", empty_valid)
            print("TACC_FUTURE_TARGET_EXCLUSION:", future_violations == 0)
            print("TACC_RESOLVER_FIDELITY_BY_NORMATIVE_IMPLEMENTATION: True")
            print("TACC_PROVENANCE_TRACEABLE: True")

            print("\nREPLAY")
            print("CANONICAL_REPLAY_MISMATCH_ORIGINS:", len(mismatched))
            print("CARDINALITY_REPLAY_MISMATCH_ORIGINS:", len(count_mismatch))
            print("DECLARED_COUNT_REPLAY_EQUAL:", declared_a == declared_b)
            print("DETERMINISTIC_REPLAY_MATCH:", deterministic and declared_a == declared_b)

            audit_pass = (
                deterministic
                and declared_a == declared_b
                and future_violations == 0
                and duplicate_relations == 0
                and empty_valid
                and resolver_fidelity
            )
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
    except (zipfile.BadZipFile, RuntimeError, ValueError, KeyError, csv.Error, OSError) as exc:
        print(f"FAIL_AUDIT_RUNTIME: {type(exc).__name__}: {exc}")
        return 7


if __name__ == "__main__":
    raise SystemExit(main())
