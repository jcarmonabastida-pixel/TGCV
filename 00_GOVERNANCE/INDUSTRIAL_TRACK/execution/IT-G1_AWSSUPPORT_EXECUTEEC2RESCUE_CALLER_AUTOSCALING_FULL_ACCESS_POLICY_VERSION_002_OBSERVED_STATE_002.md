# IT-G1 — AWSSupport-ExecuteEC2Rescue Caller AutoScaling Full Access Policy Version 002 Observed State 002

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Acquisition

Command executed locally:

```powershell
aws iam get-policy-version --profile tgcv --policy-arn arn:aws:iam::aws:policy/AutoScalingFullAccess --version-id v2 --query "PolicyVersion.Document" --output json --no-cli-pager
```

## Observed policy

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "autoscaling:*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "cloudwatch:PutMetricAlarm",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:DescribeAccountAttributes",
                "ec2:DescribeAvailabilityZones",
                "ec2:DescribeImages",
                "ec2:DescribeInstanceAttribute",
                "ec2:DescribeInstances",
                "ec2:DescribeKeyPairs",
                "ec2:DescribeLaunchTemplateVersions",
                "ec2:DescribePlacementGroups",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeSpotInstanceRequests",
                "ec2:DescribeSubnets",
                "ec2:DescribeVpcClassicLink"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "elasticloadbalancing:DescribeLoadBalancers",
                "elasticloadbalancing:DescribeTargetGroups"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "iam:CreateServiceLinkedRole",
            "Resource": "*",
            "Condition": {
                "StringEquals": {
                    "iam:AWSServiceName": "autoscaling.amazonaws.com"
                }
            }
        }
    ]
}
```

## Observation

The caller's directly attached `AutoScalingFullAccess` policy, version `v2`, grants `autoscaling:*` on `*`, `cloudwatch:PutMetricAlarm`, selected EC2 describe actions, selected Elastic Load Balancing describe actions, and conditional creation of the Auto Scaling service-linked role.

## Interpretation boundary

This provides direct-policy evidence for broad Auto Scaling permissions and the listed supporting actions. It does not by itself establish complete effective authorization for every action/resource used by `AWSSupport-ExecuteEC2Rescue` or its nested workflow. The policy also does not itself establish execution authorization or any incident/prerequisite condition.

No IAM modification was performed. No SSM Automation was started.

**Execution status:** `NOT_EXECUTED`
