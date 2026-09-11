# IT-NOSD-010 — TR-132 IT-G2 Downstream Separation Gate 001

**Date:** 2026-09-11  
**Status:** `OPEN — GATE DEFINITION ONLY`  
**Candidate:** ETSI TS 23.502 / 3GPP 5GS procedures  
**Experimental unit:** one frozen public 5G-to-5G handover event

## 1. Purpose

Define the next controlled gate after IT-G0 case-definition and IT-G1 reproducibility/admission closure.

IT-G2 is a **downstream-separation and realized-transition gate**. Its purpose is to determine whether the frozen event package can support a bounded representation of:

`pre-state → candidate transformation → realized post-state`

while preserving the separation between transformation identity, pre-outcome accessibility, realized transition, downstream trajectory and any later outcome/value interpretation.

This gate does **not** authorize industrial execution and does not establish utility, causality, value, comparative superiority, normative 3GPP admissibility or scientific validation.

## 2. Upstream closure

- `IT-G0 = CLOSED — BOUNDED PRE-OUTCOME CASE-DEFINITION PASS`.
- `IT-G1 = CLOSED — BOUNDED REPRODUCIBILITY / ADMISSION PASS`.
- Independent v0.2 reproduction: all G1-01 through G1-10 `PASS`.
- Package integrity/seal basis: `PASS`.
- `INDUSTRIAL_EXECUTION_AUTHORIZATION = NONE`.

The IT-G1 closure is limited to the single frozen event. Historical records remain immutable.

## 3. IT-G2 question

Can the frozen evidence support a bounded, auditable representation of the **realized state transition** for the already-admitted candidate transformation, without using the realized outcome to redefine the pre-event accessibility predicate and without conflating the transition with downstream utility/value?

## 4. Mandatory predicates

### G2-01 — Frozen candidate continuity
The exact IT-G0/IT-G1 candidate selector must remain unchanged: session, timestamp, event type, source cell, target cell and node.

### G2-02 — Pre-state continuity
The pre-event state/context used by IT-G0/IT-G1 must remain unchanged and traceable to the frozen evidence.

### G2-03 — Post-state observability
The evidence must contain an explicitly identifiable post-event state associated with the candidate event, using only evidence temporally at or after the event for this realized-transition predicate.

### G2-04 — Transition identity
The realized transition must be representable as a bounded mapping from the frozen pre-event serving state to the frozen post-event serving state, consistent with the admitted `τ_HO` identity.

### G2-05 — Accessibility isolation
No post-event observation may be used to establish or modify the pre-outcome accessibility result already closed under IT-G0/IT-G1.

### G2-06 — Outcome separation
The realized transition must be represented separately from downstream outcome, trajectory, utility, value or comparative performance.

### G2-07 — Temporal closure
The post-event observation rule, inclusion boundary and maximum temporal association window must be explicit and reproducible.

### G2-08 — Evidence integrity
The exact frozen source files and hashes must remain unchanged. No replacement dataset or substituted event is permitted.

### G2-09 — Deterministic reconstruction
An independent technical executor must be able to reproduce the same bounded post-event transition representation from the frozen evidence package.

### G2-10 — Scope discipline
IT-G2 closure must not be interpreted as proof of complete `T_acc(S_t)`, normative 3GPP admissibility, utility, causality, value, comparative superiority, transversal validity or scientific validation.

## 5. Required execution package

Before IT-G2 can close, the controlled package must contain:

1. the unchanged IT-G0/IT-G1 candidate selector;
2. exact frozen file hashes;
3. explicit post-event association window;
4. explicit post-event state variables used;
5. transition reconstruction rule;
6. explicit proof that accessibility is pre-outcome and unchanged;
7. downstream-outcome separation declaration;
8. independent reconstruction result;
9. deterministic result artifact;
10. package integrity/seal record.

## 6. Prohibitions

The IT-G2 executor must not:

- alter the frozen candidate event;
- redefine the accessibility predicate;
- use post-event data to retroactively establish accessibility;
- introduce a new dataset or event;
- infer utility, value or causal effect;
- execute a network transformation;
- mutate external systems;
- claim normative 3GPP compliance from the empirical observation alone.

## 7. Decision rule

`IT-G2 = CLOSED` only if all mandatory predicates G2-01 through G2-10 are `PASS`, the independent reconstruction is deterministic, and package integrity/seal is `PASS`.

Otherwise IT-G2 remains `OPEN` or `NOT ADMITTED` according to the documented failure mode.

## 8. Authorization boundary

`INDUSTRIAL_EXECUTION_AUTHORIZATION = NONE`.

No network-side action, operational handover, industrial transformation or external-system mutation is authorized by this gate.

## 9. Next controlled operation

Create the IT-G2 independent post-event transition executor using only the frozen IT-NOSD-010 evidence and the bounded post-event association rule. The executor must be technical/read-only and must preserve the closed IT-G0/IT-G1 boundaries.
