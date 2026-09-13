# TGCV — C09 Chicago Accessibility Data Provenance Audit 001

**Status:** `COMPLETED — OPERATIONAL REPRODUCIBILITY FAILED / CANDIDATE CLOSED FOR EXECUTION`
**Date:** 2026-09-13
**Candidate:** Chicago Housing Voucher Lottery (CHAC, 1997)
**Parent:** `TGCV_C09_CHICAGO_VOUCHER_TR132_OPERATIONAL_PREFLIGHT_001.md`
**Execution authorization:** `NONE`

## 1. Purpose

Determine whether legitimately accessible public/replication materials are sufficient to reconstruct the household-level bounded accessibility representation required by TR-132 and C09, without restricted administrative data.

## 2. Provenance findings

### A — Lottery application / assignment data

**NOT PUBLICLY REPRODUCIBLE AS RAW HOUSEHOLD DATA.**

The published research identifies CHAC 1997 application files as the source for lottery number, baseline address and household information. The underlying research materials are described as CHAC application files rather than a public microdata release. citeturn0search24turn1search27

### B — Voucher utilization / lease-up

**REPLICATION MATERIALS EXIST, BUT NOT AS THE REQUIRED ACCESSIBILITY SPACE.**

OpenICPSR hosts a replication package for Jacob & Ludwig (2012), including programs and derived analysis files. citeturn1search0turn1search8

However, the published data construction relies on HUD 50058 administrative records for voucher utilization, and the underlying source is described as restricted-use administrative data. citeturn0search25turn0search24

### C — Residential location

**CRITICAL FAILURE FOR C09 PUBLIC RECONSTRUCTION.**

The Chicago research reconstructs residential location using passive tracking sources such as NCOA and credit-bureau checks; in one major analysis only a random 10% subsample was tracked. Residential locations were then combined with census geography to characterize neighborhoods. citeturn0search24

A later Chicago voucher study reports residential-location information at voucher offer for approximately half of the sample and explicitly states that these address data came from public-assistance records. citeturn2search0

These are research-infrastructure variables, not an established public-use household-level dataset from which TGCV can reconstruct `T_acc,0/T_acc,1` for the full declared unit universe.

### D — Longitudinal outcomes

**STRONG BUT RESTRICTED.**

The literature demonstrates rich longitudinal outcome construction: UI earnings, public-assistance records, arrests, school records and other administrative outcomes. citeturn2search0turn1search6

The relevant source data are administrative datasets; the replication package contains derived files/code but does not establish unrestricted access to the underlying linked household-level administrative records. The AER replication documentation also labels key source files as restricted use. citeturn0search25turn1search0

## 3. TR-132 sufficiency consequence

TR-132 requires that the bounded `U*` representation be sufficient for the declared causal contrast and reproducibly reconstructible at the unit level.

Chicago fails the operational reproducibility condition because:

1. the lottery application source is not established as public household microdata;
2. voucher utilization depends on HUD administrative records;
3. residential location is reconstructed from administrative/passive-tracking sources and is not available as a complete public unit-level accessibility representation;
4. the longitudinal outcome linkage also depends on restricted administrative sources.

The existence of public replication code and derived analysis material does **not** satisfy these conditions. citeturn1search0turn1search5

## 4. No-go decisions

The following substitutions are rejected:

- lottery number/offer as a proxy for `T_acc`;
- lease-up as `T_acc`;
- realized destination as ex-ante accessible transformation space;
- baseline tract characteristics as the treatment-induced accessibility contrast;
- replication-derived aggregate statistics as household-level `T_acc`;
- restricted administrative data without a new governed access pathway.

## 5. Final disposition

**CHICAGO = CLOSED FOR C09 CAUSAL EXECUTION.**

This is an operational closure, not a rejection of the scientific design or of the empirical value of the Chicago experiment.

Chicago remains a **strong methodological reference** for randomized accessibility/intervention designs and longitudinal trajectory measurement.

No causal execution.
No restricted-data request.
No claim-matrix upgrade.
No Core change.
No execution authorization.

## 6. Next candidate

The next ranked candidate under the retrospective TR-132 review is:

**NYCHANS Affordable-Housing — dedicated TR-132 operational preflight.**
