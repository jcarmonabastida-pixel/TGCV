# TGCV — Rust Ω-Primary Data Minimisation, Access, Retention and Reuse Scope Proposal 001

**Status:** PROPOSED — NOT AN ADMISSION DECISION / NOT AN EXECUTION AUTHORIZATION  
**Date:** 2026-10-09  
**Scope:** Existing Rust 2022-09-07 source ZIP and historical U_t artifact  
**Branch:** `governance/rust-omega-raw-data-admission-firewall-audit-20261009`

## 1. Purpose

Translate the documentary field-level assessment into explicit, conservative controls that a future prospective admission decision can accept, amend, or reject. This proposal does not grant privacy clearance, admit the dataset, authorise scientific reuse, or retroactively cure the acknowledged processing-sequence deviation.

The current disposition remains:

- privacy/identifiability clearance: **NOT GRANTED**;
- structural scientific reuse of the existing U_t: **BLOCKED**;
- longitudinal empirical interpretation: **BLOCKED**;
- new download, transformation, reconstruction, fixture creation, or scientific execution: **NOT AUTHORISED**.

## 2. Artifact classes

| Class | Artifact | Proposed treatment |
|---|---|---|
| A — Raw source | Local `rust_repos_2022_09_07.zip` (published full dataset; matching size and MD5 recorded) | Restricted, non-public; use only for provenance or a separately authorised operation |
| B — Derived structural artifact | Existing U_t JSON result, approximately 1.08 GB, with numeric identifiers, timestamps, dependency structure, and row-level provenance | Treat as potentially linkable; not anonymous by assumption; no scientific reuse pending prospective approval |
| C — Governance evidence | Source/item metadata, hashes, code identity, schemas, execution closures, audits, this proposal | May be reviewed as documentary provenance evidence; do not include raw rows or expose the large artifact through GitHub |
| D — Future minimised derivative | Any artifact produced after a new approved minimisation rule | Not currently authorised; must receive its own specification, hash, validation, and reuse decision |

## 3. Proposed minimisation controls

These are proposals for the next decision, not claims that the current artifacts already comply.

1. **Purpose limitation:** restrict any eventual admission to the explicitly named TGCV research question and the minimum fields needed for that question. Do not treat general scientific interest as sufficient purpose.
2. **Raw-field boundary:** the documented runner reads only `package_versions.csv` and `package_dependencies.csv`; this is a code-path boundary, not an archive-wide privacy assessment. Do not broaden the member set without a new gate.
3. **Input minimisation:** review whether `semver_str` must be read when its value is not emitted into U_t. If it is not needed for validation of the frozen contract, a future implementation should avoid reading it; any such change requires its own versioned review and must not silently replace the historical implementation.
4. **Identifier minimisation:** retain numeric IDs only where necessary to define `tau`, resolve dependency relations, or establish required provenance. Consider whether any future research derivative can use stable pseudonymous IDs instead of raw source IDs; do not alter the existing artifact in place.
5. **Provenance minimisation:** the dependency row ordinal enables exact source-row traceability but also linkage to the raw file. Decide whether it is necessary in a research-facing derivative. If auditability requires it, separate restricted provenance from a minimised analysis artifact rather than removing it without a traceability plan.
6. **Temporal minimisation:** retain the cutoff and timestamp precision only to the degree required by the specified temporal rule. Any coarsening must be evaluated for its effect on temporal ordering and must not be introduced into the current U_t without a new specification.
7. **No enrichment:** do not join package/version identifiers to public registries, repository accounts, author identities, emails, or other external data as part of privacy review without a separately authorised threat-model or linkage study.
8. **No row-level public release:** do not publish the raw ZIP, existing U_t, or a row-level derivative through GitHub, a public supplement, or external collaboration pending explicit disclosure review.

## 4. Proposed access controls

Current technical access controls have not been independently verified by this document. A future admission decision should record evidence for each selected control.

- Limit raw ZIP and existing U_t access to the minimum number of authorised project operators.
- Keep the raw ZIP and U_t outside the public repository; continue storing only metadata, manifests, hashes, code, protocols, and permitted aggregate outputs in GitHub.
- Record the storage location, access principal(s), and access-control mechanism in a restricted operational record; do not put personal account secrets or sensitive access details in the public repository.
- Confirm whether local disk encryption, OS account separation, backups, and synchronisation services are enabled before granting reuse; mark unverified controls OPEN rather than assuming compliance.
- Do not transfer either artifact to collaborators or external services until that recipient, purpose, transfer channel, and retention are explicitly approved.
- If access cannot be restricted or verified, keep the relevant artifact blocked from empirical use.

## 5. Proposed retention and deletion controls

No retention/deletion policy is currently evidenced as frozen for these artifacts. The following conservative policy is proposed for prospective approval:

1. Preserve the existing artifacts unchanged as historical evidence while the admission-sequence reconciliation and audit obligations remain open.
2. During this blocked period, allow documentary governance review only; do not inspect row-level content for scientific purposes.
3. At the next formal gate, choose one of these explicit outcomes for each artifact: retain under restricted research admission; retain solely as historical evidence; or securely delete after confirming that required audit evidence can be preserved without the artifact.
4. If restricted research admission is later granted, record a concrete review/deletion date or event, an accountable owner/role, backup handling, and the process for verified deletion. “Keep indefinitely” must not be the default without an explicit rationale.
5. Do not delete the only copy or modify an artifact as an ad hoc minimisation measure; any deletion or replacement must preserve a canonical record of the decision and required integrity evidence.

No actual retention setting, disk encryption, backup status, or deletion action is asserted or changed by this proposal.

## 6. Reuse-scope matrix proposed for the prospective decision

| Use category | Proposed current disposition | What a future decision must specify |
|---|---|---|
| Review of published metadata, hashes, code and governance documents | **Allowed as documentary governance review** | Exact sources reviewed; no row-level content inspection |
| Verification of a recorded hash or file metadata without opening row-level content | **Allowed where it does not transform or inspect dataset content** | Exact artifact and command; record output |
| Opening/parsing the raw ZIP or U_t to inspect rows | **Blocked** | Purpose, fields, operator, environment, minimisation, audit trail |
| Structural scientific derivation from existing U_t | **Blocked** | Research question, exact artifact hash, approved fields, validation and output controls |
| Longitudinal comparison, absence/removal, coverage or trajectory claims | **Blocked** | Multiple admitted snapshots, completeness evidence, semantics and separate scientific gate |
| External sharing or public disclosure | **Blocked** | Recipient/audience, exact fields, disclosure risk, license/terms and explicit approval |
| Rebuild or new transformation | **Blocked** | New versioned specification, prospective data-admission approval and explicit execution authorization |

“Allowed” in the first two rows means only documentary/metadata governance work within the stated boundary. It is not a general permission to access the dataset contents.

## 7. Required prospective approval checklist

Before any structural research reuse, the responsible decision-maker must explicitly record PASS/FAIL/OPEN for:

- [ ] exact snapshot identity and provenance;
- [ ] actual source fields and derived output fields confirmed against the frozen implementation;
- [ ] necessity of every retained identifier, timestamp, and provenance pointer;
- [ ] linkage threat model and whether independent review is needed;
- [ ] access controls and storage boundary verified;
- [ ] retention, review/deletion date or event, backups, and owner defined;
- [ ] intended use(s) and prohibited use(s) stated;
- [ ] external sharing/publication status decided;
- [ ] existing U_t reuse expressly approved or denied;
- [ ] longitudinal inference separately blocked unless completeness/admission evidence supports it;
- [ ] acknowledged sequencing deviation retained in the record;
- [ ] separate execution authorization issued if any new processing is proposed.

An OPEN or FAIL item blocks the corresponding use. A license declaration or successful technical execution cannot substitute for these controls.

## 8. Decision requested at the next gate

The next gate should review this proposal and the field-level assessment, then either:

- **A. Accept with evidence:** approve only the specific reuse categories and controls that are evidenced;
- **B. Amend:** specify the exact changes and evidence required, leaving reuse blocked meanwhile; or
- **C. Reject / retain audit-only:** prohibit empirical reuse and preserve the artifact solely for governance/audit purposes.

This document itself chooses none of A/B/C and does not imply approval.

## 9. Related records

- `00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_FIELD_LEVEL_PRIVACY_AND_REUSE_ASSESSMENT_001.md`
- `00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_ADMISSION_SEQUENCE_RECONCILIATION_DECISION_001.md`
- `00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_ADMISSION_CHAIN_RECONCILIATION_REVIEW_001.md`
- `00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_DATASET_IDENTIFIABILITY_AND_PRIVACY_ADMISSION_REVIEW_v0.1.md`

No dataset bytes were opened, downloaded, transformed, or reprocessed to prepare this proposal. No scientific code was executed. No current artifact was changed, and TGCV Core / Ω-primary status remain unchanged.
