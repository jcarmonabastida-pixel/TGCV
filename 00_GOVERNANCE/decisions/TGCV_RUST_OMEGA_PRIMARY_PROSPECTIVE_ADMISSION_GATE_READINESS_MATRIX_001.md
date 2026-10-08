# TGCV — Rust Ω-Primary Prospective Admission Gate Readiness Matrix 001

**Status:** OPEN — READINESS REVIEW ONLY / ADMISSION NOT GRANTED  
**Date:** 2026-10-09  
**Branch:** `governance/rust-omega-raw-data-admission-firewall-audit-20261009`  
**Scope:** Existing Rust 2022-09-07 source ZIP and historical U_t artifact

## 1. Purpose and rule

This matrix converts the existing admission criteria and field-level assessment into a decision-readiness register. It distinguishes evidence already documented from controls or conclusions that remain unverified. It is not a privacy certification, admission decision, or execution authorization.

**Gate result: NOT READY FOR EMPIRICAL REUSE APPROVAL.** The historical dataset-admission denial remains in force until a prospective decision explicitly resolves the open criteria. No evidence is promoted to PASS merely because the file identity or technical construction is reproducible.

## 2. Readiness matrix

| Criterion | Evidence currently documented | Readiness | Remaining action before any reuse approval |
|---|---|---|---|
| Exact source item and version | Figshare Full dataset item 21345990, version 1, file 37887018; DOI and source linkage recorded | **SUPPORTED** | Preserve item/version/file references in the prospective decision |
| Local file identity | Local size 6,047,715,996 bytes and MD5 match the published Figshare file metadata; previously recorded SHA-256 remains separately recorded | **MATCHED, WITH MD5 LIMITATION** | No repeat hash needed for this documentary gate; do not equate MD5 with collision-resistant proof |
| Dataset license metadata | Figshare item declares CC0 | **SUPPORTED AS PUBLISHED METADATA** | Confirm that this item-level declaration is the license basis intended for the proposed use; it does not clear privacy |
| Input member boundary | Historical runner declares two CSV members: package_versions.csv and package_dependencies.csv | **SUPPORTED FOR THAT CODE PATH** | Do not generalise to all archive members; confirm implementation revision against the historical execution closure |
| Input schemas | Four-column package_versions schema and three-column package_dependencies schema recorded | **DOCUMENTED** | Field inventory exists; retain schema provenance |
| Direct identifiers in the two schemas | No name, email, or login fields explicitly listed | **LIMITED OBSERVATION ONLY** | Do not conclude anonymity; assess linkability of identifiers, time and graph structure |
| U_t output fields | `tau`, `snapshot_time`, provenance strings including dependency row ordinal, coverage/resolution labels and construction metadata documented | **DOCUMENTED** | Justify necessity of each identifier, timestamp and provenance pointer for each intended use |
| Linkage/re-identification threat model | Plausible linkage to public package/version histories and dependency graphs identified conceptually | **OPEN** | Specify threat actor, auxiliary sources, feasible linkage paths and whether independent review is required |
| Input minimisation | `semver_str` is read/validated but not emitted; no necessity decision frozen | **OPEN** | Decide whether it is required for the frozen contract; any implementation change must be separately versioned and reviewed |
| Provenance minimisation | Row ordinal enables exact source-row traceability; research-facing necessity not established | **OPEN** | Decide whether to separate restricted provenance from any future analysis derivative |
| Temporal minimisation | Cutoff is copied into output; timestamp precision risk noted but not evaluated | **OPEN** | Justify required granularity against temporal rule and research purpose |
| Storage location and access controls | Proposal asks for restricted access and non-public storage; actual settings have not been verified | **OPEN — NO CONTROL EVIDENCE** | Provide a non-sensitive operational record of storage boundary, authorised roles and access mechanism |
| Disk encryption, backups and sync | Proposal identifies these as checks; no actual settings supplied in the canonical record | **OPEN — UNVERIFIED** | Verify relevant controls or explicitly record compensating controls and residual risk |
| Retention/deletion and owner | Proposed options recorded; no period/event, accountable role or backup deletion policy frozen | **OPEN — NO POLICY FROZEN** | Select retention outcome per artifact, review/deletion trigger, owner and backup handling |
| Intended and prohibited uses | Proposal distinguishes documentary review, structural derivation, longitudinal inference and external disclosure | **PROPOSED, NOT APPROVED** | Name the exact intended research question and expressly decide each requested use category |
| External sharing/publication | No permitted disclosure scope approved | **OPEN / BLOCKED** | Record no-sharing or define audience, fields, channel, risk review and approval |
| Historical admission before processing | 2026-10-01 reviews say NOT GRANTED; later technical preflight and U_t construction exist | **SEQUENCING DEVIATION ACKNOWLEDGED** | Preserve historical records; prospective approval cannot retroactively cure the deviation |
| U_t completeness semantics | 2,946,888 OBSERVED_PRESENT; 671,635 UNKNOWN_MISSING; zero OBSERVED_ABSENT_COMPLETE; complete_target_packages empty | **COVERAGE LIMITATION DOCUMENTED** | Keep absence/removal and longitudinal claims blocked without independent completeness evidence |
| Existing U_t empirical reuse | No prospective privacy/reuse approval exists | **BLOCKED** | Decision-maker must expressly approve or deny the exact artifact hash and narrow permitted purpose |
| New processing / scientific execution | No new execution authorization issued by this review | **NOT AUTHORIZED** | Requires separate prospective admission and explicit execution authorization |
| TGCV architecture / claim status | Existing records keep Core unchanged and Ω-primary proposed/non-canonical | **UNCHANGED** | No upgrade based on this governance review |

## 3. Decision rule

The matrix is **not ready** for an empirical-reuse approval because linkage risk, minimisation necessity, operational access controls, retention, and exact purpose remain OPEN or merely PROPOSED.

The next gate must choose one of these bounded outcomes:

- **Audit-only retention:** retain raw ZIP and U_t as restricted historical evidence; no scientific reuse.
- **Restricted prospective reuse:** only after the OPEN controls are evidenced and the decision names the exact artifact, fields, research purpose, operator/access boundary, retention and output restrictions.
- **Reject / securely dispose:** if the required controls cannot be established, document the decision and preserve only the audit evidence that must remain.

No option is selected by this matrix. Unless and until a prospective decision is recorded, the effective state remains audit/documentary review only, no row-level inspection for scientific purposes, no structural derivation, no longitudinal claims, no external disclosure, and no new processing.

## 4. Required evidence package for the next gate

To turn OPEN entries into decision-grade evidence, provide only the minimum non-sensitive information needed:

1. Exact intended TGCV research question and requested use category.
2. Whether raw ZIP and U_t remain outside public repositories and the storage/access controls in force; do not include secrets or sensitive account details.
3. Proposed retention/review trigger and accountable role.
4. Whether U_t is intended for internal analysis only, collaborator sharing, or public release.
5. A field-by-field necessity decision for numeric IDs, timestamps, `tau`, and provenance row ordinal.
6. Whether an independent privacy/re-identification review is available or required.

If any item remains unknown, keep the corresponding use blocked. Do not inspect dataset rows, alter artifacts, or run scientific code to complete this documentary readiness matrix.

## 5. Related records

- `00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_FIELD_LEVEL_PRIVACY_AND_REUSE_ASSESSMENT_001.md`
- `00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_DATA_MINIMISATION_ACCESS_RETENTION_AND_REUSE_SCOPE_PROPOSAL_001.md`
- `00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_ADMISSION_SEQUENCE_RECONCILIATION_DECISION_001.md`
- `00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_DATASET_IDENTIFIABILITY_AND_PRIVACY_ADMISSION_REVIEW_v0.1.md`
- `00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_DATASET_ADMISSION_PACKAGE_REVIEW_v0.1.md`
- `00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_DATASET_SNAPSHOT_MANIFEST_AND_PROVENANCE_REVIEW_v0.1.md`

No dataset bytes were accessed or processed. No scientific code was executed. No existing artifact was modified. This matrix does not change TGCV Core, Ω-primary status, the historical admission decision, or the acknowledged sequencing deviation.


## 6. Confirmed purpose boundary — 2026-10-09

The proposed research purpose is now confirmed for admission assessment only in:

`00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_PROPOSED_RESEARCH_PURPOSE_AND_USE_BOUNDARY_001.md`

Purpose: assess whether existing U_t can support structural transformation-space and reachability analysis, without causal/value claims and without interpreting `UNKNOWN_MISSING` as absence. This resolves the purpose-definition question for the next review; it does not resolve linkage risk, minimisation, operational controls, retention, or admission. The gate remains **NOT READY FOR EMPIRICAL REUSE APPROVAL**.


## 7. Field necessity review — 2026-10-09

The source-level field necessity and minimisation review is recorded at:

`00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_FIELD_NECESSITY_AND_MINIMISATION_REVIEW_001.md`

It identifies `semver_str` access, repeated artifact constants, duplicate provenance references, and the dependency row ordinal as candidates for a future versioned minimisation design. No change is made to the frozen runner or U_t. Linkage risk and operational controls remain OPEN; empirical reuse remains blocked.
