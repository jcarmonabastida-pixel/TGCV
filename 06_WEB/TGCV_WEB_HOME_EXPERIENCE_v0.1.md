# TGCV — Home Experience Concept
**Identifier:** TGCV-WEB-HOME-001  
**Version:** 0.4  
**Date:** 2026-11-24  
**Status:** STRATEGIC DESIGN — WORKING CONCEPT  
**Parent documents:**  
- `06_WEB/TGCV_WEB_MASTER_BRIEF_v0.1.md`  
- `06_WEB/TGCV_WEB_INFORMATION_ARCHITECTURE_v0.1.md`  
**Branch:** `strategy/tgcv-web-master`  
**Purpose:** Define the Home page's conceptual narrative, visitor experience, content hierarchy and first-release explanatory visual before visual identity and detailed UI design.  
**Authority:** This document governs only the proposed web experience. It does not alter TGCV's scientific Core, canonical definitions, evidence status or execution authorization.

---

> **Current editorial authority (2026-11-24):** the approved decision-lock section at the end of this document is authoritative for the first public web release. It supersedes any earlier working text that conflicts with the approved audience, identity architecture, Home narrative, software-migration illustration, first-release navigation, Spanish/English requirement or non-blocking Efecto Ajá status. Earlier material is retained as design history until the next full editorial rewrite; it must not be treated as current instruction where it conflicts with the decision lock.

## 0. Strategic decision

The Home page should introduce TGCV's intellectual and engineering territory through one compelling question:

> **How does a change in a system alter what that system can do next?**

This question is more distinctive and more faithful to the current research orientation than a generic promise about transformation, innovation, AI or value creation.

The Home page should make the visitor intuitively understand that systems do not only change state. Their available transformations can also change. When that happens, the system's future possibilities and trajectories may change as well.

The page is not a consultancy sales funnel, product launch page or institutional brochure. It is the front door to a research and systems-engineering ecosystem.

## 1. First-screen experience

### 1.1 Working headline

**Understanding and engineering how systems transform.**

### 1.2 Supporting statement

**Research, systems engineering and transformational intelligence for exploring how systems change, what becomes possible, and how future trajectories unfold.**

This is a working proposition, not final brand copy. It should be tested for comprehension with people from systems engineering, AI/software, complex-systems research and adjacent disciplines.

### 1.3 Primary action

**Explore how systems transform**

This leads to the guided Explore experience, not to a sales contact form.

### 1.4 Secondary actions

- **Discover the research** → Research / TGCV.
- **Explore the engineering** → Systems Engineering.
- **See it in action** → Labs & Simulation, but only when a demonstrator is ready and its status is explicit.

### 1.5 First-screen visual

Use a simple, legible static transformation-space illustration rather than stock photography or decorative AI imagery.

The visual should show:
- a system represented as a set of connected components or states;
- a set of candidate transformations;
- a boundary or condition that determines which transformations are accessible;
- a change in conditions or system configuration;
- a visibly altered set of accessible transformations;
- at least two possible subsequent trajectories.

The diagram must communicate a change in *what is possible next*, not merely a before/after state change.

Avoid suggesting that every candidate transformation is always accessible, that every accessible transformation is executed, or that every new possibility produces value.

## 2. The Home narrative

The page should unfold in six narrative movements.

### Movement 1 — The question

**Section title:** What changes when a system changes?

Short copy:

A system is more than its current state. Its structure, resources, relationships, rules and environment shape the transformations it can perform. When these conditions change, the system's possibilities can change too.

Purpose: introduce the distinctive question without overloading the visitor with notation.

### Movement 2 — The central insight

**Section title:** Systems change. Their possibilities change too.

Short copy:

A new resource, capability, connection, permission or constraint can open some transformations, close others or alter the paths available afterwards. Understanding these changes requires looking beyond isolated actions and states to the system's transformation space.

Visual: a two-stage diagram:
1. Initial system configuration and accessible transformations.
2. Modified conditions and a changed accessible transformation space.

The visual should include one opened path and one constrained or closed path to show that transformation-space change is not always expansion.

### Movement 3 — The analytical sequence

**Section title:** From conditions to future trajectories

Present a simplified, explorable sequence:

`SYSTEM & CONDITIONS → CANDIDATE TRANSFORMATIONS → ACCESSIBILITY → TRANSITION → NEW STATE & POSSIBILITIES → TRAJECTORY → OUTCOME`

Value may be shown as a later contextual evaluation, not as an automatic result of accessibility or transformation.

Each stage should have a concise visible explanation (no interaction is required on Home):
- **System & conditions:** the system boundary, current configuration and context.
- **Candidate transformations:** changes that can be considered.
- **Accessibility:** which transformations are available under the specified conditions and decision boundary.
- **Transition:** which transformation is actually performed.
- **New state & possibilities:** how the system and its subsequent options change.
- **Trajectory:** the sequence of possible or realised transitions.
- **Outcome:** what happens and how it is evaluated.

The detailed scientific chain and notation belong in Explore and Research. Home should use plain language first.

### Movement 4 — The ecosystem

**Section title:** Researching, modelling and engineering transformation

Introduce four mutually connected pillars:

1. **Research** — investigate systems, transformation spaces and their dynamics.
2. **Systems Engineering** — model boundaries, subsystems, interfaces, dependencies and constraints.
3. **Transformational Intelligence** — reason about, navigate and adapt to accessible transformation spaces and orient trajectories under independently specified objectives.
4. **Labs & Applications** — build models, simulations and bounded demonstrators; explore application fit across real system domains.

Do not present these as four unrelated business units. Show them as connected modes of work around a shared research object.

### Movement 5 — Across domains

**Section title:** One analytical question. Many kinds of systems.

Show a small selection of candidate application contexts:
- distributed networks and cloud-edge systems;
- AI agents and tool-enabled software systems;
- industrial and cyber-physical systems;
- energy and mobility infrastructures;
- socio-technical and interinstitutional systems.

For each, state the transformation problem in one sentence. Examples:
- How does a change in network configuration alter the services and paths available to dependent systems?
- How do tools, permissions and environment state change the actions an AI agent can actually perform?
- How do physical condition, information, resources and operator interventions reshape maintenance options?
- How do energy constraints and mobility demand alter each other's feasible trajectories?
- How does a transition in one institution change the next actions available to another?

Label these as **candidate application contexts** unless a case has been qualified by appropriate evidence. Do not imply validated performance or generality.

### Movement 6 — Invitation

**Section title:** Explore the transformation space

Primary invitation: enter the guided Explore narrative, supported by a clear static explanatory diagram.

Secondary invitations:
- Explore the research.
- Inspect methods and demonstrators.
- Follow or contribute to the work.

Avoid leading with “Book a consultation”, “Get a business assessment” or other consultancy-first calls to action.

## 3. Recommended page wireframe

```text
┌──────────────────────────────────────────────────────────┐
│ TGCV / identity             Explore Research Engineering  │
│                              Intelligence Labs About      │
├──────────────────────────────────────────────────────────┤
│ HERO                                                     │
│ Understanding and engineering how systems transform.    │
│ Supporting statement                                     │
│ [Explore how systems transform] [Discover the research]  │
│                                                          │
│       Static transformation-space diagram               │
├──────────────────────────────────────────────────────────┤
│ THE QUESTION                                             │
│ What changes when a system changes?                      │
├──────────────────────────────────────────────────────────┤
│ THE CENTRAL INSIGHT                                      │
│ Systems change. Their possibilities change too.         │
│ Initial configuration → changed accessible space         │
├──────────────────────────────────────────────────────────┤
│ THE ANALYTICAL SEQUENCE                                  │
│ Conditions → Accessibility → Transition → Trajectory     │
│ Concise explanation of each stage                        │
├──────────────────────────────────────────────────────────┤
│ THE ECOSYSTEM                                            │
│ Research | Systems Engineering                           │
│ Transformational Intelligence | Labs & Applications     │
├──────────────────────────────────────────────────────────┤
│ ACROSS DOMAINS                                           │
│ Networks | Agentic AI | Industry | Energy | Socio-technical│
│ Candidate cases with mechanism-led explanations         │
├──────────────────────────────────────────────────────────┤
│ EXPLORE                                                  │
│ Guided explanation / available demonstrator (if ready)   │
│ [Explore the transformation space]                       │
├──────────────────────────────────────────────────────────┤
│ FOOTER                                                   │
│ Research sources | Governance | About | Contact          │
└──────────────────────────────────────────────────────────┘
```

This is a content wireframe, not a final visual layout. The actual composition should be responsive and tested on mobile and desktop.

## 4. First-release explanatory visual

The initial Home page should use a carefully designed static diagram or a sequence of annotated visual states. Its purpose is to make the central idea tangible without creating a separate miniature simulator.

The visual should show:
- a bounded system and its relevant conditions;
- candidate transformations;
- which transformations are accessible under the initial conditions;
- a change in one or more declared conditions;
- the resulting change in accessible transformations;
- at least two possible subsequent trajectories.

The visitor should be able to understand the visual without interacting with it. An accessible text explanation must accompany it. The visual must not imply that accessibility guarantees execution, a favourable outcome or value.

A link to an existing demonstrator may be included only when that demonstrator is available, bounded and accurately labelled. The future Playground is a separate application and is not part of this Home implementation.

## 5. Copy principles

The Home page should:
- start from a question about systems, not from a product or service;
- explain the distinctive object in ordinary language;
- introduce formal terms only after intuitive understanding;
- use active, precise verbs: model, represent, inspect, compare, explore, simulate, engineer;
- state uncertainty and evidence status honestly;
- distinguish TGCV, Transformational Intelligence, systems engineering and AI.

Avoid:
- “Unlock limitless potential”;
- “Transform your business”;
- “Create value with AI”;
- “The future of intelligence”;
- “A universal engine for transformation”;
- claims that the approach predicts or optimises all systems.

## 6. Visual direction before visual identity

The visual direction should be derived from the research object.

Potential visual primitives:
- nodes, components and subsystem boundaries;
- transformation edges and admissibility conditions;
- branching trajectories;
- changing topology or connectivity;
- layered system architecture;
- coupled domains and propagation paths;
- state and condition comparisons.

The visual system should feel like a blend of systems research, engineering instrumentation and exploratory scientific software. It should not imitate a generic corporate consultancy or a generic AI startup.

No final colour palette, typography, logo or brand name is selected here.

## 7. Scientific and editorial controls

Before publication:
1. Verify every scientific statement against current canonical sources.
2. Keep the current TGCV Core distinct from non-canonical proposals and adjacent frameworks.
3. Identify synthetic material as synthetic.
4. Do not elevate a completed technical run into scientific validation.
5. Do not imply the candidate Application-Fit cases have been validated.
6. Keep outcome and value models independent from accessibility measures.
7. Link detailed definitions and evidence to versioned source artefacts.
8. Mark working copy and provisional concepts as such during internal review.

The Home page may simplify the explanation, but it must not simplify away distinctions that change the scientific meaning.

## 8. Success criteria

The Home experience is successful when:
- a first-time visitor can explain the central question after a short visit;
- a systems engineer recognises the relevance to modelling and engineering systems;
- an AI practitioner understands that Transformational Intelligence is not simply another term for AI;
- a researcher can find the research programme and evidence boundaries;
- the visitor can see how changing conditions can change accessible transformations;
- no visitor is led to believe that every newly accessible transformation is executed or valuable;
- the site communicates an interdisciplinary research and engineering ecosystem, not a business consultancy.

## 9. Open decisions

The following remain open:
- final headline and supporting copy after comprehension testing;
- whether the Home interaction is embedded or linked to Explore;
- which synthetic example best explains the concept;
- exact navigation labels after user testing;
- final visual identity, brand name and design system;
- public display level for technical notation and formal models.

## 10. Relationship to the master architecture

This concept implements the Home page role in `TGCV_WEB_INFORMATION_ARCHITECTURE_v0.1.md` and the identity orientation in `TGCV_WEB_MASTER_BRIEF_v0.1.md`.

If the design becomes more product-led, consultancy-led or value-marketing-led than the master brief permits, revise the design. The governing idea is:

**Make the visitor see that a system's future depends not only on its current state, but also on which transformations its structure and conditions make accessible.**


## 11. AWGI adaptation: Home as the start of an active visitor journey

The Home page must do more than describe TGCV. It should help visitors recognise a meaningful question, grasp the central insight, find useful depth and identify a real next step. Apply the sequence:
**Recognition → Insight → Understanding → Exploration → Participation.**

### 11.1 Efecto Ajá test for Home

The Home experience should be tested with people unfamiliar with TGCV. After a short visit (two minutes as a design target), ask them to explain:
1. what question the ecosystem investigates;
2. what changes when a system's conditions change;
3. why the distinction between current state and accessible future transformations matters;
4. where they would go next.

Record their own words, misunderstandings, relevant questions and whether they found a meaningful next step. Do not coach them during the test. A positive reaction is not enough if the central idea was not understood. Repeat the test after material changes to headline, visual explanation or page hierarchy.

### 11.2 Visitor-centred narrative and honest invitation

Lead with the visitor's question, not a long institutional self-description. Use a shared invitation such as explore, inspect, compare or contribute only where the destination and activity exist. The Home page should offer value before requesting data: no registration wall for core explanations or public resources, and no contact form as the primary call to action.

### 11.3 Home as a gateway, not a miniature Playground

The first web release will not include a bespoke micro-simulator or an isolated interactive widget on Home. This avoids duplicating the existing Juguete Colectivo and avoids creating a second, disconnected demonstrator. The Playground is a later, separate application line, planned after the germinal website has a stable identity and substantive content.

For the initial Home:
- use a clear static diagram or carefully designed sequence to explain the change in accessible transformations;
- provide text explanations and a guided route to Explore;
- link to a demonstrator only if one is genuinely available and its status and scope are explicit;
- do not show a non-functional “Enter the Playground” action or imply that a professional Playground already exists.

The future Playground may be deployed separately (for example, on an app subdomain), subject to its own technical and product specification. It is not a prerequisite for publishing the germinal website.

### 11.4 Useful content before participation

The visitor should be able to understand the core idea, inspect available research and access public resources without registering. Offer a low-friction way to send a question or correction, including for people who do not use GitHub. Contributions must be reviewed; no public contribution mechanism should be advertised until its process and ownership are defined.

### 11.5 Honest maturity signals

Where relevant, distinguish:
- available content or resource;
- work in development;
- exploratory candidate;
- open contribution with a defined task and route;
- deferred capability.

Keep these operational states separate from scientific labels such as synthetic, executed, audited, empirical or pilot. The Home page must not make a visually polished diagram or demonstrator look like empirical validation.

## 12. Revised first-release Home acceptance criteria

The Home experience is ready for the germinal website when:
1. external visitors can explain the central question without repeating project jargon;
2. the first screen identifies the subject and offers a clear route into Explore;
3. the central visual explains a change in what is possible next, not merely a before/after state;
4. accessible transformations are not confused with executed transformations or outcomes;
5. the visitor finds useful content without registering;
6. every call to action leads to an existing destination or is clearly marked as forthcoming;
7. application contexts and demonstrators carry honest maturity/evidence labels;
8. there is a real, low-friction route for questions or corrections, or the absence of one is clearly disclosed;
9. the page is accessible, responsive and maintainable;
10. no Playground or custom simulator is required for launch.



## 13. Home copy reference

The complete Spanish working copy for the first-release Home page is maintained in `06_WEB/TGCV_WEB_HOME_COPY_v0.1.md`. It provides proposed hero copy, narrative sections, analytical sequence, ecosystem pillars, candidate application contexts, calls to action, footer, headline alternatives and an Efecto Ajá review checklist.

The copy is an editorial draft, not publication-approved. The public language strategy (Spanish, English or bilingual) remains open. Scientific and evidence wording must be checked against current canonical state before publication.

### v0.3 — 2026-11-24
- Aligned the wireframe and visual references with a static explanatory diagram rather than an interactive Home simulator.
- Replaced premature community navigation references with About.
- Added the Home Copy v0.1 as the detailed editorial source.


## 14. Approved visitor experience — decision lock (2026-11-24)

This section is authoritative for the first-release Home and supersedes incompatible wording in earlier sections until the detailed copy and wireframe are fully rewritten. Parent decision: Web Master Brief §21.

### 14.1 Audience and identity

Address first people who research, design, develop or engineer systems, while keeping the entry point understandable to other visitors. Present TGCV as an ecosystem of research, systems thinking and systems engineering articulated around Transformational Intelligence.

TI is the integrative capability/conceptual axis for understanding, reasoning about and orienting transformations in systems. Systems Thinking is the perspective for understanding systems and their conditions, relations and dynamics. Systems Engineering is the discipline for modelling, designing, developing and intervening in systems. They are not three equivalent departments. Research and Labs & Applications are activity spaces that exchange knowledge and feedback.

### 14.2 Approved narrative sequence

1. **Question:** «¿Qué tendría que cambiar para que un sistema pudiera hacer algo que hoy no puede hacer?»
2. **Discovery:** a system can change not only its state but also its possibilities.
3. **Tangible example:** migration of a software configuration between two different environments.
4. **Conceptual explanation:** conditions → candidate transformations → accessibility → transition → new possibilities → trajectories. Keep accessibility distinct from execution, outcomes and value.
5. **Ecosystem:** TI as the axis; Systems Thinking and Systems Engineering as complementary perspectives; Research and Labs & Applications as activity spaces.
6. **Exploration:** direct routes to Explore, Research, Systems Engineering, Transformational Intelligence and Labs & Applications, with About and Contact as supporting destinations.

### 14.3 Hero direction

Opening question: **«¿Qué tendría que cambiar para que un sistema pudiera hacer algo que hoy no puede hacer?»**

Working headline: **«Comprende cómo cambian las posibilidades de un sistema.»**

Working supporting copy: «Un sistema no solo cambia cuando pasa de un estado a otro. También puede adquirir nuevas capacidades, acceder a transformaciones que antes no estaban a su alcance y abrir trayectorias diferentes.»

Ecosystem line: **«Tres perspectivas. Una ambición compartida: comprender, diseñar y orientar cómo evolucionan las posibilidades de los sistemas.»**

These are approved editorial directions, not immutable final copy. Adapt for natural Spanish and English and verify scientific fidelity before publication.

### 14.4 Example design and scientific boundary

The software-configuration migration between two environments is a new illustrative Home example. Show a bounded initial environment, a target environment, relevant changed conditions/dependencies/configuration, a transformation becoming accessible, the distinction between accessibility and actual execution, and possible subsequent trajectories. Do not imply that migration is automatically successful, valuable or executed. Do not describe the existing Collective Toy as this migration demonstrator unless its actual scenario is independently verified.

Use a static, accessible explanatory illustration; no bespoke simulator is required. The visual should allow opening, closing or reconfiguration of possibilities, not only expansion. Keep TGCV's general research question central; software is an example, not the domain definition.

### 14.5 Ecosystem and visitor routes

Present TI, Systems Thinking and Systems Engineering as related but functionally different. Present Research and Labs & Applications as mutually informative activity spaces. Systems Thinking is transversal: visible on Home, explained in Explore and developed in Research; no separate first-release page.

Approved navigation: Explore, Research, Systems Engineering, Transformational Intelligence, Labs & Applications, About, Contact. Explore must add explanatory depth rather than repeat Home. Contact is advertised only when a real monitored route and privacy notice exist.

### 14.6 Languages and Efecto Ajá

First public release: Spanish and English with conceptual/editorial equivalence, not literal translation. Efecto Ajá is a desired quality objective, not a mandatory acceptance gate. Before publication, perform an integral conceptual, narrative and example review, including simulated visitor profiles. Conduct real visitor testing when an external group becomes viable; its absence alone does not block launch.

### 14.7 First-release acceptance criteria

Mandatory: (a) coherent identity and clear visitor-facing message; (b) the question and example explain changed possibilities without jargon overload; (c) accessibility is not confused with execution, outcome or value; (d) useful content and direct routes exist; (e) evidence and asset maturity are labelled honestly; (f) all links and contact claims are true; (g) responsive, accessible and maintainable design; (h) complete equivalent ES/EN content. External Efecto Ajá validation is desirable, not a launch stopper.

### v0.4 — 2026-11-24
- Replaces the earlier six-movement institutional narrative with the approved question → discovery → example → explanation → ecosystem → exploration sequence.
- Locks the software-migration example, hero direction, ecosystem relationship, bilingual requirement and non-blocking Efecto Ajá status.
