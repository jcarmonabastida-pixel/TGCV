import unittest
from decimal import Decimal

from vcont_integrated_harness import (Analyzer, EvidenceCandidate, Evaluator, Generator,
                                      Sealer, benchmark_scenarios, contract_for)

from c10s_synthetic_components import (
    ContractError, D2Baseline, D2MechanismConfig, EventHistory,
    StructuralTransformation, StructuralSnapshot, StructuralRouteStep,
    StructuralRoute, StructuralReachabilityEngine,
    evaluate_synthetic_world_reachability,
    StructuralAtom, StructuralIdentityMatch, StructuralTransitionRule, TransformationalStateSnapshot,
    EvidenceStateSnapshot, TransformationalDeltaEngine, D2StructuralPotentialPair,
    evaluate_d2_structural_deltas, D2StructuralGenerationConfig,
    generate_d2_structural_potential_pairs, D2ReachStepTemplate, D2ReachRouteTemplate,
    D2ReachGenerationConfig, evaluate_d2_structural_reachability,
    D2TrajectoryGenerationConfig, evaluate_d2_potential_trajectories,
    evaluate_d2_vcont_potential_truth, compute_theta_a_vcont_truth_from_event_histories,
    digest,
    FunctionalState, FunctionalTransition, FunctionalStateChange,
    EventHistoryGenerationSpec, generate_event_history, IntervalGrid,
    JointPolicyHistory, QXHistoryMass, RCommonPairCertificate,
    S3SequenceKernelRow, S3ObservationConfig, adjudicate_intervals,
    compute_theta_a_truth, evaluate_theta_a_output, generate_d2_potentials, project_s3,
    ThetaAPolicyAssignmentConfig, generate_theta_a_policy_assignments,
    theta_a_event_history_potential_id, select_theta_a_realized_histories,
    project_s3_into_evidence_candidate, compose_existing_generation,
)


class SyntheticComponentTests(unittest.TestCase):
    def history(self, transitions=(), *, initial=None, complete=True):
        return EventHistory(
            history_id="EH-001", history_version="001", run_id="RUN-001",
            world_id="WORLD-001", world_version="001", dgp_version="DGP-001",
            unit_id="UE-001", potential_id="Z0_POLICY0",
            adjudication_rules_version="AB1-001",
            support_start=Decimal("0"), support_end=Decimal("4"),
            initial_post_z_state=initial or FunctionalState(False, "NO_ADMISSION"),
            transitions=tuple(transitions), expected_transition_ids=tuple(
                event.transition_id for event in transitions
            ),
            scope_declared_complete=complete, generation_complete=complete,
            representation_complete=complete,
        )

    def test_event_history_generator_materializes_complete_chained_transitions(self):
        initial = FunctionalState(False, "NO_ADMISSION")
        enabled_without_admission = FunctionalState(True, "NO_ADMISSION")
        admitted = FunctionalState(True, "ADMIT")
        spec = EventHistoryGenerationSpec(
            "EH-GEN-001", "001", "RUN-001", "WORLD-001", "001",
            "DGP-001", "UE-001", "GA-A1-VECTOR-R", "AB1-001",
            Decimal("0"), Decimal("4"), initial,
            (
                FunctionalStateChange(Decimal("1"), enabled_without_admission,
                                      "ENABLEMENT", "DGP-TRUTH-ENABLE"),
                FunctionalStateChange(Decimal("2"), admitted,
                                      "ADMISSION", "DGP-TRUTH-ADMIT"),
            ),
        )
        first = generate_event_history(spec)
        second = generate_event_history(spec)
        self.assertEqual(first, second)
        self.assertTrue(first.scope_declared_complete)
        self.assertTrue(first.generation_complete)
        self.assertTrue(first.representation_complete)
        self.assertEqual(len(first.transitions), 2)
        self.assertEqual(first.transitions[1].state_before, enabled_without_admission)
        self.assertEqual(first.expected_transition_ids,
                         tuple(row.transition_id for row in first.transitions))
        adjudicated = adjudicate_intervals(
            first, IntervalGrid((Decimal("0"), Decimal("2"), Decimal("4")), "GRID-GEN", "001")
        )
        self.assertEqual(adjudicated.interval_truth, (0, 1))

    def test_event_history_generator_rejects_neutral_or_unordered_changes(self):
        initial = FunctionalState(False, "NO_ADMISSION")
        spec = EventHistoryGenerationSpec(
            "EH-GEN-002", "001", "RUN-001", "WORLD-001", "001",
            "DGP-001", "UE-001", "GA-A0-VECTOR-R", "AB1-001",
            Decimal("0"), Decimal("4"), initial,
            (FunctionalStateChange(Decimal("1"), initial, "NOOP", "P-NOOP"),),
        )
        with self.assertRaises(ContractError):
            generate_event_history(spec)
        unordered = EventHistoryGenerationSpec(
            "EH-GEN-003", "001", "RUN-001", "WORLD-001", "001",
            "DGP-001", "UE-001", "GA-A0-VECTOR-R", "AB1-001",
            Decimal("0"), Decimal("4"), initial,
            (
                FunctionalStateChange(Decimal("2"), FunctionalState(True, "ADMIT"),
                                      "ADMISSION", "P2"),
                FunctionalStateChange(Decimal("1"), FunctionalState(False, "ADMIT"),
                                      "ENABLEMENT", "P1"),
            ),
        )
        with self.assertRaises(ContractError):
            generate_event_history(unordered)

    def test_internal_boundary_event_belongs_to_interval_that_starts_there(self):
        before = FunctionalState(False, "NO_ADMISSION")
        failed = FunctionalState(True, "NO_ADMISSION")
        history = self.history((
            FunctionalTransition("T-1", Decimal("2"), before, failed, "RUNTIME_FAILURE", "TRUTH-PROV-1"),
        ))
        result = adjudicate_intervals(
            history, IntervalGrid((Decimal("0"), Decimal("2"), Decimal("4")), "GRID", "001")
        )
        self.assertEqual(result.interval_truth, (1, 0))
        self.assertEqual(result.v_cont_truth, 0.5)

    def test_event_at_final_T_star_belongs_to_last_interval(self):
        before = FunctionalState(False, "NO_ADMISSION")
        failed = FunctionalState(True, "NO_ADMISSION")
        history = self.history((
            FunctionalTransition("T-1", Decimal("4"), before, failed, "RUNTIME_FAILURE", "TRUTH-PROV-1"),
        ))
        result = adjudicate_intervals(
            history, IntervalGrid((Decimal("0"), Decimal("2"), Decimal("4")), "GRID", "001")
        )
        self.assertEqual(result.interval_truth, (1, 0))

    def test_same_time_intermediate_functional_state_is_adjudicated(self):
        s0 = FunctionalState(False, "NO_ADMISSION")
        s1 = FunctionalState(True, "NO_ADMISSION")
        s2 = FunctionalState(True, "ADMIT")
        history = self.history((
            FunctionalTransition("T-1", Decimal("1"), s0, s1, "DECLARATIVE_CHANGE", "P1", 0),
            FunctionalTransition("T-2", Decimal("1"), s1, s2, "RUNTIME_RECOVERY", "P2", 1),
        ))
        result = adjudicate_intervals(
            history, IntervalGrid((Decimal("0"), Decimal("2"), Decimal("4")), "GRID", "001")
        )
        self.assertEqual(result.interval_truth, (0, 1))

    def test_incomplete_history_fails_closed_not_functional_unknown(self):
        history = self.history(complete=False)
        with self.assertRaises(ContractError):
            adjudicate_intervals(
                history, IntervalGrid((Decimal("0"), Decimal("2"), Decimal("4")), "GRID", "001")
            )

    def test_d2_generates_separate_stages_and_common_exogenous_potentials(self):
        baseline = D2Baseline(
            "UE-001", "BASE-001", False, True, True, True, True, True, True
        )
        config = D2MechanismConfig(
            "D2-SYNTH", "001", ("B_D2_0", "B_D2_1"), ("001", "001"),
            ("ARTIFACT-0", "ARTIFACT-1"), ("ACTOR-0", "ACTOR-1"),
            (0.0, 1.0), (0.8, 0.8), (0.0, 0.0), (0.9, 0.9), (0.8, 0.8),
            (((True, True, True, True), 0.7), ((True, False, True, True), 0.3)),
            "MECH-001",
        )
        result = generate_d2_potentials(baseline, config, exogenous_seed=42)
        result.validate()
        p0, p1 = result.potentials_by_z
        self.assertFalse(p0.w_programmed)
        self.assertTrue(p1.w_programmed)
        self.assertEqual(p0.z, 0)
        self.assertEqual(p1.z, 1)
        self.assertEqual(p1.c_dep_star, all((
            p1.c_install, p1.c_integrity, p1.c_compat, p1.c_oper
        )))
        if not p1.c_dep_star:
            self.assertFalse(p1.a_f_post)

    def test_theta_a_truth_uses_explicit_qx_joint_policies_and_common_regime(self):
        qx = (QXHistoryMass("H1", "X1", "H0-1", "CC-1", 1.0),)
        g0 = (JointPolicyHistory("H1", (((0.0, 0.0, 0.0, 0.0), 1.0),)),)
        g1 = (JointPolicyHistory("H1", (((1.0, 1.0, 1.0, 1.0), 1.0),)),)
        cert = (RCommonPairCertificate("H1", "R-COMMON", "001", "same", "same", "COMMON_FIXED"),)
        truth = compute_theta_a_truth(
            qx, g0, g1, {"H1": ((0.0, 0.0, 0.0, 0.0), (1.0, 1.0, 1.0, 1.0))},
            cert, lambda h, vector, regime: sum(vector) / 4.0,
            estimand_version="001", outcome_version="001",
        )
        self.assertAlmostEqual(truth.theta_a_truth, 1.0)
        self.assertTrue(truth.evaluator_only)
        scored = evaluate_theta_a_output(
            truth, identification_status="IDENTIFIED", estimate=0.95, tolerance=0.10
        )
        self.assertTrue(scored.recovered_within_tolerance)
        abstained = evaluate_theta_a_output(
            truth, identification_status="NOT_IDENTIFIED", estimate=None, tolerance=0.10
        )
        self.assertTrue(abstained.abstention_respected)

    def test_theta_a_rejects_non_common_r_common(self):
        qx = (QXHistoryMass("H1", "X1", "H0-1", "CC-1", 1.0),)
        g0 = (JointPolicyHistory("H1", (((0.0, 0.0, 0.0, 0.0), 1.0),)),)
        g1 = (JointPolicyHistory("H1", (((1.0, 1.0, 1.0, 1.0), 1.0),)),)
        cert = (RCommonPairCertificate("H1", "R-COMMON", "001", "r0", "r1", "COMMON_FIXED"),)
        with self.assertRaises(ContractError):
            compute_theta_a_truth(
                qx, g0, g1, {"H1": ((0.0, 0.0, 0.0, 0.0), (1.0, 1.0, 1.0, 1.0))},
                cert, lambda h, vector, regime: sum(vector) / 4.0,
                estimand_version="001", outcome_version="001",
            )

    def test_s3_joint_kernel_can_emit_missing_without_mutating_truth(self):
        history = self.history()
        before_hash = history.content_sha256
        config = S3ObservationConfig(
            (Decimal("0"), Decimal("2"), Decimal("4")),
            (Decimal("0.1"), Decimal("0.1"), Decimal("0.1")),
            (Decimal("0.2"), Decimal("0.2"), Decimal("0.2")),
            (S3SequenceKernelRow(
                ((False, "NO_ADMISSION", "STANDARD"),) * 3,
                ((((None, None, None), (None, None, None), (None, None, None)), 1.0),),
            ),),
            "S3-TEST", "001",
        )
        rows = project_s3(history, config, seed=7)
        self.assertEqual(len(rows), 3)
        self.assertTrue(all(row.enabled_status == "MISSING" for row in rows))
        self.assertTrue(all(row.admission_status == "MISSING" for row in rows))
        self.assertEqual(history.content_sha256, before_hash)
        self.assertEqual(rows[0].ingestion_time, Decimal("0.3"))
        self.assertEqual(rows[0].profile_value_observed, "STANDARD")
        self.assertEqual(rows[0].profile_config_id, "B1-PROFILE")
        self.assertFalse(hasattr(rows[0], "profile_exposure_observed"))



    def test_profile_configuration_transition_does_not_change_a_b1(self):
        before = FunctionalState(False, "NO_ADMISSION", "STANDARD")
        after = FunctionalState(False, "NO_ADMISSION", "READ_ONLY", "B1-PROFILE", "002")
        history = self.history((
            FunctionalTransition("T-PROFILE", Decimal("2"), before, after,
                                 "DECLARATIVE_CONFIGURATION", "TRUTH-PROFILE-1"),
        ), initial=before)
        result = adjudicate_intervals(
            history, IntervalGrid((Decimal("0"), Decimal("2"), Decimal("4")), "GRID", "001")
        )
        self.assertEqual(result.interval_truth, (1, 1))
        self.assertTrue(before.declarative_valid)
        self.assertTrue(after.declarative_valid)
        invalid_declaration = FunctionalState(True, "ADMIT", "DISABLED")
        self.assertFalse(invalid_declaration.declarative_valid)
        # D_valid is separate: this does not rewrite the A_B1 admission predicate.
        self.assertTrue(invalid_declaration.compliant)

    def test_s3_projection_binds_observations_without_truth_leakage(self):
        history = self.history()
        config = S3ObservationConfig(
            (Decimal("0"), Decimal("2"), Decimal("4")),
            (Decimal("0.1"),) * 3, (Decimal("0.2"),) * 3,
            (S3SequenceKernelRow(
                ((False, "NO_ADMISSION", "STANDARD"),) * 3,
                ((((False, "NO_ADMISSION", "STANDARD"),
                   (False, "NO_ADMISSION", "STANDARD"),
                   (False, "NO_ADMISSION", "STANDARD")), 1.0),),
            ),),
            "S3-ADAPTER", "001",
        )
        observations = project_s3(history, config, seed=11)
        original = {
            "unit_id": "UE-001", "s3_enabled": [1, 1, 1],
            "s3_admission_behavior": ["ADMIT"] * 3,
            "s3_profile_value": ["READ_ONLY"] * 3,
            "s3_enabled_status": ["OBSERVED"] * 3,
            "s3_admission_status": ["OBSERVED"] * 3,
            "s3_profile_status": ["OBSERVED"] * 3,
        }
        candidate = EvidenceCandidate("RUN-001", (original,), {"run_id": "RUN-001"})
        projected = project_s3_into_evidence_candidate(candidate, (history,), observations)
        row = projected.rows[0]
        self.assertEqual(row["s3_enabled"], [0, 0, 0])
        self.assertEqual(row["s3_admission_behavior"], ["NO_ADMISSION"] * 3)
        self.assertEqual(row["s3_profile_value"], ["STANDARD"] * 3)
        self.assertEqual(row["s3_profile_config_id"], ["B1-PROFILE"] * 3)
        self.assertEqual(row["s3_profile_config_version"], ["001"] * 3)
        self.assertEqual(row["s3_temporal_support"], ["POINT_SAMPLE"] * 3)
        self.assertNotIn("event_history", row)
        self.assertNotIn("interval_adjudication", row)
        self.assertEqual(candidate.rows[0], original)


    def test_composition_connects_realized_eventhistory_s3_and_sealed_evidence(self):
        scenario = benchmark_scenarios(n_units=16, n_intervals=5)[0]
        baselines = tuple(
            D2Baseline(f"UE-{i+1:06d}", f"BASE-{i+1:06d}", False, True, True, True, True, True, True)
            for i in range(16)
        )
        d2_config = D2MechanismConfig(
            "D2-SYNTH", "001", ("B_D2_0", "B_D2_1"), ("001", "001"),
            ("ARTIFACT-0", "ARTIFACT-1"), ("ACTOR-0", "ACTOR-1"),
            (0.0, 1.0), (0.8, 0.8), (0.0, 0.0), (0.9, 0.9), (0.8, 0.8),
            (((True, True, True, True), 0.7), ((True, False, True, True), 0.3)),
            "MECH-001",
        )

        def history_factory(manifest, bundles):
            histories = []
            for bundle in bundles:
                unit_id = bundle.unit_id
                state = FunctionalState(False, "NO_ADMISSION", "STANDARD")
                histories.append(EventHistory(
                    history_id=f"EH-{unit_id}", history_version="001",
                    run_id=manifest.run_id, world_id=manifest.world_id,
                    world_version=manifest.world_version, dgp_version="DGP-001",
                    unit_id=unit_id, potential_id="REALIZED_SELECTED",
                    adjudication_rules_version="AB1-001",
                    support_start=Decimal("0"), support_end=Decimal("1"),
                    initial_post_z_state=state, transitions=(),
                    expected_transition_ids=(), scope_declared_complete=True,
                    generation_complete=True, representation_complete=True,
                ))
            return tuple(histories)

        def grid_factory(histories):
            return {
                history.history_id: IntervalGrid(
                    (Decimal("0"), Decimal("0.2"), Decimal("0.4"), Decimal("0.6"), Decimal("0.8"), Decimal("1")), "GRID", "001"
                ) for history in histories
            }

        selected = {row.unit_id: f"EH-{row.unit_id}" for row in baselines}
        configs, seeds = {}, {}
        for index, history_id in enumerate(selected.values()):
            configs[history_id] = S3ObservationConfig(
                (Decimal("0"), Decimal("0.2"), Decimal("0.4"), Decimal("0.6"), Decimal("0.8")),
                (Decimal("0.01"),) * 5,
                (Decimal("0.02"),) * 5,
                (S3SequenceKernelRow(
                    ((False, "NO_ADMISSION", "STANDARD"),) * 5,
                    (
                        (((False, "NO_ADMISSION", "STANDARD"),) * 5, 1.0),
                    ),
                ),),
                "S3-COMPOSE", "001",
            )
            seeds[history_id] = 700 + index

        envelope = compose_existing_generation(
            Generator(), scenario, baselines, d2_config,
            {row.unit_id: 1000 + i for i, row in enumerate(baselines)},
            history_factory, grid_factory,
            selected_history_id_by_unit=selected,
            s3_configs_by_history=configs,
            s3_seeds_by_history=seeds,
        )
        self.assertEqual(len(envelope.s3_observations), 80)
        self.assertEqual(len(envelope.evidence_candidate.rows), 16)
        self.assertTrue(all(
            set(row["s3_temporal_support"]) == {"POINT_SAMPLE"}
            for row in envelope.evidence_candidate.rows
        ))
        self.assertNotIn("event_history", envelope.evidence_candidate.rows[0])
        sealed = Sealer().seal(envelope.evidence_candidate)
        self.assertEqual(sealed.manifest["schema"], "C10S-VCONT-S3-002")
        analyzer_result = Analyzer().analyze(sealed, contract_for(scenario))
        evaluation = Evaluator().evaluate_event_history_interface(
            envelope, sealed, analyzer_result, contract_for(scenario)
        )
        self.assertEqual(evaluation["selected_history_count"], 16)
        self.assertEqual(evaluation["s3_observation_count"], 80)
        self.assertTrue(evaluation["point_sample_only"])
        self.assertTrue(evaluation["analyzer_abstention_respected"])
        self.assertTrue(evaluation["analysis_output_seal_verified"])
        self.assertTrue(evaluation["analysis_reference_identification_status_correct"])
        self.assertTrue(evaluation["analysis_expected_abstention_respected"])
        self.assertTrue(all(
            value == 1.0 for value in evaluation["v_cont_truth_by_unit"].values()
        ))
        self.assertFalse(evaluation["causal_itt_and_theta_a_scored"])
        self.assertEqual(
            len(envelope.truth_extension.event_histories), 16
        )


    def test_world_builder_materializes_explicit_roster_qx_and_d2_potentials(self):
        from c10s_synthetic_components import (
            SyntheticWorldBuilder, SyntheticWorldConfig,
        )
        world_config = SyntheticWorldConfig(
            world_id="WORLD-FIXTURE", world_version="001",
            dgp_id="D2-WORLD-FIXTURE", dgp_version="001",
            roster_id="ROSTER-FIXTURE", roster_version="001",
            unit_id_prefix="UE", n_units=4, seed=20261116,
            x_dimension=2, h0_distribution=(("H0-A", 0.75), ("H0-B", 0.25)),
            c_c_dimension=2, c_c_component_probability=0.8,
            focal_accessible_pre_probability=0.2,
            c_auth_base_probability=1.0, c_resource_probability=0.9,
            c_capacity_probability=0.9, c_info_probability=0.95,
            c_domain_probability=0.95, c_other_probability=0.95,
            q_x_mass_by_unit=(0.1, 0.2, 0.3, 0.4),
        )
        d2_config = D2MechanismConfig(
            "D2-WORLD-FIXTURE", "001",
            ("B_D2_0", "B_D2_1"), ("001", "001"),
            ("ARTIFACT-0", "ARTIFACT-1"), ("ACTOR-0", "ACTOR-1"),
            (0.0, 1.0), (0.8, 0.8), (0.0, 0.0), (0.9, 0.9), (0.8, 0.8),
            (((True, True, True, True), 0.7),
             ((True, False, True, True), 0.3)),
            "MECH-001",
        )
        builder = SyntheticWorldBuilder()
        world = builder.generate(world_config, d2_config)
        replay = builder.generate(world_config, d2_config)
        world.validate()
        from c10s_synthetic_components import (
            NeedPreZStipulation, materialize_need_prez_truth,
        )
        stipulations = tuple(
            NeedPreZStipulation(
                unit_id=unit.unit_id,
                b1_id=f"B1-{index:03d}",
                service_instance_id=f"SVC-{index:03d}",
                contract_id="C10S-SVC-REQUEST-PROCESSOR",
                contract_version="1.0.0",
                instance_version=1,
                package_version="B1-PACKAGE-001",
                baseline_record_id=f"BASELINE-{index:03d}",
                baseline_time="t-1",
                stipulation=("FOCAL_INCLUSION", "FOCAL_EXCLUSION",
                             "SEMANTIC_INDETERMINACY", "FOCAL_INCLUSION")[index - 1],
                rule_version="NEED-RULE-001",
                basis_ref=f"RESERVED-STIPULATION-{index:03d}",
            )
            for index, unit in enumerate(world.units, start=1)
        )
        need_truth = materialize_need_prez_truth(world, stipulations)
        need_truth.validate(world)
        self.assertEqual(
            tuple(row.need_truth_state for row in need_truth.records),
            (1, 0, "?", 1),
        )
        self.assertEqual(
            tuple(row.unit_id for row in need_truth.records),
            tuple(unit.unit_id for unit in world.units),
        )
        self.assertTrue(all(
            type(row.instance_version) is int and row.instance_version == 1
            for row in need_truth.records
        ))
        with self.assertRaises(ContractError):
            materialize_need_prez_truth(world, stipulations[:-1])
        with self.assertRaises(ContractError):
            materialize_need_prez_truth(world, stipulations + (stipulations[0],))
        with self.assertRaises(ContractError):
            materialize_need_prez_truth(
                world, (stipulations[0],) * len(world.units)
            )
        self.assertEqual(world.roster_sha256, replay.roster_sha256)
        self.assertEqual(world.configuration_sha256, replay.configuration_sha256)
        self.assertEqual(tuple(row.mass for row in world.q_x), (0.1, 0.2, 0.3, 0.4))
        self.assertAlmostEqual(sum(row.mass for row in world.q_x), 1.0)
        self.assertEqual(len(world.units), 4)
        self.assertEqual({len(unit.x) for unit in world.units}, {2})
        self.assertEqual({len(unit.c_c) for unit in world.units}, {2})
        self.assertTrue(all(
            tuple(stage.z for stage in unit.d2_potentials.potentials_by_z) == (0, 1)
            for unit in world.units
        ))
        self.assertTrue(all(
            unit.d2_baseline.baseline_history_ref == qx.history_ref
            for unit, qx in zip(world.units, world.q_x)
        ))

    def test_world_builder_rejects_qx_masses_that_are_not_explicitly_normalized(self):
        from c10s_synthetic_components import SyntheticWorldBuilder, SyntheticWorldConfig
        config = SyntheticWorldConfig(
            world_id="WORLD-FIXTURE", world_version="001",
            dgp_id="D2-WORLD-FIXTURE", dgp_version="001",
            roster_id="ROSTER-FIXTURE", roster_version="001",
            unit_id_prefix="UE", n_units=2, seed=7,
            x_dimension=1, h0_distribution=(("H0-A", 1.0),),
            c_c_dimension=1, c_c_component_probability=1.0,
            focal_accessible_pre_probability=0.0,
            c_auth_base_probability=1.0, c_resource_probability=1.0,
            c_capacity_probability=1.0, c_info_probability=1.0,
            c_domain_probability=1.0, c_other_probability=1.0,
            q_x_mass_by_unit=(0.5, 0.6),
        )
        with self.assertRaises(ContractError):
            config.validate()


    def structural_snapshot(self, *, exhaustive=True, horizon=5.0):
        return StructuralSnapshot(
            "SNAP-001", "001", "WORLD-001", "001", "DGP-001", "001",
            "UE-001", 0, "BOUNDARY-001", "CONTEXT-001", horizon,
            (
                StructuralTransformation("TAU-1", "v1", "SNAP-001", 1),
                StructuralTransformation("TAU-2", "v1", "SNAP-001", 1),
                StructuralTransformation("TAU-3", "v1", "SNAP-001", "?"),
            ),
            exhaustive, exhaustive, exhaustive, exhaustive, "CATALOG-001",
        )

    def test_reach_confirmed_by_one_route_even_if_alternative_is_unknown(self):
        snapshot = self.structural_snapshot()
        routes = (
            StructuralRoute(
                "ROUTE-VALID", "S-TARGET",
                (StructuralRouteStep("TAU-1", "S0", "S1", 1, duration=1.0),),
                (), 1, "FOCAL",
            ),
            StructuralRoute(
                "ROUTE-UNKNOWN", "S-TARGET",
                (StructuralRouteStep("TAU-3", "S0", "S2", 1, duration=1.0),),
                (), 1, "ALTERNATIVE",
            ),
        )
        result = StructuralReachabilityEngine().evaluate(
            snapshot, routes, enumeration_complete=True,
        )
        self.assertEqual(dict(result.target_states)["S-TARGET"], 1)
        self.assertEqual(result.route_evaluations[1].route_state, "?")

    def test_reach_zero_requires_exhaustive_catalog_and_completed_enumeration(self):
        snapshot = self.structural_snapshot()
        blocked = StructuralRoute(
            "ROUTE-BLOCKED", "S-TARGET",
            (StructuralRouteStep("TAU-1", "S0", "S1", 0, duration=1.0),),
            (), 1, "FOCAL",
        )
        exhaustive = StructuralReachabilityEngine().evaluate(
            snapshot, (blocked,), enumeration_complete=True,
        )
        incomplete = StructuralReachabilityEngine().evaluate(
            snapshot, (blocked,), enumeration_complete=False,
        )
        self.assertEqual(dict(exhaustive.target_states)["S-TARGET"], 0)
        self.assertEqual(dict(incomplete.target_states)["S-TARGET"], "?")

    def test_accessibility_is_not_applicability_or_execution(self):
        snapshot = self.structural_snapshot()
        route = StructuralRoute(
            "ROUTE-NOT-APPLICABLE", "S-TARGET",
            (StructuralRouteStep("TAU-1", "S0", "S1", 0, duration=1.0),),
            (), 1, "FOCAL",
        )
        result = StructuralReachabilityEngine().evaluate(
            snapshot, (route,), enumeration_complete=True,
        )
        self.assertEqual(snapshot.transformations[0].accessible_state, 1)
        self.assertEqual(result.route_evaluations[0].route_state, 0)

    def test_truncated_or_over_horizon_route_cannot_establish_reach(self):
        snapshot = self.structural_snapshot(horizon=1.0)
        route = StructuralRoute(
            "ROUTE-LONG", "S-TARGET",
            (StructuralRouteStep("TAU-1", "S0", "S1", 1, duration=2.0),),
            (), 1, "FOCAL",
        )
        result = StructuralReachabilityEngine().evaluate(
            snapshot, (route,), enumeration_complete=False, search_truncated=True,
        )
        self.assertEqual(result.route_evaluations[0].route_state, 0)
        self.assertTrue(result.search_truncated)
        with self.assertRaises(ContractError):
            StructuralReachabilityEngine().evaluate(
                snapshot, (route,), enumeration_complete=True, search_truncated=True,
            )


    def test_structural_reachability_is_bound_to_every_world_unit_and_z_potential(self):
        from c10s_synthetic_components import SyntheticWorldBuilder, SyntheticWorldConfig
        d2_config = D2MechanismConfig(
            "D2-WORLD", "001", ("POL-0", "POL-1"), ("001", "001"),
            ("ART-0", "ART-1"), ("ACT-0", "ACT-1"),
            (0.0, 1.0), (0.8, 0.8), (0.0, 0.0), (0.9, 0.9), (0.8, 0.8),
            (((True, True, True, True), 1.0),), "MECH-001",
        )
        config = SyntheticWorldConfig(
            "WORLD-REACH", "001", "D2-WORLD", "001", "ROSTER-REACH", "001",
            "UE", 2, 91, 1, (("H0", 1.0),), 1, 1.0,
            0.5, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, (0.5, 0.5),
        )
        world = SyntheticWorldBuilder().generate(config, d2_config)
        snapshots, routes, complete, truncated = {}, {}, {}, {}
        for unit in world.units:
            for z in (0, 1):
                key = (unit.unit_id, z)
                snap_id = f"SNAP-{unit.unit_id}-Z{z}"
                snapshots[key] = StructuralSnapshot(
                    snap_id, "001", world.world_id, world.world_version,
                    world.dgp_id, world.dgp_version, unit.unit_id, z,
                    "BOUNDARY-001", "CONTEXT-001", 2.0,
                    (StructuralTransformation(f"TAU-{unit.unit_id}-Z{z}", "v1", snap_id, 1),),
                    True, True, True, True, "CATALOG-001",
                )
                routes[key] = (StructuralRoute(
                    f"ROUTE-{unit.unit_id}-Z{z}", f"TARGET-{unit.unit_id}-Z{z}",
                    (StructuralRouteStep(f"TAU-{unit.unit_id}-Z{z}", "S0", "S1", 1, duration=1.0),),
                    (), 1, "FOCAL",
                ),)
                complete[key] = True
                truncated[key] = False
        result = evaluate_synthetic_world_reachability(
            world, snapshots, routes,
            {key: (f"TARGET-{key[0]}-Z{key[1]}",) for key in snapshots},
            complete, truncated,
        )
        result.validate(world)
        self.assertEqual(len(result.unit_potential_results), 4)
        self.assertEqual(
            {(row.unit_id, row.z) for row in result.unit_potential_results},
            {(unit.unit_id, z) for unit in world.units for z in (0, 1)},
        )
        self.assertTrue(all(
            next(iter(row.result.target_states))[1] == 1
            for row in result.unit_potential_results
        ))


    def test_no_route_is_zero_only_when_explicit_target_universe_is_exhaustive(self):
        snapshot = self.structural_snapshot()
        engine = StructuralReachabilityEngine()
        exhaustive = engine.evaluate(
            snapshot, (), enumeration_complete=True,
            target_states=("S-TARGET-ABSENT",),
        )
        incomplete = engine.evaluate(
            snapshot, (), enumeration_complete=False,
            target_states=("S-TARGET-ABSENT",),
        )
        self.assertEqual(dict(exhaustive.target_states)["S-TARGET-ABSENT"], 0)
        self.assertEqual(dict(incomplete.target_states)["S-TARGET-ABSENT"], "?")


    def test_declared_absent_target_is_preserved_alongside_targets_with_routes(self):
        snapshot = self.structural_snapshot()
        route = StructuralRoute(
            "ROUTE-PRESENT", "S-TARGET-PRESENT",
            (StructuralRouteStep("TAU-1", "S0", "S1", 1, duration=1.0),),
            (), 1, "FOCAL",
        )
        result = StructuralReachabilityEngine().evaluate(
            snapshot, (route,), enumeration_complete=True,
            target_states=("S-TARGET-PRESENT", "S-TARGET-ABSENT"),
        )
        self.assertEqual(dict(result.target_states), {
            "S-TARGET-ABSENT": 0,
            "S-TARGET-PRESENT": 1,
        })


    def structural_state_snapshot(self, snapshot_id, timepoint, atoms, *, unit="UE-1", z=0,
                                   complete=(("U", True), ("R", True), ("C", True), ("X", True))):
        return TransformationalStateSnapshot(
            snapshot_id, "001", "WORLD-DELTA", "001", "DGP-DELTA", "001",
            unit, z, timepoint, "BOUNDARY-1", "CONTEXT-1", "CATALOG-1",
            tuple(atoms), tuple(complete),
        )

    def evidence_state(self, evidence_id, *, coverage="COMPLETE", source="SRC-1"):
        return EvidenceStateSnapshot(
            evidence_id, (source,), coverage, "VALID", f"PROV-{evidence_id}",
            "EVIDENCE-001", "ADJUDICATION-001",
        )

    def test_delta_t_acc_materializes_u_r_c_x_separately_from_evidence_delta(self):
        baseline_atoms = (
            StructuralAtom("U", "TAU-FOCAL", "TRANSFORMATION", "v1", 0, (("kind", "migration"),)),
            StructuralAtom("U", "TAU-ALT", "TRANSFORMATION", "v1", 1, (("kind", "fallback"),)),
            StructuralAtom("R", "REL-1", "RELATION", "v1", 1, (("from", "S0"), ("to", "S1"))),
            StructuralAtom("C", "COND-1", "CONDITION", "v1", 1, (("authorization", "true"),)),
            StructuralAtom("X", "CTX-1", "CONTEXT", "v1", 1, (("environment", "A"),)),
        )
        post_atoms = (
            StructuralAtom("U", "TAU-FOCAL", "TRANSFORMATION", "v2", 1, (("kind", "migration"),)),
            StructuralAtom("U", "TAU-ALT", "TRANSFORMATION", "v1", 1, (("kind", "fallback"),)),
            StructuralAtom("R", "REL-1", "RELATION", "v1", 1, (("from", "S0"), ("to", "S1"))),
            StructuralAtom("C", "COND-1", "CONDITION", "v1", 1, (("authorization", "true"),)),
            StructuralAtom("X", "CTX-1", "CONTEXT", "v1", 1, (("environment", "A"),)),
        )
        result = TransformationalDeltaEngine().evaluate(
            self.structural_state_snapshot("SNAP-B", "BASELINE", baseline_atoms),
            self.structural_state_snapshot("SNAP-P", "POST", post_atoms),
            evidence_baseline=self.evidence_state("E-B", coverage="PARTIAL"),
            evidence_post=self.evidence_state("E-P", coverage="COMPLETE", source="SRC-2"),
        )
        self.assertEqual(result.delta_state, 1)
        self.assertEqual(len(result.delta_u), 2)
        focal = next(row for row in result.delta_u if row.baseline_id == "TAU-FOCAL")
        self.assertEqual((focal.change_kind, focal.change_state), ("MODIFIED", 1))
        self.assertTrue(all(row.change_state == 0 for rows in (result.delta_r, result.delta_c, result.delta_x) for row in rows))
        self.assertTrue(result.evidence_delta.changed)
        self.assertEqual(result.delta_state, 1)

    def test_evidence_improvement_alone_does_not_create_delta_t_acc(self):
        atoms = (
            StructuralAtom("U", "TAU-1", "TRANSFORMATION", "v1", 1, (("kind", "convert"),)),
            StructuralAtom("R", "REL-1", "RELATION", "v1", 1, (("edge", "a-b"),)),
            StructuralAtom("C", "COND-1", "CONDITION", "v1", 1, (("rule", "r1"),)),
            StructuralAtom("X", "CTX-1", "CONTEXT", "v1", 1, (("state", "s0"),)),
        )
        result = TransformationalDeltaEngine().evaluate(
            self.structural_state_snapshot("SNAP-B", "BASELINE", atoms),
            self.structural_state_snapshot("SNAP-P", "POST", atoms),
            evidence_baseline=self.evidence_state("E-B", coverage="PARTIAL"),
            evidence_post=self.evidence_state("E-P", coverage="COMPLETE"),
        )
        self.assertEqual(result.delta_state, 0)
        self.assertTrue(result.evidence_delta.changed)

    def test_unknown_identity_correspondence_propagates_unknown_not_add_remove(self):
        before = (StructuralAtom("U", "TAU-OLD", "TRANSFORMATION", "v1", 1, (("kind", "convert"),)),)
        after = (StructuralAtom("U", "TAU-NEW", "TRANSFORMATION", "v2", 1, (("kind", "convert"),)),)
        result = TransformationalDeltaEngine().evaluate(
            self.structural_state_snapshot("SNAP-B", "BASELINE", before),
            self.structural_state_snapshot("SNAP-P", "POST", after),
            identity_matches=(StructuralIdentityMatch("TAU-OLD", "TAU-NEW", "?"),),
            evidence_baseline=self.evidence_state("E-B"),
            evidence_post=self.evidence_state("E-P"),
        )
        self.assertEqual(result.delta_state, "?")
        self.assertEqual(result.entries[0].change_kind, "UNKNOWN")

    def test_incomplete_component_cannot_turn_unmatched_atom_into_confirmed_addition(self):
        before = ()
        after = (StructuralAtom("R", "REL-NEW", "RELATION", "v1", 1, (("edge", "a-b"),)),)
        incomplete = (("U", True), ("R", False), ("C", True), ("X", True))
        result = TransformationalDeltaEngine().evaluate(
            self.structural_state_snapshot("SNAP-B", "BASELINE", before, complete=incomplete),
            self.structural_state_snapshot("SNAP-P", "POST", after, complete=incomplete),
            evidence_baseline=self.evidence_state("E-B"),
            evidence_post=self.evidence_state("E-P"),
        )
        self.assertEqual(result.delta_r[0].change_kind, "UNKNOWN")
        self.assertEqual(result.delta_state, "?")

    def test_noncomparable_snapshots_and_outcome_value_fields_are_rejected(self):
        atoms = (StructuralAtom("U", "TAU-1", "TRANSFORMATION", "v1", 1, (("kind", "convert"),)),)
        before = self.structural_state_snapshot("SNAP-B", "BASELINE", atoms)
        after = TransformationalStateSnapshot(
            "SNAP-P", "001", "WORLD-DELTA", "001", "DGP-DELTA", "001",
            "UE-OTHER", 0, "POST", "BOUNDARY-1", "CONTEXT-1", "CATALOG-1",
            atoms, (("U", True), ("R", True), ("C", True), ("X", True)),
        )
        with self.assertRaises(ContractError):
            TransformationalDeltaEngine().evaluate(
                before, after, evidence_baseline=self.evidence_state("E-B"),
                evidence_post=self.evidence_state("E-P"),
            )
        with self.assertRaises(ContractError):
            StructuralAtom("X", "CTX-1", "CONTEXT", "v1", 1, (("Outcome", "post"),)).validate()

    def test_d2_world_generator_materializes_structural_snapshots_for_every_potential(self):
        from c10s_synthetic_components import SyntheticWorldBuilder, SyntheticWorldConfig
        d2_config = D2MechanismConfig(
            "D2-DELTA", "001", ("POL-0", "POL-1"), ("001", "001"),
            ("ART-0", "ART-1"), ("ACT-0", "ACT-1"),
            (1.0, 1.0), (1.0, 1.0), (0.0, 0.0), (1.0, 1.0), (1.0, 1.0),
            (((True, True, True, True), 1.0),), "MECH-001",
        )
        config = SyntheticWorldConfig(
            "WORLD-DELTA", "001", "D2-DELTA", "001", "ROSTER-DELTA", "001",
            "UE", 2, 92, 1, (("H0", 1.0),), 1, 1.0,
            0.5, 0.0, 1.0, 1.0, 1.0, 1.0, 1.0, (0.5, 0.5),
        )
        structural_config = D2StructuralGenerationConfig(
            "STRUCTURAL-D2-MIN", "001", "TAU-FOCAL", "v1",
            "BOUNDARY-1", "CONTEXT-1", "CATALOG-1",
            (
                StructuralAtom("U", "TAU-ALT", "TRANSFORMATION", "v1", 1, (("kind", "alternative"),)),
                StructuralAtom("R", "REL-1", "RELATION", "v1", 0, (("edge", "focal-route-closed"),)),
                StructuralAtom("C", "COND-1", "CONDITION", "v1", 0, (("authorization", "false"),)),
                StructuralAtom("X", "CTX-1", "CONTEXT", "v1", 1, (("environment", "A"),)),
            ),
            transition_rules=(
                StructuralTransitionRule(
                    StructuralAtom("R", "REL-1", "RELATION", "v1", 1, (("edge", "focal-route-open"),)),
                    "MODIFY", "c_dep_star",
                ),
                StructuralTransitionRule(
                    StructuralAtom("C", "COND-1", "CONDITION", "v1", 1, (("authorization", "true"),)),
                    "MODIFY", "s_install",
                ),
            ),
        )
        reach_config = D2ReachGenerationConfig(
            "REACH-D2-MIN", "001", 5.0,
            ("TAU-FOCAL", "TAU-ALT"),
            ("TARGET-FOCAL", "TARGET-ABSENT"),
            (D2ReachRouteTemplate(
                "ROUTE-FOCAL", "TARGET-FOCAL",
                (
                    D2ReachStepTemplate("TAU-FOCAL", "S0", "S1", 1, predicate_atom_bindings=(("AUTH", "C", "COND-1"),)),
                    D2ReachStepTemplate("TAU-ALT", "S1", "S2", 1),
                ),
                (("R", "REL-1"),), 1, "FOCAL",
            ),),
            True, True, True, True, True, False,
        )
        trajectory_config = D2TrajectoryGenerationConfig(
            "TRAJECTORY-D2-MIN", "001",
            (("TARGET-FOCAL", 1.0), ("TARGET-ABSENT", 1.0)),
            (("ROUTE-FOCAL", 1.0),),
            (("ROUTE-FOCAL", 1.0),),
            (("TAU-FOCAL", 1.0), ("TAU-ALT", 1.0)),
            "FIXTURE-SEED-001",
        )
        world, pairs, reach, trajectories = SyntheticWorldBuilder().generate_complete_with_trajectories(
            config, d2_config, structural_config, reach_config, trajectory_config,
        )
        deltas = evaluate_d2_structural_deltas(world, pairs)
        self.assertEqual(set(pairs), {(unit.unit_id, z) for unit in world.units for z in (0, 1)})
        self.assertEqual(len(deltas), 4)
        self.assertTrue(all(delta.delta_state == 1 for delta in deltas))
        self.assertTrue(all(any(row.baseline_id == "TAU-FOCAL" and row.change_kind == "MODIFIED"
                                for row in delta.delta_u) for delta in deltas))
        self.assertTrue(all(delta.evidence_delta.changed is False for delta in deltas))
        self.assertTrue(all(
            any(row.change_kind == "MODIFIED" and row.baseline_id == "REL-1" for row in delta.delta_r)
            and any(row.change_kind == "MODIFIED" and row.baseline_id == "COND-1" for row in delta.delta_c)
            and len(delta.delta_x) == 1
            for delta in deltas
        ))
        self.assertEqual(len(reach.contrasts), 4)
        self.assertTrue(all(
            dict(row.baseline.target_states)["TARGET-FOCAL"] == 0
            and dict(row.post.target_states)["TARGET-FOCAL"] == 1
            and dict(row.post.target_states)["TARGET-ABSENT"] == 0
            and dict(row.delta_by_target)["TARGET-FOCAL"] == 1
            for row in reach.contrasts
        ))
        self.assertEqual(len(trajectories.trajectories), 8)
        replay = evaluate_d2_potential_trajectories(
            world, reach, reach_config, trajectory_config,
        )
        self.assertEqual(trajectories.result_sha256, replay.result_sha256)
        by_key = {(row.unit_id, row.z, row.target_state): row for row in trajectories.trajectories}
        for unit in world.units:
            self.assertEqual(by_key[(unit.unit_id, 0, "TARGET-FOCAL")].trajectory_status, "NOT_REACHABLE")
            self.assertEqual(by_key[(unit.unit_id, 1, "TARGET-FOCAL")].trajectory_status, "COMPLETED")
            self.assertEqual(by_key[(unit.unit_id, 1, "TARGET-FOCAL")].terminal_state, "S2")
            self.assertEqual(by_key[(unit.unit_id, 0, "TARGET-ABSENT")].trajectory_status, "NOT_REACHABLE")

        no_selection_config = D2TrajectoryGenerationConfig(
            "TRAJECTORY-NO-SELECTION", "001",
            (("TARGET-FOCAL", 0.0), ("TARGET-ABSENT", 0.0)),
            (("ROUTE-FOCAL", 1.0),), (("ROUTE-FOCAL", 1.0),),
            (("TAU-FOCAL", 1.0), ("TAU-ALT", 1.0)), "FIXTURE-SEED-002",
        )
        no_selection = evaluate_d2_potential_trajectories(
            world, reach, reach_config, no_selection_config,
        )
        self.assertTrue(all(
            row.reach_state == 1 and row.selection_state == 0
            and row.trajectory_status == "NOT_SELECTED"
            for row in no_selection.trajectories if row.z == 1 and row.target_state == "TARGET-FOCAL"
        ))

        execution_failure_config = D2TrajectoryGenerationConfig(
            "TRAJECTORY-EXECUTION-FAIL", "001",
            (("TARGET-FOCAL", 1.0), ("TARGET-ABSENT", 1.0)),
            (("ROUTE-FOCAL", 1.0),), (("ROUTE-FOCAL", 0.0),),
            (("TAU-FOCAL", 1.0), ("TAU-ALT", 1.0)), "FIXTURE-SEED-003",
        )
        execution_failure = evaluate_d2_potential_trajectories(
            world, reach, reach_config, execution_failure_config,
        )
        self.assertTrue(all(
            row.reach_state == 1 and row.selection_state == 1
            and row.execution_state == 0 and row.trajectory_status == "EXECUTION_FAILED"
            for row in execution_failure.trajectories if row.z == 1 and row.target_state == "TARGET-FOCAL"
        ))

        # V_cont is adjudicated from its own EventHistory truth, never inferred
        # from Reach or trajectory. This deliberately adversarial fixture has
        # opposite trajectory/continuity patterns across the two potentials.
        histories_by_unit_z = {}
        for unit in world.units:
            for z in (0, 1):
                initial = (
                    FunctionalState(False, "NO_ADMISSION")
                    if z == 0 else FunctionalState(True, "NO_ADMISSION")
                )
                history_id = f"{unit.unit_id}-EH-Z{z}"
                histories_by_unit_z[(unit.unit_id, z)] = EventHistory(
                    history_id=history_id, history_version="001", run_id="RUN-DELTA",
                    world_id=world.world_id, world_version=world.world_version,
                    dgp_version=world.dgp_version, unit_id=unit.unit_id,
                    potential_id=f"{unit.unit_id}-POTENTIAL-Z{z}",
                    adjudication_rules_version="AB1-001",
                    support_start=Decimal("0"), support_end=Decimal("4"),
                    initial_post_z_state=initial, transitions=(),
                    expected_transition_ids=(), scope_declared_complete=True,
                    generation_complete=True, representation_complete=True,
                )
        vcont_grid = IntervalGrid(
            (Decimal("0"), Decimal("2"), Decimal("4")), "GRID-D2", "001",
        )
        vcont_truth = SyntheticWorldBuilder().evaluate_complete_vcont_truth(
            world, histories_by_unit_z, vcont_grid,
        )
        self.assertEqual(len(vcont_truth.potential_truth), 4)
        self.assertAlmostEqual(vcont_truth.finite_population_itt_z_v_cont, -1.0)
        self.assertTrue(all(
            row.v_cont_truth == (1.0 if row.z == 0 else 0.0)
            for row in vcont_truth.potential_truth
        ))

        vector_0 = (0.0, 0.0, 0.0, 0.0)
        vector_1 = (1.0, 1.0, 1.0, 1.0)
        g_a0 = tuple(JointPolicyHistory(row.history_ref, ((vector_0, 1.0),)) for row in world.q_x)
        g_a1 = tuple(JointPolicyHistory(row.history_ref, ((vector_1, 1.0),)) for row in world.q_x)
        feasible = {row.history_ref: (vector_0, vector_1) for row in world.q_x}
        r_common = tuple(
            RCommonPairCertificate(row.history_ref, "R-COMMON", "001",
                                   "R-COMMON-FP", "R-COMMON-FP", "COMMON_FIXED")
            for row in world.q_x
        )
        histories_by_policy = {}
        for qx in world.q_x:
            unit_id = next(unit.unit_id for unit in world.units
                           if unit.d2_baseline.baseline_history_ref == qx.history_ref)
            for vector in (vector_0, vector_1):
                is_zero_policy = vector == vector_0
                history = EventHistory(
                    history_id=f"{unit_id}-POLICY-{int(is_zero_policy)}",
                    history_version="001", run_id="RUN-THETA",
                    world_id=world.world_id, world_version=world.world_version,
                    dgp_version=world.dgp_version, unit_id=unit_id,
                    potential_id=f"{unit_id}-POLICY-POTENTIAL-{int(is_zero_policy)}",
                    adjudication_rules_version="AB1-001",
                    support_start=Decimal("0"), support_end=Decimal("4"),
                    initial_post_z_state=(
                        FunctionalState(False, "NO_ADMISSION") if is_zero_policy
                        else FunctionalState(True, "NO_ADMISSION")
                    ),
                    transitions=(), expected_transition_ids=(),
                    scope_declared_complete=True, generation_complete=True,
                    representation_complete=True,
                )
                histories_by_policy[(
                    qx.history_ref, digest(vector), "R-COMMON-FP",
                )] = history
        theta_vcont = compute_theta_a_vcont_truth_from_event_histories(
            world, world.q_x, g_a0, g_a1, feasible, r_common,
            histories_by_policy, vcont_grid,
            estimand_version="001", outcome_version="VCONT-001",
        )
        self.assertEqual(theta_vcont.theta_a_truth.outcome_id, "V_CONT")
        self.assertAlmostEqual(theta_vcont.theta_a_truth.theta_a_truth, -1.0)

        # Direct g_A assignment is a separate randomized intervention, not
        # the legacy package Z or scalar G assignment.
        policy_assignment_config = ThetaAPolicyAssignmentConfig(
            "G_A_DIRECT_RANDOMIZED", "001", "THETA-A-SEED-001",
            tuple((row.history_ref, 0.5) for row in world.q_x),
        )
        policy_assignments = generate_theta_a_policy_assignments(
            world, policy_assignment_config, g_a0, g_a1, feasible, r_common,
        )
        replay_assignments = generate_theta_a_policy_assignments(
            world, policy_assignment_config, g_a0, g_a1, feasible, r_common,
        )
        self.assertEqual(policy_assignments.result_sha256, replay_assignments.result_sha256)
        self.assertEqual(
            {row.history_ref for row in policy_assignments.assignments},
            {row.history_ref for row in world.q_x},
        )
        for assignment in policy_assignments.assignments:
            self.assertEqual(assignment.probability_a0, 0.5)
            self.assertEqual(assignment.probability_a1, 0.5)
            self.assertEqual(
                assignment.assigned_vector,
                vector_1 if assignment.assigned_arm == 1 else vector_0,
            )
        with self.assertRaises(ContractError):
            generate_theta_a_policy_assignments(
                world,
                ThetaAPolicyAssignmentConfig(
                    "G_A_NO_POSITIVITY", "001", "THETA-A-SEED-002",
                    tuple((row.history_ref, 1.0) for row in world.q_x),
                ),
                g_a0, g_a1, feasible, r_common,
            )

        realized_policy_histories = []
        for assignment in policy_assignments.assignments:
            realized_policy_histories.append(EventHistory(
                history_id=f"{assignment.unit_id}-REALIZED-GA",
                history_version="001", run_id="RUN-THETA",
                world_id=world.world_id, world_version=world.world_version,
                dgp_version=world.dgp_version, unit_id=assignment.unit_id,
                potential_id=theta_a_event_history_potential_id(assignment),
                adjudication_rules_version="AB1-001",
                support_start=Decimal("0"), support_end=Decimal("4"),
                initial_post_z_state=(
                    FunctionalState(False, "NO_ADMISSION") if assignment.assigned_arm == 0
                    else FunctionalState(True, "NO_ADMISSION")
                ),
                transitions=(), expected_transition_ids=(),
                scope_declared_complete=True, generation_complete=True,
                representation_complete=True,
            ))
        selected_policy_histories = select_theta_a_realized_histories(
            policy_assignments, realized_policy_histories,
        )
        self.assertEqual(len(selected_policy_histories.selected_history_id_by_unit), len(world.units))
        self.assertEqual(
            {row[0] for row in selected_policy_histories.selected_history_id_by_unit},
            {unit.unit_id for unit in world.units},
        )
        with self.assertRaises(ContractError):
            select_theta_a_realized_histories(
                policy_assignments, realized_policy_histories[:-1],
            )
        with self.assertRaises(ContractError):
            compute_theta_a_vcont_truth_from_event_histories(
                world, world.q_x, g_a0, g_a1, feasible, r_common,
                {key: value for key, value in histories_by_policy.items()
                 if key[1] != digest(vector_1)},
                vcont_grid, estimand_version="001", outcome_version="VCONT-001",
            )
        self.assertTrue(all(
            row.trajectory_status == "NOT_REACHABLE"
            for row in trajectories.trajectories if row.z == 0 and row.target_state == "TARGET-FOCAL"
        ))
        self.assertTrue(all(
            row.trajectory_status == "COMPLETED"
            for row in trajectories.trajectories if row.z == 1 and row.target_state == "TARGET-FOCAL"
        ))
        with self.assertRaises(ContractError):
            evaluate_d2_vcont_potential_truth(
                world, {key: value for key, value in histories_by_unit_z.items() if key[1] == 0},
                vcont_grid,
            )


    def test_empty_incomplete_structural_universe_is_unknown_not_zero(self):
        incomplete = (("U", False), ("R", False), ("C", False), ("X", False))
        before = self.structural_state_snapshot("SNAP-B", "BASELINE", (), complete=incomplete)
        after = self.structural_state_snapshot("SNAP-P", "POST", (), complete=incomplete)
        result = TransformationalDeltaEngine().evaluate(
            before, after, evidence_baseline=self.evidence_state("E-B"),
            evidence_post=self.evidence_state("E-P"),
        )
        self.assertEqual(result.delta_state, "?")
        self.assertEqual(dict(result.component_completeness), {"U": False, "R": False, "C": False, "X": False})


if __name__ == "__main__":
    unittest.main()
