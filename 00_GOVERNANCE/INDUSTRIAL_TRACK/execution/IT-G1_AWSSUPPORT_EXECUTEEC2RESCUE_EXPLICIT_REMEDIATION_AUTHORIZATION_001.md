# IT-G1 — AWSSupport-ExecuteEC2Rescue — Explicit Remediation Authorization 001

**Status:** `CANONICAL — EXPLICITLY AUTHORIZED`
**Case:** `IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
**Decision:** `OPTION A — NARROW REMEDIATION AUTHORIZED`
**Authorization date:** `2026-09-12`

## Authorized change

Authorize exactly one inbound Security Group rule on the target instance's sole Security Group:

- Security Group: `sg-05c212fdd50abc3fc`
- Protocol: `tcp`
- Port: `3389`
- Source: `113.203.180.202/32`
- Purpose: controlled functional-recovery verification for IT-G1

## Basis

The canonical diagnostic attribution established the Security Group inbound policy as the observed blocker. The instance has TCP/3389 listening after EC2Rescue remediation, while the NACL and route evidence do not explain the external failure.

## Scope boundary

This authorization permits only the single inbound TCP/3389 rule above.

It does not authorize:

- any NACL modification;
- any route-table modification;
- any RDP/Windows configuration change;
- any additional Security Group rule;
- any EC2Rescue rerun;
- stop/start or volume mutation;
- execution of the manual comparator.

## Verification requirement

After the rule is applied, perform the same external TCP/3389 functional test from the same observation point. Record before/after state and outcome. Do not broaden the mutation if the test fails; stop and open a new governed decision.

## State

`REMEDIATION_AUTHORIZATION = AUTHORIZED`

`INFRASTRUCTURE_MUTATION_BEFORE_THIS_ARTIFACT = NONE`

`AUTHORIZED_SOURCE = 113.203.180.202/32`

`AUTHORIZED_PORT = 3389`
