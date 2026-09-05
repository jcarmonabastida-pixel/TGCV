"""N-R4B implementation conformance runner v0.3.

Conformance only. No scientific corpus generation or learner fitting.
"""

from __future__ import annotations

import hashlib
import importlib.util
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SRC = ROOT / "03_EXPERIMENTS" / "EMP-1.1" / "src"
IMPLEMENTATION = SRC / "branch_n_r4b_trajectory_v01.py"
BRANCH_N = SRC / "branch_n_r_v02.py"
if str(SRC) not in sys.path:
    sys.path.insert(0, str(SRC))


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"IMPORT_SPEC_FAILED:{path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


branch = load_module(BRANCH_N, "branch_n_r_v02")
mod = load_module(IMPLEMENTATION, "branch_n_r4b_trajectory_v01")


def check(name, fn):
    try:
        ok, details = fn()
        return {"name": name, "status": "PASS" if ok else "FAIL", **details}
    except Exception as exc:
        return {"name": name, "status": "FAIL", "error": f"{type(exc).__name__}:{exc}"}


def make_state(objective="O01", resources=(1, 1, 1), components=("A1", "B1", "C1"), edges=()):
    return branch.State.make(components=components, edges=edges, resources=resources, objective=objective)


results = []
results.append(check("goal_codebook", lambda: (
    all(isinstance(mod.goal(make_state(), o), bool) for o in mod.OBJECTIVES),
    {"objectives": list(mod.OBJECTIVES)},
)))
results.append(check("goal_state_dependence", lambda: (
    mod.goal(make_state("O01"), "O01") is True and
    mod.goal(make_state("O02"), "O02") is False and
    mod.goal(make_state("O08"), "O08") is False and
    mod.goal(make_state("O10"), "O10") is False,
    {},
)))
results.append(check("trajectory_seed_determinism", lambda: (
    mod.trajectory_seed(3_100_000, 7) == 3_100_007 and
    mod.trajectory_seed(4_100_000, 7) == 4_100_007,
    {},
)))


def deterministic_trajectory():
    s = make_state("O02")
    a = mod.generate_trajectory(s, "train", 3_100_000, 7)
    b = mod.generate_trajectory(s, "train", 3_100_000, 7)
    return mod.canonical_trajectory_json(a) == mod.canonical_trajectory_json(b), {
        "outcome": a.outcome, "terminal_reason": a.terminal_reason,
        "terminal_step": a.terminal_step, "steps": len(a.steps),
    }
results.append(check("same_snapshot_same_seed_byte_identity", deterministic_trajectory))


def seed_change():
    s = make_state("O06", components=("A1", "B1", "C1", "C2"), edges=(("A1", "B1"), ("B1", "C1")))
    a = mod.generate_trajectory(s, "train", 3_100_000, 0)
    b = mod.generate_trajectory(s, "train", 3_100_000, 1)
    return a.initial_snapshot_sha256 == b.initial_snapshot_sha256 and a.trajectory_seed != b.trajectory_seed, {}
results.append(check("seed_changes_trajectory_seed_not_snapshot", seed_change))


def objective_independence():
    s1 = make_state("O01")
    s2 = make_state("O12")
    original_goal = mod.goal
    mod.goal = lambda state, objective: False
    try:
        a = mod.generate_trajectory(s1, "train", 3_100_000, 22)
        b = mod.generate_trajectory(s2, "train", 3_100_000, 22)
    finally:
        mod.goal = original_goal
    ids_a = [x.transformation_id for x in a.steps]
    ids_b = [x.transformation_id for x in b.steps]
    return ids_a == ids_b and len(ids_a) == 6 and len(ids_b) == 6, {"steps_a": len(ids_a), "steps_b": len(ids_b)}
results.append(check("objective_independent_transition_selection", objective_independence))


def empty_tacc():
    s = make_state("O12")
    original_enum = mod.enumerate_transformations
    mod.enumerate_transformations = lambda state: tuple()
    try:
        r = mod.generate_trajectory(s, "train", 3_100_000, 41)
    finally:
        mod.enumerate_transformations = original_enum
    return r.outcome == 0 and r.terminal_step == 0 and r.terminal_reason == "NO_ACCESSIBLE_TRANSFORMATION" and len(r.steps) == 0, {
        "terminal_reason": r.terminal_reason, "terminal_step": r.terminal_step, "steps": len(r.steps)
    }
results.append(check("empty_tacc_terminal_semantics", empty_tacc))


def duplicate_successor_selection():
    # Two distinct transformation identities are mapped to the same successor.
    # Sampling must remain over transformation entries, not deduplicated successors.
    s = make_state("O12")
    t1 = ("FIXTURE_TRANSFORMATION_A",)
    t2 = ("FIXTURE_TRANSFORMATION_B",)
    tacc = (t1, t2)
    original_enum = mod.enumerate_transformations
    original_apply = mod.apply_transformation
    original_goal = mod.goal
    mod.enumerate_transformations = lambda state: tacc
    mod.apply_transformation = lambda state, selected: state
    mod.goal = lambda state, objective: False
    try:
        selected_ids = []
        for episode_id in range(60, 92):
            r = mod.generate_trajectory(s, "train", 3_100_000, episode_id)
            selected_ids.extend(x.transformation_id for x in r.steps)
    finally:
        mod.enumerate_transformations = original_enum
        mod.apply_transformation = original_apply
        mod.goal = original_goal
    observed = set(selected_ids)
    return observed == {repr(t1), repr(t2)}, {"distinct_transformation_ids_observed": sorted(observed), "episodes": 32}
results.append(check("duplicate_successor_transformations_remain_selectable", duplicate_successor_selection))


def success_after_step():
    s = make_state("O02")
    forced = (("ADD_COMPONENT", "A2"),)
    original_enum = mod.enumerate_transformations
    mod.enumerate_transformations = lambda state: forced
    try:
        r = mod.generate_trajectory(s, "train", 3_100_000, 103)
    finally:
        mod.enumerate_transformations = original_enum
    return r.outcome == 1 and r.terminal_step == 1 and r.terminal_reason == "GOAL_REACHED" and len(r.steps) == 1, {
        "terminal_step": r.terminal_step, "terminal_reason": r.terminal_reason, "steps": len(r.steps)
    }
results.append(check("success_after_one_or_more_steps", success_after_step))


def horizon_and_schema():
    s = make_state("O02")
    original_goal = mod.goal
    mod.goal = lambda state, objective: False
    try:
        r = mod.generate_trajectory(s, "train", 3_100_000, 31)
    finally:
        mod.goal = original_goal
    raw = json.loads(mod.canonical_trajectory_json(r).decode("utf-8"))
    required = {"episode_id", "dataset_split", "dataset_seed", "trajectory_seed", "initial_snapshot_sha256", "objective", "horizon", "steps", "terminal_step", "terminal_reason", "outcome"}
    return r.horizon == 6 and required == set(raw) and r.terminal_reason == "HORIZON_EXHAUSTED" and r.terminal_step == 6 and len(r.steps) == 6, {"horizon": r.horizon, "terminal_reason": r.terminal_reason}
results.append(check("horizon_and_record_schema", horizon_and_schema))


def predictor_outcome_boundary():
    source = IMPLEMENTATION.read_text(encoding="utf-8")
    forbidden = ("learner", "prediction", "test_accuracy", "logloss")
    return not any(x in source.lower() for x in forbidden), {"forbidden_predictor_tokens": list(forbidden)}
results.append(check("no_learner_dependency", predictor_outcome_boundary))


def success_at_h0():
    s = make_state("O01")
    r = mod.generate_trajectory(s, "train", 3_100_000, 3)
    return r.outcome == 1 and r.terminal_step == 0 and r.terminal_reason == "GOAL_REACHED" and len(r.steps) == 0, {}
results.append(check("success_at_h0", success_at_h0))


def state_hash_stability():
    s = make_state("O01")
    return mod.state_sha256(s) == mod.state_sha256(s), {"sha256": mod.state_sha256(s)}
results.append(check("state_hash_determinism", state_hash_stability))

failures = [r for r in results if r["status"] != "PASS"]
output = {
    "checks": results,
    "implementation_path": str(IMPLEMENTATION),
    "implementation_sha256": hashlib.sha256(IMPLEMENTATION.read_bytes()).hexdigest(),
    "runner": "N_R4B_CONFORMANCE_RUNNER_v0.3",
    "scientific_execution": "NOT_PERFORMED",
    "status": "FAIL" if failures else "PASS",
}
print(json.dumps(output, indent=2, sort_keys=True))
raise SystemExit(1 if failures else 0)
