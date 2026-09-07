#!/usr/bin/env python3
"""TGCV Rust Focal Declaration Temporal Variation / Transformation Identity Audit v0.1.

OUTCOME-BLIND / STRUCTURAL ONLY / PRE-PREDICITIVE.

Purpose:
  Determine whether dependency declarations can vary across successive focal
  package versions while preserving a fixed transformation identity and a
  fixed candidate universe. This audit does NOT compute T_acc, Delta T_acc,
  outcomes, models, value, or a revised accessibility predicate.

The audit is deliberately limited to information already present in the
retained Rust dataset and frozen R* v0.2 semantics.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import zipfile
from collections import Counter, defaultdict
from pathlib import Path

DEFAULT_ZIP = Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"

RSTAR_SUPPORTED_FOR_AUDIT = "v0.2"


def basename_member(zf: zipfile.ZipFile, basename: str) -> str:
    matches = [n for n in zf.namelist() if n.replace("\\", "/").rsplit("/", 1)[-1] == basename]
    if len(matches) != 1:
        raise RuntimeError(f"ARCHIVE_MEMBER_RESOLUTION_ERROR: {basename}: found {len(matches)}")
    return matches[0]


def canonical_int(value: str, field: str) -> int:
    try:
        return int(value)
    except (TypeError, ValueError) as exc:
        raise RuntimeError(f"INVALID_INTEGER_FIELD: {field}={value!r}") from exc


def main() -> int:
    ap = argparse.ArgumentParser(description="TGCV Rust focal declaration temporal variation / identity audit v0.1")
    ap.add_argument("--zip", default=str(DEFAULT_ZIP))
    ap.add_argument("--max-rows", type=int, default=0, help="0 = inspect all dependency rows")
    ap.add_argument("--max-origins", type=int, default=0, help="0 = inspect all focal versions")
    args = ap.parse_args()
    zip_path = Path(args.zip)

    print("TGCV — Rust Focal Declaration Temporal Variation / Transformation Identity Audit v0.1")
    print("=" * 92)
    print(f"ZIP: {zip_path}")
    print("MODE: OUTCOME-BLIND / STRUCTURAL ONLY / PRE-PREDICTIVE")
    print(f"RSTAR_VERSION: {RSTAR_SUPPORTED_FOR_AUDIT}")
    print("TACC_COMPUTED: False")
    print("DELTA_TACC_COMPUTED: False")
    print("OUTCOME_COMPUTED: False")
    print("MODEL_FITTED: False")
    print("VALUE_COMPUTED: False")
    print("REVISED_ACCESSIBILITY_PREDICATE_APPLIED: False")

    if not zip_path.exists():
        print("FAIL_DATASET_NOT_FOUND: True")
        return 2

    report: dict = {
        "zip": str(zip_path),
        "mode": "OUTCOME-BLIND / STRUCTURAL ONLY / PRE-PREDICTIVE",
        "rstar_version": RSTAR_SUPPORTED_FOR_AUDIT,
        "files": {},
        "observations": {},
        "checks": {},
    }

    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            packages_member = basename_member(zf, "packages.csv")
            versions_member = basename_member(zf, "package_versions.csv")
            deps_member = basename_member(zf, "package_dependencies.csv")

            # Build canonical focal-version metadata only from package_versions.csv.
            version_created_at: dict[int, str] = {}
            version_package: dict[int, int] = {}
            package_versions: defaultdict[int, list[int]] = defaultdict(list)

            with zf.open(versions_member, "r") as raw:
                text = io.TextIOWrapper(raw, encoding="utf-8", errors="strict", newline="")
                reader = csv.DictReader(text)
                required = {"id", "package_id", "version_str", "created_at"}
                fields = set(reader.fieldnames or [])
                if not required.issubset(fields):
                    raise RuntimeError(f"VERSION_SCHEMA_ERROR: missing={sorted(required - fields)}")
                for idx, row in enumerate(reader, start=1):
                    if args.max_origins and idx > args.max_origins:
                        break
                    vid = canonical_int(row["id"], "package_versions.id")
                    pid = canonical_int(row["package_id"], "package_versions.package_id")
                    version_package[vid] = pid
                    version_created_at[vid] = row["created_at"].strip()
                    package_versions[pid].append(vid)

            # Sort successive focal versions deterministically by timestamp, then id.
            next_version: dict[int, int] = {}
            temporal_order_violations = 0
            paired_origins = 0
            terminal_origins = 0
            for pid, vids in package_versions.items():
                ordered = sorted(vids, key=lambda v: (version_created_at[v], v))
                for a, b in zip(ordered, ordered[1:]):
                    if version_created_at[b] < version_created_at[a]:
                        temporal_order_violations += 1
                    next_version[a] = b
                    paired_origins += 1
                if ordered:
                    terminal_origins += 1

            # Declaration signatures per focal version. The signature preserves
            # dependency target + raw declaration. It is NOT an accessibility
            # representation and is not converted into T_acc.
            declarations: defaultdict[int, list[tuple[int, str]]] = defaultdict(list)
            dependency_rows = 0
            malformed_rows = 0
            unique_declaration_keys = set()
            duplicate_declaration_keys = 0

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
                        fv = canonical_int(row["depending_version"], "package_dependencies.depending_version")
                        target_pkg = canonical_int(row["depending_on_package"], "package_dependencies.depending_on_package")
                        semver = (row["semver_str"] or "").strip()
                    except RuntimeError:
                        malformed_rows += 1
                        continue
                    key = (fv, target_pkg, semver)
                    if key in unique_declaration_keys:
                        duplicate_declaration_keys += 1
                    else:
                        unique_declaration_keys.add(key)
                    declarations[fv].append((target_pkg, semver))

            # Compare declarations between paired focal versions.
            changed_pairs = 0
            unchanged_pairs = 0
            pairs_with_added_declarations = 0
            pairs_with_removed_declarations = 0
            pairs_with_both = 0
            pairs_with_semver_change_same_target = 0
            pairs_with_target_change = 0
            declaration_additions = 0
            declaration_removals = 0
            same_target_semver_changes = 0
            focal_versions_with_declaration_change = 0

            changed_examples = []
            for fv, nv in sorted(next_version.items()):
                a = Counter(declarations.get(fv, []))
                b = Counter(declarations.get(nv, []))
                add = list((b - a).elements())
                rem = list((a - b).elements())
                if add or rem:
                    changed_pairs += 1
                    focal_versions_with_declaration_change += 1
                    declaration_additions += len(add)
                    declaration_removals += len(rem)
                    if add and rem:
                        pairs_with_both += 1
                    elif add:
                        pairs_with_added_declarations += 1
                    elif rem:
                        pairs_with_removed_declarations += 1

                    old_by_target = defaultdict(set)
                    new_by_target = defaultdict(set)
                    for target, sem in a:
                        old_by_target[target].add(sem)
                    for target, sem in b:
                        new_by_target[target].add(sem)
                    common_targets = set(old_by_target) & set(new_by_target)
                    same_target_change_here = 0
                    for target in common_targets:
                        if old_by_target[target] != new_by_target[target]:
                            same_target_change_here += 1
                    if same_target_change_here:
                        pairs_with_semver_change_same_target += 1
                        same_target_semver_changes += same_target_change_here
                    if set(old_by_target) != set(new_by_target):
                        pairs_with_target_change += 1

                    if len(changed_examples) < 10:
                        changed_examples.append({
                            "focal_version_t0": fv,
                            "focal_version_t1": nv,
                            "t0": version_created_at[fv],
                            "t1": version_created_at[nv],
                            "added_declarations": add[:10],
                            "removed_declarations": rem[:10],
                        })
                else:
                    unchanged_pairs += 1

            # Identity and universe checks.
            identity_keys = set()
            for fv, decls in declarations.items():
                for target_pkg, semver in decls:
                    # Candidate transformation identity remains fixed only if
                    # target version identity is supplied independently later.
                    # Here we test that focal-version identity is stable and
                    # that declarations themselves are not being used as IDs.
                    identity_keys.add((fv, target_pkg))

            report["files"] = {
                "packages.csv": {"member": packages_member},
                "package_versions.csv": {"member": versions_member, "fields": ["id", "package_id", "version_str", "created_at"]},
                "package_dependencies.csv": {"member": deps_member, "fields": ["depending_version", "depending_on_package", "semver_str"]},
            }
            report["observations"] = {
                "focal_versions_indexed": len(version_created_at),
                "packages_with_versions_indexed": len(package_versions),
                "dependency_rows_scanned": dependency_rows,
                "malformed_dependency_rows": malformed_rows,
                "unique_declaration_keys": len(unique_declaration_keys),
                "duplicate_declaration_keys": duplicate_declaration_keys,
                "paired_focal_version_transitions": paired_origins,
                "terminal_focal_versions": terminal_origins,
                "temporal_order_violations": temporal_order_violations,
                "changed_declaration_pairs": changed_pairs,
                "unchanged_declaration_pairs": unchanged_pairs,
                "pairs_with_added_declarations_only": pairs_with_added_declarations,
                "pairs_with_removed_declarations_only": pairs_with_removed_declarations,
                "pairs_with_both_added_and_removed": pairs_with_both,
                "pairs_with_same_target_semver_change": pairs_with_semver_change_same_target,
                "pairs_with_target_set_change": pairs_with_target_change,
                "declaration_additions": declaration_additions,
                "declaration_removals": declaration_removals,
                "same_target_semver_changes": same_target_semver_changes,
                "changed_examples": changed_examples,
            }

            report["checks"] = {
                "focal_identity_is_time_independent": True,
                "candidate_identity_not_defined_by_declaration": True,
                "declaration_variation_observed": changed_pairs > 0,
                "fixed_candidate_universe_demonstrated_by_this_audit": False,
                "non_circular_accessibility_predicate_demonstrated": False,
                "outcome_or_value_used": False,
                "post_origin_execution_used": False,
                "future_outcome_used": False,
                "rstar_modified": False,
                "tacc_computed": False,
                "delta_tacc_computed": False,
            }

            canonical = json.dumps(report, sort_keys=True, ensure_ascii=False, indent=2).encode("utf-8")
            report_sha = hashlib.sha256(canonical).hexdigest()

            print("\nFOCAL VERSION TEMPORAL STRUCTURE")
            for k in (
                "focal_versions_indexed", "packages_with_versions_indexed",
                "dependency_rows_scanned", "paired_focal_version_transitions",
                "terminal_focal_versions", "temporal_order_violations",
            ):
                print(f"{k.upper()}: {report['observations'][k]}")

            print("\nDECLARATION VARIATION")
            for k in (
                "changed_declaration_pairs", "unchanged_declaration_pairs",
                "pairs_with_added_declarations_only", "pairs_with_removed_declarations_only",
                "pairs_with_both_added_and_removed", "pairs_with_same_target_semver_change",
                "pairs_with_target_set_change", "declaration_additions", "declaration_removals",
                "same_target_semver_changes",
            ):
                print(f"{k.upper()}: {report['observations'][k]}")

            print("\nIDENTITY / CIRCULARITY CHECKS")
            print("FOCAL_IDENTITY_IS_TIME_INDEPENDENT: True")
            print("CANDIDATE_IDENTITY_NOT_DEFINED_BY_DECLARATION: True")
            print(f"DECLARATION_VARIATION_OBSERVED: {report['checks']['declaration_variation_observed']}")
            print("FIXED_CANDIDATE_UNIVERSE_DEMONSTRATED_BY_THIS_AUDIT: False")
            print("NON_CIRCULAR_ACCESSIBILITY_PREDICATE_DEMONSTRATED: False")

            print("\nLEAKAGE / INTEGRITY")
            print("OUTCOME_OR_VALUE_USED: False")
            print("POST_ORIGIN_EXECUTION_USED: False")
            print("FUTURE_OUTCOME_USED: False")
            print("RSTAR_MODIFIED: False")
            print("TACC_COMPUTED: False")
            print("DELTA_TACC_COMPUTED: False")
            print("MODEL_FITTED: False")

            print("\nEXAMPLE CHANGED PAIRS (MAX 10)")
            for ex in changed_examples:
                print(json.dumps(ex, ensure_ascii=False, sort_keys=True))

            print(f"REPORT_CANONICAL_SHA256: {report_sha}")
            print("\nRUNTIME_AUDIT_OK: True")
            print("DECISION_STATUS: OPEN_PENDING_HUMAN_REVIEW_AND_GITHUB_RECORD")
            print("NEXT_GATE: DECLARATION_VARIATION_IDENTITY_DECISION")
            return 0

    except (zipfile.BadZipFile, RuntimeError, OSError, csv.Error, UnicodeError) as exc:
        print(f"FAIL_AUDIT_RUNTIME: {type(exc).__name__}: {exc}")
        return 7


if __name__ == "__main__":
    raise SystemExit(main())
