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


if __name__ == "__main__":
    unittest.main(verbosity=2)
