#!/usr/bin/env python3
"""
TI-001 V012 NEXT3 fixture generator.

Design-only artifact. It generates a candidate fixture but does not authorize
or perform scientific execution.
"""

import hashlib
import json
import random
from pathlib import Path

VERSION = "NEXT3_v001"
REQUIREMENTS_HASH = "TI001_V012_NEXT3_MINIMAL_IDENTIFIABILITY_REQUIREMENTS_001"
SEMANTICS_HASH = "TI001_V012_NEXT3_MAPPING_SEMANTICS_001"

DOMAINS = [
    "D1_spatial_planning",
    "D2_resource_planning",
    "D3_graph_reconfiguration",
    "D4_workflow_state_machine",
]
OPERATIONALISATIONS = [
    "O1_cardinality",
    "O2_topology",
    "O3_depth",
    "O4_constraints",
    "O5_composition",
]
PRESENTATIONS = ["P1_order", "P2_position", "P3_orientation", "P4_format"]
CONDITIONS = [
    "INFORMATIVE",
    "SURFACE_PERMUTED",
    "UNINFORMATIVE_NULL",
    "CONTRADICTORY",
]
ACTIONS = ["A", "B", "C", "D"]
PROFILES = ["slot_1", "slot_2", "slot_3", "slot_4"]

PROFILE_VALUES = {
    "slot_1": [1, 1, 1, 1],
    "slot_2": [2, 1, 1, 2],
    "slot_3": [3, 2, 2, 2],
    "slot_4": [4, 3, 3, 3],
}

# Fixed-point-free permutations used only for post-decision realization.
SURFACE_PERMUTATION = {
    "slot_1": "slot_2",
    "slot_2": "slot_3",
    "slot_3": "slot_4",
    "slot_4": "slot_1",
}
CONTRADICTORY_PERMUTATION = {
    "slot_1": "slot_3",
    "slot_2": "slot_4",
    "slot_3": "slot_1",
    "slot_4": "slot_2",
}

REPLICATES = 30


def digest(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def deterministic_permutation(seed_material):
    seed = int(digest(seed_material)[:16], 16)
    rng = random.Random(seed)
    values = PROFILES[:]
    rng.shuffle(values)
    return values


def validate_bijection(mapping):
    return (
        list(mapping.keys()) == ACTIONS
        and sorted(mapping.values()) == sorted(PROFILES)
    )


def null_mapping(d, o, p, r):
    # Deliberately independent of f, selected action and z.
    seed_material = "|".join(
        [
            VERSION,
            REQUIREMENTS_HASH,
            SEMANTICS_HASH,
            d,
            o,
            p,
            str(r),
            "NULL",
        ]
    )
    profiles = deterministic_permutation(seed_material)
    return dict(zip(ACTIONS, profiles))


def realized_mapping(condition, f):
    if condition == "INFORMATIVE":
        return dict(f)
    if condition == "SURFACE_PERMUTED":
        return {a: SURFACE_PERMUTATION[f[a]] for a in ACTIONS}
    if condition == "CONTRADICTORY":
        return {a: CONTRADICTORY_PERMUTATION[f[a]] for a in ACTIONS}
    if condition == "UNINFORMATIVE_NULL":
        raise ValueError("NULL realization requires unit-specific null_mapping.")
    raise ValueError(condition)


def make_unit(d, o, condition, p, permutation_index, replicate):
    f_profiles = deterministic_permutation(
        "|".join(
            [
                VERSION,
                "F",
                d,
                o,
                condition,
                p,
                str(permutation_index),
                str(replicate),
            ]
        )
    )
    f = dict(zip(ACTIONS, f_profiles))
    assert validate_bijection(f)

    if condition == "UNINFORMATIVE_NULL":
        z = null_mapping(d, o, p, replicate)
    else:
        z = realized_mapping(condition, f)

    assert validate_bijection(z)

    presented_profiles = [
        {
            "action": action,
            "profile_id": f[action],
            "profile": PROFILE_VALUES[f[action]],
        }
        for action in ACTIONS
    ]

    return {
        "version": VERSION,
        "unit_id": (
            f"{d}|{o}|{condition}|{p}|"
            f"k{permutation_index:02d}|r{replicate:02d}"
        ),
        "domain": d,
        "operationalisation": o,
        "mapping_condition_metadata": condition,
        "presentation": p,
        "permutation_index": permutation_index,
        "replicate": replicate,
        "actions": ACTIONS,
        "f": f,
        "presented_profiles": presented_profiles,
        "z": z,
        "profile_values": PROFILE_VALUES,
        "scientific_execution": False,
    }


def generate(output_path):
    rows = []
    for d in DOMAINS:
        for o in OPERATIONALISATIONS:
            for condition in CONDITIONS:
                for p in PRESENTATIONS:
                    for k in range(24):
                        for r in range(1, REPLICATES + 1):
                            rows.append(make_unit(d, o, condition, p, k, r))

    assert len(rows) == 4 * 5 * 4 * 4 * 24 * 30
    assert all(validate_bijection(row["f"]) for row in rows)
    assert all(validate_bijection(row["z"]) for row in rows)

    output = {
        "fixture_id": "TI001_V012_NEXT3_CANDIDATE_FIXTURE_001",
        "status": "CANDIDATE_NOT_FROZEN",
        "version": VERSION,
        "requirements_reference": REQUIREMENTS_HASH,
        "semantics_reference": SEMANTICS_HASH,
        "unit_count": len(rows),
        "domain_count": len(DOMAINS),
        "operationalisation_count": len(OPERATIONALISATIONS),
        "condition_count": len(CONDITIONS),
        "presentation_count": len(PRESENTATIONS),
        "permutations_per_cell": 24,
        "replicates_per_cell": REPLICATES,
        "rows": rows,
        "scientific_execution_authorized": False,
    }

    text = json.dumps(output, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    Path(output_path).write_text(text, encoding="utf-8")
    return digest(text), len(rows)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    sha256, count = generate(args.output)
    print(json.dumps({
        "status": "CANDIDATE_FIXTURE_GENERATED",
        "unit_count": count,
        "sha256": sha256,
        "scientific_execution": False,
        "authorization": "NOT_AUTHORIZED",
    }, sort_keys=True))
