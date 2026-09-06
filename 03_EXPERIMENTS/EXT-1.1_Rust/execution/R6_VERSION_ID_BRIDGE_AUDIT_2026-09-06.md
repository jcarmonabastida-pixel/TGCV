# EXT-1.1 Rust — R6 Version-ID Bridge Audit v0.1

Date: 2026-09-06
Status: PASS — demonstrated for C1–C3
Scientific execution: NOT PERFORMED

## Purpose
Audit the independent `package@version -> crates.io version_id` bridge required by CHR-MICRO-3 R6. The bridge must identify the exact crates.io version corresponding to each historically reconstructed package/version without using dependency outcomes, the frozen N-R8-C2 corpus, or scientific execution results.

## Evidence source
Authoritative bridge record:
`03_EXPERIMENTS/EXT-1.1_Rust/execution/VERSION_IDS.md`

The bridge is explicitly described there as an independent package@version -> version_id mapping obtained from the crates.io API, queried independently of the local historical registry.

## Audited mappings

| Case | Package | Version | version_id | Historical checksum | Bridge checksum match |
|---|---|---:|---:|---|---|
| C1 | serde | 1.0.0 | 50790 | `369633cfe0f0bde1dfc037fb6c5a329d46586a31f981bed14d87487a3439ae37` | PASS |
| C2 | tokio | 1.0.0 | 318256 | `9f4bfdcbd00fa893ac0549b38aa27080636a0104b0d0c38475a99439405e1df8` | PASS |
| C3 | rand | 0.8.0 | 316445 | `a76330fb486679b4ace3670f117bbc9e16204005c4bde9c4bd372f45bed34f12` | PASS |

## Audit findings

1. All three confirmatory historical cases have an explicit `version_id`.
2. Package and version are exact, so the bridge is keyed by the intended `package@version` identity rather than by package name alone.
3. The bridge source is independent of the local historical registry used for reconstruction.
4. The checksum is retained alongside each mapping, providing an additional identity consistency check against the reconstructed artifact metadata.
5. C2 being yanked does not invalidate the existence of its historical `version_id`; the bridge identifies the historical version independently of whether fresh dependency resolution would select it.
6. No outcome data, frozen corpus membership, or scientific execution result is used by this bridge.

## R6 verdict

**R6 — PASS for C1–C3.**

The required package@version -> crates.io version_id bridge is demonstrated for all three historical confirmatory cases used in the current CHR-MICRO-3 reconstruction work.

This PASS is scoped to the demonstrated cases. It does not claim that every package/version in the eventual EXT-1.1 observation universe has already been bridged. Any expansion of the empirical universe must apply the same independent bridge procedure before scientific execution.

## Gate implications

- C1 R6: PASS
- C2 R6: PASS
- C3 R6: PASS
- Global R6: PASS for current confirmatory reconstruction cases; broader empirical-universe coverage remains to be established during R7/R8 preparation if required.
- CHR-MICRO-3 global gate: remains OPEN / NOT CLOSED because R7–R10 are not yet demonstrated.
- EXT-1.1 scientific execution: NOT PERFORMED.

## Integrity boundary
This audit does not modify or consume the frozen N-R8-C2 corpus. It does not alter historical snapshots, Cargo resolution artifacts, or the scientific execution boundary.
