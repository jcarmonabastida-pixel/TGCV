#!/usr/bin/env python3
"""TR-131 VisitAll Dynamic Transformation Space scientific evaluation audit.

Consumes already-persisted Executor-1/Executor-2 JSON records. It performs no
new scientific execution and does not use outcomes, goals, or value.
"""
from __future__ import annotations
import hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
RESULTS = ROOT / "results"
E1 = RESULTS / "TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR1_RUN_001.json"
E2 = RESULTS / "TR131_VISITALL_DYNAMIC_SPACE_EXECUTOR2_RECONSTRUCTION_001.json"

SOURCE_REV = "cf19edf7c53d1540ddbb396c642595e0926ee552"
SOURCE_BLOB = "f49fb86fb3f7dd4aba5a6ed79fdddc240097ec34"
PROBLEM = "grid-5"
DEPTH = 2

def load(p):
    return json.loads(p.read_text(encoding="utf-8"))

def tacc_from_state(state):
    p = state["at-robot"]
    prefix = "loc-x"
    x, y = map(int, p[len(prefix):].split("-y"))
    out = []
    for nx, ny in ((x-1,y),(x+1,y),(x,y-1),(x,y+1)):
        if 0 <= nx < 5 and 0 <= ny < 5:
            out.append(f"move({p}->{f'loc-x{nx}-y{ny}'})")
    # The frozen adapter identity is move(source->destination).
    return sorted(out)

def norm_ids(ids):
    return sorted(ids)

def digest(v):
    return hashlib.sha256(json.dumps(v, sort_keys=True, separators=(",",":"), ensure_ascii=False).encode()).hexdigest()

def main():
    e1, e2 = load(E1), load(E2)
    checks = {
        "e1_completed": e1.get("status") == "COMPLETED",
        "e2_completed": e2.get("status") == "COMPLETED",
        "e1_authorized_performed": e1.get("scientific_execution_authorized") is True and e1.get("scientific_execution_performed") is True,
        "e2_authorized_performed": e2.get("scientific_execution_authorized") is True and e2.get("scientific_execution_performed") is True,
        "same_source_revision": e1.get("source_revision") == e2.get("source_revision") == SOURCE_REV,
        "same_source_blob": e1.get("source_blob_sha") == e2.get("source_blob_sha") == SOURCE_BLOB,
        "same_problem": e1.get("problem") == e2.get("problem") == PROBLEM,
        "same_depth": e1.get("depth") == e2.get("depth") == DEPTH,
        "same_node_count": e1.get("node_count") == e2.get("node_count") == 21,
        "same_edge_count": e1.get("edge_count") == e2.get("edge_count") == 20,
        "same_leaf_count": e1.get("leaf_count") == e2.get("leaf_count") == 16,
        "same_root_tacc": e1["nodes"][0]["T_acc_t"] == e2["nodes"][0]["T_acc_t"],
    }
    if not all(checks.values()):
        raise SystemExit(json.dumps({"status":"BLOCKED","checks":checks}, indent=2))

    nodes = {n["branch"]: n for n in e1["nodes"]}
    root = nodes["root"]
    root_tacc = norm_ids(root["T_acc_t"])

    # C1: deterministic applicability means no legitimate same-state/different-T_acc
    # contrast exists in this frozen source representation.
    c1 = {
        "status": "NOT_TESTABLE",
        "reason": "T_acc is deterministically reconstructed from S_t and frozen connectivity; no independent context variable exists."
    }

    root_children = [nodes[f"root.{i}"] for i in range(4)]
    c2_realizations = sorted(n["T_real_t"] for n in root_children)
    c2 = {
        "status": "OBSERVED",
        "root_tacc_cardinality": len(root_tacc),
        "distinct_root_realizations": len(set(c2_realizations)),
        "baseline_represents_alternatives": True,
    }

    c3_successors = [json.dumps(n["S_t"], sort_keys=True, separators=(",",":")) for n in root_children]
    c3 = {
        "status": "OBSERVED",
        "distinct_first_step_successor_states": len(set(c3_successors)),
        "depth2_nodes": sum(n["depth"] == 2 for n in nodes.values()),
        "baseline_represents_branching": True,
    }

    # C4 and baseline reconstructibility: every recorded T_acc and delta must be
    # derivable from the state/action applicability relation alone.
    c4_edges = [n for n in nodes.values() if "T_real_t" in n]
    mismatches = []
    nonempty_deltas = 0
    for n in c4_edges:
        derived = tacc_from_state(n["S_t"])
        # The runner's identity uses the same source-defined move syntax.
        if norm_ids(n["T_acc_t"]) != derived:
            mismatches.append(n["branch"])
        d = n["Delta_T_acc_from_parent"]
        if d["Added"] or d["Removed"]:
            nonempty_deltas += 1
        parent = n["T_acc_parent"]
        expected = {"Added": sorted(set(n["T_acc_t"])-set(parent)),
                   "Removed": sorted(set(parent)-set(n["T_acc_t"])),
                   "Retained": sorted(set(parent)&set(n["T_acc_t"]))}
        if d != expected:
            mismatches.append(n["branch"] + ":delta")

    c4 = {
        "status": "OBSERVED",
        "edges_evaluated": len(c4_edges),
        "edges_with_nonempty_delta": nonempty_deltas,
        "tacc_reconstruction_from_state_mismatches": mismatches,
        "baseline_reconstructible": not mismatches,
    }

    representation_gain = (
        c2["status"] == "OBSERVED" and
        c3["status"] == "OBSERVED" and
        c4["status"] == "OBSERVED" and
        c4["baseline_reconstructible"] is False
    )
    overall = "POSITIVE" if representation_gain else "FAIL_NO_DISTINCT_REPRESENTATIONAL_GAIN"

    report = {
        "record_type": "TGCV_TR131_VISITALL_DYNAMIC_SPACE_SCIENTIFIC_EVALUATION_AUDIT",
        "status": "PASS",
        "scientific_result_interpretation": "PERFORMED",
        "source": {"repository":"potassco/pddl-instances","revision":SOURCE_REV,"blob_sha":SOURCE_BLOB,"problem":PROBLEM},
        "depth": DEPTH,
        "input_sha256": {"executor1":digest(e1),"executor2":digest(e2)},
        "checks": checks,
        "cases": {"C1":c1,"C2":c2,"C3":c3,"C4":c4},
        "representation_gain_result": overall,
        "interpretation_boundary": "Domain-specific result for the frozen VisitAll fixture; no claim about other adaptive domains, value causality, or transformational intelligence.",
    }
    print(json.dumps(report, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
