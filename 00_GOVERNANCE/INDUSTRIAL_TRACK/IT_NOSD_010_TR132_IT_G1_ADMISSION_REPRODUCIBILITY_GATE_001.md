# IT-NOSD-010 — TR-132 IT-G1 Admission / Reproducibility Gate 001

**Date:** 2026-09-11  
**Status:** `CLOSED — BOUNDED REPRODUCIBILITY / ADMISSION PASS`  
**Candidate:** ETSI TS 23.502 / 3GPP 5GS procedures  
**Experimental unit:** one frozen public 5G-to-5G handover event

## 1. Purpose

Define the minimum controlled evidence required to admit the single frozen IT-NOSD-010 event from IT-G0 into IT-G1. This is an admission/reproducibility gate only. It does not authorize industrial execution, utility assessment, causal assessment, value assessment or comparative superiority assessment.

## 2. Upstream closure

IT-G0 is closed as `CLOSED — BOUNDED PRE-OUTCOME CASE-DEFINITION PASS`.

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

## 3. IT-G1 admission predicates — final result

All mandatory predicates were independently reproduced by executor v0.2 and returned `PASS`:

- G1-01 Provenance integrity — PASS
- G1-02 Candidate event identity — PASS
- G1-03 Pre-event state closure — PASS
- G1-04 Transformation identity — PASS
- G1-05 Accessibility/outcome separation — PASS
- G1-06 State-transition closure — PASS
- G1-07 Temporal closure — PASS
- G1-08 Downstream separation — PASS
- G1-09 Reproducibility — PASS
- G1-10 Scope discipline — PASS

## 4. Independent execution evidence

Executor:
`IT-NOSD-010-IT-G1-INDEPENDENT-REPRODUCIBILITY-v0.2`

Canonical path:
`00_GOVERNANCE/INDUSTRIAL_TRACK/execution/it_nosd_010_it_g1_independent_reproducibility_v02.py`

Executor blob SHA:
`58534d178df0174c28165c1162cf4ba65dc8fd75`

Independent local execution result:
`PASS`

Reproduced:
- target observations: `15`;
- first target observation: `2026-03-28T05:15:32`;
- source observations: `2`;
- post-event rows used for accessibility: `0`;
- outcome used for accessibility: `false`.

## 5. IT-G1 decision

`IT-G1 = CLOSED — BOUNDED REPRODUCIBILITY / ADMISSION PASS`

Package integrity/seal disposition: `PASS`.

Closure record:
`00_GOVERNANCE/INDUSTRIAL_TRACK/IT_NOSD_010_TR132_IT_G1_CLOSURE_001.md`

## 6. Scope discipline

IT-G1 closure is limited to the single frozen event and the bounded admission/reproducibility question. It does not imply:
- complete `T_acc(S_t)`;
- full normative 3GPP admissibility;
- industrial utility;
- causal effect;
- value realization;
- comparative superiority;
- transversal validity;
- scientific validation.

## 7. Authorization boundary

`INDUSTRIAL_EXECUTION_AUTHORIZATION = NONE`.

Any subsequent utility or industrial execution requires a separate explicit gate and authorization.

`SCIENTIFIC CORE = UNCHANGED`.

## 8. Historical v0.1 defect disposition

The initial v0.1 executor produced a technical FAIL because it queried non-canonical timestamp field names. This was classified as an executor defect, not a dataset or IT-G1 evidence failure. v0.2 corrected the schema to the canonical `timestamp_iso` and associated frozen fields, after which the independent reconstruction returned PASS.
