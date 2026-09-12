# IT-G1 — AWSSupport-ExecuteEC2Rescue Caller AutoScaling Full Access Policy Version 002 Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Acquisition

Policy metadata observed locally:

- PolicyName: `AutoScalingFullAccess`
- PolicyArn: `arn:aws:iam::aws:policy/AutoScalingFullAccess`
- DefaultVersionId: `v2`
- AttachmentCount: `1`

## Interpretation boundary

The caller has the AWS-managed `AutoScalingFullAccess` policy directly attached, with default version `v2` observed. This artifact records policy metadata only; the exact statement content of version `v2` must be observed separately before making action-level authorization claims.

Policy attachment alone does not establish complete effective authorization for the EC2Rescue runbook or its nested workflow. Other authorization layers and service-specific conditions remain separate evidence dimensions.

No IAM modification was performed. No SSM Automation was started.

**Execution status:** `NOT_EXECUTED`
