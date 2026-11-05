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
