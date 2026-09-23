#!/usr/bin/env python3
"""TR-131 VisitAll independent Executor-1/Executor-2 comparison audit.

Audit only. It consumes two persisted local JSON outputs, compares the
scientific structure without requiring byte identity, and emits no scientific
interpretation beyond PASS/FAIL/INCONCLUSIVE of reconstruction agreement.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
E1=ROOT/"results"/"TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR1_RUN_001.json"
E2=ROOT/"results"/"TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR2_RECONSTRUCTION_001.json"

def load(p):
    return json.loads(p.read_text(encoding="utf-8"))

def node_key(n):
    return (n["branch"], n["depth"], n["S_t"], n["T_acc_t"], n.get("T_real_t"),
            n.get("S_parent"), n.get("T_acc_parent"), n.get("Delta_T_acc_from_parent"),
            n.get("baseline"))

def main():
    if not E1.exists() or not E2.exists():
        raise SystemExit("MISSING_PERSISTED_EXECUTOR_OUTPUT")
    a,b=load(E1),load(E2)
    checks={
      "e1_completed": a.get("status")=="COMPLETED",
      "e2_completed": b.get("status")=="COMPLETED",
      "e1_authorized_performed": a.get("scientific_execution_authorized") is True and a.get("scientific_execution_performed") is True,
      "e2_authorized_performed": b.get("scientific_execution_authorized") is True and b.get("scientific_execution_performed") is True,
      "same_source_revision": a.get("source_revision")==b.get("source_revision"),
      "same_source_blob": a.get("source_blob_sha")==b.get("source_blob_sha"),
      "same_problem": a.get("problem")==b.get("problem")=="grid-5",
      "same_depth": a.get("depth")==b.get("depth")==2,
      "same_root_tacc": a.get("root_tacc")==b.get("root_tacc"),
      "same_node_count": a.get("node_count")==b.get("node_count")==21,
    }
    # E1 may use a different top-level schema; compare its nodes when present.
    e1nodes=a.get("nodes",[])
    e2nodes=b.get("nodes",[])
    checks["same_node_count_actual"]=len(e1nodes)==len(e2nodes)==21
    if len(e1nodes)!=len(e2nodes):
        checks["node_structure_equal"]=False
    else:
        checks["node_structure_equal"]=all(node_key(x)==node_key(y) for x,y in zip(e1nodes,e2nodes))
    checks["root_hash_present_and_equal"]=bool(e1nodes and e2nodes and e1nodes[0].get("T_acc_hash")==e2nodes[0].get("T_acc_hash"))
    checks["byte_identity_not_required"]=True
    status="PASS" if all(checks.values()) else "FAIL"
    print(json.dumps({
      "record_type":"TGCV_TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR_COMPARISON_AUDIT",
      "status":status,
      "scientific_result_interpretation":"NOT_PERFORMED",
      "byte_identity_required":False,
      "e1_sha256":hashlib.sha256(E1.read_bytes()).hexdigest(),
      "e2_sha256":hashlib.sha256(E2.read_bytes()).hexdigest(),
      "checks":checks
    },indent=2,ensure_ascii=False))
    return 0 if status=="PASS" else 2

if __name__=="__main__":
    raise SystemExit(main())
