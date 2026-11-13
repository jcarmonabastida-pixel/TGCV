"""Tests for descriptive C10-S benchmark statistics; no simulation is run."""
import unittest
from dataclasses import replace

from vcont_benchmark_protocol import (
    ProtocolError, build_seed_bank, SeedAssignment, required_replicates, select_minimum_n,
    summarize_binary, summarize_continuous, summarize_scenario, summarize_monte_carlo_rmse,
    seed_bank_fingerprint, validate_seed_banks, build_scenario_estimand_matrix, summarize_monte_carlo,
    select_minimum_n_by_estimand, required_replicates_by_estimand,
    validate_evaluation_observation, EvaluationKey, summarize_estimand,
    MonteCarloBenchmarkDesign, scenario_matrix_fingerprint,
    validate_monte_carlo_benchmark_design, SCENARIO_IDS,
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


    def test_outer_m_seed_bank_has_independent_worlds_and_designated_run(self):
        rows = build_seed_bank("calibration", ["R0"], [100], 3, "m-protocol",
                               {"R0": "DGP-001"}, outer_replicates=4)
        self.assertEqual(len(rows), 4 * (1 + 3))
        worlds = {}
        for row in rows:
            worlds.setdefault(row.outer_replicate_id, set()).add(row.world_seed)
        self.assertEqual(len(worlds), 4)
        self.assertTrue(all(len(seeds) == 1 for seeds in worlds.values()))
        self.assertEqual(len({next(iter(seeds)) for seeds in worlds.values()}), 4)
        for outer_id in worlds:
            group = [row for row in rows if row.outer_replicate_id == outer_id]
            self.assertEqual(sum(row.assignment_role == "RUN" for row in group), 1)
            self.assertEqual(sum(row.assignment_role == "REPEATED_ASSIGNMENT" for row in group), 3)
        validate_seed_banks(rows, ())

    def test_outer_m_fingerprint_includes_outer_identity_and_role(self):
        rows = build_seed_bank("calibration", ["R0"], [100], 2, "m-fingerprint",
                               outer_replicates=2)
        self.assertEqual(seed_bank_fingerprint(rows), seed_bank_fingerprint(tuple(rows)))
        altered = list(rows)
        altered[0] = __import__("dataclasses").replace(
            altered[0], outer_replicate_id="outer-altered")
        self.assertNotEqual(seed_bank_fingerprint(rows), seed_bank_fingerprint(altered))

    def test_monte_carlo_aggregator_requires_unique_complete_outer_contributions(self):
        summary = summarize_monte_carlo(
            [("m0", 1.0), ("m1", 1.2), ("m2", 0.8)],
            expected_m=3, target_mcse=0.2)
        self.assertEqual(summary.outer_replicates, 3)
        self.assertAlmostEqual(summary.metric_mean, 1.0)
        self.assertEqual(summary.precision_status, "PASS")
        with self.assertRaises(ProtocolError):
            summarize_monte_carlo([("m0", 1.0), ("m0", 1.2), ("m2", 0.8)],
                                  expected_m=3, target_mcse=0.2)
        with self.assertRaises(ProtocolError):
            summarize_monte_carlo([("m0", 1.0), ("m1", 1.2)],
                                  expected_m=3, target_mcse=0.2)


    def test_monte_carlo_rmse_uses_outer_squared_error_contributions(self):
        summary = summarize_monte_carlo_rmse(
            [("m0", 1.0), ("m1", 4.0), ("m2", 0.0)],
            expected_m=3, target_mcse=1.0)
        self.assertAlmostEqual(summary.mean_squared_error, 5.0/3.0)
        self.assertAlmostEqual(summary.rmse, (5.0/3.0)**0.5)
        self.assertIsNotNone(summary.mcse_rmse_delta)
        self.assertIn(summary.precision_status, ("PASS", "FAIL"))
        with self.assertRaises(ProtocolError):
            summarize_monte_carlo_rmse(
                [("m0", -1.0), ("m1", 0.0)], expected_m=2, target_mcse=1.0)

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
        numeric = [row.key for row in matrix if row.evaluation_class == "EVALUABLE"]
        targets, observed = {key: 0.1 for key in numeric}, {key: 0.05 for key in numeric}
        required = [row.key for row in matrix]
        self.assertEqual(select_minimum_n_by_estimand({100: observed}, targets, matrix, {100: required}), 100)
        with self.assertRaises(ProtocolError):
            select_minimum_n_by_estimand({100: observed}, targets, matrix, {100: required[:-1]})

    def test_pairwise_selection_rejects_missing_numeric_pair(self):
        matrix = build_scenario_estimand_matrix()
        numeric = [row.key for row in matrix if row.evaluation_class == "EVALUABLE"]
        required = [row.key for row in matrix]
        with self.assertRaises(ProtocolError):
            select_minimum_n_by_estimand({100: {key: 0.05 for key in numeric[:-1]}},
                {key: 0.1 for key in numeric}, matrix, {100: required})

    def test_non_numeric_classes_cannot_receive_numeric_pass(self):
        matrix = build_scenario_estimand_matrix()
        for cls in ("STATUS_ONLY", "NOT_IDENTIFIABLE"):
            spec = next(row for row in matrix if row.evaluation_class == cls)
            with self.assertRaises(ProtocolError):
                validate_evaluation_observation(spec, observed_key=spec.key, analyzer_output_field=None, dgp_truth=1.0, analyzer_output=1.0, adjudication="PASS", observed_identification_status="IDENTIFIED", observed_abstained=False)
            validate_evaluation_observation(spec, observed_key=spec.key, analyzer_output_field=None, dgp_truth=1.0, analyzer_output=None, adjudication="STATUS_PASS", observed_identification_status=spec.identification_expectation, observed_abstained=spec.abstention_expectation)

    def test_evaluable_pair_rejects_null_truth_and_missing_output(self):
        spec = next(row for row in build_scenario_estimand_matrix() if row.evaluation_class == "EVALUABLE")
        with self.assertRaises(ProtocolError):
            validate_evaluation_observation(spec, observed_key=spec.key, analyzer_output_field=spec.analyzer_output_field, dgp_truth=None, analyzer_output=1.0, adjudication="PASS", observed_identification_status="IDENTIFIED", observed_abstained=False)
        with self.assertRaises(ProtocolError):
            validate_evaluation_observation(spec, observed_key=spec.key, analyzer_output_field=spec.analyzer_output_field, dgp_truth=1.0, analyzer_output=None, adjudication="PASS", observed_identification_status="IDENTIFIED", observed_abstained=False)

    def test_pair_validator_rejects_mismatched_estimand_or_version(self):
        spec = next(row for row in build_scenario_estimand_matrix() if row.evaluation_class == "EVALUABLE")
        wrong_key = EvaluationKey(spec.key.scenario_id, spec.key.scenario_version,
                                  "ITT_G_Z0_VCONT", "999")
        with self.assertRaises(ProtocolError):
            validate_evaluation_observation(spec, observed_key=wrong_key,
                analyzer_output_field=spec.analyzer_output_field, dgp_truth=1.0,
                analyzer_output=1.0, adjudication="PASS", observed_identification_status="IDENTIFIED", observed_abstained=False)
        with self.assertRaises(ProtocolError):
            validate_evaluation_observation(spec, observed_key=spec.key,
                analyzer_output_field="g_assignment_effect", dgp_truth=1.0,
                analyzer_output=1.0, adjudication="PASS", observed_identification_status="IDENTIFIED", observed_abstained=False)

    def test_seed_bank_identity_includes_scenario_version(self):
        v1 = build_seed_bank("calibration", ["R0"], [100], 2, "protocol-v2", {"R0": "DGP-001"})
        v2 = build_seed_bank("calibration", ["R0"], [100], 2, "protocol-v2", {"R0": "DGP-002"})
        self.assertNotEqual(v1[0].world_seed, v2[0].world_seed)
        self.assertNotEqual(seed_bank_fingerprint(v1), seed_bank_fingerprint(v2))

    def test_r_dimensioning_is_estimand_specific(self):
        specs = [row for row in build_scenario_estimand_matrix() if row.evaluation_class == "EVALUABLE"][:2]
        keys = [row.key for row in specs]
        result = required_replicates_by_estimand({keys[0]: 2.0, keys[1]: 1.0}, {keys[0]: 0.1, keys[1]: 0.1}, specs)
        self.assertEqual(result, {keys[0]: 400, keys[1]: 100})

    def test_matrix_declares_distinct_temporal_evaluation_classes(self):
        specs = {row.key.estimand_id: row for row in build_scenario_estimand_matrix()
                 if row.key.scenario_id == "R0_FOCAL_POSITIVE"}
        self.assertEqual(specs["ITT_Z_RUN_CONDITIONAL_VCONT"].run_evaluation_class, "EVALUABLE")
        self.assertIsNone(specs["ITT_Z_RUN_CONDITIONAL_VCONT"].repeated_evaluation_class)
        self.assertIsNone(specs["ITT_Z_MECHANISM_MARGINAL_VCONT"].run_evaluation_class)
        self.assertEqual(specs["ITT_Z_MECHANISM_MARGINAL_VCONT"].repeated_evaluation_class, "EVALUABLE")
        self.assertEqual(specs["ITT_Z_REFERENCE_REGIME_VCONT"].run_evaluation_class, "STATUS_ONLY")
        self.assertEqual(specs["ITT_Z_REFERENCE_REGIME_VCONT"].repeated_evaluation_class, "EVALUABLE")
        self.assertEqual(specs["ITT_G_Z0_VCONT"].run_evaluation_class, "EVALUABLE")
        self.assertIsNone(specs["ITT_G_Z0_VCONT"].repeated_evaluation_class)
    def test_seed_assignment_exposes_typed_r_index(self):
        run = SeedAssignment("evaluation", SCENARIO_IDS[0], 400, -1, 101, 201, 301,
                             scenario_version="VCONT-SYNTH-001", outer_replicate_id="M0",
                             assignment_role="RUN")
        repeated = SeedAssignment("evaluation", SCENARIO_IDS[0], 400, 2, 101, 203, 303,
                                  scenario_version="VCONT-SYNTH-001", outer_replicate_id="M0")
        self.assertEqual(run.assignment_index, -1)
        self.assertEqual(repeated.assignment_index, 2)

    def test_monte_carlo_design_requires_exact_52_pair_matrix_and_targets(self):
        matrix = build_scenario_estimand_matrix()
        targets = []
        for spec in matrix:
            temporal = (spec.run_evaluation_class
                        if spec.key.estimand_id in ("ITT_Z_RUN_CONDITIONAL_VCONT", "ITT_G_Z0_VCONT")
                        else spec.repeated_evaluation_class)
            if temporal == "EVALUABLE":
                for metric in ("bias", "mae", "rmse"):
                    targets.append((spec.key.scenario_id, spec.key.scenario_version,
                                    spec.key.estimand_id, spec.key.estimand_version, metric, 0.05))
        design = MonteCarloBenchmarkDesign(
            scenario_versions=tuple((sid, "VCONT-SYNTH-001") for sid in SCENARIO_IDS),
            n_units=400, outer_replicates=2, repeated_assignments=3,
            matrix_fingerprint=scenario_matrix_fingerprint(matrix),
            metric_targets=tuple(targets), seed_bank_label="DETERMINISTIC_TEST_FIXTURE",
            seed_bank_fingerprint="a"*64, executable_commit="c"*40,
            configuration_fingerprint="b"*64,
        )
        self.assertEqual(len(validate_monte_carlo_benchmark_design(design, matrix)), 52)
        with self.assertRaises(ProtocolError):
            validate_monte_carlo_benchmark_design(
                replace(design, scenario_versions=design.scenario_versions[:-1]), matrix)
        with self.assertRaises(ProtocolError):
            validate_monte_carlo_benchmark_design(
                replace(design, metric_targets=design.metric_targets[:-1]), matrix)
        duplicated = matrix[:-1] + (matrix[0],)
        with self.assertRaises(ProtocolError):
            validate_monte_carlo_benchmark_design(design, duplicated)
        with self.assertRaises(ProtocolError):
            validate_monte_carlo_benchmark_design(
                replace(design, executable_commit="not-a-commit"), matrix)

    def test_mcse_precision_distinguishes_fail_from_not_evaluable(self):
        spec = next(row for row in build_scenario_estimand_matrix()
                    if row.evaluation_class == "EVALUABLE")
        failed = summarize_estimand(spec, estimates=[0.0, 2.0], truth=1.0, mcse_target=0.1)
        self.assertEqual(failed.precision_status, "FAIL")
        unavailable = summarize_estimand(spec, estimates=[1.0], truth=1.0, mcse_target=0.1)
        self.assertEqual(unavailable.precision_status, "NOT_EVALUABLE")
        passed = summarize_estimand(spec, estimates=[1.0, 1.0, 1.0], truth=1.0, mcse_target=0.1)
        self.assertEqual(passed.precision_status, "PASS")

if __name__ == "__main__":
    unittest.main()
