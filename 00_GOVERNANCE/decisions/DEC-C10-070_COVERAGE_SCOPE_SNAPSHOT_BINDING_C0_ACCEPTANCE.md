# DEC-C10-070 — Aceptación del binding C0 para scopes de cobertura C10-S

**Fecha:** 2026-11-07  
**Estado:** ACCEPTED — decisión de diseño documental condicionada  
**Ámbito:** C10-S; integridad de COVERAGE_REGISTER↔SNAPSHOT para scopes de cobertura.  
**Base:** IAM §19.8; plantilla U_G §18.7; maestro C10-S §182; alternativas C0/C1/C2.  
**Autorización de implementación/validación ejecutable/ejecución científica:** `false`

## 1. Decisión aceptada

El usuario acepta **C0** como solución documental provisional para vincular scopes de cobertura a snapshots, manteniendo el esquema físico vigente. Cada `coverage_scope_id` C10-S deberá identificar una única tupla exacta:

(contract_id, contract_version, instance_id, instance_version, snapshot_id, snapshot_object_record_id, stage_key, route/route_id, object_class).

La tupla, la regla de enumeración y la versión del universo se registran en `universe_definition/version`. Cada registro que referencia el scope debe coincidir con esa tupla. El control independiente deberá comprobar, como mínimo, igualdad del binding, unicidad, cardinalidad, referencias huérfanas, scopes no usados cuando deban existir y conflictos entre registros.

## 2. Alcance y condición

C0 conserva el esquema actual y **no proporciona integridad relacional/FK compuesta**. Su estado es `CONDITIONAL` hasta que el control independiente esté especificado, implementado bajo autorización, ejecutado y auditado antes de Design Freeze. Un resultado estático o una declaración documental no se presentará como enforcement de base de datos.

El control deberá preservar separación por snapshot, etapa, ruta y clase CMP/PAR/REF/RUL/MET; no podrá fusionar denominadores ni convertir cobertura NONE/PARTIAL/UNKNOWN en ausencia. REF=0 seguirá requiriendo enumeración exhaustiva. La regla de cobertura COMPLETE continúa siendo relativa al universo operativo declarado y versionado.

## 3. Alternativas no aceptadas

- **C1:** ampliar COVERAGE_REGISTER con snapshot_id/snapshot_object_record_id y FKs compuestas. No aceptada ni autorizada; podría reconsiderarse mediante nueva decisión tras revisar DDL completo, ciclos con SNAPSHOT.coverage_scope_id, legacy y compatibilidad del motor.
- **C2:** tabla puente. No aceptada; no recomendada salvo demostración de inviabilidad de C1.

## 4. Separación de decisiones y límites

Esta decisión no reabre DEC-C10-065/Opción A sobre pertenencia versionada del grafo a SNAPSHOT; su validación física conserva su gate técnico. Tampoco acepta ni congela la codificación `SNAPSHOT.scope`, ni modifica `SNAPSHOT.phase`.

No crea scopes, snapshots, filas de cobertura, fixtures, DDL ni controles ejecutables. No acepta IAM, mapping, serialización/MET, oráculo o evidencia. No constituye Design Freeze ni autoriza implementación, validación ejecutable, simulación o ejecución científica.

`scientific_execution=false`; `execution_authorized=false`.
