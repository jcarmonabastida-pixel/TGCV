# TGCV — Rust Ω-Primary Field Necessity and Minimisation Review 001

**Status:** DOCUMENTARY REVIEW COMPLETE FOR CURRENT SCHEMA / MINIMISATION DECISIONS OPEN / EMPIRICAL REUSE BLOCKED  
**Date:** 2026-10-09  
**Branch:** `governance/rust-omega-raw-data-admission-firewall-audit-20261009`  
**Purpose:** assess whether existing U_t supports structural transformation-space and reachability analysis, without causal/value claims and without treating `UNKNOWN_MISSING` as absence.

## 1. Boundary

This review assesses the functional role of input and output fields using the frozen constructor/runner source and existing governance records. No dataset bytes were opened and no scientific execution was performed. This is not privacy clearance, admission, or execution authorization.

It distinguishes functional necessity in the current contract from record-level repetition, audit provenance, and potential linkability. No field is removed and no artifact is modified.

## 2. Input-field review

Reviewed schemas:
- `package_versions(id, package_id, version_str, created_at)`
- `package_dependencies(depending_version, depending_on_package, semver_str)`

| Field | Current source-code role | Assessment for confirmed purpose |
|---|---|---|
| `package_versions.id` | Resolves source version and forms part of `tau` and provenance | Necessary for current stable endpoint identity; potentially linkable |
| `package_versions.package_id` | Groups versions, resolves target package, forms part of `tau` | Necessary for current target selection/identity; potentially linkable |
| `package_versions.version_str` | Deterministic tie-breaker after timestamp and ID; stored in index | Not emitted, but affects target selection; cannot be removed without a reviewed equivalent rule |
| `package_versions.created_at` | Source/target temporal ordering and cutoff | Necessary for the frozen temporal rule; timestamp precision minimisation remains open |
| `package_dependencies.depending_version` | Source endpoint reference | Necessary for current structural relation; potentially linkable |
| `package_dependencies.depending_on_package` | Target package resolution and `tau` | Necessary for current target relation; potentially linkable |
| `package_dependencies.semver_str` | Read and converted to string; value not used in selection or emitted | Candidate for omission in a future version, subject to schema-validation review; do not change frozen runner silently |

## 3. U_t output-field review

| Output field | Current role | Minimisation finding |
|---|---|---|
| `tau` | Structural triple: origin version, target package, target version | A stable representation of all three roles is required for the proposed structural question. Source numeric IDs are not proven to be the only possible representation |
| `snapshot_time` | Same frozen cutoff repeated on every emitted record | Semantically relevant, but may be represented once in an immutable artifact manifest in a future schema |
| `provenance[0]` source version reference | Audit traceability; overlaps with first `tau` component | Assess whether duplication in each analysis record is needed |
| `provenance[1]` dependency row ordinal | Exact source-row traceability | Strong minimisation candidate for a research-facing derivative; consider retaining only in restricted provenance |
| `provenance[2]` target version reference | Audit traceability; overlaps with third `tau` component | Assess whether duplication in each analysis record is needed |
| `coverage_state` | Every emitted record is marked `OBSERVED_PRESENT` | Constant in emitted positive records; candidate for schema/manifest declaration, but do not drop separate coverage counters |
| `resolution_status` | Every emitted record is marked `RESOLVED` | Constant in emitted positive records; candidate for schema/manifest declaration |
| `construction_version` | Constructor identity | Constant per artifact; candidate for manifest metadata |
| `temporal_rule` | Temporal-rule identity | Constant per artifact; candidate for manifest metadata |

These are future schema candidates, not changes to the canonical artifact. Relocating or removing record fields changes the schema and canonical U_t hash; it requires a new versioned contract, validation, and explicit governance approval.

## 4. Artifact-level semantics that must be preserved

The result includes `u_count`, `unresolved_count`, `coverage_counts`, `coverage_states`, `construction_version`, `temporal_rule`, `cutoff`, and `output_sha256`. The runner also records snapshot and execution metadata.

The coverage distinction among `OBSERVED_PRESENT`, `OBSERVED_ABSENT_COMPLETE`, `UNKNOWN_MISSING`, and `OUT_OF_SCOPE` must survive any future minimisation. Historical closure reports 2,946,888 `OBSERVED_PRESENT`, 671,635 `UNKNOWN_MISSING`, zero `OBSERVED_ABSENT_COMPLETE`, and an empty `complete_target_packages`. Unknown cannot be recoded as absence.

The canonical U_t hash identifies the canonical record sequence; the physical JSON hash identifies the complete JSON bytes. They are not interchangeable.

## 5. Proposed future field policy

1. Preserve the three semantic roles in `tau`, while evaluating internal stable identifiers as a future privacy measure.
2. Preserve the exact temporal rule and cutoff in a canonical manifest; do not coarsen timestamps without a separate semantic-impact review.
3. Assess separating dependency row ordinal and duplicate source/target references into a restricted provenance map.
4. Assess moving repeated snapshot time, coverage/resolution defaults, constructor version, and temporal rule to artifact-level metadata.
5. Preserve `version_str` for the frozen contract because it affects deterministic ordering.
6. Review whether `semver_str` needs to be read by a future version.
7. Preserve coverage and missingness semantics.
8. No public row-level release without explicit disclosure review.

## 6. Unresolved decision evidence

This source-level review cannot determine actual re-identification likelihood or verify operational controls. Still open are: threat actor and auxiliary sources; actual storage/access controls; encryption, backup and sync handling; accountable role; raw-ZIP and unknown-copy retention; verified backup/deletion handling; independent privacy review; and sharing restrictions. The existing U_t JSON already has a separate audit-only retention decision for its current location, with six-month and change-triggered review and no automatic deletion. That decision does not authorise structural reuse or a minimised derivative; either would require a separate prospective decision.

## 7. Outcome

- Field roles: **DOCUMENTED AT SOURCE LEVEL**.
- Minimisation candidates: **IDENTIFIED, NOT IMPLEMENTED**.
- Linkage risk: **OPEN; NO EMPIRICAL LINKAGE TEST**.
- Actual access/storage/retention controls: **OPEN; NOT VERIFIED**.
- Existing U_t structural reuse: **BLOCKED PENDING PROSPECTIVE DECISION**.
- Longitudinal/absence claims: **BLOCKED**.
- New processing/scientific execution: **NOT AUTHORISED**.
- TGCV Core and Ω-primary status: **UNCHANGED**.

## 8. Related records

- `00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_PROPOSED_RESEARCH_PURPOSE_AND_USE_BOUNDARY_001.md`
- `00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_FIELD_LEVEL_PRIVACY_AND_REUSE_ASSESSMENT_001.md`
- `00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_PROSPECTIVE_ADMISSION_GATE_READINESS_MATRIX_001.md`
- `00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_DATA_MINIMISATION_ACCESS_RETENTION_AND_REUSE_SCOPE_PROPOSAL_001.md`
- `07_CODE/src/omega_u_constructor_v01.py`
- `07_CODE/src/rust_omega_u_real_data_execution_v01.py`

No dataset bytes were accessed. No scientific code or existing artifact was changed. This review does not authorize a rebuild, data transformation, or empirical analysis.


## 9. Operational evidence follow-up — 2026-10-09

The non-sensitive operational controls evidence template is linked at:

`00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_OPERATIONAL_CONTROLS_EVIDENCE_RECORD_TEMPLATE_001.md`

This addresses the documentary gap by specifying the evidence to collect, not by claiming controls are active. Storage/access, encryption, backup/sync, retention and accountable role remain UNKNOWN until verified. No data use is authorised by the template.
