#!/usr/bin/env python3
"""TI-001 V010 deterministic scientific analysis."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

VALID_OUTPUTS = {"A", "B"}
EXPECTED_DECISIONS = 420
EXPECTED_PER_CONDITION = 140
EXPECTED_PAIRS = 210
EXPECTED_PRESENTATIONS = 210

E1_RESULT_BLOB = "5297b578f250a50e90043dab5806877e3c3eec1d"
E2_RESULT_BLOB = "82b09712d1fa866dc25927c62ada1c7da1004665"


def git_blob_sha(path: Path) -> str:
    import subprocess
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def load_result(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def analyze(result):
    records = result["records"]
    conditions = ("control", "treatment", "null")
    presentations = ("I1_FIRST", "I2_FIRST")
    by_condition = {}
    for condition in conditions:
        rows = [r for r in records if r["condition"] == condition]
        a = sum(r["parsed_response"] == "A" for r in rows)
        b = sum(r["parsed_response"] == "B" for r in rows)
        by_condition[condition] = {
            "n": len(rows),
            "A": a,
            "B": b,
            "q_A": a / len(rows),
        }

    ti_dc = by_condition["treatment"]["q_A"] - by_condition["control"]["q_A"]
    ti_null = by_condition["null"]["q_A"] - by_condition["control"]["q_A"]

    by_presentation = {}
    for presentation in presentations:
        rows = [r for r in records if r["presentation"] == presentation]
        a = sum(r["parsed_response"] == "A" for r in rows)
        b = sum(r["parsed_response"] == "B" for r in rows)
        by_presentation[presentation] = {
            "n": len(rows),
            "A": a,
            "B": b,
            "q_A": a / len(rows),
        }

    pairs = {}
    for r in records:
        pairs.setdefault(r["pair_id"], []).append(r["parsed_response"])
    agreement = sum(len(v) == 2 and v[0] == v[1] for v in pairs.values())
    disagreement = EXPECTED_PAIRS - agreement

    return {
        "decision_count": len(records),
        "valid_count": sum(r["validity"] == "VALID" for r in records),
        "invalid_count": sum(r["validity"] != "VALID" for r in records),
        "by_condition": by_condition,
        "TI_DC": ti_dc,
        "TI_NULL": ti_null,
        "by_presentation": by_presentation,
        "pair_level": {
            "pairs": len(pairs),
            "agreement": agreement,
            "disagreement": disagreement,
            "agreement_rate": agreement / EXPECTED_PAIRS,
        },
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--executor-1-result", required=True)
    parser.add_argument("--executor-2-result", required=True)
    parser.add_argument("--authorization", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    e1_path = Path(args.executor_1_result)
    e2_path = Path(args.executor_2_result)
    auth = json.loads(Path(args.authorization).read_text(encoding="utf-8"))

    if auth.get("scientific_analysis") != "AUTHORIZED":
        raise SystemExit("scientific analysis is not authorized")
    if auth.get("executor_1_result_sha") != E1_RESULT_BLOB:
        raise SystemExit("Executor-1 result binding mismatch")
    if auth.get("executor_2_result_sha") != E2_RESULT_BLOB:
        raise SystemExit("Executor-2 result binding mismatch")
    if auth.get("pool_executions") is not False:
        raise SystemExit("pooling is prohibited")

    e1 = load_result(e1_path)
    e2 = load_result(e2_path)

    if git_blob_sha(e1_path) != E1_RESULT_BLOB:
        raise SystemExit("Executor-1 local result does not match canonical Git blob")
    if git_blob_sha(e2_path) != E2_RESULT_BLOB:
        raise SystemExit("Executor-2 local result does not match canonical Git blob")

    analysis = {
        "analysis_id": "TI001-V010-SCIENTIFIC-ANALYSIS-001",
        "scientific_analysis": "PERFORMED",
        "authorization_id": auth["authorization_id"],
        "pool_executions": False,
        "executor_1": analyze(e1),
        "executor_2": analyze(e2),
    }

    Path(args.output).write_text(json.dumps(analysis, indent=2) + "
", encoding="utf-8")


if __name__ == "__main__":
    main()
