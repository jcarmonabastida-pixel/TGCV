#!/usr/bin/env python3
import argparse
import hashlib
import json
import subprocess
import sys
import tempfile
from pathlib import Path

EXPECTED_GENERATOR_SHA = "9170f767cac3fceccaba248747c6524c5f150e11"
EXPECTED_FIXTURE_SHA256 = "30268ab425aaeff23f0a719126765f832653d37dfb45746388a272d054549ee1"
EXPECTED_SEED = 20260926
EXPECTED_GENERATOR_ID = "TI001-V011-FIXTURE-GENERATOR-001"
EXPECTED_FIXTURE_ID = "TI001-V011-FIXTURE-001"
EXPECTED_SCHEMA_ID = "TI001-V011-DU-SCHEMA-001"
EXPECTED_DECISIONS = 420
EXPECTED_PAIRS = 210
EXPECTED_CONDITIONS = {"control": 70, "treatment": 70, "null": 70}
EXPECTED_UNIT_CONDITIONS = {"control": 140, "treatment": 140, "null": 140}
EXPECTED_PRESENTATIONS = {"I1_FIRST": 210, "I2_FIRST": 210}
EXPECTED_FIELDS = [
    "decision_id", "pair_id", "condition", "presentation",
    "context", "available_actions", "future_structure"
]
FORBIDDEN_KEYS = {
    "utility", "reward", "value", "performance", "task_success",
    "successor_state", "outcome", "model_response", "scientific_score"
}


def git_blob_sha(path):
    return subprocess.check_output(
        ["git", "hash-object", str(path)], text=True
    ).strip()


def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()


def fail_or_pass(checks):
    return "PASS" if all(checks.values()) else "FAIL"


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", required=True)
    parser.add_argument("--generator", required=True)
    parser.add_argument("--schema", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    fixture = Path(args.fixture)
    generator = Path(args.generator)
    schema = Path(args.schema)
    fixture_bytes = fixture.read_bytes()
    data = json.loads(fixture_bytes.decode("utf-8"))

    units = data.get("decision_units", [])
    pairs = {}
    first_counts = {c: {"I1_FIRST": 0, "I2_FIRST": 0} for c in EXPECTED_CONDITIONS}
    condition_units = {c: 0 for c in EXPECTED_CONDITIONS}
    presentation_units = {p: 0 for p in EXPECTED_PRESENTATIONS}
    decision_ids = []
    pair_ids = []

    for unit in units:
        decision_ids.append(unit.get("decision_id"))
        pair_ids.append(unit.get("pair_id"))
        condition = unit.get("condition")
        presentation = unit.get("presentation")
        condition_units[condition] = condition_units.get(condition, 0) + 1
        presentation_units[presentation] = presentation_units.get(presentation, 0) + 1
        pairs.setdefault(unit.get("pair_id"), []).append(unit)
        if len(pairs[unit.get("pair_id")]) == 1:
            first_counts[condition][presentation] += 1

    checks = {}
    checks["A1_FIXTURE_EXISTS"] = fixture.exists()
    checks["A2_GENERATOR_EXISTS"] = generator.exists()
    checks["A3_SCHEMA_EXISTS"] = schema.exists()
    checks["A4_FIXTURE_IDENTITY"] = data.get("fixture_id") == EXPECTED_FIXTURE_ID
    checks["A5_SCHEMA_IDENTITY"] = data.get("schema_id") == EXPECTED_SCHEMA_ID
    checks["A6_GENERATOR_IDENTITY"] = data.get("generator_id") == EXPECTED_GENERATOR_ID
    checks["A7_SEED_IDENTITY"] = data.get("seed") == EXPECTED_SEED
    checks["A8_FIXTURE_SHA256"] = sha256_bytes(fixture_bytes) == EXPECTED_FIXTURE_SHA256
    checks["A9_DECISION_COUNT"] = len(units) == EXPECTED_DECISIONS
    checks["A10_UNIQUE_PAIRS"] = len(pairs) == EXPECTED_PAIRS
    checks["A11_TWO_UNITS_PER_PAIR"] = all(len(v) == 2 for v in pairs.values())
    checks["A12_PAIR_PRESENTATIONS"] = all(
        sorted(u.get("presentation") for u in v) == ["I1_FIRST", "I2_FIRST"]
        for v in pairs.values()
    )
    checks["A13_PAIR_CONDITION_BALANCE"] = {
        c: sum(1 for v in pairs.values() if v[0].get("condition") == c)
        for c in EXPECTED_CONDITIONS
    } == EXPECTED_CONDITIONS
    checks["A14_UNIT_CONDITION_BALANCE"] = condition_units == EXPECTED_UNIT_CONDITIONS
    checks["A15_PRESENTATION_BALANCE"] = presentation_units == EXPECTED_PRESENTATIONS
    checks["A16_FIRST_ORIENTATION_BALANCE"] = first_counts == {
        c: {"I1_FIRST": 35, "I2_FIRST": 35} for c in EXPECTED_CONDITIONS
    }
    checks["A17_DECISION_IDS_UNIQUE"] = len(decision_ids) == len(set(decision_ids))
    checks["A18_PAIR_IDS_UNIQUE"] = len(pair_ids) == len(set(pair_ids))
    checks["A19_UNIT_FIELD_ORDER"] = all(list(u.keys()) == EXPECTED_FIELDS for u in units)
    checks["A20_ACTION_SET"] = all(u.get("available_actions") == ["A", "B"] for u in units)
    checks["A21_FUTURE_STRUCTURE_SEMANTICS"] = all(
        u.get("future_structure") == {
            "successor_realized": False,
            "future_structure_available": u.get("condition") == "treatment",
        } for u in units
    )
    checks["A22_NO_FORBIDDEN_FIELDS"] = not any(
        key in FORBIDDEN_KEYS for u in units for key in u.keys()
    )
    checks["A23_GENERATOR_GIT_BLOB_SHA"] = git_blob_sha(generator) == EXPECTED_GENERATOR_SHA
    checks["A24_SCIENTIFIC_EXECUTION_NOT_PERFORMED"] = True

    with tempfile.TemporaryDirectory() as tmp:
        reconstructed = Path(tmp) / "reconstructed.json"
        subprocess.check_call([
            sys.executable, str(generator), "--output", str(reconstructed)
        ], stdout=subprocess.DEVNULL)
        checks["A25_DETERMINISTIC_RECONSTRUCTION"] = (
            reconstructed.read_bytes() == fixture_bytes
        )

    status = fail_or_pass(checks)
    result = {
        "gate_id": "TI001-V011-FIXTURE-INTEGRITY-GATE-001",
        "status": status,
        "checks": checks,
        "fixture_id": EXPECTED_FIXTURE_ID,
        "schema_id": EXPECTED_SCHEMA_ID,
        "generator_id": EXPECTED_GENERATOR_ID,
        "seed": EXPECTED_SEED,
        "decision_count": len(units),
        "pair_count": len(pairs),
        "fixture_sha256": sha256_bytes(fixture_bytes),
        "generator_sha": git_blob_sha(generator),
        "schema_sha": git_blob_sha(schema),
        "scientific_execution": "NOT_PERFORMED",
    }
    Path(args.output).write_text(
        json.dumps(result, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(result, indent=2))
    raise SystemExit(0 if status == "PASS" else 1)


if __name__ == "__main__":
    main()
