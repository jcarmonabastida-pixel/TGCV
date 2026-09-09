# TR-132-MOD-1 — AUTHORIZATION RECORD v0.1

**Fixture:** `MOD1-FX-001`
**Package:** `TR132-MOD1-PKG-001`
**Status:** `EXECUTION AUTHORIZED`
**Authorization commit:** `eeb26dce18a6e0a7524446138468ed7c829830e0`
**Authorization date:** 2026-09-09

## Decision

Scientific execution of TR-132-MOD-1 is explicitly authorized for the exact frozen package identified above.

## Preconditions verified

- Current-state governance CI: PASS on authorization commit `eeb26dce18a6e0a7524446138468ed7c829830e0`.
- Package integrity review: PASS.
- Immutable package input manifest present and frozen.
- Evidence/provenance manifest present and frozen.
- Executable protocol: `TR-132_EXECUTABLE_PROTOCOL_v0.1`, CURRENT / OPERATIVE / DESIGN-ONLY prior to this authorization.
- Fixture and controls frozen before execution.
- No scientific claim, Core definition, or C01-C16 wording has been changed by this authorization.

## Authorized scope

Execution is limited exclusively to `MOD1-FX-001` using the immutable package inputs recorded in `PACKAGE_INPUT_MANIFEST_v0.1.md`.

This authorization does not authorize processing of the Rust dataset, any industrial experiment or industrial case, O3, Stage-C or Stage-D activity, causal inference, value inference, or validation of the TGCV Core beyond the declared methodological test.

## Execution integrity boundary

Execution must use the exact immutable package. Any post-freeze mutation, substitution, omission, or deviation from the frozen protocol or package invalidates this authorization and requires a new authorization review.

Realization of a transformation must not be used to establish its accessibility. Execution results must be recorded separately from the pre-execution fixture classifications and must follow the frozen result schema and stop rules.

## Result and stop-rule requirements

The execution result must be recorded using `TR-132-MOD-1_EXECUTION_RESULT_AND_STOP_RULES_v0.2`.

The pre-declared methodological target remains bounded L3 temporal identifiability: under the invariant candidate universe, identity rule, accessibility predicate, and evidence rules, the certified bounded accessible sets at `t0` and `t1` must exhibit a non-empty symmetric difference.

Failure to satisfy the minimum conforming level, or any violation of the frozen non-circularity or reproducibility conditions, requires the applicable frozen FAIL/INCONCLUSIVE stop rule.

## Authorization boundary

This record authorizes execution only. It does not pre-judge the execution result and does not constitute evidence of PASS for TR-132 itself.

**EXECUTION AUTHORIZED**
