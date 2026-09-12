# IT-G1 — AWSSupport-ExecuteEC2Rescue Caller IAM Full Access Policy Version 002 Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Acquisition

Command executed locally:

```powershell
aws iam get-policy-version --profile tgcv --policy-arn arn:aws:iam::aws:policy/IAMFullAccess --version-id v2 --query "PolicyVersion.Document" --output json --no-cli-pager
```

## Observed policy

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam:*",
                "organizations:DescribeAccount",
                "organizations:DescribeOrganization",
                "organizations:DescribeOrganizationalUnit",
                "organizations:DescribePolicy",
                "organizations:ListChildren",
                "organizations:ListParents",
                "organizations:ListPoliciesForTarget",
                "organizations:ListRoots",
                "organizations:ListPolicies",
                "organizations:ListTargetsForPolicy"
            ],
            "Resource": "*"
        }
    ]
}
```

## Observation

The caller's directly attached `IAMFullAccess` managed policy is observed at version `v2`, granting `iam:*` on `Resource: *` and the listed read-only AWS Organizations actions on `Resource: *`.

## Interpretation boundary

This establishes the content of one directly attached managed policy version. It supports the conclusion that the caller has broad direct IAM permissions through this policy, subject to any other authorization layers applicable to the request.

The observed policy does not itself establish that a particular IAM role is suitable as `AutomationAssumeRole`, nor does it establish complete effective authorization for every action performed by the runbook and its nested workflow. Trust policy, role permissions, resource-based policies, session policies, and service-specific conditions remain separate evidence dimensions.

No IAM modification was performed. No SSM Automation was started.

**Execution status:** `NOT_EXECUTED`
