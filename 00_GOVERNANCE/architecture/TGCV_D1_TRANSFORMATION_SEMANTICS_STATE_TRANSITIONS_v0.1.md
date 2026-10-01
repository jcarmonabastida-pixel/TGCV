# TGCV — D1 Minimal Transformation Semantics & State Transitions v0.1

**Status:** GOVERNANCE DESIGN SPECIFICATION / NO EXPERIMENT AUTHORIZATION  
**Date:** 2026-10-01  
**Decision:** ARCH-DISC-001

## 1. Purpose

Define minimal deterministic transformation semantics that make the D1 dependency contrast operational while preserving identical initial T_acc and inherited state.

## 2. State

The synthetic state contains a binary prerequisite register:

`P = {p1, p2}`

At the initial observation point:

`P_0 = {p1, p2}`

and the inherited state/context is identical across matched worlds.

The prerequisite register is part of the operational execution state, but the architectural test must establish whether its organisation can be represented without explicitly encoding the disputed dependency structure.

## 3. Transformation semantics

Each transformation has a deterministic effect:

- `tau_1`: requires `p1`; preserves `p1`; produces no new prerequisite.
- `tau_2`: requires `p1`; sets `p2` as the preserved prerequisite for the next step.
- `tau_3`: requires `p2`; preserves `p2`; produces no new prerequisite.
- `tau_4`: requires `p2`; sets `p1` as the preserved prerequisite for the next step.

These primitive effects alone do not define E_tau. E_tau is the pre-registered relation specifying which subsequent transformation dependency is instantiated in the controlled world.

## 4. Dependency-conditioned transition rule

For D1, a directed edge `(tau_i,tau_j)` means that after successful execution of `tau_i`, the protocol permits `tau_j` as the designated dependent continuation when its ordinary transformation precondition is satisfied.

The matched worlds instantiate different designated continuations over the same initial transformation identities.

Candidate controlled pairings:

`World 1: tau_1 -> tau_2 and tau_3 -> tau_4`

`World 2: tau_1 -> tau_3 and tau_2 -> tau_4`

The exact pairing remains subject to the A-reconstruction test before fixture freeze.

## 5. Initial accessibility invariant

At the frozen initial point, all four transformations are accessible in both worlds:

`T_acc,0 = {tau_1, tau_2, tau_3, tau_4}`

No dependency edge is allowed to alter this initial membership.

## 6. Future observable

After selecting a first transformation, the protocol attempts the pre-specified second transformation.

`Y = 1` iff the prescribed two-step trajectory is completed under the frozen transition rules.

The first transformation, second transformation, intervention order and success criterion must be fixed before observing Y.

## 7. Non-circularity constraint

The dependency relation cannot be inferred from Y.

The transformation definitions, prerequisites and designated dependency structure are frozen before trajectory execution.

## 8. A-reconstruction requirement

Before scientific preflight, the package must test whether the complete dependency-conditioned transition behaviour can be reconstructed from the inherited representation alone:

`S_0, C_0, L_0, T_acc,0` plus declared inherited auxiliary variables.

If it can, D1 is non-discriminating.

If reconstruction requires introducing the same relational/dependency object whose architectural necessity is being tested, the result must be recorded as **equivalent reconstruction**, not as an independent A explanation.

## 9. Important limitation

The present semantics deliberately avoid claiming that dependency structure is a new causal primitive. They define only a controlled mechanism through which two worlds with equal initial T_acc can generate different subsequent trajectory constraints.

## 10. Next gate

The next governance task is to perform a **formal non-degeneracy / A-reconstruction audit** on these semantics before any fixture, sample-size or statistical design is considered.

No experiment is authorized by this document.