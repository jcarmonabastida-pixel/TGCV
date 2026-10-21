"""Deterministic, bounded condition evaluator for the Collective Toy prototype.

This module evaluates only a tiny expression format. It never uses eval/exec,
attribute access, function calls, or arbitrary Python expressions.

Expression grammar:
    identifier ( "<" | "<=" | "==" | "!=" | ">=" | ">" ) number

Identifiers are ASCII names such as soil_moisture_pct and low_threshold.
Values must be finite numbers (booleans are rejected). Missing variables or
unsupported expressions return NOT_EVALUABLE rather than guessing.
"""
from __future__ import annotations

from dataclasses import dataclass
import math
import re
from typing import Any, Mapping

EVALUATOR_VERSION = "condition-evaluator-001"
_EXPRESSION = re.compile(
    r"^\s*([A-Za-z_][A-Za-z0-9_]*)\s*(<=|>=|==|!=|<|>)\s*"
    r"(-?(?:0|[1-9][0-9]*)(?:\.[0-9]+)?)\s*$"
)
_ALLOWED_OPERATORS = {"<", "<=", "==", "!=", ">=", ">"}


@dataclass(frozen=True)
class ConditionResult:
    status: str
    expression: str
    value: bool | None
    reason: str | None = None
    variable: str | None = None

    def to_dict(self) -> dict[str, Any]:
        return {
            "status": self.status,
            "expression": self.expression,
            "value": self.value,
            "reason": self.reason,
            "variable": self.variable,
            "evaluator_version": EVALUATOR_VERSION,
        }


def evaluate_condition(expression: str, values: Mapping[str, Any]) -> ConditionResult:
    """Return TRUE/FALSE only for a supported comparison with a supplied number."""
    if not isinstance(expression, str):
        return ConditionResult("NOT_EVALUABLE", str(expression), None, "expression_not_string")
    match = _EXPRESSION.fullmatch(expression)
    if not match:
        return ConditionResult("NOT_EVALUABLE", expression, None, "unsupported_expression")
    variable, operator, literal = match.groups()
    if operator not in _ALLOWED_OPERATORS:
        return ConditionResult("NOT_EVALUABLE", expression, None, "unsupported_operator", variable)
    if not isinstance(values, Mapping) or variable not in values:
        return ConditionResult("NOT_EVALUABLE", expression, None, "missing_variable", variable)
    observed = values[variable]
    if isinstance(observed, bool) or not isinstance(observed, (int, float)):
        return ConditionResult("NOT_EVALUABLE", expression, None, "variable_not_numeric", variable)
    if not math.isfinite(float(observed)):
        return ConditionResult("NOT_EVALUABLE", expression, None, "variable_not_finite", variable)
    threshold = float(literal)
    comparisons = {
        "<": observed < threshold,
        "<=": observed <= threshold,
        "==": observed == threshold,
        "!=": observed != threshold,
        ">=": observed >= threshold,
        ">": observed > threshold,
    }
    return ConditionResult("TRUE" if comparisons[operator] else "FALSE", expression, comparisons[operator], None, variable)
