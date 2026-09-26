#!/usr/bin/env python3
import argparse
import json
import subprocess
from pathlib import Path

EXPECTED_GENERATOR_SHA = "15257bde7007ee861e4217d16ded40d2a27e92c8"
EXPECTED_SEED = "20260926"
EXPECTED_GENERATOR_ID = "TI001-V011-FIXTURE-GENERATOR-001"
EXPECTED_FIXTURE_ID = "TI001-V011-FIXTURE-001"
EXPECTED_SCHEMA_ID = "TI001-V011-DU-SCHEMA-001"


def git_blob_sha(path):
    return subprocess.check_output(
        ["git", "hash-object", path], text=True
    ).strip()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--generator", required=True)
    parser.add_argument("--schema", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    generator = Path(args.generator)
    schema = Path(args.schema)
    source = generator.read_text(encoding="utf-8")
    schema_source = schema.read_text(encoding="utf-8")

    checks = {
        "A1_GENERATOR_EXISTS": generator.exists(),
        "A2_SCHEMA_EXISTS": schema.exists(),
        "A3_GENERATOR_GIT_BLOB_SHA": git_blob_sha(generator) == EXPECTED_GENERATOR_SHA,
        "A4_SEED_FROZEN": f"SEED = {EXPECTED_SEED}" in source,
        "A5_GENERATOR_ID": EXPECTED_GENERATOR_ID in source,
        "A6_FIXTURE_ID": EXPECTED_FIXTURE_ID in source,
        "A7_SCHEMA_ID": EXPECTED_SCHEMA_ID in source,
        "A8_XORSHIFT32_PRESENT": "class XorShift32" in source,
        "A9_FISHER_YATES_PRESENT": "def fisher_yates" in source,
        "A10_NO_EXTERNAL_API": "OpenAI(" not in source and "requests." not in source,
        "A11_NO_MODEL_EXECUTION": "responses.create" not in source and "chat.completions" not in source,
        "A12_NO_RESULT_CONSUMPTION": "EXECUTOR_1_RESULT" not in source and "EXECUTOR_2_RESULT" not in source,
        "A13_NO_SCIENTIFIC_ANALYSIS": "scientific_analysis" not in source,
        "A14_SCHEMA_SEMANTICS_BOUND": EXPECTED_SCHEMA_ID in schema_source,
        "A15_POPULATION_420": "420" in source and "210" in source,
        "A16_CONDITION_BALANCE": '"control": 70' in source and '"treatment": 70' in source and '"null": 70' in source,
        "A17_PRESENTATION_BALANCE": '"I1_FIRST": 210' in source and '"I2_FIRST": 210' in source,
        "A18_PAIR_COMPLEMENT": '"I2_FIRST" if first == "I1_FIRST" else "I1_FIRST"' in source,
        "A19_CANONICAL_SERIALIZATION": 'separators=(",", ":")' in source and 'encode("utf-8")' in source,
        "A20_GENERATION_ONLY": '"scientific_execution": "NOT_PERFORMED"' in source,
    }

    status = "PASS" if all(checks.values()) else "FAIL"
    result = {
        "gate_id": "TI001-V011-FIXTURE-GENERATOR-IDENTITY-PREFLIGHT-001",
        "status": status,
        "checks": checks,
        "generator_sha": git_blob_sha(generator),
        "schema_sha": git_blob_sha(schema),
        "generator_id": EXPECTED_GENERATOR_ID,
        "fixture_id": EXPECTED_FIXTURE_ID,
        "schema_id": EXPECTED_SCHEMA_ID,
        "seed": int(EXPECTED_SEED),
        "fixture_generation": "NOT_PERFORMED",
        "scientific_execution": "NOT_PERFORMED",
    }
    Path(args.output).write_text(
        json.dumps(result, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
