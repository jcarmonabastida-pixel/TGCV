# C09 Operational Execution Bundle 002 — Hash Manifest

**Status:** `FROZEN — EXECUTION NOT YET AUTHORIZED`
**Derivation:** Corrective successor to Bundle 001. Bundle 001 remains immutable evidence.
**Hash mechanism:** Git blob object SHA-1, recorded as immutable repository content identifiers. The executor additionally computes SHA-256 over exact UTF-8 bytes at runtime; that runtime manifest is part of the execution result and must be independently recomputed by Executor-2.

| Component | Git blob SHA-1 |
|---|---|
| `fixture.json` | `b6f48442965641295269d3bf284cc4416a4070e1` |
| `EXECUTION_SPEC.md` | `ded8f0f3f8c524e60a5fc532b20a6b10c556e444` |
| `execute_c09_bundle_002.py` | `aa201d68f46afcf09071e2edf24408999335942a` |

## SHA-256 rule

Before any scientific authorization, Executor-1 must record SHA-256 for the three components above and the exact runtime fingerprint. Executor-2 must independently recompute the same hashes from its admitted bundle. Any mismatch is a hard block.

The Git blob identifiers provide repository provenance; they are not substituted for the SHA-256 integrity check.

## Corrective change from Bundle 001

The predeclared null is a measurement/control check. Its observed contrast is reported but is not required to equal zero and is not an authorization gate. Integrity authorization is determined only by the declared checks in `EXECUTION_SPEC.md`.
