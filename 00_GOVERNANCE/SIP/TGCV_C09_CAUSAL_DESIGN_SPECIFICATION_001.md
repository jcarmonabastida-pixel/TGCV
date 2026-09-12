# TGCV — C09 Causal Design Specification 001

**Status:** `DESIGN / CONTROLLED / EXECUTION NOT AUTHORIZED`
**Date:** 2026-09-12
**Claim under test:** C09 — Accessibility changes causally affect subsequent trajectories
**Parent priority gate:** `TGCV_C09_CAUSAL_DESIGN_PRIORITY_GATE_001.md`

## 1. Objective

Determine whether a change in accessibility conditions, independently defined at decision time, has a causal effect on subsequent trajectory rather than merely an association with it.

The design tests the segment:

`exogenous accessibility intervention → ΔT_acc → subsequent trajectory`

It does not test value, industrial utility, explanatory superiority, originality or transversal validity.

## 2. Causal estimand

For an admissible unit `u` at decision time `t0`, define:

- `S0`: frozen pre-treatment structural state;
- `C0`: frozen pre-treatment context;
- `L`: frozen accessibility semantics;
- `A0 = T_acc(S0,C0,L)`: pre-treatment accessible transformation structure;
- `Z`: exogenous treatment/intervention affecting accessibility conditions;
- `A1(Z)`: post-intervention accessible transformation structure;
- `Y(Z)`: independently defined subsequent-trajectory outcome over fixed horizon `H`.

Primary estimand:

`τ = E[Y(1) − Y(0)]`

where treatment `Z=1` changes accessibility conditions and `Z=0` is the counterfactual/control condition, with identification strategy explicitly justified before execution.

The causal estimand is not defined as a change in execution success or immediate outcome. The trajectory variable must be independently specified.

## 3. Unit and temporal boundary

The unit is one decision-time case with a uniquely reconstructible `S0,C0` and candidate transformation universe. Treatment assignment must occur after the pre-treatment state/context and candidate accessibility rule are frozen and before post-treatment trajectory observation.

No post-treatment event may alter the classification of `A0`, treatment assignment, or eligibility.

## 4. Accessibility intervention

The treatment must alter accessibility conditions while avoiding direct encoding of the target trajectory. Acceptable intervention classes include a controlled change to an enabling condition that changes which transformations satisfy the frozen accessibility predicate, while leaving the structural target and trajectory scoring rule unchanged.

The intervention is inadmissible if it directly selects, executes, or otherwise forces the target trajectory outcome.

The design must demonstrate ex ante that:

`T_acc,1 ≠ T_acc,0`

for treated units, or classify the treatment as a failed accessibility manipulation.

## 5. Control / counterfactual identification

Preferred design hierarchy:

1. randomized assignment where feasible;
2. controlled matched assignment with pre-treatment equivalence and a documented identification argument;
3. natural-experiment/quasi-experimental assignment with explicit assumptions and falsification checks.

A before/after comparison without a credible counterfactual is insufficient for C09.

The design must record treatment assignment mechanism, eligibility, exclusion criteria, baseline balance, interference assumptions, attrition and deviations from protocol.

## 6. Trajectory outcome

`Y` must be fixed before treatment outcomes are inspected and must describe subsequent trajectory, not merely immediate execution/result.

Minimum acceptable trajectory representation is an ordered structure of post-decision transformation/state transitions over a predeclared horizon. Candidate metrics may include trajectory identity, transition sequence divergence, continuation/branching difference or a prespecified distance between trajectory structures.

If H=1 is used, the result must be explicitly classified as one-step downstream trajectory evidence and must not be generalized to arbitrary H>1 trajectory claims.

## 7. Confounding and alternative explanations

The protocol must identify variables that can affect both accessibility and trajectory. Baseline structural state, context, resource conditions, workload/demand, policy/rule state and assignment mechanism must be considered where applicable.

A treatment effect is not attributable to accessibility if the intervention independently changes the trajectory mechanism itself, execution capacity, objective function or observation process. Such cases are classified as design failure or inconclusive unless the direct pathway is separately identified and excluded.

## 8. Information firewall

The following are frozen before outcome observation:

- candidate universe;
- `S0` and `C0`;
- accessibility semantics `L`;
- treatment assignment/intervention definition;
- trajectory definition and horizon;
- primary estimand;
- exclusion criteria;
- confounder set;
- stopping and falsification criteria.

Future releases, observed outcomes, later activity and value results cannot be used to define pre-treatment accessibility or eligibility.

## 9. Falsification / inconclusive criteria

The operation cannot support C09 if any of the following occurs:

- accessibility manipulation does not produce an independently verified change in `T_acc`;
- treatment assignment lacks a defensible counterfactual identification strategy;
- trajectory cannot be reconstructed independently of treatment/outcome;
- post-treatment information leaks into treatment or accessibility classification;
- direct intervention effects cannot be separated from the accessibility pathway;
- baseline imbalance or confounding invalidates the identification assumptions;
- missingness/attrition prevents valid estimation;
- results require post hoc changes to the estimand, horizon, metric or eligibility rule.

A null effect is a legitimate scientific result and must not trigger redesign toward a positive result.

## 10. Evidence required for a PASS

A C09 bounded causal PASS requires, at minimum:

1. successful ex-ante freeze and integrity verification;
2. independently verified accessibility change attributable to treatment;
3. credible treatment/control or counterfactual identification;
4. independently reconstructed subsequent trajectories;
5. prespecified causal estimate with uncertainty/appropriate inference;
6. falsification and alternative-explanation checks passed;
7. reproducible reconstruction from frozen inputs;
8. explicit scope limits and no contamination by value/outcome interpretation beyond the defined trajectory endpoint.

## 11. Claim boundary

Even a bounded C09 PASS would establish only the tested causal relation under the specified domain, intervention, population, horizon and identification assumptions. It would not establish universality, cross-domain validity, predictive superiority, value creation or industrial utility.

## 12. Authorization boundary

This artifact is a design specification only.

`EXECUTION AUTHORIZATION = NONE`

No dataset acquisition, external execution, AWS mutation, SWIM rerun or RUST-DYN-2 rerun is authorized by this document.

## 13. Audit disposition

Against `TGCV_C09_CAUSAL_DESIGN_PRIORITY_GATE_001.md`, requirements are satisfied at design level: causal question explicit; state/context and accessibility rule frozen conceptually; intervention/control boundary specified; trajectory fixed ex ante; information firewall defined; falsifiers and stop conditions defined; execution and claim-upgrade boundaries preserved.

Remaining pre-execution gate: select a concrete admissible domain/unit and demonstrate that the proposed intervention can change accessibility without directly encoding the trajectory outcome. Until that is independently established, C09 remains `OPEN — DESIGN PRECONDITION NOT YET CLOSED`.

**Decision:** `C09 CAUSAL DESIGN = PASS — CONTROLLED DESIGN SPECIFICATION; PRE-EXECUTION DOMAIN/IDENTIFICATION GATE OPEN`.
