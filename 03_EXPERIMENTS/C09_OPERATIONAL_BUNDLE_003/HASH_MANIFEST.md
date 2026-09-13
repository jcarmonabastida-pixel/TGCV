# C09 Operational Execution Bundle 003 — Hash Manifest

**Status:** `FROZEN — EXECUTION NOT YET AUTHORIZED`
**Derivation:** Corrective successor to Bundle 002. Bundles 001 and 002 remain immutable evidence.
**Hash mechanism:** Git blob object SHA-1 provides repository provenance. SHA-256 is the execution-integrity mechanism and is populated from the exact canonical bytes in the frozen checkout.

| Component | Git blob SHA-1 | SHA-256 |
|---|---|---|
| `fixture.json` | `141f6952a915150d538bc9a2241d14600d6be471` | `3E3AC9601F893B7E01F75813499BB3F539D7B192AE18F0332DC6365AAA5EBD49` |
| `EXECUTION_SPEC.md` | `606c84dcfd2c4000007ed5930533aef1c981428a` | `D1621DBBCB9DD840828D0F3C431949D7DDA2B73F3E4B43EA86F35FC07A87E10B` |
| `execute_c09_bundle_003.py` | `d983e15a485b2e12a36b3c69271ab1bcc995b7c3` | `94534CC29FA31E86A9936DE8615D8B0114D44F183942C2126E817E507BF62AC3` |

**Authorization rule:** any `PENDING_*` value or any SHA-256 mismatch is a hard block. The manifest itself is not included in the three-file SHA-256 set above; it declares the hashes of those three frozen components.

**Correction from Bundle 002:** the executor now performs the actual SHA-256-to-manifest comparison rather than merely computing and reporting hashes. The null contrast remains a reported control observation and is not an exact-zero authorization gate.
