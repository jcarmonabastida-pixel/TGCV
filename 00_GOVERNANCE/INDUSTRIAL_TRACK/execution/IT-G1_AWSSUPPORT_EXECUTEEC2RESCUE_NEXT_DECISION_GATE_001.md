# IT-G1 — AWSSupport-ExecuteEC2Rescue — Next Decision Gate 001

**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
**Status:** `CANONICAL — DECISION GATE OPEN`
**Parent execution result:** `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_EXECUTION_RESULT_001.md`
**Execution result commit:** `7a55e62c1a455959484abb11af4c0545c40cb748`

## 1. Decision state

The authorized `AWSSupport-ExecuteEC2Rescue` execution completed successfully, but end-to-end RDP accessibility was not recovered.

Therefore the case must **not** be treated as a successful functional repair and must **not** trigger an automatic retry or a manual-comparator execution.

## 2. Established evidence

- Authorized method executed: `AWSSupport-ExecuteEC2Rescue`
- Parent execution: `d0158f56-82ce-4d2c-99ed-b7e99f16c93f`
- Parent status: `Success`
- Target restored to `running`
- Root volume restored to target `/dev/sda1`
- `TermService`: `Running`
- TCP `3389`: `Listen` on `0.0.0.0` and `::`
- External test from frozen observation source `192.168.1.17`: `TcpTestSucceeded=False`
- Post-execution public IP used for the external test: `18.100.134.191`
- Manual comparator: not authorized and not executed

## 3. Decision boundary

The current evidence establishes an internal state transformation without end-to-end functional recovery.

No further remediation is authorized by this gate.

In particular, this gate does **not** authorize:

- a second `AWSSupport-ExecuteEC2Rescue` execution;
- execution of the frozen manual comparator;
- security-group changes;
- route-table changes;
- NACL changes;
- RDP configuration changes;
- firewall changes beyond those already produced by the authorized runbook;
- stop/start operations outside the authorized workflow;
- modification of the root volume;
- any other infrastructure mutation.

## 4. Required next analytical operation

The next operation is **diagnostic attribution**, not remediation.

The purpose is to determine whether the remaining external failure is attributable to an observable condition outside the transformation already demonstrated by EC2Rescue.

The diagnostic scope should remain read-only and should preserve the current post-execution state.

Priority evidence dimensions:

1. Effective network reachability to TCP/3389 from the same observation point.
2. Security-group ingress applicable to the target ENI.
3. Network ACL applicability to the target subnet.
4. Route-path consistency between the observation source and target.
5. Windows Firewall effective state after EC2Rescue.
6. RDP listener binding and local endpoint state.

No inference of root cause should be recorded until the corresponding evidence is obtained.

## 5. Comparator boundary

The manual comparator remains frozen and unauthorized. Its execution cannot be used as a diagnostic shortcut.

## 6. TGCV-relevant observation

The case currently provides a controlled example in which:

`S_pre -> S_post`

includes a demonstrated transformation of the internal RDP service/listener state, while the externally observed reachable transformation remains absent:

`T_local = achieved`

`T_external = not achieved`

This distinction must remain explicit in subsequent analysis.

## 7. Current disposition

`EXECUTION = CLOSED`

`FUNCTIONAL_RECOVERY = FAIL / NOT DEMONSTRATED`

`REMEDIATION_RETRY = NOT AUTHORIZED`

`MANUAL_COMPARATOR = NOT AUTHORIZED`

`NEXT_OPERATION = READ-ONLY DIAGNOSTIC ATTRIBUTION`
