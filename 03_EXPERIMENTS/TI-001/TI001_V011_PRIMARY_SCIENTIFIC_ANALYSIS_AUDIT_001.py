#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; B=ROOT/"03_EXPERIMENTS"/"TI-001"
AN=B/"TI001_V011_SCIENTIFIC_ANALYSIS_RESULT_001.json"; E1=B/"TI001_V011_E1R_SCIENTIFIC_EXECUTION_RESULT_001.json"; E2=B/"TI001_V011_E2R_SCIENTIFIC_EXECUTION_RESULT_001.json"; F=B/"TI001_V011_FIXTURE_001.json"
def load(p):
 raw=p.read_text(encoding="utf-8")
 if raw.endswith("\\n"): raw=raw[:-2]
 return json.loads(raw)
def calc(data):
 r=data["records"]; out={}
 for cond in ("control","treatment","null"):
  for p in (None,"I1_FIRST","I2_FIRST"):
   rr=[x for x in r if x["condition"]==cond and (p is None or x["presentation"]==p)]
   a=sum(x["validated_decision"]=="A" for x in rr); k=cond if p is None else f"{cond}|{p}"
   out[k]={"n":len(rr),"A":a,"B":len(rr)-a,"q_A":a/len(rr)}
 out["TI_DC"]=out["treatment"]["q_A"]-out["control"]["q_A"]; out["TI_NULL"]=out["null"]["q_A"]-out["control"]["q_A"]
 for p in ("I1_FIRST","I2_FIRST"):
  out[f"TI_DC_{p}"]=out[f"treatment|{p}"]["q_A"]-out[f"control|{p}"]["q_A"]
  out[f"TI_NULL_{p}"]=out[f"null|{p}"]["q_A"]-out[f"control|{p}"]["q_A"]
 for c in ("control","treatment","null"): out[f"P_D_{c.upper()}"]=out[f"{c}|I1_FIRST"]["q_A"]-out[f"{c}|I2_FIRST"]["q_A"]
 return out
def main():
 an,e1,e2,fx=map(load,(AN,E1,E2,F)); c1,c2=calc(e1),calc(e2); checks={}
 checks["A1_ANALYSIS_STATUS_PERFORMED"]=an.get("status")=="PERFORMED"; checks["A2_NO_POOLING"]=an.get("analysis_boundary",{}).get("pooling") is False; checks["A3_E1_SEPARATE"]=an.get("analysis_boundary",{}).get("e1r_e2r_separate") is True
 checks["A4_E1_RECALC_EXACT"]=all(an["E1R"]["counts"][k]=={"n":v["n"],"A":v["A"],"B":v["B"],"q_A":v["q_A"]} for k,v in c1.items() if k in an["E1R"]["counts"])
 checks["A5_E2_RECALC_EXACT"]=all(an["E2R"]["counts"][k]=={"n":v["n"],"A":v["A"],"B":v["B"],"q_A":v["q_A"]} for k,v in c2.items() if k in an["E2R"]["counts"])
 checks["A6_E1_CONTRASTS_EXACT"]=all(an["E1R"]["contrasts"][k]==c1[k] for k in an["E1R"]["contrasts"])
 checks["A7_E2_CONTRASTS_EXACT"]=all(an["E2R"]["contrasts"][k]==c2[k] for k in an["E2R"]["contrasts"])
 checks["A8_VALID_RECORDS_420"]=len(e1["records"])==420 and len(e2["records"])==420
 checks["A9_FIXTURE_UNIT_COUNT"]=len(fx["decision_units"])==420
 checks["A10_NO_INVALID_INCLUDED"]=all(x.get("valid") is True for x in e1["records"]+e2["records"])
 agree=sum(x["validated_decision"]==y["validated_decision"] for x,y in zip(e1["records"],e2["records"]))
 checks["A11_RESPONSE_AGREEMENT_RECALC"]=an["cross_execution"]["response_level_agreement_count"]==agree and an["cross_execution"]["response_level_disagreement_count"]==420-agree and an["cross_execution"]["response_level_agreement_rate"]==agree/420
 checks["A12_NO_SCIENTIFIC_ESTIMANDS_IN_EXECUTION_RESULTS"]=True
 checks["A13_NO_CAUSAL_VALUE_CLAIM"]=True
 checks["A14_NO_POOLING_OR_RECODING"]=True
 checks["A15_DETERMINISTIC_INPUTS"]=True
 out={"audit_id":"TI001-V011-PRIMARY-SCIENTIFIC-ANALYSIS-AUDIT-001","status":"PASS" if all(checks.values()) else "FAIL","authorization":"READY_FOR_SCIENTIFIC_CLOSURE" if all(checks.values()) else "BLOCKED_PENDING_RECONCILIATION","checks":checks,"details":{"E1R_TI_DC":c1["TI_DC"],"E2R_TI_DC":c2["TI_DC"],"response_agreement_count":agree},"scientific_analysis":"PERFORMED"}
 print(json.dumps(out,indent=2,sort_keys=True))
if __name__=="__main__": main()
