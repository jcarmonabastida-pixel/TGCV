# DEC-C10-098 — B1/Need_preZ minimum S7 source-opportunity frame

**Date:** 2026-11-12  
**Status:** ACCEPTED WORKING DESIGN DECISION — NOT DESIGN FREEZE  
**Scope:** Ex-ante expected opportunity frame for the S7 focal declaration in B1/Need_preZ validation  
**Branch:** research/c10-s-consolidation-draft · PR #116 (Draft)

## 1. Decision

The user explicitly accepted the recommendation to adopt **one logical S7 source opportunity per UE** in the approved B1/Need_preZ validation census.

The accepted unit is an expected logical opportunity, not a guarantee of emission, capture, retention, admissibility or successful adjudication. The opportunity is enumerated ex ante for every UE in the approved, versioned B1/Need roster, under the same focal claim dimension Need_preZ, before truth-dependent observation outcomes, emission, capture or adjudication are generated.

The opportunity supports either polarity of the focal declaration:
- affirmative inclusion of the B1 focal operational objective;
- affirmative focal exclusion of that objective.

It may also result in an ambiguous/conflicting declaration, non-emission, failed capture or loss. Those states do not become affirmative exclusion and do not establish observed=0.

## 2. Microdomain and scope

This decision inherits DEC-C10-051: Option A, migration of configuration between two software environments, with F* retained as a candidate functional contract. It does not reopen microdomain selection.

The declarative scope is B1's own focal operational objective for the linked UE and logical service instance at baseline t−1. The proposed declarant attribution is B1 self-attestation within that limited scope. It does not confer authority on B1 over technical configuration, IAM, the service implementation, or third-party objectives.

The one-opportunity rule is a minimal frame for the S7 semantic declaration. Identity, binding, provenance, authority, temporal integrity and coverage remain mandatory controls, not additional semantic source opportunities. Copies/derivatives of the same declaration retain common lineage and are not independent corroboration.

## 3. Independence and temporal constraints

The expected opportunity frame and its scope are fixed before generating:
- need_truth_state-dependent observation outcomes;
- Z or D2;
- installation, accessibility, Reach, trajectory, execution, Outcome or Value;
- evidence search/capture outcomes;
- E1/E2 adjudication or Analyzer output.

This does not assert statistical independence of the observation content from baseline truth. DEC-C10-097 permits truth to influence authentic observable content only through an explicitly specified observation mechanism, without direct truth-label copying or side-channel leakage. This decision does not define that mechanism's probabilities, parameters or dependence graph.

The declaration's event time is pre-Z at t−1. Later capture may preserve a demonstrably immutable pre-Z record but cannot turn post-Z content into baseline evidence.

## 4. Evaluation and coverage

The expected-source universe for the focal UE × Need_preZ dimension contains one logical S7 opportunity. Coverage is assessed against that enumerated opportunity and its in-scope surfaces, with the existing NONE/PARTIAL/COMPLETE semantics.

COMPLETE means the declared opportunity and all applicable in-scope surfaces were examined under the versioned rule. It does not imply emission, validity, an affirmative statement, or observed=0.

observed=0 still requires an admissible affirmative focal exclusion. Non-emission, absence, failed search, loss, ambiguity, conflict or insufficient coverage yield observed=? or an explicit technical block according to DEC-C10-097; never infer zero from silence.

The validation cohort remains the census of all UE in the approved roster under DEC-C10-096. The one-opportunity frame does not alter causal populations, ITT denominators, P* populations, positivity or identification.

## 5. Explicit non-decisions

This acceptance does not fix:
- roster size, UE identities or materialized opportunity IDs;
- truth prevalence or proportions of 1/0/?;
- emission, error, ambiguity, conflict, capture or loss probabilities;
- conditional-independence assumptions or source-dependence parameters;
- the physical source document format, signature, storage or schema;
- a cognitive agent model or a separate pre-Z signal variable;
- statistical power, precision or sensitivity adequacy;
- implementation, materialization, DGP/Analyzer execution or replay authorization.

The observation channel and its mechanism remain OPEN for explicit specification and justification. B1 self-attestation is accepted as the proposed declarative mandate within the narrow objective scope; its concrete identity/role implementation and authority evidence remain design requirements.

## 6. Reconciliation and reuse

This decision specializes the proposal in §10.9 of C10_S_B1_PREZ_EVIDENCE_SOURCE_INVENTORY_AND_COVERAGE_AUDIT_DRAFT_001.md, and must be read with:
- DEC-C10-095 (truth composition and focal exclusion);
- DEC-C10-096 (census validation cohort);
- DEC-C10-097 (observation and coverage model);
- the B1 objective specification contract;
- the DGP temporal/role contract;
- the observation mechanism and coverage reconciliation.

No new U_G target, Evidence→Claim claim, analytical package artifact, PE role, test family or test ID is created.

## 7. Status and authorization

Accepted working design decision on the research branch; not Design Freeze, implementation approval, materialization approval or scientific execution authorization.

scientific_execution=false; execution_authorized=false.

## 8. Traceability

User acceptance: 2026-11-12, response “Sí” to the recommendation “una oportunidad lógica S7 de autodeclaración basal B1 por UE”.
