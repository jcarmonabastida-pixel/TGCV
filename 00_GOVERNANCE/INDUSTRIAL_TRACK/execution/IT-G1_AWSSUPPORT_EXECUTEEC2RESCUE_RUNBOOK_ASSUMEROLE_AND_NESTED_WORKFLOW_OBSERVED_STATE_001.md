# IT-G1 — AWSSupport-ExecuteEC2Rescue Runbook AssumeRole and Nested Workflow Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

## Observed runbook structure

The active `AWSSupport-ExecuteEC2Rescue` Automation document (version `1`) declares:

```text
assumeRole: {{ AutomationAssumeRole }}
```

The parameter `AutomationAssumeRole` is optional. Its documented behavior is that, when supplied, Systems Manager Automation uses that IAM role to perform actions on the caller's behalf; when omitted, Systems Manager Automation uses the permissions of the user that starts the runbook.

The Windows and Linux branches both invoke the nested Automation document:

`AWSSupport-StartEC2RescueWorkflow`

and pass the same `AutomationAssumeRole` value to the nested workflow through its `RuntimeParameters`.

## Observed execution-relevant inputs

The top-level runbook also passes to the nested workflow:

- `InstanceId` = `{{ UnreachableInstanceId }}`
- `SubnetId` = `{{ SubnetId }}`
- `EC2RescueInstanceType` = `{{ EC2RescueInstanceType }}`
- `CreatePreEC2RescueBackup` = `True`
- `S3BucketName` = `{{ LogDestination }}`
- `S3Prefix` = `AWSSupport-ExecuteEC2Rescue`
- `HelperInstanceProfileName` = `{{ HelperInstanceProfileName }}`
- `HelperInstanceSecurityGroupId` = `{{ HelperInstanceSecurityGroupId }}`
- `AllowEncryptedVolume` = `{{ AllowEncryptedVolume }}`
- `AssociatePublicIpAddress` = `{{ AssociatePublicIpAddress }}`
- `UniqueId` = `{{ automation:EXECUTION_ID }}`

The Windows branch uses an offline PowerShell script and the Linux branch uses an offline shell script. Both branches are marked critical and both invoke the nested workflow.

## Important observed consequence

The current IAM inventory found no separate role whose name contains `EC2Rescue`; only `IT-G1-EC2Rescue-InstanceRole` was returned.

Therefore, no dedicated `AutomationAssumeRole` has been identified from the current account inventory. This does **not** establish that the runbook cannot execute: the document explicitly permits an empty `AutomationAssumeRole`, in which case the permissions of the user starting the Automation are used.

## Interpretation boundary

This artifact establishes the runbook's declared role-assumption mechanism and nested-workflow dependency. It does not establish that the current caller has the permissions required to execute the runbook, nor that the nested workflow can complete successfully.

It also does not establish incident condition, RDP failure, complete prerequisites, helper-resource validity, evidence-freeze completion, `A(t0)`, or execution authorization.

No SSM Automation execution was started.

**Execution status:** `NOT_EXECUTED`
