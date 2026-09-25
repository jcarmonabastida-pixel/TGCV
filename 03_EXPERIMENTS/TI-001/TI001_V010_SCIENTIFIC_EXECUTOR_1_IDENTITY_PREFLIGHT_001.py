#!/usr/bin/env python3
"""TI-001 V010 Scientific Executor-1 identity preflight."""
from __future__ import annotations

import ast
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
EXECUTOR = ROOT / "03_EXPERIMENTS/TI-001/TI001_V010_SCIENTIFIC_EXECUTOR_1_001.py"
INTERFACE = ROOT / "03_EXPERIMENTS/TI-001/TI001_V010_DECISION_INTERFACE_001.py"
CONTRACT = ROOT / "03_EXPERIMENTS/TI-001/TI001_V010_SCIENTIFIC_EXECUTION_CONTRACT_001.json"

EXPECTED_EXECUTOR_ID = "TI001-V010-SCIENTIFIC-EXECUTOR-1-001"
EXPECTED_INTERFACE_ID = "TI001-V010-DECISION-INTERFACE-001"
EXPECTED_INTERFACE_SHA256 = "e025d66e477de3afd79147986b716389d7d7be03d01a21d4380b384e17c8510c"
EXPECTED_FIXTURE_ID = "TI001-V008-FIXTURE-001"
EXPECTED_FIXTURE_SHA256 = "dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"
EXPECTED_MODEL = "gpt-5.6-luna"
EXPECTED_API = "Responses API"

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()

def source_text() -> str:
    return EXECUTOR.read_text(encoding="utf-8")

def main():
    src = source_text()
    tree = ast.parse(src)
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))

    constants = {
        node.targets[0].id: ast.literal_eval(node.value)
        for node in tree.body
        if isinstance(node, ast.Assign)
        and len(node.targets) == 1
        and isinstance(node.targets[0], ast.Name)
        and isinstance(node.value, (ast.Constant, ast.Set, ast.Dict, ast.List, ast.Tuple))
    }

    checks = {
        "A1_EXECUTOR_EXISTS": EXECUTOR.exists(),
        "A2_INTERFACE_EXISTS": INTERFACE.exists(),
        "A3_CONTRACT_EXISTS": CONTRACT.exists(),
        "A4_EXECUTOR_ID": constants.get("EXECUTOR_ID") == EXPECTED_EXECUTOR_ID,
        "A5_FIXTURE_ID": constants.get("FIXTURE_ID") == EXPECTED_FIXTURE_ID,
        "A6_FIXTURE_SHA256": constants.get("FIXTURE_SHA256") == EXPECTED_FIXTURE_SHA256,
        "A7_INTERFACE_ID": constants.get("INTERFACE_ID") == EXPECTED_INTERFACE_ID,
        "A8_INTERFACE_SHA256": constants.get("INTERFACE_SHA256") == EXPECTED_INTERFACE_SHA256,
        "A9_INTERFACE_HASH_CURRENT": sha256(INTERFACE) == EXPECTED_INTERFACE_SHA256,
        "A10_MODEL": constants.get("MODEL_ID") == EXPECTED_MODEL,
        "A11_API_SURFACE": constants.get("API_SURFACE") == EXPECTED_API,
        "A12_TOP_P": constants.get("TOP_P") == 0.98,
        "A13_MAX_OUTPUT_TOKENS": constants.get("MAX_OUTPUT_TOKENS") == 64,
        "A14_REASONING_NONE": constants.get("REASONING") == {"effort": "none"},
        "A15_VALID_OUTPUTS_AB": constants.get("VALID_OUTPUTS") == {"A", "B"},
        "A16_NO_RETRY_CALL": "retry(" not in src,
        "A17_NO_RECODE_CALL": "recode(" not in src,
        "A18_NO_ANALYSIS_DURING_EXECUTION": 'analysis_performed": False' in src,
        "A19_CONTRACT_EXECUTOR_BINDING": contract["execution_identity"]["executor_1"] == "TO_BE_BOUND_BY_V010_RUNNER_IDENTITY_PREFLIGHT",
        "A20_CONTRACT_INTERFACE_HASH": contract["decision_interface"]["implementation_sha256"] == EXPECTED_INTERFACE_SHA256,
    }

    result = {
        "preflight_id": "TI001-V010-SCIENTIFIC-EXECUTOR-1-IDENTITY-PREFLIGHT-001",
        "checks": checks,
        "all_checks_pass": all(checks.values()),
        "scientific_execution": "NOT_PERFORMED",
        "authorization": "NOT_AUTHORIZED",
        "executor_sha256": sha256(EXECUTOR),
        "interface_sha256": sha256(INTERFACE),
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
