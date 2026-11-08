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
