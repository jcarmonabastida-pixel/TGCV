"""End-to-end integration of the DGP -> EventHistory -> interval S3 -> oracle path.

Source-level regression only. This module is included in EP-02 but has not
been executed under the current execution authorization boundary.
"""
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
from theta_a_interval_observation import IntervalMonitorConfig


class CompleteWorldIntervalIntegrationTests(unittest.TestCase):
    def _fixture(self):
        world_config = SyntheticWorldConfig(
            world_id="WORLD-INTERVAL-INTEGRATION",
            world_version="1",
            dgp_id="DGP-INTERVAL-INTEGRATION",
            dgp_version="1",
            roster_id="ROSTER-INTERVAL-INTEGRATION",
            roster_version="1",
            unit_id_prefix="U",
            n_units=16,
            seed=20261116,
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
            q_x_mass_by_unit=(1.0 / 16.0,) * 16,
        )
        d2_config = D2MechanismConfig(
            "DGP-INTERVAL-INTEGRATION", "1",
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
        zero_vector = (0.0, 0.0, 0.0, 0.0)
        one_vector = (1.0, 0.0, 0.0, 0.0)
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
            True, "NO_ADMISSION", "STANDARD", "PROFILE-1", "1",
        )
        functional_config = FunctionalHistoryDGPConfig(
            dgp_id=world.dgp_id,
            dgp_version=world.dgp_version,
            mechanism_id="FUNCTIONAL-MECHANISM",
            mechanism_version="1",
            run_id="RUN-INTERVAL-INTEGRATION",
            history_version="1",
            adjudication_rules_version="B1-RULES-1",
            support_start=Decimal("0"),
            support_end=Decimal("2"),
            profile_config_id="PROFILE-1",
            profile_config_version="1",
            rules=(
                FunctionalHistoryRule(
                    rule_id="GA-VECTOR-ENABLES-ADMISSION",
                    source="G_A",
                    event_time=Decimal("1"),
                    causal_family="DIRECT_GA_FUNCTIONAL_ADMISSION",
                    provenance_ref="FUNCTIONAL-DGP#GA-VECTOR-ENABLES-ADMISSION",
                    set_admission="ADMIT",
                    vector_index=0,
                    vector_value=1.0,
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

    def test_dgp_world_flows_through_realized_interval_evidence_and_reserved_oracle(self):
        fixture = self._fixture()
        result = materialize_c10s_complete_world_from_dgp(
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

        # The DGP-generated potential histories, not caller-supplied histories,
        # feed the reserved oracle and the realized-assignment selection.
        self.assertEqual(len(result.d2_histories_by_unit_z), 32)
        self.assertEqual(len(result.theta_a_truth.event_history_manifest), 32)
        self.assertAlmostEqual(result.theta_a_truth.theta_a_truth, 0.5)
        self.assertEqual(
            {row.assigned_arm for row in result.theta_a_assignments.assignments},
            {0, 1},
        )
        self.assertEqual(len(result.realized_history_selection.selected_history_manifest), 16)

        # Every selected history is observed on the common continuous interval
        # grid; neither latent histories nor V_cont adjudications cross S3.
        self.assertEqual(result.sealed_evidence.manifest["temporal_resolution"], "INTERVAL_LEVEL")
        self.assertEqual(len(result.s3_records), 32)
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


if __name__ == "__main__":
    unittest.main()
