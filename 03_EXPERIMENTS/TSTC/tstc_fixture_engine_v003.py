"""TGCV WP2 TSTC deterministic Fixture-003 engine.

Preflight/conformance only. This engine binds to
TGCV_APPLICATION_FIT_WP2_TSTC_SYNTHETIC_FIXTURES_FREEZE_003.md.
It does not execute trajectories, baselines, outcomes, or value analysis.
"""
from __future__ import annotations
from copy import deepcopy
from dataclasses import dataclass
import hashlib, json
from typing import Callable, Tuple

VERSION = "TSTC_FIXTURE_ENGINE_v003"

@dataclass(frozen=True)
class Transformation:
    transformation_id: str
    domain: str
    predicate: Callable[[dict, dict], bool]
    affected_variables: Tuple[str, ...]
    transition: Callable[[dict, dict], Tuple[dict, dict]]

@dataclass(frozen=True)
class Fixture:
    fixture_id: str
    fixture_version: str
    state: dict
    context: dict
    transformations: Tuple[Transformation, ...]
    intervention_id: str
    intervention: Callable[[dict, dict], Tuple[dict, dict]]
    intervention_variables: Tuple[str, ...]
    negative_control_id: str
    negative_control: Callable[[dict, dict], Tuple[dict, dict]]
    negative_control_variables: Tuple[str, ...]
    baseline_kind: str
    traceability_only: Tuple[str, ...] = ()


def digest(obj):
    return hashlib.sha256(json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str).encode()).hexdigest()


def _state(key, value):
    def op(s, c):
        s, c = deepcopy(s), deepcopy(c); s[key] = value; return s, c
    return op


def _context(key, value):
    def op(s, c):
        s, c = deepcopy(s), deepcopy(c); c[key] = value; return s, c
    return op


def _compose(*ops):
    def op(s, c):
        for fn in ops: s, c = fn(s, c)
        return s, c
    return op


def _noop(s, c): return deepcopy(s), deepcopy(c)


def _c01():
    s={"service":"absent","compute_A":"free","compute_B":"free","routing":"A","security":"normal"}
    c={"sla":"standard","policy_deploy":"allowed","trust_B":"trusted"}
    p={"c01.deploy_A":lambda s,c:s["service"]=="absent" and s["compute_A"]=="free" and c["policy_deploy"]=="allowed" and s["security"]=="normal","c01.deploy_B":lambda s,c:s["service"]=="absent" and s["compute_B"]=="free" and c["policy_deploy"]=="allowed" and c["trust_B"]=="trusted" and s["security"]=="normal","c01.route_A_to_B":lambda s,c:s["service"]=="deployed" and s["routing"]=="A" and s["compute_B"]=="free" and c["trust_B"]=="trusted" and s["security"]=="normal","c01.route_B_to_A":lambda s,c:s["service"]=="deployed" and s["routing"]=="B" and s["compute_A"]=="free" and s["security"]=="normal","c01.restrict_security":lambda s,c:s["security"]=="normal","c01.restore_security":lambda s,c:s["security"]=="restricted"}
    tr={"c01.deploy_A":_compose(_state("service","deployed"),_state("compute_A","occupied")),"c01.deploy_B":_compose(_state("service","deployed"),_state("compute_B","occupied")),"c01.route_A_to_B":_state("routing","B"),"c01.route_B_to_A":_state("routing","A"),"c01.restrict_security":_state("security","restricted"),"c01.restore_security":_state("security","normal")}
    av={"c01.deploy_A":("service","compute_A"),"c01.deploy_B":("service","compute_B"),"c01.route_A_to_B":("routing",),"c01.route_B_to_A":("routing",),"c01.restrict_security":("security",),"c01.restore_security":("security",)}
    ts=tuple(Transformation(n,"C01",p[n],av[n],tr[n]) for n in p)
    return Fixture("FX-C01","003",s,c,ts,"I-C01",_context("trust_B","untrusted"),("trust_B",),"N-C01",_state("routing","B"),("routing",),"finite-state-rule-graph")


def _c03():
    s={"task":"pending","db":"available","repo":"clean"}; c={"permission_db":"granted","permission_repo":"granted","tool_query":"available","tool_pr":"available"}
    p={"c03.query_db":lambda s,c:s["db"]=="available" and c["permission_db"]=="granted" and c["tool_query"]=="available","c03.inspect_repo":lambda s,c:s["repo"] in ("clean","changed") and c["permission_repo"]=="granted","c03.open_pr":lambda s,c:c["permission_repo"]=="granted" and c["tool_pr"]=="available" and s["repo"] in ("clean","changed"),"c03.complete_task":lambda s,c:s["task"]=="pending","c03.modify_repo":lambda s,c:s["repo"]=="clean" and c["permission_repo"]=="granted"}
    av={"c03.query_db":(),"c03.inspect_repo":(),"c03.open_pr":(),"c03.complete_task":(),"c03.modify_repo":("repo",)}
    tr={"c03.query_db":_noop,"c03.inspect_repo":_noop,"c03.open_pr":_noop,"c03.complete_task":_state("task","completed"),"c03.modify_repo":_state("repo","changed")}
    ts=tuple(Transformation(n,"C03",p[n],av[n],tr[n]) for n in p)
    return Fixture("FX-C03","003",s,c,ts,"I-C03",_context("permission_repo","denied"),("permission_repo",),"N-C03",_context("tool_query","available"),("tool_query",),"capability-permission-matrix-workflow")


def _c05():
    s={"grid_capacity":"high","site_A":"available","site_B":"available","ev_A":"waiting","ev_B":"waiting"}; c={"mobility_requirement_A":"normal","mobility_requirement_B":"normal","charger_A":"V1G","charger_B":"V1G"}
    p={"c05.start_A":lambda s,c:s["site_A"]=="available" and s["grid_capacity"]=="high" and s["ev_A"]=="waiting","c05.start_B":lambda s,c:s["site_B"]=="available" and s["grid_capacity"]=="high" and s["ev_B"]=="waiting","c05.defer_A":lambda s,c:s["ev_A"]=="waiting","c05.defer_B":lambda s,c:s["ev_B"]=="waiting","c05.redirect_A_to_B":lambda s,c:s["ev_A"]=="waiting" and s["site_B"]=="available" and c["mobility_requirement_A"]!="urgent","c05.reduce_power_A":lambda s,c:s["ev_A"]=="charging" and c["charger_A"] in ("V1G","V2G")}
    av={"c05.start_A":("ev_A",),"c05.start_B":("ev_B",),"c05.defer_A":(),"c05.defer_B":(),"c05.redirect_A_to_B":(),"c05.reduce_power_A":()}
    tr={"c05.start_A":_state("ev_A","charging"),"c05.start_B":_state("ev_B","charging"),"c05.defer_A":_noop,"c05.defer_B":_noop,"c05.redirect_A_to_B":_noop,"c05.reduce_power_A":_noop}
    ts=tuple(Transformation(n,"C05",p[n],av[n],tr[n]) for n in p)
    return Fixture("FX-C05","003",s,c,ts,"I-C05",_state("grid_capacity","low"),("grid_capacity",),"N-C05",_context("mobility_requirement_A","normal"),("mobility_requirement_A",),"finite-constrained-feasibility")


def fixtures(): return (_c01(), _c03(), _c05())


def tacc(f, state=None, context=None):
    state=f.state if state is None else state; context=f.context if context is None else context
    out=[]; traces={}
    for t in f.transformations:
        ok=bool(t.predicate(state,context)); traces[t.transformation_id]={"admissible":ok,"domain":t.domain}
        if ok: out.append(t.transformation_id)
    return tuple(out), traces


def _changed(before, after):
    s0,c0=before; s1,c1=after; out=[]
    for k in set(s0)|set(s1):
        if s0.get(k)!=s1.get(k): out.append(k)
    for k in set(c0)|set(c1):
        if c0.get(k)!=c1.get(k): out.append(k)
    return tuple(sorted(out))


def apply_checked(f, operation, allowed):
    before=(deepcopy(f.state),deepcopy(f.context)); after=operation(*before)
    changed=_changed(before,after); unexpected=set(changed)-set(allowed)
    assert not unexpected, f"undeclared mutation: {sorted(unexpected)}"
    return after, changed


def preflight_fixture(f):
    ids=tuple(t.transformation_id for t in f.transformations)
    assert len(ids)==len(set(ids))
    assert set(f.traceability_only).isdisjoint(ids)
    t0,_=tacc(f); assert set(t0)<=set(ids)
    for t in f.transformations: assert t.affected_variables is not None
    after,changed=apply_checked(f,f.intervention,f.intervention_variables); t1,_=tacc(f,*after)
    neg_after,neg_changed=apply_checked(f,f.negative_control,f.negative_control_variables); nt,_=tacc(f,*neg_after)
    assert set(nt)==set(t0), f"negative control changed T_acc: {set(t0)^set(nt)}"
    manifest={"fixture_id":f.fixture_id,"fixture_version":f.fixture_version,"state":f.state,"context":f.context,"U_tau":ids,"traceability_only":f.traceability_only,"baseline":f.baseline_kind}
    return {"status":"PREFLIGHT_PASS","fixture":manifest,"T_acc_0":t0,"T_acc_1":t1,"intervention_changed":changed,"negative_control_changed":neg_changed,"negative_control_delta":tuple(sorted(set(nt)^set(t0))),"ruleset_hash":digest(manifest),"output_hash":digest({"manifest":manifest,"t0":t0,"t1":t1})}


def run_preflight():
    rs=[preflight_fixture(f) for f in fixtures()]
    return {"engine_version":VERSION,"mode":"PREFLIGHT_ONLY","results":rs}

if __name__=="__main__": print(json.dumps(run_preflight(),sort_keys=True,indent=2))
