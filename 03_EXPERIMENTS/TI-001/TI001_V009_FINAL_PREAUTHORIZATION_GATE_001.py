#!/usr/bin/env python3
import argparse,json,hashlib
from pathlib import Path

CONTRACT_SHA1="05a6a755e6898b36c351c8b040ec76c06468a4e6"
RUNNER_SHA1="2618c1ca6191bb616c9c3b064234b062b98ae68b"
FIXTURE_SHA256="dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"

def blob_sha1(b): return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()
def load(path):
    p=Path(path)
    if not p.exists(): return None
    return json.loads(p.read_text(encoding="utf-8"))
def passed(x):
    return x is not None and x.get("status")=="PASS" and x.get("scientific_execution")=="NOT_PERFORMED"

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--contract",required=True)
    p.add_argument("--fixture",required=True)
    p.add_argument("--runtime-contract-preflight-result",required=True)
    p.add_argument("--runner-identity-result",required=True)
    p.add_argument("--executor2-result",required=True)
    p.add_argument("--analysis-result",required=True)
    p.add_argument("--indicator-result",required=True)
    p.add_argument("--analysis-contract-integrity-result",required=True)
    p.add_argument("--output",required=True)
    a=p.parse_args()

    cb=Path(a.contract).read_bytes()
    rb=Path("03_EXPERIMENTS/TI-001/TI001_V009_SCIENTIFIC_EXECUTOR_1_001.py").read_bytes()
    fb=Path(a.fixture).read_bytes()
    c=json.loads(cb)
    rcp=load(a.runtime_contract_preflight_result)
    ri=load(a.runner_identity_result)
    e2=load(a.executor2_result)
    ar=load(a.analysis_result)
    ir=load(a.indicator_result)
    ac=load(a.analysis_contract_integrity_result)

    checks={
      "execution_contract_identity": blob_sha1(cb)==CONTRACT_SHA1,
      "fixture_identity": hashlib.sha256(fb).hexdigest()==FIXTURE_SHA256,
      "scientific_runner_identity": blob_sha1(rb)==RUNNER_SHA1,
      "runtime_contract_preflight_pass": passed(rcp),
      "runner_identity_preflight_pass": passed(ri),
      "executor2_reconstruction_pass": passed(e2),
      "analysis_definition_pass": passed(ar),
      "indicator_definition_pass": passed(ir),
      "analysis_contract_integrity_pass": passed(ac),
      "contract_not_authorized": c.get("status")=="CONTRACT — SCIENTIFIC EXECUTION NOT AUTHORIZED",
      "contract_runtime_reasoning_none": c.get("runtime",{}).get("reasoning")=={"effort":"none"},
      "contract_runtime_max_tokens_64": c.get("runtime",{}).get("max_output_tokens")==64,
      "contract_domain_AB": c.get("decision_domain")==["A","B"] if isinstance(c.get("decision_domain"),list) else True,
      "no_scientific_execution": all(x is None or x.get("scientific_execution")=="NOT_PERFORMED" for x in [rcp,ri,e2,ar,ir,ac]),
      "explicit_authorization_required": c.get("authorization_required") is True
    }
    out={"preflight_id":"TI001-V009-FINAL-PREAUTHORIZATION-GATE-001","checks":checks,"scientific_execution":"NOT_PERFORMED","authorization":"NOT_AUTHORIZED","status":"PASS" if all(checks.values()) else "BLOCKED"}
    Path(a.output).write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")

if __name__=="__main__":
    main()
