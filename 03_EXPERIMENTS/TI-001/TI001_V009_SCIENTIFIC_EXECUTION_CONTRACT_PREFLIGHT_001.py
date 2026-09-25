#!/usr/bin/env python3
import argparse, hashlib, json, pathlib

BASE = pathlib.Path(__file__).resolve().parent
ROOT = BASE.parents[2]

CONTRACT_PATH = BASE / "TI001_V009_SCIENTIFIC_EXECUTION_CONTRACT_001.json"
RUNTIME_SPEC_PATH = BASE / "TI001_V009_SCIENTIFIC_RUNTIME_SPECIFICATION_001.md"
DIAG_RESULT_PATH = BASE / "TI001_V009_RUNTIME_DIAGNOSTIC_002_RESULT_001.json"
DIAG_PREFLIGHT_PATH = BASE / "TI001_V009_RUNTIME_DIAGNOSTIC_002_PREFLIGHT_RESULT_001.json"
FIXTURE_PATH = BASE / "generated" / "V008" / "TI001_V008_FIXTURE_001.json"

EXPECTED_FIXTURE_SHA256 = "dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"

def sha256(path):
    h=hashlib.sha256()
    with open(path,"rb") as f:
        for chunk in iter(lambda:f.read(1024*1024),b""):
            h.update(chunk)
    return h.hexdigest()

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output", required=True)
    a=p.parse_args()

    contract=json.load(open(CONTRACT_PATH,encoding="utf-8"))
    diag=json.load(open(DIAG_RESULT_PATH,encoding="utf-8"))
    dp=json.load(open(DIAG_PREFLIGHT_PATH,encoding="utf-8"))

    checks={
      "contract_exists": CONTRACT_PATH.is_file(),
      "runtime_spec_exists": RUNTIME_SPEC_PATH.is_file(),
      "diagnostic_result_exists": DIAG_RESULT_PATH.is_file(),
      "diagnostic_preflight_exists": DIAG_PREFLIGHT_PATH.is_file(),
      "fixture_exists": FIXTURE_PATH.is_file(),
      "contract_status_not_authorized": contract.get("status")=="CONTRACT — SCIENTIFIC EXECUTION NOT AUTHORIZED",
      "runtime_spec_commit_bound": contract["runtime_specification"]["commit"]=="0a77b62f45a64bae192162f430081cb029df2d34",
      "model_identity": contract["runtime_specification"]["model"]=="gpt-5.6-luna",
      "top_p": contract["runtime_specification"]["top_p"]==0.98,
      "max_output_tokens": contract["runtime_specification"]["max_output_tokens"]==64,
      "reasoning_effort_none": contract["runtime_specification"]["reasoning"]=={"effort":"none"},
      "temperature_omitted": contract["runtime_specification"]["temperature"] is None,
      "tools_empty": contract["runtime_specification"]["tools"]==[],
      "fixture_identity": contract["scientific_fixture"]["sha256"]==EXPECTED_FIXTURE_SHA256 and contract["scientific_fixture"]["git_blob"]=="3ff971544f98c8d810173493cd49d54c46070952",
      "fixture_sha256_matches_local": sha256(FIXTURE_PATH)==EXPECTED_FIXTURE_SHA256 if FIXTURE_PATH.is_file() else False,
      "decision_domain_AB": contract["decision_schema"]["allowed_decisions"]==["A","B"],
      "diagnostic_pass": dp.get("status")=="PASS",
      "diagnostic_scientific_not_performed": diag.get("scientific_execution")=="NOT_PERFORMED",
      "diagnostic_reasoning_none": (diag.get("generation_configuration",{}).get("reasoning") or {}).get("effort")=="none",
      "diagnostic_reasoning_tokens_zero": ((diag.get("usage") or {}).get("output_tokens_details") or {}).get("reasoning_tokens")==0,
      "no_retry_recode": contract["execution_controls"]["retry"] is False and contract["execution_controls"]["recode"] is False,
      "separate_authorization_required": contract["authorization"]["separate_explicit_user_authorization_required"] is True
    }
    out={"preflight_id":"TI001-V009-SCIENTIFIC-EXECUTION-CONTRACT-PREFLIGHT-001","checks":checks,"status":"PASS" if all(checks.values()) else "FAIL","scientific_execution":"NOT_PERFORMED"}
    open(a.output,"w",encoding="utf-8").write(json.dumps(out,indent=2)+ "\n")
    print(json.dumps(out,indent=2))
    return 0 if out["status"]=="PASS" else 1

if __name__=="__main__":
    raise SystemExit(main())
