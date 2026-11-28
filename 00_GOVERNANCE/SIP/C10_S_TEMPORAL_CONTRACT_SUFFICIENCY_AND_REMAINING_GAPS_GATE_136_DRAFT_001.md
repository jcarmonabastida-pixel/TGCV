# C10-S — Gate 136: suficiencia de contratos temporales y vacíos residuales

**Fecha:** 2026-11-16  
**Rama:** research/c10-s-consolidation-draft · PR #116 (Draft)  
**Estado:** TEMPORAL_SEMANTICS_DOCUMENTED / EVENT_MODEL_DOCUMENTED_NOT_MATERIALIZED / BOUNDARY_RULE_PENDING_VERSIONED_ADOPTION / GENERATOR_UNKNOWN_SOURCE_UNSPECIFIED / S3_OBSERVATION_SEPARATED / PARAMETERS_OPEN_BY_DESIGN / NO_CODE_CHANGE / NO_EXECUTION / NO_DESIGN_FREEZE.

## 1. Objeto y alcance

Auditoría estática de suficiencia de los contratos existentes para no rediseñar aquello que ya está especificado. Fuentes examinadas: plan integrado C10-S Draft 004 §§16.195–198; contrato DGP temporal y de roles §§49–55; reconciliación B1/Need_preZ; DEC-C10-100…102; Test Contract Register P182/P183/MEAS/MISS; Gates 131, 133–135; y fuente de harness inspeccionada en Gate 135. No se ejecutaron pruebas, validadores ni simulaciones.

## 2. Dictamen ejecutivo

La especificación temporal documental es más completa de lo que sugería una lectura aislada del harness. El plan §§16.195–198 y el contrato DGP §§49–55 ya definen el reloj normalizado, el dominio de episodios, el orden Generator→S3, la estructura mínima de cada transición, la adjudicación estricta por intervalo, la regla de frontera propuesta, los mecanismos S3 y la estrategia de recuperación/bounds/abstención.

Por tanto, **no procede crear otra matriz temporal, otra familia de escenarios ni otra decisión para volver a definir continuidad, eventos o la separación de observación**.

Quedan dos asuntos residuales genuinos:
1. La fuente/condición generadora que hace legítimo que Generator emita truth funcional ? para A_B1/V_cont no está operacionalmente especificada en los contratos temporales revisados. Las reglas de UNKNOWN en Reach y en otros objetos no se pueden trasladar automáticamente a V_cont.
2. La convención semiabierta de frontera está formulada y recomendada, pero sigue marcada como pendiente de versionado/adopción antes de materializarla.

El mapping semántico de t0 y la inclusión de provisión/instalación están definidos por DEC-C10-101 y §§16.195/49/55. Lo que falta es su representación y trazabilidad concreta en el futuro event history/harness, no otra decisión sobre el origen de la ventana.

## 3. Crosswalk de suficiencia

| Requisito | Fuente existente | Suficiencia documental | Estado material |
|---|---|---|---|
| Reloj común desde t0 post-Z | DEC-C10-101; plan §16.195.1/8; DGP §§49/55 | DEFINIDO: reloj adimensional desde t0, soporte común | No representado plenamente en harness |
| Provisión e instalación dentro de ventana | DEC-C10-101; DGP §§49/55; plan §16.195 | DEFINIDO: son antecedentes/eventos dentro del soporte; no son por sí solos fallo funcional | Mapping de eventos aún no materializado |
| Episodio funcional | Plan §16.195.2; §16.198.4; DGP §55 | DEFINIDO: inicio, fin, familia, unidad/versión, estados previo/posterior, event_time y provenance | No existe event history intraintervalo en harness actual |
| Continuidad estricta | DEC-C10-102; plan §§16.195.2, 16.197.2/4, 16.198.1/4; DGP §§49/55 | DEFINIDO: cualquier incumplimiento confirmado afecta todos los intervalos intersectados | Harness solo usa estados por slot |
| Evento en frontera | Plan §§16.195.6, 16.197.4, 16.198.2; DGP §49 | REGLA PROPUESTA: [b_k,b_{k+1}); frontera asignada al intervalo que comienza allí; último incluye T* | Pendiente de versionado/adopción explícita |
| Reloj de observación S3 | Plan §§16.195.3–4, 16.196, 16.198.3; DGP §§49/55 | DEFINIDO: captura, lag, cobertura, pérdida, validez, error y dependencia; snapshots/logs/híbrido | No calibrado ni materializado por completo |
| Separación truth/S3 | DEC-C10-102; plan §16.198.4; DGP §§49/55; P182-11; P183-01…04 | DEFINIDO: Generator primero genera truth; S3 observa después; Analyzer solo recibe proyección sellada; Evaluator abre truth después | Firewall parcial en harness; full conformance no acreditada |
| UNKNOWN funcional de A_B1 | DEC-C10-100/102; P183 taxonomía general | REGLA DE SALIDA DEFINIDA; fuente generadora específica de ? para V_cont no cerrada | No representado |
| Bounds y abstención | DEC-C10-100; plan §§16.196.3–4, 16.197.4, 16.198.5; P183-11/12 | REGLA GENERAL DEFINIDA; método individual [n1/K,(n1+n?)/K]; dictamen por estimando | No implementado para truth tri-valuada ni medición imperfecta |

## 4. Hallazgo específico: fuente legítima de UNKNOWN

DEC-C10-100/102 no autoriza que ? signifique S3 ausente, perdido, retrasado, inválido o fuera de cobertura. Esos son estados del canal de observación. El Test Register refuerza la separación (P183-01…04, P183-09/11), pero esos contratos son taxonomías y criterios generales; no definen por sí solos el mecanismo generador de UNKNOWN de A_B1.

El contrato DGP ya establece reglas 1/0/? para otros constructos, por ejemplo Reach y componentes de accesibilidad, pero no se debe extrapolar esa lógica sin mapping. Para V_cont falta precisar qué indeterminación pertenece a la propia estipulación funcional de B1 y bajo qué condición el Generator no puede adjudicar si ENABLED/PROFILE se mantuvo durante todo el intervalo.

**Restricción crítica:** en un DGP sintético, que el Generator omita una regla, no modele un componente o no conserve eventos no puede convertirse en UNKNOWN científico legítimo. Eso sería una carencia de especificación/implementación. ? solo será admisible cuando el contrato defina una indeterminación interna del estado funcional generado, distinta de la ausencia/error de observación. El caso debe conservar razón y provenance reservadas para Evaluator. No se decide aquí cuál será ese mecanismo.

## 5. Eventos, reloj y frontera: no reabrir lo definido

La estructura de evento está descrita en el plan §16.198.4 y DGP §55: estado previo, evento/causa, event_time, estado posterior, versión y provenance. DGP §49 separa el reloj de truth/event_time, la rejilla de agregación y el reloj de observación S3. Las cinco familias causales y sus transiciones se mantienen; no se crea un catálogo alternativo.

La adjudicación por intervalo está especificada: un incumplimiento confirmado en cualquier instante hace A_B1=0 en cada intervalo que intersecte. La regla semiabierta evita doble asignación en fronteras. Sin embargo, como el plan registra esa regla como PENDING_PREMATERIALIZATION y exige versionarla, Gate 136 no la eleva unilateralmente a decisión aprobada. Debe formalizarse por el procedimiento documental correspondiente antes de la materialización.

DEC-C10-101 fija el ancla post-Z e incluye provisión/instalación. La normalización x=(t−t0)/W_c no introduce duración física ni fija T*. La cola, soporte de transiciones, T*, Δ y K siguen OPEN deliberadamente.

## 6. P182/P183/MEAS/MISS: alcance real

- P182-07/08: error de medición; P182-11: separación de datos; P182-12: trazabilidad.
- P183-01/02: taxonomía y mecanismos de ausencia; P183-03/04: desconocido/no observado no equivalen a inaccesible/cero; P183-09: censura; P183-11/12: bounds y dictamen por estimando.
- MEAS/MISS aportan perfiles adversariales reutilizables, incluyendo errores, pérdida, lag, selección y censura.

Estos contratos son criterios de cobertura, no evidencia de que los escenarios estén materializados, los oráculos implementados, la calibración realizada o los tests ejecutados. No se crean IDs ni se declara PASS técnico.

## 7. Consecuencia para la secuencia de cierre

Gate 136 reduce el trabajo documental residual a:
1. Resolver la semántica generadora de UNKNOWN funcional de A_B1, sin confundirla con S3 missingness ni con omisiones del propio harness.
2. Adoptar/versionar formalmente la regla de frontera ya propuesta, si el contrato de precedencia confirma que no existe una adopción posterior.
3. Después, preparar un crosswalk de implementación hacia Generator/TruthBundle/Sealer/Analyzer/Evaluator, preservando la estructura de evento y el orden de información ya definidos.

No se requiere reabrir reloj, cinco familias, continuidad estricta, mecanismos S3, bounds individuales ni separación de roles. No se fijan valores numéricos ni se seleccionan K, Δ o T*.

## 8. Límites y autorización

No modifica DEC, contratos base, código, schemas, tests, workflows, IDs de prueba, DGP ledger, RMA, Evidence→Claim Matrix, STATUS, main ni PR base. No ejecuta código, validadores, workflows, generación, simulación, calibración o estimación.

scientific_execution=false  
execution_authorized=false
