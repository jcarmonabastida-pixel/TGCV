#!/usr/bin/env python3
"""TI-001 V009 scientific Executor-1.

Runtime correction relative to V008: explicitly transmits
reasoning={"effort":"none"} and max_output_tokens=64.
Scientific design and frozen fixture remain V008.
"""
from __future__ import annotations
import argparse, hashlib, json, os
from datetime import datetime, timezone
from pathlib import Path
from openai import OpenAI

PROVIDER_ID="TI001-V008-DECISION-AGENT-PROVIDER-001"
PROVIDER_BLOB_SHA1="c7d066de3481143d878f06bb2c1d791cb7dc54e1"
FIXTURE_ID="TI001-V008-FIXTURE-001"
FIXTURE_SHA256="dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"
SCHEMA_ID="TI001-V008-DU-SCHEMA-001"
MODEL_ID="gpt-5.6-luna"
API_SURFACE="Responses API"
EXECUTOR_ID="TI001-V009-SCIENTIFIC-EXECUTOR-1-001"
TOP_P=0.98
MAX_OUTPUT_TOKENS=64
REASONING={"effort":"none"}
VALID_OUTPUTS={"A","B"}

def load_fixture(path):
    raw=path.read_bytes()
    if hashlib.sha256(raw).hexdigest()!=FIXTURE_SHA256: raise SystemExit("fixture SHA-256 mismatch")
    return json.loads(raw)

def model_input(unit):
    expected={"decision_id","pair_id","condition","presentation","context","available_actions","future_structure"}
    if set(unit)!=expected: raise ValueError("V008 decision-unit schema mismatch")
    if unit["available_actions"]!=["A","B"]: raise ValueError("action space must be exactly A/B")
    if unit["future_structure"]["successor_realized"] is not False: raise ValueError("successor must not be realized")
    return {"context":unit["context"],"available_actions":["A","B"],"future_structure":{
        "successor_realized":False,
        "future_structure_available":bool(unit["future_structure"]["future_structure_available"])}}

def authorization_ok(a):
    return (a.get("scientific_execution")=="AUTHORIZED"
      and a.get("executor_id")==EXECUTOR_ID
      and a.get("fixture_id")==FIXTURE_ID and a.get("fixture_sha256")==FIXTURE_SHA256
      and a.get("provider_id")==PROVIDER_ID and a.get("provider_blob_sha1")==PROVIDER_BLOB_SHA1
      and a.get("model_id")==MODEL_ID and a.get("api_surface")==API_SURFACE
      and a.get("top_p")==TOP_P and a.get("max_output_tokens")==MAX_OUTPUT_TOKENS
      and a.get("reasoning")==REASONING and a.get("temperature") is None
      and a.get("tools")==[] and a.get("conversation") is None
      and a.get("previous_response_id") is None and a.get("store") is False)

def dump(r):
    if hasattr(r,"model_dump"): return r.model_dump()
    if hasattr(r,"to_dict"): return r.to_dict()
    return {"repr":repr(r)}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--fixture",required=True); ap.add_argument("--authorization",required=True); ap.add_argument("--output",required=True)
    args=ap.parse_args()
    fixture=load_fixture(Path(args.fixture))
    auth=json.loads(Path(args.authorization).read_text(encoding="utf-8"))
    if not authorization_ok(auth): raise SystemExit("authorization does not match exact V009 runner binding")
    units=fixture.get("decision_units",[])
    if len(units)!=420: raise SystemExit("fixture must contain exactly 420 decision units")
    if not os.environ.get("OPENAI_API_KEY"): raise SystemExit("OPENAI_API_KEY is required")
    client=OpenAI(); records=[]; started=datetime.now(timezone.utc).isoformat()
    for unit in units:
        visible=model_input(unit)
        record={"decision_id":unit["decision_id"],"pair_id":unit["pair_id"],"condition":unit["condition"],
                "presentation":unit["presentation"],"request":{"model":MODEL_ID,"api_surface":API_SURFACE,
                "temperature":None,"top_p":TOP_P,"max_output_tokens":MAX_OUTPUT_TOKENS,"reasoning":REASONING,
                "tools":[],"tool_choice":"auto","background":False,"previous_response_id":None,
                "conversation":None,"store":False,"input_visible_to_model":visible}}
        try:
            response=client.responses.create(model=MODEL_ID,input=json.dumps(visible,ensure_ascii=False,separators=(",",":")),
                top_p=TOP_P,max_output_tokens=MAX_OUTPUT_TOKENS,reasoning=REASONING,tools=[],tool_choice="auto",
                background=False,store=False)
            text=getattr(response,"output_text","")
            record.update({"response_id":getattr(response,"id",None),"response_status":getattr(response,"status",None),
                           "output_text":text,"raw_response":dump(response)})
            selected=text.strip()
            if selected in VALID_OUTPUTS: record.update({"parsed_response":selected,"validity":"VALID"})
            else: record.update({"parsed_response":None,"validity":"INVALID","validation_error":"invalid model output"})
        except Exception as exc:
            record.update({"response_id":None,"response_status":None,"output_text":None,"parsed_response":None,
                           "validity":"RUNTIME_ERROR","error_type":type(exc).__name__,"error_message":str(exc)})
        records.append(record)
    result={"executor_id":EXECUTOR_ID,"fixture_id":FIXTURE_ID,"fixture_sha256":FIXTURE_SHA256,"schema_id":SCHEMA_ID,
            "provider_id":PROVIDER_ID,"provider_blob_sha1":PROVIDER_BLOB_SHA1,"model_id":MODEL_ID,"api_surface":API_SURFACE,
            "runtime":{"temperature":None,"top_p":TOP_P,"max_output_tokens":MAX_OUTPUT_TOKENS,"reasoning":REASONING,
                       "tools":[],"tool_choice":"auto","background":False,"previous_response_id":None,"conversation":None,"store":False},
            "started_at":started,"completed_at":datetime.now(timezone.utc).isoformat(),"decision_count":len(records),
            "scientific_execution":"PERFORMED","analysis_performed":False,"records":records}
    Path(args.output).write_text(json.dumps(result,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
if __name__=="__main__": main()
