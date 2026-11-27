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
| 1.3 | Elementos, estados, propiedades y comportamientos / Elements, States, Properties and Behaviours | reviewed — decisions pending |
| 1.4 | Actores, capacidades, recursos y dependencias / Actors, Capabilities, Resources and Dependencies | reviewed — decisions pending |
| 1.5 | Relaciones, interacciones y estructura del sistema / Relationships, Interactions and System Structure | reviewed — decisions pending |
| 1.6 | Sistemas abiertos, entornos cambiantes y tiempo / Open Systems, Changing Environments and Time | reviewed — decisions pending |
| 1.7 | Las descripciones de sistemas son modelos: alcance, supuestos y omisiones / System Descriptions Are Models: Scope, Assumptions and Omissions | reviewed — decisions pending |
| 1.8 | De la optimización de componentes al razonamiento a escala de sistema / From Component Optimisation to System-Level Reasoning | reviewed — decisions pending |
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

**Review status:** reviewed; decisions pending  
**Manuscript changes:** none

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

