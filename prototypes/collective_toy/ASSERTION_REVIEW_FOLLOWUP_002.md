# Collective Toy — Assertion Review Follow-up 002

**Status:** source review updated after a minimal test-only patch; CI is not yet confirmed.
**Engine path/blob:** `prototypes/collective_toy/collective_toy_engine_001.py` / `f7816e325beb580779badfae1e35bcd8235cf5d4`.
**Test path/blob:** `prototypes/collective_toy/test_collective_toy_engine_001.py` / `b62d9a05f8116d3c2da75d2bc39919af7680705f`.
**Commit:** `692570d6174282ac3fbafe9f026edc36f6a997c9`.
**Date:** 2026-10-13.

## 1. Minimal test added

Added `test_nonterminal_trajectory_cap_marks_omitted_terminal_path_truncated`.

The test builds a hand-checkable graph with two terminal paths from initial state A: A→B via `t_ab` and A→C via `t_ac`. With `max_trajectories = 1`, it asserts the exact emitted trajectory is A→B and asserts `truncated is True`, because the second terminal path remains pending when the output cap is reached.

This supplies the missing independent expected outcome identified in Follow-up 001. It changes no engine code, fixture baseline, hash algorithm, UI, or scientific authorization. Test count in the fetched source is now 98 named `test_*` methods.

## 2. Limit-guard traceability

The reviewed engine has separate predicates:
- Engine line 210: reject more than 500 states or more than 2000 transitions.
- Engine line 212: reject `max_depth > 100` or `max_trajectories > 10000`.

Existing tests provide:
- `test_schema_resource_limits_accept_exact_upper_bounds`: validates 500 states, 2000 transitions, depth 100 and trajectory cap 10000 together.
- `test_schema_resource_limits_reject_values_above_upper_bounds`: independent subcases for 501 states, 2001 transitions, depth 101 and trajectory cap 10001; each expects `ModelValidationError`.
- `test_schema_rejects_boolean_and_negative_exploration_bounds`: rejects Boolean/negative/zero exploration values.

These are direct boundary assertions. The upper-bound acceptance fixture checks all four limits together rather than isolating each accepted boundary in a separate test; that is acceptable for current contract evidence but should be considered if future failures make diagnosis ambiguous.

## 3. Verification status

The new test file was fetched back from GitHub and its blob SHA verified. The expected exact trajectory and `truncated=True` assertion are present. The engine blob remains unchanged.

No workflow runs were returned for commit `692570d6174282ac3fbafe9f026edc36f6a997c9`. Therefore this is **source-verified, not runtime-validated**. Do not claim the new test passes until CI executes against this exact head.

## 4. Remaining audit work

1. Run the relevant engine test workflow for this exact commit and inspect its result.
2. Continue the exception-contract sweep for malformed inputs that might leak raw `TypeError`/`KeyError`.
3. If the exact-head run fails, diagnose one cause per iteration; do not alter engine semantics to make a test green without a separate reviewed rationale.

Synthetic-only scope remains. No scientific execution, contract freeze, merge, or promotion is authorized by this commit.
