# IT-NOSD-010 — TR-132 Case Definition Gate 001

**Date:** 2026-09-11  
**Status:** `OPEN — CASE DEFINITION EVIDENCE PENDING`  
**Candidate:** ETSI TS 23.502 / 3GPP 5GS procedures  
**Parent screening:** `IT_NOSD_010_TR132_RESCREENING_001.md`

## 1. Controlled objective

Define one concrete, publicly reproducible 5G handover event that can be screened under TR-132 without requiring exhaustive ex-ante reconstruction of `T_acc(S_t)`.

## 2. Preferred public evidence source

The **T-Mobile Spectrum Usage Dataset**, Zenodo record `10.5281/zenodo.19462212`, is retained as the preferred source because its public description explicitly reports both spectrum measurements (including frequency band, RSRP and RSRQ) and event measurements including **5G-to-5G handover**, with measurements associated with latitude, longitude and elevation. The record was published 2026-04-07, version 1.0.

The dataset contains a combined events CSV and separate drive-event/spectrum files. Source identity must be frozen before any event-level reconstruction.

## 3. Candidate event definition

A candidate case shall be exactly one recorded `5G-to-5G handover` event plus a bounded pre-event observation window and the immediately corresponding post-event state needed only to establish the state transition.

The candidate must not be defined by post-event performance, success, throughput, continuity or other downstream outcome.

## 4. Required evidence closure

The next controlled inspection must establish, from the frozen public record:

- exact event row / event identifier;
- timestamp and bounded pre-event window;
- serving and target cell identity, where available;
- pre-event radio/context variables;
- whether the relevant target transformation is identifiable before the outcome;
- whether accessibility/admissibility can be evaluated from pre-event information;
- post-event state sufficient to reconstruct the transition;
- exact file/version/hash provenance.

## 5. TR-132 rule

Failure to enumerate every alternative handover available at the pre-event state is **not**, by itself, a failure. The decisive question is whether the observed candidate transformation `τ_i` has independently assessable pre-outcome accessibility/admissibility and a reconstructable state transition.

## 6. Current gate decision

`CASE_DEFINITION = PENDING EVIDENCE INSPECTION`

`IT-G0 = NOT STARTED`

`IT-G1 = NOT STARTED`

`INDUSTRIAL EXECUTION AUTHORIZATION = NONE`

No dataset download, event selection, scoring, utility assessment, causal assessment or value assessment is authorized by this record.

## 7. Next operation

Inspect the public event file and freeze the first event that satisfies the above identity/provenance requirements. If no event permits the required pre-outcome reconstruction, the candidate remains conditional or is discarded; do not relax TR-132 to rescue the candidate.
