"""Regressions for continuous interval S3 measurement."""
from decimal import Decimal
import unittest

from c10s_synthetic_components import (
    ContractError, EventHistoryGenerationSpec, FunctionalState, FunctionalStateChange,
    IntervalGrid, generate_event_history,
)
from theta_a_interval_observation import (
    IntervalMonitorConfig, ThetaAIntervalObservationRecord,
    candidate_from_theta_a_interval_records, project_interval_s3,
    validate_interval_s3_observations,
)
from theta_a_observation_harness import ThetaAIntervalSealer
from theta_a_analyzer import ThetaAObservationAnalysisContract, ThetaAObservationAnalyzer


class IntervalObservationTests(unittest.TestCase):
    def setUp(self):
        self.grid = IntervalGrid(
            (Decimal("0"), Decimal("1"), Decimal("2")), "GRID", "1",
        )
        self.config = IntervalMonitorConfig(
            "MONITOR", "1", "CONTINUOUS_EVENT_COVERAGE", 0.0,
            Decimal("0.1"), Decimal("0.2"),
        )
        good = FunctionalState(True, "ADMIT")
        bad = FunctionalState(True, "NO_ADMISSION")
        self.history = generate_event_history(EventHistoryGenerationSpec(
            history_id="H1", history_version="1", run_id="RUN",
            world_id="WORLD", world_version="1", dgp_version="DGP1",
            unit_id="U1", potential_id="U1:GA:1",
            adjudication_rules_version="RULES1",
            support_start=Decimal("0"), support_end=Decimal("2"),
            initial_post_z_state=good,
            changes=(
                FunctionalStateChange(
                    Decimal("0.5"), bad, "OUTAGE", "DGP#OUTAGE",
                ),
                FunctionalStateChange(
                    Decimal("0.75"), good, "RECOVERY", "DGP#RECOVERY",
                ),
            ),
        ))

    def test_continuous_monitor_detects_transient_interruption_missed_by_endpoints(self):
        records = project_interval_s3(self.history, self.grid, self.config, seed=17)
        self.assertEqual([row.observed_compliance for row in records], [False, True])
        self.assertEqual([row.observation_status for row in records], ["OBSERVED", "OBSERVED"])
        self.assertEqual(records[0].interval_start, Decimal("0"))
        self.assertEqual(records[0].interval_end, Decimal("1"))

    def test_missingness_is_explicit_and_deterministic(self):
        config = IntervalMonitorConfig(
            "MONITOR", "1", "CONTINUOUS_EVENT_COVERAGE", 1.0 - 1e-12,
            Decimal("0"), Decimal("0"),
        )
        a = project_interval_s3(self.history, self.grid, config, seed=42)
        b = project_interval_s3(self.history, self.grid, config, seed=42)
        self.assertEqual(a, b)
        self.assertTrue(all(row.observation_status == "MISSING" for row in a))
        self.assertTrue(all(row.observed_compliance is None for row in a))

    def test_contract_rejects_incomplete_or_misaligned_interval_coverage(self):
        records = project_interval_s3(self.history, self.grid, self.config, seed=5)
        validate_interval_s3_observations(records, self.history, self.grid, self.config)
        with self.assertRaises(ContractError):
            validate_interval_s3_observations(records[:1], self.history, self.grid, self.config)

    def test_point_sampling_cannot_be_declared_continuous_monitoring(self):
        config = IntervalMonitorConfig(
            "MONITOR", "1", "POINT_SAMPLE", 0.0,
            Decimal("0"), Decimal("0"),
        )
        with self.assertRaises(ContractError):
            project_interval_s3(self.history, self.grid, config, seed=1)


    def _focal_records(self, missing_arm1=False):
        rows = []
        for unit, history, arm, values in (
            ("U0", "H0", 0, (True, True)),
            ("U1", "H1", 1, ((None, True) if missing_arm1 else (False, True))),
        ):
            for index, value in enumerate(values):
                start = Decimal(index)
                end = Decimal(index + 1)
                rows.append(ThetaAIntervalObservationRecord(
                    run_id="RUN", unit_id=unit, history_ref=history,
                    assignment_bundle_sha256="ASSIGN", q_x_sha256="QX",
                    g_a0_sha256="GA0", g_a1_sha256="GA1", r_common_sha256="RC",
                    assigned_arm=arm, assignment_probability=0.5,
                    assigned_vector_sha256=f"VECTOR-{unit}",
                    policy_fingerprint=f"POLICY-{arm}", r_common_fingerprint="RC-FP",
                    history_id=f"HISTORY-{unit}", history_version="1",
                    history_content_sha256=f"HASH-{unit}", observation_id=f"OBS-{unit}-{index}",
                    interval_index=index, interval_start=start, interval_end=end,
                    observed_compliance=value,
                    observation_status="MISSING" if value is None else "OBSERVED",
                    coverage_mode="CONTINUOUS_EVENT_COVERAGE",
                    capture_time=end + Decimal("0.1"),
                    ingestion_time=end + Decimal("0.2"),
                    monitor_id="MONITOR", monitor_version="1",
                    grid_id="GRID", grid_version="1",
                ))
        return tuple(rows)

    def _focal_analysis(self, missing_arm1=False, confidence_level=None):
        records = self._focal_records(missing_arm1)
        candidate = candidate_from_theta_a_interval_records(records)
        sealed = ThetaAIntervalSealer().seal(candidate)
        contract = ThetaAObservationAnalysisContract(
            q_x_mass_by_history=(("H0", 0.5), ("H1", 0.5)),
            q_x_sha256="QX", assignment_bundle_sha256="ASSIGN",
            g_a0_sha256="GA0", g_a1_sha256="GA1", r_common_sha256="RC",
            probability_a1_by_history=(("H0", 0.5), ("H1", 0.5)) if confidence_level is not None else (),
            confidence_level=confidence_level,
            unit_independence_certified=confidence_level is not None,
        )
        result = ThetaAObservationAnalyzer().analyze(sealed, contract)
        return sealed, result

    def test_interval_sealer_and_analyzer_recover_complete_direct_ga_contrast(self):
        sealed, result = self._focal_analysis()
        self.assertEqual(sealed.manifest["temporal_resolution"], "INTERVAL_LEVEL")
        self.assertEqual(result.temporal_resolution, "INTERVAL_LEVEL")
        self.assertEqual(result.identification, "IDENTIFIED")
        self.assertAlmostEqual(result.point_estimate, -0.5)
        self.assertEqual(result.missing_interval_count, 0)
        self.assertEqual(result.measurement_lower_bound, -0.5)
        self.assertEqual(result.measurement_upper_bound, -0.5)

    def test_two_stage_hoeffding_interval_accounts_for_policy_draw_and_arm_randomization(self):
        _, result = self._focal_analysis(confidence_level=0.95)
        self.assertEqual(result.inference_method, "HOEFFDING_TWO_STAGE_BOUNDED_HT_V1")
        self.assertEqual(result.inference_confidence_level, 0.95)
        self.assertAlmostEqual(result.hoeffding_range_sum_squares, 8.0)
        radius = (0.5 * 8.0 * __import__("math").log(2.0 / 0.05)) ** 0.5
        self.assertAlmostEqual(result.inference_lower_bound, result.point_estimate - radius)
        self.assertAlmostEqual(result.inference_upper_bound, result.point_estimate + radius)

    def test_two_stage_hoeffding_interval_is_not_reported_after_missingness_abstention(self):
        _, result = self._focal_analysis(missing_arm1=True, confidence_level=0.95)
        self.assertEqual(result.identification, "INDETERMINATE")
        self.assertIsNone(result.inference_method)
        self.assertIsNone(result.inference_lower_bound)
        self.assertIsNone(result.inference_upper_bound)

    def test_interval_missingness_abstains_and_reports_measurement_only_bounds(self):
        sealed, result = self._focal_analysis(missing_arm1=True)
        self.assertEqual(result.identification, "INDETERMINATE")
        self.assertIsNone(result.point_estimate)
        self.assertEqual(result.abstention_reason, "INTERVAL_MISSINGNESS_REQUIRES_ABSTENTION")
        self.assertEqual(result.lower_bound, -1.0)
        self.assertEqual(result.upper_bound, 1.0)
        self.assertEqual(result.measurement_lower_bound, -0.5)
        self.assertEqual(result.measurement_upper_bound, 0.0)
        self.assertEqual(result.missing_interval_count, 1)
        self.assertEqual(result.total_interval_count, 4)

    def test_interval_sealer_rejects_mixed_grid_identity(self):
        rows = list(self._focal_records())
        rows[-1] = ThetaAIntervalObservationRecord(
            **{**rows[-1].__dict__, "grid_id": "OTHER-GRID"}
        )
        candidate = candidate_from_theta_a_interval_records(tuple(rows))
        with self.assertRaises(ContractError):
            ThetaAIntervalSealer().seal(candidate)


if __name__ == "__main__":
    unittest.main()
