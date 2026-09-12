# IT-G1 — AWSSupport-ExecuteEC2Rescue Caller SSM Full Access Policy Version 004 Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Acquisition

Command executed locally:

```powershell
aws iam get-policy-version --profile tgcv --policy-arn arn:aws:iam::aws:policy/AmazonSSMFullAccess --version-id v4 --query "PolicyVersion.Document" --output json --no-cli-pager
```

## Observed policy

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:PutMetricData",
                "ds:CreateComputer",
                "ds:DescribeDirectories",
                "ec2:DescribeInstanceStatus",
                "logs:*",
                "ssm:*",
                "ec2messages:*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "arn:aws:iam::*:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM*",
            "Condition": {
                "StringLike": {
                    "iam:AWSServiceName": "ssm.amazonaws.com"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:DeleteServiceLinkedRole",
                "iam:GetServiceLinkedRoleDeletionStatus"
            ],
            "Resource": "arn:aws:iam::*:role/aws-service-role/ssm.amazonaws.com/AWSServiceRoleForAmazonSSM*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ssmmessages:CreateControlChannel",
                "ssmmessages:CreateDataChannel",
                "ssmmessages:OpenControlChannel",
                "ssmmessages:OpenDataChannel"
            ],
            "Resource": "*"
        }
    ]
}
```

## Observation

The caller's directly attached `AmazonSSMFullAccess` managed policy is observed at version `v4`. Its primary statement grants `ssm:*` on `Resource: *`, together with the listed CloudWatch, Directory Service, CloudWatch Logs, EC2 instance-status, `ec2messages`, and SSM Messages actions. It also grants the specific IAM service-linked-role actions shown above.

## Interpretation boundary

This establishes the content of one directly attached managed policy version. Combined with the previously observed caller identity, absence of caller inline policies, absence of caller groups, absence of a permissions boundary, and absence of AWS Organizations membership, it provides strong evidence that these observed layers do not constrain the caller through an explicit deny.

It does **not** by itself establish complete effective authorization for every action/resource required by `AWSSupport-ExecuteEC2Rescue`. In particular, the other directly attached policies, resource-based policies, session policies, and any applicable service-specific authorization conditions remain separate evidence dimensions. The runbook's `AutomationAssumeRole` semantics also remain relevant: the document permits an empty value, in which case the permissions of the starting caller are used.

No IAM modification was performed. No SSM Automation was started.

**Execution status:** `NOT_EXECUTED`
