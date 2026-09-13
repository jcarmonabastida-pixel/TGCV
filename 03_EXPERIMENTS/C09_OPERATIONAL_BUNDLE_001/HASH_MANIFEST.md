# C09 Operational Execution Bundle 001 — Hash Manifest

**Status:** `FROZEN`
**Hash mechanism:** Git blob object SHA-1, recorded as immutable repository content identifiers. The executor additionally computes SHA-256 over exact UTF-8 bytes at runtime; that runtime manifest is part of the execution result and must be independently recomputed by Executor-2.

| Component | Git blob SHA-1 |
|---|---|
| `fixture.json` | `f403c127f6908912022d11ab9f6c3d7c19205ca6` |
| `EXECUTION_SPEC.md` | `762f2c271f455c627da34e708d24157e23c4f205` |
| `execute_c09_bundle_001.py` | `ac4196d5c79d9770ba033fbe4a4b7e660a01fdb7` |

## SHA-256 rule

Before any scientific authorization, Executor-1 must record SHA-256 for the three components above and the exact runtime fingerprint. Executor-2 must independently recompute the same hashes from its admitted bundle. Any mismatch is a hard block.

The Git blob identifiers provide repository provenance; they are not substituted for the SHA-256 integrity check.
