# TGCV — C09 Pre-Execution Domain / Identification Gate 001

**Status:** `DESIGN GATE — EXECUTION NOT AUTHORIZED`
**Date:** 2026-09-13
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories
**Parent:** `TGCV_C09_CAUSAL_DESIGN_AUDIT_001.md`

## 1. Purpose

Close the remaining pre-execution design precondition identified by the C09 causal-design audit: select a concrete admissible domain/unit and demonstrate that an accessibility-changing intervention can be identified causally without directly encoding the subsequent trajectory outcome.

This gate is a selection and identification gate only. It does not authorize execution or dataset acquisition.

## 2. Required domain properties

A candidate domain may proceed only if all of the following can be demonstrated before execution:

1. decision-time state `S0` and context `C0` are reconstructible and sealable;
2. the candidate transformation universe is explicitly bounded or reproducible;
3. `T_acc(S0,C0,L)` can be reconstructed independently of subsequent outcomes;
4. an intervention can change accessibility conditions while leaving the trajectory scoring rule unchanged;
5. the intervention does not directly select, force or encode the target trajectory;
6. a credible treatment/control or counterfactual construction exists;
7. subsequent trajectory can be observed over a fixed predeclared horizon;
8. the complete causal comparison can be independently reconstructed.

## 3. Candidate-domain screening

Each candidate domain must be scored against the following mandatory questions:

| Criterion | PASS condition | BLOCK condition |
|---|---|---|
| State freeze | `S0,C0` can be sealed before treatment | post-treatment information required |
| Accessibility observability | `T_acc` is independently reconstructible | accessibility inferred from trajectory |
| Manipulability | intervention produces verifiable `ΔT_acc` | no independent accessibility change |
| Outcome independence | intervention does not encode target trajectory | intervention directly forces outcome |
| Counterfactual | credible control/counterfactual exists | only uncontrolled before/after comparison |
| Temporal ordering | treatment precedes trajectory observation | ordering ambiguous |
| Confounding | relevant confounders identifiable and controlled/justified | unresolved alternative explanation |
| Reconstruction | independent executor can reproduce comparison | hidden or non-reconstructible inputs |
| Scope | causal conclusion can be bounded to domain/intervention/H | design requires extrapolation |

A candidate fails the gate if any mandatory criterion is BLOCK.

## 4. Identification strategy

The preferred identification order is:

1. randomized intervention, where feasible;
2. controlled assignment with demonstrable pre-treatment comparability and explicit assumptions;
3. quasi-experimental/natural-experiment design with explicit identification assumptions and falsification checks.

A simple observational association, uncontrolled before/after comparison, or retrospective classification is insufficient.

The final candidate must state the estimand, treatment assignment mechanism, counterfactual, unit of analysis, eligibility, exclusion criteria, confounder set, interference assumptions and inference procedure before execution.

## 5. Direct-effect exclusion test

The decisive test is:

> Can the intervention change `T_acc` while keeping the target trajectory mechanism, objective/scoring rule and observation procedure unchanged?

Required evidence must distinguish:

`intervention → ΔT_acc`

from any independent pathway:

`intervention → direct trajectory effect`.

If the latter cannot be excluded or separately identified, the candidate is `BLOCKED` for C09.

## 6. Accessibility manipulation test

Before execution authorization, the candidate design must specify a deterministic or independently auditable accessibility rule `L` and demonstrate, on frozen pre-treatment states or an explicitly designated design-validation fixture, that:

`T_acc,1 ≠ T_acc,0`

under the proposed intervention.

This demonstration is a design-validation requirement and is not itself evidence for C09 causal success.

## 7. Counterfactual integrity test

The candidate must establish that treatment and control differ in the accessibility condition of interest while remaining comparable under the declared identification assumptions.

The protocol must specify how it will detect:

- baseline imbalance;
- treatment-selection bias;
- temporal shocks;
- interference/spillover;
- attrition or missingness;
- changes in observation or measurement caused by treatment.

Failure of counterfactual integrity blocks execution authorization.

## 8. Required pre-execution artifact package

Before any execution authorization, the following must exist and be internally consistent:

1. selected-domain definition;
2. unit-of-analysis definition;
3. frozen accessibility rule;
4. intervention specification;
5. treatment/control or counterfactual identification specification;
6. trajectory definition and fixed horizon;
7. confounder/alternative-explanation register;
8. direct-effect exclusion argument;
9. accessibility-manipulation validation;
10. reconstruction and hashing plan;
11. explicit falsification and stop criteria.

## 9. Disqualifiers

The candidate must be rejected or returned for redesign if:

- accessibility is defined using post-treatment trajectory information;
- the intervention directly chooses or forces the target trajectory;
- `ΔT_acc` cannot be independently verified;
- treatment and counterfactual cannot be distinguished;
- causal identification depends on untestable post-hoc assumptions introduced after outcome inspection;
- the domain requires external mutation or unavailable infrastructure before design validity can be established;
- the proposed result would only establish association rather than causality.

## 10. Decision rule

`PASS` requires every mandatory criterion to pass and the complete pre-execution artifact package to be internally consistent.

`BLOCKED` applies when a mandatory causal-integrity condition cannot yet be demonstrated.

`INCONCLUSIVE` applies only where the domain is otherwise admissible but the available design evidence cannot resolve a required identification question.

No `PASS` under this gate implies a C09 scientific result. It only permits preparation of a separately audited execution protocol.

## 11. Authorization boundary

This gate authorizes neither execution nor dataset acquisition.

Even after `PASS`, the sequence remains:

`domain/identification gate → execution protocol → protocol audit → explicit execution authorization → controlled execution → independent reconstruction → claim assessment`.

## 12. Current disposition

`STATUS = OPEN — CANDIDATE DOMAIN NOT YET SELECTED`

`EXECUTION AUTHORIZATION = NONE`

`NEXT OPERATION = SELECT AND AUDIT CONCRETE C09 DOMAIN/UNIT CANDIDATE`
