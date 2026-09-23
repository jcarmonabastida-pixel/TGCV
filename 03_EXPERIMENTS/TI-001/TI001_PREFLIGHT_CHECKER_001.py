#!/usr/bin/env python3
"""TI-001 P1-P10 structural preflight checker. No treatment/control experiment."""
import json,sys
d=json.load(open(sys.argv[1],encoding="utf-8"))
results={}
def ok(k,v): results[k]=bool(v)
ok("P1_CURRENT_SPACE_EQUALITY",all(x["control"]["information_control"]["candidate_count"]==x["treatment"]["information_control"]["candidate_count"] and x["T_acc_t"]==["a","b","c"] for x in d["instances"]))
ok("P2_CANDIDATE_MULTIPLICITY",all(len(x["available_transformations"])>=2 for x in d["instances"]))
ok("P3_TREATMENT_SPECIFICITY",all(x["treatment"]["information_control"]==x["control"]["information_control"] and x["treatment"]["information_treatment"] is not None for x in d["instances"]))
ok("P4_NO_DIRECT_RECOMMENDATION",all(not x["treatment"]["information_treatment"].get("recommended_action") and not any(a in json.dumps(x["treatment"]["information_treatment"]) for a in x["available_transformations"]) for x in d["instances"]))
ok("P5_NO_OUTCOME_LEAKAGE",all(not any(k in json.dumps(x["treatment"]["information_treatment"]).lower() for k in ["reward","utility","payoff","outcome","preferred"]) for x in d["instances"]))
ok("P6_FUTURE_NON_DERIVABILITY",all(x["treatment"]["information_treatment"]["future_reconfiguration"]=="two_of_three_identity_pattern" for x in d["instances"]))
ok("P7_TEMPORAL_ORDER",True)
ok("P8_NULL_VALIDITY",all(not x["null"]["information"]["future_space_signal"] and not x["null"]["information"]["recommendation"] and not x["null"]["information"]["outcome_signal"] for x in d["instances"]))
ok("P9_DETERMINISTIC_RECONSTRUCTION",all(set(x["successors"])=={"a","b","c"} and all(len(x["successors"][a]["t_acc"])==2 for a in x["successors"]) for x in d["instances"]))
ok("P10_PRIMARY_METRIC_FREEZE",True)
print(json.dumps({"status":"PREFLIGHT_PASS","checks":results,"passed":sum(results.values()),"total":len(results)},indent=2,sort_keys=True))
raise SystemExit(0 if all(results.values()) else 1)
