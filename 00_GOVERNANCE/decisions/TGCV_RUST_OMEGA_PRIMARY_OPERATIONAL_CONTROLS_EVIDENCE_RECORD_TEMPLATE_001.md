# TGCV — Rust Ω-Primary Operational Controls Evidence Record Template 001

**Status:** TEMPLATE — UNFILLED / NO CONTROL VERIFIED / ADMISSION NOT GRANTED  
**Date created:** 2026-10-09  
**Branch:** `governance/rust-omega-raw-data-admission-firewall-audit-20261009`  
**Purpose:** collect minimal non-sensitive evidence needed for a prospective decision about the confirmed structural transformation-space/reachability research purpose.

## 1. Use and safety boundary

This is an evidence-collection template, not an attestation that controls exist. Leave fields as `UNKNOWN` unless there is direct evidence. Do not enter passwords, access tokens, private keys, personal account identifiers, exact sensitive storage paths, or other secrets in this public repository.

Completing this template does not grant data admission or authorize row-level inspection, transformation, scientific execution, or disclosure.

## 2. Artifact inventory

| Artifact | Current reference | Location class (do not expose sensitive path) | Publicly accessible? | Evidence reference | Status |
|---|---|---|---|---|---|
| Raw source ZIP | `rust_repos_2022_09_07.zip`; size and MD5 matched to Figshare metadata | UNKNOWN | UNKNOWN | UNKNOWN | OPEN |
| Existing U_t JSON | Canonical U_t hash recorded in governance; physical JSON hash separately recorded | UNKNOWN | UNKNOWN | UNKNOWN | OPEN |
| Restricted provenance / logs | Identify by artifact class only | UNKNOWN | UNKNOWN | UNKNOWN | OPEN |
| Backups / synced copies | Inventory existence without exposing paths | UNKNOWN | UNKNOWN | UNKNOWN | OPEN |

## 3. Access and storage controls

For each row, provide a non-sensitive evidence reference or leave UNKNOWN.

| Control | Evidence needed | Recorded state |
|---|---|---|
| Storage boundary | Local-only, encrypted managed storage, or other class; no exact path | UNKNOWN |
| Authorised access | Roles/groups allowed to read raw ZIP and U_t | UNKNOWN |
| Access restriction | OS permissions, repository visibility, or storage ACL evidence | UNKNOWN |
| Disk/device encryption | Enabled/disabled/unknown, with a non-sensitive verification reference | UNKNOWN |
| Cloud sync / external backup | Whether copies exist and their control boundary | UNKNOWN |
| Transfer to third parties | Whether any transfer occurred; if yes, separate approval record | UNKNOWN |
| Public exposure check | Evidence that raw ZIP and U_t are not in a public repository or public artifact store | UNKNOWN |

Do not conduct a new content inspection as part of filling this table. Use configuration evidence and already available records only.

## 4. Retention and accountability

| Decision item | Required value |
|---|---|
| Accountable role (role, not personal details) | UNKNOWN |
| Raw ZIP disposition | Choose: restricted research / audit-only / proposed deletion / UNKNOWN |
| Existing U_t disposition | Choose: restricted research / audit-only / proposed deletion / UNKNOWN |
| Review or deletion trigger/date | UNKNOWN |
| Backup retention/deletion treatment | UNKNOWN |
| Minimum audit evidence to preserve | UNKNOWN |
| External sharing | Proposed default: prohibited unless separately approved |
| Public row-level release | Proposed default: prohibited unless separately approved |

No deletion should occur solely by filling this template. Preserve historical integrity and audit requirements; any deletion requires a separate recorded decision.

## 5. Research scope and field necessity

Confirmed purpose under assessment: assess whether the existing U_t can support structural transformation-space and reachability analysis, with no causal/value claims and no inference of absence from `UNKNOWN_MISSING`.

| Question | Proposed default | Decision/evidence |
|---|---|---|
| Internal research only? | Yes, unless a separate scope is approved | UNKNOWN |
| External linkage/enrichment? | Prohibited for this proposed use | UNKNOWN |
| Need for stable structural endpoint IDs? | Needed in some stable form; source-ID linkability must be assessed | OPEN |
| Need for dependency row ordinal in analysis-facing data? | Not established; consider restricted provenance separation | OPEN |
| Need to repeat snapshot time and constant status fields on every record? | Not established; consider manifest-level representation in a future version | OPEN |
| Need to read `semver_str` value? | Not established for output selection; frozen code must not be silently changed | OPEN |
| Independent linkage/privacy review? | Decide based on residual risk and intended use | UNKNOWN |

## 6. Required sign-off

This section is completed only by the authorised decision-maker, after evidence review.

- Evidence package reviewed: UNKNOWN
- Residual linkage/privacy risk explicitly accepted or rejected: UNKNOWN
- Permitted use categories: UNKNOWN
- Prohibited use categories: UNKNOWN
- Exact artifact/hash covered by the decision: UNKNOWN
- Decision date and accountable role: UNKNOWN
- Separate execution authorization required for any new processing: YES
- Decision outcome: **NOT DECIDED**

## 7. Current gate state

Until this record is completed and reviewed in a separate prospective decision:

- Dataset admission: **NOT GRANTED**.
- Privacy/identifiability clearance: **NOT GRANTED**.
- Existing U_t empirical reuse: **BLOCKED**.
- Longitudinal absence/removal claims: **BLOCKED**.
- New processing or scientific execution: **NOT AUTHORIZED**.
- TGCV Core and Ω-primary canonical status: **UNCHANGED**.

## 8. Related records

- `00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_PROSPECTIVE_ADMISSION_GATE_READINESS_MATRIX_001.md`
- `00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_FIELD_NECESSITY_AND_MINIMISATION_REVIEW_001.md`
- `00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_PROPOSED_RESEARCH_PURPOSE_AND_USE_BOUNDARY_001.md`
- `00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_DATA_MINIMISATION_ACCESS_RETENTION_AND_REUSE_SCOPE_PROPOSAL_001.md`

No dataset bytes were opened, transformed, or processed. No scientific code was executed. This template records unknowns rather than inventing control evidence.
