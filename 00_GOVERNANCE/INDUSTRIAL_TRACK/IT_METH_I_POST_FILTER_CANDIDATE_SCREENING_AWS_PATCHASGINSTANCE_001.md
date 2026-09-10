# IT-METH-I Post-Filter Candidate Screening — AWS-PatchAsgInstance

**Status:** `CONDITIONAL — RETAIN FOR TARGETED CASE DISCOVERY`
**Date:** 2026-09-10
**Filter:** `INDUSTRIAL_DISCOVERY_FILTER_POST_IT_METH_I_v0.1`
**IT-G1:** `NOT STARTED`
**Execution authorization:** `NONE`

## Candidate

Amazon-owned Systems Manager Automation runbook `AWS-PatchAsgInstance`, which patches an EC2 instance in an Auto Scaling group.

AWS explicitly states that the runbook applies an `AutoPatchInstanceInASG` tag during execution to prevent simultaneous duplicate execution. It also explicitly warns that this tag is **not** a patch-compliance indicator and may remain `Completed` even if patching fails; compliance must instead be verified through `DescribeInstancePatchStates` or `ListComplianceItems`. The runbook exposes `InstanceId`, `WaitForInstance` (default `PT2M`) and `WaitForReboot` (default `PT5M`).

AWS separately states that the purpose of this runbook for Auto Scaling instances is to help avoid instances undergoing patching from being replaced. This creates a potentially strong decision-time accessibility distinction: patching under controlled Auto Scaling conditions versus ordinary patching that does not explicitly preserve instance continuity.

## F1–F12 screening

| Gate | Result | Basis |
|---|---|---|
| F1 Documentary closure | PASS | First-party AWS runbook and EC2 update-management documentation are explicit. |
| F2 System/state identifiability | PASS/CONDITIONAL | Boundary is an EC2 instance in an Auto Scaling group; concrete group/instance state remains to be frozen. |
| F3 Transformation identity | PASS | Patch an instance while preserving its Auto Scaling service context is explicit. |
| F4 Accessibility observability | CONDITIONAL | The runbook's operational controls are explicit, but actual ASG state and replacement conditions are case-specific. |
| F5 Temporal closure | CONDITIONAL | Wait parameters are explicit, but execution window and runbook/baseline versions require freezing. |
| F6 Evidence integrity | PASS | First-party AWS sources. |
| F7 Metric observability | PASS/CONDITIONAL | Automation execution and patch compliance are observable; AWS explicitly recommends compliance APIs rather than the transient tag. A discriminative utility metric remains to be frozen. |
| F8 Effort readiness | CONDITIONAL | Execution timestamps exist, but IT-G4 effort convention must be frozen ex ante. |
| F9 Reproducibility readiness | CONDITIONAL | Public runbook and parameters are reproducible; exact ASG/instance/baseline state is not supplied by AWS documentation. |
| F10 Discriminative utility potential | **PROMISING** | The documented purpose is specifically to avoid replacement of an instance undergoing patching, creating a potentially measurable continuity/accessibility distinction. |
| F11 Comparator validity | CONDITIONAL-PASS | Conventional comparator can be `AWS-RunPatchBaseline` or another frozen patching path on the same instance, provided the ASG state and baseline are identical. |
| F12 Downstream separation | PASS/CONDITIONAL | Accessibility can be defined from pre-execution ASG membership, patching controls and instance state without using the later patch outcome. |

## Important methodological advantage

This candidate is potentially stronger than `AWSEC2-PatchLoadBalancerInstance` for discriminative utility because AWS itself states the operational purpose in terms of **avoiding instance replacement during patching**. The relevant transformation is therefore not merely a procedural sequence; it changes the conditions under which patching can occur while retaining the intended Auto Scaling service context.

The candidate must nevertheless not be admitted on that statement alone. The concrete ASG state, replacement policy/configuration, patch baseline and comparator must be frozen before any IT-G1 decision.

## Required case-data closure

1. Fixed Auto Scaling group and instance boundary.
2. Pre-decision ASG membership and instance lifecycle state.
3. Relevant replacement/health configuration.
4. Fixed OS/platform and patch baseline.
5. Fixed `AWS-PatchAsgInstance` document version and parameters.
6. Frozen conventional comparator.
7. Ex-ante utility metric capable of detecting a practically relevant continuity/accessibility difference.
8. IT-G4 effort convention.
9. Independent two-reconstruction design.
10. Explicit proof that post-decision patch outcome is not needed to define accessibility.

## Decision

**DISPOSITION = CONDITIONAL — RETAIN FOR TARGETED CASE DISCOVERY**

No IT-G1 admission. No execution authorization. No TGCV Core change. No superiority, causal, safety, financial or value claim.

## Source references

- AWS Systems Manager Automation Runbook Reference: `AWS-PatchAsgInstance`.
- Amazon EC2 User Guide: `Update management for Amazon EC2 instances`.
- AWS Systems Manager Runbook Reference: EC2 runbooks.
