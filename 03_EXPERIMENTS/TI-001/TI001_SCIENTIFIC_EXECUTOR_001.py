#!/usr/bin/env python3
"""TI-001 Scientific Execution Harness 002.

Consumes the frozen fixture and a decision-provider evidence package.
The harness does not generate decisions. It validates the decision record
against the execution record, then applies the frozen deterministic transition.

Scientific execution remains governed by the separate authorization record.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ALLOWED_ACTIONS = {"a", "b", "c"}
REQUIRED_DECISION_FIELDS = {
    "pair_id",
    "instance_id",
    "condition",
    "selected_transformation",
    "decision_timestamp",
}

def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))

def canonical_body_hash(fixture: dict) -> str:
    body = dict(fixture)
    body.pop("fixture_sha256", None)
    raw = json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return sha256_bytes(raw)

def decision_key(record: dict) -> str:
    return f"{record['pair_id']}::{record['condition']}"

def validate_decision(decision: dict, record: dict) -> None:
    missing = REQUIRED_DECISION_FIELDS - set(decision)
    if missing:
        raise ValueError(f"missing decision fields: {sorted(missing)}")
    for key in ("pair_id", "instance_id", "condition"):
        if decision[key] != record[key]:
            raise ValueError(f"decision mismatch in {key}")
    action = decision["selected_transformation"]
    if action not in ALLOWED_ACTIONS:
        raise ValueError(f"invalid selected_transformation: {action}")
    if not isinstance(decision["decision_timestamp"], str) or not decision["decision_timestamp"]:
        raise ValueError("invalid decision_timestamp")

def execute(fixture: dict, decision_package: dict, canonical_commit: str, executor_version: str):
    expected_hash = fixture["fixture_sha256"]
    actual_hash = canonical_body_hash(fixture)
    if actual_hash != expected_hash:
        raise ValueError("fixture canonical body hash mismatch")

    if decision_package.get("fixture_sha256") != expected_hash:
        raise ValueError("decision package fixture hash mismatch")

    decisions = decision_package.get("decisions")
    if not isinstance(decisions, dict):
        raise ValueError("decision package missing decisions object")

    records = fixture["instances"]
    observations = []

    for record in records:
        key = decision_key(record)
        if key not in decisions:
            raise ValueError(f"missing decision for {key}")

        # Decision point: successor information is intentionally not consulted.
        decision = decisions[key]
        validate_decision(decision, record)
        selected = decision["selected_transformation"]

        transitions = record["successors"]
        if selected not in transitions:
            raise ValueError(f"selected transformation not executable for {key}")

        successor = transitions[selected]
        observations.append({
            "pair_id": record["pair_id"],
            "instance_id": record["instance_id"],
            "condition": record["condition"],
            "execution_slot": record["execution_slot"],
            "selected_transformation": selected,
            "successor_state": successor["state"],
            "successor_accessibility": successor["t_acc"],
            "canonical_commit": canonical_commit,
            "fixture_sha256": expected_hash,
            "executor_version": executor_version,
        })

    return {
        "record_type": "TGCV_TI001_SCIENTIFIC_EXECUTION_OUTPUT",
        "executor_version": executor_version,
        "canonical_commit": canonical_commit,
        "fixture_sha256": expected_hash,
        "decision_provider_version": decision_package.get("provider_version"),
        "observation_count": len(observations),
        "observations": observations,
        "deviations": [],
        "scientific_execution": "PERFORMED",
    }

def main(argv):
    if len(argv) != 4:
        raise SystemExit(
            "usage: TI001_SCIENTIFIC_EXECUTOR_002.py <fixture.json> <decisions.json> <canonical_commit>"
        )

    fixture_path = Path(argv[1])
    decisions_path = Path(argv[2])
    canonical_commit = argv[3]
    fixture = load_json(fixture_path)
    decision_package = load_json(decisions_path)

    result = execute(
        fixture,
        decision_package,
        canonical_commit,
        executor_version="TI001_SCIENTIFIC_EXECUTOR_002",
    )
    print(json.dumps(result, sort_keys=True, indent=2))

if __name__ == "__main__":
    main(sys.argv)
