# C10-S — Reconciliación UG-SCH-10: pertenencia a snapshot y referencias versionadas

**Estado:** PROPOSAL / NOT ACCEPTED / NOT FROZEN  
**Fecha:** 2026-11-05  
**Ámbito:** U_G; NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT y referencias entre registros.  
**Hallazgo:** UG-SCH-10 — OPEN / DESIGN_RECONCILIATION_REQUIRED.  
**Base:** DEC-C10-059…062; contratos de identidad/versionado/snapshot y de ΔT_acc; plantilla U_G vigente.  
**Naturaleza:** comparación de alternativas. No modifica decisiones aceptadas ni autoriza implementación o ejecución.

## 1. Problema

El esquema identifica objetos semánticos y registros versionados, pero no define completamente la composición exacta de cada snapshot ni fija todas las referencias del grafo a registros/versiones concretos.

Debe resolver:
1. Pertenencia: qué registro de NODE, EDGE, ROUTE y PREDICATE forma parte de cada snapshot.
2. Extremos: EDGE debe referir las versiones concretas de NODE usadas como origen y destino.
3. Secuencia: ROUTE debe resolver cada paso ordenado a una versión concreta de NODE o EDGE.
4. Predicados: PREDICATE debe referir la versión exacta de ROUTE que evalúa.

Timestamp, coverage_scope_id, IDs semánticos aislados y orden de filas no bastan. Nunca se infiere que la versión más reciente pertenece al snapshot.

## 2. Restricciones históricas que no se reabren

- DEC-C10-059 conserva SNAPSHOT→NODE mediante la FK compuesta (unit_object_record_id, unit_id) → NODE(object_record_id, node_id), y exige semantic_role=LOGICAL_SERVICE_UNIT.
- DEC-C10-060 conserva el vocabulario controlado de semantic_role y un nodo raíz lógico único por unidad/snapshot/scope.
- DEC-C10-061 conserva las referencias polimórficas tipadas y la procedencia normalizada.
- DEC-C10-062 conserva object_record_id único por tabla, object_version positivo/secuencial por identidad semántica, supersession inmediato y lineal e historial inmutable.
- El contrato de snapshots exige identidad, frontera, granularidad, catálogo y mapping explícitos antes de calcular diffs. ΔE_T permanece separado de ΔT_acc*.
- Las diez tablas son el inventario documental vigente; añadir una relación requiere justificación y aceptación expresa. No se presume que diez sea un límite ontológico inamovible.

## 3. Alternativas

### Opción A — registros de grafo ligados directamente a snapshot

Cada fila de NODE, EDGE, ROUTE y PREDICATE representa la observación versionada de ese objeto semántico en un snapshot concreto.

Cambios lógicos:
- Añadir snapshot_id a NODE, EDGE, ROUTE y PREDICATE, con FK a SNAPSHOT.
- Declarar UNIQUE(snapshot_id, object_record_id) en cada tabla, además de las claves semánticas/versionadas.
- Cada objeto semántico observado en otro snapshot genera un nuevo registro inmutable y un nuevo object_version, incluso si sus propiedades estructurales no cambiaron. Esto registra una nueva observación, no un cambio real de configuración.
- EDGE incorpora source_node_record_id y target_node_record_id; FKs compuestas con snapshot_id resuelven a registros NODE del mismo snapshot.
- PREDICATE incorpora route_record_id; FK compuesta con snapshot_id a ROUTE.
- Crear ROUTE_STEP con route_record_id, snapshot_id, step_index y una referencia tipada exactamente-una a NODE o EDGE por paso. UNIQUE(route_record_id, step_index); FKs compuestas fijan el mismo snapshot.
- route_id, node_id y edge_id permanecen como identidades semánticas; las nuevas referencias fijan el registro concreto.
- Se conserva la FK raíz SNAPSHOT→NODE de DEC-C10-059 y se extiende para comprobar que la versión raíz corresponde al snapshot.

Ventajas:
- Correspondencia directa entre cada registro observado y un snapshot.
- FKs compuestas pueden impedir referencias cruzadas entre snapshots.
- Se conserva identidad semántica y se distingue observación de versión/build/hash técnica.
- No exige una tabla genérica de pertenencia; solo ROUTE_STEP para la secuencia ordenada.

Costes/riesgos:
- Repite filas de objetos no cambiados entre snapshots; object_version identifica revisiones de registro/observación, no exclusivamente cambios materiales.
- Debe explicitarse que un nuevo registro por snapshot no implica ΔT_acc*.
- SNAPSHOT→NODE raíz y NODE→SNAPSHOT crean dependencia circular. El diseño debe declarar cómo se resuelve transaccionalmente (p. ej., constraints diferibles si el motor lo soporta) sin relajar integridad.
- ROUTE_STEP es una undécima tabla operativa y requiere dominio, cardinalidad, orden, unicidad y reglas de inicio/fin.

### Opción B — relación normalizada SNAPSHOT_MEMBER

NODE, EDGE, ROUTE y PREDICATE conservan registros versionados independientes; SNAPSHOT_MEMBER asocia cada snapshot con los registros que contiene. La pertenencia es muchos-a-muchos: un registro inmutable puede aparecer en más de un snapshot.

Cambios lógicos:
- Añadir SNAPSHOT_MEMBER(snapshot_member_id, snapshot_id, member_type, target_*_record_id...) con FKs tipadas exactamente-una a NODE/EDGE/ROUTE/PREDICATE y UNIQUE por snapshot/tipo/registro.
- EDGE debe fijar, para cada snapshot, los miembros NODE concretos que actúan como extremos. Se necesita una relación de binding de extremos o contrato equivalente que compruebe que los miembros origen/destino y el miembro EDGE pertenecen al mismo snapshot.
- ROUTE requiere ROUTE_STEP para ordenar referencias a miembros concretos NODE/EDGE.
- PREDICATE debe fijar el miembro ROUTE exacto.
- Reconciliar la relación con el vínculo raíz SNAPSHOT→NODE de DEC-C10-059, garantizando que el NODE raíz también es miembro del snapshot.

Ventajas:
- Separa identidad del objeto de pertenencia a una captura.
- Reutiliza el mismo registro inmutable en varios snapshots sin crear revisiones repetidas.
- Modela explícitamente una relación potencialmente muchos-a-muchos.

Costes/riesgos:
- Añade al menos SNAPSHOT_MEMBER y ROUTE_STEP; puede requerir otra relación para binding de extremos por snapshot.
- Referencias tipadas y controles de mismo-snapshot aumentan la complejidad de claves y constraints.
- El nodo raíz requiere comprobación adicional de coherencia con SNAPSHOT_MEMBER.
- No elimina la necesidad de versionar relaciones cuando cambian extremos o correspondencias.

### Opción C — manifiesto serializado por snapshot

Guardar dentro de SNAPSHOT o en ordered_node_edge_sequence listas/JSON de IDs y versiones.

Ventaja: menor número aparente de tablas y fácil exportación.

Rechazo como solución canónica:
- No permite FKs ordinarias por cada elemento.
- Un parser externo tendría que reproducir integridad referencial, exclusividad, unicidad y mismo-snapshot.
- Facilita referencias huérfanas, duplicadas, mal tipadas o ambiguas.
- Convierte un contrato relacional en una convención de serialización.

Puede servir como formato de intercambio derivado, nunca como fuente canónica de integridad.

### Opción D — inferencia por timestamp, coverage_scope_id o última versión

No aceptable. Ninguno de estos campos demuestra por sí solo pertenencia exacta ni correspondencia. No resuelve snapshots simultáneos, cambios de cobertura o registros históricos y contradice la regla de no inferir versiones implícitamente.

## 4. Comparación resumida

| Criterio | A. Snapshot en cada registro | B. SNAPSHOT_MEMBER | C. Manifiesto serializado | D. Inferencia temporal |
|---|---|---|---|---|
| Pertenencia inequívoca | Sí, directa | Sí, relacional | Parcial, validación externa | No |
| Reutilización de registro inmutable | No, crea observación/versionado por snapshot | Sí | Sí, sin FK | Indeterminada |
| FKs entre versiones concretas | Sí, compuestas | Sí, mediante miembros/bindings | No ordinarias | No |
| Secuencia ROUTE verificable | Requiere ROUTE_STEP | Requiere ROUTE_STEP | Parser externo | No |
| Complejidad de esquema | Media | Alta | Baja en apariencia, alta en validación | Baja, inválida |
| Compatibilidad con DEC-C10-062 | Compatible si object_version es revisión del registro observacional | Compatible directamente | Parcial | Incompatible |

## 5. Recomendación provisional

**Recomiendo Opción A**, condicionada a cerrar la semántica de object_version y la integridad de la FK raíz circular.

Razones:
1. Los registros actuales contienen observed_state, timestamp, cobertura y referencias de evidencia; representan observaciones contextualizadas, no únicamente definiciones abstractas reutilizables.
2. El versionado secuencial de DEC-C10-062 puede representar revisiones de registro/captura sin afirmar que la configuración subyacente cambió. La versión/build/hash técnica sigue siendo un campo separado.
3. La asociación directa snapshot_id facilita auditar pertenencia y establecer FKs compuestas de mismo-snapshot.
4. Solo añade una relación normalizada nueva, ROUTE_STEP, frente a la mayor complejidad de SNAPSHOT_MEMBER y sus bindings.
5. Evita convertir listas serializadas en fuente de integridad.

Condiciones para aceptar A:
- Definir object_version como versión del registro observacional por identidad semántica, no como indicador de cambio material del objeto.
- Un nuevo snapshot crea nuevos registros de observación para los objetos incluidos; la ausencia de cambio se determina comparando propiedades/mappings, no por igualdad del número de versión.
- Los registros históricos nunca se reescriben.
- FKs de EDGE, ROUTE_STEP y PREDICATE fijan referencias exactas y mismo-snapshot.
- Resolver explícitamente la dependencia circular SNAPSHOT↔NODE raíz.
- ROUTE_STEP contiene referencias tipadas exactas, índices únicos/ordenados y reglas de secuencia predefinidas.
- El contrato de diff separa nuevo registro/captura de cambio estructural ΔT_acc* y de cambio de evidencia ΔE_T.

Opción B debe mantenerse como alternativa si reutilizar una misma fila inmutable en múltiples snapshots resulta requisito esencial. No se recomienda C ni D como esquema canónico.

## 6. Efecto sobre decisiones y contratos existentes

Esta propuesta no altera DEC-C10-059…062. Si se acepta Opción A, será necesario:
- añadir snapshot_id a NODE/EDGE/ROUTE/PREDICATE;
- añadir referencias de registro exactas en EDGE y PREDICATE;
- normalizar ROUTE_STEP;
- precisar la FK SNAPSHOT→NODE raíz y la circularidad;
- revisar §12.10, encabezados e IAM/FP crosswalk;
- actualizar el contrato de identidad/snapshot para distinguir versión observacional de versión/build técnica.

No se propone cambiar objeto experimental, F*, DGP causal, estimandos, intervención, Outcome o Value.

## 7. Estado y límites

Estado histórico actualizado: la Opción A fue aceptada semánticamente mediante DEC-C10-065 y propagada al contrato U_G vigente (§15 de la plantilla). Este documento conserva la comparación A/B/C/D como antecedente de diseño; no debe leerse como estado actual ni como autorización de implementación. La validación física/compatibilidad de motor sigue pendiente en su gate técnico separado.

No se han creado instancias U_G, inventarios reales, fixtures, truth accesible al analizador, parser, constraints, simulaciones ni experimentos. No se ha ejecutado validación técnica. Se mantienen scientific_execution=false y execution_authorized=false.
