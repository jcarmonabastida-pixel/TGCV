# TGCV — Research Page Experience v0.1

**Identifier:** TGCV-WEB-RESEARCH-EXP-001  
**Version:** 0.8  
**Date:** 2026-11-25  
**Status:** EDITORIAL WORKING DRAFT — NOT APPROVED FOR PUBLICATION  
**Branch:** `strategy/tgcv-web-master`  
**Parent documents:** Web Master Brief v1.5; Information Architecture v1.8; Content Blueprint v1.7; Explore Experience v0.9; Explore Copy v0.8.  
**Scientific source baseline:** TGCV Core current; Research Prospectus v0.2; Testable Concept Paper v0.4; Architectural Research Map v0.2; STATUS.md as retrieved from `main` on 2026-11-25.

> This document specifies the visitor experience for Research. It does not change scientific governance, scientific claims, evidence status, publication permissions or execution authorizations. All scientific source assets require a fresh status and publication-permission check before public linking.

---

## 1. Role in the visitor journey

Research is the transition from understanding the idea (Home and Explore) to understanding the programme that investigates it.

- **Home** raises the question: how can a system come to do something it could not do before?
- **Explore** explains how system boundaries and conditions shape which candidate transformations are within reach, and why accessibility is distinct from execution, outcome and value.
- **Research** answers: what exactly is TGCV investigating, how is the question structured, how is it tested, what has the work established so far, and what remains unresolved?

Research must not repeat Explore's introductory explanation at length. It should assume the visitor has encountered the basic distinctions, briefly restate the minimum needed, then move into the scientific object, research questions, methods, evidence and limitations.

**Primary visitor outcome:** leave with an accurate understanding of TGCV as an integrative, falsifiable applied-research programme; its current conceptual architecture; the questions and methods through which it is being examined; and the bounded status of its evidence.

**Secondary visitor outcome:** know where to go next—to Systems Engineering for modelling and engineering practice, Transformational Intelligence for the capability concept, or Labs & Applications for bounded demonstrators and exploratory contexts.

## 2. Audience and depth

The page serves several levels without becoming a technical repository dump:

1. **Curious but informed visitor:** wants to know what the programme investigates and why it is a research question.
2. **Researcher / academic:** wants the object, questions, conceptual commitments, falsifiability and evidence boundaries.
3. **Systems engineer / technical practitioner:** wants to understand the analytical architecture and how it relates to modelling, constraints, dependencies and domain semantics.
4. **Potential collaborator:** wants to distinguish current work, open questions and possible contribution areas.

Use progressive disclosure: plain-language explanation first; compact architecture diagram and research-question summaries next; evidence-status detail and controlled source references last.

## 3. Narrative architecture

### Block 1 — What is TGCV?

**Visitor question:** What is TGCV, and what does it actually investigate?

Introduce the approved public identity:

**TGCV — Transformaciones Generativas y Construcción de Valor**

*Un programa de investigación aplicada e innovación sobre cómo la ampliación de las posibilidades de transformación de los sistemas puede contribuir a la construcción de valor.*

Explain that TGCV is a research programme, not a consolidated or universally validated theory. It investigates the structure and evolution of transformations accessible to systems, the conditions that shape that accessibility, and the possible downstream implications for reachability, trajectories, outcomes and value.

The English page uses **TGCV — Generative Transformations and Value Construction** and the approved English descriptor.

**Experience:** concise identity and purpose, followed by one strong research question. Avoid a long institutional preamble or a promotional pitch.

### Block 2 — The research object

**Visitor question:** What is the scientific object, beyond the general idea that systems change?

Explain the distinction between a system's state and the transformations accessible under relevant conditions.

Introduce the current minimum carefully:

- (S): the relevant system/state; this is the current ontological Core.
- (T_{acc}): an analytical representation of transformations accessible under relevant state, context and constraint conditions.
- (Delta T_{acc}): change in the structure of accessible transformations over time.

A candidate transformation is accessible only under a declared rule and relevant conditions; accessibility must not be defined retrospectively from execution or outcome.

State explicitly that (T_{acc}) is analytically indispensable but is not an independent ontological primitive in the current Core. Context and constraints inform the analytical representation; they are not additional Core primitives.

Show that change is sign-neutral: the accessible structure may expand, contract, reconfigure or substitute. Do not imply that every change is an expansion or improvement.

**Experience:** a compact conceptual diagram, supported by a short explanation. Do not reproduce the entire Explore migration example.

### Block 3 — From accessibility to downstream consequences

**Visitor question:** How does the research connect accessibility with what happens next?

Present the analytical sequence:

`mechanism → (S,C) → (S',C') → ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

Explain the notation in plain language: **C** is the relevant context and conditions at the initial point; **C'** is the context and conditions at the later point, after the transition being examined. The prime marks a later state of the context, not a different category. Give concrete examples (operating environment, organisational arrangements, institutional rules) and distinguish context from separately specified constraints, resources and admissibility conditions. Explain that this is an analytical architecture, not an already established complete causal chain. Each link needs its own definition, operationalisation and evidence.

Clarify:
- Reach concerns what states/configurations can be reached under a declared transition semantics.
- Trajectory concerns temporal development through states and transitions; it is not a single inevitable linear path.
- Outcome is an observed result.
- Value is a downstream evaluation that requires an explicit, context-sensitive model.
- A change in accessibility does not by itself establish execution, a favourable outcome or value.

The public-facing visual should make the distinctions inspectable without suggesting that all links have equal evidential status.

### Block 4 — The research questions

**Visitor question:** What questions is TGCV trying to answer?

Organise the programme around the six research questions in the current controlled Research Prospectus v0.2. Present them as open research questions, not completed achievements:

1. **Structure and identifiability:** What minimal representation distinguishes the system, candidate transformations, accessibility and changes in accessibility without circularity or unjustified conceptual redundancy?
2. **Dynamics:** Under what conditions can changes in (T_{acc}) be identified independently of observed outcomes and distinguished from changes in state, Reach or Trajectory?
3. **Cross-domain translation:** Can the analytical distinctions be carried across heterogeneous domains while preserving domain-specific semantics rather than merely renaming existing constructs?
4. **Reach and Trajectory:** Under what conditions are accessibility changes related to differences in reachable states or subsequent trajectories?
5. **Outcome and Value:** What additional conditions and evidence would be required to establish a defensible relationship with outcomes and value?
6. **Limits:** In which domains or conditions do identifiability, translation or downstream relationships fail?

**Experience:** use question-led blocks. For each, distinguish the problem, what would count as informative evidence, and the possibility of a negative or limiting result. Avoid turning the page into a list of claimed accomplishments.

### Block 5 — How the programme tests its ideas

**Visitor question:** How can these questions be investigated scientifically?

Explain the methodological logic at a high level:

- define the system boundary and unit of analysis;
- specify the candidate transformation(s);
- define an accessibility/admissibility rule independently of outcome;
- freeze relevant decision-time conditions and temporal assumptions;
- reconstruct the transition where applicable;
- measure or analyse downstream Reach, Trajectory and Outcome separately;
- evaluate Value only under an independently specified model;
- compare against relevant domain baselines and alternative explanations;
- state assumptions, sensitivity and limits before interpreting results.

Clarify that exhaustive ex-ante enumeration of every accessible transformation is not a universal prerequisite; operational closure is case-dependent. Partial knowledge of alternatives does not automatically invalidate a study, but the focal transformation's accessibility must be independently and temporally well-defined.

Present synthetic experiments, computational analyses, empirical domain studies and cross-domain translation as distinct forms of work. Do not imply that a synthetic result is empirical validation or that a demonstrator is a scientific test.

**Experience:** a methodological pathway or layered diagram. Each method type must carry a clear label indicating what it can and cannot establish.

### Block 6 — What the evidence currently says

**Visitor question:** What has the research found so far, and what can those findings support?

This block is a public-facing evidence overview, not a project-status report or a dump of internal tracking records. Organise it by research question or evidence theme, using plain-language titles:

- [longitudinal evidence of changes in accessible transformations in a software ecosystem](https://github.com/jcarmonabastida-pixel/TGCV/blob/strategy/tgcv-web-master/06_WEB/TGCV_WEB_EVIDENCE_SOFTWARE_ECOSYSTEM_v0.1.md) — first detailed evidence brief, in Spanish and English;
- [analysis of the distinction between accessible transformations and potential reachability](https://github.com/jcarmonabastida-pixel/TGCV/blob/strategy/tgcv-web-master/06_WEB/TGCV_WEB_EVIDENCE_REACH_DISTINCTION_v0.1.md) — an open empirical question because the successor construction examined so far was not independent of accessibility;
- [controlled tests and cross-domain reconstruction](https://github.com/jcarmonabastida-pixel/TGCV/blob/strategy/tgcv-web-master/06_WEB/TGCV_WEB_EVIDENCE_METHODS_CROSS_DOMAIN_v0.1.md) — a bounded synthetic test of representational insufficiency and a secondary analysis of previously audited evidence from two domains;
- [from accessibility changes to subsequent trajectories](https://github.com/jcarmonabastida-pixel/TGCV/blob/strategy/tgcv-web-master/06_WEB/TGCV_WEB_EVIDENCE_ACCESSIBILITY_TRAJECTORY_v0.1.md) — a bounded temporal reconstruction, a randomised structural-access intervention and an explicit account of the limits of trajectory observation;
- [selected research cases and evidence portfolio](https://github.com/jcarmonabastida-pixel/TGCV/blob/strategy/tgcv-web-master/06_WEB/TGCV_WEB_EVIDENCE_PORTFOLIO_v0.1.md) — a bilingual overview of representative empirical, industrial, computational and synthetic work, including SWIM, AWS functional recovery, rural financial access, software ecosystems, EV–Grid, VSL Paired, cross-domain tests and additional methodological cases;
- analyses identifying conditions under which accessibility cannot be determined confidently.

For each theme, distinguish the research question, system/data, method, main finding, scope and limitations. State explicitly what the result does not establish. Do not display internal project codes, experiment identifiers, governance labels or raw status excerpts as public-facing names or claims.

**Evidence links are part of the experience, not optional decoration.** Each theme should link to a dedicated, readable evidence description. That page should provide enough detail for an interested visitor to understand and assess the result, with links to public papers, methods, data or reproducibility materials where publication permission exists. If a detailed public description does not yet exist, do not show a dead link or expose a private record; mark the item as awaiting a public evidence brief in the editorial workflow.

The overview must make clear that evidence is heterogeneous and bounded. It must not imply universal validation, general causal efficacy, predictive value, value creation, superiority, full originality, industrial deployment or general Transformational Intelligence validation.

**Experience:** concise evidence summaries with meaningful titles and a clear “Explore the evidence” link to each public evidence brief. Each brief should include: question; system and unit; data and period; operational definitions; method/design; result; what it supports; what it does not establish; limitations; public sources and version/date. Avoid traffic-light badges as a substitute for explanation.

### Block 7 — What remains open

**Visitor question:** What does TGCV not yet know?

Make open questions visible rather than burying them in footnotes. For each question, distinguish: (a) what is currently defined or supported; (b) what remains unidentified; (c) what observation or comparison would support the claim; and (d) what result would weaken, restrict or refute it under the stated conditions.

At minimum, cover:
- **Accessibility identification:** whether T_acc can be defined from independent, pre-outcome admissibility conditions; circularity, temporal leakage or non-reproducibility limit identification.
- **Additional explanatory/representational contribution:** whether TGCV adds information beyond domain-native models; pre-specified comparisons showing no relevant incremental contribution restrict the claim.
- **Reach and Trajectory:** when a change in T_acc is followed by a difference in reachable states or realised trajectories; repeated null or contrary results under conditions where a difference is predicted weaken the relevant proposition.
- **Causal contribution:** separation of the total intervention effect, the accessibility-mediated effect and residual pathways; where assumptions or data do not identify these quantities, state underidentification rather than causal confirmation.
- **Outcome and Value:** independent outcome and value measures; no effect, invalid measurement or effects attributable to other intervention components limit any value claim.
- **Cross-domain transfer:** whether constructs can be reconstructed without erasing domain semantics; failed or non-reproducible operationalisation marks an applicability boundary.
- **Transformational Intelligence:** whether the proposed capability can be distinguished and reproduced beyond stable preferences, heuristics or design artefacts.

Falsifiability applies to specific claims under explicit conditions, not to an undifferentiated all-or-nothing verdict on the entire programme. A negative, conditional or domain-limited result is a legitimate scientific outcome. Do not imply that every open question is simply awaiting engineering completion or retrospectively change criteria to turn a negative result into success.

### Block 8 — Research materials and traceability

**Visitor question:** Where can I inspect the underlying work?

Provide a curated, versioned list rather than a raw repository dump. Candidate source assets identified by the Content Blueprint include:
- current TGCV Core formulation;
- Testable Concept Paper v0.4;
- Research Prospectus v0.2;
- Vision Paper v0.3;
- Architectural Research Map v0.2;
- selected public papers, methods and evidence records after review.

For each asset, state document type, version/date, status and scope. Distinguish canonical scientific source, controlled external asset, working paper, historical/superseded material and public editorial summary.

**Publication gate:** CURRENT / CONTROLLED does not automatically mean unrestricted public release. Confirm publication permission, remove internal-only material and check that the asset has not been superseded before adding a public link. RMA, Evidence→Claim Matrix and internal governance records are sources for editorial verification; they are not automatically public downloads.

### Block 9 — Where the research connects

**Visitor question:** How does the research relate to the rest of the TGCV ecosystem?

Explain the complementary roles without collapsing them:
- **Systems Engineering:** practices for modelling, designing, integrating and working with engineered systems; not replaced by TGCV.
- **Transformational Intelligence:** a working capability concept concerning reasoning, navigation and adaptation in transformation spaces; not a synonym for AI and not generally validated.
- **Labs & Applications:** bounded demonstrators, synthetic methods and candidate application contexts; their maturity and evidence status must be labelled individually.

This block should orient rather than duplicate those pages.

### Block 10 — Invitation

Offer a restrained invitation to examine the research materials, ask a substantive question, suggest a correction or discuss a scoped collaboration. Only publish a contact route that is monitored and operational. Do not imply a staffed institute, scientific board, active community or guaranteed response.

## 4. Bilingual and terminology requirements

Spanish and English must be complete and conceptually equivalent.

| Spanish | English |
|---|---|
| programa de investigación aplicada e innovación | programme of applied research and innovation |
| sistema / estado | system / state |
| transformaciones candidatas | candidate transformations |
| transformaciones accesibles | accessible transformations |
| accesibilidad de las transformaciones | accessibility of transformations |
| cambio de la estructura de transformaciones accesibles | change in the structure of accessible transformations |
| alcance / estados alcanzables | Reach / reachable states |
| trayectoria | Trajectory |
| resultado | Outcome |
| valor | Value |

Use the English phrase “accessibility of transformations” with a short explanation so it is not confused with digital/interface accessibility. Keep “Outcome” consistent for the analytical layer corresponding to “resultado”.

Do not translate TGCV into a new acronym. Use the approved English rendering of the public name while retaining TGCV.

## 5. Editorial and scientific guardrails

- Do not present TGCV as an established, universally validated theory.
- Do not present (T_{acc}) as an ontological primitive independent of (S).
- Do not present the proposed (Omega_T) formalisation as frozen canonical ontology; the relevant proposal is a non-canonical development draft.
- Do not infer accessibility from execution, adoption, success or outcome.
- Do not infer causal efficacy from descriptive association.
- Do not infer value from accessibility expansion or a favourable outcome without an independent valuation model.
- Do not imply that accessibility always expands or that expansion is always beneficial.
- Do not imply that a complete universal enumeration of (T_{acc}) is required in every study.
- Do not turn bounded synthetic, computational, empirical or fixture-level evidence into universal or industrial validation.
- Do not claim general superiority, full originality or validated Transformational Intelligence.
- Do not use the public identity decision to rename or alter scientific artefacts.

## 6. Content production sequence

1. Approve this experience architecture and its research-page scope.
2. Reconcile the evidence snapshot against the current canonical RMA, Evidence→Claim Matrix, traceability and relevant audit records.
3. Prepare the complete Spanish Research copy.
4. Prepare and review the conceptually equivalent English copy.
5. Review every public source link, publication permission, version, status and no-claim.
6. Conduct scientific/editorial review before any visual-design or implementation phase.

## 7. Dependencies and publication conditions

**Authoritative working references:**
- Web Master Brief v1.5.
- Information Architecture v1.7.
- Content Blueprint v1.6.
- TGCV Core current.
- Research Prospectus v0.2.
- Testable Concept Paper v0.4.
- Architectural Research Map v0.2.
- Current STATUS, RMA and Evidence→Claim Matrix (freshly reconciled before publication).

This document is a page-experience specification only. It does not constitute final copy, visual design, publication clearance, scientific authorization or a change to any canonical research state.

## 8. Change log

### v0.1 — 2026-11-25
- Creates the first Research page experience specification.
- Defines the page's role after Home and Explore.
- Organises the visitor journey around the scientific object, research questions, methods, evidence, open questions and traceable materials.
- Adds explicit controls for evidence maturity, publication permission and the current scientific Core.
