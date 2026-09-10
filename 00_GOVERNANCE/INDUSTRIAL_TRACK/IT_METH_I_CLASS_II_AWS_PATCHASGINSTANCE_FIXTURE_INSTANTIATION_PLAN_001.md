# IT-METH-I — Class II AWS-PatchAsgInstance Fixture Instantiation Plan 001

**Date:** 2026-09-10  
**Status:** `PLAN FROZEN — NO EXECUTION AUTHORIZATION`  
**Candidate:** `AWS-PatchAsgInstance`  
**Evidence class:** `CLASS II — PUBLIC REPRODUCIBLE FIXTURE`

## 1. Decision question

Determine the minimum additional instantiation required to close the pre-decision state contract without introducing unnecessary AWS execution.

## 2. Result

A purely static reconstruction is **insufficient** for the intended accessibility experiment because several decisive variables are inherently instance/runtime-specific:

- concrete ASG identity;
- concrete target `InstanceId`;
- effective AMI/image identity;
- actual ASG lifecycle/health/replacement state;
- effective patch-baseline assignment;
- pre-decision patch compliance state;
- Systems Manager managed-instance state;
- observation timestamp/cutoff.

Therefore a **controlled AWS fixture instantiation is methodologically necessary** if the experiment is to test actual decision-time accessibility rather than merely reproduce documentary structure.

## 3. What can remain static

No AWS execution is needed to freeze these elements:

- source repository commits;
- source-file byte hashes;
- ASG template structure;
- Amazon Linux 2 configuration intent;
- patch baseline rules;
- Patch Group mechanism;
- runbook identity and parameter semantics;
- candidate/comparator conceptual contract;
- accessibility predicate definitions;
- evidence schema.

## 4. Minimum runtime fixture

The runtime fixture should contain only the resources necessary to instantiate the frozen state:

1. one bounded Auto Scaling Group;
2. one target EC2 instance managed by Systems Manager;
3. one deterministic launch-template/image configuration;
4. one explicit patch baseline and patch-group assignment;
5. the minimum IAM permissions needed for observation and, only after separate authorization, transformation execution;
6. no unrelated production resources.

The existing public AWS sources may be used as construction references, but the instantiated fixture is a composition and must retain source provenance.

## 5. Pre-decision freeze procedure

Before any candidate or comparator transformation:

1. instantiate the bounded fixture;
2. resolve and record concrete resource identifiers;
3. resolve and record effective AMI/image identity;
4. record ASG capacity and lifecycle/health/replacement configuration;
5. record target instance state;
6. record Patch Group and effective baseline assignment;
7. obtain and freeze pre-decision patch compliance state;
8. record Systems Manager managed-instance state;
9. record all accessibility-predicate inputs;
10. establish the observation timestamp/cutoff;
11. generate byte hashes for the resulting evidence package;
12. independently reconstruct the frozen state through a second path.

No candidate transformation occurs during this freeze.

## 6. Comparator instantiation

The comparator must be frozen against the same initial state/evidence package. It must be an explicit ordinary patching transformation with a defined command/document/procedure, not an informal description.

If a comparator cannot be made operationally explicit while preserving the common evidence boundary, the experiment is blocked rather than relaxed.

## 7. Authorization boundary

This plan does **not** authorize:

- AWS account/resource creation;
- `AWS-PatchAsgInstance` invocation;
- comparator execution;
- utility measurement;
- production or industrial claims.

A separate authorization record is required before any runtime transformation is executed.

## 8. Gate status

`STATIC_RECONSTRUCTION_SUFFICIENCY = FAIL`

Reason: static material cannot supply the required concrete decision-time state variables.

`CONTROLLED_RUNTIME_INSTANTIATION_REQUIRED = TRUE`

`PRE_EXECUTION_GATE = BLOCKED`

## 9. Falsification safeguard

If the controlled fixture cannot be instantiated with independently observable values for the mandatory state variables, the Class II experiment must terminate as methodologically blocked. The design must not substitute post-decision outcomes, inferred state, or documentary labels for missing pre-decision observations.

## 10. Next permissible operation

Prepare the **controlled fixture build specification**: exact AWS resources, deterministic configuration, observation commands, evidence files, hashes, teardown boundary, and the separation between pre-decision observation and any later transformation execution.

That build specification must remain non-executing until separately authorized.
