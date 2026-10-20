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


if __name__ == "__main__":
    unittest.main()
