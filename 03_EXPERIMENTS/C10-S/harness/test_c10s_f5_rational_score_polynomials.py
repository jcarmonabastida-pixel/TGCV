"""Deterministic algebra tests for c10s_f5_rational_score_polynomials."""
from fractions import Fraction
import unittest

from c10s_f5_rational_score_polynomials import beta_binomial_score_numerators


def _evaluate(poly, mu, kappa):
    return sum(
        Fraction(coef) * mu**i * kappa**j
        for (i, j), coef in poly.items()
    )


def _direct_scores(r, hist, mu, kappa):
    score_mu = Fraction(0)
    score_kappa = Fraction(0)
    for x, multiplicity in hist.items():
        for j in range(x):
            score_mu += multiplicity * kappa / (mu * kappa + j)
            score_kappa += multiplicity * mu / (mu * kappa + j)
        for j in range(r - x):
            score_mu -= multiplicity * kappa / ((1 - mu) * kappa + j)
            score_kappa += multiplicity * (1 - mu) / ((1 - mu) * kappa + j)
        for j in range(r):
            score_kappa -= multiplicity / (kappa + j)
    return score_mu, score_kappa


def _denominators(r, mu, kappa):
    a = [mu * kappa + j for j in range(r)]
    b = [(1 - mu) * kappa + j for j in range(r)]
    c = [kappa + j for j in range(r)]
    d_mu = 1
    d_kappa = 1
    for value in a + b:
        d_mu *= value
        d_kappa *= value
    for value in c:
        d_kappa *= value
    return d_mu, d_kappa


class RationalScorePolynomialTests(unittest.TestCase):
    def test_exact_score_identity_small_fixture(self):
        r = 5
        hist = {0: 2, 1: 3, 3: 4, 5: 1}
        n_mu, n_kappa = beta_binomial_score_numerators(r, hist)
        for mu, kappa in (
            (Fraction(1, 3), Fraction(7, 4)),
            (Fraction(2, 5), Fraction(11, 3)),
            (Fraction(7, 8), Fraction(2, 7)),
        ):
            score_mu, score_kappa = _direct_scores(r, hist, mu, kappa)
            d_mu, d_kappa = _denominators(r, mu, kappa)
            self.assertEqual(_evaluate(n_mu, mu, kappa), score_mu * d_mu)
            self.assertEqual(_evaluate(n_kappa, mu, kappa), score_kappa * d_kappa)

    def test_m30_r20_bidegrees_and_sparse_size(self):
        hist = {x: 1 for x in range(21)}
        for x, extra in {0: 1, 5: 2, 10: 3, 15: 3}.items():
            hist[x] += extra
        self.assertEqual(sum(hist.values()), 30)
        n_mu, n_kappa = beta_binomial_score_numerators(20, hist)
        self.assertEqual(
            (max(i for i, _ in n_mu), max(j for _, j in n_mu)), (39, 40)
        )
        self.assertEqual(
            (max(i for i, _ in n_kappa), max(j for _, j in n_kappa)), (40, 58)
        )
        self.assertEqual(len(n_mu), 629)
        self.assertEqual(len(n_kappa), 1368)

    def test_histogram_validation(self):
        with self.assertRaisesRegex(ValueError, "COUNT_OUTSIDE_0_TO_R"):
            beta_binomial_score_numerators(5, {6: 1})
        with self.assertRaisesRegex(ValueError, "MULTIPLICITY_MUST_BE_NONNEGATIVE_INTEGER"):
            beta_binomial_score_numerators(5, {2: -1})
        with self.assertRaisesRegex(ValueError, "POSITIVE_TOTAL_MULTIPLICITY_REQUIRED"):
            beta_binomial_score_numerators(5, {2: 0})

    def test_zero_count_cells_are_ignored(self):
        a, b = beta_binomial_score_numerators(5, {0: 2, 1: 1})
        c, d = beta_binomial_score_numerators(5, {0: 2, 1: 1, 5: 0})
        self.assertEqual(a, c)
        self.assertEqual(b, d)


if __name__ == "__main__":
    unittest.main()
