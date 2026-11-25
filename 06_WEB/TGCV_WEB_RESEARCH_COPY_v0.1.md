# TGCV — Research Page Copy v0.1

**Identifier:** TGCV-WEB-RESEARCH-COPY-001  
**Version:** 0.3  
**Date:** 2026-11-25  
**Status:** EDITORIAL WORKING DRAFT — NOT APPROVED FOR PUBLICATION  
**Branch:** `strategy/tgcv-web-master`  
**Depends on:** Web Master Brief v1.5; Research Experience v0.2; Information Architecture v1.8; Content Blueprint v1.7; current TGCV Core; Research Prospectus v0.2; Testable Concept Paper v0.4; Architectural Research Map v0.2; current RMA v3.38 and Evidence→Claim Matrix v1.47.

> This is a first bilingual editorial draft. It is not a scientific asset, does not change claim status, and does not authorize publication of controlled scientific records. The evidence snapshot must be rechecked immediately before publication.

---

# ESPAÑOL

## 1. TGCV: un programa para investigar cómo cambian las posibilidades de transformación de los sistemas

**TGCV — Transformaciones Generativas y Construcción de Valor**

*Un programa de investigación aplicada e innovación sobre cómo la ampliación de las posibilidades de transformación de los sistemas puede contribuir a la construcción de valor.*

TGCV investiga cómo las condiciones de un sistema determinan qué transformaciones están a su alcance, cómo cambia esa estructura de posibilidades y bajo qué condiciones esos cambios pueden relacionarse con lo que el sistema puede alcanzar y con las trayectorias que puede seguir.

La pregunta no presupone que ampliar las posibilidades produzca necesariamente mejores resultados. La investigación estudia también contracciones, pérdidas, reconfiguraciones y situaciones en las que no puede establecerse una relación útil entre los cambios observados.

TGCV es un programa de investigación integrador y falsable, no una teoría consolidada ni una explicación universal de todos los sistemas.

## 2. ¿Qué investiga TGCV?

Un sistema puede describirse por su estado o configuración en un momento determinado. Pero conocer ese estado no basta para saber qué cambios puede realizar. Las transformaciones que están a su alcance dependen también del contexto, las restricciones, los recursos y otras condiciones relevantes.

TGCV estudia la estructura de esas transformaciones accesibles y cómo se modifica.

En su formulación actual, el núcleo ontológico mínimo es el estado del sistema, representado por **S**. La estructura de transformaciones accesibles, **T_acc**, es una representación analítica derivada de ese estado y de las condiciones pertinentes; no se postula como una entidad ontológica independiente.

Una transformación candidata se considera accesible cuando satisface un criterio de admisibilidad definido para el sistema y las condiciones relevantes. Ese criterio debe poder especificarse sin recurrir al resultado posterior para decidir retrospectivamente si la transformación era accesible.

Los cambios en T_acc pueden adoptar distintas formas:

- **Expansión:** algunas transformaciones pasan a estar al alcance.
- **Contracción:** algunas dejan de estarlo.
- **Reconfiguración:** cambia la composición o relación entre las transformaciones accesibles.
- **Sustitución:** unas posibilidades son reemplazadas por otras.

Por tanto, el fenómeno investigado no equivale simplemente a crecimiento, adaptación o aumento de capacidades. El espacio de transformaciones puede cambiar en distintas direcciones.

## 3. De la accesibilidad a las trayectorias y los resultados

La investigación examina cómo una modificación de las transformaciones accesibles puede relacionarse con cambios en los estados que el sistema puede alcanzar y en sus trayectorias posteriores.

La arquitectura analítica de referencia es:

`mecanismo → (S,C) → (S',C') → ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

Aquí, **C** representa el contexto y las condiciones relevantes del sistema en el momento inicial: por ejemplo, su entorno operativo, organizativo o institucional. **C'** representa ese contexto y esas condiciones en el momento posterior, después de la transición considerada. La prima no designa otro tipo de contexto: señala que las condiciones pueden haber cambiado. Las restricciones, los recursos y los criterios de admisibilidad se especifican además en el análisis de accesibilidad.

Esta secuencia organiza preguntas y niveles de análisis; no representa una cadena causal completa ya demostrada.

- **Accesibilidad y T_acc:** qué transformaciones satisfacen las condiciones definidas.
- **ΔT_acc:** cómo cambia la estructura de transformaciones accesibles.
- **Reach:** qué estados o configuraciones pueden alcanzarse bajo una semántica de transición especificada.
- **Trajectory:** cómo evoluciona el sistema a través de estados y transiciones a lo largo del tiempo.
- **Outcome:** qué resultado se observa.
- **Value:** cómo se evalúa ese resultado según un modelo de valoración explícito y dependiente del contexto.

Que una transformación sea accesible no significa que vaya a ejecutarse. Que se ejecute no garantiza un resultado favorable. Y un resultado no constituye por sí mismo una medida de valor.

## 4. Las preguntas que guían la investigación

El programa se organiza alrededor de seis preguntas principales:

1. **Estructura e identificabilidad.** ¿Qué representación mínima permite distinguir el sistema, las transformaciones candidatas, su accesibilidad y los cambios en esa accesibilidad sin circularidad ni redundancia conceptual injustificada?
2. **Dinámica.** ¿En qué condiciones puede identificarse un cambio en T_acc independientemente del resultado observado y distinguirse de cambios en el estado, Reach o Trajectory?
3. **Traducción entre dominios.** ¿Puede aplicarse una arquitectura analítica común a dominios heterogéneos preservando sus diferencias semánticas, sin limitarse a renombrar conceptos existentes?
4. **Reach y Trajectory.** ¿En qué condiciones los cambios de accesibilidad se relacionan con diferencias en los estados alcanzables o en las trayectorias posteriores?
5. **Outcome y Value.** ¿Qué condiciones y evidencias adicionales permitirían establecer una relación defendible con los resultados y el valor, sin confundir esos niveles?
6. **Límites.** ¿En qué dominios o condiciones fallan la identificabilidad, la traducción o las relaciones entre las distintas capas?

Estas preguntas admiten respuestas positivas, parciales o negativas. Delimitar dónde una representación no funciona también es un resultado relevante.

## 5. Cómo se investiga

TGCV combina formalización conceptual, reconstrucción analítica, pruebas computacionales y estudios delimitados en dominios concretos. Cada diseño debe precisar qué sistema y unidad analiza, qué transformaciones considera, qué regla determina su accesibilidad y qué condiciones son relevantes en el momento de decisión.

Cuando se estudian consecuencias posteriores, Reach, Trajectory y Outcome se definen y analizan por separado. La valoración se incorpora únicamente cuando existe un modelo de Value explícito e independiente.

La investigación compara sus representaciones con modelos y explicaciones alternativas, declara los supuestos necesarios y conserva los resultados negativos o inconclusos. La enumeración exhaustiva de todas las transformaciones posibles no es un requisito universal: el alcance operativo depende de cada pregunta y de las condiciones que puedan reconstruirse de forma independiente.

Las pruebas sintéticas permiten examinar propiedades bajo condiciones controladas; no equivalen por sí mismas a validación empírica en sistemas reales. Del mismo modo, una reconstrucción o un demostrador técnico no demuestra automáticamente causalidad, utilidad o creación de valor.

## 6. Qué indica la evidencia hasta ahora

La investigación ha producido resultados de distintos tipos y alcances. No todos responden a la misma pregunta ni permiten el mismo tipo de conclusión. La evidencia disponible debe entenderse como parcial y específica de los sistemas, datos, métodos y condiciones examinados; no constituye una validación general de TGCV.

Entre las líneas de evidencia que pueden explicarse al público se encuentran:

- [**Cambios en las posibilidades de transformación de un ecosistema de software.**](https://github.com/jcarmonabastida-pixel/TGCV/blob/strategy/tgcv-web-master/06_WEB/TGCV_WEB_EVIDENCE_SOFTWARE_ECOSYSTEM_v0.1.md) Un análisis longitudinal de sus componentes y dependencias identifica persistencia, expansión, contracción y reconfiguración de las transformaciones que resultan accesibles bajo una definición operacional explícita. Describe cambios estructurales en ese ecosistema; no demuestra que todas esas transformaciones se ejecutaran ni que produjeran valor.
- **Relación entre accesibilidad y estados alcanzables.** Un segundo análisis compara los cambios en las transformaciones accesibles con los estados que podrían alcanzarse bajo reglas de transición delimitadas. Encuentra situaciones en las que ambas dimensiones cambian de forma distinta. El resultado depende de la semántica de alcance utilizada y no equivale a demostrar ejecución real.
- **Reconstrucción y comparación entre dominios.** Pruebas metodológicas y experimentos sintéticos examinan si las distinciones entre estado, transformaciones candidatas, accesibilidad y consecuencias pueden reconstruirse en sistemas diferentes. Sus resultados son acotados a los casos y diseños estudiados; no demuestran validez transversal completa ni superioridad frente a todos los modelos existentes.
- **Accesibilidad y evolución posterior.** Un estudio empírico delimitado aporta apoyo a la hipótesis de que las condiciones de accesibilidad pueden relacionarse con la trayectoria posterior de un sistema. La conclusión está restringida a la población, las medidas y el diseño de ese estudio; no demuestra una relación universal ni permite inferir por sí sola creación de valor.
- **Límites de identificación.** Otros análisis muestran que, cuando no se conocen suficientemente las condiciones relevantes en el momento de decisión, puede no ser posible determinar si una transformación era realmente accesible. Reconocer esa indeterminación es parte del método, no un resultado que deba ocultarse.

La investigación también ha examinado métodos de razonamiento y selección de transformaciones. Esos trabajos no justifican afirmar que exista una capacidad general validada de Transformational Intelligence.

**La relación entre los cambios en las transformaciones accesibles, los resultados y el valor sigue siendo una cuestión abierta.** Ampliar lo que un sistema puede hacer no garantiza que lo haga, que obtenga un resultado favorable ni que ese resultado tenga valor.

Las descripciones detalladas de cada línea de evidencia deberán estar disponibles mediante enlaces específicos desde esta sección. Cada ficha explicará la pregunta examinada, el sistema y los datos utilizados, el método, el resultado, su alcance, sus limitaciones y los materiales de respaldo que puedan hacerse públicos. Los identificadores técnicos y las referencias internas de seguimiento no se mostrarán como si fueran nombres significativos para el visitante.

## 7. Qué sigue abierto

TGCV no presupone de antemano que su arquitectura sea aplicable a cualquier sistema. Permanecen abiertas, entre otras, las siguientes cuestiones:

- cómo identificar T_acc de forma robusta y no circular en distintos dominios;
- qué información analítica aporta que no esté ya representada por modelos existentes;
- cuándo los cambios en T_acc se relacionan con Reach y Trajectory, y cuándo no;
- qué diseños permiten atribuir causalmente consecuencias a cambios de accesibilidad;
- qué evidencia y qué modelo independiente serían necesarios para conectar esos cambios con Outcome y Value;
- dónde falla la traducción entre dominios;
- hasta qué punto puede operacionalizarse y validarse Transformational Intelligence como capacidad.

Un resultado negativo, una limitación de identificación o una frontera de aplicabilidad pueden modificar sustancialmente el alcance del programa. La investigación debe poder reconocerlos sin redefinir retrospectivamente sus criterios.

## 8. Un programa en desarrollo

TGCV conecta investigación conceptual y metodológica con ingeniería de sistemas, experimentación computacional y exploración de aplicaciones. Estas conexiones permiten formular nuevas preguntas y construir entornos de prueba; no convierten una posibilidad de aplicación en un resultado demostrado.

El programa continúa desarrollando y contrastando su arquitectura. Su contribución, alcance y límites deben juzgarse a partir de definiciones explícitas, evidencia reproducible y comparación crítica con alternativas.

**Investigar cómo cambian las posibilidades de transformación exige estudiar tanto lo que llega a ser posible como aquello que permanece fuera de alcance.**

---

# ENGLISH

## 1. TGCV: a programme investigating how systems' transformation possibilities change

**TGCV — Generative Transformations and Value Construction**

*A programme of applied research and innovation exploring how expanding the transformations available to systems may contribute to value construction.*

TGCV investigates how a system's conditions determine which transformations are accessible to it, how that structure of possibilities changes, and under what conditions such changes may relate to what the system can reach and the trajectories it can follow.

The question does not assume that expanding possibilities necessarily produces better outcomes. The research also examines contraction, loss, reconfiguration and cases in which no useful relationship can be established.

TGCV is an integrative, falsifiable research programme—not a consolidated theory or a universal explanation of all systems.

## 2. What does TGCV investigate?

A system can be described by its state or configuration at a given time. But knowing that state is not enough to determine which changes it can make. The transformations available to it also depend on relevant context, constraints, resources and other conditions.

TGCV studies the structure of those accessible transformations and how it changes.

In the current formulation, the minimal ontological Core is the system's state, denoted by **S**. The structure of accessible transformations, **T_acc**, is an analytical representation derived from that state and relevant conditions; it is not posited as an independent ontological entity.

A candidate transformation is considered accessible when it satisfies an admissibility criterion defined for the system and relevant conditions. That criterion must be specified without using the subsequent outcome to decide retrospectively whether the transformation was accessible.

Changes in T_acc may take different forms:

- **Expansion:** some transformations become accessible.
- **Contraction:** some cease to be accessible.
- **Reconfiguration:** the composition or relationships among accessible transformations change.
- **Substitution:** some possibilities are replaced by others.

The phenomenon under investigation is therefore not simply growth, adaptation or increased capability. The transformation space can change in different directions.

## 3. From accessibility to trajectories and outcomes

The research examines how a modification in accessible transformations may relate to changes in the states a system can reach and in its subsequent trajectories.

The reference analytical architecture is:

`mechanism → (S,C) → (S',C') → ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`

Here, **C** denotes the system's relevant context and conditions at the initial point—for example, its operating, organisational or institutional environment. **C'** denotes that context and those conditions at the later point, after the transition under study. The prime does not indicate a different kind of context; it marks that the conditions may have changed. Constraints, resources and admissibility criteria are also specified separately in the accessibility analysis.

This sequence organises questions and analytical layers; it is not a fully established causal chain.

- **Accessibility and T_acc:** which transformations satisfy the specified conditions.
- **ΔT_acc:** how the structure of accessible transformations changes.
- **Reach:** which states or configurations can be reached under a specified transition semantics.
- **Trajectory:** how the system develops through states and transitions over time.
- **Outcome:** the result that is observed.
- **Value:** how that result is evaluated under an explicit, context-dependent value model.

An accessible transformation is not necessarily executed. Execution does not guarantee a favourable outcome. And an outcome is not, by itself, a measure of value.

## 4. The questions guiding the research

The programme is organised around six main questions:

1. **Structure and identifiability.** What minimal representation can distinguish the system, candidate transformations, their accessibility and changes in accessibility without circularity or unjustified conceptual redundancy?
2. **Dynamics.** Under what conditions can a change in T_acc be identified independently of the observed outcome and distinguished from changes in state, Reach or Trajectory?
3. **Cross-domain translation.** Can a common analytical architecture be applied across heterogeneous domains while preserving their semantic differences, rather than merely renaming existing concepts?
4. **Reach and Trajectory.** Under what conditions are accessibility changes related to differences in reachable states or subsequent trajectories?
5. **Outcome and Value.** What additional conditions and evidence would be required to establish a defensible relationship with outcomes and value without conflating these layers?
6. **Limits.** In which domains or conditions do identifiability, translation or relationships among the different layers fail?

These questions allow positive, partial or negative answers. Establishing where a representation does not work is also a relevant research result.

## 5. How the programme investigates these questions

TGCV combines conceptual formalisation, analytical reconstruction, computational tests and bounded studies in specific domains. Each design must specify the system and unit being analysed, the transformations under consideration, the rule determining their accessibility, and the conditions relevant at decision time.

When downstream consequences are examined, Reach, Trajectory and Outcome are defined and analysed separately. Value is introduced only where an explicit and independent value model is available.

The research compares its representations with alternative models and explanations, states the assumptions required, and preserves negative or inconclusive results. Exhaustive enumeration of every possible transformation is not a universal requirement: operational scope depends on the question and on the conditions that can be independently reconstructed.

Synthetic tests can examine properties under controlled conditions; they do not, by themselves, amount to empirical validation in real systems. Likewise, a technical reconstruction or demonstrator does not automatically demonstrate causality, utility or value creation.

## 6. What does the evidence indicate so far?

The research has produced results of different kinds and with different scopes. They do not all address the same question or support the same type of conclusion. The available evidence should be understood as partial and specific to the systems, data, methods and conditions examined; it does not amount to general validation of TGCV.

The evidence strands that can be explained to a public audience include:

- [**Changes in the transformation possibilities of a software ecosystem.**](https://github.com/jcarmonabastida-pixel/TGCV/blob/strategy/tgcv-web-master/06_WEB/TGCV_WEB_EVIDENCE_SOFTWARE_ECOSYSTEM_v0.1.md) A longitudinal analysis of its components and dependencies identifies persistence, expansion, contraction and reconfiguration in the transformations accessible under an explicit operational definition. It describes structural changes in that ecosystem; it does not show that all such transformations were executed or generated value.
- **The relationship between accessibility and reachable states.** A second analysis compares changes in accessible transformations with the states that could be reached under bounded transition rules. It finds cases in which the two dimensions change differently. The result depends on the reachability semantics used and is not equivalent to demonstrating actual execution.
- **Reconstruction and comparison across domains.** Methodological tests and synthetic experiments examine whether distinctions among state, candidate transformations, accessibility and consequences can be reconstructed in different systems. Their results are bounded to the cases and designs studied; they do not demonstrate complete cross-domain validity or superiority over all existing models.
- **Accessibility and subsequent development.** A bounded empirical study provides support for the hypothesis that accessibility conditions may be related to a system's subsequent trajectory. The conclusion is limited to that study's population, measures and design; it does not demonstrate a universal relationship or, by itself, imply value creation.
- **Limits of identification.** Other analyses show that when relevant conditions at the decision point are not sufficiently known, it may be impossible to determine whether a transformation was genuinely accessible. Recognising such indeterminacy is part of the method, not a result to be concealed.

The research has also examined methods for reasoning about and selecting transformations. Those studies do not justify claiming that a generally validated Transformational Intelligence capability already exists.

**The relationship between changes in accessible transformations, outcomes and value remains an open question.** Expanding what a system can do does not guarantee that it will do it, achieve a favourable outcome or produce something valuable.

Detailed descriptions of each evidence strand should be available through dedicated links from this section. Each evidence page will explain the research question, system and data, method, result, scope, limitations and supporting materials that can be made public. Technical identifiers and internal tracking references should not be displayed as if they were meaningful names for visitors.

## 7. What remains open?

TGCV does not assume in advance that its architecture applies to every system. Open questions include:

- how to identify T_acc robustly and non-circularly across domains;
- what analytical information it adds beyond existing models;
- when changes in T_acc relate to Reach and Trajectory, and when they do not;
- which designs allow causal attribution of consequences to accessibility changes;
- what evidence and independent model would be required to connect those changes with Outcome and Value;
- where cross-domain translation fails;
- to what extent Transformational Intelligence can be operationalised and validated as a capability.

A negative result, an identification limitation or an applicability boundary may materially change the programme's scope. The research must be able to recognise such findings without retrospectively redefining its criteria.

## 8. A programme in development

TGCV connects conceptual and methodological research with systems engineering, computational experimentation and application exploration. These connections make it possible to formulate new questions and build test environments; they do not turn an application possibility into a demonstrated result.

The programme continues to develop and test its architecture. Its contribution, scope and limitations must be assessed through explicit definitions, reproducible evidence and critical comparison with alternatives.

**Investigating how transformation possibilities change means studying both what becomes possible and what remains out of reach.**

---

## Editorial controls before publication

1. Reconcile this copy with the final approved Research Experience.
2. Recheck all evidence claims against the current RMA, Evidence→Claim Matrix, traceability and material evidence records; STATUS.md is dated 2026-11-06 and is not a live evidence feed.
3. Confirm publication permission and stable public destinations for every linked scientific asset.
4. Decide whether the public page should expose numerical evidence summaries or retain qualitative, bounded descriptions.
5. Run a terminology and comprehension review in Spanish and English.
6. Preserve all negative, conditional and open findings; do not convert programme activity into scientific achievement.
