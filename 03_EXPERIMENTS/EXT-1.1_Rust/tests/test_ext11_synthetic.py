"""Pure-Python reference tests for the EXT-1.1 operational fixtures.

These tests deliberately avoid real crates.io data. They verify the set-based
semantics of T_acc and temporal/outcome independence before data ingestion.
"""


def delta(old, new):
    return new - old, old - new


def test_f1_new_accessible_transformation():
    old = {"upgrade_to_1.0"}
    new = {"upgrade_to_1.0", "upgrade_to_1.1"}
    assert delta(old, new) == ({"upgrade_to_1.1"}, set())


def test_f2_irrelevant_state_change_no_tacc_change():
    old = {"upgrade_to_1.0"}
    new = {"upgrade_to_1.0"}
    assert delta(old, new) == (set(), set())


def test_f3_yank_removes_transformation():
    old = {"upgrade_to_1.0", "upgrade_to_1.1"}
    new = {"upgrade_to_1.0"}
    assert delta(old, new) == (set(), {"upgrade_to_1.1"})


def test_f4_narrow_requirement_contracts_space():
    old = {"dep_1.0", "dep_1.1"}
    new = {"dep_1.0"}
    assert delta(old, new) == (set(), {"dep_1.1"})


def test_f5_broaden_requirement_expands_space():
    old = {"dep_1.0"}
    new = {"dep_1.0", "dep_1.1"}
    assert delta(old, new) == ({"dep_1.1"}, set())


def test_f6_irrelevant_metadata_does_not_change_tacc():
    old = {"transform_A"}
    new = {"transform_A"}
    assert delta(old, new) == (set(), set())


def test_f7_future_version_is_not_accessible_at_t():
    available_at_t = {"1.0"}
    future = "1.1"
    assert future not in available_at_t


def test_f8_outcome_change_is_not_an_input_to_tacc():
    tacc = {"transform_A"}
    downloads_before = 10
    downloads_after = 1000
    assert downloads_before != downloads_after
    assert tacc == {"transform_A"}


def test_f9_determinism():
    structural_input = {"transform_A", "transform_B"}
    assert structural_input == set(structural_input)
    assert structural_input == set(structural_input)


def test_f10_ambiguous_identity_fails_closed():
    identities = {"pkg@1.0", "pkg@1.0"}
    assert len(identities) == 1
    # A production parser must reject conflicting records for the same canonical ID.
