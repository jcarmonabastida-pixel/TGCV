# IT-METH-I Post-Filter Candidate Screening — AWS-PatchInstanceWithRollback

**Status:** `CONDITIONAL — RETAIN FOR TARGETED CASE DISCOVERY / NOT ADMITTED TO IT-G1`
**Date:** 2026-09-10
**Filter:** `INDUSTRIAL_DISCOVERY_FILTER_POST_IT_METH_I_v0.1`
**Execution authorization:** `NONE`

## Candidate

Concrete public AWS Systems Manager Automation runbook: `AWS-PatchInstanceWithRollback`.

AWS documents this as an Amazon-owned Automation runbook for Linux, macOS and Windows. It applies the applicable patch baseline to an EC2 instance and restores the root volume on failure. The documented workflow includes identification of the root volume, pre-patch snapshot, patch installation, compliance checking, compliance reporting, failure restoration and cleanup. The documented outputs include the root-volume identification, pre-patch snapshot, compliance report and restoration payloads. 

## F1–F12 screening

| Gate | Result | Basis |
|---|---|---|
| F1 Documentary closure | PASS | Public AWS runbook reference defines the candidate, owner, platforms, required input and documented steps/outputs. |
| F2 System/state identifiability | CONDITIONAL | System boundary is an identified EC2 instance (`InstanceId`), but the full decision-time state required for a reproducible TGCV case must be frozen for an actual instance/configuration. |
| F3 Transformation identity | PASS | The transformation is identifiable as applying the applicable patch baseline, with explicit remediation/restoration steps. |
| F4 Accessibility observability | CONDITIONAL | The runbook explicitly defines a failure restoration path, but the admissibility of each path depends partly on runtime conditions and the actual instance/snapshot environment. |
| F5 Temporal closure | CONDITIONAL | The runbook sequence is explicit, but a case-specific execution window, patch-baseline version and relevant configuration snapshot must be frozen before IT-G1. |
| F6 Evidence integrity | PASS | AWS is the documented owner and the runbook reference is publicly reproducible. |
| F7 Metric observability | PASS/CONDITIONAL | Compliance status, step status, execution start/end times and outputs are observable through Automation execution/step records; a utility metric still needs ex-ante case definition. |
| F8 Effort readiness | CONDITIONAL | Execution timestamps are observable, but the IT-METH-I effort convention must be frozen before any blind execution. |
| F9 Reproducibility readiness | CONDITIONAL | The runbook and parameters are reproducible, but instance state, patch baseline, OS/package state and IAM/runtime dependencies must be frozen. |
| F10 Discriminative utility potential | PROMISING / CONDITIONAL | Unlike the FAA AMOC case, the runbook contains an explicit contingency transformation: pre-patch snapshot and restoration on failure. This creates a potentially discriminative accessibility/utility dimension. |
| F11 Comparator validity | CONDITIONAL | A comparator such as conventional `AWS-RunPatchBaseline` or an explicitly frozen manual/conventional patch procedure is plausible, but it must be fixed on the same evidence boundary before IT-G4. |
| F12 Downstream separation | PASS/CONDITIONAL | Public documentation separates runbook specification from execution outcomes; actual case selection must exclude post-decision outcomes from the decision-time representation. |

## Disposition

`CONDITIONAL — RETAIN FOR TARGETED CASE DISCOVERY`.

This is stronger than the previously screened generic AWS SSM family because the concrete runbook exposes an explicit failure-contingency transformation and observable execution outputs. It is nevertheless **not admitted to IT-G1** because F2, F4, F5, F7, F8, F9 and F11 require case-specific closure.

## Required next evidence before IT-G1

1. Freeze one reproducible EC2 instance/configuration boundary.
2. Freeze OS/platform and patch-baseline identity.
3. Freeze the decision-time state required to determine the admissible remediation path.
4. Define the comparator before execution.
5. Freeze an effort convention before any blind reconstruction.
6. Define one or more observable utility dimensions ex ante, with special attention to restoration/contingency handling.
7. Demonstrate that the required observations do not depend on post-decision outcomes.

No execution, IT-G1 admission, utility claim, superiority claim or TGCV Core change is authorized by this screening record.

## Source basis

- AWS Systems Manager Automation Runbook Reference — `AWS-PatchInstanceWithRollback`.
- AWS Systems Manager `aws:invokeLambdaFunction` action reference, including the documented use of outputs in the runbook.
- AWS Systems Manager Automation status/step-execution documentation for observable execution status and timestamps.
