# C10-S — Gate 133: benchmark ideal, abstención adversarial y correspondencia temporal V_cont

**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** IDEAL_S3_BASELINE_SCOPE_BOUNDED / R0_MEASUREMENT_ADVERSE_STATUS_ONLY / EP01_EP02_EP03_PROFILE_SCOPE_GOVERNED / WORKFLOW_VALIDATION_OPEN / TEMPORAL_GRID_PARTIAL_MATCH / UNKNOWN_TRUTH_NOT_MATERIALIZED / NO_DESIGN_FREEZE / NO_EXECUTION.  
**Precedencia:** contrato integrado V_cont §§1–6; DEC-C10-099…102; Gates 131–132; Gates 184, 200–205; `vcont_integrated_harness.py`; `vcont_benchmark_protocol.py`; `test_vcont_integrated_harness.py`; workflows EP-01/02/03.

## 1. Pregunta y dictamen

¿El benchmark ideal, el escenario R0 adverso, los contratos de prueba, los workflows y la rejilla temporal ya ofrecen una base suficiente para considerar cerrada la medición de V_cont?

**Dictamen: no.** Sí existe una base implementada y gobernada para un benchmark de asignación con outcome sintético V_cont, bajo medición S3 perfecta y completa. También existe una ruta adversarial de abstención. Sin embargo, esa base es más estrecha que la semántica temporal completa de DEC-C10-100…102: la truth del harness es binaria por intervalo y no representa UNKNOWN en la truth; la rejilla no representa eventos runtime subintervalo. El canal S3 imperfecto genera error/ausencia, pero no corrige ni acota V_cont.

La cobertura EP-01/02/03 y sus autorizaciones ya fueron reconstruidas y corregidas en Gates 200–205. Gate 133 no vuelve a diseñar esos perfiles. Su validación completa de YAML/workflows sigue abierta según Gate 205.

## 2. Qué benchmark ideal está realmente implementado

El contrato integrado identifica cuatro targets de asignación separados: ITT-Z run-conditional, ITT-Z mechanism-marginal, ITT-Z reference-regime y ITT-G bajo Z=0. El benchmark no estima θ_A; `theta_a_truth=None` y el contrato prohíbe relabelar ITT-G como θ_A.

En el DGP implementado:

1. Generator crea, para cada unidad y cada régimen potencial (Z,G), estados ENABLED y PROFILE por intervalo.
2. El estado funcional de intervalo es su conjunción binaria ENABLED∧PROFILE.
3. El V_cont potencial de unidad/régimen es la media aritmética de esos estados sobre `n_intervals`.
4. S3 produce para el régimen realizado observaciones separadas de ENABLED y PROFILE, con sensibilidad, especificidad y ausencia parametrizadas.
5. ScenarioConfig solo permite declarar `measurement_identified=true` cuando sensibilidad=1, especificidad=1 y probabilidad de ausencia=0.
6. Analyzer solo calcula el outcome observado cuando las condiciones compartidas se satisfacen y toda la cobertura S3 está observada; de lo contrario se abstiene. No usa parámetros secretos de error ni truth del Generator.

**Interpretación admisible:** el benchmark ideal permite evaluar recuperación de los estimandos de asignación del contrato integrado bajo el DGP binario por intervalos y medición perfecta/completa, siempre que también se satisfagan sus condiciones de asignación, soporte, interferencia, versión y estimando.

**No permite afirmar:** recuperación robusta bajo error/ausencia, validez general de S3, recuperación de θ_A, validez de V_cont para cualquier semántica temporal, ni evidencia confirmatoria de ΔT_acc→Value.

## 3. R0_MEASUREMENT_ADVERSE y su cobertura real

El roster contiene 13 escenarios y la matriz 52 pares escenario-estimando. `R0_MEASUREMENT_ADVERSE` se clasifica como `STATUS_ONLY`, identificación `INDETERMINATE` y abstención esperada para sus cuatro estimandos; no genera pares de recuperación numérica en ese escenario.

El test existente `test_measurement_adversity_requires_abstention` ejecuta el helper de test `execute_world` sobre ese escenario y comprueba:
- `package_status == INDETERMINATE`;
- `g_assignment_status == INDETERMINATE`;
- `report.expected_abstention_respected == True`.

Esto acredita que el código fuente contiene una prueba contractual de clasificación/abstención para ese escenario. **No acredita que el test se haya ejecutado en esta auditoría**, que la suite esté pasando, que Analyzer corrija error, que produzca bounds, que recupere V_cont con missingness o que se haya calibrado Se/Sp. No se ha ejecutado Gate 133 ni se ha consultado un resultado de CI para inferir PASS.

P182/P183 y MEAS/MISS son contratos y taxonomías de cobertura; los perfiles de test no materializan automáticamente todos sus casos. No se crean ni renumeran IDs.

## 4. EP-01, EP-02 y EP-03: estado que ya quedó resuelto documentalmente

Gates 200–205 ya establecieron el registro de perfiles y las correcciones de alcance:

| Perfil | Trigger y autorización | Suite | Naturaleza |
|---|---|---|---|
| EP-01 P178 | Manual; confirmación explícita; rama research exacta | 3 módulos P178 | Incluye fixtures sintéticos y Monte Carlo P178 27×10.000; no es C10-S V_cont |
| EP-02 integrado | Manual; `confirm_synthetic_test_execution=true`; rama research exacta | 8 módulos explícitos | Suite de contratos integrada que incluye generación sintética de tests y smoke tests; no equivale al benchmark científico completo |
| EP-03 package v2 pure | Manual; rama research exacta | 3 módulos explícitos | Captura/writer/verifier puros; no invoca Generator ni productor sintético |

La suite EP-02 incluye `test_vcont_integrated_harness`, `test_vcont_benchmark_protocol`, `test_vcont_capture_v2`, `test_vcont_package_v2_serialization` y `test_vcont_package_v2_verifier`, además de los tres módulos P178 heredados. La confirmación EP-02 cubre exactamente esa suite y replay, no autoriza Monte Carlo 27×10.000, calibración, paquete de producción o ejecución confirmatoria.

Gate 205 verificó estáticamente allowlists, arrays de materialización, locks y guardas. También corrigió tres expresiones shell y una omisión de retención de logs. Pero **la validación completa YAML/actionlint y la validación integral de los bloques shell/Python siguen OPEN**. La comprobación puntual de sintaxis Bash no equivale a validación completa de workflows.

Por tanto, la cobertura de workflows ya no es una dependencia de diseño científico que requiera otro inventario. Es una condición técnica pendiente antes de cualquier despacho. Ningún workflow se ha despachado en Gate 133.

## 5. Correspondencia temporal con DEC-C10-100…102

### 5.1 Coincidencias reales

El harness declara explícitamente `window_start`, `last_transition_support`, `follow_up` y `n_intervals`; valida que la ventana sea positiva y que el final del soporte de transición caiga en una frontera de intervalo anterior al follow-up. El manifiesto calcula `window_end = last_transition_support + follow_up` y una anchura común `(window_end-window_start)/n_intervals`.

La truth se conserva por unidad, régimen potencial e intervalo. El test existente comprueba una ventana de ejemplo que comienza en 0, termina en 1 y tiene intervalos iguales. Esto demuestra correspondencia estructural con una ventana común y agregación por intervalos iguales.

### 5.2 Límites que impiden equivalencia completa

1. **UNKNOWN de truth:** `potential_interval_truth` se construye como conjunción binaria de estados ENABLED/PROFILE. No hay un tercer estado de truth UNKNOWN. El `None` de S3 es ausencia de observación y no UNKNOWN funcional del Generator.
2. **Continuidad estricta:** la truth se evalúa por estado de intervalo; el harness no conserva un event log que permita adjudicar una interrupción funcional en cualquier instante intraintervalo. Una interrupción breve que no altere el estado binario representado no está separadamente modelada.
3. **Resolución temporal:** `n_intervals` fija la granularidad. No hay event-time, observation-time e ingestion-time diferenciados ni un modelo de lag de señal.
4. **t0 y provisión/instalación:** la ventana parametrizada y el soporte de transición dan una abstracción temporal común, pero el mapping exacto de t0, asignación, provisión, instalación y cada frontera de intervalo a DEC-C10-101 no queda acreditado solo por el manifiesto.
5. **Bounds:** el Analyzer no implementa bounds de V_cont para truth UNKNOWN ni para medición S3 imperfecta. La abstención no equivale a bounds.

**Conclusión temporal:** existe una implementación de V_cont ideal, intervalizada y binaria, alineada parcialmente con la forma de DEC-C10-100…102; no está demostrado que materialice su semántica completa, especialmente UNKNOWN y continuidad estricta en cualquier instante.

## 6. Estado de evidencia: no mezclar los niveles

| Afirmación | Estado admisible |
|---|---|
| Existe DGP sintético y truth reservada para V_cont | IMPLEMENTED IN SOURCE |
| Existe canal S3 imperfecto por intervalo | IMPLEMENTED IN SOURCE |
| Existe ruta ideal S3 perfecta/completa | IMPLEMENTED IN SOURCE / CONTRACTED |
| Existe escenario adverso y test de abstención | TEST SOURCE PRESENT |
| Suite EP-02 ejecutada y PASS | NOT ESTABLISHED HERE |
| Workflows validados integralmente | OPEN (Gate 205) |
| Recuperación numérica bajo error/ausencia | NOT IMPLEMENTED / NOT ESTABLISHED |
| Bounds ante truth UNKNOWN | NOT IMPLEMENTED |
| Correspondencia completa con DEC-C10-100…102 | NOT ESTABLISHED |
| θ_A recuperado | NOT ESTABLISHED; `theta_a_truth=None` |
| Puente V_cont→consecuencia B1→Value | OPEN (Gate 126 y contratos relacionados) |

## 7. Decisión metodológica que falta — Gate 134

No hace falta otro ledger, escenario, canal S3, matriz o inventario de workflow. Hace falta resolver una cuestión de alcance antes de freeze:

**¿El benchmark integrado V_cont debe representar el estado UNKNOWN en la truth y la semántica de continuidad estricta de DEC-C10-100…102, o se acepta explícitamente como benchmark ideal acotado a truth binaria por intervalos, dejando la semántica UNKNOWN/continuidad intraintervalo fuera de ese benchmark?**

Gate 134 debe:
- reconstruir DEC-C10-100…102 y el contrato integrado, sin reinterpretarlos;
- comprobar si una exclusión de UNKNOWN/continuidad intraintervalo está ya autorizada en una decisión o contrato subordinado;
- separar alcance del benchmark de la definición general de V_cont;
- evaluar consecuencias para el estimando/verdad del Evaluator y para la interpretación del benchmark;
- elevar la decisión que corresponda al nivel de gobernanza autorizado, sin cambiar el código ni DEC por inferencia.

No elegir ahora una opción, ni introducir parámetros, granularidades, mecanismos de UNKNOWN, tolerancias o métodos de bounds. No abrir una nueva familia de pruebas.

## 8. Límites de autorización

Auditoría estática de artefactos y fuentes GitHub. No se importó ni ejecutó código; no se ejecutaron tests, validadores, compilación, actionlint, YAML parser, workflows, generación, simulación, calibración, Monte Carlo, estimación o experimento. No se modificó código, workflow, schema, DEC, test register, RMA, Evidence→Claim Matrix, STATUS, main o PR base.

`scientific_execution=false`  
`execution_authorized=false`
