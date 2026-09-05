from src.rstar_v02 import requirement_kind, satisfies, resolve_edge


def test_exact_and_caret():
    assert requirement_kind("=3.5.0") == "EXACT"
    assert requirement_kind("^1.0") == "CARET"
    assert satisfies("3.5.0", "=3.5.0")
    assert not satisfies("3.5.1", "=3.5.0")
    assert satisfies("1.2.9", "^1.0")
    assert not satisfies("2.0.0", "^1.0")


def test_unsupported_fails_closed():
    assert requirement_kind("~1.0") == "UNSUPPORTED"
    assert requirement_kind(">=1.0") == "UNSUPPORTED"
    assert requirement_kind("^1") == "UNSUPPORTED"
    assert requirement_kind("^1.0.0, <2.0.0") == "UNSUPPORTED"


def test_temporal_cutoff_and_max_selection():
    result = resolve_edge(
        4, "solana-tokens@1.10.38", "2022-08-27 01:03:20.654886",
        17, "serde", "^1.0",
        [
            (1, "1.0.144", "2022-08-21 03:25:01.347811"),
            (2, "1.0.145", "2022-08-28 03:25:01.347811"),
            (3, "1.0.100", "2022-08-01 03:25:01.347811"),
        ],
    )
    assert result["candidate_count"] == 2
    assert result["selected_version"] == "1.0.144"
    assert result["selected_created_at"] <= result["origin_created_at"]


def test_empty_vs_unsupported():
    empty = resolve_edge(1, "a@1.0.0", "2022-01-01", 2, "b", "=9.9.9", [])
    unsupported = resolve_edge(1, "a@1.0.0", "2022-01-01", 2, "b", "~1.0", [])
    assert empty["exclusion_reason"] == "NO_ELIGIBLE_CANDIDATE"
    assert unsupported["exclusion_reason"] == "UNSUPPORTED"


def test_row_order_independence():
    rows = [
        (1, "1.0.1", "2022-01-01"),
        (2, "1.0.3", "2022-01-03"),
        (3, "1.0.2", "2022-01-02"),
    ]
    a = resolve_edge(9, "a@1.0.0", "2022-01-04", 8, "b", "^1.0", rows)
    b = resolve_edge(9, "a@1.0.0", "2022-01-04", 8, "b", "^1.0", list(reversed(rows)))
    assert a == b


def test_duplicate_version_id_fails_closed():
    rows = [(1, "1.0.1", "2022-01-01"), (1, "1.0.2", "2022-01-02")]
    try:
        resolve_edge(9, "a@1.0.0", "2022-01-04", 8, "b", "^1.0", rows)
    except ValueError as exc:
        assert str(exc).startswith("DUPLICATE_VERSION_ID:")
    else:
        raise AssertionError("duplicate version IDs must fail closed")
