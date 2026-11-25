# TGCV — Home Experience Specification

**Identifier:** TGCV-WEB-HOME-001  
**Version:** 1.5  
**Date:** 2026-11-24  
**Status:** STRATEGIC EXPERIENCE SPECIFICATION — WORKING DRAFT  
**Parent:** `06_WEB/TGCV_WEB_MASTER_BRIEF_v0.1.md`, §21  
**Related:** `06_WEB/TGCV_WEB_INFORMATION_ARCHITECTURE_v0.1.md`, §16–17; `06_WEB/TGCV_WEB_HOME_COPY_v0.1.md`, v0.9; `06_WEB/TGCV_WEB_EXPLORE_EXPERIENCE_v0.1.md`; `06_WEB/TGCV_WEB_EXPLORE_COPY_v0.1.md`  
**Branch:** `strategy/tgcv-web-master`

---

## 1. Purpose and authority

This document specifies the visitor experience, content hierarchy, explanatory sequence and visual requirements for the first public Home page of TGCV. It is an editorial and experience-design artifact. It does not modify TGCV's scientific Core, canonical definitions, evidence status, execution authorization or research priorities.

The approved decisions in Web Master Brief §21 govern this specification. If any future copy or design conflicts with those decisions, the conflict must be resolved before publication.

The Home is the entrance to an interdisciplinary research and systems-engineering ecosystem. It is not a consultancy landing page, an AI-company homepage, a product launch page or an institutional brochure.

## 2. Primary visitor and intended understanding

### 2.1 Primary visitor

Address people who research, design, develop or engineer systems. Keep the explanation accessible to adjacent audiences and interested newcomers who do not know TGCV.

### 2.2 Intended understanding

After engaging with the Home, a visitor should be able to explain in ordinary language that:

1. a system has a current state and operates under particular conditions;
2. those conditions shape which candidate transformations are accessible;
3. changing relevant conditions can open, close or reorganise accessible transformations;
4. accessibility does not mean that a transformation is executed;
5. a realised transformation may change the system's state and its subsequent possibilities;
6. outcomes and value require separate evaluation;
7. when new transformations become accessible, new options and possible paths emerge, creating opportunities for value without guaranteeing execution, favourable outcomes or value.

The visitor should also understand where to go next according to their interests.

## 3. Identity architecture to communicate

### 3.0 Public name and Home placement

The site-wide header/brand lockup is **TGCV — Transformaciones Generativas y Construcción de Valor**. In English use **TGCV — Generative Transformations and Value Construction**; TGCV remains the proper name. The full descriptor belongs in the footer and relevant About/Research identity blocks. Do not insert a long institutional self-description before the opening question. On narrow screens the wordmark may prioritise “TGCV”, provided the full name remains available accessibly.

“Generative” refers to transformations that can change what systems can do or access. Do not let the name imply that TGCV is only about generative AI, content generation or autonomous self-modification.

The Home must not display three equivalent discipline cards or imply three separate departments.

### 3.1 Transformational Intelligence — integrative axis

Transformational Intelligence (TI) is the ecosystem's integrative conceptual axis: the capability being explored to understand, reason about and orient transformations in systems. Present it as a working concept/capability under development, not as a consolidated academic discipline or generally validated capability.

### 3.2 Systems Thinking — perspective for understanding

Systems Thinking contributes the perspective for understanding systems, their boundaries, conditions, relationships, dynamics and possibilities. Its role is transversal: visible on Home, explained in Explore and developed further in Research. It is not a separate first-release navigation destination.

### 3.3 Systems Engineering — discipline for design and intervention

Systems Engineering contributes established practices for modelling, designing, developing, integrating and intervening in systems and their transformations. Do not invent or imply a validated proprietary TGCV engineering lifecycle.

### 3.4 Activity spaces

**Research** develops questions, conceptual foundations, models, methods, experiments and evidence.

**Labs & Applications** hosts or presents bounded experiments, demonstrators and exploratory application contexts, with their actual maturity and evidence limitations made explicit.

Research and Labs & Applications inform one another. They are activity spaces, not additional conceptual pillars or promises of staffed physical laboratories.

## 4. Approved narrative sequence

The Home follows this order:

1. **Question:** What would need to change for a system to do something it cannot do today?
2. **Discovery:** «Las posibilidades de un sistema también pueden cambiar» / “A system's possibilities can change, too.” Explain that this happens when relevant conditions change; it need not be an autonomous change initiated by the system itself.
3. **Second visitor question and concise answer:** «¿Qué nuevas opciones aparecen cuando un sistema puede hacer algo que antes no estaba a su alcance?» / “What new options become available when a system can do something that was previously beyond its reach?” Explain that newly accessible transformations create new options and possible paths, which may open opportunities for value but do not guarantee that they will be realised or valuable.
4. **Tangible example:** a software configuration considered across two different environments.
5. **Conceptual explanation:** conditions, candidate transformations, accessibility, transition, new state and possibilities, trajectories, outcomes and value.
6. **Ecosystem:** TI as the integrative capability, supported by Systems Thinking as a perspective and Systems Engineering as a discipline.
7. **Exploration:** direct routes to the relevant sections, without forcing a linear journey.

Do not add a separate generic “What is transformation?” introduction before the approved question. Do not lead with institutional self-description.

## 5. First-screen experience

### 5.1 Opening question

**¿Qué tendría que cambiar para que un sistema pudiera hacer algo que hoy no puede hacer?**

English equivalent:

**What would need to change for a system to do something it cannot do today?**

### 5.2 Working headline

**Comprende cómo cambian las posibilidades de un sistema.**

English equivalent:

**Understand how a system's possibilities can change.**

### 5.3 Supporting copy

Spanish:

Un sistema no solo cambia cuando pasa de un estado a otro. También puede cambiar qué transformaciones tiene a su alcance y abrir trayectorias diferentes.

English:

A system does not only change when it moves from one state to another. The transformations within its reach can also change, opening up different trajectories.

### 5.4 Primary action

**Explora el enfoque / Explore the approach** → Explore.

Secondary links may lead to Research and Systems Engineering. The Home must not use a “See it in action” action unless a specific demonstrator is available, accessible and accurately described at publication time.

### 5.5 Hero visual

Use a clear static explanatory visual, not stock photography or decorative AI imagery. It should show a bounded system, relevant conditions, candidate transformations, an initial accessibility pattern, a change in conditions, and a resulting pattern in which some transformations become accessible while others may remain inaccessible or become unavailable.

The visual should communicate change in what is possible next, not merely a before/after state change. It must be understandable without interaction and accompanied by an equivalent text explanation.

## 6. Tangible example: software configuration across environments

The Home uses a bounded illustrative scenario: a software configuration considered across a source environment and a target environment with different dependencies, resources, permissions or configuration conditions.

The example must make this sequence explicit:

1. **Source environment:** a specified operation is accessible under the declared configuration and dependencies.
2. **Target environment:** the required dependency is absent.
3. **Before intervention:** under those target conditions, the same operation is not accessible.
4. **Change of condition:** the missing dependency is made available in the target environment.
5. **After intervention:** the operation becomes accessible under the changed target conditions, but has not thereby been executed.

The explanatory point is the change in accessibility caused by a change in conditions. Do not imply that copying a configuration automatically transfers all capabilities between environments.

Accessibility still does not establish that the operation is executed, succeeds, produces a favourable outcome or creates value. Do not invent detailed technical parameters that are not needed to explain the concept.

Use this example as an explanatory illustration only. It is not an existing execution, a validated application, a feature of Juguete Colectivo or evidence from C10-S.

## 7. Conceptual sequence on Home

Use plain language and a compact visual sequence:

1. **System and conditions** — What system are we considering, where are its boundaries, and under what conditions does it operate?
2. **Candidate transformations** — What changes or transitions are relevant to this system and context?
3. **Accessibility** — Which candidate transformations are available under the stated conditions and decision boundary?
4. **Realised transition** — Which transformation is actually carried out?
5. **New state and possibilities** — How does the system change, and what becomes accessible from the resulting state?
6. **Trajectory** — What sequence of transitions is possible or has occurred?
7. **Outcome and value** — What happens, and how is it evaluated under independently specified criteria?

This numbered sequence is an explanatory reading aid, not a universal linear causal chain. **Trajectory** must be represented as the path formed by states and transitions (including possible and realised transitions), spanning the sequence rather than as a separate box or stage between the new state and outcome/value.

The central guardrail is:

**Possible, accessible, realised and valuable do not mean the same thing.**

Do not suggest that accessible transformations are necessarily executed, that an expanded accessible set is always better, or that value follows automatically.

## 8. Ecosystem presentation

Use a relational composition, not four equal cards.

Suggested order:

- **Transformational Intelligence** — the integrative capability and conceptual axis.
- **Systems Thinking** — the perspective for understanding systems and their dynamics.
- **Systems Engineering** — the discipline for modelling, designing and intervening in systems.

Use the line:

**Una capacidad integradora, apoyada en dos bases complementarias.**

English:

**An integrative capability, supported by two complementary foundations.**

The accompanying explanation must make the different roles explicit: TI is the integrative capability; Systems Thinking is a perspective; Systems Engineering is a discipline. They are not three equivalent perspectives or disciplines.

Then show the two activity spaces:

- **Research** — concepts, models, methods, experiments and evidence.
- **Labs & Applications** — demonstrators, bounded experiments and exploratory application contexts.

## 9. Application contexts

If space and current content justify it, show a small selection of candidate contexts, labelled **Exploratory**. Possible examples include AI agents and tools, industrial and cyber-physical systems, energy and mobility, distributed infrastructure and interinstitutional systems.

Each item must be phrased as a question TGCV may help investigate, not as a validated deployment, customer case, proven solution or demonstrated impact. Do not include a context merely to fill a visual grid.

## 10. Visitor routes and navigation

Approved first-release navigation:

- Explore
- Research
- Systems Engineering
- Transformational Intelligence
- **Value Construction**
- Labs & Applications
- About
- Contact

Systems Thinking is transversal: Home, Explore and Research. It has no independent first-release page.

Home should offer a primary route to Explore, with secondary routes to Research and other destinations. Visitors may enter any destination directly; no mandatory linear journey is imposed.

Explore must take the Home example as its starting point and add conceptual depth: clarify how candidate transformations are distinguished from accessible ones, how accessibility depends on a defined system boundary and conditions, and how accessibility differs from execution, outcome and value. Do not replay the full Home narrative. About explains purpose, scope and governance without implying a staffed institute, external board or formal consortium. Contact is shown only when a real monitored channel and proportionate privacy information are in place.

## 11. Languages

The first public release is Spanish and English. Both versions must be complete and conceptually equivalent. Adapt idiom, syntax and terminology naturally; do not translate literally when that would make either version awkward or misleading.

Do not publish a partial language version or a language switch that leads to missing content.

## 12. Efecto Ajá and quality review

Efecto Ajá is a desired quality objective, not a mandatory publication gate.

Before publication, conduct an integral review of the full experience: conceptual accuracy, narrative sequence, example, visual explanation, visitor orientation and representative visitor-profile simulations. When an external group is viable, add real visitor testing. Lack of external testing alone does not block publication.

A useful qualitative review asks whether visitors can explain:
- what question TGCV explores;
- how conditions affect what transformations are accessible;
- why accessibility differs from execution;
- what they would explore next.

This is an editorial comprehension review, not a representative survey or scientific experiment.

## 13. Mandatory release checks

Before publication:

- Identity and audience are coherent with the approved architecture.
- The opening question and example explain changed possibilities without excessive jargon.
- The example explicitly distinguishes source and target conditions, the change that is made, and the resulting accessibility.
- The example is clearly illustrative and is not confused with an existing demonstrator.
- Accessibility, execution, trajectory, outcome and value remain distinct.
- TI, Systems Thinking, Systems Engineering, VALUE, ValueLabOS and Labs & Applications have distinct, accurate roles.
- The ecosystem map is accessible, understandable without interaction and does not imply a proven causal chain.
- Research and Labs & Applications content is real, bounded and labelled honestly.
- Existing, In development and Exploratory are used as operational content-maturity labels where useful; they are not scientific evidence grades.
- Scientific claims are checked against current canonical sources and evidence state.
- All destinations, links and any Contact route work as described.
- Spanish and English are complete and equivalent.
- Accessibility, responsive behaviour, privacy and maintainability have been reviewed.

External Efecto Ajá testing is desirable, not a release stopper.

## 14. Visual and interaction constraints

The first Home does not require a custom simulator, interactive widget or future Playground. Prefer a static, accessible diagram or a small sequence of annotated visual states.

The visual language may use system boundaries, nodes, components, transformation links, conditions, branching trajectories and before/after accessibility patterns. Show both opening and restriction/reconfiguration; do not depict possibility expansion as inherently positive.

Do not imply that the future Playground is available. Do not duplicate Juguete Colectivo with a second miniature simulator on Home.

## 15. Status

**Status: WORKING EXPERIENCE SPECIFICATION — NOT APPROVED FOR PUBLICATION.**

The second visitor question is a required Home content block, positioned immediately after the initial discovery and before the tangible example. Its answer must remain short and visitor-facing; Explore retains the detailed explanation of system elements, relationships, conditions and accessibility.

The conceptual decisions are approved. Final design, current evidence review, asset verification, bilingual editorial QA, contact readiness and accessibility/responsive checks remain publication work.

### Version history
- **1.0 — 2026-11-24:** Adds the second visitor question as a required Home discovery/payoff block, with a concise answer linking new options to possible value while explicitly avoiding a guarantee. Updates the bilingual Home Copy reference.
- **0.9 — 2026-11-24:** Clarifies that the Home sequence is a reading aid and specifies trajectory as a path across states and transitions, not a discrete sequential stage.
- **0.8 — 2026-11-24:** Fixes the Home migration example to one missing dependency in the target environment and clarifies the distinct deepening role of Explore.

- **0.6 — 2026-11-24:** Clarifies that changes in a system's possibilities need not be autonomous; corrects the TI/Systems Thinking/Systems Engineering hierarchy; specifies the source-to-target example as a change in accessibility, not automatic capability transfer.
- **0.5 — 2026-11-24:** Rewritten as a clean experience specification; removes superseded four-pillar narrative and earlier navigation assumptions; integrates the approved audience, identity, example, routes, bilingual requirement and non-blocking Efecto Ajá review.
- **0.4 — 2026-11-24:** Decision-lock layer added to the prior working concept.


## 16. Public identity decision (2026-11-24)

The Home presents the initiative as **TGCV — Transformaciones Generativas y Construcción de Valor**, a programme of applied research and innovation.

Approved Spanish descriptor:
*Un programa de investigación aplicada e innovación sobre cómo la ampliación de las posibilidades de transformación de los sistemas puede contribuir a la construcción de valor.*

Approved English rendering:
**TGCV — Generative Transformations and Value Construction**.
*A programme of applied research and innovation exploring how expanding the transformations available to systems may contribute to value construction.*

Use “programme of applied research and innovation” / “programa de investigación aplicada e innovación”, not “theory” / “teoría”, as the public description of TGCV. The Spanish expansion is canonical; TGCV remains the proper name in English. The identity must not imply that expanded accessibility or possibilities automatically produce execution, outcomes or value.

This is a public editorial decision only. It does not alter scientific definitions, evidence status or repository identifiers.

### v1.1 — 2026-11-24
- Aligns the Home experience identity and first-mention description with the approved TGCV public name and research-programme positioning.


## 17. Integrated Home identity review (2026-11-24)

The Home uses the approved site-wide brand lockup **TGCV — Transformaciones Generativas y Construcción de Valor**. English rendering: **TGCV — Generative Transformations and Value Construction**. The full approved applied-research-and-innovation programme descriptor remains in the footer and relevant About/Research identity blocks; it must not displace the opening question or create a long institutional preamble.

The required narrative order is: opening question → discovery → second question and concise answer → tangible software-configuration example → conceptual explanation → ecosystem → exploration. This corrects the earlier ordering in §4 and aligns the specification with the approved Home Copy.

The word “Generative” refers to transformations that can change what a system can do or access. It is not a synonym for generative AI or content generation, and it does not imply autonomous self-modification. Relevant conditions may change through intervention, system dynamics or environmental change.

The identity and copy are directionally coherent. Publication remains blocked pending the checks listed in §13 and the visual/asset work described in this specification.

### v1.2 — 2026-11-24
- Aligns the Home sequence with the approved order, placing the second question before the tangible example.
- Adds site-wide brand-lockup placement and meaning controls for “Generative”.
- Updates the Home Copy dependency to v0.9.

### v1.3 — 2026-11-24
- Adopts the public descriptor “investigación aplicada e innovación” and its English equivalent.
- Clarifies that Home's concise discovery answer should describe newly accessible transformations, not imply that accessibility means execution.
- Updates the public positioning from research programme to applied research and innovation programme.

### v1.4 — 2026-11-24
- Refines the Home supporting copy to foreground changes in accessible transformations rather than capability acquisition.
- Updates the current Home Copy reference to v1.1.

### v1.5 — 2026-11-25
- Adds Value Construction as a first-release visitor destination after Transformational Intelligence.
- Replaces the earlier simplified ecosystem composition with a visitor-facing conceptual map distinguishing TGCV, Systems Thinking, Systems Engineering, Transformational Intelligence, VALUE/Value Construction, Labs & Applications and the proposed ValueLabOS ecosystem.
- Requires labelled, non-causal relationships and makes the map reachable from Home and relevant pages without displacing the opening narrative.
