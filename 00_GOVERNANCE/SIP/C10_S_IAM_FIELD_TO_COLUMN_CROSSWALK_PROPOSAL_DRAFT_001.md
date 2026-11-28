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


## 9. Addendum DEC-C10-064 — snapshot pinning y referencias exactas

Opción A queda aprobada por DEC-C10-064. La plantilla U_G §13 es normativa para la correspondencia física: NODE/EDGE/ROUTE/PREDICATE incluyen snapshot_id; EDGE incorpora source_node_record_id/target_node_record_id; PREDICATE incorpora route_record_id; SNAPSHOT fija la versión exacta del NODE raíz mediante FK compuesta que incluye snapshot_id; ROUTE_STEP normaliza la secuencia.

Los IDs semánticos se conservan como crosswalk, pero nunca sustituyen los record IDs en las FKs. Todas las referencias interobjeto deben comprobar mismo snapshot. El crosswalk IAM/FP deberá mapear estos nuevos campos y claves compuestas en la siguiente reconciliación. No se inventan relaciones ni instancias.


### 9.1. Field-to-column mapping reconciled under Opción A

| Concepto/campo | Tabla.columna | Identidad/FK destino | Regla |
|---|---|---|---|
| Pertenencia semántica a snapshot | NODE/EDGE/ROUTE/PREDICATE.snapshot_id | SNAPSHOT.snapshot_id (identidad semántica; FK física exacta aún bloqueada) | Mismo snapshot lógico; no resolver por última versión |
| Extremo origen de EDGE | EDGE.source_node_id + source_node_record_id | NODE.node_id + NODE.object_record_id, compuesto con snapshot_id | ID semántico y revisión exacta deben coincidir |
| Extremo destino de EDGE | EDGE.target_node_id + target_node_record_id | NODE.node_id + NODE.object_record_id, compuesto con snapshot_id | ID semántico y revisión exacta deben coincidir |
| Ruta evaluada por PREDICATE | PREDICATE.route_id + route_record_id | ROUTE.route_id + ROUTE.object_record_id, compuesto con snapshot_id | Pinning exacto; route_id aislado no basta |
| Nodo raíz de unidad | SNAPSHOT.unit_id + unit_object_record_id | NODE.node_id + NODE.object_record_id, compuesto con snapshot_id | semantic_role=LOGICAL_SERVICE_UNIT |
| Secuencia de ruta | ROUTE_STEP.route_record_id / node_record_id / edge_record_id | ROUTE/ NODE/ EDGE.object_record_id, compuesto con snapshot_id | ROUTE_STEP es fuente canónica; ordered_node_edge_sequence no se persiste |
| Versión observacional | Cinco tablas versionadas.object_record_id/object_version/supersedes_record_id | Misma tabla e identidad semántica | Nueva captura crea nueva versión, sin implicar cambio material |

**Bloqueo explícito:** el mapping de snapshot_id solo fija identidad semántica, no una versión concreta de SNAPSHOT. DEC-C10-062 versiona también SNAPSHOT; se requiere resolver OAS-02 mediante un campo de pinning exacto (recomendación: snapshot_object_record_id) o mediante decisión que cambie expresamente la semántica/versionado de SNAPSHOT. Hasta entonces no se declara FK física de mismo snapshot completamente especificada.


### 9.2. DEC-C10-065 — exact SNAPSHOT revision pinning

| Concepto/campo | Tabla.columna | Clave destino | Regla |
|---|---|---|---|
| Revisión exacta del snapshot | NODE/EDGE/ROUTE/PREDICATE/ROUTE_STEP.snapshot_id + snapshot_object_record_id | SNAPSHOT(snapshot_id, object_record_id) | FK compuesta obligatoria; nunca latest-version/timestamp |
| Extremos EDGE | EDGE.snapshot_id + snapshot_object_record_id + source/target_node_record_id | SNAPSHOT(snapshot_id,object_record_id) y NODE(snapshot_id,snapshot_object_record_id,object_record_id) | Mismo snapshot revision y NODE record exacto |
| Ruta de PREDICATE | PREDICATE.snapshot_id + snapshot_object_record_id + route_record_id | SNAPSHOT(snapshot_id,object_record_id) y ROUTE(snapshot_id,snapshot_object_record_id,object_record_id) | Mismo snapshot revision y ROUTE record exacto |
| Paso ROUTE_STEP | ROUTE_STEP.snapshot_id + snapshot_object_record_id + route_record_id/node_record_id/edge_record_id | SNAPSHOT + ROUTE/NODE/EDGE compuestos | Todas las referencias fijan el mismo snapshot revision |
| NODE raíz de SNAPSHOT | SNAPSHOT.snapshot_id + unit_object_record_id | NODE(snapshot_id,object_record_id,node_id) | El registro NODE raíz pertenece al snapshot; circularidad diferible/transaccional |

DEC-C10-065 resuelve OAS-02 a nivel documental. El crosswalk físico aún debe verificarse con claves candidatas completas y orden de columnas exacto; el motor no está seleccionado.


## 9.3. Reconciliación física completa de referencias — DEC-C10-065

**Precedencia:** esta tabla completa y corrige el mapping previo de §§9.1–9.2. Las menciones anteriores a una FK basada solo en `snapshot_id`, o a una referencia sin `snapshot_object_record_id`, se conservan como historial de la evolución documental y no son normativas.

| Relación | Columnas de origen, en orden | Clave destino, en el mismo orden | Regla |
|---|---|---|---|
| Pertenencia de NODE | NODE(`snapshot_id,snapshot_object_record_id`) | SNAPSHOT(`snapshot_id,object_record_id`) | Fija revisión exacta de SNAPSHOT |
| Pertenencia de EDGE | EDGE(`snapshot_id,snapshot_object_record_id`) | SNAPSHOT(`snapshot_id,object_record_id`) | Fija revisión exacta de SNAPSHOT |
| Pertenencia de ROUTE | ROUTE(`snapshot_id,snapshot_object_record_id`) | SNAPSHOT(`snapshot_id,object_record_id`) | Fija revisión exacta de SNAPSHOT |
| Pertenencia de PREDICATE | PREDICATE(`snapshot_id,snapshot_object_record_id`) | SNAPSHOT(`snapshot_id,object_record_id`) | Fija revisión exacta de SNAPSHOT |
| Pertenencia de ROUTE_STEP | ROUTE_STEP(`snapshot_id,snapshot_object_record_id`) | SNAPSHOT(`snapshot_id,object_record_id`) | Fija revisión exacta de SNAPSHOT |
| EDGE origen → NODE | EDGE(`snapshot_id,snapshot_object_record_id,source_node_record_id,source_node_id`) | NODE(`snapshot_id,snapshot_object_record_id,object_record_id,node_id`) | Mismo snapshot exacto, record ID y node_id semántico |
| EDGE destino → NODE | EDGE(`snapshot_id,snapshot_object_record_id,target_node_record_id,target_node_id`) | NODE(`snapshot_id,snapshot_object_record_id,object_record_id,node_id`) | Mismo snapshot exacto, record ID y node_id semántico |
| PREDICATE → ROUTE | PREDICATE(`snapshot_id,snapshot_object_record_id,route_record_id,route_id`) | ROUTE(`snapshot_id,snapshot_object_record_id,object_record_id,route_id`) | Misma revisión exacta de ROUTE |
| ROUTE_STEP → ROUTE | ROUTE_STEP(`snapshot_id,snapshot_object_record_id,route_record_id`) | ROUTE(`snapshot_id,snapshot_object_record_id,object_record_id`) | Misma revisión exacta de ROUTE |
| ROUTE_STEP → NODE | ROUTE_STEP(`snapshot_id,snapshot_object_record_id,node_record_id`) | NODE(`snapshot_id,snapshot_object_record_id,object_record_id`) | Mismo snapshot exacto y NODE |
| ROUTE_STEP → EDGE | ROUTE_STEP(`snapshot_id,snapshot_object_record_id,edge_record_id`) | EDGE(`snapshot_id,snapshot_object_record_id,object_record_id`) | Mismo snapshot exacto y EDGE |
| SNAPSHOT → NODE raíz | SNAPSHOT(`snapshot_id,object_record_id,unit_object_record_id,unit_id`) | NODE(`snapshot_id,snapshot_object_record_id,object_record_id,node_id`) | El object_record_id de SNAPSHOT ocupa el valor de snapshot_object_record_id en NODE; exige semantic_role=LOGICAL_SERVICE_UNIT |

**Claves destino exigidas:** las claves candidatas UNIQUE indicadas en U_G §15.2 deben existir en el mismo orden de columnas que las FKs anteriores. La tabla no declara implementadas esas constraints. ROUTE_STEP conserva PK/UNIQUE por ruta y posición, además de la FK de snapshot exacto.

**Estado:** reconciliación documental de columnas y orden de referencias; motor, DDL, constraints, circularidad diferible, CHECKs, continuidad cross-row, inmutabilidad y pruebas negativas siguen pendientes. No hay schema freeze ni autorización de ejecución.


## 9.4. Reconciliación de referencias tipadas, evidencia y adjudicación — DEC-C10-061

| Tabla origen | Columnas/FK | Destino | Regla |
|---|---|---|---|
| CLAIM_EVIDENCE_LINK | target_node_record_id | NODE.object_record_id | FK nullable; exclusiva con las otras cinco |
| CLAIM_EVIDENCE_LINK | target_edge_record_id | EDGE.object_record_id | FK nullable; exclusiva con las otras cinco |
| CLAIM_EVIDENCE_LINK | target_route_record_id | ROUTE.object_record_id | FK nullable; exclusiva con las otras cinco |
| CLAIM_EVIDENCE_LINK | target_predicate_record_id | PREDICATE.object_record_id | FK nullable; exclusiva con las otras cinco |
| CLAIM_EVIDENCE_LINK | target_snapshot_record_id | SNAPSHOT.object_record_id | FK nullable; exclusiva con las otras cinco |
| CLAIM_EVIDENCE_LINK | target_coverage_scope_id | COVERAGE_REGISTER.coverage_scope_id | FK nullable; exclusiva con las otras cinco |
| CLAIM_EVIDENCE_LINK | evidence_id | EVIDENCE_REGISTER.evidence_id | FK obligatoria |
| CLAIM_EVIDENCE_LINK | evaluator_record_id / adjudication_id | EVALUATOR_ASSESSMENT.evaluator_record_id / ADJUDICATION_REGISTER.adjudication_id | FKs opcionales |
| EVALUATOR_ASSESSMENT | seis columnas target_* | NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT/COVERAGE_REGISTER | Exactamente una FK poblada y coherente con object_type |
| ADJUDICATION_REGISTER | seis columnas target_* | NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT/COVERAGE_REGISTER | Exactamente una FK poblada y coherente con object_type |
| ADJUDICATION_REGISTER | evaluator_record_E1 / evaluator_record_E2 | EVALUATOR_ASSESSMENT.evaluator_record_id | Dos FKs obligatorias a las evaluaciones originales |

**Integridad complementaria:** `claim_evidence_id`, `evidence_id`, `evaluator_record_id`, `adjudication_id` y `coverage_scope_id` deben ser PK/UNIQUE en sus tablas. Las FKs tipadas no se mezclan con las FKs de pertenencia a SNAPSHOT ni sustituyen el par `snapshot_id + snapshot_object_record_id` de las relaciones de grafo. `source_provenance` reside en EVIDENCE_REGISTER; `evidence_ref` es solo navegación 0..1; CLAIM_EVIDENCE_LINK mantiene la relación 0..n.

**Estado:** mapping documental consolidado; CHECK/FK, cardinalidad efectiva, integridad de instancia, custodia y consultas de reconstrucción pendientes de validación técnica autorizada.


## 10. Auditoría de estado del crosswalk C0 — reconciliación temporal, de clase y ruta

**Estado:** reconciliación documental de trabajo; no constituye aceptación nueva, cierre del mapping por propiedad, schema freeze ni autorización de implementación. Prevalecen DEC-C10-065, DEC-C10-070, DEC-C10-071, DEC-C10-072, DEC-C10-074, DEC-C10-075, DEC-C10-076, DEC-C10-077, DEC-C10-079, DEC-C10-080 y DEC-C10-081.

### 10.1. Eje temporal — stage_key

El vocabulario de siete valores está aceptado por DEC-C10-071 y sus significados se encuentran reconciliados en el protocolo de evidencia §20.4:

| stage_key | Función temporal C10-S | Límite del mapping |
|---|---|---|
| C_SRC | Snapshot de configuración fuente | No implica ruta F/A ni estado aplicado |
| F1_S2 | Representación S2 producida por F1 | No equivale a aplicación en destino |
| A1_S1 | Representación S1 producida por A1 | Preservación independiente bajo ruta A |
| F2_DST_DECL | Configuración destino declarada para F2 | No prueba aplicación |
| A2_DST_DECL | Configuración destino declarada para A2 | No prueba aplicación |
| F2_DST_APPLIED | Estado destino observado tras F2 | Requiere snapshot post-aplicación y evidencia |
| A2_DST_APPLIED | Estado destino observado tras A2 | Requiere snapshot post-aplicación y evidencia |

**Dictamen:** el enum y la semántica de etapa no están abiertos. Lo abierto es la asignación de cada captura concreta a una revisión exacta de SNAPSHOT y su evidencia, dentro de `universe_definition/version`. `SNAPSHOT.phase`, reloj DGP `t−1…t9` y timestamp son ejes separados. No se acepta codificar `stage_key` en `SNAPSHOT.scope`; tampoco se infiere desde `phase`, timestamp o texto libre.

### 10.2. Eje de clase — object_class C10 frente a U_G

La clase de origen C10 y el tipo físico U_G son ejes diferentes. La siguiente tabla es una guía de mapping candidato, no una equivalencia automática:

| object_class | Materialización U_G candidata | Regla mínima para resolver | Estado |
|---|---|---|---|
| CMP | NODE; EDGE solo representa relaciones | Identidad CMP/versión exacta, NODE record exacto, semantic_role y boundary_class aplicables; EDGE no sustituye al CMP | Parcial; mapping por instancia/objeto pendiente |
| PAR | Propiedad tipada del owner CMP; NODE solo si la propiedad necesita identidad propia justificada | parameter_key/type/state/value y owner CMP exactos; regla explícita de granularidad; sin NODE por cada valor | OPEN por propiedad |
| REF | EDGE y/o referencia tipada conforme al modelo de REF aceptado | REF conserva identidad propia y extremos; mapping M explícito/versionado; split/merge/n-aria con identidad de grupo y conservación | OPEN por REF y mapping M |
| RUL | PREDICATE y referencias a operandos/owner | rule_id/version, scope, AST, operandos y efecto exactos; distinguir regla de registro de sus referencias | Parcial; mapping por regla pendiente |
| MET | Metadatos tipados distribuidos entre registros existentes, SNAPSHOT y EVIDENCE_REGISTER según función | Clasificar cada atributo por owner, temporalidad, custodia y función; no inventar tabla MET ni target único | OPEN por atributo |

No se infiere `object_class` desde `ug_record_type`, `semantic_role`, `boundary_class`, `predicate_type` o `relation_type`. El mapping debe declarar, como mínimo, identidad de origen/registro, destino/propiedad U_G, owner cuando aplique, cardinalidad, regla de inclusión/exclusión, etapa, snapshot exacto, evidencia y provenance. Puede ser 1:N o N:M; no se fuerza una correspondencia uno-a-uno.

### 10.3. Eje de ruta — familia, identidad y pertenencia

- `F` y `A` son etiquetas auxiliares de familia/branch; no son `route_id`.
- En scope route-specific, `route_id` identifica la ruta y el universo fija `route_record_id` exacto dentro del par `snapshot_id + snapshot_object_record_id`.
- ROUTE_STEP es la fuente canónica de pertenencia de NODE/EDGE a la revisión exacta de ROUTE; PREDICATE debe resolver `route_record_id`; ROUTE se fija por su propio record.
- `routes_affected`, nombre, proximidad o texto libre no demuestran pertenencia.
- El token global `C10S_SCOPE_GLOBAL` y su semántica están aceptados por DEC-C10-072: “sin restricción a una ruta concreta”. No significa ausencia de rutas ni ausencia de pertenencia; no puede colisionar con un route_id real. NULL, vacío, NONE, F y A no lo sustituyen.
- La pertenencia de PAR sigue la regla explícita de owner CMP; no se crea una ruta implícita para cada parámetro. REF requiere mapping a EDGE y pertenencia demostrada; RUL/MET necesitan reglas de clase/función explícitas.

**Dictamen:** la semántica del slot route_id y del token global está decidida. La adjudicación de pertenencia para cada objeto concreto permanece OPEN/UNKNOWN hasta resolver mapping de clase, owner, revisión ROUTE y ROUTE_STEP exhaustivos.

### 10.4. Vinculación con C0 y dimension

La tupla C0 conserva exactamente nueve componentes conforme a DEC-C10-070. `dimension` es atributo independiente de COVERAGE_REGISTER, no décimo componente. La tupla se declara y versiona en `universe_definition/version`; no se reconstruye desde `SNAPSHOT.scope`. La dimensión debe concordar con la clase, regla de elegibilidad y universo, pero no cambia la identidad de C0.

### 10.5. Dictamen de cierre por eje

| Eje | Vocabulario/semántica | Mapping a registro/captura exacta | Resultado actual |
|---|---|---|---|
| stage_key | ACEPTADO | Snapshot exacto y evidencia por etapa | PARCIAL / OPEN |
| object_class | ACEPTADO: CMP/PAR/REF/RUL/MET | Mapping por objeto/propiedad a U_G | OPEN |
| route_id/global | DEC-C10-072 ACEPTADO | Route record y pertenencia por objeto | PARCIAL / OPEN |
| dimension | Separada de C0 | Regla de elegibilidad por scope | OPEN |
| universe_definition/version | Envelope U1 y canonicalización sujetos a DEC-C10-073/074 | Contenido recuperable, versión y provenance por scope | Según DEC-C10-073/074; no reabrir |

**Siguiente unidad de trabajo recomendada:** resolver el mapping CMP→NODE y PAR→propiedad tipada/owner como un único par de granularidad e identidad, porque PAR no puede adjudicarse sin un owner CMP exacto. Después abordar REF→EDGE conforme a DEC-C10-077 y mapping M. RUL y MET quedan para sus contratos específicos.

**Límites:** esta auditoría no puebla IAM, no crea snapshots/scopes/registros, no cierra mappings por instancia, no añade columnas/FKs/tablas, no autoriza parser, validator, fixtures, Design Freeze, validación técnica, implementación ni ejecución. `scientific_execution=false`; `execution_authorized=false`.


### 10.6. Par CMP→NODE y PAR→propiedad del CMP — granularidad e identidad

**Estado:** reconciliación documental candidata, basada en DEC-C10-068/069/070/071/079 y en las reglas de no duplicación del inventario U_G §18.1. No constituye aceptación nueva del mapping por instancia ni completa IAM.

#### A. Identidad del CMP focal

Para el contrato sintético de referencia, los identificadores aceptados por DEC-C10-069 son:

- contrato: `C10S-SVC-REQUEST-PROCESSOR`, versión `1.0.0`;
- instancia: `C10S-SVC-REQUEST-PROCESSOR-001`, revisión `1`;
- componente: `CMP-SERVICE-LOGIC-001`, clase `SERVICE_LOGIC`;
- `CMP-SERVICE-LOGIC` es alias/rol lógico histórico, no identificador de instancia.

La identidad lógica CMP y su representación U_G son distintas. El mapping candidato se expresa como una correspondencia explícita entre:
1. identidad CMP contractual `(contract_id, contract_version, instance_id, instance_version, component_id, component_class)`;
2. NODE semántico `(snapshot_id, snapshot_object_record_id, node_id)`;
3. registro físico U_G exacto `object_record_id`, dentro del mismo snapshot.

La resolución exige un mapping versionado que vincule la identidad CMP con un único NODE raíz para el CMP focal en cada snapshot aplicable. La unicidad se comprueba dentro del universo/snapshot declarado; no se infiere por nombre, alias, `parent_catalog_id`, TID/SID/RID ni por `semantic_role` aislado. El NODE raíz puede usar `semantic_role=LOGICAL_SERVICE_UNIT` según el contrato de inventario, pero ese rol por sí solo no demuestra que sea el CMP contractual.

Los CMP adicionales solo se materializan como NODE si son componentes funcionales distintos con identidad y frontera propias declaradas ex ante. Un CMP no se duplica como NODE en cada etapa: se conserva la identidad lógica y se resuelve el registro NODE de cada snapshot exacto. Si una instancia contiene varios CMP, cada uno requiere su propia correspondencia inequívoca.

#### B. Identidad y granularidad PAR

PAR no recibe por defecto un NODE ni un EDGE. La identidad de la propiedad se define en el ámbito de su owner:
`(owner_component_id, parameter_key)`, con tipo, dominio, unidad, estados permitidos y semántica contractual asociados.

La fila de manifiesto que registra su aplicabilidad/observación conserva además la identidad append-only de DEC-C10-079: `manifest_record_id` global y `manifest_record_revision` por clave lógica, con supersession lineal. Esa identidad de fila no convierte PAR en entidad U_G ni sustituye `parameter_key`.

La correspondencia candidata para cada PAR y snapshot es:
`(component_id, parameter_key)` → propiedad tipada declarada del CMP → NODE owner exacto del snapshot.
Debe resolver:
- contrato/versión e instancia/revisión;
- owner `component_id` y su NODE `object_record_id` exacto en el snapshot;
- `parameter_key`, tipo, dominio, unidad y allowed_states;
- estado/valor conforme a DEC-C10-068 y contrato de parámetro;
- `stage_key`, ruta/scope y `coverage_scope_id`;
- mapping_id/version y evidencia/provenance aplicables.

Los valores ABSENT, NULL, DEFAULT y VALUE son estados tipados distintos cuando estén permitidos; no se convierten en filas NODE ni se equiparan por omisión. Los parámetros del CMP focal aceptados en DEC-C10-068 (`PAR-SVC-ENABLED`, `PAR-SVC-PROFILE`) conservan sus claves y tipos contractuales; esta sección no reabre sus dominios ni obligatoriedad.

#### C. Cuándo sería legítimo un NODE PAR separado

Solo podría proponerse un NODE propio si el objeto tiene identidad y ciclo de vida independientes del owner —no solo porque tenga un valor, cambie entre snapshots o necesite trazabilidad— y si se especifican semántica de entidad, frontera, identidad estable, relaciones con owner, cardinalidad y regla de conservación. Esa excepción requiere decisión explícita y mapping M; no se presume en esta reconciliación.

#### D. Resolución y estados

- CMP con identidad contractual pero sin NODE exacto o mapping inequívoco: `UNKNOWN`.
- Dos NODE candidatos para el mismo CMP en el mismo scope, o identidad/owner contradictorios: `FAIL`.
- Revisión de contrato/instancia/snapshot incompatible sin mapping aprobado: `NOT_COMPARABLE`.
- PAR sin owner CMP resuelto: no se adjudica como PAR independiente; `UNKNOWN`.
- PAR ausente solo es `ABSENT` si el universo y la cobertura ex ante permiten demostrarlo; la falta de fila no demuestra ausencia.
- No aplicable requiere declaración ex ante y justificación de dominio; no equivale a desconocido.

**Conclusión:** el par de granularidad queda fijado como hipótesis de trabajo: un CMP funcional se vincula a un NODE exacto por snapshot; sus PAR se representan como propiedades tipadas del owner y como filas IAM/PAR trazables, no como NODE por parámetro. La resolución por objeto, snapshot y etapa sigue abierta hasta que exista mapping versionado y evidencia suficiente.

**Límites:** no se crea esquema, entidad PAR, columna, FK, tabla, mapping físico ni registro de instancia. No se sella IAM, no se acepta mapping M concreto y no se autoriza parser, validator, fixtures, Design Freeze, implementación o ejecución. `scientific_execution=false`; `execution_authorized=false`.


### 10.7. Contrato candidato de correspondencia CMP↔NODE por snapshot

**Estado:** propuesta documental para adjudicación; no aceptada todavía. Especializa §10.6 sin crear entidad ni campo físico.

#### 10.7.1. Unidad de correspondencia

La unidad de mapping es el par:

`(CMP contractual exacto, SNAPSHOT exacto)`

donde CMP contractual exacto comprende `contract_id/version`, `instance_id/version`, `component_id` y `component_class`; SNAPSHOT exacto comprende `snapshot_id + snapshot_object_record_id` conforme a DEC-C10-065.

La relación propuesta es una correspondencia de anclaje semántico **1:1 dentro de cada snapshot**:
- cada CMP declarado aplicable tiene exactamente un NODE raíz/anchor en ese snapshot;
- un NODE anchor no puede representar simultáneamente dos CMP distintos;
- los NODE subordinados que describan partes, dependencias o estructura interna no son mappings CMP adicionales salvo que tengan identidad funcional propia declarada ex ante como CMP separado;
- un CMP no se duplica en varios NODE anchor para resolver una descomposición estructural. La descomposición se representa mediante las relaciones U_G existentes y no altera la identidad del CMP.

La cardinalidad 1:1 se limita al anclaje de identidad CMP↔NODE, no a la transformación semántica completa entre configuraciones ni a la correspondencia entre todos los NODE de origen y destino.

#### 10.7.2. Registro de mapping exigido

Cada mapping debe declarar, como mínimo:
- `mapping_id` y `mapping_version`;
- identidad contractual completa CMP;
- `snapshot_id` y `snapshot_object_record_id`;
- `node_id` y `object_record_id` exactos del NODE anchor;
- `semantic_role` y `boundary_class` observados, sin usarlos como sustitutos de identidad;
- `universe_definition_id/version` y scope de aplicabilidad;
- regla de selección/identidad, cardinalidad esperada y control de unicidad;
- provenance, evidencia y adjudicación independiente.

No se permite resolver por nombre, alias, parent_catalog_id, TID/SID/RID, similitud de atributos o posición en tabla. El mapping debe apuntar al registro NODE real del mismo snapshot exacto; no basta con node_id sin record ID.

#### 10.7.3. Continuidad entre snapshots y etapas

La continuidad se establece mediante el mismo `component_id` contractual y mappings separados a cada snapshot exacto. No se exige que `node_id` ni `object_record_id` se repitan entre snapshots; son identidades de registro sujetas a snapshot. La continuidad semántica entre versiones debe justificarse por el contrato y la provenance del mapping, no por igualdad de IDs U_G.

`stage_key` y `route_id/scope` califican la observación/cobertura C0, no multiplican la identidad del NODE ni crean un NODE por etapa o ruta. Si un mismo snapshot exacto sirve a más de una etapa declarada, el NODE anchor es el mismo registro y las filas de cobertura permanecen diferenciadas por sus scopes C0.

#### 10.7.4. Estados de adjudicación

- Exactamente un NODE anchor, identidad CMP/snapshot concordante y mapping versionado completo: candidato a `PASS` de correspondencia.
- Ningún NODE encontrado tras enumeración exhaustiva del universo declarado, pese a que el CMP es aplicable: `FAIL` de integridad del mapping/inventario.
- Dos o más NODE candidatos para el mismo CMP y snapshot, o un NODE asignado a dos CMP: `FAIL` por violación de unicidad.
- Universo, snapshot o mapping incompleto/no accesible, o falta de evidencia para decidir unicidad: `UNKNOWN`.
- Cambio incompatible de contrato/instancia o semántica sin mapping de comparabilidad aprobado: `NOT_COMPARABLE`.
- CMP declarado no aplicable ex ante en ese snapshot: `NA`, con disparador y justificación predeclarados; nunca por ausencia de NODE observada.

Un PASS de correspondencia no acredita por sí mismo la verdad de propiedades PAR, la pertenencia a rutas, la preservación entre transformaciones ni la completitud global del universo.

#### 10.7.5. Controles independientes mínimos

1. Integridad de identidad contractual y versión.
2. Existencia exacta del SNAPSHOT y del NODE record dentro de ese snapshot.
3. Unicidad CMP→NODE y NODE→CMP dentro del universo/snapshot.
4. Consistencia de `node_id`, `object_record_id`, `snapshot_id` y `snapshot_object_record_id`.
5. Concordancia con `universe_definition/version`, aplicabilidad y scope C0.
6. Ausencia de mappings implícitos por alias, nombre o similitud.
7. Trazabilidad de mapping, evidencia y adjudicador independiente.

**No se autoriza** crear el registro de mapping físico, poblar IAM, generar snapshots, añadir columnas/FKs/tablas, implementar controles, ni ejecutar validación. La propuesta tampoco cierra el roster CMP completo ni los mappings P1.


### 10.8. Registro de aceptación — DEC-C10-082

**Estado:** ACEPTADO — contrato lógico documental.

La cardinalidad 1:1 del anclaje CMP↔NODE por CMP y snapshot queda aceptada conforme a DEC-C10-082. Se acepta la unidad (identidad contractual CMP exacta, snapshot exacto), NODE anchor identificado por `node_id + object_record_id`, mapping versionado, unicidad en ambos sentidos y continuidad entre snapshots mediante `component_id` contractual sin exigir igualdad de IDs U_G.

La etapa y ruta califican cobertura, no multiplican la identidad NODE. Los resultados de adjudicación y sus límites son los establecidos en §10.7 y DEC-C10-082. Esta aceptación no completa el roster CMP, no resuelve mappings P1/PAR, no sella IAM ni autoriza poblar registros, implementar o ejecutar controles. `scientific_execution=false`; `execution_authorized=false`.


### 10.9. Reconciliación de PAR por stage_key — propuesta pendiente

La matriz de aplicabilidad §18.6 desarrolla la obligación de los dos PAR aceptados en las siete etapas DEC-C10-071. Se distingue: configuración fuente (`C_SRC`); preservación intermedia independiente (`F1_S2`, `A1_S1`); configuración destino declarada (`F2_DST_DECL`, `A2_DST_DECL`); y estado efectivamente aplicado (`F2_DST_APPLIED`, `A2_DST_APPLIED`).

Ambos parámetros son P0 REQUIRED por DEC-C10-068. Para estados declarativos, el contrato base espera VALUE tipado; no hay DEFAULT contractual aceptado y ABSENT/NULL no son admisibles. Las etapas intermedias exigen preservación semántica por ruta, no aplicación. Las etapas aplicadas exigen snapshot y evidencia del estado real, sin inferirlo desde la declaración ni desde runtime.

La falta de evidencia/cobertura produce UNKNOWN; la contradicción demostrada produce 0 en el predicado predeclarado; NA no se deriva de falta de datos ni se aplica a estos dos parámetros en las siete etapas del contrato base. `E_dst/runtime` permanece fuera de `stage_key`.

**Estado:** propuesta pendiente de aceptación. No asigna valores por escenario, no sella IAM ni crea mappings físicos/fixtures ni autoriza implementación o ejecución. Prevalecen DEC-C10-068/069/071/082 y matriz §18.3–18.6.

### 10.10. Aceptación — DEC-C10-083

La adjudicación de `PAR-SVC-ENABLED` y `PAR-SVC-PROFILE` en las siete etapas DEC-C10-071 queda aceptada conforme a DEC-C10-083 y matriz §18.6–18.7: P0 REQUIRED; VALUE tipado en configuración declarada; preservación semántica independiente en F1/A1; evidencia independiente del estado aplicado en F2/A2; sin DEFAULT contractual; ABSENT/NULL no admisibles si la ausencia está demostrada con cobertura suficiente.

La falta de snapshot, mapping o cobertura es UNKNOWN. Runtime permanece separado de `stage_key`. Esta aceptación no adjudica observaciones ni fija valores por escenario, no sella IAM ni autoriza implementación/ejecución.


### 10.11. Equivalencia semántica de PAR — referencia a matriz §15.1

**Estado:** propuesta documental pendiente de aceptación.

La matriz abstracta §15.1 especifica el contrato candidato reutilizable para equivalencia semántica de `PAR-SVC-ENABLED` y `PAR-SVC-PROFILE`: identidad exacta BOOL; biyección total, inyectiva y versionada ENUM sobre STANDARD/READ_ONLY/DISABLED; preservación separada de estado y valor; mappings F1 y A1 independientes; declaración destino separada de aplicación efectiva; y conservación independiente de `RUL-SVC-ENABLE-PROFILE-01`.

El IAM deberá referenciar el `mapping_id/version` y el contrato semántico aprobado, sin inferir equivalencia por igualdad de literales físicos ni por igualdad de nombre de parámetro. Los resultados se adjudican por etapa/ruta; falta de evidencia produce UNKNOWN y versiones incompatibles sin mapping aprobado producen NOT_COMPARABLE.

No se aprueban codificaciones físicas, tablas concretas, valores por escenario, oráculo ni resultados observados. No se sella IAM ni se autoriza implementación o ejecución científica.

### 10.12. Aceptación del contrato semántico PAR — DEC-C10-084

La referencia de §10.11 queda aceptada conforme a DEC-C10-084 y matriz abstracta §15.1–15.2: BOOL con identidad semántica exacta; ENUM con biyección total, inyectiva y versionada sobre STANDARD/READ_ONLY/DISABLED; separación estado/valor; preservación independiente de la regla constitutiva; mappings F1/A1 independientes; y verificación separada de destino declarado y estado aplicado F2/A2.

El IAM deberá identificar el mapping y versión aprobados y la unidad CMP/snapshot/etapa/ruta exacta. No inferirá equivalencia por igualdad de nombres o literales físicos ni transitividad entre mappings incompatibles. La aceptación no aprueba codificaciones físicas, mappings observados ni sella IAM; no autoriza implementación o ejecución científica.

### 10.13. Predicados C_SRC→F1_S2 / C_SRC→A1_S1 — propuesta pendiente

La matriz abstracta §15.3 define cinco familias independientes: estado PAR, valor/tipo/dominio PAR, preservación RUL, binding de identidad/alcance y suficiencia de procedencia. Cada familia se instancia por separado para `r=F1` y `r=A1`; la unidad de adjudicación fija CMP owner, snapshot fuente/destino, stage_key, route_id/route_record_id, coverage_scope_id, parámetro/regla y mapping_id/version.

El IAM deberá enlazar las filas PAR/RUL con sus registros y evidencias exactos, sin inferir mapping por nombre ni usar el NODE anchor como sustituto de la identidad PAR. El NODE anchor por snapshot se resuelve conforme a DEC-C10-082. La evidencia de una ruta no cubre la otra.

Los predicados de estado/valor se adjudican separadamente; la regla `ENABLED=true ⇒ PROFILE∈{STANDARD, READ_ONLY}` se comprueba como preservación semántica FP-03, no como prueba de aplicación runtime FP-06/FP-07. Falta de observación/cobertura produce UNKNOWN; contradicción solo produce FAIL con cobertura suficiente.

**Estado:** propuesta documental pendiente de aceptación. No crea columnas, FK ni filas IAM; no define mappings físicos ni autoriza implementación/ejecución.


## 10.14. Aceptación DEC-C10-085 — adjudicación PAR F1/A1

**Estado:** ACCEPTED — DOCUMENTAL. La matriz abstracta §15.3 y DEC-C10-085 gobiernan los predicados C_SRC→F1_S2 y C_SRC→A1_S1.

El IAM deberá soportar adjudicaciones independientes por ruta y parámetro/regla, resolviendo CMP owner/NODE anchor, snapshots/registros, stage_key, route_id/route_record_id, coverage_scope_id y mapping_id/version exactos. Las cinco familias (estado PAR; valor/tipo/dominio; RUL; identidad/alcance; procedencia) son organizadoras y se reconcilian con SM/FP; no generan predicados duplicados ni doble contabilización.

La ausencia de observación o cobertura suficiente es UNKNOWN, no ABSENT ni FAIL. FAIL requiere contradicción demostrada con cobertura suficiente. La evidencia de F1 no cubre A1. Esta aceptación no crea columnas/FK/filas IAM, no sella IAM ni autoriza implementación o ejecución científica. Véase DEC-C10-085.

## 10.15. Propuesta de mapping IAM para F1/A1→destino declarado

**Estado:** PROPUESTA DOCUMENTAL — pendiente de aceptación. Véase la matriz abstracta §15.5.

El IAM deberá poder resolver separadamente para F y A: artefacto intermedio exacto, artefacto destino declarado exacto, CMP owner/NODE anchor por snapshot, `stage_key`, ruta/scope, parámetros PAR y regla RUL, mapping/versiones y evidencia del proceso. Se distinguen dos dimensiones no compensables: (i) conformidad semántica del destino declarado respecto de F1/A1 y (ii) conformidad probatoria de la transición que afirma haber producido ese destino.

La primera exige equivalencia de estado, tipo/dominio y valor BOOL/ENUM, y preservación semántica RUL conforme a DEC-C10-084. La segunda exige lineage de proceso y evidencia íntegra que vincule entrada/salida y artefacto declarado; la mera igualdad/equivalencia de artefactos no demuestra que la transformación los conecte causalmente.

Los resultados se adjudican por ruta, sin compensación F/A. UNKNOWN ante cobertura/evidencia insuficientes; FAIL solo ante contradicción o ausencia exhaustivamente demostrada; NOT_COMPARABLE ante incompatibilidad sin mapping aprobado. La configuración declarada no demuestra aplicación efectiva: FP-06/FP-07 y F2/A2 applied quedan fuera de este bloque.

Esta propuesta no añade columnas/FK ni filas IAM, no define mappings físicos, no sella IAM y no autoriza implementación o ejecución científica.


## 10.16. Aceptación DEC-C10-086 — mapping de conformidad F1/A1→F2/A2 declarada

**Estado:** ACCEPTED — DOCUMENTAL. Véase DEC-C10-086 y matriz abstracta §15.5.

El contrato IAM debe permitir resolver por separado `P-DECL` y `P-TRANS`, por ruta F/A, parámetro/regla, CMP owner/NODE anchor, snapshots/registros, etapa, ruta/scope, mapping/versiones y evidencia. La conformidad semántica del destino declarado no implica que la transición haya producido ese artefacto; el lineage probatorio requiere evidencia propia del proceso y vínculo exacto de entradas/salidas.

Los resultados F y A no se compensan. La configuración declarada no acredita aplicación efectiva; FP-06/FP-07 y las etapas applied permanecen separadas. Esta aceptación no añade campos físicos/FK, no sella IAM y no autoriza implementación o ejecución científica.

## 10.17. Propuesta IAM — aplicación efectiva y verificación post-aplicación (FP-06/07/08)

**Estado:** PROPUESTA DOCUMENTAL — pendiente de aceptación. Véase matriz abstracta §15.7.

El contrato IAM deberá poder resolver separadamente, para F y A: (i) artefacto declarado exacto; (ii) evento de aplicación y target/environment identity; (iii) snapshot/registro post-aplicación; (iv) CMP owner/NODE anchor, PAR/RUL, stage_key, route/scope y mapping/versiones; y (v) evidencia de proceso y observación con provenance/integridad.

La separación semántica es obligatoria:
- FP-06 acredita la aplicación efectiva del paquete/configuración declarada sobre el destino identificado, con evidencia del evento y resultado.
- FP-07 acredita que el estado post-aplicación observado satisface el contrato, usando snapshot/cobertura y predicados FP-01…05 aplicables. No basta el log o exit code de la herramienta.
- FP-08 acredita identidad, procedencia, integridad y reproducibilidad de paquete, evento, destino, snapshot y evidencia; no sustituye FP-06 ni FP-07.

Los resultados se mantienen independientes por ruta y por familia. La falta de registro de aplicación no demuestra no aplicación: UNKNOWN salvo evidencia autoritativa/exhaustiva o contradicción positiva. La configuración declarada no se confunde con la aplicada. Esta propuesta no añade columnas/FK, no sella IAM ni autoriza implementación o ejecución científica.


## 10.18. Aceptación DEC-C10-087 — mapping IAM de aplicación efectiva y post-check

**Estado:** ACCEPTED — DOCUMENTAL. Véase DEC-C10-087 y matriz abstracta §15.7.

El contrato IAM debe permitir resolver por ruta F/A el artefacto declarado y registro exactos, evento de aplicación, target/environment identity, snapshot y registro post-aplicación, CMP owner/NODE anchor, PAR/RUL, stage_key, route/scope, mapping/versiones y evidencia.

Se distinguen FP-06 (evento efectivo), FP-07 (estado observado post-aplicación contra FP-01…05 aplicables) y FP-08 (procedencia, identidad e integridad). FP-08 no sustituye evidencia de aplicación ni observación. Ausencia de registro no demuestra no aplicación: UNKNOWN salvo evidencia autoritativa/exhaustiva o contradicción positiva. F y A no se compensan; no hay doble contabilización de un mismo defecto.

Esta aceptación no añade campos/FK, no sella IAM ni autoriza implementación o ejecución científica.

## 10.19. Integración IAM por etapa, ruta y tiempo (DEC-C10-088 aceptada)

**Estado:** ACCEPTED — DOCUMENTAL por DEC-C10-088.

El IAM/crosswalk debe resolver, sin inferencia nominal, la tupla de cada observación y transición: contrato/instancia y versiones; CMP owner/NODE anchor; object/record identities; `stage_key`; snapshot y snapshot record; route_id/route_record_id; coverage_scope_id y universe_definition/version; parameter_key/rule_id y manifest_record_id/revision; mapping_id/version; evidencia y su predicado/afirmación; instante DGP de generación y observación. `stage_key`, reloj DGP `t0…t9`, SNAPSHOT.phase y step_k son ejes distintos y requieren enlaces explícitos.

El crosswalk debe representar tres tramos independientes por ruta: C_SRC→F1/A1 (DEC-C10-085), F1/A1→F2/A2 declaradas (DEC-C10-086), y F2/A2 declaradas→aplicadas (DEC-C10-087). En el tercer tramo debe resolver evento FP-06, observación post-aplicación FP-07 y provenance/identidad FP-08, sin convertirlos en campos físicos no aprobados ni en predicados nuevos.

La evidencia no se hereda entre etapa, ruta ni afirmación. COV/E_T es epistémico; UNKNOWN ante cobertura, mapping o lineage insuficientes. El vínculo IAM no acredita por sí solo ACC/APP/Reach ni causalidad de ΔT_acc→Value. Esta propuesta no añade columnas/FK, no sella IAM y no autoriza implementación o ejecución científica.


## 10.20. Contrato lógico candidato de roster CMP y mapping IAM↔U_G

**Estado:** PROPUESTA DOCUMENTAL — pendiente de aceptación. Desarrolla DEC-C10-078 y especializa el anclaje ya aceptado por DEC-C10-082. No amplía el schema U_G ni crea una decisión nueva.

### 10.20.1. Roster CMP: lo identificado frente a lo exhaustivo

El roster se construye desde identidades contractuales, nunca desde nombres observados de NODE ni desde roles inferidos.

| Elemento | Identidad/valor documental | Estado | Tratamiento IAM |
|---|---|---|---|
| Contrato de servicio | contract_id=C10S-SVC-REQUEST-PROCESSOR; contract_version=1.0.0 | Aceptado por DEC-C10-069 | Referencia contractual inmutable para la instancia de referencia |
| Instancia lógica | instance_id=C10S-SVC-REQUEST-PROCESSOR-001; instance_version=1 | Aceptado por DEC-C10-069 | Unidad versionada; no confundir con NODE ni snapshot |
| CMP de referencia | component_id=CMP-SERVICE-LOGIC-001; component_class=SERVICE_LOGIC | Aceptado por DEC-C10-069 | Único CMP con identidad concreta recuperada en este contrato |
| Etiqueta de owner | CMP-SERVICE-LOGIC | Etiqueta/rol lógico provisional | No es component_id ni una segunda instancia |
| CMP adicionales | No hay IDs adicionales aceptados en el contrato de servicio recuperado | OPEN / roster no exhaustivo | No inventar ni declarar cardinalidad total 1 por ausencia de otros IDs |

La propuesta de roster mínimo identificable contiene el CMP de referencia anterior. No afirma que el universo total CMP de toda la instancia experimental esté exhaustivamente enumerado. Antes de sellar IAM deberá reconciliarse el roster completo con el universo UDG, la instancia y el boundary contract; cada CMP adicional requerirá identidad contractual propia, clase, versión y justificación de inclusión. La regla de cardinalidad de clase CMP≥1 (DEC-C10-056) no autoriza inferir CMP=1.

### 10.20.2. Unidad y clave del mapping CMP↔NODE

Se reutiliza, sin modificar, la unidad ya aceptada en DEC-C10-082:

- CMP contractual exacto: contract_id/version + instance_id/version + component_id + component_class.
- Snapshot exacto: snapshot_id + snapshot_object_record_id.
- NODE anchor exacto: node_id + object_record_id, perteneciente al snapshot indicado.
- Mapping: mapping_id + mapping_version, ligado a universe_definition_id/version y scope.

**Cardinalidad aceptada:** exactamente un NODE anchor por cada CMP aplicable y snapshot; ningún NODE anchor puede representar dos CMP. Los NODE subordinados no son CMP adicionales por defecto. La continuidad entre snapshots se basa en component_id y mappings versionados independientes; no exige igualdad de node_id/object_record_id.

stage_key y route_id/scope califican la cobertura de observaciones; no forman parte de la identidad CMP↔NODE ni multiplican el NODE anchor. Si un mismo snapshot exacto es utilizado en varias etapas/rutas, se reutiliza el mismo anchor y se registran scopes de cobertura distintos.

### 10.20.3. Proyección propuesta sobre U_G existente

La proyección se limita a los diez registros U_G existentes y a los campos que ya aparecen en la plantilla. No autoriza columnas nuevas.

| Concepto IAM/CMP | Ubicación U_G | Regla de enlace |
|---|---|---|
| Identidad contractual CMP | NODE.owner/boundary y/o notes/unknowns como referencia descriptiva; identidad normativa permanece en contrato/MET y mapping versionado | No sustituir component_id por node_id, nombre o semantic_role |
| CMP anchor | NODE.node_id + object_record_id + snapshot_id + snapshot_object_record_id | Debe resolver al registro NODE exacto del snapshot; FK compuesta conforme al contrato snapshot |
| Unidad lógica del servicio | SNAPSHOT.unit_id + unit_object_record_id → NODE raíz semantic_role=LOGICAL_SERVICE_UNIT | No duplicar logical_service_id en cada fila; aplicar el pinning de snapshot aceptado |
| Clase de frontera | NODE.boundary_class existente | Usar únicamente P0_CONFIG, P1_ENVIRONMENT, DUAL_P0_P1 o NA conforme DEC-C10-059; P2 es transversal, no valor |
| Rol semántico | NODE.semantic_role existente | Describe función en U_G; no es identidad CMP ni prueba de membership |
| Revisión/identidad del registro | NODE.object_record_id, object_version, supersedes_record_id y snapshot exacto | No usar latest implícito; respetar append-only y DEC-C10-079 cuando aplique |
| Relaciones entre CMP/NODE | EDGE y sus endpoints/record IDs existentes | Solo relaciones observadas y tipos ya catalogados; no crear EDGE por inferencia |
| Aplicabilidad y membership | IAM L1/L2 + universe_definition/version + COVERAGE_REGISTER | La membership se prueba contra universo exacto; mapping anchor no demuestra exhaustividad |
| Evidencia y adjudicación | EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER | Mantener evidencia 1:N, cobertura y dictamen separados; no sobrecargar NODE.evidence_ref |

boundary_class y semantic_role son atributos de clasificación/rol, nunca claves de matching. No se autoriza añadir component_id, mapping_id, logical_service_id u otras columnas nuevas a NODE por esta propuesta; cuando no exista campo U_G adecuado, la identidad contractual se conserva en el artefacto de mapping/MET enlazado y versionado, no se simula con un campo semánticamente distinto.

### 10.20.4. Contrato mínimo del registro lógico de mapping

Cada mapping candidato debe declarar, como mínimo:

1. mapping_id, mapping_version y estado de adjudicación;
2. identidad CMP completa (contract_id/version, instance_id/version, component_id, component_class);
3. snapshot_id y snapshot_object_record_id exactos;
4. node_id y object_record_id exactos del NODE anchor;
5. universe_definition_id/version, coverage_scope_id y scope aplicable;
6. semantic_role y boundary_class observados, sin usarlos como sustitutos de identidad;
7. regla de selección/identidad, cardinalidad esperada 1:1 y controles de unicidad bidireccional;
8. provenance, evidencia y adjudicación independiente;
9. compatibilidad/continuidad respecto de otros mappings del mismo component_id, sin igualdad nominal implícita.

El contrato lógico no determina todavía dónde se almacenará físicamente este registro ni añade una tabla. Su representación debe reutilizar el artefacto/registro de mapping ya previsto y el soporte de MET/U_G, una vez que se resuelva su crosswalk físico.

### 10.20.5. Reglas de resolución y estados

- PASS: identidad contractual y snapshot exactos; un NODE anchor; unicidad CMP→NODE y NODE→CMP; mapping versionado; universo/scope y evidencia suficientes.
- FAIL: contradicción positiva o cardinalidad distinta de 1:1 demostrada con enumeración exhaustiva del universo/snapshot aplicable.
- UNKNOWN: universo, snapshot, registro, mapping, cobertura o evidencia incompletos/no accesibles; no convertir ausencia de fila en ausencia de CMP/NODE.
- NOT_COMPARABLE: contrato, clase, versión, frontera o snapshot incompatibles sin mapping de comparabilidad aprobado.
- NA: solo cuando la no aplicabilidad del CMP al snapshot se declaró ex ante, con disparador y fundamento; nunca por ausencia de observación.

Un PASS solo demuestra anclaje de identidad. No prueba pertenencia exhaustiva del universo, equivalencia semántica, verdad PAR, preservación F1/A1, destino declarado/aplicado, disponibilidad, accesibilidad, Reach ni causalidad.

### 10.20.6. Límites y decisiones aún abiertas

Permanecen OPEN: roster CMP exhaustivo; mappings de CMP P1 y otros CMP no identificados; ubicación física del mapping; dominio y cardinalidad de las referencias IAM por capa; integración exacta de MET; mappings de REF/RUL y mapping M; evidencia observacional y cobertura real; controles técnicos de unicidad y resolución.

Esta propuesta no sella IAM, no declara cobertura, no modifica DEC-C10-082, no añade columnas/FK/tablas, no autoriza parser, resolver, validator, fixtures, implementación, Design Freeze ni ejecución. scientific_execution=false; execution_authorized=false.


## 10.21. Reconciliación del catálogo U_G N01–N23 con membership IAM CMP/PAR/REF/RUL/MET

**Estado:** PROPUESTA DOCUMENTAL DE CLASIFICACIÓN — pendiente de aceptación. Reutiliza U_G §§81–84, el contrato de frontera §82, DEC-C10-058/059/065/069/082 y el contrato IAM L1–L4. No crea nodos ni instancias y no convierte el catálogo candidato en roster observado.

### 10.21.1. Distinción normativa: NODE no equivale a CMP

U_G NODE es una clase de registro del grafo de auditoría. CMP es una clase de objeto del dominio de instancia dentro del IAM. Por tanto:
- todo CMP que entre en U_G debe tener un NODE anchor exacto conforme a DEC-C10-082;
- no todo NODE U_G es CMP;
- la pertenencia a NODE, la clasificación P0/P1/DUAL_P0_P1/NA y el rol semántico no demuestran por sí solos membership CMP;
- PAR, REF, RUL y MET conservan sus identidades/clases propias y no se convierten en CMP por estar asociados a un NODE;
- P2 es perímetro causal transversal, no clase de boundary_class ni clase IAM.

DEC-C10-058 fija el criterio conceptual de unidad lógica y clasificación P0/P1/P2; DEC-C10-059 fija el dominio de boundary_class. DEC-C10-082 fija la cardinalidad del anclaje CMP↔NODE por snapshot. Ninguna de estas decisiones declara que los 23 roles U_G sean 23 CMP ni determina el roster técnico real.

### 10.21.2. Clasificación provisional de los 23 roles U_G

La columna “IAM candidato” es una hipótesis de clase primaria que debe resolverse a partir de identidad contractual y descomposición observada. “No CMP por función” no significa inexistencia del nodo: significa que su papel conceptual no es un componente CMP. “Condicional” exige evidencia de identidad/versión propia y criterio de frontera antes de asignar clase.

| U_G | Rol candidato | IAM candidato | Regla de reconciliación / condición |
|---|---|---|---|
| N01 | Unidad/sistema anfitrión y S0 | Condicional: unidad lógica / NODE raíz; objetos host descompuestos pueden ser CMP P1 | La unidad lógica se representa por NODE raíz LOGICAL_SERVICE_UNIT y SNAPSHOT.unit_id/FK exacta; host/SO no se fusiona con la unidad ni se declara CMP sin identidad contractual propia |
| N02 | Asignación Z | No CMP; diseño/registro de asignación | Mantener como objeto de diseño/medición según U_G; no introducir en roster CMP |
| N03 | Política/proceso B | No CMP por defecto; intervención/política | Identidad de política y eventos de provisión no son automáticamente componentes de la instancia destino |
| N04 | Paquete adaptador focal | CMP candidato P0/P1 según frontera funcional | CMP solo si tiene component_id/clase/versión contractuales propios; artefacto/paquete puede ser parte de CMP o CMP separado si supera criterio de granularidad §82.2 |
| N05 | Runtime/sidecar focal | CMP candidato P1 o DUAL_P0_P1 | Separar de N04 solo si identidad, versión, fallo, interfaz, recursos o exposición causal difieren materialmente; sidecar no se presupone CMP autónomo |
| N06 | Librerías/dependencias focales | CMP candidato P1, posiblemente múltiple | Cada dependencia solo es CMP si objeto contractual independiente; lockfile/SBOM y dependencia transitiva son evidencia/relación, no membership automática |
| N07 | Endpoint/canal focal | Condicional: REF/interfaz o CMP | Normalmente interfaz/endpoint referido por REF o atributo del CMP; CMP separado solo si es servicio/componente con identidad, lifecycle y contrato propios |
| N08 | C_dep | No CMP; MET/medición técnica | Constructo/resultado de evaluación, no componente técnico |
| N09 | Predicados A_f* | No CMP; MET/constructo | Predicados y dictámenes de accesibilidad permanecen separados de los componentes que evalúan |
| N10 | Transformación focal τ2/F1 | No CMP por defecto; transformación/objeto semántico | Identidad transformacional TID/SID/RID no se reutiliza como component_id; mapping explícito si existe implementación técnica CMP |
| N11 | Aplicación F2 | No CMP por defecto; transformación/operación semántica | La operación o etapa no es componente salvo implementación autónoma contractual diferenciada |
| N12 | Estado destino | No CMP; estado/datos | Configuración/estado se representa como PAR/NODE/artefacto según identidad y granularidad; no como CMP por nombre |
| N13 | Exportador A1 | CMP candidato de ruta alternativa | CMP solo con identidad contractual independiente; si es una capacidad dentro de otro CMP, se conserva como rol/función y relación |
| N14 | Formato/artefacto de intercambio | Condicional: PAR/REF/artefacto de datos, raramente CMP | Formato/contrato puede ser REF o metadato/versionado; el archivo/artefacto concreto no es CMP salvo que sea componente ejecutable independiente |
| N15 | Importador A2 | CMP candidato de ruta alternativa | Mismo criterio de N13; no se presume existente ni funcional |
| N16 | Oráculo/criterio F* | No CMP; MET y/o activo de evaluación P2 | Oráculo, criterio, evaluator y evidencia deben permanecer separados del mecanismo focal; si existe software de oráculo, su implementación puede tener CMP propio, sin confundirlo con el criterio MET |
| N17 | Autorizaciones C_auth | Condicional: PAR/POL/REF y/o servicio IAM técnico | La regla/estado de autorización no es automáticamente CMP; un servicio de autorización independiente puede ser CMP P1 si tiene identidad contractual propia. Diferenciar autorización basal de ACL/credenciales técnicas |
| N18 | Recursos/capacidad compartida | Condicional: recurso P1/P2, no CMP por defecto | Registrar capacidad, disponibilidad, asignación y consumo separadamente; recurso compartido solo es CMP si corresponde a componente software contractual; recurso físico/cuota es recurso/condición, no CMP |
| N19 | Configuración fuente/destino | PAR y/o NODE de estado/configuración | Las propiedades atómicas pertenecen al roster PAR con owner CMP exacto; no crear CMP por cada configuración ni confundir configuración con el componente owner |
| N20 | Dependencias/API/servicios compartidos | Condicional: CMP, REF o externo | Dependencia software bajo contrato de instancia puede ser CMP; API/interface puede ser REF; servicio fuera del control/contrato se mantiene externo. Requiere identidad, owner, versión y boundary |
| N21 | Servicios externos | Externo; CMP solo en su propio dominio contractual si se modela explícitamente | En el IAM de la instancia focal no se incorporan como CMP internos por el mero consumo; registrar identidad/contrato externo, interfaz, versión, disponibilidad, límites y relaciones P2 |
| N22 | Información/conocimiento agente | No CMP por defecto; mecanismo/estado informacional P2 | Conocimiento, aviso y consideración son mecanismos/mediadores posteriores; información técnica incorporada al sistema puede ser PAR/REF o componente solo si cumple criterio propio |
| N23 | Ejecución/Outcome/Value | No CMP; eventos/resultados/constructos | Mantener ejecución, Outcome y Value desagregados cuando tengan identidad/tiempo propio; el software evaluado puede ser CMP, pero no el resultado |

### 10.21.3. Regla para construir el roster CMP completo

El roster completo no se obtiene enumerando los 23 roles U_G ni copiando los IDs de una tabla candidata. Debe construirse por contrato e instancia:
1. partir de contract_id/version e instance_id/version exactos;
2. enumerar objetos con identidad contractual component_id, component_class y versión/revisión propia;
3. decidir granularidad conforme a §82.2, evitando tanto agregación que oculte vías como fragmentación por archivo/hash/nombre;
4. clasificar boundary_class conforme DEC-C10-059 sin inferir membership CMP desde P0/P1;
5. mapear cada CMP aplicable a exactamente un NODE anchor por snapshot, y garantizar unicidad inversa, conforme DEC-C10-082;
6. vincular relaciones y dependencias mediante EDGE/REF según su naturaleza; REF no se infiere de FK ni de endpoint;
7. mantener PAR/RUL/MET en sus clases propias y enlazar sus owners/referencias sin duplicar identidad;
8. declarar universo, scope, regla de enumeración, fuentes y cobertura. Sin enumeración exhaustiva, roster completeness=UNKNOWN/PARTIAL, nunca PASS por ausencia de IDs adicionales.

### 10.21.4. Matriz de decisión de frontera vs membership

La adjudicación de cada objeto debe responder separadamente:
- **Identidad:** ¿existe objeto contractual autónomo con component_id/version propios?
- **Granularidad:** ¿difiere materialmente en función, cambio, fallo, interfaz, permisos, recursos, ruta o evidencia?
- **Clase IAM:** ¿CMP, PAR, REF, RUL o MET, sin doble contabilización?
- **Frontera:** ¿P0_CONFIG, P1_ENVIRONMENT, DUAL_P0_P1 o NA según DEC-C10-059?
- **Relación:** ¿EDGE estructural, REF de dominio, dependencia externa o vínculo probatorio?
- **Snapshot:** ¿qué registro exacto y qué mapping versionado lo ancla?
- **Evidencia/cobertura:** ¿qué fuentes y denominador sustentan membership, exclusión y completitud?

Las preguntas son independientes: un objeto puede ser P1 y no CMP; puede ser CMP P1 y tener relaciones P2; una REF puede conectar dos CMP sin ser CMP; un parámetro PAR puede ser propiedad de un CMP sin ser CMP; un servicio externo puede ser P2 y no pertenecer al roster interno.

### 10.21.5. Estado y límites

Identidad CMP-SERVICE-LOGIC-001 continúa siendo la única identidad CMP concreta recuperada en el contrato de servicio de referencia, no el roster exhaustivo. N04–N07, N13–N15 y N20–N21 son candidatos/condicionales según la clasificación anterior, no instancias existentes. N01 y N17–N19 requieren descomposición adicional. No se asignan IDs ni versiones a candidatos.

La matriz no sella IAM, no adjudica membership de ningún CMP adicional, no cambia boundary_class, no añade columnas/FK/tablas, no crea registros U_G, no declara cobertura ni exclusión causal. No autoriza inspección técnica, captura de snapshots, parser, validator, fixtures, implementación, Design Freeze o ejecución. scientific_execution=false; execution_authorized=false.

## 10.22. Resolución conceptual de N01 — unidad lógica, host y S0

**Estado:** PROPUESTA DE DESAMBIGUACIÓN DOCUMENTAL — pendiente de aceptación. Reutiliza DEC-C10-058, DEC-C10-059, DEC-C10-064, DEC-C10-065 y el contrato de frontera §82. No crea instancias técnicas ni cambia las decisiones aceptadas.

### 10.22.1. Dictamen

N01 no debe conservarse como un único objeto indiferenciado «unidad/sistema anfitrión y S0». Esa etiqueta mezcla tres entidades conceptualmente distintas:

1. **Unidad lógica de servicio (objeto raíz):** identidad estable del servicio migrado, definida por contrato funcional/configuracional; independiente del host, pod, contenedor, clúster o ubicación. Es la unidad lógica del estudio, no una afirmación de que el host o toda la plataforma formen parte de ella.
2. **Host/entorno anfitrión (contexto P1):** infraestructura y realización técnica que alojan, ejecutan o condicionan el servicio. Deben representarse como NODE P1 separados solo cuando exista identidad/versión y alguna diferencia material de intervención, fallo, interfaz, permisos, recursos, exposición causal, ruta o evidencia conforme al contrato de granularidad §82. No se presupone host concreto ni que el entorno sea un único nodo.
3. **S0 (estado basal):** estado temporal observado de la unidad y su contexto antes de la intervención; pertenece al registro SNAPSHOT y a sus referencias exactas, no es un segundo CMP ni debe confundirse con el host. Un snapshot fija snapshot_id + snapshot_object_record_id y apunta a la revisión exacta del NODE raíz mediante la FK compuesta aceptada.

### 10.22.2. Proyección U_G

| Elemento | Representación | boundary_class | Condición |
|---|---|---|---|
| Unidad lógica de servicio | NODE raíz con semantic_role=LOGICAL_SERVICE_UNIT; identidad semántica estable en node_id | NA si actúa solo como contenedor de identidad, conforme DEC-C10-059 | Contrato lógico aceptado; identidad concreta de instancia/registro aún no poblada |
| Host físico/virtual | NODE P1 independiente, solo si supera criterio de granularidad | P1_ENVIRONMENT | Requiere inventario y evidencia de identidad/versión; no inferir del nombre de proveedor o ubicación |
| Runtime, SO, orquestador, red, storage y capacidad | NODE P1 por objeto/grupo técnicamente justificable | P1_ENVIRONMENT | Separar cuando existan ciclos de cambio, fallos, permisos, recursos o exposiciones materiales diferentes |
| S0 | SNAPSHOT basal con referencias exactas a unidad raíz y objetos observados | No aplica boundary_class a SNAPSHOT | Captura y evidencia aún no autorizadas ni realizadas |
| Dependencias/servicios externos | NODE P1 cuando realizan/condicionan el servicio; relaciones P2 en grafo causal | P1_ENVIRONMENT si aplica | Identidad/contrato/versión o caja negra observable; desconocimiento se mantiene ? |

La unidad lógica raíz no absorbe el host, el runtime ni los recursos. Tampoco se divide automáticamente en varios CMP por estar implementada en varios procesos: DEC-C10-058 permite varios procesos para un servicio lógico si comparten un contrato funcional/configuracional único. La separación se justifica por identidad y diferencias materiales, no por despliegue o nombre.

### 10.22.3. Identidad y anclaje

La identidad de la unidad lógica (unit_id) coincide con NODE.node_id del NODE raíz. SNAPSHOT.unit_object_record_id fija la revisión exacta de ese NODE; la FK compuesta incluye snapshot_id según DEC-C10-064/065. La revisión de NODE no se reescribe retroactivamente en snapshots históricos.

El CMP contractual CMP-SERVICE-LOGIC-001 no debe confundirse automáticamente con el NODE raíz: DEC-C10-082 exige un NODE anchor por CMP y snapshot, mientras que el NODE raíz representa la unidad lógica de servicio. Si el mismo objeto de dominio cumple ambas funciones, el mapping deberá declararlo explícitamente y demostrar identidad y cardinalidad; no se presupone que raíz y CMP sean idénticos ni que deban ser dos nodos distintos.

### 10.22.4. Estados y límites

La definición conceptual de unidad lógica y la clasificación P0/P1/P2 están aceptadas por DEC-C10-058; el dominio de boundary_class y la regla de raíz SNAPSHOT→NODE están aceptados por DEC-C10-059/064/065. Esta sección propone su aplicación sin ambigüedad a N01.

No se ha identificado host, entorno, runtime, clúster, servicio externo ni registro basal real. El inventario permanece sin observación y la cobertura NONE donde no existe inspección. No se asignan node_id, object_record_id, snapshot_id, component_id ni mapping IDs. No se sella IAM, no se declara roster exhaustivo y no se autoriza acceso técnico, captura de snapshots, implementación, Design Freeze o ejecución. scientific_execution=false; execution_authorized=false.
## 10.23. Aplicación aceptada de N01 — DEC-C10-089

**Estado:** ACCEPTED — DOCUMENTAL. Esta sección resuelve la propuesta §10.22.

Se acepta que NODE raíz `LOGICAL_SERVICE_UNIT` represente la unidad lógica de servicio, separada conceptualmente del host/entorno y de S0. S0 se representa como SNAPSHOT basal con pinning exacto de la revisión raíz. Host/runtime se descomponen como NODE P1 solo cuando satisfacen el criterio de granularidad y existe identidad/versión suficiente.

La relación entre NODE raíz y CMP-SERVICE-LOGIC-001 queda OPEN: no se presume identidad ni separación. Solo un mapping explícito, versionado y sustentado podrá resolverla, preservando DEC-C10-082. No se fuerzan uno o dos NODE ni se asignan IDs.

La aceptación es conceptual/documental. No hay identidad raíz observada, host inventariado, snapshots ni cobertura. No sella IAM ni autoriza acceso, captura, implementación, Design Freeze o ejecución. Véase DEC-C10-089.
## 10.24. Reconciliación de DEC-C10-089 con los contratos históricos CMP↔NODE

**Estado:** RECONCILIACIÓN DOCUMENTAL — aplicación de DEC-C10-089; no modifica DEC-C10-082.

La revisión histórica de §§10.6–10.7 detecta una precisión necesaria. §10.6 utilizaba la expresión «NODE raíz para el CMP focal», mientras que DEC-C10-082 acepta un NODE anchor único por CMP y snapshot. DEC-C10-089 establece que el NODE raíz `LOGICAL_SERVICE_UNIT` y CMP-SERVICE-LOGIC-001 no deben presumirse idénticos ni distintos.

Se resuelve la terminología del siguiente modo:
1. **NODE raíz de unidad lógica:** representa la unidad lógica de servicio del estudio.
2. **NODE anchor CMP:** registro U_G exacto que corresponde al CMP contractual en un snapshot conforme DEC-C10-082.
3. Ambas funciones pueden recaer en el mismo NODE únicamente si un mapping explícito demuestra que se trata del mismo objeto de dominio y satisface identidad/cardinalidad.
4. Si son objetos distintos, el NODE raíz y el NODE anchor CMP se mantienen diferenciados, con relaciones U_G explícitas y sin duplicar el anchor del CMP.
5. La regla 1:1 CMP↔NODE anchor de DEC-C10-082 permanece intacta. No implica que todo NODE raíz sea CMP ni que cada unidad lógica tenga necesariamente un CMP idéntico.
6. La frase «NODE raíz para el CMP» en §10.6 debe leerse como formulación histórica no adjudicativa; DEC-C10-089 gobierna la identidad de la unidad raíz.

Esta reconciliación evita tanto la inferencia de identidad como la inferencia de separación. No añade entidades ni cardinalidades, no cambia el esquema U_G y no crea mappings observados. Permanecen OPEN el mapping concreto, la identidad de registros, el snapshot y la evidencia. No sella IAM ni autoriza captura, implementación, Design Freeze o ejecución.
## 10.25. Resolución propuesta de N07 — endpoint, interfaz y servicio

**Estado:** PROPUESTA DOCUMENTAL — pendiente de aceptación. Reutiliza DEC-C10-058/059/076/077/082/089 y el contrato de granularidad §82. No declara endpoint observado ni crea identidades.

### 10.25.1. Descomposición semántica

La etiqueta N07 «endpoint/canal focal» puede mezclar tres objetos distintos que deben adjudicarse por separado:

1. **Endpoint técnico concreto:** dirección, URL, socket, puerto, topic, canal o punto de acceso desplegado. Por defecto es un atributo/recurso de interfaz del servicio o un NODE de entorno P1 si tiene identidad/versionado y relevancia material independiente. No es CMP por ser direccionable.
2. **Contrato/interfaz de comunicación:** especificación versionada de operaciones, protocolo, esquema, roles de extremo y reglas de intercambio. Puede representarse como REF solo cuando constituye un objeto de dominio con identidad propia y extremos tipados; si es una propiedad del CMP, se mantiene como atributo/artefacto contractual referenciado. No inferir REF desde un endpoint, FK o EDGE.
3. **Servicio/componente que atiende el endpoint:** CMP únicamente si posee identidad contractual component_id, clase y versión/revisión propias, lifecycle y frontera funcional diferenciados. Si el endpoint es una fachada o capacidad interna de un CMP, no se crea CMP adicional.

### 10.25.2. Regla de adjudicación

| Evidencia/condición | Clase candidata | Regla |
|---|---|---|
| URL/socket/puerto/topic sin identidad funcional autónoma | Atributo de interfaz o recurso P1 | No CMP ni REF automáticamente |
| Interfaz/contrato versionado con identidad y extremos tipados propios | REF | Registrar extremos SOURCE/TARGET y mapping explícito; conservar dirección y cardinalidad según DEC-C10-077 |
| Servicio atendido con component_id/versión y lifecycle autónomos | CMP | Roster IAM propio y NODE anchor por snapshot conforme DEC-C10-082 |
| Servicio externo consumido por la instancia focal | Externo / relación P2 | No incluir como CMP interno por consumo; registrar identidad externa, contrato, disponibilidad y límites si son observables |
| Canal compartido o recurso de infraestructura | P1/P2 según frontera y función | Separar solo si cumple granularidad; no convertirlo en CMP por ser una dependencia |

Un REF no se crea para cada conexión: la conexión observada puede ser EDGE; REF es un objeto del dominio con identidad propia. EDGE y REF no se infieren entre sí. El endpoint puede ser solo el valor técnico de un extremo de interfaz, no la entidad REF misma.

### 10.25.3. Preguntas independientes de control

Para cada candidato N07 se deberá resolver: (a) identidad y versión del endpoint; (b) identidad del contrato/interfaz; (c) identidad del servicio proveedor; (d) extremos y dirección; (e) interno/externo y boundary_class; (f) owner CMP; (g) snapshot y mapping exactos; (h) rutas F/A, fallback y compartición; (i) permisos, recursos y efectos de B; (j) evidencia y cobertura. La falta de información conserva UNKNOWN, no ausencia.

### 10.25.4. Estado y límites

No se conoce endpoint, protocolo, contrato de interfaz, servicio proveedor, topología ni registro técnico real. N07 queda semánticamente descompuesto como propuesta; ninguna clase se adjudica a una instancia concreta. No se asignan IDs, no se crean REF/EDGE/CMP, no se sella IAM ni se captura snapshot.

No autoriza inspección técnica, llamadas de red, pruebas de conectividad, acceso a credenciales, parser, validator, implementación, Design Freeze o ejecución científica. scientific_execution=false; execution_authorized=false.
## 10.26. Aplicación aceptada de N07 — DEC-C10-090

**Estado:** ACCEPTED — DOCUMENTAL. Esta sección formaliza la aceptación de la propuesta §10.25.

N07 queda descompuesto conceptualmente en endpoint técnico, contrato/interfaz de comunicación y servicio proveedor. Se aplican las reglas de clasificación de DEC-C10-090: endpoint no equivale automáticamente a CMP/REF; interfaz es REF solo con identidad de objeto y extremos tipados propios; servicio es CMP solo con identidad contractual, lifecycle y frontera autónomos; servicio externo no se incorpora al roster interno por mero consumo; EDGE y REF no se infieren entre sí.

La propuesta §10.25 queda aceptada como regla conceptual, no como adjudicación de objetos técnicos concretos. Permanecen OPEN identidades, protocolo, topología, mappings, rutas, snapshots, cobertura y evidencia. No se asignan IDs ni se crean registros; no se sella IAM ni se autoriza inspección, captura, implementación, Design Freeze o ejecución. Véase DEC-C10-090.
## 10.27. Resolución propuesta de N14 — contrato/formato, payload y transferencia

**Estado:** PROPUESTA DOCUMENTAL — pendiente de aceptación. Reutiliza N14 y E12/E13 de la plantilla U_G §10.2, B-M14 §17.2, DEC-C10-073/074/075/076/077/079/080 y la separación ya aceptada para N07 en DEC-C10-090. No crea una nueva entidad universal ni una tabla.

### 10.27.1. Hallazgo histórico y alcance

N14 ya existe en el catálogo U_G como «Formato/artefacto intercambio»; la plantilla indica versionar formato y artefacto cuando difieran. E12 (N13→N14) y E13 (N14→N15) son relaciones candidatas, no relaciones observadas. B-M14 ya incluye N14 entre los objetos candidatos para auditar alternativas. Por tanto, este gate refina una definición existente; no crea otro N14 ni sustituye el catálogo.

### 10.27.2. Descomposición semántica

Separar, como mínimo, tres planos:

1. **Definición de formato/contrato de intercambio:** especificación versionada que define sintaxis, estructura, tipos, codificación, reglas de compatibilidad y, cuando corresponda, semántica de campos. Se registra como referencia/artefacto contractual versionado. No es REF automáticamente: solo se clasifica REF si es un objeto de dominio con identidad propia y extremos tipados, según DEC-C10-077. Si es una propiedad o perfil interno de un CMP, permanece como metadato/artefacto referenciado de ese CMP.
2. **Payload/artefacto concreto:** instancia de datos producida por A1 y destinada a A2. Tiene identidad/procedencia de artefacto y versión o revisión propia, separada de la identidad/versionado del formato. Se representa como NODE/artefacto U_G solo si tiene identidad y relevancia causal/material independiente según §82; si no, se conserva como artefacto de transferencia/evidencia con sus referencias exactas, sin forzar un NODE.
3. **Transferencia y recepción:** eventos temporales distintos (producido, transmitido, recibido, parseado, validado y aplicado). No son estados intercambiables ni crean por sí solos un CMP/REF. La evidencia de cada transición se registra con su tiempo, actor, snapshot, ruta y procedencia; «recibido» no implica «validado» ni «aplicado».

El exportador A1 (N13) y el importador A2 (N15) siguen siendo actores/operaciones separados de N14. El endpoint/canal técnico corresponde al ámbito N07; el mapping de contenido fuente→payload→destino es M y no se confunde con el formato ni con el canal.

### 10.27.3. Identidad, versiones e integridad

- Identificar por separado `format_id + format_version`, `artifact_id + artifact_revision` (o equivalente contractual que se defina), y los identificadores/versiones de A1/A2 y de los snapshots fuente/destino. Estos nombres son etiquetas conceptuales de propuesta, no columnas ni IDs físicos aprobados.
- El mismo formato puede producir muchos payloads; un payload puede dividirse en partes o ser consumido por más de un proceso. No asumir cardinalidad 1:1 entre formato, artefacto, exportación e importación.
- Preservar lineage explícito entre snapshot/estado fuente, ejecución A1, artefacto producido, transferencia, recepción, ejecución A2 y estado destino. Si el payload se transforma durante transporte, conversión, normalización o empaquetado, registrar cada versión/etapa y su relación; no sobrescribir el artefacto previo.
- Hash/digest puede respaldar integridad de bytes en un punto definido, pero no demuestra identidad semántica, equivalencia de contenido, compatibilidad, aplicación ni éxito funcional. Registrar algoritmo, ámbito exacto (bytes/paquete/parte), etapa y procedencia; no comparar hashes de representaciones distintas como si fueran equivalencia.
- DEC-C10-074 y el perfil TGCV-C10S-JCS-1 gobiernan la canonicalización del envelope UDG-01; no se extienden automáticamente al payload de N14. La serialización del payload, su canonicalización y su hash requieren especificación propia si fueran necesarios.

### 10.27.4. Compatibilidad y evaluación

La compatibilidad debe evaluarse por separado en: (a) conformidad sintáctica con el formato; (b) compatibilidad semántica de campos/tipos; (c) resolución del mapping M; (d) integridad/procedencia del payload; (e) recepción y parseo; (f) aplicación efectiva en destino; y (g) criterio funcional F* común. El oráculo F* y su implementación permanecen separados del mecanismo A1/A2, conforme al catálogo N16.

La ruta alternativa A1→N14→A2 solo cuenta como alternativa funcional cuando se demuestra contra el mismo F*, frontera, granularidad G, horizonte H y condiciones comparables; su mera existencia documental o un payload recibido no demuestra Reach ni substituibilidad. Deben preservarse R0/R1 frente a R2 y auditarse vías colaterales B→A1/A2, formato, mapping, dependencias, permisos y recursos conforme B-M14/PROV. No inferir exclusión instrumental.

### 10.27.5. Estados y límites

Estados mínimos a mantener diferenciados: no generado; generado; transmitido; recibido; parseado; validado; aplicado; fallido; desconocido/no observable. La falta de registro no prueba que el evento no ocurriera. La evidencia se adjudica por etapa, artefacto, snapshot, ruta y cobertura; no se hereda entre etapas.

No se conoce formato, esquema, codificación, payload, herramienta, mapping M, endpoint, ni eventos de transferencia reales. No se asignan IDs, no se crean filas NODE/REF/EDGE/CMP, no se declara presencia/ausencia ni cobertura. No se sella IAM ni se autoriza acceso técnico, captura, parser, validator, fixtures, implementación, Design Freeze o ejecución científica. scientific_execution=false; execution_authorized=false.
## 10.28. Aplicación aceptada de N14 — DEC-C10-091

**Estado:** ACCEPTED — DOCUMENTAL. Se acepta §10.27 como refinamiento del N14 existente: definición versionada de formato/contrato, payload concreto y eventos separados de transferencia/recepción/parseo/validación/aplicación. Formato y payload tienen identidad/versionado separados; formato no es REF automáticamente; payload no es NODE automáticamente; N13/A1 y N15/A2 son productor y consumidor; N07 conserva endpoint/canal y M el mapping. E12/E13 siguen siendo candidatas, no observadas.

Se preservan las reglas de lineage, split/merge, integridad de bytes frente a equivalencia semántica y el alcance limitado de JCS al envelope UDG-01. La alternativa A1→N14→A2 requiere demostración contra el mismo F*, frontera, G y H; recepción no implica validación ni aplicación.

Permanecen OPEN los objetos y eventos reales, formato, payload, mapping, compatibilidad, aplicación, evidencia y cobertura. No se asignan IDs ni se crean filas; IAM no se sella. No autoriza captura, parser, validator, implementación, Design Freeze o ejecución. Véase DEC-C10-091.
## 10.29. Resolución propuesta de N15 — importador A2, procesamiento y aplicación

**Estado:** PROPUESTA DOCUMENTAL — pendiente de aceptación. Refina el N15 ya existente del catálogo U_G y reutiliza DEC-C10-071/082/083/084/086/087/088/090/091, la matriz abstracta §§15.6–15.9 y el crosswalk temporal §§10.1/10.19. No crea nuevas etapas `stage_key`, predicados FP/SM ni entidades U_G.

### 10.29.1. Identidad funcional de N15

N15 representa la función de importación A2, pero no se presume que sea un CMP autónomo. Distinguir:

1. **Capacidad/contrato A2:** función lógica de importar/aplicar un artefacto N14 en un destino. Es una capacidad del CMP owner salvo que exista un componente software separado con identidad contractual, versión, lifecycle y frontera autónomos conforme DEC-C10-090.
2. **Implementación A2:** software/herramienta concreta que realiza la función. Solo se registra como CMP independiente si satisface esos criterios; un comando, módulo, plugin o endpoint no crea CMP por su nombre.
3. **Ejecución A2:** instancia temporal de invocación/importación, con identidad de evento, instante, actor, entrada exacta, destino, ruta, resultado y provenance. No es un CMP ni se confunde con `stage_key`.

### 10.29.2. Cadena de procesamiento a distinguir

Para cada ruta y unidad de adjudicación, conservar los siguientes hitos como eventos/observaciones distintos:

1. **Entrada declarada (`A2_DST_DECL`):** artefacto/paquete que A2 declara que importará, con referencia exacta a N14, formato, versión, mapping y destino. La declaración no demuestra disponibilidad ni recepción.
2. **Recepción efectiva:** payload exacto recibido por la instancia A2, con identidad/revisión, integridad de bytes en el ámbito declarado, canal N07, evento y lineage. No se infiere desde el envío ni desde el artefacto declarado.
3. **Parseo/decodificación:** intento y resultado de interpretar bytes conforme al formato/versionado. Registrar por separado parse success, parse failure y causa; parsear no implica validez semántica.
4. **Validación estructural y semántica:** comprobar estructura, tipos, dominios, obligatoriedad y reglas aplicables al payload decodificado. Mantener conformidad sintáctica separada de conformidad semántica y de compatibilidad del destino.
5. **Resolución del mapping M:** resolver mapping_id/version para cada propiedad/clase/owner/versión/snapshot, incluidos split/merge, conversiones, pérdidas y elementos no mapeados. Mapping disponible o resuelto no prueba que se haya aplicado.
6. **Aplicación efectiva (FP-06):** evento trazable que aplica el paquete exacto al destino identificado. Reutilizar FP-06; no crear otro predicado de importación/aplicación.
7. **Verificación post-aplicación (FP-07):** snapshot/observación exacta del destino y adjudicación del estado real mediante FP-01…05 aplicables. Reutilizar FP-07; no derivar conformidad de un log o código de salida.
8. **Identidad y provenance (FP-08):** vincular formato, payload, recepción, ejecución A2, mapping, evento de aplicación, destino, snapshot y evidencia. FP-08 soporta, no sustituye, FP-06/FP-07.

### 10.29.3. Fallos y estados no intercambiables

Distinguir al menos: fallo de transporte/recepción; fallo de integridad del artefacto; formato/codificación desconocidos o incompatibles; parseo/decodificación; validación estructural; validación semántica/reglas; mapping ausente/ambiguo/incompatible; incompatibilidad del destino; fallo de aplicación; aplicación ejecutada con post-check fallido; y estado no observable.

El estado de cada hito se conserva como observado con su evidencia o UNKNOWN cuando falte cobertura. `RECEIVED` no implica `PARSED`; `PARSED` no implica `VALIDATED`; `VALIDATED` no implica `MAPPED`; `MAPPED` no implica `APPLIED`; `APPLIED` no implica `POSTCHECK_PASS`. La ausencia de registro no demuestra fallo ni ausencia de evento.

Los errores intermedios son diagnóstico/provenance y no nuevas familias confirmatorias. La adjudicación final continúa usando DEC-C10-085/086/087/088, FP-01…08 y los estados ya aceptados; no se duplican ni se suman predicados.

### 10.29.4. Tiempo, ruta y evidencia

El vocabulario `stage_key` sigue exactamente los siete valores aceptados por DEC-C10-071. Los hitos internos de A2 (recepción, parseo, validación y resolución M) no se convierten en nuevos `stage_key`: se registran como eventos temporales con identidad, instante DGP, actor, artefacto, etapa de configuración relacionada, ruta/route_record_id, snapshot, cobertura y provenance. `A2_DST_DECL` y `A2_DST_APPLIED` siguen representando declaración y estado efectivamente aplicado, no los pasos internos del importador.

F y A se adjudican independientemente. La evidencia no se hereda entre rutas ni etapas. La falta de cobertura, mapping o snapshot conserva UNKNOWN; incompatibilidad sin mapping aprobado produce NOT_COMPARABLE; FAIL requiere contradicción/no aplicación demostrada con cobertura suficiente. No se infiere ausencia a partir de registros faltantes.

### 10.29.5. Límites

No se conoce la implementación A2, su protocolo, formato concreto, parser, política de errores, estrategia transaccional, mapping físico ni destino real. No se adjudica N15 como CMP independiente ni se asignan IDs; no se crean registros NODE/EDGE/REF/CMP ni columnas. No se altera el catálogo U_G, los siete `stage_key`, F*, N16 ni los predicados FP existentes. IAM no se sella y no se declara cobertura.

No autoriza acceso técnico, captura, pruebas de importación/conectividad, parser, validator, fixtures, implementación, Design Freeze ni ejecución científica. `scientific_execution=false`; `execution_authorized=false`.

## 10.30. DEC-C10-092 — aceptación conceptual de N15 (importador A2)

**Estado:** ACCEPTED — DOCUMENTAL (2026-11-08).

Se acepta la descomposición conceptual de N15 propuesta en §10.29: distinguir capacidad/contrato A2, implementación concreta y ejecución temporal; separar entrada declarada, recepción efectiva, parseo, validación estructural/semántica, resolución del mapping M, aplicación FP-06, verificación post-aplicación FP-07 y procedencia FP-08. N15 no se presume CMP autónomo; solo se clasificará como CMP si se demuestra identidad contractual, lifecycle y frontera propios.

Se reutilizan los siete stage_key y los contratos FP-01…FP-08 y DEC-C10-086/087/088. Los hitos internos no crean etapas ni predicados confirmatorios. F y A permanecen independientes; la evidencia no se hereda entre etapas/rutas. La ausencia de registro no demuestra ausencia de evento.

**Pendiente:** implementación/protocolo A2, formato y parser reales, reglas de validación, mapping físico, destino, eventos, snapshots, cobertura y evidencia. La aceptación no adjudica N15 como CMP, no crea IDs/filas/columnas, no sella IAM ni autoriza captura, pruebas, parser, validator, implementación, Design Freeze o ejecución.


## 11. AB-01/02 — crosswalk semántico consolidado de la instancia de servicio (2026-11-10)

**Estado:** reconciliación documental reutilizando DEC-C10-054/068/069/071/079/080/082/083. No crea una nueva decisión, no sella IAM ni define schema físico.

### 11.1. Precedencia y trabajo histórico reutilizado

No se vuelve a definir lo ya aceptado:
- DEC-C10-054: AST declarativo acíclico, presupuesto 4/16/16, operadores y efectos REQUIRE/FORBID; UNKNOWN no se fuerza a booleano.
- DEC-C10-068/069: contrato funcional ENABLED/PROFILE/RUL y sus identidades/versiones.
- DEC-C10-071/083: siete stage_key y aplicabilidad/preservación PAR por etapa.
- DEC-C10-079/080/081: identidad append-only del manifiesto PAR, binding probatorio mediante COVERAGE_SCOPE y control independiente.
- DEC-C10-082: anclaje CMP↔NODE 1:1 por snapshot exacto.

La matriz de aplicabilidad §§18.6–18.7 ya resuelve los dos PAR en las siete etapas. Esta sección no la duplica ni modifica. Su función es integrar esas reglas con RUL, CMP, MET y la composición de mappings de las rutas.

### 11.2. Contrato lógico de la instancia

| Elemento | Identidad/semántica de referencia | Correspondencia lógica/U_G | Estado |
|---|---|---|---|
| CMP | CMP-SERVICE-LOGIC-001, clase SERVICE_LOGIC; contrato C10S-SVC-REQUEST-PROCESSOR v1.0.0; instancia C10S-SVC-REQUEST-PROCESSOR-001 rev1 | Un NODE anchor exacto por CMP y snapshot; pinning según DEC-C10-065/082 | Identidad aceptada; roster total y registros observados OPEN |
| PAR-ENABLED | PAR-SVC-ENABLED, BOOL, {false,true}, REQUIRED | Propiedad tipada del CMP owner; manifiesto PAR y COVERAGE_SCOPE; no NODE propio | Contrato y etapas aceptados por DEC-C10-068/083 |
| PAR-PROFILE | PAR-SVC-PROFILE, ENUM {STANDARD, READ_ONLY, DISABLED}, REQUIRED | Propiedad tipada del CMP owner; manifiesto PAR y COVERAGE_SCOPE; no NODE propio | Contrato y etapas aceptados por DEC-C10-068/083 |
| RUL | RUL-SVC-ENABLE-PROFILE-01, REQUIRE, scope de unidad lógica | Registro PREDICATE del snapshot exacto; operand bindings a las dos claves PAR | Semántica aceptada; mapping de registros/evidencia aún no instanciado |
| REF | Sin IDs aceptados | EDGE solo para relación constitutiva real con extremos/tipo/dirección propios | OPEN; no afirmar REF=0 ni inventar EDGE |
| POL | Ausente por diseño en el núcleo mínimo | Sin objeto POL en el DGP base; FP-05 permanece como gate separado cuando aplique | Regla de diseño aceptada |
| MET | Identidad contractual, versión, instancia, revisión y procedencia | Metadatos distribuidos en registros existentes, snapshots y evidencia; no tabla MET nueva | IDs/versiones aceptados; serialización/hash OPEN |

### 11.3. Mapping semántico de parámetros — reutilización de DEC-C10-083

Se fija como contrato semántico, no como mapping físico, la preservación de la identidad de parámetro y de su valor tipado:

- PAR-SVC-ENABLED: BOOL; no coerción, no inversión y no conversión implícita.
- PAR-SVC-PROFILE: símbolo del dominio semántico finito aceptado; no reetiquetado que cambie STANDARD/READ_ONLY/DISABLED ni ampliación del conjunto permitido por RUL.
- En C_SRC, F2_DST_DECL y A2_DST_DECL, ambos PAR deben estar presentes como VALUE tipado. No existe DEFAULT contractual aceptado.
- En F1_S2 y A1_S1, cada ruta preserva independientemente identidad, tipo, dominio, estado y valor. Un cambio de etiqueta/encoding físico solo es admisible si una tabla total, versionada y sin ambigüedad conserva el mismo símbolo semántico.
- En F2_DST_APPLIED y A2_DST_APPLIED, la conformidad exige observación del estado aplicado real; no se infiere desde el destino declarado.
- ABSENT/NULL confirmados con cobertura suficiente incumplen el contrato REQUIRED; falta de snapshot, mapping o cobertura produce UNKNOWN, nunca ABSENT/NA inferidos.

No se asignan valores por unidad ni escenario. Los siete stage_key, la identidad de fila PAR, su supersession y el vínculo probatorio se rigen por DEC-C10-071/079/080/083 y sus contratos vigentes.

### 11.4. Mapping semántico de RUL y AST

La verdad funcional aceptada es:

OR(NEQ(PAR-SVC-ENABLED,true),IN(PAR-SVC-PROFILE,{STANDARD,READ_ONLY})) bajo efecto REQUIRE.

El mapping de RUL entre C_SRC, S2/S1, destinos declarados y destinos aplicados debe conservar conjuntamente:
1. identidad RUL-SVC-ENABLE-PROFILE-01 y versión contractual;
2. owner CMP exacto y scope de unidad lógica;
3. operador OR, átomos NEQ e IN, constantes y conjunto ENUM;
4. exactamente dos operand bindings tipados: ENABLED→PAR-SVC-ENABLED/BOOL; PROFILE→PAR-SVC-PROFILE/ENUM;
5. efecto REQUIRE, semántica TRUE/FALSE/UNKNOWN y presupuesto AST 4/16/16.

Los bindings son referencias tipadas desde el AST a propiedades PAR; no son objetos REF ni aristas EDGE. No se permite reordenar, simplificar, invertir ni ampliar la regla por conveniencia de serialización. Una representación física distinta solo podrá aceptarse tras demostrar que se decodifica a la misma estructura/semántica abstracta mediante mapping versionado. No se define aquí una sintaxis serializada ni un algoritmo de canonicalización.

### 11.5. Composición de rutas y significado de M

Se distinguen cuatro mappings de etapa y dos mappings de ruta completa:

- M_F1_sem: C_SRC → F1_S2; M_F2_sem: F1_S2 → F2_DST_DECL.
- M_A1_sem: C_SRC → A1_S1; M_A2_sem: A1_S1 → A2_DST_DECL.
- M_F_sem = M_F2_sem ∘ M_F1_sem; M_A_sem = M_A2_sem ∘ M_A1_sem.

Ambas rutas se juzgan contra la misma instancia lógica, dominio semántico, RUL y criterio F*. Que compartan invariantes semánticos no las hace el mismo mecanismo: la independencia técnica de A1/A2 respecto de B y la no-afectación se evalúan separadamente en R0–R3 y no quedan demostradas por este crosswalk.

Cada mapping futuro deberá tener ID/versión, cobertura por clase/propiedad, correspondencias explícitas y estado MAPPED, UNMAPPED, AMBIGUOUS o NOT_APPLICABLE. No se asignan todavía mapping_id/version ni se declara un mapping material completo. Los estados desconocidos no se convierten en eliminación, default, NA o equivalencia.

### 11.6. Reconciliación de representación sin duplicar U_G

- CMP: NODE anchor exacto por snapshot conforme a DEC-C10-082.
- PAR: propiedad del CMP owner y registro de manifiesto/coverage conforme a DEC-C10-079/080; no crear NODE por parámetro ni FK PAR inexistente.
- RUL: PREDICATE y referencias tipadas a operandos/owner; no convertir bindings AST→PAR en EDGE.
- REF: EDGE solo tras inventario de relación constitutiva; el roster desconocido no autoriza REF=0.
- MET: reutilizar metadatos y registros existentes; no crear tabla MET por conveniencia.
- Evidencia/procedencia/cobertura: reutilizar EVIDENCE_REGISTER, COVERAGE_REGISTER, CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER; respetar pinning de snapshot exacto.

No se añaden columnas, tablas, FKs ni nuevos tipos U_G. JCS UDG-01 no se extiende al payload/AST de configuración.

### 11.7. Dictamen AB-01/02

- AB-01: binding AST→PAR semánticamente resuelto; representación física del AST, schema/encoding, escaping, canonicalización y constraints OPEN.
- AB-02: mapping semántico de los dos PAR por siete etapas aceptado por DEC-C10-083 y reconciliado aquí con CMP/RUL/U_G; mappings versionados materiales, REF exhaustivo, registro RUL por snapshot y evidencia de destinos aplicados OPEN.

No se declara IAM sellado, REF=0, schema freeze, oráculo validado ni DGP autocontenido. Sin fixtures, parser, validator, implementación, simulación ni ejecución científica. scientific_execution=false; execution_authorized=false.
