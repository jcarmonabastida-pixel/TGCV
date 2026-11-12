"""Contract tests for the integrated V_cont synthetic harness.

These tests are intentionally not run as part of documentary/code authoring.
Running them generates synthetic truth and requires the explicit execution gate.
"""
import unittest

from vcont_integrated_harness import (
    Analyzer, Evaluator, Generator, Sealer, benchmark_scenarios, contract_for,
    FirewallError,
)


class VContIntegratedHarnessTests(unittest.TestCase):
    def setUp(self):
        self.generator = Generator()
        self.sealer = Sealer()
        self.analyzer = Analyzer()
        self.evaluator = Evaluator()

    def execute_world(self, cfg):
        manifest, truth, candidate = self.generator.generate(cfg)
        sealed = self.sealer.seal(candidate)
        contract = contract_for(cfg)
        result = self.analyzer.analyze(sealed, contract)
        report = self.evaluator.evaluate(truth, result, contract, tolerance=0.10)
        return manifest, truth, sealed, result, report

    def worlds(self):
        return {cfg.scenario_id: cfg for cfg in benchmark_scenarios(n_units=400, n_intervals=20)}

    def test_clean_positive_recovers_package_and_focal(self):
        _, _, _, result, report = self.execute_world(self.worlds()["R0_FOCAL_POSITIVE"])
        self.assertEqual(result.package_status, "IDENTIFIED")
        self.assertEqual(result.focal_status, "IDENTIFIED")
        self.assertIsNotNone(report.package_recovered)
        self.assertIsNotNone(report.focal_recovered)
        self.assertTrue(all(x > 0.80 for x in result.first_stage_delta_t_acc))

    def test_null_and_adverse_truth_signs_are_preserved(self):
        worlds = self.worlds()
        _, truth0, _, result0, _ = self.execute_world(worlds["R0_FOCAL_NULL"])
        _, truthn, _, resultn, _ = self.execute_world(worlds["R0_FOCAL_ADVERSE"])
        self.assertAlmostEqual(truth0.theta_access_truth, 0.0, delta=0.02)
        self.assertLess(truthn.theta_access_truth, 0.0)
        self.assertEqual(result0.focal_status, "IDENTIFIED")
        self.assertEqual(resultn.focal_status, "IDENTIFIED")

    def test_direct_focal_path_blocks_focal_attribution_not_package_itt(self):
        _, _, _, result, _ = self.execute_world(self.worlds()["R0_DIRECT_G"])
        self.assertEqual(result.package_status, "IDENTIFIED")
        self.assertEqual(result.focal_status, "NOT_IDENTIFIED")
        self.assertIsNone(result.focal_effect)

    def test_direct_package_path_preserves_package_itt_only(self):
        _, _, _, result, _ = self.execute_world(self.worlds()["R0_DIRECT_Z"])
        self.assertEqual(result.package_status, "IDENTIFIED")
        self.assertEqual(result.focal_status, "IDENTIFIED")

    def test_alternative_baseline_blocks_focal_first_stage(self):
        _, truth, _, result, _ = self.execute_world(self.worlds()["R1_ALTERNATIVE_BASELINE"])
        self.assertAlmostEqual(truth.theta_access_truth, 0.0, delta=0.02)
        self.assertEqual(result.focal_status, "IDENTIFIED")

    def test_b1_truth_is_conjunction_of_enabled_and_profile(self):
        _, truth, _, _, _ = self.execute_world(self.worlds()["R0_FOCAL_POSITIVE"])
        for i, unit in enumerate(truth.potential_interval_truth):
            for z in (0, 1):
                for g in (0, 1):
                    derived = tuple(
                        int(en and pr)
                        for en, pr in zip(
                            truth.potential_enabled_truth[i][z][g],
                            truth.potential_profile_truth[i][z][g],
                        )
                    )
                    self.assertEqual(derived, unit[z][g])

    def test_r2_collateral_alternative_and_r3_provision_are_separate(self):
        _, truth2, _, result2, _ = self.execute_world(self.worlds()["R2_ALTERNATIVE_AFFECTED"])
        _, truth3, _, result3, _ = self.execute_world(self.worlds()["R3_PROVISION_FAILURE"])
        self.assertEqual(result2.package_status, "IDENTIFIED")
        self.assertEqual(result2.focal_status, "IDENTIFIED")
        self.assertLess(truth3.itt_package_truth, 0.0)
        self.assertEqual(result3.package_status, "IDENTIFIED")
        self.assertGreater(result3.first_stage_delta_t_acc[0], 0.0)

    def test_manifest_uses_equal_intervals_over_common_window(self):
        manifest, _, _, _, _ = self.execute_world(self.worlds()["R0_FOCAL_POSITIVE"])
        self.assertAlmostEqual(manifest.window_start, 0.0)
        self.assertAlmostEqual(manifest.window_end, 1.0)
        self.assertAlmostEqual(manifest.interval_width * manifest.n_intervals, 1.0)

    def test_measurement_adversity_requires_abstention(self):
        _, _, _, result, report = self.execute_world(self.worlds()["R0_MEASUREMENT_ADVERSE"])
        self.assertEqual(result.package_status, "INDETERMINATE")
        self.assertEqual(result.focal_status, "INDETERMINATE")
        self.assertTrue(report.expected_abstention_respected)

    def test_interference_requires_cluster_level_analysis(self):
        _, _, _, result, report = self.execute_world(self.worlds()["R0_INTERFERENCE"])
        self.assertEqual(result.package_status, "INDETERMINATE")
        self.assertEqual(result.focal_status, "INDETERMINATE")
        self.assertTrue(report.expected_abstention_respected)

    def test_support_failure_blocks_focal_but_not_package(self):
        _, _, _, result, report = self.execute_world(self.worlds()["R0_SUPPORT_FAILURE"])
        self.assertEqual(result.package_status, "IDENTIFIED")
        self.assertEqual(result.focal_status, "NOT_IDENTIFIED")
        self.assertTrue(report.expected_abstention_respected)

    def test_sealed_evidence_tampering_is_detected(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        _, _, candidate = self.generator.generate(cfg)
        sealed = self.sealer.seal(candidate)
        mutated = dict(sealed.rows[0])
        mutated["assignment_z"] = 1 - mutated["assignment_z"]
        from dataclasses import replace
        tampered = replace(sealed, rows=(mutated,) + sealed.rows[1:])
        with self.assertRaises(FirewallError):
            self.analyzer.analyze(tampered, contract_for(cfg))


if __name__ == "__main__":
    unittest.main()
