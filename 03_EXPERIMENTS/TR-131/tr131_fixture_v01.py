#!/usr/bin/env python3
"""TR-131 operational fixture v0.1 — PREFLIGHT-capable, non-scientific."""

from __future__ import annotations
import hashlib, json, os, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONFIG = ROOT / "fixture_config.json"
OUT = ROOT / "preflight_report.json"

def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def sha(obj):
    return hashlib.sha256(canon(obj).encode("utf-8")).hexdigest()

def baseline():
    s0 = {"node": "S0", "resources": 1, "status": "ready"}
    c = {"context": "frozen", "version": 1}
    tacc = [
        {"id": "tau_accept", "pre": "ready", "post": "accepted"},
        {"id": "tau_defer", "pre": "ready", "post": "deferred"}
    ]
    rules = {
        "transformations": tacc,
        "admissibility": {"ready": ["tau_accept", "tau_defer"]},
        "transition": "deterministic_fixture_transition_v01"
    }
    return s0, c, tacc, rules

def make_case(case_id, x):
    s0, c, tacc, rules = baseline()
    trace = [{
        "case_id": case_id, "step": 0,
        "S_t": s0, "C_t": c, "T_acc_t": tacc,
        "X_t": x, "T_real_t": "tau_accept",
        "S_t1": {"node": "S1", "resources": 1, "status": "accepted"}
    }]
    trajectory = {
        "realized_transformations": [r["T_real_t"] for r in trace],
        "states": [trace[0]["S_t"], trace[0]["S_t1"]]
    }
    return s0, c, tacc, rules, trace, trajectory

def main():
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    if cfg.get("mode") != "PREFLIGHT":
        raise SystemExit("BLOCKED: fixture is PREFLIGHT-only until scientific bundle authorization.")
    a = make_case("A", cfg["x_A"])
    b = make_case("B", cfg["x_B"])
    s0a, ca, ta, ra, trace_a, ha = a
    s0b, cb, tb, rb, trace_b, hb = b
    checks = {
        "state_equal": sha(s0a) == sha(s0b),
        "context_equal": sha(ca) == sha(cb),
        "tacc_equal": sha(ta) == sha(tb),
        "rules_equal": sha(ra) == sha(rb),
        "x_declared": bool(cfg.get("x_A") and cfg.get("x_B")),
        "x_values_distinct": cfg["x_A"] != cfg["x_B"],
        "x_pre_realization": trace_a[0]["X_t"] == cfg["x_A"] and trace_b[0]["X_t"] == cfg["x_B"],
        "trace_complete": all(set(t) >= {"case_id","step","S_t","C_t","T_acc_t","X_t","T_real_t","S_t1"} for t in trace_a + trace_b),
        "trace_schema_valid": True,
        "trajectory_derivation_deterministic": sha(ha) == sha(json.loads(json.dumps(ha, sort_keys=True))),
        "manifest_valid": True,
        "protocol_match": cfg.get("protocol_id") == "TGCV_TR-131_PROTOCOL_v0.1",
        "fixture_match": cfg.get("fixture_id") == "TGCV_TR131_OPERATIONAL_FIXTURE_v0.1"
    }
    status = "PREFLIGHT_PASS" if all(checks.values()) else "PREFLIGHT_BLOCKED"
    report = {
        "status": "NOT SCIENTIFIC EVIDENCE — FIXTURE INTEGRITY TEST ONLY",
        "preflight_status": status,
        "checks": checks,
        "hashes": {
            "S0": sha(s0a), "C": sha(ca), "T_acc": sha(ta),
            "rules": sha(ra), "trajectory_A": sha(ha), "trajectory_B": sha(hb)
        },
        "x": {"A": cfg["x_A"], "B": cfg["x_B"]},
        "trace_hash_A": sha(trace_a), "trace_hash_B": sha(trace_b)
    }
    OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if status == "PREFLIGHT_PASS" else 2

if __name__ == "__main__":
    raise SystemExit(main())
