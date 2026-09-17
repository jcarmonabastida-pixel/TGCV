"""TGCV WP2 TSTC deterministic synthetic fixture engine v001.

Preflight/conformance only. No external datasets, outcomes, sampling, network,
or scientific interpretation are permitted by this module.
"""
from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass, asdict
import hashlib
import json
from typing import Callable, Dict, List, Tuple


VERSION = "TSTC_FIXTURE_ENGINE_v001"


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
    declared_intervention_variables: Tuple[str, ...]
    negative_control_id: str
    negative_control: Callable[[dict, dict], Tuple[dict, dict]]
    baseline_kind: str


def _canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), default=str)


def digest(obj):
    return hashlib.sha256(_canon(obj).encode()).hexdigest()


def _replace_context(key, value):
    def op(s, c):
        s, c = deepcopy(s), deepcopy(c)
        c[key] = value
        return s, c
    return op


def _replace_state(key, value):
    def op(s, c):
        s, c = deepcopy(s), deepcopy(c)
        s[key] = value
        return s, c
    return op


def _noop(s, c):
    return deepcopy(s), deepcopy(c)


def _c01():
    s = {"service":"absent", "compute_A":"free", "compute_B":"free", "routing":"A", "security":"normal"}
    c = {"sla":"standard", "policy_deploy":"allowed", "trust_B":"trusted"}
    def pred(name):
        return {
            "c01.deploy_A": lambda s,c: s["service"]=="absent" and s["compute_A"]=="free" and c["policy_deploy"]=="allowed" and s["security"]=="normal",
            "c01.deploy_B": lambda s,c: s["service"]=="absent" and s["compute_B"]=="free" and c["policy_deploy"]=="allowed" and c["trust_B"]=="trusted" and s["security"]=="normal",
            "c01.route_A_to_B": lambda s,c: s["service"]=="deployed" and s["routing"]=="A" and s["compute_B"]=="free" and c["trust_B"]=="trusted" and s["security"]=="normal",
            "c01.route_B_to_A": lambda s,c: s["service"]=="deployed" and s["routing"]=="B" and s["compute_A"]=="free" and s["security"]=="normal",
            "c01.restrict_security": lambda s,c: s["security"]=="normal",
            "c01.restore_security": lambda s,c: s["security"]=="restricted",
        }[name]
    def trans(name):
        def op(s,c):
            s,c=deepcopy(s),deepcopy(c)
            if name=="c01.deploy_A": s["service"],s["compute_A"]="deployed","occupied"
            elif name=="c01.deploy_B": s["service"],s["compute_B"]="deployed","occupied"
            elif name=="c01.route_A_to_B": s["routing"]="B"
            elif name=="c01.route_B_to_A": s["routing"]="A"
            elif name=="c01.restrict_security": s["security"]="restricted"
            elif name=="c01.restore_security": s["security"]="normal"
            return s,c
        return op
    names=("c01.deploy_A","c01.deploy_B","c01.route_A_to_B","c01.route_B_to_A","c01.restrict_security","c01.restore_security")
    ts=tuple(Transformation(n,"C01",pred(n),(),trans(n)) for n in names)
    return Fixture("FX-C01","001",s,c,ts,"I-C01",_replace_context("trust_B","untrusted"),("trust_B",),"N-C01",_replace_state("routing","B"),"finite-state-rule-graph")


def _c03():
    s={"task":"pending","db":"available","repo":"clean"}
    c={"permission_db":"granted","permission_repo":"granted","tool_query":"available","tool_pr":"available"}
    p={
      "c03.query_db":lambda s,c:s["db"]=="available" and c["permission_db"]=="granted" and c["tool_query"]=="available",
      "c03.inspect_repo":lambda s,c:s["repo"] in ("clean","changed") and c["permission_repo"]=="granted",
      "c03.open_pr":lambda s,c:c["permission_repo"]=="granted" and c["tool_pr"]=="available" and s["repo"] in ("clean","changed"),
      "c03.complete_task":lambda s,c:s["task"]=="pending",
    }
    names=tuple(p)
    ts=tuple(Transformation(n,"C03",p[n],(),_noop) for n in names)
    return Fixture("FX-C03","001",s,c,ts,"I-C03",_replace_context("permission_repo","denied"),("permission_repo",),"N-C03",_replace_context("tool_query","available"),"capability-permission-matrix-workflow")


def _c05():
    s={"grid_capacity":"high","site_A":"available","site_B":"available","ev_A":"waiting","ev_B":"waiting"}
    c={"mobility_requirement_A":"normal","mobility_requirement_B":"normal","charger_A":"V1G","charger_B":"V1G"}
    p={
      "c05.start_A":lambda s,c:s["site_A"]=="available" and s["grid_capacity"]=="high" and s["ev_A"]=="waiting",
      "c05.start_B":lambda s,c:s["site_B"]=="available" and s["grid_capacity"]=="high" and s["ev_B"]=="waiting",
      "c05.defer_A":lambda s,c:s["ev_A"]=="waiting",
      "c05.defer_B":lambda s,c:s["ev_B"]=="waiting",
      "c05.redirect_A_to_B":lambda s,c:s["ev_A"]=="waiting" and s["site_B"]=="available" and c["mobility_requirement_A"]!="urgent",
      "c05.reduce_power_A":lambda s,c:s["ev_A"]=="charging" and c["charger_A"] in ("V1G","V2G"),
    }
    ts=tuple(Transformation(n,"C05",p[n],(),_noop) for n in p)
    return Fixture("FX-C05","001",s,c,ts,"I-C05",_replace_state("grid_capacity","low"),("grid_capacity",),"N-C05",_replace_context("mobility_requirement_A","normal"),"finite-constrained-feasibility")


def fixtures():
    return (_c01(), _c03(), _c05())


def tacc(fixture, state=None, context=None):
    state=fixture.state if state is None else state
    context=fixture.context if context is None else context
    out=[]
    traces={}
    for t in fixture.transformations:
        result=bool(t.predicate(state,context))
        traces[t.transformation_id]={"admissible":result,"domain":t.domain}
        if result: out.append(t.transformation_id)
    return tuple(out), traces


def apply_checked(state, context, operation, allowed_variables):
    before=(deepcopy(state),deepcopy(context))
    after=operation(state,context)
    if not isinstance(after,tuple) or len(after)!=2:
        raise AssertionError("transition must return (state, context)")
    s1,c1=after
    changed=[]
    for k in set(before[0])|set(s1):
        if before[0].get(k)!=s1.get(k): changed.append(k)
    for k in set(before[1])|set(c1):
        if before[1].get(k)!=c1.get(k): changed.append(k)
    if set(changed)-set(allowed_variables):
        raise AssertionError(f"undeclared mutation: {sorted(set(changed)-set(allowed_variables))}")
    return s1,c1,tuple(sorted(changed))


def fixture_manifest(f):
    return {"fixture_id":f.fixture_id,"fixture_version":f.fixture_version,"state":f.state,"context":f.context,
            "transformation_universe":[t.transformation_id for t in f.transformations],"intervention_id":f.intervention_id,
            "negative_control_id":f.negative_control_id,"baseline":f.baseline_kind}


def preflight_fixture(f):
    manifest=fixture_manifest(f)
    assert len(manifest["transformation_universe"])==len(set(manifest["transformation_universe"]))
    t0,tr0=tacc(f)
    assert set(t0)<=set(manifest["transformation_universe"])
    for t in f.transformations:
        assert bool(t.predicate(f.state,f.context))==(t.transformation_id in t0)
    s1,c1,changed=apply_checked(f.state,f.context,f.intervention,f.declared_intervention_variables)
    t1,_=tacc(f,s1,c1)
    delta=(tuple(sorted(set(t1)-set(t0))),tuple(sorted(set(t0)-set(t1))))
    ns,nc,nchanged=apply_checked(f.state,f.context,f.negative_control,tuple(k for k in f.state if False) + tuple(k for k in f.context if False))
    # Identity-preserving negative controls must not mutate state/context.
    assert not nchanged
    nt,_=tacc(f,ns,nc)
    assert set(nt)==set(t0)
    repeat=tacc(f)[0]
    assert repeat==t0
    return {"status":"PREFLIGHT_PASS","fixture":manifest,"T_acc_0":t0,"T_acc_1":t1,
            "delta_T_acc":{"opened":delta[0],"closed":delta[1]},"intervention_changed":changed,
            "negative_control_delta":tuple(sorted(set(nt)^set(t0))),"ruleset_hash":digest(manifest),
            "output_hash":digest({"fixture":manifest,"t0":t0,"t1":t1})}


def run_preflight():
    # Hard firewall: this module has no imports for datasets/network/randomness.
    results=[preflight_fixture(f) for f in fixtures()]
    return {"engine_version":VERSION,"mode":"PREFLIGHT_ONLY","results":results}


if __name__ == "__main__":
    print(json.dumps(run_preflight(),sort_keys=True,indent=2))
