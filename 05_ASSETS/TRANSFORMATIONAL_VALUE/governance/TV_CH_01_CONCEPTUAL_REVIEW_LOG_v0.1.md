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

**Important:** Findings below are review observations and proposed resolutions, not approved editorial decisions. The conceptual review of all nine sections is complete. Accepted decisions have been integrated into the manuscripts in successive, independently authored language updates, with the completion of each integration stage recorded below. Both language versions remain `draft` pending the remaining chapter-level editorial workflow.

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

**Review status:** reviewed; decisions pending  
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

**Review status:** reviewed; decisions pending  
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

**Review status:** reviewed; decisions pending  
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

**Review status:** reviewed; decisions accepted; integrated and verified in both language manuscripts  
**Manuscript changes:** section 1.4 integrated in Spanish v1.0 and English v0.9; both files re-fetched and checked

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

## 5. Author decisions and implementation status

The following decisions were explicitly approved by the author during the decision-resolution phase on 2026-11-27. They supersede the corresponding “pending author review” statements in the section review records above. They are **accepted editorial decisions**, not evidence that manuscript changes have been applied. Both manuscripts remain unchanged until the coordinated integration phase.

### 5.1 Scope of the working concept of system — accepted

The chapter's primary scope comprises physical, social, organisational and socio-technical systems. It includes systems whose behaviour is not directly observable, provided that behaviour can be inferred through relevant evidence. Purely conceptual systems may be discussed as representations or analytical constructions, but are not automatically equated with systems operating in the world.

### 5.2 System of interest, unit of analysis and analytical perspective — accepted

The chapter will distinguish:
- **System of interest:** the particular system to be understood or studied.
- **Unit of analysis:** what observations or analysis are performed on; this may be the whole system, a subsystem, an actor or an interaction.
- **Analytical perspective:** the approach from which the system is examined, such as functional, operational, organisational or temporal.

### 5.3 System behaviour and emergent behaviour — accepted

The chapter will distinguish:
- **System behaviour:** any behaviour of the system that is observable or inferable.
- **Emergent behaviour:** behaviour or a property arising from the interactions and organisation of the whole, which cannot be adequately explained by examining each element in isolation.

The text must not imply that all system behaviour is emergent.

### 5.4 Operational definition of a system — accepted

The following definition is approved as the common conceptual basis for both language versions. The final Spanish and English wording will be authored independently while preserving its meaning:

> A system is a delimitable set of related and organised elements that interact or maintain relevant dependencies, and whose behaviour can be understood by considering both its elements and the relationships between them, within a given context and over a given period.

This is an introductory operational definition, not a universal definition for every discipline. It does not require every system to have an explicit purpose, every behaviour to be emergent, or every element to interact directly.

### 5.5 Water-distribution network example in section 1.1 — accepted

The author approved a common conceptual scenario for both manuscripts, with equivalent scope and content:
- water source and treatment;
- storage and pumping stations;
- distribution network and its connections;
- consumption points;
- demand varying by location and time;
- pressure, flow and operating conditions;
- energy and control dependencies; and
- propagation of failures and possible service interruptions.

The example should remain introductory and explanatory, not become a detailed hydraulic-engineering case. Each language version should express the scenario naturally and independently while retaining the same principal elements, relationships, conditions and consequences.

**Disposition after this decision phase:** decisions 5.1–5.5 are accepted. Manuscript integration, bilingual cross-review and post-integration verification remain pending. No manuscript text has been changed by recording these decisions.

### 5.6 Purpose, function and objectives in section 1.2 — accepted

The author approved the following working distinctions for both language versions:
- **Purpose:** the declared or attributed reason for the system's existence.
- **Function:** an activity or contribution performed by the system.
- **Objectives:** intended results, which may be multiple and may conflict.

The manuscripts should preserve the distinction between these concepts and should not use the terms interchangeably. The Spanish and English versions will be authored independently while retaining equivalent meaning.

**Disposition:** accepted; manuscript integration and bilingual cross-review remain pending. No manuscript text has been changed by recording this decision.

### 5.7 System boundary and relevant interfaces in section 1.2 — accepted

The author approved the following criterion for both language versions:

The system boundary must not be presented merely as a list of elements classified as inside or outside the system. It must also identify relevant interfaces between the system of interest and its environment. In the water-distribution example, these may include:
- the pumping station's connection to electrical supply;
- its connection to control systems;
- connections to upstream supply infrastructure; and
- connections to downstream networks and consumption points.

The boundary may have physical, functional, operational and temporal dimensions; it need not coincide with a physical perimeter. The manuscripts should explain this at an introductory level and preserve equivalent meaning while being authored independently.

**Disposition:** accepted; manuscript integration and bilingual cross-review remain pending. No manuscript text has been changed by recording this decision.

### 5.8 Environment and context in section 1.2 — accepted

The author approved the following operational definitions for both language versions:

- **Environment:** external elements, systems and conditions that interact with the system of interest or may be affected by it.
- **Context:** the set of circumstances, relationships and conditions from which the problem and the system of interest are defined and interpreted.

The chapter must state that this distinction is an editorial working convention adopted for this book to support analysis. It is not presented as a universal separation used identically across all disciplines.

The Spanish and English manuscripts will express these definitions independently while preserving equivalent conceptual scope.

**Disposition:** accepted; manuscript integration and bilingual cross-review remain pending. No manuscript text has been changed by recording this decision.

### 5.9 Revisability of the system boundary in section 1.2 — accepted

The author approved the criterion that the system boundary is not necessarily definitive. It may be revised when analysis or evidence reveals relevant dependencies, interfaces or effects that were initially excluded.

Any revision must be justified by its relevance to the problem under examination; it must not become an arbitrary expansion of the system of interest. Both language versions should preserve this qualification and express it naturally in their independently authored text.

**Disposition:** accepted; manuscript integration and bilingual cross-review remain pending. No manuscript text has been changed by recording this decision.

### 5.10 Element and component terminology in section 1.3 — accepted

The author approved **element** as the general term for any relevant part of a system identified in the analysis. **Component** may be used as a more specific term, commonly in technical and engineering systems, for a constituent part of the system.

The distinction should remain flexible rather than being imposed as a rigid taxonomy where the disciplinary context does not require it. Both language versions should preserve the same conceptual relationship while using natural, independently authored wording.

**Disposition:** accepted; manuscript integration and bilingual cross-review remain pending. No manuscript text has been changed by recording this decision.

### 5.11 State and time in section 1.3 — accepted

The author approved the following clarification for both language versions:

A **state** is the condition of a system or element at a specified reference moment. Observations made across an interval form a sequence or trajectory of states, which can be used to examine the system's evolution and behaviour.

The text should not conflate a state with the set of observations collected over a period. Both manuscripts should preserve this distinction with independently authored, natural wording.

**Disposition:** accepted; manuscript integration and bilingual cross-review remain pending. No manuscript text has been changed by recording this decision.

### 5.12 Properties and variables in section 1.3 — accepted

The author approved the following distinction for both language versions:

- **Property:** a characteristic attributed to an element or system, such as a pump's rated capacity.
- **Variable:** a quantity or representation used to describe or track a relevant characteristic or condition, such as the flow delivered at a given moment.

The text should clarify that not every property needs to be represented by a variable, and that a variable may be used to observe changes in a property or condition over time. Both manuscripts should retain this conceptual distinction and use equivalent examples, with independently authored wording.

**Disposition:** accepted; manuscript integration and bilingual cross-review remain pending. No manuscript text has been changed by recording this decision.

### 5.13 System behaviour and evidence in section 1.3 — accepted

The author approved the following clarification for both language versions:

System **behaviour** is characterised through patterns of operation, responses or changes in state observed or inferred under specified conditions. A single observation or measurement may describe a state, but is not normally sufficient on its own to establish a pattern of behaviour. Repeated observations or other evidence appropriate to the phenomenon are generally needed.

The wording should avoid turning this into an absolute rule: the type and amount of evidence depend on the phenomenon and the question being examined. Both manuscripts should preserve the same qualification and conceptual scope, using independently authored wording.

**Disposition:** accepted; manuscript integration and bilingual cross-review remain pending. No manuscript text has been changed by recording this decision.

### 5.14 Unknown or unavailable information and deliberate omissions in section 1.3 — accepted

The author approved the following distinction for both language versions:

- **Unknown or unavailable information:** aspects for which sufficient information or accessible evidence is not available.
- **Deliberate omissions:** aspects that are known or recognised but intentionally excluded from a description or model because of its scope, purpose or chosen level of detail.

Both kinds of limitation should be documented when they may affect interpretation or conclusions. They must not be conflated: one concerns an information or evidence gap; the other concerns a representational decision.

Both manuscripts should preserve this distinction with independently authored wording and equivalent conceptual scope.

**Disposition:** accepted; manuscript integration and bilingual cross-review remain pending. No manuscript text has been changed by recording this decision.

### 5.15 Actor scope in section 1.4 — accepted

The author approved the use of **actor** in the socio-organisational sense for both language versions: a person, group or organisation that participates in the system or has a relevant influence on its functioning.

Autonomous systems, software agents and other non-human elements may form part of the system, perform functions or produce effects, but they will not automatically be classified as actors in this introductory chapter. If **agent** is used in a broader technical sense, that meaning must be made explicit.

This terminology choice is intended to keep the introductory vocabulary clear and avoid conflating socio-organisational analysis with the different conventions used in agent-based modelling. Both manuscripts should preserve the same scope and distinction, using natural, independently authored wording.

**Disposition:** accepted, integrated and verified in both language manuscripts. The Spanish and English wording was authored independently and checked for equivalent conceptual scope.


### 5.16 Actors inside or outside the system boundary in section 1.4 — accepted

The author approved the criterion that an actor may be located inside or outside the boundary of the system of interest. Whether an actor is included in the system description depends on the relevance of their interaction, influence or dependency in relation to the problem being analysed, not merely on their physical or organisational location.

Both language versions should preserve this distinction and explain that the system boundary and the analytical relevance of an actor are related but separate questions. Wording should be natural and independently authored in each language.

**Disposition:** accepted, integrated and verified in both language manuscripts. The Spanish and English wording was authored independently and checked for equivalent conceptual scope.


### 5.17 Individual and system-level capabilities in section 1.4 — accepted

The author approved the distinction for both language versions:

- **Individual capability:** the ability of an actor or component to perform an activity under specified conditions.
- **System-level capability:** the ability of the organised whole to perform an activity or achieve an outcome through the combination and coordination of its elements.

System-level capability must not be presented as the simple sum of individual capabilities. It may depend on coordination, interfaces, resources and operating conditions.

Both manuscripts should preserve this distinction with natural, independently authored wording and equivalent conceptual scope.

**Disposition:** accepted, integrated and verified in both language manuscripts. The Spanish and English wording was authored independently and checked for equivalent conceptual scope.


### 5.18 Competence, capability and effective availability in section 1.4 — accepted

The author approved the following distinction for both language versions:

- **Competence:** the knowledge and skills a person or organisation has to perform an activity.
- **Capability:** the ability or possibility to perform that activity, taking into account the means and conditions required.
- **Effective availability:** whether that capability can actually be exercised at a particular time and in a particular context, considering constraints such as authority, access, resources, workload or operational state.

The illustrative example may describe a technician who has the competence to repair a pump but lacks authorisation or tools, and therefore cannot effectively perform the repair at that moment.

Both manuscripts should preserve the conceptual distinctions and the example's meaning, using natural, independently authored wording. The text should avoid implying that these terms have one universal definition across all disciplines; they are working distinctions for this introductory chapter.

**Disposition:** accepted, integrated and verified in both language manuscripts. The Spanish and English wording was authored independently and checked for equivalent conceptual scope.


### 5.19 People as actors and as contributors of resources in section 1.4 — accepted

The author approved the following criterion for both language versions:

People should be treated first and foremost as **actors** in the system, not reduced to interchangeable resources. At the same time, people may contribute resources needed for system activities, including their time, knowledge, experience, skills or availability.

When discussing resources, the manuscripts should identify the specific contribution being made rather than referring to people themselves as resources. The distinction between a person's role as an actor and the resources they make available should remain clear.

Both versions should preserve equivalent conceptual scope through natural, independently authored wording.

**Disposition:** accepted, integrated and verified in both language manuscripts. The Spanish and English wording was authored independently and checked for equivalent conceptual scope.


### 5.20 Dependency in section 1.4 — accepted

The author approved the following working definition for both language versions:

A **dependency** exists when the functioning, availability or outcome of an activity, actor or component requires a contribution, service, state or condition provided by another element.

A dependency must be distinguished from a generic relationship: two elements may be related without one requiring the other in order to function or achieve an outcome.

Dependencies may be conditional, substitutable, reciprocal or time-sensitive, and they do not all have the same degree of criticality. Both manuscripts should preserve these distinctions with natural, independently authored wording and equivalent conceptual scope.

**Disposition:** accepted, integrated and verified in both language manuscripts. The Spanish and English wording was authored independently and checked for equivalent conceptual scope.


### 5.21 Dependencies and constraints in section 1.4 — accepted

The author approved the following distinction for both language versions:

- **Dependency:** identifies a contribution, service, state or condition that is required for an activity to be performed or an outcome to be achieved.
- **Constraint:** establishes a limit or condition that reduces the options or ways in which an activity can be performed.

Dependencies and constraints may coexist. For example, an activity may depend on an electricity supply while also being constrained by consumption limits, regulation or safety conditions.

Both manuscripts should preserve this distinction and the example's meaning through natural, independently authored wording. The text should not imply that dependencies and constraints are mutually exclusive.

**Disposition:** accepted, integrated and verified in both language manuscripts. The Spanish and English wording was authored independently and checked for equivalent conceptual scope.


### 5.22 Bilingual terminology baseline for section 1.4 — accepted

The author approved the following common terminology baseline for the Spanish and English manuscripts:

| Spanish | English |
|---|---|
| actor | actor |
| competencia | competence |
| capacidad | capability |
| disponibilidad efectiva | effective availability |
| recurso | resource |
| dependencia | dependency |
| restricción | constraint |

These terms establish conceptual equivalence, not a requirement for literal or mechanically identical phrasing. Each manuscript should retain natural language-specific wording while preserving the agreed distinctions and scope. Where a term has a different established meaning in a particular technical discipline, the chapter should make the intended working meaning clear.

**Disposition:** accepted, integrated and verified in both language manuscripts. The Spanish and English wording was authored independently and checked for equivalent conceptual scope.

## 6. Review completion status

The section-by-section conceptual review is complete for all nine sections. The status below distinguishes review completion from editorial decision, manuscript integration and verification.

| Section | Spanish / English topic | Review status | Manuscript changes |
|---|---|---|---|
| 1.1 | ¿Qué entendemos por sistema? / What Do We Mean by a System? | integrated and verified | Spanish v1.5; English v1.4 |
| 1.2 | Propósito, frontera, entorno y contexto / Purpose, Boundary, Environment and Context | integrated and verified | Spanish v1.5; English v1.4 |
| 1.3 | Elementos, estados, propiedades y comportamientos / Elements, States, Properties and Behaviours | integrated and verified | Spanish v1.5; English v1.4 |
| 1.4 | Actores, capacidades, recursos y dependencias / Actors, Capabilities, Resources and Dependencies | integrated and verified | Spanish v1.0; English v0.9 |
| 1.5 | Relaciones, interacciones y estructura del sistema / Relationships, Interactions and System Structure | integrated and verified | Spanish v1.1; English v1.0 |
| 1.6 | Sistemas abiertos, entornos cambiantes y tiempo / Open Systems, Changing Environments and Time | integrated and verified | Spanish v1.2; English v1.1 |
| 1.7 | Las descripciones de sistemas son modelos: alcance, supuestos y omisiones / System Descriptions Are Models: Scope, Assumptions and Omissions | integrated and verified | Spanish v1.3; English v1.2 |
| 1.8 | De la optimización de componentes al razonamiento a escala de sistema / From Component Optimisation to System-Level Reasoning | integrated and verified | Spanish v1.4; English v1.3 |
| 1.9 | Síntesis y preguntas de reflexión / Chapter Synthesis and Reflection Questions | decisions accepted; integration pending | no manuscript changes yet |

## 7. Next phase — editorial decisions

In accordance with the Content Model §11.3, the next phase resolves the findings before any manuscript editing.

1. Work through the sections in chapter order, starting at 1.1.
2. For each finding, distinguish: accepted correction; accepted editorial refinement; rejected proposal (with rationale); deferred item; or source/domain verification required.
3. Do not treat a candidate source as authoritative until its bibliographic identity, exact passage and relevance have been checked and, where appropriate, entered in the central reference registry.
4. Record the author's explicit decision and rationale in this log. A review recommendation does not become an accepted correction by default.
5. Once the decisions for the chapter are resolved, prepare one coordinated integration pass across both original manuscripts. Do not edit one language as the translation source of the other.
6. After integration, re-read both manuscripts, verify conceptual equivalence and update the status to integrated and then verified only when the corresponding checks have actually been completed.

**Current phase:** sections 1.1–1.8 have accepted decisions and are integrated and verified in both manuscripts. Section 1.9 has accepted conceptual decisions; its integration and verification remain pending. The chapter is not yet editorially closed.  
**Editing authorisation:** the author has authorised integration of accepted decisions into sections 1.1–1.8 and approved the section 1.9 criteria; the section 1.9 manuscript integration remains to be completed.

## 8. Resolution and manuscript integration

### 8.1 Author decisions — section 1.1

**Decision 1.1-SCOPE — accepted by the author (2026-11-27).**

The book's working scope will focus on physical, social, organisational and socio-technical systems, including systems whose behaviour is not directly observable but can be inferred from relevant evidence.

Purely conceptual systems may be mentioned as representations or analytical constructs, but will not automatically be treated as equivalent to systems operating in the world.

**Rationale:** This preserves a broad systems-engineering orientation without unnecessarily restricting the book to directly observable physical systems, while maintaining a useful distinction between systems of interest and conceptual representations.

**Implementation status:** decision recorded; wording not yet integrated into either manuscript. The remaining section 1.1 findings are still unresolved.

**Decision 1.1-ANALYTICAL-UNIT — accepted by the author (2026-11-27).**

The chapter will distinguish three concepts:
- **System of interest:** the concrete system we seek to understand or study.
- **Unit of analysis:** what observations or analysis are performed on; this may be the whole system, a subsystem, an actor or an interaction.
- **Analytical perspective:** the approach from which the system is examined, for example functional, operational, organisational or temporal.

**Rationale:** These concepts must not be conflated. The system being studied is distinct from the analytical scale or perspective selected to investigate it.

**Implementation status:** decision recorded; wording not yet integrated into either manuscript.

**Decision 1.1-EMERGENCE — accepted by the author (2026-11-27).**

The chapter will distinguish:
- **System behaviour:** any behaviour that can be observed or inferred at the system level.
- **Emergent behaviour:** behaviour or a property arising from the interactions and organisation of the whole, which cannot be adequately explained by examining each element independently.

The text must not imply that all system behaviour is necessarily emergent.

**Rationale:** This preserves emergence as an important systems concept without making it a defining feature of every system behaviour.

**Implementation status:** decision recorded; wording not yet integrated into either manuscript.

**Decision 1.1-OPERATIONAL-DEFINITION — accepted by the author (2026-11-27).**

The following working definition is accepted as the basis for both language versions:

> A system is a delimitable set of related and organised elements that interact or maintain relevant dependencies, and whose behaviour can be understood by considering both its elements and the relationships between them, within a context and over a given period.

The definition does not require every system to have an explicit purpose, all system behaviours to be emergent, or all elements to interact directly.

**Rationale:** This definition consolidates the agreed scope and the distinctions among system of interest, analytical unit, analytical perspective, system behaviour and emergent behaviour. It is intended as an operational introductory definition, not as a universal definition binding every discipline.

**Implementation status:** decision recorded; wording not yet integrated into either manuscript.

After the conceptual review of sections 1.1–1.9 is complete:
1. Review the accumulated findings for consistency and dependencies across the chapter.
2. Resolve open recommendations explicitly; do not silently convert suggestions into decisions.
3. Verify candidate sources and create or update central reference records where justified.
4. Agree the required edits for Spanish and English independently, preserving equivalent conceptual scope without translation-first drafting.
5. Apply approved changes to both manuscripts, update their versions and metadata as required, and verify the resulting files.
6. Conduct the subsequent editorial and cross-language checks under the governing Content Model.

Until that integration step is authorised and completed, the findings in this log do not alter the manuscripts or their `draft` status.


### 8.2 Section 1.4 — decisions integrated and verified (2026-11-28)

Following the author's explicit authorisation to integrate section 1.4, the accepted decisions recorded in §§5.15–5.22 were applied to both native-language manuscripts in one coordinated section-level pass.

**Spanish manuscript**
- Path: `05_ASSETS/TRANSFORMATIONAL_VALUE/book/es/part-01-understanding-transformation/ch-01-pensar-en-sistemas.md`
- Version updated: 0.9 → 1.0
- Commit: `74f933a530a183d1195554aed1260c6e53358553`
- Blob SHA after re-fetch: `8fe4f457ebf89df72b4d03674bfddb19ed9b8860`

**English manuscript**
- Path: `05_ASSETS/TRANSFORMATIONAL_VALUE/book/en/part-01-understanding-transformation/ch-01-thinking-in-systems.md`
- Version updated: 0.8 → 0.9
- Commit: `b6ba1f6acbea0624e1a4ecbd515b018e2ec2bacc`
- Blob SHA after re-fetch: `1600198265b56566afabbb2181b3b0ba44bc7b21`

**Integration checks completed**
- Actor is consistently defined in the agreed socio-organisational sense; non-human and software agents are not automatically classified as actors.
- Actors may be inside or outside the system boundary; relevance to the analytical problem, rather than location alone, determines inclusion in the description.
- Individual and system-level capabilities are distinguished; system-level capability is not treated as the sum of individual capabilities.
- Competence, capability and effective availability are distinguished.
- People are treated as actors while their specific contributions (time, knowledge, experience, skills and availability) may be described as resources.
- Dependencies are distinguished from generic relationships and from constraints; relevant dependency characteristics are retained.
- Both manuscripts express equivalent conceptual scope through independently authored wording.
- The section boundaries and surrounding chapter content were preserved; no other section was intentionally edited in this integration.

**Verification:** both files were re-fetched from the target branch after their commits. The section text, version metadata and key conceptual distinctions were checked in both files.

**Scope limitation:** this completes integration and verification for section 1.4 only. It does not complete the chapter's editorial, subject-matter or overall cross-language review gates. Sections 1.1–1.3 and 1.5–1.9 still require their accepted decisions to be integrated, followed by the applicable chapter-level reviews. Both manuscripts remain in `draft` status.

## 9. Change history

- **v0.1 — 2026-11-27:** Created the Chapter 1 conceptual review record; preserved the findings, bilingual observations, proposed resolutions and unverified source candidates for sections 1.1 and 1.2; recorded that manuscript changes have not been applied.
- **2026-11-27:** Completed the conceptual review records for sections 1.3–1.9; reconciled the completion status for all nine sections and documented the decision-resolution phase. No manuscript changes were made.
- **2026-11-28:** Integrated the accepted section 1.4 decisions independently into the Spanish and English manuscripts; updated versions to ES 1.0 and EN 0.9; re-fetched and verified both files; recorded section-level integration and verification in §8.2. Other sections remain pending integration.

### 4.5 Section 1.5 — Relaciones, interacciones y estructura del sistema / Relationships, Interactions and System Structure

**Review status:** reviewed; decisions pending  
**Manuscript changes:** none

#### Conceptual assessment

- The section develops a coherent progression from elements to relationships, interactions and system structure. Its central claim—that system behaviour depends on how elements are connected and coordinated, not only on their individual characteristics—is appropriate and consistent with sections 1.1–1.4.
- The distinction between **relationship** and **interaction** is useful: a relationship identifies a relevant link, while an interaction describes something that happens through influence or action. The distinction should be retained. However, the current wording “act or influence one another” / “actúan o influyen unos sobre otros” may suggest that interaction must be reciprocal. Interactions can be directional or asymmetric; the definition should allow one element to act on or influence another.
- The statement that a dependency can exist without continuous interaction is sound and usefully connects to section 1.4. To avoid repetition, section 1.5 should use dependency as one kind of relationship and focus on how it is represented in structure, rather than redefining it.
- The list of relationship forms is useful and appropriately illustrative, not exhaustive. Some categories can overlap: a functional connection may also carry a physical flow or embody a dependency; coordination/authority relationships may include information exchanges. The text already notes overlap, but could say explicitly that the categories are analytical lenses, not mutually exclusive classes.
- The section's definition of **system structure** is sound and broader than physical layout. It appropriately includes functional connections, information flows, operational dependencies and coordination mechanisms. Consider keeping the distinction between structure (the relatively enduring configuration of relationships) and interactions (activities or influences occurring through those relationships) clear without suggesting that structure is necessarily static.
- The discussion of structure shaping behaviour is strong. The water-network failure and local optimisation examples demonstrate propagation and system-level trade-offs. The examples should remain illustrative rather than imply that every local change produces a system-wide adverse effect.
- The feedback-loop explanation is broadly correct for an introductory chapter: an outcome returns to influence a process or its regulation. The definition could be made slightly more precise by referring to a closed chain of influence in which a change in an outcome affects subsequent operation. The distinction from a mere return arrow in a diagram is important and should remain.
- The feedback example is understandable, but the diagram and prose should not imply that a sensor reading alone establishes the full state of the network. Measurements are information used to infer or monitor operating conditions; this nuance may be worth retaining if the section is revised.
- The representation guidance is particularly valuable: node and edge meanings, directionality, omitted relationships and diagram scope must be explicit. This should be retained as a general modelling principle.

#### Example and bilingual-equivalence observations

- The Spanish and English versions are closely aligned in structure, argument, examples and learning outcome. No material conceptual divergence was identified.
- “Relación” / “relationship” and “interacción” / “interaction” are appropriate equivalents. Both versions should make the directionality point consistently.
- The examples of physical flow, sensor information, control action, maintenance dependency, network failure and local optimisation are equivalent in substance.
- “Puntos de consumo” / “points of use” are broadly equivalent in this section's context. Maintain consistent naming for the water-network entities across the chapter, but no section-specific correction is essential here.
- “Bucles de realimentación” / “feedback loops” are suitable equivalents. The definition and example should be adjusted in parallel if the author accepts the precision improvement.
- Both versions refer to the supporting visual as TV-DIA-002. The asset README identifies it as **Draft — conceptual and visual review pending**. The chapter must not imply that the diagram is approved or publication-ready. Its status and pending checks must be respected; do not modify or remove the asset without separate explicit authorisation.

#### Proposed resolution

A. **Relationship and interaction:** retain the distinction, but revise the interaction definition in both languages so that an interaction may be directional or asymmetric; it need not involve reciprocal influence.

B. **Relationship categories:** retain the illustrative list and state that categories may overlap and are not mutually exclusive. Keep physical flows, information flows, functional connections, dependencies and coordination/authority relationships distinguishable by their meaning in a particular model.

C. **Structure and interaction:** clarify, if needed, that structure describes the configuration of relevant relationships, while interactions describe actions, exchanges or influences occurring through or changing those relationships. Avoid presenting structure as necessarily fixed.

D. **Dependencies:** refer back to section 1.4 for the concept of dependency. In 1.5, focus on dependencies as a structural relationship and on their representation, avoiding unnecessary duplication.

E. **Feedback:** retain the closed-loop criterion and the warning against interpreting any return arrow as feedback. Consider tightening the definition to make clear that an outcome influences subsequent operation or regulation. Preserve the possibility of both stabilising and amplifying effects without introducing a full treatment of feedback-loop taxonomy at this stage.

F. **Measurements:** where the sensor example is refined, describe readings as evidence used to monitor or infer operating conditions, not as a complete representation of system state.

G. **Diagram governance:** retain the TV-DIA-002 reference provisionally, but treat the visual as a draft asset. Its conceptual/visual review, bilingual rendering, accessibility, provenance/licensing and publication checks remain open under its own asset record. No change to TV-DIA-002 is authorised by this chapter review.

H. **Bilingual alignment:** apply any accepted conceptual edits independently to both original manuscripts, preserving equivalent scope and examples rather than translating one version from the other.

#### Candidate sources — verification pending

No external source has yet been selected for this section. If a formal source is considered necessary for feedback, system structure or relationship/interaction distinctions, verify an authoritative systems-engineering or systems-dynamics reference and its exact edition and passages before recording it in the central references registry. No source is approved or attached to a claim at this stage.

**Decision:** pending author review. No source has yet been formally attached to a claim.

### 4.6 Section 1.6 — Sistemas abiertos, entornos cambiantes y tiempo / Open Systems, Changing Environments and Time

**Review status:** conceptual decisions accepted; integrated and verified in both language manuscripts  
**Manuscript changes:** section 1.6 integrated in Spanish v1.2 and English v1.1; both files re-fetched and checked

#### Conceptual assessment

- The section provides a coherent account of systems as bounded for analysis yet connected to their environments through exchanges. It correctly avoids treating a boundary as a barrier that eliminates external dependencies.
- The working definition of an **open system** is suitable for this introductory chapter: exchanges of matter, energy, information, resources or services are relevant to operation. It may be useful to signal that openness is considered relative to the chosen system boundary and analytical purpose; the same system may be modelled with different boundaries and exchange sets for different questions. Avoid turning this into a rigid binary classification.
- The distinction among inputs, outputs and exchanges is useful, but the table currently mixes exchange categories with a final row labelled “outputs to the environment” / «resultados hacia el entorno». Outputs are already part of the input/output framing, whereas the other rows classify types of flow. Consider either making the table consistently about exchange types or explicitly distinguishing inputs and outputs from the types of exchanged content. The current text defines these terms but does not fully clarify the table's mixed classification.
- The warning that an input is not necessarily a sufficient condition for operation is important and should be retained. It connects well with section 1.4's treatment of capabilities and dependencies: availability of one required input does not guarantee that the system can perform its function.
- The treatment of environmental change is sound and includes relevant external drivers. The reciprocal influence between system and environment is also important; retain the point that system-environment influence need not be one-way.
- The temporal discussion correctly distinguishes short-, medium- and long-term scales as relative to the system and analytical question. It appropriately warns against interpreting a point observation as a persistent pattern. A concise clarification could distinguish the observation time, the period represented by the data and the time horizon over which a conclusion is intended to apply.
- The discussion of disturbances and responses is useful, but **adaptation** should not be read as necessarily intentional, successful or beneficial. A system may adjust, reorganise or fail to maintain expected performance. If the term is retained, clarify that the section describes different response patterns rather than presuming that every response constitutes successful adaptation.
- The contrast between an operational response and a more lasting transformation is valuable and relevant to the wider book. However, the text should avoid implying that duration alone defines transformation: a structural change may be rapid, and a long-lasting operational adjustment may not amount to a structural transformation. The distinction should be tied to the nature and persistence of the change, not only to elapsed time.
- The “snapshot and moving picture” explanation is accessible and pedagogically effective. It reinforces the earlier treatment of states and behaviour and should be retained. Its value depends on maintaining the distinction between a configuration observed at one time and evidence of change or behaviour across a defined period.

#### Example and bilingual-equivalence observations

- The Spanish and English versions are closely aligned in structure, reasoning, examples and learning outcome. No major conceptual divergence was identified.
- “Sistemas abiertos” / “open systems”, “entradas” / “inputs”, “salidas” / “outputs” and “intercambios” / “exchanges” are appropriate equivalents.
- The table's final row, “Resultados hacia el entorno” / “Outputs to the environment”, is broadly equivalent but not perfectly parallel in terminology. Align the Spanish label with the chosen input/output/exchange structure.
- The examples of drought, heatwave, regulatory change and power interruption are equivalent in substance.
- “Perturbaciones” / “disturbances” and “adaptación” / “adaptation” are suitable equivalents, but any clarification that adaptation is not necessarily intentional or successful should be made in both texts.
- The contrast between a temporary pump adjustment and a more lasting network redesign is equivalent. If the conceptual distinction is refined, both versions should make clear that structural nature and persistence matter more than duration alone.
- The snapshot/time-based representation and the reflection question are equivalent and appropriately reinforce the same temporal reasoning.

#### Proposed resolution

A. **Openness and boundary:** retain the working definition of open systems, while briefly clarifying that relevant exchanges are identified relative to the chosen boundary and analytical purpose. Avoid treating openness as an absolute property independent of the model.

B. **Inputs, outputs and exchanges:** revise the table so that its organising principle is consistent. Either classify rows by type of exchanged content and label inputs/outputs separately, or make clear that inputs and outputs are directions/roles of exchange rather than additional material categories. Harmonise the Spanish and English labels.

C. **Input versus sufficiency:** retain the warning that receiving an input does not guarantee operation. Preserve the link to capabilities and dependencies developed in section 1.4 without repeating their definitions.

D. **System-environment influence:** retain the bidirectional influence point and the examples of effects a system may have on its environment.

E. **Temporal evidence:** preserve the relative short-, medium- and long-term scales. Consider stating explicitly the distinction among the time of observation, the period covered by evidence and the horizon to which conclusions apply.

F. **Adaptation and response:** clarify that the response categories (absorbing variation, adjusting operation, reorganising, or losing expected performance) do not all imply successful adaptation. Avoid anthropomorphic or teleological wording.

G. **Operational response and transformation:** retain the distinction, but do not define transformation by duration alone. Consider distinguishing temporary operating adjustments from changes in system configuration or organisation that persist, while recognising that persistence and structural significance are separate dimensions.

H. **Bilingual alignment:** make any accepted changes independently in both original manuscripts, maintaining equivalent concepts, table logic and examples rather than translating one version from the other.

#### Candidate sources — verification pending

No external source has yet been selected for this section. If a formal source is considered necessary for open-system boundaries, system-environment exchanges, adaptation or temporal system behaviour, verify an authoritative systems-engineering, systems-theory or systems-dynamics reference and its exact edition and passages before recording it in the central references registry. No source is approved or attached to a claim at this stage.

**Decision:** pending author review. No source has yet been formally attached to a claim.

### 4.7 Section 1.7 — Las descripciones de sistemas son modelos: alcance, supuestos y omisiones / System Descriptions Are Models: Scope, Assumptions and Omissions

**Review status:** reviewed; decisions pending  
**Manuscript changes:** none

#### Conceptual assessment

- The central proposition—that a system description is a selective representation rather than the system itself—is sound and well placed after sections on boundaries, relationships and temporal behaviour. The section explains why simplification is necessary without equating simplification with poor quality.
- The relationship between analytical purpose and model scope is clearly presented. The table is useful because it shows that different questions about the same water network call for different representations. Retain it as a teaching device.
- The term **model** is used broadly to include prose, diagrams, tables, variable sets and mathematical models. This is defensible for an introductory chapter, but readers may associate “model” primarily with formal or mathematical representations. Consider stating explicitly that the chapter uses the term in this broad sense: any purposeful, selective representation can function as a model.
- The section could make a sharper distinction between **scope**, **boundary** and **level of detail**. Scope concerns what the representation covers for a given question; boundary identifies what is treated as inside or outside the system of interest; level of detail concerns how finely included elements and relationships are represented. They are related but not interchangeable.
- The treatment of assumptions is particularly strong in distinguishing assumptions from observed facts and quantified uncertainty. It could also distinguish an assumption from a model input or parameter: an input may be measured, estimated, specified or assumed. Not every value supplied to a model is an assumption.
- The statement that assumptions should be recorded, justified and tested where possible is appropriate. Sensitivity analysis is implied by examining how conclusions change when assumptions vary; the text need not introduce the technical term unless it is useful for the intended audience.
- The treatment of omissions is sound. A useful further distinction is between something deliberately excluded for scope or simplicity and something absent because it is unknown or not represented due to lack of evidence. These cases should not be conflated: an unknown dependency is not necessarily a deliberate modelling choice. This also connects to section 1.3's distinction between unavailable information and deliberate omission.
- The example of omitting electricity dependency is effective because it demonstrates how a model can be adequate for one question and inadequate for another. Retain it.
- The suitability checklist is practical and appropriately avoids claiming that a model can be guaranteed correct by following it. Consider distinguishing **evidence supporting the model's inputs and relationships** from **evidence that the model adequately represents the relevant system behaviour**. The presence of evidence for individual data does not by itself establish model adequacy.
- The subsection on revisiting models when the question or system changes is valuable. The discussion of complementary hydraulic and socio-technical models could add a concise caution: combining models requires checking differences in boundaries, assumptions, time horizons, terminology and level of detail. Otherwise, integration may create apparent consistency where the underlying representations are not compatible.
- The section is appropriately introductory and does not need a taxonomy of model types, validation methods or uncertainty analysis. The priority is to clarify the distinctions above without expanding the chapter disproportionately.

#### Example and bilingual-equivalence observations

- The Spanish and English versions are closely aligned in structure, reasoning, table content, examples and learning outcome. No material conceptual divergence was identified.
- “Modelo” / “model”, “alcance” / “scope”, “supuestos” / “assumptions” and “omisiones” / “omissions” are appropriate equivalents.
- “Esquema de la red” / “network layout” are functionally equivalent in the table, although “layout” can suggest a spatial arrangement. If the intended representation is specifically connectivity and flow direction, consider a more precise equivalent in both languages.
- “Zonas de consumo” / “consumption areas” are equivalent in substance. Maintain consistency with the water-network terminology used in earlier sections.
- The assumption example concerning equipment availability, the electricity-dependency omission and the shift from hydraulic flow to service resilience are equivalent.
- The distinction between model evidence and model adequacy, and the distinction between deliberate omission and unknown information, should be expressed in both versions if accepted.

#### Proposed resolution

A. **Broad use of model:** retain the broad definition but state briefly that “model” is used here for any purposeful, selective representation, not only mathematical or computational models.

B. **Scope, boundary and detail:** add concise distinctions among the scope of a representation, the system boundary adopted for the analysis and the level of detail used within that scope.

C. **Assumptions and inputs:** retain the distinction between assumptions, observations and quantified uncertainty. Clarify, if useful, that model inputs or parameters may be measured, estimated, specified or assumed; they are not automatically assumptions.

D. **Omissions and unknowns:** distinguish deliberate exclusions from information that is unknown, unavailable or unsupported by evidence. Cross-reference the conceptual distinction established in section 1.3 without repeating it at length.

E. **Evidence and adequacy:** refine the checklist so that evidence for input data and relationships is not confused with evidence that the representation is adequate for the question and relevant behaviour. Do not imply that a checklist guarantees correctness.

F. **Complementary models:** retain the hydraulic and socio-technical examples. Add a brief note that combining representations requires checking compatibility of boundaries, assumptions, time horizons, terminology and levels of detail.

G. **Bilingual alignment:** preserve equivalent conceptual distinctions and examples in both original manuscripts. Review the translation-equivalence of “network layout” / «esquema de la red» if the wording is changed.

H. **Editorial restraint:** do not expand this introductory section into a formal taxonomy of modelling, validation or uncertainty methods. Keep the focus on purpose, scope, assumptions, omissions and limits of use.

#### Candidate sources — verification pending

No external source has yet been selected for this section. If a formal source is considered necessary for model purpose and scope, assumptions, model validation or uncertainty, verify an authoritative systems-engineering or modelling reference and its exact edition and passages before recording it in the central references registry. No source is approved or attached to a claim at this stage.

**Decision:** pending author review. No source has yet been formally attached to a claim.

### 4.8 Section 1.8 — De la optimización de componentes al razonamiento a escala de sistema / From Component Optimisation to System-Level Reasoning

**Review status:** reviewed; decisions pending  
**Manuscript changes:** none

#### Conceptual assessment

- The central argument is sound and well positioned: improving a component or subsystem does not guarantee improvement in overall system performance. The water-pump example makes the possibility of transferred costs, constraints and effects concrete without requiring advanced technical knowledge.
- The section correctly avoids the opposite error of dismissing component optimisation. Local optimisation remains necessary; the issue is treating a local indicator as a proxy for system performance. Retain this qualification.
- There is a terminology inconsistency between the section's framing as **system-level reasoning** and the table's definition of **system-level optimisation**. These are related but not identical. Reasoning at system level is an approach to framing and evaluating decisions; optimisation is a more specific task of selecting the best feasible option against defined criteria and constraints. The text should either define the relationship or use “system-level reasoning” consistently where it describes the broader approach.
- The table's three levels (component, subsystem, system) are useful as analytical levels, not as a mandatory hierarchy or mutually exclusive decomposition. It may help to state that the appropriate level depends on the decision and that relevant effects can cross levels and boundaries. The existing paragraph already points in this direction.
- The phrase “results that cross internal boundaries” / «resultados que atraviesan sus fronteras internas» is potentially imprecise: results do not necessarily cross boundaries; interactions, flows, constraints and effects may cross interfaces or boundaries between components and subsystems. Consider revising the wording in both languages.
- The treatment of interfaces, constraints and bottleneck displacement is strong. The example correctly illustrates that resolving one constraint can reveal another, but this is not inevitable in every intervention. The conditional wording should be retained and examples should not be read as universal laws.
- The section identifies multiple performance criteria and trade-offs, including service continuity, quality, pressure, energy, operating cost, recovery time and environmental effects. This is a valuable corrective to single-metric optimisation. Consider distinguishing **requirements** (conditions that must be met), **objectives** (outcomes to improve) and **preferences** (trade-offs that may be negotiated), as the text already begins to do. Ensure that non-negotiable safety, regulatory or service constraints are not presented as ordinary preferences.
- The process sequence is practical and coherent. Step 1, “what the system must achieve and for whom”, should not imply that a system always has one uncontested purpose or a single beneficiary. Relevant actors may have different or conflicting needs. A concise acknowledgement of this would strengthen the connection with sections 1.2 and 1.4.
- Step 5's “whether the improvement is sustained, shifted elsewhere or creates unintended consequences” is useful, but should not suggest that every consequence can be predicted in advance. It is an invitation to examine plausible effects and monitor actual outcomes under appropriate conditions.
- The paragraph on the value of an improvement is important as a bridge to the book's wider subject. However, the wording “a technical improvement becomes meaningful when related to the outcomes...” should not be read as a full definition of value or as a claim that technical performance automatically creates value. The relevance of an outcome depends on whose needs are considered, which constraints apply and how benefits, costs and risks are distributed. Keep this as an introductory bridge, not a premature definition of value construction.
- The closing idea is appropriate. No additional diagram is necessary: the existing table and six-step sequence provide sufficient visual/structural support for this section.

#### Example and bilingual-equivalence observations

- The Spanish and English versions are closely aligned in structure, reasoning, examples, table and practical sequence. No material conceptual divergence was identified.
- “Optimización local” / “local optimisation”, “optimización a escala de sistema” / “system-level optimisation” and “razonamiento a escala de sistema” / “system-level reasoning” are natural equivalents, but the conceptual distinction between optimisation and reasoning should be made explicit in both versions.
- The phrase “resultados que atraviesan sus fronteras internas” / “outcomes that cross internal boundaries” is equivalent but potentially imprecise in both languages. Revise both consistently if accepted.
- The pump capacity, pressure, energy, maintenance and bottleneck examples are equivalent in substance.
- “Requisitos, objetivos y preferencias” / “requirements, objectives and preferences” are appropriate equivalents. Any clarification that mandatory constraints are not negotiable preferences should be made in both.
- “Para quién” / “for whom” is equivalent. Both versions should acknowledge that relevant actors may have different or conflicting needs if this point is added.
- The final discussion of the value of an improvement is aligned. Any qualification that this is not yet a definition of value or proof of value creation should be expressed in both versions.

#### Proposed resolution

A. **Local optimisation:** retain the statement that component optimisation remains necessary. The section critiques isolated evaluation, not technical improvement at component level.

B. **Optimisation versus reasoning:** distinguish system-level reasoning from system-level optimisation. Use the former for the broad decision approach; reserve the latter for explicit optimisation against defined objectives and constraints. Align the table terminology with this distinction.

C. **Analytical levels:** retain component, subsystem and system as useful levels of analysis, while clarifying that they are not a compulsory hierarchy and that relevant effects may cross their interfaces.

D. **Interfaces and boundaries:** revise the wording about “outcomes crossing internal boundaries” so it refers more accurately to interactions, flows, constraints or effects crossing interfaces/boundaries.

E. **Constraints and trade-offs:** retain the multi-criteria discussion and distinguish mandatory requirements/constraints from objectives and negotiable preferences. Do not imply that safety, regulatory or essential service requirements can be traded away as preferences.

F. **Purpose and beneficiaries:** qualify “what the system must achieve and for whom” to recognise that relevant actors may have different or conflicting needs. Preserve the link to sections 1.2 and 1.4 without duplicating them.

G. **Consequences and evidence:** retain the review of sustained, displaced and unintended effects, but present it as analysis of plausible consequences followed by observation/monitoring, not as a guarantee that all effects can be predicted.

H. **Bridge to value:** retain the final subsection, but make clear that technical improvement is not automatically value creation and that outcomes must be considered in relation to relevant actors, needs, constraints and distribution of benefits, costs and risks. Do not introduce a full definition of value in this chapter.

I. **Bilingual alignment and editorial restraint:** apply accepted refinements independently to both original manuscripts. The existing table and process sequence are sufficient; no additional visual asset is recommended for this section.

#### Candidate sources — verification pending

No external source has yet been selected for this section. If a formal source is considered necessary for local versus system-level optimisation, multi-criteria decision-making or systems engineering trade-offs, verify an authoritative reference and its exact edition and passages before recording it in the central references registry. No source is approved or attached to a claim at this stage.

**Decision:** pending author review. No source has yet been formally attached to a claim.

### 4.9 Section 1.9 — Síntesis y preguntas de reflexión / Chapter Synthesis and Reflection Questions

**Review status:** reviewed; decisions pending  
**Manuscript changes:** none

#### Conceptual assessment

- The synthesis accurately captures the chapter's progression: from system purpose and composition through relationships, boundaries, environment, time, models and evidence, to the evaluation of interventions beyond the component being changed. It is an effective consolidation rather than a new exposition.
- The integrated table is useful and proportionate. It provides a compact set of dimensions without claiming to be exhaustive. Retain it.
- The table should be checked against the decisions made in sections 1.1–1.8 before manuscript integration. In particular, terminology for actors and capabilities, boundaries and exchanges, model scope and evidence, and system-level reasoning should use the final agreed formulations. The synthesis should not preserve wording that the detailed reviews later refine.
- The row “Composition and capabilities” / «Composición y capacidades» is slightly compressed: it combines elements, actors, resources and capabilities. This is appropriate for a summary, but the phrase “what each part contributes” / «qué puede aportar cada parte» may blur the distinction between an actor, a resource contributed by an actor and a system-level capability emerging from coordination. A small wording refinement could preserve the summary while reflecting section 1.4.
- The “Boundary and environment” row correctly includes exchanges crossing boundaries. Ensure that it remains consistent with the final section 1.6 distinction between exchange types and the direction/role of inputs and outputs.
- The “Model and evidence” row is strong, but “fitness for purpose” / «adecuación al propósito» should refer to the adequacy of the representation for the analytical question, not to the quality or success of the real system. This distinction should be clear in the final wording.
- The exercise asking the reader to describe a familiar system is appropriate and actionable. The instruction to distinguish what is known, assumed or not yet examined is especially valuable and consistent with sections 1.3 and 1.7. Retain it.
- The five reflection questions cover the chapter well. Question 1 could acknowledge that relevant actors may have different or conflicting expectations about outcomes, following the review of section 1.8. Question 2 should preserve the distinction between external dependencies and internal structure. Question 4 appropriately asks about assumptions and omissions; it may also prompt the reader to consider whether omissions are deliberate or due to lack of information. These are refinements, not reasons to add more questions.
- The closing paragraph is conceptually sound. “The configuration ... that makes a particular behaviour possible” / «la configuración ... que hace posible un determinado comportamiento» is an effective synthesis of the systems perspective.
- The transition to chapter 2 is logical, but it should be checked against the actual scope and opening of chapter 2 when that chapter is reviewed. In particular, “transformation as a system capability” should not prematurely imply that all transformations are capabilities already available to the system; the next chapter should clarify the difference between existing capability and capability to be developed or enabled.
- No additional diagram or illustration is needed in this synthesis section. The integrated table already provides the appropriate visual summary.

#### Example and bilingual-equivalence observations

- The Spanish and English versions are closely aligned in structure, dimensions, exercise, reflection questions and closing transition. No material conceptual divergence was identified.
- “Comprender el sistema antes de intervenir” / “Understanding the system before changing it” are close equivalents, though “intervening” and “changing” have slightly different connotations. Either is acceptable; keep the chosen title aligned with the chapter's established terminology.
- “Una visión integrada” / “Bringing the dimensions together” are conceptually equivalent.
- “Rendimiento del conjunto” / “Overall performance” are appropriate equivalents, subject to the terminology decision in section 1.8 about system-level reasoning versus optimisation.
- “Adecuación al propósito” / “fitness for purpose” are equivalent, but should be anchored to the model/representation rather than to the system itself.
- “Qué puede aportar cada parte” / “what each part contributes” are equivalent but may obscure the actor/resource/capability distinctions identified in section 1.4. Refine in parallel if accepted.
- The exercise and five reflection questions are equivalent in substance. Any addition about conflicting actor expectations or deliberate versus information-driven omissions should be made in both original manuscripts.
- The closing transition is equivalent. Its wording should be reconciled with chapter 2's conceptual framing during cross-chapter review.

#### Proposed resolution

A. **Integrated table:** retain the table, but perform a terminology reconciliation after decisions on sections 1.1–1.8 are resolved. It should reflect the final agreed distinctions and should not introduce new concepts.

B. **Actors, resources and capabilities:** refine the composition/capabilities row so that it does not collapse actors, resources they contribute and system capabilities into one undifferentiated “part”.

C. **Boundary and exchanges:** align the boundary/environment row with the final classification of exchanges, inputs and outputs adopted in section 1.6.

D. **Model adequacy:** make explicit that fitness for purpose concerns whether the representation is adequate for the question and intended use, not whether the real system itself is fit for purpose.

E. **Reflection questions:** retain five questions. Consider adding within the existing questions (not as extra questions) the possibility of conflicting actor expectations and the distinction between deliberate omissions and unknown/unavailable information.

F. **Chapter 2 transition:** retain the transition provisionally. Revisit it when chapter 2 is available for review, checking that “transformation as a system capability” distinguishes existing capability from capability that may need to be developed or enabled.

G. **Visual support:** no additional visual asset is recommended; the synthesis table is sufficient.

H. **Bilingual alignment:** make any accepted changes independently in both original manuscripts, preserving equivalent scope and terminology rather than translating one version from the other.

#### Candidate sources — verification pending

No external source is required specifically for this synthesis. Any references added to support substantive claims in sections 1.1–1.8 should be linked at the relevant point in those sections and registered centrally; the synthesis should not duplicate the references registry or introduce unsupported claims.

**Decision:** pending author review. No source has yet been formally attached to a claim.


### 5.23 Section 1.5 — relationship and interaction directionality — accepted

The author approved the proposed clarification for both language versions:

- **Relationship:** a relevant link between two or more elements.
- **Interaction:** an action, exchange or influence occurring between related elements. An interaction may be unidirectional, reciprocal or asymmetric; it does not require equivalent influence in both directions.

The examples of a sensor transmitting a measurement to a monitoring system, a control system sending a command to a pump, and a manager's decision changing a team's activity illustrate directional interactions.

**Rationale:** The wording must not imply that interaction necessarily involves mutual or reciprocal influence.

**Disposition:** accepted. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.24 Section 1.5 — relationship categories may overlap — accepted

The author approved retaining the illustrative relationship forms in both language versions: physical flows, information flows, functional connections, dependencies, and coordination or authority relationships. These are analytical perspectives that may overlap; they are not mutually exclusive categories.

For example, a functional relationship may also involve a physical flow and a dependency, while an authority relationship may include information exchanges. The categories should remain distinguishable by the meaning they serve in a particular system representation, without implying that each relationship belongs to only one class.

**Rationale:** The classification is intended to help readers examine relationships from different analytical perspectives, not to impose a rigid or exhaustive taxonomy.

**Disposition:** accepted. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.25 Section 1.5 — system structure and interaction — accepted

The author approved the following distinction for both language versions:

- **System structure:** the configuration of relevant relationships among the system's elements.
- **Interactions:** actions, exchanges or influences occurring through those relationships, which may affect how the system operates and, in some circumstances, may change the structure itself.

Structure may be relatively stable, but it is not necessarily fixed or immutable. The wording should preserve the distinction between the configuration of relationships and what happens through them, without presenting the two as wholly independent.

**Rationale:** This clarifies the different analytical roles of structure and interaction while recognising that interactions can reproduce or alter structural relationships over time.

**Disposition:** accepted. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.26 Section 1.5 — dependencies as structural relationships — accepted

The author approved treating dependencies in section 1.5 as a relevant form of structural relationship, without redefining the term. The operational definition established in section 1.4 remains authoritative for this chapter. Section 1.5 should focus on how dependencies connect system elements and how they are represented as part of system structure.

**Rationale:** This maintains conceptual continuity between sections 1.4 and 1.5, avoids unnecessary repetition, and keeps the focus of section 1.5 on relationships and their structural representation.

**Disposition:** accepted. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.27 Section 1.5 — feedback-loop definition — accepted

The author approved the following clarification for both language versions: a **feedback loop** exists when a closed chain of influences causes an outcome of the system to affect its subsequent operation or regulation.

Two qualifications must be retained:
- A return arrow in a diagram is not sufficient by itself; there must be a chain of influence that closes the loop.
- Feedback may have stabilising or amplifying effects. It does not necessarily correct or reduce variation.

The explanation should remain introductory and should not expand into a technical taxonomy of feedback loops.

**Rationale:** This provides a more precise operational explanation of feedback while preventing readers from equating it with any graphical return connection or assuming that all feedback is corrective.

**Disposition:** accepted. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.28 Section 1.5 — measurements and system state — accepted

The author approved clarifying the sensor example in both language versions: a **measurement reading is not equivalent to the complete state of the system**. A measurement provides information about a particular variable or condition. It may be used, together with other measurements, observations and knowledge of system operation, to monitor or infer the network's operating conditions. By itself, however, it does not represent every relevant dimension of the system's state.

**Rationale:** This prevents a single sensor reading from being treated as a complete representation of a complex system and reinforces the distinction between measured variables and system state.

**Disposition:** accepted. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.29 Section 1.5 — bilingual terminology and conceptual review closure — accepted

The author approved the following common terminology baseline for both language versions:

| Español | English |
|---|---|
| relación | relationship |
| interacción | interaction |
| estructura del sistema | system structure |
| dependencia | dependency |
| realimentación | feedback |
| bucle de realimentación | feedback loop |
| medición | measurement |
| estado del sistema | system state |

The equivalence is conceptual rather than a requirement for literal translation. Each manuscript should retain natural, independently authored wording while preserving the agreed distinctions and equivalent scope.

The author also approved closing the **conceptual decision phase** for section 1.5, subject to manuscript integration and subsequent editorial checks. TV-DIA-002 remains a draft asset; this decision does not modify it or authorise its publication.

**Disposition:** terminology baseline accepted; conceptual review decisions for section 1.5 closed. Manuscript integration remains pending. No manuscript text or visual asset has been changed by this decision.


### 5.30 Section 1.5 — manuscript integration and verification — completed

The approved section 1.5 decisions have been integrated independently into both original-language manuscripts. The Spanish and English texts were revised as separate authored versions and then checked for conceptual equivalence.

Integration includes: relationship versus interaction; directional, reciprocal and asymmetric interactions; overlapping relationship categories; structure as the configuration of relevant relationships; interaction as activity occurring through those relationships and potentially changing them; dependencies treated structurally without redefining the term from section 1.4; feedback-loop closure and stabilising/amplifying effects; and the distinction between an individual measurement and the system's complete state.

The TV-DIA-002 reference remains in both sections. The asset itself was not modified, and this integration does not approve its publication or change its draft status.

**Manuscripts updated:**
- Spanish: `05_ASSETS/TRANSFORMATIONAL_VALUE/book/es/part-01-understanding-transformation/ch-01-pensar-en-sistemas.md`, version 1.1.
- English: `05_ASSETS/TRANSFORMATIONAL_VALUE/book/en/part-01-understanding-transformation/ch-01-thinking-in-systems.md`, version 1.0.

Both files were fetched again after the commits. Their version metadata and the accepted conceptual changes were checked in the persisted section 1.5 text. The bilingual review confirms equivalent conceptual scope while preserving independent wording.

**Disposition:** section 1.5 integration completed and verified. This does not close the chapter or authorise progression to chapter 2; other section integrations and subsequent editorial phases remain pending.


### 5.31 Section 1.6 — openness relative to boundary and analytical purpose — accepted

The author approved the clarification for both language versions that system openness must be understood relative to the selected system boundary and the purpose of the analysis. Relevant exchanges of matter, energy, information, resources or services are identified in relation to that boundary and analytical question.

The text should make clear that:
- Openness is not an absolute property independent of how the system is delimited.
- The exchanges considered relevant depend on the chosen boundary and the question guiding the analysis.
- The section should not impose a rigid open/closed classification; its emphasis is on identifying the exchanges relevant to the analysis.

The example of an organisation considered first as a whole and then through one of its facilities may illustrate how exchanges previously internal to the larger system cross the boundary of the narrower system of interest.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.

### 5.32 Section 1.6 — direction and nature of exchanges — accepted

The author approved the distinction for both language versions between the direction of an exchange and the nature of what is exchanged:

- **Inputs:** what crosses the selected system boundary into the system of interest.
- **Outputs:** what crosses the selected system boundary from the system of interest into its environment.
- **Types of exchange:** matter, energy, information, resources or services. Any of these may be an input or an output depending on the system and the analytical boundary.

The existing table should be reorganised so that direction (input/output) is not mixed with the nature or category of the exchanged item. The wording should remain consistent with the boundary-relative treatment of openness accepted in section 5.31.

**Rationale:** This separates two different classification dimensions and avoids presenting “results towards the environment” as if it were the same kind of category as matter, energy or information.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.

### 5.33 Section 1.6 — inputs and effective operating conditions — accepted

The author approved clarifying in both language versions that receiving an input does not, by itself, mean that the system has the conditions required to use it or operate effectively.

For example, a facility may receive an electricity supply but remain unable to operate because personnel are unavailable, its control system is faulty, or an operational constraint prevents use.

The explanation should distinguish the existence of an exchange across the system boundary from the system's effective ability to make use of that input under the relevant operating conditions.

**Rationale:** The presence of a resource or service at the boundary does not establish that the system can access, integrate or use it to perform its functions.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.

### 5.34 Section 1.6 — temporal references in system analysis — accepted

The author approved distinguishing three temporal references in both language versions:

1. **Observation time:** when a measurement is taken or a system state is recorded.
2. **Data coverage period:** the time interval from which the evidence used in the analysis is drawn.
3. **Conclusion horizon:** the period to which the analysis's interpretations or conclusions apply.

The explanation should make clear that these references are related but not interchangeable. A point measurement does not, by itself, establish that an operating condition or behaviour persists over a longer period. Conclusions should be proportionate to the temporal coverage and nature of the available evidence.

**Rationale:** This prevents a measurement taken at one moment, or evidence covering a limited interval, from being used to support conclusions that imply persistence or validity over a substantially longer horizon without adequate justification.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.

### 5.35 Section 1.6 — response to change and adaptation — accepted

The author approved distinguishing **response to change** from **adaptation** in both language versions:

- **Response to change:** a modification in the system's behaviour or state following an internal or external variation.
- **Adaptation:** a response that modifies characteristics, capabilities, relationships or ways of operating so that the system can cope with changing conditions.

The text should not imply that every response is an adaptation or that adaptation is necessarily successful, beneficial or intentional. An adaptation may be insufficient, unsuccessful or produce unintended consequences. It may also emerge through distributed adjustments or unplanned processes rather than deliberate action.

**Rationale:** This preserves the distinction between reacting to a change and developing or modifying the system in ways that affect how it copes with changing conditions, without assuming that such changes lead to improved performance.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.

### 5.36 Section 1.6 — operational response and transformation — accepted

The author approved distinguishing an **operational response or adjustment** from a **transformation** in both language versions. The distinction should be based on the nature and scope of the change, not solely on how long it lasts:

- **Operational response or adjustment:** a modification of the system's state, behaviour or operating parameters that does not necessarily alter its fundamental configuration.
- **Transformation:** a change that significantly modifies the system's configuration, organisation, relationships or capabilities and may therefore alter what the system is able to do.

Duration may be relevant evidence, but it is not the decisive criterion. A brief change may trigger a structural transformation, while a prolonged modification may remain an operational adjustment.

**Rationale:** This avoids classifying changes as transformations merely because they persist over time and keeps the distinction focused on changes to the system's organisation and capabilities.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.

### 5.37 Section 1.6 — conceptual decision phase closed — accepted

The author approved closing the conceptual decision phase for section 1.6 after resolving all six review questions:

1. System openness relative to the selected boundary and analytical purpose.
2. The distinction between inputs, outputs and types of exchange.
3. The difference between receiving an input and having the conditions required to use it.
4. The distinction between observation time, data coverage period and conclusion horizon.
5. The distinction between response to change and adaptation.
6. The distinction between operational adjustment and transformation, based on the nature and scope of change rather than duration alone.

The accepted decisions apply to both the Spanish and English manuscripts. The next stage is to integrate the decisions independently into each original-language manuscript, then verify their conceptual equivalence and update this log with the integration and verification evidence.

**Disposition:** conceptual decision phase closed for section 1.6. Manuscript integration and verification remain pending. No manuscript text has been changed by this closure decision.

### 5.38 Section 1.6 — manuscript integration and bilingual verification — completed

The six accepted conceptual decisions recorded in sections 5.31–5.37 have been integrated independently into the Spanish and English manuscripts. The section was rewritten in each language as an original-language text; neither version was produced by translating the other.

The integrated text now covers:
- openness as relative to the selected system boundary and analytical purpose, including the organisation/facility example;
- inputs and outputs as directions across the boundary, distinguished from the nature or type of exchange;
- matter, energy, information, resources and services as exchange types that may enter or leave the system;
- the distinction between receiving an input and having the effective operating conditions to use it;
- observation time, data coverage period and conclusion horizon, alongside relative short-, medium- and long-term scales;
- response to change versus adaptation, including the possibility of insufficient, unsuccessful, unintended or unplanned adaptation; and
- operational adjustment versus transformation, based on the nature and scope of change rather than duration alone.

The snapshot/time-based explanation and the environmental examples have been retained and reconciled with the accepted temporal distinctions. The former mixed table category “outputs to the environment” / «resultados hacia el entorno» has been removed and replaced with a table that separates exchange type from direction.

**Manuscripts updated:**
- Spanish: `05_ASSETS/TRANSFORMATIONAL_VALUE/book/es/part-01-understanding-transformation/ch-01-pensar-en-sistemas.md`, version 1.2, blob SHA `c7e9dec4f643f836c040a4f8f2006398367dde6a`.
- English: `05_ASSETS/TRANSFORMATIONAL_VALUE/book/en/part-01-understanding-transformation/ch-01-thinking-in-systems.md`, version 1.1, blob SHA `3205749b77eb80262399ed157dd207a193a0a957`.

Both files were fetched again from the research branch after the updates. The persisted section headings, revised table structure, temporal distinctions and response/adaptation/transformation content were checked. The bilingual cross-review confirms equivalent conceptual scope, while preserving independently authored wording.

**Disposition:** section 1.6 integration and bilingual verification completed. The manuscripts remain `draft`; this does not approve publication or close the chapter. Other chapter-level editorial phases and unresolved section integrations remain pending.

### 5.39 Section 1.7 — broad working meaning of model — accepted

The author approved retaining and explicitly clarifying the broad use of **model** in both language versions. In this book, a model means any deliberately constructed, selective representation used to understand particular aspects of a system, answer a question or support a task.

This includes written descriptions, diagrams, tables, sets of variables and mathematical or computational models. The wording should make clear that a model need not be mathematical, computational or formally expressed.

**Rationale:** This broad working meaning supports the introductory purpose of the chapter and prevents readers from interpreting every use of “model” as referring only to formal quantitative or computational models.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.

### 5.40 Section 1.7 — scope, system boundary and level of detail — accepted

The author approved explicitly distinguishing three related but non-interchangeable aspects of a system representation in both language versions:

- **Scope of the representation:** the aspects of the system that the model is intended to cover in order to address a particular question.
- **System boundary:** what is treated as inside and outside the system of interest for the analysis.
- **Level of detail:** how finely the elements and relationships included within that scope are represented.

The explanation may note that a model can have broad scope while representing some aspects at a low level of detail, or examine a subsystem in considerable detail without covering the entire system.

**Rationale:** These distinctions prevent scope, analytical delimitation and granularity from being treated as synonyms, and help readers understand that they are separate modelling choices.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.

### 5.41 Section 1.7 — assumptions, observations and model inputs — accepted

The author approved retaining the distinction between assumptions, observed facts and quantified uncertainty, and clarifying in both language versions that **model inputs or parameters are not necessarily assumptions**. Their values may be measured, estimated, specified or assumed.

The water-network examples illustrate the distinction:
- a flow rate measured at a point may be an observed value;
- future demand may be an estimate;
- a pump's rated capacity may come from a technical specification; and
- the assumption that a pump will remain available throughout the analysis period is an assumption.

The text should avoid classifying every value entered into a model as an assumption. It should also preserve the distinction between an assumption and quantified uncertainty.

**Rationale:** The origin and epistemic status of an input value should be made explicit. A model input may be supported by observation or specification, estimated from evidence, or adopted as an assumption; these are not interchangeable categories.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.42 Section 1.7 — deliberate omissions and unknown information — accepted

The author approved clarifying in both language versions the distinction between a **deliberate omission** and **unknown or unavailable information**:

- **Deliberate omission:** an aspect that is known or recognised but intentionally excluded from the representation for reasons of scope, purpose or simplicity.
- **Unknown or unavailable information:** an aspect for which sufficient information or accessible evidence is not available to represent it adequately.

The text must not describe an unknown dependency as though it had been deliberately excluded. Nor should the absence of an element or relationship from a model be treated as evidence that the element or relationship does not exist.

Section 1.7 should briefly refer back to the distinction established in section 1.3 rather than repeat its full explanation.

**Rationale:** This preserves the epistemic distinction between a conscious modelling choice and a limitation arising from insufficient knowledge or evidence, while maintaining continuity across the chapter.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.43 Section 1.7 — evidence for model content and model adequacy — accepted

The author approved distinguishing two questions in both language versions:

1. **Evidence supporting the model's data and relationships:** for example, measurements, technical specifications, estimates grounded in evidence, or observations supporting dependencies between system elements.
2. **Evidence that the model is adequate for the question being addressed:** whether the representation captures the aspects and behaviour relevant to the intended analysis.

Reliable data do not, by themselves, demonstrate that a model is adequate. A model may use accurate measurements and still omit an important dependency or represent relevant system behaviour insufficiently.

The suitability checklist should help readers examine both questions. It must not imply that following the checklist guarantees that a model is correct or adequate.

**Rationale:** This distinguishes the evidential support for individual model contents from the adequacy of the overall representation for its intended purpose, avoiding an inference from accurate inputs to model validity.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.44 Section 1.7 — compatibility when combining complementary models — accepted

The author approved adding a concise caution in both language versions that combining complementary representations of the same system requires checking their compatibility.

Before combining, compare at least:
- the system boundaries represented;
- the assumptions adopted;
- the time horizons covered;
- the terminology used; and
- the levels of detail.

Without these checks, combining models may create an appearance of coherence between representations that describe different scopes or rely on incompatible choices.

The explanation should remain introductory and should not expand into formal methods for model integration.

**Rationale:** Complementary models can provide different but useful views of a system; their combination is meaningful only when relevant differences in scope and modelling choices are recognised and addressed.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.45 Section 1.7 — conceptual decision phase closed — accepted

The author approved closing the conceptual decision phase for section 1.7 after resolving the eight review areas recorded for the section:

1. The broad working meaning of model.
2. The distinctions among representation scope, system boundary and level of detail.
3. The status of model inputs and parameters, including assumptions, observations, estimates, specifications and quantified uncertainty.
4. Deliberate omissions versus unknown or unavailable information.
5. Evidence supporting model data and relationships versus evidence of model adequacy for the intended question.
6. Compatibility checks when combining complementary models.
7. Retention and appropriate use of the section's examples and pedagogical intent.
8. Conceptual equivalence across the independently authored Spanish and English versions.

The accepted decisions apply to both language versions. The next stage is to integrate them independently into each original-language manuscript, then verify the persisted changes and their bilingual conceptual equivalence. The introductory scope should be maintained; no unnecessary expansion into formal modelling methods is authorised by this closure.

**Disposition:** conceptual decision phase closed for section 1.7. Manuscript integration and verification remain pending. No manuscript text has been changed by this closure decision.


### 5.46 Section 1.7 — manuscript integration and bilingual verification — completed

The accepted conceptual decisions recorded in sections 5.39–5.45 have been integrated independently into the Spanish and English manuscripts. Each version was revised as an original-language text; neither was produced by translating the other.

The integrated section now:
- defines **model** broadly as a deliberately constructed, selective representation, including prose, diagrams, tables, variable sets, and mathematical or computational models;
- distinguishes representation scope, system boundary and level of detail;
- clarifies that model inputs and parameters may be measured, estimated, specified or assumed, and retains the distinction between assumptions and quantified uncertainty;
- distinguishes deliberate omissions from unknown or unavailable information, and cautions that absence from a model does not establish non-existence;
- separates evidence supporting model data and relationships from evidence that the representation is adequate for its intended question;
- clarifies that a checklist supports examination but does not guarantee correctness; and
- adds compatibility checks for boundaries, assumptions, time horizons, terminology and levels of detail when complementary models are combined.

The water-network examples and introductory pedagogical scope have been retained. The revisions do not introduce a formal taxonomy of modelling methods or model integration.

**Manuscripts updated:**
- Spanish: `05_ASSETS/TRANSFORMATIONAL_VALUE/book/es/part-01-understanding-transformation/ch-01-pensar-en-sistemas.md`, version 1.3, blob SHA `dcf83f7d79e5964ebf9d0b4170efb495028963ad`.
- English: `05_ASSETS/TRANSFORMATIONAL_VALUE/book/en/part-01-understanding-transformation/ch-01-thinking-in-systems.md`, version 1.2, blob SHA `09f532dfaf070e730ca349520ebf58f2d7fb6fb1`.

Both manuscripts were fetched again from the research branch after the updates. The version metadata and the accepted conceptual changes were checked in each persisted section. The bilingual cross-review confirms equivalent conceptual scope and examples while preserving independently authored wording.

**Disposition:** section 1.7 integration and bilingual verification completed. Both manuscripts remain `draft`; this does not approve publication or close the chapter. Other chapter-level editorial phases and unresolved section integrations remain pending.


### 5.47 Section 1.8 — local optimisation and system-level reasoning — accepted

The author approved clarifying, in both language versions, the distinction between local optimisation and system-level reasoning without implying that system-level reasoning necessarily means solving a formal mathematical global optimisation problem.

The section should establish that:
- **Local optimisation** seeks to improve one or more criteria for a component or subsystem.
- **System-level reasoning** evaluates the consequences of decisions for the relevant whole, its dependencies and its relevant environment.
- A system-level decision does not necessarily maximise all performance criteria simultaneously; criteria may conflict.
- Decisions should make explicit the relevant outcomes, mandatory requirements, constraints and acceptable trade-offs.
- The scale and breadth of analysis should be proportionate to the decision; a broader boundary is not automatically a better or more appropriate analysis.

The wording should avoid presenting system-level reasoning as synonymous with formal global optimisation.

**Rationale:** This preserves the practical systems-engineering distinction between local performance and consequences for the wider system, while avoiding an unjustified implication that a global mathematical optimum is always definable or attainable.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.48 Section 1.8 — constraints and bottlenecks — accepted

The author approved distinguishing a **constraint** from a **bottleneck** in both language versions:

- **Constraint:** a condition that limits the available alternatives, the performance or the possible outcomes of a system.
- **Bottleneck:** an element, capacity or process whose limitation significantly restricts the performance of the whole in relation to a specified outcome.

A constraint may exist without being the dominant limiting factor. A bottleneck may shift when the system is changed. The water-network example should illustrate this possibility without implying that every local improvement necessarily creates or moves a bottleneck.

**Rationale:** This prevents the terms from being treated as interchangeable and makes clear that bottleneck identification depends on the outcome being considered and the system's current configuration.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.49 Section 1.8 — requirements, performance objectives and preferences — accepted

The author approved clarifying the different status of requirements, performance objectives and preferences in both language versions:

- **Requirements:** conditions that must be met for the system or solution to be acceptable.
- **Performance objectives:** outcomes that the decision seeks to achieve or improve, allowing for different degrees of attainment.
- **Preferences:** criteria used to compare alternatives when several options meet the applicable requirements, but may involve conflicting considerations.

These criteria should not be treated as interchangeable. An alternative that fails an applicable mandatory requirement should not be presented as equivalent to one that satisfies it merely because it performs better on other indicators.

The text must also avoid implying that every requirement is absolute in every context: whether a requirement is mandatory depends on the decision framework and applicable conditions.

**Rationale:** This distinction makes trade-offs more transparent and prevents compensatory comparisons from obscuring non-negotiable conditions, while recognising that requirement status is context-dependent.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.50 Section 1.8 — direct, indirect and unintended effects — accepted

The author approved clarifying the analysis of intervention consequences in both language versions:

1. **Direct effects:** consequences occurring in the element or subsystem being changed.
2. **Indirect effects:** consequences arising elsewhere in the system through relationships, interfaces or dependencies.
3. **Unintended effects:** consequences, whether direct or indirect, that harm relevant outcomes or create risks that were not anticipated.

These categories are not mutually exclusive: an unintended effect may be either direct or indirect. The text must not imply that every consequence can be anticipated. Analysis can identify plausible effects, while subsequent observation may reveal additional consequences.

**Rationale:** This distinguishes where an effect occurs and how it relates to the intervention from whether it was intended, while recognising the limits of prediction.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.51 Section 1.8 — time horizons in intervention evaluation — accepted

The author approved clarifying in both language versions that an intervention may produce different results depending on the time horizon considered:

- **Short term:** immediate effects of the intervention and its commissioning or initial operation.
- **Medium term:** consequences emerging during operation and the adjustment or adaptation of affected parts.
- **Long term:** cumulative effects, changing needs, wear, maintenance and evolution of the environment.

These are analytical horizons, not universal fixed time intervals. Their duration depends on the system, the intervention and the decision being evaluated.

The evaluation should not present an initial improvement as sustained improvement without sufficient evidence of subsequent behaviour.

**Rationale:** This makes temporal scope explicit and prevents short-term performance from being treated as proof of durable system-level improvement.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.52 Section 1.8 — scope and proportionality of system-level reasoning — accepted

The author approved clarifying, in both language versions, that system-level reasoning does not require analysing every possible element, relationship or consequence. It requires identifying and examining those relevant to the decision, considering:

- the importance of the outcomes affected;
- the magnitude and likelihood of potential consequences;
- uncertainty in the available information;
- the reversibility of the intervention; and
- the consequences of an incorrect decision.

The depth and breadth of analysis should be proportionate to the importance and risk of the decision. The analysis should also state its boundaries and the uncertainties that remain unresolved.

This clarification should connect section 1.8 with the earlier discussion of system boundaries, representation scope and models, without turning the section into a formal risk-assessment methodology.

**Rationale:** System-level reasoning must be sufficiently broad to capture decision-relevant effects, but bounded and proportionate rather than exhaustive. Making limitations and residual uncertainty explicit helps prevent conclusions from exceeding the analysis performed.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.53 Section 1.8 — interdependencies and effects across subsystems — accepted

The author approved clarifying, in both language versions, that an improvement to one component or subsystem may change the operating conditions of other parts of the system, including parts that were not directly modified.

The section should explain that:

- local improvements may alter flows, loads, dependencies or operating conditions elsewhere in the system;
- these effects depend on the system's configuration and relationships;
- an improvement may create benefits, costs or new trade-offs in other subsystems; and
- interdependencies should not automatically be assumed to produce negative effects, since they may also create synergies.

The water-network example should be used to illustrate the point at an introductory level, without introducing quantitative methods for analysing effect propagation.

**Rationale:** This makes the consequences of system interdependence concrete while avoiding the assumption that local changes have either isolated or necessarily adverse effects.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.54 Section 1.8 — conceptual decision phase closed — accepted

The author approved closing the conceptual decision phase for section 1.8 after resolving the review areas recorded in sections 5.47–5.53:

1. Local optimisation and system-level reasoning.
2. Constraints and bottlenecks.
3. Requirements, performance objectives and preferences.
4. Direct, indirect and unintended effects.
5. Time horizons in intervention evaluation.
6. Scope, proportionality and limits of the analysis.
7. Interdependencies and effects across subsystems.
8. Conceptual equivalence across the independently authored Spanish and English versions.

The accepted decisions apply to both language versions. The next stage is to integrate them independently into each original-language manuscript, then verify the persisted changes and their bilingual conceptual equivalence.

The section should retain its introductory purpose. The accepted decisions do not authorise expansion into formal global optimisation, quantitative effect-propagation methods or a formal risk-assessment methodology.

**Disposition:** conceptual decision phase closed for section 1.8. Manuscript integration and verification remain pending. No manuscript text has been changed by this closure decision.


### 5.55 Section 1.8 — manuscript integration and bilingual verification — completed

The accepted conceptual decisions recorded in sections 5.47–5.54 have been integrated independently into the Spanish and English manuscripts. Each version was revised as an original-language text; neither was produced by translating the other.

The integrated section now covers:
- the distinction between local optimisation and system-level reasoning, without equating the latter with formal mathematical global optimisation;
- constraints and bottlenecks, including the possibility that a bottleneck may shift as the system configuration changes;
- interdependencies across subsystems, including changes to flows, loads, resource distribution and operating conditions, and the possibility of benefits, costs, trade-offs or synergies;
- requirements, performance objectives and preferences, including the context-dependent status of mandatory requirements;
- direct, indirect and unintended effects, while acknowledging that not all consequences can be anticipated;
- short-, medium- and long-term evaluation horizons, without treating them as universal fixed intervals;
- proportionality of analytical scope and depth to decision importance and risk, including uncertainty, reversibility, explicit boundaries and residual limitations; and
- a practical set of guiding questions and a revised reflection prompt.

The water-network example has been retained and expanded consistently in both languages. The section remains introductory and does not introduce formal global optimisation, quantitative effect-propagation methods or a formal risk-assessment methodology.

**Manuscripts updated:**
- Spanish: `05_ASSETS/TRANSFORMATIONAL_VALUE/book/es/part-01-understanding-transformation/ch-01-pensar-en-sistemas.md`, version 1.4, blob SHA `8023735e8e9ce65bdfc5fc9005886691148dcdf8`.
- English: `05_ASSETS/TRANSFORMATIONAL_VALUE/book/en/part-01-understanding-transformation/ch-01-thinking-in-systems.md`, version 1.3, blob SHA `55ee3476f187f31c2e92beeaadbc67cab0d67954`.

Both files were fetched again from the research branch after the updates. Their version metadata, section boundaries, principal conceptual topics and revised reflection prompts were checked. The bilingual cross-review confirms equivalent conceptual scope and pedagogical intent while preserving independently authored wording.

**Disposition:** section 1.8 integration and bilingual verification completed. Both manuscripts remain `draft`; this does not approve publication or close the chapter. Other chapter-level editorial phases remain pending.


### 5.56 Section 1.9 — integrative scope of the chapter synthesis — accepted

The author approved, for both language versions, that the chapter synthesis should not be a linear recap of the individual sections. It should integrate the relationships among the chapter's central dimensions:

- purpose, boundary and context;
- elements, states, properties and behaviours;
- actors, capabilities, resources and dependencies;
- relationships, interactions and system structure;
- openness, environment and time;
- models, scope, assumptions and omissions; and
- local optimisation and system-level reasoning.

The synthesis should help readers leave the chapter with an integrated perspective for describing and understanding a system, rather than only a list of concepts encountered.

**Rationale:** The chapter's learning outcome is the ability to connect these dimensions when forming a system description and interpreting its behaviour. The synthesis should make those connections visible without repeating the chapter section by section.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.57 Section 1.9 — purpose and structure of the integrative table — accepted

The author approved, for both language versions, retaining and revising the existing integrative table so that it functions as a practical reference rather than a simple index of concepts.

Each row should connect:
- a dimension of system analysis;
- a guiding question that supports reasoning;
- what the dimension helps the reader understand or examine; and
- its relationship with other dimensions, where relevant.

The table should support readers in constructing a description of a system. It is not an exhaustive checklist and should not be presented as a mandatory procedure.

**Rationale:** A useful synthesis table should show how analytical dimensions inform one another and help readers frame a system description, while preserving flexibility across different systems and purposes.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.58 Section 1.9 — applied exercise and bounded system description — accepted

The author approved, for both language versions, retaining the exercise in which readers choose a familiar system and prepare a brief description, while making four aspects explicit:

1. the purpose of the description and the question it is intended to answer;
2. the selected boundary, context and elements or relationships considered relevant;
3. what is known, which assumptions have been adopted, and what information is still missing or has not been examined; and
4. the limits of the description: what it helps the reader understand and which conclusions it does not support.

The exercise should not require a formal model or a comprehensive system assessment. Its purpose is to apply the chapter's principles to a proportionate system description whose scope and limitations are clear.

**Rationale:** The exercise turns the chapter's conceptual distinctions into a manageable learning activity and reinforces the need to make analytical choices and epistemic limits explicit.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.59 Section 1.9 — reflection questions and integrative reasoning — accepted

The author approved, for both language versions, retaining the five-question structure while revising the questions so that each:

- requires the reader to connect at least two dimensions of the chapter;
- presents a situation or decision that calls for reasoning rather than merely recalling definitions;
- allows different answers to be justified by the system and purpose selected; and
- avoids duplicating the preceding applied system-description exercise.

The final question should especially integrate intervention decisions, effects across subsystems, trade-offs among criteria and evaluation time horizons.

**Rationale:** Reflection questions should test whether readers can use the chapter's concepts together in context, not simply reproduce terminology or repeat the applied exercise.

**Disposition:** accepted for ES/EN. Manuscript integration remains pending; no manuscript text has been changed by this decision.


### 5.60 Section 1.9 — chapter closure and transition to Chapter 2 — accepted

The author approved, for both language versions, that the end of Chapter 1 should:

- reaffirm that understanding a system requires constructing a purpose-oriented representation with an explicit boundary and awareness of its assumptions and limitations;
- highlight that components, capabilities and relationships condition what a system can do;
- introduce transformation as change in states, behaviours, relationships or configuration, without developing the conceptual framework prematurely; and
- avoid implying that every change constitutes a transformation or that every transformation creates value.

The transition should leave the following question open:

> How can a system change, and what determines the transformations that are genuinely within its reach?

**Sequencing constraint:** Chapter 2 must not begin until the pending integration work for sections 1.1–1.3 has been completed and verified in both original-language manuscripts. The approved conceptual decisions for sections 1.4–1.9 do not waive this requirement. Chapter 1 must complete its outstanding integration and verification work before progression to Chapter 2.

**Disposition:** closure and transition criterion accepted for ES/EN. Integration into section 1.9 remains pending. Sections 1.1–1.3 integration and verification remain mandatory before Chapter 2. No manuscript text has been changed by this decision.


### 5.61 Sections 1.1–1.3 — manuscript integration and bilingual verification — completed

Following the author's explicit instruction that Chapter 2 must not begin before sections 1.1–1.3 are integrated, the accepted decisions recorded in sections 5.1–5.14 were integrated independently into both original-language manuscripts.

The integration includes:

**Section 1.1**
- An operational definition of a system as a delimitable set of related and organised elements that interact or maintain relevant dependencies, interpreted within a context and period.
- The distinction among system of interest, unit of analysis and analytical perspective.
- The distinction between system behaviour and emergent behaviour, avoiding the claim that all system behaviour is emergent.
- The declared scope covering physical, social, organisational and socio-technical systems, while treating purely conceptual systems as representations or analytical constructions unless otherwise established.
- An aligned water-network example covering source and treatment, storage and pumping, distribution connections, consumption points, variable demand, pressure, flow, operating conditions, energy and control dependencies, and possible failure propagation or service interruption.

**Section 1.2**
- Distinctions among purpose, function and objectives, and between the purpose of the analysis and the purpose attributed to the system.
- The system boundary as an analytical choice that includes relevant interfaces and may have physical, functional, operational and temporal dimensions.
- The operational editorial convention distinguishing environment from context, explicitly not presented as universal across disciplines.
- The revisability of a boundary when relevant dependencies, interfaces or effects are revealed, subject to justification.

**Section 1.3**
- Element as the general analytical term and component as a more specific term commonly used in technical and engineering contexts.
- State as a condition at a specified reference time; observations over an interval form a sequence or trajectory of states.
- The distinction between properties and variables.
- Behaviour characterised through patterns, responses or changes under specified conditions, with evidence proportionate to the phenomenon and question; a single observation is not automatically sufficient to establish a pattern.
- The distinction between unknown or unavailable information and deliberate omissions.

**Manuscripts updated and re-fetched from the research branch:**
- Spanish: `05_ASSETS/TRANSFORMATIONAL_VALUE/book/es/part-01-understanding-transformation/ch-01-pensar-en-sistemas.md`, version 1.5, blob SHA `4dadec09697e4bf038e846b6745e9e50ce81985c`.
- English: `05_ASSETS/TRANSFORMATIONAL_VALUE/book/en/part-01-understanding-transformation/ch-01-thinking-in-systems.md`, version 1.4, blob SHA `f34811bc4c0dbf69ef96d1e64f58251518c3b3d7`.

Post-update verification checked both files' metadata and section boundaries, and confirmed the principal accepted distinctions and examples in each language. A bilingual cross-review confirmed equivalent conceptual scope and pedagogical intent while preserving independently authored wording.

**Disposition:** sections 1.1–1.3 integrated and verified. Both manuscripts remain `draft`. This completion does not close Chapter 1 or authorise progression to Chapter 2 while section 1.9 integration and chapter-level editorial checks remain pending.


### 5.62 Section 1.9 — manuscript integration and bilingual verification — completed

The accepted decisions recorded in sections 5.56–5.60 have been integrated independently into the Spanish and English manuscripts. Both versions were revised as original-language texts; neither was produced by translating the other.

The revised synthesis now:
- integrates the relationships among purpose and context; composition and capabilities; organisation and interactions; boundary and environment; time and change; model and evidence; and system-level performance;
- revises the integrative table so each dimension connects a guiding question, its analytical contribution and its relationship to other dimensions;
- retains the applied exercise and makes its four required aspects explicit: purpose and question, boundary and context, knowledge and assumptions, and scope and limits;
- retains five reflection questions, each requiring contextual reasoning across multiple dimensions and avoiding duplication of the applied exercise; and
- closes the chapter by relating system configuration and capabilities to the transformations within a system's reach, without implying that every change is a transformation or that every transformation creates value.

The Spanish and English versions preserve equivalent conceptual scope and pedagogical intent while using independently authored wording. The exercise remains proportionate and does not require a formal model or comprehensive system assessment. The reflection questions include the approved integration of intervention effects across subsystems, trade-offs, uncertainty and time horizons.

**Manuscripts updated and re-fetched from the research branch:**
- Spanish: `05_ASSETS/TRANSFORMATIONAL_VALUE/book/es/part-01-understanding-transformation/ch-01-pensar-en-sistemas.md`, version 1.6, blob SHA `ba3672fa3e663f9b457fc46ea66d8550ab28f72e`.
- English: `05_ASSETS/TRANSFORMATIONAL_VALUE/book/en/part-01-understanding-transformation/ch-01-thinking-in-systems.md`, version 1.5, blob SHA `d81a5d9ea5dc20261cc063feee0c51c0979bab13`.

Post-update verification checked the current metadata, section headings and boundaries, table structure, four exercise requirements, five reflection questions, chapter closure and transition question in both files. Both manuscripts remain `draft`.

**Disposition:** section 1.9 integration and bilingual verification completed. Chapter 1 is not yet editorially closed. The remaining chapter-level editorial workflow must be completed before progression to Chapter 2.


### 5.63 Chapter 1 — initial global editorial review: structure and learning design findings

This entry records findings from the first chapter-level editorial pass against the current Content Model & Editorial Workflow, Learning Master Architecture and Detailed TOC. It is a findings record, not an approval or a set of manuscript corrections. No manuscript text has been changed in this review stage.

**Scope inspected:** both current original-language manuscripts, their section hierarchy and metadata, the chapter template and cross-cutting learning-design requirements.

**Finding 5.63.1 — chapter sequence and progression — no correction currently indicated**

The nine-section progression is coherent: system definition; purpose and analytical boundary; elements and states; actors, capabilities and resources; relationships and structure; openness and time; models and limitations; system-level reasoning; and integrated synthesis. The sequence supports the chapter purpose stated in the Detailed TOC. No reordering is proposed on the evidence of this pass.

**Finding 5.63.2 — explicit learning objectives — confirmed editorial gap**

The Detailed TOC §4.3 states that each chapter should have explicit learning objectives. The recommended chapter template also includes learning objectives. Neither the Spanish nor English manuscript currently contains an explicit learning-objectives section or an equivalent clearly identifiable set of outcomes.

The existing explanations, key ideas, exercises and reflection questions provide material from which objectives can be formulated, but they do not replace the explicit statement required by the learning-design criterion.

**Status:** finding confirmed; wording and placement of objectives not yet decided. No manuscript change authorised by this finding alone.

**Finding 5.63.3 — opening question or motivating situation — partial fulfilment / editorial option**

The chapter opens with the situation of examining an installation, service or organisation and then introduces a water-network example. This provides a concrete entry point consistent with the recommended template's motivating-situation criterion. However, the opening does not frame an explicit question for the reader.

This is not treated as a structural defect. Consider whether a concise opening question would materially improve orientation without repeating the reflection prompt at the end of §1.1.

**Status:** editorial option; decision deferred.

**Finding 5.63.4 — references and source traceability — confirmed completion gap**

Both manuscript metadata blocks currently declare `references: []`. Neither manuscript includes a references or source-notes section. The chapter presents substantive systems concepts and technical distinctions, while the Content Model §9 requires central reference records and traceability appropriate to substantive claims.

A search of the current branch did not locate the expected central `references.yml` or `terminology.yml` records. This search result is not sufficient to conclude that no equivalent registry exists elsewhere; the canonical location and relevant sources must be confirmed before adding or citing records.

**Status:** source audit required. No references are to be invented or inserted without verification.

**Finding 5.63.5 — glossary and related-content links — pending content architecture dependency**

The current metadata declares `concepts: []` and `related: []`. The chapter's closing paragraph names the transition to Chapter 2, but the manuscripts do not yet provide navigable cross-links or glossary references. The Detailed TOC template recommends related chapters and glossary links, and the Content Model defines shared terminology as a governed resource.

The expected glossary and terminology registry locations were not found by the initial branch search. Confirm whether these resources have been created or whether the links must remain deferred until their records exist.

**Status:** dependency check required; do not create placeholder links or invent glossary IDs.

**Finding 5.63.6 — chapter-level synthesis and application — satisfactory in the current draft**

Section 1.9 now includes an integrative synthesis, a table connecting dimensions and their relationships, a bounded applied exercise, and five reflection questions. These elements provide the chapter-level synthesis and application components recommended by the Detailed TOC. The existing section-level key ideas and reflection prompts in §§1.1–1.8 provide progressive reinforcement. No duplication correction is proposed at this stage.

**Finding 5.63.7 — visual assets — no automatic gap**

The chapter currently contains no diagram or image. The chapter template calls for a diagram or model only where it materially improves understanding, and the Content Model requires governance controls if a substantive reusable visual asset is created. The absence of a visual asset is therefore not, by itself, a defect. Any proposal must demonstrate learning value and follow the applicable asset review process.

**Finding 5.63.8 — draft metadata and review readiness**

Both manuscripts retain `status: draft`, empty author/reviewer arrays, and empty references/concepts/related metadata. The draft status is consistent with the current workflow. Authors, reviewers and publication metadata must be resolved at the appropriate later review and approval stages; they are not silently inferred in this pass.

**Next review sequence:** resolve the learning-objective proposal; complete the source and terminology registry audit; then continue with the remaining editorial criteria (clarity, readability, accessibility, consistency of editorial voice, examples, terminology and duplication) before routing any required subject-matter review. Cross-language review remains a distinct gate. Chapter 1 remains `draft`; Chapter 2 must not begin until the applicable Chapter 1 editorial workflow is complete.


### 5.64 Chapter 1 learning objectives — approved, integrated and verified

The author approved the five proposed learning objectives for Chapter 1. They have been added to both manuscripts immediately after the chapter title and before section 1.1.

The objectives cover the reader's ability to:
1. define and delimit a system in relation to analytical purpose, boundary, environment and context;
2. describe system composition and organisation, including elements, states, properties, behaviour, actors, capabilities, resources, dependencies and relationships;
3. interpret the operation of open systems over time, including exchanges, changing conditions, responses and trajectories;
4. construct and assess a system description suited to a question, including information sources, assumptions, omissions, uncertainty and limitations; and
5. reason about system-level interventions, including interdependencies, constraints, direct and indirect effects, trade-offs and time horizons.

The Spanish and English versions were authored independently and preserve equivalent learning outcomes.

**Manuscripts updated and re-fetched from the research branch:**
- Spanish: `05_ASSETS/TRANSFORMATIONAL_VALUE/book/es/part-01-understanding-transformation/ch-01-pensar-en-sistemas.md`, version 1.7, blob SHA `0cc38d87371e480806eeb7ade007886795dc4b0e`.
- English: `05_ASSETS/TRANSFORMATIONAL_VALUE/book/en/part-01-understanding-transformation/ch-01-thinking-in-systems.md`, version 1.6, blob SHA `4fff179e32df23cdd49e1c341dd66c28786973ef`.

Post-update verification confirmed the objective headings, all five outcomes in each language, their placement before section 1.1, and the continued `draft` status of both manuscripts.

**Disposition:** learning-objective gap resolved for the current draft. The remaining global editorial findings in §5.63 remain open or deferred according to their stated status. Chapter 1 is not yet editorially closed; do not begin Chapter 2.


### 5.65 Chapter 1 — source and reference registry audit

This audit corrects and refines the preliminary findings in §5.63.4 and §5.63.5. The initial search did not inspect the canonical Learning reference and terminology locations defined by the Content Model. The following findings supersede the corresponding preliminary search statements; the earlier review history is retained.

**5.65.1 — Central reference registry exists; current entries do not cover Chapter 1**

The canonical shared reference registry is present at `05_ASSETS/TRANSFORMATIONAL_VALUE/references/references.yml`. It currently contains six records (TV-REF-001 through TV-REF-006), primarily supporting existing TGCV applied examples, empirical analyses and source datasets. None of these six records is an appropriate general systems-thinking or systems-engineering source for Chapter 1.

The registry's existence means the statement in §5.63.4 that the expected central registry had not been located is superseded. The actual gap is narrower: Chapter 1 has no linked reference IDs and the existing registry contains no suitable Chapter 1 sources.

**Status:** registry located and inspected; Chapter 1 reference coverage gap confirmed.

**5.65.2 — Shared terminology registry exists; Chapter 1 glossary coverage remains incomplete**

The shared terminology registry is present at `05_ASSETS/TRANSFORMATIONAL_VALUE/metadata/terminology.yml`. It currently contains one draft term, `TV-TERM-001` (“espacio de transformaciones accesibles” / “accessible transformation space”), which belongs to later TGCV content and is not a Chapter 1 systems-thinking term. The glossary directory contains its orientation README but no bilingual glossary entries were found in the expected location.

The statement in §5.63.5 that the expected terminology registry had not been located is therefore superseded. The current issue is that Chapter 1's metadata declares `concepts: []`, no Chapter 1 glossary entries are registered, and the book's shared register does not yet cover the key systems concepts introduced in this chapter.

**Status:** registry and glossary location confirmed; Chapter 1 terminology coverage gap confirmed. Do not invent term IDs or duplicate definitions in the chapter.

**5.65.3 — Verified candidate references for Chapter 1**

The following three sources have been bibliographically checked against publisher or issuing-organisation records and are recommended for addition to the central registry. These are candidates for the author's approval; no new records have yet been added.

1. **Donella H. Meadows (2008), _Thinking in Systems: A Primer_.** Edited by Diana Wright. Chelsea Green Publishing. ISBN 978-1-60358-055-7. The publisher confirms the author, editor, publisher, publication date and ISBN. Relevance: introductory systems thinking, relationships, feedback and system behaviour. Candidate coverage: §§1.1, 1.5, 1.6 and selected parts of 1.9. Treat as a foundational complementary reading, not as the authority for every operational definition adopted in this book.

2. **International Council on Systems Engineering (INCOSE) (2023), _Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities_ (5th ed.), INCOSE-TP-2003-002-05.** Compiled and edited by David D. Walden, Thomas M. Shortell, Garry J. Roedler, Bernardo A. Delicado, Odile Mornas, Yip Yew-Seng and David Endler. Wiley. ISBN 978-1-119-81429-0. The issuing organisation and publisher confirm the fifth edition, publication date and bibliographic identity. The available contents identify relevant sections on system boundary and system of interest, emergence, interfacing systems, system states and modes, and systems science/systems thinking. Candidate coverage: §§1.1–1.8.

3. **National Aeronautics and Space Administration (NASA) (2016), _NASA Systems Engineering Handbook_, NASA/SP-2016-6105 Rev 2.** The official NASA PDF confirms the report identifier and revision. Relevant material includes §2.0 (Fundamentals of Systems Engineering), §4.1 (Stakeholder Expectations Definition), §6.3 (Interface Management) and §6.8 (Decision Analysis). Candidate coverage: §§1.1, 1.2, 1.4, 1.5 and 1.8.

**5.65.4 — Source-to-section mapping and limitations**

The candidate sources are complementary rather than interchangeable:
- Meadows provides an accessible systems-thinking foundation, particularly for relationships and feedback.
- INCOSE provides the closest domain-free systems-engineering reference for the chapter's system concepts, boundary, interfaces, states and system-level perspective.
- NASA provides authoritative engineering guidance on system-level results, stakeholder expectations, interfaces and trade-offs.

The proposed mapping is a guide for selective in-text attribution and further reading, not a claim that the chapter's editorial working definitions are copied from or formally prescribed by these sources. The distinctions adopted in this book (including its operational convention for environment versus context) must remain identified as editorial conventions where appropriate.

ISO/IEC/IEEE 15288:2023 was also checked. It is an active international standard establishing system life-cycle process descriptions, but it is not necessary as a core Chapter 1 reference: the chapter does not teach a life-cycle process framework. It may be more appropriate in later chapters or as optional further reading if the relevant content warrants it.

**5.65.5 — Section 1.7 requires careful source framing**

The chapter's treatment of system descriptions as selective models, and its distinctions among scope, boundary, level of detail, evidence, assumptions and omissions, should not be attributed wholesale to the three general references. These are useful editorial distinctions developed for this book. Either retain them explicitly as the book's working analytical guidance, or undertake a targeted source search if a stronger external methodological claim is introduced. No additional reference is recommended at this stage without a specific claim requiring it.

**Disposition and next decision**

The registry audit is complete. Proposed reference records are not yet approved or entered. The next step is to approve or amend the three candidate references and their intended role; after approval, create the central records with stable IDs, update both chapter metadata blocks and add selective source attribution/further-reading presentation in both original-language manuscripts. Chapter 1 remains `draft`; the source audit does not constitute subject-matter approval or editorial closure.


### 5.66 Chapter 1 references — author-approved, registered, integrated and verified

The author approved the three candidate references and their proposed complementary roles in Chapter 1. The approval has been implemented in the central bibliographic registry and both original-language manuscripts.

**Central registry records created:**
- `TV-REF-007` — Donella H. Meadows, `Thinking in Systems: A Primer` (2008), edited by Diana Wright, Chelsea Green Publishing, ISBN 978-1-60358-055-7.
- `TV-REF-008` — International Council on Systems Engineering (INCOSE), `Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities` (5th ed., 2023), compiled and edited by the named editors, INCOSE-TP-2003-002-05, ISBN 978-1-119-81429-0.
- `TV-REF-009` — Steven R. Hirshorn, Linda D. Voss and Linda K. Bromley, `NASA Systems Engineering Handbook`, NASA/SP-2016-6105 Rev 2. The report identifier carries 2016; the NASA Technical Reports Server catalogue record gives a publication date of 2017-02-17. This bibliographic date distinction is retained in the registry note.

The registry uses the stable IDs above and records publisher/issuing organisation, bibliographic identity, stable URL and relevance/limitations notes. The registry `last_updated` field is 2026-11-28.

**Manuscript integration:**
- Both metadata blocks now list `TV-REF-007`, `TV-REF-008` and `TV-REF-009` in `references`.
- Both manuscripts include a final references/further-reading section with the bibliographic entries and stable IDs.
- Selective source notes were added in sections 1.1, 1.2, 1.5 and 1.8, corresponding to the approved source-to-section mapping. Meadows and INCOSE are presented as complementary systems-thinking/systems-engineering reading; NASA is cited for system interfaces and decision analysis.
- Both language versions explicitly state that the sources do not prescribe every working definition or editorial distinction adopted in the chapter.

**Files updated and re-fetched from the research branch:**
- Registry: `05_ASSETS/TRANSFORMATIONAL_VALUE/references/references.yml`, blob SHA `63b52ecc0d12e000e52ddb116b9deda98827feb8`.
- Spanish manuscript: version 1.8, blob SHA `8b46279b103d07f8e4800e6376f7c08a48bfeb97`.
- English manuscript: version 1.7, blob SHA `79e0c0c6bf2fcc6e9efee4f3b4681e97ae48ba47`.

Post-update checks confirmed all three registry IDs, the metadata reference lists, the in-text source notes, the bibliography sections and the continued `draft` status of both manuscripts.

**Disposition:** the approved reference-integration task is complete. This does not resolve the separate terminology/glossary audit, does not constitute subject-matter approval, and does not close Chapter 1 editorially.


### 5.67 Chapter 1 — terminology and glossary audit

The current bilingual manuscripts and the shared terminology register were inspected against Content Model §§4.1 and 8 and the Detailed TOC §§3 and 4.1. This entry records the audit and a proposed shortlist for author decision. No terminology records or manuscript metadata have been changed in this stage.

**5.67.1 — Current registry state**

The shared terminology register `metadata/terminology.yml` contains only `TV-TERM-001`, a draft entry for “espacio de transformaciones accesibles” / “accessible transformation space”. It is a TGCV-specific concept intended for later material, not a Chapter 1 systems concept. It remains unchanged.

The glossary directory contains only its orientation README. No bilingual glossary entry files currently exist. The two Chapter 1 manuscripts still declare `concepts: []`.

**5.67.2 — Audit principle**

The chapter uses many ordinary systems and engineering terms. Their presence does not automatically justify a canonical glossary entry. In line with the Content Model, register only concepts that need stable bilingual equivalents, a definition reused across chapters, or an explicit distinction that readers could otherwise conflate. Do not duplicate textbook definitions for ordinary vocabulary or create entries solely to populate the glossary.

**5.67.3 — Proposed canonical glossary shortlist**

The following concepts are recommended for controlled bilingual treatment because they anchor the chapter's analytical distinctions and are likely to recur in later chapters:

| Proposed concept | Preferred Spanish | Preferred English | Reason for controlled treatment |
|---|---|---|---|
| System of interest | sistema de interés | system of interest | Distinguishes the system being examined from the unit and perspective of analysis |
| System boundary | frontera del sistema | system boundary | Core delimitation concept; not necessarily a physical or administrative perimeter |
| Environment | entorno | environment | Must preserve the chapter's operational distinction from context |
| Context | contexto | context | Must preserve the chapter's operational distinction from environment |
| Emergent behaviour | comportamiento emergente | emergent behaviour | A specific kind of system behaviour; must not be used as a synonym for all system behaviour |
| System capability | capacidad del sistema | system capability | Refers to what the system is able to do under relevant conditions; avoid conflating with a resource, an individual competence or nominal capacity |
| Dependency | dependencia | dependency | More specific than a generic relationship; denotes a condition in which one element's operation or outcome relies on another |
| Feedback loop | bucle de realimentación | feedback loop | A closed chain of influence; not merely a return arrow or any generic interaction |
| Assumption | supuesto | assumption | Must be distinguished from measured, estimated or specified input values and from uncertainty |
| Deliberate omission | omisión deliberada | deliberate omission | Must be distinguished from information that is unknown or unavailable |
| Constraint | restricción | constraint | A condition limiting alternatives or outcomes; not necessarily the dominant limiting factor |
| Bottleneck | cuello de botella | bottleneck | A limiting element, capacity or process relative to a specified system result; may shift as the system changes |
| Requirement | requisito | requirement | An acceptability condition that must be met when applicable and mandatory |
| Performance objective | objetivo de rendimiento | performance objective | A result to be achieved or improved, potentially to different degrees |
| Preference | preferencia | preference | A criterion for comparing alternatives that meet applicable requirements but involve different trade-offs |

These are proposed terms, not approved definitions. Their eventual definitions must be drafted in Spanish and English independently, preserve the chapter's working distinctions, include accepted synonyms/terms to avoid where useful, and carry a review status. The three concepts in the final cluster (requirement, performance objective and preference) should be cross-linked so the distinctions remain visible.

**5.67.4 — Terms not recommended for separate canonical entries at this stage**

The following are important chapter vocabulary but do not currently require a shared glossary record: system, element, component, state, property, behaviour, actor, resource, relationship, interaction, system structure, input, output, adaptation, transformation, model, scope, level of detail, evidence, uncertainty, local optimisation and system-level reasoning. These terms should still be used consistently and explained at first use where needed. Reconsider them only if later chapters establish a specialised definition or recurring distinction that warrants canonical control.

“Unit of analysis” / “unidad de análisis” is also not proposed as a glossary entry at this stage: it is used as a methodological phrase and is already distinguished in §1.1. Reconsider if it becomes a recurring analytical construct in later chapters.

**5.67.5 — Bilingual equivalence observations**

The chapter currently uses British English spellings and terminology (for example, “behaviour”, “optimisation” and “organisation”). The English glossary should preserve this editorial convention. The preferred equivalents above match the current manuscripts. No automatic word-for-word mapping should be applied where the concept requires a definition to preserve its scope.

**Disposition and next decision**

The audit is complete. The recommended shortlist comprises 15 controlled concepts. No IDs have been allocated and no entries have been added. The next step is author approval or amendment of the shortlist. Following approval, create bilingual definitions and stable IDs in the central terminology register, then update the `concepts` metadata in both manuscripts and create glossary pages only if the agreed publishing workflow requires them. Chapter 1 remains `draft` and is not editorially closed.


### 5.68 Chapter 1 terminology — approved shortlist registered and linked

The author approved the 15-concept shortlist in §5.67.3, including the preferred Spanish and English labels. The concepts have now been added to the shared terminology registry with stable IDs and independently drafted bilingual definitions.

**Canonical terminology records created:**

| ID | Concept | Spanish preferred term | English preferred term |
|---|---|---|---|
| TV-TERM-002 | System of interest | sistema de interés | system of interest |
| TV-TERM-003 | System boundary | frontera del sistema | system boundary |
| TV-TERM-004 | Environment | entorno | environment |
| TV-TERM-005 | Context | contexto | context |
| TV-TERM-006 | Emergent behaviour | comportamiento emergente | emergent behaviour |
| TV-TERM-007 | System capability | capacidad del sistema | system capability |
| TV-TERM-008 | Dependency | dependencia | dependency |
| TV-TERM-009 | Feedback loop | bucle de realimentación | feedback loop |
| TV-TERM-010 | Assumption | supuesto | assumption |
| TV-TERM-011 | Deliberate omission | omisión deliberada | deliberate omission |
| TV-TERM-012 | Constraint | restricción | constraint |
| TV-TERM-013 | Bottleneck | cuello de botella | bottleneck |
| TV-TERM-014 | Requirement | requisito | requirement |
| TV-TERM-015 | Performance objective | objetivo de rendimiento | performance objective |
| TV-TERM-016 | Preference | preferencia | preference |

**Definition and governance status**

- Each record contains an independently authored Spanish and English working definition, related-term links and a note preserving the distinctions established in Chapter 1.
- The definitions are marked `draft`. Author approval of the shortlist and preferred labels does not imply approval of the proposed definition wording or publication readiness.
- Environment/context are explicitly documented as the chapter's operational editorial convention, not a universal disciplinary distinction.
- Requirement, performance objective and preference are cross-linked.
- The existing `TV-TERM-001` record remains unchanged.
- No separate language-specific glossary pages have been created: the shared terminology registry is the canonical definition source, consistent with the glossary README instruction not to duplicate definitions across language folders.

**Manuscript metadata linked:**
- Spanish manuscript updated to version 1.9; `concepts` now lists `TV-TERM-002` through `TV-TERM-016`.
- English manuscript updated to version 1.8; `concepts` now lists the same stable IDs.
- The prose has not been rewritten in this operation. Existing chapter wording remains subject to the later terminology and editorial consistency review.

**Files updated and re-fetched from the research branch:**
- Shared terminology registry: `05_ASSETS/TRANSFORMATIONAL_VALUE/metadata/terminology.yml`, blob SHA `fac979d637e31c3908b4236e762dd9bf2145e52d`.
- Spanish manuscript: version 1.9, blob SHA `4cef1705a4c84c55a8b37932eacacaf3708e5d36`.
- English manuscript: version 1.8, blob SHA `b2af3616c9f70f5e75a87296df21f832912f29b1`.

**Disposition:** the approved shortlist is registered and linked from both manuscripts. The bilingual definitions remain drafts and require review before approval. The next step is to review the 15 definition pairs for conceptual precision and bilingual equivalence, then check whether the manuscript's first-use wording aligns with the preferred terms. Chapter 1 remains `draft`; this operation does not close the chapter.


### 5.69 Terminology definition review — TV-TERM-002 approved

The author approved the revised bilingual definition of `TV-TERM-002 — system_of_interest`.

**Approved Spanish definition:**

> Sistema que se selecciona como objeto de interés para un análisis o una descripción determinados. Los aspectos que se consideran parte del sistema y su delimitación se establecen en función del propósito y de la pregunta que orientan el trabajo.

**Approved English definition:**

> The system selected as the object of interest for a particular analysis or description. The aspects considered part of the system and its delimitation are established in relation to the purpose and question guiding the work.

The revised wording makes explicit that the system is the object of interest, while the aspects considered part of it and its delimitation are established for the purpose and question at hand. It preserves the distinction from the unit of analysis and analytical perspective, and links naturally to `TV-TERM-003 — system_boundary`.

The definitions were updated in the shared terminology registry and re-fetched from the research branch. The entry remains in `draft` pending completion of the full terminology review and subsequent approval of the terminology set. No manuscript prose or metadata was changed in this step.


### 5.70 Terminology definition review — TV-TERM-003 approved

The author approved the revised bilingual definition of `TV-TERM-003 — system_boundary`.

**Approved Spanish definition:**

> Delimitación que establece qué elementos, relaciones, procesos y aspectos se consideran dentro del sistema de interés y cuáles quedan fuera, en función del propósito y de la pregunta del análisis. Puede considerar interfaces y dimensiones físicas, funcionales, operativas o temporales, y revisarse cuando resulte necesario. No tiene por qué coincidir con un perímetro físico o administrativo.

**Approved English definition:**

> The delimitation that establishes which elements, relationships, processes and aspects are considered inside the system of interest and which are outside it, according to the purpose and question of the analysis. It may account for interfaces and physical, functional, operational or temporal dimensions, and may be revised when necessary. It need not coincide with a physical or administrative perimeter.

The revised wording makes the boundary explicitly dependent on the purpose and question of the analysis, covers elements, relationships, processes and aspects considered inside or outside the system of interest, recognises physical, functional, operational and temporal dimensions, and states that the boundary may be revised when necessary. It avoids implying that interfaces are necessarily internal to the system and preserves the distinction from a physical or administrative perimeter.

The definitions were updated in the shared terminology registry and re-fetched from the research branch. The entry remains in `draft` pending completion of the full terminology review and subsequent approval of the terminology set. No manuscript prose or metadata was changed in this step.


### 5.71 Terminology definition review — TV-TERM-004 approved

The author approved retaining the current bilingual definitions of `TV-TERM-004 — environment` without changes.

**Spanish definition:**

> Conjunto de elementos, sistemas y condiciones situados fuera de la frontera seleccionada que interactúan con el sistema de interés, influyen en él o reciben sus efectos.

**English definition:**

> The set of elements, systems and conditions outside the selected boundary that interact with, influence or are affected by the system of interest.

The review confirmed that the definition:
- treats the environment relative to the selected system boundary rather than as an absolute category;
- includes external elements, other systems and conditions, not only physical objects;
- covers interaction, influence and effects received from the system; and
- preserves the book's operational distinction between environment and context, without claiming that this distinction is universal across disciplines.

No change to the terminology registry was required because the approved definitions already match the current entry. No manuscript changes were made. The term remains in `draft` pending completion of the terminology review and approval of the terminology set.


### 5.72 Terminology definition review — TV-TERM-005 approved

The author approved the revised bilingual definition of `TV-TERM-005 — context`.

**Approved Spanish definition:**

> Conjunto de circunstancias, relaciones y condiciones relevantes que permiten situar y comprender el problema, propósito o situación objeto de análisis. Puede incluir actores, otros sistemas y condiciones de operación, tanto dentro como fuera de la frontera del sistema de interés.

**Approved English definition:**

> The set of relevant circumstances, relationships and conditions that provide the setting for understanding the problem, purpose or situation being analysed. It may include actors, other systems and operating conditions, both inside and outside the boundary of the system of interest.

The revision makes the interpretive function of context explicit: it situates and supports understanding of the problem, purpose or situation being analysed. It also clarifies that relevant actors, systems and operating conditions may lie either inside or outside the system-of-interest boundary. This preserves the chapter's operational distinction between context and environment without treating context as a synonym for the system's physical surroundings.

The approved definitions were updated in the shared terminology registry and re-fetched from the research branch. The entry remains in `draft` pending completion of the terminology review and approval of the terminology set. No manuscript changes were made in this step.


### 5.73 Terminology definition review — TV-TERM-006 approved

The author approved the revised bilingual definition of `TV-TERM-006 — emergent_behaviour`.

**Approved Spanish definition:**

> Comportamiento o patrón del sistema que surge de las interacciones entre sus elementos y de la forma en que están organizados, y que no puede explicarse adecuadamente considerando esos elementos de manera aislada. Aunque puede resultar difícil de anticipar a partir de las características de cada elemento, no es necesariamente imprevisible ni inexplicable.

**Approved English definition:**

> System behaviour or a pattern that arises from interactions among its elements and the way they are organised, and that cannot be adequately explained by considering those elements in isolation. Although it may be difficult to anticipate from the characteristics of individual elements, it is not necessarily unpredictable or inexplicable.

The revision emphasises that emergence concerns behaviour or patterns arising from interactions among system elements and their organisation, rather than system behaviour in general. It also distinguishes limited explanatory power of isolated element-level descriptions from absolute unpredictability or inexplicability. The term's note that not all system behaviour is emergent remains applicable.

The approved definitions were updated in the shared terminology registry and re-fetched from the research branch. The entry remains in `draft` pending completion of the terminology review and approval of the terminology set. No manuscript changes were made in this step.


### 5.74 Terminology definition review — TV-TERM-007 approved

The author approved the revised bilingual definition of `TV-TERM-007 — system_capability`.

**Approved Spanish definition:**

> Aptitud del sistema, considerado como conjunto, para realizar una acción o alcanzar un resultado bajo determinadas condiciones. Esta capacidad depende de la combinación y coordinación de sus recursos, competencias, relaciones y condiciones operativas. Que exista una capacidad no implica que esté siempre disponible o pueda ejercerse efectivamente en cualquier situación.

**Approved English definition:**

> The ability of the system, considered as a whole, to perform an action or achieve an outcome under specified conditions. This capability depends on the combination and coordination of its resources, competencies, relationships and operating conditions. The existence of a capability does not mean that it is always available or can be exercised effectively in every situation.

The revision defines capability at system level and makes clear that its existence does not imply continuous availability or effective exercise under every situation. It retains the role of resources, competencies, relationships and operating conditions, while preserving the distinction from individual competence and a component's nominal technical capacity.

The approved definitions were updated in the shared terminology registry and re-fetched from the research branch. The entry remains in `draft` pending completion of the terminology review and approval of the terminology set. No manuscript changes were made in this step.


### 5.75 Terminology definition review — TV-TERM-008 approved

The author approved the revised bilingual definition of `TV-TERM-008 — dependency`.

**Approved Spanish definition:**

> Relación en la que el funcionamiento, la disponibilidad o la capacidad de un elemento, proceso o sistema para alcanzar un resultado está condicionada por una condición, recurso, capacidad o contribución de otro elemento, proceso o sistema. La dependencia puede ser total o parcial, crítica o sustituible, y no implica necesariamente una relación recíproca.

**Approved English definition:**

> A relationship in which the operation, availability or ability of an element, process or system to achieve an outcome is conditioned by a condition, resource, capability or contribution from another element, process or system. The dependency may be total or partial, critical or substitutable, and does not necessarily imply a reciprocal relationship.

The revision makes dependency more specific than a generic relationship: it conditions operation, availability or the ability to achieve an outcome. It recognises dependencies that are total or partial, critical or substitutable, and potentially asymmetric rather than necessarily reciprocal. The distinction from a constraint is preserved: a dependency describes a conditioning relationship, whereas a constraint limits available alternatives or achievable performance or outcomes.

The approved bilingual definitions were updated in the shared terminology registry and re-fetched from the research branch. The entry remains in `draft` pending completion of the terminology review and approval of the terminology set. No manuscript prose or metadata was changed in this step.


### 5.76 Terminology definition review — TV-TERM-009 approved

The author approved the revised bilingual definition of `TV-TERM-009 — feedback loop`.

**Approved Spanish definition:**

> Estructura de relaciones causales cerrada en la que los efectos de un proceso, directa o indirectamente, vuelven a influir en las condiciones o procesos que contribuyeron a generarlos, afectando así al comportamiento posterior del sistema. Los bucles de realimentación pueden ser reforzadores, cuando amplifican una tendencia o cambio, o compensadores, cuando contrarrestan una desviación o contribuyen a regular una variable. Estas denominaciones describen el comportamiento del bucle, no su carácter beneficioso o perjudicial.

**Approved English definition:**

> A closed structure of causal relationships in which the effects of a process, directly or indirectly, feed back to influence the conditions or processes that contributed to generating them, thereby affecting the subsequent behaviour of the system. Feedback loops may be reinforcing, when they amplify a trend or change, or balancing, when they counteract a deviation or contribute to regulating a variable. These terms describe the behaviour of the loop, not whether it is beneficial or harmful.

The definition distinguishes a feedback loop from a one-way causal sequence by requiring effects to feed back into conditions or processes that contributed to generating them. It identifies reinforcing and balancing loops without assigning positive or negative value judgements. The entry remains in `draft` pending completion of the terminology review and approval of the terminology set. No manuscript prose or metadata was changed in this step.
