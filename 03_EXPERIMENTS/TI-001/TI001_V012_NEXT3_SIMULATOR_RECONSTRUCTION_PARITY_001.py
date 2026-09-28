#!/usr/bin/env python3
"""NEXT3 deterministic simulator/reconstruction parity harness.

Non-scientific validation only.
"""
import importlib.util
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
def load(name,path):
 spec=importlib.util.spec_from_file_location(name,path)
 m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
sim=load("sim",ROOT/"TI001_V012_NEXT3_DETERMINISTIC_SIMULATOR_001.py")
rec=load("rec",ROOT/"TI001_V012_NEXT3_INDEPENDENT_RECONSTRUCTION_001.py")

CASES=[
 {"domain":"D1_spatial_planning","operationalisation":"O1_cardinality","action":"A","z":{"A":"slot_1","B":"slot_2","C":"slot_3","D":"slot_4"}},
 {"domain":"D2_resource_planning","operationalisation":"O2_topology","action":"B","z":{"A":"slot_4","B":"slot_1","C":"slot_2","D":"slot_3"}},
 {"domain":"D3_graph_reconfiguration","operationalisation":"O4_constraints","action":"C","z":{"A":"slot_3","B":"slot_4","C":"slot_1","D":"slot_2"}},
 {"domain":"D4_workflow_state_machine","operationalisation":"O5_composition","action":"D","z":{"A":"slot_2","B":"slot_1","C":"slot_4","D":"slot_3"}}
]
BASE={"active":[1,2],"relations":[[1,2,"seed"]],"constraints":[["base","valid",0]]}
results=[]
for i,c in enumerate(CASES,1):
 out=sim.execute_transition(BASE,c["action"],c["z"],c["domain"],c["operationalisation"])
 rr=rec.reconstruct(BASE,c["action"],c["z"],c["domain"],c["operationalisation"])
 results.append({
  "case":i,
  "S_t_plus_1_sha256_simulator":out["S_t_plus_1_sha256"],
  "S_t_plus_1_sha256_reconstruction":rr["successor_sha256"],
  "realized_transformation_sha256_simulator":out["realized_transformation_sha256"],
  "realized_transformation_sha256_reconstruction":rr["transformation_sha256"],
  "S_t_plus_1_match":out["S_t_plus_1_sha256"]==rr["successor_sha256"],
  "realized_transformation_match":out["realized_transformation_sha256"]==rr["transformation_sha256"]
 })
print(json.dumps({"status":"PARITY_PASS" if all(x["S_t_plus_1_match"] and x["realized_transformation_match"] for x in results) else "PARITY_FAIL","scientific_execution":False,"cases":results},sort_keys=True,indent=2))
