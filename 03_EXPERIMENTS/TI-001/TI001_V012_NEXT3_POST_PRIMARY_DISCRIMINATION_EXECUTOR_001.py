#!/usr/bin/env python3
"""TI-001 V012 NEXT3 post-primary Q1-Q5 scientific-analysis executor."""

import argparse
import hashlib
import importlib.util
import json
import platform
import sys
import warnings
from pathlib import Path

SPECIFICATION_SHA256 = "f65737c3d24d2e4c973c0649632abf4247c9004452eed7c08225102b74a52f0f"
IMPLEMENTATION_SHA256 = None
FIXTURE_SHA256 = "0f16ebd02275ed32c481d34f92f704bb375dbe21e90d807483904ca73a9912d0"
EXECUTION_RESULT_SHA256 = "b908abe936bbfd19232a1436f8a308ac5dd23ca7df418c55715520c80ec9f5de"
MATRIX_AUDIT_ID = "TI001_V012_NEXT3_POST_PRIMARY_DISCRIMINATION_MATRIX_CONSTRUCTION_AUDIT_001"
GATE_ID = "TI001_V012_NEXT3_POST_PRIMARY_DISCRIMINATION_PRE_EXECUTION_GATE_006"
SPEC_ID = "TI001_V012_NEXT3_POST_PRIMARY_DISCRIMINATION_ANALYSIS_SPECIFICATION_002"

def sha256_file(path):
    h = hashlib.sha256()
    with Path(path).open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def load_module(path):
    spec = importlib.util.spec_from_file_location("ti001_next3_post_primary_impl", path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

def require(condition, message):
    if not condition:
        raise RuntimeError(message)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--result", required=True, type=Path)
    parser.add_argument("--specification", required=True, type=Path)
    parser.add_argument("--implementation", required=True, type=Path)
    parser.add_argument("--gate", required=True, type=Path)
    parser.add_argument("--matrix-audit", required=True, type=Path)
    parser.add_argument("--fixture", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    hashes = {
        "result": sha256_file(args.result),
        "specification": sha256_file(args.specification),
        "implementation": sha256_file(args.implementation),
        "fixture": sha256_file(args.fixture),
    }
    expected = {"result": EXECUTION_RESULT_SHA256, "specification": SPECIFICATION_SHA256, "fixture": FIXTURE_SHA256}
    for key, value in expected.items():
        require(hashes[key] == value, f"{key} SHA-256 mismatch: expected {value}, got {hashes[key]}")

    specification = load_json(args.specification)
    gate = load_json(args.gate)
    audit = load_json(args.matrix_audit)
    result_obj = load_json(args.result)
    fixture_obj = load_json(args.fixture)

    require(specification["artifact_id"] == SPEC_ID, "Unexpected specification artifact")
    require(specification["status"] == "SPECIFICATION_COMPLETE_NOT_EXECUTION_AUTHORIZED", "Unexpected specification status")
    require(gate["artifact_id"] == GATE_ID, "Unexpected post-primary gate")
    require(gate["status"] == "AUTHORIZED_FOR_SCIENTIFIC_EXECUTION", "Post-primary gate is not authorized")
    require(gate["decision"] == "ALLOW_AND_EXECUTE", "Post-primary gate decision is not ALLOW_AND_EXECUTE")
    require(gate["governance"]["scientific_execution_authorized"] is True, "Scientific execution is not authorized")
    require(gate["governance"]["exploratory"] is True and gate["governance"]["confirmatory"] is False, "Execution status mismatch")
    require(audit["artifact_id"] == MATRIX_AUDIT_ID, "Unexpected matrix audit artifact")
    require(audit["status"] == "MATRIX_CONSTRUCTION_AUDIT_PASS", "Matrix construction audit is not PASS")
    require(audit["scientific_fitting_performed"] is False, "Matrix audit must precede scientific fitting")

    require(fixture_obj["fixture_id"] == "TI001_V012_NEXT3_CANDIDATE_FIXTURE_003", "Unexpected fixture")
    require(fixture_obj["version"] == "NEXT3_v003", "Unexpected fixture version")
    require(fixture_obj["unit_count"] == 23040, "Unexpected fixture unit count")
    require(len(fixture_obj["rows"]) == 23040, "Unexpected fixture row count")
    fixture_by_unit = {row["unit_id"]: row for row in fixture_obj["rows"]}
    require(len(fixture_by_unit) == 23040, "Fixture unit_id uniqueness failure")

    decisions = result_obj["decisions"]
    require(len(decisions) == 23040, "Unexpected execution decision count")
    valid = [d for d in decisions if d["validity"] == "VALID"]
    invalid = len(decisions) - len(valid)
    require(len(valid) == 22649, "Unexpected valid population")
    require(invalid == 391, "Unexpected invalid population")

    rows = []
    for decision in valid:
        unit_id = decision["unit_id"]
        fixture_row = fixture_by_unit.get(unit_id)
        require(fixture_row is not None, f"Missing fixture row for {unit_id}")
        f = fixture_row["f"]
        require(set(f.keys()) == {"A", "B", "C", "D"}, f"Unexpected action mapping for {unit_id}")
        require(sorted(f.values()) == ["slot_1", "slot_2", "slot_3", "slot_4"], f"Non-bijective mapping for {unit_id}")
        parsed = decision["parsed_action"]
        condition = fixture_row["mapping_condition_metadata"]
        require(condition in {"INFORMATIVE", "SURFACE_PERMUTED", "UNINFORMATIVE_NULL", "CONTRADICTORY"},
                f"Unexpected mapping condition for {unit_id}: {condition}")
        for action in ["A", "B", "C", "D"]:
            rows.append({
                "unit_id": unit_id,
                "action_identity": action,
                "profile_id": f[action],
                "chosen": int(parsed == action),
                "condition": condition,
                "domain": decision["domain"],
                "operationalisation": decision["operationalisation"],
                "presentation": decision["presentation"],
                "permutation_index": decision["permutation_index"],
                "replicate": decision["replicate"],
            })

    require(len(rows) == 90596, "Unexpected long-form analysis cardinality")
    by_unit = {}
    for row in rows:
        by_unit.setdefault(row["unit_id"], []).append(row)
    require(len(by_unit) == 22649, "Unexpected number of valid choice sets")
    require(all(len(v) == 4 and sum(r["chosen"] for r in v) == 1 for v in by_unit.values()),
            "Invalid choice-set structure")

    implementation = load_module(args.implementation)
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter("always")
        analysis = implementation.run_post_primary(rows)
        captured_warnings = [{"category": w.category.__name__, "message": str(w.message)} for w in caught]

    tests = [
        analysis["Q1"]["primary_contrast"],
        analysis["Q2"]["primary_contrast"],
        *analysis["Q3"]["primary_contrasts"],
        analysis["Q4"]["domain"]["primary_contrast"],
        analysis["Q4"]["operationalisation"]["primary_contrast"],
        analysis["Q5"]["primary_contrast"],
    ]
    require(len(tests) == 8, "Expected exactly eight primary inferential tests")
    require(all("holm_adjusted_p_value" in t for t in tests), "Holm adjustment missing")

    output = {
        "artifact_id": "TI001_V012_NEXT3_POST_PRIMARY_DISCRIMINATION_ANALYSIS_RESULT_001",
        "record_type": "TGCV_TI001_V012_NEXT3_POST_PRIMARY_DISCRIMINATION_ANALYSIS_RESULT",
        "status": "POST_PRIMARY_Q1_Q5_ANALYSIS_COMPLETE",
        "analysis_specification": SPEC_ID,
        "analysis_specification_sha256": hashes["specification"],
        "pre_execution_gate": GATE_ID,
        "matrix_construction_audit": MATRIX_AUDIT_ID,
        "fixture_version": fixture_obj["version"],
        "fixture_sha256": hashes["fixture"],
        "execution_result_sha256": hashes["result"],
        "implementation_sha256": hashes["implementation"],
        "population_rule": "validity == VALID",
        "total_decisions": 23040,
        "valid_decisions": 22649,
        "invalid_decisions_excluded": 391,
        "analysis_alternatives": 90596,
        "choice_sets": 22649,
        "primary_inferential_contrasts": 8,
        "multiple_comparison_adjustment": "Holm",
        "exploratory": True,
        "confirmatory": False,
        "next2_pooling": False,
        "value_signal": False,
        "utility_signal": False,
        "reward_signal": False,
        "performance_signal": False,
        "primary_analysis_modified": False,
        "analysis": analysis,
        "runtime": {
            "python": sys.version,
            "platform": platform.platform(),
            "numpy": __import__("numpy").__version__,
            "scipy": __import__("scipy").__version__,
            "pandas": __import__("pandas").__version__,
            "statsmodels": __import__("statsmodels").__version__,
        },
        "warnings": captured_warnings,
    }
    args.output.write_text(json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"status": output["status"], "valid_decisions": output["valid_decisions"],
                      "choice_sets": output["choice_sets"], "primary_inferential_contrasts": output["primary_inferential_contrasts"],
                      "warnings": len(captured_warnings)}, sort_keys=True))

if __name__ == "__main__":
    main()
