"""IT-METH-I FAA AMOC — Executor-2 isolated runtime v0.1

PRE-R002 PREFLIGHT ONLY.

This runtime is intentionally limited to the controlled transfer directory.
It does not execute Reconstruction 002. It does not access Reconstruction 001,
the TGCV repository, network resources, or any other evidence source.

The runtime establishes the technical execution boundary; it does not by itself
establish human/operator independence or authorization.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import platform
import socket
import sys
from datetime import datetime, timezone

PACKAGE_NAME = "IT-METH-I_FAA_AMOC_BLIND_EXECUTION_PACKAGE_001.md"
EVIDENCE_NAME = "IT-METH-I_FAA_AMOC_FROZEN_EVIDENCE_001.zip"
EXPECTED_PACKAGE_SHA256 = "352F56F5EBF1E5CB43B02D56B38B6A02BCBE3F8DC9B6058AFED8A495550E7A69"
EXPECTED_EVIDENCE_SHA256 = "829A301215FB13EC619EE478DA45FDE4DABF0A3206B7D14F8ECADBF1660EDCBA"


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def resolve_transfer_root(raw: str) -> Path:
    root = Path(raw).resolve()
    if not root.is_dir():
        raise RuntimeError(f"TRANSFER_ROOT_NOT_FOUND: {root}")
    return root


def assert_confined(path: Path, root: Path) -> None:
    try:
        path.resolve().relative_to(root.resolve())
    except ValueError as exc:
        raise RuntimeError(f"ISOLATION_VIOLATION: {path} is outside {root}") from exc


def preflight(root: Path, output: Path) -> dict:
    package = root / PACKAGE_NAME
    evidence = root / EVIDENCE_NAME
    assert_confined(package, root)
    assert_confined(evidence, root)
    assert_confined(output, root)

    checks = {}
    checks["transfer_root_exists"] = root.is_dir()
    checks["package_present"] = package.is_file()
    checks["frozen_evidence_present"] = evidence.is_file()
    checks["package_sha256"] = sha256_file(package) if package.is_file() else None
    checks["evidence_sha256"] = sha256_file(evidence) if evidence.is_file() else None
    checks["package_integrity"] = checks["package_sha256"] == EXPECTED_PACKAGE_SHA256
    checks["evidence_integrity"] = checks["evidence_sha256"] == EXPECTED_EVIDENCE_SHA256

    # Explicit negative controls. These are boundary assertions, not claims of
    # human/operator independence.
    checks["r001_reference_supplied"] = False
    checks["tgcv_repo_reference_supplied"] = False
    checks["network_execution_requested"] = False
    checks["r002_execution_performed"] = False

    technical_pass = all(
        checks[k] is True
        for k in (
            "transfer_root_exists",
            "package_present",
            "frozen_evidence_present",
            "package_integrity",
            "evidence_integrity",
            "r001_reference_supplied",
            "tgcv_repo_reference_supplied",
            "network_execution_requested",
            "r002_execution_performed",
        )
    )

    result = {
        "PACKAGE_ID": "IT-METH-I-AMOC-BLIND-EXEC-001",
        "CASE_ID": "IT-G1-I-AMOC-US-91-12-10-7K0-18-00734",
        "RUNTIME_ID": "IT-METH-I-AMOC-EXECUTOR-2-ISOLATED-RUNTIME-001",
        "RUNTIME_VERSION": "v0.1",
        "MODE": "PRE_R002_ISOLATION_PREFLIGHT",
        "TIMESTAMP_UTC": utc_now(),
        "TRANSFER_ROOT": str(root),
        "EXECUTION_HOST": platform.node(),
        "PLATFORM": platform.platform(),
        "PYTHON": sys.version,
        "NETWORK_EXPECTED": "DISABLED_BY_SANDBOX_CONTROL",
        "CHECKS": checks,
        "TECHNICAL_ISOLATION_PREFLIGHT": "PASS" if technical_pass else "FAIL",
        "R002_STATUS": "NOT_EXECUTED",
        "EXECUTOR_2_INDEPENDENCE": "NOT_ESTABLISHED_BY_RUNTIME",
        "AUTHORIZATION": "INHERITED_FROM_IT-G5-002; NOT_REISSUED_BY_RUNTIME",
        "NOTE": "This runtime only establishes a pre-R002 technical boundary. It must not be treated as proof of human/operator independence.",
    }

    output.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--transfer-root", required=True)
    parser.add_argument("--output", default="executor_2_isolation_preflight.json")
    args = parser.parse_args()

    root = resolve_transfer_root(args.transfer_root)
    output = (root / args.output).resolve()
    assert_confined(output, root)

    result = preflight(root, output)
    print(json.dumps(result, indent=2, ensure_ascii=False))
    return 0 if result["TECHNICAL_ISOLATION_PREFLIGHT"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
