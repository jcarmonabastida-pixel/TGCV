# EXT-1.1_Rust — Experimental Results Consolidation

## Scope

This file consolidates the observed results of the three controlled Cargo probes performed against the historical Rust registry snapshots.

Source policy: local historical snapshot only.

## C1 — Positive historical resolution

Target: serde ^1.0.0

Observed: Cargo.lock pins serde 1.0.0. Historical checksum: 369633cfe0f0bde1dfc037fb6c5a329d46586a31f981bed14d87487a3439ae37.

Interpretation: Positive historical resolution/materialization case.

## C2 — Yanked version rejection

Target: tokio =1.0.0

Observed: tokio 1.0.0 is present in the 2021 historical index and is marked yanked. Cargo generate-lockfile --offline rejects the new resolution because version 1.0.0 is yanked.

Historical checksum: 9f4bfdcbd00fa893ac0549b38aa27080636a0104b0d0c38475a99439405e1df8.

Interpretation: Expected negative resolution case.

## C3 — Positive transitive resolution and materialization

Target: rand =0.8.0

Observed: Cargo resolved 9 packages offline. rand 0.8.0 resolved successfully and cargo check --offline completed successfully. The Cargo.lock records the historical transitive graph.

Historical checksum for rand 0.8.0: a76330fb486679b4ace3670f117bbc9e16204005c4bde9c4bd372f45bed34f12.

Interpretation: Positive historical transitive resolution and local materialization case.

## Current conclusion

C1, C2 and C3 have all produced their intended observable outcomes.

This file does NOT by itself declare EXT-1.1 PASS.

Remaining closure items:
1. Verify the independent package@version -> version_id bridge.
2. Consolidate checksum/evidence records.
3. Update the experiment manifest only after those closure checks.
