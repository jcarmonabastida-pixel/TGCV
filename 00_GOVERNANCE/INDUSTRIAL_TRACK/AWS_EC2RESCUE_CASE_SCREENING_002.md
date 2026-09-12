# TGCV — AWS EC2Rescue Case Screening 002

**Date:** 2026-09-12
**Status:** `CONDITIONAL — RETAIN FOR IT-G1 CASE IDENTIFIABILITY`
**Execution:** `NOT PERFORMED`
**Candidate:** `AWSSupport-ExecuteEC2Rescue`
**Scenario:** `UNREACHABLE EC2 INSTANCE / WINDOWS RDP CONNECTIVITY`

## 1. Case basis

AWS publicly documents a concrete, bounded operational scenario: an impaired/unreachable Windows EC2 instance whose connectivity/RDP must be restored using `AWSSupport-ExecuteEC2Rescue`.

AWS states that the runbook automatically troubleshoots and can restore EC2/RDP connectivity, and that execution stops the instance, creates an AMI backup, performs EC2Rescue processing through a temporary helper instance, and then restores/restarts the original instance. citeturn0search3turn0search1

This is suitable as a documentary case template, but it is **not yet a frozen empirical incident**.

## 2. Proposed natural unit

One unreachable Windows EC2 instance at one frozen decision time, with:

`S_t = {instance platform/state, root-volume state, subnet/AZ, SSM/IAM prerequisites, relevant connectivity context}`

Candidate transformation:

`τ_i = ExecuteEC2RescueRemediation`

The candidate identity does not depend on successful recovery.

## 3. Pre-outcome accessibility

AWS documentation identifies concrete prerequisites and constraints, including the unreachable instance ID, subnet/AZ conditions, SSM endpoints, IAM permissions, and the exclusion of encrypted root volumes. citeturn0search0turn0search1

Therefore the accessibility/admissibility assessment can in principle be frozen before execution and kept separate from the subsequent repair outcome.

## 4. Comparator candidate

The conventional comparator should be a documented manual Windows EC2/RDP troubleshooting procedure using the same pre-outcome case state, without the automated EC2Rescue remediation path.

AWS itself documents manual troubleshooting alongside the automation route. citeturn0search5turn0search3

The comparator is **not yet frozen** and therefore no comparative execution is authorized.

## 5. F1–F12 status

| Filter | Status |
|---|---|
| F1 Natural boundary | PASS-BOUND |
| F2 State reconstructability | CONDITIONAL |
| F3 Transformation identity | PASS |
| F4 Accessibility sufficiency | PASS-BOUND |
| F5 Temporal closure | CONDITIONAL |
| F6 Evidence independence | PASS |
| F7 Downstream separation | PASS-BOUND |
| F8 Effort convention | OPEN |
| F9 Reproducibility | CONDITIONAL |
| F10 Discriminative utility | PROMISING / UNTESTED |
| F11 Conventional comparator | OPEN |
| F12 Outcome/accessibility separation | PASS-BOUND |

## 6. Decision

`CANDIDATE = RETAINED CONDITIONALLY`

The scenario is sufficiently concrete to justify preparation of an IT-G1 case-identifiability package, but not sufficiently frozen to admit IT-G1 yet.

No AWS account, live instance, partner evidence, execution, intervention, utility measurement, causal assessment, or claim upgrade is authorized by this record.

## 7. Next gate

Prepare the **IT-G1 Case Identifiability Package** for this documented scenario, freezing:

1. exact case boundary;
2. pre-decision state schema;
3. candidate transformation identity;
4. accessibility/admissibility rule;
5. finite temporal window;
6. independent evidence sources;
7. conventional comparator;
8. effort convention;
9. reconstruction/agreement rule.

`IT-G1 AUTHORIZATION = NOT YET GRANTED`
