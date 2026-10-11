import copy
import unittest

from collective_toy_engine_001 import (
    ModelValidationError,
    demo_model,
    export_run,
    run_model,
    canonical_json,
    sha256_json,
)


class CollectiveToyEngineTests(unittest.TestCase):
    def setUp(self):
        self.model = demo_model()

    def test_diamond_fixture_matches_expected_reachability_and_paths(self):
        result = run_model(self.model)
        base = result["scenario_results"]["baseline"]
        intervention = result["scenario_results"]["block_ac"]
        self.assertEqual(base["reachable_states"], ["A", "B", "C", "D"])
        self.assertEqual(intervention["reachable_states"], ["A", "B", "D"])
        base_paths = {
            tuple(item.get("state") for item in path)
            for path in base["trajectories"]
            if path[-1].get("state") == "D"
        }
        intervention_paths = {
            tuple(item.get("state") for item in path)
            for path in intervention["trajectories"]
            if path[-1].get("state") == "D"
        }
        self.assertEqual(base_paths, {("A", "B", "D"), ("A", "C", "D")})
        self.assertEqual(intervention_paths, {("A", "B", "D")})
        self.assertFalse(base["truncated"])
        self.assertFalse(intervention["truncated"])

    def test_initial_state_must_be_a_string_id_and_malformed_containers_raise_validation_error(self):
        for invalid_initial_state in ([], {}, None, 1):
            with self.subTest(initial_state=invalid_initial_state):
                model = copy.deepcopy(self.model)
                model["initial_state"] = invalid_initial_state
                with self.assertRaises(ModelValidationError):
                    run_model(model)

    def test_unknown_state_reference_fails(self):
        model = copy.deepcopy(self.model)
        model["transitions"][0]["target"] = "UNKNOWN"
        with self.assertRaises(ModelValidationError):
            run_model(model)

    def test_duplicate_transition_id_fails(self):
        model = copy.deepcopy(self.model)
        model["transitions"].append(dict(model["transitions"][0]))
        with self.assertRaises(ModelValidationError):
            run_model(model)

    def test_intervention_does_not_change_unrelated_transition(self):
        result = run_model(self.model)
        base = result["scenario_results"]["baseline"]
        intervention = result["scenario_results"]["block_ac"]
        self.assertIn("t_ab", base["enabled_transitions_at_initial_state"])
        self.assertIn("t_ab", intervention["enabled_transitions_at_initial_state"])
        self.assertNotIn("t_ac", intervention["enabled_transitions_at_initial_state"])
        self.assertEqual(
            result["comparisons_to_baseline"]["block_ac"]["enabled_at_initial_removed"],
            ["t_ac"],
        )

    def test_cycle_terminates_and_marks_depth_truncation(self):
        model = copy.deepcopy(self.model)
        model["transitions"].append({"id": "t_ba", "source": "B", "target": "A"})
        model["exploration"]["max_depth"] = 3
        result = run_model(model)
        self.assertEqual(set(result["scenario_results"]["baseline"]["reachable_states"]), {"A", "B", "C", "D"})
        self.assertTrue(result["scenario_results"]["baseline"]["truncated"])

    def test_trajectory_limit_is_explicit(self):
        model = copy.deepcopy(self.model)
        model["exploration"]["max_trajectories"] = 1
        result = run_model(model)
        self.assertTrue(result["scenario_results"]["baseline"]["truncated"])

    def test_exact_trajectory_cap_does_not_mark_complete_enumeration_truncated(self):
        model = copy.deepcopy(self.model)
        model["states"] = ["A", "B"]
        model["initial_state"] = "A"
        model["transitions"] = [{"id": "t_ab", "source": "A", "target": "B"}]
        model["scenarios"] = [{"id": "baseline", "disabled_transitions": []}]
        model["exploration"] = {"max_depth": 4, "max_trajectories": 1}
        result = run_model(model)
        baseline = result["scenario_results"]["baseline"]
        self.assertEqual(baseline["trajectories"], [[{"state": "A"}, {"transition": "t_ab", "state": "B"}]])
        self.assertFalse(baseline["truncated"])

    def test_terminal_path_at_depth_boundary_is_not_truncated(self):
        model = copy.deepcopy(self.model)
        model["states"] = ["A", "B"]
        model["initial_state"] = "A"
        model["transitions"] = [{"id": "t_ab", "source": "A", "target": "B"}]
        model["scenarios"] = [{"id": "baseline", "disabled_transitions": []}]
        model["exploration"] = {"max_depth": 1, "max_trajectories": 10}
        result = run_model(model)
        baseline = result["scenario_results"]["baseline"]
        self.assertEqual(len(baseline["trajectories"]), 1)
        self.assertFalse(baseline["truncated"])

    def test_deterministic_result_hash(self):
        first = run_model(self.model)
        second = run_model(self.model)
        self.assertEqual(first["result_sha256"], second["result_sha256"])
        self.assertEqual(first["input_sha256"], second["input_sha256"])

    def test_canonical_json_normalizes_integral_floats_and_codepoint_sorts_unicode_keys(self):
        value = {"n": 1.0, "negative_zero": -0.0, "\U00010000": "supplementary", "\uE000": "bmp"}
        self.assertEqual(
            canonical_json(value),
            '{"n":1,"negative_zero":0,"\uE000":"bmp","𐀀":"supplementary"}',
        )
        self.assertEqual(sha256_json({"n": 1.0}), sha256_json({"n": 1}))

    def test_canonical_json_rejects_non_integer_and_unsafe_numbers(self):
        for value in ({"n": 1.5}, {"n": float("nan")}, {"n": 9_007_199_254_740_992}):
            with self.subTest(value=value):
                with self.assertRaises(ModelValidationError):
                    canonical_json(value)

    def test_canonical_json_rejects_unpaired_surrogates(self):
        with self.assertRaises(ModelValidationError):
            canonical_json({"label": "\ud800"})

    def test_export_contains_reproduction_inputs_and_hashes(self):
        package = export_run(self.model)
        self.assertEqual(package["input"], self.model)
        self.assertIn("result_sha256", package["result"])
        self.assertIn("package_sha256", package)

    def test_export_package_hashes_verify_and_export_replays_independently(self):
        package = export_run(self.model)

        package_payload = copy.deepcopy(package)
        del package_payload["package_sha256"]
        self.assertEqual(sha256_json(package_payload), package["package_sha256"])

        self.assertEqual(sha256_json(package["input"]), package["result"]["input_sha256"])
        result_payload = copy.deepcopy(package["result"])
        del result_payload["input_sha256"]
        del result_payload["result_sha256"]
        self.assertEqual(sha256_json(result_payload), package["result"]["result_sha256"])

        replayed = run_model(package["input"])
        self.assertEqual(replayed, package["result"])

        tampered = copy.deepcopy(package)
        tampered["input"]["transitions"][0]["target"] = "D"
        tampered_payload = copy.deepcopy(tampered)
        del tampered_payload["package_sha256"]
        self.assertNotEqual(sha256_json(tampered_payload), tampered["package_sha256"])
        self.assertNotEqual(sha256_json(tampered["input"]), tampered["result"]["input_sha256"])

    def test_schema_type_and_required_field_validation_matrix(self):
        cases = []

        model = copy.deepcopy(self.model)
        model["schema_version"] = "unsupported"
        cases.append(("schema-version", model))

        model = copy.deepcopy(self.model)
        model["model_id"] = "   "
        cases.append(("blank-model-id", model))

        model = copy.deepcopy(self.model)
        model.pop("initial_state")
        cases.append(("missing-initial-state", model))

        model = copy.deepcopy(self.model)
        model["transitions"] = [None]
        cases.append(("non-object-transition", model))

        model = copy.deepcopy(self.model)
        model["scenarios"] = [None]
        cases.append(("non-object-scenario", model))

        model = copy.deepcopy(self.model)
        model["scenarios"].append({"id": "baseline", "disabled_transitions": []})
        cases.append(("duplicate-scenario-id", model))

        model = copy.deepcopy(self.model)
        model["scenarios"][1]["disabled_transitions"] = "t_ac"
        cases.append(("disabled-transitions-not-list", model))

        model = copy.deepcopy(self.model)
        model["exploration"] = []
        cases.append(("exploration-not-object", model))

        model = copy.deepcopy(self.model)
        model["exploration"]["max_depth"] = True
        cases.append(("boolean-depth", model))

        model = copy.deepcopy(self.model)
        model["exploration"]["max_trajectories"] = 0
        cases.append(("zero-trajectory-cap", model))

        model = copy.deepcopy(self.model)
        model["exploration"]["max_depth"] = 101
        cases.append(("depth-over-resource-cap", model))

        model = copy.deepcopy(self.model)
        model["exploration"]["max_trajectories"] = 10001
        cases.append(("trajectory-cap-over-resource-limit", model))

        model = copy.deepcopy(self.model)
        model["states"] = ["S" + str(i) for i in range(501)]
        model["initial_state"] = "S0"
        model["transitions"] = []
        cases.append(("state-count-over-resource-cap", model))

        model = copy.deepcopy(self.model)
        model["transitions"] = [
            {"id": "t" + str(i), "source": "A", "target": "A"} for i in range(2001)
        ]
        cases.append(("transition-count-over-resource-cap", model))

        model = copy.deepcopy(self.model)
        model["unexpected_top_level"] = True
        cases.append(("unknown-top-level-field", model))

        model = copy.deepcopy(self.model)
        model["transitions"][0]["unexpected"] = True
        cases.append(("unknown-transition-field", model))

        model = copy.deepcopy(self.model)
        model["scenarios"][0]["unexpected"] = True
        cases.append(("unknown-scenario-field", model))

        model = copy.deepcopy(self.model)
        model["exploration"]["unexpected"] = True
        cases.append(("unknown-exploration-field", model))

        model = copy.deepcopy(self.model)
        model["rule_profile"]["unexpected"] = True
        cases.append(("unknown-rule-profile-field", model))

        # Systematic missing-required-field and wrong-container-type cases.
        for field in ("schema_version", "model_id", "states", "transitions",
                      "rule_profile", "scenarios", "exploration"):
            model = copy.deepcopy(self.model)
            model.pop(field)
            cases.append(("missing-required-" + field, model))

        model = copy.deepcopy(self.model)
        model["states"] = "A"
        cases.append(("states-not-list", model))

        model = copy.deepcopy(self.model)
        model["transitions"] = {}
        cases.append(("transitions-not-list", model))

        model = copy.deepcopy(self.model)
        model["rule_profile"] = None
        cases.append(("rule-profile-not-object", model))

        model = copy.deepcopy(self.model)
        model["relations"] = {}
        cases.append(("relations-not-list", model))

        model = copy.deepcopy(self.model)
        model["scenarios"][0]["disabled_transitions"] = ["t_ab", "t_ab"]
        cases.append(("duplicate-disabled-transition", model))

        # Nested-field presence, non-empty identifiers, and numeric type boundaries.
        for field in ("id", "source", "target"):
            model = copy.deepcopy(self.model)
            model["transitions"][0].pop(field)
            cases.append(("missing-transition-" + field, model))

        for field in ("id", "source", "target"):
            model = copy.deepcopy(self.model)
            model["transitions"][0][field] = ""
            cases.append(("empty-transition-" + field, model))

        model = copy.deepcopy(self.model)
        model["exploration"]["max_depth"] = 1.5
        cases.append(("fractional-max-depth", model))

        model = copy.deepcopy(self.model)
        model["exploration"]["max_trajectories"] = True
        cases.append(("boolean-max-trajectories", model))

        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "unknown_graph", "version": "1"}
        cases.append(("unknown-rule-profile-type", model))

        model = copy.deepcopy(self.model)
        model["scenarios"][0]["disabled_transitions"] = [""]
        cases.append(("empty-disabled-transition-id", model))

        # Nested relation/scenario/exploration field coverage (profile 2 where applicable).
        valid_relation = {
            "id": "r_schema", "type": "requires_transition_enabled",
            "transition_id": "t_bd", "requires_transition_id": "t_ab"
        }
        for field in ("id", "type", "transition_id", "requires_transition_id"):
            model = copy.deepcopy(self.model)
            model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
            relation = copy.deepcopy(valid_relation)
            relation.pop(field)
            model["relations"] = [relation]
            cases.append(("missing-relation-" + field, model))

        for field in ("id", "transition_id", "requires_transition_id"):
            model = copy.deepcopy(self.model)
            model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
            relation = copy.deepcopy(valid_relation)
            relation[field] = ""
            model["relations"] = [relation]
            cases.append(("empty-relation-" + field, model))

        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [None]
        cases.append(("non-object-relation", model))

        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        relation = copy.deepcopy(valid_relation)
        relation["unexpected"] = True
        model["relations"] = [relation]
        cases.append(("unknown-relation-field", model))

        model = copy.deepcopy(self.model)
        model["scenarios"][0].pop("id")
        cases.append(("missing-scenario-id", model))

        model = copy.deepcopy(self.model)
        model["scenarios"][0]["disabled_transitions"] = [1]
        cases.append(("non-string-disabled-transition-id", model))

        for field in ("max_depth", "max_trajectories"):
            model = copy.deepcopy(self.model)
            model["exploration"].pop(field)
            cases.append(("missing-exploration-" + field, model))

        for name, candidate in cases:
            with self.subTest(name=name):
                with self.assertRaises(ModelValidationError):
                    run_model(candidate)

    def test_relation_guard_cannot_reference_itself(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [{
            "id": "r_self",
            "type": "requires_transition_enabled",
            "transition_id": "t_ab",
            "requires_transition_id": "t_ab",
        }]
        with self.assertRaises(ModelValidationError):
            run_model(model)

    def test_duplicate_state_id_fails(self):
        model = copy.deepcopy(self.model)
        model["states"].append("A")
        with self.assertRaises(ModelValidationError):
            run_model(model)

    def test_unknown_disabled_transition_fails(self):
        model = copy.deepcopy(self.model)
        model["scenarios"][1]["disabled_transitions"] = ["no_such_transition"]
        with self.assertRaises(ModelValidationError):
            run_model(model)

    def test_disabled_transition_ids_must_be_strings(self):
        for invalid_ids in ([{}], [None], [1], [""]):
            with self.subTest(invalid_ids=invalid_ids):
                model = copy.deepcopy(self.model)
                model["scenarios"][1]["disabled_transitions"] = invalid_ids
                with self.assertRaises(ModelValidationError):
                    run_model(model)

    def test_reachability_invariants_across_deterministic_generated_graphs(self):
        # Fixed-seed graph generation keeps this property suite reproducible.
        import random

        rng = random.Random(20261011)
        states = [f"S{i}" for i in range(5)]
        for case_index in range(30):
            transitions = []
            for source in states:
                for target in states:
                    if rng.random() < 0.24:
                        transitions.append({
                            "id": f"c{case_index}_t{len(transitions)}",
                            "source": source,
                            "target": target,
                        })
            disabled = [t["id"] for t in transitions if rng.random() < 0.18]
            model = {
                "schema_version": "collective-toy-input-001",
                "model_id": f"property-graph-{case_index:02d}",
                "initial_state": "S0",
                "states": states,
                "transitions": transitions,
                "relations": [],
                "rule_profile": {"type": "finite_deterministic_graph", "version": "1"},
                "scenarios": [
                    {"id": "baseline", "disabled_transitions": []},
                    {"id": "intervention", "disabled_transitions": disabled},
                ],
                "exploration": {"max_depth": 5, "max_trajectories": 500},
            }
            with self.subTest(case=case_index):
                result = run_model(model)
                base = result["scenario_results"]["baseline"]
                altered = result["scenario_results"]["intervention"]

                # Initial state is always reachable, and reachability never
                # includes an undeclared state.
                self.assertIn(model["initial_state"], base["reachable_states"])
                self.assertIn(model["initial_state"], altered["reachable_states"])
                self.assertLessEqual(set(base["reachable_states"]), set(states))
                self.assertLessEqual(set(altered["reachable_states"]), set(states))

                # Removing transitions cannot add reachable states in this
                # graph semantics, regardless of bounded trajectory output.
                self.assertLessEqual(
                    set(altered["reachable_states"]), set(base["reachable_states"])
                )

                # Every emitted path starts at the initial state and every
                # transition/state pair is a declared edge in that scenario.
                enabled = {
                    t["id"]: t for t in transitions if t["id"] not in set(disabled)
                }
                for path in altered["trajectories"]:
                    self.assertEqual(path[0], {"state": model["initial_state"]})
                    for previous, current in zip(path, path[1:]):
                        tid = current.get("transition")
                        self.assertIn(tid, enabled)
                        self.assertEqual(enabled[tid]["source"], previous["state"])
                        self.assertEqual(enabled[tid]["target"], current["state"])

    def test_relation_metadata_does_not_change_hashes_or_execution_in_profile_one(self):
        model_without = copy.deepcopy(self.model)
        model_with = copy.deepcopy(self.model)
        model_with["relations"] = [
            {"id": "r1", "type": "descriptive-only", "from": "A", "to": "D"}
        ]
        without_result = run_model(model_without)
        with_result = run_model(model_with)
        self.assertEqual(
            without_result["scenario_results"], with_result["scenario_results"]
        )
        self.assertNotEqual(without_result["input_sha256"], with_result["input_sha256"])
        self.assertEqual(without_result["result_sha256"], with_result["result_sha256"])

    def test_relation_guarded_profile_blocks_transition_when_prerequisite_disabled(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [{
            "id": "r_guard_bd",
            "type": "requires_transition_enabled",
            "transition_id": "t_bd",
            "requires_transition_id": "t_ab",
        }]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_prerequisite", "disabled_transitions": ["t_ab"]},
        ]
        result = run_model(model)
        baseline = result["scenario_results"]["baseline"]
        intervention = result["scenario_results"]["disable_prerequisite"]
        self.assertNotIn("t_bd", baseline["effective_disabled_transitions"])
        self.assertIn("t_bd", intervention["effective_disabled_transitions"])
        self.assertIn("D", intervention["reachable_states"])  # alternate route A -> C -> D remains available
        self.assertFalse(any(step.get("transition") == "t_bd" for path in intervention["trajectories"] for step in path))
        self.assertEqual(intervention["relation_effects"], [{
            "relation_id": "r_guard_bd",
            "type": "requires_transition_enabled",
            "transition_id": "t_bd",
            "requires_transition_id": "t_ab",
            "status": "BLOCKED",
            "reason": "prerequisite_transition_disabled",
        }])
        self.assertEqual(baseline["relation_effects"][0]["status"], "APPLIED")

    def test_relation_guarded_profile_applies_multiple_guards_deterministically(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [
            {
                "id": "r_guard_bd",
                "type": "requires_transition_enabled",
                "transition_id": "t_bd",
                "requires_transition_id": "t_ab",
            },
            {
                "id": "r_guard_cd",
                "type": "requires_transition_enabled",
                "transition_id": "t_cd",
                "requires_transition_id": "t_ac",
            },
        ]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_both_prerequisites", "disabled_transitions": ["t_ab", "t_ac"]},
        ]
        first = run_model(model)
        second = run_model(model)
        baseline = first["scenario_results"]["baseline"]
        altered = first["scenario_results"]["disable_both_prerequisites"]
        self.assertEqual(first["result_sha256"], second["result_sha256"])
        self.assertEqual(
            [effect["relation_id"] for effect in altered["relation_effects"]],
            ["r_guard_bd", "r_guard_cd"],
        )
        self.assertEqual(
            [effect["status"] for effect in altered["relation_effects"]],
            ["BLOCKED", "BLOCKED"],
        )
        self.assertEqual(altered["effective_disabled_transitions"], ["t_ab", "t_ac", "t_bd", "t_cd"])
        self.assertEqual(altered["reachable_states"], ["A"])
        self.assertIn("D", baseline["reachable_states"])

    def test_multiple_guards_for_same_transition_use_explicit_interventions(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [
            {"id": "r_guard_bd_by_ab", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ab"},
            {"id": "r_guard_bd_by_ac", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ac"},
        ]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_ab_only", "disabled_transitions": ["t_ab"]},
        ]
        result = run_model(model)
        altered = result["scenario_results"]["disable_ab_only"]
        self.assertEqual(
            [(effect["relation_id"], effect["status"]) for effect in altered["relation_effects"]],
            [("r_guard_bd_by_ab", "BLOCKED"), ("r_guard_bd_by_ac", "APPLIED")],
        )
        self.assertEqual(altered["effective_disabled_transitions"], ["t_ab", "t_bd"])
        self.assertNotIn("t_cd", altered["effective_disabled_transitions"])

    def test_cyclic_guard_relations_are_not_recursively_evaluated(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [
            {"id": "r_ab_requires_bd", "type": "requires_transition_enabled",
             "transition_id": "t_ab", "requires_transition_id": "t_bd"},
            {"id": "r_bd_requires_ab", "type": "requires_transition_enabled",
             "transition_id": "t_bd", "requires_transition_id": "t_ab"},
        ]
        model["scenarios"] = [
            {"id": "baseline", "disabled_transitions": []},
            {"id": "disable_ab_only", "disabled_transitions": ["t_ab"]},
        ]
        result = run_model(model)
        baseline = result["scenario_results"]["baseline"]
        altered = result["scenario_results"]["disable_ab_only"]
        self.assertEqual(
            [(effect["relation_id"], effect["status"]) for effect in baseline["relation_effects"]],
            [("r_ab_requires_bd", "APPLIED"), ("r_bd_requires_ab", "APPLIED")],
        )
        self.assertEqual(
            [(effect["relation_id"], effect["status"]) for effect in altered["relation_effects"]],
            [("r_ab_requires_bd", "APPLIED"), ("r_bd_requires_ab", "BLOCKED")],
        )
        self.assertEqual(altered["effective_disabled_transitions"], ["t_ab", "t_bd"])
        self.assertNotIn("t_ac", altered["effective_disabled_transitions"])

    def test_relation_guarded_profile_cycle_and_exploration_caps_are_explicit(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["transitions"].append({"id": "t_ba", "source": "B", "target": "A"})
        model["relations"] = [{
            "id": "r_guard_bd",
            "type": "requires_transition_enabled",
            "transition_id": "t_bd",
            "requires_transition_id": "t_ab",
        }]
        model["exploration"] = {"max_depth": 3, "max_trajectories": 2}
        result = run_model(model)
        baseline = result["scenario_results"]["baseline"]
        self.assertEqual(set(baseline["reachable_states"]), {"A", "B", "C", "D"})
        self.assertTrue(baseline["truncated"])
        self.assertLessEqual(len(baseline["trajectories"]), 2)
        self.assertEqual(baseline["exploration_bounds"], {"max_depth": 3, "max_trajectories": 2})

    def test_relation_guarded_profile_rejects_unknown_relation_references(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [{
            "id": "r_bad",
            "type": "requires_transition_enabled",
            "transition_id": "t_bd",
            "requires_transition_id": "missing",
        }]
        with self.assertRaises(ModelValidationError):
            run_model(model)

    def test_relation_guarded_profile_rejects_unknown_relation_types(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        model["relations"] = [{
            "id": "r_bad",
            "type": "mystery",
            "transition_id": "t_bd",
            "requires_transition_id": "t_ab",
        }]
        with self.assertRaises(ModelValidationError):
            run_model(model)

    def test_relation_guarded_profile_rejects_duplicate_relation_ids(self):
        model = copy.deepcopy(self.model)
        model["rule_profile"] = {"type": "relation_guarded_graph", "version": "1"}
        relation = {
            "id": "r_duplicate",
            "type": "requires_transition_enabled",
            "transition_id": "t_bd",
            "requires_transition_id": "t_ab",
        }
        model["relations"] = [relation, copy.deepcopy(relation)]
        with self.assertRaises(ModelValidationError):
            run_model(model)

    def test_relations_are_inert_metadata_in_profile_one(self):
        baseline = run_model(self.model)["scenario_results"]
        model = copy.deepcopy(self.model)
        model["relations"] = [{"id": "r1", "type": "descriptive-only", "from": "A", "to": "D"}]
        with_relations = run_model(model)["scenario_results"]
        self.assertEqual(baseline, with_relations)


if __name__ == "__main__":
    unittest.main(verbosity=2)
