# TGCV — C10-C Empirical Design Gate 001

**Status:** FROZEN — DESIGN GATE ONLY; NO EMPIRICAL EXECUTION AUTHORIZED
**Date:** 2026-09-15
**Claim:** C10 — causal `ΔT_acc → ΔV`
**Precondition:** C10-A/B sufficient for C10-C design; C10-C empirical gap open

## 1. Purpose

Freeze the minimum admissible causal design for C10-C before any new dataset/case search, acquisition, inspection, reconstruction or causal estimation.

C10-C targets the bounded causal contribution of an identified change in accessibility to an independently defined value endpoint. It does not test the already-established C09 question of whether `ΔT_acc` can affect subsequent trajectories.

## 2. Causal target

The target is not the association `ΔT_acc ↔ ΔV`, nor the generic proposition that more accessible transformations are beneficial.

The target is:

`Effect(ΔT_acc on V | admissible counterfactual, specified context)`

with preferred causal ordering:

`Z → ΔS → ΔT_acc → ΔReach/ΔTrajectory → Outcome → V`

The sign is unrestricted: positive, null, negative and heterogeneous effects are all admissible outcomes.

## 3. C10-C1 — Value estimand and endpoint

A candidate must define, before causal estimation:

- an explicit value endpoint `V`;
- its unit of observation;
- measurement scale and units;
- aggregation rule;
- evaluation horizon;
- value context/objectives/preferences/constraints;
- the causal estimand, including treatment contrast and target population.

`V` must be observable or deterministically reproducible and must be defined independently of `T_acc`, treatment success and downstream observed results.

If value is multidimensional, the primary estimand and any secondary dimensions must be frozen before estimation. A post-treatment composite selected for statistical advantage is inadmissible.

## 4. C10-C2 — Accessibility representation

The candidate must support independent reconstruction of:

`T_acc,0 = F(S_0,C_0,L)`

`T_acc,1 = F(S_1,C_1,L)`

`ΔT_acc = T_acc,1 − T_acc,0`

within a bounded, explicit and minimum-sufficient `U_τ* ⊂ U_τ`.

`U_τ*` must be:

1. observable or deterministically reconstructible;
2. defined before access to value results;
3. structurally grounded;
4. sufficiently rich for non-trivial `ΔT_acc`;
5. small enough for explicit predicate reconstruction;
6. independently reproducible.

No outcome, value, treatment effect or downstream success measure may enter `P_τ`.

## 5. C10-C3 — Intervention and identification

A candidate must provide a credible source of variation `Z` that changes accessibility or the structural conditions determining accessibility.

Preferred hierarchy:

1. randomized assignment;
2. credible quasi-experimental assignment with auditable assumptions;
3. other explicitly justified identification strategy only where confounding/selection can be addressed defensibly.

Pure cross-sectional association is insufficient.

The identification strategy, treatment definition, unit, timing, clustering and principal assumptions must be specified before estimation.

## 6. C10-C4 — Counterfactual

The design must identify an admissible counterfactual value for the relevant unit under the alternative accessibility condition.

Acceptable counterfactual construction must be justified by the identification design. Before/after comparison without a credible counterfactual is insufficient.

Where interference or spillovers are plausible, the estimand must explicitly address them or the candidate must be bounded accordingly.

## 7. C10-C5 — Downstream separation

The design must distinguish the contribution of `ΔT_acc` from:

- transformation selection;
- execution quality/intensity;
- realized transformation frequency;
- Reach;
- trajectory/sequence;
- external conditions;
- simultaneous interventions;
- other competing mechanisms.

Where mediation is analysed, the preferred structure is:

`ΔT_acc → ΔReach → ΔTrajectory → Outcome → V`.

C09 evidence may serve as upstream evidence for the accessibility-to-trajectory boundary but cannot be reused as evidence of causal value attribution.

## 8. C10-C6 — Value attribution boundary

The analysis must distinguish at minimum:

- total intervention effect on `V`;
- the component attributable to changed accessibility;
- mediation through Reach/Trajectory/Outcome where identifiable;
- contextual modification;
- competing causal explanations.

If the design cannot isolate the accessibility contribution, it may report an intervention effect but does not close C10-C.

## 9. Inclusion rules

A candidate enters C10-C design admission only if all are potentially satisfiable from its pre-estimation information:

- exact source identity and provenance;
- independent value endpoint;
- reconstructible baseline/follow-up structural state;
- explicit bounded `U_τ*` and deterministic `P_τ` rules;
- treatment/state separation;
- credible causal identification;
- admissible counterfactual;
- downstream outcome/value linkage;
- interference/spillover assessment;
- reproducibility by independent execution.

## 10. Exclusion rules

A candidate is excluded or stopped if any required condition depends on:

- post-treatment value information to define `T_acc`;
- outcome-informed selection of transformations;
- retrospective threshold selection;
- latent accessibility fitted to `V`;
- arbitrary narrowing of `U_τ` to improve the result;
- cross-sectional association presented as causal identification;
- value inferred retrospectively from an intervention outcome;
- missing provenance that requires guessing;
- irreducible confounding without a defensible identification strategy;
- absence of an admissible counterfactual;
- unresolved interference that invalidates the stated estimand.

## 11. Falsification and robustness requirements

Before causal closure, the design must pre-specify applicable tests for:

- baseline balance / pre-trends where relevant;
- placebo or falsification outcomes where justified;
- alternative admissible specifications;
- sensitivity to clustering and dependence structure;
- attrition/missingness;
- interference/spillovers;
- measurement error in structural state and value;
- heterogeneous effects where substantively required.

These tests must not be selected after observing the preferred value result.

## 12. Minimum evidence and provenance package

Before empirical execution, the candidate package must contain:

1. frozen source manifest and hashes;
2. provenance chain `source → variable → definition → coding → admissible values → missingness → unit → time → level`;
3. structural state dictionary;
4. treatment/intervention dictionary;
5. frozen `U_τ*` and transformation identifiers;
6. deterministic `P_τ` definitions;
7. value endpoint specification;
8. causal estimand and identification assumptions;
9. counterfactual definition;
10. interference/spillover assessment;
11. pre-specified falsification/robustness plan;
12. independent-execution reproducibility requirements;
13. explicit stop conditions.

## 13. Closure criterion

C10-C can close only when a real-world bounded study provides:

- reproducible `T_acc,0`, `T_acc,1` and `ΔT_acc`;
- credible causal variation in accessibility;
- an independently defined value endpoint;
- an admissible counterfactual;
- separation of accessibility from major competing mechanisms;
- reproducible downstream outcome/value data;
- a causal estimate with uncertainty and auditable assumptions;
- bounded interpretation.

A null, negative or heterogeneous estimate is scientifically admissible and must update the claim accordingly.

## 14. Governance boundary

This gate freezes the design only.

It does **not** authorize:

- dataset search;
- dataset acquisition;
- data download;
- data inspection;
- candidate admission;
- reconstruction;
- causal estimation;
- claim upgrade.

Those actions require a subsequent explicit C10-C candidate discovery/data-level authorization derived from this frozen gate.

## 15. Relationship to C10C-002

C10C-002 remains closed with its previously recorded negative bounded causal result. This gate does not reopen, reinterpret or rerun that experiment.

The methodological lesson on minimum-sufficient bounded `U_τ*` remains binding for future candidates and prevents both unnecessary semantic breadth and post-hoc value-driven narrowing.

## 16. Decision

**C10-C EMPIRICAL DESIGN GATE: FROZEN — PASS FOR DESIGN, NO EXECUTION AUTHORIZATION.**

Next governed operation: derive the candidate-discovery/data-level admission specification from this frozen causal design, then evaluate future candidates against it before any acquisition or execution.
