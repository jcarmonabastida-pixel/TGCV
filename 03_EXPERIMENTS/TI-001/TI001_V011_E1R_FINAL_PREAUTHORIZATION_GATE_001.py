#!/usr/bin/env python3
"""TI-001 V011 E1-R final preauthorization gate."""
import hashlib
import json
import subprocess
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
BASE=ROOT/"03_EXPERIMENTS"/"TI-001"
FIXTURE=BASE/"TI001_V011_FIXTURE_001.json"
GENERATOR=BASE/"TI001_V011_FIXTURE_GENERATOR_001.py"
SCHEMA=BASE/"TI001_V011_DECISION_UNIT_SCHEMA_SPECIFICATION_001.md"
INTERFACE=BASE/"TI001_V011_DECISION_INTERFACE_001.py"
EXECUTOR=BASE/"TI001_V011_E1R_SCIENTIFIC_EXECUTOR_001.py"
DESIGN=BASE/"TI001_V011_E1R_REPLACEMENT_EXECUTION_DESIGN_SPECIFICATION_001.md"
PREFLIGHT=BASE/"TI001_V011_E1R_EXECUTOR_IDENTITY_COMPATIBILITY_PREFLIGHT_RESULT_001.json"
E1_RESULT=BASE/"TI001_V011_SCIENTIFIC_EXECUTION_E1_RESULT_001.json"
AUTHORIZATION=BASE/"TI001_V011_E1R_SCIENTIFIC_EXECUTION_AUTHORIZATION_001.json"
E1R_RESULT=BASE/"TI001_V011_E1R_SCIENTIFIC_EXECUTION_RESULT_001.json"

EXPECTED_FIXTURE_SHA="30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1"
EXPECTED_GENERATOR_SHA="9170f767cac3fceccaba248747c6524c5f150e11"
EXPECTED_SCHEMA_SHA="b2fef667f6eb33689ece5481957d3917a860dd3e"
EXPECTED_INTERFACE_SHA="8667b0ff70f58283c688f24c76f10db142655d14"
EXPECTED_EXECUTOR_SHA="f51e62cce134303df4a5fede92bb7b33ff38f5c0"

def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def blob(p): return subprocess.check_output(["git","hash-object",str(p)],text=True).strip()
def exists(p): return p.is_file()

def main():
    checks={}
    checks["A1_FIXTURE_SHA_EXACT"]=exists(FIXTURE) and sha(FIXTURE)==EXPECTED_FIXTURE_SHA
    checks["A2_GENERATOR_BLOB_EXACT"]=exists(GENERATOR) and blob(GENERATOR)==EXPECTED_GENERATOR_SHA
    checks["A3_SCHEMA_BLOB_EXACT"]=exists(SCHEMA) and blob(SCHEMA)==EXPECTED_SCHEMA_SHA
    checks["A4_INTERFACE_BLOB_EXACT"]=exists(INTERFACE) and blob(INTERFACE)==EXPECTED_INTERFACE_SHA
    checks["A5_E1R_EXECUTOR_BLOB_EXACT"]=exists(EXECUTOR) and blob(EXECUTOR)==EXPECTED_EXECUTOR_SHA
    checks["A6_PREFLIGHT_EXISTS_PASS"]=exists(PREFLIGHT)
    preflight=json.loads(PREFLIGHT.read_text(encoding="utf-8")) if checks["A6_PREFLIGHT_EXISTS_PASS"] else {}
    checks["A7_PREFLIGHT_STATUS_PASS"]=preflight.get("status")=="PASS"
    checks["A8_PREFLIGHT_BINDINGS_EXACT"]=(
        preflight.get("fixture_sha256")==EXPECTED_FIXTURE_SHA and
        preflight.get("executor_blob_sha")==EXPECTED_EXECUTOR_SHA and
        preflight.get("reasoning")=={"effort":"none"}
    )
    checks["A9_DESIGN_EXISTS"]=exists(DESIGN)
    design=DESIGN.read_text(encoding="utf-8") if checks["A9_DESIGN_EXISTS"] else ""
    checks["A10_DESIGN_BINDS_REASONING_NONE"]='reasoning={"effort":"none"}' in design and '"none"' in design
    checks["A11_E1_PRESERVED"]=exists(E1_RESULT)
    checks["A12_NO_E1R_AUTHORIZATION_EXISTS"]=not exists(AUTHORIZATION)
    checks["A13_NO_E1R_RESULT_EXISTS"]=not exists(E1R_RESULT)
    checks["A14_GATE_ITSELF_NO_PROVIDER_CALL"]=True
    result={
        "gate_id":"TI001-V011-E1R-FINAL-PREAUTHORIZATION-GATE-001",
        "status":"PASS" if all(checks.values()) else "FAIL",
        "checks":checks,
        "fixture_sha256":sha(FIXTURE) if exists(FIXTURE) else None,
        "executor_blob_sha":blob(EXECUTOR) if exists(EXECUTOR) else None,
        "scientific_execution":"NOT_PERFORMED",
        "authorization":"READY_FOR_EXPLICIT_AUTHORIZATION" if all(checks.values()) else "NOT_AUTHORIZED"
    }
    print(json.dumps(result,indent=2,sort_keys=True))
    return 0 if result["status"]=="PASS" else 1

if __name__=="__main__":
    raise SystemExit(main())
