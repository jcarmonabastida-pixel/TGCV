#!/usr/bin/env python3
"""Deterministic TI-001 V012 candidate fixture generator. No scientific execution."""
import hashlib, json, random

VERSION="TI001_V012_FIXTURE_v001"
SEED=582031
ACTIONS=["a","b","c"]
OPS={
 "O1":{"a":["x","y"],"b":["x","z"],"c":["y","z"]},
 "O2":{"a":["p","q"],"b":["p","r"],"c":["q","s"]},
 "O3":{"a":["m","n"],"b":["n","o"],"c":["m","o"]},
}
DESCRIPTORS={
 "O1":{"a":{"future_accessibility_class":"pair_xy","identity_turnover_class":"turnover_2","persistence_class":"none","reconfiguration_class":"pair_xy"},
        "b":{"future_accessibility_class":"pair_xz","identity_turnover_class":"turnover_2","persistence_class":"none","reconfiguration_class":"pair_xz"},
        "c":{"future_accessibility_class":"pair_yz","identity_turnover_class":"turnover_2","persistence_class":"none","reconfiguration_class":"pair_yz"}},
 "O2":{"a":{"future_accessibility_class":"pair_pq","identity_turnover_class":"turnover_2","persistence_class":"none","reconfiguration_class":"pair_pq"},
        "b":{"future_accessibility_class":"pair_pr","identity_turnover_class":"turnover_2","persistence_class":"none","reconfiguration_class":"pair_pr"},
        "c":{"future_accessibility_class":"pair_qs","identity_turnover_class":"turnover_2","persistence_class":"none","reconfiguration_class":"pair_qs"}},
 "O3":{"a":{"future_accessibility_class":"pair_mn","identity_turnover_class":"turnover_2","persistence_class":"none","reconfiguration_class":"pair_mn"},
        "b":{"future_accessibility_class":"pair_no","identity_turnover_class":"turnover_2","persistence_class":"none","reconfiguration_class":"pair_no"},
        "c":{"future_accessibility_class":"pair_mo","identity_turnover_class":"turnover_2","persistence_class":"none","reconfiguration_class":"pair_mo"}}
}
PRESENTATIONS=["P1","P2"]
CONDITIONS=["INTACT","SCRAMBLED","NULL"]
RECORDS=[]

for op, mapping in OPS.items():
    ids=[f"{op}-{i:02d}" for i in range(1,25)]
    rng=random.Random(SEED + {"O1":0,"O2":1,"O3":2}[op])
    rng.shuffle(ids)
    # Balanced 8 per condition and 12 per presentation.
    assignments=[]
    for i, iid in enumerate(ids):
        condition=CONDITIONS[(i//8)%3]
        presentation=PRESENTATIONS[(i//4)%2]
        assignments.append((iid,condition,presentation))
    for iid,condition,presentation in assignments:
        future_mapping=None
        if condition=="INTACT":
            future_mapping=mapping
        elif condition=="SCRAMBLED":
            perm={"a":"b","b":"c","c":"a"}
            future_mapping={a:mapping[perm[a]] for a in ACTIONS}
        RECORDS.append({
          "instance_id":iid,"operationalisation":op,"seed":SEED,
          "state":{"state_id":"S0","T_acc":["a","b","c"]},
          "available_transformations":ACTIONS,
          "condition":condition,"presentation":presentation,
          "information":{
            "current_task":{"task":"select_one_current_transformation","candidate_count":3},
            "future_space_mapping":future_mapping,
            "future_signal": condition!="NULL"
          },
          "transition_spec":{
            a:{"successor_state":f"S_{a.upper()}","T_acc_t1":mapping[a],"descriptor":DESCRIPTORS[op][a]}
            for a in ACTIONS
          },
          "temporal_order":["information_presentation","transformation_selection","successor_realisation","future_accessibility_reveal"],
          "selected_transformation":None,"S_t1":None,"T_acc_t1":None,
          "decision_before_future_reveal":True,
          "scientific_execution":False
        })

out={"schema":VERSION,"randomisation_seed":SEED,"actions":ACTIONS,
     "operationalisations":OPS,"presentation_variants":PRESENTATIONS,
     "conditions":CONDITIONS,"instance_count":len(RECORDS),"instances":RECORDS,
     "scientific_execution":False}
raw=json.dumps(out,sort_keys=True,separators=(",",":")).encode()
out["fixture_sha256"]=hashlib.sha256(raw).hexdigest()
print(json.dumps(out,indent=2,sort_keys=True))
