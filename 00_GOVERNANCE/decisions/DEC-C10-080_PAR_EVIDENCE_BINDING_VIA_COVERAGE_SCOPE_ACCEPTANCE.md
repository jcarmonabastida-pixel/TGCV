# DEC-C10-080 — Binding probatorio de filas PAR mediante COVERAGE_SCOPE y localizador lógico

**Fecha:** 2026-11-08  
**Estado:** ACEPTADA — contrato documental lógico  
**Ámbito:** C10-S / IAM / filas PAR / U_G CLAIM_EVIDENCE_LINK y COVERAGE_REGISTER  
**Rama de registro:** `research/c10-s-consolidation-draft`

## 1. Decisión aceptada

Se acepta el perfil de trazabilidad probatoria de las filas PAR sin introducir un destino PAR ni una FK inexistente en U_G:

1. Cada afirmación probatoria sobre una fila PAR se registra en CLAIM_EVIDENCE_LINK con `claim_target_type=COVERAGE_SCOPE` y `target_coverage_scope_id` apuntando al scope PAR exacto (`dimension=C10S_CONFIG_PAR`).
2. La identidad de la fila PAR se expresa mediante un localizador lógico en los campos textuales existentes `claim_statement` y `relevance_scope`. El localizador incluye, como mínimo, `manifest_record_id`, `manifest_record_revision`, `parameter_key`, CMP owner exacto, snapshot/record, `stage_key`, ruta o ausencia justificada y `coverage_scope_id`.
3. Cada fila CLAIM_EVIDENCE_LINK vincula una evidencia exacta de EVIDENCE_REGISTER con una afirmación y una fila PAR. La relación múltiple evidencia×afirmación×fila se representa mediante filas independientes, no mediante listas serializadas ni un campo singular que se interprete como contenedor 1:N.
4. Un control independiente resuelve `manifest_record_id` globalmente conforme a DEC-C10-079 y comprueba revisión/supersession, clave lógica, owner CMP, snapshot, etapa, ruta/scope, `coverage_scope_id`, versión del universo y consistencia del predicado/estado con la evidencia.
5. Si la misma evidencia respalda además una afirmación distinta sobre el CMP owner como objeto, se crea un CLAIM_EVIDENCE_LINK separado con `claim_target_type=NODE` y su FK NODE exacta. No se sustituye ni mezcla el target COVERAGE_SCOPE de la afirmación PAR.
6. El vínculo a COVERAGE_SCOPE no implica que el scope esté COMPLETE. La completitud se adjudica conforme a U_G §12.3 y §18.6, con denominador, enumeración, fuentes válidas, excepciones y revisión.

## 2. Restricciones de esquema y semántica

- Se conservan los destinos actuales de CLAIM_EVIDENCE_LINK: NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT/COVERAGE_SCOPE.
- No se añade target_type PAR, FK PAR, tabla PAR, tabla puente ni columna U_G.
- No se inventa FK desde CLAIM_EVIDENCE_LINK a `manifest_record_id`; su resolución se hace mediante el localizador textual y el control independiente contra el manifiesto IAM versionado.
- `claim_statement` y `relevance_scope` son campos textuales existentes; esta decisión no aprueba gramática física, escaping, canonicalización, parser ni serialización automatizada.
- Los campos singulares `evidence_id`/`claim_evidence_id` que puedan aparecer en el manifiesto documental no sustituyen el registro relacional 1:N de CLAIM_EVIDENCE_LINK ni autorizan listas embebidas. La trazabilidad probatoria completa se conserva en filas CLAIM_EVIDENCE_LINK independientes.
- Un enlace estructural válido no prueba que la evidencia respalde sustantivamente el predicado.

## 3. Estados y fallos

- Identidad o relación contradictoria, ID duplicado, revisión/supersession inválida o mismatch de scope/owner/snapshot/etapa: FAIL.
- Falta de manifiesto, snapshot, scope, evidencia o fuente necesaria para resolver: UNKNOWN / ?.
- Incompatibilidad de versiones sin mapping aprobado: NOT_COMPARABLE.
- NA solo por inaplicabilidad justificada ex ante.
- No se infiere ausencia 0 por falta de vínculo ni por falta de observación.

## 4. Límites

Esta decisión es documental y lógica. No crea registros observados, no declara cobertura, no sella IAM, no cierra el crosswalk PAR↔U_G, no modifica el schema físico, no autoriza DDL, serialización, parser, validator, fixtures, implementación, Design Freeze ni ejecución. Se mantienen `scientific_execution=false` y `execution_authorized=false`.

## 5. Propagación

Prevalece sobre la propuesta §17.4/§19.23/§23/§16.65/§83/§210/§89 en cuanto a su estado: deja de estar pendiente de aceptación y pasa a contrato lógico aceptado. Los detalles de implementación no definidos permanecen OPEN y no se presumen resueltos.
