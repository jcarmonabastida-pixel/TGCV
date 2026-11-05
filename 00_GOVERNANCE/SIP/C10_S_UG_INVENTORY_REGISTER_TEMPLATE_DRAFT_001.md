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
- Toda fila debe incluir procedencia, versión, fecha, responsable/evaluador y limitaciones.

## 2. Registro de nodos

| node_id | semantic_role | class | TID | SID | RID | version/build/hash | owner/boundary | consumers/routes/arms | direct_dependencies | external/shared_resource | permissions/state | evidence_ref | observed_status (1/0/?) | coverage_status (NONE/PARTIAL/COMPLETE) | evaluator/blinding | timestamp | notes/unknowns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | NO INVENTARIADO | — | — | — | — | — | — | — | — | — | — | — | ? | NONE | — | — | Fila de esquema; no representa componente real |

## 3. Registro de aristas/dependencias

| edge_id | source_node | target_node | relation_type | direction | direct_or_transitive | version_constraint | time_window | condition | arms/routes_affected | resource_or_permission | necessary_for_path | evidence_ref | observed_status (1/0/?) | coverage_status | evaluator/blinding | timestamp | unknowns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | NO INVENTARIADO | — | — | — | — | — | — | — | ? | — | ? | NONE | — | — | Fila de esquema; no representa dependencia real |

## 4. Registro de rutas y substituibilidad

| route_id | parent_route_class (Rτ2/RA12/Rshared/Rexternal/Runknown) | route_subtype (native/manual/fallback/recovery/other) | ordered_node_edge_sequence | entry_state | target/F* | G | H/window | C0/constraints | version_set | shared_dependencies | affected_by_B | functional_substitutability (1/0/?) | evidence_ref(s) | coverage_scope_id | evaluator_record_id | unresolved_alternatives | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | Runknown | unknown | — | — | — | — | — | — | — | — | ? | ? | — | — | — | Runknown | Fila de esquema; no representa ruta real |

## 5. Registro de predicados por ruta/paso/tiempo

| predicate_id | route_id | step | time/snapshot | predicate_type (ID/REL/COND/AUTH/RES/DEP/BLOCK/APP/ALT/ORACLE/EXT) | observed_state (1/0/?) | evidence_ref(s) | coverage_scope_id | source/version/hash | adjudication_rule/tolerance | evaluator_record_id | reason_for_unknown | impact_on_A_f/App/Reach/F_alt/IV | timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | ? | — | — | — | — | — | No existe evidencia aportada | Mantener indeterminación | — |

**La truth del DGP no forma parte de esta tabla ni de ningún artefacto visible al analizador.** Se almacena únicamente en un registro separado, segregado y con control de acceso del generador/evaluador autorizado. Esta plantilla contiene solo observed_state y evidence_ref.

## 6. Registro de snapshots y fuentes

| snapshot_id | unit_id | phase (baseline/post-B/rollback/route-test) | timestamp | scope | source_artifacts | version/hash | method | coverage_limitations | custodian | integrity_check | evidence_ref |
|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | No capturado | — | — | — |

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

La plantilla se entrega vacía de observaciones reales. Todos los registros de ejemplo son filas de esquema, no nodos, aristas o rutas existentes. Cobertura NONE; A_f*=?, F_alt,0=?, Reach_H=?. No hay evidencia de instalación, runtime, SBOM, snapshots, grafo de dependencias, no-afectación A1/A2 ni independencia de B. No se ha ejecutado auditoría técnica, simulación ni experimento.


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

Añadir a los registros node/edge/route/predicate: parent_catalog_id, evidence_status (AVAILABLE/MISSING/CONFLICTING), contract_intent (intención normativa, no observación), coverage_scope_id, source_provenance, review/adjudication_status y unknown_reason. Para aristas, parent_edge_id y atomic_edge_id; para rutas, route_subtype y parent_route_class. Para predicados, predicate_id completo y separación truth_dgp_restricted / observed_state.

**Dictamen:** correspondencia semántica completa en los cuatro catálogos; normalización necesaria de aristas mult destino; E07 es regla lógica; E22 carece de nodos destino identificados; N16 y N23 tienen granularidad compuesta que debe revisarse. La plantilla necesita los campos complementarios anteriores antes de cerrar su esquema. No se asignan estados técnicos ni se declara inventario completo.


### 10.6. Definición de campos complementarios (schema)

Los campos siguientes pasan a formar parte del esquema obligatorio de cada tabla de registro, no son valores precargados:

| Campo | Aplicación | Dominio/uso |
|---|---|---|
| parent_catalog_id | Nodo/arista/predicado/ruta | ID de catálogo U_G de origen (Nxx, Exx, código de predicado o clase de ruta). |
| source_provenance | Todas | Documento/sistema/origen, ubicación, método de obtención, fecha y custodio. |
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

Para cada fila, evidence_ref debe resolver a un evidence_id del registro de procedencia. Los campos source_provenance, collection_method, scope, timestamp, integrity, access_lineage, completeness_limitations, evidence_status, reviewer y reproducibility se registran en el expediente de evidencia enlazado. observed_status/observed_state y coverage_status nunca se sustituyen por evidence_status. Ningún 0 se admite sin argumento de cobertura negativa; ningún COMPLETE sin universo, denominador y excepciones. Las discrepancias críticas requieren adjudicación independiente y preservación del desacuerdo.

El crosswalk §10 identifica que las tablas actuales aún requieren columnas explícitas para parent_catalog_id, source_provenance, evidence_status, contract_intent, coverage_scope_id, review_adjudication_status y unknown_reason; este protocolo define su semántica, pero no declara el esquema tabular completamente cerrado. La revisión de correspondencia de todas las columnas sigue abierta.


## 12. Esquema canónico normalizado de captura (Draft 001)

Esta sección es normativa para futuras instancias de la plantilla y resuelve la insuficiencia de las tablas abreviadas §§2–7. Los encabezados abreviados anteriores sirven como vistas de trabajo; cuando difieran, prevalece el esquema normalizado de esta sección. Ninguna fila de ejemplo constituye observación.

### 12.1. Registro de evidencia (EVIDENCE_REGISTER)

Una fila por artefacto/fuente y versión exacta. Un mismo evidence_id puede respaldar varias afirmaciones; cada vínculo claim-evidence se registra en CLAIM_EVIDENCE_LINK.

| evidence_id | source_class (S1–S8) | source_type | source_provenance | source_location_ref | custodian | collection_method/tool_version | scope_id | unit/environment | version_identity | timestamp_start/end_tz | integrity_hash/signature | access_lineage | completeness_limitations | confidentiality/access_ref | evidence_status | reviewer_id | reproducibility_ref |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — | — | — | — | — | — | MISSING | — | — |

No incluir secretos, credenciales ni datos personales innecesarios. source_location_ref debe ser referencia segura, no volcado de material sensible.

### 12.2. Registro de vínculo afirmación-evidencia (CLAIM_EVIDENCE_LINK)

| claim_evidence_id | claim_target_type | claim_target_id | claim_statement | evidence_id | support_type (direct/inferred/contradictory/contextual) | relevance_scope | reviewer_note |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — |

Toda fila de nodo, arista, predicado, ruta o cobertura debe enlazar al menos un claim_evidence_id cuando tenga una clasificación observada. Una fila ? puede tener cero evidencia disponible, pero debe registrar unknown_reason.

### 12.3. Registro normalizado de cobertura (COVERAGE_REGISTER)

| coverage_scope_id | dimension | universe_definition/version | denominator_unit_and_count | expected_sources | examined_sources | valid_sources | covered_units/count | excluded_units/reason | opaque_or_unknown_units/count | status (NONE/PARTIAL/COMPLETE) | completion_rule | exceptions_and_impact | reviewer_id | timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | — | — | NONE | — | — | — | — |

COMPLETE exige denominador finito y trazable, regla de enumeración, fuentes válidas, excepciones resueltas/justificadas y revisión. El porcentaje no sustituye la evaluación de superficies críticas ni la cobertura transitiva.

### 12.4. Registro de evaluación independiente (EVALUATOR_ASSESSMENT)

| evaluator_record_id | object_type | object_id | evaluator_id | role (E1/E2/ADJUDICATOR) | observed_state | evidence_ids | rule_version | scope_id | blinded_to_outcome_value | blinded_to_Z_B | confidence_or_limitations | rationale | timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | ? | — | — | — | — | — | — | — | — |

E1 y E2 deben emitir registros independientes antes de conocer la clasificación del otro. Las variables de cegamiento aceptan YES/NO/NOT_FEASIBLE con justificación; no se presupone cegamiento logrado por declarar un procedimiento.

### 12.5. Registro de discrepancia y adjudicación (ADJUDICATION_REGISTER)

| adjudication_id | object_type | object_id | evaluator_record_E1 | evaluator_record_E2 | disagreement_type | evidence_reviewed | adjudicator_id | decision (1/0/?/NA) | rule_and_reason | minority_position | unresolved_limitations | timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — | ? | — | — | — | — |

No se permite majority-vote automático. Si no se resuelve el conflicto con evidencia y regla aplicable, decisión final ?.

### 12.6. Registro de truth restringida del DGP (DGP_TRUTH_SECURE)

**No forma parte de este inventario ni del paquete accesible al analizador.** Se mantiene en el entorno/artefacto segregado del generador/evaluador autorizado, con control de acceso, versionado, hash y log de accesos. Solo se permite exportar resultados de evaluación observables autorizados y cegados; nunca los valores de truth que permitan reconstruir la asignación verdadera antes del cierre analítico. La existencia de esta tabla en el esquema conceptual no autoriza crearla ni poblarla.

### 12.7. Campos comunes obligatorios y extensión de tablas

Todas las tablas de objetos (NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT) deben incluir:
- `object_record_id` único; `parent_catalog_id`; `object_version` o versión aplicable;
- `coverage_scope_id`; `evidence_status`; `review_adjudication_status`;
- `observed_state` cuando el objeto admita clasificación trivalente;
- `evidence_ref` como uno o varios `claim_evidence_id`, nunca como texto libre sin resolución;
- `unknown_reason`; `contract_intent` cuando aplique; `created_at`, `recorded_by`, `supersedes_record_id`.

Extensiones:
- NODE: TID/SID/RID, estado declarado/instalado/desplegado/cargado/invocado/ejecutado, owner/boundary, consumers, dependencias.
- EDGE: parent_edge_id, atomic_edge_id, source_node_id, target_node_id, dirección, tipo, condición, directo/transitivo, versión/tiempo, necesidad para ruta.
- ROUTE: parent_route_class (una de cinco clases U_G) y route_subtype separado; secuencia ordenada y predicados necesarios.
- PREDICATE: predicate_id exacto, familia, ruta/paso/tiempo, observed_state, regla y tolerancia; nunca DGP truth.
- SNAPSHOT: snapshot_id, unit_id, phase, scope_id, timestamp, artefactos/hash, método, cobertura y evidence refs.

### 12.8. Reglas de consistencia entre tablas

1. evidence_ref → CLAIM_EVIDENCE_LINK.claim_evidence_id → EVIDENCE_REGISTER.evidence_id; no se aceptan referencias huérfanas.
2. Cada claim-evidence link debe tener alcance compatible con la unidad, versión, entorno y tiempo de la afirmación.
3. observed_state no se copia desde evidence_status; evidence_status no se deriva de observed_state.
4. coverage_scope_id debe resolver a una fila COVERAGE_REGISTER; no se puede declarar COMPLETE sin denominador.
5. E1/E2 se almacenan por separado; ADJUDICATION_REGISTER solo se crea cuando proceda.
6. parent_route_class no puede sustituirse por route_subtype.
7. DGP_TRUTH_SECURE no se mezcla ni sincroniza con los registros visibles al analizador.
8. Las revisiones generan nuevos registros versionados; no se sobrescribe el historial.

## 13. Auditoría campo-a-campo: resultado

La auditoría detecta que el protocolo de procedencia estaba más desarrollado que la plantilla física. Se identifican y corrigen/documentan estas brechas:

| ID | Brecha encontrada | Resolución documental | Estado |
|---|---|---|---|
| FCM-01 | No existía tabla separada EVIDENCE_REGISTER con evidence_id | §12.1–12.2 | Incorporada |
| FCM-02 | evidence_ref no resolvía explícitamente a vínculo afirmación-evidencia | Cadena de referencias §12.8.1 | Incorporada |
| FCM-03 | Cobertura carecía de denominador, fuentes válidas y unidades opacas | COVERAGE_REGISTER §12.3 | Incorporada |
| FCM-04 | No había tabla de doble evaluación individual | EVALUATOR_ASSESSMENT §12.4 | Incorporada |
| FCM-05 | No había expediente de discrepancia/adjudicación | ADJUDICATION_REGISTER §12.5 | Incorporada |
| FCM-06 | truth_dgp aparecía físicamente en la tabla de predicados | Retirada de tabla analítica; segregación §12.6 | Corregida documentalmente |
| FCM-07 | route_class mezclaba cinco clases primarias y subtipos | parent_route_class y route_subtype separados | Corregida documentalmente |
| FCM-08 | Campos complementarios no estaban como columnas/contrato común | Schema común §12.7 | Incorporado |
| FCM-09 | No existía regla de integridad referencial y versionado | §12.8 | Incorporada |

**Dictamen:** la correspondencia semántica se mantiene, pero el esquema anterior no era operacionalmente completo. El esquema normalizado queda especificado documentalmente en §12; aún requiere revisión independiente, validación de tipos/valores, y correspondencia exacta con cada tabla antes de declararse cerrado. No se han creado instancias reales, no hay inventario ni cobertura técnica. FCM-01…09 son hallazgos documentales, no tests ejecutados.
