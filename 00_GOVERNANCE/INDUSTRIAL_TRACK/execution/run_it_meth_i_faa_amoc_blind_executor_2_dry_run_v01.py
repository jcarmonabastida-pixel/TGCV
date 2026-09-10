#!/usr/bin/env python3
"""One-shot local launcher for IT-METH-I FAA AMOC blind-control DRY RUN.

Technical DRY_RUN_CONTROL only. This launcher does not execute reconstruction
002 and does not establish EXECUTOR-2 independence.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

# execution/ -> INDUSTRIAL_TRACK/ -> 00_GOVERNANCE/ -> repository root
REPO_ROOT = Path(__file__).resolve().parents[3]
HARNESS = REPO_ROOT / "00_GOVERNANCE" / "INDUSTRIAL_TRACK" / "execution" / "it_meth_i_faa_amoc_blind_executor_2_control_v01.py"
PACKAGE = REPO_ROOT / "00_GOVERNANCE" / "INDUSTRIAL_TRACK" / "execution" / "IT-METH-I_FAA_AMOC_BLIND_EXECUTION_PACKAGE_001.md"
MANIFEST = REPO_ROOT / "00_GOVERNANCE" / "INDUSTRIAL_TRACK" / "execution" / "IT-METH-I_FAA_AMOC_GITHUB_DOCUMENTARY_EVIDENCE_MANIFEST_001.json"
EVIDENCE_ROOT = REPO_ROOT / "00_GOVERNANCE" / "INDUSTRIAL_TRACK" / "execution"
OUTPUT_ROOT = REPO_ROOT / "03_EXPERIMENTS" / "IT-METH-I_FAA_AMOC_BLIND_DRY_RUN" / "output"
RESULT = OUTPUT_ROOT / "IT-METH-I_FAA_AMOC_BLIND_DRY_RUN_RESULT_001.json"


def require(path: Path, label: str) -> None:
    if not path.exists():
        raise SystemExit(f"BLOCKED: missing {label}: {path}")
    if path.is_symlink():
        raise SystemExit(f"BLOCKED: symlink is not accepted for {label}: {path}")
    if not path.is_file() and path != REPO_ROOT / ".git":
        raise SystemExit(f"BLOCKED: invalid {label}: {path}")


def main() -> int:
    if not (REPO_ROOT / ".git").exists():
        raise SystemExit(f"BLOCKED: Git repository metadata not found: {REPO_ROOT}")
    require(HARNESS, "v0.6 control harness")
    require(PACKAGE, "frozen blind execution package")
    require(MANIFEST, "frozen documentary evidence manifest")

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)
    command = [
        sys.executable, str(HARNESS),
        "--package", str(PACKAGE),
        "--repo-root", str(REPO_ROOT),
        "--evidence", str(EVIDENCE_ROOT),
        "--evidence-manifest", str(MANIFEST),
        "--output", str(OUTPUT_ROOT),
        "--result", str(RESULT),
        "--mode", "DRY_RUN_CONTROL",
    ]

    print("IT-METH-I FAA AMOC — TECHNICAL DRY-RUN CONTROL")
    print(f"REPO_ROOT={REPO_ROOT}")
    print("MODE=DRY_RUN_CONTROL")
    print("RECONSTRUCTION_002=BLOCKED")
    print()

    completed = subprocess.run(command, cwd=REPO_ROOT, check=False)

    if not RESULT.exists():
        print(f"BLOCKED: harness did not produce expected result: {RESULT}")
        return completed.returncode or 1

    try:
        payload = json.loads(RESULT.read_text(encoding="utf-8"))
    except Exception as exc:
        print(f"BLOCKED: result JSON is unreadable: {exc}")
        return 1

    print()
    for key in (
        "OVERALL_CONTROL_STATUS", "PACKAGE_INTEGRITY", "EVIDENCE_MANIFEST_STATUS",
        "DECLARED_EVIDENCE_BOUNDARY_STATUS", "OUTPUT_BOUNDARY_STATUS",
        "SEAL_MECHANISM_CAPABILITY_STATUS", "CONTROL_SEQUENCE_STATUS",
        "EXECUTOR_2_DISTINCT", "INDEPENDENCE_STATUS", "RECONSTRUCTION_002_STATUS",
    ):
        print(f"{key}={payload.get(key)}")
    print(f"RESULT_FILE={RESULT}")
    print(f"EXIT_CODE={completed.returncode}")
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
