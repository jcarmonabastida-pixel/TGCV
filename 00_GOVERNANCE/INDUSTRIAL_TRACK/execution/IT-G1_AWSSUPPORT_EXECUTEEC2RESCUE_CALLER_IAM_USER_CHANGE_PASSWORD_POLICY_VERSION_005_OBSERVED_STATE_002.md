# IT-G1 — AWSSupport-ExecuteEC2Rescue Caller IAM User Change Password Policy Version 005 Observed State 002

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Acquisition

Command executed locally:

```powershell
aws iam get-policy-version --profile tgcv --policy-arn arn:aws:iam::aws:policy/IAMUserChangePassword --version-id v5 --query "PolicyVersion.Document" --output json --no-cli-pager
```

## Observed policy

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "iam:ChangePassword"
            ],
            "Resource": [
                "arn:aws:iam::*:user/${aws:username}",
                "arn:aws:iam::*:user/*/${aws:username}"
            ]
        },
        {
            "Effect": "Allow",
            "Action": [
                "iam:GetAccountPasswordPolicy"
            ],
            "Resource": "*"
        }
    ]
}
```

## Observation

The caller's directly attached `IAMUserChangePassword` policy, version `v5`, grants `iam:ChangePassword` for the current IAM username resource patterns and `iam:GetAccountPasswordPolicy` on `*`.

## Interpretation boundary

These permissions are unrelated to the core EC2Rescue automation path except for general IAM context. This artifact does not establish complete effective authorization for the runbook or nested workflow and does not establish execution authorization.

No IAM modification was performed. No SSM Automation was started.

**Execution status:** `NOT_EXECUTED`
