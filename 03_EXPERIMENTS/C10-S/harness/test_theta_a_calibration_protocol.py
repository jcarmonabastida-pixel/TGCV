from __future__ import annotations

import unittest

from theta_a_calibration_protocol import (
    ThetaACalibrationDesign,
    ThetaACalibrationError,
    ThetaACalibrationScenario,
    ThetaAReplicateRecord,
    build_theta_a_seed_bank,
    s3_seeds_by_unit,
    summarize_theta_a_calibration,
    validate_theta_a_seed_banks,
)


class ThetaACalibrationProtocolTests(unittest.TestCase):
    def _design(self, scenario=None):
        scenario = scenario or ThetaACalibrationScenario(
            "THETA_A_IDEAL", "1.0", "IDENTIFIED", True,
            "unit-level potential histories and two-stage randomization are generated independently by unit",
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
        )

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
            self.assertEqual(len({x.randomization_salt for x in rows}), 2)
            self.assertEqual(len({x.s3_seed for x in rows}), 2)
            self.assertEqual(len({x.run_id for x in rows}), 2)
        self.assertEqual(
            len({x.world_seed for x in calibration if x.outer_world_id != "outer-000000"}), 1
        )
        self.assertFalse({x.world_seed for x in calibration} & {x.world_seed for x in evaluation})

    def test_seed_bank_rejects_incomplete_r_coverage(self):
        design = self._design()
        rows = build_theta_a_seed_bank(design, "calibration")
        with self.assertRaises(ThetaACalibrationError):
            validate_theta_a_seed_banks(rows[:-1], (), design=design)

    def test_s3_unit_seeds_are_stable_and_distinct(self):
        first = s3_seeds_by_unit(12345, ("u1", "u2", "u3"))
        second = s3_seeds_by_unit(12345, ("u1", "u2", "u3"))
        self.assertEqual(first, second)
        self.assertEqual(len(set(first.values())), 3)

    def test_identified_summary_aggregates_coverage_and_width_across_m(self):
        design = self._design()
        assignments = build_theta_a_seed_bank(design, "calibration")
        records = tuple(
            ThetaAReplicateRecord(
                row.scenario_id, row.scenario_version, row.n_units,
                row.outer_world_id, row.assignment_replicate, row.world_id, row.run_id,
                "IDENTIFIED", "IDENTIFIED", 0.2, 0.21,
                0.1, 0.3, True, 0.2, 0.95,
            )
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
        self.assertEqual(summary.type_i_error_status, "NOT_DEFINED_NO_TEST_PROCEDURE")
        self.assertEqual(summary.power_status, "NOT_DEFINED_NO_TEST_PROCEDURE")

    def test_missing_interval_is_not_dropped_from_coverage_denominator(self):
        design = self._design()
        assignments = build_theta_a_seed_bank(design, "calibration")
        records = []
        for index, row in enumerate(assignments):
            if index == 0:
                records.append(ThetaAReplicateRecord(
                    row.scenario_id, row.scenario_version, row.n_units,
                    row.outer_world_id, row.assignment_replicate, row.world_id, row.run_id,
                    "IDENTIFIED", "INDETERMINATE", 0.2, None,
                    None, None, None, None, 0.95,
                ))
            else:
                records.append(ThetaAReplicateRecord(
                    row.scenario_id, row.scenario_version, row.n_units,
                    row.outer_world_id, row.assignment_replicate, row.world_id, row.run_id,
                    "IDENTIFIED", "IDENTIFIED", 0.2, 0.21,
                    0.1, 0.3, True, 0.2, 0.95,
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
            "THETA_A_NO_SUPPORT", "1.0", "NOT_IDENTIFIED", False
        )
        design = self._design(scenario)
        assignments = build_theta_a_seed_bank(design, "calibration")
        records = tuple(
            ThetaAReplicateRecord(
                row.scenario_id, row.scenario_version, row.n_units,
                row.outer_world_id, row.assignment_replicate, row.world_id, row.run_id,
                "NOT_IDENTIFIED", "NOT_IDENTIFIED", 0.2, None,
                None, None, None, None, None,
            )
            for row in assignments
        )
        summary = summarize_theta_a_calibration(
            design, assignments, records, bank="calibration"
        )[0]
        metrics = {x.metric: x for x in summary.metrics}
        self.assertAlmostEqual(metrics["correct_abstention_rate"].mean, 1.0)
        self.assertAlmostEqual(metrics["false_identification_rate"].mean, 0.0)

    def test_partial_identification_is_rejected_until_bounds_are_adjudicated(self):
        scenario = ThetaACalibrationScenario(
            "THETA_A_PARTIAL", "1.0", "PARTIALLY_IDENTIFIED", False
        )
        with self.assertRaises(ThetaACalibrationError):
            self._design(scenario).validate()


if __name__ == "__main__":
    unittest.main()
