# C10-S — Contrato de semantic_role y nodo raíz lógico U_G

**ID:** C10-S-UG-ROLE-ROOT-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** PROPUESTA DE CIERRE DOCUMENTAL; pendiente de aceptación y validación técnica.  
**Ámbito:** especialización de NODE y de la FK compuesta SNAPSHOT→NODE de DEC-C10-059.

## 1. Problema y principio de diseño

U_G contiene 23 roles de catálogo N01–N23. Esos roles describen funciones dentro del modelo causal y de medición; no son una taxonomía de clases de objetos NODE. Por ejemplo, N08 (C_dep) y N09 (predicados A_f*) son constructos/variables, mientras N04 (adaptador) y N05 (runtime) son componentes técnicos. Por tanto, no debe copiarse Nxx directamente en semantic_role ni suponerse una correspondencia uno-a-uno.

Se separan tres dimensiones:
- `parent_catalog_id`: procedencia del rol de catálogo (N01–N23).
- `semantic_role`: clase semántica del registro NODE.
- `boundary_class`: clasificación P0/P1/DUAL/NA ya aceptada en DEC-C10-059.

Ninguna dimensión implica existencia, observación, accesibilidad, cobertura ni pertenencia a una ruta.

## 2. Vocabulario controlado propuesto

Cada NODE debe utilizar exactamente un valor de esta lista versionada:

| semantic_role | Definición | Ejemplos de uso, no instancias |
|---|---|---|
| LOGICAL_SERVICE_UNIT | Ancla de identidad de la instancia lógica de servicio que se migra | Nodo raíz de SNAPSHOT |
| CONFIGURATION_ARTIFACT | Paquete, manifiesto o artefacto declarativo de configuración | P0 |
| SOFTWARE_COMPONENT | Componente ejecutable o instalable con identidad/versionado propio | Adaptador, importador, exportador |
| RUNTIME_ENVIRONMENT | Runtime, sidecar, host o entorno de ejecución | P1 |
| LIBRARY_DEPENDENCY | Librería, paquete o dependencia técnica versionada | Dependencia focal |
| INTERFACE_ENDPOINT | Interfaz, endpoint o canal técnico | Canal de invocación |
| EXTERNAL_SERVICE | Servicio/API externo fuera del control directo de la unidad | Servicio externo |
| RESOURCE_CAPACITY | Recurso, pool, capacidad o reserva compartida | CPU, cuota, pool |
| AUTHORIZATION_POLICY | Política, principal, rol o permiso efectivo | C_auth |
| DATA_STATE_SNAPSHOT | Estado/configuración/datos versionados en un instante | C_src, C_dst, S0 |
| TRANSFORMATION_SPEC | Definición versionada de una transformación | τ2, F1, F2, A1, A2 como especificaciones |
| TRANSFORMATION_EVENT | Intento, invocación o ejecución concreta de transformación | Evento de ejecución |
| ANALYTIC_CONSTRUCT | Variable, constructo o predicado analítico no material | C_dep, A_f*, Reach |
| INFORMATION_ASSET | Información o conocimiento disponible para un agente | Información de agente |
| MEASUREMENT_ORACLE | Criterio, instrumento u oráculo de evaluación | F* y su implementación de medida, distinguidos por versión |
| OUTCOME_VALUE_RECORD | Resultado o valoración contextual, con Outcome y Value separados por identidad/tiempo | Outcome, Value/contextual valuation |

Este vocabulario es una propuesta de tipado de NODE, no una ampliación del catálogo causal EDGE. Si un registro no encaja, no se fuerza la categoría: se conserva pendiente de clasificación y se propone una revisión versionada del vocabulario antes de instanciarlo.

## 3. Crosswalk N01–N23 → semantic_role

El crosswalk es de muchos-a-muchos y orientativo; no crea nodos ni aristas:

| Catálogo | semantic_role candidato | Regla |
|---|---|---|
| N01 Unidad/sistema anfitrión y S0 | LOGICAL_SERVICE_UNIT para el ancla; DATA_STATE_SNAPSHOT para S0 | Separar unidad de snapshot si tienen identidades distintas |
| N02 Asignación Z | TRANSFORMATION_EVENT | Evento de asignación, no componente técnico |
| N03 Política/proceso B | AUTHORIZATION_POLICY solo si es una política de autorización; en otro caso TRANSFORMATION_SPEC o TRANSFORMATION_EVENT según sea definición o evento | No colapsar asignación, intento y recepción |
| N04 Paquete adaptador focal | SOFTWARE_COMPONENT o CONFIGURATION_ARTIFACT | Según el objeto inventariado sea ejecutable o declarativo |
| N05 Runtime/sidecar focal | RUNTIME_ENVIRONMENT | Separar configuración si tiene ciclo de vida propio |
| N06 Librerías/dependencias focales | LIBRARY_DEPENDENCY | Una identidad/versión material por registro |
| N07 Endpoint/canal focal | INTERFACE_ENDPOINT | Distinguir interfaz lógica de endpoint desplegado |
| N08 C_dep | ANALYTIC_CONSTRUCT | Constructo derivado; no componente físico |
| N09 Predicados A_f* | ANALYTIC_CONSTRUCT | No tratar cada predicado como componente técnico |
| N10 Transformación focal τ2/F1 | TRANSFORMATION_SPEC y/o TRANSFORMATION_EVENT | Separar definición de evento de ejecución |
| N11 Aplicación F2 | TRANSFORMATION_SPEC y/o TRANSFORMATION_EVENT | Separar definición y ejecución |
| N12 Estado destino | DATA_STATE_SNAPSHOT | Identidad, versión y tiempo |
| N13 Exportador A1 | SOFTWARE_COMPONENT y/o TRANSFORMATION_SPEC/EVENT | Distinguir capacidad, implementación y ejecución |
| N14 Formato/artefacto de intercambio | CONFIGURATION_ARTIFACT | Versionar formato y artefacto concreto |
| N15 Importador A2 | SOFTWARE_COMPONENT y/o TRANSFORMATION_SPEC/EVENT | Distinguir capacidad, implementación y ejecución |
| N16 Oráculo/criterio F* | MEASUREMENT_ORACLE | Separar definición, implementación y adjudicación |
| N17 Autorizaciones C_auth | AUTHORIZATION_POLICY | Separar política, principal, permiso efectivo y evento |
| N18 Recursos/capacidad compartida | RESOURCE_CAPACITY | Distinguir capacidad instalada, pool, reserva y consumo |
| N19 Configuración fuente/destino | DATA_STATE_SNAPSHOT o CONFIGURATION_ARTIFACT | Según sea estado observado o artefacto declarativo |
| N20 Dependencias/API/servicios compartidos | EXTERNAL_SERVICE, INTERFACE_ENDPOINT, LIBRARY_DEPENDENCY o SOFTWARE_COMPONENT | Un registro por identidad/contrato/versión material |
| N21 Servicios externos | EXTERNAL_SERVICE | Opacidad mantiene estado ? |
| N22 Información/conocimiento agente | INFORMATION_ASSET o ANALYTIC_CONSTRUCT | Separar información disponible, conocimiento y selección |
| N23 Ejecución/Outcome/Value | TRANSFORMATION_EVENT y OUTCOME_VALUE_RECORD | No usar un único registro compuesto cuando los tiempos/identidades difieren |

El catálogo N01–N23 conserva su versión e IDs. El campo `parent_catalog_id` puede contener varios IDs solo si la implementación formaliza relación 1:N; en la plantilla actual, si solo admite un valor, se crea un NODE por rol semántico y se conserva una referencia primaria, dejando el resto de la trazabilidad en los vínculos de catálogo/evidencia. No serializar listas en una celda.

## 4. Nodo raíz lógico y SNAPSHOT

Se conserva sin modificación conceptual DEC-C10-059:

`SNAPSHOT.(unit_object_record_id, unit_id) → NODE.(object_record_id, node_id)`

Reglas:
1. El NODE destino debe tener `semantic_role=LOGICAL_SERVICE_UNIT`.
2. `unit_id` es la identidad semántica estable de la unidad lógica.
3. `unit_object_record_id` identifica la revisión exacta del nodo raíz utilizada por el snapshot.
4. Para cada combinación `(unit_id, snapshot_id)` debe resolver exactamente un registro raíz.
5. En un mismo snapshot no puede haber dos NODE raíz activos para la misma unidad y scope.
6. Snapshots distintos pueden referenciar distintas revisiones del mismo `unit_id`; no se reescribe la historia.
7. La FK compuesta debe comprobar tanto existencia como unicidad del par destino y el predicado semantic_role.
8. El nodo raíz es un ancla de identidad analítica, no necesariamente el paquete P0 ni el entorno P1. Su `boundary_class` será `NA` con justificación explícita si no es por sí mismo un objeto/artefacto P0/P1. No asignar DUAL por el mero hecho de representar la unidad lógica.

## 5. Cardinalidad y claves propuestas

- Una unidad lógica tiene exactamente un nodo raíz por snapshot/scope capturado.
- Un nodo raíz puede ser referenciado por múltiples snapshots si representan la misma revisión exacta y el contrato temporal lo permite; si la revisión cambia, se crea nuevo `object_record_id`.
- `node_id` identifica la identidad semántica estable; `object_record_id` identifica la fila versionada.
- La unicidad física de la FK compuesta y la regla de exclusividad por snapshot requieren constraints del formato/motor elegido; aún no están implementadas.

## 6. Límites y pendientes

- No se crean nodos, snapshots, evidencias ni IDs de servicio.
- No se cambia el catálogo EDGE ni se introducen relaciones causales.
- El vocabulario es candidato y requiere aprobación antes de considerarse cerrado.
- La implementación física de enums, FK compuesta y unicidad queda pendiente del gate técnico autorizado.
- La clasificación real de objetos requiere evidencia; no puede derivarse solo de N01–N23.

`AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT`.  
`scientific_execution=false`; `execution_authorized=false`.

 
## 7. Aceptación — DEC-C10-060 (2026-11-05)

El usuario acepta el vocabulario controlado de 16 valores, la separación entre `parent_catalog_id`, `semantic_role` y `boundary_class`, el crosswalk no uno-a-uno N01–N23 y las reglas del nodo raíz lógico. El contrato queda ACCEPTED_DOCUMENTALLY bajo DEC-C10-060. Esta aceptación no equivale a implementación física ni validación del esquema. Se mantienen los límites de §6.


## 8. Addendum DEC-C10-065 — actualización de la FK raíz

La regla conceptual de nodo raíz y semantic_role aceptada por DEC-C10-060 se conserva. La FK física completa, tras DEC-C10-065, es:

`SNAPSHOT(snapshot_id, object_record_id, unit_object_record_id, unit_id) → NODE(snapshot_id, snapshot_object_record_id, object_record_id, node_id)`.

El `object_record_id` de SNAPSHOT debe coincidir con el `snapshot_object_record_id` del NODE raíz. `unit_object_record_id` identifica el registro NODE exacto y `unit_id` comprueba su identidad semántica. El NODE destino mantiene `semantic_role=LOGICAL_SERVICE_UNIT`. La FK compuesta debe ser diferible o disponer de mecanismo transaccional equivalente probado, sin debilitar integridad.

Este addendum es la especificación vigente y complementa el mapping histórico de §4; no altera el vocabulario de 16 roles ni el crosswalk N01–N23. Validación física pendiente.
