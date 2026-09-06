# EXT-1.1 Rust — DR-023A Ex-Ante Outcome / Horizon Design v0.1

**Status:** EX-ANTE DESIGN ANALYSIS — NO ACCEPTANCE
**Scope:** Selection of outcome, horizon, and follow-up rule for EXT-1.1
**Prerequisite:** DR-023 structural audit PASS

## 1. Purpose

This record defines the methodological gate for selecting one primary post-origin outcome and one primary observation horizon without inspecting confirmatory associations involving `T_acc`, `B`, or `R`.

It is deliberately a design record, not an experimental result and not an acceptance of DR-023.

## 2. Candidate outcomes

### A. `subsequent_release_activity`

Binary event:

`Y_H(v_o) = 1` iff at least one release of the same package as origin release `v_o` has `created_at` strictly greater than `created_at(v_o)` and no later than `created_at(v_o) + H`.

Otherwise `Y_H(v_o) = 0`, provided complete follow-up through `H` is available.

### B. `later_package_state_transition`

A later package-version event for the same package within `H`.

This is structurally available but is less parsimonious because the event is not substantively distinct from release activity in the current observational unit: a package-version observation is itself a release event.

## 3. Ex-ante comparison

`subsequent_release_activity` is preferred as the primary candidate because:

1. it is directly observable in the accepted package-version representation;
2. it is strictly post-origin;
3. it is independent of `T_acc`, `R*`, and `B` by construction;
4. it does not require a popularity, download, adoption, or downstream-success proxy;
5. it is binary and therefore imposes minimal outcome structure;
6. it has an unambiguous event interpretation at the package level;
7. `later_package_state_transition` does not add a substantively different event under the current observational unit.

This preference is based on ontology, observability, non-circularity, and minimality only. No empirical association has been inspected.

## 4. Horizon requirements

The primary horizon `H` must satisfy all of the following:

- be fixed before confirmatory outcome analysis;
- be common to all primary observations;
- be long enough to represent a meaningful subsequent package trajectory rather than an immediate administrative artefact;
- be short enough to remain interpretable as a local post-origin trajectory;
- be supported by the temporal extent of the frozen snapshot;
- permit an explicit complete-follow-up rule;
- not be selected by maximizing any association, significance, effect size, or sample size after outcome construction.

No numerical `H` is selected in this document.

## 5. Follow-up / censoring principle

For a fixed primary horizon `H`, an origin release is eligible for the primary binary outcome only when the frozen snapshot contains observable package-version coverage through:

`created_at(v_o) + H`.

Origins too close to the dataset's terminal observation boundary to have complete follow-up are excluded from the primary horizon analysis rather than treated as negative outcomes.

This rule prevents right-censored origins from being misclassified as `Y_H = 0`.

The terminal coverage criterion is defined from the frozen dataset's maximum observable `package_versions.created_at`, not from outcome prevalence or predictor values.

## 6. Important distinction

The follow-up rule is not a sampling optimization. It is part of the outcome's measurement definition and must therefore be frozen before confirmatory execution.

The exclusion of incomplete-follow-up origins may reduce the eligible population. Any later sampling decision must operate only after this eligibility rule has been frozen.

## 7. Horizon selection protocol

Before selecting the numerical horizon, the following non-confirmatory questions must be resolved:

1. Is a fixed-day horizon preferable to a calendar-based horizon? **Yes.** A fixed elapsed-time window is invariant to release-calendar irregularities and directly represents temporal exposure after the origin event.
2. Should multiple horizons be searched and the best retained? **No.** That creates researcher degrees of freedom unless alternatives are explicitly pre-registered as secondary/exploratory.
3. Should the primary horizon be chosen from the outcome distribution? **No.** That would make the outcome itself influence the design criterion.
4. Should the horizon be chosen from predictor distributions? **No.** That would couple the outcome definition to `T_acc`.
5. Should incomplete follow-up be coded as zero? **No.** It conflates absence of observed event with absence of observation opportunity.

## 8. Current provisional conclusion

The ex-ante design analysis supports:

`Primary outcome candidate = subsequent_release_activity`

and

`Primary outcome = 1 iff a later release of the same package occurs within H days; otherwise 0, only for origins with complete H-day follow-up.`

The numerical value of `H` remains OPEN.

## 9. Next gate

The next action is a **horizon-justification audit** that may use only non-confirmatory information: dataset temporal coverage, methodological requirements of the outcome definition, and independently stated design criteria. It must not calculate or inspect `Y_H`, outcome prevalence, `T_acc` associations, effect sizes, significance, or any pilot/confirmatory result.

Only after that gate may DR-023 be converted into an accepted decision record.

## 10. Explicit non-claims

This document does not claim that subsequent release activity is caused by or statistically associated with `T_acc`. It does not establish predictive validity. It does not choose sampling, pilot size, baseline encoding, representation serialization, or any confirmatory statistical procedure.
