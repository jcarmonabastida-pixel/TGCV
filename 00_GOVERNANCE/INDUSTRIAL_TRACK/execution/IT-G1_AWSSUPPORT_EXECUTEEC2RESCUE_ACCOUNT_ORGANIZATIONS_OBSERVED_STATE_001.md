# IT-G1 — AWSSupport-ExecuteEC2Rescue Account Organizations Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Acquisition

Command executed locally:

```powershell
aws organizations describe-account --profile tgcv --account-id 502731779370 --query "Account.{Id:Id,Arn:Arn,Name:Name,Email:Email,Status:Status}" --output json --no-cli-pager
```

## Observed result

AWS returned:

```text
AWSOrganizationsNotInUseException: Your account is not a member of an organization.
```

## Observation

Account `502731779370` is not a member of an AWS Organization. Consequently, no AWS Organizations Service Control Policy (SCP) applies to this account through an AWS Organizations hierarchy.

## Interpretation boundary

This removes AWS Organizations/SCP membership as an observed authorization-control layer for the account. It does not establish complete effective IAM authorization and does not exclude other authorization mechanisms applicable to the principal or resources.

No IAM modification was performed. No SSM Automation was started.

**Execution status:** `NOT_EXECUTED`
