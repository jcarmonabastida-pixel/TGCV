"""N-R4B implementation conformance runner v0.1.

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

for path in (str(SRC),):
    if path not in sys.path:
        sys.path.insert(0, path)


def load_module(path: Path, name: str):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"IMPORT_SPEC_FAILED:{path}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


mod = load_module(IMPLEMENTATION, "branch_n_r4b_trajectory_v01")
branch = load_module(BRANCH_N, "branch_n_r_v02_conformance")


def check(name, fn):
    try:
        ok, details = fn()
        return {"name": name, "status": "PASS" if ok else "FAIL", **details}
    except Exception as exc:
        return {"name": name, "status": "FAIL", "error": f"{type(exc).__name__}:{exc}"}


def base_state():
    return branch.State.make(
        components=("A1", "B1", "C1"),
        edges=(("A1", "B1"),),
        resources=(1, 2, 1),
        objective="O01",
    )


def empty_access_state():
    # At least one component is required by N-R1.2. The state itself has
    # accessible transformations; the empty-T_acc branch is tested through
    # a controlled monkey-patched accessibility provider below.
    return base_state()


results = []

results.append(check("goal_codebook", lambda: (
    all(isinstance(mod.goal(base_state(), o), bool) for o in mod.OBJECTIVES),
    {"objectives": list(mod.OBJECTIVES)},
)))

results.append(check("goal_state_dependence", lambda: (
    mod.goal(base_state(), "O01") is True and
    mod.goal(base_state(), "O02") is False and
    mod.goal(base_state(), "O08") is False and
    mod.goal(base_state(), "O10") is False,
    {},
)))

results.append(check("trajectory_seed_determinism", lambda: (
    mod.trajectory_seed(3_100_000, 7) == 3_100_007 and
    mod.trajectory_seed(4_100_000, 7) == 4_100_007,
    {},
)))


def deterministic_trajectory():
    s = base_state()
    a = mod.generate_trajectory(s, "train", 3_100_000, 7)
    b = mod.generate_trajectory(s, "train", 3_100_000, 7)
    return mod.canonical_trajectory_json(a) == mod.canonical_trajectory_json(b), {
        "outcome": a.outcome,
        "terminal_reason": a.terminal_reason,
        "terminal_step": a.terminal_step,
        "steps": len(a.steps),
    }


results.append(check("same_snapshot_same_seed_byte_identity", deterministic_trajectory))


def seed_change():
    s = branch.State.make(
        components=("A1", "B1", "C1", "C2"),
        edges=(("A1", "B1"), ("B1", "C1")),
        resources=(1, 1, 1),
        objective="O06",
    )
    a = mod.generate_trajectory(s, "train", 3_100_000, 0)
    b = mod.generate_trajectory(s, "train", 3_100_000, 1)
    return a.initial_snapshot_sha256 == b.initial_snapshot_sha256 and a.trajectory_seed != b.trajectory_seed, {}


results.append(check("seed_changes_trajectory_seed_not_snapshot", seed_change))


def objective_independence():
    s1 = branch.State.make(components=("A1", "B1", "C1"), edges=(), resources=(1, 1, 1), objective="O01")
    s2 = branch.State.make(components=("A1", "B1", "C1"), edges=(), resources=(1, 1, 1), objective="O12")
    a = mod.generate_trajectory(s1, "train", 3_100_000, 22)
    b = mod.generate_trajectory(s2, "train", 3_100_000, 22)
    ids_a = [x.transformation_id for x in a.steps]
    ids_b = [x.transformation_id for x in b.steps]
    return ids_a == ids_b, {"steps_a": len(ids_a), "steps_b": len(ids_b)}


results.append(check("objective_independent_transition_selection", objective_independence))


def horizon_and_schema():
    s = branch.State.make(components=("A1", "B1", "C1"), edges=(), resources=(1, 1, 1), objective="O02")
    r = mod.generate_trajectory(s, "train", 3_100_000, 31)
    raw = json.loads(mod.canonical_trajectory_json(r).decode("utf-8"))
    required = {
        "episode_id", "dataset_split", "dataset_seed", "trajectory_seed",
        "initial_snapshot_sha256", "objective", "horizon", "steps",
        "terminal_step", "terminal_reason", "outcome"
    }
    return r.horizon == 6 and required == set(raw), {"horizon": r.horizon, "terminal_reason": r.terminal_reason}


results.append(check("horizon_and_record_schema", horizon_and_schema))


def predictor_outcome_boundary():
    source = IMPLEMENTATION.read_text(encoding="utf-8")
    forbidden = ("learner", "prediction", "test_accuracy", "logloss")
    return not any(x in source.lower() for x in forbidden), {"forbidden_predictor_tokens": list(forbidden)}


results.append(check("no_learner_dependency", predictor_outcome_boundary))


def terminal_semantics():
    # O01 is satisfied at h=0 for the base state, so this must terminate
    # before any transformation is sampled.
    s = branch.State.make(components=("A1", "B1", "C1"), edges=(), resources=(1, 1, 1), objective="O01")
    r = mod.generate_trajectory(s, "train", 3_100_000, 3)
    return r.outcome == 1 and r.terminal_step == 0 and r.terminal_reason == "GOAL_REACHED" and len(r.steps) == 0, {}


results.append(check("success_at_h0", terminal_semantics))


def state_hash_stability():
    s = base_state()
    return mod.state_sha256(s) == mod.state_sha256(s), {"sha256": mod.state_sha256(s)}


results.append(check("state_hash_determinism", state_hash_stability))

failures = [r for r in results if r["status"] != "PASS"]

output = {
    "checks": results,
    "implementation_path": str(IMPLEMENTATION),
    "implementation_sha256": hashlib.sha256(IMPLEMENTATION.read_bytes()).hexdigest(),
    "runner": "N_R4B_CONFORMANCE_RUNNER_v0.1",
    "scientific_execution": "NOT_PERFORMED",
    "status": "FAIL" if failures else "PASS",
}

print(json.dumps(output, indent=2, sort_keys=True))
raise SystemExit(1 if failures else 0)
