# IT-G1 — AWSSupport-ExecuteEC2Rescue Root Volume Observed State 001

**Status:** `OBSERVED EVIDENCE — NOT EXECUTION AUTHORIZATION`

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
**InstanceId:** `i-0b0bf56b94733718c`
**Region:** `eu-south-2`

## Observation

Observed locally with AWS CLI before any EC2Rescue remediation execution:

```text
aws ec2 describe-instances --profile tgcv --region eu-south-2 --instance-ids i-0b0bf56b94733718c --query "Reservations[0].Instances[0].BlockDeviceMappings[].{Device:DeviceName,VolumeId:Ebs.VolumeId,DeleteOnTermination:Ebs.DeleteOnTermination}" --output table
```

Observed result:

| Device | VolumeId | DeleteOnTermination |
|---|---|---|
| `/dev/sda1` | `vol-003ff62dff6e449a4` | `True` |

## Interpretation boundary

This record establishes only the observed block-device mapping and termination configuration at the time of observation. It does not establish root-volume encryption state, SSM managed-node status, automation prerequisites, RDP failure, A(t0), evidence completeness, or authorization to execute `AWSSupport-ExecuteEC2Rescue`.

No EC2Rescue remediation was executed as part of this observation.

## Provenance

The controlled resource identity is frozen canonically in `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_CASE_RESOURCE_FREEZE_001.md`.

This observation is empirical evidence for the pending decision-critical root-volume state and must not be treated as a replacement for the complete evidence-freeze gate.
