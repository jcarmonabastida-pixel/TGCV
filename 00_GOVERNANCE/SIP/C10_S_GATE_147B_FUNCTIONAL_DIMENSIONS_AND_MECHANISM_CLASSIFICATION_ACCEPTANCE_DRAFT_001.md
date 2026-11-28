# C10-S — Gate 147-B: aceptación de dimensiones funcionales y clasificación de mecanismos B1

**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft  
**Estado:** R147-B1_ACCEPTED / R147-B2_ACCEPTED / R147-B3_ACCEPTED / R147-B4_ACCEPTED / THREE_FUNCTIONAL_DIMENSIONS_ACCEPTED / RELATION_FORMALIZATION_OPEN / MECHANISM_COVERAGE_AUDIT_OPEN / NO_SCHEMA_CHANGE / NO_CODE_CHANGE / NO_TESTS / NO_EXECUTION.

## 1. Acto de aceptación

Se registra la aceptación expresa del usuario de R147-B1…R147-B4 y de la separación conceptual en tres dimensiones funcionales. La aceptación es semántica y lógica para el DGP sintético. No crea DEC-C10, no modifica decisiones DEC existentes, no altera el DGP original ni promueve contenido a `main`.

## 2. Reglas aceptadas

### R147-B1 — EventHistory representa verdad funcional

EventHistory representa estados y cambios funcionales verdaderos, no un inventario indiscriminado de acontecimientos técnicos. Los eventos de proceso y las observaciones se mantienen en sus canales propios.

### R147-B2 — inclusión de mecanismos runtime según efecto funcional

Los mecanismos runtime se reflejan en la historia truth cuando modifican efectivamente la disponibilidad operativa de B1. La mera presencia de una señal, log, fallo técnico o antecedente no basta para crear una transición truth.

### R147-B3 — no duplicación por antecedentes múltiples

Varios antecedentes que concurren en un mismo cambio funcional no generan transiciones truth duplicadas. Se aplica R144-A para simultaneidad atómica y suborden explícito cuando existan estados intermedios funcionalmente relevantes. La atribución causal/provenance de los antecedentes no se pierde por consolidar el cambio funcional.

### R147-B4 — ciclo discreto de solicitud separado

Las solicitudes y sus etapas constituyen un ciclo discreto separado. La ausencia de solicitud no es fallo ni incumplimiento. Solo una consecuencia funcional real sobre la admisión modifica el estado truth correspondiente; intento, recepción, admisión, rechazo, procesamiento y respuesta no se colapsan en un único evento.

## 3. Tres dimensiones funcionales conceptualmente diferenciadas

Se aceptan como dimensiones distintas, sin fijar todavía su relación formal:

1. **Configuración declarativa:** ENABLED/PROFILE.
2. **Disponibilidad operativa efectiva:** condiciones funcionales runtime relevantes (proceso/módulo, listener/socket/superficie de ingreso, dependencias y capacidad/recursos).
3. **Capacidad efectiva de admisión B1:** resultado funcional respecto de la admisión de solicitudes bajo las condiciones y reglas aplicables.

No se presume que ENABLED=true garantice disponibilidad operativa ni capacidad efectiva de admisión. Tampoco se presume que cualquier indisponibilidad runtime equivalga por sí sola a una transición de admisión. La relación determinista, sus condiciones necesarias/suficientes, precedencia e interacción quedan abiertas para formalización posterior contra §§49–50 y el DGP vigente.

## 4. Separación truth / observed_evidence / evaluation

- **Truth:** estados y cambios funcionales verdaderos en las dimensiones pertinentes.
- **Observed_evidence:** señales, logs, métricas, resultados de solicitudes y registros de proceso; pueden ser parciales, tardíos o imperfectos.
- **Evaluation:** derivaciones y adjudicaciones del Evaluator, tras el sellado del Analyzer, mediante reglas versionadas.

La detectabilidad S3 no define ni limita la verdad funcional. La falta de observación no convierte automáticamente un estado truth en UNKNOWN. Los defectos de historia/harness se mantienen como defectos de generación o representación, conforme a R144-A y R146-D.

## 5. Límites

Esta aceptación no cierra la cobertura exhaustiva del catálogo de mecanismos ni clasifica definitivamente cada señal runtime como estado, condición antecedente o evidencia. Tampoco define estados físicos, schema, campos, IDs, serialización, algoritmo de adjudicación, reloj, rejilla, unidad temporal, soporte numérico, T*, Δ, K, calibración S3, fixtures, código, pruebas, generación, simulación ni ejecución científica.

No se crean DEC-C10 ni se modifican decisiones existentes. R144-B y §51 permanecen abiertos.

## 6. Siguiente trabajo

Continuar Gate 147 mediante una matriz de cobertura de mecanismos B1 que identifique por mecanismo: dimensión afectada, condición funcional, cambio truth resultante (si lo hay), antecedentes causales, evidencia observacional, posibilidad de concurrencia/duplicación y lagunas del contrato. Resolver la relación formal entre las tres dimensiones sin introducir supuestos no presentes en §§49–50.

`scientific_execution=false`  
`execution_authorized=false`  
`implementation_authorized=false`
