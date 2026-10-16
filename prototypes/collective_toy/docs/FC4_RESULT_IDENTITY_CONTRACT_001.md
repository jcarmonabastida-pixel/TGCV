# Collective Toy result identity contract — FC-4

Status: proposed contract for implementation; not yet an implementation or acceptance result.

## Scope

This contract separates three claims that must never be conflated:

1. **Input provenance** — SHA-256 of the exact canonical input JSON. It changes when a declaration list is reordered.
2. **Artifact integrity** — SHA-256 of the exact serialized result payload under its declared package/engine schema. It detects edits to that payload and is not expected to be invariant under semantic normalization.
3. **Semantic identity** — SHA-256 of a versioned canonical semantic projection. It is expected to remain invariant only under explicitly admitted semantics-preserving permutations.

The package-level hash remains an independent integrity check. None of these hashes alone proves that the engine's scientific claims are valid.

## Compatibility rules

- Do not silently change the meaning of the existing `result_sha256` field in already-published package fixtures.
- Historical package fixtures must be assessed using their declared package/engine contract. Do not rewrite their bytes or hashes to make a current engine pass.
- If semantic identity is introduced, add a separately named field (proposed: `semantic_sha256`) and an explicit semantic-canonicalization version (proposed: `semantic_identity_version`). The final field names and version must be agreed by Python and browser implementations in the same change.
- Keep exact input hash and package integrity hash independent from semantic identity.
- Python and browser must use identical canonicalization rules and fixtures. A pass in one runtime is not evidence for the other.

## Canonical semantic projection — proposed

The projection must be constructed from validated model/result semantics, not by sorting arbitrary JSON recursively.

Potentially invariant list dimensions, subject to profile-specific review:
- state declarations: sort by state ID;
- transition declarations: sort by transition ID;
- scenario declarations: sort by scenario ID;
- relation declarations: sort by their full validated semantic tuple, preserving multiplicity;
- disabled-transition declarations: sort by transition ID when order is not semantically meaningful.

Preserve order where it represents behavior:
- executed transformation sequences and their step order;
- temporal prerequisites and event histories;
- trajectories;
- any ordered intervention sequence whose order is part of the profile contract.

Do not sort every array indiscriminately. Do not discard relation metadata or source provenance from integrity artifacts. Semantic projection may omit provenance hashes only when those hashes are separately integrity-checked and the omission is specified by this versioned contract.

## Required acceptance tests

1. Exact-input hash changes after reordering input declaration arrays.
2. Semantic identity remains stable for each explicitly admitted semantics-preserving permutation.
3. Semantic identity changes for a mutation that changes reachability, enabled transformations, trajectory order, or temporal applicability.
4. Artifact integrity fails after editing any protected result field, including `delta_reach`.
5. Package integrity remains independent of semantic identity.
6. Current package export can be replayed independently by Python.
7. Browser export/import and replay produce the same fields and hashes as Python.
8. The historical baseline fixture remains byte-identical and is assessed according to its declared historical contract; no fixture hash is regenerated as a workaround.
9. Legacy packages without semantic identity remain readable under an explicit compatibility path, without claiming a semantic hash that they do not contain.
10. Invalid or unsupported semantic-identity versions are rejected or marked inspect-only; they must not be silently treated as current.

## Implementation gate

Implement only after the existing historical fixture and browser/Python expectations are mapped to the versioned package contract. Run the synthetic Python suite and browser/cross-runtime suite on the same branch head. Do not merge to `main` until both pass and the run SHA matches the reviewed commit.

## Non-goals

- No changes to the structural graph detector or OCR.
- No scientific execution or performance optimization.
- No change to TGCV Core or scientific claims.
