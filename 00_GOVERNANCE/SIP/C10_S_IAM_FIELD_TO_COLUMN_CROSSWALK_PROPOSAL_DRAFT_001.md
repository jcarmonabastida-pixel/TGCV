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
