# C10-S V_cont — Gate 169: world identity invariance audit

**Status:** STATIC AUDIT PASS WITH REGRESSION STRENGTHENED; TEST EXECUTION NOT PERFORMED  
**Branch:** `research/c10-s-consolidation-draft`  
**Depends on:** Gates 154, 155, 167 and 168  
**Scientific execution:** NOT AUTHORIZED  
**Code change:** none to Generator; regression test strengthened only

## 1. Purpose and correction to Gate 168

Gate 168 reported that the current Generator world-identity projection retained `assignment_role` and `assignment_index`, and consequently blocked evidence-bundle implementation pending a source correction.

That source finding was incorrect for the branch state inspected in Gate 169. The current source already removes both fields before computing `world_id`. The Gate 168 blocker is therefore withdrawn. Gate 168's bundle and retention contract remains valid; its source-level blocker/status must be read as superseded by this audit.

The cause of the earlier discrepancy is not established from the repository evidence inspected here. No claim is made about when or by whom the correct projection was introduced. This audit reports only the exact current branch content.

## 2. Current source projection

In `03_EXPERIMENTS/C10-S/harness/vcont_integrated_harness.py`, `Generator.generate()` constructs `world_spec = asdict(cfg)` and removes:

- `seed`
- `world_seed`
- `z_assignment_seed`
- `g_assignment_seed`
- `replicate_id`
- `assignment_role`
- `assignment_index`

It then computes:

`world_id = H({world_seed, outer_replicate_id, world_spec})`.

The run identity is computed separately from the complete config, `replicate_id`, `outer_replicate_id`, `assignment_role`, `world_id`, `z_seed` and `g_seed`, then truncated to 24 hexadecimal characters.

Static interpretation:

- Assignment role/index do not enter the world projection.
- Assignment seeds and legacy replicate ID do not enter the world projection.
- World seed and outer M identity do enter the world projection.
- DGP-defining ScenarioConfig fields remain in world_spec.
- Assignment role/index, assignment-specific configuration and streams remain represented in run identity.

This is consistent with Gate 154's fixed-world-within-M / distinct-world-across-M requirement. It is not a cryptographic proof of independent random draws; the seed-bank/manifest provenance contract remains separately required.

## 3. Existing regression and gap

The existing test `test_outer_replicate_identity_propagates_and_separates_worlds` already checked:

- designated RUN and repeated assignment share `world_id`;
- another outer replicate has a different `world_id`;
- outer identity and assignment role propagate.

The original test did not isolate role/index as the only changed fields, explicitly assert distinct run IDs under that change, or isolate a DGP-parameter change from an M/world-seed change.

Gate 169 strengthens that same test with static assertions for:

1. role/index changed while the rest of the run config, including `replicate_id`, is held fixed: same `world_id`, different `run_id`;
2. another M with a different world seed: different `world_id` and `world_seed`;
3. a DGP-defining parameter change at fixed M/world seed: different `world_id`.

The test source has been updated. **It has not been executed.** No PASS, CI result or runtime verification is claimed.

## 4. Disposition

- Generator world-identity projection: STATICALLY CONSISTENT WITH GATE 154.
- Gate 168's claim that role/index remain in world_spec: RETRACTED.
- Gate 168 implementation blocker on world identity: CLOSED AT STATIC-SOURCE LEVEL.
- Regression coverage: STRENGTHENED IN SOURCE; NOT EXECUTED.
- World-seed independence and bank separation: still require Gate 159 manifest/seed reconciliation and trusted provenance.
- RunEvidenceBundle/OuterWorldEvidenceBundle: Gate 168 contract remains DEFINED; implementation remains OPEN.
- Export orchestrator/packager: NOT IMPLEMENTED.
- Scientific execution, calibration, seed-bank generation, Monte Carlo and benchmark: NOT AUTHORIZED / NOT PERFORMED.
- `main`: unchanged; PR #116 remains Draft on its existing base.

## 5. Next operation

Proceed to Gate 170: implement the Gate 168 RunEvidenceBundle capture boundary and deep-immutable snapshots, while preserving the current Generator/Sealer/Analyzer/Evaluator semantics. Before accepting the implementation, execute only the explicitly authorized technical regression suite; do not run calibration, seed-bank generation, Monte Carlo or scientific benchmark operations.
