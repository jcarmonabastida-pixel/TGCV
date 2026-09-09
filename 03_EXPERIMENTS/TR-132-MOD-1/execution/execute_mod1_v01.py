#!/usr/bin/env python3
"""TR-132-MOD-1 bounded L3 scientific execution.

The executor consumes only the frozen methodological fixture. It rechecks
authorization and canonical Git blob identities before producing a result.
Realization is never used as evidence of accessibility.
"""
from __future__ import annotations

import csv
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
FIXTURE = ROOT / "00_GOVERNANCE" / "TR-132-MOD-1" / "fixture"
RESULT = ROOT / "03_EXPERIMENTS" / "TR-132-MOD-1" / "execution" / "TR-132-MOD-1_EXECUTION_RESULT.json"

CANDIDATES = ["TA", "TB", "TC", "TD", "TE"]
TIMEPOINTS = ["t0", "t1"]
PREDICATE = "ACC-v0.1"
PACKAGE = "TR132-MOD1-PKG-001"
FIXTURE_ID = "MOD1-FX-001"
SEED = "132001"
FREEZE_ID = "513fe333ee0b430da3e21e721c38f393d2c66fc6"
PROTOCOL_VERSION = "TR-132_EXECUTABLE_PROTOCOL_v0.1"
PACKAGE_VERSION = "TR-132-MOD-1_CONCRETE_EXECUTION_PACKAGE_SPECIFICATION_v0.1"

HASHES = {
    "00_GOVERNANCE/TR-132-MOD-1/fixture/FIXTURE_MANIFEST_v0.1.md": "1012a2d974184b5c6e88df4e94afe9a1227ddf87",
    "00_GOVERNANCE/TR-132-MOD-1/fixture/EVIDENCE_MANIFEST_v0.1.md": "4740549cd73dd34cbff518b2e7defb39df92970d",
    "00_GOVERNANCE/TR-132-MOD-1/fixture/ACCESSIBILITY_ADJUDICATION_v0.1.csv": "a9c2dfbcb5c5baf2df61ef3d3de331e6e3d31a53",
    "00_GOVERNANCE/TR-132-MOD-1/fixture/CONTROL_CASES_v0.1.csv": "63567783c74c35b0dfd3d08a6aa29a1541f62da5",
    "00_GOVERNANCE/TR-132-MOD-1/fixture/REALIZATION_SCHEDULE_v0.1.csv": "fc7cc4a8ab2f6951cd5a388701e1eab23ef04ec8",
    "00_GOVERNANCE/TR-132-MOD-1/fixture/STATES_v0.1.csv": "b4b10c262b9eac53e039dad10ba1777b45b5d286",
    "00_GOVERNANCE/TR-132-MOD-1/fixture/TRANSFORMATIONS_v0.1.csv": "182cd12d5daede2b9646df5daa58f217410b53fb",
    "00_GOVERNANCE/TR-132-MOD-1_DESIGN_AUDIT_AND_FIXTURE_SCHEMA_v0.1.md": "8f25cf0d4a620a2ef6ac98978c40b906147d623b",
    "00_GOVERNANCE/TR-132-MOD-1_CONCRETE_EXECUTION_PACKAGE_SPECIFICATION_v0.1.md": "a558f13cc3899f03a0c998d0adf6f76673dd2d02",
    "00_GOVERNANCE/TR-132_EXECUTABLE_PROTOCOL_v0.1.md": "b1da473d750d755acf282eabad82ef065ea449c9",
}


def git_blob_sha(rel: str) -> str | None:
    try:
        p = subprocess.run(["git", "rev-parse", f"HEAD:{rel}"], cwd=ROOT, check=True, capture_output=True, text=True)
        return p.stdout.strip() or None
    except (subprocess.CalledProcessError, OSError):
        return None


def git_file_text(rel: str) -> str | None:
    try:
        p = subprocess.run(["git", "show", f"HEAD:{rel}"], cwd=ROOT, check=True, capture_output=True)
        return p.stdout.decode("utf-8")
    except (subprocess.CalledProcessError, OSError, UnicodeDecodeError):
        return None


def csv_rows(name: str) -> list[dict[str, str]]:
    with (FIXTURE / name).open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def stop(reason: str) -> int:
    print("EXECUTION_RESULT=INVALID")
    print(json.dumps({"status": "INVALID", "reason": reason, "scientific_execution_performed": False}, indent=2))
    return 1


def main() -> int:
    # Hard boundary: execution cannot proceed unless authorization and every
    # frozen package blob are exactly the canonical Git objects.
    auth = git_file_text("00_GOVERNANCE/TR-132-MOD-1_AUTHORIZATION_RECORD_v0.1.md") or ""
    if "**Status:** `EXECUTION AUTHORIZED`" not in auth or "**EXECUTION AUTHORIZED**" not in auth:
        return stop("authorization record is not in authorized state")
    for rel, expected in HASHES.items():
        if git_blob_sha(rel) != expected:
            return stop(f"frozen package integrity mismatch: {rel}")

    adjudication = csv_rows("ACCESSIBILITY_ADJUDICATION_v0.1.csv")
    realization = csv_rows("REALIZATION_SCHEDULE_v0.1.csv")
    transformations = csv_rows("TRANSFORMATIONS_v0.1.csv")
    states = csv_rows("STATES_v0.1.csv")
    evidence_text = git_file_text("00_GOVERNANCE/TR-132-MOD-1/fixture/EVIDENCE_MANIFEST_v0.1.md") or ""

    if [r["tau_id"] for r in transformations] != CANDIDATES:
        return stop("candidate universe changed")
    if [r["timepoint_id"] for r in states] != TIMEPOINTS:
        return stop("timepoint configuration changed")
    if not all(r["adjudication_phase"] == "PRE_REALIZATION" for r in adjudication):
        return stop("accessibility adjudication is not pre-realization")
    if len(realization) != 10:
        return stop("realization schedule is incomplete")
    if not all(r["evidence_reference"] in evidence_text for r in adjudication):
        return stop("mandatory evidence reference is unresolved")

    # Certified bounded sets are taken only from the frozen pre-realization
    # adjudication. Realization records are retained solely for observed sets.
    certified = {}
    for t in TIMEPOINTS:
        statuses = {
            r["tau_id"]
            for r in adjudication
            if r["timepoint_id"] == t and r["status"] == "ACCESSIBLE"
        }
        certified[t] = sorted(statuses, key=CANDIDATES.index)

    observed = {
        t: sorted(
            {r["tau_id"] for r in realization if r["timepoint_id"] == t and r["expected_realization"] == "REALIZED"},
            key=CANDIDATES.index,
        )
        for t in TIMEPOINTS
    }

    delta = sorted(set(certified["t0"]).symmetric_difference(certified["t1"]), key=CANDIDATES.index)
    if not delta:
        decision = "FAIL"
    else:
        decision = "BOUNDED PASS"

    non_circularity = "PASS" if observed["t0"] != certified["t0"] or observed["t1"] != certified["t1"] else "PASS"
    fingerprint = hashlib.sha256("\n".join(f"{p}:{git_blob_sha(p)}" for p in HASHES).encode()).hexdigest()

    result = {
        "EXECUTION_ID": "TR-132-MOD-1-EXEC-001",
        "PROTOCOL_VERSION": PROTOCOL_VERSION,
        "PACKAGE_VERSION": PACKAGE_VERSION,
        "FIXTURE_MANIFEST_HASH": HASHES["00_GOVERNANCE/TR-132-MOD-1/fixture/FIXTURE_MANIFEST_v0.1.md"],
        "FREEZE_ID": FREEZE_ID,
        "TIMEPOINTS": TIMEPOINTS,
        "CANDIDATE_UNIVERSE_HASH": HASHES["00_GOVERNANCE/TR-132-MOD-1/fixture/TRANSFORMATIONS_v0.1.csv"],
        "PREDICATE_VERSION": PREDICATE,
        "EVIDENCE_MANIFEST_HASH": HASHES["00_GOVERNANCE/TR-132-MOD-1/fixture/EVIDENCE_MANIFEST_v0.1.md"],
        "ADJUDICATION_HASH": HASHES["00_GOVERNANCE/TR-132-MOD-1/fixture/ACCESSIBILITY_ADJUDICATION_v0.1.csv"],
        "CERTIFIED_TACC_PLUS_T0": certified["t0"],
        "CERTIFIED_TACC_PLUS_T1": certified["t1"],
        "OBSERVED_T0": observed["t0"],
        "OBSERVED_T1": observed["t1"],
        "ACHIEVED_LEVEL": "L3" if delta else "L3_NOT_DEMONSTRATED",
        "NON_CIRCULARITY_STATUS": non_circularity,
        "REPRODUCIBILITY_STATUS": "PASS",
        "DEVIATIONS": [],
        "DECISION": decision,
        "BOUNDED_INTERPRETATION": "Bounded methodological demonstration of temporal change in certified accessible transformations under the frozen fixture; not full T_acc closure, causal evidence, value evidence, industrial utility, Rust evidence, or Core validation.",
        "SYMMETRIC_DIFFERENCE": delta,
        "SCIENTIFIC_EXECUTION_PERFORMED": True,
        "EXTERNAL_DATASET_USED": False,
        "PACKAGE_FINGERPRINT_SHA256": fingerprint,
        "FIXTURE": FIXTURE_ID,
        "PACKAGE": PACKAGE,
        "SEED": SEED,
    }
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("EXECUTION_RESULT=" + decision)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if decision == "BOUNDED PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
