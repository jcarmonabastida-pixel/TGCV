"""Canonical DGP materializer for the five candidate focal theta_A scenarios.

This module constructs only the declared synthetic world and complete pipeline
result. It does not create seed banks, authorize execution, or run calibration.
"""
from decimal import Decimal

from c10s_synthetic_components import (
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
from c10s_functional_history import FunctionalHistoryDGPConfig, FunctionalHistoryRule
from c10s_world_pipeline import (
    SyntheticThetaATargetHistory,
    materialize_c10s_complete_world_from_dgp,
)
from theta_a_interval_observation import IntervalMonitorConfig
from d2_observed_assignment import D2ObservedAssignmentConfig
from theta_a_calibration_protocol import ThetaACalibrationScenario, ThetaASeedAssignment, s3_seeds_by_unit


class ThetaACalibrationDGPFactory:
    def build_fixture(self, theta_a_mode="positive", seed_assignment=None, n_units=None):
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
        d2_assignment_config = D2ObservedAssignmentConfig(
            mechanism_id="D2-PACKAGE-Z-RANDOMIZATION",
            mechanism_version="1",
            randomization_salt="D2-PACKAGE-Z-SALT",
            probability_z1_by_history=tuple(
                (row.history_ref, 0.5) for row in world.q_x
            ),
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
        monitor_seeds = (
            s3_seeds_by_unit(seed_assignment.s3_seed, tuple(unit.unit_id for unit in world.units))
            if seed_assignment is not None else {
                unit.unit_id: 9000 + index
                for index, unit in enumerate(world.units)
            }
        )
        return {
            "world": world,
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
            "d2_assignment_config": d2_assignment_config,
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
            "monitor_seeds": monitor_seeds,
            # D2 package ITT uses a distinct interval-monitor stream from the
            # direct-g_A focal measurement lane, while sharing the frozen grid.
            "d2_monitor_seeds": {
                unit_id: seed + 100000 for unit_id, seed in monitor_seeds.items()
            },
        }

    def run_pipeline(
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
            d2_assignment_config=fixture["d2_assignment_config"],
            d2_interval_monitor_configs_by_history_ref=fixture["monitor_configs"],
            d2_interval_monitor_seeds_by_unit=fixture["d2_monitor_seeds"],
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

    def configure_target_only_support_fixture(self, fixture, scenario):
        profile = scenario.dgp_profile
        if profile is None or profile.support_relation != "TARGET_HAS_UNSUPPORTED_HISTORIES":
            raise ValueError("target-only fixture requires a target-unsupported DGP profile")
        if len(profile.target_unsupported_history_masses) != 1:
            raise ValueError("current target-only materializer supports exactly one reserved target-only history")
        world = fixture["world"]
        extra_ref, unsupported_mass = profile.target_unsupported_history_masses[0]
        extra_unit_id = "TARGET-ONLY-UNIT-001"
        extra_qx = QXHistoryMass(
            extra_ref, "TARGET-X-001", "TARGET-H0-001", "TARGET-CC-001", unsupported_mass,
        )
        supported_mass = 1.0 - unsupported_mass
        target_q_x = tuple(
            QXHistoryMass(row.history_ref, row.x_ref, row.h0_ref, row.c_c_ref, row.mass * supported_mass)
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
            profile.structural_support_contract_id,
            profile.structural_support_contract_version,
            digest(target_q_x), digest(world.q_x),
            tuple(
                ThetaAStructuralSupportRow(
                    row.history_ref, row.mass, source_row.mass,
                    True, True, True, assignment_probabilities[row.history_ref],
                )
                for row, source_row in zip(target_q_x[:-1], world.q_x)
            ) + (ThetaAStructuralSupportRow(
                extra_ref, unsupported_mass, 0.0, True, True, True, None,
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
        fixture["target_q_x"] = target_q_x
        fixture["target_materialization"] = target_materialization
        return fixture

    def execute_calibration_scenario(self, assignment, scenario, inference_options):
        profile = scenario.dgp_profile
        if profile is None or profile.generator_variant is None:
            raise ValueError("canonical calibration execution requires a typed generator variant")
        mode = "positive" if profile.generator_variant == "positive_target_only" else profile.generator_variant
        fixture = self.build_fixture(mode, seed_assignment=assignment)
        if profile.support_relation == "TARGET_HAS_UNSUPPORTED_HISTORIES":
            fixture = self.configure_target_only_support_fixture(fixture, scenario)
        elif profile.support_relation == "EQUAL":
            world = fixture["world"]
            probabilities = dict(fixture["assignment_config"].probability_a1_by_history)
            support = ThetaAStructuralSupportContract(
                profile.structural_support_contract_id,
                profile.structural_support_contract_version,
                digest(world.q_x), digest(world.q_x),
                tuple(
                    ThetaAStructuralSupportRow(
                        row.history_ref, row.mass, row.mass,
                        True, True, True, probabilities[row.history_ref],
                    ) for row in world.q_x
                ),
            )
            fixture["theta_a_population_args"] = {
                "theta_a_structural_support_contract": support,
            }
        else:
            raise ValueError("candidate calibration factory does not materialize this support relation")
        return self.run_pipeline(fixture, **inference_options)

