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
| Retention/deletion and owner | Existing U_t JSON has a separate recorded decision for audit-only retention in its current location, six-month/triggered review, and no automatic deletion; raw ZIP and other copies/backup handling remain unresolved | **PARTIALLY DECIDED — U_t ONLY; OPERATIONAL GAPS OPEN** | Preserve the existing U_t decision; separately resolve raw ZIP retention, copies/backups, accountable role, and any verified deletion/backup-handling procedure before changing use or storage |
| Intended and prohibited uses | Proposal distinguishes documentary review, structural derivation, longitudinal inference and external disclosure | **PROPOSED, NOT APPROVED** | Name the exact intended research question and expressly decide each requested use category |
| External sharing/publication | No permitted disclosure scope approved | **OPEN / BLOCKED** | Record no-sharing or define audience, fields, channel, risk review and approval |
| Historical admission before processing | 2026-10-01 reviews say NOT GRANTED; later technical preflight and U_t construction exist | **SEQUENCING DEVIATION ACKNOWLEDGED** | Preserve historical records; prospective approval cannot retroactively cure the deviation |
| U_t completeness semantics | 2,946,888 OBSERVED_PRESENT; 671,635 UNKNOWN_MISSING; zero OBSERVED_ABSENT_COMPLETE; complete_target_packages empty | **COVERAGE LIMITATION DOCUMENTED** | Keep absence/removal and longitudinal claims blocked without independent completeness evidence |
| Existing U_t empirical reuse | No prospective privacy/reuse approval exists | **BLOCKED** | Decision-maker must expressly approve or deny the exact artifact hash and narrow permitted purpose |
| New processing / scientific execution | No new execution authorization issued by this review | **NOT AUTHORIZED** | Requires separate prospective admission and explicit execution authorization |
| TGCV architecture / claim status | Existing records keep Core unchanged and Ω-primary proposed/non-canonical | **UNCHANGED** | No upgrade based on this governance review |

## 3. Decision rule

The matrix is **not ready** for an empirical-reuse approval because linkage risk, minimisation necessity, and operational access controls remain OPEN; the exact research purpose is defined only as a proposal and is not approved; and retention is decided only for the existing U_t JSON (audit-only, current location), while raw-ZIP retention, unknown copies/backups, and cross-artifact operational handling remain OPEN.

The next gate must choose one of these bounded outcomes:

- **Existing U_t retention:** audit-only in its current location under the separate recorded retention decision; no scientific reuse. **Raw ZIP retention and the handling of unknown copies/backups remain unresolved** and require a separate decision.
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


## 8. Operational controls evidence template — 2026-10-09

A non-sensitive evidence collection template is recorded at:

`00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_OPERATIONAL_CONTROLS_EVIDENCE_RECORD_TEMPLATE_001.md`

It records artifact classes, access/storage controls, backup/synchronisation, retention/accountability, research scope and decision sign-off. All currently unverified values remain `UNKNOWN`; the template does not attest that controls exist and does not grant admission or execution authorization.


## 9. Bounded public-repository exposure check — 2026-10-09

The result is recorded at:

`00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_PUBLIC_REPOSITORY_EXPOSURE_CHECK_001.md`

The repository is public. A bounded path-name search of the reviewed branch tree did not find the raw source ZIP or an obvious full real-data U_t JSON path. This is not a content/history scan and does not verify local storage, permissions, encryption, backups, or retention. All those items remain UNKNOWN; the admission gate remains blocked.


## 10. Local controls verification procedure — 2026-10-09

The read-only, privacy-conscious local verification procedure is recorded at:

`00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_LOCAL_CONTROLS_VERIFICATION_PROCEDURE_001.md`

It provides local PowerShell checks for artifact existence/metadata, an initial ACL inventory, and system-drive encryption, plus a manual process for sync/backup and retention. It has **not** been executed on the user's machine. No local-control result is claimed; these criteria remain OPEN until sanitised evidence is supplied and reviewed.

## 11. Existing U_t artifact retention decision — 2026-10-09

The user has explicitly selected **audit-only retention in the current location** for the existing JSON artifact. The decision is recorded in:

`00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_EXISTING_U_ARTIFACT_RETENTION_DECISION_001.md`

This closes the user's choice of retention outcome for the existing U_t artifact, but it does not establish a complete local-storage audit or resolve the admission gate. Additional copies remain **UNKNOWN**; the user reports no backup tool configured in Ubuntu/WSL, but this is not an independent audit and does not rule out other copy/sync paths. The user's current sole use of the computer is recorded as a declaration; no inference is made about historical access.

For the existing U_t artifact:
- Retention choice: **DECIDED — AUDIT/DOCUMENTARY REVIEW ONLY**.
- Existing artifact physical SHA-256: recorded in the retention decision from the user's prior local output; not recalculated.
- Retention review: every six months and on change of purpose, storage location, or access conditions.
- Automatic deletion: **NOT AUTHORIZED**; deletion requires a separate explicit decision.
- Scientific inspection, structural derivation, longitudinal claims, external disclosure, and new processing: **BLOCKED** pending a separate prospective decision and any required execution authorization.

This decision does not retroactively cure the acknowledged sequencing deviation, grant privacy clearance, or change Core / Ω-primary status.


## 12. Indirect-linkage threat model — 2026-10-09

A preliminary documentary threat model has been recorded at:

`00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_INDIRECT_LINKAGE_THREAT_MODEL_001.md`

It identifies plausible, untested linkage paths through numeric package/version identifiers, release timestamps, dependency graph structure, dependency-row ordinals, and combinations of these fields. It does not claim successful re-identification, estimate probabilities, or establish anonymity. No public registry was queried and no dataset rows or JSON content were inspected.

Independent privacy/re-identification review is currently unavailable, as reported by the user. This is recorded as a limitation; it does not establish that independent review is unnecessary. The threat model is documentary and preliminary. Privacy/identifiability clearance remains **NOT GRANTED**, and empirical reuse, further processing, and external disclosure remain **BLOCKED**. The existing U_t artifact remains retained only for audit/documentary traceability under the separate retention decision.

## 13. Documentary governance phase closure — 2026-10-09

The bounded documentary governance phase is recorded as **CLOSED WITH RESTRICTIONS** in:

`00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_DOCUMENTARY_GOVERNANCE_PHASE_CLOSURE_DECISION_001.md`

This is a closure of the documentary review work possible with the evidence currently available, **not** a grant of scientific admission and not a finding that the source data or U_t are anonymous or safe for reuse. The gate result above therefore remains **NOT READY FOR EMPIRICAL REUSE APPROVAL**. Privacy/identifiability clearance remains **NOT GRANTED**; scientific inspection, structural reuse, further processing, new scientific execution, and external disclosure remain blocked or unauthorised under the existing retention decision.

The closure does not retroactively cure the historical admission-sequencing deviation, change TGCV Core, or promote Ω-primary to canonical status. Reopening requires a separate prospective decision if the proposed use, storage/access conditions, retention boundary, external sharing, or material evidence changes.

