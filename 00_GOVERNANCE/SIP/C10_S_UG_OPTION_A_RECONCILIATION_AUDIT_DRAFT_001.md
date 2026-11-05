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
- NODE: 31 columnas.
- EDGE: 34.
- ROUTE: 30.
- ROUTE_STEP: 7.
- PREDICATE: 26.
- SNAPSHOT: 26.
- CLAIM_EVIDENCE_LINK: 15.
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
