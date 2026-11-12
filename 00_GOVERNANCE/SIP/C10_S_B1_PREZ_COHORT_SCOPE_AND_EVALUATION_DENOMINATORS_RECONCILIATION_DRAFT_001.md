# C10-S — Alcance de cohorte B1/Need_preZ y denominadores de evaluación

**ID:** C10-S-B1-PREZ-COHORT-SCOPE-DENOMINATORS-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** DOCUMENTARY_RECONCILIATION / PROPOSED_SCOPE / NOT_APPROVED / NOT_MATERIALIZED / NOT_EXECUTED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)

## 1. Pregunta y resultado de la reconciliación

Se resuelve la alternativa entre (a) tomar todas las unidades del roster aplicable o (b) seleccionar una subcohorte pre-Z: **la cohorte objetivo de validación Need_preZ será el censo de UE incluidas en el roster aprobado de la variante B1 que materialice el paquete analítico B1/Need**. No se recomienda una subcohorte adicional.

Esta formulación es deliberadamente precisa: no equivale a afirmar que la cohorte abarque cualquier roster de C10-S, la variante A, toda P*_{τ2}, P*_F ni el denominador ITT. La arquitectura A/B define B como extensión sintética separada y versionada; el marco pertinente es, por tanto, el roster de UE de esa instancia/versión B1. Si el futuro diseño aprueba un único roster conjunto A/B, el crosswalk deberá reflejarlo; no se presume ahora.

La decisión es una recomendación documental de mínimo impacto, no una aceptación de roster, una población causal nueva ni una autorización de materialización.

## 2. Por qué censo del roster B1 y no subcohorte

1. La unidad del paquete es B1/UE, con una B1 por UE y una instancia lógica de servicio vinculada/versionada por UE. No hay una razón conceptual documentada para muestrear unidades dentro de ese marco.
2. La selección de casos por truth, disponibilidad de evidencia, cobertura, resultado E1/E2 o respuesta del Analyzer sesgaría la evaluación del propio procedimiento.
3. Un censo conserva el flujo completo de unidades, incluidos truth=?, expedientes incompletos, salidas abstencionistas y bloqueos de integridad.
4. El requisito de soporte truth=1 y truth=0 se comprueba sobre el marco de validación definido; no se obtiene seleccionando después las unidades que facilitan las métricas.
5. Una subcohorte solo sería admisible si una restricción de diseño verificable la hace necesaria y su regla de selección se preespecifica sin usar truth, Z, evidencia/observabilidad, adjudicaciones, Analyzer ni variables post-Z. No hay ahora una justificación que la requiera.

## 3. Definición operacional de pertenencia y flujo

La cohorte objetivo comprende todas las UE del roster B1 aprobado para la versión del paquete. La pertenencia se determina por roster/versionado, antes de generar o abrir truth y antes de Z. La regla no depende del estado de Need.

Cada unidad debe permanecer visible en el flujo del paquete, con uno de estos estados de proceso (no son estados de truth):

- incluida en el roster y con identidad/binding íntegros;
- incluida, pero bloqueada por identidad, binding, referencia o integridad;
- truth válida 1/0/? sellada;
- evidencia observable NONE/PARTIAL/COMPLETE conforme al alcance aplicable;
- adjudicaciones E1 y E2 selladas, por separado;
- salida del Analyzer registrada, incluida abstención, error o ausencia de salida;
- evaluación abierta/sellada o no evaluable, con motivo explícito.

Un fallo de identidad o integridad no se recodifica como truth=?, no se elimina silenciosamente del roster y no se convierte en error de clasificación. Se reporta como fallo de materialización/cobertura del paquete. La ausencia o insuficiencia de evidencia tampoco excluye la unidad: es una condición que el procedimiento debe afrontar y registrar.

## 4. Tres objetos de evaluación, tres resultados separados

El objetivo de evaluación debe descomponerse en tareas que no se confundan:

### 4.1 Adjudicación humana/protocolaria E1 y E2

E1 y E2 reciben evidencia y metadatos permitidos, sin acceso a TRUTH_LEDGER ni a metadatos reconstructivos. Cada salida se conserva y evalúa individualmente contra truth DGP. La concordancia E1–E2 es un resultado adicional de fiabilidad, no un sustituto de exactitud respecto de truth.

### 4.2 Analyzer automático

La salida del Analyzer se registra y evalúa como procedimiento distinto. No se presume que Analyzer sea idéntico a E1/E2, que consuma sus decisiones, ni que un consenso E1/E2 constituya su etiqueta de referencia. Su interfaz y tarea exactas deben corresponder al contrato Generator/Analyzer/Evaluator vigente antes de implementación.

### 4.3 Evaluación por el Evaluator

El Evaluator accede a truth reservada solo después de que las salidas requeridas estén selladas. Compara, por separado, cada salida E1, E2 y Analyzer contra truth. Debe preservar desacuerdos, abstenciones, errores y casos no evaluables; no reemplaza las salidas originales por consenso.

No se introduce un séptimo artefacto: las salidas E1/E2 permanecen en ADJUDICATION_LEDGER, la salida del Analyzer se registra en el componente/registro de salida previsto por el contrato de interfaz, y la comparación se conserva en EVALUATION_LEDGER. La ubicación exacta del resultado Analyzer debe cerrarse mediante crosswalk de interfaz, no mediante una nueva entidad lógica.

## 5. Denominadores y reporting

Se deben informar al menos cuatro cantidades/flujo, sin colapsarlas:

1. **N roster B1:** todas las UE del roster aprobado de la variante B1.
2. **N integridad evaluable:** unidades con identidad, binding, baseline y truth ledger íntegros. Los bloqueos se informan aparte, con causa.
3. **N truth binaria:** unidades evaluables con truth=1 o truth=0. Este es el marco de cálculo de métricas binarias, condicionado a que ambas clases tengan soporte.
4. **N truth indeterminada:** unidades evaluables con truth=?; se informan por separado y no se imputan a 0/1.

Para cada procedimiento (E1, E2, Analyzer) informar:
- cobertura/salida disponible respecto de N roster y N integridad evaluable;
- matriz de clasificación 1/0/? contra truth binaria;
- sensibilidad, especificidad y errores pertinentes con denominadores explícitos, si los contratos estadísticos fijan que son métricas aplicables;
- abstención, observed=?, error técnico y ausencia de salida como resultados diferenciados;
- comportamiento frente a truth=? por separado, sin medirlo como falso positivo/negativo binario;
- flujo de exclusiones técnicas/bloqueos y análisis de límites de generalización.

No se calcularán métricas binarias únicamente sobre los casos en que el Analyzer produjo una clasificación 1/0 sin informar las abstenciones y fallos de salida: hacerlo ocultaría el rendimiento operativo real. El rendimiento condicional a una clasificación emitida puede presentarse como análisis complementario, con su denominador y tasa de cobertura claramente indicados.

## 6. Relación con las poblaciones causales y con la asignación

Este alcance no modifica:

- P*_{τ2}, población primaria candidata de C1;
- P*_F, subpoblación secundaria de apertura funcional exclusiva;
- el denominador de cada ITT por variante/resultado/horizonte;
- unidad de asignación UA, unidad experimental UE, interferencia ni el mecanismo Z;
- las condiciones constitutivas de elegibilidad experimental.

Need_preZ no es criterio de pertenencia a P*_{τ2}, P*_F ni al denominador ITT. Tampoco se exige soporte truth=1/0 en cada brazo, estrato o población causal. Si se desea afirmar que la validez del Analyzer se transporta a P*_{τ2}, P*_F o a otra población, habrá que informar el solapamiento, soporte y cobertura en esa población y justificar la transportabilidad; el resultado de la cohorte B1 no lo demuestra automáticamente.

La truth se fija en t−1. Z, política D2, provisión, instalación, accesibilidad, Reach, trayectoria, ejecución, Outcome y Value no pueden determinar la pertenencia a la cohorte ni modificar truth.

## 7. Gate de soporte y reglas de bloqueo

Antes de una evaluación confirmatoria:

- el roster B1 debe estar aprobado, versionado y cerrado;
- la cohorte se congela como censo de ese roster antes de truth/evidencia/Z;
- deben existir casos válidos truth=1 y truth=0 en N integridad evaluable;
- ambas clases deben permanecer representadas en el denominador binario, sin reequilibrio posterior;
- truth=? se conserva y reporta separadamente;
- las salidas E1/E2/Analyzer deben estar selladas antes de abrir truth;
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
1. aprobación del roster de la variante B1 y su identidad/versionado;
2. crosswalk exacto de la salida Analyzer con los seis artefactos, sin crear séptimo artefacto;
3. especificación del objetivo de Analyzer (clasificación Need, reconstrucción de evidencia o ambas) y de su abstención;
4. correspondencia final con PKG/PREZ tests existentes, evitando IDs duplicados;
5. suficiencia estadística, potencia y precisión;
6. verificación computacional del firewall Generator/Analyzer/Evaluator;
7. generalización/transportabilidad a poblaciones causales, si se pretende.

## 9. Dictamen

**RECOMENDACIÓN:** censo de todas las UE del roster aprobado de la variante B1 como cohorte de validación Need_preZ; ninguna subcohorte por conveniencia. E1, E2 y Analyzer se evalúan separadamente contra truth DGP; truth=? y bloqueos permanecen visibles; P* e ITT no se alteran.

Este documento es una reconciliación documental propuesta, no una decisión aceptada, contrato congelado ni especificación física. No materializa roster, unidades, truth, evidencia, adjudicaciones, salidas Analyzer, fixtures ni código. No ejecuta validadores, DGP, simulación, replay o análisis estadístico.

`scientific_execution=false`; `execution_authorized=false`.
