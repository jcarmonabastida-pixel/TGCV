#!/usr/bin/env python3
"""TI-001 P1-P10 structural preflight checker plus Gate A assignment integrity. No scientific execution."""
import json,sys,random
d=json.load(open(sys.argv[1],encoding="utf-8"))
results={}
def ok(k,v): results[k]=bool(v)
instances=d["instances"]
ok("P1_CURRENT_SPACE_EQUALITY",all(x["control"]["information_control"]["candidate_count"]==x["treatment"]["information_control"]["candidate_count"] and x["T_acc_t"]==["a","b","c"] for x in instances))
ok("P2_CANDIDATE_MULTIPLICITY",all(len(x["available_transformations"])>=2 for x in instances))
ok("P3_TREATMENT_SPECIFICITY",all(x["treatment"]["information_control"]==x["control"]["information_control"] and x["treatment"]["information_treatment"] is not None for x in instances))
ok("P4_NO_DIRECT_RECOMMENDATION",all(not any(k in x["treatment"]["information_treatment"] for k in ["recommended_action","preferred_action","selected_action","action_recommendation","recommended_transformation","preferred_transformation"]) for x in instances))
ok("P5_NO_OUTCOME_LEAKAGE",all(not any(k in json.dumps(x["treatment"]["information_treatment"]).lower() for k in ["reward","utility","payoff","outcome","preferred"]) for x in instances))
present=[json.dumps({"S_t":x["S_t"],"T_acc_t":x["T_acc_t"],"control":x["control"]["information_control"]},sort_keys=True,separators=(",",":")) for x in instances]
futures=[(tuple(x["future_alternatives"][0]["T_acc_t1"]),tuple(x["future_alternatives"][1]["T_acc_t1"])) for x in instances]
ok("P6_FUTURE_NON_DERIVABILITY",all(len(set(f))>=2 for f in futures) and len(set(present))==1)
ok("P7_TEMPORAL_ORDER",all(x["temporal_order"]==["information_available","transformation_choice","successor_state","successor_accessibility"] for x in instances))
ok("P8_NULL_VALIDITY",all(not x["null"]["information"]["future_space_signal"] and not x["null"]["information"]["recommendation"] and not x["null"]["information"]["outcome_signal"] for x in instances))
ok("P9_DETERMINISTIC_RECONSTRUCTION",all(set(x["successors"])=={"a","b","c"} and all(len(x["successors"][a]["t_acc"])==2 for a in x["successors"]) for x in instances))
ok("P10_PRIMARY_METRIC_FREEZE",len({x["primary_estimand"]["name"] for x in instances})==1 and all(x["primary_estimand"]["type"]=="difference_in_subsequent_transformation_handling" and all(k in x["primary_estimand"]["forbidden"] for k in ["TI_score","value","reward","utility","performance"]) for x in instances))

# Gate A — Randomisation & Assignment Integrity.
# These checks intentionally fail on the pre-assignment fixture until the generator is updated.
ok("A1_ASSIGNMENT_FIELDS_PRESENT",all(all(k in x for k in ["pair_id","condition","execution_slot","environment_seed","randomisation_seed"]) for x in instances))
pair_ids=[x.get("pair_id") for x in instances]
conditions=[x.get("condition") for x in instances]
slots=[x.get("execution_slot") for x in instances]
ok("A2_PAIR_STRUCTURE",len(instances)==32 and len(set(pair_ids))==32 and all(isinstance(p,str) and p.startswith("TI001-") for p in pair_ids))
ok("A3_CONDITION_BALANCE",conditions.count("control")==16 and conditions.count("treatment")==16)
ok("A4_PAIR_CONDITION_COMPLETENESS",len({(x.get("pair_id"),x.get("condition")) for x in instances})==32)
ok("A5_SLOT_UNIQUENESS",len({(x.get("pair_id"),x.get("execution_slot")) for x in instances})==32)
ok("A6_SEED_SEPARATION",all(x.get("environment_seed") is not None and x.get("randomisation_seed")==582031 for x in instances) and len({x.get("environment_seed") for x in instances})==32)
ok("A7_ASSIGNMENT_REPRODUCIBILITY",False)
ok("A8_ASSIGNMENT_CONTENT_INDEPENDENCE",all("condition" not in x.get("S_t","") and "condition" not in json.dumps(x.get("T_acc_t",[])).lower() for x in instances))
ok("A9_NO_DUPLICATE_INSTANCE",len({x.get("instance_id") for x in instances})==len(instances))

print(json.dumps({"status":"PREFLIGHT_PASS" if all(results.values()) else "PREFLIGHT_FAIL","checks":results,"passed":sum(results.values()),"total":len(results),"scientific_execution":"NOT_AUTHORIZED"},indent=2,sort_keys=True))
raise SystemExit(0 if all(results.values()) else 1)
