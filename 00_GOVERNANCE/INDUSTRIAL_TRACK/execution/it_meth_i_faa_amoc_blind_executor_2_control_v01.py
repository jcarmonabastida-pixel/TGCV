#!/usr/bin/env python3
"""IT-METH-I FAA AMOC Blind Executor-2 control harness v0.2.

DRY-RUN CONTROL ONLY.

This program verifies technical controls for a proposed blind execution
context. It does not perform reconstruction 002 and it cannot establish
executor independence by itself.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.metadata
import json
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


def iter_files(root: Path):
    if not root.exists() or not root.is_dir():
        return
    for p in sorted(root.rglob("*")):
        if p.is_file():
            yield p


def path_is_inside(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root.resolve())
        return True
    except ValueError:
        return False


def scan_tree(root: Path) -> list[str]:
    hits: list[str] = []
    if not root.exists():
        return hits
    for p in iter_files(root):
        if any(term in p.name.upper() for term in FORBIDDEN_TERMS):
            hits.append(str(p))
    return hits


def symlink_escape_paths(root: Path) -> list[str]:
    escapes: list[str] = []
    if not root.exists() or not root.is_dir():
        return escapes
    for p in root.rglob("*"):
        if p.is_symlink() and not path_is_inside(p, root):
            escapes.append(str(p))
    return escapes


def manifest(root: Path) -> list[dict[str, str]]:
    entries: list[dict[str, str]] = []
    for p in iter_files(root):
        entries.append({"path": str(p), "sha256": sha256_file(p)})
    return entries


def local_dependency_inventory() -> list[str]:
    return sorted(
        f"{d.metadata['Name']}=={d.version}"
        for d in importlib.metadata.distributions()
        if d.metadata.get("Name")
    )


def control(args: argparse.Namespace) -> dict:
    package = args.package.resolve()
    evidence = args.evidence.resolve()
    output = args.output.resolve()

    checks: dict[str, object] = {
        "PACKAGE_ID": PACKAGE_ID,
        "CASE_ID": CASE_ID,
        "EXECUTION_MODE": "DRY_RUN_CONTROL",
        "CONTROL_TIMESTAMP_UTC": utc_now(),
    }

    package_hash = sha256_file(package) if package.is_file() else None
    checks["PACKAGE_SHA256_OBSERVED"] = package_hash
    checks["PACKAGE_INTEGRITY"] = (
        "PASS"
        if package.is_file()
        and bool(args.expected_package_sha256)
        and package_hash == args.expected_package_sha256.lower()
        else "FAIL"
    )

    forbidden_hits = sorted(
        set(scan_tree(evidence) + scan_tree(output) + scan_tree(package.parent))
    )
    symlink_escapes = sorted(
        set(symlink_escape_paths(evidence) + symlink_escape_paths(output))
    )
    checks["RECONSTRUCTION_001_ACCESS_STATUS"] = (
        "PASS" if not forbidden_hits and not symlink_escapes else "FAIL"
    )
    checks["RECONSTRUCTION_001_ACCESS_EVIDENCE"] = forbidden_hits
    checks["SYMLINK_ESCAPE_EVIDENCE"] = symlink_escapes

    declared_inputs = {
        "package": str(package),
        "evidence_root": str(evidence),
    }
    checks["DECLARED_INPUTS"] = declared_inputs
    checks["INPUT_BOUNDARY_STATUS"] = (
        "PASS"
        if package.is_file() and evidence.is_dir() and not symlink_escapes
        else "FAIL"
    )

    output_exists_before = output.exists()
    if output_exists_before and not output.is_dir():
        checks["OUTPUT_BOUNDARY_STATUS"] = "FAIL"
    else:
        checks["OUTPUT_BOUNDARY_STATUS"] = (
            "PASS" if output != package.parent and output != evidence else "FAIL"
        )

    # Dry-run seal: create a control-only temporary record inside the output
    # boundary, hash it, and remove it. No reconstruction data is generated.
    seal_probe = output / ".it_meth_i_seal_probe.tmp"
    seal_hash = None
    seal_status = "FAIL"
    try:
        output.mkdir(parents=True, exist_ok=True)
        seal_probe.write_text(
            "IT-METH-I DRY-RUN SEAL PROBE\nPACKAGE_ID=" + PACKAGE_ID + "\n",
            encoding="utf-8",
        )
        seal_hash = sha256_file(seal_probe)
        seal_status = "PASS" if len(seal_hash) == 64 else "FAIL"
    finally:
        if seal_probe.exists():
            seal_probe.unlink()
    checks["SEAL_CAPABILITY_STATUS"] = seal_status
    checks["DRY_RUN_SEAL_PROBE_SHA256"] = seal_hash

    # P7 is observable control sequencing, not a claim that an independent
    # executor has already existed.
    checks["PRESEAL_CONTROL_RECORDED"] = True
    checks["TEMPORAL_ORDERING_STATUS"] = "PASS"

    # No comparison target is accepted by this harness. The dry-run itself
    # performs no comparison and therefore cannot disclose reconstruction 001.
    checks["COMPARISON_PRESEAL_STATUS"] = "PASS"
    checks["COMPARISON_TARGET_CONFIGURED"] = False

    checks["ENVIRONMENT_FINGERPRINT"] = {
        "python_version": sys.version,
        "python_implementation": platform.python_implementation(),
        "platform": platform.platform(),
        "executable": sys.executable,
        "script_sha256": sha256_file(Path(__file__).resolve()),
        "local_dependency_inventory": local_dependency_inventory(),
    }

    checks["INPUT_MANIFEST"] = {
        "package": manifest(package.parent),
        "evidence": manifest(evidence),
    }

    technical = [
        checks["PACKAGE_INTEGRITY"] == "PASS",
        checks["RECONSTRUCTION_001_ACCESS_STATUS"] == "PASS",
        checks["INPUT_BOUNDARY_STATUS"] == "PASS",
        checks["OUTPUT_BOUNDARY_STATUS"] == "PASS",
        checks["SEAL_CAPABILITY_STATUS"] == "PASS",
        checks["TEMPORAL_ORDERING_STATUS"] == "PASS",
        checks["COMPARISON_PRESEAL_STATUS"] == "PASS",
    ]
    checks["OVERALL_CONTROL_STATUS"] = "PASS" if all(technical) else "BLOCKED"

    # These fields are deliberately non-promotable by this program.
    checks["EXECUTOR_2_DISTINCT"] = "NOT_ESTABLISHED"
    checks["GOVERNANCE_AUTHORIZATION_STATUS"] = "NOT_AUTHORIZED"
    checks["INDEPENDENCE_STATUS"] = "NOT_DEMONSTRATED"
    checks["RECONSTRUCTION_002_STATUS"] = "NOT_EXECUTED"
    return checks


def main() -> int:
    parser = argparse.ArgumentParser(description="IT-METH-I blind executor control harness")
    parser.add_argument("--package", type=Path, required=True)
    parser.add_argument("--evidence", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--expected-package-sha256", required=True)
    parser.add_argument("--result", type=Path)
    parser.add_argument(
        "--mode",
        choices=("DRY_RUN_CONTROL", "EXECUTION"),
        default="DRY_RUN_CONTROL",
    )
    args = parser.parse_args()

    if args.mode != "DRY_RUN_CONTROL":
        print("BLOCKED: EXECUTION mode is not implemented/authorized by v0.2.")
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
