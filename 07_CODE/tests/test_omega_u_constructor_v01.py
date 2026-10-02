from omega_u_constructor_v01 import build_u_t


def selector(source, dependency, eligible_targets):
    # Synthetic deterministic selector: accept every target visible in the
    # frozen primitive window. Real semver semantics remain an explicit,
    # separately frozen resolver concern.
    return eligible_targets


VERSIONS = [
    {"id": 1, "package_id": 10, "version_str": "1.0.0", "created_at": "2022-08-01T00:00:00Z"},
    {"id": 2, "package_id": 20, "version_str": "1.0.0", "created_at": "2022-08-02T00:00:00Z"},
    {"id": 3, "package_id": 20, "version_str": "2.0.0", "created_at": "2022-08-03T00:00:00Z"},
    {"id": 4, "package_id": 30, "version_str": "1.0.0", "created_at": "2022-09-02T00:00:00Z"},
]
DEPS = [
    {"depending_version": 1, "depending_on_package": 20, "semver_str": "^1.0.0"},
    {"depending_version": 1, "depending_on_package": 20, "semver_str": "^1.0.0"},
]


def test_valid_construction_and_duplicate_collapse():
    result = build_u_t(VERSIONS, DEPS, cutoff="2022-09-01T00:00:00Z", target_selector=selector)
    assert result["u_count"] == 2
    assert [r["tau"] for r in result["U_t"]] == [[1, 20, 2], [1, 20, 3]]
    assert all(r["coverage_state"] == "OBSERVED_PRESENT" for r in result["U_t"])


def test_out_of_scope_target_is_not_emitted():
    deps = [{"depending_version": 1, "depending_on_package": 30, "semver_str": "*"}]
    result = build_u_t(VERSIONS, deps, cutoff="2022-09-01T00:00:00Z", target_selector=selector)
    assert result["u_count"] == 0


def test_missing_origin_fails_closed():
    deps = [{"depending_version": 999, "depending_on_package": 20, "semver_str": "*"}]
    result = build_u_t(VERSIONS, deps, cutoff="2022-09-01T00:00:00Z", target_selector=selector)
    assert result["u_count"] == 0
    assert result["skipped_out_of_scope_count"] == 1


def test_unknown_identity_input_fails_closed():
    deps = [{"depending_version": None, "depending_on_package": 20, "semver_str": "*"}]
    result = build_u_t(VERSIONS, deps, cutoff="2022-09-01T00:00:00Z", target_selector=selector)
    assert result["u_count"] == 0
    assert result["unresolved_count"] == 1


def test_future_target_never_enters_u():
    deps = [{"depending_version": 1, "depending_on_package": 30, "semver_str": "*"}]
    result = build_u_t(VERSIONS, deps, cutoff="2022-09-01T00:00:00Z", target_selector=selector)
    assert result["u_count"] == 0


def test_firewall_fields_cannot_affect_u():
    deps1 = [{"depending_version": 1, "depending_on_package": 20, "semver_str": "*",
              "T_acc": 999, "Reach": 999, "outcome": "bad", "value": 999}]
    deps2 = [{"depending_version": 1, "depending_on_package": 20, "semver_str": "*",
              "T_acc": 0, "Reach": 0, "outcome": "good", "value": 0}]
    r1 = build_u_t(VERSIONS, deps1, cutoff="2022-09-01T00:00:00Z", target_selector=selector)
    r2 = build_u_t(VERSIONS, deps2, cutoff="2022-09-01T00:00:00Z", target_selector=selector)
    assert r1["U_t"] == r2["U_t"]
    assert r1["output_sha256"] == r2["output_sha256"]


def test_deterministic_under_dependency_row_permutation():
    a = build_u_t(VERSIONS, DEPS, cutoff="2022-09-01T00:00:00Z", target_selector=selector)
    b = build_u_t(VERSIONS, list(reversed(DEPS)), cutoff="2022-09-01T00:00:00Z", target_selector=selector)
    assert a["U_t"] == b["U_t"]
    assert a["output_sha256"] == b["output_sha256"]


def test_provenance_is_retained():
    result = build_u_t(VERSIONS, DEPS, cutoff="2022-09-01T00:00:00Z", target_selector=selector)
    assert result["U_t"][0]["provenance"][0].startswith("package_dependencies.csv:row:")


def test_schema_error_is_explicit():
    bad_versions = [{"id": 1, "package_id": 10, "created_at": "2022-08-01T00:00:00Z"}]
    try:
        build_u_t(bad_versions, DEPS, cutoff="2022-09-01T00:00:00Z", target_selector=selector)
    except ValueError:
        return
    raise AssertionError("schema error was not rejected")


def test_constructor_version_and_rule_are_emitted():
    result = build_u_t(VERSIONS, DEPS, cutoff="2022-09-01T00:00:00Z", target_selector=selector)
    assert result["construction_version"] == "RUST_OMEGA_U_CONSTRUCTOR_v0.1"
    assert result["temporal_rule"] == "DR-035-v0.1-ADJACENT-CREATED-AT"
