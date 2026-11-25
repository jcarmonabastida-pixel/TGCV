# TGCV — Web Information Architecture
**Identifier:** TGCV-WEB-IA-001  
**Version:** 2.3  
**Date:** 2026-11-25  
**Status:** STRATEGIC DESIGN — WORKING DOCUMENT  
**Parent reference:** `06_WEB/TGCV_WEB_MASTER_BRIEF_v0.1.md`  
**Branch:** `strategy/tgcv-web-master`  
**Purpose:** Convert the approved working orientation of the TGCV Web Master Brief into a coherent information architecture, navigation model, page system and staged publication plan.  
**Authority:** This is a web-design artifact. It does not modify TGCV scientific governance, canonical definitions, evidence status or execution authorization.

---

> **Current editorial authority (2026-11-24):** the approved decision-lock section at the end of this document is authoritative for the first public web release. It supersedes any earlier working text that conflicts with the approved audience, identity architecture, Home narrative, software-migration illustration, first-release navigation, Spanish/English requirement or non-blocking Efecto Ajá status. Earlier material is retained as design history until the next full editorial rewrite; it must not be treated as current instruction where it conflicts with the decision lock.

## 0. Executive decision

The website should be designed as the public interface of an interdisciplinary research, systems-engineering and experimentation ecosystem focused on systems and their transformation spaces.

It must not be structured as a conventional consultancy website, an AI agency website, or a product landing page.

The information architecture follows this editorial progression:

`SYSTEMS → TRANSFORMATIONS → TRANSFORMATION-SPACE DYNAMICS → TRANSFORMATIONAL INTELLIGENCE → SYSTEMS ENGINEERING & EXPERIMENTATION → APPLIED SYSTEMS`

The website has two simultaneous jobs:

1. **Explain:** make the intellectual object, research programme and engineering orientation understandable.
2. **Enable exploration:** let visitors inspect research, methods, demonstrators, application contexts, tools and opportunities to participate.

The website should reveal the system behind the ecosystem, not merely list its departments.

## 1. Primary audiences and their questions

Audience definitions are provisional working hypotheses. They should be validated through interviews and usage evidence before being treated as established market segments.

| Audience | Primary question | Content they need | Desired next step |
|---|---|---|---|
| Systems researchers and academics | What is the research object and what is scientifically established? | TGCV, concepts, formal models, evidence, limitations, publications | Examine research and evidence |
| Systems engineers and architects | How can this perspective help model or reason about a system? | System boundaries, transformations, dependencies, constraints, engineering methods | Explore methods or a technical demonstrator |
| AI and software systems practitioners | How do tools, permissions, resources and environments alter what agents/systems can do? | Agentic systems, infrastructure, access conditions, trajectory examples | Inspect a case or experiment |
| Complex-systems and interdisciplinary researchers | How does the approach transfer across domains? | Application-Fit, cross-domain patterns, case comparisons | Explore an application domain |
| Developers and technical collaborators | What can be tested, reused, integrated or contributed? | Open Playground, tools, connectors, specifications, repositories | Try, inspect or contribute |
| Institutions and organisations with complex systems | Is there a relevant problem that can be represented and explored? | Applied Systems, case method, boundaries and evidence limits | Propose a scoped exploration |
| Students and wider curious audience | What does this mean, and can I see it working? | Clear introduction, visual explanations, glossary, interactive examples | Learn and explore |

Do not assume all audiences need the same entry point. The site should support both a conceptual route and a practical route.

## 2. Navigation model

### 2.1 Recommended top-level navigation

Keep the primary navigation compact. Use six principal destinations:

1. **Explore** — a guided entry into the core ideas and interactive explanations.
2. **Research** — TGCV, transformation-space dynamics, scientific programme and evidence.
3. **Engineering** — systems thinking, systems engineering, modelling and methods.
4. **Intelligence** — Transformational Intelligence: concepts, capabilities and technical work.
5. **Labs & Applications** — simulation, demonstrators, Application-Fit and applied systems.
6. **Community** — learning, participation, collaboration and open resources.

A persistent **About** destination may sit at the end of the navigation or in the footer, depending on visual design. Search can be added when content volume justifies it.

### 2.2 Sitemap

```text
/
├── Explore
│   ├── The central question
│   ├── How systems transform
│   ├── Transformation spaces
│   ├── A guided example
│   └── Glossary
│
├── Research
│   ├── TGCV
│   ├── Transformation-space dynamics
│   ├── Concepts and definitions
│   ├── Research programme
│   ├── Experiments and evidence
│   └── Publications and working papers
│
├── Engineering
│   ├── Systems thinking
│   ├── Systems engineering
│   ├── System modelling
│   ├── Cross-domain architecture
│   └── Methods and specifications
│
├── Intelligence
│   ├── Transformational Intelligence
│   ├── Reasoning over transformation spaces
│   ├── Navigation
│   ├── Adaptation
│   ├── Trajectory orientation
│   └── Technical explorations
│
├── Labs & Applications
│   ├── Labs and simulation
│   ├── Demonstrators
│   ├── Open Playground
│   ├── Application-Fit
│   │   ├── Cross-domain patterns
│   │   └── Candidate cases
│   └── Applied Systems
│       ├── Distributed networks
│       ├── Agentic AI systems
│       ├── Industrial and cyber-physical systems
│       ├── Energy and mobility
│       └── Socio-technical and public systems
│
├── Community
│   ├── Learning resources
│   ├── Participate
│   ├── Collaborate
│   └── Events / updates (when available)
│
└── About
    ├── Ecosystem
    ├── Relationship with TGCV
    ├── Principles and governance
    └── Contact
```

This is a target content model, not a commitment to publish every page in the first release. Empty or speculative pages should not be published merely to fill the menu.

## 3. Page roles and content briefs

### 3.1 Home

**Role:** communicate the identity, central question and routes into the ecosystem within the first screen and first scroll.

**Working headline:**  
*Understanding and engineering how systems transform.*

**Working subheading:**  
*Research, systems engineering and transformational intelligence for exploring how systems change, what becomes possible, and how future trajectories unfold.*

**Required content blocks:**
1. The central question: systems change, and so does what they can do.
2. A simple visual of the transformation sequence.
3. Three entry routes: Research, Engineering, Explore.
4. A current featured experiment or demonstrator, with evidence status.
5. Selected application domains as examples, not as a sector catalogue.
6. Invitation to explore, collaborate or follow the work.

**Avoid:** generic claims such as “unlock your potential”, “revolutionise your business”, “create value through AI”, or claims of universal predictive capability.

### 3.2 Explore

**Role:** teach the central idea without requiring prior knowledge of TGCV.

A guided narrative should distinguish:
- system and system boundary;
- state and context;
- candidate transformations;
- accessibility conditions;
- transformations actually performed;
- successor states and trajectories;
- outcomes and contextual value.

Use one carefully bounded example, ideally an interactive synthetic system. Make clear what is illustrative and what is evidence.

### 3.3 Research

**Role:** provide the scientifically disciplined account.

Core pages:
- TGCV: research programme, object and scope.
- Transformation-space dynamics: concepts and current formalisation status.
- Research programme: questions, hypotheses and experimental lines.
- Evidence: claims, supporting evidence, limitations and open questions.
- Publications and working papers: versioned artefacts with status labels.

Every research page must identify whether content is canonical, a working proposal, a hypothesis, a synthetic demonstration, an empirical result or a superseded item. Link to canonical repository artefacts where possible.

### 3.4 Engineering

**Role:** show how the conceptual perspective connects with systems-engineering practice.

Content should cover:
- system-of-interest and boundary definition;
- states, interfaces and subsystems;
- dependencies and constraints;
- transformation and admissibility modelling;
- domain connectors and semantic translation;
- scenario design, verification and validation;
- comparison against conventional domain baselines.

Do not imply TGCV replaces established systems-engineering standards, methods or domain models.

### 3.5 Intelligence

**Role:** explain Transformational Intelligence as a functional capability, not as a synonym for AI.

Present the four working capabilities:
1. Reasoning over transformation spaces.
2. Navigation among accessible transformations.
3. Adaptation as states and accessible spaces change.
4. Trajectory orientation under an independently specified outcome/value model.

Show how AI may support or instantiate parts of this capability, while remaining only one possible enabling technology.

### 3.6 Labs & Simulation

**Role:** make the work inspectable through experiments, models and demonstrators.

Each item must have a visible status:
- Concept
- Design
- Synthetic prototype
- Executed
- Audited
- Empirical pilot
- Deployed

A status must not be inferred from visual polish or a successful software run. Each demonstrator page should include purpose, system boundary, assumptions, inputs, method, output, baseline, limitations, provenance and reproducibility information.

TSTC v004 may be presented as a bounded synthetic methodological demonstrator. It must not be presented as empirical validation, proof of causal propagation in real systems or evidence of universal applicability.

### 3.7 Application-Fit and Applied Systems

**Role:** show where the analytical perspective may be useful and how fit is assessed.

Organise content by transformation mechanism and system architecture, not only by industry.

The eight candidate cases from the Application-Fit register can be browsed as a research portfolio. The five deep-screened cases (C01, C03, C04, C05 and C08) may receive fuller pages, subject to source and evidence review.

A case page should state:
- problem context and system boundary;
- domains and subsystems involved;
- transformation mechanism;
- cross-domain coupling pattern;
- accessibility conditions and constraints;
- downstream trajectory implications;
- conventional baseline;
- what TGCV representation adds or does not add;
- evidence status and unresolved questions.

Candidate cases must be labelled as candidates. A case's presence on the website is not proof of application fit.

### 3.8 Open Playground

**Role:** provide a safe, understandable environment to inspect transformation-space behaviour.

Initial experience should be narrow and guided rather than a broad, unbounded platform. A first demonstrator could let visitors:
1. inspect a small synthetic system;
2. view candidate transformations;
3. toggle a declared condition or constraint;
4. compare accessible transformations before and after;
5. execute an admissible transformation;
6. inspect the successor state and changed possibilities;
7. trace a simple multi-domain dependency;
8. inspect assumptions and limitations.

The playground must distinguish simulation rules from empirical observations and must not imply that synthetic outcomes predict real-world behaviour.

### 3.9 Community

**Role:** invite participation in an interdisciplinary research and engineering ecosystem.

Possible elements:
- learning paths and introductory materials;
- technical documentation;
- contribution opportunities;
- calls for collaboration;
- events or seminars when they exist;
- community code of conduct and contribution principles.

Do not claim an active community, events programme or open contribution process before these exist.

### 3.10 About and governance

**Role:** establish identity, transparency and boundaries.

Explain:
- the ecosystem's purpose;
- its relationship to TGCV;
- scientific independence and evidence discipline;
- how methods, prototypes and applications are governed;
- collaboration and contact routes.

The ecosystem may develop applications around TGCV but cannot redefine scientific claims through marketing or deployment activity.

## 4. Two primary visitor journeys

### Journey A — Understand the research

`Home → Explore → Research / TGCV → Transformation-space dynamics → Evidence → Research artefacts`

Success means the visitor understands the central research question, knows what is and is not established, and can inspect the underlying work.

### Journey B — Explore a technical application

`Home → Engineering or Labs → Application-Fit case → Demonstrator → Method / baseline → Collaboration`

Success means the visitor understands a bounded system problem, sees how transformations and dependencies are represented, and can judge whether a deeper technical exploration is warranted.

Additional journeys can be developed for developers, students and institutions after initial usability testing.

## 5. Content types and metadata

Use a small number of reusable content types rather than designing every page independently.

| Content type | Required metadata |
|---|---|
| Research concept | Title, definition, scope, status, related concepts, canonical source, last reviewed |
| Research question / hypothesis | Question, hypothesis, assumptions, falsifiers, evidence status, related experiment |
| Experiment | ID, objective, system boundary, design, inputs, execution state, audit, limitations, artefacts |
| Demonstrator | Name, version, synthetic/empirical designation, capabilities, baseline, reproducibility, limitations |
| Application case | Case ID, domain(s), system boundary, mechanism, coupling pattern, candidate/qualified status, sources |
| Method / specification | Version, intended use, inputs, outputs, assumptions, constraints, status |
| Tool / component | Version, function, interfaces, dependencies, availability, documentation |
| Learning resource | Level, prerequisites, topic, format, related concepts |
| News / update | Date, change, affected artefact, status, source link |

Recommended universal metadata:
- unique identifier;
- title and short summary;
- content owner or responsible role (when defined);
- status;
- version;
- publication/review date;
- provenance/source links;
- related pages and concepts;
- scientific/evidence caveat where applicable.

## 6. Evidence and publication labels

Use explicit, text-based labels consistently. Do not rely on colour alone.

| Label | Meaning |
|---|---|
| **Concept** | Explanatory concept; not itself an empirical result |
| **Hypothesis** | Proposition to be tested |
| **Proposed** | Design or method not yet demonstrated |
| **Synthetic** | Generated or simulated data/system |
| **Executed** | A defined run completed |
| **Audited** | A specified audit was performed; scope must be named |
| **Empirical** | Data or observations from a real-world system; study design must be described |
| **Pilot** | Bounded real-world trial; not automatically generalisable |
| **Deployed** | Operating in a real environment; does not by itself establish effectiveness |
| **Open question** | Unresolved issue or evidence gap |

A label must always be accompanied by a short explanation. “Audited” must identify what was audited. “Empirical” must identify the empirical basis. “Deployed” must not be treated as “validated”.

## 7. Editorial principles and vocabulary

### Prefer
- systems and subsystems;
- transformation spaces;
- accessible transformations;
- admissibility and constraints;
- transformation-space dynamics;
- trajectories and successor states;
- cross-domain dependencies;
- systems engineering;
- modelling, simulation and experimentation;
- evidence, baselines and limitations.

### Use carefully
- intelligence (define the functional meaning);
- generative (specify what is generated);
- emergence (state the system and conditions);
- value (specify whose value, under which model and context);
- optimisation (state objective, constraints and trade-offs);
- prediction (state target, horizon and validation).

### Avoid as identity-defining language
- business transformation consultancy;
- generic AI transformation;
- guaranteed value creation;
- universal systems intelligence;
- autonomous optimisation of any system;
- “revolutionary”, “breakthrough” or “proven” without evidence.

## 8. Visual and interaction principles

The visual system should feel like a serious, contemporary systems research and engineering environment: clear, precise, exploratory and technically literate.

Recommended visual language:
- diagrams of systems, boundaries, interfaces and dependencies;
- transformation graphs and state-transition sequences;
- before/after accessible-space comparisons;
- layered architecture views;
- cross-domain propagation maps;
- timelines and trajectories;
- interactive model inspection.

Avoid stock imagery of generic business meetings, abstract glowing brains, humanoid robots used as decoration, or generic “AI network” backgrounds that do not explain the work.

Every diagram should answer a question. Every interaction should reveal a model, distinction or consequence. Motion and visual effects should never obscure evidence status or system boundaries.

Accessibility requirements:
- responsive layouts;
- keyboard-operable interactions;
- readable contrast and type;
- text alternatives for diagrams;
- reduced-motion support;
- no colour-only encoding;
- clear focus states and descriptive labels.

## 9. Release plan

### Phase 0 — Foundation and content integrity
- confirm identity language and core definitions;
- validate source links and evidence labels;
- approve navigation and page templates;
- establish visual principles and editorial workflow.

### Phase 1 — Credible minimum website
Publish:
- Home;
- Explore;
- Research / TGCV;
- Transformational Intelligence;
- Engineering;
- Labs & Simulation with one carefully bounded demonstrator;
- Application-Fit overview with clearly labelled candidate cases;
- About / governance;
- contact route.

Do not publish empty pages or imply a complete product ecosystem.

### Phase 2 — Technical depth
Add:
- detailed research and evidence pages;
- full Application-Fit case pages;
- methods and specifications;
- technical documentation;
- reproducibility artefacts;
- learning resources.

### Phase 3 — Interactive exploration
Add:
- Open Playground;
- interactive transformation-space explorer;
- cross-domain scenario;
- model and experiment comparison;
- contributor workflows.

### Phase 4 — Ecosystem growth
Add only when operationally real:
- community programmes;
- events;
- external collaborations;
- reusable tools and connectors;
- applied pilots and deployment cases.

## 10. Acceptance criteria for the web architecture

The information architecture is ready for visual design when:

1. A first-time visitor can explain in their own words what TGCV investigates.
2. A researcher can distinguish concepts, hypotheses, synthetic demonstrations and empirical evidence.
3. A systems engineer can find the modelling, architecture and experimentation material.
4. An AI practitioner can understand why Transformational Intelligence is not simply another name for AI.
5. A visitor can trace at least one example from system conditions to accessible transformations and subsequent trajectory.
6. Candidate application cases are not mistaken for validated applications.
7. Value and outcomes are not conflated with accessibility or transformation.
8. The website's structure reflects the ecosystem rather than a consultancy sales funnel.
9. Every published claim has an identifiable source and appropriate status.
10. The site can grow without requiring a redesign of its core navigation.

## 11. Decisions intentionally left open

This document does not decide:
- final ecosystem or brand name;
- logo, typography, colour palette or visual identity;
- final technology stack or CMS;
- hosting, analytics or privacy tooling;
- exact public/private split of repositories and artefacts;
- whether all candidate cases should be public;
- community platform or contribution model;
- commercial or advisory offerings;
- final copy and scientific wording for every page.

These decisions should follow the approved Web Master Brief and this information architecture, not precede them.

## 12. Relationship to the master brief

This document operationalises `TGCV_WEB_MASTER_BRIEF_v0.1.md`. If a web-design choice conflicts with the master brief's scientific boundaries or identity orientation, revise the web-design choice or raise the conflict explicitly. Do not silently reinterpret TGCV.

**Master orientation:** build a website where people can understand, inspect and explore how systems transform, how accessible transformation spaces change, and how systems engineering and transformational intelligence can help reason about those dynamics.


## 13. AWGI principles and visitor-experience requirements

This information architecture applies the transferable web principles recorded in the Web Master Brief §17. They are adapted to TGCV's research and engineering ecosystem, not copied as AFLUYA's identity or commercial model.

### 13.1 Web as active ecosystem infrastructure
The site must progressively support discovery, understanding, exploration, learning, connection and contribution. It is not merely a descriptive catalogue. Each published section should provide a useful next step and should correspond to content, resources or participation routes that actually exist.

### 13.2 Efecto Ajá as an acceptance test
A first-time visitor should be able to explain, in their own words and after a short visit (two minutes as a design target, not a scientific threshold):
- the central question TGCV investigates;
- why a system's conditions can change what it can do next;
- why this matters to systems thinking, modelling or engineering;
- where they can go next to explore the topic.

Test with people outside the project and from more than one background. Ask what they understood, what they found relevant, what remained confusing and what they would do next. Do not substitute internal approval or a satisfaction score for comprehension evidence.

### 13.3 Experience sequence
Page hierarchy and cross-links should support this sequence:
**Recognition → Insight → Understanding → Exploration → Participation.**

Recognition begins with a problem or question familiar to the visitor. Insight reveals the distinctive transformation-space perspective. Understanding explains the analytical distinctions. Exploration offers substantive content. Participation offers a real, bounded next step.

### 13.4 Value before data; participation without forced registration
Public explanatory content and available learning resources should be accessible without registration. Forms should be used only for a clear purpose, collect the minimum data necessary and explain its use. GitHub may be the canonical source for technical artefacts but must not be the only route for questions or contributions from non-technical visitors.

### 13.5 Transparent maturity and evidence
Show operational content states only when useful: Available, In development, Open to contribution, Exploratory, Deferred and Closed. Keep these separate from scientific evidence labels (Concept, Hypothesis, Synthetic, Executed, Audited, Empirical, Pilot, Deployed). A page being available does not make its claims scientifically validated.

### 13.6 Network effects without simulated community
Create pathways between related concepts, cases, methods, people and contribution opportunities. Do not imply that a community, events programme, collaboration offer or contribution workflow is active until it exists and can be maintained.

### 13.7 Progressive, maintainable growth
Publish a small coherent site before attempting the full sitemap. Add pages and functions according to visitor needs, evidence, contributions and maintenance capacity. Prefer portable, reversible and low-friction choices; no technology, domain purchase, paid service or external account is authorized by this architecture.

## 14. First-release visitor journeys and acceptance

The first release must support at least three realistic journeys:

1. **Understand:** Home → Explore → Research / TGCV → evidence and limitations.
2. **Apply the perspective:** Home → Engineering → a candidate application context → method or demonstrator (only if available).
3. **Connect or contribute:** Home / relevant content → participation information → an actual contact or proposal route.

The third journey must not end in a dead link or a promise of an unavailable process. If a contribution mechanism is not ready, offer a truthful contact route and label the status accordingly.

For the Efecto Ajá test, record whether visitors can explain the central question, distinguish accessibility from execution at a basic level, locate a relevant next step and identify uncertainties without being coached.

The first-release architecture is accepted only if it remains useful without the Playground, has no empty menu destinations, offers content before requesting personal data, and accurately labels the maturity of every featured asset.


## 15. Content implementation reference

The first-release page inventory, content specifications, reusable source-asset register, evidence controls, publication clearance and editorial gates are defined in `06_WEB/TGCV_WEB_CONTENT_BLUEPRINT_v0.1.md`.

The content blueprint is the operational content plan under this information architecture. If a page or navigation destination cannot be populated with accurate, useful and maintainable content, omit or defer it rather than publish an empty destination.

### First-release rule

The germinal website must provide coherent journeys through Home, Explore, Research, the systems-engineering/TI identity areas, bounded Labs & Applications, About/Governance and a real contact route. It must remain useful without the future Playground, a new simulator or a community platform.

### v0.3 — 2026-11-24

- Added the first-release Content Blueprint as the operational content-planning reference.
- Clarified the rule against empty or premature navigation destinations.


## 16. Decision lock — approved Home identity and navigation (2026-11-24)

This section supersedes any incompatible navigation, audience, page-role or Efecto Ajá requirement earlier in this document. The Web Master Brief §21 is the parent decision record.

### 16.1 Primary visitor

The primary visitor is a person who researches, designs, develops or engineers systems. The experience remains understandable to adjacent audiences and interested newcomers.

### 16.2 Ecosystem identity

Transformational Intelligence (TI) is the integrative capability and conceptual axis of the ecosystem: understanding, reasoning about and orienting transformations in systems. It is a working concept/capability, not a claim of a consolidated academic discipline or generally validated capability.

Systems Thinking is the perspective for understanding systems, conditions, relations, dynamics and possibilities. Systems Engineering is the discipline for modelling, designing, developing and intervening in systems and their transformations. They are complementary foundations contributing to TI, not three equivalent departments.

Research and Labs & Applications are activity spaces: Research develops knowledge, models, methods and evidence; Labs & Applications explores experiments, demonstrators and application contexts. They interact bidirectionally.

### 16.3 First-release navigation

The approved top-level navigation is:
1. **Explore** — conceptual entry, accessible explanation and the central software-migration example.
2. **Research** — TGCV, research questions, methods, experiments, evidence and limits.
3. **Systems Engineering** — engineering practices and their relation to the TGCV research object.
4. **Transformational Intelligence** — working capability concept, functional dimensions, distinction from AI and open questions.
5. **Value Construction** — VALUE as an applied framework complementary to TGCV, its lifecycle and a clearly labelled fictional clinic case.
6. **Labs & Applications** — bounded demonstrators, synthetic methodological work and exploratory application contexts.
7. **About** — purpose, scope, governance and accurate programme context.
8. **Contact** — only a real, monitored contact route with proportionate privacy information.

Systems Thinking is transversal, not a separate first-release page: introduce it on Home, explain its role in Explore and develop its methods/foundations in Research. Do not retain Community as a top-level first-release destination. Do not publish empty destinations.

### 16.4 Home narrative and language

Home sequence: opening question → discovery → second visitor question and concise answer → tangible example → conceptual explanation → ecosystem → exploration. Opening question: «¿Qué tendría que cambiar para que un sistema pudiera hacer algo que hoy no puede hacer?» Second question: «¿Qué nuevas opciones aparecen cuando un sistema puede hacer algo que antes no estaba a su alcance?» Its concise answer connects newly accessible transformations with new options and possible opportunities for value, without guaranteeing execution, favourable outcomes or value. Working headline: «Comprende cómo cambian las posibilidades de un sistema.» The example is migration of a software configuration between two distinct environments. It is an illustrative editorial example, not an existing validated demonstrator.

The first public release is Spanish and English, conceptually and editorially equivalent. Adapt naturally rather than translate literally. Home must introduce the accessible ecosystem map that distinguishes TGCV, Systems Thinking, Systems Engineering, Transformational Intelligence, Value Construction/VALUE, Labs & Applications and proposed ValueLabOS.

### 16.5 Efecto Ajá and release acceptance

Efecto Ajá is a desired quality objective, not a mandatory publication gate. Conduct an integral pre-publication review of concept, narrative, visitor journey and examples, including simulated visitor profiles. Add real visitor testing when an external group is available. Lack of external validation alone must not block publication.

Mandatory release requirements remain: coherent identity, clear message, visitor orientation, scientific credibility, accessible and responsive experience, useful content, truthful asset/evidence labels, working links and a maintainable scope. No page may imply a community, collaboration programme, lab facility, deployed application or professional Playground that does not exist.

### 16.6 Content maturity and cross-document consistency

Use **Existing**, **In development** and **Exploratory** as operational content labels where useful; keep them distinct from scientific evidence labels. The Content Blueprint remains the operational content inventory. The Home Experience defines the visitor sequence; Home Copy supplies editable language. All must conform to this decision lock.

### v0.4 — 2026-11-24
- Reconciles navigation and page roles with the approved identity architecture.
- Removes Community from first-release top-level navigation and gives Systems Thinking a transversal role.
- Makes bilingual publication explicit and Efecto Ajá non-blocking.


## 17. Explore page experience and content authority

The detailed visitor experience and bilingual copy for Explore are defined in:

- `06_WEB/TGCV_WEB_EXPLORE_EXPERIENCE_v0.1.md` — current content version 0.9.
- `06_WEB/TGCV_WEB_EXPLORE_COPY_v0.1.md` — current content version 0.8.

Explore is the conceptual deepening after Home, not a second presentation of the same discovery. Home introduces that a system's possibilities can change; Explore asks how we determine whether a candidate transformation is accessible, relative to a defined system, boundary and set of conditions. Home's numbered conceptual sequence is a reading aid, not a universal causal chain; trajectory must be visualised as the path across states and transitions, not as a discrete stage.

Its working progression is:
1. Move from the Home insight to the question of how accessibility is assessed.
2. Distinguish a candidate transformation from an accessible transformation.
3. Use the same migration transformation in two environments, with one explicit difference: the required dependency is available in A and missing in B. State that the comparison holds the same operation, stated boundary assumptions and other specified prerequisites constant, and does not imply that this dependency is the only factor in a real migration.
4. Explain that making the dependency available may change accessibility, without implying execution, success or value.
5. Keep the visible sequence **Accessibility → Execution → Outcome → Value** (Spanish: **Accesibilidad → Ejecución → Resultado → Valor**) as a persistent visual anchor. Place candidate transformation before it as the object whose accessibility is assessed; represent trajectory across states and transformations, not as another stage.
6. Open the space-of-possibilities section with the question: “¿Qué nuevas opciones aparecen cuando un sistema puede hacer algo que antes no estaba a su alcance?” / “What new options become available when a system can do something that was previously beyond its reach?”
7. Explain the space of possibilities through three visitor questions: what elements are present and what can each do; how are they related; and under what conditions can they act together. Make clear that component capabilities alone do not determine accessibility.
7. Connect Systems Thinking and Systems Engineering as complementary foundations to Transformational Intelligence as the ecosystem's integrative capability concept.

The migration example is illustrative only. It is not an existing execution, validated application, Juguete Colectivo feature or C10-S result. Keep the single missing-dependency condition consistent across Home, Explore and both languages.

The Spanish and English versions must be complete and conceptually equivalent. In English, introduce “accessibility of transformations” and clarify that it refers to whether a transformation is within a system's reach under the system boundary and conditions being considered—not to digital/interface accessibility. “Outcome” remains the consistent equivalent of “resultado” in this explanatory context.

The page must preserve these distinctions:
- candidate transformation is the object assessed before accessibility; candidate does not mean accessible;
- keep the visible sequence **Accessibility → Execution → Outcome → Value** (Spanish: **Accesibilidad → Ejecución → Resultado → Valor**);
- accessibility means being within reach under specified boundaries and conditions; it does not mean execution;
- execution does not guarantee a favourable outcome;
- outcome is not equivalent to value;
- trajectory describes evolution through states and transformations and does not imply one inevitable chain or an additional universal linear stage.

The visitor-facing explanation should also make the practical implication clear: changed accessibility changes the options within reach, while deciding whether those options are useful or desirable requires additional objectives and contextual criteria. The detailed specification and copy remain working drafts, not publication clearance. Apply the non-blocking Efecto Ajá policy and all scientific, accessibility, bilingual, privacy and maintainability release checks already established in this architecture.

### v0.5 — 2026-11-24
- Adds the initial Explore experience specification and bilingual copy as working references for P02.
- Aligns the page's narrative, example, terminology and conceptual guardrails with the approved first-release identity and navigation.

### v0.6 — 2026-11-24
- Clarifies the Home-to-Explore hand-off so Explore deepens rather than repeats the Home discovery.
- Fixes the migration illustration to one missing dependency and updates the conceptual progression and terminology.


### v0.7 — 2026-11-24
- Aligns the Home visual treatment of trajectory with the Explore conceptual guardrail: trajectory spans states and transitions and is not a discrete linear stage.


### v0.8 — 2026-11-24
- Refreshes the current Explore Experience version reference after the integrated editorial reconciliation.

### v0.9 — 2026-11-24
- Incorporates the final editorial refinement of Explore: accessibility as being within reach rather than execution, practical implications of changed accessibility, and trajectory as an evolution that need not form one chain.
- Updates the current bilingual copy and experience references.

### v1.0 — 2026-11-24
- Makes the block-5 question about newly available options an explicit content requirement in Spanish and English.
- Requires the visible Accessibility → Execution → Outcome → Value sequence, with candidate transformation placed before it and trajectory represented across states and transformations.
- Updates the authoritative Explore Experience and Copy versions.


### v1.1 — 2026-11-24
- Adds the second visitor question and its concise value-oriented answer to the mandatory Home narrative, positioned immediately after the initial discovery and before the tangible example.
- Preserves the existing Explore block-5 question as the deeper conceptual development rather than replacing or duplicating its explanatory role.


## 18. Public identity decision (2026-11-24)

The website's public identity is **TGCV — Transformaciones Generativas y Construcción de Valor**. TGCV is presented as a research programme, not as an established theory.

Canonical Spanish descriptor:
*Un programa de investigación aplicada e innovación sobre cómo la ampliación de las posibilidades de transformación de los sistemas puede contribuir a la construcción de valor.*

English rendering:
**TGCV — Generative Transformations and Value Construction**.
*A programme of applied research and innovation exploring how expanding the transformations available to systems may contribute to value construction.*

Apply this consistently to page titles, first-mention descriptions, About/Research identity blocks, footer and metadata. The Spanish expansion is canonical; in English, TGCV remains the proper name rather than a mechanically re-derived acronym. Keep the scientific and public-identity layers separate.

### v1.2 — 2026-11-24
- Adds the approved public identity and bilingual naming convention to the information architecture.


## 19. Home identity placement review (2026-11-24)

The site-wide header identifies the initiative as **TGCV — Transformaciones Generativas y Construcción de Valor**. The English rendering is **TGCV — Generative Transformations and Value Construction**; TGCV remains the proper name. The full programme descriptor is used in the footer and relevant About/Research identity blocks.

The Home's first substantive message remains the approved visitor question. Do not add a long institutional introduction ahead of it. On narrow screens, the header may visually prioritise “TGCV”, provided the full name remains available accessibly.

The required Home sequence is opening question → discovery → second question and concise answer → tangible software-configuration example → conceptual explanation → ecosystem → exploration. The second question precedes the example in both languages.

“Generative” refers to transformations that can change what systems can do or access; it must not be interpreted as a reference only to generative AI, content generation or autonomous self-modification.

### v1.3 — 2026-11-24
- Specifies placement of the approved TGCV public identity in the site-wide header and footer.
- Preserves the visitor-first opening and aligns Home narrative ordering.
- Clarifies the public meaning of “Generative”.

### v1.4 — 2026-11-24
- Updates the canonical bilingual public descriptor to “applied research and innovation”.
- Preserves the existing visitor-first Home sequence and the distinction between accessibility, execution, outcome and value.


### v1.5 — 2026-11-25
- Refreshes the authoritative Explore Experience and Copy references to v0.7 and v0.6.
- Makes the single-variable illustrative contrast explicit without generalising it into a complete account of real migration feasibility.


### v1.6 — 2026-11-25
- Updates Explore Experience and Copy references to v0.8 and v0.7.
- Clarifies the visitor-facing explanation of system possibilities through elements, relationships/dependencies and operating conditions, avoiding a disconnected factor checklist.


### v1.7 — 2026-11-25
- Updates Explore Experience and Copy references to v0.9 and v0.8.
- Clarifies the distinct roles and maturity of Systems Thinking, Systems Engineering, Transformational Intelligence and TGCV.


## 20. Research page experience authority

The Research visitor experience is specified in:

- `06_WEB/TGCV_WEB_RESEARCH_EXPERIENCE_v0.1.md` — current content version 0.2.

Research follows Home and Explore. Home introduces the central question; Explore explains candidate transformations and accessibility under stated system boundaries and conditions; Research presents the scientific programme, current Core, research questions, methodological logic, evidence status, open questions and traceable research materials.

The page must distinguish canonical conceptual definitions, analytical representations, working proposals, synthetic methodological evidence, bounded empirical evidence and unresolved claims. The evidence snapshot must be reconciled against the then-current RMA, Evidence→Claim Matrix, traceability and source audit records before final copy or publication. A controlled source asset is not automatically cleared for public release.

The visitor experience is progressive: accessible explanation first, research architecture and questions next, methods and dated evidence status thereafter, then open questions and curated source materials. The detailed experience document is a working draft, not publication approval.

### v1.8 — 2026-11-25
- Adds the Research page experience authority and its current working specification.
- Defines Research as the scientific deepening after Home and Explore.
- Adds explicit evidence-status and public-source publication controls.


## 21. Systems Engineering page experience authority

The P04 visitor experience and bilingual copy are specified in:

- `06_WEB/TGCV_WEB_SYSTEMS_ENGINEERING_EXPERIENCE_v0.2.md` — current experience version 0.2.
- `06_WEB/TGCV_WEB_SYSTEMS_ENGINEERING_COPY_v0.2.md` — current bilingual copy version 0.2.

Systems Engineering is a concise first-release destination (P1). Its visitor question is: **How does systems engineering relate to the research object of TGCV?**

The five-movement experience moves from working with systems as wholes, through representing system structure and conditions, to design/integration/verification, an illustrative software-configuration migration, and finally the complementary TGCV research question about changes in accessible transformations.

Keep Systems Thinking, Systems Engineering, TGCV and Transformational Intelligence distinct. Do not imply that TGCV replaces systems engineering, provides a proprietary or validated engineering method, or that the illustrative migration has been executed. Bilingual copy must preserve the distinction between accessibility, execution, outcome and value.

### v1.9 — 2026-11-25
- Adds the Systems Engineering page experience and bilingual copy as current P04 authorities.
- Aligns the information architecture with the approved five-movement experience and the first-release P1 scope.


### v2.0 — 2026-11-25
- Updates the P04 Systems Engineering experience and bilingual copy authorities to v0.2.
- Records the technical editorial refinements: iterative/concurrent life-cycle activities, verification and validation throughout the work, and recognised further-reading sources.


## 22. Public ecosystem architecture and Value Construction destination

The public website must make the relationship among the programme's distinct elements visible through an accessible conceptual map, introduced from Home or an immediately accessible “How the parts connect” overview and reachable from relevant pages.

The map distinguishes:
- **TGCV:** applied research and innovation programme investigating changes in systems' accessible transformations and their possible consequences.
- **Systems Thinking:** transversal perspective for understanding systems, boundaries, relationships, context and dynamics.
- **Systems Engineering:** established engineering discipline and practice for defining, modelling, designing, integrating and evaluating engineered systems.
- **Transformational Intelligence:** integrative capability concept under development, not a generally validated capability or synonym for AI.
- **Value Construction / VALUE:** applied framework for exploring opportunities and organising understanding, design, decision, action and learning. It is complementary to TGCV, not a proven derivation or an assumption that TGCV's causal hypothesis is confirmed.
- **Labs & Applications:** experimental and application spaces whose assets require explicit maturity and evidence labels.
- **ValueLabOS:** proposed enabling digital/collaborative ecosystem for applying and evolving VALUE; distinct from VALUE and from Labs & Applications.

The map must not show a single unqualified causal or operational chain. Use labelled relationships and preserve the distinction between conceptual relationship, engineering practice, applied framework, implementation support and evidence.

### 22.1 New first-release destination — Value Construction

Position **Value Construction** after Transformational Intelligence and before Labs & Applications.

**Visitor question:** How can a system explore opportunities and organise decisions, action and learning to build value?

The future page must present VALUE as an applied framework complementary to TGCV and independently evaluable. Its working six-movement visitor experience is:
1. From opportunity to value: contextual value criteria and affected actors.
2. Understand the system: context, actors, needs, capabilities, knowledge, relations, flows and constraints.
3. Explore possibilities: opportunities and alternatives as hypotheses.
4. Decide and act: separate selection, authority, execution authorisation, implementation and adoption.
5. Learn and renew: evaluate results against prior criteria and update capabilities.
6. A worked fictional case: the clinic appointment-management system, showing relevant A1–A8 artefacts and decision trail only after version and disclosure checks.

Use the methodology's current lifecycle: ALIGN as entry/alignment and governance, then SENSE, CONNECT, DESIGN, DECIDE, ACT and LEARN. The lifecycle is iterative, not a rigid waterfall. The fictional clinic case and its simulated figures/outcomes are pedagogical material, not empirical validation or evidence of real-world effectiveness.

**Core relationship:** TGCV investigates how transformations available to systems change and whether those changes may contribute to value; VALUE structures applied work to understand opportunities, design alternatives, decide, act and learn. Neither validates the other automatically.

### 22.2 Source assets and readiness

At page-development time, review:
- `05_ASSETS/Business_Translation/VALUE_METHODOLOGY_LIFECYCLE_001.md` (v0.4 at the time of this decision);
- `05_ASSETS/Business_Translation/TGCV_VALUE_VALUELABOS_IDENTITY_ARCH_v0.1.md`;
- `05_ASSETS/Business_Translation/VALUE_FICTIONAL_CASE_CLINIC_001_v1.1.md`;
- current A1–A8 artefacts and supporting clinic-case coherence reviews in `05_ASSETS/Business_Translation/`.

Do not assume these versions remain current when development begins. Recheck exact filenames, versions, internal consistency and public-disclosure suitability. Do not expose internal identifiers or artefact codes in visitor-facing copy unless converted into understandable public descriptions.

### 22.3 Claim boundaries

- Do not imply that accessible transformations automatically create value.
- Do not present VALUE as scientifically validated by TGCV or as dependent on confirmation of C10.
- A VALUE application does not establish TGCV causal claims; a limitation of a TGCV hypothesis does not automatically invalidate VALUE.
- Keep opportunity, accessibility, decision, authorisation, execution, adoption, outcome and value distinct.
- Value is contextual and must specify whose value, which outcome, over what horizon and under what constraints.
- ValueLabOS is proposed, not a released product; it is not the Labs & Applications section.

### v2.1 — 2026-11-25
- Adds Value Construction as a first-release destination between Transformational Intelligence and Labs & Applications.
- Adds the public conceptual map and defines its non-linear, non-causal explanatory role.
- Records the VALUE lifecycle, clinic-case use and independent-evaluation guardrails.


### v2.2 — 2026-11-25
- Synchronises the approved first-release navigation with the new Value Construction destination and its position after Transformational Intelligence.
- Updates Home's Experience and Copy authorities to v1.5 and v1.2.
- Makes the public ecosystem map a Home-level explanatory element and preserves the distinctions among TGCV, VALUE, ValueLabOS and Labs & Applications.


### v2.3 — 2026-11-25
- Corrects the authoritative first-release navigation list to include Value Construction between Transformational Intelligence and Labs & Applications.
