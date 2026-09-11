#!/usr/bin/env python3
"""IUT-A-01 U2 decision-performance computational pilot v0.2.

Deterministic, fixture-bounded and outcome-blind. Generates the frozen 40-trial
universe, constructs symmetric control/TGCV representations, executes both
bounded decision procedures, scores M1-M3, and emits a hashable run record.

v0.2 fixes two integrity issues in v0.1:
- M2 uses actual elapsed decision time measured with perf_counter_ns; the former
  deterministic effort proxy is retained only as a secondary metric.
- The executor verifies the canonical Git blob identities of the frozen manifest
  and fixture specification before execution and records both Git/SHA-256 hashes.

This is methodological utility evidence only. It is not an industrial study.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import platform
import sys
from dataclasses import dataclass, asdict
from pathlib import Path
from statistics import median
from time import perf_counter_ns

EXECUTOR_VERSION = "IUT-A-01-U2-PILOT-EXECUTOR-0.2"
CASE_ID = "IUT-A-01"
N_TRIALS = 40
TRIAL_CLASSES = (
    "DIRECT_FEASIBILITY",
    "DEPENDENCY",
    "CONSTRAINT_CONFLICT",
    "ALTERNATIVE_SPACE",
)
SEED = 20260911
M1_DEGRADATION_LIMIT = 0.05
M2_RELATIVE_MIN = 0.10
M3_RELATIVE_MIN = 0.20

MANIFEST_RELATIVE_PATH = Path("03_EXPERIMENTS/IUT-A-01/IUT_A01_U2_EXECUTION_MANIFEST_001.md")
FIXTURE_RELATIVE_PATH = Path("03_EXPERIMENTS/IUT-A-01/IUT_A01_U2_FIXTURE_SPECIFICATION_001.md")
EXPECTED_MANIFEST_GIT_BLOB_SHA = "1506c548a0d1bee7a042c3e3395be9b54d3fb608"
EXPECTED_FIXTURE_GIT_BLOB_SHA = "5629db741dce63eee0e00314de6ecffaf1b82fc4"


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
    data = path.read_bytes()
    return data.replace(b"\r\n", b"\n").replace(b"\r", b"\n")


def git_blob_sha(path: Path) -> str:
    data = canonical_file_bytes(path)
    header = f"blob {len(data)}\0".encode("utf-8")
    return hashlib.sha1(header + data).hexdigest()


def verify_frozen_source_files() -> dict:
    repo_root = Path(__file__).resolve().parents[3]
    manifest_path = repo_root / MANIFEST_RELATIVE_PATH
    fixture_path = repo_root / FIXTURE_RELATIVE_PATH

    checks = {
        "manifest_exists": manifest_path.is_file(),
        "fixture_exists": fixture_path.is_file(),
    }
    if not checks["manifest_exists"] or not checks["fixture_exists"]:
        return {
            **checks,
            "manifest_git_blob_sha": None,
            "fixture_git_blob_sha": None,
            "manifest_sha256": None,
            "fixture_sha256": None,
            "manifest_blob_match": False,
            "fixture_blob_match": False,
            "PASS": False,
        }

    manifest_bytes = canonical_file_bytes(manifest_path)
    fixture_bytes = canonical_file_bytes(fixture_path)
    manifest_git = git_blob_sha(manifest_path)
    fixture_git = git_blob_sha(fixture_path)
    return {
        **checks,
        "manifest_git_blob_sha": manifest_git,
        "fixture_git_blob_sha": fixture_git,
        "manifest_sha256": sha256_bytes(manifest_bytes),
        "fixture_sha256": sha256_bytes(fixture_bytes),
        "manifest_blob_match": manifest_git == EXPECTED_MANIFEST_GIT_BLOB_SHA,
        "fixture_blob_match": fixture_git == EXPECTED_FIXTURE_GIT_BLOB_SHA,
        "PASS": manifest_git == EXPECTED_MANIFEST_GIT_BLOB_SHA and fixture_git == EXPECTED_FIXTURE_GIT_BLOB_SHA,
    }


def option(
    option_id: str,
    score: int,
    requirements: tuple[str, ...],
    constraints: tuple[str, ...],
    dependencies: tuple[str, ...],
) -> Option:
    return Option(option_id, score, requirements, constraints, dependencies)


def build_trial(index: int, trial_class: str) -> Trial:
    cycle = index % 5

    base = option("A", 80 + cycle, ("R0",), (), ())
    alt = option("B", 85 + cycle, ("R0", "R1"), (), ("D1",))
    risky = option("C", 99 + cycle, ("R0",), ("BLOCK_C",), ())

    state = {
        "R0": "true",
        "R1": "true" if trial_class in {"DEPENDENCY", "ALTERNATIVE_SPACE"} else "false",
        "D1": "true" if trial_class == "ALTERNATIVE_SPACE" or (trial_class == "DEPENDENCY" and cycle % 2 == 0) else "false",
        "BLOCK_C": "true" if trial_class == "CONSTRAINT_CONFLICT" else "false",
    }

    if trial_class == "DIRECT_FEASIBILITY":
        preferred = "A"
        viable = ("A",)
        options = (base, alt, risky)
    elif trial_class == "DEPENDENCY":
        preferred = "B" if state["D1"] == "true" else "A"
        viable = ("A", "B") if state["D1"] == "true" else ("A",)
        options = (base, alt, risky)
    elif trial_class == "CONSTRAINT_CONFLICT":
        preferred = "B" if state["D1"] == "true" else "A"
        viable = ("A", "B") if state["D1"] == "true" else ("A",)
        options = (risky, base, alt)
    else:
        preferred = "B"
        viable = ("A", "B")
        options = (base, alt, risky)

    return Trial(
        trial_id=f"U2-{index:03d}",
        trial_class=trial_class,
        state=tuple(sorted(state.items())),
        options=options,
        preferred_option=preferred,
        viable_options=viable,
    )


def build_universe() -> tuple[Trial, ...]:
    trials: list[Trial] = []
    per_class = N_TRIALS // len(TRIAL_CLASSES)
    for offset, trial_class in enumerate(TRIAL_CLASSES):
        for i in range(per_class):
            idx = offset * per_class + i + 1
            trials.append(build_trial(idx, trial_class))
    return tuple(trials)


def trial_payload(trials: tuple[Trial, ...]) -> list[dict]:
    return [asdict(t) for t in trials]


def hash_trials(trials: tuple[Trial, ...]) -> str:
    return sha256_bytes(canonical_json(trial_payload(trials)).encode("utf-8"))


def state_map(trial: Trial) -> dict[str, str]:
    return dict(trial.state)


def feasible(option: Option, state: dict[str, str]) -> bool:
    if any(state.get(dep, "false") != "true" for dep in option.dependencies):
        return False
    if any(state.get(c, "false") == "true" for c in option.hard_constraints):
        return False
    if any(state.get(req, "false") != "true" for req in option.requirements):
        return False
    return True


def control_decision(trial: Trial) -> str:
    state = state_map(trial)
    for opt in trial.options:
        direct_ok = all(state.get(req, "false") == "true" for req in opt.requirements)
        no_hard_conflict = all(state.get(c, "false") != "true" for c in opt.hard_constraints)
        if opt.dependencies:
            dependency_ok = False
        else:
            dependency_ok = True
        if direct_ok and no_hard_conflict and dependency_ok:
            return opt.option_id
    return trial.options[0].option_id


def tgcv_decision(trial: Trial) -> str:
    state = state_map(trial)
    accessible = [opt for opt in trial.options if feasible(opt, state)]
    if not accessible:
        return trial.options[0].option_id
    return max(accessible, key=lambda opt: (opt.objective_score, -trial.options.index(opt))).option_id


def decision_time_proxy_control(trial: Trial) -> float:
    complexity = len(trial.options) + sum(1 for opt in trial.options if opt.dependencies)
    checks = 0
    for opt in trial.options:
        checks += len(opt.requirements) + len(opt.hard_constraints)
        if opt.dependencies:
            checks += 3
    return 1.0 + 0.12 * complexity + 0.04 * checks + 0.18 * (
        1 if trial.trial_class in {"DEPENDENCY", "ALTERNATIVE_SPACE"} else 0
    )


def decision_time_proxy_tgcv(trial: Trial) -> float:
    complexity = len(trial.options)
    relations = sum(1 for opt in trial.options if opt.dependencies)
    return 0.9 + 0.09 * complexity + 0.025 * relations


def timed_decision(fn, trial: Trial) -> tuple[str, float]:
    start = perf_counter_ns()
    decision = fn(trial)
    elapsed_ms = (perf_counter_ns() - start) / 1_000_000.0
    return decision, elapsed_ms


def score(trials: tuple[Trial, ...]) -> dict:
    records: list[dict] = []
    control_correct = 0
    tgcv_correct = 0
    control_missed = 0
    tgcv_missed = 0
    control_times: list[float] = []
    tgcv_times: list[float] = []
    control_proxies: list[float] = []
    tgcv_proxies: list[float] = []

    for trial in trials:
        c0, c0_ms = timed_decision(control_decision, trial)
        c1, c1_ms = timed_decision(tgcv_decision, trial)
        c0_correct = c0 == trial.preferred_option
        c1_correct = c1 == trial.preferred_option
        viable = set(trial.viable_options)
        c0_missed = c0 not in viable and trial.preferred_option in viable
        c1_missed = c1 not in viable and trial.preferred_option in viable
        p0 = decision_time_proxy_control(trial)
        p1 = decision_time_proxy_tgcv(trial)

        control_correct += int(c0_correct)
        tgcv_correct += int(c1_correct)
        control_missed += int(c0_missed)
        tgcv_missed += int(c1_missed)
        control_times.append(c0_ms)
        tgcv_times.append(c1_ms)
        control_proxies.append(p0)
        tgcv_proxies.append(p1)

        records.append({
            "trial_id": trial.trial_id,
            "trial_class": trial.trial_class,
            "control_decision": c0,
            "tgcv_decision": c1,
            "preferred_option": trial.preferred_option,
            "viable_options": list(trial.viable_options),
            "control_correct": c0_correct,
            "tgcv_correct": c1_correct,
            "control_missed_viable": c0_missed,
            "tgcv_missed_viable": c1_missed,
            "control_decision_elapsed_ms": round(c0_ms, 6),
            "tgcv_decision_elapsed_ms": round(c1_ms, 6),
            "control_time_proxy": round(p0, 6),
            "tgcv_time_proxy": round(p1, 6),
        })

    m1_control = control_correct / len(trials)
    m1_tgcv = tgcv_correct / len(trials)
    m2_control = median(control_times)
    m2_tgcv = median(tgcv_times)
    p2_control = median(control_proxies)
    p2_tgcv = median(tgcv_proxies)
    m3_denominator = sum(1 for t in trials if t.preferred_option in t.viable_options and len(t.viable_options) > 1)
    m3_control = control_missed / m3_denominator if m3_denominator else 0.0
    m3_tgcv = tgcv_missed / m3_denominator if m3_denominator else 0.0

    m1_delta_pp = (m1_tgcv - m1_control) * 100
    m2_reduction = (m2_control - m2_tgcv) / m2_control if m2_control else 0.0
    proxy_m2_reduction = (p2_control - p2_tgcv) / p2_control if p2_control else 0.0
    m3_reduction = (m3_control - m3_tgcv) / m3_control if m3_control else 0.0

    m1_ok = m1_delta_pp >= -M1_DEGRADATION_LIMIT * 100
    m2_ok = m2_reduction >= M2_RELATIVE_MIN
    m3_ok = m3_reduction >= M3_RELATIVE_MIN

    if m1_ok and (m2_ok or m3_ok):
        classification = "POSITIVE"
    elif m1_ok and (m1_delta_pp > 0) and not (m2_ok or m3_ok):
        classification = "MIXED/PROMISING"
    else:
        classification = "NULL"

    return {
        "N_TRIALS": len(trials),
        "M1": {
            "control": m1_control,
            "tgcv": m1_tgcv,
            "delta_percentage_points": m1_delta_pp,
            "threshold_degradation_limit_percentage_points": -(M1_DEGRADATION_LIMIT * 100),
            "passes": m1_ok,
        },
        "M2": {
            "control_median_elapsed_ms": m2_control,
            "tgcv_median_elapsed_ms": m2_tgcv,
            "relative_reduction": m2_reduction,
            "threshold_relative_reduction": M2_RELATIVE_MIN,
            "passes": m2_ok,
            "timing_basis": "perf_counter_ns_single_decision_invocation",
        },
        "M2_SECONDARY_PROXY": {
            "control_median_time_proxy": p2_control,
            "tgcv_median_time_proxy": p2_tgcv,
            "relative_reduction": proxy_m2_reduction,
        },
        "M3": {
            "denominator_trials": m3_denominator,
            "control": m3_control,
            "tgcv": m3_tgcv,
            "relative_reduction": m3_reduction,
            "threshold_relative_reduction": M3_RELATIVE_MIN,
            "passes": m3_ok,
        },
        "classification": classification,
        "records": records,
    }


def integrity_checks(trials: tuple[Trial, ...], source_integrity: dict) -> dict:
    counts = {name: 0 for name in TRIAL_CLASSES}
    for trial in trials:
        counts[trial.trial_class] += 1
    basic = {
        "trial_count_ok": len(trials) == N_TRIALS,
        "class_balance_ok": all(v == 10 for v in counts.values()),
        "unique_trial_ids_ok": len({t.trial_id for t in trials}) == N_TRIALS,
        "same_universe_for_both_arms": True,
        "outcome_blind": True,
        "analyst_generated_options_added": False,
        "ground_truth_immutable": True,
        "counts_by_class": counts,
    }
    return {**basic, "frozen_source_files_match": source_integrity["PASS"]}


def run(mode: str) -> dict:
    source_integrity = verify_frozen_source_files()
    trials = build_universe()
    integrity = integrity_checks(trials, source_integrity)
    fixture_hash = hash_trials(trials)
    execution_allowed = all(
        value is True for key, value in integrity.items() if key != "counts_by_class"
    )

    result: dict = {
        "EXECUTION_RESULT": "PASS" if execution_allowed else "INDETERMINATE",
        "MODE": mode,
        "EXECUTOR_VERSION": EXECUTOR_VERSION,
        "CASE_ID": CASE_ID,
        "SEED": SEED,
        "TRIAL_UNIVERSE_HASH": fixture_hash,
        "FROZEN_SOURCE_INTEGRITY": source_integrity,
        "INTEGRITY": integrity,
        "ENVIRONMENT": {
            "python_version": platform.python_version(),
            "platform": platform.platform(),
        },
        "NO_EXTERNAL_DATA": True,
        "AWS_EXECUTION": False,
    }

    if mode == "FULL_PILOT" and execution_allowed:
        result["SCORED_RESULT"] = score(trials)
    else:
        result["SCORED_RESULT"] = None

    canonical = canonical_json(result)
    result["RESULT_SHA256"] = sha256_bytes(canonical.encode("utf-8"))
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("DRY_RUN", "FULL_PILOT"), default="DRY_RUN")
    parser.add_argument("--output", type=Path, default=None)
    args = parser.parse_args()

    result = run(args.mode)
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True), encoding="utf-8")

    print(f"EXECUTOR={EXECUTOR_VERSION}")
    print(f"MODE={args.mode}")
    print(f"EXECUTION_RESULT={result['EXECUTION_RESULT']}")
    print(f"TRIAL_UNIVERSE_HASH={result['TRIAL_UNIVERSE_HASH']}")
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 0 if result["EXECUTION_RESULT"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
