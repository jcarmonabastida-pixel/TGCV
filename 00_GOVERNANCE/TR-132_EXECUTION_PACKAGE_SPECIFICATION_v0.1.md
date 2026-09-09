# TR-132 — Execution Package Specification v0.1

**Status:** CURRENT / OPERATIVE — DESIGN-ONLY
**Execution:** NOT AUTHORIZED
**Date:** 2026-09-09
**Parent protocol:** `00_GOVERNANCE/TR-132_EXECUTABLE_PROTOCOL_v0.1.md`

## 1. Purpose

Define the frozen execution package required to instantiate TR-132 without allowing the dataset, case, observed result, or downstream outcome to determine the operational definition of `T_acc`.

This specification is preparation infrastructure only. It does not select a dataset, industrial case, or empirical result.

## 2. Target claim and required level

Before execution, the package MUST name the target claim and the minimum identifiability level required by the claim-identifiability matrix.

Permitted levels:
- L1 — certified accessible candidate;
- L2 — certified bounded subset `T_acc^+`;
- L3 — bounded temporal change `ΔT_acc^+`;
- L4 — complete/full-space `T_acc`.

The package MUST NOT silently substitute a stronger or weaker level after execution begins.

## 3. Unit and temporal frame

The package MUST freeze:
- system boundary `S`;
- unit of analysis;
- state/context representation at each decision time;
- decision time(s) and temporal horizon;
- relevant rules/constraints `L`;
- material/setup/authorization conditions that are part of accessibility.

## 4. Candidate transformation universe

The candidate universe MUST be defined before result inspection.

Each candidate transformation `τ` MUST have a stable identity rule that permits independent matching across the relevant timepoints.

The universe MAY be bounded for L2/L3, but the bound MUST be explicit and fixed ex ante. A bounded universe MUST NOT be represented as the complete `T_acc` unless completeness is independently demonstrated.

## 5. Accessibility predicate

The package MUST freeze an explicit predicate for certification of accessibility. The predicate MUST distinguish at least:

1. technical/physical possibility (`T_poss`);
2. admissibility under applicable rules (`T_adm`);
3. effective decision-time accessibility (`T_acc`);
4. realized/observed transformation (`T_obs`).

Accessibility MUST be adjudicated independently of whether the transformation was subsequently realized. Non-observation MUST NOT be treated as proof of inaccessibility.

## 6. Evidence rules

The package MUST freeze:
- admissible evidence classes;
- evidence sufficiency criteria;
- provenance requirements;
- handling of missing, unavailable, ambiguous, or conflicting evidence;
- adjudication procedure and audit record.

Evidence thresholds MUST NOT be relaxed after observing outcomes.

## 7. Bounded subset and comparison rules

For L2/L3, the package MUST freeze the rule selecting `T_acc^+` before results are inspected.

For L3, the package MUST additionally freeze:
- timepoint pair/order;
- identity matching rule;
- comparison rule;
- minimum evidence required to establish membership/non-membership at each timepoint.

A favorable observed change MUST NOT determine subset membership or comparison criteria.

## 8. Outcome independence

Outcome, Reach, Trajectory, Value, or any downstream performance measure MUST NOT be used to define accessibility or select the bounded subset.

If blinding is technically impossible, the execution record MUST document the alternative independence control before execution.

## 9. Reproducibility and manifest

The execution package MUST contain a frozen manifest with:
- package version;
- protocol version;
- execution identifier;
- target claim/level;
- unit/system/timepoints;
- candidate-universe definition;
- accessibility predicate version;
- evidence-rule version;
- subset/comparison-rule versions where applicable;
- input inventory and immutable identifiers;
- environment information;
- expected result schema;
- deviations field, initially empty.

## 10. Result schema

The execution result MUST separately report:

`EXECUTION_ID`
`PROTOCOL_VERSION`
`PACKAGE_VERSION`
`CLAIM_TARGET`
`REQUIRED_LEVEL`
`UNIT`
`TIMEPOINTS`
`CANDIDATE_UNIVERSE`
`ACCESSIBILITY_PREDICATE`
`EVIDENCE_INVENTORY`
`ADJUDICATION`
`CERTIFIED_TACC_PLUS`
`COMPARISON`
`ACHIEVED_LEVEL`
`NON_CIRCULARITY_STATUS`
`DEVIATIONS`
`REPRODUCIBILITY_STATUS`
`DECISION`
`BOUNDED_INTERPRETATION`

The result MUST NOT contain a claim of completeness unless L4 criteria are independently satisfied.

## 11. Stop conditions

Execution MUST stop or return INCONCLUSIVE when a material accessibility condition cannot be independently adjudicated, when candidate identity is ambiguous, when the frozen universe cannot be reconstructed, or when a non-circularity control is violated.

Any violation that allows the result to influence the operational definition invalidates the execution rather than authorizing post-hoc repair.

## 12. Authorization boundary

This specification does NOT authorize execution.

Execution requires a separate explicit authorization record confirming that a concrete package instance has been frozen and that current canonical governance state is PASS.

No dataset, industrial case, partner evidence, causal inference, value assessment, Core modification, or claim upgrade is authorized by this document.

## 13. Required next step

Instantiate one concrete execution package only after separate authorization. Until then, this asset remains DESIGN-ONLY and the scientific state remains unchanged.
