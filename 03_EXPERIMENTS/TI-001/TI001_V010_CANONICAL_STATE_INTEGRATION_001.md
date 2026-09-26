# TI-001 V010 Canonical State Integration 001

**Status:** INTEGRATED — DESCRIPTIVE EVIDENCE RETAINED

## Evidence disposition

TI-001 V010 is now a completed and closed experimental record.

Canonical closure:
- `03_EXPERIMENTS/TI-001/TI001_V010_SCIENTIFIC_CLOSURE_001.md`
- Commit: `651aa6e614ff11b9a067626b97d02375e0977e92`

Canonical analysis:
- `03_EXPERIMENTS/TI-001/TI001_V010_SCIENTIFIC_ANALYSIS_RESULT_001.json`
- Blob: `5e4586be82fc8ade6331d0260d9d968468fffade`

## Scientific-state update

TI-001 V010 is retained as descriptive empirical evidence concerning A/B decision behaviour under the specified fixture, decision interface, and runtime.

The evidence does not modify TGCV core definitions, claim statuses, or the open `delta_tacc_to_value` question.

The experiment does not establish a value effect, causal effect, or general model capability.

## Concrete findings retained

1. Both independent executions produced 420/420 valid decisions.
2. The predefined treatment-control indicator differed between executions: E1 `TI_DC=0.0`; E2 `TI_DC=-0.08571428571428563`.
3. The predefined null-control indicator was positive in both executions: E1 `0.042857142857142816`; E2 `0.021428571428571463`.
4. Both executions exhibited a pronounced presentation-stratified difference between `I1_FIRST` and `I2_FIRST`.
5. Executor-level differences are retained rather than pooled or post-hoc reconciled.

## Implication for future research

The presentation-stratified pattern and execution-level variation are concrete observations for subsequent experimental design. They do not themselves determine a causal explanation.

Any follow-up experiment must have its own design, frozen fixture/interface, preflight, authorization, execution, replay, analysis, and closure gates.

## Canonical disposition

**TI-001 V010: RETAINED AS DESCRIPTIVE EMPIRICAL EVIDENCE.**

**TGCV core: UNCHANGED.**

**Claim status: UNCHANGED.**
