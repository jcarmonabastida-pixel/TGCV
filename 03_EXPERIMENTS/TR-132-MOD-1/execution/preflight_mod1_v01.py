#!/usr/bin/env python3
"""TR-132-MOD-1 deterministic execution preflight.

This program validates the authorized, frozen package before any scientific
execution. It performs no realization and produces no scientific result.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[3]
FIXTURE = ROOT / "00_GOVERNANCE" / "TR-132-MOD-1" / "fixture"
GOV = ROOT / "00_GOVERNANCE"
EXEC = ROOT / "03_EXPERIMENTS" / "TR-132-MOD-1" / "execution"

EXPECTED_PACKAGE = "TR132-MOD1-PKG-001"
EXPECTED_FIXTURE = "MOD1-FX-001"
EXPECTED_SEED = "132001"
EXPECTED_PREDICATE = "ACC-v0.1"
EXPECTED_CANDIDATES = ["TA", "TB", "TC", "TD", "TE"]
EXPECTED_TIMEPOINTS = ["t0", "t1"]

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
    """Return the canonical Git blob SHA for *rel* at the checked-out HEAD."""
    try:
        result = subprocess.run(
            ["git", "rev-parse", f"HEAD:{rel}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except (subprocess.CalledProcessError, OSError):
        return None
    return result.stdout.strip() or None


def git_file_text(rel: str) -> str | None:
    """Read canonical UTF-8 file content directly from the checked-out Git tree."""
    try:
        result = subprocess.run(
            ["git", "show", f"HEAD:{rel}"],
            cwd=ROOT,
            check=True,
            capture_output=True,
        )
    except (subprocess.CalledProcessError, OSError):
        return None
    try:
        return result.stdout.decode("utf-8")
    except UnicodeDecodeError:
        return None


def read_csv(name: str) -> list[dict[str, str]]:
    with (FIXTURE / name).open("r", encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh))


def main() -> int:
    checks: dict[str, bool] = {}
    errors: list[str] = []

    manifest = git_file_text("00_GOVERNANCE/TR-132-MOD-1/fixture/FIXTURE_MANIFEST_v0.1.md") or ""
    checks["fixture_identity"] = f"**Fixture ID:** `{EXPECTED_FIXTURE}`" in manifest
    checks["package_identity"] = f"**Package ID:** `{EXPECTED_PACKAGE}`" in manifest
    checks["seed"] = f"**Deterministic seed:** `{EXPECTED_SEED}`" in manifest
    checks["predicate"] = f"fixed accessibility predicate version `{EXPECTED_PREDICATE}`" in manifest

    # Immutable package integrity: compare frozen hashes with canonical Git blobs,
    # never with the Windows working-tree byte representation.
    for rel, expected in HASHES.items():
        key = f"hash:{rel}"
        actual = git_blob_sha(rel)
        ok = actual == expected
        checks[key] = ok
        if not ok:
            errors.append(f"{rel}: expected {expected}, got {actual or 'MISSING'}")

    auth_rel = "00_GOVERNANCE/TR-132-MOD-1_AUTHORIZATION_RECORD_v0.1.md"
    auth = git_file_text(auth_rel) or ""
    checks["authorization"] = "Status: EXECUTION AUTHORIZED" in auth and "EXECUTION AUTHORIZED" in auth

    transformations = read_csv("TRANSFORMATIONS_v0.1.csv")
    states = read_csv("STATES_v0.1.csv")
    adjudication = read_csv("ACCESSIBILITY_ADJUDICATION_v0.1.csv")
    controls = read_csv("CONTROL_CASES_v0.1.csv")
    evidence = (FIXTURE / "EVIDENCE_MANIFEST_v0.1.md").read_text(encoding="utf-8")

    checks["candidate_universe"] = [r["tau_id"] for r in transformations] == EXPECTED_CANDIDATES
    checks["timepoints"] = [r["timepoint_id"] for r in states] == EXPECTED_TIMEPOINTS
    checks["state_delta_only_R2"] = (
        len(states) == 2
        and states[0]["R2_available"] == "false"
        and states[1]["R2_available"] == "true"
        and all(states[0][k] == states[1][k] for k in states[0] if k not in {"timepoint_id", "R2_available"})
    )
    checks["adjudication_pre_realization"] = bool(adjudication) and all(
        r["adjudication_phase"] == "PRE_REALIZATION" for r in adjudication
    )
    checks["evidence_complete"] = all(r["evidence_reference"] in evidence for r in adjudication)

    realization = read_csv("REALIZATION_SCHEDULE_v0.1.csv")
    checks["realization_separate"] = len(realization) == 10 and all(
        r["tau_id"] in EXPECTED_CANDIDATES for r in realization
    )
    checks["negative_control_TB"] = any(
        r["tau_id"] == "TB" and r["timepoint_id"] == "t0" and r["expected_accessibility"] == "ACCESSIBLE"
        and r["expected_realization"] == "NOT_REALIZED" for r in controls
    )
    checks["indeterminate_TE"] = any(
        r["tau_id"] == "TE" and r["expected_accessibility"] == "INDETERMINATE" for r in controls
    )

    t0 = {r["tau_id"] for r in adjudication if r["timepoint_id"] == "t0" and r["status"] == "ACCESSIBLE"}
    t1 = {r["tau_id"] for r in adjudication if r["timepoint_id"] == "t1" and r["status"] == "ACCESSIBLE"}
    checks["bounded_sets"] = t0 == {"TA", "TB"} and t1 == {"TA", "TB", "TD"}
    checks["temporal_delta"] = t0.symmetric_difference(t1) == {"TD"}

    forbidden = []
    for p in EXEC.rglob("*"):
        if p.is_file() and p.name != Path(__file__).name and p.suffix.lower() in {".zip", ".parquet", ".sqlite", ".db"}:
            forbidden.append(str(p.relative_to(ROOT)))
    checks["no_external_dataset_in_execution_layer"] = not forbidden
    if forbidden:
        errors.append("External/data artifact in execution layer: " + ", ".join(forbidden))

    failed = [name for name, ok in checks.items() if not ok]
    status = "PASS" if not failed and not errors else "FAIL"
    result = {
        "preflight": "TR-132-MOD-1",
        "status": status,
        "scientific_execution_performed": False,
        "fixture": EXPECTED_FIXTURE,
        "package": EXPECTED_PACKAGE,
        "checks": checks,
        "failed_checks": failed,
        "errors": errors,
    }
    print("PREFLIGHT_RESULT=" + status)
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
