#!/usr/bin/env python3
"""TI-001 V010 Executor-2 replay identity preflight."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

EXPECTED_EXECUTOR_ID = "TI001-V010-EXECUTOR-2-REPLAY-001"
EXPECTED_FIXTURE_ID = "TI001-V008-FIXTURE-001"
EXPECTED_FIXTURE_SHA = "dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"
EXPECTED_INTERFACE_ID = "TI001-V010-DECISION-INTERFACE-001"
EXPECTED_INTERFACE_SHA = "e025d66e477de3afd79147986b716389d7d7be03d01a21d4380b384e17c8510c"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--executor", required=True)
    p.add_argument("--fixture", required=True)
    p.add_argument("--output", required=True)
    a = p.parse_args()

    executor_path = Path(a.executor)
    source = executor_path.read_text(encoding="utf-8")
    fixture_raw = Path(a.fixture).read_bytes()

    checks = {
        "A1_EXECUTOR_ID": EXPECTED_EXECUTOR_ID in source,
        "A2_FIXTURE_ID": EXPECTED_FIXTURE_ID in source,
        "A3_FIXTURE_SHA": EXPECTED_FIXTURE_SHA in source,
        "A4_INTERFACE_ID": EXPECTED_INTERFACE_ID in source,
        "A5_INTERFACE_SHA": EXPECTED_INTERFACE_SHA in source,
        "A6_FIXTURE_SHA_MATCH": hashlib.sha256(fixture_raw).hexdigest() == EXPECTED_FIXTURE_SHA,
        "A7_420_UNITS_LITERAL": "420" in source,
        "A8_NO_EXECUTOR_1_IMPORT": "SCIENTIFIC_EXECUTOR_1_001" not in source,
        "A9_NO_EXECUTOR_1_RESULT": "SCIENTIFIC_EXECUTOR_1_RESULT_001" not in source,
        "A10_NO_RETRY": "retry(" not in source.lower(),
        "A11_NO_RECODE": "recode(" not in source.lower(),
        "A12_NO_ANALYSIS": '"analysis_performed": False' in source,
        "A13_NOT_PERFORMED_BY_DEFAULT": '"scientific_execution": "NOT_PERFORMED"' in source,
    }

    result = {
        "gate_id": "TI001-V010-EXECUTOR-2-IDENTITY-PREFLIGHT-001",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "all_checks_pass": all(checks.values()),
        "scientific_execution": "NOT_PERFORMED",
        "authorization": "NOT_AUTHORIZED",
    }

    Path(a.output).write_text(
        json.dumps(result, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
