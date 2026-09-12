# IT-G1 — AWSSupport-ExecuteEC2Rescue Case Resource Freeze 001

**Status:** `RESOURCE IDENTIFIED — EVIDENCE FREEZE IN PROGRESS`

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
**Decision unit:** one controlled Windows EC2 instance at one frozen pre-decision instant t0
**AWS account:** `502731779370`
**Region:** `eu-south-2`

## Frozen resource identity

- **InstanceId:** `i-0b0bf56b94733718c`
- **AMI:** `ami-0c837ccf2bf0a97c9`
- **Instance type:** `t3.micro`
- **Availability Zone:** `eu-south-2b`
- **Subnet:** `subnet-02b90b9a7f2a2966a`
- **Private IP:** `172.31.24.247`
- **Public IP:** `51.48.121.140`
- **Security Group:** `sg-05c212fdd50abc3fc` (`IT-G1-EC2Rescue-SG`)
- **Instance Profile:** `IT-G1-EC2Rescue-InstanceProfile`
- **Instance Role:** `IT-G1-EC2Rescue-InstanceRole`
- **Observed instance state:** `running`

## Acquisition configuration

The resource was created as a dedicated IT-G1 controlled target. It is not one of the pre-existing IT-METH-I Linux fixture instances.

The dedicated security group has no ingress rules and unrestricted egress at acquisition time. VPC DNS support and DNS hostnames are enabled. The subnet maps public IPv4 addresses on launch and the VPC route table has an active Internet Gateway route.

## Control boundary

This freeze establishes resource identity only. It does **not** establish the IT-G1 empirical incident condition, RDP failure condition, A(t0), case-specific evidence completeness, or authorization to execute `AWSSupport-ExecuteEC2Rescue`.

No EC2Rescue remediation has been executed.

## Next required evidence

Before IT-G1 execution can be authorized, freeze the remaining decision-critical state and provenance, including root volume identity/encryption, SSM managed-node status, automation prerequisites, runbook parameter tuple, and the controlled pre-decision RDP condition. The case must then be evaluated against the canonical accessibility predicate A(t0).
