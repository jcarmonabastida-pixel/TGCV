# IT-METH-I — Class II AWS-PatchAsgInstance B0 Operational Routing Decision 001

**Date:** 2026-09-11  
**Status:** `CLOSED — NO ADMISSIBLE ALTERNATIVE EXECUTION ROUTE WITHIN FROZEN BOUNDARY`  
**Case:** `IT-METH-I-CLASS-II-AWS-PATCHASGINSTANCE`  
**Candidate:** `AWS-PatchAsgInstance`  
**Comparator:** `DIRECT-AWS-SSM-RUNCOMMAND-PATCHBASELINE`  
**Evidence class:** `CLASS II — PUBLIC REPRODUCIBLE FIXTURE`

## 1. Decision scope

This record resolves the routing question raised after the B0 permissions audit:

> Whether the candidate transformation can be executed through an alternative route that remains compatible with the already frozen Phase-A boundary and does not require retrospective alteration of the fixture or permission model.

The decision is bounded to the frozen Phase-A state/evidence boundary and to the candidate identity already defined as `AWS-PatchAsgInstance`.

## 2. Evidence used

Frozen Phase-A evidence establishes:

- `AutomationAssumeRole = OMITTED_UNLESS_FROZEN`;
- `LambdaRoleArn = OMITTED_UNLESS_FROZEN`;
- no concrete candidate service-role ARN was frozen;
- no later-discovered role may be substituted retroactively.

The B0 permissions audit established:

- caller permissions for the previously simulated SSM, CloudFormation, EC2 and IAM actions were `allowed`;
- `lambda:CreateFunction = implicitDeny`;
- `lambda:DeleteFunction = implicitDeny`;
- `lambda:GetFunction = implicitDeny`;
- `lambda:InvokeFunction = implicitDeny`;
- the completed Lambda simulation had `MissingContextValues = []`;
- no IAM or fixture mutation occurred.

Official AWS runbook documentation states that `AWS-PatchAsgInstance` requires the four Lambda actions above, in addition to the other listed permissions, and that `LambdaRoleArn` is optional: when omitted, Automation creates a transient role for the Lambda function. citeturn461512search0

## 3. Alternative-route assessment

### 3.1 Supplying a different Lambda role

Not admissible under the frozen boundary.

Reason: no concrete `LambdaRoleArn` was frozen in Phase A. Introducing a newly discovered role would change the execution preconditions after the predecision freeze and would therefore be retrospective substitution rather than an alternative route within the same frozen candidate definition.

### 3.2 Granting the current caller Lambda permissions

Not admissible as a continuation of B0/B1.

Reason: granting permissions would mutate the authorization state and would create a new execution condition that is not contained in the frozen Phase-A boundary. Such a change would require a separately authorized intervention and a newly defined execution boundary.

### 3.3 Replacing the candidate with direct Run Command

Not an alternative route for the candidate.

Reason: `AWS-SSM-RunCommand(AWS-RunPatchBaseline, ...)` is the explicit comparator transformation, not an implementation-equivalent execution route for `AWS-PatchAsgInstance`. Substituting it would change the transformation identity under comparison.

### 3.4 Executing only the non-Lambda subset of candidate actions

Not admissible.

Reason: the subset would not constitute execution of the frozen `AWS-PatchAsgInstance` transformation. It would define a different transformation.

## 4. Routing decision

The candidate has no admissible alternative execution route that simultaneously preserves:

- the frozen candidate identity;
- the frozen Phase-A predecision boundary;
- the non-mutation constraint;
- the candidate/comparator distinction;
- the explicit execution authorization boundary of Phase B.

Therefore:

`CANDIDATE_ALTERNATIVE_EXECUTION_ROUTE = NONE_ADMISSIBLE`

`B1_CANDIDATE_EXECUTION = BLOCKED`

`B1_COMPARATOR_EXECUTION = NOT AUTHORIZED`

`IAM_REPAIR = NOT AUTHORIZED`

`FIXTURE_REBUILD = NOT REQUIRED`

`RETROSPECTIVE_ROLE_SUBSTITUTION = FORBIDDEN`

## 5. Methodological consequence

The blocker is now an explicit operational condition rather than an unresolved routing question:

`operation_permission_availability = FAIL`

The separate identity condition remains:

`iam_role_availability = UNRESOLVED`

The latter does not weaken or reverse the Lambda permission failure, because the frozen candidate definition does not contain a concrete role identity to evaluate.

## 6. Interpretation limits

This decision does not establish:

- candidate utility;
- comparator superiority;
- production benefit;
- causality;
- financial/value realization;
- predictive validity;
- generalization beyond the fixture;
- Class-II to Class-I promotion;
- any TGCV Core modification.

It establishes only that, under the frozen boundary and current authorization state, the candidate cannot advance to transformation execution through an admissible alternative route.

## 7. Routing state

`PHASE_A_PREDECISION_RECONSTRUCTION = CLOSED-PASS`  
`PHASE_B_PROTOCOL = FROZEN-DESIGN`  
`PHASE_B0_ACCESSIBILITY_PREFLIGHT = CLOSED`  
`PHASE_B0_PERMISSIONS_AUDIT = CLOSED — OPERATION PERMISSION FAIL; IAM ROLE UNRESOLVED`  
`ALTERNATIVE_EXECUTION_ROUTE = NONE-ADMISSIBLE`  
`CANDIDATE_TRANSFORMATION = BLOCKED`  
`COMPARATOR_TRANSFORMATION = NOT AUTHORIZED`  
`UTILITY_SCORING = NOT AUTHORIZED`  
`INDUSTRIAL_CASE_ADMISSION = NOT AUTHORIZED`

## 8. Next permissible action

No AWS mutation or transformation execution is authorized from this record.

The next action may only be a separately authorized change of the execution environment/authorization boundary, followed by a new pre-execution permission assessment. The existing Phase-A frozen boundary must remain historically immutable.
