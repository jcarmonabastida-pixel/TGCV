#!/usr/bin/env python3
"""TI-001 V008 generator integrity preflight."""

from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SPEC_PATH = ROOT / "03_EXPERIMENTS" / "TI-001" / "TI001_V008_GENERATOR_SPECIFICATION_001.md"
GENERATOR_PATH = ROOT / "03_EXPERIMENTS" / "TI-001" / "TI001_V008_GENERATOR_001.py"

EXPECTED_GENERATOR_ID = "TI001-V008-FIXTURE-GENERATOR-001"
EXPECTED_SPEC_SHA = "8964cb1cee4e5017d8512873fcb7934c21d5d18c"
EXPECTED_GENERATOR_SHA = "bcc86196060db50a62e512549c94a84c55561669"
EXPECTED_IMPLEMENTATION_COMMIT = "ca2219420ffdab20c4bb4d98e116ab9eb3b989b3"

REQUIRED_SPEC_MARKERS = (
    "Status:** DESIGN — NOT GENERATED",
    "**Scientific execution:** NOT_PERFORMED",
    "- PRNG: xorshift32.",
    "- State width: exactly 32 bits.",
    "- Seed: decimal integer `20260925`.",
    "- Condition stream initial state: seed.",
    "- Presentation stream initial state: `seed XOR 0x9E3779B9`, reduced to 32 bits.",
    "- Iteration is descending: `i = n-1, n-2, ..., 1`.",
    "- At each iteration, consume one PRNG state and calculate `j = state % (i+1)`.",
    "- Condition labels before shuffle: 70 `control`, followed by 70 `treatment`, followed by 70 `null`.",
    "- Presentation labels before shuffle: 105 `I1_FIRST`, followed by 105 `I2_FIRST`.",
    "- Pair IDs are assigned in fixed lexical order `P001` through `P210`;",
    "V008 fixture generation remains blocked until the implementation passes every self-test vector and the generator preflight binds the implementation blob SHA.",
)

REQUIRED_GENERATOR_MARKERS = (
    'GENERATOR_ID = "TI001-V008-FIXTURE-GENERATOR-001"',
    "SEED = 20260925",
    "MASK32 = 0xFFFFFFFF",
    "PRESENTATION_XOR = 0x9E3779B9",
    "def xorshift32(state: int) -> int:",
    "def fisher_yates(values: list[str], seed: int)",
    'def self_test() -> dict:',
    'raise RuntimeError(',
    '"BLOCKED: V008 fixture generation requires generator preflight "',
    "and source hash binding.",
    '"scientific_execution": "NOT_PERFORMED"',
)


def git_blob_sha1(data: bytes) -> str:
    header = f"blob {len(data)}\0".encode("utf-8")
    return hashlib.sha1(header + data).hexdigest()


def load_generator():
    spec = importlib.util.spec_from_file_location("ti001_v008_generator", GENERATOR_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Unable to load V008 generator module")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run_preflight() -> dict:
    checks = {}

    spec_bytes = SPEC_PATH.read_bytes()
    generator_bytes = GENERATOR_PATH.read_bytes()
    spec_text = spec_bytes.decode("utf-8")
    generator_text = generator_bytes.decode("utf-8")

    checks["spec_exists"] = SPEC_PATH.is_file()
    checks["generator_exists"] = GENERATOR_PATH.is_file()
    checks["spec_blob_sha1"] = git_blob_sha1(spec_bytes) == EXPECTED_SPEC_SHA
    checks["generator_blob_sha1"] = git_blob_sha1(generator_bytes) == EXPECTED_GENERATOR_SHA
    checks["implementation_commit_binding_declared"] = bool(EXPECTED_IMPLEMENTATION_COMMIT)
    checks["generator_id"] = EXPECTED_GENERATOR_ID in generator_text
    checks["spec_markers"] = all(marker in spec_text for marker in REQUIRED_SPEC_MARKERS)
    checks["generator_markers"] = all(marker in generator_text for marker in REQUIRED_GENERATOR_MARKERS)

    module = load_generator()
    result = module.self_test()
    checks["self_test_status"] = result.get("status") == "PASS"
    checks["self_test_all_checks"] = all(result.get("checks", {}).values())
    checks["self_test_generator_id"] = result.get("generator_id") == EXPECTED_GENERATOR_ID
    checks["self_test_scientific_execution"] = result.get("scientific_execution") == "NOT_PERFORMED"

    checks["generation_blocked"] = (
        "BLOCKED: V008 fixture generation requires generator preflight "
        in generator_text
        and "and source hash binding." in generator_text
        and generator_text.count("def generate") == 1
    )

    passed = all(checks.values())
    return {
        "preflight_id": "TI001-V008-GENERATOR-PREFLIGHT-001",
        "status": "PASS" if passed else "FAIL",
        "scientific_execution": "NOT_PERFORMED",
        "fixture_generated": False,
        "expected_implementation_commit": EXPECTED_IMPLEMENTATION_COMMIT,
        "expected_spec_blob_sha1": EXPECTED_SPEC_SHA,
        "expected_generator_blob_sha1": EXPECTED_GENERATOR_SHA,
        "checks": checks,
    }


def main() -> None:
    print(json.dumps(run_preflight(), sort_keys=True))


if __name__ == "__main__":
    main()
