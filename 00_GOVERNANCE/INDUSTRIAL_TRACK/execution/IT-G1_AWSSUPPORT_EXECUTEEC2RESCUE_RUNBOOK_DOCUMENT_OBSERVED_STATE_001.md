# IT-G1 — AWSSupport-ExecuteEC2Rescue Runbook Document Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

**Decision unit:** One controlled Windows EC2 instance at frozen pre-decision instant `t0`.

**Observation purpose:** Record the observed AWS Systems Manager Automation document state for `AWSSupport-ExecuteEC2Rescue` without executing the automation document.

## Observed state

- Document name: `AWSSupport-ExecuteEC2Rescue`
- Document type: `Automation`
- Document version: `1`
- Status: `Active`
- Platform types: `Windows`, `Linux`

## Acquisition command

```powershell
aws ssm describe-document --profile tgcv --region eu-south-2 --name AWSSupport-ExecuteEC2Rescue --query "{Name:Document.Name,Status:Document.Status,DocumentVersion:Document.DocumentVersion,PlatformTypes:Document.PlatformTypes,DocumentType:Document.DocumentType}" --output table
```

## Interpretation boundary

This observation establishes that the named SSM Automation document was observed as `Active`, version `1`, and declared support for Windows and Linux at the acquisition time.

This observation does **not** establish:

- that all prerequisites for execution are satisfied;
- that the controlled Windows instance meets every automation prerequisite;
- that an RDP failure exists or existed at `t0`;
- that the evidence-freeze gate is complete;
- that the canonical accessibility predicate `A(t0)` is satisfied;
- that execution of `AWSSupport-ExecuteEC2Rescue` is authorized;
- or that the automation document has been executed.

**Execution status:** `NOT_EXECUTED`
