"""Regressions for continuous interval S3 measurement."""
from decimal import Decimal
import unittest

from c10s_synthetic_components import (
    EventHistoryGenerationSpec, FunctionalState, FunctionalStateChange,
    IntervalGrid, generate_event_history,
)
from theta_a_interval_observation import (
    IntervalMonitorConfig, project_interval_s3, validate_interval_s3_observations,
)


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
        with self.assertRaises(Exception):
            validate_interval_s3_observations(records[:1], self.history, self.grid, self.config)

    def test_point_sampling_cannot_be_declared_continuous_monitoring(self):
        config = IntervalMonitorConfig(
            "MONITOR", "1", "POINT_SAMPLE", 0.0,
            Decimal("0"), Decimal("0"),
        )
        with self.assertRaises(Exception):
            project_interval_s3(self.history, self.grid, config, seed=1)


if __name__ == "__main__":
    unittest.main()
