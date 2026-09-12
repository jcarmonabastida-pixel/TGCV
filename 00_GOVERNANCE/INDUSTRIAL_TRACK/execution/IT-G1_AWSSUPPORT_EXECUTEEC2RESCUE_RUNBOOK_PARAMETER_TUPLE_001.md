# IT-G1 — AWSSupport-ExecuteEC2Rescue Runbook Parameter Tuple 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

**Document:** `AWSSupport-ExecuteEC2Rescue`

**Document version:** `1`

**Document status observed:** `Active`

**Observation purpose:** Freeze the observed parameter inventory of the SSM Automation document without invoking the automation.

## Observed parameter inventory

| Name | Type | Default value |
|---|---|---|
| `UnreachableInstanceId` | `AWS::EC2::Instance::Id` | none; required |
| `LogDestination` | `AWS::S3::Bucket::Name` | empty string |
| `EC2RescueInstanceType` | `String` | `t3.medium` |
| `SubnetId` | `String` | `CreateNewVPC` |
| `AutomationAssumeRole` | `AWS::IAM::Role::Arn` | none shown |
| `HelperInstanceProfileName` | `String` | none shown |
| `HelperInstanceSecurityGroupId` | `String` | none shown |
| `AllowEncryptedVolume` | `String` | `False` |
| `AssociatePublicIpAddress` | `String` | `True` |

## Previously observed parameter semantics

The document description for `UnreachableInstanceId` states that the Automation stops the target instance. It further warns that RAM and instance-store data are lost on stop, and that an automatically assigned public IPv4 address is released if an Elastic IP is not being used.

The document description for `SubnetId` states that a custom subnet must be in the same Availability Zone as `UnreachableInstanceId` and must allow access to SSM endpoints. The default is `CreateNewVPC`.

## Controlled-case mapping status

The frozen target instance is:

`i-0b0bf56b94733718c`

The target is in Availability Zone:

`eu-south-2b`

No execution parameter values are being supplied or authorized by this artifact. This artifact records the document's observed interface only. In particular, it does **not** establish values for `AutomationAssumeRole`, `HelperInstanceProfileName`, `HelperInstanceSecurityGroupId`, `LogDestination`, `SubnetId`, or the conditional execution parameters.

## Interpretation boundary

This observation does **not** establish:

- that the automation prerequisites are satisfied;
- that a helper instance can be created;
- that the required IAM role/profile/security-group configuration is valid;
- that the target is actually unreachable by RDP;
- that `A(t0)` is satisfied;
- that the evidence-freeze gate is complete;
- or that execution is authorized.

**Execution status:** `NOT_EXECUTED`
