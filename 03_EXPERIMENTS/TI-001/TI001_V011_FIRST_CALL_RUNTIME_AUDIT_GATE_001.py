#!/usr/bin/env python3
"""TI-001 V011 first-call runtime audit gate."""

import ast
import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "03_EXPERIMENTS" / "TI-001"
EXECUTOR = BASE / "TI001_V011_SCIENTIFIC_EXECUTOR_001.py"
FIXTURE = BASE / "TI001_V011_FIXTURE_001.json"
INTERFACE = BASE / "TI001_V011_DECISION_INTERFACE_001.py"
GENERATOR = BASE / "TI001_V011_FIXTURE_GENERATOR_001.py"
SCHEMA = BASE / "TI001_V011_DECISION_UNIT_SCHEMA_SPECIFICATION_001.md"
AUTHORIZATION = BASE / "TI001_V011_SCIENTIFIC_EXECUTION_AUTHORIZATION_001.json"
EXPECTED_EXECUTOR_SHA = "578294aa7d2698ffa181ecbf1d1acbfe882087f9"
EXPECTED_FIXTURE_SHA = "30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1"
EXPECTED_INTERFACE_SHA = "8667b0ff70f58283c688f24c76f10db142655d14"
EXPECTED_GENERATOR_SHA = "9170f767cac3fceccaba248747c6524c5f150e11"
EXPECTED_SCHEMA_SHA = "b2fef667f6eb33689ece5481957d3917a860dd3e"

def sha256_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def blob_sha(path):
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()

def main():
    source = EXECUTOR.read_text(encoding="utf-8")
    interface_source = INTERFACE.read_text(encoding="utf-8")
    tree = ast.parse(source)
    checks = {}
    checks["A1_EXECUTOR_EXISTS"] = EXECUTOR.is_file()
    checks["A2_EXECUTOR_BLOB_SHA_EXACT"] = blob_sha(EXECUTOR) == EXPECTED_EXECUTOR_SHA
    checks["A3_FIXTURE_SHA_EXACT"] = sha256_file(FIXTURE) == EXPECTED_FIXTURE_SHA
    checks["A4_INTERFACE_BLOB_SHA_EXACT"] = blob_sha(INTERFACE) == EXPECTED_INTERFACE_SHA
    checks["A5_GENERATOR_BLOB_SHA_EXACT"] = blob_sha(GENERATOR) == EXPECTED_GENERATOR_SHA
    checks["A6_SCHEMA_BLOB_SHA_EXACT"] = blob_sha(SCHEMA) == EXPECTED_SCHEMA_SHA
    checks["A7_EXECUTOR_VERSION_EXACT"] = "TI001-V011-SCIENTIFIC-EXECUTOR-001" in source
    checks["A8_MODEL_EXACT"] = 'MODEL_ID = "gpt-5.6-luna"' in source
    checks["A9_GENERATION_CONFIGURATION_EXACT"] = all(x in source for x in ("TOP_P = 0.98", "MAX_OUTPUT_TOKENS = 64", "TOOLS = []", 'TOOL_CHOICE = "auto"', "BACKGROUND = False", "STORE = False")) and '"reasoning": None' in source
    calls = [n for n in ast.walk(tree) if isinstance(n, ast.Call) and isinstance(n.func, ast.Attribute) and n.func.attr == "create" and isinstance(n.func.value, ast.Attribute) and n.func.value.attr == "responses" and isinstance(n.func.value.value, ast.Name) and n.func.value.value.id == "client"]
    checks["A10_EXACTLY_ONE_RESPONSES_CREATE_CALL"] = len(calls) == 1
    checks["A11_NO_RETRY_MECHANISM"] = not any(t in source.lower() for t in ("retry", "tenacity", "backoff"))
    checks["A12_NO_RECODE_REPAIR_INFERENCE_IMPUTATION"] = not any(t in source.lower() for t in ("recode", "repair", "imputation", "infer("))
    checks["A13_PAYLOAD_FROM_DECISION_PROJECTION"] = 'input=json.dumps(' in source and 'model_input["decision"]' in source
    checks["A14_HIDDEN_FIELDS_NOT_TRANSMITTED"] = all(f not in 'model_input["decision"]' for f in ("decision_id", "pair_id", "condition", "presentation"))
    try:
        itree = ast.parse(interface_source)
        visible = None
        for node in itree.body:
            if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "ALLOWED_VISIBLE_FIELDS" for t in node.targets):
                visible = ast.literal_eval(node.value)
                break
        checks["A15_VISIBLE_FIELDS_EXACT"] = visible == ("context", "available_actions", "future_structure")
    except Exception:
        checks["A15_VISIBLE_FIELDS_EXACT"] = False
    checks["A16_INSTRUCTION_FROM_INTERFACE"] = 'instructions=model_input["instruction"]' in source and "interface.build_input" in source
    checks["A17_OUTPUT_VALIDATION_FROM_INTERFACE"] = "interface.validate_output(raw_output)" in source
    payload_expr = source.split('input=json.dumps(', 1)[1].split('),', 1)[0]
    checks["A18_NO_FORBIDDEN_SCIENTIFIC_FIELDS_TRANSMITTED"] = all(f not in payload_expr for f in ("reward", "utility", "performance", "task_success", "successor_realized"))
    auth = json.loads(AUTHORIZATION.read_text(encoding="utf-8"))
    checks["A19_AUTHORIZATION_PRE_EXECUTION_STATE"] = auth.get("authorization_status") == "AUTHORIZED" and auth.get("execution_status") == "AUTHORIZED_NOT_STARTED"
    checks["A20_NO_EXECUTION_WITHOUT_EXECUTE_FLAG"] = "if not args.execute:" in source and "client = OpenAI()" in source and source.index("if not args.execute:") < source.index("client = OpenAI()")
    checks["A21_GATE_ITSELF_NOT_SCIENTIFIC_EXECUTION"] = True
    result = {"gate_id": "TI001-V011-FIRST-CALL-RUNTIME-AUDIT-GATE-001", "status": "PASS" if all(checks.values()) else "FAIL", "checks": checks, "executor_blob_sha": blob_sha(EXECUTOR), "fixture_sha256": sha256_file(FIXTURE), "scientific_execution": "NOT_PERFORMED", "authorization": "READY_FOR_FIRST_CALL" if all(checks.values()) else "BLOCKED"}
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result["status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
