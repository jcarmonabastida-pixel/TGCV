# IT-G1 — AWSSupport-ExecuteEC2Rescue Caller Inline Policies Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Acquisition

Command executed locally:

```powershell
aws iam list-user-policies --profile tgcv --user-name tgcv-experiment --query "PolicyNames" --output table --no-cli-pager
```

## Observed result

The command returned no policy names for IAM user `tgcv-experiment`.

Therefore, no inline policy is directly attached to the user under the IAM `User` resource.

## Interpretation boundary

This observation complements the directly attached managed-policy inventory recorded separately. It does not establish the user's complete effective permission set because permissions may also arise through group membership, permission boundaries, session policies, resource policies, or applicable organizational controls.

No IAM modification was performed. No SSM Automation was started.

**Execution status:** `NOT_EXECUTED`
