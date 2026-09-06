"""DR-021 — R* conformance audit for EXT-1.1 Rust.

Synthetic, dataset-independent gate. This audit checks the normative R*
implementation against the frozen operational contract before any large-scale
Rust accessibility reconstruction is attempted.
"""
from __future__ import annotations

import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
if str(HERE) not in sys.path:
    sys.path.insert(0, str(HERE))

from rstar_v02 import requirement_kind, satisfies, resolve_edge  # noqa: E402


def check(name, condition):
    print(f"{name}: {'PASS' if condition else 'FAIL'}")
    return condition


def main():
    print("TGCV EXT-1.1 — DR-021 R* conformance audit v0.1")
    results = []

    results.append(check("P1_exact_grammar", requirement_kind("=1.2.3") == "EXACT"))
    results.append(check("P2_caret_grammar", requirement_kind("^1.2") == "CARET"))
    results.append(check("P3_bare_stable_caret_grammar", requirement_kind("1.2.3") == "CARET"))
    results.append(check("P4_unsupported_wildcard", requirement_kind("1.*") == "UNSUPPORTED"))
    results.append(check("P5_unsupported_tilde", requirement_kind("~1.2") == "UNSUPPORTED"))
    results.append(check("P6_unsupported_compound", requirement_kind(">=1.2,<2.0") == "UNSUPPORTED"))

    versions = [
        (10, "1.1.0", "2022-01-01T00:00:00"),
        (11, "1.2.0", "2022-02-01T00:00:00"),
        (12, "1.3.0", "2022-04-01T00:00:00"),
        (13, "2.0.0", "2022-05-01T00:00:00"),
    ]
    results.append(check("P7_temporal_cutoff", [x[0] for x in __import__('rstar_v02').eligible_versions(versions, "2022-03-01T00:00:00", "^1.0")[0]] == [10, 11]))
    results.append(check("P8_max_selection", resolve_edge(1, "origin", "2022-03-01T00:00:00", 9, "target", "^1.0", versions)["selected_version"] == "1.2.0"))
    results.append(check("P9_exact_selection", resolve_edge(1, "origin", "2022-03-01T00:00:00", 9, "target", "=1.1.0", versions)["selected_version"] == "1.1.0"))
    results.append(check("P10_unsupported_fails_closed", resolve_edge(1, "origin", "2022-03-01T00:00:00", 9, "target", "1.*", versions)["exclusion_reason"] == "UNSUPPORTED"))
    # The cutoff is 2022-03-01, so 1.3.0 and 2.0.0 are future. The
    # greatest eligible ^1.0 target is therefore 1.2.0, not 1.1.0.
    selected = resolve_edge(1, "origin", "2022-03-01T00:00:00", 9, "target", "^1.0", versions)["selected_version"]
    results.append(check("P11_no_future_target", selected == "1.2.0" and selected not in {"1.3.0", "2.0.0"}))

    shuffled = list(reversed(versions))
    a = resolve_edge(1, "origin", "2022-03-01T00:00:00", 9, "target", "^1.0", versions)
    b = resolve_edge(1, "origin", "2022-03-01T00:00:00", 9, "target", "^1.0", shuffled)
    results.append(check("P12_row_order_invariant", a == b))
    results.append(check("P13_duplicate_version_id_fails_closed", _duplicate_id_fails_closed()))
    results.append(check("P14_empty_candidate_distinct", resolve_edge(1, "origin", "2022-03-01T00:00:00", 9, "target", "=9.9.9", versions)["exclusion_reason"] == "NO_ELIGIBLE_CANDIDATE"))

    print(f"DR021_CONFORMANCE_PASS: {all(results)}")
    return 0 if all(results) else 1


def _duplicate_id_fails_closed():
    try:
        resolve_edge(
            1,
            "origin",
            "2022-03-01T00:00:00",
            9,
            "target",
            "^1.0",
            [(10, "1.1.0", "2022-01-01T00:00:00"), (10, "1.2.0", "2022-02-01T00:00:00")],
        )
    except ValueError as exc:
        return str(exc).startswith("DUPLICATE_VERSION_ID:")
    return False


if __name__ == "__main__":
    raise SystemExit(main())
