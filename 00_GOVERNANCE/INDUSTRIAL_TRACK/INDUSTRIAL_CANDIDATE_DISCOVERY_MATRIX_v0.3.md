# TGCV — Industrial Candidate Discovery Matrix v0.3

**Status:** CURRENT / OPERATIVE — DESIGN-ONLY  
**Execution:** NOT AUTHORIZED  
**Protocol:** `INDUSTRIAL_CANDIDATE_DISCOVERY_PROTOCOL_v0.1.md`

Documentary screening completed. IT-G1 has now been separately applied to ICD-01. Retention is not admission.

| Candidate | Natural unit / boundary | State reconstructability | Transformation identity | Accessibility observability | Temporal closure | Independent evidence | Downstream separation | Access dependency | Risks | Disposition |
|---|---|---|---|---|---|---|---|---|---|---|
| **ICD-01 BPI-2019 Purchase-item workflow** | One purchase-document line item within the P2P process; case identity is purchase document + item | **PASS-BOUND** | **PASS-CANDIDATE** | **FAIL at IT-G1** — decision-time accessibility/admissibility not independently closed | **PASS** — 2018 coverage | **PASS for case identity; insufficient for accessibility closure** | **PASS-BOUND** | **PASS for initial documentary identifiability** | Alternative accessible actions remain underdetermined | **IT-G1 FAIL — NOT ADMITTED** |
| **ICD-02 BPI-2015 Building-permit workflow** | One building-permit application within one Dutch municipality/process slice | **PASS-BOUND** | **PASS-CANDIDATE** | **CONDITIONAL** — exact admissible alternatives require separate IT-G1 closure | **PASS** — multi-year observation | **PASS** — public event log, resources and costs | **PASS-CANDIDATE** | **PASS** for initial documentary identifiability | Rule-change timing and municipal implementation differences | **RETAIN — NOT ADMITTED** |
| **ICD-03 BPI-2014 Change/Incident management** | One IT change record / associated incident | **PASS-CANDIDATE** | **CONDITIONAL** | **CONDITIONAL** | **PASS-CANDIDATE** | **PASS** — public logs | **PASS-CANDIDATE** | **PASS** | Accessibility coupling unresolved | **CONDITIONAL — NOT ADMITTED** |
| **ICD-04 BPI-2020 Travel-permit workflow** | One travel-permit case | **PASS-BOUND** | **CONDITIONAL** | **CONDITIONAL** | **PASS** — 2017–2018 | **PASS** | **PASS-CANDIDATE** | **PASS** | Process changes complicate closure | **CONDITIONAL — NOT ADMITTED** |
| **ICD-05 BPI-2017 Loan-application workflow** | One loan application / associated offers | **PASS-BOUND** | **CONDITIONAL** | **WEAK / OPEN** | **PASS** — 2016–Feb 2017 | **PASS** | **PASS-CANDIDATE** | **PASS** | Multiple event origins | **CONDITIONAL — LOW PRIORITY** |

## Screening and gate result

- Candidate discovery: **COMPLETED — DOCUMENTARY ONLY**
- Retained before IT-G1: **ICD-01, ICD-02**
- IT-G1 reviewed: **ICD-01**
- IT-G1 result: **FAIL / NOT ADMITTED**
- Remaining retained candidate: **ICD-02 — NOT ADMITTED**
- Industrial evidence introduced: **NO**
- Scientific claims changed: **NO**
- Execution authorized: **NO**

## Governance interpretation

ICD-01's failure is a candidate-definition/evidence-closure failure at IT-G1, not a scientific failure of TGCV. The case is naturally bounded, but realized event data do not independently establish the complete decision-time set of admissible alternatives.

ICD-02 remains available for a separate IT-G1 review only if governance authorizes it. No candidate is currently admitted to IT-G2 and no dataset execution is authorized.
