# TGCV — MT5 Value Interpretation Layer Candidate 001

**Date:** 2026-09-17  
**Status:** `CURRENT_INDEPENDENT_ANALYSIS`  
**Scope:** Value track following MT5-06

## 1. Objective

Identify the minimum explicit information required to interpret an independently measured downstream outcome as a candidate TGCV Value endpoint, without defining Value as a universal scalar and without contaminating `T_acc`.

## 2. Separation principle

The analysis separates three layers:

`Outcome O` → `Value Interpretation Layer I_V` → `Value candidate V*`

Where:

- `O` is an empirically measured downstream outcome;
- `I_V` specifies why, for whom, and under what declared reference frame the outcome is value-relevant;
- `V*` is the resulting domain-bounded Value candidate.

The interpretation layer is not allowed to alter the construction of `Pτ`, `T_acc`, or `ΔT_acc`.

## 3. Minimum information required in I_V

### IV1 — Reference entity
Identify the system, actor, beneficiary, organization, or other entity relative to which value is assessed.

### IV2 — Valuation objective
State what improvement, preservation, avoidance, capability, welfare condition, utility, or other value-relevant objective the endpoint represents.

### IV3 — Direction of valuation
Specify which changes count as value-increasing, decreasing, or neutral under the declared objective.

### IV4 — Outcome mapping
Specify the explicit mapping from the measured outcome variables to the value-relevant construct. The mapping must not be inferred merely from correlation or improvement.

### IV5 — Reference frame
Declare relevant constraints, horizon, population/actor scope, and comparison frame required to interpret the outcome as value.

### IV6 — Measurement rule
Specify the reproducible endpoint, index, contrast, or estimand used to represent the value-relevant construct.

### IV7 — Non-circularity
The interpretation must not use TGCV's own conclusion, `ΔT_acc`, treatment assignment, or the observed causal pathway as part of the value definition.

### IV8 — Domain-boundedness
The interpretation may be domain-specific. Domain-specific semantics are not promoted to TGCV primitives unless independently shown to be transversal.

## 4. What this layer does NOT require

The candidate layer does **not** require:

- a universal scalar value metric;
- a universal weighting function;
- identical substantive endpoints across domains;
- a causal effect of `ΔT_acc`;
- monetary valuation;
- a normative theory selected as TGCV's universal ontology.

## 5. Application to existing candidates

| Case | Outcome `O` | Required interpretation | Current status |
|---|---|---|---|
| KGFS/C09 | poverty/well-being measures | beneficiary/reference + welfare objective + direction + measurement rule | `CANDIDATE-LAYER-DEFINED, NOT EMPIRICALLY OPERATIONALIZED` |
| IT-G1 | utility measures | system/user reference + utility objective + direction + reproducible utility metric | `PARTIAL; REPRODUCIBILITY GAP REMAINS` |
| C10C002/MT5 | downstream structural/socioeconomic outcomes | explicit actor/reference + objective + value mapping + estimand | `CANDIDATE-LAYER-DEFINED, NOT EMPIRICALLY OPERATIONALIZED` |
| SWIM | no sufficiently explicit Value outcome | interpretation layer cannot be instantiated | `NO-CANDIDATE` |

## 6. Key finding

A transversal **interpretation architecture** is more defensible at this stage than a transversal substantive definition of Value.

The candidate architecture is:

`O` + `Reference` + `Objective` + `Direction` + `Mapping` + `Reference frame` + `Measurement rule` → `V*`

This is a methodological construction rule, not evidence that the resulting `V*` is universally valid or that different domains share one substantive value quantity.

## 7. Remaining empirical requirement

The next empirical question is whether one existing case can instantiate all mandatory interpretation fields with independently auditable evidence, while preserving the already established separation from `T_acc` and without importing an unsupported universal normative assumption.

Passing this would produce a **domain-bounded operational Value candidate**, not yet a universal TGCV Value definition.

## 8. Governance disposition

**MT5-07: CLOSED — VALUE INTERPRETATION LAYER CANDIDATE IDENTIFIED.**

No Core modification.  
No RMA modification.  
No Evidence→Claim Matrix upgrade.  
No causal claim `ΔT_acc → ΔV`.  
M9 remains open.

## 9. Next authorized movement

Select the strongest existing candidate case and run an **end-to-end Value Interpretation Instantiation Test**, using only already frozen evidence and explicitly recording any missing interpretation field. No new case discovery is required before this test.
