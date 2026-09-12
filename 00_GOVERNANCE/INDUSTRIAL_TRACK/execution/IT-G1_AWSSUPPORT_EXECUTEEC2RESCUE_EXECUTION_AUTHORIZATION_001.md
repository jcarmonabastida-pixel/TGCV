# IT-G1 — AWSSupport-ExecuteEC2Rescue — Explicit Execution Authorization 001

**Status:** `CANONICAL — EXPLICITLY AUTHORIZED`

## Authorization

- `CASE_ID=IT-G1-AWSSUPPORT-EXECUTEEC2RESCUE`
- `AUTHORIZED_METHOD=AWSSupport-ExecuteEC2Rescue`
- `TARGET_ID=i-0b0bf56b94733718c`
- `REGION=eu-south-2`
- `AUTHORIZATION_DECISION=AUTHORIZED`
- `AUTHORIZATION_SOURCE=EXPLICIT USER AUTHORIZATION IN CURRENT GOVERNANCE FLOW`
- `AUTHORIZATION_TIMESTAMP=2026-09-12` 
- `CONFIRMATION_EXECUTION_BEFORE_AUTHORIZATION=FALSE`

## Preconditions

The authorization is issued only after the canonical execution authorization gate established:

- frozen evidence completeness/integrity: `PASS`
- `A(t0)=TRUE`
- manual comparator: `FROZEN — NOT EXECUTED`
- effort convention: `FROZEN`
- R001: `SEALED — PASS`
- R002: `SEALED — PASS`
- independent reconstruction concordance: `PASS`
- final integrity/provenance closure: `CLOSED — PASS`
- AWS execution before this authorization: `FALSE`

## Scope and stopping boundary

This authorization covers only the execution of `AWSSupport-ExecuteEC2Rescue` for the identified target instance `i-0b0bf56b94733718c` in `eu-south-2`, using the frozen pre-execution case definition and governance package.

Execution must remain within the authorized AWS Support automation/runbook scope. No unrelated infrastructure change, target expansion, comparator execution, or change to the frozen evidence package is authorized by this record.

If the authorized execution cannot proceed within the frozen case scope, or requires an out-of-scope mutation or decision, execution must stop and the condition must be recorded rather than inferred as authorized.

## Governance state transition

Before this record:

`EXECUTION_AUTHORIZATION=NONE`

After this record:

`EXECUTION_AUTHORIZATION=AWSSupport-ExecuteEC2Rescue`

This record authorizes the method; it does **not** assert that execution has occurred or that the execution will succeed.

## Explicit exclusions

- `MANUAL_COMPARATOR_AUTHORIZED=FALSE`
- `COMPARATOR_EXECUTED=FALSE`
- `AWS_EXECUTION_PERFORMED=FALSE` at authorization-record creation time
- no post-decision evidence is admitted into the pre-execution reconstruction
- no authorization is granted for a different target, region, case, or method

## Next controlled state

The case is now eligible for the authorized execution step. The execution result must be recorded separately from this authorization record, including terminal outcome, effort measurements under the frozen convention, and any resulting evidence/provenance required by the IT-G1 governance chain.
