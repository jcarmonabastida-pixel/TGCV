# IT-G1 — AWSSupport-ExecuteEC2Rescue Instance Role Attached Policies Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

**Purpose:** Record the AWS-managed policies directly attached to the IAM role associated with the controlled EC2 instance, without modifying IAM resources or executing the SSM Automation.

## Observed state

Role:
- Name: `IT-G1-EC2Rescue-InstanceRole`
- ARN: `arn:aws:iam::502731779370:role/IT-G1-EC2Rescue-InstanceRole`

Directly attached managed policy:
- Name: `AmazonSSMManagedInstanceCore`
- ARN: `arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore`

## Acquisition command

```powershell
aws iam list-attached-role-policies --profile tgcv --role-name IT-G1-EC2Rescue-InstanceRole --query "AttachedPolicies[].{PolicyName:PolicyName,PolicyArn:PolicyArn}" --output table --no-cli-pager
```

## Interpretation boundary

The observation establishes that `AmazonSSMManagedInstanceCore` is directly attached to the target instance role. It does **not** establish the complete effective permission set of the role, because inline policies and other relevant IAM relationships have not yet been inspected. It also does not establish that the role satisfies all permissions required by `AWSSupport-ExecuteEC2Rescue` or that any Automation execution is authorized.

No IAM modification was performed.

**Execution status:** `NOT_EXECUTED`
