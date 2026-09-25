# TI-001 V010 — Primary Execution Audit 001

**Status:** CLOSED — EXECUTION STRUCTURALLY VALID  
**Scope:** Primary audit of the canonical V010 scientific execution result.  
**Scientific interpretation:** NOT PERFORMED in this audit.

## Canonical execution record

- Result: `03_EXPERIMENTS/TI-001/TI001_V010_SCIENTIFIC_EXECUTOR_1_RESULT_001.json`
- Result blob SHA: `5297b578f250a50e90043dab5806877e3c3eec1d`
- Canonicalization commit: `a30112a660ad30fdcad97dc945fdc0031e8821e0`
- Executor: `TI001-V010-SCIENTIFIC-EXECUTOR-1-001`
- Fixture: `TI001-V008-FIXTURE-001`
- Fixture SHA-256: `dd45ae453b5a3d37b4faff34ed829e7aac52ce4ed5a7462bb3546c1a420c2eb9`
- Decision interface: `TI001-V010-DECISION-INTERFACE-001`
- Interface SHA-256: `e025d66e477de3afd79147986b716389d7d7be03d01a21d4380b384e17c8510c`
- Scientific authorization: `TI001-V010-SCIENTIFIC-AUTHORIZATION-001`

## Structural execution findings

The execution record reports:

- scientific execution: `PERFORMED`
- decision units processed: 420
- valid decisions: 420
- invalid decisions: 0
- runtime errors: 0
- missing response IDs: 0
- incomplete statuses: 0
- analysis performed: false

Decision-unit counts reported by condition:

- control: 140
- treatment: 140
- null: 140

Presentation counts:

- I1_FIRST: 210
- I2_FIRST: 210

Output counts:

- control: A=82, B=58
- treatment: A=82, B=58
- null: A=88, B=52

These are decision-unit counts. The frozen fixture specification defines 70 pairs per condition; each pair contains two decision units, so 140 decision units per condition is consistent with the frozen design.

## Audit conclusion

The primary execution audit finds no structural invalidity in the reported V010 execution:

1. The scientific execution was explicitly authorized before execution.
2. The canonical result is present in `main`.
3. The reported execution count is 420.
4. All 420 decision outputs passed the exact A/B validator.
5. No invalid, runtime-error, missing-response, or incomplete execution records are reported.
6. The condition and presentation counts are consistent with the pair-level frozen fixture design.
7. No scientific analysis was performed by the executor.

**Disposition:** PASS — READY FOR REPLAY GATE.

This audit does not calculate, rank, interpret, or draw conclusions from TI indicators. Such analysis remains downstream of replay and final audit gates.

## Parameter note

The raw API response metadata reports an effective `temperature: 1.0`, while the scientific contract/request configuration specifies temperature as omitted/null. This audit treats that as response metadata for an omitted request parameter, not as evidence that a temperature parameter was explicitly supplied by the executor. It must remain documented for replay comparison.

## Next gate

**Replay Gate V010.**
