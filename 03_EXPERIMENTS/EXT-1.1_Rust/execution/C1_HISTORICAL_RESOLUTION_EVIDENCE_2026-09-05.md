# C1 Historical Resolution Evidence — 2026-09-05

## Scope
Confirmatory historical reconstruction case C1 for CHR-MICRO-3. This evidence concerns historical dependency resolution only and does not consume or modify the frozen N-R8-C2 corpus.

## Historical cutoff
- Snapshot date: 2018-09-26
- crates.io-index snapshot commit: `9110daee6752e903379f3af955506d6116315273`
- Historical toolchain: `1.29.1-x86_64-pc-windows-msvc`
- rustc: `rustc 1.29.1 (b801ae664 2018-09-20)`
- Cargo: `cargo 1.29.0 (524a578d7 2018-08-05)`

## Resolution isolation
Cargo 1.29.0 was configured through the project-local `.cargo/config` using source replacement:

```text
[source.crates-io]
replace-with = "tgcv-historical"

[source.tgcv-historical]
local-registry = "local_registry"
```

The local registry contained the historically extracted index records and checksum-verified crate archives required for C1. The current registry was not used as the resolution source.

## Root package

```toml
[package]
name = "tgcv_ext11_c1_historical_resolver"
version = "0.1.0"

[dependencies]
serde = { version = "=1.0.0", features = ["derive"] }
```

## Resolved graph
The clean historical resolution produced the following dependency versions:

- `serde 1.0.0`
- `serde_derive 1.0.79`
- `proc-macro2 0.4.19`
- `quote 0.6.8`
- `syn 0.15.6`
- `unicode-xid 0.1.0`

The resulting `Cargo.lock` SHA-256 was:

`1AD55D5BAD473DFC6F88854FEA5DCFF4863EC21BC6D5602FD089FD93977C98BD`

## Reproducibility
The first generated `Cargo.lock` was preserved as an evidence copy. The working `Cargo.lock` was then deleted and `cargo generate-lockfile` was executed again using the same historical toolchain and local registry configuration.

- First lock SHA-256: `1AD55D5BAD473DFC6F88854FEA5DCFF4863EC21BC6D5602FD089FD93977C98BD`
- Clean rerun lock SHA-256: `1AD55D5BAD473DFC6F88854FEA5DCFF4863EC21BC6D5602FD089FD93977C98BD`
- Deterministic byte-for-byte match: PASS

## Archive/checksum bridges
The selected resolved crate archives were independently downloaded and verified against the historical index checksums:

- `serde 1.0.0`: `369633CFE0F0BDE1DFC037FB6C5A329D46586A31F981BED14D87487A3439AE37`
- `serde_derive 1.0.79`: `31569D901045AFBFF7A9479F793177FE9259819AFF10AB4F89EF69BBC5F567FE`
- `proc-macro2 0.4.19`: `FFE022FB8C8BD254524B0B3305906C1921FA37A84A644E29079A9E62200C3901`
- `quote 0.6.8`: `DD636425967C33AF890042C483632D33FA7A18F19AD1D7EA72E8998C6EF8DEA5`
- `syn 0.15.6`: `854B08A640FC8F54728FB95321E3EC485B365A97FE47609797C671ADDD1DDE69`
- `unicode-xid 0.1.0`: `FC72304796D0818E357EAD4E000D19C9C174AB23DC11093AC919054D20A6A7FC`

## Gate status
- C1 R1 release identity: PASS
- C1 R2 historical registry state: PASS
- C1 R3 dependency metadata: PASS for the reconstructed graph
- C1 R4 candidate universe: PASS for the demonstrated local snapshot replay
- C1 R5 deterministic historical resolution: PASS
- C1 R6 version-ID bridge: PASS based on the independently verified mapping already recorded in `VERSION_IDS.md`
- R5 global CHR-MICRO-3 status: OPEN pending remaining required cases/evidence
- CHR-MICRO-3 global gate: BLOCKED / NOT EXECUTED
- EXT-1.1 scientific execution: NOT PERFORMED

## Interpretation boundary
This record demonstrates a reproducible historical resolution for confirmatory case C1. It does not by itself establish complete historical Cargo resolver equivalence for every possible dependency construct, nor does it close the global CHR-MICRO-3 gate. C2 and C3, plus the remaining reconstruction checks, remain required according to the gate protocol.
