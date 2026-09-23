#!/usr/bin/env python3
"""TI-001 deterministic preflight fixture generator. No scientific execution."""
import json,hashlib,random

RANDOMISATION_SEED=582031
ENVIRONMENT_SEED_BASE=731407
N=32
BASE_ACTIONS=["a","b","c"]
PAIR_IDS=[f"TI001-{i+1:03d}" for i in range(N)]

# Frozen assignment protocol: shuffle pair IDs, then alternate slot mapping.
rng=random.Random(RANDOMISATION_SEED)
shuffled_pairs=PAIR_IDS[:]
rng.shuffle(shuffled_pairs)
assignment={}
for j,pair_id in enumerate(shuffled_pairs):
    assignment[pair_id]=(
        {"slot_A":"control","slot_B":"treatment"}
        if j % 2 == 0
        else {"slot_A":"treatment","slot_B":"control"}
    )

RECORDS=[]
for i,pair_id in enumerate(PAIR_IDS):
    environment_seed=ENVIRONMENT_SEED_BASE+i

    # Environment seed is persisted as the frozen generation seed.
    # The preflight environment is intentionally structurally identical
    # across matched pairs; no scientific outcome is generated here.
    environment_rng=random.Random(environment_seed)
    _environment_nonce=environment_rng.getrandbits(32)

    current={"state":"S0","t_acc":BASE_ACTIONS}
    successors={
      "a":{"state":"SA","t_acc":["x","y"]},
      "b":{"state":"SB","t_acc":["x","z"]},
      "c":{"state":"SC","t_acc":["y","z"]},
    }
    future_alternatives=[
        {"choice":"a","successor":"SA","T_acc_t1":["x","y"]},
        {"choice":"b","successor":"SB","T_acc_t1":["x","z"]},
    ]

    treatment_info={
      "future_reconfiguration":"two_of_three_identity_pattern",
      "candidate_count":3,
      "descriptor":"successor_space_identity_turnover"
    }
    control_info={
      "task":"select_one_current_transformation",
      "candidate_count":3
    }

    tsda_descriptors={
      "representation":"transition_level_preflight",
      "accessibility_cardinality_t":len(current["t_acc"]),
      "future_alternative_count":len(future_alternatives),
      "future_accessibility_cardinalities":[
          len(x["T_acc_t1"]) for x in future_alternatives
      ],
      "identity_turnover":True,
      "net_accessibility_change_by_alternative":[
          len(x["T_acc_t1"])-len(current["t_acc"])
          for x in future_alternatives
      ]
    }

    common={
      "pair_id":pair_id,
      "S_t":current["state"],
      "T_acc_t":current["t_acc"],
      "available_transformations":BASE_ACTIONS,
      "successors":successors,
      "future_alternatives":future_alternatives,
      "temporal_order":[
          "information_available",
          "transformation_choice",
          "successor_state",
          "successor_accessibility"
      ],
      "primary_estimand":{
        "name":"matched_condition_difference_in_transformation_handling",
        "type":"difference_in_subsequent_transformation_handling",
        "forbidden":["TI_score","value","reward","utility","performance"]
      },
      "null_condition":{
        "information":{
          "task":"select_one_current_transformation",
          "candidate_count":3,
          "format":"structured",
          "future_space_signal":False,
          "recommendation":False,
          "outcome_signal":False
        },
        "scientific_execution":False
      }
    }

    for slot in ["slot_A","slot_B"]:
        condition=assignment[pair_id][slot]
        RECORDS.append({
          **common,
          "instance_id":pair_id,
          "condition":condition,
          "execution_slot":slot,
          "seed":environment_seed,
          "environment_seed":environment_seed,
          "randomisation_seed":RANDOMISATION_SEED,
          "information_control":control_info,
          "information_treatment":treatment_info if condition=="treatment" else None,

          # Execution-only observations remain explicitly null in preflight.
          "selected_transformation":None,
          "S_t1":None,
          "T_acc_t1":None,
          "Delta_T_acc_t":None,

          "TSDA_descriptors":tsda_descriptors,
          "decision_before_future_reveal":True,
          "leakage_checks":{
            "condition_in_state":False,
            "condition_in_current_accessibility":False,
            "preferred_action_revealed":False,
            "outcome_revealed":False,
            "future_space_signal_in_control":False,
            "future_space_signal_in_treatment_is_structured":True
          }
        })

out={
  "schema":"TI001_PREFLIGHT_FIXTURE_v004",
  "randomisation_seed":RANDOMISATION_SEED,
  "environment_seed_base":ENVIRONMENT_SEED_BASE,
  "pair_count":N,
  "record_count":len(RECORDS),
  "instances":RECORDS
}
raw=json.dumps(out,sort_keys=True,separators=(",",":")).encode()
out["fixture_sha256"]=hashlib.sha256(raw).hexdigest()
print(json.dumps(out,indent=2,sort_keys=True))
