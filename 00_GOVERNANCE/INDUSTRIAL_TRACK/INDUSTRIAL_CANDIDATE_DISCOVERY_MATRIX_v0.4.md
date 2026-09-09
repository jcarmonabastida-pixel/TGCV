# TGCV — Industrial Candidate Discovery Matrix v0.4

**Status:** CURRENT / OPERATIVE — DESIGN-ONLY  
**Execution:** NOT AUTHORIZED  
**Protocol:** `INDUSTRIAL_CANDIDATE_DISCOVERY_PROTOCOL_v0.1.md`

Documentary discovery has now been extended after separate IT-G1 failures of ICD-01 and ICD-02. Retention is not admission.

| Candidate | Natural unit / boundary | State reconstructability | Transformation identity | Accessibility observability | Temporal closure | Independent evidence | Downstream separation | Disposition |
|---|---|---|---|---|---|---|---|---|
| **ICD-01 BPI-2019 Purchase-item workflow** | Purchase-document line item | PASS-BOUND | PASS-CANDIDATE | **FAIL at IT-G1** | PASS | Insufficient for accessibility closure | PASS-BOUND | **IT-G1 FAIL — NOT ADMITTED** |
| **ICD-02 BPI-2015 Building-permit workflow** | Building-permit application / municipality slice | PASS-BOUND | PASS-CANDIDATE | **FAIL at IT-G1** | PASS | Insufficient for accessibility closure | PASS-CANDIDATE | **IT-G1 FAIL — NOT ADMITTED** |
| **ICD-03 BPI-2014 Change/Incident management** | IT change / incident | PASS-CANDIDATE | CONDITIONAL | CONDITIONAL | PASS-CANDIDATE | PASS | PASS-CANDIDATE | CONDITIONAL — NOT ADMITTED |
| **ICD-04 BPI-2020 Travel-permit workflow** | Travel-permit case | PASS-BOUND | CONDITIONAL | CONDITIONAL | PASS | PASS | PASS-CANDIDATE | CONDITIONAL — NOT ADMITTED |
| **ICD-05 BPI-2017 Loan-application workflow** | Loan application / offers | PASS-BOUND | CONDITIONAL | WEAK / OPEN | PASS | PASS | PASS-CANDIDATE | CONDITIONAL — LOW PRIORITY |
| **ICD-06 Road Traffic Fine Management** | One traffic fine | PASS-BOUND | PASS-CANDIDATE | **FAIL at screening** — normative alternatives exist, but actual choice can depend on unavailable contextual factors | PASS | Public event log + normative description | PASS-CANDIDATE | **DISCARD** |
| **ICD-07 Hospital Sepsis pathway** | One patient pathway | PASS | CONDITIONAL | **FAIL at screening** — evolving clinical state/judgement does not yield complete ex-ante admissibility set | PASS | Public event log + clinical attributes | CONDITIONAL | **DISCARD** |
| **ICD-08 BPI-2017 decision process** | One loan application | PASS-BOUND | PASS-CANDIDATE | **CONDITIONAL / NOT CLOSED** — decision-mining inference is not independent accessibility evidence | PASS | Public event log with activity data | PASS-CANDIDATE | **CONDITIONAL — NOT RETAINED** |

## Discovery-cycle result

- Documentary discovery cycle v0.2: **COMPLETED**.
- IT-G1 candidates retained and tested: **ICD-01, ICD-02**.
- Both: **IT-G1 FAIL / NOT ADMITTED**.
- New documentary candidates satisfying the mandatory accessibility filter: **NONE**.
- No candidate admitted to IT-G2.
- Industrial evidence introduced: **NO**.
- Scientific claims changed: **NO**.
- Execution authorized: **NO**.

## Governance interpretation

The repeated failure is specifically about **independent decision-time accessibility closure**, not about the existence of process alternatives or the usefulness of event logs. Several sources support decision-model inference from observed traces, but inference from realized choices is not equivalent to an independently grounded ex-ante accessible transformation set. This distinction remains frozen.

The Industrial Track therefore currently has no documentary candidate suitable for progression. Further discovery, if authorized, should target domains with explicit normative or operational specifications of admissible alternatives rather than another generic event-log search.
