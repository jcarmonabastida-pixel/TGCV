# D-OPS-16 — Legal / Regulatory Rule-Layer & Longitudinal-State Identifiability Audit v0.1

**Status:** CLOSED — CANDIDATE RETAINED CONDITIONALLY / NOT EXECUTION-READY
**Date:** 2026-09-08
**Execution:** NOT AUTHORIZED
**Scope:** Legal / regulatory systems, with BOE/EUR-Lex as concrete public archival infrastructures

## 1. Purpose

Determine whether a legal/regulatory domain can instantiate the TGCV operational architecture independently of observed outcomes, while satisfying the stricter D-OPS-15 rule-layer-first filter:

1. independently governed rule layer;
2. public, versioned longitudinal state archive;
3. stable canonical identity across versions;
4. independently defined transformation universe U_tau;
5. non-circular pre-execution accessibility predicate P_tau;
6. downstream Reach distinct from T_acc.

No dataset download, sampling, implementation or real-data execution is authorized by this audit.

## 2. Historical reconstruction

D-OPS-14 closed the railway route because public historical state recovery could not be demonstrated. The governance consequence was to return to discovery rather than reconstruct a missing state. The current search therefore applies the stricter rule-layer + longitudinal-archive filter.

The existing TGCV architecture remains unchanged:

- Core_ontological = S
- T_acc,t = {tau in U_tau | P_tau(S_t,C_t,L)=1}
- Delta T_acc is the primary comparative object
- Reach and Trajectory are downstream
- Outcome and Value are downstream and cannot define accessibility retrospectively.

## 3. Candidate domain

### Legal / regulatory text and rule systems

Two public infrastructures were examined:

- Spanish BOE / AEBOE consolidated legislation and ELI identifiers.
- EU EUR-Lex / CELLAR consolidated legislation and machine-readable metadata.

### 3.1 Longitudinal archive — BOE

The AEBOE states that consolidated legislation includes the latest text and intermediate versions corresponding to modifications over time. Its API exposes a specific norm by identifier, including all text versions, metadata, legal analysis and ELI metadata. The text endpoint exposes the complete history of versions; blocks within a norm also carry their successive versions and publication dates.

The BOE ELI implementation provides persistent legal-resource URIs and explicitly encodes version and version_date for consolidated versions. The BOE states that it provides the initial version and all consolidated versions a norm has undergone.

Assessment: **longitudinal state archive PASS**.

### 3.2 Longitudinal archive — EUR-Lex / CELLAR

EUR-Lex states that consolidated texts provide the view of an EU act applicable at a specific point in time and that “show all versions” exposes all consolidated versions of an act. CELLAR provides a machine-readable data model and public SPARQL/REST access to metadata and document content. Its WEMI model distinguishes legal works, expressions, manifestations and items.

Assessment: **longitudinal state archive PASS**.

### 3.3 Rule layer

The legal domain has an explicit external rule layer: statutes, regulations, amendments, derogations, applicability dates, validity information and formal relations between legal acts. BOE consolidation criteria explicitly distinguish express modifications, corrections and derogations and record entry-into-force information. EUR-Lex consolidation methodology specifies how amendments and applicability dates determine the consolidated state.

Assessment: **independently governed rule layer PASS**.

## 4. TGCV identifiability audit

| Criterion | Result | Assessment |
|---|---|---|
| D16-1 Domain independence | PASS | Materially distinct from Rust package dependency evolution. |
| D16-2 Observable system state S | PASS | A legal corpus / norm-state can be reconstructed from identified acts and versions. |
| D16-3 Observable C and L | CONDITIONAL | Jurisdiction, temporal applicability, hierarchy and legal scope are observable, but the exact analytical level must be frozen. |
| D16-4 Independent U_tau | CONDITIONAL | Candidate transformations can be defined as formally specified legal-state edits (insert, repeal, replace, modify, activate/deactivate provisions), but the exact universe must be frozen before data access is used to define it. |
| D16-5 Canonical tau | PASS/CONDITIONAL | Norm identifier + provision/block + operation + target text/version can be canonicalized; exact identity contract remains to be designed. |
| D16-6 Pre-execution P_tau | CONDITIONAL | Formal admissibility can be based on legislative/legal rule constraints and temporal applicability, but this must not collapse into “actually enacted” or “observed legal effect”. |
| D16-7 T_acc construction | CONDITIONAL | Potentially constructible from the frozen legal rule layer, but no operational protocol yet exists. |
| D16-8 Delta T_acc | PASS/CONDITIONAL | Versioned legal states provide a genuine longitudinal boundary; accessibility comparison is feasible in principle once U_tau/P_tau are frozen. |
| D16-9 Downstream Reach | CONDITIONAL | Reach can be represented as legally admissible successor corpus/configuration states, but successor semantics must be independently specified. |
| D16-10 Reproducibility | PASS | BOE and EUR-Lex provide public APIs/structured access and versioned identifiers. |
| D16-11 Information firewall | PASS in principle | Future court outcomes, compliance, economic effects, political outcomes and value can be excluded from accessibility construction. |
| D16-12 Falsifiability | PASS | The candidate admits non-trivial collapse cases, including equal T_acc across legal-state changes and equal Reach despite Delta T_acc. |

## 5. Critical semantic risk

The decisive unresolved issue is **not data availability**. It is the definition of accessibility.

A legally enacted modification must not automatically be treated as the complete set of transformations that were accessible before enactment. Conversely, defining P_tau from the observed fact that a legislature enacted a transformation would make accessibility retrospective and circular.

Therefore the following are prohibited:

- using enactment frequency as P_tau;
- using subsequent court decisions as P_tau;
- using compliance or enforcement outcomes as P_tau;
- using economic/social outcomes as P_tau;
- defining U_tau from only observed amendments;
- treating the historical sequence of enacted laws as T_acc;
- using later legal states to classify earlier accessibility.

The domain is admissible only if an independent legal transformation universe and pre-enactment admissibility predicate can be frozen.

## 6. Candidate operational direction

A potentially viable operationalization is **normative-state transformation space** rather than “law as observed event”.

Candidate state:

`S_t = canonical normative corpus at time t`

Candidate transformation universe:

`U_tau = formally typed edits over identified normative provisions`

Candidate accessibility predicate:

`P_tau(S_t,C_t,L) = 1` iff the transformation is legally admissible under a separately frozen rule layer at t, without consulting whether the transformation was later enacted or what happened after t.

This is only a design direction. It is **not frozen** and must not be treated as an empirical specification.

## 7. Scientific information gain

The candidate has unusually high potential information gain because it is:

- outside software/package dependency evolution;
- governed by explicit rule systems;
- intrinsically longitudinal;
- rich in canonical version identifiers;
- publicly reproducible;
- structurally capable of separating state change from the space of formally admissible normative transformations.

However, information gain is not sufficient for selection. The remaining P_tau/U_tau ambiguity is decisive.

## 8. Decision

**D-OPS-16 = CLOSED — LEGAL/REGULATORY DOMAIN RETAINED CONDITIONALLY; NOT EXECUTION-READY.**

The domain passes the archival and rule-layer requirements that blocked railway, but does not yet pass the full TGCV operational identifiability requirement.

This is **not** an empirical failure and does **not** alter the TGCV claim matrix.

No real-data execution is authorized.

## 9. Next controlled operation

**D-OPS-17 — Legal Transformation Universe & Pre-Execution Admissibility Design Gate.**

The next operation must answer only:

1. What is the independently defined universe U_tau of legal-state transformations?
2. What exact rule system determines P_tau before observing enactment or downstream effects?
3. Can the resulting T_acc be computed from a frozen legal state without using future information?
4. Can Reach be constructed as a downstream successor object without collapsing into the observed amendment history?

If these questions cannot be answered non-circularly, the legal domain must be rejected despite its excellent archival infrastructure.

**REAL-DATA EXECUTION AUTHORIZED: NO.**

## 10. Primary sources reviewed

- BOE Open Data API / consolidated legislation: https://www.boe.es/datosabiertos/api/api.php
- BOE consolidated legislation FAQ: https://www.boe.es/datosabiertos/faq/consolidada.php
- BOE ELI implementation: https://www.boe.es/legislacion/eli.php
- EUR-Lex consolidated texts: https://eur-lex.europa.eu/collection/eu-law/consleg.html
- EUR-Lex ELI: https://eur-lex.europa.eu/content/help/eurlex-content/eli.html
- EUR-Lex / CELLAR data reuse: https://eur-lex.europa.eu/content/help/data-reuse/reuse-contents-eurlex-details.html
- EUR-Lex consolidation methodology: https://eur-lex.europa.eu/content/intro/collection/Methodology-on-Consolidation.pdf
