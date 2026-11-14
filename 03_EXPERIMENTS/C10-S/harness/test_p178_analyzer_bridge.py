"""Deterministic one-dataset bridge: P178 DGP sample -> TGCV Analyzer.

This is a software integration/equivalence check, not a Monte Carlo run.
"""
from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest

import numpy as np
from scipy.stats import t as student_t

HERE = Path(__file__).resolve().parent
CALIBRATION = HERE.parent / "calibration"
sys.path.insert(0, str(CALIBRATION))
import p178_focal_monte_carlo as p178  # noqa: E402

from focal_harness import (  # noqa: E402
    AnalysisContract, Analyzer, EvidenceCandidate, Sealer,
)


class P178AnalyzerBridgeTests(unittest.TestCase):
    def test_analyzer_matches_independent_welch_on_p178_sample(self):
        # Match one finite-sample P178 cell exactly: N=700, pi0=.5, K=10,
        # positive focal scenario, balanced 350/350 allocation.
        seed = 20261495  # P178 reference seed rule, K=10, pi0=.5, positive cell.
        rng = np.random.default_rng(seed)
        q0 = p178.draw_arm(rng, 1, 350, 0.5, 10, 1.0, -1.0, p178.LAMBDA0)[0]
        q1 = p178.draw_arm(rng, 1, 350, 0.5, 10, 1.0, -1.0, p178.LAMBDA1)[0]

        rows = []
        for i, value in enumerate(q0):
            rows.append({
                "unit_id": f"P178-CTRL-{i + 1:04d}",
                "assignment_z": 0,
                "q_b1_observed": float(value),
                "observation_status": "OBSERVED",
            })
        for i, value in enumerate(q1):
            rows.append({
                "unit_id": f"P178-TREAT-{i + 1:04d}",
                "assignment_z": 1,
                "q_b1_observed": float(value),
                "observation_status": "OBSERVED",
            })

        evidence = Sealer().seal(EvidenceCandidate("p178-bridge-positive-n700", tuple(rows)))
        contract = AnalysisContract(
            estimand_id="THETA_A_Q_B1",
            estimand_version="001",
            randomized_assignment=True,
            direct_path_status="ABSENT",
            common_regime=True,
            positivity=True,
            version_consistency=True,
            measurement_ideal=True,
            interference_absent=True,
        )
        result = Analyzer().analyze(evidence, contract)

        # Independent reference calculation using NumPy sample variances and SciPy t.
        mean0, mean1 = float(np.mean(q0)), float(np.mean(q1))
        var0, var1 = float(np.var(q0, ddof=1)), float(np.var(q1, ddof=1))
        estimate = mean1 - mean0
        v0, v1 = var0 / 350, var1 / 350
        se = float(np.sqrt(v0 + v1))
        df = (v0 + v1) ** 2 / (v0**2 / 349 + v1**2 / 349)
        critical = float(student_t.ppf(0.975, df))
        expected_interval = (estimate - critical * se, estimate + critical * se)

        self.assertEqual(result.package_identification, "IDENTIFIED")
        self.assertEqual(result.focal_identification, "IDENTIFIED")
        self.assertAlmostEqual(result.package_itt_estimate, estimate, places=14)
        self.assertAlmostEqual(result.package_itt_standard_error, se, places=14)
        self.assertAlmostEqual(result.package_itt_interval_95[0], expected_interval[0], places=12)
        self.assertAlmostEqual(result.package_itt_interval_95[1], expected_interval[1], places=12)
        self.assertAlmostEqual(result.focal_estimate, estimate, places=14)


if __name__ == "__main__":
    unittest.main()
