# C10-S — Plantilla de inventario U_G y registro de evidencia

**ID:** C10-S-UG-INVENTORY-TEMPLATE-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05
**Estado:** DRAFT / PLANTILLA VACÍA / NO INVENTARIADA / NO EJECUTADA.
**Dependencias:** C10-S §§80–82; contratos de frontera/granularidad, cobertura trivalente, identidad/snapshots, Reach y DGP.

## 1. Propósito y reglas de uso

Esta plantilla instancia el catálogo U_G sin inventar componentes, relaciones, rutas, valores de predicados ni cobertura. Es un esquema de captura, no evidencia de que un nodo/arista exista o no exista. La plantilla vacía no permite inferir ausencia ni exhaustividad.

Reglas obligatorias:
- Una fila representa una entidad versionada y con identidad; usar IDs persistentes, no nombres ambiguos.
- Registrar por separado nodos, aristas, rutas y predicados.
- Usar 1, 0, ?, NA solo según contrato; MISSING, NO INVENTARIADO, NONE y PARTIAL son estados de inventario/cobertura, no truth estructural.
- No derivar accesibilidad, aplicabilidad, Reach o ausencia de alternativa desde Outcome/Value.
- No declarar independencia de B sin análisis de dependencias transitivas y evidencia pre/post.
- No usar 0 por falta de observación. Todo 0 requiere evidencia válida y cobertura suficiente para el predicado concreto.
- Toda afirmación observada debe reconstruir su procedencia mediante CLAIM_EVIDENCE_LINK → EVIDENCE_REGISTER; cada objeto conserva identidad, versión, fecha, responsable y limitaciones aplicables.

## 2. Registro de nodos

| node_id | semantic_role | class | boundary_class (P0_CONFIG/P1_ENVIRONMENT/DUAL_P0_P1/NA) | TID | SID | RID | version/build/hash | owner/boundary | consumers/routes/arms | direct_dependencies | external/shared_resource | permissions/state | evidence_ref (0..1 optional) | observed_state (1/0/?) | coverage_status (NONE/PARTIAL/COMPLETE) | timestamp | notes/unknowns | evaluator_record_ids | object_record_id | parent_catalog_id | object_version | coverage_scope_id | evidence_status (AVAILABLE/MISSING/CONFLICTING) | review_adjudication_status | unknown_reason | contract_intent | created_at | recorded_by | supersedes_record_id  | snapshot_id | snapshot_object_record_id |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|--- | --- | — |
| — | NO INVENTARIADO | — | NA | — | — | — | — | — | — | — | — | — | — | ? | NONE | — | Marcador NA de plantilla; no es observación ni clasificación real | — | — | — | — | — | MISSING | NOT_REVIEWED | — | — | — | — | —  | — | — |

## 3. Registro de aristas/dependencias

| edge_id | atomic_edge_id | parent_edge_id | source_node_id | target_node_id | relation_type | direction | direct_or_transitive | version_constraint | time_window | condition | arms/routes_affected | resource_or_permission | necessary_for_path | evidence_ref (0..1 optional) | observed_state (1/0/?) | coverage_status | timestamp | unknowns | evaluator_record_ids | object_record_id | parent_catalog_id | object_version | coverage_scope_id | evidence_status (AVAILABLE/MISSING/CONFLICTING) | review_adjudication_status | unknown_reason | contract_intent | created_at | recorded_by | supersedes_record_id  | snapshot_id | snapshot_object_record_id | source_node_record_id | target_node_record_id |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|--- | --- | — | --- | --- |
| — | — | — | — | — | NO INVENTARIADO | — | — | — | — | — | — | — | ? | — | ? | NONE | — | Fila de esquema; no representa dependencia real | — | — | — | — | — | MISSING | NOT_REVIEWED | — | — | — | — | —  | — | — | — | — |

## 4. Registro de rutas y substituibilidad

| route_id | parent_route_class (Rτ2/RA12/Rshared/Rexternal/Runknown) | route_subtype (native/manual/fallback/recovery/other) | entry_state | target/F* | G | H/window | C0/constraints | version_set | shared_dependencies | affected_by_B | functional_substitutability (1/0/?) | evidence_ref (0..1 optional) | coverage_scope_id | evaluator_record_ids | unresolved_alternatives | notes | observed_state (1/0/?) | object_record_id | parent_catalog_id | object_version | evidence_status (AVAILABLE/MISSING/CONFLICTING) | review_adjudication_status | unknown_reason | contract_intent | created_at | recorded_by | supersedes_record_id  | snapshot_id | snapshot_object_record_id |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|--- | --- | — |
| — | Runknown | unknown | — | — | — | — | — | — | — | ? | ? | — | — | — | Runknown | Fila de esquema; no representa ruta real | ? | — | — | — | MISSING | NOT_REVIEWED | — | — | — | — | —  | — | — |


### 4.1. Registro normalizado de pasos de ruta (ROUTE_STEP)

Una fila por paso ordenado. ROUTE_STEP sustituye a `ordered_node_edge_sequence` como fuente canónica; el campo serializado de ROUTE, si se conserva, será una vista/export derivado.

| route_step_id | snapshot_id | snapshot_object_record_id | route_record_id | step_index | step_type (NODE/EDGE) | node_record_id (nullable) | edge_record_id (nullable) |
|---|---| — |---|---|---|---|---|
| — | — | — | — | — | — | — | — |

Invariantes: exactamente uno de node_record_id/edge_record_id no nulo y coherente con step_type; FK `(snapshot_id,snapshot_object_record_id)` → SNAPSHOT(`snapshot_id,object_record_id`); FKs a ROUTE/NODE/EDGE con el mismo par exacto `(snapshot_id,snapshot_object_record_id)` y el record ID de destino correspondiente; step_index entero positivo, único y contiguo por route_record_id; continuidad de extremos de EDGE con los NODE adyacentes. La continuidad es una regla cross-row que requiere constraint/trigger verificable o validador independiente y pruebas negativas. No se han creado pasos reales.

## 5. Registro de predicados por ruta/paso/tiempo

| predicate_id | route_id | step | time/snapshot | predicate_type (ID/REL/COND/AUTH/RES/DEP/BLOCK/APP/ALT/ORACLE/EXT) | observed_state (1/0/?) | evidence_ref (0..1 optional) | coverage_scope_id | source/version/hash | adjudication_rule/tolerance | evaluator_record_ids | reason_for_unknown | impact_on_A_f/App/Reach/F_alt/IV | timestamp | object_record_id | parent_catalog_id | object_version | evidence_status (AVAILABLE/MISSING/CONFLICTING) | review_adjudication_status | unknown_reason | contract_intent | created_at | recorded_by | supersedes_record_id  | snapshot_id | snapshot_object_record_id | route_record_id |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|--- | --- | — | --- |
| — | — | — | — | — | ? | — | — | — | — | — | No existe evidencia aportada | Mantener indeterminación | — | — | — | — | MISSING | NOT_REVIEWED | — | — | — | — | —  | — | — | — |

**La truth del DGP no forma parte de esta tabla ni de ningún artefacto visible al analizador.** Se almacena únicamente en un registro separado, segregado y con control de acceso del generador/evaluador autorizado. Esta plantilla contiene solo observed_state y evidence_ref.

## 6. Registro de snapshots y fuentes

| snapshot_id | unit_id | unit_object_record_id (FK raíz: SNAPSHOT(snapshot_id,object_record_id,unit_object_record_id,unit_id) → NODE(snapshot_id,snapshot_object_record_id,object_record_id,node_id); semantic_role=LOGICAL_SERVICE_UNIT) | phase (baseline/post-B/rollback/route-test) | timestamp | scope | source_artifacts | version/hash | method | coverage_limitations | custodian | integrity_check | evidence_ref (0..1 optional) | observed_state (1/0/?) | evaluator_record_ids | object_record_id | parent_catalog_id | object_version | coverage_scope_id | evidence_status (AVAILABLE/MISSING/CONFLICTING) | review_adjudication_status | unknown_reason | contract_intent | created_at | recorded_by | supersedes_record_id |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | No capturado | — | — | — | NA | — | — | — | — | — | MISSING | NOT_REVIEWED | — | — | — | — | — |

## 7. Matriz de cobertura por dimensión

| dimension | declared_universe | sources_examined | covered_scope | omitted/opaque | status (NONE/PARTIAL/COMPLETE) | justification | reviewer | date |
|---|---|---|---|---|---|---|---|---|
| Componentes/paquetes | — | — | — | — | NONE | Sin inventario observado | — | — |
| Dependencias directas | — | — | — | — | NONE | Sin manifiesto/relaciones observadas | — | — |
| Dependencias transitivas/carga dinámica | — | — | — | — | NONE | Sin grafo transitivo | — | — |
| Interfaces/canales | — | — | — | — | NONE | Sin evidencia | — | — |
| Datos/estado | — | — | — | — | NONE | Sin snapshots | — | — |
| Permisos/autorizaciones | — | — | — | — | NONE | Sin diff de permisos | — | — |
| Recursos/capacidad/contención | — | — | — | — | NONE | Sin mediciones/inventario | — | — |
| Alternativas funcionales | — | — | — | — | NONE | F* y universo no cerrados | — | — |
| Servicios externos/opacos | — | — | — | — | NONE | Sin catálogo externo | — | — |
| Tiempo/versiones/ventanas | — | — | — | — | NONE | Sin snapshots comparables | — | — |
| Observabilidad/telemetría | — | — | — | — | NONE | Sin fuentes | — | — |
| Evidencia/adjudicación | — | — | — | — | NONE | Sin evaluadores ni adjudicación | — | — |

## 8. Reglas de clasificación y parada

- COMPLETE solo se aplica al universo operativo declarado y versionado, nunca como exhaustividad ontológica absoluta.
- Una dependencia crítica desconocida impide declarar independencia de rutas.
- Una ruta externa/opaca no resuelta mantiene Reach/F_alt en ? cuando puede ser relevante.
- Reach=0 requiere universo de rutas exhaustivo y todas las rutas descartadas con evidencia válida.
- F_alt,0=0 requiere descartar toda ruta funcionalmente substituible dentro de frontera, G, H, C0 y F* explícitos.
- Si B afecta o puede afectar una ruta alternativa, recurso, permiso, servicio o estado compartido, registrar vía colateral y no interpretar el contraste como efecto focal exclusivo.
- Discrepancias entre evaluadores se conservan; no se promedian estados categóricos. Adjudicación independiente documenta regla y fundamento.
- Si F*, frontera, G o H no están fijados, marcar inventario como PRELIMINAR / NOT_COMPARABLE donde corresponda.

## 9. Estado inicial de la plantilla

La plantilla se entrega vacía de observaciones reales. Todos los registros de ejemplo son filas de esquema, no nodos, aristas o rutas existentes. Cobertura NONE; A_f*=?, F_alt,0=?, Reach_H=?. No hay evidencia de instalación, runtime, SBOM, snapshots, grafo de dependencias, no-afectación A1/A2 ni independencia de B. Los valores NA en las filas ilustrativas de NODE.boundary_class y SNAPSHOT.observed_state son exclusivamente marcadores de plantilla; no se interpretan como valores de registros reales. En filas reales, NA exige justificación según los contratos aplicables. Los NA de las filas ilustrativas NODE/SNAPSHOT son marcadores de plantilla, no valores de registros reales. En filas reales, NA exige justificación. No se ha ejecutado auditoría técnica, simulación ni experimento.


## 10. Crosswalk explícito con U_G §81 (reconciliación Draft 001)

**Dictamen:** correspondencia semántica 23/23 roles de nodo, 23/23 IDs padre de arista, 14/14 predicados y 5/5 clases de ruta. La correspondencia es semántica, no evidencia de existencia. Todos los estados siguen ? y cobertura NONE.

### 10.1. Roles de nodo N01–N23

| ID | Rol U_G | Registro | Observación |
|---|---|---|---|
| N01 | Unidad/sistema anfitrión y S0 | Nodo | Separar unidad y snapshot S0 si tienen identidad propia. |
| N02 | Asignación Z | Nodo/evento | Distinguir asignación Z de política B recibida. |
| N03 | Política/proceso B | Nodo/evento | Diferenciar política asignada, intento de provisión y provisión recibida. |
| N04 | Paquete adaptador focal | Nodo | Registrar identidad y versión. |
| N05 | Runtime/sidecar focal | Nodo | Separar runtime/configuración si difieren en ciclo de vida o fallo. |
| N06 | Librerías/dependencias focales | Nodos | Desagregar dependencias por identidad/versión material. |
| N07 | Endpoint/canal focal | Nodo | Distinguir interfaz lógica, endpoint desplegado y permisos cuando proceda. |
| N08 | C_dep | Variable/medición | No asumir componente físico; registrar estado derivado y componentes constituyentes. |
| N09 | Predicados A_f* | Constructo/variable | No tratar cada predicado como nodo técnico. |
| N10 | Transformación focal τ2/F1 | Transformación | Distinguir definición/versionado de evento de ejecución. |
| N11 | Aplicación F2 | Transformación | Distinguir definición de F2 y su ejecución. |
| N12 | Estado destino | Estado/snapshot | Identificar por unidad, versión y tiempo. |
| N13 | Exportador A1 | Nodo/transformación alternativa | Distinguir capacidad, implementación y ejecución. |
| N14 | Formato/artefacto intercambio | Nodo/artefacto | Versionar formato y artefacto concreto cuando difieran. |
| N15 | Importador A2 | Nodo/transformación alternativa | Distinguir capacidad, implementación y ejecución. |
| N16 | Oráculo/criterio F* | Criterio/medición | Separar definición de F*, oráculo implementado y adjudicación. |
| N17 | Autorizaciones C_auth | Política/condición | Separar política, principal/rol, permiso efectivo y evento. |
| N18 | Recursos/capacidad compartida | Recurso | Separar capacidad instalada, pool disponible, reserva y consumo. |
| N19 | Configuración fuente/destino | Datos/estado | Separar fuente, destino y snapshots/versiones. |
| N20 | Dependencias/API/servicios compartidos | Nodos/dependencias | Desagregar servicios/APIs y registrar consumidores/transitividad. |
| N21 | Servicios externos | Nodos externos | Un nodo por servicio/contrato/versión material; opacos siguen ?. |
| N22 | Información/conocimiento agente | Variable/mecanismo | Separar información disponible, conocimiento, consideración y selección. |
| N23 | Ejecución/Outcome/Value | Resultado compuesto | No es unidad única válida por defecto: separar ejecución, Outcome y Value/contextual valuation con reloj t7/t8/t9. |

### 10.2. Aristas E01–E23 y normalización

Conservar los 23 IDs originales como parent_edge_id. Una relación mult destino se registra como una fila por par origen-destino. Los IDs atómicos siguientes son claves propuestas, no relaciones observadas.

| ID padre | Filas atómicas candidatas | Regla |
|---|---|---|
| E01 | E01 | Z→B |
| E02 | E02 | B→N04 |
| E03 | E03 | N04→N05 |
| E04 | E04 | N05→N06; desagregar por dependencia real. |
| E05 | E05 | N05→N07 |
| E06 | E06 | N07→N08; medición/verificación, C_dep no equivale a A_f*. |
| E07 | Ninguna arista técnica | Relación lógica/conjuntiva N04–N08→N09; registrar como regla de derivación, no edge binario. |
| E08 | E08 | N09→N10; separar accesibilidad de invocación/ejecución. |
| E09 | E09 | N10→N11 |
| E10 | E10 | N11→N12 |
| E11 | E11 | N01→N13 |
| E12 | E12 | N13→N14 |
| E13 | E13 | N14→N15 |
| E14 | E14 | N15→N12 |
| E15 | E15 | N12→N16; evaluación observa el estado, no necesariamente lo causa. |
| E16 | E16 | N18→N05 |
| E17 | E17.1 (N18→N13); E17.2 (N18→N15) | Dos filas; no presumir pool compartido real. |
| E18 | E18.1 (N17→N07); E18.2 (N17→N10); E18.3 (N17→N11); E18.4 (N17→N13); E18.5 (N17→N15) | Cinco relaciones potenciales; autorización por operación/tiempo. |
| E19 | E19.1 (N20→N05); E19.2 (N20→N13); E19.3 (N20→N15) | Tres relaciones potenciales; ampliar por dependencia/consumidor. |
| E20 | E20.1 (N21→N04); E20.2 (N21→N05); E20.3 (N21→N07); E20.4 (N21→N13); E20.5 (N21→N15) | Cinco relaciones potenciales; desagregar servicio/contrato/versión. |
| E21 | E21.1 (N19→N10); E21.2 (N19→N11); E21.3 (N19→N13); E21.4 (N19→N15) | Cuatro relaciones potenciales; desagregar fuente/destino y snapshots. |
| E22 | E22.1 (N22→selección); E22.2 (N22→ejecución) | Destinos sin IDs explícitos en U_G; definir como eventos/variables, no inventar nodos técnicos. |
| E23 | E23.1 (N10→ejecución); E23.2 (N11→ejecución); E23.3 (N15→ejecución) | Tres relaciones candidatas; separar además ejecución→Outcome y Outcome→Value en el modelo causal si aplica. |

Resultado: **39 filas binarias candidatas** derivadas de E01–E06 y E08–E23; E07 es regla lógica, no arista. No son 39 dependencias observadas. La topología definitiva puede cambiar tras inventario y adjudicación.

### 10.3. Los 14 predicados

| Código U_G | Familia en plantilla | Momento y regla |
|---|---|---|
| ID-τ2 | ID | t−1,t2; TID/SID/RID, mapping y versión. |
| REL-τ2 | REL | t2–t3; canal lógico y endpoint desplegado. |
| COND-τ2 | COND | t−1,t3; precondiciones y S0. |
| AUTH-τ2 | AUTH | t−1,t3; política y permisos efectivos; cambios por B. |
| RES-τ2 | RES | t1–t3; capacidad, pool, reserva y ventana. |
| DEP-τ2 | DEP | t1–t3; dependencias transitivas, integridad y compatibilidad; C_dep es subconjunto técnico. |
| BLOCK-τ2 | BLOCK | t−1–t3; bloqueos y cobertura suficiente. |
| APP-τ2 | APP | t3; aplicabilidad desde S0, distinta de A_f*. |
| ALT-A1 | ALT | t−1–t3; conservar código exacto en predicate_id. |
| ALT-A2 | ALT | t−1–t3; conservar código exacto en predicate_id. |
| ALT-DEP | ALT | t−1–t3; dependencia directa/transitiva y afectación por B. |
| ALT-F* | ALT | t3,t7,t8; F*, C0, G, H, restricciones y tolerancias comunes. |
| ORACLE | ORACLE | t−1–t8; separar F*, oráculo implementado, versión y cegamiento. |
| EXT | EXT | t−1–t3; servicios externos/opacos y cobertura. |

El código completo va en predicate_id; predicate_type solo identifica la familia. Truth DGP y estado observado permanecen separados.

### 10.4. Las cinco clases de ruta

| Clase U_G | route_class | Regla |
|---|---|---|
| Rτ2 | focal | Ruta focal potencial, no ejecución. |
| RA12 | alternative | Ruta A1→A2; evaluar F* separadamente. |
| Rshared | shared | Exposición compartida; puede ser variante de Rτ2/RA12, no ruta disjunta. |
| Rexternal | external | Ruta con servicio externo; opacidad mantiene ?. |
| Runknown | unknown | Clase abierta; no convertirla en ruta ficticia enumerada. |

Native/manual/fallback/recovery son subtipos descriptivos, no sustitutos de las cinco clases primarias. Añadir route_subtype y conservar parent_route_class.

### 10.5. Campos complementarios y dictamen

Añadir a los registros node/edge/route/predicate: parent_catalog_id, evidence_status (AVAILABLE/MISSING/CONFLICTING), contract_intent (intención normativa, no observación), coverage_scope_id, review/adjudication_status y unknown_reason. La procedencia de la fuente se registra una sola vez en EVIDENCE_REGISTER y se enlaza desde las afirmaciones. Para aristas, parent_edge_id y atomic_edge_id; para rutas, route_subtype y parent_route_class. Para predicados, predicate_id completo y separación truth_dgp_restricted / observed_state.

**Dictamen:** correspondencia semántica completa en los cuatro catálogos; normalización necesaria de aristas mult destino; E07 es regla lógica; E22 carece de nodos destino identificados; N16 y N23 tienen granularidad compuesta que debe revisarse. La plantilla necesita los campos complementarios anteriores antes de cerrar su esquema. No se asignan estados técnicos ni se declara inventario completo.


### 10.6. Definición de campos complementarios (schema)

Los campos siguientes forman parte del esquema de registro en las tablas indicadas; la procedencia de la fuente se normaliza exclusivamente en EVIDENCE_REGISTER (§12.1), no se duplica en NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT:

| Campo | Aplicación | Dominio/uso |
|---|---|---|
| parent_catalog_id | Nodo/arista/predicado/ruta | ID de catálogo U_G de origen (Nxx, Exx, código de predicado o clase de ruta). |
| evidence_status | Todas | AVAILABLE / MISSING / CONFLICTING; no sustituye observed_status. |
| contract_intent | Nodo/arista/ruta/predicado | Requisito normativo de diseño, separado de observación. |
| coverage_scope_id | Todas | Identificador de la frontera/universo operativo y versión a la que aplica la cobertura. |
| review_adjudication_status | Todas | NOT_REVIEWED / INDEPENDENT_REVIEWED / DISAGREEMENT / ADJUDICATED. |
| unknown_reason | Todas | Motivo concreto del estado ?, fuente faltante y consecuencia sobre clasificación. |
| parent_edge_id | Aristas | ID padre E01–E23 conservado para trazabilidad. |
| atomic_edge_id | Aristas | ID único por relación origen-destino; requerido para mult destino. |
| route_subtype | Rutas | native/manual/fallback/recovery u otro subtipo; no sustituye clase primaria. |
| parent_route_class | Rutas | Rτ2/RA12/Rshared/Rexternal/Runknown exacta. |
| truth_dgp_restricted | Predicados | Campo reservado al generador/evaluador; acceso restringido, nunca expuesto al analizador. |
| observed_state | Predicados | 1/0/? basado en evidencia observacional y regla de adjudicación. |

Los campos existentes evidence_ref, observed_status, coverage_status, evaluator/blinding y timestamp se conservan. Si se registra un estado observado 0, evidence_status debe ser AVAILABLE y coverage_status debe justificar cobertura suficiente para ese predicado. CONFLICTING fuerza ? hasta adjudicación; MISSING no equivale a 0.


## 11. Protocolo de fuentes y adjudicación (cross-reference)

La captura de evidencias, los campos de procedencia, la clasificación 1/0/? y la cobertura NONE/PARTIAL/COMPLETE se rigen por C10_S_UG_EVIDENCE_PROVENANCE_AND_ADJUDICATION_PROTOCOL_DRAFT_001.md. Esa especificación prevalece para reglas de evidencia y adjudicación; esta plantilla define las tablas de captura.

Cuando `evidence_ref` esté poblado, debe resolver a un `claim_evidence_id` existente de CLAIM_EVIDENCE_LINK; el campo es opcional y no representa el conjunto completo de evidencias. Para instancias con `observed_state=1` o `0` se exige al menos un vínculo válido en CLAIM_EVIDENCE_LINK, con alcance compatible. Para `observed_state=?` se registra evidencia vinculada si existe; si no existe, deben consignarse `unknown_reason`, `evidence_status=MISSING` y las limitaciones de búsqueda/cobertura, sin fabricar un vínculo. `NA` requiere justificación de no aplicabilidad y no exige vínculo de evidencia por defecto. Los campos source_provenance, collection_method, scope, timestamp, integrity, access_lineage, completeness_limitations, evidence_status, reviewer y reproducibility se registran en el expediente de evidencia enlazado cuando exista. observed_status/observed_state y coverage_status nunca se sustituyen por evidence_status. Ningún 0 se admite sin argumento de cobertura negativa; ningún COMPLETE sin universo, denominador y excepciones. Las discrepancias críticas requieren adjudicación independiente y preservación del desacuerdo. **Regla documental aceptada para C10-S por decisión del usuario de 2026-11-05.** La aceptación no equivale a validación técnica ni freeze.

El crosswalk §10 identifica columnas comunes que deben estar presentes en las tablas de objetos. `source_provenance` no es una columna de esas tablas: su registro canónico es EVIDENCE_REGISTER; los objetos se vinculan a la evidencia mediante CLAIM_EVIDENCE_LINK. La revisión de correspondencia de todas las columnas sigue abierta.



**Nota de normalización:** la tabla de §7 es una vista-resumen legible de cobertura; el registro canónico por dimensión es `COVERAGE_REGISTER` (§12.3). Las tablas de §§2–6 son ahora instancias físicas de captura y deben contener las columnas comunes de §12.7, añadidas explícitamente a sus encabezados. Los campos `observed_state` se aplican solo cuando el objeto admite clasificación trivalente; para snapshots se registra `NA` cuando no sea una afirmación de presencia/ausencia.

## 12. Esquema canónico normalizado de captura (Draft 001)

Esta sección es normativa para futuras instancias de la plantilla y resuelve la insuficiencia de las tablas abreviadas §§2–7. Los encabezados abreviados anteriores sirven como vistas de trabajo; cuando difieran, prevalece el esquema normalizado de esta sección. Ninguna fila de ejemplo constituye observación.

### 12.1. Registro de evidencia (EVIDENCE_REGISTER)

Una fila por artefacto/fuente y versión exacta. Un mismo evidence_id puede respaldar varias afirmaciones; cada vínculo claim-evidence se registra en CLAIM_EVIDENCE_LINK.

| evidence_id | source_class (S1–S8) | source_type | source_provenance | source_location_ref | custodian | collection_method/tool_version | scope_id | unit/environment | version_identity | timestamp_start/end_tz | integrity_hash/signature | access_lineage | completeness_limitations | confidentiality/access_ref | evidence_status | reviewer_id | reproducibility_ref |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | MISSING | — | — |

No incluir secretos, credenciales ni datos personales innecesarios. source_location_ref debe ser referencia segura, no volcado de material sensible.

### 12.2. Registro de vínculo afirmación-evidencia (CLAIM_EVIDENCE_LINK)

| claim_evidence_id | claim_target_type (NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT/COVERAGE_SCOPE) | target_node_record_id (FK nullable) | target_edge_record_id (FK nullable) | target_route_record_id (FK nullable) | target_predicate_record_id (FK nullable) | target_snapshot_record_id (FK nullable) | target_coverage_scope_id (FK nullable) | claim_statement | evidence_id (FK EVIDENCE_REGISTER) | support_type (direct/inferred/contradictory/contextual) | relevance_scope | evaluator_record_id (optional FK) | adjudication_id (optional FK) | reviewer_note |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|—|—|—|—|—|—|—|—|—|—|—|—|—|—|—|

Toda fila de nodo, arista, predicado, ruta o cobertura debe enlazar al menos un claim_evidence_id cuando tenga una clasificación observada. Una fila ? puede tener cero evidencia disponible, pero debe registrar unknown_reason.

### 12.3. Registro normalizado de cobertura (COVERAGE_REGISTER)

| coverage_scope_id | dimension | universe_definition/version | denominator_unit_and_count | expected_sources | examined_sources | valid_sources | covered_units/count | excluded_units/reason | opaque_or_unknown_units/count | status (NONE/PARTIAL/COMPLETE) | completion_rule | exceptions_and_impact | reviewer_id | timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — | NONE | — | — | — | — |

COMPLETE exige denominador finito y trazable, regla de enumeración, fuentes válidas, excepciones resueltas/justificadas y revisión. El porcentaje no sustituye la evaluación de superficies críticas ni la cobertura transitiva.

### 12.4. Registro de evaluación independiente (EVALUATOR_ASSESSMENT)

| evaluator_record_id | object_type (NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT/COVERAGE_SCOPE) | target_node_record_id (FK nullable) | target_edge_record_id (FK nullable) | target_route_record_id (FK nullable) | target_predicate_record_id (FK nullable) | target_snapshot_record_id (FK nullable) | target_coverage_scope_id (FK nullable) | evaluator_id | role (E1/E2) | observed_state | rule_version | scope_id | blinded_to_outcome_value | blinded_to_Z_B | confidence_or_limitations | rationale | timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|—|—|—|—|—|—|—|—|—|—|—|—|—|—|—|—|—|—|

E1 y E2 deben emitir registros independientes antes de conocer la clasificación del otro. Las variables de cegamiento aceptan YES/NO/NOT_FEASIBLE con justificación; no se presupone cegamiento logrado por declarar un procedimiento.

### 12.5. Registro de discrepancia y adjudicación (ADJUDICATION_REGISTER)

| adjudication_id | object_type (NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT/COVERAGE_SCOPE) | target_node_record_id (FK nullable) | target_edge_record_id (FK nullable) | target_route_record_id (FK nullable) | target_predicate_record_id (FK nullable) | target_snapshot_record_id (FK nullable) | target_coverage_scope_id (FK nullable) | evaluator_record_E1 (FK) | evaluator_record_E2 (FK) | disagreement_type | adjudicator_id | decision (1/0/?/NA) | rule_and_reason | minority_position | unresolved_limitations | timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|—|—|—|—|—|—|—|—|—|—|—|—|—|—|—|—|—|

No se permite majority-vote automático. Si no se resuelve el conflicto con evidencia y regla aplicable, decisión final ?.

### 12.6. Registro de truth restringida del DGP (DGP_TRUTH_SECURE)

**No forma parte de este inventario ni del paquete accesible al analizador.** Se mantiene en el entorno/artefacto segregado del generador/evaluador autorizado, con control de acceso, versionado, hash y log de accesos. Solo se permite exportar resultados de evaluación observables autorizados y cegados; nunca los valores de truth que permitan reconstruir la asignación verdadera antes del cierre analítico. La existencia de esta tabla en el esquema conceptual no autoriza crearla ni poblarla.

### 12.7. Campos comunes obligatorios y extensión de tablas

**Precedencia vigente:** para Opción A + DEC-C10-065, NODE/EDGE/ROUTE/PREDICATE y ROUTE_STEP deben incluir `snapshot_id` y `snapshot_object_record_id`; SNAPSHOT conserva `snapshot_id` como identidad semántica y `object_record_id` como revisión exacta. Las reglas detalladas y las FKs normativas vigentes están en §§15.1–15.3. La lista heredada siguiente se conserva como contrato base y no prevalece sobre esas secciones.

Todas las tablas de objetos (NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT) deben incluir:
- `object_record_id` opaco, no vacío y UNIQUE dentro de su tabla (no global); `parent_catalog_id`; `object_version` como INT positivo, secuencial desde 1 y único por identidad semántica;
- `coverage_scope_id`; `evidence_status`; `review_adjudication_status`;
- `observed_state` cuando el objeto admita clasificación trivalente;
- `evidence_ref` como cero o un `claim_evidence_id` de navegación opcional, nunca como lista serializada ni texto libre; el conjunto completo se obtiene de CLAIM_EVIDENCE_LINK;
- `unknown_reason`; `contract_intent` cuando aplique; `created_at` (record-time), `recorded_by`, `supersedes_record_id` según DEC-C10-062.

Extensiones:
- NODE: TID/SID/RID, `boundary_class`, estado declarado/instalado/desplegado/cargado/invocado/ejecutado, owner/boundary, consumers, dependencias.
- EDGE: edge_id (identidad semántica de la arista atómica en el snapshot), atomic_edge_id (identidad estable de la relación origen-destino), parent_edge_id (E01–E23), source_node_id, target_node_id, dirección, tipo, condición, directo/transitivo, versión/tiempo, necesidad para ruta.
- ROUTE: parent_route_class (una de cinco clases U_G) y route_subtype separado; secuencia ordenada y predicados necesarios.
- PREDICATE: predicate_id exacto, familia, ruta/paso/tiempo, observed_state, regla y tolerancia; nunca DGP truth.
- SNAPSHOT: snapshot_id, `unit_id`, `unit_object_record_id` (FK compuesta al nodo raíz de servicio), phase, scope_id, timestamp, artefactos/hash, método, cobertura y evidence refs.

### 12.8. Reglas de consistencia entre tablas

1. Si `evidence_ref` está poblado, debe resolver a `CLAIM_EVIDENCE_LINK.claim_evidence_id` y de ahí a `EVIDENCE_REGISTER.evidence_id`; no se aceptan referencias huérfanas. La existencia de `evidence_ref` no es obligatoria: la relación canónica completa es CLAIM_EVIDENCE_LINK. Conforme a la regla aceptada UG-SR-A01, observed_state 1/0 exige al menos un vínculo válido; observed_state ? admite ausencia de vínculo solo con unknown_reason, evidence_status=MISSING y limitaciones de búsqueda/cobertura documentadas; NA exige justificación.
2. Cada claim-evidence link debe tener alcance compatible con la unidad, versión, entorno y tiempo de la afirmación.
3. observed_state no se copia desde evidence_status; evidence_status no se deriva de observed_state.
4. coverage_scope_id debe resolver a una fila COVERAGE_REGISTER; no se puede declarar COMPLETE sin denominador.
5. En CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER exactamente una de las seis FK tipadas debe estar poblada y debe coincidir con el enum claim_target_type/object_type.
6. Cada FK tipada a NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT apunta a object_record_id UNIQUE dentro de su tabla; la FK a cobertura apunta a COVERAGE_REGISTER.coverage_scope_id PK/UNIQUE.
7. La exclusividad se expresa como CHECK de suma de indicadores de no-nulo igual a 1; un CHECK adicional vincula el único campo no nulo con el enum correspondiente (NODE↔target_node_record_id, EDGE↔target_edge_record_id, ROUTE↔target_route_record_id, PREDICATE↔target_predicate_record_id, SNAPSHOT↔target_snapshot_record_id, COVERAGE_SCOPE↔target_coverage_scope_id).
8. E1/E2 se almacenan por separado; ADJUDICATION_REGISTER solo se crea cuando proceda. Los vínculos de evidencia revisados por cada rol se filtran mediante evaluator_record_id/adjudication_id en CLAIM_EVIDENCE_LINK.
9. parent_route_class no puede sustituirse por route_subtype.
10. DGP_TRUTH_SECURE no se mezcla ni sincroniza con los registros visibles al analizador.
11. Las revisiones generan nuevos registros versionados; no se sobrescribe el historial.
12. `SNAPSHOT` fija su revisión mediante `(snapshot_id, object_record_id)`; su referencia al nodo raíz usa `(snapshot_id, object_record_id, unit_object_record_id, unit_id) → NODE(snapshot_id, snapshot_object_record_id, object_record_id, node_id)`. El NODE destino debe tener `semantic_role=LOGICAL_SERVICE_UNIT`. Además, cada NODE/EDGE/ROUTE/PREDICATE/ROUTE_STEP fija la revisión SNAPSHOT exacta mediante `(snapshot_id, snapshot_object_record_id) → SNAPSHOT(snapshot_id, object_record_id)`. Todas las referencias interobjeto dentro del snapshot deben compartir exactamente ese par. Esta regla sustituye cualquier formulación previa basada solo en `snapshot_id` o `unit_id`.
13. `NODE.boundary_class` admite `P0_CONFIG`, `P1_ENVIRONMENT`, `DUAL_P0_P1` y `NA`. Los tres primeros son clases sustantivas; `NA` es solo no aplicabilidad justificada para nodos fuera de los objetos/artefactos P0/P1. No usar null/ausencia como sustituto de NA. El campo no codifica P2.


### 12.9. Diccionario de tipos, dominios e integridad

| Familia | Tipo/formato candidato | Dominio/regla |
|---|---|---|
| Identificadores | String UTF-8, estable, no vacío | Unicidad por tabla; no reutilizar IDs; referencias a IDs existentes |
| Estados estructurales | Enum | `observed_state ∈ {1,0,?,NA}`; NA solo cuando la dimensión no aplique |
| Estado de evidencia | Enum | `evidence_status ∈ {AVAILABLE,MISSING,CONFLICTING}` |
| Cobertura | Enum | `coverage_status ∈ {NONE,PARTIAL,COMPLETE}`; COMPLETE exige denominador y regla |
| Revisión | Enum | `review_adjudication_status ∈ {NOT_REVIEWED,INDEPENDENT_PENDING,AGREED,ADJUDICATION_PENDING,ADJUDICATED,UNRESOLVED,NOT_APPLICABLE}` |
| Tiempos | ISO 8601 con offset explícito | No aceptar fecha/hora sin zona; intervalos con inicio ≤ fin |
| Hashes | Algoritmo + digest | Registrar algoritmo (p. ej. SHA-256) junto al digest; no asumir algoritmo por longitud |
| Conteos | Entero no negativo | Denominador > 0 para COMPLETE; cubiertos ≤ denominador |
| Cegamiento | Enum | YES/NO/NOT_FEASIBLE, con justificación para NO/NOT_FEASIBLE |
| Referencias | FK tipada | No aceptar referencia huérfana ni alcance incompatible |

**Normalización de evidencia:** `CLAIM_EVIDENCE_LINK` es la relación uno-a-muchos canónica entre objetos/afirmaciones y evidencias. Los campos `evidence_ref` de las tablas de objeto son referencias de navegación opcionales (cero o un vínculo primario); no sustituyen el conjunto completo de vínculos. Cada vínculo adicional se registra como fila independiente. `claim_target_type` selecciona exactamente una FK tipada (`target_*`) a NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT o COVERAGE_REGISTER; `evidence_id` apunta a EVIDENCE_REGISTER. La exclusividad y correspondencia tipo-destino son constraints obligatorias, no convenciones. No almacenar listas serializadas de IDs.

**Identidad de registro — DEC-C10-062:** `object_record_id` identifica una fila inmutable y es UNIQUE dentro de cada tabla de objetos; no se exige unicidad global. `node_id/edge_id/route_id/predicate_id/snapshot_id` identifican la entidad semántica. `UNIQUE(semantic_id, object_version)` identifica cada revisión dentro de su tabla. `object_version` es INT positivo, comienza en 1 y aumenta de uno en uno, sin saltos ni reutilización. `supersedes_record_id` es NULL solo en v1; desde v2 referencia el registro inmediatamente anterior de la misma tabla e identidad. La cadena es lineal, sin bifurcaciones, ciclos ni huérfanos; las filas históricas son inmutables. `created_at` es record-time, no tiempo de observación/validez. `parent_catalog_id` enlaza al catálogo U_G o a un subcatálogo versionado. SNAPSHOT conserva la FK compuesta a la versión exacta del NODE raíz conforme a DEC-C10-059.

**Cobertura:** `coverage_scope_id` es FK a COVERAGE_REGISTER. Las tablas de objeto no replican el estado de cobertura como sustituto del registro canónico; los campos heredados `coverage_status` son vistas/resúmenes y deben coincidir con el scope enlazado o marcar discrepancia.

**Evaluadores:** `evaluator_record_ids` admite varios registros, pero cada E1/E2 se conserva como fila independiente en EVALUATOR_ASSESSMENT. No almacenar dos evaluadores en una sola celda.

**Estado de revisión:** NOT_REVIEWED antes de doble evaluación; INDEPENDENT_PENDING mientras falta una de las dos; AGREED si E1/E2 coinciden bajo la misma regla y versión; ADJUDICATION_PENDING si discrepan; ADJUDICATED tras resolución motivada; UNRESOLVED si persiste ?; NOT_APPLICABLE solo con justificación.

### 12.10. Matriz de claves, referencias y obligatoriedad por tabla

**Nota de precedencia (Opción A + DEC-C10-065):** la matriz que sigue conserva el baseline histórico del esquema y ya no es la fuente normativa de las claves/FKs de snapshot. Para NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT/ROUTE_STEP, la matriz física vigente es §15.2 y sus reglas complementarias §§15.1, 15.3 y 16. En caso de discrepancia prevalecen esas secciones. Los demás registros y reglas tipadas de evidencia/evaluación conservan las disposiciones de §§12.7–12.9 y 15.4.

La matriz cubre los diez registros operativos normalizados preexistentes más ROUTE_STEP, relación operativa de secuencia aprobada por DEC-C10-064. `DGP_TRUTH_SECURE` queda fuera de este inventario y del paquete accesible al analizador (§12.6). Las claves primarias compuestas históricas se conservan como definición lógica; las claves candidatas UNIQUE adicionales se declaran explícitamente cuando son necesarias para FKs tipadas.

| Tabla | PK lógica | Claves candidatas / unicidad | Referencias obligatorias y cardinalidad | Estado / campos de control |
|---|---|---|---|---|
| NODE | (object_record_id, node_id) | UNIQUE(object_record_id); UNIQUE(node_id, object_version) | coverage_scope_id → COVERAGE_REGISTER; supersedes_record_id autorreferente según DEC-C10-062; claim-evidence 0..n; evidence_ref 0..1 | semantic_role enum obligatorio; boundary_class obligatorio; observed_state según aplicabilidad |
| EDGE | (object_record_id, edge_id) | UNIQUE(object_record_id); UNIQUE(edge_id, object_version) | coverage_scope_id; supersedes_record_id autorreferente; claim-evidence 0..n; evidence_ref 0..1; extremos source_node_id/target_node_id resuelven a NODE conforme a identidad/versionado | observed_state 1/0/?/NA justificado; parent_edge_id y atomic_edge_id según crosswalk |
| ROUTE | (object_record_id, route_id) | UNIQUE(object_record_id); UNIQUE(route_id, object_version) | coverage_scope_id; supersedes_record_id autorreferente; claim-evidence 0..n; evidence_ref 0..1; secuencia refiere a nodos/aristas existentes | parent_route_class y route_subtype separados; observed_state según aplicabilidad |
| PREDICATE | (object_record_id, predicate_id) | UNIQUE(object_record_id); UNIQUE(predicate_id, object_version) | coverage_scope_id; supersedes_record_id autorreferente; claim-evidence 0..n; evidence_ref 0..1; route_id resuelve a ROUTE | observed_state 1/0/?; regla/tolerancia y unknown_reason cuando proceda |
| SNAPSHOT | (object_record_id, snapshot_id) | UNIQUE(object_record_id); UNIQUE(snapshot_id, object_version) | coverage_scope_id; supersedes_record_id autorreferente; FK compuesta (unit_object_record_id, unit_id) → NODE(object_record_id, node_id); claim-evidence 0..n; evidence_ref 0..1 | phase y timestamp obligatorios; nodo raíz con semantic_role=LOGICAL_SERVICE_UNIT |
| ROUTE_STEP | route_step_id (o PK compuesta route_record_id, step_index) | UNIQUE(route_record_id, step_index) | route_record_id → ROUTE; FK compuestas (snapshot_id, node_record_id) → NODE y (snapshot_id, edge_record_id) → EDGE, exactamente una por fila | step_index positivo, único y contiguo; step_type coherente; continuidad NODE/EDGE cross-row validada |
| EVIDENCE_REGISTER | evidence_id | UNIQUE(evidence_id) | scope_id conforme al contrato de procedencia; 1..n CLAIM_EVIDENCE_LINK cuando la evidencia respalda afirmaciones | source_provenance y evidence_status; custodia, integridad, alcance y límites |
| CLAIM_EVIDENCE_LINK | claim_evidence_id | UNIQUE(claim_evidence_id) | exactamente una FK destino tipada: NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT/COVERAGE_SCOPE; evidence_id → EVIDENCE_REGISTER obligatorio; evaluator_record_id y adjudication_id opcionales | claim_target_type coherente con la única FK poblada; una fila por vínculo; relación 0..n desde cada destino |
| COVERAGE_REGISTER | coverage_scope_id | UNIQUE(coverage_scope_id) | destino tipado opcional de CLAIM_EVIDENCE_LINK; referenciado por coverage_scope_id desde tablas de objeto | universo/versionado y denominador; COMPLETE solo con regla y cobertura suficiente |
| EVALUATOR_ASSESSMENT | evaluator_record_id | UNIQUE(evaluator_record_id) | exactamente una FK destino tipada a NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT/COVERAGE_SCOPE | evaluator_id y rol E1/E2; registros separados; cegamiento y regla versionada |
| ADJUDICATION_REGISTER | adjudication_id | UNIQUE(adjudication_id) | exactamente una FK destino tipada; evaluator_record_E1 y evaluator_record_E2 → EVALUATOR_ASSESSMENT obligatorias | decisión 1/0/?/NA motivada; conservar posición minoritaria y limitaciones |

Reglas transversales:

1. En NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT, `object_record_id` es UNIQUE por tabla y `UNIQUE(semantic_id, object_version)` evita dos revisiones con la misma versión. Se conserva la PK lógica compuesta declarada; la unicidad individual de object_record_id es una clave candidata adicional requerida por las FKs tipadas.
2. En las mismas cinco tablas, `object_version` es INT positivo, comienza en 1 y es contiguo por identidad semántica. `supersedes_record_id` es NULL en v1 y referencia al predecesor inmediato de la misma tabla/identidad desde v2. Cada fila admite como máximo un sucesor; no se permiten ciclos, bifurcaciones ni huérfanos. El historial es inmutable.
3. Cada fila CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER debe poblar exactamente una de sus seis FKs destino tipadas, coherente con su enum. Las FKs opcionales de evaluación/adjudicación en CLAIM_EVIDENCE_LINK no sustituyen las relaciones E1/E2.
4. `DGP_TRUTH_SECURE` no es una undécima tabla del inventario operativo ni se añade a la matriz: permanece segregada y fuera del acceso del analizador.
5. Las cardinalidades descritas son contratos documentales. La implementación de PK/UNIQUE/FK/CHECK, secuencias, triggers, permisos de inmutabilidad y restricciones compuestas requiere gate técnico autorizado y pruebas negativas.

La FK SNAPSHOT→NODE conserva exactamente la pareja `(unit_object_record_id, unit_id)` hacia `(object_record_id, node_id)`; no se resuelve por `unit_id` aislado ni por “última versión”.

### 12.11. Regla aceptada de reconciliación UG-SR-A01

Se adopta la distinción entre obligatoriedad de soporte probatorio y referencia de navegación:

- `evidence_ref` permanece opcional (0..1) y, si se usa, debe resolver a un vínculo existente. No es el repositorio de evidencias.
- `CLAIM_EVIDENCE_LINK` sigue siendo la relación canónica 0..n.
- Una instancia con `observed_state=1` o `0` requiere al menos un vínculo válido CLAIM_EVIDENCE_LINK con alcance compatible. Para 0 se mantiene además la carga de cobertura negativa suficiente.
- Una instancia con `observed_state=?` puede carecer de vínculo solo si registra `unknown_reason`, `evidence_status=MISSING` y límites de búsqueda/cobertura; si hay evidencia relevante de incertidumbre, se vincula.
- `NA` requiere justificación de no aplicabilidad; no exige vínculo de evidencia por defecto.

**Aceptación documental:** la regla queda aceptada en el diseño documental C10-S por decisión explícita del usuario (2026-11-05). No queda congelada ni validada técnicamente. Requiere posterior validación de cardinalidad/FK con instancias y motor.


### 14.1. Reconciliación física EDGE — UG-SCH-01

El encabezado EDGE se alinea con el contrato normalizado y el catálogo E01–E23:
- `edge_id`: identidad semántica de la arista atómica dentro del registro/grafo versionado.
- `atomic_edge_id`: identificador estable de la relación origen-destino atómica.
- `parent_edge_id`: uno de los IDs de catálogo E01–E23; conserva trazabilidad al contrato padre.
- `source_node_id` y `target_node_id`: referencias explícitas a NODE; sustituyen los nombres ambiguos `source_node`/`target_node`.

Para una relación padre con varios destinos se registra una fila por par origen-destino, con el mismo `parent_edge_id` y distinto `atomic_edge_id`. La clave local EDGE sigue siendo `(object_record_id, edge_id)`; `atomic_edge_id` requiere unicidad dentro del `coverage_scope_id` y versión de grafo correspondiente. No se crean filas observadas ni IDs atómicos nuevos en esta actualización.

E07 permanece fuera de EDGE porque es una regla lógica/conjuntiva. E22 conserva sus destinos como eventos/variables no identificados: no se inventan nodos para selección o ejecución. Las 39 filas descritas en el catálogo siguen siendo candidatas, no relaciones observadas.


### 14.2. Reconciliación de referencias tipadas y procedencia — DEC-C10-061

Se aplica el contrato aceptado:
- CLAIM_EVIDENCE_LINK: seis FK tipadas; exactamente una no nula y coherente con claim_target_type.
- EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER: mismo patrón con object_type.
- NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT: object_record_id UNIQUE dentro de cada tabla como clave candidata para las FKs; se preservan sus claves semánticas y versionadas.
- COVERAGE_REGISTER.coverage_scope_id: PK/UNIQUE.
- source_provenance: canónica en EVIDENCE_REGISTER; retirada de la lista de campos comunes de las tablas de objetos.
- evidence_ref: opcional 0..1 de navegación; CLAIM_EVIDENCE_LINK mantiene 0..n.

Las constraints CHECK/FK, la compatibilidad del motor/formato y las pruebas negativas no se han ejecutado. La decisión es documental, no freeze ni validación técnica.


### 12.12. Identidad de registro, versionado y supersession — DEC-C10-062

Esta sección complementa y prevalece sobre cualquier formulación genérica anterior de `object_version` o `supersedes_record_id`.

- Ámbito: solo NODE, EDGE, ROUTE, PREDICATE y SNAPSHOT.
- `object_record_id`: identificador opaco, no vacío y UNIQUE dentro de cada tabla; no se exige unicidad global entre tablas.
- ID semántico: identifica la entidad dentro de su tabla. `UNIQUE(semantic_id, object_version)` identifica cada revisión.
- `object_version`: INT positivo; comienza en 1 y aumenta de uno en uno. Sin duplicados, saltos, decrementos ni reutilización.
- `supersedes_record_id`: NULL solo en v1; desde v2 referencia la fila inmediatamente anterior de la misma tabla e identidad semántica, con versión actual menos uno.
- Cadena lineal: cada registro admite como máximo un sucesor; sin autorreferencias, referencias futuras, bifurcaciones, ciclos, huérfanos ni múltiples raíces/extremos vigentes.
- Historial inmutable: correcciones crean nuevas filas. Supersession no significa equivalencia funcional, causal ni de valor.
- Cambio semántico material, split/merge, derivación, alternativa o nueva captura SNAPSHOT requiere identidad/relación propia; continuidad incierta permanece `MATCH_UNRESOLVED / ?`.
- `created_at` es record-time, no tiempo de observación/validez. SNAPSHOT conserva la FK compuesta a la versión exacta del NODE raíz; nunca se resuelve a la última versión implícitamente.

**Estado:** ACCEPTED DOCUMENTALLY por DEC-C10-062. Constraints, FK autorreferentes, secuencias, triggers, inmutabilidad y detección de ciclos quedan pendientes del gate técnico autorizado; no hay validación física.


## 13. Aplicación normativa — DEC-C10-064 / Opción A (2026-11-05)

Esta sección complementa y prevalece sobre los encabezados incompatibles de §§2–6 y sobre formulaciones previas de pertenencia/referencias. No crea instancias ni altera la semántica de los catálogos.

### 13.1. NODE

Añadir `snapshot_id` y `snapshot_object_record_id` obligatorios a cada registro NODE. La FK compuesta `(snapshot_id, snapshot_object_record_id) → SNAPSHOT(snapshot_id, object_record_id)` fija la revisión exacta del snapshot. Mantener `node_id` como identidad semántica y `object_record_id` como identidad inmutable de fila. Claves candidatas necesarias, conforme a §15.2: UNIQUE(`snapshot_id, snapshot_object_record_id, object_record_id`), UNIQUE(`snapshot_id, snapshot_object_record_id, node_id`) y UNIQUE(`snapshot_id, snapshot_object_record_id, object_record_id, node_id`). La clave semántica por snapshot debe incluir `snapshot_object_record_id`; `UNIQUE(snapshot_id,node_id)` sería incorrecta porque impediría conservar la misma identidad NODE en distintas revisiones del mismo snapshot semántico.

### 13.2. EDGE

Añadir `snapshot_id`, `snapshot_object_record_id`, `source_node_record_id` y `target_node_record_id`, todos obligatorios en filas EDGE observadas. La pertenencia de EDGE fija la revisión exacta de SNAPSHOT mediante FK compuesta. Mantener `source_node_id`/`target_node_id` como IDs semánticos/crosswalk. Las FKs de origen y destino incluyen `(snapshot_id, snapshot_object_record_id, node_record_id, node_id)` y resuelven a `(snapshot_id, snapshot_object_record_id, object_record_id, node_id)` en NODE. No se admiten aristas con extremos de otro snapshot/revisión ni resolución por identidad semántica aislada/última versión.

### 13.3. ROUTE y PREDICATE

ROUTE añade `snapshot_id` y `snapshot_object_record_id` obligatorios, con FK compuesta a la revisión exacta de SNAPSHOT. PREDICATE añade ambos campos y `route_record_id`; su FK compuesta `(snapshot_id, snapshot_object_record_id, route_record_id, route_id)` debe resolver a `(snapshot_id, snapshot_object_record_id, object_record_id, route_id)` en ROUTE. `route_id` aislado no identifica la versión evaluada.

### 13.4. SNAPSHOT y nodo raíz

SNAPSHOT conserva `snapshot_id` como identidad semántica, `object_record_id` como revisión exacta, y `unit_id` + `unit_object_record_id` para identificar la unidad raíz. La FK raíz es `(snapshot_id, object_record_id, unit_object_record_id, unit_id) → NODE(snapshot_id, snapshot_object_record_id, object_record_id, node_id)`. El NODE destino debe tener `semantic_role=LOGICAL_SERVICE_UNIT`. Se mantiene la unicidad de la raíz para unidad/snapshot/scope. La circularidad SNAPSHOT↔NODE se valida al COMMIT mediante constraints diferibles y transacción atómica. Si el motor elegido no soporta FKs diferibles o garantía equivalente demostrada, el gate físico queda BLOCKED; no se debilitan FKs ni se confirma un estado huérfano.

### 13.5. ROUTE_STEP — relación operativa normalizada

Añadir ROUTE_STEP como relación de secuencia con campos mínimos: `route_step_id` (o PK compuesta `route_record_id, step_index`), `snapshot_id`, `snapshot_object_record_id`, `route_record_id`, `step_index`, `step_type` (NODE/EDGE), `node_record_id` nullable y `edge_record_id` nullable. `snapshot_object_record_id` fija la revisión exacta de SNAPSHOT y debe coincidir con la revisión fijada por ROUTE, NODE y EDGE. Cada paso debe referenciar exactamente uno de NODE/EDGE, coherente con step_type. Todas las FKs a SNAPSHOT y a ROUTE/NODE/EDGE incluyen `snapshot_id` y `snapshot_object_record_id`, con el mismo par exacto en origen y destino. Los índices empiezan en 1, son únicos y contiguos por ruta. La continuidad entre nodos y aristas adyacentes es una invariante cross-row que requiere constraint/trigger verificable o validador independiente y pruebas negativas. La secuencia serializada de ROUTE deja de ser fuente canónica; puede sobrevivir solo como vista/export derivado.

### 13.6. Interpretación y diff

`object_version` es la revisión observacional secuencial por identidad semántica. Nueva captura en otro snapshot genera nueva fila/version aunque los atributos sean idénticos. Por ello:
- cambio de record ID/version/snapshot no implica cambio material;
- cambios estructurales se determinan comparando propiedades constitutivas y relaciones entre snapshots comparables;
- cambios de evidencia/cobertura se registran separadamente como ΔE_T;
- ΔT_acc* se deriva mediante su contrato independiente, outcome-blind y con universo/frontera/granularidad/mapping fijados;
- no se comparan IDs opacos, record IDs, timestamps ni object_version como diferencias sustantivas.

### 13.7. Estado

DEC-C10-064 aprueba esta resolución de detalle. La aplicación documental de encabezados queda registrada aquí; la plantilla sigue siendo Draft y vacía de observaciones. No equivale a freeze, validación física, parser, fixtures ni autorización de experimento. El motor relacional aún no está fijado; compatibilidad con FKs diferibles, constraints compuestas, ROUTE_STEP cross-row, secuencia/supersession e inmutabilidad son gates técnicos pendientes. `scientific_execution=false`; `execution_authorized=false`.


## 14. Reconciliación de matriz de claves y campos comunes — DEC-C10-064

ROUTE_STEP se incorpora a la matriz de claves de §12.10 como relación normalizada adicional. No se cuenta como una de las cinco tablas de objetos versionados (NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT) ni recibe object_version/supersedes_record_id: sus filas pertenecen a una revisión exacta de ROUTE y quedan identificadas por route_record_id + step_index. Una modificación de secuencia se registra en la revisión de ROUTE correspondiente y en sus ROUTE_STEP asociados; no se reescribe el historial de una ruta publicada.

Los campos comunes de §12.7 se mantienen para las cinco tablas de objetos versionados. Bajo Opción A + DEC-C10-065, NODE/EDGE/ROUTE/PREDICATE y ROUTE_STEP incorporan obligatoriamente `snapshot_id` + `snapshot_object_record_id`; SNAPSHOT conserva `snapshot_id` como identidad semántica y `object_record_id` como revisión exacta. EDGE añade source_node_record_id/target_node_record_id; PREDICATE añade route_record_id. ROUTE_STEP usa el mismo par de pinning y route_record_id para fijar la secuencia a la revisión exacta de SNAPSHOT y de ROUTE.

ROUTE_STEP no sustituye CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER, EVALUATOR_ASSESSMENT ni ADJUDICATION_REGISTER. Si en una fase posterior se requiere evidencia directa por paso, deberá definirse una extensión tipada explícita; no se amplía implícitamente el enum de destinos actual.

**Control pendiente:** la matriz y los encabezados deberán revisarse conjuntamente contra DDL/serialización del motor seleccionado. La continuidad cross-row no queda garantizada por la fila ROUTE_STEP aislada.


## 15. Contrato normalizado reconciliado — Opción A / DEC-C10-064 (addendum normativo)

Este apartado sustituye las formulaciones incompatibles de §§12.7–12.10 en lo relativo a snapshot membership, referencias interobjeto y secuencia de rutas. Los campos y relaciones no afectados por Opción A conservan sus reglas previas. La sustitución incorpora la decisión DEC-C10-065: los cinco registros dependientes fijan la revisión exacta de SNAPSHOT mediante snapshot_object_record_id y FK compuesta. La validación física y compatibilidad de motor siguen pendientes.

### 15.1. Cinco tablas versionadas

NODE, EDGE, ROUTE, PREDICATE y SNAPSHOT conservan `object_record_id` opaco y UNIQUE por tabla, identidad semántica separada y `object_version` positivo, secuencial por identidad semántica, con `supersedes_record_id` al predecesor inmediato. Una nueva observación en snapshot nuevo crea nuevo registro/version aunque no haya cambio material.

NODE, EDGE, ROUTE, PREDICATE y ROUTE_STEP incorporan `snapshot_id` y `snapshot_object_record_id` obligatorios. El primero identifica el snapshot semántico; el segundo fija la fila versionada exacta de SNAPSHOT. SNAPSHOT conserva `snapshot_id` como identidad semántica y `object_record_id` como identidad de fila versionada. La FK compuesta evita resolver por última versión o timestamp.

### 15.2. Claves candidatas y referencias interobjeto aprobadas

- NODE: UNIQUE(`object_record_id`); UNIQUE(`node_id, object_version`); UNIQUE(`snapshot_id, object_record_id`); UNIQUE(`snapshot_id, snapshot_object_record_id, object_record_id`); UNIQUE(`snapshot_id, snapshot_object_record_id, node_id`); UNIQUE(`snapshot_id, snapshot_object_record_id, object_record_id, node_id`).
- EDGE: UNIQUE(`object_record_id`); UNIQUE(`edge_id, object_version`); UNIQUE(`snapshot_id, object_record_id`); UNIQUE(`snapshot_id, snapshot_object_record_id, object_record_id`); UNIQUE(`snapshot_id, snapshot_object_record_id, edge_id`); UNIQUE(`snapshot_id, snapshot_object_record_id, object_record_id, edge_id`).
- ROUTE: UNIQUE(`object_record_id`); UNIQUE(`route_id, object_version`); UNIQUE(`snapshot_id, object_record_id`); UNIQUE(`snapshot_id, snapshot_object_record_id, object_record_id`); UNIQUE(`snapshot_id, snapshot_object_record_id, route_id`); UNIQUE(`snapshot_id, snapshot_object_record_id, object_record_id, route_id`).
- PREDICATE: UNIQUE(`object_record_id`); UNIQUE(`predicate_id, object_version`); UNIQUE(`snapshot_id, object_record_id`); UNIQUE(`snapshot_id, snapshot_object_record_id, object_record_id`); UNIQUE(`snapshot_id, snapshot_object_record_id, predicate_id`); UNIQUE(`snapshot_id, snapshot_object_record_id, object_record_id, predicate_id`).
- SNAPSHOT: UNIQUE(`object_record_id`); UNIQUE(`snapshot_id, object_version`); UNIQUE(`snapshot_id, object_record_id`).
- Para NODE/EDGE/ROUTE/PREDICATE/ROUTE_STEP: FK compuesta (`snapshot_id`, `snapshot_object_record_id`) → SNAPSHOT(`snapshot_id`, `object_record_id`).

Las claves candidatas necesarias para las FKs compuestas de mismo snapshot quedan explicitadas así (columnas en el mismo orden en origen y destino):

- NODE: UNIQUE(snapshot_id, snapshot_object_record_id, node_id); UNIQUE(snapshot_id, snapshot_object_record_id, object_record_id); UNIQUE(snapshot_id, snapshot_object_record_id, object_record_id, node_id).
- EDGE: UNIQUE(snapshot_id, snapshot_object_record_id, edge_id); UNIQUE(snapshot_id, snapshot_object_record_id, object_record_id); UNIQUE(snapshot_id, snapshot_object_record_id, object_record_id, edge_id).
- ROUTE: UNIQUE(snapshot_id, snapshot_object_record_id, route_id); UNIQUE(snapshot_id, snapshot_object_record_id, object_record_id); UNIQUE(snapshot_id, snapshot_object_record_id, object_record_id, route_id).
- PREDICATE: UNIQUE(snapshot_id, snapshot_object_record_id, predicate_id); UNIQUE(snapshot_id, snapshot_object_record_id, object_record_id); UNIQUE(snapshot_id, snapshot_object_record_id, object_record_id, predicate_id).
- SNAPSHOT: UNIQUE(snapshot_id, object_record_id), que ya forma la clave candidata destino del pinning exacto.
- ROUTE_STEP: PK/UNIQUE(route_record_id, step_index); UNIQUE(snapshot_id, snapshot_object_record_id, route_record_id, step_index).

FKs normativas:
- Cada NODE/EDGE/ROUTE/PREDICATE/ROUTE_STEP: (snapshot_id, snapshot_object_record_id) → SNAPSHOT(snapshot_id, object_record_id).
- EDGE origen: (snapshot_id, snapshot_object_record_id, source_node_record_id, source_node_id) → NODE(snapshot_id, snapshot_object_record_id, object_record_id, node_id).
- EDGE destino: (snapshot_id, snapshot_object_record_id, target_node_record_id, target_node_id) → NODE(snapshot_id, snapshot_object_record_id, object_record_id, node_id).
- PREDICATE→ROUTE: (snapshot_id, snapshot_object_record_id, route_record_id, route_id) → ROUTE(snapshot_id, snapshot_object_record_id, object_record_id, route_id).
- ROUTE_STEP→ROUTE: (snapshot_id, snapshot_object_record_id, route_record_id) → ROUTE(snapshot_id, snapshot_object_record_id, object_record_id).
- ROUTE_STEP→NODE: (snapshot_id, snapshot_object_record_id, node_record_id) → NODE(snapshot_id, snapshot_object_record_id, object_record_id).
- ROUTE_STEP→EDGE: (snapshot_id, snapshot_object_record_id, edge_record_id) → EDGE(snapshot_id, snapshot_object_record_id, object_record_id).
- SNAPSHOT→NODE raíz: (snapshot_id, object_record_id, unit_object_record_id, unit_id) → NODE(snapshot_id, snapshot_object_record_id, object_record_id, node_id). En este caso, el object_record_id de la fila SNAPSHOT ocupa el papel snapshot_object_record_id de NODE y fija el registro SNAPSHOT que contiene la referencia raíz.

Todas las referencias interobjeto comparten exactamente el mismo par (snapshot_id, snapshot_object_record_id). Las claves semánticas node_id/edge_id/route_id/predicate_id son comprobaciones adicionales de identidad y no sustituyen a los record IDs. Las FKs circulares SNAPSHOT↔NODE raíz deberán ser diferibles hasta COMMIT o equivalentes transaccionales, y se probarán sin relajar integridad.

### 15.3. ROUTE y ROUTE_STEP

`ordered_node_edge_sequence` deja de ser columna persistida de ROUTE. ROUTE_STEP es la única fuente canónica del orden y usa: route_step_id, snapshot_id, snapshot_object_record_id, route_record_id, step_index, step_type, node_record_id nullable y edge_record_id nullable.

- FK de snapshot: `(snapshot_id, snapshot_object_record_id)` → SNAPSHOT(`snapshot_id`, `object_record_id`).
- FK de ruta: `(snapshot_id, snapshot_object_record_id, route_record_id)` → ROUTE(`snapshot_id, snapshot_object_record_id, object_record_id`).
- FK de nodo: `(snapshot_id, snapshot_object_record_id, node_record_id)` → NODE(`snapshot_id, snapshot_object_record_id, object_record_id`).
- FK de arista: `(snapshot_id, snapshot_object_record_id, edge_record_id)` → EDGE(`snapshot_id, snapshot_object_record_id, object_record_id`).
- CHECK: exactamente uno de node_record_id/edge_record_id no nulo y coherente con step_type.
- UNIQUE(route_record_id, step_index); step_index entero positivo y contiguo desde 1.
- La continuidad entre extremos exactos de EDGE y NODE adyacentes es una invariante cross-row que requiere constraint/trigger verificable o validador independiente y pruebas negativas.

Todas las FKs de pertenencia fijan la misma revisión exacta de SNAPSHOT. EDGE, PREDICATE y ROUTE_STEP deben satisfacer además que los registros relacionados comparten el mismo par (snapshot_id, snapshot_object_record_id). Las FKs de ROUTE_STEP a ROUTE/NODE/EDGE incluyen obligatoriamente ambos componentes del pinning; una FK que omita `snapshot_object_record_id` no satisface DEC-C10-065.

### 15.4. Referencias tipadas de evidencia y evaluación — DEC-C10-061

Estas relaciones son independientes de las FKs interobjeto de Opción A y conservan los seis destinos tipados aprobados. Las columnas y constraints documentales son:

**CLAIM_EVIDENCE_LINK**
- PK/UNIQUE: `claim_evidence_id`.
- `claim_target_type` enum cerrado: NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT, COVERAGE_SCOPE.
- Seis columnas nullable: `target_node_record_id`, `target_edge_record_id`, `target_route_record_id`, `target_predicate_record_id`, `target_snapshot_record_id`, `target_coverage_scope_id`; cada una FK a la clave única de su tabla destino.
- CHECK: exactamente una de las seis columnas no nula y coherente con `claim_target_type`.
- `evidence_id` NOT NULL → EVIDENCE_REGISTER(`evidence_id`).
- `evaluator_record_id` y `adjudication_id` son FKs opcionales a EVALUATOR_ASSESSMENT(`evaluator_record_id`) y ADJUDICATION_REGISTER(`adjudication_id`).
- Cardinalidad 0..n por destino: múltiples afirmaciones/evidencias se representan mediante filas distintas, nunca listas serializadas.

**EVALUATOR_ASSESSMENT**
- PK/UNIQUE: `evaluator_record_id`.
- `object_type` usa el mismo enum de seis destinos.
- Conserva las seis columnas nullable `target_*`; exactamente una debe estar poblada y concordar con `object_type`, con FK tipada al destino correspondiente.
- `role` distingue E1/E2. Una fila representa una evaluación de un evaluador; no se serializan evaluadores múltiples.

**ADJUDICATION_REGISTER**
- PK/UNIQUE: `adjudication_id`.
- `object_type` y las seis columnas nullable `target_*` siguen la misma regla de destino exclusivo y FK tipada.
- `evaluator_record_E1` y `evaluator_record_E2` son FKs obligatorias a EVALUATOR_ASSESSMENT(`evaluator_record_id`); la posición minoritaria y el razonamiento quedan preservados.

**EVIDENCE_REGISTER y COVERAGE_REGISTER**
- `evidence_id` es PK/UNIQUE; `source_provenance` y sus campos complementarios de origen/custodia/integridad/completitud son canónicos aquí, no duplicados en NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT.
- `coverage_scope_id` es PK/UNIQUE en COVERAGE_REGISTER; el destino COVERAGE_SCOPE de las tres tablas relacionales referencia esa clave.

**Reglas de evidencia**
- `evidence_ref` en registros de objeto es navegación opcional 0..1 hacia `claim_evidence_id`, no el soporte probatorio completo.
- Todo registro observado real con `observed_state=1` o `0` requiere al menos un CLAIM_EVIDENCE_LINK válido y de alcance compatible; un 0 requiere además cobertura negativa suficiente.
- Un `?` sin vínculo exige `unknown_reason`, `evidence_status=MISSING` y límites de búsqueda/cobertura; NA exige justificación.
- La segregación de DGP_TRUTH_SECURE respecto del analizador es una condición de arquitectura/custodia, no una FK ni una etiqueta que por sí sola pruebe seguridad.

La matriz precedente expresa el contrato documental aceptado por DEC-C10-061 y UG-SR-A01. CHECK, FK, cardinalidades, dominios, protección de truth y consultas de reconstrucción no están implementados ni validados físicamente.

### 15.5. Estado y gate

La matriz anterior §12.10 se considera reemplazada por este addendum solo para los elementos aquí enumerados; debe convertirse en una matriz física única y verificarse contra DDL tras seleccionar motor. No se declara schema freeze ni integridad física. Motor no seleccionado; soporte de FKs diferibles, restricciones cross-row, inmutabilidad y parser pendientes. `scientific_execution=false`; `execution_authorized=false`.


## 16. DEC-C10-065 — pinning exacto de revisión SNAPSHOT (aprobado)

DEC-C10-065 aprueba añadir `snapshot_object_record_id` obligatorio a NODE, EDGE, ROUTE, PREDICATE y ROUTE_STEP. En cada caso, junto con `snapshot_id`, forma la FK compuesta hacia SNAPSHOT(`snapshot_id`, `object_record_id`). La columna snapshot_id sola no se considera referencia suficiente a una fila versionada.

La referencia exacta debe propagarse también a las referencias entre objetos: EDGE.source/target NODE, PREDICATE→ROUTE, ROUTE_STEP→ROUTE/NODE/EDGE y SNAPSHOT→NODE raíz deben compartir el mismo snapshot_id y snapshot_object_record_id del registro SNAPSHOT fijado. El nodo raíz del snapshot mantiene su referencia exacta mediante unit_object_record_id; la circularidad NODE↔SNAPSHOT se resolverá con FK diferibles o mecanismo transaccional equivalente, sujeto a prueba del motor.

No se alteran las identidades semánticas, object_record_id, object_version ni supersedes_record_id. No se permite latest-version lookup, timestamp inference ni fallback. Esta decisión cierra el requisito documental de OAS-02, pero no acredita integridad física, schema freeze, parser, DDL ni compatibilidad de motor. UG-SCH-10 permanece OPEN hasta reconciliación completa y revisión independiente.


### 15.6. Integridad de revisión exacta — matriz de claves y FKs

La matriz precedente constituye la especificación documental de orden de columnas para Opción A + DEC-C10-065. La compatibilidad de cada clave candidata con las restricciones físicas del motor seleccionado sigue pendiente. No se permite asumir que la presencia de una UNIQUE textual en este documento equivale a constraint implementado.


---

## 17. Aplicación del crosswalk de provisión B-M01…15 al registro U_G (D2, 2026-11-06)

**Estado:** protocolo de instanciación documental DRAFT / NO APROBADO / NO CONGELADO / NO EJECUTADO. Reutiliza el crosswalk de la matriz de cobertura §9 y la matriz de cierre §31. No añade entidades observadas, no altera los catálogos U_G ni modifica las claves/columnas aprobadas en §§12–16.

### 17.1. Regla de identidad y separación de catálogos

1. B-M01…15 identifica **dominios de auditoría de la provisión**, no nodos, aristas, rutas ni predicados del sistema. No crear un NODE llamado “B-Mxx”, una EDGE por cada dominio ni un PREDICATE nuevo con ese código.
2. Los objetos materiales que se encuentren dentro de cada dominio se registran con la identidad U_G que corresponda: NODE para componentes/servicios/artefactos con identidad propia; EDGE para relaciones reales entre extremos identificados; ROUTE para secuencias funcionales candidatas; PREDICATE para condiciones tipadas por ruta/paso/tiempo; SNAPSHOT para capturas comparables.
3. En `parent_catalog_id` se conserva exclusivamente el ID del catálogo U_G definido en §10.6 (Nxx, Exx, código de predicado o clase de ruta). **No** introducir B-Mxx en ese campo. La trazabilidad del dominio de auditoría se conserva en `notes/unknowns` de NODE/EDGE/ROUTE, y en `claim_statement` + `relevance_scope` de CLAIM_EVIDENCE_LINK para cada afirmación/predicado; `dimension` identifica B-Mxx en COVERAGE_REGISTER. No se añaden columnas ni se amplía el enum de destinos.
4. Los IDs Nxx/Exx de la matriz §9 son roles y relaciones candidatas, no IDs de registros observados. La instanciación crea un registro solo después de identificar un objeto/relación real, asignarle identidad, versión, snapshot y frontera. Las relaciones mult destino se desagregan en filas EDGE atómicas conforme a §10.2. E07 sigue siendo regla lógica, no EDGE; E22 no autoriza inventar nodos destino.
5. La intención contractual de B se registra en `contract_intent`; nunca se copia como `observed_state`. La truth del DGP sigue fuera del registro visible al analizador.

### 17.2. Correspondencia de cada dominio con los registros

La tabla determina **qué buscar y dónde registrarlo si se encuentra**, no afirma que exista. Los Nxx/Exx remiten a la matriz de cobertura §9 y al catálogo §10.

| Dominio de auditoría | NODE / EDGE | ROUTE | PREDICATE | SNAPSHOT / evidencia | Dimensión de cobertura |
|---|---|---|---|---|---|
| B-M01 Artefacto/versión | NODE candidatos N04, N06; EDGE E02–E04, solo si se observan carga/dependencia reales | Rτ2 si integra una ruta material identificada | ID-τ2, DEP-τ2, REL-τ2 | Capturas/hash de paquete, manifiesto/SBOM y versiones; evidencia de procedencia | B-M01-ARTEFACTO_VERSION |
| B-M02 Runtime | NODE candidatos N05, N06, N18, N20, N21; EDGE E03, E04, E16, E19, E20, solo con relación observada | Rτ2 y rutas compartidas/externas solo si se demuestra participación | DEP-τ2, RES-τ2, ALT-DEP, EXT; Rshared/Rexternal | Configuración/runtime, aislamiento, librerías, cuotas, dependencias y consumidores pre/post | B-M02-RUNTIME |
| B-M03 Host | NODE candidatos N01, N06, N13, N15, N18, N20, N21; EDGE E16–E20, solo con dependencia/consumo comprobado | Rτ2/RA12/Rshared según relación real | ALT-A1, ALT-A2, ALT-DEP, RES-τ2, EXT; Rshared | Snapshot host/SO/paquetes y diff; consumidores y comportamiento alternativo | B-M03-HOST |
| B-M04 Interfaz | NODE candidatos N07, N17, N20, N21; EDGE E05, E06, E18–E20, solo con llamada/relación efectiva | Rτ2 si el canal forma parte de la secuencia material | REL-τ2, AUTH-τ2, DEP-τ2, EXT | API/schema/endpoint/ACL/versiones, llamadas, relaciones y trazas | B-M04-INTERFAZ |
| B-M05 Permisos | NODE candidatos N17, N07, N10, N11, N13, N15; EDGE E18, solo para autorización efectiva observada | Rτ2/RA12 para operaciones autorizadas concretas | AUTH-τ2, ALT-A1, ALT-A2, BLOCK-τ2 | Snapshot/diff de políticas y permisos; fuente normativa de C_auth separada de ACL técnica | B-M05-PERMISOS |
| B-M06 Datos | NODE candidatos N19, N10, N11, N12, N13, N15, N16; EDGE E10, E14, E15, E21, E23, solo para flujo/lectura/escritura/evaluación observados | Rτ2/RA12 para rutas que consuman los datos | COND-τ2, APP-τ2, ALT-F*, ORACLE | Snapshots fuente/destino, hashes, linaje, reglas y versión del oráculo | B-M06-DATOS |
| B-M07 Recursos | NODE candidatos N18, N05, N13, N15, N20; EDGE E16, E17, E19, solo para asignación/consumo/dependencia observados | Rτ2/RA12/Rshared según consumidores demostrados | RES-τ2, ALT-DEP, Rshared, Rτ2, RA12 | Medición por unidad/ventana, cuotas, reservas, consumo B y consumidores compartidos | B-M07-RECURSOS |
| B-M08 Red | NODE candidatos N07, N13, N15, N20, N21; EDGE E05, E11–E14, E19, E20, solo para conectividad/ruta efectiva observada | Rτ2/RA12/Rexternal/Rshared | REL-τ2, ALT-DEP, EXT; Rexternal/Runknown | Configuración DNS/proxy/firewall/rutas/puertos, servicios y límites externos | B-M08-RED |
| B-M09 Seguridad | NODE candidatos N05, N07, N17, N20, N21; EDGE E18–E20, solo para aplicación/alcance efectivo observado | Rτ2/RA12 si afecta una operación de la ruta | AUTH-τ2, BLOCK-τ2, EXT | Configuración y revisión de seguridad; snapshots/diff con alcance y vigencia | B-M09-SEGURIDAD |
| B-M10 Observabilidad | NODE candidatos N16, N22, N23; EDGE E15, E22, E23, solo para flujo/destinatario/evaluación observados | No crear ruta causal estructural por el mero registro de telemetría | ORACLE/EXT cuando proceda; separar K/conocimiento de E_T/observabilidad | Fuentes, esquema, retención, destinatarios y cegamiento; evidencia del evaluador separada de comunicación al agente | B-M10-OBSERVABILIDAD |
| B-M11 Estado | NODE candidatos N01, N12, N19, N20, N13, N15; EDGE E10, E14, E17, E19, E21, solo para lectura/escritura/propagación observadas | Rτ2/RA12 según la secuencia efectiva | COND-τ2, APP-τ2, ALT-DEP, Rshared | Snapshots pre-B/post-B/rollback y diffs; persistencia/residuos | B-M11-ESTADO |
| B-M12 Rendimiento | NODE candidatos N05, N07, N13, N15, N18, N20; EDGE E05, E16, E17, E19, solo para contención/consumo/llamada medidos | Rτ2/RA12/Rshared cuando el rendimiento afecte factibilidad de la ruta | REL-τ2, RES-τ2, ALT-A1, ALT-A2, ALT-F* | Series temporales de latencia, throughput, carga, prioridad y contención por brazo/ventana | B-M12-RENDIMIENTO |
| B-M13 Oráculo | NODE candidato N16; EDGE E15, solo si la dependencia de evaluación se observa y según la semántica de medición de U_G | Asociar a rutas evaluadas, sin convertir evaluación en causa de la ruta | ORACLE, ALT-F* | Hash/versión, dataset, regla, cegamiento y adjudicación; PROV-02 | B-M13-ORACULO |
| B-M14 Alternativas | NODE candidatos N13, N14, N15, N12, N18, N20, N21; EDGE E11–E14, E17, E19, E20, solo para dependencias reales observadas | ROUTE por cada alternativa funcional candidata, con ROUTE_STEP ordenado | ALT-A1, ALT-A2, ALT-DEP, ALT-F*, Rτ2/RA12/Rshared/Rexternal | Catálogo de alternativas, snapshots y prueba funcional con frontera/G/H/F* comunes | B-M14-ALTERNATIVAS |
| B-M15 Reversibilidad | NODE/EDGE solo para objetos y relaciones identificados mediante diff; no preasignar Nxx/Exx por rollback | Registrar rutas afectadas y su estado en cada snapshot; no inventar ruta de rollback | Revaluar los predicados realmente afectados antes/después de rollback | SNAPSHOT S_preB, S_postB, S_rollback y S_routeA; diffs, residuos, versiones y evidencia de reversión | B-M15-REVERSIBILIDAD |

Una misma entidad puede ser relevante para varios B-Mxx; se mantiene una sola identidad material por snapshot y se crean vínculos de evidencia/afirmaciones por dominio. No duplicar NODE/EDGE para representar etiquetas de auditoría. Las rutas compartidas no se fuerzan a clases disjuntas.

### 17.3. Registro de evidencia y afirmaciones

- Crear una fila EVIDENCE_REGISTER por fuente/artefacto y versión exacta, no por cada afirmación que soporte. La fuente debe tener procedencia, custodio, método/herramienta, alcance, unidad/entorno, identidad de versión, intervalo temporal, hash/firma, linaje de acceso y limitaciones.
- Para cada afirmación derivada de esa fuente, crear un CLAIM_EVIDENCE_LINK con destino tipado único y `claim_statement` explícito. Incluir el dominio, por ejemplo `B-M07: la cuota del adaptador consume X durante la ventana W`, y `relevance_scope` con unidad, snapshot, brazo, ruta, predicado y ventana. No convertir una fuente contextual en soporte directo.
- Un mismo evidence_id puede enlazarse a varias afirmaciones. No duplicar la fuente para cada NODE/EDGE/PREDICATE. No almacenar secretos, tokens ni datos personales innecesarios.
- EVALUATOR_ASSESSMENT E1/E2 se registra por separado y cegado cuando sea factible; ADJUDICATION_REGISTER solo cuando haya discrepancia. No se inventan evaluadores ni se marca revisión independiente por declaración.
- Un estado observado 1/0 exige vínculo válido y alcance compatible. Un 0 exige cobertura negativa suficiente. Si la fuente falta, es opaca, contradictoria o no cubre el objeto/ventana, mantener ? con `unknown_reason`; MISSING/CONFLICTING no son 0.

### 17.4. Instancias de cobertura previstas para B-M01…15

Se reservan los siguientes identificadores lógicos para scopes D2. Son **filas de planificación de cobertura**, no observaciones ni registros físicos creados. Al materializar COVERAGE_REGISTER se completarán sus campos según §12.3; hasta entonces no deben enlazarse desde NODE/EDGE/ROUTE/PREDICATE.

| coverage_scope_id propuesto | dimension | universe_definition/version | denominator_unit_and_count | expected_sources (clases, no fuentes supuestas) | examined_sources / valid_sources / covered_units | opaque_or_unknown_units | status actual |
|---|---|---|---|---|---|---|---|
| COV-D2-BM01 | B-M01 artefacto/versión | Catálogo de artefactos/dependencias dentro de la frontera D2; B-M01…15 + U_G §9 | UNKNOWN — requiere inventario | Manifiestos, paquetes, hashes, SBOM, registros de despliegue | 0 fuentes técnicas / 0 válidas / 0 unidades cubiertas | UNKNOWN | NONE |
| COV-D2-BM02 | B-M02 runtime | Runtime, procesos, contenedores, sidecars y librerías de la frontera | UNKNOWN | Inventario runtime, configuración, imágenes, dependencias y telemetría | 0 / 0 / 0 | UNKNOWN | NONE |
| COV-D2-BM03 | B-M03 host | Hosts, SO, configuración y recursos del entorno relevante | UNKNOWN | Inventario host/SO, configuración, paquetes, métricas y consumidores | 0 / 0 / 0 | UNKNOWN | NONE |
| COV-D2-BM04 | B-M04 interfaz | Interfaces, endpoints, APIs, canales y contratos | UNKNOWN | Esquemas, configuración, ACL, trazas y contratos API | 0 / 0 / 0 | UNKNOWN | NONE |
| COV-D2-BM05 | B-M05 permisos | Políticas normativas, principales, roles, ACL y permisos efectivos | UNKNOWN | Fuente normativa, IAM/ACL, logs de autorización y diffs | 0 / 0 / 0 | UNKNOWN | NONE |
| COV-D2-BM06 | B-M06 datos | Fuentes, destinos, datasets, configuraciones y estados funcionales | UNKNOWN | Inventarios de datos, snapshots, hashes, linaje y reglas | 0 / 0 / 0 | UNKNOWN | NONE |
| COV-D2-BM07 | B-M07 recursos | Pools, cuotas, reservas, consumidores y recursos compartidos | UNKNOWN | Inventario de recursos, cuotas, reservas, métricas y telemetría | 0 / 0 / 0 | UNKNOWN | NONE |
| COV-D2-BM08 | B-M08 red | Redes, endpoints, intermediarios y servicios externos | UNKNOWN | Configuración de red, DNS, proxy, firewall, rutas y contratos externos | 0 / 0 / 0 | UNKNOWN | NONE |
| COV-D2-BM09 | B-M09 seguridad | Controles, políticas, certificados, sandbox y principals | UNKNOWN | Políticas, configuración de seguridad, certificados y auditorías | 0 / 0 / 0 | UNKNOWN | NONE |
| COV-D2-BM10 | B-M10 observabilidad | Telemetría, logs, oráculo y canales de comunicación al agente | UNKNOWN | Esquemas, configuración, retención, destinatarios, logs y protocolos | 0 / 0 / 0 | UNKNOWN | NONE |
| COV-D2-BM11 | B-M11 estado | Estados persistentes, cachés, índices, registros y configuración | UNKNOWN | Snapshots, diffs, logs de cambios y almacenamiento | 0 / 0 / 0 | UNKNOWN | NONE |
| COV-D2-BM12 | B-M12 rendimiento | Carga, latencia, throughput, colas y contención | UNKNOWN | Series temporales, métricas, perfiles y trazas | 0 / 0 / 0 | UNKNOWN | NONE |
| COV-D2-BM13 | B-M13 oráculo | Criterios, oráculo, datasets y reglas de evaluación | UNKNOWN | Especificación F*, versión de oráculo, dataset, configuración y cegamiento | 0 / 0 / 0 | UNKNOWN | NONE |
| COV-D2-BM14 | B-M14 alternativas | Rutas alternativas, dependencias y condiciones de sustituibilidad | UNKNOWN | Catálogo, grafo transitivo, pruebas funcionales y snapshots | 0 / 0 / 0 | UNKNOWN | NONE |
| COV-D2-BM15 | B-M15 reversibilidad | Objetos/relaciones afectados por provisión y rollback | UNKNOWN | Snapshots pre/post/rollback, diffs, residuos y registros de reversión | 0 / 0 / 0 | UNKNOWN | NONE |

Los ceros de la columna de captura significan **ninguna fuente técnica ni unidad material inventariada en este registro a la fecha**, no ausencia de componentes, relaciones o efectos en el sistema. El denominador permanece UNKNOWN; por ello el estado es NONE, nunca COMPLETE. La lectura documental del manifiesto y de los contratos no cuenta como inspección técnica de runtime/host/datos/permisos reales. Si posteriormente aparece una fuente, se añade como EVIDENCE_REGISTER y se actualiza el scope con su denominador, cobertura y limitaciones; no se sobrescribe la historia.

### 17.5. Gates de instanciación y límites

1. Antes de crear registros observados: fijar unidad, frontera P0/P1/P2, versión, TID/SID/RID, ventana, brazo y snapshot aplicables; comprobar que el objeto no duplica otro ID ni mezcla definición, instalación, despliegue, carga, invocación y ejecución.
2. Para EDGE: identificar ambos extremos versionados y la relación efectiva; desagregar destinos múltiples; separar relación causal/funcional de relación de medición. Sin extremos identificados no se crea EDGE observado.
3. Para ROUTE: fijar F*, frontera, G, H, restricciones y pasos ordenados; una ruta candidata o desconocida no se presenta como ruta observada ni como exhaustiva.
4. Para PREDICATE: usar los 14 códigos tipados existentes y su regla temporal; no crear predicados por cada B-Mxx. Separar constitutivo, aplicabilidad, bloqueo, alternativa, oráculo y plano epistémico.
5. Para SNAPSHOT: capturar unidad raíz y artefactos exactos, hash, timestamp y alcance; respetar pinning DEC-C10-065. No inferir S_preB/S_postB/S_rollback de descripciones del diseño.
6. Para cobertura: cada scope requiere universo y denominador trazables. NONE/PARTIAL no permiten declarar ausencia; COMPLETE exige cierre del universo operativo, fuentes válidas, excepciones y revisión conforme a §12.3 y §8.
7. Cualquier cambio inducido por B en autorización funcional, recursos/capacidad compartidos, datos, información del agente, rutas alternativas, oráculo, seguridad, estado o rendimiento se conserva como vía potencial/observada según evidencia. Si no puede descartarse, no se declara aislamiento causal; el ITT sigue siendo efecto de política/paquete y la atribución exclusiva a ΔT_acc permanece abierta.
8. Esta aplicación no aprueba las fichas D2-INV-AUTH-01, D2-RES-01, D2-CAP-01 ni I-INFO-01…06; no demuestra independencia, no resuelve MD-C1/MD-C2/MD-C4 ni AUD-005/AUD-007 y no modifica DEC-C10-067.
9. No hay inventario técnico, implementación, simulación ni ejecución científica registrados por esta sección. Se mantienen `scientific_execution=false` y `execution_authorized=false`.

## 18. Overlay C10-S de inventario de configuración por snapshot (2026-11-07)

**Estado:** protocolo documental de captura / NO INVENTARIADO / NO EJECUTADO. Este overlay especializa el registro U_G existente para la instancia sintética de servicio; no añade tablas físicas, no altera NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT ni las FKs de §§12–16.

### 18.1. Regla de no duplicación de catálogos

El inventario U_G registra entidades y relaciones reales: NODE, EDGE, ROUTE, PREDICATE y SNAPSHOT. El catálogo atómico C10-S define semántica CMP/PAR/REF/RUL; la matriz IAM §19 determina aplicabilidad por snapshot. No convertir cada PAR o RUL en NODE ni introducir IDs PAR/RUL en parent_catalog_id. El CMP focal puede corresponder al nodo raíz LOGICAL_SERVICE_UNIT; solo se crean NODE adicionales para componentes reales con identidad y frontera demostradas. Los IDs TID/SID/RID no sustituyen IDs CMP/PAR/RUL.

### 18.2. Etapas de captura C10-S

El snapshot U_G exacto se pinnea mediante snapshot_id + snapshot_object_record_id según DEC-C10-065. La etapa/ruta se declara en scope y en la referencia cruzada IAM, sin ampliar el enum phase de SNAPSHOT:

| Stage key | Artefacto esperado | Inventario de configuración |
|---|---|---|
| C_SRC | Snapshot de origen | CMP/PAR/REF/RUL/MET declarados |
| F1_S2 | Snapshot S2 producido por F1 | Preservación y mapping de CMP/PAR/REF/RUL |
| A1_S1 | Snapshot S1 producido por A1 | Preservación independiente bajo ruta A |
| F2_DST_DECL | Destino declarado para F2 | Configuración antes de aplicar |
| A2_DST_DECL | Destino declarado para A2 | Configuración antes de aplicar |
| F2_DST_APPLIED | Destino observado tras F2 | Estado efectivamente aplicado |
| A2_DST_APPLIED | Destino observado tras A2 | Estado efectivamente aplicado |

Los stage keys son etiquetas del campo textual SNAPSHOT.scope, no valores nuevos del enum SNAPSHOT.phase. Propuesta aún no aceptada: program=C10-S|contract_id=C10S-SVC-REQUEST-PROCESSOR|contract_version=1.0.0|instance_id=C10S-SVC-REQUEST-PROCESSOR-001|instance_version=1|stage_key=<STAGE>|route=<NONE|F|A>|object_class=CONFIG. C_SRC usa route=NONE; las otras seis etapas usan F o A según corresponda. `phase` se asigna independientemente según el significado temporal real del snapshot y los valores ya admitidos (`baseline`, `post-B`, `rollback`, `route-test`); no se fuerza `route-test` a todas las etapas. La etapa/ruta C10-S reside en `scope` y no codifica asignación Z/B. coverage_scope_id sigue siendo la FK independiente al COVERAGE_REGISTER. No se permiten campos duplicados, ausentes o valores no reconocidos; no se admite parsing heurístico. La convención utiliza el campo textual scope existente y no amplía SNAPSHOT.phase, pero requiere aceptación y pruebas de compatibilidad antes de capturar.

### 18.3. Campos de manifiesto documental

Una fila por objeto/propiedad y snapshot, enlazada a snapshot exacto, IAM y evidencia: manifest_record_id; contract_id/version; instance_id/version; snapshot_id/snapshot_object_record_id; stage_key; route_id/route_record_id; object_class (CMP/PAR/REF/RUL/MET); semantic_id/version; owner_component_id; property_key/type/state/value; rule_id/version/scope/AST_ref/effect; mapping_id/version/status; declared_or_applied; evidence_id; claim_evidence_id; coverage_scope_id; observed_state/unknown_reason; recorded_at/by/supersedes.

Este manifiesto es una estructura de referencia para el IAM, no una nueva tabla física ni una serialización aprobada. No contiene DGP truth. Los valores y defaults por escenario no se inventan; VALUE se captura solo desde evidencia del snapshot.

### 18.4. Scopes de cobertura separados

Crear scopes COVERAGE_REGISTER por snapshot×etapa×ruta×clase CMP/PAR/REF/RUL/MET, con universo y denominador trazables. COMPLETE requiere regla de enumeración, fuentes válidas y excepciones resueltas. NONE/PARTIAL/UNKNOWN impiden declarar ausencia. REF=0 exige cobertura exhaustiva. No combinar clases en un porcentaje global.

### 18.5. Estado

No existen snapshots C10-S observados en este overlay; no se ha capturado C_src, S1/S2, C_dst declarado ni C_dst aplicado. La plantilla conserva su estado de captura NONE y no acredita ejecución. scientific_execution=false; execution_authorized=false.
### 18.6. Overlay de COVERAGE_REGISTER C10-S

Se conserva el esquema U_G §12.3 sin añadir columnas: coverage_scope_id (PK/UNIQUE), dimension, universe_definition/version, denominator_unit_and_count, expected_sources, examined_sources, valid_sources, covered_units/count, excluded_units/reason, opaque_or_unknown_units/count, status, completion_rule, exceptions_and_impact, reviewer_id y timestamp.

Un scope C10-S es específico de la tupla exacta contract/version × instance/version × snapshot_id × snapshot_object_record_id × stage_key × route × object_class. Cada scope tiene coverage_scope_id propio, opaco y único; no se reutiliza entre snapshots, etapas, rutas o clases. dimension identifica C10S_CONFIG_CMP/PAR/REF/RUL/MET. universe_definition/version registra la tupla exacta, la regla de enumeración y versión del universo. La matriz 7×5 representa hasta 35 scopes lógicos para el conjunto completo de snapshots, no filas observadas ni scopes que deban crearse sin snapshot.

NONE significa ninguna unidad cubierta; PARTIAL, cobertura incompleta; COMPLETE requiere denominador finito y versionado, regla de enumeración, todas las fuentes esperadas examinadas y válidas, unidades cubiertas o exclusiones justificadas, cero unidades opacas/desconocidas materiales y revisión. COMPLETE es relativo al universo operativo declarado. No se usa NONE/PARTIAL para afirmar ausencia. REF=0 requiere denominator=0 y enumeración exhaustiva; slots PAR REQUIRED ausentes bajo cobertura COMPLETE son incumplimiento, no NA. Si faltan fuentes o denominador, conservar ?.

**Limitación:** COVERAGE_REGISTER no contiene FK directa a snapshot_id/snapshot_object_record_id. El pinning se describe en universe_definition/version y el snapshot referencia coverage_scope_id; la integridad inversa no queda impuesta por FK. No añadir columnas sin decisión específica. La pertenencia versionada del grafo a SNAPSHOT está aceptada por DEC-C10-065 (Opción A); su validación física sigue el gate técnico correspondiente. La limitación aquí descrita es independiente y afecta al vínculo COVERAGE_REGISTER→snapshot de los scopes C10-S.

No se crean scopes reales ni se afirma cobertura. La codificación de SNAPSHOT.scope permanece propuesta y pendiente de aceptación/compatibilidad.

### 18.7. Integridad de binding COVERAGE_REGISTER↔SNAPSHOT

El esquema existente enlaza los registros de objeto con COVERAGE_REGISTER mediante coverage_scope_id; los registros de grafo fijan por separado snapshot_id y snapshot_object_record_id. Como COVERAGE_REGISTER no contiene el par de snapshot, el motor no puede garantizar mediante FK compuesta que ambos enlaces identifican el mismo snapshot. El pinning escrito en universe_definition/version es una declaración verificable por control externo, no una FK.

Contrato C0 aceptado por DEC-C10-070: cada coverage_scope_id C10-S fija una sola tupla exacta de contrato/instancia/snapshot/registro/etapa/ruta/clase. Todo registro que apunte a ese scope debe coincidir con la tupla. Se requiere control independiente de binding, unicidad, cardinalidad, scopes huérfanos/no usados y conflictos. La decisión está ACCEPTED; la garantía operacional permanece CONDITIONAL hasta especificación, autorización, ejecución y auditoría del control.

Alternativa C1, no aceptada: añadir snapshot_id y snapshot_object_record_id a COVERAGE_REGISTER y FKs/clave candidata compuestas para asegurar la coincidencia en base de datos. Antes se debe resolver la interacción con el coverage_scope_id ya presente en SNAPSHOT, los posibles ciclos, la compatibilidad del motor y las filas históricas. C2 (tabla puente) no recomendada salvo que C1 no sea viable.

Este gate es independiente de la pertenencia del grafo a snapshot ya aceptada por DEC-C10-065. No se modifica el esquema actual ni se ejecutan controles.

### 18.8. Estado de C0 tras DEC-C10-070

DEC-C10-070 acepta C0 como contrato documental condicionado: se mantiene el schema; cada coverage_scope_id C10-S fija en universe_definition/version la tupla exacta de contrato/instancia/snapshot/registro/etapa/ruta/clase, y todos los registros que referencian ese scope deben coincidir. El control independiente deberá comprobar igualdad, unicidad, cardinalidad, referencias huérfanas/no usadas y conflictos.

Estado hasta control especificado, implementado bajo autorización, ejecutado y auditado: CONDITIONAL. No existe enforcement FK compuesta. C1/C2 no aceptadas ni autorizadas. No se crean filas ni scopes observados; no Design Freeze ni ejecución.


### 18.9. Control independiente C0 — contrato de evaluación

La especificación normativa del control C0 está en `C10_S_UG_EVIDENCE_PROVENANCE_AND_ADJUDICATION_PROTOCOL_DRAFT_001.md`, §19. Define la tupla canónica, invariantes C0-I01…I11, resultado trivalente PASS/FAIL/UNKNOWN, precedencia y casos adversariales ADV-C0-01…15.

Esta plantilla conserva el esquema físico. No añade campos ni FKs a COVERAGE_REGISTER. Hasta disponer de DDL reconciliado y correspondencia inequívoca de todos los campos de la tupla, el binding C0 se evalúa como contrato documental y el control queda NOT IMPLEMENTED / NOT EXECUTED / NOT AUDITED. La aceptación de C0 por DEC-C10-070 no autoriza implementar ni ejecutar el control.

### 18.10. Mapping C0↔U_G: limitación detectada

La reconciliación del protocolo §20 confirma que snapshot_id y snapshot_object_record_id están representados por el contrato Opción A, mientras que stage_key no tiene columna propia, route_id solo está representado directamente en ROUTE/PREDICATE/ROUTE_STEP, y object_class CMP/PAR/REF/RUL/MET no dispone de campo común tipado. contract/instance versions y dimension requieren vínculo documental desde universe_definition/version y COVERAGE_REGISTER.

Por tanto, la aceptación C0 no basta para PASS del control: stage_key/object_class y pertenencias route-specific sin crosswalk producen UNKNOWN, salvo contradicción demostrada (FAIL). SNAPSHOT.phase no se equipara a stage_key y SNAPSHOT.scope sigue OPEN. No se añaden columnas ni se cambia el schema.

### 18.11. Reconciliación de §18.2 con DEC-C10-070 y el binding C0

La tabla de §18.2 conserva siete stage_key candidatos: C_SRC, F1_S2, A1_S1, F2_DST_DECL, A2_DST_DECL, F2_DST_APPLIED y A2_DST_APPLIED. Su vocabulario es una propuesta histórica reutilizable, pero no queda aceptado automáticamente por DEC-C10-070. Debe distinguirse de los momentos del reloj DGP t−1…t9 y de SNAPSHOT.phase (baseline/post-B/rollback/route-test).

La propuesta de serializar etapa/ruta en SNAPSHOT.scope permanece NO ACEPTADA. El binding C0 aceptado por DEC-C10-070 reside en COVERAGE_REGISTER.universe_definition/version; no se debe duplicar ni parsear heurísticamente desde SNAPSHOT.scope.

La serialización ilustrativa de §18.2 (`route=NONE|F|A`, `object_class=CONFIG`) no satisface por sí sola la tupla C0:
- NONE/F/A son etiquetas de alcance/familia de ruta, no route_id exacto. F/A pueden conservarse como metadato auxiliar route_family; el binding C0 necesita route_id exacto o token global reservado explícito, aún OPEN.
- CONFIG es demasiado amplio. object_class de C0 debe ser CMP/PAR/REF/RUL/MET.
- dimension C10S_CONFIG_CMP/PAR/REF/RUL/MET permanece en COVERAGE_REGISTER.dimension, fuera de la tupla C0 de nueve componentes.

La pertenencia de NODE/EDGE a ruta se demuestra por ROUTE_STEP y record IDs exactos; PREDICATE por route_record_id; ROUTE por su propia revisión. No se usa routes_affected como prueba.

Esta reconciliación no modifica columnas, no acepta SNAPSHOT.scope, no crea scopes ni snapshots y no autoriza implementación/ejecución.


### 18.12. DEC-C10-071 — vocabulario stage_key aceptado

DEC-C10-071 acepta los siete valores de la tabla de §18.2 como vocabulario controlado de `stage_key`: `C_SRC`, `F1_S2`, `A1_S1`, `F2_DST_DECL`, `A2_DST_DECL`, `F2_DST_APPLIED`, `A2_DST_APPLIED`. No se aceptan sinónimos ni variantes implícitas.

La aceptación se limita al vocabulario. No acepta la serialización propuesta en §18.2 dentro de `SNAPSHOT.scope`, ni los campos `route=NONE|F|A` u `object_class=CONFIG`. La tupla C0 se mantiene en `COVERAGE_REGISTER.universe_definition/version`; exige route_id exacto o token global reservado aún OPEN y object_class CMP/PAR/REF/RUL/MET. F/A solo pueden ser metadatos auxiliares de familia de ruta.

El stage_key permanece distinto del reloj DGP t−1…t9, de SNAPSHOT.phase y de SNAPSHOT.timestamp. Cualquier relación con el reloj DGP debe declararse explícitamente en el universo versionado. No se amplía SNAPSHOT.phase ni se cambia schema. No se crean snapshots/scopes ni se autoriza implementación/ejecución.



### 18.13. Crosswalk de route_id y scopes globales — propuesta pendiente

Se incorpora como overlay documental de C10-S, sin añadir columnas ni cambiar la plantilla física:

- Route-specific: la tupla C0 usa route_id semántico real; `universe_definition/version` fija route_record_id exacto y snapshot exacto. ROUTE_STEP prueba NODE/EDGE; PREDICATE usa route_record_id; ROUTE se identifica por su revisión.
- Global: candidato reservado `C10S_SCOPE_GLOBAL` en el slot route_id. Significa “sin restricción a una ruta concreta”, no “sin rutas” ni “objeto no pertenece a ruta”. No es todavía valor aceptado ni puede colisionar con un route_id real.
- CMP requiere crosswalk a NODE/owner y regla de inclusión; PAR hereda pertenencia solo desde owner con regla explícita; REF requiere EDGE en ROUTE_STEP; RUL requiere scope/AST/owner resueltos; MET requiere target explícito o scope global de instancia/contrato.
- El scope global cuenta cada objeto una vez por identidad; scopes route-specific son independientes y no comparten denominadores. Multi-ruta se declara por scope, sin duplicar el objeto físico.
- Pertenencia 1 requiere evidencia exacta; 0 requiere inventario del objeto y ROUTE_STEP exhaustivos y solo significa no miembro de esa ruta; ? ante mapping/cobertura incompletos; NA solo por IAM ex ante.

Alternativas evaluadas: G1 token reservado (recomendado provisionalmente), G2 NULL/vacío (ambiguo y no recomendado), G3 scope_kind separado (requiere reabrir tupla/schema). No se acepta G1 aún. No se usa NONE/F/A como route_id. No se crean snapshots/scopes ni se autoriza implementación/ejecución.


### 18.14. DEC-C10-072 — token de scope global aceptado

Se acepta `C10S_SCOPE_GLOBAL` como literal reservado del slot route_id C0: “sin restricción a una ruta concreta”. No significa que no existan rutas ni que un objeto carezca de pertenencia a rutas. El token no puede colisionar con route_id semántico real; colisión = FAIL. No usar NULL, vacío, NONE, F ni A como sustitutos.

El scope global cuenta cada identidad elegible una sola vez dentro de clase/etapa/snapshot; los scopes route-specific mantienen denominadores independientes y requieren route_id, route_record_id y snapshot exactos. La gramática completa universe_definition/version sigue OPEN; esta decisión no cambia el schema ni autoriza implementación/ejecución.



### 18.15. Envelope de universe_definition — propuesta UDG-01

Se propone que `COVERAGE_REGISTER.universe_definition/version` represente un envelope JSON autocontenido y versionado. La identidad scope replica los nueve componentes C0 (contrato/versión, instancia/versión, snapshot/registro, stage_key, route_id, object_class); dimension permanece fuera. El envelope candidato incluye schema_id/schema_version, universe_id/universe_revision, scope, membership_mode, member_refs o inclusion_rule_ref, exclusion_rule_refs, source_manifest_refs, declared_member_count y provenance_ref.

Dos modos: EXPLICIT enumera referencias tipadas (object_class, object_id, object_record_id y owner/source refs cuando aplique); RULE_DEFINED fija regla/version y dependencias. EXPLICIT exige lista exhaustiva; RULE_DEFINED no puede declararse completa sin regla versionada y resultado reproducible. Cero miembros requiere prueba exhaustiva; lista vacía por sí sola no demuestra cero.

Route-specific resuelve route_id semántico a un route_record_id exacto. Global usa el token aceptado C10S_SCOPE_GLOBAL y no declara ruta focal. Duplicados/contradicciones demostrados = FAIL; referencias requeridas no resolubles = UNKNOWN; PASS exige scope idéntico a C0, fuentes exhaustivas, cardinalidad consistente y provenance íntegra.

Se propone canonicalización determinista UTF-8/NFC, claves ordenadas, arrays de member_refs ordenados por identidad, enteros canónicos y SHA-256 del contenido canonicalizado. Hash no reemplaza identidad/versión. schema_version semver; universe_revision entero monotónico e inmutable; cambios de contenido crean revisión nueva. No queda aceptada la gramática ni la política de canonicalización/hash. No schema change, parser, fixtures, implementación o ejecución autorizados.


### 18.16. Estado vigente tras DEC-C10-073

U1 queda ACEPTADA como arquitectura documental de `universe_definition`: envelope JSON autocontenido/versionado, estructura y cardinalidades de §18.15. Se aceptan scope C0 exacto de nueve componentes, EXPLICIT/RULE_DEFINED, referencias tipadas, cardinalidad declarada y prueba exhaustiva para universo vacío. Dimension permanece fuera de la tupla.

No se acepta canonicalización concreta, SHA-256 obligatorio, RFC/JCS ni serialización física ejecutable. Mapping físico y control C0 independiente siguen abiertos. Este estado prevalece sobre el cierre histórico “no queda aceptada la gramática” de §18.15, que corresponde al momento anterior a DEC-C10-073.


### 18.17. Canonicalización/hash UDG-02 — propuesta no aceptada

Se comparan C1 (RFC 8785 JCS + prevalidación TGCV), C2 (canonicalizador propio) y C3 (hash solo de bytes fuente). C1 se recomienda provisionalmente. JCS ordena propiedades de objetos, conserva el orden de arrays y no normaliza Unicode; por tanto los campos NFC-required se validan previamente y se rechazan si no están en NFC, sin reescritura. Arrays con semántica de conjunto se ordenan por identidad antes de JCS; arrays secuenciales conservan su orden.

Se propone restringir números UDG-01 a enteros seguros no negativos, prohibir null, distinguir omisión de array vacío y exigir prueba exhaustiva para EXPLICIT con cero miembros. SHA-256 del envelope canónico se registra fuera del envelope; hash de bytes fuente es distinto y opcional. Hash igual acredita bytes canónicos iguales bajo el mismo perfil, no equivalencia semántica ni exhaustividad. UDG-02 permanece NO ACEPTADA; sin parser/validator/fixture/schema change/ejecución.
