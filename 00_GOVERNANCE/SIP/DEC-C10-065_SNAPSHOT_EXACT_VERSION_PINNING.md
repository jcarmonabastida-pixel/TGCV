# DEC-C10-065 — Pinning exacto de revisión SNAPSHOT

**Fecha:** 2026-11-05  
**Estado:** ACCEPTED — decisión expresa del usuario  
**Ámbito:** C10-S / U_G / Opción A  
**Antecedentes:** DEC-C10-059…064; OAS-02 del informe de reconciliación integral.

## Decisión

Se aprueba incorporar el campo obligatorio `snapshot_object_record_id` en NODE, EDGE, ROUTE, PREDICATE y ROUTE_STEP, además de `snapshot_id`.

En cada uno de esos cinco registros, la pareja:

`(snapshot_id, snapshot_object_record_id)`

debe referenciar mediante FK compuesta:

`SNAPSHOT(snapshot_id, object_record_id)`

SNAPSHOT mantiene su versionado observacional conforme a DEC-C10-062. `snapshot_id` identifica el snapshot semántico; `snapshot_object_record_id` identifica la revisión física exacta. No se permite resolver la referencia por timestamp, última versión, orden de inserción ni fallback.

## Reconciliación de referencias

- EDGE.source/target NODE: deben fijar el mismo snapshot semántico y la misma revisión de SNAPSHOT, además del registro NODE exacto.
- PREDICATE→ROUTE: misma revisión exacta de SNAPSHOT y registro ROUTE exacto.
- ROUTE_STEP→ROUTE/NODE/EDGE: misma revisión exacta de SNAPSHOT y registros exactos de cada objeto.
- SNAPSHOT→NODE raíz: conserva la FK compuesta al NODE raíz mediante `unit_object_record_id`, incluyendo snapshot_id; la revisión NODE debe corresponder al snapshot que la referencia. La circularidad se resolverá con FK diferibles o mecanismo transaccional equivalente, sin debilitar integridad.

## No cambia

No cambian las identidades semánticas, `object_record_id`, `object_version`, `supersedes_record_id`, la distinción entre revisión observacional y cambio material, ni los contratos de evidencia/adjudicación. ROUTE_STEP sigue siendo relación de secuencia y no una sexta tabla de objetos versionados.

## Condiciones de cierre

La decisión resuelve OAS-02 a nivel de arquitectura documental. No acredita todavía:
- que todas las tablas, encabezados, matrices, crosswalks y contratos estén reconciliados;
- que las claves candidatas compuestas estén declaradas en orden compatible con las FKs;
- compatibilidad con un motor relacional concreto;
- soporte de FK diferibles/transacción atómica para la circularidad;
- constraints, parser, validadores, fixtures o pruebas negativas;
- revisión independiente o schema freeze.

**Estado resultante:** OAS-02 = RESOLVED_DOCUMENTARILY / TECHNICAL_VALIDATION_PENDING. UG-SCH-10 permanece OPEN. `scientific_execution=false`; `execution_authorized=false`.
