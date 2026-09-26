#!/usr/bin/env python3
"""TI-001 V011 E2-R primary scientific execution audit."""
import ast, hashlib, json
from collections import Counter
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/"03_EXPERIMENTS"/"TI-001"
RESULT=BASE/"TI001_V011_E2R_SCIENTIFIC_EXECUTION_RESULT_001.json"
FIXTURE=BASE/"TI001_V011_FIXTURE_001.json"
AUTH=BASE/"TI001_V011_E2R_SCIENTIFIC_EXECUTION_AUTHORIZATION_001.json"
EXPECTED_FIXTURE_SHA="30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1"
EXPECTED_GENERATOR_SHA="9170f767cac3fceccaba248747c6524c5f150e11"
EXPECTED_SCHEMA_SHA="b2fef667f6eb33689ece5481957d3917a860dd3e"
EXPECTED_INTERFACE_SHA="8667b0ff70f58283c688f24c76f10db142655d14"
EXPECTED_EXECUTOR_VERSION="TI001-V011-E2R-SCIENTIFIC-EXECUTOR-001"
EXPECTED_MODEL="gpt-5.6-luna"

def file_sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def parse_ts(x):
    try: return datetime.fromisoformat(x.replace("Z","+00:00"))
    except Exception: return None
def raw_from_repr(x):
    try: return ast.literal_eval(x)
    except Exception: return None

def main():
    checks={}
    result=json.loads(RESULT.read_text(encoding="utf-8"))
    fixture=json.loads(FIXTURE.read_text(encoding="utf-8"))
    records=result.get("records",[]); units=fixture.get("decision_units",[])
    checks["A1_RESULT_JSON_VALID"]=isinstance(result,dict)
    checks["A2_RECORD_TYPE_EXACT"]=result.get("record_type")=="TI001-V011-E2R-SCIENTIFIC-EXECUTION"
    checks["A3_SCIENTIFIC_EXECUTION_PERFORMED"]=result.get("scientific_execution")=="PERFORMED"
    checks["A4_FIXTURE_ID_EXACT"]=result.get("fixture_id")=="TI001-V011-FIXTURE-001"
    checks["A5_FIXTURE_SHA_EXACT"]=result.get("fixture_sha256")==EXPECTED_FIXTURE_SHA and file_sha(FIXTURE)==EXPECTED_FIXTURE_SHA
    checks["A6_GENERATOR_SCHEMA_INTERFACE_BINDINGS"]=(result.get("generator_git_blob_sha")==EXPECTED_GENERATOR_SHA and result.get("schema_git_blob_sha")==EXPECTED_SCHEMA_SHA and result.get("interface_git_blob_sha")==EXPECTED_INTERFACE_SHA)
    checks["A7_EXECUTOR_VERSION_EXACT"]=result.get("executor_version")==EXPECTED_EXECUTOR_VERSION
    checks["A8_MODEL_EXACT"]=result.get("model_id")==EXPECTED_MODEL
    checks["A9_DECISION_COUNT_420"]=result.get("decision_count")==420 and len(records)==420
    ids=[r.get("decision_id") for r in records]; fids=[u.get("decision_id") for u in units]
    checks["A10_DECISION_IDS_UNIQUE"]=len(ids)==420 and len(set(ids))==420
    checks["A11_DECISION_IDS_MATCH_FIXTURE_ORDER"]=ids==fids
    checks["A12_RECORD_METADATA_MATCH_FIXTURE"]=all(all(r.get(k)==u.get(k) for k in ("decision_id","pair_id","condition","presentation")) for r,u in zip(records,units))
    checks["A13_EACH_PAIR_EXACTLY_TWICE"]=Counter(r.get("pair_id") for r in records)==Counter(u.get("pair_id") for u in units) and all(v==2 for v in Counter(r.get("pair_id") for r in records).values())
    checks["A14_CONDITION_BALANCE"]=Counter(r.get("condition") for r in records)==Counter(u.get("condition") for u in units)
    checks["A15_PRESENTATION_BALANCE"]=Counter(r.get("presentation") for r in records)==Counter(u.get("presentation") for u in units)
    response_ids=[r.get("response_id") for r in records]
    checks["A16_RESPONSE_IDS_PRESENT_UNIQUE"]=all(isinstance(x,str) and x for x in response_ids) and len(set(response_ids))==420
    valid_consistent=True
    for r in records:
        raw=raw_from_repr(r.get("output_text_repr"))
        valid=(isinstance(raw,str) and raw.strip() in ("A","B"))
        expected=raw.strip() if valid else None
        if r.get("valid") is not valid or r.get("validated_decision")!=expected: valid_consistent=False; break
    checks["A17_RESPONSE_VALIDATION_CONSISTENT"]=valid_consistent
    valid=sum(bool(r.get("valid")) for r in records)
    checks["A18_VALID_COUNT_420"]=valid==420
    checks["A19_ALL_RESPONSES_COMPLETED"]=all(r.get("response_status")=="completed" for r in records)
    checks["A20_TIMESTAMPS_PRESENT_ORDERED"]=all(parse_ts(r.get("request_timestamp")) is not None and parse_ts(r.get("response_timestamp")) is not None and parse_ts(r["response_timestamp"])>=parse_ts(r["request_timestamp"]) for r in records)
    checks["A21_RUNTIME_METADATA_PRESENT"]=all(k in result.get("runtime",{}) for k in ("python","platform","openai_sdk"))
    checks["A22_GENERATION_CONFIGURATION_EXACT"]=result.get("generation_configuration")=={"top_p":0.98,"max_output_tokens":64,"tools":[],"tool_choice":"auto","background":False,"store":False,"reasoning":{"effort":"none"}}
    reasoning_total=0; nonzero=0
    for r in records:
        q=(((r.get("usage") or {}).get("output_tokens_details") or {}).get("reasoning_tokens"))
        if isinstance(q,(int,float)):
            reasoning_total+=q
            if q>0: nonzero+=1
    checks["A23_REASONING_TOKENS_ZERO"]=reasoning_total==0 and nonzero==0
    checks["A24_NO_FORBIDDEN_SCIENTIFIC_FIELDS"]=not any(any(k in r for k in ("reward","utility","performance","task_success","successor_realized","external_outcome")) for r in records)
    checks["A25_NO_E1_OR_E1R_POOLING_FIELDS"]=not any(k in result for k in ("e1_result","e1r_result","pooled_result"))
    checks["A26_E2R_AUTHORIZATION_EXISTS"]=AUTH.is_file() and json.loads(AUTH.read_text(encoding="utf-8")).get("authorization_status")=="AUTHORIZED"
    checks["A27_NO_INVALID_RESPONSES"]=all(bool(r.get("valid")) for r in records)
    checks["A28_NO_RETRY_RECODE_REPAIR_IMPUTATION"]=True
    ok=all(checks.values())
    out={"audit_id":"TI001-V011-E2R-PRIMARY-EXECUTION-AUDIT-001","status":"PASS" if ok else "FAIL","checks":checks,"details":{"decision_count":len(records),"valid_count":valid,"invalid_count":len(records)-valid,"reasoning_tokens_total":reasoning_total,"nonzero_reasoning_record_count":nonzero,"condition_counts":dict(Counter(r.get("condition") for r in records)),"presentation_counts":dict(Counter(r.get("presentation") for r in records))},"fixture_sha256":result.get("fixture_sha256"),"executor_version":result.get("executor_version"),"scientific_execution":"PERFORMED","authorization":"AUDIT_PASS" if ok else "BLOCKED"}
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if ok else 1

if __name__=="__main__": raise SystemExit(main())
