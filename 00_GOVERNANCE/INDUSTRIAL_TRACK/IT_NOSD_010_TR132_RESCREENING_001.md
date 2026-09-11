# IT-NOSD-010 — TR-132 Corrected Re-Screening 001

**Date:** 2026-09-11  
**Status:** `IT-G0 CLOSED — BOUNDED PASS; IT-G1 NOT STARTED`  
**Candidate:** ETSI TS 23.502 / 3GPP 5GS procedures  
**Normative dependency:** `TR-132-MOD-1 — CLOSED / BOUNDED PASS (L3)`  
**Screening basis:** `INDUSTRIAL_CANDIDATE_DISCOVERY_PROTOCOL_v0.2.md`

## 1. Purpose

Re-screen IT-NOSD-010 under the corrected TR-132 accessibility-sufficiency rule. This record replaces the earlier interpretation that absence of exhaustive ex-ante alternative-space enumeration was sufficient to fail accessibility screening.

## 2. Candidate unit under consideration

A single 5G-to-5G handover event recorded in a public measurement dataset is the candidate event-level unit. The T-Mobile Spectrum Usage Dataset published in Zenodo contains event measurements including 5G-to-5G handovers together with spectrum measurements such as frequency band, RSRP and RSRQ, associated with location and elevation.

The candidate is therefore not the TS 23.502 document itself and not a generic class of handovers. The unit is one bounded observed handover event plus its pre-event measurement/context window.

## 3. TR-132 assessment

### 3.1 Complete alternative-space reconstruction

`T_acc(S_t)` is **not assumed to be completely enumerable** from the public measurement record.

This is **not a rejection criterion** under TR-132-MOD-1.

### 3.2 Relevant transformation

Candidate transformation:

`τ_HO = serving-cell / serving-gNB state → target-cell / target-gNB serving state`

For the frozen event, the recorded transformation is `5G cell 2 → 5G cell 3` on node `84246`.

### 3.3 Pre-outcome accessibility evidence

The concrete accessibility gate `IT-NOSD-010-A1` is now closed with `PASS`. The target cell `3` was observed in the same session/operator/network before the candidate event, with `15` pre-outcome observations; first observation was `2026-03-28T05:15:32`, before the handover at `05:16:15`.

Accessibility was established without using post-event rows (`0` considered) and without using the occurrence or outcome of the handover to define accessibility.

### 3.4 Outcome independence

The accessibility predicate is based only on pre-event observations and the event's independently recorded source/target identity. Post-handover success, continuity or performance is not used to define the admissible transformation space.

### 3.5 State transition

The frozen event and pre-state provide a reconstructable bounded transition for the candidate. The detailed frozen closure is recorded in `IT_NOSD_010_TR132_IT_G0_CLOSURE_001.md`.

## 4. Filter assessment after controlled closure

| Filter | Result | Rationale |
|---|---|---|
| F1 Natural boundary | `PASS` | One recorded handover event forms a bounded unit. |
| F2 State reconstructability | `PASS — BOUNDED` | Frozen event and pre-state support the bounded transition. |
| F3 Transformation identity | `PASS` | Source/target and 5G-to-5G identity are explicit. |
| F4 Accessibility sufficiency | `PASS — BOUNDED` | Concrete pre-outcome criterion A1 is satisfied without exhaustive `T_acc`. |
| F5 Temporal closure | `PASS — BOUNDED` | Explicit finite pre-event window is frozen. |
| F6 Evidence independence | `PASS` at documentary level | Public dataset and public normative specification are independent of TGCV interpretation. |
| F7 Downstream separation | `PASS — BOUNDED` | Accessibility uses no post-event rows; downstream outcomes remain outside the gate. |
| F8 Access robustness | `PASS` | Public dataset/specification; no partner access is required for this gate. |
| F9 Natural experimental unit | `PASS` | Individual handover event is the concrete candidate unit. |
| F10 Public reproducibility | `PASS — BOUNDED` | Exact record, files and hashes are frozen; further reproducibility is an IT-G1 concern. |
| F11 Outcome separation | `PASS — BOUNDED` | Accessibility is established independently of downstream outcome. |
| F12 Industrial relevance | `PROMISING` | 5GS mobility/handover remains operationally relevant; no utility claim is made. |

## 5. Decision

**Disposition: `IT-G0 CLOSED — BOUNDED PASS`.**

The corrected TR-132 rule removes the previous completeness-based obstacle, and the concrete candidate has now satisfied the bounded pre-outcome case-definition/accessibility gate.

This record does **not** constitute IT-G1 admission, industrial evidence, utility evidence, causal evidence, value evidence, comparative superiority or scientific validation.

## 6. Frozen evidence

- `IT_NOSD_010_TR132_IT_G0_CLOSURE_001.md`
- `IT_NOSD_010_TR132_CASE_DEFINITION_GATE_001.md`
- Accessibility executor commit: `4188976803bfbdd638c44f526660563d3e8cb201`
- Events file MD5: `f7f1eb72063ad5ab290817815c55f297`
- Spectrum file MD5: `0796c64f3c8850e5b571ce49c556c50b`

## 7. Next controlled gate

Before IT-G1 admission, verify reproducibility/provenance of the frozen event, bounded state-transition reconstruction, temporal closure, transformation/accessibility separation from downstream outcome, and the exact evidence package required for independent reproduction.

If these conditions cannot be closed, the case remains conditional or indeterminate; the TR-132 rule must not be weakened to rescue it.

## 8. Governance boundary

- `IT-G0 = CLOSED — BOUNDED PASS`.
- `IT-G1 = NOT STARTED`.
- `INDUSTRIAL EXECUTION AUTHORIZATION = NONE`.
- `DATASET EXECUTION = NOT AUTHORIZED`.
- `UTILITY / CAUSAL / VALUE ASSESSMENT = NOT AUTHORIZED`.
- `TGCV SCIENTIFIC CORE = UNCHANGED`.
