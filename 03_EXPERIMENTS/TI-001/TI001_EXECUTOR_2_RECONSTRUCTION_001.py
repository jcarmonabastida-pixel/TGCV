#!/usr/bin/env python3
"""TI-001 independent Executor-2 fixture reconstruction.

This implementation is intentionally independent of the canonical fixture
generator. It reconstructs the observable preflight fixture from the frozen
TI-001 reconstruction specification only. It performs no scientific
execution.
"""
import hashlib
import json
import random
import sys

RANDOMISATION_SEED = 582031
ENVIRONMENT_SEED_BASE = 731407
PAIR_COUNT = 32
BASE_ACTIONS = ["a", "b", "c"]


def build_assignment():
    pair_ids = [f"TI001-{i + 1:03d}" for i in range(PAIR_COUNT)]
    shuffled = pair_ids[:]
    rng = random.Random(RANDOMISATION_SEED)
    rng.shuffle(shuffled)

    assignment = {}
    for j, pair_id in enumerate(shuffled):
        if j % 2 == 0:
            assignment[pair_id] = {
                "slot_A": "control",
                "slot_B": "treatment",
            }
        else:
            assignment[pair_id] = {
                "slot_A": "treatment",
                "slot_B": "control",
            }
    return pair_ids, assignment


def build_records(pair_ids, assignment):
    records = []

    for i, pair_id in enumerate(pair_ids):
        environment_seed = ENVIRONMENT_SEED_BASE + i

        current_state = "S0"
        current_accessibility = ["a", "b", "c"]

        successors = {
            "a": {"state": "SA", "t_acc": ["x", "y"]},
            "b": {"state": "SB", "t_acc": ["x", "z"]},
            "c": {"state": "SC", "t_acc": ["y", "z"]},
        }

        future_alternatives = [
            {"choice": "a", "successor": "SA", "T_acc_t1": ["x", "y"]},
            {"choice": "b", "successor": "SB", "T_acc_t1": ["x", "z"]},
        ]

        treatment_info = {
            "future_reconfiguration": "two_of_three_identity_pattern",
            "candidate_count": 3,
            "descriptor": "successor_space_identity_turnover",
        }

        control_info = {
            "task": "select_one_current_transformation",
            "candidate_count": 3,
        }

        tsda_descriptors = {
            "representation": "transition_level_preflight",
            "accessibility_cardinality_t": len(current_accessibility),
            "future_alternative_count": len(future_alternatives),
            "future_accessibility_cardinalities": [
                len(item["T_acc_t1"]) for item in future_alternatives
            ],
            "identity_turnover": True,
            "net_accessibility_change_by_alternative": [
                len(item["T_acc_t1"]) - len(current_accessibility)
                for item in future_alternatives
            ],
        }

        null_information = {
            "task": "select_one_current_transformation",
            "candidate_count": 3,
            "format": "structured",
            "future_space_signal": False,
            "recommendation": False,
            "outcome_signal": False,
        }

        common = {
            "pair_id": pair_id,
            "S_t": current_state,
            "T_acc_t": current_accessibility,
            "available_transformations": BASE_ACTIONS,
            "successors": successors,
            "future_alternatives": future_alternatives,
            "temporal_order": [
                "information_available",
                "transformation_choice",
                "successor_state",
                "successor_accessibility",
            ],
            "primary_estimand": {
                "name": "matched_condition_difference_in_transformation_handling",
                "type": "difference_in_subsequent_transformation_handling",
                "forbidden": [
                    "TI_score",
                    "value",
                    "reward",
                    "utility",
                    "performance",
                ],
            },
            "null": {"information": null_information},
            "null_condition": {
                "information": null_information,
                "scientific_execution": False,
            },
        }

        for slot in ("slot_A", "slot_B"):
            condition = assignment[pair_id][slot]

            records.append({
                **common,
                "instance_id": pair_id,
                "condition": condition,
                "execution_slot": slot,
                "seed": environment_seed,
                "environment_seed": environment_seed,
                "randomisation_seed": RANDOMISATION_SEED,
                "information_control": control_info,
                "information_treatment": (
                    treatment_info if condition == "treatment" else None
                ),
                "selected_transformation": None,
                "S_t1": None,
                "T_acc_t1": None,
                "Delta_T_acc_t": None,
                "TSDA_descriptors": tsda_descriptors,
                "decision_before_future_reveal": True,
                "leakage_checks": {
                    "condition_in_state": False,
                    "condition_in_current_accessibility": False,
                    "preferred_action_revealed": False,
                    "outcome_revealed": False,
                    "future_space_signal_in_control": False,
                    "future_space_signal_in_treatment_is_structured": True,
                },
            })

    return records


def build_fixture():
    pair_ids, assignment = build_assignment()
    records = build_records(pair_ids, assignment)

    fixture = {
        "schema": "TI001_PREFLIGHT_FIXTURE_v004",
        "randomisation_seed": RANDOMISATION_SEED,
        "environment_seed_base": ENVIRONMENT_SEED_BASE,
        "pair_count": PAIR_COUNT,
        "record_count": len(records),
        "instances": records,
    }

    canonical_bytes = json.dumps(
        fixture,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8")

    fixture["fixture_sha256"] = hashlib.sha256(canonical_bytes).hexdigest()
    return fixture


def main():
    fixture = build_fixture()

    if len(sys.argv) == 2:
        with open(sys.argv[1], "w", encoding="utf-8", newline="\n") as handle:
            json.dump(fixture, handle, indent=2, sort_keys=True)
            handle.write("\n")

    print(json.dumps({
        "status": "RECONSTRUCTION_COMPLETE",
        "schema": fixture["schema"],
        "pair_count": fixture["pair_count"],
        "record_count": fixture["record_count"],
        "fixture_sha256": fixture["fixture_sha256"],
        "scientific_execution": "NOT_PERFORMED",
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
