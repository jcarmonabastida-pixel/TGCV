# Collective Toy — Residual Schema Predicate Matrix 001

**Status:** scoped engineering traceability record; not exhaustive branch coverage or scientific validation.  
**Branch:** `prototype/collective-toy-promotion-clean-001-20261012`  
**Scope:** Python `validate_model` and scenario-level relation evaluation in the Collective Toy MVP.  
**Governance:** contract remains draft; no scientific execution authorization; no promotion authorization.

## Reading the statuses

- **COVERED** — a named existing test is identified as asserting the relevant acceptance/rejection or output.
- **INDIRECT** — the behavior is exercised, but the available inventory does not establish a dedicated independent expected-outcome assertion for every predicate in this row.
- **NOT_ASSESSED** — this review has not verified a specific test-to-predicate mapping. This is not proof that no test exists.

This matrix is deliberately organized by predicate families, not by raw line count. A single test can cover several predicates; no coverage percentage is claimed. Cross-runtime agreement is useful consistency evidence but is not an independent oracle.

## Validator predicates

| Predicate family | Concrete predicate(s) | Existing evidence identified | Status | Residual action |
|---|---|---|---|---|
| Top-level shape | Input is an object; only declared top-level keys are accepted | Schema type/required-field matrix; unknown-field tests | COVERED | No new test unless a specific unasserted predicate is demonstrated |
| Schema version | Exact supported schema version | Schema type/required-field matrix | INDIRECT | Confirm explicit wrong-version assertion in the current test source |
| Model identifier | String and non-blank | Schema type/required-field matrix; empty identifier invalid-input matrix | COVERED | None identified |
| States collection | Non-empty list; each ID is a non-empty string; IDs unique | Schema type/required-field matrix; duplicate identifier matrix | COVERED | None identified |
| Initial state | String referencing a declared state | Required-field and unknown-reference invalid-input matrix | COVERED | None identified |
| Rule profile | Object; no unknown profile keys; exact supported profile/type/version pair | Schema type/required-field matrix and cross-runtime invalid-input matrix | INDIRECT | Confirm separate wrong-type, wrong-version and extra-key assertions against current source |
| Transitions collection and entries | List; each entry is an object with allowed keys; non-empty string ID/source/target; unique transition IDs; source/target declared | Schema type/required-field matrix, unknown references, duplicate IDs and unknown nested fields | COVERED | None identified |
| Relations container | Relations defaults to an empty list; when present, must be a list | Relation-profile tests and invalid-input matrix | INDIRECT | Verify missing, null and wrong-container cases are explicitly distinguished |
| Profile 1 relations | Relation records remain inert descriptive metadata and do not affect execution | `test_relations_are_inert_metadata_in_profile_one`; `test_relation_metadata_does_not_change_hashes_or_execution_in_profile_one`; browser UI contract test | COVERED | None identified |
| Profile 2 relation entries | Object shape and allowed keys; non-empty unique relation ID; supported relation type; required non-empty transition references; both references exist; guarded transition cannot require itself | Named relation tests cover unknown references/types and duplicate IDs; audit also reports invalid-input matrix | INDIRECT | Confirm independent assertions for malformed entry, unknown keys, empty fields and self-guard against current test source |
| Scenarios collection | Non-empty list; each scenario object uses allowed keys; scenario IDs non-empty and unique | Schema type/required-field matrix and cross-runtime invalid-input matrix | COVERED | None identified |
| Disabled transition list | Defaults to empty list; list type; each ID is a non-empty string; every ID exists; no duplicate IDs | Schema type/required-field matrix, unknown references and duplicate identifiers | INDIRECT | Confirm missing-vs-null and duplicate disabled-ID expected error assertions |
| Baseline requirement | A scenario named `baseline` must exist | Baseline comparison tests and schema tests | INDIRECT | Confirm explicit rejection assertion when baseline is absent |
| Exploration object | Object shape and allowed keys | Schema type/required-field and unknown nested field tests | COVERED | None identified |
| Exploration numeric bounds | `max_depth` non-negative integer; booleans rejected; `max_trajectories` positive integer; booleans rejected | `test_schema_rejects_boolean_and_negative_exploration_bounds`; numeric invalid-input matrix | COVERED | None identified |
| Exploration upper limits | Exact accepted bounds and values above caps | `test_schema_resource_limits_accept_exact_upper_bounds`; `test_schema_resource_limits_reject_values_above_upper_bounds` | COVERED | None identified |
| Model resource limits | At most 500 states and 2000 transitions | Resource-limit boundary tests and cross-runtime invalid-input matrix | COVERED | None identified |
| Canonical JSON domain | Reject unsafe/non-finite numbers, unpaired surrogates and non-JSON values | `test_canonical_json_rejects_unsafe_and_non_finite_numbers`; `test_canonical_json_rejects_unpaired_surrogates_and_non_json_values` | COVERED | None identified |

## Scenario evaluation and exported package predicates

| Predicate family | Expected outcome | Existing evidence identified | Status | Residual action |
|---|---|---|---|---|
| Initial enabled transitions | Only declared outgoing transitions surviving scenario/profile filtering are listed | Minimum graph, intervention and relation-profile tests | INDIRECT | Retain hand-computed fixture expectations as the independent oracle |
| Relation guard locality | A guard checks explicit scenario disablement; derived disablements are not recursively re-applied as new explicit inputs | Relation guarded-profile tests and browser UI relation add/remove test | COVERED | None identified |
| Deterministic relation application | Relation declaration order does not change outcomes; relation effects have deterministic ordering | `test_relation_declaration_order_does_not_change_semantics`; multiple-guard deterministic test | COVERED | None identified |
| Scenario isolation | Reordering scenarios does not couple scenario results | `test_scenario_declaration_order_does_not_couple_scenarios` | COVERED | None identified |
| Intervention monotonicity | Combined disablements do not re-enable transitions | `test_combined_disabling_interventions_are_monotone` | COVERED | None identified |
| Reachability and cycles | Reachable states and trajectories follow filtered graph; cycles terminate under explicit bounds | Named graph, cycle, unreachable-state, depth and trajectory-cap tests in the inventory | COVERED | None identified |
| Truncation semantics | Zero depth and output caps expose truncation rather than implying omitted paths do not exist | `test_zero_depth_with_enabled_outgoing_transition_is_explicitly_truncated`; depth/cap audit | COVERED | None identified |
| Baseline comparison | Full scenario result comparison includes intervention metadata | Branch expected-outcome audit and exact baseline assertions | COVERED | None identified |
| Canonical hashes | Input/result/package hashes verify documented canonical representation | `test_export_package_hashes_verify_and_export_replays_independently`; tamper-rejection UI test | COVERED | None identified |
| Independent replay | Known engine/package can replay and compare outputs from the exported input | Python replay test; browser import/export replay test; clean-source CI replays | COVERED | Do not equate replay success with scientific validity |
| Unknown engine version | Package can be inspected but must not be reported as independently replay-verified when replay is unavailable | Browser UI contract test for unknown engine | COVERED | None identified |
| Tampered or malformed package | Reject invalid JSON and stale hashes; fail closed | Browser UI tamper and malformed-package tests | COVERED | None identified |
| Failed current run | Prior successful package must not remain exposed as the current successful result | Browser UI fail-closed test | COVERED | None identified |
| Cross-runtime concordance | Browser and Python outputs agree on shared fixtures and invalid-input matrix | Cross-runtime test and clean-source replay | COVERED | Agreement alone is not an independent formal oracle |

## Residual conclusions

1. The current inventories identify existing tests for the major schema and evaluation families. This pass has **not** established a concrete uncovered runtime outcome that justifies adding a test.
2. Rows marked **INDIRECT** are targeted follow-up checks against the current test source, not confirmed defects. Their presence is not a claim that tests are absent.
3. The schema inventory's stated baseline, `4ec30575586706c7ba4b65542a9ff8b4ca2513ac`, is historical and predates later test additions. Do not present its CI evidence as validation of the current head. Reconcile the inventory's provenance and run links when the final head is known.
4. Before contract freeze, review the INDIRECT rows in source order and upgrade them only when a concrete assertion is located. If a predicate has no dedicated assertion, add a test only where the expected outcome can be hand-calculated independently and is not already covered by a stronger test.
5. This record does not establish exhaustive branch coverage, scientific validity, causality, value construction, or equality between state-local `T_enabled` and system-level `T_acc`.

**Gate:** contract freeze and PR promotion remain blocked pending explicit governance review. Scientific execution remains unauthorized.
