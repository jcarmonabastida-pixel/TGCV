# TGCV — Ω-Primary Boundary Admissibility Review v0.1

**Status:** CLOSED — CONDITIONALLY ADMISSIBLE AS ARCHITECTURAL CANDIDATE / NOT EMPIRICALLY ADMITTED
**Date:** 2026-10-01
**Gate:** OMEGA_PRIMARY_BOUNDARY_ADMISSIBILITY_REVIEW

## 1. Question

Can the redesigned Ω-primary object be specified at an observation boundary without relying on the failed isolated-E3 discriminator or importing future outcome information?

## 2. Result

**YES at the formal admissibility level; NOT YET at the empirical identification level.**

The candidate primary object Ω_T,t = (U_t, ≡_t, R_t) has a coherent domain-independent specification in the existing non-canonical formalization draft. It defines transformation identity, typed relations, snapshot comparability, structural change, representation invariance, a structural null, state-reducibility, and explicit failure conditions.

Crucially, Ω-primary no longer requires an isolated relation to be appended to A.

## 3. Information-boundary test

The candidate can be constructed without future trajectory, outcome, value or reward information in principle, provided the domain-specific observation rule supplies U, identity/equivalence and R before those variables are observed.

The information firewall is therefore a design requirement, not yet an empirical result.

## 4. Identifiability bottlenecks

Empirical admissibility remains unresolved at four points:

1. Transformation identity: a real domain must expose a reproducible U_t and frozen ≡_t.
2. Relation observation: R_t must be observable rather than hidden in the generator or inferred from outcomes.
3. Longitudinal correspondence: adjacent Ω_T snapshots need a frozen common universe or correspondence κ.
4. State reducibility: structural change must survive the pre-specified state-only comparison class C_S.

These are the actual empirical gates for Ω-primary.

## 5. Consequence for E3

The previous E3 route is not carried forward as a mandatory primitive.

E3 remains a possible domain-specific relation type if it satisfies the Ω-primary contract, but it no longer has special architectural status.

This closes the failed A + isolated-E3 route without discarding the broader Ω-primary hypothesis.

## 6. Minimum admissibility package

Before any experiment, a domain-specific candidate must freeze:

- U_t construction;
- ≡_t canonicalisation;
- complete R_t relation signatures;
- κ/common-universe rule;
- Γ_t comparison;
- representation perturbation class;
- structural null;
- state-only comparison class C_S;
- information firewall;
- missingness/uncertainty rules;
- falsification criteria;
- data sufficiency.

A package failing any of these remains NON-ADMISSIBLE.

## 7. Architectural status

**Inherited:** A-primary = (S,T_acc).

**Candidate:** Ω-primary = (U,≡_T,R); accessibility is optional/derived.

**Status:** Ω-primary is now a coherent architectural candidate, but empirical identification remains open.

This is a governance/design result, not evidence for TSDI.

## 8. Governance consequence

- Core: unchanged.
- Evidence→Claim Matrix v1.44: unchanged.
- RMA v3.37: unchanged.
- Existing closed experiments: unchanged.
- D1: historical/closed.
- E3 isolated discriminator: closed.
- No fixture frozen.
- No scientific execution authorized.

## 9. Next gate

**OMEGA_PRIMARY_DOMAIN_INSTANTIABILITY_REVIEW**

The next review must ask a narrower question:

> Is there a concrete domain in which U_t, ≡_t, R_t, longitudinal correspondence, and the information firewall can all be instantiated from observable records without using outcomes to define the structure?

Only after that gate should a domain-specific operationalisation be drafted.

**Scientific execution: NOT AUTHORIZED.**
