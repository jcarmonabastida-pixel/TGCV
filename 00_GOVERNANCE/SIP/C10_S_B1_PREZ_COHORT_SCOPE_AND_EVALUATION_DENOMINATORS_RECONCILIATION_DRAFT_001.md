# C10-S — Alcance de cohorte B1/Need_preZ y denominadores de evaluación

**ID:** C10-S-B1-PREZ-COHORT-SCOPE-DENOMINATORS-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** DOCUMENTARY_RECONCILIATION / COHORT_CENSUS_SCOPE_ACCEPTED_BY_DEC-C10-096 / ALIGNED_WITH_DEC-C10-095 / E1_E2_ONLY_FOR_NEED_ADJUDICATION / ROSTER_NOT_APPROVED / NOT_MATERIALIZED / NOT_EXECUTED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)

## 1. Pregunta y resultado de la reconciliación

DEC-C10-096 acepta cerrar la alternativa entre (a) censo del roster al que aplica el paquete y (b) subcohorte pre-Z: **la cohorte objetivo de validación Need_preZ será el censo de todas las UE incluidas en la versión aprobada del roster DGP/paquete B1 para la que se materialice el paquete analítico B1/Need**. No se selecciona una subcohorte adicional.

La pertenencia se determina por identidad, binding y alcance del roster antes de generar/abrir truth, evidencia o Z. La cardinalidad aceptada de una B1 por UE y una instancia lógica de servicio propia/versionada por UE fundamenta la aplicabilidad del paquete; no se usa Need ni observabilidad para decidirla. Si el diseño mantiene rosters A/B separados, se toma el roster exacto de la instancia DGP/paquete B1 aprobada; si aprueba un roster conjunto, se incluyen todas las UE a las que aplique el paquete. No se debe usar la expresión ambigua «variante B1» como sustituto de la identidad/versionado del roster.

Esta cohorte no equivale a cualquier roster C10-S, toda P*_{τ2}, P*_F ni al denominador ITT. La decisión no aprueba todavía el roster, no crea una población causal nueva ni autoriza materialización.

## 2. Por qué censo del roster B1 y no subcohorte

1. La unidad del paquete es B1/UE, con una B1 por UE y una instancia lógica de servicio vinculada/versionada por UE. No hay una razón conceptual documentada para muestrear unidades dentro de ese marco.
2. La selección de casos por truth, disponibilidad de evidencia, cobertura, resultado E1/E2 o respuesta del Analyzer sesgaría la evaluación del propio procedimiento.
3. Un censo conserva el flujo completo de unidades, incluidos truth=?, expedientes incompletos, salidas abstencionistas y bloqueos de integridad.
4. El requisito de soporte truth=1 y truth=0 se comprueba sobre el marco de validación definido; no se obtiene seleccionando después las unidades que facilitan las métricas.
5. Una subcohorte solo sería admisible si una restricción de diseño verificable la hace necesaria y su regla de selección se preespecifica sin usar truth, Z, evidencia/observabilidad, adjudicaciones, Analyzer ni variables post-Z. No hay ahora una justificación que la requiera.

## 3. Definición operacional de pertenencia y flujo

La cohorte objetivo comprende todas las UE del roster DGP/paquete B1 aprobado para la versión del paquete. La pertenencia se determina por roster/versionado, identidad y binding, antes de generar o abrir truth/evidencia y antes de Z. La regla no depende del estado de Need, la disponibilidad de fuentes ni los resultados de adjudicación.

Cada unidad debe permanecer visible en el flujo del paquete, con uno de estos estados de proceso (no son estados de truth):

- incluida en el roster y con identidad/binding íntegros;
- incluida, pero bloqueada por identidad, binding, referencia o integridad;
- truth válida 1/0/? sellada;
- evidencia observable NONE/PARTIAL/COMPLETE conforme al alcance aplicable;
- adjudicaciones E1 y E2 selladas, por separado;
- referencia al output PE del Analyzer solo si existe un estimando que lo requiera, conservada y evaluada fuera de la clasificación Need; no es un resultado del paquete de adjudicación B1/Need;
- evaluación abierta/sellada o no evaluable, con motivo explícito.

Un fallo de identidad, binding o integridad no se recodifica como truth=?, no se elimina silenciosamente del roster y no se convierte en error de clasificación. Se reporta como bloqueo del paquete/unidad; mientras no se resuelva, no puede declararse completada la evaluación confirmatoria censal. La ausencia o insuficiencia de evidencia tampoco excluye la unidad: es una condición que E1/E2 deben afrontar y registrar, normalmente como observed=? según el protocolo.

## 4. Tres objetos de evaluación, tres resultados separados

El objetivo de evaluación debe descomponerse en tareas que no se confundan:

### 4.1 Adjudicación B1/Need E1 y E2 — objetivo de esta cohorte

E1 y E2 reciben el mismo expediente observable autorizado y metadatos permitidos, sin acceso a TRUTH_LEDGER ni a metadatos reconstructivos, y sin ver la salida del otro. Cada salida se conserva y evalúa individualmente contra Need_truth DGP. La concordancia E1–E2 es un resultado adicional de fiabilidad, no un sustituto de exactitud respecto de truth.

### 4.2 Analyzer PE — fuera del objetivo de clasificación Need

El Analyzer PE no forma parte de la evaluación de clasificación Need ni se le atribuye una salida `need_observed_state`. El crosswalk de interfaz existente recomienda mantener su tarea de reconstrucción/estimación por constructo y estimando separada. Puede consumir una variable observada B1/Need únicamente cuando un contrato de estimando lo requiera explícitamente; eso no convierte a Analyzer en adjudicador Need ni incorpora E1/E2 como etiqueta de entrada por defecto.

### 4.3 Evaluación por el Evaluator B1/Need

El Evaluator B1/Need abre truth reservada solo después de que E1 y E2 hayan sellado sus salidas. Compara E1 y E2 por separado contra truth y conserva desacuerdos, abstenciones, errores y casos no evaluables. No reemplaza las salidas originales por consenso. La evaluación del Analyzer PE permanece bajo el Evaluator PE y sus propios oráculos por estimando/constructo.

No se introduce un séptimo artefacto: las salidas E1/E2 permanecen en ADJUDICATION_LEDGER y sus comparaciones con Need_truth en EVALUATION_LEDGER. El output Analyzer PE permanece en su objeto de salida/Artifact-Provenance Store PE, fuera de los seis artefactos B1/Need; solo podrá existir una referencia cruzada externa si un contrato de estimando la requiere.

## 5. Denominadores y reporting

Se deben informar al menos cuatro cantidades/flujo, sin colapsarlas:

1. **N roster B1:** todas las UE del roster DGP/paquete aprobado al que aplica B1/Need; no presupone que el roster se denomine «variante B1» ni que sea conjunto A/B.
2. **N integridad evaluable:** unidades con identidad, binding, baseline y truth ledger íntegros. Los bloqueos se informan aparte, con causa.
3. **N truth binaria:** unidades evaluables con truth=1 o truth=0. Este es el marco de cálculo de métricas binarias, condicionado a que ambas clases tengan soporte.
4. **N truth indeterminada:** unidades evaluables con truth=?; se informan por separado y no se imputan a 0/1.

Para cada adjudicador (E1 y E2) informar:
- cobertura/salida disponible respecto de N roster y N integridad evaluable;
- matriz de clasificación 1/0/? contra truth binaria;
- sensibilidad, especificidad y errores pertinentes con denominadores explícitos, si los contratos estadísticos fijan que son métricas aplicables;
- abstención, observed=?, error técnico y ausencia de salida como resultados diferenciados;
- comportamiento frente a truth=? por separado, sin medirlo como falso positivo/negativo binario;
- flujo de bloqueos técnicos y análisis de límites de generalización.

La evaluación del Analyzer PE no se incorpora a estos denominadores: conserva su salida PE y evaluación propia contra oráculos DGP por constructo/estimando.

No se calcularán métricas binarias únicamente sobre los casos en que E1/E2 emitieron 1/0 sin informar observed=?, ausencia de salida, fallo técnico y cobertura: hacerlo ocultaría el rendimiento operativo real. El rendimiento condicional a una clasificación emitida puede presentarse como análisis complementario, con su denominador y tasa de cobertura claramente indicados.

## 6. Relación con las poblaciones causales y con la asignación

Este alcance no modifica:

- P*_{τ2}, población primaria candidata de C1;
- P*_F, subpoblación secundaria de apertura funcional exclusiva;
- el denominador de cada ITT por variante/resultado/horizonte;
- unidad de asignación UA, unidad experimental UE, interferencia ni el mecanismo Z;
- las condiciones constitutivas de elegibilidad experimental.

Need_preZ no es criterio de pertenencia a P*_{τ2}, P*_F ni al denominador ITT. Tampoco se exige soporte truth=1/0 en cada brazo, estrato o población causal. Si se desea afirmar que la validez de la adjudicación E1/E2 se transporta a P*_{τ2}, P*_F o a otra población, habrá que informar el solapamiento, soporte y cobertura en esa población y justificar la transportabilidad; el resultado de la cohorte B1 no lo demuestra automáticamente. La transportabilidad del Analyzer PE se evalúa por separado conforme a sus estimandos y oráculos.

La truth se fija en t−1. Z, política D2, provisión, instalación, accesibilidad, Reach, trayectoria, ejecución, Outcome y Value no pueden determinar la pertenencia a la cohorte ni modificar truth.

## 7. Gate de soporte y reglas de bloqueo

Antes de una evaluación confirmatoria:

- el roster DGP/paquete al que aplica B1/Need debe estar aprobado, versionado y cerrado;
- la cohorte se congela como censo de ese roster antes de truth/evidencia/Z;
- deben existir casos válidos truth=1 y truth=0 en N integridad evaluable;
- ambas clases deben permanecer representadas en el denominador binario, sin reequilibrio posterior;
- truth=? se conserva y reporta separadamente;
- las salidas E1 y E2 deben estar selladas antes de abrir Need_truth; el Analyzer PE no forma parte de esta evaluación;
- la segregación de roles y el acceso del Evaluator deben estar verificados.

Si falta una clase binaria, el dictamen es SUPPORT_FAILURE / CONFIRMATORY_CLASSIFICATION_BLOCKED. No se crea una subcohorte de conveniencia, no se cambia truth, no se generan unidades ad hoc y no se fuerza balance. La suficiencia de N, precisión, potencia y estabilidad de métricas sigue pendiente del paquete estadístico P177/P178/P179/P182/P183; el soporte lógico de una unidad por clase no acredita suficiencia estadística.

## 8. Reconciliación con los artefactos existentes y gates restantes

Se reutilizan, sin sustituirlos:
- `C10_S_B1_PREZ_ANALYTICAL_PACKAGE_CONTRACT_DRAFT_001.md` — seis artefactos lógicos y separación Generator/Analyzer/Evaluator;
- `C10_S_B1_PREZ_TRUTH_COMPOSITION_AND_SUPPORT_REVIEW_DRAFT_001.md` — estipulación 1/0/? y soporte binario;
- `C10_S_B1_PREZ_VALIDATION_COHORT_POPULATION_CROSSWALK_DRAFT_001.md` — distinción respecto de P* e ITT;
- `C10_S_B1_PREZ_ADJUDICATION_AND_CONSEQUENCE_RECONCILIATION_DRAFT_001.md` — reglas observed y cegamiento E1/E2;
- `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md` — roles, temporalidad y firewall;
- `C10_S_TEST_CONTRACT_REGISTER_DRAFT_001.md` — contratos P177/P178/P179/P182/P183 y firewall;
- `C10_S_CLOSURE_SEQUENCE_AND_C1_ITT_WORKPLAN_001.md` — orden de cierre de paquetes: C1, Outcome/Value, C2, C3, C4, C5+DGP, estadística/Analyzer e implementación.

Gates todavía abiertos:
1. aprobación del roster DGP/paquete al que aplica B1/Need, con decisión explícita de si los rosters A/B son separados o conjuntos, identidad/versionado y cierre;
2. confirmación de que el paquete B1/Need cubre todas las UE de ese roster conforme a la cardinalidad B1/UE ya aceptada;
3. correspondencia final con PKG/PREZ tests existentes, evitando IDs duplicados;
4. suficiencia estadística, potencia y precisión para E1/E2;
5. verificación computacional del firewall Generator/Proyector/E1/E2/Evaluator B1;
6. generalización/transportabilidad de la adjudicación E1/E2 a poblaciones causales, solo si se pretende;
7. evaluación PE del Analyzer contra sus propios oráculos, independiente de la cohorte de clasificación Need.

## 9. Dictamen

**DECISIÓN ACEPTADA (DEC-C10-096):** censo de todas las UE del roster DGP/paquete aprobado al que aplica B1/Need como cohorte de validación; ninguna subcohorte por conveniencia. E1 y E2 se evalúan separadamente contra Need_truth DGP; Analyzer PE permanece fuera de la clasificación Need. Truth=?, evidencia insuficiente y bloqueos permanecen visibles. Los bloqueos de identidad/truth-integrity impiden declarar completa la evaluación censal hasta resolverse; no se eliminan unidades. P* e ITT no se alteran.

Este documento incorpora la decisión de alcance aceptada en DEC-C10-096; sigue siendo una reconciliación documental, no un contrato congelado ni una especificación física. No materializa roster, unidades, truth, evidencia, adjudicaciones, salidas Analyzer, fixtures ni código. No ejecuta validadores, DGP, simulación, replay o análisis estadístico.

`scientific_execution=false`; `execution_authorized=false`.
