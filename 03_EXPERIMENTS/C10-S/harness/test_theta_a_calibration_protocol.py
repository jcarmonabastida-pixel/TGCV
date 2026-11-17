from __future__ import annotations

import hashlib
import json
import unittest
from dataclasses import replace
from decimal import Decimal
from types import SimpleNamespace

from theta_a_calibration_protocol import (
    ThetaACalibrationDesign,
    ThetaACalibrationError,
    ThetaACalibrationScenario,
    ThetaAReplicateRecord,
    build_theta_a_seed_bank,
    s3_seeds_by_unit,
    theta_a_pipeline_inference_options,
    summarize_theta_a_calibration,
    validate_theta_a_seed_banks,
    _validate_interval_s3_seed_provenance,
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
        )

    def _record(self, row, expected, observed, point, lower, upper, covered, width, requested_level):
        def fp(value):
            return hashlib.sha256(value.encode("utf-8")).hexdigest()
        return ThetaAReplicateRecord(
            row.scenario_id, row.scenario_version, row.n_units,
            row.outer_world_id, row.assignment_replicate, row.world_id, row.run_id,
            expected, observed, 0.2, point, lower, upper, covered, width, requested_level,
            fp("world|" + row.outer_world_id), fp("policy-design"),
            fp(row.randomization_salt), fp(row.run_id + "|evidence"),
            fp(row.run_id + "|analyzer"),
        )

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
        self.assertEqual(summary.type_i_error_status, "NOT_DEFINED_NO_TEST_PROCEDURE")
        self.assertEqual(summary.power_status, "NOT_DEFINED_NO_TEST_PROCEDURE")

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
        )
        design = self._design(scenario)
        assignments = build_theta_a_seed_bank(design, "calibration")
        records = tuple(
            self._record(row, "NOT_IDENTIFIED", "NOT_IDENTIFIED", None, None, None, None, None, None)
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
            scenario_id="THETA_A_PARTIAL", scenario_version="1.0",
            world_version="world-v1", dgp_id="C10S-THETA-A", dgp_version="1.0",
            roster_version="1.0", unit_id_prefix="unit",
            expected_identification="PARTIALLY_IDENTIFIED", unit_independence_certified=False,
        )
        with self.assertRaises(ThetaACalibrationError):
            self._design(scenario).validate()


if __name__ == "__main__":
    unittest.main()
