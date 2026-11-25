# TGCV — Explore Copy

**Identifier:** TGCV-WEB-EXPLORE-COPY-001  
**Version:** 1.0  
**Date:** 2026-11-25  
**Status:** BILINGUAL WORKING COPY — NOT APPROVED FOR PUBLICATION  
**Parent:** `06_WEB/TGCV_WEB_EXPLORE_EXPERIENCE_v0.1.md`  
**Branch:** `strategy/tgcv-web-master`

---

## 1. Editorial purpose

This document contains the Spanish and English working copy for the first Explore release. Both versions express the same concepts, claims, caveats and visitor routes. They are editorial adaptations, not line-by-line translations.

Explore starts where Home leaves off. Home introduces the idea that a system's possibilities can change; Explore deepens the explanation by examining how candidate transformations are assessed for accessibility, how that assessment depends on system boundaries and conditions, and what accessibility does—and does not—tell us. It is written primarily for people who research, design, develop or engineer systems, while remaining understandable to interested visitors outside those fields.

The software-migration scenario is an illustrative editorial example. It is not an existing execution, validated application, Juguete Colectivo feature or C10-S result.

# 2. Spanish version

## ¿Qué cambia cuando cambia lo que un sistema puede hacer?

Un sistema no está definido únicamente por su estado actual. También importa qué transformaciones puede realizar, cuáles están realmente a su alcance y qué tendría que cambiar para hacer posibles otras.

Comprender esta dimensión permite mirar los sistemas desde una perspectiva diferente: no solo preguntarnos cómo funcionan hoy, sino cómo pueden cambiar sus posibilidades de transformación.

---

## 2.1 De la intuición a una pregunta más precisa

Home introduce una idea: las posibilidades de un sistema pueden cambiar cuando cambian determinadas condiciones. Explore da un paso más y plantea una pregunta:

**¿Cómo sabemos si una transformación está realmente al alcance de un sistema?**

Para responder, no basta con enumerar lo que un sistema podría hacer. Necesitamos identificar qué sistema estamos considerando, dónde establecemos sus límites, bajo qué condiciones lo analizamos y qué transformaciones contemplamos en ese contexto.

*Orientación visual:* Un esquema sencillo que muestre el sistema y sus límites, las condiciones relevantes y varias transformaciones candidatas.

---

## 2.2 Ser candidata no significa ser accesible

Retomemos brevemente el ejemplo de migración de configuración presentado en Home. La operación considerada es la misma en ambos entornos. Para aislar el contraste de este ejemplo, mantenemos constantes la configuración considerada, la operación, los límites asumidos y los demás requisitos relevantes especificados. La única diferencia que examinamos es que la dependencia necesaria está disponible en el entorno A y falta en el entorno B. Esto permite explicar el papel de esa dependencia en la accesibilidad; no significa que sea el único factor que podría influir en una migración real.

Por tanto, la operación puede considerarse una transformación candidata en ambos entornos, pero solo es accesible en A bajo las condiciones representadas.

Una **transformación candidata** es un cambio que se contempla como posibilidad para un sistema dentro de un contexto de análisis. Que se considere candidata no significa que el sistema reúna las condiciones necesarias para realizarla.

**Una transformación puede ser candidata sin ser accesible.**

*Orientación visual:* Comparación breve de ambos entornos. La transformación candidata se mantiene idéntica; solo cambia la disponibilidad de la dependencia y, con ella, su condición de accesibilidad.

---

## 2.3 La accesibilidad depende de las condiciones y de los límites considerados

La dependencia ausente en el entorno B ilustra una de las formas en que puede cambiar la accesibilidad. Cuando esa dependencia se hace disponible en el entorno de destino, manteniendo los demás supuestos del ejemplo, la transformación puede pasar a ser accesible bajo las nuevas condiciones.

Esta conclusión tiene un alcance delimitado: se refiere al sistema, la transformación, los límites y las condiciones que se han especificado. No demuestra que la transformación se haya ejecutado, que vaya a tener éxito ni que su resultado tenga valor.

La accesibilidad no es una propiedad que deba interpretarse al margen del sistema y de su contexto. Se evalúa respecto de los límites y las condiciones que estamos considerando.

**La accesibilidad depende del sistema, de sus límites y de las condiciones consideradas.**

*Orientación visual:* Estado del entorno B antes y después de hacer disponible la dependencia. Se modifica únicamente el estado de accesibilidad; no se representa ejecución ni éxito.

## 2.4 Posibilidad, ejecución, resultado y valor

Imagina que ahora la operación está al alcance del entorno B. ¿Qué podemos afirmar realmente? ¿Que el sistema puede realizarla, que ya la ha realizado o que ha obtenido algo valioso?

No son afirmaciones equivalentes. Conviene mantener visible una distinción central:

**Accesibilidad → Ejecución → Resultado → Valor**

Esta secuencia organiza niveles de análisis; no es una explicación causal completa ni sustituye el análisis de las condiciones, los mecanismos y las trayectorias concretas del sistema.

- **Accesibilidad:** la transformación está al alcance del sistema bajo los límites y las condiciones consideradas. No significa que se haya realizado.
- **Ejecución:** el sistema realiza efectivamente la transformación.
- **Resultado:** el estado o efecto que se produce como consecuencia de la ejecución.
- **Valor:** la relevancia o contribución de ese resultado, evaluada según un contexto y unos criterios determinados.

La **transformación candidata** es anterior a esta secuencia: es la transformación que se contempla y cuya accesibilidad se evalúa. Ser candidata no significa que esté al alcance del sistema.

Una transformación puede estar a nuestro alcance y no ejecutarse. Puede ejecutarse y no producir el resultado esperado. Y un resultado, incluso cuando es satisfactorio, no tiene por qué representar el mismo valor para todos los sistemas o contextos.

Cuando cambia la accesibilidad, también cambia el conjunto de opciones que están al alcance del sistema en ese contexto. Esto puede abrir nuevas formas de actuar o de diseñar una intervención. Decidir si esas opciones son útiles o deseables requiere objetivos y criterios adicionales.

Las transformaciones pueden relacionarse y condicionar lo que el sistema podrá hacer después. La trayectoria describe la evolución del sistema a través de estados y transformaciones; no presupone que todas formen una única cadena ni constituye una etapa adicional después del valor.

**Que cambie lo que un sistema puede hacer no garantiza, por sí mismo, un resultado favorable ni la generación de valor.**

*Orientación visual:* Mostrar de forma destacada y legible la secuencia **Accesibilidad → Ejecución → Resultado → Valor**. Situar «Transformación candidata» antes de la secuencia, como el objeto cuya accesibilidad se evalúa. Representar la trayectoria como un recorrido que atraviesa distintos estados y transformaciones, no como una quinta etapa ni como una prolongación de la cadena.

---

## 2.5 El espacio de posibilidades de un sistema

**¿Qué nuevas opciones aparecen cuando un sistema puede hacer algo que antes no estaba a su alcance?**

Para responder, necesitamos mirar más allá de las capacidades de cada componente por separado. Un sistema puede contener todos los elementos necesarios para una operación y, aun así, no tener esa transformación a su alcance. También importa cómo se relacionan esos elementos, de qué dependen y bajo qué condiciones pueden trabajar conjuntamente.

Podemos observarlo desde tres preguntas:

- **¿Qué elementos hay y qué puede hacer cada uno?** Los componentes tienen capacidades distintas; los recursos y las dependencias pueden estar disponibles o faltar.
- **¿Cómo se relacionan?** Las conexiones, interfaces e interacciones permiten que algunos elementos trabajen juntos, o pueden impedirlo aunque los componentes existan.
- **¿En qué condiciones pueden actuar?** Las reglas, permisos, restricciones y condiciones del entorno pueden habilitar, limitar o bloquear determinadas transformaciones.

Volvamos al ejemplo de la migración. En ambos entornos consideramos la misma operación y mantenemos los demás supuestos. Sin embargo, en el entorno B falta la dependencia necesaria. Los componentes pueden estar presentes, pero esa relación de dependencia no está satisfecha. Por eso, la operación puede ser una transformación candidata sin estar todavía al alcance del sistema bajo esas condiciones.

Esto muestra por qué no basta con conocer los elementos de un sistema: también necesitamos comprender cómo están conectados y qué condiciones hacen posible que funcionen conjuntamente.

Estas dimensiones no actúan de forma independiente. Un cambio en una condición puede modificar una dependencia, hacer que una conexión pueda utilizarse o deje de estar disponible y, como consecuencia, habilitar una transformación mientras limita otra. Las posibilidades pueden abrirse, cerrarse o reorganizarse; ampliarlas no es necesariamente beneficioso en todos los contextos.

Aquí resulta útil el pensamiento sistémico (*Systems Thinking*): una perspectiva que ayuda a observar conjuntamente los límites del sistema, sus relaciones, dependencias, condiciones y dinámicas.

**Las posibilidades de un sistema dependen no solo de lo que sus elementos pueden hacer por separado, sino también de cómo se relacionan y de las condiciones en las que pueden actuar conjuntamente.**

*Orientación visual:* Representar un sistema sencillo con varios componentes, una dependencia entre dos de ellos y una condición externa. Mostrar que los componentes pueden existir, pero que una transformación sigue fuera del alcance mientras falte la dependencia necesaria. Después, mostrar cómo el cambio de esa condición puede modificar la relación y la accesibilidad de la transformación. Evitar una red demasiado compleja o una lista visual de factores.

## 2.6 Una nueva forma de comprender y orientar las transformaciones

Si las posibilidades de un sistema pueden cambiar, necesitamos comprender cómo se producen esos cambios, cómo se relacionan con su evolución y qué consecuencias pueden tener. Para abordar esa cuestión se necesitan perspectivas y prácticas complementarias.

**Systems Thinking — comprender los sistemas**

Una perspectiva para observar conjuntamente los límites del sistema, sus elementos, relaciones, dependencias, condiciones, restricciones y dinámicas. Ayuda a comprender cómo se relaciona el conjunto, en lugar de analizar cada componente de forma aislada.

**Systems Engineering — diseñar e intervenir**

Una disciplina de ingeniería, con métodos y prácticas para modelar, diseñar, desarrollar, integrar e intervenir en sistemas. Permite llevar la comprensión de un sistema al terreno de su diseño y transformación.

**Transformational Intelligence — integrar el razonamiento sobre el cambio**

Un concepto de capacidad integradora en desarrollo. Busca conectar la comprensión de un sistema con el razonamiento sobre las transformaciones que pueden estar a su alcance, los cambios en esas posibilidades, las trayectorias que podrían abrirse y las consecuencias de distintas intervenciones.

En términos prácticos, la pregunta que orienta este concepto es: ¿cómo podemos comprender un sistema, examinar qué transformaciones puede realizar bajo determinadas condiciones, razonar sobre cómo podrían cambiar sus posibilidades y orientar esos cambios? Esto expresa el propósito de la capacidad que se quiere desarrollar, no un método completo ni una capacidad operativa ya validada.

Transformational Intelligence no es otro nombre para Systems Thinking o Systems Engineering, ni es sinónimo de inteligencia artificial. La IA puede aportar tecnologías de apoyo, pero no define el concepto. Tampoco se presenta como una disciplina académica consolidada o como una capacidad generalmente validada.

TGCV — Transformaciones Generativas y Construcción de Valor es el programa de investigación aplicada e innovación que estudia cómo las condiciones y relaciones de un sistema influyen en las transformaciones que tiene a su alcance y cómo estas pueden relacionarse con sus trayectorias y la construcción de valor. Esa investigación contribuye a las bases para desarrollar y examinar el concepto de Transformational Intelligence. Ambos están relacionados, pero no son equivalentes: TGCV es el programa de investigación; Transformational Intelligence es un concepto de capacidad que busca integrar comprensión, razonamiento y orientación del cambio.

**El objetivo no es solamente comprender los sistemas o intervenir en ellos, sino desarrollar formas de razonar sobre los cambios en lo que pueden hacer y sobre cómo orientar esos cambios.**

## ¿Por dónde quieres continuar?

**Profundiza en la investigación y los conceptos**

- **Research** — Explora los fundamentos, modelos, preguntas y líneas de investigación de TGCV.
- **Systems Engineering** — Descubre cómo la ingeniería de sistemas permite modelar, diseñar, integrar e intervenir en sistemas.
- **Transformational Intelligence** — Conoce el concepto de capacidad integradora en desarrollo y las preguntas que orientan su investigación.

**Explora una vía de aplicación complementaria**

- **Value Construction** — Descubre cómo VALUE, un framework aplicado complementario a TGCV, organiza la comprensión de oportunidades, el diseño de alternativas, las decisiones, la acción y el aprendizaje en la búsqueda de valor contextual.

TGCV investiga si los cambios en las transformaciones accesibles pueden contribuir a la construcción de valor. VALUE ofrece un marco propio para organizar el trabajo aplicado; su metodología y eficacia tienen fundamentos y evaluación propios. Esta conexión no implica que TGCV haya validado VALUE ni que ampliar las posibilidades de un sistema produzca valor automáticamente.

*Las posibilidades de un sistema no terminan en lo que puede hacer hoy. Comprender cómo cambian es el primer paso para explorar lo que puede llegar a hacer.*

# 3. English version

## What changes when a system changes what it can do?

A system is defined by more than its current state. What also matters is which transformations it can perform, which ones are actually within its reach, and what would need to change to make others possible.

Understanding this dimension offers a different way of looking at systems: instead of asking only how they work today, we can also ask how their possibilities for transformation can change.

---

## 3.1 From the Home insight to a more precise question

Home introduces the idea that a system's possibilities can change when relevant conditions change. Explore takes the next step:

**How do we determine whether a transformation is actually within a system's reach?**

Answering this requires more than listing what a system might do. We need to identify the system being considered, where its boundaries are drawn, the conditions under which it is analysed, and the transformations considered within that analytical context.

*Visual guidance:* A simple frame showing the system and its boundaries, relevant conditions and several candidate transformations.

---

## 3.2 Candidate does not mean accessible

Briefly return to the software-configuration migration introduced on Home. The operation being considered is the same in both environments. To isolate the contrast in this example, keep the configuration being considered, the operation, the stated boundary assumptions and the other specified relevant prerequisites constant. The only difference examined is that the required dependency is available in environment A and missing in environment B. This illustrates the role of that dependency in accessibility; it does not mean it is the only factor that could matter in a real migration.

The operation can therefore be considered a candidate transformation in both environments, but it is accessible only in A under the conditions shown.

A **candidate transformation** is a change considered as a possibility for a system within an analytical context. Being considered a candidate does not mean that the system meets the conditions required to carry it out.

**A transformation may be a candidate without being accessible.**

*Visual guidance:* A concise comparison of the two environments. Keep the candidate transformation identical; show only the dependency condition and resulting accessibility status as different.

---

## 3.3 Accessibility depends on conditions and boundaries

The missing dependency in environment B illustrates one way accessibility can change. When that dependency is made available in the target environment, while the other assumptions in the example remain unchanged, the transformation may become accessible under the revised conditions.

This conclusion is bounded: it concerns the specified system, transformation, boundary and conditions. It does not establish that the transformation has been executed, that it will succeed, or that its outcome will have value.

Here, **accessibility of transformations** refers to whether a transformation is within a system's reach under the system boundary and conditions being considered. It is not the same as digital or interface accessibility.

**Accessibility is assessed relative to a system, its boundary and the conditions being considered.**

*Visual guidance:* Show the target environment before and after the dependency becomes available. Mark only the accessibility status as changed; do not depict execution or success.

## 3.4 Possibility, execution, outcome and value

Imagine that the operation is now within the reach of environment B. What can we actually claim? That the system can perform it, that it has already performed it, or that it has achieved something valuable?

These are not equivalent claims. One distinction should remain clearly visible:

**Accessibility → Execution → Outcome → Value**

This sequence organises analytical distinctions; it is not a complete causal explanation and does not replace analysis of the system's specific conditions, mechanisms and trajectories.

- **Accessibility:** the transformation is within the system's reach under the boundary and conditions being considered. This does not mean it has been performed.
- **Execution:** the system actually performs the transformation.
- **Outcome:** the state or effect produced as a consequence of execution.
- **Value:** the relevance or contribution of that outcome, assessed against a particular context and set of criteria.

The **candidate transformation** comes before this sequence: it is the transformation being considered and whose accessibility is assessed. Being a candidate does not mean that it is within the system's reach.

A transformation can be within a system's reach without being executed. It can be executed without producing the expected outcome. And even a satisfactory outcome does not necessarily represent the same value for every system or context.

When accessibility changes, the set of options within the system's reach in that context changes too. This may open new ways to act or design an intervention. Deciding whether those options are useful or desirable requires additional objectives and contextual criteria.

Transformations may relate to one another and shape what the system can do next. A trajectory describes the system's evolution through states and transformations; it does not assume that all transformations form one chain, nor is it an additional stage after value.

**A change in what a system can do does not, by itself, guarantee a favourable outcome or the creation of value.**

*Visual guidance:* Make **Accessibility → Execution → Outcome → Value** a prominent, readable sequence. Place “Candidate transformation” before it, as the object whose accessibility is assessed. Represent trajectory as a path across different states and transformations, not as a fifth stage or an extension of the chain.

---

## 3.5 A system's space of possibilities

**What new options become available when a system can do something that was previously beyond its reach?**

To answer this, we need to look beyond the capabilities of individual components. A system may contain all the elements needed for an operation and still not have that transformation within its reach. How those elements relate, what they depend on and under which conditions they can work together also matters.

We can examine this through three questions:

- **What elements are present, and what can each one do?** Components have different capabilities; resources and dependencies may or may not be available.
- **How are they related?** Connections, interfaces and interactions allow some elements to work together, or may prevent this even when the components are present.
- **Under what conditions can they act?** Rules, permissions, constraints and environmental conditions can enable, limit or block particular transformations.

Return to the migration example. We consider the same operation in both environments and keep the other assumptions unchanged. However, the required dependency is missing in environment B. The components may be present, but that dependency relationship is not satisfied. The operation can therefore be a candidate transformation without yet being within the system's reach under those conditions.

This shows why knowing which elements a system contains is not enough: we also need to understand how they are connected and what conditions allow them to work together.

These dimensions do not operate independently. A change in one condition may alter a dependency, make a connection usable or unavailable and, as a result, enable one transformation while constraining another. Possibilities can open, close or be reorganised; expanding them is not necessarily beneficial in every context.

This is where *Systems Thinking* becomes useful: a perspective that helps us examine system boundaries, relationships, dependencies, conditions and dynamics together.

**A system's possibilities depend not only on what its elements can do individually, but also on how they are related and on the conditions under which they can work together.**

*Visual guidance:* Show a simple system with several components, a dependency between two of them and one external condition. Make clear that the components may be present while a transformation remains out of reach because the required dependency is missing. Then show how changing that condition may alter the relationship and the accessibility of the transformation. Avoid an overly complex network or a visual checklist of factors.

## 3.6 A new way to understand and guide transformations

If a system's possibilities can change, we need to understand how those changes occur, how they relate to the system's evolution and what consequences they may have. Addressing this requires complementary perspectives and practices.

**Systems Thinking — understanding systems**

A perspective for examining system boundaries, elements, relationships, dependencies, conditions, constraints and dynamics together. It helps us understand how the whole is connected rather than analysing each component in isolation.

**Systems Engineering — designing and intervening**

An engineering discipline, with methods and practices for modelling, designing, developing, integrating and intervening in systems. It helps translate an understanding of a system into its design and transformation.

**Transformational Intelligence — integrating reasoning about change**

A working concept of an integrative capability under development. It seeks to connect system understanding with reasoning about transformations that may be within a system's reach, changes in those possibilities, trajectories that may become available and the consequences of alternative interventions.

In practical terms, the question guiding this concept is: how can we understand a system, examine which transformations it can carry out under specified conditions, reason about how its possibilities might change and guide those changes? This expresses the purpose of the capability being developed; it is not a complete method or an already validated operational capability.

Transformational Intelligence is not another name for Systems Thinking or Systems Engineering, nor is it synonymous with artificial intelligence. AI may provide supporting technologies, but it does not define the concept. It is also not presented as a consolidated academic discipline or a generally validated capability.

TGCV — Generative Transformations and Value Construction is the programme of applied research and innovation that explores how a system's conditions and relationships influence the transformations within its reach and how these may relate to its trajectories and the construction of value. This research contributes to the foundations for developing and examining the Transformational Intelligence concept. They are related but not equivalent: TGCV is the research programme; Transformational Intelligence is a capability concept seeking to integrate understanding, reasoning and guidance of change.

**The aim is not only to understand systems or intervene in them, but to develop ways of reasoning about changes in what they can do and how those changes might be guided.**

## Where would you like to go next?

**Explore the research and its conceptual foundations**

- **Research** — Explore TGCV's foundations, models, questions and research directions.
- **Systems Engineering** — Discover how systems engineering helps model, design, integrate and intervene in systems.
- **Transformational Intelligence** — Learn about the integrative capability concept under development and the questions guiding its investigation.

**Explore a complementary applied approach**

- **Value Construction** — Discover how VALUE, an applied framework complementary to TGCV, organises opportunity understanding, alternative design, decisions, action and learning in pursuit of contextual value.

TGCV investigates whether and how changes in accessible transformations may contribute to value construction. VALUE provides its own framework for organising applied work, with its own methodological foundations and evaluation. This connection does not mean that TGCV has validated VALUE or that expanding a system's possibilities automatically produces value.

*A system's possibilities do not end with what it can do today. Understanding how they change is the first step towards exploring what it could do next.*

---

## 4. Bilingual editorial controls

- Both language versions must remain complete and conceptually equivalent.
- “Accessibility of transformations” introduces the analytical meaning in English; “accessible transformations” and “within the system's reach” may be used where natural.
- “Outcome” is the consistent English equivalent of “resultado” in this explanatory context.
- “Trajectory” refers to the system's evolution through states and transformations, not to an isolated outcome or an automatic stage after value.
- Keep the visible distinction **Accessibility → Execution → Outcome → Value**; candidate transformation precedes it, while trajectory is represented across states and transformations rather than as another stage.
- “Transformational Intelligence” remains a working capability concept under development.
- The software-migration example is illustrative in both languages and must not be represented as an executed or validated case.
- Any future edit to one language must trigger a corresponding conceptual check of the other.


## 5. Version history
- **0.1 — 2026-11-24:** Initial bilingual Explore copy.
- **0.2 — 2026-11-24:** Integrates the Home-to-Explore editorial hand-off, the single-dependency example, a broader candidate-transformation definition and an explicit English definition of accessibility of transformations.
- **0.3 — 2026-11-24:** Makes the practical implication of changed accessibility explicit in both languages, clarifies accessible as “within reach” rather than performed, and refines trajectory wording so it does not imply one inevitable chain of transformations.
- **0.4 — 2026-11-24:** Adds the explicit block-5 question about newly available options in Spanish and English; makes **Accessibility → Execution → Outcome → Value** a persistent visual anchor; places candidate transformation before that sequence and trajectory across states and transformations.


- **0.5 — 2026-11-25:** Aligns the Spanish and English TGCV identity statements with the approved public name and applied-research-and-innovation programme description; removes the superseded public-facing “Theory” wording.

- **0.6 — 2026-11-25:** Clarifies in Spanish and English that the migration comparison holds the stated system/configuration, operation, boundary assumptions and other specified prerequisites constant while varying one dependency-availability condition; explicitly bounds the inference to the illustration.

- **0.7 — 2026-11-25:** Rewrites the space-of-possibilities section in Spanish and English to explain how element capabilities, relationships/dependencies and operating conditions jointly shape accessible transformations.

- **0.8 — 2026-11-25:** Rewrites the Spanish and English TI explanation to distinguish the developing capability concept from Systems Thinking, Systems Engineering, AI and the TGCV research programme; clarifies intended function without implying validation.
- **0.9 — 2026-11-25:** Clarifies in both languages that the visible accessibility/execution/outcome/value sequence is an analytical distinction, not a complete causal explanation.
- **1.0 — 2026-11-25:** Adds a distinct Value Construction route in both languages, separating conceptual/research deepening from the complementary applied VALUE framework and stating their non-validated relationship.
