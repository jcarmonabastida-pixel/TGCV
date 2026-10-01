# TGCV — Architectural Boundary Redesign Review v0.1

**Status:** CLOSED — REDESIGN TARGET IDENTIFIED / NOT FROZEN
**Date:** 2026-10-01
**Gate:** ARCHITECTURAL_BOUNDARY_REDESIGN_REVIEW

## 1. Purpose

Determine whether the failure of the Ω_T/E3 discriminator is caused by an overly restrictive candidate boundary rather than by absence of a potentially distinct transformation-space object.

## 2. Finding

The current Ω_T/E3 route asks for an independently observed relation added to a matched inherited A representation. That framing creates an avoidable adversarial construction:

`A = (S,T_acc) + admissible auxiliaries`

versus

`A + E3`

and then asks E3 to prove that it is not an auxiliary.

The resulting reconstruction problem is structurally biased toward A-equivalence whenever the auxiliary vocabulary is sufficiently extensible.

This does not justify declaring E3 irreducible. It indicates that E3 is the wrong unit at which to pose the architectural distinction.

## 3. Redesign target

The candidate architecture should instead be formulated at the level of a complete primary structural object:

`Ω_T,t = (U_t, ≡_t, R_t)`

with accessibility/admissibility treated as a derived or optional layer:

`A_t = F(Ω_T,t, S_t, C_t, L_t)`

where F is domain-specific and must itself be frozen before empirical evaluation.

The distinction is therefore no longer A versus A + E3. It becomes:

**A-primary:** the primary explanatory representation is `S_t + T_acc,t`, with structural relations treated as admissible auxiliaries.

**Ω-primary:** the primary explanatory representation is the transformation-space structure `Ω_T,t`; `T_acc,t` is one derived observational layer over that structure and system/context information.

## 4. Why this is a genuine boundary redesign

The redesign does not declare Ω_T to be true.

It changes the question from whether one can append an independent relation to A without A absorbing it, to whether there is an independently defined and empirically observable primary object whose canonical identity, relational structure and temporal comparison are well-defined, and from which the inherited accessibility representation can be derived when the domain permits it.

This avoids treating every structural component as an auxiliary variable by default while preserving a reconstruction test between whole representations.

## 5. Required admissibility conditions

A future Ω-primary candidate must demonstrate:

1. independently defined transformation identities;
2. frozen equivalence/canonicalisation;
3. typed relation signatures;
4. longitudinal comparability;
5. observable provenance;
6. construction without future outcome/value information;
7. a declared derivation rule for any accessibility layer;
8. representation invariance;
9. state-reducibility test;
10. falsification conditions.

The candidate must not be admitted merely because it contains more variables than A.

## 6. What this redesign resolves

It resolves the specific circularity exposed by the E3 route:

- E3 is no longer required to be an isolated extra field.
- A relation may be constitutive of Ω_T without being automatically evidence for Ω_T.
- The empirical question becomes whether the whole Ω_T representation is independently identifiable and whether its structural information is non-reducible under the frozen A representation.
- A can still be retained as a valid derived or alternative representation where it is sufficient.

## 7. What this redesign does NOT establish

This review does not establish that Ω_T is empirically observable in any particular domain.
It does not establish that Ω_T is non-reducible to A.
It does not revise the canonical Core.
It does not revise Evidence→Claim Matrix v1.44.
It does not revise RMA v3.37.
It does not authorize an experiment.

## 8. Relationship to existing formalization

The existing non-canonical `TGCV_TRANSFORMATIONAL_DYNAMICS_FORMALIZATION_PROPOSAL_v0.3` is consistent with this redesign because it already defines `Ω_T,t = (U_t, ≡_t, R_t)` as the candidate primary object and treats accessibility as a derived layer.

That proposal remains DEVELOPMENT DRAFT and is not promoted by this review.

## 9. Transition consequence

The explicit transition layer has now identified a more coherent candidate architecture:

**Inherited architecture:** `A-primary = (S,T_acc)`.

**Candidate architecture:** `Ω-primary = (U,≡_T,R)` with derived accessibility.

**Status:** candidate boundary identified; empirical admissibility unresolved.

The failed E3 route is retained as a methodological negative result against the A + isolated-E3 discriminator, not against Ω-primary architecture as such.

## 10. Next gate

**OMEGA_PRIMARY_BOUNDARY_ADMISSIBILITY_REVIEW**

This gate must determine whether the Ω-primary object can be made empirically admissible from an observation boundary without importing future outcome information and without relying on the failed isolated-E3 construction.

Only after that review may a concrete domain or experimental package be considered.

**Scientific execution: NOT AUTHORIZED.**
