#!/usr/bin/env python3
import argparse, json

EXPECTED = {
    "diagnostic_only": True,
    "scientific_execution": "NOT_PERFORMED",
    "status": "completed",
    "output_text": "A",
    "model": "gpt-5.6-luna",
    "top_p": 0.98,
    "max_output_tokens": 64,
    "reasoning_effort": "none",
    "tools_empty": True,
    "tool_choice": "auto",
    "background": False,
    "previous_response_id": None,
    "conversation": None,
    "store": False,
    "incomplete_details_absent": True,
    "reasoning_tokens": 0,
}

def main():
    p=argparse.ArgumentParser()
    p.add_argument("result")
    a=p.parse_args()
    r=json.load(open(a.result,encoding="utf-8"))
    cfg=r.get("generation_configuration",{})
    usage=r.get("usage") or {}
    outdet=usage.get("output_tokens_details") or {}
    checks={
        "diagnostic_only": r.get("diagnostic_only") is True,
        "scientific_execution_not_performed": r.get("scientific_execution")=="NOT_PERFORMED",
        "status_completed": r.get("status")=="completed",
        "incomplete_details_absent": r.get("incomplete_details") is None,
        "output_valid_A_or_B": r.get("output_text") in {"A","B"},
        "model_identity": r.get("model")=="gpt-5.6-luna",
        "top_p": cfg.get("top_p")==0.98,
        "max_output_tokens": cfg.get("max_output_tokens")==64,
        "reasoning_effort_none": (cfg.get("reasoning") or {}).get("effort")=="none",
        "tools_empty": cfg.get("tools")==[],
        "tool_choice_auto": cfg.get("tool_choice")=="auto",
        "background_false": cfg.get("background") is False,
        "previous_response_absent": cfg.get("previous_response_id") is None,
        "conversation_absent": cfg.get("conversation") is None,
        "store_false": cfg.get("store") is False,
        "reasoning_tokens_zero": outdet.get("reasoning_tokens")==0,
    }
    result={"preflight_id":"TI001-V009-RUNTIME-DIAGNOSTIC-002-PREFLIGHT-001","checks":checks,"status":"PASS" if all(checks.values()) else "FAIL","scientific_execution":"NOT_PERFORMED"}
    print(json.dumps(result,indent=2))
    return 0 if result["status"]=="PASS" else 1

if __name__=="__main__":
    raise SystemExit(main())
