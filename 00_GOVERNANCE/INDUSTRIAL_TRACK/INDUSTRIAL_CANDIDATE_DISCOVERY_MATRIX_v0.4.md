# TGCV — Industrial Candidate Discovery Matrix v0.4

**Status:** CURRENT / OPERATIVE — DESIGN-ONLY  
**Execution:** NOT AUTHORIZED  
**Protocol:** `INDUSTRIAL_CANDIDATE_DISCOVERY_PROTOCOL_v0.1.md`

Documentary screening completed. IT-G1 has now been separately applied to ICD-01 and ICD-02. Retention is not admission.

| Candidate | Natural unit / boundary | State reconstructability | Transformation identity | Accessibility observability | Temporal closure | Independent evidence | Downstream separation | Access dependency | Risks | Disposition |
|---|---|---|---|---|---|---|---|---|---|---|
| **ICD-01 BPI-2019 Purchase-item workflow** | One purchase-document line item within the P2P process; case identity is purchase document + item | **PASS-BOUND** | **PASS-CANDIDATE** | **FAIL at IT-G1** — decision-time accessibility/admissibility not independently closed | **PASS** — 2018 coverage | **PASS for case identity; insufficient for accessibility closure** | **PASS-BOUND** | **PASS for initial documentary identifiability** | Alternative accessible actions remain underdetermined | **IT-G1 FAIL — NOT ADMITTED** |
| **ICD-02 BPI-2015 Building-permit workflow** | One building-permit application within one Dutch municipality/process slice | **CONDITIONAL** | **PASS-CANDIDATE** | **FAIL at IT-G1** — exact admissible alternatives not independently closed | **PASS** — multi-year observation | **PASS for case identity; insufficient for accessibility closure** | **PASS-BOUND** | **PASS** for initial documentary identifiability | Rule-change timing and municipal implementation differences; admissible alternatives underdetermined | **IT-G1 FAIL — NOT ADMITTED** |
| **ICD-03 BPI-2014 Change/Incident management** | One IT change record / associated incident | **PASS-CANDIDATE** | **CONDITIONAL** | **CONDITIONAL** | **PASS-CANDIDATE** | **PASS** — public logs | **PASS-CANDIDATE** | **PASS** | Accessibility coupling unresolved | **CONDITIONAL — NOT ADMITTED** |
| **ICD-04 BPI-2020 Travel-permit workflow** | One travel-permit case | **PASS-BOUND** | **CONDITIONAL** | **CONDITIONAL** | **PASS** — 2017–2018 | **PASS** | **PASS-CANDIDATE** | **PASS** | Process changes complicate closure | **CONDITIONAL — NOT ADMITTED** |
| **ICD-05 BPI-2017 Loan-application workflow** | One loan application / associated offers | **PASS-BOUND** | **CONDITIONAL** | **WEAK / OPEN** | **PASS** — 2016–Feb 2017 | **PASS** | **PASS-CANDIDATE** | **PASS** | Multiple event origins | **CONDITIONAL — LOW PRIORITY** |

## Gate result

- Candidate discovery: **COMPLETED — DOCUMENTARY ONLY**
- Retained before IT-G1: **ICD-01, ICD-02**
- IT-G1 reviewed: **ICD-01, ICD-02**
- IT-G1 result: **FAIL / NOT ADMITTED** for both
- No candidate is currently admitted to IT-G2.
- Industrial evidence introduced: **NO**
- Scientific claims changed: **NO**
- Execution authorized: **NO**

## Governance interpretation

The failures of ICD-01 and ICD-02 are candidate-definition/evidence-closure failures at IT-G1, not scientific failures of TGCV. Both candidates have usable case identities and temporal structure, but realized event data do not independently establish the complete decision-time set of admissible alternatives.

No further candidate may advance without separately grounded accessibility closure. A new documentary discovery cycle may be proposed under governance; no dataset execution is implied.
