#!/usr/bin/env python3
"""TI-001 V011 E2-R independent scientific executor.

This implementation is intentionally independent of the E1-R executor.
It loads the frozen fixture/interface directly and performs one provider
request per unit with reasoning.effort="none".
"""
from __future__ import annotations
import argparse, hashlib, importlib.metadata, importlib.util, json, platform, subprocess, sys
from datetime import datetime, timezone
from pathlib import Path
from openai import OpenAI

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/"03_EXPERIMENTS"/"TI-001"
FIXTURE=BASE/"TI001_V011_FIXTURE_001.json"
INTERFACE=BASE/"TI001_V011_DECISION_INTERFACE_001.py"
GENERATOR=BASE/"TI001_V011_FIXTURE_GENERATOR_001.py"
SCHEMA=BASE/"TI001_V011_DECISION_UNIT_SCHEMA_SPECIFICATION_001.md"
AUTHORIZATION=BASE/"TI001_V011_E2R_SCIENTIFIC_EXECUTION_AUTHORIZATION_001.json"

FIXTURE_SHA256="30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1"
GENERATOR_SHA="9170f767cac3fceccaba248747c6524c5f150e11"
SCHEMA_SHA="b2fef667f6eb33689ece5481957d3917a860dd3e"
INTERFACE_SHA="8667b0ff70f58283c688f24c76f10db142655d14"
MODEL_ID="gpt-5.6-luna"
TOP_P=0.98
MAX_OUTPUT_TOKENS=64
TOOLS=[]
TOOL_CHOICE="auto"
BACKGROUND=False
STORE=False
REASONING={"effort":"none"}
EXECUTOR_VERSION="TI001-V011-E2R-SCIENTIFIC-EXECUTOR-001"

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def blob(p): return subprocess.check_output(["git","hash-object",str(p)],text=True).strip()
def load_interface():
    spec=importlib.util.spec_from_file_location("ti001_v011_interface_e2r",INTERFACE)
    if spec is None or spec.loader is None: raise RuntimeError("cannot load V011 interface")
    m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
def load_fixture(): return json.loads(FIXTURE.read_text(encoding="utf-8"))
def load_auth(): return json.loads(AUTHORIZATION.read_text(encoding="utf-8"))

def bindings(fixture,interface,auth):
    return {
        "fixture_sha256":sha(FIXTURE)==FIXTURE_SHA256,
        "generator_blob_sha":blob(GENERATOR)==GENERATOR_SHA,
        "schema_blob_sha":blob(SCHEMA)==SCHEMA_SHA,
        "interface_blob_sha":blob(INTERFACE)==INTERFACE_SHA,
        "fixture_id":fixture.get("fixture_id")==interface.FIXTURE_ID,
        "decision_unit_count":len(fixture.get("decision_units",[]))==420,
        "authorization_present":AUTHORIZATION.is_file(),
        "authorization_record_type":auth.get("record_type")=="TI001-V011-E2R-SCIENTIFIC-EXECUTION-AUTHORIZATION",
        "interface_fixture_binding":interface.FIXTURE_SHA256==FIXTURE_SHA256,
        "interface_generator_binding":interface.GENERATOR_SHA==GENERATOR_SHA,
        "interface_schema_binding":interface.SCHEMA_SHA==SCHEMA_SHA,
    }

def main(argv):
    ap=argparse.ArgumentParser(); ap.add_argument("--output",required=True); ap.add_argument("--execute",action="store_true")
    args=ap.parse_args(argv[1:])
    fixture=load_fixture(); interface=load_interface(); auth=load_auth(); checks=bindings(fixture,interface,auth)
    if not all(checks.values()):
        print(json.dumps({"status":"BINDING_FAIL","checks":checks,"scientific_execution":"NOT_PERFORMED"},indent=2)); return 1
    if not args.execute:
        print(json.dumps({"status":"READY_NOT_EXECUTED","executor_version":EXECUTOR_VERSION,"checks":checks,"fixture_sha256":FIXTURE_SHA256,"reasoning":REASONING,"scientific_execution":"NOT_PERFORMED"},indent=2,sort_keys=True)); return 0
    if auth.get("authorization_status")!="AUTHORIZED":
        print(json.dumps({"status":"AUTHORIZATION_BLOCKED","scientific_execution":"NOT_PERFORMED","authorization":auth.get("authorization_status")},indent=2)); return 1
    client=OpenAI(); records=[]
    for unit in fixture["decision_units"]:
        model_input=interface.build_input(unit)
        request_timestamp=datetime.now(timezone.utc).isoformat()
        response=client.responses.create(model=MODEL_ID,instructions=model_input["instruction"],input=json.dumps(model_input["decision"],sort_keys=True,separators=(",",":"),ensure_ascii=False),top_p=TOP_P,max_output_tokens=MAX_OUTPUT_TOKENS,tools=TOOLS,tool_choice=TOOL_CHOICE,background=BACKGROUND,store=STORE,reasoning=REASONING)
        response_timestamp=datetime.now(timezone.utc).isoformat()
        raw=response.output_text; validated=interface.validate_output(raw); usage=getattr(response,"usage",None)
        records.append({"decision_id":unit["decision_id"],"pair_id":unit["pair_id"],"condition":unit["condition"],"presentation":unit["presentation"],"response_id":response.id,"response_status":response.status,"output_text_repr":repr(raw),"validated_decision":validated,"valid":validated is not None,"request_timestamp":request_timestamp,"response_timestamp":response_timestamp,"model_id":getattr(response,"model",MODEL_ID),"usage":usage.model_dump() if usage is not None else None})
    package={"record_type":"TI001-V011-E2R-SCIENTIFIC-EXECUTION","executor_version":EXECUTOR_VERSION,"fixture_id":fixture["fixture_id"],"fixture_sha256":FIXTURE_SHA256,"interface_git_blob_sha":INTERFACE_SHA,"generator_git_blob_sha":GENERATOR_SHA,"schema_git_blob_sha":SCHEMA_SHA,"model_id":MODEL_ID,"api_surface":"Responses API","generation_configuration":{"top_p":TOP_P,"max_output_tokens":MAX_OUTPUT_TOKENS,"tools":TOOLS,"tool_choice":TOOL_CHOICE,"background":BACKGROUND,"store":STORE,"reasoning":REASONING},"runtime":{"python":platform.python_version(),"platform":platform.platform(),"openai_sdk":importlib.metadata.version("openai")},"decision_count":len(records),"records":records,"scientific_execution":"PERFORMED"}
    Path(args.output).write_text(json.dumps(package,indent=2,sort_keys=True,ensure_ascii=False)+"\n",encoding="utf-8")
    print(json.dumps({"status":"SCIENTIFIC_EXECUTION_WRITTEN","output":args.output,"decision_count":len(records),"valid_count":sum(r["valid"] for r in records),"fixture_sha256":FIXTURE_SHA256,"reasoning":REASONING},indent=2,sort_keys=True)); return 0

if __name__=="__main__": raise SystemExit(main(sys.argv))
