#!/usr/bin/env python3
"""TI-001 V012 NEXT3 primary scientific analysis executor.

Executes only the frozen PRIMARY_ANALYSIS_SPECIFICATION_002 model after the
explicit PRIMARY_ANALYSIS_AUTHORIZATION_GATE_001. No scientific model
definition is changed here; the statistical fit is delegated to the frozen
fit_primary_analysis implementation.
"""

import argparse
import hashlib
import importlib.util
import json
import platform
import sys
import warnings
from pathlib import Path

RESULT_SHA256 = "b908abe936bbfd19232a1436f8a308ac5dd23ca7df418c55715520c80ec9f5de"
POPULATION_SHA256 = "dceb6065a723a37db235b3ea496e087e711f3e8bdb9d7d6731b949d2a22c04f8"
SPECIFICATION_SHA256 = "f65737c3d24d2e4c973c0649632abf4247c9004452eed7c08225102b74a52f0f"
IMPLEMENTATION_SHA256 = "1d29894b1ccb49c0dfce8b389fedb3a1f4d7d1bf83d5d38b5d24d5e3802ae22d"
FIXTURE_SHA256 = "0f16ebd02275ed32c481d34f92f704bb375dbe21e90d807483904ca73a9912d0"
AUTH_GATE_ID = "TI001_V012_NEXT3_PRIMARY_ANALYSIS_AUTHORIZATION_GATE_001"
PRE_GATE_ID = "TI001_V012_NEXT3_PRIMARY_ANALYSIS_PRE_EXECUTION_GATE_001"

def sha256_file(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def load_module(path):
    spec = importlib.util.spec_from_file_location("ti001_next3_primary_analysis", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--result", required=True, type=Path)
    parser.add_argument("--population", required=True, type=Path)
    parser.add_argument("--specification", required=True, type=Path)
    parser.add_argument("--implementation", required=True, type=Path)
    parser.add_argument("--authorization", required=True, type=Path)
    parser.add_argument("--pre-gate", required=True, type=Path)
    parser.add_argument("--fixture", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    hashes = {
        "result": sha256_file(args.result),
        "population": sha256_file(args.population),
        "specification": sha256_file(args.specification),
        "implementation": sha256_file(args.implementation),
        "fixture": sha256_file(args.fixture),
    }
    expected = {
        "result": RESULT_SHA256,
        "population": POPULATION_SHA256,
        "specification": SPECIFICATION_SHA256,
        "implementation": IMPLEMENTATION_SHA256,
        "fixture": FIXTURE_SHA256,
    }
    for key, value in expected.items():
        require(hashes[key] == value, f"{key} SHA-256 mismatch: expected {value}, got {hashes[key]}")

    authorization = load_json(args.authorization)
    pre_gate = load_json(args.pre_gate)
    require(authorization["artifact_id"] == AUTH_GATE_ID, "Unexpected authorization gate artifact")
    require(authorization["scientific_execution_authorized"] is True, "Scientific execution is not authorized")
    require(authorization["status"] == "SCIENTIFIC_EXECUTION_AUTHORIZED", "Authorization gate is not PASS")
    require(pre_gate["artifact_id"] == PRE_GATE_ID, "Unexpected pre-execution gate artifact")
    require(pre_gate["status"] == "PRE_EXECUTION_GATE_PASS", "Pre-execution gate is not PASS")
    require(pre_gate["scientific_execution_authorized"] is False, "Pre-execution gate must not itself authorize execution")

    population = load_json(args.population)
    specification = load_json(args.specification)
    require(population["artifact_id"] == "TI001_V012_NEXT3_ANALYSIS_POPULATION_SPECIFICATION_001", "Unexpected population specification")
    require(specification["artifact_id"] == "TI001_V012_NEXT3_PRIMARY_ANALYSIS_SPECIFICATION_002", "Unexpected primary specification")
    require(specification["exploratory_only"] is True and specification["confirmatory"] is False, "NEXT3 primary analysis must remain exploratory")
    require(specification["no_pooling_with_NEXT2"] is True, "NEXT2 pooling is prohibited")

    analysis = load_module(args.implementation)
    fixture_obj, fixture_by_unit = analysis.load_fixture(args.fixture)
    result_obj, decisions = analysis.load_result(args.result)
    rows, invalid = analysis.build_choice_rows(decisions, fixture_by_unit)
    analysis.audit_choice_rows(rows)

    require(len(decisions) == population["total_decisions"] == 23040, "Decision count mismatch")
    require(len(decisions) - invalid == population["valid_decisions"] == 22649, "Valid decision count mismatch")
    require(len(rows) == 90596, "Analysis alternative count mismatch")
    require(len({row["unit_id"] for row in rows}) == 22649, "Choice-set count mismatch")
    require(fixture_obj["unit_count"] == 23040, "Fixture unit count mismatch")

    primary_module = load_module(args.implementation)
    captured_warnings = []
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        fit = primary_module.fit_primary_analysis(rows)
        captured_warnings = [
            {"category": w.category.__name__, "message": str(w.message)}
            for w in caught
        ]

    output = {
        "artifact_id": "TI001_V012_NEXT3_PRIMARY_ANALYSIS_RESULT_001",
        "record_type": "TGCV_TI001_V012_NEXT3_PRIMARY_ANALYSIS_RESULT",
        "status": "PRIMARY_STATISTICAL_ANALYSIS_COMPLETE",
        "analysis_specification": specification["artifact_id"],
        "analysis_specification_sha256": hashes["specification"],
        "authorization_gate": authorization["artifact_id"],
        "pre_execution_gate": pre_gate["artifact_id"],
        "source_result_artifact": "TI001_V012_NEXT3_EXPLORATORY_SCIENTIFIC_EXECUTION_RESULT_001",
        "source_result_sha256": hashes["result"],
        "population_specification": population["artifact_id"],
        "population_sha256": hashes["population"],
        "analysis_implementation_sha256": hashes["implementation"],
        "fixture_version": fixture_obj["version"],
        "fixture_sha256": hashes["fixture"],
        "analysis_population": "validity == VALID",
        "total_decisions": len(decisions),
        "valid_decisions": len(decisions) - invalid,
        "invalid_decisions_excluded": invalid,
        "analysis_alternatives": len(rows),
        "choice_sets": len({row["unit_id"] for row in rows}),
        "alternatives_per_choice_set": 4,
        "model": fit,
        "execution": {
            "scientific_execution_authorized": True,
            "exploratory_only": True,
            "confirmatory": False,
            "next2_pooling": False,
            "mapping_condition_in_model": False,
            "value_signal": False,
            "utility_signal": False,
            "reward_signal": False,
            "performance_signal": False,
        },
        "runtime": {
            "python": sys.version,
            "platform": platform.platform(),
            "pandas": __import__("pandas").__version__,
            "numpy": __import__("numpy").__version__,
            "scipy": __import__("scipy").__version__,
            "statsmodels": __import__("statsmodels").__version__,
        },
        "warnings": captured_warnings,
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "status": output["status"],
        "valid_decisions": output["valid_decisions"],
        "analysis_alternatives": output["analysis_alternatives"],
        "choice_sets": output["choice_sets"],
        "lr_statistic": fit["primary_test"]["lr_statistic"],
        "degrees_of_freedom": fit["primary_test"]["degrees_of_freedom"],
        "p_value": fit["primary_test"]["p_value"],
        "warnings": len(captured_warnings),
    }, sort_keys=True))

if __name__ == "__main__":
    main()
