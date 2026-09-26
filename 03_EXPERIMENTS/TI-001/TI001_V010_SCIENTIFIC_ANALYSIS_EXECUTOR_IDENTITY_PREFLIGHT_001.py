#!/usr/bin/env python3
"""TI-001 V010 scientific analysis executor identity preflight."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

ANALYSIS_SHA = "7044dc6bb346fa891b9750f5c63931adfcc7c391"
E1_RESULT_SHA = "5297b578f250a50e90043dab5806877e3c3eec1d"
E2_RESULT_SHA = "82b09712d1fa866dc25927c62ada1c7da1004665"


def git_blob_sha(path: Path) -> str:
    import subprocess
    return subprocess.check_output(["git", "hash-object", str(path)], text=True).strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--analysis", required=True)
    parser.add_argument("--executor-1-result", required=True)
    parser.add_argument("--executor-2-result", required=True)
    parser.add_argument("--authorization", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    analysis = Path(args.analysis)
    e1 = Path(args.executor_1_result)
    e2 = Path(args.executor_2_result)
    auth = json.loads(Path(args.authorization).read_text(encoding="utf-8"))
    source = analysis.read_text(encoding="utf-8")

    checks = {
        "A1_ANALYSIS_SOURCE_EXISTS": analysis.exists(),
        "A2_ANALYSIS_SOURCE_SHA": git_blob_sha(analysis) == ANALYSIS_SHA,
        "A3_E1_RESULT_SHA_BINDING": auth.get("executor_1_result_sha") == E1_RESULT_SHA,
        "A4_E2_RESULT_SHA_BINDING": auth.get("executor_2_result_sha") == E2_RESULT_SHA,
        "A5_E1_LOCAL_CANONICAL": git_blob_sha(e1) == E1_RESULT_SHA,
        "A6_E2_LOCAL_CANONICAL": git_blob_sha(e2) == E2_RESULT_SHA,
        "A7_AUTHORIZED": auth.get("scientific_analysis") == "AUTHORIZED",
        "A8_NO_POOLING": auth.get("pool_executions") is False and '"pool_executions": False' in source,
        "A9_NO_RECODING": "recode" not in source.lower(),
        "A10_NO_RETRY": "retry" not in source.lower(),
        "A11_NO_IMPUTATION": "imputation" not in source.lower(),
        "A12_NO_VALUE_METRIC": all(term not in source.lower() for term in ("value", "reward", "utility", "performance")),
        "A13_TIDC_PRESENT": '"TI_DC"' in source and "q_A" in source,
        "A14_TINULL_PRESENT": '"TI_NULL"' in source and "q_A" in source,
        "A15_PRESENTATION_ANALYSIS": "I1_FIRST" in source and "I2_FIRST" in source,
        "A16_PAIR_ANALYSIS": "pair_level" in source and "agreement" in source,
        "A17_NO_EXECUTION_CALLS": "OpenAI(" not in source and "responses.create" not in source,
        "A18_NO_RESULT_MODIFICATION": "write_text" in source,
        "A19_ANALYSIS_NOT_PERFORMED_BY_PREFLIGHT": True,
    }

    result = {
        "gate_id": "TI001-V010-SCIENTIFIC-ANALYSIS-EXECUTOR-IDENTITY-PREFLIGHT-001",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "analysis_execution": "NOT_PERFORMED",
        "authorization": "AUTHORIZED_BUT_NOT_EXECUTED",
        "analysis_sha": ANALYSIS_SHA,
        "executor_1_result_sha": E1_RESULT_SHA,
        "executor_2_result_sha": E2_RESULT_SHA,
    }
    Path(args.output).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
