# TGCV — Current Status

**Date:** 2026-09-11
**Governance state:** CURRENT — material IUT-A-01 and IT-NOSD-010 evidence propagation completed
**Current RMA:** `00_GOVERNANCE/rma/TGCV_RMA_current.md`
**Current Evidence→Claim Matrix:** `00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md`

## Scientific Core
- **Core:** unchanged.
- **TR-132-MOD-1:** `CLOSED — BOUNDED PASS (L3)`.
- No Core primitive, relation, threshold or falsification criterion was modified.
- No scientific claim upgrade was introduced.
- Material evidence is now propagated to the Evidence→Claim Matrix even when claim status does not change; claim upgrade remains a separate decision.

## Industrial Track
- **Track status:** `PROPOSED`.
- **IUT-A-01 U2:** `CLOSED — U2-NULL`; FULL_PILOT 001 integrity PASS; M1 PASS; M2 FAIL; no U2-positive decision-performance conclusion.
- **FAA AMOC IT-METH-I:** `CLOSED — INCONCLUSIVE`; historical records immutable.
- **Class-II AWS-PatchAsgInstance Phase A:** `CLOSED — PREDECISION RECONSTRUCTION REPRODUCIBILITY PASS`.
- **Class-II AWS-PatchAsgInstance Phase B0 accessibility:** `CLOSED — NO ADMISSIBLE RESOLVED ACCESSIBILITY DIFFERENCE IDENTIFIED`.
- **Class-II AWS-PatchAsgInstance B0 permissions audit:** `CLOSED — PARTIAL / EFFECTIVE CANDIDATE PERMISSION UNRESOLVED`.
- **IT-NOSD-010 / ETSI TS 23.502 / 3GPP 5GS:** `IT-G0 CLOSED — BOUNDED PRE-OUTCOME CASE-DEFINITION PASS`; `IT-G1 CLOSED — BOUNDED REPRODUCIBILITY / ADMISSION PASS`; `IT-G2 CLOSED — BOUNDED DOWNSTREAM-SEPARATION PASS`.
- Industrial utility: `UNPROVEN / OPEN`.
- Comparative superiority: `NOT ESTABLISHED`.
- Causality: `NOT ASSESSED`.
- Financial/value effect: `NOT ASSESSED`.

## Evidence propagation boundary
- Current Evidence→Claim Matrix: `v1.0`.
- IUT-A-01 U2 is represented as material bounded comparative methodological evidence; C12 remains `H` because M2 failed and the overall result is `U2-NULL`.
- IT-NOSD-010 G0/G1/G2 is represented as material bounded methodological evidence for reconstruction and downstream separation; no C01–C16 status is upgraded.
- Evidence propagation does not imply claim upgrade.

## IUT-A-01 U2 closure boundary
- Evidence artifact: `03_EXPERIMENTS/IUT-A-01/IUT_A01_U2_FULL_PILOT_RESULT_001.json`.
- Closure audit: `03_EXPERIMENTS/IUT-A-01/IUT_A01_U2_FULL_PILOT_CLOSURE_AUDIT_001.md`.
- Trial universe hash: `4a993f428144fc955c4060bc0299c23357f663929ecf05bfa3cb9cade30b8ec5`.
- M1: Control `60.0% (24/40)`; TGCV `100.0% (40/40)`; `+40.0 pp`; predeclared gate `PASS`.
- M2: Control median `0.00155 ms`; TGCV median `0.00485 ms`; relative reduction `-212.9%`; predeclared gate `FAIL`.
- M3: retired and not active for scoring.
- Final classification: `U2-NULL`.
- Timing is a microbenchmark of the decision functions, not evidence of human or industrial workflow time.
- Manifest/executor overhead-field discrepancy recorded as non-blocking documentation/methodological note.
- No rerun is authorized or required.
- No explanatory superiority, industrial utility, financial/value realization, causal generalisation, or TGCV Core modification is established by this pilot.

## IT-NOSD-010 bounded closure boundary
- Candidate: `ETSI TS 23.502 / 3GPP 5GS procedures`.
- Experimental unit: one bounded public `5G-to-5G` handover event from the T-Mobile Spectrum Usage Dataset.
- `IT-G0 = CLOSED — BOUNDED PRE-OUTCOME CASE-DEFINITION PASS`.
- `IT-G1 = CLOSED — BOUNDED REPRODUCIBILITY / ADMISSION PASS`.
- `IT-G2 = CLOSED — BOUNDED DOWNSTREAM-SEPARATION PASS`.
- G2-01 through G2-10 all `PASS`; accessibility was not reused as outcome; outcome was not used to define post-state; complete `T_acc` enumeration was not required.
- This remains bounded evidence for one frozen event and does not establish normative 3GPP admissibility, complete `T_acc`, utility, causality, value, superiority or scientific validation.

## Methodological closure
- `MR-01` through `MR-07` remain adopted as preconditions for future industrial utility tests.
- IUT-A-01 U2 FULL_PILOT 001 is closed as `U2-NULL`; its frozen evidence and closure audit are canonical experiment records.
- IT-NOSD-010 G2 closure is a bounded downstream-separation/reconstructability result for the single frozen event; it does not authorize industrial execution or establish utility/value/causality.

## Industrial discovery
- Corrected post-IT-METH-I discovery framework: `CURRENT / OPERATIVE`.
- AWS Systems Manager Automation / PatchAsgInstance: conditional candidate family; targeted fixture Phase-A/B0 methodological work closed to the extent governed; IT-G1 industrial admission remains open/not granted.
- IT-NOSD-010: IT-G0, IT-G1 and IT-G2 closed for one concrete bounded event; no industrial execution authorization.

## Existing routing
- FAA AMOC: G1/G2/G3/G4/G5 completed; comparison and experiment closed `INCONCLUSIVE`.
- LynxOS-178 RSC: G1 PASS; G2 HOLD / NOT CLOSED.
- Searecs/BG Verkehr: G1 PASS; G2 HOLD / NOT CLOSED.
- PROC-001 through PROC-005: G1 PASS; G2 HOLD / NOT CLOSED.
- PROC-006: G1 INSUFFICIENT; no G2.
- IUT-A-01 U2: FULL_PILOT 001 closed `U2-NULL`; no rerun; no positive-utility claim.
- AWS PatchAsgInstance: Phase-A reconstruction CLOSED — PASS at Class-II fixture level; B0 accessibility CLOSED — no admissible resolved difference; B0 permissions audit CLOSED — PARTIAL / effective candidate permission unresolved; downstream candidate/comparator execution separately governed.
- IT-NOSD-010 / ETSI TS 23.502 / 3GPP 5GS: IT-G0 CLOSED — BOUNDED PRE-OUTCOME CASE-DEFINITION PASS; IT-G1 CLOSED — BOUNDED REPRODUCIBILITY / ADMISSION PASS; IT-G2 CLOSED — BOUNDED DOWNSTREAM-SEPARATION PASS; no industrial execution authorization.

## Canonical continuity
`00_GOVERNANCE/CANONICAL_STATE.json` remains the canonical current-state entry point.

Current chain:
`CANONICAL_STATE → RMA → Evidence→Claim Matrix → RMA traceability → STATUS → validator`

Historical experiment and governance records remain immutable. Standing industrial execution authorization: `NONE`.
