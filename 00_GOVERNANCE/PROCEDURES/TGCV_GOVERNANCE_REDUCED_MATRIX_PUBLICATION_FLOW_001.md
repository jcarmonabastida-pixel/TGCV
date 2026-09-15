# TGCV — Reduced Governance Flow for Future Matrix Publications

**Status:** OPERATIVE PROCEDURE
**Purpose:** establish the reduced, single-pass workflow to be used for the next and subsequent Evidence-to-Claim Matrix publications.

## 1. Governing principle

`EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md` is a **stable alias of the complete versioned current matrix**. It is never an independently authored or simplified derivative.

For every publication, `CURRENT.md` must be an exact copy of the versioned matrix being promoted.

## 2. Single-pass publication flow

### Step 1 — Prepare the new version

Create the next versioned matrix (`vX.Y`) from the complete previous current matrix and apply only the intended cumulative update.

Requirements:
- preserve all prior material evidence;
- preserve the established schema and claim boundaries;
- add the new evidence/qualification explicitly;
- do not independently edit `CURRENT.md`.

### Step 2 — Derive CURRENT directly

Generate `EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md` as an **exact copy** of `EVIDENCE_TO_CLAIM_MATRIX_vX.Y.md`.

The source of truth for both files is therefore the versioned artifact; `CURRENT.md` is only its stable alias.

### Step 3 — Prepare the complete governance transition

Update, in the same prepared transition:
- `CANONICAL_STATE.json` to the new matrix version;
- `EVIDENCE_TO_CLAIM_MATRIX_CURRENT_POINTER.md` to the same version;
- any other canonical pointer that the existing state architecture requires.

No intermediate state is published intentionally.

### Step 4 — Run the existing recurring gate once

Run **only** the existing `00_GOVERNANCE/tools/validate_current_state.py` as the recurring governance gate.

It must verify at minimum:
- canonical state is `CURRENT`;
- canonical matrix version, pointer and manifest agree;
- `CURRENT.md` is exactly identical to the resolved versioned matrix;
- cumulative evidence and required matrix structure are preserved;
- all other canonical-state invariants pass.

### Step 5 — Publish only on PASS

If the gate returns `GOVERNANCE_CURRENT_STATE=PASS`, publish/merge the prepared transition.

If it returns `FAIL`, **do not repair the repository iteratively**. Diagnose the failed invariant, correct the prepared transition, and rerun the same gate.

## 3. Explicitly excluded from the recurring flow

The following are not part of the recurring publication cycle:
- automatic repair scripts;
- dynamic "highest version" discovery;
- independent synchronization of `CURRENT.md`;
- multiple competing validators;
- repeated mutation-and-retry loops;
- automatic commits or auto-repair after validation failure.

The broader canonical-state reconciliation mechanism remains available **on demand** (for example, at a chat/context change), but it is not a substitute for the recurring publication gate.

## 4. Operational invariant

The desired end state of every matrix publication is:

`versioned matrix vX.Y` = `CURRENT.md` = `pointer target` = `CANONICAL_STATE matrix version`

with the existing validator confirming the complete chain in one pass.

## 5. Next-use rule

For the next matrix publication, start directly at **Step 1**. Do not recreate migration, repair, synchronization, or parallel validation tooling unless a separately identified scientific or governance requirement makes such a component necessary.
