# IT-NOSD-010 — TR-132 IT-G1 Closure Record 001

**Date:** 2026-09-11  
**Status:** `CLOSED — BOUNDED REPRODUCIBILITY / ADMISSION PASS`  
**Candidate:** ETSI TS 23.502 / 3GPP 5GS procedures  
**Experimental unit:** one frozen public 5G-to-5G handover event

## 1. Decision

`IT-G1 = CLOSED — BOUNDED REPRODUCIBILITY / ADMISSION PASS`

The independent technical executor v0.2 reproduced the frozen IT-NOSD-010 candidate event, the bounded pre-event state observations, the operational accessibility predicate and the state-transition identity. All mandatory predicates G1-01 through G1-10 returned `true`.

This closes admission/reproducibility for the **single frozen event** only. It does not authorize industrial execution and does not establish utility, causality, value, comparative superiority, transversal validity or scientific validation.

## 2. Independent execution evidence

Executor:
`IT-NOSD-010-IT-G1-INDEPENDENT-REPRODUCIBILITY-v0.2`

Canonical executor path:
`00_GOVERNANCE/INDUSTRIAL_TRACK/execution/it_nosd_010_it_g1_independent_reproducibility_v02.py`

Canonical executor blob SHA:
`58534d178df0174c28165c1162cf4ba65dc8fd75`

Execution result supplied from independent local run:
`PASS`

Execution mode:
`TECHNICAL_INDEPENDENT_REPRODUCIBILITY`

Environment reported:
- Python `3.14.7`
- Windows `11-10.0.26200-SP0`

## 3. Frozen provenance reproduced

Events MD5:
`f7f1eb72063ad5ab290817815c55f297`

Spectrum MD5:
`0796c64f3c8850e5b571ce49c556c50b`

Both matched the frozen IT-G0 values.

## 4. Frozen candidate reproduced

- session: `T-Mobile_2026.03.28_05.14.11`
- timestamp: `2026-03-28T05:16:15`
- event: `HANDOVER_DATA_5G5G`
- source cell: `2`
- target cell: `3`
- node: `84246`

Pre-event window:
`[2026-03-28T05:15:15, 2026-03-28T05:16:15)`

Target observations reproduced: `15`  
First target observation: `2026-03-28T05:15:32`  
Source observations reproduced: `2`  
Post-event rows used for accessibility: `0`  
Outcome used for accessibility: `false`

## 5. Mandatory predicate result

| Predicate | Result |
|---|---|
| G1-01 Provenance integrity | PASS |
| G1-02 Candidate event identity | PASS |
| G1-03 Pre-event state closure | PASS |
| G1-04 Transformation identity | PASS |
| G1-05 Accessibility/outcome separation | PASS |
| G1-06 State-transition closure | PASS |
| G1-07 Temporal closure | PASS |
| G1-08 Downstream separation | PASS |
| G1-09 Reproducibility | PASS |
| G1-10 Scope discipline | PASS |

## 6. Transformation identity

`τ_HO = serving-cell / serving-gNB state → target-cell / target-gNB serving state`

The complete accessible transformation structure `T_acc(S_t)` was not enumerated and was not required by the bounded IT-G0/IT-G1 gate.

## 7. Package integrity / seal disposition

`PACKAGE_INTEGRITY_SEAL = PASS`

Seal basis:
1. frozen dataset identities and MD5 values reproduced;
2. frozen event selector reproduced uniquely;
3. frozen pre-event window reproduced exactly;
4. canonical v0.2 executor is identified by blob SHA;
5. all mandatory G1 predicates returned PASS;
6. no post-event data was used for accessibility;
7. no new dataset, event, outcome criterion or industrial action was introduced.

The independent run result is treated as execution evidence supplied to this closure record; no claim is made that the local execution environment itself is a GitHub-hosted execution artifact.

## 8. Boundary and authorization

`IT-G0 = CLOSED — BOUNDED PRE-OUTCOME CASE-DEFINITION PASS`  
`IT-G1 = CLOSED — BOUNDED REPRODUCIBILITY / ADMISSION PASS`  
`INDUSTRIAL_EXECUTION_AUTHORIZATION = NONE`  
`SCIENTIFIC_CORE = UNCHANGED`

IT-G1 closure does **not** imply:
- complete `T_acc(S_t)`;
- full normative 3GPP admissibility;
- industrial utility;
- causal effect;
- value realization;
- comparative superiority;
- transversal validity;
- scientific validation;
- authorization for industrial execution.

## 9. Next controlled gate

Any downstream experimental or industrial use of IT-NOSD-010 requires a separate explicitly authorized gate. The present record closes only the bounded IT-G1 admission/reproducibility question for the frozen event.
