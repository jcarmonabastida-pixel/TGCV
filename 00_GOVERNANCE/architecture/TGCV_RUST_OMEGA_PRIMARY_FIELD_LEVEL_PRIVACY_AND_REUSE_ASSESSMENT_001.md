# TGCV — Rust Ω-Primary Field-Level Privacy and Reuse Assessment 001

**Status:** OPEN — FIELD INVENTORY PREPARED / PRIVACY CLEARANCE NOT GRANTED / REUSE BLOCKED  
**Date:** 2026-10-09  
**Assessment type:** Documentary governance assessment; no dataset-byte access or scientific execution  
**Snapshot:** Rust repositories dataset, 2022-09-07; Figshare Full dataset, item 21345990, version 1, file 37887018  
**Branch:** `governance/rust-omega-raw-data-admission-firewall-audit-20261009`

## 1. Purpose and decision boundary

This assessment advances the admission remediation by mapping the fields and derived identifiers documented in the existing processing path to their semantic role, potential identifiability risk, minimisation status, and evidence gaps.

It is not an independent legal opinion, a formal re-identification study, or proof that the dataset is anonymous. It does not inspect the retained ZIP or the 1.08 GB U_t result. The assessment is based on the canonical schemas, constructor/runner source, execution closure, publication description, and Figshare item metadata already recorded in the repository.

**Decision at this stage: PRIVACY / IDENTIFIABILITY CLEARANCE NOT GRANTED. EXISTING U_t EMPIRICAL REUSE REMAINS BLOCKED.**

## 2. Processing boundary established by source records

The existing runner declares that it reads only these two members from the retained archive:

- `rust_repos_2022_09_07/dumps/postgresql/data/package_versions.csv`
- `rust_repos_2022_09_07/dumps/postgresql/data/package_dependencies.csv`

The recorded schemas are:

- `package_versions(id, package_id, version_str, created_at)`
- `package_dependencies(depending_version, depending_on_package, semver_str)`

The constructor uses version/package identifiers, version timestamps, and dependency source/target references to resolve candidate structural triples. It validates/coerces `semver_str` but does not include its value in the emitted U_t record. The emitted records include `tau` (three numeric identifiers), `snapshot_time` (the frozen cutoff), three provenance strings (including the dependency row ordinal), `coverage_state`, `resolution_status`, `construction_version`, and `temporal_rule`.

The current execution closure reports 2,946,888 `OBSERVED_PRESENT` records and 671,635 `UNKNOWN_MISSING` entries; it reports zero `OBSERVED_ABSENT_COMPLETE` and an empty `complete_target_packages` set. This missingness classification is a coverage constraint, not a privacy result.

## 3. Field-level inventory and preliminary risk classification

| Field / artifact | Role in current path | Preliminary identifiability consideration | Evidence status |
|---|---|---|---|
| `package_versions.id` | Numeric version-record identifier; appears in U_t source/target identifiers and provenance | Not a direct personal identifier by itself in the documented schema, but enables linkage within the source corpus and potentially with external versions of the dataset | Purpose documented; external-linkage risk not assessed |
| `package_versions.package_id` | Numeric package identity; used for dependency target resolution and appears as U_t target package ID | Stable ecosystem identifiers can support linkage to public package/release records; no package names are shown in the retained schema, but identifiers may be resolvable through external data | Linkability plausible; no empirical linkage test performed |
| `package_versions.version_str` | Release/version label used in deterministic tie-breaking; not emitted directly in U_t | May be public metadata; exact uniqueness/linkage properties not assessed | No privacy test |
| `package_versions.created_at` | Temporal ordering and cutoff; cutoff is emitted as `snapshot_time` | Fine-grained timestamps can support linkage or inference when combined with public release histories; temporal granularity is preserved in source records | No granularity/minimisation analysis |
| `package_dependencies.depending_version` | Source version reference used to construct `tau` | Referential identifier; may link to public release history | Linkability plausible; no external linkage test |
| `package_dependencies.depending_on_package` | Dependency target package identifier used to resolve target versions and emitted in `tau` | Structural relations can fingerprint package ecosystems or releases when combined with public dependency graphs | No graph re-identification test |
| `package_dependencies.semver_str` | Read/validated by constructor but not used in emitted U_t records | Its value is not emitted in the current U_t schema; input-read scope should still be documented and minimised if not required | Output omission supported by code; input-level necessity not independently tested |
| Dependency row ordinal (`package_dependencies.csv:row:n`) | Provenance pointer included in U_t records | Reveals source row position and can make records linkable to the exact raw file; may be unnecessary if a stable provenance key exists | Retention necessity not assessed |
| U_t `tau` tuple | Canonical structural triple of numeric IDs | Pseudonymous/linkable rather than proven anonymous; external data may map IDs to public packages and releases | Reuse risk open |
| U_t `snapshot_time` | Frozen maximum `created_at` cutoff copied to each record | Exposes snapshot cutoff; likely low incremental risk alone, but combines with structural identifiers | Minimisation not assessed |
| U_t provenance strings | Source IDs, dependency row ordinal, target IDs | High internal traceability and external linkability to the raw snapshot | Necessary for auditability is plausible; least-privilege access/retention unspecified |
| Full source ZIP | Two CSV members consumed by the documented runner; archive contains other members not admitted by this runner | The two schemas do not prove absence of personal data elsewhere in the full archive | Runner boundary documented; archive-wide privacy assessment not performed |
| U_t JSON result | Derived artifact with numeric IDs, row pointers, temporal and structural information | Not shown to contain direct names or login/email fields, but remains linkable and must not be described as anonymous without further evidence | Physical result exists historically; access and retention controls not documented here |

## 4. Published pseudonymisation statement — limited relevance

The associated data descriptor describes a pseudonymisation process involving discarding name attributes and hashing email addresses and GitHub/GitLab logins with MD5 and a random salt. This is publisher-described process information, not an independent assessment of the exact two CSV members or the emitted U_t artifact.

The documented schemas for the two members consumed by the TGCV runner do not list names, emails, or login fields. That does **not** prove that all other archive members are free of such fields, that numeric identifiers cannot be linked to people, or that structural/timestamp combinations cannot support inference. No direct re-identification test has been performed for this assessment.

The Figshare item-level CC0 declaration supports the recorded license metadata. A public-domain license does not by itself establish privacy clearance, eliminate third-party rights concerns, or authorise every proposed reuse under TGCV governance.

## 5. Data minimisation and purpose limitation

The current code's output is narrower than the full archive: it emits structural triples and provenance rather than names or login/email fields. However, the following controls are not yet evidenced as frozen:

1. A field-level justification for retaining each identifier and the dependency row ordinal in the derived artifact.
2. A decision on whether `semver_str` must be read at all, given that its value is not used in the emitted record.
3. Whether provenance can be represented by a stable minimal reference without retaining row ordinals.
4. Access restrictions for the retained ZIP and U_t JSON artifact.
5. Retention period and deletion/archival policy for raw and derived artifacts.
6. Whether any public release, publication supplement, or external sharing of U_t is intended.
7. A documented threat model for linkage to public crates.io/package histories and dependency graphs.

No fields are removed and no artifact is altered by this documentary assessment.

## 6. Reuse categories requiring explicit distinction

Any future decision must not treat all uses as equivalent:

- **Governance/provenance audit:** checking hashes, schema descriptions, execution records, and historical closure documents without reading dataset content.
- **Technical artifact integrity review:** validating the existing U_t file and its recorded canonical hash, subject to approved access controls.
- **Structural research reuse:** using U_t as input to derive further Ω-related objects or statistics.
- **Longitudinal empirical claims:** interpreting differences across snapshots, including absence/removal, coverage change, or trajectories.
- **External disclosure:** sharing raw or derived data with collaborators, publishing U_t, or providing row-level output.

This document does not authorise any of these uses beyond documentary governance review. Technical reproducibility does not automatically imply privacy clearance or research-use admission.

## 7. Decision and blocking conditions

The available evidence is insufficient to conclude that the exact retained fields and the U_t output are adequately minimised and non-identifying for all intended TGCV uses. The safe, evidence-grounded decision is therefore:

- **Direct identifiers in the two documented input schemas:** none are explicitly listed.
- **Potentially linkable/quasi-identifying fields:** numeric package/version IDs, release timestamps, dependency structure, row-level provenance.
- **Privacy/identifiability clearance:** **OPEN — NOT GRANTED**.
- **Existing U_t reuse for structural scientific derivation:** **BLOCKED pending prospective approval**.
- **Longitudinal absence/removal claims:** **BLOCKED**; `UNKNOWN_MISSING` is not absence.
- **New download, data transformation, U_t reconstruction, fixture creation, or scientific execution:** **NOT AUTHORISED** by this assessment.
- **TGCV Core / Ω-primary status:** unchanged; Ω-primary remains proposed and non-canonical.

## 8. Evidence required to reconsider

A prospective gate must resolve the following without assuming that the publisher's pseudonymisation statement is sufficient:

1. Confirm the exact processing and output field inventory against the frozen implementation and existing closure.
2. Document the public-linkage threat model for numeric IDs, release timestamps, and dependency graph structure.
3. Decide whether row-level provenance ordinals and other identifiers are necessary, and specify a minimisation rule for any future permitted artifact.
4. Freeze access controls, retention/deletion, and external-sharing restrictions for the raw ZIP and existing U_t result.
5. Specify the precise intended use(s) to be approved and prohibited uses.
6. Obtain any needed independent privacy/legal review if the risk assessment cannot be resolved from the documented evidence.
7. Make an explicit prospective decision on whether the already-produced U_t artifact can be reused, for what purpose, and under what restrictions.
8. Keep the sequencing deviation acknowledged; no later approval retroactively changes the fact that processing preceded a documented admission decision.

Incomplete evidence keeps the relevant reuse category blocked.

## 9. Source records

- `00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_DATASET_IDENTIFIABILITY_AND_PRIVACY_ADMISSION_REVIEW_v0.1.md`
- `00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_DATASET_ADMISSION_PACKAGE_REVIEW_v0.1.md`
- `00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_DATASET_SNAPSHOT_MANIFEST_AND_PROVENANCE_REVIEW_v0.1.md`
- `00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_U_REAL_DATA_CONSTRUCTION_EXECUTION_CLOSURE_001.md`
- `00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_ADMISSION_CHAIN_RECONCILIATION_REVIEW_001.md`
- `07_CODE/src/omega_u_constructor_v01.py`
- `07_CODE/src/rust_omega_u_real_data_execution_v01.py`

This is a documentary field-level assessment. No dataset bytes were opened, downloaded, transformed, or reprocessed; no scientific code was executed; no existing artifact was modified.
