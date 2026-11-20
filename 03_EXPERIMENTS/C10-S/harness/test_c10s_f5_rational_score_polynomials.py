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
    krawczyk_certify_unique_root,
    bernstein_krawczyk_root_classification,
    beta_binomial_boundary_likelihoods,
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

    def test_krawczyk_certifies_simple_common_root_exactly(self):
        # P=2*mu-1, Q=2*t-1; the unique root is exactly (1/2,1/2).
        result = krawczyk_certify_unique_root(
            {(1, 0): 2, (0, 0): -1},
            {(0, 1): 2, (0, 0): -1},
            mu_bounds=(Fraction(1, 4), Fraction(3, 4)),
            t_bounds=(Fraction(1, 4), Fraction(3, 4)),
        )
        self.assertEqual(result["status"], "CERTIFIED_UNIQUE_ROOT")
        self.assertEqual(result["contraction_bound"], 0)
        self.assertEqual(result["krawczyk_box"], (
            (Fraction(1, 2), Fraction(1, 2)),
            (Fraction(1, 2), Fraction(1, 2)),
        ))

    def test_krawczyk_abstains_on_singular_multiple_root(self):
        # P=(2*mu-1)^2, Q=2*t-1; midpoint Jacobian is singular.
        result = krawczyk_certify_unique_root(
            {(2, 0): 4, (1, 0): -4, (0, 0): 1},
            {(0, 1): 2, (0, 0): -1},
            mu_bounds=(Fraction(1, 4), Fraction(3, 4)),
            t_bounds=(Fraction(1, 4), Fraction(3, 4)),
        )
        self.assertEqual(result["status"], "UNRESOLVED_SINGULAR_MIDPOINT_JACOBIAN")

    def test_krawczyk_rejects_float_bounds(self):
        with self.assertRaisesRegex(ValueError, "EXACT_RATIONAL_BOUNDS_REQUIRED"):
            krawczyk_certify_unique_root(
                {(1, 0): 1}, {(0, 1): 1},
                mu_bounds=(0.1, 1), t_bounds=(0, 1),
            )

    def test_krawczyk_rejects_degenerate_box(self):
        with self.assertRaisesRegex(ValueError, "INVALID_CERTIFICATION_BOX"):
            krawczyk_certify_unique_root(
                {(1, 0): 1}, {(0, 1): 1},
                mu_bounds=(1, 1), t_bounds=(0, 1),
            )

    def test_integrated_bernstein_krawczyk_certifies_simple_root(self):
        # Root (3/8,3/8) is the midpoint of the rational test box.
        result = bernstein_krawczyk_root_classification(
            {(1, 0): 8, (0, 0): -3},
            {(0, 1): 8, (0, 0): -3},
            mu_bounds=(Fraction(1, 4), Fraction(1, 2)),
            t_bounds=(Fraction(1, 4), Fraction(1, 2)),
            max_boxes=1, max_depth=0,
        )
        self.assertEqual(
            result["status"], "ALL_SURVIVING_BOXES_CERTIFIED_SIMPLE_ROOTS"
        )
        self.assertEqual(len(result["certified_root_boxes"]), 1)
        self.assertEqual(result["unresolved_boxes"], [])

    def test_integrated_bernstein_krawczyk_preserves_multiple_root_as_unresolved(self):
        result = bernstein_krawczyk_root_classification(
            {(2, 0): 4, (1, 0): -4, (0, 0): 1},
            {(0, 1): 2, (0, 0): -1},
            mu_bounds=(Fraction(1, 4), Fraction(3, 4)),
            t_bounds=(Fraction(1, 4), Fraction(3, 4)),
            max_boxes=1, max_depth=0,
        )
        self.assertEqual(result["status"], "PARTIAL_CERTIFICATION_WITH_REMAINDER")
        self.assertEqual(result["certified_root_boxes"], [])
        self.assertEqual(len(result["unresolved_boxes"]), 1)

    def test_integrated_controller_refines_unresolved_boxes_deterministically(self):
        # A repeated root must remain unresolved after adaptive subdivision.
        square_mu = {(2, 0): 4, (1, 0): -4, (0, 0): 1}
        linear_t = {(0, 1): 2, (0, 0): -1}
        first = bernstein_krawczyk_root_classification(
            square_mu, linear_t,
            mu_bounds=(Fraction(1, 4), Fraction(3, 4)),
            t_bounds=(Fraction(1, 4), Fraction(3, 4)),
            max_boxes=9, max_depth=2,
        )
        second = bernstein_krawczyk_root_classification(
            square_mu, linear_t,
            mu_bounds=(Fraction(1, 4), Fraction(3, 4)),
            t_bounds=(Fraction(1, 4), Fraction(3, 4)),
            max_boxes=9, max_depth=2,
        )
        self.assertEqual(first, second)
        self.assertGreater(first["subdivisions"], 0)
        self.assertEqual(first["certified_root_boxes"], [])
        self.assertTrue(first["unresolved_boxes"])

    def test_integrated_controller_marks_unprocessed_budget_remainder(self):
        result = bernstein_krawczyk_root_classification(
            {(1, 0): 2, (0, 0): -1},
            {(0, 1): 2, (0, 0): -1},
            max_boxes=1, max_depth=10,
        )
        self.assertEqual(result["status"], "RESOURCE_LIMIT_WITH_REMAINDER")
        self.assertTrue(any(
            box["state"] == "NOT_PROCESSED_RESOURCE_LIMIT"
            for box in result["unresolved_boxes"]
        ))

    def test_boundary_profiles_are_exact_for_endpoint_histogram(self):
        result = beta_binomial_boundary_likelihoods(2, {0: 1, 2: 1})
        self.assertEqual(result["kappa_infinity"]["profile_mean"], Fraction(1, 2))
        self.assertEqual(result["kappa_infinity"]["likelihood"], Fraction(1, 16))
        self.assertEqual(result["kappa_zero"]["profile_mean"], Fraction(1, 2))
        self.assertEqual(result["kappa_zero"]["likelihood"], Fraction(1, 4))
        self.assertEqual(result["mu_zero"]["likelihood"], 0)
        self.assertEqual(result["mu_one"]["likelihood"], 0)
        self.assertEqual(
            result["corner_path_limits"], "NOT_CLASSIFIED_BY_ONE_EDGE_PROFILES"
        )

    def test_zero_concentration_limit_is_zero_with_interior_counts(self):
        result = beta_binomial_boundary_likelihoods(2, {1: 1})
        self.assertEqual(result["kappa_zero"]["likelihood"], 0)
        self.assertEqual(result["kappa_zero"]["status"], "ZERO_LIMIT_LIKELIHOOD")
        self.assertIsNone(result["kappa_zero"]["profile_mean"])
        self.assertEqual(result["kappa_infinity"]["likelihood"], Fraction(1, 2))

    def test_degenerate_mean_boundary_profiles(self):
        all_zero = beta_binomial_boundary_likelihoods(3, {0: 2})
        self.assertEqual(all_zero["mu_zero"]["likelihood"], 1)
        self.assertEqual(all_zero["mu_one"]["likelihood"], 0)
        self.assertEqual(all_zero["kappa_infinity"]["likelihood"], 1)
        all_r = beta_binomial_boundary_likelihoods(3, {3: 2})
        self.assertEqual(all_r["mu_zero"]["likelihood"], 0)
        self.assertEqual(all_r["mu_one"]["likelihood"], 1)
        self.assertEqual(all_r["kappa_zero"]["likelihood"], 1)

    def test_boundary_profile_rejects_invalid_histogram(self):
        with self.assertRaisesRegex(ValueError, "COUNT_OUTSIDE_0_TO_R"):
            beta_binomial_boundary_likelihoods(2, {3: 1})
        with self.assertRaisesRegex(ValueError, "MULTIPLICITY_MUST_BE_NONNEGATIVE_INTEGER"):
            beta_binomial_boundary_likelihoods(2, {1: -1})

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
        # Integer scaling preserves the common zero at (1/2, 1/2).
        result = bernstein_exclusion_subdivision(
            {(1, 0): 2, (0, 0): -1},
            {(0, 1): 2, (0, 0): -1},
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
            {(1, 0): 2, (0, 0): -1},
            {(0, 1): 2, (0, 0): -1},
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
        # (2*mu-1)^2 and (2*t-1)^2: integer-scaled double-root fixture.
        square = {(2, 0): 4, (1, 0): -4, (0, 0): 1}
        square_t = {(0, 2): 4, (0, 1): -4, (0, 0): 1}
        result = bernstein_exclusion_subdivision(
            square, square_t, max_boxes=100, max_depth=2
        )
        self.assertEqual(result["status"], "UNRESOLVED_BOXES")
        self.assertGreater(len(result["unresolved_boxes"]), 0)

    def test_bernstein_controller_retains_near_coincident_common_roots(self):
        denominator = 2**20
        a_num = denominator // 2
        b_num = a_num + 1
        # P=(D*mu-a_num)(D*mu-b_num), Q=3*t-1.
        # Integer scaling preserves roots separated by exactly 2^-20.
        p = {
            (2, 0): denominator**2,
            (1, 0): -denominator * (a_num + b_num),
            (0, 0): a_num * b_num,
        }
        q = {(0, 1): 3, (0, 0): -1}
        result = bernstein_exclusion_subdivision(
            p, q, max_boxes=100, max_depth=2
        )
        self.assertNotEqual(result["status"], "ALL_BOXES_EXCLUDED")
        self.assertGreater(len(result["unresolved_boxes"]), 0)


if __name__ == "__main__":
    unittest.main()
