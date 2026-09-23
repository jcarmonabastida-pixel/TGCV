#!/usr/bin/env python3
"""TI-001 deterministic preflight fixture generator. No scientific execution."""
import json, hashlib
SEED=582031
N=32
BASE_ACTIONS=["a","b","c"]
INSTANCES=[]
for i in range(N):
    iid=f"TI001-{i+1:03d}"
    # Same current state/action space in both conditions.
    current={"state":"S0","t_acc":["a","b","c"]}
    # Future-space consequences differ by selected action.
    succ={
      "a":{"state":"SA","t_acc":["x","y"]},
      "b":{"state":"SB","t_acc":["x","z"]},
      "c":{"state":"SC","t_acc":["y","z"]},
    }
    # Treatment signal is a permutation-invariant structural descriptor,
    # not an action label or outcome/reward.
    treatment_info={
      "future_reconfiguration":"two_of_three_identity_pattern",
      "candidate_count":3,
      "descriptor":"successor_space_identity_turnover"
    }
    control_info={"task":"select_one_current_transformation","candidate_count":3}
    INSTANCES.append({
      "instance_id":iid,"seed":SEED+i,"S_t":current["state"],
      "T_acc_t":current["t_acc"],"available_transformations":BASE_ACTIONS,
      "control":{"information_control":control_info,"information_treatment":None},
      "treatment":{"information_control":control_info,"information_treatment":treatment_info},
      "successors":succ,"future_alternatives":[{"choice":"a","successor":"SA","T_acc_t1":["x","y"]},{"choice":"b","successor":"SB","T_acc_t1":["x","z"]}],"temporal_order":["information_available","transformation_choice","successor_state","successor_accessibility"],"primary_estimand":{"name":"matched_condition_difference_in_transformation_handling","type":"difference_in_subsequent_transformation_handling","forbidden":["TI_score","value","reward","utility","performance"]},
      "null":{"information":{"task":"select_one_current_transformation","candidate_count":3,
                             "format":"structured","future_space_signal":False,
                             "recommendation":False,"outcome_signal":False}}
    })
out={"schema":"TI001_PREFLIGHT_FIXTURE_v001","seed":SEED,"instances":INSTANCES}
raw=json.dumps(out,sort_keys=True,separators=(",",":")).encode()
out["fixture_sha256"]=hashlib.sha256(raw).hexdigest()
print(json.dumps(out,indent=2,sort_keys=True))

