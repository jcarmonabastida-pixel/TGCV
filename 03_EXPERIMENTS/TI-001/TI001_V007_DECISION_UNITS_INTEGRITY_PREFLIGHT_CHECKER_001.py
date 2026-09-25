#!/usr/bin/env python3
"""TI-001 V007 decision-units integrity preflight checker.

Infrastructure/design gate only. Never performs scientific execution.
The fixture stores its version under "version"; the derived decision-units
artifact stores the bound value under "fixture_version".
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

EXPECTED_FIXTURE_ID = "TI001-v007-candidate-001"
EXPECTED_FIXTURE_BLOB_SHA = "663383b27b567d73757ac967986d0b9b949dc50e"
EXPECTED_CONDITIONS = {"control", "treatment", "null"}
EXPECTED_DECISIONS = 420
EXPECTED_PER_CONDITION = 140

def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def main(argv=None):
    p = argparse.ArgumentParser()
    p.add_argument("--fixture", required=True)
    p.add_argument("--decision-units", required=True)
    p.add_argument("--output", required=True)
    args = p.parse_args(argv)

    fixture = load(args.fixture)
    units = load(args.decision_units)
    decision_units = units.get("decision_units", [])
    instances = units.get("instances", [])
    checks = {}

    checks["decision_units_420"] = len(decision_units) == EXPECTED_DECISIONS
    checks["instances_420"] = len(instances) == EXPECTED_DECISIONS
    checks["decision_ids_unique"] = len({u.get("decision_id") for u in decision_units}) == EXPECTED_DECISIONS
    checks["decision_unit_schema"] = all(set(u.keys()) == {"decision_id", "condition"} for u in decision_units)

    counts = {c: sum(u.get("condition") == c for u in decision_units) for c in EXPECTED_CONDITIONS}
    checks["conditions_balanced"] = set(counts) == EXPECTED_CONDITIONS and all(n == EXPECTED_PER_CONDITION for n in counts.values())
    checks["condition_values_valid"] = all(u.get("condition") in EXPECTED_CONDITIONS for u in decision_units)
    checks["instance_ids_unique"] = len({i.get("instance_id") for i in instances}) == EXPECTED_DECISIONS
    checks["instance_pair_variant_traceability"] = all(i.get("pair_id") and i.get("variant") in {"I1", "I2"} for i in instances)
    checks["condition_matches_fixture"] = all(any(p.get("pair_id") == i.get("pair_id") and p.get("condition") == i.get("condition") for p in fixture.get("pairs", [])) for i in instances)

    # Correct binding criterion: artifact.fixture_version must match fixture.version.
    checks["fixture_id_binding"] = units.get("fixture_id") == fixture.get("fixture_id") == EXPECTED_FIXTURE_ID
    checks["fixture_version_binding"] = units.get("fixture_version") == fixture.get("version")
    checks["fixture_blob_binding"] = units.get("fixture_sha256") == EXPECTED_FIXTURE_BLOB_SHA

    checks["agent_identity_hidden"] = all(i.get("audit", {}).get("condition_hidden") is True and i.get("audit", {}).get("pair_id_hidden") is True and i.get("audit", {}).get("variant_hidden") is True for i in instances)
    checks["treatment_future_structure"] = all(isinstance(i.get("audit", {}).get("expected_future_t_acc", {}).get("A"), list) and isinstance(i.get("audit", {}).get("expected_future_t_acc", {}).get("B"), list) for i in instances if i.get("condition") == "treatment")
    checks["non_treatment_no_future_structure"] = all(i.get("audit", {}).get("future_structure_withheld") is True for i in instances if i.get("condition") != "treatment")
    checks["successor_not_realised"] = all(i.get("audit", {}).get("successor_realised_before_decision") is False for i in instances)
    checks["scientific_execution_absent"] = units.get("scientific_execution") == "NOT_PERFORMED"

    out = {
        "record_type": "TGCV_TI001_V007_DECISION_UNITS_INTEGRITY_PREFLIGHT",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "scientific_execution": "NOT_PERFORMED",
        "checks": checks,
        "condition_counts": counts,
        "binding_criterion": "decision_units.fixture_version == fixture.version"
    }
    Path(args.output).write_text(json.dumps(out, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(out, indent=2, sort_keys=True))
    return 0 if out["status"] == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
