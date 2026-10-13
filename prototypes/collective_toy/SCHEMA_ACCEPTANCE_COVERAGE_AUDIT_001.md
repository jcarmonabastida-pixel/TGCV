# Collective Toy Schema Acceptance Coverage Audit 001

**Status:** engineering test inventory; not exhaustive schema proof or scientific validation.  
**Historical baseline:** `4ec30575586706c7ba4b65542a9ff8b4ca2513ac` (pre-inventory snapshot).  
**Current traceability supplement:** `SCHEMA_RESIDUAL_PREDICATE_MATRIX_001.md`, added on the PR #52 development branch at commit `289597bc216e228923d935f8bc210ac5d43bc808`.  
**Purpose:** map demonstrated contract coverage to existing tests so future additions target evidenced gaps rather than duplicate tests.

## Provenance and current-head caution

The original inventory below records evidence for its historical baseline only. Do not attribute its listed workflow runs to later commits. The residual predicate matrix is the newer review aid and deliberately uses `COVERED`, `INDIRECT`, and `NOT_ASSESSED` statuses. Its `INDIRECT` rows require source-level confirmation; they do not imply a confirmed missing test.

At commit `289597bc216e228923d935f8bc210ac5d43bc808`, the workflow lookup reported:
- Engine unit suite and clean-source replay: completed / success.
- Governance consistency: completed / success.
- Browser/Python concordance and clean-source replay: in progress at the time of lookup.

Therefore CI for that commit was **not yet fully verified** at the time this note was updated. Recheck the exact commit's runs before recording an all-green result.

## Historical evidence (baseline only)

At historical baseline `4ec30575586706c7ba4b65542a9ff8b4ca2513ac`, all three GitHub Actions checks passed:
- Engine unit suite and clean-source replay: run 38269494203.
- Browser/Python concordance and clean-source replay: run 38269494168.
- Governance consistency: run 38269494153.

These runs are historical evidence for that baseline only, not for the current PR head or the later residual matrix.

## Python unit coverage identified in the historical inventory

| Contract area | Representative tests |
|---|---|
| Required fields, types, unknown fields, IDs and numeric bounds | `test_schema_type_and_required_field_validation_matrix`, `test_schema_rejects_boolean_and_negative_exploration_bounds`, `test_schema_rejects_unknown_nested_fields` |
| Canonical JSON domain and deterministic package hashes | `test_canonical_json_rejects_unsafe_and_non_finite_numbers`, `test_canonical_json_rejects_unpaired_surrogates_and_non_json_values`, `test_export_package_hashes_verify_and_export_replays_independently` |
| Exact and over-limit resource bounds | `test_schema_resource_limits_accept_exact_upper_bounds`, `test_schema_resource_limits_reject_values_above_upper_bounds` |
| Minimal valid graph and zero-depth semantics | `test_schema_accepts_minimum_valid_graph_and_zero_depth`, `test_zero_depth_with_enabled_outgoing_transition_is_explicitly_truncated` |
| Relation-guarded semantics and invalid relation references | `test_relation_guarded_profile_blocks_transition_when_prerequisite_disabled`, `test_relation_guarded_profile_applies_multiple_guards_deterministically`, `test_relation_guarded_profile_rejects_unknown_relation_references`, `test_relation_guarded_profile_rejects_unknown_relation_types`, `test_relation_guarded_profile_rejects_duplicate_relation_ids` |
| Determinism, intervention composition and scenario isolation | `test_transition_declaration_order_does_not_change_semantics`, `test_relation_declaration_order_does_not_change_semantics`, `test_scenario_declaration_order_does_not_couple_scenarios`, `test_combined_disabling_interventions_are_monotone` |
| Profile 1 metadata remains inert | `test_relations_are_inert_metadata_in_profile_one`, `test_relation_metadata_does_not_change_hashes_or_execution_in_profile_one` |

## Browser/Python cross-runtime coverage identified in the historical inventory

`prototypes/collective_toy/web/cross_runtime_test.cjs` includes valid reference/generated fixtures and an invalid-input matrix. The inventory identified:
- Valid minimum single-state graph, cycles, unreachable states, terminal initial state, trajectory caps, multiple interventions, and relation-guarded models.
- Relation and scenario ordering/permutation invariance, guard locality, conjunction, monotonicity, cyclic guards, and non-recursive evaluation.
- Invalid top-level/nested fields, missing and empty identifiers, unknown references/types, duplicate identifiers, wrong container types, boolean/fractional/unsafe numeric inputs, non-finite/unpaired Unicode metadata, and resource-limit violations.
- Browser/Python result concordance and clean-source archive replay.

## Known limitations / next audit targets

1. This is a test inventory, not a formal proof that every schema branch is covered.
2. Existing cases may overlap; no unique case count or percentage is claimed.
3. Cross-runtime agreement alone does not prove both implementations match an independent formal specification.
4. Use `SCHEMA_RESIDUAL_PREDICATE_MATRIX_001.md` for the current predicate-family review. Verify `INDIRECT` entries against the exact Python tests and explicit expected outcomes; do not add tests solely to increase volume.
5. No engine behavior, frozen fixture, baseline hash, scientific claim, or authorization state is changed by this inventory.

## Governance boundary

This audit supports engineering traceability only. It does not establish TGCV causality, value construction, empirical validity, or general scientific validation. The mathematical/functional contract remains a draft, PR #52 remains in draft, and promotion requires explicit governance review. Scientific execution remains unauthorized.
