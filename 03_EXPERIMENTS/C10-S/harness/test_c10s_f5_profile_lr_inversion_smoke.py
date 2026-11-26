from __future__ import annotations

from fractions import Fraction
import unittest

from c10s_f5_component_profile_score import f5_component_profile_confidence_set
from c10s_f5_rational_score_polynomials import beta_binomial_global_mle_certificate


class F5ProfileLRInversionSmokeTests(unittest.TestCase):
    def test_single_fixture_full_lr_grid_inversion_smoke(self):
        r = 5
        histogram = {0: 1, 1: 2, 2: 2, 3: 2, 4: 2, 5: 1}
        global_certificate = beta_binomial_global_mle_certificate(
            r, histogram, max_refinements=1, projection_bits=12,
            max_projection_depth=40, max_lift_intervals=100,
            max_lift_depth=20, max_mu_depth=10,
            source_revision="0123456789abcdef0123456789abcdef01234567",
        )
        result = f5_component_profile_confidence_set(
            r, histogram, component="W",
            likelihood_ratio_cutoff=Fraction(384, 100),
            global_certificate=global_certificate,
            scan_grid_points=5, max_bisection_steps=1,
            root_isolation_width=Fraction(1, 2**40),
            max_depth=140, max_intervals=5000,
            log_series_terms=80,
        )
        self.assertIn(
            result["status"],
            {
                "GRID_DETECTED_SINGLE_COMPONENT_BRACKETED",
                "GRID_DETECTED_DISCONNECTED_COMPONENTS_BRACKETED",
                "EMPTY_LR_SET_ON_NUMERICAL_GRID",
            },
        )
        self.assertFalse(result["topology_certified"])
        self.assertGreaterEqual(result["target_evaluations"], 5)


if __name__ == "__main__":
    unittest.main()
