"""Audit the corrected RUST-DYN primary JSON without re-reading the dataset."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

DATASET_SHA256 = "823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224"
TEMPORAL_RULE_ID = "DR-035-v0.1-ADJACENT-CREATED-AT"
HORIZON = 1
EXPECTED_TOTAL = 516061
EXPECTED_CLASSES = {"PERSISTENCE": 77858, "EXPANSION": 8295, "CONTRACTION": 3786, "RECONFIGURATION": 426122}


def sha256_file(p: Path) -> str:
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(1024*1024),b""): h.update(b)
    return h.hexdigest()


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input", required=True)
    ap.add_argument("--output", required=False)
    a=ap.parse_args()
    p=Path(a.input)
    d=json.loads(p.read_text(encoding="utf-8"))
    rows=d.get("pairs",[])
    tests={}
    tests["mode"] = d.get("MODE")=="REAL_DATASET_EXECUTION"
    tests["pass_flag"] = d.get("pass") is True
    tests["dataset_sha256"] = d.get("dataset_sha256")==DATASET_SHA256
    tests["temporal_rule"] = d.get("temporal_rule_id")==TEMPORAL_RULE_ID
    tests["horizon"] = d.get("horizon")==HORIZON
    tests["pair_count"] = d.get("temporal_pair_count")==len(rows)==EXPECTED_TOTAL
    tests["class_counts"] = d.get("classification_counts")==EXPECTED_CLASSES
    tests["unique_pairs"] = len({(r.get("origin_a"),r.get("origin_b")) for r in rows})==len(rows)
    tests["directional_pairs"] = all(r.get("origin_a")!=r.get("origin_b") for r in rows)
    tests["class_semantics"] = all((r["class"]=="PERSISTENCE" and not r["delta_tacc"]) or (r["class"]!="PERSISTENCE" and r["delta_tacc"]) for r in rows)
    tests["exact_delta_counts"] = all(r["delta_tacc_added_count"]==0 and r["delta_tacc_removed_count"]==0 if r["class"]=="PERSISTENCE" else True for r in rows)
    tests["tacc_hashes_present"] = all(isinstance(r.get("tacc_a_hash"),str) and len(r["tacc_a_hash"])==64 and isinstance(r.get("tacc_b_hash"),str) and len(r["tacc_b_hash"])==64 for r in rows)
    tests["firewall"] = d.get("firewall")=={
        "outcome_read":False,"future_activity_read":False,"predictive_metrics":False,"sampling":False,
        "post_origin_metadata":False,"reach_used_to_construct_tacc":False,"trajectory_used_to_construct_tacc":False}
    tests["reach_trajectory_exclude_origin"] = all(r["origin_a"] not in r.get("trajectory_a_h1",[]) and r["origin_b"] not in r.get("trajectory_b_h1",[]) for r in rows)
    tests["trajectory_sorted"] = all(r.get("trajectory_a_h1",[])==sorted(r.get("trajectory_a_h1",[])) and r.get("trajectory_b_h1",[])==sorted(r.get("trajectory_b_h1",[])) for r in rows)
    result={"MODE":"PRIMARY_EXECUTION_AUDIT","pass":all(tests.values()),"input":str(p),"input_sha256":sha256_file(p),"tests":tests,"row_count":len(rows),"expected_dataset_sha256":DATASET_SHA256,"temporal_rule_id":TEMPORAL_RULE_ID,"horizon":HORIZON}
    text=json.dumps(result,indent=2,sort_keys=True)
    print(text)
    if a.output: Path(a.output).write_text(text,encoding="utf-8")
    return 0 if result["pass"] else 7
if __name__=="__main__": raise SystemExit(main())
