# IT-METH-I — Class II AWS-PatchAsgInstance Phase-B Accessibility Comparison Protocol 001

**Date:** 2026-09-11  
**Status:** `DESIGN FROZEN — COMPARISON EXECUTION NOT YET AUTHORIZED`  
**Candidate:** `AWS-PatchAsgInstance`  
**Comparator:** `DIRECT-AWS-SSM-RUNCOMMAND-PATCHBASELINE`  
**Evidence class:** `CLASS II — PUBLIC REPRODUCIBLE FIXTURE`  
**Parent closure:** `IT-METH-I_CLASS_II_AWS_PATCHASGINSTANCE_PHASE_A_RECONSTRUCTION_CLOSURE_001.md`  
**Parent contract:** `IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_PREDECISION_STATE_AND_COMPARATOR_CONTRACT_001.md`

## 1. Purpose

Define the next bounded operation after the closed Phase-A predecision reconstruction gate: an ex-ante, fixture-level comparison of the accessibility conditions of a candidate transformation and an explicit conventional comparator.

This protocol does **not** authorize transformation execution, utility scoring, causal inference, financial/value assessment, production testing, or industrial-case admission.

## 2. Frozen common boundary

The comparison shall use the already closed Phase-A predecision reconstruction boundary as the common state/evidence reference.

Required common inputs:

- frozen ASG identity and source/reference;
- frozen target EC2 identity;
- frozen ASG capacity state;
- frozen launch-template identity/version;
- frozen effective AMI/image identity;
- frozen OS identity;
- frozen health/lifecycle/replacement state;
- frozen Patch Group state;
- frozen effective patch baseline identity/version and assignment;
- frozen predecision patch compliance state;
- frozen SSM managed-instance state;
- frozen evidence provenance;
- frozen predecision cutoff;
- closed independent reconstruction comparison showing exact agreement.

No post-decision execution output may be used to define this common boundary.

## 3. Transformation identities

### 3.1 Candidate

`T_candidate = AWS-PatchAsgInstance(InstanceId, frozen parameters)`

The candidate parameter vector is the vector frozen by the parent comparator contract:

- `InstanceId` = frozen target instance;
- `AutomationAssumeRole` = explicit value if used, otherwise documented omission;
- `LambdaRoleArn` = explicit value if used, otherwise documented omission;
- `WaitForInstance` = `PT2M` unless amended under governance;
- `WaitForReboot` = `PT5M` unless amended under governance.

### 3.2 Comparator

`T_comparator = AWS-SSM-RunCommand(AWS-RunPatchBaseline, same target, frozen patch parameters)`

For the accessibility comparison, the comparator is defined as a direct Systems Manager Run Command invocation of the patch-baseline execution path on the same frozen target, using the same frozen patch-group/baseline context and an explicitly frozen operation/parameter vector.

The comparator must be represented by an operationally explicit invocation, not a generic label such as “normal patching”.

## 4. Accessibility object

For each transformation:

`A(T | S_t, E_t) = (a_1, ..., a_n)`

Each predicate must be anchored to a predecision observable or independently reconstructable condition.

The accessibility comparison shall distinguish at least the following dimensions:

1. target resolvability;
2. required SSM registration/readiness;
3. required resource-state predicates;
4. required patch-group/baseline resolution;
5. required IAM/role availability;
6. required API/operation permission availability;
7. required parameter completeness;
8. required temporal availability;
9. required dependency availability;
10. evidence sufficiency at the cutoff.

## 5. Predicate evaluation rule

Each predicate is classified as:

- `PASS` — directly supported by frozen predecision evidence;
- `FAIL` — directly contradicted by frozen predecision evidence;
- `UNRESOLVED` — required evidence is absent or ambiguous.

`UNRESOLVED` is not converted to `PASS` by inference.

A candidate/comparator accessibility distinction is admissible only when:

1. the predicate is evaluated from the same common state/evidence boundary; and
2. the predicate result differs, or the transformation identity introduces a separately demonstrable accessibility requirement/route that is observable before execution.

Post-decision observations cannot create an ex-ante accessibility distinction.

## 6. Candidate/comparator symmetry requirements

The comparison must preserve symmetry on all variables that could independently explain accessibility differences:

- same target;
- same OS/image;
- same patch-group state;
- same effective baseline context;
- same predecision compliance state;
- same observation cutoff;
- same evidence boundary;
- same non-production fixture boundary.

Any asymmetry that can itself explain the comparison is recorded as a confounder and blocks an accessibility superiority interpretation.

## 7. Metric contract

Phase B evaluates **accessibility structure**, not utility.

Primary comparison outputs:

- predicate-by-predicate accessibility vector for candidate;
- predicate-by-predicate accessibility vector for comparator;
- set/vector of predecision differences;
- unresolved predicates;
- symmetry/confounder assessment.

No scalar utility score is assigned.

A simple structural summary may be reported as:

`ΔA = A_candidate - A_comparator`

where `ΔA` is treated as a descriptive difference in predicate states, not as a utility or value measure.

## 8. Execution boundary

Phase B is split into two distinct operations:

### B0 — Read-only accessibility preflight

Permitted:

- load the closed Phase-A evidence package;
- load the frozen source/provenance package;
- inspect the concrete target and runtime configuration read-only;
- inspect candidate/comparator prerequisites read-only;
- evaluate the frozen accessibility predicates;
- produce and seal an accessibility-comparison artifact.

Forbidden during B0:

- starting the candidate transformation;
- starting the comparator transformation;
- changing the fixture;
- modifying Patch Group/baseline state;
- changing IAM permissions;
- changing the target state;
- using post-decision outcomes.

### B1 — Transformation execution

Not covered by this protocol. Any candidate or comparator execution requires a separate explicit authorization record after B0 integrity and accessibility closure.

## 9. Independence and provenance

Phase B may consume the closed Phase-A reconstruction result as a frozen common-state input because Phase A is already closed and its seal/comparison have been independently verified.

Phase B must not:

- alter the Phase-A closure;
- replace any frozen value with a later observed value;
- treat Phase-A reproducibility as evidence of utility;
- import candidate/comparator outcome information.

All Phase-B output must identify its exact source artifact(s), hashes and cutoff.

## 10. Closure criteria for B0

B0 may close only if:

- the common predecision boundary is loaded and intact;
- candidate identity is explicit;
- comparator identity is explicit;
- all required accessibility predicates are defined before evaluation;
- each predicate has an evidence anchor;
- candidate and comparator are evaluated symmetrically;
- unresolved conditions are retained as unresolved;
- no transformation is executed;
- the comparison artifact is sealed;
- the protocol version and executable version, if any, are recorded.

## 11. Interpretation limits

A Phase-B result, even if it shows a non-empty `ΔA`, does **not** establish:

- industrial utility;
- superiority in practical outcomes;
- production benefit;
- causality;
- financial/value realization;
- predictive validity;
- generalization beyond the fixture;
- Class-II to Class-I promotion;
- any TGCV Core modification.

A non-empty accessibility difference is evidence only of a fixture-level difference in predecision accessibility structure under the frozen definitions.

## 12. Governance state

`PHASE_A_PREDECISION_RECONSTRUCTION = CLOSED-PASS`  
`PHASE_B_PROTOCOL = FROZEN-DESIGN`  
`PHASE_B0_READ_ONLY_ACCESSIBILITY_PREFLIGHT = NOT YET PERFORMED`  
`CANDIDATE_TRANSFORMATION = NOT AUTHORIZED`  
`COMPARATOR_TRANSFORMATION = NOT AUTHORIZED`  
`UTILITY_SCORING = NOT AUTHORIZED`  
`INDUSTRIAL_CASE_ADMISSION = NOT AUTHORIZED`

## 13. Next operation

The next permissible technical operation is **B0 read-only accessibility preflight** against the frozen Phase-A boundary.

The B0 executable must evaluate only the ex-ante candidate/comparator accessibility predicates and must stop before invoking either transformation.
