# TGCV VSL Executor-2 Independent Reconstruction A — Audit 001

## Status

**RECONSTRUCTION OUTPUT CONSISTENT — AUXILIARY EVIDENCE; NOT FROZEN-BUNDLE EXECUTION**

Date: 2026-09-19

## Boundary

This reconstruction was executed with an independent script outside the frozen executable bundle after the initial Executor-2 bundle execution attempt failed with a syntax error.

The reconstruction was not represented as execution of the frozen bundle.

## Results

- N = 100
- fixtures = 100
- control T_acc size = 7 for all fixtures
- treatment T_acc size = 8 for all fixtures
- delta_t_acc = +1 for all fixtures
- control trajectory = e01 -> e13 -> e35
- treatment trajectory = e01 -> e13 -> e35
- control O = 17
- treatment O = 17
- control V* = -17
- treatment V* = -17
- delta_V* = 0 for all fixtures
- dataset SHA-256 = 6b51f7f46e75c76bfbb9e0428f8828d0b2641805c545f8cd7436a59b2cfdea58

## Reconciliation

The dataset hash is identical to the persisted Executor-1 A result:

`A_EXECUTION_RESULT_002.json`

This establishes byte-level agreement of the canonical dataset representation used by the A result hash, subject to the distinction that this reconstruction was performed outside the frozen bundle execution boundary.

The independent script reproduces the current A bundle constants and deterministic BFS rule.

## Limitations

This artifact does not by itself establish formal Executor-2 protocol completion because the A executable package remains a freeze/authorization-controlled object and the independent reconstruction was not executed from the frozen bundle itself.

No TGCV Core, RMA, Evidence-to-Claim Matrix, C09, VSL-SPEC-01 or VSL-EXP-01 claim is upgraded by this artifact.

## Files

- `A_EXECUTOR_2_RECONSTRUCTION_001.py`
- `A_EXECUTOR_2_RECONSTRUCTION_001.json`
