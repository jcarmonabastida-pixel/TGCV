# TGCV — D1 Structural Relation & Future Observable Selection v0.1

**Status:** GOVERNANCE SPECIFICATION / NO EXPERIMENT AUTHORIZATION  
**Date:** 2026-10-01  
**Decision:** ARCH-DISC-001

## 1. Decision

For D1, define E_tau as a **precondition/dependency relation among transformations** and define the future observable as an **independent successful two-step transformation trajectory event**.

This is a formalization choice for the discriminator, not evidence that the TSDI hypothesis is true.

## 2. Semantics of E_tau

For transformations tau_i, tau_j in T_acc:

`(tau_i, tau_j) in E_tau`

means:

> execution of tau_i establishes or preserves a condition required for tau_j to be executable in the subsequent step under the frozen transformation protocol.

The relation is directional.

### Requirements

- E_tau is frozen before future outcomes are observed.
- The relation is defined from transformation semantics/preconditions, not from observed success rates.
- An edge is not inferred merely because tau_i and tau_j happened to co-occur.
- The same transformation identities and the same T_acc membership are retained across matched cases.
- Only the pre-specified dependency relation differs between matched conditions.

## 3. Why dependency rather than generic similarity

A generic similarity or adjacency measure could be reconstructed in many ways from transformation descriptions and would risk becoming an arbitrary extra feature.

A precondition/dependency relation has a direct operational interpretation: it specifies whether one transformation changes the conditions under which another transformation can subsequently occur.

This makes it possible to hold instantaneous accessibility constant while varying the organisation governing subsequent trajectories.

## 4. Future observable Y

The primary future observable is:

**Y = successful execution of a specified two-step transformation trajectory tau_i -> tau_j after the frozen initial state.**

Y is binary at the primary level:

- Y=1: the prescribed two-step trajectory is successfully completed;
- Y=0: it is not successfully completed within the frozen protocol.

The trajectory and success criterion must be specified independently of the A/B comparison.

## 5. Critical independence

The future observable must not be used to construct E_tau.

In particular:

- success/failure of tau_i -> tau_j cannot define whether (tau_i,tau_j) belongs to E_tau;
- the outcome cannot alter T_acc;
- no outcome-dependent edge pruning is permitted.

## 6. D1 contrast

Matched cases must satisfy:

`T_acc^(1) = T_acc^(2)`

while:

`E_tau^(1) != E_tau^(2)`

The future trajectory outcome is then measured under the same outcome definition.

The intended architectural contrast is:

- **A:** the two cases are equivalent with respect to the common inherited representation, unless A contains an independently pre-specified variable that distinguishes them.
- **B:** the dependency structure predicts a difference in subsequent trajectory feasibility.

## 7. A-reconstruction safeguard

Before scientific preflight, the package must test whether the proposed E_tau can be reconstructed from:

`S_t, C_t, L_t, T_acc,t`

and any declared inherited auxiliary variables.

If reconstruction is exact, or if the structural contrast is merely a deterministic relabelling of inherited information, the D1 test is declared **NON-DISCRIMINATING** before execution.

## 8. What remains deliberately unfrozen

This document does **not** select:

- a domain;
- concrete transformation identities;
- a fixture;
- sample size;
- effect size;
- statistical model;
- execution workflow;
- scientific authorization.

## 9. Next gate

The next governance task is to define the **minimal controlled synthetic world** in which the same T_acc can coexist with two distinct, pre-specified dependency structures and in which the two-step future trajectory can be observed without circularity.

No experiment is authorized by this document.
