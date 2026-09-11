# TGCV — Industrial Candidate Discovery Matrix v0.5

**Date:** 2026-09-11  
**Status:** CURRENT / OPERATIVE — DESIGN-ONLY  
**Supersedes:** `INDUSTRIAL_CANDIDATE_DISCOVERY_MATRIX_v0.4.md`  
**Protocol:** `INDUSTRIAL_CANDIDATE_DISCOVERY_PROTOCOL_v0.2.md`

## TR-132 screening correction

This matrix incorporates TR-132-MOD-1. **Complete ex-ante reconstruction of `T_acc(S_t)` is not a mandatory retention criterion.** Accessibility screening concerns whether the candidate transformation can be identified and its admissibility/accessibility assessed from pre-outcome state/context.

| Candidate | Natural unit / boundary | State reconstructability | Transformation identity | Accessibility sufficiency | Alternative-space completeness | Outcome-independent evidence | Disposition |
|---|---|---|---|---|---|---|---|
| ICD-01 BPI-2019 Purchase-item workflow | Purchase-document line item | PASS-BOUND | PASS-CANDIDATE | Historical IT-G1 FAIL; prior basis requires re-audit if completeness criterion was material | Historical record not reclassified | Historical evidence preserved | **HISTORICAL — REVIEW ELIGIBILITY PENDING** |
| ICD-02 BPI-2015 Building-permit workflow | Building-permit application / municipality slice | PASS-BOUND | PASS-CANDIDATE | Historical IT-G1 FAIL; prior basis requires re-audit if completeness criterion was material | Historical record not reclassified | Historical evidence preserved | **HISTORICAL — REVIEW ELIGIBILITY PENDING** |
| ICD-03 BPI-2014 Change/Incident management | IT change / incident | PASS-CANDIDATE | CONDITIONAL | To be assessed under v0.2 | Unknown/partial permitted if non-material | To be assessed | CONDITIONAL — NOT ADMITTED |
| ICD-04 BPI-2020 Travel-permit workflow | Travel-permit case | PASS-BOUND | CONDITIONAL | To be assessed under v0.2 | Unknown/partial permitted if non-material | To be assessed | CONDITIONAL — NOT ADMITTED |
| ICD-05 BPI-2017 Loan-application workflow | Loan application / offers | PASS-BOUND | CONDITIONAL | To be assessed under v0.2 | Unknown/partial permitted if non-material | To be assessed | CONDITIONAL — NOT ADMITTED |
| ICD-06 Road Traffic Fine Management | One traffic fine | PASS-BOUND | PASS-CANDIDATE | Prior failure included unavailable contextual factors; remains unresolved independently of completeness issue | Partial/unknown alone is not disqualifying | To be assessed | **HISTORICAL DISCARD — NO AUTOMATIC REOPENING** |
| ICD-07 Hospital Sepsis pathway | One patient pathway | PASS | CONDITIONAL | Prior failure also involved evolving clinical state/judgement; no automatic reopening | Partial/unknown alone is not disqualifying | To be assessed | **HISTORICAL DISCARD — NO AUTOMATIC REOPENING** |
| ICD-08 BPI-2017 decision process | One loan application | PASS-BOUND | PASS-CANDIDATE | Prior non-retention specifically cited incomplete ex-ante accessibility; therefore eligible for corrected re-screening | Partial/unknown permitted subject to materiality test | To be reassessed | **ELIGIBLE FOR RE-SCREENING** |
| IT-NOSD-010 ETSI TS 23.502 / 3GPP 5GS | Case-specific 5GS procedure/event | Promising | Promising | Requires concrete event-level assessment; complete alternative enumeration not required | Potentially partial | Pending case evidence | **ELIGIBLE FOR RE-SCREENING** |

## Mandatory new screening fields

Every future candidate record must include:

- `TR132_APPLICABILITY`
- `OBSERVED_TRANSFORMATION_IDENTIFIED`
- `PRE_OUTCOME_ACCESSIBILITY_EVIDENCE`
- `ACCESSIBILITY_OUTCOME_INDEPENDENT`
- `ALTERNATIVE_SPACE_COMPLETENESS` = `COMPLETE / PARTIAL / UNKNOWN`
- `ALTERNATIVE_SPACE_INCOMPLETENESS_MATERIAL` = `YES / NO / UNDETERMINED`
- `STATE_TRANSITION_RECONSTRUCTABLE`

## Governance consequence

This matrix does not admit any candidate to IT-G1 and authorizes no execution. It establishes the corrected screening basis for subsequent discovery/re-screening.
