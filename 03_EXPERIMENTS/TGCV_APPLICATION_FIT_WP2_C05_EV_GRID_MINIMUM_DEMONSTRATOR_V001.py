"""TGCV Application Fit WP2 — C05 EV–Grid Minimum Demonstrator V001.

Frozen, deterministic, offline runner. It implements only the rules in the
C05 specification/fixture and emits a JSON execution record. It does not
perform inference, optimization, network access, or value evaluation.
"""
from __future__ import annotations

import hashlib
import json
import platform
import sys
from copy import deepcopy
from pathlib import Path

MODE = "C05_EV_GRID_SYNTHETIC_MINIMUM_DEMONSTRATOR_V001"
SPEC_COMMIT = "5aa2c7e20ea3f5775b2d6e60797f9be9efe10e05"
FIXTURE_COMMIT = "9dd6e9b6bb8d0b7a7e686c4dc61926fc627fa8b6"

U_TAU = [
    "accept_A", "accept_B", "defer", "reduce_power", "shift_window",
    "redirect_A_to_B", "redirect_B_to_A", "reserve_capacity",
    "release_capacity", "v1g_discharge", "v2g_discharge", "reject",
]


def sha256_obj(obj):
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=True).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def base_state_context():
    s = {
        "site_assignment": {"EV1": "A", "EV2": "B"},
        "charging_state": {"EV1": "idle", "EV2": "idle"},
        "grid_capacity_state": "high",
        "active_power": {"A": 0, "B": 0},
        "EV_energy_state": {"EV1": 20, "EV2": 20},
    }
    c = {
        "departure_requirement": {"EV1": 24, "EV2": 24},
        "mobility_requirement": {"EV1": "required", "EV2": "required"},
        "site_capacity": {"A": 11, "B": 11},
        "grid_limit": 22,
        "charging_policy": "standard_then_reduced",
        "V1G_V2G_capability": {"EV1": "available", "EV2": "unavailable"},
    }
    l = {
        "grid_safety": True,
        "site_charging_constraints": True,
        "EV_state_constraints": True,
        "mobility_departure_constraints": True,
        "charging_policy_constraints": True,
    }
    return s, c, l


def admissible(s, c, l):
    assert l
    energies = s["EV_energy_state"]
    req = c["departure_requirement"]
    site = c["site_capacity"]
    grid = c["grid_limit"]
    active = s["active_power"]
    assignment = s["site_assignment"]
    result = []
    unmet = any(energies[e] < req[e] for e in energies)
    if site["A"] > 0 and assignment["EV1"] == "A" and active["A"] + 4 <= site["A"] and sum(active.values()) + 4 <= grid:
        result.append("accept_A")
    if site["B"] > 0 and assignment["EV2"] == "B" and active["B"] + 4 <= site["B"] and sum(active.values()) + 4 <= grid:
        result.append("accept_B")
    if unmet:
        result.append("defer")
    if any(site[x] >= active[x] + 2 and active[x] + 2 <= grid for x in ("A", "B")):
        result.append("reduce_power")
    if unmet and c["charging_policy"] == "standard_then_reduced":
        result.append("shift_window")
    if assignment["EV1"] == "A" and site["B"] > 0 and c["mobility_requirement"]["EV1"] == "required" and sum(active.values()) + 4 <= grid:
        result.append("redirect_A_to_B")
    if assignment["EV2"] == "B" and site["A"] > 0 and c["mobility_requirement"]["EV2"] == "required" and sum(active.values()) + 4 <= grid:
        result.append("redirect_B_to_A")
    if sum(active.values()) < grid and any(site[x] > active[x] for x in ("A", "B")):
        result.append("reserve_capacity")
    if s.get("reserved_capacity", False):
        result.append("release_capacity")
    if c["V1G_V2G_capability"]["EV1"] == "available" and energies["EV1"] > req["EV1"]:
        result.append("v1g_discharge")
    if c["V1G_V2G_capability"]["EV2"] == "available" and energies["EV2"] > req["EV2"]:
        result.append("v2g_discharge")
    if not any(x in result for x in ("accept_A", "accept_B", "reduce_power", "redirect_A_to_B", "redirect_B_to_A")):
        result.append("reject")
    return [x for x in U_TAU if x in result]


def baseline(s, c, l):
    # Same information, constraints and action universe; conventional feasible set.
    return admissible(s, c, l)


def apply_transition(name, s, c):
    s, c = deepcopy(s), deepcopy(c)
    if name == "T1": c["grid_limit"] = 8; s["grid_capacity_state"] = "constrained"
    elif name == "T2": c["departure_requirement"] = {"EV1": 28, "EV2": 28}
    elif name == "T3": c["site_capacity"]["B"] = 0
    elif name == "T4": c["departure_requirement"] = {"EV1": 26, "EV2": 26}
    elif name == "T5": c["V1G_V2G_capability"]["EV2"] = "available"
    elif name == "T6": c["grid_limit"] = 8; c["departure_requirement"] = {"EV1": 26, "EV2": 26}; s["grid_capacity_state"] = "constrained"
    elif name == "NC1": c["telemetry_label"] = "recalibrated"
    elif name == "NC2": s["selection_tiebreak"] = "reverse_lexical"
    else: raise ValueError(name)
    return s, c


def trajectory(s, c, acc):
    priority = ["accept_A", "accept_B", "reduce_power", "redirect_A_to_B", "redirect_B_to_A", "defer", "shift_window", "reserve_capacity", "release_capacity", "v1g_discharge", "v2g_discharge", "reject"]
    chosen = next((x for x in priority if x in acc), None)
    return {"policy": "frozen_priority", "selected_transformation": chosen, "accessible_count": len(acc)}


def run():
    s0, c0, l = base_state_context()
    transitions = ["T1", "T2", "T3", "T4", "T5", "T6", "NC1", "NC2"]
    records = []
    for name in transitions:
        s1, c1 = apply_transition(name, s0, c0)
        a0 = admissible(s0, c0, l)
        a1 = admissible(s1, c1, l)
        b1 = baseline(s1, c1, l)
        opened = [x for x in a1 if x not in a0]
        closed = [x for x in a0 if x not in a1]
        rec = {
            "transition_id": name,
            "S0": s0,
            "C0": c0,
            "L": l,
            "U_tau": U_TAU,
            "T_acc_0": a0,
            "S1": s1,
            "C1": c1,
            "T_acc_1": a1,
            "Delta_T_acc": {"opened": opened, "closed": closed, "reordered": []},
            "trajectory": trajectory(s1, c1, a1),
            "baseline_reconstruction": b1,
            "baseline_equivalent": b1 == a1,
            "comparison_observations": {"representation_difference": "none" if b1 == a1 else "observed"},
        }
        if name in ("NC1", "NC2") and (a0 != a1):
            raise RuntimeError(name + " violated negative-control contract")
        records.append(rec)
    payload = {
        "mode": MODE,
        "status": "C05_EXECUTION_COMPLETE",
        "spec_commit": SPEC_COMMIT,
        "fixture_commit": FIXTURE_COMMIT,
        "python_version": platform.python_version(),
        "platform": platform.platform(),
        "U_tau": U_TAU,
        "transitions": records,
        "nonclaims": ["no scientific validity", "no causal validity", "no superiority", "no generality", "no value/ROI", "no deployment readiness"],
    }
    payload["output_hash"] = sha256_obj(payload)
    return payload


if __name__ == "__main__":
    out = run()
    print(json.dumps(out, indent=2, sort_keys=True))
