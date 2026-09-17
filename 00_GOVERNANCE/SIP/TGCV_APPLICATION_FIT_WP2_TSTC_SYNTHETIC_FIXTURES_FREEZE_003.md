# TGCV — WP2 TSTC Synthetic Fixtures Freeze 003

**Status:** FROZEN — SYNTHETIC FIXTURE REVISION; EXECUTION NOT STARTED  
**Date:** 2026-09-17  
**Supersedes for execution purposes:** `TGCV_APPLICATION_FIT_WP2_TSTC_SYNTHETIC_FIXTURES_FREEZE_001.md`  
**Reason for revision:** restore specification-to-engine traceability for the declared C03→C05 composed path.

## 1. Revision boundary

This version preserves all Freeze-001 definitions except for the explicitly versioned addition below. Freeze-001 remains immutable historical specification and is not modified.

The revision adds one C03 transformation required to make the already-declared cross-domain rule

`FX-C03 repo=changed → FX-C05 mobility_requirement_A=urgent`

reachable through a declared C03 state transition.

No execution result is contained here.

## 2. FX-C03 revision

### Candidate transformations

```text
c03.query_db
c03.inspect_repo
c03.open_pr
c03.complete_task
c03.modify_repo
```

### Additional admissibility rule

`modify_repo` iff `repo=clean` AND `permission_repo=granted`.

### Additional transition

```text
repo: clean → changed
```

Only `repo` may be changed by `c03.modify_repo`.

### Interaction with I-C03

Under positive intervention `permission_repo: granted → denied`, `c03.modify_repo` becomes inaccessible, together with `c03.inspect_repo` and `c03.open_pr`; `c03.query_db` remains accessible.

This is a fixture definition, not an execution result.

## 3. Cross-domain composed path

The revised fixture now makes the declared sequence operationally traceable:

```text
Initial
  ↓
FX-C01 security restriction
  ↓
FX-C01 → FX-C03: permission_repo = denied
  ↓
C03 accessibility update
  ↓
[separate admissible C03 state-transition scenario]
  c03.modify_repo: repo clean → changed
  ↓
FX-C03 → FX-C05: mobility_requirement_A = urgent
  ↓
C05 accessibility update
```

The C03→C05 coupling is therefore exercised only in a C03 state in which `c03.modify_repo` is admissible. The C01→C03 propagation scenario and the C03→C05 propagation scenario must be recorded as distinct controlled transition records; the implementation must not claim that `c03.modify_repo` is executable after `permission_repo` has been set to denied.

## 4. Invariants retained

All Freeze-001 invariants remain applicable, including:

- finite transformation universes;
- deterministic admissibility;
- `T_acc ⊆ Uτ`;
- declared-variable-only transitions;
- trajectory transformations drawn only from the current admissible universe;
- explicit cross-domain dependencies;
- negative controls with expected `ΔT_acc = ∅`;
- baseline information parity;
- reproducibility metadata;
- no downstream outcome access.

## 5. Negative controls

C01, C03 and C05 negative controls remain unchanged from Freeze-001.

No negative control may use `c03.modify_repo`.

## 6. Baseline boundary

The C03 baseline must include the same newly declared bounded repository mutation capability so that baseline/TGCV information parity is preserved.

The baseline remains a capability-permission matrix plus finite workflow representation. The cross-domain baseline remains the explicitly declared dependency graph.

## 7. Execution boundary

This document does **not** authorize execution by itself. The following gates remain mandatory:

1. schema/fixture preflight;
2. invariant and negative-control preflight;
3. reproducibility/preflight checks;
4. explicit execution authorization against Freeze-003;
5. only then, a TSTC execution.

No scientific validity, causal validity, superiority, generality, value-creation, ROI, or industrial claim follows from this fixture revision.

## 8. Governance disposition

- Freeze-001: retained unchanged as historical frozen definition.
- Traceability Block 001: remains the historical record of the discrepancy that motivated this revision.
- Freeze-003: new execution candidate specification.
- Existing TSTC execution code: **not yet declared conformant** to Freeze-003 until a dedicated preflight verifies exact fixture/engine identity and hashes.
- TGCV Core/RMA/Evidence→Claim Matrix: unchanged.
