# Chapter 1 — Conceptual Review Log

**Review ID:** TV-REV-CH01-CONCEPTUAL-001  
**Content ID:** TV-CH-01  
**Review type:** Conceptual and domain review, including bilingual conceptual equivalence  
**Status:** in_progress  
**Branch:** strategy/transformational-value-learning  
**Created:** 2026-11-27

## 1. Purpose and authority

This record preserves the findings and open recommendations from the conceptual review of Chapter 1. It is an internal editorial traceability record. It supplements, but does not replace, the Content Model & Editorial Workflow, the Learning Master Architecture, the Detailed TOC, TGCV scientific governance, or any relevant domain authority.

The review assesses conceptual clarity, technical precision, scope, examples and equivalence between the independently authored Spanish and English versions. It does not itself approve claims, references, assets, or manuscript changes.

**Important:** Findings below are review observations and proposed resolutions, not approved editorial decisions. No manuscript text has been changed as a result of these two review steps. Both language versions remain `draft`.

## 2. Scope and source manuscripts

| Language | Path | Version at review start | Last known blob SHA |
|---|---|---:|---|
| Spanish | `05_ASSETS/TRANSFORMATIONAL_VALUE/book/es/part-01-understanding-transformation/ch-01-pensar-en-sistemas.md` | 0.9 | `e8e024f6c7740cbe21fa32d935ffe3a6fb3532b8` |
| English | `05_ASSETS/TRANSFORMATIONAL_VALUE/book/en/part-01-understanding-transformation/ch-01-thinking-in-systems.md` | 0.8 | `3fdd8850d1864a3b0ccede3aa0637bd59f5e7e12` |

The manuscript SHAs above are the last known references when this log was prepared; verify current file SHAs before applying any edits.

## 3. Review method and disposition

For each section, record: conceptual assessment; precision or scope issues; ES/EN equivalence observations; proposed resolution; source needs; and decision state. A recommendation remains open until explicitly resolved. References are not considered verified merely because they are named as candidates.

Disposition vocabulary:
- **open** — requires author decision, evidence, or further review;
- **accepted** — resolution agreed but not necessarily yet applied;
- **applied** — manuscript updated and verified;
- **not_applicable** — reviewed and no change required, with rationale.

## 4. Section review records

### 4.1 Section 1.1 — ¿Qué entendemos por sistema? / What Do We Mean by a System?

**Review status:** open  
**Manuscript changes:** none

#### Conceptual assessment

- The treatment of a system as elements connected by relationships is sound and appropriately goes beyond an inventory of components.
- The emphasis on organisation of the whole helps avoid reducing a system to the sum of its parts.
- The operational definition is useful, but the phrase “unit of analysis” needs clarification so that the system of interest is not conflated with the analytical unit or perspective used to study it.
- The discussion of emergent behaviour should be qualified: not every system behaviour is necessarily emergent. The text should distinguish system-level behaviour from behaviour that cannot be understood simply by examining components in isolation.
- The scope of “system” should be made explicit. The chapter should clarify whether its working definition includes physical, social and conceptual systems. Conceptual systems may produce meaning or other conceptual outcomes, not only directly observable behaviour.

#### Example and bilingual-equivalence observations

The water-network example is broadly suitable, but the two language versions are not fully aligned:
- The English version includes treatment facilities not explicitly listed in the Spanish version.
- “Puntos de consumo” and “delivery points” may not identify equivalent network elements.
- The English version adds network topology, demand location/timing and operating conditions; these dimensions are less explicit in Spanish.
- The Spanish text refers to capacity to meet demand, while English makes pressure and flow more concrete.
- The Spanish version discusses propagation of a failure; English refers to service interruption in other areas. These are related but not identical consequences.

#### Proposed resolution

1. Retain the section's overall structure and core systems perspective.
2. Clarify the distinction between system of interest, analytical unit and analytical perspective.
3. State the intended scope of the working definition, including whether conceptual systems are in scope.
4. Qualify the emergence discussion so it does not imply that all system behaviour is emergent.
5. Harmonise the water-network example in both languages: same principal elements, relationships, operating conditions and consequences, while allowing natural language-specific phrasing.

#### Candidate sources — verification pending

- NASA, *NASA Systems Engineering Handbook*, §2.0, “Fundamentals of Systems Engineering”.
- INCOSE, “Systems Engineering and System Definitions” (22 July 2019).
- INCOSE, *Systems Engineering Handbook*, 5th edition (2023).

Bibliographic details, stable URLs, relevant passages and suitability for the specific claims must be checked before adding records to the central references registry. These are candidates, not yet approved citations.

**Decision:** pending author review. No source has yet been formally attached to a claim.

### 4.2 Section 1.2 — Propósito, frontera, entorno y contexto / Purpose, Boundary, Environment and Context

**Review status:** open  
**Manuscript changes:** none

#### Conceptual assessment

- The distinction between the purpose of the analysis and the purpose attributed to the system is useful and should be retained.
- The system boundary should not be described only as a list of included elements and relationships. It should also account for relevant interfaces and may have physical, functional, operational and temporal dimensions.
- The treatment of environment is directionally sound: external elements, systems and conditions can influence the system or be affected by it.
- Context needs a more operational definition. It should include the circumstances, actors, other systems, operating conditions and relationships through which the problem and system of interest are defined and interpreted.
- The distinction between environment and context is an editorial convention for this book, not a universal separation used identically across all disciplines. The text should state this.
- The explanation that delimitation affects what can be observed and concluded is sound. Conclusions and evidence are conditional on the chosen boundary and context.

#### Proposed resolution

A. **Boundary and interfaces:** explain that the boundary identifies what is treated as inside or outside the system of interest and identifies relevant interfaces. For example, a pump may depend on electrical supply, control systems and upstream/downstream infrastructure.

B. **Purpose, function and objectives:** avoid using these interchangeably. Proposed working distinctions:
- Purpose: the declared or attributed reason for the system's existence.
- Function: an activity or contribution the system performs.
- Objectives: intended results, which may be multiple or conflicting.

C. **Operational convention for this book:**
- Environment: external elements, systems and conditions that interact with the system of interest.
- Context: the set of circumstances, relationships and conditions from which the problem and system of interest are defined and interpreted.

D. **Revisability:** state that a boundary may be revised when evidence reveals relevant dependencies, interfaces or effects previously excluded, and that such revision should be justified rather than arbitrary.

#### Bilingual-equivalence observations

- “Propósito” and “purpose” must distinguish the purpose of the analysis from the purpose of the system in both versions.
- “System boundary” / “frontera del sistema” must not be reduced to a physical perimeter.
- “Context” / “contexto” requires an explicit operational definition in both versions.
- The drought, seasonal-demand and regulation example is equivalent in its main idea. It could be strengthened by identifying a concrete interface or dependency, provided both versions retain equivalent scope.

#### Candidate sources — verification pending

- NASA, *NASA Systems Engineering Handbook*, §3.5, concerning boundaries and interfaces (exact subsection and edition to verify).
- INCOSE, *Systems Engineering Handbook*, 5th edition (2023), §1.3.1 (exact wording and relevance to verify).
- NASA, *NASA Systems Engineering Handbook*, §2.0, for foundational systems-engineering framing.

Bibliographic details, exact sections, stable URLs and claim-level relevance must be checked before adding records to the central references registry. These are candidates, not approved citations.

**Decision:** pending author review. No source has yet been formally attached to a claim.


### 4.3 Section 1.3 — Elementos, estados, propiedades y comportamientos / Elements, States, Properties and Behaviours

**Review status:** open  
**Manuscript changes:** none

#### Conceptual assessment

- The section provides a coherent descriptive sequence: identify relevant elements, describe their properties and variables, represent states, and examine behaviour over time. Its central warning against treating isolated data as a complete system description is sound.
- The distinction between an element and a component is not yet fully explicit. The text uses elements as the broader analytical category, but does not explain whether component is a narrower term or simply a near-synonym. This could leave readers uncertain about the intended terminology.
- The definition of state as a condition at a moment **or over an interval** is potentially imprecise. In many modelling contexts, a state is specified at a given time; observations over an interval form a sequence or trajectory of states. The wording should avoid implying that a time interval itself is one state, unless a specific convention is introduced.
- The relationship between properties and variables needs a sharper distinction. A property is a characteristic attributed to an element or system; a variable is a quantity or representation whose value may vary or be used in the model. The current text partly explains this through rated pump capacity versus delivered flow, but could make the conceptual relationship more explicit. Not every property needs to be a variable, and a variable may represent a changing property or condition.
- The behaviour definition is appropriate, but the section could clarify that behaviour is inferred or described from patterns and changes in states/variables under conditions; a single observation may describe a state but is not usually enough to establish a behavioural pattern.
- The section appropriately notes that descriptions are selective and question-dependent. It could also distinguish unavailable information from information deliberately excluded by the chosen scope, since these have different implications for confidence and conclusions.

#### Example and bilingual-equivalence observations

- The Spanish and English versions are closely aligned in structure, concepts, sequence and water-network example.
- The English version introduces “teams” in its list of possible elements, while Spanish lists people and organisations but not teams. This is a minor scope difference; either include teams in both or remove the additional term.
- “Comportamientos” / “behaviours” is a defensible pairing, though “behaviour” can also be used as a collective or uncountable term in English. Maintain consistent usage in the chapter.
- The examples of reservoir level, pump operating condition, pressure, flow, rated capacity and delivered flow are conceptually equivalent.
- The two versions both distinguish a state observation from behaviour observed over time. The precision issue around a state applying “over an interval” is shared by both and should be corrected consistently.
- The reflection question is equivalent and suitably asks the reader to distinguish elements, properties, variables, states and behaviour.

#### Proposed resolution

A. **Element/component terminology:** retain element as the broad analytical term. Add a concise clarification that component is often used for a constituent part, especially in technical or engineered systems, but that the book uses element as the more general term unless a domain-specific distinction is needed.

B. **State and time:** define a state as the condition represented at a specified time (or at a specified reference point). Explain that observations across an interval form a sequence or trajectory of states and can support analysis of behaviour.

C. **Property and variable:** sharpen the distinction between a characteristic attributed to a system/element and a variable used to represent or track a relevant quantity/condition. Retain the rated-capacity/delivered-flow example because it makes the distinction concrete.

D. **Behaviour and evidence:** clarify that behaviour concerns patterns of operation, responses or changes over time under stated conditions. A single measurement may describe a state; repeated observations or other suitable evidence are generally needed to characterise a pattern.

E. **Information gaps:** distinguish information that is unavailable from aspects intentionally omitted from the model or description. Both should be documented when they could affect interpretation, but they are not the same kind of limitation.

F. **Bilingual alignment:** harmonise the list of socio-technical elements (including or excluding teams consistently) and preserve the same conceptual distinctions and examples in both versions.

#### Candidate sources — verification pending

No external source has yet been selected for this section. If the author wishes to strengthen the formal treatment of state, state variables, system behaviour or component terminology, consult an authoritative systems-engineering or systems-modelling reference and verify the exact edition and passages before adding any citation to the central registry. No source is approved or attached to a claim at this stage.

**Decision:** pending author review. No source has yet been formally attached to a claim.


### 4.4 Section 1.4 — Actores, capacidades, recursos y dependencias / Actors, Capabilities, Resources and Dependencies

**Review status:** open  
**Manuscript changes:** none

#### Conceptual assessment

- The section usefully extends the system description beyond physical components, showing how operation may rely on people, organisations, capabilities, resources and dependencies. The integrated water-network example makes the interdependence of these dimensions tangible.
- The definition of **actor** is centred on people, groups and organisations capable of intervening. This is appropriate for the socio-technical emphasis of the section, but the boundary of the term should be explicit: in some modelling traditions, actor or agent can include non-human or software agents. The chapter should either state that it uses actor in the narrower socio-organisational sense or adopt a broader definition consistently.
- The text correctly notes that an actor can be outside the system boundary while influencing the system. It should avoid implying that being outside the boundary automatically means belonging to the environment in every model: classification depends on the system of interest and the chosen boundary. The reason for including an external actor in the description should be tied to a relevant interaction, influence or dependency.
- **Capability** is defined as an ability to perform an activity or fulfil a function under specified conditions. This is useful, but the text should distinguish capability from competence, capacity and currently available operational capability. A person may be competent but lack authority or tools; a technical asset may have a rated capacity that differs from the capability of the wider system to deliver an outcome.
- The section moves between capabilities of individual actors/components and capabilities arising from an organised combination. That is an important distinction and should be made explicit: system-level capability can depend on coordinated contributions and cannot necessarily be inferred by adding individual capabilities.
- **Resources** are described as means used to perform activities, including material, energy, financial, human, informational and temporal resources. The category is broad but understandable. The phrase “human resources” can make people sound like interchangeable assets; consider referring instead to personnel, staff availability, skills or time where that is what the example means. Distinguish people as actors from the time, knowledge or services they make available.
- **Dependencies** are defined in terms of one activity, actor or component requiring another element. The definition is sound but could clarify direction and conditions: A depends on B when A's performance or availability requires a contribution, service, state or condition supplied by B. Some dependencies are conditional, substitutable, time-critical or reciprocal; they need not all be equally critical.
- Dependencies should not be conflated with relationships in general. A relationship may exist without one party depending on the other for a required contribution. The section could make this distinction briefly, especially because relationships were introduced earlier in the chapter.
- The section could also distinguish a dependency from a constraint. A dependency identifies something required; a constraint limits the ways or conditions under which an activity can be performed. They may interact, but are not interchangeable.

#### Example and bilingual-equivalence observations

- The Spanish and English versions are closely aligned in structure, reasoning and examples. The main water-network scenario and the repair example convey equivalent dependencies and coordinated action.
- The heading “Quién interviene y con qué medios” is not an exact rendering of “Who is involved, and what do they need?” The current Spanish heading focuses on means, while English includes needs more broadly. This is a minor editorial difference; align the intended emphasis rather than translating literally.
- Spanish “personal de mantenimiento” and English “maintenance teams” are close but not identical: one refers to staff, the other to a team as an organised unit. Either can work, but the conceptual unit should remain consistent in the example.
- The English phrase “operational ability” in the integrated example is broader and less terminologically precise than Spanish “capacidad operativa”. Consider using “operational capability” consistently if capability is the defined term.
- The two versions both include “human resources” / “recursos humanos”. If revised to avoid treating people as resources, make the adjustment in both languages.
- The actor definition and the caveat about systems without human or organisational agents are equivalent. Both versions should retain the same declared scope for actor.

#### Proposed resolution

A. **Actor scope:** decide whether actor is used in the narrower sense of human, group and organisational participants, or in a broader agent sense that could include software/autonomous agents. Given the examples and chapter purpose, the narrower socio-organisational convention is a defensible choice, provided it is stated.

B. **Boundary and interaction:** clarify that an actor may be inside or outside the system boundary; include external actors when their interactions, influence or dependencies are relevant to the analysis. Avoid treating “outside boundary” and “environment” as automatic synonyms.

C. **Capability levels:** distinguish individual capability from system-level capability that emerges from coordinated elements and actors. Consider a concise note separating capability from competence, rated capacity and current availability, without overloading this introductory chapter.

D. **Resources and people:** retain the broad resource categories but revise “human resources” where appropriate to refer to staff, skills, availability or time. Keep the distinction between actors (participants) and resources (means they can mobilise).

E. **Dependencies:** clarify the direction of dependence and the required contribution/condition. Distinguish dependencies from relationships in general and, briefly, from constraints. Avoid implying that all dependencies are equally critical or non-substitutable.

F. **Bilingual alignment:** align the heading emphasis, maintenance personnel/team example and the use of “operational capability” / «capacidad operativa» across the two original texts.

#### Candidate sources — verification pending

No external source has yet been selected for this section. If formal definitions are needed, consult and verify authoritative sources on capability, actor/agent, resource, dependency and constraint in systems engineering or enterprise/system architecture. Exact editions, terminology and passages must be checked before adding any citation to the central references registry. No source is approved or attached to a claim at this stage.

**Decision:** pending author review. No source has yet been formally attached to a claim.

## 5. Pending review sequence

The remaining sections are to be reviewed in order, one step at a time. No findings are pre-judged here.

| Section | Spanish / English topic | Review status |
|---|---|---|
| 1.3 | Elementos, estados, propiedades y comportamientos / Elements, States, Properties and Behaviours | open |
| 1.4 | Actores, capacidades, recursos y dependencias / Actors, Capabilities, Resources and Dependencies | open |
| 1.5 | To be read from both manuscripts | not_reviewed |
| 1.6 | To be read from both manuscripts | not_reviewed |
| 1.7 | To be read from both manuscripts | not_reviewed |
| 1.8 | To be read from both manuscripts | not_reviewed |
| 1.9 | To be read from both manuscripts | not_reviewed |

Each completed step must be added to this log and committed to the same working branch before moving to the next section. Re-read and verify the updated log after each write.

## 6. Resolution and manuscript integration

After the conceptual review of sections 1.1–1.9 is complete:
1. Review the accumulated findings for consistency and dependencies across the chapter.
2. Resolve open recommendations explicitly; do not silently convert suggestions into decisions.
3. Verify candidate sources and create or update central reference records where justified.
4. Agree the required edits for Spanish and English independently, preserving equivalent conceptual scope without translation-first drafting.
5. Apply approved changes to both manuscripts, update their versions and metadata as required, and verify the resulting files.
6. Conduct the subsequent editorial and cross-language checks under the governing Content Model.

Until that integration step is authorised and completed, the findings in this log do not alter the manuscripts or their `draft` status.

## 7. Change history

- **v0.1 — 2026-11-27:** Created the Chapter 1 conceptual review record; preserved the findings, bilingual observations, proposed resolutions and unverified source candidates for sections 1.1 and 1.2; recorded that manuscript changes have not been applied.
