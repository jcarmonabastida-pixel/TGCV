

## 277. DEC-C10-099 — V_cont: selección provisional y límites (2026-11-12)

Se incorpora la decisión aceptada DEC-C10-099. Para la extensión sintética B, V_cont es la única dimensión mínima provisional de Value; V=(V_cont), sin índice ni pesos. La selección del constructo no operacionaliza su medición. Indicador, regla temporal, baseline, horizonte, resolución, fuente, escala, agregación, error, cobertura y adjudicación permanecen OPEN. Se exige separación truth_dgp/observed_evidence/evaluation, independencia respecto de ΔT_acc*/Reach/trayectoria y Outcome técnico, y gates de discriminación frente a O-CONF/F* y de identificación. Si fallan, V_cont queda NOT_CONFIRMATORY/NOT_IDENTIFIED; no se sustituye por otra dimensión. DEC-C10-095 sigue rigiendo A/B en su alcance, complementada por esta decisión específica posterior para B. No se autoriza implementación ni ejecución.


## 278. Contrato de medición sintética V_cont — referencia integrada (2026-11-12)

La especificación rectora se encuentra en el plan C10-S §16.182. V_cont tiene selección provisional por DEC-C10-099; truth temporal B1 y canal S3 pasivo se mantienen separados. S3 es un vector de indicadores runtime imperfectos, no evidencia funcional concluyente. La recuperación puntual requiere un canal identificable/calibrado y acceso permitido al protocolo; sin ello, bounds o NOT_IDENTIFIED. La regla de agregación, K, ventana, frecuencia, baseline y parámetros siguen abiertos. O-CONF/F* y la discriminación terminal/temporal siguen CONDITIONAL/NOT_VERIFIABLE. No se autoriza implementación ni ejecución.



## 279. N16 — F* y ficha §224 de O-CONF (2026-11-12)

La especificación rectora está en el plan §16.184 y la matriz F* §22. F* es criterio de ruta completa; O-CONF es su adjudicación terminal, no un Outcome duplicado. La unidad es instancia × ruta, anclada en F2_DST_APPLIED o A2_DST_APPLIED; la regla lógica 1/0/? es no compensatoria sobre FP-01…07, con FP-08 separado. PAR/RUL y las etapas de aplicación/post-check reutilizan DEC-C10-083…088. La ficha §224 queda PARTIAL, no operacionalizada: IAM, atomización/mappings globales, C0/G/H materiales, snapshots/evento, tolerancias, oráculo, validación, error/cobertura/acuerdo y firewall efectivo siguen abiertos. V_cont conserva su dimensión temporal y la discriminación frente a O-CONF no está verificada. No Design Freeze ni autorización de ejecución.



## 280. C+D — crosswalk causal integrado (2026-11-12)

Referencia rectora: plan §16.185; complementa §268 PC, §276–279 y contratos D2/PD/C1. D2/Z_B genera potenciales separados por etapa y su ITT es efecto total del paquete por resultado. g_A1/g_A0 interviene sobre distribuciones factibles del ΔT_acc* completo bajo q basal y régimen común; su mapping a D2 no está demostrado. C4 es mediación interventional y no resta del ITT. O-CONF_r (terminal F*) y V_cont (temporal B1) conservan truth/observación/estimandos independientes. P*τ2/P*_F, q_X*, soporte, π_h, unidad/interferencia y parámetros siguen abiertos. P177–P183 y familias existentes se reutilizan; no nuevos tests. No Design Freeze, implementación ni ejecución.



## 281. DEC-C10-100 — V_cont: agregación temporal igualitaria aceptada (2026-11-12)

Se incorpora DEC-C10-100: la verdad sintética V_cont_truth(i) es la fracción temporal de cumplimiento funcional B1, calculada como media no ponderada de A_B1(i,k) en K intervalos de igual duración dentro de una ventana/rejilla post-Z común preespecificada. UNKNOWN permanece y se propaga a bounds [n1/K,(n1+n?)/K]; no se imputa cero ni se elimina del denominador. El estimando es nivel post-Z, no cambio pre/post. S3 sigue siendo vector de señales imperfectas y no se promedia para sustituir truth. K, frecuencia, ventana, baseline/transitorios, canal, MDE y criterios cuantitativos permanecen abiertos. La calibración se evalúa como superficie de recuperación [0,1] por estimando/escenario, sin inventar un MDE ni transferir N/R de P178. Validez de medición, discriminación O-CONF/F*, identificación y punto de operación confirmatorio siguen abiertos. No Design Freeze, implementación ni ejecución.

## 282. DEC-C10-101/102 — ventana t0, continuidad estricta y dominio de observación S3 (2026-11-12)

La ventana de V_cont comienza en t0 e incluye provisión/instalación; la continuidad B1 se adjudica estrictamente por intervalos iguales, sin gracia ni duración mínima funcional. Cualquier incumplimiento confirmado hace A_B1=0 en cada intervalo afectado. V_cont es la proporción de bloques plenamente conformes, no uptime exacto.

El DGP acota cinco familias causales: ENABLED/PROFILE efectivos; proceso/módulo; listener/socket/superficie de ingreso; dependencias solo cuando alteran admisión; capacidad/recursos solo cuando alteran admisión. Provisión, instalación, verificación, rollback y reinicio son antecedentes/transiciones, no fallos automáticos. El estado funcional efectivo determina truth.

Se separa δ_det, dominio mínimo de duración para el que S3 demuestre detección tras calibración, de cualquier duración funcional: δ_det no cambia truth ni crea tolerancia. Para episodios no detectables o cobertura insuficiente, Analyzer debe producir bounds/abstención. Δ, cadencia/resolución S3 y δ_det son distintos. t_last es la última transición causal, incluida recuperación final; T*=t_last+τ_follow. Episodio activo en T* queda terminal/censurado, no recuperado por imputación.

Unidad normalizada, δ_det, Δ, τ_follow, T* y K permanecen abiertos para derivación conjunta. No se generan datos ni se ejecuta código, simulación, calibración o validación. No Design Freeze; scientific_execution=false; execution_authorized=false.


## 283. Reconciliación temporal integrada: reloj normalizado y captura S3 (2026-11-12)

Se incorpora la derivación rectora del plan §16.195. El reloj es adimensional: W_c=t_c,max−t0 representa el soporte común de transiciones causales; x=(t−t0)/W_c, t0=0 y t_c,max=1. No equivale a una duración física ni a t9/H. La cola común ρ_follow=τ_follow/W_c sigue OPEN y T*=1+ρ_follow.

Las duraciones de episodio d_e, la resolución/cadencia S3, Δ de adjudicación y la cola de seguimiento son magnitudes separadas. S3 conserva cinco componentes pasivos y se modela bajo snapshots/métricas, logs/trazas/eventos e híbrido, sin presuponer periodicidad, completitud, captura event-driven o independencia. La detectabilidad se representa primero como curva conjunta por duración, fase, familia y versión; δ_det puntual requiere umbral p* aprobado. d_min,DGP es límite del soporte del benchmark, nunca mínimo funcional ni gracia. DEC-C10-102 sigue aplicándose sin excepción; falta de detección implica bounds/abstención, no continuidad.

K/Δ se derivan por recuperación/aliasing y divisibilidad exacta; ρ_follow por soporte de recuperación/persistencia. No se fijan parámetros numéricos ni se ejecuta calibración. No Design Freeze; scientific_execution=false; execution_authorized=false.


## 284. Horizonte común y precedencia de t_last (2026-11-12)

Se aclara que t_last,i es la última transición efectiva de cada UE, mientras t_last^max=t_c,max es el límite superior común ex ante del soporte de transiciones causales posibles en todos los brazos/escenarios. T*=t_last^max+τ_follow (normalizado: 1+ρ_follow) mantiene una ventana común; no se calcula t_last,i+τ_follow por unidad tras observar resultados. Episodios activos en T* son terminales/censurados. Si el soporte no puede acotarse ex ante, T* permanece OPEN.


## 285. Crosswalk temporal integrado de escenarios y contratos (2026-11-12)

Se reutilizan los perfiles DGP de §16.188.4 y los contratos P182/P183/MEAS/MISS; no se crean escenarios ni tests nuevos. Los contrastes temporales se integran en control de truth estable/señal espuria, fallo por etapas, interrupción B1 funcional, medición adversarial, pérdida diferencial, soporte/interferencia/versionado y discriminación O/V.

S3 permanece un único canal lógico pasivo, contrastado bajo snapshots/métricas, logs/trazas/eventos e híbrido. Se preservan fase, lag, pérdida, cobertura, validez, falsos positivos/negativos y dependencia conjunta. P182-07/08/11/12, P183-01/02/04/07/09/10/11 y P182-04/10 gobiernan error, firewall, trazabilidad, ausencia, censura, bounds y discriminación. No hay nuevos IDs.

Analyzer solo produce punto si la observación identifica; en otro caso bounds/abstención. Evaluator abre truth tras sellado. No ejecución ni PASS técnico.


## 286. Matriz temporal adimensional y selección de K (2026-11-12)

Se adopta la cobertura dirigida del plan §16.197, sin factorial completo ni IDs nuevos. Los ejes son r_c=d_e/c_j, r_Δ=d_e/Δ, fase de captura y r_f=τ_follow/τ_recovery,max cuando exista soporte. Se cubren relaciones menores/iguales/mayores que 1, aliasing, cruce de fronteras, pérdida/lag diferencial, errores correlacionados, recuperación, censura y discriminación O-CONF/V_cont, reutilizando perfiles §16.188.4 y P182/P183/MEAS/MISS.

τ_follow cubre el soporte de recuperación solo si existe límite defendible; de otro modo se preserva censura. K/Δ se seleccionan por recuperación, aliasing, sensibilidad a fase y estabilidad al refinar K, no por conveniencia. No se fijan valores ni se ejecuta calibración.


## 287. Registro paramétrico temporal integrado

Se integra el ledger §16.198: inicio normalizado, familia causal, duración/soporte DGP, recurrencia, recuperación, cadencia/fase/cobertura S3, emisión/captura, lag, pérdida, error y dependencia conjunta. No se fijan valores ni leyes por defecto. Generator crea truth y estados; A_B1 se deriva por DEC-C10-102; S3 se genera después; Analyzer recibe evidencia sellada y Evaluator abre truth tras sellado.

V_cont_truth es proporción de intervalos completamente conformes, no uptime exacto. Un incumplimiento confirmado afecta a todos los intervalos que intersecta; d_min,DGP no es tolerancia funcional. p*, δ_det, Δ, K, ρ_follow y distribuciones siguen OPEN. No se crean tests ni se ejecuta calibración.


## 288. Crosswalk estructural D2–ΔT_acc*–g_A

Referencia rectora: plan §16.199. La política D2 conserva potenciales separados W_programmed, W_attempt, receipt, S_install, C_dep*, A_f*, D_f*, T_acc*/ΔT_acc*, Reach/Π y etapas downstream. O-CONF y V_cont tienen truth separada. Ninguna etapa se presume exitosa por la anterior.

ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*); ΔE_T es epistémico. q_X* es historia basal común; q_L* solo si C4 exige intervención longitudinal. g_A1/g_A0 actúan sobre distribuciones factibles del cambio completo bajo q_X* y r_common explícito. No se equiparan a Z_D2: el ITT D2 es efecto total del paquete y el mapping D2→g_A no está demostrado. C4 no es una resta del ITT.

Se preservan vías directas, colaterales, alternativas, interacciones y spillovers. Las distribuciones, funciones estructurales, q_X*, soporte, r_common y mapping ΔX* permanecen OPEN. No se importan tasas históricas ni parámetros P178. No se crean tests, no se ejecuta ni se declara Design Freeze.


## 289. Funciones estructurales, q_X* y ΔX*

Referencia rectora: plan §16.200. D2 conserva funciones/potenciales separados para programación, intento, recepción, instalación, C_dep*, A_f*/D_f*, T_acc*/ΔT_acc*, Reach/Π, trayectoria y O-CONF/V_cont. Solo W_programmed(z)=z está fijado para la política D2; las demás funciones no heredan éxito ni tasas por defecto.

q_X* es historia basal común: X/H0 y C_c con mapping; F_alt,0 modifica análisis P*_F; E/App son marco; C_dep,0=A_f,0*=0 son estipulaciones del núcleo limpio. L_m,0 solo con justificación. Need_preZ/S7 no entra como filtro ni predictor; variables post-Z excluidas.

ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*), con ΔE_T separado. ΔX* se clasifica campo a campo; campos no resueltos quedan ?. Funciones, distribuciones, soporte y parámetros OPEN. No se crean tests ni se ejecuta calibración.


## 290. DEC-C10-103 — resolución aceptada de las cinco decisiones P0 de arquitectura causal (2026-11-15)

Se incorpora DEC-C10-103, aceptada expresamente por el responsable científico tras Gate 120. Las cinco recomendaciones quedan aceptadas como arquitectura de trabajo condicionada:
- A/B continúan como variantes DGP separadas conforme DEC-C10-095; rosters causales separados por defecto y crosswalk/matching solo con equivalencia basal y elegibilidad pre-Z demostradas. DEC-C10-096 sigue delimitada al censo de validación B1/Need_preZ.
- Asignación individual por UE es la arquitectura confirmatoria preferida solo tras demostrar aislamiento material. La instancia B1 por UE no demuestra por sí sola aislamiento de recursos, dependencias mutables, agentes, canales, estado, side effects o carryover. Sin aislamiento, cluster/mapa de exposición requieren contrato propio; interferencia no mapeada exige bounds/abstención.
- El target es promedio por UE bajo asignación individual aislada. Si se adopta cluster, reabrir unidad y ponderación UE/cluster.
- θ_A(q_X*,r_common;V_cont), sobre el vector completo ΔT_acc* en B, es el objetivo focal de atribución, condicionado a factibilidad, soporte e identificación. ITT-D2 conserva el efecto total del paquete como estimando separado; C4 es mediación interventional longitudinal secundaria condicionada; efecto directo/no mediado queda fuera hasta definición propia. No calcular residual por resta.
- UE tiene identidad inmutable dentro del roster/package versionado; matching A/B solo mediante crosswalk explícito. No se materializa ue_id ni se fuerza UE→U_G.

Permanecen abiertos el roster B/P*τ2, aislamiento, UE=UA, Z/RNG/provenance, soporte de q_X*/g_A/r_common, mapping D2→g_A, medición y calibración V_cont/S3, T*/Δ/K, missingness, sensibilidad, potencia, vías colaterales y criterios Analyzer/Evaluator. La aceptación no acredita esas condiciones.

No Design Freeze, materialización, implementación ni ejecución. No cambios en main, C0, U_G, RMA, Evidence→Claim Matrix o STATUS. PR #116 Draft. scientific_execution=false; execution_authorized=false.


## 291. Gate 121 — suficiencia de evidencia material y adjudicación del aislamiento entre UE (2026-11-15)

Registro: `00_GOVERNANCE/SIP/C10_S_ISOLATION_EVIDENCE_SUFFICIENCY_AND_ADJUDICATION_GATE_121_DRAFT_001.md`.

Gate 121 reutiliza Gate 102, PB material D2, Adapter Provision Manifest, U_G Inventory Register Template, IAM overlays, PE, PROV-01…12 y UNIT-01…14. No crea un segundo inventario ni nuevos test IDs. La identidad lógica de instancia única por UE no demuestra aislamiento físico. Se distingue compartición, transmisión entre UE y consecuencia causal.

La asignación individual UE=UA solo puede declararse `ISOLATION_DEMONSTRATED_WITHIN_SCOPE` si se satisfacen IS-1…IS-8: frontera/cobertura cerradas; inventario versionado y trazable; ausencia de transmisión cruzada relevante; recursos no rivales/segregados; permisos/datos segregados; alternativas y medición preservadas; temporalidad/rollback cubiertos; adjudicación independiente bajo firewall efectivo. Un solo requisito relevante OPEN, ?, PARTIAL, MISSING o CONFLICTING impide el PASS. NONE/MISSING no equivale a 0.

Si la interferencia es contenible por grupos definidos pre-Z, se requiere contrato cluster y reabrir UA, estimando y ponderación; si es mapeable con soporte, contrato versionado G_i(Z_-i); si no es mapeable o carece de soporte, bounds/abstención. No se selecciona arquitectura post-outcome ni se forman clusters retrospectivos.

Estado: `MATERIAL_INVENTORY_NONE / ISOLATION_NOT_DEMONSTRATED / UE_ASSIGNMENT_CONDITIONAL / UNIT_01_14_DOCUMENTED_NOT_EXECUTED / PROV_01_12_DOCUMENTED_NOT_EXECUTED`. El gate no acredita aislamiento, no identifica θ_A, no cierra ITT/medición/soporte, y no autoriza materialización, implementación o ejecución. `scientific_execution=false`; `execution_authorized=false`.


## 292. Gate 122 — expediente mínimo de materialización probatoria del aislamiento (2026-11-15)

Registro: `00_GOVERNANCE/SIP/C10_S_MINIMUM_ISOLATION_EVIDENCE_MATERIALIZATION_DOCKET_GATE_122_DRAFT_001.md`.

Gate 122 reutiliza Gate 121, B-M01…15, S1…S8, U_G, IAM/C_SRC, PE, UNIT-01…14 y PROV-01…12. Define el crosswalk IS-1…IS-8 → afirmación → clases de fuente → registros U_G → cobertura necesaria, además de procedencia, triangulación, roles, secuencia futura y precondiciones de captura.

Dictamen: las fuentes técnicas concretas, el sistema B1/D2, el roster causal, los custodios y los permisos no están identificados en este gate. Los contratos y plantillas de GitHub están disponibles como documentación, pero no constituyen evidencia material del runtime. Se mantiene `SOURCE_AVAILABILITY_UNVERIFIED / MATERIAL_INVENTORY_NONE / ISOLATION_NOT_DEMONSTRATED / UE_ASSIGNMENT_CONDITIONAL`.

Gate 122 no crea registros físicos, no captura datos, no consulta entornos técnicos, no cambia esquemas ni autoriza operaciones. Ninguna de las condiciones IS-1…IS-8 pasa a PASS. `scientific_execution=false`; `execution_authorized=false`.


## 293. Gate 123 — corrección del encuadre sintético de aislamiento y evidencia (2026-11-15)

Registro: `00_GOVERNANCE/SIP/C10_S_SYNTHETIC_ISOLATION_AND_EVIDENCE_REINTERPRETATION_GATE_123_DRAFT_001.md`; addendum al plan: `00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_CORRECTIVE_ADDENDUM_GATE_123_DRAFT_001.md`.

Gate 123 corrige el error de alcance de Gates 121–122: C10-S es un experimento sintético y no requiere localizar infraestructura productiva B1/D2, hosts, runtimes, IAM real, proveedores, custodios ni snapshots externos. Se conservan los Gates 121–122 como historial, pero su exigencia de adquisición de fuentes externas queda supersedida para este experimento.

Se separan cuatro capas: (1) verdad estructural del DGP conocida por Generator; (2) fidelidad con que el harness materializa el DGP; (3) evidencia observada filtrada y sellada por Sealer/Projector; (4) recuperación/abstención de Analyzer y evaluación posterior contra truth por Evaluator. El conocimiento de Generator no demuestra identificabilidad ni recuperación por Analyzer.

IS-1…IS-8 y S1…S8 se conservan como taxonomías, reinterpretadas sobre roster, dependencias, recursos, interferencia, permisos sintéticos, temporalidad, manifests, trazas, snapshots y bundles del mundo generado. U_G solo se reutiliza dentro de sus contratos existentes; no se crea schema ni test ID nuevo.

DEC-C10-103 y la jerarquía de estimandos permanecen sin cambios. UE=UA sigue condicional por escenario DGP y fidelidad del harness; los escenarios con interferencia requieren arquitectura/estimando compatibles; la interferencia no mapeable requiere bounds/abstención. No se declara aislamiento demostrado, identificación de θ_A ni Design Freeze.

No se generan datos, no se modifica código, no se ejecutan pruebas/validadores/simulaciones/estimaciones ni se autoriza ejecución. PR #116 permanece Draft; `scientific_execution=false`; `execution_authorized=false`.


## 294. Gate 124 — auditoría de cobertura y separación de carriles S/M (2026-11-15)

Registro: `00_GOVERNANCE/SIP/C10_S_SYNTHETIC_AND_MATERIAL_D2_SCOPE_COVERAGE_AUDIT_GATE_124_DRAFT_001.md`; addendum al plan: `00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_DUAL_LANE_CORRECTION_GATE_124_DRAFT_001.md`.

Gate 124 confirma que C10-S tiene dos carriles relacionados pero no intercambiables:

- **S — harness sintético:** mundos DGP generados, truth restringida, evidencia observada/sellada, Analyzer ciego y Evaluator posterior. No requiere infraestructura productiva ni fieldwork.
- **M — confirmación material D2/B1:** identidad/roster reales, IAM/C_SRC, snapshots, inventario de dependencias, recursos, aislamiento, soporte y evidencia material.

La especificación integrada del harness §§1, 6–9 declara expresamente esta separación. El inventario finito §14 declara que E1–E4 y B-M01…15 son tipos de evidencia sintética, sin recuperación de SBOM/APIs/runtime/ACL/logs/snapshots externos. PD §4 y §15, el DGP temporal §§6–10/15–17 y el Test Contract Register §§10–12/17/22–23 contienen contratos de interferencia, recursos, truth/observed, adversarios y evaluación. PE §§8–14/16–20 conserva el firewall como contrato lógico, pero no implementado ni probado.

IS-1…IS-8 se clasifican **PARTIAL** en S: hay contratos lógicos reutilizables, pero permanecen abiertos universo/escenarios y parámetros, mapa de interferencia, reglas cuantitativas de recursos, firewall efectivo, oráculos/medición, resets/replay y adjudicación efectiva. En M, IS-1…IS-8 permanecen OPEN / NOT MATERIALIZED / NOT EVIDENCED conforme a PB y Gates 121–122.

Gate 123 acertó al retirar fieldwork externo como precondición del carril S, pero su supersession general de Gates 121–122 era demasiado amplia. Gate 124 la limita: Gates 121–122 no aplican como adquisición material al harness sintético; se conservan como contratos del carril M. No se infiere aislamiento material desde truth o tests sintéticos.

El siguiente trabajo del carril S es consolidar el ledger mínimo de parámetros y escenarios, distinguiendo requisitos esenciales para identificación/recuperación de escenarios secundarios y análisis de sensibilidad, sin inventar valores. El carril M permanece separado y bloqueado a la espera de instancia/roster/autorización material. No se generan datos ni se modifica/ejecuta código. PR #116 sigue Draft; `scientific_execution=false`; `execution_authorized=false`.


## 295. Gate 125 — auditoría de suficiencia del ledger DGP existente y dependencias de Design Freeze (2026-11-16)

Registro: `00_GOVERNANCE/SIP/C10_S_EXISTING_DGP_LEDGER_SUFFICIENCY_AND_FREEZE_DEPENDENCY_AUDIT_GATE_125_DRAFT_001.md`; addendum al plan: `00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_125_LEDGER_REUSE_ADDENDUM_DRAFT_001.md`.

Gate 125 verifica que el ledger paramétrico ya está definido estructuralmente en §16.223 (Gate 69), el roster dirigido y las funciones/potenciales en §§16.188–16.212, y los doce roles de celda C1/C3 en §§16.224–16.225 (Gates 70–71). No se crea otro ledger ni se amplía el roster por defecto. La cobertura conceptual no equivale a materialización ni a recuperación verificada.

Las brechas prioritarias no son simplemente numéricas: (1) la cadena causal D2 de DEC-C10-067 no está representada como etapas separadas en el harness actual; (2) G no equivale a g_A, no existe un par operativo g_A0/g_A1 ni truth/estimador θ_A; (3) q_X*, historias basales, masas y soporte conjunto siguen sin materializarse; (4) asignación/interferencia debe definirse por escenario sintético, sin transferir PASS al carril material; (5) V_cont conserva selección provisional y reglas temporales aceptadas, pero T*, Δ, K, S3 y validez siguen abiertos; (6) el puente V_cont→consecuencia B1→Value contextual no está cerrado; (7) O-CONF/F*, missingness/censura, bounds/abstención y criterios cuantitativos siguen pendientes.

DEC-C10-099…102 se respetan: la selección provisional de V_cont no prueba por sí sola que continuidad funcional sea una consecuencia valorada para B1. B2–B3 exige consecuencia, perspectiva y autoridad de valoración; la relación entre ambas debe justificarse sin circularidad. Por ello, θ_A sobre V_cont no equivale todavía a evidencia confirmatoria de ΔT_acc*→Value contextual.

Gate 125 determina que no estamos cerca de Design Freeze para la pregunta causal ΔT_acc*→Value. Sí existe una arquitectura candidata desarrollada, que permite concentrar el trabajo en dependencias estructurales/semánticas concretas sin reiniciar el diseño. La siguiente operación es Gate 126: auditoría de consistencia/admisibilidad del puente V_cont→consecuencia B1→Value, reutilizando DEC-C10-099…102, B2–B3, B1 Valuation Case, Outcome/Value Operationalization y P179/P182/P183.

La secuencia Gates 181–199 de captura, serialización y procedencia del paquete V_cont permanece como corriente técnica separada: no rellena el DGP causal ni acredita θ_A. No se modifica código, DGP, DEC, C0, U_G, RMA, Evidence→Claim Matrix, STATUS o main; no se crean mundos/test IDs ni se ejecutan validadores, pruebas, simulaciones, estimaciones, calibraciones, productores o benchmarks. PR #116 permanece Draft; `scientific_execution=false`; `execution_authorized=false`.


## 296. Gate 126 — admisibilidad del puente V_cont → consecuencia B1 → Value (2026-11-16)

**Registro:** `00_GOVERNANCE/SIP/C10_S_VCONT_B1_VALUE_BRIDGE_ADMISSIBILITY_AUDIT_GATE_126_DRAFT_001.md`.  
**Addendum al plan:** `00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_126_VALUE_BRIDGE_ADDENDUM_DRAFT_001.md`.  
**Estado:** DEC-C10-099_102_PRESERVED / VCONT_SELECTED_PROVISIONALLY / BENEFICIARY_CONSEQUENCE_NOT_OPERATIONALIZED / VALUE_VALUATION_RULE_OPEN / THETA_A_TARGET_IS_VCONT_NOT_FULL_VALUE / NOT_DESIGN_FROZEN / NO_IMPLEMENTATION / NO_EXECUTION.

Gate 126 audita la consistencia de DEC-C10-099…103 con B2–B3, la reconciliación Outcome/Value y los contratos P179/P182/P183. No reabre las decisiones aceptadas: V_cont sigue siendo la dimensión mínima provisional de Value para B; DEC-C10-100 conserva la agregación temporal igualitaria; DEC-C10-101 fija t0; DEC-C10-102 conserva continuidad estricta por intervalo; DEC-C10-103 mantiene θ_A(q_X*,r_common;V_cont) como estimando focal seleccionado, distinto de ITT-D2 y C4.

El hallazgo es que la función técnica B1 (ENABLED/PROFILE), la consecuencia para B1 respecto de Need_preZ y la valoración contextual son tres niveles distintos. B2–B3 mantiene la consecuencia no operacionalizada y la perspectiva/autoridad de valoración OPEN. Por tanto, la selección de V_cont y su truth temporal no validan automáticamente su interpretación como Value contextual. θ_A puede evaluar atribución causal sobre continuidad funcional; su interpretación como contribución a Value permanece CONDITIONAL hasta justificar el puente no circular hacia consecuencia y valoración.

O-CONF/F* no sustituye ni valida automáticamente V_cont. Se preservan truth_dgp/observed_evidence/evaluation, el canal S3 imperfecto, el firewall Generator/Analyzer/Evaluator y la posibilidad de bounds/abstención. No se crean dimensiones, pesos, instrumentos, umbrales, IDs, parámetros o fixtures. No se modifican DEC, C0, U_G, RMA, Evidence→Claim Matrix, STATUS, Core o main. No hay Design Freeze, implementación ni ejecución; `scientific_execution=false`; `execution_authorized=false`.

**Siguiente operación:** Gate 127 — reconciliar el caso de valoración B1 y Need_preZ con la consecuencia funcional que V_cont puede representar, distinguiendo qué está ya estipulado en el DGP, qué requiere definición normativa adicional y qué no puede identificarse desde la evidencia permitida al Analyzer. No asumir una relación determinista V_cont→Value.


## 297. Gate 127 — reconciliación de Need_preZ, función B1 y consecuencia representable por V_cont (2026-11-16)

**Registro:** `00_GOVERNANCE/SIP/C10_S_B1_NEED_PREZ_VCONT_CONSEQUENCE_RECONCILIATION_GATE_127_DRAFT_001.md`.  
**Addendum al plan:** `00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_127_B1_CONSEQUENCE_RECONCILIATION_ADDENDUM_DRAFT_001.md`.  
**Estado:** B1_FUNCTIONAL_PURPOSE_ACCEPTED / NEED_PREZ_CLASS_DEFINED / PER_UE_TRUTH_OPEN / VCONT_DIMENSION_PROVISIONALLY_SELECTED / CONSEQUENCE_MAPPING_PARTIALLY_ADMISSIBLE / VALUE_VALUATION_RULE_CONDITIONAL / NO_DESIGN_FREEZE.

Gate 127 corrige una sobreextensión potencial de Gate 126. La reconstrucción del caso B1 §§12–17 y del maestro §282 confirma que el propósito funcional mínimo ya está definido: mantener disponible en destino un servicio capaz de admitir solicitudes conforme a ENABLED y exponer PROFILE. No se requiere inventar una operación de negocio adicional; la semántica de procesamiento posterior y de los perfiles puede permanecer abstracta en el DGP sintético.

Need_preZ está definido conceptualmente como propósito basal pre-Z, pero su truth/roster por UE y evidencia/adjudicación siguen OPEN. V_cont representa cumplimiento temporal de la función ENABLED/PROFILE; no equivale a procesamiento exitoso ni al resultado de la oportunidad estandarizada. La continuidad de la capacidad de admisión es una consecuencia focal admisible candidata. Su interpretación como dimensión de Value requiere que el DGP estipule ex ante una regla normativa sintética, desde la perspectiva B1, versionada y simétrica. No se requiere autoridad humana/externa real, pero la regla no puede inventarse por conveniencia ni presentarse como preferencia empírica real.

θ_A sobre V_cont conserva su estimando seleccionado; su interpretación como efecto sobre la dimensión Value queda condicionada a la regla de valoración, validez de medición y identificación. No se transfiere a Value contextual general ni a una afirmación general de creación de valor. Se mantienen vías colaterales/alternativas, truth/observed/evaluation y firewall Generator/Sealer/Analyzer/Evaluator.

Pendientes: Need_preZ por UE; regla normativa DGP; parámetros y S3; vías por escenario; soporte/identificación/sensibilidad de θ_A; criterios cuantitativos y adjudicación. No se crean escalas, pesos, instrumentos, IDs, parámetros, roster o fixtures. No se modifican DEC, C0, U_G, RMA, Evidence→Claim Matrix, STATUS, Core o main. No Design Freeze, implementación ni ejecución; `scientific_execution=false`; `execution_authorized=false`.

**Siguiente operación:** Gate 128 — especificar la mínima regla de valoración sintética admisible para V_cont sin convertirla en tautología de accesibilidad ni introducir una función numérica no justificada; reutilizar DEC-C10-099…103, B1 §§14–17, B2–B3 y P179/P182/P183. Determinar si la regla puede estipularse dentro del DGP y qué elementos necesitan aceptación explícita antes de congelar el diseño.


## 298. Gate 128 — regla normativa mínima VCONT-B1-MIN aceptada (2026-11-16)

**Registro:** `00_GOVERNANCE/SIP/C10_S_VCONT_MINIMUM_SYNTHETIC_VALUATION_RULE_GATE_128_DRAFT_001.md`.  
**Registro de aceptación y routing:** `00_GOVERNANCE/SIP/C10_S_GATE_128_ACCEPTANCE_AND_GATE_129_ROUTING_ADDENDUM_DRAFT_001.md`.  
**Estado:** DEC-C10-099_102_PRESERVED / VCONT_B1_MIN_EXPLICITLY_ACCEPTED / VALUE_DIMENSION_BOUNDED_TO_FUNCTIONAL_CONTINUITY / VALUE_GENERAL_NOT_ESTABLISHED / NO_DESIGN_FREEZE.

El usuario aceptó explícitamente VCONT-B1-MIN el 2026-11-16. La regla se incorpora como estipulación normativa sintética ex ante para la dimensión unitaria V_cont ya seleccionada por DEC-C10-099: desde la perspectiva B1 del mundo sintético, la consecuencia focal es la continuidad temporal de la capacidad del servicio para admitir solicitudes conforme a ENABLED y exponer PROFILE; dentro de esa dimensión, mayor continuidad no se valora peor y niveles iguales representan igual valoración.

No se introduce función cardinal, pesos, umbrales, compensación, índice compuesto o dimensión adicional. La aceptación limita la afirmación a Value en la dimensión de continuidad funcional; no establece Value contextual general, beneficio neto, éxito de negocio ni creación de valor universal. DEC-C10-099…103 permanecen sin modificación. La aceptación conversacional no se presenta como un nuevo Decision Record formal.

Implicaciones del firewall: Generator incorpora la regla versionada ex ante y conserva truth reservada; Sealer expone solo observaciones permitidas; Analyzer estima desde evidencia sellada o entrega bounds/se abstiene, sin acceso a truth/potenciales/parámetros secretos; Evaluator aplica la regla y compara con truth solo después del sellado. La regla no resuelve validez de S3 ni identificación de θ_A.

No se modifican DEC, C0, U_G, RMA, Evidence→Claim Matrix, STATUS, Core o main. No Design Freeze, implementación ni ejecución; `scientific_execution=false`; `execution_authorized=false`.

**Siguiente operación:** Gate 129 — auditoría de identificabilidad y recuperación de θ_A sobre V_cont bajo VCONT-B1-MIN aceptada. Recuperar DEC-C10-095…103, P177/P178/P179/P182/P183, ledger §16.223, matriz temporal de rutas, q_X*, r_common, población/unidad/soporte, interferencia y contratos Generator–Sealer–Analyzer–Evaluator. Distinguir condiciones de identificación, medición S3, bounds/abstención, sensibilidad y decisiones cuantitativas abiertas; no añadir escenarios/parámetros/test IDs por conveniencia.


## 299. Gate 129 — identificabilidad y recuperación de θ_A sobre V_cont (2026-11-16)

**Registro:** `00_GOVERNANCE/SIP/C10_S_THETA_A_IDENTIFICATION_AND_ANALYZER_RECOVERY_AUDIT_GATE_129_DRAFT_001.md`.  
**Addendum al plan:** `00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_129_THETA_A_IDENTIFICATION_ADDENDUM_DRAFT_001.md`.  
**Estado:** THETA_A_ESTIMAND_DEFINED / FULL_VECTOR_G_A_INTERVENTIONS_NOT_MATERIALIZED / Q_X_AND_R_COMMON_NOT_MATERIALIZED / IDENTIFICATION_NOT_ESTABLISHED / VCONT_S3_MEASUREMENT_NOT_VALIDATED / CURRENT_ANALYZER_DOES_NOT_ESTIMATE_THETA_A / P178_BOUNDED_METHOD_BENCHMARK_ONLY / NO_DESIGN_FREEZE.

Gate 129 reutiliza DEC-C10-103, el ledger §16.223, los contratos §§16.226–16.227, Gates 69–86, 90–93 y 110–125 y P177/P178/P179/P182/P183. Confirma que θ_A(q_X*,r_common;V_cont), como intervención sobre el vector completo ΔT_acc*, está definido y seleccionado, pero no materializado ni identificado. Las historias basales/masas q_X*, las políticas conjuntas g_A0/g_A1, su factibilidad/soporte y r_common por celda siguen OPEN. No se crea otro ledger.

El Generator integrado conserva theta_a_truth=None hasta materializar g_A y q_X*. El Analyzer integrado estima ITT-Z e ITT-G, no θ_A. G no equivale a g_A; ITT-D2, ITT-G|Z=0, θ_A y C4 mantienen identidades separadas. La cadena D2 no está completamente representada en el harness. La asignación individual UE es preferida solo condicionada a demostrar aislamiento sintético por construcción/evidencia; cluster o mapa G_i requieren contratos propios; interferencia no mapeada conduce a bounds/abstención.

P178 tiene PASS de reproducibilidad para un benchmark metodológico escalar Q_B1, con N=700, R=10.000/celda, 27 celdas y 270.000 invocaciones, replay byte-identical y 17/17 contract tests en el workflow auditado. Su manifiesto limita el alcance a benchmark estimator only con medición ideal, régimen común, positividad, vía directa ausente e interferencia ausente fijados. No acredita θ_A sobre ΔT_acc*, V_cont/S3, adversidad, interferencia o falta de soporte.

DEC-C10-099…102 mantienen la regla temporal de V_cont; VCONT-B1-MIN está aceptada para la dimensión acotada de continuidad funcional. Sin embargo, T*, Δ, K, S3, cobertura/error/missingness y calibración no están cerrados. P177/P179/P182/P183 permanecen contratos con cobertura parcial, no PASS global.

No se modifica código, schema, roster, test register, DEC, C0, U_G, RMA, Evidence→Claim Matrix, STATUS, Core o main. No se ejecutan validadores, tests, workflows, generación, simulaciones, calibraciones, estimaciones o experimentos. No Design Freeze; `scientific_execution=false`; `execution_authorized=false`.

**Siguiente operación:** Gate 130 — reconciliar los contratos existentes de q_X*, g_A0/g_A1 y r_common frente al ledger §16.223 y los potenciales §16.226, para identificar el mínimo contrato operativo reutilizable y el bloqueo exacto que impide materializar theta_a_truth, sin crear políticas, historias, masas, parámetros, IDs o escenarios.


## 300. Gate 130 — reconciliación de q_X*, g_A0/g_A1 y r_common con contratos existentes (2026-11-16)

**Registro:** `00_GOVERNANCE/SIP/C10_S_QX_GA_RCOMMON_EXISTING_CONTRACT_RECONCILIATION_GATE_130_DRAFT_001.md`.  
**Addendum al plan:** `00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_130_QX_GA_RCOMMON_RECONCILIATION_ADDENDUM_DRAFT_001.md`.  
**Estado:** CONTRACT_SCHEMAS_ALREADY_DEFINED / q_X_HISTORY_ROWS_AND_MASSES_NOT_MATERIALIZED / g_A_PAIR_NOT_SELECTED_OR_VERSIONED / r_COMMON_SEMANTICS_DEFINED_BUT_NOT_CERTIFIED_PER_HISTORY / MATERIALIZATION_AUTHORIZATION_ABSENT / NO_NEW_CONTRACT_REQUIRED / NO_DESIGN_FREEZE.

Gate 130 determina que no falta otra especificación narrativa para los objetos que impiden materializar theta_a_truth. §16.223 ya define el ledger padre por celda; §16.232 (Gate 79) el registro hijo por historia y controles de q_X*/soporte/r_common; §§16.231 y 16.236 (Gates 78/86) cierran la forma conjunta y condicionada por historia de g_A0/g_A1, la definición simbólica de q_X* y el significado operativo de r_common. §16.233 (Gate 80) ya constató que el roster B1/UE no está aprobado/materializado, faltan historias X/H0/C_c y snapshots basales, y no existe autorización de materialización en este ciclo.

q_X* está definido como distribución objetivo conjunta pre-Z, pero carece de roster causal, filas de historia y masas. La forma de g_A está definida, pero no existe par operativo versionado: los extremos deterministas (0,0,0,0)/(1,1,1,1) de §16.230.2 no fueron ratificados por §16.231.1 y §16.236.2, y no hay alternativa aprobada. r_common tiene regla semántica definida, pero no puede certificarse por historia/celda sin historias y potenciales versionados. Factibilidad estructural, evaluabilidad contrafactual del Generator y soporte de identificación del Analyzer permanecen separados.

La dependencia de theta_a_truth es: roster aprobado → historias/snapshots pre-Z → q_X* y masas → par g_A → factibilidad/soporte conjunto → r_common acreditable → potenciales focales. El Generator no debe calcular theta_a_truth desde G y el Analyzer no debe confundir asignación G con intervención focal. No se crean políticas, historias, masas, parámetros, escenarios ni tests; no se modifican código, schema, DEC, C0, U_G, RMA, Evidence→Claim Matrix, STATUS, Core o main. No ejecución; `scientific_execution=false`; `execution_authorized=false`.

**Siguiente operación:** Gate 131 — auditoría de suficiencia de medición/observación de V_cont mediante S3, reutilizando DEC-C10-099…102, el contrato integrado V_cont, P182/P183 y la matriz temporal existente. No fijar T*, Δ, K, tolerancias, tasas de error o calibración por conveniencia; no duplicar matrices ni ejecutar.


## 301. Corrigendum a Gate 130 — semántica de G frente a g_A y θ_A (2026-11-16)

**Registro:** `00_GOVERNANCE/SIP/C10_S_GATE_130_G_ASSIGNMENT_AND_GA_SEMANTICS_CORRIGENDUM_DRAFT_001.md`. Gate 130 debe leerse con esta precisión: el contrato integrado V_cont §1 define G como asignación aleatorizada a una intervención sintética sobre el vector focal completo ΔT_acc*. Por tanto, no es correcto caracterizar G como si careciera de intervención focal. Sin embargo, el ITT-G^{Z=0} de ese benchmark no equivale automáticamente a θ_A(q_X*,r_common;V_cont): falta acreditar correspondencia de niveles con el par g_A0/g_A1 aceptado, población objetivo, soporte por historia, régimen no focal común y medición válida. G tampoco representa la asignación material D2 B_g0^D2/B_g1^D2. Se conserva theta_a_truth=None y la no equivalencia de ITT-G y θ_A. No se altera DEC-C10-103 ni el contrato integrado.

## 302. Gate 131 — suficiencia de medición e identificación observacional de V_cont mediante S3 (2026-11-16)

**Registro:** `00_GOVERNANCE/SIP/C10_S_VCONT_S3_MEASUREMENT_IDENTIFICATION_SUFFICIENCY_AUDIT_GATE_131_DRAFT_001.md`. **Addendum al plan:** `00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_131_S3_MEASUREMENT_AUDIT_ADDENDUM_DRAFT_001.md`.

DEC-C10-099…102 aceptan la dimensión V_cont, su agregación temporal igualitaria, inicio de ventana t0 y continuidad estricta por intervalo. S3 está definido como canal pasivo, no-mutante, vectorial e imperfecto, pero no existe un modelo de medición S3 identificado/validado que permita recuperar puntualmente V_cont a partir de señales observadas. El contrato integrado mantiene medición perfecta y completa como restricción actual de identificación puntual; error o ausencia sin modelo aprobado exige bounds/abstención/INDETERMINATE, no una estimación puntual.

P182-01…12 y P183-01…13, MEAS-01…14 y MISS-01…15 son contratos generales reutilizables, no fixtures/oráculos ejecutados para S3. Gates 172–183 y 199–205 establecen captura/export/provenance/workflow, no validez de medida. No se crean nuevas matrices ni familias de tests, ni se fijan T*, Δ, K, tasas o tolerancias. No ejecución; `scientific_execution=false`; `execution_authorized=false`.

**Siguiente operación:** Gate 132 — crosswalk dirigido entre señales S3 observables, truth A_B1/V_cont, P182/P183, MEAS/MISS y allowlist del Analyzer; distinguir benchmark ideal de robustez a error, sin seleccionar parámetros ni ejecutar.


## 303. Gate 132 — crosswalk S3 observación → truth V_cont y allowlist del Analyzer (2026-11-16)

**Registro:** `00_GOVERNANCE/SIP/C10_S_VCONT_S3_OBSERVATION_TO_TRUTH_CROSSWALK_GATE_132_DRAFT_001.md`. **Addendum al plan:** `00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_132_S3_OBSERVATION_CROSSWALK_ADDENDUM_DRAFT_001.md`.

Gate 132 precisa Gate 131: el harness implementa un canal S3 sintético por unidad e intervalo para ENABLED y PROFILE, con sensibilidad, especificidad y ausencia. El Generator conserva los estados potenciales y la conjunción funcional por intervalo; V_cont se calcula como su media sobre la rejilla. El Sealer aplica allowlist y sello; el Analyzer calcula la conjunción observada solo si la medición está declarada identificada y la cobertura es completa. ScenarioConfig limita esa ruta a Se=1, Sp=1 y missingness=0. No hay corrección calibrada de error, bounds validados, calibración independiente ni resolución temporal intraintervalo.

Existe `R0_MEASUREMENT_ADVERSE` como escenario STATUS_ONLY y un test de software que comprueba abstención. Esto corrige la afirmación de Gate 131 de que no había caso adversarial/test S3: sí existe, pero no demuestra recuperación bajo error. `delta_t_acc_observed` es un vector focal separado de S3. Las etiquetas MEAS/MISS deben conservar su ámbito; el register reutiliza etiquetas en subdominios distintos y no deben fusionarse por coincidencia nominal.

El benchmark ideal puede servir como baseline metodológico para ITT-Z/ITT-G bajo las restricciones del contrato; no acredita robustez de medida, θ_A ni el puente completo V_cont→consecuencia B1→Value. No se modifica código, schemas, test register, workflows, DEC, main, RMA, Evidence→Claim Matrix o STATUS. No ejecución; `scientific_execution=false`; `execution_authorized=false`.

**Siguiente operación:** Gate 133 — reconciliar alcance del benchmark ideal y R0_MEASUREMENT_ADVERSE, MEAS/MISS, cobertura técnica ya existente y perfiles de ejecución, además de correspondencia temporal con DEC-C10-100…102. No crear IDs ni ejecutar.


**Precisión Gate 132:** el harness materializa `potential_interval_truth` como 0/1; S3 missingness es `None` en observación y no UNKNOWN de la truth. La ruta UNKNOWN/bounds de DEC-C10-100 no está materializada y debe reconciliarse en Gate 133, sin asumir equivalencia.


## 304. Gate 133 — benchmark ideal, abstención adversarial y correspondencia temporal V_cont (2026-11-16)

**Registro:** `00_GOVERNANCE/SIP/C10_S_VCONT_IDEAL_BENCHMARK_AND_TEMPORAL_SEMANTICS_RECONCILIATION_GATE_133_DRAFT_001.md`. **Addendum al plan:** `00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_133_IDEAL_BENCHMARK_RECONCILIATION_ADDENDUM_DRAFT_001.md`.

Gate 133 delimita el benchmark integrado: DGP con truth ENABLED/PROFILE y V_cont binario por intervalo; S3 con sensibilidad/especificidad/ausencia; ruta numérica solo con S3 perfecto y completo. Permite evaluar recuperación de los cuatro estimandos de asignación ITT-Z/ITT-G definidos en el contrato integrado bajo sus condiciones; no estima θ_A (`theta_a_truth=None`) ni acredita robustez a error/ausencia o el claim ΔT_acc→Value.

`R0_MEASUREMENT_ADVERSE` es STATUS_ONLY/INDETERMINATE con abstención esperada para sus cuatro estimandos. Existe test fuente que comprueba package_status y g_assignment_status INDETERMINATE y expected_abstention_respected; no se ejecutó. Gates 200–205 ya gobiernan EP-01/02/03; Gate 205 mantiene abierta la validación integral YAML/actionlint y shell/Python de workflows.

La correspondencia temporal con DEC-C10-100…102 es parcial: ventana común, intervalos iguales y truth por unidad/régimen/intervalo sí están representados; UNKNOWN funcional en truth, eventos intraintervalo, event/observation/ingestion time y bounds para UNKNOWN no. La ausencia S3 (`None`) no equivale a UNKNOWN de truth.

**Siguiente operación:** Gate 134 — determinar si UNKNOWN/continuidad estricta completa debe formar parte del benchmark o si el alcance binario intervalizado está expresamente autorizado como benchmark acotado. Sin cambios de código ni ejecución; `scientific_execution=false`; `execution_authorized=false`.


## 305. Gate 134 — conformidad temporal de V_cont y alcance admisible del benchmark integrado (2026-11-16)

**Registro:** `00_GOVERNANCE/SIP/C10_S_VCONT_TEMPORAL_SEMANTICS_CONFORMANCE_AND_BENCHMARK_SCOPE_GATE_134_DRAFT_001.md`. **Addendum al plan:** `00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_134_TEMPORAL_SEMANTICS_ADDENDUM_DRAFT_001.md`.

Gate 134 reconcilia DEC-C10-099…102. No queda pendiente elegir entre truth binaria y tri-valuada: DEC-C10-100 ya acepta truth `{1,0,?}` por intervalos iguales y bounds `[n1/K,(n1+n?)/K]`; DEC-C10-101 inicia la ventana en t0 incluyendo provisión/instalación; DEC-C10-102 exige continuidad estricta durante todo intervalo, 0 ante cualquier incumplimiento confirmado y ? solo si el Generator no determina truth. Missingness/lag/cobertura S3 son observacionales y no equivalen a UNKNOWN funcional.

El harness actual usa truth binaria 0/1 por intervalo, no materializa UNKNOWN ni bounds y no conserva eventos fechados que permitan adjudicar cualquier incumplimiento intraintervalo o frontera. Su correspondencia temporal es parcial. El benchmark actual se conserva como baseline metodológico restringido para ITT-Z/ITT-G bajo DGP binario y S3 perfecto/completo; no es implementación completa ni validación confirmatoria de V_cont. No se emite otra DEC para redecidir semántica ya aceptada.

**Siguiente operación:** Gate 135 — crosswalk DEC → DGP → TruthBundle → Evaluator, sin fijar parámetros ni modificar código/schemas/DEC. No ejecución; `scientific_execution=false`; `execution_authorized=false`.


## 306. Gate 135 — crosswalk DEC → DGP → TruthBundle → Evaluator (2026-11-16)

**Registro:** 00_GOVERNANCE/SIP/C10_S_DEC_TO_DGP_TRUTHBUNDLE_EVALUATOR_CONFORMANCE_CROSSWALK_GATE_135_DRAFT_001.md. **Addendum al plan:** 00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_135_TRUTHBUNDLE_EVALUATOR_ADDENDUM_DRAFT_001.md.

Gate 135 localiza la pérdida principal de conformidad en Generator: ENABLED/PROFILE se generan como estados binarios por slot y su conjunción fuerza 0/1; TruthBundle conserva la frontera de truth reservada, pero no contiene actualmente UNKNOWN funcional. El código no conserva event log de transiciones efectivas intraintervalo, por lo que no acredita continuidad estricta en cualquier instante. transition_slots y estados por slot no sustituyen la cronología necesaria.

Se distingue UNKNOWN funcional (indeterminación de truth por Generator) de S3 None/MISSING, error observado y lag event/observation/ingestion. Sealer debe seguir sellando solo observaciones permitidas, sin TruthBundle. Evaluator verifica el sello y compara ITT-Z/ITT-G puntuales, pero no calcula bounds tri-valuados de V_cont. Los bounds individuales por unidad/régimen son [n1/K,(n1+n?)/K]; no se prescribe trasladarlos a contrastes causales restando extremos marginales, pues requieren contrato conjunto de potenciales, población, soporte e interferencia.

Se reutilizan TruthBundle como frontera, S3/Sealer/firewall, baseline ideal bajo S3 perfecto/completo y evaluación puntual ITT existente, con alcance limitado. Permanecen no implementados UNKNOWN, adjudicación por eventos intraintervalo, bounds de V_cont y bounds causales. No se modifican código, schemas, DEC, tests, workflows ni parámetros.

**Siguiente operación:** Gate 136 — auditoría de suficiencia de los contratos temporales existentes (DGP temporal/roles, plan §§16.195–198, P182/P183/MEAS/MISS), para localizar solo vacíos genuinos antes de decidir cualquier cambio de diseño. No ejecución; scientific_execution=false; execution_authorized=false.


## 307. Gate 136 — suficiencia de contratos temporales y vacíos residuales (2026-11-16)

**Registro:** 00_GOVERNANCE/SIP/C10_S_TEMPORAL_CONTRACT_SUFFICIENCY_AND_REMAINING_GAPS_GATE_136_DRAFT_001.md. **Addendum al plan:** 00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_136_TEMPORAL_CONTRACT_SUFFICIENCY_ADDENDUM_DRAFT_001.md.

La auditoría de §§16.195–198 del plan y §§49–55 del contrato DGP determina que ya están especificados el reloj normalizado desde t0, el soporte común, episodios funcionales con estado previo/posterior, event_time, versión y provenance, continuidad estricta por todos los intervalos intersectados, separación de los relojes truth/agregación/S3, mecanismos de captura snapshot/log/híbrido y estrategia general de bounds/abstención. No se crean otra matriz, escenarios ni familia de pruebas.

Quedan dos vacíos documentales: (1) fuente/condición generadora legítima de UNKNOWN funcional para A_B1/V_cont, distinta de S3 missingness y de una omisión del propio DGP/harness; (2) la regla semiabierta [b_k,b_{k+1}) y asignación de frontera al intervalo que comienza allí está propuesta, pero pendiente de versionado/adopción antes de materializarla. DEC-C10-101 ya fija t0 post-Z e incluye provisión/instalación; falta mapping concreto en event history/harness, no redefinir la ventana.

P182/P183/MEAS/MISS son criterios reutilizables, no evidencia de materialización, calibración, ejecución o PASS. No se modifican decisiones, código, schemas ni parámetros.

**Siguiente:** Gate 137 — delimitar UNKNOWN funcional y verificar precedencia/adopción de frontera; luego preparar crosswalk de implementación sin autorizar cambios ni ejecución. scientific_execution=false; execution_authorized=false.


## 308. Gate 137 — docket de UNKNOWN funcional y convención de frontera (2026-11-16)

**Registro:** 00_GOVERNANCE/SIP/C10_S_UNKNOWN_AND_INTERVAL_BOUNDARY_DECISION_DOCKET_GATE_137_DRAFT_001.md. **Addendum:** 00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_137_UNKNOWN_BOUNDARY_DOCKET_ADDENDUM_DRAFT_001.md.

La reconstrucción de DEC-C10-100…102, Decision Log hasta DEC-C10-103, DGP §§48–55 y plan §§16.193–198 no encuentra una causa intrínseca ya aceptada para que Generator emita UNKNOWN funcional en A_B1. P182/P183/MEAS/MISS describen incertidumbre del canal observacional, no una causa de UNKNOWN de truth. Se recomienda no fabricar ? en historias sintéticas completas y determinadas; conservar el valor tri-valuado y sus bounds, permitiendo ? solo cuando un contrato DGP explícito defina una indeterminación funcional propia con condición semántica y provenance reservada. No se inventa aquí esa condición.

La convención semiabierta [b_{k−1},b_k) para intervalos internos, con el último intervalo incluyendo T*, está recomendada consistentemente en DGP §49 y plan §§16.193.4, 16.195 y 16.198.2. DEC-C10-102 exige asignación determinista, única y versionada, pero no la adopta; no se encontró aceptación posterior hasta DEC-C10-103. Se propone aceptación expresa antes de versionar/materializar. No se crea DEC-C10-104 ni se modifica el Decision Log antes de la aceptación.

**Siguiente tras la decisión:** crosswalk de conformidad de implementación hacia Generator → TruthBundle → Sealer → Analyzer → Evaluator. Sin cambios de código/schema ni ejecución; scientific_execution=false; execution_authorized=false.


## 309. DEC-C10-104 — aceptación de frontera y regla conservadora de UNKNOWN (2026-11-16)

**Registro autónomo:** 00_GOVERNANCE/decisions/DEC-C10-104_VCONT_INTERVAL_BOUNDARY_AND_GENERATOR_UNKNOWN_RULE_ACCEPTANCE.md. **Gate de origen:** Gate 137; **Decision Log:** C10_S_DECISION_LOG_DRAFT_001.md.

El usuario acepta la convención versionada: para b0=t0 < … < bK=T*, I_k=[b_{k−1},b_k) en k=1,…,K−1 e I_K=[b_{K−1},b_K]. Los eventos en fronteras internas se asignan al intervalo que comienza allí; los eventos en T* al último. Los episodios de fallo que cruzan fronteras afectan a todos los intervalos intersectados. No se fijan T*, K, Δ, unidad, resolución, frecuencia ni detectabilidad.

Se acepta la regla conservadora: se mantiene {1,0,?} y la propagación a bounds de DEC-C10-100; no se genera ? en historias completas y determinadas. UNKNOWN funcional requiere una estipulación DGP futura, explícita y tipada, que defina indeterminación intrínseca de A_B1, condición, alcance y provenance. S3 missingness/lag/error/cobertura, omisiones de DGP/harness, eventos/timestamps no modelados, fallo de observación o defectos de implementación no son UNKNOWN funcional.

DEC-C10-100…103 permanecen vigentes salvo esta especificación complementaria. No se autoriza código, schemas, tests, materialización, generación, simulación, calibración, estimación, ejecución ni Design Freeze. scientific_execution=false; execution_authorized=false.


## 310. Gate 138 — crosswalk DEC → Generator → TruthBundle → Sealer → Analyzer → Evaluator (2026-11-16)

**Registro:** 00_GOVERNANCE/SIP/C10_S_DECISION_TO_GENERATOR_TRUTHBUNDLE_SEALER_ANALYZER_EVALUATOR_CONFORMANCE_GATE_138_DRAFT_001.md. **Addendum al plan:** 00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_138_CONFORMANCE_CROSSWALK_ADDENDUM_DRAFT_001.md.

Gate 138 confirma que el harness integrado conserva una arquitectura útil de DGP sintético con potenciales Z/G, TruthBundle separado, proyección observacional, Sealer, Analyzer y Evaluator, pero todavía no es conforme con la semántica confirmatoria completa de V_cont. Generator produce ENABLED/PROFILE y conjunción binaria por slot, sin event history fechado que acredite continuidad estricta intraintervalo. provision_ok es un sorteo binario, no una cronología separada de provisión e instalación. TruthBundle mantiene arrays actuales binarios, sin truth tri-valuada ni bounds individuales. Analyzer opera en ruta puntual bajo S3 perfecto/completo y se abstiene ante missingness/medición no identificada; no implementa bounds V_cont ni corrección por error. Evaluator valida integridad y compara ITT-Z/ITT-G escalares, pero no evalúa recuperación/cobertura de bounds V_cont.

Se conserva el firewall: Projector/Sealer no reciben TruthBundle; Analyzer consume solo evidencia sellada; Evaluator abre truth tras verificar la salida. S3 missingness/error/lag no modifica truth funcional. DEC-C10-104 ya fija frontera semiabierta y regla conservadora de UNKNOWN: historias completas/determinadas producen 1/0; ? requiere estipulación DGP futura explícita.

El baseline ideal se reutiliza solo para los estimandos puntuales ya implementados bajo S3 perfecto/completo. No acredita continuidad estricta, fronteras DEC-C10-104, bounds V_cont ni identificación de θ_A. No se ejecutaron tests, validadores ni simulaciones.

**Siguiente:** especificación lógica mínima de conformidad event history → TruthBundle → bounds → Analyzer/Evaluator; después decidir plan de implementación. Sin cambios de código/schema ni ejecución. scientific_execution=false; execution_authorized=false.


## 311. Gate 139 — especificación lógica EventHistory → TruthBundle → Analyzer → Evaluator (2026-11-16)

**Registro:** 00_GOVERNANCE/SIP/C10_S_LOGICAL_CONFORMANCE_SPEC_EVENTHISTORY_TRUTHBUNDLE_ANALYZER_EVALUATOR_GATE_139_DRAFT_001.md. **Addendum al plan:** 00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_139_LOGICAL_CONFORMANCE_ADDENDUM_DRAFT_001.md.

Gate 139 especifica la cadena lógica mínima sin schema físico ni parámetros nuevos. EventHistory es truth reservada con estados funcionales efectivos, transiciones fechadas, identidad/versión y provenance; la adjudicación A_B1 por intervalo aplica DEC-C10-101/102/104 y continuidad estricta; TruthBundle conserva potenciales, truth por intervalo, n1/n0/n?, bounds y trazabilidad; Analyzer consume solo evidencia sellada; Evaluator abre truth después y valida correspondencia, recuperación, bounds y abstención.

Se reutiliza DGP temporal §§49–55, que ya propone event_time, familias de transición, relojes separados, horizonte común y orden de generación. Su estado sigue siendo DRAFT/propuesto; Gate 139 no lo convierte en contrato aprobado ni implementado. El harness sigue sin event history materializado.

Se explicita la distinción entre truth bounds DEC-C10-100 [n1/K,(n1+n?)/K] y Analyzer bounds por identificación parcial desde S3: son objetos distintos. DEC-C10-104 implica n?=0 para historias sintéticas completas/determinadas; S3 missingness/error/lag no crea UNKNOWN funcional. Una causa intrínseca de ? requerirá estipulación DGP futura explícita y aceptada. No existe tal causa aprobada actualmente.

El baseline ITT-Z/ITT-G, TruthBundle como frontera, Sealer/firewall, S3 ideal y abstención adversarial se reutilizan en su alcance. No acreditan V_cont temporal completo, bounds Analyzer ni θ_A. Pendientes: estado/versionado del DGP temporal, mapping post-Z de provisión/instalación, derivación determinista EventHistory→A_B1, método Analyzer bounds o abstención y criterio de cobertura Evaluator.

No se modificaron código/schema/DEC/tests/workflows ni se ejecutó ninguna operación técnica o científica. scientific_execution=false; execution_authorized=false.


## 312. Gate 140 — reconciliación DGP temporal, mapping post-Z y alcance inicial Analyzer (2026-11-16)

**Registro:** 00_GOVERNANCE/SIP/C10_S_TEMPORAL_DGP_AND_ANALYZER_SCOPE_RECONCILIATION_GATE_140_DRAFT_001.md. **Addendum al plan:** 00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_140_TEMPORAL_ANALYZER_RECONCILIATION_ADDENDUM_DRAFT_001.md.

La reconstrucción histórica determina que las tres dependencias propuestas tras Gate 139 ya tienen cobertura lógica en contratos existentes. DGP temporal §§49–55 define inventario B1, familias de transición, relojes, horizonte, mapping de perfiles y P182/P183/MEAS/MISS, cobertura adimensional y orden de generación. Sigue siendo DRAFT y requiere aceptación/versionado explícitos antes de considerarlo baseline congelado; no necesita una DEC por subsección.

El mapping post-Z W_programmed → W_attempt → receipt → S_install → C_dep* está definido a nivel contractual. DEC-C10-101 incluye provisión e instalación desde t0 inmediatamente posterior a Z. Estas etapas no son automáticamente fallos B1: solo su efecto funcional efectivo sobre ENABLED/PROFILE y la capacidad de admisión determina A_B1. El vacío actual es de materialización: el harness usa provision_ok binario y no conserva la cronología diferenciada/event history.

El Analyzer inicial puede limitarse a estimación puntual bajo S3 perfecto/completo y abstención INDETERMINATE ante missingness/error no corregidos. El contrato integrado no habilita bounds sin un método y contrato aprobados. Esto conserva el benchmark ideal y los controles adversariales de abstención en su alcance actual, sin afirmar recuperación bajo S3 imperfecto ni convertir ITT-Z/ITT-G en θ_A.

No se requiere nueva semántica, DEC, ledger, escenario ni schema para estas tres cuestiones. Siguiente: revisión de aceptación/versionado del DGP temporal y delta de implementación trazable contra contratos existentes. Esta recomendación no acepta formalmente el DGP ni autoriza implementación. C10-S global sigue abierto por θ_A/q_X*/g_A/r_common, identificación, soporte/interferencia, calibración y criterios de recuperación.

No se modificó código, schema, DEC, tests, workflows, main ni PR base. No hubo ejecución. scientific_execution=false; execution_authorized=false.


## 313. Gate 141 — revisión de aceptación del contrato DGP temporal §§48–55 (2026-11-16)

**Registro:** 00_GOVERNANCE/SIP/C10_S_DGP_TEMPORAL_CONTRACT_ACCEPTANCE_REVIEW_GATE_141_DRAFT_001.md. **Addendum al plan:** 00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_141_DGP_TEMPORAL_ACCEPTANCE_REVIEW_ADDENDUM_DRAFT_001.md.

La reconstrucción confirma que el contrato DGP temporal §§48–55 sigue DRAFT/NO APROBADO/NO IMPLEMENTADO. DEC-C10-100…104 sí están aceptadas y prevalecen: no se reabren agregación V_cont, inicio t0 post-Z, continuidad estricta, fronteras semiabiertas ni UNKNOWN conservador.

Gate 141 recomienda aceptación parcial como especificación técnica de trabajo de: inventario/familias B1 y relojes separados (§§49–50), principio de horizonte común/censura (§52), reutilización de perfiles/IDs existentes (§53), plan de cobertura (§54, sin calibración aprobada) y orden lógico Generator→truth→S3→Analyzer→Evaluator (§55). §48 se reconoce solo como integración de decisiones vigentes. §51 y parámetros temporales/mecanismos S3 siguen propuestos y abiertos.

La aceptación parcial R141-A requiere aprobación expresa del usuario. R141-B condiciona la aceptación futura del contrato completo a una revisión versionada que armonice frontera/UNKNOWN con DEC-C10-104 y distinga bounds futuros de la ruta inicial Analyzer ideal + abstención. No se modifica el DGP original ni el Decision Log. La implementación del harness sigue pendiente.

No hay Design Freeze, cambios de código/schema ni ejecución. scientific_execution=false; execution_authorized=false.


## 314. Gate 142 — aceptación parcial y armonización del DGP temporal (2026-11-16)

**Registro:** 00_GOVERNANCE/SIP/C10_S_DGP_TEMPORAL_PARTIAL_ACCEPTANCE_AND_HARMONIZATION_GATE_142_DRAFT_001.md. **Addendum:** 00_GOVERNANCE/SIP/C10_S_DGP_TEMPORAL_CONTRACT_HARMONIZATION_ADDENDUM_GATE_142_DRAFT_001.md.

El usuario aceptó expresamente R141-A y R141-B. Quedan aceptados como especificación técnica de trabajo, no congelada: §§48–50, §52, §53 y §55 dentro de sus límites; §54 únicamente como plan de cobertura. §51, coordenada, rejilla, anclaje, soporte, mecanismo S3 y parámetros temporales/calibración permanecen OPEN. DEC-C10-100…104 prevalecen sin cambios.

Se registra la armonización versionada exigida por R141-B: DEC-C10-104 gobierna fronteras/UNKNOWN; ? funcional requiere estipulación explícita Generator/DGP y nunca representa missingness/error/lag S3 ni defectos del harness; bounds Analyzer son posibilidad futura no aprobada; la ruta inicial es estimación puntual bajo S3 perfecto/completo y abstención INDETERMINATE si no identifica. El DGP original se conserva inalterado.

El DGP íntegro §§48–55 no queda aceptado ni congelado. La aceptación documental no materializa EventHistory/TruthBundle ni acredita conformidad del harness. Próximo trabajo documental: delta único de implementación trazable. No hay autorización de código ni ejecución.

scientific_execution=false; execution_authorized=false.


## 315. Gate 143 — delta único de implementación temporal V_cont (2026-11-16)

**Registro:** 00_GOVERNANCE/SIP/C10_S_VCONT_TEMPORAL_IMPLEMENTATION_DELTA_SPECIFICATION_GATE_143_DRAFT_001.md. **Addendum:** 00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_143_TEMPORAL_IMPLEMENTATION_DELTA_ADDENDUM_DRAFT_001.md.

Gate 143 prepara un delta único para el harness integrado. La inspección estática del blob 88c6c7bd6f82353e64a4f12edbe2e2abc2cec002 identifica la limitación actual: truth por intervalos generada directamente como ENABLED∧PROFILE, rejilla uniforme obligatoria, provision_ok binario y ausencia de EventHistory de transiciones fechadas/adjudicación estricta desde eventos. S3 representa None/MISSING separadamente y Analyzer se abstiene ante medición no identificada; Evaluator actual evalúa ITT-Z/ITT-G, no bounds temporales V_cont.

El delta D1–D6 comprende EventHistory por unidad/potencial (z,g); adjudicador A_B1 estricto conforme DEC-C10-102/104; TruthBundle temporal versionado y bounds de truth DEC-C10-100; canal S3/Sealer independiente sin truth leakage; Analyzer puntual ideal + abstención sin bounds propios; Evaluator post-sellado que separa truth bounds y resultados Analyzer.

La baseline actual se preserva intacta. La ruta temporal sería una versión sucesora con identidad/hashes propios. No fijar unidad temporal, coordenada, event_time numérico, §51, T*, Δ, K, soporte, τ_follow ni calibración. Estas dependencias impiden implementación inmediata.

No se modificó código, tests, schemas, DGP, DEC ni Decision Log. No hubo pruebas, simulaciones, calibración o workflows. Preflight, tests y cambios de código requieren autorización separada.

scientific_execution=false; execution_authorized=false.


## 316. Gate 144 — semántica mínima de event_time y transiciones para V_cont (2026-11-16)

**Registro:** 00_GOVERNANCE/SIP/C10_S_EVENT_TIME_AND_TRANSITION_SEMANTICS_GATE_144_DRAFT_001.md. **Addendum:** 00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_144_EVENT_TIME_SEMANTICS_ADDENDUM_DRAFT_001.md.

Gate 144 confirma que DEC-C10-100…104 y Gates 135–143 fijan agregación, t0, continuidad estricta, fronteras, UNKNOWN, separación de relojes y firewall. DGP §51 contiene una coordenada normalizada x=(t−t0)/W_c, pero quedó fuera de la aceptación parcial Gate 142 y sigue como propuesta.

Vacío no cerrado: persistencia del estado entre transiciones, estado inicial post-Z, simultaneidad/igual event_time y representación de estados intermedios. El orden ordinal preserva EventHistory, pero no basta para adjudicar intervalos sin comparación con fronteras.

R144-A propone proceso de estado por tramos, estado inicial en t0, eventos before/after con provenance, simultaneidad atómica y suborden explícito para secuencias con estados intermedios, y aplicación de DEC-C10-104 cuando exista rejilla comparable. Historias completas/determinadas producen 1/0; defectos de historia no producen funcional UNKNOWN.

R144-B mantiene §51 completo, reloj numérico, soporte, T*, ρ_follow, Δ, K y contrato/calibración S3 abiertos. La aceptación de R144-A no autoriza implementación ni aprueba EventHistory físico, rejilla o adjudicador. Requiere aceptación expresa.

No se modificó DGP, DEC, Decision Log, schemas, código, tests, workflows ni artefactos canónicos main. No hubo ejecución.

scientific_execution=false; execution_authorized=false.


## 317. Gate 144 — aceptación expresa de R144-A (2026-11-16)

El usuario acepta R144-A para el DGP sintético: estado funcional inicial post-Z en t0; persistencia por tramos hasta transición truth explícita; transiciones con before/after, familia causal, identidad/versión, event_time y provenance; simultaneidad genuina atómica; suborden explícito para estados intermedios; aplicación de DEC-C10-104 cuando exista rejilla comparable; y defectos de historia/harness separados de UNKNOWN funcional.

R144-B permanece abierto: §51, reloj/unidad/coordenada contractual, W_c, T*, ρ_follow, Δ, K, soporte y captura/calibración S3. La aceptación no autoriza implementación ni ejecución.

Gate 144 pasa a **R144_A_ACCEPTED_FOR_SYNTHETIC_DGP_LOGICAL_SEMANTICS / R144_B_OPEN**. No se modifican DEC, DGP original, código, schemas, tests, workflows ni main.

scientific_execution=false; execution_authorized=false.


## 318. Gate 145 — contrato lógico de EventHistory (2026-11-16)

**Registro:** `00_GOVERNANCE/SIP/C10_S_EVENT_HISTORY_LOGICAL_CONTRACT_GATE_145_DRAFT_001.md`. **Addendum:** `00_GOVERNANCE/SIP/C10_S_DESIGN_CLOSURE_PLAN_GATE_145_EVENT_HISTORY_CONTRACT_ADDENDUM_DRAFT_001.md`.

Gate 145 reconstruye Gates 94–98, el DGP temporal §§48–55, Gates 135–144, DEC-C10-100…104 y Gate 139. Separa expresamente PROCESS_EVENT observacional (ocurrencias operativas y revisiones de registro) de EventHistory reservado (transiciones funcionales truth generadas por unidad y potencial); no se reutiliza el primero como truth ni se crea un registro observacional duplicado.

R144-A deja aceptados estado inicial ENABLED/PROFILE post-Z en t0, persistencia por tramos, transiciones truth con estado previo/posterior, familia, identidad/versión, event_time y provenance, simultaneidad atómica y suborden explícito. DEC-C10-104 gobierna la futura adjudicación temporal. Gates 139/143 ya sitúan EventHistory/TruthBundle en el firewall Generator→Evaluator, fuera de Sealer/Analyzer.

EventHistory queda **LOGICALLY PARTIALLY CLOSED / MATERIALIZATION OPEN**. Permanecen pendientes el alcance de identidad única y versionado de transición, regeneración/corrección y hashes, criterio verificable de completitud por unidad/potencial/soporte y comparación de event_time con fronteras. §51, reloj, W_c, T*, ρ_follow, Δ, K y S3 siguen OPEN. No se crea DEC ni schema, no se modifica DGP original ni Decision Log, y no hay autorización de código o ejecución.

scientific_execution=false; execution_authorized=false.


## 319. Reconciliación integrada de cierre del diseño y preparación del experimento (2026-11-16)

Se incorpora como síntesis rectora de cierre documental, sin sustituir las fuentes ni crear DEC:

`00_GOVERNANCE/SIP/C10_S_INTEGRATED_DESIGN_CLOSURE_RECONCILIATION_AND_EXECUTION_READINESS_DRAFT_001.md`.

La reconciliación reutiliza §§277–318, DEC-C10-099…104, R144-A, R146-A…D, R147-A/B, R148-A, R150-A, R151-A/A8, R152-A1…A6, Gates 206–208, Gate 121, Gates 129–130, el contrato DGP temporal/roles, el registro de pruebas y el protocolo de calibración/seed bank.

**Dictamen integrado:** diseño no cerrado; factibilidad confirmatoria e identificación de la contribución específica de accesibilidad a Value no establecidas; implementación y ejecución no autorizadas. El trabajo se consolida en cuatro paquetes dependientes: (A) reconciliación normativa DEC-C10-102/Gate 154/R208; (B) §51 y DGP temporal + D2/población/asignación/aislamiento/soporte; (C) medición Outcome/Value, EventHistory/S3/Analyzer/Evaluator y recuperación causal; (D) criterios estadísticos, potencia/precisión, seed banks, conformidad y autorizaciones.

**Bloqueos determinantes:** (1) precedencia normativa PROFILE/D_valid frente al predicado temporal A_B1; (2) parámetros §51 y materialización EventHistory/TruthBundle; (3) asignación D2, roster, aislamiento y soporte; (4) par operativo g_A0/g_A1, q_X* y r_common por historia; (5) Outcome/Value no operacionalizados; (6) calibración S3, bounds y objetivos N/R/MCSE; (7) enforcement técnico del firewall y pruebas no ejecutadas.

El benchmark ideal ITT-Z/ITT-G permanece reutilizable únicamente en su alcance binario y S3 perfecto/completo. No acredita V_cont temporal completo, θ_A, robustez a error/ausencia ni ΔT_acc→Value. La ausencia de identificación actual no es evidencia de efecto nulo.

No se modifica ninguna DEC, DGP original, código, schema, test, workflow, RMA, Evidence→Claim Matrix, STATUS o Core. No se ejecutan validadores, pruebas, generación, calibración, simulación, estimación o Monte Carlo. No Design Freeze.

`scientific_execution=false`; `execution_authorized=false`; `implementation_authorized=false`.


## 320. Paquete A — propuesta integrada de precedencia normativa DEC-C10-102 / Gate 154 (2026-11-16)

Se completa la reconstrucción normativa y se prepara una única propuesta complementaria, sin reabrir ni modificar decisiones aceptadas:

`00_GOVERNANCE/SIP/C10_S_DEC-C10-102_COMPLEMENTARY_SCOPE_DECISION_PROPOSAL_DRAFT_001.md`.

**Hallazgo integrado:** Gate 154 ya fue aceptado expresamente y delimita A_B1/V_cont al comportamiento de admisión/no-admisión exigido por ENABLED, incluida la disponibilidad runtime constitutiva que impida realizarlo. R150-A mantiene PROFILE exposure como obligación contractual; R151-A8 excluye su adjudicación temporal por ausencia de trayectoria truth independiente; R208-A conserva PROFILE como configuración declarativa versionada y D_valid como dimensión separada. La composición es científicamente coherente si se formaliza la precedencia de alcance sin alterar el operador estricto de DEC-C10-102.

**Propuesta C1–C6:** (C1) alcance temporal A_B1; (C2) semántica ENABLED=true/false; (C3) PROFILE y D_valid; (C4) runtime constitutivo/EventHistory; (C5) operador estricto y {1,0,?}; (C6) límite de la afirmación de V_cont. La propuesta preserva todas las obligaciones y decisiones históricas, y descarta inferir PROFILE exposure desde admisión o convertir ausencia de representación/observación en UNKNOWN.

**Estado:** propuesta completa pendiente de aceptación expresa. No se registra DEC-C10-105 como aceptada. Si se acepta, se cerrará únicamente el crosswalk normativo lógico para el DGP sintético vigente; §51, materialización temporal, D2, identificación, medición, potencia y ejecución seguirán abiertos.

No modifica DEC-C10-068/099…104, DGP original, §51, código, schema, tests, RMA, Matrix, STATUS o Core. Sin Design Freeze, implementación ni ejecución.

`scientific_execution=false`; `execution_authorized=false`; `implementation_authorized=false`.


## 321. Paquete A — aceptación de C1–C6 (2026-11-16)

El responsable científico acepta conjuntamente C1–C6 de `C10_S_DEC-C10-102_COMPLEMENTARY_SCOPE_DECISION_PROPOSAL_DRAFT_001.md`. Registro: `C10_S_DEC-C10-102_COMPLEMENTARY_SCOPE_ACCEPTANCE_RECORD_DRAFT_001.md`.

El crosswalk DEC-C10-102/Gate 154/R150-A/R151-A8/R152-A/R208-A queda **CLOSED_FOR_CURRENT_SYNTHETIC_DGP_LOGICAL_SCOPE**. Se preserva DEC-C10-102 y no se crea DEC-C10-105. V_cont queda delimitado a continuidad de admisión/no-admisión efectiva requerida por ENABLED; PROFILE sigue como obligación contractual declarativa, sin adjudicación temporal en el DGP actual; D_valid se evalúa separadamente. Se conserva operador estricto y {1,0,?} sin UNKNOWN por missingness/defectos.

No cierra §51, materialización EventHistory/TruthBundle, D2, población/asignación, aislamiento/soporte, θ_A, Outcome/Value, potencia, tests, firewall técnico o Design Freeze. Sin autorización de implementación/ejecución.


## 322. Paquete B — reconciliación integrada temporal y causal (2026-11-16)

Se incorpora la propuesta integrada `C10_S_PACKAGE_B_INTEGRATED_TEMPORAL_DGP_AND_CAUSAL_DESIGN_CLOSURE_PROPOSAL_DRAFT_001.md`, que reúne §51, DEC-C10-099…104, R144-A/R146-A…D, contrato EventHistory, S3, D2, población, asignación, aislamiento, q_X*/g_A/r_common y θ_A. Reutiliza D2 Assignment/Population/Support, Gate 121, Gate 129, Gate 130, DGP Temporal and Role Contract §§48–55, Path Predicate Temporal Evidence Matrix y contratos UNIT/PROV/P177–P183/MEAS/MISS.

**Dictamen:** reconciliación documental completa; se propone aceptar B1–B6 como cierre del contrato lógico integrado. La coordenada normalizada §51 (t0=0, t_c,max=1) se distingue de los parámetros aún abiertos ρ_follow/T*, Δ/K y de la calibración S3. EventHistory y la adjudicación conservan R144-A/R146-A…D y la separación truth/PROCESS_EVENT/S3/Analyzer/Evaluator. D2 preserva Z frente a programación/provisión, P*τ2/P*_F, UE/UA/UO, ITT y θ_A separados; aislamiento, roster, asignación, q_X*, g_A y r_common siguen sin materialización/certificación.

**Estado:** PROPOSED_FOR_ACCEPTANCE. La aceptación B1–B6 cerraría únicamente el contrato lógico; no convertiría parámetros, población, soporte, θ_A o V_cont-S3 en materialmente identificados, ni autorizaría materialización, implementación o ejecución. Paquete A C1–C6 permanece aceptado (§321).


## 323. Paquete B aceptado y corrección del alcance de materialización (2026-11-16)

B1–B6 quedan aceptadas conjuntamente como contrato lógico temporal y causal integrado. Se registra que C10-S confirmatorio es el carril sintético S; no exige roster real, IAM/C_SRC, snapshots productivos ni evidencia IS-1…8 del carril M. La materialización pendiente es la del DGP sintético, reutilizando §§16.188–16.223, matriz 13×52, vcont_integrated_harness.py, seed-bank protocol y contratos existentes.

Las brechas sintéticas reales son: (i) cadena D2 por etapas; (ii) q_X*, par g_A0/g_A1, r_common y truth/estimador θ_A; (iii) EventHistory con event_time y completitud, más IntervalAdjudication conectado a DEC-C10-100…104; (iv) valores sintéticos versionados para ρ_follow/T*/K/Δ y calibración temporal; (v) proyección S3 temporal imperfecta completa; (vi) asignación/independencia por construcción y escenarios adversariales de interferencia. El puente V_cont→consecuencia B1→Value contextual sigue en Paquete C.

Se autoriza implementación únicamente del carril sintético S en el harness existente y sus tests fuente. No se autoriza ejecutar tests/workflows, generar bancos, calibrar, simular, estimar ni ejecutar el experimento. No se abre carril M ni se promueve contenido a main.


## 324. Paquete B — materialización fuente integrada de componentes sintéticos (2026-11-16)

Se registra la primera materialización de software del carril sintético S conforme a la autorización posterior del usuario. Artefacto rector: C10_S_PACKAGE_B_SYNTHETIC_COMPONENTS_SOURCE_MATERIALIZATION_RECORD_DRAFT_001.md.

Se añade c10s_synthetic_components.py y test_c10s_synthetic_components.py. El bloque implementa: D2 como potenciales por etapas parametrizados (Z/B/W_programmed/W_attempt/receipt/S_install/C_dep*/A_f*/D_f*); EventHistory con identidad, versiones separadas, expected-transition manifest y completitud; adjudicación estricta A_B1/V_cont con fronteras DEC-C10-104 sobre una rejilla explícita suministrada; oracle Evaluator de θ_A sobre inputs explícitos q_X*/g_A0/g_A1/soporte/r_common; comparador de recuperación/abstención; S3 con kernel conjunto de secuencia; composer sobre el Generator existente sin alterar EvidenceCandidate.

No se modificó vcont_integrated_harness.py ni se añadió estimador θ_A al Analyzer. No se han elegido parámetros D2, roster/masas q_X*, políticas g_A, certificados r_common, reloj/§51, T*/Δ/K ni calibración S3. El mapping D_f*→ΔT_acc*→Reach/Π→trayectoria→Outcome/Value permanece abierto. El oracle de truth no equivale a identificación ni recuperación por Analyzer.

El workflow EP-02 amplía su allowlist de ocho a nueve módulos y mantiene dispatch manual en research, confirmación expresa, primary y clean replay. No se ha despachado. No se han ejecutado import, compile, tests, generación, calibración, Monte Carlo, Analyzer, Evaluator o experimento.

**Estado:** SOURCE_COMPONENTS_MATERIALIZED / NOT_TESTED / ANALYZER_THETA_A_NOT_IMPLEMENTED / EXECUTION_NOT_AUTHORIZED. PR #116 Draft; main intacta. DEC, RMA, Evidence→Claim Matrix, STATUS y TGCV Core sin cambios.


## 325. Directriz operativa C10-S — misión ejecutable y regla de no-dispersión (2026-11-16)

La misión y disciplina de trabajo quedan fijadas en 00_GOVERNANCE/SIP/C10_S_EXECUTABLE_EXPERIMENT_MISSION_AND_NO_DRIFT_CONTRACT_001.md.

**Objeto único:** cerrar la materialización del mundo sintético completo y completar el software para ejecutar un experimento sintético reproducible que pueda demostrar, limitar o refutar la contribución causal de la accesibilidad al Value contextual. No se trata de seguir ampliando documentación ni de demostrar solo un estimando auxiliar sobre V_cont.

El mundo ejecutable debe conectar población/covariables/Need_preZ, asignación Z, política D2 y etapas de provisión, C_dep*, A_f*/D_f*, T_acc basal/post y ΔT_acc* completo, Reach/rutas/alternativas, selección/ejecución/trayectoria, Outcome, consecuencia y Value contextual. EventHistory y adjudicación temporal producen truth; S3 produce observación imperfecta; Sealer/Analyzer no reciben truth; Evaluator compara la salida sellada con potenciales y truth independientes. Z/ITT de paquete, g_A0/g_A1, q_X*, r_common y θ_A deben quedar integrados en el mismo DGP, sin confundir efecto de paquete con contribución de accesibilidad. La valoración aplica VCONT-B1-MIN (Gate 128): V_cont es la dimensión sintética acotada de continuidad funcional valorada desde B1; no representa Value general ni autoriza extrapolación a otras dimensiones.

**Regla de no-dispersión:** no abrir nuevos Gates, micro-Gates, matrices o documentos por cada campo/función; no repetir auditorías ni reconstrucciones cerradas. Priorizar código, integración y tests. Documentar únicamente decisiones científicas nuevas, contratos de interfaz realmente no determinados y ejecuciones/resultados materiales. Reutilizar los artefactos y suites existentes. El carril M no es prerequisito.

**Ruta técnica:** (I) world builder end-to-end; (II) intervenciones y truth causal; (III) S3/firewall; (IV) Analyzer/Evaluator; (V) escenarios adversariales y dimensionamiento; (VI) preflight, primary/replay y experimento bajo autorización específica.

**Criterio de finalización:** protocolo/comando reproducible y paquete auditable con resultados por estimando/escenario que distingan recuperación, contribución limitada/parcial, ausencia bajo el DGP probado, no-identificación/abstención y fallo del método. V_cont/Outcome no se equiparan automáticamente a Value.

Esta directriz no altera DEC, DGP, estimandos, claims ni Core. Implementación del carril sintético S autorizada; tests, dispatch, calibración y ejecución científica continúan sin autorizarse. La continuidad futura debe seguir esta directriz y el código GitHub, no memoria conversacional.


## 326. Estado de integración posterior a EP-02 y auditoría de inferencia focal (2026-11-17)

Se registra el estado material posterior a la directriz §325, sin reabrir decisiones ni ampliar el diseño.

**EP-02 — evidencia técnica acotada.** La suite integrada de quince módulos ejecutó 283/283 pruebas PASS y su replay limpio 283/283 PASS sobre el commit probado `4b402b58d209672432250de57881120365e25264`. La ejecución 824 de GitHub Actions está registrada en el README del harness y conserva payload/manifiesto. El diff posterior de limpieza solo restauró el workflow y retiró el centinela temporal. Esta evidencia acredita los contratos de software incluidos en esa suite; no es calibración, Monte Carlo, confirmación científica ni validación general de la hipótesis TGCV.

**Ruta focal materializada.** El código actual integra asignación directa Bernoulli por unidad a `g_A0/g_A1`, selección de EventHistory realizada, proyección S3 por intervalo, Sealer, Analyzer focal y Evaluator independiente. La ruta no sustituye `g_A` por Z o por el G histórico. El Analyzer utiliza las masas declaradas de `q_X*` y un contraste Horvitz–Thompson cuando hay cobertura completa y soporte realizado en ambos brazos; ante missingness, soporte objetivo incompleto o brazo ausente, se abstiene. La prueba end-to-end incluida en EP-02 demuestra integración y aritmética determinista de fixtures, no recuperación estadística general.

**Brecha inferencial focal.** `ThetaAObservationAnalysisResult` incorpora ahora, opcionalmente, un intervalo Hoeffding conservador de rango acotado para el contraste Horvitz–Thompson ponderado por q_X bajo la aleatorización conjunta de dos etapas. Para cada unidad i, la contribución HT queda acotada por `[-q_i/p0_i, q_i/p1_i]`; el radio es `sqrt(0.5 * sum_i width_i^2 * log(2/alpha))`, con `width_i=q_i*(1/p0_i+1/p1_i)`. El nivel de confianza y las probabilidades por historia son entradas explícitas del contrato; no se fija alpha ni precisión por defecto. El sorteo del vector conjunto dentro de la política se integra como parte del resultado unitario acotado [0,1], no se condiciona ni se ignora. El Evaluator reconstruye el intervalo y verifica las probabilidades contra el bundle real de asignación. El pipeline de mundo completo expone `theta_a_confidence_level` opcional, exige certificación explícita `theta_a_unit_independence_certified` y propaga las probabilidades exactas de `assignment_config`; se añadieron regresiones fuente para Analyzer, abstención por missingness y wiring end-to-end. Este intervalo no es error estándar, intervalo Wald, estadístico de contraste ni p-value. Su garantía requiere certificación explícita de independencia entre unidades (aleatorización conjunta independiente, incluidos los sorteos de vector, y ausencia de interferencia), pesos q_X fijos, probabilidades correctas, observación completa y resultado [0,1]. El pipeline exige `theta_a_unit_independence_certified=True`; no deduce esa condición del uso de sales de aleatorización independientes. La fixture de dos unidades solo comprueba aritmética y wiring; no valida cobertura empírica, error tipo I, potencia, precisión útil ni comportamiento en muestras pequeñas o probabilidades desiguales.

**Límite de medición.** El monitor S3 por intervalos implementado es un baseline de cobertura continua ideal con missingness por intervalo; no incorpora un modelo calibrado de falsos positivos/negativos ni demuestra robustez frente a medición imperfecta. La ruta de punto sigue sin identificar continuidad estricta. El benchmark ideal se conserva como baseline acotado y no se etiqueta como conformidad confirmatoria plena de V_cont.

**Límite de calibración.** La matriz 13×52 y su protocolo de seed bank corresponden a los cuatro estimandos de asignación registrados y excluyen expresamente `theta_A`. El protocolo distingue N, R y M; R no se reutiliza como M, y la dimensión M/identidad de outer worlds no está implementada en el harness actual. No se transfieren N=700, R=10.000 ni tolerancias de P178 al estimando focal.

**Siguiente bloque.** El primer contrato inferencial conservador está implementado como `HOEFFDING_TWO_STAGE_BOUNDED_HT_V1` en Analyzer/Evaluator, opcional hasta que se proporcionen nivel de confianza y probabilidades por historia explícitos. Devuelve un intervalo inferencial separado de los límites lógicos y de los límites de medición; se abstiene de producirlo si falta soporte o hay missingness. Falta calibrarlo empíricamente con N/R/M separados y bancos disjuntos, evaluando cobertura, anchura/precisión, error tipo I y potencia cuando se defina un contraste, recuperación puntual y abstención correcta. No se ha implementado SE ni p-value. Los escenarios de medición imperfecta y el puente Outcome/consecuencia B1/Value contextual continúan como dependencias separadas; no se presentan como cerrados.

**Autorización y estado.** La implementación del carril S continúa autorizada por §325. La ejecución EP-02 fue acotada a su autorización técnica específica. No se ha ejecutado calibración, generación de bancos, Monte Carlo, evaluación científica ni experimento confirmatorio. Las modificaciones fuente de Analyzer/Evaluator v0.2 y pipeline posteriores a EP-02 tampoco se han compilado ni probado; las regresiones añadidas son todavía fuente no ejecutada. No se modifica `main), no se promueve el PR #116 (sigue Draft) y no se alteran DEC, RMA, Evidence→Claim Matrix, STATUS o Core.

## 327. EP-02 — regresión de inferencia focal integrada (2026-11-17)

Se ejecutó de nuevo la suite técnica después de implementar el intervalo conservador de dos etapas y propagar sus parámetros por el punto de entrada DGP.

**Run 826:** PASS. GitHub Actions `44174593341`, commit probado `d25065add02057256ea26e412a5abf15d30eb539`. Suite primaria **286/286 PASS** en 8.193 s; replay limpio **286/286 PASS** en 8.119 s. La prueba nueva de wiring del intervalo en el mundo completo y Evaluator pasó. Payload y manifiesto se conservan en los artefactos del run y se registran en el README del harness.

**Corrección intermedia:** Run 825 falló con seis errores por omisión de los parámetros nuevos en la firma de `materialize_c10s_complete_world_from_dgp`. Se corrigió la firma y propagación; Run 826 valida esa corrección. La comparación de commits confirma que los dos commits posteriores al commit probado solo restauran el workflow manual y eliminan el centinela temporal; no alteran código ni tests.

**Alcance:** evidencia técnica de compilación, contratos de software y replay. No acredita calibración del intervalo, cobertura empírica, error tipo I, potencia, precisión útil ni identificación causal general. No hubo calibración, Monte Carlo ni experimento científico. La activación temporal quedó retirada; el workflow vuelve a ser manual y el centinela no existe.

## 328. Protocolo focal de calibración θ_A — scaffold N/M/R (2026-11-17)

**Implementación fuente añadida en research:** `03_EXPERIMENTS/C10-S/harness/theta_a_calibration_protocol.py`, con diez definiciones de regresión en `test_theta_a_calibration_protocol.py`. Se amplió el allowlist manual EP-02 a dieciséis módulos para incluir ambos archivos. El workflow sigue siendo manual-only y no se ha despachado.

### Contrato de replicación

- **N:** unidades de cada mundo sintético.
- **M:** mundos exteriores independientes, con identidades de mundo/roster, prefijo de unidad y semilla distintos.
- **R:** asignaciones repetidas dentro de un M fijo. El world_id, world_seed y configuración del mundo deben permanecer invariantes; cada R tiene run_id, salt de aleatorización conjunta y semilla S3 propios.
- El salt por R alimenta las dos etapas ya separadas por domain labels en el generador: asignación Bernoulli a g_A0/g_A1 y sorteo del vector conjunto dentro de la política seleccionada. El sorteo de vector permanece dentro del resultado estocástico del estimando.
- El flujo S3 se deriva separadamente por R y se expande por unidad. El capture boundary vuelve a comprobar el compromiso de seed del mundo y el hash del salt realmente usado; en el canal S3 de intervalo continuo verifica también cada observation_id contra la semilla de monitor por R/unidad. El muestreo puntual queda fuera de esta calibración de intervalos de confianza.
- Los fingerprints de configuración del mundo y del diseño q_X/g_A/r_common deben permanecer constantes dentro de M; los fingerprints de asignación, evidencia sellada y salida Analyzer deben variar entre R.
- Calibration y evaluation banks tienen namespaces separados y validación de disjunción de streams world/assignment/S3. El protocolo no reutiliza el seed bank ni las clases RUN/R de la matriz 13×52.

### Agregación y métricas

El capture/agregador queda fijado a `THETA_A_QX_GA_RCOMMON_VCONT` sobre `V_CONT` y exige que las identidades/versiones de estimando y outcome permanezcan constantes entre M. Calcula primero una contribución por mundo M a partir de sus R asignaciones, y después estima medias y MCSE entre M independientes. Incluye cobertura y anchura de intervalo, bias/MAE/RMSE, recuperación puntual solo con tolerancia explícita, disponibilidad de intervalo, identificación/abstención, abstención correcta, falsa identificación y falsa abstención. No elimina silenciosamente replicaciones incompletas: si falta cualquier contribución requerida, la métrica correspondiente es `NOT_EVALUABLE`.

La clasificación esperada de identificación es una entrada explícita del contrato de escenario, separada del Analyzer. Si el escenario debe abstenerse, cualquier estado Analyzer distinto de `IDENTIFIED` cuenta como abstención correcta y se conserva el subtipo observado. Se requiere una base explícita para declarar independencia entre unidades. En esos escenarios se conserva el confidence level solicitado aunque el Analyzer se abstenga por missingness o falta de soporte; la disponibilidad del intervalo se informa por separado y no se eliminan esas replicaciones. Los escenarios de verdad `PARTIALLY_IDENTIFIED` se rechazan por ahora porque P183-11 no dispone todavía de bounds de medición adjudicados. Type-I error y power quedan `NOT_DEFINED_NO_TEST_PROCEDURE`; no se infieren de un intervalo de confianza.

### Estado y límites

- **Implementación fuente:** presente en la rama research.
- **Pruebas:** diez definiciones añadidas al allowlist; **no compiladas ni ejecutadas**.
- **Workflow:** allowlist estáticamente ampliado; YAML/actionlint no validado y no despachado.
- **Calibración:** no ejecutada.
- **Seed banks:** no generados.
- **Diseño científico:** no se han seleccionado roster focal de escenarios, N, M, R, confidence level, MCSE targets, tolerancia de recuperación ni parámetros DGP. Los números usados por las fixtures unitarias son exclusivamente datos de prueba de software.
- **Identificación parcial:** no evaluable hasta resolver el uso adjudicativo de measurement bounds.
- **Type-I/power:** pendientes de un procedimiento de contraste separado.
- **Value contextual:** el protocolo sigue limitado a `θ_A(q_X*,r_common;V_cont)`; no cierra el puente V_cont→Outcome/Value general ni la contribución `ΔT_acc→Value`.

El siguiente paso dependiente de decisión es aportar un roster focal versionado con world/DGP/roster IDs y versiones, prefijo de unidad, truth-status independiente y base de independencia por escenario, además de objetivos MCSE explícitos. No se infieren del protocolo 13×52 ni de P178. La creación de este scaffold no autoriza la generación de bancos ni la calibración.

### Integración técnica del protocolo N/M/R con World Builder

Se extendió el fixture de `test_c10s_world_pipeline_integration.py` para aceptar cada `ThetaASeedAssignment` sin cambiar la semántica del DGP existente. El fixture ahora propaga al mundo la identidad/versión world, DGP y roster, el prefijo de unidades, N y la semilla de mundo; propaga a la asignación directa el salt propio de R, el run_id propio de R y al monitor S3 las semillas derivadas por unidad. Se añadió una regresión de integración que ejecuta en memoria el pipeline completo de la fixture para las cuatro filas de prueba N=32, M=2, R=2, captura Analyzer/Evaluator y comprueba la agregación por M.

Esta prueba usa exclusivamente parámetros de fixture para verificar interfaces y separación N/M/R. No selecciona el roster científico focal, no fija el dimensionamiento confirmatorio y no genera un banco persistido ni ejecuta calibración. El allowlist EP-02 conserva sus dieciséis módulos; la regresión se añade al módulo de integración ya incluido.

**Estado tras la integración:** fuente y regresión validadas técnicamente en EP-02 Run 828: compilación PASS, 297/297 pruebas PASS y replay limpio 297/297 PASS. La autorización puntual del usuario se consumió y quedó cerrada en el contrato de misión. No se habilitó calibración ni experimento científico.
`scientific_execution=false` · `execution_authorized=false` · `calibration_authorized=false`

No se modifica `main`, RMA, Evidence→Claim Matrix, STATUS o TGCV Core. PR #116 permanece Draft/no merged.
## 329. EP-02 — validación técnica del scaffold focal y World Builder (2026-11-18)

**Run 828 PASS:** GitHub Actions `44201023934`, commit probado `0139ff58864db455ab49ed8addd2fec28188a45c`. La compilación exacta del allowlist de dieciséis módulos pasó; la suite primaria completó **297/297 PASS (12.945 s)** y el replay desde una materialización limpia e idéntica completó **297/297 PASS (13.085 s)**. Pasaron también la equivalencia de árboles, los controles de bytecode y el nuevo test `test_theta_a_nmr_protocol_is_wired_through_complete_world_and_evaluator`.

**Defecto encontrado y corregido durante la validación:** Run 827 (`44200852299`) detectó ocho errores por sombreado de variable en `validate_theta_a_seed_banks`: la tupla de derivación de una fila sobrescribía el conjunto `expected` de claves N×M×R antes de comprobar cardinalidad. Se renombró la variable local a `expected_derivation`; Run 828 valida la corrección. No se ocultó ni se contabilizó Run 827 como PASS.

**Artefactos:** payload `14379769769`; manifiesto `14380508733`. **Estado de autorización:** la autorización puntual cubrió únicamente compilación, suite EP-02 y replay; quedó consumida. El workflow se restauró a `workflow_dispatch` manual-only. `calibration_authorized=false`, `scientific_execution=false`, `execution_authorized=false`.

**Alcance:** evidencia de integración de software y regresión reproducible. No acredita calibración estadística, cobertura, potencia, error tipo I, identificación causal ni contribución empírica de ΔT_acc a Value. No se generaron bancos de calibración/evaluación, no se ejecutó Monte Carlo ni experimento científico. No se modificó `main`, RMA, Evidence→Claim Matrix, STATUS ni TGCV Core.

## 330. Propuesta preliminar de dimensionamiento para calibración focal θ_A — NO CONGELADA (2026-11-18)

**Naturaleza:** propuesta de trabajo para discusión y sensibilidad; no constituye decisión científica, roster aprobado, diseño confirmatorio ni autorización de ejecución. Se incorpora en el maestro existente para evitar abrir un documento paralelo.

### Estado de partida y restricciones observadas

El protocolo `theta_a_calibration_protocol.py` ya implementa N unidades por mundo, M mundos exteriores independientes y R asignaciones dentro de cada mundo; exige M≥2 y R≥2, separa los streams de calibración/evaluación y calcula primero contribuciones por M antes de obtener MCSE entre mundos. Los objetivos MCSE son explícitos por escenario, N y métrica. La suite EP-02 Run 828 acredita la integración de software de este scaffold y del fixture World Builder; no acredita calibración estadística.

Los cuatro modos `positive`, `null`, `negative` y `alternative` presentes en `test_c10s_world_pipeline_integration.py` son modos de fixture de integración. Sus nombres no constituyen por sí mismos adjudicación de truth θ_A ni de estado de identificación. En particular, el caso `alternative` comparte configuración base con `positive` y añade una vía funcional alternativa/interacción; no se le asignará automáticamente una clase NOT_IDENTIFIED o PARTIALLY_IDENTIFIED. La clase debe salir de la verdad independiente del DGP y de los contratos de identificación vigentes. El protocolo actual rechaza truth PARTIALLY_IDENTIFIED hasta que existan bounds adjudicados; no debe forzarse esa clase para encajar el roster.

La métrica de Type-I error y la potencia siguen sin procedimiento de contraste definido. Un escenario con θ_A=0 no basta por sí solo para declarar Type-I error ni potencia.

### Roster focal propuesto — primera ola

1. **Identificado positivo:** efecto focal no nulo positivo, sin vía alternativa/directa incompatible con la identificación.
2. **Identificado nulo:** θ_A=0 por construcción, manteniendo las condiciones de identificación.
3. **Identificado negativo:** efecto focal no nulo negativo, manteniendo las condiciones de identificación.
4. **Vía alternativa/competidora:** el fixture `alternative` activa una vía funcional alternativa en el régimen común de ambas políticas g_A. La verdad reservada construida por el DGP es θ_A=0; el contrato de regresión ahora exige que Analyzer/Evaluator la clasifiquen como IDENTIFIED / POINT_RECOVERED, porque la vía alternativa común enmascara el contraste focal pero no elimina soporte ni identificación. Esta adjudicación está codificada como expectativa de test, todavía no ejecutada dinámicamente. No confundirla con un escenario de vía directa diferencial ni con no-identificación.

**Condición de entrada por escenario:** registrar la verdad analítica θ_A y expected_identification a partir del DGP/Evaluator independiente, y verificar que la manipulación cambia el mecanismo pretendido sin alterar inadvertidamente q_X*, r_common, soporte, versiones ni otras rutas. La clase esperada nunca se inferirá de la respuesta del Analyzer.

### Dimensionamiento exploratorio escalonado — candidato, no congelado

| Parámetro | Propuesta inicial | Motivo / regla de revisión |
|---|---:|---|
| N (unidades por mundo) | 32, 64, 128 | 32 reutiliza el tamaño del fixture actual; 64/128 permiten observar sensibilidad a N. La compatibilidad de N mayores debe verificarse técnicamente antes de construir bancos. |
| M (mundos exteriores) | 30 | Unidad independiente para MCSE; primera aproximación de piloto, no garantía de precisión. |
| R (asignaciones por mundo) | 20 | Reduce ruido de asignación dentro de cada mundo y permite estimar contribuciones por M; no sustituye aumentar M. |
| Confianza | 0,95 | Nivel explícito inicial coherente con la lectura del intervalo conservador; no se presenta como decisión confirmatoria. |
| Tolerancia de recuperación puntual | No fijada inicialmente | Mantener errores continuos (bias, MAE, RMSE); fijar tolerancia solo con justificación de escala/uso del estimando, no por conveniencia del resultado. |

El tamaño inicial sería 3 N × 30 M × 20 R = 1.800 ejecuciones por escenario y banco. Con los tres escenarios identificados serían 5.400 ejecuciones por banco; calibración y evaluación usarían bancos disjuntos y, por tanto, streams independientes. La vía alternativa solo añade coste después de su adjudicación. Este volumen es una propuesta de planificación, no una generación de seeds ni una ejecución.

**Regla adaptativa de coste:** comenzar con N=32/64/128, M=30, R=20 en calibración; ampliar primero M (por ejemplo a 60 y después 100) cuando el MCSE entre mundos no alcance el objetivo. Aumentar R si la variación entre asignaciones dentro de M domina la contribución por mundo. Aumentar N solo cuando el objetivo sea estudiar la dependencia del comportamiento del estimador respecto del tamaño de roster; no usar N como sustituto de M. Evaluación independiente se ejecutaría únicamente tras cerrar y congelar el diseño y obtener autorización específica.

### Objetivos MCSE propuestos para la primera ola

Para los escenarios identificados, objetivos iniciales de MCSE absoluto ≤0,02 para: bias puntual, MAE, RMSE, cobertura del intervalo y anchura media del intervalo. Para todos los escenarios, MCSE ≤0,02 para tasas de identificación y abstención. Para escenarios no identificados/indeterminados, MCSE ≤0,02 para abstención correcta y falsa identificación. Son objetivos de precisión Monte Carlo de las métricas, no umbrales de calidad científica del estimador ni tolerancias de error por unidad.

La cobertura y anchura solo son evaluables cuando el Analyzer entrega intervalos admisibles; las abstenciones y la falta de intervalos se mantienen en sus denominadores y se informan por separado. Cualquier contribución M/R requerida ausente conserva el estado NOT_EVALUABLE según el agregador actual. No se eliminarán réplicas incompletas mediante complete-case.

### Límites y decisiones aún abiertas

- El intervalo Hoeffding de dos etapas requiere certificación explícita de independencia por unidad, probabilidades correctas, pesos q_X fijos, observación completa y resultado acotado; el roster debe declarar y justificar esa base, no inferirla de seeds diferentes.
- La calibración focal actual se restringe a `THETA_A_QX_GA_RCOMMON_VCONT` sobre `V_CONT`. No demuestra el puente general V_cont→Outcome/Value contextual ni la contribución completa ΔT_acc→Value.
- Type-I error/potencia requieren un procedimiento de contraste separado y preespecificado; no se inventan a partir de cobertura.
- La clase de identificación del caso alternativo, los escenarios no identificados específicos, la tolerancia puntual, los valores finales de N/M/R y los objetivos MCSE permanecen abiertos.
- No se han construido bancos, ejecutado simulaciones, calculado resultados de precisión ni realizado calibración/evaluación científica.

**Estado:** PROPOSAL_ONLY / NOT_FROZEN / NOT_EXECUTED. Se mantienen `calibration_authorized=false`, `scientific_execution=false`, `execution_authorized=false`; no cambia la autorización vigente. PR #116 permanece Draft; `main`, RMA, Evidence→Claim Matrix, STATUS y TGCV Core no se modifican.

## 331. Adjudicación de verdad del fixture alternativo común — contrato de regresión (2026-11-18)

La inspección del DGP de `test_c10s_world_pipeline_integration.py` permite precisar el significado del modo `alternative`: ambos brazos g_A se evalúan bajo el mismo régimen con la segunda coordenada del vector activa; la regla alternativa deshabilita ENABLED en ambos, mientras la regla focal se aplica solo cuando esa coordenada está ausente. Por tanto, en el régimen común alternativo la verdad reservada focal es θ_A=0. La vía alternativa enmascara el efecto focal, pero al ser común a ambos brazos y mantenerse asignación/observación completas, no constituye por sí sola una violación de identificación.

Se añadió al test end-to-end existente una expectativa explícita: `alternative_result.analyzer_result.identification == IDENTIFIED`, truth del Evaluator igual a cero, adjudicación correcta y disposición `POINT_RECOVERED`. Se conserva la distinción respecto al ITT-Z de paquete, cuya verdad permanece −0,5.

**Estado de evidencia:** contrato de regresión añadido y persistido; no ejecutado. Es una adjudicación estática de la verdad del DGP y de la clase esperada, no un resultado observado del Analyzer. EP-02 Run 828 no cubre esta nueva aserción. Requiere autorización técnica para ejecutar la suite antes de elevarla a PASS.

**Roster preliminar resultante:** positivo identificado (+0,5); nulo identificado (0); negativo identificado (−0,5); alternativa común identificada nula (0, vía alternativa activa). Los valores son verdades analíticas del fixture existente, no estimaciones muestrales. No se ha añadido todavía un escenario con vía directa diferencial/no-identificación: debe reutilizarse un mecanismo existente y adjudicar su verdad reservada antes de incorporarlo, sin fabricar un nuevo DGP paralelo.

No se generan bancos, no se ejecutan simulaciones ni calibración; no se modifica autorización. Estado: SOURCE_CONTRACT_ADDED / NOT_EXECUTED.

## 332. Auditoría de la ruta integrada de no-identificación / abstención (2026-11-18)

Se inspeccionó el World Builder, el pipeline completo, el Analyzer y los tests de observación. Resultado:

1. El fixture completo actual genera una sola historia q_X (H0, masa 1), asignación g_A con probabilidad 0.5 por historia y roster de 32 unidades. La rama interval-level exige cobertura q_X y ambos brazos realizados; con monitor de missingness 0.0, el fixture base está construido para identificación, no para pérdida de soporte.
2. El pipeline completo sí dispone de una segunda ruta de medición point-S3: cuando no se pasan configs interval-monitor, exige `s3_configs_by_history_ref` y `s3_seeds_by_unit`, sella evidencia con `ThetaASealer` y el Analyzer clasifica point samples completos como `PARTIALLY_IDENTIFIED` (`STRICT_VCONT_NOT_OBSERVED_BY_POINT_SAMPLES`). Esto es una limitación de resolución temporal, no falta de positividad ni pérdida de soporte.
3. Los tests unitarios ya cubren `INDETERMINATE` por ausencia de brazo realizado y soporte q_X incompleto; no se ha encontrado todavía un fixture World Builder que produzca esas condiciones conservando un DGP coherente y un Evaluator que adjudique la abstención.
4. El fixture `alternative` común permanece identificado y nulo; no sirve como caso de no-identificación.

**Conclusión:** no debe etiquetarse la ruta point-S3 como falta de soporte, ni alterar probabilidades/roster a posteriori para forzar un brazo ausente. La siguiente implementación válida es reutilizar los kernels S3 puntuales ya definidos en `c10s_synthetic_components.py` y añadir una variante de observación point-S3 al fixture World Builder; su test debe comprobar `PARTIALLY_IDENTIFIED`, razón de abstención, bounds que contienen la truth reservada y adjudicación correcta del Evaluator. La ruta `INDETERMINATE` por falta de soporte queda como una línea distinta y requiere manipulación del soporte/assignment especificada en el DGP antes de implementarla.

No se han modificado Analyzer/Evaluator, no se han creado nuevos DGPs, no se han generado bancos ni ejecutado pruebas. Estado: SOURCE_AUDIT_COMPLETE / IMPLEMENTATION_PENDING / NOT_EXECUTED. La autorización científica y de calibración permanece desactivada.

## 333. Integración de observación puntual S3 en World Builder — contrato de abstención parcial (2026-11-18)

La regresión end-to-end de World Builder incorpora ahora una ruta alternativa de observación point-S3 mediante `S3ObservationConfig` y `S3SequenceKernelRow` existentes, con muestreo en t=0 solamente. Las historias latentes del DGP siguen completas y la verdad reservada del Evaluator permanece separada; la proyección puntual no revela continuidad estricta a nivel de intervalo.

El nuevo test exige: Analyzer `PARTIALLY_IDENTIFIED`; razón `STRICT_VCONT_NOT_OBSERVED_BY_POINT_SAMPLES`; ausencia de estimación puntual; bounds lógicos [-1,1]; y Evaluator `BOUNDS_COVER_TRUTH` para truth positiva conocida (+0,5). Esto prueba abstención por resolución de medición, no falta de positividad, soporte q_X ni brazo realizado.

Reutiliza el World Builder y los kernels S3 existentes; no introduce DGP ni estimando nuevo. Contrato fuente persistido, ejecución dinámica pendiente. No se han generado bancos ni ejecutado calibración o experimento científico. Estado: SOURCE_CONTRACT_ADDED / NOT_EXECUTED.


## 334. Integración de abstención por brazo realizado ausente en World Builder (2026-11-18)

Se amplía el fixture existente con un parámetro de tamaño de roster y un test point-S3 de N=1. La probabilidad de asignación sigue siendo p=0,5, por lo que la positividad estructural del mecanismo se conserva; con una única unidad, necesariamente falta uno de los dos brazos realizados.

El contrato exige Analyzer `INDETERMINATE`, razón `REALIZED_GA_ARM_SUPPORT_MISSING`, ausencia de estimación puntual, bounds [-1,1] y Evaluator `CORRECT_ABSTENTION` con truth reservada cubierta. Es una insuficiencia de soporte de brazos en el roster realizado, no una violación de positividad del mecanismo. Reutiliza el DGP/World Builder y el canal point-S3 existentes, sin introducir DGP o estimando nuevo.

Estado: SOURCE_CONTRACT_ADDED / NOT_EXECUTED. La suite no se ha ejecutado; no se han generado bancos ni realizado calibración o experimento científico.

## 335. EP-02 dynamic validation of integrated abstention paths — Run 829 (2026-11-18)

Run 829 (`44204384079`) executed the exact sixteen-module EP-02 software-contract suite against commit `e0c939b43601f140155666b5a9b6a022853b6bbd`. The primary run passed all 299 tests; the clean replay from an equivalent independent source materialization also passed all 299 tests. Both point-S3 partial-identification and one-unit realized-arm-absence World Builder regressions passed in both executions.

Preconditions and provenance checks also passed: CPython 3.12.10, hash-locked dependencies, compilation of the exact source/test allowlist, byte-identical primary/replay source trees, no residual bytecode caches, successful uploads of payload and execution manifest. Payload artifact ID `14383046746` (SHA-256 `c34eca732e75d3f3ba070f243aa48c0383ffc567ff9bfb533b35ece9d3beda03`); manifest artifact ID `14383560381` (SHA-256 `989a52821a4d0c07dbf36ab77b95bd13ff190dc5b239a321cbdca6f8e7fa925f`).

The temporary push trigger used only to start this previously authorized technical suite was removed; workflow `.github/workflows/c10-s-focal-harness-tests.yml` is restored to its original `workflow_dispatch`-only gate in commit `5df7961cd960f6fccdb02d3c3658dee095fc6683`. The tested source commit remains identifiable and immutable. This evidence is EP-02 software-contract evidence only: it does not constitute statistical calibration, confirmatory experiment execution, or a scientific claim about causal recovery. No banks or Monte Carlo calibration were generated. State: `PASS_STATIC + PASS_DYNAMIC_EP02 / 299+299 / REPLAY_PASS / SCIENTIFIC_EXECUTION_NOT_AUTHORIZED`.

## 336. Refinamiento del roster y precisión de la primera calibración focal — propuesta no congelada (2026-11-18)

Este refinamiento concreta la propuesta §330 utilizando exclusivamente los cuatro modos focales ya presentes en `test_c10s_world_pipeline_integration.py`. No crea DGP, estimando, test ID ni documento paralelo. La selección es una propuesta de primera ola para la calibración de software/DGP directo-g_A; no equivale a roster confirmatorio aprobado ni a evidencia de identificación fuera del mundo sintético especificado.

### 336.1 Roster candidato derivado de fixtures existentes

| Escenario propuesto | Fixture existente | Truth focal del DGP | Identificación esperada | Función |
|---|---|---:|---|---|
| `THETA_A_POSITIVE_V1` | `positive` | +0,5 | IDENTIFIED | Recuperación de efecto focal positivo |
| `THETA_A_NULL_V1` | `null` | 0 | IDENTIFIED | Recuperación del nulo bajo soporte |
| `THETA_A_NEGATIVE_V1` | `negative` | −0,5 | IDENTIFIED | Recuperación de efecto focal negativo |
| `THETA_A_ALTERNATIVE_COMMON_V1` | `alternative` | 0 | IDENTIFIED | Vía alternativa común a ambos brazos que enmascara el contraste focal sin retirar soporte |

Las cuatro verdades son potenciales reservados calculados por el DGP/Evaluator del fixture, no valores estimados. El ITT-D2 del paquete permanece separado (−0,5 en estos fixtures) y no se incorpora como truth de θ_A.

Los escenarios positivo y alternativo comparten el mundo/población basal de interacción, pero representan regímenes funcionales distintos. Se ha corregido estáticamente la identidad del fixture para que cada modo tenga un `functional_mechanism_id` diferenciado y el fingerprint de `r_common` refleje si la vía alternativa común está activa. Commit de fuente: `ab816910dc8e50d75be78f54af0b6e9d47de3cf4`. Las aserciones de separación de identidades se añadieron al test, pero este commit **no está cubierto por Run 829** y sigue NOT_EXECUTED.

### 336.2 Alcance real de la primera ola

El roster anterior cubre una distribución finita `q_X*` materializada dentro de cada mundo de fixture, con masas por unidad iguales a `1/N`, historia basal `H0` de soporte único y condiciones basales del fixture. Las políticas `g_A0/g_A1` son vectores conjuntos deterministas versionados por el fingerprint de la política; `r_common` se certifica dentro de cada par de potenciales.

Este es un benchmark mínimo de una sola clase de historia basal, no una validación de heterogeneidad entre múltiples clases `X/H0/C_c`, ni una certificación general de soporte para cualquier `q_X*`. Las unidades y masas son generadas por el mundo sintético; no son un roster empírico ni una población externa B1. La independencia por unidad debe seguir respaldada por el generador y el diseño de asignación, no por la mera separación de seeds.

La ruta point-S3 `PARTIALLY_IDENTIFIED` y el test N=1 `REALIZED_GA_ARM_SUPPORT_MISSING` son controles adversariales de software, no escenarios numéricos de esta primera calibración: el protocolo focal no admite truth PARTIALLY_IDENTIFIED y el N=1 está fuera del grid candidato. La falta de soporte de historias `q_X*` sigue siendo una condición distinta; no se simula retirando unidades ni se declara cubierta por el test N=1.

### 336.3 Dimensionamiento y objetivos de precisión propuestos

| Parámetro | Propuesta primera ola | Justificación / límite |
|---|---:|---|
| N | 32, 64, 128 | Grid permitido por el Generator (N≥16 y divisible por cuatro); 32 ancla en el fixture actual |
| M | 100 mundos exteriores | Unidad de agregación para MCSE; más conservador que el piloto M=30 de §330 |
| R | 20 asignaciones por mundo | Reduce ruido de asignación dentro de M; no sustituye aumentar M |
| Confianza | 0,95 | Nivel candidato explícito; no decisión confirmatoria |
| MCSE de bias, MAE, RMSE y anchura media | ≤0,02 | Precisión Monte Carlo absoluta propuesta para métricas continuas |
| MCSE de cobertura, identificación y tasas de abstención/falsa clasificación | ≤0,05 | Objetivo separado para métricas de tasa |

Con cuatro escenarios, tres valores N, M=100 y R=20, el presupuesto candidato es **24.000 ejecuciones por banco** (calibración; evaluación independiente solo tras freeze y autorización). Para una tasa binaria agregada por M, el límite de desviación estándar de una contribución acotada en [0,1] es 0,5; M=100 limita su MCSE máximo a 0,05. Exigir MCSE≤0,02 para todas las tasas requeriría hasta M=625 en el peor caso, antes de considerar cualquier refinamiento por la varianza observada. Por ello no se mantiene el objetivo uniforme de 0,02 de §330 para tasas binarias.

M=100 es un punto inicial de diseño, no garantía de que bias/MAE/RMSE alcancen MCSE≤0,02. Si el MCSE observado de una métrica continua supera el objetivo, M debe aumentarse mediante una extensión de calibración con derivación de seeds reproducible; no se aumenta R como sustituto de la independencia entre mundos. No se fijan todavía tolerancia de recuperación puntual, MDE, type-I error ni potencia: estos últimos requieren un test de hipótesis preespecificado.

### 336.4 Dictamen

La primera ola puede evaluar recuperación puntual e intervalar de θ_A en cuatro escenarios identificados de un benchmark directo-g_A, manteniendo separado el ITT-D2. No cubre todavía: una truth focal genuinamente NOT_IDENTIFIED, pérdida de soporte `q_X*` integrada, múltiples clases basales, interferencia, vías directas diferenciales no focales ni corrección de error S3. Esas limitaciones deben permanecer explícitas; no se rellenan con el escenario alternativo común, point-S3 ni N=1.

**Estado:** ROSTER_CANDIDATE / DIMENSIONING_CANDIDATE / NOT_FROZEN / NOT_EXECUTED. La propuesta §330 queda refinada en los puntos de roster y MCSE por este apartado; no se congelan valores ni se selecciona un banco. No se generan seeds/bancos, no se ejecuta calibración, Monte Carlo ni experimento científico. Se mantienen `calibration_authorized=false`, `scientific_execution=false`, `execution_authorized=false`.

## 337. EP-02 dynamic validation of focal-mechanism identity separation — Run 830 (2026-11-18)

Run 830 (`44206129607`) executed the exact sixteen-module EP-02 software-contract suite against commit `f307fea1e24c1dc17ad53e47914668707506b18f`, which includes the §336 fixture identity/fingerprint correction. Primary execution passed all 299 tests; clean replay from an equivalent independent source materialization also passed all 299 tests. The added assertions that the positive and common-alternative scenarios have distinct functional mechanism IDs and distinct `r_common` fingerprints passed in both executions.

Preconditions and provenance checks passed: CPython 3.12.10, hash-locked dependencies, compilation of the exact source/test allowlist, byte-identical primary/replay source trees, no residual bytecode caches, and successful payload/manifest uploads. Payload artifact ID `14381964999` (SHA-256 `66e5f84565f300f879ab448bcbc7298999dfda1108b7ef524136783d164aeef6`); manifest artifact ID `14383437476` (SHA-256 `4000883453cf7f1f89f17187418f43fbb8f36e8c2cb543e2294e9f97c1e2da32`).

The temporary push trigger was removed. Workflow `.github/workflows/c10-s-focal-harness-tests.yml` is restored to its original `workflow_dispatch`-only gate in commit `8451ea7c3c9e5f387c84e292099901e4ef436df3`. Run 830 is bound to the exact tested source commit; this subsequent workflow-restoration commit does not alter that tested source. This evidence establishes EP-02 software-contract behavior only, not calibration accuracy, statistical identification in general, or scientific causal recovery. No banks or Monte Carlo calibration were generated. State: `PASS_STATIC + PASS_DYNAMIC_EP02 / 299+299 / REPLAY_PASS / SCIENTIFIC_EXECUTION_NOT_AUTHORIZED`.

## 338. Auditoría estática del soporte estructural de q_X* para θ_A (2026-11-18)

### q_X* structural-support audit — static result (2026-11-18)

The current implementation distinguishes three different conditions, but does not yet instantiate the structural target-support failure required for a focal `theta_A(q_X*,g_A0,g_A1,r_common;V_cont)` non-identification scenario:

1. **Target-history evidence incompleteness:** `ThetaAObservationAnalyzer` reports `INDETERMINATE / TARGET_QX_SUPPORT_INCOMPLETE` when a positive-mass history in the declared q_X target is absent from sealed observations. This is evidence/observation incompleteness, not proof that the source DGP population cannot support the target history.
2. **Realized-arm absence:** it reports `INDETERMINATE / REALIZED_GA_ARM_SUPPORT_MISSING` when one policy arm has no realized units. The N=1 point-S3 regression tests this finite-sample event while preserving design probabilities p=0.5; it is not structural positivity failure.
3. **Structural assignment/policy support:** the current DGP constructors fail closed before Analyzer adjudication. `ThetaAPolicyAssignmentConfig.validate` requires 0<p(A=1|h)<1 for every q_X history; `generate_theta_a_policy_assignments` requires both g_A policies to cover q_X histories exactly and every policy vector to belong to `feasible_vectors_by_history[h]`. The truth constructor requires q_X to equal the exact world q_X and EventHistory potentials to cover the exact q_X × joint-policy support. Therefore an infeasible g_A on a positive-mass target history raises `ContractError` during construction; it does not produce a sealed nonidentified Analyzer case.

The existing 13×4 coverage matrix's `R0_SUPPORT_FAILURE` and `R2_SUPPORT_FAILURE_ZG_INTERACTION` rows adjudicate ITT-G and/or ITT-Z reference transportability, not focal theta_A; the matrix itself says theta_A is outside its assignment-contrast benchmark. The calibration unit test named `test_nonidentified_scenario_reports_correct_abstention` constructs synthetic `ThetaAReplicateRecord` values directly (including a fabricated NOT_IDENTIFIED observation) and tests summary arithmetic. It does not run World Builder → assignment → S3 → Analyzer → Evaluator under a structural q_X*/g_A support failure. It must not be cited as end-to-end non-identification evidence.

**Disposition:** the positive/negative/null/common-alternative first-wave roster remains an identified-support recovery benchmark only. Structural q_X*/g_A support-failure coverage is OPEN / NOT IMPLEMENTED END-TO-END. Do not relabel target-history observation incompleteness or N=1 realized-arm absence as that scenario. No new estimand, ledger, or test ID is created by this audit. Gate 130's restriction remains operative: no approved B1/UE target roster or materialization authorization is inferred from a synthetic fixture. A future test-only DGP case must make the target-vs-source support relation explicit, retain the full declared q_X target (no post-hoc trimming), and produce a provenance-bound NOT_IDENTIFIED adjudication without fabricating replicate records. That requires a narrowly scoped implementation/design decision before adding the case.

**Execution:** static source audit only. No code changes, calibration bank, Monte Carlo run, or scientific execution.

## 339. Contrato explícito de soporte estructural focal — primer paso de implementación (2026-11-18)

En la rama de investigación se ha añadido a theta_a_analyzer.py un contrato versionado y estrictamente sintético para separar, por cada historia de masa positiva en la distribución objetivo: masa objetivo, masa en la distribución fuente, definición de la intervención, factibilidad de ambas políticas focales y probabilidad declarada de asignación.

La adjudicación tiene alcance deliberadamente acotado:

- Intervención no definida o política focal estructuralmente inviable: ContractError. No se clasifica como NOT_IDENTIFIED, porque el contraste puede no estar definido.
- Intervención definida, ambas políticas factibles y alguna historia objetivo de masa positiva con masa fuente cero: NOT_IDENTIFIED / TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT.
- Soporte estructural completo: STRUCTURAL_SUPPORT_SUFFICIENT. Esto no acredita soporte de brazos realizados, integridad de observación ni identificación final.

Se han añadido cuatro pruebas unitarias de contrato para no solapamiento objetivo/fuente, soporte completo, intervención/política no admisible y positividad de asignación inválida.

**Límite esencial:** esta primera modificación aún no conecta el contrato con SyntheticWorldBundle, la generación de asignaciones, el sellado de evidencia, el resultado del Analyzer ni el Evaluator. Por tanto, no constituye el caso end-to-end de no identificación estructural y no cierra la brecha. Tampoco altera el roster, las decisiones Gate 130, el estimando ni las políticas confirmatorias.

**Estado:** CONTRATO Y PRUEBAS UNITARIAS AÑADIDOS / INTEGRACIÓN END-TO-END PENDIENTE / NO EJECUTADO. No se ejecutó EP-02 ni replay; no se generaron bancos, seeds, Monte Carlo ni ejecución científica. La autorización de ejecución sigue sin presumirse.
## 340. Separación de fingerprints q_X objetivo/fuente y adjudicación estructural en Analyzer (2026-11-18)

El contrato focal del Analyzer incorpora ahora fingerprints diferenciados: `q_x_sha256` identifica la distribución objetivo del estimando y `source_q_x_sha256` identifica la población fuente de asignación. El contrato de soporte estructural debe cubrir exactamente todas las historias y masas del q_X objetivo, y su fingerprint fuente debe coincidir con el q_X de asignación. Las observaciones selladas continúan vinculadas al fingerprint fuente.

Antes de la adjudicación de medición point/interval, el Analyzer valida el digest y la procedencia de la evidencia. Si la intervención está definida, ambas políticas son factibles y alguna historia objetivo de masa positiva carece de soporte fuente, devuelve `NOT_IDENTIFIED / TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT`, sin estimación puntual, con cotas lógicas [-1,1], masa objetivo soportada, historias sin soporte y fingerprint del contrato. La clasificación estructural precede a las limitaciones de observación o brazos realizados. Si el soporte estructural es completo, continúan las rutas existentes del Analyzer.

El pipeline completo actual declara explícitamente `source_q_x_sha256=assignments.q_x_sha256`, sin cambiar el caso legacy de soporte coincidente. **La separación aún no está integrada en World Builder, Generator, TruthBundle y Evaluator:** `SyntheticWorldBundle` mantiene el anclaje uno-a-uno entre roster y q_X; generación de asignaciones y potenciales exige ese mismo soporte; el Evaluator aún exige igualdad entre el fingerprint q_X de asignación y el del truth/contrato. Por tanto, el cambio no constituye el escenario end-to-end requerido ni permite declarar cerrada la brecha.

Se añadieron pruebas de fuente al módulo existente para la abstención estructural y la vinculación de fingerprints objetivo/fuente. No se ejecutó EP-02 ni replay; no se generaron bancos ni se realizó calibración o ejecución científica.

**Estado:** ANALYZER_STRUCTURAL_ADJUDICATION_SOURCE_IMPLEMENTED / TARGET_SOURCE_SEPARATION_PARTIAL / WORLD_GENERATOR_TRUTH_EVALUATOR_INTEGRATION_OPEN / NOT_DYNAMICALLY_VALIDATED.
## 341. Evaluator independiente: soporte estructural y semántica de propensión fuente (2026-11-18)

El Evaluator independiente deja de exigir que el fingerprint q_X del bundle de asignación coincida con el q_X objetivo del estimando. Comprueba ahora la verdad reservada contra el q_X objetivo, el bundle y las observaciones selladas contra el q_X fuente, el digest del contrato de soporte contra el resultado del Analyzer y la abstención exacta `NOT_IDENTIFIED / TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT`: sin estimación puntual, con cotas lógicas [-1,1] y lista íntegra de historias sin soporte. Después verifica que las cotas cubren la verdad objetivo reservada.

Se precisa además la semántica de la probabilidad de asignación en el contrato de soporte: si la masa fuente de una historia objetivo es positiva, debe declararse positividad estricta de ambos brazos; si la masa fuente es cero, la propensión fuente debe ser `None`, porque una probabilidad condicional de asignación no está definida en un estrato vacío. La intervención focal debe seguir estando definida y ambas políticas deben ser factibles en todas las historias objetivo de masa positiva.

Se añadió una prueba de fuente del Evaluator con q_X objetivo sobre h0/h1 y población fuente que solo contiene h0; la adjudicación esperada es `CORRECT_ABSTENTION`. Esta prueba sigue siendo una fixture de componente, no un mundo DGP generado. `SyntheticWorldBundle`, la generación de asignaciones y la construcción de verdad EventHistory continúan acoplados al mismo roster/q_X. El end-to-end real requiere una población sintética separada de potenciales de historias objetivo, factibilidad explícita de políticas sobre el objetivo completo y construcción de verdad que conserve historias objetivo sin unidades asignables en la fuente. No se infiere autorización de materialización B1/UE bajo Gate 130.

Los cambios son estáticos. No se ejecutó EP-02 ni replay; no hubo calibración, seed bank, Monte Carlo ni ejecución científica.

**Estado:** EVALUATOR_TARGET_SOURCE_CHECKS_IMPLEMENTED / WORLD_GENERATOR_TRUTH_DECOUPLING_OPEN / NOT_DYNAMICALLY_VALIDATED.
## 342. Desacoplamiento generado q_X objetivo/fuente y prueba estructural end-to-end (2026-11-18)

El pipeline focal `g_A` acepta ahora un `theta_a_q_x` objetivo separado del `SyntheticWorldBundle.q_x` fuente y un mapa uno-a-uno historia objetivo→identidad de unidad de potencial reservada. El roster `SyntheticWorldBundle` continúa siendo la población fuente de asignación. Las historias objetivo que no existen en la fuente reciben identidades sintéticas separadas y potenciales `EventHistory` generados por el DGP funcional; no se incorporan al roster ni a las asignaciones aleatorizadas.

Las políticas `g_A0/g_A1`, los vectores factibles y los certificados `r_common` cubren el soporte objetivo completo. La aleatorización continúa restringida a las unidades fuente. Los fingerprints de políticas/certificados se calculan sobre el soporte completo objetivo, mientras que el fingerprint q_X de asignación y evidencia identifica la población fuente. La verdad reservada `V_CONT` se calcula sobre el q_X objetivo completo mediante el mapa explícito de identidades de potencial.

El pipeline comprueba que los fingerprints del contrato de soporte coinciden con las distribuciones objetivo/fuente materializadas y que las masas fuente por historia reproducen el q_X fuente real. El Analyzer adjudica el no-solapamiento estructural antes de analizar la medición. El Evaluator verifica el sello del contrato, la evidencia y asignaciones fuente, la verdad reservada objetivo y la cobertura de las cotas de abstención; una comprobación de medición intervalar no desplaza la adjudicación estructural.

Se añade `test_structural_target_source_nonoverlap_runs_through_generated_world_to_evaluator`: mundo fuente de cuatro unidades, distribución objetivo de cinco historias con masa 0.5 fuera del soporte fuente, generación de potenciales reservados para la historia objetivo adicional, cuatro asignaciones fuente y evidencia intervalar sellada. Resultado exigido: `NOT_IDENTIFIED / TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT` en Analyzer y `CORRECT_ABSTENTION` en Evaluator con la verdad objetivo cubierta. Es una fixture sintética de contrato software, no un roster B1/UE aprobado ni una afirmación sobre una población científica.

**EP-02 Run 833:** PASS sobre commit `a14a93e5743ccd09c6396a9b67573563994add82`, GitHub Actions `44211416128`: compilación PASS; 307/307 pruebas primarias PASS (10.262 s); replay limpio 307/307 PASS (10.227 s) desde cierre de fuentes independiente e idéntico. Pasaron en ambos recorridos la nueva regresión end-to-end y la prueba del Evaluator independiente. Artefactos: payload `14386501382`, manifiesto `14385987836`.

El workflow fue restaurado a `workflow_dispatch` solamente en commit `dee4d4a8fce721f63a00d190e99f7896a508dc7c` (blob SHA `28471861a1c94038a11b5997a0b0e761b2659466`).

**Alcance:** evidencia de contrato software acotada; no valida calibración, MCSE, potencia, Type-I error, identificación científica ni contribución causal de accesibilidad. No se generó banco de calibración ni se ejecutó Monte Carlo o experimento científico. **Estado:** `PASS_STATIC + PASS_DYNAMIC_EP02 / 307+307 / REPLAY_PASS / STRUCTURAL_TARGET_SOURCE_ABSTENTION_PATH_TESTED / CALIBRATION_ROSTER_NOT_FROZEN`.
## 343. Materialización basal tipada de historias objetivo fuera de soporte fuente (2026-11-18)

Se introduce `SyntheticThetaATargetHistory` como contrato de materialización de harness para historias objetivo sintéticas sin unidad en el roster fuente. La fila vincula el `QXHistoryMass` exacto, una identidad de unidad potencial reservada y distinta, valores basales tipados (`X` vector numérico finito, `H0`, vector Booleano `C_c`), estado funcional inicial y referencia de procedencia sintética no vacía. Valida no alias con historias/unidades fuente, dimensiones X/C_c conformes al esquema DGP y validez del estado funcional.

El punto de entrada DGP exige materializaciones para todas y solo las historias objetivo externas al soporte fuente. Para historias con solapamiento, los anclajes X/H0/C_c deben reproducir los de la unidad fuente. El estado inicial entregado al generador EventHistory debe coincidir con el estado de la materialización tipada. Ausencia de materialización o dimensión X incompatible produce fallo cerrado. El contrato es exclusivamente de harness sintético: no crea ni autoriza un roster B1/UE.

**EP-02 Run 834:** GitHub Actions `44280284615`, commit probado `a92bbdc5b6f5a75e6c22d1e0c5a266185b5b106d`: compilación PASS; primaria 307/307 PASS (13.579 s); replay limpio 307/307 PASS (13.379 s). Payload `14416891006`, SHA-256 `d01bb844c4a91e25de8180031c25f860a975c27dc1b0972d6376fe298050691d`; manifiesto `14417325217`, SHA-256 `9656eebe7593761bb7df51edde0f7494c6355be4d171477077777b20f57eafe8`.

Workflow restaurado a `workflow_dispatch` únicamente; blob SHA `28471861a1c94038a11b5997a0b0e761b2659466`. Evidencia técnica acotada del contrato de materialización sintética; no constituye calibración científica ni autorización de población.
## 344. Cierre de dominio H0 para materialización basal objetivo — EP-02 Run 835 (2026-11-18)

Se refuerza `SyntheticThetaATargetHistory`: el valor tipado H0 de una historia objetivo externa debe pertenecer al soporte declarado en `SyntheticWorldConfig.h0_distribution`. Una etiqueta fuera del dominio falla cerrado. La regresión cubre además la omisión de materialización y la dimensión X incompatible.

**EP-02 Run 835:** GitHub Actions `44280725936`, commit `a9a2999309c32bba5cdc89901fdd45e1d9c24c3b`: compilación PASS; primaria 307/307 PASS (13.634 s); replay limpio 307/307 PASS (13.404 s). Payload `14416543657`, SHA-256 `953dbdbf545d2a91299fc8ec5f0620170c21468aa063e9fee9b2a59ca3d5cb6d`; manifiesto `14416238830`, SHA-256 `57f11616c56a626435cb79c11b2067ce40429389b9aa404406f02123042ae8ea`.

Workflow restaurado a activación manual `workflow_dispatch`; blob SHA `28471861a1c94038a11b5997a0b0e761b2659466`. Validación técnica acotada, sin calibración científica ni autorización de población.
## 345. Adjudicación separada de soporte fuente, positividad y factibilidad de intervención (2026-11-18)

Se precisa la adjudicación focal sin reabrir Gate 130 ni materializar objetos B1/UE:

- **Historia objetivo fuera del soporte fuente:** `NOT_IDENTIFIED / TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT`, con sus referencias separadas.
- **Historia objetivo con soporte fuente pero probabilidad de asignación focal 0 o 1:** `NOT_IDENTIFIED / SOURCE_ASSIGNMENT_POSITIVITY_FAILURE`, también con referencias separadas.
- **Intervención indefinida o política conjunta estructuralmente inviable:** `ContractError`; no es no-identificación estadística porque el contraste/intervención no está bien definido o no es aplicable.

Si concurren las dos primeras causas, el Analyzer conserva ambos tokens de razón y ambos conjuntos de historias. El Analyzer comprueba la propensión de cada observación sellada contra el contrato estructural; el Evaluator vuelve a comprobar la evidencia y el bundle de asignación contra el mismo contrato. La ausencia finita de un brazo realizado permanece `INDETERMINATE / REALIZED_GA_ARM_SUPPORT_MISSING`, distinta de la falta estructural de positividad.

El generador ejecutable de asignaciones mantiene positividad estricta; no se relaja el diseño de asignación. Los valores frontera se admiten únicamente en el contrato explícito de adjudicación del Analyzer para representar la causa de no identificación. La evaluabilidad de potenciales por Generator sigue siendo una condición separada.

Alcance: contrato software sintético; no crea ni autoriza roster q_X* B1/UE, pareja operativa g_A ni población científica. Sin cambio de estimando, objetivo causal ni decisión Gate 130. Estado de validación dinámica pendiente de EP-02/replay.