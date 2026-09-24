#!/usr/bin/env python3
"""TI-001 Formal Analysis 001.

Deterministic post-execution analysis for the frozen primary estimand:
matched_condition_difference_in_transformation_handling.

The analysis consumes only the frozen fixture and a scientific execution
output. It performs no model calls, no external lookups, and no manual
interpretation. The primary operational metric is matched-pair
transformation-choice divergence: the proportion of complete matched pairs
whose control and treatment selected transformations differ.

It also reports condition/action counts and action-specific condition
differences as descriptive audit quantities. No composite TI score is built.
"""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

EXPECTED_FIXTURE_SHA256 = (
    "20ad94fcaca2e85228f1a266ae69d9d391a35182a64ab122fd5feed56b46a4dd"
)
EXPECTED_RECORDS = 64
EXPECTED_PAIRS = 32
EXPECTED_ESTIMAND = "matched_condition_difference_in_transformation_handling"
EXPECTED_ESTIMAND_TYPE = "difference_in_subsequent_transformation_handling"
ALLOWED_CONDITIONS = {"control", "treatment"}
ALLOWED_ACTIONS = {"a", "b", "c"}


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def canonical_fixture_hash(fixture: dict) -> str:
    body = dict(fixture)
    body.pop("fixture_sha256", None)
    raw = json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    return sha256_bytes(raw)


def main(argv):
    if len(argv) != 3:
        raise SystemExit(
            "usage: TI001_FORMAL_ANALYSIS_001.py <fixture.json> <scientific_execution_output.json>"
        )

    fixture_path = Path(argv[1])
    output_path = Path(argv[2])

    fixture = load_json(fixture_path)
    execution = load_json(output_path)

    declared_hash = fixture.get("fixture_sha256")
    actual_hash = canonical_fixture_hash(fixture)
    if declared_hash != EXPECTED_FIXTURE_SHA256 or actual_hash != EXPECTED_FIXTURE_SHA256:
        raise ValueError("fixture hash mismatch")

    observations = execution.get("observations")
    if execution.get("scientific_execution") != "PERFORMED":
        raise ValueError("scientific execution output is not marked PERFORMED")
    if execution.get("fixture_sha256") != EXPECTED_FIXTURE_SHA256:
        raise ValueError("execution output fixture hash mismatch")
    if execution.get("observation_count") != EXPECTED_RECORDS:
        raise ValueError("unexpected observation count")
    if not isinstance(observations, list) or len(observations) != EXPECTED_RECORDS:
        raise ValueError("invalid observations collection")
    if execution.get("deviations") != []:
        raise ValueError("scientific execution contains deviations")

    fixture_pairs = {}
    for record in fixture.get("instances", []):
        key = (record["pair_id"], record["condition"])
        if key in fixture_pairs:
            raise ValueError(f"duplicate fixture slot: {key}")
        fixture_pairs[key] = record

    if len(fixture_pairs) != EXPECTED_RECORDS:
        raise ValueError("fixture does not contain exactly 64 pair-condition slots")

    obs_by_slot = {}
    for obs in observations:
        condition = obs.get("condition")
        pair_id = obs.get("pair_id")
        action = obs.get("selected_transformation")
        key = (pair_id, condition)

        if condition not in ALLOWED_CONDITIONS:
            raise ValueError(f"invalid condition: {condition}")
        if action not in ALLOWED_ACTIONS:
            raise ValueError(f"invalid selected transformation: {action}")
        if key in obs_by_slot:
            raise ValueError(f"duplicate execution slot: {key}")
        if key not in fixture_pairs:
            raise ValueError(f"execution slot absent from fixture: {key}")
        obs_by_slot[key] = obs

    if set(obs_by_slot) != set(fixture_pairs):
        raise ValueError("execution slots do not exactly match frozen fixture")

    pair_ids = sorted({pair_id for pair_id, _ in fixture_pairs})
    if len(pair_ids) != EXPECTED_PAIRS:
        raise ValueError("unexpected matched-pair count")

    pair_rows = []
    for pair_id in pair_ids:
        control = obs_by_slot.get((pair_id, "control"))
        treatment = obs_by_slot.get((pair_id, "treatment"))
        if control is None or treatment is None:
            raise ValueError(f"incomplete matched pair: {pair_id}")

        control_action = control["selected_transformation"]
        treatment_action = treatment["selected_transformation"]
        pair_rows.append({
            "pair_id": pair_id,
            "control_transformation": control_action,
            "treatment_transformation": treatment_action,
            "transformation_choice_diverged": control_action != treatment_action,
        })

    divergent_pairs = sum(r["transformation_choice_diverged"] for r in pair_rows)
    divergence_rate = divergent_pairs / EXPECTED_PAIRS

    action_counts = {
        condition: {
            action: sum(
                obs_by_slot[(pair_id, condition)]["selected_transformation"] == action
                for pair_id in pair_ids
            )
            for action in sorted(ALLOWED_ACTIONS)
        }
        for condition in ("control", "treatment")
    }

    action_condition_differences = {
        action: (
            action_counts["treatment"][action] / EXPECTED_PAIRS
            - action_counts["control"][action] / EXPECTED_PAIRS
        )
        for action in sorted(ALLOWED_ACTIONS)
    }

    result = {
        "record_type": "TGCV_TI001_FORMAL_ANALYSIS_OUTPUT",
        "analysis_version": "TI001_FORMAL_ANALYSIS_001",
        "fixture_sha256": EXPECTED_FIXTURE_SHA256,
        "scientific_execution_output_fixture_sha256": execution["fixture_sha256"],
        "scientific_execution_canonical_commit": execution.get("canonical_commit"),
        "scientific_executor_version": execution.get("executor_version"),
        "decision_provider_version": execution.get("decision_provider_version"),
        "estimand": EXPECTED_ESTIMAND,
        "estimand_type": EXPECTED_ESTIMAND_TYPE,
        "record_count": EXPECTED_RECORDS,
        "matched_pair_count": EXPECTED_PAIRS,
        "primary_metric": "transformation_choice_divergence_rate",
        "primary_metric_definition": (
            "proportion of complete matched pairs for which treatment and control "
            "selected different transformations"
        ),
        "divergent_pairs": divergent_pairs,
        "non_divergent_pairs": EXPECTED_PAIRS - divergent_pairs,
        "transformation_choice_divergence_rate": divergence_rate,
        "condition_action_counts": action_counts,
        "action_specific_condition_differences": action_condition_differences,
        "pair_results": pair_rows,
        "composite_ti_score": None,
        "interpretation": "NOT_PERFORMED",
        "deviations": [],
    }

    print(json.dumps(result, sort_keys=True, indent=2))


if __name__ == "__main__":
    main(sys.argv)
