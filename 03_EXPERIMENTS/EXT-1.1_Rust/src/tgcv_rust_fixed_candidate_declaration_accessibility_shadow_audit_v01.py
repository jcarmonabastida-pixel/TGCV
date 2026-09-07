#!/usr/bin/env python3
"""TGCV Rust Fixed-Candidate Declaration-Driven Accessibility Shadow Audit v0.1.

OUTCOME-BLIND / STRUCTURAL / SHADOW ONLY.
No T_acc, Delta T_acc, outcome, model, value, execution, or future activity.
R* v0.2 is frozen and used only through its existing API.
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


def main():
    ap = argparse.ArgumentParser(description="TGCV Rust fixed-candidate declaration-driven accessibility shadow audit v0.1")
    ap.add_argument("--zip", default=str(DEFAULT_ZIP))
    ap.add_argument("--max-rows", type=int, default=0, help="0 = all dependency rows")
    ap.add_argument("--max-pairs", type=int, default=0, help="0 = all successive focal-version pairs")
    args = ap.parse_args()
    zip_path = Path(args.zip)

    print("TGCV — Rust Fixed-Candidate Declaration-Driven Accessibility Shadow Audit v0.1")
    print("=" * 94)
    print(f"ZIP: {zip_path}")
    print("MODE: OUTCOME-BLIND / STRUCTURAL / SHADOW ONLY")
    print("ARCHITECTURE: FIXED CANDIDATE UNIVERSE + DECLARATION-DRIVEN PRESENT ACCESSIBILITY")
    print("RSTAR_VERSION: v0.2")
    print("TACC_COMPUTED: False")
    print("DELTA_TACC_COMPUTED: False")
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
                fields = set(reader.fieldnames or [])
                if not required.issubset(fields):
                    raise RuntimeError(f"VERSION_SCHEMA_ERROR: missing={sorted(required - fields)}")
                for row in reader:
                    vid = as_int(row["id"], "package_versions.id")
                    pid = as_int(row["package_id"], "package_versions.package_id")
                    version_package[vid] = pid
                    version_str[vid] = row["version_str"].strip()
                    version_created[vid] = row["created_at"].strip()
                    versions_by_package[pid].append(vid)

            next_version = {}
            total_pairs = 0
            for pid, vids in versions_by_package.items():
                ordered = sorted(vids, key=lambda v: (version_created[v], v))
                for old, new in zip(ordered, ordered[1:]):
                    next_version[old] = new
                    total_pairs += 1

            if args.max_pairs:
                selected = set(sorted(next_version)[: args.max_pairs])
                next_version = {k: v for k, v in next_version.items() if k in selected}

            declarations = defaultdict(lambda: defaultdict(set))
            dependency_rows = 0
            malformed_rows = 0
            duplicate_rows = 0
            seen_rows = set()
            with zf.open(deps_member, "r") as raw:
                text = io.TextIOWrapper(raw, encoding="utf-8", errors="strict", newline="")
                reader = csv.DictReader(text)
                required = {"depending_version", "depending_on_package", "semver_str"}
                fields = set(reader.fieldnames or [])
                if not required.issubset(fields):
                    raise RuntimeError(f"DEPENDENCY_SCHEMA_ERROR: missing={sorted(required - fields)}")
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
                    if key in seen_rows:
                        duplicate_rows += 1
                    seen_rows.add(key)
                    declarations[focal][target_pkg].add(req)

            # Fixed candidate target universe: all canonical target releases in the
            # dataset, independently of focal declarations. For this shadow isolation
            # test, only candidates whose target release existed by t0 are evaluated.
            target_versions_by_package = defaultdict(list)
            for vid, pid in version_package.items():
                target_versions_by_package[pid].append(vid)
            for pid in target_versions_by_package:
                target_versions_by_package[pid].sort(key=lambda v: (version_created[v], v))

            stats = defaultdict(int)
            examples = []

            for old, new in sorted(next_version.items()):
                old_deps = declarations.get(old, {})
                new_deps = declarations.get(new, {})
                for target_pkg in sorted(set(old_deps) | set(new_deps)):
                    old_reqs = old_deps.get(target_pkg, set())
                    new_reqs = new_deps.get(target_pkg, set())
                    if old_reqs == new_reqs:
                        continue

                    stats["declaration_changed_focal_target_pairs"] += 1
                    if old_reqs and not new_reqs:
                        stats["declaration_removed_target_pairs"] += 1
                    elif new_reqs and not old_reqs:
                        stats["declaration_added_target_pairs"] += 1
                    else:
                        stats["declaration_changed_target_pairs"] += 1

                    # Isolate declaration variation: target release must already
                    # exist at t0. Thus target availability cannot create the change.
                    for target_vid in target_versions_by_package.get(target_pkg, []):
                        if version_created[target_vid] > version_created[old]:
                            break

                        old_supported = [r for r in old_reqs if requirement_kind(r) != "UNSUPPORTED"]
                        new_supported = [r for r in new_reqs if requirement_kind(r) != "UNSUPPORTED"]

                        # A target version outside the frozen R* v0.2 SemVer grammar
                        # is explicitly unsupported and excluded, never coerced.
                        try:
                            old_access = any(satisfies(version_str[target_vid], r) for r in old_supported)
                            new_access = any(satisfies(version_str[target_vid], r) for r in new_supported)
                        except ValueError as exc:
                            message = str(exc)
                            if message.startswith("UNSUPPORTED_VERSION:"):
                                stats["unsupported_target_versions_excluded"] += 1
                                continue
                            raise RuntimeError(f"RSTAR_EVALUATION_ERROR: {exc}") from exc

                        stats["fixed_candidates_tested"] += 1
                        if old_access and not new_access:
                            stats["accessibility_1_to_0"] += 1
                        elif not old_access and new_access:
                            stats["accessibility_0_to_1"] += 1
                        elif old_access and new_access:
                            stats["accessibility_persistent_1"] += 1
                        else:
                            stats["accessibility_persistent_0"] += 1

                        if old_access != new_access:
                            stats["declaration_driven_accessibility_changes"] += 1
                            if len(examples) < 20:
                                examples.append({
                                    "origin_version_t0": old,
                                    "origin_version_t1": new,
                                    "target_package_id": target_pkg,
                                    "target_version_id": target_vid,
                                    "target_version": version_str[target_vid],
                                    "target_version_created_at": version_created[target_vid],
                                    "t0": version_created[old],
                                    "t1": version_created[new],
                                    "t0_requirements": sorted(old_reqs),
                                    "t1_requirements": sorted(new_reqs),
                                    "access_t0": old_access,
                                    "access_t1": new_access,
                                })

            report = {
                "zip": str(zip_path),
                "rstar_version": "v0.2",
                "pairs_total": total_pairs,
                "pairs_inspected": len(next_version),
                "dependency_rows_scanned": dependency_rows,
                "malformed_rows": malformed_rows,
                "duplicate_rows": duplicate_rows,
                "stats": dict(sorted(stats.items())),
                "examples": examples,
                "checks": {
                    "candidate_identity_includes_declaration": False,
                    "candidate_universe_membership_driven_by_declaration": False,
                    "target_release_cutoff_used_as_change_driver": False,
                    "unsupported_target_versions_silently_coerced": False,
                    "execution_used": False,
                    "outcome_used": False,
                    "value_used": False,
                    "future_activity_used": False,
                    "rstar_modified": False,
                    "tacc_computed": False,
                    "delta_tacc_computed": False,
                },
            }
            canonical = json.dumps(report, sort_keys=True, ensure_ascii=False, indent=2).encode("utf-8")
            report_sha = hashlib.sha256(canonical).hexdigest()

            print("\nTEMPORAL / DECLARATION BASE")
            print(f"FOCAL_VERSION_COUNT: {len(version_created)}")
            print(f"PACKAGE_COUNT: {len(versions_by_package)}")
            print(f"SUCCESSIVE_FOCAL_PAIRS_TOTAL: {total_pairs}")
            print(f"SUCCESSIVE_FOCAL_PAIRS_INSPECTED: {len(next_version)}")
            print(f"DEPENDENCY_ROWS_SCANNED: {dependency_rows}")
            print(f"MALFORMED_ROWS: {malformed_rows}")
            print(f"DUPLICATE_ROWS: {duplicate_rows}")

            print("\nDECLARATION VARIATION SHADOW")
            for k in (
                "declaration_changed_focal_target_pairs",
                "declaration_removed_target_pairs",
                "declaration_added_target_pairs",
                "declaration_changed_target_pairs",
                "fixed_candidates_tested",
                "unsupported_target_versions_excluded",
                "accessibility_1_to_0",
                "accessibility_0_to_1",
                "accessibility_persistent_1",
                "accessibility_persistent_0",
                "declaration_driven_accessibility_changes",
            ):
                print(f"{k.upper()}: {stats[k]}")

            print("\nIDENTITY / UNIVERSE FIREWALL")
            print("CANDIDATE_IDENTITY_INCLUDES_DECLARATION: False")
            print("CANDIDATE_UNIVERSE_MEMBERSHIP_DRIVEN_BY_DECLARATION: False")
            print("TARGET_RELEASE_CUTOFF_USED_AS_CHANGE_DRIVER: False")
            print("UNSUPPORTED_TARGET_VERSIONS_SILENTLY_COERCED: False")

            print("\nLEAKAGE / INTEGRITY")
            print("EXECUTION_USED: False")
            print("OUTCOME_USED: False")
            print("VALUE_USED: False")
            print("FUTURE_ACTIVITY_USED: False")
            print("RSTAR_MODIFIED: False")
            print("TACC_COMPUTED: False")
            print("DELTA_TACC_COMPUTED: False")
            print("MODEL_FITTED: False")

            print("\nACCESSIBILITY-CHANGING EXAMPLES (MAX 20)")
            for example in examples:
                print(json.dumps(example, ensure_ascii=False, sort_keys=True))

            print(f"REPORT_CANONICAL_SHA256: {report_sha}")
            print("\nRUNTIME_AUDIT_OK: True")
            print("DECISION_STATUS: OPEN_PENDING_HUMAN_REVIEW_AND_GITHUB_RECORD")
            print("NEXT_GATE: FIXED_IDENTITY_ACCESSIBILITY_DECISION")
            return 0

    except (zipfile.BadZipFile, RuntimeError, OSError, csv.Error, UnicodeError) as exc:
        print(f"FAIL_AUDIT_RUNTIME: {type(exc).__name__}: {exc}")
        return 7


if __name__ == "__main__":
    raise SystemExit(main())
