# N-R8-C2 vNext — Corpus / Conformance Gate v0.1

**Status:** PASS — SMOKE CONFORMANCE COMPLETED

## Result

The deterministic smoke conformance probe was executed locally after the deterministic witness-search step.

All assertions C1–C9 returned `true` and the overall decision was `PASS`.

- `corpus_generation`: `NOT_PERFORMED`
- `scientific_execution`: `NOT_PERFORMED`
- `N-R7`: `INTACT`
- `states_examined`: `2`
- `key_collision_pairs_examined`: `1`
- `K(A) == K(B)`: `true`
- `O_T(A) != O_T(B)`: `true`

Witness hashes:

- `state_a_sha256 = 0d965256c3aae89093fa954db992843e770b0c358be5392634078b3af0fb6b7c`
- `state_b_sha256 = 0dd6e9d0418beb5c92778cb0e5b3c167b9bc89afc9cbea20c5cbc8ec69870880`

## Scope

This gate validates implementation conformance only. It does not establish global identifiability, does not inspect the Rust dataset, does not train or evaluate models, and does not constitute scientific execution of EXT-1.1.

The frozen key, authoritative operationalisation, target observable, and fail-closed rules remain unchanged.

## Preconditions preserved

- `N-R8-C2_vNEXT_FREEZE_v0.1.md` remains frozen.
- `branch_n_r8c2_vnext_key_v01.py` remains unchanged.
- `branch_n_r8_operationalisation_v01.py` remains unchanged.
- The bounded identifiability result remains an immutable empirical record.
- The deterministic witness is recovered from the same 4-component / 4,096-state fixture family; no target-optimised fixture was introduced.

## Conformance assertions

- **C1 — Frozen-key conformance:** PASS
- **C2 — State canonicalisation:** PASS
- **C3 — Pair equality:** PASS
- **C4 — Target inequality:** PASS
- **C5 — Result-blind construction:** PASS
- **C6 — Determinism:** PASS
- **C7 — Witness compatibility:** PASS
- **C8 — Provenance separation:** PASS
- **C9 — No scientific execution:** PASS

## Corpus boundary

The intended prospective corpus remains **5,000 matched pairs**. It has **not** been generated.

The smoke gate PASS permits progression to the separately controlled corpus-generation preparation stage. It does **not** itself authorize scientific execution.

## Required next step

Prepare and freeze the prospective 5,000-pair corpus-generation configuration and provenance contract before any corpus generation is executed. The configuration must make the sampling space, deterministic seed, pair-bucketing rule, post hoc `O_T` acceptance rule, output schema, canonical hashes, and provenance classification explicit and reproducible.

Any change to the frozen key, target observable, or authoritative transformation semantics invalidates this gate and requires a new versioned audit/freeze.
