# IT-G1 — AWSSupport-ExecuteEC2Rescue Caller Attached Policies Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Acquisition

Command executed locally:

```powershell
aws iam list-attached-user-policies --profile tgcv --user-name tgcv-experiment --query "AttachedPolicies[].{PolicyName:PolicyName,PolicyArn:PolicyArn}" --output table --no-cli-pager
```

## Observed result

The IAM user `tgcv-experiment` has the following directly attached AWS-managed policies:

| Policy | ARN |
|---|---|
| `AmazonSSMFullAccess` | `arn:aws:iam::aws:policy/AmazonSSMFullAccess` |
| `AmazonEC2FullAccess` | `arn:aws:iam::aws:policy/AmazonEC2FullAccess` |
| `AutoScalingFullAccess` | `arn:aws:iam::aws:policy/AutoScalingFullAccess` |
| `IAMFullAccess` | `arn:aws:iam::aws:policy/IAMFullAccess` |
| `IAMUserChangePassword` | `arn:aws:iam::aws:policy/IAMUserChangePassword` |
| `AmazonS3FullAccess` | `arn:aws:iam::aws:policy/AmazonS3FullAccess` |
| `AWSCloudFormationFullAccess` | `arn:aws:iam::aws:policy/AWSCloudFormationFullAccess` |

## Interpretation boundary

This establishes the directly attached managed-policy inventory observed for the caller `arn:aws:iam::502731779370:user/tgcv-experiment`.

The inventory shows broad permissions through AWS-managed policies, including Systems Manager, EC2, IAM, and S3 administration. It does **not**, by itself, establish the caller's complete effective permission set because permissions may also arise from inline policies, group membership, permission boundaries, session policies, resource policies, or applicable organizational controls.

Accordingly, this observation is not treated as proof that every action required by `AWSSupport-ExecuteEC2Rescue` or its nested `AWSSupport-StartEC2RescueWorkflow` is permitted. It is also not treated as execution authorization.

No IAM modification was performed. No SSM Automation was started.

**Execution status:** `NOT_EXECUTED`
