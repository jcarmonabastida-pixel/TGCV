"""Self-contained sanity checks for the reconstructed TR-181E R engine.

Deterministic software checks only. Synthetic snapshots are used; no sealed
EMP-1.1 data are touched.
"""
from copy import deepcopy
from r_engine import compute_r

CANDIDATES = [
    {"id": "a", "type": "ACTIVATE", "target": "c1",
     "pre": [{"kind": "component_exists", "value": "c1"}]},
    {"id": "b", "type": "COMPOSE", "target": ["c1", "c2"],
     "pre": [{"kind": "component_pair", "value": ["c1", "c2"]}]},
    {"id": "c", "type": "ACQUIRE", "target": "c3",
     "pre": [{"kind": "resource_min", "name": "r1", "value": 5}]},
]

BASE = {
    "components": ["c1", "c2"],
    "resources": {"r1": 5},
    "objective": "o1",
    "outcome": 0,
    "trajectory": [{"step": 1}],
}


def test_determinism():
    assert compute_r(BASE, CANDIDATES) == compute_r(deepcopy(BASE), CANDIDATES)


def test_outcome_and_trajectory_invariance():
    a = deepcopy(BASE); b = deepcopy(BASE)
    a["outcome"] = 0; a["trajectory"] = []
    b["outcome"] = 999; b["trajectory"] = [{"step": 999, "future": "different"}]
    assert compute_r(a, CANDIDATES) == compute_r(b, CANDIDATES)


def test_candidate_order_invariance():
    assert compute_r(BASE, CANDIDATES) == compute_r(BASE, list(reversed(CANDIDATES)))


def test_missing_resource_blocks_candidate():
    a = compute_r(BASE, CANDIDATES)
    altered = deepcopy(BASE); altered["resources"]["r1"] = 0
    b = compute_r(altered, CANDIDATES)
    assert a["total_accessible"] == b["total_accessible"] + 1


def test_invalid_snapshot_fails_closed():
    try:
        compute_r({}, CANDIDATES)
    except ValueError:
        return
    raise AssertionError("Malformed snapshot must fail closed")


if __name__ == "__main__":
    tests = [test_determinism, test_outcome_and_trajectory_invariance,
             test_candidate_order_invariance, test_missing_resource_blocks_candidate,
             test_invalid_snapshot_fails_closed]
    for test in tests:
        test()
    print(f"PASS: {len(tests)} deterministic R-engine sanity checks")
