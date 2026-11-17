# C10-S — Gate 132: crosswalk S3 observable → A_B1 / V_cont y contratos de identificación

**Fecha:** 2026-11-17  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft, no merge)  
**Estado:** `STATIC_CROSSWALK_COMPLETED_WITH_GAPS / IDEAL_INTERVAL_CHANNEL_CANDIDATE_IDENTIFIED / IMPERFECT_S3_NOT_IDENTIFIED_OR_VALIDATED / NO_DESIGN_FREEZE / NO_SCIENTIFIC_EXECUTION`  
**Precedencia:** DEC-C10-099…102; Gate 128; Gate 129; Gate 130 y su corrigendum; Gate 131; contrato integrado V_cont §§5–6; maestro C10-S §§52.11–52.12, 222, 225, 226–228 y 233; Test Contract Register P182-01…12, P183-01…13, MEAS-01…14 y MISS-01…15.  
**Naturaleza:** auditoría estática de contratos y código ya existente en la rama de investigación. No crea una nueva familia de tests ni una matriz paralela.

## 1. Pregunta y dictamen

¿Existe en los artefactos actuales un subconjunto de señales S3 y reglas que permita un benchmark sintético ideal de medición de A_B1/V_cont, manteniendo separado el canal observado de la truth del Generator y sin atribuir al benchmark ideal validez frente a error, lag, censura o ausencia realistas?

**Dictamen.** Sí existe un candidato de benchmark ideal: una observación booleana por intervalo bajo `CONTINUOUS_EVENT_COVERAGE`, sobre la rejilla común de intervalos iguales y con cobertura completa, sin intervalos ausentes. Este canal representa directamente la conformidad funcional A_B1 por intervalo y permite evaluar la ruta ideal de observación. Es una estipulación del DGP/monitor sintético que proyecta la historia completa; no constituye validación de un sensor S3 real ni un modelo de medición imperfecta identificado.

Los muestreos puntuales de ENABLED/admission, incluso sin error de clasificación, no identifican la continuidad estricta durante todo el intervalo: pueden omitir interrupciones entre observaciones. El canal imperfecto y sus mecanismos de ausencia/error siguen sin calibración ni validación suficientes. Los límites de medición calculados para intervalos ausentes no equivalen todavía a un procedimiento de identificación parcial adjudicado por el Evaluator.

Por tanto:
- `IDEAL_INTERVAL_CHANNEL = CANDIDATE / SOURCE_IMPLEMENTED / TECHNICALLY_REGRESSION_TESTED`;
- `POINT_SAMPLE_CHANNEL = IMPLEMENTED / INSUFFICIENT_FOR_STRICT_CONTINUITY`;
- `IMPERFECT_S3_MEASUREMENT_MODEL = OPEN / NOT_IDENTIFIED / NOT_CALIBRATED`;
- `P182/P183` no quedan cerrados por este crosswalk;
- no se cierra Gate 131, Gate 129/130, C-MED ni la identificación de `θ_A`;
- no se identifica `ΔT_acc → Value`. `V_cont` es el outcome funcional B1 del contrato, no el Value contextual de TGCV.

## 2. Fuentes inspeccionadas y alcance de versión

Se inspeccionaron en `main` los contratos y reglas canónicas de gobernanza, Gate 131 y el maestro C10-S; y en `research/c10-s-consolidation-draft` las implementaciones de harness ya existentes, sin modificarlas en esta auditoría.

Fuentes principales:
- `C10_S_VCONT_S3_MEASUREMENT_IDENTIFICATION_SUFFICIENCY_AUDIT_GATE_131_DRAFT_001.md` (Gate 131).
- `C10_S_DESIGN_CLOSURE_PLAN_GATE_131_S3_MEASUREMENT_AUDIT_ADDENDUM_DRAFT_001.md`.
- `C10_S_GATE_130_G_ASSIGNMENT_AND_GA_SEMANTICS_CORRIGENDUM_DRAFT_001.md`.
- `c10s_synthetic_components.py`: `FunctionalState`, `EventHistory`, `IntervalGrid`, `adjudicate_intervals`, `S3ObservationConfig`, `S3Observation`, `ThetaAS3ObservationRecord`.
- `theta_a_interval_observation.py`, `theta_a_observation_harness.py`, `theta_a_analyzer.py`, `theta_a_evaluator.py`.
- `vcont_integrated_harness.py`: `ScenarioConfig`, `Generator`, `Sealer`, `Analyzer`, `Evaluator`.
- `03_EXPERIMENTS/C10-S/harness/README.md` y el resultado técnico EP-02 run 826.

**Límite de autoridad:** el harness no existe en `main`; la implementación vive en la rama research y PR #116 continúa Draft/no merged. Por tanto, sus estados son de implementación de investigación, no aceptación canónica ni Design Freeze. EP-02 run 826 acredita regresión de software y replay, no ejecución científica ni validez de medida.

## 3. Truth y regla temporal de A_B1 / V_cont

La regla funcional vigente se recupera de DEC-C10-099…102, Gate 128 y Gate 131:

1. `A_B1(i,k)` es conformidad funcional en la unidad `i` y el intervalo `k`. Gate 154/R208 limita la adjudicación a que el comportamiento de admisión sea el requerido por ENABLED: `ADMIT` cuando ENABLED está activo y `NO_ADMISSION` cuando no lo está.
2. PROFILE es una configuración declarativa versionada. No es una señal de exposición runtime ni un segundo componente de A_B1.
3. `V_cont_truth = (1/K) Σ_k A_B1(i,k)`, con intervalos de igual duración. La ventana comienza en t0 según DEC-C10-101.
4. La continuidad es estricta dentro de cada intervalo según DEC-C10-102: una interrupción funcional confirmada en cualquier instante afecta al intervalo correspondiente.
5. Truth estructural/funcional y evidencia observada son canales distintos. La falta de señal no convierte truth en cero ni en uno; el desconocimiento de evidencia no se recodifica como inaccesibilidad.

En el harness de historias funcionales, `FunctionalState.compliant` aplica precisamente la relación ENABLED/admission; `adjudicate_intervals(EventHistory, IntervalGrid)` recorre la historia completa y produce truth 1/0 por intervalo. La rejilla exige límites Decimal, intervalos contiguos e iguales, y cobertura del soporte exacto de la historia. La truth de historias completas no se reconstruye a partir de PROFILE.

## 4. Crosswalk de las rutas S3 existentes

### 4.1 S3 de muestreo puntual: ENABLED / admission / PROFILE

La configuración `S3ObservationConfig` contiene:
- agenda explícita de tiempos de observación;
- lags de captura e ingestión por observación;
- identidad y versión de configuración;
- un kernel conjunto de emisión de secuencias observadas, que permite dependencia entre señales y tiempos.

La fila observada `ThetaAS3ObservationRecord` conserva identidad de unidad/historia/asignación/política, observation-time, capture-time, ingestion-time, valores observados y estados OBSERVED/MISSING para ENABLED, admission y PROFILE, además de las versiones de PROFILE y S3.

**Interpretación de señales:**
- ENABLED y admission behavior son las señales que, conjuntamente, informan sobre A_B1.
- PROFILE conserva identidad/configuración declarativa; no es una señal runtime de cumplimiento.
- En `project_s3`, el componente PROFILE del kernel observado no se utiliza como exposición independiente: el valor PROFILE se proyecta desde el estado/configuración declarativa. Por tanto, no debe contarse como tercer sensor de A_B1.
- El schedule finito solo observa instantes. Un kernel con Se=Sp=1 puede ser perfecto en esos instantes y aun así no detectar una interrupción entre ellos.

El Analyzer focal clasifica esta ruta como `POINT_SAMPLE`, no calcula un punto para V_cont estricto y devuelve abstención/parcialidad con el rango lógico del contraste. Esto es coherente con Gate 131: muestreo puntual no demuestra continuidad intra-intervalo.

### 4.2 S3 de intervalo con cobertura continua: canal ideal candidato

`IntervalMonitorConfig` declara monitor/version, `CONTINUOUS_EVENT_COVERAGE`, probabilidad de ausencia y lags de captura/ingestión. `project_interval_s3` emite por unidad e intervalo:
- `observed_compliance` booleano o ausente;
- `observation_status`;
- límites del intervalo e índice;
- capture-time e ingestion-time;
- identidad/versión de monitor y rejilla.

El monitor proyecta la historia funcional completa y calcula conformidad a lo largo de todos los eventos del intervalo. La validación comprueba cobertura de todas las celdas, identidad, orden, continuidad temporal, lags y estado de ausencia sin exportar transiciones ni el objeto de adjudicación reservado.

**Condiciones para el benchmark ideal:** rejilla común de igual duración que cubra el soporte completo; `CONTINUOUS_EVENT_COVERAGE` estipulado; cero intervalos ausentes; observación booleana válida en todas las unidades y todos los intervalos; soporte completo de historias q_X y de ambos brazos; procedencia de asignación/historia y versiones coherentes.

Bajo esas condiciones, el canal es suficiente para el benchmark sintético ideal de observación de V_cont. La suficiencia es condicional al supuesto de cobertura continua perfecta. El monitor accede a la EventHistory completa para proyectar la señal: esto es una construcción ideal del DGP, no evidencia independiente de que un sistema de telemetría real pueda observar todos los eventos.

### 4.3 Ruta integrada V_CONT del harness anterior

El Generator emite arrays por intervalo para:
- `s3_enabled`;
- `s3_admission_behavior`;
- `s3_profile_value` y su identidad/versión declarativa;
- estados OBSERVED/MISSING;
- `s3_temporal_support`;
- `delta_t_acc_observed` y metadatos de asignación.

El Sealer aplica una allowlist cerrada. El Analyzer reconstruye el resultado funcional con la concordancia ENABLED/admission y exige observaciones completas, `measurement_identified=True`, y soporte etiquetado `INTERVAL_LEVEL`; si hay error/ausencia no identificados, abstiene. El escenario adversarial `R0_MEASUREMENT_ADVERSE` usa error y ausencia estipulados y marca `measurement_identified=False`, por lo que no debe producir una estimación puntual.

**Discrepancia de fuerza semántica:** `INTERVAL_LEVEL` es una etiqueta de resolución, no equivale por sí sola a `CONTINUOUS_EVENT_COVERAGE`. Este harness no conserva para cada señal el mismo contrato explícito de grid/monitor/interval bounds/capture/ingestion que la ruta 4.2. No debe utilizarse la etiqueta `INTERVAL_LEVEL` como prueba de detección exhaustiva de interrupciones intra-intervalo. Su benchmark ideal es una abstracción de DGP por intervalos; no se equipara automáticamente con el monitor de eventos continuos.

## 5. Allowlist y firewall Generator → Sealer → Analyzer → Evaluator

### 5.1 Qué recibe el Analyzer focal

La allowlist puntual incluye identidad de ejecución/unidad/historia, hashes de asignación/q_X/políticas/régimen común, brazo y probabilidad asignada, vector/política versionados, observation/capture/ingestion times, ENABLED/admission/PROFILE observados y sus estados, y versiones de configuración. No contiene potenciales, truth, semillas latentes, parámetros del Generator, etiquetas ocultas ni `θ_A truth`.

La allowlist de intervalo incluye identidad y versión de historia, asignación/políticas/régimen, intervalo, booleano observado/estado, modo de cobertura, capture/ingestion time y monitor/grid. No exporta transiciones EventHistory, adjudicación de intervalo ni potenciales.

El Analyzer recibe evidencia sellada y un contrato de análisis (q_X, fingerprints de políticas/régimen y, opcionalmente, probabilidades inferenciales). El Evaluator recibe por separado la truth reservada y comprueba procedencia y salida sellada después del análisis.

### 5.2 Dictamen del firewall

- **P182-11:** separación estructural implementada en la rama y cubierta por regresiones técnicas; no equivale a auditoría independiente ni a aceptación canónica.
- **P182-12:** IDs, versiones, hashes y provenance están presentes en las rutas focales; cobertura de trazabilidad técnica parcial/implementada.
- La presencia de un hash demuestra integridad del payload declarado, no validez del constructo medido ni independencia real de la fuente.

## 6. Crosswalk dirigido a P182 / P183 / MEAS / MISS

| Contrato | Hallazgo sobre S3 actual | Estado |
|---|---|---|
| P182-05 Reproducibilidad | Identidades, versiones, hashes, historias, rejillas y provenance permiten reconstrucción técnica del payload. Falta evidencia de reconstrucción independiente de un instrumento/fuente real. | IMPLEMENTADO EN RESEARCH / TÉCNICO; VALIDEZ ABIERTA |
| P182-06 Acuerdo interevaluador | No hay roster de observadores independientes, doble adjudicación ni estadístico/regla de acuerdo en el canal S3. | OPEN |
| P182-07 Error en A | El kernel puntual y los parámetros Se/Sp del DGP pueden representar error; no hay calibración, matriz de confusión validada ni error diferencial adjudicado. El monitor continuo es ideal, no un modelo de detección imperfecta. | REPRESENTACIÓN PARCIAL / NO CALIBRADO |
| P182-08 Error en O/V | El crosswalk cubre V_cont como outcome funcional B1, no dimensiones de Value contextual TGCV. No hay modelo de error/validación de Value en esta ruta. | NO CUBIERTO POR GATE 132 |
| P182-11 Firewall | Allowlist y separación de objetos Generator/Analyzer/Evaluator presentes; regresión EP-02 técnica PASS. | IMPLEMENTADO / PASS TÉCNICO; NO AUDITORÍA INDEPENDIENTE |
| P182-12 Trazabilidad | Versionado, IDs, tiempos y hashes presentes en el canal focal; falta evidencia de instrumento externo. | IMPLEMENTADO EN RESEARCH / PARCIAL |

| Contrato | Hallazgo sobre ausencia/censura | Estado |
|---|---|---|
| P183-01 Taxonomía | S3 utiliza principalmente OBSERVED/MISSING; no representa toda la taxonomía OBSERVED_INVALID, NOT_APPLICABLE, CENSORED, DISPUTED y UNKNOWN. | PARCIAL |
| P183-02 MCAR/MAR/MNAR | El monitor de intervalo admite ausencia aleatoria estipulada; el DGP integrado tiene missingness y un escenario adversarial. No hay mecanismo MAR/MNAR materializado, clasificado y calibrado. | MCAR SINTÉTICO LIMITADO / MAR-MNAR OPEN |
| P183-03 Desconocido ≠ inaccesible | Ausencia observacional se conserva como MISSING/None y provoca abstención; no se recodifica como A_B1=0. | PARCIALMENTE IMPLEMENTADO |
| P183-04 No observado ≠ cero | El Sealer exige coherencia entre valor nulo y estado MISSING; Analyzer cuenta ausencias y no las trata como cumplimiento/incumplimiento. | IMPLEMENTADO EN CÓDIGO |
| P183-05 Ausencia de Value ≠ Value nulo | No aplica a la medida V_cont de Gate 132; V_cont es outcome funcional, no Value contextual. | FUERA DE ALCANCE |
| P183-06 ITT conserva población aleatorizada | Se exige roster exacto de unidades asignadas para el canal focal; falta de soporte produce abstención. No hay corrección general por pérdida de seguimiento. | PARCIAL |
| P183-07 Selección postasignación | El Evaluator comprueba correspondencia con el roster de asignación; no se observó un modelo completo de abandono/censura. | PARCIAL |
| P183-08 Ausencia de A y mediación | La ruta S3 aquí mide A_B1/V_cont, no la medición de A_f*/ΔT_acc* ni su mediación causal. | NO CUBIERTO |
| P183-09 Censura | No existe distinción operativa suficiente entre censura administrativa/informativa y MISSING. | OPEN |
| P183-10 Sensibilidad MAR/MNAR | No hay análisis de sensibilidad o tipping points ejecutados para mecanismos de ausencia S3. | OPEN |
| P183-11 Cotas | El Analyzer calcula bounds de medición para intervalos ausentes y el Evaluator reconstruye su aritmética; pero el dictamen principal sigue siendo INDETERMINATE y la adjudicación `truth_within_bounds` usa el rango lógico [-1,1], no esos measurement bounds. No se expone una cobertura adjudicada de los bounds de medición en el resultado del Evaluator. | IMPLEMENTACIÓN DIAGNÓSTICA PARCIAL; NO CIERRE P183-11 |
| P183-12 Dictamen por estimando | Hay estados/razones de identificación para el estimando focal y estados separados en el harness V_CONT; no cubren aún cada estimando × dimensión Value del paquete C. | PARCIAL |
| P183-13 Trazabilidad | Estados de ausencia, identidades, versiones y hashes se preservan técnicamente. | PARCIAL / IMPLEMENTADO EN RESEARCH |

### 6.1 Cobertura de los escenarios MEAS-01…14

- **MEAS-01 (Se=Sp=1):** representable por el canal ideal; benchmark sintético candidato, no validez de instrumento.
- **MEAS-02 (error no diferencial):** parámetros Se/Sp están representables en el DGP integrado; un escenario adversarial fijo existe, pero no calibra recuperación.
- **MEAS-03 (Se+Sp=1), MEAS-04 (error diferencial por brazo), MEAS-05 (error por versión):** no hay batería focal ejecutada ni contrato calibrado que los cierre. El kernel conjunto puede expresar emisiones dependientes de la historia, pero no sustituye escenarios versionados y adjudicados por estos mecanismos.
- **MEAS-06 (fuga retrospectiva):** allowlists excluyen Outcome/ejecución/truth del Analyzer; cobertura técnica parcial.
- **MEAS-07…09 (validación aleatoria/no aleatoria/referencia imperfecta):** no materializados como validación independiente del canal S3.
- **MEAS-10…14:** errores de U/R/C, recodificación de desconocido, snapshots post-ejecución, pérdidas de validación y catálogo incompleto no quedan resueltos por medir A_B1/V_cont; son contratos adversariales reutilizables, no evidencia cubierta por el benchmark ideal.

### 6.2 Cobertura de los escenarios MISS-01…15

- **MISS-01:** ausencia aleatoria independiente representable en el DGP; no calibrada.
- **MISS-02…03:** MAR por covariables basales o historia postasignación no materializado.
- **MISS-04, MISS-06, MISS-07, MISS-10, MISS-11:** MNAR, ausencia ligada a truth/accesibilidad/resultado, selección de validación y abandono adverso no materializados como modelos identificados ni sensibilidad.
- **MISS-05, MISS-13, MISS-14:** pérdida diferencial por brazo, por clúster o casi nula por estrato no cubiertas por una auditoría de retención.
- **MISS-08…09:** snapshot intermedio ausente y selección de ejecutores no son resueltos por el canal de intervalos V_cont.
- **MISS-12:** Value no definido frente a no observado queda fuera del objeto V_cont.
- **MISS-15:** documentación diferencial de U/R/C pertenece a medición de accesibilidad, no al canal funcional A_B1.

Los IDs se conservan como contratos existentes; no se crean nuevos casos ni se declara que los escenarios listados hayan sido ejecutados.

## 7. Gaps concretos y clasificación de estado

1. **Semántica temporal:** `POINT_SAMPLE` no identifica continuidad estricta; `INTERVAL_LEVEL` tampoco prueba por sí solo `CONTINUOUS_EVENT_COVERAGE`. Solo el contrato explícito de monitor continuo satisface el supuesto ideal del benchmark.
2. **Error de medición:** existen mecanismos de emisión configurables, pero no tasas aprobadas, calibración independiente, acuerdo ni invariancia de medida.
3. **Ausencia:** OBSERVED/MISSING es insuficiente para la taxonomía completa; MCAR sintético no resuelve MAR/MNAR, censura ni selección.
4. **Bounds:** los measurement bounds son verificados aritméticamente, pero no se usan para adjudicar cobertura de truth en el Evaluator; no deben presentarse como identificación parcial validada.
5. **Estimando:** la suficiencia de medida ideal de V_cont no demuestra que G/ITT-G sea `θ_A(q_X*, r_common; V_cont)`. Se mantiene el corrigendum Gate 130: la correspondencia con g_A0/g_A1, q_X*, soporte y r_common debe acreditarse por separado.
6. **Value:** V_cont no es Value contextual; no se cierra el puente `ΔT_acc → Value`.

| Objeto | Definido | Implementado en research | Ejecutado técnicamente | Aceptado/cerrado |
|---|---|---|---|---|
| Truth A_B1/V_cont | Sí, DEC-C10-100…102 | Adjudicación por EventHistory | Regresión de software | Semántica temporal parcialmente aceptada |
| S3 puntual | Contrato de schedule/kernel | Sí | Regresiones técnicas | No; insuficiente para continuidad estricta |
| S3 intervalo ideal | Condición de cobertura continua | Sí | EP-02 run 826 prueba de integración, no validez del sensor | No; benchmark candidato |
| S3 imperfecto | Familias MEAS/MISS | Representación parcial | No calibración/validación científica | OPEN |
| P182/P183 | Contratos definidos | Cobertura parcial por código | Solo regresiones de software pertinentes | OPEN/PARCIAL según fila |

## 8. Routing y límites

El crosswalk documental de Gate 132 queda completado en su alcance estático. No requiere otra matriz ni nuevos IDs. El siguiente trabajo, si se autoriza documentalmente, debe resolver las discrepancias concretas ya identificadas en los contratos existentes; no elegir señales, agenda temporal, rejilla, tasas, tolerancias, parámetros MAR/MNAR, N o R en esta auditoría.

Este registro no:
- modifica DEC-C10-099…102 ni la semántica A_B1/V_cont;
- convierte `INTERVAL_LEVEL` en cobertura continua;
- acepta un modelo S3 imperfecto;
- cierra P182/P183, Gate 131, Gate 129/130, C-MED o C-ANALYZER;
- equipara ITT-G con θ_A;
- selecciona Value, outcome adicional, parámetros, tamaños o tolerancias;
- autoriza cambios de código, tests, CI/workflows, calibración, Monte Carlo o experimento científico;
- modifica `main`, RMA, Evidence→Claim Matrix, STATUS o TGCV Core.

`scientific_execution=false`  
`execution_authorized=false`

