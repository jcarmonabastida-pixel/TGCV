# C10-S — Gate 111: crosswalk de cobertura de contratos existentes frente a asignación e interferencia

**Estado:** HISTORICAL CONTRACT INVENTORY RECONCILED / UNIT FAMILY IS AUTHORITATIVE EXISTING COVERAGE / SCENARIO COVERAGE PARTIAL / IMPLEMENTATION EVIDENCE SCOPE-LIMITED / P178 BENCHMARK EXECUTION DISTINGUISHED FROM FOCAL HARNESS / NO NEW TEST IDS / NO TEST EXECUTION IN THIS GATE / NO DESIGN FREEZE  
**Fecha:** 2026-11-15  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft  
**Precedencia:** README/bootstrap/main governance; plan maestro §§16.185–16.200 y §§16.249–16.260; Test Contract Register §§4–9, 13–17, 55 y 69–76; Gate 109/110; PE Integrated Technical Specification; PR #116 implementation-alignment records.  
**Tipo:** auditoría documental de cobertura y trazabilidad. No es test run, validación estadística, ejecución científica ni autorización de cambios de contratos.

---

## 1. Pregunta y dictamen

¿Los contratos ya existentes cubren las cuatro arquitecturas A–D de Gate 110 y sus estados de identificación, y qué huecos son reales?

**Dictamen:** el registro ya contiene cobertura explícita de unidad, independencia, correlación basal, spillover de recursos e información, asignación por clúster, exposición parcial/desconocida, positividad, LATE bajo interferencia, integridad de asignación, tamaño efectivo y prohibición de formar clústeres retrospectivamente: **UNIT-01…14** (§17). Es la familia primaria para Gate 109/110; no procede crear otra familia de pruebas de interferencia.

La cobertura está definida en el plano contractual, pero no equivale a implementación ni ejecución. Las familias P177/P178/P179/P182/P183 y S4R/MEAS/MISS/TRJ/POL/XSYNC aportan controles complementarios por estimando, medición, missingness, vías colaterales y abstención. INT-01/02 no son una familia general de interferencia: tratan combinaciones q/g y soporte; INT-01…08 aparece también como material histórico de un escenario alternativo explícitamente no primario.

La inspección de la implementación disponible confirma una limitación material: el focal harness solo modela asignación individual balanceada con un indicador `interference_absent`; no implementa un motor de clústeres ni un mapa (G_i(Z_{-i})), ni una red de exposición. Su README declara que no es un motor de clúster/interferencia, ni el D2 material completo. Por ello, el código existente no acredita cobertura implementada de B/C/D.

**Resultado:** GATE_111_EXISTING_CONTRACTS_CROSSWALKED / UNIT_01_14_PRIMARY_INTERFERENCE_FAMILY / CONTRACT_COVERAGE_DEFINED_NOT_EXECUTED / FOCAL_HARNESS_SCOPE_LIMITED_TO_INDIVIDUAL_NO_INTERFERENCE / B_C_D_NOT_IMPLEMENTED_IN_FOCAL_HARNESS / P178_BENCHMARK_RUN_SEPARATE_FROM_ANALYZER / NO_NEW_TEST_IDS / NO_TEST_EXECUTION / NO_FREEZE.

## 2. Fuentes recuperadas

1. `C10_S_TEST_CONTRACT_REGISTER_DRAFT_001.md` (rama research; §17 UNIT-01…14; §§5–9 MEAS/MISS/VER/TRJ/INT/POL; §55 P177/P178/P179; §§69–76 crosswalks).
2. Plan maestro `C10_S_DESIGN_CLOSURE_AND_OPERATIONALIZATION_PLAN_DRAFT_004.md`, §§16.185–16.200, 16.249–16.260.
3. Gate 109 y Gate 110.
4. `03_EXPERIMENTS/C10-S/harness/README.md`, `focal_harness.py`, `test_focal_harness.py`, `test_p178_analyzer_bridge.py`, `test_p178_analyzer_monte_carlo.py`.
5. `03_EXPERIMENTS/C10-S/calibration/p178_run_manifest.json`, stdout/stderr y outputs CSV.
6. PR #116 metadata/description y comparación base/head disponible en GitHub.

No se ejecutó ningún archivo ni workflow durante Gate 111. La inspección fue de contenido y provenance declarada.

## 3. Matriz principal: escenarios Gate 110 × contratos existentes

| Escenario Gate 110 | Contratos primarios | Complementarios | Cobertura contractual | Implementación inspeccionada |
|---|---|---|---|---|
| A — individual aislada | UNIT-01/02/03/09/11/12/13/14 | P177-01/02/06; P178-SIM-03/06; S4R-07/08/09; POL-01; MISS-13/14 | PARCIAL-ALTA: define unidad, independencia, asignación, positividad y tamaño efectivo; no acredita aislamiento material | Focal harness: supuesto booleano `interference_absent`; no prueba aislamiento de recursos reales |
| B — asignación por clúster | UNIT-03/06/12/13/14 | P178-SIM-03; MISS-13; P177-01/06; P183-09/10/11/12 | PARCIAL: define cambio de UA y tamaño/inferencia por clúster; faltan estimandos/ponderación UE vs cluster y spillover intra/intercluster discriminados | No implementado en focal harness |
| C — individual + mapa de exposición | UNIT-04/05/07/09/11 | QX-06/07; P177-01/02/03/04/10/12; P183-10/12; POL-02/06; INT-02 (soporte q/g, no mapa de red) | PARCIAL: mapa (G_i) está nombrado y exige efecto directo/indirecto/total; faltan especificación, suficiencia, probabilidades de exposición y soporte por combinación | No implementado en focal harness |
| D — interferencia no mapeada | UNIT-08/10; UNIT-04/05 | P177-03/04/12; P183-10/11/12; POL-02; S4R-13/18 | PARCIAL-ALTA en regla de rechazo/efecto paquete; falta evaluación completa de tasas de falsa identificación, falsa abstención y cotas | Harness permite gate binario de interferencia y abstención; no modela DGP de interferencia desconocida |

La calificación mide cobertura de aserciones, no aceptación científica. Ningún escenario A–D se declara implementado o ejecutado como suite integrada.

## 4. Cobertura exacta de UNIT-01…14

| ID existente | Función contractual | Gate 110 | Dictamen de cobertura / límite |
|---|---|---|---|
| UNIT-01 | UE, UA y UO identificadas; repetición observacional no aumenta UE | A/B/C | Directa; el mapping material UE–UA–UO sigue abierto (Gate 109) |
| UNIT-02 | Independencia primaria; recursos/agentes/información/infraestructura/canales compartidos ausentes | A | Directa; requiere evidencia material de aislamiento, no solo flag de configuración |
| UNIT-03 | Correlación basal por cluster diferenciada de spillover por Z | A/B | Directa; no especifica por sí sola estimando/varianza |
| UNIT-04 | Spillover de recurso; rechazar ITT individual simple | C/D | Directa para detección; no define mapa completo |
| UNIT-05 | Spillover informacional; requiere exposición | C/D | Directa para detectar necesidad de mapa; no verifica su suficiencia |
| UNIT-06 | Asignación por clúster; UA, N e inferencia por clúster | B | Directa pero incompleta: no separa intracluster/intercluster ni ponderación UE/cluster |
| UNIT-07 | (G_i(Z_{-i})); efecto directo/indirecto/total | C | Directa conceptual; función, versiones, probabilidades y soporte no operacionalizados |
| UNIT-08 | Exposición desconocida; INDETERMINATE/NO IDENTIFIED | D | Directa; tolerancias y denominadores de clasificación no fijados |
| UNIT-09 | Positividad en unidad realmente aleatorizada y soporte de exposición | A/B/C | Directa; falta soporte conjunto concreto y cálculo de probabilidades de exposición |
| UNIT-10 | Rechazar Wald individual como LATE focal si no se sostiene no interferencia | B/C/D | Directa para prohibición; no reemplaza identificación IV bajo interferencia |
| UNIT-11 | Semilla, algoritmo, bloque/estrato, versión B, probabilidades y desviaciones | A/B/C | Directa como requisito; el contrato real de aleatorización continúa incompleto |
| UNIT-12 | N UE, N UA/clúster y observaciones longitudinales | A/B/C | Directa; requiere regla de ponderación/inferencia por estimando |
| UNIT-13 | Prohibir clúster retrospectivo tras Outcome/Value | A/B/C | Directa; no implica que el roster/cluster ya esté fijado |
| UNIT-14 | Cambio UE/UA exige recalcular población, estimando, qX, soporte, N y protocolo | A/B/C | Directa; criterio de control transversal |

**Conclusión:** UNIT-01…14 es la familia de referencia y cubre los conceptos centrales, pero es una especificación de aceptación propuesta, no evidencia de que los cuatro diseños hayan sido implementados o probados.

## 5. Crosswalk de familias auxiliares

### 5.1 S4R-01…18 y POL-01…10

- **S4R-07/08/09** separan intento, instalación, primera etapa nula y primera etapa débil; no prueban interferencia entre unidades.
- **S4R-05/06/13** cubren vías directas/colaterales y dependencias compartidas que alteran alternativas; aportan detección de rutas no focales, pero no sustituyen (G_i).
- **S4R-18** conserva el crosswalk XSYNC de atribución de política; debe leerse en su alcance D2 vigente.
- **POL-01/02** distinguen DGP aislado frente a vías directas B→Value/coste/calidad/seguridad; **POL-02** es complementario al escenario D y a la regla de efecto de paquete.
- **POL-03/04/05/06** cubren versión/coste, probabilidades finales, q/Value y factibilidad/soporte; no especifican spillovers de red.
- **POL-08/09/10** separan PASS metodológico de afirmación científica, imprecisión y cobertura limitada del módulo.

**Dictamen:** cobertura útil de atribución y rutas alternativas; no duplicar UNIT ni presentarla como motor de exposición.

### 5.2 MEAS-01…14

MEAS cubre error diferencial/no diferencial, validación, cegamiento, circularidad temporal, pérdida en submuestras y catálogo incompleto. Es transversal a A–D, pero no identifica el mecanismo de asignación ni corrige automáticamente sesgo de medición inducido por exposición. MEAS-04/05/13 son relevantes para medición diferencial por brazo/versión; su extensión a exposición requiere que el estrato de exposición esté definido y medido.

### 5.3 MISS-01…15

MISS cubre MCAR/MAR/MNAR, pérdidas por brazo, accesibilidad, selección postratamiento, snapshots ausentes, retención por estrato y pérdida por cluster/unidad organizativa. **MISS-13/14** son los vínculos más directos con B/C; MISS-03/04/05/06/09/11 son controles transversales de seguimiento/selección. Ninguno define el mapa de exposición ni resuelve por sí mismo positividad.

### 5.4 VER/TRJ-01…07

VER-04/05/06 protegen versión asignada/recibida, ITT por Z y efecto de paquete. TRJ-07 prohíbe ajustar por selección/ejecución postratamiento si cambia el estimando o induce sesgo. Son necesarios para A–D, pero no prueban unidad de aleatorización o interferencia.

### 5.5 INT-01/02 y material INT-01…08

En el Test Contract Register vigente, §8 contiene INT-01/02: interacciones de q/g y falta de soporte de una combinación. XSYNC-138-04 también exige soporte por estrato e historia. No deben etiquetarse como test de interferencia entre unidades.

El material INT-01…08 citado en la reconciliación AUD-001/002 se conserva únicamente como reutilizable en un escenario alternativo explícito; su supersesión y alcance están documentados en el plan. No lo contamos como suite primaria D2 ni como cobertura de (G_i).

### 5.6 P177/P178/P179/P182/P183

| Contrato | Contribución a Gate 111 | Límite |
|---|---|---|
| P177-01 | ITT por resultado | No define unidad/interferencia |
| P177-02 | Primera etapa | No es probabilidad de exposición |
| P177-03/04 | Wald/LATE y weak-IV | UNIT-10 restringe LATE bajo interferencia; no hay solución IV general |
| P177-05/06 | O/V separados; ajuste basal y no post-Z | No modela spillovers |
| P177-07/08 | ATE/ATT, heterogeneidad, ponderación/compliers | No fija ponderación UE/cluster |
| P177-10 | Recuperación sintética | No cubre por sí solo falsa identificación/abstención |
| P177-12 | Efecto de política vs atribución a accesibilidad | Complementa POL y escenarios D |
| P178-SIM-01…10 | Potencia, N, clúster, R, error MC, semillas, pérdidas, métricas y parámetros ex ante | Diseño cuantitativo; SIM-03 menciona ICC/efecto de diseño/número de clústeres, no implementa mapa de exposición |
| P179-01…08 | A/O/V, Value vectorial, contexto, trade-offs y agregación | No sustituye identificación ni define estimando de interferencia |
| P182-01…12 | Validez, circularidad, error, acuerdo, invariancia, firewall | Medición/constructo; no identifica asignación |
| P183-01…13 | Ausencia, selección, censura, sensibilidad, bounds y dictamen | Complementario a B/C/D; no construye (G_i) |

Los crosswalks históricos §§69–76 del registro ya corrigen que P177-05…08 no son contratos de mediación y que C-MED/C-ANALYZER conservan vacíos. Gate 111 respeta esa corrección y no amplía su alcance.

## 6. Evidencia de implementación y ejecución: separación estricta

### 6.1 Focal harness

El README del harness declara:
- IMPLEMENTED_IN_RESEARCH_BRANCH.
- NOT_EXECUTED / NOT_CONFIRMATORY / NOT_DESIGN_FROZEN.
- DGP focal con asignación balanceada individual.
- El Analyzer recibe un contrato público con `interference_absent` como condición; no un mapa de exposición.
- No es un motor de clúster/interferencia, ni un D2 material completo, ni un store U_G general.
- Los tests de `test_focal_harness.py` son 15 tests de contrato más un bridge P178; `test_p178_analyzer_monte_carlo.py` contiene una definición smoke test. Su presencia no prueba que se hayan ejecutado.

El código recuperado confirma `ScenarioConfig` con `assignment_probability` y `interference_absent`; no se observa representación de cluster, roster, (G_i), exposición (E_i) o probabilidades de exposición en esta slice. El flag binario no equivale a demostrar UNIT-02.

### 6.2 P178 benchmark

El repositorio contiene `p178_run_manifest.json` con:
- (R=10{,}000) por celda.
- Asignación declarada: balanced 1:1, independent UE.
- 27 celdas de referencia y 32 celdas de curva central.
- Captura stdout y hashes de artefactos.
- Limitación expresa: benchmark estimator only; no TGCV Analyzer, no escenarios adversariales de medición, no experimento confirmatorio.

El stdout persistido informa 27 reference cells y 32 curve cells. Esto constituye evidencia documental de una ejecución del benchmark P178 según el manifiesto y la captura; **no** acredita ejecución del focal harness, pruebas UNIT-01…14, CI, Analyzer Monte Carlo ni escenarios B/C/D. La independencia individual es una estipulación del benchmark, no una auditoría empírica de aislamiento del sistema.

### 6.3 PR #116 y trazabilidad de pruebas

La descripción actual del PR registra, para las alineaciones Gate 123/124, recuentos de definiciones de tests y aserciones source-level, pero también declara que no se ejecutaron tests/CI en esas pasadas. Estos recuentos no se usan como evidencia de cobertura de interferencia sin mapping por test concreto. La comparación de ramas confirma que el head incluye harness, workflows y artefactos de calibración; la presencia de workflows no significa que hayan corrido.

**Corrección de estado necesaria:** no repetir el enunciado global «no hay ejecución» para todo C10-S. El estado documental correcto es:
- P178 estimator benchmark: ejecución registrada por manifiesto/captura.
- Focal harness: implementado, declarado no ejecutado.
- UNIT-01…14: contratos definidos; ejecución no acreditada.
- Escenarios de interferencia B/C/D: no implementados en el focal harness inspeccionado; no ejecutados.
- Experimento confirmatorio D2/C10: no acreditado ni autorizado por Gate 111.

## 7. Gaps reales de cobertura (sin crear IDs)

| Gap | Vacío observado | Contratos que ya lo rodean | Tratamiento |
|---|---|---|---|
| G111-01 | Aislamiento individual material no probado por mero flag | UNIT-02/03; S4R-06 | Mantener evidencia material requerida; no duplicar test |
| G111-02 | B no distingue formalmente spillover intraclúster vs interclúster | UNIT-03/06; P178-SIM-03 | Extensión de criterio/escenario pendiente; no nuevo ID |
| G111-03 | Diferencia de estimando ponderado UE vs cluster no operacionalizada | UNIT-06/12; P177-07/08; P178-SIM-03 | Requiere especificación de estimando/peso |
| G111-04 | C no especifica suficiencia/versión/cobertura del mapa (G_i) | UNIT-04/05/07/09 | Gap sustantivo del contrato; no crear test hasta decidir especialización |
| G111-05 | Probabilidades de exposición inducidas por aleatorización no derivadas | UNIT-09/11; QX-06 | Mapping mecanismo→exposición pendiente |
| G111-06 | Soporte conjunto por (z,e), estrato e historia no instanciado | UNIT-09; QX-05/06/07; INT-02 | Requiere soporte DGP y regla de adjudicación |
| G111-07 | D no tiene tasas/denominadores de falsa identificación, falsa abstención y abstención correcta | UNIT-08/10; P177-10/12; P183-11/12 | Especialización de Evaluator pendiente; P177-10 no basta |
| G111-08 | Aleatorización real y provenance completa siguen abiertas | UNIT-11; Gate 101/109 | No inventar algoritmo, clave o vector |
| G111-09 | El focal harness no materializa B/C/D ni G_i | README/harness; UNIT-04…10 | Fuera de alcance de implementación existente |
| G111-10 | O-CONF por instance×route y V_cont por UE×K aún no tienen mapping de agregación a estimando bajo cluster/exposición | Gate 109/110; P177-01/05; P179; P183 | Mantener resultados/unidades separados hasta mapping |
| G111-11 | C-MED bajo interferencia/exposición y confusión post-Z sigue parcial | Plan §225.3; P177-06/12; P182; P183 | No adjudicar C4 desde UNIT ni ITT |
| G111-12 | Sensibilidad a misspecification del mapa y spillover residual sin parámetros/reglas | UNIT-04/05/07; P178-SIM-10; P183-10 | Sensibilidad requerida, no cuantificada |

## 8. Reglas de no duplicación y estado de cobertura

1. UNIT-01…14 es la familia primaria de interferencia; no crear nuevos IDs paralelos.
2. P177/P178/P179/P182/P183 conservan su significado original.
3. INT-01/02 no se renombran como interferencia de unidades.
4. POL-01/02 distinguen atribución focal y vías directas; no sustituyen los contratos UNIT.
5. MEAS/MISS/TRJ son capas transversales, no nuevas unidades experimentales.
6. Cobertura definida ≠ test implementado; test implementado ≠ test ejecutado; test ejecutado ≠ aceptación científica.
7. La abstención correcta ante D debe contarse como resultado correcto, con denominador y verdad DGP; no se aceptan umbrales inventados.
8. No se puede inferir que los 35 test definitions mencionados por el PR cubren UNIT-01…14: hace falta mapping nominal a test source y a aserción; no se dispone de ese crosswalk en el material recuperado.

## 9. Dictamen y siguiente gate

**Dictamen:** GATE_111_CONTRACT_CROSSWALK_COMPLETED / UNIT_01_14_RECOGNIZED_AS_PRIMARY_INTERFERENCE_CONTRACTS / A_CONTRACT_DEFINED_IMPLEMENTATION_LIMITED / B_C_D_CONTRACT_PARTIAL / FOCAL_HARNESS_NO_CLUSTER_OR_EXPOSURE_ENGINE / P178_BENCHMARK_EXECUTION_RECORDED_BUT_NOT_ANALYZER_OR_INTERFERENCE_VALIDATION / TEST_RUN_STATUS_NOT_INFERRED / GAPS_111_01_12_OPEN / NO_NEW_TEST_IDS.

**Siguiente operación propuesta — Gate 112:** reconciliación de los gaps G111-01…12 contra el contrato DGP y el PE Integrated Technical Specification, determinando qué requisitos se pueden cerrar documentalmente con reglas ya existentes, cuáles exigen una especialización versionada de UNIT-01…14 y cuáles son dependencias de diseño que deben permanecer abiertas. Priorizar G111-02…07 y G111-10…11; no implementar motor de interferencia ni ejecutar pruebas.

## 10. Gobernanza y límites

- No se modifica `main`, RMA, Evidence→Claim Matrix, STATUS, Core, C09 ni claims.
- No se cambian DEC-C10-059/065/066/067/069/100/101/102, C0, Gate 109 o Gate 110.
- No se crean test IDs, fixtures, schemas, claves, tablas o DDL.
- No se ejecutan tests, workflows, benchmarks, simulaciones, estimaciones ni experimentos.
- No se altera el estado Draft del PR #116 ni se promueve la rama research.
- `scientific_execution=false`; `execution_authorized=false`.
