# IT-G1 — AWSSupport-ExecuteEC2Rescue — SSM Connectivity Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
**Region:** `eu-south-2`
**Target:** `i-0b0bf56b94733718c`
**Observation status:** `PASS`
**Execution status:** `NOT_EXECUTED` for `AWSSupport-ExecuteEC2Rescue`

## Observation

Connectivity was tested from the controlled Windows target through
`AWS-RunPowerShellScript`.

Command ID:

`96bac387-2878-4d92-b445-c9d9de09108a`

The observation resolved and tested TCP connectivity to:

- `ssm.eu-south-2.amazonaws.com`
  - Resolved IP: `18.101.82.185`
  - DNS resolution: `PASS`
  - TCP/443: `PASS`

- `ssmmessages.eu-south-2.amazonaws.com`
  - Resolved IP: `18.100.75.155`
  - DNS resolution: `PASS`
  - TCP/443: `PASS`

Observed network context:

- Source address: `172.31.24.247`
- Network isolation context: `Internet`
- Interface: `Amazon Elastic Network Adapter`
- Response code: `0`
- SSM command status: `Success`
- Standard error: empty

## Interpretation boundary

This observation establishes effective DNS resolution and TCP/443
connectivity from the controlled target to the regional SSM and
SSM Messages endpoints at the observation time.

It does not establish:

- successful execution of `AWSSupport-ExecuteEC2Rescue`;
- successful creation or management of an EC2Rescue helper instance;
- complete helper-instance connectivity;
- RDP failure;
- incident-state predicate;
- complete runbook eligibility;
- complete effective authorization under all AWS policy mechanisms.

No EC2Rescue remediation was executed.
