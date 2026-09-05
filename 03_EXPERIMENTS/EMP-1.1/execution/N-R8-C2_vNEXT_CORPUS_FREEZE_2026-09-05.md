# N-R8-C2 vNext Corpus — Scientific Input Freeze

**Freeze date:** 2026-09-05
**Status:** FROZEN SCIENTIFIC INPUT
**Scientific execution:** NOT_PERFORMED
**Rust dataset consumption:** NOT_PERFORMED

## Corpus identity

- Corpus: `N-R8-C2_vNEXT_CORPUS_v0.1.jsonl`
- Corpus SHA-256: `795bfb12b11be49dc08f4dbe568141cd0a2f7e776c7a10cc8aa9122befb408af`
- Manifest: `N-R8-C2_vNEXT_CORPUS_MANIFEST_v0.1.json`
- Manifest final SHA-256: `14ed0cdc3ec00690b06ea12d4e6cf6b97cd15037a506bfe202984f07f1614c07`
- Target / accepted pairs: `5000 / 5000`
- Candidate count: `27318`
- Equal-key pairs examined: `12317`
- Equal-O_T rejections: `7317`
- Distinct states audited: `7496`

## Frozen inputs

- Config blob SHA: `48c00a16fb50d2258e50920b3bd283810c60d149`
- Contract blob SHA: `62e0ad9b5b075276af4a8716f8ac824e14a47021`
- Generator blob SHA: `652ffeebab1f43095494a93a5cae04d18656d51d`
- Key blob SHA: `40a8cfa6c74cbdf253285b3073372e6c42d262e3`
- Operationalisation blob SHA: `0cc01c7afb051b44f010a798a1b8a256dff286c9`
- O_T implementation blob SHA: `095cff6c69adfba19b1722a5a355b58f7e2cbe1a`
- Seed: `582031`

## Gate evidence

### Pre-generation
`N-R8-C2_vNEXT_PRE_GENERATION_v0.1` — PASS

Conformance result SHA: `4091d7ee78d3a6981228935279ffb6aa33ddc5f32c40b77570a71b3c889734d9`

### Generation
Production generation — PASS

The corrected generator produced the corpus without scientific EXT-1.1 execution and without Rust dataset consumption.

### Corpus audit
`N-R8-C2_vNEXT_CORPUS_AUDIT_v0.1` — PASS

Decision: `CORPUS_AUDITED_READY_FOR_FREEZE`

The audit verified all 5,000 records, state hashes, pair IDs, exact K equality and K hash, authoritative O_T signatures, O_T inequality, provenance/version, input manifest identity, ordering, and manifest integrity.

### Deterministic rerun
`N-R8-C2_vNEXT_DETERMINISTIC_RERUN_v0.1` — PASS

Decision: `DETERMINISTIC_RERUN_CONFIRMED`

The independent full rerun reproduced the production corpus byte-for-byte:

- Rerun corpus SHA: `795bfb12b11be49dc08f4dbe568141cd0a2f7e776c7a10cc8aa9122befb408af`
- Production corpus SHA: `795bfb12b11be49dc08f4dbe568141cd0a2f7e776c7a10cc8aa9122befb408af`
- Byte-for-byte match: `true`
- Production artifacts modified: `false`
- Generation metrics match: `true`
- Manifest deterministic projection matches: `true`
- Manifest records match rerun: `true`

## Freeze decision

The N-R8-C2 vNext corpus is hereby recorded as a **FROZEN SCIENTIFIC INPUT** for EXT-1.1.

This freeze certifies the integrity, reproducibility, and identity of the preparation-stage corpus. It does **not** constitute scientific execution, empirical result, hypothesis confirmation, or validation of TGCV. EXT-1.1 scientific execution remains explicitly pending.

The frozen corpus must not be regenerated, normalized, reordered, overwritten, or otherwise modified. Any future alternative corpus must receive a distinct version and a separate provenance/freeze record.
