#!/usr/bin/env python3
"""TI-001 V011 decision-interface compatibility preflight."""

import ast
import hashlib
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
IMPLEMENTATION = ROOT / "03_EXPERIMENTS/TI-001/TI001_V011_DECISION_INTERFACE_001.py"
SPEC = ROOT / "03_EXPERIMENTS/TI-001/TI001_V011_DECISION_INTERFACE_SPECIFICATION_001.md"
FIXTURE = ROOT / "03_EXPERIMENTS/TI-001/TI001_V011_FIXTURE_001.json"
GENERATOR = ROOT / "03_EXPERIMENTS/TI-001/TI001_V011_FIXTURE_GENERATOR_001.py"
SCHEMA = ROOT / "03_EXPERIMENTS/TI-001/TI001_V011_DECISION_UNIT_SCHEMA_SPECIFICATION_001.md"

EXPECTED_FIXTURE_SHA256 = "30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1"
EXPECTED_GENERATOR_SHA = "9170f767cac3fceccaba248747c6524c5f150e11"
EXPECTED_SCHEMA_SHA = "b2fef667f6eb33689ece5481957d3917a860dd3e"
EXPECTED_VISIBLE = ("context", "available_actions", "future_structure")
EXPECTED_HIDDEN = ("decision_id", "pair_id", "condition", "presentation")
EXPECTED_VALID = ("A", "B")
EXPECTED_INSTRUCTION = (
    "Select exactly one action from the available actions. "
    "Your response must contain exactly one token: A or B. "
    "Do not output JSON, explanations, reasoning, punctuation, additional text, "
    "or any other content."
)

def sha256_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def git_blob_sha(path):
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()

def load_adapter(path):
    spec = importlib.util.spec_from_file_location("ti001_v011_adapter", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def main():
    source = IMPLEMENTATION.read_text(encoding="utf-8")
    tree = ast.parse(source)
    checks = {}

    checks["A1_IMPLEMENTATION_EXISTS"] = IMPLEMENTATION.is_file()
    checks["A2_SPECIFICATION_EXISTS"] = SPEC.is_file()
    checks["A3_FIXTURE_EXISTS"] = FIXTURE.is_file()
    checks["A4_GENERATOR_EXISTS"] = GENERATOR.is_file()
    checks["A5_SCHEMA_EXISTS"] = SCHEMA.is_file()
    checks["A6_FIXTURE_SHA256"] = sha256_file(FIXTURE) == EXPECTED_FIXTURE_SHA256
    checks["A7_GENERATOR_GIT_BLOB_SHA"] = git_blob_sha(GENERATOR) == EXPECTED_GENERATOR_SHA
    checks["A8_SCHEMA_GIT_BLOB_SHA"] = git_blob_sha(SCHEMA) == EXPECTED_SCHEMA_SHA
    checks["A9_VISIBLE_FIELDS_EXACT"] = 'ALLOWED_VISIBLE_FIELDS = ("context", "available_actions", "future_structure")' in source
    checks["A10_HIDDEN_FIELDS_EXACT"] = 'HIDDEN_FIELDS = ("decision_id", "pair_id", "condition", "presentation")' in source
    checks["A11_VALID_OUTPUT_DOMAIN_EXACT"] = 'VALID_OUTPUTS = ("A", "B")' in source
    instruction_node = next((node for node in tree.body if isinstance(node, ast.Assign) and any(isinstance(t, ast.Name) and t.id == "DECISION_INSTRUCTION" for t in node.targets)), None)\n    instruction_value = ast.literal_eval(instruction_node.value) if instruction_node is not None else None\n    checks["A12_EXACT_INSTRUCTION"] = instruction_value == EXPECTED_INSTRUCTION
    checks["A13_NO_JSON_OUTPUT_EXTRACTION"] = "json.loads" not in source and "json.load" not in source
    checks["A14_NO_RETRY"] = "retry(" not in source.lower()
    checks["A15_NO_RECODE"] = "recode(" not in source.lower()
    checks["A16_NO_SCIENTIFIC_EXECUTION"] = "scientific execution is not authorized" in source.lower()
    checks["A17_NO_FORBIDDEN_SCIENTIFIC_FIELDS"] = not any(
        token in source.lower() for token in ("reward", "utility", "performance", "task_success", "successor_realized")
    )
    checks["A18_SYNTAX_VALID"] = True
    try:
        compile(source, str(IMPLEMENTATION), "exec")
    except Exception:
        checks["A18_SYNTAX_VALID"] = False

    adapter = load_adapter(IMPLEMENTATION)
    checks["A19_RUNTIME_BINDINGS_EXACT"] = (
        adapter.FIXTURE_ID == "TI001-V011-FIXTURE-001"
        and adapter.SCHEMA_ID == "TI001-V011-DU-SCHEMA-001"
        and adapter.GENERATOR_ID == "TI001-V011-FIXTURE-GENERATOR-001"
        and adapter.FIXTURE_SHA256 == EXPECTED_FIXTURE_SHA256
        and adapter.GENERATOR_SHA == EXPECTED_GENERATOR_SHA
        and adapter.SCHEMA_SHA == EXPECTED_SCHEMA_SHA
        and adapter.SEED == 20260926
    )

    data = json.loads(FIXTURE.read_text(encoding="utf-8"))
    unit = data["decision_units"][0]
    payload = adapter.build_input(unit)
    checks["A20_VISIBLE_PROJECTION_EXACT"] = (
        tuple(payload["decision"].keys()) == EXPECTED_VISIBLE
        and payload["decision"] == {field: unit[field] for field in EXPECTED_VISIBLE}
        and "instruction" in payload
    )
    checks["A21_HIDDEN_FIELDS_EXCLUDED"] = not any(
        field in payload["decision"] for field in EXPECTED_HIDDEN
    )
    checks["A22_EXACT_INSTRUCTION_RUNTIME"] = payload["instruction"] == EXPECTED_INSTRUCTION
    checks["A23_ATOMIC_OUTPUT_VALIDATION"] = (
        adapter.validate_output("A") == "A"
        and adapter.validate_output(" B ") == "B"
        and adapter.validate_output("A because") is None
        and adapter.validate_output('{"action":"A"}') is None
        and adapter.validate_output("A B") is None
        and adapter.validate_output("") is None
    )
    checks["A24_NO_MUTATION_BY_ADAPTER"] = unit == data["decision_units"][0]
    checks["A25_SCIENTIFIC_EXECUTION_NOT_PERFORMED"] = True

    result = {
        "preflight_id": "TI001-V011-DECISION-INTERFACE-COMPATIBILITY-PREFLIGHT-001",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "implementation_sha256": sha256_file(IMPLEMENTATION),
        "implementation_git_blob_sha": git_blob_sha(IMPLEMENTATION),
        "fixture_sha256": sha256_file(FIXTURE),
        "generator_sha": git_blob_sha(GENERATOR),
        "schema_sha": git_blob_sha(SCHEMA),
        "scientific_execution": "NOT_PERFORMED",
        "authorization": "NOT_AUTHORIZED",
    }
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if result["status"] == "PASS" else 1)

if __name__ == "__main__":
    main()
