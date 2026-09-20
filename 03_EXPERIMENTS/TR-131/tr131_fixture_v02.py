#!/usr/bin/env python3
"""TR-131 exact-source fixture v0.2 — PREFLIGHT only.

This fixture consumes the canonical source-lock record and reconstructs only
source-defined baseline state / accessible transformation spaces. It does not
perform scientific realization.
"""
from __future__ import annotations
import hashlib, json, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
LOCK = ROOT / "execution" / "TR131_EXACT_FIXTURE_SOURCE_LOCK_v01.json"
CONFIG = ROOT / "fixture_config.json"
OUT = ROOT / "execution" / "TR131_EXACT_FIXTURE_PREFLIGHT_REPORT_v02.json"

def canon(x):
    return json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False)

def sha(x):
    return hashlib.sha256(canon(x).encode()).hexdigest()

def fail(msg):
    raise SystemExit("PREFLIGHT_BLOCKED: " + msg)

def build_visitall(lock):
    v = lock["visitall"]
    s0 = {
        "at-robot": v["initial_state"]["at_robot"],
        "visited": sorted(v["initial_state"]["visited"])
    }
    tacc = [{"id":"move", "from":a.split("->")[0], "to":a.split("->")[1]}
            for a in v["t_acc"]["transformations"]]
    return s0, {"domain":"grid-visit-all","problem":v["problem"]}, tacc

def build_rainbow(lock):
    r = lock["rainbow"]
    s0 = {
        "LB0.dimmer": r["state_defaults"]["LB0_dimmer"],
        "DIMMER_LEVELS": r["state_defaults"]["DIMMER_LEVELS"],
        "DIMMER_MARGIN": r["state_defaults"]["DIMMER_MARGIN"],
        "servers": sorted(r["state_defaults"]["servers"])
    }
    tacc = [{"id":x} for x in r["t_acc_minimum"]["transformations"]]
    return s0, {"model":"SwimSys","revision":r["revision"]}, tacc

def main():
    cfg = json.loads(CONFIG.read_text(encoding="utf-8"))
    lock = json.loads(LOCK.read_text(encoding="utf-8"))

    if cfg.get("mode") != "PREFLIGHT":
        fail("mode is not PREFLIGHT")
    if lock.get("scientific_execution_authorized") is not False:
        fail("source lock authorizes scientific execution")

    va_s, va_c, va_t = build_visitall(lock)
    rw_s, rw_c, rw_t = build_rainbow(lock)

    # Exact source-lock assertions.
    checks = {
        "visitall_source_revision_pinned":
            lock["visitall"]["revision"] == "cf19edf7c53d1540ddbb396c642595e0926ee552",
        "visitall_instance_blob_pinned":
            lock["visitall"]["blob_sha"] == "f49fb86fb3f7dd4aba5a6ed79fdddc240097ec34",
        "visitall_problem_exact":
            lock["visitall"]["problem"] == "grid-5",
        "visitall_tacc_cardinality_exact":
            len(va_t) == 4,
        "visitall_initial_state_exact":
            va_s == {"at-robot":"loc-x2-y2","visited":["loc-x2-y2"]},
        "rainbow_source_revision_pinned":
            lock["rainbow"]["revision"] == "c053e2aab6d58c233016574887296e2be43ca60f4",
        "rainbow_model_blob_pinned":
            lock["rainbow"]["model_blob_sha"] == "9989790020ff1b814e0b1aa7bd1f926d980ce823",
        "rainbow_tactics_blob_pinned":
            lock["rainbow"]["tactics_blob_sha"] == "513a5d78e301e9fa4660b8bac9154b93e6a7a605",
        "rainbow_tacc_minimum_exact":
            len(rw_t) >= 2 and [x["id"] for x in rw_t] == ["TIncDimmer","TRemoveServer"],
        "no_fabricated_instance":
            lock["visitall"]["path"].endswith("instance-1.pddl"),
        "semantic_isomorphism_not_claimed":
            lock["structural_resolution"]["semantic_isomorphism_claim"] is False,
    }

    # A/B invariance is constructed from the same canonical source state.
    x_a, x_b = cfg["x_A"], cfg["x_B"]
    cases = {}
    for case_id, x in (("A",x_a),("B",x_b)):
        cases[case_id] = {
            "X": x,
            "visitall": {"S0":va_s, "C":va_c, "T_acc":va_t},
            "rainbow": {"S0":rw_s, "C":rw_c, "T_acc":rw_t},
            # No scientific realization is performed in PREFLIGHT.
            "realization_status":"NOT_EXECUTED"
        }

    checks.update({
        "x_declared": bool(x_a and x_b),
        "x_values_distinct": x_a != x_b,
        "x_not_in_baseline_A": x_a not in canon(cases["A"]["visitall"]) and x_a not in canon(cases["A"]["rainbow"]),
        "x_not_in_baseline_B": x_b not in canon(cases["B"]["visitall"]) and x_b not in canon(cases["B"]["rainbow"]),
        "visitall_A_B_invariant":
            sha(cases["A"]["visitall"]) == sha(cases["B"]["visitall"]),
        "rainbow_A_B_invariant":
            sha(cases["A"]["rainbow"]) == sha(cases["B"]["rainbow"]),
        "realization_not_executed":
            all(cases[k]["realization_status"]=="NOT_EXECUTED" for k in cases),
    })

    hashes = {
        "visitall_S0":sha(va_s), "visitall_C":sha(va_c), "visitall_T_acc":sha(va_t),
        "rainbow_S0":sha(rw_s), "rainbow_C":sha(rw_c), "rainbow_T_acc":sha(rw_t),
        "case_A":sha(cases["A"]), "case_B":sha(cases["B"]),
        "source_lock":sha(lock),
    }
    status = "PREFLIGHT_PASS" if all(checks.values()) else "PREFLIGHT_BLOCKED"
    report = {
        "record_type":"TGCV_TR131_EXACT_FIXTURE_PREFLIGHT",
        "status":"NOT SCIENTIFIC EVIDENCE — FIXTURE INTEGRITY TEST ONLY",
        "preflight_status":status,
        "scientific_execution_authorized":False,
        "checks":checks,
        "cardinalities":{"VisitAll_T_acc":len(va_t),"Rainbow_T_acc_minimum":len(rw_t)},
        "hashes":hashes,
        "X":{"A":x_a,"B":x_b},
        "realization":"NOT_EXECUTED",
        "source_lock":lock["record_type"]
    }
    OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False)+"\n", encoding="utf-8")
    print(json.dumps(report, indent=2, ensure_ascii=False))
    return 0 if status == "PREFLIGHT_PASS" else 2

if __name__ == "__main__":
    raise SystemExit(main())
