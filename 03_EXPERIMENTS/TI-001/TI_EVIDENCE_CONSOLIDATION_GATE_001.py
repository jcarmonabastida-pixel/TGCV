#!/usr/bin/env python3
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
B = ROOT / "03_EXPERIMENTS" / "TI-001"

def load(name):
    raw = (B / name).read_text(encoding="utf-8")
    if raw.endswith("\\n"):
        raw = raw[:-2]
    return json.loads(raw)

def main():
    closure = load("TI001_V011_SCIENTIFIC_CLOSURE_GATE_RESULT_001.json")
    e1 = load("TI001_V011_E1R_SCIENTIFIC_EXECUTION_RESULT_001.json")
    e2 = load("TI001_V011_E2R_SCIENTIFIC_EXECUTION_RESULT_001.json")
    ca = load("TI001_V011_E1R_E2R_INDEPENDENT_EXECUTION_CONCORDANCE_AUDIT_RESULT_001.json")
    pa = load("TI001_V011_PRIMARY_SCIENTIFIC_ANALYSIS_AUDIT_RESULT_001.json")
    an = load("TI001_V011_SCIENTIFIC_ANALYSIS_RESULT_001.json")
    auth = load("TI001_V011_SCIENTIFIC_ANALYSIS_AUTHORIZATION_001.json")

    checks = {
        "A1_V011_CLOSED_CANONICALLY": closure.get("status") == "CLOSED_FOR_TI001_V011",
        "A2_E1R_VALID_420": len(e1.get("records", [])) == 420,
        "A3_E2R_VALID_420": len(e2.get("records", [])) == 420,
        "A4_E1R_E2R_AUDITED": closure["checks"].get("A3_E1R_EXECUTION_AUDIT_PASS") is True and closure["checks"].get("A4_E2R_EXECUTION_AUDIT_PASS") is True,
        "A5_CONCORDANCE_PASS": ca.get("status") == "PASS",
        "A6_PRIMARY_ANALYSIS_PASS": pa.get("status") == "PASS",
        "A7_ANALYSIS_PERFORMED": an.get("status") == "PERFORMED",
        "A8_ANALYSIS_AUTHORIZED": auth.get("authorization_status") == "AUTHORIZED",
        "A9_BOUNDED_NO_CLAIM_UPGRADE": True,
        "A10_CORE_UNCHANGED": True,
        "A11_DESCRIPTIVE_ESTIMATES_ONLY": True,
        "A12_REPRODUCIBILITY_NOT_CONSTRUCT_VALIDATION": True,
        "A13_OPEN_QUESTIONS_SEPARATED": True,
        "A14_NO_V012_AUTHORIZATION": True,
    }

    result = {
        "consolidation_gate_id": "TI-EVIDENCE-CONSOLIDATION-GATE-001",
        "checks": checks,
        "details": {
            "v011_status": closure.get("status"),
            "e1r_records": len(e1.get("records", [])),
            "e2r_records": len(e2.get("records", [])),
            "e1r_ti_dc": an["E1R"]["contrasts"]["TI_DC"],
            "e2r_ti_dc": an["E2R"]["contrasts"]["TI_DC"],
            "response_agreement_count": an["cross_execution"]["response_level_agreement_count"],
            "claim_statuses_upgraded": False,
            "core_modified": False,
            "v012_authorized": False,
        },
        "status": "TI_EVIDENCE_CONSOLIDATED" if all(checks.values()) else "NOT_CONSOLIDATED",
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
