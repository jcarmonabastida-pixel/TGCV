# TGCV TR-131 — Expanded-State Challenge Package v01

**Status:** CANDIDATE — NOT FROZEN
**Scientific execution:** NOT AUTHORIZED
**Design audit:** PASS
**Date:** 2026-09-20

## Purpose

Evaluate whether the positive TR-131 representation-insufficiency result can be absorbed into a pre-realization expanded state/context representation without merely renaming or copying X and without using post-execution information.

## Frozen inherited evidence

- TR-131 result: `03_EXPERIMENTS/TR-131/execution/TR131_SCIENTIFIC_EXECUTION_RESULT_001.json`
- Result SHA-256: `6925a4064bd6a0fb295c21dc83f8a703fe92adb43dbb5972d5a37bf7ee6d3fb0`
- Result Audit: PASS
- Scientific Disposition: PASS — POSITIVE / REPRESENTATION INSUFFICIENCY
- Frozen package commit: `b0b3cd4e2d4c86f341b9465f9f6188de9f1bfbb0`
- G8 authorization for the original TR-131 execution remains historical evidence only.

## Challenge candidates

### E1 — Expanded state

`S' = G(S,C,X)`

G must be defined before challenge execution from independently specified pre-realization semantics. X may not simply be copied into S' as a new label.

### E2 — Expanded context

`C' = G(C,X)`

The same non-tautology requirement applies.

## Deterministic sufficiency test

For each candidate, define a single rule before execution:

`T_real = F(S',C',T_acc)`

The rule may not receive X or Π as a separate input.

## Non-tautology constraints

The candidate representation must not encode or derive from:

- T_real;
- H;
- final outcome;
- value;
- post-execution classification.

Merely renaming X, T_real, H, or the case outcome fails.

## Counterfactual

At least one pre-realization counterfactual must be evaluated. The counterfactual must alter the admissible realization condition without inserting the observed outcome into S' or C'.

If the only reason the candidate representation differs between conditions is that X was copied into it, the candidate fails the absorption test.

## Outcomes

- **PASS — ABSORBABLE:** a valid expanded representation and single deterministic rule reproduce the admissible realization behavior without separate X/Π.
- **FAIL — NOT ABSORBABLE:** no admissible non-tautological expanded representation satisfies the criteria.
- **INCONCLUSIVE:** a material identification condition cannot be evaluated without post hoc information or changing the construction.

## Governance

This package does not authorize execution and does not modify the frozen TR-131 package, TGCV Core, RMA or Evidence Matrix.

## Required independent audit

Executor-2 must receive only the frozen challenge package and must not receive any challenge outcome or interpretation.

No execution is permitted until package freeze and a new explicit authorization gate are complete.
