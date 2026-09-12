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

The IAM user `tgcv-experiment` has no permissions boundary configured.

## Interpretation boundary

This establishes that no IAM permissions boundary is attached directly to the caller user at the observed instant. Together with the preceding observations, no direct inline policy and no group membership have been observed for this user.

This still does not establish the complete effective authorization context: session policies, resource policies, applicable organizational controls, and other IAM evaluation mechanisms remain separate considerations.

No IAM modification was performed. No SSM Automation was started.

**Execution status:** `NOT_EXECUTED`
