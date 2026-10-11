import copy
import unittest

from collective_toy_engine_001 import (
    ModelValidationError,
    demo_model,
    export_run,
    run_model,
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

    def test_deterministic_result_hash(self):
        first = run_model(self.model)
        second = run_model(self.model)
        self.assertEqual(first["result_sha256"], second["result_sha256"])
        self.assertEqual(first["input_sha256"], second["input_sha256"])

    def test_export_contains_reproduction_inputs_and_hashes(self):
        package = export_run(self.model)
        self.assertEqual(package["input"], self.model)
        self.assertIn("result_sha256", package["result"])
        self.assertIn("package_sha256", package)

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
        self.assertNotIn("D", intervention["reachable_states"])
        self.assertEqual(intervention["relation_effects"], [{
            "relation_id": "r_guard_bd",
            "type": "requires_transition_enabled",
            "transition_id": "t_bd",
            "requires_transition_id": "t_ab",
            "status": "BLOCKED",
            "reason": "prerequisite_transition_disabled",
        }])
        self.assertEqual(baseline["relation_effects"][0]["status"], "APPLIED")

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
