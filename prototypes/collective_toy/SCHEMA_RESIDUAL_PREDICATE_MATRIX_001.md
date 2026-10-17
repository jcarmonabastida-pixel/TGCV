# Collective Toy — Residual Schema Predicate Matrix 001

**Status:** scoped engineering traceability record; not exhaustive branch coverage or scientific validation.  
**Source branch:** `prototype/collective-toy-promotion-clean-001-20261012`  
**Review basis:** current PR #52 Python test file and engine patch inspected during this pass; schema audit provenance was updated at commit `b56cb21c0073dafa80465d2be7246ac528474466`.  
**Governance:** contract remains draft; no scientific execution authorization; no promotion authorization.

## Reading the statuses

- **COVERED** — a named existing test asserts acceptance/rejection or the expected output for the predicate family.
- **INDIRECT** — exercised by broader tests, but a dedicated independent assertion for every predicate is not established in this review.
- **NOT_ASSESSED** — no source-level test mapping verified in this pass; this is not proof that no test exists.

This is a targeted predicate-family inventory, not exhaustive branch coverage. No coverage percentage is claimed. Cross-runtime agreement is consistency evidence, not an independent oracle.

## Validator predicates

| Predicate family | Concrete predicate(s) | Existing test evidence verified in source | Status | Residual action |
|---|---|---|---|---|
| Top-level shape | Input object; unknown top-level keys rejected | `test_top_level_model_and_required_string_fields_reject_wrong_types`; broad schema matrix | COVERED | None identified |
| Schema version | Only `collective-toy-input-001` accepted | Browser H1 grouped adversary `input-schema-version-unknown-string` explicitly rejects `collective-toy-input-999`; broad schema matrix also exercises invalid schema inputs | COVERED | None for unsupported string version; other H1 field/type coverage remains partial |
| Model identifier | Non-empty string | `test_top_level_model_and_required_string_fields_reject_wrong_types`; broad schema matrix | COVERED | None identified |
| States collection | Non-empty list; non-empty string IDs; uniqueness | `test_schema_container_branches_report_specific_expected_errors`; `test_schema_rejects_empty_states_and_scenarios`; `test_state_ids_must_be_strings`; schema matrix | COVERED | None identified |
| Initial state | String referring to declared state | `test_initial_state_must_be_a_string_id_and_malformed_containers_raise_validation_error`; `test_unknown_initial_state_string_fails` | COVERED | None identified |
| Rule profile | Object, no unknown keys, supported type/version pair | `test_schema_type_and_required_field_validation_matrix` rejects unknown type, unsupported version for `relation_guarded_graph`, and unsupported version for `finite_deterministic_graph`; container and unknown-key tests cover shape | COVERED | CI must verify the two newly added unsupported-version cases |
| Transition entries | List; object entries; allowed keys; non-empty string fields; unique IDs; known source/target | `test_nested_object_and_scenario_validation_report_specific_errors`; `test_duplicate_transition_id_fails`; unknown-state tests; nested-field matrix | COVERED | None identified |
| Relations container | Omitted means empty; present value must be list | `test_optional_relations_and_disabled_transitions_default_empty`; `test_omitted_relations_default_empty_in_relation_guarded_profile`; `test_schema_container_branches_report_specific_expected_errors` | COVERED | None identified |
| Profile 1 relations | Descriptive metadata remains operationally inert | `test_relations_are_inert_metadata_in_profile_one`; `test_relation_metadata_does_not_change_hashes_or_execution_in_profile_one` | COVERED | None identified |
| Profile 2 relation entries | Object; allowed keys; valid unique ID/type; required non-empty refs; known transition refs; no self-guard | `test_nested_object_and_scenario_validation_report_specific_errors`; `test_relation_and_baseline_validation_report_specific_expected_errors`; `test_non_string_nested_relation_and_scenario_identifiers_fail`; duplicate/type/reference tests | COVERED | None identified for listed predicates |
| Scenarios collection | Non-empty list; object entries; allowed keys; non-empty unique string IDs | `test_nested_object_and_scenario_validation_report_specific_errors`; `test_non_string_nested_relation_and_scenario_identifiers_fail`; schema matrix | COVERED | None identified |
| Disabled transition list | Omitted means empty; list required when present; non-empty string IDs, known and unique | `test_optional_relations_and_disabled_transitions_default_empty`; `test_nested_object_and_scenario_validation_report_specific_errors`; `test_schema_rejects_duplicate_disabled_transition_ids`; schema matrix | COVERED | None identified |
| Baseline requirement | Scenario ID `baseline` must exist | `test_relation_and_baseline_validation_report_specific_expected_errors`; `test_schema_rejects_missing_baseline_and_empty_state_ids` | COVERED | None identified |
| Exploration object and keys | Object required; unknown keys rejected | `test_schema_container_branches_report_specific_expected_errors`; `test_schema_rejects_unknown_nested_fields` | COVERED | None identified |
| Exploration numeric bounds | Integer bounds; booleans rejected; non-negative depth; positive trajectory cap | `test_schema_rejects_boolean_and_negative_exploration_bounds`; schema matrix | COVERED | None identified |
| Exploration upper limits | Exact maximums accepted and above-limit values rejected | `test_schema_resource_limits_accept_exact_upper_bounds`; `test_schema_resource_limits_reject_values_above_upper_bounds` | COVERED | None identified |
| Model resource limits | At most 500 states and 2000 transitions | Exact-boundary and above-boundary tests | COVERED | None identified |
| Canonical JSON domain | Reject unsafe/non-finite numbers, unpaired surrogates and non-JSON values | `test_canonical_json_rejects_unsafe_and_non_finite_numbers`; `test_canonical_json_rejects_unpaired_surrogates_and_non_json_values` | COVERED | None identified |

## Scenario evaluation and exported package predicates

| Predicate family | Expected outcome | Existing evidence identified | Status | Residual action |
|---|---|---|---|---|
| Initial enabled transitions | Only transitions available from initial state after explicit and profile-local filtering | Literal diamond fixture; intervention comparison; profile 2 tests | COVERED | No gap demonstrated in reviewed cases; not a universal proof |
| Relation guard locality | Guard tests explicit disablement only; derived effects are not recursively fed back | Relation guarded-profile and multiple-guard deterministic tests | COVERED | None identified |
| Deterministic relation application | Declaration order does not alter semantics; effects ordered deterministically | `test_relation_declaration_order_does_not_change_semantics`; multiple-guard test | COVERED | None identified |
| Scenario isolation | Scenario declaration order does not couple results | `test_scenario_declaration_order_does_not_couple_scenarios` | COVERED | None identified |
| Intervention monotonicity | Additional disabling cannot enable transitions or expand paths | `test_combined_disabling_interventions_are_monotone`; unreachable-transition intervention test | COVERED | None identified |
| Reachability and cycles | Reachability follows filtered graph; bounded walks terminate under depth/cap limits | Diamond, cycle, unreachable-state, depth and trajectory-cap tests | COVERED | None identified |
| Truncation semantics | Bounds distinguish complete terminal paths from omitted continuations | Zero-depth, terminal-boundary, exact-cap and combined-cap tests | COVERED | None identified |
| Baseline comparison | Deltas include intervention metadata and exact path changes; truncation propagates from either side | Exact baseline comparison test and both truncation propagation tests | COVERED | None identified |
| Canonical hashes | Input/result/package hashes match canonical representation | Canonical JSON tests and export package hash/replay tests | COVERED | None identified |
| Independent replay | Known engine recomputes output; package integrity is not conflated with replay | Current baseline package fixture; independent replay tests | COVERED | Do not equate replay success with scientific validity |
| Unknown engine version | Intact known-format package can be inspected without claiming replay verification | Package lifecycle/unknown-engine tests in Python and browser | COVERED | None identified |
| Tampered or malformed package | Invalid JSON and hash mismatch rejected; fail closed | Export package tamper tests and browser tests | COVERED | None identified |
| Failed current run | Prior successful package not misrepresented as current success | Browser fail-closed test | COVERED | None identified |
| Cross-runtime concordance | Shared fixtures and invalid inputs agree between Python and browser | Cross-runtime suite and clean-source replay | COVERED | Agreement alone is not an independent formal oracle |

## Residual conclusions

1. Source review upgrades several earlier `INDIRECT` rows to `COVERED`: omitted-vs-invalid relations, disabled-transition defaults and rejection, self-guard, non-string relation/scenario IDs, and missing baseline all have named Python assertions.
2. Schema version and rule-profile version combinations are now mapped to explicit rejection cases. The Python invalid-input matrix includes unsupported string versions for both `relation_guarded_graph` and `finite_deterministic_graph`; CI is required to verify the newly added cases before treating this evidence as validated.
3. No concrete uncovered runtime outcome was demonstrated in this pass. No engine behavior, fixture, or test was changed.
4. Historical CI runs in `SCHEMA_ACCEPTANCE_COVERAGE_AUDIT_001.md` apply only to their historical commit. Recheck exact-head CI before claiming current all-green status.
5. This record does not establish exhaustive branch coverage, scientific validity, causality, value construction, or equivalence between state-local `T_enabled` and system-level `T_acc`.

**Gate:** contract freeze and PR promotion remain blocked pending explicit governance review. Scientific execution remains unauthorized.
