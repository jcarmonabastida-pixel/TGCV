# IT-G1 — AWSSupport-ExecuteEC2Rescue Instance Role Trust Policy Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Observed state

Role: `IT-G1-EC2Rescue-InstanceRole`

ARN: `arn:aws:iam::502731779370:role/IT-G1-EC2Rescue-InstanceRole`

Trust policy: `ec2.amazonaws.com` is allowed to perform `sts:AssumeRole`.

Maximum session duration: `3600` seconds.

## Interpretation boundary

The observed trust relationship is consistent with use of the role through an EC2 instance profile. It does not establish that this role is suitable as the SSM Automation `AutomationAssumeRole`, nor does it establish complete effective permissions for the EC2Rescue workflow. Trust and permissions are separate authorization dimensions.

No IAM modification was performed. No SSM Automation was started.

**Execution status:** `NOT_EXECUTED`
