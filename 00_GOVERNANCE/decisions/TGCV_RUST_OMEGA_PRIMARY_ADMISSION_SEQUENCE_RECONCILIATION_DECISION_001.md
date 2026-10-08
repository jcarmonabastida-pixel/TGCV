# TGCV — Rust Ω-Primary Admission-Sequence Reconciliation Decision 001

**Status:** DECISION RECORDED — SEQUENCING DEVIATION ACKNOWLEDGED / EMPIRICAL REUSE RESTRICTED  
**Date:** 2026-10-09  
**Decision type:** Governance continuity; no scientific execution  
**Scope:** Historical Rust snapshot, real-data preflight, and existing U_t construction artifact  
**Branch:** `governance/rust-omega-raw-data-admission-firewall-audit-20261009`

## 1. Decision question

How should TGCV represent the fact that canonical admission reviews dated 2026-10-01 recorded dataset admission as not granted, while later records document a real-snapshot preflight on 2026-10-02 and U_t construction using the same retained snapshot?

## 2. Evidence basis

This decision is limited to the following canonical records on `main` and the provenance cross-checks recorded in the linked reconciliation review:

1. `TGCV_RUST_OMEGA_PRIMARY_RAW_DATA_ADMISSION_AND_INFORMATION_FIREWALL_AUDIT_v0.1.md` — raw-data admission not granted; identifiability/privacy gate required before acquisition or processing.
2. `TGCV_RUST_OMEGA_PRIMARY_DATASET_IDENTIFIABILITY_AND_PRIVACY_ADMISSION_REVIEW_v0.1.md` — dataset admission not granted because the required frozen admission evidence was insufficient.
3. `TGCV_RUST_OMEGA_PRIMARY_DATASET_ADMISSION_PACKAGE_REVIEW_v0.1.md` — admission package incomplete; dataset admission not granted.
4. `TGCV_RUST_OMEGA_PRIMARY_DATASET_SOURCE_AND_SNAPSHOT_SPECIFICATION_REVIEW_v0.1.md` — source class conditionally acceptable, exact snapshot not frozen at that gate.
5. `TGCV_RUST_OMEGA_PRIMARY_DATASET_SNAPSHOT_MANIFEST_AND_PROVENANCE_REVIEW_v0.1.md` — snapshot manifest conditionally frozen and provenance bound to the retained artifact; Ω-primary admission still pending.
6. `TGCV_RUST_OMEGA_PRIMARY_REAL_DATA_PREFLIGHT_EXECUTION_CLOSURE_001.md` — technical preflight PASS; describes the retained snapshot as preflight-admitted for the next processing gate.
7. `TGCV_RUST_OMEGA_PRIMARY_U_REAL_DATA_CONSTRUCTION_EXECUTION_CLOSURE_001.md` — U_t-only construction PASS under a recorded execution authorization, with 671,635 UNKNOWN_MISSING entries and no OBSERVED_ABSENT_COMPLETE entries.
8. `TGCV_RUST_OMEGA_PRIMARY_ADMISSION_CHAIN_RECONCILIATION_REVIEW_001.md` — published-source and Figshare item/file cross-check; local ZIP MD5 and byte size match the published full-dataset file metadata.

## 3. Findings

### F1 — The canonical admission gate was not recorded as passed before processing

The 2026-10-01 admission documents explicitly say **DATASET ADMISSION: NOT GRANTED** and prohibit download/processing pending sufficient identifiability/privacy evidence. The later technical closures establish that preflight and U_t construction occurred; they do not document a formal decision superseding or satisfying that earlier admission gate.

### F2 — This is a governance sequencing deviation, not a scientific result

On the records available, the correct reconciliation is to acknowledge that the technical processing chain advanced before the required canonical admission transition was evidenced. Do not reinterpret the earlier denial as approval, infer retroactive admission from successful execution, or silently rewrite historical closures.

### F3 — File identity is now supported, but privacy admission is still unresolved

The local ZIP's supplied MD5 matches Figshare's published MD5 for the full dataset item, and the filename and byte size match. Figshare declares CC0 for that item. These facts strengthen provenance and licensing identification; they do not establish that the fields retained by TGCV are sufficiently minimised, non-identifying, or appropriate for the intended processing and research use.

### F4 — The U_t artifact remains technically reproducible but not cleared for empirical reuse

The construction closure reports 2,946,888 OBSERVED_PRESENT and 671,635 UNKNOWN_MISSING, with zero OBSERVED_ABSENT_COMPLETE and an empty complete_target_packages set. Therefore absence/removal must not be inferred from non-observation. Neither this technical PASS nor the current provenance match authorises further scientific interpretation.

## 4. Decision

The historical sequence is reconciled as follows:

1. **Admission status:** the dataset was **not formally admitted before the recorded processing**, on the evidence currently canonical.
2. **Deviation status:** record a **governance sequencing deviation** between the fail-closed admission decisions and the later preflight/U_t construction.
3. **Historical integrity:** preserve the admission reviews, preflight closure, construction closure, hashes, and execution records unchanged. Do not retroactively alter their dates or meanings.
4. **Existing artifact scope:** preserve the existing U_t result as a historical technical artifact for provenance, audit, and reproducibility review only. Do not use it to support scientific claims, longitudinal absence/removal claims, or further empirical derivations until a prospective governance decision resolves the admission and permitted-reuse question.
5. **Further processing:** no new download, transformation, U_t rebuild, derivation, fixture construction, or scientific run is authorised by this decision.
6. **Admission remediation:** the next gate must assess the complete identifiability/privacy package for the exact retained fields and intended use, including minimisation, access, retention, processing boundaries, and explicit permitted-reuse scope. That gate must make a prospective decision; it cannot erase the sequencing deviation.
7. **Architectural status:** TGCV Core remains unchanged. Ω-primary remains a proposed, non-canonical candidate. No claim about irreducibility, causality, outcomes, value, or Transformational Intelligence is upgraded.

## 5. Conditions for reconsidering reuse

Reconsideration requires a new explicit decision based on, at minimum:

- exact source item/version/file and matching retained snapshot identity;
- a field-by-field inventory of the actual retained and derived fields;
- semantic/provenance classification and confirmation that prohibited outcome/accessibility information did not enter U_t;
- identifiability/privacy risk assessment for the actual fields and intended use, not merely the publisher's general description of anonymisation;
- data minimisation and access/retention controls;
- license/terms record for the exact dataset item;
- an explicit decision about whether the already-produced U_t artifact may be reused, and for which limited purposes.

A failed or incomplete criterion keeps empirical reuse blocked. No requirement is deemed met solely because the computation completed successfully.

## 6. Current state after this decision

- **Source/file identity:** MATCHED to published Figshare full-dataset metadata.
- **Technical preflight:** PASS (historical record).
- **U_t construction:** PASS (historical record; U_t-only scope).
- **Admission before processing:** NOT EVIDENCED / NOT GRANTED.
- **Sequencing deviation:** ACKNOWLEDGED.
- **Privacy/identifiability clearance for TGCV's exact retained fields and intended use:** OPEN.
- **Further scientific processing or empirical reuse:** BLOCKED pending a new prospective decision.
- **Longitudinal empirical admission:** NOT GRANTED.
- **Core / Ω-primary claim status:** UNCHANGED.

## 7. Linked reconciliation review

`00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_ADMISSION_CHAIN_RECONCILIATION_REVIEW_001.md`

This decision is a governance record only. It does not process data, rerun code, reconstruct U_t, or perform scientific execution.


## 8. Follow-up field-level assessment — 2026-10-09

A documentary field-level inventory has been added at:

`00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_FIELD_LEVEL_PRIVACY_AND_REUSE_ASSESSMENT_001.md`

It maps the two input CSV schemas and emitted U_t fields, including numeric identifiers, timestamps, dependency structure, and dependency-row provenance ordinals. It finds no direct personal identifier explicitly listed in those two documented schemas, but does not conclude that the data are anonymous: external linkage and structural/timestamp inference remain unassessed.

**Privacy/identifiability clearance remains NOT GRANTED.** The existing U_t artifact remains restricted to documentary provenance/audit review; structural scientific reuse, longitudinal claims, further processing, and external disclosure remain blocked pending a prospective decision. This assessment did not inspect data bytes or execute scientific code.


## 9. Proposed controls for prospective reuse decision — 2026-10-09

A proposed control and reuse-scope matrix is recorded at:

`00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_DATA_MINIMISATION_ACCESS_RETENTION_AND_REUSE_SCOPE_PROPOSAL_001.md`

It proposes conservative boundaries for raw/derived artifacts, identifier and provenance minimisation, access verification, retention/deletion decisions, and use-specific approval. It does not select or grant any future reuse category. Privacy clearance remains **NOT GRANTED**, structural/longitudinal empirical reuse remains **BLOCKED**, and any new processing still requires separate prospective approval.
