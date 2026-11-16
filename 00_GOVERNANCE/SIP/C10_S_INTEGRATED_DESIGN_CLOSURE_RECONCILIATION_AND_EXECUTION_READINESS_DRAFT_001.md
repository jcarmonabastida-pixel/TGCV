# C10-S — Reconciliación integrada de cierre del diseño y preparación del experimento sintético

**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** INTEGRATED_RECONCILIATION_COMPLETED / DESIGN_NOT_CLOSED / CONFIRMATORY_IDENTIFICATION_NOT_ESTABLISHED / IMPLEMENTATION_NOT_AUTHORIZED / SCIENTIFIC_EXECUTION_NOT_AUTHORIZED.  
**Tipo:** síntesis integradora de fuentes existentes; no crea DEC ni sustituye contratos fuente.

## 1. Dictamen ejecutivo

La reconstrucción documental permite reducir el trabajo pendiente a un conjunto pequeño de bloqueos estructurales. No procede continuar con micro-Gates que vuelvan a describir decisiones ya aceptadas. Tampoco procede declarar Design Freeze.

**Dictamen:** C10-S dispone de una arquitectura causal y de medición sustancialmente desarrollada, un conjunto amplio de contratos de prueba y un benchmark ideal parcialmente implementado. Sin embargo, el experimento sintético confirmatorio completo aún no está especificado/materialmente identificado en los puntos críticos siguientes:

1. **Precedencia normativa B1:** la aceptación de R208-A y Gate 154 delimita A_B1/V_cont, pero no resuelve formalmente la tensión textual con DEC-C10-102.
2. **DGP temporal:** DEC-C10-100…104 y R144-A/R146-A…D fijan buena parte de la semántica lógica; §51 y los parámetros temporales siguen abiertos y el harness no materializa EventHistory ni la adjudicación estricta desde eventos.
3. **D2 y población:** no hay contrato material de aleatorización Z, roster UE/B1, IAM/snapshots ni evidencia suficiente de aislamiento/interferencia.
4. **Atribución de accesibilidad:** θ_A está definido conceptualmente, pero el par operacional g_A0/g_A1, q_X* por historia, soporte común y certificados r_common no están materializados; el Analyzer actual no estima θ_A.
5. **Resultados y Value:** V_cont está seleccionado provisionalmente, pero su medición temporal completa no está materializada; O-CONF no está operacionalizado y no existe una ficha Value confirmatoria completa.
6. **Medición, inferencia y potencia:** S3 ideal permite solo un benchmark restringido; calibración imperfecta, error/ausencia, bounds temporales, precisión científica, N y R confirmatorios siguen abiertos.
7. **Roles y conformidad:** el firewall está especificado lógicamente, pero su enforcement técnico/custodia no está demostrado; varios contratos de prueba existen como especificación, no como tests ejecutados.

En consecuencia, el resultado científico actual es **NOT IDENTIFIED / NOT EVALUABLE** para la atribución confirmatoria de ΔT_acc*→Value. Esto no es evidencia de efecto nulo ni refutación de TGCV.

## 2. Alcance y fuentes reconciliadas

Se aplicó la operativa de `00_GOVERNANCE/README.md` y `CHATGPT_BOOTSTRAP.md` desde `main`. Se recuperaron `STATUS.md`, RMA/Evidence pointers en la medida necesaria para orientar el estado y los artefactos C10-S de la rama de investigación. La consistencia local de bootstrap no se certifica: no se ejecutaron los validadores locales.

Fuentes de trabajo principales:
- `C10_S_SYNTHETIC_EXPERIMENT_CONSOLIDATED_DRAFT_004.md`, especialmente §§277–318 y los contratos históricos enlazados.
- `C10_S_CLOSURE_CONTROL_MATRIX_DRAFT_001.md` y `C10_S_DECISION_LOG_DRAFT_001.md`.
- `C10_S_INTEGRATED_CONFIRMATORY_FEASIBILITY_AND_DESIGN_FREEZE_RECONCILIATION_DRAFT_001.md`.
- `C10_S_C10D1_S4R_ESTIMAND_RECONCILIATION_DRAFT_001.md`.
- `C10_S_D2_ASSIGNMENT_POPULATION_SUPPORT_RECONCILIATION_DRAFT_001.md`.
- Gate 121 de aislamiento; Gates 129–130 de θ_A/q_X*/g_A/r_common.
- Contrato DGP temporal/roles, contrato lógico de EventHistory y Gates 131–152.
- Gates 206–208 y aceptación R208-A1…A6.
- Test Contract Register, Path Predicate Temporal Evidence Matrix y protocolo de calibración/seed bank.

La reconstrucción histórica se reutiliza; no se reabren decisiones aceptadas ni se duplican IDs de prueba.

## 3. Reconciliación de B1, EventHistory y DEC-C10-102

### 3.1 Decisiones que se conservan

Se mantienen, dentro de sus respectivos alcances:
- DEC-C10-099: V_cont como dimensión mínima provisional, sin índice ni pesos.
- DEC-C10-100: agregación igualitaria por K intervalos y truth tri-valuada con bounds individuales.
- DEC-C10-101: ventana post-Z iniciada en t0, incluyendo provisión/instalación.
- DEC-C10-102: continuidad estricta por intervalo; cualquier incumplimiento funcional confirmado afecta el intervalo.
- DEC-C10-104: intervalos semiabiertos [b_{k−1},b_k), último intervalo cerrado en T*, asignación determinista de fronteras y regla conservadora para UNKNOWN funcional.
- R144-A: estado inicial post-Z, persistencia por tramos, transición truth explícita, simultaneidad atómica y suborden para estados intermedios.
- R146-A…D: identidad propia de transición, versionado separado DGP/EventHistory/adjudicación, regeneración inmutable y completitud por ámbito/generación/integridad.
- R147-A/B, R148-A, R150-A, R151-A/A8 y R152-A1…A6.
- Gate 154: alcance temporal de A_B1/V_cont limitado a admisión efectiva conforme a ENABLED, incluyendo runtime constitutivo; PROFILE exposure permanece obligación contractual fuera de esa adjudicación temporal.
- R208-A1…A6: PROFILE versionado en EventHistory como configuración declarativa; D_valid separado; runtime solo si altera efectivamente admisión; no inventar recursos/umbrales; una solicitud no demuestra capacidad continua; separación truth/observación/evaluación.

### 3.2 Tensión normativa que sigue bloqueando el cierre

DEC-C10-102 formula literalmente la continuidad estricta en términos de ENABLED/PROFILE. Gate 154 y R151-A8 excluyen PROFILE exposure del predicado temporal adjudicado. R208-A acepta conservar los cambios declarativos de PROFILE en EventHistory, pero no crea una trayectoria de exposición ni proyecta un cambio de PROFILE, por sí solo, a A_B1/V_cont.

Estas reglas pueden ser compatibles si se distingue con precisión:
- PROFILE como estado declarativo versionado y obligación contractual;
- D_valid como validez de la configuración bajo RUL;
- D_enabled como mandato de admitir/no admitir;
- O como disponibilidad operativa;
- A_B1 como comportamiento efectivo de admisión;
- PROFILE exposure como obligación no adjudicada temporalmente en el DGP actual.

Pero esa lectura no debe imponerse como si ya modificara el texto de DEC-C10-102. Gate 206/208 deja constancia de precedencia de alcance, no una enmienda normativa formal.

**Acción de cierre necesaria:** una aclaración/DEC complementaria explícita que preserve el texto histórico de DEC-C10-102, declare el predicado adjudicado después de Gate 154 y especifique cómo se conserva D_valid/PROFILE sin confundirlo con A_B1. Hasta que se apruebe, el crosswalk normativo es **BLOCKED**. No se modifica ahora ninguna DEC.

### 3.3 Contrato lógico que debe materializarse

La lectura funcional resultante es no compensatoria: ENABLED=false exige no admitir; ENABLED=true exige capacidad efectiva de admitir. La incapacidad runtime confirmada que impide la admisión exigida hace fallar el intervalo. PROFILE exposure no se presume cumplido ni se convierte en UNKNOWN. Los antecedentes de proceso no son transiciones truth por sí mismos.

EventHistory es verdad generada, distinta de PROCESS_EVENT, evidencia S3 y adjudicación. Por unidad y potencial debe conservar estado inicial post-Z, transiciones efectivas, before/after, identidad, versión, familia, provenance y event_time ordenable; completitud debe demostrar ámbito, generación íntegra e integridad de representación. El adjudicador aplica DEC-C10-100…104. TruthBundle conserva la versión exacta de EventHistory y de las reglas de adjudicación. Analyzer no recibe EventHistory/TruthBundle; Evaluator accede a truth solo tras el sellado.

**Estado:** semántica lógica avanzada/aceptada en sus componentes; contrato normativo compuesto pendiente; EventHistory, adjudicador y TruthBundle temporal no materializados.

## 4. Reconciliación causal D2, población, accesibilidad y estimandos

### 4.1 Jerarquía de estimandos

No se sustituyen unos objetos por otros:
- `ITT_Z^D2`: efecto total de asignación a la política/paquete D2 sobre un resultado definido.
- `ITT_G`: efecto de asignación del mecanismo G en el contrato correspondiente.
- `LATE_f`: efecto local de apertura focal entre compliers, solo bajo supuestos IV completos.
- `θ_A(q)`: pregunta científica general de efecto de políticas factibles de accesibilidad bajo régimen común q.
- `θ_Af(q_X*)`: contraste focal de accesibilidad bajo la distribución conjunta de historias basales.
- `C4`: mediación interventional, separada de ITT y θ_A.
- Efecto directo/residual: no se obtiene por resta ad hoc.

La aleatorización de Z identifica, bajo sus condiciones, el efecto de asignar la política implementada. No identifica automáticamente θ_A. Si existen vías directas/colaterales, la etiqueta correcta es efecto de política/paquete o no identificación focal. P178 es benchmark metodológico acotado; Gate 129 confirma que no estima θ_A y que el Analyzer actual no lo recupera.

### 4.2 D2 y población

D2 continúa como escenario primario candidato y D1 como secundario; P*_{τ2} es población primaria candidata y P*_F subpoblación secundaria. Se preservan una B1 por UE y una oportunidad estandarizada por UE. No se presume asignación 1:1.

Faltan el mecanismo Z (unidad de asignación, ratio/probabilidades, estratos/bloques, algoritmo, semillas, hash y desviaciones), roster versionado UE/B1/servicio, composición material de elegibilidad pre-Z, IAM/snapshots y protocolo de consistencia/recepción/crossover. Las probabilidades de programación de provisión bajo D2 no son probabilidades de asignación Z. El 0.80 de éxito técnico es hipótesis candidata no validada y no equivale a apertura focal.

### 4.3 Aislamiento e interferencia

Gate 121 establece que los contratos de inspección son suficientes para especificar qué habría que revisar, pero el inventario material está vacío y el aislamiento no está demostrado. La unicidad de instance_id por UE no prueba independencia de host, recursos, dependencias, agentes, red, credenciales, canales, colas o estado compartido. La asignación individual solo es admisible si el aislamiento material se demuestra en la frontera, versión y ventana auditadas; de lo contrario debe definirse unidad cluster/exposición o declararse no identificado. No se presume SUTVA.

### 4.4 q_X*, g_A0/g_A1 y r_common

Gate 130 concluye que el esquema documental de q_X*, intervenciones conjuntas g_A y r_common ya está definido; no faltan más contratos narrativos. Faltan las filas y objetos materiales: roster e historias basales, masas positivas que sumen uno, par de políticas factibles/versionadas sobre el vector completo ΔT_acc*, soporte conjunto por historia y certificados r_common por historia. Los extremos deterministas anteriores no están ratificados; G no sustituye g_A. No se inventarán masas, kernels ni políticas para obtener positividad.

**Estado causal global:** ITT de política potencialmente identificable en un diseño futuro, pero asignación/población/resultado no materializados; θ_A/θ_Af y LATE_f **NOT IDENTIFIED** en el diseño material actual; C4 y efectos directos/residuales **NOT IDENTIFIED / NOT EVALUABLE**.

## 5. Temporalidad, S3, V_cont y medición

DEC-C10-100…104 y R144-A fijan semántica importante, pero no seleccionan los valores temporales. §51, reloj/unidad/coordenada contractual, W_c, T*, Δ, K, soporte temporal, τ_follow, resolución y calibración S3 siguen abiertos.

El harness actual:
- genera truth ENABLED/PROFILE y conjunción binaria por slot, no EventHistory con eventos fechados;
- usa provision_ok binario, no cronología diferenciada de programación/intento/recepción/instalación/verificación;
- no adjudica continuidad estricta ante cualquier evento intraintervalo/frontera;
- no materializa UNKNOWN funcional ni bounds individuales de DEC-C10-100;
- conserva S3 missingness como ausencia observacional, correctamente distinta de UNKNOWN funcional;
- ejecuta la ruta numérica solo con S3 perfecto/completo;
- tiene R0_MEASUREMENT_ADVERSE como escenario STATUS_ONLY con abstención esperada, pero no demuestra recuperación bajo error/ausencia;
- no ofrece corrección calibrada por error, bounds validados ni resolución temporal intraintervalo.

El benchmark ideal puede conservarse para los ITT-Z/ITT-G puntuales bajo su DGP binario y S3 perfecto/completo. No valida V_cont temporal completo, robustez S3, θ_A ni ΔT_acc→Value. Los bounds truth individuales y los bounds de identificación parcial del Analyzer son objetos distintos. No se deben restar extremos marginales para fabricar bounds causales.

**Estado:** benchmark ideal restringido reutilizable; V_cont confirmatorio completo **NOT IMPLEMENTED / NOT VALIDATED**.

## 6. Outcome y Value

DEC-C10-099 selecciona provisionalmente V_cont como dimensión mínima, no como medida ya operacionalizada. Siguen pendientes su relación temporal exacta con O-CONF, baseline, ventana, fuente, escala, error, cobertura y adjudicación.

O-CONF es candidato prioritario de Outcome técnico, anclado en F*, pero su mapping fuente→destino, evento/snapshot terminal, oráculo, ventana, baseline, validez, error, ausencia y cegamiento siguen abiertos. F* no es por sí mismo un Outcome adicional.

Value debe conservarse como vector mientras no exista justificación de una dimensión/escala. Need_preZ, perspectiva/autoridad de valoración, dimensiones V_j, indicadores, fuentes, unidades, baseline/post, horizonte, missingness, error y regla de agregación no están cerrados. No se deriva Value de T_acc, Reach, trayectoria, ejecución, recursos o Outcome técnico. No hay estimando confirmatorio completo de Value hoy.

## 7. Estadística, potencia y calibración

El protocolo de seed bank separa bancos de calibración y evaluación, usa semillas domain-separated, fija el mundo por escenario/N y varía asignaciones Z/G por réplica. N se seleccionaría como el mínimo candidato que satisface todos los objetivos de MCSE por escenario/estimando; R se dimensiona desde SD de calibración y MCSE objetivo. Es un protocolo scaffold, no una ejecución ni autorización.

Permanecen sin aprobación: grid N, MCSE objetivo por escenario/estimando, escala/MDE o precisión relevante, presupuesto/regla de parada de calibración, set de escenarios/estimandos requerido, tolerancias científicas, criterios de cobertura/potencia/error tipo I y regla de precisión de SD_cal. La tolerancia de test 0.10 no es criterio científico. N=2.000/R=1.000 históricos no se promueven a confirmatorios.

P177–P183 y MEAS/MISS/UNIT/S4R se reutilizan como contratos adversariales. Sus especificaciones no equivalen a implementación o PASS. No se ejecutaron tests, calibración ni Monte Carlo en esta reconciliación.

## 8. Roles, firewall y Evaluator

La separación lógica Generator → TruthBundle → Projector/S3 → Sealer → Analyzer → Evaluator está descrita. Se conserva la regla: Analyzer solo recibe evidencia sellada permitida; truth y potenciales permanecen reservados; Evaluator abre truth tras verificar salida/sello.

El enforcement técnico (ACL, custodia, aislamiento de procesos/archivos, secretos, canales, reproducibilidad del sellado) no está demostrado. El Evaluator actual valida integridad y contrasta estimandos escalares ITT-Z/ITT-G; no verifica recuperación de V_cont con bounds ni θ_A. El Analyzer actual no estima θ_A.

## 9. Matriz integrada de estado y bloqueos

| Paquete | Estado | Bloqueo real para cierre |
|---|---|---|
| B1 / DEC-C10-102 | BLOCKED_NORMATIVE_CROSSWALK | Aclaración normativa explícita tras Gate 154/R208 |
| EventHistory | LOGICAL_PARTIAL / MATERIALIZATION_OPEN | §51, contrato temporal versionado, implementación de eventos y completitud |
| D2 assignment | OPEN / NOT_MATERIALIZED | Aleatorización Z y provenance |
| Población / roster | OPEN / NOT_MATERIALIZED | UE/B1/servicio, elegibilidad y snapshots pre-Z |
| Aislamiento | NOT_DEMONSTRATED | Inventario y evidencia de transmisión/interferencia |
| Soporte / q_X* | NOT_ESTABLISHED | Historias, masas, soporte común y certificados |
| g_A0/g_A1 | FORM_DEFINED / PAIR_NOT_SELECTED | Políticas conjuntas factibles, versionadas y materializadas |
| θ_A / Analyzer | NOT_IDENTIFIED / NOT_RECOVERED | Intervenciones, soporte, vías alternativas y estimador |
| Outcome O-CONF | CANDIDATE / NOT_OPERATIONALIZED | Ficha §224, mapping y oráculo |
| Value | NOT_OPERATIONALIZED | Need_preZ, dimensiones, perspectiva, fuente y regla |
| V_cont / S3 | BENCHMARK_RESTRICTED | EventHistory, rejilla/params, S3 calibration, bounds y recuperación |
| Estadística | PROTOCOL_SCAFFOLD / NUMERIC_TARGETS_OPEN | N/R, MCSE, MDE/precisión, potencia y tolerancias |
| Firewall | LOGIC_SPECIFIED / TECHNICAL_NOT_VERIFIED | Enforcement y evidencia de separación |
| Tests | CONTRACTS_DEFINED / NOT_EXECUTED | Implementación, fixtures, oráculos, tolerancias y ejecución autorizada |

## 10. Ruta mínima integrada para cerrar el diseño

No abrir un Gate por cada fila. La secuencia recomendada se limita a cuatro paquetes dependientes:

### Paquete A — Decisión científica/normativa de alcance
1. Aprobar una aclaración complementaria a DEC-C10-102 que reconcilie PROFILE/D_valid con A_B1/V_cont sin alterar retroactivamente DEC.
2. Congelar el alcance de afirmación: benchmark ITT de política, atribución focal θ_Af, pregunta general θ_A y Value son resultados separados.
3. Declarar expresamente qué objetos quedan fuera del núcleo confirmatorio y cuáles solo son escenarios adversariales.

### Paquete B — DGP temporal y material causal
1. Completar §51 con reloj, unidad, soporte, T*, Δ, K y resolución coherentes con DEC-C10-100…104.
2. Versionar el contrato DGP temporal completo; no basta la aceptación parcial de §§48–50, 52–55.
3. Definir la instancia D2: roster, población, asignación, políticas, snapshots, aislamiento, soporte y mappings.
4. Seleccionar/instanciar g_A0/g_A1 y q_X* solo si existe factibilidad y soporte; si no, mantener θ_A como no identificado y acotar el alcance confirmatorio a ITT de política.

### Paquete C — Medición, resultados y recuperación
1. Completar EventHistory → A_B1 → TruthBundle → S3 → Analyzer → Evaluator, manteniendo separación de roles.
2. Completar fichas O-CONF y Value/Need_preZ, o declarar el experimento limitado a outcomes que sí puedan medirse válidamente.
3. Definir calibración S3, error, missingness, cobertura, bounds/abstención y oráculos independientes.
4. Cruzar P177–P183, S4R, MEAS/MISS y UNIT existentes a estimandos/escenarios; no crear pruebas duplicadas.

### Paquete D — dimensionamiento y autorización
1. Fijar escenarios y estimandos obligatorios, criterios de recuperación, precisión/MCSE, potencia/error tipo I cuando proceda, N y R.
2. Congelar seed banks separados, manifests, hashes, entorno y replay.
3. Completar G-SCI, G-MAT, G-SCHEMA, G-ROLE, G-TEST y G-REPRO.
4. Ejecutar solo tras autorización específica de implementación y, posteriormente, autorización científica independiente.

## 11. Criterio de Design Freeze

Design Freeze no se propone hasta que:
- la precedencia normativa esté resuelta y trazada;
- el DGP y §51 estén versionados y completos;
- el estimando confirmatorio y su población/unidad/intervención estén identificados;
- asignación, soporte, interferencia y medición sean defendibles;
- Outcome/Value tengan fichas completas para los claims que se pretenden evaluar;
- Analyzer/Evaluator y firewall tengan contratos verificables;
- tests adversariales, tolerancias, potencia/precisión y reproducibilidad estén preespecificados;
- cada claim no identificado quede excluido o expresamente acotado.

La salida puede ser **PASS**, **CONDITIONAL**, **NOT_IDENTIFIED**, **NOT_EVALUABLE** o **BOUNDS_ONLY**, según el objeto. No se fuerza una conclusión positiva.

## 12. Límites de esta reconciliación

Esta operación es documental. No crea DEC, no altera el DGP original, no cambia RMA/Evidence→Claim Matrix/STATUS/Core, no modifica código, schemas, fixtures, tests ni workflows; no ejecuta validadores, simulaciones, calibración, estimación o Monte Carlo; no selecciona parámetros numéricos; no declara Design Freeze.

`scientific_execution=false`  
`execution_authorized=false`  
`implementation_authorized=false`


## 13. Paquete A — resultado de reconciliación normativa (2026-11-16)

**Estado:** DOCUMENTARY_RECONCILIATION_COMPLETE / COMPLEMENTARY_DECISION_PROPOSAL_PENDING_ACCEPTANCE.

Se resolvió la reconstrucción de precedencia: Gate 154 está aceptado; R150-A conserva PROFILE exposure como obligación contractual; R151-A8 impide adjudicar su continuidad sin trayectoria truth; R152-A deja abierta la composición; R208-A conserva PROFILE declarativo versionado, D_valid separado y runtime constitutivo. No es necesario reabrir esas aceptaciones ni modificar el operador estricto de DEC-C10-102.

La propuesta única C1–C6 se encuentra en `C10_S_DEC-C10-102_COMPLEMENTARY_SCOPE_DECISION_PROPOSAL_DRAFT_001.md`. Hasta su aceptación expresa, el crosswalk se clasifica como **PROPOSAL_PREPARED / ACCEPTANCE_PENDING**, no como CLOSED. La propuesta preserva la obligación contractual PROFILE sin atribuirle una trayectoria temporal que el DGP no genera, y limita V_cont a la continuidad temporal de la función efectiva de admisión requerida por ENABLED.

**Resultado de paquete:** la ambigüedad se ha reducido a una decisión de alcance precisa, no a una nueva auditoría. No se ha creado DEC aceptada. §51 y los paquetes B–D permanecen abiertos.


## 14. Paquete A — aceptación decisional (2026-11-16)

C1–C6 han sido aceptadas conjuntamente. Registro: `C10_S_DEC-C10-102_COMPLEMENTARY_SCOPE_ACCEPTANCE_RECORD_DRAFT_001.md`. Crosswalk normativo **CLOSED_FOR_CURRENT_SYNTHETIC_DGP_LOGICAL_SCOPE**. DEC-C10-102 y DEC-C10-099…104 no se modifican; no se crea DEC-C10-105. PROFILE exposure permanece obligación contractual no adjudicada temporalmente por V_cont en el DGP actual; D_valid se mantiene separado; operador estricto y {1,0,?} intactos.

El Paquete A queda cerrado en su alcance lógico. Paquetes B–D y Design Freeze permanecen abiertos; no se autoriza implementación ni ejecución.


## 15. Paquete B — propuesta integrada de cierre lógico (2026-11-16)

Se completa una única propuesta B1–B6 en `C10_S_PACKAGE_B_INTEGRATED_TEMPORAL_DGP_AND_CAUSAL_DESIGN_CLOSURE_PROPOSAL_DRAFT_001.md`. La reconciliación combina §51 y DEC-C10-099…104, EventHistory R144-A/R146-A…D, S3, D2, población, asignación, aislamiento, q_X*/g_A/r_common y jerarquía ITT/θ_A/C4.

La coordenada temporal está conceptualmente delimitada; ρ_follow/T*, Δ/K y calibración S3 siguen parámetros abiertos. El contrato causal distingue asignación Z, programación D2, provisión/instalación, apertura focal y vector ΔT_acc*. UE=UA solo con aislamiento demostrado. Los contratos q_X*, g_A y r_common existen; las filas, masas, políticas factibles y certificados no están materializados. θ_A permanece no identificado y el Analyzer actual no lo estima.

**Estado:** PROPOSED_FOR_ACCEPTANCE. La aceptación cerrará el contrato lógico integrado, no los parámetros/materialización/identificación. Paquete A ya aceptado; paquetes C y D siguen pendientes.
