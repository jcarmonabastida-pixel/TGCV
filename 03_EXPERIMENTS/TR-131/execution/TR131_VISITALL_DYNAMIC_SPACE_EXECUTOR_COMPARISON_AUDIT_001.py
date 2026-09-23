#!/usr/bin/env python3
"""TR-131 VisitAll independent Executor-1/Executor-2 comparison audit."""
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
E1=ROOT/"results"/"TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR1_RUN_001.json"
E2=ROOT/"results"/"TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR2_RECONSTRUCTION_001.json"

def load(p):
    return json.loads(p.read_text(encoding="utf-8"))

def canon(v):
    if isinstance(v, dict):
        return {k:canon(v[k]) for k in sorted(v)}
    if isinstance(v, list):
        return sorted((canon(x) for x in v), key=lambda x: json.dumps(x,sort_keys=True,separators=(",",":")))
    return v

def node_signature(n):
    # Branch labels and list ordering are executor-local representation details.
    # Compare the scientific node content as an unordered canonical structure.
    x={k:v for k,v in n.items() if k!="branch"}
    return json.dumps(canon(x),sort_keys=True,separators=(",",":"))

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
      "same_root_tacc": canon(a.get("root_tacc"))==canon(b.get("root_tacc")),
      "same_node_count": a.get("node_count")==b.get("node_count")==21,
    }
    e1nodes=a.get("nodes",[])
    e2nodes=b.get("nodes",[])
    checks["same_node_count_actual"]=len(e1nodes)==len(e2nodes)==21
    s1=sorted(node_signature(x) for x in e1nodes)
    s2=sorted(node_signature(x) for x in e2nodes)
    checks["node_structure_equal"]=s1==s2
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
