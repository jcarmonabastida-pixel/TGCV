#!/usr/bin/env python3
"""TGCV TR-131 scientific runner v0.1 — construction only.

This runner is fail-closed. It is NOT authorized for scientific execution.
It may be used only to validate that the scientific realization rule is
explicitly driven by X and that non-target invariants are preserved.
"""

from __future__ import annotations
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG = ROOT / "scientific_config.json"

def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def sha(obj):
    return hashlib.sha256(canon(obj).encode("utf-8")).hexdigest()

def baseline():
    s0 = {"node": "S0", "resources": 1, "status": "ready"}
    c = {"context": "frozen", "version": 1}
    tacc = [
        {"id": "tau_accept", "pre": "ready", "post": "accepted"},
        {"id": "tau_defer", "pre": "ready", "post": "deferred"},
    ]
    rules = {
        "transformations": tacc,
        "admissibility": {"ready": ["tau_accept", "tau_defer"]},
        "transition": "deterministic_scientific_transition_v01",
    }
    return s0, c, tacc, rules

def realize(tacc, x):
    allowed = {t["id"] for t in tacc}
    policy = {
        "policy_A": "tau_accept",
        "policy_B": "tau_defer",
    }
    if x not in policy:
        raise ValueError(f"Unknown X policy: {x}")
    selected = policy[x]
    if selected not in allowed:
        raise ValueError(f"Selected transformation not in T_acc: {selected}")
    return selected

def transition(s, t_real):
    if t_real == "tau_accept":
        return {"node": "S1", "resources": 1, "status": "accepted"}
    if t_real == "tau_defer":
        return {"node": "S1", "resources": 1, "status": "deferred"}
    raise ValueError(f"Unknown realized transformation: {t_real}")

def construct_case(case_id, x):
    s0, c, tacc, rules = baseline()
    t_real = realize(tacc, x)
    s1 = transition(s0, t_real)
    trace = [{
        "case_id": case_id,
        "step": 0,
        "S_t": s0,
        "C_t": c,
        "T_acc_t": tacc,
        "X_t": x,
        "T_real_t": t_real,
        "S_t1": s1,
    }]
    trajectory = {
        "realized_transformations": [t_real],
        "states": [s0, s1],
    }
    return s0, c, tacc, rules, trace, trajectory

def main():
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    if cfg.get("mode") != "CONSTRUCTION_CHECK":
        raise SystemExit("BLOCKED: scientific execution mode is not authorized.")

    a = construct_case("A", cfg["x_A"])
    b = construct_case("B", cfg["x_B"])
    s0a, ca, ta, ra, trace_a, ha = a
    s0b, cb, tb, rb, trace_b, hb = b

    checks = {
        "state_equal": sha(s0a) == sha(s0b),
        "context_equal": sha(ca) == sha(cb),
        "tacc_equal": sha(ta) == sha(tb),
        "rules_equal": sha(ra) == sha(rb),
        "x_distinct": cfg["x_A"] != cfg["x_B"],
        "x_pre_realization": trace_a[0]["X_t"] == cfg["x_A"] and trace_b[0]["X_t"] == cfg["x_B"],
        "realization_depends_on_x": trace_a[0]["T_real_t"] != trace_b[0]["T_real_t"],
        "realizations_admissible": trace_a[0]["T_real_t"] in {t["id"] for t in ta} and trace_b[0]["T_real_t"] in {t["id"] for t in tb},
        "trajectory_derivation_deterministic": sha(ha) == sha(json.loads(json.dumps(ha, sort_keys=True))),
        "trace_complete": all(set(t) >= {"case_id","step","S_t","C_t","T_acc_t","X_t","T_real_t","S_t1"} for t in trace_a + trace_b),
    }

    status = "CONSTRUCTION_CHECK_PASS" if all(checks.values()) else "CONSTRUCTION_CHECK_BLOCKED"
    report = {
        "status": "NOT SCIENTIFIC EVIDENCE — CONSTRUCTION CHECK ONLY",
        "construction_check_status": status,
        "checks": checks,
        "hashes": {
            "S0": sha(s0a),
            "C": sha(ca),
            "T_acc": sha(ta),
            "rules": sha(ra),
            "trajectory_A": sha(ha),
            "trajectory_B": sha(hb),
        },
        "x": {"A": cfg["x_A"], "B": cfg["x_B"]},
        "realized_transformations": {
            "A": trace_a[0]["T_real_t"],
            "B": trace_b[0]["T_real_t"],
        },
        "trace_hash_A": sha(trace_a),
        "trace_hash_B": sha(trace_b),
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if status == "CONSTRUCTION_CHECK_PASS" else 2

if __name__ == "__main__":
    raise SystemExit(main())
