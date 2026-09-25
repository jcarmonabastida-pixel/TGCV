#!/usr/bin/env python3
"""TI-001 V007 scientific execution harness.

Consumes the frozen V007 fixture, the V007 decision-units package, and the
provider decision output. It does not generate model decisions. Successor
effects are evaluated only after the decision has been supplied.
No scientific execution occurs during import or validation.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ALLOWED = {"A", "B"}
CONDITIONS = {"control", "treatment", "null"}
EXPECTED_FIXTURE_ID = "TI001-v007-candidate-001"
EXPECTED_FIXTURE_VERSION = "v007-candidate-001"
EXPECTED_DECISIONS = 420


def load(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def flatten_instances(fixture):
    out = {}
    for pair in fixture["pairs"]:
        for instance in pair["instances"]:
            key = instance["instance_id"]
            if key in out:
                raise ValueError(f"duplicate instance_id: {key}")
            out[key] = instance
    return out


def execute(fixture, units_package, decision_package):
    if fixture.get("fixture_id") != EXPECTED_FIXTURE_ID:
        raise ValueError("unexpected V007 fixture_id")
    if fixture.get("version") != EXPECTED_FIXTURE_VERSION:
        raise ValueError("unexpected V007 fixture version")
    if len(fixture.get("pairs", [])) != 210:
        raise ValueError("V007 fixture must contain 210 pairs")
    if decision_package.get("scientific_execution") != "PERFORMED":
        raise ValueError("decision package is not marked PERFORMED")
    if decision_package.get("decision_count") != EXPECTED_DECISIONS:
        raise ValueError("decision package must contain 420 decisions")
    if units_package.get("fixture_id") != fixture.get("fixture_id"):
        raise ValueError("decision-units fixture_id mismatch")
    if units_package.get("fixture_version") != fixture.get("version"):
        raise ValueError("decision-units fixture_version mismatch")
    if units_package.get("fixture_sha256") != decision_package.get("fixture_sha256"):
        raise ValueError("decision package fixture hash mismatch")

    units = units_package.get("decision_units", [])
    instances = units_package.get("instances", [])
    decisions = decision_package.get("decisions", {})
    if len(units) != EXPECTED_DECISIONS or len(instances) != EXPECTED_DECISIONS:
        raise ValueError("V007 decision-units package must contain 420 units and instances")

    by_instance = flatten_instances(fixture)
    observations = []

    for unit, traced in zip(units, instances):
        decision_id = unit["decision_id"]
        instance_id = traced["instance_id"]
        if decision_id not in decisions:
            raise ValueError(f"missing decision: {decision_id}")
        if instance_id not in by_instance:
            raise ValueError(f"instance absent from fixture: {instance_id}")

        fixture_instance = by_instance[instance_id]
        if fixture_instance["condition"] != unit["condition"]:
            raise ValueError(f"condition mismatch for {instance_id}")
        selected = decisions[decision_id].get("selected_transformation")
        if selected not in ALLOWED:
            raise ValueError(f"invalid selected transformation for {decision_id}: {selected!r}")

        expected = fixture_instance["audit"]["expected_future_t_acc"][selected]
        enables_c = "C" in expected
        observations.append({
            "decision_id": decision_id,
            "pair_id": fixture_instance["pair_id"],
            "instance_id": instance_id,
            "condition": fixture_instance["condition"],
            "variant": fixture_instance["variant"],
            "selected_transformation": selected,
            "future_t_acc_after_selected_transformation": expected,
            "Y": 1 if enables_c else 0,
            "response_id": decisions[decision_id].get("response_id"),
            "decision_timestamp": decisions[decision_id].get("decision_timestamp"),
        })

    if len(observations) != EXPECTED_DECISIONS:
        raise ValueError("unexpected observation count")

    return {
        "record_type": "TGCV_TI001_V007_SCIENTIFIC_EXECUTION_OUTPUT",
        "executor_version": "TI001_V007_SCIENTIFIC_EXECUTOR_001",
        "fixture_id": fixture.get("fixture_id"),
        "fixture_version": fixture.get("version"),
        "fixture_sha256": decision_package.get("fixture_sha256"),
        "decision_provider_version": decision_package.get("provider_version"),
        "observation_count": len(observations),
        "observations": observations,
        "deviations": [],
        "scientific_execution": "PERFORMED",
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("fixture")
    p.add_argument("decision_units")
    p.add_argument("decisions")
    p.add_argument("--output")
    args = p.parse_args()

    result = execute(load(Path(args.fixture)), load(Path(args.decision_units)), load(Path(args.decisions)))
    text = json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    if args.output:
        Path(args.output).write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
