#!/usr/bin/env python3
"""TI-001 V012 V002 independent Executor-2 reconstruction."""
from __future__ import annotations
import argparse, hashlib, json
from pathlib import Path

EXPECTED_FIXTURE_SHA256 = "065ffa5f51fb69b5c9cca8f958bd424375b47b3e2e4e4b5cdb48f4259794a04d"
EXPECTED_COUNT = 72
ACTIONS = ["a", "b", "c"]
ORDERS = {"P1": ["a", "b", "c"], "P2": ["c", "b", "a"]}

def canonical_hash(fixture):
    body = dict(fixture)
    body.pop("fixture_sha256", None)
    raw = json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    return hashlib.sha256(raw).hexdigest()

def expected_records(record):
    ts = record["transition_spec"]
    cond = record["condition"]
    mapping = (
        {a: ts[a]["T_acc_t1"] for a in ACTIONS}
        if cond == "INTACT"
        else record.get("information", {}).get("future_space_mapping", {})
    )
    rows = []
    for action in ORDERS[record["presentation"]]:
        d = ts[action]["descriptor"]
        rows.append({
            "action": action,
            "future_accessibility_class": d["future_accessibility_class"],
            "identity_turnover_class": d["identity_turnover_class"],
            "persistence_class": d["persistence_class"],
            "reconfiguration_class": d["reconfiguration_class"],
            "future_accessibility": mapping[action],
        })
    return rows

def validate(fixture):
    failures = []
    if fixture.get("instance_count") != EXPECTED_COUNT:
        failures.append("instance_count")
    if len(fixture.get("instances", [])) != EXPECTED_COUNT:
        failures.append("instances_length")
    if canonical_hash(fixture) != EXPECTED_FIXTURE_SHA256:
        failures.append("canonical_body_hash")

    for r in fixture.get("instances", []):
        p = r.get("presentation")
        cond = r.get("condition")
        iid = r.get("instance_id")
        if p not in ORDERS:
            failures.append(f"{iid}:presentation")
            continue
        if r.get("state", {}).get("T_acc") != ACTIONS:
            failures.append(f"{iid}:current_T_acc")
        if r.get("available_transformations") != ACTIONS:
            failures.append(f"{iid}:actions")
        if r.get("selected_transformation") is not None:
            failures.append(f"{iid}:selected_nonnull")
        if r.get("S_t1") is not None or r.get("T_acc_t1") is not None:
            failures.append(f"{iid}:future_revealed")

        rep = r.get("presentation_representation", {})
        if cond == "NULL":
            if rep.get("p1_records") != []:
                failures.append(f"{iid}:null_p1_representation")
            if rep.get("p2_records") != []:
                failures.append(f"{iid}:null_p2_representation")
            if rep.get("p2_order") != []:
                failures.append(f"{iid}:null_p2_order")
            if r.get("information", {}).get("future_space_mapping") is not None:
                failures.append(f"{iid}:null_future_signal")
        else:
            key = "p1_records" if p == "P1" else "p2_records"
            if rep.get("p2_order") != ORDERS["P2"]:
                failures.append(f"{iid}:p2_order")
            if rep.get(key) != expected_records(r):
                failures.append(f"{iid}:representation")

            mapping = r.get("information", {}).get("future_space_mapping", {})
            true_mapping = {a: r["transition_spec"][a]["T_acc_t1"] for a in ACTIONS}
            if cond == "INTACT" and mapping != true_mapping:
                failures.append(f"{iid}:intact_mapping")
            elif cond == "SCRAMBLED":
                if set(mapping.keys()) != set(ACTIONS):
                    failures.append(f"{iid}:scrambled_keys")
                if any(mapping[a] == true_mapping[a] for a in ACTIONS):
                    failures.append(f"{iid}:scramble_not_deranged")

    return failures

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("fixture")
    ap.add_argument("output")
    args = ap.parse_args()
    fixture = json.loads(Path(args.fixture).read_text(encoding="utf-8"))
    failures = validate(fixture)
    fixture_hash = canonical_hash(fixture)
    result = {
        "record_type": "TGCV_TI001_V012_V002_EXECUTOR_2_RECONSTRUCTION_RESULT",
        "executor_2_id": "TI001-V012-V002-INDEPENDENT-RECONSTRUCTOR-2-001",
        "fixture_sha256": fixture_hash,
        "expected_fixture_sha256": EXPECTED_FIXTURE_SHA256,
        "instance_count": len(fixture.get("instances", [])),
        "status": "PASS" if not failures else "FAIL",
        "failures": failures,
        "scientific_execution": False
    }
    Path(args.output).write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, sort_keys=True, indent=2))
    return 0 if not failures else 1

if __name__ == "__main__":
    raise SystemExit(main())
