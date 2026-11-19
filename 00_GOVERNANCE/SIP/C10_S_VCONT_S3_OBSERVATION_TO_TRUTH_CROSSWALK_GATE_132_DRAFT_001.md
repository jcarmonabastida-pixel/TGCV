# C10-S — Gate 132: crosswalk S3 observación → truth V_cont y allowlist del Analyzer

**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** S3_SYNTHETIC_OBSERVATION_CHANNEL_IMPLEMENTED / IDEAL_MEASUREMENT_PATH_IMPLEMENTED_BY_CONTRACT / ADVERSE_MEASUREMENT_ABSTENTION_SCENARIO_PRESENT / ERROR_CORRECTION_NOT_IMPLEMENTED_OR_VALIDATED / TEMPORAL_RESOLUTION_LIMITED_TO_INTERVAL_GRID / VALUE_BRIDGE_NOT_ESTABLISHED / NO_DESIGN_FREEZE / NO_EXECUTION.  
**Precedencia:** contrato integrado V_cont §§1, 5–6; DEC-C10-099…102; Gate 131; Gates 126–128; `vcont_integrated_harness.py`; `vcont_benchmark_protocol.py`; Test Contract Register; P182/P183 y MEAS/MISS aplicables.

## 1. Pregunta y dictamen

¿El harness ya contiene un canal S3 observable y un mapping explícito entre su salida, la verdad sintética de V_cont y la información que puede utilizar el Analyzer?

**Sí, parcialmente.** La inspección estática confirma que S3 no es una mera propuesta documental: el Generator crea observaciones sintéticas de ENABLED y PROFILE por unidad e intervalo; introduce sensibilidad, especificidad y ausencia; el Sealer valida una allowlist; y el Analyzer construye V_cont observado desde esas señales. Existe un escenario adverso de medición que debe producir abstención y un test contractual correspondiente.

**Pero no existe una corrección calibrada/validada que permita identificar puntualmente V_cont con S3 imperfecto o incompleto.** La ruta numérica implementada requiere medición perfecta y completa. El canal actual tampoco representa eventos runtime con marcas temporales de alta resolución: sus observaciones son binarias y están indexadas por la rejilla de intervalos del DGP.

Resultado: `S3_CHANNEL_IMPLEMENTED / S3_IDEAL_PATH_CONTRACTED / S3_ADVERSE_ABSTENTION_CASE_PRESENT / ERROR_CORRECTION_NOT_IMPLEMENTED / INDEPENDENT_CALIBRATION_NOT_ESTABLISHED / INTERVAL_LEVEL_ONLY / NO_FREEZE`.

## 2. Reconstrucción de la truth del Generator

En `03_EXPERIMENTS/C10-S/harness/vcont_integrated_harness.py`:

1. El Generator conserva por unidad y régimen potencial los estados ENABLED y PROFILE en `potential_enabled_truth` y `potential_profile_truth`.
2. Construye por intervalo `potential_interval_truth` como la conjunción binaria de ENABLED y PROFILE.
3. Calcula el potencial `V_cont` de cada unidad/régimen como la media de esos estados de intervalo sobre `n_intervals`.
4. Conserva por separado los potenciales de V_cont, los estados de los dos componentes y el vector focal `potential_delta_t_acc`.
5. `theta_a_truth` permanece `None`; el benchmark actual estima contrastes de asignación ITT-Z e ITT-G, no θ_A.

Esta truth es conocida por el Generator y queda reservada en TruthBundle. No es observación S3 ni evidencia disponible para Analyzer.

## 3. Canal S3 realmente implementado

Para el régimen realizado de cada unidad, el Generator genera dos series observadas, con cardinalidad `n_intervals`:

- `s3_enabled`
- `s3_profile_match`

Cada componente se somete a:
- ausencia probabilística mediante `missing_probability`, codificada como valor `None` y estado `MISSING`;
- error binario mediante `measurement_sensitivity` y `measurement_specificity`, con estado `OBSERVED` cuando hay señal.

No se genera una señal temporal continua ni un event log con event-time, observation-time e ingestion-time. La unidad temporal observable es el intervalo sintético predefinido. Por ello, el canal actual puede estudiar error/ausencia por intervalo, pero no acredita detección de fallos breves intraintervalo ni resolución temporal inferior a Δ.

Los parámetros Se/Sp/missingness están presentes en ScenarioConfig y se usan para generar las observaciones. Su existencia en el DGP no equivale a que el Analyzer conozca parámetros de corrección ni a que estén calibrados contra una referencia independiente.

## 4. Allowlist y firewall: qué recibe cada componente

| Campo/capa | Generator / TruthBundle | EvidenceCandidate → Sealer → Analyzer | Evaluator |
|---|---|---|---|
| ENABLED y PROFILE verdaderos por intervalo | Sí | No | Acceso posterior mediante TruthBundle |
| Conjunción funcional por intervalo y potencial V_cont | Sí | No | Sí, tras sellado del resultado |
| ENABLED observado S3 | Genera | Sí: `s3_enabled` | Puede comparar después |
| PROFILE observado S3 | Genera | Sí: `s3_profile_match` | Puede comparar después |
| Estado de observación | Genera | Sí: `s3_enabled_status`, `s3_profile_status` | Sí |
| Asignaciones Z/G | Genera | Sí | Sí |
| `delta_t_acc_observed` | Genera | Sí, vector focal separado de S3 | Sí |
| Sensibilidad, especificidad y probabilidad de ausencia del DGP | Sí | No en filas observadas ni en allowlist | Truth/configuración reservada según contrato |
| Potenciales, truth V_cont, semillas y parámetros secretos | Sí | No | Sí, después del sellado |

El Sealer aplica una allowlist cerrada que incluye identificadores de unidad/clúster, asignaciones, estrato basal, las cuatro series/campos S3, `delta_t_acc_observed`, perfil y versión. Rechaza campos ausentes, adicionales o reservados y verifica cardinalidad/valores. La procedencia de asignación se conserva en un manifiesto separado.

**Distinción crítica:** `delta_t_acc_observed` no es una señal S3 de V_cont. Es el vector focal observado utilizado para la primera etapa. No debe confundirse con ENABLED/PROFILE ni con su verdad potencial.

## 5. Qué hace y qué no hace el Analyzer

El Analyzer verifica integridad del sello y correspondencia entre el contrato y la procedencia de asignación. Después:

1. exige las condiciones declaradas de asignación, soporte, ausencia de interferencia, medición identificada y consistencia de versión;
2. comprueba que los valores S3 no sean ausentes y que todos los estados de cobertura sean `OBSERVED`;
3. si esas condiciones se cumplen, calcula para cada unidad la media de la conjunción observada `s3_enabled AND s3_profile_match`;
4. estima separadamente ITT-Z e ITT-G|Z=0, manteniendo sus condiciones propias;
5. si falta medición identificada o cobertura, emite `INDETERMINATE` y no sustituye ausencias por cero ni usa complete-case.

ScenarioConfig impone que `measurement_identified=true` solo sea compatible con Se=1, Sp=1 y missingness=0. Por tanto, la identificación puntual actual es una ruta de medición ideal. El Analyzer **no** usa Se/Sp para corregir error, no estima un modelo de medición, no implementa bounds para S3 y no resuelve MNAR.

## 6. Evidencia adversarial existente y cobertura no demostrada

La matriz de escenarios incluye `R0_MEASUREMENT_ADVERSE` como `STATUS_ONLY` con abstención esperada `INDETERMINATE`. El test `test_measurement_adversity_requires_abstention` comprueba que Analyzer y Evaluator respetan esa abstención. Esto corrige una formulación demasiado amplia de Gate 131: sí existe un caso adversarial de medición y un test de software asociado.

El alcance es limitado:
- el caso adversarial prueba la clasificación/abstención del escenario; no demuestra recuperación bajo error;
- el contrato de matriz no convierte ese escenario en estimación numérica ni en calibración;
- no se ha acreditado aquí una submuestra de validación independiente para estimar Se/Sp;
- no se han materializado fixtures/oráculos de todos los MEAS/MISS para S3 ni parámetros/tolerancias aceptados;
- los tests que existen son evidencia técnica registrada, no una nueva ejecución de Gate 132.

P182-05…08 y P183-01…13 proporcionan criterios generales de reproducibilidad, acuerdo, error, ausencia, selección, censura, bounds y abstención. MEAS-01…14 y MISS-01…15 contienen casos reutilizables de medición y ausencia, pero su aplicabilidad debe conservar su ámbito exacto. El Test Contract Register también reutiliza etiquetas MEAS en otros subdominios de C10-S; no se deben fusionar filas homónimas sin namespace/ámbito y referencia de sección. Este gate no crea ni renumera IDs.

## 7. Dictamen de suficiencia por nivel

| Nivel | Estado | Qué permite afirmar |
|---|---|---|
| Truth sintética de ENABLED/PROFILE/V_cont | DEFINED / IMPLEMENTED IN SOURCE | El Generator conoce los potenciales por unidad e intervalo |
| Canal S3 sintético con Se/Sp/ausencia | IMPLEMENTED IN SOURCE | El DGP genera observaciones imperfectas por intervalo |
| Allowlist y sello de evidencia | IMPLEMENTED IN SOURCE; no revalidado aquí | Existe una frontera lógica de campos permitidos |
| Analyzer con medición ideal | IMPLEMENTED IN SOURCE; ruta contractual | Puede estimar ITT-Z/ITT-G si se satisfacen las condiciones y S3 es perfecto/completo |
| Adversidad de medición y abstención | SCENARIO + TEST SOURCE PRESENT | Existe un caso status-only y una aserción de abstención |
| Corrección de error Se/Sp | NOT IMPLEMENTED | No se recupera punto estimado bajo error |
| Bounds de V_cont bajo S3 imperfecto | NOT IMPLEMENTED / NOT VALIDATED | No hay estimación parcial acreditada |
| Calibración independiente S3 | NOT ESTABLISHED | No se han acreditado referencia y diseño de validación |
| Ausencia MCAR/MAR/MNAR específica S3 | PARTIAL DGP CAPABILITY / MECHANISM NOT IDENTIFIED | Hay ausencia generada, pero no mecanismo causal/auxiliares que justifiquen MAR/MNAR |
| Resolución temporal intraintervalo | NOT REPRESENTED | No se evalúa detección de interrupciones breves dentro de Δ |
| Puente V_cont → consecuencia B1 → Value | OPEN | V_cont sigue siendo Outcome mínimo provisional, no Value completo |

## 8. Corrección de alcance respecto a Gate 131

Gate 131 permanece válido en su conclusión central: no hay identificación puntual validada con medición imperfecta/ausente, ni recuperación de θ_A. Se precisa, sin reescribir el gate histórico, que:

- el canal S3 sintético sí está implementado en el harness;
- existe una ruta ideal de medición;
- existe al menos un escenario adverso de medición y un test de abstención;
- la insuficiencia reside en calibración/corrección/bounds, validación independiente y resolución temporal, no en ausencia total de observables o de casos adversariales.

## 9. Routing mínimo — Gate 133

No crear otro canal, nueva matriz ni familia de tests. El siguiente paso debe reconciliar únicamente:
1. el alcance exacto de `R0_MEASUREMENT_ADVERSE` y los contratos MEAS/MISS ya registrados;
2. si el benchmark ideal se puede tratar como baseline metodológico de recuperación de ITT-Z/ITT-G (sin afirmar robustez a error);
3. qué pruebas de software ya existen y cuáles solo están registradas como contratos;
4. el estado de los perfiles de ejecución/workflow que podrían ejecutar esas pruebas y el límite de autorización;
5. si la ruta de medición ideal corresponde exactamente a la regla temporal V_cont de DEC-C10-100…102, o si el mapping de rejilla/horizonte permanece parcial.

No elegir nuevos valores Se/Sp, missingness, T*, Δ, K, tasas, tolerancias, submuestras, N/R/M ni métodos de corrección. No ejecutar tests, workflow, calibración, generación, benchmark o experimento.

## 10. Límite de autorización

Auditoría estática de GitHub. No imports, compilación, tests, CI, dispatch, generación, simulación, calibración, estimación, empaquetado ni ejecución científica. No cambios en código, schemas, DEC, C0, U_G, test register, workflows, RMA, Evidence→Claim Matrix, STATUS, Core o main.

`scientific_execution=false`  
`execution_authorized=false`


**Límite adicional de la truth:** en el código actual, `potential_interval_truth` se materializa como conjunción binaria ENABLED∧PROFILE (0/1) para cada intervalo. La ausencia S3 produce `None` en el canal observado, no un estado desconocido de la truth del Generator. Por tanto, la semántica UNKNOWN de DEC-C10-100 y sus bounds por intervalos de truth desconocida no están materializados en este harness; no deben confundirse con missingness observacional. Gate 133 comprobará si esta diferencia está intencionadamente fuera del alcance del benchmark ideal o requiere una decisión de diseño antes del freeze.
