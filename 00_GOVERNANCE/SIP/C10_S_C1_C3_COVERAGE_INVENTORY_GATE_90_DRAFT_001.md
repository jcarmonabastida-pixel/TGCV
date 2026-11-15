# C10-S — Gate 90: inventario de cobertura científica C1/C3 contra el roster finito existente

**Estado:** STATIC COVERAGE AUDIT COMPLETE / C1 PARTIAL / C3 NOT MATERIALIZED / CURRENT-HEAD EXECUTION NOT VERIFIED / NO NEW WORLDS / NO SCIENTIFIC EXECUTION  
**Rama:** `research/c10-s-consolidation-draft`  
**HEAD auditado:** `c892dedbce748dba0572061c428c7c30582e04bc`  
**Precedencia:** Design Closure and Operationalization Plan Draft 004 §§16.225, 16.234–16.239; especialmente Gate 71 (doce roles C1/C3), Gate 81 (cobertura inicial), Gate 86 (G ≠ g_A), Gate 87–89 (separación de verdades y suite técnica).  
**Alcance:** cruzar los seis roles C1 y seis C3 con los escenarios y tests existentes; distinguir mecanismo/código, test declarado en el HEAD actual y ejecución técnica histórica. No modificar DGP, estimandos, parámetros, roster, políticas ni código. No ejecutar tests, benchmark ni experimento.

## 1. Reconstrucción histórica y procedencia

Se recuperaron desde `main` README, bootstrap, estado canónico, STATUS, regla de reconstrucción histórica y workflow técnico. La gobernanza canónica mantiene RMA v3.38 y Evidence→Claim Matrix v1.47. La línea de trabajo C10 continúa abierta; este gate no modifica `main`, Core, RMA, Matrix ni autorizaciones.

La especificación obligatoria de las doce celdas procede de Gate 71 (§16.225.2–.3), no de los nombres de escenarios ni de una reinterpretación posterior. El roster de escenarios se conserva cerrado: Gate 90 no añade mundos.

### Identidad de los artefactos examinados

| Artefacto | Blob actual en HEAD | Referencia ejecutada Gate 89 |
|---|---|---|
| `vcont_integrated_harness.py` | `88c6c7bd6f82353e64a4f12edbe2e2abc2cec002` | `ba0b588051cad1b7f5cf91af19200fdfaaa77f20` |
| `test_vcont_integrated_harness.py` | `1933f9b17cedce919adb3d60ac138d18320ef35e` | `b4fd8ea192ab145d990bee3e1087ebc12b665502` |
| `vcont_benchmark_protocol.py` | `8511f289224a885bdc69b2b494f4e6dd345fa8b8` | No se usa como evidencia de ejecución de Gate 89 |
| `.github/workflows/c10-s-focal-harness-tests.yml` | `1bc2253b4b6fa08e37aebc561e5b9aff287703cd` | El run Gate 89 probó otro commit/workflow state |

El run técnico de Gate 89 fue el run `43412059150`, commit `244896092e6414ccd92bd31a19776dcf71266c15`, con 33/33 tests en primaria y replay. El módulo integrado probado entonces tenía 16 métodos `test_*`. En el HEAD actual ese mismo módulo contiene 60 métodos declarados y su blob ha cambiado. Por tanto, el PASS de Gate 89 **no acredita** los 60 tests actuales ni el código actual.

El workflow actual es manual (`workflow_dispatch`), exige confirmación explícita y restringe la rama. No hay ejecución actual en HEAD `c892ded…` recuperada para este gate. No se ha solicitado ni realizado dispatch.

## 2. Roster finito actual

`benchmark_scenarios()` contiene 13 escenarios explícitos:
- R0: `R0_FOCAL_POSITIVE`, `R0_FOCAL_NULL`, `R0_FOCAL_ADVERSE`, `R0_DIRECT_G`, `R0_DIRECT_Z`, `R0_MEASUREMENT_ADVERSE`, `R0_INTERFERENCE`, `R0_SUPPORT_FAILURE`, `R0_HETEROGENEITY`;
- R1: `R1_ALTERNATIVE_BASELINE`;
- R2: `R2_ALTERNATIVE_AFFECTED`, `R2_SUPPORT_FAILURE_ZG_INTERACTION`;
- R3: `R3_PROVISION_FAILURE`.

La identidad de escenario está también restringida por el protocolo a 13 IDs y 52 pares escenario–estimando. No se ha inferido cobertura científica de esa cardinalidad.

## 3. C1 — efecto total de asignación D2 (seis roles)

| Celda Gate 71 | Escenarios/mecanismos existentes | Evidencia de test en el HEAD actual | Dictamen de cobertura |
|---|---|---|---|
| **C1-POS** — ITT-D2 positivo | `R0_FOCAL_POSITIVE` tiene primera etapa G positiva, pero en R0 Z no modifica provisión, alternativa ni outcome. `R0_DIRECT_Z` sí introduce efecto positivo de Z, pero es vía directa y no el control focal limpio exigido. R2 modifica alternativa y añade vía colateral; no es R0 limpio. | `test_clean_positive_recovers_package_and_g_assignment` comprueba estados identificados y primera etapa G, no que ITT-Z truth/estimate sea positivo. | **NOT COVERED.** Falta un contraste ITT-Z positivo en el control R0 limpio y su assertion de truth/recuperación. No resolverlo renombrando `R0_DIRECT_Z`. |
| **C1-NULL** — ITT-D2 exactamente cero | `R0_FOCAL_NULL` fija `focal_access_effect=0`; en R0 Z no tiene otro mecanismo activo. La truth ITT-Z se calcula desde potenciales. | `test_null_and_adverse_truth_signs_are_preserved` verifica el nulo de `itt_g_z0_truth`, no el nulo de `itt_z_truth`. | **PARTIAL / NOT ACCREDITED.** Hay configuración compatible y truth computable, pero falta test explícito de ITT-Z nulo propio y su adjudicación. |
| **C1-NEG** — ITT-D2 negativo | `R3_PROVISION_FAILURE`: Z reduce la probabilidad de provisión focal; el código genera una vía adversa. | `test_r2_collateral_alternative_and_r3_provision_are_separate` comprueba `truth3.itt_z_truth < 0` y estado package identificado. Este test existía en el blob ejecutado por Gate 89. | **PARTIAL / HISTORICAL TEST PASS.** Signo de truth y estado identificable están comprobados; no hay assertion explícita de recuperación del signo/magnitud ITT-Z en ese test. |
| **C1-DECOUPLED** — ITT no nulo con efecto focal nulo/no identificable | `R0_DIRECT_Z`, `R0_DIRECT_G`, R2 y R3 contienen vías directas/colaterales; TruthBundle separa ITT-Z, ITT-G y `theta_a_truth=None`. | Tests de separación de truth, vía directa G y vía directa Z. | **PARTIAL / NOT A COMPLETE CELL.** Los mecanismos y el firewall están presentes, pero no existe par adjudicable ITT-Z / θ_A: θ_A está no materializado, no establecido como nulo o no identificado para una celda evaluable. |
| **C1-HET** — efectos condicionales ITT con signos opuestos | `R0_HETEROGENEITY` usa coeficiente `heterogeneity=0.20`; con `focal_access_effect=0.20`, el término condicional `0.20 + 0.20(x−0.5)` permanece positivo para x∈[0,1]. | No hay truth ITT-Z estratificada, estimador por estrato ni test de recuperación de signos opuestos. | **NOT COVERED.** El parámetro nominal de heterogeneidad no produce la heterogeneidad de signos opuestos requerida por Gate 71; no hay análisis condicional. |
| **C1-ABSTAIN** — falta identificación/observación/interferencia | `R0_MEASUREMENT_ADVERSE`, `R0_INTERFERENCE`, `R0_SUPPORT_FAILURE`, `R2_SUPPORT_FAILURE_ZG_INTERACTION`. | Tests de medición adversa, interferencia, soporte, shortfall de brazos, interacción Z×G y consistencia/versiones. Parte de la batería existía y se ejecutó en Gate 89; el HEAD actual añade más tests no ejecutados en ese run. | **PARTIAL / MECHANISM COVERED.** La abstención ITT por medición/interferencia está representada. El soporte G fallido puede dejar ITT-Z identificado por transportabilidad; no contarlo erróneamente como abstención de ITT-Z. |

### Hallazgo estructural C1-POS

En el Generator actual, para R0:
- la probabilidad de provisión es independiente de Z;
- la alternativa es independiente de Z;
- el término de efecto directo de paquete es cero en el escenario focal limpio;
- el efecto focal `focal_access_effect` opera con G, no con Z.

La única modificación de provisión por Z está codificada para R3 como reducción `−0.20*z`; el efecto positivo directo de Z aparece en `R0_DIRECT_Z`, que no es focal limpio. Por ello el roster no contiene hoy una celda C1-POS limpia. Es una ausencia real de mecanismo/verdad de referencia, no una ausencia de test que pueda repararse solo añadiendo una assertion.

## 4. C3 — efecto de intervención focal sobre ΔT_acc* completo (seis roles)

| Celda Gate 71 | Escenarios/mecanismos existentes | Evidencia de test en el HEAD actual | Dictamen de cobertura |
|---|---|---|---|
| **C3-POS** — θ_A positivo bajo g_A1/g_A0 | `R0_FOCAL_POSITIVE` genera vector ΔT_acc* con G, pero no hay par operativo de políticas conjuntas g_A ni q_X*. | No hay truth θ_A ni estimador θ_A. | **NOT MATERIALIZED.** El efecto G no es sustituto de θ_A. |
| **C3-NULL** — θ_A nulo propio | `R0_FOCAL_NULL` hace cero el coeficiente de resultado focal para G, pero no representa por sí solo el contraste de políticas conjuntas versionadas bajo q_X*. | El test existente verifica el nulo de ITT-G, no θ_A. | **NOT MATERIALIZED.** No existe verdad/estimador focal que distinga nulo propio de saturación, alternativa o cancelación. |
| **C3-NEG** — θ_A negativo | `R0_FOCAL_ADVERSE` hace negativo el término focal de G. | El test de signos adversos verifica ITT-G, no θ_A. | **NOT MATERIALIZED.** No hay verdad independiente ni recuperación de θ_A. |
| **C3-DECOUPLED** — vía directa/colateral impeditiva | `R0_DIRECT_G`, `R0_DIRECT_Z`, R2 y R3 generan vías no focales. | Tests prueban separación ITT-G y θ_A no materializado y mantienen firewall. | **MECHANISMS ONLY.** No se evalúa θ_A en mundos limpios/directos/colaterales porque la truth y el estimador no existen. |
| **C3-HET** — θ_A condicional de signos opuestos | `R0_HETEROGENEITY` modula el término de outcome por `baseline_x`; no produce truth focal estratificada. | No hay estimador ni tests de heterogeneidad focal por estrato. | **NOT COVERED.** Falta truth condicional, soporte por historia y evaluación estratificada. |
| **C3-ABSTAIN** — no identificación/identificación parcial | Escenarios de soporte, medición, interferencia y vías directas están presentes para ITT-G. | Tests verifican abstención de ITT-G y estados de soporte. | **NOT A C3 CELL.** El Analyzer no emite estado de identificación de θ_A; `theta_a_truth=None` no equivale a `NOT_IDENTIFIED` ni a `PARTIALLY_IDENTIFIED`. No hay bounds. |

**Dictamen C3:** los seis roles permanecen sin materialización científica. El contraste de asignación G es un objeto distinto. Gate 86 ya resolvió que G no puede reutilizarse como g_A; el par de políticas conjuntas, q_X* y certificación r_common siguen bloqueados por falta de dominio conjunto, historias, masas y soporte.

## 5. Discrepancia de precedencia detectada en el código

La docstring inicial del módulo actual afirma que la asignación aleatorizada G es una intervención sintética explícita sobre el cambio focal completo `g_A`. Esto contradice Gate 86 (§16.236.1–.2), que rechaza reutilizar G como g_A, y Gate 87–89, que mantienen `theta_a_truth=None` hasta materializar políticas conjuntas aprobadas y q_X*.

La implementación actual distingue correctamente el contraste G de la truth θ_A, pero la docstring no refleja esa distinción. Se registra como **documentación semántica obsoleta**, no se corrige en este gate porque Gate 90 es de auditoría de cobertura y no de modificación de código. Debe corregirse en el siguiente gate de reconciliación de contrato, sin alterar el comportamiento del Generator.

## 6. Separación de estados de evidencia

| Capa | Estado |
|---|---|
| Roster | 13 escenarios definidos en el código actual |
| Mecanismos Generator | Parcialmente implementados; G, Z, vías directas, R2/R3, medición, interferencia y soporte |
| Truth ITT-Z / ITT-G | Implementada |
| Truth θ_A | No materializada (`None`) |
| Analyzer ITT-Z / ITT-G | Implementado con estados de identificación y abstención |
| Analyzer θ_A | Ausente |
| Truth/estimación por estrato de signos opuestos | Ausente |
| Bounds / identificación parcial | Ausentes |
| Tests declarados en módulo integrado actual | 60 |
| Tests del módulo integrado en commit Gate 89 | 16 |
| Ejecución Gate 89 | 33/33 primaria y 33/33 replay en commit anterior |
| Ejecución del HEAD actual | No verificada / no ejecutada en Gate 90 |
| Benchmark Monte Carlo C1/C3 | No ejecutado |
| Ejecución científica confirmatoria | No realizada ni autorizada |

No se usa el PASS técnico de Gate 89 para inferir cobertura de C1/C3. El cambio de blobs entre el commit ejecutado y HEAD actual impide transferir ese resultado a la versión actual sin una nueva ejecución técnica autorizada.

## 7. Disposición y siguiente operación

**Gate 90 cerrado como inventario estático de cobertura.**

Dictamen:
`GATE_90_STATIC_C1_C3_COVERAGE_INVENTORY_COMPLETE / C1_PARTIAL_WITH_C1_POS_MISSING_AND_C1_HET_MISSING / C3_NOT_MATERIALIZED / 13_SCENARIO_ROSTER_RETAINED / GATE_89_PASS_BOUNDED_TO_2448960 / CURRENT_HEAD_NOT_EXECUTED / STALE_G_EQUALS_G_A_DOCSTRING_FOUND / NO_NEW_WORLDS / NO_CODE_CHANGE / NO_BENCHMARK / NO_SCIENTIFIC_EXECUTION / NO_DESIGN_FREEZE`.

**Siguiente operación — Gate 91:** resolver documentalmente, sin ampliar el roster, el contrato causal de C1-POS y la discrepancia G/g_A:
1. determinar si el mecanismo de D2/Z debe abrir una vía focal positiva en el R0 limpio o si el diseño actual no puede representar esa celda;
2. fijar qué verdad/estimador debe demostrar C1-POS y cómo se distingue del efecto G;
3. corregir la docstring obsoleta contra Gate 86–89;
4. mantener θ_A no materializado hasta que g_A0/g_A1, q_X* y r_common sean realmente factibles;
5. decidir si la cobertura C1-HET requiere una configuración dentro del roster existente o queda como ausencia científica explícita.
No modificar DGP ni código antes de resolver el contrato; no crear mundos, políticas, parámetros ni masas; no ejecutar tests ni benchmark en ese gate.
