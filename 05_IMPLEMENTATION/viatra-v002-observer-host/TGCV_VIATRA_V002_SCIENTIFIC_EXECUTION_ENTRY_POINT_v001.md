# TGCV VIATRA V002 — Scientific Execution Entry Point v001

**status:** DRAFT_PENDING_PREFLIGHT  
**scientific_execution_authorized:** false

## Purpose

This document defines the exact technical entry point that a future authorized scientific execution shall invoke for the frozen VIATRA V002 package.

It does not authorize execution, fitting, inference, interpretation, or publication of scientific results.

## Canonical implementation

The entry point is bound to the canonical V002 implementation commit:

`8bef1d02c23b58dc5d5165b8aff51b264d4fd52f`

The implementation entry point is:

`org.tgcv.viatra.v002.observer.V002SerialExecutor.execute()`

The entry point SHALL be invoked through the already validated V002 observer-host runtime test/invocation boundary. No alternate executor, reflective invocation, historical private rule object, or regenerated transformation source is permitted.

## Input package

The execution SHALL use only:

1. canonical implementation commit `8bef1d02c23b58dc5d5165b8aff51b264d4fd52f`;
2. frozen fixture `TGCV_VIATRA_MINIMAL_FIXTURE_v002`;
3. frozen fixture SHA-256 manifest revision `83019cb86e41a3277dbd59b651c1bd5d2c810561`;
4. the exact runtime/toolchain package validated by the technical preflight.

The fixture bytes SHALL be verified before invocation.

## Execution mode

The scientific execution entry point is a single isolated serial invocation of:

`V002SerialExecutor.execute()`

The invocation SHALL:

- operate on one frozen V002 fixture instance;
- execute serially;
- preserve the six-rule historical order;
- emit the canonical observer lifecycle;
- produce the deterministic observation artifacts already defined by the V002 observer contract.

No batching, pooling, parallel execution, random scheduling, parameter search, fitting, inference, reward calculation, utility calculation, or value calculation is part of this entry point.

## Scientific boundary

This entry point is an execution primitive, not a scientific estimator.

It SHALL NOT compute or infer:

- `T_acc`;
- `Delta T_acc`;
- reachability;
- trajectories;
- utility;
- reward;
- value;
- scientific effect sizes;
- inferential statistics.

Any scientific analysis using the resulting technical observations SHALL be a separate, explicitly specified stage and is outside this entry point.

## Required execution parameters

The entry point itself has no tunable scientific parameters.

The execution package SHALL nevertheless record:

- implementation commit;
- workflow revision;
- fixture manifest revision;
- execution ref;
- runtime/toolchain identity;
- workflow run ID;
- executor identity;
- seed policy.

Because the canonical V002 serial execution is deterministic and contains no stochastic sampling, the seed policy for this entry point SHALL be recorded as:

`seed_policy = NOT_APPLICABLE_DETERMINISTIC_SERIAL_EXECUTION`

## Expected technical outputs

A successful invocation SHALL preserve the canonical V002 observation outputs, including:

- transformation identity;
- activation instance identity;
- deterministic event sequence;
- pre-state digest;
- post-state digest;
- fixture provenance;
- implementation/instrumentation provenance;
- resulting Deployment/Traceability state required by the V002 runtime contract.

The scientific execution package SHALL persist raw outputs and cryptographic hashes of persisted artifacts.

## Fail-closed requirements

Before invocation, the execution workflow SHALL fail if any of the following is true:

1. canonical implementation commit is absent or not the required ancestor;
2. fixture identity or any frozen fixture SHA-256 differs;
3. execution contract is absent or modified incompatibly;
4. scientific authorization is not explicitly granted by the separate authorization record;
5. runtime/toolchain package does not match the validated package;
6. scientific firewall detects prohibited authorization/execution markers;
7. the expected entry point cannot be resolved exactly.

## Separation from authorization

Definition of this entry point does not grant authorization.

The authorization gate remains the sole decision boundary for scientific execution.

The workflow SHALL continue to report:

`scientific_execution_authorized = false`

until a separate explicit authorization record changes that state.

## Preflight acceptance

This entry point may be considered preflighted only after an isolated workflow demonstrates, without scientific execution:

1. exact resolution of `V002SerialExecutor.execute()`;
2. exact implementation and fixture identity;
3. deterministic environment capture;
4. expected output manifest;
5. fail-closed behavior;
6. scientific firewall coverage;
7. preservation of the authorization boundary.

## Non-decisions

This entry point does not establish:

- scientific validity;
- causal validity;
- TGCV effect;
- value construction;
- estimator validity;
- statistical power;
- scientific acceptance.

Those questions remain outside this technical entry-point contract.

## Authorization boundary

**This document does not authorize scientific execution.**
