# IT-G1 — AWSSupport-ExecuteEC2Rescue — Case Closure 001

**Status:** `CANONICAL — CASE CLOSED`
**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
**Closure date:** `2026-09-12`

## Final decision chain

1. Pre-decision accessibility: `A(t0)=TRUE`.
2. Independent reconstructions R001/R002: `PASS` and concordant.
3. Integrity/provenance closure: `PASS`.
4. Execution authorization: explicitly authorized for `AWSSupport-ExecuteEC2Rescue`.
5. EC2Rescue execution: `SUCCESS`.
6. Internal remediation: `PASS` — Windows RDP service/configuration and listener state restored.
7. Initial end-to-end functional recovery: `FAIL`.
8. Read-only diagnostic attribution: `PASS` — observed blocker attributed to Security Group inbound policy.
9. Explicit remediation decision: Option A.
10. Narrow remediation authorization: TCP/3389 from `113.203.180.202/32` only.
11. Security Group mutation: `SUCCESS`, rule `sgr-0fbb978cecdef01e9`.
12. Same-observation-point functional verification: `PASS` — `TcpTestSucceeded=True` to `18.100.134.191:3389`.

## Final outcome

`IT-G1 = CLOSED — FUNCTIONAL RECOVERY DEMONSTRATED`

The governed intervention sequence established that EC2Rescue successfully repaired the internal Windows/RDP state, while end-to-end recovery additionally required the separately authorized Security Group ingress rule. After that narrow rule was applied, TCP/3389 connectivity was demonstrated from the same external observation point.

## Scope compliance

No ungoverned NACL, route, Windows, volume, EC2Rescue rerun, or manual-comparator mutation was performed during the remediation phase.

`GOVERNANCE_SCOPE_COMPLIANT = TRUE`
`FUNCTIONAL_RECOVERY = PASS`
`CASE_CLOSURE = PASS`

## Canonical evidence

- Explicit remediation authorization commit: `695ca568129c7a1afd956f1dfe466151e21c2f66`
- Functional remediation verification commit: `8ecc386e8d2d07d65a6625d6ce8d1236cd3b5a6b`
