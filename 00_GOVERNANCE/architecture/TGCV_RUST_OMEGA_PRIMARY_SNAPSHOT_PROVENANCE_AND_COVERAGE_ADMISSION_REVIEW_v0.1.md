# TGCV — Rust Ω-Primary Snapshot Provenance and Coverage Admission Review v0.1

**Status:** CLOSED — COVERAGE BASIS PARTIALLY ADMITTED / FORMAL Ω DATASET ADMISSION NOT YET GRANTED  
**Date:** 2026-10-02  
**Gate:** RUST_OMEGA_PRIMARY_SNAPSHOT_PROVENANCE_AND_COVERAGE_ADMISSION_REVIEW

## 1. Evidence basis

The existing canonical Rust real-data preflight establishes a fixed local artifact:

- `C:\Users\pedri\Downloads\rust_repos_2022_09_07.zip`
- SHA-256: `823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`
- expected hash matched: YES
- ZIP opened: YES
- structural members and schemas: PASS.

The same preflight records the temporal rule `DR-035-v0.1-ADJACENT-CREATED-AT` and horizon `H=1`.

## 2. Provenance status

The intended historical source has previously been identified operationally as a Figshare Rust dataset snapshot associated with the 2022-09-07 corpus.

However, the current canonical repository does not contain a complete frozen provenance manifest binding all of the following into one auditable record:

1. source DOI/item identity;
2. exact published version;
3. source file/archive identity;
4. local ZIP byte hash;
5. archive member manifest;
6. acquisition date/provenance;
7. licensing/usage metadata.

Therefore provenance is **CONDITIONALLY IDENTIFIED, NOT FULLY FROZEN**.

No new download is warranted to resolve this. The existing local artifact remains the only candidate snapshot for this route.

## 3. Coverage status

The prior preflight establishes the presence of the two structural CSV members required by the existing Rust route:

- `package_versions.csv`
- `package_dependencies.csv`

This establishes **structural presence**, not complete database coverage.

For Ω-primary use, coverage must additionally distinguish:

- observed presence;
- observed complete absence;
- unknown/missing;
- out-of-scope.

Structural appearance/disappearance cannot be inferred from absence unless completeness for the relevant snapshot is established.

The current evidence therefore supports **schema/member presence**, but not yet a frozen completeness claim over the full transformation universe.

## 4. Ω implications

The existing data are sufficient to retain the Rust route as the active empirical candidate because they expose primitive structural fields:

- package/version identity;
- version creation time;
- dependency declaration;
- dependency target identity.

They are not sufficient, by this gate alone, to admit:

`Ω_T,t=(U_t,≡_T,R_t)`

because the following remain open:

- exact transformation identity/canonicalisation;
- relation vocabulary and completeness;
- longitudinal correspondence `κ`;
- coverage/completeness manifest;
- provenance binding;
- state-reducibility test.

## 5. Decision

**LOCAL SNAPSHOT:** RETAINED.

**BYTE IDENTITY:** PREVIOUS PREFLIGHT PASS.

**STRUCTURAL MEMBER PRESENCE:** PASS.

**COVERAGE:** PARTIAL / NOT YET FROZEN.

**PROVENANCE:** CONDITIONALLY IDENTIFIED / NOT YET FULLY FROZEN.

**Ω-PRIMARY DATASET ADMISSION:** NOT GRANTED.

**DOWNLOAD:** PROHIBITED AS A SUBSTITUTE; use the existing local snapshot.

**SCIENTIFIC EXECUTION:** NOT AUTHORIZED.

Core, Evidence→Claim Matrix v1.44 and RMA v3.37 remain unchanged.

## 6. Next gate

`RUST_OMEGA_PRIMARY_PROVENANCE_MANIFEST_AND_COVERAGE_FREEZE_REVIEW`
