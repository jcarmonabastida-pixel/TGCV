"""Smoke tests for the P178 Analyzer Monte Carlo runner."""
from __future__ import annotations

import unittest

from run_p178_analyzer_monte_carlo import read_reference, run_cell


class P178AnalyzerMonteCarloSmokeTests(unittest.TestCase):
    def test_small_cell_runs_full_seal_analyze_evaluate_path(self):
        reference = read_reference()[(10, 0.5, "positive")]
        result = run_cell(
            pi0=0.5,
            k_slots=10,
            scenario="positive",
            replications=8,
            seed=20261495,
            reference_row=reference,
        )
        self.assertEqual(result["valid_replicates"], 8)
        self.assertEqual(result["invalid_replicates"], 0)
        self.assertEqual(result["classification_errors"], 0)
        self.assertEqual(result["abstentions"], 0)
        self.assertEqual(result["scenario"], "positive")
        self.assertTrue(result["mean_se"] > 0.0)


if __name__ == "__main__":
    unittest.main()
