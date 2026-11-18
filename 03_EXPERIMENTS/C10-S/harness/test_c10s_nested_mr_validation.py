from __future__ import annotations

import tempfile
import unittest

import numpy as np
from pathlib import Path

from c10s_nested_mr_fixtures import (
    FIXTURE_GENERATOR_VERSION,
    SEED_SCHEDULE_VERSION,
    deterministic_guard_specs,
    derive_seed,
    generate_deterministic_guard,
    generate_fixture,
    tier_a_specs,
    tier_b_specs,
)
from validate_c10s_nested_mr_execution_authorization import validate_authorization
from run_c10s_nested_mr_validation import (
    _run_deterministic_guards,
    analyze_fixture,
    coverage_summary,
)


class NestedMRFixtureContractTests(unittest.TestCase):
    def test_frozen_tier_a_has_eight_cells_and_exact_k_b(self):
        specs = tier_a_specs()
        self.assertEqual(len(specs), 8)
        self.assertTrue(all(spec.k == 1000 and spec.b == 1000 for spec in specs))
        self.assertEqual({(spec.m, spec.r) for spec in specs}, {(10, 5), (30, 20)})
        self.assertEqual(sum(spec.family == "F1" for spec in specs), 6)
        self.assertEqual(sum(spec.family == "F5" for spec in specs), 2)

    def test_frozen_tier_b_has_twenty_stochastic_cells(self):
        specs = tier_b_specs()
        self.assertEqual(len(specs), 20)
        self.assertTrue(all(spec.k == 500 and spec.b == 500 for spec in specs))
        self.assertEqual(sum(spec.m == 2 for spec in specs), 2)
        self.assertEqual(len(deterministic_guard_specs()), 4)

    def test_seed_schedule_is_stable_and_namespaces_are_separate(self):
        a = derive_seed("fixture_dataset", "F1_balanced_M10_R5", 17)
        b = derive_seed("bootstrap", "F1_balanced_M10_R5", 17)
        self.assertEqual(a, derive_seed("fixture_dataset", "F1_balanced_M10_R5", 17))
        self.assertNotEqual(a, b)
        self.assertEqual(SEED_SCHEDULE_VERSION, "C10S_NESTED_MR_SEED_SCHEDULE_1.0")
        self.assertEqual(FIXTURE_GENERATOR_VERSION, "C10S_NESTED_MR_FIXTURES_1.1")

    def test_gaussian_fixture_has_declared_truth_and_shape(self):
        spec = next(x for x in tier_a_specs() if x.cell_id == "F1_balanced_M10_R5")
        dataset = generate_fixture(spec, 0)
        self.assertEqual(len(dataset.rows), 10)
        self.assertTrue(all(len(row) == 5 for row in dataset.rows))
        self.assertEqual(spec.true_within, 1.0)
        self.assertEqual(spec.true_between, 1.0)

    def test_beta_binomial_oracle_is_analytically_fixed(self):
        spec = next(x for x in tier_a_specs() if x.family == "F5")
        self.assertAlmostEqual(spec.true_within, 0.20)
        self.assertAlmostEqual(spec.true_between, 0.05)
        dataset = generate_fixture(spec, 3)
        self.assertTrue(all(value in (0.0, 1.0) for row in dataset.rows for value in row))

    def test_analyzer_receives_complete_fixture_and_returns_all_bootstrap_draws(self):
        spec = next(x for x in tier_a_specs() if x.cell_id == "F1_balanced_M10_R5")
        dataset = generate_fixture(spec, 4)
        record = analyze_fixture(dataset, bootstrap_replicates=100)
        self.assertEqual(record["bootstrap_replicates"], 100)
        self.assertEqual(record["valid_bootstrap_replicates"], 100)
        self.assertIn("within_ms", record["intervals_95"])
        self.assertIn("between_raw", record["intervals_95"])
        self.assertIsNotNone(record["observed_mcse"])
        world_means = np.mean(np.asarray(dataset.rows), axis=1)
        expected_legacy_mcse = float(np.sqrt(np.var(world_means, ddof=1) / spec.m))
        self.assertAlmostEqual(record["observed_mcse"], expected_legacy_mcse)

    def test_deterministic_degeneracy_guards_are_explicit_and_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            guards = _run_deterministic_guards(Path(tmp), Path.cwd(), "test-commit")
        self.assertEqual(len(guards), 4)
        self.assertTrue(all(item["direct_invariant_pass"] for item in guards))
        by_family = {item["cell"]["family"]: item for item in guards}
        self.assertTrue(by_family["F4"]["analysis"]["bootstrap_degenerate"])
        self.assertEqual(
            by_family["F6"]["analysis"]["projected_mcse_status"],
            "RMSE_DELTA_NONREGULAR",
        )

    def test_coverage_rule_requires_both_tolerance_and_wilson_containment(self):
        passing = coverage_summary(950, 1000)
        failing = coverage_summary(930, 1000)
        self.assertEqual(passing["status"], "PASS_BOUNDED_NUMERICAL_VALIDATION")
        self.assertEqual(failing["status"], "NOT_VALIDATED")
        self.assertLessEqual(passing["wilson_95"][0], 0.95)
        self.assertGreaterEqual(passing["wilson_95"][1], 0.95)


    def test_authorization_validator_fails_closed_without_approved_status(self):
        import json
        with tempfile.TemporaryDirectory() as tmp:
            auth_path = Path(tmp) / "authorization.json"
            auth_path.write_text(json.dumps({"schema": "TGCV-C10S-NESTED-MR-EXECUTION-AUTH-001", "status": "PENDING"}), encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "not APPROVED"):
                validate_authorization(
                    auth_path, Path(tmp), "0" * 40,
                    "research/c10s-nested-mr-auth-test",
                )



if __name__ == "__main__":
    unittest.main()
