# C10-S — Gate 101: auditoría de identidad del artefacto focal y del mecanismo de asignación Z

**Estado:** DOCUMENTARY HISTORICAL AUDIT / EXISTING LOGICAL IDENTITIES RECOVERED / PHYSICAL CROSSWALKS OPEN / NO SCHEMA CHANGE / NO IMPLEMENTATION / NO EXECUTION / NO FREEZE  
**Fecha:** 2026-11-15  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft  
**Precedencia:** DEC-C10-066/067; Gate 98–100; DGP Temporal and Role Contract; PE Integrated Technical Specification; Identity/Version/Snapshot Matching Contract; Test Contract Register; U_G Evidence/Provenance Protocol; DEC-C10-068/069/076/079–081.  
**Objetivo:** recuperar identidades ya previstas para el artefacto focal y la asignación Z antes de proponer nuevas claves. No definir DDL ni completar por inferencia valores ausentes.

---

## 1. Dictamen ejecutivo

Gate 101 recupera una parte importante de la estructura de identidad que Gate 100 había dejado demasiado abierta:

1. **Artefacto focal:** el contrato de identidad TID/SID/RID/EID ya distingue especificación semántica (TID), versión de especificación (SID), realización técnica/artefacto concreto (RID) e instancia/ocurrencia de aplicación (EID). Para el artefacto técnico usado por B_g1, **RID es el candidato de crosswalk existente más próximo**, acompañado por la versión/build/hash de la realización y su registro exacto según el contrato aplicable. Sin embargo, no se ha demostrado que el artefacto mencionado por DEC-C10-067 sea exactamente el RID de una transformación focal τ2, ni se ha localizado el RID concreto ni su registro/versionado. Por tanto, no se puede cerrar el mapping físico todavía.
2. **Fixture y escenario:** el Test Contract Register ya prevé `fixture_id/fixture_hash`, `test_id/version`, `scenario identity`, `run identity`, y reproducibilidad mediante semilla, versiones, configuración y hash del entorno. Son identidades del experimento/fixture/run, no del artefacto focal ni de la asignación individual Z.
3. **Unidad y asignación:** el DGP y la especificación técnica ya prevén `unit_id`, UE/UA/UO, Z, brazo/política y versión, con unidad experimental y unidad de asignación separadas. El Test Contract Register expresa `unit_id / assignment_unit`. Esto demuestra que el contrato lógico conoce ambos papeles; no aporta una PK física canónica para la asignación ni resuelve aún si UA es unidad individual o clúster.
4. **Mecanismo/vector de aleatorización:** el DGP solo indica aleatorización conforme al diseño y conservación de ITT; no se localiza en los contratos consultados un esquema concreto para RNG/algoritmo, semilla por run/replicación, vector de asignación, estratos/bloques, hash del vector, o `assignment_id` como PK. La semilla/estado generador es entrada del Generator y está reservada frente al Analyzer; eso es un requisito de separación de roles, no una especificación de mecanismo reproducible completa.
5. **B y artefacto no son el mismo objeto:** B_g1 define la política que programa el intento; RID, si corresponde, identifica la realización técnica/artefacto utilizado por esa política. CMP `instance_id/version` y fixture/run identity siguen siendo distintos.

**Dictamen:** `GATE_101_EXISTING_IDENTITY_VOCABULARY_RECOVERED / RID_IS_CANDIDATE_NOT_CONFIRMED_FOCAL_ARTIFACT_MAPPING / FIXTURE_AND_RUN_IDS_NOT_ASSIGNMENT_IDS / UE_UA_ROLES_EXIST_BUT_UA_KEY_AND_CLUSTER_OPEN / RANDOMIZATION_MECHANISM_VECTOR_PROVENANCE_OPEN / NO_SCHEMA_CHANGE / NO_IMPLEMENTATION / NO_EXECUTION / NO_FREEZE`.

## 2. Fuentes recuperadas y alcance

| Fuente | Elemento recuperado | Límite |
|---|---|---|
| DEC-C10-067 | B_g1 debe usar artefacto y versión identificados antes de asignación; registrar actor, inicio, recepción, finalización, versión recibida y desviaciones | No proporciona identidad, versión ni hash concretos del artefacto |
| DGP Temporal and Role Contract §§2–3 | Unidad experimental y unidad de asignación separadas; t0 Z/probabilidad; t1 B_i/version_B; Z_i asigna B_i; ITT preservado | No define RNG, seed, vector, PK de asignación ni clave de cluster |
| PE Integrated Technical Specification §5 | test_id/version, fixture_id/hash, run identity, scenario identity; unit_id, UE/UA/UO, Z, brazo/política y versión | Categorías lógicas previstas; no autoriza nuevas columnas ni prueba que existan valores físicos |
| Test Contract Register §2 | test_id/version, fixture_id/fixture_hash, unit_id/assignment_unit, intervención Z/B/version, hidden_truth, reproducibility con semilla, versiones, configuración y hash de entorno | Contrato de test, no ledger de asignación por unidad ni especificación del algoritmo aleatorio |
| Identity/Version/Snapshot Matching Contract §2 | TID, SID, RID y EID separados; RID = implementación/módulo/dependencia que realiza la especificación, artefacto/software/configuración concreta | Contrato Draft; no identifica el artefacto de DEC-C10-067 por sí solo |
| U_G Inventory Register Template | NODE versionado registra TID/SID/RID, version/build/hash y owner/dependencies/evidence; SNAPSHOT fija unidad y revisión exacta | No crear NODE para la asignación Z ni asumir que el artefacto debe ser NODE sin crosswalk |
| U_G Evidence/Provenance Protocol | evidencia con origen/custodio/método/versión/hash; manifiesto versionado y resolución tipada exacta; semilla secreta no visible al Analyzer según PE spec | Protocolo de evidencia no sustituye contrato de aleatorización |
| DEC-C10-069 | instance_id + instance_version para instancia CMP | No es RID, identidad de artefacto, Z ni fixture/run |

La reconstrucción aplica la regla histórica de reutilización: no crear un nuevo registro si un contrato compatible ya existe. Las búsquedas y recuperaciones se limitaron a los contratos y rutas identificados en la tabla; la ausencia de una clave en ellos no demuestra inexistencia en cualquier artefacto no consultado.

## 3. Crosswalk del artefacto focal

### 3.1 Jerarquía ya definida

| Nivel | Identidad existente | Función | Relación con DEC-C10-067 |
|---|---|---|---|
| Transformación semántica | TID | Identidad de la transformación/contrato esencial | Podría identificar τ2 si el procedimiento de provisión se corresponde con una transformación; no asumirlo |
| Especificación | SID | Revisión versionada del contrato de TID | Puede fijar la especificación técnica aplicable |
| Realización | RID | Implementación, módulo, dependencia, artefacto/software/configuración concreta | Candidato más próximo al artefacto técnico focal |
| Instancia/aplicación | EID | Aplicación o intento concreto sobre unidad/tiempo | No identifica el paquete/artefacto preasignación ni la política B |
| Integridad del registro | object_record_id / object_version y evidencia/hash aplicables | Registro inmutable/revisión y procedencia | No confundir con identidad semántica RID |

La identidad de artefacto no debe comprimirse en un único campo `artifact_id` si el contrato aplicable distingue RID, versión/build, hash, registro y procedencia. Un hash diferente tampoco prueba por sí solo una nueva identidad semántica.

### 3.2 Hallazgo y limitación

DEC-C10-067 requiere artefacto y versión identificados antes de asignación. El contrato TID/SID/RID/EID proporciona un vocabulario compatible para describir la realización técnica. No obstante, no se ha encontrado evidencia que enlace explícitamente el artefacto de provisión B_g1 a un RID concreto de τ2 ni que declare si el objeto es:
- la dependencia focal;
- un paquete/instalador que la entrega;
- un adaptador o configuración;
- una realización completa de τ2;
- o un conjunto de artefactos con dependencias.

No se selecciona una de estas alternativas por analogía. Tampoco se presume que RID sea obligatorio si el artefacto no es una realización de transformación bajo el contrato TID/SID/RID.

### 3.3 Datos de versión/recepción

Se mantienen separados:
- identidad y revisión del artefacto previsto antes de Z;
- artefacto/versión efectivamente ofrecido;
- artefacto/versión efectivamente recibido;
- registro de recepción y evidencia;
- instalación, integridad, compatibilidad y operatividad verificadas;
- cambios/rollback/reintentos y desviaciones.

DEC-C10-067 exige registrar versión recibida y desviaciones; no prescribe un único campo físico ni un hash específico. No imponer `artifact_hash` como nueva clave o requisito autónomo sin mapping al contrato de artefacto y al protocolo de canonicalización vigente.

## 4. Crosswalk de unidad, asignación y aleatorización

### 4.1 Roles ya previstos

| Rol | Identidad lógica existente | Resultado |
|---|---|---|
| Unidad experimental (UE) | unidad indexada (i) / `unit_id` en el dominio del DGP | Rol previsto; mapping físico a U_G OPEN |
| Unidad de asignación (UA) | `assignment_unit` en Test Contract Register | Rol explícito; clave física/cluster OPEN |
| Unidad de observación (UO) | UO del vocabulario PE spec | Rol previsto; mapping exacto OPEN |
| Unidad lógica U_G | `unit_id = NODE.node_id` y revisión `unit_object_record_id` | Identidad estructural definida en Gate 99 |
| Clúster | unidad superior de asignación/interferencia si procede | No se ha encontrado clave/semántica final aprobada |
| Asignación | (Z_i), brazo/política y versión | Variable/resultado de asignación; no PK de ocurrencia |
| Ocurrencia observada | `Z_ASSIGNED` con `event_id` candidato Gate 98 | Identidad lógica propuesta; no implementada |

El contrato no autoriza la igualdad UE=UA=UO=U_G unit_id. Debe declararse por escenario. Si UA es cluster, el mapping debe representar varias UE dentro de una UA y el estimando/interferencia debe seguir esa unidad de asignación.

### 4.2 Mecanismo de asignación: qué está y qué falta

**Recuperado:**
- aleatorización conforme al diseño;
- probabilidad de asignación en t0;
- conservación de ITT;
- Z_i ∈ {0,1};
- unidad experimental y unidad de asignación diferenciadas;
- escenario/fixture/run y semillas/configuración como parte de reproducibilidad;
- semilla/estado generador restringidos al Generator/Evaluator, no al Analyzer.

**No recuperado como contrato completo:**
- algoritmo RNG y versión;
- fuente/derivación de semilla y alcance (experimento, run, réplica, bloque);
- estratificación, bloques, permutaciones o mecanismo de asignación;
- vector de asignación inmutable y su identidad/hash;
- mapping unidad→Z y registro de reasignaciones/errores;
- PK persistente `assignment_id` y sus reglas de unicidad;
- relación explícita entre vector asignado y ocurrencias Z_ASSIGNED;
- protocolo de cluster/interferencia y clave UA.

Por tanto, `fixture_id/hash`, `test_id/version`, `run identity` y `scenario identity` identifican contexto experimental, no sustituyen una identidad de vector de asignación. La semilla identifica o controla una entrada del mecanismo, no la asignación individual ni la ocurrencia observada.

### 4.3 Reproducibilidad sin fuga

El Generator recibe semillas/estado generador. El Analyzer no recibe semilla secreta ni parámetros que permitan reconstruir truth. Para reconciliar reproducibilidad y cegamiento:
- conservar semilla/estado y algoritmo en el ámbito restringido de generación;
- conservar referencia de procedencia, versión del mecanismo y evidencia de integridad accesible al evaluador autorizado;
- no exponer secreto ni derivaciones reconstructivas al Analyzer;
- sellar el vector de asignación y el bundle observable según contrato autorizado;
- separar hash del vector, hash del fixture, hash del entorno y hash de artefactos.

Esto es una regla de diseño documental, no un diseño criptográfico aprobado ni una especificación de almacenamiento.

## 5. Crosswalk de identidades no intercambiables

| Identidad | Qué identifica | No identifica |
|---|---|---|
| `policy_contract_id + policy_version` | Definición B_g^D2 asignable (Gate 100, valores OPEN) | Artefacto/RID, vector Z, fixture, run |
| TID/SID | Transformación y revisión de especificación | Política B ni intento |
| RID + versión/build/hash + registro exacto | Realización técnica/artefacto si el mapping se confirma | Política B, instancia CMP, asignación |
| EID | Instancia/aplicación de transformación | Artefacto preasignación ni Z |
| `instance_id + instance_version` | Instancia CMP | RID, B, Z, UE/UA |
| `fixture_id + fixture_hash` | Fixture/escenario de prueba | Artefacto focal, vector Z |
| `test_id + version` | Contrato/familia de prueba | Run o asignación individual |
| Run identity / scenario identity | Ejecución y escenario | Unidad experimental o vector de asignación |
| Semilla + algoritmo/versión | Entrada/reproducibilidad del mecanismo | PK de asignación o event_id |
| `unit_id` / UE / UA / UO | Roles de unidad distintos | Equivalencia automática entre ellos |
| `event_id` | Ocurrencia Z_ASSIGNED propuesta | Vector/mecanismo de asignación |

## 6. Disposiciones

1. Reutilizar el vocabulario TID/SID/RID/EID para investigar el artefacto focal; **RID queda como candidato, no como mapping confirmado**.
2. Reutilizar fixture_id/hash, test_id/version, run identity y scenario identity únicamente para sus ámbitos.
3. Reutilizar UE/UA/UO y `unit_id` como roles diferenciados; no inventar `assignment_id` ni `cluster_id`.
4. Mantener `Z_i`, mecanismo/vector de aleatorización y ocurrencia `Z_ASSIGNED` como tres capas.
5. Mantener semilla/estado generador fuera del Analyzer conforme al firewall del PE spec.
6. No crear NODE para política, artefacto o asignación sin mapping semántico/estructural aprobado.
7. No modificar DEC-C10-061, DEC-C10-067 ni DEC-C10-070; no alterar Gate 98/99/100.

## 7. Bloqueos y cierre requerido

| ID | Bloqueo | Cierre documental requerido |
|---|---|---|
| G101-01 | Artefacto DEC-C10-067 no enlazado a RID/TID/SID | Identificar objeto concreto, clase/rol, frontera, unidad de versionado y mapping al catálogo |
| G101-02 | No se conoce si el artefacto es dependencia, instalador, adaptador o conjunto | Recuperar el inventario material/dependencias del DGP y declarar cardinalidad |
| G101-03 | Versión/hash preasignación y versión recibida sin identidad concreta | Resolver contra registro de artefactos y canonicalización existentes; no inventar campos |
| G101-04 | Algoritmo RNG/versión y alcance de semilla no fijados | Recuperar/definir contrato de aleatorización, con separación de secreto y provenance |
| G101-05 | Vector de asignación sin identidad/versionado/registro canónico | Resolver su identidad y relación con test/run/escenario/unidades |
| G101-06 | No hay PK canónica confirmada para asignación individual | No asumir assignment_id; decidir si el vector más índice estable de unidad basta o si existe identidad persistente ya prevista |
| G101-07 | UA/cluster y mapping UE→UA→U_G no cerrados | Resolver población, interferencia y clave de asignación antes de materializar |
| G101-08 | Ocurrencia Z_ASSIGNED propuesta, no implementada | Mantener event_id/event_record_id como propuesta Gate 98, no PK actual |
| G101-09 | Artefacto técnico y política B pueden ser 1:N | Identificar mapping B→RID(s) sin colapsar identidad ni versionado |

## 8. Siguiente operación

**Gate 102 — reconciliación del inventario material de τ2 y del grafo de dependencias del servicio**, usando los contratos U_G/manifest existentes y las decisiones de frontera C10. El objetivo es comprobar si el artefacto de DEC-C10-067 ya aparece como NODE/DEPENDENCY/RID/manifest property y recuperar las relaciones de cardinalidad, owner, versión, unidad y snapshot. En paralelo, preparar el contrato de asignación solo después de localizar el ledger/vector real o confirmar que no existe en el material consultado.

No se propone DDL ni se crean identidades físicas en Gate 101.

**Control:** `scientific_execution=false`; `execution_authorized=false`; sin tests, validadores, workflows, simulaciones ni experimentos. Auditoría documental asistida, no independiente.
