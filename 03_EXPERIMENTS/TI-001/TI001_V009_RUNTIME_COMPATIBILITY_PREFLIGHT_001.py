import json

EXPECTED_MODEL="gpt-5.6-luna"
EXPECTED_TOP_P=0.98
EXPECTED_MAX_OUTPUT_TOKENS=64

def main():
    diagnostic=json.load(open("03_EXPERIMENTS/TI-001/TI001_V009_RUNTIME_DIAGNOSTIC_RESULT_001.json",encoding="utf-8"))
    checks={
      "diagnostic_only": diagnostic.get("diagnostic_only") is True,
      "scientific_execution_not_performed": diagnostic.get("scientific_execution")=="NOT_PERFORMED",
      "status_completed": diagnostic.get("status")=="completed",
      "incomplete_details_absent": diagnostic.get("incomplete_details") is None,
      "output_present": diagnostic.get("output_text")=="A",
      "model_identity": diagnostic.get("model")==EXPECTED_MODEL,
      "top_p": diagnostic.get("runtime",{}).get("top_p")==EXPECTED_TOP_P,
      "max_output_tokens": diagnostic.get("runtime",{}).get("max_output_tokens")==EXPECTED_MAX_OUTPUT_TOKENS,
      "temperature_omitted": diagnostic.get("runtime",{}).get("temperature") is None,
      "tools_empty": diagnostic.get("runtime",{}).get("tools")==[],
      "conversation_absent": diagnostic.get("runtime",{}).get("conversation") is None,
      "previous_response_absent": diagnostic.get("runtime",{}).get("previous_response_id") is None,
      "store_false": diagnostic.get("runtime",{}).get("store") is False
    }
    result={"preflight_id":"TI001-V009-RUNTIME-COMPATIBILITY-PREFLIGHT-001","checks":checks,"status":"PASS" if all(checks.values()) else "FAIL","scientific_execution":"NOT_PERFORMED"}
    print(json.dumps(result,indent=2))
if __name__=="__main__": main()
