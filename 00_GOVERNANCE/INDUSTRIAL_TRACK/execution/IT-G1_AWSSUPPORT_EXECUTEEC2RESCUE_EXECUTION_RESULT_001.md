# IT-G1 — AWSSupport-ExecuteEC2Rescue — Execution Result 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
**Candidate:** `AWSSupport-ExecuteEC2Rescue`
**Status:** `CLOSED — EXECUTION RESULT RECORDED — FUNCTIONAL RECOVERY NOT DEMONSTRATED`
**Execution authorization:** `CANONICAL — EXPLICITLY AUTHORIZED`

## 1. Execution identity

- Parent AutomationExecutionId: `d0158f56-82ce-4d2c-99ed-b7e99f16c93f`
- Nested workflow AutomationExecutionId: `237dae19-a215-49bc-bf08-5b411bf88086`
- Nested document: `AWSSupport-StartEC2RescueWorkflow`
- Nested document version: `11`
- Target instance: `i-0b0bf56b94733718c`
- Region: `eu-south-2`
- Target AZ: `eu-south-2b`
- Root volume: `vol-003ff62dff6e449a4`
- Authorized method: `AWSSupport-ExecuteEC2Rescue`
- Helper instance type: `t3.small`

## 2. Execution terminal result

Parent execution:

- Status: `Success`
- Start: `2026-09-12T06:53:39.230000+02:00`
- End: `2026-09-12T07:09:13.416000+02:00`
- Wall-clock elapsed: `15m 34.186s`
- Failure: `null`

Nested workflow:

- Status: `Success`
- Start: `2026-09-12T06:53:40.310000+02:00`
- End: `2026-09-12T07:09:11.505000+02:00`
- Failure: none reported

## 3. Authorized execution path actually completed

The successful workflow included the following observed operations:

1. Target prechecks passed.
2. Temporary EC2Rescue helper infrastructure was created.
3. Helper instance became SSM managed/online.
4. Target root volume `vol-003ff62dff6e449a4` was detached from the target.
5. Pre-script backup AMI was created: `ami-07bdbf42c34abb269`.
6. EC2Rescue was installed/executed on the helper.
7. Offline Windows analysis/remediation completed with command response code `0`.
8. Root volume was detached from the helper and reattached to the target as `/dev/sda1`.
9. Target instance was restored to `running`.
10. Temporary CloudFormation/helper infrastructure reached terminal cleanup state.

## 4. EC2Rescue transformation evidence

Offline Windows EC2Rescue output reported:

- Windows Server 2025 Datacenter detected.
- Remote Desktop Connections: `Enabled`.
- TCP Port: `3389`.
- Windows Firewall: enabled on Domain, Private and Public profiles before remediation.
- Changes: Windows Firewall disabled on Domain, Private and Public profiles.
- Volume successfully set offline.

No evidence in the EC2Rescue output alone establishes external RDP reachability.

## 5. Post-execution infrastructure verification

Read-only verification after completion established:

- Instance state: `running`
- Instance ID: `i-0b0bf56b94733718c`
- AZ: `eu-south-2b`
- Root device: `/dev/sda1`
- Root volume: `vol-003ff62dff6e449a4`
- Volume state: `in-use`
- Attached to: `i-0b0bf56b94733718c`
- DeleteOnTermination: `true`
- Post-execution public IP: `18.100.134.191`

## 6. Post-execution Windows verification

SSM read-only command `9f0af747-03cb-4551-809b-fc640dee270b` established:

- `TermService`: `Running`
- Command response code: `0`
- Command status: `Success`

SSM read-only command `063075d4-7032-48bf-9452-b202b2df298b` established:

- `0.0.0.0:3389`: `Listen`
- `[::]:3389`: `Listen`
- Command response code: `0`
- Command status: `Success`
- Standard error: empty

Therefore the execution demonstrably transformed the local Windows RDP service condition from the frozen pre-execution state (`TermService=Stopped`, no TCP/3389 listener) to (`TermService=Running`, TCP/3389 listeners present).

## 7. Functional external verification

The same external observation point used for the pre-execution symptom test was used after execution:

- Source: `192.168.1.17`
- Target post-execution public IP: `18.100.134.191`
- Target port: `3389`
- `TcpTestSucceeded`: `False`
- `PingSucceeded`: `False`
- Result: `TCP CONNECTIVITY NOT RECOVERED`

This is the controlling functional result for the case's RDP accessibility criterion.

## 8. Final outcome classification

### Execution-level outcome

`EXECUTION_STATUS = SUCCESS`

The authorized `AWSSupport-ExecuteEC2Rescue` automation completed successfully and restored the target instance/root-volume configuration.

### Internal remediation outcome

`INTERNAL_RDP_STATE_TRANSFORMED = TRUE`

Evidence:

`TermService: Stopped -> Running`

`TCP/3389: no listener -> Listen on 0.0.0.0 and ::`

### Functional recovery outcome

`FUNCTIONAL_RDP_RECOVERY = NOT DEMONSTRATED / FAIL`

Reason:

`192.168.1.17 -> 18.100.134.191:3389` remained unsuccessful after the intervention.

### Overall case conclusion

`AWSSupport-ExecuteEC2Rescue = EXECUTION SUCCESS / INTERNAL REMEDIATION PASS / END-TO-END FUNCTIONAL RECOVERY FAIL`

The result must not be interpreted as evidence that the runbook failed to execute. It executed successfully. Rather, the evidence shows that the intervention changed the internal Windows RDP state without restoring external TCP reachability from the frozen observation point.

## 9. Comparator boundary

The manual comparator remains:

`NOT AUTHORIZED — NOT EXECUTED`

No manual remediation, firewall adjustment, RDP configuration change, security-group change, route change, stop/start action, or other comparator intervention was performed after the EC2Rescue result.

## 10. Effort measurement

The effort convention defines operator active effort separately from wall-clock automation time.

- Wall-clock execution interval: `15m 34.186s`
- Active operator effort: `NOT RECONSTRUCTED`
- Automation/passive waiting: not counted as active effort
- Intervention count for the authorized execution: `1`

No active-effort duration is inferred from wall-clock time.

## 11. Provenance / evidence boundary

This result records only evidence available from the authorized execution and its immediate read-only post-execution verification.

It does not incorporate the unauthorized manual comparator, later remediation attempts, or later post-decision evidence.

The result is therefore suitable as the canonical execution outcome for the first authorized `AWSSupport-ExecuteEC2Rescue` execution in this case.

## 12. Canonical conclusion

`IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`

`AUTHORIZATION = PASS`

`EXECUTION = PASS`

`INFRASTRUCTURE_RESTORATION = PASS`

`INTERNAL_RDP_REMEDIATION = PASS`

`EXTERNAL_RDP_FUNCTIONAL_RECOVERY = FAIL`

`MANUAL_COMPARATOR = NOT EXECUTED`

`CASE = OPEN FOR NEXT GOVERNED DECISION`
