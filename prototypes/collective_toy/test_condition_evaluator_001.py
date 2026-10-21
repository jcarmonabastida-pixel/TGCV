"""Focused tests for the deterministic condition evaluator."""
import unittest

from condition_evaluator_001 import evaluate_condition


class ConditionEvaluatorTests(unittest.TestCase):
    def test_true_and_false_comparisons(self):
        self.assertEqual(evaluate_condition("soil_moisture_pct < 30", {"soil_moisture_pct": 20}).status, "TRUE")
        self.assertEqual(evaluate_condition("soil_moisture_pct < 30", {"soil_moisture_pct": 40}).status, "FALSE")

    def test_boundary_is_explicit(self):
        self.assertEqual(evaluate_condition("soil_moisture_pct <= 30", {"soil_moisture_pct": 30}).status, "TRUE")
        self.assertEqual(evaluate_condition("soil_moisture_pct < 30", {"soil_moisture_pct": 30}).status, "FALSE")

    def test_missing_or_invalid_data_never_guesses(self):
        self.assertEqual(evaluate_condition("soil_moisture_pct < 30", {}).reason, "missing_variable")
        self.assertEqual(evaluate_condition("soil_moisture_pct < 30", {"soil_moisture_pct": True}).reason, "variable_not_numeric")
        self.assertEqual(evaluate_condition("soil_moisture_pct < 30", {"soil_moisture_pct": float("nan")}).reason, "variable_not_finite")

    def test_arbitrary_code_and_unrecognised_language_are_rejected(self):
        self.assertEqual(evaluate_condition("__import__('os').system('true')", {}).reason, "unsupported_expression")
        self.assertEqual(evaluate_condition("la humedad del suelo es baja", {}).reason, "unsupported_expression")
        self.assertEqual(evaluate_condition("soil_moisture_pct ** 2", {"soil_moisture_pct": 10}).reason, "unsupported_expression")


class ConcreteSequenceConditionTests(unittest.TestCase):
    def _model(self, gate_value):
        return {
            "schema_version": "collective-toy-input-002",
            "model_id": "concrete-condition-execution",
            "initial_state": "A",
            "states": ["A", "B"],
            "transitions": [{"id": "t_ab", "source": "A", "target": "B", "condition": "gate == 1"}],
            "relations": [],
            "rule_profile": {"type": "temporal_prerequisite_graph", "version": "1"},
            "scenarios": [{"id": "baseline", "disabled_transitions": []}],
            "exploration": {"max_depth": 3, "max_trajectories": 10},
            "condition_values": {"gate": gate_value},
        }

    def test_true_condition_can_be_executed_concretely(self):
        from collective_toy_engine_001 import execute_sequence
        result = execute_sequence(self._model(1), "baseline", ["t_ab"])
        self.assertEqual(result["status"], "PASS")
        self.assertEqual(result["steps"][0]["state_before"], "A")
        self.assertEqual(result["steps"][0]["state_after"], "B")

    def test_false_condition_blocks_concrete_execution(self):
        from collective_toy_engine_001 import execute_sequence
        result = execute_sequence(self._model(0), "baseline", ["t_ab"])
        self.assertEqual(result["status"], "BLOCKED")
        self.assertEqual(result["blocked_step"]["reason"], "condition_false")
        self.assertEqual(result["final_state"], "A")

    def test_unevaluable_condition_blocks_concrete_execution(self):
        from collective_toy_engine_001 import execute_sequence
        model = self._model(1)
        model["condition_values"] = {}
        result = execute_sequence(model, "baseline", ["t_ab"])
        self.assertEqual(result["status"], "BLOCKED")
        self.assertEqual(result["blocked_step"]["reason"], "condition_not_evaluable")
        self.assertEqual(result["final_state"], "A")


if __name__ == "__main__":
    unittest.main()
