# GOV-REPAIR-01 — Version-Independent Current-State Validation

**Status:** FROZEN / INFRASTRUCTURE REPAIR DESIGN
**Scope:** Governance continuity infrastructure only

## Problem

The previous current-state validator encoded historical versions and operation identifiers directly in executable validation logic. This makes the continuity gate brittle when the canonical RMA or Evidence→Claim Matrix advances.

## Repair principle

The validator must validate **identity and alignment of canonical current-state pointers**, not historical version filenames or operation numbers.

Versions, dates, and operation identifiers remain properties of the resolved canonical artifacts.

## Canonical manifest

`00_GOVERNANCE/CANONICAL_STATE.json` is the stable machine-readable registry of canonical pointer locations.

Stable keys are paths/roles, not versions:

- current RMA pointer
- current Evidence→Claim Matrix
- current matrix pointer
- current traceability pointer
- STATUS
- CHANGELOG
- scientific registry
- validator itself

## Required invariants

1. Canonical manifest exists and is valid JSON.
2. Every declared canonical pointer resolves to the expected file/directory.
3. Exactly one current RMA pointer exists.
4. The RMA pointer resolves to a file declaring `CURRENT / OPERATIVE` and a concrete current master.
5. The declared RMA master exists and is marked current/operative.
6. The current matrix exists and declares a current version.
7. The matrix pointer resolves to the same canonical matrix and agrees with its declared current version.
8. RMA and matrix references are mutually aligned.
9. Traceability is resolved dynamically from the current RMA version; historical traceability versions are not hardcoded.
10. STATUS resolves and declares the same current RMA and matrix.
11. No historical version is required merely because it was current previously.
12. Duplicate canonical current pointers are failures; historical artifacts are not failures solely for existing.

## Dynamic resolution rules

- Extract current RMA master from the RMA pointer content.
- Extract current matrix path/version from the matrix pointer and/or matrix content.
- Resolve traceability by matching the current RMA version to `TGCV_RMA_traceability_<version>.csv`.
- Do not encode `v2.6`, `v0.6`, `EXT-UPD-4.6`, `EXT-UPD-4.7`, or `EXT-UPD-4.8` as mandatory validator constants.
- Do not require a particular historical control chain to remain current.

## Failure semantics

- Missing canonical artifact: FAIL.
- Invalid manifest: FAIL.
- Zero current target: FAIL.
- More than one canonical current target: FAIL.
- Pointer resolves but declarations disagree: FAIL.
- Historical artifacts present without current designation: PASS.

## Non-goals

This repair does not alter TGCV science, evidence, epistemic status, external assets, experiments, or research decisions. It is a governance continuity repair only.

## Verification

After implementation, the repository Actions workflow must execute the refactored validator on `main`. A successful run establishes only **governance current-state consistency**, not scientific validation.
