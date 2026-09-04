# EXT-1.1_Rust — Closure Record

## Status

C1: PASS — historical positive resolution/materialization case.
C2: PASS — expected rejection of yanked tokio 1.0.0 in new offline resolution.
C3: PASS — historical transitive resolution of rand 0.8.0 to 9 packages and successful cargo check --offline.
Independent identity bridge: PASS — serde@1.0.0 -> 50790; tokio@1.0.0 -> 318256; rand@0.8.0 -> 316445.
Checksum integrity: PASS for the archived root artifacts and recorded execution evidence.

## Overall experimental closure

EXT-1.1 is CLOSED at the level of the executed C1/C2/C3 probes and the independent package@version -> version_id bridge.

## Reproducibility qualification

C3 was successfully materialized and compiled offline using a locally reconstructed historical registry. The repository preserves the root rand-0.8.0 crate, resolution lock, resolution log and full cargo-check log, but does not archive every transitive .crate artifact used during compilation. Therefore the repository is an auditable record of the successful run, but not yet a fully self-contained byte-for-byte rebuild bundle.

## Evidence

See execution/C1, execution/C2, execution/C3, RESULTS.md, VERSION_IDS.md and SHA256SUMS.txt.
