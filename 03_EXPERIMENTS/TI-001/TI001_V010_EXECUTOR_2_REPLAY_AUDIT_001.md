# TI-001 V010 — Executor-2 Replay Audit 001

**Status:** CONDITIONAL — GOVERNANCE DEVIATION REQUIRES RECONCILIATION BEFORE SCIENTIFIC ANALYSIS

## Scope

Audit of the canonical Executor-2 replay result after scientific execution. This audit does not modify, recode, replace, or reinterpret the replay result.

## Canonical replay result

- Result: `03_EXPERIMENTS/TI-001/TI001_V010_EXECUTOR_2_REPLAY_RESULT_001.json`
- Canonicalization commit: `5c04d47b`
- Result blob SHA: `82b09712d1fa866dc25927c62ada1c7da1004665`
- Executor ID: `TI001-V010-EXECUTOR-2-REPLAY-001`
- Scientific execution: `PERFORMED`
- Decision units: 420
- Analysis performed: false

## Execution integrity

Observed canonical result summary:

- VALID: 420
- INVALID: 0
- RUNTIME_ERROR: 0
- missing response IDs: 0
- incomplete responses: 0
- control decision units: 140
- treatment decision units: 140
- null decision units: 140
- I1_FIRST: 210
- I2_FIRST: 210
- outputs: A=285, B=135

**Disposition:** PASS for execution/result structural integrity.

## Binding verification

Executor-2 source currently canonical on `main`:

- Path: `03_EXPERIMENTS/TI-001/TI001_V010_EXECUTOR_2_REPLAY_001.py`
- Blob SHA: `e8699d725b3c19df6572e229ca91ade9df811daa`
- Executor ID: `TI001-V010-EXECUTOR-2-REPLAY-001`
- Fixture ID/SHA bound in source: `TI001-V008-FIXTURE-001` / `dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9`
- Interface ID/SHA bound in source: `TI001-V010-DECISION-INTERFACE-001` / `e025d66e477de3afd79147986b716389d7d7be03d01a21d4380b384e17c8510c`
- Runtime bound in source: gpt-5.6-luna, Responses API, top_p 0.98, max_output_tokens 64, reasoning none, tools empty, no retry/recode.

The canonical authorization binds the same executor ID, fixture/interface IDs and SHAs, and runtime parameters.

## Independence verification

The canonical Executor-2 source:

- does not import Executor-1;
- does not reference the Executor-1 result;
- independently builds the visible model input;
- independently validates exact A/B outputs;
- does not consume Executor-1 outputs;
- performs no scientific analysis during replay.

**Disposition:** PASS for implementation independence.

## Governance deviation

The Executor-2 implementation was corrected after the original Executor-2 identity preflight and after the replay authorization artifact had been created. The canonical authorization binds the Executor-2 **ID**, but does not bind an Executor-2 source SHA.

Therefore:

1. the original identity-preflight result does not certify the corrected source;
2. the scientific replay nevertheless executed with the authorized executor ID and the authorized fixture/interface/runtime bindings;
3. the canonical replay result must be preserved unchanged;
4. this is a governance/traceability deviation, not a reason to alter or discard the scientific result;
5. no scientific interpretation should be performed until the deviation is formally reconciled.

## Replay comparison boundary

The difference between Executor-1 and Executor-2 output counts is not treated as an execution failure. The runtime contract does not establish deterministic response identity across independent model calls. Replay comparison must therefore distinguish:

- structural reproducibility: population, bindings, validity and execution integrity;
- stochastic response variation: observed A/B differences;
- scientific interpretation: deferred until governance reconciliation is closed.

## Gate disposition

**CONDITIONAL — EXECUTOR-2 REPLAY RESULT IS CANONICAL AND STRUCTURALLY VALID, BUT SCIENTIFIC ANALYSIS IS BLOCKED PENDING FORMAL RECONCILIATION OF THE POST-AUTHORIZATION EXECUTOR-SOURCE CHANGE.**

No replay result is modified or recoded.
