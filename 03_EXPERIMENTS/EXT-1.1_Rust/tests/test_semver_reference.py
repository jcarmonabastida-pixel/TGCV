from src.semver_reference import accessible_versions, satisfies


def test_exact_requirement():
    assert satisfies("1.2.3", "1.2.3")
    assert not satisfies("1.2.4", "1.2.3")


def test_caret_major():
    assert accessible_versions(["1.0.0", "1.2.0", "2.0.0"], "^1.0.0") == {"1.0.0", "1.2.0"}


def test_caret_zero_minor():
    assert accessible_versions(["0.2.0", "0.2.5", "0.3.0"], "^0.2.0") == {"0.2.0", "0.2.5"}


def test_lower_and_upper_bounds():
    assert accessible_versions(["1.0.0", "1.1.0", "1.2.0"], ">=1.1.0") == {"1.1.0", "1.2.0"}
    assert accessible_versions(["1.0.0", "1.1.0", "1.2.0"], "<1.2.0") == {"1.0.0", "1.1.0"}


def test_empty_candidate_set():
    assert accessible_versions(["1.0.0"], ">=2.0.0") == set()


def test_unsupported_requirement_fails_closed():
    try:
        satisfies("1.0.0", "~1.0")
    except ValueError:
        pass
    else:
        raise AssertionError("unsupported requirement must fail closed")
