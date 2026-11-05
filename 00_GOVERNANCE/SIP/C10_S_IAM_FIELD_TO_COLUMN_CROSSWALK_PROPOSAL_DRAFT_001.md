# C10-S — Crosswalk de atributos IAM a columnas existentes de U_G

**ID:** C10-S-IAM-FIELD-CROSSWALK-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** propuesta documental parcialmente aceptada mediante DEC-C10-059; plantilla actualizada documentalmente, sin schema freeze ni validación técnica.  
**Base:** DEC-C10-057/058; U_G template §§2–6 y 10–12; auditoría IAM FP/EDGE.

## 1. Propósito

Resolver cómo representar la clasificación del servicio lógico sin duplicar campos ya normalizados en U_G ni introducir columnas por simple conveniencia. La plantilla U_G ya contiene un esquema normalizado común en §12.7 y extensiones por tipo de registro; este documento debe leerse junto a esa sección, que prevalece sobre las vistas abreviadas §§2–6.

## 2. Regla de diseño

- No añadir columnas si un campo existente expresa el mismo concepto sin pérdida semántica.
- No reutilizar una columna con significado distinto (p. ej. `class` no debe confundirse automáticamente con P0/P1).
- No repetir `logical_service_id` en todas las tablas si puede identificarse mediante el nodo raíz de servicio y las relaciones U_G.
- P2 no es una clase de objeto excluyente: se expresa por pertenencia a la frontera causal y relaciones pertinentes, no como `class=P2`.
- Los campos de evidencia, cobertura, adjudicación y procedencia se rigen por U_G §§11–12 y no se redefinen aquí.

## 3. Crosswalk atributo IAM → esquema U_G

| Atributo propuesto | Destino U_G | Dictamen | Justificación/límite |
|---|---|---|---|
| `logical_service_id` | NODE raíz con `semantic_role=LOGICAL_SERVICE_UNIT`; SNAPSHOT.`unit_id` referencia ese ID; EDGE conecta objetos incluidos | Reutilizar, sin columna común nueva | La unidad lógica es un objeto identificable del grafo. No duplicar su ID en todas las filas; verificar que unit_id y node_id usen el mismo espacio de IDs o definir FK explícita. |
| `boundary_class` | Candidato a nueva columna NODE.`boundary_class` con P0_CONFIG / P1_ENVIRONMENT / DUAL_P0_P1 | Brecha real candidata; requiere aprobación antes de schema | No sobrecargar NODE.`class`, que clasifica roles amplios del grafo (frontera, intervención, recurso, externo, etc.) y no equivale a P0/P1. P2 no es valor de este enum. |
| `object_scope` | NODE.`semantic_role` cuando describa el rol semántico; campos tipados existentes en EDGE/ROUTE/PREDICATE para sus respectivas entidades | Reutilizar con vocabulario controlado | No añadir object_scope universal. Definir vocabulario y cardinalidad por tabla; no convertir texto libre en categoría validada sin decisión. |
| `semantic_inclusion_rationale` | NODE.`notes/unknowns`; usar `contract_intent` solo para requisito normativo | Reutilizar, con convención documental | La razón de inclusión no es lo mismo que la intención contractual. No duplicar ambos conceptos en contract_intent. |
| `sensitivity_class` | EVIDENCE_REGISTER.`confidentiality/access_ref` y controles de acceso del repositorio de evidencia | Reutilizar referencia de custodia; no añadir al NODE por defecto | La sensibilidad pertenece al artefacto/fuente y a su régimen de acceso. No registrar secretos ni valores confidenciales en U_G. Si un nodo requiere clasificación intrínseca de seguridad, documentar el caso y proponer extensión separada. |
| P2 / causal boundary membership | Grafo U_G: NODE/EDGE/ROUTE/PREDICATE y coverage_scope_id del universo causal | Sin columna P2 ni clase excluyente | P2 es perímetro analítico transversal. Un objeto P0/P1 puede participar en P2; nodos de asignación, oráculo, evaluación y resultados pueden ser relevantes sin ser contenido P0 ni entorno P1. |
| Parent/child de manifiesto descompuesto | NODE.`parent_catalog_id` para linaje de catálogo; object_record_id/object_version para versión de fila | Reutilizar; no crear EDGE CONTAINS_FIELD | Parent_catalog_id no representa una dependencia causal. Solo crear EDGE si existe relación tipada y el catálogo la admite. |
| Evidencia y procedencia | object tables §12.7 + EVIDENCE_REGISTER + CLAIM_EVIDENCE_LINK | Reutilizar exactamente | evidence_ref es navegación opcional 0..1; CLAIM_EVIDENCE_LINK conserva relación completa 0..n. |
| Cobertura del inventario | coverage_scope_id + COVERAGE_REGISTER | Reutilizar exactamente | No confundir cobertura del objeto con boundary_class ni con observed_state. |

## 4. Propuesta mínima de extensión, pendiente de decisión

La única extensión que parece semánticamente justificada en esta fase es:

**NODE.boundary_class ∈ {P0_CONFIG, P1_ENVIRONMENT, DUAL_P0_P1}.**

Condiciones:
1. Aplica solo a nodos que representan objetos/artefactos dentro del contenido de servicio o entorno.
2. No se aplica a Z, oráculo, evaluador, Outcome/Value u otros nodos analíticos P2-only.
3. P2 se determina por inclusión en la frontera causal y relaciones, no por este campo.
4. DUAL solo cuando un artefacto físico no pueda descomponerse sin perder integridad/versionado; preferir descomposición por campo/clave cuando sea viable.
5. La columna no se añade hasta aceptar el dominio, reglas de obligatoriedad/NA y su relación con NODE.class/semantic_role.
6. La aceptación de la columna no equivale a inventario ni permite rellenar instancias sin evidencia.

Alternativa menos recomendable: codificar P0/P1 en NODE.class. Se desaconseja porque mezcla dos taxonomías distintas y dificulta preservar los roles U_G ya existentes.

## 5. Comprobaciones de consistencia

- NODE lógico de servicio, snapshot.unit_id y enlaces EDGE deben referirse a la misma unidad de migración; la FK exacta sigue abierta.
- boundary_class no reemplaza class ni semantic_role.
- object_scope no debe duplicar route_class, predicate_type ni relation_type.
- La sensibilidad no se resuelve copiando valores secretos o credenciales.
- P2 no puede utilizarse para inferir presencia, accesibilidad, ausencia de alternativas o cobertura completa.
- No añadir una relación de contención no existente al catálogo EDGE.
- Ninguna extensión modifica los estados 1/0/?/NA ni evidence_status/coverage_status.

## 6. Dictamen y siguiente gate

**Dictamen documental:** la mayoría de atributos IAM se pueden mapear a campos U_G existentes o al grafo; no justifican columnas universales nuevas. Existe una única brecha candidata clara: `NODE.boundary_class`, cuya adopción debe decidirse explícitamente.

**Estado histórico supersedido por DEC-C10-059:** boundary_class aceptada y añadida documentalmente; unit_object_record_id incorporado a SNAPSHOT para FK compuesta. No se han creado filas/IDs de inventario ni ejecutado parser/validador; no se ha iniciado captura técnica.

**Siguiente gate:** revisar el esquema completo actualizado, resolver los dominios/vocabularios de semantic_role y boundary_class y preparar validación estructural autorizada. La FK compuesta está definida documentalmente en DEC-C10-059 y en el contrato asociado.


## 7. Resolución — DEC-C10-059

El usuario acepta `NODE.boundary_class` con tres clases sustantivas `P0_CONFIG/P1_ENVIRONMENT/DUAL_P0_P1`. Se incorpora `NA` exclusivamente como no aplicabilidad justificada, no como cuarta clase ni como sustituto de unknown. El campo es obligatorio en NODE y no codifica P2.

La FK se cierra documentalmente con `SNAPSHOT.(unit_object_record_id, unit_id) → NODE.(object_record_id, node_id)`; el nodo destino debe tener `semantic_role=LOGICAL_SERVICE_UNIT`. Se añade `unit_object_record_id` a SNAPSHOT porque `unit_id` aislado no identifica una revisión concreta del registro NODE.

Véase `C10_S_UG_LOGICAL_UNIT_FOREIGN_KEY_AND_BOUNDARY_CLASS_CONTRACT_DRAFT_001.md`. La plantilla se actualiza documentalmente; no se declara implementada ni validada por parser/constraints.


## Addendum — EDGE y semantic_role (2026-11-05)

La plantilla EDGE actualizada utiliza `edge_id`, `atomic_edge_id`, `parent_edge_id`, `source_node_id` y `target_node_id`. El primero es la identidad semántica local de la arista en el registro versionado; atomic_edge_id identifica la relación atómica estable; parent_edge_id conserva E01–E23. Los extremos resuelven a NODE.node_id dentro del scope/versión aplicable. E07 no es arista binaria y E22 no autoriza inventar nodos de selección/ejecución.

El vocabulario de `semantic_role` y el nodo raíz se desarrolla en `C10_S_UG_SEMANTIC_ROLE_AND_LOGICAL_ROOT_CONTRACT_DRAFT_001.md`. El crosswalk N01–N23 no es uno-a-uno y no altera `boundary_class` ni DEC-C10-059. Propuesta pendiente de aceptación.

 
## Addendum — DEC-C10-060 accepted (2026-11-05)

Se acepta el vocabulario controlado de `semantic_role` y el contrato del nodo raíz lógico. La correspondencia N01–N23 → semantic_role no es uno-a-uno y no genera instancias ni aristas. `parent_catalog_id`, `semantic_role` y `boundary_class` permanecen dimensiones distintas. La regla de referencia compuesta SNAPSHOT→NODE se conserva conforme a DEC-C10-059 y requiere validación física futura.


## 8. Reconciliación de procedencia y referencias tipadas — DEC-C10-061

- `source_provenance` pertenece al registro normalizado EVIDENCE_REGISTER; no es columna común duplicada en NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT.
- CLAIM_EVIDENCE_LINK usa una FK destino tipada entre NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT/COVERAGE_REGISTER, con exclusividad exactamente-una y coherencia de claim_target_type.
- EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER aplican el mismo patrón mediante object_type; las referencias E1/E2 son FKs directas a evaluator_record_id.
- object_record_id debe ser UNIQUE dentro de cada tabla de objeto; coverage_scope_id es PK/UNIQUE.
- evidence_ref sigue siendo referencia de navegación 0..1; la relación probatoria canónica es CLAIM_EVIDENCE_LINK 0..n.

La aceptación DEC-C10-061 es documental. No se han ejecutado parser, FK/CHECK, constraints ni pruebas negativas.
