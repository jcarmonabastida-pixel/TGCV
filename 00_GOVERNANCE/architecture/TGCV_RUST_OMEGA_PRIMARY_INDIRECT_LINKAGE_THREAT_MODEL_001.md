# TGCV — Rust Ω-Primary Indirect Linkage Threat Model 001

**Status:** PRELIMINARY DOCUMENTARY THREAT MODEL — PRIVACY CLEARANCE NOT GRANTED / EMPIRICAL REUSE BLOCKED  
**Date:** 2026-10-09  
**Branch:** `governance/rust-omega-raw-data-admission-firewall-audit-20261009`  
**Scope:** Existing Rust 2022-09-07 source dataset and historically constructed U_t artifact  
**Review type:** Documentary assessment only; no dataset-byte access, row inspection, linkage test, or scientific execution

## 1. Purpose and decision boundary

This document records plausible indirect-linkage threats relevant to the existing Rust Ω-Primary U_t artifact. It converts the field inventory and existing governance decisions into a bounded threat model. It is not a formal re-identification study, a legal opinion, an independent privacy review, or a finding that any person has been identified.

**Current decision:** the existing U_t artifact is retained in its current location for audit and documentary traceability only. Structural scientific reuse, additional processing, longitudinal claims, and external disclosure remain blocked pending a separate prospective decision. The historical admission sequencing deviation remains acknowledged and is not retroactively cured.

No dataset bytes were opened, parsed, downloaded, transformed, or reprocessed to prepare this document. No scientific code was executed.

## 2. Assets and processing boundary

The in-scope assets are:
- the source Rust repository dataset archive identified in the existing admission-chain records;
- the existing U_t JSON artifact, whose recorded physical SHA-256 is `6d2f3066346c70068e6d044fa5575ff5a84572f74ca1ada06d5d3b49239810ab`;
- the existing schema, constructor, execution-closure, provenance, and governance records.

The documented runner's input boundary names two CSV members:
- `package_versions.csv`, with documented fields `id`, `package_id`, `version_str`, `created_at`;
- `package_dependencies.csv`, with documented fields `depending_version`, `depending_on_package`, `semver_str`.

The documented U_t output includes numeric identifiers in `tau`, `snapshot_time`, provenance strings including a dependency-row ordinal, coverage/resolution labels, and construction metadata. This description comes from existing source/governance records; it is not a new inspection of the retained artifact.

The threat model is limited to these documented fields and their combinations. It does not claim that the whole source archive has been privacy-audited.

## 3. Threat actors and auxiliary information

Plausible actor classes, considered as hypotheses rather than observed activity:

1. **Public-data analyst:** has access to public Rust package/version records and dependency metadata.
2. **Dataset holder or recipient with source access:** can compare a derived record against the corresponding source snapshot or a copy of it.
3. **External researcher or collaborator:** has independently collected package release timelines, version identifiers, or dependency graphs.
4. **Unintended recipient of a disclosed derivative:** can combine disclosed rows with public ecosystem information.

Potential auxiliary sources include public package registries, public version histories, dependency listings, archived copies of the same dataset, and independently collected ecosystem snapshots. No such sources were queried or compared for this assessment. No claim is made that a particular actor has attempted or can successfully perform linkage.

## 4. Plausible linkage paths

| Vector | Plausible linkage mechanism | Current evidence | Status |
|---|---|---|---|
| Numeric version/package IDs | Match stable identifiers against a source snapshot or public registry metadata | Identifiers are documented in the input/output path; no matching exercise performed | PLAUSIBLE / UNTESTED |
| Version labels and timestamps | Correlate a release label or timestamp with public release history | `version_str` and `created_at` are documented source fields; exact uniqueness and temporal granularity have not been tested | PLAUSIBLE / UNTESTED |
| Dependency graph structure | Use a combination of dependency edges as a structural fingerprint for a package/version or ecosystem state | U_t represents dependency structure; no graph-matching or re-identification test performed | PLAUSIBLE / UNTESTED |
| Dependency-row ordinal | Use the recorded source-row position to locate a row in a matching copy of the raw CSV | The ordinal is documented as part of provenance; necessity for any future research derivative is not established | LINKAGE CAPABILITY DOCUMENTED / RISK NOT QUANTIFIED |
| Combined identifiers, time, graph and provenance | Combine several weak or quasi-identifying signals to narrow a match | Combination risk is a reasoned threat hypothesis; no empirical test performed | PLAUSIBLE / UNTESTED |
| Other archive members | Direct or indirect identifiers may exist outside the two CSV members declared by the runner | Runner boundary is documented, but archive-wide privacy assessment is absent | OUT OF SCOPE FOR THIS FIELD REVIEW / UNKNOWN |

The table describes possible mechanisms, not proof of successful re-identification. No probabilities, risk scores, uniqueness rates, or affected-person counts are estimated.

## 5. Direct identifiers, pseudonymity and anonymity

The two documented input schemas do not explicitly list names, email addresses, or login fields. This limited observation does not establish anonymity. Numeric identifiers, temporal metadata, structural relationships, and row-level provenance may remain linkable to external or source data.

The publisher-described pseudonymisation process and the dataset item's published CC0 license metadata do not independently resolve the specific linkage risks of the retained fields or authorise all TGCV reuse categories. License metadata and privacy clearance are separate questions.

Accordingly:
- **Direct identifiers in the two documented schemas:** none explicitly listed.
- **Potentially linkable fields and combinations:** identified conceptually.
- **Successful re-identification:** not demonstrated.
- **Anonymity:** not established.
- **Privacy/identifiability clearance:** NOT GRANTED.

## 6. Mitigations and unresolved choices

The following are candidate controls for a future prospective decision; this document does not implement them or authorise changes to the frozen artifact:

1. Keep the source archive and existing U_t non-public and access-restricted.
2. Do not distribute row-level U_t or source-row provenance externally without a separate risk review and explicit approval.
3. Decide field by field whether numeric identifiers, timestamps, and row ordinals are required for the specific approved purpose.
4. Consider separating audit-only provenance from any future research derivative, if a future derivative is explicitly approved and separately versioned.
5. Document the storage/access boundary, backup or synchronisation paths, retention, accountability, and permitted recipients.
6. Require a separate decision before any linkage test, structural derivation, new transformation, or scientific run.

These are proposals and boundaries, not evidence that technical controls have been verified. No independent privacy/re-identification reviewer is currently available, according to the user's response. The lack of an independent reviewer is recorded as a limitation, not as proof that review is unnecessary.

## 7. Current access and use decision

The separate retention decision records the user's choice to keep the existing JSON at its current location solely for documentary provenance, audit, integrity reference, and reproducibility review. Additional copies remain UNKNOWN; the user reports no backup tool configured in Ubuntu/WSL, but this does not rule out other copies, snapshots, sync, or transfer paths.

Permitted under the existing retention decision:
- preserve the artifact in place;
- cite the recorded file identity/hash in governance records;
- review existing provenance and execution records without reading or processing the artifact's data bytes.

Not authorised:
- scientific inspection of rows or content;
- structural transformation-space or reachability analysis;
- new derivations, fixtures, or U_t rebuilds;
- new downloads or transformations;
- longitudinal absence/removal claims;
- external disclosure or public release.

Any change to this boundary requires a separate prospective decision and, where applicable, explicit execution authorization.

## 8. Limitations and next gate

This is a documentary threat model based on existing field and execution records. It does not include:
- a test against live or archived public registries;
- an empirical uniqueness or graph-matching study;
- a formal attacker-capability assessment;
- independent legal/privacy review;
- a complete local access, backup, synchronisation, or copy audit;
- an archive-wide inspection of all dataset members.

The next governance gate may decide whether the documentary risk description is sufficient for audit-only retention, or whether an independent review or other evidence would be required before considering any prospective reuse. Until a separate decision says otherwise, empirical reuse remains blocked.

## 9. Related records

- `00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_FIELD_LEVEL_PRIVACY_AND_REUSE_ASSESSMENT_001.md`
- `00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_FIELD_NECESSITY_AND_MINIMISATION_REVIEW_001.md`
- `00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_EXISTING_U_ARTIFACT_RETENTION_DECISION_001.md`
- `00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_PROSPECTIVE_ADMISSION_GATE_READINESS_MATRIX_001.md`
- `00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_ADMISSION_SEQUENCE_RECONCILIATION_DECISION_001.md`

This document records governance reasoning only. It does not change TGCV Core, Ω-primary canonical status, the historical admission decision, the recorded sequencing deviation, or the existing U_t artifact.
