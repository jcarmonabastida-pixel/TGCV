# N-R8-C2 vNext — Bounded Identifiability Result v0.1

**Status:** IMMUTABLE RESULT RECORD

## Result

The bounded identifiability probe for the frozen N-R8-C2 vNext key completed successfully.

```json
{
  "corpus_generation": "NOT_PERFORMED",
  "decision": "IDENTIFIABLE",
  "fixture_family": "fixed_4_component_all_directed_edge_subsets",
  "key_collision_pairs_examined": 1194,
  "n_r7": "INTACT",
  "scientific_execution": "NOT_PERFORMED",
  "states_examined": 4096,
  "status": "PASS",
  "witness": {
    "state_a_sha256": "0d965256c3aae89093fa954db992843e770b0c358be5392634078b3af0fb6b7c",
    "state_b_sha256": "0dd6e9d0418beb5c92778cb0e5b3c167b9bc89afc9cbea20c5cbc8ec69870880"
  }
}
```

## Interpretation

The frozen key

`K_C2_vNext = B + degree-multiset(V)`

has, within the bounded fixture family, at least one equal-key pair whose transformation-organisation observable `O_T` differs. Therefore N-R8-C2 vNext is **IDENTIFIABLE for the bounded fixture family**.

This is the required positive witness for the identifiability gate. It does **not** by itself establish global identifiability across all possible Branch N states, nor does it constitute scientific execution of EXT-1.1.

## Scope preserved

- Corpus generation: **NOT PERFORMED**.
- 5,000-pair corpus: **NOT PERFORMED**.
- Scientific execution: **NOT PERFORMED**.
- N-R7: **INTACT**.
- Fixture family: all `2^12 = 4096` directed edge subsets over the fixed 4-component fixture, with the frozen resources/objective.
- Collision pairs examined: 1,194.

## Witness traceability

The two witness states are identified by SHA-256 hashes only in this result record. The corresponding state reconstruction and O_T comparison remain attributable to the probe implementation:

`03_EXPERIMENTS/EMP-1.1/src/probe_n_r8c2_vnext_identifiability_v01.py`

The frozen key is implemented in:

`03_EXPERIMENTS/EMP-1.1/src/branch_n_r8c2_vnext_key_v01.py`

## Gate decision

**IDENTIFIABILITY GATE: PASS**

The next step is therefore not to modify the key or broaden the bounded search. The appropriate next step is to preserve this result, verify/record the witness traceability, and prepare the subsequent bounded corpus/conformance gate according to the existing EMP-1.1 execution contract. No scientific run should be started from this result alone.
