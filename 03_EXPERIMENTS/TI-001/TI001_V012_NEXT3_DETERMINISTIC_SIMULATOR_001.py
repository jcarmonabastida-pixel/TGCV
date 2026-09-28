#!/usr/bin/env python3
"""TI-001 V012 NEXT3 deterministic simulator.

Implementation-only artifact. Does not execute scientific decisions.
"""

import hashlib
import json

PROFILE_VALUES = {
    "slot_1": {"reachable_change_count":1,"constraint_count":1,"composition_depth":1,"dependency_count":1},
    "slot_2": {"reachable_change_count":2,"constraint_count":1,"composition_depth":1,"dependency_count":2},
    "slot_3": {"reachable_change_count":3,"constraint_count":2,"composition_depth":2,"dependency_count":2},
    "slot_4": {"reachable_change_count":4,"constraint_count":3,"composition_depth":3,"dependency_count":3},
}
ACTIONS = ["A","B","C","D"]
SLOTS = ["slot_1","slot_2","slot_3","slot_4"]

def canonical(obj):
    return json.dumps(obj, ensure_ascii=False, sort_keys=True, separators=(",", ":"))

def sha256(obj):
    return hashlib.sha256(canonical(obj).encode("utf-8")).hexdigest()

def apply_edit(state, action, slot, domain, operationalisation):
    s = json.loads(canonical(state))
    active = list(s.get("active", []))
    relations = list(s.get("relations", []))
    constraints = list(s.get("constraints", []))
    profile = PROFILE_VALUES[slot]
    base = len(active) + 1
    change_count = profile["reachable_change_count"]
    for i in range(change_count):
        node = base + i
        if node not in active:
            active.append(node)
    for i in range(profile["dependency_count"]):
        if len(active) >= 2:
            relations.append([active[-1], active[-2], action])
    for i in range(profile["constraint_count"]):
        constraints.append([action, slot, i])
    s["active"] = sorted(set(active))
    s["relations"] = sorted(relations)
    s["constraints"] = sorted(constraints)
    return s

def valid_state(state):
    active = set(state["active"])
    return all(r[0] in active and r[1] in active for r in state["relations"])

def realized_transformation(s0, s1):
    return {
        "added_active": sorted(set(s1["active"]) - set(s0["active"])),
        "added_relations": [r for r in s1["relations"] if r not in s0["relations"]],
        "added_constraints": [c for c in s1["constraints"] if c not in s0["constraints"]],
    }

def enumerate_t_acc(state, domain, operationalisation):
    out = []
    for action in ACTIONS:
        for slot in SLOTS:
            nxt = apply_edit(state, action, slot, domain, operationalisation)
            if valid_state(nxt):
                out.append({
                    "action": action,
                    "slot": slot,
                    "state_sha256": sha256(nxt),
                    "transformation": realized_transformation(state, nxt),
                })
    return sorted(out, key=canonical)

def execute_transition(state, action, z, domain, operationalisation):
    slot = z[action]
    nxt = apply_edit(state, action, slot, domain, operationalisation)
    if not valid_state(nxt):
        raise ValueError("Invalid successor state")
    tr = realized_transformation(state, nxt)
    t_acc = enumerate_t_acc(nxt, domain, operationalisation)
    return {
        "S_t_plus_1": nxt,
        "realized_transformation": tr,
        "T_acc_t_plus_1": t_acc,
        "S_t_plus_1_sha256": sha256(nxt),
        "realized_transformation_sha256": sha256(tr),
        "T_acc_t_plus_1_sha256": sha256(t_acc),
    }
