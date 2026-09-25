#!/usr/bin/env python3
"""TI-001 V008 Executor-1 scientific executor boundary.

Scientific execution is intentionally blocked unless an explicit authorization
record is supplied by the separate execution gate.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

FIXTURE_ID = "TI001-V008-FIXTURE-001"
SCHEMA_ID = "TI001-V008-DU-SCHEMA-001"
PROVIDER_ID = "TI001-V008-DECISION-AGENT-PROVIDER-001"
FIXTURE_SHA256 = "dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9"
PROVIDER_BLOB_SHA1 = "c7d066de3481143d878f06bb2c1d791cb7dc54e1"
MODEL_ID = "gpt-5.6-luna"
API_SURFACE = "Responses API"
VALID_OUTPUTS = {"A", "B"}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_fixture(path: Path):
    raw = path.read_bytes()
    actual = sha256_bytes(raw)
    if actual != FIXTURE_SHA256:
        raise SystemExit(f"fixture SHA-256 mismatch: {actual}")
    return json.loads(raw), actual


def visible_input(unit):
    return {
        "context": unit["context"],
        "available_actions": unit["available_actions"],
        "future_structure": unit["future_structure"],
    }


def validate_boundary(fixture):
    if fixture.get("fixture_id") != FIXTURE_ID:
        return False, "fixture_id"
    units = fixture.get("decision_units", [])
    if len(units) != 420:
        return False, "decision_count"
    for unit in units:
        if set(visible_input(unit)) != {"context", "available_actions", "future_structure"}:
            return False, "visible_fields"
        if set(unit["available_actions"]) != {"A", "B"}:
            return False, "actions"
        if unit["future_structure"].get("successor_realized") is not False:
            return False, "successor"
    return True, None


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture", required=True)
    parser.add_argument("--authorization", default=None)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()

    fixture, fixture_sha256 = load_fixture(Path(args.fixture))
    boundary_ok, reason = validate_boundary(fixture)

    # Scientific execution is forbidden unless a separate authorization record
    # explicitly authorizes this exact V008 executor and runtime binding.
    authorized = False
    authorization = None
    if args.authorization:
        authorization = json.loads(Path(args.authorization).read_text(encoding="utf-8"))
        authorized = (
            authorization.get("scientific_execution") == "AUTHORIZED"
            and authorization.get("executor_id") == "TI001-V008-EXECUTOR-1-001"
        )

    result = {
        "executor_id": "TI001-V008-EXECUTOR-1-001",
        "fixture_id": FIXTURE_ID,
        "schema_id": SCHEMA_ID,
        "provider_id": PROVIDER_ID,
        "provider_blob_sha1": PROVIDER_BLOB_SHA1,
        "model_id": MODEL_ID,
        "api_surface": API_SURFACE,
        "fixture_sha256": fixture_sha256,
        "boundary_checks": {
            "fixture_identity": boundary_ok and reason != "fixture_id",
            "decision_count": boundary_ok and reason != "decision_count",
            "visible_fields": boundary_ok and reason != "visible_fields",
            "action_space_ab": boundary_ok and reason != "actions",
            "no_successor_realization": boundary_ok and reason != "successor",
        },
        "scientific_execution": "NOT_PERFORMED" if not authorized else "AUTHORIZED",
        "authorization_present": authorization is not None,
        "authorization_valid_for_executor": authorized,
        "status": "READY" if boundary_ok and not authorized else ("AUTHORIZED" if boundary_ok else "FAIL"),
    }
    Path(args.output).write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
