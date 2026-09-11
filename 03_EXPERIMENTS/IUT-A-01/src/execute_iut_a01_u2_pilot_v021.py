#!/usr/bin/env python3
"""IUT-A-01 U2 executor v0.2.1.

Compatibility wrapper around v0.2 that fixes control-flow bugs in the wrapper:
the dynamically loaded source module is registered in sys.modules, the per-class
count dictionary is metadata, and the negative integrity assertion
analyst_generated_options_added=False is evaluated with the correct polarity.
All scientific logic, frozen source checks, trial universe and M1-M3 scoring are
inherited unchanged from v0.2.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import platform
import sys
from pathlib import Path

SOURCE = Path(__file__).with_name("execute_iut_a01_u2_pilot_v02.py")


def load_source_module():
    spec = importlib.util.spec_from_file_location("iut_a01_u2_v02", SOURCE)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Cannot load executor source: {SOURCE}")
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def canonical_json(value: object) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def sha256_bytes(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def run(mode: str) -> dict:
    mod = load_source_module()
    source_integrity = mod.verify_frozen_source_files()
    trials = mod.build_universe()
    integrity = mod.integrity_checks(trials, source_integrity)
    fixture_hash = mod.hash_trials(trials)

    positive_integrity_flags = (
        "trial_count_ok",
        "class_balance_ok",
        "unique_trial_ids_ok",
        "same_universe_for_both_arms",
        "outcome_blind",
        "ground_truth_immutable",
        "frozen_source_files_match",
    )
    execution_allowed = (
        all(integrity[key] is True for key in positive_integrity_flags)
        and integrity["analyst_generated_options_added"] is False
    )

    result = {
        "EXECUTION_RESULT": "PASS" if execution_allowed else "INDETERMINATE",
        "MODE": mode,
        "EXECUTOR_VERSION": "IUT-A-01-U2-PILOT-EXECUTOR-0.2.1",
        "CASE_ID": mod.CASE_ID,
        "SEED": mod.SEED,
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
        result["SCORED_RESULT"] = mod.score(trials)
    else:
        result["SCORED_RESULT"] = None

    result["RESULT_SHA256"] = sha256_bytes(canonical_json(result).encode("utf-8"))
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

    print("EXECUTOR=IUT-A-01-U2-PILOT-EXECUTOR-0.2.1")
    print(f"MODE={args.mode}")
    print(f"EXECUTION_RESULT={result['EXECUTION_RESULT']}")
    print(f"TRIAL_UNIVERSE_HASH={result['TRIAL_UNIVERSE_HASH']}")
    print(json.dumps(result, indent=2, ensure_ascii=False, sort_keys=True))
    return 0 if result["EXECUTION_RESULT"] == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
