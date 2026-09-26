#!/usr/bin/env python3
"""TI-001 V011 E2-R executor identity/compatibility preflight."""
import ast, hashlib, json, subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]; BASE=ROOT/"03_EXPERIMENTS"/"TI-001"
EXECUTOR=BASE/"TI001_V011_E2R_SCIENTIFIC_EXECUTOR_001.py"; FIXTURE=BASE/"TI001_V011_FIXTURE_001.json"; INTERFACE=BASE/"TI001_V011_DECISION_INTERFACE_001.py"; GENERATOR=BASE/"TI001_V011_FIXTURE_GENERATOR_001.py"; SCHEMA=BASE/"TI001_V011_DECISION_UNIT_SCHEMA_SPECIFICATION_001.md"
EXPECTED_EXECUTOR_SHA="f4f1e1d5b4a17e0b0b4c9a6d4e1e8e7e4c1d5b3a"
EXPECTED_FIXTURE_SHA="30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1"; EXPECTED_INTERFACE_SHA="8667b0ff70f58283c688f24c76f10db142655d14"; EXPECTED_GENERATOR_SHA="9170f767cac3fceccaba248747c6524c5f150e11"; EXPECTED_SCHEMA_SHA="b2fef667f6eb33689ece5481957d3917a860dd3e"

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def blob(p): return subprocess.check_output(["git","hash-object",str(p)],text=True).strip()
def main():
    s=EXECUTOR.read_text(encoding="utf-8"); t=ast.parse(s); checks={}
    checks["A1_EXECUTOR_EXISTS"]=EXECUTOR.is_file(); checks["A2_EXECUTOR_BLOB_SHA_EXACT"]=blob(EXECUTOR)==EXPECTED_EXECUTOR_SHA
    checks["A3_FIXTURE_SHA_EXACT"]=sha(FIXTURE)==EXPECTED_FIXTURE_SHA; checks["A4_INTERFACE_BLOB_SHA_EXACT"]=blob(INTERFACE)==EXPECTED_INTERFACE_SHA; checks["A5_GENERATOR_BLOB_SHA_EXACT"]=blob(GENERATOR)==EXPECTED_GENERATOR_SHA; checks["A6_SCHEMA_BLOB_SHA_EXACT"]=blob(SCHEMA)==EXPECTED_SCHEMA_SHA
    checks["A7_EXECUTOR_VERSION_EXACT"]='EXECUTOR_VERSION="TI001-V011-E2R-SCIENTIFIC-EXECUTOR-001"' in s
    calls=[n for n in ast.walk(t) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=="create" and isinstance(n.func.value,ast.Attribute) and n.func.value.attr=="responses" and isinstance(n.func.value.value,ast.Name) and n.func.value.value.id=="client"]
    checks["A8_EXACTLY_ONE_RESPONSES_CREATE_CALL"]=len(calls)==1
    checks["A9_MODEL_EXACT"]='MODEL_ID="gpt-5.6-luna"' in s
    checks["A10_GENERATION_CONFIGURATION_EXACT"]=all(x in s for x in ("TOP_P=0.98","MAX_OUTPUT_TOKENS=64","TOOLS=[]",'TOOL_CHOICE="auto"',"BACKGROUND=False","STORE=False"))
    checks["A11_REASONING_EXPLICIT_NONE"]='REASONING={"effort":"none"}' in s; checks["A12_REASONING_TRANSMITTED"]="reasoning=REASONING" in s; checks["A13_REASONING_PERSISTED"]='"reasoning":REASONING' in s
    checks["A14_PAYLOAD_FROM_INTERFACE"]='model_input["decision"]' in s and "interface.build_input" in s
    checks["A15_NO_E1R_DEPENDENCY"]="E1R_SCIENTIFIC_EXECUTOR" not in s and "E1R" not in s
    checks["A16_INDEPENDENT_RESULT_IDENTITY"]='"record_type":"TI001-V011-E2R-SCIENTIFIC-EXECUTION"' in s
    checks["A17_INSTRUCTION_FROM_INTERFACE"]='instructions=model_input["instruction"]' in s
    checks["A18_VALIDATOR_FROM_INTERFACE"]="interface.validate_output(raw)" in s
    low=s.lower(); checks["A19_NO_RETRY_REPAIR_RECODE_IMPUTATION"]=not any(x in low for x in ("retry","repair","recode","imputation","infer("))
    checks["A20_NO_FORBIDDEN_SCIENTIFIC_FIELDS"]=not any(x in s for x in ("reward","utility","performance","task_success","successor_realized","external_outcome"))
    checks["A21_SEPARATE_AUTHORIZATION_REQUIRED"]="AUTHORIZATION=BASE" in s and "authorization_status" in s
    checks["A22_NO_PROVIDER_CALL_IN_PREFLIGHT"]=True
    result={"preflight_id":"TI001-V011-E2R-EXECUTOR-IDENTITY-COMPATIBILITY-PREFLIGHT-001","status":"PASS" if all(checks.values()) else "FAIL","checks":checks,"executor_blob_sha":blob(EXECUTOR),"fixture_sha256":sha(FIXTURE),"reasoning":{"effort":"none"},"scientific_execution":"NOT_PERFORMED","authorization":"READY_FOR_FINAL_PREAUTHORIZATION" if all(checks.values()) else "NOT_AUTHORIZED"}
    print(json.dumps(result,indent=2,sort_keys=True)); return 0 if result["status"]=="PASS" else 1
if __name__=="__main__": raise SystemExit(main())
