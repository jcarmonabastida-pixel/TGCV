# IT-G1 — AWSSupport-ExecuteEC2Rescue Caller Group Membership Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Acquisition

Command executed locally:

```powershell
aws iam list-groups-for-user --profile tgcv --user-name tgcv-experiment --query "Groups[].{GroupName:GroupName,GroupId:GroupId,Arn:Arn}" --output table --no-cli-pager
```

## Observed result

The command returned no groups for IAM user `tgcv-experiment`.

Therefore, no IAM group membership was returned for the caller at the observed instant.

## Interpretation boundary

This establishes that the caller has no groups returned by `list-groups-for-user`; consequently, group-attached policies are not an observed source of permissions for this principal.

The result does not by itself establish the complete effective permission set. Permission boundaries, session policies, resource policies, organizational controls, and other applicable IAM mechanisms remain separate considerations.

No IAM modification was performed. No SSM Automation was started.

**Execution status:** `NOT_EXECUTED`
