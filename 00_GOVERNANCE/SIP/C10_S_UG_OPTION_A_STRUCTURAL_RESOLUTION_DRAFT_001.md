# C10-S — Resolución de condiciones estructurales de Opción A para UG-SCH-10

**ID:** C10-S-UG-SNAPSHOT-A-RESOLUTION-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** DESIGN RESOLUTION PROPOSAL / NOT FROZEN / NOT IMPLEMENTED  
**Base:** aceptación del usuario de Opción A; DEC-C10-059…062; plantilla U_G Draft 001.  
**Ámbito:** pertenencia a snapshot y pinning exacto de NODE, EDGE, ROUTE y PREDICATE.

## 1. Decisión de arquitectura registrada

El usuario acepta Opción A como arquitectura de referencia: cada registro observacional de NODE, EDGE, ROUTE y PREDICATE pertenece directamente a un snapshot mediante `snapshot_id`. Se conserva la identidad semántica y se fija cada referencia interobjeto a un `object_record_id` exacto. La secuencia de ROUTE se normaliza mediante ROUTE_STEP.

La aceptación selecciona la arquitectura, no congela aún el esquema ni autoriza su implementación. Esta resolución desarrolla las dos condiciones pendientes y define los límites que deben conservarse al aplicar la arquitectura.

## 2. Condición 1 — semántica de object_version

### 2.1. Definición normativa propuesta

En NODE, EDGE, ROUTE, PREDICATE y SNAPSHOT, `object_version` sigue siendo el contador entero positivo, contiguo y lineal por identidad semántica fijado por DEC-C10-062. Para NODE/EDGE/ROUTE/PREDICATE, bajo Opción A, identifica la **revisión del registro observacional** de esa entidad semántica, no exclusivamente una modificación material de su configuración.

Por tanto:

- Cada aparición de una entidad semántica en un nuevo snapshot genera un nuevo `object_record_id` inmutable y la siguiente `object_version` de esa identidad.
- La fila nueva se vincula al snapshot observado mediante `snapshot_id`.
- `supersedes_record_id` apunta al registro inmediatamente anterior de la misma tabla e identidad semántica, aunque las propiedades observadas sean idénticas.
- La secuencia de versiones se ordena por registro/supersession, no por inferencia de timestamp. El timestamp de observación y `created_at` (record-time) siguen siendo conceptos separados.
- Dos snapshots distintos pueden contener observaciones estructuralmente idénticas de la misma entidad; ello produce registros/versiones diferentes, pero **no implica cambio estructural**.
- El número de versión, el nuevo `object_record_id`, el timestamp o el cambio de snapshot nunca se usan por sí solos como señal de `ΔT_acc*`, `ΔE_T`, cambio de configuración, cambio funcional o cambio de Value.

### 2.2. Regla de comparación

Los diffs se calculan entre snapshots comparables, emparejando identidades semánticas mediante el mapping explícito y comparando las propiedades estructurales declaradas, relaciones, secuencias, predicados y estados pertinentes bajo las reglas congeladas del experimento.

Se separan al menos:

1. **Cambio de observación/registro:** nueva fila, nuevo snapshot o nueva versión sin cambio material demostrado.
2. **Cambio estructural:** diferencia en propiedades/relaciones constitutivas del objeto o del grafo comparable.
3. **Cambio de evidencia:** altas, bajas, conflicto, cobertura o calidad probatoria sin cambio estructural necesariamente asociado (`ΔE_T`).
4. **Cambio de accesibilidad:** derivación de `T_acc` y `ΔT_acc*` mediante universo, predicado de admisibilidad, frontera, granularidad y mapping ex ante; no se identifica con cualquier cambio del grafo.

La comparación no debe usar `object_version`, `object_record_id`, `created_at` ni `timestamp` como variables sustantivas de diferencia.

## 3. Condición 2 — dependencia circular SNAPSHOT↔NODE raíz

### 3.1. Conservación de integridad

Se conserva DEC-C10-059/060: cada SNAPSHOT apunta a la versión exacta del NODE raíz de servicio lógico (`semantic_role=LOGICAL_SERVICE_UNIT`), y cada NODE de Opción A referencia el snapshot al que pertenece.

La FK de SNAPSHOT al NODE raíz se fortalece para comprobar también pertenencia al mismo snapshot:

`SNAPSHOT(snapshot_id, unit_object_record_id, unit_id) → NODE(snapshot_id, object_record_id, node_id)`

NODE deberá exponer la clave candidata compuesta correspondiente. Se mantienen la identidad semántica estable `unit_id`, el pinning exacto `unit_object_record_id` y la unicidad de raíz por unidad/snapshot/scope. No se sustituye la FK por una búsqueda de “última versión”, timestamp, rol sin FK ni validación exclusivamente externa.

### 3.2. Resolución transaccional propuesta

La dependencia es circular y se resuelve sin debilitar las FKs mediante **constraints diferibles al final de una transacción atómica**:

1. Preasignar `snapshot_id`, `unit_id`, `unit_object_record_id` y el resto de identificadores opacos.
2. Insertar SNAPSHOT con la FK compuesta al NODE raíz ya identificada, aunque la fila NODE aún no se haya insertado.
3. Insertar el NODE raíz con `snapshot_id` igual al SNAPSHOT recién creado y `semantic_role=LOGICAL_SERVICE_UNIT`.
4. Insertar los demás registros del grafo y ROUTE_STEP.
5. Validar constraints diferidas y todas las invariantes de cardinalidad/consistencia antes del COMMIT.
6. Confirmar la transacción solo si ambas direcciones de la FK circular y las reglas de raíz única quedan satisfechas; en otro caso, rollback completo.

Las FKs circulares relevantes deben declararse `DEFERRABLE INITIALLY DEFERRED` (o mecanismo transaccional equivalente con garantía de integridad al commit). No se permite desactivar constraints, insertar datos huérfanos confirmados ni posponer la comprobación fuera de la transacción.

### 3.3. Gate de compatibilidad del motor

El motor relacional aún no está fijado en el contrato. Por ello, la solución transaccional queda **resuelta a nivel lógico, condicionada a capacidad física del motor**. Antes de implementar se debe demostrar que el motor elegido soporta FKs diferibles y las claves compuestas requeridas.

Si el motor no soporta diferimiento equivalente, la implementación se detiene. No se debilita la FK ni se introduce un trigger no auditado como sustituto tácito. Se reabre una decisión de arquitectura para evaluar una alternativa que preserve exactamente las garantías de DEC-C10-059/060; Opción B u otra normalización solo podrían adoptarse mediante decisión expresa.

## 4. Referencias exactas entre registros

### 4.1. NODE

Añadir `snapshot_id` FK a SNAPSHOT. Mantener `node_id` como identidad semántica. Claves candidatas mínimas: UNIQUE(`snapshot_id, object_record_id`) y UNIQUE(`snapshot_id, object_record_id, node_id`); además, UNIQUE(`snapshot_id, node_id`) para impedir dos revisiones de la misma identidad semántica dentro de un mismo snapshot.

### 4.2. EDGE

Añadir `snapshot_id`, `source_node_record_id` y `target_node_record_id`. Las FKs compuestas deben resolver cada extremo a NODE del mismo snapshot y comprobar simultáneamente el `node_id` semántico declarado. Se conservan `source_node_id` y `target_node_id` para legibilidad/crosswalk, pero nunca sustituyen el pinning por registro. Una arista no puede unir nodos de snapshots distintos.

### 4.3. PREDICATE

Añadir `snapshot_id` y `route_record_id`. La FK compuesta resuelve a la revisión exacta de ROUTE del mismo snapshot y comprueba la identidad semántica `route_id`. Se conserva `route_id` como identidad semántica; no basta por sí solo para identificar la revisión evaluada.

### 4.4. ROUTE_STEP — relación normalizada de secuencia

Se incorpora ROUTE_STEP como relación operativa adicional necesaria para materializar el orden de cada ruta. Campos mínimos:

- `route_step_id` (identidad opaca de fila) o PK compuesta `(route_record_id, step_index)`;
- `snapshot_id`;
- `route_record_id`;
- `step_index` (entero positivo, único y contiguo por ruta);
- `step_type` (`NODE` o `EDGE`);
- `node_record_id` nullable;
- `edge_record_id` nullable.

Invariantes:
- Cada paso referencia exactamente uno de NODE o EDGE; CHECK de exclusividad y coherencia con `step_type`.
- La FK a ROUTE y la FK tipada a NODE/EDGE incluyen `snapshot_id`; no se admiten pasos cruzados entre snapshots.
- Los índices empiezan en 1, son únicos y contiguos, sin duplicados ni huecos.
- La secuencia representa una ruta ordenada; cuando se compone de nodos y aristas, la arista debe conectar los nodos adyacentes según sus referencias exactas y dirección declarada.
- La validez de secuencia completa es una regla cross-row; requiere constraint/trigger verificable o validador independiente del gate técnico, con pruebas negativas. No se presume garantizada por una FK individual.
- `ordered_node_edge_sequence` no puede seguir siendo una lista libre o serializada como fuente canónica. Puede mantenerse temporalmente como vista/export derivado, nunca como segunda fuente de verdad.

ROUTE_STEP es una relación adicional al inventario previo de diez tablas. Su necesidad y alcance quedan justificados por la secuencia ordenada exigida por la arquitectura aceptada; su inclusión física en la plantilla se realizará al aprobar esta resolución de detalle.

## 5. Restricciones de mismo-snapshot y unicidad

La aplicación de A debe definir claves candidatas compuestas para que las FKs puedan comprobar, en la base de datos, simultáneamente:

- pertenencia del registro al snapshot;
- identidad exacta del registro referenciado;
- coherencia entre el ID semántico conservado y el registro exacto;
- unicidad de una observación de cada identidad semántica por snapshot;
- pertenencia del nodo raíz al mismo snapshot.

No basta una FK aislada a `object_record_id` si la regla exige además mismo snapshot y coincidencia del ID semántico.

## 6. Contrato de diff y no doble conteo

- La pertenencia a snapshot es una propiedad de captura, no una transformación.
- Nueva versión observacional ≠ cambio material.
- Cambio material de NODE/EDGE/ROUTE/PREDICATE ≠ automáticamente cambio de `T_acc`.
- Cambio de `T_acc` requiere el contrato de accesibilidad independiente y outcome-blind.
- `ΔE_T` se mantiene separado de `ΔT_acc*`.
- Las filas de ROUTE_STEP se comparan por ruta semántica, orden y referencias semánticas emparejadas, no por sus IDs opacos o record IDs.
- Los cambios de cobertura, evidencia, evaluación o adjudicación no deben convertirse automáticamente en cambios estructurales.

## 7. Estado, límites y siguientes gates

**Resuelto documentalmente en esta propuesta:** semántica observacional de `object_version`; transacción atómica con FKs diferibles para SNAPSHOT↔NODE raíz; pinning de extremos EDGE; pinning PREDICATE→ROUTE; y estructura/invariantes de ROUTE_STEP.

**Pendiente de aceptación de detalle:** este documento no modifica aún la plantilla U_G ni las decisiones DEC-C10-059…062. La aceptación previa de Opción A no debe interpretarse como aceptación automática de todos los tipos, nombres y constraints físicos aquí propuestos.

**Pendiente de gate técnico posterior:** motor/DDL, soporte de constraints diferibles, constraints compuestas, integridad cross-row de ROUTE_STEP, unicidad/secuencias/supersession, inmutabilidad, parser, pruebas positivas/negativas, rollback y replay de captura.

No se crean instancias, inventario real, truth, fixtures ni datasets. No se ejecutan validadores, parser, constraints, simulaciones ni experimentos. No cambia TGCV Core, RMA, Evidence→Claim Matrix, claims, estimandos, Outcome o Value. Se mantienen `scientific_execution=false` y `execution_authorized=false`.


## 8. Estado actualizado tras DEC-C10-064 y auditoría OAS

DEC-C10-064 acepta documentalmente la resolución de detalle y la plantilla U_G ya incorpora Opción A/ROUTE_STEP. Por tanto, las formulaciones de §7 que indicaban “pendiente de aceptación” y “la plantilla no se modifica aún” quedan supersedidas por la decisión posterior y su aplicación documental.

La auditoría integral OAS identifica un bloqueo adicional no resuelto por la aceptación: SNAPSHOT está versionado bajo DEC-C10-062, pero las filas NODE/EDGE/ROUTE/PREDICATE/ROUTE_STEP solo fijan snapshot_id semántico. No se identifica así una revisión exacta de SNAPSHOT. La solución recomendada es añadir snapshot_object_record_id a cada registro hijo y fijar FK compuesta (snapshot_id, snapshot_object_record_id) → SNAPSHOT(snapshot_id, object_record_id), conservando el pinning del NODE raíz y difiriendo la circularidad completa hasta COMMIT. Esta extensión requiere decisión expresa; no se incorpora unilateralmente.

Estado actual: Opción A y su detalle base aceptados documentalmente; aplicación documental parcial; pinning exacto de versión SNAPSHOT BLOCKED_PENDING_DECISION; esquema no congelado ni implementado; sin validación técnica ni ejecución científica.
