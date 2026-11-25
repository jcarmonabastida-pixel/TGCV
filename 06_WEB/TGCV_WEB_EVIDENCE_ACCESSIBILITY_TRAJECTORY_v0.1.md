# TGCV — Evidence Brief: From Accessibility Changes to Subsequent Trajectories v0.1

**Identifier:** TGCV-WEB-EVIDENCE-TRAJECTORY-001  
**Version:** 0.1  
**Date:** 2026-11-25  
**Status:** EDITORIAL WORKING DRAFT — SCIENTIFIC CLASSIFICATION RECONCILIATION REQUIRED BEFORE PUBLICATION  
**Branch:** strategy/tgcv-web-master

# ESPAÑOL

## La pregunta

¿Qué evidencia existe de que un cambio en las transformaciones que están al alcance de un sistema pueda ir seguido de cambios en su trayectoria?

Esta pregunta va más allá de comprobar que las posibilidades accesibles cambian. Requiere observar o reconstruir qué transformaciones se realizan después, qué estados atraviesa el sistema y durante qué periodo. También exige distinguir una asociación temporal de una relación causal.

La investigación disponible aporta tres tipos de evidencia complementarios, con alcances diferentes: una reconstrucción temporal en un sistema de software auto-adaptativo, un experimento de campo sobre expansión estructural del acceso financiero y una evaluación de los límites de los datos de otro ecosistema de software.

## 1. Un sistema de software que cambia durante su funcionamiento

En un sistema de gestión de recursos informáticos, la evidencia de una ejecución ya realizada permitió reconstruir varios momentos en los que cambiaba el conjunto de transformaciones accesibles. Por ejemplo, añadir un servidor podía estar disponible cuando el sistema operaba por debajo de su límite, mientras que eliminar un servidor dejaba de estar disponible al alcanzar el mínimo permitido.

Esos cambios se pudieron ordenar temporalmente junto con las transformaciones seleccionadas y las transiciones de estado que efectivamente se registraron. La reconstrucción siguió una secuencia delimitada: cambios en las posibilidades accesibles, transformaciones realizadas y estados posteriores.

### Qué aporta

Este caso muestra que, en un sistema auto-adaptativo concreto, es posible reconstruir una asociación temporal y estructural entre cambios en las transformaciones accesibles y una trayectoria posterior de acciones y estados.

La evidencia procede de una ejecución existente y de una reconstrucción analítica de sus registros. No se realizó una nueva simulación para obtener este resultado.

### Qué no demuestra

No demuestra que los cambios en accesibilidad causaran las decisiones posteriores, que la misma relación se dé en otros sistemas, que la trayectoria fuera mejor que otra alternativa, ni que se generara valor. Es una reconstrucción acotada de asociación observada, no una identificación causal.

## 2. Una intervención estructural de acceso financiero y sus consecuencias posteriores

Un experimento de campo en zonas rurales de India evaluó la apertura temprana de sucursales de un sistema de servicios financieros. La asignación de las zonas que recibirían primero una sucursal se realizó de forma aleatoria entre áreas comparables.

La intervención amplió estructuralmente el acceso a servicios financieros formales: préstamos, ahorro, seguros y asesoramiento financiero a través de sucursales locales. Esta ampliación se define a partir de la intervención y de la infraestructura ofrecida, no a partir de que los hogares decidieran utilizar los productos.

El estudio recogió información antes de la intervención y entre 18 y 24 meses después. Los resultados posteriores incluyeron dimensiones como actividad económica, ocupación, ingresos, endeudamiento y bienestar de los hogares.

### Qué aporta

Este diseño ofrece evidencia causal acotada de las consecuencias de una intervención estructural que amplía el acceso financiero. La asignación aleatoria permite estimar el efecto de ofrecer esa expansión de infraestructura y servicios sobre resultados posteriores, dentro de la población y el periodo estudiados.

La investigación TGCV ha reconstruido la intervención como un cambio estructural en las posibilidades financieras disponibles y ha auditado la correspondencia de las variables longitudinales de los archivos públicos. La auditoría técnica cubrió 74 de 74 archivos de datos previstos, sin archivos requeridos ausentes.

### Qué requiere cautela

El efecto causal identificado corresponde a la intervención estructural asignada como conjunto. No debe confundirse automáticamente con una estimación aislada de un efecto mediado por cada transformación accesible, ni con una demostración de que todos los componentes de la intervención operen exclusivamente a través de la ampliación de posibilidades.

La clasificación científica interna del grado de identificación y de los posibles canales residuales requiere reconciliación documental antes de publicar una etiqueta más fuerte. Por ello, esta ficha presenta el caso como evidencia causal acotada de una intervención estructural de acceso, sin afirmar que se haya aislado un efecto causal universal o independiente de cada componente de T_acc.

## 3. Por qué no todos los datos permiten reconstruir trayectorias

Un análisis de otro ecosistema de software, construido a partir de versiones y dependencias declaradas, permitió estudiar cambios en las transformaciones accesibles. Sin embargo, sus datos no contenían registros explícitos de resolución efectiva de dependencias, secuencias de ejecución ni transiciones de estado en tiempo de ejecución.

Por tanto, esos datos permiten estudiar posibilidades estructurales y algunas formas de alcance potencial bajo reglas delimitadas, pero no reconstruir directamente una trayectoria ejecutada.

Esta limitación es importante: una secuencia de estados potenciales no equivale a una secuencia de acciones que el sistema haya realizado.

## 4. Qué podemos concluir al considerar conjuntamente la evidencia

Los casos permiten distinguir tres niveles:

1. **Reconstrucción temporal:** en un sistema auto-adaptativo concreto, los cambios en las posibilidades accesibles pueden ponerse en relación temporal con transformaciones realizadas y estados posteriores.
2. **Evidencia causal acotada:** un experimento aleatorizado puede identificar las consecuencias posteriores de una intervención que implementa una expansión estructural de acceso, dentro de los límites de esa intervención y población.
3. **Límite de observación:** algunos conjuntos de datos permiten reconstruir posibilidades, pero no contienen la información necesaria para observar trayectorias efectivamente ejecutadas.

La evidencia disponible respalda que la relación entre accesibilidad y trayectoria puede investigarse empíricamente y que existen casos acotados de reconstrucción temporal y de intervención causal. No demuestra una ley universal según la cual todo cambio en las posibilidades accesibles produzca una trayectoria distinta o mejor.

## 5. Qué sigue abierto

Quedan abiertas preguntas importantes:

- ¿En qué condiciones un cambio en las transformaciones accesibles modifica las trayectorias posibles o realizadas?
- ¿Cuándo una posibilidad adicional es redundante y cuándo abre un camino que antes no existía?
- ¿Qué mecanismos determinan qué transformación se selecciona y realiza?
- ¿Qué parte de los efectos posteriores corresponde a la expansión estructural de posibilidades y qué parte a otros componentes de una intervención?
- ¿Cuándo los cambios de trayectoria conducen a resultados y cuándo esos resultados pueden considerarse valiosos?
- ¿Hasta qué punto se reproducen estas relaciones en otros dominios?

Estas preguntas requieren diseños que mantengan separadas accesibilidad, selección, ejecución, trayectoria, resultado y valor.

## Interpretación

La evidencia no permite afirmar que TGCV haya demostrado una relación universal entre accesibilidad y trayectoria. Sí permite mostrar cómo esa relación se reconstruye en un sistema concreto, cómo puede estudiarse mediante una intervención estructural aleatorizada y por qué los límites de los datos importan.

El avance científico consiste tanto en los vínculos que se han podido documentar como en las condiciones bajo las cuales todavía no es posible establecerlos.

---

# ENGLISH

## The question

What evidence is available that a change in the transformations accessible to a system may be followed by changes in its trajectory?

This goes beyond showing that accessible possibilities change. It requires observing or reconstructing which transformations are subsequently realised, which states the system moves through and over what period. It also requires distinguishing temporal association from a causal relationship.

The available research provides three complementary forms of evidence with different scopes: a temporal reconstruction in a self-adaptive software system, a field experiment on the structural expansion of financial access, and an assessment of the limits of data from another software ecosystem.

## 1. A software system changing during operation

In a computing-resource management system, evidence from an existing execution made it possible to reconstruct several moments when the set of accessible transformations changed. For example, adding a server could be available while the system operated below its limit, whereas removing a server ceased to be available when the permitted minimum was reached.

These changes could be temporally ordered alongside selected transformations and the state transitions actually recorded. The reconstruction followed a bounded sequence: changes in accessible possibilities, realised transformations and subsequent states.

### What this contributes

This case shows that, in one specific self-adaptive system, a temporal and structural association can be reconstructed between changes in accessible transformations and a subsequent trajectory of actions and states.

The evidence comes from an existing execution and an analytical reconstruction of its records. No new simulation was run to obtain this result.

### What it does not demonstrate

It does not demonstrate that accessibility changes caused subsequent decisions, that the same relationship holds in other systems, that the trajectory was better than an alternative, or that value was created. It is a bounded reconstruction of observed association, not causal identification.

## 2. A structural financial-access intervention and its subsequent consequences

A field experiment in rural India evaluated the early opening of branches belonging to a financial-services system. The areas receiving a branch first were randomly assigned among comparable service areas.

The intervention structurally expanded access to formal financial services: loans, savings, insurance and financial advice through local branches. This expansion is defined from the intervention and the infrastructure provided, not from whether households chose to use the products.

The study collected information before the intervention and between 18 and 24 months afterwards. Subsequent measures included economic activity, occupation, income, borrowing and household wellbeing.

### What this contributes

The design provides bounded causal evidence about the consequences of a structural intervention expanding financial access. Random assignment makes it possible to estimate the effect of offering that infrastructure and service expansion on subsequent outcomes, within the population and period studied.

TGCV research has reconstructed the intervention as a structural change in available financial possibilities and audited the mapping of longitudinal variables in the public files. The technical audit covered all 74 of the 74 expected data files, with no required files missing.

### Why caution is needed

The identified causal effect concerns the assigned structural intervention as a whole. It should not automatically be treated as an isolated estimate of an effect mediated by each accessible transformation, or as proof that every intervention component operates exclusively through the expansion of possibilities.

The internal scientific classification of the identification strength and possible residual pathways requires documentary reconciliation before a stronger label is published. This brief therefore presents the case as bounded causal evidence about a structural access intervention, without claiming a universal causal effect or an independently isolated effect for every component of T_acc.

## 3. Why not all datasets allow trajectories to be reconstructed

An analysis of another software ecosystem, based on package versions and declared dependencies, made it possible to study changes in accessible transformations. However, its data did not contain explicit records of actual dependency resolution, execution sequences or runtime state transitions.

Those data can therefore support the study of structural possibilities and certain forms of bounded potential reachability, but they cannot directly reconstruct an executed trajectory.

This limitation matters: a sequence of potential states is not equivalent to a sequence of actions the system actually performed.

## 4. What can be concluded across the evidence

The cases distinguish three levels:

1. **Temporal reconstruction:** in one specific self-adaptive system, changes in accessible possibilities can be related temporally to realised transformations and subsequent states.
2. **Bounded causal evidence:** a randomised experiment can identify subsequent consequences of an intervention that implements a structural expansion of access, within the limits of that intervention and population.
3. **Observation limits:** some datasets allow possibilities to be reconstructed but do not contain the information needed to observe executed trajectories.

The available evidence supports the empirical investigation of the accessibility–trajectory relationship and provides bounded cases of temporal reconstruction and causal intervention. It does not demonstrate a universal law whereby every change in accessible possibilities produces a different or better trajectory.

## 5. What remains open

Important questions remain:

- Under what conditions does a change in accessible transformations alter possible or realised trajectories?
- When is an additional possibility redundant, and when does it open a path that did not previously exist?
- What mechanisms determine which transformation is selected and realised?
- Which part of subsequent effects is attributable to structural expansion of possibilities, and which part to other components of an intervention?
- When do trajectory changes lead to outcomes, and when can those outcomes be considered valuable?
- To what extent do these relationships replicate across other domains?

These questions require designs that keep accessibility, selection, execution, trajectory, outcome and value distinct.

## Interpretation

The evidence does not allow the claim that TGCV has demonstrated a universal relationship between accessibility and trajectory. It does show how that relationship can be reconstructed in a specific system, how it can be studied through a randomised structural intervention, and why data limitations matter.

Scientific progress consists both in the links that have been documented and in identifying the conditions under which those links cannot yet be established.

---

## Editorial source and publication checks — not visitor-facing

Before publication, reconcile the conflicting historical classifications of the KGFS candidate's identification status and residual-pathway assessment. The adopted structural-accessibility intervention extension classifies the candidate as bounded/assumption-explicit, while a separate claim-level consolidation record describes an identified contribution. Do not publish stronger mediation claims or internal classification labels until the authoritative scientific record is reconciled. Confirm public citation destinations for the SWIM execution evidence, KGFS study/archive and Rust dataset feasibility review. This brief intentionally avoids internal experiment and governance identifiers in visitor-facing prose.
