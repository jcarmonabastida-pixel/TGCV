# TR-131 VisitAll Dynamic Transformation Space — Scientific Execution Authorization Gate

**Status:** GATE DEFINITION — SCIENTIFIC EXECUTION NOT AUTHORIZED

## Purpose

Establish an explicit, auditable boundary between package freeze/preflight and scientific execution.

## Required conditions

Scientific execution may proceed only when all are true:

1. The VisitAll Dynamic Transformation Space package freeze/integrity audit is PASS.
2. The exact runner, adapter, source lock, and Executor-2 reconstruction are unchanged from the audited package, or the package has been explicitly reopened and re-frozen.
3. The runner has an explicit authorization mechanism. Default execution must not constitute scientific execution.
4. The execution output is persisted locally as an exact machine-readable artifact and hashed.
5. Executor-2 reconstruction is run independently and its output is persisted separately.
6. No Rainbow/SWIM runtime, RUST experiment, goal achievement, optimization, value evaluation, or outcome-dependent selection enters the experiment.
7. The authorization act is explicit and attributable to the experiment operator; it is not inferred from the presence of the package or from a preflight PASS.

## Current blocker

The frozen Executor-1 runner currently reports `scientific_execution_authorized = false` while performing the exhaustive computation and reporting `scientific_execution_performed = true`.

This field combination is not an acceptable scientific execution state. It must be corrected before authorization.

## Required correction

Reopen the package governance state, modify the Executor-1 runner so that:

- default invocation does not perform scientific execution;
- explicit authorization is required;
- the authorization state is recorded consistently;
- unauthorized invocation exits without producing a scientific-run result;
- authorized invocation records `scientific_execution_authorized = true` and `scientific_execution_performed = true`.

Executor-2 must remain an independent reconstruction and must not consume Executor-1 output.

After the correction, the runner conformance preflight and package freeze/integrity audit must be rerun. Only a new PASS freeze may authorize the scientific run.

## Scientific boundary

The experiment remains VisitAll-only, exhaustive depth 2, with C1 excluded as not testable under deterministic source semantics and C2/C3/C4 enumerated. This gate introduces no new scientific construct and does not alter the experimental question.

**Scientific execution: NOT AUTHORIZED.**
