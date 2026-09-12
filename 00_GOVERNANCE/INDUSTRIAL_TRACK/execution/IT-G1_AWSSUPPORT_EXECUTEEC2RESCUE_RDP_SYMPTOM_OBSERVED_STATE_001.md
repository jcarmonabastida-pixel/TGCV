# IT-G1 — AWSSupport-ExecuteEC2Rescue
## CASE-012 — Pre-decision RDP Symptom / Context Observed State 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
**Evidence item:** `CASE-012`
**Status:** `OBSERVED`
**Decision stage:** `PRE-DECISION`
**Execution authorization:** `NONE`

### Observation A — Operator-side TCP reachability

- Observation timestamp: `2026-09-12T05:06:20.2164627+02:00`
- Source: operator workstation
- Source address: `192.168.1.17`
- Target address: `51.48.121.140`
- Target port: `3389`
- Network isolation context: `Internet`
- `TcpTestSucceeded`: `False`
- `PingSucceeded`: `False`

Interpretation boundary: TCP/3389 was not reachable from the operator observation point at the stated timestamp. This does not by itself localize the cause.

### Observation B — Target-side RDP service state

- Observation timestamp: `2026-09-12T05:07:46.6856891+02:00`
- Source: AWS Systems Manager `AWS-RunPowerShellScript`
- Target instance: `i-0b0bf56b94733718c`
- Service: `TermService`
- Status: `Stopped`
- StartType: `Manual`

The explicit listener query produced no listener output for TCP/3389.

Interpretation boundary: the Windows target's `TermService` was stopped at the stated timestamp. No remediation, service start, reboot, network modification, or EC2Rescue execution was performed.

### CASE-012 conclusion

`CASE-012 = OBSERVED`.

The evidence establishes a reproducible pre-decision RDP symptom consisting of failed TCP/3389 connectivity from the operator observation point and `TermService` stopped on the target.

This artifact does not establish root cause, remediation necessity, runbook success, or authorization to execute `AWSSupport-ExecuteEC2Rescue`.

### Provenance

The observations were obtained directly from PowerShell `Test-NetConnection` executed from the operator workstation and AWS Systems Manager `AWS-RunPowerShellScript` executed against the frozen target instance.

### Integrity

SHA-256 shall be recorded after canonical persistence.