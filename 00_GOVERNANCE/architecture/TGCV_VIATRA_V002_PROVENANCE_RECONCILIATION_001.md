# TGCV VIATRA V002 Provenance Reconciliation Record

**Status:** RECONCILED — no retroactive evidence rewrite  
**Date:** 2026-10-03  
**Branch:** `viatra-v002-minimal-fixture-spec`

## 1. Purpose

Record the provenance discrepancy identified between the VIATRA Core revision used by the closed PF-09 preflight and the revision associated with the subsequently materialized/audited V002 fixture.

## 2. Evidence

| Evidence | VIATRA Core revision | Interpretation |
|---|---|---|
| PF-09 strengthening preflight, run 37074926235 | `6f7d2d7860ed901c33029700387d3535bd2553f1` | Actual executed evidence |
| V002 fixture materialization/audit | `ffa111dbb160c0bc55e89ea16430e97a38908662` | Fixture provenance/reference revision |
| PF-09 workflow | Explicitly pinned to `6f7d2d7860ed901c33029700387d3535bd2553f1` | Confirms execution pin |

The two revisions are distinct commits in `eclipse-viatra/org.eclipse.viatra` and therefore must not be conflated.

## 3. Interpretation

The PF-09 PASS remains valid **only for the revision actually executed**:

`6f7d2d7860ed901c33029700387d3535bd2553f1`

It is not retroactively upgraded to evidence for:

`ffa111dbb160c0bc55e89ea16430e97a38908662`

Conversely, the fixture materialization record remains provenance evidence for the fixture associated with `ffa111db...`; it does not imply that PF-09 was executed at that revision.

No existing scientific or preflight result is rewritten.

## 4. Canonical next validation target

If the materialized fixture is to be validated as the canonical V002 fixture, the next dedicated preflight must pin:

- VIATRA Core: `ffa111dbb160c0bc55e89ea16430e97a38908662`
- the already recorded VIATRA Examples revision for V002;
- the frozen TGCV fixture bytes;
- the relevant TGCV source revision.

The preflight must independently establish build, runtime closure, fixture loading, semantic equivalence, and contamination/firewall status.

## 5. Governance consequence

Until that preflight passes, the following distinction remains mandatory:

- **PF-09 evidence:** PASS at `6f7d2d78...`
- **canonical fixture provenance:** `ffa111db...`
- **equivalence between those two provenance states:** NOT YET ESTABLISHED

No scientific execution is authorized by this record.

## 6. Decision

**RECONCILIATION PASS — provenance discrepancy documented and contained.**

The next gate is a **fresh V002 runtime-equivalence preflight at the canonical fixture revision**, not a reinterpretation or rerun of historical PF-09 evidence.
