#!/usr/bin/env python3
"""TI-001 V008 Provider–Contract Compatibility Preflight 001."""

from pathlib import Path
import hashlib
import re

PROVIDER = Path("03_EXPERIMENTS/TI-001/TI001_V008_DECISION_AGENT_PROVIDER_001.py")
SPEC = Path("03_EXPERIMENTS/TI-001/TI001_V008_PROVIDER_CONTRACT_COMPATIBILITY_SPECIFICATION_001.md")
EXPECTED_PROVIDER_BLOB = "c7d066de3481143d878f06bb2c1d791cb7dc54e1"
EXPECTED_SCHEMA_BLOB = "d9539790452b047bc845a19bdcf50b8713a42b2a"
EXPECTED_PROVIDER_ID = "TI001-V008-DECISION-AGENT-PROVIDER-001"
EXPECTED_SCHEMA_ID = "TI001-V008-DU-SCHEMA-001"

def check(ok, name, checks):
    checks[name] = bool(ok)

def main():
    checks = {}
    text = PROVIDER.read_text(encoding="utf-8")
    spec = SPEC.read_text(encoding="utf-8")

    check(PROVIDER.exists(), "provider_exists", checks)
    check(SPEC.exists(), "spec_exists", checks)
    check(EXPECTED_PROVIDER_ID in text, "provider_id", checks)
    check(EXPECTED_SCHEMA_ID in text, "schema_id", checks)
    check(EXPECTED_SCHEMA_BLOB in text, "schema_blob_binding", checks)

    for marker, name in [
        ('HIDDEN_FIELDS = frozenset(("decision_id", "pair_id", "condition", "presentation"))', "hidden_fields"),
        ('VISIBLE_FIELDS = frozenset(("context", "available_actions", "future_structure"))', "visible_fields"),
        ('unit["available_actions"] != ["A", "B"]', "available_actions"),
        ('set(context) != {"items", "item_count"}', "context_fields"),
        ('context["item_count"] != len(context["items"])', "context_item_count"),
        ('set(future) != {"successor_realized", "future_structure_available"}', "future_structure_fields"),
        ('future["successor_realized"]', "successor_not_realized"),
        ('selected not in ALLOWED_ACTIONS', "response_validation"),
    ]:
        check(marker in text, name, checks)

    check("V007" not in text, "no_v007_binding", checks)
    check("scientific execution requires" in text, "scientific_execution_gate", checks)
    check("model/API" not in text, "no_model_api_execution_in_provider", checks)
    check("Fixture generated:** false" in spec, "fixture_not_generated", checks)
    check("Scientific execution:** NOT_PERFORMED" in spec, "scientific_not_performed", checks)

    # Source-level blob verification uses the canonical Git blob algorithm.
    data = PROVIDER.read_bytes()
    header = f"blob {len(data)}\0".encode("utf-8")
    blob_sha = hashlib.sha1(header + data).hexdigest()
    check(blob_sha == EXPECTED_PROVIDER_BLOB, "provider_blob_sha", checks)

    status = "PASS" if all(checks.values()) else "FAIL"
    result = {
        "preflight_id": "TI001-V008-PROVIDER-CONTRACT-COMPATIBILITY-PREFLIGHT-001",
        "provider_id": EXPECTED_PROVIDER_ID,
        "provider_blob_sha1": blob_sha,
        "expected_provider_blob_sha1": EXPECTED_PROVIDER_BLOB,
        "schema_id": EXPECTED_SCHEMA_ID,
        "expected_schema_blob_sha1": EXPECTED_SCHEMA_BLOB,
        "checks": checks,
        "fixture_generated": False,
        "scientific_execution": "NOT_PERFORMED",
        "status": status,
    }
    print(__import__("json").dumps(result, indent=2, sort_keys=True))
    return 0 if status == "PASS" else 1

if __name__ == "__main__":
    raise SystemExit(main())
