"""Tests for descriptive C10-S benchmark statistics; no simulation is run."""
import unittest

from vcont_benchmark_protocol import (
    ProtocolError, build_seed_bank, required_replicates, select_minimum_n,
    summarize_binary, summarize_continuous, summarize_scenario,
    seed_bank_fingerprint, validate_seed_banks, build_scenario_estimand_matrix,
    select_minimum_n_by_estimand, required_replicates_by_estimand,
    validate_evaluation_observation,
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



    def test_calibration_and_evaluation_seed_banks_are_disjoint(self):
        calibration = build_seed_bank("calibration", ["R0_NULL"], [100, 200], 3, "protocol-v1")
        evaluation = build_seed_bank("evaluation", ["R0_NULL"], [100, 200], 3, "protocol-v1")
        validate_seed_banks(calibration, evaluation)
        self.assertEqual(calibration[0].world_seed, calibration[1].world_seed)
        self.assertNotEqual(calibration[0].z_assignment_seed, calibration[1].z_assignment_seed)
        self.assertNotEqual(calibration[0].g_assignment_seed, calibration[1].g_assignment_seed)
        self.assertNotEqual(calibration[0].world_seed, evaluation[0].world_seed)

    def test_seed_bank_rejects_invalid_n_grid(self):
        with self.assertRaises(ProtocolError):
            build_seed_bank("calibration", ["R0"], [99], 2, "protocol-v1")

    def test_minimum_n_selection_requires_all_scenario_targets(self):
        observed = {
            100: {"R0_NULL": 0.08, "R0_POSITIVE": 0.15},
            200: {"R0_NULL": 0.04, "R0_POSITIVE": 0.08},
            400: {"R0_NULL": 0.02, "R0_POSITIVE": 0.04},
        }
        targets = {"R0_NULL": 0.05, "R0_POSITIVE": 0.10}
        self.assertEqual(select_minimum_n(observed, targets), 200)

    def test_minimum_n_fails_closed_if_no_candidate_meets_targets(self):
        with self.assertRaises(ProtocolError):
            select_minimum_n({100: {"R0": 0.2}}, {"R0": 0.1})


    def test_seed_bank_fingerprint_is_stable_and_bank_specific(self):
        cal = build_seed_bank("calibration", ["R0"], [100], 2, "protocol-v1")
        ev = build_seed_bank("evaluation", ["R0"], [100], 2, "protocol-v1")
        self.assertEqual(seed_bank_fingerprint(cal), seed_bank_fingerprint(tuple(cal)))
        self.assertNotEqual(seed_bank_fingerprint(cal), seed_bank_fingerprint(ev))

    def test_scenario_estimand_matrix_has_52_versioned_records(self):
        matrix = build_scenario_estimand_matrix()
        self.assertEqual(len(matrix), 52)
        self.assertEqual(len({row.key for row in matrix}), 52)
        self.assertEqual({row.key.scenario_version for row in matrix}, {"VCONT-SYNTH-001"})

    def test_pairwise_n_selection_requires_complete_coverage_and_mcse(self):
        matrix = build_scenario_estimand_matrix()
        required = [row.key for row in matrix]
        numeric = [row.key for row in matrix if row.evaluation_class == "EVALUABLE"]
        targets, observed = {key: 0.1 for key in numeric}, {key: 0.05 for key in numeric}
        self.assertEqual(select_minimum_n_by_estimand({100: observed}, targets, required, numeric, {100: required}), 100)
        with self.assertRaises(ProtocolError):
            select_minimum_n_by_estimand({100: observed}, targets, required, numeric, {100: required[:-1]})

    def test_pairwise_selection_rejects_missing_numeric_pair(self):
        matrix = build_scenario_estimand_matrix()
        required = [row.key for row in matrix]
        numeric = [row.key for row in matrix if row.evaluation_class == "EVALUABLE"]
        with self.assertRaises(ProtocolError):
            select_minimum_n_by_estimand({100: {key: 0.05 for key in numeric[:-1]}},
                {key: 0.1 for key in numeric}, required, numeric, {100: required})

    def test_non_numeric_classes_cannot_receive_numeric_pass(self):
        matrix = build_scenario_estimand_matrix()
        for cls in ("STATUS_ONLY", "NOT_IDENTIFIABLE"):
            spec = next(row for row in matrix if row.evaluation_class == cls)
            with self.assertRaises(ProtocolError):
                validate_evaluation_observation(spec, dgp_truth=1.0, analyzer_output=1.0, adjudication="PASS")
            validate_evaluation_observation(spec, dgp_truth=1.0, analyzer_output=None, adjudication="STATUS_PASS")

    def test_evaluable_pair_rejects_null_truth_and_missing_output(self):
        spec = next(row for row in build_scenario_estimand_matrix() if row.evaluation_class == "EVALUABLE")
        with self.assertRaises(ProtocolError):
            validate_evaluation_observation(spec, dgp_truth=None, analyzer_output=1.0, adjudication="PASS")
        with self.assertRaises(ProtocolError):
            validate_evaluation_observation(spec, dgp_truth=1.0, analyzer_output=None, adjudication="PASS")

    def test_seed_bank_identity_includes_scenario_version(self):
        v1 = build_seed_bank("calibration", ["R0"], [100], 2, "protocol-v2", {"R0": "DGP-001"})
        v2 = build_seed_bank("calibration", ["R0"], [100], 2, "protocol-v2", {"R0": "DGP-002"})
        self.assertNotEqual(v1[0].world_seed, v2[0].world_seed)
        self.assertNotEqual(seed_bank_fingerprint(v1), seed_bank_fingerprint(v2))

    def test_r_dimensioning_is_estimand_specific(self):
        keys = [row.key for row in build_scenario_estimand_matrix() if row.evaluation_class == "EVALUABLE"][:2]
        result = required_replicates_by_estimand({keys[0]: 2.0, keys[1]: 1.0}, {keys[0]: 0.1, keys[1]: 0.1})
        self.assertEqual(result, {keys[0]: 400, keys[1]: 100})

if __name__ == "__main__":
    unittest.main()
