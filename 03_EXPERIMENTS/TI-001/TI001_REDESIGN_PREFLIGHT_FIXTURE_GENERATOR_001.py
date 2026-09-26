#!/usr/bin/env python3
"""
TGCV TI-001 redesign preflight candidate fixture generator 001.

Generates a new v005 candidate for TI001_REDESIGN_PREFLIGHT_SPECIFICATION_002.
This file does not execute the scientific experiment and does not modify v004.
"""

from __future__ import annotations

import hashlib
import json
import random
from typing import Any, Dict


RANDOMISATION_SEED = 582031
ENVIRONMENT_SEED_BASE = 731407
FIXTURE_VERSION = "TI001_REDESIGN_PREFLIGHT_FIXTURE_v005"
ACTIONS = ["a", "b", "c"]


def build_fixture() -> Dict[str, Any]:
    # Deterministic frozen transition specification.  The per-instance nonce
    # is provenance only; it is not exposed as treatment information.
    environment_rng = random.Random(ENVIRONMENT_SEED_BASE)
    environment_nonce = environment_rng.getrandbits(32)

    transition_spec = {
        "state": "S0",
        "current_accessible_transformations": ACTIONS,
        "transitions": {
            "a": {
                "successor": "SA",
                "future_accessible_transformations": ["x", "y"],
                "future_descriptor": {
                    "future_accessibility_class": "pair_xy",
                    "identity_turnover_class": "turnover_2",
                    "persistence_class": "none",
                    "reconfiguration_class": "pair_xy",
                },
            },
            "b": {
                "successor": "SB",
                "future_accessible_transformations": ["x", "z"],
                "future_descriptor": {
                    "future_accessibility_class": "pair_xz",
                    "identity_turnover_class": "turnover_2",
                    "persistence_class": "none",
                    "reconfiguration_class": "pair_xz",
                },
            },
            "c": {
                "successor": "SC",
                "future_accessible_transformations": ["y", "z"],
                "future_descriptor": {
                    "future_accessibility_class": "pair_yz",
                    "identity_turnover_class": "turnover_2",
                    "persistence_class": "none",
                    "reconfiguration_class": "pair_yz",
                },
            },
        },
    }

    future_mapping = {
        action: transition_spec["transitions"][action]["future_descriptor"]
        for action in ACTIONS
    }

    transition_traceability = {
        action: {
            "action": action,
            "future_descriptor": future_mapping[action],
            "source_successor": transition_spec["transitions"][action]["successor"],
            "source_future_accessibility": transition_spec["transitions"][action][
                "future_accessible_transformations"
            ],
        }
        for action in ACTIONS
    }

    conditions = {
        "control": {
            "state": "S0",
            "t_acc": ACTIONS,
            "actions": ACTIONS,
            "task": "select_one_current_transformation",
            "candidate_count": 3,
            "mapping_non_derivable": True,
            "future_signal": None,
        },
        "treatment": {
            "state": "S0",
            "t_acc": ACTIONS,
            "actions": ACTIONS,
            "task": "select_one_current_transformation",
            "candidate_count": 3,
            "admissible_actions": ACTIONS,
            "future_mapping": future_mapping,
        },
        "null": {
            "state": "S0",
            "t_acc": ACTIONS,
            "actions": ACTIONS,
            "task": "select_one_current_transformation",
            "candidate_count": 3,
            "future_mapping": None,
            "future_signal": None,
            "recommendation": None,
            "format_compatible": True,
        },
    }

    fixture: Dict[str, Any] = {
        "schema": FIXTURE_VERSION,
        "randomisation_seed": RANDOMISATION_SEED,
        "environment_seed": ENVIRONMENT_SEED_BASE,
        "environment_nonce": environment_nonce,
        "state": "S0",
        "t_acc": ACTIONS,
        "actions": ACTIONS,
        "temporal_order": [
            "information_presentation",
            "transformation_selection",
            "successor_realisation",
            "future_accessibility_reveal",
        ],
        "conditions": conditions,
        "transition_spec": transition_spec,
        "transition_traceability": transition_traceability,
        "successor_state_before_selection": False,
        "successor_accessibility_before_selection": False,
        "divergence_witness": {
            "control_action": "a",
            "treatment_action": "b",
            "different": True,
            "depends_on_treatment_mapping": True,
            "same_state": True,
            "same_t_acc": True,
            "same_task": True,
            "same_timing": True,
            "same_decision_rule": True,
            "no_evaluation": True,
            "removing_mapping_removes_witness": True,
            "mapping_action_used": "b",
            "mapping_descriptor_used": future_mapping["b"],
            "control_without_mapping_action": "a",
            "treatment_with_mapping_action": "b",
            "mapping_removed_action": "a",
        },
        "scientific_execution": False,
    }

    raw = json.dumps(
        fixture, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    ).encode("utf-8")
    fixture["fixture_sha256"] = hashlib.sha256(raw).hexdigest()
    return fixture


def main() -> None:
    print(json.dumps(build_fixture(), indent=2, sort_keys=True, ensure_ascii=False))


if __name__ == "__main__":
    main()
