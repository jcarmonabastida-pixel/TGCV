# C10-S — Contrato de FK de unidad lógica y clasificación boundary_class

**ID:** C10-S-UG-IAM-FK-BOUNDARY-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** DEC-C10-059 ACCEPTED (decisión conceptual y documental); esquema físico aún no implementado ni validado.

## 1. DEC-C10-059 — decisión aceptada

Se acepta incorporar en el registro NODE el campo `boundary_class`, con tres clases sustantivas:
- `P0_CONFIG`: objeto/artefacto de configuración declarativa del servicio.
- `P1_ENVIRONMENT`: objeto/artefacto de realización técnica o estado ambiental.
- `DUAL_P0_P1`: artefacto mixto indivisible sin pérdida de integridad/versionado; usar solo cuando descomponer campo/clave no sea viable.

Se admite `NA` como estado de no aplicabilidad justificada para nodos que no representen objetos/artefactos P0/P1 (por ejemplo, nodos analíticos, oráculo, Outcome/Value o unidad lógica raíz si actúa solo como contenedor de identidad). `NA` no es cuarta clase sustantiva. No se admite null/omisión como sustituto de NA. P2 no forma parte del dominio: sigue siendo frontera causal transversal.

El campo es obligatorio en cada fila NODE, pero su valor podrá ser NA cuando la clasificación P0/P1 no aplique. No sustituye NODE.class ni semantic_role.

## 2. Reconciliación de identidad y FK SNAPSHOT→NODE

La plantilla U_G define NODE con identidad semántica `node_id` y registro versionado `object_record_id`; la clave lógica de fila es la pareja `(object_record_id,node_id)`. Por ello, `SNAPSHOT.unit_id` no puede ser FK suficiente por sí solo.

Se establece:
- `SNAPSHOT.unit_id`: identidad semántica estable de la unidad lógica de servicio; su valor coincide exactamente con NODE.node_id del nodo raíz.
- `SNAPSHOT.unit_object_record_id`: FK que, junto con unit_id, resuelve la fila NODE versionada concreta.
- Restricción compuesta: `SNAPSHOT.(unit_object_record_id, unit_id) → NODE.(object_record_id, node_id)`.
- El nodo NODE referenciado debe tener `semantic_role=LOGICAL_SERVICE_UNIT`.
- Cada snapshot debe referenciar la versión del nodo raíz aplicable al tiempo/scope del snapshot; una revisión posterior del NODE no reescribe retroactivamente el snapshot.
- Todos los snapshots de la misma unidad conservan el mismo unit_id semántico; unit_object_record_id puede cambiar si cambia la versión del registro raíz aplicable.

Esto evita FK huérfanas y resuelve el problema de versionado sin duplicar logical_service_id en todas las tablas.

## 3. Reglas de boundary_class

1. Aplicar P0_CONFIG/P1_ENVIRONMENT a nodos de objetos/artefactos incluidos en el servicio o entorno.
2. Preferir descomposición campo/clave de manifiestos/variables mixtos.
3. DUAL_P0_P1 solo cuando la descomposición rompa integridad, identidad o versionado del artefacto.
4. NA requiere razón documentada en notes/unknowns y no se utiliza para ocultar clasificación desconocida: si el objeto es P0/P1 pero no se sabe cuál, la clasificación queda pendiente/UNKNOWN según el mecanismo de evidencia, no NA.
5. boundary_class no implica observed_state=1, existencia, disponibilidad, accesibilidad, aplicabilidad, Reach, cobertura ni inclusión en una ruta.
6. P2 se deriva del perímetro causal/relaciones, nunca de boundary_class.
7. Las revisiones siguen el versionado U_G: nuevo object_record_id y supersedes_record_id; no sobrescribir filas históricas.

## 4. Cambios de plantilla

- NODE: añadir `boundary_class` después de `class`.
- SNAPSHOT: añadir `unit_object_record_id` inmediatamente después de `unit_id`.
- Mantener sin cambios el resto de tablas, catálogo EDGE, campos de evidencia, estados trivalentes y registros U_G.
- No se crean instancias reales ni IDs de servicio.

## 5. Validación pendiente

La aceptación es conceptual/documental. Antes de considerar el esquema implementado deben comprobarse:
- recuento igual de columnas por encabezado, separador y fila de esquema;
- unicidad y FK compuesta;
- validación de semantic_role en el nodo raíz;
- obligatoriedad y dominio de boundary_class;
- NA con justificación;
- coherencia de object_record_id/object_version/supersedes_record_id;
- parser y validador canónicos;
- compatibilidad con todas las diez tablas U_G y con CLAIM_EVIDENCE_LINK.

No se han ejecutado validadores ni fixtures. No se han creado nodos, snapshots, evidencias ni truth. `scientific_execution=false`; `execution_authorized=false`.


## 6. Addendum DEC-C10-064 — actualización de la FK raíz

Se conserva el contrato de unidad lógica y boundary_class, ampliando la FK raíz para incluir pertenencia al snapshot: SNAPSHOT(snapshot_id, unit_object_record_id, unit_id) → NODE(snapshot_id, object_record_id, node_id). El NODE referenciado debe tener semantic_role=LOGICAL_SERVICE_UNIT. La circularidad con NODE.snapshot_id se valida al COMMIT mediante constraints diferibles y transacción atómica. La compatibilidad del motor es gate técnico obligatorio. Las formulaciones previas que describen la FK solo como (object_record_id,node_id) quedan complementadas por esta regla más específica; no se elimina el pinning exacto.


## 7. Addendum DEC-C10-065 — revisión exacta de SNAPSHOT en la FK raíz

La FK raíz histórica de §§2 y 6 queda especificada, tras DEC-C10-065, como:

`SNAPSHOT(snapshot_id, object_record_id, unit_object_record_id, unit_id) → NODE(snapshot_id, snapshot_object_record_id, object_record_id, node_id)`.

El `object_record_id` de la fila SNAPSHOT es el valor que debe coincidir con `snapshot_object_record_id` del NODE raíz; `unit_object_record_id` resuelve el `object_record_id` exacto de NODE. El NODE raíz debe pertenecer por tanto a la revisión exacta del SNAPSHOT que lo referencia y tener `semantic_role=LOGICAL_SERVICE_UNIT`.

Esta formulación complementa/sustituye cualquier FK raíz anterior que omitiera el pinning exacto. No modifica DEC-C10-059 ni DEC-C10-060; los extiende documentalmente conforme a DEC-C10-065. Circularidad y unicidad física siguen pendientes de motor/constraints y pruebas.
