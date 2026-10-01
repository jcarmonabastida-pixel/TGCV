# TGCV — Inherited Architecture Admissibility Specification v0.1

**Status:** CURRENT GOVERNANCE SPECIFICATION / NO EXPERIMENT AUTHORIZATION  
**Date:** 2026-10-01  
**Decision:** ARCH-TRANS-001

## 1. Purpose

Formalize the inherited architecture's admissible representational boundary before any new architectural discriminator is designed.

This specification does not declare the inherited architecture correct. It makes its scope sufficiently explicit that a future empirical result can distinguish:

- a derivable/declared auxiliary within the existing architecture; from
- a genuinely new primary structural object requiring architectural review.

## 2. Working Core

For the present transition period, the inherited working Core is:

`A_Core = (S, T_acc)`

where:

- `S` is the system state at the relevant observation point;
- `T_acc` is the explicitly identified accessible transformation set.

This is a **working canonical baseline**, not a claim that this ontology is final.

## 3. Admissible auxiliary vocabulary

Auxiliary information may be used with A only when it is one of:

1. **Declared state/context:** variables already included in the frozen definition of `S`, or explicitly declared components of `C` and `L`.
2. **Derived descriptors:** deterministic functions of `S`, `C`, `L`, `T_acc` and fixed inputs.
3. **Event/transition annotations:** observations describing an already-defined transformation execution, provided they do not introduce a new independently evolving structural object.
4. **Derived temporal quantities:** changes, counts, reachability or trajectories computed from the frozen A representation and its declared transition rules.
5. **Measurement metadata:** variables needed to document the measurement process but not used to create a new explanatory object.

## 4. Auxiliary admissibility test

A candidate variable X remains admissible within A only if all conditions hold:

`X = f(S,C,L,T_acc,I_fixed)`

for a pre-specified fixed function or formally declared measurement rule, and:

- X does not define a new primitive relation among transformations;
- X does not require treating transformation-space organisation as an independently evolving object;
- X can be frozen before the relevant outcome is observed;
- X is not introduced solely because an earlier A representation failed;
- adding X does not change the identity of the primary explanatory object.

Failure of any condition triggers architectural review.

## 5. Specifically non-admissible by default

The following are **not automatically admissible auxiliaries**:

- an independently evolving graph over transformations;
- an independently evolving dependency/relation structure over transformations;
- topology/connectivity of the transformation space when treated as a primary evolving object;
- structural reconfiguration that cannot be derived from the frozen A representation;
- a new state variable whose only justification is to encode an observed failure of A.

Such objects may ultimately be shown reducible to A, but that reducibility must be demonstrated rather than assumed.

## 6. Core-revision trigger

A candidate object X requires Core review when:

1. X is independently observable;
2. X has its own temporal evolution or structural identity;
3. X is not derivable from the frozen A representation under the admissibility test;
4. X carries explanatory/predictive information relevant to the architectural question;
5. treating X as an auxiliary would amount to changing the primary object rather than merely describing it.

Meeting these conditions does **not** automatically establish a new Core. It triggers formal architectural review.

## 7. Anti-post-hoc rule

The admissibility status of a candidate structural object must be specified before the discriminating observation.

A failed A representation may not be retroactively expanded by declaring the missing structure an auxiliary after seeing the result.

Conversely, a candidate B object may not be declared ontologically new merely because it improves prediction.

## 8. Equivalence principle

A future architectural test must distinguish three outcomes:

### A-equivalent

The candidate structural object is reconstructible from the frozen A representation under the pre-specified admissibility rules.

**Disposition:** remains within A; no architectural inference.

### Architecturally non-equivalent but empirically unnecessary

The candidate object is not derivable under A, but its presence produces no reproducible discriminating information in the controlled test.

**Disposition:** no Core revision; candidate remains unresolved or rejected for that test.

### Architecturally non-equivalent and empirically informative

The candidate object is not derivable under A and provides reproducible information under a controlled, independently operationalised test.

**Disposition:** triggers architectural review. It is not itself an automatic Core replacement.

## 9. Implication for D1

The current D1 `E_tau` construction fails the A-reconstruction boundary because `E_tau` can be interpreted as an auxiliary transition mechanism.

Therefore D1 remains:

**NON-DISCRIMINATING / CLOSED FOR EXPERIMENTAL FREEZE.**

No D1 fixture should proceed until a candidate structural object satisfies this admissibility boundary.

## 10. Governance consequence

The inherited Core and Evidence→Claim Matrix remain unchanged.

This specification is a transition-governance constraint, not a scientific claim and not a Core revision.

## 11. Next gate

The next task is to perform a **candidate-object admissibility audit** on possible TSDI structural objects already visible in the accumulated evidence (for example, independently observed structural organisation, connectivity/reconfiguration, or trajectory-space properties), without designing or executing a new experiment.

No scientific execution is authorized by this document.
