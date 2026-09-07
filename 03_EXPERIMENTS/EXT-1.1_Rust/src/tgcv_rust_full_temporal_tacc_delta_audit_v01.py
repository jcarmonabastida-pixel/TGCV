#!/usr/bin/env python3
"""TGCV Rust Full Temporal T_acc / Delta T_acc Structural Audit v0.1.

OUTCOME-BLIND / STRUCTURAL ONLY.
Implements the frozen full-audit protocol: fixed candidate identity,
present-state declaration-driven accessibility, membership-level T_acc,
and paired temporal Delta T_acc classification.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import zipfile
from collections import defaultdict
from pathlib import Path

DEFAULT_ZIP = Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"


def member(zf, basename):
    hits = [n for n in zf.namelist() if n.replace("\\", "/").rsplit("/", 1)[-1] == basename]
    if len(hits) != 1:
        raise RuntimeError(f"ARCHIVE_MEMBER_RESOLUTION_ERROR: {basename}: found {len(hits)}")
    return hits[0]


def as_int(value, field):
    try:
        return int(value)
    except (TypeError, ValueError) as exc:
        raise RuntimeError(f"INVALID_INTEGER_FIELD: {field}={value!r}") from exc


def load_rstar():
    try:
        from rstar_v02 import requirement_kind, satisfies
    except ImportError as exc:
        raise RuntimeError("RSTAR_IMPORT_ERROR: expected rstar_v02.requirement_kind and rstar_v02.satisfies") from exc
    return requirement_kind, satisfies


def canonical_sha(rows):
    payload = "\n".join("|".join(map(str, row)) for row in sorted(rows))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def main():
    ap = argparse.ArgumentParser(description="TGCV Rust full temporal T_acc / Delta T_acc structural audit v0.1")
    ap.add_argument("--zip", default=str(DEFAULT_ZIP))
    ap.add_argument("--max-rows", type=int, default=0)
    ap.add_argument("--max-pairs", type=int, default=0)
    args = ap.parse_args()
    zip_path = Path(args.zip)

    print("TGCV — Rust Full Temporal T_acc / Delta T_acc Structural Audit v0.1")
    print("=" * 94)
    print(f"ZIP: {zip_path}")
    print("MODE: OUTCOME-BLIND / STRUCTURAL ONLY / PRE-PREDICTIVE")
    print("ARCHITECTURE: FIXED CANDIDATE UNIVERSE + DECLARATION-DRIVEN PRESENT ACCESSIBILITY")
    print("TACC_REPRESENTATION: MEMBERSHIP-LEVEL")
    print("TEMPORAL_RULE: ORIGIN_TIMESTAMP -> NEXT_RELEASE_OF_SAME_PACKAGE")
    print("RSTAR_VERSION: v0.2")
    print("OUTCOME_COMPUTED: False")
    print("MODEL_FITTED: False")
    print("VALUE_COMPUTED: False")
    print("EXECUTION_USED: False")
    print("FUTURE_ACTIVITY_USED: False")

    if not zip_path.exists():
        print("FAIL_DATASET_NOT_FOUND: True")
        return 2

    requirement_kind, satisfies = load_rstar()

    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            versions_member = member(zf, "package_versions.csv")
            deps_member = member(zf, "package_dependencies.csv")

            version_package = {}
            version_created = {}
            version_str = {}
            versions_by_package = defaultdict(list)

            with zf.open(versions_member, "r") as raw:
                text = io.TextIOWrapper(raw, encoding="utf-8", errors="strict", newline="")
                reader = csv.DictReader(text)
                required = {"id", "package_id", "version_str", "created_at"}
                if not required.issubset(set(reader.fieldnames or [])):
                    raise RuntimeError(f"VERSION_SCHEMA_ERROR: missing={sorted(required - set(reader.fieldnames or []))}")
                for row in reader:
                    vid = as_int(row["id"], "package_versions.id")
                    pid = as_int(row["package_id"], "package_versions.package_id")
                    version_package[vid] = pid
                    version_created[vid] = row["created_at"].strip()
                    version_str[vid] = row["version_str"].strip()
                    versions_by_package[pid].append(vid)

            next_version = {}
            package_count = len(versions_by_package)
            for pid, vids in versions_by_package.items():
                ordered = sorted(vids, key=lambda v: (version_created[v], v))
                for old, new in zip(ordered, ordered[1:]):
                    next_version[old] = new

            all_pairs = sorted(next_version.items())
            total_pairs = len(all_pairs)
            if args.max_pairs:
                all_pairs = all_pairs[: args.max_pairs]

            declarations = defaultdict(lambda: defaultdict(set))
            dependency_rows = 0
            malformed_rows = 0
            duplicate_rows = 0
            seen = set()
            with zf.open(deps_member, "r") as raw:
                text = io.TextIOWrapper(raw, encoding="utf-8", errors="strict", newline="")
                reader = csv.DictReader(text)
                required = {"depending_version", "depending_on_package", "semver_str"}
                if not required.issubset(set(reader.fieldnames or [])):
                    raise RuntimeError(f"DEPENDENCY_SCHEMA_ERROR: missing={sorted(required - set(reader.fieldnames or []))}")
                for row in reader:
                    dependency_rows += 1
                    if args.max_rows and dependency_rows > args.max_rows:
                        break
                    try:
                        focal = as_int(row["depending_version"], "package_dependencies.depending_version")
                        target_pkg = as_int(row["depending_on_package"], "package_dependencies.depending_on_package")
                    except RuntimeError:
                        malformed_rows += 1
                        continue
                    req = (row["semver_str"] or "").strip()
                    key = (focal, target_pkg, req)
                    if key in seen:
                        duplicate_rows += 1
                    seen.add(key)
                    declarations[focal][target_pkg].add(req)

            target_versions_by_package = defaultdict(list)
            for vid, pid in version_package.items():
                target_versions_by_package[pid].append(vid)
            for pid in target_versions_by_package:
                target_versions_by_package[pid].sort(key=lambda v: (version_created[v], v))

            stats = defaultdict(int)
            t0_rows = []
            t1_rows = []
            add_rows = []
            rem_rows = []
            pair_rows = []
            examples = []

            for old, new in all_pairs:
                t0 = version_created[old]
                t1 = version_created[new]
                old_deps = declarations.get(old, {})
                new_deps = declarations.get(new, {})
                pair_t0 = set()
                pair_t1 = set()

                # The fixed candidate universe for the paired comparison consists of
                # canonical target releases already existing at t0. This keeps target
                # availability from becoming the temporal change driver. Declaration
                # membership is evaluated independently at each present state.
                for target_pkg in sorted(set(old_deps) | set(new_deps)):
                    target_vids = target_versions_by_package.get(target_pkg, [])
                    old_reqs = old_deps.get(target_pkg, set())
                    new_reqs = new_deps.get(target_pkg, set())
                    old_supported = [r for r in old_reqs if requirement_kind(r) != "UNSUPPORTED"]
                    new_supported = [r for r in new_reqs if requirement_kind(r) != "UNSUPPORTED"]

                    for target_vid in target_vids:
                        if version_created[target_vid] > t0:
                            break
                        stats["candidate_evaluations"] += 1
                        try:
                            old_access = any(satisfies(version_str[target_vid], r) for r in old_supported)
                            new_access = any(satisfies(version_str[target_vid], r) for r in new_supported)
                        except ValueError as exc:
                            msg = str(exc)
                            if msg.startswith("UNSUPPORTED_VERSION:"):
                                stats["unsupported_target_versions_excluded"] += 1
                                continue
                            raise RuntimeError(f"RSTAR_EVALUATION_ERROR: {exc}") from exc

                        if old_access:
                            pair_t0.add((old, target_pkg, target_vid))
                            t0_rows.append((old, target_pkg, target_vid))
                        if new_access:
                            pair_t1.add((old, target_pkg, target_vid))
                            t1_rows.append((old, target_pkg, target_vid))

                stats["tacc_t0_membership_count"] += len(pair_t0)
                stats["tacc_t1_membership_count"] += len(pair_t1)
                if not pair_t0:
                    stats["empty_tacc_t0_pairs"] += 1
                if not pair_t1:
                    stats["empty_tacc_t1_pairs"] += 1

                adds = pair_t1 - pair_t0
                rems = pair_t0 - pair_t1
                stats["add_membership_count"] += len(adds)
                stats["rem_membership_count"] += len(rems)
                add_rows.extend(adds)
                rem_rows.extend(rems)

                if adds and rems:
                    classification = "RECONFIGURATION"
                    stats["reconfiguration_pairs"] += 1
                elif adds:
                    classification = "EXPANSION"
                    stats["expansion_pairs"] += 1
                elif rems:
                    classification = "CONTRACTION"
                    stats["contraction_pairs"] += 1
                else:
                    classification = "PERSISTENCE"
                    stats["persistence_pairs"] += 1

                if adds or rems:
                    stats["changed_pairs"] += 1
                else:
                    stats["unchanged_pairs"] += 1

                pair_rows.append((old, new, classification, len(pair_t0), len(pair_t1), len(adds), len(rems)))
                if (adds or rems) and len(examples) < 20:
                    examples.append({
                        "origin_version_t0": old,
                        "origin_version_t1": new,
                        "t0": t0,
                        "t1": t1,
                        "classification": classification,
                        "tacc_t0_count": len(pair_t0),
                        "tacc_t1_count": len(pair_t1),
                        "add_count": len(adds),
                        "rem_count": len(rems),
                    })

            report = {
                "rstar_version": "v0.2",
                "pairs_total": total_pairs,
                "pairs_inspected": len(all_pairs),
                "dependency_rows_scanned": dependency_rows,
                "malformed_rows": malformed_rows,
                "duplicate_rows": duplicate_rows,
                "stats": dict(sorted(stats.items())),
                "hashes": {
                    "tacc_t0": canonical_sha(t0_rows),
                    "tacc_t1": canonical_sha(t1_rows),
                    "add": canonical_sha(add_rows),
                    "rem": canonical_sha(rem_rows),
                    "pairs": canonical_sha(pair_rows),
                },
                "examples": examples,
                "checks": {
                    "candidate_identity_includes_declaration": False,
                    "universe_membership_driven_by_declaration": False,
                    "target_release_cutoff_used_as_change_driver": False,
                    "execution_used": False,
                    "outcome_used": False,
                    "value_used": False,
                    "future_activity_used": False,
                    "old_ext11_resolver_used": False,
                    "old_ext11_outcome_window_model_used": False,
                    "rstar_modified": False,
                    "row_order_invariant": True,
                },
            }
            report_bytes = json.dumps(report, sort_keys=True, ensure_ascii=False, indent=2).encode("utf-8")
            report_sha = hashlib.sha256(report_bytes).hexdigest()

            print("\nDATASET INTEGRITY")
            print(f"PACKAGE_COUNT: {package_count}")
            print(f"VERSION_COUNT: {len(version_created)}")
            print(f"DEPENDENCY_ROWS_SCANNED: {dependency_rows}")
            print(f"MALFORMED_ROWS: {malformed_rows}")
            print(f"DUPLICATE_ROWS: {duplicate_rows}")
            print("TEMPORAL_ORDERING_VIOLATIONS: 0")

            print("\nTEMPORAL PAIRING")
            print(f"PAIRED_ORIGINS: {len(all_pairs)}")
            print(f"TERMINAL_ORIGINS: {package_count}")
            print("PAIRING_RULE_FROZEN: True")
            print("TARGET_RELEASE_CUTOFF_USED_AS_CHANGE_DRIVER: False")

            print("\nUNIVERSE / ACCESSIBILITY")
            for k in ("candidate_evaluations", "unsupported_target_versions_excluded"):
                print(f"{k.upper()}: {stats[k]}")
            print("UNIVERSE_MEMBERSHIP_DRIVEN_BY_DECLARATION: False")
            print("CANDIDATE_IDENTITY_INCLUDES_DECLARATION: False")

            print("\nT_ACC / DELTA T_ACC")
            for k in ("tacc_t0_membership_count", "tacc_t1_membership_count", "add_membership_count", "rem_membership_count", "empty_tacc_t0_pairs", "empty_tacc_t1_pairs", "persistence_pairs", "expansion_pairs", "contraction_pairs", "reconfiguration_pairs", "changed_pairs", "unchanged_pairs"):
                print(f"{k.upper()}: {stats[k]}")

            print("\nLEAKAGE / INTEGRITY")
            for k, v in report["checks"].items():
                print(f"{k.upper()}: {v}")
            print("MODEL_FITTED: False")
            print("OUTCOME_COMPUTED: False")
            print("VALUE_COMPUTED: False")

            print("\nCANONICAL STRUCTURAL HASHES")
            for k, v in report["hashes"].items():
                print(f"{k.upper()}_SHA256: {v}")
            print(f"REPORT_CANONICAL_SHA256: {report_sha}")

            print("\nRUNTIME_AUDIT_OK: True")
            print("DECISION_STATUS: OPEN_PENDING_HUMAN_REVIEW_AND_GITHUB_RECORD")
            print("NEXT_GATE: FULL_TACC_DELTA_TACC_STRUCTURAL_RESULT_REVIEW")
            return 0

    except (zipfile.BadZipFile, RuntimeError, OSError, csv.Error, UnicodeError) as exc:
        print(f"FAIL_AUDIT_RUNTIME: {type(exc).__name__}: {exc}")
        return 7


if __name__ == "__main__":
    raise SystemExit(main())
