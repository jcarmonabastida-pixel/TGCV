# TGCV — C10C-002 Candidate-Specific Causal Execution Specification 001

**Status:** FROZEN — DESIGN SPECIFICATION ONLY; EXECUTION NOT YET AUTHORIZED
**Date:** 2026-09-15
**Candidate:** C10C-002 — The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico
**Source:** OpenICPSR 113705 V1

## 1. Purpose

Freeze the causal design before any new empirical execution. This specification is a methodological C10-C value-linkage design and does not reopen the completed C10C-002 bounded `ΔT_acc` experiment.

## 2. Causal target

The primary target is the causal effect of randomized infrastructure assignment on the subsequent change in an independently measured real-estate value endpoint, with TGCV accessibility change treated as the structural pathway rather than as the final value endpoint.

Conceptual chain:

`Z → ΔS → ΔT_acc(U_τ*) → downstream/property mechanism → ΔV`

The causal estimand is **not** the effect of `ΔT_acc` itself unless an independently identified design for that mediator is later justified.

## 3. Unit and time

- Unit: polygon in the admitted `sample_PANEL==1` universe.
- Panel: baseline (round 1) and follow-up (round 2).
- Structural state: six elemental infrastructure dimensions.
- Bounded transformation universe: 12 opening/closure transformations.
- Treatment assignment: `treat`.
- Municipality identifier: `cve_mun`.

The previously reconstructed 342-polygon panel is the admissible structural/value linkage universe.

## 4. Accessibility construction

For each dimension `j`:

`τ_j+` is structurally accessible when `S_j,t < 1`.

`τ_j−` is structurally accessible when `S_j,t > 0`.

Thus:

`T_acc,t* = {τ_j+ : S_j,t < 1} ∪ {τ_j− : S_j,t > 0}`.

`ΔT_acc` is derived only from baseline/follow-up structural states. Treatment, value and downstream outcomes are prohibited inputs to `P_τ`.

## 5. Value endpoint

The independent value endpoint is the change in professional valuation of unbuilt lots supplied by the real-estate replication layer.

The exact variable, unit, transformation, missing-value rule and aggregation to the polygon-level estimand must be frozen from the admitted V1 value file before execution.

No value-informed accessibility definition is permitted.

## 6. Treatment and counterfactual

Primary assignment variable: `treat`.

Primary contrast: intention-to-treat assignment under the randomized design.

Counterfactual: the same polygon under its realized assignment alternative, subject to the saturation/interference structure of the experiment.

No treatment-on-treated or mediator causal effect is authorized by this specification.

## 7. Saturation / interference rule

Municipal saturation is a design feature and a potential source of interference.

The deposited fields `sat`, `sat_treat`, `r2` and related undocumented variables are **not admissible analysis variables** unless their provenance is independently established and frozen before execution.

A derived municipal treatment share computed deterministically from admitted `treat` values may be considered only as a documented design descriptor, not automatically as an adjustment covariate or causal control.

The primary estimand must remain interpretable without silently conditioning on post-treatment or undocumented saturation measures.

## 8. Primary estimand

The primary confirmatory estimand is:

**ITT effect of randomized infrastructure assignment on the independent polygon-level change in professional real-estate value.**

Secondary descriptive estimands, if separately frozen, may report the treatment effect on `ΔT_acc` and the relationship between `ΔT_acc` and value, but the latter is not to be interpreted causally without an additional identification strategy.

## 9. TGCV pathway analysis

`ΔT_acc` is a pre-specified structural mediator/pathway descriptor.

Execution may report:

1. ITT → `ΔT_acc`;
2. ITT → `ΔV`;
3. descriptive association `ΔT_acc` ↔ `ΔV`.

A claim that `ΔT_acc` causes `ΔV` requires separate mediator identification and is outside this frozen specification.

## 10. Statistical specification

Primary analysis:

`ΔV_i = α + β Z_i + ε_i`

where `Z_i = treat_i`.

Standard errors must account for the randomized municipal design and be frozen before execution. The default candidate is municipality-clustered inference (`cve_mun`), subject to confirmation against the documented randomization unit and number of clusters before execution.

No covariate, fixed effect, saturation variable or post-treatment variable may be added after observing the outcome.

## 11. Falsification / robustness

Before execution, the final analysis package must freeze:

- baseline balance checks;
- missing-value and endpoint-linkage rules;
- alternative legitimate aggregation rules, if any;
- municipality-clustered inference;
- a pre-specified robustness treatment of saturation/interference;
- sensitivity to the exact value transformation;
- independent reproduction procedure.

No specification search is permitted.

## 12. Required pre-execution freeze items

Execution remains blocked until the following are recorded from V1:

1. exact professional-value variable(s);
2. exact unit and monetary scale;
3. baseline/follow-up valuation mapping;
4. exact missing-value codes;
5. polygon aggregation rule;
6. treatment randomization documentation;
7. documented saturation variable definition, or a formally justified decision to proceed without it;
8. interference estimand/robustness rule;
9. final statistical script/specification hash;
10. independent executor package and reproducibility test.

## 13. Prohibited operations

- reopening the previous negative bounded causal experiment;
- selecting the value variable after seeing treatment results;
- using undocumented `sat`, `sat_treat`, `r2` as if their definitions were known;
- conditioning on post-treatment variables;
- causal mediation claims from observational `ΔT_acc`–`ΔV` association;
- outcome-informed transformation selection;
- importing external datasets without a new governance decision;
- upgrading TGCV claims from this design alone.

## 14. Execution authorization

**NOT AUTHORIZED.**

This document freezes the candidate-specific design only. A separate execution authorization is required after the five pre-execution freeze items and independent reproducibility package are completed.

## 15. Non-reopening statement

The earlier C10C-002 bounded causal experiment and its negative result remain closed and unchanged. This specification is a distinct methodological C10-C value-linkage design.
