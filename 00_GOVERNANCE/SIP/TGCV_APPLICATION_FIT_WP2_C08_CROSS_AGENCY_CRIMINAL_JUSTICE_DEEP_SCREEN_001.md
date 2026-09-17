# TGCV — WP2-C08 Cross-Agency Criminal Justice Deep-Screen 001

**Status:** PROVISIONAL — COUPLING-CANDIDATE / RECONSTRUCTION INCOMPLETE
**Date:** 2026-09-17
**Parent screen:** `TGCV_APPLICATION_FIT_WP2_DEEP_SCREENING_001.md`
**Candidate register:** `TGCV_APPLICATION_FIT_WP2_CANDIDATE_REGISTER_001.md`
**Scientific base:** RMA v3.35 / Evidence→Claim Matrix v1.12 / RMA traceability v3.35

## 1. Evidence boundary

The EU has an explicit programme of digitalisation and interoperability across criminal-justice authorities. The European Commission describes e-CODEX as an interoperable and secure decentralised communication infrastructure connecting national IT systems and supporting electronic exchange in cross-border civil and criminal proceedings. Regulation (EU) 2023/2844 establishes a legal framework for electronic communication between competent authorities in cross-border judicial cooperation, including criminal matters. [European Commission — Digitalisation of justice](https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/digitalisation-justice/communication-digitalisation-justice-european-union-and-proposal-e-codex-regulation_en); [EUR-Lex — Regulation (EU) 2023/2844](https://eur-lex.europa.eu/eli/reg/2023/2844/2023-12-27/eng).

Eurojust's Digital Criminal Justice Programme describes a redesigned Case Management System, secure communication channels with national authorities and connections to external systems including the JITs Collaboration Platform and ECRIS-TCN. SIRIUS likewise provides tools and platforms supporting law-enforcement and judicial authorities in cross-border access to electronic evidence. [Eurojust — Digital Criminal Justice Programme](https://www.eurojust.europa.eu/fr/node/2021); [Eurojust — SIRIUS](https://www.eurojust.europa.eu/sirius).

The UK Common Platform case study provides a concrete national example: legacy criminal-court case-management systems were brought together under a unified digital platform, with police, prosecution, courts, legal-aid and prison/probation stakeholders participating in the operating model. [GOV.UK — Common Platform](https://www.gov.uk/government/case-studies/common-platform-a-modern-digital-case-management-system-for-the-criminal-justice-system).

These sources establish a real cross-agency digital-transformation context. They do **not** establish TGCV validity, causal evidence, or differential value.

## 2. Why C08 is structurally different

C01: federated technical orchestration.

C03: agent/tool/permission action space.

C04: physical asset/digital-twin/maintenance coupling.

C05: shared-resource and constraint coupling between energy and mobility.

C08 introduces **institutional authority, inter-organisational workflow and case-trajectory coupling**.

The central question is not merely whether agencies exchange data. It is whether a state transition in one institutional domain changes which transformations are subsequently accessible to another agency in the same case trajectory.

A useful conceptual chain is:

`agency A state/decision → case-state transition → changed admissibility of agency B transformations → changed cross-agency trajectory`.

## 3. Decision-time boundary

A clean boundary should be defined at a concrete case-management decision immediately before an agency selects or authorises its next action.

Possible examples include:

- police investigation → prosecution referral;
- prosecution decision → request for additional evidence;
- prosecution → court filing;
- court disposition → prison/probation action;
- cross-border authority → request for evidence or judicial cooperation;
- one agency uploads/validates a case artefact → another agency becomes able to initiate a defined next action.

The screening should select **one concrete transition**, rather than attempting to model the entire criminal-justice system.

## 4. Candidate state representation

A bounded analytical representation is:

`S_t = {case status, legally/administratively recognised artefacts, current agency responsibilities, pending actions, relevant procedural state}`

`C_t = {available evidence, inter-agency messages, permissions/authority, deadlines, resource availability, procedural constraints, system interoperability state}`

`L = {legal/procedural admissibility rules, agency mandates, access rights, data-protection rules, workflow rules}`

The institutional component is important: an action may be technically possible but institutionally inadmissible because the acting authority lacks the required mandate, procedural condition or access right.

This is precisely why C08 should not be reduced to an IT interoperability case.

## 5. Candidate transformations

A deliberately finite `Uτ` might include:

- open a case or subcase;
- transfer/referral to another authority;
- request additional evidence;
- disclose an authorised case artefact;
- validate/accept a submitted artefact;
- issue a procedural request;
- schedule a hearing;
- file/forward a prosecution package;
- initiate a cross-border judicial-cooperation request;
- request preservation/disclosure of electronic evidence;
- change case status;
- initiate prison/probation action;
- return a case for missing information;
- close or suspend a procedural branch.

The actual experiment should select a small finite subset tied to one case trajectory.

## 6. Accessibility hypothesis

The provisional TGCV hypothesis is:

`case/institutional transition`
→ `change in admissibility of subsequent agency action`
→ `ΔT_acc`
→ `changed downstream case trajectory`.

Examples:

`validated evidence package becomes available to prosecution`
→ a defined prosecution transformation becomes admissible.

`required procedural authorisation absent`
→ a downstream action becomes inadmissible while request/return/remediation actions remain accessible.

`cross-border digital channel becomes available`
→ a previously unavailable evidence-request transformation becomes admissible.

`court disposition changes case status`
→ a different subset of prison/probation transformations becomes accessible.

The key is that the change must be specified **at decision time**, before the downstream outcome is known.

## 7. Institutional authority as an accessibility determinant

C08 provides a useful test of whether accessibility can be represented when the determining conditions are not purely physical or technical.

For example:

`Pτ(S_t,C_t,L)=1`

may require simultaneously:

- the relevant case artefact exists;
- it has the required status;
- the actor has the necessary authority;
- the receiving agency has access;
- the procedural precondition is satisfied;
- the relevant digital channel is available.

Thus:

`T_acc = F(S, C, L)`

can include institutional and procedural conditions without making institutional authority itself a TGCV primitive.

The candidate therefore tests the portability of the accessibility representation beyond technical systems.

## 8. Multidomain coexistence vs transformational coupling

The presence of police, prosecutors, courts and prison/probation services does not by itself establish multidomain transformational coupling.

Ordinary coordination could explain the observed structure:

- information sharing;
- workflow integration;
- case-management consolidation;
- process standardisation;
- interoperability;
- organisational governance.

The coupling hypothesis requires a stronger observation:

> A transition in the state of agency A changes the admissibility of a concrete transformation available to agency B, and that change can be represented independently of the downstream outcome.

This distinction is especially important because the Common Platform case demonstrates that digital consolidation can change how agencies interact, but that fact alone does not show a TGCV-specific explanatory contribution.

## 9. Conventional baselines

C08 has several strong alternative explanatory frameworks:

- BPM/workflow models;
- case-management systems;
- process mining;
- inter-organisational workflow models;
- access-control and authorisation models;
- legal/procedural rule engines;
- Petri nets and finite-state process models;
- interoperability architectures;
- digital public-service coordination models.

A TGCV demonstration must therefore avoid merely translating an existing workflow graph into the label `T_acc`.

The discriminating question is whether the transformation-space representation captures a reusable property of **how case-state changes alter future action possibilities across organisational boundaries**, and whether that property contributes information not already available in the conventional representation.

## 10. Minimum next proof

**Cross-Agency Case-State Transformation Mapper — synthetic bounded demonstrator.**

Use a synthetic case involving three agencies, for example:

`Police → Prosecution → Court`

with an optional fourth node:

`Court → Probation/Prison`.

The demonstrator should contain:

1. finite agency states;
2. finite case states;
3. finite candidate transformations;
4. explicit authority/access/procedural predicates;
5. `T_acc,0` reconstruction;
6. one controlled transition at agency A;
7. `T_acc,1` reconstruction for agency B;
8. downstream trajectory simulation;
9. a conventional workflow/process baseline;
10. comparison of explanatory information.

A useful controlled intervention is:

`case artefact status: unavailable → validated`

with all other state variables frozen.

A second intervention can be:

`agency authority/access: absent → present`

again freezing the remainder.

A third can be:

`interoperable channel: unavailable → available`.

The objective is to isolate whether the change in accessible transformations can be reconstructed as a direct analytical object.

## 11. Potentially strongest variant

The strongest bounded variant may use a **single case trajectory** rather than an entire criminal-justice workflow.

For example:

`Police investigation state S0`
→ `evidence package validated`
→ `prosecution receives authorised package`
→ `prosecution transformations become accessible`
→ `court submission`
→ `court transformations become accessible`.

The demonstrator would explicitly record:

`T_acc,0 → T_acc,1 → T_acc,2`

and compare this representation with an ordinary case-management/workflow representation.

The purpose is not to reproduce legal practice in full detail, but to test whether TGCV provides a useful cross-agency transformation-space abstraction.

## 12. Potential scientific route

C08 is potentially more suitable for a later scientific route than the technical demonstrators if a suitable empirical case can be identified with:

- a known decision-time boundary;
- independently observable institutional state;
- identifiable procedural/accessibility conditions;
- a reconstructible transition;
- observable downstream trajectory;
- sufficient counterfactual or quasi-experimental structure.

However, the current public material is architectural/programmatic and does not supply such a frozen empirical reconstruction.

Therefore no scientific evidence is admitted at this stage.

## 13. Maturation route

**Primary route: Applied Demonstration.**

The minimum artefact is a synthetic cross-agency case-state mapper.

A scientific route is conditional on finding a real case with sufficiently reconstructible institutional transitions.

A deployment route is not being assessed in this screen.

A value route is not being assessed.

## 14. Current disposition

**WP2-C08 — COUPLING-CANDIDATE.**

Reason: current EU and national digital-justice programmes demonstrate genuine cross-agency and cross-system transformation involving police, prosecutors, courts and other justice authorities, with interoperability, authority, secure information exchange and case-management changes. [European Commission](https://commission.europa.eu/strategy-and-policy/policies/justice-and-fundamental-rights/digitalisation-justice_en); [Eurojust](https://www.eurojust.europa.eu/fr/node/2021); [GOV.UK](https://www.gov.uk/government/case-studies/common-platform-a-modern-digital-case-management-system-for-the-criminal-justice-system).

The case is structurally interesting because accessibility may be determined by institutional authority and procedural state, not only technical resources. Nevertheless, ordinary workflow, process, authorisation and interoperability models remain strong alternative explanations.

Therefore C08 remains a **provisional coupling candidate**, not evidence of differential TGCV value.

## 15. Cross-case observation after C01–C05 and C08

The WP2 deep-screened set now spans:

- C01 — federated technical orchestration;
- C03 — AI-agent/tool/permission action spaces;
- C04 — physical-digital maintenance;
- C05 — energy–mobility resource/constraint coupling;
- C08 — institutional authority/inter-organisational case trajectories.

The recurrence is notable because the same analytical question can be posed across increasingly different systems:

`What state transition changes which transformations remain accessible next?`

But the recurrence is **not yet a validation result**. In every case, established domain-specific representations can potentially encode the same feasible-action information.

The next WP2 step should therefore be synthesis/discrimination rather than adding more candidates: compare C01/C03/C04/C05/C08 against the same baseline criteria and determine whether there is a coherent Applied Demonstration opportunity and/or a genuinely non-redundant scientific question.

## 16. Governance boundary

This deep-screen:

- does not modify TGCV Core;
- does not modify RMA;
- does not modify Evidence→Claim Matrix;
- does not modify STATUS;
- does not admit application-fit observations as scientific evidence;
- does not establish differential value;
- does not imply deployment readiness;
- does not substitute demonstration for scientific validation.

**Next controlled WP2 action:** cross-case synthesis of C01/C03/C04/C05/C08, with explicit baseline/discrimination matrix and selection of the smallest common Applied Demonstration or scientific discriminator.
