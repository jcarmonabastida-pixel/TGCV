# IT-METH-I — FAA AMOC Blind Executor-2 Control Harness Audit 001

**Status:** `AUDIT COMPLETE — REPAIR REQUIRED BEFORE DRY-RUN`

**Audited artifact:** `it_meth_i_faa_amoc_blind_executor_2_control_v01.py`  
**Specification:** `IT-METH-I_FAA_AMOC_BLIND_EXECUTOR_2_SPEC_v0.1.md`

## 1. Audit conclusion

The v0.1 harness has the correct high-level safety posture — it defaults to `DRY_RUN_CONTROL`, refuses `EXECUTION`, and does not claim executor independence — but it is **not yet sufficient to produce a defensible technical PASS**.

No reconstruction was executed. The deficiencies are implementation defects in the control harness itself and must be repaired before local dry-run execution.

## 2. Findings

### H1 — Frozen package integrity is optional

**Severity:** HIGH

The specification requires verification of the frozen package integrity. v0.1 permits `--expected-package-sha256` to be omitted and then treats package existence alone as `PACKAGE_INTEGRITY=PASS`.

**Required repair:** expected package hash must be mandatory for a technical PASS.

### H2 — Missing output root is incorrectly treated as a P1 failure

**Severity:** MEDIUM

`scan_tree()` returns `MISSING_ROOT` for a not-yet-created output directory, causing `RECONSTRUCTION_001_ACCESS_STATUS=FAIL`. In dry-run control, the output directory may legitimately not exist yet.

**Required repair:** distinguish `ABSENT_OUTPUT_ROOT` from a forbidden-artifact detection. The output boundary itself must still be validated.

### H3 — Input-boundary test is tautological

**Severity:** HIGH

The current `INPUT_BOUNDARY_STATUS` checks whether the three configured roots are inside a list containing those same roots. This cannot detect undeclared consumed inputs and therefore does not implement P3.

**Required repair:** construct and record an explicit manifest of declared inputs and validate actual files consumed by the dry-run. At minimum, the dry-run must validate package and evidence roots against a declared-root policy and record the manifest.

### H4 — P1 scans names, not content or access paths

**Severity:** HIGH

The forbidden-material scan checks filenames only. A reconstruction-001 artifact with a neutral filename would not be detected.

**Required repair:** for the dry-run, use a conservative boundary model: only explicitly declared package/evidence roots are readable, reject symlinks escaping those roots, and record the complete file manifest. Filename scanning remains a supplementary check, not the primary isolation claim.

### H5 — P6 is capability-only, not seal verification

**Severity:** MEDIUM

`SEAL_CAPABILITY_STATUS` currently means that an output directory exists or its parent exists. This does not demonstrate artifact hashing or immutable sealing.

**Required repair:** dry-run must verify that a temporary control artifact can be hashed and a seal record can be generated without altering reconstruction data. The result must still be labelled technical control only.

### H6 — P7 and P9 are asserted constants

**Severity:** HIGH

`TEMPORAL_ORDERING_STATUS="PASS"` and `COMPARISON_PRESEAL_STATUS="NOT_PRESENT"` are hardcoded values. A constant cannot verify the corresponding property.

**Required repair:** record an explicit pre-seal state and ensure no comparison target is configured or read in dry-run. Temporal ordering should be represented as a control sequence with start timestamp and, where sealing is exercised, seal timestamp.

### H7 — Environment fingerprint omits dependency inventory

**Severity:** LOW/MEDIUM

The specification requests relevant package/runtime information. v0.1 records Python/OS/script hash but no dependency inventory.

**Required repair:** record `sys.version` and a deterministic inventory of installed distributions where available, without requiring network access.

## 3. Safety assessment

The defects do not create evidence contamination in the current unexecuted state, but they make a technical PASS potentially misleading. Therefore execution of the current v0.1 harness is **not accepted** as a governance-quality dry-run.

## 4. Required repair set

The next implementation revision shall:

1. require the frozen package SHA-256;
2. handle absent output roots correctly;
3. replace the tautological input-boundary check with explicit declared-root/file-manifest validation;
4. strengthen the blind boundary with symlink/escape detection;
5. implement an actual dry-run seal artifact/hash operation;
6. replace constant P7/P9 assertions with observable control evidence;
7. extend the environment fingerprint with Python runtime and local dependency inventory;
8. preserve the prohibition on reconstruction 002 execution and independence claims.

## 5. Gate result

`HARNESS_AUDIT = FAIL — REPAIR REQUIRED`

`DRY_RUN_EXECUTION = BLOCKED`

`RECONSTRUCTION_002 = NOT EXECUTED`

`INDEPENDENCE_STATUS = NOT DEMONSTRATED`

`NEXT_GATE = REPAIRED_HARNESS_STATIC_AUDIT`
