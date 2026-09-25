#!/usr/bin/env python3
import argparse,json,hashlib
from pathlib import Path

CONTRACT_SHA1="64efcdad2aa0be52774588c90956087426d67d9d"
AMENDMENT_SHA1="90c6fa41493bd233db1222c4047431b80e401c39"
RUNNER_SHA1="04a1b6cf37197499988579e5636c72a445a03a16"
FIXTURE_SHA256="dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"

def blob_sha1(b): return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()

def load(path):
    p=Path(path)
    if not p.exists(): return None
    return json.loads(p.read_text(encoding="utf-8"))

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--contract",required=True)
    p.add_argument("--fixture",required=True)
    p.add_argument("--runtime-result",required=True)
    p.add_argument("--executor1-result",required=True)
    p.add_argument("--amendment",required=True)
    p.add_argument("--scientific-runner",required=True)
    p.add_argument("--executor2-result",required=True)
    p.add_argument("--analysis-result",required=True)
    p.add_argument("--indicator-result",required=True)
    p.add_argument("--contract-integrity-result",required=True)
    p.add_argument("--output",required=True)
    a=p.parse_args()

    cb=Path(a.contract).read_bytes()
    ab=Path(a.amendment).read_bytes()
    rb=Path(a.scientific_runner).read_bytes()
    fb=Path(a.fixture).read_bytes()
    c=json.loads(cb); f=json.loads(fb)
    rr=load(a.runtime_result); e1=load(a.executor1_result); e2=load(a.executor2_result)
    ar=load(a.analysis_result); ir=load(a.indicator_result); cr=load(a.contract_integrity_result)

    def passed(x): return x is not None and x.get("status")=="PASS" and x.get("scientific_execution")=="NOT_PERFORMED"

    checks={
      "execution_contract_identity": blob_sha1(cb)==CONTRACT_SHA1,
      "fixture_identity": hashlib.sha256(fb).hexdigest()==FIXTURE_SHA256,
      "amendment_identity": blob_sha1(ab)==AMENDMENT_SHA1,
      "scientific_runner_identity": blob_sha1(rb)==RUNNER_SHA1,
      "runtime_compatibility_pass": passed(rr),
      "executor1_identity_pass": passed(e1),
      "executor2_reconstruction_pass": passed(e2),
      "analysis_definition_pass": passed(ar),
      "indicator_definition_pass": passed(ir),
      "analysis_contract_integrity_pass": passed(cr),
      "contract_not_authorized": c.get("scientific_execution")=="NOT_AUTHORIZED",
      "amendment_binds_runner": RUNNER_SHA1 in ab.decode("utf-8") and CONTRACT_SHA1 in ab.decode("utf-8"),
      "no_scientific_execution": all(x is None or x.get("scientific_execution")=="NOT_PERFORMED" for x in [rr,e1,e2,ar,ir,cr])
    }
    r={"preflight_id":"TI001-V008-FINAL-PREAUTHORIZATION-GATE-001","checks":checks,"scientific_execution":"NOT_PERFORMED","authorization":"NOT_AUTHORIZED","status":"PASS" if all(checks.values()) else "BLOCKED"}
    Path(a.output).write_text(json.dumps(r,indent=2)+"\n",encoding="utf-8")

if __name__=="__main__": main()
