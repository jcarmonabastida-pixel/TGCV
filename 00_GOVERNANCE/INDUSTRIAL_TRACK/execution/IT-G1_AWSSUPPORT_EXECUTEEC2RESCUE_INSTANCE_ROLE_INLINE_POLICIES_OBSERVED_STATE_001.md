# IT-G1 — AWSSupport-ExecuteEC2Rescue Instance Role Inline Policies Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

**Purpose:** Record the observed absence of inline IAM policies directly attached to the target instance role.

## Observed state

Role:
- Name: `IT-G1-EC2Rescue-InstanceRole`
- ARN: `arn:aws:iam::502731779370:role/IT-G1-EC2Rescue-InstanceRole`

Inline policy inventory:
- `PolicyNames`: empty
- Result: no inline policies returned for the role

## Acquisition command

```powershell
aws iam list-role-policies --profile tgcv --role-name IT-G1-EC2Rescue-InstanceRole --query "PolicyNames" --output table --no-cli-pager
```

## Interpretation boundary

The observation establishes that no inline policies were returned for this role at the observation time. Together with the directly attached managed-policy observation, the currently observed direct role policy inventory consists of `AmazonSSMManagedInstanceCore` only.

This does **not** establish the complete effective permission set across all IAM mechanisms, nor that the role satisfies every permission required by `AWSSupport-ExecuteEC2Rescue`.

No IAM modification was performed.

**Execution status:** `NOT_EXECUTED`
