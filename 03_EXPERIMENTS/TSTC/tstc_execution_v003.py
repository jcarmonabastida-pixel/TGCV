"""TGCV WP2 TSTC bounded execution adapter v003.

Authorized synthetic execution path for Fixture-003.

This module implements the minimum demonstrator execution boundary only:
fixture -> T_acc,0 -> declared transition/intervention -> T_acc,1 ->
Delta T_acc -> bounded admissible trajectory -> explicit cross-domain
propagation -> baseline reconstruction -> qualitative representation comparison.

No real datasets, network access, predictive modelling, downstream outcomes,
causal inference, value analysis, ROI, or industrial validation are permitted.
The module does not execute on import; run_execution() must be called
explicitly.
"""
from __future__ import annotations

import hashlib
import json
import platform
import subprocess
import sys
from copy import deepcopy
from dataclasses import dataclass
from typing import Tuple

from tstc_fixture_engine_v003 import fixtures, tacc, digest

EXECUTION_VERSION = "TSTC_EXECUTION_v003"
FIXTURE_VERSION = "003"

COUPLING_RULES = (
    {"source_connector": "C01", "source_condition": {"security": "restricted"},
     "target_connector": "C03", "target_condition": {"permission_repo": "denied"},
     "transition": "propagate"},
    {"source_connector": "C03", "source_condition": {"repo": "changed"},
     "target_connector": "C05", "target_condition": {"mobility_requirement_A": "urgent"},
     "transition": "propagate"},
)

@dataclass(frozen=True)
class TransitionRecord:
    intervention_id: str
    changed_variables: Tuple[str, ...]
    S_before: dict
    C_before: dict
    S_after: dict
    C_after: dict


def _fixture_by_id(items, fixture_id):
    return next(f for f in items if f.fixture_id == fixture_id)


def _find_transformation(fixture, transformation_id):
    return next(t for t in fixture.transformations if t.transformation_id == transformation_id)


def _changed(before, after):
    s0, c0 = before; s1, c1 = after
    return tuple(sorted([k for k in set(s0) | set(s1) if s0.get(k) != s1.get(k)] +
                        [k for k in set(c0) | set(c1) if c0.get(k) != c1.get(k)]))


def _apply(fixture, operation, allowed_variables, label):
    before = (deepcopy(fixture.state), deepcopy(fixture.context))
    after = operation(*before)
    changed = _changed(before, after)
    assert not (set(changed) - set(allowed_variables)), f"{label}: undeclared mutation"
    return before, after, changed


def _transition(fixture, transformation_id, state, context):
    transformation = _find_transformation(fixture, transformation_id)
    assert transformation.predicate(state, context), f"inaccessible transformation used: {transformation_id}"
    before = (deepcopy(state), deepcopy(context))
    after = transformation.transition(*before)
    changed = _changed(before, after)
    assert not (set(changed) - set(transformation.affected_variables)), f"{transformation_id}: undeclared mutation"
    return before, after, changed


def _delta(t0, t1):
    a, b = set(t0), set(t1)
    return {"opened": tuple(sorted(b-a)), "closed": tuple(sorted(a-b)),
            "persistent": tuple(sorted(a&b)), "changed": tuple(sorted((a-b)|(b-a)))}


def _bounded_trajectory(fixture, state, context):
    """Record one bounded step using only a transformation admissible now."""
    admissible, _ = tacc(fixture, state, context)
    assert admissible
    tid = admissible[0]
    before, after, changed = _transition(fixture, tid, state, context)
    return [{"step": 0, "transformation_id": tid, "S_before": before[0],
             "C_before": before[1], "S_after": after[0], "C_after": after[1],
             "changed_variables": changed}]


def _baseline_representation(fixture, state, context):
    admissible, _ = tacc(fixture, state, context)
    if fixture.fixture_id == "FX-C01":
        kind = "finite-state-rule-graph"
    elif fixture.fixture_id == "FX-C03":
        kind = "capability-permission-matrix-workflow"
    else:
        kind = "finite-constrained-feasibility"
    return {"representation": kind, "state": deepcopy(state), "context": deepcopy(context),
            "feasible_actions": admissible}


def _baseline_compare(tgcv_before, tgcv_after, baseline_before, baseline_after):
    if tuple(tgcv_before) == tuple(baseline_before) and tuple(tgcv_after) == tuple(baseline_after):
        return {"category": "EQUIVALENT_REPRESENTATION",
                "observations": ["Baseline reconstructs the same admissible transformation sets under the same frozen state/context information."]}
    return {"category": "INCONCLUSIVE", "observations": ["The bounded comparison did not establish information parity."]}


def _assert_fixture_versions(fs):
    assert {f.fixture_id: f.fixture_version for f in fs} == {"FX-C01": "003", "FX-C03": "003", "FX-C05": "003"}


def _assert_frozen_universes(fs):
    expected = {
        "FX-C01": ("c01.deploy_A","c01.deploy_B","c01.route_A_to_B","c01.route_B_to_A","c01.restrict_security","c01.restore_security"),
        "FX-C03": ("c03.query_db","c03.inspect_repo","c03.open_pr","c03.complete_task","c03.modify_repo"),
        "FX-C05": ("c05.start_A","c05.start_B","c05.defer_A","c05.defer_B","c05.redirect_A_to_B","c05.reduce_power_A"),
    }
    for f in fs:
        assert tuple(t.transformation_id for t in f.transformations) == expected[f.fixture_id]


def _run_local_positive(fixture):
    t0, _ = tacc(fixture)
    before, after, changed = _apply(fixture, fixture.intervention, fixture.intervention_variables, "positive intervention")
    t1, _ = tacc(fixture, *after)
    return {"intervention_id": fixture.intervention_id, "S0": before[0], "C0": before[1],
            "S1": after[0], "C1": after[1], "changed_variables": changed,
            "T_acc_0": t0, "T_acc_1": t1, "Delta_T_acc": _delta(t0,t1),
            "trajectory": _bounded_trajectory(fixture, *after),
            "baseline_before": _baseline_representation(fixture,*before),
            "baseline_after": _baseline_representation(fixture,*after)}


def _run_negative_control(fixture):
    t0, _ = tacc(fixture)
    before, after, changed = _apply(fixture, fixture.negative_control, fixture.negative_control_variables, "negative control")
    t1, _ = tacc(fixture, *after)
    delta = _delta(t0,t1)
    assert delta["opened"] == () and delta["closed"] == () and delta["changed"] == ()
    return {"negative_control_id": fixture.negative_control_id, "changed_variables": changed,
            "T_acc_0": t0, "T_acc_1": t1, "Delta_T_acc": delta}


def _cross_domain_scenario_c01_to_c03(c01, c03):
    # It does not execute C03.modify_repo.
    assert c03.context["permission_repo"] == "granted"
    t0, _ = tacc(c01)
    _, after_c01, changed = _apply(c01, _find_transformation(c01,"c01.restrict_security").transition,
                                   ("security",), "C01 restriction")
    t1, _ = tacc(c01, *after_c01)
    propagated_context = deepcopy(c03.context)
    propagated_context["permission_repo"] = "denied"
    c03_t0, _ = tacc(c03)
    c03_t1, _ = tacc(c03, c03.state, propagated_context)
    assert "c03.modify_repo" in c03_t0 and "c03.modify_repo" not in c03_t1
    # Guard: the denied target scenario must never invoke the repo mutation.
    assert propagated_context["permission_repo"] == "denied"
    return {"scenario_id":"CD-C01-C03-001",
            "source":{"connector":"C01","changed_variables":changed,"S_after":after_c01[0],"C_after":after_c01[1],"T_acc_before":t0,"T_acc_after":t1},
            "propagation":{"rule":COUPLING_RULES[0],"target_context_before":deepcopy(c03.context),"target_context_after":propagated_context,
                            "T_acc_before":c03_t0,"T_acc_after":c03_t1,"Delta_T_acc":_delta(c03_t0,c03_t1)},
            "non_claim":"synthetic rule propagation, not empirical causality"}


def _cross_domain_scenario_c03_to_c05(c03, c05):
    # Scenario B is independent from Scenario A and starts from a fresh C03 state/context.
    assert c03.context["permission_repo"] == "granted" and c03.state["repo"] == "clean"
    before, after, changed = _transition(c03,"c03.modify_repo",c03.state,c03.context)
    assert changed == ("repo",)
    t0, _ = tacc(c03,*before); t1, _ = tacc(c03,*after)
    propagated_context = deepcopy(c05.context)
    propagated_context["mobility_requirement_A"] = "urgent"
    c05_t0, _ = tacc(c05); c05_t1, _ = tacc(c05,c05.state,propagated_context)
    assert "c05.redirect_A_to_B" in c05_t0 and "c05.redirect_A_to_B" not in c05_t1
    return {"scenario_id":"CD-C03-C05-001",
            "source":{"connector":"C03","transition":"c03.modify_repo","S_before":before[0],"C_before":before[1],"S_after":after[0],"C_after":after[1],"changed_variables":changed,"T_acc_before":t0,"T_acc_after":t1,"Delta_T_acc":_delta(t0,t1)},
            "propagation":{"rule":COUPLING_RULES[1],"target_context_before":deepcopy(c05.context),"target_context_after":propagated_context,"T_acc_before":c05_t0,"T_acc_after":c05_t1,"Delta_T_acc":_delta(c05_t0,c05_t1)},
            "non_claim":"synthetic rule propagation, not empirical causality"}


def _source_commit():
    try:
        return subprocess.check_output(["git","rev-parse","HEAD"],stderr=subprocess.DEVNULL,text=True).strip()
    except Exception as exc:
        raise RuntimeError("source_commit unavailable; execution must fail closed") from exc


def _metadata(fs, output, source_commit):
    manifest = {f.fixture_id:{"fixture_version":f.fixture_version,"state":f.state,"context":f.context,
                              "U_tau":tuple(t.transformation_id for t in f.transformations),"baseline":f.baseline_kind} for f in fs}
    return {"execution_version":EXECUTION_VERSION,"fixture_version":FIXTURE_VERSION,"source_commit":source_commit,
            "fixture_manifest_hash":digest(manifest),"ruleset_hash":digest(COUPLING_RULES),
            "transformation_universe_hash":digest({k:v["U_tau"] for k,v in manifest.items()}),
            "configuration_hash":hashlib.sha256(json.dumps({"execution_version":EXECUTION_VERSION,"fixture_version":FIXTURE_VERSION},sort_keys=True).encode()).hexdigest(),
            "environment":{"python":sys.version.split()[0],"platform":platform.platform()},"random_seed":None,"output_hash":digest(output)}


def run_execution():
    fs = fixtures(); _assert_fixture_versions(fs); _assert_frozen_universes(fs)
    source_commit = _source_commit()
    c01 = _fixture_by_id(fs,"FX-C01"); c03 = _fixture_by_id(fs,"FX-C03"); c05 = _fixture_by_id(fs,"FX-C05")
    local = {f.fixture_id:{"positive":_run_local_positive(f),"negative_control":_run_negative_control(f)} for f in fs}
    comparisons = {f.fixture_id:_baseline_compare(local[f.fixture_id]["positive"]["T_acc_0"],local[f.fixture_id]["positive"]["T_acc_1"],
                                                   tuple(local[f.fixture_id]["positive"]["baseline_before"]["feasible_actions"]),tuple(local[f.fixture_id]["positive"]["baseline_after"]["feasible_actions"])) for f in fs}
    cross_domain = {"C01_to_C03":_cross_domain_scenario_c01_to_c03(c01,c03),"C03_to_C05":_cross_domain_scenario_c03_to_c05(c03,c05)}
    result = {"status":"TSTC_EXECUTION_COMPLETE","mode":"TSTC_SYNTHETIC_EXECUTION_V003",
              "fixture_versions":{f.fixture_id:f.fixture_version for f in fs},"local_connector_results":local,
              "cross_domain_results":cross_domain,"baseline_comparison":comparisons,
              "limitations":["synthetic bounded demonstrator","no empirical causal inference","no downstream outcome measurement","no value/ROI analysis","no superiority claim","no generality claim"],
              "non_claims":["No scientific validity claim","No empirical causal claim","No superiority claim","No generality claim","No value creation claim","No industrial validation claim"]}
    result["execution_metadata"] = _metadata(fs,result,source_commit)
    return result


if __name__ == "__main__":
    print(json.dumps(run_execution(),sort_keys=True,indent=2,default=list))
