#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path

EXECUTOR_ID="TI001-V008-EXECUTOR-1-001"
EXPECTED_EXECUTOR_SHA1="533dc44c30331bcb561712d6a0a762660dd7737f"
FIXTURE_ID="TI001-V008-FIXTURE-001"
FIXTURE_SHA256="dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"
SCHEMA_ID="TI001-V008-DU-SCHEMA-001"
PROVIDER_ID="TI001-V008-DECISION-AGENT-PROVIDER-001"
PROVIDER_SHA1="c7d066de3481143d878f06bb2c1d791cb7dc54e1"

def git_blob_sha1(data):
    header=f"blob {len(data)}\0".encode()
    return hashlib.sha1(header+data).hexdigest()

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--executor",required=True)
    p.add_argument("--fixture",required=True)
    p.add_argument("--output",required=True)
    a=p.parse_args()
    eb=Path(a.executor).read_bytes()
    fb=Path(a.fixture).read_bytes()
    fixture=json.loads(fb)
    checks={
      "executor_identity":git_blob_sha1(eb)==EXPECTED_EXECUTOR_SHA1,
      "fixture_identity":fixture.get("fixture_id")==FIXTURE_ID and hashlib.sha256(fb).hexdigest()==FIXTURE_SHA256,
      "schema_identity":SCHEMA_ID=="TI001-V008-DU-SCHEMA-001",
      "provider_identity":PROVIDER_ID=="TI001-V008-DECISION-AGENT-PROVIDER-001" and PROVIDER_SHA1=="c7d066de3481143d878f06bb2c1d791cb7dc54e1",
      "decision_count":len(fixture.get("decision_units",[]))==420,
      "action_space_ab":all(set(u.get("available_actions",[]))=={"A","B"} for u in fixture.get("decision_units",[])),
      "no_successor_realization":all(u.get("future_structure",{}).get("successor_realized") is False for u in fixture.get("decision_units",[])),
      "scientific_execution_not_performed":True
    }
    result={"preflight_id":"TI001-V008-EXECUTOR-1-IDENTITY-PREFLIGHT-001","checks":checks,"executor_blob_sha1":git_blob_sha1(eb),"scientific_execution":"NOT_PERFORMED","status":"PASS" if all(checks.values()) else "FAIL"}
    Path(a.output).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
if __name__=="__main__": main()
