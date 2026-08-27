"""TR-181E R invariant scaffolding.

This file is intentionally a test scaffold, not the confirmatory implementation.
The executable R operationalisation must be supplied only after the schema is frozen.
"""

from copy import deepcopy


def test_same_snapshot_is_deterministic(compute_r, snapshot):
    assert compute_r(snapshot) == compute_r(deepcopy(snapshot))


def test_outcome_cannot_change_r(compute_r, snapshot):
    a = deepcopy(snapshot)
    b = deepcopy(snapshot)
    a["outcome"] = 0
    b["outcome"] = 1
    assert compute_r(a) == compute_r(b)


def test_future_trajectory_cannot_change_r(compute_r, snapshot):
    a = deepcopy(snapshot)
    b = deepcopy(snapshot)
    a["trajectory"] = []
    b["trajectory"] = [{"future": "different"}]
    assert compute_r(a) == compute_r(b)


def test_candidate_order_does_not_change_r(compute_r, snapshot):
    a = deepcopy(snapshot)
    b = deepcopy(snapshot)
    if "candidates" in a:
        b["candidates"] = list(reversed(a["candidates"]))
    assert compute_r(a) == compute_r(b)


def test_invalid_snapshot_fails_closed(compute_r):
    try:
        compute_r({})
    except (ValueError, KeyError, TypeError):
        return
    raise AssertionError("Malformed snapshots must fail closed")


def test_empty_candidate_set_is_deterministic(compute_r, empty_snapshot):
    r1 = compute_r(empty_snapshot)
    r2 = compute_r(deepcopy(empty_snapshot))
    assert r1 == r2


# Additional domain-specific tests must be added when the exact frozen schema exists:
# - resource monotonicity
# - satisfied-precondition monotonicity
# - no B/R feature duplication
# - fixed feature ordering
# - explicit encoding of degenerate cases
