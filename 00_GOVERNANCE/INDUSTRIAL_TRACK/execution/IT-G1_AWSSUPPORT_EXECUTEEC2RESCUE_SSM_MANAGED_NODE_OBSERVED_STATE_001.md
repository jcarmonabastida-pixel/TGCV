# IT-G1 — AWSSupport-ExecuteEC2Rescue — SSM Managed Node Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
**Status:** `OBSERVED EVIDENCE — NOT AN EXECUTION AUTHORIZATION`
**Decision unit:** Frozen controlled Windows EC2 instance at pre-decision instant `t0`

## Observed resource

- Region: `eu-south-2`
- InstanceId: `i-0b0bf56b94733718c`

## Local AWS CLI observation

The following query was executed locally before any `AWSSupport-ExecuteEC2Rescue` remediation:

```powershell
aws ssm describe-instance-information --profile tgcv --region eu-south-2 --filters "Key=InstanceIds,Values=i-0b0bf56b94733718c" --query "InstanceInformationList[].{InstanceId:InstanceId,PingStatus:PingStatus,LastPingDateTime:LastPingDateTime,AgentVersion:AgentVersion,PlatformType:PlatformType,PlatformName:PlatformName,PlatformVersion:PlatformVersion}" --output table
```

Observed result:

| Field | Observed value |
|---|---|
| AgentVersion | `3.3.5226.0` |
| InstanceId | `i-0b0bf56b94733718c` |
| LastPingDateTime | `2026-09-12T03:48:08.100000+02:00` |
| PingStatus | `Online` |
| PlatformName | `Microsoft Windows Server 2025 Datacenter` |
| PlatformType | `Windows` |
| PlatformVersion | `10.0.26100` |

## Interpretation boundary

The observed `PingStatus=Online` establishes that the target was reporting to SSM at the observed instant. It does not, by itself, establish that every prerequisite of `AWSSupport-ExecuteEC2Rescue` is satisfied or that the runbook is authorized for execution.

This artifact does **not** establish:

- the case-specific RDP failure condition;
- complete runbook parameter readiness;
- completeness of the frozen evidence set;
- the accessibility predicate `A(t0)`;
- authorization to execute `AWSSupport-ExecuteEC2Rescue`.

No EC2Rescue remediation was executed as part of this observation.

## Next controlled evidence gate

Continue acquisition of the remaining decision-critical pre-execution evidence, with the runbook's automation prerequisites and parameter tuple next. Execution remains outside the current evidence-acquisition operation.
