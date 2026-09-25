#!/usr/bin/env python3
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GENERATOR = ROOT / "03_EXPERIMENTS" / "TI-001" / "TI001_V008_GENERATOR_001.py"
SCHEMA = ROOT / "03_EXPERIMENTS" / "TI-001" / "TI001_V008_DECISION_UNIT_SCHEMA_SPECIFICATION_001.md"
PREFLIGHT_ID = "TI001-V008-GENERATOR-SCHEMA-BINDING-PREFLIGHT-001"
GENERATOR_ID = "TI001-V008-FIXTURE-GENERATOR-001"
SCHEMA_ID = "TI001-V008-DU-SCHEMA-001"
EXPECTED_SCHEMA_SHA = "d9539790452b047bc845a19bdcf50b8713a42b2a"
EXPECTED_GENERATOR_SHA = "f345c41371a189c43b69b707b49b7eb17d140f55"

def git_blob_sha1(data):
    return hashlib.sha1((f"blob {len(data)}\0").encode() + data).hexdigest()

def main():
    checks = {}
    checks["generator_exists"] = GENERATOR.exists()
    checks["schema_exists"] = SCHEMA.exists()
    if not (GENERATOR.exists() and SCHEMA.exists()):
        checks["source_hashes"] = False
        print(json.dumps({"preflight_id": PREFLIGHT_ID, "checks": checks, "scientific_execution": "NOT_PERFORMED", "fixture_generated": False, "status": "FAIL"}, indent=2, sort_keys=True))
        raise SystemExit(1)
    generator = GENERATOR.read_bytes()
    schema = SCHEMA.read_bytes()
    gt = generator.decode("utf-8")
    st = schema.decode("utf-8")
    generator_sha = git_blob_sha1(generator)
    schema_sha = git_blob_sha1(schema)
    checks["generator_blob_sha_binding"] = generator_sha == EXPECTED_GENERATOR_SHA
    checks["schema_blob_sha_binding"] = schema_sha == EXPECTED_SCHEMA_SHA
    checks["generator_id"] = GENERATOR_ID in gt
    checks["schema_id"] = SCHEMA_ID in st
    checks["self_test_vectors"] = all(x in gt for x in ["SEED1_VECTORS", "CONDITION_VECTORS", "PRESENTATION_VECTORS"])
    checks["self_test_status"] = '"status": "PASS"' in gt
    checks["materialization_210_pairs"] = "range(1, 211)" in gt
    checks["materialization_420_decisions"] = "decision_number" in gt and "D{decision_number:03d}" in gt
    checks["condition_allocation"] = '"control"] * 70' in gt and '"treatment"] * 70' in gt and '"null"] * 70' in gt
    checks["presentation_allocation"] = '"I1_FIRST"] * 105' in gt and '"I2_FIRST"] * 105' in gt
    checks["complementary_pair_presentation"] = '"I1_FIRST", "I2_FIRST") if first == "I1_FIRST" else ("I2_FIRST", "I1_FIRST")' in gt
    checks["seven_fields"] = all(f'"{x}"' in gt for x in ["decision_id", "pair_id", "condition", "presentation", "context", "available_actions", "future_structure"])
    checks["nested_context_order"] = '"context": {"items": items, "item_count": 2}' in gt
    checks["available_actions"] = '"available_actions": ["A", "B"]' in gt
    checks["future_structure"] = '"successor_realized": False, "future_structure_available": condition == "treatment"' in gt
    checks["top_level_order"] = '"fixture_id": FIXTURE_ID, "schema_id": SCHEMA_ID, "generator_id": GENERATOR_ID, "seed": SEED, "decision_units": records' in gt
    checks["compact_utf8_lf"] = 'ensure_ascii=False, separators=(",", ":"), sort_keys=False) + "\\n"' in gt
    checks["fixture_sha256"] = 'hashlib.sha256(fixture_bytes).hexdigest()' in gt
    checks["manifest_binding"] = '"schema_blob_sha1": schema_sha, "generator_blob_sha1": generator_sha' in gt
    checks["explicit_binding_manifest"] = 'args.binding_manifest is None' in gt and 'binding manifest does not match' in gt
    checks["executor2_independence"] = "Executor-2" in st and "MUST NOT read" in st
    checks["scientific_not_performed"] = '"scientific_execution": "NOT_PERFORMED"' in gt
    checks["generation_requires_binding"] = 'requires --binding-manifest' in gt
    checks["schema_order_reconciliation"] = "the first decision uses the pair's deterministically shuffled presentation assignment" in st and "the second decision uses the complementary presentation assignment" in st and "pair-level orientation is determined by the approved presentation stream" in st\n    checks["generation_not_performed"] = not (ROOT / "03_EXPERIMENTS/TI-001/generated/V008/TI001_V008_FIXTURE_001.json").exists()
    status = "PASS" if all(checks.values()) else "FAIL"
    result = {"preflight_id": PREFLIGHT_ID, "expected_generator_blob_sha1": EXPECTED_GENERATOR_SHA, "expected_schema_blob_sha1": EXPECTED_SCHEMA_SHA, "actual_generator_blob_sha1": generator_sha, "actual_schema_blob_sha1": schema_sha, "checks": checks, "scientific_execution": "NOT_PERFORMED", "fixture_generated": False, "status": status}
    print(json.dumps(result, indent=2, sort_keys=True))
    raise SystemExit(0 if status == "PASS" else 1)

if __name__ == "__main__":
    main()