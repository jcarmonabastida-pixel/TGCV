#!/usr/bin/env python3
import hashlib,json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; B=ROOT/"03_EXPERIMENTS"/"TI-001"
E1R=B/"TI001_V011_E1R_SCIENTIFIC_EXECUTION_RESULT_001.json"; E2R=B/"TI001_V011_E2R_SCIENTIFIC_EXECUTION_RESULT_001.json"
A1=B/"TI001_V011_E1R_PRIMARY_EXECUTION_AUDIT_RESULT_001.json"; A2=B/"TI001_V011_E2R_PRIMARY_EXECUTION_AUDIT_RESULT_001.json"
F=B/"TI001_V011_FIXTURE_001.json"
F_SHA="30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1"
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def load(p):
    raw=p.read_text(encoding="utf-8")
    if raw.endswith("\\n"):
        raw=raw[:-2]
    return json.loads(raw)
def main():
 c={}; d={}
 e1,e2,a1,a2,fx=map(load,(E1R,E2R,A1,A2,F)); r1=e1["records"]; r2=e2["records"]; units=fx["decision_units"]
 c["A1_E1R_AUDIT_PASS"]=a1.get("status")=="PASS"; c["A2_E2R_AUDIT_PASS"]=a2.get("status")=="PASS"
 c["A3_DISTINCT_EXECUTOR_IDENTITIES"]=e1.get("executor_version")!=e2.get("executor_version")
 c["A4_DISTINCT_RESULT_FILES"]=E1R.resolve()!=E2R.resolve()
 c["A5_SAME_FIXTURE_BINDING"]=all(x.get("fixture_sha256")==F_SHA for x in (e1,e2)) and sha(F)==F_SHA
 c["A6_SAME_INTERFACE_GENERATOR_SCHEMA"]=all(e1.get(k)==e2.get(k) for k in ("interface_git_blob_sha","generator_git_blob_sha","schema_git_blob_sha"))
 c["A7_EACH_420_RECORDS"]=len(r1)==420 and len(r2)==420
 c["A8_EACH_FIXTURE_ORDER"]= [x.get("decision_id") for x in r1]==[u.get("decision_id") for u in units] and [x.get("decision_id") for x in r2]==[u.get("decision_id") for u in units]
 c["A9_EACH_BALANCED"]=all(Counter(x.get("condition") for x in r)=={"control":140,"treatment":140,"null":140} and Counter(x.get("presentation") for x in r)=={"I1_FIRST":210,"I2_FIRST":210} for r in (r1,r2))
 c["A10_EACH_ALL_VALID"]=all(all(bool(x.get("valid")) and x.get("validated_decision") in ("A","B") for x in r) for r in (r1,r2))
 c["A11_EACH_REASONING_ZERO"]=all(sum((((x.get("usage") or {}).get("output_tokens_details") or {}).get("reasoning_tokens") or 0) for x in r)==0 for r in (r1,r2))
 c["A12_EACH_RESPONSE_IDS_UNIQUE"]=all(len({x.get("response_id") for x in r})==420 for r in (r1,r2))
 ids1={x.get("response_id") for x in r1}; ids2={x.get("response_id") for x in r2}
 c["A13_RESPONSE_IDS_DISJOINT"]=ids1.isdisjoint(ids2)
 s1=json.dumps(e1,sort_keys=True); s2=json.dumps(e2,sort_keys=True)
 c["A14_NO_CROSS_RESULT_REFERENCE"]=("E2R_SCIENTIFIC_EXECUTION_RESULT_001" not in s1 and "E1R_SCIENTIFIC_EXECUTION_RESULT_001" not in s2 and "pooled_result" not in s1 and "pooled_result" not in s2)
 c["A15_SEPARATE_RUNTIME_METADATA"]=e1.get("runtime") is not None and e2.get("runtime") is not None
 c["A16_NO_FORBIDDEN_EXECUTION_FIELDS"]=all(not any(k in x for k in ("reward","utility","performance","task_success","successor_realized","external_outcome")) for r in (r1,r2) for x in r)
 c["A17_NO_POOLING_OR_RECODING_MARKERS"]=all(not any(k in json.dumps(e,sort_keys=True).lower() for k in ("pooled","majority vote","imputation","recode","retry","repair")) for e in (e1,e2))
 c["A18_NO_SCIENTIFIC_ESTIMANDS_IN_RESULTS"]=all(not any(k in e for k in ("TI_DC","TI_NULL","q_A","presentation_contrast","estimand")) for e in (e1,e2))
 c["A19_AGREEMENT_NOT_USED_AS_VALIDITY"]=True
 c["A20_GATE_NO_ESTIMATION"]=True
 ok=all(c.values()); d={"e1r_valid":sum(bool(x.get("valid")) for x in r1),"e2r_valid":sum(bool(x.get("valid")) for x in r2),"e1r_executor":e1.get("executor_version"),"e2r_executor":e2.get("executor_version"),"response_id_overlap":len(ids1&ids2)}
 out={"audit_id":"TI001-V011-E1R-E2R-INDEPENDENT-EXECUTION-CONCORDANCE-AUDIT-001","status":"PASS" if ok else "FAIL","authorization":"READY_FOR_SCIENTIFIC_ANALYSIS" if ok else "BLOCKED","checks":c,"details":d,"scientific_analysis":"NOT_PERFORMED"}; print(json.dumps(out,indent=2,sort_keys=True)); return 0 if ok else 1
if __name__=="__main__": raise SystemExit(main())
