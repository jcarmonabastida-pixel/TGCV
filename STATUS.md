# TGCV — Current Status

**Date:** 2026-09-11
**Governance state:** CURRENT — AWS Class-II B0 permissions-audit closure propagated
**Current RMA:** `00_GOVERNANCE/rma/TGCV_RMA_current.md`
**Current Evidence→Claim Matrix:** `00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md`

## Scientific Core
- **Core:** unchanged.
- **TR-132-MOD-1:** `CLOSED — BOUNDED PASS (L3)`.
- No Core primitive, relation, threshold or falsification criterion was modified.
- No scientific claim upgrade was introduced.

## Industrial Track
- **Track status:** `PROPOSED`.
- **IUT-A-01 U2:** `CLOSED — U2-NULL`; FULL_PILOT 001 integrity PASS; M1 PASS; M2 FAIL; no U2-positive decision-performance conclusion.
- **FAA AMOC IT-METH-I:** `CLOSED — INCONCLUSIVE`; historical records immutable.
- **Class-II AWS-PatchAsgInstance Phase A:** `CLOSED — PREDECISION RECONSTRUCTION REPRODUCIBILITY PASS`.
- **Class-II AWS-PatchAsgInstance Phase B0 accessibility:** `CLOSED — NO ADMISSIBLE RESOLVED ACCESSIBILITY DIFFERENCE IDENTIFIED`.
- **Class-II AWS-PatchAsgInstance B0 permissions audit:** `CLOSED — PARTIAL / EFFECTIVE CANDIDATE PERMISSION UNRESOLVED`.
- R001/R002: target and ASG identity agreement `True`; 21/21 exact reconstruction-field agreements; 0 disagreements; 0 unresolved.
- R002 seal: `PASS`; governed reconstruction comparison seal: `PASS`.
- Industrial utility: `UNPROVEN / OPEN`.
- Comparative superiority: `NOT ESTABLISHED`.
- Causality: `NOT ASSESSED`.
- Financial/value effect: `NOT ASSESSED`.

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

## Class-II AWS Phase-A/B0 boundary
- Evidence class: `CLASS II — PUBLIC REPRODUCIBLE FIXTURE`.
- Phase-A result establishes fixture-level reproducibility of the bounded predecision state representation.
- B0 accessibility preflight found no admissible resolved candidate/comparator predicate difference.
- Phase-A contract permits `AutomationAssumeRole` and `LambdaRoleArn` to be omitted when not used.
- Frozen Phase-A role fields are `OMITTED_UNLESS_FROZEN`, not concrete frozen IAM identities.
- `FROZEN_CANDIDATE_ROLE_ARN_PRESENT=False`.
- `IAM_ROLE_AVAILABILITY=UNRESOLVED`.
- `OPERATION_PERMISSION_AVAILABILITY=UNRESOLVED`.
- Comparator caller IAM simulation observed `ssm:SendCommand` as `allowed` under `AmazonSSMFullAccess`; this is simulation evidence only and not end-to-end execution evidence.
- No discovered IAM role was substituted retrospectively.
- Candidate transformation: `NOT AUTHORIZED`.
- Comparator transformation: `NOT AUTHORIZED`.
- No postdecision outcome was used to define predecision state.
- No Class-II → Class-I promotion.

## Methodological closure
- `MR-01` through `MR-07` remain adopted as preconditions for future industrial utility tests.
- The AWS Phase-A reconstruction gate is closed and must not be retroactively altered.
- The B0 accessibility preflight is closed with no admissible resolved difference.
- The B0 permissions audit is closed as an audit operation, while the effective candidate permission dimensions remain unresolved.
- The earlier malformed reconstruction comparison is invalidated as non-evidentiary tooling output.
- No transformation or fixture/IAM mutation was performed in B0.
- IUT-A-01 U2 FULL_PILOT 001 is closed as `U2-NULL`; its frozen evidence and closure audit are canonical experiment records.

## Industrial discovery
- Post-IT-METH-I discovery filter: `FROZEN`.
- AWS Systems Manager Automation / PatchAsgInstance: conditional candidate family; targeted fixture Phase-A/B0 methodological work closed to the extent governed; IT-G1 industrial admission remains open/not granted.
- No industrial execution is authorized by this status.

## Existing routing
- FAA AMOC: G1/G2/G3/G4/G5 completed; comparison and experiment closed `INCONCLUSIVE`.
- LynxOS-178 RSC: G1 PASS; G2 HOLD / NOT CLOSED.
- Searecs/BG Verkehr: G1 PASS; G2 HOLD / NOT CLOSED.
- PROC-001 through PROC-005: G1 PASS; G2 HOLD / NOT CLOSED.
- PROC-006: G1 INSUFFICIENT; no G2.
- IUT-A-01 U2: FULL_PILOT 001 closed `U2-NULL`; no rerun; no positive-utility claim.
- AWS PatchAsgInstance: Phase-A reconstruction CLOSED — PASS at Class-II fixture level; B0 accessibility CLOSED — no admissible resolved difference; B0 permissions audit CLOSED — PARTIAL / effective candidate permission unresolved; downstream candidate/comparator execution separately governed.

## Canonical continuity
`00_GOVERNANCE/CANONICAL_STATE.json` remains the canonical current-state entry point.

Current chain:
`CANONICAL_STATE → RMA → Evidence→Claim Matrix → RMA traceability → STATUS → validator`

Historical experiment and governance records remain immutable. Standing industrial execution authorization: `NONE`.
