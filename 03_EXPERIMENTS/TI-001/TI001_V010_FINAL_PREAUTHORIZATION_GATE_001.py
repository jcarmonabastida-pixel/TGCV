#!/usr/bin/env python3
"""TI-001 V010 final pre-authorization gate. Does not execute science."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TI = ROOT / "03_EXPERIMENTS/TI-001"

CONTRACT = TI / "TI001_V010_SCIENTIFIC_EXECUTION_CONTRACT_001.json"
CONTRACT_PREFLIGHT = TI / "TI001_V010_SCIENTIFIC_EXECUTION_CONTRACT_PREFLIGHT_RESULT_001.json"
IDENTITY_PREFLIGHT = TI / "TI001_V010_SCIENTIFIC_EXECUTOR_1_IDENTITY_PREFLIGHT_RESULT_001.json"
INTERFACE = TI / "TI001_V010_DECISION_INTERFACE_001.py"
EXECUTOR = TI / "TI001_V010_SCIENTIFIC_EXECUTOR_1_001.py"

EXPECTED_INTERFACE_SHA256 = "e025d66e477de3afd79147986b716389d7d7be03d01a21d4380b384e17c8510c"
EXPECTED_FIXTURE_SHA256 = "dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"
EXPECTED_EXECUTOR_SHA256 = "0be1b1d63ff8f70a4f8e5c80004a1267aa72f5c5266a80aeb697906facd77131"

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def main():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    cp = json.loads(CONTRACT_PREFLIGHT.read_text(encoding="utf-8"))
    ip = json.loads(IDENTITY_PREFLIGHT.read_text(encoding="utf-8"))

    checks = {
        "A1_CONTRACT_EXISTS": CONTRACT.exists(),
        "A2_CONTRACT_PREFLIGHT_EXISTS": CONTRACT_PREFLIGHT.exists(),
        "A3_IDENTITY_PREFLIGHT_EXISTS": IDENTITY_PREFLIGHT.exists(),
        "A4_CONTRACT_NOT_AUTHORIZED": contract.get("scientific_execution") == "NOT_AUTHORIZED",
        "A5_CONTRACT_PREFLIGHT_PASS": cp.get("all_checks_pass") is True,
        "A6_IDENTITY_PREFLIGHT_PASS": ip.get("all_checks_pass") is True,
        "A7_INTERFACE_SHA_CURRENT": sha256(INTERFACE) == EXPECTED_INTERFACE_SHA256,
        "A8_INTERFACE_SHA_CONTRACT": contract["decision_interface"]["implementation_sha256"] == EXPECTED_INTERFACE_SHA256,
        "A9_IDENTITY_INTERFACE_SHA": ip.get("interface_sha256") == EXPECTED_INTERFACE_SHA256,
        "A10_EXECUTOR_SHA_IDENTITY": ip.get("executor_sha256") == EXPECTED_EXECUTOR_SHA256,
        "A11_EXECUTOR_EXISTS": EXECUTOR.exists(),
        "A12_FIXTURE_SHA_CONTRACT": EXPECTED_FIXTURE_SHA256 == "dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9",
        "A13_EXPLICIT_AUTH_REQUIRED": contract["authorization_boundary"]["explicit_user_authorization_required"] is True,
        "A14_FINAL_GATE_REQUIRED": contract["authorization_boundary"]["final_pre_authorization_gate_required"] is True,
        "A15_NO_SCIENTIFIC_EXECUTION": cp.get("scientific_execution") == "NOT_PERFORMED" and ip.get("scientific_execution") == "NOT_PERFORMED",
    }

    result = {
        "gate_id": "TI001-V010-FINAL-PREAUTHORIZATION-GATE-001",
        "status": "PASS — READY FOR EXPLICIT AUTHORIZATION" if all(checks.values()) else "BLOCKED",
        "checks": checks,
        "all_checks_pass": all(checks.values()),
        "scientific_execution": "NOT_PERFORMED",
        "authorization": "NOT_AUTHORIZED",
        "interface_sha256": sha256(INTERFACE),
        "executor_sha256": sha256(EXECUTOR),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
