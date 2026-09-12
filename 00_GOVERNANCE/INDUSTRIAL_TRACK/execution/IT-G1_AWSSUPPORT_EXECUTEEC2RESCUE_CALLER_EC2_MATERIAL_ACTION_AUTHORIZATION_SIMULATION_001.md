# IT-G1 — AWSSupport-ExecuteEC2Rescue Caller EC2 Material Action Authorization Simulation 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Acquisition

The caller principal `arn:aws:iam::502731779370:user/tgcv-experiment` was evaluated with IAM policy simulation for the EC2 actions identified as material to the observed EC2Rescue workflow:

- `ec2:DescribeInstances`
- `ec2:DescribeVolumes`
- `ec2:CreateSnapshot`
- `ec2:CreateImage`
- `ec2:RunInstances`
- `ec2:StopInstances`
- `ec2:StartInstances`
- `ec2:TerminateInstances`
- `ec2:AttachVolume`
- `ec2:DetachVolume`

## Observed result

All ten tested actions returned `EvalDecision: allowed` and all returned `MissingContextValues: []`.

| Action | Decision | Matching policy evidence |
|---|---|---|
| `ec2:DescribeInstances` | `allowed` | `AmazonEC2FullAccess`; `AutoScalingFullAccess` |
| `ec2:DescribeVolumes` | `allowed` | `AmazonEC2FullAccess` |
| `ec2:CreateSnapshot` | `allowed` | `AmazonEC2FullAccess` |
| `ec2:CreateImage` | `allowed` | `AmazonEC2FullAccess` |
| `ec2:RunInstances` | `allowed` | `AmazonEC2FullAccess` |
| `ec2:StopInstances` | `allowed` | `AmazonEC2FullAccess` |
| `ec2:StartInstances` | `allowed` | `AmazonEC2FullAccess` |
| `ec2:TerminateInstances` | `allowed` | `AmazonEC2FullAccess` |
| `ec2:AttachVolume` | `allowed` | `AmazonEC2FullAccess` |
| `ec2:DetachVolume` | `allowed` | `AmazonEC2FullAccess` |

## Interpretation boundary

This is IAM policy simulation evidence that the tested EC2 actions evaluate as allowed for the caller under the supplied simulation inputs. It materially strengthens the authorization evidence for the EC2 action layer of the workflow.

It does **not** establish successful execution of any of these actions, nor does it establish that the complete `AWSSupport-ExecuteEC2Rescue` workflow is executable. In particular, it does not establish all resource-specific conditions, dependent IAM actions, service-linked-role requirements, nested Automation actions, `AutomationAssumeRole` suitability, networking prerequisites, helper-resource prerequisites, runbook preconditions, or the complete effective authorization context of a real execution request.

No EC2 resource mutation was performed by this observation. No SSM Automation was started. No IAM modification was performed.

**Execution status:** `NOT_EXECUTED`
