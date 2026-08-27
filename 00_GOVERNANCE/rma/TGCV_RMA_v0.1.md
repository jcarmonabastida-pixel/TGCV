# TGCV — Registro Maestro de Activos (RMA) v0.1

**Estado:** Working / operativo  
**Fecha:** 2026-08-27  
**Propósito:** registro maestro de activos del programa TGCV, sus dependencias, trazabilidad, estado epistemológico y gates de decisión.

## 1. Regla de estado

Este RMA se construye sobre el último estado seguro recuperado del programa. No sustituye a los documentos científicos ni reabre decisiones ya estabilizadas.

La arquitectura de trabajo vigente es:

- Ontología mínima: `S`
- Estructura analítica: `T_acc = F(S,C,L)`
- Dinámica: `(S_t,C_t) ->τ (S_{t+1},C_{t+1})`
- Fenómeno: `T_acc,t ≄ T_acc,t+1`
- Consecuencia: `ΔT_acc -> ΔReach -> ΔTrajectory`
- Extensión de valor: `Trajectory -> Outcome -> Value`
- `I` permanece como mecanismo explicativo, no como primitivo del Core.

TR-129, TR-130 y TR-135–TR-140 constituyen el estado conceptual seguro recuperado. TR-139 es Conditional Pass y TR-140 Survives; la originalidad arquitectónica no se considera demostrada hasta completar el contraste sistemático con literatura.

## 2. Gate crítico actual

**GATE EXT-1.0 — validación/falsación empírica de la operacionalización actual de TGCV.**

Estado histórico en esta versión: pendiente de ejecución por liberación de cuota.

Regla: los activos pueden desarrollarse en paralelo cuando su arquitectura no dependa del resultado de EXT-1.0. Los activos dependientes se marcan como `CONDITIONAL` y no pueden presentar la hipótesis como teoría validada.

## 3. Convención de estados epistemológicos

- **FOUNDATIONAL:** decisión/arquitectura ya estabilizada por el programa.
- **WORKING:** construcción actual susceptible de revisión.
- **CONDITIONAL:** depende materialmente de un gate pendiente.
- **EMPIRICALLY TESTED:** sometido a prueba, con resultado registrado.
- **VALIDATED:** reservado para afirmaciones que hayan satisfecho los criterios de validación establecidos; no usar anticipadamente.
- **RETIRED/SUPERSEDED:** conservado para trazabilidad histórica, no vigente.

## 4. Registro de activos — primera cartera

| ID | Activo | Clase | Propósito | Estado | Dependencia principal | Sensibilidad EXT-1.0 | Prioridad |
|---|---|---|---|---|---|---|---|
| TGCV-EXT-VP-001 | Vision Paper | Externo científico | Exponer visión, problema, apuesta y arquitectura sin sobreactuar validación | WORKING | Arquitectura estabilizada; SLR-1 | Media | 1 |
| TGCV-EXT-RP-001 | Research Prospectus | Externo científico | Convertir la visión en programa doctoral/investigador falsable | WORKING | VP, TCP, arquitectura | Alta | 1 |
| TGCV-EXT-ARM-001 | ARM | Externo/aplicado | Formalizar la arquitectura de transformación y su interfaz con aplicación/valor | WORKING | TCP, arquitectura | Alta | 1 |
| TGCV-EXT-MOI-001 | Mapa de Oportunidades Industriales | Externo/aplicado | Mapear dominios donde el fenómeno puede ser investigado/aplicado | WORKING | ARM, RII, arquitectura | Media | 1 |
| TGCV-EXT-TCP-001 | TCP | Externo científico/técnico | Fijar la arquitectura testable, variables, mecanismos y criterios de prueba | WORKING | Arquitectura, EXT-1.0 | Muy alta | 1 |
| TGCV-EXT-RII-001 | RII | Externo científico/aplicado | Articular investigación, implementación, evidencia e impacto | WORKING | ARM, MOI, TCP | Alta | 1 |
| TGCV-MET-SIP-001 | SIP | Metodológico | Sistema operativo de investigación y priorización | WORKING | Gobernanza, RMA | Media | 2 |
| TGCV-MET-PMO-001 | PMO/SMO | Metodológico/gobernanza | Coordinar activos, gates, decisiones, versiones y dependencias | WORKING | Proyecto Cero, contrato de trabajo | Baja | 2 |
| TGCV-MET-SDM-001 | Metodología de descubrimiento científico | Metodológico | Compilar y explicitar la metodología de descubrimiento usada por el programa | PROPOSED | SIP, PMO/SMO, historia de investigación | Media | 2 |
| TGCV-SLR-EXP-001 | Expedientes SLR | Científico | Preservar investigación de literatura, decisiones y trazabilidad por fuente | WORKING | SLR-1 | Baja | 3 |
| TGCV-SLR-EVB-001 | Banco de Evidencias | Científico | Estructurar evidencia primaria y su relación con claims | WORKING | Expedientes SLR | Baja | 3 |
| TGCV-SLR-FCT-001 | Banco de Hechos | Científico | Separar hechos extraídos de inferencias y claims | WORKING | Evidence Bank | Baja | 3 |
| TGCV-SLR-MAT-001 | SLR-1 Prior-Art Absorption Matrix | Científico/gate | Intentar falsar la originalidad arquitectónica de TGCV | WORKING | Literatura + arquitectura | Baja | 3 |

## 5. Dependencias y orden de construcción

### Ola A — activos externos

1. TCP
2. Vision Paper
3. Research Prospectus
4. ARM
5. RII
6. Mapa de Oportunidades Industriales

### Ola B — infraestructura metodológica

7. SIP.
8. PMO/SMO.
9. Evaluación y, si procede, consolidación de SDM.

### Ola C — infraestructura científica SLR

10. Expedientes.
11. Banco de Evidencias.
12. Banco de Hechos.
13. Matriz SLR-1.

## 6. Matriz de trazabilidad maestra — esquema operativo v0.1

Cada activo debe registrar, como mínimo:

`Activo -> propósito -> pregunta/claim -> componente arquitectónico -> evidencia requerida -> fuentes/expedientes -> activos de entrada -> activos de salida -> gate -> versión TGCV -> estado epistemológico -> decisiones que pueden modificarlo.`

### Trazas estructurales iniciales

- **Core ontológico `S`** -> TCP, VP, RP, ARM.
- **`T_acc = F(S,C,L)`** -> TCP, VP, RP, ARM.
- **Cambio estructural `ΔT_acc`** -> TCP, VP, RP, SLR-1.
- **Cadena `ΔT_acc -> ΔReach -> ΔTrajectory`** -> TCP, ARM, RP.
- **Extensión `Trajectory -> Outcome -> Value`** -> ARM, RII, MOI; no debe justificar retrospectivamente el Core ontológico.
- **Interacción `I` como mecanismo, no Core** -> TCP, VP, RP; evitar reintroducción como primitivo.
- **Novedad/originalidad** -> SLR-1, Evidence Bank, Banco de Hechos; no declararla demostrada por los tests conceptuales previos.
- **EXT-1.0** -> TCP y cualquier activo que dependa de la operacionalización empírica; resultado debe propagarse mediante el RMA antes de actualizar claims externos.

## 7. Reglas de actualización

1. No sobrescribir el estado histórico: cada cambio sustantivo debe generar nueva versión.
2. Todo activo externo debe indicar su versión de TGCV y su estado epistemológico.
3. Ningún resultado de aplicación industrial se utilizará como prueba retrospectiva del Core.
4. Ninguna coincidencia terminológica de la literatura implica absorción arquitectónica.
5. La SLR debe distinguir similitud terminológica, equivalencia de constructo, equivalencia estructural y absorción arquitectónica completa.
6. Una modificación del Core requiere evidencia/gate explícito; no se deriva de una coincidencia aislada.
7. EXT-1.0 es un gate de validación de la operacionalización, no una confirmación asumida.
8. Los activos se mantienen trazables aunque un gate produzca un resultado negativo o intermedio.

## 8. Registro de decisiones pendiente

- [ ] Confirmar el nombre largo y definición contractual exacta de TCP antes de congelar la portada externa.
- [ ] Recuperar/contrastar la matriz de trazabilidad histórica completa cuando aparezca el documento maestro correspondiente.
- [ ] Determinar si SDM se eleva a activo formal tras reconstruir su metodología.
- [ ] Vincular los criterios cuantitativos definitivos de EXT-1.0 al RMA.

## 9. Próxima operación de esta versión histórica

Construir el TCP como primer activo externo estructural y derivar VP y RP de la misma arquitectura, evitando divergencia entre documentos.

> **Continuidad:** esta versión se conserva como artefacto histórico. El estado posterior debe leerse desde `STATUS.md` y sus registros de gobierno/experimentos más recientes.