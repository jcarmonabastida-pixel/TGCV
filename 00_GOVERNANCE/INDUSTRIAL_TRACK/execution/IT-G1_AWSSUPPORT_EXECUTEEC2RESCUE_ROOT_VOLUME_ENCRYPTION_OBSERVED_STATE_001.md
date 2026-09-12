# IT-G1 — AWSSupport-ExecuteEC2Rescue — Root Volume Encryption Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
**Status:** `OBSERVED EVIDENCE — NOT AN EXECUTION AUTHORIZATION`
**Decision unit:** Frozen controlled Windows EC2 instance at pre-decision instant `t0`

## Observed resource

- Region: `eu-south-2`
- InstanceId: `i-0b0bf56b94733718c`
- Root device: `/dev/sda1`
- VolumeId: `vol-003ff62dff6e449a4`

## Local AWS CLI observation

The following query was executed locally before any `AWSSupport-ExecuteEC2Rescue` remediation:

```powershell
aws ec2 describe-volumes --profile tgcv --region eu-south-2 --volume-ids vol-003ff62dff6e449a4 --query "Volumes[0].{VolumeId:VolumeId,Encrypted:Encrypted,KmsKeyId:KmsKeyId,State:State,Size:Size,VolumeType:VolumeType,AvailabilityZone:AvailabilityZone}" --output table
```

Observed result:

| Field | Observed value |
|---|---|
| AvailabilityZone | `eu-south-2b` |
| Encrypted | `False` |
| KmsKeyId | `None` |
| Size | `30` GiB |
| State | `in-use` |
| VolumeId | `vol-003ff62dff6e449a4` |
| VolumeType | `gp3` |

## Interpretation boundary

This artifact records an observed infrastructure state only.

It does **not** establish:

- SSM managed-node status;
- automation prerequisites for `AWSSupport-ExecuteEC2Rescue`;
- the case-specific RDP failure condition;
- completeness of the frozen evidence set;
- the accessibility predicate `A(t0)`;
- authorization to execute `AWSSupport-ExecuteEC2Rescue`.

No EC2Rescue remediation was executed as part of this observation.

## Next controlled evidence gate

Continue acquisition of the remaining decision-critical pre-execution evidence, with SSM managed-node status as the next state-dependent item. Execution of the runbook remains outside the current evidence-acquisition operation.
