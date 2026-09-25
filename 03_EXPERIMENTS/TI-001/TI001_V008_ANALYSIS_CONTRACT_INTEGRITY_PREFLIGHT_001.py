#!/usr/bin/env python3
import argparse,hashlib,json
from pathlib import Path

CONTRACT_SHA1="4c94e497e333ecf80072985cbcb4fe05b959609b"
SPEC_SHA1="5cb84ecb96dc08664fc507d5b681d1e3c935437a"
FIXTURE_ID="TI001-V008-FIXTURE-001"
FIXTURE_SHA256="dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"

def blob_sha1(b): return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()

def main():
 p=argparse.ArgumentParser()
 p.add_argument("--contract",required=True); p.add_argument("--spec",required=True); p.add_argument("--fixture",required=True); p.add_argument("--output",required=True)
 a=p.parse_args()
 cb=Path(a.contract).read_bytes(); sb=Path(a.spec).read_bytes(); fb=Path(a.fixture).read_bytes()
 c=json.loads(cb); s=sb.decode("utf-8"); f=json.loads(fb)
 checks={
  "contract_identity":blob_sha1(cb)==CONTRACT_SHA1,
  "spec_identity":blob_sha1(sb)==SPEC_SHA1,
  "fixture_identity":f.get("fixture_id")==FIXTURE_ID and hashlib.sha256(fb).hexdigest()==FIXTURE_SHA256,
  "object_ti":c.get("object")=="Transformational Intelligence",
  "primary_indicator":c.get("primary_indicator")=="TI_DC = q_treatment(A) - q_control(A)",
  "null_reference":c.get("null_reference")=="TI_NULL = q_null(A) - q_control(A)",
  "indicator_bound":c.get("indicator_specification")=="TI001_V008_TI_INDICATOR_SPECIFICATION_001.md" and c.get("indicator_spec_blob_sha1")==SPEC_SHA1,
  "required_outputs_bound":len(c.get("required_outputs",[]))==7,
  "prohibited_value_metrics":all(x in c.get("prohibited_inputs_or_metrics",[]) for x in ["value","reward","utility","performance"]),
  "no_recode":c.get("invalid_response_rule")=="Invalid or non-completed responses are not silently recoded as A or B.",
  "interpretation_boundary":"not, by themselves, causal claims about value" in c.get("interpretation_boundary",""),
  "not_authorized":c.get("scientific_execution")=="NOT_AUTHORIZED",
  "spec_indicator_text":"TI_DC = q_treatment(A) - q_control(A)" in s and "TI_NULL = q_null(A) - q_control(A)" in s,
  "fixture_420":len(f.get("decision_units",[]))==420
 }
 r={"preflight_id":"TI001-V008-ANALYSIS-CONTRACT-INTEGRITY-PREFLIGHT-001","checks":checks,"contract_blob_sha1":blob_sha1(cb),"spec_blob_sha1":blob_sha1(sb),"scientific_execution":"NOT_PERFORMED","status":"PASS" if all(checks.values()) else "FAIL"}
 Path(a.output).write_text(json.dumps(r,indent=2)+"\\n",encoding="utf-8")
if __name__=="__main__": main()
