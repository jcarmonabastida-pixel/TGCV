# TGCV — Domain A Primary-Source Verification 001

**Status:** PASS — PRIMARY SOURCE VERIFIED
**Scientific execution:** NOT AUTHORIZED
**Date:** 2026-09-20

## 1. Verification target
The previous construction audit required a primary source for the Domain A self-adaptive-system fixture.

Primary source verified:
Garlan, Cheng, Huang, Schmerl and Steenkiste, **Rainbow: Architecture-Based Self Adaptation with Reusable Infrastructure**, IEEE Computer, 2004. The Carnegie Mellon/ABLE publication record identifies the paper and states that Rainbow uses software architectures and reusable infrastructure for self-adaptation, with explicit adaptation strategies. citeturn0search0turn0search1

A detailed Rainbow source also explicitly describes operators with conditions of applicability, expected effects, cost-benefit attributes, and target-system commands, while the framework separates adaptation logic from application logic. citeturn0search27

## 2. Verified source semantics
The primary source basis establishes the following independently specified elements:

- an architecture model representing the managed system;
- monitored observations reflected into the architecture model;
- adaptation strategies;
- operators/commands used by strategies;
- applicability conditions for adaptive operators;
- expected effects of operators;
- strategy selection and execution;
- resulting changes to the managed system.

The Rainbow framework is explicitly intended to monitor, reason about, and adapt running systems, with adaptation strategies specified separately from the managed system. citeturn0search9turn0search17

## 3. Consequence for fixture construction
Domain A can therefore derive accessibility from source-defined applicability without using the realized adaptation or its later result:

`T_acc,t = { o ∈ Operators | Applicability(o,S_t) = true }`

where `Operators` and their applicability conditions originate in the source model.

`T_real,t` is the operator actually selected/executed.

`S_(t+1)` is obtained from the operator's specified effect on the managed system.

This derivation is an analytical mapping over source semantics, not a new TGCV domain assumption.

## 4. Important distinction
Rainbow itself already provides an explicit notion of applicable adaptive actions/operators. Therefore TGCV must treat the identity:

`T_acc,t ≡ applicable Rainbow operators`

as a legitimate null hypothesis.

The representation test cannot claim novelty merely by renaming the Rainbow operator set `T_acc`.

## 5. Source-to-fixture traceability requirement
The exact Rainbow example/model selected for the executable fixture must still be recorded before freeze, including:

- architecture/model identifier;
- operator/strategy identifiers;
- applicability conditions;
- expected effects;
- state variables used by those conditions;
- strategy-selection rule;
- resulting-state rule.

Only source facts explicitly available before realization may enter the pre-realization representation.

## 6. Verification decision
**PASS — DOMAIN A PRIMARY-SOURCE VERIFICATION.**

The previous blocker concerning absence of a primary source is resolved.

This does not yet mean that the Domain A fixture is frozen or scientifically executable.

## 7. Governance
No frozen TR-131 artifact is modified.
No TGCV Core/RMA/Evidence→Claim Matrix change is authorized.
No scientific execution is authorized.

## 8. Next gate
**CROSS-DOMAIN REPRESENTATION PACKAGE FREEZE CANDIDATE**

Construct the exact two fixtures using the verified Rainbow source and the already audited ACPBench/VisitAll source. Complete source-to-fixture traceability, null/control, ambiguity case, equivalence relation and ΔT_acc operator. Then perform the package audit before any freeze.