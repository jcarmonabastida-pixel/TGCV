# TGCV — C09 New-Domain Public Operational Data Screen 001

**Status:** `COMPLETED — CHESS SELECTED FOR FOCUSED TR-132 PROVENANCE AUDIT / EXECUTION NOT AUTHORIZED`
**Date:** 2026-09-13
**Purpose:** identify a candidate with genuinely public individual-level operational data after the Santiago blocker

## 1. Screening criterion

The candidate must combine:

- credible randomized intervention;
- intervention that plausibly changes accessibility to a bounded transformation class;
- public individual-level data including treatment assignment and outcomes;
- enough intervention documentation to attempt an explicit `T_acc,0/T_acc,1` reconstruction;
- no assumed restricted-data access.

## 2. Screened candidates

### CHESS digital hypertension-management RCT — SELECTED FOR FOCUSED AUDIT

A Dryad record published 7 August 2026 provides a raw individual-level CSV with 1,666 records from the CHESS evaluation trial, including baseline characteristics, follow-up outcomes and treatment assignment. The record states that the de-identified data are publicly released with participant consent. citeturn2search0

This materially improves the provenance situation relative to the previously screened transport and lottery candidates.

The remaining scientific question is narrower: whether the CHESS intervention can be represented as a bounded change in accessible transformations rather than merely as a treatment-arm indicator, and whether the intervention protocol supplies an ex-ante rule sufficient to define `T_acc,0/T_acc,1` without using realized outcomes.

### Other screened public RCT datasets

Several public RCT datasets were found, including TIMCI Tanzania and other clinical/behavioural trials. Their public availability is useful, but the intervention-to-accessibility mapping is less direct than CHESS for the present C09 question. citeturn2search13turn2search4

Records whose data are restricted, embargoed, or approval-only are excluded from this discovery path. citeturn2search5turn2search7

## 3. Decision

**NEW-DOMAIN SCREEN = CHESS SELECTED FOR FOCUSED TR-132 PROVENANCE AUDIT.**

This is a candidate selection decision only. It does not establish C09 evidence and does not authorize execution.

The focused audit must determine whether the digital intervention creates an explicit, bounded accessibility-state contrast that can be reconstructed from the public dataset and intervention specification.

No treatment assignment may be substituted for `T_acc` unless the intervention rule itself establishes the correspondence.
No outcome-derived variable may define accessibility.
No restricted data may be assumed.

**Next operation:** `C09 CHESS TR-132 data/intervention provenance audit 001`.
