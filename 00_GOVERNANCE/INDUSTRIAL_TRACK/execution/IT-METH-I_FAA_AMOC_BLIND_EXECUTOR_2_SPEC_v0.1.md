# IT-METH-I — FAA AMOC Blind Executor-2 Technical Specification v0.1

**Status:** `CONTROLLED INFRASTRUCTURE SPECIFICATION — DESIGN / DRY-RUN ONLY`

**Case:** `IT-G1-I-AMOC-US-91-12-10-7K0-18-00734`  
**Method:** `IT-METH-I`  
**Blind package:** `IT-METH-I-AMOC-BLIND-EXEC-001`  
**Reconstruction target:** `IT-METH-I_FAA_AMOC_INDEPENDENT_RECONSTRUCTION_002.md`

## 1. Purpose

Define the technical requirements for a Python-based blind execution environment supporting reconstruction 002.

The implementation is infrastructure only. It does not establish EXECUTOR-2 identity, does not authorize reconstruction 002, and must not be represented as an independent executor when operated by EXECUTOR-1.

## 2. Operating modes

The implementation shall expose two explicit modes:

- `DRY_RUN_CONTROL`: verifies the blind boundary and sealing controls without performing the reconstruction.
- `EXECUTION`: available only after the external governance pre-execution gate has recorded PASS for Gates A–E.

Default mode shall be `DRY_RUN_CONTROL`.

No implicit transition from dry-run to execution is permitted.

## 3. Required inputs

The executor may receive only:

1. frozen blind package;
2. frozen evidence bundle admitted by IT-METH-I;
3. reconstruction worksheet/template;
4. execution environment metadata required for control and sealing.

The implementation must reject or flag any input identified as reconstruction-001 material, comparative output, post-decision outcome material, or evidence outside the frozen boundary.

## 4. Required controls

### P1 — Reconstruction-001 isolation

Before execution, verify that the configured input/output roots contain no reconstruction-001 artifact, score, interpretation, effort record, or comparison file.

A positive detection is a hard block.

### P2 — Frozen package integrity

Verify the expected blind package identifier and recorded integrity reference before execution.

A mismatch is a hard block.

### P3 — Input provenance

Record a manifest of files actually consumed by the environment.

Inputs outside the declared frozen boundary are a hard block.

### P4 — Deterministic control execution

The control phase shall produce a machine-readable result with stable field names and explicit PASS/FAIL/BLOCKED values.

Any scientific reconstruction content is outside the dry-run control result.

### P5 — Separate output boundary

Reconstruction-002 output shall be written to a dedicated path distinct from reconstruction 001 and any comparison output.

### P6 — Seal mechanism

On completion, the environment shall calculate an artifact hash and record a seal timestamp. After sealing, the reconstruction artifact must be treated as immutable for purposes of the IT-METH-I comparison sequence.

### P7 — Temporal ordering

The environment shall record start and seal timestamps and shall not expose reconstruction 001 before the seal event.

### P8 — Environment fingerprint

Record Python version, operating-system identifier, executable/script hash and relevant package/runtime information sufficient to reproduce the control environment.

### P9 — Pre-seal comparison prohibition

No code path may load, compare, score against, or summarize reconstruction 001 before the seal event.

The control implementation must not contain a comparison operation in the pre-seal execution path.

## 5. Hard-fail conditions

The environment shall return `BLOCKED` rather than `PASS` when any of the following occurs:

- reconstruction 001 is accessible;
- frozen package integrity cannot be verified;
- an undeclared input is consumed;
- output path is not separate;
- sealing cannot be performed;
- timestamp evidence is unavailable;
- pre-seal comparison is detected or requested;
- governance authorization for execution is absent;
- the environment is being used to claim executor separation without a distinct executor or separately approved governance basis.

## 6. Machine-readable control result

The control result should contain at least:

```text
PACKAGE_ID
PACKAGE_INTEGRITY
INPUT_BOUNDARY_STATUS
RECONSTRUCTION_001_ACCESS_STATUS
COMPARISON_PRESEAL_STATUS
OUTPUT_BOUNDARY_STATUS
SEAL_CAPABILITY_STATUS
TEMPORAL_ORDERING_STATUS
ENVIRONMENT_FINGERPRINT
EXECUTION_MODE
GOVERNANCE_AUTHORIZATION_STATUS
OVERALL_CONTROL_STATUS
```

`OVERALL_CONTROL_STATUS` may be `PASS` only when every mandatory technical control passes and the external governance authorization condition is satisfied.

## 7. Separation of technical and governance claims

The implementation may establish statements such as:

- `RECONSTRUCTION_001_INACCESSIBLE = PASS`;
- `FROZEN_INPUT_BOUNDARY = PASS`;
- `SEAL_CAPABILITY = PASS`;
- `PRESEAL_COMPARISON = NOT_PRESENT`.

It may not establish from those facts alone:

- `EXECUTOR_2_DISTINCT = PASS`;
- `INDEPENDENCE_STATUS = PASS`;
- `REPRODUCIBILITY = PASS`;
- `UTILITY = PASS`;
- `SUPERIORITY = PASS`.

Those are governance/scientific conclusions outside the Python infrastructure itself.

## 8. Execution authorization interface

Before `EXECUTION` mode is accepted, the environment must require an explicit authorization record corresponding to the IT-METH-I control record.

The authorization must attest that Gates A–E have been independently satisfied.

The script must not self-authorize reconstruction 002 merely because its technical checks pass.

## 9. Seal sequence

The implementation shall enforce the following order:

`LOAD FROZEN INPUTS → VERIFY BOUNDARY → EXECUTE BLIND RECONSTRUCTION → COMPLETE ARTIFACT → HASH → RECORD SEAL TIME → FINALIZE → ONLY THEN RELEASE FOR COMPARISON`

No pre-seal path may access reconstruction 001.

## 10. Dry-run acceptance target

A dry-run shall prove only technical controls. It shall not generate a purported reconstruction 002 and shall not modify reconstruction 001.

Expected dry-run disposition:

`TECHNICAL_CONTROL_STATUS = PASS` only if all implemented checks pass.

This must remain distinct from:

`INDEPENDENCE_STATUS = NOT DEMONSTRATED` until the factual executor condition and the full governance gate are satisfied.

## 11. Relationship to current protocol

This specification implements the technical portion of the controlled blind environment mechanism described by IT-METH-I. The governing protocol remains authoritative for independence. In particular, a same-human second run remains non-independent under the current protocol even if every technical control in this specification passes.

## 12. Explicit non-actions

The implementation must not:

- inspect reconstruction 001;
- modify reconstruction 001;
- compare reconstruction 001 and 002 before seal;
- use later outcomes to reconstruct the decision-time state;
- change IT-G4 thresholds or comparator;
- alter G5 authorization;
- execute another industrial case;
- access Rust/EXT-1.1;
- modify the TGCV Core;
- upgrade any claim.

## 13. Current status

`SPECIFICATION_STATUS = DESIGN_COMPLETE`

`DRY_RUN_STATUS = NOT_EXECUTED`

`EXECUTION_MODE = NOT_AUTHORIZED`

`EXECUTOR_2_STATUS = NOT_ESTABLISHED`

`INDEPENDENCE_STATUS = NOT_DEMONSTRATED`

`RECONSTRUCTION_002 = BLOCKED`

**Conclusion:** the Python blind executor is technically specifiable and can provide auditable isolation/sealing controls. It remains infrastructure; it does not itself create an independent EXECUTOR-2 under the current IT-METH-I governance definition.
