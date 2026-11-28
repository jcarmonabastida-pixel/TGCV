# C10-S — Gate 114: crosswalk material UE–instancia CMP–U_G–EID–ruta

**ID:** C10-S-GATE-114-MATERIAL-CROSSWALK-001  
**Fecha:** 2026-11-15  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft  
**Estado:** B1_UE_TO_SERVICE_INSTANCE_CARDINALITY_RESOLVED_DOCUMENTALLY / CMP_TO_NODE_ANCHOR_1_TO_1_PER_SNAPSHOT_ACCEPTED / U_G_ROOT_MAPPING_NOT_EQUIVALENT / TRANSFORMATION_EID_MAPPING_OPEN / ROUTE_SCOPE_NOT_UNIT / MATERIAL_ROSTER_ABSENT / NO_IDS_MATERIALIZED / NO_SCHEMA_CHANGE / NO_EXECUTION / NO_FREEZE.  
**Tipo:** reconciliación documental de decisiones aceptadas y contratos; no materialización, no validación física, no ejecución.

---

## 1. Pregunta y resultado

Gate 114 resuelve qué cardinalidades pueden fijarse con decisiones aceptadas y cuáles siguen dependiendo de roster, snapshots, mappings y evidencia material.

**Resultado principal:** la cardinalidad UE↔instancia de servicio B1 no está ya abierta para el diseño lógico: quedó resuelta por `DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001`. Cada UE tiene un `instance_id` propio, único en el roster C10-S, con `instance_version` monotónica e independiente. La plantilla funcional y el contrato son comunes. Los valores concretos no se pueden asignar porque no hay roster material.

Además, `DEC-C10-082` acepta una correspondencia 1:1 entre cada CMP contractual aplicable y un NODE anchor dentro de cada snapshot exacto. Esto no convierte `instance_id` en `node_id`, no hace que la UE sea una unidad U_G y no resuelve por sí solo la identidad del nodo raíz.

Por tanto, el crosswalk lógico B1 se expresa como:

`UE_i → instance_i → {CMP components} → NODE anchors in snapshot_s`

con una relación separada de la aplicación de transformación:

`EID (application/attempt) → applicable TID/SID/RID + UE/context/time`

y otra de evaluación:

`route_id (versioned route/scope) → route steps/objects → O-CONF adjudication`.

Estas relaciones no deben colapsarse en una PK universal.

## 2. Fuentes autoritativas recuperadas

| Fuente | Regla que gobierna | Límite |
|---|---|---|
| `DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001` (2026-11-11) | Contrato común; una instancia lógica propia por UE; versionado independiente; componente local y clave compuesta | No asigna IDs concretos; no demuestra aislamiento |
| `DEC-C10-069` | Identidad/versionado del contrato e instancia de referencia ejemplar | Su instance_id de referencia no se reutiliza para todas las UE |
| `C10_S_PB_MATERIAL_D2_INSTANCE_AND_ISOLATION_RECONCILIATION_DRAFT_001.md` | Reconciliación de identidad B1 por UE y distinción instancia servicio vs dependencia focal | Roster material NONE; IAM/C_SRC observado NONE; aislamiento no demostrado |
| `DEC-C10-082` | CMP contractual↔NODE anchor 1:1 por CMP y snapshot exacto | Solo anclaje de identidad; no equivalencia funcional ni mapping entre snapshots |
| `DEC-C10-065` | Pinning exacto snapshot_id + snapshot_object_record_id y FK de revisión | Aceptación arquitectónica; FK física no validada |
| `DEC-C10-059/064` y contrato U_G FK/boundary | Identidad lógica NODE.node_id y revisión object_record_id; SNAPSHOT raíz con unit_id y unit_object_record_id | No equipara U_G con UE o instancia |
| `DEC-C10-076` | Identidad lógica vs identidad de registro exacto; typed refs y resolución exacta | No cierra registry/schema físico |
| `C10_S_IDENTITY_VERSION_AND_SNAPSHOT_MATCHING_CONTRACT_DRAFT_001.md` | TID/SID/RID/EID separados | Contrato de matching propuesto; no asumir mapping focal aceptado |
| Gate 109 y Gate 113 | No equivalencias entre UE/UA/U_G/instancia/EID/ruta; PE interfaces lógicas | Gate 109 antecede a la decisión B1 de 11-11; Gate 113 requiere actualizar la ambigüedad PE-PB-01 |

La fuente de verdad para las reglas aceptadas son las decisiones anteriores en su alcance; el Gate 114 no crea ni amplía decisiones.

## 3. Crosswalk por dominio

| Dominio | Identidad | Relación respaldada | Qué NO significa |
|---|---|---|---|
| UE | Índice/unidad experimental del DGP; clave concreta pendiente de roster | Una instancia de servicio B1 por UE | No es UA, U_G unit_id, CMP component_id ni route_id |
| UA | Unidad sobre la que actúa Z; rol `assignment_unit` | UE→UA según mecanismo de asignación aún no cerrado | No inferir UA=UE ni UA=cluster |
| Cluster | Identidad de clúster solo si se define en el diseño | UA→cluster solo si el mecanismo asigna por clúster | No deducirlo de correlación ni de NODE compartido |
| Contrato servicio | `contract_id + contract_version` | Común a las UE mientras semántica coincida | No identifica instancia ni unidad |
| Instancia CMP de servicio | `instance_id + instance_version` | **Una instancia única por UE** según DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001 | No es el ID de la instancia ejemplar DEC-C10-069 para todas las UE |
| Componente CMP | `(instance_id, component_id)` + class | Dentro de cada snapshot aplicable, cada CMP tiene exactamente un NODE anchor | No se duplica por ruta/etapa; no es EID |
| U_G NODE | `(object_class, node_id, object_record_id)`, con snapshot exacto | CMP→NODE anchor 1:1 por snapshot; root unit referenciado por SNAPSHOT mediante FK compuesta | No equiparar node_id con instance_id o UE |
| U_G logical root | `NODE.node_id` con `semantic_role=LOGICAL_SERVICE_UNIT`; revisión exacta `object_record_id` | Ancla la unidad lógica del snapshot; relación con UE requiere mapping explícito | No asumir que la raíz es la UE ni que un NODE por snapshot equivale a una unidad experimental |
| Snapshot | `snapshot_id + snapshot_object_record_id` y root `unit_id + unit_object_record_id` | Fija universo/revisión exacta; objetos del snapshot fijan también su revisión exacta | No es UE ni una nueva instancia |
| Transformación | TID (tipo), SID (especificación), RID (realización técnica), EID (aplicación/episodio) | EID se contextualiza con unidad/transformación/tiempo cuando se observa una aplicación | RID no es instancia CMP; EID no es instancia CMP ni evento genérico |
| Ruta | `route_id` versionada y route steps | Puede haber varias rutas por UE/instancia; O-CONF se adjudica por instance×route | No es unidad experimental, asignación ni identidad de instancia |
| UO/observación | Identidad de observación/captura y su provenance | Varias UO por UE, instancia, fuente y ventana son posibles | No aumenta N por sí sola |
| Run/fixture/scenario | Identidades de procedencia/ejecución propias | Enlazan material de experimento y ejecución | No son PK de UE/UA/cluster ni reemplazan EID |

## 4. Cardinalidades y estatus

| Relación | Regla lógica vigente | Estado material |
|---|---|---|
| UE→instancia CMP servicio B1 | 1:1; cada UE tiene instance_id único en roster | IDs no asignados; roster inexistente |
| contrato→instancias B1 | 1:N; contrato/version común mientras semántica coincida | No instanciado |
| instancia→componentes CMP | 1:N; component_id local; clave externa compuesta | Manifiesto por UE no materializado |
| CMP aplicable→NODE anchor | 1:1 por snapshot exacto (DEC-C10-082) | Sin snapshots/IAM/registro poblado; no PASS |
| NODE anchor→CMP | 1:1 por snapshot; no dos CMP distintos por el mismo anchor | Sin mapping poblado |
| UE→U_G logical root | Cardinalidad material no establecida por DEC-C10-059/064/082 | OPEN; requiere roster, snapshot y mapping UE↔root |
| UE→UA | 1:1 solo si asignación individual; N:1 posible si cluster/UA compartida | OPEN; mecanismo Z no especificado |
| UA→cluster | 1:1 si UA es clúster; no aplica si UA individual | OPEN |
| UE→EID | 0:N según haya cero, uno o múltiples episodios de aplicación observados; la semántica del EID exige aplicación/episodio concreto | Mapping y cardinalidad del DGP aún OPEN; no crear EID por cada NODE o ruta |
| UE→route_id | 1:N cuando se evalúan alternativas; no significa que todas se ejecuten | Roster de rutas OPEN |
| instancia×route→O-CONF | Unidad de adjudicación terminal | Agregación/mapping a UE OPEN |
| UE→V_cont | Una trayectoria de Value por UE, construida a partir de K intervalos | K/ventanas/observación siguen sus contratos; K no es N |
| UE→UO | 0:N / 1:N según disponibilidad de observaciones y cobertura | No materializado |

## 5. Reconciliación de la ambigüedad PE-PB-01

Gate 113 registró como ambigua la frase de PE §15 sobre `instance_id/instance_version` “propios de cada UE”, frente al Gate 109 que dejaba UE→CMP instance en 1:1, 1:N o N:1.

La ambigüedad queda **resuelta a nivel lógico para B1** por la decisión posterior y específica `DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001`:
- una instancia de servicio única por UE;
- IDs concretos únicos dentro del roster C10-S;
- plantilla/contrato común;
- versionado por instancia;
- instancia ejemplar DEC-C10-069 preservada como referencia, no reutilizada.

Por ello, el estado de PE-PB-01 pasa a `RESOLVED_DOCUMENTARILY_FOR_B1`. No se extrapola a otras variantes/servicios ni se interpreta como prueba de aislamiento material. La identidad de instancia técnica focal/dependencia que intenta provisionar B_g1 es distinta de la instancia lógica del servicio beneficiario.

## 6. Relaciones que no pueden derivarse

1. **UE↔U_G root:** DEC-C10-082 fija el anclaje CMP↔NODE por snapshot, no que el nodo raíz de SNAPSHOT sea la UE ni que exista un root por UE. El mapping necesita roster, snapshot exacto y referencia tipada.
2. **U_G NODE↔EID:** EID identifica una aplicación/episodio de transformación; NODE representa objeto lógico versionado. No existe equivalencia ni cardinalidad deducible.
3. **EID↔route:** una ruta puede contener varias transformaciones y una transformación puede ser reutilizada por distintas rutas. El mapping depende de route steps y de las ocurrencias observadas; no se crea EID por mera pertenencia a una ruta.
4. **Instancia CMP↔EID:** una instancia de servicio puede tener cero o varias aplicaciones de transformación en el tiempo; el EID no es un componente CMP.
5. **UE↔UA/cluster:** continúa abierto hasta que se especifique el mecanismo de aleatorización y la estructura de interferencia. La instancia única por UE no implica asignación individual ni aislamiento.
6. **Snapshot↔UE:** snapshot ancla una unidad lógica U_G; la relación con UE requiere mapping explícito. Un snapshot por instancia no debe asumirse si el contrato no lo determina.

En ausencia de roster o evidencia exhaustiva, los mappings permanecen UNKNOWN, no 0, no NA y no “sin relación”.

## 7. Consecuencias para Gate 109 y Gate 113

- Gate 109 conserva sus conclusiones sobre UE/UA/cluster/U_G/EID/ruta no equivalentes y mecanismo Z/interferencia abierto. Su celda UE→CMP instance debe especializarse para B1: **1:1 lógico aceptado**, con roster/IDs OPEN.
- Gate 113 §4.1/§8 G113-04 y PE-PB-01 deben dejar de describir la cardinalidad UE↔CMP como ambigüedad irresuelta para B1. La decisión posterior resuelve el nivel lógico; el mapping físico sigue sin evidencia.
- DEC-C10-069 permanece intacta: su instance_id es instancia ejemplar de referencia.
- DEC-C10-082 permanece intacta: CMP↔NODE anchor 1:1 por snapshot.
- DEC-C10-065/076 permanecen intactas: pinning y referencias tipadas exactas.
- No se modifica el DGP ni se resuelve UA, interferencia, soporte, RNG, estimandos ni C4.

## 8. Dependencias materiales que siguen abiertas

1. Roster exhaustivo de UE del DGP, incluyendo identidad y provenance.
2. Derivación y persistencia futura de instance_id único por UE, con historial/sucesión/versiones.
3. Manifiesto CMP/PAR/RUL/MET completo por instancia y mapping IAM.
4. Snapshots exactos comparables y root NODE con semantic_role LOGICAL_SERVICE_UNIT.
5. Mapping CMP contractual→NODE anchor por cada snapshot, con unicidad bidireccional y evidencia.
6. Mapping UE→U_G root y UE→observaciones/UO.
7. Inventario de dependencias P1, artefacto focal, RID y su relación con B_g1; no reutilizar instance_id CMP.
8. Definición y ocurrencias EID, TID/SID/RID aplicables y relación temporal con W_attempt/receipt/S_install.
9. Roster de rutas/route steps y mapping instance×route→UE.
10. Asignación UE→UA/cluster, vector Z, RNG/provenance, exposición G_i y soporte.
11. Pruebas materiales de aislamiento, recursos, estado, credenciales, canales y no-interferencia.

La reconciliación PB declara `MATERIAL_INVENTORY_NONE`, `ISOLATION_NOT_DEMONSTRATED`, no snapshots comparables y ningún roster material. Por tanto no se puede convertir el contrato lógico en registros concretos.

## 9. No-governance drift

- No crear `assignment_id`, `cluster_id`, `ue_id`, `service_instance_id`, tablas puente, nuevas FKs, columnas, schemas, DDL, fixtures ni test IDs.
- No convertir `C10S-SVC-REQUEST-PROCESSOR-001` en ID compartido de todas las UE.
- No igualar UE, UA, cluster, U_G root, instance_id, component_id, EID, RID, route_id, snapshot_id o run_id.
- No interpretar CMP↔NODE 1:1 por snapshot como identidad de todo el U_G.
- No declarar PASS de DEC-C10-082 sin universo exhaustivo, snapshot, mapping y evidencia.
- No confundir instancia de servicio B1 con adaptador/dependencia focal P1.
- No alterar DEC, C0, RMA, Evidence→Claim Matrix, STATUS, main ni PR status.
- No ejecutar validadores, código, tests, workflows, simulaciones, estimaciones, calibraciones o experimentos.

## 10. Dictamen

**GATE_114_B1_UE_TO_INSTANCE_1_TO_1_RESOLVED_DOCUMENTALLY / CMP_TO_NODE_ANCHOR_1_TO_1_PER_SNAPSHOT_REUSED / PE_PB_01_RESOLVED_FOR_B1 / UE_TO_UG_ROOT_OPEN / UE_TO_UA_CLUSTER_OPEN / EID_TO_UNIT_ROUTE_MAPPING_OPEN / ROUTE_ROSTER_OPEN / MATERIAL_ROSTER_NONE / ISOLATION_NOT_DEMONSTRATED / NO_IDS_MATERIALIZED / NO_SCHEMA_CHANGE / NO_IMPLEMENTATION / NO_EXECUTION / NO_FREEZE.**

Gate 114 reduce una ambigüedad real: para B1, la cardinalidad lógica UE↔instancia CMP está aceptada y no debe seguir tratándose como 1:1/1:N/N:1 abierta. No resuelve las cardinalidades materiales ni las demás identidades. La ausencia de roster y snapshots impide asignar IDs o demostrar relaciones concretas.

**Siguiente operación:** Gate 115 — reconciliar el contrato de roster/UE y la raíz U_G con DEC-C10-059/064/065/082, el contrato IAM y el material PB; identificar si existe una fuente aprobada que defina el universo/clave de UE y su mapping a SNAPSHOT.unit_id/unit_object_record_id. Si no existe, formalizar exactamente qué decisión documental falta para cerrar la identidad de UE sin crear otra clave por analogía. No materializar roster ni IDs en este gate.

---

**Gobernanza:** no se modifican main, RMA, Evidence→Claim Matrix, STATUS, DEC, C0, U_G ni schemas. PR #116 permanece Draft. `scientific_execution=false`; `execution_authorized=false`.
