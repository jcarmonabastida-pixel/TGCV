#!/usr/bin/env python3
"""TI-001 P1-P10 structural preflight checker. No treatment/control experiment."""
import json,sys
d=json.load(open(sys.argv[1],encoding="utf-8"))
results={}
def ok(k,v): results[k]=bool(v)
ok("P1_CURRENT_SPACE_EQUALITY",all(x["control"]["information_control"]["candidate_count"]==x["treatment"]["information_control"]["candidate_count"] and x["T_acc_t"]==["a","b","c"] for x in d["instances"]))
ok("P2_CANDIDATE_MULTIPLICITY",all(len(x["available_transformations"])>=2 for x in d["instances"]))
ok("P3_TREATMENT_SPECIFICITY",all(x["treatment"]["information_control"]==x["control"]["information_control"] and x["treatment"]["information_treatment"] is not None for x in d["instances"]))
ok("P4_NO_DIRECT_RECOMMENDATION",all(not any(k in x["treatment"]["information_treatment"] for k in ["recommended_action","preferred_action","selected_action","action_recommendation","recommended_transformation","preferred_transformation"]) for x in d["instances"]))
ok("P5_NO_OUTCOME_LEAKAGE",all(not any(k in json.dumps(x["treatment"]["information_treatment"]).lower() for k in ["reward","utility","payoff","outcome","preferred"]) for x in d["instances"]))
present=[json.dumps({"S_t":x["S_t"],"T_acc_t":x["T_acc_t"],"control":x["control"]["information_control"]},sort_keys=True,separators=(",",":")) for x in d["instances"]]; futures=[(tuple(x["future_alternatives"][0]["T_acc_t1"]),tuple(x["future_alternatives"][1]["T_acc_t1"])) for x in d["instances"]]; ok("P6_FUTURE_NON_DERIVABILITY",all(len(set(f))>=2 for f in futures) and len(set(present))==1)
ok("P7_TEMPORAL_ORDER",all(x["temporal_order"]==["information_available","transformation_choice","successor_state","successor_accessibility"] for x in d["instances"]))
ok("P8_NULL_VALIDITY",all(not x["null"]["information"]["future_space_signal"] and not x["null"]["information"]["recommendation"] and not x["null"]["information"]["outcome_signal"] for x in d["instances"]))
ok("P9_DETERMINISTIC_RECONSTRUCTION",all(set(x["successors"])=={"a","b","c"} and all(len(x["successors"][a]["t_acc"])==2 for a in x["successors"]) for x in d["instances"]))
ok("P10_PRIMARY_METRIC_FREEZE",len({x["primary_estimand"]["name"] for x in d["instances"]})==1 and all(x["primary_estimand"]["type"]=="difference_in_subsequent_transformation_handling" and all(k in x["primary_estimand"]["forbidden"] for k in ["TI_score","value","reward","utility","performance"]) for x in d["instances"]))
print(json.dumps({"status":"PREFLIGHT_PASS","checks":results,"passed":sum(results.values()),"total":len(results)},indent=2,sort_keys=True))
raise SystemExit(0 if all(results.values()) else 1)




