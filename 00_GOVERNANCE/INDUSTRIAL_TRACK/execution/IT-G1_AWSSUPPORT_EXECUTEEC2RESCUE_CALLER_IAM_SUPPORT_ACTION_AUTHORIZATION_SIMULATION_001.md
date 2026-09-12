# IT-G1 — AWSSupport-ExecuteEC2Rescue Caller IAM Support Action Authorization Simulation 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Acquisition

IAM policy simulation was performed for caller principal `arn:aws:iam::502731779370:user/tgcv-experiment` against the following support actions:

- `iam:PassRole`
- `iam:GetRole`
- `iam:GetInstanceProfile`
- `iam:CreateRole`
- `iam:CreateInstanceProfile`
- `iam:AddRoleToInstanceProfile`
- `iam:AttachRolePolicy`
- `iam:PutRolePolicy`

`iam:CreateInstanceProfile` was supplied twice in the simulation request; both returned the same `allowed` result.

## Observed result

All submitted evaluations returned `EvalDecision: allowed` with `MissingContextValues: []`.

| Action | Decision | Matching policy |
|---|---|---|
| `iam:PassRole` | `allowed` | `IAMFullAccess` |
| `iam:GetRole` | `allowed` | `IAMFullAccess` |
| `iam:GetInstanceProfile` | `allowed` | `IAMFullAccess` |
| `iam:CreateRole` | `allowed` | `IAMFullAccess` |
| `iam:CreateInstanceProfile` | `allowed` | `IAMFullAccess` |
| `iam:AddRoleToInstanceProfile` | `allowed` | `IAMFullAccess` |
| `iam:AttachRolePolicy` | `allowed` | `IAMFullAccess` |
| `iam:PutRolePolicy` | `allowed` | `IAMFullAccess` |

## Interpretation boundary

This is IAM policy simulation evidence that the tested IAM support actions evaluate as allowed for the caller under the supplied simulation inputs. In particular, `iam:PassRole` is not blocked by the simulated identity-policy layer for the wildcard resource used in this test.

It does **not** establish that any role will actually be passed or created, that a particular role is suitable as `AutomationAssumeRole`, or that the complete nested EC2Rescue workflow is executable. Resource-specific conditions, trust relationships, dependent service actions, runtime context, and other effective authorization mechanisms remain separate questions.

No IAM resource was modified by this observation. No SSM Automation was started. No EC2 remediation was executed.

**Execution status:** `NOT_EXECUTED`
