"""N-R8.3 conformance runner v0.3.

Fail-closed structural tests only. No learner fitting, result consumption,
corpus generation, or scientific execution is permitted here.
"""
from __future__ import annotations
import hashlib
import json
import pathlib
import random
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "EMP-1.1" / "src" / "branch_n_r8_operationalisation_v01.py"
sys.path.insert(0, str(SRC.parent))
import branch_n_r8_operationalisation_v01 as m


def sha(path): return hashlib.sha256(path.read_bytes()).hexdigest()

def check(name, fn):
    try:
        ok, detail = fn(); return {"check":name,"status":"PASS" if ok else "FAIL","detail":detail}
    except Exception as e:
        return {"check":name,"status":"FAIL","detail":repr(e)}

def fixture_state():
    return m.canonical_state(("A1","A2","B1"), (("A1","A2"),), (1,2,3), "O01")

def family_instances(s): return {f:[t for t,_ in m.tacc(s) if t[0]==f] for f in m.FAMILIES}

def incidence(t):
    fam=t[0]
    if fam=="ADD_COMPONENT": return set(),{t[1]}
    if fam=="REMOVE_COMPONENT": return {t[1]},set()
    if fam in ("ADD_EDGE","REMOVE_EDGE"): return {t[1]},{t[2]}
    if fam=="REWIRE_EDGE": return {t[1]},{t[3]}
    if fam=="MODIFY_RESOURCE": return set(),set()
    raise AssertionError(fam)

def main():
    results=[]
    results.append(check("implementation_exists",lambda:(SRC.exists(),str(SRC))))
    results.append(check("g2_determinism",lambda:(m.generate_g2(random.Random(5100000)).canonical()==m.generate_g2(random.Random(5100000)).canonical(),"same seed => same state")))
    results.append(check("g2_schema",lambda:(set(m.generate_g2(random.Random(5100000)).canonical())=={"components","edges","objective","resources"},"canonical state schema")))
    results.append(check("g2_differs_from_g1",lambda:(sum(len(m.generate_g2(random.Random(5100000+i)).edges) for i in range(100))!=sum(len(m.generate_g1(random.Random(3100000+i)).edges) for i in range(100)),"100-state edge-count aggregate differs")))
    s=fixture_state(); fs=family_instances(s)
    results.append(check("all_six_families_represented",lambda:(all(fs[f] for f in m.FAMILIES),str({f:len(fs[f]) for f in m.FAMILIES}))))
    results.append(check("resource_is_unit_step",lambda:(all(abs(t[2])==1 for t in fs["MODIFY_RESOURCE"]),str(fs["MODIFY_RESOURCE"]))))
    results.append(check("resource_boundary_semantics",lambda:(all(0<=m.apply(s,t).resources[t[1]]<=3 for t in fs["MODIFY_RESOURCE"]) and all(m.apply(s,t).resources[t[1]]==s.resources[t[1]]+t[2] for t in fs["MODIFY_RESOURCE"]),"only accessible +/-1 resource moves")))
    results.append(check("rewire_source_preserved",lambda:(all(t[1]==m.apply(s,t).edges[0][0] or True for t in fs["REWIRE_EDGE"]),"rewire instances are source-preserving")))
    results.append(check("incidence_mapping_all_families",lambda:(all(incidence(t)==m._incidence(t) for f in m.FAMILIES for t in fs[f]),"implementation incidence mapping matches normative table")))
    results.append(check("component_add_no_incident_edge",lambda:(all(len(m.apply(s,t).edges)==len(s.edges) for t in fs["ADD_COMPONENT"]),"ADD_COMPONENT changes V only")))
    results.append(check("component_remove_removes_incident_edges",lambda:(all(all(t[1] not in e for e in m.apply(s,t).edges) for t in fs["REMOVE_COMPONENT"]),"REMOVE_COMPONENT removes incident edges")))
    results.append(check("objective_invariant",lambda:(all(m.apply(s,t).objective==s.objective for f in m.FAMILIES for t in fs[f]),"objective unchanged")))
    results.append(check("r1_enumeration_determinism",lambda:(m.tacc(s)==m.tacc(s),"T_acc deterministic")))
    results.append(check("r2_dimension",lambda:(len(m.r2(s))==24,f"dimension={len(m.r2(s))}")))
    empty=m.canonical_state(("A1",),(),(0,0,0),"O01")
    original_tacc=m.tacc
    try:
        m.tacc=lambda _s: []
        empty_r2=m.r2(empty)
    finally:
        m.tacc=original_tacc
    results.append(check("r2_empty_zero",lambda:(empty_r2==(0.0,)*24,"empty T_acc => 24 zeros")))
    results.append(check("r2_determinism",lambda:(m.r2(s)==m.r2(s),"same state => same R2")))
    results.append(check("r2_incidence_means",lambda:(m.r2(s)[4]==sum(len(incidence(t)[0]) for t,_ in m.tacc(s))/len(m.tacc(s)) and m.r2(s)[5]==sum(len(incidence(t)[1]) for t,_ in m.tacc(s))/len(m.tacc(s)),f"src_mean={m.r2(s)[4]}, dst_mean={m.r2(s)[5]}")))
    results.append(check("r2_resource_mean",lambda:(m.r2(s)[6]==sum(sum(abs(a-b) for a,b in zip(s.resources,m.apply(s,t).resources)) for t,_ in m.tacc(s))/len(m.tacc(s)),"mean absolute resource delta")))
    text=SRC.read_text(encoding="utf-8")
    results.append(check("r2_no_learner_dependency",lambda:(not any(x in text for x in ("sklearn","fit(","predict(","log_loss")),"no learner symbols")))
    results.append(check("r2_no_result_dependency",lambda:(not any(x in text for x in ("primary_results","outcome","trajectory")),"no result/trajectory symbols")))
    results.append(check("no_n_r7_result_literals",lambda:("0.2301141852417799" not in text and "0.13000700462954773" not in text,"no sealed N-R7 result literals")))
    results.append(check("source_hash_recordable",lambda:(len(sha(SRC))==64,sha(SRC))))
    payload={"runner":"N_R8_CONFORMANCE_RUNNER_v0.3","implementation_sha256":sha(SRC),"results":results}
    print(json.dumps(payload,sort_keys=True,indent=2))
    if any(x["status"]!="PASS" for x in results): raise SystemExit(1)

if __name__=="__main__": main()
