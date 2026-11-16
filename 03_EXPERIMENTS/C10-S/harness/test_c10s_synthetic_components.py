import unittest
from decimal import Decimal

from vcont_integrated_harness import (Analyzer, EvidenceCandidate, Evaluator, Generator,
                                      Sealer, benchmark_scenarios, contract_for)

from c10s_synthetic_components import (
    ContractError, D2Baseline, D2MechanismConfig, EventHistory,
    FunctionalState, FunctionalTransition, IntervalGrid,
    JointPolicyHistory, QXHistoryMass, RCommonPairCertificate,
    S3SequenceKernelRow, S3ObservationConfig, adjudicate_intervals,
    compute_theta_a_truth, evaluate_theta_a_output, generate_d2_potentials, project_s3,
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


if __name__ == "__main__":
    unittest.main()
