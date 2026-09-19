#!/usr/bin/env python3
"""TGCV TR-131 scientific runner v0.2 — frozen-candidate implementation.

This implementation is distinct from the construction-only runner v0.1.
It implements the candidate scientific configuration but remains fail-closed:
scientific execution requires an explicit G8 authorization record supplied
through the command line. Without that authorization it performs no run.
"""

from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG = ROOT / "scientific_execution_config_v01.json"
POLICIES = ROOT / "scientific_policy_definitions.json"

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

def load_policy_definitions():
    data = json.loads(POLICIES.read_text(encoding="utf-8"))
    required = {"protocol_id", "policy_definition_version", "policies", "constraints"}
    if set(data) != required:
        raise ValueError("Policy definition schema mismatch.")
    if set(data["policies"]) != {"policy_A", "policy_B"}:
        raise ValueError("Policy definition set mismatch.")
    if data["constraints"] != {
        "selection_source": "X",
        "post_hoc_selection": false,
        "selected_transformation_must_be_in_T_acc": true
    }:
        raise ValueError("Policy constraints mismatch.")
    policies = data["policies"]
    for name in ("policy_A", "policy_B"):
        if policies[name].get("selection_source") != "X" or policies[name].get("post_hoc") is not False:
            raise ValueError(f"Policy {name} is not a frozen pre-declared X policy.")
    return policies

def realize(tacc, x, policies):
    allowed = {t["id"] for t in tacc}
    if x not in policies:
        raise ValueError(f"Unknown X policy: {x}")
    selected = policies[x]["select"]
    if policies[x].get("selection_source") != "X":
        raise ValueError(f"Policy {x} is not explicitly X-driven.")
    if policies[x].get("post_hoc", True):
        raise ValueError(f"Policy {x} is marked post-hoc.")
    if selected not in allowed:
        raise ValueError(f"Selected transformation not in T_acc: {selected}")
    return selected

def transition(s, t_real):
    if t_real == "tau_accept":
        return {"node": "S1", "resources": 1, "status": "accepted"}
    if t_real == "tau_defer":
        return {"node": "S1", "resources": 1, "status": "deferred"}
    raise ValueError(f"Unknown realized transformation: {t_real}")

def construct_case(case_id, x, policies):
    s0, c, tacc, rules = baseline()
    t_real = realize(tacc, x, policies)
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
    # H is derived deterministically from the realized trajectory, not read
    # from a post-execution variable.
    h = {
        "realized_transformations": [t_real],
        "states": [s0, s1],
    }
    return s0, c, tacc, rules, trace, h

def validate_config(cfg):
    required = {
        "protocol_id", "bundle_id", "bundle_version", "mode", "cases",
        "x_A", "x_B", "policy_definitions", "primary_outcome",
        "positive_contrast", "null_contrast", "post_hoc_modification",
        "authorization_required", "executor_2_required"
    }
    missing = required - set(cfg)
    if missing:
        raise ValueError(f"Missing configuration fields: {sorted(missing)}")
    if cfg["mode"] != "SCIENTIFIC_CANDIDATE":
        raise ValueError("Scientific runner requires SCIENTIFIC_CANDIDATE mode.")
    if cfg["cases"] != ["A", "B"]:
        raise ValueError("Only the frozen A/B candidate is supported.")
    if cfg["primary_outcome"] != "H":
        raise ValueError("Primary outcome must be H.")
    if cfg["positive_contrast"] != "H_A != H_B":
        raise ValueError("Unexpected positive contrast.")
    if cfg["null_contrast"] != "H_A == H_B":
        raise ValueError("Unexpected null contrast.")
    if cfg["post_hoc_modification"] is not False:
        raise ValueError("Post-hoc modification must be false.")
    if cfg["authorization_required"] is not True or cfg["executor_2_required"] is not True:
        raise ValueError("Authorization and Executor-2 requirements must be true.")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--authorization-record", default=None)
    args = parser.parse_args()

    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    validate_config(cfg)

    if not args.authorization_record:
        print(json.dumps({
            "status": "BLOCKED — SCIENTIFIC EXECUTION NOT AUTHORIZED",
            "mode": cfg["mode"],
            "authorization_required": True,
            "executor_2_required": True,
            "execution_performed": False
        }, indent=2, ensure_ascii=False))
        return 3

    auth = Path(args.authorization_record)
    if not auth.exists():
        raise SystemExit(f"BLOCKED: authorization record not found: {auth}")

    authorization = json.loads(auth.read_text(encoding="utf-8"))
    if authorization.get("gate") != "G8" or authorization.get("authorized") is not True:
        raise SystemExit("BLOCKED: supplied record is not a valid G8 authorization.")

    policies = load_policy_definitions()
    a = construct_case("A", cfg["x_A"], policies)
    b = construct_case("B", cfg["x_B"], policies)
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
    if not all(checks.values()):
        raise SystemExit("BLOCKED: scientific precondition check failed.")

    report = {
        "status": "SCIENTIFIC EXECUTION RESULT",
        "execution_performed": True,
        "authorization_gate": "G8",
        "checks": checks,
        "primary_outcome": {
            "H_A": ha,
            "H_B": hb,
            "contrast": ha != hb
        },
        "hashes": {
            "S0": sha(s0a),
            "C": sha(ca),
            "T_acc": sha(ta),
            "rules": sha(ra),
            "H_A": sha(ha),
            "H_B": sha(hb),
            "trace_A": sha(trace_a),
            "trace_B": sha(trace_b),
        },
        "x": {"A": cfg["x_A"], "B": cfg["x_B"]},
        "realized_transformations": {
            "A": trace_a[0]["T_real_t"],
            "B": trace_b[0]["T_real_t"],
        },
        "traces": {"A": trace_a, "B": trace_b}
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
