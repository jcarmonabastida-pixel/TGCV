"""End-to-end integration of the DGP -> EventHistory -> interval S3 -> oracle path.

Source-level regression only. This module is included in EP-02 but has not
been executed under the current execution authorization boundary.
"""
from dataclasses import replace
from decimal import Decimal
import unittest

from c10s_synthetic_components import (
    D2MechanismConfig,
    D2ReachGenerationConfig,
    D2ReachRouteTemplate,
    D2ReachStepTemplate,
    D2StructuralGenerationConfig,
    D2TrajectoryGenerationConfig,
    FunctionalState,
    IntervalGrid,
    JointPolicyHistory,
    RCommonPairCertificate,
    SyntheticWorldBuilder,
    SyntheticWorldConfig,
    ThetaAPolicyAssignmentConfig,
)
from c10s_functional_history import (
    FunctionalHistoryDGPConfig,
    FunctionalHistoryRule,
)
from c10s_world_pipeline import materialize_c10s_complete_world_from_dgp
from c10s_factorial_pipeline import materialize_c10s_factorial_world_from_dgp
from theta_am_factorial import FactorialAssignmentConfig
from theta_a_interval_observation import IntervalMonitorConfig


class CompleteWorldIntervalIntegrationTests(unittest.TestCase):
    def _fixture(self, theta_a_mode="positive"):
        if theta_a_mode not in ("positive", "null", "negative", "alternative"):
            raise ValueError("unsupported focal theta_A scenario")
        # Positive and alternative regimes share one base DGP/population.
        scenario = "INTERACTION" if theta_a_mode in ("positive", "alternative") else theta_a_mode.upper()
        dgp_id = f"DGP-INTERVAL-INTEGRATION-{scenario}"
        world_config = SyntheticWorldConfig(
            world_id=f"WORLD-INTERVAL-INTEGRATION-{scenario}",
            world_version="1",
            dgp_id=dgp_id,
            dgp_version="1",
            roster_id=f"ROSTER-INTERVAL-INTEGRATION-{scenario}",
            roster_version="1",
            unit_id_prefix="U",
            n_units=32,
            seed=20261116 + {"positive": 0, "null": 1, "negative": 2, "alternative": 0}[theta_a_mode],
            x_dimension=1,
            h0_distribution=(("H0", 1.0),),
            c_c_dimension=1,
            c_c_component_probability=1.0,
            need_pre_z_probability=1.0,
            focal_accessible_pre_probability=0.0,
            c_auth_base_probability=1.0,
            c_resource_probability=1.0,
            c_capacity_probability=1.0,
            c_info_probability=1.0,
            c_domain_probability=1.0,
            c_other_probability=1.0,
            q_x_mass_by_unit=(1.0 / 32.0,) * 32,
        )
        d2_config = D2MechanismConfig(
            dgp_id, "1",
            ("D2-Z0", "D2-Z1"), ("1", "1"),
            ("ART-D2-Z0", "ART-D2-Z1"), ("ACTOR-Z0", "ACTOR-Z1"),
            (0.0, 1.0), (1.0, 1.0), (0.0, 0.0),
            (1.0, 1.0), (1.0, 1.0),
            (((True, True, True, True), 1.0),),
            "D2-MECH-1",
        )
        structural_config = D2StructuralGenerationConfig(
            config_id="STRUCTURAL-INTEGRATION",
            config_version="1",
            focal_transformation_id="TAU-FOCAL",
            focal_semantic_version="1",
            boundary_id="BOUNDARY-1",
            context_id="CONTEXT-1",
            catalog_version="CATALOG-1",
            invariant_atoms=(),
        )
        reach_config = D2ReachGenerationConfig(
            config_id="REACH-INTEGRATION",
            config_version="1",
            horizon=2.0,
            transformation_universe=("TAU-FOCAL",),
            target_states=("TARGET",),
            route_templates=(
                D2ReachRouteTemplate(
                    route_id="ROUTE-FOCAL",
                    target_state="TARGET",
                    steps=(D2ReachStepTemplate(
                        transformation_id="TAU-FOCAL",
                        state_before="S0",
                        state_after="S1",
                        applicability_state=1,
                        duration=1.0,
                    ),),
                    relation_atom_bindings=(),
                    temporal_feasibility_state=1,
                    route_scope="FOCAL",
                ),
            ),
            universe_exhaustive=True,
            relations_exhaustive=True,
            conditions_exhaustive=True,
            resources_exhaustive=True,
            enumeration_complete=True,
        )
        trajectory_config = D2TrajectoryGenerationConfig(
            config_id="TRAJECTORY-INTEGRATION",
            config_version="1",
            selection_probability_by_target=(("TARGET", 1.0),),
            route_selection_weight=(("ROUTE-FOCAL", 1.0),),
            route_execution_probability=(("ROUTE-FOCAL", 1.0),),
            step_execution_probability=(("TAU-FOCAL", 1.0),),
            randomization_salt="TRAJECTORY-SALT",
        )
        world = SyntheticWorldBuilder().generate(world_config, d2_config)
        alternative_active = theta_a_mode == "alternative"
        zero_vector = (0.0, 1.0, 0.0, 0.0) if alternative_active else (0.0, 0.0, 0.0, 0.0)
        one_vector = (1.0, 1.0, 0.0, 0.0) if alternative_active else (1.0, 0.0, 0.0, 0.0)
        g_a0 = tuple(
            JointPolicyHistory(row.history_ref, ((zero_vector, 1.0),))
            for row in world.q_x
        )
        g_a1 = tuple(
            JointPolicyHistory(row.history_ref, ((one_vector, 1.0),))
            for row in world.q_x
        )
        r_common = tuple(
            RCommonPairCertificate(
                row.history_ref, "R-COMMON", "1",
                "R-COMMON-FINGERPRINT", "R-COMMON-FINGERPRINT",
                "COMMON_FIXED",
            )
            for row in world.q_x
        )
        feasible = {
            row.history_ref: (zero_vector, one_vector)
            for row in world.q_x
        }
        assignment_config = ThetaAPolicyAssignmentConfig(
            mechanism_id="DIRECT-GA-RANDOMIZATION",
            mechanism_version="1",
            randomization_salt="DIRECT-GA-SALT",
            probability_a1_by_history=tuple(
                (row.history_ref, 0.5) for row in world.q_x
            ),
        )
        initial = FunctionalState(
            True, "ADMIT", "STANDARD", "PROFILE-1", "1",
        )
        functional_config = FunctionalHistoryDGPConfig(
            dgp_id=world.dgp_id,
            dgp_version=world.dgp_version,
            mechanism_id=f"FUNCTIONAL-MECHANISM-{scenario}",
            mechanism_version="1",
            run_id=f"RUN-INTERVAL-INTEGRATION-{theta_a_mode.upper()}",
            history_version="1",
            adjudication_rules_version="B1-RULES-1",
            support_start=Decimal("0"),
            support_end=Decimal("2"),
            profile_config_id="PROFILE-1",
            profile_config_version="1",
            rules=(
                # D2 package-to-admission is held constant across focal scenarios.
                FunctionalHistoryRule(
                    rule_id="D2-PACKAGE-DIRECTLY-INTERRUPTS-ADMISSION",
                    source="D2",
                    event_time=Decimal("1"),
                    causal_family="D2_DIRECT_PACKAGE_PATH",
                    provenance_ref="FUNCTIONAL-DGP#D2-PACKAGE-DIRECTLY-INTERRUPTS-ADMISSION",
                    set_admission="NO_ADMISSION",
                    d2_field="w_programmed",
                    d2_value=True,
                ),
                *(
                    (
                        FunctionalHistoryRule(
                            rule_id="GA-ALTERNATIVE-DISABLES-ADMISSION",
                            source="G_A",
                            event_time=Decimal("0.5"),
                            causal_family="ALTERNATIVE_FUNCTIONAL_PATH",
                            provenance_ref="FUNCTIONAL-DGP#GA-ALTERNATIVE-DISABLES-ADMISSION",
                            set_enabled=False,
                            vector_index=1,
                            vector_value=1.0,
                        ),
                        FunctionalHistoryRule(
                            rule_id="GA-FOCAL-ONLY-WHEN-ALTERNATIVE-ABSENT",
                            source="G_A",
                            event_time=Decimal("1"),
                            causal_family="FOCAL_BY_ALTERNATIVE_INTERACTION",
                            provenance_ref="FUNCTIONAL-DGP#GA-FOCAL-ONLY-WHEN-ALTERNATIVE-ABSENT",
                            set_admission="NO_ADMISSION",
                            vector_predicates=((0, 0.0), (1, 0.0)),
                        ),
                    )
                    if theta_a_mode in ("positive", "alternative")
                    else (() if theta_a_mode == "null" else (FunctionalHistoryRule(
                        rule_id=f"GA-VECTOR-INTERRUPTS-ADMISSION-{scenario}",
                        source="G_A",
                        event_time=Decimal("1"),
                        causal_family="DIRECT_GA_FUNCTIONAL_ADMISSION",
                        provenance_ref=f"FUNCTIONAL-DGP#GA-VECTOR-INTERRUPTS-ADMISSION-{scenario}",
                        set_admission="NO_ADMISSION",
                        vector_predicates=((0, 1.0), (1, 0.0)),
                    ),))
                ),
            ),
        )
        initial_by_unit_z = {
            (unit.unit_id, z): initial
            for unit in world.units for z in (0, 1)
        }
        initial_by_history = {
            row.history_ref: initial for row in world.q_x
        }
        grid = IntervalGrid(
            (Decimal("0"), Decimal("1"), Decimal("2")),
            "GRID-INTEGRATION", "1",
        )
        # Gate 131 scope: ideal best-case benchmark only. This perfect,
        # complete interval channel tests the software path; it is not a
        # validated model for imperfect passive S3 measurement.
        monitor = IntervalMonitorConfig(
            monitor_id="MONITOR-INTEGRATION",
            monitor_version="1",
            coverage_mode="CONTINUOUS_EVENT_COVERAGE",
            missing_probability=0.0,
            capture_lag=Decimal("0.1"),
            ingestion_lag=Decimal("0.2"),
        )
        return {
            "world_config": world_config,
            "d2_config": d2_config,
            "structural_config": structural_config,
            "reach_config": reach_config,
            "trajectory_config": trajectory_config,
            "functional_config": functional_config,
            "initial_by_unit_z": initial_by_unit_z,
            "initial_by_history": initial_by_history,
            "grid": grid,
            "g_a0": g_a0,
            "g_a1": g_a1,
            "feasible": feasible,
            "r_common": r_common,
            "assignment_config": assignment_config,
            "monitor_configs": {
                row.history_ref: monitor for row in world.q_x
            },
            "monitor_seeds": {
                unit.unit_id: 9000 + index
                for index, unit in enumerate(world.units)
            },
        }

    def _run_pipeline(self, fixture):
        return materialize_c10s_complete_world_from_dgp(
            world_config=fixture["world_config"],
            d2_config=fixture["d2_config"],
            structural_config=fixture["structural_config"],
            reach_config=fixture["reach_config"],
            trajectory_config=fixture["trajectory_config"],
            functional_history_config=fixture["functional_config"],
            initial_state_by_unit_z=fixture["initial_by_unit_z"],
            initial_state_by_history=fixture["initial_by_history"],
            grid=fixture["grid"],
            g_a0=fixture["g_a0"],
            g_a1=fixture["g_a1"],
            feasible_vectors_by_history=fixture["feasible"],
            r_common_certificates=fixture["r_common"],
            assignment_config=fixture["assignment_config"],
            estimand_version="1",
            outcome_version="VCONT-B1-1",
            evaluation_tolerance=2.0,
            interval_monitor_configs_by_history_ref=fixture["monitor_configs"],
            interval_monitor_seeds_by_unit=fixture["monitor_seeds"],
        )

    def test_dgp_world_flows_through_realized_interval_evidence_and_reserved_oracle(self):
        fixture = self._fixture("positive")
        result = self._run_pipeline(fixture)

        # The DGP-generated potential histories, not caller-supplied histories,
        # feed the reserved oracle and the realized-assignment selection.
        self.assertEqual(len(result.d2_histories_by_unit_z), 64)
        self.assertEqual(len(result.theta_a_truth.event_history_manifest), 64)
        self.assertAlmostEqual(result.theta_a_truth.theta_a_truth, 0.5)
        # D2 has a distinct direct package path with the opposite sign.
        # Its ITT-Z must never be relabelled as the focal accessibility effect.
        self.assertAlmostEqual(result.d2_vcont_truth.finite_population_itt_z_v_cont, -0.5)
        self.assertNotAlmostEqual(
            result.d2_vcont_truth.finite_population_itt_z_v_cont,
            result.theta_a_truth.theta_a_truth,
        )
        self.assertEqual(
            {row.assigned_arm for row in result.theta_a_assignments.assignments},
            {0, 1},
        )
        self.assertEqual(len(result.realized_history_selection.selected_history_manifest), 32)

        # Every selected history is observed on the common continuous interval
        # grid; neither latent histories nor V_cont adjudications cross S3.
        self.assertEqual(result.sealed_evidence.manifest["temporal_resolution"], "INTERVAL_LEVEL")
        self.assertEqual(len(result.s3_records), 64)
        self.assertTrue(all(row.observation_status == "OBSERVED" for row in result.s3_records))
        for row in result.sealed_evidence.rows:
            self.assertNotIn("event_history", row)
            self.assertNotIn("interval_adjudication", row)
            self.assertNotIn("v_cont_truth", row)
            self.assertIn("history_content_sha256", row)

        # Independently reproduce the Analyzer's finite-sample HT contrast
        # from sealed observations and the declared q_X / assignment design.
        qx_mass = {row.history_ref: row.mass for row in result.world.q_x}
        unit_rows = {}
        for row in result.sealed_evidence.rows:
            unit_rows.setdefault(row["unit_id"], []).append(row)
        expected_by_arm = [0.0, 0.0]
        for rows in unit_rows.values():
            first = rows[0]
            ordered = sorted(rows, key=lambda row: row["interval_index"])
            unit_outcome = sum(
                row["observed_compliance"] is True for row in ordered
            ) / len(ordered)
            expected_by_arm[first["assigned_arm"]] += (
                qx_mass[first["history_ref"]] / first["assignment_probability"]
            ) * unit_outcome
        expected_ht = expected_by_arm[1] - expected_by_arm[0]
        self.assertEqual(result.analyzer_result.identification, "IDENTIFIED")
        self.assertAlmostEqual(result.analyzer_result.point_estimate, expected_ht)
        self.assertTrue(result.evaluator_result.correct_adjudication)
        self.assertEqual(
            result.evaluator_result.evidence_sha256,
            result.sealed_evidence.sha256,
        )
        self.assertEqual(
            result.evaluator_result.analyzer_output_sha256,
            result.analyzer_result.output_sha256,
        )
        result.validate(
            grid=fixture["grid"],
            reach_config=fixture["reach_config"],
            g_a0=fixture["g_a0"],
            g_a1=fixture["g_a1"],
            assignment_config=fixture["assignment_config"],
            feasible_vectors_by_history=fixture["feasible"],
            r_common_certificates=fixture["r_common"],
        )
        # Same base world/population and DGP; only the common alternative
        # regime changes between the two focal-policy contrasts.
        alternative_fixture = self._fixture("alternative")
        alternative_result = self._run_pipeline(alternative_fixture)
        self.assertEqual(result.world.world_id, alternative_result.world.world_id)
        self.assertEqual(result.world.q_x, alternative_result.world.q_x)
        self.assertAlmostEqual(alternative_result.theta_a_truth.theta_a_truth, 0.0)
        self.assertAlmostEqual(
            result.theta_a_truth.theta_a_truth - alternative_result.theta_a_truth.theta_a_truth,
            0.5,
        )
        self.assertAlmostEqual(alternative_result.d2_vcont_truth.finite_population_itt_z_v_cont, -0.5)

    def test_null_and_negative_focal_scenarios_are_separately_generated(self):
        expected_truth = {"null": 0.0, "negative": -0.5}
        results = {}
        for mode, truth in expected_truth.items():
            with self.subTest(theta_a_mode=mode):
                result = self._run_pipeline(self._fixture(mode))
                results[mode] = result
                self.assertAlmostEqual(result.theta_a_truth.theta_a_truth, truth)
                self.assertAlmostEqual(result.d2_vcont_truth.finite_population_itt_z_v_cont, -0.5)
                self.assertEqual(result.analyzer_result.identification, "IDENTIFIED")
                self.assertEqual(result.evaluator_result.truth, truth)
                self.assertTrue(result.evaluator_result.correct_adjudication)
                self.assertEqual(result.evaluator_result.evidence_sha256, result.sealed_evidence.sha256)
                self.assertEqual(result.evaluator_result.analyzer_output_sha256, result.analyzer_result.output_sha256)
        # Under the null, a single randomized HT estimate may fluctuate; the
        # reserved oracle truth, not a forced zero estimate, defines the null.


    def test_factorial_a_by_m_recovers_both_simple_effects_and_interaction(self):
        fixture = self._fixture("positive")
        base = fixture["functional_config"]
        # M is an independent synthetic functional pathway. It changes
        # admission directly through a G_M rule and has no Vector4 coordinate.
        m_rule = FunctionalHistoryRule(
            rule_id="GM-ALTERNATIVE-FUNCTIONAL-ADMISSION-PATH",
            source="G_M",
            event_time=Decimal("0.5"),
            causal_family="ALTERNATIVE_FUNCTIONAL_PATH_M",
            provenance_ref="FUNCTIONAL-DGP#GM-ALTERNATIVE-FUNCTIONAL-ADMISSION-PATH",
            set_admission="NO_ADMISSION",
            factor_m_value=True,
        )
        functional = replace(base, rules=base.rules + (m_rule,))
        probability_by_history = tuple(
            (history_ref, 0.25, 0.25, 0.25, 0.25)
            for history_ref in fixture["monitor_configs"]
        )
        assignment = FactorialAssignmentConfig(
            mechanism_id="DIRECT-GA-X-ALT-M-FACTORIAL",
            mechanism_version="1",
            factor_m_id="ALT-FUNCTIONAL-PATH-M",
            factor_m_version="1",
            randomization_salt="DIRECT-GA-X-ALT-M-FACTORIAL-SALT",
            probability_by_history=probability_by_history,
        )
        grids = {ref: fixture["grid"] for ref in fixture["monitor_configs"]}
        result = materialize_c10s_factorial_world_from_dgp(
            world_config=fixture["world_config"],
            d2_config=fixture["d2_config"],
            structural_config=fixture["structural_config"],
            reach_config=fixture["reach_config"],
            trajectory_config=fixture["trajectory_config"],
            functional_history_config=functional,
            initial_state_by_unit_z=fixture["initial_by_unit_z"],
            initial_state_by_history=fixture["initial_by_history"],
            grid=fixture["grid"],
            g_a0=fixture["g_a0"],
            g_a1=fixture["g_a1"],
            feasible_vectors_by_history=fixture["feasible"],
            r_common_certificates=fixture["r_common"],
            assignment_config=assignment,
            grids_by_history_ref=grids,
            interval_monitor_configs_by_history_ref=fixture["monitor_configs"],
            interval_monitor_seeds_by_unit=fixture["monitor_seeds"],
            estimand_version="1",
            evaluation_tolerance=2.0,
        )
        self.assertEqual(len(result.factorial_potential_histories), 128)
        self.assertEqual(len(result.assignment_bundle.assignments), 32)
        self.assertEqual(
            {row.cell_id for row in result.assignment_bundle.assignments},
            {"00", "10", "01", "11"},
        )
        truth = result.reserved_truth
        self.assertAlmostEqual(truth.cell_means[0], 0.0)
        self.assertAlmostEqual(truth.cell_means[1], 1.0)
        self.assertAlmostEqual(truth.cell_means[2], 0.0)
        self.assertAlmostEqual(truth.cell_means[3], 0.0)
        self.assertAlmostEqual(truth.theta_a_given_m0, 1.0)
        self.assertAlmostEqual(truth.theta_a_given_m1, 0.0)
        self.assertAlmostEqual(truth.theta_am_interaction, -1.0)
        self.assertEqual(len(result.analyzer_result.contrasts), 3)
        self.assertTrue(result.evaluator_result.correct_adjudication)

        # Independently reconstruct the four strict-V_cont HT cell means from
        # realized S3 rows; no latent or reserved truth enters this calculation.
        qx_mass = {row.history_ref: row.mass for row in result.world.q_x}
        by_unit = {}
        for row in result.sealed_evidence.rows:
            by_unit.setdefault(row["unit_id"], []).append(row)
        expected_cells = [0.0, 0.0, 0.0, 0.0]
        cell_index = {"00": 0, "10": 1, "01": 2, "11": 3}
        for rows in by_unit.values():
            first = rows[0]
            strict_v_cont = float(all(row["observed_compliance"] is True for row in rows))
            expected_cells[cell_index[first["assigned_cell"]]] += (
                qx_mass[first["history_ref"]] / first["assignment_probability"]
            ) * strict_v_cont
        expected_contrasts = (
            expected_cells[1] - expected_cells[0],
            expected_cells[3] - expected_cells[2],
            (expected_cells[3] - expected_cells[2]) - (expected_cells[1] - expected_cells[0]),
        )
        for observed, expected in zip(result.analyzer_result.contrasts, expected_contrasts):
            self.assertEqual(observed.identification, "IDENTIFIED")
            self.assertAlmostEqual(observed.point_estimate, expected)

        # Null-M negative control: the same factorial assignment and world,
        # but no G_M functional rule, must recover zero interaction.
        null_result = materialize_c10s_factorial_world_from_dgp(
            world_config=fixture["world_config"],
            d2_config=fixture["d2_config"],
            structural_config=fixture["structural_config"],
            reach_config=fixture["reach_config"],
            trajectory_config=fixture["trajectory_config"],
            functional_history_config=base,
            initial_state_by_unit_z=fixture["initial_by_unit_z"],
            initial_state_by_history=fixture["initial_by_history"],
            grid=fixture["grid"],
            g_a0=fixture["g_a0"],
            g_a1=fixture["g_a1"],
            feasible_vectors_by_history=fixture["feasible"],
            r_common_certificates=fixture["r_common"],
            assignment_config=assignment,
            grids_by_history_ref=grids,
            interval_monitor_configs_by_history_ref=fixture["monitor_configs"],
            interval_monitor_seeds_by_unit=fixture["monitor_seeds"],
            estimand_version="1",
            evaluation_tolerance=2.0,
        )
        self.assertAlmostEqual(null_result.reserved_truth.theta_a_given_m0, 1.0)
        self.assertAlmostEqual(null_result.reserved_truth.theta_a_given_m1, 1.0)
        self.assertAlmostEqual(null_result.reserved_truth.theta_am_interaction, 0.0)
        self.assertTrue(null_result.evaluator_result.correct_adjudication)

if __name__ == "__main__":
    unittest.main()
