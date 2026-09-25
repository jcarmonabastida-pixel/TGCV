#!/usr/bin/env python3
import argparse,hashlib,json
from pathlib import Path
RUNNER_SHA1="04a1b6cf37197499988579e5636c72a445a03a16"
FIXTURE_SHA256="dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"
PROVIDER_SHA1="c7d066de3481143d878f06bb2c1d791cb7dc54e1"
def blob_sha1(b): return hashlib.sha1(f"blob {len(b)}\0".encode()+b).hexdigest()
def main():
 ap=argparse.ArgumentParser(); ap.add_argument("--runner",required=True); ap.add_argument("--fixture",required=True); ap.add_argument("--provider",required=True); ap.add_argument("--output",required=True); a=ap.parse_args()
 rb=Path(a.runner).read_bytes(); fb=Path(a.fixture).read_bytes(); pb=Path(a.provider).read_bytes()
 runner_sha=blob_sha1(rb); fixture_sha=hashlib.sha256(fb).hexdigest(); provider_sha=blob_sha1(pb); text=rb.decode("utf-8")
 ms=text.index("def model_input"); ae=text.index("def authorization_ok"); model_section=text[ms:ae]
 checks={
 "runner_identity":runner_sha==RUNNER_SHA1,"fixture_identity":fixture_sha==FIXTURE_SHA256,"provider_identity":provider_sha==PROVIDER_SHA1,
 "model_identity":'MODEL_ID = "gpt-5.6-luna"' in text,"api_surface":'API_SURFACE = "Responses API"' in text,
 "runtime_top_p":"TOP_P = 0.98" in text,"runtime_max_output_tokens":"MAX_OUTPUT_TOKENS = 16" in text,
 "temperature_omitted_from_request":'"temperature": None' in text,"tools_empty":'"tools": []' in text,
 "no_conversation":'"conversation": None' in text,"no_previous_response":'"previous_response_id": None' in text,
 "hidden_fields_not_in_model_input":all(x not in model_section for x in ['unit["decision_id"]','unit["pair_id"]','unit["condition"]','unit["presentation"]']),
 "successor_not_realized":'unit["future_structure"]["successor_realized"] is not False' in model_section,
 "ab_only":'VALID_OUTPUTS = {"A", "B"}' in text,
 "no_retry_or_recode_logic":'if selected not in VALID_OUTPUTS' in text and 'raise ValueError("invalid model output")' in text,
 "no_analysis":'"analysis_performed": False' in text,"explicit_authorization":'if not authorization_ok(auth):' in text,
 "scientific_execution_only_after_authorization":'record.get("scientific_execution") == "AUTHORIZED"' in text,
 "preflight_non_scientific":True}
 result={"preflight_id":"TI001-V008-SCIENTIFIC-EXECUTOR-1-IDENTITY-PREFLIGHT-001","checks":checks,"runner_blob_sha1":runner_sha,"provider_blob_sha1":provider_sha,"fixture_sha256":fixture_sha,"scientific_execution":"NOT_PERFORMED","status":"PASS" if all(checks.values()) else "BLOCKED"}
 Path(a.output).write_text(json.dumps(result,indent=2)+"\n",encoding="utf-8")
if __name__=="__main__": main()
