# C10-S — Gate 146: aceptación semántica de identidad, versionado, regeneración y completitud de EventHistory

**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft  
**Estado:** R146_A_ACCEPTED / R146_B_ACCEPTED / R146_C_ACCEPTED / R146_D_ACCEPTED / LOGICAL_RULES_ACCEPTED / MATERIALIZATION_OPEN / NO_SCHEMA_CHANGE / NO_CODE_CHANGE / NO_TESTS / NO_EXECUTION / NO_DESIGN_FREEZE.

## 1. Acto de aceptación

Se registra la aceptación expresa del usuario de las cuatro reglas propuestas en Gate 146. La aceptación es semántica y lógica para el DGP sintético. No crea DEC-C10 nuevas, no modifica decisiones DEC existentes, no altera el DGP original ni promueve contenido a `main`.

## 2. Reglas aceptadas

### R146-A — Identidad propia de transición truth

Cada transición funcional truth tiene identidad propia, distinta de TID, EID, identificadores de `PROCESS_EVENT`, evidence_id y adjudication_id. Su unicidad se define dentro del ámbito de una EventHistory concreta. TID/EID y otras identidades existentes pueden aparecer como referencias cuando corresponda, pero no sustituyen la identidad de transición.

Dos transiciones en historias potenciales distintas pueden ser semánticamente equivalentes sin ser el mismo acontecimiento. Timestamp, orden de serialización, posición, familia causal o hash no constituyen por sí solos identidad semántica.

### R146-B — Versionado separado

Se distinguen tres niveles:
1. **Versión del DGP:** definición versionada de funciones, reglas y parámetros generadores.
2. **Versión de EventHistory:** realización completa de la historia para un ámbito y potencial determinados.
3. **Versión de reglas de adjudicación:** reglas utilizadas para derivar A_B1 desde la historia.

No se establece un mecanismo general de revisión/versionado independiente por transición. La transición es un hecho generado dentro de una versión concreta de historia.

### R146-C — Regeneración inmutable

Una corrección o regeneración no sobrescribe silenciosamente una historia anterior. Produce una nueva versión de EventHistory y conserva la anterior con su provenance e integridad. La continuidad de identidad entre versiones solo se afirma con correspondencia semántica demostrable; no se infiere por posición, timestamp o igualdad de hash. La repetición determinista y una nueva ejecución bajo las mismas condiciones se distinguen como ejecuciones, aunque sus contenidos puedan resultar idénticos.

### R146-D — Completitud en tres planos

La completitud exige distinguir:
- **Ámbito:** mundo/DGP, versión, unidad, réplica/run, potencial y soporte declarados.
- **Generación:** todas las transiciones funcionales estipuladas para ese ámbito y soporte han sido producidas; no quedan transiciones pendientes u omitidas por Generator/harness.
- **Integridad de representación:** la historia producida se conserva íntegramente y sus referencias/provenance permiten verificarla.

La ausencia de transiciones solo implica persistencia del estado previo cuando la completitud generativa está garantizada. Una historia completa puede contener cero transiciones. Un evento de proceso funcionalmente neutro no es una transición truth. Omisiones, colisiones irresueltas, timestamps inválidos o defectos del harness son defectos de generación/representación y no se recodifican automáticamente como UNKNOWN funcional.

## 3. Reconciliación y límites

Las reglas se aplican a EventHistory y su relación con TruthBundle/Evaluator. No transfieren el modelo de revisiones observacionales de Gates 94–98. No definen schema, nombres de campos físicos, algoritmo de IDs, serialización, hash obligatorio, reloj, rejilla, unidad temporal, soporte numérico, T*, Δ, K, calibración S3 ni mecanismo de matching ejecutable.

TruthBundle debe conservar referencia inequívoca a la versión exacta de EventHistory y a la versión de reglas de adjudicación utilizada para obtener A_B1. El Analyzer no recibe EventHistory ni TruthBundle; el Evaluator accede a la verdad únicamente después del sellado del Analyzer.

R144-A permanece aceptada. R144-B, §51 y parámetros temporales permanecen abiertos.

## 4. Estado de cierre

| Elemento | Estado |
|---|---|
| R146-A identidad | ACCEPTED — lógica |
| R146-B versionado | ACCEPTED — lógica |
| R146-C regeneración | ACCEPTED — lógica |
| R146-D completitud | ACCEPTED — lógica |
| Contrato lógico de EventHistory | Avanza; materialización pendiente |
| Matching entre versiones | Formalización posterior |
| §51 / reloj / soporte temporal | OPEN |
| Schema / código / tests | No autorizados |
| Generación / simulación / ejecución científica | No autorizadas |

## 5. Siguiente gate: Gate 147

Auditar si la completitud generativa de R146-D queda respaldada por el universo de mecanismos y el catálogo de transiciones B1 de §§49–50, sin ampliar silenciosamente su alcance.

La auditoría deberá distinguir:
1. cambios efectivos de ENABLED/PROFILE;
2. pérdida/recuperación de proceso o módulo;
3. pérdida/recuperación de listener/socket/superficie de ingreso;
4. pérdida/recuperación de dependencias cuando altere la capacidad funcional de admisión;
5. insuficiencia/restauración de capacidad o recursos cuando altere esa capacidad;
6. antecedentes de provisión, instalación, verificación, rollback y reinicio que no constituyen por sí mismos incumplimiento;
7. ciclo discreto de solicitud y sus etapas, sin convertir la ausencia de solicitud en fallo.

Punto crítico: comprobar la coherencia entre el contenido de EventHistory fijado en Gate 145 (estado ENABLED/PROFILE y transiciones truth) y las familias funcionales/runtime enumeradas en §50. No resolver por anticipado si una señal runtime constituye transición de estado, condición causal antecedente o evidencia observacional; clasificarla según el contrato y dejar explícita cualquier incompatibilidad. La auditoría debe preservar la separación truth / observed_evidence / evaluation, y no convertir límites de detectabilidad S3 en límites de verdad.

Gate 147 sigue siendo documental y lógico. No autoriza fixtures ejecutables, schema, código, tests, generación, simulación, calibración ni ejecución científica.

`scientific_execution=false`  
`execution_authorized=false`  
`implementation_authorized=false`
