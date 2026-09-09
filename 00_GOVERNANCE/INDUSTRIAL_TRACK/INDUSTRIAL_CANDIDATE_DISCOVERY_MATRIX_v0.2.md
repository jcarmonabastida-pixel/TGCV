# TGCV — Industrial Candidate Discovery Matrix v0.2

**Status:** CURRENT / OPERATIVE — DESIGN-ONLY  
**Execution:** NOT AUTHORIZED  
**Protocol:** `INDUSTRIAL_CANDIDATE_DISCOVERY_PROTOCOL_v0.1.md`

Documentary screening completed. Retention is not IT-G1 admission.

| Candidate | Natural unit / boundary | State reconstructability | Transformation identity | Accessibility observability | Temporal closure | Independent evidence | Downstream separation | Access dependency | Risks | Disposition |
|---|---|---|---|---|---|---|---|---|---|---|
| **ICD-01 BPI-2019 Purchase-item workflow** | One purchase-document line item within the P2P process of a multinational coatings/paints company; case identity is purchase document + item | **PASS-BOUND** | **PASS-CANDIDATE** — state-changing workflow actions can be defined independently of outcome | **CONDITIONAL** — contextual constraints observable; decision-time accessibility requires IT-G1 closure | **PASS** — 2018 coverage | **PASS** — public event log and contextual attributes | **PASS-CANDIDATE** | **PASS** for initial documentary identifiability | Alternative accessible actions may remain underdetermined; dataset scale | **RETAIN — PRIORITY** |
| **ICD-02 BPI-2015 Building-permit workflow** | One building-permit application within one Dutch municipality/process slice | **PASS-BOUND** | **PASS-CANDIDATE** — procedure/rule-driven actions independently describable | **CONDITIONAL** — exact admissible alternatives require IT-G1 closure | **PASS** — multi-year observation | **PASS** — public event log, resources and costs | **PASS-CANDIDATE** | **PASS** for initial documentary identifiability | Rule-change timing and municipal implementation differences | **RETAIN** |
| **ICD-03 BPI-2014 Change/Incident management** | One IT change record / associated incident | **PASS-CANDIDATE** | **CONDITIONAL** — implementation change may be a transformation, but transformation space is not yet closed | **CONDITIONAL** | **PASS-CANDIDATE** | **PASS** — public logs | **PASS-CANDIDATE** | **PASS** | Coupling change records to accessible alternatives may be insufficient | **CONDITIONAL** |
| **ICD-04 BPI-2020 Travel-permit workflow** | One travel-permit case | **PASS-BOUND** | **CONDITIONAL** — workflow actions identifiable, but accessible alternatives remain open | **CONDITIONAL** | **PASS** — 2017–2018 | **PASS** — public event log/process description | **PASS-CANDIDATE** | **PASS** | Process changes and estimated travel dates complicate closure | **CONDITIONAL** |
| **ICD-05 BPI-2017 Loan-application workflow** | One loan application / associated offers | **PASS-BOUND** | **CONDITIONAL** — system/process change may confound identity | **WEAK / OPEN** | **PASS** — 2016–Feb 2017 | **PASS** — public event log | **PASS-CANDIDATE** | **PASS** | Multiple event origins and weak accessibility closure | **CONDITIONAL — LOW PRIORITY** |

## Screening result

- Candidate discovery: **COMPLETED — DOCUMENTARY ONLY**
- Retained: **ICD-01, ICD-02**
- Conditional: **ICD-03, ICD-04, ICD-05**
- Selected for IT-G1: **NONE**
- Industrial evidence introduced: **NO**
- Scientific claims changed: **NO**
- Execution authorized: **NO**

## Priority recommendation

**ICD-01** is the current documentary priority because the purchase-item case has a naturally bounded unit, concrete industrial process context, explicit event history and contextual constraints. This is only a screening priority. It is not admission to IT-G1 and does not authorize dataset execution.

The next governance step, if separately authorized, is to propose ICD-01 for a formal IT-G1 review of exact system boundary, transformation identity and decision-time accessibility.
