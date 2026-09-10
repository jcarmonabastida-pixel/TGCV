"""IT-METH-I Class II AWS-PatchAsgInstance — Phase A fixture executor.

Scope: Phase A fixture construction and pre-decision freeze only.
Candidate/comparator transformations and utility scoring are forbidden.

This version is intentionally a guarded executor/preflight. It validates
canonical governance locally and the AWS execution prerequisite, but performs
no AWS resource mutation until the implementation has passed its primary
code audit and a concrete runtime build procedure is frozen.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

CANDIDATE = "AWS-PatchAsgInstance"
EVIDENCE_CLASS = "CLASS II — PUBLIC REPRODUCIBLE FIXTURE"
PHASE = "PHASE_A_FIXTURE_BUILD_AND_PREDECISION_FREEZE"
EXPECTED_SOURCE_SHA256 = {
    "ASG_TEMPLATE": "D10B323570774C9D4C07547A8035EB7D6B3D907E83CF0DDF95A8EDC73D02C339",
    "PATCH_TEMPLATE": "FD1C09C1FD200BC14A8039F00BF15AB3E894DE5DBA15315A07C375FD2ECEF5E2",
    "RUNBOOK": "EFC2F49FFA368EFF1BF768F71E74F7BC518C136EDE03ABAAB97D5B966DC3C4EB",
}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def run_checked(command: list[str]) -> str:
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout.strip()


def require_text(path: Path, patterns: list[str]) -> list[str]:
    text = path.read_text(encoding="utf-8")
    return [p for p in patterns if p not in text]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument("--region", required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()

    governance = args.repo_root / "00_GOVERNANCE/INDUSTRIAL_TRACK"
    required = {
        "build_spec": governance / "IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_CONTROLLED_FIXTURE_BUILD_SPECIFICATION_001.md",
        "authorization": governance / "IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_FIXTURE_BUILD_AUTHORIZATION_001.md",
        "manifest": governance / "IT_METH_I_CLASS_II_FIXTURE_COMPOSITION_MANIFEST_001.md",
        "contract": governance / "IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_PREDECISION_STATE_AND_COMPARATOR_CONTRACT_001.md",
    }
    missing = [str(p) for p in required.values() if not p.is_file()]
    if missing:
        print("PHASE_A_STATUS=BLOCKED_INPUTS")
        print(json.dumps({"missing": missing}, indent=2))
        return 4

    checks = {}
    checks["authorization"] = require_text(required["authorization"], [
        "FIXTURE_BUILD_AUTHORIZATION = GRANTED",
        "PHASE_A_AUTHORIZED = TRUE",
        "CANDIDATE_EXECUTION_AUTHORIZED = FALSE",
        "COMPARATOR_EXECUTION_AUTHORIZED = FALSE",
    ])
    checks["build_spec"] = require_text(required["build_spec"], [
        "BUILD_SPECIFICATION = FROZEN",
        "FIXTURE_BUILD_AUTHORIZATION = GRANTED",
        "PHASE_A_AUTHORIZED = TRUE",
        "PRE_EXECUTION_TRANSFORMATION_GATE = BLOCKED",
    ])
    checks["manifest"] = require_text(required["manifest"], [
        "aws-samples/ec2-auto-scaling-instance-refresh-sample",
        "95fcf3dd19f837349098e1a710b1a6bdd9705ecc",
        "aws-samples/aws-cloud-and-hybrid-operations-workshop",
        "618d0ab6da6a3c282e87a098efaa2e62284a8c8f",
        "AWS-PatchAsgInstance",
        "PRE_EXECUTION_GATE = BLOCKED",
    ])
    checks["contract"] = require_text(required["contract"], [
        "PREDECISION_STATE_CONTRACT = FROZEN DESIGN",
        "COMPARATOR_CONTRACT = FROZEN DESIGN",
        "PRE_EXECUTION_GATE = BLOCKED",
    ])
    failed = {k: v for k, v in checks.items() if v}
    if failed:
        print("PHASE_A_STATUS=BLOCKED_GOVERNANCE")
        print(json.dumps({"missing_canonical_assertions": failed}, indent=2))
        return 5

    aws = shutil.which("aws")
    if aws is None:
        print("PHASE_A_STATUS=BLOCKED_INFRASTRUCTURE")
        print("REASON=AWS_CLI_NOT_FOUND")
        print("NOTE=Governance preflight passed; no AWS mutation was attempted.")
        return 2

    try:
        identity = json.loads(run_checked([aws, "sts", "get-caller-identity", "--output", "json"]))
    except (subprocess.CalledProcessError, json.JSONDecodeError) as exc:
        print("PHASE_A_STATUS=BLOCKED_INFRASTRUCTURE")
        print("REASON=AWS_IDENTITY_CHECK_FAILED")
        print(str(exc))
        return 3

    source_candidates = {
        "ASG_TEMPLATE": [
            args.repo_root / ".." / "Downloads" / "AWS-PatchAsgInstance" / "PUBLIC_SOURCES" / "ASG_FIXTURE_SOURCE" / "template.yaml",
        ],
        "PATCH_TEMPLATE": [
            args.repo_root / ".." / "Downloads" / "AWS-PatchAsgInstance" / "PUBLIC_SOURCES" / "PATCH_SOURCE" / "cfntemplates" / "ssm-workshop-resources-episode-04.yml",
        ],
        "RUNBOOK": [
            args.repo_root / ".." / "Downloads" / "AWS-PatchAsgInstance" / "AWS-PatchAsgInstance_OFFICIAL_RUNBOOK.md",
        ],
    }
    source_hashes = {}
    hash_failures = {}
    for key, paths in source_candidates.items():
        existing = next((p.resolve() for p in paths if p.is_file()), None)
        actual = sha256_file(existing) if existing else None
        expected = EXPECTED_SOURCE_SHA256[key]
        source_hashes[key] = {"path": str(existing) if existing else None,
                              "sha256": actual,
                              "expected_sha256": expected,
                              "status": "PASS" if actual == expected else ("BLOCKED_MISSING" if actual is None else "FAIL")}
        if actual != expected:
            hash_failures[key] = source_hashes[key]

    if hash_failures:
        print("PHASE_A_STATUS=BLOCKED_SOURCE_INTEGRITY")
        print(json.dumps({"source_hash_failures": hash_failures}, indent=2))
        return 6

    args.output_dir.mkdir(parents=True, exist_ok=True)
    record = {
        "phase": PHASE,
        "candidate": CANDIDATE,
        "evidence_class": EVIDENCE_CLASS,
        "started_utc": datetime.now(timezone.utc).isoformat(),
        "region": args.region,
        "canonical_governance_checks": {k: "PASS" for k in checks},
        "aws_identity_check": identity,
        "source_hash_preflight": source_hashes,
        "execution_boundary": {
            "fixture_build": "authorized",
            "predecision_freeze": "authorized",
            "candidate_transformation": "NOT_AUTHORIZED",
            "comparator_transformation": "NOT_AUTHORIZED",
            "utility_scoring": "NOT_AUTHORIZED",
        },
        "status": "PREFLIGHT_READY",
        "note": "No AWS resource mutation is performed by this guarded version.",
    }
    output = args.output_dir / "PHASE_A_PREFLIGHT_RECORD_001.json"
    output.write_text(json.dumps(record, indent=2) + "\n", encoding="utf-8")
    print("PHASE_A_STATUS=PREFLIGHT_READY")
    print(f"OUTPUT={output}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
