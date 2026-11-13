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
from vcont_benchmark_protocol import (
    ProtocolError, MonteCarloBenchmarkDesign, build_scenario_estimand_matrix,
    scenario_matrix_fingerprint, SCENARIO_IDS,
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


    def test_typed_assignment_index_is_sealed_and_propagated(self):
        cfg = replace(self.worlds()["R0_FOCAL_POSITIVE"], assignment_role="RUN",
                      assignment_index=-1, replicate_id="gate157-designated-run")
        manifest, truth, sealed, result, _ = self.execute_world(cfg)
        self.assertEqual(manifest.assignment_index, -1)
        self.assertEqual(truth.assignment_index, -1)
        self.assertEqual(sealed.manifest["provenance"]["assignment_index"], -1)
        self.assertEqual(result.assignment_index, -1)

    def test_monte_carlo_rejects_incomplete_declared_r_index_set(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        outer_runs = {}
        for m in range(2):
            outer_id = f"gate157-outer-{m}"
            rows = []
            for role, index in (("RUN", -1), ("REPEATED_ASSIGNMENT", 0),
                                ("REPEATED_ASSIGNMENT", 1)):
                rep_cfg = replace(
                    cfg, outer_replicate_id=outer_id, assignment_role=role,
                    assignment_index=index, replicate_id=f"{outer_id}-{role}-{index}",
                    world_seed=9000 + m, z_assignment_seed=10000 + 10*m + index + 2,
                    g_assignment_seed=11000 + 10*m + index + 2,
                )
                manifest, truth, candidate = self.generator.generate(rep_cfg)
                contract = contract_for(rep_cfg)
                result = self.analyzer.analyze(self.sealer.seal(candidate), contract)
                rows.append((truth, result, contract, manifest))
            outer_runs[outer_id] = rows
        with self.assertRaises(ContractError):
            self.evaluator.evaluate_monte_carlo(
                outer_runs, tolerance=0.10, target_mcse_by_metric={},
                expected_repeated_assignments=3)

    def test_benchmark_aggregator_returns_reconstructable_52_pair_ledger(self):
        scenarios = benchmark_scenarios(n_units=16, n_intervals=20)
        versions = tuple((cfg.scenario_id, cfg.version) for cfg in scenarios)
        version_map = dict(versions)
        matrix = build_scenario_estimand_matrix(version_map)
        targets = []
        for spec in matrix:
            temporal = (spec.run_evaluation_class
                        if spec.key.estimand_id in ("ITT_Z_RUN_CONDITIONAL_VCONT", "ITT_G_Z0_VCONT")
                        else spec.repeated_evaluation_class)
            if temporal == "EVALUABLE":
                for metric in ("bias", "mae", "rmse"):
                    targets.append((spec.key.scenario_id, spec.key.scenario_version,
                                    spec.key.estimand_id, spec.key.estimand_version, metric, 10.0))
        design = MonteCarloBenchmarkDesign(
            scenario_versions=versions, n_units=16, outer_replicates=2,
            repeated_assignments=2, matrix_fingerprint=scenario_matrix_fingerprint(matrix),
            metric_targets=tuple(targets), seed_bank_label="DETERMINISTIC_TEST_FIXTURE",
            seed_bank_fingerprint="a"*64, executable_commit="c"*40,
            configuration_fingerprint="b"*64)
        scenario_outer_runs = {}
        for cfg in scenarios:
            scenario_outer_runs[cfg.scenario_id] = {}
            for m in range(2):
                outer_id = f"{cfg.scenario_id}-M{m}"
                rows = []
                for role, index in (("RUN", -1), ("REPEATED_ASSIGNMENT", 0),
                                    ("REPEATED_ASSIGNMENT", 1)):
                    rep_cfg = replace(
                        cfg, outer_replicate_id=outer_id, assignment_role=role,
                        assignment_index=index, world_seed=30000 + m,
                        z_assignment_seed=40000 + m*10 + index + 2,
                        g_assignment_seed=50000 + m*10 + index + 2,
                        replicate_id=f"{outer_id}-{role}-{index}")
                    manifest, truth, candidate = self.generator.generate(rep_cfg)
                    contract = contract_for(rep_cfg)
                    result = self.analyzer.analyze(self.sealer.seal(candidate), contract)
                    rows.append((truth, result, contract, manifest))
                scenario_outer_runs[cfg.scenario_id][outer_id] = rows
        report = self.evaluator.evaluate_monte_carlo_benchmark(
            scenario_outer_runs, design, tolerance=0.20, matrix=matrix)
        self.assertEqual(report["coverage"], {
            "required_pairs": 52, "observed_pairs": 52, "scenario_count": 13})
        self.assertEqual(len(report["pair_ledger"]), 52)
        self.assertEqual(len({row["key"] for row in report["pair_ledger"]}), 52)
        self.assertEqual(len(report["temporal_manifest"]), 13 * 2 * 3)
        self.assertEqual(len(report["report_fingerprint"]), 64)
        self.assertTrue(all(row["observed_M"] == 2 for row in report["pair_ledger"]))
        status_only = next(row for row in report["pair_ledger"]
                           if row["key"][0] == "R0_MEASUREMENT_ADVERSE"
                           and row["key"][2] == "ITT_Z_RUN_CONDITIONAL_VCONT")
        self.assertEqual(status_only["evaluation_class"], "STATUS_ONLY")
        self.assertEqual(status_only["numeric_denominator"], 0)
        self.assertIsNone(status_only["metrics"]["mae"])

    def test_monte_carlo_classifies_truth_missing_and_invalid_output_separately(self):
        from vcont_integrated_harness import _hash

        scenarios = benchmark_scenarios(n_units=16, n_intervals=20)
        versions = tuple((cfg.scenario_id, cfg.version) for cfg in scenarios)
        matrix = build_scenario_estimand_matrix(dict(versions))
        targets = []
        for spec in matrix:
            temporal = (spec.run_evaluation_class
                        if spec.key.estimand_id in ("ITT_Z_RUN_CONDITIONAL_VCONT", "ITT_G_Z0_VCONT")
                        else spec.repeated_evaluation_class)
            if temporal == "EVALUABLE":
                for metric in ("bias", "mae", "rmse"):
                    targets.append((spec.key.scenario_id, spec.key.scenario_version,
                                    spec.key.estimand_id, spec.key.estimand_version, metric, 10.0))
        design = MonteCarloBenchmarkDesign(
            scenario_versions=versions, n_units=16, outer_replicates=2,
            repeated_assignments=2, matrix_fingerprint=scenario_matrix_fingerprint(matrix),
            metric_targets=tuple(targets), seed_bank_label="DETERMINISTIC_TEST_FIXTURE",
            seed_bank_fingerprint="a"*64, executable_commit="c"*40,
            configuration_fingerprint="b"*64)

        scenario_outer_runs = {}
        target_scenario = "R0_FOCAL_POSITIVE"
        for cfg in scenarios:
            scenario_outer_runs[cfg.scenario_id] = {}
            for m in range(2):
                outer_id = f"{cfg.scenario_id}-classification-M{m}"
                rows = []
                for role, index in (("RUN", -1), ("REPEATED_ASSIGNMENT", 0),
                                    ("REPEATED_ASSIGNMENT", 1)):
                    rep_cfg = replace(
                        cfg, outer_replicate_id=outer_id, assignment_role=role,
                        assignment_index=index, world_seed=61000 + m,
                        z_assignment_seed=62000 + m*10 + index + 2,
                        g_assignment_seed=63000 + m*10 + index + 2,
                        replicate_id=f"{outer_id}-{role}-{index}")
                    manifest, truth, candidate = self.generator.generate(rep_cfg)
                    contract = contract_for(rep_cfg)
                    result = self.analyzer.analyze(self.sealer.seal(candidate), contract)
                    if cfg.scenario_id == target_scenario and role == "RUN":
                        if m == 0:
                            truth = replace(truth, itt_z_run_truth=None)
                        else:
                            result = replace(result, package_itt=None)
                            output_payload = {
                                "run_id": result.run_id, "estimand_id": result.estimand_id,
                                "package_status": result.package_status,
                                "g_assignment_status": result.g_assignment_status,
                                "package_itt": result.package_itt,
                                "g_assignment_effect": result.g_assignment_effect,
                                "first_stage_delta_t_acc": result.first_stage_delta_t_acc,
                                "package_se": result.package_se, "g_assignment_se": result.g_assignment_se,
                                "reasons": list(result.abstention_reasons),
                                "input_sha256": result.input_sha256,
                                "target_regime_id": result.target_regime_id,
                                "target_regime_version": result.target_regime_version,
                                "outcome_id": result.outcome_id, "outcome_version": result.outcome_version,
                                "reference_regime_status": result.reference_regime_status,
                                "reference_regime_id": result.reference_regime_id,
                                "reference_regime_version": result.reference_regime_version,
                                "g_assignment_mechanism_hash": result.g_assignment_mechanism_hash,
                                "z_assignment_mechanism_hash": result.z_assignment_mechanism_hash,
                                "transportability_id": result.transportability_id,
                                "transportability_version": result.transportability_version,
                                "transportability_scope": result.transportability_scope,
                                "transportability_evidence_status": result.transportability_evidence_status,
                                "estimand_version": result.estimand_version,
                                "g_assignment_mechanism_id": result.g_assignment_mechanism_id,
                                "g_assignment_mechanism_version": result.g_assignment_mechanism_version,
                                "z_assignment_mechanism_id": result.z_assignment_mechanism_id,
                                "z_assignment_mechanism_version": result.z_assignment_mechanism_version,
                                "provenance_sha256": result.provenance_sha256,
                                "transportability_outcome_id": result.transportability_outcome_id,
                                "transportability_basis": result.transportability_basis,
                                "reference_regime_itt": result.reference_regime_itt,
                                "run_conditional_estimand_id": result.run_conditional_estimand_id,
                                "run_conditional_estimand_version": result.run_conditional_estimand_version,
                                "reference_regime_estimand_id": result.reference_regime_estimand_id,
                                "reference_regime_estimand_version": result.reference_regime_estimand_version,
                                "g_assignment_estimand_id": result.g_assignment_estimand_id,
                                "g_assignment_estimand_version": result.g_assignment_estimand_version,
                                "outer_replicate_id": result.outer_replicate_id,
                                "assignment_role": result.assignment_role,
                                "assignment_index": result.assignment_index,
                            }
                            result = replace(result, output_sha256=_hash(output_payload))
                    rows.append((truth, result, contract, manifest))
                scenario_outer_runs[cfg.scenario_id][outer_id] = rows

        report = self.evaluator.evaluate_monte_carlo_benchmark(
            scenario_outer_runs, design, tolerance=0.20, matrix=matrix)
        pair = next(row for row in report["pair_ledger"]
                    if row["key"][0] == target_scenario
                    and row["key"][2] == "ITT_Z_RUN_CONDITIONAL_VCONT")
        states = {item["contribution_state"] for item in pair["contributions"]}
        self.assertEqual(states, {"TRUTH_MISSING", "INVALID_OUTPUT"})
        self.assertEqual(pair["truth_missing_count"], 1)
        self.assertEqual(pair["invalid_output_count"], 1)
        self.assertEqual(pair["missing_contribution_count"], 0)
        self.assertEqual(pair["status_denominator"], 2)
        self.assertEqual(pair["numeric_denominator"], 0)
        self.assertEqual(pair["abstention_count"], 0)
        self.assertEqual(pair["observed_M"], pair["expected_M"])

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
        self.assertEqual(result.run_conditional_estimand_id, "ITT_Z_RUN_CONDITIONAL_VCONT")
        self.assertEqual(result.reference_regime_estimand_id, "ITT_Z_REFERENCE_REGIME_VCONT")
        self.assertEqual(result.g_assignment_estimand_id, "ITT_G_Z0_VCONT")
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


    def test_outer_replicate_identity_propagates_and_separates_worlds(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        common = dict(world_seed=991, outer_replicate_id="outer-000001")
        run_cfg = replace(cfg, **common, assignment_role="RUN", assignment_index=-1,
                          z_assignment_seed=11, g_assignment_seed=21, replicate_id="designated-run")
        repeat_cfg = replace(cfg, **common, assignment_role="REPEATED_ASSIGNMENT",
                             z_assignment_seed=12, g_assignment_seed=22, replicate_id="r0")
        other_world_cfg = replace(cfg, world_seed=992, outer_replicate_id="outer-000002",
                                  assignment_role="RUN", assignment_index=-1, z_assignment_seed=13,
                                  g_assignment_seed=23, replicate_id="designated-run-2")
        run_manifest, run_truth, run_candidate = self.generator.generate(run_cfg)
        repeat_manifest, repeat_truth, _ = self.generator.generate(repeat_cfg)
        other_manifest, _, _ = self.generator.generate(other_world_cfg)
        self.assertEqual(run_manifest.world_id, repeat_manifest.world_id)
        self.assertNotEqual(run_manifest.world_id, other_manifest.world_id)
        self.assertEqual(run_truth.outer_replicate_id, "outer-000001")
        self.assertEqual(repeat_truth.assignment_role, "REPEATED_ASSIGNMENT")
        sealed = self.sealer.seal(run_candidate)
        result = self.analyzer.analyze(sealed, contract_for(run_cfg))
        report = self.evaluator.evaluate(run_truth, result, contract_for(run_cfg),
                                         tolerance=0.10, manifest=run_manifest)
        self.assertEqual(result.outer_replicate_id, run_manifest.outer_replicate_id)
        self.assertEqual(result.assignment_role, "RUN")
        self.assertIsNotNone(report)

    def test_evaluator_rejects_outer_identity_mismatch(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        manifest, truth, _, result, _ = self.execute_world(cfg)
        with self.assertRaises(ContractError):
            self.evaluator.evaluate(replace(truth, outer_replicate_id="outer-forged"),
                                    result, contract_for(cfg), tolerance=0.10, manifest=manifest)
        with self.assertRaises((ContractError, FirewallError)):
            self.evaluator.evaluate(truth, replace(result, assignment_role="RUN"),
                                    contract_for(cfg), tolerance=0.10, manifest=manifest)


    def test_monte_carlo_aggregates_one_run_and_r_within_each_independent_world(self):
        cfg = replace(self.worlds()["R0_FOCAL_POSITIVE"], n_units=16)
        outer_runs = {}
        for m in range(2):
            outer_id = f"outer-{m:06d}"
            world_seed = 4000 + m
            rows = []
            run_cfg = replace(cfg, outer_replicate_id=outer_id, assignment_role="RUN", assignment_index=-1,
                              world_seed=world_seed, z_assignment_seed=5000+m,
                              g_assignment_seed=6000+m, replicate_id=f"{outer_id}-RUN")
            manifest, truth, candidate = self.generator.generate(run_cfg)
            sealed = self.sealer.seal(candidate)
            contract = contract_for(run_cfg)
            result = self.analyzer.analyze(sealed, contract)
            rows = [(truth, result, contract, manifest)]
            for r in range(2):
                rep_cfg = replace(cfg, outer_replicate_id=outer_id,
                                  assignment_role="REPEATED_ASSIGNMENT", assignment_index=r,
                                  world_seed=world_seed, z_assignment_seed=7000+m*10+r,
                                  g_assignment_seed=8000+m*10+r, replicate_id=f"{outer_id}-R{r}")
                rep_manifest, rep_truth, rep_candidate = self.generator.generate(rep_cfg)
                rep_result = self.analyzer.analyze(self.sealer.seal(rep_candidate), contract_for(rep_cfg))
                rows.append((rep_truth, rep_result, contract_for(rep_cfg), rep_manifest))
            outer_runs[outer_id] = rows
        summary = self.evaluator.evaluate_monte_carlo(
            outer_runs, tolerance=0.20,
            target_mcse_by_metric={
                "run_conditional.bias": 1.0, "run_conditional.mae": 1.0, "run_conditional.rmse": 1.0,
                "g_assignment_z0.bias": 1.0, "g_assignment_z0.mae": 1.0, "g_assignment_z0.rmse": 1.0,
                "mechanism_marginal.bias": 1.0, "mechanism_marginal.mae": 1.0, "mechanism_marginal.rmse": 1.0,
                "reference_regime.bias": 1.0, "reference_regime.mae": 1.0, "reference_regime.rmse": 1.0,
            })
        self.assertEqual(summary["outer_replicate_count"], 2)
        self.assertEqual(summary["coverage"]["run_conditional_numeric"], 2)
        self.assertIsNotNone(summary["run_conditional"]["mae"])
        self.assertIsNotNone(summary["mechanism_marginal"]["mae"])

    def test_monte_carlo_rejects_shared_world_identity_across_outer_replicates(self):
        cfg = replace(self.worlds()["R0_FOCAL_POSITIVE"], n_units=16)
        outer_runs = {}
        for m in range(2):
            outer_id = f"outer-shared-{m}"
            run_cfg = replace(cfg, outer_replicate_id=outer_id, assignment_role="RUN", assignment_index=-1,
                              world_seed=9000, z_assignment_seed=9100+m,
                              g_assignment_seed=9200+m, replicate_id=f"{outer_id}-RUN")
            manifest, truth, candidate = self.generator.generate(run_cfg)
            contract = contract_for(run_cfg)
            result = self.analyzer.analyze(self.sealer.seal(candidate), contract)
            outer_runs[outer_id] = [(truth, result, contract, manifest)]
        with self.assertRaises(ContractError):
            self.evaluator.evaluate_monte_carlo(
                outer_runs, tolerance=0.20,
                target_mcse_by_metric={
                    "run_conditional.bias": 1.0, "run_conditional.mae": 1.0, "run_conditional.rmse": 1.0,
                    "g_assignment_z0.bias": 1.0, "g_assignment_z0.mae": 1.0, "g_assignment_z0.rmse": 1.0,
                    "mechanism_marginal.bias": 1.0, "mechanism_marginal.mae": 1.0, "mechanism_marginal.rmse": 1.0,
                    "reference_regime.bias": 1.0, "reference_regime.mae": 1.0, "reference_regime.rmse": 1.0,
                })

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
        _, _, candidate = self.generator.generate(cfg)
        with self.assertRaises(ContractError):
            self.analyzer.analyze(self.sealer.seal(candidate), wrong)
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
        altered_basis = replace(contract_for(cfg), transportability_basis="unsupported alternate basis")
        with self.assertRaises(ContractError):
            self.evaluator.evaluate(truth, result, altered_basis, tolerance=0.10, manifest=manifest)


    def test_sealer_rejects_provenance_truth_injection_and_assignment_hash_mismatch(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        _, _, candidate = self.generator.generate(cfg)
        injected = dict(candidate.provenance)
        injected["potential_outcome_truth"] = "forbidden"
        with self.assertRaises(FirewallError):
            self.sealer.seal(replace(candidate, provenance=injected))
        altered = dict(candidate.provenance)
        altered["g_assignment_vector_hash"] = "0"*64
        with self.assertRaises(ContractError):
            self.sealer.seal(replace(candidate, provenance=altered))

    def test_realized_arm_support_shortfall_abstains_without_exception(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        _, _, candidate = self.generator.generate(cfg)
        rows = [dict(row) for row in candidate.rows]
        z0_ids = [i for i, row in enumerate(rows) if row["assignment_z"] == 0]
        for i in z0_ids:
            rows[i]["assignment_g"] = 0
        from vcont_integrated_harness import _hash
        provenance = dict(candidate.provenance)
        provenance["g_assignment_vector_hash"] = _hash([row["assignment_g"] for row in rows])
        sparse = replace(candidate, rows=tuple(rows), provenance=provenance)
        sealed = self.sealer.seal(sparse)
        result = self.analyzer.analyze(sealed, contract_for(cfg))
        self.assertEqual(result.g_assignment_status, "INDETERMINATE")
        self.assertIn("G_REALIZED_ARM_SUPPORT_INSUFFICIENT", result.abstention_reasons)


    def test_evaluator_rejects_remaining_transportability_and_identity_mismatches(self):
        cfg = self.worlds()["R0_SUPPORT_FAILURE"]
        manifest, truth, _, result, _ = self.execute_world(cfg)
        bad_contracts = (
            replace(contract_for(cfg), transportability_id="OTHER_RESTRICTION"),
            replace(contract_for(cfg), transportability_version="999"),
            replace(contract_for(cfg), outcome_id="OTHER_OUTCOME"),
            replace(contract_for(cfg), z_assignment_mechanism_version="999"),
            replace(contract_for(cfg), reference_regime_id="OTHER_REGIME"),
        )
        for bad_contract in bad_contracts:
            with self.subTest(contract=bad_contract):
                with self.assertRaises(ContractError):
                    self.evaluator.evaluate(truth, result, bad_contract, tolerance=0.10, manifest=manifest)
        with self.assertRaises(ContractError):
            self.evaluator.evaluate(truth, result, contract_for(cfg), tolerance=0.10,
                                    manifest=replace(manifest, version="999"))

    def test_evaluator_adjudicates_version_inconsistency_as_expected_abstention(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        manifest, truth, candidate = self.generator.generate(cfg)
        sealed = self.sealer.seal(candidate)
        inconsistent = replace(contract_for(cfg), version_consistency=False)
        result = self.analyzer.analyze(sealed, inconsistent)
        report = self.evaluator.evaluate(truth, result, inconsistent,
                                         tolerance=0.10, manifest=manifest)
        self.assertEqual(result.package_status, "INDETERMINATE")
        self.assertEqual(result.g_assignment_status, "INDETERMINATE")
        self.assertEqual(result.reference_regime_status, "INDETERMINATE")
        self.assertTrue(report.expected_abstention_respected)
        self.assertTrue(report.reference_regime_status_correct)
        self.assertNotIn("REFERENCE_REGIME_IDENTIFICATION_STATUS_MISMATCH", report.notes)

    def test_assignment_streams_are_independently_reproducible(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        base = replace(cfg, world_seed=771, z_assignment_seed=881,
                       g_assignment_seed=991, replicate_id="seed-check")
        same = replace(base, replicate_id="same-seeds")
        z_changed = replace(base, z_assignment_seed=882, replicate_id="z-changed")
        g_changed = replace(base, g_assignment_seed=992, replicate_id="g-changed")
        m0, t0, e0 = self.generator.generate(base)
        ms, ts, es = self.generator.generate(same)
        mz, tz, ez = self.generator.generate(z_changed)
        mg, tg, eg = self.generator.generate(g_changed)
        z0 = [row["assignment_z"] for row in e0.rows]
        g0 = [row["assignment_g"] for row in e0.rows]
        self.assertEqual(z0, [row["assignment_z"] for row in es.rows])
        self.assertEqual(g0, [row["assignment_g"] for row in es.rows])
        self.assertEqual(g0, [row["assignment_g"] for row in ez.rows])
        self.assertEqual(z0, [row["assignment_z"] for row in eg.rows])
        self.assertNotEqual(z0, [row["assignment_z"] for row in ez.rows])
        self.assertNotEqual(g0, [row["assignment_g"] for row in eg.rows])
        for truth in (ts, tz, tg):
            self.assertEqual(t0.potential_v, truth.potential_v)
            self.assertEqual(t0.potential_delta_t_acc, truth.potential_delta_t_acc)
        self.assertEqual(m0.world_id, ms.world_id)
        self.assertEqual(m0.world_id, mz.world_id)
        self.assertEqual(m0.world_id, mg.world_id)


    def test_repeated_assignment_rejects_z_mechanism_identity_version_or_hash_mismatch(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        runs = []
        for replicate in range(2):
            rep_cfg = replace(cfg, world_seed=8181, z_assignment_seed=500+replicate,
                              g_assignment_seed=700+replicate, replicate_id=f"z-check-{replicate}")
            manifest, truth, candidate = self.generator.generate(rep_cfg)
            contract = contract_for(rep_cfg)
            result = self.analyzer.analyze(self.sealer.seal(candidate), contract)
            runs.append((truth, result, contract, manifest))
        altered_manifest = replace(runs[1][3], z_assignment_mechanism_version="999")
        bad_runs = [runs[0], (runs[1][0], runs[1][1], runs[1][2], altered_manifest)]
        with self.assertRaises(ContractError):
            self.evaluator.evaluate_repeated_assignment(bad_runs, tolerance=0.10)

    def test_repeated_assignment_reports_reference_and_mechanism_marginals_separately(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        runs = []
        for replicate in range(12):
            rep_cfg = replace(cfg, world_seed=1818, z_assignment_seed=500+replicate,
                              g_assignment_seed=1500+replicate, replicate_id=f"ref-{replicate}")
            manifest, truth, candidate = self.generator.generate(rep_cfg)
            sealed = self.sealer.seal(candidate)
            contract = contract_for(rep_cfg)
            result = self.analyzer.analyze(sealed, contract)
            runs.append((truth, result, contract, manifest))
        aggregate = self.evaluator.evaluate_repeated_assignment(runs, tolerance=0.12)
        self.assertIsNotNone(aggregate.mechanism_truth)
        self.assertIsNotNone(aggregate.reference_truth)
        self.assertEqual(aggregate.reference_identification_status, "IDENTIFIED")
        self.assertIsNotNone(aggregate.reference_estimate_mean)
        self.assertIsNotNone(aggregate.reference_abs_error)
        self.assertEqual(aggregate.mechanism_marginal_estimand_id, "ITT_Z_MECHANISM_MARGINAL_VCONT")
        self.assertEqual(aggregate.reference_regime_estimand_id, "ITT_Z_REFERENCE_REGIME_VCONT")

    def test_evaluator_rejects_assignment_estimand_version_mismatch(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        manifest, truth, sealed, result, _ = self.execute_world(cfg)
        bad_contract = replace(contract_for(cfg), run_conditional_estimand_version="999")
        with self.assertRaises(ContractError):
            self.evaluator.evaluate(truth, result, bad_contract, tolerance=0.10, manifest=manifest)

    def test_repeated_assignment_does_not_score_unidentified_reference_target(self):
        cfg = self.worlds()["R2_SUPPORT_FAILURE_ZG_INTERACTION"]
        runs = []
        for replicate in range(3):
            rep_cfg = replace(cfg, world_seed=2828, z_assignment_seed=700+replicate,
                              g_assignment_seed=1700+replicate, replicate_id=f"ni-{replicate}")
            manifest, truth, candidate = self.generator.generate(rep_cfg)
            sealed = self.sealer.seal(candidate)
            contract = contract_for(rep_cfg)
            result = self.analyzer.analyze(sealed, contract)
            runs.append((truth, result, contract, manifest))
        aggregate = self.evaluator.evaluate_repeated_assignment(runs, tolerance=0.12)
        self.assertEqual(aggregate.reference_identification_status, "NOT_IDENTIFIED")
        self.assertIsNone(aggregate.reference_estimate_mean)
        self.assertIsNone(aggregate.reference_abs_error)
        self.assertIsNone(aggregate.reference_recovered)

    def test_matrix_adapter_uses_run_and_repeated_assignment_levels(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        runs = []
        for replicate in range(3):
            rep_cfg = replace(cfg, world_seed=4242, z_assignment_seed=5100+replicate,
                              g_assignment_seed=6100+replicate, replicate_id=f"matrix-{replicate}")
            manifest, truth, candidate = self.generator.generate(rep_cfg)
            result = self.analyzer.analyze(self.sealer.seal(candidate), contract_for(rep_cfg))
            runs.append((truth, result, contract_for(rep_cfg), manifest))
        report = self.evaluator.evaluate_matrix_pairs(runs, tolerance=0.10)
        records = report["pair_records"]
        self.assertEqual(len({record.key for record in records}), 4)
        self.assertEqual({record.outer_replicate_id for record in records}, {"outer-000000"})
        self.assertTrue(all(record.assignment_role == "REPEATED_ASSIGNMENT" for record in records))
        run_records = [record for record in records if record.evaluation_level == "RUN"]
        repeated_records = [record for record in records if record.evaluation_level == "REPEATED_ASSIGNMENT"]
        self.assertEqual(len(run_records), 3 * 3)
        self.assertEqual(len(repeated_records), 2)
        self.assertNotIn("ITT_Z_MECHANISM_MARGINAL_VCONT",
                         {record.key.estimand_id for record in run_records})
        self.assertIn("ITT_Z_MECHANISM_MARGINAL_VCONT",
                      {record.key.estimand_id for record in repeated_records})
        self.assertIn("ITT_Z_REFERENCE_REGIME_VCONT",
                      {record.key.estimand_id for record in run_records})
        reference_run_records = [record for record in run_records
                                 if record.key.estimand_id == "ITT_Z_REFERENCE_REGIME_VCONT"]
        self.assertTrue(all(record.evaluation_class == "STATUS_ONLY"
                            and record.analyzer_output is None and record.dgp_truth is None
                            for record in reference_run_records))
        self.assertIn("ITT_Z_REFERENCE_REGIME_VCONT",
                      {record.key.estimand_id for record in repeated_records})

    def test_matrix_adapter_rejects_scenario_version_mismatch(self):
        cfg = self.worlds()["R0_FOCAL_POSITIVE"]
        manifest, truth, candidate = self.generator.generate(cfg)
        result = self.analyzer.analyze(self.sealer.seal(candidate), contract_for(cfg))
        altered_manifest = replace(manifest, version="OTHER-DGP-VERSION")
        with self.assertRaises(ProtocolError):
            self.evaluator.evaluate_matrix_pairs(
                [(truth, result, contract_for(cfg), altered_manifest)], tolerance=0.10)

    def test_matrix_adapter_preserves_nonidentified_reference_as_status(self):
        cfg = self.worlds()["R2_SUPPORT_FAILURE_ZG_INTERACTION"]
        runs = []
        for replicate in range(2):
            rep_cfg = replace(cfg, world_seed=8282, z_assignment_seed=7200+replicate,
                              g_assignment_seed=8200+replicate, replicate_id=f"matrix-ni-{replicate}")
            manifest, truth, candidate = self.generator.generate(rep_cfg)
            contract = contract_for(rep_cfg)
            result = self.analyzer.analyze(self.sealer.seal(candidate), contract)
            runs.append((truth, result, contract, manifest))
        report = self.evaluator.evaluate_matrix_pairs(runs, tolerance=0.10)
        reference = [record for record in report["pair_records"]
                     if record.key.estimand_id == "ITT_Z_REFERENCE_REGIME_VCONT"]
        self.assertEqual(len(reference), 3)
        self.assertTrue(all(record.identification_status == "NOT_IDENTIFIED" and record.abstained
                            for record in reference))
        self.assertTrue(all(record.analyzer_output is None for record in reference))

if __name__ == "__main__":
    unittest.main()
