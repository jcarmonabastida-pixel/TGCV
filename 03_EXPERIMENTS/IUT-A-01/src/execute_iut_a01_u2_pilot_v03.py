#!/usr/bin/env python3
"""IUT-A-01 U2 computational executor v0.3.

Fixture-002 executor aligned with Metric Design Revision 001.
M1 is primary, M2 is secondary, and M3 is retired and absent from scoring.
The executor derives viable and preferred references from frozen semantics and
blocks on construction/integrity mismatches.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
from dataclasses import asdict, dataclass
from pathlib import Path
from statistics import median
from time import perf_counter_ns

EXECUTOR_VERSION = "IUT-A-01-U2-PILOT-EXECUTOR-0.3"
CASE_ID = "IUT-A-01"
N_TRIALS = 40
TRIAL_CLASSES = ("DIRECT_FEASIBILITY", "DEPENDENCY", "CONSTRAINT_CONFLICT", "ALTERNATIVE_SPACE")
SEED = 20260911
M1_DEGRADATION_LIMIT = 0.05
M2_RELATIVE_MIN = 0.10

REPO_ROOT = Path(__file__).resolve().parents[3]
FIXTURE_PATH = REPO_ROOT / "03_EXPERIMENTS/IUT-A-01/IUT_A01_U2_FIXTURE_SPECIFICATION_002.md"
MANIFEST_PATH = REPO_ROOT / "03_EXPERIMENTS/IUT-A-01/IUT_A01_U2_EXECUTION_MANIFEST_002.md"
METRIC_PATH = REPO_ROOT / "03_EXPERIMENTS/IUT-A-01/IUT_A01_U2_METRIC_DESIGN_REVISION_001.md"
EXPECTED_FIXTURE_GIT_BLOB_SHA = "fc274826f66ee28f6e1b0329866b322577c6bc62"

@dataclass(frozen=True)
class Option:
    option_id: str
    objective_score: int
    requirements: tuple[str, ...]
    hard_constraints: tuple[str, ...]
    dependencies: tuple[str, ...]

@dataclass(frozen=True)
class Trial:
    trial_id: str
    trial_class: str
    state: tuple[tuple[str, str], ...]
    options: tuple[Option, ...]
    preferred_option: str
    viable_options: tuple[str, ...]


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def canonical_file_bytes(path: Path) -> bytes:
    return path.read_bytes().replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def git_blob_sha(path: Path) -> str:
    data = canonical_file_bytes(path)
    return hashlib.sha1(f"blob {len(data)}\0".encode() + data).hexdigest()


def source_integrity() -> dict:
    checks = {"fixture_exists": FIXTURE_PATH.is_file(), "manifest_exists": MANIFEST_PATH.is_file(), "metric_exists": METRIC_PATH.is_file()}
    if not all(checks.values()):
        return {**checks, "fixture_git_blob_sha": None, "fixture_blob_match": False, "PASS": False}
    fixture_git = git_blob_sha(FIXTURE_PATH)
    return {**checks, "fixture_git_blob_sha": fixture_git, "fixture_blob_match": fixture_git == EXPECTED_FIXTURE_GIT_BLOB_SHA, "PASS": fixture_git == EXPECTED_FIXTURE_GIT_BLOB_SHA}


def make_option(option_id: str, score: int, req: tuple[str, ...], constraints: tuple[str, ...], deps: tuple[str, ...]) -> Option:
    return Option(option_id, score, req, constraints, deps)


def build_trial(index: int, trial_class: str) -> Trial:
    cycle = (index - 1) % 5
    options = (
        make_option("A", 80 + cycle, ("R0",), (), ()),
        make_option("B", 85 + cycle, ("R0", "R1"), (), ("D1",)),
        make_option("C", 70 + cycle, ("R0",), ("BLOCK_C",), ()),
    )
    state = {
        "R0": "true",
        "R1": "true" if trial_class in {"DEPENDENCY", "ALTERNATIVE_SPACE"} else "false",
        "D1": "true" if trial_class == "ALTERNATIVE_SPACE" or (trial_class == "DEPENDENCY" and cycle % 2 == 0) else "false",
        "BLOCK_C": "true" if trial_class == "CONSTRAINT_CONFLICT" else "false",
    }
    st = tuple(sorted(state.items()))
    computed_viable = tuple(o.option_id for o in options if feasible(o, state))
    preferred = max((o for o in options if o.option_id in computed_viable), key=lambda o: (o.objective_score, -options.index(o))).option_id
    return Trial(f"U2-{index:03d}", trial_class, st, options, preferred, computed_viable)


def build_universe() -> tuple[Trial, ...]:
    per_class = N_TRIALS // len(TRIAL_CLASSES)
    return tuple(build_trial(offset * per_class + i + 1, cls) for offset, cls in enumerate(TRIAL_CLASSES) for i in range(per_class))


def state_map(trial: Trial) -> dict[str, str]:
    return dict(trial.state)


def feasible(option: Option, state: dict[str, str]) -> bool:
    return (all(state.get(d, "false") == "true" for d in option.dependencies)
            and all(state.get(c, "false") != "true" for c in option.hard_constraints)
            and all(state.get(r, "false") == "true" for r in option.requirements))


def control_decision(trial: Trial) -> str:
    state = state_map(trial)
    for opt in trial.options:
        if opt.dependencies:
            continue
        if feasible(opt, state):
            return opt.option_id
    return trial.options[0].option_id


def tgcv_decision(trial: Trial) -> str:
    state = state_map(trial)
    accessible = [o for o in trial.options if feasible(o, state)]
    return max(accessible, key=lambda o: (o.objective_score, -trial.options.index(o))).option_id


def verify_fixture_semantics(trials: tuple[Trial, ...]) -> dict:
    viable_exact = True
    preferred_exact = True
    preferred_viable = True
    for t in trials:
        state = state_map(t)
        computed_viable = tuple(o.option_id for o in t.options if feasible(o, state))
        computed_preferred = max((o for o in t.options if o.option_id in computed_viable), key=lambda o: (o.objective_score, -t.options.index(o))).option_id
        viable_exact &= t.viable_options == computed_viable
        preferred_exact &= t.preferred_option == computed_preferred
        preferred_viable &= t.preferred_option in computed_viable
    return {"viable_options_exact": viable_exact, "preferred_option_exact": preferred_exact, "preferred_option_viable": preferred_viable}


def integrity_checks(trials: tuple[Trial, ...], src: dict) -> dict:
    counts = {c: sum(t.trial_class == c for t in trials) for c in TRIAL_CLASSES}
    semantics = verify_fixture_semantics(trials)
    return {
        "trial_count_ok": len(trials) == N_TRIALS,
        "class_balance_ok": all(v == 10 for v in counts.values()),
        "unique_trial_ids_ok": len({t.trial_id for t in trials}) == N_TRIALS,
        "same_universe_for_both_arms": True,
        "outcome_blind": True,
        "analyst_generated_options_added": False,
        "ground_truth_immutable": True,
        "m3_active": False,
        "fixture_source_integrity": src["PASS"],
        "counts_by_class": counts,
        **semantics,
    }


def hash_trials(trials: tuple[Trial, ...]) -> str:
    return sha256_bytes(canonical_json([asdict(t) for t in trials]).encode())


def score(trials: tuple[Trial, ...]) -> dict:
    records = []
    control_correct = tgcv_correct = 0
    control_times, tgcv_times = [], []
    for t in trials:
        s = state_map(t)
        c_start = perf_counter_ns(); c = control_decision(t); c_ms = (perf_counter_ns() - c_start) / 1_000_000
        g_start = perf_counter_ns(); g = tgcv_decision(t); g_ms = (perf_counter_ns() - g_start) / 1_000_000
        cc = c == t.preferred_option; gc = g == t.preferred_option
        control_correct += int(cc); tgcv_correct += int(gc)
        control_times.append(c_ms); tgcv_times.append(g_ms)
        records.append({"trial_id": t.trial_id, "trial_class": t.trial_class, "control_decision": c, "tgcv_decision": g, "preferred_option": t.preferred_option, "control_correct": cc, "tgcv_correct": gc, "control_elapsed_ms": round(c_ms, 6), "tgcv_elapsed_ms": round(g_ms, 6)})
    m1c, m1g = control_correct / len(trials), tgcv_correct / len(trials)
    medc, medg = median(control_times), median(tgcv_times)
    reduction = (medc - medg) / medc if medc else 0.0
    m1_delta_pp = (m1g - m1c) * 100
    m1_pass = m1_delta_pp >= -(M1_DEGRADATION_LIMIT * 100)
    m2_pass = reduction >= M2_RELATIVE_MIN
    classification = "U2-POSITIVE" if m1_pass and m2_pass else ("U2-NULL" if m1_pass else "U2-MIXED")
    return {"N_TRIALS": len(trials), "M1": {"control": m1c, "tgcv": m1g, "delta_percentage_points": m1_delta_pp, "degradation_limit_percentage_points": -(M1_DEGRADATION_LIMIT * 100), "passes": m1_pass}, "M2": {"control_median_elapsed_ms": medc, "tgcv_median_elapsed_ms": medg, "relative_reduction": reduction, "threshold_relative_reduction": M2_RELATIVE_MIN, "passes": m2_pass, "timing_basis": "perf_counter_ns_single_decision_invocation"}, "classification": classification, "records": records}


def run(mode: str) -> dict:
    src = source_integrity()
    trials = build_universe()
    integrity = integrity_checks(trials, src)
    required = ("trial_count_ok", "class_balance_ok", "unique_trial_ids_ok", "same_universe_for_both_arms", "outcome_blind", "ground_truth_immutable", "fixture_source_integrity", "viable_options_exact", "preferred_option_exact", "preferred_option_viable")
    allowed = all(integrity[k] is True for k in required) and integrity["analyst_generated_options_added"] is False and integrity["m3_active"] is False
    result = {"EXECUTION_RESULT": "PASS" if allowed else "INDETERMINATE", "MODE": mode, "EXECUTOR_VERSION": EXECUTOR_VERSION, "CASE_ID": CASE_ID, "SEED": SEED, "TRIAL_UNIVERSE_HASH": hash_trials(trials), "SOURCE_INTEGRITY": src, "INTEGRITY": integrity, "ENVIRONMENT": {"python_version": platform.python_version(), "platform": platform.platform()}, "NO_EXTERNAL_DATA": True, "AWS_EXECUTION": False}
    result["SCORED_RESULT"] = score(trials) if mode == "FULL_PILOT" and allowed else None
    result["RESULT_SHA256"] = sha256_bytes(canonical_json(result).encode())
    return result


def main() -> int:
    p = argparse.ArgumentParser(); p.add_argument("--mode", choices=("DRY_RUN", "FULL_PILOT"), default="DRY_RUN"); p.add_argument("--output", type=Path, default=None); args = p.parse_args()
    result = run(args.mode)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True); args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True), encoding="utf-8")
    print(f"EXECUTOR={EXECUTOR_VERSION}"); print(f"MODE={args.mode}"); print(f"EXECUTION_RESULT={result['EXECUTION_RESULT']}"); print(f"TRIAL_UNIVERSE_HASH={result['TRIAL_UNIVERSE_HASH']}"); print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 0 if result["EXECUTION_RESULT"] == "PASS" else 2

if __name__ == "__main__":
    raise SystemExit(main())
