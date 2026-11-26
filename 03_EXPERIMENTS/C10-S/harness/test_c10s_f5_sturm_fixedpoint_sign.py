from __future__ import annotations

import random
import unittest
from fractions import Fraction

import c10s_f5_rational_score_polynomials as rational
from c10s_f5_sturm_call_instrumentation import (
    sign_variations_integer_certified_fixedpoint,
)


class CertifiedFixedPointSturmSignTests(unittest.TestCase):
    def test_exact_parity_over_dyadic_grid_and_large_integer_polynomials(self):
        rng = random.Random(20261126)
        polynomials = [
            [-1, 2],  # exact dyadic root at one half
            [1, -7, 11, -5],
            [3, 0, -2, 0, 1],
        ]
        for degree in range(2, 15):
            values = [rng.getrandbits(384) * (-1 if rng.randrange(2) else 1)
                      for _ in range(degree)]
            values.append(rng.getrandbits(384) or 1)
            polynomials.append(values)

        for coefficients in polynomials:
            sequence = rational._uni_sturm_integer_sequence(
                rational._uni_sturm_sequence(coefficients)
            )
            for depth in range(0, 9):
                denominator = 1 << depth
                for numerator in range(denominator + 1):
                    point = Fraction(numerator, denominator)
                    expected = rational._uni_sign_variations_integer(sequence, point)
                    observed = sign_variations_integer_certified_fixedpoint(
                        sequence, point,
                    )
                    self.assertEqual(
                        observed, expected,
                        msg=f"{coefficients=} {point=} {sequence=}",
                    )

    def test_exact_zero_and_endpoint_sign_conventions(self):
        sequence = rational._uni_sturm_integer_sequence(
            rational._uni_sturm_sequence([-1, 2])
        )
        for point in (Fraction(0), Fraction(1, 2), Fraction(1)):
            self.assertEqual(
                sign_variations_integer_certified_fixedpoint(sequence, point),
                rational._uni_sign_variations_integer(sequence, point),
            )

    def test_non_dyadic_point_uses_exact_fallback(self):
        sequence = ((-1, 2), (1,))
        point = Fraction(1, 3)
        self.assertEqual(
            sign_variations_integer_certified_fixedpoint(sequence, point),
            rational._uni_sign_variations_integer(sequence, point),
        )


    def test_integer_prs_sequence_has_exact_rational_sturm_sign_parity(self):
        from c10s_f5_sturm_call_instrumentation import primitive_integer_sturm_sequence

        rng = random.Random(20261127)
        polynomials = [
            [-1, 2],
            [1, -7, 11, -5],
            [3, 0, -2, 0, 1],
            [-5, 0, 0, 1],
            [7, -3, 0, 0, -2, 1],
        ]
        for degree in range(2, 18):
            coefficients = [
                rng.getrandbits(256) * (-1 if rng.randrange(2) else 1)
                for _ in range(degree)
            ]
            coefficients.append(
                (rng.getrandbits(256) or 1) * (-1 if rng.randrange(2) else 1)
            )
            polynomials.append(coefficients)

        for coefficients in polynomials:
            reference = rational._uni_sturm_integer_sequence(
                rational._uni_sturm_sequence(coefficients)
            )
            candidate = primitive_integer_sturm_sequence(coefficients)
            self.assertEqual(len(candidate), len(reference))
            for depth in range(0, 8):
                denominator = 1 << depth
                for numerator in range(denominator + 1):
                    point = Fraction(numerator, denominator)
                    self.assertEqual(
                        rational._uni_sign_variations_integer(reference, point),
                        rational._uni_sign_variations_integer(candidate, point),
                        msg=f"{coefficients=} {point=}",
                    )


if __name__ == "__main__":
    unittest.main()


    def test_integer_prs_sequence_has_exact_rational_sturm_sign_parity(self):
        from c10s_f5_sturm_call_instrumentation import primitive_integer_sturm_sequence

        rng = random.Random(20261127)
        polynomials = [
            [-1, 2],
            [1, -7, 11, -5],
            [3, 0, -2, 0, 1],
            [-5, 0, 0, 1],
            [7, -3, 0, 0, -2, 1],
        ]
        for degree in range(2, 18):
            coefficients = [
                rng.getrandbits(256) * (-1 if rng.randrange(2) else 1)
                for _ in range(degree)
            ]
            coefficients.append(
                (rng.getrandbits(256) or 1) * (-1 if rng.randrange(2) else 1)
            )
            polynomials.append(coefficients)

        for coefficients in polynomials:
            reference = rational._uni_sturm_integer_sequence(
                rational._uni_sturm_sequence(coefficients)
            )
            candidate = primitive_integer_sturm_sequence(coefficients)
            self.assertEqual(len(candidate), len(reference))
            for depth in range(0, 8):
                denominator = 1 << depth
                for numerator in range(denominator + 1):
                    point = Fraction(numerator, denominator)
                    self.assertEqual(
                        rational._uni_sign_variations_integer(reference, point),
                        rational._uni_sign_variations_integer(candidate, point),
                        msg=f"{coefficients=} {point=}",
                    )
