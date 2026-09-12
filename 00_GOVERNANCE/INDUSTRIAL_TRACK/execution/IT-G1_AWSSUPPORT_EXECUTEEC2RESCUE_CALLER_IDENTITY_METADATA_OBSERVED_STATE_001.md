# IT-G1 — AWSSupport-ExecuteEC2Rescue Caller Identity Metadata Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Acquisition

Command executed locally:

```powershell
aws iam get-user --profile tgcv --user-name tgcv-experiment --query "User.{UserName:UserName,Path:Path,CreateDate:CreateDate,PasswordLastUsed:PasswordLastUsed,Tags:Tags}" --output json --no-cli-pager
```

## Observed result

```json
{
    "UserName": "tgcv-experiment",
    "Path": "/",
    "CreateDate": "2026-09-10T18:00:27+00:00",
    "PasswordLastUsed": "2026-09-12T01:19:05+00:00",
    "Tags": [
        {
            "Key": "AKIAXKDJGFUVFH6EGAM4",
            "Value": "tgcv experiment"
        }
    ]
}
```

## Interpretation boundary

This records the observed IAM user metadata returned by `get-user` at the evidence-acquisition instant. The `CreateDate` and `PasswordLastUsed` fields are descriptive metadata only and do not establish authorization, session state, or execution eligibility.

No IAM modification was performed. No SSM Automation was started.

**Execution status:** `NOT_EXECUTED`
