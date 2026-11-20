"""Deterministic algebra tests for c10s_f5_rational_score_polynomials."""
from fractions import Fraction
import unittest

from c10s_f5_rational_score_polynomials import (
    beta_binomial_score_numerators,
    compactify_concentration,
    bernstein_coefficients_on_box,
    bernstein_sign_excludes_zero,
    bernstein_subdivide,
    bernstein_exclusion_subdivision,
)


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


    def test_exact_score_identity_on_m30_r20_fixture(self):
        hist = {x: 1 for x in range(21)}
        for x, extra in {0: 1, 5: 2, 10: 3, 15: 3}.items():
            hist[x] += extra
        n_mu, n_kappa = beta_binomial_score_numerators(20, hist)
        for mu, kappa in (
            (Fraction(1, 3), Fraction(7, 4)),
            (Fraction(2, 5), Fraction(11, 3)),
        ):
            score_mu, score_kappa = _direct_scores(20, hist, mu, kappa)
            d_mu, d_kappa = _denominators(20, mu, kappa)
            self.assertEqual(_evaluate(n_mu, mu, kappa), score_mu * d_mu)
            self.assertEqual(_evaluate(n_kappa, mu, kappa), score_kappa * d_kappa)

    def test_exact_positive_concentration_compactification(self):
        poly = {(0, 0): 2, (1, 1): -3, (2, 3): 5, (0, 4): -1}
        transformed = compactify_concentration(poly)
        degree = max(j for _, j in poly)
        for mu, t in (
            (Fraction(1, 3), Fraction(1, 4)),
            (Fraction(2, 5), Fraction(3, 7)),
            (Fraction(7, 8), Fraction(9, 10)),
        ):
            kappa = t / (1 - t)
            lhs = _evaluate(transformed, mu, t)
            rhs = (1 - t) ** degree * _evaluate(poly, mu, kappa)
            self.assertEqual(lhs, rhs)

    def test_compactification_preserves_interior_zero(self):
        poly = {(0, 0): -1, (0, 1): 1}
        transformed = compactify_concentration(poly)
        self.assertEqual(_evaluate(transformed, Fraction(1, 2), Fraction(1, 2)), 0)


    def test_bernstein_coefficients_enclose_positive_polynomial(self):
        # p(mu,t)=1+mu+t is bounded by [1,3] on the unit square.
        coefficients = bernstein_coefficients_on_box(
            {(0, 0): 1, (1, 0): 1, (0, 1): 1}
        )
        self.assertEqual(coefficients, [
            [Fraction(1), Fraction(2)],
            [Fraction(2), Fraction(3)],
        ])
        self.assertTrue(bernstein_sign_excludes_zero(coefficients))

    def test_bernstein_exact_affine_box_substitution(self):
        # p(mu,t)=mu-2t is strictly positive on [3/4,1] x [0,1/4].
        coefficients = bernstein_coefficients_on_box(
            {(1, 0): 1, (0, 1): -2},
            mu_bounds=(Fraction(3, 4), Fraction(1)),
            t_bounds=(Fraction(0), Fraction(1, 4)),
        )
        self.assertEqual(coefficients, [
            [Fraction(3, 4), Fraction(1, 4)],
            [Fraction(1), Fraction(1, 2)],
        ])
        self.assertTrue(bernstein_sign_excludes_zero(coefficients))

    def test_bernstein_mixed_sign_does_not_claim_exclusion(self):
        coefficients = bernstein_coefficients_on_box({(1, 0): 1, (0, 0): -1})
        self.assertFalse(bernstein_sign_excludes_zero(coefficients))

    def test_bernstein_rejects_degenerate_box(self):
        with self.assertRaisesRegex(ValueError, "INVALID_MU_BOUNDS"):
            bernstein_coefficients_on_box({(0, 0): 1}, mu_bounds=(1, 1))

    def test_bernstein_rejects_binary_float_bounds(self):
        with self.assertRaisesRegex(ValueError, "INVALID_MU_BOUNDS"):
            bernstein_coefficients_on_box({(0, 0): 1}, mu_bounds=(0.1, 1))
        with self.assertRaisesRegex(ValueError, "INVALID_T_BOUNDS"):
            bernstein_coefficients_on_box({(0, 0): 1}, t_bounds=(0, 0.9))

    def test_bernstein_rejects_binary_float_coefficients(self):
        with self.assertRaisesRegex(ValueError, "EXACT_RATIONAL_REQUIRED"):
            bernstein_sign_excludes_zero([[0.5, 1]])
        with self.assertRaisesRegex(ValueError, "EXACT_RATIONAL_REQUIRED"):
            bernstein_subdivide([[0.5, 1]], "t")

    def test_bernstein_controller_rejects_binary_float_bounds(self):
        with self.assertRaisesRegex(ValueError, "INVALID_INITIAL_BOX"):
            bernstein_exclusion_subdivision(
                {(0, 0): 1}, {(0, 0): 1}, mu_bounds=(0.1, 1)
            )

    def test_empty_polynomial_still_validates_box(self):
        with self.assertRaisesRegex(ValueError, "INVALID_MU_BOUNDS"):
            bernstein_coefficients_on_box({}, mu_bounds=(1, 1))

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


    def test_bernstein_subdivision_mu_is_exact(self):
        coefficients = bernstein_coefficients_on_box(
            {(0, 0): 0, (1, 0): 1}
        )
        left, right = bernstein_subdivide(coefficients, "mu")
        self.assertEqual(left, [[Fraction(0)], [Fraction(1, 2)]])
        self.assertEqual(right, [[Fraction(1, 2)], [Fraction(1)]])

    def test_bernstein_subdivision_t_is_exact(self):
        coefficients = bernstein_coefficients_on_box(
            {(0, 0): 0, (0, 1): 1}
        )
        left, right = bernstein_subdivide(coefficients, "t")
        self.assertEqual(left, [[Fraction(0), Fraction(1, 2)]])
        self.assertEqual(right, [[Fraction(1, 2), Fraction(1)]])

    def test_bernstein_subdivision_bivariate_tensor_product(self):
        coefficients = bernstein_coefficients_on_box(
            {(0, 0): 0, (1, 0): 1, (0, 1): 1, (1, 1): 1}
        )
        left, right = bernstein_subdivide(coefficients, "mu")
        self.assertEqual(len(left), len(coefficients))
        self.assertEqual(len(right), len(coefficients))
        self.assertEqual([len(row) for row in left], [2, 2])
        self.assertEqual([len(row) for row in right], [2, 2])
        # The two pieces agree exactly on their shared subdivision edge.
        self.assertEqual(left[-1], right[0])

    def test_bernstein_subdivision_rejects_invalid_inputs(self):
        with self.assertRaisesRegex(ValueError, "AXIS_MUST_BE_MU_OR_T"):
            bernstein_subdivide([[Fraction(1)]], "kappa")
        with self.assertRaisesRegex(ValueError, "RECTANGULAR_COEFFICIENT_MATRIX_REQUIRED"):
            bernstein_subdivide([[Fraction(1)], [Fraction(1), Fraction(2)]], "mu")


    def test_bernstein_controller_excludes_root_free_system(self):
        result = bernstein_exclusion_subdivision(
            {(0, 0): 1}, {(0, 0): -2}, max_boxes=10, max_depth=4
        )
        self.assertEqual(result["status"], "ALL_BOXES_EXCLUDED")
        self.assertEqual(result["processed_boxes"], 1)
        self.assertEqual(result["excluded_boxes"], 1)
        self.assertEqual(result["unresolved_boxes"], [])

    def test_bernstein_controller_retains_common_root_box(self):
        result = bernstein_exclusion_subdivision(
            {(1, 0): 1, (0, 0): Fraction(-1, 2)},
            {(0, 1): 1, (0, 0): Fraction(-1, 2)},
            max_boxes=100, max_depth=2,
        )
        self.assertEqual(result["status"], "UNRESOLVED_BOXES")
        self.assertGreater(len(result["unresolved_boxes"]), 0)
        self.assertTrue(all(
            item["state"] == "UNRESOLVED_AT_MAX_DEPTH"
            for item in result["unresolved_boxes"]
        ))

    def test_bernstein_controller_fails_closed_at_box_budget(self):
        result = bernstein_exclusion_subdivision(
            {(1, 0): 1, (0, 0): Fraction(-1, 2)},
            {(0, 1): 1, (0, 0): Fraction(-1, 2)},
            max_boxes=1, max_depth=20,
        )
        self.assertEqual(result["status"], "RESOURCE_LIMIT_WITH_REMAINDER")
        self.assertGreater(len(result["unresolved_boxes"]), 0)

    def test_bernstein_controller_rejects_invalid_budgets(self):
        with self.assertRaisesRegex(ValueError, "MAX_BOXES_MUST_BE_POSITIVE_INTEGER"):
            bernstein_exclusion_subdivision({(0, 0): 1}, {(0, 0): 1}, max_boxes=0)
        with self.assertRaisesRegex(ValueError, "MAX_DEPTH_MUST_BE_NONNEGATIVE_INTEGER"):
            bernstein_exclusion_subdivision({(0, 0): 1}, {(0, 0): 1}, max_depth=-1)


    def test_bernstein_controller_retains_even_multiplicity_common_root(self):
        half = Fraction(1, 2)
        square = {
            (2, 0): 1,
            (1, 0): -2 * half,
            (0, 0): half * half,
        }
        square_t = {
            (0, 2): 1,
            (0, 1): -2 * half,
            (0, 0): half * half,
        }
        result = bernstein_exclusion_subdivision(
            square, square_t, max_boxes=100, max_depth=2
        )
        self.assertEqual(result["status"], "UNRESOLVED_BOXES")
        self.assertGreater(len(result["unresolved_boxes"]), 0)

    def test_bernstein_controller_retains_near_coincident_common_roots(self):
        a = Fraction(1, 2)
        b = a + Fraction(1, 2**20)
        c = Fraction(1, 3)
        # P=(mu-a)(mu-b); Q=(t-c). Both common roots are inside the box
        # and closer than the coarse initial subdivision can separate.
        p = {
            (2, 0): 1,
            (1, 0): -(a + b),
            (0, 0): a * b,
        }
        q = {(0, 1): 1, (0, 0): -c}
        result = bernstein_exclusion_subdivision(
            p, q, max_boxes=100, max_depth=2
        )
        self.assertNotEqual(result["status"], "ALL_BOXES_EXCLUDED")
        self.assertGreater(len(result["unresolved_boxes"]), 0)


if __name__ == "__main__":
    unittest.main()
