# C10-S — Gate 91: reconciliación de D2/Z, Generator y la ausencia de C1-POS

**Estado:** D2 MATERIAL POLICY ↔ GENERATOR MISMATCH CONFIRMED / C1-POS NOT REPRESENTABLE IN CURRENT R0 / G ≠ g_A PRECEDENCE RECONFIRMED / PARAMETERIZATION OPEN / NO CODE CHANGE / NO EXECUTION  
**Rama:** `research/c10-s-consolidation-draft`  
**HEAD de referencia:** `e43f9601021ec90edbb775cfbaa19479c4d6f8a2` (Gate 90 integrado; fuentes de código identificadas por blob en §1).  
**Precedencia:** DEC-C10-066, DEC-C10-067, DGP Temporal and Role Contract, Design Closure Plan §§16.225, 16.234–16.240, especialmente Gate 86–90.  
**Alcance:** resolver documentalmente si la configuración R0 existente puede representar el efecto positivo de la asignación material D2/Z, identificar el mapping ausente y reconciliar la terminología G/g_A. No cambiar código, DGP, escenarios, parámetros, estimandos o decisiones aceptadas; no ejecutar.

## 1. Fuentes y versiones recuperadas

| Fuente | Identidad |
|---|---|
| DEC-C10-066 | `f7dd31b217e0bb2e4c92367b48bf296938bc7883` |
| DEC-C10-067 | `2c3e1dbff4c83ded910a1fd8ca0a47a602df2213` |
| DGP Temporal and Role Contract | `d893983c57a4aac5a13f0d5cc2734e9798ca6181` |
| Generator actual | `88c6c7bd6f82353e64a4f12edbe2e2abc2cec002` |
| Test module actual | `1933f9b17cedce919adb3d60ac138d18320ef35e` |
| README del harness actual | `f835b92d06aec9693c24ce92d82e0d47de3be1cf` |

No se ha modificado ninguna de estas fuentes.

## 2. Contrato material D2 que prevalece

DEC-C10-066 mantiene D2 como escenario primario candidato: control sin intento focal programado y tratamiento con intento focal programado. D1 permanece secundario.

DEC-C10-067 acepta conceptualmente:
- (B_{g0}^{D2}): no programar ni iniciar intento focal; registrar cualquier provisión de fondo/crossover.
- (B_{g1}^{D2}): programar el intento de despliegue/configuración focal, con artefacto/versionado, actor, recepción y verificación diferenciadas.
- La secuencia material es (Z ightarrow B_{gZ}^{D2} ightarrow W_{programmed} ightarrow W_{attempt} ightarrow S_{install} ightarrow C_{dep}^{*} ightarrow A_f^{*} ightarrow D_f^{*}).
- (P(W_{programmed}=1mid Z=0)=0) y (P(W_{programmed}=1mid Z=1)=1) son las probabilidades candidatas de programación de D2.
- La programación no garantiza intento efectivo, recepción, instalación, (C_{dep}^{*}), (A_f^{*}) ni (D_f^{*}).
- El cumplimiento/recepción, éxito técnico condicional, reintentos y fallos parciales siguen sin valores cuantitativos aprobados. (s=0.80) es hipótesis no validada.
- Recursos no focales, autorización normativa basal y otras condiciones no focales se mantienen comunes en el DGP aislado; cualquier cambio inducido por B se registra como vía colateral.

Esta semántica no puede sustituirse por un efecto directo Z→Outcome ni por una asignación auxiliar G.

## 3. Implementación efectiva del Generator actual

La lectura estática del blob actual confirma:

1. `ScenarioConfig` no tiene campos/eventos separados para `W_programmed`, `W_attempt`, recepción, `S_install` ni componentes verificados de `C_dep*`. Tiene un único `provision_probability`.
2. En el bucle de potenciales `(z,g)`, R0 utiliza `provision_p = cfg.provision_probability`, sin dependencia de Z.
3. El mismo exógeno `u_provision` genera `provision_ok`; la disponibilidad focal `delta_vector` depende de `g == 1`, `provision_ok` y los cuatro umbrales exógenos. No depende de Z en R0.
4. Solo R3 modifica `provision_p` según Z, y lo hace como fallo adverso: `provision_p = cfg.provision_probability - 0.20*z`.
5. R2 modifica la probabilidad de alternativa según Z y añade una vía colateral; no es el contraste focal limpio.
6. `R0_DIRECT_Z` añade `package_direct_effect * z), que constituye una vía directa, no el mecanismo material de provisión focal.
7. `R0_FOCAL_POSITIVE` produce primera etapa G sobre el vector, pero Z no altera la provisión ni el vector focal en R0.

Por tanto, el actual `provision_probability` no implementa la secuencia D2. Es una probabilidad genérica de provisión/éxito usada en el potencial; no distingue intento programado, intento efectivo, recepción, instalación ni éxito de componentes.

## 4. Dictamen sobre C1-POS

**C1-POS no puede representarse con ninguna configuración actual del roster sin activar una vía distinta de la política D2 focal limpia.**

- R0 limpio: Z no altera provisión ni accesibilidad; ITT-Z carece de vía focal positiva.
- R0_DIRECT_Z: puede crear ITT-Z positivo, pero mediante vía directa al resultado.
- R2: altera alternativas y colaterales; no es focal limpio.
- R3: introduce reducción de provisión bajo Z; es adversarial y de signo contrario.
- G: altera el vector focal, pero su contraste no es ITT-D2 ni (g_A).

No es una carencia de una assertion o de un test. Falta el mecanismo generador Z→B_D2→W_programmed→W_attempt→S_install→C_dep*→A_f*/D_f* en el perfil R0. No se debe presentar `R0_DIRECT_Z` ni el efecto G como sustitutos de C1-POS.

La ausencia puede resolverse en el futuro mediante una reconciliación del Generator dentro del roster existente, pero requerirá:
- materializar las etapas distintas de la política D2;
- definir el mapping entre intento/éxito técnico y los predicados focales sin equiparar C_dep*, A_f* y D_f*;
- mantener explícitas provisión de fondo/crossover, fallos parciales y vías colaterales;
- seleccionar parámetros de cumplimiento/recepción/éxito solo mediante el ledger y justificación cuantitativa ya exigidos, no por conveniencia para producir el signo esperado.

No se crea un nuevo escenario ni se fija ahora ningún valor de cumplimiento o éxito. La decisión conceptual de D2 no autoriza por sí sola a escoger una distribución numérica no aprobada.

## 5. C1-HET: no confundir heterogeneidad G con heterogeneidad ITT-Z

El parámetro actual `heterogeneity` modifica el término de resultado asociado a `trajectory`, cuyo cambio focal en R0 depende de G. No produce por sí mismo heterogeneidad de ITT-Z porque Z no modifica la trayectoria/accesibilidad en R0.

Con los valores actuales (`focal_access_effect=0.20`, `heterogeneity=0.20`) la pendiente focal condicional respecto de `baseline_x` es (0.20+0.20(x-0.5)), positiva en todo (xin[0,1]). No hay signos condicionales opuestos. Incluso cambiar el coeficiente sin introducir una vía Z→provisión focal solo alteraría el contraste G, no el ITT-Z requerido por C1-HET.

C1-HET permanece NOT COVERED. Su eventual configuración debe reutilizar el mecanismo y el roster existente, con verdad ITT-Z por estrato, masas/soporte y recuperación condicional/marginal; no se asigna ahora un valor nuevo a `heterogeneity`.

## 6. Reconciliación G ≠ g_A y corrección documental pendiente

Gate 86 (§16.236) resolvió que la asignación G no puede reutilizarse como (g_A): no representa el par versionado de políticas conjuntas sobre el vector completo condicionado por historia, población (q_X^*) y régimen (r_{common}).

El Generator actual conserva dos residuos textuales:
- docstring inicial: afirma que G es una intervención sintética explícita sobre el cambio focal completo `(g_A)`;
- validación de `ScenarioConfig`: exige “randomized g_A”, aunque el objeto que el código implementa y el Analyzer estima es `ITT_G_Z0`.

El README integrado (§68) ya expresa la distinción correcta: ITT-Z, ITT-G bajo Z=0 y `theta_a_truth=None` hasta que las políticas conjuntas y q_X* estén operativamente definidas y soportadas.

**Dictamen:** los dos textos del código son obsoletos y deben describir G como asignación auxiliar G, no como (g_A). Gate 91 no los modifica: la corrección de código queda pendiente de autorización específica y debe ser puramente documental, sin alterar el mecanismo ni el comportamiento.

## 7. Disposición

- D2 material policy: aceptada conceptualmente por DEC-C10-067.
- Mapping D2/Z→etapas de provisión del Generator: AUSENTE en R0.
- C1-POS: NOT REPRESENTABLE IN CURRENT ROSTER CONFIGURATION.
- C1-HET: NOT COVERED; heterogeneidad actual pertenece al contraste G, no al ITT-Z.
- C3: continúa NOT MATERIALIZED; (g_A), (q_X^*), soporte conjunto y (r_{common}) siguen bloqueados.
- Parámetros de intento/cumplimiento/recepción/éxito: OPEN; no asignados.
- Corrección docstring/error message: identificada, no aplicada.
- Roster: sin ampliación.
- Código/DGP/Decision Records: sin cambios.
- Tests/compilación/workflows/Monte Carlo: no ejecutados.
- `scientific_execution=false`; `execution_authorized=false`.

**Dictamen:** `GATE_91_D2_Z_GENERATOR_MISMATCH_CONFIRMED / C1_POS_NOT_REPRESENTABLE_IN_CURRENT_R0 / C1_HET_NOT_COVERED_BY_Z / G_NOT_G_A_PRECEDENCE_CONFIRMED / W_PROGRAMMED_W_ATTEMPT_STAGES_ABSENT / QUANTITATIVE_COMPLIANCE_PARAMETERS_OPEN / STALE_G_EQUALS_G_A_CODE_TEXT_FOUND / NO_CODE_CHANGE / NO_NEW_WORLDS / NO_EXECUTION / NO_DESIGN_FREEZE`.

**Siguiente operación — Gate 92:** construir una matriz de correspondencia de etapas D2 (Z/B/W_{programmed}/W_{attempt}/S_{install}/C_{dep}/A_f/D_f/Delta T_{acc}) contra los campos actuales del Generator, TruthBundle, Projector, Sealer, Analyzer y Evaluator; clasificar cada etapa como existente, proxy no válido o ausente. Especificar el mínimo contrato de representación y las decisiones cuantitativas que faltan, sin implementar ni inventar parámetros. La corrección de los textos obsoletos G/g_A se ejecutará solo con autorización de edición de código.
