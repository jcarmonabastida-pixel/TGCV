# IT-G1 — AWSSupport-ExecuteEC2Rescue Caller CloudFormation Full Access Policy Version 001 Observed State 002

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Acquisition

Command executed locally:

```powershell
aws iam get-policy-version --profile tgcv --policy-arn arn:aws:iam::aws:policy/AWSCloudFormationFullAccess --version-id v1 --query "PolicyVersion.Document" --output json --no-cli-pager
```

## Observed policy

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudformation:*"
            ],
            "Resource": "*"
        }
    ]
}
```

## Interpretation boundary

The caller's directly attached `AWSCloudFormationFullAccess` policy, version `v1`, grants broad CloudFormation actions on all resources. This is direct-policy evidence only. It does not establish complete effective authorization for the EC2Rescue runbook or nested workflow, nor does it establish execution authorization.

No IAM modification was performed. No SSM Automation was started.

**Execution status:** `NOT_EXECUTED`
