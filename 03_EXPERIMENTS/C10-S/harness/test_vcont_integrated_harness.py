"""Contract tests for the integrated V_cont synthetic harness.

These tests are intentionally not run as part of documentary/code authoring.
Running them generates synthetic truth and requires the explicit execution gate.
"""
import unittest
from dataclasses import replace

from vcont_integrated_harness import (
    Analyzer, Evaluator, Generator, Sealer, benchmark_scenarios, contract_for,
    FirewallError, ContractError,
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
        report = self.evaluator.evaluate(truth, result, contract, tolerance=0.10, manifest=manifest)
        return manifest, truth, sealed, result, report

    def worlds(self):
        return {cfg.scenario_id: cfg for cfg in benchmark_scenarios(n_units=400, n_intervals=20)}


    def test_truth_bundle_separates_g_assignment_from_unmaterialized_theta_a(self):
        worlds = self.worlds()
        _, clean_truth, _ = self.generator.generate(worlds["R0_FOCAL_POSITIVE"])
        _, direct_truth, _ = self.generator.generate(worlds["R0_DIRECT_G"])
        self.assertIsNotNone(clean_truth.itt_g_z0_truth)
        self.assertIsNotNone(direct_truth.itt_g_z0_truth)
        self.assertIsNone(clean_truth.theta_a_truth)
        self.assertIsNone(direct_truth.theta_a_truth)
        # Same seed/exogenous draws; the direct G -> outcome path changes
        # the total G-assignment truth and is not mislabelled as theta_A.
        self.assertNotAlmostEqual(
            clean_truth.itt_g_z0_truth, direct_truth.itt_g_z0_truth, delta=0.01
        )

    def test_clean_positive_recovers_package_and_g_assignment(self):
        _, _, _, result, report = self.execute_world(self.worlds()["R0_FOCAL_POSITIVE"])
        self.assertEqual(result.package_status, "IDENTIFIED")
        self.assertEqual(result.g_assignment_status, "IDENTIFIED")
        self.assertIsNotNone(report.package_recovered)
        self.assertIsNotNone(report.g_assignment_recovered)
        self.assertTrue(all(x > 0.80 for x in result.first_stage_delta_t_acc))

    def test_null_and_adverse_truth_signs_are_preserved(self):
        worlds = self.worlds()
        _, truth0, _, result0, _ = self.execute_world(worlds["R0_FOCAL_NULL"])
        _, truthn, _, resultn, _ = self.execute_world(worlds["R0_FOCAL_ADVERSE"])
        self.assertAlmostEqual(truth0.itt_g_z0_truth, 0.0, delta=0.02)
        self.assertLess(truthn.itt_g_z0_truth, 0.0)
        self.assertEqual(result0.g_assignment_status, "IDENTIFIED")
        self.assertEqual(resultn.g_assignment_status, "IDENTIFIED")

    def test_g_assignment_does_not_require_z_randomization(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        manifest, truth, candidate = self.generator.generate(cfg)
        sealed = self.sealer.seal(candidate)
        contract = replace(contract_for(cfg), randomized_z=False)
        result = self.analyzer.analyze(sealed, contract)
        report = self.evaluator.evaluate(truth, result, contract, tolerance=0.10, manifest=manifest)
        self.assertEqual(result.package_status, "NOT_IDENTIFIED")
        self.assertEqual(result.g_assignment_status, "IDENTIFIED")
        self.assertIsNotNone(result.g_assignment_effect)
        self.assertIsNone(report.package_recovered)
        self.assertIsNotNone(report.g_assignment_recovered)
        self.assertTrue(report.expected_abstention_respected)

    def test_direct_g_path_does_not_contaminate_g_assignment_truth(self):
        _, _, _, result, _ = self.execute_world(self.worlds()["R0_DIRECT_G"])
        self.assertEqual(result.package_status, "IDENTIFIED")
        self.assertEqual(result.g_assignment_status, "IDENTIFIED")
        self.assertIsNotNone(result.g_assignment_effect)

    def test_direct_package_path_preserves_package_itt_only(self):
        _, _, _, result, _ = self.execute_world(self.worlds()["R0_DIRECT_Z"])
        self.assertEqual(result.package_status, "IDENTIFIED")
        self.assertEqual(result.g_assignment_status, "IDENTIFIED")

    def test_alternative_baseline_has_null_g_assignment_contrast(self):
        _, truth, _, result, _ = self.execute_world(self.worlds()["R1_ALTERNATIVE_BASELINE"])
        self.assertAlmostEqual(truth.itt_g_z0_truth, 0.0, delta=0.02)
        self.assertEqual(result.g_assignment_status, "IDENTIFIED")

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
        self.assertEqual(result2.g_assignment_status, "IDENTIFIED")
        self.assertLess(truth3.itt_z_truth, 0.0)
        self.assertEqual(result3.package_status, "IDENTIFIED")
        self.assertGreater(result3.first_stage_delta_t_acc[0], 0.0)

    def test_structural_support_failure_removes_high_stratum_g1(self):
        _, _, sealed, result, _ = self.execute_world(self.worlds()["R0_SUPPORT_FAILURE"])
        high = [row for row in sealed.rows if row["baseline_stratum"] == "HIGH"]
        self.assertTrue(high)
        self.assertTrue(all(row["assignment_g"] == 0 for row in high))
        self.assertEqual(result.g_assignment_status, "NOT_IDENTIFIED")

    def test_follow_up_freezes_state_after_last_transition_support(self):
        _, truth, _, _, _ = self.execute_world(self.worlds()["R0_FOCAL_POSITIVE"])
        for i in range(len(truth.potential_enabled_truth)):
            for z in (0, 1):
                for g in (0, 1):
                    enabled = truth.potential_enabled_truth[i][z][g]
                    profile = truth.potential_profile_truth[i][z][g]
                    self.assertEqual(enabled[16:], (enabled[15],) * 4)
                    self.assertEqual(profile[16:], (profile[15],) * 4)

    def test_manifest_uses_equal_intervals_over_common_window(self):
        manifest, _, _, _, _ = self.execute_world(self.worlds()["R0_FOCAL_POSITIVE"])
        self.assertAlmostEqual(manifest.window_start, 0.0)
        self.assertAlmostEqual(manifest.window_end, 1.0)
        self.assertAlmostEqual(manifest.interval_width * manifest.n_intervals, 1.0)

    def test_measurement_adversity_requires_abstention(self):
        _, _, _, result, report = self.execute_world(self.worlds()["R0_MEASUREMENT_ADVERSE"])
        self.assertEqual(result.package_status, "INDETERMINATE")
        self.assertEqual(result.g_assignment_status, "INDETERMINATE")
        self.assertTrue(report.expected_abstention_respected)

    def test_interference_requires_cluster_level_analysis(self):
        _, _, _, result, report = self.execute_world(self.worlds()["R0_INTERFERENCE"])
        self.assertEqual(result.package_status, "INDETERMINATE")
        self.assertEqual(result.g_assignment_status, "INDETERMINATE")
        self.assertTrue(report.expected_abstention_respected)

    def test_support_failure_blocks_g_assignment_but_not_package(self):
        _, _, _, result, report = self.execute_world(self.worlds()["R0_SUPPORT_FAILURE"])
        self.assertEqual(result.package_status, "IDENTIFIED")
        self.assertEqual(result.g_assignment_status, "NOT_IDENTIFIED")
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



    def test_itt_z_truths_are_separated_and_run_estimate_uses_matching_truth(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        manifest, truth, sealed, result, report = self.execute_world(cfg)
        self.assertIsNotNone(truth.itt_z_run_truth)
        self.assertIsNotNone(truth.itt_z_mechanism_truth)
        self.assertIsNotNone(truth.itt_z_reference_truth)
        self.assertAlmostEqual(truth.itt_z_reference_truth, truth.itt_z_truth)
        self.assertEqual(manifest.g_reference_regime_id, "G_REFERENCE_50_50")
        self.assertEqual(result.target_regime_id, "G_REALIZED_VECTOR")
        self.assertIsNotNone(report.package_abs_error)

    def test_fixed_world_uses_independent_assignment_streams(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        cfg_a = replace(cfg, world_seed=991, z_assignment_seed=11, g_assignment_seed=21, replicate_id="r1")
        cfg_b = replace(cfg, world_seed=991, z_assignment_seed=12, g_assignment_seed=22, replicate_id="r2")
        manifest_a, truth_a, candidate_a = self.generator.generate(cfg_a)
        manifest_b, truth_b, candidate_b = self.generator.generate(cfg_b)
        self.assertEqual(truth_a.potential_v, truth_b.potential_v)
        self.assertEqual(manifest_a.world_id, manifest_b.world_id)
        self.assertNotEqual([r["assignment_z"] for r in candidate_a.rows],
                            [r["assignment_z"] for r in candidate_b.rows])

    def test_support_failure_transportability_is_separate_from_run_level_itt_z(self):
        cfg = self.worlds()["R0_SUPPORT_FAILURE"]
        _, truth, _, result, _ = self.execute_world(cfg)
        self.assertTrue(truth.transportability_invariant_truth)
        self.assertEqual(result.package_status, "IDENTIFIED")
        self.assertEqual(result.reference_regime_status, "IDENTIFIED")
        self.assertEqual(result.g_assignment_status, "NOT_IDENTIFIED")

    def test_adversarial_support_failure_zg_interaction_blocks_reference_regime(self):
        cfg = self.worlds()["R2_SUPPORT_FAILURE_ZG_INTERACTION"]
        _, truth, sealed, result, report = self.execute_world(cfg)
        high = [r for r in sealed.rows if r["baseline_stratum"] == "HIGH"]
        self.assertTrue(high)
        self.assertTrue(all(r["assignment_g"] == 0 for r in high))
        self.assertFalse(truth.transportability_invariant_truth)
        self.assertEqual(result.package_status, "IDENTIFIED")
        self.assertEqual(result.reference_regime_status, "NOT_IDENTIFIED")
        self.assertEqual(result.g_assignment_status, "NOT_IDENTIFIED")
        self.assertTrue(report.reference_regime_status_correct)

    def test_evaluator_rejects_target_regime_mismatch(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        manifest, truth, _, result, _ = self.execute_world(cfg)
        bad_contract = replace(contract_for(cfg), target_regime_id="G_REFERENCE_50_50")
        with self.assertRaises(ContractError):
            self.evaluator.evaluate(truth, result, bad_contract, tolerance=0.10, manifest=manifest)


    def test_assignment_mechanism_probabilities_and_hashes_are_recorded(self):
        worlds = self.worlds()
        ordinary_manifest, _, _ = self.generator.generate(worlds["R0_FOCAL_POSITIVE"])
        support_manifest, _, _ = self.generator.generate(worlds["R0_SUPPORT_FAILURE"])
        self.assertEqual(ordinary_manifest.g_assignment_probability_by_stratum,
                         (("LOW", 0.5), ("HIGH", 0.5)))
        self.assertEqual(support_manifest.g_assignment_probability_by_stratum,
                         (("LOW", 0.5), ("HIGH", 0.0)))
        self.assertTrue(ordinary_manifest.g_assignment_vector_hash)
        self.assertTrue(ordinary_manifest.z_assignment_vector_hash)
        self.assertTrue(ordinary_manifest.g_assignment_mechanism_hash)

    def test_repeated_assignment_average_targets_mechanism_marginal_truth(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        runs = []
        for replicate in range(12):
            rep_cfg = replace(cfg, world_seed=8181, z_assignment_seed=300+replicate,
                              g_assignment_seed=900+replicate, replicate_id=f"r{replicate}")
            manifest, truth, candidate = self.generator.generate(rep_cfg)
            sealed = self.sealer.seal(candidate)
            contract = contract_for(rep_cfg)
            result = self.analyzer.analyze(sealed, contract)
            self.assertEqual(result.package_status, "IDENTIFIED")
            runs.append((truth, result, contract, manifest))
        aggregate = self.evaluator.evaluate_repeated_assignment(runs, tolerance=0.12)
        self.assertEqual(aggregate.replicate_count, 12)
        self.assertIsNotNone(aggregate.marginal_abs_error)
        self.assertTrue(aggregate.marginal_recovered)

    def test_sealer_rejects_generator_truth_metadata(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        _, _, candidate = self.generator.generate(cfg)
        rows = [dict(row) for row in candidate.rows]
        rows[0]["potential_outcome_truth"] = 0.5
        from dataclasses import replace
        with self.assertRaises(FirewallError):
            self.sealer.seal(replace(candidate, rows=tuple(rows)))

    def test_transportability_cannot_be_inferred_from_absent_direct_path(self):
        cfg = self.worlds()["R0_SUPPORT_FAILURE"]
        invalid = replace(contract_for(cfg), z_effect_invariant_across_g=True,
                          transportability_id=None, transportability_version=None,
                          transportability_scope=None,
                          transportability_evidence_status="NOT_ESTABLISHED")
        _, _, candidate = self.generator.generate(cfg)
        sealed = self.sealer.seal(candidate)
        with self.assertRaises(ContractError):
            self.analyzer.analyze(sealed, invalid)

    def test_evaluator_rejects_assignment_mechanism_hash_mismatch(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        manifest, truth, _, result, _ = self.execute_world(cfg)
        wrong = replace(contract_for(cfg), g_assignment_mechanism_hash="0"*64)
        with self.assertRaises(ContractError):
            self.evaluator.evaluate(truth, result, wrong, tolerance=0.10, manifest=manifest)


    def test_evaluator_rejects_run_and_estimand_mismatch(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        manifest, truth, _, result, _ = self.execute_world(cfg)
        with self.assertRaises(ContractError):
            self.evaluator.evaluate(replace(truth, run_id="other-run"), result,
                                    contract_for(cfg), tolerance=0.10, manifest=manifest)
        wrong_estimand = replace(contract_for(cfg), estimand_id="OTHER_ESTIMAND")
        with self.assertRaises(ContractError):
            self.evaluator.evaluate(truth, result, wrong_estimand, tolerance=0.10, manifest=manifest)

    def test_evaluator_rejects_transportability_scope_mismatch(self):
        cfg = self.worlds()["R0_SUPPORT_FAILURE"]
        manifest, truth, _, result, _ = self.execute_world(cfg)
        wrong_scope = replace(contract_for(cfg), transportability_scope="LOW")
        with self.assertRaises(ContractError):
            self.evaluator.evaluate(truth, result, wrong_scope, tolerance=0.10, manifest=manifest)

    def test_version_inconsistency_causes_indeterminate_adjudication(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        _, _, candidate = self.generator.generate(cfg)
        sealed = self.sealer.seal(candidate)
        inconsistent = replace(contract_for(cfg), version_consistency=False)
        result = self.analyzer.analyze(sealed, inconsistent)
        self.assertEqual(result.package_status, "INDETERMINATE")
        self.assertEqual(result.g_assignment_status, "INDETERMINATE")


    def test_evaluator_rejects_outcome_and_z_mechanism_mismatch(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        manifest, truth, _, result, _ = self.execute_world(cfg)
        wrong_outcome = replace(contract_for(cfg), outcome_version="002")
        with self.assertRaises(ContractError):
            self.evaluator.evaluate(truth, result, wrong_outcome, tolerance=0.10, manifest=manifest)
        wrong_z = replace(contract_for(cfg), z_assignment_mechanism_hash="f"*64)
        with self.assertRaises(ContractError):
            self.evaluator.evaluate(truth, result, wrong_z, tolerance=0.10, manifest=manifest)


    def test_evaluator_rejects_manifest_scenario_world_and_vector_mismatch(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        manifest, truth, _, result, _ = self.execute_world(cfg)
        for altered in (replace(manifest, scenario_id="OTHER_SCENARIO"),
                        replace(manifest, world_id="OTHER_WORLD"),
                        replace(manifest, z_assignment_vector_hash="0"*64),
                        replace(manifest, g_assignment_mechanism_version="999")):
            with self.assertRaises(ContractError):
                self.evaluator.evaluate(truth, result, contract_for(cfg), tolerance=0.10, manifest=altered)

    def test_evaluator_rejects_estimand_and_mechanism_version_mismatch(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        manifest, truth, _, result, _ = self.execute_world(cfg)
        for altered in (replace(contract_for(cfg), estimand_version="999"),
                        replace(contract_for(cfg), g_assignment_mechanism_version="999"),
                        replace(contract_for(cfg), z_assignment_mechanism_id="OTHER_Z"),
                        replace(contract_for(cfg), reference_regime_version="999")):
            with self.assertRaises(ContractError):
                self.evaluator.evaluate(truth, result, altered, tolerance=0.10, manifest=manifest)

    def test_transportability_scope_and_outcome_are_checked_against_truth(self):
        cfg = self.worlds()["R0_SUPPORT_FAILURE"]
        manifest, truth, _, result, _ = self.execute_world(cfg)
        altered_truth = replace(truth, transportability_scope_truth="LOW")
        with self.assertRaises(ContractError):
            self.evaluator.evaluate(altered_truth, result, contract_for(cfg), tolerance=0.10, manifest=manifest)
        altered_contract = replace(contract_for(cfg), transportability_outcome_id="OTHER_OUTCOME")
        with self.assertRaises(ContractError):
            self.evaluator.evaluate(truth, result, altered_contract, tolerance=0.10, manifest=manifest)

if __name__ == "__main__":
    unittest.main()
