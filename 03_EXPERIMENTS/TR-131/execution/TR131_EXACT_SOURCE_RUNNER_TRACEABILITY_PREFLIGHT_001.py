#!/usr/bin/env python3
from __future__ import annotations
import json, hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parent
LOCK=ROOT/"TR131_EXACT_FIXTURE_SOURCE_LOCK_v01.json"
MANIFEST=ROOT.parent/"TR-131_EXACT_SOURCE_FREEZE_CANDIDATE_MANIFEST_v03.json"

def canon(x): return json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False)
def sha(x): return hashlib.sha256(canon(x).encode()).hexdigest()

def visitall_apply(s, action):
    cur,nxt=action.split(":")[1].split("->")
    assert s["at_robot"] == cur
    out={"at_robot":nxt,"visited":sorted(set(s["visited"])|{nxt})}
    return out

def rainbow_inc(s):
    assert s["LB0_dimmer"] < s["DIMMER_LEVELS"]
    out=dict(s); out["LB0_dimmer"]=s["LB0_dimmer"]+1; return out

def rainbow_remove(s):
    assert len(s["servers"]) > 1
    out=dict(s); out["servers"]=list(s["servers"][:-1]); return out

def main():
    lock=json.loads(LOCK.read_text(encoding="utf-8"))
    manifest=json.loads(MANIFEST.read_text(encoding="utf-8"))
    checks={}
    checks["manifest_version"]=manifest["manifest_version"]=="v0.3"
    checks["execution_blocked"]=manifest["scientific_execution_authorized"] is False
    checks["visitall_revision"]=lock["visitall"]["revision"]==manifest["source_revisions"]["visitall_instances"]["revision"]
    checks["visitall_blob"]=lock["visitall"]["blob_sha"]==manifest["source_revisions"]["visitall_instances"]["blob"]
    checks["visitall_tacc_cardinality"]=lock["visitall"]["t_acc"]["cardinality"]==4
    checks["rainbow_revision"]=lock["rainbow"]["revision"]==manifest["source_revisions"]["rainbow"]["revision"]
    checks["rainbow_model_blob"]=lock["rainbow"]["model_blob_sha"]==manifest["source_revisions"]["rainbow"]["model_blob"]
    checks["rainbow_tactics_blob"]=lock["rainbow"]["tactics_blob_sha"]==manifest["source_revisions"]["rainbow"]["tactics_blob"]
    checks["rainbow_tacc_minimum"]=lock["rainbow"]["t_acc_minimum"]["cardinality"]>=2
    checks["X_A"]=manifest["x"]["A"]=="SELECT_RANK_0"
    checks["X_B"]=manifest["x"]["B"]=="SELECT_RANK_1"

    va={"at_robot":lock["visitall"]["initial_state"]["at_robot"],"visited":lock["visitall"]["initial_state"]["visited"]}
    a=visitall_apply(va,lock["visitall"]["t_acc"]["transformations"][0])
    b=visitall_apply(va,lock["visitall"]["t_acc"]["transformations"][1])
    checks["visitall_A_B_same_S0"]=va=={"at_robot":"loc-x2-y2","visited":["loc-x2-y2"]}
    checks["visitall_A_B_distinct_realization"]=a["at_robot"]!=b["at_robot"]

    rw={"LB0_dimmer":lock["rainbow"]["state_defaults"]["LB0_dimmer"],
        "DIMMER_LEVELS":lock["rainbow"]["state_defaults"]["DIMMER_LEVELS"],
        "servers":lock["rainbow"]["state_defaults"]["servers"]}
    ra=rainbow_inc(rw); rb=rainbow_remove(rw)
    checks["rainbow_A_B_same_S0"]=rw["LB0_dimmer"]==1 and len(rw["servers"])==3
    checks["rainbow_A_B_distinct_realization"]=ra!=rb

    report={"record_type":"TGCV_TR131_EXACT_SOURCE_RUNNER_TRACEABILITY_PREFLIGHT",
            "status":"RUNNER_PREFLIGHT_PASS" if all(checks.values()) else "RUNNER_PREFLIGHT_BLOCKED",
            "scientific_execution_authorized":False,
            "scientific_execution_performed":False,
            "checks":checks,
            "trace_hashes":{"visitall_A":sha(a),"visitall_B":sha(b),"rainbow_A":sha(ra),"rainbow_B":sha(rb)}}
    print(json.dumps(report,indent=2))
    return 0 if all(checks.values()) else 2

if __name__=="__main__": raise SystemExit(main())
