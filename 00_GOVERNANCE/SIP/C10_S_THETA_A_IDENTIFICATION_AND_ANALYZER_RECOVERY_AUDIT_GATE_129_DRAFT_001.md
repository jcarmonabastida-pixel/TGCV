# C10-S — Gate 129: identificabilidad y recuperación de θ_A sobre V_cont

**ID:** C10-S-THETA-A-IDENTIFICATION-ANALYZER-RECOVERY-129  
**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft; base `research/c10-d1-protocol-draft`)  
**Estado:** THETA_A_ESTIMAND_DEFINED / FULL_VECTOR_G_A_INTERVENTIONS_NOT_MATERIALIZED / Q_X_AND_R_COMMON_NOT_MATERIALIZED / IDENTIFICATION_NOT_ESTABLISHED / VCONT_S3_MEASUREMENT_NOT_VALIDATED / CURRENT_ANALYZER_DOES_NOT_ESTIMATE_THETA_A / P178_BOUNDED_METHOD_BENCHMARK_ONLY / NO_DESIGN_FREEZE / NO_IMPLEMENTATION / NO_NEW_EXECUTION  
**Precedencia:** DEC-C10-095…103; DEC-C10S-D2-ESTIMAND-SEPARATION-001; Gate 110; Gates 69–86; Gates 90–93; Gates 111–125; Gates 126–128; plan §§16.188–16.223, 16.226–16.227, 16.231–16.243; DGP Temporal and Role Contract; Test Contract Register §13, §17 and P177/P178/P179/P182/P183; P178 clean replay audit.

## 1. Pregunta y dictamen ejecutivo

¿Está identificado y puede recuperarse por el Analyzer el estimando focal aceptado `θ_A(q_X*, r_common; V_cont)), que interviene sobre la distribución conjunta del vector completo `ΔT_acc*`, y qué evidencia/condiciones faltan?

**Dictamen:** el estimando está definido y seleccionado por DEC-C10-103, pero no está materializado como contraste operacional ni identificado por el diseño/harness actual. El ledger existente especifica los campos y reglas necesarios, pero sus filas por historia/celda, masas de `q_X*`, políticas conjuntas `g_A0/g_A1`, soporte y `r_common` no están materializados. El Generator integrado mantiene `theta_a_truth=None` hasta que se aprueben/materialicen esas intervenciones y la población objetivo. El Analyzer integrado estima ITT-Z y contrastes de asignación G; no estima θ_A. El contraste G no puede renombrarse como θ_A.

P178 aporta un benchmark metodológico ejecutado y reproducido para un estimador bajo supuestos ideales y una variable escalar `Q_B1`. No demuestra recuperación de θ_A sobre el vector completo `ΔT_acc*`, ni medición S3 de `V_cont`, ni robustez a interferencia, falta de soporte, vías directas, error de medición o missingness. Su PASS debe conservarse en su alcance original.

**Resultado:** `THETA_A_DEFINED_BUT_NOT_MATERIALIZED / IDENTIFICATION_NOT_ESTABLISHED / ANALYZER_RECOVERY_NOT_DEMONSTRATED / P178_BENCHMARK_REPRODUCIBILITY_PASS_BOUNDED / NO_FREEZE`.

## 2. Reconstrucción y reutilización obligatoria

Gate 129 no crea otra matriz de identificación, otro ledger ni nuevas familias de tests. Reutiliza:

| Artefacto | Contenido reutilizable | Estado que no debe exagerarse |
|---|---|---|
| DEC-C10-103 §5 | θ_A focal sobre vector completo; ITT-D2 separado; C4 secundario condicionado; sin residual por resta | Selección de estimando, no identificación |
| Plan §16.223 / Gate 69 | Ledger por celda, historia, soporte, `q_X*`, `g_A`, `r_common`, interferencia y canal | Esquema cerrado; filas y valores no materializados |
| Plan §§16.226–16.227 / Gates 73–74 | Tres verdades, definición contrafactual, criterio G≠g_A, evidencia observable y abstención | Contratos analíticos documentales; θ_A y bounds no implementados |
| Plan §§16.231–16.236 / Gates 78–86 | Factibilidad por historia, soporte conjunto y separación entre G y g_A | No existe par operativo g_A0/g_A1 ni soporte certificado |
| Plan §§16.240–16.243 / Gates 90–93 | Cobertura del harness, ausencia de cadena D2 y crosswalk de etapas | Cadena D2 no representada de forma completa en el harness |
| DEC-C10-099…102 | V_cont seleccionado, agregación temporal, inicio t0 y continuidad estricta | T*, Δ, K y validez/detectabilidad S3 siguen abiertos |
| DEC-C10-103 | Asignación individual UE preferida solo bajo aislamiento; target promedio UE; θ_A aceptado como estimando | Aislamiento, roster, asignación, soporte y estimación permanecen condicionales |
| Test Contract Register | P177, P178-SIM, P179, P182, P183, UNIT, MEAS, MISS, QX, XSYNC | Contratos de diseño; no todos implementados/ejecutados |
| P178 clean replay audit | 27 celdas, N=700, R=10.000/celda, 270.000 invocaciones; replay byte-identical; 17/17 tests en aquel workflow | Benchmark no confirmatorio de `Q_B1`, no experimento C10-S completo |

## 3. El estimando: definido, pero no operacionalizado

DEC-C10-103 acepta `θ_A(q_X*,r_common;V_cont)` como efecto focal de dos intervenciones `g_A1` y `g_A0` sobre la distribución conjunta del vector completo `ΔT_acc*`, estandarizadas sobre la misma distribución objetivo de historias basales `q_X*` y el mismo régimen no focal `r_common`.

Se mantienen las distinciones ya aceptadas:

- `P_w`: cohorte finita pre-Z del ITT-D2.
- `q_X*`: distribución objetivo de historias basales para el estimando focal; masas positivas que suman uno.
- `π_h`: probabilidades de asignación en la unidad de asignación; no son masas de `q_X*`.
- `g_A0/g_A1`: políticas/intervenciones conjuntas sobre el vector completo `ΔT_acc*); no son Z, G, ni una primera etapa parcial.
- `r_common`: régimen no focal común y explícito; no se presume por igualdad de nombres ni por omisión.
- `Need_preZ`: objeto basal propio; no es sustituto de elegibilidad causal, historia `X/H0/C_c` ni de `q_X*`.

La fórmula del estimando no especifica por sí sola cómo se asignan las políticas, qué distribuciones conjuntas son factibles, qué historias tienen masa, qué observaciones identifican los contrafactuales o qué estimador debe utilizarse.

## 4. Bloqueos de identificación por condición

| Condición necesaria | Requisito de identificación | Estado reconstruido |
|---|---|---|
| Población objetivo | Roster causal B versionado, pertenencia pre-Z y definición de `q_X*`; separar A/B y censo Need_preZ | OPEN / NOT MATERIALIZED |
| Historias basales | Historias conjuntas `X,H0,C_c` o representación contractual equivalente, con referencias y masas | OPEN; no hay filas/masas de `q_X*` |
| Intervenciones focales | Reglas versionadas `g_A0/g_A1` sobre las cuatro coordenadas de `ΔT_acc*`, con dependencias conjuntas y factibilidad | OPEN; no existe par operativo |
| Soporte conjunto | Ambas políticas factibles y con soporte para cada historia de masa positiva bajo `q_X*`; sin extrapolación | OPEN / NOT ESTABLISHED |
| Régimen no focal | `r_common` idéntico en los dos mundos contrafactuales, o diferencias no focales identificadas separadamente | OPEN por celda; no inferible de etiquetas iguales |
| Consistencia/versiones | Correspondencia inequívoca entre intervención definida, vector generado, versión y resultado | Parcialmente contractual; cadena D2 incompleta |
| Asignación/unidad | Mecanismo de asignación y unidad independiente compatibles con el estimando; UE=UA solo si aislamiento demostrado | Individual UE preferida, CONDITIONAL |
| Interferencia | Ausencia por construcción y evidencia sintética/harness, o arquitectura de cluster/mapa `G_i` con estimando y soporte propios | OPEN; no presumir SUTVA |
| Vías directas/colaterales | Diferenciar paquete/otras vías de la intervención focal; no atribuir a θ_A cambios no focales | Mecanismos inventariados; celdas/soporte no materializados |
| Medición de V_cont | Verdad temporal DEC-C10-100…102 y canal S3 válido, calibrado y con cobertura suficiente | Truth definida parcialmente; S3 y parámetros temporales OPEN |
| Ausencia/censura | Mecanismo y análisis por estimando; bounds cuando proceda; desconocido no es cero | Contratos P183; materialización/validación OPEN |
| Inferencia | Estimador coherente con el mecanismo y el soporte; incertidumbre, sensibilidad y precisión justificadas | No existe estimador θ_A implementado/validado |
| Adjudicación | Evaluator compara salida sellada con truth de θ_A después de la salida del Analyzer | Arquitectura lógica; verdad focal aún no materializada |

Una condición que solo figura como booleano o supuesto en `AnalysisContract` no se convierte por ello en evidencia verificada. El Analyzer debe distinguir OBSERVABLE/VERIFIABLE, DECLARED_NOT_VERIFIED, ASSUMPTION_NOT_TESTABLE, FAILED y UNKNOWN conforme a Gate 74. UNKNOWN no se convierte en PASS.

## 5. G, ITT-D2, θ_A y C4 no son intercambiables

DEC-C10-103 y el plan §16.226 mantienen tres objetos distintos:

1. **ITT-D2 / ITT-Z:** efecto total de asignar el paquete D2 sobre V_cont. Incluye todas las vías que el paquete active.
2. **ITT-G|Z=0:** efecto de asignar G dentro de Z=0. Incluye fallos de provisión y otras vías de G permitidas por el DGP.
3. **θ_A:** efecto de intervenir directamente sobre la distribución conjunta del vector completo `ΔT_acc*`, manteniendo `q_X*` y `r_common` comunes.

La igualdad ITT-G|Z=0 = θ_A requiere, entre otras condiciones, que G implemente exactamente `g_A1/g_A0` o exista transporte identificador válido, ausencia de vías directas diferenciales, régimen no focal común, factibilidad/soporte conjunto, consistencia, medición e interferencia resueltas. No hay evidencia de que esas condiciones se cumplan. No se calcula θ_A dividiendo por la primera etapa de G ni aplicando Wald automáticamente.

C4 sigue siendo mediación interventional longitudinal secundaria y condicionada; no se deriva algebraicamente de ITT-D2 ni de θ_A. No se define un efecto residual por resta.

## 6. Auditoría del Generator, Sealer, Analyzer y Evaluator

### 6.1 Generator / truth

La estructura actual de `vcont_integrated_harness.py` conserva por separado `itt_z_truth`, `itt_g_z0_truth` y `theta_a_truth`. El propio contrato tipa `theta_a_truth` como opcional y declara que permanece ausente hasta que se materialicen las políticas conjuntas `g_A` y `q_X*`. Esto es coherente con la especificación científica: no fabrica θ_A a partir de G.

No obstante, el harness genera potenciales indexados por Z/G y cuatro coordenadas de `ΔT_acc*` en ese régimen. La cadena D2 (B, W_programmed, W_attempt, recepción, S_install, C_dep*, A_f*, D_f*) no está separada de forma completa. Gate 92 ya confirmó que `provision_ok` no sustituye las etapas ausentes y que la primera etapa actual es G→ΔT_acc*, no D2/Z→ΔT_acc*.

### 6.2 Sealer / evidencia observada

El canal sellado y su provenance preservan la separación de roles a nivel de aplicación. Pero la cobertura observacional que el Analyzer necesita para θ_A no está especificada/materializada: no hay evidencia de asignación a `g_A`, soporte por historia, ni un canal S3 validado para V_cont bajo error, pérdida, lag y dependencia. Un hash acredita integridad del paquete, no identificación causal ni ausencia de interferencia.

### 6.3 Analyzer

El Analyzer integrado produce ITT-Z, ITT-G y resultados de régimen de referencia. No estima θ_A sobre intervenciones conjuntas del vector. La salida focal del harness previo y su campo histórico `theta_access_truth` no se deben reinterpretar como θ_A: Gate 86 y §16.226.4–.5 ya identificaron que el contraste G es ITT-G|Z=0.

La implementación de `AnalysisContract` que exige flags como aleatorización, common regime, positivity, measurement ideal e interference absent es una condición contractual de entrada; si esos flags no se respaldan por evidencia/certificados observables, no prueban que los supuestos se cumplan.

### 6.4 Evaluator

El patrón de Evaluator abre truth después de que el Analyzer produce y sella su salida. Debe mantener separadas las adjudicaciones de ITT-Z, ITT-G|Z=0 y θ_A, y detectar tanto la falsa atribución G→θ_A como la estimación puntual cuando falta identificación. Hoy no hay `theta_a_truth` materializada contra la que adjudicar recuperación focal.

## 7. Qué demuestra y qué no demuestra P178

P178 tiene un cierre real de reproducibilidad computacional: 27 celdas, N=700 con asignación balanceada 1:1, R=10.000 por celda, 270.000 invocaciones; replay limpio byte-identical y 17/17 contract tests PASS en el workflow registrado.

Su propio manifiesto declara `benchmark estimator only`, sin TGCV Analyzer confirmatorio, sin escenarios adversariales de medición y sin experimento confirmatorio. El script usa una variable escalar `Q_B1`, un benchmark de diferencia de medias y un `AnalysisContract` con supuestos fijados como verdaderos: asignación aleatoria, vía directa ausente, régimen común, positividad, consistencia de versiones, medición ideal e interferencia ausente. La truth de referencia se suministra al Evaluator después de producir el resultado del Analyzer.

Por tanto P178 acredita únicamente reproducibilidad y recuperación en esa clase restringida de benchmark. No acredita:
- la intervención sobre el vector completo `ΔT_acc*`;
- `q_X*`, `g_A0/g_A1` o `r_common` materializados;
- identificación de θ_A en el DGP B confirmatorio;
- medición de V_cont por S3;
- bounds/abstención bajo falta de soporte o interferencia;
- recuperación ante vías directas/colaterales, medición degradada, missingness o MNAR;
- Design Freeze ni la afirmación TGCV `ΔT_acc* → Value`.

No se reabre P178 ni se propone repetirlo. Se reutiliza como control metodológico limitado.

## 8. P177/P179/P182/P183: cobertura contractual y límites

- **P177-01…12:** cubre ITT, primera etapa, Wald/IV, O/V separados, ajuste basal, ATE/ATT, heterogeneidad, multiplicidad, recuperación sintética y separación entre efecto de política y atribución. Son contratos de aceptación, no pruebas todas implementadas.
- **P179-01…08:** cubre separación A/O/V, vector Value, independencia de medición, contexto/autoridad, baseline, discordancias, estimación por dimensión y agregación. VCONT-B1-MIN cierra solo el criterio ordinal de la dimensión unitaria seleccionada; no convierte P179 completo en PASS ni autoriza Value global.
- **P182-01…12:** cubre validez de constructo, circularidad, especificación O/V, reproducibilidad, acuerdo, error, invariancia, sensibilidad, separación de datos y trazabilidad. La validez de V_cont/S3 no queda demostrada por la truth del Generator.
- **P183-01…13:** cubre taxonomía/mecanismo de ausencia, separación de A/O/V, conservación ITT, selección postasignación, mediación, censura, sensibilidad MAR/MNAR, bounds y dictamen por estimando. Los contratos no acreditan que esos escenarios estén materializados o que las salidas de bounds estén implementadas/validadas.

No se crean nuevos test IDs. Se mantienen las familias ya registradas.

## 9. Disposición por estado epistemológico

| Objeto | Estado |
|---|---|
| Definición de θ_A sobre vector completo | DEFINED / ACCEPTED AS ESTIMAND |
| Población causal B y `q_X*` | DEFINED SYMBOLICALLY / NOT MATERIALIZED |
| `g_A0/g_A1` | DEFINED AS REQUIRED INTERVENTIONS / NOT OPERATIONALIZED |
| `r_common` | RULE DEFINED / NOT CERTIFIED PER CELL |
| Soporte/factibilidad conjunta | NOT ESTABLISHED |
| Asignación individual UE | PREFERRED / CONDITIONAL ON SYNTHETIC ISOLATION EVIDENCE |
| Cluster / `G_i` | ALTERNATIVES DOCUMENTED / NOT SELECTED OR MATERIALIZED |
| Truth focal θ_A | NOT MATERIALIZED IN CURRENT HARNESS |
| Analyzer θ_A | NOT IMPLEMENTED / NOT RECOVERED |
| V_cont truth | TEMPORAL RULE PARTIALLY ACCEPTED |
| S3 measurement validity | OPEN / NOT VALIDATED |
| P178 benchmark | EXECUTED / AUDITED / REPRODUCIBILITY PASS / BOUNDED |
| P177/P179/P182/P183 | CONTRACTS REGISTERED / PARTIAL IMPLEMENTATION AT MOST / NO GLOBAL PASS |
| Value interpretation | VCONT-B1-MIN ACCEPTED FOR BOUNDED FUNCTIONAL-CONTINUITY DIMENSION ONLY |
| Design Freeze | NOT READY |

## 10. Secuencia mínima para resolver los bloqueos — sin ampliar el universo

1. **Cerrar materialización documental del contrato focal:** precisar, usando únicamente el ledger existente, qué contrato y representación existentes pueden especificar `q_X*`, las historias basales, `g_A0/g_A1` y `r_common`; no asignar valores ni masas.
2. **Cerrar la arquitectura sintética de asignación/interferencia:** determinar si el DGP/harness puede demostrar aislamiento individual por construcción y trazas, o si el diseño requiere cluster/mapa `G_i`; si no se representa o no se identifica, fijar bounds/abstención.
3. **Reconciliar la cadena D2 con el Generator:** completar documentalmente el crosswalk de etapas ya definido en Gate 92 y determinar si el diseño existente permite generar la intervención focal sin confundir D2/Z, G y `g_A`.
4. **Cerrar el contrato de observación V_cont:** resolver parámetros temporales y suficiencia de S3, con los contratos MEAS/MISS/P182/P183 existentes; mantener unknown y bounds.
5. **Especificar el contrato de identificación del Analyzer:** definir qué información sellada identifica el contraste, qué certificados de diseño son observables, qué supuestos son no testables y las condiciones exactas de abstención/bounds.
6. **Solo después** revisar si el ledger existente puede poblarse sin nuevos escenarios, y si los criterios cuantitativos aceptados de §16.219 pueden aplicarse sin inventar MDE, N, R, tolerancias o potencia.

El siguiente trabajo debe ser un cierre de dependencias por artefacto y no otro inventario genérico. La decisión de estimador/estrategia de identificación no debe anticiparse hasta que las intervenciones y el soporte estén especificados.

## 11. Dictamen final y autorización

Gate 129 confirma que la arquitectura causal de θ_A está conceptualmente definida, pero no hay todavía un experimento sintético C10-S capaz de identificar y recuperar ese estimando. El benchmark P178 no llena esa brecha. La próxima tarea es resolver las especificaciones de intervención, población/soporte y observación dentro del DGP sintético existente; no buscar sistemas reales, no crear escenarios adicionales y no sustituir el estimando por ITT-D2 o ITT-G.

No se modifica código, schema, roster, test register, DEC, C0, U_G, RMA, Evidence→Claim Matrix, STATUS, Core o `main`. No se ejecutan validadores, tests, workflows, generación, simulaciones, calibraciones, estimaciones o experimentos. No se promueve research a main.

`scientific_execution=false`  
`execution_authorized=false`

**Siguiente operación:** Gate 130 — reconciliación focal de los contratos existentes de `q_X*`, `g_A0/g_A1` y `r_common` frente al ledger §16.223 y la especificación de potenciales §16.226, determinando el mínimo contrato operativo ya disponible y el bloqueo exacto que impide materializar `theta_a_truth`. No crear nuevas políticas, historias, masas, parámetros, IDs o escenarios.
