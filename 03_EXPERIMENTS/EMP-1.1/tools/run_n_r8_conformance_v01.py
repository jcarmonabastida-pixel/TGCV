"""N-R8.3 conformance runner v0.1.

Fail-closed structural tests only. No learner fitting, outcomes, N-R7 result
reads, or scientific execution are permitted here.
"""
from __future__ import annotations
import hashlib
import inspect
import json
import pathlib
import random
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
SRC = ROOT / "EMP-1.1" / "src" / "branch_n_r8_operationalisation_v01.py"
sys.path.insert(0, str(SRC.parent))
import branch_n_r8_operationalisation_v01 as m


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def check(name, fn):
    try:
        ok, detail = fn()
        return {"check":name,"status":"PASS" if ok else "FAIL","detail":detail}
    except Exception as e:
        return {"check":name,"status":"FAIL","detail":repr(e)}

def main():
    results=[]
    results.append(check("implementation_exists", lambda:(SRC.exists(), str(SRC))))
    results.append(check("g2_determinism", lambda: (
        m.generate_g2(random.Random(5100000)).canonical()==m.generate_g2(random.Random(5100000)).canonical(), "same seed => same state")))
    results.append(check("g2_schema", lambda: (
        set(m.generate_g2(random.Random(5100000)).canonical())=={"components","edges","objective","resources"}, "canonical state schema")))
    results.append(check("g2_differs_from_g1", lambda: (
        sum(len(m.generate_g2(random.Random(5100000+i)).edges) for i in range(100)) != sum(len(m.generate_g1(random.Random(3100000+i)).edges) for i in range(100)), "100-state edge-count aggregate differs")))
    s=m.generate_g2(random.Random(5100001))
    results.append(check("r1_enumeration_determinism", lambda:(m.tacc(s)==m.tacc(s), "T_acc deterministic")))
    results.append(check("r2_dimension", lambda:(len(m.r2(s))==24, f"dimension={len(m.r2(s))}")))
    empty=m.canonical_state(("A1","A2","B1"),(),(0,0,0),"O01")
    results.append(check("r2_empty_zero", lambda:(m.r2(empty)==(0.0,)*24, "empty T_acc => 24 zeros")))
    results.append(check("r2_determinism", lambda:(m.r2(s)==m.r2(s), "same state => same R2")))
    src_text=SRC.read_text(encoding="utf-8")
    results.append(check("no_learner_dependency", lambda:(not any(x in src_text for x in ("sklearn","fit(","predict(","log_loss")), "no learner symbols")))
    results.append(check("no_outcome_dependency", lambda:(not any(x in src_text for x in ("primary_results","Y","outcome","trajectory")), "no outcome/trajectory symbols")))
    results.append(check("no_n_r7_result_literals", lambda:("0.2301141852417799" not in src_text and "0.13000700462954773" not in src_text, "no sealed N-R7 result literals")))
    results.append(check("source_hash_recordable", lambda:(len(sha(SRC))==64, sha(SRC))))
    payload={"runner":"N_R8_CONFORMANCE_RUNNER_v0.1","implementation_sha256":sha(SRC),"results":results}
    print(json.dumps(payload,sort_keys=True,indent=2))
    if any(x["status"]!="PASS" for x in results): raise SystemExit(1)

if __name__=="__main__": main()
