# C10-S — Gate 116: reconciliación de identidad, versionado del roster y binding pre-Z

**ID:** C10-S-GATE-116-ROSTER-IDENTITY-PREZ-BINDING-001  
**Fecha:** 2026-11-15  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft  
**Estado:** UE_IDENTITY_FIELD_ALREADY_SPECIFIED_AS_DRAFT / ROSTER_MANIFEST_CONTRACT_DRAFT_EXISTS / DEC_CENSUS_SCOPE_ACCEPTED / ROSTER_APPROVAL_ABSENT / UE_KEY_SCOPE_AND_CONTINUITY_OPEN / PREZ_BINDING_RULE_SPECIFIED_BUT_NOT_MATERIALIZED / NO_NEW_ID / NO_SCHEMA_CHANGE / NO_EXECUTION / NO_FREEZE.  
**Tipo:** reconstrucción histórica y reconciliación de contratos B1/Need; no aprobación de roster ni materialización.

---

## 1. Pregunta y dictamen

¿Existe ya una fuente autoritativa y versionada de roster, una identidad de UE con continuidad definida y un binding pre-Z verificable UE↔B1↔instancia?

**Dictamen:** existen piezas de diseño explícitas y aceptadas, pero no el roster aprobado/materializado que las haga operativas. El campo lógico `ue_id` ya aparece en el contrato mínimo de materialización B1/Need y en el contrato del paquete analítico; por tanto, no debe afirmarse que la identidad UE no esté representada en absoluto. El paquete también define `roster_id`, `roster_version`, `roster_digest`, un `PACKAGE_MANIFEST` y un `UNIT_BINDING`.

Sin embargo, ambos contratos de paquete/materialización siguen en estado de propuesta no aprobada, no implementada y no materializada. No hay roster cerrado, aprobado ni con valores concretos. No se ha encontrado una decisión que fije el namespace/alcance de unicidad y continuidad de `ue_id` entre versiones de DGP, roster, paquete, escenario, réplica y run. La identidad y el binding están **especificados parcialmente a nivel lógico**, no demostrados ni ejecutables.

**Resultado:** no se necesita inventar otra clave ni crear un séptimo artefacto. El gap inmediato es la aprobación documental de la fuente de roster y el cierre de sus reglas de identidad/continuidad, antes de cualquier materialización.

## 2. Fuentes históricas recuperadas

| Fuente | Contenido vinculante o propuesto | Estado y límite |
|---|---|---|
| DEC-C10-095 | Estipulación Need_preZ por B1/UE y versión basal; roster/cohorte se define ex ante por identidad y binding; integridad inválida bloquea, no se convierte en truth=? | Aceptada como working design; no aprueba roster ni schema |
| DEC-C10-096 | Cohorte Need = censo de todas las UE del roster DGP/paquete aprobado al que aplica B1/Need; pertenencia por roster identity/version, UE identity y binding B1↔UE↔service-instance antes de truth/evidence/Z | Aceptada; expresamente deja abierta aprobación/versionado del roster y material identity/binding |
| DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001 | Cada UE tiene `instance_id` propio y único en roster C10-S; `instance_version` monotónica; unicidad contra roster completo, incluidas instancias históricas/supersedidas | Decisión aceptada; no asigna IDs ni aprueba/materializa roster |
| B1 minimum DGP materialization contract §2 | Define `ue_id`, `b1_id`, `contract_id/version`, `instance_id/version`, `baseline_record_id`, `z_event_id`; IDs se generan solo desde roster cerrado y versionado | DOCUMENTARY_SPECIFICATION / NOT_APPROVED / NOT_MATERIALIZED |
| B1 analytical package contract §§3–4, 10 | `PACKAGE_MANIFEST` contiene `package_id/version`, `dgp_spec_id/version`, `dgp_code_commit` cuando exista implementación, `roster_id/version/digest`; `UNIT_BINDING` contiene UE↔B1↔servicio↔ancla basal↔Z | PACKAGE_REPRESENTATION_NOT_APPROVED; sin registros físicos |
| B1 validation cohort population crosswalk | Cohorte Need se deriva del roster DGP B1/UE; no se equipara con P* ni denominadores ITT | Reconciliación documental; roster no aprobado |
| DGP Temporal and Role Contract §2 | UE indexada como (i); UE y UA se declaran separadamente; asignación por clúster/interferencia requiere ampliar indexación/estimandos | Contrato DGP DRAFT / NOT APPROVED; no fija clave persistente |
| Test Contract Register §2 | Usa `unit_id / assignment_unit` para expresar UE y UA como roles distintos | Plantilla genérica; no define namespace/PK de UE y no debe prevalecer sobre la identidad U_G de `unit_id` |
| Gate 115 | Concluyó que no se había localizado clave persistente canónica ni mapping UE→raíz U_G | Se corrige parcialmente: sí existe campo lógico propuesto `ue_id`; sigue sin existir roster aprobado ni mapping UE→U_G root |

## 3. Identidad UE: precisión corregida

### 3.1 Campo lógico ya existente

El contrato mínimo B1/Need §2 define expresamente `ue_id` como identidad de la unidad experimental sintética. El contrato del paquete analítico §4.2 lo repite como clave por unidad. No se debe crear un segundo identificador, renombrar el campo ni sustituirlo por `instance_id`, `node_id` o el `unit_id` de U_G.

La regla existente dice que los IDs concretos solo se generan a partir de un roster cerrado y versionado. Esto es una regla de precedencia/materialización, no una definición completa de continuidad.

### 3.2 Reglas aún no fijadas

No se ha encontrado decisión aprobada que resuelva:
- si `ue_id` es global/persistente para una unidad conceptual o único dentro de un `roster_id`, DGP, paquete o escenario;
- si la misma UE conserva identidad al aparecer en una nueva `roster_version` o `package_version`;
- cómo se distinguen una nueva réplica/unidad, un replay de la misma unidad, una copia/snapshot y una unidad sucesora;
- qué sucede con una UE retirada/supersedida y si sus IDs se pueden reutilizar (la regla de no reutilizar IDs de instancia no sustituye la regla de UE);
- cómo se relacionan rosters A y B separados o un eventual roster conjunto;
- qué fuente/artefacto es el owner autoritativo del roster, quién lo aprueba y qué condición lo cierra.

No se deben importar automáticamente a UE las reglas de `instance_id`: la decisión de instancia tiene su propio ámbito de unicidad y versionado.

## 4. Roster y manifiesto: estado exacto

El contrato del paquete ya ofrece una representación lógica suficiente para alojar la referencia de roster sin crear otro artefacto:
- `PACKAGE_MANIFEST`: identifica paquete, DGP/spec, versiones, roster y digest;
- `UNIT_BINDING`: expresa las relaciones por unidad y sus referencias;
- `TRUTH_LEDGER`, `EVIDENCE_LEDGER`, `ADJUDICATION_LEDGER` y `EVALUATION_LEDGER`: consumen las identidades/bindings según su segregación de roles.

Esto no prueba que el manifiesto exista físicamente ni que su contrato esté aprobado. El propio documento declara `PACKAGE_REPRESENTATION_NOT_APPROVED`; el mínimo DGP declara `NOT_APPROVED` y `NO_ROSTER`. DEC-C10-096 exige que el roster sea aprobado, versionado y cerrado antes de evaluar el censo. La condición no está satisfecha.

No hay evidencia de un artefacto canónico alternativo de roster ya aprobado. Por tanto, no se debe señalar el manifiesto propuesto como fuente autoritativa efectiva hasta que se apruebe el contrato que le da ese papel y se identifique el artefacto concreto/versionado.

## 5. Binding pre-Z: regla definida, evidencia material ausente

La cadena lógica requerida está descrita:
`roster identity/version → ue_id → b1_id → contract_id/version + instance_id/version → baseline_record_id (t−1) → z_event_id (t0)`.

Reglas recuperadas:
1. Una B1 por UE.
2. Una instancia lógica de servicio propia por UE; `instance_id` único en el roster completo, con `instance_version` monotónica.
3. El contrato funcional puede ser común; `contract_id/version` no se confunde con la identidad/versionado de instancia.
4. El ancla basal es inmutable y anterior a Z.
5. `z_event_id` refiere al evento de asignación y debe ser posterior al ancla basal.
6. La pertenencia a la cohorte Need se fija ex ante por roster/version, UE identity y binding válido; no por Need, evidencia, Z, cumplimiento ni resultados.

Falta materializar y validar la cadena. No hay roster/IDs, baseline records, eventos Z, IAM ni registros C_SRC observados. No puede declararse binding verificado, aislamiento material ni integridad de referencias.

## 6. Crosswalk de identidades, no equivalencias

| Campo/objeto | Qué identifica | No debe confundirse con |
|---|---|---|
| `roster_id + roster_version + roster_digest` | Edición íntegra del universo/roster de unidades | UE individual, paquete o DGP completo |
| `ue_id` | Unidad experimental sintética | B1, instancia de servicio, UA/cluster, U_G root, fixture o run |
| `b1_id` | Entidad B1 vinculada unívocamente a UE | UE ni servicio técnico |
| `contract_id + contract_version` | Contrato funcional común | Instancia concreta |
| `instance_id + instance_version` | Instancia lógica de servicio propia de UE y su revisión | UE ni `NODE.node_id` |
| `baseline_record_id` | Ancla basal inmutable pre-Z | Identidad persistente UE |
| `z_event_id` | Episodio de asignación en t0 | Identidad de UE, brazo por sí solo o run |
| `SNAPSHOT.unit_id` | `NODE.node_id` de la raíz U_G `LOGICAL_SERVICE_UNIT` | `ue_id` |
| `unit_object_record_id` | Revisión exacta del NODE raíz | UE ni `instance_version` |
| `assignment_unit` / cluster | Unidad/agrupación de asignación, según mecanismo | UE por defecto |
| fixture/scenario/run | Procedencia y contexto de test/ejecución | Identidad experimental persistente |

UE→U_G root sigue UNKNOWN. La relación se resolverá solo con mapping explícito y snapshots exactos; no se deriva del binding B1 ni de la instancia CMP.

## 7. Dictamen de suficiencia y gap

| Requisito | Estado |
|---|---|
| Campo lógico de identidad UE (`ue_id`) | ESPECIFICADO EN CONTRATOS DRAFT |
| Roster con identidad/version/digest | ESPECIFICADO EN PACKAGE_MANIFEST DRAFT |
| Fuente autoritativa aprobada del roster | OPEN / NO LOCALIZADA |
| Alcance/namespace de unicidad UE | OPEN |
| Continuidad/sucesión/replay entre versiones | OPEN |
| Decisión A/B separado vs conjunto | OPEN |
| Binding UE↔B1↔instancia | REGLA LÓGICA ACEPTADA; NO MATERIALIZADA |
| Ancla basal y orden pre-Z | ESPECIFICADOS; NO MATERIALIZADOS |
| Binding z_event_id posterior | ESPECIFICADO; NO MATERIALIZADO |
| Censo de cohorte Need | ALCANCE ACEPTADO; CONDICIONADO A ROSTER APROBADO |
| UE→U_G root | UNKNOWN |

**Conclusión:** no se requiere una nueva clave UE ni un séptimo artefacto. Se requiere un cierre documental acotado que apruebe (o rechace/modifique con justificación) el contrato de roster/manifest existente y complete namespace, continuidad, roster scope A/B, autoridad, cierre pre-Z y reglas de binding. Solo después podría aprobarse y materializarse un roster concreto bajo autorización separada.

## 8. Corrección de Gate 115

La frase de Gate 115 “la clave persistente/namespace/continuidad del roster no está establecida” sigue siendo correcta respecto de la ausencia de una clave aprobada y de reglas completas. Pero su lectura “no existe representación de identidad UE” sería demasiado fuerte: `ue_id` sí aparece como campo lógico propuesto en el mínimo DGP y el paquete analítico. Gate 116 precisa que existe **identidad representada en draft**, no identidad canónica aprobada ni roster material.

Esta precisión no cambia el dictamen UE→U_G root = UNKNOWN ni el estado de materialización.

## 9. No-governance drift y autorización

- No crear otro ID UE, alias o clave alternativa.
- No promover `ue_id` a clave canónica aprobada por mera presencia en contratos draft.
- No tratar `roster_id/version/digest` propuestos como artefacto real aprobado.
- No materializar roster, UE, B1, instancias, truth, evidence, baseline, Z, snapshots ni registros IAM/C_SRC.
- No asumir UE=UA/cluster/U_G root/CMP instance.
- No modificar DEC-C10-095/096, C0, U_G, RMA, Evidence→Claim Matrix, STATUS ni main.
- No ejecutar validadores, código, tests, workflows, simulaciones, estimaciones, calibraciones ni experimentos.

**Dictamen final:** `GATE_116_DRAFT_IDENTITY_AND_ROSTER_RECONCILIATION_COMPLETE / UE_IDENTITY_FIELD_EXISTS_AS_DRAFT / ROSTER_MANIFEST_CONTRACT_EXISTS_AS_DRAFT / ROSTER_APPROVAL_ABSENT / UE_KEY_SCOPE_AND_CONTINUITY_OPEN / B1_PREZ_BINDING_RULE_SPECIFIED_NOT_MATERIALIZED / NO_NEW_ID / NO_SCHEMA_CHANGE / NO_EXECUTION / NO_FREEZE`.

**Siguiente operación:** Gate 117 — cerrar por reconstrucción documental el alcance/namespace y la continuidad de `ue_id`, y la decisión A/B sobre roster separado o conjunto, usando los contratos DGP, package, identidad B1 e historial de decisiones. Si las fuentes no permiten decidirlo sin nueva decisión del responsable científico, presentar la bifurcación exacta para decisión explícita; no seleccionar una opción ni crear roster.

**Gobernanza:** PR #116 permanece Draft. `scientific_execution=false`; `execution_authorized=false`.
