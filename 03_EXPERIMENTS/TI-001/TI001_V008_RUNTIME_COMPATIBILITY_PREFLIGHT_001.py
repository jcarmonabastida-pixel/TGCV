#!/usr/bin/env python3
"""TI-001 V008 runtime compatibility preflight.
Infrastructure gate only. Never consumes a V008 decision unit.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

FIXTURE_SHA256="dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"
PROVIDER_ID="TI001-V008-DECISION-AGENT-PROVIDER-001"
PROVIDER_BLOB="c7d066de3481143d878f06bb2c1d791cb7dc54e1"
SCHEMA_ID="TI001-V008-DU-SCHEMA-001"
SCHEMA_BLOB="d9539790452b047bc845a19bdcf50b8713a42b2a"
CONTRACT_ID="TI001_V008_EXECUTION_CONTRACT_001"
MODEL="gpt-5.6-luna"

def blob_sha1(raw: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()

def read_json(path: str):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def main(argv):
    p=argparse.ArgumentParser()
    p.add_argument("--provider",required=True)
    p.add_argument("--contract",required=True)
    p.add_argument("--fixture-manifest",required=True)
    p.add_argument("--runtime-record",required=True)
    p.add_argument("--output",required=True)
    a=p.parse_args(argv[1:])

    provider_raw=Path(a.provider).read_bytes()
    provider=provider_raw.decode("utf-8")
    contract=json.loads(Path(a.contract).read_text(encoding="utf-8"))
    manifest=read_json(a.fixture_manifest)
    runtime=read_json(a.runtime_record)
    checks={}

    checks["provider_identity"]=PROVIDER_ID in provider
    checks["provider_blob_sha"]=blob_sha1(provider_raw)==PROVIDER_BLOB
    checks["schema_identity"]=SCHEMA_ID in provider and SCHEMA_BLOB in provider
    checks["fixture_identity"]=manifest.get("fixture_sha256")==FIXTURE_SHA256
    checks["contract_identity"]=contract.get("contract_id")==CONTRACT_ID
    checks["model_identity"]=runtime.get("model_id")==MODEL
    checks["api_surface"]=runtime.get("api_surface")=="Responses API"
    checks["temperature_omitted"]=runtime.get("temperature") in (None,"OMITTED")
    checks["top_p"]=runtime.get("top_p")==0.98
    checks["max_output_tokens"]=runtime.get("max_output_tokens")==16
    checks["tools_empty"]=runtime.get("tools")==[]
    checks["conversation_absent"]=runtime.get("conversation") is None
    checks["previous_response_absent"]=runtime.get("previous_response_id") is None
    checks["store_false"]=runtime.get("store") is False
    checks["hidden_fields_isolated"]=all(x not in provider for x in ['unit["decision_id"]','unit["pair_id"]','unit["condition"]','unit["presentation"]'])
    checks["ab_only"]=all(x in provider for x in ['"A"','"B"'])
    checks["invalid_no_retry_or_recode"]=all(x in provider for x in ['invalid model output','raise ValueError'])
    checks["no_successor_realization"]= "successor must not be realized before decision" in provider
    checks["no_scientific_inputs_consumed"]=runtime.get("fixture_inputs_consumed") is False
    checks["diagnostic_only"]=runtime.get("diagnostic_only") is True
    checks["diagnostic_completed"]=runtime.get("status")=="completed"
    checks["diagnostic_non_scientific"]=runtime.get("scientific_execution")=="NOT_PERFORMED"
    checks["diagnostic_response_present"]=bool(runtime.get("response_id")) and bool(runtime.get("output_text"))
    checks["scientific_execution_not_authorized"]=contract.get("scientific_execution")=="NOT_AUTHORIZED"

    out={
        "preflight_id":"TI001-V008-RUNTIME-COMPATIBILITY-PREFLIGHT-001",
        "checks":checks,
        "provider_blob_sha1":blob_sha1(provider_raw),
        "fixture_sha256":manifest.get("fixture_sha256"),
        "scientific_execution":"NOT_PERFORMED",
        "status":"PASS" if all(checks.values()) else "FAIL"
    }
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if out["status"]=="PASS" else 1

if __name__=="__main__":
    raise SystemExit(main(__import__("sys").argv))
