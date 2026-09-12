# IT-G1 — AWSSupport-ExecuteEC2Rescue Caller S3 Full Access Policy Version 002 Observed State 002

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Acquisition

Command executed locally:

```powershell
aws iam get-policy-version --profile tgcv --policy-arn arn:aws:iam::aws:policy/AmazonS3FullAccess --version-id v2 --query "PolicyVersion.Document" --output json --no-cli-pager
```

## Observed policy

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*",
                "s3-object-lambda:*"
            ],
            "Resource": "*"
        }
    ]
}
```

## Interpretation boundary

The caller's directly attached `AmazonS3FullAccess` policy, version `v2`, grants broad S3 and S3 Object Lambda actions on all resources. This is direct-policy evidence only. It does not establish complete effective authorization for the EC2Rescue runbook or nested workflow, nor does it establish execution authorization.

This policy is relevant to the runbook's optional S3 logging path, but the observed policy alone does not establish that an S3 log destination has been selected or that all runbook-specific S3 prerequisites are satisfied.

No IAM modification was performed. No SSM Automation was started.

**Execution status:** `NOT_EXECUTED`
