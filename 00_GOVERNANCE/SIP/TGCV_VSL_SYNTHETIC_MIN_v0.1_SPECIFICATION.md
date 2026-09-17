# TGCV — VSL SYNTHETIC MINIMUM v0.1

**Status:** CANDIDATE SPECIFICATION — TO BE FROZEN BEFORE EXECUTION  
**Scope:** Synthetic demonstrator only  
**Purpose:** External, non-circular valuation specification for a bounded synthetic demonstration of the pathway from transformation accessibility to downstream outcome and Value.

---

## 1. Purpose

This specification defines a minimal artificial Value Specification Layer (VSL) that is external to the TGCV transformational core.

The VSL is intended to operationalize a synthetic Value variable without defining Value as a function of transformation accessibility.

The intended analytical chain is:

`ΔT_acc → trajectory → ΔO → ΔV*`

The VSL itself implements only:

`O → V*`

It does not construct or modify:

- `T_acc`
- `ΔT_acc`
- `Pτ`
- treatment assignment
- trajectory selection
- transformation identity
- accessibility conditions

---

## 2. Reference Entity

The reference entity is a fully synthetic system.

No real-world entity, organization, population, economic quantity, social objective, or empirical valuation is represented.

The demonstrator is therefore domain-bounded to the synthetic model.

---

## 3. Artificial Valuation Objective

The synthetic valuation objective is:

> Value is represented by the downstream operational result achieved by the synthetic system relative to its baseline.

This is an artificial methodological convention.

It is not a claim that operational performance constitutes Value in real systems.

It does not establish a universal TGCV definition of Value.

---

## 4. Outcome Variable

The independently measured outcome is:

`O = performance_final`

where `performance_final` is a scalar property of the final synthetic system state.

The outcome must be computed from downstream state/performance variables.

The outcome definition must not use:

- cardinality of `T_acc`
- membership of `T_acc`
- `ΔT_acc`
- treatment assignment
- selected transformation identity
- the fact that a transformation was made accessible
- any Value variable

The outcome therefore remains conceptually distinct from transformation accessibility.

---

## 5. Direction Rule

Higher values of `O` represent greater synthetic operational performance.

Therefore:

`O₂ > O₁ ⇒ O₂` has greater synthetic Value under this VSL.

This direction is a property of the artificial specification and carries no normative interpretation outside the synthetic domain.

---

## 6. Reference Frame

For each experimental case:

- `S₀` = frozen baseline state
- `S₁` = final state after the experimental trajectory

The outcome change is:

`ΔO = O(S₁) − O(S₀)`

The baseline is common to the relevant synthetic comparison cases.

---

## 7. Value Mapping

The VSL defines:

`V*(S) = O(S)`

and therefore:

`ΔV* = V*(S₁) − V*(S₀)`

which gives:

`ΔV* = ΔO`

This identity is intentional.

The purpose of this minimal VSL is not to demonstrate a sophisticated valuation function, but to establish a clean external valuation layer whose input is an independently defined outcome.

---

## 8. Interpretation Rule

For the synthetic demonstrator:

- `ΔV* > 0` → synthetic Value gain
- `ΔV* = 0` → synthetic Value neutrality
- `ΔV* < 0` → synthetic Value loss

These labels are model-defined classifications only.

They must not be interpreted as empirical, economic, social, organizational, or normative Value claims.

---

## 9. Provenance

The VSL is:

- artificial;
- synthetic;
- domain-bounded;
- versioned as `v0.1`;
- defined before experimental execution;
- independently hashable;
- independent of the transformation-accessibility runner;
- frozen before execution.

Any substantive change to the valuation objective, outcome definition, direction rule, measurement rule, or Value mapping creates a new VSL version.

---

## 10. Non-Circularity Rule

The VSL must not receive or inspect:

- `T_acc`;
- `ΔT_acc`;
- `Pτ`;
- treatment assignment;
- selected transformation;
- transformation-accessibility deltas;
- experimental case labels that encode the expected result;
- prior knowledge of whether accessibility changed;
- any variable derived from Value.

The VSL may receive only the independently measured outcome and the information explicitly required to calculate that outcome.

Operationally:

`state → O → V*`

is admissible.

`T_acc → V*`

is not admissible.

`ΔT_acc → V*`

is not admissible.

`selected transformation → V*`

is not admissible.

---

## 11. Domain Boundedness

The specification applies exclusively to the synthetic TGCV demonstrator.

No inference is authorized concerning:

- C09;
- KGFS;
- financial wellbeing;
- economic Value;
- industrial Value;
- monetary ROI;
- social Value;
- organizational Value;
- universal Value;
- cross-domain Value comparability.

The synthetic VSL must not be used to resolve any open substantive issue in the C09 VSL.

---

## 12. Independent Reproducibility

Given:

1. the frozen VSL;
2. the frozen final state;
3. the frozen outcome definition;
4. the frozen measurement rule;

an independent executor must obtain the same `O` and therefore the same `V*`.

Reproducibility of the VSL does not imply reproducibility of the transformation trajectory itself.

Those are separate experimental properties.

---

## 13. Required Synthetic Cases

The demonstrator should contain, at minimum, the following cases.

| Case | ΔT_acc | Selected trajectory | ΔO | ΔV* | Purpose |
|---|---:|---|---:|---:|---|
| T1 | 0 | A | 0 | 0 | Baseline |
| T2 | ≠ 0 | A | 0 | 0 | Accessibility change without Value change |
| T3 | ≠ 0 | B | > 0 | > 0 | Accessibility → trajectory → outcome → Value pathway |
| T4 | 0 | A | > 0 | > 0 | Outcome/Value change without accessibility change |
| NC1 | 0 | A | 0 | 0 | Irrelevant-control case |
| NC2 | ≠ 0 | A | 0 | 0 | Accessible-but-not-selected control |

T4 must obtain its outcome change through an exogenous synthetic state factor unrelated to transformation accessibility.

T4 must not directly manipulate `V*`.

---

## 14. Identifiability Requirement

The experimental implementation must permit an observer to distinguish at least:

1. change in transformation accessibility;
2. change in selected trajectory;
3. change in downstream outcome;
4. change in Value under the VSL.

The implementation must therefore prevent the following identity collapse:

`ΔT_acc = ΔO = ΔV*`

merely because all three variables were generated by the same function.

The accessibility mechanism and outcome mechanism must remain operationally separable.

---

## 15. Circularity Review Gate

Before execution, the specification and planned fixture must pass a dedicated circularity review.

The review must verify that:

- the VSL was defined independently of experimental outcomes;
- the outcome does not encode accessibility;
- Value is not used to select the trajectory;
- treatment assignment does not depend on Value;
- the VSL does not inspect `T_acc`;
- the runner does not feed `ΔT_acc` into the VSL;
- the outcome is measured downstream of the trajectory;
- T4 can produce `ΔV* ≠ 0` while `ΔT_acc = 0`;
- T2 can produce `ΔT_acc ≠ 0` while `ΔV* = 0`.

Failure of any of these conditions blocks execution.

---

## 16. Claim Boundary

Successful execution may support only a bounded synthetic methodological statement of the form:

> Under a frozen artificial external VSL, a synthetic intervention that changes transformation accessibility can, under specified conditions, alter a subsequent trajectory, produce a downstream outcome change, and thereby produce a corresponding Value change under the VSL.

It does not establish:

- real-world causal validity;
- a universal Value construct;
- an empirical definition of Value;
- generalizability across domains;
- validity of the C09 VSL;
- monetary or economic Value;
- superiority of any transformation;
- deployment readiness.

---

## 17. Governance Status

Until the circularity/identifiability review is completed:

`VSL_SYNTHETIC_MIN_v0.1 = CANDIDATE`

After formal freezing:

`VSL_SYNTHETIC_MIN_v0.1 = FROZEN`

Freezing the specification does not constitute experimental evidence.

No Evidence-to-Claim Matrix propagation is authorized from the specification alone.

---

## 18. Separation from C09

This synthetic VSL is intentionally independent from:

`TGCV_MT5_VSL_C09_SPECIFICATION_v0.1`

No unresolved C09 field is imported into this specification.

In particular, the synthetic VSL does not depend upon:

- financial wellbeing;
- household-level outcomes;
- KGFS objectives;
- C09 outcome selection;
- C09 missing-data rules;
- C09 aggregation;
- C09 source interpretation;
- C09 treatment-effect estimates.

The purpose of this separation is methodological isolation: the synthetic demonstrator tests the architecture of an external VSL without requiring resolution of the substantive C09 valuation problem.

---

## 19. Version Rule

`VSL_SYNTHETIC_MIN_v0.1` is immutable once frozen.

Any change to:

- objective;
- outcome;
- direction;
- reference frame;
- measurement;
- Value mapping;
- non-circularity constraints;
- domain;
- reproducibility rule;

requires a new version.

No silent modification is permitted.
