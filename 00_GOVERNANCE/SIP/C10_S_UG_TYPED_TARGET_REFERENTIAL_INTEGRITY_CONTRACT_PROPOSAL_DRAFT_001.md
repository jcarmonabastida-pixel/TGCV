# C10-S — Propuesta de contrato de referencias tipadas e integridad referencial U_G

**ID:** C10-S-UG-TYPED-REF-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** ACCEPTED DOCUMENTALLY — DEC-C10-061; plantilla actualizada en rama Draft, validación física pendiente.  
**Ámbito:** UG-SCH-04, UG-SCH-05 y UG-SCH-06. No resuelve UG-SCH-07.

## 1. Hallazgos que aborda

- **UG-SCH-04:** `source_provenance` aparece como campo común de objetos en §10.6, pero la procedencia completa ya está normalizada en EVIDENCE_REGISTER.
- **UG-SCH-05:** CLAIM_EVIDENCE_LINK usa `claim_target_id (object_record_id)`, mientras COVERAGE_REGISTER se identifica mediante `coverage_scope_id`.
- **UG-SCH-06:** CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER utilizan referencias polimórficas sin mecanismo físico que garantice destino único y existente.

## 2. Principio de diseño

No utilizar una FK polimórfica basada únicamente en `target_type + target_id` sin constraint que garantice el destino. Se propone representar cada destino admisible mediante una columna FK tipada, con exclusividad verificable. Así se conserva una sola tabla relacional para cada función y se evitan tablas-registro genéricas cuya integridad dependería de lógica externa.

El ámbito de destino de las afirmaciones U_G se limita a:
- NODE.object_record_id
- EDGE.object_record_id
- ROUTE.object_record_id
- PREDICATE.object_record_id
- SNAPSHOT.object_record_id
- COVERAGE_REGISTER.coverage_scope_id

EVIDENCE_REGISTER no es un claim target en esta relación: es el artefacto que respalda la afirmación y se referencia por `evidence_id`.

## 3. CLAIM_EVIDENCE_LINK propuesto

Sustituir:
- `claim_target_type`
- `claim_target_id (object_record_id)`

por:
- `claim_target_type` (enum cerrado: NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT, COVERAGE_SCOPE)
- `target_node_record_id` nullable FK → NODE.object_record_id
- `target_edge_record_id` nullable FK → EDGE.object_record_id
- `target_route_record_id` nullable FK → ROUTE.object_record_id
- `target_predicate_record_id` nullable FK → PREDICATE.object_record_id
- `target_snapshot_record_id` nullable FK → SNAPSHOT.object_record_id
- `target_coverage_scope_id` nullable FK → COVERAGE_REGISTER.coverage_scope_id

Reglas:
1. Exactamente una de las seis columnas target_* debe ser no nula.
2. `claim_target_type` debe coincidir con la única columna no nula.
3. Cada FK debe apuntar a una clave única de su tabla destino.
4. `evidence_id` conserva FK obligatoria a EVIDENCE_REGISTER.evidence_id.
5. Un claim de cobertura debe expresar la dimensión, universo/versionado, denominador y alcance en COVERAGE_REGISTER; `relevance_scope` debe ser compatible, pero no sustituye al registro de cobertura.
6. Las relaciones 0..n se mantienen como múltiples filas CLAIM_EVIDENCE_LINK. `evidence_ref` sigue siendo navegación opcional 0..1.
7. No se acepta destino genérico no tipado ni lista serializada.

La constraint de exclusividad puede expresarse como CHECK (suma de indicadores de no-nulo = 1), más CHECK de correspondencia con claim_target_type. Si el formato físico elegido no soporta CHECK, la implementación deberá aportar mecanismo equivalente verificable y pruebas negativas; no se asumirá integridad por convención.

## 4. Referencias de evaluación y adjudicación

Aplicar el mismo patrón de FKs tipadas a:
- EVALUATOR_ASSESSMENT: sustituir `object_type + object_record_id` por `object_type` enum y seis columnas nullable `target_*_record_id / target_coverage_scope_id`, exactamente una no nula y coherente con el tipo.
- ADJUDICATION_REGISTER: mismo patrón para el objeto evaluado/adjudicado. `evaluator_record_E1` y `evaluator_record_E2` permanecen FKs directas a EVALUATOR_ASSESSMENT.evaluator_record_id.

La adjudicación de cobertura queda permitida si el universo y scope son el objeto de la afirmación; si la adjudicación se refiere a una afirmación concreta, se debe preservar el vínculo CLAIM_EVIDENCE_LINK relacionado y no inferirlo únicamente del scope.

## 5. UG-SCH-04 — procedencia canónica

`source_provenance` es atributo de la fuente/evidencia, no atributo repetido de cada objeto:
- EVIDENCE_REGISTER.source_provenance es canónico y obligatorio cuando exista una evidencia registrada.
- EVIDENCE_REGISTER.source_location_ref, custodian, collection_method/tool_version, scope_id, version_identity, timestamp, integrity, access_lineage y completeness_limitations completan la procedencia.
- NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT no duplican `source_provenance`; sus afirmaciones se conectan a evidencias por CLAIM_EVIDENCE_LINK.
- En registros ? sin evidencia, la procedencia no se inventa: unknown_reason, evidence_status=MISSING y límites de búsqueda/cobertura documentados.
- §10.6 debe dejar de declarar source_provenance como campo común obligatorio en las cinco tablas de objetos. No se elimina del esquema de evidencia.

## 6. Integridad y unicidad requeridas

- `object_record_id` debe ser UNIQUE dentro de cada una de NODE, EDGE, ROUTE, PREDICATE y SNAPSHOT para que las FKs tipadas sean ejecutables.
- `coverage_scope_id` debe ser UNIQUE/PK en COVERAGE_REGISTER.
- `evidence_id`, `claim_evidence_id`, `evaluator_record_id` y `adjudication_id` son PK/UNIQUE de sus tablas.
- `evaluator_record_E1/E2` son FKs directas a evaluator_record_id.
- `adjudication_id` y `evaluator_record_id` en CLAIM_EVIDENCE_LINK conservan FKs directas opcionales.
- La FK compuesta SNAPSHOT→NODE y el predicado `semantic_role=LOGICAL_SERVICE_UNIT` se conservan sin alteración.
- No se presupone unicidad global de object_record_id: la unicidad por tabla y los destinos tipados evitan colisiones entre tablas. UG-SCH-07 deberá decidir expresamente el ámbito canónico y las reglas de supersession.

## 7. Impacto en esquema y compatibilidad

Esta propuesta requiere modificar encabezados y filas de esquema de CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER; actualizar dominios y reglas de §12.8–12.10; corregir §10.6 y el crosswalk IAM. No requiere alterar NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT salvo confirmar UNIQUE por tabla para object_record_id.

La propuesta no introduce una tabla adicional ni una capa semántica persistida. Mantiene EVIDENCE_REGISTER y COVERAGE_REGISTER como registros normalizados independientes.

## 8. Límites

- Aceptada documentalmente por el usuario mediante DEC-C10-061; no congelada ni validada técnicamente.
- No se han creado instancias, claves, registros de evidencia o cobertura.
- No se ha elegido motor/formato ni ejecutado parser, CHECK, FK, fixtures o pruebas.
- La FK tipada es especificación de diseño, no integridad física demostrada.
- UG-SCH-07 (unicidad/versionado/supersedes) permanece separado.
- Autoauditoría: AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT.
- `scientific_execution=false`; `execution_authorized=false`.


## 9. Aceptación y aplicación — DEC-C10-061 (2026-11-05)

El usuario acepta la arquitectura de referencias tipadas y la procedencia canónica. La plantilla U_G de la rama C10-S se actualiza en §§10.6, 11, 12.2, 12.4, 12.5, 12.8, 12.9 y 14.2. La aceptación no declara constraints físicas implementadas ni esquema cerrado.


## 10. Addendum DEC-C10-064 — coexistencia con referencias de snapshot

Las FKs tipadas de CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER permanecen separadas de las FKs interobjeto de Opción A. DEC-C10-064 añade claves candidatas compuestas para fijar mismo snapshot en NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT, pero no cambia la regla de exactamente una FK destino tipada ni el ámbito de unicidad de object_record_id por tabla. La matriz física deberá integrar ambos grupos de restricciones sin colisión.


## 11. Addendum DEC-C10-065 — independencia de las FKs tipadas frente al pinning de SNAPSHOT

DEC-C10-065 añade el pinning exacto `snapshot_id + snapshot_object_record_id` a las relaciones de pertenencia e interobjeto del grafo y completa la FK SNAPSHOT→NODE raíz. Esta ampliación no altera las seis FKs tipadas de CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER: sus destinos siguen siendo object_record_id UNIQUE por tabla o coverage_scope_id PK/UNIQUE, con exclusividad y concordancia de enum. Las FKs tipadas no sustituyen ni heredan implícitamente el snapshot pinning; el objeto de destino queda identificado por su registro exacto y la evidencia/claim se vincula a ese registro.

U_G §15.4 y crosswalk IAM/FP §9.4 consolidan las columnas y destinos. No se modifica DEC-C10-061. CHECK/FK, integridad de instancia y cardinalidad siguen pendientes de validación técnica.
