# Collective Toy — Predicate-to-Test Mapping 001

**Status:** static traceability worklist; not a completed branch-coverage result.
**Reviewed engine blob:** `f7816e325beb580779badfae1e35bcd8235cf5d4` on `prototype/collective-toy-phase-instrumentation-001-20261013`.
**Reviewed test blob:** `7aaf511fa4e1e44b241b568f2529372b0ce3a1ba` on the same ref; `97` named `test_*` methods.
**Generated:** 2026-10-13.

## Method and limits

This worklist enumerates Python control-flow statements in the exact engine blob and gives likely test-name candidates based on lexical overlap. A candidate is **not** proof that the test executes that branch or asserts its outcome. No test bodies were treated as verified by this lexical mapping. The status for all rows is therefore `PENDING_ASSERTION_REVIEW` until a reviewer checks the actual test body, expected value/exception, and the predicate's true/false outcomes.

The enumeration includes loops and `else` blocks as control-flow sites, not only Boolean decisions. It is not a substitute for measured coverage instrumentation, MC/DC, or independent oracle validation.

## Source and test identity

- Engine path: `prototypes/collective_toy/collective_toy_engine_001.py`
- Engine blob: `f7816e325beb580779badfae1e35bcd8235cf5d4`
- Test path: `prototypes/collective_toy/test_collective_toy_engine_001.py`
- Test blob: `7aaf511fa4e1e44b241b568f2529372b0ce3a1ba`
- Engine lines enumerated: 92 control-flow sites across 463 lines.
- Named test methods in test blob: 97.

## Control-flow inventory

| Engine line | Function | Predicate / control flow | Candidate test names (heuristic only) | Status |
|---:|---|---|---|---|
| 27 | `_reject_unknown_keys` | `if unknown:` | `test_unknown_state_reference_fails` (L139); `test_unknown_initial_state_string_fails` (L145); `test_unknown_transition_source_state_fails` (L154) | PENDING_ASSERTION_REVIEW |
| 36 | `_validate_canonical_domain` | `if value is None or isinstance(value, bool):` | `test_schema_rejects_boolean_and_negative_exploration_bounds` (L1667) | PENDING_ASSERTION_REVIEW |
| 38 | `_validate_canonical_domain` | `if isinstance(value, int):` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 39 | `_validate_canonical_domain` | `if abs(value) > MAX_SAFE_JSON_INTEGER:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 42 | `_validate_canonical_domain` | `if isinstance(value, float):` | `test_canonical_json_normalizes_integral_floats_and_codepoint_sorts_unicode_keys` (L371) | PENDING_ASSERTION_REVIEW |
| 43 | `_validate_canonical_domain` | `if not math.isfinite(value) or not value.is_integer() or abs(value) > MAX_SAFE_JSON_INTEGER:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 46 | `_validate_canonical_domain` | `if isinstance(value, str):` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 47 | `_validate_canonical_domain` | `if any(0xD800 <= ord(char) <= 0xDFFF for char in value):` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 50 | `_validate_canonical_domain` | `if isinstance(value, list):` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 51 | `_validate_canonical_domain` | `for index, item in enumerate(value):` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 54 | `_validate_canonical_domain` | `if isinstance(value, dict):` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 55 | `_validate_canonical_domain` | `for key, item in value.items():` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 56 | `_validate_canonical_domain` | `if not isinstance(key, str):` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 65 | `_normalize_integral_floats` | `if isinstance(value, float):` | `test_canonical_json_normalizes_integral_floats_and_codepoint_sorts_unicode_keys` (L371) | PENDING_ASSERTION_REVIEW |
| 67 | `_normalize_integral_floats` | `if isinstance(value, list):` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 69 | `_normalize_integral_floats` | `if isinstance(value, dict):` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 97 | `validate_model` | `if not isinstance(model, dict):` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 101 | `validate_model` | `if model.get("schema_version") != SUPPORTED_SCHEMA:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 103 | `validate_model` | `if not isinstance(model.get("model_id"), str) or not model["model_id"].strip():` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 106 | `validate_model` | `if not isinstance(states, list) or not states:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 108 | `validate_model` | `if any(not isinstance(s, str) or not s for s in states):` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 110 | `validate_model` | `if len(set(states)) != len(states):` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 113 | `validate_model` | `if not isinstance(initial_state, str) or initial_state not in set(states):` | `test_initial_state_must_be_a_string_id_and_malformed_containers_raise_validation_error` (L131); `test_unknown_initial_state_string_fails` (L145) | PENDING_ASSERTION_REVIEW |
| 119 | `validate_model` | `if not isinstance(profile, dict):` | `test_relation_metadata_does_not_change_hashes_or_execution_in_profile_one` (L897); `test_relation_guarded_profile_blocks_transition_when_prerequisite_disabled` (L1034); `test_relation_guarded_profile_applies_multiple_guards_deterministically` (L1064) | PENDING_ASSERTION_REVIEW |
| 122 | `validate_model` | `if profile not in (profile1, profile2):` | `test_relation_metadata_does_not_change_hashes_or_execution_in_profile_one` (L897); `test_relation_guarded_profile_blocks_transition_when_prerequisite_disabled` (L1034); `test_relation_guarded_profile_applies_multiple_guards_deterministically` (L1064) | PENDING_ASSERTION_REVIEW |
| 126 | `validate_model` | `if not isinstance(raw_transitions, list):` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 129 | `validate_model` | `for item in raw_transitions:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 130 | `validate_model` | `if not isinstance(item, dict):` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 134 | `validate_model` | `if any(not isinstance(x, str) or not x for x in (tid, source, target)):` | `test_unknown_transition_source_state_fails` (L154); `test_schema_resource_limits_accept_exact_upper_bounds` (L1623); `test_schema_resource_limits_reject_values_above_upper_bounds` (L1637) | PENDING_ASSERTION_REVIEW |
| 136 | `validate_model` | `if tid in transitions:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 138 | `validate_model` | `if source not in states or target not in states:` | `test_unknown_transition_source_state_fails` (L154); `test_schema_resource_limits_accept_exact_upper_bounds` (L1623); `test_schema_resource_limits_reject_values_above_upper_bounds` (L1637) | PENDING_ASSERTION_REVIEW |
| 143 | `validate_model` | `if not isinstance(relations, list):` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 145 | `validate_model` | `if profile == profile1:` | `test_relation_metadata_does_not_change_hashes_or_execution_in_profile_one` (L897); `test_relation_guarded_profile_blocks_transition_when_prerequisite_disabled` (L1034); `test_relation_guarded_profile_applies_multiple_guards_deterministically` (L1064) | PENDING_ASSERTION_REVIEW |
| 148 | `validate_model` | `else:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 150 | `validate_model` | `for relation in relations:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 151 | `validate_model` | `if not isinstance(relation, dict):` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 156 | `validate_model` | `if not isinstance(rid, str) or not rid:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 158 | `validate_model` | `if rid in relation_ids:` | `test_relation_guarded_profile_rejects_duplicate_relation_ids` (L1559) | PENDING_ASSERTION_REVIEW |
| 161 | `validate_model` | `if rtype != "requires_transition_enabled":` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 163 | `validate_model` | `if not isinstance(guarded, str) or not guarded or not isinstance(prerequisite, str) or not prerequisite:` | `test_relation_guarded_profile_blocks_transition_when_prerequisite_disabled` (L1034); `test_relation_guarded_intervention_preserves_reachability_monotonicity` (L960); `test_relation_guarded_profile_applies_multiple_guards_deterministically` (L1064) | PENDING_ASSERTION_REVIEW |
| 165 | `validate_model` | `if guarded not in transitions:` | `test_relation_guarded_intervention_preserves_reachability_monotonicity` (L960); `test_relation_guarded_profile_blocks_transition_when_prerequisite_disabled` (L1034); `test_relation_guarded_profile_applies_multiple_guards_deterministically` (L1064) | PENDING_ASSERTION_REVIEW |
| 167 | `validate_model` | `if prerequisite not in transitions:` | `test_relation_guarded_profile_blocks_transition_when_prerequisite_disabled` (L1034); `test_guard_is_inert_when_prerequisite_is_enabled` (L1355) | PENDING_ASSERTION_REVIEW |
| 169 | `validate_model` | `if guarded == prerequisite:` | `test_relation_guarded_profile_blocks_transition_when_prerequisite_disabled` (L1034); `test_relation_guarded_intervention_preserves_reachability_monotonicity` (L960); `test_relation_guarded_profile_applies_multiple_guards_deterministically` (L1064) | PENDING_ASSERTION_REVIEW |
| 172 | `validate_model` | `if not isinstance(scenarios, list) or not scenarios:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 175 | `validate_model` | `for scenario in scenarios:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 176 | `validate_model` | `if not isinstance(scenario, dict):` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 180 | `validate_model` | `if not isinstance(sid, str) or not sid:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 182 | `validate_model` | `if sid in scenario_ids:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 186 | `validate_model` | `if not isinstance(disabled, list):` | `test_unknown_disabled_transition_fails` (L821); `test_disabled_transition_ids_must_be_strings` (L827); `test_relation_guarded_profile_blocks_transition_when_prerequisite_disabled` (L1034) | PENDING_ASSERTION_REVIEW |
| 188 | `validate_model` | `if any(not isinstance(tid, str) or not tid for tid in disabled):` | `test_unknown_disabled_transition_fails` (L821); `test_disabled_transition_ids_must_be_strings` (L827); `test_relation_guarded_profile_blocks_transition_when_prerequisite_disabled` (L1034) | PENDING_ASSERTION_REVIEW |
| 193 | `validate_model` | `if unknown:` | `test_unknown_state_reference_fails` (L139); `test_unknown_initial_state_string_fails` (L145); `test_unknown_transition_source_state_fails` (L154) | PENDING_ASSERTION_REVIEW |
| 195 | `validate_model` | `if len(disabled) != len(set(disabled)):` | `test_unknown_disabled_transition_fails` (L821); `test_disabled_transition_ids_must_be_strings` (L827); `test_relation_guarded_profile_blocks_transition_when_prerequisite_disabled` (L1034) | PENDING_ASSERTION_REVIEW |
| 197 | `validate_model` | `if "baseline" not in scenario_ids:` | `test_baseline_comparison_reports_expected_reachability_and_trajectory_differences` (L60); `test_baseline_comparison_propagates_truncation_from_either_scenario` (L97); `test_baseline_comparison_propagates_truncation_when_only_intervention_is_truncated` (L114) | PENDING_ASSERTION_REVIEW |
| 201 | `validate_model` | `if not isinstance(exploration, dict):` | `test_relation_guarded_profile_cycle_and_exploration_caps_are_explicit` (L1517); `test_schema_rejects_boolean_and_negative_exploration_bounds` (L1667) | PENDING_ASSERTION_REVIEW |
| 205 | `validate_model` | `if not isinstance(max_depth, int) or isinstance(max_depth, bool) or max_depth < 0:` | `test_schema_rejects_boolean_and_negative_exploration_bounds` (L1667) | PENDING_ASSERTION_REVIEW |
| 207 | `validate_model` | `if not isinstance(max_trajectories, int) or isinstance(max_trajectories, bool) or max_trajectories < 1:` | `test_schema_rejects_boolean_and_negative_exploration_bounds` (L1667) | PENDING_ASSERTION_REVIEW |
| 210 | `validate_model` | `if len(states) > 500 or len(transitions) > 2000:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 212 | `validate_model` | `if max_depth > 100 or max_trajectories > 10000:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 223 | `_scenario_result` | `if model["rule_profile"] == {"type": "relation_guarded_graph", "version": "1"}:` | `test_exported_package_rejects_unsupported_package_version_even_with_recomputed_hash` (L451); `test_integrity_rejects_missing_or_malformed_engine_version_even_with_recomputed_package_hash` (L542); `test_schema_type_and_required_field_validation_matrix` (L603) | PENDING_ASSERTION_REVIEW |
| 224 | `_scenario_result` | `for relation in sorted(model.get("relations", []), key=lambda item: item["id"]):` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 234 | `_scenario_result` | `if blocked:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 240 | `_scenario_result` | `for t in transitions.values():` | `test_schema_resource_limits_reject_values_above_upper_bounds` (L1637); `test_canonical_json_rejects_unpaired_surrogates_and_non_json_values` (L1753) | PENDING_ASSERTION_REVIEW |
| 241 | `_scenario_result` | `if t.id not in disabled:` | `test_unknown_disabled_transition_fails` (L821); `test_disabled_transition_ids_must_be_strings` (L827); `test_relation_guarded_profile_blocks_transition_when_prerequisite_disabled` (L1034) | PENDING_ASSERTION_REVIEW |
| 243 | `_scenario_result` | `for outgoing in adjacency.values():` | `test_schema_resource_limits_reject_values_above_upper_bounds` (L1637); `test_canonical_json_rejects_unpaired_surrogates_and_non_json_values` (L1753); `test_zero_depth_with_enabled_outgoing_transition_is_explicitly_truncated` (L1826) | PENDING_ASSERTION_REVIEW |
| 249 | `_scenario_result` | `while queue:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 251 | `_scenario_result` | `for transition in adjacency[state]:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 252 | `_scenario_result` | `if transition.target not in reached:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 262 | `_scenario_result` | `while stack:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 264 | `_scenario_result` | `if depth >= max_depth:` | `test_cycle_terminates_and_marks_depth_truncation` (L241); `test_depth_boundary_distinguishes_pending_transition_from_terminal_path` (L255); `test_terminal_path_at_depth_boundary_is_not_truncated` (L286) | PENDING_ASSERTION_REVIEW |
| 265 | `_scenario_result` | `if adjacency[state]:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 267 | `_scenario_result` | `if len(trajectories) < max_trajectories:` | `test_disabling_transitions_cannot_expand_reachability_or_trajectories` (L196); `test_adding_guard_cannot_expand_reachability_or_trajectories` (L1415) | PENDING_ASSERTION_REVIEW |
| 269 | `_scenario_result` | `else:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 274 | `_scenario_result` | `if not outgoing:` | `test_zero_depth_with_enabled_outgoing_transition_is_explicitly_truncated` (L1826) | PENDING_ASSERTION_REVIEW |
| 275 | `_scenario_result` | `if len(trajectories) < max_trajectories:` | `test_disabling_transitions_cannot_expand_reachability_or_trajectories` (L196); `test_adding_guard_cannot_expand_reachability_or_trajectories` (L1415) | PENDING_ASSERTION_REVIEW |
| 277 | `_scenario_result` | `else:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 282 | `_scenario_result` | `for transition in reversed(outgoing):` | `test_zero_depth_with_enabled_outgoing_transition_is_explicitly_truncated` (L1826) | PENDING_ASSERTION_REVIEW |
| 286 | `_scenario_result` | `if len(trajectories) >= max_trajectories and stack:` | `test_disabling_transitions_cannot_expand_reachability_or_trajectories` (L196); `test_adding_guard_cannot_expand_reachability_or_trajectories` (L1415) | PENDING_ASSERTION_REVIEW |
| 301 | `_scenario_result` | `if model["rule_profile"] == {"type": "relation_guarded_graph", "version": "1"}:` | `test_exported_package_rejects_unsupported_package_version_even_with_recomputed_hash` (L451); `test_integrity_rejects_missing_or_malformed_engine_version_even_with_recomputed_package_hash` (L542); `test_schema_type_and_required_field_validation_matrix` (L603) | PENDING_ASSERTION_REVIEW |
| 314 | `run_model` | `for sid, result in results.items():` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 315 | `run_model` | `if sid == "baseline":` | `test_baseline_comparison_reports_expected_reachability_and_trajectory_differences` (L60); `test_baseline_comparison_propagates_truncation_from_either_scenario` (L97); `test_baseline_comparison_propagates_truncation_when_only_intervention_is_truncated` (L114) | PENDING_ASSERTION_REVIEW |
| 367 | `verify_exported_package_integrity` | `if not isinstance(package, dict) or not required.issubset(package):` | `test_schema_type_and_required_field_validation_matrix` (L603); `test_top_level_model_and_required_string_fields_reject_wrong_types` (L1988) | PENDING_ASSERTION_REVIEW |
| 369 | `verify_exported_package_integrity` | `if package["package_version"] != "collective-toy-run-package-001":` | `test_exported_package_rejects_unsupported_package_version_even_with_recomputed_hash` (L451) | PENDING_ASSERTION_REVIEW |
| 371 | `verify_exported_package_integrity` | `if not isinstance(package["engine_version"], str) or not package["engine_version"]:` | `test_integrity_rejects_missing_or_malformed_engine_version_even_with_recomputed_package_hash` (L542) | PENDING_ASSERTION_REVIEW |
| 373 | `verify_exported_package_integrity` | `if not isinstance(package["input"], dict) or not isinstance(package["result"], dict):` | `test_export_package_detects_tampering_of_input_result_and_package` (L389); `test_export_contains_reproduction_inputs_and_hashes` (L574); `test_deterministic_malformed_input_mutation_matrix` (L1579) | PENDING_ASSERTION_REVIEW |
| 378 | `verify_exported_package_integrity` | `if sha256_json(package_payload) != package["package_sha256"]:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 382 | `verify_exported_package_integrity` | `if not {"input_sha256", "result_sha256"}.issubset(result):` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 384 | `verify_exported_package_integrity` | `if sha256_json(package["input"]) != result["input_sha256"]:` | `test_export_package_detects_tampering_of_input_result_and_package` (L389); `test_export_contains_reproduction_inputs_and_hashes` (L574); `test_deterministic_malformed_input_mutation_matrix` (L1579) | PENDING_ASSERTION_REVIEW |
| 389 | `verify_exported_package_integrity` | `if sha256_json(result_payload) != expected_result_sha256:` | No lexical candidate | PENDING_ASSERTION_REVIEW |
| 413 | `assess_exported_package` | `if package["engine_version"] != ENGINE_VERSION:` | `test_integrity_rejects_missing_or_malformed_engine_version_even_with_recomputed_package_hash` (L542) | PENDING_ASSERTION_REVIEW |
| 420 | `assess_exported_package` | `if run_model(package["input"]) != package["result"]:` | `test_export_package_detects_tampering_of_input_result_and_package` (L389); `test_export_contains_reproduction_inputs_and_hashes` (L574); `test_deterministic_malformed_input_mutation_matrix` (L1579) | PENDING_ASSERTION_REVIEW |
| 433 | `verify_exported_package` | `if assessment["status"] != "replay-verified":` | `test_package_assessment_reports_replay_verified_for_current_engine` (L509); `test_current_baseline_package_fixture_is_canonical_and_replay_verified` (L324); `test_unknown_engine_can_be_integrity_verified_but_not_replayed` (L468) | PENDING_ASSERTION_REVIEW |
| 461 | `demo_model` | `if __name__ == "__main__":` | No lexical candidate | PENDING_ASSERTION_REVIEW |

## Required closure criteria

For every `if` / `elif`, document a test for each relevant outcome (true/false or exception) where feasible. For loops and truncation exits, document the zero/one/multiple iteration and boundary outcomes that are contractually meaningful. For each mapped test, inspect the actual assertion; distinguish hand-computed expected output, rejection/error contract, metamorphic invariant, generated fixture, and cross-runtime agreement. Mark a branch `DIRECT`, `INDIRECT`, `MISSING`, or `NOT_APPLICABLE` only after that inspection. If a gap remains, add only the smallest test-only patch with an independent expected outcome.

No engine behavior, baseline fixture, hashes, schema contract, scientific claim, or authorization state is changed by this worklist. It authorizes no scientific execution or promotion.
