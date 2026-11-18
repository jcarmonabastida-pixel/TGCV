"""End-to-end integration of the DGP -> EventHistory -> interval/point S3 -> oracle paths.

Source-level regression only. This module is included in EP-02 but has not
been executed under the current execution authorization boundary.
"""
from dataclasses import replace
from decimal import Decimal
import unittest

from c10s_synthetic_components import (
    ContractError,
    D2MechanismConfig,
    D2ReachGenerationConfig,
    D2ReachRouteTemplate,
    D2ReachStepTemplate,
    D2StructuralGenerationConfig,
    D2TrajectoryGenerationConfig,
    GAStructuralTransitionRule,
    StructuralAtom,
    FunctionalState,
    IntervalGrid,
    JointPolicyHistory,
    QXHistoryMass,
    RCommonPairCertificate,
    SyntheticWorldBuilder,
    digest,
    SyntheticWorldConfig,
    NeedPreZStipulation,
    ThetaAPolicyAssignmentConfig,
    S3ObservationConfig,
    S3SequenceKernelRow,
)
from theta_a_analyzer import ThetaAStructuralSupportRow, ThetaAStructuralSupportContract
from c10s_functional_history import (
    FunctionalHistoryDGPConfig,
    FunctionalHistoryRule,
)
from c10s_world_pipeline import (
    SyntheticThetaATargetHistory,
    materialize_c10s_complete_world_from_dgp,
)
from c10s_factorial_pipeline import materialize_c10s_factorial_world_from_dgp
from c10s_dual_cohort_pipeline import (
    materialize_c10s_dual_cohort_world_from_dgp,
    _validate_cohort_initial_states,
)
from d2_observed_assignment import D2ObservedAssignmentConfig
from d2_ittz_evaluator import D2ITTZEvaluator
from d2_ittz_analyzer import D2ITTZAnalyzer, _result_payload, _output_hash
from d2_interval_observation import D2IntervalEvidenceCandidate, D2IntervalSealer
from theta_am_factorial import (
    FactorialAssignmentConfig, FactorialIntervalSealer,
    FactorialObservationAnalyzer, evaluate_factorial_analysis,
    factorial_candidate_from_records,
)
from theta_a_interval_observation import IntervalMonitorConfig
from theta_a_calibration_protocol import (
    ThetaACalibrationDesign, ThetaACalibrationScenario,
    build_theta_a_seed_bank, capture_theta_a_replicate,
    s3_seeds_by_unit, summarize_theta_a_calibration,
    theta_a_pipeline_inference_options,
)


class CompleteWorldIntervalIntegrationTests(unittest.TestCase):
    def _fixture(self, theta_a_mode="positive", seed_assignment=None, n_units=None):
        if theta_a_mode not in ("positive", "null", "negative", "alternative"):
            raise ValueError("unsupported focal theta_A scenario")
        # Positive and alternative regimes share one base DGP/population.
        scenario = "INTERACTION" if theta_a_mode in ("positive", "alternative") else theta_a_mode.upper()
        dgp_id = f"DGP-INTERVAL-INTEGRATION-{scenario}"
        n_units = (seed_assignment.n_units if seed_assignment is not None
                   else (n_units if n_units is not None else 32))
        world_config = SyntheticWorldConfig(
            world_id=(seed_assignment.world_id if seed_assignment is not None
                      else f"WORLD-INTERVAL-INTEGRATION-{scenario}"),
            world_version=(seed_assignment.world_version if seed_assignment is not None else "1"),
            dgp_id=(seed_assignment.dgp_id if seed_assignment is not None else dgp_id),
            dgp_version=(seed_assignment.dgp_version if seed_assignment is not None else "1"),
            roster_id=(seed_assignment.roster_id if seed_assignment is not None
                       else f"ROSTER-INTERVAL-INTEGRATION-{scenario}"),
            roster_version=(seed_assignment.roster_version if seed_assignment is not None else "1"),
            unit_id_prefix=(seed_assignment.unit_id_prefix if seed_assignment is not None else "U"),
            n_units=n_units,
            seed=(seed_assignment.world_seed if seed_assignment is not None else
                  20261116 + {"positive": 0, "null": 1, "negative": 2, "alternative": 0}[theta_a_mode]),
            x_dimension=1,
            h0_distribution=(("H0", 1.0),),
            c_c_dimension=1,
            c_c_component_probability=1.0,
            focal_accessible_pre_probability=0.0,
            c_auth_base_probability=1.0,
            c_resource_probability=1.0,
            c_capacity_probability=1.0,
            c_info_probability=1.0,
            c_domain_probability=1.0,
            c_other_probability=1.0,
            q_x_mass_by_unit=(1.0 / n_units,) * n_units,
        )
        d2_config = D2MechanismConfig(
            world_config.dgp_id, world_config.dgp_version,
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
        r_common_fingerprint = digest((
            "R-COMMON", "1",
            "ALTERNATIVE_ACTIVE" if alternative_active else "ALTERNATIVE_ABSENT",
        ))
        r_common = tuple(
            RCommonPairCertificate(
                row.history_ref, "R-COMMON", "1",
                r_common_fingerprint, r_common_fingerprint,
                "COMMON_FIXED",
            )
            for row in world.q_x
        )
        feasible = {
            row.history_ref: (zero_vector, one_vector)
            for row in world.q_x
        }
        g_a_structural_rules = (
            (
                GAStructuralTransitionRule(
                    atom=StructuralAtom(
                        "U", "TAU-FOCAL", "TRANSFORMATION", "1", 1,
                        (("role", "D2_FOCAL"), ("boundary_id", "BOUNDARY-1")),
                    ),
                    action="MODIFY",
                    vector_predicates=((0, 1.0),),
                ),
            )
            if theta_a_mode != "null" else ()
        )
        assignment_config = ThetaAPolicyAssignmentConfig(
            mechanism_id="DIRECT-GA-RANDOMIZATION",
            mechanism_version="1",
            randomization_salt=(seed_assignment.randomization_salt
                                if seed_assignment is not None else "DIRECT-GA-SALT"),
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
            mechanism_id=f"FUNCTIONAL-MECHANISM-{theta_a_mode.upper()}",
            mechanism_version="1",
            run_id=(seed_assignment.run_id if seed_assignment is not None
                    else f"RUN-INTERVAL-INTEGRATION-{theta_a_mode.upper()}"),
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
        fixture_need_states = (
            "FOCAL_INCLUSION", "FOCAL_EXCLUSION", "SEMANTIC_INDETERMINACY",
        )
        return {
            "world_config": world_config,
            "need_pre_z_stipulations": tuple(
                NeedPreZStipulation(
                    unit_id=unit.unit_id,
                    b1_id=f"FIXTURE-B1-{index:03d}",
                    service_instance_id=f"FIXTURE-SVC-{index:03d}",
                    contract_id="C10S-SVC-REQUEST-PROCESSOR",
                    contract_version="1.0.0",
                    instance_version=1,
                    package_version="B1-PACKAGE-001",
                    baseline_record_id=f"FIXTURE-BASELINE-{index:03d}",
                    baseline_time="t-1",
                    stipulation=fixture_need_states[(index - 1) % 3],
                    rule_version="NEED-RULE-TEST-001",
                    basis_ref=f"FIXTURE-RESERVED-STIPULATION-{index:03d}",
                )
                for index, unit in enumerate(world.units, start=1)
            ),
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
            "g_a_structural_rules": g_a_structural_rules,
            "g_a_structural_mapping_id": "TEST-GA-STRUCTURAL-MAP",
            "g_a_structural_mapping_version": "1",
            "feasible": feasible,
            "r_common": r_common,
            "assignment_config": assignment_config,
            "monitor_configs": {
                row.history_ref: monitor for row in world.q_x
            },
            # Deliberately point-sampled at t=0 only. The DGP truth path is
            # complete, but strict interval continuity is not observed.
            "point_s3_configs": {
                row.history_ref: S3ObservationConfig(
                    schedule=(Decimal("0"),),
                    capture_lags=(Decimal("0.1"),),
                    ingestion_lags=(Decimal("0.2"),),
                    kernel=(S3SequenceKernelRow(
                        truth_sequence=((True, "ADMIT", "STANDARD"),),
                        observed_sequences=(
                            (((True, "ADMIT", "STANDARD"),), 1.0),
                        ),
                    ),),
                    config_id="POINT-S3-INTEGRATION",
                    config_version="1",
                )
                for row in world.q_x
            },
            "monitor_seeds": (
                s3_seeds_by_unit(seed_assignment.s3_seed, tuple(unit.unit_id for unit in world.units))
                if seed_assignment is not None else {
                    unit.unit_id: 9000 + index
                    for index, unit in enumerate(world.units)
                }
            ),
        }

    def _run_pipeline(
        self, fixture, theta_a_confidence_level=None,
        theta_a_unit_independence_certified=None, point_s3=False,
    ):
        measurement_args = (
            {
                "s3_configs_by_history_ref": fixture["point_s3_configs"],
                "s3_seeds_by_unit": fixture["monitor_seeds"],
            }
            if point_s3 else
            {
                "interval_monitor_configs_by_history_ref": fixture["monitor_configs"],
                "interval_monitor_seeds_by_unit": fixture["monitor_seeds"],
            }
        )
        return materialize_c10s_complete_world_from_dgp(
            world_config=fixture["world_config"],
            d2_config=fixture["d2_config"],
            structural_config=fixture["structural_config"],
            reach_config=fixture["reach_config"],
            trajectory_config=fixture["trajectory_config"],
            functional_history_config=fixture["functional_config"],
            initial_state_by_unit_z=fixture["initial_by_unit_z"],
            initial_state_by_history=fixture["initial_by_history"],
            need_pre_z_stipulations=fixture["need_pre_z_stipulations"],
            grid=fixture["grid"],
            g_a0=fixture["g_a0"],
            g_a1=fixture["g_a1"],
            feasible_vectors_by_history=fixture["feasible"],
            r_common_certificates=fixture["r_common"],
            assignment_config=fixture["assignment_config"],
            estimand_version="1",
            outcome_version="VCONT-B1-1",
            evaluation_tolerance=0.25,
            **measurement_args,
            **fixture.get("theta_a_population_args", {}),
            theta_a_confidence_level=(None if point_s3 else theta_a_confidence_level),
            theta_a_unit_independence_certified=(
                theta_a_unit_independence_certified
                if theta_a_unit_independence_certified is not None
                else theta_a_confidence_level is not None
            ),
        )

    def test_structural_target_source_nonoverlap_runs_through_generated_world_to_evaluator(self):
        fixture = self._fixture(n_units=4)
        world = SyntheticWorldBuilder().generate(fixture["world_config"], fixture["d2_config"])
        extra_ref = "TARGET-ONLY-HISTORY-001"
        extra_unit_id = "TARGET-ONLY-UNIT-001"
        extra_qx = QXHistoryMass(extra_ref, "TARGET-X-001", "TARGET-H0-001", "TARGET-CC-001", 0.5)
        target_q_x = tuple(
            QXHistoryMass(row.history_ref, row.x_ref, row.h0_ref, row.c_c_ref, row.mass * 0.5)
            for row in world.q_x
        ) + (extra_qx,)
        source_unit_ids = {
            unit.d2_baseline.baseline_history_ref: unit.unit_id for unit in world.units
        }
        target_unit_ids = {**source_unit_ids, extra_ref: extra_unit_id}
        assignment_probabilities = dict(fixture["assignment_config"].probability_a1_by_history)
        positivity_failure_history = world.q_x[0].history_ref
        assignment_probabilities[positivity_failure_history] = 0.0
        fixture["assignment_config"] = replace(
            fixture["assignment_config"],
            probability_a1_by_history=tuple(sorted(assignment_probabilities.items())),
        )
        zero_vector = fixture["g_a0"][0].distribution[0][0]
        one_vector = fixture["g_a1"][0].distribution[0][0]
        fixture["g_a0"] = fixture["g_a0"] + (JointPolicyHistory(extra_ref, ((zero_vector, 1.0),)),)
        fixture["g_a1"] = fixture["g_a1"] + (JointPolicyHistory(extra_ref, ((one_vector, 1.0),)),)
        fixture["r_common"] = fixture["r_common"] + (
            RCommonPairCertificate(
                extra_ref, "R-COMMON", "1",
                fixture["r_common"][0].g_a0_fingerprint,
                fixture["r_common"][0].g_a1_fingerprint, "COMMON_FIXED",
            ),
        )
        fixture["feasible"][extra_ref] = (zero_vector, one_vector)
        fixture["initial_by_history"][extra_ref] = FunctionalState(
            True, "ADMIT", "STANDARD", "PROFILE-1", "1",
        )
        support = ThetaAStructuralSupportContract(
            "SYNTHETIC-TARGET-SOURCE-SUPPORT-001", "1",
            digest(target_q_x), digest(world.q_x),
            tuple(
                ThetaAStructuralSupportRow(
                    row.history_ref, row.mass, 1.0 / len(world.units),
                    True, True, True, assignment_probabilities[row.history_ref],
                ) for row in target_q_x[:-1]
            ) + (ThetaAStructuralSupportRow(
                extra_ref, 0.5, 0.0, True, True, True, None,
            ),),
        )
        source_anchor = world.units[0]
        target_materialization = SyntheticThetaATargetHistory(
            q_x=extra_qx,
            potential_unit_id=extra_unit_id,
            x_values=source_anchor.x,
            h0_value=source_anchor.h0,
            c_c_values=source_anchor.c_c,
            initial_functional_state=fixture["initial_by_history"][extra_ref],
            provenance_ref="SYNTHETIC-TEST-DGP-TARGET-BASELINE-001",
        )
        fixture["theta_a_population_args"] = {
            "theta_a_q_x": target_q_x,
            "theta_a_unit_id_by_history": target_unit_ids,
            "theta_a_structural_support_contract": support,
            "theta_a_target_history_materializations": (target_materialization,),
        }
        with self.assertRaisesRegex(ContractError, "every and only target-only histories"):
            incomplete_fixture = dict(fixture)
            incomplete_fixture["theta_a_population_args"] = {
                key: value for key, value in fixture["theta_a_population_args"].items()
                if key != "theta_a_target_history_materializations"
            }
            self._run_pipeline(incomplete_fixture)
        with self.assertRaisesRegex(ContractError, "dimensions must match"):
            replace(
                target_materialization,
                x_values=target_materialization.x_values + (999.0,),
            ).validate(
                source_world=world,
                allowed_h0_values={label for label, _ in fixture["world_config"].h0_distribution},
            )
        with self.assertRaisesRegex(ContractError, "X/H0/C_c anchors"):
            replace(target_materialization, h0_value="OUTSIDE-DGP-SUPPORT").validate(
                source_world=world,
                allowed_h0_values={label for label, _ in fixture["world_config"].h0_distribution},
            )
        result = self._run_pipeline(fixture)
        self.assertEqual(len(result.world.units), 4)
        self.assertEqual(len(result.theta_a_truth.event_history_manifest), 10)
        # The four source units are randomized; the target-only synthetic
        # history is not silently added to the source assignment roster.
        self.assertEqual(len(result.theta_a_assignments.assignments), 4)
        self.assertEqual(result.analyzer_result.identification, "NOT_IDENTIFIED")
        self.assertEqual(
            result.analyzer_result.abstention_reason,
            "TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT+SOURCE_ASSIGNMENT_POSITIVITY_FAILURE",
        )
        self.assertEqual(result.analyzer_result.missing_target_histories, (extra_ref,))
        self.assertEqual(
            result.analyzer_result.assignment_positivity_failure_histories,
            (positivity_failure_history,),
        )
        self.assertAlmostEqual(result.analyzer_result.target_q_x_coverage, 0.5)
        self.assertTrue(result.evaluator_result.truth_within_bounds)
        self.assertTrue(result.evaluator_result.correct_adjudication)
        self.assertEqual(result.evaluator_result.disposition, "CORRECT_ABSTENTION")

    def test_target_only_support_without_assignment_failure_abstains_end_to_end(self):
        fixture = self._fixture(n_units=4)
        world = SyntheticWorldBuilder().generate(fixture["world_config"], fixture["d2_config"])
        extra_ref = "TARGET-ONLY-HISTORY-001"
        extra_unit_id = "TARGET-ONLY-UNIT-001"
        extra_qx = QXHistoryMass(extra_ref, "TARGET-X-001", "TARGET-H0-001", "TARGET-CC-001", 0.5)
        target_q_x = tuple(
            QXHistoryMass(row.history_ref, row.x_ref, row.h0_ref, row.c_c_ref, row.mass * 0.5)
            for row in world.q_x
        ) + (extra_qx,)
        source_unit_ids = {
            unit.d2_baseline.baseline_history_ref: unit.unit_id for unit in world.units
        }
        target_unit_ids = {**source_unit_ids, extra_ref: extra_unit_id}
        assignment_probabilities = dict(fixture["assignment_config"].probability_a1_by_history)
        zero_vector = fixture["g_a0"][0].distribution[0][0]
        one_vector = fixture["g_a1"][0].distribution[0][0]
        fixture["g_a0"] = fixture["g_a0"] + (JointPolicyHistory(extra_ref, ((zero_vector, 1.0),)),)
        fixture["g_a1"] = fixture["g_a1"] + (JointPolicyHistory(extra_ref, ((one_vector, 1.0),)),)
        fixture["r_common"] = fixture["r_common"] + (
            RCommonPairCertificate(
                extra_ref, "R-COMMON", "1",
                fixture["r_common"][0].g_a0_fingerprint,
                fixture["r_common"][0].g_a1_fingerprint, "COMMON_FIXED",
            ),
        )
        fixture["feasible"][extra_ref] = (zero_vector, one_vector)
        fixture["initial_by_history"][extra_ref] = FunctionalState(
            True, "ADMIT", "STANDARD", "PROFILE-1", "1",
        )
        support = ThetaAStructuralSupportContract(
            "SYNTHETIC-TARGET-SOURCE-SUPPORT-001", "1",
            digest(target_q_x), digest(world.q_x),
            tuple(
                ThetaAStructuralSupportRow(
                    row.history_ref, row.mass, 1.0 / len(world.units),
                    True, True, True, assignment_probabilities[row.history_ref],
                ) for row in target_q_x[:-1]
            ) + (ThetaAStructuralSupportRow(
                extra_ref, 0.5, 0.0, True, True, True, None,
            ),),
        )
        source_anchor = world.units[0]
        target_materialization = SyntheticThetaATargetHistory(
            q_x=extra_qx,
            potential_unit_id=extra_unit_id,
            x_values=source_anchor.x,
            h0_value=source_anchor.h0,
            c_c_values=source_anchor.c_c,
            initial_functional_state=fixture["initial_by_history"][extra_ref],
            provenance_ref="SYNTHETIC-TEST-DGP-TARGET-BASELINE-001",
        )
        fixture["theta_a_population_args"] = {
            "theta_a_q_x": target_q_x,
            "theta_a_unit_id_by_history": target_unit_ids,
            "theta_a_structural_support_contract": support,
            "theta_a_target_history_materializations": (target_materialization,),
        }
        with self.assertRaisesRegex(ContractError, "every and only target-only histories"):
            incomplete_fixture = dict(fixture)
            incomplete_fixture["theta_a_population_args"] = {
                key: value for key, value in fixture["theta_a_population_args"].items()
                if key != "theta_a_target_history_materializations"
            }
            self._run_pipeline(incomplete_fixture)
        with self.assertRaisesRegex(ContractError, "dimensions must match"):
            replace(
                target_materialization,
                x_values=target_materialization.x_values + (999.0,),
            ).validate(
                source_world=world,
                allowed_h0_values={label for label, _ in fixture["world_config"].h0_distribution},
            )
        with self.assertRaisesRegex(ContractError, "X/H0/C_c anchors"):
            replace(target_materialization, h0_value="OUTSIDE-DGP-SUPPORT").validate(
                source_world=world,
                allowed_h0_values={label for label, _ in fixture["world_config"].h0_distribution},
            )
        result = self._run_pipeline(fixture)
        self.assertEqual(len(result.world.units), 4)
        self.assertEqual(len(result.theta_a_truth.event_history_manifest), 10)
        self.assertEqual(len(result.theta_a_assignments.assignments), 4)
        self.assertEqual(result.analyzer_result.identification, "NOT_IDENTIFIED")
        self.assertEqual(
            result.analyzer_result.abstention_reason,
            "TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT",
        )
        self.assertEqual(result.analyzer_result.missing_target_histories, (extra_ref,))
        self.assertEqual(result.analyzer_result.assignment_positivity_failure_histories, ())
        self.assertAlmostEqual(result.analyzer_result.target_q_x_coverage, 0.5)
        self.assertTrue(result.evaluator_result.truth_within_bounds)
        self.assertTrue(result.evaluator_result.correct_adjudication)
        self.assertEqual(result.evaluator_result.disposition, "CORRECT_ABSTENTION")

    def test_source_support_strict_superset_of_target_is_benign_end_to_end(self):
        # Use enough predeclared units that the fixed target subset retains
        # realized support in both randomized arms; this avoids conflating
        # source/target support compatibility with a tiny-sample arm accident.
        fixture = self._fixture(n_units=8)
        world = SyntheticWorldBuilder().generate(fixture["world_config"], fixture["d2_config"])
        excluded_source_history = world.q_x[-1].history_ref
        target_rows = world.q_x[:-1]
        target_mass = 1.0 / len(target_rows)
        target_q_x = tuple(
            QXHistoryMass(row.history_ref, row.x_ref, row.h0_ref, row.c_c_ref, target_mass)
            for row in target_rows
        )
        target_refs = {row.history_ref for row in target_q_x}
        target_unit_ids = {
            unit.d2_baseline.baseline_history_ref: unit.unit_id
            for unit in world.units
            if unit.d2_baseline.baseline_history_ref in target_refs
        }
        support = ThetaAStructuralSupportContract(
            "SYNTHETIC-SOURCE-SUPERSET-TARGET-SUBSET-001", "1",
            digest(target_q_x), digest(world.q_x),
            tuple(
                ThetaAStructuralSupportRow(
                    row.history_ref, row.mass, 1.0 / len(world.units),
                    True, True, True,
                    dict(fixture["assignment_config"].probability_a1_by_history)[row.history_ref],
                ) for row in target_q_x
            ),
        )
        fixture["theta_a_population_args"] = {
            "theta_a_q_x": target_q_x,
            "theta_a_unit_id_by_history": target_unit_ids,
            "theta_a_structural_support_contract": support,
        }
        result = self._run_pipeline(fixture)
        self.assertEqual(len(world.q_x), 8)
        self.assertEqual(len(result.theta_a_truth.event_history_manifest), 14)
        self.assertEqual(len(result._policy_histories), 16)
        # Assignment/evidence materialization retains all eight source units;
        # target standardization is applied later by the Analyzer.
        self.assertEqual(len(result.theta_a_assignments.assignments), 8)
        self.assertEqual(len(result.s3_records), 16)
        self.assertEqual(result.analyzer_result.total_interval_count, 14)
        self.assertEqual(result.analyzer_result.missing_interval_count, 0)
        self.assertEqual(
            result.analyzer_contract.source_only_history_refs,
            (excluded_source_history,),
        )
        self.assertEqual(sum(result.analyzer_result.assigned_arm_unit_counts), 7)
        self.assertNotEqual(
            result.analyzer_contract.g_a0_sha256,
            result.analyzer_contract.target_g_a0_sha256,
        )
        self.assertNotEqual(
            result.analyzer_contract.g_a1_sha256,
            result.analyzer_contract.target_g_a1_sha256,
        )
        self.assertEqual(
            result.theta_a_truth.theta_a_truth.g_a0_fingerprint,
            result.analyzer_contract.target_g_a0_sha256,
        )
        self.assertEqual(
            result.theta_a_truth.theta_a_truth.g_a1_fingerprint,
            result.analyzer_contract.target_g_a1_sha256,
        )
        self.assertNotIn(excluded_source_history, target_refs)
        self.assertEqual(
            result.analyzer_result.identification, "IDENTIFIED",
            f"diagnostic: reason={result.analyzer_result.abstention_reason}; "
            f"arms={result.analyzer_result.assigned_arm_unit_counts}; "
            f"missing={result.analyzer_result.missing_target_histories}; "
            f"intervals={result.analyzer_result.missing_interval_count}/"
            f"{result.analyzer_result.total_interval_count}",
        )
        self.assertEqual(result.analyzer_result.abstention_reason, "")
        self.assertEqual(result.analyzer_result.missing_target_histories, ())
        self.assertEqual(result.analyzer_result.assignment_positivity_failure_histories, ())
        self.assertAlmostEqual(result.analyzer_result.target_q_x_coverage, 1.0)
        self.assertTrue(result.evaluator_result.truth_within_bounds)
        self.assertTrue(result.evaluator_result.correct_adjudication)
        self.assertEqual(result.evaluator_result.disposition, "POINT_RECOVERED")

    def test_source_assignment_positivity_failure_runs_through_generated_world_to_evaluator(self):
        fixture = self._fixture(n_units=4)
        world = SyntheticWorldBuilder().generate(fixture["world_config"], fixture["d2_config"])
        probabilities = dict(fixture["assignment_config"].probability_a1_by_history)
        failed_history = world.q_x[0].history_ref
        probabilities[failed_history] = 0.0
        fixture["assignment_config"] = replace(
            fixture["assignment_config"],
            probability_a1_by_history=tuple(sorted(probabilities.items())),
        )
        support = ThetaAStructuralSupportContract(
            "SYNTHETIC-ASSIGNMENT-POSITIVITY-001", "1",
            digest(world.q_x), digest(world.q_x),
            tuple(
                ThetaAStructuralSupportRow(
                    row.history_ref, row.mass, row.mass, True, True, True,
                    probabilities[row.history_ref],
                ) for row in world.q_x
            ),
        )
        fixture["theta_a_population_args"] = {
            "theta_a_structural_support_contract": support,
        }
        result = self._run_pipeline(fixture)
        self.assertEqual(result.analyzer_result.identification, "NOT_IDENTIFIED")
        self.assertEqual(result.analyzer_result.abstention_reason, "SOURCE_ASSIGNMENT_POSITIVITY_FAILURE")
        self.assertEqual(result.analyzer_result.missing_target_histories, ())
        self.assertEqual(result.analyzer_result.assignment_positivity_failure_histories, (failed_history,))
        self.assertTrue(result.evaluator_result.truth_within_bounds)
        self.assertTrue(result.evaluator_result.correct_adjudication)
        self.assertEqual(result.evaluator_result.disposition, "CORRECT_ABSTENTION")

    def test_theta_a_nmr_protocol_is_wired_through_complete_world_and_evaluator(self):
        scenario = ThetaACalibrationScenario(
            scenario_id="THETA_A_POSITIVE_INTERVAL_FIXTURE",
            scenario_version="1.0",
            world_version="1",
            dgp_id="DGP-INTERVAL-INTEGRATION-INTERACTION",
            dgp_version="1",
            roster_version="1",
            unit_id_prefix="U",
            expected_identification="IDENTIFIED",
            unit_independence_certified=True,
            independence_basis=(
                "fixture units have independently generated potential histories; "
                "both assignment stages use independent unit-level draws and no interference"
            ),
        )
        design = ThetaACalibrationDesign(
            scenario_specs=(scenario,),
            n_grid=(32,),
            outer_worlds_m=2,
            assignment_replicates_r=2,
            confidence_level=0.95,
            namespace="theta-a-world-pipeline-integration-test-v1",
        )
        assignments = build_theta_a_seed_bank(design, "calibration")
        records = []
        for assignment in assignments:
            fixture = self._fixture("positive", seed_assignment=assignment)
            inference_options = theta_a_pipeline_inference_options(design, scenario)
            result = self._run_pipeline(fixture, **inference_options)
            records.append(capture_theta_a_replicate(
                result, assignment, scenario,
                requested_confidence_level=design.confidence_level,
            ))
        summaries = summarize_theta_a_calibration(
            design, assignments, records, bank="calibration",
        )
        self.assertEqual(len(assignments), 4)
        self.assertEqual(len(records), 4)
        self.assertEqual(len(summaries), 1)
        summary = summaries[0]
        self.assertEqual(summary.outer_worlds_m, 2)
        self.assertEqual(summary.assignment_replicates_r, 2)
        metrics = {item.metric: item for item in summary.metrics}
        self.assertEqual(metrics["identification_rate"].mean, 1.0)
        self.assertIsNotNone(metrics["point_bias"].mean)
        self.assertIsNotNone(metrics["interval_coverage"].mean)
        self.assertEqual(
            len({row.world_id for row in records}), 2,
            "M must contain distinct outer worlds while R stays within each world",
        )
        for world_id in {row.world_id for row in records}:
            group = [row for row in records if row.world_id == world_id]
            self.assertEqual(len(group), 2)
            self.assertEqual(len({row.run_id for row in group}), 2)

    def test_point_s3_world_pipeline_abstains_with_truth_covered(self):
        fixture = self._fixture("positive")
        result = self._run_pipeline(fixture, point_s3=True)

        self.assertEqual(result.sealed_evidence.manifest["temporal_resolution"], "POINT_SAMPLE")
        self.assertEqual(result.analyzer_result.temporal_resolution, "POINT_SAMPLE")
        self.assertEqual(result.analyzer_result.identification, "PARTIALLY_IDENTIFIED")
        self.assertEqual(
            result.analyzer_result.abstention_reason,
            "STRICT_VCONT_NOT_OBSERVED_BY_POINT_SAMPLES",
        )
        self.assertIsNone(result.analyzer_result.point_estimate)
        self.assertEqual(result.analyzer_result.lower_bound, -1.0)
        self.assertEqual(result.analyzer_result.upper_bound, 1.0)
        self.assertAlmostEqual(result.evaluator_result.truth, 0.5)
        self.assertTrue(result.evaluator_result.truth_within_bounds)
        self.assertTrue(result.evaluator_result.correct_adjudication)
        self.assertEqual(result.evaluator_result.disposition, "BOUNDS_COVER_TRUTH")

    def test_point_s3_single_unit_world_adjudicates_missing_realized_arm(self):
        # Positivity of the assignment mechanism is preserved (p=0.5).
        # With one realized unit, one arm is necessarily absent; this tests
        # realized-arm support failure, not structural assignment positivity.
        fixture = self._fixture("positive", n_units=1)
        result = self._run_pipeline(fixture, point_s3=True)

        self.assertEqual(result.analyzer_result.identification, "INDETERMINATE")
        self.assertEqual(
            result.analyzer_result.abstention_reason,
            "REALIZED_GA_ARM_SUPPORT_MISSING",
        )
        self.assertIsNone(result.analyzer_result.point_estimate)
        self.assertEqual(result.analyzer_result.lower_bound, -1.0)
        self.assertEqual(result.analyzer_result.upper_bound, 1.0)
        self.assertEqual(sum(result.analyzer_result.assigned_arm_unit_counts), 1)
        self.assertIn(0, result.analyzer_result.assigned_arm_unit_counts)
        self.assertAlmostEqual(result.evaluator_result.truth, 0.5)
        self.assertTrue(result.evaluator_result.truth_within_bounds)
        self.assertTrue(result.evaluator_result.correct_adjudication)
        self.assertEqual(result.evaluator_result.disposition, "CORRECT_ABSTENTION")

    def test_two_stage_inference_is_wired_through_complete_world_and_evaluator(self):
        fixture = self._fixture("positive")
        result = self._run_pipeline(fixture, theta_a_confidence_level=0.95)
        self.assertEqual(
            result.analyzer_result.inference_method,
            "HOEFFDING_TWO_STAGE_BOUNDED_HT_V1",
        )
        self.assertEqual(result.analyzer_result.inference_confidence_level, 0.95)
        self.assertIsNotNone(result.analyzer_result.inference_lower_bound)
        self.assertIsNotNone(result.analyzer_result.inference_upper_bound)
        self.assertIsNotNone(result.evaluator_result.inference_truth_covered)
        self.assertEqual(
            dict(result.analyzer_contract.probability_a1_by_history),
            dict(fixture["assignment_config"].probability_a1_by_history),
        )

    def test_dgp_world_flows_through_realized_interval_evidence_and_reserved_oracle(self):
        fixture = self._fixture("positive")
        result = self._run_pipeline(fixture)
        self.assertEqual(len(result.need_pre_z_truth.records), fixture["world_config"].n_units)
        self.assertEqual(
            {row.need_truth_state for row in result.need_pre_z_truth.records},
            {1, 0, "?"},
        )

        # The DGP-generated potential histories, not caller-supplied histories,
        # feed the reserved oracle and the realized-assignment selection.
        self.assertEqual(len(result.d2_histories_by_unit_z), 64)
        self.assertEqual(len(result.theta_a_truth.event_history_manifest), 64)
        self.assertAlmostEqual(result.theta_a_truth.theta_a_truth.theta_a_truth, 0.5)
        # D2 has a distinct direct package path with the opposite sign.
        # Its ITT-Z must never be relabelled as the focal accessibility effect.
        self.assertAlmostEqual(result.d2_vcont_truth.finite_population_itt_z_v_cont, -0.5)
        self.assertNotAlmostEqual(
            result.d2_vcont_truth.finite_population_itt_z_v_cont,
            result.theta_a_truth.theta_a_truth.theta_a_truth,
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
        self.assertNotEqual(
            fixture["functional_config"].mechanism_id,
            alternative_fixture["functional_config"].mechanism_id,
        )
        self.assertNotEqual(
            fixture["r_common"][0].g_a0_fingerprint,
            alternative_fixture["r_common"][0].g_a0_fingerprint,
        )
        self.assertEqual(result.world.world_id, alternative_result.world.world_id)
        self.assertEqual(result.world.q_x, alternative_result.world.q_x)
        self.assertAlmostEqual(alternative_result.theta_a_truth.theta_a_truth.theta_a_truth, 0.0)
        self.assertAlmostEqual(
            result.theta_a_truth.theta_a_truth.theta_a_truth - alternative_result.theta_a_truth.theta_a_truth.theta_a_truth,
            0.5,
        )
        self.assertAlmostEqual(alternative_result.d2_vcont_truth.finite_population_itt_z_v_cont, -0.5)
        # The alternative pathway is active in the common policy regime for
        # both g_A arms. It masks the focal contrast but does not, by itself,
        # make that contrast unidentified: the DGP truth is zero and the
        # observation/assignment support remains complete.
        self.assertEqual(alternative_result.analyzer_result.identification, "IDENTIFIED")
        self.assertAlmostEqual(alternative_result.evaluator_result.truth, 0.0)
        self.assertTrue(alternative_result.evaluator_result.correct_adjudication)
        self.assertEqual(
            alternative_result.evaluator_result.disposition,
            "POINT_RECOVERED",
        )

    def test_null_and_negative_focal_scenarios_are_separately_generated(self):
        expected_truth = {"null": 0.0, "negative": -0.5}
        results = {}
        for mode, truth in expected_truth.items():
            with self.subTest(theta_a_mode=mode):
                result = self._run_pipeline(self._fixture(mode))
                results[mode] = result
                self.assertAlmostEqual(result.theta_a_truth.theta_a_truth.theta_a_truth, truth)
                self.assertAlmostEqual(result.d2_vcont_truth.finite_population_itt_z_v_cont, -0.5)
                self.assertEqual(result.analyzer_result.identification, "IDENTIFIED")
                self.assertEqual(result.evaluator_result.truth, truth)
                self.assertIn(
                    result.evaluator_result.disposition,
                    ("POINT_RECOVERED", "POINT_RECOVERY_FAILED"),
                )
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
            g_a_structural_rules=fixture["g_a_structural_rules"],
            g_a_structural_mapping_id=fixture["g_a_structural_mapping_id"],
            g_a_structural_mapping_version=fixture["g_a_structural_mapping_version"],
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
        self.assertEqual(len(result.factorial_structural_potentials), 64)
        self.assertEqual(len(result.factorial_reach_potentials), 64)
        self.assertEqual(len(result.factorial_trajectories), 64)
        self.assertEqual(
            {(row.mapping_id, row.mapping_version)
             for row in result.factorial_structural_potentials.values()},
            {("TEST-GA-STRUCTURAL-MAP", "1")},
        )
        for key, potential in result.factorial_structural_potentials.items():
            reach = result.factorial_reach_potentials[key]
            trajectory = result.factorial_trajectories[(*key, "TARGET")]
            if potential.vector[0] == 1.0:
                self.assertEqual(potential.delta.delta_state, 1)
                self.assertEqual(dict(reach.post.target_states)["TARGET"], 1)
                self.assertEqual(trajectory.trajectory_status, "COMPLETED")
            else:
                self.assertEqual(potential.delta.delta_state, 0)
                self.assertEqual(dict(reach.post.target_states)["TARGET"], 0)
                self.assertEqual(trajectory.trajectory_status, "NOT_REACHABLE")
        self.assertEqual(
            result.accessibility_attribution_status,
            "GA_TO_DELTA_T_ACC_REACH_TRAJECTORY_MATERIALIZED_VALUE_BRIDGE_OPEN",
        )
        with self.assertRaises(ContractError):
            result.require_accessibility_attribution()
        self.assertEqual(len(result.assignment_bundle.assignments), 32)
        self.assertEqual(
            {row.cell_id for row in result.assignment_bundle.assignments},
            {"00", "10", "01", "11"},
        )
        truth = result.reserved_truth
        # Package-level D2 ITT-Z is retained as a separate potential-outcome
        # contrast; it is not the focal direct-g_A effect or A×M interaction.
        self.assertAlmostEqual(result.d2_vcont_truth.finite_population_itt_z_v_cont, -0.5)
        self.assertNotAlmostEqual(
            result.d2_vcont_truth.finite_population_itt_z_v_cont,
            truth.theta_a_given_m0,
        )
        # DEC-C10-100/102 aggregate equal-duration, strictly adjudicated
        # intervals. The A=0 interruption at t=1 affects the second block,
        # so its V_cont is 1/2 rather than a horizon-wide binary zero.
        self.assertAlmostEqual(truth.cell_means[0], 0.5)
        self.assertAlmostEqual(truth.cell_means[1], 1.0)
        self.assertAlmostEqual(truth.cell_means[2], 0.0)
        self.assertAlmostEqual(truth.cell_means[3], 0.0)
        self.assertAlmostEqual(truth.theta_a_given_m0, 0.5)
        self.assertAlmostEqual(truth.theta_a_given_m1, 0.0)
        self.assertAlmostEqual(truth.theta_am_interaction, -0.5)
        self.assertEqual(len(result.analyzer_result.contrasts), 3)
        self.assertEqual(len(result.evaluator_result.absolute_errors), 3)
        for error, observed, expected_truth in zip(
            result.evaluator_result.absolute_errors,
            result.analyzer_result.contrasts,
            (truth.theta_a_given_m0, truth.theta_a_given_m1, truth.theta_am_interaction),
        ):
            self.assertAlmostEqual(error, abs(observed.point_estimate - expected_truth))

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

        # All interval values missing: the Analyzer must abstain from point
        # identification and return an estimator missingness envelope. This
        # envelope is not a confidence interval or causal truth bound.
        missing_records = tuple(
            replace(row, observed_compliance=None, observation_status="MISSING")
            for row in result.interval_observations
        )
        missing_evidence = FactorialIntervalSealer().seal(
            factorial_candidate_from_records(missing_records)
        )
        partial_analysis = FactorialObservationAnalyzer().analyze(
            missing_evidence, result.analysis_contract,
        )
        self.assertEqual(
            tuple(row.identification for row in partial_analysis.contrasts),
            ("PARTIALLY_IDENTIFIED",) * 3,
        )
        self.assertTrue(all(
            row.point_estimate is None
            and row.lower_bound is not None
            and row.upper_bound is not None
            for row in partial_analysis.contrasts
        ))
        partial_evaluation = evaluate_factorial_analysis(
            result.reserved_truth, missing_evidence, partial_analysis,
            result.assignment_bundle, tolerance=0.25,
        )
        self.assertTrue(partial_evaluation.correct_adjudication)

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
            g_a_structural_rules=fixture["g_a_structural_rules"],
            g_a_structural_mapping_id=fixture["g_a_structural_mapping_id"],
            g_a_structural_mapping_version=fixture["g_a_structural_mapping_version"],
            feasible_vectors_by_history=fixture["feasible"],
            r_common_certificates=fixture["r_common"],
            assignment_config=assignment,
            grids_by_history_ref=grids,
            interval_monitor_configs_by_history_ref=fixture["monitor_configs"],
            interval_monitor_seeds_by_unit=fixture["monitor_seeds"],
            estimand_version="1",
            evaluation_tolerance=2.0,
        )
        self.assertAlmostEqual(null_result.reserved_truth.theta_a_given_m0, 0.5)
        self.assertAlmostEqual(null_result.reserved_truth.theta_a_given_m1, 0.5)
        self.assertAlmostEqual(null_result.reserved_truth.theta_am_interaction, 0.0)
        self.assertTrue(all(
            row.delta.delta_state == (1 if row.vector[0] == 1.0 else 0)
            for row in null_result.factorial_structural_potentials.values()
        ))
        self.assertEqual(len(null_result.evaluator_result.absolute_errors), 3)


    def test_dual_cohort_pipeline_keeps_ittz_and_factorial_assignments_disjoint(self):
        fixture = self._fixture("positive")
        d2_world_config = replace(
            fixture["world_config"],
            world_id="WORLD-INTERVAL-INTEGRATION-D2-COHORT",
            roster_id="ROSTER-INTERVAL-INTEGRATION-D2-COHORT",
            unit_id_prefix="D2U",
            seed=fixture["world_config"].seed + 101,
        )
        d2_world = SyntheticWorldBuilder().generate(
            d2_world_config, fixture["d2_config"],
        )
        initial = FunctionalState(
            True, "ADMIT", "STANDARD", "PROFILE-1", "1",
        )
        d2_initial_by_unit_z = {
            (unit.unit_id, z): initial
            for unit in d2_world.units for z in (0, 1)
        }
        factorial_world = SyntheticWorldBuilder().generate(
            fixture["world_config"], fixture["d2_config"],
        )
        distinct_d2_initial_states = dict(d2_initial_by_unit_z)
        distinct_d2_initial_states[(d2_world.units[0].unit_id, 0)] = replace(
            initial, admission_behavior="NO_ADMISSION",
        )
        _validate_cohort_initial_states(
            factorial_world, fixture["initial_by_unit_z"], "factorial",
        )
        _validate_cohort_initial_states(
            d2_world, distinct_d2_initial_states, "D2",
        )
        self.assertNotEqual(
            fixture["initial_by_unit_z"][(factorial_world.units[0].unit_id, 0)],
            distinct_d2_initial_states[(d2_world.units[0].unit_id, 0)],
        )
        with self.assertRaises(ContractError):
            _validate_cohort_initial_states(
                d2_world, {}, "D2",
            )
        d2_assignment = D2ObservedAssignmentConfig(
            mechanism_id="D2-PACKAGE-Z-RANDOMIZATION",
            mechanism_version="1",
            randomization_salt="D2-PACKAGE-Z-SALT-INDEPENDENT",
            probability_z1_by_history=tuple(
                (row.history_ref, 0.5) for row in d2_world.q_x
            ),
        )
        factorial_assignment_config = FactorialAssignmentConfig(
            mechanism_id="FACTORIAL-AxM-DUAL-COHORT",
            mechanism_version="1",
            factor_m_id="FACTOR-M-DUAL-COHORT",
            factor_m_version="1",
            randomization_salt="FACTORIAL-AxM-DUAL-COHORT-SALT",
            probability_by_history=tuple(
                (row.history_ref, 0.25, 0.25, 0.25, 0.25)
                for row in factorial_world.q_x
            ),
        )
        d2_monitor_seeds = {
            unit.unit_id: 19000 + index
            for index, unit in enumerate(d2_world.units)
        }
        monitor = next(iter(fixture["monitor_configs"].values()))
        trajectory_rule = FunctionalHistoryRule(
            rule_id="DUAL-TRAJECTORY-COMPLETION-TO-B1",
            source="TRAJECTORY",
            event_time=Decimal("1.5"),
            causal_family="TRAJECTORY_EXECUTION_TO_B1_ADMISSION",
            provenance_ref="FUNCTIONAL-DGP#DUAL-TRAJECTORY-COMPLETION-TO-B1",
            set_admission="NO_ADMISSION",
            trajectory_target_state="TARGET",
            trajectory_field="trajectory_status",
            trajectory_value="COMPLETED",
        )
        dual_functional_config = replace(
            fixture["functional_config"],
            rules=fixture["functional_config"].rules + (trajectory_rule,),
        )
        def stipulations_for(world, prefix):
            states = (
                ("FOCAL_INCLUSION", "FOCAL_EXCLUSION", "SEMANTIC_INDETERMINACY")
                if prefix == "FACTORIAL"
                else ("FOCAL_EXCLUSION", "SEMANTIC_INDETERMINACY", "FOCAL_INCLUSION")
            )
            return tuple(
                NeedPreZStipulation(
                    unit_id=unit.unit_id,
                    b1_id=f"{prefix}-B1-{index:03d}",
                    service_instance_id=f"{prefix}-SVC-{index:03d}",
                    contract_id="C10S-SVC-REQUEST-PROCESSOR",
                    contract_version="1.0.0",
                    instance_version=1,
                    package_version="B1-PACKAGE-001",
                    baseline_record_id=f"{prefix}-BASELINE-{index:03d}",
                    baseline_time="t-1",
                    stipulation=states[(index - 1) % 3],
                    rule_version="NEED-RULE-TEST-001",
                    basis_ref=f"{prefix}-RESERVED-STIPULATION-{index:03d}",
                )
                for index, unit in enumerate(world.units, start=1)
            )

        result = materialize_c10s_dual_cohort_world_from_dgp(
            factorial_world_config=fixture["world_config"],
            d2_world_config=d2_world_config,
            d2_config=fixture["d2_config"],
            structural_config=fixture["structural_config"],
            reach_config=fixture["reach_config"],
            trajectory_config=fixture["trajectory_config"],
            functional_history_config=dual_functional_config,
            factorial_initial_state_by_unit_z=fixture["initial_by_unit_z"],
            d2_initial_state_by_unit_z=d2_initial_by_unit_z,
            factorial_need_pre_z_stipulations=stipulations_for(factorial_world, "FACTORIAL"),
            d2_need_pre_z_stipulations=stipulations_for(d2_world, "D2"),
            initial_state_by_history=fixture["initial_by_history"],
            grid=fixture["grid"],
            g_a0=fixture["g_a0"],
            g_a1=fixture["g_a1"],
            g_a_structural_rules=fixture["g_a_structural_rules"],
            g_a_structural_mapping_id=fixture["g_a_structural_mapping_id"],
            g_a_structural_mapping_version=fixture["g_a_structural_mapping_version"],
            feasible_vectors_by_history=fixture["feasible"],
            r_common_certificates=fixture["r_common"],
            factorial_assignment_config=factorial_assignment_config,
            d2_assignment_config=d2_assignment,
            factorial_grids_by_history_ref=dict.fromkeys(
                fixture["monitor_configs"], fixture["grid"],
            ),
            factorial_interval_monitor_configs_by_history_ref=fixture["monitor_configs"],
            factorial_interval_monitor_seeds_by_unit=fixture["monitor_seeds"],
            d2_interval_monitor_configs_by_history_ref=dict.fromkeys(
                (row.history_ref for row in d2_world.q_x), monitor,
            ),
            d2_interval_monitor_seeds_by_unit=d2_monitor_seeds,
            estimand_version="1",
            evaluation_tolerance=0.25,
        )
        self.assertEqual(
            len(result.factorial_need_pre_z_truth.records),
            len(result.factorial_cohort.world.units),
        )
        self.assertEqual(
            len(result.d2_need_pre_z_truth.records), len(result.d2_world.units),
        )
        self.assertNotEqual(
            tuple(row.need_truth_state for row in result.factorial_need_pre_z_truth.records),
            tuple(row.need_truth_state for row in result.d2_need_pre_z_truth.records),
        )
        factorial_ids = {unit.unit_id for unit in result.factorial_cohort.world.units}
        d2_ids = {unit.unit_id for unit in result.d2_world.units}
        self.assertFalse(factorial_ids & d2_ids)
        self.assertNotEqual(
            result.factorial_cohort.world.seed_commitment_sha256,
            result.d2_world.seed_commitment_sha256,
        )
        self.assertEqual(
            result.factorial_cohort.accessibility_attribution_status,
            "GA_TO_DELTA_T_ACC_REACH_TRAJECTORY_MATERIALIZED_VALUE_BRIDGE_OPEN",
        )
        with self.assertRaises(ContractError):
            result.factorial_cohort.require_accessibility_attribution()
        self.assertEqual(len(result.factorial_initial_states_by_unit_z), 64)
        self.assertEqual(len(result.d2_initial_states_by_unit_z), 64)
        self.assertEqual(len(result.d2_structural_pairs), 64)
        self.assertEqual(len(result.d2_structural_deltas), 64)
        self.assertEqual(len(result.d2_reachability.contrasts), 64)
        self.assertEqual(len(result.factorial_cohort.structural_deltas), 64)
        self.assertEqual(len(result.factorial_cohort.factorial_structural_potentials), 64)
        self.assertEqual(len(result.factorial_cohort.factorial_reach_potentials), 64)
        self.assertEqual(len(result.factorial_cohort.factorial_trajectories), 64)
        self.assertEqual(len(result.d2_trajectories.trajectories), 64)
        d2_histories = result.d2_event_histories_by_unit_z
        factorial_d2_histories = result.factorial_cohort.d2_event_histories_by_unit_z
        for cohort_ids, histories in (
            (d2_ids, d2_histories), (factorial_ids, factorial_d2_histories),
        ):
            self.assertTrue(all(
                any(change.causal_family == "D2_DIRECT_PACKAGE_PATH"
                    for change in histories[(unit_id, 1)].transitions)
                and not any(change.causal_family == "D2_DIRECT_PACKAGE_PATH"
                            for change in histories[(unit_id, 0)].transitions)
                for unit_id in cohort_ids
            ))
        for key, history in result.factorial_cohort.factorial_potential_histories.items():
            vector_key = key[:3]
            trajectory = result.factorial_cohort.factorial_trajectories[
                (*vector_key, "TARGET")
            ]
            has_trajectory_change = any(
                change.causal_family == "TRAJECTORY_EXECUTION_TO_B1_ADMISSION"
                for change in history.transitions
            )
            self.assertEqual(
                has_trajectory_change,
                trajectory.trajectory_status == "COMPLETED",
            )
        self.assertEqual(
            result.d2_observed_lane.sealed_evidence.manifest["unit_count"],
            len(result.d2_world.units),
        )
        self.assertEqual(
            result.d2_analysis_contract.assignment_bundle_sha256,
            result.d2_observed_lane.assignments.result_sha256,
        )
        self.assertEqual(
            result.d2_analyzer_result.input_sha256,
            result.d2_observed_lane.sealed_evidence.sha256,
        )
        self.assertIn(
            result.d2_evaluator_result.disposition,
            (
                "TRUTH_WITHIN_HOEFFDING_RANDOMIZATION_BOUND",
                "TRUTH_OUTSIDE_HOEFFDING_RANDOMIZATION_BOUND",
            ),
        )
        self.assertIsNotNone(result.d2_evaluator_result.absolute_error)
        result.validate(fixture["grid"], fixture["reach_config"])

        # Tampering with assignment probabilities while retaining the opaque
        # bundle digest must fail at the independent oracle-side boundary.
        original_bundle = result.d2_observed_lane.assignments
        original_row = original_bundle.assignments[0]
        tampered_row = replace(
            original_row,
            probability_z0=original_row.probability_z0 - 0.01,
            probability_z1=original_row.probability_z1 + 0.01,
        )
        tampered_bundle = replace(
            original_bundle,
            assignments=(tampered_row,) + original_bundle.assignments[1:],
        )
        with self.assertRaises(ContractError):
            D2ITTZEvaluator().evaluate(
                world=result.d2_world,
                truth=result.d2_vcont_truth,
                assignments=tampered_bundle,
                evidence=result.d2_observed_lane.sealed_evidence,
                contract=result.d2_analysis_contract,
                result=result.d2_analyzer_result,
                tolerance=0.25,
            )

        # Force one observed interval to missing, then verify that the oracle
        # reconstructs the measurement-completion bounds rather than trusting
        # the Analyzer's declared interval.
        source_rows = [dict(row) for row in result.d2_observed_lane.sealed_evidence.rows]
        source_rows[0]["observed_compliance"] = None
        source_rows[0]["observation_status"] = "MISSING"
        partial_evidence = D2IntervalSealer().seal(
            D2IntervalEvidenceCandidate(result.d2_observed_lane.sealed_evidence.run_id,
                                        tuple(source_rows))
        )
        partial_analysis = D2ITTZAnalyzer().analyze(
            partial_evidence, result.d2_analysis_contract,
        )
        self.assertEqual(partial_analysis.identification, "PARTIALLY_IDENTIFIED")
        partial_evaluation = D2ITTZEvaluator().evaluate(
            world=result.d2_world, truth=result.d2_vcont_truth,
            assignments=original_bundle, evidence=partial_evidence,
            contract=result.d2_analysis_contract, result=partial_analysis,
            tolerance=0.25,
        )
        self.assertEqual(
            partial_evaluation.disposition,
            "CORRECT_ABSTENTION_MEASUREMENT_INCOMPLETE",
        )
        tampered_partial = replace(
            partial_analysis, lower_bound=partial_analysis.lower_bound + 0.1,
        )
        tampered_payload = _result_payload(tampered_partial)
        tampered_partial = replace(
            tampered_partial, output_sha256=_output_hash(tampered_payload),
        )
        with self.assertRaises(ContractError):
            D2ITTZEvaluator().evaluate(
                world=result.d2_world, truth=result.d2_vcont_truth,
                assignments=original_bundle, evidence=partial_evidence,
                contract=result.d2_analysis_contract, result=tampered_partial,
                tolerance=0.25,
            )

        # Entire-unit nonresponse is distinct from interval missingness:
        # retain the full randomized roster in the sealed manifest while
        # withholding every S3 row for one assigned unit.
        omitted_unit = original_bundle.assignments[-1].unit_id
        observed_subset = tuple(
            dict(row) for row in result.d2_observed_lane.sealed_evidence.rows
            if row["unit_id"] != omitted_unit
        )
        expected_roster = tuple(
            (row.unit_id, row.history_ref) for row in original_bundle.assignments
        )
        expected_assignment_details = tuple(
            (row.unit_id, row.history_ref, row.assigned_z,
             row.probability_z0, row.probability_z1)
            for row in original_bundle.assignments
        )
        self.assertEqual(
            {row.assigned_z for row in original_bundle.assignments}, {0, 1},
        )
        missing_one_per_arm = tuple(
            next(row.unit_id for row in original_bundle.assignments if row.assigned_z == z)
            for z in (0, 1)
        )
        two_arm_rows = tuple(
            dict(row) for row in result.d2_observed_lane.sealed_evidence.rows
            if row["unit_id"] not in set(missing_one_per_arm)
        )
        two_arm_evidence = D2IntervalSealer().seal(
            D2IntervalEvidenceCandidate(
                result.d2_observed_lane.sealed_evidence.run_id,
                two_arm_rows, expected_roster, expected_assignment_details,
            )
        )
        two_arm_analysis = D2ITTZAnalyzer().analyze(
            two_arm_evidence, result.d2_analysis_contract,
        )
        self.assertEqual(two_arm_analysis.identification, "PARTIALLY_IDENTIFIED")
        self.assertEqual(two_arm_analysis.missing_target_histories, tuple(sorted(
            row.history_ref for row in original_bundle.assignments
            if row.unit_id in set(missing_one_per_arm)
        )))
        self.assertEqual(
            two_arm_analysis.assigned_z_unit_counts,
            (sum(row.assigned_z == 0 for row in original_bundle.assignments) - 1,
             sum(row.assigned_z == 1 for row in original_bundle.assignments) - 1),
        )
        two_arm_evaluation = D2ITTZEvaluator().evaluate(
            world=result.d2_world, truth=result.d2_vcont_truth,
            assignments=original_bundle, evidence=two_arm_evidence,
            contract=result.d2_analysis_contract, result=two_arm_analysis,
            tolerance=0.25,
        )
        self.assertEqual(
            two_arm_evaluation.disposition,
            "CORRECT_ABSTENTION_UNIT_NONRESPONSE",
        )
        unit_nonresponse_evidence = D2IntervalSealer().seal(
            D2IntervalEvidenceCandidate(
                result.d2_observed_lane.sealed_evidence.run_id,
                observed_subset,
                expected_roster,
                tuple((row.unit_id, row.history_ref, row.assigned_z,
                       row.probability_z0, row.probability_z1)
                      for row in original_bundle.assignments),
            )
        )
        self.assertEqual(
            unit_nonresponse_evidence.manifest["missing_unit_ids"],
            (omitted_unit,),
        )
        unit_nonresponse_analysis = D2ITTZAnalyzer().analyze(
            unit_nonresponse_evidence, result.d2_analysis_contract,
        )
        self.assertEqual(unit_nonresponse_analysis.identification, "PARTIALLY_IDENTIFIED")
        self.assertEqual(
            unit_nonresponse_analysis.bound_scope,
            "REALIZED_HT_MEASUREMENT_COMPLETION",
        )
        self.assertIsNone(unit_nonresponse_analysis.point_estimate)
        self.assertIn(
            original_bundle.assignments[-1].history_ref,
            unit_nonresponse_analysis.missing_target_histories,
        )
        self.assertLessEqual(unit_nonresponse_analysis.lower_bound, unit_nonresponse_analysis.upper_bound)
        unit_nonresponse_evaluation = D2ITTZEvaluator().evaluate(
            world=result.d2_world, truth=result.d2_vcont_truth,
            assignments=original_bundle, evidence=unit_nonresponse_evidence,
            contract=result.d2_analysis_contract,
            result=unit_nonresponse_analysis, tolerance=0.25,
        )
        self.assertEqual(
            unit_nonresponse_evaluation.disposition,
            "CORRECT_ABSTENTION_UNIT_NONRESPONSE",
        )

        # The Evaluator must reconstruct the unit-nonresponse envelope even
        # when a tampered Analyzer output is re-hashed consistently.
        tampered_unit_bounds = replace(
            unit_nonresponse_analysis,
            upper_bound=unit_nonresponse_analysis.upper_bound + 0.1,
        )
        tampered_unit_payload = _result_payload(tampered_unit_bounds)
        tampered_unit_bounds = replace(
            tampered_unit_bounds,
            output_sha256=_output_hash(tampered_unit_payload),
        )
        with self.assertRaises(ContractError):
            D2ITTZEvaluator().evaluate(
                world=result.d2_world, truth=result.d2_vcont_truth,
                assignments=original_bundle, evidence=unit_nonresponse_evidence,
                contract=result.d2_analysis_contract,
                result=tampered_unit_bounds, tolerance=0.25,
            )

        # Combined nonresponse: one unit is wholly absent and another has
        # an interval missing. The two mechanisms must remain distinguishable.
        combined_rows = [
            dict(row) for row in observed_subset
            if row["unit_id"] != omitted_unit
        ]
        combined_rows[0]["observed_compliance"] = None
        combined_rows[0]["observation_status"] = "MISSING"
        combined_evidence = D2IntervalSealer().seal(
            D2IntervalEvidenceCandidate(
                result.d2_observed_lane.sealed_evidence.run_id,
                tuple(combined_rows),
                expected_roster,
                tuple((row.unit_id, row.history_ref, row.assigned_z,
                       row.probability_z0, row.probability_z1)
                      for row in original_bundle.assignments),
            )
        )
        combined_analysis = D2ITTZAnalyzer().analyze(
            combined_evidence, result.d2_analysis_contract,
        )
        self.assertEqual(combined_analysis.identification, "PARTIALLY_IDENTIFIED")
        self.assertIn("UNIT_NONRESPONSE_AND_INTERVAL_MISSINGNESS",
                      combined_analysis.abstention_reason)
        combined_evaluation = D2ITTZEvaluator().evaluate(
            world=result.d2_world, truth=result.d2_vcont_truth,
            assignments=original_bundle, evidence=combined_evidence,
            contract=result.d2_analysis_contract, result=combined_analysis,
            tolerance=0.25,
        )
        self.assertEqual(
            combined_evaluation.disposition,
            "CORRECT_ABSTENTION_MEASUREMENT_AND_UNIT_NONRESPONSE",
        )

        # Zero-response edge: retain the complete randomized assignment roster
        # and the declared grid/monitor independently of observed S3 rows.
        assignment_rows = tuple(
            (row.unit_id, row.history_ref, row.assigned_z,
             row.probability_z0, row.probability_z1)
            for row in original_bundle.assignments
        )
        self.assertEqual({row[2] for row in assignment_rows}, {0, 1})
        monitor = next(iter(fixture["monitor_configs"].values()))
        boundaries = fixture["grid"].boundaries
        empty_candidate = D2IntervalEvidenceCandidate(
            run_id=result.d2_observed_lane.sealed_evidence.run_id,
            rows=(),
            expected_unit_assignments=assignment_rows,
            grid_id=fixture["grid"].grid_id,
            grid_version=fixture["grid"].grid_version,
            monitor_id=monitor.monitor_id,
            monitor_version=monitor.monitor_version,
            interval_bounds=tuple(zip(boundaries, boundaries[1:])),
            assignment_bundle_sha256=original_bundle.result_sha256,
            assignment_mechanism_id=original_bundle.mechanism_id,
            assignment_mechanism_version=original_bundle.mechanism_version,
            q_x_sha256=original_bundle.q_x_sha256,
        )
        empty_evidence = D2IntervalSealer().seal(empty_candidate)
        self.assertEqual(empty_evidence.rows, ())
        self.assertEqual(empty_evidence.manifest["row_count"], 0)
        self.assertEqual(empty_evidence.manifest["unit_count"], 0)
        self.assertEqual(empty_evidence.manifest["expected_unit_count"], len(assignment_rows))
        self.assertEqual(empty_evidence.manifest["interval_count_per_unit"], len(boundaries) - 1)
        self.assertEqual(empty_evidence.manifest["missing_unit_ids"], tuple(sorted(
            row[0] for row in assignment_rows
        )))
        empty_lane = replace(
            result.d2_observed_lane,
            interval_records=(),
            sealed_evidence=empty_evidence,
        )
        empty_lane.validate(
            result.d2_world, result.d2_vcont_truth,
            result.d2_event_histories_by_unit_z, fixture["grid"],
        )
        self.assertEqual(
            (result.d2_analysis_contract.grid_id, result.d2_analysis_contract.grid_version,
             result.d2_analysis_contract.monitor_id, result.d2_analysis_contract.monitor_version),
            (fixture["grid"].grid_id, fixture["grid"].grid_version,
             monitor.monitor_id, monitor.monitor_version),
        )
        false_assignment_provenance = D2IntervalSealer().seal(replace(
            empty_candidate, assignment_bundle_sha256="0" * 64,
        ))
        with self.assertRaises(ContractError):
            D2ITTZAnalyzer().analyze(
                false_assignment_provenance, result.d2_analysis_contract,
            )
        false_monitor_evidence = D2IntervalSealer().seal(replace(
            empty_candidate, monitor_id="MONITOR-ALTERED",
        ))
        with self.assertRaises(ContractError):
            D2ITTZAnalyzer().analyze(
                false_monitor_evidence, result.d2_analysis_contract,
            )
        empty_analysis = D2ITTZAnalyzer().analyze(
            empty_evidence, result.d2_analysis_contract,
        )
        self.assertEqual(empty_analysis.identification, "PARTIALLY_IDENTIFIED")
        self.assertIsNone(empty_analysis.point_estimate)
        self.assertEqual(empty_analysis.assigned_z_unit_counts, (0, 0))
        self.assertEqual(empty_analysis.total_interval_count, 0)
        self.assertEqual(empty_analysis.target_q_x_coverage, 0.0)
        self.assertEqual(empty_analysis.bound_scope, "REALIZED_HT_MEASUREMENT_COMPLETION")
        empty_evaluation = D2ITTZEvaluator().evaluate(
            world=result.d2_world, truth=result.d2_vcont_truth,
            assignments=original_bundle, evidence=empty_evidence,
            contract=result.d2_analysis_contract, result=empty_analysis,
            tolerance=0.25,
        )
        self.assertEqual(
            empty_evaluation.disposition,
            "CORRECT_ABSTENTION_UNIT_NONRESPONSE",
        )
        self.assertTrue(empty_evaluation.correct_adjudication)

        false_monitor_result = replace(
            empty_analysis, input_sha256=false_monitor_evidence.sha256,
        )
        false_monitor_payload = _result_payload(false_monitor_result)
        false_monitor_result = replace(
            false_monitor_result,
            output_sha256=_output_hash(false_monitor_payload),
        )
        with self.assertRaises(ContractError):
            D2ITTZEvaluator().evaluate(
                world=result.d2_world, truth=result.d2_vcont_truth,
                assignments=original_bundle, evidence=false_monitor_evidence,
                contract=result.d2_analysis_contract, result=false_monitor_result,
                tolerance=0.25,
            )

        false_grid_evidence = D2IntervalSealer().seal(replace(
            empty_candidate, grid_id="GRID-ALTERED",
        ))
        with self.assertRaises(ContractError):
            D2ITTZAnalyzer().analyze(
                false_grid_evidence, result.d2_analysis_contract,
            )
        false_grid_result = replace(
            empty_analysis, input_sha256=false_grid_evidence.sha256,
        )
        false_grid_payload = _result_payload(false_grid_result)
        false_grid_result = replace(
            false_grid_result,
            output_sha256=_output_hash(false_grid_payload),
        )
        with self.assertRaises(ContractError):
            D2ITTZEvaluator().evaluate(
                world=result.d2_world, truth=result.d2_vcont_truth,
                assignments=original_bundle, evidence=false_grid_evidence,
                contract=result.d2_analysis_contract, result=false_grid_result,
                tolerance=0.25,
            )

        # Rehashed false arm metadata for a wholly unobserved unit is rejected
        # against the independent randomized assignment bundle.
        false_roster = list(assignment_rows)
        first_assignment = false_roster[0]
        false_roster[0] = (
            first_assignment[0], first_assignment[1],
            1 - first_assignment[2], first_assignment[3], first_assignment[4],
        )
        false_evidence = D2IntervalSealer().seal(replace(
            empty_candidate, expected_unit_assignments=tuple(false_roster),
        ))
        false_analysis = D2ITTZAnalyzer().analyze(
            false_evidence, result.d2_analysis_contract,
        )
        with self.assertRaises(ContractError):
            D2ITTZEvaluator().evaluate(
                world=result.d2_world, truth=result.d2_vcont_truth,
                assignments=original_bundle, evidence=false_evidence,
                contract=result.d2_analysis_contract, result=false_analysis,
                tolerance=0.25,
            )



    def test_d2_trajectory_execution_explicitly_drives_b1_vcont_history(self):
        fixture = self._fixture("positive")
        trajectory_rule = FunctionalHistoryRule(
            rule_id="TRAJECTORY-EXECUTION-FAILURE-INTERRUPTS-B1",
            source="TRAJECTORY",
            event_time=Decimal("1.5"),
            causal_family="TRAJECTORY_EXECUTION_TO_B1_ADMISSION",
            provenance_ref="FUNCTIONAL-DGP#TRAJECTORY-EXECUTION-FAILURE-INTERRUPTS-B1",
            set_admission="NO_ADMISSION",
            trajectory_target_state="TARGET",
            trajectory_field="trajectory_status",
            trajectory_value="EXECUTION_FAILED",
        )
        fixture["functional_config"] = replace(
            fixture["functional_config"], rules=(trajectory_rule,),
        )
        fixture["trajectory_config"] = replace(
            fixture["trajectory_config"],
            route_execution_probability=(("ROUTE-FOCAL", 0.0),),
        )
        result = self._run_pipeline(fixture)
        trajectories = {
            (row.unit_id, row.z, row.target_state): row
            for row in result.trajectories.trajectories
        }
        truth = {
            (row.unit_id, row.z): row.v_cont_truth
            for row in result.d2_vcont_truth.potential_truth
        }
        histories = dict(result.d2_histories_by_unit_z)
        for unit in result.world.units:
            self.assertEqual(
                trajectories[(unit.unit_id, 0, "TARGET")].trajectory_status,
                "NOT_REACHABLE",
            )
            self.assertEqual(
                trajectories[(unit.unit_id, 1, "TARGET")].trajectory_status,
                "EXECUTION_FAILED",
            )
            self.assertEqual(truth[(unit.unit_id, 0)], 1)
            self.assertEqual(truth[(unit.unit_id, 1)], 0.5)
            self.assertFalse(any(
                change.causal_family == "TRAJECTORY_EXECUTION_TO_B1_ADMISSION"
                for change in histories[(unit.unit_id, 0)].transitions
            ))
            self.assertTrue(any(
                change.causal_family == "TRAJECTORY_EXECUTION_TO_B1_ADMISSION"
                for change in histories[(unit.unit_id, 1)].transitions
            ))


    def test_complete_world_rejects_reach_detached_from_delta_snapshots(self):
        fixture = self._fixture("positive")
        result = self._run_pipeline(fixture)
        first = result.reachability.contrasts[0]
        detached_baseline = replace(first.baseline, snapshot_id="DETACHED-BASELINE")
        detached_contrast = replace(first, baseline=detached_baseline)
        detached_reach = replace(
            result.reachability,
            contrasts=(detached_contrast,) + result.reachability.contrasts[1:],
        )
        detached_result = replace(result, reachability=detached_reach)
        with self.assertRaises(ContractError):
            detached_result.validate(
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
