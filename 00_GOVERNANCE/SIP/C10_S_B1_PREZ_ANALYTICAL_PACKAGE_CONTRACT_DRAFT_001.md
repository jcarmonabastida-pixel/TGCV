# C10-S — Contrato del paquete analítico B1/Need_preZ

**ID:** C10-S-B1-PREZ-ANALYTICAL-PACKAGE-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** DOCUMENTARY_SPECIFICATION / PACKAGE_REPRESENTATION_NOT_APPROVED / OBSERVATION_RULES_ACCEPTED_BY_DEC-C10-097 / SOURCE_CLASSES_AND_PARAMETERS_OPEN / NOT_IMPLEMENTED / NOT_MATERIALIZED / NOT_EXECUTED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)  
**Precedencia:** DEC-C10-095 (truth/exclusion composition); DEC-C10-096 (validation census/task boundary); DEC-C10-097 (observation/coverage model); DEC-C10S-B1-UNIT-001; DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001; DEC-C10S-B1-OPPORTUNITY-CARDINALITY-001; DEC-C10-061/068/069; `C10_S_B1_PREZ_MINIMUM_DGP_MATERIALIZATION_CONTRACT_DRAFT_001.md`; `C10_S_B1_PREZ_DGP_U_G_COMPATIBILITY_AUDIT_DRAFT_001.md`; protocolo U_G de evidencia/procedencia/adjudicación.

## 1. Objeto y decisión de representación propuesta

Este contrato define la representación lógica del expediente B1/Need_preZ para separar: (a) truth estipulada por el generador; (b) evidencia pre-Z producida por un modelo de observación; (c) adjudicaciones observadas E1/E2; y (d) evaluación truth-versus-observed posterior al sellado.

**Propuesta:** mantener el expediente como paquete analítico B1/Need, versionado y separado de U_G y de la Evidence→Claim Matrix. No es una nueva clase de grafo, no amplía los seis destinos tipados de DEC-C10-061 y no crea una FK polimórfica en U_G. Los registros de evidencia pueden reutilizar los conceptos de provenance del protocolo U_G, pero el paquete no presume que CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT o ADJUDICATION_REGISTER admitan B1/UE/Need como target.

La decisión de representación queda propuesta, no aprobada. No se crean todavía tablas físicas, ficheros de datos, IDs de unidad, truth, fuentes ni adjudicaciones.

## 2. Límites semánticos

`Need_preZ` es la existencia del objetivo funcional basal de B1 definido en el contrato de adjudicación vigente. No equivale a demanda, elegibilidad, necesidad de recursos, oportunidad estandarizada, petición, admisión, procesamiento, respuesta, instalación, accesibilidad, Reach, Outcome ni Value.

La truth se ancla en t−1; Z ocurre en t0. Ningún dato post-Z puede modificar retrospectivamente Need_preZ. Una B1 por UE y una instancia lógica de servicio propia/versionada por UE son las cardinalidades de diseño ya aceptadas; los IDs concretos solo podrán generarse a partir de un roster aprobado.

## 3. Arquitectura lógica del paquete

El paquete se compone de seis artefactos lógicos, que podrán materializarse en ficheros tabulares/serializados separados cuando exista autorización. Sus nombres son roles de artefacto, no nombres de nuevas tablas U_G.

| Artefacto lógico | Contenido | Acceso |
|---|---|---|
| `PACKAGE_MANIFEST` | Identidad/versiones del paquete, hashes, esquema, roster y contratos referenciados | Generador y evaluador |
| `UNIT_BINDING` | UE↔B1↔contrato/instancia de servicio↔ancla basal↔evento Z | Generador; campos no sensibles para adjudicadores |
| `TRUTH_LEDGER` | Truth basal y regla generadora por unidad | Generador; evaluador solo después del sellado de adjudicación |
| `EVIDENCE_LEDGER` | Fuentes sintéticas observables, contenido, provenance, alcance, disponibilidad y lineage | Analyzer/adjudicadores |
| `ADJUDICATION_LEDGER` | Salidas separadas E1/E2, discrepancias y resolución conforme al protocolo | Adjudicadores; evaluador tras sellado |
| `EVALUATION_LEDGER` | Comparación truth/observed, métricas y diagnósticos de clasificación | Evaluador solamente |

La cobertura se representa dentro del manifiesto de evidencia y mediante registros de alcance por unidad/dimensión; no se interpreta como identidad de target. Los artefactos pueden implementarse como ficheros lógicos separados, pero no se fija aquí formato físico, motor, rutas ni tecnología.

## 4. Contrato mínimo de identidad y referencias

### 4.1 Claves de paquete

- `package_id`, `package_version`, `schema_version`.
- `dgp_spec_id`, `dgp_spec_version`, `dgp_code_commit` (solo cuando exista implementación autorizada).
- `roster_id`, `roster_version`, `roster_digest`.
- Referencias versionadas y hashes de los contratos B1, servicio, temporalidad, observación y adjudicación aplicables.

### 4.2 Claves por unidad

- `ue_id`: unidad experimental.
- `b1_id`: B1 vinculada unívocamente a UE.
- `contract_id`, `contract_version`: contrato lógico de servicio.
- `instance_id`, `instance_version`: instancia específica de esa UE.
- `baseline_record_id`: ancla basal inmutable en t−1.
- `z_event_id`: evento Z en t0, posterior al ancla.

Todas las referencias deben resolver dentro del mismo paquete/versión y respetar las cardinalidades aceptadas. No se permite reutilizar el ID ejemplar del servicio como `instance_id` de todas las unidades. No se asigna ningún valor concreto en este contrato.

## 5. Truth reservada: TRUTH_LEDGER

Cada unidad tiene exactamente un registro de truth basal por versión de paquete y baseline:

- `ue_id`, `b1_id`, `baseline_record_id`;
- `need_truth_state ∈ {1,0,?}`;
- `truth_rule_id`, `truth_rule_version`;
- `truth_basis_ref`: referencia a la regla/estipulación generadora, no a evidencia observada;
- `truth_generated_at`, `truth_sealed_at`;
- `truth_record_digest`.

La regla debe estipular el objetivo funcional de B1 antes de Z. No puede usar Z, política D2, provisión, instalación, C_dep, A_f, ΔT_acc, Reach, petición, admisión, procesamiento, ejecución, Outcome o Value.

**No-default:** el generador no puede asignar `1` a todas las unidades por definición, por pertenecer al microdominio, por compartir el servicio lógico o por recibir una oportunidad estandarizada. Tampoco puede asignar `0` por ausencia de petición, evidencia o actividad. El mecanismo de generación de truth se rige por DEC-C10-095: estipulación explícita, versionada y reservada por B1/UE, con derivación determinista reproducible a partir de esa estipulación; no se emplea generador estocástico de Need en el núcleo confirmatorio.

Para evaluar clasificación binaria y sus errores, la cohorte de validación definida ex ante debe contener truth=1 y truth=0. DEC-C10-095 establece que, si falta una clase, se declara SUPPORT_FAILURE / DESIGN_BLOCKED, sin reparación post hoc. No se fija balance, proporción, prevalencia, soporte por brazo/estrato ni representatividad poblacional. Truth=? conserva su significado de indeterminación semántica genuina y se informa separadamente. No se fija aquí ninguna tasa ni distribución. `?` solo expresa indeterminación estipulada por la propia definición generadora, no falta de evidencia observacional.

## 6. Evidencia observacional: EVIDENCE_LEDGER

La evidencia se genera mediante un **modelo de observación separado** de la truth ledger. Puede depender de la truth como causa generadora de la disponibilidad/contenido de una declaración, pero no debe copiar el campo `need_truth_state`, su etiqueta ni su referencia al paquete visible al adjudicador. El adjudicador recibe artefactos y contenido probatorio, no la etiqueta de truth ni variables potenciales.

Cada fuente tendrá, como mínimo:

- `evidence_id`, `package_id`, `ue_id`, `b1_id`;
- `source_class`/tipo concreto y versión;
- `claim_content`: contenido semántico de la fuente, no una etiqueta automática truth=1/0;
- `source_authority`/rol, emisor sintético, origen y método de generación/captura;
- `service_binding` cuando sea pertinente: contrato/instancia/versiones;
- `event_time`, `capture_time`, zona horaria y orden respecto de t−1/t0;
- `scope_id`, universo de fuentes esperado, examinadas, válidas, excluidas y opacas;
- `availability_status ∈ {AVAILABLE,MISSING,CONFLICTING}`;
- `integrity_digest`, lineage, transformaciones, limitaciones y `evidence_record_digest`.

La fuente debe referirse semánticamente al objetivo basal de B1 para respaldar Need. Identidad del servicio, ENABLED/PROFILE, IAM, ACL, SBOM, snapshots técnicos o contratos genéricos pueden acreditar identidad/configuración/estado técnico, pero no demuestran por sí solos que B1 tenga ese objetivo.

El modelo de observación debe especificar separadamente los mecanismos —sin asignar aún parámetros— de: emisión/ausencia de declaración, sensibilidad semántica, falsos positivos, falsos negativos, ambigüedad, conflicto, corrupción, error temporal, pérdida/captura y cobertura. Los errores pueden depender de características basales declaradas ex ante; no pueden depender de Z ni de variables post-Z/Outcome/Value. No se presume independencia entre fuentes.

## 7. Adjudicación observada: ADJUDICATION_LEDGER

Cada evaluador trabaja solo con el subconjunto de evidencia autorizado, reglas públicas versionadas, identity binding no sensible y alcance/cobertura. No tiene acceso a TRUTH_LEDGER ni a variables post-Z.

Campos mínimos por evaluación:

- `adjudication_case_id`, `ue_id`, `b1_id`, `baseline_record_id`;
- `evaluator_id`, `evaluator_role ∈ {E1,E2}`, `adjudication_rule_version`;
- `need_observed_state ∈ {1,0,?}`;
- `evidence_ids`, `coverage_scope_refs`, `rationale`;
- `unknown_reason` y/o `conflict_reason`;
- `evaluated_at`, `sealed_at`, `output_digest`.

E1 y E2 son independientes: no comparten truth, no consultan la salida del otro antes de sellar y no acceden a Outcome/Value. La resolución posterior conserva ambas salidas, el desacuerdo y la regla aplicada; nunca sobrescribe los registros originales.

Reglas obligatorias:
- observed=1 exige fuente afirmativa, admisible, semánticamente alineada, vinculada a B1/UE y pre-Z.
- observed=0 exige evidencia afirmativa de no pertenencia del objetivo a la especificación basal dentro de un universo cerrado, pertinente, versionado y con cobertura negativa suficiente.
- ausencia de documento, campo, solicitud, log o resultado de búsqueda no equivale a observed=0.
- configuración técnica sin fuente del objetivo no permite observed=1 ni observed=0.
- conflicto, identidad ambigua, temporalidad dudosa, cobertura insuficiente o fuente no admisible producen observed=?.

## 8. Cobertura y denominadores

La cobertura se calcula por unidad y dimensión de afirmación, no mediante un porcentaje global que oculte huecos. Cada alcance debe declarar universo, versión, custodio/autoridad, fuentes esperadas, examinadas, válidas, excluidas, opacas, método de enumeración y limitaciones.

Estados:
- `NONE`: ninguna inspección material válida para la dimensión;
- `PARTIAL`: inspección incompleta o con superficies opacas;
- `COMPLETE`: universo pertinente cerrado y cubierto según regla versionada.

`COMPLETE` no implica automáticamente observed=0: solo permite evaluar la suficiencia de una afirmación negativa cuando además existe evidencia afirmativa y autoridad adecuada. El roster aprobado determina el denominador de unidades; no se inventa un denominador antes de aprobarlo.

## 9. Sellado, permisos y flujo de información

| Fase | Generador | Analyzer/adjudicadores E1/E2 | Evaluador |
|---|---|---|---|
| Estipulación basal | Crear truth y regla | Sin acceso | Sin acceso hasta fase de evaluación |
| Generación de fuentes pre-Z | Crear fuentes según modelo de observación | Reciben solo ledger observable | Sin truth expuesta |
| Adjudicación | No interviene en la clasificación | Adjudicar de forma independiente y sellar | No intervenir |
| Sellado | Sellar truth/evidencia/salidas con digests | Sellar sus salidas | Verificar sellos |
| Evaluación | No reescribe | Sin cambios | Comparar truth y observed tras sellado |

El control de acceso debe ser técnico, no una mera convención documental: separación de ubicaciones/artefactos, permisos mínimos, export observable sin truth, logs de acceso y verificación automatizada de que el Analyzer no puede resolver referencias a TRUTH_LEDGER. La ubicación segura, cifrado, gestión de claves y retención se definirán en el contrato de implementación; no se guardarán secretos en GitHub.

## 10. Integridad, reproducibilidad y versionado

- Cada artefacto tiene schema/version y digest; el manifiesto contiene hashes de todos los artefactos y sus dependencias.
- La truth se sella antes de Z; la evidencia declara event_time pre-Z y capture_time; la adjudicación se sella antes de abrir truth al evaluador.
- Los cambios de regla, roster, contrato, generador o modelo de observación crean nueva versión; no se sobrescriben registros históricos.
- Las referencias cruzadas deben resolverse y las cardinalidades validarse; claves duplicadas, huérfanas, versiones incompatibles, orden temporal inválido o digest inconsistente bloquean el paquete.
- El replay, si se autoriza, debe reproducir el mismo paquete a partir de las versiones/semillas autorizadas; la semilla y el método de generación se almacenan en el manifiesto restringido cuando puedan revelar truth.
- La evaluación debe reportar matriz de confusión y cobertura/indeterminación separadas; sensibilidad, especificidad, valores predictivos, calibración o métricas agregadas solo cuando el soporte y denominadores estén definidos. Los casos ? no se convierten en errores ni aciertos binarios por defecto.

## 11. Pruebas contractuales previas a implementación

Las pruebas siguientes son requisitos de diseño, no pruebas ejecutadas:

1. **PKG-01** — una B1 por UE y una instancia de servicio única/versionada por UE; ninguna clave compartida por accidente.
2. **PKG-02** — truth generada/sellada en t−1, antes de Z en t0.
3. **PKG-03** — truth incluye mecanismo explícito; no existe asignación por defecto Need=1 ni regla de Need=0 por silencio.
4. **PKG-04** — escenarios de evaluación binaria contienen soporte truth=1 y truth=0, sin fijar prevalencias aquí.
5. **PKG-05** — la evidencia se genera por modelo de observación separado y no copia/exhibe la etiqueta de truth.
6. **PKG-06** — manipular Z/política/post-Z no altera truth ni fuentes pre-Z ya generadas.
7. **PKG-07** — el Analyzer no puede leer truth, potenciales ni salida del otro adjudicador antes de sellar.
8. **PKG-08** — ausencia de evidencia/solicitud no produce observed=0.
9. **PKG-09** — observed=0 exige evidencia afirmativa y cobertura negativa suficiente.
10. **PKG-10** — evidencia técnica del servicio sin contenido sobre objetivo B1 no permite adjudicar Need.
11. **PKG-11** — conflicto, ambigüedad de identidad, temporalidad o versión producen ?.
12. **PKG-12** — E1/E2 independientes; desacuerdo preservado y resolución trazable.
13. **PKG-13** — evaluación truth-versus-observed solo después de sellar las adjudicaciones.
14. **PKG-14** — hashes, FK lógicas, cardinalidades, versiones y lineage se validan; fallos bloquean el paquete.

## 12. Dependencias abiertas y límites

| Dependencia | Estado |
|---|---|
| Regla funcional de Need_preZ | Definida documentalmente en contrato B1 |
| Unidad B1/UE y servicio por UE | Decisiones de diseño aceptadas; roster/IDs no materializados |
| Representación separada del paquete | Propuesta de este documento; requiere aceptación |
| Mecanismo de truth por unidad | ACCEPTED BY DEC-C10-095: reserved explicit stipulation per B1/UE + deterministic mapping; no stochastic Need generation |
| Reglas operativas generales de observación/cobertura | ACCEPTED BY DEC-C10-097; no parametrizadas |
| Clases concretas de fuentes, universo esperado y dependencias de observación | OPEN; no materializados ni parametrizados |
| Fuentes sintéticas y cobertura por unidad | No materializadas; cobertura NONE |
| Reglas/roles E1/E2 | Definidos documentalmente; ninguna adjudicación realizada |
| Seguridad técnica y control de acceso | Requisitos definidos; no implementados |
| Esquema físico/formatos/ubicación | OPEN; no seleccionados |
| DGP temporal completo, soporte, interferencia, estimandos y Value | Siguen sujetos a sus propios gates |

## 13. Dictamen

`B1_NEED_ANALYTICAL_PACKAGE_SPECIFIED / SEPARATE_FROM_UG / NO_NEW_UG_TARGET / TRUTH_RULE_ACCEPTED / OBSERVATION_OPERATIONAL_RULES_ACCEPTED / SOURCE_CLASSES_AND_PARAMETERS_OPEN / NO_ROSTER / NO_RECORDS / NOT_IMPLEMENTED / NOT_EXECUTED`.

El contrato propone una arquitectura de expediente que conserva la integridad tipada U_G y hace verificable la separación truth/evidencia/adjudicación. No prueba que Need sea adjudicable con las fuentes actualmente disponibles ni selecciona parámetros para el DGP. No autoriza materialización, implementación, simulación, estimación, ejecución ni Design Freeze.

**Decisiones aplicables:** DEC-C10-095 acepta el mecanismo de estipulación y el gate de soporte binario; DEC-C10-096 acepta el censo de validación y la frontera E1/E2 vs Analyzer PE; DEC-C10-097 acepta las reglas operativas de observación/cobertura. Ninguna aprueba roster ni materialización. **Autorización:** `scientific_execution=false`; `execution_authorized=false`.



### 6.1 Especialización lógica del canal S7 tras DEC-C10-098

El modelo de observación se interpreta conforme a la estructura lógica propuesta en §14 de C10_S_B1_PREZ_OBSERVATION_MECHANISM_AND_COVERAGE_RULES_RECONCILIATION_DRAFT_001.md. En particular, el campo agregado availability_status descrito en §6 no puede sustituir ni colapsar emisión, contenido semántico, captura/retención, integridad, autoridad, temporalidad, binding y cobertura. Su eventual codificación física deberá preservar esos estados diferenciados dentro de los artefactos lógicos ya definidos.

Para la oportunidad única S7 por UE:
- la oportunidad esperada es ex ante y no garantiza emisión;
- el contenido, cuando existe emisión, expresa inclusión, exclusión focal, ambigüedad o contradicción interna;
- la no emisión y la pérdida de una emisión no son exclusión;
- la autenticidad del mandato B1 no implica exactitud del contenido;
- truth=? no obliga a producir contenido ambiguo y permanece fuera de métricas binarias de exactitud;
- E1/E2 adjudican Need por separado; Analyzer PE conserva su tarea analítica distinta.

La factorización condicional que se utilice en el DGP debe preservar dependencias posibles; ninguna independencia se infiere de la separación conceptual de etapas. No se fijan parámetros, probabilidades ni schema físico. Esta especialización es una reconciliación de diseño, no una aprobación de representación física, materialización o ejecución.
