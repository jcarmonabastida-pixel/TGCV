#!/usr/bin/env python3
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SCHEMA = ROOT / "03_EXPERIMENTS" / "TI-001" / "TI001_V008_DECISION_UNIT_SCHEMA_SPECIFICATION_001.md"
PREFLIGHT_ID = "TI001-V008-DU-SCHEMA-PREFLIGHT-001"
SCHEMA_ID = "TI001-V008-DU-SCHEMA-001"

def git_blob_sha1(data):
    header = ("blob %d\0" % len(data)).encode("utf-8")
    return hashlib.sha1(header + data).hexdigest()

def main():
    if not SCHEMA.exists():
        print(json.dumps({"preflight_id": PREFLIGHT_ID, "schema_id": SCHEMA_ID, "status": "FAIL", "scientific_execution": "NOT_PERFORMED", "fixture_generated": False}))
        raise SystemExit(1)
    data = SCHEMA.read_bytes()
    text = data.decode("utf-8")
    checks = {}
    required = [
        "decision_id", "pair_id", "condition", "presentation",
        "context", "available_actions", "future_structure"
    ]
    checks["schema_exists"] = True
    checks["schema_id"] = SCHEMA_ID in text
    checks["decision_id_range"] = "D001" in text and "D420" in text
    checks["pair_id_range"] = "P001" in text and "P210" in text
    checks["condition_vocabulary"] = all(x in text for x in ["control", "treatment", "null"])
    checks["presentation_vocabulary"] = "I1_FIRST" in text and "I2_FIRST" in text
    checks["seven_decision_unit_fields"] = all(x in text for x in required)
    checks["pair_count_210"] = "exactly 210 pairs" in text
    checks["decision_count_420"] = "420 decision units" in text
    checks["two_per_pair"] = "Each pair contains exactly two decision units" in text
    checks["pair_order"] = "I1_FIRST" in text and "I2_FIRST" in text
    checks["condition_pair_allocation"] = all(x in text for x in ["70 control pairs", "70 treatment pairs", "70 null pairs"])
    checks["condition_decision_allocation"] = all(x in text for x in ["140 control decision units", "140 treatment decision units", "140 null decision units"])
    checks["context_fields"] = "items" in text and "item_count" in text
    checks["action_mapping"] = "I1 → action A" in text and "I2 → action B" in text
    checks["available_actions"] = '["A","B"]' in text
    checks["future_structure"] = "successor_realized" in text and "future_structure_available" in text
    checks["agent_boundary"] = all(x in text for x in ["context", "available_actions", "future_structure"])
    checks["hidden_boundary"] = all(x in text for x in ["decision_id", "pair_id", "condition", "presentation"])
    checks["prohibited_information"] = all(x in text for x in ["utility", "reward", "value", "performance feedback", "observed successor"])
    checks["serialization"] = all(x in text for x in ["UTF-8 encoding", "no insignificant whitespace", "exactly one LF byte", "no BOM"])
    checks["top_level_order"] = all(x in text for x in ["fixture_id", "schema_id", "generator_id", "seed", "decision_units"])
    checks["provenance"] = all(x in text for x in ["TI001-V008-FIXTURE-001", "TI001-V008-FIXTURE-GENERATOR-001", "20260925"])
    checks["executor2_independence"] = "Executor-2" in text and "MUST NOT read" in text
    checks["scientific_not_performed"] = "scientific_execution = NOT_PERFORMED" in text
    checks["generation_prohibited"] = "No fixture may be generated before these conditions are satisfied." in text
    checks["schema_blob_sha1_computable"] = bool(git_blob_sha1(data))
    status = "PASS" if all(checks.values()) else "FAIL"
    result = {
        'preflight_id': PREFLIGHT_ID,
        'schema_id': SCHEMA_ID,
        'schema_path': str(SCHEMA.relative_to(ROOT)).replace('\\\\', '/'),
        'schema_blob_sha1': git_blob_sha1(data),
        'checks': checks,
        'scientific_execution': 'NOT_PERFORMED',
        'fixture_generated': False,
        'status': status
    }
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if status == 'PASS' else 1)

if __name__ == '__main__':
    main()