# C10-S — Gate 109: crosswalk UE–UA/cluster–U_G–instancia–ruta e interferencia

**Estado:** HISTORICAL RECONSTRUCTION COMPLETED / UNIT ROLES AND NON-EQUIVALENCES RECONCILED / EXPERIMENTAL-TO-U_G MAPPING OPEN / ASSIGNMENT AND EXPOSURE CONTRACT INCOMPLETE / NO SCHEMA CHANGE / NO IMPLEMENTATION / NO EXECUTION / NO FREEZE  
**Fecha:** 2026-11-15  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft  
**Precedencia:** C10-S master §§277–289; plan §§16.199–16.200; DEC-C10-059/065/069; DEC-C10-066/067; Gate 99, Gate 101, Gate 108; DGP Temporal and Role Contract; PE Integrated Technical Specification §5; Test Contract Register §2; U_G logical-root / unit-FK / boundary-class contracts; Identity/Version/Snapshot Matching Contract; O-CONF/F* and V_cont contracts.  
**Alcance:** auditoría documental asistida, no independiente. No inspecciona registros poblados, no valida el harness y no define identificadores físicos nuevos.

---

## 1. Pregunta y dictamen ejecutivo

¿Puede establecerse una correspondencia inequívoca entre la unidad experimental, la unidad de asignación, el clúster, la unidad lógica U_G, la instancia técnica y la ruta, y determinarse qué estructura de interferencia exige el estimando D2?

**Dictamen:** los contratos ya distinguen los roles principales, pero no fijan el mapping material ni el mecanismo completo de asignación/exposición. No se demuestra UE=UA=U_G, ni que una instancia CMP sea una UE, ni que route_id sea una unidad. La estructura de interferencia debe declararse antes de identificar ITT individual; la aleatorización por clúster no elimina por sí sola la interferencia intraclúster.

**Resultado:** GATE_109_ROLE_CROSSWALK_RECONCILED / UE_TO_UA_CLUSTER_OPEN / UE_TO_UG_MAPPING_OPEN / INSTANCE_AND_ROUTE_CARDINALITY_OPEN / EXPOSURE_MAPPING_NOT_SPECIFIED / NO_NEW_KEYS / NO_SCHEMA_CHANGE / NO_IMPLEMENTATION / NO_EXECUTION / NO_FREEZE.

## 2. Reconstrucción histórica y fuentes

| Fuente | Recuperado | Límite |
|---|---|---|
| Gate 99 | `unit_id = NODE.node_id` para raíz LOGICAL_SERVICE_UNIT; `unit_object_record_id = NODE.object_record_id`; UE→U_G abierto; cluster no resuelto | Identidad U_G no identifica UE/UA |
| Gate 101 | DGP y PE spec prevén UE/UA/UO; Test Contract Register contiene `unit_id / assignment_unit`; no PK física de UA ni clave cluster confirmada | Roles previstos, no materialización |
| Gate 108 | UE es unidad de potenciales/resultados; UA/cluster puede diferir; UO, instancia, ruta y U_G separados | Interferencia/exposición y mapping siguen OPEN |
| Plan §16.199.3 | UE, UA y UO diferenciadas; UE=UA solo con aislamiento completo; recursos/dependencias/pools/agentes/canales compartidos requieren clúster o mapa de exposición (G_i(Z_{-i})) | No establece un mapa concreto ni permite asumir SUTVA |
| Plan §16.200.1 | Asignación como función de UA, estratos, π_h y semilla; sus parámetros permanecen abiertos | No fija RNG, estratos, vector ni claves |
| DEC-C10-059 | Identidad lógica de unidad raíz U_G | No equipara esa unidad con unidad DGP |
| DEC-C10-065 | Pinning exacto snapshot_id + snapshot_object_record_id en los objetos cubiertos | No resuelve la unidad experimental; aceptación arquitectónica no es validación física |
| DEC-C10-069 | CMP focal: contract_id/version, instance_id/version y component_id/class diferenciados | Instancia CMP no es UE, UA, cluster ni U_G unit_id |
| DEC-C10-066/067 | D2 escenario primario candidato; política/artefacto/asignación y etapas materiales diferenciados | No fijan unidad física de asignación ni interferencia |

Los contratos consultados son especificaciones de diseño, varias en estado Draft. La presencia de un campo lógico no acredita que exista una columna implementada, un valor poblado, una FK validada o una observación runtime.

## 3. Crosswalk de roles e identidades

| Rol | Identidad o referencia existente | Función | Estado |
|---|---|---|---|
| UE | Índice (i) del DGP; `unit_id` solo en el ámbito del harness cuando se mapee | Unidad de potenciales y resultados | Semántica definida; mapping físico OPEN |
| UA | `assignment_unit` / rol UA del PE spec | Unidad que recibe Z | Rol previsto; clave y cardinalidad OPEN |
| Cluster | Clave de clúster solo si el diseño la define | Nivel de aleatorización o agrupación de exposición | No establecido |
| UO | Rol UO del PE spec | Unidad a la que corresponde una observación/medición | Mapping a UE/instancia/ventana OPEN |
| Unidad lógica U_G | `unit_id = NODE.node_id`, semantic_role LOGICAL_SERVICE_UNIT | Identidad estable de la unidad lógica raíz | Definida documentalmente |
| Revisión U_G | `unit_object_record_id = NODE.object_record_id` + object_version | Revisión exacta del objeto lógico | Definida; validación física OPEN |
| Instancia CMP | `instance_id + instance_version` conforme DEC-C10-069 | Instancia de configuración/servicio | Identidad aceptada; mapping UE OPEN |
| Instancia/aplicación técnica | EID si satisface su contrato TID/SID/RID/EID | Aplicación concreta de una transformación | No confundir con CMP instance_id |
| Ruta | `route_id` versionada bajo contrato de rutas | Camino funcional/transformacional evaluado | No es unidad ni asignación |
| Snapshot | `snapshot_id + snapshot_object_record_id` | Captura estructural exacta, con pinning DEC-C10-065 | No sustituye identidad de UE |

### 3.1 No equivalencias

No están justificadas las igualdades:

- UE = UA.
- UE = cluster.
- UE = U_G unit_id.
- UA = cluster (salvo que el diseño asigne exactamente por clúster).
- U_G unit_id = instance_id.
- CMP instance_id = EID.
- UO = UE.
- route_id = unidad experimental, unidad de asignación o instancia.
- object_record_id = identidad de unidad experimental o asignación.

Un mismo NODE lógico puede tener revisiones, snapshots, instancias y ejecuciones distintas. Una UE puede requerir varios objetos U_G para representar el servicio y su entorno; una unidad lógica puede aparecer en varias UE/escenarios/runs. Las cardinalidades concretas no se pueden deducir de los nombres.

## 4. Cardinalidades que deben permanecer explícitas

| Relación | Cardinalidad admisible conceptualmente | Estado |
|---|---|---|
| UE → UA | N:1 si varias UE comparten una unidad de asignación/clúster; 1:1 si cada UE se asigna individualmente | OPEN por escenario |
| UA → cluster | 1:1 si UA es el clúster; no aplica si UA individual | OPEN |
| UE → U_G unit | 1:1 solo si la unidad lógica raíz coincide materialmente; 1:N si el sistema de la UE contiene varias unidades lógicas | OPEN |
| U_G unit → UE | Puede ser 1:N a través de escenarios/tiempos si el objeto lógico se reutiliza; no asumir unicidad global | OPEN |
| UE → CMP instance | 1:1, 1:N o N:1 según replicación/instanciación del servicio | OPEN |
| UE → route_id | 1:N cuando se evalúan rutas alternativas; no implica ejecución de todas | Requisito de análisis, roster concreto OPEN |
| UE → UO | 1:N por mediciones, ventanas, fuentes o episodios | OPEN |
| UE × intervalo k → V_cont | K intervalos iguales por UE, según DEC-C10-100/102 | Regla conceptual aceptada; K/ventana/medición OPEN |
| instance × route_id → O-CONF | Unidad de adjudicación terminal según contrato F*/O-CONF | Semántica documental; mapping a UE/agregación OPEN |

No se elige una cardinalidad física hasta recuperar el roster del DGP y el contrato de instanciación por escenario. No se crean tablas de mapping ni claves nuevas por conveniencia.

## 5. Aleatorización: lo que está definido y lo que falta

**Recuperado:**
- (Z_i in {0,1}) como valor de brazo.
- Aleatorización y probabilidad de asignación en t0 como intención del diseño.
- UE y UA son roles distintos.
- `assignment_unit` es vocabulario del Test Contract Register.
- La función estructural del plan §16.200.1 es (Z sim Assign(UA, strata, π_h, seed)).
- (W_{programmed,i}(z)=z) es la regla de programación D2; no implica intento, recepción, instalación ni accesibilidad.
- Semilla/estado del Generator debe permanecer fuera del Analyzer; el Evaluator puede disponer de la procedencia autorizada tras el sellado.

**No recuperado como contrato confirmatorio completo:**
- Algoritmo RNG y versión.
- Unidad exacta sobre la que se genera cada asignación.
- Clave/definición de UA y cluster.
- Estratos/bloques y sus reglas.
- π_h y soporte por unidad/estrato.
- Derivación y alcance de semilla por experimento/run/réplica/bloque.
- Vector de asignación inmutable, identidad/hash y vínculo unidad→Z.
- Reglas para duplicados, reasignación, fallo del mecanismo, contaminación y desviación.
- Identidad persistente de la ocurrencia observada Z_ASSIGNED, sin confundirla con el vector/mecanismo.

`test_id/version`, `fixture_id/hash`, `run_id`, `scenario_id`, semilla, hash del entorno, `unit_id` y `assignment_unit` tienen ámbitos distintos. Ninguno debe convertirse en PK de asignación por analogía. `assignment_id` no se confirma como PK canónica por Gate 99/101.

## 6. Interferencia y exposición

### 6.1 Condición para inferencia individual

No se presume SUTVA ni ausencia de interferencia. Si los recursos, dependencias, pools, agentes, canales, servicios compartidos o cambios de entorno permiten que (Z_j) afecte al resultado de (i), los potenciales deben admitir exposición a asignaciones ajenas:

[
Y_i(z_i, e_i), qquad e_i = G_i(Z_{-i}, mathcal{G}, 	ext{recursos/relaciones compartidas})
]

La expresión es un requisito de representación, no un mapa de exposición aprobado. (G_i), la red (mathcal{G}), el soporte de exposición y las interferencias relevantes permanecen OPEN.

### 6.2 Alternativas de diseño que no deben confundirse

1. **Asignación individual con aislamiento completo:** UA=UE podría ser admisible solo si la independencia/aislamiento está justificada por construcción y evidencia del diseño. No está demostrado.
2. **Asignación por clúster:** UA=cluster y varias UE reciben el mismo brazo si así lo establece el mecanismo. La asignación por clúster no elimina automáticamente interferencia dentro del clúster; debe definirse si esta es parte del tratamiento/exposición o si se necesita una hipótesis adicional.
3. **Asignación individual con interferencia modelada:** puede conservar UA=UE, pero requiere un mapa (G_i(Z_{-i})), soporte suficiente y estimando compatible. No está especificado.
4. **Interferencia no mapeada:** no declarar ITT individual identificado bajo SUTVA. Mantener el estimando como no identificado/indeterminado o reformularlo a nivel compatible solo mediante decisión explícita y soporte suficiente.

No seleccionar una de estas alternativas en este gate.

### 6.3 Estimandos y ponderación

- El ITT D2 es el efecto total de asignar la política/paquete por resultado, no el efecto aislado de accesibilidad.
- Si UA es cluster, deben distinguirse el estimando promedio por UE y el promedio por cluster; no son intercambiables cuando los tamaños de clúster difieren.
- La inferencia debe respetar el nivel de aleatorización y la dependencia inducida por el diseño; N bruto de UE no sustituye el número efectivo de unidades/clústeres independientes.
- La exposición a otras asignaciones puede requerir potenciales (Y_i(z_i,e_i)), probabilidades de exposición y soporte por categoría. No se derivan a partir de una etiqueta de clúster.
- La ponderación, población objetivo, unidad de inferencia y reglas de agregación permanecen OPEN.

## 7. Relación con los resultados y constructos C10-S

| Constructo | Unidad/granularidad vigente | Relación necesaria | Gap |
|---|---|---|---|
| ITT-Z D2 | UE como unidad de potenciales/resultados; asignación a UA/cluster | Mapping UE→UA y exposición/interferencia; política B versionada | Mecanismo/vector y unidad de aleatorización OPEN |
| W_programmed / W_attempt / receipt / S_install | UE × etapa; intento/recepción/instalación por episodio cuando haya multiplicidad | Enlace a Z asignada y versión B, conservando desviaciones | Claves físicas y cardinalidad OPEN |
| C_dep* / A_f* / D_f* | UE × dependencia/transformación × frontera/versión; basal/post | Mapping UE→U_G, NODE exacto y snapshots comparables | UE→U_G y snapshots materiales OPEN |
| T_acc*/ΔT_acc* | UE × frontera/versiones × snapshots pre/post | Grafo estructural y diff exacto, sin confundir ΔE_T | Identidad y cobertura material OPEN |
| Reach/Π_H | UE × estado inicial × objetivo × H; route_id | Roster de rutas y reglas versionadas | Rutas materiales/exhaustividad OPEN |
| O-CONF | instance × route_id, terminal F* | Mapping instance→UE y regla de agregación si hay varias instancias/rutas | Mapping y agregación OPEN |
| V_cont | UE × K intervalos iguales | Transiciones internas truth; S3 observado con cobertura/clock; no promediar por instancia sin regla | K/ventana/canal y agregación OPEN |
| UO/S3 | Fuente × captura/ventana × variable | Vincular observaciones a UE y a objeto/instancia exactos | Crosswalk UO→UE/instancia OPEN |

No se agregan O-CONF por UE ni se replica V_cont por instancia sin una regla explícita. El resultado terminal por instancia×ruta y el Value temporal por UE permanecen constructos distintos.

## 8. Matriz de resolución y gaps

| ID | Requisito | Resultado Gate 109 |
|---|---|---|
| G109-01 | Definición y PK de UE | Rol abstracto (i) identificado; clave física OPEN |
| G109-02 | Definición y PK de UA | Rol `assignment_unit` previsto; clave/semántica OPEN |
| G109-03 | Unidad de aleatorización/cluster | No establecida |
| G109-04 | UE→UA/cluster | Mapping y cardinalidad OPEN |
| G109-05 | UE→U_G unit_id/object_record_id | No demostrado; cardinalidad OPEN |
| G109-06 | U_G unit→instancia CMP/EID | Crosswalk y cardinalidad OPEN |
| G109-07 | UE→UO/S3 | Mapping de observación OPEN |
| G109-08 | UE→route_id / instance×route | Roster y agregación OPEN |
| G109-09 | RNG/seed/strata/π_h | Contrato incompleto |
| G109-10 | Vector Z y provenance | Identidad/hash/mapping no recuperados |
| G109-11 | Interferencia/exposure mapping | (G_i(Z_{-i})) no especificado |
| G109-12 | Unidad de inferencia y ponderación | OPEN; cluster-level no equivale a UE-level |
| G109-13 | Soporte de exposiciones y positividad | OPEN |
| G109-14 | Integridad y firewall Generator/Analyzer/Evaluator | Requisito conceptual recuperado; validación no ejecutada |

## 9. Disposiciones y límites

1. No equiparar UE, UA, cluster, UO, U_G unit_id, instance_id, EID ni route_id.
2. No inventar `assignment_id`, `cluster_id`, `unit_id`, claves puente, tablas o FKs.
3. No usar `object_record_id` como PK de UE/UA; respetar DEC-C10-065 para snapshots.
4. No declarar SUTVA, no interferencia ni aislamiento sin justificación material.
5. No asumir que asignar por clúster resuelve interferencia intraclúster.
6. No cambiar DEC-C10-059/065/066/067/069 ni DEC-C10-061/070.
7. No modificar C0, no crear PROCESS_EVENT ni tocar Gate 98.
8. No inferir unidad/ponderación para O-CONF o V_cont por conveniencia.
9. No crear nuevos escenarios, tests, fixtures, DDL, parser, validadores ni código.
10. No ejecutar validadores locales, workflows, simulaciones ni experimentos en esta operación.

**Limitación:** el análisis es documental y asistido. No se inspeccionaron datos poblados, código/harness, registros de asignación, fixtures serializados ni telemetría. Por tanto, las conclusiones describen contratos recuperados y gaps; no demuestran implementación, asignación real, aislamiento, interferencia empírica ni validez estadística.

**Autorización:** `scientific_execution=false`; `execution_authorized=false`.

**Dictamen final:** GATE_109_ROLE_CROSSWALK_RECONCILED / NO_UE_UA_UG_EQUIVALENCE_ESTABLISHED / CLUSTERING_AND_EXPOSURE_OPEN / RANDOMIZATION_VECTOR_CONTRACT_OPEN / ITT_UNIT_AND_WEIGHTING_OPEN / O_CONF_AND_V_CONT_AGGREGATION_OPEN / NO_SCHEMA_CHANGE / NO_IMPLEMENTATION / NO_EXECUTION / NO_DESIGN_FREEZE.
