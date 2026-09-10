# TGCV — Post-IT-METH-I Industrial Candidate Discovery 001

**Date:** 2026-09-10  
**Status:** `DISCOVERY SCREENING — NO IT-G1 AUTHORIZATION`  
**Filter:** `INDUSTRIAL_DISCOVERY_FILTER_POST_IT_METH_I_v0.1`

## 1. Objective

Screen candidate industrial domains against the frozen post-IT-METH-I discovery filter before any candidate is routed to IT-G1.

No experiment is authorized by this record. The FAA AMOC experiment remains closed and is not reopened.

## 2. Discovery findings

### Candidate family A — Cloud incident remediation / runbook automation

**Priority:** `HIGH — SUBJECT TO CASE-SPECIFIC CLOSURE`

Public AWS documentation establishes that Automation runbooks have explicit parameters, actions, outputs, conditional branches, approvals, execution states and step-level execution records. Runbooks can branch on parameter values or outputs from previous steps, and execution metadata records status, start time, outputs, targets and step executions. AWS also exposes automation metrics and CloudWatch monitoring. This makes the domain materially different from the closed FAA documentary-reconstruction case because it contains executable state-dependent alternatives and observable operational execution data. 

Evidence:
- AWS Automation actions define explicit inputs, outputs, conditional branching and approval actions. [AWS Systems Manager documentation]
- `aws:branch` selects different execution paths from current parameters or prior-step outputs.
- Automation execution metadata includes status, start time, outputs, targets and step executions.
- AWS exposes Automation metrics and detailed execution statuses.

**Preliminary filter assessment:**

| Gate | Preliminary disposition | Reason |
|---|---|---|
| F1 | CONDITIONAL | A concrete incident/runbook unit and frozen decision-time evidence still need to be selected |
| F2 | PASS/CONDITIONAL | Runbook/resource state is explicit, but case boundary must be frozen |
| F3 | PASS | Runbook actions and branches have explicit identities |
| F4 | CONDITIONAL | Candidate-specific resource/configuration conditions must be shown independently observable |
| F5 | CONDITIONAL | Incident timestamp and relevant pre-action state must be frozen per case |
| F6 | PASS/CONDITIONAL | Public runbook/version and execution records provide strong anchoring, but exact case evidence must be frozen |
| F7 | PASS/CONDITIONAL | Execution status, step status, duration and failure state are observable; utility metric must be frozen per case |
| F8 | CONDITIONAL | Effort convention must be frozen before any blind execution |
| F9 | PASS/CONDITIONAL | Execution records support reproducibility, but reconstruction unit and agreement rule must be frozen |
| F10 | **PROMISING** | Routing among state-dependent remediation paths creates plausible discriminative utility beyond simple information reconstruction |
| F11 | CONDITIONAL | Conventional human/runbook procedure must be selected and frozen as comparator |
| F12 | PASS/CONDITIONAL | Operational outcomes can be separated from decision-time accessibility, subject to case design |

**Disposition:** `RETAIN FOR CASE-SPECIFIC SCREENING`.

### Candidate family B — Azure Automation / incident-response runbooks

**Priority:** `MEDIUM-HIGH — SUBJECT TO CASE-SPECIFIC CLOSURE`

Microsoft documentation establishes runbook parameters, execution status, start/end times, job history, diagnostic logs and metrics. Azure incident-response guidance also describes routing and automation according to incident context and guardrails.

**Preliminary filter assessment:** similar to Candidate A. The strongest discriminative dimension is state-dependent routing of response plans rather than mere runbook execution.

**Disposition:** `RETAIN AS SECONDARY CANDIDATE FAMILY`.

### Candidate family C — Aviation AMOC / AltMoC

**Disposition:** `HOLD / LOW PRIORITY`.

Public FAA/EASA material confirms strong explicit alternative-compliance structures, but the recently closed FAA AMOC experiment demonstrated that a documentary reconstruction case can produce near-equivalent TGCV and conventional representations without discriminative utility. Reusing this family immediately would risk repeating the same methodological limitation rather than testing the newly adopted F10 requirement.

The family is not rejected universally; it is deprioritized for the next discovery cycle.

## 3. Discovery decision

The first promising direction is **state-dependent operational remediation**, especially cloud incident/runbook automation, because it potentially satisfies the new requirement that a candidate expose a genuine difference in accessible transformations rather than only equivalent documentary reconstruction.

However, no concrete incident has yet passed all F1–F12 gates. Therefore:

`CANDIDATE_ADMISSION = NOT YET GRANTED`

`IT-G1 = NOT STARTED`

`EXECUTION_AUTHORIZATION = NONE`

## 4. Next operation

The next operation is **case-specific screening of one concrete public, reproducible runbook/incident unit** against F1–F12, with particular attention to F8–F11 before IT-G1.

No candidate may be promoted merely because the domain is promising.
