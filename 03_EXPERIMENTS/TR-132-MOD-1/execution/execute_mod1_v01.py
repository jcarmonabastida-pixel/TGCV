#!/usr/bin/env python3
"""TR-132-MOD-1 bounded L3 scientific execution.

Consumes only the frozen methodological fixture. Realization is never used
as evidence of accessibility. The result is an operational fixture result,
not empirical evidence from the Rust ecosystem and not Core/value validation.
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


def git_blob_sha(rel: str) -> str | None:
    try:
        p = subprocess.run(["git", "rev-parse", f"HEAD:{rel}"], cwd=ROOT, check=True, capture_output=True, text=True)
        return p.stdout.strip() or None
    except (subprocess.CalledProcessError, OSError):
        return None


def csv_rows(name: str) -> list[dict[str, str]]:
    with (FIXTURE / name).open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def main() -> int:
    adjudication = csv_rows("ACCESSIBILITY_ADJUDICATION_v0.1.csv")
    realization = csv_rows("REALIZATION_SCHEDULE_v0.1.csv")
    transformations = csv_rows("TRANSFORMATIONS_v0.1.csv")

    if [r["tau_id"] for r in transformations] != CANDIDATES:
        raise SystemExit("STOP: candidate universe mismatch")
    if [r["timepoint_id"] for r in csv_rows("STATES_v0.1.csv")] != TIMEPOINTS:
        raise SystemExit("STOP: timepoint mismatch")
    if not all(r["adjudication_phase"] == "PRE_REALIZATION" for r in adjudication):
        raise SystemExit("STOP: accessibility adjudication is not pre-realization")
    if len(realization) != 10:
        raise SystemExit("STOP: realization schedule is incomplete")

    accessible = {}
    for t in TIMEPOINTS:
        statuses = {
            r["tau_id"]
            for r in adjudication
            if r["timepoint_id"] == t and r["status"] == "ACCESSIBLE"
        }
        accessible[t] = sorted(statuses, key=CANDIDATES.index)

    delta = sorted(set(accessible["t0"]).symmetric_difference(accessible["t1"]), key=CANDIDATES.index)
    if not delta:
        decision = "FAIL"
        level = "L3"
    else:
        decision = "BOUNDED PASS"
        level = "L3"

    # Reproducibility fingerprint is over canonical Git blob identities, not
    # Windows working-tree bytes. This binds the result to the frozen package.
    frozen = [
        "00_GOVERNANCE/TR-132-MOD-1/fixture/FIXTURE_MANIFEST_v0.1.md",
        "00_GOVERNANCE/TR-132-MOD-1/fixture/EVIDENCE_MANIFEST_v0.1.md",
        "00_GOVERNANCE/TR-132-MOD-1/fixture/ACCESSIBILITY_ADJUDICATION_v0.1.csv",
        "00_GOVERNANCE/TR-132-MOD-1/fixture/CONTROL_CASES_v0.1.csv",
        "00_GOVERNANCE/TR-132-MOD-1/fixture/REALIZATION_SCHEDULE_v0.1.csv",
        "00_GOVERNANCE/TR-132-MOD-1/fixture/STATES_v0.1.csv",
        "00_GOVERNANCE/TR-132-MOD-1/fixture/TRANSFORMATIONS_v0.1.csv",
    ]
    fingerprint = hashlib.sha256("\n".join(f"{p}:{git_blob_sha(p)}" for p in frozen).encode()).hexdigest()

    result = {
        "execution": "TR-132-MOD-1",
        "status": decision,
        "decision_level": level,
        "fixture": FIXTURE_ID,
        "package": PACKAGE,
        "seed": SEED,
        "predicate": PREDICATE,
        "scientific_execution_performed": True,
        "methodological_scope": "BOUNDED_L3_TEMPORAL_IDENTIFIABILITY",
        "accessible_sets": accessible,
        "symmetric_difference": delta,
        "realization_used_as_accessibility_evidence": False,
        "external_dataset_used": False,
        "claims_supported": [
            "bounded temporal identifiability of a change in accessible transformations under the frozen fixture"
        ] if decision == "BOUNDED PASS" else [],
        "claims_not_supported": [
            "full T_acc closure",
            "causal inference",
            "value inference",
            "industrial utility",
            "TGCV Core validation beyond the declared methodological test",
            "Rust ecosystem evidence",
        ],
        "package_fingerprint_sha256": fingerprint,
    }
    RESULT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("EXECUTION_RESULT=" + decision)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if decision == "BOUNDED PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
