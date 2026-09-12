# IT-G1 — AWSSupport-ExecuteEC2Rescue Caller SSM Execution Authorization Simulation 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Acquisition

Command executed locally:

```powershell
aws iam simulate-principal-policy --profile tgcv --policy-source-arn arn:aws:iam::502731779370:user/tgcv-experiment --action-names ssm:StartAutomationExecution ssm:GetAutomationExecution ssm:DescribeAutomationExecutions --output json --no-cli-pager
```

## Observed result

All three tested actions returned `EvalDecision: allowed` with no missing context values:

| Action | Decision | Matched policy |
|---|---|---|
| `ssm:StartAutomationExecution` | `allowed` | `AmazonSSMFullAccess` |
| `ssm:GetAutomationExecution` | `allowed` | `AmazonSSMFullAccess` |
| `ssm:DescribeAutomationExecutions` | `allowed` | `AmazonSSMFullAccess` |

The matching statement was reported as an IAM policy statement from `AmazonSSMFullAccess`, with no `MissingContextValues` for the tested evaluations.

## Interpretation boundary

This is direct IAM policy simulation evidence for the tested caller actions. It establishes that, under the simulation inputs supplied, these three SSM actions evaluate as allowed for the caller.

It does **not** establish that `AWSSupport-ExecuteEC2Rescue` would successfully execute. In particular, the simulation does not establish all resource-specific conditions, all nested-workflow actions, AutomationAssumeRole suitability, runbook prerequisites, target incident state, or the complete effective authorization context of the real execution request.

No SSM Automation was started. No IAM modification was performed.

**Execution status:** `NOT_EXECUTED`
