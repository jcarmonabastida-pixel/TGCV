from __future__ import annotations

import unittest
from fractions import Fraction

from c10s_f5_adaptive_profile_lr import adaptive_refine_lr_results


def _result(bounds, status="LR_STATISTIC_ENCLOSED"):
    return {"status": status, "lr_statistic_bounds": bounds}


def _classifier(result, cutoff):
    if result.get("status") == "LR_STATISTIC_INFINITE":
        return "OUT"
    lower, upper = result["lr_statistic_bounds"]
    if upper <= cutoff:
        return "IN"
    if lower > cutoff:
        return "OUT"
    return "AMBIGUOUS"


class AdaptiveExactLRRefinementTests(unittest.TestCase):
    def setUp(self):
        self.widths = (
            Fraction(1, 2**8),
            Fraction(1, 2**16),
            Fraction(1, 2**24),
        )

    def test_refines_only_until_cutoff_classification_is_exact(self):
        results = {
            self.widths[0]: _result((Fraction(2), Fraction(4))),
            self.widths[1]: _result((Fraction(3), Fraction(7, 2))),
        }
        observed = adaptive_refine_lr_results(
            lambda width: results[width],
            cutoff=Fraction(18, 5),
            widths=self.widths,
            classifier=_classifier,
        )
        self.assertEqual(observed["status"], "ADAPTIVE_CLASSIFIED")
        self.assertEqual(observed["classification"], "IN")
        self.assertEqual(observed["selected_width"], self.widths[1])
        self.assertEqual(observed["step_count"], 2)

    def test_rejects_non_nested_exact_enclosures(self):
        results = {
            self.widths[0]: _result((Fraction(2), Fraction(4))),
            self.widths[1]: _result((Fraction(3, 2), Fraction(9, 2))),
        }
        observed = adaptive_refine_lr_results(
            lambda width: results[width],
            cutoff=Fraction(3),
            widths=self.widths,
            classifier=_classifier,
        )
        self.assertEqual(observed["status"], "ADAPTIVE_ENCLOSURE_NESTING_VIOLATION")

    def test_returns_typed_exhaustion_if_cutoff_remains_inside(self):
        results = {
            self.widths[0]: _result((Fraction(2), Fraction(4))),
            self.widths[1]: _result((Fraction(5, 2), Fraction(7, 2))),
            self.widths[2]: _result((Fraction(11, 4), Fraction(13, 4))),
        }
        observed = adaptive_refine_lr_results(
            lambda width: results[width],
            cutoff=Fraction(3),
            widths=self.widths,
            classifier=_classifier,
        )
        self.assertEqual(observed["status"], "ADAPTIVE_REFINEMENT_EXHAUSTED")
        self.assertEqual(observed["step_count"], 3)

    def test_fails_closed_on_unresolved_profile(self):
        observed = adaptive_refine_lr_results(
            lambda width: _result(None, status="CONSTRAINED_PROFILE_MAXIMUM_UNRESOLVED"),
            cutoff=Fraction(3),
            widths=self.widths,
            classifier=_classifier,
        )
        self.assertEqual(observed["status"], "ADAPTIVE_PROFILE_UNRESOLVED")
        self.assertEqual(observed["inner_status"], "CONSTRAINED_PROFILE_MAXIMUM_UNRESOLVED")

    def test_requires_decreasing_positive_exact_widths(self):
        with self.assertRaises(ValueError):
            adaptive_refine_lr_results(
                lambda width: _result((Fraction(1), Fraction(2))),
                cutoff=Fraction(3),
                widths=(Fraction(1, 2**8), Fraction(1, 2**4)),
                classifier=_classifier,
            )


if __name__ == "__main__":
    unittest.main()
