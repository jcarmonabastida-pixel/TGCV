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
    compactified_boundary_common_factors,
    compactified_boundary_common_roots,
    compactified_boundary_corner_census,
    beta_binomial_joint_corner_likelihood_limits,
    compactified_axis_common_components,
    compactified_projection_resultant_mu,
    compactified_projection_root_isolation_mu,
    compactified_concentration_resultant_t,
    compactified_concentration_root_isolation_t,
    conditional_mean_tube_and_concentration_exclusion,
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

    def test_compactified_edge_common_factor_preserves_multiplicity(self):
        # On mu=0 and mu=1: P=(2t-1)^2, Q=(2t-1)^3.
        p = {(0, 2): 4, (0, 1): -4, (0, 0): 1}
        q = {(0, 3): 8, (0, 2): -12, (0, 1): 6, (0, 0): -1}
        result = compactified_boundary_common_factors(p, q)
        self.assertEqual(result["status"], "BOUNDARY_COMMON_FACTORS_CLASSIFIED")
        for edge in ("mu_zero", "mu_one"):
            self.assertEqual(
                result["edges"][edge]["status"], "FINITE_COMMON_EDGE_ROOTS"
            )
            self.assertEqual(
                result["edges"][edge]["squarefree_factors"],
                [{
                    "multiplicity": 2,
                    "coefficients": (
                        Fraction(-1, 2), Fraction(1)
                    ),
                }],
            )
        self.assertEqual(
            result["edges"]["t_zero"]["status"], "NO_COMMON_EDGE_ROOT"
        )
        self.assertEqual(
            result["edges"]["t_one"]["status"], "NO_COMMON_EDGE_ROOT"
        )
        self.assertEqual(result["root_isolation"], "NOT_YET_PERFORMED")

    def test_sturm_isolates_exact_rational_edge_root_and_multiplicity(self):
        p = {(0, 2): 4, (0, 1): -4, (0, 0): 1}
        q = {(0, 3): 8, (0, 2): -12, (0, 1): 6, (0, 0): -1}
        result = compactified_boundary_common_roots(p, q)
        self.assertEqual(result["status"], "BOUNDARY_ROOT_ISOLATION_COMPLETE")
        for edge in ("mu_zero", "mu_one"):
            factor = result["edges"][edge]["isolated_factors"][0]
            self.assertEqual(factor["multiplicity"], 2)
            self.assertEqual(factor["exact_roots"], (Fraction(1, 2),))
            self.assertEqual(factor["isolating_intervals"], [])

    def test_sturm_isolates_irrational_edge_root(self):
        # The common factor 2*t^2-1 has one root in [0,1], sqrt(1/2).
        p = {(0, 2): 2, (0, 0): -1}
        q = {(0, 4): 4, (0, 2): -4, (0, 0): 1}
        result = compactified_boundary_common_roots(
            p, q, width=Fraction(1, 32)
        )
        self.assertEqual(result["status"], "BOUNDARY_ROOT_ISOLATION_COMPLETE")
        factor = result["edges"]["mu_zero"]["isolated_factors"][0]
        self.assertEqual(factor["multiplicity"], 1)
        self.assertEqual(len(factor["isolating_intervals"]), 1)
        left, right = factor["isolating_intervals"][0]["interval"]
        self.assertGreaterEqual(left, 0)
        self.assertLessEqual(right, 1)
        self.assertLess(2 * left * left, 1)
        self.assertGreater(2 * right * right, 1)
        self.assertLess(right - left, Fraction(1, 32))
        self.assertEqual(factor["isolating_intervals"][0]["root_count"], 1)

    def test_sturm_boundary_isolation_abstains_on_resource_limit(self):
        p = {(0, 2): 2, (0, 0): -1}
        q = {(0, 4): 4, (0, 2): -4, (0, 0): 1}
        result = compactified_boundary_common_roots(
            p, q, width=Fraction(1, 2**30),
            max_depth=1, max_intervals=100,
        )
        self.assertEqual(result["status"], "PARTIAL_BOUNDARY_ROOT_ISOLATION")
        factor = result["edges"]["mu_zero"]["isolated_factors"][0]
        self.assertEqual(factor["status"], "PARTIAL_ISOLATION")
        self.assertTrue(factor["unresolved_intervals"])

    def test_compactified_edge_common_component_abstains(self):
        # Both score polynomials vanish identically on mu=0.
        result = compactified_boundary_common_factors(
            {(1, 0): 1}, {(1, 0): 2}
        )
        self.assertEqual(
            result["edges"]["mu_zero"]["status"],
            "COMMON_EDGE_COMPONENT_UNRESOLVED",
        )
        self.assertEqual(
            result["status"], "BOUNDARY_COMMON_COMPONENTS_UNRESOLVED"
        )

    def test_compactified_edge_factor_validation(self):
        with self.assertRaisesRegex(ValueError, "INTEGER_SPARSE_POLYNOMIALS_REQUIRED"):
            compactified_boundary_common_factors(
                {(1, 0): Fraction(1, 2)}, {(0, 1): 1}
            )
        with self.assertRaisesRegex(ValueError, "INTEGER_SPARSE_POLYNOMIALS_REQUIRED"):
            compactified_boundary_common_factors(
                {(1,): 1}, {(0, 1): 1}
            )

    def test_corner_census_assigns_one_owner_and_keeps_both_edge_references(self):
        # P=mu+t and Q=2*mu+2*t share exactly the corner (0,0).
        p = {(1, 0): 1, (0, 1): 1}
        q = {(1, 0): 2, (0, 1): 2}
        result = compactified_boundary_corner_census(p, q)
        self.assertEqual(
            result["status"], "BOUNDARY_ROOT_CENSUS_WITH_CORNER_OWNERSHIP"
        )
        corner = result["corners"]["mu0_t0"]
        self.assertEqual(corner["status"], "CORNER_OWNED_ONCE")
        self.assertEqual(corner["owner"]["edge"], "mu_zero")
        self.assertEqual(
            {item["edge"] for item in corner["occurrences"]},
            {"mu_zero", "t_zero"},
        )
        vertical = result["edges"]["mu_zero"]["isolated_factors"][0]
        horizontal = result["edges"]["t_zero"]["isolated_factors"][0]
        self.assertEqual(
            vertical["root_ownership"][0]["state"],
            "CANONICAL_CORNER_OWNER",
        )
        self.assertEqual(
            horizontal["root_ownership"][0]["state"],
            "CORNER_REFERENCE_ONLY",
        )

    def test_corner_census_assigns_each_of_four_corners_to_vertical_edge(self):
        # P=mu*(1-mu)+t*(1-t), Q=2P: all four corners are roots.
        p = {(1, 0): 1, (2, 0): -1, (0, 1): 1, (0, 2): -1}
        q = {(1, 0): 2, (2, 0): -2, (0, 1): 2, (0, 2): -2}
        result = compactified_boundary_corner_census(p, q)
        self.assertEqual(
            result["status"], "BOUNDARY_ROOT_CENSUS_WITH_CORNER_OWNERSHIP"
        )
        self.assertEqual(len(result["corners"]), 4)
        self.assertEqual(
            {key: value["owner"]["edge"] for key, value in result["corners"].items()},
            {
                "mu0_t0": "mu_zero",
                "mu0_t1": "mu_zero",
                "mu1_t0": "mu_one",
                "mu1_t1": "mu_one",
            },
        )

    def test_corner_census_propagates_partial_edge_isolation(self):
        p = {(0, 2): 2, (0, 0): -1}
        q = {(0, 4): 4, (0, 2): -4, (0, 0): 1}
        result = compactified_boundary_corner_census(
            p, q, width=Fraction(1, 2**30),
            max_depth=1, max_intervals=100,
        )
        self.assertEqual(result["status"], "PARTIAL_BOUNDARY_ROOT_ISOLATION")
        self.assertEqual(
            result["corner_deduplication"], "CORNER_OWNERSHIP_COMPLETE"
        )

    def test_concentration_resultant_eliminates_mean_and_projects_t(self):
        # P=mu-t, Q=2*mu-1; Res_mu(P,Q)=2*t-1.
        p = {(1, 0): 1, (0, 1): -1}
        q = {(1, 0): 2, (0, 0): -1}
        result = compactified_concentration_resultant_t(p, q)
        self.assertEqual(result["status"], "EXACT_RESULTANT_NONZERO")
        self.assertEqual(result["resultant"], (Fraction(-1), Fraction(2)))
        self.assertEqual(result["eliminated_axis"], "mu")
        self.assertEqual(result["projection_axis"], "t")
        self.assertEqual(result["mathematical_object"], "RESULTANT_MU_P_Q")

    def test_concentration_root_isolation_preserves_even_multiplicity(self):
        # P=mu-t, Q=(mu+t-1)^2; Res_mu(P,Q)=(2*t-1)^2.
        p = {(1, 0): 1, (0, 1): -1}
        q = {
            (2, 0): 1, (1, 1): 2, (0, 2): 1,
            (1, 0): -2, (0, 1): -2, (0, 0): 1,
        }
        resultant = compactified_concentration_resultant_t(p, q)
        self.assertEqual(
            resultant["resultant"],
            (Fraction(1), Fraction(-4), Fraction(4)),
        )
        isolated = compactified_concentration_root_isolation_t(
            resultant, width=Fraction(1, 100)
        )
        self.assertEqual(
            isolated["status"], "PROJECTION_ROOT_ISOLATION_COMPLETE"
        )
        self.assertEqual(isolated["axis"], "t")
        self.assertEqual(isolated["factors"][0]["projection_multiplicity"], 2)
        self.assertEqual(
            isolated["factors"][0]["exact_roots"], (Fraction(1, 2),)
        )

    def test_concentration_resultant_rejects_malformed_sparse_input(self):
        with self.assertRaisesRegex(ValueError, "POLYNOMIAL_MUST_HAVE_INTEGER_SPARSE_TERMS"):
            compactified_concentration_resultant_t(
                {(0.5, 0): 1}, {(1, 0): 1}
            )

    def test_projection_root_isolation_preserves_projection_multiplicity(self):
        # Res_t(t-mu, (t+mu-1)^2) = (2*mu-1)^2.
        p = {(0, 1): 1, (1, 0): -1}
        q = {
            (0, 2): 1, (1, 1): 2, (0, 1): -2,
            (2, 0): 1, (1, 0): -2, (0, 0): 1,
        }
        resultant = compactified_projection_resultant_mu(p, q)
        self.assertEqual(
            resultant["resultant"],
            (Fraction(1), Fraction(-4), Fraction(4)),
        )
        isolated = compactified_projection_root_isolation_mu(
            resultant, width=Fraction(1, 100)
        )
        self.assertEqual(
            isolated["status"], "PROJECTION_ROOT_ISOLATION_COMPLETE"
        )
        factor = isolated["factors"][0]
        self.assertEqual(factor["projection_multiplicity"], 2)
        self.assertEqual(factor["exact_roots"], (Fraction(1, 2),))
        self.assertEqual(
            isolated["multiplicity_warning"],
            "PROJECTION_MULTIPLICITY_IS_NOT_LOCAL_INTERSECTION_MULTIPLICITY",
        )

    def test_projection_root_isolation_handles_irrational_root(self):
        # Res_t(t, 2*t+2*mu^2-1) = 2*mu^2-1.
        p = {(0, 1): 1}
        q = {(0, 1): 2, (2, 0): 2, (0, 0): -1}
        resultant = compactified_projection_resultant_mu(p, q)
        isolated = compactified_projection_root_isolation_mu(
            resultant, width=Fraction(1, 32)
        )
        self.assertEqual(
            isolated["status"], "PROJECTION_ROOT_ISOLATION_COMPLETE"
        )
        intervals = isolated["factors"][0]["isolating_intervals"]
        self.assertEqual(len(intervals), 1)
        self.assertEqual(intervals[0]["root_count"], 1)
        self.assertLess(intervals[0]["interval"][0], Fraction(3, 4))
        self.assertGreater(intervals[0]["interval"][1], Fraction(7, 10))

    def test_projection_root_isolation_retains_partial_and_nonresultant_states(self):
        p = {(0, 1): 1}
        q = {(0, 1): 2, (2, 0): 2, (0, 0): -1}
        resultant = compactified_projection_resultant_mu(p, q)
        partial = compactified_projection_root_isolation_mu(
            resultant, width=Fraction(1, 1000), max_depth=0
        )
        self.assertEqual(
            partial["status"], "PROJECTION_ROOT_ISOLATION_PARTIAL"
        )
        unavailable = compactified_projection_root_isolation_mu(
            {"status": "ZERO_RESULTANT_COMMON_FACTOR_OR_DEGENERACY"},
            width=Fraction(1, 100),
        )
        self.assertEqual(
            unavailable["status"],
            "PROJECTION_ISOLATION_NOT_AVAILABLE_FROM_RESULTANT_STATUS",
        )
        with self.assertRaisesRegex(ValueError, "EXACT_RATIONAL_REQUIRED"):
            compactified_projection_root_isolation_mu(
                {"status": "EXACT_RESULTANT_NONZERO", "resultant": (0.5, 1)},
                width=Fraction(1, 100),
            )
        with self.assertRaisesRegex(ValueError, "ISOLATION_WIDTH_MUST_BE_POSITIVE"):
            compactified_projection_root_isolation_mu(
                resultant, width=0
            )

    def test_projection_resultant_exact_linear_fixture(self):
        p = {(0, 1): 1, (1, 0): -1}       # t - mu
        q = {(0, 1): 2, (0, 0): -1}      # 2*t - 1
        result = compactified_projection_resultant_mu(p, q)
        self.assertEqual(result["status"], "EXACT_RESULTANT_NONZERO")
        self.assertEqual(result["resultant"], (Fraction(-1), Fraction(2)))
        self.assertEqual(result["matrix_dimension"], 2)

    def test_projection_resultant_detects_mixed_common_factor(self):
        # P=(t-mu)(t+1), Q=(t-mu)(t+2).
        p = {(0, 2): 1, (0, 1): 1, (1, 1): -1, (1, 0): -1}
        q = {(0, 2): 1, (0, 1): 2, (1, 1): -1, (1, 0): -2}
        result = compactified_projection_resultant_mu(p, q)
        self.assertEqual(
            result["status"], "ZERO_RESULTANT_COMMON_FACTOR_OR_DEGENERACY"
        )
        self.assertEqual(result["resultant"], (Fraction(0),))

    def test_projection_resultant_restores_axis_contents(self):
        # P=(mu-1)(t+1), Q=(mu-1)(t+2).
        p = {(1, 1): 1, (0, 1): -1, (1, 0): 1, (0, 0): -1}
        q = {(1, 1): 1, (0, 1): -1, (1, 0): 2, (0, 0): -2}
        result = compactified_projection_resultant_mu(p, q)
        self.assertEqual(result["status"], "EXACT_RESULTANT_NONZERO")
        self.assertEqual(
            result["resultant"],
            (Fraction(1), Fraction(-2), Fraction(1)),
        )
        self.assertEqual(result["content_mu_p"], (Fraction(-1), Fraction(1)))
        self.assertEqual(result["content_mu_q"], (Fraction(-1), Fraction(1)))

    def test_projection_resultant_retains_degree_drop_candidate(self):
        # P=mu*t+1, Q=t+1; the resultant vanishes at mu=1.
        p = {(1, 1): 1, (0, 0): 1}
        q = {(0, 1): 1, (0, 0): 1}
        result = compactified_projection_resultant_mu(p, q)
        self.assertEqual(result["resultant"], (Fraction(-1), Fraction(1)))
        self.assertEqual(result["status"], "EXACT_RESULTANT_NONZERO")

    def test_projection_resultant_resource_and_invalid_input_abstain(self):
        p = {(0, 2): 1, (0, 0): 1}
        q = {(0, 2): 1, (0, 1): 1}
        limited = compactified_projection_resultant_mu(
            p, q, max_matrix_dimension=3
        )
        self.assertEqual(limited["status"], "RESULTANT_MATRIX_RESOURCE_LIMIT")
        with self.assertRaisesRegex(ValueError, "MAX_MATRIX_DIMENSION_MUST_BE_POSITIVE_INTEGER"):
            compactified_projection_resultant_mu(p, q, max_matrix_dimension=0)
        zero = compactified_projection_resultant_mu({}, q)
        self.assertEqual(zero["status"], "ZERO_POLYNOMIAL_RESULTANT_UNRESOLVED")

    def test_axis_common_component_detects_vertical_factor_and_multiplicity(self):
        p = {(1, 1): 2, (1, 0): 2, (0, 1): -1, (0, 0): -1}
        q = {(1, 2): 2, (1, 0): 4, (0, 2): -1, (0, 0): -2}
        result = compactified_axis_common_components(p, q)
        self.assertEqual(
            result["status"], "AXIS_ALIGNED_COMMON_COMPONENTS_DETECTED"
        )
        vertical = result["axes"]["mu"]
        self.assertEqual(vertical["component_type"], "VERTICAL_COMMON_COMPONENT")
        self.assertEqual(vertical["common_factor"], (Fraction(-1, 2), Fraction(1)))
        self.assertEqual(vertical["squarefree_factors"][0]["multiplicity"], 1)
        self.assertEqual(
            result["general_mixed_bivariate_factors"], "NOT_CHECKED"
        )

    def test_axis_common_component_detects_horizontal_repeated_factor(self):
        p = {(0, 2): 4, (0, 1): -4, (0, 0): 1, (1, 2): 4, (1, 1): -4, (1, 0): 1}
        q = {(0, 2): 8, (0, 1): -8, (0, 0): 2, (1, 2): 4, (1, 1): -4, (1, 0): 1}
        result = compactified_axis_common_components(p, q)
        horizontal = result["axes"]["t"]
        self.assertEqual(
            horizontal["component_type"], "HORIZONTAL_COMMON_COMPONENT"
        )
        self.assertEqual(horizontal["squarefree_factors"][0]["multiplicity"], 2)

    def test_axis_common_component_reports_absence_without_overclaim(self):
        p = {(1, 0): 1, (0, 1): 1}
        q = {(0, 0): 1, (1, 1): 1}
        result = compactified_axis_common_components(p, q)
        self.assertEqual(
            result["status"], "NO_AXIS_ALIGNED_COMMON_COMPONENT_DETECTED"
        )
        self.assertEqual(
            result["general_mixed_bivariate_factors"], "NOT_CHECKED"
        )

    def test_axis_common_component_abstains_on_zero_polynomial(self):
        result = compactified_axis_common_components({}, {(1, 0): 1, (0, 0): -1})
        self.assertEqual(
            result["status"], "ZERO_POLYNOMIAL_COMMON_COMPONENT_UNRESOLVED"
        )
        zero_terms = compactified_axis_common_components(
            {(0, 0): 0}, {(1, 0): 1, (0, 0): -1}
        )
        self.assertEqual(
            zero_terms["status"], "ZERO_POLYNOMIAL_COMMON_COMPONENT_UNRESOLVED"
        )
        with self.assertRaisesRegex(ValueError, "POLYNOMIAL_MUST_HAVE_INTEGER_SPARSE_TERMS"):
            compactified_axis_common_components({}, {(0, 0): Fraction(1, 2)})

    def test_axis_common_component_rejects_noninteger_sparse_input(self):
        with self.assertRaisesRegex(ValueError, "POLYNOMIAL_MUST_HAVE_INTEGER_SPARSE_TERMS"):
            compactified_axis_common_components({(0, 0): Fraction(1, 2)}, {(0, 0): 1})
        with self.assertRaisesRegex(ValueError, "AXIS_MUST_BE_MU_OR_T"):
            from c10s_f5_rational_score_polynomials import _bivariate_axis_content
            _bivariate_axis_content({(0, 0): 1}, "kappa")

    def test_joint_corner_limits_are_path_independent_for_all_zero_histogram(self):
        result = beta_binomial_joint_corner_likelihood_limits(4, {0: 3})
        self.assertEqual(
            result["status"], "ALL_JOINT_CORNER_LIMITS_PATH_INDEPENDENT"
        )
        self.assertEqual(
            result["corners"]["mu_zero_t_zero"]["likelihood"], Fraction(1)
        )
        self.assertEqual(
            result["corners"]["mu_zero_t_one"]["likelihood"], Fraction(1)
        )
        self.assertEqual(
            result["corners"]["mu_one_t_zero"]["likelihood"], Fraction(0)
        )
        self.assertEqual(
            result["corners"]["mu_one_t_one"]["likelihood"], Fraction(0)
        )
        self.assertEqual(
            result["corners"]["mu_zero_t_zero"]["limit_distribution"],
            (Fraction(1), Fraction(0), Fraction(0), Fraction(0), Fraction(0)),
        )

    def test_joint_corner_limits_are_path_independent_for_all_r_histogram(self):
        result = beta_binomial_joint_corner_likelihood_limits(3, {3: 2})
        self.assertEqual(
            result["corners"]["mu_one_t_zero"]["likelihood"], Fraction(1)
        )
        self.assertEqual(
            result["corners"]["mu_one_t_one"]["likelihood"], Fraction(1)
        )
        self.assertEqual(
            result["corners"]["mu_zero_t_zero"]["likelihood"], Fraction(0)
        )
        self.assertEqual(
            result["corners"]["mu_one_t_zero"]["limit_distribution"],
            (Fraction(0), Fraction(0), Fraction(0), Fraction(1)),
        )

    def test_joint_corner_limits_zero_likelihood_for_mixed_and_interior_counts(self):
        for histogram in ({0: 1, 4: 1}, {2: 1}, {0: 1, 2: 1, 4: 1}):
            result = beta_binomial_joint_corner_likelihood_limits(4, histogram)
            for corner in ("mu_zero_t_zero", "mu_zero_t_one"):
                self.assertEqual(
                    result["corners"][corner]["likelihood"], Fraction(0)
                )
            for corner in ("mu_one_t_zero", "mu_one_t_one"):
                self.assertEqual(
                    result["corners"][corner]["likelihood"], Fraction(0)
                )

    def test_joint_corner_limits_reuse_histogram_validation(self):
        with self.assertRaisesRegex(ValueError, "POSITIVE_TOTAL_MULTIPLICITY_REQUIRED"):
            beta_binomial_joint_corner_likelihood_limits(4, {0: 0})
        with self.assertRaisesRegex(ValueError, "COUNT_OUTSIDE_0_TO_R"):
            beta_binomial_joint_corner_likelihood_limits(4, {5: 1})

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


    def test_conditional_mean_tube_prunes_interval_when_concentration_score_excludes_zero(self):
        result = conditional_mean_tube_and_concentration_exclusion(
            {(0, 0): 1, (1, 0): -2},
            {(0, 0): 1},
            t_bounds=(Fraction(0), Fraction(1)),
            max_mu_depth=4,
        )
        self.assertEqual(result["status"], "NO_COMMON_STATIONARY_POINT_ON_T_INTERVAL")
        self.assertEqual(result["mean_root_tube_mu_bounds"], (Fraction(1, 2), Fraction(1, 2)))
        self.assertTrue(result["mean_root_existence_for_every_t_certified"])
        self.assertTrue(result["concentration_score_excludes_zero_on_tube"])

    def test_conditional_mean_tube_retains_candidate_interval(self):
        result = conditional_mean_tube_and_concentration_exclusion(
            {(0, 0): 1, (1, 0): -2},
            {(0, 1): 2, (0, 0): -1},
            t_bounds=(Fraction(0), Fraction(1)),
            max_mu_depth=4,
        )
        self.assertEqual(result["status"], "CANDIDATE_T_INTERVAL_UNRESOLVED")
        self.assertEqual(result["mean_root_tube_mu_bounds"], (Fraction(1, 2), Fraction(1, 2)))
        self.assertFalse(result["concentration_score_excludes_zero_on_tube"])

    def test_conditional_mean_tube_abstains_without_strict_endpoint_signs(self):
        result = conditional_mean_tube_and_concentration_exclusion(
            {(1, 0): 1},
            {(0, 0): 1},
            t_bounds=(Fraction(0), Fraction(1)),
            max_mu_depth=4,
        )
        self.assertEqual(result["status"], "MEAN_ROOT_TUBE_UNRESOLVED_ENDPOINT_SIGNS")

    def test_conditional_mean_tube_rejects_invalid_domain_and_budget(self):
        with self.assertRaisesRegex(ValueError, "T_BOUNDS_MUST_BE_WITHIN_UNIT_INTERVAL"):
            conditional_mean_tube_and_concentration_exclusion(
                {(0, 0): 1, (1, 0): -2}, {(0, 0): 1},
                t_bounds=(Fraction(-1, 2), Fraction(1)), max_mu_depth=4,
            )
        with self.assertRaisesRegex(ValueError, "MAX_MU_DEPTH_MUST_BE_INTEGER_1_TO_16"):
            conditional_mean_tube_and_concentration_exclusion(
                {(0, 0): 1, (1, 0): -2}, {(0, 0): 1},
                t_bounds=(Fraction(0), Fraction(1)), max_mu_depth=0,
            )


if __name__ == "__main__":
    unittest.main()
