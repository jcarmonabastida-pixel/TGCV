# IT-G1 — AWSSupport-ExecuteEC2Rescue — Explicit Remediation Decision 001

**Status:** `CANONICAL — REMEDIATION DECISION REQUIRED`
**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
**Diagnostic attribution:** `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_DIAGNOSTIC_ATTRIBUTION_001.md`

## 1. Decision trigger

Read-only diagnostics established that the target instance has exactly one associated Security Group, `sg-05c212fdd50abc3fc`, and that Security Group has no inbound permissions. The route table and NACL evidence do not show an equivalent block.

The remaining external TCP/3389 failure is therefore attributable to the current Security Group inbound policy.

## 2. What is and is not authorized at this point

The evidence supports a narrowly scoped remediation candidate: permit TCP/3389 inbound to the target Security Group from the intended operator source.

**No Security Group mutation has been performed by this artifact.**

An explicit authorization is still required before `AuthorizeSecurityGroupIngress` may be executed. AWS documents that this API adds inbound rules and that a TCP rule requires a source and port range. citeturn0search1turn0search8

## 3. Required authorization parameters

Before mutation, the following must be fixed explicitly:

- Security Group: `sg-05c212fdd50abc3fc`
- Protocol: `tcp`
- Port: `3389`
- Source: the operator's actual public IPv4 CIDR, not the private observation address `192.168.1.17`.
- Rule scope: single-source `/32` wherever operationally valid.
- Description: identify the rule as the controlled IT-G1 RDP functional-recovery test.

The public source must be determined from the same observation path immediately before authorization because private address `192.168.1.17` is not the Internet-routable source seen by the EC2 Security Group.

## 4. Decision options

### Option A — AUTHORIZE NARROW REMEDIATION

Authorize exactly one inbound TCP/3389 rule from the operator's current public IPv4 `/32`, then perform read-only verification and one functional TCP/3389 retest.

This option changes only the identified blocker and creates a clean before/after transformation for the case.

### Option B — DO NOT AUTHORIZE REMEDIATION

Keep the Security Group unchanged and close the case with the demonstrated classification:

`INTERNAL_REMEDIATION = PASS`

`EXTERNAL_FUNCTIONAL_RECOVERY = FAIL`

`BLOCKER = SECURITY_GROUP_INBOUND_POLICY`

## 5. Explicit boundary

Until Option A is explicitly selected and a corresponding authorization artifact is recorded:

- do not run `authorize-security-group-ingress`;
- do not alter the Security Group through the console;
- do not change NACLs or routes;
- do not repeat EC2Rescue;
- do not execute the manual comparator.

## 6. Current decision state

`DIAGNOSTIC_ATTRIBUTION = PASS`

`REMEDIATION_CANDIDATE = TCP/3389 FROM OPERATOR_PUBLIC_IP /32`

`REMEDIATION_AUTHORIZATION = PENDING EXPLICIT DECISION`

`INFRASTRUCTURE_MUTATION = NONE`
