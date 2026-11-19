"""Adversarial tests for the independent exact-rational F1 root isolator."""
from fractions import Fraction
import unittest

from c10s_f1_independent_root_isolator import isolate_real_roots


class IndependentRootIsolatorTests(unittest.TestCase):
    def test_cubic_three_distinct_real_roots(self):
        # (x-1)(x-2)(x-3), ascending coefficients.
        result = isolate_real_roots((-6, 11, -6, 1), lower=-4, upper=4)
        self.assertEqual(result.status, "ROOTS_ISOLATED")
        self.assertEqual(len(result.roots), 3)
        self.assertEqual([r.multiplicity for r in result.roots], [1, 1, 1])
        self.assertTrue(all(r.lower < r.upper for r in result.roots))

    def test_exact_double_root_and_simple_root(self):
        # (x-1)^2 (x-2)
        result = isolate_real_roots((-2, 5, -4, 1), lower=0, upper=3)
        self.assertEqual(result.status, "ROOTS_ISOLATED")
        self.assertEqual([r.multiplicity for r in result.roots], [2, 1])
        self.assertTrue(result.roots[0].lower <= 1 <= result.roots[0].upper)
        self.assertTrue(result.roots[1].lower <= 2 <= result.roots[1].upper)

    def test_triple_root(self):
        # (x-1)^3
        result = isolate_real_roots((-1, 3, -3, 1), lower=0, upper=2)
        self.assertEqual(result.status, "ROOTS_ISOLATED")
        self.assertEqual(len(result.roots), 1)
        self.assertEqual(result.roots[0].multiplicity, 3)

    def test_two_close_distinct_rational_roots(self):
        a = Fraction(1, 1)
        b = Fraction(1000000001, 1000000000)
        # (x-a)(x-b)
        coefficients = (a * b, -(a + b), Fraction(1))
        result = isolate_real_roots(
            coefficients, lower=Fraction(0), upper=Fraction(2),
            max_width=Fraction(1, 10**14),
        )
        self.assertEqual(result.status, "ROOTS_ISOLATED")
        self.assertEqual(len(result.roots), 2)
        self.assertLess(result.roots[0].upper, result.roots[1].lower)

    def test_exact_roots_at_domain_boundaries(self):
        # x(x-1), with zero included as an exact boundary root.
        result = isolate_real_roots((0, -1, 1), lower=0, upper=1)
        self.assertEqual(result.status, "ROOTS_ISOLATED")
        self.assertEqual(len(result.roots), 2)
        self.assertEqual(result.roots[0].lower, 0)
        self.assertEqual(result.roots[0].upper, 0)
        self.assertEqual(result.roots[1].lower, 1)
        self.assertEqual(result.roots[1].upper, 1)

    def test_degree_reduction_and_negative_root_exclusion(self):
        # Effective degree two; roots -1 and 2, retain only [0, 3].
        result = isolate_real_roots((2, -1, -1, 0), lower=0, upper=3)
        self.assertEqual(result.status, "ROOTS_ISOLATED")
        self.assertEqual(len(result.roots), 1)
        self.assertTrue(result.roots[0].lower <= 2 <= result.roots[0].upper)

    def test_float_is_exact_binary_rationalization_not_measurement_interval(self):
        result = isolate_real_roots((-1.0, 1.0), lower=0, upper=2)
        self.assertEqual(result.status, "ROOTS_ISOLATED")
        self.assertEqual(
            result.coefficient_semantics,
            "EXACT_RATIONALIZATION_OF_INPUT_VALUES",
        )

    def test_constant_polynomial(self):
        result = isolate_real_roots((7,))
        self.assertEqual(result.status, "NO_ROOTS_CONSTANT_POLYNOMIAL")
        self.assertEqual(result.roots, ())

    def test_rejects_degree_above_three(self):
        with self.assertRaisesRegex(ValueError, "DEGREE_EXCEEDS_THREE"):
            isolate_real_roots((1, 0, 0, 0, 1))

    def test_rejects_nonfinite_coefficient(self):
        with self.assertRaisesRegex(ValueError, "NONFINITE_FLOAT_INPUT"):
            isolate_real_roots((1.0, float("nan")))


if __name__ == "__main__":
    unittest.main()
