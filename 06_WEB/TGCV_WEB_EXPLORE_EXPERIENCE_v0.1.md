# TGCV — Explore Experience Specification

**Identifier:** TGCV-WEB-EXPLORE-001  
**Version:** 0.9  
**Date:** 2026-11-25  
**Status:** STRATEGIC EXPERIENCE SPECIFICATION — WORKING DRAFT  
**Parent:** `06_WEB/TGCV_WEB_MASTER_BRIEF_v0.1.md`, §21–22  
**Related:** `06_WEB/TGCV_WEB_INFORMATION_ARCHITECTURE_v0.1.md`, §16–17; `06_WEB/TGCV_WEB_CONTENT_BLUEPRINT_v0.1.md`, §12–13; Home Experience v1.4; Home Copy v1.1  
**Copy:** `06_WEB/TGCV_WEB_EXPLORE_COPY_v0.1.md` — v0.5  
**Branch:** `strategy/tgcv-web-master`

---

## 1. Purpose and authority

Explore is the first guided conceptual destination after Home. Its purpose is to turn the initial intuition that a system's possibilities can change into an accessible, operational understanding of what this means.

Explore is an editorial and experience-design artifact. It does not modify TGCV's scientific Core, canonical definitions, evidence status, execution authorization or research priorities. The approved identity, audience and first-release decisions in Web Master Brief §21 govern this specification.

Explore must add conceptual depth and a bounded example; it must not repeat the Home narrative or become a technical Research page.

## 2. Primary visitor and intended understanding

### 2.1 Primary visitor

Address people who research, design, develop or engineer systems. Keep the explanation understandable to adjacent audiences and interested newcomers without assuming prior knowledge of TGCV.

### 2.2 Intended understanding

After engaging with Explore, a visitor should be able to explain in ordinary language:

1. Why a system is more than its current state.
2. Why a transformation can be considered as a candidate without being accessible under current conditions.
3. How a change in relevant conditions can make a transformation accessible, inaccessible or differently constrained.
4. Why accessibility does not mean execution, and why execution does not guarantee a particular outcome or value.
5. How transformations relate to the system's subsequent states and trajectory.
6. Why understanding these possibilities requires looking at system elements, relationships and conditions together.
7. How Systems Thinking, Systems Engineering, Transformational Intelligence and TGCV relate without being treated as equivalent concepts.

The visitor should also be able to identify a useful next destination: Research, Systems Engineering or Transformational Intelligence.

## 3. Narrative architecture

Keep the approved six-part progression. The page should move from an intuitive observation to an example, then to conceptual distinctions and the ecosystem's integrative orientation.

### Opening

**Question:** “¿Qué cambia cuando cambia lo que un sistema puede hacer?”  
**English:** “What changes when a system changes what it can do?”

Opening copy should explain that a system is defined by more than its current state: its accessible transformations and the conditions shaping them also matter.

### 3.1 From the Home insight to a more precise question

Home introduces the central intuition: a system's possibilities can change when relevant conditions change. Explore should not repeat that discovery. It begins one step further:

**How do we determine whether a transformation is actually within a system's reach?**

Answering this requires more than listing what a system might do. We must identify the system and its boundary, the conditions being considered, and the transformations that are candidates within that analytical context.

**Visual direction:** Reuse the Home system illustration only as a small point of reference. Introduce a clearer analytical frame around system boundary, conditions and candidate transformations.

### 3.2 Candidate does not mean accessible

Return briefly to the software-configuration migration introduced on Home. The operation being considered is the same in both environments. For this illustrative comparison, keep the system/configuration, operation, boundary assumptions and all other specified relevant prerequisites constant; the single difference being examined is that the required dependency is available in environment A and missing in environment B. This isolates the dependency's availability as the condition associated with the accessibility contrast; it does not establish that dependency availability is the only factor that could matter in a real migration.

The operation can therefore be considered a candidate transformation in both environments, while being accessible only in A under the conditions shown.

A **candidate transformation** is a change considered as a possibility for a system within an analytical context. Being considered a candidate does not mean that the system meets the conditions required to carry it out.

**Key message:** A transformation may be a candidate without being accessible.

**Visual direction:** A concise side-by-side comparison, not a retelling of the full migration story. Keep the candidate transformation identical; show only the dependency condition and resulting accessibility status as different.

### 3.3 Accessibility depends on conditions and boundaries

The missing dependency in environment B illustrates one way accessibility can change. When that dependency is made available in the target environment, while the other specified conditions remain as assumed in the illustration, the transformation may become accessible under the revised conditions.

This conclusion is bounded: it concerns the specified system, transformation, boundary and conditions. It does not establish that the transformation has been executed, that it will succeed, or that its outcome will have value.

In English, introduce the analytical term **accessibility of transformations**. It refers to whether a transformation is within a system's reach under the system boundary and conditions being considered; it does not refer to digital or interface accessibility.

**Key message:** Accessibility is assessed relative to a system, its boundary and the conditions being considered.

**Visual direction:** Show the target environment before and after the dependency becomes available. Mark only the accessibility status as changed; do not depict execution or success.

### 3.4 Possibility, execution, outcome and value

Introduce the distinction through a visitor-facing question: if the operation is now within reach, what can actually be claimed — that the system can perform it, that it has performed it, or that it has achieved something valuable?

Keep the following distinction explicit and visually prominent:

**Accessibility → Execution → Outcome → Value**

- **Accessibility:** a transformation is within the system's reach under the boundary and conditions being considered; this does not mean it has been performed.
- **Execution:** the system actually performs the transformation.
- **Outcome:** the state or effect produced as a consequence of execution.
- **Value:** the relevance or contribution of that outcome, assessed against a particular context and set of criteria.

The **candidate transformation** is the object considered before this sequence: its accessibility is assessed, but being a candidate does not mean it is accessible.

Explain that accessibility does not imply execution; execution does not guarantee the expected outcome; and an outcome does not carry the same value in every context.

Make the practical implication explicit without promising value: when accessibility changes, the set of options within the system's reach changes too. This may open new ways to act or design an intervention, but deciding whether an option is useful or desirable requires additional objectives and contextual criteria.

Introduce **trajectory** separately: transformations may be connected and may shape what the system can do next. A trajectory describes the system's evolution through states and transformations. It is not a synonym for outcome and should not be shown as a sixth stage in a universal linear causal chain.

**Key message:** A change in accessibility changes what is within the system's reach; it does not, by itself, establish what should be done or guarantee a favourable outcome or value.

**Visual direction:** Make **Accesibilidad → Ejecución → Resultado → Valor** (English: **Accessibility → Execution → Outcome → Value**) a persistent, high-visibility visual anchor. Place “Candidate transformation” before the sequence as the object being assessed. Show trajectory as a path across states and transformations, not as a fifth stage or a terminal step. Keep these relationships clear in both static diagrams and responsive/mobile layouts.

### 3.5 A system's space of possibilities

Open with the highlighted question:

**What new options become available when a system can do something that was previously beyond its reach?**

The Spanish equivalent is: **«¿Qué nuevas opciones aparecen cuando un sistema puede hacer algo que antes no estaba a su alcance?»**

Build the explanation around one central idea: a system's possibilities cannot be understood by adding up the capabilities of its components in isolation. What matters is also how those elements are connected, what they depend on, how they interact, and under which internal and external conditions they can work together.

Use three visitor-friendly lenses, not a closed checklist:

1. **What is present and what can each element do?** Components may have different capabilities; resources and dependencies may or may not be available.
2. **How are the elements connected?** Interfaces, relationships and interactions can allow elements to work together, or prevent a transformation even when the individual components exist.
3. **Under what conditions can they operate?** Rules, permissions, constraints and environmental conditions can enable, limit or block particular transformations.

Return briefly to the migration illustration without changing its controlled premise: the same operation and stated assumptions, with the required dependency available in A and missing in B. The example shows why the presence of individual components is not enough if a required dependency is absent. It remains a bounded illustration, not a general model of every migration.

Explain that these dimensions are relational rather than independent. A change in one condition can alter a dependency, make a connection usable or unavailable, and consequently enable one transformation while constraining another. Possibilities can therefore open, close or be reorganised; their expansion is not automatically beneficial.

Introduce **Systems Thinking** as the perspective that helps examine system boundaries, relationships, dependencies, conditions and dynamics together. Avoid implying that the visitor must master a formal method to understand the point.

**Key message:** A system's possibilities depend not only on what its elements can do individually, but also on how they are related and on the conditions under which they can work together.

**Visual direction:** Show a small system with components, a dependency between two of them and one external condition. Make the relationship legible: the components may be present, but the transformation remains out of reach while the required dependency is unavailable. Show that changing a condition can alter the relationship and the accessibility of a transformation. Do not use a dense network, a universal factor checklist or a diagram suggesting every connection is beneficial.

### 3.6 A new way to understand and guide transformations

Explain three complementary but non-equivalent contributions:

- **Systems Thinking — understanding systems:** a perspective for examining boundaries, relationships, conditions, constraints, feedback and dynamics. It helps build a connected understanding of the system rather than treating elements in isolation.
- **Systems Engineering — designing and intervening:** an established engineering discipline with methods and practices for modelling, designing, developing, integrating and intervening in engineered systems.
- **Transformational Intelligence — integrating reasoning about change:** a working concept of an integrative capability under development. It seeks to connect system understanding with reasoning about candidate transformations, changes in accessibility, possible trajectories and the consequences of alternative interventions.

Make the intended integration concrete but provisional: the concept asks how we can understand a system, examine what transformations may be within its reach under specified conditions, consider how those possibilities and trajectories may change, and reason about how to guide such change. Do not imply that a complete method, operational capability or validated product already exists.

State explicitly that Transformational Intelligence is not a synonym for artificial intelligence, a new name for Systems Thinking or Systems Engineering, or a consolidated academic discipline. AI may be one possible supporting technology, not its definition.

Position TGCV accurately: **TGCV is the applied research and innovation programme whose research question contributes to the foundations for developing and examining this capability concept.** TGCV and Transformational Intelligence are related but not equivalent: the programme investigates how transformations available to systems may change and how this may contribute to value construction; TI is a capability concept that seeks to integrate understanding, reasoning and guidance around such changes. Do not imply that TGCV has already validated TI.

**Key message:** The aim is not only to understand systems or to intervene in them, but to develop ways of reasoning about changes in what systems can do and how those changes might be guided.

**Visual direction:** Show Systems Thinking as a perspective and Systems Engineering as an established discipline contributing complementary foundations. Place Transformational Intelligence as the integrative capability concept under development, not as a third equivalent discipline. Show TGCV as the research programme contributing questions, models and evidence to its development. Mark the maturity of the TI concept clearly.

## 4. Visitor routes

At the end of Explore, provide clear routes:

- **Research** — foundations, models, questions and research directions.
- **Systems Engineering** — systems-engineering practices for modelling, designing and developing systems.
- **Transformational Intelligence** — the working capability concept and its development.

These destinations must be populated with accurate, useful content before their links are published. Do not promise a simulator, Playground, community, collaboration workflow or application that is not available.

## 5. Visual and interaction constraints

- Prefer a small set of static, accessible diagrams or annotated states.
- No bespoke interactive simulator is required for the germinal release.
- Keep the same software-migration example consistent across sections and languages.
- Label the example as illustrative; it is not an executed experiment, validated application, Juguete Colectivo feature or C10-S result.
- Distinguish source and target environments, the changed condition and the resulting accessibility status.
- Show that possibilities can open, close or be reconfigured; do not imply that more accessible transformations are always better.
- Do not imply autonomous change: conditions may change through intervention, system dynamics or the surrounding environment.
- Provide text alternatives and ensure that status distinctions are not conveyed by colour alone.
- Keep visual and interaction choices responsive, keyboard accessible and compatible with reduced-motion preferences.

## 6. Language and terminology

The first public release is Spanish and English. Both versions must be complete and conceptually equivalent, not literal translations.

Maintain the following terms:

| Spanish | English | Editorial note |
|---|---|---|
| Transformación candidata | Candidate transformation | Do not use as a synonym for feasible or accessible. |
| Transformación accesible | Accessible transformation | Explain that accessibility is relative to the system boundary and conditions being considered. |
| Accesibilidad de las transformaciones | Accessibility of transformations | On first English use, clarify the TGCV meaning to avoid confusion with digital/interface accessibility. |
| Ejecución | Execution | Actual performance of a transformation. |
| Resultado | Outcome | Use consistently in this explanatory context. |
| Trayectoria | Trajectory | Evolution through states and transformations; not an isolated outcome. |
| Valor | Value | Contextual assessment, not an automatic consequence. |
| Inteligencia Transformacional | Transformational Intelligence | Working capability concept under development. |

In English, prefer “within the system's reach” in visitor-facing prose where it improves readability. Use “accessibility of transformations” when introducing the analytical concept. Avoid “integrated intelligence” as a substitute for “integrative capability”.

## 7. Editorial and scientific guardrails

Do not:

- imply that candidate transformations are necessarily feasible or accessible;
- imply that accessibility entails execution;
- imply that execution guarantees success, a favourable outcome or value;
- present trajectory as a synonym for outcome or as a mandatory linear stage after value;
- obscure or omit the visible sequence **Accessibility → Execution → Outcome → Value**; candidate transformation must be positioned before it, while trajectory is represented across states and transformations;
- suggest that expanding the accessible set is always desirable;
- present the list of accessibility conditions as exhaustive or independent;
- imply that the system must autonomously initiate changes in its possibilities;
- equate TGCV with Transformational Intelligence;
- present TI as a validated discipline, product or generally demonstrated capability;
- present the illustrative migration as an existing execution, application, experiment or Juguete Colectivo function.

The page is an introductory explanation, not a formal definition of TGCV's transformation space or a substitute for Research.

## 8. Comprehension review and acceptance

Before publication, review Explore together with the full web experience. Simulate representative visitor profiles and, when an external group is viable, test with real visitors. External testing is desirable, not a mandatory publication gate.

A qualitative review should check whether visitors can explain, without coaching:

1. why a system is more than its current state;
2. the difference between a candidate and an accessible transformation;
3. how conditions can change accessibility;
4. why accessibility, execution, outcome and value are distinct;
5. what trajectory means in this context;
6. why system relationships and conditions matter;
7. where to go next.

A visitor should be able to retell the software example without concluding that the operation was executed or that value was demonstrated.

This is an editorial comprehension review, not a representative survey or scientific experiment.

## 9. Status and release checks

**Status: WORKING EXPERIENCE SPECIFICATION — NOT APPROVED FOR PUBLICATION.**

Before publication:

- the Spanish and English copy is complete and conceptually equivalent;
- the example is clearly marked as illustrative and bounded;
- diagrams preserve the distinctions and do not imply unsupported causal claims;
- terminology is consistent with Home and Research;
- links lead to real, populated destinations;
- scientific wording and evidence references are checked against current canonical sources;
- responsive behaviour, accessibility, privacy and maintainability are reviewed.

### Version history

- **0.1 — 2026-11-24:** Initial Explore experience specification.
- **0.2 — 2026-11-24:** Repositions Explore as a conceptual deepening of Home, fixes the example to one missing dependency, broadens the candidate-transformation definition beyond software operations, and clarifies the bounded meaning of accessibility.
- **0.3 — 2026-11-24:** Refreshes related Home document versions after the trajectory-visual reconciliation.
- **0.4 — 2026-11-24:** Adds a visitor-facing explanation of the practical implication of changed accessibility, clarifies that accessibility means being within reach rather than execution, and refines trajectory wording to avoid implying that transformations always form a chain.
- **0.5 — 2026-11-24:** Requires the block-5 question in both languages and a persistent visual anchor for Accessibility → Execution → Outcome → Value, with candidate transformation before the sequence and trajectory across states and transformations.


- **0.6 — 2026-11-25:** Refreshes Home and Explore Copy references to their current versions after the integrated bilingual identity review.

- **0.7 — 2026-11-25:** Makes the illustrative comparison's control assumptions explicit: the same operation and stated boundary/prerequisites are held constant while one dependency-availability condition differs; limits the inference to that bounded illustration.

- **0.8 — 2026-11-25:** Reframes the space-of-possibilities explanation around component capabilities, relationships/dependencies and operating conditions; uses three visitor questions and reconnects the controlled migration example without implying a universal checklist.

- **0.9 — 2026-11-25:** Clarifies Transformational Intelligence as an integrative capability concept under development; distinguishes its intended role from Systems Thinking, Systems Engineering, AI and the TGCV research programme, and avoids implying an operational or validated capability.
