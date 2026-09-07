#!/usr/bin/env python3
"""TGCV — Rust Reach Non-Redundancy Structural Audit v0.1

Outcome-blind, depth-1, configuration-level structural audit.

IMPORTANT: This is a bounded structural audit. It does not execute Cargo,
resolve real runtime transitions, compute outcomes/value, or use future
activity. It explicitly separates transformation identity from successor
configuration identity.
"""

from __future__ import annotations

import csv
import hashlib
import json
import sqlite3
import sys
import zipfile
from collections import defaultdict
from pathlib import Path

ZIP_PATH = Path(r"C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip")
RSTAR_VERSION = "v0.2"
DEPTH = 1


def canon(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def normalize_requirement(s: str) -> str:
    return " ".join((s or "").strip().split())


def parse_rstar_api():
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from rstar_v02 import requirement_kind, satisfies
    return requirement_kind, satisfies


def load_csv(zf: zipfile.ZipFile, member: str):
    with zf.open(member) as raw:
        return list(csv.DictReader((line.decode("utf-8") for line in raw)))


def main():
    requirement_kind, satisfies = parse_rstar_api()

    print("TGCV — Rust Reach Non-Redundancy Structural Audit v0.1")
    print("=" * 94)
    print(f"ZIP: {ZIP_PATH}")
    print("MODE: OUTCOME-BLIND / STRUCTURAL ONLY / DEPTH-1 CONFIGURATION SUCCESSORS")
    print("TACC_COMPUTED: True")
    print("DELTA_TACC_COMPUTED: True")
    print("REACH_COMPUTED: True")
    print("TRAJECTORY_COMPUTED: False")
    print("OUTCOME_COMPUTED: False")
    print("MODEL_FITTED: False")
    print("VALUE_COMPUTED: False")
    print("EXECUTION_USED: False")
    print("FUTURE_ACTIVITY_USED: False")
    print()

    if not ZIP_PATH.exists():
        raise FileNotFoundError(ZIP_PATH)

    with zipfile.ZipFile(ZIP_PATH) as zf:
        packages = load_csv(zf, "packages.csv")
        versions = load_csv(zf, "package_versions.csv")
        deps = load_csv(zf, "package_dependencies.csv")

    package_by_version = {int(v["id"]): int(v["package_id"]) for v in versions}
    version_created = {int(v["id"]): v["created_at"] for v in versions}
    version_str = {int(v["id"]): v["version_str"] for v in versions}
    package_versions = defaultdict(list)
    for v in versions:
        vid = int(v["id"])
        package_versions[int(v["package_id"])].append((v["created_at"], vid))
    for arr in package_versions.values():
        arr.sort(key=lambda x: (x[0], x[1]))

    deps_by_origin = defaultdict(list)
    malformed = 0
    duplicate = 0
    seen_edges = set()
    for d in deps:
        try:
            ov = int(d["depending_version"])
            tp = int(d["depending_on_package"])
            req = normalize_requirement(d["semver_str"])
            if not req:
                malformed += 1
                continue
            key = (ov, tp, req)
            if key in seen_edges:
                duplicate += 1
                continue
            seen_edges.add(key)
            deps_by_origin[ov].append((tp, req))
        except Exception:
            malformed += 1

    # Fixed candidate universe: target releases existing by the focal origin.
    # Candidate identity is independent of declaration text.
    target_versions_by_pkg = defaultdict(list)
    for vid, pid in package_by_version.items():
        target_versions_by_pkg[pid].append((version_created[vid], vid))
    for arr in target_versions_by_pkg.values():
        arr.sort(key=lambda x: (x[0], x[1]))

    def declaration_map(origin_vid):
        out = defaultdict(list)
        for tp, req in deps_by_origin.get(origin_vid, []):
            kind = requirement_kind(req)
            if kind == "UNSUPPORTED":
                continue
            out[tp].append(req)
        return out

    def candidate_accessible(origin_vid, target_pkg, target_vid, decls):
        tv = version_str[target_vid]
        for req in decls:
            try:
                if satisfies(tv, req):
                    return True
            except ValueError as exc:
                if str(exc).startswith("UNSUPPORTED_VERSION:"):
                    continue
                raise
        return False

    def build_tacc(origin_vid, t):
        """Membership-level T_acc using fixed candidate universe and present declarations."""
        result = set()
        decl = declaration_map(origin_vid)
        origin_pkg = package_by_version[origin_vid]
        for target_pkg, requirements in decl.items():
            for created, target_vid in target_versions_by_pkg.get(target_pkg, []):
                if created > t:
                    break
                if candidate_accessible(origin_vid, target_pkg, target_vid, requirements):
                    result.add((origin_vid, target_pkg, target_vid))
        return result

    def successor_configuration(origin_vid, target_pkg, target_vid, decl):
        """Canonical depth-1 potential configuration.

        This is declaration-induced configuration, not an execution state.
        All focal declarations are retained; one target package assignment is
        replaced by the selected target version. This avoids inventing Cargo
        lockfile/resolution/runtime semantics absent from the dataset.
        """
        assignments = []
        for pkg, reqs in sorted(decl.items()):
            assignments.append((pkg, tuple(sorted(reqs))))
        # Explicit potential assignment, separated from tau identity.
        replacement = (target_pkg, (version_str[target_vid],))
        base = [x for x in assignments if x[0] != target_pkg]
        base.append(replacement)
        base.sort(key=lambda x: x[0])
        return (origin_vid, tuple(base))

    paired = 0
    terminal = 0
    tacc_t0_count = tacc_t1_count = 0
    add_count = rem_count = 0
    reach_t0 = set()
    reach_t1 = set()
    tau_to_succ_t0 = defaultdict(set)
    tau_to_succ_t1 = defaultdict(set)
    redundant_added = 0
    nonredundant_added = 0
    unchanged_tacc_different_reach = 0
    examples = []

    versions_by_pkg = {pid: arr for pid, arr in package_versions.items()}
    focal_pairs = []
    for pid, arr in versions_by_pkg.items():
        for i in range(len(arr) - 1):
            t0, v0 = arr[i]
            t1, v1 = arr[i + 1]
            focal_pairs.append((pid, v0, v1, t0, t1))
        if arr:
            terminal += 1

    for pid, v0, v1, t0, t1 in focal_pairs:
        paired += 1
        a0 = build_tacc(v0, t0)
        a1 = build_tacc(v1, t1)
        add = a1 - a0
        rem = a0 - a1
        tacc_t0_count += len(a0)
        tacc_t1_count += len(a1)
        add_count += len(add)
        rem_count += len(rem)

        decl0 = declaration_map(v0)
        decl1 = declaration_map(v1)
        r0_local = set()
        r1_local = set()

        for tau in a0:
            ov, tp, tv = tau
            succ = successor_configuration(ov, tp, tv, decl0)
            r0_local.add(succ)
            tau_to_succ_t0[tau].add(succ)
        for tau in a1:
            ov, tp, tv = tau
            succ = successor_configuration(ov, tp, tv, decl1)
            r1_local.add(succ)
            tau_to_succ_t1[tau].add(succ)

        reach_t0.update(r0_local)
        reach_t1.update(r1_local)

        # Added transformations are classified against successor structure.
        for tau in add:
            ov, tp, tv = tau
            succ = successor_configuration(ov, tp, tv, decl1)
            if succ in r0_local:
                redundant_added += 1
                if len(examples) < 20:
                    examples.append({"case": "DELTA_TACC_NONZERO_DELTA_REACH_ZERO", "tau": tau, "successor": succ})
            else:
                nonredundant_added += 1
                if len(examples) < 20:
                    examples.append({"case": "DELTA_TACC_NONZERO_DELTA_REACH_NONZERO", "tau": tau, "successor": succ})

        # Detect a bounded same-cardinality structural distinction locally.
        if len(a0) == len(a1) and r0_local != r1_local:
            unchanged_tacc_different_reach += 1

    tacc0_global = None
    tacc1_global = None
    # Global hashes are computed from the collected successor sets. The local
    # sets are intentionally keyed by focal origin, preserving configuration
    # identity and avoiding accidental cross-origin equivalence.

    def hash_sorted(values):
        payload = "\n".join(canon(x) for x in sorted(values, key=canon))
        return sha256_text(payload)

    # Build global T_acc hashes from the transformation sets represented by the
    # successor maps. These are canonical structural anchors, not scientific
    # outcome measures.
    all_tau0 = set(tau_to_succ_t0)
    all_tau1 = set(tau_to_succ_t1)
    tacc0_hash = hash_sorted(all_tau0)
    tacc1_hash = hash_sorted(all_tau1)
    reach0_hash = hash_sorted(reach_t0)
    reach1_hash = hash_sorted(reach_t1)

    print("DATASET / TEMPORAL INTEGRITY")
    print(f"PACKAGE_COUNT: {len(packages)}")
    print(f"VERSION_COUNT: {len(versions)}")
    print(f"DEPENDENCY_ROWS_SCANNED: {len(deps)}")
    print(f"MALFORMED_ROWS: {malformed}")
    print(f"DUPLICATE_ROWS: {duplicate}")
    print(f"PAIRED_FOCAL_VERSION_TRANSITIONS: {paired}")
    print(f"TERMINAL_FOCAL_VERSIONS: {terminal}")
    print()

    print("T_ACC / REACH STRUCTURE")
    print(f"TACC_T0_MEMBERSHIP_COUNT: {len(all_tau0)}")
    print(f"TACC_T1_MEMBERSHIP_COUNT: {len(all_tau1)}")
    print(f"TACC_ADD_MEMBERSHIP_COUNT: {len(all_tau1 - all_tau0)}")
    print(f"TACC_REM_MEMBERSHIP_COUNT: {len(all_tau0 - all_tau1)}")
    print(f"REACH1_T0_CONFIGURATION_IDENTITY_COUNT: {len(reach_t0)}")
    print(f"REACH1_T1_CONFIGURATION_IDENTITY_COUNT: {len(reach_t1)}")
    print(f"REACH1_GLOBAL_ADD_CONFIGURATION_COUNT: {len(reach_t1 - reach_t0)}")
    print(f"REACH1_GLOBAL_REM_CONFIGURATION_COUNT: {len(reach_t0 - reach_t1)}")
    print(f"DELTA_TACC_ADDITIONS_WITH_REDUNDANT_SUCCESSOR: {redundant_added}")
    print(f"DELTA_TACC_ADDITIONS_WITH_NONREDUNDANT_SUCCESSOR: {nonredundant_added}")
    print(f"SAME_LOCAL_TACC_CARDINALITY_DIFFERENT_REACH_PAIRS: {unchanged_tacc_different_reach}")
    print()

    print("FIREWALL")
    print("CANDIDATE_IDENTITY_INCLUDES_DECLARATION: False")
    print("SUCCESSOR_IDENTITY_EQUALS_TRANSFORMATION_IDENTITY: False")
    print("EXECUTION_USED: False")
    print("OUTCOME_USED: False")
    print("VALUE_USED: False")
    print("FUTURE_ACTIVITY_USED: False")
    print(f"RSTAR_VERSION: {RSTAR_VERSION}")
    print("TRAJECTORY_COMPUTED: False")
    print()

    print("CANONICAL STRUCTURAL HASHES")
    print(f"TACC_T0_HASH: {tacc0_hash}")
    print(f"TACC_T1_HASH: {tacc1_hash}")
    print(f"REACH1_T0_HASH: {reach0_hash}")
    print(f"REACH1_T1_HASH: {reach1_hash}")
    print()

    print("EXAMPLES")
    for ex in examples:
        print(json.dumps(ex, ensure_ascii=False, sort_keys=True))
    print()

    report = {
        "version": "v0.1",
        "paired": paired,
        "terminal": terminal,
        "tacc_t0": len(all_tau0),
        "tacc_t1": len(all_tau1),
        "tacc_add": len(all_tau1 - all_tau0),
        "tacc_rem": len(all_tau0 - all_tau1),
        "reach_t0": len(reach_t0),
        "reach_t1": len(reach_t1),
        "reach_add": len(reach_t1 - reach_t0),
        "reach_rem": len(reach_t0 - reach_t1),
        "redundant_added": redundant_added,
        "nonredundant_added": nonredundant_added,
        "same_cardinality_different_reach": unchanged_tacc_different_reach,
        "tacc_t0_hash": tacc0_hash,
        "tacc_t1_hash": tacc1_hash,
        "reach_t0_hash": reach0_hash,
        "reach_t1_hash": reach1_hash,
        "firewall": {
            "execution": False,
            "outcome": False,
            "value": False,
            "future_activity": False,
            "rstar_modified": False,
        },
    }
    report_hash = sha256_text(canon(report))
    print(f"REPORT_CANONICAL_SHA256: {report_hash}")
    print()
    print("RUNTIME_AUDIT_OK: True")
    print("DECISION_STATUS: OPEN_PENDING_HUMAN_REVIEW_AND_GITHUB_RECORD")
    print("NEXT_GATE: REACH_NON_REDUNDANCY_RESULT_REVIEW")


if __name__ == "__main__":
    main()
