#!/usr/bin/env python3
"""TI-001 v005 scientific executor.

Consumes only the frozen v005 design and a v005 decision package.
It validates decision-time evidence and never requires or synthesizes
v004 successor information.
"""
from __future__ import annotations
import argparse, hashlib, json, sys
from pathlib import Path

ALLOWED = {"a", "b", "c"}
FIXTURE_ID = "TI001-v005-candidate-001"
FIXTURE_VERSION = "v005-candidate-001"
EXPECTED_FIXTURE_GIT_BLOB_SHA = "edd83fd2df3d39aad8911087569c19614c2264b7"
EXPECTED_FIXTURE_CANONICAL_SHA256 = "bc7e0e69cb56337145593e67fb55c1a1b5042db661520498a2c86b346eef76e5"
EXECUTOR_VERSION = "TI001_V005_SCIENTIFIC_EXECUTOR_001"

def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))

def canonical_hash(obj: dict) -> str:
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

def validate_fixture(fixture: dict) -> None:
    if fixture.get("fixture_id") != FIXTURE_ID:
        raise ValueError("unexpected fixture_id")
    if fixture.get("version") != FIXTURE_VERSION:
        raise ValueError("unexpected fixture version")
    if fixture.get("status") != "FROZEN":
        raise ValueError("fixture is not FROZEN")
    if fixture.get("scientific_execution") != "NOT_AUTHORIZED":
        raise ValueError("fixture execution state changed")
    for condition, c in fixture["conditions"].items():
        if c["state"] != "S0" or c["t_acc"] != ["a", "b", "c"] or c["actions"] != ["a", "b", "c"]:
            raise ValueError(f"{condition}: current decision environment mismatch")
        if c["decision_timing"] != "before_successor_realisation":
            raise ValueError(f"{condition}: invalid decision timing")
    if fixture["successor_state_before_selection"] or fixture["successor_accessibility_before_selection"]:
        raise ValueError("future reveal is not blocked")

def validate_decisions(package: dict, fixture: dict) -> list[dict]:
    if package.get("fixture_sha256") != EXPECTED_FIXTURE_CANONICAL_SHA256:
        raise ValueError("decision package fixture hash mismatch")
    decisions = package.get("decisions")
    if not isinstance(decisions, dict) or not decisions:
        raise ValueError("missing decisions")
    observations = []
    for key, d in decisions.items():
        if d.get("condition") not in fixture["conditions"]:
            raise ValueError(f"{key}: invalid condition")
        if d.get("selected_transformation") not in ALLOWED:
            raise ValueError(f"{key}: invalid selected transformation")
        if not d.get("response_id"):
            raise ValueError(f"{key}: missing response_id")
        if not d.get("decision_input_sha256"):
            raise ValueError(f"{key}: missing decision input hash")
        observations.append({
            "pair_id": d.get("pair_id"),
            "condition": d["condition"],
            "selected_transformation": d["selected_transformation"],
            "decision_timestamp": d.get("decision_timestamp"),
            "response_id": d["response_id"],
            "decision_input_sha256": d["decision_input_sha256"],
        })
    return observations

def execute(fixture: dict, package: dict, canonical_commit: str) -> dict:
    actual = canonical_hash(fixture)
    if actual != EXPECTED_FIXTURE_CANONICAL_SHA256:
        raise ValueError("frozen v005 fixture canonical hash mismatch")
    observations = validate_decisions(package, fixture)
    return {
        "record_type": "TGCV_TI001_V005_SCIENTIFIC_EXECUTION_OUTPUT",
        "executor_version": EXECUTOR_VERSION,
        "contract": "TI001_V005_EXECUTION_CONTRACT_001",
        "canonical_commit": canonical_commit,
        "fixture_sha256": EXPECTED_FIXTURE_CANONICAL_SHA256,
        "decision_provider_version": package.get("provider_version"),
        "observation_count": len(observations),
        "estimand": "matched_condition_difference_in_transformation_selection",
        "composite_ti_score": None,
        "observations": observations,
        "deviations": [],
        "successor_information_consumed": False,
        "scientific_execution": "PERFORMED",
    }

def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("fixture")
    p.add_argument("decisions")
    p.add_argument("canonical_commit")
    p.add_argument("output")
    args = p.parse_args(argv[1:])
    result = execute(load_json(Path(args.fixture)), load_json(Path(args.decisions)), args.canonical_commit)
    Path(args.output).write_text(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False)+"
", encoding="utf-8")
    print(json.dumps({"status":"SCIENTIFIC_EXECUTION_OUTPUT_WRITTEN","observation_count":result["observation_count"]},indent=2))
    return 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
