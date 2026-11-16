# C10-S — Gate 137: docket de UNKNOWN funcional y convención de frontera

**Fecha:** 2026-11-16  
**Rama:** research/c10-s-consolidation-draft · PR #116 (Draft)  
**Estado:** UNKNOWN_SOURCE_NOT_SPECIFIED / CONSERVATIVE_GENERATION_RULE_RECOMMENDED / HALF_OPEN_BOUNDARY_RECOMMENDED_NOT_ACCEPTED / USER_DECISION_PENDING / NO_CODE_CHANGE / NO_EXECUTION / NO_DESIGN_FREEZE.

## 1. Objeto y precedencia

Resolver hasta donde permiten los contratos vigentes los dos residuos de Gate 136, sin reabrir DEC-C10-100…102 ni convertir una propuesta histórica en decisión aceptada.

Fuentes inspeccionadas: DEC-C10-100, DEC-C10-101 y DEC-C10-102 autónomas; Decision Log C10-S hasta DEC-C10-103; DGP temporal §§48–55; plan integrado §§16.193–16.198; Gates 134–136; contratos P182/P183/MEAS/MISS.

## 2. UNKNOWN funcional: resultado de la reconstrucción

DEC-C10-100 define A_B1(i,k)∈{1,0,?} y bounds. DEC-C10-102 restringe ? a los casos en que la truth funcional del intervalo no queda determinada por Generator. DGP §48 repite esa condición. Sin embargo, los contratos B1/DGP revisados describen ENABLED/PROFILE, cinco familias de transiciones funcionales, estados efectivos, event_time y provenance; no especifican una causa intrínseca concreta por la que Generator deba dejar indeterminada A_B1 en un intervalo.

P182/P183/MEAS/MISS no rellenan ese vacío: sus categorías de missingness, error, lag, censura y bounds pertenecen a observación/identificación. Las reglas 1/0/? de Reach u otros constructos no se transfieren automáticamente a A_B1.

### 2.1 Regla conservadora recomendada

Hasta que exista una estipulación DGP específica, no se debe fabricar ningún ? funcional. En una historia sintética completa y determinista, Generator debe derivar 1 o 0 de la secuencia funcional efectiva. El soporte tri-valuado de DEC-C10-100 y sus bounds se conserva; que una ejecución completamente determinada tenga n?=0 no invalida la regla.

En el futuro, ? solo podrá aparecer si un contrato DGP explícito define un estado de indeterminación funcional propio de A_B1, con condición semántica y provenance reservada para Evaluator. No podrá originarse en:
- ausencia, pérdida, lag, invalidez o cobertura S3;
- falta de ENABLED/PROFILE, eventos o timestamps por omisión del modelo/harness;
- eventos no modelados, soporte temporal no acotado o una frontera sin convención;
- incapacidad de Analyzer para observar o clasificar;
- cualquier fallo de implementación o de integridad del Generator.

Esta regla evita convertir carencias de especificación en UNKNOWN científico. No decide qué condición intrínseca podría justificarlo; no se ha encontrado una ya aceptada y no se inventa aquí.

## 3. Convención de frontera: precedencia y propuesta

DEC-C10-102 exige asignación determinista, única y versionada, pero no selecciona una convención concreta. DGP §49 y plan §§16.193.4, 16.195 y 16.198.2 recomiendan de forma consistente intervalos internos semiabiertos: el evento en una frontera interna pertenece al intervalo que comienza allí; el último intervalo incluye T*. No se encontró adopción posterior en el Decision Log hasta DEC-C10-103 ni una DEC autónoma que la eleve a aceptada.

### 3.1 Propuesta para aceptación expresa

Con b_0=t0 y b_K=T*:
- intervalos k=1,…,K−1: [b_{k−1},b_k);
- intervalo final k=K: [b_{K−1},b_K].

Un evento exactamente en b_j, para 0<j<K, pertenece al intervalo que comienza en b_j. Un evento en T* pertenece al último intervalo. Un episodio que cruza una frontera afecta a cada intervalo cuyo periodo de incumplimiento intersecte. La convención se versiona antes de materializar cualquier rejilla.

La propuesta resuelve únicamente la asignación temporal. No fija t0, T*, K, Δ, unidad, frecuencia, duración mínima, detectabilidad ni seguimiento; tampoco altera la regla de continuidad estricta.

## 4. Dictamen y decisión pendiente

- **UNKNOWN:** no hay base para crear un mecanismo generador concreto. Recomendación: regla conservadora de §2.1; conservar el valor ? y bounds, pero no emitir ? salvo estipulación DGP explícita, tipada y con provenance.
- **Frontera:** propuesta semiabierta consistente con el contrato existente, pero requiere aceptación expresa antes de considerarse adoptada/versionada.

No se crea DEC-C10-104 ni se cambia el Decision Log: ambos asuntos permanecen propuestos hasta aceptación. Una respuesta afirmativa permitiría registrar la convención como decisión complementaria y cerrar el docket; no autorizaría código, schema físico, generación, pruebas ni ejecución.

## 5. Consecuencia para el cierre

Tras resolver la aceptación pendiente, el siguiente artefacto será el crosswalk de implementación de requisitos ya definidos hacia Generator → TruthBundle → Sealer → Analyzer → Evaluator. Será una trazabilidad de conformidad, no una nueva especificación temporal ni autorización de implementación.

## 6. Límites y autorización

No modifica DEC, DGP base, plan base, schemas, código, tests, workflows, IDs, RMA, Evidence→Claim Matrix, STATUS, main ni PR base. No ejecuta código, validadores, workflows, generación, simulación, calibración o estimación.

scientific_execution=false  
execution_authorized=false
