# IT-G1 — AWSSupport-ExecuteEC2Rescue Caller EC2 Full Access Policy Version 005 Observed State 002

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Acquisition

Command executed locally:

```powershell
aws iam get-policy-version --profile tgcv --policy-arn arn:aws:iam::aws:policy/AmazonEC2FullAccess --version-id v5 --query "PolicyVersion.Document" --output json --no-cli-pager
```

## Observed policy

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Action": "ec2:*",
            "Effect": "Allow",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "elasticloadbalancing:*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "cloudwatch:*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "autoscaling:*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iam:AWSServiceName": [
                        "autoscaling.amazonaws.com",
                        "ec2scheduled.amazonaws.com",
                        "elasticloadbalancing.amazonaws.com",
                        "spot.amazonaws.com",
                        "spotfleet.amazonaws.com",
                        "transitgateway.amazonaws.com"
                    ]
                }
            }
        }
    ]
}
```

## Observation

The caller's directly attached `AmazonEC2FullAccess` policy, version `v5`, grants `ec2:*` on `*`, plus broad Elastic Load Balancing, CloudWatch, and Auto Scaling permissions, and the listed conditional service-linked-role creation permission.

## Interpretation boundary

This provides strong direct-policy evidence for broad EC2 authorization by the caller. It does not, by itself, establish complete effective authorization for the full `AWSSupport-ExecuteEC2Rescue` runbook and nested workflow, nor does it establish that execution should be initiated. Other authorization layers and runbook prerequisites remain separate evidence dimensions.

No IAM modification was performed. No SSM Automation was started.

**Execution status:** `NOT_EXECUTED`
