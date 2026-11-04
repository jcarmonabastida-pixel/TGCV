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
CURRENT_STATE_VALIDATOR = ROOT / "00_GOVERNANCE" / "tools" / "validate_current_state.py"

EXPECTED_BOOTSTRAP_SCHEMA = "TGCV-CHATGPT-BOOTSTRAP-1"


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def extract(pattern: str, text: str, label: str, errors: list[str]) -> str | None:
    match = re.search(pattern, text, flags=re.MULTILINE)
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
        read(TRACE)
        read(CURRENT_STATE_VALIDATOR)
    except Exception as exc:
        print("TGCV CHATGPT BOOTSTRAP VALIDATOR")
        print("RESULT=BLOCKED")
        print("ERROR=INPUT_READ_FAILED:" + str(exc))
        return 2

    if EXPECTED_BOOTSTRAP_SCHEMA not in bootstrap:
        errors.append("BOOTSTRAP_SCHEMA_INVALID")

    # IGRT has not been established as a canonical TGCV artifact. The bootstrap
    # must explicitly treat it as non-required rather than blocking on a missing
    # pointer or inventing a status. Future adoption requires a governance decision.
    if "NOT_ESTABLISHED / NOT_REQUIRED_BY_CURRENT_CANONICAL_SCHEMA" not in bootstrap:
        errors.append("IGRT_STATUS_NOT_EXPLICITLY_NON_REQUIRED")
    if re.search(r"→\s*IGRT status", bootstrap):
        errors.append("BOOTSTRAP_STILL_REQUIRES_IGRT_STATUS")

    versions = canonical.get("current_versions", {})
    rma_v = versions.get("rma")
    matrix_v = versions.get("claim_matrix")
    trace_v = versions.get("rma_traceability")

    if canonical.get("status") != "CURRENT":
        errors.append("CANONICAL_STATUS_NOT_CURRENT")
    pointers = canonical.get("pointers")
    if not isinstance(pointers, dict):
        errors.append("CANONICAL_POINTERS_INVALID")
        pointers = {}

    status_rma = extract(r"Current RMA.*?→\s*(v\d+\.\d+)", status, "STATUS_RMA", errors)
    status_matrix = extract(r"Current Evidence→Claim Matrix.*?→\s*(v\d+\.\d+)", status, "STATUS_MATRIX", errors)
    line = re.search(
        r"Canonical current versions: RMA `([^`]+)`, Evidence→Claim Matrix `([^`]+)`, RMA traceability `([^`]+)`,",
        status,
    )
    if not line:
        errors.append("STATUS_CANONICAL_VERSIONS_NOT_FOUND")
        status_versions = (None, None, None)
    else:
        status_versions = line.groups()

    rma_pointer_v = extract(r"\*\*Current version:\*\*\s*(v\d+\.\d+)", rma_pointer, "RMA_POINTER", errors)
    matrix_pointer_v = extract(r"\*\*Current version:\*\*\s*(v\d+\.\d+)", matrix_pointer, "MATRIX_POINTER", errors)

    if rma_v != status_rma or rma_v != status_versions[0] or rma_v != rma_pointer_v:
        errors.append("RMA_VERSION_CROSS_REFERENCE_MISMATCH")
    if matrix_v != status_matrix or matrix_v != status_versions[1] or matrix_v != matrix_pointer_v:
        errors.append("MATRIX_VERSION_CROSS_REFERENCE_MISMATCH")
    if trace_v != status_versions[2]:
        errors.append("TRACE_VERSION_CROSS_REFERENCE_MISMATCH")

    expected_paths = {
        "rma": "00_GOVERNANCE/rma/TGCV_RMA_current.md",
        "claim_matrix": "00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md",
        "claim_matrix_pointer": "00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT_POINTER.md",
        "rma_traceability": "00_GOVERNANCE/rma/TGCV_RMA_traceability_current.csv",
        "governance_operating_principles": "00_GOVERNANCE/GOVERNANCE_OPERATING_PRINCIPLES_v0.1.md",
        "status": "STATUS.md",
        "changelog": "CHANGELOG.md",
        "scientific_registry": "02_EXTERNAL_SCIENCE/SCIENTIFIC_ASSET_REGISTRY_v0.1.md",
        "validator": "00_GOVERNANCE/tools/validate_current_state.py",
    }
    for key, expected in expected_paths.items():
        if pointers.get(key) != expected:
            errors.append(f"CANONICAL_POINTER_INVALID:{key}")
        if not (ROOT / expected).is_file():
            errors.append(f"CANONICAL_POINTER_TARGET_MISSING:{key}")

    for path in (RMA_POINTER, MATRIX_POINTER, TRACE, STATUS, BOOTSTRAP, CURRENT_STATE_VALIDATOR):
        if not path.exists():
            errors.append("MISSING_FILE:" + path.relative_to(ROOT).as_posix())

    print("TGCV CHATGPT BOOTSTRAP VALIDATOR")
    print("SCHEMA=" + EXPECTED_BOOTSTRAP_SCHEMA)
    print("CANONICAL_RMA=" + str(rma_v))
    print("CANONICAL_MATRIX=" + str(matrix_v))
    print("CANONICAL_TRACE=" + str(trace_v))
    print("RMA_CROSS_REFERENCE=" + ("PASS" if "RMA_VERSION_CROSS_REFERENCE_MISMATCH" not in errors else "FAIL"))
    print("MATRIX_CROSS_REFERENCE=" + ("PASS" if "MATRIX_VERSION_CROSS_REFERENCE_MISMATCH" not in errors else "FAIL"))
    print("TRACE_CROSS_REFERENCE=" + ("PASS" if "TRACE_VERSION_CROSS_REFERENCE_MISMATCH" not in errors else "FAIL"))
    print("IGRT_STATUS=NOT_ESTABLISHED_NOT_REQUIRED")
    if errors:
        print("RESULT=BLOCKED")
        print("ERRORS=" + "|".join(errors))
        return 2
    print("RESULT=PASS")
    print("READ_ONLY=TRUE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
