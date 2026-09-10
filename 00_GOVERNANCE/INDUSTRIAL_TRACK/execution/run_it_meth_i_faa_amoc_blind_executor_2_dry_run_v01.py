#!/usr/bin/env python3
"""One-shot local launcher for IT-METH-I FAA AMOC blind-control DRY RUN.

This launcher performs technical DRY_RUN_CONTROL only. It does not execute
reconstruction 002 and does not establish EXECUTOR-2 independence.

Expected local checkout:
    C:\\Users\\pedri\\TGCV

Run from the repository root or from any working directory.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[4]
HARNESS = REPO_ROOT / "00_GOVERNANCE" / "INDUSTRIAL_TRACK" / "execution" / "it_meth_i_faa_amoc_blind_executor_2_control_v01.py"
PACKAGE = REPO_ROOT / "00_GOVERNANCE" / "INDUSTRIAL_TRACK" / "execution" / "IT-METH-I_FAA_AMOC_BLIND_EXECUTION_PACKAGE_001.md"
MANIFEST = REPO_ROOT / "00_GOVERNANCE" / "INDUSTRIAL_TRACK" / "execution" / "IT-METH-I_FAA_AMOC_GITHUB_DOCUMENTARY_EVIDENCE_MANIFEST_001.json"
EVIDENCE_ROOT = REPO_ROOT / "00_GOVERNANCE" / "INDUSTRIAL_TRACK" / "execution"
OUTPUT_ROOT = REPO_ROOT / "03_EXPERIMENTS" / "IT-METH-I_FAA_AMOC_BLIND_DRY_RUN" / "output"
RESULT = OUTPUT_ROOT / "IT-METH-I_FAA_AMOC_BLIND_DRY_RUN_RESULT_001.json"


def require(path: Path, label: str) -> None:
    if not path.exists() or not path.is_file():
        raise SystemExit(f"BLOCKED: missing {label}: {path}")
    if path.is_symlink():
        raise SystemExit(f"BLOCKED: symlink is not accepted for {label}: {path}")


def main() -> int:
    require(REPO_ROOT / ".git", "Git repository metadata")
    require(HARNESS, "v0.6 control harness")
    require(PACKAGE, "frozen blind execution package")
    require(MANIFEST, "frozen documentary evidence manifest")

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    command = [
        sys.executable,
        str(HARNESS),
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
    print(f"HARNESS={HARNESS}")
    print(f"PACKAGE={PACKAGE}")
    print(f"MANIFEST={MANIFEST}")
    print(f"OUTPUT={OUTPUT_ROOT}")
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
    print("RESULT_FILE=" + str(RESULT))
    print("OVERALL_CONTROL_STATUS=" + str(payload.get("OVERALL_CONTROL_STATUS")))
    print("PACKAGE_INTEGRITY=" + str(payload.get("PACKAGE_INTEGRITY")))
    print("EVIDENCE_MANIFEST_STATUS=" + str(payload.get("EVIDENCE_MANIFEST_STATUS")))
    print("DECLARED_EVIDENCE_BOUNDARY_STATUS=" + str(payload.get("DECLARED_EVIDENCE_BOUNDARY_STATUS")))
    print("OUTPUT_BOUNDARY_STATUS=" + str(payload.get("OUTPUT_BOUNDARY_STATUS")))
    print("SEAL_MECHANISM_CAPABILITY_STATUS=" + str(payload.get("SEAL_MECHANISM_CAPABILITY_STATUS")))
    print("CONTROL_SEQUENCE_STATUS=" + str(payload.get("CONTROL_SEQUENCE_STATUS")))
    print("EXECUTOR_2_DISTINCT=" + str(payload.get("EXECUTOR_2_DISTINCT")))
    print("INDEPENDENCE_STATUS=" + str(payload.get("INDEPENDENCE_STATUS")))
    print("RECONSTRUCTION_002_STATUS=" + str(payload.get("RECONSTRUCTION_002_STATUS")))
    print("EXIT_CODE=" + str(completed.returncode))
    return completed.returncode


if __name__ == "__main__":
    raise SystemExit(main())
