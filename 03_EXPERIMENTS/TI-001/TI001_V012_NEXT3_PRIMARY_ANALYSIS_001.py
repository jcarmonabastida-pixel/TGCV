#!/usr/bin/env python3

import json
import sys
from pathlib import Path

RESULT = Path("03_EXPERIMENTS/TI-001/TI001_V012_NEXT3_EXPLORATORY_SCIENTIFIC_EXECUTION_RESULT_001.json")
POPULATION = Path("03_EXPERIMENTS/TI-001/TI001_V012_NEXT3_ANALYSIS_POPULATION_SPECIFICATION_001.json")
SPECIFICATION = Path("03_EXPERIMENTS/TI-001/TI001_V012_NEXT3_PRIMARY_ANALYSIS_SPECIFICATION_001.json")

EXPECTED_RESULT_SHA256 = "b908abe936bbfd19232a1436f8a308ac5dd23ca7df418c55715520c80ec9f5de"
EXPECTED_POPULATION_SHA256 = "dceb6065a723a37db235b3ea496e087e711f3e8bdb9d7d6731b949d2a22c04f8"
EXPECTED_SPECIFICATION_SHA256 = "9bd8c64594e4e8f853b498cf6d630e5d13668ceba115daef606fdb8225c28daf"

def sha256_file(path):
    import hashlib
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def main():
    for path in (RESULT, POPULATION, SPECIFICATION):
        if not path.exists():
            raise FileNotFoundError(path)

    hashes = {
        "result": sha256_file(RESULT),
        "population": sha256_file(POPULATION),
        "specification": sha256_file(SPECIFICATION),
    }

    expected = {
        "result": EXPECTED_RESULT_SHA256,
        "population": EXPECTED_POPULATION_SHA256,
        "specification": EXPECTED_SPECIFICATION_SHA256,
    }

    for key in expected:
        if hashes[key] != expected[key]:
            raise RuntimeError(
                f"{key} SHA-256 mismatch: expected {expected[key]}, got {hashes[key]}"
            )

    result = json.loads(RESULT.read_text(encoding="utf-8"))
    population = json.loads(POPULATION.read_text(encoding="utf-8"))
    specification = json.loads(SPECIFICATION.read_text(encoding="utf-8"))

    if result["decision_count"] != population["total_decisions"]:
        raise RuntimeError("Decision-count mismatch")

    valid = [
        d for d in result["decisions"]
        if d["validity"] == "VALID"
    ]

    if len(valid) != population["valid_decisions"]:
        raise RuntimeError("Valid-decision count mismatch")

    if specification["analysis_population"] != "validity == VALID":
        raise RuntimeError("Unexpected analysis population rule")

    print(json.dumps({
        "status": "ANALYSIS_INPUT_PREFLIGHT_PASS",
        "result_sha256": hashes["result"],
        "population_sha256": hashes["population"],
        "specification_sha256": hashes["specification"],
        "total_decisions": len(result["decisions"]),
        "valid_decisions": len(valid),
        "invalid_decisions": len(result["decisions"]) - len(valid),
        "analysis_executed": False
    }, indent=2))

    return 0

if __name__ == "__main__":
    raise SystemExit(main())
