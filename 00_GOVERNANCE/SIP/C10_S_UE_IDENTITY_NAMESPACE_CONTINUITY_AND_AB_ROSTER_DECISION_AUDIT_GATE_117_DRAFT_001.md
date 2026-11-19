# C10-S — Gate 117: auditoría de namespace/continuidad UE y alcance de roster A/B

**ID:** C10-S-GATE-117-UE-NAMESPACE-CONTINUITY-AB-ROSTER-001  
**Fecha:** 2026-11-15  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft  
**Estado:** UE_LOCAL_ROLE_CONFIRMED / UE_GLOBAL_PERSISTENCE_NOT_SPECIFIED / ROSTER_VERSION_SCOPE_PROPOSED_NOT_APPROVED / A_B_ROSTER_SCOPE_OPEN_BY_DECISION / UE_VS_UA_NOT_EQUIVALENT_BY_DEFAULT / CLUSTER_INTERFERENCE_REGIME_OPEN / NO_NEW_ID / NO_DECISION_CHANGE / NO_FREEZE / NO_IMPLEMENTATION / NO_EXECUTION.

---

## 1. Pregunta y dictamen

Gate 117 reconstruye si las fuentes existentes permiten cerrar: (a) namespace y continuidad de `ue_id`; (b) roster A/B separado o conjunto; y (c) relación UE–UA–cluster.

**Dictamen:** no existe base documental suficiente para escoger una identidad persistente global ni para decidir roster A/B conjunto o separado. Sí puede establecerse una interpretación mínima compatible con las fuentes: UE es una unidad experimental lógica indexada por (i) dentro del DGP; el contrato del paquete la representa mediante `ue_id` y obliga a resolver referencias dentro del mismo `package_id/package_version`. Esto permite identidad inequívoca dentro de un roster/paquete aprobado, pero no define continuidad de la misma UE entre versiones de roster, DGP, escenarios, réplicas o replays.

La decisión A/B permanece explícitamente abierta en DEC-C10-096. No se debe convertir una condición de alcance en una elección implícita.

## 2. Fuentes reconstruidas

| Fuente | Regla recuperada | Límite |
|---|---|---|
| DGP Temporal and Role Contract §2 | Unidad experimental y unidad de asignación se declaran por separado; contrato expresado para unidad (i); si hay asignación por cluster o interferencia, ampliar indexación y estimandos antes de implementar | DRAFT / NO APPROVED; no decide UE=UA ni define PK persistente |
| DGP Temporal and Role Contract §2, t0 | (Z_i) y probabilidad de asignación; preservar ITT | No determina la unidad real de aleatorización ni el mecanismo final |
| B1 minimum DGP materialization contract §2 | `ue_id` identifica unidad experimental sintética; IDs concretos solo se generan desde roster cerrado y versionado | NOT_APPROVED / NOT_MATERIALIZED; no define namespace ni continuidad entre rosters |
| B1 analytical package contract §§3–4 | `package_id/version`, `roster_id/version/digest`, `ue_id`; referencias resuelven dentro del mismo paquete/versión | PACKAGE_REPRESENTATION_NOT_APPROVED; no define matching entre versiones |
| DEC-C10-095 | Estipulación Need por B1/UE y baseline/package version; no aprueba roster, prevalencia ni tamaño muestral | ACCEPTED WORKING DESIGN, NOT DESIGN FREEZE |
| DEC-C10-096 | Censo de todas las UE del roster DGP/package aprobado al que aplique B1/Need; si A/B separados, roster aplicable exacto; si conjunto, todas las UE aplicables | La decisión declara expresamente que no elige entre A/B separados o conjunto |
| DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001 | Cada UE tiene instancia propia; `instance_id` único en roster C10-S; `instance_version` monotónica por instancia | Resuelve identidad de instancia, no namespace de UE; no se extrapola su unicidad a `ue_id` |
| Gate 116 | `ue_id` existe como identidad lógica propuesta; roster/manifest y binding aún no aprobados ni materializados | Sin evidencia material de continuidad ni mappings |
| DGP/plan §28 | Interferencia, exposición, unidad/cluster y carryover requieren régimen explícito; contraste individual aislado no es válido si hay recursos/pools compartidos sin modelar | Sigue OPEN |

## 3. Namespace y continuidad de UE

### 3.1 Lo que sí se puede sostener

- La unidad semántica es UE, indexada como (i) en el DGP.
- `ue_id` es el campo lógico ya propuesto para identificar esa unidad en el paquete.
- El paquete define `roster_id`, `roster_version`, `roster_digest`, y obliga a resolver referencias dentro de `package_id/package_version`.
- El contrato mínimo impide generar IDs concretos antes de disponer de roster cerrado/versionado.

### 3.2 Lo que no se puede elevar a decisión

No está definido si `ue_id`:
- es único solo dentro de un roster/paquete versionado;
- conserva identidad al cambiar `roster_version` o `package_version`;
- identifica una unidad conceptual persistente entre escenarios D1/D2;
- se reutiliza para replay determinista de la misma unidad;
- cambia para una réplica nueva o para una unidad sucesora;
- requiere matching explícito entre versiones o si las versiones son universos completamente nuevos.

La regla de `instance_id` único contra roster completo no resuelve estas cuestiones de UE. Tampoco `package_id`, `roster_id`, `scenario_id`, fixture o run son sustitutos de `ue_id`.

**Resultado de identidad:** namespace local a roster/paquete es una interpretación provisional conservadora y compatible con la resolución de referencias intra-paquete, no una decisión aprobada de persistencia. La continuidad inter-versiones queda UNKNOWN. No se inventa PK compuesta ni se propone renombrar el campo.

## 4. Roster A/B: bifurcación explícita

DEC-C10-096 mantiene dos alternativas válidas, sujetas al roster DGP/package aprobado:

| Alternativa | Implicación | Consecuencia para cohorte Need |
|---|---|---|
| A — rosters separados | Cada escenario/paquete A o B tiene roster versionado propio; no se presupone equivalencia ni matching UE entre ellos | Se evalúa el censo completo del roster aplicable a cada paquete |
| B — roster conjunto | Un roster versionado incluye todas las UE de A/B y permite distinguir el escenario dentro del registro de unidad | Se evalúa el censo de todas las UE a las que aplique el paquete |

No se ha recuperado una decisión previa que elija A o B. Tampoco hay evidencia de que A y B compartan universo, composición o identidad de unidad. Por ello:
- no se selecciona ninguna alternativa;
- no se presupone que los índices (i) de A y B sean comparables;
- no se presupone una misma UE expuesta a ambos escenarios;
- no se interpreta la bifurcación como una elección de estimando ni como diseño crossover.

La decisión requiere una justificación científica de la comparación pretendida: escenarios como universos independientes vs variantes aplicadas al mismo universo de unidades. Si ambos escenarios son potenciales tratamientos de una misma población, la estructura de unidad/potenciales y asignación debe decirlo expresamente; si son poblaciones sintéticas distintas, el crosswalk entre unidades no debe inventarse.

## 5. UE, UA y cluster

Las fuentes obligan a declarar UE y UA separadamente. No establecen que sean siempre distintas, pero tampoco autorizan asumir que sean la misma entidad. Por tanto:

- UE es unidad sobre la que se definen estados, trayectorias, Outcome y Value.
- UA es la unidad a la que se asigna Z conforme al mecanismo efectivo.
- Cluster es la unidad/grupo de aleatorización solo si el diseño utiliza asignación agrupada.
- Si UE=UA, debe quedar declarado y justificado por el mecanismo de aleatorización.
- Si UA agrupa varias UE, debe definirse mapping UE→UA y estimandos/varianza coherentes.
- Si hay interferencia, spillovers, recursos compartidos o carryover, debe definirse exposición/interference regime y ampliar indexación antes de implementar.

El DGP actual no autoriza congelar aleatorización individual ni inferencia individual independiente. Z_i aparece como notación de trabajo, mientras que el propio contrato mantiene abierta la unidad efectiva de asignación y el régimen de interferencia.

## 6. Qué está cerrado, qué falta y efecto sobre Design Freeze

| Dominio | Estado |
|---|---|
| Semántica de UE | Definida |
| Campo lógico `ue_id` | Propuesto en contratos Draft |
| Binding UE–B1–instancia B1 | Cardinalidad lógica aceptada |
| Namespace/continuidad UE | OPEN |
| Roster/manifest y aprobación | OPEN / NOT MATERIALIZED |
| A/B roster scope | OPEN explícito por DEC-C10-096 |
| UE–UA–cluster | OPEN |
| Mecanismo de asignación Z | OPEN |
| Interferencia/exposición/carryover | OPEN |
| Mapping UE→U_G root exacto | UNKNOWN |
| Contrato package B1/Need | Propuesto, no aprobado |
| Parámetros de observación, fuentes y error | OPEN |
| Soporte truth 1/0 en cohorte | No evaluado; requiere roster |
| Tamaño, precisión y potencia E1/E2 | OPEN |
| Estimandos/identificación, sensibilidad y análisis | No completamente cerrados |
| Analyzer schemas/enums y proyección Need→PE | Propuestos/condicionales; no congelados |
| Implementación, firewall y validación estática | No autorizados/no implementados |

**Respuesta sobre proximidad:** no estamos todavía cerca de Design Freeze ni de implementación científica. Se han cerrado decisiones locales importantes (truth Need, cohorte como censo, identidad lógica B1/instancia y varias distinciones analíticas), pero faltan decisiones estructurales que pueden cambiar población, aleatorización, dependencia, estimandos y materialización. Implementar ahora fijaría supuestos no autorizados.

El trabajo está más cerca de poder producir una **lista integrada y finita de decisiones pendientes** que de un diseño congelable. La prioridad es resolver las decisiones que afectan a identificación causal; no seguir ampliando documentación periférica.

## 7. Decisiones que requieren al responsable científico

Gate 117 no elige por el responsable. Las cuestiones que requieren decisión explícita son:

1. **A/B:** roster separado por escenario o roster conjunto. Justificar si A/B son universos distintos o escenarios sobre la misma población.
2. **UE identity:** confirmar si `ue_id` solo necesita unicidad dentro del roster/package version o si debe persistir entre versiones/escenarios; si persiste, definir matching/sucesión/replay sin colisiones.
3. **Assignment:** declarar UE=UA o definir UA/cluster y mapping; solo después fijar mecanismo Z e inferencia.
4. **Interference:** declarar el régimen relevante (no interferencia defendible, exposición parcial/modelada, cluster, pools/recursos compartidos o carryover) y qué contrastes permite.

No se pide crear IDs, roster o tablas ahora. Las opciones se deben decidir a partir de la pregunta causal primaria y del DGP, no de conveniencia de serialización.

## 8. No-governance drift y autorización

- No crear nuevos IDs, namespace sintético, roster, manifiesto físico ni matching entre A/B.
- No elegir A/B ni equiparar UE=UA/cluster.
- No asumir aleatorización individual, SUTVA, ausencia de interferencia o independencia.
- No derivar mapping UE→U_G root de la instancia B1.
- No modificar DEC-C10-095/096 ni las decisiones de identidad B1.
- No alterar C0, U_G, main, RMA, Evidence→Claim Matrix o STATUS.
- No implementar, materializar, ejecutar validadores, código, tests, workflows, simulaciones, estimaciones, calibraciones ni experimentos.

**Dictamen final:** `GATE_117_HISTORICAL_RECONSTRUCTION_COMPLETE / UE_NAMESPACE_AND_CROSS_VERSION_CONTINUITY_OPEN / A_B_ROSTER_CHOICE_OPEN_BY_DEC_C10_096 / UE_UA_CLUSTER_ASSIGNMENT_AND_INTERFERENCE_OPEN / DESIGN_FREEZE_NOT_NEAR / IMPLEMENTATION_NOT_AUTHORIZED / NO_NEW_ID / NO_SCHEMA_CHANGE / NO_EXECUTION`.

**Siguiente operación:** Gate 118 — convertir los cuatro bloqueos estructurales anteriores en una matriz de decisiones causales mínima, rastreada a los estimandos ITT/mediación/residual y al DGP D2 prioritario. Separar lo que exige decisión del responsable de lo que puede cerrarse por reconstrucción; no pedir decisiones de formato si no alteran identificación.

**Gobernanza:** PR #116 permanece Draft. `scientific_execution=false`; `execution_authorized=false`.
