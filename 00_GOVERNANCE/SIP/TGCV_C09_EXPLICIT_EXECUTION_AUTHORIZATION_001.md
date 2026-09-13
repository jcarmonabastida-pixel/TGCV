# TGCV — C09 Explicit Execution Authorization 001

**Status:** `EXECUTION AUTHORIZED — CONTROLLED / H=1 / FINITE DOMAIN`
**Date:** 2026-09-13
**Claim:** C09 — Accessibility changes causally affect subsequent trajectories

## 1. Authorization decision

The C09 controlled execution protocol and its audit are complete.

`PROTOCOL AUDIT = PASS`
`EXECUTION AUTHORIZATION = GRANTED`

Authorization is limited strictly to the frozen protocol, package, domain and execution boundaries specified below.

## 2. Frozen authorization basis

Protocol:
`TGCV_C09_CONTROLLED_EXECUTION_PROTOCOL_001.md`

Protocol blob SHA at authorization:
`935ea4cb626d9dbbf1f48c8f078f2f6f4c6155f2`

Audit:
`TGCV_C09_CONTROLLED_EXECUTION_PROTOCOL_AUDIT_001.md`

Audit commit:
`765828c3388fd01b0d3d00306acddd79bb589df6`

Domain-selection audit:
`TGCV_C09_CONTROLLED_DOMAIN_CANDIDATE_SELECTION_AUDIT_001.md`

## 3. Authorized scientific scope

Finite synthetic domain only:

`U={A,B,C}`

`T_acc,0={A,C}`
`T_acc,1={A,B,C}`

Intervention:

`Z=1` enables `R1`; `Z=0` leaves `R1` disabled.

Trajectory horizon:

`H=1`

Primary endpoint:

frozen one-step trajectory endpoint `Y`.

Primary causal contrast:

`τ = E[Y(1)-Y(0)]`

## 4. Operational authorization conditions

Execution may proceed only if the executor first verifies:

1. the exact protocol blob SHA above;
2. the frozen domain/pre-execution package and its hashes;
3. a clean execution environment;
4. declared executor identity/role;
5. declared Executor-2 independence condition;
6. declared seed/randomization range before outcome observation;
7. canonical output schema and destination;
8. hash-verification procedure;
9. adjudication rule for any Executor-1/Executor-2 disagreement;
10. absence of any scientific outcome at the time of authorization.

If any precondition fails, execution is `BLOCKED` and no substitute protocol may be used.

## 5. Executor separation

Executor-1 performs the authorized controlled execution.

Executor-2 remains independent and outcome-blind until its own reconstruction is complete.

Executor-2 must not receive:

- Executor-1 outputs;
- observed treatment/control endpoint values;
- post-execution interpretation;
- modified protocol files;
- coaching about expected results.

## 6. Integrity boundary

The following remain invariant:

- `S0,C0,U`;
- accessibility logic except for the declared `R1` intervention;
- transformation definitions;
- transition function `G`;
- decision policy `P(S,C,T_acc)`;
- objective/scoring;
- execution engine;
- observation procedure;
- trajectory metric;
- randomization procedure after assignment.

Any unauthorized dependency of `Z` outside accessibility is a protocol violation and invalidates causal interpretation.

## 7. Stop conditions

Execution must stop immediately if:

- protocol/package hash mismatch occurs;
- an undeclared input affects execution;
- accessibility is derived using post-treatment information;
- `Z` directly reaches trajectory-generation components outside `T_acc`;
- `T_acc,0=T_acc,1` under the declared intervention;
- randomization is not reproducible;
- endpoint or metric is altered after observation;
- independent reconstruction cannot be performed under the declared firewall.

Stopped execution does not constitute C09 evidence.

## 8. Evidence and claim firewall

This authorization does not authorize:

- value analysis;
- industrial utility analysis;
- predictive-superiority claims;
- cross-domain generalization;
- modification of TGCV Core;
- RMA or Evidence→Claim Matrix upgrade;
- reinterpretation of SWIM/FOS/RUST-DYN-2 evidence;
- acquisition of external datasets;
- AWS mutation or external-system intervention.

## 9. Required execution sequence

`Executor-1 preflight → controlled execution → seal results → independent Executor-2 reconstruction → blind comparison → adjudication → C09 result classification`

No result may be interpreted before the independent reconstruction stage is complete.

## 10. Authorization record

`AUTHORIZATION_ID = TGCV-C09-EXEC-AUTH-001`
`AUTHORIZATION_STATE = GRANTED`
`SCIENTIFIC_EXECUTION = PERMITTED`
`HORIZON = H=1`
`DOMAIN = FINITE_RESOURCE_GATED_TRANSFORMATION_MICRODOMAIN`
`OUTCOME_AVAILABLE_AT_AUTHORIZATION = NO`

This record authorizes execution of the frozen C09 protocol only. It does not assert that C09 has passed, failed, or been established.
