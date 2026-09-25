#!/usr/bin/env python3
"""TI-001 V006 runtime-correction compatibility preflight.
Infrastructure gate only. Never performs scientific execution.
"""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

EXPECTED_FIXTURE_GIT_BLOB_SHA="edd83fd2df3d39aad8911087569c19614c2264b7"
EXPECTED_FIXTURE_CANONICAL_SHA256="bc7e0e69cb56337145593e67fb55c1a1b5042db661520498a2c86b346eef76e5"
EXPECTED_PROVIDER="TI001_DECISION_AGENT_PROVIDER_V006_001"
EXPECTED_EXECUTOR="TI001_V005_SCIENTIFIC_EXECUTOR_001"
EXPECTED_EXECUTOR_GIT_BLOB_SHA="28f4dabedf1b053c0928f96c323c5e7d99feef5d"
EXPECTED_MODEL="gpt-5.6-luna"
EXPECTED_CONTRACT="TI001_V006_EXECUTION_CONTRACT_001"
EXPECTED_ESTIMAND="matched_condition_difference_in_transformation_selection"
EXPECTED_ACTIONS=["a","b","c"]

def load(p): return json.loads(Path(p).read_text(encoding="utf-8"))
def canonical_sha256(obj):
    raw=json.dumps(obj,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

def main(argv):
    p=argparse.ArgumentParser()
    for name in ("fixture","provider","executor","executor2","contract","runtime_spec","output"): p.add_argument(name)
    a=p.parse_args(argv[1:])
    fixture=load(a.fixture)
    provider=Path(a.provider).read_text(encoding="utf-8")
    executor=Path(a.executor).read_text(encoding="utf-8")
    executor2=Path(a.executor2).read_text(encoding="utf-8")
    contract=Path(a.contract).read_text(encoding="utf-8")
    runtime_spec=load(a.runtime_spec)
    checks={}; reasons={}
    checks["fixture_frozen_pass"]=fixture.get("status")=="FROZEN" and fixture.get("scientific_execution")=="NOT_AUTHORIZED"
    checks["fixture_canonical_sha256_pass"]=canonical_sha256(fixture)==EXPECTED_FIXTURE_CANONICAL_SHA256
    checks["fixture_git_blob_identity_declared_pass"]=EXPECTED_FIXTURE_GIT_BLOB_SHA in contract and EXPECTED_FIXTURE_GIT_BLOB_SHA in executor and EXPECTED_FIXTURE_GIT_BLOB_SHA in executor2
    checks["v005_fixture_identity_pass"]=fixture.get("fixture_id")=="TI001-v005-candidate-001" and fixture.get("version")=="v005-candidate-001"
    checks["condition_structure_pass"]=set(fixture.get("conditions",{}))=={"control","treatment","null"}
    checks["action_space_pass"]=all(fixture["conditions"][c].get("t_acc")==EXPECTED_ACTIONS and fixture["conditions"][c].get("actions")==EXPECTED_ACTIONS for c in fixture["conditions"])
    checks["treatment_mapping_pass"]=set(fixture["conditions"]["treatment"].get("future_mapping",{}))==set(EXPECTED_ACTIONS)
    checks["null_pass"]=fixture["conditions"]["null"].get("future_mapping") is None and fixture["conditions"]["null"].get("future_signal") is None
    checks["temporal_pass"]=fixture.get("successor_state_before_selection") is False and fixture.get("successor_accessibility_before_selection") is False
    checks["provider_binding_pass"]=EXPECTED_PROVIDER in provider and EXPECTED_MODEL in provider and "future_transformation_space_information" in provider
    checks["provider_reasoning_explicit_pass"]='reasoning=REASONING' in provider and 'REASONING = {"effort": "none"}' in provider
    checks["provider_isolation_pass"]=all(t not in provider for t in ['record["successors"]','record["future_alternatives"]','record["S_t1"]','record["T_acc_t1"]'])
    checks["provider_output_pass"]="selected_transformation" in provider and "decision_input_sha256" in provider
    executor_blob_sha=hashlib.sha1(("blob "+str(len(executor.encode("utf-8")))+"\0").encode()+executor.encode("utf-8")).hexdigest()
    checks["executor_binding_pass"]=EXPECTED_EXECUTOR in executor and "TI001_V005_EXECUTION_CONTRACT_001" in executor and EXPECTED_FIXTURE_GIT_BLOB_SHA in executor and executor_blob_sha==EXPECTED_EXECUTOR_GIT_BLOB_SHA
    checks["executor_no_successor_dependency_pass"]=not any(t in executor for t in ['fixture["successors"]','record["successors"]','successor =','transitions ='])
    checks["executor_estimand_pass"]=EXPECTED_ESTIMAND in executor and not any(t in executor for t in ["calculate_composite_ti_score","compute_composite_ti_score","composite_ti_score =","composite_ti_score="])
    checks["executor2_independence_pass"]=all(t not in executor2 for t in ["V005_DECISION_AGENT_PROVIDER","V005_SCIENTIFIC_EXECUTOR","Executor-1"])
    checks["executor2_hash_pass"]=EXPECTED_FIXTURE_GIT_BLOB_SHA in executor2
    checks["contract_binding_pass"]=EXPECTED_FIXTURE_GIT_BLOB_SHA in contract and EXPECTED_ESTIMAND in contract and EXPECTED_PROVIDER in contract and EXPECTED_EXECUTOR in contract
    checks["runtime_spec_pass"]=runtime_spec.get("authorized_runtime_change",{}).get("parameter")=="reasoning" and runtime_spec.get("authorized_runtime_change",{}).get("value")=={"effort":"none"} and runtime_spec.get("status")=="SPECIFICATION_ONLY — NO SCIENTIFIC EXECUTION AUTHORIZED"
    checks["runtime_model_pass"]=EXPECTED_MODEL in json.dumps(runtime_spec,sort_keys=True) and runtime_spec.get("frozen_runtime_parameters",{}).get("max_output_tokens")==64
    has_execute_flag='"--execute"' in provider or 'add_argument("--execute"' in provider
    has_execute_branch='if not args.execute:' in provider
    has_scientific_call='client.responses.create(' in provider
    checks["execution_requires_explicit_flag_pass"]=has_execute_flag and has_execute_branch and has_scientific_call and provider.find('if not args.execute:') < provider.find('client.responses.create(')
    checks["scientific_execution_absent_pass"]=checks["execution_requires_explicit_flag_pass"]
    checks["v004_dependency_absent_pass"]=not any(t in (provider+executor+executor2+contract) for t in ["20ad94fcaca2e85228f1a266ae69d9d391a35182a64ab122fd5feed56b46a4dd","582031","731407","TI001_PREFLIGHT_FIXTURE_v004"])
    for k,v in checks.items():
        if not v: reasons[k]="v006 runtime-correction compatibility requirement failed"
    out={**checks,"overall_compatibility_pass":all(checks.values()),"reasons":reasons,"scientific_execution":"NOT_AUTHORIZED"}
    Path(a.output).write_text(json.dumps(out,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print(json.dumps(out,indent=2,sort_keys=True))
    return 0 if out["overall_compatibility_pass"] else 1

if __name__=="__main__": raise SystemExit(main(__import__("sys").argv))
