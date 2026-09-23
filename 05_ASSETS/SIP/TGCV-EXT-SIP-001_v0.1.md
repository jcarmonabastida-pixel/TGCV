# TGCV-EXT-SIP-001 — Scientific Integration Plan (SIP) v0.2

**Programa:** TGCV — Teoría de Construcción de Valor de Sistemas Generativos  
**Clase:** Planificación científica estratégica  
**Estado:** CURRENT / CONTROLLED  
**Supersedes:** v0.1 (`f147b94c15ccea98f6306c75d708d54f49a4e3dd`)  
**Fecha:** 2026-09-23  
**Asset ID:** TGCV-EXT-SIP-001  
**Base canónica:** RMA v3.32 + Evidence→Claim Matrix v1.1 + TCP v0.4 + Vision Paper v0.3 + Research Prospectus v0.2 + ARM v0.2 + RII v0.1 + MOI v0.1

## 1. Propósito

El SIP organiza la integración del programa científico TGCV: arquitectura conceptual, evidencia, comparación con antecedentes, operacionalización, experimentación, límites, transferencia y futuras líneas doctorales/industriales.

El SIP es un instrumento de planificación y coordinación. No constituye evidencia científica adicional, no modifica el Core, no convierte hipótesis en resultados y no autoriza por sí mismo ninguna ejecución experimental o industrial.

## 2. Arquitectura científica de referencia

- `Core_ontological = S`
- `T_acc = F(S,C,L)`
- `ΔT_acc(t,t+1) = T_acc,t+1 ≄ T_acc,t`
- `I` permanece como mecanismo explicativo y no como primitivo del Core.
- Cadena analítica: `mechanism → (S_t,C_t) → (S_{t+1},C_{t+1}) → ΔT_acc → ΔReach → ΔTrajectory → Outcome → Value`.

El SIP adopta la consecuencia metodológica vigente: la enumeración exhaustiva ex ante de todo `T_acc(S_t)` no es un prerrequisito universal. Las operaciones deben justificar, según el caso, la transformación candidata, estado/contexto relevante, regla de accesibilidad independiente del resultado, condiciones de decisión congeladas y transición reconstruible.

## 3. Objetivos de integración

1. Mantener una única arquitectura conceptual y terminológica entre activos.
2. Mantener separadas ontología, representación analítica, mecanismo, accesibilidad, Reach, trayectoria, Outcome y Value.
3. Integrar evidencia sin convertir evidencia metodológica acotada en claims generales.
4. Priorizar operaciones por valor informativo y capacidad de falsación, no por volumen de actividad.
5. Mantener trazabilidad desde cada resultado hasta su evidencia, protocolo y estado epistemológico.
6. Preparar una ruta coherente hacia investigación doctoral, colaboración científica y exploración industrial sin anticipar validación externa.

## 4. Capas y dependencias

### Capa A — Fundamento científico

RMA, Matrix, TR-131, TCP, Vision Paper y Research Prospectus constituyen la referencia conceptual y de claim boundary.

### Capa B — Evidencia y metodología

ARM, registros experimentales y operaciones metodológicas cerradas proporcionan evidencia y límites. La evidencia Rust es estructural/operacional; IUT-A-01 U2 permanece `U2-NULL`; IT-NOSD-010 aporta evidencia metodológica acotada; EXT-UPD-4.8 cierra O3 como `INDETERMINATE / H-B / HS-AC01`; AWS Class-II permanece evidencia de fixture.

### Capa C — Transferencia y oportunidad

RII y MOI traducen evidencia acotada en rutas de transferencia y oportunidades hipotéticas. No constituyen demostración de utilidad, superioridad, causalidad o valor.

### Capa D — Ejecución futura controlada

Cualquier nueva operación requiere su propio diseño, preflight, autorización y cierre. El SIP no sustituye esos gates.

## 5. Priorización

La prioridad se determina por:

- reducción de incertidumbre científica relevante;
- capacidad de falsar o acotar la arquitectura;
- independencia respecto de resultados previos;
- disponibilidad de evidencia y condiciones de reconstrucción;
- claridad de las variables y reglas de accesibilidad;
- trazabilidad y reproducibilidad;
- coste/esfuerzo razonable frente a información esperada;
- potencial de traducción transversal sin forzar equivalencias.

No se prioriza una operación únicamente por interés industrial, facilidad de ejecución o expectativa de resultado positivo.

## 6. Líneas de trabajo

**SIP-L1 — Consolidación científica:** mantener arquitectura, claims y no-claims sincronizados con RMA/Matrix.

**SIP-L2 — Validación y límites:** desarrollar únicamente operaciones que puedan distinguir estructura, redundancia, dinámica, Reach/Trajectory y límites de aplicabilidad.

**SIP-L3 — Comparación externa:** continuar delimitando antecedentes y riesgo de absorción por estado del arte; originalidad permanece abierta.

**SIP-L4 — Reutilización científica:** aplicar el Scientific Asset Registry y la prohibición de trabajo desde cero antes de nuevas operaciones.

**SIP-L5 — Transferencia disciplinada:** usar RII/MOI para formular hipótesis de aplicación y no para afirmar beneficios.

**SIP-L6 — Ruta doctoral:** mantener una narrativa investigadora falsable y acumulativa, separando resultados científicos de adaptación institucional o de candidatura.

## 7. Estado de operaciones cerradas

El SIP reconoce como cerradas dentro de sus respectivos alcances las operaciones D-OPS-24 y EXT-UPD-4.8. No las reabre ni las convierte en tareas pendientes.

TR-131 está aceptado y no debe reabrirse como test pendiente. TCP v0.4, Vision Paper v0.3, Research Prospectus v0.2, ARM v0.2, RII v0.1 y MOI v0.1 son activos actuales controlados.

## 8. Gate para nuevas operaciones

Antes de iniciar una nueva operación:

1. consultar `CANONICAL_STATE` y governance vigente;
2. consultar el Scientific Asset Registry;
3. identificar antecedentes y activos históricos relevantes;
4. fijar objetivo y claim boundary;
5. definir diseño y criterios de parada;
6. ejecutar preflight;
7. obtener autorización específica cuando corresponda;
8. ejecutar sin contaminar el resultado con información posterior al punto de decisión;
9. registrar hashes, resultados y límites;
10. propagar materialmente el resultado a RMA/Matrix/traceability cuando proceda;
11. ejecutar el validator como gate final.

## 9. Interfaces con planificación posterior

El SIP precede lógicamente a instrumentos de gestión operativa como PMO/SMO. Esos instrumentos, si se crean, deben derivarse de este marco y no modificar la arquitectura científica ni conceder autorización experimental por defecto.

## 10. Redirección científica vigente de TR-131

La línea vigente de TR-131 se ha desplazado desde la búsqueda de superioridad representacional de \`T_acc\` y desde la hipótesis causal \`ΔT_acc → ΔValue\` hacia la dinámica del espacio de transformaciones y la capacidad de navegarlo.

Referencia canónica:
- \`03_EXPERIMENTS/TR-131/TR131_CONVERSATION_RECORD_TRANSFORMATIONAL_INTELLIGENCE_001.md\`
- \`00_GOVERNANCE/TGCV_TRANSFORMATIONAL_DYNAMICS_INTELLIGENCE_MANIFESTO_001.md\`

La interpretación vigente de VisitAll es:

**PASS — instrumentación y observación de estructura/dinámica de transformación; sin demostración de ganancia representacional distintiva frente al baseline nativo.**

Este resultado no constituye un fracaso de TGCV. VisitAll queda cerrado como demostración de instrumentación y observación; no se reabre para perseguir representational gain.

Rainbow queda fuera de la infraestructura científica requerida para esta línea actual de TR-131. SWIM no forma parte de esta línea científica.

## 11. Transformation-Space Dynamics

La cadena dinámica de referencia es:

\`S_t → T_acc,t → T_real,t → S_(t+1) → T_acc,t+1 → ...\`

con:

\`ΔT_acc,t = D(T_acc,t,T_acc,t+1)\`

El foco pasa a ser cómo evoluciona el espacio de transformaciones accesibles.

Los fenómenos candidato incluyen expansión, contracción, turnover, persistencia, novedad, pérdida, reversibilidad, dependencia histórica, branching, reconfiguración y efectos de las transformaciones realizadas sobre las posibilidades futuras.

La transversalidad se busca en la lógica analítica y en la utilidad práctica, no en una ontología idéntica entre dominios.

## 12. Transformational Intelligence

Constructo de trabajo:

> **Transformational Intelligence is the capacity to reason over, navigate, and adapt a system's space of accessible transformations in order to shape future trajectories toward desired outcomes under an independently specified value model.**

Componentes funcionales:
1. **Reason over:** representar y analizar el espacio de transformaciones.
2. **Navigate:** discriminar y seleccionar entre transformaciones accesibles.
3. **Adapt:** incorporar que las transformaciones realizadas modifican estados y posibilidades futuras.
4. **Orient trajectories:** utilizar outcomes deseados y un modelo de valor independiente como contexto de orientación.

TI no se define por valor, éxito, performance ni outcome observado.

## 13. Value/VSL

La arquitectura de valor permanece downstream e independiente:

\`T_acc → transformation handling / TI → T_real → trajectory → O → VSL → V*\`

VSL no define \`T_acc\`, \`ΔT_acc\`, TI, transformación ni trayectoria.

La hipótesis \`ΔT_acc → ΔValue\` deja de ser el eje de investigación. Cualquier relación entre dinámica transformacional y valor deberá establecerse mediante evidencia independiente y controles apropiados.

## 14. Secuencia experimental canónica

La nueva secuencia de investigación queda fijada en el SIP:

### Gate A — Cross-domain operationalisation

Seleccionar un segundo dominio sustancialmente diferente de VisitAll y comprobar que puede instanciarse de forma reproducible:

\`state → transformation space → realized transformation → successor state → changed transformation space → trajectory\`

Requisitos mínimos: estado bien definido, transformaciones identificables, ejecución/reconstrucción reproducible, evolución observable de \`T_acc\`, trayectorias observables y fuente primaria reproducible.

**Criterio:** operacionalización reproducible de la dinámica transformacional en un dominio materialmente distinto.

### Gate B — Cross-domain usefulness

Comparar los dominios sin exigir equivalencia ontológica y evaluar si la representación permite extraer información útil sobre expansión/contracción, apertura/cierre de posibilidades, persistencia/pérdida, branching, efectos sobre espacio futuro, trayectorias y adaptación/reconfiguración.

**Criterio:** información analíticamente útil y transversalmente interpretable sobre dinámica transformacional.

### Gate C — Transformational Intelligence differentiation

Diferenciar TI frente a dynamic capabilities, adaptability, self-adaptation, search/selection, learning/evolution, affordances y constructos relacionados.

**Criterio:** diferenciación conceptual y operacional falsable, sin reclamar novedad por terminología.

### Gate D — Outcome linkage

Estudiar \`trajectory → outcome\`, manteniendo outcomes fuera de la definición de TI.

**Criterio:** relaciones sistemáticas, si existen, entre patrones de navegación/dinámica transformacional y outcomes independientes.

### Gate E — Value-guided navigation

Integrar:

\`trajectory → outcome → VSL → value\`

y estudiar si el conocimiento de la dinámica transformacional puede orientar la selección entre transformaciones accesibles hacia trayectorias cuyos outcomes reciben mayor valoración.

**Criterio:** evidencia de utilidad de navegación orientada por valor sin convertir TI en una función de valor ni VSL en una definición de transformación.


### Gate F — Scientific Core & Ontology Review

Gate F follows Gate E and is explicitly part of the cross-domain research programme. Its purpose is to determine, from accumulated evidence, whether the current TGCV scientific Core and ontology remain adequate for the phenomena exposed by transformation-space dynamics and Transformational Intelligence.

Gate F does **not** presume that the Core must change. It may conclude:

- **NO ONTOLOGICAL CHANGE REQUIRED**;
- Core extension required;
- existing construct demotion required;
- new primitive/process/capability warranted;
- analytical architecture should remain outside the ontology;
- boundaries between mechanism, capability, process and ontology require revision.

Candidate constructs for review include `T_real`, selection, transformation handling, trajectory, transformation-space dynamics and Transformational Intelligence, alongside the existing Core assumption centred on `S`.

Methodological rule:

> **Evidence first → conceptual differentiation second → ontological review third → Core modification only if warranted by accumulated evidence.**

Until Gate F, candidate constructs are not to be promoted silently into the Core.

## 15. Flujo experimental operativo

Cada Gate mantiene:

\`source → fixture → operationalisation → Executor-1 → Executor-2 → audit → scientific result → canonical incorporation\`

Toda nueva operación requiere consultar \`CANONICAL_STATE\`, Scientific Asset Registry y antecedentes; fijar objetivo y claim boundary; definir diseño y stop criteria; ejecutar preflight y autorización específica; ejecutar independientemente; registrar hashes, resultados y desviaciones; auditar; propagar materialmente el resultado y cerrar mediante validator.

## 16. Líneas de trabajo actualizadas

**SIP-L1 — Consolidación científica:** mantener arquitectura, claims y no-claims sincronizados.

**SIP-L2 — Transformation-Space Dynamics:** operacionalizar y estudiar la evolución de espacios de transformación.

**SIP-L3 — Cross-domain applicability:** evaluar operacionalización y utilidad transversal en dominios heterogéneos.

**SIP-L4 — Transformational Intelligence:** diferenciar y operacionalizar el constructo frente al estado del arte.

**SIP-L5 — Outcome/Value linkage:** conectar trayectorias con outcomes y, posteriormente, con VSL independiente.

**SIP-L6 — Transferencia disciplinada:** formular aplicaciones como hipótesis y no como beneficios demostrados.

**SIP-L7 — Ontology/Core governance:** preserve the explicit Gate F and the rule that evidence precedes ontological modification.\n\n**SIP-L8 — Ruta doctoral:** mantener una narrativa falsable, acumulativa y separada de las adaptaciones institucionales.

## 17. Próximo paso

El próximo gate de la planificación científica es:

**GATE A — CROSS-DOMAIN OPERATIONALISATION**

La tarea inmediata es seleccionar y auditar un segundo dominio experimental materialmente diferente de VisitAll, con fuente primaria reproducible y capacidad de observar la evolución de \`T_acc\`.

No se inicia Gate B, C, D, E o F hasta cerrar el correspondiente gate anterior. Gate F is a review gate, not a presumption of ontological change.

## 10. No-claims

Este SIP no establece:

- universalidad de TGCV;
- causalidad entre cambios de `T_acc` y Value;
- superioridad frente a métodos existentes;
- originalidad completa;
- validación transversal completa;
- utilidad industrial demostrada;
- valor económico realizado;
- validación por socios externos;
- certificación o estándar externo;
- autorización permanente de ejecución.

## 18. Estado

**CURRENT / CONTROLLED — v0.2.** Esta versión sustituye a v0.1 como SIP vigente.

Este documento es un activo de planificación estratégica científica. Cualquier revisión material debe crear una nueva versión controlada y propagarse por los canales canónicos correspondientes.
