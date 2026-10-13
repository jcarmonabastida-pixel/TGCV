# Collective Toy — Assertion Review 001

**Status:** static assertion review of selected high-risk branches; not runtime CI evidence.
**Reviewed ref:** `prototype/collective-toy-phase-instrumentation-001-20261013`
**Engine blob:** `f7816e325beb580779badfae1e35bcd8235cf5d4`
**Test blob:** `7aaf511fa4e1e44b241b568f2529372b0ce3a1ba`
**Date:** 2026-10-13.

## Scope

Unlike lexical candidate matching in `PREDICATE_TO_TEST_MAPPING_001.md`, this review inspected the actual bodies of selected tests. The classifications below mean that a relevant assertion is visible in source, not that the test was executed in this review. Runtime status must come from CI for this exact head.

## Confirmed direct assertion links

| Engine source line(s) | Predicate / behavior | Test and test source lines | Actual expected outcome | Classification |
|---:|---|---|---|---|
| 101 | Unsupported schema version | `test_schema_type_and_required_field_validation_matrix`, 603–608 and its assertion loop in the remainder of the method | `ModelValidationError` for unsupported schema | DIRECT — rejection asserted; exact error text not pinned in this case |
| 106–113 | States container/uniqueness and initial-state validity | `test_duplicate_state_id_fails`, 815–819; `test_initial_state_must_be_a_string_id_and_malformed_containers_raise_validation_error`, 131 onward | Duplicate state IDs and malformed initial state raise `ModelValidationError` | DIRECT for named failure cases; not every predicate outcome |
| 136–138 | Duplicate transition ID and unknown endpoint | `test_unknown_state_reference_fails`, 139 onward; malformed mutation matrix, 1579–1620 | Unknown state reference raises a specific validation error; malformed transition fields reject | DIRECT for these negative cases |
| 151–169 | Relation object/type/reference/self-guard checks | `test_relation_guard_cannot_reference_itself`, 803 onward; `test_relation_guarded_profile_rejects_unknown_relation_references`, 1535 onward; `test_relation_and_baseline_validation_report_specific_expected_errors`, 1901 onward | Invalid self-reference and missing prerequisite reject; targeted cases pin expected messages/status | DIRECT for selected invalid cases; full predicate matrix still pending |
| 205–212 | Exploration type and resource bounds | `test_schema_resource_limits_accept_exact_upper_bounds`, 1623–1635; `test_schema_resource_limits_reject_values_above_upper_bounds`, 1637–1664; `test_schema_rejects_boolean_and_negative_exploration_bounds`, 1667–1682 | Exact upper limits accepted; 501 states, 2001 transitions, depth 101 and 10001 trajectories rejected; boolean/negative/zero bounds rejected | DIRECT for stated boundaries |
| 223–232 | Relation-guarded profile and prerequisite blocking | `test_relation_guarded_profile_blocks_transition_when_prerequisite_disabled`, 1034 onward; `test_guard_is_inert_when_prerequisite_is_enabled`, 1355 onward; `test_two_relations_guarding_same_transition_form_conjunctive_requirements`, 911 onward | Enabled prerequisite leaves semantics unchanged; disabled prerequisite blocks target; multiple guards act conjunctively | DIRECT for these scenarios, not proof of all graph cases |
| 252–265 | Reachability and depth-boundary/truncation behavior | `test_reachability_invariants_across_deterministic_generated_graphs`, 835–895; `test_cycle_terminates_and_marks_depth_truncation`, 241 onward; `test_terminal_path_at_depth_boundary_is_not_truncated`, 286 onward | Initial state remains reachable; intervention reachability is a subset in generated finite cases; cycle can truncate; terminal path at boundary does not falsely truncate | DIRECT for named finite cases; generated invariants are not exhaustive |
| trajectory cap handling | Exact cap and truncation distinction | `test_exact_trajectory_cap_does_not_mark_complete_enumeration_truncated`, 274 onward | Exactly one terminal trajectory with cap 1; `truncated == False` | DIRECT for exact-cap terminal case; nonterminal cap-hit counterpart must also be confirmed |
| package integrity | Input/result/package tampering | `test_export_package_detects_tampering_of_input_result_and_package`, 389 onward | Altered payload hashes differ from recorded hashes | DIRECT for hash mismatch; this test alone does not prove replay |
| replay assessment | Integrity must not imply replay; self-consistent forged result must fail replay | `test_integrity_only_assessment_does_not_claim_replay`, 480 onward; `test_valid_hashes_do_not_make_divergent_result_replay_verified`, 556 onward; `test_export_package_hashes_verify_and_export_replays_independently`, 580 onward | Integrity-only returns `replay_verified: False`; forged result with recomputed hashes fails independent replay; honest export matches fresh run | DIRECT for those outcomes |

## Gaps to resolve before declaring the audit closed

1. **Positive counterparts:** the current review is weighted toward failure branches. For every validator predicate, explicitly link the accepted valid input or explain why a positive counterpart is not meaningful.
2. **Missing baseline:** inspect the `"baseline" not in scenario_ids` branch at engine line 197 and link a test that pins the expected error; a similarly named test is not enough.
3. **Resource guard separation:** engine line 210 checks graph size while line 212 checks exploration bounds. Keep each predicate tied to its own boundary test; do not collapse them into a single “limits covered” row.
4. **Trajectory cap nonterminal exit:** confirm a test where another path is available when the cap is reached, so the expected `truncated` outcome is independently pinned.
5. **Canonicalization details:** validate canonical JSON numeric, Unicode and unsafe-number predicates against exact expected canonical bytes/hash, not only acceptance/rejection.
6. **Exception contract:** review all remaining branches for raw `TypeError`/`KeyError` leakage versus the promised `ModelValidationError` contract.
7. **Cross-runtime:** Python/JavaScript fixture agreement remains evidence for the fixtures exercised, not all-input equivalence.

## Disposition

This is a useful partial closure of the earlier lexical map: the listed rows have been linked to inspected test bodies and visible assertions. The audit is **not closed**. No engine or test code was modified, no test was run by this static review, and no claim is made that current-head CI is green. The next minimal step is to inspect the remaining validator branches, particularly baseline presence and canonical JSON, then run the relevant test workflow on the exact branch head. Synthetic-only scope remains; scientific execution and promotion remain unauthorized.
