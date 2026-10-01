# TGCV — D1 Minimal Controlled Synthetic World v0.1

**Status:** GOVERNANCE DESIGN SPECIFICATION / NO EXPERIMENT AUTHORIZATION  
**Date:** 2026-10-01  
**Decision:** ARCH-DISC-001

## 1. Purpose

Define the smallest synthetic world capable of instantiating D1: identical instantaneous accessible transformation sets with different pre-specified dependency structures, followed by an independently observed two-step trajectory outcome.

This document defines the world structure only. It does not define N, power, statistical model, fixture seed, workflow or execution authorization.

## 2. Primitive world

The world contains a finite set of transformation identities:

`T = {tau_1, tau_2, tau_3, tau_4}`

Each transformation has a deterministic precondition and a deterministic state transition.

The system state contains only variables necessary to evaluate those preconditions and transitions.

## 3. Matched initial conditions

Two matched worlds, W_A and W_B, begin from states that are equivalent on every variable admitted to the inherited representation:

`S_0, C_0, L_0, T_acc,0`

Both worlds must have exactly the same:

`T_acc,0 = {tau_1, tau_2, tau_3, tau_4}`

Thus every transformation identity is initially accessible in both worlds.

## 4. Structural contrast

The worlds differ only in the pre-specified dependency relation governing subsequent execution.

Example controlled structures:

`E_tau^A = {(tau_1,tau_2), (tau_3,tau_4)}`

`E_tau^B = {(tau_1,tau_3), (tau_2,tau_4)}`

These are deliberately different organisations over the same transformation set.

The concrete edge pattern remains a design candidate until the A-reconstruction and non-degeneracy checks are completed.

## 5. Two-step intervention

The observation protocol selects a first transformation from the common initial accessible set and then attempts a specified second transformation under the frozen state-transition rules.

The primary outcome is whether the prescribed two-step trajectory completes successfully.

The outcome is never used to construct or modify E_tau.

## 6. Required invariants

Before any outcome is observed, the scientific package must verify:

1. identical transformation identities;
2. identical initial accessibility;
3. identical inherited state/context variables;
4. pre-registered dependency structures;
5. dependency structures not reconstructible from the inherited representation;
6. identical intervention and observation protocol;
7. no outcome-dependent modification of either T_acc or E_tau.

## 7. Why four transformations

Three transformations are insufficient for a clean crossed dependency contrast with a nontrivial control relation while retaining a common accessible set. Four transformations provide the minimal convenient construction for two distinct directed pairings without requiring additional semantic machinery.

This is a design rationale, not an empirical claim.

## 8. A-reconstruction test

Before fixture freeze, the package must attempt to reconstruct E_tau from the complete inherited information available to A.

If the reconstruction succeeds exactly, the synthetic world is rejected as non-discriminating and must be redesigned.

## 9. Deliberate exclusions

Not yet fixed:

- transformation semantics beyond the minimal precondition/transition formalism;
- exact state variables;
- concrete dependency pattern;
- intervention sequence;
- N;
- effect size;
- power;
- statistical model;
- randomisation scheme;
- implementation language;
- workflow;
- execution authorization.

## 10. Next gate

The next governance task is to specify the **minimal transformation semantics and state-transition rules** that make the two dependency structures causally operative while preserving identical initial T_acc and inherited state.

No experiment is authorized by this document.