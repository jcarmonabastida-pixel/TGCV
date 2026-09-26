#!/usr/bin/env python3
"""TI-001 V011 primary Executor-1 execution audit."""

import ast
import hashlib
import json
import re
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BASE = ROOT / "03_EXPERIMENTS" / "TI-001"
FIXTURE = BASE / "TI001_V011_FIXTURE_001.json"
RESULT = BASE / "TI001_V011_SCIENTIFIC_EXECUTION_E1_RESULT_001.json"
INTERFACE = BASE / "TI001_V011_DECISION_INTERFACE_001.py"

EXPECTED_FIXTURE_SHA = "30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1"
EXPECTED_INTERFACE_SHA = "8667b0ff70f58283c688f24c76f10db142655d14"
EXPECTED_GENERATOR_SHA = "9170f767cac3fceccaba248747c6524c5f150e11"
EXPECTED_SCHEMA_SHA = "b2fef667f6eb33689ece5481957d3917a860dd3e"
EXPECTED_EXECUTOR = "TI001-V011-SCIENTIFIC-EXECUTOR-001"
EXPECTED_MODEL = "gpt-5.6-luna"
EXPECTED_COUNT = 420
EXPECTED_PAIRS = 210
EXPECTED_CONDITIONS = {"control": 70, "treatment": 70, "null": 70}
EXPECTED_PRESENTATIONS = {"I1_FIRST": 210, "I2_FIRST": 210}
FORBIDDEN = ("reward", "utility", "performance", "task_success", "successor_realized", "external_outcome")

def sha256_file(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def parse_timestamp(value):
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except Exception:
        return None

def extract_raw(output_text_repr):
    try:
        value = ast.literal_eval(output_text_repr)
    except Exception:
        return None, False
    return value, isinstance(value, str)

def interface_validator_valid(raw):
    if not isinstance(raw, str):
        return False
    return raw.strip() in ("A", "B")

def main():
    checks = {}
    details = {}
    if not FIXTURE.is_file() or not RESULT.is_file():
        print(json.dumps({"audit_id":"TI001-V011-PRIMARY-EXECUTION-AUDIT-001","status":"FAIL","error":"missing fixture or result"}, indent=2))
        return 1

    fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
    result = json.loads(RESULT.read_text(encoding="utf-8"))
    fixture_units = fixture["decision_units"]
    records = result.get("records", [])

    checks["A1_RESULT_EXISTS_AND_JSON"] = isinstance(result, dict)
    checks["A2_RECORD_TYPE_EXACT"] = result.get("record_type") == "TI001-V011-SCIENTIFIC-EXECUTION"
    checks["A3_SCIENTIFIC_EXECUTION_PERFORMED"] = result.get("scientific_execution") == "PERFORMED"
    checks["A4_FIXTURE_ID_EXACT"] = result.get("fixture_id") == "TI001-V011-FIXTURE-001"
    checks["A5_FIXTURE_SHA_EXACT"] = result.get("fixture_sha256") == EXPECTED_FIXTURE_SHA and sha256_file(FIXTURE) == EXPECTED_FIXTURE_SHA
    checks["A6_INTERFACE_BLOB_EXACT"] = result.get("interface_git_blob_sha") == EXPECTED_INTERFACE_SHA
    checks["A7_GENERATOR_BLOB_EXACT"] = result.get("generator_git_blob_sha") == EXPECTED_GENERATOR_SHA
    checks["A8_SCHEMA_BLOB_EXACT"] = result.get("schema_git_blob_sha") == EXPECTED_SCHEMA_SHA
    checks["A9_EXECUTOR_VERSION_EXACT"] = result.get("executor_version") == EXPECTED_EXECUTOR
    checks["A10_MODEL_EXACT"] = result.get("model_id") == EXPECTED_MODEL
    checks["A11_DECISION_COUNT_420"] = result.get("decision_count") == EXPECTED_COUNT and len(records) == EXPECTED_COUNT

    fixture_ids = [u["decision_id"] for u in fixture_units]
    record_ids = [r.get("decision_id") for r in records]
    checks["A12_DECISION_IDS_UNIQUE"] = len(record_ids) == len(set(record_ids)) == EXPECTED_COUNT
    checks["A13_DECISION_IDS_MATCH_FIXTURE_ORDER"] = record_ids == fixture_ids

    checks["A14_RECORD_METADATA_MATCH_FIXTURE"] = all(
        r.get("pair_id") == u["pair_id"] and
        r.get("condition") == u["condition"] and
        r.get("presentation") == u["presentation"]
        for u, r in zip(fixture_units, records)
    )
    pair_counts = Counter(r.get("pair_id") for r in records)
    checks["A15_EACH_PAIR_EXACTLY_TWICE"] = len(pair_counts) == EXPECTED_PAIRS and all(v == 2 for v in pair_counts.values())
    condition_counts = Counter(r.get("condition") for r in records)
    presentation_counts = Counter(r.get("presentation") for r in records)
    checks["A16_CONDITION_BALANCE"] = dict(condition_counts) == EXPECTED_CONDITIONS
    checks["A17_PRESENTATION_BALANCE"] = dict(presentation_counts) == EXPECTED_PRESENTATIONS

    response_ids = [r.get("response_id") for r in records]
    checks["A18_RESPONSE_IDS_PRESENT_UNIQUE"] = len(response_ids) == EXPECTED_COUNT and None not in response_ids and len(set(response_ids)) == EXPECTED_COUNT

    validity_ok = True
    invalid_count = 0
    reasoning_tokens = 0
    nonzero_reasoning_records = []
    completed_invalid = 0
    for r in records:
        raw, raw_ok = extract_raw(r.get("output_text_repr"))
        valid_by_text = raw_ok and interface_validator_valid(raw)
        recorded_valid = r.get("valid") is True
        recorded_decision = r.get("validated_decision")
        expected_decision = raw.strip() if valid_by_text else None
        if recorded_valid != valid_by_text or recorded_decision != expected_decision:
            validity_ok = False
        if not valid_by_text:
            invalid_count += 1
            if r.get("response_status") == "completed":
                completed_invalid += 1
        usage = r.get("usage") or {}
        rt = (usage.get("output_tokens_details") or {}).get("reasoning_tokens")
        if isinstance(rt, int):
            reasoning_tokens += rt
            if rt > 0:
                nonzero_reasoning_records.append(r.get("decision_id"))

    checks["A19_RESPONSE_VALIDATION_CONSISTENT"] = validity_ok
    observed_valid = sum(1 for r in records if r.get("valid") is True)
    checks["A20_VALID_COUNT_RECOMPUTED"] = observed_valid == 245
    checks["A21_INVALID_RESPONSES_RETAINED"] = invalid_count == EXPECTED_COUNT - observed_valid
    checks["A22_TIMESTAMP_FIELDS_PRESENT_ORDERED"] = all(
        parse_timestamp(r.get("request_timestamp")) is not None and
        parse_timestamp(r.get("response_timestamp")) is not None and
        parse_timestamp(r["response_timestamp"]) >= parse_timestamp(r["request_timestamp"])
        for r in records
    )
    checks["A23_RUNTIME_METADATA_PRESENT"] = all(
        key in result.get("runtime", {}) for key in ("python", "platform", "openai_sdk")
    )

    config = result.get("generation_configuration", {})
    checks["A24_GENERATION_CONFIGURATION_EXACT"] = (
        config.get("background") is False and
        config.get("max_output_tokens") == 64 and
        config.get("reasoning") is None and
        config.get("store") is False and
        config.get("tool_choice") == "auto" and
        config.get("tools") == [] and
        config.get("top_p") == 0.98
    )
    checks["A25_NO_FORBIDDEN_SCIENTIFIC_FIELDS"] = not any(
        key in result for key in FORBIDDEN
    ) and not any(
        any(key in r for key in FORBIDDEN) for r in records
    )
    source_text = RESULT.read_text(encoding="utf-8")
    checks["A26_NO_RETRY_RECODE_REPAIR_IN_RESULT"] = not any(
        token in source_text.lower() for token in ("retry", "recode", "repair", "imputation")
    )
    checks["A27_REASONING_RUNTIME_CONSISTENCY"] = len(nonzero_reasoning_records) == 0

    details["valid_count"] = observed_valid
    details["invalid_count"] = invalid_count
    details["completed_invalid_count"] = completed_invalid
    details["reasoning_tokens_total_observed"] = reasoning_tokens
    details["nonzero_reasoning_record_count"] = len(nonzero_reasoning_records)
    details["nonzero_reasoning_sample"] = nonzero_reasoning_records[:10]
    details["execution_end"] = records[-1].get("response_timestamp") if records else None

    status = "PASS" if all(checks.values()) else "FAIL"
    authorization = "READY_FOR_SCIENTIFIC_ANALYSIS" if status == "PASS" else "BLOCKED_PENDING_RECONCILIATION"
    audit = {
        "audit_id": "TI001-V011-PRIMARY-EXECUTION-AUDIT-001",
        "status": status,
        "checks": checks,
        "details": details,
        "fixture_sha256": EXPECTED_FIXTURE_SHA,
        "executor_version": EXPECTED_EXECUTOR,
        "scientific_execution": "PERFORMED",
        "authorization": authorization
    }
    print(json.dumps(audit, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
