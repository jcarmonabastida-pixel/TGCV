#!/usr/bin/env python3
import argparse
import json
import subprocess
from pathlib import Path

EXPECTED_GENERATOR_SHA = "15257bde7007ee861e4217d16ded40d2a27e92c8"
GENERATOR_PATH = "03_EXPERIMENTS/TI-001/TI001_V011_FIXTURE_GENERATOR_001.py"
EXPECTED_FIRST_XORSHIFT32 = [270369, 67634689, 2647435461, 307599695, 2398689233]
EXPECTED_SEED = 20260926
EXPECTED_PRESENTATION_XOR = 0x9E3779B9


def git_blob_sha(path):
    return subprocess.check_output(["git", "hash-object", path], text=True).strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--generator", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    generator = Path(args.generator)
    source = generator.read_text(encoding="utf-8")
    checks = {}

    checks["A1_GENERATOR_EXISTS"] = generator.exists()
    checks["A2_GENERATOR_SHA"] = git_blob_sha(generator) == EXPECTED_GENERATOR_SHA
    checks["A3_XORSHIFT32_CLASS"] = "class XorShift32" in source
    checks["A4_FISHER_YATES"] = "def fisher_yates" in source
    checks["A5_SEED"] = "SEED = 20260926" in source
    checks["A6_PRESENTATION_XOR"] = "PRESENTATION_XOR = 0x9E3779B9" in source
    checks["A7_ZERO_STATE_REJECTION"] = "seed == 0" in source and "forbidden zero state" in source
    checks["A8_NO_WARMUP_DRAWS"] = "warm" not in source.lower()
    checks["A9_MODULO_SELECTION"] = "prng.next() % (i + 1)" in source
    checks["A10_SERIALIZATION"] = 'separators=(",", ":")' in source and 'encode("utf-8")' in source
    checks["A11_NO_MODEL_API"] = "OpenAI(" not in source and "responses.create" not in source and "chat.completions" not in source
    checks["A12_NO_RESULT_CONSUMPTION"] = "EXECUTOR_1_RESULT" not in source and "EXECUTOR_2_RESULT" not in source

    namespace = {}
    exec(compile(source, str(generator), "exec"), namespace)
    XorShift32 = namespace["XorShift32"]
    build_fixture = namespace["build_fixture"]
    serialize = namespace["serialize"]

    prng = XorShift32(1)
    observed = [prng.next() for _ in range(5)]
    checks["A13_XORSHIFT32_KNOWN_VECTOR"] = observed == EXPECTED_FIRST_XORSHIFT32

    try:
        XorShift32(0)
        zero_rejected = False
    except ValueError:
        zero_rejected = True
    checks["A14_ZERO_SEED_REJECTED"] = zero_rejected

    fixture_a = build_fixture()
    fixture_b = build_fixture()
    checks["A15_DETERMINISTIC_FIXTURE"] = serialize(fixture_a) == serialize(fixture_b)

    units = fixture_a["decision_units"]
    checks["A16_UNITS_420"] = len(units) == 420
    checks["A17_PAIRS_210"] = len({u["pair_id"] for u in units}) == 210

    condition_counts = {c: 0 for c in ("control", "treatment", "null")}
    presentation_counts = {"I1_FIRST": 0, "I2_FIRST": 0}
    first_counts = {c: {"I1_FIRST": 0, "I2_FIRST": 0} for c in condition_counts}
    by_pair = {}
    for unit in units:
        condition_counts[unit["condition"]] += 1
        presentation_counts[unit["presentation"]] += 1
        by_pair.setdefault(unit["pair_id"], []).append(unit)

    for pair in by_pair.values():
        first_counts[pair[0]["condition"]][pair[0]["presentation"]] += 1

    checks["A18_CONDITION_BALANCE"] = condition_counts == {"control": 140, "treatment": 140, "null": 140}
    checks["A19_PRESENTATION_BALANCE"] = presentation_counts == {"I1_FIRST": 210, "I2_FIRST": 210}
    checks["A20_FIRST_ORIENTATION_BALANCE"] = all(
        first_counts[c] == {"I1_FIRST": 35, "I2_FIRST": 35}
        for c in first_counts
    )
    checks["A21_PAIR_COMPLEMENT"] = all(
        {p[0]["presentation"], p[1]["presentation"]} == {"I1_FIRST", "I2_FIRST"}
        for p in by_pair.values()
    )
    checks["A22_SCHEMA_FIELD_ORDER"] = all(
        list(u.keys()) == ["decision_id", "pair_id", "condition", "presentation", "context", "available_actions", "future_structure"]
        for u in units
    )
    checks["A23_FUTURE_STRUCTURE_SEMANTICS"] = all(
        u["future_structure"]["successor_realized"] is False
        and u["future_structure"]["future_structure_available"] is (u["condition"] == "treatment")
        for u in units
    )
    checks["A24_SERIALIZATION_DETERMINISTIC"] = serialize(fixture_a) == serialize(fixture_b) and serialize(fixture_a).endswith(b"\n")

    status = "PASS" if all(checks.values()) else "FAIL"
    result = {
        "gate_id": "TI001-V011-FIXTURE-GENERATOR-SELF-TEST-001",
        "status": status,
        "checks": checks,
        "generator_sha": git_blob_sha(generator),
        "generator_id": "TI001-V011-FIXTURE-GENERATOR-001",
        "fixture_id": "TI001-V011-FIXTURE-001",
        "seed": EXPECTED_SEED,
        "presentation_xor": "0x9E3779B9",
        "fixture_generation": "NOT_PERFORMED",
        "scientific_execution": "NOT_PERFORMED",
    }
    Path(args.output).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
