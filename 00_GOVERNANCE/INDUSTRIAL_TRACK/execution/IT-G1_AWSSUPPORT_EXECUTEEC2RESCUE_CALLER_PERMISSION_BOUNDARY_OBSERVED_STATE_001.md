# IT-G1 — AWSSupport-ExecuteEC2Rescue Caller Permission Boundary Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Acquisition

Command executed locally:

```powershell
aws iam get-user --profile tgcv --user-name tgcv-experiment --query "User.{UserName:UserName,Arn:Arn,PermissionsBoundary:PermissionsBoundary}" --output json --no-cli-pager
```

## Observed result

```json
{
    "UserName": "tgcv-experiment",
    "Arn": "arn:aws:iam::502731779370:user/tgcv-experiment",
    "PermissionsBoundary": null
}
```

## Observation

No permissions boundary is attached to IAM user `tgcv-experiment` at the observed instant.

## Interpretation boundary

This removes a directly attached IAM permissions boundary as an observed constraint on the caller. It does not establish the caller's complete effective authorization context. Session policies, resource policies, AWS Organizations controls, SCPs, and other applicable authorization mechanisms remain separate considerations.

No IAM modification was performed. No SSM Automation was started.

**Execution status:** `NOT_EXECUTED`
