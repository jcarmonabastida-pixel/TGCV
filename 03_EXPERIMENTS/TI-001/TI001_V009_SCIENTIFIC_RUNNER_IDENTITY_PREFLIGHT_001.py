#!/usr/bin/env python3
import argparse, hashlib, json
from pathlib import Path

EXPECTED_BLOB = "2618c1ca6191bb616c9c3b064234b062b98ae68b"
EXPECTED_FIXTURE = "dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"
EXPECTED_PROVIDER = "c7d066de3481143d878f06bb2c1d791cb7dc54e1"
EXPECTED_EXECUTOR = "TI001-V009-SCIENTIFIC-EXECUTOR-1-001"
EXPECTED_REASONING = {"effort":"none"}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--runner",required=True)
    p.add_argument("--contract",required=True)
    p.add_argument("--output",required=True)
    a=p.parse_args()
    src=Path(a.runner).read_bytes()
    text=src.decode("utf-8")
    contract=json.load(open(a.contract,encoding="utf-8"))
    checks={
      "runner_exists": Path(a.runner).is_file(),
      "runner_blob_binding_declared": "REASONING" in text and "MAX_OUTPUT_TOKENS=64" in text,
      "runner_executor_id": EXPECTED_EXECUTOR in text,
      "runner_reasoning_explicit": 'REASONING={"effort":"none"}' in text and "reasoning=REASONING" in text,
      "runner_max_output_tokens_64": "max_output_tokens=MAX_OUTPUT_TOKENS" in text,
      "runner_fixture_sha": EXPECTED_FIXTURE in text,
      "runner_provider_blob": EXPECTED_PROVIDER in text,
      "runner_domain_AB": 'VALID_OUTPUTS={"A","B"}' in text,
      "runner_no_retry_recode": "retry" not in text.lower() and "recode" not in text.lower(),
      "runner_no_analysis": '"analysis_performed":False' in text,
      "contract_runner_identity": contract["required_preconditions"][-1]=="explicit user authorization",
      "contract_runtime_reasoning": contract["runtime_specification"]["reasoning"]==EXPECTED_REASONING,
      "contract_runtime_max_tokens": contract["runtime_specification"]["max_output_tokens"]==64,
      "contract_still_not_authorized": contract["status"]=="CONTRACT — SCIENTIFIC EXECUTION NOT AUTHORIZED"
    }
    out={"preflight_id":"TI001-V009-SCIENTIFIC-RUNNER-IDENTITY-PREFLIGHT-001","runner_source_sha256":hashlib.sha256(src).hexdigest(),"checks":checks,"status":"PASS" if all(checks.values()) else "FAIL","scientific_execution":"NOT_PERFORMED"}
    Path(a.output).write_text(json.dumps(out,indent=2)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2))
    return 0 if out["status"]=="PASS" else 1
if __name__=="__main__": raise SystemExit(main())
