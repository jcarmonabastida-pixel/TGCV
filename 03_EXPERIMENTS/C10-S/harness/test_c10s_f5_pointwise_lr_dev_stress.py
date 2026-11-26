from __future__ import annotations

import unittest

from run_c10s_f5_pointwise_lr_dev_stress import (
    K_PER_CELL,
    TARGETS,
    build_seed_audit,
    derive_stress_seed,
)


class F5PointwiseLRDevelopmentStressTests(unittest.TestCase):
    def test_seed_derivation_is_stable_and_uint64(self):
        first = derive_stress_seed("F5_beta22_M10_R5", 0)
        second = derive_stress_seed("F5_beta22_M10_R5", 0)
        other = derive_stress_seed("F5_beta22_M10_R5", 1)
        self.assertEqual(first, second)
        self.assertNotEqual(first, other)
        self.assertGreaterEqual(first, 0)
        self.assertLess(first, 2**64)

    def test_predeclared_seed_roster_is_disjoint_from_history(self):
        rows, audit = build_seed_audit()
        self.assertEqual(len(rows), 2 * K_PER_CELL)
        self.assertEqual(audit["status"], "PASS")
        self.assertEqual(audit["new_unique_seed_values"], len(rows))
        self.assertEqual(audit["collision_count"], 0)
        self.assertGreater(audit["historical_unique_seed_values_checked"], 100000)

    def test_targets_are_exact_f5_beta22_functionals(self):
        self.assertEqual(str(TARGETS["W"]), "1/5")
        self.assertEqual(str(TARGETS["B"]), "1/20")


if __name__ == "__main__":
    unittest.main()
