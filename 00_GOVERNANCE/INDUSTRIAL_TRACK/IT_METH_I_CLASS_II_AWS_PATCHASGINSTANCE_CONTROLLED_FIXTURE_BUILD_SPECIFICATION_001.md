# IT-METH-I — Class II AWS-PatchAsgInstance Controlled Fixture Build Specification 001

**Date:** 2026-09-10  
**Status:** `BUILD SPECIFICATION FROZEN — NOT AUTHORIZED FOR EXECUTION`  
**Candidate:** `AWS-PatchAsgInstance`  
**Evidence class:** `CLASS II — PUBLIC REPRODUCIBLE FIXTURE`  
**Parent plan:** `IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_FIXTURE_INSTANTIATION_PLAN_001.md`

## 1. Objective

Define the smallest controlled AWS fixture capable of producing a directly observable, frozen pre-decision state for the Class II experiment.

The fixture exists only to test methodological/representational feasibility. It is not an industrial production case.

## 2. Resource boundary

The fixture SHALL contain only:

- one dedicated Auto Scaling Group;
- one or more EC2 instances sufficient to establish a target instance;
- one launch template/version;
- networking required for the target to operate and be managed by Systems Manager;
- one explicit patch baseline and patch-group assignment;
- minimum IAM roles required for management and observation;
- Systems Manager managed-instance registration;
- no production workloads or unrelated resources.

The target fixture should use Amazon Linux 2, consistent with the frozen public-source composition, unless an amended design explicitly records a different image.

## 3. Deterministic configuration requirements

The build MUST freeze before deployment:

- source commits and source-file hashes from the composition manifest;
- AWS region;
- CloudFormation/template identity if used;
- ASG name;
- desired/min/max capacity;
- launch-template identity/version;
- exact AMI ID;
- instance type;
- health-check configuration;
- lifecycle/replacement configuration relevant to the target;
- Patch Group tag value;
- patch baseline identity/version;
- all SSM configuration relevant to patch-state reporting.

Where the public template uses a dynamic/latest parameter, the effective resolved value MUST be recorded after resolution and before the pre-decision freeze.

## 4. Build order

1. Freeze build inputs and hashes.
2. Create isolated networking and prerequisite IAM resources, if required.
3. Create the explicit patch baseline and patch-group association.
4. Create the bounded ASG and launch template.
5. Wait only for required infrastructure stabilization.
6. Identify the concrete target instance.
7. Verify Systems Manager registration.
8. Capture the target's pre-decision state.
9. Capture patch compliance and effective baseline information.
10. Capture ASG health/lifecycle/replacement information.
11. Capture all accessibility-predicate inputs.
12. Freeze the evidence package and hashes.
13. Perform independent reconstruction of the frozen state.
14. Stop. No candidate transformation is performed by this build specification.

## 5. Pre-decision evidence package

The package MUST include, at minimum:

- fixture manifest;
- source provenance manifest;
- ASG description/configuration;
- launch-template/version description;
- target instance description;
- effective AMI identity;
- instance OS identity;
- health status;
- ASG lifecycle/replacement configuration;
- Patch Group tags;
- patch baseline identity and rules;
- target patch compliance state;
- SSM managed-instance state;
- relevant IAM/access predicates;
- timestamped observation record;
- accessibility-predicate evaluation;
- SHA-256 manifest for every evidence file.

Raw command output must be preserved. Derived summaries must not replace raw evidence.

## 6. Evidence integrity

Every generated evidence file MUST be hashed after capture. The evidence manifest MUST record:

`path | size | SHA256 | capture_time | source_command_or_method`

The build MUST distinguish:

- source-byte integrity;
- generated-evidence byte integrity;
- semantic/documentary interpretation.

A hash mismatch blocks progression.

## 7. Candidate execution boundary

This specification deliberately ends before transformation execution.

`PHASE_A = FIXTURE_BUILD_AND_PREDECISION_FREEZE`

`PHASE_B = CANDIDATE_EXECUTION`

`PHASE_C = COMPARATOR_EXECUTION`

Only Phase A is described here. Phases B and C require separate authorization after the pre-execution integrity gate.

## 8. Comparator preparation

The comparator contract must be operationalized before execution authorization. It must use the same frozen pre-decision state/evidence boundary and must not derive eligibility from a candidate outcome.

If the comparator cannot be implemented without changing the common state boundary, the experiment remains blocked.

## 9. Independent reconstruction

The second reconstruction MUST NOT depend on the first reconstruction's derived interpretation.

It should consume the frozen source package and independently produce:

- state vector;
- accessibility predicates;
- candidate transformation identity;
- comparator identity;
- temporal cutoff.

Agreement must be established before any transformation execution.

## 10. Teardown boundary

After evidence capture and any separately authorized experimental execution, all fixture resources must be explicitly identified for teardown.

The teardown record must preserve the complete pre-decision evidence package before resources are removed.

No production resource may be used as part of this fixture.

## 11. Safety and non-claims

This build specification does not establish:

- industrial utility;
- production superiority;
- financial value;
- causal effect;
- generalization beyond the fixture;
- AWS production performance;
- any change to TGCV Core.

## 12. Current gate

`BUILD_SPECIFICATION = FROZEN`

`FIXTURE_BUILD_AUTHORIZATION = NOT GRANTED`

`PRE_EXECUTION_GATE = BLOCKED`

The next governance decision is whether to authorize **Phase A fixture construction only**. Authorization of fixture construction must not be interpreted as authorization to invoke `AWS-PatchAsgInstance` or the comparator.
