# IT-NOSD-010 — TR-132 IT-G1 Admission Package 001

**Date:** 2026-09-11  
**Status:** `FROZEN — READY FOR INDEPENDENT REPRODUCIBILITY`  
**Upstream gate:** `IT-G0 CLOSED — BOUNDED PRE-OUTCOME CASE-DEFINITION PASS`  
**IT-G1:** `OPEN — REPRODUCIBILITY EXECUTION PENDING`  
**Industrial execution authorization:** `NONE`

## 1. Scope

This package freezes the single IT-NOSD-010 experimental unit for independent technical reconstruction. It is intentionally limited to provenance, event identity, pre-event state/context, bounded accessibility, transformation identity, temporal closure and realized state transition. No industrial transformation is to be executed.

## 2. Frozen public evidence

Source: T-Mobile Spectrum Usage Dataset, Zenodo record `10.5281/zenodo.19462212`, version 1.0.

Frozen files:
- `tmobile_combined_events.csv` — MD5 `f7f1eb72063ad5ab290817815c55f297`
- `tmobile_combined_spectrum.csv` — MD5 `0796c64f3c8850e5b571ce49c556c50b`

## 3. Frozen event selector

The independent executor must locate exactly:

- session: `T-Mobile_2026.03.28_05.14.11`
- timestamp: `2026-03-28T05:16:15`
- event type: `HANDOVER_DATA_5G5G`
- source cell: `2`
- target cell: `3`
- node: `84246`
- transition: `5G-to-5G`

No replacement event is permitted without a new governance gate.

## 4. Frozen temporal windows

Pre-event window:
`[2026-03-28T05:15:15, 2026-03-28T05:16:15)`

Post-event observation may be inspected only to reconstruct the realized state transition. It must not be used to establish pre-event accessibility/admissibility.

The accessibility predicate uses zero post-event rows.

## 5. Frozen accessibility predicate

Rule ID: `IT-NOSD-010-A1`

Bounded operational rule:

> The target cell is considered pre-outcome observable/accessible for this case if it is observed in spectrum data before the candidate event, within the same session/operator/network context, while the event record independently identifies source and target.

Mandatory conditions:
- target observed before event;
- source and target explicitly identified by event record;
- same session/operator/network context;
- event occurrence not used to establish accessibility;
- no post-event data used for accessibility;
- exhaustive `T_acc(S_t)` enumeration not required under TR-132-MOD-1.

## 6. Frozen pre-event evidence expected

The controlled prior inspection established:
- target cell 3 observed 15 times in the pre-event window;
- first target observation `2026-03-28T05:15:32`;
- `5G NSA`;
- `cell_id=3`;
- `cgi=3102601154500003`;
- `node=84246`;
- `ARFCN=66786`;
- level `-79 dBm`;
- quality `-12 dB`;
- SNR `19 dB`.

These are reference values for integrity checking, not outcome-derived inputs.

## 7. Transformation identity

The bounded candidate transformation is:

`τ_HO = serving-cell / serving-gNB state → target-cell / target-gNB serving state`

The executor must identify the transformation before using any post-event outcome.

## 8. State transition

The realized transition is reconstructed only after the pre-event accessibility predicates have been evaluated. The event record supplies source/target transition identity; post-event state may confirm the realized target serving state.

Accessibility and realized outcome must remain separate fields.

## 9. Independent executor requirements

The executor must:
1. obtain the exact public files;
2. verify both frozen MD5 hashes;
3. locate the exact frozen event;
4. reconstruct the frozen pre-event window;
5. evaluate `IT-NOSD-010-A1` without post-event data;
6. verify transformation identity;
7. verify temporal boundaries;
8. reconstruct the realized transition separately;
9. emit a deterministic JSON result with predicate-level PASS/FAIL;
10. record package/provenance hashes and execution environment.

The executor must not:
- select a different event;
- modify the frozen window;
- infer accessibility from successful occurrence;
- enumerate the complete alternative transformation space;
- introduce a new dataset;
- execute a 3GPP/industrial handover;
- make utility, causal, value or superiority claims.

## 10. Admission decision

IT-G1 can be closed only after an independent execution reproduces all mandatory predicates and the result package is integrity-checked against this frozen package.

Until then:

`IT-G1 = OPEN — REPRODUCIBILITY EXECUTION PENDING`

`INDUSTRIAL EXECUTION AUTHORIZATION = NONE`
