#!/usr/bin/env python3
"""Independent NEXT3 reconstruction harness.

This artifact intentionally reimplements the transition logic independently
from the scientific executor interface and performs no scientific execution.
"""

import hashlib
import json


ACTIONS = ["A", "B", "C", "D"]
SLOTS = ["slot_1", "slot_2", "slot_3", "slot_4"]

PROFILE_VALUES = {
    "slot_1": {
        "reachable_change_count": 1,
        "constraint_count": 1,
        "composition_depth": 1,
        "dependency_count": 1,
    },
    "slot_2": {
        "reachable_change_count": 2,
        "constraint_count": 1,
        "composition_depth": 1,
        "dependency_count": 2,
    },
    "slot_3": {
        "reachable_change_count": 3,
        "constraint_count": 2,
        "composition_depth": 2,
        "dependency_count": 2,
    },
    "slot_4": {
        "reachable_change_count": 4,
        "constraint_count": 3,
        "composition_depth": 3,
        "dependency_count": 3,
    },
}

DOMAIN_TAGS = {
    "D1_spatial_planning": ("spatial_node", "spatial_relation"),
    "D2_resource_planning": ("resource_node", "allocation_relation"),
    "D3_graph_reconfiguration": ("graph_node", "graph_edge"),
    "D4_workflow_state_machine": ("workflow_state", "workflow_transition"),
}


def canonical(obj):
    return json.dumps(
        obj,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def canon(obj):
    return canonical(obj)


def sha256(obj):
    return hashlib.sha256(
        canonical(obj).encode("utf-8")
    ).hexdigest()


def h(obj):
    return sha256(obj)


def _element_id(element):
    if isinstance(element, dict):
        return int(element["id"])
    return int(element)


def _sort_elements(elements):
    return sorted(elements, key=_element_id)


def _sort_structures(values):
    return sorted(values, key=canonical)


def _next_base_id(active):
    ids = [_element_id(x) for x in active]
    return max(ids, default=0) + 1


def _add_cardinality(active, profile, domain):
    element_type, _ = DOMAIN_TAGS[domain]
    base = _next_base_id(active)

    for i in range(profile["reachable_change_count"]):
        active.append(
            {
                "id": base + i,
                "type": element_type,
                "domain": domain,
            }
        )


def _add_topology(active, relations, profile, action, domain):
    _, relation_type = DOMAIN_TAGS[domain]

    ordered = _sort_elements(active)
    if len(ordered) < 2:
        return

    src = _element_id(ordered[-1])
    dst = _element_id(ordered[-2])

    for i in range(profile["dependency_count"]):
        relations.append(
            [
                src,
                dst,
                relation_type,
                action,
                domain,
                i,
            ]
        )


def _add_depth(active, relations, profile, action, domain):
    _, relation_type = DOMAIN_TAGS[domain]

    ordered = _sort_elements(active)
    if len(ordered) < 2:
        return

    for layer in range(profile["composition_depth"]):
        src_index = max(0, len(ordered) - 1 - layer)
        dst_index = max(0, src_index - 1)

        src = _element_id(ordered[src_index])
        dst = _element_id(ordered[dst_index])

        relations.append(
            [
                src,
                dst,
                relation_type,
                action,
                domain,
                "layer",
                layer,
            ]
        )


def _add_constraints(
    constraints,
    profile,
    action,
    slot,
    domain,
    operationalisation,
):
    for i in range(profile["constraint_count"]):
        constraints.append(
            [
                action,
                slot,
                domain,
                operationalisation,
                i,
            ]
        )


def apply(
    state,
    action,
    slot,
    domain,
    operationalisation,
):
    """Independent structural transition implementation."""
    if action not in ACTIONS:
        raise ValueError(f"Unknown action: {action}")
    if slot not in PROFILE_VALUES:
        raise ValueError(f"Unknown slot: {slot}")
    if domain not in DOMAIN_TAGS:
        raise ValueError(f"Unknown domain: {domain}")

    s = json.loads(canonical(state))

    active = list(s.get("active", []))
    relations = list(s.get("relations", []))
    constraints = list(s.get("constraints", []))

    profile = PROFILE_VALUES[slot]

    if operationalisation in (
        "O1_cardinality",
        "O5_composition",
    ):
        _add_cardinality(
            active,
            profile,
            domain,
        )

    if operationalisation in (
        "O2_topology",
        "O5_composition",
    ):
        _add_topology(
            active,
            relations,
            profile,
            action,
            domain,
        )

    if operationalisation in (
        "O3_depth",
        "O5_composition",
    ):
        _add_depth(
            active,
            relations,
            profile,
            action,
            domain,
        )

    if operationalisation in (
        "O4_constraints",
        "O5_composition",
    ):
        _add_constraints(
            constraints,
            profile,
            action,
            slot,
            domain,
            operationalisation,
        )

    s["active"] = _sort_elements(active)
    s["relations"] = _sort_structures(relations)
    s["constraints"] = _sort_structures(constraints)

    return s


def valid(state):
    active = {
        _element_id(x)
        for x in state.get("active", [])
    }

    for relation in state.get("relations", []):
        if len(relation) < 2:
            return False
        if int(relation[0]) not in active:
            return False
        if int(relation[1]) not in active:
            return False

    return True


def realized_transformation(s0, s1):
    s0_active = {
        _element_id(x)
        for x in s0.get("active", [])
    }
    s1_active = {
        _element_id(x)
        for x in s1.get("active", [])
    }

    return {
        "added_active": sorted(s1_active - s0_active),
        "added_relations": [
            r
            for r in s1.get("relations", [])
            if r not in s0.get("relations", [])
        ],
        "added_constraints": [
            c
            for c in s1.get("constraints", [])
            if c not in s0.get("constraints", [])
        ],
    }


def enumerate_t_acc(
    state,
    domain,
    operationalisation,
):
    out = []

    for action in ACTIONS:
        for slot in SLOTS:
            nxt = apply(
                state,
                action,
                slot,
                domain,
                operationalisation,
            )

            if valid(nxt):
                transformation = realized_transformation(
                    state,
                    nxt,
                )

                out.append(
                    {
                        "action": action,
                        "slot": slot,
                        "state_sha256": sha256(nxt),
                        "transformation": transformation,
                        "transformation_sha256": sha256(
                            transformation
                        ),
                    }
                )

    return sorted(out, key=canonical)


def reconstruct(
    state,
    action,
    z,
    domain,
    operationalisation,
):
    """Reconstruct successor, transformation and T_acc independently."""
    if action not in z:
        raise ValueError(
            f"No z mapping for selected action: {action}"
        )

    slot = z[action]

    successor = apply(
        state,
        action,
        slot,
        domain,
        operationalisation,
    )

    if not valid(successor):
        raise ValueError("invalid")

    transformation = realized_transformation(
        state,
        successor,
    )

    t_acc = enumerate_t_acc(
        successor,
        domain,
        operationalisation,
    )

    successor_hash = sha256(successor)
    transformation_hash = sha256(transformation)
    t_acc_hash = sha256(t_acc)

    return {
        "S_t_plus_1": successor,
        "realized_transformation": transformation,
        "T_acc": t_acc,

        "successor_sha256": successor_hash,
        "transformation_sha256": transformation_hash,
        "T_acc_sha256": t_acc_hash,

        "S_t_plus_1_sha256": successor_hash,
        "realized_transformation_sha256": transformation_hash,
        "T_acc_t_plus_1_sha256": t_acc_hash,
        "t_acc_sha256": t_acc_hash,
    }
