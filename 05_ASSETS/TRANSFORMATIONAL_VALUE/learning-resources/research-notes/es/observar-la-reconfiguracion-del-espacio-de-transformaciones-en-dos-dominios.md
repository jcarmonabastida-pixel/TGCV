---
content_id: TV-LR-001
language_pair_id: TV-LR-001
title: "Observar la reconfiguración del espacio de transformaciones en dos dominios"
language: es
content_type: research_note
status: draft
version: 0.2
created: 2026-11-26
updated: 2026-11-26
authors: []
reviewers: []
summary: "Nota de evidencia metodológica sobre la reconstrucción de cambios en espacios de transformaciones accesibles en dos dominios computacionales acotados."
part: null
chapter: null
parent_id: null
tags:
  - research-evidence
  - transformation-space
  - cross-domain-method
concepts:
  - TV-TERM-001
prerequisites: []
related:
  - TV-CH-03
references:
  - TV-REF-004
  - TV-REF-005
epistemic_status:
  - bounded_methodological_evidence
source_assets:
  - 00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_v1.47.md
  - 03_EXPERIMENTS/TR-131/execution/TR131_CROSS_DOMAIN_OPERATIONALISATION_UPDATE_001.md
  - 03_EXPERIMENTS/TR-131/execution/TR131_VISITALL_DYNAMIC_SPACE_SCIENTIFIC_EVALUATION_AUDIT_001.md
  - 03_EXPERIMENTS/TR-131/execution/TR131_PRISM_GATE_A_A1_A5_AUDIT_001.md
  - 03_EXPERIMENTS/TR-131/execution/TR131_PRISM_LEADER_SYNC_A6_RECONSTRUCTION_AUDIT_001.md
  - 03_EXPERIMENTS/TR-131/execution/TR131_PRISM_GATE_A_A7_DOMAIN_BOUNDARY_AUDIT_001.md
license: null
---

# Observar la reconfiguración del espacio de transformaciones en dos dominios

## Propósito

Esta nota resume un análisis metodológico acotado que examinó si una misma estructura analítica podía utilizarse para reconstruir la evolución de los espacios de transformaciones accesibles en dos dominios computacionales con semánticas diferentes.

La pregunta no era si esa representación era superior a las representaciones nativas de cada dominio, ni si los cambios observados producían valor. Se examinó si podían identificarse y relacionarse de forma consistente el estado, las transformaciones accesibles, la transformación realizada, el estado sucesor y el nuevo espacio accesible.

## Los dos dominios examinados

**Planificación de movimientos en una cuadrícula.** El primer dominio procede de un problema de planificación de visita de una cuadrícula publicado en el repositorio de instancias PDDL de Potassco. Se examinó una instancia de cuadrícula de tamaño cinco, con exploración exhaustiva hasta profundidad dos. Las transformaciones candidatas son los movimientos permitidos por las condiciones de conectividad y posición definidas en el problema original.

**Coordinación probabilística de procesos.** El segundo dominio procede de un modelo de elección de líder distribuida publicado en el repositorio de ejemplos de PRISM. El modelo representa tres procesos organizados en anillo y utiliza comandos sincronizados, guardas y alternativas probabilísticas. Las identidades de transformación corresponden a las etiquetas de acción definidas por el propio modelo.

Los dominios no comparten las mismas transformaciones ni la misma semántica. La comparación no equipara un movimiento de la cuadrícula con una acción del modelo probabilístico.

## Procedimiento analítico

En ambos casos se reconstruyó la siguiente secuencia:

\[
S_t \rightarrow T_{acc,t} \rightarrow T_{real,t}
\rightarrow S_{t+1} \rightarrow T_{acc,t+1}
\]

A partir de los espacios accesibles en los dos estados se derivaron descriptores de persistencia, identidades incorporadas, identidades retiradas, rotación y cambio neto de cardinalidad. Las operaciones de conjuntos se realizaron dentro de cada dominio; la comparación entre dominios se limitó a la estructura de los descriptores.

La evidencia de origen ya estaba congelada. El análisis comparativo fue una elaboración secundaria de esos registros, no una nueva ejecución científica. En cada transición, el espacio accesible inicial se derivó del estado de origen y el espacio sucesor se volvió a calcular a partir del estado sucesor reconstruido. Las reconstrucciones independientes de la cuadrícula coincidieron en la estructura del árbol de 21 nodos y 20 aristas. En el modelo probabilístico, los dos ejecutores reconstruyeron 25 registros cada uno, con coincidencia de la huella de la fuente y cero desviaciones estructurales. Una auditoría matemática independiente revisó después los 36 registros comparativos y sus descriptores derivados.

## Resultados

El análisis comparativo reunió **36 registros de transición**: 20 procedentes del dominio de planificación en cuadrícula y 16 del modelo probabilístico. El proceso de análisis no identificó registros inválidos. La auditoría matemática comprobó los 36 registros y no encontró discrepancias en los descriptores calculados.

### Dominio de planificación en cuadrícula

En las 20 transiciones se observó rotación de identidades: aparecieron transformaciones accesibles nuevas y otras dejaron de estarlo. La cardinalidad media del espacio pasó de 4,0 a 3,8. En el estado inicial había cuatro movimientos accesibles.

Este resultado tiene una limitación importante. La auditoría científica específica del dominio mostró que tanto el conjunto de movimientos accesibles como sus cambios podían reconstruirse completamente a partir de la representación convencional de estados, acciones y transiciones del problema. Por tanto, en esta instancia no se demostró una ganancia representacional distinta por introducir explícitamente el espacio de transformaciones accesibles.

Este resultado negativo se conserva como parte de la evidencia; no se modificaron las definiciones del dominio para evitarlo.

### Modelo probabilístico de coordinación

En las 16 transiciones, la cardinalidad media del espacio accesible permaneció en 1,0 antes y después de la transición. Sin embargo, en todos los registros cambió la identidad de la transformación accesible. El número de opciones se mantuvo, pero la opción disponible fue sustituida.

Este patrón ilustra por qué la cardinalidad, considerada de forma aislada, no describe toda la reconfiguración de un espacio de transformaciones.

## Qué respalda el análisis

El resultado respalda una conclusión metodológica delimitada: en estos dos ejemplos computacionales, con semánticas de dominio diferentes y reglas de accesibilidad explícitas, fue posible reconstruir la relación entre estado, accesibilidad, realización, estado sucesor y accesibilidad sucesora, y derivar descriptores comparables sin equiparar las identidades de transformación de ambos dominios.

La evidencia permite tratar esa estructura como una forma de operacionalización interdominio en los casos examinados. No demuestra que funcione en cualquier sistema ni que constituya una representación necesaria o superior.

## Qué no demuestra

El análisis no demuestra:

- validez transversal o universalidad entre dominios;
- superioridad explicativa o representacional frente a los modelos nativos;
- que el espacio accesible sea un nuevo primitivo ontológico;
- que los cambios de accesibilidad causen cambios en trayectorias;
- efectos sobre resultados posteriores o creación de valor;
- Transformational Intelligence como capacidad demostrada;
- utilidad práctica en sistemas desplegados.

Además, la reconstrucción del modelo probabilístico codificó directamente las semánticas del modelo congelado; no fue una nueva ejecución del motor PRISM. Aunque las fuentes de dominio están públicamente identificadas y las reconstrucciones independientes concordaron, esta nota todavía no incluye un paquete público autónomo con los ejecutores y los 36 registros derivados. Por tanto, no debe confundirse la concordancia de reconstrucción auditada con una reproducción independiente realizada por cualquier lector a partir de esta nota.

## Fuentes de los dominios

- Potassco. *PDDL instances covering the International Planning Competitions*. Revisión fijada del repositorio: [potassco/pddl-instances](https://github.com/potassco/pddl-instances/tree/cf19edf7c53d1540ddbb396c642595e0926ee552).
- PRISM Model Checker. *PRISM Benchmark Suite — synchronous leader-election model*. Archivo y revisión fijados: [leader_sync3_2.pm](https://github.com/prismmodelchecker/prism-benchmarks/blob/59ee49c031dbdfdb1e606edcdd643410de32192b/models/dtmcs/leader_sync/leader_sync3_2.pm).

## Relación con el capítulo

Esta nota complementa el capítulo **El espacio de transformaciones accesibles**. Su función es documentar el alcance de un resultado metodológico concreto, incluidos sus límites y el resultado negativo obtenido en uno de los dominios.
