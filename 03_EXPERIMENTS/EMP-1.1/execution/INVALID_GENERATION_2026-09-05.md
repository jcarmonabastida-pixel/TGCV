# Invalid N-R8-C2 vNext production generation — 2026-09-05

## Status
The first production corpus generated on 2026-09-05 is **INVALID / NOT SCIENTIFICALLY USABLE**.

## Original artifacts
- Corpus: `N-R8-C2_vNEXT_CORPUS_v0.1.jsonl`
- Corpus SHA-256: `abff66d496c2ab5dadbf5adc0e05daf3c2992c18b1b6118b58c8c4d712910f3f`
- Manifest: `N-R8-C2_vNEXT_CORPUS_MANIFEST_v0.1.json`
- Internal manifest `final_manifest_sha256`: `03caf7bb680b93b696dd2914dd06b4c30fe4340559c44698bb33fc9be124c323`
- Raw manifest file SHA-256: `e287fd3bba404d68a5c8d4d8c8d863e98eb47c5a93e101dbe3f35a15bf89a50d`
- Generator blob used: `1cbffad8f14cb004b81e5ef1613e1f288d7962d1`

## Defect
The generator cached the two-element return value of `evaluate_ot_after_key_equality(state, state)` as if it were a single O_T signature. Consequently each record stored `o_t_a_signature` and `o_t_b_signature` with an extra outer nesting level.

The corpus therefore fails authoritative O_T recomputation/audit even though generation reported `PASS`.

## Correction
The generator was corrected so that each cached state stores exactly its own O_T signature:
- `ot_cache[a_sha], _ = evaluate_ot_after_key_equality(a, a)`
- `_, ot_cache[b_sha] = evaluate_ot_after_key_equality(b, b)`

Corrected generator blob SHA-1: `652ffeebab1f43095494a93a5cae04d18656d51d`
Correction commit: `a7d88ddcbbd817275587e8947327ae71b16a2336`

## Disposition
The invalid corpus must be preserved as evidence and must not be treated as a frozen scientific artifact. A corrected corpus will be regenerated under the corrected generator and subjected to the full audit before any EXT-1.1 scientific execution.

Scientific execution and Rust dataset consumption remain **NOT PERFORMED**.
