# C10-S — Gate 99: crosswalk canónico de asignación Z, política D2 y unidad

**Estado:** DOCUMENTARY CROSSWALK / SEMANTIC DISTINCTIONS RESOLVED / PHYSICAL IDENTITIES PARTIALLY UNRESOLVED / NO SCHEMA CHANGE / NO IMPLEMENTATION / NO EXECUTION / NO FREEZE  
**Fecha:** 2026-11-15  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft  
**Precedencia:** DEC-C10-066, DEC-C10-067; Gate 91–98; DGP Temporal and Role Contract; U_G semantic-role/logical-root contract; unit FK/boundary contract; DEC-C10-059–065, 069–071.  
**Propósito:** resolver las correspondencias semánticas justificables entre Z, B_g0/B_g1 y la unidad; identificar las claves canónicas que existen y las que siguen sin existir. No crear identidades físicas por analogía.

---

## 1. Dictamen ejecutivo

Gate 99 resuelve la semántica del crosswalk, pero **no encuentra claves físicas canónicas para la asignación Z ni para las políticas materiales B_g0/B_g1** en los contratos consultados. N02 y N03 son identificadores de catálogo/roles conceptuales, no claves primarias ni FKs de U_G.

Resultados:

1. **Z:** la asignación aleatoria y la ocurrencia observada de asignación son conceptos distintos. N02 identifica el rol conceptual «Asignación Z»; no es un `node_id`, `object_record_id`, `event_id` ni `assignment_id` físico. Si se materializa el registro de eventos propuesto por Gate 98, `event_id` identifica la ocurrencia Z y `event_record_id` su revisión observacional. Son identidades lógicas candidatas del registro de eventos, no claves ya implementadas.
2. **B_g0/B_g1:** DEC-C10-067 define dos políticas materiales conceptuales, pero no fija un `policy_id`/`policy_contract_id` ni una `policy_version` canónicos. N03 es un rol del catálogo N01–N23 con correspondencia semántica condicional; no es la identidad de la política. La identidad/versionado de artefactos técnicos tampoco sustituye la identidad/versionado de la política.
3. **Unidad:** U_G sí define una identidad semántica de unidad lógica: `unit_id = NODE.node_id` del nodo raíz `LOGICAL_SERVICE_UNIT`. La revisión exacta es `unit_object_record_id = NODE.object_record_id`, ligada al snapshot mediante DEC-C10-065. Pero no está demostrado que la unidad experimental/de asignación (i) del DGP sea idéntica a esa unidad lógica U_G, ni que la unidad de asignación no sea un clúster. Por tanto, el mapping DGP (i) → U_G `unit_id` queda **OPEN**.
4. **POLICY_BOUND:** no debe generarse como evento separado por defecto. En el caso ordinario en que Z asigna directamente B_gZ, la referencia a la política asignada es un binding tipado de la ocurrencia `Z_ASSIGNED`. Solo habrá un evento independiente si la fuente/DGP demuestra un acto operativo posterior y distinguible de vinculación/recepción, con identidad, tiempo y evidencia propios.
5. No se modifican DEC-C10-061 ni DEC-C10-070. No se crea NODE artificial para Z/B, no se asigna EID por analogía y no se crean IDs físicos o FKs no respaldados.

**Dictamen:** `GATE_99_SEMANTIC_CROSSWALK_PARTIALLY_RESOLVED / N02_N03_ARE_CATALOG_ROLES_NOT_KEYS / Z_ASSIGNMENT_PHYSICAL_KEY_OPEN / B_POLICY_ID_AND_VERSION_OPEN / POLICY_BOUND_NOT_SEPARATE_BY_DEFAULT / U_G_UNIT_IDENTITY_DEFINED_BUT_DGP_UNIT_MAPPING_OPEN / NO_SCHEMA_CHANGE / NO_CODE_CHANGE / NO_EXECUTION / NO_DESIGN_FREEZE`.

## 2. Fuentes históricas y precedencia

| Fuente | Aporte utilizado | Límite |
|---|---|---|
| DEC-C10-066 | D2 es escenario primario candidato; D1 secundario; asignación y política no equivalen a accesibilidad | No define claves físicas Z/B |
| DEC-C10-067 | Semántica material de B_g0/B_g1, secuencia Z→B→W_programmed→W_attempt→S_install→C_dep*→A_f*→D_f* y datos operativos pendientes | No aprueba IDs/versiones físicos de política ni un evento POLICY_BOUND |
| DGP Temporal and Role Contract | Distingue unidad experimental y unidad de asignación; t0 asignación, t1 política ofrecida/recibida; registra versión asignada/recibida | Declara abierta la unidad final y la posible asignación por clúster |
| U_G Semantic Role and Logical Root Contract | N02/N03 y crosswalk N01–N23; unidad lógica raíz y semantic_role | El crosswalk es orientativo, no crea nodos, IDs ni FKs |
| U_G Logical Unit FK and Boundary Class Contract | `unit_id` semántico y `unit_object_record_id` exacto | No identifica la unidad experimental DGP |
| DEC-C10-069 | Identidad/versionado CMP del servicio sintético | No es la identidad de la asignación ni de B_gZ |
| Gate 91–93 | Diferencia Z, G, B y etapas materiales; crosswalk previo de etapas y reutilización U_G | N02/N03 no quedaron resueltos como claves |
| Gate 95–98 | Opción B recomendada pero no aceptada; contrato lógico sucesor y bindings tipados | No implementable ni congelado; Gate 98 remite expresamente a este Gate 99 |

La autoridad material de las políticas es DEC-C10-067. Los contratos DGP/U_G son borradores de diseño que deben leerse subordinados a las decisiones aceptadas. Ninguna propuesta de mapping de estos contratos transforma un rol de catálogo en identidad física.

## 3. Crosswalk de identidades

| Concepto | Identidad/clave disponible | Semántica y uso permitido | Estado |
|---|---|---|---|
| Brazo/valor aleatorio Z_i | Valor (Z_i\in\{0,1\}) y mecanismo/semilla/provenance del diseño de asignación | Indica brazo asignado; no identifica por sí solo una ocurrencia única ni la política recibida | Semántica definida; identidad de asignación individual no cerrada |
| N02 — Asignación Z | ID de catálogo N02 | Etiqueta conceptual del rol; no PK/FK, no NODE y no event_id | Confirmado como no-clave |
| Ocurrencia observada Z_ASSIGNED | `event_id` candidato de Gate 98 | Identidad estable de la ocurrencia observada; `event_record_id` identifica revisión exacta | Contrato lógico propuesto; no implementado |
| Registro/revisión de ocurrencia Z | `event_record_id`, `event_revision` candidatos | Append-only; no hereda DEC-C10-062 | Propuesto; reglas físicas pendientes |
| Política material asignada | B_g0^D2 o B_g1^D2 según DEC-C10-067, referenciada desde Z | Definición de política asignada; no confundir con ejecución, recepción ni éxito | Semántica aceptada; ID/versionado canónico OPEN |
| N03 — Política/proceso B | ID de catálogo N03 | Rol conceptual polivalente; puede mapear a AUTHORIZATION_POLICY solo si es política de autorización, TRANSFORMATION_SPEC si es definición de procedimiento, o TRANSFORMATION_EVENT si es una ocurrencia | No es clave; clasificación por objeto/acto pendiente |
| Versión de política asignada/recibida | No hay clave canónica aprobada | Debe distinguirse versión de política, versión del artefacto, versión de instancia CMP y versión recibida | OPEN |
| Artefacto focal | Identidad/versionado de artefacto bajo el crosswalk N04–N07, si corresponde | Artefacto/paquete técnico no es la política B ni su ID | Mapping concreto OPEN |
| Unidad lógica U_G | `unit_id = NODE.node_id` con `semantic_role=LOGICAL_SERVICE_UNIT` | Identidad semántica estable de la unidad estructural | Definido documentalmente |
| Revisión de unidad U_G | `unit_object_record_id = NODE.object_record_id` | Revisión exacta del nodo raíz; SNAPSHOT la fija con la FK compuesta DEC-C10-065 | Definido documentalmente; validación física pendiente |
| Unidad experimental/asignación DGP | Índice abstracto (i) en el contrato DGP | Unidad sobre la que se definen potenciales y Z; unidad de asignación puede diferir de unidad experimental | OPEN |
| Unidad/cluster del harness | Campos existentes como `unit_id` y `cluster_id` en el harness | No prueban por sí solos la equivalencia con U_G `unit_id` ni resuelven la unidad final de asignación | Mapping OPEN |

### 3.1 Claves que NO deben reutilizarse

- N02 y N03 no son claves de fila.
- `node_id` no debe asignarse a Z ni a B para aprovechar el catálogo de NODE.
- `object_record_id` no puede inventarse para Z/B ni tomarse de una revisión de artefacto.
- `EID` solo identifica una instancia concreta de transformación si satisface su contrato; asignación Z y definición B no son transformaciones por defecto.
- `assignment_id` aparece en el ledger de celdas/diseño como referencia al mecanismo/estratos de asignación; no se ha identificado como PK física canónica de U_G ni como sustituto de `event_id`.
- `instance_id`/`instance_version` de DEC-C10-069 identifican la instancia CMP de servicio, no la unidad experimental, la asignación Z ni la política B.

## 4. Resolución semántica de Z_ASSIGNED frente a POLICY_BOUND

### 4.1 Acto de asignación

La asignación aleatoria Z es el acto que determina el brazo. Bajo D2, ese brazo determina qué política conceptual B_gZ se asigna. La relación de diseño es:

[
Z_i \mapsto B_{gZ_i}^{D2}
]

La ocurrencia `Z_ASSIGNED` registra que la asignación se produjo. El binding de la política asignada es una referencia tipada asociada a esa ocurrencia, no una segunda ocurrencia creada por el mero hecho de que la política tenga identidad conceptual.

### 4.2 Cuándo NO existe POLICY_BOUND separado

No se registra un evento `POLICY_BOUND` adicional cuando:

- la política B_gZ queda determinada directamente por el resultado de Z según DEC-C10-067;
- no existe un acto posterior, autónomo y observable de vinculación;
- la única diferencia es que la fila Z_ASSIGNED contiene una referencia a B_gZ;
- el evento duplicaría la misma asignación bajo otro nombre.

En ese caso, `POLICY_BOUND` sería una duplicación semántica. La política asignada se representa como binding tipado de `Z_ASSIGNED`, condicionado a que el contrato posterior identifique la clave canónica de B.

### 4.3 Cuándo podría existir POLICY_BOUND separado

Solo se admite como candidato si se identifica un acto independiente, por ejemplo una vinculación/entrega posterior de una versión de política a una unidad, que tenga:

1. identidad propia de ocurrencia;
2. actor/proceso emisor identificable;
3. tiempo de ocurrencia propio, distinto de `recorded_at`;
4. referencia a la unidad exacta;
5. referencia a la política/versión efectivamente vinculada o recibida;
6. evidencia/provenance separable;
7. posibilidad real de desviación entre política asignada y política recibida.

La existencia de una política definida o de un campo de versión no demuestra por sí sola ese acto. Si la política recibida difiere de la asignada, debe registrarse la desviación/recepción conforme al crosswalk futuro; no reescribir Z ni la política asignada.

**Disposición:** `POLICY_BOUND = NOT_A_SEPARATE_EVENT_BY_DEFAULT / CONDITIONAL_ON_DISTINCT_OBSERVABLE_BINDING_ACT`. No se elimina del catálogo candidato de Gate 98 ni se amplía su enum en este gate.

## 5. Crosswalk temporal y causal mínimo

| Etapa | Identidad/registro | Regla |
|---|---|---|
| t0 — asignación Z | Ocurrencia Z_ASSIGNED, event_id candidato | Registra el acto de asignación; no prueba recepción ni intento |
| B_gZ asignada | Binding tipado desde Z_ASSIGNED a definición/version de política | La clave de política sigue OPEN; no inventar NODE |
| t1 — política ofrecida/recibida | Solo evento separado si la fuente identifica acto autónomo; versión asignada y recibida diferenciadas | No colapsar asignación y recepción |
| W_programmed | Ocurrencia procedimental si la programación individual es observable | No inferir desde Z cuando la fuente no registra el acto; DEC-C10-067 define política de programación |
| W_attempt | Ocurrencia de intento efectivo | EID solo si el acto es realmente aplicación de transformación bajo contrato; no por defecto |
| ARTIFACT_RECEIVED | Ocurrencia de recepción, con destino/artefacto versionado | No demuestra instalación |
| S_install | Inicio/terminación de instalación si existe acto observable | No implica C_dep* verificado |
| C_dep* | Constructo/predicados técnicos verificados, no política ni evento de asignación | Evidencia en U_G/PREDICATE/EVIDENCE_REGISTER según contrato aplicable |

Los ejes t0/t1 del DGP, `event_time`, `scheduled_time`, `recorded_at`, `observed_at`, `stage_key` y `SNAPSHOT.phase` siguen separados. DEC-C10-071 no autoriza derivar stage_key de t0/t1 ni de SNAPSHOT.phase.

## 6. Mapping de unidad: decisión parcial y bloqueo restante

La identidad estructural U_G está definida:

`SNAPSHOT.unit_id` identifica la unidad lógica y coincide con `NODE.node_id` del nodo raíz `LOGICAL_SERVICE_UNIT`; `SNAPSHOT.unit_object_record_id` resuelve la revisión exacta de NODE. Tras DEC-C10-065, la integridad requiere la referencia compuesta exacta del snapshot.

Sin embargo, el contrato DGP declara expresamente que la unidad experimental y la unidad de asignación deben declararse por separado y que la asignación por clúster/interferencia puede exigir ampliar la indexación. Por tanto, no se puede concluir que:

[
i = unit\_id = cluster\_id
]

El mapping solo podrá cerrarse cuando el contrato de población/asignación/interferencia establezca si cada unidad experimental corresponde a una unidad lógica U_G, si varias unidades comparten clúster de asignación y qué entidad recibe Z. Hasta entonces:

- `unit_id` U_G es la identidad estructural de servicio, no una autorización para asumir que es la unidad de aleatorización.
- `unit_object_record_id` es revisión estructural, no ID de asignación.
- `cluster_id` no se convierte en unidad raíz ni en NODE sin crosswalk explícito.
- El binding de evento a NODE LOGICAL_SERVICE_UNIT exige una correspondencia DGP→U_G exacta y versionada; coincidencia textual no basta.

## 7. Bloqueos y acciones siguientes

| ID | Bloqueo | Cierre requerido |
|---|---|---|
| G99-01 | No existe PK física canónica para asignación individual Z | Definir si el registro de eventos Gate 98 será su registro observacional; mantener aparte el identificador/mecanismo de asignación del diseño |
| G99-02 | B_g0/B_g1 carecen de policy_id/version canónicos | Resolver identidad contractual de política y versionado, separada de artefacto y CMP |
| G99-03 | N02/N03 son roles de catálogo, no claves | Mantenerlos como referencias de catálogo; no usarlos como FK |
| G99-04 | Unidad experimental DGP no mapeada a U_G | Resolver unidad experimental, unidad de asignación y cluster/interferencia; después mapear a unit_id y object_record_id exactos |
| G99-05 | POLICY_BOUND no tiene criterio de ocurrencia autónoma demostrado | Mantenerlo no-separado por defecto; exigir evidencia de acto independiente para materializarlo |
| G99-06 | Política asignada vs política recibida/versiones | Definir cómo registrar desviación/crossover sin alterar Z ni sobrescribir B asignada |
| G99-07 | Binding tipado a B no tiene target físico aceptado | Determinar referencia contractual externa tipada o target existente; no crear NODE artificial |
| G99-08 | N02→TRANSFORMATION_EVENT entra en tensión con la semántica de Z | No aplicar ese crosswalk físico a Z; mantener N02 como etiqueta conceptual hasta decisión explícita |

## 8. Recomendación de continuidad

No crear aún una decisión normativa ni una enmienda de esquema. El mínimo siguiente es una auditoría de identidad/versionado del objeto política B y del registro de asignación, limitada a los contratos ya existentes, y una reconciliación de unidad experimental/asignación/cluster con el crosswalk U_G. La necesidad de un target contractual externo para B solo debe plantearse después de recuperar las claves reales del DGP y de U_G.

No se cambian DEC-C10-061, DEC-C10-067 ni DEC-C10-070. No se acepta la Opción B, no se congela el contrato lógico y no se implementa.

**Control:** `scientific_execution=false`; `execution_authorized=false`; no se ejecutaron tests, validadores, workflows, simulaciones ni experimentos. Auditoría documental asistida, no independiente.
