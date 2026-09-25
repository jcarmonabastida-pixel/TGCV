#!/usr/bin/env python3
import argparse,hashlib,json
from pathlib import Path

RUNNER_SHA1="REPLACE_AFTER_COMMIT"
FIXTURE_SHA256="dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"
PROVIDER_SHA1="c7d066de3481143d878f06bb2c1d791cb7dc54e1"
MODEL="gpt-5.6-luna"

def blob_sha1(b): return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--runner",required=True)
    ap.add_argument("--fixture",required=True)
    ap.add_argument("--provider",required=True)
    ap.add_argument("--output",required=True)
    a=ap.parse_args()
    rb=Path(a.runner).read_bytes()
    fb=Path(a.fixture).read_bytes()
    pb=Path(a.provider).read_bytes()
    runner_sha=blob_sha1(rb)
    fixture_sha=hashlib.sha256(fb).hexdigest()
    provider_sha=blob_sha1(pb)
    text=rb.decode("utf-8")
    checks={
      "runner_identity": RUNNER_SHA1!="REPLACE_AFTER_COMMIT" and runner_sha==RUNNER_SHA1,
      "fixture_identity": fixture_sha==FIXTURE_SHA256,
      "provider_identity": provider_sha==PROVIDER_SHA1,
      "model_identity": MODEL in text,
      "runtime_top_p": "TOP_P = 0.98" in text,
      "runtime_max_output_tokens": "MAX_OUTPUT_TOKENS = 16" in text,
      "temperature_omitted": "temperature=None" in text,
      "tools_empty": "tools=[]" in text,
      "no_conversation": "conversation": None" in text,
      "no_previous_response": "previous_response_id": None" in text,
      "hidden_fields_not_in_model_input": 'unit["condition"]' not in text[text.find("def model_input"):text.find("def authorization_ok")],
      "no_successor_realization": 'successor_realized"] is not False' in text,
      "ab_only": 'VALID_OUTPUTS = {"A", "B"}' in text,
      "no_retry_or_recode": "retry" not in text.lower() and "recode" not in text.lower(),
      "no_analysis": '"analysis_performed": False' in text,
      "explicit_authorization": "authorization_ok(auth)" in text,
      "scientific_not_performed_in_preflight": True
    }
    result={"preflight_id":"TI001-V008-SCIENTIFIC-EXECUTOR-1-IDENTITY-PREFLIGHT-001","checks":checks,"runner_blob_sha1":runner_sha,"provider_blob_sha1":provider_sha,"fixture_sha256":fixture_sha,"scientific_execution":"NOT_PERFORMED","status":"PASS" if all(checks.values()) else "BLOCKED"}
    Path(a.output).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
if __name__=="__main__": main()
