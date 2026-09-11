# IT-NOSD-010 — TR-132 Corrected Re-Screening 001

**Date:** 2026-09-11  
**Status:** `CONDITIONAL — RETAIN FOR IT-G0 CASE DEFINITION; IT-G1 NOT STARTED`  
**Candidate:** ETSI TS 23.502 / 3GPP 5GS procedures  
**Normative dependency:** `TR-132-MOD-1 — CLOSED / BOUNDED PASS (L3)`  
**Screening basis:** `INDUSTRIAL_CANDIDATE_DISCOVERY_PROTOCOL_v0.2.md`

## 1. Purpose

Re-screen IT-NOSD-010 under the corrected TR-132 accessibility-sufficiency rule. This record replaces the earlier interpretation that absence of exhaustive ex-ante alternative-space enumeration was sufficient to fail accessibility screening.

## 2. Candidate unit under consideration

A single 5G-to-5G handover event recorded in a public measurement dataset is a candidate event-level unit. The T-Mobile Spectrum Usage Dataset published in Zenodo contains event measurements including 5G-to-5G handovers together with spectrum measurements such as frequency band, RSRP and RSRQ, associated with location and elevation.

The candidate is therefore not the TS 23.502 document itself and not a generic class of handovers. The proposed unit is one bounded observed handover event plus its pre-event measurement/context window.

## 3. TR-132 assessment

### 3.1 Complete alternative-space reconstruction

`T_acc(S_t)` is **not assumed to be completely enumerable** from the public measurement record.

This is **not a rejection criterion** under TR-132-MOD-1.

### 3.2 Relevant transformation

Candidate transformation:

`τ_HO = serving-cell / serving-gNB state → target-cell / target-gNB serving state`

The transformation identity can be anchored to the recorded handover event and corresponding serving/target identifiers or measurements where available.

### 3.3 Pre-outcome accessibility evidence

The screening question is whether the conditions preceding the event provide sufficient information to assess that the observed handover transformation was accessible/admissible, without defining accessibility from the fact that the handover subsequently occurred.

Public measurement data provide pre-event radio measurements and event records. TS 23.502 provides the normative procedural structure for 5GS mobility. The combination is promising but does not yet establish full case-level admissibility.

### 3.4 Outcome independence

A handover event itself is the observed transformation, not the definition of accessibility. The screening must use only measurements/context available before the handover event to establish relevant preconditions. Post-handover success, continuity or performance must not be used to define the admissible transformation space.

### 3.5 State transition

The candidate has a naturally bounded before/after transition if serving and target state can be reconstructed around the event. This remains to be demonstrated at the concrete dataset-record level before IT-G1.

## 4. Filter assessment

| Filter | Result | Rationale |
|---|---|---|
| F1 Natural boundary | `PROMISING` | One recorded handover event can form a bounded unit. |
| F2 State reconstructability | `CONDITIONAL` | Pre/post radio/context variables are available, but event-level sufficiency must be verified. |
| F3 Transformation identity | `PROMISING` | Handover transformation is procedurally defined and event-observable. |
| F4 Accessibility sufficiency | `CONDITIONAL` | Can be assessed for the observed transformation without exhaustive `T_acc`; concrete pre-event variables must be mapped. |
| F5 Temporal closure | `PROMISING` | Dataset timestamps and a finite pre/post window are available. |
| F6 Evidence independence | `PASS` at documentary level | Public dataset and public normative specification are independent of TGCV interpretation. |
| F7 Downstream separation | `CONDITIONAL` | Outcome/performance must remain separate from transformation and accessibility. |
| F8 Access robustness | `PASS` | Public dataset/specification; no partner access is logically required for screening. |
| F9 Natural experimental unit | `PROMISING` | Individual handover event is a concrete candidate unit. |
| F10 Public reproducibility | `CONDITIONAL` | Dataset is public, but exact event-level reconstruction must be demonstrated. |
| F11 Outcome separation | `CONDITIONAL` | Must freeze pre-event accessibility evidence before using downstream outcome data. |
| F12 Industrial relevance | `PROMISING` | 5GS mobility/handover is an operational telecom process. |

## 5. Decision

**Disposition: `CONDITIONAL — RETAIN FOR IT-G0 CASE DEFINITION`.**

The corrected TR-132 rule removes the previous completeness-based obstacle. IT-NOSD-010 is therefore not discarded.

This record does **not** constitute IT-G1 admission, industrial evidence, utility evidence or scientific validation.

## 6. Required next controlled gate

Before IT-G1, select and freeze one concrete public handover event and verify:

1. exact dataset version/record identity;
2. pre-event state/context window;
3. transformation identity;
4. pre-outcome accessibility/admissibility evidence;
5. independence of that accessibility assessment from post-event outcome;
6. reconstructable state transition;
7. temporal closure;
8. separation of transformation, Reach/trajectory and downstream outcome.

If these conditions cannot be closed, discard or classify the candidate as indeterminate without weakening the TR-132 rule.

## 7. Governance boundary

- `IT-G0 = NOT STARTED` — case definition gate remains pending.
- `IT-G1 = NOT STARTED`.
- `INDUSTRIAL EXECUTION AUTHORIZATION = NONE`.
- `DATASET EXECUTION = NOT AUTHORIZED`.
- `UTILITY / CAUSAL / VALUE ASSESSMENT = NOT AUTHORIZED`.
- `TGCV SCIENTIFIC CORE = UNCHANGED`.
