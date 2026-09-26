#!/usr/bin/env python3
import json
from collections import Counter
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]; B=ROOT/"03_EXPERIMENTS"/"TI-001"
E1=B/"TI001_V011_E1R_SCIENTIFIC_EXECUTION_RESULT_001.json"; E2=B/"TI001_V011_E2R_SCIENTIFIC_EXECUTION_RESULT_001.json"
AUTH=B/"TI001_V011_SCIENTIFIC_ANALYSIS_AUTHORIZATION_001.json"; OUT=B/"TI001_V011_SCIENTIFIC_ANALYSIS_RESULT_001.json"
def load(p):
 raw=p.read_text(encoding="utf-8")
 if raw.endswith("\\n"): raw=raw[:-2]
 return json.loads(raw)
def analyze(data):
 r=data["records"]; out={}
 for cond in ("control","treatment","null"):
  rr=[x for x in r if x["condition"]==cond]; a=sum(x["validated_decision"]=="A" for x in rr)
  out[cond]={"n":len(rr),"A":a,"B":len(rr)-a,"q_A":a/len(rr)}
 for p in ("I1_FIRST","I2_FIRST"):
  for cond in ("control","treatment","null"):
   rr=[x for x in r if x["condition"]==cond and x["presentation"]==p]; a=sum(x["validated_decision"]=="A" for x in rr)
   out[f"{cond}|{p}"]={"n":len(rr),"A":a,"B":len(rr)-a,"q_A":a/len(rr)}
 return out
def main():
 auth=load(AUTH)
 if auth.get("authorization_status")!="AUTHORIZED": raise SystemExit("ANALYSIS_NOT_AUTHORIZED")
 e1,e2=load(E1),load(E2); a1,a2=analyze(e1),analyze(e2)
 def contrasts(a):
  return {
   "TI_DC":a["treatment"]["q_A"]-a["control"]["q_A"],
   "TI_NULL":a["null"]["q_A"]-a["control"]["q_A"],
   "TI_DC_I1_FIRST":a["treatment|I1_FIRST"]["q_A"]-a["control|I1_FIRST"]["q_A"],
   "TI_DC_I2_FIRST":a["treatment|I2_FIRST"]["q_A"]-a["control|I2_FIRST"]["q_A"],
   "TI_NULL_I1_FIRST":a["null|I1_FIRST"]["q_A"]-a["control|I1_FIRST"]["q_A"],
   "TI_NULL_I2_FIRST":a["null|I2_FIRST"]["q_A"]-a["control|I2_FIRST"]["q_A"],
   "P_D_CONTROL":a["control|I1_FIRST"]["q_A"]-a["control|I2_FIRST"]["q_A"],
   "P_D_TREATMENT":a["treatment|I1_FIRST"]["q_A"]-a["treatment|I2_FIRST"]["q_A"],
   "P_D_NULL":a["null|I1_FIRST"]["q_A"]-a["null|I2_FIRST"]["q_A"]}
 c1,c2=contrasts(a1),contrasts(a2)
 r1,r2=e1["records"],e2["records"]; agree=sum(x["validated_decision"]==y["validated_decision"] for x,y in zip(r1,r2))
 pair_agreement={}
 for pair in sorted({x["pair_id"] for x in r1}):
  x=[z["validated_decision"] for z in r1 if z["pair_id"]==pair]; y=[z["validated_decision"] for z in r2 if z["pair_id"]==pair]
  pair_agreement[pair]=x==y
 out={"analysis_id":"TI001-V011-SCIENTIFIC-ANALYSIS-001","status":"PERFORMED","analysis_boundary":{"pooling":False,"e1r_e2r_separate":True},"E1R":{"counts":a1,"contrasts":c1},"E2R":{"counts":a2,"contrasts":c2},"cross_execution":{"response_level_agreement_count":agree,"response_level_disagreement_count":420-agree,"response_level_agreement_rate":agree/420,"pair_level_exact_agreement_count":sum(pair_agreement.values()),"pair_level_exact_disagreement_count":len(pair_agreement)-sum(pair_agreement.values())}}
 OUT.write_text(json.dumps(out,indent=2,sort_keys=True,ensure_ascii=False)+"\\n",encoding="utf-8")
 print(json.dumps(out,indent=2,sort_keys=True))
if __name__=="__main__": main()
