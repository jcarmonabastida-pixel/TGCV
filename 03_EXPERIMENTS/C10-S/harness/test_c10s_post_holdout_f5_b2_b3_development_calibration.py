from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from c10s_nested_mr_fixtures import tier_a_specs
from run_c10s_post_holdout_f5_b2_b3_development_calibration import (
    B3_B1000,
    B3_B4000,
    C0_B,
    C5_B,
    EXPECTED_CELLS,
    K_CALIBRATION,
    K_VALIDATION,
    SEED_SCHEDULE_ID,
    _component_gate,
    _optimizer_diagnostic_is_resolved,
    _rank_uncertainty,
    dataset_id,
    derive_seed,
    run_f5_bank,
    run_f5_endpoint_sensitivity,
    run_f5_development_calibration,
    select_b3_calibration_datasets,
    validate_seed_separation,
)


class F5DevelopmentCalibrationTests(unittest.TestCase):
    def setUp(self):
        self.spec = next(
            spec for spec in tier_a_specs()
            if spec.cell_id == "F5_beta22_M30_R20"
        )

    def test_frozen_development_roster_and_budgets(self):
        self.assertEqual(EXPECTED_CELLS, ("F5_beta22_M10_R5", "F5_beta22_M30_R20"))
        self.assertEqual((K_CALIBRATION, K_VALIDATION), (5000, 5000))
        self.assertEqual((C0_B, C5_B), (1000, 1000))
        self.assertEqual((B3_B1000, B3_B4000), (1000, 4000))
        self.assertEqual(SEED_SCHEDULE_ID, "C10S_POST_HOLDOUT_F1_F5_DEV_CAL_SEEDS_1.0")

    def test_seed_streams_are_stable_and_disjoint_from_historical_schedules(self):
        first = derive_seed("f5_optimizer_calibration_dataset", self.spec.cell_id, 12)
        self.assertEqual(first, derive_seed("f5_optimizer_calibration_dataset", self.spec.cell_id, 12))
        self.assertNotEqual(first, derive_seed("f5_optimizer_validation_dataset", self.spec.cell_id, 12))
        audit = validate_seed_separation(
            k_calibration=3, k_validation=2, b3_selected_per_cell=1,
        )
        self.assertEqual(audit["status"], "PASS")
        self.assertGreater(audit["historical_unique_seed_values_checked"], 0)
        self.assertEqual(audit["new_seed_values_checked"], audit["new_unique_seed_values"])

    def test_b3_selection_is_deterministic_and_uses_only_dataset_ids(self):
        ids = [dataset_id("calibration", self.spec.cell_id, i) for i in range(20)]
        first = select_b3_calibration_datasets(self.spec.cell_id, ids, n=5)
        second = select_b3_calibration_datasets(self.spec.cell_id, list(reversed(ids)), n=5)
        self.assertEqual(first, second)
        self.assertEqual(len(first), 5)
        self.assertEqual(len({item["dataset_id"] for item in first}), 5)
        self.assertTrue(all(len(item["selection_sha256"]) == 64 for item in first))

    def test_component_gate_enforces_all_three_frozen_conditions(self):
        passing = _component_gate({
            "conditional_coverage": 0.95,
            "coverage_wilson_95": [0.93, 0.97],
            "interval_emission_rate": 0.96,
            "abstention_count": 4,
            "abstention_reasons": [],
        })
        self.assertEqual(passing["status"], "PASS")
        self.assertTrue(passing["denominator_ok"])
        wrong_denominator = _component_gate({
            "n_datasets": 4999,
            "conditional_coverage": 0.95,
            "coverage_wilson_95": [0.93, 0.97],
            "interval_emission_rate": 0.96,
        }, expected_n=5000)
        self.assertEqual(wrong_denominator["status"], "FAIL_FROZEN_COMPONENT_GATE")
        failed_coverage = _component_gate({
            "conditional_coverage": 0.98,
            "coverage_wilson_95": [0.96, 0.99],
            "interval_emission_rate": 1.0,
        })
        self.assertEqual(failed_coverage["status"], "FAIL_FROZEN_COMPONENT_GATE")
        self.assertEqual(_component_gate(None)["status"], "FAIL_MISSING_METRIC")

    def test_optimizer_gate_accepts_only_complete_concordant_interior_audit(self):
        start = {
            "final_mean_logit": 0.1,
            "final_log_concentration": 0.5,
            "gradient_norm": 1e-8,
            "lower_mean_bound_distance": 1.0,
            "upper_mean_bound_distance": 2.0,
            "lower_concentration_bound_distance": 1.5,
            "upper_concentration_bound_distance": 3.0,
        }
        audit = {
            "status": "OPTIMIZER_CONCORDANT",
            "independent_optimizer_success": True,
            "selected_mean_logit": 0.1,
            "selected_log_concentration": 0.5,
            "selected_log_likelihood": -10.0,
            "selected_score_norm": 1e-7,
            "profile_log_concentration_curvature": -0.5,
            "independent_terminal_log_alpha": 0.2,
            "independent_terminal_log_beta": 0.3,
            "independent_score_norm": 1e-7,
            "absolute_log_likelihood_difference": 1e-9,
            "log_shape_parameter_distance": 1e-8,
            "starts": [dict(start) for _ in range(3)],
            "independent_observed_hessian": [[-2.0, 0.1], [0.1, -1.0]],
        }
        self.assertTrue(_optimizer_diagnostic_is_resolved({
            "fit_status": "INTERIOR",
            "optimizer_status": "OPTIMIZER_CONCORDANT",
            "optimizer_audit": audit,
        }))

    def test_optimizer_gate_fails_closed_on_missing_or_discordant_audit(self):
        self.assertFalse(_optimizer_diagnostic_is_resolved({
            "fit_status": "INTERIOR", "optimizer_status": "OPTIMIZER_DISCORDANT",
            "optimizer_audit": {},
        }))
        self.assertFalse(_optimizer_diagnostic_is_resolved({
            "fit_status": "BOUNDARY", "optimizer_status": "OPTIMIZER_CONCORDANT",
            "optimizer_audit": {},
        }))

    def test_rank_uncertainty_reports_discrete_binomial_rank_diagnostic(self):
        result = _rank_uncertainty(1000, 0.025)
        self.assertEqual(result["bootstrap_replicates"], 1000)
        self.assertEqual(result["quantile_probability"], 0.025)
        self.assertGreater(result["binomial_rank_sd"], 0)
        lower, upper = result["approximate_95_percent_order_statistic_rank_bounds_1based"]
        self.assertGreaterEqual(lower, 1)
        self.assertGreaterEqual(upper, lower)
        self.assertEqual(result["interpretation"], "DISCRETE_BINOMIAL_ORDER_STATISTIC_RANK_DIAGNOSTIC_NOT_COVERAGE")

    def test_small_f5_bank_retains_full_optimizer_audit_and_within_between_intervals(self):
        with tempfile.TemporaryDirectory() as tmp:
            result = run_f5_bank(
                self.spec, bank="calibration", k=1, c0_b=100, c5_b=100,
                output_path=Path(tmp) / "bank.jsonl",
            )
            self.assertEqual(result["datasets_completed"], 1)
            self.assertEqual(len(result["metrics_within_and_raw_between_only"]), 4)
            record = result["records"][0]
            fit = record["fit_diagnostics"]
            self.assertIn(fit["fit_status"], {"INTERIOR", "BOUNDARY", "ABSTAINED"})
            audit = fit["optimizer_audit"]
            self.assertIsInstance(audit, dict)
            self.assertEqual(len(audit["starts"]), 3)
            self.assertEqual(record["comparison"]["candidates"][0]["comparison"]["mcse_interval"], None)
            self.assertIsNotNone(record["comparison"]["candidates"][0]["comparison"]["within_interval"])
            self.assertIsNotNone(record["comparison"]["candidates"][0]["comparison"]["between_interval"])
            self.assertTrue((Path(tmp) / "bank.jsonl").is_file())

    def test_b3_reuses_calibration_dataset_and_compares_independent_bootstrap_streams(self):
        calibration = run_f5_bank(
            self.spec, bank="calibration", k=2, c0_b=100, c5_b=100,
        )
        with tempfile.TemporaryDirectory() as tmp:
            sensitivity = run_f5_endpoint_sensitivity(
                self.spec, calibration_records=calibration["records"],
                n_selected=1, b1000=100, b4000=120,
                output_path=Path(tmp) / "b3.jsonl",
            )
            self.assertEqual(sensitivity["selected_datasets"], 1)
            record = sensitivity["records"][0]
            self.assertEqual(record["rows_sha256"], next(
                row["rows_sha256"] for row in calibration["records"]
                if row["dataset_id"] == record["dataset_id"]
            ))
            self.assertNotEqual(
                record["B1000"]["bootstrap_seed"],
                record["B4000"]["bootstrap_seed"],
            )
            self.assertEqual(record["B1000"]["bootstrap_replicates"], 100)
            self.assertEqual(record["B4000"]["bootstrap_replicates"], 120)
            self.assertIn("lower_rank_uncertainty", record["B1000"]["within_endpoint_diagnostics"])
            self.assertEqual(sensitivity["coverage_adjudication"], "NOT_USED_B3_IS_DIAGNOSTIC_ONLY")
            self.assertTrue((Path(tmp) / "b3.jsonl").is_file())

    def test_runner_rejects_scope_before_any_bank_work(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaisesRegex(RuntimeError, "AUTHORIZATION_SCOPE_MISMATCH"):
                run_f5_development_calibration(
                    Path(tmp), root=Path.cwd(), code_commit="0" * 40,
                    authorization={
                        "validation_status": "PASS",
                        "authorization_id": "TEST-F5-AUTH-001",
                        "authorization_sha256": "a" * 64,
                        "approved_code_commit": "0" * 40,
                        "scope": "WRONG",
                        "f5_b2_b3_authorized": False,
                        "f1_a2_a3_authorized": False,
                        "tier_b_authorized": False,
                        "comparative_holdout_authorized": False,
                        "c10_scientific_execution_authorized": False,
                    },
                )


if __name__ == "__main__":
    unittest.main()
