# TGCV — GL-07 Material Evidence Completeness Rule

**Status:** GOVERNANCE RULE — PERSISTENT  
**Effective:** 2026-09-18  
**Scope:** Evidence-to-Claim Matrix and all future cumulative matrix versions

## Rule
A material evidence section in the Evidence-to-Claim Matrix is an **expediente material desarrollado**, not a summary or citation stub. Whenever a material evidence item is routed to a claim, its corresponding `Material ... evidence` section MUST be **complete, enriched and autocontained** within the same matrix version.

### Mandatory content
A complete material section MUST contain, to the extent applicable to the evidence type:
1. identity, status and evidence classification;
2. purpose, research role and frozen scope;
3. source/provenance, protocol, runner, fixture, commits, environment and output identifiers;
4. operational universe, variables, constructs and execution or inspection contract;
5. methods and coverage actually executed;
6. quantitative or otherwise material findings, including controls and negative controls;
7. interpretation of what the evidence establishes;
8. explicit distinction between observation, reconstruction, inference and non-claim;
9. methodological limitations, identification boundaries and reproducibility boundaries;
10. evidence-to-claim routing, including positive, qualifying and explicitly excluded propagation;
11. governance disposition and claim-level consequences.

### Autocontainment test
A reader MUST be able to understand the material result, its provenance, operational scope, findings, limitations and claim impact from the section itself, without reconstructing the evidentiary record from scattered table cells, short references or external chat context. External artifacts MAY be cited for auditability, but citations MUST supplement the developed section rather than substitute for it.

### Anti-compression rule
A version MUST NOT satisfy GL-07 by reducing a developed material record to a few summary paragraphs, a status line, a list of artifact names, or a compressed claim-table cell. If the predecessor contains a developed material expediente, the cumulative successor MUST preserve it. If a predecessor contains only a compressed representation of material evidence, the successor MUST restore the developed record when that evidence is carried forward or materially relied upon.

### Versioning and GL-07
GL-07 is distinct from the incremental-version header rule: the version header records only what the current version changes; GL-07 governs the required completeness of the underlying cumulative material-evidence record. Adding or enriching a material section is therefore a versioned governance change even when claim status/level remains unchanged.

### Integrity relation
The matrix must satisfy the bidirectional relation:
`material evidence item routed in claim table ↔ complete, enriched, autocontained material expediente`.

A GL-07 failure is a **governance-integrity defect**, not a reason to silently delete, compress or downgrade the underlying evidence. The corrective action is to restore or enrich the material expediente and re-run the cumulative preservation and bidirectional-integrity checks.
