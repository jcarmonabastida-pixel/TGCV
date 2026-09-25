# TI-001 V010 — Replay Comparison Gate 001

**Status:** PASS — READY FOR FORMAL REPLAY COMPARISON

## Purpose

Establish the comparison boundary between the canonical Executor-1 primary execution and the canonical Executor-2 independent replay.

This gate does not alter either result and does not yet interpret the Transformational Intelligence indicator.

## Canonical executions

### Executor-1

- Result: `03_EXPERIMENTS/TI-001/TI001_V010_SCIENTIFIC_EXECUTOR_1_RESULT_001.json`
- Result blob SHA: `5297b578f250a50e90043dab5806877e3c3eec1d`
- Scientific execution: `PERFORMED`
- Decision units: 420
- Valid: 420
- Invalid: 0
- Runtime errors: 0
- Analysis performed: false
- Condition counts at decision-unit level: control 140, treatment 140, null 140
- Presentation counts: I1_FIRST 210, I2_FIRST 210

### Executor-2

- Result: `03_EXPERIMENTS/TI-001/TI001_V010_EXECUTOR_2_REPLAY_RESULT_001.json`
- Result blob SHA: `82b09712d1fa866dc25927c62ada1c7da1004665`
- Scientific execution: `PERFORMED`
- Decision units: 420
- Valid: 420
- Invalid: 0
- Runtime errors: 0
- Analysis performed: false
- Condition counts at decision-unit level: control 140, treatment 140, null 140
- Presentation counts: I1_FIRST 210, I2_FIRST 210

## Shared scientific bindings

Both executions are bound to:

- fixture: `TI001-V008-FIXTURE-001`
- fixture SHA-256: `dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9`
- interface: `TI001-V010-DECISION-INTERFACE-001`
- interface SHA-256: `e025d66e477de3afd79147986b716389d7d7be03d01a21d4380b384e17c8510c`
- model: `gpt-5.6-luna`
- API surface: Responses API
- top_p: 0.98
- max_output_tokens: 64
- reasoning: effort none
- tools: empty
- retry: none
- recode: none
- analysis during execution: none

## Comparison invariants

The following are required structural invariants and are satisfied by both canonical execution records:

1. same frozen decision-unit population: 420;
2. same condition allocation: 140/140/140 decision units;
3. same presentation allocation: 210/210;
4. same fixture identity and SHA;
5. same decision-interface identity and SHA;
6. same runtime contract;
7. exact A/B validity rule;
8. no missing response IDs;
9. no incomplete responses;
10. no execution-time scientific analysis.

**Structural reproducibility disposition: PASS.**

## Observed response distributions

Executor-1:

- control: A=82, B=58
- treatment: A=82, B=58
- null: A=88, B=52
- total: A=252, B=168

Executor-2:

- control: A=98, B=42
- treatment: A=86, B=54
- null: A=101, B=39
- total: A=285, B=135

The distributions are not identical.

This difference is recorded as an observed cross-execution response difference. It is not classified as an execution defect because the frozen runtime contract did not specify deterministic response identity or a reproducibility criterion requiring bit-for-bit agreement across independent model calls.

## Scientific interpretation boundary

The observed A/B differences must not be converted into a scientific conclusion at this gate.

In particular, this gate does not:

- select Executor-1 or Executor-2 as authoritative for scientific interpretation;
- average, pool, or otherwise combine the two executions;
- discard either execution;
- calculate a final TI effect;
- infer causality;
- infer value effects;
- rank conditions;
- treat response variation as evidence for or against TGCV.

A dedicated scientific analysis specification/gate is required for any indicator calculation and interpretation.

## Gate disposition

**PASS — STRUCTURAL REPLAY COMPARISON COMPLETE.**

Both executions are retained as independent canonical records. The observed response-distribution differences are preserved as part of the empirical record.

**Next gate:** formal scientific analysis specification and pre-analysis authorization.
