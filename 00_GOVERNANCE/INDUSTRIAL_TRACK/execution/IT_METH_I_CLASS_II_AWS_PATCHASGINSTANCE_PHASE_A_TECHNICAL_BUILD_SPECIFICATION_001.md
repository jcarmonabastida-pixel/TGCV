# IT-METH-I — Class II AWS-PatchAsgInstance Phase A Technical Build Specification 001

**Date:** 2026-09-10  
**Status:** `TECHNICAL BUILD SPECIFICATION FROZEN — PHASE A AUTHORIZED / EXECUTION NOT YET PERFORMED`  
**Evidence class:** `CLASS II — PUBLIC REPRODUCIBLE FIXTURE`  
**Candidate:** `AWS-PatchAsgInstance`  
**Parent design:** `IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_EXPERIMENT_DESIGN_001.md`  
**Parent state contract:** `IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_PREDECISION_STATE_AND_COMPARATOR_CONTRACT_001.md`  
**Parent build specification:** `IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_CONTROLLED_FIXTURE_BUILD_SPECIFICATION_001.md`  
**Authorization:** `IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_FIXTURE_BUILD_AUTHORIZATION_001.md`

## 1. Scope

This specification operationalizes **Phase A only**: controlled fixture construction and pre-decision state freeze. It does not authorize candidate transformation, comparator transformation, utility scoring, industrial execution, or TGCV Core modification.

## 2. Frozen source composition

The build consumes the already frozen Class II public composition. No source substitution, latest-version resolution, or silent input replacement is permitted.

Required source artifacts and expected SHA-256 values:

- ASG template: `D10B323570774C9D4C07547A8035EB7D6B3D907E83CF0DDF95A8EDC73D02C339`
- Patch workshop template: `FD1C09C1FD200BC14A8039F00BF15AB3E894DE5DBA15315A07C375FD2ECEF5E2`
- AWS-PatchAsgInstance runbook: `EFC2F49FFA368EFF1BF768F71E74F7BC518C136EDE03ABAAB97D5B966DC3C4EB`

The source Git commits remain those frozen in the composition manifest; this specification does not amend them.

## 3. Minimum fixture boundary

The fixture shall contain only resources required to instantiate and observe the target state:

1. one dedicated Auto Scaling Group;
2. one launch template/version used by that ASG;
3. at least one target EC2 instance;
4. networking required for the instance and SSM connectivity;
5. one explicit patch baseline and patch-group assignment;
6. minimum IAM required for management and observation;
7. no production resources and no unrelated workload resources.

The ASG source structure is the starting public fixture composition. Dynamic/latest values must be resolved at instantiation and recorded as effective values.

## 4. Required frozen build parameters

Before resource creation, freeze in the execution record:

- AWS region;
- source commit identifiers and source hashes;
- canonical local source paths/references bound to those hashes;
- CloudFormation/template identity;
- dedicated fixture stack/name prefix;
- ASG desired/min/max capacity;
- launch-template identity/version;
- instance type;
- exact effective AMI/image ID;
- OS identity;
- health-check type;
- lifecycle hooks and relevant replacement/termination behavior;
- Patch Group key/value;
- patch baseline identity/version;
- SSM configuration and required IAM role identities;
- candidate transformation identity and frozen parameter vector;
- comparator transformation identity, implementation/procedure reference, and eligibility predicates;
- effort measurement status and convention (`EFFORT_MEASURED = TRUE/FALSE`);
- pre-decision observation window and exact UTC cutoff.

Any dynamic value such as a public latest-AMI parameter must be resolved once and frozen; it must not remain an implicit moving input.

## 5. Build sequence

Execute in this order:

1. recover canonical inputs from GitHub;
2. run static source-integrity preflight, including path-to-hash binding;
3. verify AWS CLI and caller identity;
4. create the isolated fixture infrastructure;
5. resolve and record effective resource identifiers;
6. wait for instance stabilization;
7. verify SSM managed-instance registration;
8. verify Patch Group and effective baseline assignment;
9. establish the pre-decision observation window and exact UTC cutoff;
10. capture the mandatory pre-decision observation set, preserving individual capture times;
11. capture pre-decision patch compliance state;
12. capture ASG capacity and launch-template state;
13. capture instance image/OS identity;
14. capture health, lifecycle and replacement configuration/state;
15. evaluate the frozen accessibility predicates from observations within the pre-decision boundary only;
16. freeze the evidence package and SHA-256 inventory;
17. perform the independent reconstruction check;
18. stop.

No candidate or comparator transformation may occur in this sequence.

## 6. Mandatory pre-decision evidence record

The Phase A record must contain, at minimum:

- fixture identifier;
- source provenance, canonical local references and hashes;
- region;
- ASG identity and desired/min/max;
- target instance identity;
- launch-template identity/version;
- effective AMI ID and OS identity;
- health state at cutoff;
- lifecycle hooks/state;
- health-check and replacement/termination behavior;
- Patch Group state;
- effective patch baseline identity/version and assignment;
- pre-decision patch compliance state;
- SSM managed-instance state;
- accessibility predicates and their evidence variables;
- candidate transformation identity and frozen parameter vector;
- comparator identity, implementation/procedure reference and eligibility predicates;
- effort measurement status/convention;
- exact UTC cutoff and pre-decision observation window;
- raw observation references with individual capture times;
- evidence-file SHA-256 values;
- independent reconstruction result.

A field is `CLOSED` only when directly observed or independently reconstructed within the declared pre-decision observation boundary. Missing, out-of-window, or post-decision-derived values remain `NOT_CLOSED`.

## 7. Observation consistency

The executor shall preserve the distinction between the declared common cutoff and the individual capture time of each observation.

All mandatory state observations must be captured within the declared pre-decision observation window. If the observations cannot be bounded sufficiently to support a common frozen state representation, Phase A closure is blocked.

The accessibility predicates must consume only evidence captured at or before the cutoff. No later observation may retroactively alter a pre-decision predicate.

## 8. Independent reconstruction

A second reconstruction must use the same frozen public source package and independently reproduce the pre-decision state representation.

Agreement is required for:

- resource identities;
- state variables and values;
- effective image/baseline;
- health/lifecycle/replacement state;
- Patch Group and compliance state;
- SSM state;
- accessibility predicates;
- candidate transformation identity and parameters;
- comparator identity and operationalization;
- cutoff and observation window;
- provenance;
- effort status/convention where applicable.

Material disagreement blocks Phase A closure.

## 9. Comparator and effort freeze

Phase A must freeze the comparator definition without executing it. The comparator must be operationally explicit and tied to the same pre-decision state/evidence boundary.

If effort is measured, its measurement convention and boundary must be frozen before observations are interpreted. If effort is not measured, the evidence record shall state `EFFORT_MEASURED = FALSE`.

Neither comparator execution nor utility scoring is part of Phase A.

## 10. Failure conditions

Phase A must terminate as blocked if any of the following occurs:

- source hash mismatch;
- missing mandatory source;
- unauthorized governance state;
- AWS identity unavailable;
- required resource cannot be instantiated;
- target state cannot be uniquely identified;
- effective AMI or baseline cannot be frozen;
- health/lifecycle/replacement state cannot be observed;
- pre-decision compliance cannot be observed;
- SSM state cannot be established;
- accessibility predicates cannot be evaluated without post-decision information;
- mandatory observations fall outside the declared pre-decision boundary;
- evidence cannot be preserved and hashed;
- independent reconstruction materially disagrees;
- comparator identity/operationalization is not frozen;
- required effort convention is absent when effort is measured.

No partial Phase A record may be promoted to `CLOSED`.

## 11. Runtime and cost boundary

The fixture must be minimal and disposable. Runtime duration, resource identifiers, and cleanup status shall be recorded. Any cost-bearing resource must be explicitly within the authorized fixture boundary.

The build does not authorize persistence beyond what is required for evidence capture.

## 12. Execution boundary

`PHASE_A_FIXTURE_BUILD = AUTHORIZED`

`PREDECISION_STATE_FREEZE = AUTHORIZED`

`CANDIDATE_TRANSFORMATION = NOT AUTHORIZED`

`COMPARATOR_TRANSFORMATION = NOT AUTHORIZED`

`UTILITY_SCORING = NOT AUTHORIZED`

`INDUSTRIAL_EXECUTION = NOT AUTHORIZED`

`TGCV_CORE_MODIFICATION = NOT AUTHORIZED`

## 13. Current gate

`TECHNICAL_BUILD_SPECIFICATION = FROZEN`

`PHASE_A_EXECUTION = NOT YET PERFORMED`

`PRE_EXECUTION_TRANSFORMATION_GATE = BLOCKED`

This record makes the authorized Phase A build operationally explicit. It does not itself constitute evidence that the fixture has been instantiated.
