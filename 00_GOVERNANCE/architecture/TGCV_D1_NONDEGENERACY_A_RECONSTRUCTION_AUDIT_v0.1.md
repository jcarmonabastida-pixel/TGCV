# TGCV — D1 Formal Non-Degeneracy / A-Reconstruction Audit v0.1

**Status:** CURRENT GOVERNANCE AUDIT / D1 NOT ADMISSIBLE FOR EXPERIMENTAL FREEZE  
**Date:** 2026-10-01  
**Decision:** ARCH-DISC-001

## 1. Audit objective

Test whether the D1 synthetic construction actually distinguishes the inherited architecture A from the TSDI hypothesis B, rather than merely hiding an additional transition rule from A.

## 2. Audit result

**RESULT: NON-DISCRIMINATING / REDESIGN REQUIRED.**

The current D1 construction does not yet pass the architectural non-degeneracy test.

## 3. Finding 1 — E_tau is currently encoded in the transition mechanism

The current specification says that the world differs through E_tau and that E_tau determines which subsequent transformation is permitted.

Therefore E_tau is functionally part of the system's transition rule.

If the inherited architecture permits its auxiliary transition/mechanism representation to contain the operative rule governing transformations, then an A representation can encode the same distinction as an auxiliary mechanism without adopting a new primary object called a dynamic transformation-space structure.

In that case:

`A = (S, T_acc, auxiliary transition mechanism)`

can reproduce the same future behaviour.

This is an **equivalent reconstruction**, not evidence against A.

## 4. Finding 2 — identical S_0 and T_acc are insufficient

Although the current construction correctly holds `S_0` and `T_acc,0` equal, that equality does not establish architectural discrimination if the two worlds differ in an unrepresented rule that controls subsequent transitions.

The experiment would otherwise test:

`same observed variables + hidden rule -> different outcome`

rather than:

`same inherited architecture -> insufficient representation of an empirically necessary transformation-space structure`.

## 5. Finding 3 — current P register does not solve the problem

The common prerequisite register P is identical initially. The difference is introduced by the designated dependency relation.

Because the dependency relation changes which continuation is permitted, the relation can be treated as part of the transition mechanism unless the experiment demonstrates that the relevant relational information is not reducible to the inherited mechanism/state representation under a pre-specified equivalence criterion.

## 6. Architectural consequence

D1 in its current form cannot be used to produce FOR-B / AGAINST-A evidence.

It may still be useful as a **diagnostic construction** showing exactly where a naive D1 design collapses into an auxiliary transition-rule explanation.

This is a useful governance result: the transition layer has prevented premature experimental confirmation.

## 7. Required redesign condition

A valid discriminator must prevent A from recovering the B distinction simply by appending the same transition relation as an auxiliary mechanism.

At least one of the following must be established before D1 can reopen:

1. the disputed structural property is empirically observable independently of the transition rule that generates the future outcome;
2. A's admissible representation is formally frozen and excludes the disputed relational object for an explicit theoretical reason, rather than by experimental convenience;
3. the experiment compares predictions made from equal inherited representations where all admissible auxiliary mechanisms are also equivalent, while B uses an independently observed structural property to predict the future outcome;
4. a materially different discriminator is selected that tests structural information not reducible to an inherited transition mechanism.

## 8. Current gate

**D1 EXPERIMENTAL GATE: CLOSED — REDESIGN REQUIRED.**

No fixture, sample size, power analysis, statistical model or execution workflow should be designed from the current D1 construction.

## 9. Next governed task

The next task is not to repair the same example by adding parameters. It is to revisit the architectural distinction and identify an observable property of transformation-space structure that can be held independently of the mechanism producing the future outcome.

Only after that property survives an A-reconstruction audit should D1 or another discriminator proceed to experimental specification.