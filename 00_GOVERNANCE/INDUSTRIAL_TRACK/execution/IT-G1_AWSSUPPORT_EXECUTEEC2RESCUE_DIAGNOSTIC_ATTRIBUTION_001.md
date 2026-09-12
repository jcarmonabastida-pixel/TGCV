# IT-G1 — AWSSupport-ExecuteEC2Rescue — Diagnostic Attribution 001

**Status:** `CANONICAL — READ-ONLY DIAGNOSTIC ATTRIBUTION CLOSED`
**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
**Parent gate:** `IT-G1_AWSSUPPORT_EXECUTEEC2RESCUE_NEXT_DECISION_GATE_001.md`

## 1. Evidence reviewed

### Security Group

The target instance `i-0b0bf56b94733718c` has exactly one associated Security Group:

`sg-05c212fdd50abc3fc`

The Security Group has:

`IpPermissions = []`

and therefore no inbound rule permitting TCP/3389.

AWS documentation states that a Security Group with no inbound rules permits no inbound traffic. citeturn0search0

### Route path

The subnet has no explicit route-table association returned by the subnet filter, so the VPC main route table was inspected.

Main route table:

`rtb-02d751c62c36e7b06`

It contains an active default route:

`0.0.0.0/0 -> igw-00129c3186099eb4c`

Therefore the observed route configuration is consistent with Internet egress/ingress pathing at the VPC route-table layer.

### Network ACL

Subnet `subnet-02b90b9a7f2a2966a` is associated with:

`acl-06e3ed4a71b0f5d48`

The ACL has an inbound rule 100 allowing all IPv4 traffic from `0.0.0.0/0` and an outbound rule 100 allowing all IPv4 traffic to `0.0.0.0/0`.

The numbered rules therefore do not explain the observed TCP/3389 failure. AWS documents that NACL rules are evaluated in ascending rule order and the first matching rule applies. citeturn0search2

### Windows internal state

Previously established post-execution evidence remains:

- `TermService = Running`
- TCP/3389 listening on `0.0.0.0` and `::`
- external TCP/3389 test from source `192.168.1.17` to public IP `18.100.134.191` failed.

The authorized EC2Rescue output also recorded Windows Firewall profiles being disabled during remediation.

## 2. Attribution result

The diagnostic evidence establishes a **specific external access blocker at the Security Group layer**:

`sg-05c212fdd50abc3fc` has no inbound permissions, while the instance has no other associated Security Group.

Consequently, the case has demonstrated:

`INTERNAL_RDP_STATE = RECOVERED`

`VPC_ROUTE_PATH = CONSISTENT`

`NACL = NOT BLOCKING BY OBSERVED RULES`

`SECURITY_GROUP_INBOUND_3389 = BLOCKED / NOT PERMITTED`

`EXTERNAL_RDP = NOT REACHABLE`

This is sufficient to attribute the observed external TCP/3389 failure to the current Security Group configuration, without making any infrastructure change.

## 3. Command error disposition

The final SSM diagnostic command was not executed because PowerShell/AWS CLI quoting produced invalid JSON. This does not invalidate the attribution because the decisive Security Group, route-table and NACL evidence was obtained independently, and the Windows listener/service state was already established by prior successful read-only SSM checks.

## 4. Governance boundary

No remediation was performed.

No Security Group rule was added.

No route, NACL, Windows Firewall, RDP, instance, or volume state was modified.

The manual comparator remains unauthorized.

A remediation decision must be made explicitly before any Security Group mutation.

## 5. Current classification

`DIAGNOSTIC_ATTRIBUTION = PASS`

`PRIMARY_OBSERVED_BLOCKER = SECURITY_GROUP_INBOUND_POLICY`

`FUNCTIONAL_RDP_RECOVERY = FAIL — BLOCKER ATTRIBUTED`

`REMEDIATION = NOT YET AUTHORIZED`

`MANUAL_COMPARATOR = NOT AUTHORIZED`

`NEXT GOVERNED DECISION = EXPLICIT REMEDIATION DECISION`
