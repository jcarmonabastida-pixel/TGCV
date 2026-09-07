#!/usr/bin/env python3
"""TGCV Rust Reachability / Trajectory Dataset Feasibility Audit v0.1.

OUTCOME-BLIND / SCHEMA-ONLY / PRE-IMPLEMENTATION.
This audit inspects whether the frozen Rust dataset contains enough structural
information to reconstruct transition sequences, Reach, and Trajectory.
It does not compute T_acc, Delta T_acc, outcomes, values, or models.
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import io
import json
import zipfile
from pathlib import Path

DEFAULT_ZIP = Path.home() / "Downloads" / "rust_repos_2022_09_07.zip"
EXPECTED = {
    "packages.csv": ["id", "source_id", "insource_id", "name", "url_id", "repo_id", "created_at"],
    "package_versions.csv": ["id", "package_id", "version_str", "created_at"],
    "package_dependencies.csv": ["depending_version", "depending_on_package", "semver_str"],
}


def resolve_member(zf: zipfile.ZipFile, basename: str) -> str:
    hits = [n for n in zf.namelist() if n.replace("\\", "/").rsplit("/", 1)[-1] == basename]
    if len(hits) != 1:
        raise RuntimeError(f"ARCHIVE_MEMBER_RESOLUTION_ERROR: {basename}: found {len(hits)}")
    return hits[0]


def canonical_sha(payload) -> str:
    raw = json.dumps(payload, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def inspect_csv(zf, member_name, expected_fields, sample_rows):
    with zf.open(member_name, "r") as raw:
        text = io.TextIOWrapper(raw, encoding="utf-8", errors="strict", newline="")
        reader = csv.DictReader(text)
        fields = list(reader.fieldnames or [])
        missing = [f for f in expected_fields if f not in fields]
        if missing:
            raise RuntimeError(f"SCHEMA_ERROR: {member_name}: missing={missing}")
        count = 0
        samples = []
        nonempty = {f: 0 for f in fields}
        for row in reader:
            count += 1
            if len(samples) < sample_rows:
                samples.append({f: row.get(f, "") for f in fields})
            for f in fields:
                if (row.get(f) or "").strip() != "":
                    nonempty[f] += 1
        return {"fields": fields, "row_count": count, "nonempty": nonempty, "samples": samples}


def main():
    ap = argparse.ArgumentParser(description="TGCV Rust Reachability / Trajectory Dataset Feasibility Audit v0.1")
    ap.add_argument("--zip", default=str(DEFAULT_ZIP))
    ap.add_argument("--sample-rows", type=int, default=5)
    args = ap.parse_args()
    zip_path = Path(args.zip)

    print("TGCV — Rust Reachability / Trajectory Dataset Feasibility Audit v0.1")
    print("=" * 88)
    print(f"ZIP: {zip_path}")
    print("MODE: OUTCOME-BLIND / SCHEMA-ONLY / PRE-IMPLEMENTATION")
    print("TACC_COMPUTED: False")
    print("DELTA_TACC_COMPUTED: False")
    print("REACH_COMPUTED: False")
    print("TRAJECTORY_COMPUTED: False")
    print("OUTCOME_COMPUTED: False")
    print("MODEL_FITTED: False")
    print("VALUE_COMPUTED: False")

    if not zip_path.exists():
        print("FAIL_DATASET_NOT_FOUND: True")
        return 2

    try:
        with zipfile.ZipFile(zip_path, "r") as zf:
            inventory = {}
            for basename, expected_fields in EXPECTED.items():
                m = resolve_member(zf, basename)
                inventory[basename] = inspect_csv(zf, m, expected_fields, args.sample_rows)

            pkg = inventory["packages.csv"]
            ver = inventory["package_versions.csv"]
            dep = inventory["package_dependencies.csv"]

            # Structural capabilities are inferred only from observable schema.
            # Names such as 'depending_version' are treated as identity/edge keys,
            # never as evidence of execution or realized transition.
            fields = {k: v["fields"] for k, v in inventory.items()}
            dep_fields = set(dep["fields"])
            ver_fields = set(ver["fields"])
            pkg_fields = set(pkg["fields"])

            capabilities = {
                "focal_package_identity": "id" in pkg_fields,
                "focal_version_identity": "id" in ver_fields and "package_id" in ver_fields,
                "focal_temporal_order": "created_at" in ver_fields,
                "dependency_edge_identity": {"depending_version", "depending_on_package"}.issubset(dep_fields),
                "dependency_constraint_semantics_field": "semver_str" in dep_fields,
                "target_version_identity": "id" in ver_fields,
                "target_version_temporal_availability": "created_at" in ver_fields,
                "explicit_execution_event": False,
                "explicit_dependency_resolution_event": False,
                "explicit_runtime_transition_event": False,
                "explicit_success_or_failure_event": False,
                "explicit_state_snapshot_beyond_release_metadata": False,
                "explicit_trajectory_identifier": False,
                "explicit_path_sequence_identifier": False,
                "explicit_edge_activation_timestamp": False,
            }

            reconstructability = {
                "S_t_focal_version": "R1_RECONSTRUCTABLE",
                "candidate_dependency_edge": "R1_RECONSTRUCTABLE",
                "transition_semantics": "R2_PARTIAL",
                "execution_sequence": "R3_PROXY_ONLY_OR_NOT_RECONSTRUCTABLE",
                "Reach": "R2_PARTIAL_PENDING_SEQUENCE_SEMANTICS",
                "Trajectory": "R2_PARTIAL_PENDING_SEQUENCE_SEMANTICS",
            }

            # Explicitly list what the dataset can and cannot support without
            # importing post-hoc or outcome-derived semantics.
            admissible_structural_evidence = [
                "package and package-version identity",
                "version chronology",
                "dependency edge identity",
                "declared SemVer constraint string",
                "target package/version identity and release chronology",
            ]
            absent_structural_evidence = [
                "actual dependency-resolution event",
                "executed dependency transition",
                "runtime state transition",
                "ordered execution sequence",
                "trajectory/path event log",
                "explicit reachability event or resolved successor state",
            ]

            report = {
                "archive": str(zip_path),
                "mode": "OUTCOME-BLIND / SCHEMA-ONLY / PRE-IMPLEMENTATION",
                "inventory": inventory,
                "capabilities": capabilities,
                "reconstructability": reconstructability,
                "admissible_structural_evidence": admissible_structural_evidence,
                "absent_structural_evidence": absent_structural_evidence,
                "checks": {
                    "accessibility_semantics_inferred": False,
                    "tacc_computed": False,
                    "delta_tacc_computed": False,
                    "reach_computed": False,
                    "trajectory_computed": False,
                    "execution_used": False,
                    "outcome_used": False,
                    "value_used": False,
                    "future_activity_used": False,
                    "post_hoc_semantics_used": False,
                    "old_ext11_predictive_protocol_used": False,
                    "rstar_modified": False,
                },
            }

            print("\nSCHEMA INVENTORY")
            for name, item in inventory.items():
                print(f"{name}: {item['row_count']} rows; fields={len(item['fields'])}")
                print("  " + ", ".join(item["fields"]))

            print("\nSTRUCTURAL CAPABILITIES")
            for k, v in capabilities.items():
                print(f"{k.upper()}: {v}")

            print("\nRECONSTRUCTABILITY LEVELS")
            for k, v in reconstructability.items():
                print(f"{k.upper()}: {v}")

            print("\nADMISSIBLE STRUCTURAL EVIDENCE")
            for x in admissible_structural_evidence:
                print(f"- {x}")

            print("\nABSENT STRUCTURAL EVIDENCE")
            for x in absent_structural_evidence:
                print(f"- {x}")

            print("\nINTEGRITY / LEAKAGE")
            for k, v in report["checks"].items():
                print(f"{k.upper()}: {v}")

            report_sha = canonical_sha(report)
            print(f"\nREPORT_CANONICAL_SHA256: {report_sha}")
            print("\nRUNTIME_AUDIT_OK: True")
            print("DECISION_STATUS: OPEN_PENDING_HUMAN_REVIEW_AND_GITHUB_RECORD")
            print("NEXT_GATE: REACHABILITY_TRAJECTORY_RECONSTRUCTABILITY_DECISION")
            return 0

    except (zipfile.BadZipFile, RuntimeError, OSError, csv.Error, UnicodeError) as exc:
        print(f"FAIL_AUDIT_RUNTIME: {type(exc).__name__}: {exc}")
        return 7


if __name__ == "__main__":
    raise SystemExit(main())
