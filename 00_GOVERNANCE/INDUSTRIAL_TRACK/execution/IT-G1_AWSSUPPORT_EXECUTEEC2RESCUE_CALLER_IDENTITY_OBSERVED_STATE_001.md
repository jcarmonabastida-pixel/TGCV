# IT-G1 — AWSSupport-ExecuteEC2Rescue Caller Identity Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Acquisition

Command executed locally:

```powershell
aws sts get-caller-identity --profile tgcv --no-cli-pager
```

## Observed result

- `UserId`: `AIDAXKDJGFUVFXNANAAZZ`
- `Account`: `502731779370`
- `Arn`: `arn:aws:iam::502731779370:user/tgcv-experiment`

## Interpretation boundary

The AWS CLI profile `tgcv` is authenticated as the IAM user `tgcv-experiment` in account `502731779370`.

This establishes the caller identity used for the current evidence-acquisition session. It does **not** establish that this IAM user has all permissions required to start or complete `AWSSupport-ExecuteEC2Rescue`, nor does it establish authorization to execute the runbook.

If `AutomationAssumeRole` is left empty when the runbook is eventually started, the runbook document states that Systems Manager Automation uses the permissions of the user that starts the runbook. Therefore, the permissions of this principal are directly relevant to a future execution gate.

No IAM modification was performed. No SSM Automation was started.

**Execution status:** `NOT_EXECUTED`
