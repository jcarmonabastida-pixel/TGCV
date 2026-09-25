#!/usr/bin/env python3
"""TI-001 V006 independent Executor-2 reconstruction.

Independent reconstruction of the frozen V005 scientific fixture structure.
This file performs no provider/API calls and no scientific execution.
"""

import hashlib
import json
import sys

FIXTURE_GIT_BLOB_SHA = "edd83fd2df3d39aad8911087569c19614c2264b7"
FIXTURE_CANONICAL_SHA256 = "bc7e0e69cb56337145593e67fb55c1a1b5042db661520498a2c86b346eef76e5"
FIXTURE_ID = "TI001-v005-candidate-001"
PAIR_COUNT = 32
CONDITIONS = ("control", "treatment", "null")
ACTIONS = ("a", "b", "c")
ESTIMAND = "matched_condition_difference_in_transformation_selection"


def canonical_sha256(obj):
    raw = json.dumps(obj, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode("utf-8")
    return hashlib.sha256(raw).hexdigest()


def build_fixture():
    instances = []
    for i in range(1, PAIR_COUNT + 1):
        pair_id = f"TI001-{i:03d}"
        common = {
            "pair_id": pair_id,
            "state": "S0",
            "t_acc": list(ACTIONS),
            "actions": list(ACTIONS),
            "task_id": "TI001-TASK-001",
            "decision_timing": "before_successor_realisation",
        }
        instances.extend([
            {**common, "condition": "control", "future_mapping": None, "future_signal": None},
            {**common, "condition": "treatment", "future_mapping": {
                "a": {"future_accessibility_class": "stable", "identity_turnover_class": "none",
                      "persistence_class": "persistent", "reconfiguration_class": "static"},
                "b": {"future_accessibility_class": "expanded", "identity_turnover_class": "partial",
                      "persistence_class": "persistent", "reconfiguration_class": "reconfigured"},
                "c": {"future_accessibility_class": "reduced", "identity_turnover_class": "full",
                      "persistence_class": "nonpersistent", "reconfiguration_class": "reconfigured"},
            }},
            {**common, "condition": "null", "future_mapping": None, "future_signal": None},
        ])
    return instances


def main():
    instances = build_fixture()
    assert len(instances) == PAIR_COUNT * len(CONDITIONS)
    assert {x["condition"] for x in instances} == set(CONDITIONS)
    result = {
        "record_type": "TGCV_TI001_V006_EXECUTOR_2_RECONSTRUCTION",
        "fixture_id": FIXTURE_ID,
        "fixture_git_blob_sha": FIXTURE_GIT_BLOB_SHA,
        "fixture_canonical_sha256": FIXTURE_CANONICAL_SHA256,
        "pair_count": PAIR_COUNT,
        "condition_count": len(CONDITIONS),
        "decision_count": len(instances),
        "conditions": list(CONDITIONS),
        "action_space": list(ACTIONS),
        "estimand": ESTIMAND,
        "successor_information_consumed": False,
        "scientific_execution": "NOT_PERFORMED",
        "reconstruction_instances": instances,
    }
    if len(sys.argv) == 2:
        with open(sys.argv[1], "w", encoding="utf-8", newline="\n") as handle:
            json.dump(result, handle, indent=2, sort_keys=True, ensure_ascii=False)
            handle.write("\n")
    print(json.dumps({
        "status": "RECONSTRUCTION_COMPLETE",
        "fixture_id": FIXTURE_ID,
        "fixture_git_blob_sha": FIXTURE_GIT_BLOB_SHA,
        "fixture_canonical_sha256": FIXTURE_CANONICAL_SHA256,
        "pair_count": PAIR_COUNT,
        "decision_count": len(instances),
        "estimand": ESTIMAND,
        "scientific_execution": "NOT_PERFORMED",
    }, indent=2, sort_keys=True))
    

if __name__ == "__main__":
    main()
