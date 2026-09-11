# IUT-A-01 — U2 Metric Design Revision 001

**Status:** `DESIGN DECISION — PRE-FREEZE`  
**Date:** 2026-09-11  
**Purpose:** resolve the M3 semantic defect identified during Fixture 002 consistency review.

## 1. Decision

M3 is **removed as a primary U2 performance metric** for the current computational pilot family.

M1 remains the primary accuracy metric. M2 remains the secondary computational-performance metric.

A future alternative-space metric may be introduced only as a separately specified metric with an independent semantic definition and predeclared scoring rule.

## 2. Reason

The previous M3 definition measured whether the selected option was outside the frozen viable set. That does not measure the intended TGCV-specific capability when both arms are allowed to select any viable option. It therefore cannot cleanly distinguish:

- choosing a non-preferred but admissible alternative, from
- failing to represent or discover an accessible alternative space.

The defect is conceptual rather than computational.

## 3. U2 metric set

### M1 — Decision correctness

`M1 = proportion of trials in which selected_option == frozen preferred_option`.

The preferred option is derived from the frozen objective over the frozen feasible set.

### M2 — Decision time

Elapsed decision time from presentation of the frozen trial input to emitted decision, using the predeclared timing basis. Timing overhead is reported separately.

## 4. Optional future metric

A future U2 extension may define an explicit **reachable-alternative discovery rate**, but only if:

1. the target alternative is independently identifiable from the frozen task semantics;
2. the metric distinguishes accessibility discovery from mere option preference;
3. numerator and denominator are one-to-one trial events;
4. the metric is bounded in `[0,1]`;
5. the scoring rule is frozen before execution;
6. the metric is not introduced post hoc to rescue a result.

This metric is not part of Fixture 002 execution.

## 5. Interpretation rule

U2-POSITIVE requires M1 not to suffer material degradation and at least one predeclared secondary performance criterion to meet its threshold, subject to the existing protocol's integrity and classification rules.

If only M1 is available and M2 fails its threshold, the result is not positive under the existing U2 protocol.

No metric may be selected after observing execution results.

## 6. Versioning

This revision does not alter Protocol 001 or any historical execution. A future execution requiring this metric design must use an explicitly versioned manifest/protocol relationship.

Fixture 001, FULL_PILOT 001, and Fixture 002 draft remain preserved unchanged.

## 7. Gate

Before Fixture 002 can be frozen, the manifest and executor must be versioned consistently with this metric decision, and a dedicated fixture consistency audit must pass.
