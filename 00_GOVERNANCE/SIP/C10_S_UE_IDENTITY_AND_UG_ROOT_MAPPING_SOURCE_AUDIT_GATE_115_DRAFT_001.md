# C10-S — Gate 115: auditoría de la identidad UE y de su mapping a la raíz U_G

**ID:** C10-S-GATE-115-UE-IDENTITY-UG-ROOT-001  
**Fecha:** 2026-11-15  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft  
**Estado:** UE_SEMANTIC_ROLE_DEFINED / UE_PERSISTENT_KEY_NOT_ESTABLISHED / B1_PER_UE_RELATION_ACCEPTED / U_G_ROOT_IDENTITY_DEFINED / UE_TO_UG_ROOT_MAPPING_UNKNOWN / ROSTER_NOT_MATERIALIZED / NO_NEW_ID / NO_SCHEMA_CHANGE / NO_EXECUTION / NO_FREEZE.  
**Tipo:** reconstrucción documental de identidad, alcance de roster y relaciones; no materialización ni validación técnica.

---

## 1. Pregunta y dictamen ejecutivo

¿Existe una fuente aprobada que fije la identidad persistente de cada unidad experimental (UE) y su mapping exacto a `SNAPSHOT.unit_id/unit_object_record_id`?

**Dictamen:** existe una definición semántica aceptada de UE y una identidad/versionado diferenciada para la instancia de servicio B1 por UE. También existe una identidad canónica de la raíz lógica U_G y una FK compuesta exacta desde SNAPSHOT a NODE. Sin embargo, **no se ha localizado una clave persistente canónica de UE ni un mapping aprobado UE→raíz U_G**.

La UE es la unidad sintética completa indexada como (i), a la que se asigna (Z) y para la que se generan estados transformacionales, trayectorias, Outcome y Value. El campo U_G `unit_id` identifica otra cosa: la identidad semántica estable del NODE raíz `LOGICAL_SERVICE_UNIT`; `unit_object_record_id` identifica la revisión exacta de ese NODE. La similitud de nombres no permite equipararlos.

**Conclusión material:** `UE → SNAPSHOT.unit_id/unit_object_record_id = UNKNOWN`. No equivale a 0 ni a NA. La ausencia de roster, snapshots y registros IAM/C_SRC impide verificar la relación.

## 2. Fuentes recuperadas y fuerza normativa

| Fuente | Regla recuperada | Qué no resuelve |
|---|---|---|
| DGP Temporal and Role Contract, §2 y decisión B1 de 2026-11-11 | UE indexada como (i); unidad experimental y unidad de asignación separadas; UE es la instancia sintética completa asignada a Z y seguida hasta Outcome/Value | No define una clave persistente, namespace ni PK material de UE |
| `DEC-C10S-B1-UNIT-001`, integrada en el DGP | Una entidad B1 por UE, vinculada explícita, unívoca, versionada y trazable a instancia lógica de servicio; aislamiento es hipótesis a justificar | No convierte B1 o su instancia de servicio en identidad de UE; no proporciona roster/IDs |
| `DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001` | Contrato común; instancia lógica propia por UE; `instance_id` único en roster C10-S y `instance_version` monotónica; componente local | Identidad de servicio B1, no PK de UE; IDs concretos pendientes del roster |
| DEC-C10-059 y contrato U_G FK/boundary | `SNAPSHOT.unit_id = NODE.node_id` para raíz `LOGICAL_SERVICE_UNIT`; `unit_object_record_id = NODE.object_record_id`; boundary_class independiente | No afirma que UE sea esa unidad lógica |
| DEC-C10-060 / contrato semantic_role y raíz | Raíz U_G semántica, rol LOGICAL_SERVICE_UNIT; separación de host, entorno y S0 | No crea una identidad experimental ni mapping UE→raíz |
| DEC-C10-064/065 | Pinning exacto de snapshot y revisión raíz; integridad referencial/versionada | No establece PK UE ni mapping entre DGP y U_G |
| DEC-C10-082 | CMP contractual↔NODE anchor 1:1 por CMP y snapshot exacto | No convierte el anchor CMP en UE ni en raíz lógica por defecto |
| DEC-C10-089 | Raíz NODE y CMP contractual: relación sin adjudicar; requiere mapping explícito, versionado y sustentado | No adjudica UE↔raíz ni fuerza uno/dos NODE |
| Gate 109 | Roles UE, UA, cluster, UO, U_G, instancia, EID y ruta separados; G109-01 y G109-05 abiertos | No proporciona clave física UE ni mapping |
| Gate 114 | B1 UE→instancia de servicio 1:1 lógico; roster y mappings materiales ausentes | No cierra UE→U_G root |
| DEC-C10-096 / B1 Need cohort crosswalk | Censo de todas las UE del roster DGP/paquete B1 aprobado para la cohorte Need; pertenencia por identidad/binding y versión del roster pre-Z | No crea el roster ni determina la clave primaria de UE; el roster sigue pendiente |

Las decisiones se reutilizan en su alcance exacto. Gate 115 no modifica ni amplía ninguna de ellas.

## 3. Identidad UE: qué está definido

### 3.1 Semántica

La unidad experimental es la unidad de potenciales/resultados del DGP:
- recibe la asignación Z conforme al mecanismo que se apruebe;
- se le vinculan la política D2, su versión y las etapas W_programmed, W_attempt, receipt y S_install;
- se reconstruyen C_dep*, A_f*, D_f*, ΔT_acc*, Reach y trayectoria;
- se generan/adjudican Outcomes y Value por unidad y horizonte;
- V_cont se calcula por UE a través de K intervalos, sin convertir K en N.

La notación (i) es un índice de unidad en la formulación del DGP. No demuestra por sí misma que exista un identificador persistente serializado.

### 3.2 B1 no es la clave UE

`DEC-C10S-B1-UNIT-001` acepta una entidad B1 por UE. La decisión posterior de identidad de servicio acepta un `instance_id` único por UE, con versionado propio. Esta relación permite exigir que el roster futuro tenga un binding unívoco UE↔B1/instancia de servicio.

No autoriza:
- reutilizar `instance_id` como PK UE;
- inferir UE a partir de `component_id`;
- tratar la instancia ejemplar `C10S-SVC-REQUEST-PROCESSOR-001` como identificador de todas las UE;
- presumir aislamiento efectivo porque haya instancias lógicas distintas.

La identidad de UE y la identidad de la instancia B1 deben conservar semánticas separadas aunque su relación de diseño sea 1:1.

### 3.3 El campo genérico unit_id no cierra el gap

El Test Contract Register y PE mencionan `unit_id` en el bloque unidad/asignación, pero no establecen un namespace, tipo, alcance de unicidad o binding inequívoco que demuestre que ese campo sea la PK de UE. En U_G, `unit_id` tiene una semántica específica ya fijada: equivale a `NODE.node_id` de la raíz `LOGICAL_SERVICE_UNIT`.

No se puede reutilizar el mismo literal de campo para dos entidades distintas sin un contrato de namespace y mapping. La presencia de `unit_id / assignment_unit` en una plantilla de test demuestra que se contemplan los roles; no que exista una PK material ni que `unit_id` sea UE en vez de U_G.

## 4. Identidad U_G y significado exacto del snapshot

El contrato U_G establece:

`SNAPSHOT.unit_id = NODE.node_id`

`SNAPSHOT.unit_object_record_id = NODE.object_record_id`

La FK compuesta resuelve la revisión exacta del NODE raíz con `semantic_role=LOGICAL_SERVICE_UNIT`. Todos los snapshots de la misma unidad lógica conservan `unit_id`; `unit_object_record_id` puede cambiar cuando cambia la revisión observada.

Por tanto:
- `unit_id` es identidad semántica de la unidad lógica de servicio;
- `unit_object_record_id` es identidad de la revisión exacta de la raíz;
- `snapshot_id + snapshot_object_record_id` identifica la captura/versionado del snapshot;
- ninguna de estas claves se convierte por sí misma en UE, UA, cluster, CMP instance, EID o run.

DEC-C10-089 además deja sin adjudicar la relación entre raíz lógica y CMP contractual. DEC-C10-082 ancla cada CMP aplicable a un NODE por snapshot, pero no declara que ese NODE sea la raíz. No hay base para derivar UE→root a través de CMP.

## 5. Crosswalk de identidades y relaciones

| Dominio | Identidad semántica | Relación admisible | Estado actual |
|---|---|---|---|
| UE | Índice (i) en el DGP; clave persistente no definida | UE→B1 1:1 lógico; UE→UA según mecanismo; UE→U_G root requiere mapping | Semántica definida; PK material OPEN |
| B1 | Entidad solicitante/beneficiaria sintética | Una B1 por UE; binding explícito y versionado | Regla aceptada; no materializada |
| Instancia servicio B1 | `instance_id + instance_version` | Una instancia lógica por UE en el roster C10-S | Cardinalidad lógica aceptada; IDs/roster OPEN |
| UA | Rol `assignment_unit` | Puede coincidir con UE solo bajo diseño individual justificado; puede ser cluster | Clave y mapping OPEN |
| Cluster | Unidad de aleatorización/agrupación si el mecanismo lo usa | UA→cluster según arquitectura seleccionada | No establecido |
| U_G root | `NODE.node_id`, semantic_role LOGICAL_SERVICE_UNIT | SNAPSHOT fija root y revisión exacta | Identidad U_G definida; relación UE→root OPEN |
| Revisión root | `NODE.object_record_id` | Referencia exacta mediante `unit_object_record_id` | Contrato aceptado; registros no observados |
| Snapshot | `snapshot_id + snapshot_object_record_id` | Captura exacta de una unidad lógica y su revisión raíz | Sin snapshots C10-S comparables |
| CMP anchor | Referencia CMP↔NODE por snapshot | 1:1 por CMP y snapshot conforme DEC-C10-082 | Regla documental; mapping poblado ausente |
| EID | Aplicación/episodio de transformación según TID/SID/RID/EID | UE/contexto/tiempo mediante mapping de aplicación | Mapping UE/EID OPEN |
| Run/fixture/scenario | Identidad de procedencia y ejecución | Enlaza contrato, fixture, escenario y run | No es identidad UE ni Z |
| O-CONF / V_cont | O-CONF por instancia×ruta; V_cont por UE×K intervalos | Agregación solo mediante regla explícita | No se modifica el crosswalk de Gate 109/110 |

## 6. Roster y poblaciones: evitar equivalencias falsas

Se distinguen al menos cuatro marcos:
1. **Roster DGP de UE/B1:** universo de unidades sintéticas definido por el diseño; todavía no materializado ni aprobado.
2. **Cohorte de validación Need:** DEC-C10-096 la delimita como censo del roster B1 aplicable; su propósito es validar E1/E2 y soporte truth 1/0, no definir la población causal.
3. **P*_{τ2}:** población causal primaria candidata de C1 ITT-D2, definida por condiciones basales; no equivale al roster total.
4. **P*_F:** subpoblación secundaria de apertura funcional exclusiva, subconjunto de P*_{τ2}; no define la identidad de UE.

La pertenencia al roster se determina por identidad/binding y versión pre-Z. No se filtra por Need, Z, observabilidad, tratamiento recibido, accesibilidad o resultados posteriores. Los defectos de identidad/materialización deben permanecer como bloqueos explícitos, no convertirse en truth=? ni eliminarse silenciosamente.

## 7. Cardinalidades: lo que puede afirmarse

| Relación | Dictamen |
|---|---|
| UE→B1 | 1:1 lógico, decisión aceptada |
| UE→instancia servicio B1 | 1:1 lógico, decisión aceptada; IDs materiales pendientes |
| UE→UA | OPEN; UE=UA solo si se demuestra diseño individual y aislamiento |
| UA→cluster | OPEN; depende del mecanismo de aleatorización |
| UE→U_G root | UNKNOWN; no hay mapping aprobado ni snapshots/roster |
| U_G root→CMP contractual | Sin adjudicar por DEC-C10-089 |
| CMP→NODE anchor | 1:1 por CMP y snapshot exacto, alcance DEC-C10-082 |
| UE→EID / UE→route | OPEN; requieren ocurrencias/rutas y mapping temporal explícito |
| UE→UO | 0:N según fuentes/ventanas; roster de observaciones no materializado |

No se transforma una ausencia de evidencia en cardinalidad cero. Para UE→U_G root se mantiene UNKNOWN.

## 8. Decisión documental que falta para cerrar la identidad UE

No falta otra definición de U_G. Falta una especialización del contrato DGP/PE que fije la **identidad de unidad experimental independiente de las identidades técnicas y de observación**.

Antes de crear claves o materializar roster, el contrato sucesor debe resolver expresamente:

1. Si el índice (i) es solo posición local de un roster/run o identidad semántica persistente de la UE.
2. El alcance de unicidad y continuidad de esa identidad: DGP/paquete B1, escenario, réplica, run o población; cómo se representan copias/replays y supersesión sin colisionar.
3. Qué artefacto existente es la fuente autoritativa del roster y cómo se versiona/cierra el censo antes de Z.
4. Cómo se enlaza cada UE con su B1/instancia `instance_id` sin convertir esa instancia en PK UE.
5. Cómo se declara y versiona el mapping UE→U_G root por snapshot exacto; si una UE contiene una o varias unidades lógicas, o si una unidad lógica puede reutilizarse en más de una UE, el mapping debe representarlo sin presuponer cardinalidad.
6. Cómo se separan las identidades de UE, UA/cluster, UO, U_G root/revisión, snapshot, EID, route, fixture, scenario y run.
7. Qué condición de integridad permite distinguir mapping ausente, mapping desconocido, cardinalidad múltiple y ausencia demostrada con cobertura exhaustiva.

Este gate **no propone el nombre de una nueva clave**, no decide si debe añadirse un ID adicional y no aprueba una nueva DEC. Solo especifica el contenido mínimo de la decisión pendiente. Si el contrato vigente ya contiene una regla que satisfaga estos siete puntos, debe citarse y reutilizarse en lugar de duplicarla.

## 9. Disposición sobre Gate 114 y dependencias posteriores

- Gate 114 conserva la cardinalidad UE→instancia de servicio B1 1:1 lógico.
- Se mantiene que UE no equivale a U_G root, y que instance_id no equivale a unit_id.
- DEC-C10-059/060/064/065/082/089 permanecen intactas.
- No se reabre la decisión de raíz U_G ni se adjudica la relación raíz↔CMP que DEC-C10-089 dejó abierta.
- No se cambia la población P*_{τ2}/P*_F, DEC-C10-096, el mecanismo Z ni el análisis de interferencia de Gate 110.
- La ausencia de roster/snapshots bloquea la materialización y cualquier afirmación de FK validada.

## 10. No-governance drift y autorización

- No crear `ue_id`, `unit_id` alternativo, `assignment_id`, `cluster_id`, tablas puente, FKs, columnas, DDL, schemas, fixtures ni test IDs.
- No reutilizar `instance_id`, `node_id`, `object_record_id`, `snapshot_id`, `run_id`, `fixture_id` o `scenario_id` como PK UE.
- No asumir UE=UA, UE=cluster, UE=U_G root ni UE=CMP instance.
- No convertir DEC-C10-096 (censo de cohorte Need) en aprobación del roster causal/experimental.
- No declarar aislamiento ni ausencia de interferencia.
- No modificar DEC, C0, U_G, main, RMA, Evidence→Claim Matrix ni STATUS.
- No ejecutar validadores locales, código, tests, workflows, simulaciones, estimaciones, calibraciones ni experimentos.

**Dictamen final:** `GATE_115_UE_SEMANTIC_ROLE_RECONCILED / UE_PERSISTENT_KEY_NOT_ESTABLISHED / B1_PER_UE_BINDING_ACCEPTED / UG_ROOT_IDENTITY_AND_SNAPSHOT_FK_DEFINED / UE_TO_UG_ROOT_MAPPING_UNKNOWN / ROSTER_NOT_MATERIALIZED / NO_NEW_ID / NO_SCHEMA_CHANGE / NO_IMPLEMENTATION / NO_EXECUTION / NO_FREEZE`.

**Siguiente operación:** Gate 116 — auditoría del contrato de roster y binding pre-Z: determinar si el DGP/PE y los contratos B1/Need ya ofrecen una fuente autoritativa versionada del roster, una regla de integridad/continuidad por UE y un binding verificable UE↔B1↔instance_id. Si no, precisar si el gap se resuelve con una decisión de identidad DGP o con una extensión acotada del contrato de roster; no elegir una clave ni materializar unidades. En paralelo, mantener UE→U_G root UNKNOWN hasta que exista mapping explícito con snapshots exactos.  

**Gobernanza:** PR #116 permanece Draft. No se modifica main, RMA, Evidence→Claim Matrix, STATUS, DEC, C0 ni U_G. `scientific_execution=false`; `execution_authorized=false`.
