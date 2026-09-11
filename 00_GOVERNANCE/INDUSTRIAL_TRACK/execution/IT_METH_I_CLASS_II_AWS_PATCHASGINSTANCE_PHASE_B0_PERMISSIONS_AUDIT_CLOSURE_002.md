# IT-METH-I — Class II AWS-PatchAsgInstance B0 Permissions Audit Closure 002

**Date:** 2026-09-11  
**Status:** `CLOSED — READ-ONLY PERMISSIONS AUDIT CAPTURED; CANDIDATE OPERATION PERMISSION FAIL`  
**Case:** `IT-METH-I-CLASS-II-AWS-PATCHASGINSTANCE`  
**Candidate:** `AWS-PatchAsgInstance`  
**Comparator:** `DIRECT-AWS-SSM-RUNCOMMAND-PATCHBASELINE`  
**Evidence class:** `CLASS II — PUBLIC REPRODUCIBLE FIXTURE`

## 1. Disposition

This record supersedes the permission-state conclusion of:

`IT_METH_I_CLASS_II_AWS_PATCHASGINSTANCE_PHASE_B0_PERMISSIONS_AUDIT_CLOSURE_001.md`

The earlier closure is historical and remains immutable. This closure records the subsequent bounded read-only IAM simulation that resolved the previously unresolved candidate operation-permission dimension.

## 2. Read-only permission simulation

The frozen caller identity was used as the `policy-source-arn` for IAM policy simulation. No candidate or comparator transformation was invoked and no AWS resource was mutated.

The initial simulation showed `allowed` for the SSM, CloudFormation, EC2 and IAM actions included in the bounded permission probe.

The Lambda-specific follow-up simulation supplied the required `iam:AWSServiceName=lambda.amazonaws.com` context and returned:

| Action | Decision | Missing context | Matched statements |
|---|---|---|---|
| `lambda:CreateFunction` | `implicitDeny` | none | none |
| `lambda:DeleteFunction` | `implicitDeny` | none | none |
| `lambda:GetFunction` | `implicitDeny` | none | none |
| `lambda:InvokeFunction` | `implicitDeny` | none | none |

Therefore the previous `implicitDeny` ambiguity caused by missing simulation context is eliminated.

## 3. Updated disposition

`OPERATION_PERMISSION_AVAILABILITY=FAIL`

Rationale:

1. the required Lambda simulation context was supplied;
2. all four Lambda actions remained `implicitDeny`;
3. `MissingContextValues=[]` for all four actions;
4. no matching allow statement was returned for any of the four actions.

Accordingly the candidate's effective caller-level permission set is insufficient for the bounded execution path represented by this probe.

## 4. IAM role identity status

The Phase-A frozen fields remain:

- `AutomationAssumeRole = OMITTED_UNLESS_FROZEN`;
- `LambdaRoleArn = OMITTED_UNLESS_FROZEN`.

No concrete candidate role ARN is frozen in the Phase-A boundary. No discovered IAM role has been substituted.

Therefore:

`IAM_ROLE_AVAILABILITY=UNRESOLVED`

This remains an evidence-boundary limitation and is not evidence that a role does or does not exist in AWS.

## 5. Guard integrity

All controls remain intact:

- candidate transformation invoked: `False`;
- comparator transformation invoked: `False`;
- Automation execution invoked: `False`;
- `ssm:SendCommand` transformation path invoked: `False`;
- IAM mutated: `False`;
- fixture mutated: `False`;
- read-only guard: `PASS`.

## 6. B0 gate result

`B0_STATUS = CLOSED`

`B0_ACCESSIBILITY_DIFFERENCE = NOT_ESTABLISHED`

`IAM_ROLE_AVAILABILITY = UNRESOLVED`

`OPERATION_PERMISSION_AVAILABILITY = FAIL`

`CANDIDATE_TRANSFORMATION = NOT_AUTHORIZED`

`COMPARATOR_TRANSFORMATION = NOT_AUTHORIZED`

`B1_AUTHORIZATION = BLOCKED`

A failed candidate operation-permission predicate is sufficient to prevent transformation execution. No compensating IAM change is authorized within B0.

## 7. Methodological meaning

This result is a fixture-level methodological finding only. It establishes that the frozen candidate boundary cannot currently support execution through the simulated caller permission path for the required Lambda operations.

It does **not** establish:

- utility;
- practical superiority;
- production benefit;
- causality;
- financial or value realization;
- predictive validity;
- generalization beyond the fixture;
- candidate/comparator superiority as an industrial claim;
- Class-II to Class-I promotion;
- any TGCV Core modification.

## 8. Routing

No B1 transformation execution should be attempted under the current frozen boundary.

Any future permission-resolution work must remain read-only and must use only concretely frozen identities. It must not retroactively alter Phase-A evidence. Any IAM remediation or transformation execution requires a separate explicit authorization record.
