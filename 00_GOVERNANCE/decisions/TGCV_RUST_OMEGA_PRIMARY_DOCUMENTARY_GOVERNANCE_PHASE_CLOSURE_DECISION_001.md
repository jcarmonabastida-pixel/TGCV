# TGCV — Rust Ω-Primary Documentary Governance Phase Closure Decision 001

**Status:** DOCUMENTARY GOVERNANCE PHASE CLOSED WITH RESTRICTIONS / SCIENTIFIC ADMISSION NOT GRANTED  
**Decision date:** 2026-10-09  
**Branch:** `governance/rust-omega-raw-data-admission-firewall-audit-20261009`  
**Decision type:** Prospective governance closure for documentary review only; no scientific execution

## 1. Decision

The documentary governance review phase for the existing Rust Ω-Primary source dataset and historically constructed U_t artifact is **CLOSED WITH RESTRICTIONS**, limited to the documentary work and evidence recorded in the linked governance records.

This closure means that the documentary review work possible with the currently available evidence has been recorded. It does **not** mean that the dataset or U_t has been proven anonymous, that indirect-linkage risk has been empirically measured, that local operational controls have been fully audited, or that scientific reuse is safe or admitted.

## 2. Findings and evidence boundaries

The review records distinguish the following findings:

- **Source ZIP identity:** local file size and published Figshare MD5 were previously recorded as matching. This supports the documented source-file identity with the stated MD5 limitation; it is not a new hash check.
- **Published license metadata:** the Figshare item-level CC0 declaration is recorded as published metadata. This does not settle privacy, identifiability, or every proposed use.
- **Existing U_t artifact identity:** the physical-file SHA-256 `6d2f3066346c70068e6d044fa5575ff5a84572f74ca1ada06d5d3b49239810ab` is retained from the user's previously supplied local output. It was not recalculated for this decision.
- **Field inventory:** documented source schemas do not explicitly list names, email addresses, or login fields in the two CSV members declared by the historical runner. This limited observation does not establish anonymity or privacy of the entire archive.
- **Indirect linkage:** plausible paths through numeric package/version IDs, timestamps, dependency graph structure, row ordinals, and combinations of these fields are documented in the preliminary threat model. No empirical linkage or re-identification test was performed.
- **Independent review:** an independent privacy/re-identification reviewer is currently unavailable, as reported by the user. This remains a limitation.
- **Operational controls:** evidence is partial and includes user-reported declarations. Additional copies, some access history, and some backup/synchronisation paths remain unknown; no complete local storage/access audit is claimed.
- **Historical sequencing:** the dataset admission decision was not evidenced as granted before historical processing. The sequencing deviation remains acknowledged and is not retroactively cured.

No finding in this closure should be interpreted beyond its stated evidence boundary.

## 3. Effective retention and use boundary

The separate existing-artifact retention decision remains in force. The existing U_t JSON is retained at its current location solely for documentary provenance, audit, integrity reference, and reproducibility review.

Permitted:
- preserve the existing artifact in place;
- cite its recorded identity and hash in governance records;
- review existing provenance, schema descriptions, and execution records without opening or processing the artifact's data bytes.

Not authorised by this closure:
- scientific inspection of U_t rows or content;
- structural transformation-space or reachability analysis using U_t;
- new derivations, fixtures, or U_t reconstruction;
- new downloads or data transformations;
- longitudinal absence/removal claims;
- external disclosure or public release;
- any new scientific execution.

Any change in permitted use, relocation, creation of additional copies, deletion, or external disclosure requires a separate explicit prospective decision. Any scientific execution also requires explicit execution authorisation.

## 4. Gate status

- Documentary governance review: **CLOSED WITH RESTRICTIONS**.
- Source ZIP identity evidence: **RECORDED / MATCHED WITH MD5 LIMITATION**.
- Published CC0 metadata: **SUPPORTED AS PUBLISHED METADATA ONLY**.
- Indirect-linkage threat model: **DOCUMENTED PRELIMINARILY / EMPIRICALLY UNTESTED**.
- Privacy/identifiability clearance: **NOT GRANTED**.
- Existing U_t scientific reuse: **BLOCKED**.
- Further processing and scientific execution: **NOT AUTHORISED**.
- External disclosure/public release: **BLOCKED**.
- Historical admission sequencing deviation: **ACKNOWLEDGED / NOT RETROACTIVELY CURED**.
- TGCV Core and Ω-primary canonical status: **UNCHANGED**; Ω-primary remains proposed/non-canonical.

## 5. No retroactive cure or scientific claim

This decision closes only the bounded documentary review phase. It does not retroactively grant admission for the historical processing that already occurred. It makes no claim about causality, value, transformational intelligence, reachability, anonymity, or empirical validity of Ω-primary.

The U_t coverage limitation also remains in force: `UNKNOWN_MISSING` must not be interpreted as absence or removal.

## 6. Conditions for reopening

Reopen the relevant gate if any of the following occurs:
1. a request is made for structural scientific reuse, further processing, or scientific execution;
2. the artifact's purpose, storage location, access conditions, copies, or retention boundary changes;
3. external sharing or publication is proposed;
4. new evidence materially changes the linkage threat model or operational-control assessment;
5. an independent privacy/re-identification review becomes available and is judged necessary for the proposed use.

Reopening requires a separate prospective decision. This closure itself grants no additional permission.

## 7. Related records

- `00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_ADMISSION_SEQUENCE_RECONCILIATION_DECISION_001.md`
- `00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_EXISTING_U_ARTIFACT_RETENTION_DECISION_001.md`
- `00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_PROSPECTIVE_ADMISSION_GATE_READINESS_MATRIX_001.md`
- `00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_INDIRECT_LINKAGE_THREAT_MODEL_001.md`
- `00_GOVERNANCE/architecture/TGCV_RUST_OMEGA_PRIMARY_FIELD_LEVEL_PRIVACY_AND_REUSE_ASSESSMENT_001.md`
- `00_GOVERNANCE/decisions/TGCV_RUST_OMEGA_PRIMARY_LOCAL_CONTROLS_EVIDENCE_RECORD_20261009_001.md`

This is a governance-only decision. No dataset bytes were opened or processed, no scientific code was executed, and no local artifact was modified. The repository's main branch and TGCV Core are unchanged by this decision.
