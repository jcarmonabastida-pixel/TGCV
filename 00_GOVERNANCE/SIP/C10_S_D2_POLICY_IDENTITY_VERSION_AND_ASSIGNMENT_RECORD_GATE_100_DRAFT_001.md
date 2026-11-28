# C10-S — Gate 100: identidad/versionado de política D2 y registro de asignación Z

**Estado:** DOCUMENTARY AUDIT / SEMANTIC IDENTITY CONTRACT PARTIALLY RESOLVED / PHYSICAL IDENTIFIERS OPEN / NO SCHEMA CHANGE / NO IMPLEMENTATION / NO EXECUTION / NO FREEZE  
**Fecha:** 2026-11-15  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft  
**Precedencia:** DEC-C10-066/067; Gate 98 successor; Gate 99; DGP Temporal and Role Contract; U_G Semantic Role and Logical Root Contract; DEC-C10-059–071.  
**Alcance:** identidad contractual de B_g0^D2/B_g1^D2, versionado de política frente a artefacto/CMP, relación asignada/ofrecida/recibida y registro de asignación Z. No cierra unidad/clúster ni autoriza materialización.

---

## 1. Dictamen ejecutivo

Gate 100 confirma una separación de cuatro identidades/estados que no deben colapsarse:

1. **Política material B_g^D2:** regla contractual de intervención asignada. No es el artefacto técnico ni la instancia CMP. Su identidad lógica debe ser `policy_contract_id` y su revisión `policy_version`, conforme a la alternativa tipada que Gate 98 ya contempla para POLICY_VERSION cuando B no se represente como NODE.
2. **Artefacto técnico focal:** objeto técnico concreto utilizado por la política, identificado/versionado/hash por su propio contrato. DEC-C10-067 exige que artefacto y versión estén identificados antes de asignación; no proporciona esos valores ni autoriza reutilizar su ID como policy ID.
3. **Instancia CMP:** `instance_id`/`instance_version` y provenance de DEC-C10-069 identifican la instancia del servicio sintético, no la política B, el artefacto ni la asignación individual.
4. **Asignación Z:** valor aleatorizado y mecanismo/provenance de asignación son distintos de la ocurrencia observada `Z_ASSIGNED`. Gate 98 propone `event_id` para la ocurrencia y `event_record_id`/`event_revision` para su revisión observacional; no existe todavía una PK física implementada ni se ha demostrado que `assignment_id` sea PK canónica.

**Resolución:** la forma de identidad contractual de B puede especificarse sin crear NODE: `policy_contract_id + policy_version` como referencia externa tipada. Sin embargo, no se encuentran identificadores concretos aprobados ni un registro autoritativo de esas dos versiones D2. La distinción semántica se cierra; los valores físicos permanecen OPEN.

**Dictamen:** `GATE_100_POLICY_IDENTITY_SEMANTICS_RESOLVED / POLICY_CONTRACT_ID_AND_VERSION_REQUIRED_BUT_VALUES_OPEN / ARTIFACT_IDENTITY_SEPARATE / CMP_INSTANCE_IDENTITY_SEPARATE / ASSIGNED_OFFERED_RECEIVED_DISTINCT / Z_ASSIGNMENT_MECHANISM_SEPARATE_FROM_Z_ASSIGNED_EVENT / NO_SCHEMA_CHANGE / NO_IMPLEMENTATION / NO_EXECUTION / NO_FREEZE`.

## 2. Evidencia documental recuperada

| Fuente | Evidencia | Conclusión / límite |
|---|---|---|
| DEC-C10-067 | B_g0^D2 mantiene basal y no programa provisión focal; B_g1^D2 programa intento focal; usa artefacto y versión identificados antes de asignación; registra actor, inicio, recepción, finalización, versión recibida y desviaciones | Define contenido material y datos exigidos; no asigna policy IDs/versiones concretos |
| DEC-C10-067 §6 | Actor, identidad/versión/hash del artefacto, protocolo de recepción, ventana temporal, reintentos, fallos, rollback, detección de provisión de fondo y evidencia C_dep* siguen pendientes | Confirma que no hay valores ni protocolo operativo cerrados |
| DGP Temporal and Role Contract | t0 Z; t1 política ofrecida/recibida con B_i y version_B; registra versión asignada y recibida; intento distinto de instalación | Versionado y estados distintos, sin PK contractual cerrada |
| Gate 98 §7.1 | binding_role POLICY_VERSION admite target NODE o referencia contractual externa tipada; si B_g0/B_g1 sigue siendo objeto del contrato DGP, usar policy_contract_id + policy_version y declarar autoridad/versión en mapping DGP | Proporciona representación lógica tipada sin NODE artificial; sigue siendo propuesta de contrato lógico |
| Gate 98 §5/6 | Z_ASSIGNED es ocurrencia; POLICY_BOUND solo si acto distinto; event_id/event_record_id/event_revision separados; no asignar EID a Z | La asignación puede tener registro observacional separado del mecanismo/valor |
| DEC-C10-069 | Identidad/versionado de instancia CMP | No es identidad de B ni de artefacto ni de Z |
| Gate 99 | N02/N03 son roles de catálogo, no PK/FK | No usar N02/N03 como identificadores físicos |

## 3. Identidad de política B

### 3.1 Tipo semántico

B_g0^D2 y B_g1^D2 son **definiciones de política/procedimiento de provisión**, no políticas de autorización normativa C_auth. DEC-C10-067 exige mantener C_auth,base=1 común entre brazos y prohíbe que B altere la autorización normativa basal.

Por tanto:
- No clasificar B_g0/B_g1 como `AUTHORIZATION_POLICY` solo por contener la palabra policy.
- No asignarles `semantic_role=TRANSFORMATION_EVENT`: son reglas asignables, no ocurrencias de ejecución.
- `TRANSFORMATION_SPEC` podría describir una especificación de procedimiento técnico, pero solo si el objeto concreto satisface ese rol y se mantiene separado del contrato de asignación B.
- No crear NODE para la abstracción B por comodidad del binding.

La representación primaria preferida para el objeto de asignación B es una referencia contractual externa tipada:
`(policy_contract_id, policy_version)`.

### 3.2 Identidad y versionado exigidos

| Campo lógico | Función | Estado |
|---|---|---|
| `policy_contract_id` | Identidad estable del contrato/definición de política | Obligatorio por diseño de referencia tipada; valor OPEN |
| `policy_version` | Revisión exacta de la definición asignable | Obligatorio; valor OPEN |
| `policy_arm` | Diferencia semántica B_g0^D2 / B_g1^D2 | Dominio conceptual conocido; codificación física OPEN |
| `scenario_id` / referencia D2 | Contexto del régimen de política | D2 aceptado como escenario primario candidato; clave concreta según DGP |
| `policy_authority` | Autoridad/custodio que gobierna identidad y versiones | OPEN |
| `policy_content_hash` | Integridad de contenido/versionado contractual | No exigido como campo canónico por decisión existente; no imponer sin contrato |
| `effective_from/to` | Vigencia temporal de versión, si aplica | OPEN; no inventar |
| `mapping_version` | Versión del mapping DGP que resuelve el target | Requiere declaración al materializar; no tiene valor aprobado |

Los valores B_g0^D2 y B_g1^D2 son nombres de brazo/definición conceptual de DEC-C10-067; no se deben convertir directamente en PK sin declarar namespace, autoridad, unicidad, estabilidad y versionado.

### 3.3 Asignada, ofrecida y recibida

| Estado | Significado | Identidad/versión que debe conservar |
|---|---|---|
| Assigned | Política que corresponde por la asignación Z | `policy_contract_id + policy_version` asignada |
| Offered | Política efectivamente ofrecida/comunicada a unidad/actor | Referencia exacta ofrecida; puede coincidir o diferir de assigned |
| Received | Política/versión cuya recepción por destinatario queda acreditada | Referencia exacta recibida y evidencia de recepción |
| Applied/attempted | Intento operativo iniciado bajo el procedimiento | Ocurrencia PROVISION_ATTEMPT_STARTED; no equivale a received ni éxito |
| Installed/verified | Resultado de instalación y verificación técnica | Eventos y evaluaciones separados; C_dep* no se infiere de B |

No se sobrescribe la política asignada cuando existe crossover, desviación, entrega de versión distinta o recepción parcial. La discrepancia es un dato de cumplimiento/contaminación y debe conservar ambas referencias.

La existencia de una política asignada no prueba que se ofreciera, recibiera, programara, intentara o instalara.

## 4. Identidad de artefacto y separación de CMP

DEC-C10-067 requiere que B_g1 use un artefacto y versión identificados antes de asignación, y que se registre versión recibida y desviaciones. No se encontró el identificador/hash concreto ni el contrato de artefacto que gobierna esos valores.

Se mantienen cuatro referencias no intercambiables:

| Objeto | Identidad lógica | No sustituye |
|---|---|---|
| Política B | `policy_contract_id + policy_version` | Artefacto, CMP, asignación |
| Artefacto técnico | Identidad del artefacto + versión/hash según contrato propio | Política B |
| Instancia CMP | `instance_id + instance_version` de DEC-C10-069 | Política B, artefacto, unidad experimental |
| Unidad lógica U_G | `unit_id + unit_object_record_id` según DEC-C10-059/065 | Unidad experimental/asignación hasta mapping |

La política puede referenciar un artefacto focal concreto como parámetro/dependencia de su definición. La referencia no convierte el artefacto en la política. Si cambia el artefacto entre versiones de política, se requiere un mapping explícito y no se infiere identidad por coincidencia de nombres.

## 5. Registro de asignación Z y relación con B

### 5.1 Dos capas

- **Capa de diseño/asignación:** (Z_i), probabilidad/mecanismo de aleatorización, estrato/cluster, semilla y provenance del vector de asignación. El contrato DGP debe definir las claves y hashes del mecanismo/vector; no se ha confirmado que `assignment_id` sea PK canónica de un registro persistente.
- **Capa de ocurrencia observada:** `Z_ASSIGNED`, con `event_id` estable de ocurrencia y `event_record_id`/`event_revision` de la revisión del registro, conforme a Gate 98. No está implementada y sigue condicionada a aceptación/materialización del contrato de eventos.

La ocurrencia Z_ASSIGNED debe enlazar tipadamente a la política asignada mediante `policy_contract_id + policy_version`, o mediante otro target contractual aprobado si el contrato futuro lo justifica. No enlazar a N03, NODE inventado, artifact ID o CMP instance ID.

### 5.2 Binding frente a POLICY_BOUND

El binding de B asignada es un atributo/referencia tipada de Z_ASSIGNED si no existe un acto distinto. POLICY_BOUND solo será evento autónomo si se acredita una vinculación posterior real, separada de la decisión aleatoria, con actor, instante, destinatario, referencia/versionado y evidencia propios. La recepción posterior se representa por el acto de recepción correspondiente; no se reutiliza POLICY_BOUND para encubrir recepción.

### 5.3 Fallos y ausencia

- Una asignación realizada produce Z_ASSIGNED; un fallo de mecanismo antes de producir asignación no se disfraza como Z_ASSIGNED con resultado FAILED.
- La no programación de B_g0^D2 no crea evento PROVISION_SCHEDULED negativo.
- Provisión de fondo/crossover en control se registra como ocurrencia real y no reescribe Z ni B asignada.
- UNKNOWN no equivale a ausencia, FAILED ni NOT_APPLICABLE.
- No se genera una ocurrencia solo porque exista una regla probabilística o definición de política.

## 6. Crosswalk consolidado

| Concepto | Referencia lógica correcta | Estado |
|---|---|---|
| N03 | Etiqueta de catálogo, no FK | Confirmado |
| B_g0^D2 / B_g1^D2 | Política contractual D2 | Semántica definida por DEC-C10-067 |
| Identidad B | `policy_contract_id` | Campo requerido por alternativa Gate 98; valor OPEN |
| Versión B | `policy_version` | Campo requerido; valor OPEN |
| Artefacto focal | Identidad/versión/hash de artefacto propio | Requerido por DEC-C10-067; valores/contrato OPEN |
| Instancia CMP | `instance_id + instance_version` | Identidad distinta según DEC-C10-069 |
| Valor Z | (Z_i\in\{0,1\}) | Semántica definida; clave de fila no cerrada |
| Mecanismo/vector Z | Identidad/versionado/provenance del diseño y vector | Contrato de claves OPEN |
| Ocurrencia Z | `event_id` | Propuesta Gate 98, no implementada |
| Revisión de ocurrencia | `event_record_id + event_revision` | Propuesta Gate 98, no implementada |
| Unidad receptora | Mapping DGP→U_G | OPEN según Gate 99 |

## 7. Bloqueos de cierre

| ID | Bloqueo | Cierre necesario |
|---|---|---|
| G100-01 | No hay `policy_contract_id` concreto | Identificar autoridad/registro canónico existente o aprobar contrato de identidad; no crear ID ad hoc |
| G100-02 | No hay `policy_version` concreta para B_g0^D2/B_g1^D2 | Recuperar versiones exactas del DGP; declarar revisión asignable y compatibilidad |
| G100-03 | No se identifica autoridad/custodio/versionado de política | Resolver quién publica, cambia y conserva versiones |
| G100-04 | Artefacto focal y versión/hash no localizados | Identificar artefacto preasignación y protocolo para versión recibida/desviación |
| G100-05 | `assignment_id` no demostrado como PK | Recuperar contrato de mecanismo/vector Z, claves, semilla, hash y unidad/cluster |
| G100-06 | Ocurrencia Z propuesta pero no materializada | Mantener event_id/event_record_id como propuesta Gate 98; no implementar |
| G100-07 | Política asignada/ofrecida/recibida sin diccionario de datos cerrado | Completar mapping exacto y evidencia/tiempos de cada estado |
| G100-08 | Binding POLICY_VERSION no está físicamente implementado | Mantener referencia externa tipada como alternativa lógica, sin FK física |
| G100-09 | Mapping a unidad experimental/clúster sigue OPEN | Remitir a cierre específico de unidad/interferencia posterior a Gate 99 |

## 8. Conclusión y continuidad

Gate 100 cierra la **semántica de identidad**: B es una definición contractual versionada; el artefacto es un objeto técnico independiente; CMP es una instancia de servicio independiente; Z es asignación/mecanismo distinto de la ocurrencia observada Z_ASSIGNED. La referencia externa tipada `policy_contract_id + policy_version` es compatible con Gate 98 y evita crear NODE artificial.

Gate 100 **no cierra los valores concretos**, la autoridad, el registro canónico, la clave de asignación, el versionado efectivo del artefacto ni la materialización de eventos. No se emite una DEC nueva ni se modifica DEC-C10-061/067/070.

**Siguiente gate recomendado:** Gate 101 — auditoría de fuentes/identificadores del artefacto focal y de la asignación Z (mecanismo, vector, seed/provenance y claves de unidad/cluster), limitada a localizar contratos y valores existentes antes de proponer nuevos campos.

**Control:** `scientific_execution=false`; `execution_authorized=false`; no se ejecutaron tests, validadores, workflows, simulaciones ni experimentos. Auditoría documental asistida, no independiente.
