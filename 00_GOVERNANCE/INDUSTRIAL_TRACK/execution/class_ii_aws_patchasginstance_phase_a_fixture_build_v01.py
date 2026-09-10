"""IT-METH-I Class II AWS-PatchAsgInstance — Phase A fixture builder.

Purpose: construct and freeze the pre-decision fixture only.
This executable MUST NOT invoke AWS-PatchAsgInstance or the comparator.

This first version is a controlled execution scaffold: it validates the
required local inputs and AWS CLI identity, then records the execution
boundary. AWS resource creation is intentionally explicit and is not
performed until the implementation is completed against the frozen build
specification.
"""

from __future__ import annotations

import argparse
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

CANDIDATE = "AWS-PatchAsgInstance"
EVIDENCE_CLASS = "CLASS II — PUBLIC REPRODUCIBLE FIXTURE"
PHASE = "PHASE_A_FIXTURE_BUILD_AND_PREDECISION_FREEZE"


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def run_checked(command: list[str]) -> str:
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout.strip()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[4])
    parser.add_argument("--region", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    aws = shutil.which("aws")
    if aws is None:
        print("PHASE_A_STATUS=BLOCKED_INFRASTRUCTURE")
        print("REASON=AWS_CLI_NOT_FOUND")
        return 2

    try:
        identity = run_checked([aws, "sts", "get-caller-identity", "--output", "json"])
    except subprocess.CalledProcessError as exc:
        print("PHASE_A_STATUS=BLOCKED_INFRASTRUCTURE")
        print("REASON=AWS_IDENTITY_CHECK_FAILED")
        if exc.stderr:
            print(exc.stderr.strip())
        return 3

    required = [
        args.repo_root / "00_GOVERNANCE/INDUSTRIAL_TRACK/IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_CONTROLLED_FIXTURE_BUILD_SPECIFICATION_001.md",
        args.repo_root / "00_GOVERNANCE/INDUSTRIAL_TRACK/IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_FIXTURE_BUILD_AUTHORIZATION_001.md",
        args.repo_root / "00_GOVERNANCE/INDUSTRIAL_TRACK/IT_METH_I_CLASS_II_FIXTURE_COMPOSITION_MANIFEST_001.md",
        args.repo_root / "00_GOVERNANCE/INDUSTRIAL_TRACK/IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_PREDECISION_STATE_AND_COMPARATOR_CONTRACT_001.md",
    ]
    missing = [str(p) for p in required if not p.is_file()]
    if missing:
        print("PHASE_A_STATUS=BLOCKED_INPUTS")
        print(json.dumps({"missing": missing}, indent=2))
        return 4

    args.output_dir.mkdir(parents=True, exist_ok=True)
    record = {
        "phase": PHASE,
        "candidate": CANDIDATE,
        "evidence_class": EVIDENCE_CLASS,
        "started_utc": utc_now(),
        "region": args.region,
        "aws_identity_check": json.loads(identity),
        "execution_boundary": {
            "fixture_build": "authorized",
            "predecision_freeze": "authorized",
            "candidate_transformation": "NOT_AUTHORIZED",
            "comparator_transformation": "NOT_AUTHORIZED",
            "utility_scoring": "NOT_AUTHORIZED",
        },
        "status": "SCAFFOLD_ONLY",
        "note": "No AWS resource mutation is performed by this version.",
    }
    output = args.output_dir / "PHASE_A_EXECUTION_SCAFFOLD_RECORD_001.json"
    output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print("PHASE_A_STATUS=SCAFFOLD_READY")
    print(f"OUTPUT={output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
