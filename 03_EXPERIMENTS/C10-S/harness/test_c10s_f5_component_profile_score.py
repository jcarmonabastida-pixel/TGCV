from __future__ import annotations

from collections import Counter
from fractions import Fraction
import math
import unittest

from c10s_f5_beta_binomial_likelihood_diagnostics import (
    beta_binomial_loglik_score_hessian,
)
from c10s_f5_component_profile_score import (
    F5ConstrainedScoreError,
    f5_component_profile_score_polynomial,
    f5_isolate_component_profile_score_roots,
)


COUNTS = (0, 1, 2, 3, 4, 5, 1, 3, 4, 2)
R = 5
HISTOGRAM = dict(Counter(COUNTS))


def _profile_derivative(component: str, target: float, mu: float) -> float:
    q = mu * (1.0 - mu)
    if component == "W":
        kappa = target / (q - target)
        kappa_prime = -target * (1.0 - 2.0 * mu) / ((q - target) ** 2)
    else:
        kappa = (q - target) / target
        kappa_prime = (1.0 - 2.0 * mu) / target
    eta = math.log(mu / (1.0 - mu))
    xi = math.log(kappa)
    derivatives = beta_binomial_loglik_score_hessian(
        COUNTS, R, mean_logit=eta, log_concentration=xi,
    )
    score_mu = derivatives.score_mean_logit / q
    score_kappa = derivatives.score_log_concentration / kappa
    return score_mu + score_kappa * kappa_prime


def _evaluate_integer_polynomial(coefficients, x: float) -> float:
    value = 0.0
    for coefficient in reversed(coefficients):
        value = value * x + coefficient
    return value


class F5ConstrainedProfileScoreTests(unittest.TestCase):
    def test_exact_polynomial_sign_matches_independent_analytic_constrained_score(self):
        for component in ("W", "B"):
            for target in (0.05, 0.12):
                polynomial = f5_component_profile_score_polynomial(
                    R, HISTOGRAM, component=component, target=target,
                )
                self.assertIn(
                    polynomial.status,
                    {"EXACT_SCORE_POLYNOMIAL_READY", "NO_INTERIOR_STATIONARY_ROOTS"},
                )
                for mu in (0.31, 0.39, 0.47, 0.53, 0.61, 0.69):
                    if mu * (1.0 - mu) <= target:
                        continue
                    direct = _profile_derivative(component, target, mu)
                    exact_numerator = _evaluate_integer_polynomial(
                        polynomial.coefficients_ascending, mu,
                    )
                    if abs(direct) < 1e-8 or abs(exact_numerator) < 1e-8:
                        continue
                    self.assertEqual(
                        math.copysign(1.0, direct),
                        math.copysign(1.0, exact_numerator),
                        msg=f"{component=} {target=} {mu=} {direct=} {exact_numerator=}",
                    )

    def test_root_isolation_returns_only_feasible_interior_roots(self):
        for component in ("W", "B"):
            polynomial = f5_component_profile_score_polynomial(
                R, HISTOGRAM, component=component, target=Fraction(1, 20),
            )
            roots = f5_isolate_component_profile_score_roots(
                polynomial, isolation_width=Fraction(1, 2**32),
                max_depth=120, max_intervals=5000,
            )
            self.assertIn(
                roots.status,
                {"COMPLETE_ROOT_ISOLATION", "COMPLETE_NO_INTERIOR_ROOTS"},
            )
            self.assertEqual(roots.unresolved_intervals, ())
            for root in roots.roots:
                self.assertEqual(root.feasibility, "FEASIBLE_INTERIOR")
                if root.exact_root is not None:
                    self.assertGreater(
                        root.exact_root * (1 - root.exact_root), polynomial.target,
                    )
                else:
                    lo, hi = root.isolating_interval
                    self.assertGreater(lo * (1 - lo), polynomial.target)
                    self.assertGreater(hi * (1 - hi), polynomial.target)

    def test_polynomial_is_reproducible_and_target_is_exact_binary_rational(self):
        first = f5_component_profile_score_polynomial(
            R, HISTOGRAM, component="W", target=0.1,
        )
        second = f5_component_profile_score_polynomial(
            R, HISTOGRAM, component="W", target=0.1,
        )
        self.assertEqual(first, second)
        self.assertEqual(first.target, Fraction.from_float(0.1))

    def test_invalid_component_and_target_fail_closed(self):
        with self.assertRaisesRegex(F5ConstrainedScoreError, "COMPONENT_MUST"):
            f5_component_profile_score_polynomial(
                R, HISTOGRAM, component="within", target=0.05,
            )
        for target in (0.0, 0.25, -0.1, float("nan")):
            with self.subTest(target=target):
                with self.assertRaises(F5ConstrainedScoreError):
                    f5_component_profile_score_polynomial(
                        R, HISTOGRAM, component="B", target=target,
                    )


if __name__ == "__main__":
    unittest.main()
