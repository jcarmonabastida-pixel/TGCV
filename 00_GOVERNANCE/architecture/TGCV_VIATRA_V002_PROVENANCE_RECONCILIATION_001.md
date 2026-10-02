# TGCV VIATRA V002 Provenance Reconciliation Record

**Status:** CLOSED — canonical provenance discrepancy reconciled; no retroactive evidence rewrite  
**Date:** 2026-10-03  
**Branch:** `viatra-v002-provenance-canonical-closure`

## 1. Purpose

Record and contain the provenance discrepancy identified between the VIATRA Core revision used by the closed PF-09 preflight and the revision associated with the subsequently materialized/audited V002 fixture.

This record is a **documentary provenance reconciliation**. It is not a runtime-equivalence preflight and does not require a build or scientific execution.

## 2. Evidence

| Evidence | VIATRA Core revision | Interpretation |
|---|---|---|
| PF-09 strengthening preflight, run 37074926235 | `6f7d2d7860ed901c33029700387d3535bd2553f1` | Actual executed evidence |
| V002 fixture materialization/audit | `ffa111dbb160c0bc55e89ea16430e97a38908662` | Fixture provenance/reference revision |
| PF-09 workflow | Explicitly pinned to `6f7d2d7860ed901c33029700387d3535bd2553f1` | Confirms execution pin |

The two revisions are distinct commits in `eclipse-viatra/org.eclipse.viatra` and therefore must not be conflated.

## 3. Reconciliation

The PF-09 PASS remains valid **only for the revision actually executed**:

`6f7d2d7860ed901c33029700387d3535bd2553f1`

It is not retroactively upgraded to evidence for:

`ffa111dbb160c0bc55e89ea16430e97a38908662`

Conversely, the fixture materialization record remains provenance evidence for the fixture associated with `ffa111db...`; it does not imply that PF-09 was executed at that revision.

No existing scientific or preflight result is rewritten.

The canonical provenance state is therefore:

- **PF-09 evidence:** PASS at `6f7d2d78...`
- **canonical fixture provenance:** `ffa111db...`
- **equivalence between those two provenance states:** NOT ESTABLISHED by the historical PF-09 run

This distinction is sufficient to close the provenance reconciliation. No build, runtime execution, or scientific execution is required to perform this reconciliation.

## 4. Optional future technical validation

If TGCV later requires an explicit runtime-equivalence claim for the canonical fixture at `ffa111db...`, that is a **separate technical validation task**. It must be specified and authorized independently; it is not a prerequisite for closing this reconciliation record and must not be described as part of the reconciliation itself.

No scientific execution is authorized by this record.

## 5. Decision

**RECONCILIATION CLOSED — provenance discrepancy identified, documented, and contained.**

The historical PF-09 result remains attached to its actual execution revision. The canonical fixture remains attached to its recorded provenance revision. No equivalence is inferred between them.
