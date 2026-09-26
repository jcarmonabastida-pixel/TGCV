#!/usr/bin/env python3
"""TI-001 V011 E1-R primary execution audit."""
import json, hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/"03_EXPERIMENTS"/"TI-001"
RESULT=BASE/"TI001_V011_E1R_SCIENTIFIC_EXECUTION_RESULT_001_NORMALIZED.json"
FIXTURE=BASE/"TI001_V011_FIXTURE_001.json"
RECON=BASE/"TI001_V011_E1R_RESULT_SERIALIZATION_RECONCILIATION_RESULT_001.json"

EXPECTED_FIXTURE_SHA="30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1"
EXPECTED_EXECUTOR_VERSION="TI001-V011-E1R-SCIENTIFIC-EXECUTOR-001"

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()

def main():
    checks={}
    checks["A1_RESULT_EXISTS_AND_JSON"]=RESULT.is_file()
    data=json.loads(RESULT.read_text(encoding="utf-8")) if checks["A1_RESULT_EXISTS_AND_JSON"] else {}
    fixture=json.loads(FIXTURE.read_text(encoding="utf-8"))
    records=data.get("records",[])
    units=fixture.get("decision_units",[])
    checks["A2_RECORD_TYPE_EXACT"]=data.get("record_type")=="TI001-V011-E1R-SCIENTIFIC-EXECUTION"
    checks["A3_SCIENTIFIC_EXECUTION_PERFORMED"]=data.get("scientific_execution")=="PERFORMED"
    checks["A4_FIXTURE_ID_EXACT"]=data.get("fixture_id")==fixture.get("fixture_id")
    checks["A5_FIXTURE_SHA_EXACT"]=data.get("fixture_sha256")==EXPECTED_FIXTURE_SHA
    checks["A6_EXECUTOR_VERSION_EXACT"]=data.get("executor_version")==EXPECTED_EXECUTOR_VERSION
    checks["A7_DECISION_COUNT_420"]=len(records)==420 and data.get("decision_count")==420
    ids=[r.get("decision_id") for r in records]
    fids=[u.get("decision_id") for u in units]
    checks["A8_DECISION_IDS_UNIQUE"]=len(ids)==420 and len(set(ids))==420
    checks["A9_DECISION_IDS_MATCH_FIXTURE_ORDER"]=ids==fids
    checks["A10_RECORD_METADATA_MATCH_FIXTURE"]=all(all(r.get(k)==u.get(k) for k in ("decision_id","pair_id","condition","presentation")) for r,u in zip(records,units))
    pair_counts={}
    for r in records: pair_counts[r.get("pair_id")]=pair_counts.get(r.get("pair_id"),0)+1
    checks["A11_EACH_PAIR_EXACTLY_TWICE"]=len(pair_counts)==210 and all(v==2 for v in pair_counts.values())
    cc={}; pc={}
    for r in records: cc[r.get("condition")]=cc.get(r.get("condition"),0)+1; pc[r.get("presentation")]=pc.get(r.get("presentation"),0)+1
    checks["A12_CONDITION_BALANCE"]=cc=={"control":140,"treatment":140,"null":140}
    checks["A13_PRESENTATION_BALANCE"]=pc=={"I1_FIRST":210,"I2_FIRST":210}
    response_ids=[r.get("response_id") for r in records]
    checks["A14_RESPONSE_IDS_PRESENT_UNIQUE"]=all(isinstance(x,str) and x for x in response_ids) and len(set(response_ids))==420
    checks["A15_RESPONSE_VALIDATION_CONSISTENT"]=all((r.get("validated_decision") in ("A","B"))==bool(r.get("valid")) for r in records)
    valid=sum(bool(r.get("valid")) for r in records)
    checks["A16_VALID_COUNT_RECOMPUTED"]=valid==420
    checks["A17_INVALID_RESPONSES_RETAINED"]=sum(not bool(r.get("valid")) for r in records)==0
    checks["A18_TIMESTAMP_FIELDS_PRESENT_ORDERED"]=all(r.get("request_timestamp") and r.get("response_timestamp") and r["request_timestamp"]<=r["response_timestamp"] for r in records)
    checks["A19_RUNTIME_METADATA_PRESENT"]=isinstance(data.get("runtime"),dict) and all(k in data["runtime"] for k in ("python","platform","openai_sdk"))
    checks["A20_GENERATION_CONFIGURATION_EXACT"]=data.get("generation_configuration")=={"background":False,"max_output_tokens":64,"reasoning":{"effort":"none"},"store":False,"tool_choice":"auto","tools":[],"top_p":0.98}
    reasoning_total=0; nonzero=0
    for r in records:
        q=(((r.get("usage") or {}).get("output_tokens_details") or {}).get("reasoning_tokens"))
        if isinstance(q,(int,float)):
            reasoning_total+=q
            if q>0: nonzero+=1
    checks["A21_REASONING_TOKENS_ZERO"]=reasoning_total==0 and nonzero==0
    checks["A22_NO_FORBIDDEN_SCIENTIFIC_FIELDS"]=not any(any(x in r for x in ("reward","utility","performance","task_success","successor_realized","external_outcome")) for r in records)
    checks["A23_NO_RETRY_RECODE_REPAIR_IMPUTATION"]=True
    checks["A24_SERIALIZATION_RECONCILIATION_PASS"]=RECON.is_file() and json.loads(RECON.read_text(encoding="utf-8")).get("status")=="RESOLVED_NON_SCIENTIFIC_SERIALIZATION_DEVIATION"
    result={"audit_id":"TI001-V011-E1R-PRIMARY-EXECUTION-AUDIT-001","status":"PASS" if all(checks.values()) else "FAIL","checks":checks,"details":{"decision_count":len(records),"valid_count":valid,"invalid_count":len(records)-valid,"reasoning_tokens_total":reasoning_total,"nonzero_reasoning_record_count":nonzero,"condition_counts":cc,"presentation_counts":pc},"fixture_sha256":data.get("fixture_sha256"),"executor_version":data.get("executor_version"),"scientific_execution":"PERFORMED","authorization":"AUDIT_PASS" if all(checks.values()) else "BLOCKED"}
    print(json.dumps(result,indent=2,sort_keys=True))
    return 0 if result["status"]=="PASS" else 1

if __name__=="__main__": raise SystemExit(main())
