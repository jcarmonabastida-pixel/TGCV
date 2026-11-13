"""Tests for descriptive C10-S benchmark statistics; no simulation is run."""
import unittest

from vcont_benchmark_protocol import (
    ProtocolError, required_replicates, summarize_binary,
    summarize_continuous, summarize_scenario,
)


class VContBenchmarkProtocolTests(unittest.TestCase):
    def test_continuous_summary_reports_bias_mae_rmse_and_mcse(self):
        s = summarize_continuous([1.0, 2.0, 3.0], truth=2.0, tolerance=0.1)
        self.assertEqual(s.n, 3)
        self.assertAlmostEqual(s.bias, 0.0)
        self.assertAlmostEqual(s.mae, 2.0/3.0)
        self.assertAlmostEqual(s.rmse, (2.0/3.0)**0.5)
        self.assertAlmostEqual(s.mcse_mean, 1.0/(3.0**0.5))
        self.assertTrue(s.recovered_within_tolerance)

    def test_continuous_summary_does_not_invent_tolerance(self):
        s = summarize_continuous([1.0, 1.1], truth=1.0)
        self.assertIsNone(s.recovered_within_tolerance)

    def test_binary_summary_reports_monte_carlo_uncertainty(self):
        s = summarize_binary([1, 1, 0, 0])
        self.assertEqual((s.n, s.successes), (4, 2))
        self.assertAlmostEqual(s.rate, 0.5)
        self.assertGreater(s.wilson_95_high, s.rate)
        self.assertLess(s.wilson_95_low, s.rate)

    def test_replicate_dimensioning_uses_calibration_sd(self):
        self.assertEqual(required_replicates(2.0, 0.1), 400)
        self.assertEqual(required_replicates(0.0, 0.1), 2)

    def test_scenario_keeps_missing_inference_metrics_explicit(self):
        s = summarize_scenario("R0_NULL", estimates=[0.0, 0.1], truth=0.0,
                               identified=[True, True], abstained=[False, False])
        self.assertIsNotNone(s.estimate)
        self.assertIsNotNone(s.identification_rate)
        self.assertIsNone(s.coverage_rate)
        self.assertIn("COVERAGE_NOT_EVALUATED", s.notes)
        self.assertIn("TYPE_I_ERROR_NOT_EVALUATED", s.notes)
        self.assertIn("POWER_NOT_EVALUATED", s.notes)

    def test_scenario_can_report_coverage_type_i_and_power_separately(self):
        s = summarize_scenario(
            "R0_NULL", covered=[True, True, False, True],
            rejected_null=[False, False, True, False],
            rejected_alternative=[True, True, False, True],
        )
        self.assertEqual(s.coverage_rate.rate, 0.75)
        self.assertEqual(s.type_i_error_rate.rate, 0.25)
        self.assertEqual(s.power_rate.rate, 0.75)

    def test_rejects_nonfinite_or_empty_estimates(self):
        for values in ([], [float("nan")], [float("inf")]):
            with self.assertRaises(ProtocolError):
                summarize_continuous(values, truth=0.0)

    def test_rejects_invalid_mcse_targets(self):
        with self.assertRaises(ProtocolError):
            required_replicates(1.0, 0.0)

    def test_rejects_mismatched_missing_truth(self):
        with self.assertRaises(ProtocolError):
            summarize_scenario("R0", estimates=[1.0])


if __name__ == "__main__":
    unittest.main()
