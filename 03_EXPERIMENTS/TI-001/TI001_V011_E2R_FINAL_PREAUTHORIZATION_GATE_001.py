#!/usr/bin/env python3
import json, hashlib, subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; BASE=ROOT/"03_EXPERIMENTS"/"TI-001"
FIXTURE=BASE/"TI001_V011_FIXTURE_001.json"; GENERATOR=BASE/"TI001_V011_FIXTURE_GENERATOR_001.py"; SCHEMA=BASE/"TI001_V011_DECISION_UNIT_SCHEMA_SPECIFICATION_001.md"; INTERFACE=BASE/"TI001_V011_DECISION_INTERFACE_001.py"; EXECUTOR=BASE/"TI001_V011_E2R_SCIENTIFIC_EXECUTOR_001.py"; PREFLIGHT=BASE/"TI001_V011_E2R_EXECUTOR_IDENTITY_COMPATIBILITY_PREFLIGHT_RESULT_001.json"; AUTH=BASE/"TI001_V011_E2R_SCIENTIFIC_EXECUTION_AUTHORIZATION_001.json"; RESULT=BASE/"TI001_V011_E2R_SCIENTIFIC_EXECUTION_RESULT_001.json"
F="30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1"; G="9170f767cac3fceccaba248747c6524c5f150e11"; S="b2fef667f6eb33689ece5481957d3917a860dd3e"; I="8667b0ff70f58283c688f24c76f10db142655d14"; E="a8cdb770ffab6d0023c809b7466fe00c2fcd89c6"
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def blob(p): return subprocess.check_output(["git","hash-object",str(p)],text=True).strip()
def main():
 c={}
 c["A1_FIXTURE_SHA_EXACT"]=sha(FIXTURE)==F; c["A2_GENERATOR_BLOB_EXACT"]=blob(GENERATOR)==G; c["A3_SCHEMA_BLOB_EXACT"]=blob(SCHEMA)==S; c["A4_INTERFACE_BLOB_EXACT"]=blob(INTERFACE)==I; c["A5_E2R_EXECUTOR_BLOB_EXACT"]=blob(EXECUTOR)==E
 p=json.loads(PREFLIGHT.read_text(encoding="utf-8")); c["A6_PREFLIGHT_EXISTS_PASS"]=PREFLIGHT.is_file(); c["A7_PREFLIGHT_STATUS_PASS"]=p.get("status")=="PASS"; c["A8_PREFLIGHT_BINDINGS_EXACT"]=all([p.get("executor_blob_sha")==E,p.get("fixture_sha256")==F]); c["A9_E2R_INDEPENDENT"]="E1R" not in EXECUTOR.read_text(encoding="utf-8"); c["A10_DESIGN_BINDS_REASONING_NONE"]= 'REASONING={"effort":"none"}' in EXECUTOR.read_text(encoding="utf-8"); c["A11_NO_E2R_AUTHORIZATION_EXISTS"]=not AUTH.exists(); c["A12_NO_E2R_RESULT_EXISTS"]=not RESULT.exists(); c["A13_GATE_ITSELF_NO_PROVIDER_CALL"]=True
 ok=all(c.values()); out={"gate_id":"TI001-V011-E2R-FINAL-PREAUTHORIZATION-GATE-001","status":"PASS" if ok else "FAIL","checks":c,"executor_blob_sha":blob(EXECUTOR),"fixture_sha256":sha(FIXTURE),"scientific_execution":"NOT_PERFORMED","authorization":"READY_FOR_EXPLICIT_AUTHORIZATION" if ok else "NOT_AUTHORIZED"}; print(json.dumps(out,indent=2,sort_keys=True)); return 0 if ok else 1
if __name__=="__main__": raise SystemExit(main())
