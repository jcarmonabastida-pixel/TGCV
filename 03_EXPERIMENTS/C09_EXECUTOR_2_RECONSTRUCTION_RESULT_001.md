# C09 Executor-2 Reconstruction Result 001

**Status:** PASS_RECONSTRUCTION  
**Bundle:** `C09_OPERATIONAL_BUNDLE_003`  
**Executor:** EXECUTOR-2 (independent reconstruction)  
**Scope:** bounded causal identification test `Z → ΔT_acc → Y`, H=1

## 1. Execution result

- `n_control`: 128
- `n_treatment`: 128
- `mean_control`: 5.671875
- `mean_treatment`: 7.3203125
- `tau_hat`: 1.6484375
- `null_tau_hat`: -0.3515625
- `T_acc(control)`: `[A, C]`
- `T_acc(treatment)`: `[A, B, C]`

`null_tau_hat != 0` is **not a failure condition** for Bundle 003. It is retained as a control observation by the frozen specification; no zero-null gate is applied.

## 2. Integrity checks

All 13 Executor-2 integrity checks returned `true`:

- `accessibility`
- `accessibility_differs`
- `balanced_assignment`
- `baseline_definition`
- `bundle_hashes`
- `canonical_row_schema`
- `executor_1_not_used_as_input`
- `null_no_accessibility_change`
- `policy`
- `primary_null_same_units_assignment_baseline`
- `randomization_spec_present`
- `transition`
- `executor_1_not_used_as_input`

## 3. Frozen input provenance

### Bundle 003 SHA-256

- `EXECUTION_SPEC.md`: `D1621DBBCB9DD840828D0F3C431949D7DDA2B73F3E4B43EA86F35FC07A87E10B`
- `execute_c09_bundle_003.py`: `94534CC29FA31E86A9936DE8615D8B0114D44F183942C2126E817E507BF62AC3`
- `fixture.json`: `3E3AC9601F893B7E01F75813499BB3F539D7B192AE18F0332DC6365AAA5EBD49`

### Executor-2

- Source blob: `f58c431a981d92276a9be56b781b3c50ced92192`
- Source SHA-256: `9FAFA38B0AFFC27B395B74A38C099051F9E13C1DA124D04C2905F260AA716B0E`

### Randomization specification

- File: `C09_RANDOMIZATION_SPECIFICATION_001.md`
- Git blob: `68172285a01266baa83e8c2f02a4853093a6be7b`
- SHA-256: `D07E7CA400A5B1902329237DE6CFFD84B0AE1A7FE8FE44F7F80328887E77F74F`

## 4. Runtime

- Python: CPython 3.14.7
- Platform: Windows 11 `10.0.26200-SP0`, AMD64
- External network/dataset/service: none

## 5. Independence and immutability

Executor-2 reconstructed the result from the frozen Bundle 003 inputs and the frozen successor randomization specification. Executor-1's output was not consumed as an input; its frozen source hash was checked only for bundle integrity. Bundle 003 and Executor-2 source remain immutable.

The result is recorded as a new evidence artifact and does not itself modify TGCV Core, RMA, the Evidence Matrix, or any broader theoretical claim.

## 6. Closure disposition

**C09 controlled execution reconstruction: PASS.**  
The execution gate is satisfied for the bounded test. The next governance operation is audit closure / evidence registration, not another reconstruction of Bundle 003.
