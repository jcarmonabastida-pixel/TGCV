#!/usr/bin/env python3
"""Validate the TGCV ChatGPT bootstrap against canonical GitHub state.

Read-only validator. It resolves the bootstrap-declared canonical state graph
from the local checkout and fails closed on version/pointer inconsistencies.
It does not modify governance artifacts.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BOOTSTRAP = ROOT / "00_GOVERNANCE" / "CHATGPT_BOOTSTRAP.md"
CANONICAL = ROOT / "00_GOVERNANCE" / "CANONICAL_STATE.json"
STATUS = ROOT / "STATUS.md"
RMA_POINTER = ROOT / "00_GOVERNANCE" / "rma" / "TGCV_RMA_current.md"
MATRIX_POINTER = ROOT / "00_GOVERNANCE" / "EVIDENCE_TO_CLAIM_MATRIX_CURRENT_POINTER.md"
TRACE = ROOT / "00_GOVERNANCE" / "rma" / "TGCV_RMA_traceability_current.csv"

EXPECTED_BOOTSTRAP_SCHEMA = "TGCV-CHATGPT-BOOTSTRAP-1"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def version_from(pattern: str, text: str, label: str, errors: list[str]) -> str | None:
    match = re.search(pattern, text)
    if not match:
        errors.append(f"{label}_VERSION_NOT_FOUND")
        return None
    return match.group(1)


def main() -> int:
    errors: list[str] = []

    try:
        bootstrap = read(BOOTSTRAP)
        canonical = json.loads(read(CANONICAL))
        status = read(STATUS)
        rma_pointer = read(RMA_POINTER)
        matrix_pointer = read(MATRIX_POINTER)
        trace = read(TRACE)
    except Exception as exc:
        print("TGCV CHATGPT BOOTSTRAP VALIDATOR")
        print("RESULT=BLOCKED")
        print("ERROR=INPUT_READ_FAILED:" + str(exc))
        return 2

    if EXPECTED_BOOTSTRAP_SCHEMA not in bootstrap:
        errors.append("BOOTSTRAP_SCHEMA_INVALID")

    versions = canonical.get("current_versions", {})
    rma_v = versions.get("rma")
    matrix_v = versions.get("claim_matrix")
    trace_v = versions.get("rma_traceability")

    if canonical.get("status") != "CURRENT":
        errors.append("CANONICAL_STATUS_NOT_CURRENT")
    if not isinstance(canonical.get("pointers"), dict):
        errors.append("CANONICAL_POINTERS_INVALID")

    status_rma = version_from(r"Current RMA:`?[^`\n]*`?\s*→\s*(v\d+\.\d+)", status, "STATUS_RMA", errors)
    status_matrix = version_from(r"Current Evidence→Claim Matrix:`?[^`\n]*`?\s*→\s*(v\d+\.\d+)", status, "STATUS_MATRIX", errors)
    status_trace = version_from(r"Canonical current versions: RMA `([^`]+)`, Evidence→Claim Matrix `([^`]+)`, RMA traceability `([^`]+)`", status, "STATUS_CANONICAL_LINE", errors)
    if status_trace is not None:
        # The helper captures the full line only when the expression is used as a
        # single capture; use a separate strict extraction below.
        pass
    line = re.search(
        r"Canonical current versions: RMA `([^`]+)`, Evidence→Claim Matrix `([^`]+)`, RMA traceability `([^`]+)`,",
        status,
    )
    if not line:
        errors.append("STATUS_CANONICAL_VERSIONS_NOT_FOUND")
        status_versions = (None, None, None)
    else:
        status_versions = line.groups()

    rma_pointer_v = version_from(r"\*\*Current version:\*\*\s*(v\d+\.\d+)", rma_pointer, "RMA_POINTER", errors)
    matrix_pointer_v = version_from(r"\*\*Current version:\*\*\s*(v\d+\.\d+)", matrix_pointer, "MATRIX_POINTER", errors)

    if rma_v != status_rma or rma_v != status_versions[0] or rma_v != rma_pointer_v:
        errors.append("RMA_VERSION_CROSS_REFERENCE_MISMATCH")
    if matrix_v != status_matrix or matrix_v != status_versions[1] or matrix_v != matrix_pointer_v:
        errors.append("MATRIX_VERSION_CROSS_REFERENCE_MISMATCH")
    if trace_v != status_versions[2]:
        errors.append("TRACE_VERSION_CROSS_REFERENCE_MISMATCH")

    rma_path = canonical.get("pointers", {}).get("rma")
    matrix_path = canonical.get("pointers", {}).get("claim_matrix")
    trace_path = canonical.get("pointers", {}).get("rma_traceability")
    status_path = canonical.get("pointers", {}).get("status")
    validator_path = canonical.get("pointers", {}).get("validator")

    expected_paths = {
        "rma": "00_GOVERNANCE/rma/TGCV_RMA_current.md",
        "claim_matrix": "00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md",
        "rma_traceability": "00_GOVERNANCE/rma/TGCV_RMA_traceability_current.csv",
        "status": "STATUS.md",
    }
    actual_paths = {
        "rma": rma_path,
        "claim_matrix": matrix_path,
        "rma_traceability": trace_path,
        "status": status_path,
    }
    for key, expected in expected_paths.items():
        if actual_paths[key] != expected:
            errors.append(f"CANONICAL_POINTER_INVALID:{key}")

    for path in (RMA_POINTER, TRACE, STATUS, BOOTSTRAP):
        if not path.exists():
            errors.append("MISSING_FILE:" + path.relative_to(ROOT).as_posix())

    # The canonical state must identify this validator once integrated.
    if validator_path != "00_GOVERNANCE/tools/validate_chatgpt_bootstrap.py":
        errors.append("BOOTSTRAP_VALIDATOR_POINTER_NOT_INTEGRATED")

    print("TGCV CHATGPT BOOTSTRAP VALIDATOR")
    print("SCHEMA=" + EXPECTED_BOOTSTRAP_SCHEMA)
    print("CANONICAL_RMA=" + str(rma_v))
    print("CANONICAL_MATRIX=" + str(matrix_v))
    print("CANONICAL_TRACE=" + str(trace_v))
    print("RMA_CROSS_REFERENCE=" + ("PASS" if "RMA_VERSION_CROSS_REFERENCE_MISMATCH" not in errors else "FAIL"))
    print("MATRIX_CROSS_REFERENCE=" + ("PASS" if "MATRIX_VERSION_CROSS_REFERENCE_MISMATCH" not in errors else "FAIL"))
    print("TRACE_CROSS_REFERENCE=" + ("PASS" if "TRACE_VERSION_CROSS_REFERENCE_MISMATCH" not in errors else "FAIL"))
    print("BOOTSTRAP_VALIDATOR_INTEGRATION=" + ("PASS" if "BOOTSTRAP_VALIDATOR_POINTER_NOT_INTEGRATED" not in errors else "FAIL"))
    if errors:
        print("RESULT=BLOCKED")
        print("ERRORS=" + "|".join(errors))
        return 2
    print("RESULT=PASS")
    print("READ_ONLY=TRUE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
