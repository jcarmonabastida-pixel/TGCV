# IT-METH-I Post-Filter Candidate Screening — AWS-PatchInstanceWithRollback 002

**Status:** `CONDITIONAL — RETAIN / TARGETED CASE DISCOVERY REQUIRED`
**Date:** 2026-09-10
**Filter:** `INDUSTRIAL_DISCOVERY_FILTER_POST_IT_METH_I_v0.1`
**IT-G1:** `NOT STARTED`
**Execution authorization:** `NONE`

## Screening decision

The concrete `AWS-PatchInstanceWithRollback` runbook remains the strongest current AWS candidate, but it is **not yet admissible to IT-G1**. The current documentary evidence closes the runbook-level structure substantially, but not the case-level decision state required by the industrial methodology.

AWS documents the runbook as an Amazon-owned Automation document for Linux, macOS and Windows. Its required case input is an EC2 `InstanceId`; optional inputs include IAM roles and an S3 destination for the compliance report. The documented sequence includes root-volume identification, pre-patch snapshot, patch installation, compliance check/reporting, restoration from snapshot and cleanup. The documented outputs include the snapshot, compliance report and restoration payloads. citeturn1view0

AWS also exposes execution-level state including document name/version, parameters, execution status, start/end time, current step, step executions, outputs and target information. This materially strengthens F2/F5/F7/F8/F9 readiness compared with the generic AWS family, but these fields describe an actual execution and therefore do not by themselves establish the pre-decision state needed for an IT-G1 reconstruction. citeturn1view2

## F1–F12

| Gate | Result | Determination |
|---|---|---|
| F1 Documentary closure | PASS | Public AWS documentation identifies the runbook, owner, platforms, parameters, ordered steps and outputs. |
| F2 System/state identifiability | CONDITIONAL | System boundary can be fixed to one EC2 instance, but the complete decision-time state/configuration must be frozen ex ante. |
| F3 Transformation identity | PASS | Patch-to-compliance plus snapshot-based restoration is explicitly represented in the runbook structure. |
| F4 Accessibility observability | CONDITIONAL | Restoration is explicitly available as a failure path, but actual accessibility depends on instance/root-volume/snapshot conditions that must be fixed before execution. |
| F5 Temporal closure | CONDITIONAL | Execution start/end and document version are observable, but patch-baseline version, instance configuration and decision-time temporal boundary must be frozen ex ante. |
| F6 Evidence integrity | PASS | Candidate is based on first-party AWS documentation and a named Amazon-owned runbook. |
| F7 Metric observability | CONDITIONAL-PASS | Execution status, step executions, outputs and timestamps are observable. A utility metric that distinguishes TGCV from the comparator still requires ex-ante specification. |
| F8 Effort readiness | CONDITIONAL | Start/end timestamps exist, but IT-METH-I effort convention must be frozen before execution. |
| F9 Reproducibility readiness | CONDITIONAL | Runbook structure is reproducible; case reproducibility additionally requires frozen instance, OS, patch baseline, configuration and IAM/runtime prerequisites. |
| F10 Discriminative utility potential | CONDITIONAL-PROMISING | The explicit contingency/restoration path provides a potentially discriminative transformation/accessibility dimension absent from the closed FAA case. It is not yet demonstrated to yield comparative utility. |
| F11 Comparator validity | CONDITIONAL | `AWS-RunPatchBaseline` is a plausible conventional comparator because AWS documents it as the standard patching document, but the exact comparator configuration/evidence boundary must be frozen before IT-G4. citeturn0search1 |
| F12 Downstream separation | PASS | Decision-time representation can be separated from execution outcomes; the protocol must prohibit using post-decision success/failure to define initial accessibility. |

## Why this is not IT-G1 yet

The remaining blocker is **case-level closure**, not lack of a usable public runbook.

The minimum next evidence package must establish:

1. one fixed EC2 instance boundary;
2. fixed OS/platform and relevant configuration state;
3. fixed patch baseline/document version;
4. explicit pre-decision conditions under which the patch transformation and rollback transformation are accessible;
5. a frozen conventional comparator on the same evidence boundary;
6. an effort convention frozen before any execution;
7. a utility metric capable of distinguishing the two representations without using post-decision outcomes to define accessibility;
8. a reproducibility design allowing independent reconstruction without access to the other reconstruction.

## Decision

**DISPOSITION = CONDITIONAL — RETAIN FOR TARGETED CASE DISCOVERY**

No IT-G1 admission is granted by this record. No execution is authorized. No TGCV Core claim changes. No superiority, causality, safety, financial, operational or value claim is made.

The next operation is therefore **case-specific evidence closure**, not execution and not another generic AWS-domain search.
