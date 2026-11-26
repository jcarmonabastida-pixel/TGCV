from __future__ import annotations

from collections.abc import Callable, Mapping, Sequence
from fractions import Fraction
from typing import Any


def adaptive_refine_lr_results(
    evaluate: Callable[[Fraction], Mapping[str, Any]],
    *,
    cutoff: Fraction,
    widths: Sequence[Fraction],
    classifier: Callable[[Mapping[str, Any], Fraction], str],
) -> dict[str, Any]:
    """Refine exact LR enclosures until classified or the width budget ends.

    Every refinement must be nested inside the preceding exact LR interval.
    Any malformed or unresolved intermediate result fails closed.
    """
    if not isinstance(cutoff, Fraction):
        raise TypeError("CUTOFF_MUST_BE_EXACT_FRACTION")
    if not widths:
        raise ValueError("AT_LEAST_ONE_REFINEMENT_WIDTH_REQUIRED")
    if any(not isinstance(width, Fraction) or width <= 0 for width in widths):
        raise ValueError("REFINEMENT_WIDTHS_MUST_BE_POSITIVE_EXACT_FRACTIONS")
    if any(widths[index + 1] >= widths[index] for index in range(len(widths) - 1)):
        raise ValueError("REFINEMENT_WIDTHS_MUST_BE_STRICTLY_DECREASING")

    history = []
    previous_bounds = None
    for step, width in enumerate(widths, start=1):
        result = evaluate(width)
        if result.get("status") != "LR_STATISTIC_ENCLOSED":
            return {
                "status": "ADAPTIVE_PROFILE_UNRESOLVED",
                "inner_status": result.get("status"),
                "selected_width": width,
                "step_count": step,
                "history": history,
                "last_result": result,
            }
        bounds = result.get("lr_statistic_bounds")
        if (
            not isinstance(bounds, (tuple, list))
            or len(bounds) != 2
            or not all(isinstance(value, Fraction) for value in bounds)
            or bounds[0] > bounds[1]
        ):
            return {
                "status": "ADAPTIVE_LR_BOUNDS_MALFORMED",
                "selected_width": width,
                "step_count": step,
                "history": history,
                "last_result": result,
            }
        lower, upper = bounds
        if previous_bounds is not None:
            previous_lower, previous_upper = previous_bounds
            if lower < previous_lower or upper > previous_upper:
                return {
                    "status": "ADAPTIVE_ENCLOSURE_NESTING_VIOLATION",
                    "selected_width": width,
                    "step_count": step,
                    "previous_bounds": previous_bounds,
                    "observed_bounds": bounds,
                    "history": history,
                    "last_result": result,
                }
        classification = classifier(result, cutoff)
        history.append({
            "width": width,
            "lr_statistic_bounds": bounds,
            "classification": classification,
        })
        if classification in {"IN", "OUT"}:
            return {
                "status": "ADAPTIVE_CLASSIFIED",
                "classification": classification,
                "selected_width": width,
                "step_count": step,
                "lr_statistic_bounds": bounds,
                "history": history,
                "last_result": result,
            }
        if classification != "AMBIGUOUS":
            return {
                "status": "ADAPTIVE_CLASSIFICATION_UNRESOLVED",
                "classification": classification,
                "selected_width": width,
                "step_count": step,
                "history": history,
                "last_result": result,
            }
        previous_bounds = bounds

    return {
        "status": "ADAPTIVE_REFINEMENT_EXHAUSTED",
        "selected_width": widths[-1],
        "step_count": len(widths),
        "lr_statistic_bounds": previous_bounds,
        "history": history,
    }
