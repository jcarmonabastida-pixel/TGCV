"""Contract tests for the F1/Sturm adjudication adapter."""
from fractions import Fraction
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from c10s_f1_root_adjudication import adjudicate_f1_roots
from c10s_f1_between_profile_likelihood import F1ProfileError
from c10s_f1_independent_root_isolator import IsolatedRoot, RootIsolationResult


class F1RootAdjudicationTests(unittest.TestCase):
    def setUp(self):
        self.f1 = SimpleNamespace(
            status="POLYNOMIAL_ROOTS_ISOLATED",
            coefficients_ascending=(-1.0, 1.0),
            positive_roots=(1.0,),
        )

    def test_matching_simple_root_is_agreement(self):
        independent = RootIsolationResult(
            "ROOTS_ISOLATED", 1,
            (IsolatedRoot(Fraction(1), Fraction(1), 1),),
        )
        with patch("c10s_f1_root_adjudication.f1_score_polynomial_diagnostic",
                   return_value=self.f1), patch(
            "c10s_f1_root_adjudication.isolate_real_roots",
            return_value=independent,
        ):
            result = adjudicate_f1_roots((), between_variance=0.2)
        self.assertEqual(result.status, "ROOTS_AGREE")
        self.assertEqual(result.matched_root_count, 1)

    def test_root_count_mismatch_is_discrepant(self):
        independent = RootIsolationResult(
            "ROOTS_ISOLATED", 2,
            (
                IsolatedRoot(Fraction(1), Fraction(1), 1),
                IsolatedRoot(Fraction(2), Fraction(2), 1),
            ),
        )
        with patch("c10s_f1_root_adjudication.f1_score_polynomial_diagnostic",
                   return_value=self.f1), patch(
            "c10s_f1_root_adjudication.isolate_real_roots",
            return_value=independent,
        ):
            result = adjudicate_f1_roots((), between_variance=0.2)
        self.assertEqual(result.status, "ROOTS_DISCREPANT")
        self.assertEqual(result.independent_root_count, 2)

    def test_multiple_root_is_unresolved_when_f1_has_no_certified_multiplicity(self):
        independent = RootIsolationResult(
            "ROOTS_ISOLATED", 2,
            (IsolatedRoot(Fraction(1), Fraction(1), 2),),
        )
        with patch("c10s_f1_root_adjudication.f1_score_polynomial_diagnostic",
                   return_value=self.f1), patch(
            "c10s_f1_root_adjudication.isolate_real_roots",
            return_value=independent,
        ):
            result = adjudicate_f1_roots((), between_variance=0.2)
        self.assertEqual(result.status, "ROOTS_UNRESOLVED")
        self.assertTrue(result.multiplicity_review_required)

    def test_unresolved_f1_diagnostic_stops_before_sturm(self):
        unresolved = SimpleNamespace(
            status="POLYNOMIAL_ROOTS_UNRESOLVED",
            coefficients_ascending=(-1.0, 1.0),
            positive_roots=(),
        )
        with patch("c10s_f1_root_adjudication.f1_score_polynomial_diagnostic",
                   return_value=unresolved), patch(
            "c10s_f1_root_adjudication.isolate_real_roots") as isolate:
            result = adjudicate_f1_roots((), between_variance=0.2)
        self.assertEqual(result.status, "ROOTS_UNRESOLVED")
        isolate.assert_not_called()

    def test_rejects_nonfinite_isolation_width(self):
        for value in (float("inf"), float("nan"), 0.0, -1.0):
            with self.subTest(value=value):
                with self.assertRaises(F1ProfileError):
                    adjudicate_f1_roots(
                        (), between_variance=0.2, isolation_width=value,
                    )

    def test_rejects_nonfinite_tolerances(self):
        for value in (float("inf"), float("nan"), 0.0, -1.0):
            with self.subTest(value=value):
                with self.assertRaises(F1ProfileError):
                    adjudicate_f1_roots(
                        (), between_variance=0.2, match_tolerance=value,
                    )


if __name__ == "__main__":
    unittest.main()
