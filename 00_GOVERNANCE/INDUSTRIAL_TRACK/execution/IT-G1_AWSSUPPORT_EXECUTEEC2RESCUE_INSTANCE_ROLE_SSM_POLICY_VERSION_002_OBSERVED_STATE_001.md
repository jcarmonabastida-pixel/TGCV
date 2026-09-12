# IT-G1 — AWSSupport-ExecuteEC2Rescue Instance Role SSM Policy Version 002 Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

**Purpose:** Record the observed default version and effective statements of the AWS-managed `AmazonSSMManagedInstanceCore` policy directly attached to the controlled EC2 instance role.

## Observed policy metadata

- PolicyName: `AmazonSSMManagedInstanceCore`
- PolicyArn: `arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore`
- DefaultVersionId: `v2`
- AttachmentCount: `2`
- Version inspected: `v2`

## Observed permissions

### Statement 1

Effect: `Allow`

Actions:
- `ssm:DescribeAssociation`
- `ssm:GetDeployablePatchSnapshotForInstance`
- `ssm:GetDocument`
- `ssm:DescribeDocument`
- `ssm:GetManifest`
- `ssm:GetParameter`
- `ssm:GetParameters`
- `ssm:ListAssociations`
- `ssm:ListInstanceAssociations`
- `ssm:PutInventory`
- `ssm:PutComplianceItems`
- `ssm:PutConfigurePackageResult`
- `ssm:UpdateAssociationStatus`
- `ssm:UpdateInstanceAssociationStatus`
- `ssm:UpdateInstanceInformation`

Resource: `*`

### Statement 2

Effect: `Allow`

Actions:
- `ssmmessages:CreateControlChannel`
- `ssmmessages:CreateDataChannel`
- `ssmmessages:OpenControlChannel`
- `ssmmessages:OpenDataChannel`

Resource: `*`

### Statement 3

Effect: `Allow`

Actions:
- `ec2messages:AcknowledgeMessage`
- `ec2messages:DeleteMessage`
- `ec2messages:FailMessage`
- `ec2messages:GetEndpoint`
- `ec2messages:GetMessages`
- `ec2messages:SendReply`

Resource: `*`

## Acquisition command

```powershell
aws iam get-policy-version --profile tgcv --policy-arn arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore --version-id v2 --query "PolicyVersion.Document" --output json --no-cli-pager
```

## Interpretation boundary

The observation establishes the effective statements of version `v2` of the directly attached AWS-managed policy. The policy provides the standard SSM managed-instance communication and inventory/update actions represented above.

This observation does **not** establish that the target role has every permission required by `AWSSupport-ExecuteEC2Rescue`, because the Automation may rely on other roles, helper resources, service-linked permissions, resource policies, or additional permissions not provided by this policy.

It also does not establish execution authorization or authorize any remediation.

No IAM modification was performed.

**Execution status:** `NOT_EXECUTED`
