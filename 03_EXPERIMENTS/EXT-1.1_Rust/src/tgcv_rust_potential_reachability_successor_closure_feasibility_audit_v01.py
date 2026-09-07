#!/usr/bin/env python3
"""TGCV Rust Potential Reachability Successor / Finite Closure Feasibility Audit v0.1.

Outcome-blind technical shadow audit. Does NOT compute Reach, Delta Reach,
Trajectory, Outcome, Value, or fit a model.
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
EXPECTED = {
    "packages.csv": ["id", "name", "created_at"],
    "package_versions.csv": ["id", "package_id", "version_str", "created_at"],
    "package_dependencies.csv": ["depending_version", "depending_on_package", "semver_str"],
}


def resolve_member(zf, basename):
    hits = [n for n in zf.namelist() if n.replace("\\", "/").rsplit("/", 1)[-1] == basename]
    if len(hits) != 1:
        raise RuntimeError(f"ARCHIVE_MEMBER_RESOLUTION_ERROR:{basename}:{len(hits)}")
    return hits[0]


def read_rows(zf, member):
    with zf.open(member, "r") as raw:
        text = io.TextIOWrapper(raw, encoding="utf-8", errors="strict", newline="")
        reader = csv.DictReader(text)
        fields = list(reader.fieldnames or [])
        rows = list(reader)
    return fields, rows


def sha(obj):
    return hashlib.sha256(json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--zip", default=str(DEFAULT_ZIP))
    args = ap.parse_args()
    p = Path(args.zip)
    print("TGCV — Rust Potential Reachability Successor / Finite Closure Feasibility Audit v0.1")
    print("=" * 94)
    print(f"ZIP: {p}")
    print("MODE: OUTCOME-BLIND / STRUCTURAL SHADOW / PRE-REACH")
    for k, v in [("TACC_COMPUTED",False),("DELTA_TACC_COMPUTED",False),("REACH_COMPUTED",False),("TRAJECTORY_COMPUTED",False),("OUTCOME_COMPUTED",False),("MODEL_FITTED",False),("VALUE_COMPUTED",False),("EXECUTION_USED",False),("FUTURE_ACTIVITY_USED",False)]: print(f"{k}: {v}")
    if not p.exists():
        print("FAIL_DATASET_NOT_FOUND: True"); return 2
    try:
        with zipfile.ZipFile(p) as zf:
            members = {n: resolve_member(zf, n) for n in EXPECTED}
            inv = {}
            for n, req in EXPECTED.items():
                fields, rows = read_rows(zf, members[n])
                miss = [x for x in req if x not in fields]
                if miss: raise RuntimeError(f"SCHEMA_ERROR:{n}:missing={miss}")
                inv[n] = {"fields": fields, "rows": len(rows)}

            pk_fields, pk = read_rows(zf, members["packages.csv"])
            v_fields, versions = read_rows(zf, members["package_versions.csv"])
            d_fields, deps = read_rows(zf, members["package_dependencies.csv"])

            version_by_id = {r["id"]: r for r in versions}
            package_by_id = {r["id"]: r for r in pk}
            bad_version_refs = sum(1 for r in deps if r.get("depending_version") not in version_by_id)
            bad_package_refs = sum(1 for r in deps if r.get("depending_on_package") not in package_by_id)
            missing_semver = sum(1 for r in deps if not (r.get("semver_str") or "").strip())

            dep_pairs = Counter((r.get("depending_version"), r.get("depending_on_package")) for r in deps)
            duplicate_edge_rows = sum(c - 1 for c in dep_pairs.values() if c > 1)

            # Each dependency declaration can deterministically identify a structural
            # edge from focal version to target package. It cannot, by itself, identify
            # a realized target version or execution event.
            edge_identity_ok = bad_version_refs == 0 and bad_package_refs == 0
            successor_a = edge_identity_ok and missing_semver == 0

            # A finite candidate boundary is available: the finite package-version and
            # dependency tables. No recursive candidates are invented here.
            finite_boundary = len(versions) > 0 and len(deps) > 0

            # Detect graph properties relevant to closure implementation. This is a
            # feasibility audit only; no closure is computed.
            adjacency = defaultdict(set)
            for r in deps:
                a, b = r.get("depending_version"), r.get("depending_on_package")
                if a in version_by_id and b in package_by_id:
                    adjacency[a].add(b)
            edge_count = sum(len(v) for v in adjacency.values())
            focal_versions_with_edges = len(adjacency)
            self_like = sum(1 for a, bs in adjacency.items() if a in bs)

            report = {
                "inventory": inv,
                "integrity": {
                    "invalid_dependency_version_refs": bad_version_refs,
                    "invalid_dependency_package_refs": bad_package_refs,
                    "missing_semver": missing_semver,
                    "duplicate_edge_rows": duplicate_edge_rows,
                },
                "successor_feasibility": {
                    "configuration_successor_identity": successor_a,
                    "package_version_successor_identity": False,
                    "execution_successor": False,
                    "finite_candidate_boundary": finite_boundary,
                    "recursive_candidates_invented": False,
                    "cycles_detectable_structurally": True,
                    "deterministic_structural_edge_index": edge_identity_ok,
                },
                "graph_observations": {
                    "structural_dependency_edges_indexed": edge_count,
                    "focal_versions_with_dependency_edges": focal_versions_with_edges,
                    "self_like_edges": self_like,
                },
                "reach_status": "NOT_COMPUTED",
                "trajectory_status": "BLOCKED_NO_EXECUTION_SEQUENCE",
                "checks": {
                    "accessibility_semantics_recomputed": False,
                    "tacc_computed": False,
                    "delta_tacc_computed": False,
                    "reach_computed": False,
                    "trajectory_computed": False,
                    "execution_used": False,
                    "outcome_used": False,
                    "value_used": False,
                    "future_activity_used": False,
                    "post_hoc_semantics_used": False,
                    "rstar_modified": False,
                },
            }

            print("\nDATASET INTEGRITY")
            for k,v in report["integrity"].items(): print(f"{k.upper()}: {v}")
            print("\nSUCCESSOR / CLOSURE FEASIBILITY")
            for k,v in report["successor_feasibility"].items(): print(f"{k.upper()}: {v}")
            print("\nGRAPH STRUCTURAL OBSERVATIONS")
            for k,v in report["graph_observations"].items(): print(f"{k.upper()}: {v}")
            print("\nINTERPRETATION FIREWALL")
            print("CONFIGURATION_SUCCESSOR_IS_EXECUTION: False")
            print("PACKAGE_VERSION_SUCCESSOR_IS_EXECUTION: False")
            print("REALIZED_RUNTIME_TRAJECTORY_RECONSTRUCTABLE: False")
            print("REACH_CLOSURE_COMPUTED: False")
            print("\nINTEGRITY / LEAKAGE")
            for k,v in report["checks"].items(): print(f"{k.upper()}: {v}")
            print(f"\nREPORT_CANONICAL_SHA256: {sha(report)}")
            print("\nRUNTIME_AUDIT_OK: True")
            print("DECISION_STATUS: OPEN_PENDING_HUMAN_REVIEW_AND_GITHUB_RECORD")
            print("NEXT_GATE: SUCCESSOR_CLOSURE_FEASIBILITY_DECISION")
            return 0
    except (zipfile.BadZipFile, RuntimeError, OSError, csv.Error, UnicodeError) as exc:
        print(f"FAIL_AUDIT_RUNTIME: {type(exc).__name__}: {exc}"); return 7

if __name__ == "__main__": raise SystemExit(main())
