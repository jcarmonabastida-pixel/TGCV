# Collective Toy — Assertion Review Follow-up 001

**Status:** static source review; no runtime result claimed.
**Reviewed ref:** `prototype/collective-toy-phase-instrumentation-001-20261013`
**Engine blob:** `f7816e325beb580779badfae1e35bcd8235cf5d4`
**Test blob:** `7aaf511fa4e1e44b241b568f2529372b0ce3a1ba`
**Date:** 2026-10-13.

## 1. Recheck of gaps listed in Assertion Review 001

### Missing baseline — resolved at source level

The earlier review listed the `"baseline" not in scenario_ids` branch (engine line 197) as requiring a test link. The current test blob already contains two relevant cases:

- `test_schema_rejects_missing_baseline_and_empty_state_ids` (test line 1725) rejects a model with only an `other` scenario using `assertRaises(ModelValidationError)`.
- `test_relation_and_baseline_validation_report_specific_expected_errors` (test line 1901) renames the baseline scenario to `reference` and pins the exact message `a scenario with id 'baseline' is required` using `assertRaisesRegex`.

**Disposition:** DIRECT negative assertion exists, including an exact expected message. The first test's generic exception assertion is weaker, but the second pins the specific contract. No new test is justified for this branch at this stage.

### Canonicalization — exact expected output partly confirmed

- `test_canonical_json_normalizes_integral_floats_and_codepoint_sorts_unicode_keys` (line 371) asserts the exact canonical JSON string for integral float normalization, negative zero normalization, and codepoint ordering of U+E000 and U+10000 keys. It also asserts equal hashes for `1.0` and `1`.
- `test_canonical_json_rejects_non_integer_and_unsafe_numbers` (line 379) asserts `ModelValidationError` for a fractional number, NaN and an unsafe integer.
- `test_canonical_json_rejects_unsafe_and_non_finite_numbers` (line 1738) separately checks positive and negative unsafe integers, NaN, positive/negative infinity and a fractional number.
- `test_canonical_json_rejects_unpaired_surrogates_and_non_json_values` (line 1753) rejects an unpaired surrogate, a non-JSON object and a non-string object key.

**Disposition:** DIRECT expected canonical text and negative cases exist for these selected predicates. This is not yet an exhaustive canonicalization audit, nor does it assert a fixed SHA-256 hex digest against an independently calculated known-answer vector.

### Trajectory cap — evidence split by behavior

- `test_trajectory_limit_is_explicit` (line 249) sets `max_trajectories = 1` and asserts that the baseline result is marked `truncated == True`.
- `test_exact_trajectory_cap_does_not_mark_complete_enumeration_truncated` (line 274) asserts that reaching the exact cap on a completed terminal enumeration does not mark it truncated.
- `test_disconnected_component_preserves_truncation_under_trajectory_cap` (line 1300) asserts truncation remains true when disconnected states are added, while reachable states and trajectories remain unchanged.

**Disposition:** direct assertions exist for explicit truncation and exact-cap terminal behavior. The test body for `test_trajectory_limit_is_explicit` does not itself assert the existence of a further unenumerated path, so that specific oracle question remains open. The disconnected-component test is a metamorphic invariant, not a direct count of omitted paths.

## 2. Still open

1. Inspect the actual test fixture and traversal loop to determine whether `test_trajectory_limit_is_explicit` guarantees a nonterminal cap hit with additional work pending; if not, add a minimal test with an independent expected trajectory count and `truncated=True`.
2. Separate graph-size guard coverage (engine line 210) from exploration-bound coverage (line 213), linking each predicate to its own exact boundary test.
3. Continue reviewing remaining validator branches for raw `TypeError`/`KeyError` leakage versus `ModelValidationError`.
4. Confirm current-head CI for the exact branch revision. No CI run is claimed here.

## 3. Disposition

Two previously identified review gaps (baseline and canonical JSON) were already addressed by existing test bodies and are now linked explicitly; no redundant test patch was added. The trajectory cap's nonterminal oracle and exception-contract sweep remain open. No engine code, fixtures, hashes, scientific claims, or authorization flags were changed. Synthetic-only scope, no promotion, and scientific execution disabled remain in force.
