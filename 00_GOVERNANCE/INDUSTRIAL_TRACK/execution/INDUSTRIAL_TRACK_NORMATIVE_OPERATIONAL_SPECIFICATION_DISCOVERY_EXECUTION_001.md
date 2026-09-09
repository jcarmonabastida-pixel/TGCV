# INDUSTRIAL-TRACK — Normative / Operational Specification Discovery — Execution 001

**Execution ID:** IT-NOSD-EXEC-001  
**Date:** 2026-09-09  
**Status:** CLOSED — BOUNDED DOCUMENTARY DISCOVERY  
**Authorization basis:** `INDUSTRIAL_TRACK_NORMATIVE_OPERATIONAL_SPECIFICATION_DISCOVERY_AUTHORIZATION_RECORD_v0.1.md`  
**Protocol:** `INDUSTRIAL_TRACK_NORMATIVE_OPERATIONAL_SPECIFICATION_DISCOVERY_PROTOCOL_v0.1.md`  
**Industrial execution authorization:** NOT GRANTED  

## 1. Scope freeze

This execution was limited to documentary discovery and screening of external normative/operational specifications capable of independently constraining admissible alternatives in an industrial decision context.

Frozen controls:

- maximum 20 distinct candidate specifications screened;
- maximum 10 retained candidates;
- one bounded discovery cycle;
- authoritative primary sources prioritized;
- version/edition and publication/effective information required where available;
- applicability and temporal closure assessed independently of outcomes;
- candidate identity not derived from observed TGCV results;
- no event-log execution, industrial dataset, partner/customer evidence, utility testing, causal analysis, value analysis, Rust/EXT-1.1, O3 rescue, Stage-C/D, Core modification or claim upgrading.

Search was stopped after 13 distinct candidate specifications had been screened because the bounded cross-domain discovery set was sufficient to establish the existence of multiple independently governed normative/operational mechanisms with explicit or operationally determinable alternative/compliance pathways, while further searching would add breadth without changing the immediate governance decision.

This is not an exhaustive literature or standards review.

## 2. Search classes

The frozen search classes were:

1. civil aviation certification/compliance;
2. railway vehicle authorization;
3. maritime technical/operational requirements;
4. telecommunications technical procedures;
5. general regulatory/technical specification sources.

No outcome data were used to select or classify candidates.

## 3. Execution result

**Screened:** 13  
**RETAINED-CANDIDATE:** 10  
**INDETERMINATE:** 0  
**REJECTED:** 3  
**Industrial cases admitted:** 0  
**Utility tested:** no  
**Causal/value analysis:** no  
**Scientific evidence generated:** no  
**Stop-rule violation:** no

## 4. Retained candidate set

The retained candidates are documentary candidates only. Their retention means that the artifact has an identifiable issuer/provenance, version or reconstructable identity, bounded technical/operational scope, and an explicit or operationally determinable mechanism constraining admissible alternatives. It does **not** mean that any candidate satisfies IT-G0 or IT-G1 for a concrete industrial case.

### IT-NOSD-001 — EASA Initial Airworthiness / Environmental Protection — 21.A.134A / 21.B.115

Issuer: European Union Aviation Safety Agency (EASA) / European Commission regulatory framework.  
Version basis: Regulation (EU) 2022/201 and associated EASA Easy Access Rules, revision July 2024.  
Scope: initial airworthiness and environmental protection.  
Alternative mechanism: organisations may use alternative means of compliance, subject to prior submission and competent-authority approval.  
Disposition: `RETAINED-CANDIDATE`.

Primary evidence: EASA Easy Access Rules for Initial Airworthiness and Environmental Protection, July 2024.

### IT-NOSD-002 — EASA Continuing Airworthiness — 145.A.120

Issuer: European Union Aviation Safety Agency / European Commission regulatory framework.  
Version basis: Regulation (EU) 2021/1963 and EASA Easy Access Rules, revision September 2025.  
Scope: continuing airworthiness / maintenance organisations.  
Alternative mechanism: organisations may use alternative means of compliance, with full description and prior competent-authority approval.  
Disposition: `RETAINED-CANDIDATE`.

Primary evidence: EASA Easy Access Rules for Continuing Airworthiness, September 2025.

### IT-NOSD-003 — EASA Air Operations — ARO.GEN.120

Issuer: European Union Aviation Safety Agency / European Commission regulatory framework.  
Version basis: EASA Easy Access Rules for Air Operations, Revision 24, March 2026; Regulation (EU) 2019/1384.  
Scope: civil aviation air operations.  
Alternative mechanism: alternative means of compliance may be used; competent authority evaluates and may approve/revoke/amend them.  
Disposition: `RETAINED-CANDIDATE`.

Primary evidence: EASA Easy Access Rules for Air Operations, Revision 24.

### IT-NOSD-004 — EASA ATM/ANS — ATM/ANS.AR.A.015 and ATM/ANS.OR.A.020

Issuer: European Union Aviation Safety Agency / European Commission regulatory framework.  
Version basis: Regulation (EU) 2017/373 and EASA Easy Access Rules, revision March 2025.  
Scope: air traffic management / air navigation services.  
Alternative mechanism: service providers may use AltMOC to establish compliance, subject to prior description, assessment and approval.  
Disposition: `RETAINED-CANDIDATE`.

Primary evidence: EASA Easy Access Rules for ATM/ANS, March 2025.

### IT-NOSD-005 — FAA AC 20-171 — Alternatives to RTCA/DO-178B

Issuer: Federal Aviation Administration (FAA).  
Version/date: AC 20-171, issued 2011-01-19, active.  
Scope: airborne software certification.  
Alternative mechanism: establishes what an applicant must address when proposing an alternative approach to the recognised software-development assurance method.  
Disposition: `RETAINED-CANDIDATE`.

Primary evidence: FAA AC 20-171 official document page.

### IT-NOSD-006 — FAA AC 39-10 — Alternative Methods of Compliance

Issuer: Federal Aviation Administration (FAA).  
Version/date: AC 39-10, issued 2016-09-14, active.  
Scope: approval of alternative methods of compliance to airworthiness directives.  
Alternative mechanism: explicit AMOC pathway governed by an identified regulatory directive and approval process.  
Disposition: `RETAINED-CANDIDATE`.

Primary evidence: FAA AC 39-10 official document page.

### IT-NOSD-007 — FAA AC 20-148 — Reusable Software Components

Issuer: Federal Aviation Administration (FAA).  
Version/date: AC 20-148, issued 2004-12-07, active.  
Scope: reusable software components in airborne systems and certification projects.  
Alternative mechanism: identifies one acceptable means of compliance while explicitly allowing other means.  
Disposition: `RETAINED-CANDIDATE`.

Primary evidence: FAA AC 20-148 official document page.

### IT-NOSD-008 — ERA-PRG-005/02-361 V1.0 — Practical Arrangements for Vehicle Authorisation

Issuer: European Union Agency for Railways (ERA).  
Version/date: V1.0 [2018-09-21].  
Scope: railway vehicle authorisation.  
Alternative mechanism: documents alternative methods for mandatory national rules and for non-binding requirements, including design demonstration, comparison with a similar authorised vehicle, tests, or risk assessment.  
Disposition: `RETAINED-CANDIDATE`.

Primary evidence: ERA practical-arrangements guideline and document history.

### IT-NOSD-009 — ISO 21745:2019 — Electronic Record Books for Ships

Issuer: International Organization for Standardization (ISO), ISO/TC 8/SC 11.  
Version/date: Edition 1, published 2019-09-03; confirmed current 2025-06-11.  
Scope: electronic record books on ships.  
Constraint mechanism: minimum technical and operational requirements constrain the admissible implementation/design space for the covered operational function.  
Disposition: `RETAINED-CANDIDATE`.

Primary evidence: ISO official standard record.

### IT-NOSD-010 — ETSI TS 23.502 V19.6.0 — 5GS Procedures

Issuer: ETSI / 3GPP SA.  
Version/date: V19.6.0, 2026-01, Release 19.  
Scope: procedures for the 5G System.  
Constraint mechanism: a versioned technical specification defines controlled technical procedures and their applicable conditions, constraining admissible implementations/interactions in the covered telecommunications system.  
Disposition: `RETAINED-CANDIDATE`.

Primary evidence: ETSI official publication PDF.

## 5. Rejected candidates

### IT-NOSD-011 — EASA AMC/AltMoC explanatory overview page

Disposition: `REJECTED`.  
Reason: useful locator and explanatory material, but explicitly informational and not itself the authoritative normative instrument needed when primary regulatory material is available. The underlying EASA regulatory/implementing material is retained instead.

### IT-NOSD-012 — ETSI Version Numbering System

Disposition: `REJECTED`.  
Reason: establishes document/version management conventions but does not itself constrain admissible industrial transformations or operational alternatives in a decision context. It is provenance infrastructure, not the target normative/operational specification.

### IT-NOSD-013 — European Commission TRIS notification analysing regulatory alternatives

Disposition: `REJECTED`.  
Reason: the identified document records a policy-maker's analysis of alternatives for a regulatory change. It does not independently constrain the admissible alternatives available to an industrial decision-maker at execution time and would risk confusing policy-design alternatives with operational accessibility.

## 6. Independence and temporal closure

Candidate identity was established from issuer-controlled or authoritative records. No observed TGCV result, realization, success/failure outcome, utility result, or post-hoc accessibility classification was used to select a candidate.

For the retained candidates, the documentary version/publication state is identifiable. Actual applicability at a future concrete industrial decision time remains a separate case-level question and must be closed before any IT-G1/IT-G2 progression. Later revisions must not be used to reconstruct an earlier decision state.

## 7. Governance disposition

The discovery cycle is **CLOSED — BOUNDED DOCUMENTARY DISCOVERY**.

Ten documentary candidates are retained for possible later case-specific screening. No candidate is admitted as an industrial case by this execution. Any subsequent use must route through the established `IT-G0` → `IT-G1` → `IT-G2` → `IT-G3` → `IT-G4` → `IT-G5` sequence as applicable.

No utility, superiority, causal, predictive, value or scientific-Core claim is changed.

## 8. Source register

- EASA Initial Airworthiness: https://www.easa.europa.eu/en/document-library/easy-access-rules/online-publications/easy-access-rules-initial-airworthiness-and
- EASA Continuing Airworthiness: https://www.easa.europa.eu/en/document-library/easy-access-rules/online-publications/easy-access-rules-continuing-airworthiness
- EASA Air Operations: https://www.easa.europa.eu/en/document-library/easy-access-rules/online-publications/easy-access-rules-air-operations
- EASA ATM/ANS: https://www.easa.europa.eu/en/document-library/easy-access-rules/online-publications/easy-access-rules-atm-ans-regulation-eu
- FAA AC 20-171: https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/698460
- FAA AC 39-10: https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentid/1029790
- FAA AC 20-148: https://www.faa.gov/regulations_policies/advisory_circulars/index.cfm/go/document.information/documentID/22207
- ERA-PRG-005/02-361: https://www.era.europa.eu/system/files/2022-11/guidelines_practical_arrangement_for_va_en_0.pdf
- ISO 21745:2019: https://www.iso.org/standard/71549.html
- ETSI TS 23.502 V19.6.0: https://www.etsi.org/deliver/etsi_ts/123500_123599/123502/19.06.00_60/ts_123502v190600p.pdf

## 9. Final execution status

`EXECUTION_RESULT = CLOSED-BOUNDED-DISCOVERY`  
`SCIENTIFIC_EXECUTION_PERFORMED = false`  
`INDUSTRIAL_EXECUTION_PERFORMED = false`  
`UTILITY_ASSESSMENT_PERFORMED = false`  
`CAUSAL_ANALYSIS_PERFORMED = false`  
`VALUE_ANALYSIS_PERFORMED = false`  
`CORE_MODIFICATION = false`  
`CLAIM_UPGRADE = false`  
`STOP_RULE_VIOLATION = false`
