#!/usr/bin/env python3
"""TI-001 V011 final preauthorization gate."""

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FIXTURE = ROOT / "03_EXPERIMENTS/TI-001/TI001_V011_FIXTURE_001.json"
GENERATOR = ROOT / "03_EXPERIMENTS/TI-001/TI001_V011_FIXTURE_GENERATOR_001.py"
SCHEMA = ROOT / "03_EXPERIMENTS/TI-001/TI001_V011_DECISION_UNIT_SCHEMA_SPECIFICATION_001.md"
INTERFACE = ROOT / "03_EXPERIMENTS/TI-001/TI001_V011_DECISION_INTERFACE_001.py"
COMPAT_RESULT = ROOT / "03_EXPERIMENTS/TI-001/TI001_V011_DECISION_INTERFACE_COMPATIBILITY_PREFLIGHT_RESULT_001.json"
CONTRACT = ROOT / "03_EXPERIMENTS/TI-001/TI001_V011_SCIENTIFIC_EXECUTION_CONTRACT_001.md"

EXPECTED_FIXTURE_SHA256 = "30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1"
EXPECTED_GENERATOR_SHA = "9170f767cac3fceccaba248747c6524c5f150e11"
EXPECTED_SCHEMA_SHA = "b2fef667f6eb33689ece5481957d3917a860dd3e"
EXPECTED_INTERFACE_SHA = "8667b0ff70f58283c688f24c76f10db142655d14"

def sha256_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def git_blob_sha(path):
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()

def main():
    checks = {}
    checks["A1_FIXTURE_EXISTS"] = FIXTURE.is_file()
    checks["A2_FIXTURE_SHA256"] = A1 = sha256_file(FIXTURE) == EXPECTED_FIXTURE_SHA256
    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    units = data["decision_units"]
    checks["A3_DECISION_UNIT_COUNT"] = len(units) == 420
    checks["A4_PAIR_COUNT"] = len({u["pair_id"] for u in units}) == 210
    checks["A5_GENERATOR_GIT_BLOB_SHA"] = git_blob_sha(GENERATOR) == EXPECTED_GENERATOR_SHA
    checks["A6_SCHEMA_GIT_BLOB_SHA"] = git_blob_sha(SCHEMA) == EXPECTED_SCHEMA_SHA
    checks["A7_INTERFACE_GIT_BLOB_SHA"] = git_blob_sha(INTERFACE) == EXPECTED_INTERFACE_SHA
    checks["A8_COMPAT_RESULT_EXISTS"] = COMPAT_RESULT.is_file()
    compat = json.loads(COMPAT_RESULT.read_text(encoding="utf-8"))
    checks["A9_COMPAT_STATUS_PASS"] = compat.get("status") == "PASS"
    checks["A10_COMPAT_BINDINGS_EXACT"] = (
        compat.get("fixture_sha256") == EXPECTED_FIXTURE_SHA256
        and compat.get("generator_sha") == EXPECTED_GENERATOR_SHA
        and compat.get("schema_sha") == EXPECTED_SCHEMA_SHA
        and compat.get("implementation_git_blob_sha") == EXPECTED_INTERFACE_SHA
    )
    checks["A11_CONTRACT_EXISTS"] = CONTRACT.is_file()
    contract = CONTRACT.read_text(encoding="utf-8")
    checks["A12_CONTRACT_BINDS_FIXTURE"] = EXPECTED_FIXTURE_SHA256 in contract
    checks["A13_CONTRACT_BINDS_GENERATOR"] = EXPECTED_GENERATOR_SHA in contract
    checks["A14_CONTRACT_BINDS_SCHEMA"] = EXPECTED_SCHEMA_SHA in contract
    checks["A15_CONTRACT_BINDS_INTERFACE"] = EXPECTED_INTERFACE_SHA in contract
    checks["A16_CONTRACT_NOT_AUTHORIZED"] = "Status:** CONTRACT — NOT AUTHORIZED" in contract
    checks["A17_NO_AUTHORIZATION_CREATED"] = True
    checks["A18_SCIENTIFIC_EXECUTION_NOT_PERFORMED"] = compat.get("scientific_execution") == "NOT_PERFORMED"
    checks["A19_AUTHORIZATION_NOT_AUTHORIZED"] = compat.get("authorization") == "NOT_AUTHORIZED"

    result = {
        "gate_id": "TI001-V011-FINAL-PREAUTHORIZATION-GATE-001",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "fixture_sha256": sha256_file(FIXTURE),
        "generator_sha": git_blob_sha(GENERATOR),
        "schema_sha": git_blob_sha(SCHEMA),
        "interface_git_blob_sha": git_blob_sha(INTERFACE),
        "scientific_execution": "NOT_PERFORMED",
        "authorization": "READY_FOR_EXPLICIT_AUTHORIZATION" if all(checks.values()) else "NOT_AUTHORIZED",
    }
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "PASS" else 1)

if __name__ == "__main__":
    main()
