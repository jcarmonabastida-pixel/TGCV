# IT-METH-I — Class II AWS-PatchAsgInstance Variable Observability Assessment 001

**Date:** 2026-09-10  
**Status:** `CLOSED — DOCUMENTARY OBSERVABILITY PARTIAL / EXECUTION BLOCKED`  
**Candidate:** `AWS-PatchAsgInstance`  
**Evidence class:** `CLASS II — PUBLIC REPRODUCIBLE FIXTURE`  
**Parent manifest:** `IT_METH_I_CLASS_II_FIXTURE_COMPOSITION_MANIFEST_001.md`

## 1. Purpose

Assess which variables required by the frozen Class II experiment are independently reconstructable from the public source composition, without deploying AWS, invoking the runbook, or using post-decision outcomes.

This assessment is a fixture-level methodological assessment. It is not an industrial observability claim.

## 2. Variable assessment

| Variable | Status | Basis |
|---|---|---|
| Candidate runbook identity | PASS | `AWS-PatchAsgInstance` identified by frozen runbook source. |
| Runbook parameters | CONDITIONAL | `InstanceId` required; `AutomationAssumeRole` and `LambdaRoleArn` optional; defaults `WaitForInstance=PT2M`, `WaitForReboot=PT5M`. |
| ASG structural definition | PASS | Public ASG source fixes desired capacity 2, min 0, max 4 and Amazon Linux 2 launch-template structure. |
| Patch baseline specification | PASS | Public workshop source documents `AmazonLinux2SecAndNonSecBaseline`, rules, exception and patch-group mechanism. |
| Patch-group composition choice | PASS | Composition explicitly freezes `Patch Group=App` as a fixture choice. |
| Concrete ASG identity | NOT CLOSED | No live or otherwise uniquely instantiated ASG identity exists in the frozen composition. |
| Concrete target instance identity | NOT CLOSED | `InstanceId` is required by the runbook but no target instance has been instantiated. |
| Lifecycle / health / replacement state | NOT CLOSED | Public sources provide mechanisms/examples but not a single frozen target state. |
| Effective AMI/image identity | NOT CLOSED | Source uses a public latest-AMI parameter; an exact effective image requires instantiation-time resolution. |
| Effective patch baseline assignment | NOT CLOSED | Documentary baseline and patch-group mechanism are known, but effective target assignment is not frozen at instance level. |
| Pre-decision patch compliance state | NOT CLOSED | Requires an instantiated target state; cannot be inferred from later patch outcome. |
| Accessibility predicates | NOT CLOSED | Candidate predicates can be specified, but their target-state truth values require a frozen pre-decision instance state. |
| Temporal cutoff | NOT CLOSED | No instantiated fixture observation timestamp has been frozen. |
| Comparator | NOT CLOSED | Comparator concept is defined, but its executable/observable configuration is not yet frozen. |
| Ex-ante discriminative metric | NOT CLOSED | Experiment design identifies the need for a metric; no executable metric package has yet been frozen. |
| Independent reconstruction paths | NOT CLOSED | Two independent reconstruction paths have not yet been instantiated and checked. |
| Effort convention | NOT CLOSED | Required only if analytical effort is measured; convention has not yet been frozen for this fixture. |

## 3. Closed documentary layer

The following layer is sufficiently closed for fixture construction:

1. public source identities and frozen commits;
2. byte-level hashes of the principal local source files;
3. ASG structural parameters;
4. Amazon Linux 2 source configuration;
5. patch-baseline documentary specification;
6. patch-group mechanism;
7. candidate runbook identity and documented parameter semantics;
8. explicit composition choices.

## 4. Remaining decision-time observability gap

The decisive gap is not documentation of the AWS mechanism. It is the absence of a uniquely instantiated target whose pre-decision state can be frozen and independently reconstructed.

Therefore the following cannot legitimately be promoted from documentary knowledge to observed decision-time variables:

- concrete target identity;
- effective image identity;
- actual lifecycle/health/replacement state;
- actual patch compliance state;
- truth values of accessibility predicates;
- observation cutoff.

No later execution outcome may be used to fill these fields retroactively.

## 5. Gate consequence

`VARIABLE_OBSERVABILITY_GATE = PARTIAL`

`PRE_EXECUTION_GATE = BLOCKED`

The fixture is sufficiently specified to identify the exact variables that must be frozen, but not sufficiently instantiated to authorize execution.

## 6. Required next operation

The next permissible operation is to define the **pre-decision fixture state specification and comparator contract** in a separate frozen design record. This must specify exactly which target-state variables will be captured before any candidate transformation and how the comparator will be represented under the same evidence boundary.

No AWS deployment or runbook invocation is authorized by this assessment.

## 7. Prohibitions

Until the pre-execution gate is independently closed:

- do not invoke `AWS-PatchAsgInstance`;
- do not assign utility scores;
- do not infer accessibility from outcomes;
- do not promote Class II evidence to Class I;
- do not modify TGCV Core;
- do not initiate IT-G1 or IT-G5.
