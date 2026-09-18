# TGCV — VSL Experimental Protocol Design Gate 001

**Date:** 2026-09-19  
**Status:** DESIGN GATE — NOT FROZEN  
**Preconditions:** VSL-SPEC-01 v0.1 FROZEN; VSL-EXP-01 v0.1 FROZEN; Domain-Specific VSL A and B FROZEN

## 1. Purpose

Define the minimum architecture required for a prospective TGCV experiment linking transformation-space accessibility to a pre-frozen domain Value layer.

This gate does not authorize execution and does not select between the two frozen valuation domains.

## 2. Frozen causal/analytical separation

The experiment must preserve:

`TGCV mechanism/intervention → (S_t,C_t) → S_{t+1},C_{t+1} → ΔT_acc → trajectory → Outcome → V*`

The domain-specific VSL owns only the final valuation mapping: `Outcome → V*`.

The experiment must not redefine V* from observed TGCV results.

## 3. Required experimental objects

Before execution, the protocol must freeze:

- baseline system state `S_0`;
- context/control variables `C_0`;
- accessibility representation `T_acc,0`;
- intervention/treatment definition;
- admissibility predicate used to construct `T_acc`;
- post-intervention state/context;
- `T_acc,1` and `ΔT_acc` construction;
- trajectory-selection/execution rule;
- outcome `O` definition from the selected trajectory/final state;
- frozen domain-specific VSL (A or B);
- reference/counterfactual;
- randomization or assignment rule, if applicable;
- null/control condition;
- stopping rule;
- missingness/uncertainty handling;
- integrity hashes and environment;
- independent reconstruction requirements.

## 4. Essential anti-circularity gates

### G1 — Value-before-outcome
The domain-specific VSL must be immutable before outcome data are inspected.

### G2 — Outcome independent of V*
The experimental Outcome must be defined independently of the Value mapping.

### G3 — Accessibility independent of Value
`T_acc` and `ΔT_acc` must be constructed without using Value or the observed Outcome.

### G4 — Reference-before-results
The reference/counterfactual must be frozen before treatment results are inspected.

### G5 — Trajectory rule before results
Trajectory selection/execution must be frozen before observing treatment outcomes.

### G6 — No post-hoc direction
Directionality is inherited from the frozen VSL and cannot be changed after results.

### G7 — Independent reconstruction
Where the causal claim requires reconstruction, an independent executor must reconstruct the frozen objects without access to prior interpretations.

## 5. Candidate-specific branches

### Branch A — Built assets / infrastructure LCC

Use the frozen A VSL. The experimental domain must define a concrete asset/decision unit, a pre-frozen alternative/reference, an agreed LCC analysis period, and all included cost categories before execution.

### Branch B — Petroleum/petrochemical/natural-gas LCC

Use the frozen B VSL. The experimental domain must define a concrete facility/option comparison, pre-frozen competing option/reference, life-cycle analysis period, and all included economic variables before execution.

## 6. Minimum evidence outputs

The experiment must produce enough evidence to independently reconstruct:

`S_0, C_0, T_acc,0, intervention, S_1, C_1, T_acc,1, ΔT_acc, trajectory, O, V*`

plus the frozen reference/counterfactual and control/null condition.

## 7. Claim boundary

A successful experiment may provide evidence about the relationship between accessibility changes, trajectories, outcomes and the frozen domain Value construct.

It does not automatically establish universal Value, cross-domain Value comparability, causal Value effects unless the design identifies them, predictive validity, or a universal `V = f(T_acc)` law.

## 8. Freeze gate

The protocol cannot be frozen until the following are specified:

1. exact domain branch (A or B);
2. experimental unit and population/context;
3. intervention and admissibility predicate;
4. baseline/reference and counterfactual;
5. trajectory-selection rule;
6. Outcome construction;
7. frozen VSL reference;
8. assignment/randomization strategy where applicable;
9. null/control;
10. metrics and decision thresholds;
11. missingness/uncertainty;
12. independent reconstruction package;
13. environment and integrity hashes;
14. stopping and failure rules.

## 9. Governance

No Core, RMA, C09 or Evidence-to-Claim Matrix change is made by this design gate.

## 10. Next operation

Construct the full experimental protocol for each frozen VSL branch, then perform a protocol-integrity audit before authorizing execution.