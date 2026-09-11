# IT-NOSD-010 — TR-132 IT-G1 Admission / Reproducibility Gate 001

**Date:** 2026-09-11  
**Status:** `OPEN — ADMISSION / REPRODUCIBILITY PREPARATION`  
**Candidate:** ETSI TS 23.502 / 3GPP 5GS procedures  
**Experimental unit:** one frozen public 5G-to-5G handover event

## 1. Purpose

Define the minimum controlled evidence required to admit the single frozen IT-NOSD-010 event from IT-G0 into IT-G1. This is a preparation/admission gate only. It does not authorize industrial execution, utility assessment, causal assessment, value assessment or comparative superiority assessment.

## 2. Upstream closure

IT-G0 is already closed as `CLOSED — BOUNDED PRE-OUTCOME CASE-DEFINITION PASS`.

Frozen event:
- session: `T-Mobile_2026.03.28_05.14.11`;
- timestamp: `2026-03-28T05:16:15`;
- event: `HANDOVER_DATA_5G5G`;
- source cell: `2`;
- target cell: `3`;
- node: `84246`.

Frozen source files:
- events CSV MD5: `f7f1eb72063ad5ab290817815c55f297`;
- spectrum CSV MD5: `0796c64f3c8850e5b571ce49c556c50b`.

## 3. IT-G1 admission predicates

All predicates below must be independently evidenced before IT-G1 can be closed.

### G1-01 — Provenance integrity
The exact public dataset record, version, file identities and hashes must be frozen and reproducible.

### G1-02 — Candidate event identity
The event must remain uniquely identified by session, timestamp, event type and source/target identifiers.

### G1-03 — Pre-event state closure
The bounded pre-event state/context window must be reproducible, including the variables actually used by the accessibility/admissibility rule.

### G1-04 — Transformation identity
The candidate transformation must be defined without reference to its subsequent success/failure outcome:

`τ_HO = serving-cell / serving-gNB state → target-cell / target-gNB serving state`.

### G1-05 — Accessibility/outcome separation
Accessibility/admissibility must be computed only from information available before the candidate event. The occurrence or subsequent result of the handover must not be used to establish accessibility.

### G1-06 — State-transition closure
The post-event state may be used only to establish the realized state transition, not retroactively to define pre-event accessibility. The transition must be reconstructable from frozen evidence.

### G1-07 — Temporal closure
The observation windows and inclusion/exclusion boundaries must be explicit and reproducible. No uncontrolled look-ahead is permitted.

### G1-08 — Downstream separation
Transformation identity, accessibility, Reach/trajectory and downstream outcome must remain separately represented. A successful handover is not itself evidence of TGCV utility or value.

### G1-09 — Reproducibility
An independent technical reconstruction must be able to reproduce the frozen event, pre-event observations and gate predicates from the public evidence package without relying on prior outcome interpretation.

### G1-10 — Scope discipline
IT-G1 closure must not be interpreted as complete `T_acc(S_t)`, normative 3GPP admissibility, industrial utility, causal effect, comparative superiority, value realization, transversal validity or scientific validation.

## 4. Required admission package

Before IT-G1 closure, the controlled package must contain:

1. exact dataset record/version provenance;
2. exact event and spectrum file hashes;
3. frozen candidate-event selector;
4. bounded pre-event window definition;
5. pre-event state/context extraction;
6. accessibility predicate and outcome-independence declaration;
7. transformation identity declaration;
8. state-transition reconstruction rule;
9. temporal-closure rule;
10. downstream-separation declaration;
11. independent reconstruction result;
12. integrity/seal record linking all artifacts.

## 5. Independent executor boundary

The independent reconstruction must not use a previously interpreted outcome to decide whether the candidate was accessible. It may use the frozen evidence package and the published dataset itself, but must not introduce new datasets, substitute a different event, alter the frozen windows, or infer missing fields from later outcomes.

## 6. IT-G1 decision rule

`IT-G1 = ADMITTED` only if every mandatory predicate G1-01 through G1-10 is `PASS` and the package integrity/seal is `PASS`.

Any unresolved mandatory predicate leaves IT-G1 `NOT ADMITTED` or `OPEN`, according to the specific audit disposition. No rescue by post-outcome evidence is permitted.

## 7. Authorization boundary

`INDUSTRIAL EXECUTION AUTHORIZATION = NONE`.

IT-G1 admission, even if later closed as PASS, is a reproducibility/admission result. Any subsequent utility or industrial execution requires a separate explicit gate and authorization.

## 8. Current status

`IT-G0 = CLOSED — BOUNDED PRE-OUTCOME CASE-DEFINITION PASS`  
`IT-G1 = OPEN — ADMISSION / REPRODUCIBILITY PREPARATION`  
`INDUSTRIAL EXECUTION AUTHORIZATION = NONE`  
`SCIENTIFIC CORE = UNCHANGED`

## 9. Next controlled operation

Create the frozen IT-G1 admission package and its independent technical executor. The executor must reproduce the single frozen event and all mandatory pre-outcome predicates without executing the transformation or using downstream outcome to establish accessibility.
