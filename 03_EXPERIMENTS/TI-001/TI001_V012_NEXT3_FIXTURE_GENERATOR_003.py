#!/usr/bin/env python3
"""TI-001 V012 NEXT3 amended fixture generator.

Design/binding artifact only. Scientific execution is not performed or
authorized by this generator.
"""

import hashlib
import json
import random
from pathlib import Path

REQUIREMENTS_HASH = "TI001_V012_NEXT3_MINIMAL_IDENTIFIABILITY_REQUIREMENTS_001"
SEMANTICS_HASH = "TI001_V012_NEXT3_MAPPING_SEMANTICS_001"
BASELINE_STATE_SPEC = "TI001_V012_NEXT3_DOMAIN_VALID_BASELINE_STATE_SPECIFICATION_001"
CONTEXT_SPEC = "TI001_V012_NEXT3_PREDECISION_STATE_CONTEXT_SPECIFICATION_AMENDMENT_001"

DOMAINS = [
    "D1_spatial_planning", "D2_resource_planning",
    "D3_graph_reconfiguration", "D4_workflow_state_machine",
]
OPERATIONALISATIONS = [
    "O1_cardinality", "O2_topology", "O3_depth",
    "O4_constraints", "O5_composition",
]
PRESENTATIONS = ["P1_order", "P2_position", "P3_orientation", "P4_format"]
CONDITIONS = ["INFORMATIVE", "SURFACE_PERMUTED", "UNINFORMATIVE_NULL", "CONTRADICTORY"]
ACTIONS = ["A", "B", "C", "D"]
PROFILES = ["slot_1", "slot_2", "slot_3", "slot_4"]
REPLICATES = 30  # implementation parameter only; not a scientific count

PROFILE_VALUES = {
    "slot_1": [1, 1, 1, 1],
    "slot_2": [2, 1, 1, 2],
    "slot_3": [3, 2, 2, 2],
    "slot_4": [4, 3, 3, 3],
}
DOMAIN_ELEMENT_TYPES = {
    "D1_spatial_planning": "spatial_node",
    "D2_resource_planning": "resource_node",
    "D3_graph_reconfiguration": "graph_node",
    "D4_workflow_state_machine": "workflow_state",
}
SURFACE_PERMUTATION = {
    "slot_1": "slot_2", "slot_2": "slot_3",
    "slot_3": "slot_4", "slot_4": "slot_1",
}
CONTRADICTORY_PERMUTATION = {
    "slot_1": "slot_3", "slot_2": "slot_4",
    "slot_3": "slot_1", "slot_4": "slot_2",
}
TASK_CONTEXT = {
    "task_id": "NEXT3",
    "task_instruction": (
        "Select exactly one action from the candidate action set using the "
        "visible current state and the structural transformation profile "
        "presented for each candidate action."
    ),
    "response_constraint": "Return exactly one candidate action identifier: A, B, C, or D.",
}

def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True,
                      separators=(",", ":"))

def digest(obj):
    return hashlib.sha256(canonical(obj).encode("utf-8")).hexdigest()

def deterministic_permutation(seed_material):
    seed = int(digest(seed_material)[:16], 16)
    rng = random.Random(seed)
    values = PROFILES[:]
    rng.shuffle(values)
    return values

def baseline_state(domain):
    element_type = DOMAIN_ELEMENT_TYPES[domain]
    return {
        "active": [
            {"id": 1, "type": element_type, "domain": domain},
            {"id": 2, "type": element_type, "domain": domain},
        ],
        "relations": [],
        "constraints": [],
    }

def validate_bijection(mapping):
    return list(mapping.keys()) == ACTIONS and sorted(mapping.values()) == sorted(PROFILES)

def null_mapping(d, o, p, r):
    # Exact frozen null-mapping seed inputs; no generator-version component.
    seed_material = "|".join([
        REQUIREMENTS_HASH, SEMANTICS_HASH,
        d, o, p, str(r), "NULL"
    ])
    return dict(zip(ACTIONS, deterministic_permutation(seed_material)))

def realized_mapping(condition, f):
    if condition == "INFORMATIVE":
        return dict(f)
    if condition == "SURFACE_PERMUTED":
        return {a: SURFACE_PERMUTATION[f[a]] for a in ACTIONS}
    if condition == "CONTRADICTORY":
        return {a: CONTRADICTORY_PERMUTATION[f[a]] for a in ACTIONS}
    raise ValueError("NULL realization requires null_mapping.")

def make_unit(d, o, condition, p, permutation_index, replicate):
    f_profiles = deterministic_permutation("|".join([
        "F", d, o, condition, p, str(permutation_index), str(replicate)
    ]))
    f = dict(zip(ACTIONS, f_profiles))
    assert validate_bijection(f)

    z = null_mapping(d, o, p, replicate) if condition == "UNINFORMATIVE_NULL"         else realized_mapping(condition, f)
    assert validate_bijection(z)

    s_t = baseline_state(d)
    task_context = TASK_CONTEXT.copy()
    presented_profiles = [
        {"action": action, "profile_id": f[action], "profile": PROFILE_VALUES[f[action]]}
        for action in ACTIONS
    ]

    return {
        "version": "NEXT3_v003",
        "unit_id": f"{d}|{o}|{condition}|{p}|k{permutation_index:02d}|r{replicate:02d}",
        "domain": d,
        "operationalisation": o,
        "mapping_condition_metadata": condition,
        "presentation": p,
        "permutation_index": permutation_index,
        "replicate": replicate,
        "actions": ACTIONS,
        "S_t": s_t,
        "S_t_sha256": digest(s_t),
        "task_context": task_context,
        "task_context_sha256": digest(task_context),
        "f": f,
        "presented_profiles": presented_profiles,
        "z": z,
        "profile_values": PROFILE_VALUES,
        "scientific_execution": False,
    }

def generate(output_path):
    rows = [
        make_unit(d, o, c, p, k, r)
        for d in DOMAINS
        for o in OPERATIONALISATIONS
        for c in CONDITIONS
        for p in PRESENTATIONS
        for k in range(24)
        for r in range(1, REPLICATES + 1)
    ]
    assert len(rows) == 230400
    assert all(validate_bijection(row["f"]) and validate_bijection(row["z"]) for row in rows)
    assert all(len(row["S_t"]["active"]) == 2 for row in rows)
    assert all(row["S_t"]["relations"] == [] and row["S_t"]["constraints"] == [] for row in rows)

    output = {
        "fixture_id": "TI001_V012_NEXT3_CANDIDATE_FIXTURE_003",
        "status": "CANDIDATE_NOT_FROZEN",
        "version": "NEXT3_v003",
        "requirements_reference": REQUIREMENTS_HASH,
        "semantics_reference": SEMANTICS_HASH,
        "baseline_state_specification": BASELINE_STATE_SPEC,
        "task_context_specification": CONTEXT_SPEC,
        "unit_count": len(rows),
        "domain_count": 4,
        "operationalisation_count": 5,
        "condition_count": 4,
        "presentation_count": 4,
        "permutations_per_cell": 24,
        "replicates_per_cell": REPLICATES,
        "rows": rows,
        "scientific_execution_authorized": False,
    }
    text = json.dumps(output, ensure_ascii=False, sort_keys=True, indent=2) + "\n"
    Path(output_path).write_text(text, encoding="utf-8")
    return hashlib.sha256(text.encode("utf-8")).hexdigest(), len(rows)

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
