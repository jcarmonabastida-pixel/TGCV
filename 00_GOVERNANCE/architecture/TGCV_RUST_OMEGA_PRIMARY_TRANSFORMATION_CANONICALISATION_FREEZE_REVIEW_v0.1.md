# TGCV — Rust Ω-Primary Transformation Canonicalisation Freeze Review v0.1

**Status:** CLOSED — OBSERVATIONAL CANONICALISATION FROZEN / SEMANTIC Ω ADMISSION STILL OPEN  
**Date:** 2026-10-02  
**Gate:** RUST_OMEGA_PRIMARY_TRANSFORMATION_CANONICALISATION_FREEZE_REVIEW

## 1. Purpose

Freeze the Rust transformation representation and canonicalisation rule for the Ω-primary candidate, using only pre-outcome structural information and without redefining accessibility as the transformation universe.

## 2. Transformation object

The candidate transformation is:

`τ = (origin_version_id, target_package_id, target_version_id)`

The semantic distinction remains:

- Rust package/crate = component;
- `package@version` = observational state/unit;
- `τ` = candidate change/substitution involving an identified target release.

Candidate membership is determined from the frozen temporal registry boundary, not from current accessibility or execution.

## 3. Canonicalisation rule

The frozen observational canonicalisation is:

`Canon_T(τ) = (origin_version_id, target_package_id, target_version_id)`

with field values taken directly from the admitted primitive structural records.

Equivalence is therefore:

`τ_a ≡_T τ_b ⇔ Canon_T(τ_a) = Canon_T(τ_b)`

This establishes **observational identity/equivalence**, not a stronger claim of semantic equivalence across transformations that happen to have different identifiers.

## 4. Permitted inputs

The canonicalisation may use only:

- origin version identifier;
- target package identifier;
- target version identifier;
- the frozen temporal rule needed to establish candidate membership.

It may use provenance needed to audit those fields back to primitive records.

It may not use:

- `T_acc`;
- Reach or `ΔReach`;
- execution/accessibility status;
- build/test success;
- downstream activity;
- outcome;
- reward, utility or value;
- future trajectory;
- any variable derived from those quantities.

## 5. Consequence for Ω

The canonicalisation establishes a reproducible observational universe:

`U_t = Canon_T(Raw_t)`

subject to the previously frozen coverage semantics.

It does **not** establish that every semantically meaningful transformation has been captured. Coverage and transformation-semantic completeness remain separate empirical questions.

## 6. Relation to R_t

Dependency declarations remain a candidate primitive source for typed structural relations.

A dependency observation may be retained as:

`r = (τ_i, τ_j, relation_type, provenance, observation_time)`

only after the relation vocabulary, directionality and transformation endpoints are constructed under the same frozen canonicalisation.

No claim is made that dependency relations constitute the complete `R_t`.

## 7. Longitudinal implication

Because the origin release is part of `τ`, a change in origin release produces a distinct observational transformation identity unless a future frozen correspondence rule explicitly establishes a cross-snapshot correspondence.

No silent identity collapse is permitted.

The longitudinal correspondence rule `κ` therefore remains a separate gate.

## 8. Circularity test

The canonicalisation passes the **governance non-circularity precondition** because no downstream accessibility, outcome or value variable enters the identity function.

This is not evidence that Ω is irreducible to the inherited representation. State-reducibility remains an empirical question.

## 9. Decision

**TRANSFORMATION REPRESENTATION:** FROZEN AS CANDIDATE.

**OBSERVATIONAL CANONICALISATION:** FROZEN.

**SEMANTIC EQUIVALENCE BEYOND OBSERVATIONAL IDENTITY:** NOT CLAIMED.

**R_t:** CANDIDATE / RELATION-SCHEMA OPEN.

**κ:** OPEN.

**Ω-PRIMARY EMPIRICAL ADMISSION:** NOT GRANTED.

No fixture or scientific execution is authorized.

Core, Evidence→Claim Matrix v1.44 and RMA v3.37 remain unchanged.

## 10. Next gate

`RUST_OMEGA_PRIMARY_RELATION_VOCABULARY_AND_ENDPOINT_CONSTRUCTION_FREEZE_REVIEW`
