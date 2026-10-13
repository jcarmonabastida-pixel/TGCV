# Collective Toy — Branch Audit Reconciliation 002

**Status:** engineering audit addendum; contract freeze and promotion remain blocked.
**Date:** 2026-10-13.
**Scope:** reconcile the existing preliminary branch-to-test audit with the exact source blobs currently fetched from the development branch. This is a traceability correction, not a claim of exhaustive branch coverage, MC/DC, proof of correctness, or scientific validation.

## 1. Source identity and discrepancy

Development ref inspected: `prototype/collective-toy-phase-instrumentation-001-20261013`.

Fetched source identities:
- `prototypes/collective_toy/collective_toy_engine_001.py` blob SHA: `f7816e325beb580779badfae1e35bcd8235cf5d4` (463 lines).
- `prototypes/collective_toy/test_collective_toy_engine_001.py` blob SHA: `7aaf511fa4e1e44b241b568f2529372b0ce3a1ba` (2,122 lines; 97 `test_*` methods).
- `prototypes/collective_toy/BRANCH_EXPECTED_OUTCOME_AUDIT_001.md` blob SHA: `6b3543ec6a2ffae70358fba4c92f37e161a094fe` (85 lines).

Audit 001 identifies its audited source snapshot as commit `4dd49328d02dd011233cf0f4bfb8920df6ce89a6`. That identifier is not sufficient by itself to establish that every current source blob above was covered by Audit 001. Audit 002 therefore treats Audit 001 as historical preliminary evidence and uses the explicit blob identities above as the current review target. It does not rewrite the historical audit or infer an unobserved commit SHA.

The clean-promotion PR #52 currently documents a different source point (`955a360983f724011bc4b6286234583d4a184e6b`, 96 test methods in the fetched test file). The development instrumentation branch has one additional test method relative to that snapshot. Do not treat the PR #52 CI pass as validation of this later branch state.

## 2. Current branch families and their test evidence

| Branch family | Existing evidence to inspect | Current assessment |
|---|---|---|
| Canonical JSON and cross-runtime value domain | `test_canonical_json_normalizes_integral_floats_and_codepoint_sorts_unicode_keys`; `test_canonical_json_rejects_non_integer_and_unsafe_numbers`; `test_canonical_json_rejects_unpaired_surrogates`; cross-runtime fixtures | Named positive/negative outcomes exist. Still requires explicit mapping of every predicate and recursive context; not exhaustive. |
| Model/schema fields and unknown keys | `test_schema_type_and_required_field_validation_matrix`; `test_schema_rejects_unknown_nested_fields`; `test_deterministic_malformed_input_mutation_matrix`; `test_nested_object_and_scenario_validation_report_specific_errors` | Broad matrix coverage, but exact predicate-to-case linkage must be completed before claiming full branch coverage. |
| State/transition IDs and endpoint references | `test_duplicate_state_id_fails`; `test_duplicate_transition_id_fails`; `test_unknown_state_reference_fails`; `test_unknown_transition_source_state_fails`; `test_initial_state_must_be_a_string_id_and_malformed_containers_raise_validation_error` | Principal failure modes have named tests; positive boundary outcomes must remain linked to the hand-checkable fixture. |
| Relation profile 1 inert metadata | `test_relations_are_inert_metadata_in_profile_one`; `test_relation_metadata_does_not_change_hashes_or_execution_in_profile_one` | Explicit expected outcome exists: relation metadata must not affect profile-1 execution or hashes. |
| Relation profile 2 guard evaluation | `test_relation_guard_cannot_reference_itself`; `test_relation_guarded_profile_rejects_unknown_relation_references`; `test_relation_guarded_profile_rejects_unknown_relation_types`; `test_relation_guarded_profile_rejects_duplicate_relation_ids`; `test_relation_guarded_profile_blocks_transition_when_prerequisite_disabled`; `test_guard_is_inert_when_prerequisite_is_enabled`; `test_two_relations_guarding_same_transition_form_conjunctive_requirements` | Targeted semantics are tested, including non-recursive scenario-local behavior. These tests do not by themselves freeze the mathematical contract or establish equivalence with system-level TGCV `T_acc`. |
| Reachability and intervention monotonicity | `test_disabling_transitions_cannot_expand_reachability_or_trajectories`; `test_relation_guarded_intervention_preserves_reachability_monotonicity`; `test_adding_guard_cannot_expand_reachability_or_trajectories`; `test_reachability_invariants_across_deterministic_generated_graphs` | Invariants have named tests; generated fixtures are finite and do not constitute proof for all graphs. |
| Trajectory enumeration, cycles, depth/cap truncation | `test_cycle_terminates_and_marks_depth_truncation`; `test_trajectory_limit_is_explicit`; `test_exact_trajectory_cap_does_not_mark_complete_enumeration_truncated`; `test_terminal_path_at_depth_boundary_is_not_truncated`; `test_depth_and_trajectory_caps_interact_without_false_complete_result` | Several critical boundary outcomes are explicit. Keep truncation semantics separate from claims that all trajectories were enumerated. |
| Exported package integrity and replay | `test_export_package_detects_tampering_of_input_result_and_package`; `test_exported_package_rejects_truncated_or_incomplete_documents`; `test_integrity_only_assessment_does_not_claim_replay`; `test_valid_hashes_do_not_make_divergent_result_replay_verified`; `test_export_package_hashes_verify_and_export_replays_independently` | Integrity and replay are distinguished. A hash match alone must not be represented as successful replay. |
| Browser/Python concordance and UI | `web/cross_runtime_test.cjs`, `web/ui_contract_test.cjs`, browser CI | CI is relevant only for the exact tested head. Shared-fixture concordance does not establish all-input equivalence. |

## 3. Audit rules for the next pass

1. Enumerate each executable predicate in the current engine validator, scenario evaluator, traversal, package-integrity assessment, and replay assessment.
2. For every predicate, record: source line/range at the reviewed blob; true/false or exception outcome; named test(s); whether the assertion is a hand-computed oracle, a mutation/rejection check, a cross-runtime comparison, or a generated invariant.
3. Mark each row `DIRECT`, `INDIRECT`, `MISSING`, or `NOT_APPLICABLE`. Do not call a family “covered” when only a neighboring branch is exercised.
4. Prioritize missing independent expected outcomes and malformed-input branches that could escape the documented validation exception contract.
5. Re-run or obtain CI for the exact development head after any test/code change. Historical green runs on PR #52 are not substitutes.
6. Keep the scope synthetic-only. Do not import, inspect, or process Rust/`U_t` data; do not enable scientific execution.
7. Do not alter `main`, merge PR #52, freeze the mathematical contract, or claim TGCV scientific validation as a result of this audit.

## 4. Current disposition

**Reconciliation result:** source drift is explicitly recorded; Audit 001 remains a preliminary historical audit, not a current exhaustive branch map.

**Next technical gate:** produce a predicate-level table from the current engine blob and attach exact test assertions. Only then decide whether a minimal test-only patch is justified. No code optimization or scientific execution is authorized by this audit.

**Interpretation boundary:** passing tests supports engineering conformance for the tested finite synthetic inputs only. It does not establish TGCV causality, value construction, generality, or a canonical mapping from state-local enabled transitions to system-level `T_acc`.
