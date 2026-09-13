# C09 Operational Execution Bundle 003 — Hash Manifest

**Status:** `FROZEN — EXECUTION NOT YET AUTHORIZED`
**Derivation:** Corrective successor to Bundle 002. Bundles 001 and 002 remain immutable evidence.
**Hash mechanism:** Git blob object SHA-1 provides repository provenance. SHA-256 is the execution-integrity mechanism and must be populated from the exact canonical bytes before authorization.

| Component | Git blob SHA-1 | SHA-256 |
|---|---|---|
| `fixture.json` | `PENDING_FETCH` | `PENDING_CANONICAL_HASH` |
| `EXECUTION_SPEC.md` | `PENDING_FETCH` | `PENDING_CANONICAL_HASH` |
| `execute_c09_bundle_003.py` | `PENDING_FETCH` | `PENDING_CANONICAL_HASH` |

**Authorization rule:** any `PENDING_*` value or any SHA-256 mismatch is a hard block. The manifest itself is not included in the three-file SHA-256 set above; it declares the hashes of those three frozen components.

**Correction from Bundle 002:** the executor now performs the actual SHA-256-to-manifest comparison rather than merely computing and reporting hashes. The null contrast remains a reported control observation and is not an exact-zero authorization gate.
