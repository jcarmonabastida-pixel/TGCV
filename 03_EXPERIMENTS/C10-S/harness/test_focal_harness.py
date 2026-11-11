"""Software-contract tests for the C10-S focal harness; not scientific runs."""
import unittest

from focal_harness import (
    AnalysisContract, Analyzer, ContractError, Evaluator, Generator,
    Projector, ScenarioConfig, Sealer,
)


def config(name, alpha01=0.0, alpha10=0.0, gamma01=0.0, gamma10=0.0,
           direct="ABSENT", seed=20261111):
    return ScenarioConfig(
        scenario_id=name, scenario_version="fixture-001",
        n_units=700, seed=seed, pi0=0.5, k_slots=10,
        lambda0=0.25, lambda1=0.75,
        p01_base=0.2, p10_base=0.2,
        alpha01=alpha01, alpha10=alpha10,
        gamma01=gamma01, gamma10=gamma10,
        assignment_probability=0.5, direct_path_status=direct,
        measurement_ideal=True, interference_absent=True,
    )


def contract(direct="ABSENT"):
    return AnalysisContract(
        estimand_id="THETA_A_Q_B1", estimand_version="001",
        randomized_assignment=True, direct_path_status=direct,
        common_regime=True, measurement_ideal=True, interference_absent=True,
    )


class FocalHarnessContractTests(unittest.TestCase):
    def run_case(self, cfg, analysis_contract):
        manifest, truth, source = Generator().generate(cfg)
        candidate = Projector().project(source)
        sealed = Sealer().seal(candidate)
        result = Analyzer().analyze(sealed, analysis_contract)
        report = Evaluator().evaluate(truth, result, analysis_contract, tolerance=0.20)
        self.assertEqual(manifest.run_id, result.run_id)
        self.assertEqual(sealed.run_id, result.run_id)
        return truth, source, sealed, result, report

    def test_null_scenario_has_zero_focal_truth_and_is_identified(self):
        truth, source, sealed, result, report = self.run_case(config("null"), contract())
        self.assertAlmostEqual(truth.theta_access_truth, 0.0, places=12)
        self.assertEqual(result.focal_identification, "IDENTIFIED")
        self.assertTrue(report.classification_correct)
        self.assertTrue(all(set(row) == set(Projector.ALLOWED) for row in sealed.rows))

    def test_positive_and_negative_focal_truth_preserve_sign(self):
        positive, *_ = self.run_case(config("positive", 1.0, -1.0, seed=20261112), contract())
        negative, *_ = self.run_case(config("negative", -1.0, 1.0, seed=20261113), contract())
        self.assertGreater(positive.theta_access_truth, 0.0)
        self.assertLess(negative.theta_access_truth, 0.0)

    def test_direct_path_adversary_returns_package_not_focal_effect(self):
        cfg = config("direct-path", 1.0, -1.0, 0.7, -0.4, "PRESENT", 20261114)
        truth, _source, _sealed, result, report = self.run_case(cfg, contract("PRESENT"))
        self.assertTrue(truth.direct_path_truth)
        self.assertEqual(result.package_identification, "IDENTIFIED")
        self.assertEqual(result.focal_identification, "NOT_IDENTIFIED")
        self.assertIsNone(report.focal_abs_error)
        self.assertTrue(report.classification_correct)

    def test_unknown_direct_path_forces_indeterminate_focal_status(self):
        cfg = config("unknown-direct-path", 1.0, -1.0, 0.0, 0.0, "UNKNOWN", 20261115)
        _truth, _source, _sealed, result, report = self.run_case(cfg, contract("UNKNOWN"))
        self.assertEqual(result.focal_identification, "INDETERMINATE")
        self.assertTrue(report.classification_correct)

    def test_truth_fields_are_not_projected(self):
        _manifest, truth, source = Generator().generate(config("firewall"))
        candidate = Projector().project(source)
        self.assertNotIn("seed", candidate.rows[0])
        self.assertNotIn("signature_d1", candidate.rows[0])
        self.assertNotIn("potential_q", candidate.rows[0])
        self.assertEqual(len(truth.potential_q_by_z), len(candidate.rows))

    def test_inconsistent_direct_path_declaration_fails_closed(self):
        with self.assertRaises(ContractError):
            config("bad", gamma01=0.2, direct="ABSENT").validate()


if __name__ == "__main__":
    unittest.main()
