# TGCV — Evidence Brief: Controlled Testing and Cross-Domain Reconstruction v0.1

**Identifier:** TGCV-WEB-EVIDENCE-METHODS-001  
**Version:** 0.1  
**Date:** 2026-11-25  
**Status:** EDITORIAL WORKING DRAFT — NOT APPROVED FOR PUBLICATION  
**Branch:** `strategy/tgcv-web-master`

# ESPAÑOL

## Qué pregunta aborda esta línea de investigación

¿Puede una arquitectura analítica describir cambios en las transformaciones accesibles en sistemas distintos, respetando la semántica propia de cada dominio? Y, antes de intentar aplicarla ampliamente, ¿pueden las pruebas controladas revelar qué información deja fuera una representación del sistema?

La investigación contiene aquí dos trabajos relacionados, pero diferentes: una prueba sintética controlada sobre suficiencia de representación y una comparación analítica secundaria entre dos dominios a partir de evidencias ya existentes. No deben confundirse ni presentarse como una validación general de TGCV.

## 1. Prueba controlada: cuándo una representación no basta

En una prueba sintética se construyeron dos casos con el mismo estado inicial, el mismo contexto, el mismo conjunto de transformaciones accesibles y las mismas reglas. Antes de realizar la transición, cada caso tenía asignada una condición de política distinta.

Aunque la información representada por el estado, el contexto y las transformaciones accesibles era idéntica en ambos casos, las realizaciones fueron diferentes:

- En un caso se realizó una transformación que llevó a un estado aceptado.
- En el otro se realizó una transformación distinta que llevó a un estado diferido.

La ejecución controlada, sus diez comprobaciones y la auditoría del resultado fueron satisfactorias, sin desviaciones registradas. El contraste muestra que, en esa construcción concreta, conocer únicamente el estado, el contexto y las transformaciones accesibles no bastaba para determinar qué trayectoria se realizaría. La variable de política examinada contenía información relevante para distinguir las dos realizaciones.

### Qué permite afirmar

La prueba aporta evidencia sintética controlada de una insuficiencia de la representación examinada bajo las condiciones definidas: dos casos iguales en estado, contexto, transformaciones accesibles y reglas pueden realizar trayectorias diferentes cuando difiere otra condición previa a la realización.

### Qué no permite afirmar

No demuestra que esa condición deba convertirse en un elemento universal del núcleo de TGCV, que la misma insuficiencia aparezca en todos los dominios, que el resultado sea empíricamente generalizable, ni que se produzca creación de valor o capacidad predictiva. Tampoco constituye evidencia sobre la hipótesis causal entre cambios en accesibilidad y valor en sistemas reales.

## 2. Comparación analítica entre dos dominios

Un segundo trabajo reutilizó evidencias previamente reconstruidas y auditadas de dos sistemas diferentes:

- un entorno de planificación y navegación en una cuadrícula;
- un modelo de sincronización de liderazgo especificado mediante un lenguaje formal de sistemas.

El propósito no fue afirmar que ambos sistemas tengan las mismas acciones o significados. Fue comprobar si una misma estructura de análisis puede describir, dentro de cada dominio y respetando sus reglas propias, el estado, las transformaciones accesibles, la transformación realizada, el estado sucesor y el cambio posterior en las transformaciones accesibles.

La comparación secundaria procesó 36 registros: 20 del primer dominio y 16 del segundo. No se registraron registros inválidos. Los identificadores de transformación se mantuvieron separados por dominio; no se trataron acciones de un sistema como equivalentes semánticos de acciones del otro. Tampoco se utilizaron resultados, rendimiento o valor para definir la accesibilidad.

### Qué mostró el análisis

En el entorno de planificación, los 20 registros presentaron incorporación y pérdida de transformaciones accesibles: hubo rotación completa de las opciones entre los estados comparados. El tamaño medio del conjunto accesible pasó de 4 a 3,8.

En el modelo de sincronización, los 16 registros examinados conservaron una única transformación accesible en los dos momentos comparados. En ese conjunto acotado no se observaron expansión, contracción ni rotación.

La comparación pudo calcular descriptores estructurales comunes —incorporaciones, pérdidas, persistencia y rotación— sin borrar las diferencias semánticas entre dominios. También pudo observar, en el conjunto combinado, casos en los que una transformación realizada iba seguida de una reconfiguración de las posibilidades posteriores.

Sin embargo, no se observó divergencia entre trayectorias en ninguno de los dos dominios. El análisis disponible contenía una trayectoria por dominio para esta comparación; por tanto, no permitía contrastar ramas alternativas ni demostrar que el método discrimine entre futuros posibles divergentes.

### Qué permite afirmar

Este trabajo aporta evidencia metodológica acotada de que una gramática analítica común puede aplicarse a registros ya disponibles de dos dominios heterogéneos para describir cambios estructurales en las transformaciones accesibles, manteniendo separadas sus identidades y semánticas nativas.

También muestra que la utilidad de esa gramática no está demostrada por igual para todas las preguntas: algunos descriptores fueron observables, mientras que la divergencia de trayectorias no pudo observarse en el material disponible.

### Qué no permite afirmar

La comparación no demuestra superioridad frente a las representaciones nativas, una medida universal de capacidad transformacional, utilidad práctica general, validez en otros dominios, inteligencia transformacional validada, predicción, causalidad ni creación de valor. Tampoco constituye un nuevo experimento científico sobre los sistemas originales: es un análisis secundario de evidencias congeladas y previamente auditadas.

## 3. Lectura conjunta y límites

Los dos trabajos responden a preguntas complementarias:

- La prueba controlada muestra que una representación puede ser insuficiente para determinar una realización, incluso cuando estado, contexto y transformaciones accesibles coinciden.
- La comparación entre dominios muestra que determinados descriptores de cambio transformacional pueden reconstruirse en sistemas distintos sin equiparar sus acciones nativas.

Ninguno demuestra por sí solo que la arquitectura completa de TGCV sea necesaria, suficiente o superior. La investigación debe continuar comparando sus representaciones con alternativas, delimitando las condiciones de aplicabilidad y examinando por separado las relaciones con trayectorias, resultados y valor.

La prueba sintética no sustituye a la evidencia empírica. La comparación entre dominios no equivale a una validación transversal general. La integridad de una ejecución o de un paquete analítico tampoco debe confundirse con la validez científica de todas las inferencias posibles.

---

# ENGLISH

## The research question

Can an analytical architecture describe changes in accessible transformations across different systems while preserving each domain's own semantics? And, before attempting broad application, can controlled tests reveal what information a system representation leaves out?

This line of work contains two related but distinct studies: a controlled synthetic test of representational sufficiency and a secondary analytical comparison across two domains using evidence that already existed. They must not be conflated or presented as general validation of TGCV.

## 1. Controlled test: when a representation is insufficient

A synthetic test constructed two cases with the same initial state, context, accessible-transformation set and rules. Before the transition, each case was assigned a different policy condition.

Although the information represented by state, context and accessible transformations was identical in both cases, the realised transitions differed:

- In one case, a transformation led to an accepted state.
- In the other, a different transformation led to a deferred state.

The controlled execution, its ten checks and the result audit passed, with no recorded deviations. Under this specific construction, the contrast shows that knowing only the state, context and accessible transformations was not enough to determine which trajectory would be realised. The policy variable examined contained information relevant to distinguishing the two realisations.

### What this supports

The test provides controlled synthetic evidence of representational insufficiency under the specified conditions: two cases equal in state, context, accessible transformations and rules can realise different trajectories when another pre-realisation condition differs.

### What this does not support

It does not show that this condition must become a universal element of the TGCV Core, that the same insufficiency occurs in every domain, or that the result generalises empirically. It does not establish value creation or predictive capability. Nor does it provide evidence for a causal hypothesis linking accessibility changes to value in real systems.

## 2. Analytical comparison across two domains

A second study reused previously reconstructed and audited evidence from two different systems:

- a grid-based planning and navigation environment;
- a leadership-synchronisation model specified in a formal systems language.

The purpose was not to claim that the two systems share the same actions or meanings. It was to test whether a common analytical structure could describe, within each domain and under its own rules, the state, accessible transformations, realised transformation, successor state and subsequent change in accessible transformations.

The secondary comparison processed 36 records: 20 from the first domain and 16 from the second. No invalid records were reported. Transformation identities remained separate by domain; actions from one system were not treated as semantically equivalent to actions from the other. Outcomes, performance and value were not used to define accessibility.

### What the analysis showed

In the planning environment, all 20 records showed both additions and losses of accessible transformations: the options turned over completely between the compared states. The mean size of the accessible set changed from 4 to 3.8.

In the synchronisation model, all 16 examined records retained a single accessible transformation at both compared points. No expansion, contraction or turnover was observed in this bounded set.

The comparison computed common structural descriptors—additions, losses, persistence and turnover—without erasing domain-specific semantics. Across the combined material, it could also identify cases in which a realised transformation was followed by a reconfiguration of subsequent possibilities.

However, trajectory divergence was not observed in either domain. The available analysis contained one trajectory per domain for this comparison; it therefore could not contrast alternative branches or demonstrate that the method discriminates between divergent possible futures.

### What this supports

This work provides bounded methodological evidence that a common analytical grammar can be applied to existing records from two heterogeneous domains to describe structural changes in accessible transformations while preserving their native identities and semantics.

It also shows that the usefulness of this grammar is not established equally for every question: some descriptors were observable, whereas trajectory divergence could not be observed in the available material.

### What this does not support

The comparison does not demonstrate superiority over native representations, a universal measure of transformational capability, general practical utility, validity in other domains, validated Transformational Intelligence, prediction, causality or value creation. Nor is it a new scientific experiment on the original systems: it is a secondary analysis of frozen, previously audited evidence.

## 3. Combined interpretation and limits

The two studies address complementary questions:

- The controlled test shows that a representation can be insufficient to determine a realisation, even when state, context and accessible transformations are identical.
- The cross-domain comparison shows that selected descriptors of transformational change can be reconstructed in different systems without equating their native actions.

Neither study alone demonstrates that the full TGCV architecture is necessary, sufficient or superior. Research must continue comparing its representations with alternatives, delimiting conditions of applicability and examining relationships with trajectories, outcomes and value separately.

The synthetic test does not replace empirical evidence. The cross-domain comparison is not general cross-domain validation. The integrity of an execution or analytical package must not be confused with the scientific validity of every possible inference.

---

## Editorial source and publication checks — not visitor-facing

Before publication, reconcile this brief with the current canonical claim matrix and research records. Confirm permission to publish descriptions of the two source systems and their evidence. Do not link restricted fixtures, raw execution outputs or internal governance records by default. The controlled synthetic test and the secondary cross-domain analysis must remain clearly distinguished in every summary.

