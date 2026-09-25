#!/usr/bin/env python3
"""TI-001 V010 Scientific Execution Contract Preflight."""

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
CONTRACT = ROOT / "03_EXPERIMENTS/TI-001/TI001_V010_SCIENTIFIC_EXECUTION_CONTRACT_001.json"
INTERFACE = ROOT / "03_EXPERIMENTS/TI-001/TI001_V010_DECISION_INTERFACE_001.py"
PREFLIGHT = ROOT / "03_EXPERIMENTS/TI-001/TI001_V010_DECISION_INTERFACE_COMPATIBILITY_PREFLIGHT_RESULT_001.json"

contract = json.loads(CONTRACT.read_text(encoding="utf-8"))

checks = {}

checks["A1_CONTRACT_EXISTS"] = CONTRACT.is_file()
checks["A2_INTERFACE_EXISTS"] = INTERFACE.is_file()
checks["A3_INTERFACE_PREFLIGHT_EXISTS"] = PREFLIGHT.is_file()
checks["A4_STATUS_NOT_AUTHORIZED"] = contract["scientific_execution"] == "NOT_AUTHORIZED"
checks["A5_SCIENTIFIC_OBJECT_TI"] = contract["scientific_object"] == "Transformational Intelligence"
checks["A6_FIXTURE_420"] = contract["frozen_fixture"]["decision_units"] == 420
checks["A7_FIXTURE_210_PAIRS"] = contract["frozen_fixture"]["pairs"] == 210
checks["A8_CONDITIONS_70_EACH"] = contract["frozen_fixture"]["conditions"] == {
    "control": 70, "treatment": 70, "null": 70
}
checks["A9_VISIBLE_FIELDS_EXACT"] = contract["agent_visible_fields"] == [
    "context", "available_actions", "future_structure"
]
checks["A10_HIDDEN_FIELDS_EXACT"] = contract["hidden_fields"] == [
    "decision_id", "pair_id", "condition", "presentation"
]
checks["A11_VALID_OUTPUT_AB"] = contract["valid_outputs"] == ["A", "B"]
checks["A12_RUNTIME_MODEL"] = contract["runtime"]["model"] == "gpt-5.6-luna"
checks["A13_RUNTIME_TOP_P"] = contract["runtime"]["top_p"] == 0.98
checks["A14_RUNTIME_MAX_TOKENS"] = contract["runtime"]["max_output_tokens"] == 64
checks["A15_REASONING_NONE"] = contract["runtime"]["reasoning"] == {"effort": "none"}
checks["A16_NO_TOOLS"] = contract["runtime"]["tools"] == []
checks["A17_NO_RETRY"] = contract["scientific_invariants"]["no_retry"] is True
checks["A18_NO_RECODE"] = contract["scientific_invariants"]["no_recode"] is True
checks["A19_NO_VALUE_INPUT"] = all(
    contract["scientific_invariants"][k] is True
    for k in (
        "no_value_input", "no_reward_input", "no_utility_input",
        "no_performance_input", "no_task_success_input",
        "no_external_outcome_input"
    )
)
checks["A20_NO_SUCCESSOR"] = contract["scientific_invariants"]["no_successor_realization"] is True
checks["A21_NO_EXECUTION_ANALYSIS"] = contract["scientific_invariants"]["no_analysis_during_execution"] is True
checks["A22_NO_CAUSAL_VALUE_ANALYSIS"] = contract["scientific_invariants"]["no_causal_delta_tacc_to_value_analysis"] is True
checks["A23_EXPLICIT_AUTH_REQUIRED"] = contract["authorization_boundary"]["explicit_user_authorization_required"] is True
checks["A24_FINAL_GATE_REQUIRED"] = contract["authorization_boundary"]["final_pre_authorization_gate_required"] is True
checks["A25_INTERFACE_SHA_BOUND"] = contract["decision_interface"]["implementation_sha256"] != ""

result = {
    "preflight_id": "TI001-V010-SCIENTIFIC-EXECUTION-CONTRACT-PREFLIGHT-001",
    "checks": checks,
    "all_checks_pass": all(checks.values()),
    "scientific_execution": "NOT_PERFORMED",
    "authorization": "NOT_AUTHORIZED"
}

print(result)
