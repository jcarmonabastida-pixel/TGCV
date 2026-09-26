#!/usr/bin/env python3
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
B=ROOT/"03_EXPERIMENTS"/"TI-001"

def load(p):
    raw=p.read_text(encoding="utf-8")
    if raw.endswith("\\n"): raw=raw[:-2]
    return json.loads(raw)

def main():
    e1=load(B/"TI001_V011_E1R_SCIENTIFIC_EXECUTION_RESULT_001.json")
    e2=load(B/"TI001_V011_E2R_SCIENTIFIC_EXECUTION_RESULT_001.json")
    a1=load(B/"TI001_V011_E1R_PRIMARY_EXECUTION_AUDIT_RESULT_001.json")
    a2=load(B/"TI001_V011_E2R_PRIMARY_EXECUTION_AUDIT_RESULT_001.json")
    ca=load(B/"TI001_V011_E1R_E2R_INDEPENDENT_EXECUTION_CONCORDANCE_AUDIT_RESULT_001.json")
    auth=load(B/"TI001_V011_SCIENTIFIC_ANALYSIS_AUTHORIZATION_001.json")
    an=load(B/"TI001_V011_SCIENTIFIC_ANALYSIS_RESULT_001.json")
    pa=load(B/"TI001_V011_PRIMARY_SCIENTIFIC_ANALYSIS_AUDIT_RESULT_001.json")
    fx=load(B/"TI001_V011_FIXTURE_001.json")

    auth_boundary=auth.get("analysis_boundary",{})
    an_boundary=an.get("analysis_boundary",{})
    checks={
      "A1_E1R_420_VALID": len(e1["records"])==420 and e1.get("valid_count")==420,
      "A2_E2R_420_VALID": len(e2["records"])==420 and e2.get("valid_count")==420,
      "A3_E1R_EXECUTION_AUDIT_PASS": a1.get("status")=="PASS",
      "A4_E2R_EXECUTION_AUDIT_PASS": a2.get("status")=="PASS",
      "A5_CONCORDANCE_AUDIT_PASS": ca.get("status")=="PASS",
      "A6_ANALYSIS_AUTHORIZED": auth.get("authorization_status")=="AUTHORIZED" and auth.get("scientific_analysis")=="AUTHORIZED",
      "A7_ANALYSIS_PERFORMED": an.get("status")=="PERFORMED",
      "A8_PRIMARY_ANALYSIS_AUDIT_PASS": pa.get("status")=="PASS",
      "A9_SEPARATE_NO_POOLING": an_boundary.get("e1r_e2r_separate") is True and an_boundary.get("pooling") is False,
      "A10_NO_RECODE_RETRY_IMPUTATION": auth_boundary.get("pooling") is False and auth_boundary.get("recode") is False and auth_boundary.get("retry") is False and auth_boundary.get("imputation") is False and auth_boundary.get("outcome_dependent_filtering") is False,
      "A11_NO_CAUSAL_VALUE_GENERAL_CLAIM": pa["checks"].get("A13_NO_CAUSAL_VALUE_CLAIM") is True,
      "A12_FIXTURE_420": len(fx["decision_units"])==420,
      "A13_FIXTURE_IDENTITY_PRESERVED": e1.get("fixture_sha256")==e2.get("fixture_sha256")==auth_boundary.get("fixture_sha256",e1.get("fixture_sha256")) if "fixture_sha256" in auth_boundary else e1.get("fixture_sha256")==e2.get("fixture_sha256"),
      "A14_CLOSURE_DOES_NOT_MUTATE_SCIENTIFIC_RESULTS": True,
    }
    result={
      "closure_gate_id":"TI001-V011-SCIENTIFIC-CLOSURE-GATE-001",
      "checks":checks,
      "details":{
        "fixture_sha256":e1.get("fixture_sha256"),
        "e1r_valid_count":e1.get("valid_count"),
        "e2r_valid_count":e2.get("valid_count"),
        "e1r_ti_dc":an["E1R"]["contrasts"]["TI_DC"],
        "e2r_ti_dc":an["E2R"]["contrasts"]["TI_DC"],
        "response_agreement_count":an["cross_execution"]["response_level_agreement_count"],
      },
      "scientific_analysis":"PERFORMED",
      "status":"CLOSED_FOR_TI001_V011" if all(checks.values()) else "NOT_CLOSED"
    }
    print(json.dumps(result,indent=2,ensure_ascii=False))

if __name__=="__main__":
    main()
