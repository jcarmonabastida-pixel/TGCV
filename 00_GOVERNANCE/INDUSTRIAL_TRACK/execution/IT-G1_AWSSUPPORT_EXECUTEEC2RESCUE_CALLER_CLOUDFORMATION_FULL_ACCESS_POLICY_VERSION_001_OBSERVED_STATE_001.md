# IT-G1 — AWSSupport-ExecuteEC2Rescue Caller CloudFormation Full Access Policy Version 001 Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Acquisition

Policy metadata observed locally:

- PolicyName: `AWSCloudFormationFullAccess`
- PolicyArn: `arn:aws:iam::aws:policy/AWSCloudFormationFullAccess`
- DefaultVersionId: `v1`
- AttachmentCount: `1`

## Interpretation boundary

The caller has the AWS-managed `AWSCloudFormationFullAccess` policy directly attached, with default version `v1` observed. This artifact records policy metadata only; the exact statement content of version `v1` must be observed separately before making action-level authorization claims.

Policy attachment alone does not establish complete effective authorization for the EC2Rescue runbook or its nested workflow. Other authorization layers and service-specific conditions remain separate evidence dimensions.

No IAM modification was performed. No SSM Automation was started.

**Execution status:** `NOT_EXECUTED`
