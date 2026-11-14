# C10-S — B1: contrato mínimo de materialización DGP de Need_preZ

**ID:** C10-S-B1-PREZ-DGP-MATERIALIZATION-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** DOCUMENTARY_SPECIFICATION / NOT_APPROVED / NOT_IMPLEMENTED / NOT_MATERIALIZED / NOT_EXECUTED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)  
**Precedencia:** DEC-C10S-B1-UNIT-001; DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001; DEC-C10S-B1-OPPORTUNITY-CARDINALITY-001; DEC-C10-068/069; C10_S_B1_PREZ_ADJUDICATION_AND_CONSEQUENCE_RECONCILIATION_DRAFT_001; C10_S_B1_PREZ_EVIDENCE_SOURCE_INVENTORY_AND_COVERAGE_AUDIT_DRAFT_001; protocolo U_G de procedencia/adjudicación.

## 1. Objeto y límites

Este contrato especifica el paquete mínimo que deberá separar, para cada unidad sintética, (a) la verdad basal de `Need_preZ` estipulada por el generador, (b) las fuentes/evidencias pre-Z que recibe el procedimiento de observación y adjudicación y (c) la adjudicación observada. Su finalidad es hacer implementable la separación truth/observed sin crear todavía registros ni ejecutar el DGP.

No redefine el propósito B1 ni el servicio lógico aceptados; no convierte Need en elegibilidad P*, accesibilidad, C_dep, demanda de recursos o evento de petición. No selecciona prevalencia de Need, tasas de error, tamaño muestral, mecanismo de missingness, semilla, aleatorización, estimando, dimensiones V_j, horizonte o parámetros. No modifica el DGP temporal completo, que sigue sujeto a sus gates propios.

## 2. Unidad e identidad: claves lógicas, no IDs inventados

La unidad de referencia es una entidad B1 por UE. La UE sigue siendo la instancia sintética completa y unidad de asignación candidata; B1 es su referente de objetivo basal y consecuencia. Cada UE se vincula a una instancia lógica de servicio propia, única y versionada.

El paquete por unidad deberá resolver, cuando exista roster aprobado:

- `ue_id`: identidad de la unidad experimental sintética;
- `b1_id`: identidad de la entidad beneficiaria/solicitante, con relación unívoca a `ue_id`;
- `contract_id` y `contract_version`: contrato común de servicio;
- `instance_id` y `instance_version`: instancia específica de la UE;
- `baseline_record_id`: registro basal inmutable que ancla objetivo, tiempo y versiones;
- `z_event_id`: referencia al evento de asignación, estrictamente posterior al ancla basal.

No se asignan valores concretos a estas claves en este documento. Los IDs se generan solo a partir de un roster cerrado y versionado. La instancia ejemplar documental `C10S-SVC-REQUEST-PROCESSOR-001` no se reutiliza como instance_id de todas las UE.

## 3. Tres capas obligatoriamente separadas

### 3.1 Truth reservada del DGP

El generador conserva, fuera del entorno visible al Analyzer, al menos:

- `need_truth_state ∈ {1,0,?}`;
- `need_truth_rule_version`;
- `need_truth_baseline_time`;
- `need_truth_basis_ref` (referencia a la estipulación generadora, no a evidencia observada);
- `ue_id` y `b1_id` asociados.

La truth se fija antes de Z y no puede depender de Z, de la política D2, provisión/instalación, C_dep, A_f, ΔT_acc, Reach, solicitud, admisión, procesamiento, ejecución, Outcome o Value. El estado ? es admisible si la propia estipulación basal del DGP deja el objetivo indeterminado; no equivale a missingness observacional.

La regla generadora debe ser explícita y reproducible. No se permite establecer Need=1 por defecto, inferirlo de la función genérica del servicio ni derivarlo de que el experimento ofrezca una oportunidad estandarizada.

### 3.2 Evidencia observacional pre-Z

El generador o la capa de observación produce un paquete separado de registros que simula lo que un adjudicador podría consultar. Cada artefacto de evidencia deberá portar o resolver:

- `evidence_id`, clase/tipo de fuente y versión;
- `ue_id`, `b1_id` y binding exacto al servicio cuando sea pertinente;
- contenido probatorio concreto y afirmación que respalda;
- emisor/rol o autoridad sintética, origen y método de generación/captura;
- timestamp y zona horaria, con orden demostrable anterior a Z;
- integridad/hash y lineage;
- universo/alcance, fuentes esperadas, examinadas, válidas, excluidas y opacas;
- limitaciones, estado AVAILABLE/MISSING/CONFLICTING y referencia a regla de adjudicación.

La evidencia de identidad o configuración del servicio (IAM, manifiesto, snapshot, contrato) puede demostrar identidad, versión o estado técnico; por sí sola no demuestra que B1 tenga el objetivo basal. Para Need hace falta evidencia cuyo contenido semántico se refiera al objetivo de B1.

### 3.3 Adjudicación observada

El adjudicador recibe solo el paquete de evidencia permitido, las reglas públicas versionadas y el alcance/cobertura pertinente. Produce `need_observed_state ∈ {1,0,?}`, rationale, regla aplicada, evidencia enlazada, unknown/conflict reason, evaluador y timestamp. E1/E2 permanecen independientes; la adjudicación no puede consultar `need_truth_state`.

El evaluador autorizado compara observed con truth solo después de sellar la salida del adjudicador/Analyzer. Truth nunca se incorpora a EVIDENCE_REGISTER ni a los registros que consume el Analyzer.

## 4. Reglas probatorias de 1/0/?

| Truth estipulada | Evidencia observada necesaria | Adjudicación permitida |
|---|---|---|
| 1 | Declaración/objetivo basal afirmativo, semánticamente alineado con §3 de B1, vinculado a la unidad y versionado antes de Z | 1 si identidad, temporalidad, autoridad y contenido son suficientes; en otro caso ? |
| 0 | Evidencia afirmativa de que el objetivo definido no forma parte del propósito basal de esa B1, dentro de un alcance documental/declarativo cerrado y versionado | 0 solo si la cobertura negativa y la autoridad son suficientes; en otro caso ? |
| ? | La propia especificación generadora no determina el objetivo | ? como truth; la observación se adjudica por separado |

Reglas negativas no negociables:

1. Ausencia de documento, campo, registro, solicitud o traza no equivale a Need=0.
2. Un roster completo de fuentes sin una declaración de objetivo no demuestra por sí mismo que el objetivo no exista.
3. Una configuración ENABLED/PROFILE o un snapshot técnico no demuestra Need=1 ni Need=0.
4. Una oportunidad estandarizada, Request_attempt, received, admitted, processing o response no constituye prueba de Need.
5. Un documento post-Z no puede retrotraerse como prueba basal salvo que sea una copia verificable de una fuente pre-Z cuyo origen, fecha e integridad se acrediten.
6. Conflicto no resuelto, identidad ambigua, temporalidad incierta o cobertura insuficiente producen ?.

La cobertura negativa puede respaldar 0 únicamente cuando la definición de la fuente/registro haga que el universo relevante sea cerrado y la evidencia afirmativa permita descartar el objetivo, no por simple silencio. Si no hay tal mecanismo, el estado observado correcto es ?.

## 5. Paquete mínimo por unidad y condiciones de suficiencia

El expediente lógico de una unidad no se considera listo para adjudicación hasta que incluya:

1. **Identity binding:** UE↔B1↔service instance exactos, versionados y no ambiguos.
2. **Baseline anchor:** registro inmutable con instante/orden pre-Z y contrato/instancia/versión aplicables.
3. **Need-bearing source:** al menos una fuente cuyo contenido se refiera directamente al objetivo basal de B1; para Need=0, fuente afirmativa y alcance cerrado, no mero registro vacío.
4. **Source manifest:** universo de fuentes esperado para esa afirmación, custodio/autoridad, disponibilidad, examinadas, válidas, limitaciones y exclusiones.
5. **Evidence lineage:** método, timestamp, integridad, transformación y vínculo CLAIM_EVIDENCE_LINK cuando exista evidencia admisible.
6. **Independent adjudication:** E1 y E2, discrepancias y adjudicación conforme al protocolo U_G.

Si falta un elemento crítico, no se bloquea la existencia de la unidad ni se inventa una fuente: se conserva observed=? y se explica el motivo. La cobertura se informa por dimensión y unidad; no se agrega a un porcentaje global. El denominador solo se fija cuando el roster/universo versionado está aprobado.

## 6. Mecanismo de generación y medición que deberá especificar el DGP

Antes de implementar se deberá declarar, sin valores predeterminados implícitos:

- cómo se asigna `need_truth_state` entre unidades y si existen estratos/escenarios;
- qué contenido semántico de la declaración representa cada estado;
- qué tipos de fuentes observacionales se generan por estado y con qué autoridad/temporalidad;
- qué mecanismos de disponibilidad, omisión, corrupción, ambigüedad y conflicto se evalúan;
- si los errores de observación pueden depender de características basales y cómo se evita que dependan de Z/Outcome/Value;
- cómo se mide la cobertura negativa y cuándo es imposible adjudicar 0;
- cómo se sella truth, evidencia, salida de Analyzer y evaluación.

No se fija aquí prevalencia, sensibilidad, especificidad, correlación entre fuentes ni tasas de missingness. Esos parámetros requieren justificación y análisis de sensibilidad separados; no se eligen para hacer coincidir observed con truth.

## 7. Pruebas de contrato obligatorias antes de cualquier ejecución

La futura implementación deberá probar, al menos:

- **PREZ-T01:** truth sellada antes de Z y hash/versión reproducibles.
- **PREZ-T02:** cambiar Z/política post-baseline no altera Need truth ni fuentes pre-Z.
- **PREZ-T03:** Analyzer no puede leer truth ni potenciales.
- **PREZ-T04:** ausencia de documento/solicitud no produce observed=0.
- **PREZ-T05:** configuración técnica sin fuente del objetivo no produce observed=1/0.
- **PREZ-T06:** fuente post-Z no se acepta como basal sin lineage pre-Z verificable.
- **PREZ-T07:** conflicto o identidad/versionado ambiguos producen ?.
- **PREZ-T08:** observed=0 exige evidencia afirmativa y cobertura negativa suficiente.
- **PREZ-T09:** E1/E2 no leen truth ni Outcome/Value y conservan discrepancias.
- **PREZ-T10:** evaluación truth-vs-observed ocurre solo después de sellar la salida observada.

Estas son pruebas requeridas, no pruebas existentes ni ejecutadas.

## 8. Reutilización del esquema y no duplicación

La materialización futura reutilizará los artefactos existentes:
- `EVIDENCE_REGISTER` para procedencia de cada fuente real/sintética;
- `CLAIM_EVIDENCE_LINK` para vincular evidencia a la afirmación Need_preZ y unidad exacta;
- `COVERAGE_REGISTER` con universo/denominador versionado por dimensión;
- `EVALUATOR_REGISTER` y `ADJUDICATION_REGISTER` para E1/E2 y resolución;
- almacenamiento separado y restringido del generador para truth DGP.

No se crea una tabla U_G nueva, no se añade una clase de objeto, no se expone truth en la plantilla ni se duplican registros de fuente en NODE/PREDICATE. La afirmación Need_preZ es una afirmación sobre B1; el binding al servicio es contexto de identidad y no una inferencia causal de Need.

## 9. Dependencias y bloqueos que permanecen

| Dependencia | Estado |
|---|---|
| Propósito funcional B1 y definición conceptual Need_preZ | Aceptados/definidos como contrato de trabajo |
| Una B1 por UE y una instancia lógica de servicio propia/versionada por UE | Decisión de diseño aceptada; roster e IDs no materializados |
| Oportunidad estandarizada N=1 por UE | Configuración primaria candidata aceptada; no es demanda natural ni evidencia Need |
| Truth DGP por unidad y mecanismo de asignación de estados | OPEN; no fijado |
| Fuente observacional Need-bearing y mecanismo de medición | OPEN; no materializado |
| Prevalencia, error, missingness y sensibilidad | OPEN; no parametrizados |
| Universo/denominador y cobertura por unidad | NONE / UNKNOWN hasta roster y fuentes |
| IAM/snapshots técnicos pre-Z | No materializados; no sustituyen evidencia del objetivo |
| E1/E2 y adjudicación | Protocolo definido; ninguna evaluación realizada |
| DGP temporal completo, aleatorización, soporte y gates confirmatorios | Siguen abiertos según sus artefactos rectores |

## 10. Dictamen

`NEED_PREZ_MATERIALIZATION_CONTRACT_DOCUMENTED / TRUTH_RULE_NOT_PARAMETERIZED / OBSERVATION_MODEL_NOT_PARAMETERIZED / NO_ROSTER / NO_EVIDENCE_ROWS / COVERAGE_NONE / NOT_IMPLEMENTED / NOT_EXECUTED`.

Este contrato define qué habrá que materializar y cómo impedir circularidad y filtración; no demuestra que existan fuentes ni que el constructo sea adjudicable en cada unidad. No selecciona parámetros ni genera casos. La siguiente revisión debe comprobar compatibilidad de este contrato con el DGP temporal/roles y con el esquema U_G antes de proponer fixtures o implementación.

**Autorización:** `scientific_execution=false`; `execution_authorized=false`. No se autoriza creación de roster, truth por unidad, fuentes, snapshots, fixtures, implementación, simulación, estimación, experimento ni Design Freeze.
