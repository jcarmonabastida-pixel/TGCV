#!/usr/bin/env python3
"""TI-001 V012 NEXT3 primary analysis adapter.

Implements the frozen NEXT3 PRIMARY_ANALYSIS_SPECIFICATION_002 data contract.
No NEXT2 result, model, or statistical definition is imported.

This stage audits and transforms the analysis input only. It does not fit or
execute the primary statistical models.
"""

import argparse
import hashlib
import json
from pathlib import Path

SPEC_ID = "TI001_V012_NEXT3_PRIMARY_ANALYSIS_SPECIFICATION_002"
SPEC_SHA256 = "f65737c3d24d2e4c973c0649632abf4247c9004452eed7c08225102b74a52f0f"
FIXTURE_ID = "TI001_V012_NEXT3_CANDIDATE_FIXTURE_003"
FIXTURE_VERSION = "NEXT3_v003"
FIXTURE_SHA256 = "0f16ebd02275ed32c481d34f92f704bb375dbe21e90d807483904ca73a9912d0"
ACTIONS = ("A", "B", "C", "D")
PROFILE_IDS = ("slot_1", "slot_2", "slot_3", "slot_4")
REQUIRED_DECISION_FIELDS = (
    "unit_id", "domain", "operationalisation", "presentation",
    "permutation_index", "replicate", "parsed_action", "validity",
)

def sha256_bytes(data):
    return hashlib.sha256(data).hexdigest()

def load_json(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))

def load_fixture(path):
    raw = Path(path).read_bytes()
    if sha256_bytes(raw) != FIXTURE_SHA256:
        raise ValueError("Fixture SHA-256 does not match frozen NEXT3_v003 binding.")
    obj = json.loads(raw.decode("utf-8"))
    if obj.get("fixture_id") != FIXTURE_ID or obj.get("version") != FIXTURE_VERSION:
        raise ValueError("Fixture identity/version does not match frozen binding.")
    rows = obj.get("rows")
    if not isinstance(rows, list) or len(rows) != 23040:
        raise ValueError("Fixture row count is not the frozen 23040.")
    by_unit = {}
    for row in rows:
        unit_id = row["unit_id"]
        if unit_id in by_unit:
            raise ValueError(f"Duplicate unit_id: {unit_id}")
        f = row.get("f")
        if set(f or {}) != set(ACTIONS) or sorted(f.values()) != sorted(PROFILE_IDS):
            raise ValueError(f"Invalid f bijection in {unit_id}")
        by_unit[unit_id] = row
    return obj, by_unit

def load_result(path):
    obj = load_json(path)
    decisions = obj.get("decisions")
    if not isinstance(decisions, list):
        raise ValueError("Scientific result must contain a decisions list.")
    if obj.get("scientific_execution") is not True:
        raise ValueError("Input is not marked scientific_execution=true.")
    for i, decision in enumerate(decisions):
        missing = [k for k in REQUIRED_DECISION_FIELDS if k not in decision]
        if missing:
            raise ValueError(f"Decision {i} missing fields: {missing}")
    return obj, decisions

def build_choice_rows(decisions, fixture_by_unit):
    rows = []
    invalid = 0
    for decision in decisions:
        unit_id = decision["unit_id"]
        fixture = fixture_by_unit.get(unit_id)
        if fixture is None:
            raise ValueError(f"Decision unit_id absent from frozen fixture: {unit_id}")
        if decision["validity"] != "VALID":
            invalid += 1
            continue
        selected = decision["parsed_action"]
        if selected not in ACTIONS:
            raise ValueError(f"VALID decision has invalid parsed_action: {selected}")
        for action in ACTIONS:
            rows.append({
                "unit_id": unit_id,
                "action_identity": action,
                "profile_id": fixture["f"][action],
                "chosen": int(action == selected),
                "domain": decision["domain"],
                "operationalisation": decision["operationalisation"],
                "presentation": decision["presentation"],
                "permutation_index": decision["permutation_index"],
                "replicate": decision["replicate"],
            })
    return rows, invalid

def audit_choice_rows(rows):
    by_unit = {}
    for row in rows:
        by_unit.setdefault(row["unit_id"], []).append(row)
    for unit_id, group in by_unit.items():
        if len(group) != 4:
            raise ValueError(f"Choice set {unit_id} does not contain four alternatives.")
        if sum(row["chosen"] for row in group) != 1:
            raise ValueError(f"Choice set {unit_id} does not contain exactly one choice.")
        if {row["action_identity"] for row in group} != set(ACTIONS):
            raise ValueError(f"Action identities incomplete in {unit_id}.")
        if {row["profile_id"] for row in group} != set(PROFILE_IDS):
            raise ValueError(f"Profile identities incomplete in {unit_id}.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--result", required=True, type=Path)
    parser.add_argument("--fixture", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    fixture, fixture_by_unit = load_fixture(args.fixture)
    result, decisions = load_result(args.result)
    declared_fixture_sha = result.get("fixture", {}).get("sha256")
    if declared_fixture_sha not in (None, FIXTURE_SHA256):
        raise ValueError("Scientific result declares an inconsistent fixture SHA-256.")

    rows, invalid = build_choice_rows(decisions, fixture_by_unit)
    audit_choice_rows(rows)

    output = {
        "artifact_id": "TI001_V012_NEXT3_PRIMARY_ANALYSIS_INPUT_AUDIT_001",
        "record_type": "TGCV_TI001_V012_NEXT3_PRIMARY_ANALYSIS_INPUT_AUDIT",
        "analysis_specification": SPEC_ID,
        "analysis_specification_sha256": SPEC_SHA256,
        "fixture_id": FIXTURE_ID,
        "fixture_version": FIXTURE_VERSION,
        "fixture_sha256": FIXTURE_SHA256,
        "decision_count": len(decisions),
        "valid_decision_count": len(decisions) - invalid,
        "invalid_decision_count": invalid,
        "alternative_row_count": len(rows),
        "unit_count": len({row["unit_id"] for row in rows}),
        "next2_pooling": False,
        "scientific_execution": False,
        "status": "INPUT_AUDIT_COMPLETE_MODEL_NOT_EXECUTED",
    }
    args.output.write_text(
        json.dumps(output, indent=2, sort_keys=True) + "\n", encoding="utf-8"
    )

if __name__ == "__main__":
    main()
