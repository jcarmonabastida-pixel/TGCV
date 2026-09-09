# GOV-REPAIR-02 — Atomic Canonical-State Propagation Decision v0.1

**Status:** CLOSED / GOVERNANCE DECISION — REPAIR AUTHORIZED AND APPLIED  
**Date:** 2026-09-09

## 1. Trigger

The governance-current-state workflow failed on run `3903682` with:

`STATUS current RMA disagrees with resolved RMA master`

The failure was caused by sequential propagation commits: the canonical RMA resolution advanced to v2.8 before `STATUS.md` was reconciled to the same resolved master.

The validator correctly rejected the transient inconsistent state.

## 2. Defect classification

This is a **governance propagation atomicity defect**, not a scientific or epistemic defect.

The existing validator is not weakened. The repair removes unnecessary dependence of `STATUS.md` on a versioned RMA filename.

## 3. Repair principle

Stable canonical pointers are the continuity interface. Versioned artifacts are resolved behind those pointers.

`STATUS.md` therefore declares the stable canonical RMA pointer:

`00_GOVERNANCE/rma/TGCV_RMA_current.md`

The validator verifies that STATUS points to this stable canonical location, while the RMA pointer itself resolves dynamically to the CURRENT/OPERATIVE master.

This prevents a version transition from creating a false mismatch merely because a versioned RMA master changes.

## 4. Atomic application

The repair is applied in **one Git commit** containing:

1. the STATUS declaration change;
2. the validator logic change;
3. this governance decision record.

No intermediate `main` state is intentionally created between the dependent changes.

## 5. Invariants preserved

- canonical current-state validation remains strict;
- resolved RMA master must exist and be CURRENT/OPERATIVE;
- RMA, matrix and traceability alignment remains enforced;
- historical versions are not required;
- scientific definitions and epistemic statuses are unchanged;
- no EXT-UPD-4.8 claim is upgraded;
- industrial utility remains UNPROVEN / OPEN.

## 6. Future propagation rule

Future RMA version changes must update the versioned RMA master and the stable current pointer as one canonical-state operation. STATUS must continue to reference the stable current pointer, not a versioned filename.

Where several canonical artifacts genuinely need simultaneous changes, they must be committed atomically rather than through sequential commits that intentionally create an invalid current state.

## 7. Closure criterion

Repair is considered machine-validated only after the GitHub governance-current-state workflow reports `GOVERNANCE_CURRENT_STATE=PASS` on the repair commit.

Until that occurs, this decision is recorded as applied but CI verification remains pending.
