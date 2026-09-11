# IT-NOSD-010 — TR-132 Case Definition Gate 001

**Date:** 2026-09-11  
**Status:** `CLOSED — BOUNDED PASS / IT-G0`  
**Candidate:** ETSI TS 23.502 / 3GPP 5GS procedures  
**Parent screening:** `IT_NOSD_010_TR132_RESCREENING_001.md`

## 1. Controlled objective

Define one concrete, publicly reproducible 5G handover event that can be screened under TR-132 without requiring exhaustive ex-ante reconstruction of `T_acc(S_t)`.

## 2. Preferred public evidence source

The **T-Mobile Spectrum Usage Dataset**, Zenodo record `10.5281/zenodo.19462212`, is retained as the preferred source because its public description explicitly reports both spectrum measurements (including frequency band, RSRP and RSRQ) and event measurements including **5G-to-5G handover**, with measurements associated with latitude, longitude and elevation. The record was published 2026-04-07, version 1.0.

Frozen file identities:

- events CSV MD5: `f7f1eb72063ad5ab290817815c55f297`
- spectrum CSV MD5: `0796c64f3c8850e5b571ce49c556c50b`

## 3. Frozen candidate event

A qualifying event has now been identified and frozen:

- session: `T-Mobile_2026.03.28_05.14.11`
- timestamp: `2026-03-28T05:16:15`
- event: `HANDOVER_DATA_5G5G`
- source cell: `2`
- target cell: `3`
- source/target node: `84246`
- transition: `5G-to-5G`

The bounded pre-event observation window is `[2026-03-28T05:15:15, 2026-03-28T05:16:15)`.

## 4. Required evidence closure — result

The controlled inspection established:

- exact candidate event identity: `PASS`;
- serving/source state identifiable before the event: `PASS`;
- target cell identifiable before the event: `PASS`;
- target cell observed 15 times in the pre-event window: `PASS`;
- first target observation: `2026-03-28T05:15:32`;
- first target observation: `5G NSA`, `cell_id=3`, `cgi=3102601154500003`, `node=84246`, `ARFCN=66786`, `level=-79 dBm`, `qual=-12 dB`, `SNR=19 dB`;
- pre-outcome accessibility under rule `IT-NOSD-010-A1`: `PASS`;
- post-event rows considered for accessibility: `0`;
- outcome used to establish accessibility: `false`;
- state transition reconstructable from frozen event and pre-state: `PASS`;
- complete `T_acc(S_t)` enumeration required: `false`.

The accessibility result is frozen in:

`IT_NOSD_010_TR132_IT_G0_CLOSURE_001.md`

The technical accessibility executor is:

`00_GOVERNANCE/INDUSTRIAL_TRACK/execution/it_nosd_010_accessibility_gate_v01.py`

Executor commit: `4188976803bfbdd638c44f526660563d3e8cb201`.

## 5. TR-132 rule

Failure to enumerate every alternative handover available at the pre-event state is **not**, by itself, a failure. The decisive question is whether the observed candidate transformation `τ_i` has independently assessable pre-outcome accessibility/admissibility and a reconstructable state transition.

## 6. Gate decision

`CASE_DEFINITION = CLOSED — BOUNDED PASS`

`IT-G0 = CLOSED — BOUNDED PASS`

`IT-G1 = NOT STARTED`

`INDUSTRIAL EXECUTION AUTHORIZATION = NONE`

## 7. Interpretation boundary

This gate closes the methodological case-definition/accessibility sufficiency requirement for the concrete candidate event. It does not establish full normative 3GPP admissibility, complete `T_acc(S_t)`, industrial utility, causal effect, value effect, comparative superiority, or scientific validation.

No dataset execution beyond the documented technical inspection is authorized by this record.

## 8. Next controlled gate

The next operation is the separately governed **IT-G1 admission/reproducibility gate** for this single frozen event. IT-G1 must verify reproducibility/provenance, pre-event state and transformation identity, state-transition closure, temporal closure, and explicit separation of transformation/accessibility from downstream outcome. IT-G1 does not authorize industrial execution by itself.
