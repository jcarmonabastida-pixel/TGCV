#!/usr/bin/env python3
"""Build the frozen TR-131 V006 input package from canonical evidence.

No scientific execution is performed. E1/E2 agreement is checked before
normalization into the frozen cross-domain schema.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
VA1 = ROOT / "results/TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR1_RUN_001.json"
VA2 = ROOT / "results/TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR2_RECONSTRUCTION_001.json"
P1 = ROOT / "A6_EXECUTOR_1_OUTPUT.json"
P2 = ROOT / "A6_EXECUTOR_2_OUTPUT.json"
OUT = ROOT / "TR131_CROSS_DOMAIN_COMPARISON_PACKAGE_V006_INPUT_001.json"

def canon(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def load(p):
    return json.loads(p.read_text(encoding="utf-8"))

def check_visitall(a, b):
    if len(a["nodes"]) != len(b["nodes"]):
        raise RuntimeError("VISITALL_NODE_COUNT_MISMATCH")
    fields = ("branch","depth","S_t","T_acc_t","T_acc_hash","T_real_t",
              "T_acc_parent","Delta_T_acc_from_parent","baseline")
    bmap = {(n["branch"], n["depth"]): n for n in b["nodes"]}
    for n in a["nodes"]:
        m = bmap[(n["branch"], n["depth"])]
        for f in fields:
            if canon(n.get(f)) != canon(m.get(f)):
                raise RuntimeError(f"VISITALL_E1_E2_MISMATCH:{n['branch']}:{f}")

def build_visitall(a):
    nodes = {n["branch"]: n for n in a["nodes"]}
    out = []
    for n in a["nodes"]:
        if n["depth"] == 0:
            continue
        parent = nodes[".".join(n["branch"].split(".")[:-1])]
        out.append({
            "domain": "VisitAll",
            "record_id": f"VisitAll:{n['branch']}",
            "S_t": parent["S_t"],
            "T_acc_t": parent["T_acc_t"],
            "T_real_t": n["T_real_t"],
            "S_t1": n["S_t"],
            "T_acc_t1": n["T_acc_t"],
            "trajectory_id": "grid-5",
            "step": n["depth"],
        })
    return out

def check_prism(a, b):
    if canon(a["rows"]) != canon(b["rows"]):
        raise RuntimeError("PRISM_E1_E2_MISMATCH")

def build_prism(a):
    states = {canon(r["state"]): r["t_acc"]
              for r in a["rows"] if r["kind"] == "state"}
    out = []
    for i, r in enumerate(a["rows"]):
        if r["kind"] != "transition":
            continue
        s, t = canon(r["source"]), canon(r["successor"])
        if s not in states or t not in states:
            raise RuntimeError(f"PRISM_STATE_MISSING:{i}")
        out.append({
            "domain": "PRISM",
            "record_id": f"PRISM:T{i}",
            "S_t": r["source"],
            "T_acc_t": r["t_acc"],
            "T_real_t": r["transformation"],
            "S_t1": r["successor"],
            "T_acc_t1": states[t],
            "trajectory_id": "leader_sync3_2",
            "step": i,
        })
    return out

def main():
    va1, va2, p1, p2 = map(load, (VA1, VA2, P1, P2))
    check_visitall(va1, va2)
    check_prism(p1, p2)
    records = build_visitall(va1) + build_prism(p1)
    package = {
        "protocol": "TR131_CROSS_DOMAIN_COMPARISON_PROTOCOL_FREEZE_001",
        "package_type": "TR131_CROSS_DOMAIN_COMPARISON_PACKAGE_V006_INPUT",
        "records": records,
    }
    raw = json.dumps(package, sort_keys=True, indent=2, ensure_ascii=False) + "\n"
    OUT.write_text(raw, encoding="utf-8")
    print(json.dumps({
        "status": "PACKAGE_BUILT",
        "VisitAll_records": sum(r["domain"] == "VisitAll" for r in records),
        "PRISM_records": sum(r["domain"] == "PRISM" for r in records),
        "total_records": len(records),
        "input_sha256": hashlib.sha256(raw.encode()).hexdigest(),
        "output": str(OUT),
    }, ensure_ascii=False))

if __name__ == "__main__":
    main()
