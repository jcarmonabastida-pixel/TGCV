#!/usr/bin/env python3
"""TI-001 V010 Decision-Interface Compatibility Preflight."""

import ast
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
IMPLEMENTATION = ROOT / "03_EXPERIMENTS/TI-001/TI001_V010_DECISION_INTERFACE_001.py"
SPEC = ROOT / "03_EXPERIMENTS/TI-001/TI001_V010_DECISION_INTERFACE_SPECIFICATION_001.md"

EXPECTED_VISIBLE = {"context", "available_actions", "future_structure"}
EXPECTED_HIDDEN = {"decision_id", "pair_id", "condition", "presentation"}
EXPECTED_VALID = {"A", "B"}

source = IMPLEMENTATION.read_text(encoding="utf-8")
tree = ast.parse(source)

checks = {}

checks["A1_IMPLEMENTATION_EXISTS"] = IMPLEMENTATION.is_file()
checks["A2_SPECIFICATION_EXISTS"] = SPEC.is_file()
checks["A3_EXPLICIT_DECISION_INSTRUCTION"] = (
    "Select exactly one action" in source
    and "exactly one token: A or B" in source
)
checks["A4_VISIBLE_FIELDS_EXACT"] = (
    'ALLOWED_VISIBLE_FIELDS = ("context", "available_actions", "future_structure")'
    in source
)
checks["A5_HIDDEN_FIELDS_DECLARED"] = (
    'HIDDEN_FIELDS = ("decision_id", "pair_id", "condition", "presentation")'
    in source
)
checks["A6_VALID_OUTPUT_DOMAIN_EXACT"] = (
    'VALID_OUTPUTS = ("A", "B")' in source
)
checks["A7_NO_JSON_OUTPUT_EXTRACTION"] = (
    "json.loads" not in source and "json.load" not in source
)
checks["A8_ATOMIC_OUTPUT_VALIDATION"] = (
    'normalized = output_text.strip()' in source
    and 'normalized in VALID_OUTPUTS' in source
)
checks["A9_NO_RETRY"] = "retry(" not in source.lower()
checks["A10_NO_RECODE"] = "recode(" not in source.lower()
checks["A11_NO_SCIENTIFIC_EXECUTION"] = (
    "scientific execution is not authorized" in source.lower()
)
checks["A12_NO_VALUE_REWARD_UTILITY"] = not any(
    token in source.lower()
    for token in ("reward", "utility", "performance", "task_success")
)
checks["A13_NO_SUCCESSOR_REALIZATION"] = "successor" not in source.lower()
checks["A14_SYNTAX_VALID"] = True

try:
    compile(source, str(IMPLEMENTATION), "exec")
except Exception:
    checks["A14_SYNTAX_VALID"] = False

result = {
    "preflight_id": "TI001-V010-DECISION-INTERFACE-COMPATIBILITY-PREFLIGHT-001",
    "checks": checks,
    "all_checks_pass": all(checks.values()),
    "implementation_sha256": hashlib.sha256(source.encode("utf-8")).hexdigest(),
    "scientific_execution": "NOT_PERFORMED",
    "authorization": "NOT_AUTHORIZED",
}

print(result)
