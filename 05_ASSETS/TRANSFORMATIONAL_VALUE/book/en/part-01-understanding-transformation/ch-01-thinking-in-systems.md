---
content_id: TV-CH-01
language_pair_id: TV-CH-01
title: "Thinking in Systems"
language: en
content_type: chapter
status: draft
version: 1.6
created: 2026-11-27
updated: 2026-11-28
authors: []
reviewers: []
summary: "Introduces the foundations for understanding and describing systems as organised configurations of elements and relationships."
part: TV-P1
chapter: TV-CH-01
parent_id: TV-P1-OV
tags:
  - systems-thinking
  - systems-engineering
concepts: []
prerequisites: []
related: []
references: []
epistemic_status:
  - established_external_knowledge
source_assets:
  - 05_ASSETS/TRANSFORMATIONAL_VALUE/TRANSFORMATIONAL_VALUE_DETAILED_TOC_v0.1.md
  - 05_ASSETS/TRANSFORMATIONAL_VALUE/TRANSFORMATIONAL_VALUE_LEARNING_MASTER_ARCH_v0.1.md
license: null
---

# Thinking in Systems

## Learning objectives

By the end of this chapter, you should be able to:

1. **Define and delimit a system** in relation to the purpose of the analysis, its boundary, environment and context.
2. **Describe the composition and organisation of a system**, identifying its elements, states, properties, behaviours, actors, capabilities, resources, dependencies and relationships.
3. **Interpret how open systems operate over time**, considering exchanges, changing conditions, responses and trajectories.
4. **Construct and assess a system description** suited to a particular question, identifying its information sources, assumptions, omissions and uncertainties, and recognising its limitations.
5. **Reason about interventions at the system level**, considering interdependencies, constraints, direct and indirect effects, trade-offs among criteria and time horizons.


## 1.1. What Do We Mean by a System?

### Looking beyond the components

When we examine an installation, a service or an organisation, we may begin by listing its constituent parts. That inventory is useful, but it does not yet explain how the whole works. To understand the system, we also need to examine how its parts are organised, what relationships they maintain and the conditions under which they operate.

Consider a water supply network. We can identify the water source, treatment facilities, reservoirs, pumping stations, pipes, valves and consumption points. Yet listing these elements does not explain how water reaches each area, how the network responds when demand changes or how a failure may cause interruptions elsewhere. To answer these questions, we need to consider the network configuration, its connections, operating conditions, and its energy and control dependencies.

A system is therefore more than a collection of elements located in the same place. We recognise it as an organised whole because its elements maintain relevant relationships or dependencies and, through their interactions or mutual constraints, contribute to the behaviour we want to understand.

### A working definition

For the purposes of this book, we will use the following definition:

> A system is a delimitable set of related and organised elements that interact or maintain relevant dependencies, and whose behaviour can be understood by considering both its elements and the relationships between them, within a given context and over a given period.

This is an introductory working definition, not a universal definition that applies without qualification across all disciplines. It directs attention to four aspects:

- **Elements:** the parts, entities or components we distinguish as relevant to the system of interest.
- **Organisation:** the configuration through which those elements are arranged and coordinated.
- **Relationships and dependencies:** the connections and interactions that link elements or condition what they can do.
- **Behaviour:** what the system does, how it responds or how it evolves under specified conditions.

Not every element needs to interact directly, and a system does not necessarily have an explicit purpose. Nor is all system behaviour necessarily emergent.

### System of interest and analytical perspective

It is useful to distinguish the **system of interest** from the **unit of analysis** and the **analytical perspective**.

The system of interest is the particular system we want to understand. The unit of analysis identifies what observations or analyses are performed on: it may be the whole system, a subsystem, an actor or an interaction. The analytical perspective is the approach from which we examine it, such as a functional, operational, organisational or temporal perspective.

For example, we may take a water network as the system of interest while focusing an investigation on one pumping station as the unit of analysis. We may also examine the same network from hydraulic, energy, organisational or service-continuity perspectives. These choices do not necessarily change the system of interest, but they determine which aspects we observe and which conclusions we can support.

### System behaviour and emergent behaviour

**System behaviour** includes the patterns of operation, responses or changes that we can observe or infer. **Emergent behaviour** is more specific: it arises from the interactions and organisation of the whole and cannot be adequately explained by examining each element in isolation.

For example, a pressure variation in a pipe may be explained largely by local conditions. By contrast, a network's ability to maintain supply across different areas during a rise in demand may depend on interactions among reservoirs, pumps, connections, controls and consumption patterns. We should not describe every system behaviour as emergent. The term is useful when the organisation and interactions of the whole are essential to explaining the phenomenon.

### The scope of the system concept

This book focuses primarily on physical, social, organisational and socio-technical systems. Some aspects of their behaviour may not be directly observable and can nevertheless be studied through relevant evidence, such as records, measurements, decisions or activity patterns.

We may also use conceptual systems as representations or analytical constructions. However, we will not automatically equate them with systems operating in the world. The kind of reality to which we refer, and the evidence through which it can be studied, should be clear from the context.

### Why the whole matters

Component properties remain important, but their contribution depends on the configuration in which they operate. In a water network, the rated capacity of a pump or the diameter of a pipe is not enough to determine the service received in each area. Network topology, the location and timing of demand, pressure and flow conditions, operating rules, and energy and control dependencies also matter.

An initial system description should answer at least three questions:

1. Which elements belong to the system of interest?
2. How are they organised and related?
3. What behaviour do they exhibit under the conditions we want to understand?

The first question helps us build an inventory. The other two allow us to begin explaining how the whole operates.

### Key idea

Understanding a system requires examining its elements, their organisation and the relevant relationships or dependencies among them. The behaviour of the whole cannot always be explained by studying each part separately.

### Reflection

Think of an installation, service or organisation you know. What would you consider the system of interest? Could you study it using different units of analysis or analytical perspectives? Which behaviours can be explained by the characteristics of particular elements, and which depend on the organisation and interactions of the whole?

## 1.2. Purpose, Boundary, Environment and Context

### Deciding which system we want to understand

Before analysing a system, we need to establish what we want to understand and what we will treat as part of the object of study. The physical limits of a machine or building may seem obvious, but the boundary of a system of interest does not always coincide with the perimeter of an installation, an organisation or a contract. It depends on the question guiding the analysis.

In a water supply network, a study of hydraulic behaviour may focus on reservoirs, pumping stations, pipes, valves and connections. If we want to understand service continuity, maintenance teams, response procedures and control systems may also be relevant. If we are investigating how demand affects availability, consumption points and usage patterns need to be considered.

These are different ways of delimiting the same system of interest, selected to answer different questions.

### Purpose, function and objectives

The **purpose of the analysis** states what we want to understand, explain or assess. It guides the selection of the system of interest, its boundary, the required level of detail and the information we need.

It should not be confused with the **purpose of the system**, meaning the declared or attributed reason for its existence. Nor should purpose, function and objectives be used interchangeably:

- **Purpose:** the declared or attributed reason for the system's existence.
- **Function:** an activity or contribution performed by the system.
- **Objectives:** intended outcomes, which may be multiple and may conflict.

An organisation managing a water network may declare reliable supply as its purpose. Its functions include collecting, treating, storing and distributing water. Its objectives may include service continuity, quality, energy efficiency and cost control. These objectives may reinforce one another or require trade-offs.

The purpose of the analysis is different: we may study the network to understand its energy consumption, even though its main function is water distribution. Keeping these notions separate prevents us from attributing an intention to a system that may not have one, or confusing the analyst's question with the outcomes the system is expected to produce.

### The boundary and its interfaces

The **system boundary** establishes which elements and relationships are treated as inside or outside the system of interest. It is an analytical decision that needs justification, not necessarily a physical or administrative limit.

The boundary should also help identify relevant **interfaces**: points at which the system connects or exchanges something with other elements or systems. For a pumping station, relevant interfaces may include its connection to the electricity supply, control systems, infrastructure providing incoming water and the pipes that carry water away.

A boundary may have physical, functional, operational and temporal dimensions. An installation may be physically bounded while its operation depends on external services, operating rules or processes beyond that perimeter.

A boundary that is too broad may make an analysis unwieldy; one that is too narrow may exclude dependencies or interfaces needed to explain the behaviour. We should therefore select a boundary appropriate to the question, make relevant exclusions explicit and justify the chosen level of detail.

The boundary need not be definitive. It may be revised if analysis or evidence reveals relevant dependencies, interfaces or effects that were initially excluded. Such a revision should be justified by its relevance to the problem, rather than becoming an arbitrary expansion of the system of interest.

### The environment: relevant external elements and conditions

In this book, **environment** refers to the elements, systems and conditions outside the boundary that interact with the system of interest or may be affected by it.

For a water network, the environment may include the availability of water at source, weather conditions, electricity supply, applicable regulations and changes in demand. These factors may remain outside the selected boundary while still having a significant influence on the network's operation.

A boundary does not imply isolation. Part of the analysis is precisely to identify the exchanges, influences and interfaces that cross it: matter, energy, information, resources, services, demand, constraints or effects.

### Context: the circumstances from which we interpret the system

We use **context** to refer to the set of circumstances, relationships and conditions from which the problem and system of interest are defined and interpreted. It may include technical, economic, social, institutional, environmental, historical and temporal aspects.

Environment and context are related, but they serve different purposes in this editorial convention. The environment identifies external elements, systems and conditions that interact with the system or may be affected by it. Context situates the question and helps us interpret which aspects are relevant and why.

For example, the availability of water at a source may be an environmental condition. A prolonged drought, a seasonal rise in demand and particular regulatory restrictions form contextual circumstances that matter when interpreting the network's response.

This distinction is a working convention adopted in this book to support analysis; it is not intended as a universal separation used in the same way across all disciplines.

### These decisions shape what we can conclude

Purpose, boundary, environment and context are connected. The purpose of the analysis guides the boundary; the boundary distinguishes the system of interest from external elements and conditions; and context helps us interpret the problem and the conditions under which behaviour is observed.

These decisions affect the evidence we collect, the relationships we examine and the scope of our conclusions. Two analyses may reach different results because they have delimited different systems of interest or answered different questions. To interpret their conclusions, we need to understand those choices.

A sound system description should state:

- which system of interest is being studied and the purpose of the analysis;
- which elements and relationships are included within the boundary;
- which external interfaces and exchanges are relevant;
- which external elements, systems and conditions are considered part of the environment;
- which circumstances form the interpretive context; and
- which exclusions may limit the analysis or its conclusions.

There is no single boundary that is correct for every question. There is a boundary that is more or less appropriate and defensible for a particular analytical purpose, and it may be revised if relevant reasons emerge.

### Key idea

Understanding a system depends on how we define the purpose of the analysis, select its boundary and interfaces, and distinguish the environment from the context. These choices must be explicit because they shape the evidence and conclusions.

### Reflection

Choose a service or installation you know and formulate a specific question about its operation. What system of interest would you delimit to answer it? Which interfaces and dependencies would you include in the description? Which factors belong to the environment, and which circumstances form part of the context? What evidence might lead you to revise the initial boundary?

## 1.3. Elements, States, Properties and Behaviours

### Describing what makes up a system and how it works

Once the system of interest has been defined, we need to describe its constituent elements and the characteristics relevant to the question we want to answer. Elements do not all have the same nature, and we do not need to represent them at the same level of detail. The description should be selective and consistent with the purpose of the analysis.

A water supply network may include reservoirs, pumps, pipes, valves, sensors, control equipment and consumption points. It also depends on procedures, operating rules and information used to make decisions. In socio-technical systems, people, teams and organisations should be included when their actions, decisions or responsibilities influence the behaviour being studied.

The aim is not to produce an exhaustive inventory of everything that exists, but to identify the parts needed to understand the relevant aspects of the system.

### Elements and components

We use **element** as the general term for any relevant part or entity distinguished when analysing a system. Depending on the system and level of analysis, an element may be a person, group, organisation, process, resource, item of information, subsystem or physical part.

The term **component** may be used more specifically, particularly in technical and engineering systems, to refer to a constituent part of the system. This distinction is flexible rather than a rigid taxonomy: where the disciplinary context does not require a distinction, the terms may have closely related meanings. In this chapter, element is the general term.

The choice of decomposition level matters. A pumping station may be treated as a single element when examining the overall operation of the network. If we are analysing its energy consumption or reliability, we may need to distinguish motors, pumps, sensors, power supply and control equipment. A useful description provides enough detail to answer the question without hiding relevant relationships beneath an excessively granular inventory.

### States: the condition at a reference time

A **state** describes the condition of a system or one of its elements at a specified reference time, using the variables relevant to the analysis.

In a water network, the state of a reservoir may be described by its level; the state of a pump by its operating condition and regime; and the state of a network section by pressure and flow. To describe the state of the network as a whole, we select variables that represent the aspects of its configuration and operation relevant to the question.

A state is a selective representation, not a complete account of everything that exists. We should therefore state which variables are used, how they are observed or estimated and the time to which they refer.

When observations are collected over an interval, they form a sequence or trajectory of states. This sequence allows us to examine the system's evolution and study its behaviour. The observation interval should not be confused with a single state.

### Properties and variables

A **property** is a characteristic attributed to an element or system. A **variable** is a quantity or representation used to describe or track a relevant characteristic or condition.

For example, the diameter of a pipe or the rated capacity of a pump are properties of the equipment. The flow delivered at a particular time is a variable that helps describe an operating condition. Rated capacity characterises the pump under specified conditions; it is not the same as the flow it is delivering at that moment.

Not every property needs to be represented by a variable. In turn, a variable may be used to observe how a property or condition changes over time. The choice depends on the question, the availability of information and the quality of the evidence. If a variable is estimated rather than measured directly, that should be made clear when it affects interpretation.

### Behaviours: patterns, responses and changes

**Behaviour** describes patterns of operation, responses or changes in a system or its elements under specified conditions. It is characterised through observations or inferences about how states and variables evolve.

In a water network, we may examine how pressure changes when demand rises, how the control system responds when a reservoir level falls or how service is restored after a failure. A single pressure reading may describe a state, but it is not normally sufficient on its own to establish a pattern of behaviour. Repeated observations or other evidence appropriate to the phenomenon and question are generally needed.

This is not an absolute rule: the type and amount of evidence depend on what we want to understand. The important point is not to present a single observation as if it demonstrated a stable pattern.

### Connecting elements, properties, states and behaviours

These dimensions become meaningful when considered together. We identify relevant elements, describe some of their properties, use variables to represent conditions and states, and examine patterns of operation over time.

Suppose water consumption increases in one area. We may observe changes in flow and pressure, identify which pumps and valves are operating and examine the response of the control system. To explain what happens, we need to relate the observed variables to the elements, connections and operating conditions of the network.

The same observation may have different explanations if the configuration changes or if information about relevant elements is missing. Describing a system is therefore not a matter of collecting isolated values, but of organising them so that its operation can be interpreted.

### Available information and deliberate omissions

A sound description does not need to include every possible property, but it should distinguish between two different situations:

- **Unknown or unavailable information:** we do not have sufficient information or accessible evidence about an aspect of the system.
- **Deliberate omissions:** we know or recognise an aspect but intentionally exclude it because of the purpose, scope or level of detail of the description.

The absence of an aspect from a description does not demonstrate that it does not exist. Nor should an unknown dependency be presented as if it had been deliberately excluded. When these limitations may affect interpretation or conclusions, they should be documented and their relevance explained.

### Choosing what to describe

When preparing an initial description, we can ask:

- Which elements or subsystems need to be distinguished?
- What level of detail is appropriate for the question?
- Which properties characterise those elements?
- Which variables represent the relevant states?
- What observations or evidence are needed to examine their behaviour?
- What information is unavailable, and which aspects have we chosen to omit?

These questions help build a coherent representation and prevent the information available from being mistaken for a complete description of the system.

### Key idea

To describe a system, we identify relevant elements, attribute properties, use variables to represent states and examine patterns of behaviour. We must also distinguish information that is missing from aspects we have deliberately chosen to omit.

### Reflection

Think of an installation or service you know. Choose one of its elements and distinguish a property of the equipment from a variable that can be used to observe its condition. What state could you describe at a particular time? What observations would you need to characterise its behaviour? What information might be missing, and which aspects might you deliberately omit because of the purpose of your analysis?

## 1.4. Actors, Capabilities, Resources and Dependencies

### Who takes part, and what makes their contribution possible?

So far, we have described a system in terms of its elements, states and behaviours. In many real-world systems—particularly those combining technology, people and organisations—we also need to understand who takes part, what they can do, which means they can draw on and what other contributions their activities rely on.

A water supply network illustrates this well. Its operation requires infrastructure and equipment, but it also relies on operators who monitor the installation, maintenance personnel who respond to incidents, decision-makers who authorise action, and organisations that provide energy, materials or specialist services. The physical infrastructure alone cannot explain how the service is sustained.

### Actors: people, groups and organisations involved

In this chapter, **actor** is used in a socio-organisational sense: a person, group or organisation that participates in the system or has a relevant influence on how it operates. Actors may have operational, technical, decision-making, regulatory, supplier or user roles, among others.

In a water network, operators monitor alarms and adjust settings; maintenance personnel inspect and repair equipment; managers set priorities and authorise interventions; suppliers provide equipment and spare parts; and users generate demand patterns and may report incidents.

An actor may be located inside or outside the boundary of the system of interest. Whether that actor belongs in the system description depends on the relevance of their interaction, influence or dependency in relation to the problem being analysed—not simply on their physical or organisational location. Being outside the boundary does not automatically make an actor part of the environment in every model: that classification depends on how the system has been bounded and on the purpose of the analysis.

Autonomous systems, software agents and other non-human elements may also form part of the system, perform functions and produce effects, but they are not automatically classified as actors under the convention used here. If **agent** is used in a broader technical sense, that meaning should be made explicit.

### Capabilities: what an element can do and what the system can achieve

A **capability** is the ability or possibility to perform an activity or fulfil a function under specified conditions. It may belong to an individual actor, a component or the organised system as a whole.

Three related ideas should be distinguished. **Competence** refers to the knowledge and skills a person or organisation has to perform an activity. **Capability** also takes into account the means and conditions required to perform it. **Effective availability** indicates whether that capability can actually be exercised at a particular time and in a particular context, considering factors such as authority, access, resources, workload and operational state.

For example, a technician may have the knowledge and skills needed to repair a pump but lack authorisation or the required tools. The technician has the competence, but does not have the conditions needed to exercise that capability effectively at that time.

We should also distinguish the capability of an individual element from the **capability of the system**. An operator may interpret signals, a pump may move water and a control system may regulate its operation. Yet maintaining service continuity may require these contributions to be combined and coordinated through suitable procedures, interfaces, resources and operating conditions. System-level capability is not simply the sum of individual capabilities: it depends on how the elements are integrated and coordinated.

### Resources: the means that can be mobilised

**Resources** are means that can be used to perform activities and sustain system operation. They may include material, energy, financial, informational and time-related resources, among others.

In a water network, physical resources include pumps, tools, spare parts and facilities; energy resources include the electricity supply; and information resources include network plans, operating records, measurements and technical documentation. People are actors in the system, not interchangeable resources. However, they may contribute means needed for an activity through their time, knowledge, experience, skills or availability. The description should identify these specific contributions without confusing them with people's role as actors.

The existence of a resource does not guarantee that it is available for every purpose. It may already be committed to another activity, out of service, inaccessible when needed or subject to authorisation. A description should therefore distinguish between resources that exist, those that are available and those that can actually be mobilised for a particular task.

Resources should not be confused with capabilities. Diagnostic equipment is a resource; knowing how to use it and interpret its results forms part of the competence and capability required to perform the activity. A task may require both.

### Dependencies and constraints: what is required and what limits action

A **dependency** exists when the functioning, availability or outcome of an activity, actor or component requires a contribution, service, state or condition provided by another element.

For example, a repair may depend on spare parts being available, maintenance personnel having access to the site, and the possibility of temporarily interrupting supply. The operation of a pumping station may depend on electricity, water availability and the functioning of its control systems.

A dependency is not the same as a generic relationship. Two elements may be related without one requiring the other in order to function or achieve an outcome. Dependencies may also be conditional, substitutable, reciprocal or time-sensitive, and they do not all have the same degree of criticality.

A **constraint** should also be distinguished from a dependency. A dependency identifies a contribution or condition that is required; a constraint sets a limit or condition that reduces the options or ways in which an activity can be performed. Both may coexist: a pumping station may depend on the electricity supply while also being subject to consumption limits, regulatory requirements or safety conditions.

### Bringing the dimensions together

Actors, capabilities, resources and dependencies describe complementary dimensions of how an activity is sustained within a system. It is not enough for each element to exist separately: the necessary contributions must be available and coordinated under suitable conditions.

Imagine a failure in a main water pipe. Detecting it may require sensors and monitoring systems; interpreting it requires people with technical knowledge; planning the intervention requires decision-makers with the authority to act; and carrying out the repair requires tools, spare parts, access and time. The response depends on the required competence and capability being effectively available, resources being mobilisable and dependencies being satisfied.

To understand the system's operational capability, we need to ask which activities it can perform, which actors take part, which individual and collective capabilities are required, what resources are available, which contributions or conditions are needed, and which constraints shape the response.

### Including these dimensions in a system description

When analysing a system involving people or organisations, it may be useful to record:

- which actors are involved, where they are located in relation to the boundary and what roles they perform;
- which competences and capabilities matter to the activities under study;
- whether those capabilities are effectively available under the operating conditions being considered;
- which resources the activities require, which exist and which can be mobilised;
- which contributions, services or conditions the activities depend on;
- which constraints, responsibilities or authorisations shape their involvement.

This does not mean producing an organisation chart or exhaustive resource inventory by default. It means including the information needed to explain how activities are carried out and where critical limitations or dependencies may arise.

### Key idea

A system's operation may depend on the actors involved, the competences and capabilities they can bring to bear, the resources available and the dependencies and constraints that shape their actions. System-level capability arises from integrating and coordinating these contributions, not merely adding them together.

### Reflection

Think of a service or installation you know. Choose an activity that is important to its operation and identify who needs to take part, which competences and capabilities are required, what resources can be mobilised and which contributions or conditions the activity depends on. What constraints could prevent the activity from being carried out even if the actors and necessary elements existed separately?


## 1.5. Relationships, Interactions and System Structure

### A system is more than a collection of elements

Identifying a system's elements is necessary, but it is not enough to understand how the system operates. We also need to describe how those elements are related, what they exchange and how those relationships shape the behaviour of the whole.

In a water supply network, reservoirs, treatment facilities, pumps, pipes and points of use do not operate in isolation. Water flows between them; sensors transmit information; control systems adjust equipment; and maintenance activities affect infrastructure availability. The system is defined not only by its components, but also by the configuration of the relationships that connect and coordinate them.

The **structure of a system** is the configuration of the relevant relationships among its elements. It is not limited to physical layout: it also includes functional connections, information flows, dependencies and coordination mechanisms. Structure may be relatively stable, but it is not necessarily fixed or immutable.

### Relationships and interactions

A **relationship** is a relevant link between two or more elements. It may represent a physical connection, a dependency, an authority relationship, an exchange of information or another association needed to describe the system.

An **interaction** is an action, exchange or influence occurring between related elements. It may be unidirectional, reciprocal or asymmetric; it does not require influence to be exerted equally in both directions.

In a water network, a pipe physically connects two parts of the infrastructure and allows water to flow. A sensor transmits a reading to a monitoring system; a control system sends a command to a pump; and a manager's decision may change a team's activity. These are examples of interactions whose direction and nature depend on the relationship being considered.

Not every relationship involves continuous interaction. A dependency may exist even if it becomes active only under particular circumstances. Conversely, a one-off interaction does not necessarily produce a lasting change in the system's structure.

### Flows, connections and coordination mechanisms

Relationships take different forms. Common examples include:

- **Physical flows:** the movement of water, materials, energy or products between elements.
- **Information flows:** the transmission of measurements, commands, alerts and records.
- **Functional connections:** links between components that work together to perform a function.
- **Dependencies:** structural relationships in which one element requires a contribution or condition from another. The operational meaning of dependency was established in section 1.4.
- **Coordination and authority relationships:** the allocation of responsibilities, permissions and decisions among actors.

These forms are analytical perspectives, not mutually exclusive categories. A single relationship may combine, for example, a functional connection, a physical flow and a dependency. An authority relationship may also involve information exchanges. What matters is identifying the meaning each link has in the particular representation.

To avoid ambiguity, a model should make clear what each connection represents. A line may indicate a physical flow, information transfer, dependency or influence; without an explanation, readers may assign it a meaning that was never intended.

### Structure and interactions shape behaviour

Structure describes the configuration of relevant relationships; interactions describe the actions, exchanges and influences occurring through them. The two are connected: interactions may reproduce existing relationships or, in some circumstances, change them. System structure can therefore shape behaviour and may also change as a consequence of how the system operates.

Imagine that a main pipe is taken out of service. The effect is not confined to the failed section: flow distribution may change, pressure may fall in some areas, and pumping adjustments or valve operations may become necessary. The scale and extent of these effects depend on the network structure, alternative connections and operating conditions.

A local change may also improve the performance of one component while making the overall system perform worse. Increasing the output of a pumping station, for instance, may raise energy consumption or exceed pressure limits elsewhere in the network. Understanding such consequences requires us to examine relevant relationships rather than focusing only on the component being changed.

### Feedback loops

A **feedback loop** exists when a closed chain of influences causes an outcome of the system to affect its subsequent operation or regulation.

In a water network, a sensor may detect a pressure drop; the control system interprets the signal and adjusts a pump; the change in pumping affects pressure, which is measured again. Information about the result thus influences a subsequent decision or action and closes the chain of influences.

A return arrow pointing to an earlier element in a diagram is not, by itself, enough to identify feedback: there must be a chain of influences that closes the loop. Feedback may have stabilising or amplifying effects; it does not necessarily correct or reduce variation. Its effect depends on the relationships, delays, control rules and operating conditions involved.

### Measuring and representing structure without losing meaning

Measurements help us observe how a system operates, but an isolated reading is not equivalent to the system's complete state. A measurement provides information about a particular variable or condition. Combined with other measurements, observations and knowledge of system operation, it can be used to monitor or infer the network's operating conditions. By itself, it does not represent every relevant dimension of the system's state.

A diagram can help reveal connections and distinguish types of relationships, but every representation selects part of reality. An infrastructure schematic may emphasise physical flows and omit responsibilities; a control diagram may show signals and commands without representing water distribution; an organisational chart may show authority and coordination but not technical constraints.

A diagram should therefore be read in relation to its purpose, scope and legend. It is important to state what the nodes and connections represent, which relationships have been omitted, and whether arrows indicate flow direction, information transfer or influence.

The supporting diagram in this section uses a simplified water supply network to distinguish physical flows, information and control signals, and selected external dependencies. It is not an engineering drawing and does not attempt to represent every possible relationship in a real installation.

### Key idea

A system's structure is the configuration of relevant relationships among its elements; interactions are the actions, exchanges and influences occurring through them. Understanding flows, dependencies, coordination and feedback helps explain the behaviour of the whole.

### Reflection

Choose a system you know and draw its main elements and connections. Distinguish physical flows from information exchanges and dependencies. Which behaviour would be difficult to explain if you ignored one of those relationships? Which important connections are missing from your representation?

**Supporting diagram:** [TV-DIA-002 — Relationships and structure in a water supply network](../../../assets/diagrams/TV-DIA-002/README.md)

## 1.6. Open Systems, Changing Environments and Time

### Openness depends on the boundary and the purpose of the analysis

A system can be bounded for the purpose of analysis without being isolated from everything outside that boundary. To understand its relationship with its environment, we need to identify the exchanges that matter to the analytical question.

Openness is not an absolute property independent of how the system is delimited. The exchanges considered relevant depend on the selected boundary and the purpose of the analysis. Rather than imposing a rigid classification of systems as open or closed, this section focuses on identifying what crosses the boundary and why it matters to the operation we want to understand.

Consider an organisation that includes several facilities. When we analyse it as a whole, exchanges among its facilities are internal to the bounded system. If we then examine one particular facility, some of those same exchanges—for example, energy supply, shared services or operating instructions from another unit—cross the boundary of the system of interest. The exchange itself has not necessarily changed; the analytical boundary from which we observe it has.

### Inputs, outputs and types of exchange

To describe the relationship between a system and what lies beyond its boundary, we need to distinguish two dimensions:

- **Inputs:** what crosses the boundary into the system of interest.
- **Outputs:** what crosses the boundary from the system of interest into its environment.
- **Types of exchange:** the nature of what is exchanged, such as matter, energy, information, resources or services. Any of these may be an input or an output, depending on the system and the selected boundary.

The table illustrates this distinction. It is not intended as a universal or exhaustive classification; the examples depend on the purpose and level of detail of the analysis.

| Type of exchange | Possible input | Possible output |
|---|---|---|
| Matter | Water abstracted for treatment | Distributed water, sludge or waste |
| Energy | Electricity supplied to pumps and equipment | Energy dissipated or transferred to the environment |
| Information | Sensor data, forecasts and incoming instructions | Alerts, measurements, reports or service information |
| Resources and services | Spare parts, technical support or specialist services | Services provided or resources transferred to other systems |

This way of organising exchanges avoids confusing their direction with the nature of what is exchanged. In some systems, financial, regulatory, biological or social flows may also be relevant. Their inclusion should be justified by the analytical question.

Nor should receiving an input be confused with having the conditions required to use it effectively. A facility may receive an electricity supply and still be unable to operate because personnel are unavailable, its control system is faulty or an operational constraint prevents its use. The existence of an exchange does not, by itself, demonstrate that the system can access, integrate or make use of that input to perform its functions.

### The environment can change

A system's environment is not necessarily stable. Demand, resource availability, physical conditions, technologies, regulations and user expectations may all change.

In a water network, a prolonged drought may reduce water availability; a heatwave may increase demand; a regulatory change may require additional monitoring; and a power outage may temporarily limit pumping. Such external changes can alter the conditions under which the system operates even when its internal configuration has not changed.

Influence can also run in the opposite direction. A system's decisions and operations may affect its environment: infrastructure can influence land use, energy consumption or nearby ecosystems. The relationship between a system and its environment is therefore not always one-way.

### Time is part of the description

A description of a system at a particular moment does not necessarily explain how it operates over time. States, relationships, available resources and environmental conditions may change. To understand a dynamic system, we need to examine not only how it is configured but also how it evolves.

Three temporal references should be distinguished. They are related, but they are not interchangeable:

- **Observation time:** when a measurement is taken or a system state is recorded.
- **Data coverage period:** the time interval from which the evidence used in the analysis is drawn.
- **Conclusion horizon:** the period to which the analysis's interpretations or conclusions apply.

A point measurement may describe a condition at the time of observation, but it does not, by itself, show that the condition or a particular behaviour persists for months. Conclusions should be proportionate to the temporal coverage and nature of the available evidence.

It may also be useful to distinguish time scales when organising the analysis:

- **Short term:** operational variations, daily demand cycles, responses to alarms or temporary interruptions.
- **Medium term:** maintenance, seasonal changes, equipment replacement, procedural adjustments and resource availability.
- **Long term:** infrastructure ageing, demographic change, climate trends, technological development and regulatory change.

These scales are not universal and have no fixed durations. A variation that is rapid for one infrastructure may be slow for another system. What matters is choosing a time window suited to the analytical question and not extending conclusions beyond what the evidence supports.

### Response to change, adaptation and transformation

Systems can respond in different ways to environmental changes or disturbances. A **response to change** is a modification in the system's state or behaviour following an internal or external variation. It may involve absorbing a disturbance, adjusting operations, reorganising elements or losing the ability to provide the expected service.

**Adaptation** involves a response that modifies characteristics, capabilities, relationships or ways of operating so that the system can cope with changing conditions. Not every response is an adaptation, and adaptation is not necessarily successful, beneficial or intentional. It may be insufficient, fail or produce unintended consequences; it may also emerge through distributed adjustments or unplanned processes.

We should also distinguish an **operational adjustment** from a **transformation**. The decisive criterion is not how long the change lasts, but its nature and scope:

- An operational adjustment modifies the system's state, behaviour or operating parameters without necessarily changing its fundamental configuration.
- A transformation significantly modifies the system's configuration, organisation, relationships or capabilities and may change what the system is able to do.

For example, temporarily changing a pump's operating set-points may be an operational adjustment. Redesigning the network, reorganising its dependencies or introducing capabilities that change the operations it can perform may constitute a transformation. A brief change may trigger a structural transformation, while a prolonged modification may remain an operational adjustment. Likewise, a transformation does not, by itself, guarantee successful adaptation.

### A snapshot and a trajectory of the system

A system can be described through a representation of its configuration at a particular moment, or through another representation showing how its conditions and behaviour change over time. Both perspectives are useful, but they answer different questions.

A snapshot of the water network may show which reservoirs, pumps and pipes are available at a particular time. A time-based description may show how reservoir levels, demand, energy use and incidents vary over a week or a season.

A temporal account should also state when data were collected, which period they cover and the horizon to which the conclusions apply. Without this information, we may attribute to the system's structure what is actually due to a temporary condition or an external disturbance.

### Key idea

To understand how a system relates to its environment, identify the exchanges that cross the selected boundary and distinguish their direction from their nature. We must also consider changing conditions, the temporal coverage of the evidence, and the difference between responding to change, adapting and transforming.

### Reflection

Choose a system you know. First define the boundary and purpose of your analysis. Which inputs and outputs would you identify, and what types of exchange do they represent? What conditions might prevent the system from using an input it receives? What temporal evidence would you need to distinguish a short-term response, adaptation and transformation?

## 1.7. System Descriptions Are Models: Scope, Assumptions and Omissions

### Describing a system is not the same as reproducing reality

A description of a system is not the system itself. It is a selective representation deliberately constructed to help us understand particular aspects of it, answer a question or support a task. In this chapter, we use **model** in this broad sense: it may take the form of prose, a diagram, a table, a set of variables, or a mathematical or computational model. It need not be expressed through equations or implemented in software to function as a model.

Every representation selects what to show and what to leave out. Even a highly detailed description simplifies reality: it cannot include every possible element, relationship, state, event and condition. This does not automatically make it a poor description. The question is whether its simplifications are appropriate to the purpose of the analysis and whether its limits are made explicit.

In a water supply network, for example, a pipe layout may be sufficient to examine connectivity between reservoirs and consumption areas. It may not be sufficient to analyse the effects of a power interruption, the organisation of maintenance or the consequences of a prolonged change in demand.

### Purpose determines model scope

A model is a selective representation of a system, constructed to answer a question or support a task. Three related but distinct aspects help describe the choices involved:

- **Scope of the representation:** the aspects of the system the model is intended to cover in order to address the question.
- **System boundary:** what is treated as inside and outside the system of interest for the analysis.
- **Level of detail:** how finely the included elements and relationships are represented.

A model may have broad scope while representing some aspects at a low level of detail, or examine a subsystem in considerable detail without covering the entire system.

There is no single model that is equally useful for every question. Consider several possible representations of the same network:

| Analytical question | Useful representation | What it prioritises | What it may leave out |
|---|---|---|---|
| How does water reach each area? | Network layout | Pipes, reservoirs, connections and flow direction | Energy use, maintenance and organisation |
| How does the network respond to changes in demand? | Hydraulic or operational model | Flows, pressures, levels and operating conditions | Organisational decisions or unmodelled social impacts |
| What happens if the electricity supply fails? | Dependency and scenario model | Power supply, pumping, controls and interruption consequences | Hydraulic details that do not affect the question |
| How is continuity of service maintained? | Socio-technical service model | Equipment, staff, procedures, spare parts and coordination | Component details that do not affect continuity |

The representations in the table are not interchangeable. Each makes certain aspects visible and supports a particular kind of reasoning. One may complement another when the question requires different dimensions to be connected.

### Assumptions: what we take as given in order to analyse

A model may use inputs or parameter values that come from different sources. They may be measured, estimated, specified in technical documentation or adopted as assumptions. A value entered into a model is therefore not necessarily an assumption.

For example, a flow rate measured at a point in the network is an observed value; future demand may be an estimate; a pump's rated capacity may come from its technical specification; and treating the pump as available throughout the analysis period is an assumption.

Assumptions are conditions adopted for the purpose of analysis. Some simplify complexity; others establish starting conditions or specify relationships when sufficient information is unavailable. They should be distinguished both from observed facts and from quantified uncertainty: the latter expresses a range or distribution of possible values, rather than a condition simply taken as given.

For example, an analysis of the network might assume that demand remains constant over an interval, that certain items of equipment are available or that pipe characteristics do not change during the period under study. Such assumptions may be reasonable for a particular question and a limited time horizon, but not under other circumstances.

An assumption must not be confused with an observed fact. Nor is it the same as quantified uncertainty. If we do not know whether a pump will be available, we cannot present its availability as confirmed data simply because the model requires a starting condition.

Assumptions that may influence results should be recorded, their rationale explained and the conditions under which they would no longer be acceptable identified. Where possible, we can examine how conclusions change when the most relevant assumptions are varied.

### Omissions: what the model does not represent

Omissions are inevitable, but it is important to distinguish a **deliberate omission** from **unknown or unavailable information**, as discussed in section 1.3. A deliberate omission is an aspect that is known or recognised but intentionally excluded for reasons of scope, purpose or simplicity. Unknown or unavailable information concerns an aspect for which sufficient information or evidence is not available.

An unknown dependency should not be described as though it had been deliberately excluded. Likewise, the absence of an element or relationship from a model does not demonstrate that it does not exist.

Leaving out a detail that is irrelevant to the question can make a model clearer and more manageable. Excluding a critical dependency, however, may produce an incomplete explanation or a misleading conclusion.

Imagine a model that represents the pumps, pipes and reservoirs in a network but excludes the stations' dependence on electricity supply. It may describe certain hydraulic behaviours under normal conditions adequately, yet prove insufficient for analysing service continuity during a power outage.

Therefore, alongside asking what a representation includes, we should ask what it excludes and what consequences that absence may have. An omission becomes especially important when it could change the interpretation, decisions or conclusions of the analysis.

### Suitability and limits of use

A model's quality does not depend solely on its complexity or the number of variables it contains. It depends on its suitability for the question, the quality of the information used and the clarity with which its limits are stated. Evidence supporting the data and relationships does not, by itself, demonstrate that the model is adequate: even with accurate measurements, a representation may omit an important dependency or insufficiently describe relevant behaviour. A checklist can help examine these issues, but it cannot guarantee that the model is correct.

Before using a representation, it is worth checking:

- **Purpose:** What question is it intended to answer?
- **Scope:** Which elements, relationships and conditions does it include?
- **Level of detail:** Is it sufficient for the task without adding unnecessary complexity?
- **Assumptions:** Which conditions are taken as given, and why?
- **Omissions:** Which relevant aspects are not represented?
- **Evidence for data and relationships:** Which measurements, specifications, estimates or observations support the values and connections used?
- **Model adequacy:** Is there a basis for considering that the representation captures the aspects and behaviour relevant to the question?
- **Limits of use:** In which situations should we not use this model to draw conclusions?

These checks do not eliminate uncertainty or guarantee that a model is correct. They help prevent a representation that is useful for one task from being used beyond its intended scope without justification.

### Revisiting the model when the question or system changes

A model should not be treated as final. It may need to be adjusted when the purpose of the analysis changes, new information becomes available, an omitted relationship is identified or the system itself evolves.

If the objective shifts from studying water flow to assessing service resilience, we may need to include energy dependencies, recovery capabilities, staff, procedures and coordination with suppliers. This is not simply a matter of adding detail: the aspects relevant to answering the new question have changed.

It may also be necessary to maintain several complementary representations. A hydraulic model and a socio-technical model may describe different dimensions of the same infrastructure. Before combining them, it is worth checking whether their boundaries, assumptions, time horizons, terminology and levels of detail are compatible. Otherwise, combining them may create an appearance of coherence between representations that cover different scopes or rely on incompatible choices.

### Key idea

Every description of a system is a selective model. Its usefulness depends on whether its scope, assumptions and omissions are appropriate and explicit in relation to the question it is intended to answer.

### Reflection

Think of a system you know and a representation used to describe it. What question can it answer? Which assumptions does it make? What important aspect does it leave out? In what situation might it lead to an incomplete conclusion if used beyond its original purpose?

## 1.8. From Component Optimisation to System-Level Reasoning

### Improving a part does not always improve the whole

In many systems, overall performance depends on the coordinated contribution of multiple components. A local improvement therefore does not guarantee a system-level improvement. A component may become more efficient while transferring costs, constraints or problems to other parts.

In a water supply network, replacing a pump with a higher-capacity unit may increase the flow available at a pumping station. However, it may also raise energy consumption, change pressures in certain sections or require changes to valves, pipes and controls. Assessing only the pump could lead us to consider the intervention successful without checking its consequences for the service as a whole.

Component optimisation remains necessary. The problem arises when local performance is treated as a substitute for system performance.

### Local optimisation and system-level reasoning

**Local optimisation** seeks to improve one or more criteria for a component or subsystem. **System-level reasoning** examines the consequences of decisions for the relevant whole, its dependencies and the environment insofar as these matter to the decision.

System-level reasoning does not necessarily mean solving a mathematical global optimisation problem. Nor does it imply that every criterion can be maximised at the same time: some criteria may conflict.

| Decision focus | Main question | Risk if considered in isolation |
|---|---|---|
| Component | How can this item of equipment perform better? | Improving its performance at the expense of other parts |
| Subsystem | How can we coordinate the elements that perform a function? | Shifting a significant limitation to another subsystem |
| System | How does the whole achieve its required outcomes? | Ignoring dependencies, external effects or later consequences |

The point is not always to choose the broadest level. It is to select the level of analysis appropriate to the decision and examine relevant consequences at connected levels.

### Constraints, bottlenecks and interdependencies

A **constraint** is a condition that limits available alternatives, performance or possible outcomes. A **bottleneck** is an element, capacity or process whose limitation significantly restricts the performance of the whole in relation to a specified outcome. Some constraints may not be the dominant limiting factor, and a bottleneck may shift as the system configuration changes.

Local improvements may change the operating conditions of other parts, including parts that are not directly modified. Through relationships, interfaces and dependencies, they may alter flows, loads, resource distribution or coordination requirements. These effects may create benefits, costs or new trade-offs; they may also produce synergies and should not automatically be assumed to be negative.

In the water network, increasing pumping capacity may ease a limitation at the station and make the capacity of a pipe, valve or storage tank more significant. It may also improve supply in one area while increasing energy consumption or maintenance needs. The effect depends on the configuration and relationships among the parts.

It is therefore useful to identify which elements and functions may be affected, which dependencies condition the outcome, which additional resources may be needed and which indirect effects may arise. Not every local improvement necessarily shifts a bottleneck, and not every interdependency produces an adverse effect.

### Requirements, performance objectives and preferences

System performance is rarely captured by a single measure. A water network may be assessed in terms of supply continuity, quality, pressure, energy consumption, operating costs, recovery time and environmental effects. Improving one criterion may worsen another.

When comparing alternatives, it is useful to distinguish:

- **Requirements:** conditions that must be met for the system or solution to be acceptable.
- **Performance objectives:** outcomes that a decision seeks to achieve or improve, allowing for different degrees of attainment.
- **Preferences:** criteria used to compare alternatives that meet the applicable requirements but involve different trade-offs.

These categories are not interchangeable. Failure to meet an applicable mandatory requirement cannot simply be compensated for by better results on other indicators. Whether a requirement is mandatory depends on the decision framework and relevant conditions.

For example, maintaining high pressure may help supply certain areas but increase leakage losses and energy use. Reducing maintenance costs may improve a short-term financial indicator while increasing the risk of future interruptions. A decision requires making explicit the outcomes sought, the constraints that must be respected and the trade-offs that are acceptable.

### Direct, indirect and unintended effects

When assessing an intervention, it is useful to distinguish among:

- **Direct effects:** consequences occurring in the element or subsystem being changed.
- **Indirect effects:** consequences arising elsewhere in the system through relationships, interfaces or dependencies.
- **Unintended effects:** consequences that harm relevant outcomes or create risks that were not anticipated, whether direct or indirect.

These categories can overlap. An unintended effect may be direct or indirect. Analysis can identify plausible consequences, but it cannot guarantee that every effect will be anticipated; subsequent observation may reveal additional effects.

### Time horizons for evaluation

The results of an intervention also depend on the time horizon considered:

- **Short term:** immediate effects of the intervention and its commissioning or initial operation.
- **Medium term:** consequences emerging during operation and the adjustment or adaptation of affected parts.
- **Long term:** cumulative effects, changing needs, wear, maintenance and evolution of the environment.

These horizons are analytical references, not universal time intervals. Their duration depends on the system, the intervention and the decision being evaluated. An initial improvement should not be presented as sustained improvement without sufficient evidence of subsequent behaviour.

### Scope and proportionality of the analysis

System-level reasoning does not require analysing every possible element, relationship and consequence. It requires identifying and examining those relevant to the decision. To determine the necessary depth and breadth, consider the importance of the outcomes affected, the magnitude and likelihood of potential consequences, uncertainty in the available information, the reversibility of the intervention and the consequences of an incorrect decision.

The analysis should be proportionate to the importance and risk of the decision. It should also make explicit the boundary and scope considered, as well as the uncertainties that remain unresolved. A minor intervention may require a simple check; a critical change may call for broader analysis and more rigorous testing. Widening the boundary does not always improve an analysis: it should be done when it provides information relevant to the decision.

### Reasoning at system level

System-level reasoning places technical detail within a configuration of relationships, objectives, constraints and operating conditions. As a guide, it can be organised around the following questions:

1. **What outcome is sought, and for whom?** Clarify the relevant outcomes and conditions for acceptability.
2. **What is being changed?** Define the component or subsystem targeted by the intervention.
3. **Which other parts are connected?** Examine interfaces, dependencies and interactions that may constrain or receive the effects of the change.
4. **Which criteria and trade-offs matter?** Distinguish requirements, objectives and preferences, and identify potential conflicts.
5. **What effects may arise, and when?** Consider direct, indirect and unintended effects, together with appropriate time horizons.
6. **What depth of analysis is proportionate?** Consider importance, consequences, uncertainty and reversibility, and state the limits of the analysis.
7. **What should be checked afterwards?** Observe whether expected outcomes are sustained and whether additional consequences emerge.

These questions are not an exhaustive method and do not guarantee that every effect will be identified. They help organise analysis around the consequences that matter to the decision.

### The value of an improvement depends on where and how it appears

A technical improvement becomes meaningful when related to the outcomes the system is expected to produce. Reducing a pump's energy consumption may be positive, but its significance depends on whether the required service is maintained, how other equipment is affected and which costs or risks are introduced.

Likewise, an improvement to the whole need not maximise every indicator. It may consist of reaching a defensible balance among different outcomes, constraints and needs. Making these trade-offs explicit allows alternatives to be compared without presenting one particular preference as a universal solution.

### Key idea

Optimising a component does not necessarily improve the system. System-level reasoning examines relevant interdependencies, requirements, objectives, constraints, effects and time horizons. Its scope should be proportionate to the decision, and its limits and uncertainties should be made explicit.

### Reflection

Think of an improvement made or proposed to a component of a system you know. Which local indicator was it intended to improve? Which other parts could be affected, and how? Which requirements, objectives, preferences and time horizons would need to be considered to determine whether the intervention genuinely improved the system's performance?

## 1.9. Chapter Synthesis and Reflection Questions

### Understanding a system as a connected configuration

Understanding a system involves more than identifying its components. It requires relating the purpose guiding the analysis to the elements, actors, resources and capabilities involved; to the relationships, interactions and dependencies that connect them; and to the environmental and contextual conditions in which the system operates. These dimensions shape one another: a capability depends on resources and relationships, while a change in one part may alter the operating conditions of others.

This understanding is always developed from a particular perspective and in response to a particular question. Describing a system therefore involves deciding what falls inside and outside the boundary, which interfaces and exchanges matter, what period is being considered and what level of detail is appropriate. A representation selects information and may combine observations, estimates, specifications and assumptions. Distinguishing what is known from what is unknown and what has been deliberately omitted helps prevent conclusions from exceeding the representation's scope.

Behaviour is understood by examining how states change and how relationships among parts shape those changes over time. Similarly, assessing an intervention requires looking beyond the component being modified. Dependencies, constraints, direct and indirect effects, trade-offs among criteria and consequences emerging over different time horizons all matter. The depth of analysis should be proportionate to the decision, and its limits should be made explicit.

### Bringing the dimensions together

The table connects dimensions that should remain in view when describing and analysing a system. The questions guide inquiry, while the final column highlights relevant links among dimensions. It is neither an exhaustive checklist nor a mandatory procedure: its usefulness depends on the system and the purpose of the analysis.

| Dimension | Guiding question | What it helps us examine | Relationship to other dimensions |
|---|---|---|---|
| Purpose and context | Which outcomes matter, for whom and under what conditions? | The purpose of the analysis and of the system, relevant actors and contextual conditions | Guides the boundary, performance criteria and selection of information for the model |
| Composition and capabilities | Which elements, actors, resources and capabilities are involved? | What is present, what each part can contribute and what it depends on | Capabilities rely on resources, relationships and interfaces |
| Organisation and interactions | How are the parts related and coordinated? | Flows, dependencies, interfaces, authority and effects between components | Shapes behaviour and constrains or enables available capabilities |
| Boundary and environment | What is included in the analysis, and which exchanges cross its boundaries? | Inputs, outputs, external dependencies and relevant impacts | Determines which relationships are treated as internal or external and which context matters |
| Time and change | What varies, how does the system respond and over what horizon? | States, trajectories, disturbances, responses and trends | Supports interpretation of behaviour and evaluation of intervention effects over time |
| Model and evidence | What does the description represent, what is it based on and what does it leave out? | Fitness for purpose, data, estimates, assumptions, omissions and uncertainty | Makes explicit the limits within which the other dimensions should be interpreted |
| Overall performance | How do decisions affect system outcomes and connected parts? | Requirements, objectives, constraints, bottlenecks, trade-offs and indirect effects | Integrates capabilities, interdependencies, evaluation criteria and time horizons |

### Applying the perspective to a familiar system

Choose a system you know — a facility, a service, an organisational process or an infrastructure network — and prepare a short description that would help another person understand it. You do not need to build a formal model or assess the system comprehensively. Make four things explicit:

1. **Purpose and question:** why you are preparing the description and what question it is intended to answer.
2. **Boundary and context:** what you include, what you leave out, and which elements, actors, relationships or conditions you consider relevant.
3. **Knowledge and assumptions:** what information you know, which values or relationships you are assuming, and what information is missing or has not yet been examined.
4. **Scope and limits:** what your description helps explain and which conclusions it would not justify.

The important task is to justify your analytical choices and distinguish what has been observed or supported from what is estimated, assumed or still unknown.

### Reflection questions

1. **Purpose, actors and boundary:** Imagine a service used by several groups with different needs. How might those perspectives change the definition of relevant outcomes and the boundary you would choose for analysing the service?
2. **Capabilities and dependencies:** If an organisation has qualified staff and suitable equipment but depends on an external supplier for a critical resource, what would support the claim that it can deliver the service, and what conditions might limit that capability?
3. **Model, evidence and time:** A system description is based on measurements collected over one week. Which aspects of its behaviour might it represent adequately, and which might remain hidden because of the observation period, assumptions or missing information?
4. **Interdependencies and performance:** A water network increases pumping capacity to improve supply in one area. Which other parts might be affected, and how would you compare the benefits with changes in pressure, energy use, maintenance and operating constraints?
5. **Intervention and time-based evaluation:** Before concluding that an intervention has improved the system, which outcomes and criteria should be observed, over what time horizons, and with what uncertainties or indirect effects in mind? What evidence would distinguish an initial improvement from a sustained one?

### Closing the chapter

Thinking in systems means understanding components in relation to the capabilities, interactions and conditions that make the system's operation possible. The configuration of elements, resources and relationships shapes what a system can do, as well as the options for change available to it. A useful description supports reasoning about those possibilities without confusing what is known with what is assumed or concealing the limits of the analysis.

The next chapter will examine transformation in relation to system capability: how a system can change and what determines the transformations genuinely within its reach. Not every change necessarily constitutes a transformation, and not every transformation creates value in itself.
