#!/usr/bin/env python3
"""TR-131 VisitAll independent Executor-1/Executor-2 comparison audit."""
from __future__ import annotations
import hashlib,json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
E1=ROOT/"results"/"TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR1_RUN_001.json"
E2=ROOT/"results"/"TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR2_RECONSTRUCTION_001.json"
def load(p): return json.loads(p.read_text(encoding="utf-8"))
def canon(v):
    if isinstance(v,dict): return {k:canon(v[k]) for k in sorted(v)}
    if isinstance(v,list): return sorted((canon(x) for x in v),key=lambda x:json.dumps(x,sort_keys=True,separators=(",",":")))
    return v
def node_sig(n): return json.dumps(canon(n),sort_keys=True,separators=(",",":"))
def main():
    if not E1.exists() or not E2.exists(): raise SystemExit("MISSING_PERSISTED_EXECUTOR_OUTPUT")
    a,b=load(E1),load(E2); an=a.get("nodes",[]); bn=b.get("nodes",[])
    e1root=next((n for n in an if n.get("depth")==0),None)
    e2root=next((n for n in bn if n.get("depth")==0),None)
    checks={
      "e1_completed":a.get("status")=="COMPLETED","e2_completed":b.get("status")=="COMPLETED",
      "e1_authorized_performed":a.get("scientific_execution_authorized") is True and a.get("scientific_execution_performed") is True,
      "e2_authorized_performed":b.get("scientific_execution_authorized") is True and b.get("scientific_execution_performed") is True,
      "same_source_revision":a.get("source_revision")==b.get("source_revision"),
      "same_source_blob":a.get("source_blob_sha")==b.get("source_blob_sha"),
      "same_problem":a.get("problem")==b.get("problem")=="grid-5","same_depth":a.get("depth")==b.get("depth")==2,
      "same_node_count":a.get("node_count")==b.get("node_count")==21,
      "same_node_count_actual":len(an)==len(bn)==21,
      "same_root_tacc_cardinality":a.get("root_tacc_cardinality")==len(e2root.get("T_acc_t",[]))==4 if e2root else False,
      "same_root_tacc":canon(e1root.get("T_acc_t",[]))==canon(e2root.get("T_acc_t",[])) if e1root and e2root else False,
      "same_root_hash":e1root.get("T_acc_hash")==e2root.get("T_acc_hash") if e1root and e2root else False,
      "node_structure_equal":sorted(node_sig(x) for x in an)==sorted(node_sig(x) for x in bn),
      "byte_identity_not_required":True
    }
    status="PASS" if all(checks.values()) else "FAIL"
    print(json.dumps({"record_type":"TGCV_TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR_COMPARISON_AUDIT","status":status,"scientific_result_interpretation":"NOT_PERFORMED","byte_identity_required":False,"e1_sha256":hashlib.sha256(E1.read_bytes()).hexdigest(),"e2_sha256":hashlib.sha256(E2.read_bytes()).hexdigest(),"checks":checks},indent=2,ensure_ascii=False))
    return 0 if status=="PASS" else 2
if __name__=="__main__": raise SystemExit(main())
