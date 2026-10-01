# TGCV — D1 Architectural Discriminator Specification v0.1

**Status:** GOVERNANCE SPECIFICATION / NOT YET AN EXPERIMENT  
**Date:** 2026-10-01  
**Decision:** ARCH-DISC-001  
**Authorization:** NONE

## 1. Objective

Operationalize D1 without yet specifying a scientific fixture, sample size, execution workflow or execution authorization.

The architectural question is:

> Can two cases with the same accessible transformation set be distinguishable in a pre-specified future transformation outcome solely because the relational organisation of that same set differs?

## 2. Common representation

Each matched case must expose the same canonical state variables:

`S_t, C_t, L_t, T_acc,t`

The accessible transformation set is an explicit finite object:

`T_acc,t = {τ_1, ..., τ_n}`

Equality for D1 means **extensional equality**: same transformation identities and same accessibility status at the frozen observation point.

No downstream outcome may be used to establish membership.

## 3. Structural representation

The candidate TSDI-specific object is:

`G_τ = (T_acc, E_τ)`

where `E_τ` is a pre-specified relation/dependency edge set over the transformations.

For D1, matched cases must satisfy:

`T_acc^(1) = T_acc^(2)`

and:

`E_τ^(1) ≠ E_τ^(2)`

The edge semantics must be defined independently of the future outcome. Examples include pre-existing transformation dependency, prerequisite, compatibility or transition relation, provided the chosen semantics are frozen before observation.

## 4. Critical non-degeneracy condition

The two `G_τ` structures must differ in a way that is **not recoverable from information already included in A**.

If `E_τ` can be deterministically reconstructed from `S_t`, `C_t`, `L_t` and `T_acc,t` under the inherited representation, then D1 does not discriminate architecture.

The experimental specification must therefore include an explicit **A-reconstruction test**:

`E_hat_A = f_A(S_t,C_t,L_t,T_acc,t)`

and require that the proposed B structural contrast is not simply a relabelling of an existing inherited variable.

## 5. Future observable

The future observable is provisionally defined as an **independent transformation trajectory event** after the frozen initial condition.

It must be:
- observed after `G_τ` is frozen;
- independent of the procedure used to construct `G_τ`;
- identical in definition for all matched cases;
- measurable without referring to TSDI, architecture A, or architecture B.

The exact event definition remains an experimental-design item and is deliberately not frozen here.

## 6. Prediction contrast

### A

A may predict the future observable only from the information admitted by the inherited representation:

`P_A(Y_future | S_t,C_t,L_t,T_acc,t,H_A)`

where `H_A` contains only pre-specified inherited auxiliary variables.

### B

B may additionally use the frozen structural object:

`P_B(Y_future | S_t,C_t,L_t,T_acc,t,G_τ,H_B)`

No post-hoc predictors are allowed.

## 7. Discrimination criterion

D1 can provide architectural evidence only if:

1. `T_acc` equality is independently verified;
2. `G_τ` differs as pre-specified;
3. the future observable is independently defined;
4. the outcome difference is reproducible;
5. the difference is associated with the pre-specified `G_τ` contrast;
6. the effect cannot be reproduced by an equivalent A representation without encoding the disputed structural object;
7. the result survives a materially distinct operationalisation.

Failure of any requirement prevents architectural inference.

## 8. Outcomes

**FOR-B / AGAINST-A (bounded):** conditions 1–7 satisfied and the structural contrast provides reproducible predictive information unavailable to A without equivalent reconstruction.

**AGAINST-B (bounded):** a preregistered B mechanism predicts a discriminating effect, but the controlled test fails to produce it under conditions where the mechanism is otherwise adequately instantiated.

**NON-DISCRIMINATING:** outcomes are compatible with both representations or A can reproduce the result without the disputed structural object.

**INVALID:** equality of `T_acc`, structural contrast, independence of the outcome, or pre-registration cannot be demonstrated.

## 9. Explicit exclusions

This specification does not authorize:
- choosing a particular domain;
- generating a fixture;
- choosing N or power;
- selecting a model;
- executing a workflow;
- upgrading any TGCV claim;
- changing the Core;
- changing Matrix v1.44;
- asserting Transformational Intelligence.

## 10. Next gate

The next governance task is to select and freeze the **semantics of `E_τ`** and the independent future observable. Only after those are frozen should an experimental package be drafted.
