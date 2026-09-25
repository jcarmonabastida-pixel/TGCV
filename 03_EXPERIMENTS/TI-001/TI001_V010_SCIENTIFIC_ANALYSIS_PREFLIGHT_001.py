#!/usr/bin/env python3
"""TI-001 V010 scientific analysis preflight."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

FIXTURE_SHA256 = "dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"
INTERFACE_SHA256 = "e025d66e477de3afd79147986b716389d7d7be03d01a21d4380b384e17c8510c"
EXECUTOR_1_RESULT_SHA = "5297b578f250a50e90043dab5806877e3c3eec1d"
EXECUTOR_2_RESULT_SHA = "82b09712d1fa866dc25927c62ada1c7da1004665"
EXPECTED_DECISIONS = 420
EXPECTED_PER_CONDITION = 140
EXPECTED_PRESENTATIONS = 210
VALID_OUTPUTS = {"A", "B"}


def sha256_bytes(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def check_result(result, expected_executor_id):
    records = result.get("records", [])
    validity = [r.get("validity") for r in records]
    conditions = [r.get("condition") for r in records]
    presentations = [r.get("presentation") for r in records]
    return {
        "decision_count": len(records) == EXPECTED_DECISIONS,
        "scientific_execution": result.get("scientific_execution") == "PERFORMED",
        "analysis_not_performed": result.get("analysis_performed") is False,
        "executor_identity": result.get("executor_id") == expected_executor_id,
        "all_valid": all(v == "VALID" for v in validity),
        "no_missing_response_ids": all(r.get("response_id") for r in records),
        "condition_balance": all(conditions.count(c) == EXPECTED_PER_CONDITION for c in ("control", "treatment", "null")),
        "presentation_balance": all(presentations.count(p) == EXPECTED_PRESENTATIONS for p in ("I1_FIRST", "I2_FIRST")),
        "outputs_only_A_B": all(r.get("parsed_response") in VALID_OUTPUTS for r in records),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--analysis-spec", required=True)
    parser.add_argument("--fixture", required=True)
    parser.add_argument("--executor-1-result", required=True)
    parser.add_argument("--executor-2-result", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    fixture = Path(args.fixture)
    e1 = Path(args.executor_1_result)
    e2 = Path(args.executor_2_result)
    spec = Path(args.analysis_spec)

    checks = {
        "A1_ANALYSIS_SPEC_PRESENT": spec.exists(),
        "A2_FIXTURE_SHA": sha256_bytes(fixture) == FIXTURE_SHA256,
        "A3_EXECUTOR_1_RESULT_SHA": sha256_bytes(e1) == EXECUTOR_1_RESULT_SHA,
        "A4_EXECUTOR_2_RESULT_SHA": sha256_bytes(e2) == EXECUTOR_2_RESULT_SHA,
        "A5_EXECUTOR_1_STRUCTURE": False,
        "A6_EXECUTOR_2_STRUCTURE": False,
        "A7_NO_POOLING_RULE": "MUST NOT be pooled" in spec.read_text(encoding="utf-8"),
        "A8_TIDC_FORMULA": "TI_DC = q_A(treatment) - q_A(control)" in spec.read_text(encoding="utf-8"),
        "A9_TINULL_FORMULA": "TI_NULL = q_A(null) - q_A(control)" in spec.read_text(encoding="utf-8"),
        "A10_NO_RECODING": "No recoding" in spec.read_text(encoding="utf-8"),
        "A11_NO_RETRY": spec.read_text(encoding="utf-8").count("No retry") == 1,
        "A12_NO_VALUE_METRIC": "value, reward, utility, performance" in spec.read_text(encoding="utf-8"),
        "A13_NO_CAUSAL_CLAIM": "causal impact" in spec.read_text(encoding="utf-8"),
        "A14_PRESENTATION_STRATIFICATION": "I1_FIRST" in spec.read_text(encoding="utf-8") and "I2_FIRST" in spec.read_text(encoding="utf-8"),
        "A15_PAIR_ANALYSIS": "agreement" in spec.read_text(encoding="utf-8") and "210" in spec.read_text(encoding="utf-8"),
        "A16_ANALYSIS_NOT_AUTHORIZED_BY_PREFLIGHT": True,
    }

    r1 = load_json(e1)
    r2 = load_json(e2)
    s1 = check_result(r1, "TI001-V010-SCIENTIFIC-EXECUTOR-1-001")
    s2 = check_result(r2, "TI001-V010-EXECUTOR-2-REPLAY-001")
    checks["A5_EXECUTOR_1_STRUCTURE"] = all(s1.values())
    checks["A6_EXECUTOR_2_STRUCTURE"] = all(s2.values())

    result = {
        "gate_id": "TI001-V010-SCIENTIFIC-ANALYSIS-PREFLIGHT-001",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "executor_1_checks": s1,
        "executor_2_checks": s2,
        "scientific_analysis": "NOT_PERFORMED",
        "authorization": "NOT_AUTHORIZED",
    }
    Path(args.output).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
