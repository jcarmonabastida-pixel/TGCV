from __future__ import annotations

import hashlib
import json
import unittest
from dataclasses import replace
from decimal import Decimal
from types import SimpleNamespace

from theta_a_calibration_protocol import (
    ThetaACalibrationDesign,
    ThetaACalibrationDGPProfile,
    ThetaACalibrationError,
    ThetaACalibrationScenario,
    OuterWorldSamplingContract,
    THETA_A_METRIC_REGISTRY,
    ThetaAReplicateRecord,
    build_theta_a_seed_bank,
    build_theta_a_candidate_scenario_roster,
    s3_seeds_by_unit,
    run_theta_a_calibration_replicates,
    theta_a_pipeline_inference_options,
    summarize_theta_a_calibration,
    validate_theta_a_seed_banks,
    _validate_interval_s3_seed_provenance,
    _validate_truth_assignment_population_bindings,
)


class ThetaACalibrationProtocolTests(unittest.TestCase):
    def _design(self, scenario=None):
        scenario = scenario or ThetaACalibrationScenario(
            scenario_id="THETA_A_IDEAL", scenario_version="1.0",
            world_version="world-v1", dgp_id="C10S-THETA-A", dgp_version="1.0",
            roster_version="1.0", unit_id_prefix="unit",
            expected_identification="IDENTIFIED", unit_independence_certified=True,
            independence_basis="unit-level potential histories and two-stage randomization are generated independently by unit",
        )
        return ThetaACalibrationDesign(
            scenario_specs=(scenario,),
            n_grid=(4,),
            outer_worlds_m=2,
            assignment_replicates_r=2,
            confidence_level=0.95,
            namespace="theta-a-calibration-test-v1",
            point_recovery_tolerance=0.05,
            metric_targets=(
                ("THETA_A_IDEAL", "1.0", 4, "interval_coverage", 0.01),
                ("THETA_A_IDEAL", "1.0", 4, "interval_width", 0.01),
            ) if scenario.expected_identification == "IDENTIFIED" else (),
            metric_target_manifest_id="TEST-METRIC-TARGETS" if scenario.expected_identification == "IDENTIFIED" else None,
            metric_target_manifest_version="1.0" if scenario.expected_identification == "IDENTIFIED" else None,
            outer_world_sampling=OuterWorldSamplingContract(
                mode="DECLARED_IID_PSEUDORANDOM",
                contract_id="TEST-OUTER-WORLD-IID",
                contract_version="1.0",
                target_distribution_id="TEST-WORLD-DISTRIBUTION",
                target_distribution_version="1.0",
                world_generator_id="TEST-WORLD-GENERATOR",
                world_generator_version="1.0",
                seed_stream_id="TEST-SEED-STREAM",
                seed_stream_version="1.0",
                independence_basis="independent pseudorandom streams under the declared test-only world distribution",
            ),
        )

    def _record(self, row, expected, observed, point, lower, upper, covered, width, requested_level,
                expected_reason=None, observed_reason=None, unsupported_mass=0.0):
        def fp(value):
            return hashlib.sha256(value.encode("utf-8")).hexdigest()
        return ThetaAReplicateRecord(
            row.scenario_id, row.scenario_version, row.n_units,
            row.outer_world_id, row.assignment_replicate, row.world_id, row.run_id,
            "THETA_A_QX_GA_RCOMMON_VCONT", "1.0", "V_CONT", "1.0",
            expected, observed, 0.2, point, lower, upper, covered, width, requested_level,
            fp("world|" + row.outer_world_id), fp("policy-design"),
            fp(row.randomization_salt), fp(row.run_id + "|evidence"),
            fp(row.run_id + "|analyzer"),
            row.dgp_profile_sha256, fp("target-qx"), fp("source-qx"), None,
            expected_reason, observed_reason, unsupported_mass,
        )

    def test_capture_binding_accepts_source_superset_with_target_standardization(self):
        fp = lambda value: hashlib.sha256(value.encode("utf-8")).hexdigest()
        assignment = SimpleNamespace(
            q_x_sha256=fp("source-qx"),
            g_a0_sha256=fp("source-g0"),
            g_a1_sha256=fp("source-g1"),
            r_common_sha256=fp("source-r"),
        )
        truth = SimpleNamespace(
            q_x_fingerprint=fp("target-qx"),
            g_a0_fingerprint=fp("target-g0"),
            g_a1_fingerprint=fp("target-g1"),
        )
        contract = SimpleNamespace(
            q_x_sha256=fp("target-qx"),
            source_q_x_sha256=fp("source-qx"),
            g_a0_sha256=fp("source-g0"),
            g_a1_sha256=fp("source-g1"),
            target_g_a0_sha256=fp("target-g0"),
            target_g_a1_sha256=fp("target-g1"),
            r_common_sha256=fp("source-r"),
            structural_support_contract=None,
        )
        policy_fingerprint = _validate_truth_assignment_population_bindings(
            truth, assignment, contract,
        )
        self.assertEqual(len(policy_fingerprint), 64)
        self.assertTrue(all(ch in "0123456789abcdef" for ch in policy_fingerprint))

    def test_capture_binding_rejects_truth_on_source_instead_of_target_qx(self):
        fp = lambda value: hashlib.sha256(value.encode("utf-8")).hexdigest()
        assignment = SimpleNamespace(
            q_x_sha256=fp("source-qx"),
            g_a0_sha256=fp("source-g0"),
            g_a1_sha256=fp("source-g1"),
            r_common_sha256=fp("source-r"),
        )
        truth = SimpleNamespace(
            q_x_fingerprint=fp("source-qx"),
            g_a0_fingerprint=fp("target-g0"),
            g_a1_fingerprint=fp("target-g1"),
        )
        contract = SimpleNamespace(
            q_x_sha256=fp("target-qx"),
            source_q_x_sha256=fp("source-qx"),
            g_a0_sha256=fp("source-g0"),
            g_a1_sha256=fp("source-g1"),
            target_g_a0_sha256=fp("target-g0"),
            target_g_a1_sha256=fp("target-g1"),
            r_common_sha256=fp("source-r"),
            structural_support_contract=None,
        )
        with self.assertRaises(ThetaACalibrationError):
            _validate_truth_assignment_population_bindings(truth, assignment, contract)

    def test_pipeline_inference_options_follow_explicit_independence_contract(self):
        identified = self._design()
        options = theta_a_pipeline_inference_options(identified, identified.scenario_specs[0])
        self.assertEqual(options["theta_a_confidence_level"], 0.95)
        self.assertIs(options["theta_a_unit_independence_certified"], True)

        nonidentified = self._design(ThetaACalibrationScenario(
            scenario_id="THETA_A_NO_SUPPORT", scenario_version="1.0",
            world_version="world-v1", dgp_id="C10S-THETA-A", dgp_version="1.0",
            roster_version="1.0", unit_id_prefix="unit",
            expected_identification="NOT_IDENTIFIED", unit_independence_certified=False,
            dgp_profile=ThetaACalibrationDGPProfile(
                profile_id="THETA_A_TARGET_SUPPORT_PROFILE",
                profile_version="1.0",
                structural_support_contract_id="THETA_A_STRUCTURAL_SUPPORT",
                structural_support_contract_version="1.0",
                support_relation="TARGET_HAS_UNSUPPORTED_HISTORIES",
                target_unsupported_history_masses=(("h-target-only", 0.25),),
                expected_abstention_reason="TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT",
            ),
        ))
        options = theta_a_pipeline_inference_options(nonidentified, nonidentified.scenario_specs[0])
        self.assertIsNone(options["theta_a_confidence_level"])
        self.assertIs(options["theta_a_unit_independence_certified"], False)

        missingness = self._design(ThetaACalibrationScenario(
            scenario_id="THETA_A_MISSING", scenario_version="1.0",
            world_version="world-v1", dgp_id="C10S-THETA-A", dgp_version="1.0",
            roster_version="1.0", unit_id_prefix="unit",
            expected_identification="INDETERMINATE", unit_independence_certified=True,
            independence_basis="unit-level joint assignment is independent; observation incompleteness is separately represented",
        ))
        options = theta_a_pipeline_inference_options(missingness, missingness.scenario_specs[0])
        self.assertEqual(options["theta_a_confidence_level"], 0.95)
        self.assertIs(options["theta_a_unit_independence_certified"], True)

    def test_seed_bank_keeps_world_fixed_within_m_and_randomizes_each_r(self):
        design = self._design()
        calibration = build_theta_a_seed_bank(design, "calibration")
        evaluation = build_theta_a_seed_bank(design, "evaluation")
        validate_theta_a_seed_banks(calibration, evaluation, design=design)
        self.assertEqual(len(calibration), 4)
        for outer_id in ("outer-000000", "outer-000001"):
            rows = [x for x in calibration if x.outer_world_id == outer_id]
            self.assertEqual(len({x.world_id for x in rows}), 1)
            self.assertEqual(len({x.world_seed for x in rows}), 1)
            self.assertEqual(len({x.roster_id for x in rows}), 1)
            self.assertEqual(len({x.unit_id_prefix for x in rows}), 1)
            self.assertEqual(len({x.randomization_salt for x in rows}), 2)
            self.assertEqual(len({x.s3_seed for x in rows}), 2)
            self.assertEqual(len({x.run_id for x in rows}), 2)
        world_seeds = {
            outer_id: {x.world_seed for x in calibration if x.outer_world_id == outer_id}
            for outer_id in ("outer-000000", "outer-000001")
        }
        self.assertEqual(len(world_seeds["outer-000000"]), 1)
        self.assertEqual(len(world_seeds["outer-000001"]), 1)
        self.assertNotEqual(next(iter(world_seeds["outer-000000"])),
                            next(iter(world_seeds["outer-000001"])))
        self.assertNotEqual(
            next(x.roster_id for x in calibration if x.outer_world_id == "outer-000000"),
            next(x.roster_id for x in calibration if x.outer_world_id == "outer-000001"),
        )
        self.assertNotEqual(
            next(x.unit_id_prefix for x in calibration if x.outer_world_id == "outer-000000"),
            next(x.unit_id_prefix for x in calibration if x.outer_world_id == "outer-000001"),
        )
        self.assertFalse({x.world_seed for x in calibration} & {x.world_seed for x in evaluation})

    def test_profile_fingerprint_changes_r_streams_without_circularly_changing_world_seed(self):
        def scenario(mass):
            return ThetaACalibrationScenario(
                scenario_id="THETA_A_NO_SUPPORT", scenario_version="1.0",
                world_version="world-v1", dgp_id="C10S-THETA-A", dgp_version="1.0",
                roster_version="1.0", unit_id_prefix="unit",
                expected_identification="NOT_IDENTIFIED", unit_independence_certified=False,
                dgp_profile=ThetaACalibrationDGPProfile(
                    profile_id="THETA_A_TARGET_SUPPORT_PROFILE", profile_version="1.0",
                    structural_support_contract_id="THETA_A_STRUCTURAL_SUPPORT",
                    structural_support_contract_version="1.0",
                    support_relation="TARGET_HAS_UNSUPPORTED_HISTORIES",
                    target_unsupported_history_masses=(("h-target-only", mass),),
                    expected_abstention_reason="TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT",
                ),
            )
        first = build_theta_a_seed_bank(self._design(scenario(0.25)), "calibration")
        second = build_theta_a_seed_bank(self._design(scenario(0.40)), "calibration")
        for left, right in zip(first, second):
            self.assertEqual((left.world_seed, left.world_id, left.roster_id),
                             (right.world_seed, right.world_id, right.roster_id))
            self.assertNotEqual(left.dgp_profile_sha256, right.dgp_profile_sha256)
            self.assertNotEqual(left.run_id, right.run_id)
            self.assertNotEqual(left.randomization_salt, right.randomization_salt)
            self.assertNotEqual(left.s3_seed, right.s3_seed)

    def test_seed_bank_rejects_incomplete_r_coverage(self):
        design = self._design()
        rows = build_theta_a_seed_bank(design, "calibration")
        with self.assertRaises(ThetaACalibrationError):
            validate_theta_a_seed_banks(rows[:-1], (), design=design)

    def test_replicate_runner_requires_explicit_execution_authorization(self):
        design = self._design()
        called = []
        with self.assertRaisesRegex(ThetaACalibrationError, "execution_authorized=True"):
            run_theta_a_calibration_replicates(
                design, (), lambda *args: called.append(args),
                bank="calibration", execution_authorized=False,
            )
        self.assertEqual(called, [])

    def test_five_scenario_candidate_roster_and_shared_base_worlds(self):
        roster = build_theta_a_candidate_scenario_roster()
        self.assertEqual(
            [item.scenario_id for item in roster],
            [
                "THETA_A_POSITIVE_V1",
                "THETA_A_NULL_V1",
                "THETA_A_NEGATIVE_V1",
                "THETA_A_ALTERNATIVE_COMMON_V1",
                "THETA_A_TARGET_SUPPORT_NONIDENTIFIED_V1",
            ],
        )
        self.assertEqual(
            [item.dgp_profile.expected_theta_a_truth for item in roster],
            [0.5, 0.0, -0.5, 0.0, None],
        )
        self.assertEqual(roster[-1].expected_identification, "NOT_IDENTIFIED")
        self.assertEqual(
            roster[-1].dgp_profile.expected_abstention_reason,
            "TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT",
        )
        design = ThetaACalibrationDesign(
            scenario_specs=roster, n_grid=(4,), outer_worlds_m=2,
            assignment_replicates_r=2, confidence_level=0.95,
            namespace="theta-a-five-scenario-roster-contract-v1",
        )
        assignments = build_theta_a_seed_bank(design, "calibration")
        validate_theta_a_seed_banks(assignments, (), design=design)
        self.assertEqual(len(assignments), 5 * 1 * 2 * 2)
        by_scenario = {
            item.scenario_id: [
                row for row in assignments if row.scenario_id == item.scenario_id
            ]
            for item in roster
        }
        paired_ids = (
            "THETA_A_POSITIVE_V1",
            "THETA_A_ALTERNATIVE_COMMON_V1",
            "THETA_A_TARGET_SUPPORT_NONIDENTIFIED_V1",
        )
        for outer_id in ("outer-000000", "outer-000001"):
            paired = [
                next(row for row in by_scenario[sid] if row.outer_world_id == outer_id)
                for sid in paired_ids
            ]
            self.assertEqual(len({row.world_family_id for row in paired}), 1)
            self.assertEqual(len({row.world_id for row in paired}), 1)
            self.assertEqual(len({row.roster_id for row in paired}), 1)
            self.assertEqual(len({row.world_seed for row in paired}), 1)
            self.assertEqual(len({row.unit_id_prefix for row in paired}), 1)
            self.assertEqual(len({row.run_id for row in paired}), 3)
            self.assertEqual(len({row.randomization_salt for row in paired}), 3)
            self.assertEqual(len({row.s3_seed for row in paired}), 3)

    def test_s3_unit_seeds_are_stable_and_distinct(self):
        first = s3_seeds_by_unit(12345, ("u1", "u2", "u3"))
        second = s3_seeds_by_unit(12345, ("u1", "u2", "u3"))
        self.assertEqual(first, second)
        self.assertEqual(len(set(first.values())), 3)

    def test_interval_s3_observation_ids_bind_the_r_specific_unit_seed(self):
        design = self._design()
        assignment = build_theta_a_seed_bank(design, "calibration")[0]
        unit_ids = tuple(f"unit-{i}" for i in range(4))
        seeds = s3_seeds_by_unit(assignment.s3_seed, unit_ids)
        rows = []
        for unit_id in unit_ids:
            history_id = "history-" + unit_id
            payload = (
                assignment.run_id, unit_id, history_id,
                "monitor", "1", "grid", "1", 0, seeds[unit_id],
            )
            identity = hashlib.sha256(json.dumps(
                payload, sort_keys=True, separators=(",", ":"), allow_nan=False
            ).encode("utf-8")).hexdigest()[:24]
            rows.append(SimpleNamespace(
                run_id=assignment.run_id, unit_id=unit_id, history_id=history_id,
                monitor_id="monitor", monitor_version="1", grid_id="grid", grid_version="1",
                interval_index=0, interval_start=Decimal("0"), interval_end=Decimal("1"),
                coverage_mode="CONTINUOUS_EVENT_COVERAGE", observation_status="OBSERVED",
                observed_compliance=True, observation_id="IS3-" + identity,
            ))
        result = SimpleNamespace(
            s3_records=tuple(rows),
            world=SimpleNamespace(units=tuple(SimpleNamespace(unit_id=x) for x in unit_ids)),
        )
        _validate_interval_s3_seed_provenance(result, assignment)
        tampered = list(rows)
        tampered[0] = SimpleNamespace(**{
            **vars(tampered[0]), "observation_id": "IS3-" + "0" * 24
        })
        result.s3_records = tuple(tampered)
        with self.assertRaises(ThetaACalibrationError):
            _validate_interval_s3_seed_provenance(result, assignment)

    def test_identified_summary_aggregates_coverage_and_width_across_m(self):
        design = self._design()
        assignments = build_theta_a_seed_bank(design, "calibration")
        records = tuple(
            self._record(row, "IDENTIFIED", "IDENTIFIED", 0.21, 0.1, 0.3, True, 0.2, 0.95)
            for row in assignments
        )
        summary = summarize_theta_a_calibration(
            design, assignments, records, bank="calibration"
        )[0]
        metrics = {x.metric: x for x in summary.metrics}
        self.assertAlmostEqual(metrics["interval_coverage"].mean, 1.0)
        self.assertAlmostEqual(metrics["interval_width"].mean, 0.2)
        self.assertAlmostEqual(metrics["point_bias"].mean, 0.01)
        self.assertAlmostEqual(metrics["point_rmse"].mean, 0.01)
        self.assertEqual(metrics["interval_coverage"].precision_status, "PASS_PRECISION")
        self.assertEqual(set(metrics), {item.metric for item in THETA_A_METRIC_REGISTRY})
        self.assertIsNotNone(summary.metric_target_manifest_sha256)
        self.assertEqual(summary.type_i_error_status, "NOT_DEFINED_NO_TEST_PROCEDURE")
        self.assertEqual(summary.power_status, "NOT_DEFINED_NO_TEST_PROCEDURE")

    def test_metric_registry_is_exhaustive_and_declares_denominators(self):
        specs = {item.metric: item for item in THETA_A_METRIC_REGISTRY}
        self.assertEqual(len(specs), 16)
        self.assertEqual(
            specs["identification_rate"].within_world_denominator, "ALL_R",
        )
        self.assertEqual(
            specs["point_bias"].within_world_denominator,
            "ALL_R_IDENTIFIED_REQUIRED",
        )
        self.assertEqual(
            specs["interval_coverage"].within_world_denominator,
            "ALL_R_INTERVAL_REQUIRED",
        )
        self.assertEqual(
            specs["evaluator_correct_adjudication_rate"].within_world_denominator,
            "ALL_R_EVALUATOR_AUDIT_REQUIRED",
        )
        self.assertEqual(
            specs["correct_abstention_rate"].applicability, "NOT_IDENTIFIED",
        )

    def test_metric_targets_require_versioned_manifest_identity(self):
        design = replace(
            self._design(),
            metric_target_manifest_id=None,
            metric_target_manifest_version=None,
        )
        with self.assertRaises(ThetaACalibrationError):
            design.validate()

    def test_unverified_outer_world_sampling_suppresses_inferential_mcse(self):
        design = replace(
            self._design(),
            outer_world_sampling=OuterWorldSamplingContract(),
        )
        assignments = build_theta_a_seed_bank(design, "calibration")
        records = tuple(
            self._record(row, "IDENTIFIED", "IDENTIFIED", 0.21, 0.1, 0.3, True, 0.2, 0.95)
            for row in assignments
        )
        summary = summarize_theta_a_calibration(
            design, assignments, records, bank="calibration"
        )[0]
        metrics = {item.metric: item for item in summary.metrics}
        coverage = metrics["interval_coverage"]
        self.assertAlmostEqual(coverage.mean, 1.0)
        self.assertIsNone(coverage.mcse)
        self.assertEqual(coverage.precision_status, "NOT_EVALUABLE_IID_UNVERIFIED")
        self.assertEqual(
            coverage.mcse_interpretation, "NO_INFERENTIAL_MCSE_IID_UNVERIFIED",
        )
        self.assertEqual(summary.outer_world_sampling_mode, "UNVERIFIED")
        self.assertEqual(
            summary.outer_world_sampling_contract_sha256,
            design.outer_world_sampling.fingerprint_sha256,
        )

    def test_declared_iid_outer_world_contract_requires_complete_provenance(self):
        design = replace(
            self._design(),
            outer_world_sampling=OuterWorldSamplingContract(
                mode="DECLARED_IID_PSEUDORANDOM",
                contract_id="TEST-IID", contract_version="1.0",
                target_distribution_id="TEST-DGP",
                target_distribution_version="1.0",
            ),
        )
        with self.assertRaises(ThetaACalibrationError):
            design.validate()

    def test_replicates_within_must_keep_world_and_policy_fingerprints(self):
        design = self._design()
        assignments = build_theta_a_seed_bank(design, "calibration")
        records = [
            self._record(row, "IDENTIFIED", "IDENTIFIED", 0.21, 0.1, 0.3, True, 0.2, 0.95)
            for row in assignments
        ]
        records[0] = replace(records[0], world_configuration_sha256=hashlib.sha256(b"drift").hexdigest())
        with self.assertRaises(ThetaACalibrationError):
            summarize_theta_a_calibration(design, assignments, records, bank="calibration")

    def test_missing_interval_is_not_dropped_from_coverage_denominator(self):
        design = self._design()
        assignments = build_theta_a_seed_bank(design, "calibration")
        records = []
        for index, row in enumerate(assignments):
            if index == 0:
                records.append(self._record(
                    row, "IDENTIFIED", "INDETERMINATE", None, None, None, None, None, 0.95
                ))
            else:
                records.append(self._record(
                    row, "IDENTIFIED", "IDENTIFIED", 0.21, 0.1, 0.3, True, 0.2, 0.95
                ))
        summary = summarize_theta_a_calibration(
            design, assignments, records, bank="calibration"
        )[0]
        metrics = {x.metric: x for x in summary.metrics}
        self.assertAlmostEqual(metrics["interval_availability_rate"].mean, 0.75)
        self.assertEqual(metrics["interval_coverage"].precision_status, "NOT_EVALUABLE")
        self.assertEqual(metrics["point_bias"].precision_status, "NOT_EVALUABLE")

    def test_nonidentified_scenario_reports_correct_abstention(self):
        scenario = ThetaACalibrationScenario(
            scenario_id="THETA_A_NO_SUPPORT", scenario_version="1.0",
            world_version="world-v1", dgp_id="C10S-THETA-A", dgp_version="1.0",
            roster_version="1.0", unit_id_prefix="unit",
            expected_identification="NOT_IDENTIFIED", unit_independence_certified=False,
            dgp_profile=ThetaACalibrationDGPProfile(
                profile_id="THETA_A_TARGET_SUPPORT_PROFILE",
                profile_version="1.0",
                structural_support_contract_id="THETA_A_STRUCTURAL_SUPPORT",
                structural_support_contract_version="1.0",
                support_relation="TARGET_HAS_UNSUPPORTED_HISTORIES",
                target_unsupported_history_masses=(("h-target-only", 0.25),),
                expected_abstention_reason="TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT",
            ),
        )
        design = replace(self._design(scenario), assignment_replicates_r=3)
        assignments = build_theta_a_seed_bank(design, "calibration")
        records = []
        for row in assignments:
            if row.assignment_replicate == 0:
                observed, reason, point = "NOT_IDENTIFIED", "TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT", None
            elif row.assignment_replicate == 1 and row.outer_world_id == "outer-000000":
                observed, reason, point = "NOT_IDENTIFIED", "SOURCE_ASSIGNMENT_POSITIVITY_FAILURE", None
            elif row.assignment_replicate == 1:
                observed, reason, point = "INDETERMINATE", "REALIZED_GA_ARM_SUPPORT_MISSING", None
            elif row.outer_world_id == "outer-000000":
                observed, reason, point = "PARTIALLY_IDENTIFIED", "STRICT_VCONT_NOT_OBSERVED_BY_POINT_SAMPLES", None
            else:
                observed, reason, point = "IDENTIFIED", None, 0.2
            records.append(self._record(
                row, "NOT_IDENTIFIED", observed, point, None, None, None, None, None,
                expected_reason="TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT",
                observed_reason=reason, unsupported_mass=0.25,
            ))
        summary = summarize_theta_a_calibration(
            design, assignments, tuple(records), bank="calibration"
        )[0]
        metrics = {x.metric: x for x in summary.metrics}
        self.assertAlmostEqual(metrics["correct_abstention_rate"].mean, 1 / 3)
        self.assertAlmostEqual(metrics["wrong_cause_abstention_rate"].mean, 1 / 3)
        self.assertAlmostEqual(metrics["partial_identification_rate"].mean, 1 / 6)
        self.assertAlmostEqual(metrics["false_identification_rate"].mean, 1 / 6)

    def test_partial_identification_is_rejected_until_bounds_are_adjudicated(self):
        scenario = ThetaACalibrationScenario(
            scenario_id="THETA_A_PARTIAL", scenario_version="1.0",
            world_version="world-v1", dgp_id="C10S-THETA-A", dgp_version="1.0",
            roster_version="1.0", unit_id_prefix="unit",
            expected_identification="PARTIALLY_IDENTIFIED", unit_independence_certified=False,
        )
        with self.assertRaises(ThetaACalibrationError):
            self._design(scenario).validate()


if __name__ == "__main__":
    unittest.main()
