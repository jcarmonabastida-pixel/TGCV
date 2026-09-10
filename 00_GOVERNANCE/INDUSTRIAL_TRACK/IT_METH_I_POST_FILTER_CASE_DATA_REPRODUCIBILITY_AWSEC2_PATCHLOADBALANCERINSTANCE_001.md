# IT-METH-I Post-Filter Case Data Reproducibility — AWSEC2-PatchLoadBalancerInstance

**Status:** `CLOSED — REPRODUCIBLE PUBLIC TOPOLOGY DEMONSTRATED / IT-G1 STILL BLOCKED`
**Date:** 2026-09-10
**Candidate:** `AWSEC2-PatchLoadBalancerInstance`

## Finding

A public technical reproduction was located that documents a concrete topology and execution configuration for the AWS runbook: two EC2 instances behind an Application Load Balancer target group, identified with tag `ALB=alb01`, with Automation concurrency set to `1`. The report observes the instance being deregistered and entering the draining state during execution.

This is useful evidence of **reproducibility of the operational topology and transformation**, but it is not first-party AWS evidence and therefore cannot by itself become the frozen industrial evidence boundary.

AWS's own runbook documentation independently confirms the same transformation structure: identify the load balancer/target group and verify health; remove the instance; wait for configured connection draining; invoke `AWS-RunPatchBaseline`; reattach the instance. `InstanceId` and `ConnectionDrainTime` are explicit parameters, with `ConnectionDrainTime` configurable from 1 to 59 minutes. Source: AWS Systems Manager Automation Runbook Reference, `AWSEC2-PatchLoadBalancerInstance`.

AWS also provides an official CloudFormation walkthrough capable of provisioning a reproducible load-balanced EC2 topology with an Auto Scaling group and Application Load Balancer, although that walkthrough is a generic sample and does not establish the exact patch-case state by itself.

## Gate impact

- F1 Documentary closure: PASS
- F2 System/state identifiability: **CONDITIONAL → strengthened**
- F3 Transformation identity: PASS
- F4 Accessibility observability: **CONDITIONAL → strengthened**
- F5 Temporal closure: CONDITIONAL
- F6 Evidence integrity: **CONDITIONAL** because the concrete reproduction source is third-party; AWS remains the authoritative runbook source.
- F7 Metric observability: CONDITIONAL
- F8 Effort readiness: CONDITIONAL
- F9 Reproducibility readiness: **CONDITIONAL-PASS at topology level**
- F10 Discriminative utility potential: PROMISING
- F11 Comparator validity: CONDITIONAL-PASS
- F12 Downstream separation: PASS/CONDITIONAL

## Remaining blockers before IT-G1

The reproducible topology does not close:

1. exact EC2 image/OS and configuration;
2. exact patch baseline and version;
3. exact pre-decision health/configuration snapshot;
4. ex-ante utility metric;
5. frozen IT-G4 effort convention;
6. first-party byte/evidence package for the concrete case;
7. two-reconstruction protocol instantiated for the case.

Therefore this record **does not authorize IT-G1** and does not convert the public reproduction into industrial evidence.

## Decision

**CASE_DATA_REPRODUCIBILITY = STRENGTHENED**
**IT-G1_ADMISSION = NOT_GRANTED**
**EXECUTION_AUTHORIZATION = NONE**
**TGCV_CORE_CHANGE = NO**

### Sources

- AWS Systems Manager Automation Runbook Reference: `AWSEC2-PatchLoadBalancerInstance`.
- AWS CloudFormation: `Create a scaled and load-balanced application`.
- Public technical reproduction: NHN Techorus technical blog describing two EC2 instances behind an ALB, tag-based targeting and concurrency=1, with observed draining/deregistration behavior.
