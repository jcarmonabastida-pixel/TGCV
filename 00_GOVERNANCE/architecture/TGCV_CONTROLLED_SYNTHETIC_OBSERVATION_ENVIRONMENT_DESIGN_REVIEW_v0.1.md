# TGCV — Controlled Synthetic Observation Environment Design Review v0.1

**Status:** CLOSED — DESIGN GATE / NO EXPERIMENT AUTHORIZATION
**Date:** 2026-10-01
**Gate:** CONTROLLED_SYNTHETIC_OBSERVATION_ENVIRONMENT_DESIGN_REVIEW

## 1. Decision

The existing D1 synthetic world cannot be reused as the Ω_T observation environment.

D1 embeds the disputed relation as a dependency-conditioned transition mechanism. Its own A-reconstruction audit establishes that it can be absorbed as an auxiliary mechanism of A.

The controlled synthetic route remains viable only if it changes the observation architecture, not merely the parameterisation of D1.

## 2. Required design principle

A valid synthetic environment must generate an independently observable structural relation before future trajectory execution.

The candidate relation is the surviving O4 class E3 — independently measured structural compatibility.

The environment must distinguish the primitive system/world record, the measured structural relation, the inherited A representation, and the future trajectory outcome.

The structural relation must not be defined by the transition rule that produces the outcome.

## 3. Minimum environment architecture

The environment shall contain, at minimum:

- a finite set of transformation identities V;
- primitive transformation descriptors from which type identity/equivalence can be frozen ex ante;
- an independently generated structural compatibility relation E3;
- state variables sufficient to construct S_t;
- a frozen accessibility/admissibility rule producing T_acc,t;
- immutable event provenance across at least two adjacent intervals;
- a future trajectory protocol whose outcome is not used to define any structural field.

The same primitive record must be sufficient to construct both A and Ω_T.

## 4. Required separation

P → A = (S_t,T_acc,t)

and independently:

P → Ω_T = (U, ≡_T, R, π)

while enforcing that E3 measurement is operationally independent of outcome definition: it is completed before outcome observation and does not inspect outcome, reward, value or future trajectory.

## 5. Longitudinal construction

The synthetic generator must create at least two adjacent observations P_t → P_t+1 with immutable provenance.

This is necessary to make persistence, emergence, disappearance, replacement, split or merge observable rather than merely stipulated.

A single static graph is insufficient for an empirical statement about transformation-space dynamics.

## 6. A-reconstruction gate

Before any fixture freeze, the complete generated record must be subjected to:

1. direct A encoding;
2. deterministic reconstruction from A_Core;
3. reconstruction through the declared admissible auxiliary vocabulary;
4. only then assessment of Ω_T non-reconstructibility.

If E3 or Ω_T is exactly recoverable from A under the frozen rules, the environment is classified A-EQUIVALENT and rejected for discrimination.

## 7. Non-circularity gate

The generator may determine the world and structural relation ex ante, but the relation must also be represented as an observable primitive or independently inspectable measurement record.

It is insufficient to declare a hidden graph in the generator and call it an observed Ω_T object.

The audit must therefore retain the raw structural observation that generated E3, with provenance linking it to the corresponding transformation identities.

## 8. Deliberate exclusions

This review does not fix a particular domain interpretation, concrete transformation semantics, exact E3 measurement function, number of transformations, sample size, effect size, statistical model, randomisation, implementation language, workflow, or scientific execution.

Those belong to later gates only if the observation environment first passes architectural admissibility.

## 9. Decision consequence

The synthetic route is conditionally admissible as a design path, but no current synthetic package is admitted as Ω_T evidence.

D1 remains historical/diagnostic and CLOSED.

O4/E3 remains a candidate measurement class with status UNDERDETERMINED.

Core, Evidence→Claim Matrix v1.44 and RMA v3.37 remain unchanged.

## 10. Next gate

**O4_E3_PRIMITIVE_MEASUREMENT_SPECIFICATION_REVIEW**

The next controlled operation is to specify the actual primitive measurement that would make E3 independently observable. That specification must then undergo an A-reconstruction/non-circularity review before any fixture or experimental design.

**Scientific execution: NOT AUTHORIZED.**
