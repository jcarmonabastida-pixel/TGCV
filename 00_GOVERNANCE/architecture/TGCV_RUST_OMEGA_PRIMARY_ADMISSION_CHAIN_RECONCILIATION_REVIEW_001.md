# TGCV — Rust Ω-Primary Admission-Chain Reconciliation Review 001

**Status:** OPEN — HISTORICAL GOVERNANCE CONFLICT IDENTIFIED / NO RETROACTIVE ADMISSION  
**Date:** 2026-10-09  
**Review type:** Governance continuity and provenance reconciliation; no scientific execution

## 1. Purpose

Reconcile the apparent conflict between the pre-processing admission chain and the later recorded real-data U_t construction. This review preserves both historical records and does not silently rewrite either one.

## 2. Canonical records compared

1. `TGCV_RUST_OMEGA_PRIMARY_RAW_DATA_ADMISSION_AND_INFORMATION_FIREWALL_AUDIT_v0.1.md` — raw-data admission not granted; its next gate is dataset identifiability/privacy admission.
2. `TGCV_RUST_OMEGA_PRIMARY_DATASET_IDENTIFIABILITY_AND_PRIVACY_ADMISSION_REVIEW_v0.1.md` — dataset not admitted because the required package was insufficient.
3. `TGCV_RUST_OMEGA_PRIMARY_DATASET_ADMISSION_PACKAGE_REVIEW_v0.1.md` — dataset admission not granted.
4. `TGCV_RUST_OMEGA_PRIMARY_DATASET_SOURCE_AND_SNAPSHOT_SPECIFICATION_REVIEW_v0.1.md` — source class conditionally acceptable; exact snapshot not frozen at that gate.
5. `TGCV_RUST_OMEGA_PRIMARY_DATASET_SNAPSHOT_MANIFEST_AND_PROVENANCE_REVIEW_v0.1.md` — snapshot manifest conditionally frozen; Ω-primary admission still pending.
6. `TGCV_RUST_OMEGA_PRIMARY_REAL_DATA_PREFLIGHT_EXECUTION_CLOSURE_001.md` — records a later successful local snapshot preflight and states that the retained snapshot is preflight-admitted for the next governed processing gate.
7. `TGCV_RUST_OMEGA_PRIMARY_U_REAL_DATA_CONSTRUCTION_EXECUTION_CLOSURE_001.md` — records a later U_t-only real-data construction PASS under an explicit execution record.

## 3. Findings

### F1 — The records are not logically interchangeable

A snapshot identity/preflight PASS and a U_t construction PASS establish technical properties of the recorded input and computation. They do not, by themselves, prove that the separate identifiability/privacy admission gate was formally satisfied.

### F2 — Later execution is documented, but the intervening admission transition is not yet reconciled

The repository contains a local snapshot SHA-256, schema/preflight findings, a frozen structural construction rule, and a U_t construction closure. The records inspected here do not yet establish a single explicit decision explaining how these later steps relate to the earlier `DATASET ADMISSION: NOT GRANTED` decisions.

### F3 — The existing U_t result carries material missingness

The U_t closure records 2,946,888 `OBSERVED_PRESENT` records, 671,635 `UNKNOWN_MISSING` coverage entries, zero `OBSERVED_ABSENT_COMPLETE`, and an empty `complete_target_packages` set. Thus the existing artifact cannot be used to infer absence/removal from non-observation without additional completeness evidence.

### F4 — No scientific conclusion follows from this governance conflict

The conflict neither falsifies nor validates Ω-primary. It concerns admissibility, provenance and continuity of the data-processing chain.

## 4. Interim disposition

- Preserve the historical gate documents unchanged.
- Preserve the existing preflight and U_t execution closure as historical technical records.
- Do not rerun or rebuild U_t.
- Do not describe the dataset as fully admitted for longitudinal empirical claims until the missing governance transition is explicitly resolved.
- Do not treat `UNKNOWN_MISSING` as absence.
- Do not upgrade Ω-primary, irreducibility, causal, outcome, value, or architectural claims.

**Interim status:** `TECHNICAL U_t ARTIFACT EXISTS / ADMISSION-CHAIN RECONCILIATION OPEN / LONGITUDINAL EMPIRICAL ADMISSION NOT GRANTED`.

## 5. Evidence required to close reconciliation

A follow-up decision must establish, with exact references and without altering historical records:

1. which authoritative provenance and identifiability/privacy evidence applies to the retained 2022-09-07 snapshot;
2. whether the required admission criteria were met before the recorded processing, or whether the processing occurred before the gate was satisfied;
3. the governing treatment of any sequencing deviation, without retroactively claiming a gate passed absent evidence;
4. the exact permitted scope of reuse of the already-produced U_t artifact;
5. whether any remaining limitation prevents only longitudinal interpretation or also blocks structural artifact reuse.

If the required evidence cannot establish a compliant admission, the record must say so explicitly and restrict reuse accordingly. A successful computation must not be used as a substitute for missing admission evidence.

## 6. Boundary

This is a documentation/governance review only. It does not inspect or transform dataset bytes, re-run code, construct a fixture, calculate `T_acc`, Reach, `ΔReach`, `κ`, outcomes, value, or perform a matched-pair test.

TGCV Core remains unchanged. Ω-primary remains a proposed, non-canonical candidate. Architectural transition remains unjustified.

## 7. Next gate

`RUST_OMEGA_PRIMARY_ADMISSION_EVIDENCE_RECONCILIATION_DECISION`

## 8. Published-source cross-check — 2026-10-09

The authors' public repository contains the release-specific README:

- Source: https://github.com/wschuell/repo_datasets/blob/main/rust_repos_2022_09_07/README.md
- Dataset release directory: `rust_repos_2022_09_07`
- Declared data validity upper bound: `2022-09-07`, described as the timestamp of the crates.io database dump used.
- Declared `repodepo` version: `0.1.3`
- Declared `repodepo` commit: `5c592800cbbb09f5b43c91f937f03141140f3c78`
- Documented published formats: SQLite export and PostgreSQL dump files.
- The README describes the export process as anonymizing and cleaning the database; the associated `export_dataset.py` script invokes export, anonymization, cleaning, and dump steps.

### Interpretation and limitations

This is release-specific provenance evidence and supports identifying the intended 2022-09-07 source release. It does **not** prove that the locally retained ZIP is byte-identical to a particular Figshare file/version, nor does it establish the license applicable to that exact file. The release README inspected does not itself state a dataset license. Absence of a license statement in that README is not evidence that no license exists elsewhere.

The author-described anonymization process is not an independent privacy audit of the local ZIP or every field retained in the TGCV processing path.

### Updated evidence disposition

- Source release identity: **PARTIALLY SUPPORTED** by the authors' release-specific README.
- Exact Figshare article/file/version ↔ local ZIP identity: **OPEN**.
- Applicable dataset/file license: **OPEN**.
- Local artifact hash ↔ published file hash or other authoritative identity evidence: **OPEN**.
- Privacy/identifiability adequacy for TGCV's specific retained fields and intended reuse: **OPEN**.
- Historical admission-sequence reconciliation: **OPEN**; no retroactive admission inferred.

This cross-check is documentary only. No dataset bytes were inspected or transformed, no scientific code was run, and no TGCV Core or Ω-primary status was changed.

## 9. Publisher/article-level cross-check — 2026-10-09

The published data descriptor identifies the dataset citation as Schueller et al., *Replication Data for Evolving collaboration, dependencies, and use in the Rust Open Source Software ecosystem*, Figshare collection DOI `10.6084/m9.figshare.c.5983534.v1`. The article states that the data are hosted on Figshare, that several distribution formats are provided, and that no format exceeds 6 GB when compressed. It describes pseudonymisation as discarding name attributes and hashing email addresses and GitHub/GitLab logins using MD5 with a random salt.

Sources:
- Article / data descriptor: https://www.nature.com/articles/s41597-022-01819-z
- Associated PubMed Central full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC9668998/
- Authors' release README: https://github.com/wschuell/repo_datasets/blob/main/rust_repos_2022_09_07/README.md

### Interpretation boundary

The publisher-level size statement is compatible with the locally recorded approximate ZIP size (~5.7 GB), but this is only a coarse consistency check. It is not proof of byte identity, exact file identity, version identity, or license. The cited DOI is a **collection DOI**, not yet the verified article/file/version identifier corresponding to the local ZIP. The article's own CC BY 4.0 statement licenses the article and must not be assumed to license the separate dataset file.

### Current evidence disposition

- Published dataset collection and author repository linkage: **SUPPORTED**.
- Intended 2022-09-07 release provenance: **PARTIALLY SUPPORTED**.
- Exact Figshare item/file/version and local ZIP correspondence: **OPEN**.
- Applicable dataset/file license: **OPEN**.
- Privacy/identifiability adequacy for TGCV's exact retained fields and intended use: **OPEN**.
- Admission-chain reconciliation: **OPEN**; no retroactive admission inferred.

The Figshare DOI could not be resolved to item-level metadata through the available lookup route in this review. The next evidence-bearing action is to retrieve item/version/file metadata from Figshare's collection API or landing page and compare it against the existing local manifest. Do not re-download or reprocess the dataset merely to settle this metadata question.

This is a documentary cross-check only. No dataset bytes were inspected or transformed, no scientific code was run, and no TGCV Core or Ω-primary status was changed.


## 10. Figshare item/version/file metadata cross-check — 2026-10-09

The public Figshare collection API returned collection `5983534`, DOI `10.6084/m9.figshare.c.5983534.v1`, linked to the scientific data descriptor DOI `10.1038/s41597-022-01819-z`. Its public articles endpoint lists two separate dataset records:

### Full dataset — candidate exact published file

- Item title: `Full dataset`
- Item DOI: `10.6084/m9.figshare.21345990.v1`
- Item ID: `21345990`; version: `1`
- File ID: `37887018`
- Published filename: `rust_repos_2022_09_07.zip`
- Published file size: `6,047,715,996` bytes
- Figshare supplied MD5 and computed MD5: both `a6b9feffdc3dafc86fa80ec23de38c10`
- Item license metadata: `CC0`, linking to `https://creativecommons.org/publicdomain/zero/1.0/`
- Public item page: https://springernature.figshare.com/articles/dataset/Full_dataset/21345990
- File download URL (recorded as provenance only; no download performed): https://ndownloader.figshare.com/files/37887018

### Sample dataset — distinct item, not the full dataset

- Item title: `Sample Dataset`
- Item DOI: `10.6084/m9.figshare.21345993.v1`
- Item ID: `21345993`; version: `1`
- File ID: `37887000`
- Published filename: `rust_repos_sample_2022_09_07.zip`
- Published file size: `174,313,664` bytes
- Published supplied/computed MD5: `c06f416f13f9f6c736b075ae715f7c47`
- Item license metadata: `CC0`, linking to `https://creativecommons.org/publicdomain/zero/1.0/`
- Public item page: https://springernature.figshare.com/articles/dataset/Sample_Dataset/21345993

### Interpretation and remaining identity check

The official metadata now identifies the exact published full-dataset item, version, filename, size, file ID, and item-level CC0 license. This resolves the earlier uncertainty about which Figshare item represents the full dataset and provides an authoritative published MD5 for a possible identity check.

It does **not yet prove** the locally retained ZIP is byte-identical to the published file: the local ZIP's previously recorded SHA-256 (`823b74d779c83f2b46dc02e8168c259d5701dca106465533b82277e29d852224`) is a different hash algorithm and cannot be compared directly with the published MD5. No local file bytes were read or hashed as part of this metadata cross-check. A non-content metadata comparison of the local file's exact byte size against `6,047,715,996` bytes remains to be recorded; even equal size would be consistency evidence, not proof of byte identity.

The Figshare record explicitly declares CC0 for the dataset item. Record that as the published item-level license metadata; do not infer additional privacy clearance, fitness for every TGCV use, or admission-gate satisfaction from the license.

### Updated evidence disposition

- Published collection and article linkage: **SUPPORTED**.
- Exact Figshare full-dataset item/version/file identity: **SUPPORTED** as a published source record.
- Local ZIP ↔ published file byte identity: **OPEN**.
- Local file exact-size comparison: **OPEN**.
- Published item-level license metadata: **SUPPORTED — CC0 declared by Figshare**.
- Privacy/identifiability adequacy for TGCV's exact retained fields and intended use: **OPEN**.
- Historical admission-sequence reconciliation: **OPEN**; no retroactive admission inferred.

This cross-check used only public Figshare metadata supplied by the user. No dataset bytes were inspected or transformed, no dataset was downloaded, no scientific code was run, and no TGCV Core or Ω-primary status was changed.
