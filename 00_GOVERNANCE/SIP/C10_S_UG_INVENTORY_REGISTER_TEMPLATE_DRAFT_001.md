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

| route_id | ordered_node_edge_sequence | route_class (focal/alternative/native/manual/external/shared/fallback/recovery/unknown) | entry_state | target/F* | G | H/window | C0/constraints | version_set | shared_dependencies | affected_by_B | functional_substitutability (1/0/?) | evidence_ref | coverage_status | evaluator/blinding | unresolved_alternatives | notes |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | unknown | — | — | — | — | — | — | — | ? | ? | — | NONE | — | Runknown | Fila de esquema; no representa ruta real |

## 5. Registro de predicados por ruta/paso/tiempo

| predicate_id | route_id | step | time/snapshot | predicate_type (ID/REL/COND/AUTH/RES/DEP/BLOCK/APP/ALT/ORACLE/EXT) | truth_dgp (restricted) | observed_state (1/0/?) | evidence_ref | coverage_scope | source/version/hash | adjudication_rule/tolerance | evaluator/blinding | reason_for_unknown | impact_on_A_f/App/Reach/F_alt/IV | timestamp |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| — | — | — | — | — | RESTRINGIDO | ? | — | NONE | — | — | — | No existe evidencia aportada | Mantener indeterminación | — |

truth_dgp es una columna reservada al generador/evaluador independiente; no debe exponerse al analizador. En inventario real sin DGP conocido, mantenerla vacía/restringida.

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
