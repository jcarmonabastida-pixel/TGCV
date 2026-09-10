# IT-METH-I Post-Filter Case Closure — AWS-PatchAsgInstance

**Status:** `CLOSED — CONDITIONAL / CASE NOT CLOSED FOR IT-G1`
**Date:** 2026-09-10
**Candidate:** `AWS-PatchAsgInstance`

## Evidence closure result

The first-party AWS documentation closes the **runbook mechanism and observability model** more strongly than the previous ALB candidate.

AWS documents:
- the target boundary as an EC2 instance in an Auto Scaling group;
- the explicit `InstanceId` input;
- `WaitForInstance` and `WaitForReboot` parameters;
- the `AutoPatchInstanceInASG` execution-control tag;
- the fact that this tag is not a compliance indicator;
- compliance observability through `DescribeInstancePatchStates` or `ListComplianceItems`;
- the operational purpose of helping avoid replacement of an instance undergoing patching. citeturn0search0turn0search3

AWS's patch-state API exposes `BaselineId`, `PatchGroup`, installed/missing/failed counts, operation start/end times, operation type and reboot option, making the compliance state highly observable at the API level. citeturn0search1turn0search5

## F1–F12 closure

- F1 Documentary closure: PASS
- F2 System/state identifiability: CONDITIONAL
- F3 Transformation identity: PASS
- F4 Accessibility observability: CONDITIONAL
- F5 Temporal closure: CONDITIONAL
- F6 Evidence integrity: PASS
- F7 Metric observability: PASS/CONDITIONAL
- F8 Effort readiness: CONDITIONAL
- F9 Reproducibility readiness: CONDITIONAL-PASS
- F10 Discriminative utility potential: PROMISING
- F11 Comparator validity: CONDITIONAL-PASS
- F12 Downstream separation: PASS/CONDITIONAL

## Remaining blockers

First-party public documentation still does not supply a single concrete, reproducible pre-decision industrial instance with all of the following frozen simultaneously:

1. actual Auto Scaling group and instance state;
2. lifecycle/health/replacement configuration;
3. OS and patch baseline assignment;
4. exact runbook version and parameter values;
5. decision-time patch-state snapshot;
6. comparator instance/configuration on the same evidence boundary;
7. an ex-ante discriminative utility metric;
8. a frozen IT-G4 effort convention.

The public AWS examples provide API schemas and example observations, but the example identifiers are documentation examples rather than a frozen real industrial case. They therefore cannot be promoted to case evidence without additional controlled data intake. citeturn0search1turn0search10

## Decision

**DISPOSITION = CONDITIONAL — RETAIN FOR CONTROLLED CASE-DATA INTAKE**

The candidate is now the **preferred AWS candidate**, because its documented purpose creates a stronger potential discriminative dimension than the previous ALB candidate: preservation of the intended Auto Scaling service context during patching. AWS explicitly states this purpose. citeturn0search3

However:

- `IT-G1_ADMISSION = NOT_GRANTED`
- `EXECUTION_AUTHORIZATION = NONE`
- `TGCV_CORE_CHANGE = NO`
- no industrial utility claim
- no comparative superiority claim
- no causal/value/safety/financial claim.

## Next permissible operation

Do not continue generic AWS documentation discovery. The next operation must be one of:

**A. Controlled case-data intake** from a reproducible public fixture or user-provided/exported case package that can freeze the missing state variables; or

**B. If such data cannot legitimately be obtained, close this candidate as CONDITIONAL and pivot to another domain with naturally public pre-decision state and comparator evidence.**
