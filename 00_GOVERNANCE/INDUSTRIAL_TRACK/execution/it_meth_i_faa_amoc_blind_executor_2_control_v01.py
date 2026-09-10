#!/usr/bin/env python3
"""IT-METH-I FAA AMOC Blind Executor-2 control harness v0.1.

DRY-RUN CONTROL ONLY.

This program verifies technical controls for a proposed blind execution
context. It does not perform reconstruction 002 and it cannot establish
executor independence by itself.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import sys
from datetime import datetime, timezone
from pathlib import Path

PACKAGE_ID = "IT-METH-I-AMOC-BLIND-EXEC-001"
CASE_ID = "IT-G1-I-AMOC-US-91-12-10-7K0-18-00734"
FORBIDDEN_TERMS = (
    "RECONSTRUCTION_001",
    "IT-G4_I_FAA_AMOC_UTILITY_EXECUTION_RESULT_001",
    "IT-METH-I_FAA_AMOC_INDEPENDENT_RECONSTRUCTION_001",
    "COMPARISON",
)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def scan_tree(root: Path) -> list[str]:
    if not root.exists():
        return [f"MISSING_ROOT:{root}"]
    hits: list[str] = []
    for p in root.rglob("*"):
        if not p.is_file():
            continue
        name = p.name.upper()
        if any(term in name for term in FORBIDDEN_TERMS):
            hits.append(str(p))
    return hits


def path_is_inside(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def control(args: argparse.Namespace) -> dict:
    package = args.package.resolve()
    evidence = args.evidence.resolve()
    output = args.output.resolve()
    package_hash = sha256_file(package) if package.is_file() else None

    checks: dict[str, object] = {}

    checks["PACKAGE_ID"] = PACKAGE_ID
    checks["CASE_ID"] = CASE_ID
    checks["PACKAGE_INTEGRITY"] = (
        "PASS" if package.is_file() and (
            args.expected_package_sha256 is None
            or package_hash == args.expected_package_sha256.lower()
        ) else "FAIL"
    )

    evidence_hits = scan_tree(evidence)
    output_hits = scan_tree(output)
    package_hits = scan_tree(package.parent) if package.is_file() else []

    # P1 is deliberately scoped to the configured blind roots. The harness
    # does not claim that a local user cannot access files outside those roots.
    forbidden_hits = sorted(set(evidence_hits + output_hits + package_hits))
    checks["RECONSTRUCTION_001_ACCESS_STATUS"] = "FAIL" if forbidden_hits else "PASS"
    checks["RECONSTRUCTION_001_ACCESS_EVIDENCE"] = forbidden_hits

    declared_roots = [evidence, package.parent, output]
    undeclared = []
    for p in (package, evidence, output):
        if not any(path_is_inside(p, root) for root in declared_roots):
            undeclared.append(str(p))
    checks["INPUT_BOUNDARY_STATUS"] = "PASS" if not undeclared else "FAIL"
    checks["UNDECLARED_PATHS"] = undeclared

    checks["OUTPUT_BOUNDARY_STATUS"] = (
        "PASS" if output != package.parent and output != evidence else "FAIL"
    )
    checks["SEAL_CAPABILITY_STATUS"] = "PASS" if output.exists() or output.parent.exists() else "FAIL"
    checks["TEMPORAL_ORDERING_STATUS"] = "PASS"  # dry-run records only the control timestamp
    checks["COMPARISON_PRESEAL_STATUS"] = "NOT_PRESENT"
    checks["EXECUTOR_2_DISTINCT"] = "NOT_ESTABLISHED"
    checks["GOVERNANCE_AUTHORIZATION_STATUS"] = "NOT_AUTHORIZED"
    checks["EXECUTION_MODE"] = "DRY_RUN_CONTROL"
    checks["CONTROL_TIMESTAMP_UTC"] = utc_now()
    checks["ENVIRONMENT_FINGERPRINT"] = {
        "python": platform.python_version(),
        "implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "executable": sys.executable,
        "script_sha256": sha256_file(Path(__file__).resolve()),
    }

    technical = [
        checks["PACKAGE_INTEGRITY"] == "PASS",
        checks["RECONSTRUCTION_001_ACCESS_STATUS"] == "PASS",
        checks["INPUT_BOUNDARY_STATUS"] == "PASS",
        checks["OUTPUT_BOUNDARY_STATUS"] == "PASS",
        checks["SEAL_CAPABILITY_STATUS"] == "PASS",
        checks["COMPARISON_PRESEAL_STATUS"] == "NOT_PRESENT",
    ]
    checks["OVERALL_CONTROL_STATUS"] = "PASS" if all(technical) else "BLOCKED"
    checks["INDEPENDENCE_STATUS"] = "NOT_DEMONSTRATED"
    checks["RECONSTRUCTION_002_STATUS"] = "NOT_EXECUTED"
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description="IT-METH-I blind executor control harness")
    parser.add_argument("--package", type=Path, required=True)
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--expected-package-sha256")
    parser.add_argument("--result", type=Path)
    parser.add_argument(
        "--mode",
        choices=("DRY_RUN_CONTROL", "EXECUTION"),
        default="DRY_RUN_CONTROL",
    )
    args = parser.parse_args()

    if args.mode != "DRY_RUN_CONTROL":
        print("BLOCKED: EXECUTION mode is not implemented/authorized by v0.1.")
        return 2

    result = control(args)
    payload = json.dumps(result, indent=2, ensure_ascii=False) + "\n"
    print(payload, end="")

    if args.result:
        args.result.parent.mkdir(parents=True, exist_ok=True)
        args.result.write_text(payload, encoding="utf-8")

    return 0 if result["OVERALL_CONTROL_STATUS"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
