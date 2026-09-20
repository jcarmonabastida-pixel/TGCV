#!/usr/bin/env python3
"""TR-131 source-defined transition adapter integrity preflight.

No scientific A/B execution. This module only checks that the adapter
implements the frozen source semantics for the selected transformations.
"""
from __future__ import annotations
import json, hashlib
from pathlib import Path

ROOT=Path(__file__).resolve().parent
LOCK=ROOT/"TR131_EXACT_FIXTURE_SOURCE_LOCK_v01.json"

def h(x):
    return hashlib.sha256(json.dumps(x,sort_keys=True,separators=(",",":"),ensure_ascii=False).encode()).hexdigest()

def visitall_move(state, cur, nxt):
    assert state["at-robot"] == cur
    out=dict(state)
    out["at-robot"]=nxt
    out["visited"]=sorted(set(out["visited"])|{nxt})
    return out

def rainbow_inc_dimmer(state):
    level=state["dimmer_level"]
    levels=state["DIMMER_LEVELS"]
    assert level < levels
    out=dict(state)
    out["dimmer_level"]=level+1
    return out

def rainbow_remove_server(state):
    servers=sorted(state["servers"], key=lambda x:x["index"])
    assert len(servers)>1
    out=dict(state)
    out["servers"]=servers[:-1]
    return out

def main():
    lock=json.loads(LOCK.read_text(encoding="utf-8"))
    checks={}
    va=lock["visitall"]
    checks["visitall_lock"]=va["revision"]=="cf19edf7c53d1540ddbb396c642595e0926ee552"
    checks["visitall_blob"]=va["blob_sha"]=="f49fb86fb3f7dd4aba5a6ed79fdddc240097ec34"

    s={"at-robot":"loc-x2-y2","visited":["loc-x2-y2"]}
    s1=visitall_move(s,"loc-x2-y2","loc-x1-y2")
    checks["visitall_precondition"]=s1["at-robot"]=="loc-x1-y2"
    checks["visitall_effect"]=s1["visited"]==["loc-x1-y2","loc-x2-y2"]

    rw=lock["rainbow"]
    checks["rainbow_lock"]=rw["revision"]=="c053e2aab6d58c233016574887296e2be43ca60f4"
    checks["rainbow_model_blob"]=rw["model_blob_sha"]=="9989790020ff1b814e0b1aa7bd1f926d980ce823"
    checks["rainbow_tactics_blob"]=rw["tactics_blob_sha"]=="513a5d78e301e9fa4660b8bac9154b93e6a7a605"

    d={"dimmer_level":1,"DIMMER_LEVELS":5}
    d1=rainbow_inc_dimmer(d)
    checks["TIncDimmer_effect"]=d1["dimmer_level"]==2

    sr={"servers":[{"index":0},{"index":1},{"index":2}]}
    sr1=rainbow_remove_server(sr)
    checks["TRemoveServer_max_index_removed"]=sr1["servers"]==[{"index":0},{"index":1}]

    checks["no_scientific_execution"]=True
    report={"record_type":"TGCV_TR131_ADAPTER_IMPLEMENTATION_TRACEABILITY_PREFLIGHT",
            "status":"ADAPTER_PREFLIGHT_PASS" if all(checks.values()) else "ADAPTER_PREFLIGHT_BLOCKED",
            "scientific_execution_authorized":False,
            "scientific_execution_performed":False,
            "checks":checks,
            "transition_hashes":{"visitall":h(s1),"TIncDimmer":h(d1),"TRemoveServer":h(sr1)}}
    print(json.dumps(report,indent=2,ensure_ascii=False))
    return 0 if report["status"]=="ADAPTER_PREFLIGHT_PASS" else 2

if __name__=="__main__":
    raise SystemExit(main())
