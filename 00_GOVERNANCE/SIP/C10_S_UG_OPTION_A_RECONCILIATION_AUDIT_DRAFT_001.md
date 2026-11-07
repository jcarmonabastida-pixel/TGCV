# C10-S — Auditoría de reconciliación integral de Opción A en U_G

**ID:** C10-S-UG-OPTION-A-RECON-AUDIT-001  
**Fecha:** 2026-11-05  
**Estado:** DOCUMENTARY AUDIT IN PROGRESS / AUTHOR-ASSISTED / NOT INDEPENDENT / NOT TECHNICALLY VALIDATED  
**Rama examinada:** `research/c10-s-consolidation-draft`  
**PR:** #116, Draft; base `research/c10-d1-protocol-draft`, head `research/c10-s-consolidation-draft`.  
**Límite:** sin modificación de `main`; sin parser, DDL, fixtures, validadores, inspección de sistemas ni ejecución científica.

## 1. Alcance y fuentes examinadas

Se contrastaron la plantilla U_G, Opción A y DEC-C10-064, la matriz de claves §12.10, los contratos de identidad/versionado, nodo raíz lógico, referencias tipadas, crosswalk IAM/FP, autoauditoría SR-01…20 y checklist de revisión independiente.

La auditoría es documental y asistida por la autoría. No constituye revisión independiente R1/R2 ni validación física.

## 2. Resultado de control formal

La plantilla contiene 19 tablas Markdown. El control programático confirma que encabezado, separador y filas de esquema presentes mantienen el mismo número de columnas en las 19; no se detectaron nombres de columna duplicados dentro de esos encabezados.

Conteos de las tablas físicas principales:
- NODE: 32 columnas.
- EDGE: 35.
- ROUTE: 30.
- ROUTE_STEP: 8.
- PREDICATE: 27.
- SNAPSHOT: 26.
- EVIDENCE_REGISTER: 18.
- CLAIM_EVIDENCE_LINK: 15.
- COVERAGE_REGISTER: 15.
- EVALUATOR_ASSESSMENT: 18.
- ADJUDICATION_REGISTER: 17.

**Dictamen:** PASS_FORMAT_ONLY. El resultado no demuestra compatibilidad entre encabezados, claves, FKs, dominios, cardinalidades o contratos.

## 3. Hallazgos materiales

### OAS-01 — Contratos heredados no reconciliados en §12.7–§12.10
**Severidad:** CRITICAL / BLOCKS SCHEMA CLOSURE.

La plantilla §13–14 añade snapshot_id, referencias exactas y ROUTE_STEP, pero el contrato normalizado §12.7–§12.10 conserva formulaciones previas:
- §12.7 no incluye snapshot_id ni las nuevas referencias exactas en los campos comunes/extensiones;
- §12.8.12 conserva la FK raíz histórica `(unit_id, unit_object_record_id) → (node_id, object_record_id)` sin la dimensión snapshot_id aprobada en §13.4;
- §12.10 mantiene para EDGE extremos por IDs semánticos, ROUTE secuencia como referencia no normalizada, PREDICATE route_id semántico y SNAPSHOT FK raíz sin snapshot_id;
- la matriz no enumera las claves candidatas compuestas necesarias para FKs de mismo snapshot en NODE/EDGE/ROUTE/PREDICATE ni integra todas las referencias nuevas.
  
La prevalencia de §13–14 no es sustituto de reconciliar físicamente las definiciones canónicas. Deben quedar una sola definición normativa y crosswalks coincidentes.

### OAS-02 — Pinning exacto de la versión de SNAPSHOT no resuelto
**Severidad:** CRITICAL / ARCHITECTURAL DECISION REQUIRED.

DEC-C10-062 incluye SNAPSHOT entre las cinco tablas versionadas: `snapshot_id` es identidad semántica, `object_record_id` identidad de fila y `object_version` versión secuencial. La plantilla SNAPSHOT permite, por tanto, más de una fila/versión para un mismo `snapshot_id` (UNIQUE(snapshot_id, object_version)).

Sin embargo, NODE/EDGE/ROUTE/PREDICATE y ROUTE_STEP solo contienen `snapshot_id`. Una FK desde esos registros a SNAPSHOT.snapshot_id no puede identificar inequívocamente una revisión concreta si hay varias versiones de SNAPSHOT con el mismo ID semántico. Además, una FK a una columna no única no es implementable como FK relacional ordinaria.

**Resolución recomendada para decisión:** añadir `snapshot_object_record_id` obligatorio a NODE, EDGE, ROUTE, PREDICATE y ROUTE_STEP, junto a `snapshot_id`; declarar en SNAPSHOT la clave candidata UNIQUE(snapshot_id, object_record_id); y fijar cada registro hijo mediante FK compuesta (snapshot_id, snapshot_object_record_id) → SNAPSHOT(snapshot_id, object_record_id). El nodo raíz NODE quedaría ligado al mismo registro SNAPSHOT y SNAPSHOT conservaría su FK exacta al NODE raíz; la circularidad completa se comprobaría al COMMIT mediante constraints diferibles. Debe comprobarse la compatibilidad de esta estructura con el contrato de identidad/versionado y la unicidad de raíz.

Alternativa: declarar `snapshot_id` único e inmutable y eliminar la posibilidad de múltiples versiones de SNAPSHOT con igual ID semántico. Esto exigiría revisar DEC-C10-062 y el significado de object_version para SNAPSHOT. No se adopta ninguna alternativa sin decisión expresa.

### OAS-03 — Claves candidatas compuestas insuficientemente declaradas
**Severidad:** HIGH / BLOCKS PHYSICAL DESIGN.

§13.1 enumera claves candidatas de NODE, pero no define un inventario completo y simétrico para EDGE, ROUTE, PREDICATE, SNAPSHOT y ROUTE_STEP. Las FKs compuestas descritas requieren claves destino explícitas, por ejemplo:
- NODE por snapshot y registro exacto más identidad semántica;
- ROUTE por snapshot y registro exacto más route_id;
- EDGE por snapshot y registro exacto más edge_id;
- SNAPSHOT por snapshot_id y object_record_id;
- ROUTE_STEP por ruta exacta, snapshot y posición.

La matriz §12.10 debe enumerar cada UNIQUE/PK referenciado y las FKs origen/destino, con orden de columnas coincidente. No basta describirlas en prosa.

### OAS-04 — ROUTE conserva secuencia serializada en el encabezado físico
**Severidad:** HIGH.

El encabezado ROUTE aún contiene `ordered_node_edge_sequence`, aunque §13.5 establece ROUTE_STEP como fuente canónica y permite la secuencia serializada solo como vista/export derivado. Debe retirarse del registro físico canónico o marcarse explícitamente como atributo calculado no persistido. Mantener dos fuentes persistidas genera riesgo de divergencia.

### OAS-05 — Crosswalk IAM/FP solo propagado en prosa
**Severidad:** HIGH.

El addendum DEC-C10-064 del field-to-column crosswalk enumera los nuevos campos, pero no actualiza la tabla normativa atributo→columna ni la correspondencia de claves/FKs. El crosswalk EDGE mantiene referencias semánticas como descripción previa y solo añade una nota narrativa. Se requiere una tabla campo→tabla.columna→tipo de relación→clave destino→regla mismo-snapshot, además de actualizar las entradas EDGE/PREDICATE/ROUTE_STEP.

### OAS-06 — Artefactos de estado y revisión obsoletos
**Severidad:** MEDIUM.

El documento de resolución Opción A conserva frases “pending acceptance” y “will be applied”; DEC-C10-064 ya aceptó el detalle y la plantilla ya contiene §13–14. El checklist independiente y la autoauditoría SR-01…20 describen una revisión estática de diez tablas previa a ROUTE_STEP/Opción A. Deben actualizarse como alcance histórico y no presentarse como auditoría vigente de la versión actual.

### OAS-07 — Estado de PR y destino de integración
**Severidad:** GOVERNANCE / INFORMATION.

PR #116 está abierto y Draft, pero su base es `research/c10-d1-protocol-draft`, no `main`. Por tanto, PR #116 no es una propuesta de merge directo a main. Se conserva la regla de no promover a main sin reconciliación y autorización explícita.

## 4. Dictamen provisional

- Formato Markdown de las tablas: PASS_FORMAT_ONLY.
- Coherencia integral del esquema: FAIL / NOT CLOSED por OAS-01 y OAS-02.
- Diseño físico ejecutable: NOT ASSESSED; motor no fijado.
- Revisión independiente: NOT STARTED.
- Validación técnica: NOT RUN.
- UG-SCH-10: OPEN.
- Esquema global: SCHEMA_NOT_CLOSED.
- `scientific_execution=false`; `execution_authorized=false`.

## 5. Orden de cierre recomendado

1. Resolver expresamente OAS-02 (pinning exacto de versión SNAPSHOT).
2. Propagar la resolución a encabezados y matriz §12.7–§12.10.
3. Completar todas las claves candidatas y FKs compuestas, con orden exacto de columnas.
4. Retirar la secuencia ROUTE serializada como fuente persistida y completar ROUTE_STEP.
5. Actualizar crosswalk IAM/FP con mapeo explícito campo-columna-clave.
6. Actualizar decisión Opción A, auditoría, plan, maestro, checklist y autoauditoría, conservando trazabilidad histórica.
7. Repetir control estático completo; después, revisión independiente R1/R2.
8. Solo tras cierre documental y autorización separada, fijar motor/formato y ejecutar gate técnico no destructivo con pruebas positivas/negativas y rollback.

No se autoriza inventario real, selección de microdominio, generación de truth, simulación o experimento por esta auditoría.


## 6. Bootstrap y trazabilidad de la operación

La lectura de `main` confirma la cadena canónica vigente: RMA v3.37 y Evidence→Claim Matrix v1.47. El puntero RMA resuelve a `TGCV_RMA_v3.37.md`; el alias `EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md` y el artefacto versionado v1.47 presentan el mismo blob SHA. La traceability CSV declara RMA-v3.37 y CLAIM-MATRIX-v1.47 como CURRENT. STATUS mantiene C10 value linkage OPEN y no autoriza ejecución científica.

Los validadores locales read-only del bootstrap no se ejecutaron: esta sesión no dispone de checkout local montado. No se infiere PASS de validación local. Todas las modificaciones de este trabajo se realizaron exclusivamente en `research/c10-s-consolidation-draft`; `main` no fue modificado.


## 7. Resolución de OAS-02 — DEC-C10-065 (2026-11-05)

El usuario aprueba DEC-C10-065: NODE, EDGE, ROUTE, PREDICATE y ROUTE_STEP incorporan `snapshot_object_record_id` obligatorio junto a `snapshot_id`. Se fija la revisión exacta mediante FK compuesta a SNAPSHOT(`snapshot_id`, `object_record_id`). OAS-02 pasa a **RESOLVED_DOCUMENTARILY / TECHNICAL_VALIDATION_PENDING**.

La plantilla incorpora el campo en los cinco encabezados y sus filas ilustrativas. Se corrigen los recuentos de columnas del separador y fila de esquema para esos cinco registros. La matriz §15 explicita la FK compuesta. No se modifica el contrato de versionado ni se elimina el versionado de SNAPSHOT.

Persisten condiciones de reconciliación:
- actualizar todas las claves candidatas y FKs compuestas con orden exacto de columnas;
- garantizar que NODE/EDGE/ROUTE/PREDICATE/ROUTE_STEP referencian el mismo par snapshot_id + snapshot_object_record_id en todos los enlaces;
- completar SNAPSHOT→NODE raíz y la circularidad diferible/transaccional;
- actualizar todas las tablas normalizadas, crosswalks IAM/FP y contratos de integridad;
- seleccionar motor y probar FKs diferibles, constraints cross-row e inmutabilidad;
- revisión independiente R1/R2.

El dictamen general no cambia: UG-SCH-10 OPEN; esquema no congelado; revisión independiente NOT STARTED; validación técnica NOT RUN; sin ejecución científica.


## 8. Revisión de estado tras §15.2/§15.6 y DEC-C10-065

La plantilla ahora especifica las claves candidatas compuestas y FKs con orden de columnas explícito para:
- pinning de cinco registros a SNAPSHOT;
- EDGE→NODE origen/destino;
- PREDICATE→ROUTE;
- ROUTE_STEP→ROUTE/NODE/EDGE;
- SNAPSHOT→NODE raíz.

OAS-02 queda RESOLVED_DOCUMENTARILY. OAS-03 pasa a SPECIFIED_DOCUMENTARILY / COMPLETENESS_AND_ENGINE_VALIDATION_PENDING. No se declara cierre porque aún debe comprobarse la simetría de claves destino/origen en todas las tablas normalizadas, la circularidad raíz, nulabilidad/CHECKs, unicidad de route_step, continuidad cross-row y compatibilidad física. La auditoría estática de Markdown de 19 tablas se repetirá después de la propagación final.

El hallazgo OAS-01 queda mitigado por §15 como contrato de prevalencia, pero las definiciones históricas §§12.7–12.10 y los crosswalks deben reconciliarse para evitar dos fuentes normativas. OAS-04 está corregido en el encabezado ROUTE; OAS-05 parcialmente actualizado; OAS-06 parcialmente actualizado. OAS-07 permanece como nota de gobernanza del PR #116. UG-SCH-10 OPEN.


## 9. Reconciliación posterior — control de referencias exactas (2026-11-05)

### OAS-08 — ROUTE_STEP omitía el pinning exacto en sus FKs a objetos
**Severidad:** HIGH / DOCUMENTARY CONSISTENCY BLOCKER.

Aunque §§15.1–15.2 y DEC-C10-065 exigen que ROUTE_STEP comparta el par `snapshot_id + snapshot_object_record_id` con ROUTE/NODE/EDGE, las tres FKs enumeradas en §15.3 usaban solo `snapshot_id` más el record ID del objeto. Esa forma permitía una referencia cruzada a una revisión de objeto asociada a otra revisión del mismo snapshot semántico y contradecía el requisito de pinning exacto.

**Corrección documental aplicada:** las FKs de §15.3 se han ampliado para incluir `snapshot_object_record_id` en ambos lados y mantener el mismo orden de columnas que las claves candidatas de §15.2. Se ha actualizado coherentemente el contrato §13.1–§13.5: NODE/EDGE/ROUTE/PREDICATE fijan la revisión exacta; EDGE y PREDICATE conservan sus referencias exactas; ROUTE_STEP incorpora el pinning completo. §13.4 expresa la FK raíz SNAPSHOT→NODE con el mismo orden de columnas que §15.2. §14 queda alineada con los cinco registros dependientes. No se ha modificado DEC-C10-065.

### Reconciliación de §§12.7–12.10
- §12.7 incorpora una nota de precedencia que dirige a §§15.1–15.3 para el pinning Opción A + DEC-C10-065.
- §12.8.12 explicita la FK SNAPSHOT→NODE raíz y la pertenencia de los cinco registros dependientes a la revisión exacta.
- §12.10 queda expresamente clasificada como matriz de baseline histórica para las referencias de snapshot; §15.2 es la matriz física normativa vigente.
- El crosswalk IAM/FP añade §9.3 con las doce relaciones y columnas de origen/destino en orden exacto, incluyendo SNAPSHOT→NODE raíz.

### Control estático repetido
La plantilla contiene 19 tablas Markdown. Los encabezados, separadores y filas presentes mantienen el mismo número de columnas; no se detectan nombres duplicados dentro de los encabezados. Recuento actualizado de las tablas operativas:
- NODE 32; EDGE 35; ROUTE 30; ROUTE_STEP 8; PREDICATE 27; SNAPSHOT 26.
- EVIDENCE_REGISTER 18; CLAIM_EVIDENCE_LINK 15; COVERAGE_REGISTER 15; EVALUATOR_ASSESSMENT 18; ADJUDICATION_REGISTER 17.

**Límite:** PASS_FORMAT_ONLY. No valida que las claves candidatas sean físicamente aceptables, que las FKs sean implementables, ni la circularidad, nulabilidad, dominios, CHECKs, integridad cross-row o semántica. La verificación de las FKs requiere DDL/constraints y pruebas técnicas autorizadas.

### Disposición actualizada
- OAS-01: RESOLVED_DOCUMENTARILY / TECHNICAL_VALIDATION_PENDING — prevalencia explícita de §15 y matriz histórica §12.10 identificada.
- OAS-02: RESOLVED_DOCUMENTARILY / TECHNICAL_VALIDATION_PENDING — DEC-C10-065.
- OAS-03: SPECIFIED_DOCUMENTARILY / COMPLETENESS_AND_ENGINE_VALIDATION_PENDING — las claves/FKs están descritas, pero falta revisión independiente de simetría/completitud y validación del motor.
- OAS-04: RESOLVED_DOCUMENTARILY — `ordered_node_edge_sequence` no figura como columna persistida de ROUTE.
- OAS-05: SPECIFIED_DOCUMENTARILY — crosswalk físico §9.3 añadido; requiere revisión independiente.
- OAS-06: RESOLVED_DOCUMENTARILY / SR_REASSESSMENT_PENDING — checklist y autoauditoría incorporan addenda OAS-08…11 y delimitan sus dictámenes históricos; los SR-01…20 no se recalifican automáticamente.
- OAS-07: OPEN GOVERNANCE NOTE — PR #116 conserva base `research/c10-d1-protocol-draft`, no `main`.
- OAS-08: RESOLVED_DOCUMENTARILY / TECHNICAL_VALIDATION_PENDING — FKs ROUTE_STEP corregidas; el motor debe verificar su implementación.
- OAS-09: RESOLVED_DOCUMENTARILY / TECHNICAL_VALIDATION_PENDING — unicidad semántica condicionada a la revisión exacta.
- OAS-10: RESOLVED_DOCUMENTARILY / TECHNICAL_VALIDATION_PENDING — vistas físicas §4.1 y §6 alineadas con DEC-C10-065.
- OAS-11: RESOLVED_DOCUMENTARILY / TECHNICAL_VALIDATION_PENDING — matriz tipada §15.4/§9.4 explicitada.

**Dictamen global:** UG-SCH-10 OPEN; SCHEMA_NOT_CLOSED; revisión independiente R1/R2 NOT STARTED; validación técnica NOT RUN; no DDL/parser/fixtures; `scientific_execution=false`; `execution_authorized=false`.


### OAS-09 — Unicidad semántica no condicionada a la revisión exacta de SNAPSHOT
**Severidad:** HIGH / DOCUMENTARY KEY-CONSISTENCY BLOCKER.

La propuesta previa incluía `UNIQUE(snapshot_id,node_id)`. Como `snapshot_id` es identidad semántica y SNAPSHOT admite varias revisiones `object_version`, esa clave impediría conservar la misma identidad NODE en dos revisiones distintas del mismo snapshot semántico. Además, las claves compuestas con `object_record_id` no bastan por sí solas para impedir duplicados de un mismo ID semántico dentro de una misma revisión exacta, porque `object_record_id` ya es único.

**Corrección documental aplicada:** se elimina `UNIQUE(snapshot_id,node_id)` y se sustituye por `UNIQUE(snapshot_id,snapshot_object_record_id,node_id)`. Se añaden claves semánticas equivalentes para EDGE, ROUTE y PREDICATE dentro de la revisión exacta. Se mantienen las claves compuestas adicionales con object_record_id que necesitan las FKs tipadas. La corrección se aplica en §§13.1 y 15.2; no modifica DEC-C10-062 ni DEC-C10-065.

**Disposición:** OAS-09 RESOLVED_DOCUMENTARILY / TECHNICAL_VALIDATION_PENDING. La validez física de las claves UNIQUE y la compatibilidad del motor siguen sin probarse.


### OAS-10 — Vistas físicas §4.1 y §6 conservaban FKs sin pinning exacto
**Severidad:** HIGH / DOCUMENTARY CONSISTENCY BLOCKER.

El control de la plantilla mostraba que §15.2 y §15.3 estaban actualizadas, pero dos descripciones de las vistas físicas seguían expresando referencias anteriores:
- ROUTE_STEP §4.1 indicaba genéricamente FKs compuestas solo «con snapshot_id», sin exigir `snapshot_object_record_id`.
- SNAPSHOT §6 describía la FK raíz como `SNAPSHOT(snapshot_id,unit_object_record_id,unit_id) → NODE(snapshot_id,object_record_id,node_id)`, omitiendo que el object_record_id de SNAPSHOT debe fijar `NODE.snapshot_object_record_id`.

**Corrección documental aplicada:** §4.1 exige ahora el par exacto `(snapshot_id,snapshot_object_record_id)` en pertenencia y referencias a ROUTE/NODE/EDGE. §6 expresa la FK raíz completa `SNAPSHOT(snapshot_id,object_record_id,unit_object_record_id,unit_id) → NODE(snapshot_id,snapshot_object_record_id,object_record_id,node_id)`. Se propagan addenda DEC-C10-065 a los contratos especializados de unidad lógica, semantic_role y versionado para que sus formulaciones históricas no compitan con el contrato vigente.

**Disposición:** OAS-10 RESOLVED_DOCUMENTARILY / TECHNICAL_VALIDATION_PENDING. La circularidad SNAPSHOT↔NODE, constraints diferibles, unicidad y FKs siguen sin validación física.


### OAS-11 — El contrato consolidado §15.4 no enumeraba el mapping tipado completo
**Severidad:** MEDIUM / DOCUMENTARY COMPLETENESS.

DEC-C10-061 y los contratos de procedencia/adjudicación ya definían las seis FKs tipadas, la exclusividad por enum, las referencias a EVIDENCE_REGISTER, COVERAGE_REGISTER y las evaluaciones E1/E2. Sin embargo, U_G §15.4 resumía esas reglas sin enumerar las columnas/destinos ni las FKs auxiliares, dejando la matriz normativa consolidada incompleta para cotejo directo.

**Corrección documental aplicada:** §15.4 enumera las columnas y reglas de CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT, ADJUDICATION_REGISTER, EVIDENCE_REGISTER y COVERAGE_REGISTER; crosswalk IAM/FP §9.4 añade el mapping origen→destino. No se alteran DEC-C10-061 ni UG-SR-A01.

**Disposición:** OAS-11 RESOLVED_DOCUMENTARILY / TECHNICAL_VALIDATION_PENDING.
