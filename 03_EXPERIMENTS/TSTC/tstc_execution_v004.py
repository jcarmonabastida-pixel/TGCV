"""TGCV WP2 TSTC execution adapter v004.

v004 corrects the frozen Minimum Demonstrator output contract. It keeps
Fixture-003 immutable and does not reinterpret TSTC_EXECUTION_v003.

The conventional baseline is reconstructed independently from the TGCV
`tacc()` implementation using compact domain-specific feasibility rules.
The comparison is qualitative and explicitly reports the eight dimensions
required by the frozen specification.
"""
from __future__ import annotations
import hashlib, json, platform, subprocess, sys
from copy import deepcopy
from tstc_fixture_engine_v003 import fixtures, tacc, digest

EXECUTION_VERSION = "TSTC_EXECUTION_v004"
FIXTURE_VERSION = "003"

def _fixture_by_id(fs, fid): return next(f for f in fs if f.fixture_id == fid)
def _find(f, tid): return next(t for t in f.transformations if t.transformation_id == tid)
def _changed(before, after):
    s0,c0=before; s1,c1=after
    return tuple(sorted([k for k in set(s0)|set(s1) if s0.get(k)!=s1.get(k)] + [k for k in set(c0)|set(c1) if c0.get(k)!=c1.get(k)]))
def _apply(f, op, allowed):
    before=(deepcopy(f.state),deepcopy(f.context)); after=op(*before); changed=_changed(before,after)
    assert not (set(changed)-set(allowed)), "undeclared intervention mutation"
    return before,after,changed
def _transition(f, tid, state, context):
    t=_find(f,tid); assert t.predicate(state,context), f"inaccessible transformation used: {tid}"
    before=(deepcopy(state),deepcopy(context)); after=t.transition(*before); changed=_changed(before,after)
    assert not (set(changed)-set(t.affected_variables)), f"{tid}: undeclared mutation"
    return before,after,changed
def _delta(a,b):
    a,b=set(a),set(b); return {"opened":tuple(sorted(b-a)),"closed":tuple(sorted(a-b)),"persistent":tuple(sorted(a&b)),"changed":tuple(sorted((a-b)|(b-a)))}
def _trajectory(f,state,context):
    actions,_=tacc(f,state,context); assert actions; tid=actions[0]; before,after,changed=_transition(f,tid,state,context)
    return [{"step":0,"transformation_id":tid,"S_before":before[0],"C_before":before[1],"S_after":after[0],"C_after":after[1],"changed_variables":changed}]

# Independent conventional baseline feasibility functions.
def _baseline_actions(f,state,context):
    s,c=state,context
    if f.fixture_id=="FX-C01":
        return tuple(x for x,ok in (("c01.deploy_A",s["service"]=="absent" and s["compute_A"]=="free" and c["policy_deploy"]=="allowed" and s["security"]=="normal"),("c01.deploy_B",s["service"]=="absent" and s["compute_B"]=="free" and c["policy_deploy"]=="allowed" and c["trust_B"]=="trusted" and s["security"]=="normal"),("c01.route_A_to_B",s["service"]=="deployed" and s["routing"]=="A" and s["compute_B"]=="free" and c["trust_B"]=="trusted" and s["security"]=="normal"),("c01.route_B_to_A",s["service"]=="deployed" and s["routing"]=="B" and s["compute_A"]=="free" and s["security"]=="normal"),("c01.restrict_security",s["security"]=="normal"),("c01.restore_security",s["security"]=="restricted")) if ok)
    if f.fixture_id=="FX-C03":
        return tuple(x for x,ok in (("c03.query_db",s["db"]=="available" and c["permission_db"]=="granted" and c["tool_query"]=="available"),("c03.inspect_repo",s["repo"] in ("clean","changed") and c["permission_repo"]=="granted"),("c03.open_pr",c["permission_repo"]=="granted" and c["tool_pr"]=="available" and s["repo"] in ("clean","changed")),("c03.complete_task",s["task"]=="pending"),("c03.modify_repo",s["repo"]=="clean" and c["permission_repo"]=="granted")) if ok)
    return tuple(x for x,ok in (("c05.start_A",s["site_A"]=="available" and s["grid_capacity"]=="high" and s["ev_A"]=="waiting"),("c05.start_B",s["site_B"]=="available" and s["grid_capacity"]=="high" and s["ev_B"]=="waiting"),("c05.defer_A",s["ev_A"]=="waiting"),("c05.defer_B",s["ev_B"]=="waiting"),("c05.redirect_A_to_B",s["ev_A"]=="waiting" and s["site_B"]=="available" and c["mobility_requirement_A"]!="urgent"),("c05.reduce_power_A",s["ev_A"]=="charging" and c["charger_A"] in ("V1G","V2G"))) if ok)
def _baseline_model(fid): return {"FX-C01":"finite-state-orchestration-rule-model","FX-C03":"capability-access-control-matrix-plus-workflow","FX-C05":"finite-constrained-resource-feasibility-model"}[fid]
def _comparison(f,before,after,tg0,tg1,trajectory):
    bb=_baseline_actions(f,*before); ba=_baseline_actions(f,*after); assert tuple(tg0)==bb and tuple(tg1)==ba
    observations={"transformation_identities":"equivalent within frozen U_tau","admissibility_conditions":"reconstructed independently with conventional domain rules","state_context_dependencies":"represented explicitly in both reconstructions","transition_causing_accessibility_change":"captured as declared intervention and changed variables","cross_domain_dependency":"not applicable to local connector record; logged separately in cross_domain_results","trajectory_consequence":"same bounded trajectory transformation is admissible under both representations","assumptions":"same frozen S0/C0/U_tau; no downstream outcomes supplied","information_omitted":"no value, ROI, empirical outcome, causal or industrial information used"}
    return {"category":"EQUIVALENT_REPRESENTATION","comparison_observations":observations,"baseline_reconstruction":{"before_feasible_transformations":bb,"after_feasible_transformations":ba,"Delta_T_acc":_delta(bb,ba)},"baseline_representation":{"model":_baseline_model(f.fixture_id),"state":deepcopy(before[0]),"context":deepcopy(before[1])}}
def _record(f):
    before,after,changed=_apply(f,f.intervention,f.intervention_variables); t0,_=tacc(f,*before); t1,_=tacc(f,*after); delta=_delta(t0,t1); trajectory=_trajectory(f,*after); comp=_comparison(f,before,after,t0,t1,trajectory)
    assert set(t0).issubset({t.transformation_id for t in f.transformations}) and set(t1).issubset({t.transformation_id for t in f.transformations})
    return {"fixture_id":f.fixture_id,"fixture_version":f.fixture_version,"connector_id":f.fixture_id.replace("FX-",""),"intervention_id":f.intervention_id,"S0":before[0],"C0":before[1],"L_version":"TSTC_FIXTURE_ENGINE_v003","U_tau":tuple(t.transformation_id for t in f.transformations),"T_acc_0":t0,"transition":{"type":"declared_intervention","changed_variables":changed},"S1":after[0],"C1":after[1],"T_acc_1":t1,"Delta_T_acc":delta,"trajectory":trajectory,"baseline_model":_baseline_model(f.fixture_id),"baseline_representation":comp["baseline_representation"],"baseline_reconstruction":comp["baseline_reconstruction"],"comparison_observations":comp["comparison_observations"],"comparison_category":comp["category"]}
def _negative(f):
    before,after,changed=_apply(f,f.negative_control,f.negative_control_variables); t0,_=tacc(f,*before); t1,_=tacc(f,*after); delta=_delta(t0,t1); assert delta["changed"]==() and delta["opened"]==() and delta["closed"]==()
    return {"negative_control_id":f.negative_control_id,"changed_variables":changed,"T_acc_0":t0,"T_acc_1":t1,"Delta_T_acc":delta}
def _cross_domain(fs):
    c01=_fixture_by_id(fs,"FX-C01"); c03=_fixture_by_id(fs,"FX-C03"); c05=_fixture_by_id(fs,"FX-C05"); b,a,ch=_apply(c01,_find(c01,"c01.restrict_security").transition,("security",)); c01_0,_=tacc(c01); c01_1,_=tacc(c01,*a); c03ctx=deepcopy(c03.context); c03ctx["permission_repo"]="denied"; c03_0,_=tacc(c03); c03_1,_=tacc(c03,c03.state,c03ctx); assert "c03.modify_repo" in c03_0 and "c03.modify_repo" not in c03_1; b2,a2,ch2=_transition(c03,"c03.modify_repo",c03.state,c03.context); c03b0,_=tacc(c03,*b2); c03b1,_=tacc(c03,*a2); c05ctx=deepcopy(c05.context); c05ctx["mobility_requirement_A"]="urgent"; c05_0,_=tacc(c05); c05_1,_=tacc(c05,c05.state,c05ctx); assert "c05.redirect_A_to_B" in c05_0 and "c05.redirect_A_to_B" not in c05_1
    return {"C01_to_C03":{"scenario_id":"CD-C01-C03-001","source_delta":_delta(c01_0,c01_1),"propagation_rule":{"security":"restricted"},"target_delta":_delta(c03_0,c03_1),"non_claim":"synthetic rule propagation, not empirical causality"},"C03_to_C05":{"scenario_id":"CD-C03-C05-001","source_transition":"c03.modify_repo","source_delta":_delta(c03b0,c03b1),"propagation_rule":{"repo":"changed"},"target_delta":_delta(c05_0,c05_1),"non_claim":"synthetic rule propagation, not empirical causality"}}
def _source_commit(): return subprocess.check_output(["git","rev-parse","HEAD"],stderr=subprocess.DEVNULL,text=True).strip()
def run_execution():
    fs=fixtures(); records=[_record(f) for f in fs]; negatives={f.fixture_id:_negative(f) for f in fs}; cross=_cross_domain(fs)
    metadata={"execution_version":EXECUTION_VERSION,"fixture_version":FIXTURE_VERSION,"source_commit":_source_commit(),"fixture_manifest_hash":digest({f.fixture_id:{"fixture_version":f.fixture_version,"S":f.state,"C":f.context} for f in fs}),"ruleset_hash":digest("TSTC_FIXTURE_ENGINE_v003"),"transformation_universe_hash":digest({r["fixture_id"]:r["U_tau"] for r in records}),"configuration_hash":hashlib.sha256(json.dumps({"execution_version":EXECUTION_VERSION,"fixture_version":FIXTURE_VERSION},sort_keys=True).encode()).hexdigest(),"environment":{"python":sys.version.split()[0],"platform":platform.platform()},"random_seed":None}
    result={"status":"TSTC_EXECUTION_COMPLETE","mode":"TSTC_SYNTHETIC_EXECUTION_V004","run_records":records,"negative_controls":negatives,"cross_domain_results":cross,"limitations":["synthetic bounded demonstrator","no empirical causal inference","no downstream outcome measurement","no value/ROI analysis","no superiority claim","no generality claim"],"non_claims":["No scientific validity claim","No empirical causal claim","No superiority claim","No generality claim","No value creation claim","No industrial validation claim"],"execution_metadata":metadata}; result["execution_metadata"]["output_hash"]=digest(result); return result
if __name__=="__main__": print(json.dumps(run_execution(),sort_keys=True,indent=2,default=list))
