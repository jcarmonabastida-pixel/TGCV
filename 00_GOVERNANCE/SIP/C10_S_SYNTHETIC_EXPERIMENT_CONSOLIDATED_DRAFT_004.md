

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

El generador ejecutable de asignaciones mantiene positividad estricta por defecto. Los valores frontera se admiten exclusivamente cuando recibe un contrato explícito y validado de soporte estructural que vincula el fingerprint de q_X fuente, sus masas y las propensiones por historia con el mundo generado; el pipeline vincula además ese contrato al q_X* objetivo completo. Así, el fixture sintético de brazo determinista recorre la generación real de asignaciones, evidencia sellada, Analyzer y Evaluator, sin relajar escenarios ordinarios ni admitir configuraciones frontera no vinculadas. La evaluabilidad de potenciales por Generator sigue siendo una condición separada.

Alcance: contrato software sintético; no crea ni autoriza roster q_X* B1/UE, pareja operativa g_A ni población científica. Sin cambio de estimando, objetivo causal ni decisión Gate 130. Estado de validación dinámica pendiente de EP-02/replay.
## 346. Generación explícita del brazo sin soporte y concurrencia de fallos estructurales (2026-11-18)

Se integra el contrato de soporte estructural en `ThetaAPolicyAssignmentConfig.validate`, `generate_theta_a_policy_assignments`, `ThetaAPolicyAssignmentBundle.validate` y `materialize_c10s_complete_world_from_dgp`. La asignación con probabilidad focal frontera (0/1) continúa rechazada por defecto; solo se permite cuando el contrato estructural validado vincula fuente, masas y propensiones por historia con el mundo generado, y el pipeline lo vincula además con el q_X* objetivo. El brazo no soportado queda realmente sin asignaciones en esa historia; no se simula una etiqueta de abstención sobre un diseño ordinario.

Se añade una prueba de integración que recorre mundo DGP → asignación determinista focal en una historia fuente → EventHistory/S3 → evidencia sellada → Analyzer → Evaluator. La prueba de no solapamiento objetivo/fuente se amplía para concurrir con positividad fallida en otra historia, y comprueba que el Analyzer/Evaluator conservan ambas causas y ambos conjuntos de historias. Se mantiene además una prueba aislada de positividad fallida y las pruebas de rechazo de intervención indefinida o política inviable.

**Estado:** implementación y pruebas añadidas en la rama de investigación; validación estática pendiente de revisión completa y EP-02/replay. No se ha ejecutado calibración ni se ha congelado el roster. No cambia Gate 130 ni autoriza una población B1/UE.
**Intento EP-02 Run 837:** GitHub Actions `44283822323`, SHA `7cd08eb55db8e90f7e55e716fd7d9263cd2a0d2b`, terminó como `INFRASTRUCTURE_FAILURE / NOT_EXECUTED`: el checkout reintentó tres veces y no pudo conectar con `github.com:443`; compilación, suite y replay quedaron omitidos. No es un fallo de pruebas ni un PASS. El intento precede a los últimos cambios de generador, pipeline, validación del resultado y cobertura de causas concurrentes. No se ha iniciado un nuevo run.

## 347. Soporte fuente superset del soporte objetivo — regresión EP-02 Run 838 (2026-11-18)

Se corrige la condición de inclusión entre poblaciones: el soporte fuente puede contener historias que no pertenecen a q_X*. No se exige que cada historia fuente aparezca en el contrato objetivo. Se mantiene la cobertura íntegra de q_X* y la declaración/vinculación de propensiones frontera para las historias objetivo que sí pertenecen a la fuente. La corrección conserva la separación entre historias solo-fuente, solo-objetivo, positividad estructural fallida y políticas/intervenciones no factibles o indefinidas.

**EP-02 Run 838:** GitHub Actions `44322864147`; PASS. Commit probado `8e31a68633a38eb97514049a2deba978ff503034`, descendiente temporal del commit de código `12b55384ea6ca8db489bc8d16d0bf73cfbc4a823`, sin cambios de código fuente/harness entre ambos; el commit probado añadió únicamente el disparador temporal sentinel-scoped y el sentinel requerido para ejecutar el workflow autorizado. Compilación PASS; suite primaria 311/311 PASS (8.949 s); replay limpio 311/311 PASS (8.908 s), desde cierre de fuentes independiente e idéntico.

Artefactos: payload `14435077965`, SHA-256 ZIP `4f192dad5823519bb69f43f028513aa0819dd52674a7c616a6dcb9a9fd071152`; manifiesto `14434738650`, SHA-256 ZIP `ce2936be191b92ba2c8cb3f4e1002887c154d52b01edde960dea05ef5d1b2c38`. Run: https://github.com/jcarmonabastida-pixel/TGCV/actions/runs/44322864147.

Tras la ejecución, el sentinel temporal fue eliminado y el workflow restaurado al contenido original exclusivamente `workflow_dispatch`; blob SHA restaurado `28471861a1c94038a11b5997a0b0e761b2659466`. Commits de limpieza: restauración `bc91a72f37c50706132afa988e5a75cd9308c11c`, eliminación del sentinel `d6fcf80952ef88e83c92547bc529925a3ff1373c`.

**Alcance:** PASS técnico del contrato software de soporte fuente/objetivo y de la suite EP-02; no valida calibración, MCSE, potencia, Type-I error, identificación científica ni contribución causal a Value. No se generó banco ni se ejecutó calibración/experimento científico. El roster permanece sin congelar.


## 348. Reconciliación del roster de calibración tras la brecha de soporte estructural — revisión estática (2026-11-18)

### 348.1 Dictamen sobre el roster

El roster §336 de cuatro escenarios continúa siendo un benchmark candidato de recuperación bajo soporte identificado, pero ya no basta como cobertura de primera ola tras integrar el camino generado q_X objetivo/fuente. Se propone un quinto escenario candidato: `THETA_A_TARGET_SUPPORT_NONIDENTIFIED_V1`, basado en el modo DGP sintético de no solapamiento objetivo/fuente.

El escenario debe aislar una causa: mantener una historia objetivo de masa positiva fuera del soporte fuente, con ambas intervenciones focales definidas y factibles sobre todo q_X*, potenciales reservados materializados para todo el objetivo y positividad estricta de asignación en todas las historias objetivo que sí tienen soporte fuente. La adjudicación esperada es `NOT_IDENTIFIED / TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT`. No debe concurrir el fallo de positividad de asignación en este escenario de calibración; la fixture combinada de no solapamiento + positividad sigue siendo una regresión adversarial EP-02 separada.

La verdad reservada θ_A puede existir como contraste DGP sobre q_X* completo aunque no sea identificable desde la población fuente observada. El Analyzer debe abstenerse, sin estimación puntual. El Evaluator comprueba que la abstención y las cotas lógicas cubren esa verdad. Esta clase permite medir abstención correcta y falsa identificación; no permite evaluar bias/MAE/RMSE/recuperación puntual como si el estimando estuviera identificado.

### 348.2 Caso benigno adicional: fuente estrictamente mayor que objetivo

La corrección §347 permite historias fuente que no aparecen en q_X*. No se debe confundir con el caso de historia objetivo sin soporte. El caso fuente-superset/objetivo-subset debe tener un test generado propio: q_X* es subconjunto estricto del soporte fuente, todas las historias objetivo están soportadas y las propensiones focales son positivas. La expectativa es que las historias solo-fuente no causen abstención ni invaliden el contrato. La fixture actual de no solapamiento tiene historias objetivo adicionales y no demuestra por sí sola esta propiedad.

### 348.3 Brecha entre protocolo de agregación y roster ejecutable

El protocolo `theta_a_calibration_protocol.py` admite la clase `expected_identification=NOT_IDENTIFIED` y puede resumir `correct_abstention_rate` y `false_identification_rate`. Sin embargo, `ThetaACalibrationScenario` actualmente solo vincula identidad/versión, DGP/world/roster IDs y clase de identificación esperada. No vincula un perfil DGP tipado, el contrato de soporte estructural/versionado, la masa objetivo sin soporte, ni el token de razón de abstención esperado. El seed-bank builder produce identidades/semillas N×M×R, pero no parametriza ni ejecuta el DGP. No existe todavía un roster ejecutable de cinco escenarios ni un runner que capture resultados reales del pipeline para construir `ThetaAReplicateRecord`.

La prueba `test_nonidentified_scenario_reports_correct_abstention` alimenta directamente registros sintéticos fabricados al agregador; solo prueba aritmética de resumen. No demuestra generación, adjudicación ni evaluación end-to-end para cada réplica. Por ello el quinto escenario es un candidato metodológico, no un escenario de calibración implementado.

### 348.4 Revisión de dimensionamiento

Manteniendo provisionalmente N={32,64,128}, M=100 y R=20, el paso de cuatro a cinco escenarios elevaría el coste aritmético de 24.000 a **30.000 ejecuciones por banco** (5×3×100×20). Es un cálculo de capacidad, no un diseño congelado ni autorización para crear bancos. Para el escenario no identificado solo corresponden métricas de identificación/abstención, disponibilidad de intervalo y falsa identificación; métricas de recuperación puntual e intervalar de efecto identificado no aplican. El objetivo de MCSE de tasas binarias se mantiene en ≤0,05 como candidato: con M=100 el peor caso para una contribución acotada en [0,1] tiene MCSE 0,05. No se puede prometer ≤0,02 en todas las tasas sin elevar M potencialmente hasta 625 en el peor caso. Los objetivos de MCSE continuo ≤0,02 para escenarios identificados siguen siendo candidatos, sujetos a varianza observada y extensión reproducible de M. Type-I error/potencia siguen fuera del protocolo hasta definir un test separado.

### 348.5 Trabajo requerido antes de congelar

1. Crear una fixture end-to-end **aislada** de target-only structural support, con positividad estricta en el solapamiento, y verificar Analyzer `NOT_IDENTIFIED / TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT` + Evaluator `CORRECT_ABSTENTION` para la verdad reservada.
2. Crear la regresión generada source-superset/target-subset, verificando que historias solo-fuente no provocan abstención.
3. Extender `ThetaACalibrationScenario` con un perfil de escenario tipado/versionado que vincule la configuración DGP, soporte q_X objetivo/fuente, masa objetivo no soportada y razón de adjudicación esperada; incorporar esos valores a la identidad/fingerprint de escenario y a la derivación de seeds/manifiesto.
4. Construir un runner de calibración de software que, para cada N×M×R, ejecute la cadena completa y construya registros de réplica a partir de Analyzer/Evaluator reales, sin fabricar `ThetaAReplicateRecord`.
5. Probar el agregador con esos registros capturados y verificar que las métricas inaplicables se marcan `NOT_EVALUABLE`, no se fuerzan a cero ni se omiten mediante complete-case.

**Estado:** FIVE_SCENARIO_ROSTER_CANDIDATE / STRUCTURAL_NONIDENTIFICATION_CALIBRATION_PATH_NOT_IMPLEMENTED / SOURCE_SUPERSET_REGRESSION_OPEN / DIMENSIONING_CANDIDATE / NOT_FROZEN / NOT_EXECUTED. No se generaron bancos/seeds ni se ejecutó calibración, Monte Carlo o experimento científico. No cambia Gate 130, el estimando, las políticas ni la autorización vigente.


## 349. Fixtures aisladas de frontera de soporte añadidas — EP-02 pendiente (2026-11-18)

Se añadieron dos pruebas generadas end-to-end en `test_c10s_world_pipeline_integration.py`, sin alterar la prueba adversarial combinada existente:

- `test_target_only_support_without_assignment_failure_abstains_end_to_end`: historia target-only de masa positiva, políticas focales definidas y factibles, y positividad de asignación 0.5 estricta en todo el solapamiento objetivo/fuente. Resultado esperado: `NOT_IDENTIFIED / TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT`, ninguna historia con fallo de positividad de asignación y Evaluator `CORRECT_ABSTENTION`.
- `test_source_support_strict_superset_of_target_is_benign_end_to_end`: q_X objetivo es subconjunto estricto del soporte fuente generado; masas objetivo renormalizadas y masas fuente conservadas en el contrato. Se mantiene la asignación sobre el roster fuente completo, mientras la verdad focal se evalúa sobre q_X*. Resultado esperado: Analyzer identificado, cobertura objetivo 1.0, Evaluator `CORRECT_IDENTIFICATION`; la historia solo-fuente no debe causar abstención.

La segunda prueba conserva deliberadamente políticas, certificados y asignaciones sobre todo el mundo fuente: el generador de asignaciones requiere cobertura completa del soporte fuente aunque el estimando focal se evalúe en el subconjunto objetivo. Esto evita confundir roster de asignación fuente con población objetivo del estimando.

**Estado:** TESTS_AUTHORED / STATIC_REVIEW_ONLY / EP-02_NOT_RUN / REPLAY_NOT_RUN. Las pruebas aún no están compiladas ni ejecutadas. Requieren nueva autorización EP-02 + replay sobre el nuevo commit de tests. No se ejecutó calibración, no se creó banco de seeds y no se inició experimento científico.


## 350. Soporte fuente estrictamente mayor que q_X* y validación técnica integrada (2026-11-18)

Se cerró la brecha de compatibilidad entre roster fuente y población objetivo para el caso benigno fuente-superset/objetivo-subset, sin relajar las condiciones de soporte estructural sobre historias objetivo.

- El contrato de análisis conserva por separado los fingerprints de las políticas focales del bundle de asignación fuente y los fingerprints de las políticas definidas sobre la población objetivo. El Evaluator compara la verdad reservada con estos últimos; no confunde la identidad de las políticas fuente con la identidad del estimando objetivo.
- El contrato declara explícitamente `source_only_history_refs`, únicas y disjuntas del soporte q_X*. El Analyzer exige que las historias fuera de q_X* presentes en la evidencia coincidan exactamente con esa diferencia declarada; rechaza historias externas no declaradas.
- La generación y el sellado conservan el roster fuente completo, incluidas asignaciones y evidencia de unidades solo-fuente. El Analyzer filtra esas filas antes de calcular cobertura, recuentos por brazo, estimación e inferencia sobre q_X*. El Evaluator aplica los controles de verdad y agregación al subconjunto objetivo, sin exigir que las historias solo-fuente pertenezcan al contrato de soporte objetivo.
- Las propensiones de asignación del estimando y el contraste de positividad se auditan sobre las historias objetivo; las filas solo-fuente siguen sujetas a la validación de identidad/procedencia del bundle fuente. La fuente puede contener historias adicionales sin que eso cause abstención espuria.
- Se alinearon las regresiones con el contrato real del roster: el caso fuente-superset conserva las ocho asignaciones fuente; el caso con historia objetivo solo-fuente conserva las cuatro asignaciones de las cuatro unidades fuente. La historia target-only no se incorpora artificialmente al roster aleatorizado fuente.

**Validación EP-02:** Run 851 (`44335617915`), commit exacto `90c6512f2361c153d8de550ad6167c47ceb55f7f`, SUCCESS. Suite integrada de 16 módulos: 313/313 PASS en ejecución primaria y 313/313 PASS en replay limpio desde materialización equivalente. Incluye las regresiones source-superset, target-only sin fallo de positividad y no-solapamiento combinado con fallo de positividad. Payload artifact `14440773039` (SHA-256 `bf81186b49c55d86a5f6f7303f9dbb58a182b2bfcd6803df048574b2d387bbf3`); manifest artifact `14440308992` (SHA-256 `ad092a5bd230bf4d507476e47caf6fc7d58b8f0b9d600ae23b3018798aec1045`).

**Alcance y estado:** PASS_STATIC + PASS_EP02_TECHNICAL + PASS_CLEAN_REPLAY para los contratos de software cubiertos. No constituye evidencia de calibración científica, recuperación de parámetros causales ni validez empírica. No se generó banco, no se ejecutó Monte Carlo/calibración, no se congeló el roster y no se modificó main ni Gate 130. El roster de cinco escenarios sigue siendo candidato y NOT_FROZEN. La workflow temporal por push y su sentinel se han retirado; el workflow queda limitado a `workflow_dispatch` con confirmación explícita.


## 351. Reconciliación de captura de réplicas con soporte fuente/objetivo separado (2026-11-18)

La revisión del protocolo de calibración encontró una incompatibilidad latente: `capture_theta_a_replicate` exigía igualdad entre fingerprints q_X/g_A del bundle de asignación fuente y los de la verdad reservada, aunque el pipeline ya permite que el roster fuente y la población objetivo q_X* difieran. Esa condición impedía capturar réplicas de los escenarios source-superset/target-subset y target-superset/source-support-failure aun cuando Analyzer y Evaluator los adjudicaran correctamente.

Se corrigió la vinculación de procedencia en la captura:

- Bundle de asignación: q_X fuente, g_A fuente, r_common fuente y assignment mechanism se contrastan con los campos fuente del Analyzer contract.
- Verdad reservada: q_X objetivo y g_A0/g_A1 restringidas a q_X* se contrastan con q_X y target_g_A0/target_g_A1 del Analyzer contract.
- El fingerprint de diseño de política incorpora ambos lados (fuente y objetivo) y el fingerprint canónico del contrato de soporte estructural, evitando colapsar poblaciones distintas bajo una identidad común.
- Se añadieron regresiones unitarias: aceptación de un source-superset/target-subset correctamente vinculado y rechazo de una verdad que erróneamente use el fingerprint de q_X fuente en vez del objetivo.

**EP-02 Run 852:** `44337524579`, commit probado `9b10ae3235dae0c28837a45aa824858a2fb27a7c`, SUCCESS. Suite de 16 módulos: 315/315 PASS en primaria y 315/315 PASS en replay limpio. Payload artifact `14441238525`, digest ZIP `0d56ecf8ac014250400a999bbf9a78133465754e8630e59e790d4b9dcbbec6dc`; manifest artifact `14441468115`, digest ZIP `e1f7d5af43055d67d4ece0c7e835d628de55e40f025945febea13b1fc3a28491`.

**Alcance:** PASS técnico del contrato de captura y de la suite EP-02/replay. No valida el runner de calibración, el roster tipado, el rendimiento estadístico, MCSE observado ni la recuperación causal. No se generó banco de seeds ni se ejecutó Monte Carlo/calibración. La workflow temporal por push fue retirada y el workflow queda exclusivamente `workflow_dispatch` con confirmación explícita.


## 352. Perfil DGP tipado y adjudicación exacta de abstención en el protocolo θ_A — EP-02 Run 854 (2026-11-18)

Se cierra una parte de la brecha del protocolo de calibración identificada en §348.3–§348.5, sin congelar el roster ni iniciar calibración.

### 352.1 Contrato tipado y vínculo con el diseño

Se añade \`ThetaACalibrationDGPProfile\`, que vincula:
- identidad y versión del perfil sintético;
- fingerprints de q_X objetivo y población fuente;
- identidad y versión del contrato de soporte estructural;
- relación declarada entre soportes (igualdad, fuente estrictamente mayor o historias objetivo fuera del soporte fuente);
- referencias y masas de las historias objetivo no soportadas;
- token exacto de abstención esperado.

Los escenarios \`NOT_IDENTIFIED\` requieren un perfil tipado con causa esperada explícita. Su fingerprint canónico entra en la derivación de identidades/semillas N×M×R y queda registrado en cada \`ThetaASeedAssignment\`. La validación de semillas recalcula esa derivación, por lo que cambiar el perfil altera la identidad reproducible del diseño.

### 352.2 Captura y procedencia

\`capture_theta_a_replicate()\` contrasta el perfil con el contrato estructural realmente materializado: fingerprints fuente/objetivo, ID/versión del contrato, conjunto exacto de historias objetivo sin soporte y sus masas, relación source-only cuando corresponde y digest estructural reportado por Analyzer. El registro captura el fingerprint del perfil, la causa esperada, la causa observada y la masa objetivo no soportada.

Una causa observada distinta no se transforma en error de procedencia ni se oculta: se conserva para que la calibración mida la adjudicación incorrecta. Las incoherencias entre perfil y contrato materializado sí fallan cerradas.

### 352.3 Métricas de adjudicación

Para escenarios cuyo estado esperado es \`NOT_IDENTIFIED\`, el agregador separa:
- abstención correcta: Analyzer devuelve exactamente \`NOT_IDENTIFIED\` y el token observado coincide con la causa esperada;
- abstención por causa incorrecta: Analyzer devuelve \`NOT_IDENTIFIED\` o \`INDETERMINATE\` sin esa pareja exacta estado/causa;
- identificación parcial, como categoría independiente;
- falsa identificación, cuando Analyzer devuelve \`IDENTIFIED\`.

La regresión del protocolo fuerza las cuatro categorías y añade tanto un \`NOT_IDENTIFIED\` con token equivocado como un \`INDETERMINATE\` por ausencia finita de brazo. Ninguno se contabiliza como abstención estructural correcta. Se elimina así la regla anterior que consideraba cualquier resultado distinto de \`IDENTIFIED\` como éxito.

### 352.4 Validación técnica y límite de evidencia

**EP-02 Run 854:** GitHub Actions \`44340655791\`, commit probado \`2cb1f44f4f4c9aea1372d317359f039263dbf047\`; compilación PASS, 315/315 pruebas primarias PASS y 315/315 replay limpio PASS. Tiempos: 13.742 s y 13.694 s. Payload \`14443996431\` (SHA-256 \`ad041634ecb46af8b035b303ae7a91b2b4c6b1a7e58b74f77c5b83afe0d086e0\`); manifiesto \`14443816333\` (SHA-256 \`be3123bf7897020ac179cb845e8d23e43a5bdb2d3b60edd47ea616f8e1f355a8\`).

El workflow fue restaurado a \`workflow_dispatch\` con confirmación explícita; el sentinel temporal fue eliminado. Commits de restauración/eliminación: \`bb2eafe985e75637ed8942286fc4826809400858\` / \`b0506ce709d1171c03f2dda760c53a14f50d77fd\`.

**Límite:** Run 854 valida contratos de software, derivación de semillas y lógica de agregación. La regresión de agregación todavía utiliza registros deliberadamente construidos; no prueba que un runner haya ejecutado cada réplica real. Sigue pendiente construir y validar el runner que materialice cada mundo N×M y cada asignación R por la cadena DGP → asignación → S3/seal → Analyzer → Evaluator y capture el resultado real mediante \`capture_theta_a_replicate()\`. No se genera banco de calibración, no se ejecuta Monte Carlo ni calibración científica y el roster sigue \`NOT_FROZEN\`. No cambia Gate 130, el estimando ni las autorizaciones científicas.


## 353. Runner N×M×R, desacoplamiento no circular del perfil y captura end-to-end target-only — EP-02 Run 857 (2026-11-18)

Este apartado precisa y completa §352. El perfil DGP es estable entre mundos exteriores; los fingerprints q_X materializados varían por mundo y se registran en cada réplica, no se usan como insumos del propio generador de semillas del mundo.

### 353.1 Desacoplamiento de identidades y semillas

Se detectó una dependencia circular en la primera derivación: si el fingerprint del perfil incluyera los fingerprints q_X realizados y a su vez determinara la semilla que genera esos q_X, no existiría una especificación ex ante no circular del mundo.

La derivación queda separada:
- world_seed, world_id, roster_id y unit_id_prefix dependen de namespace, banco, escenario/versión, N y M;
- el fingerprint estable del perfil DGP entra en run_id, randomization_salt y s3_seed de cada R;
- cada ThetaAReplicateRecord conserva los fingerprints q_X objetivo/fuente realmente materializados y el digest del contrato estructural;
- el agregador exige que esos fingerprints permanezcan constantes entre las R del mismo mundo M.

El perfil tipado conserva la relación de soportes, las historias target-only y sus masas, la identidad/versión del contrato estructural y la causa esperada. La captura comprueba esa especificación contra el contrato y la adjudicación realmente materializados.

### 353.2 Runner con autorización explícita

Se añade run_theta_a_calibration_replicates(). Recibe un plan N×M×R ya declarado y un executor DGP específico del escenario; exige execution_authorized=True; requiere que el executor devuelva un C10SCompleteWorldResult; y construye cada registro exclusivamente mediante capture_theta_a_replicate(). No crea bancos ni semillas por sí mismo y falla cerrado si no hay autorización explícita.

La regresión positiva identificada del pipeline completo se conecta a este runner para ejecutar la orquestación N×M×R de prueba. La fixture target-only aislada también pasa por el pipeline real y ahora comprueba la captura de Analyzer/Evaluator: causa esperada y observada, masa no soportada, fingerprints q_X objetivo/fuente y digest del contrato estructural. El test del runner verifica además el rechazo sin autorización.

### 353.3 Validación y corrección intermedia

Run 855: intento fallido por una fixture unitaria obsoleta que seguía pasando fingerprints q_X realizados al constructor del perfil estable. El error fue TypeError de argumentos no admitidos; no se interpreta como fallo científico ni como PASS. La fixture se corrigió.

EP-02 Run 857: GitHub Actions 44342279770, commit probado 9303debb2f543a4d846729bb96b4a093805a9431; compilación PASS; 317/317 pruebas primarias PASS y 317/317 replay limpio PASS (9.135 s / 9.200 s). Payload 14443164296 (SHA-256 ab8879ae5349c15c32a52ecf5a028354a5bb97f2299bddb54d9217eb8b54bcd7); manifiesto 14443967494 (SHA-256 de74247560fa2a03b3077fa97b6acbc61a2b05b14d00a2d653ecf7dfa82417a3).

El workflow fue restaurado a workflow_dispatch con confirmación explícita y el sentinel eliminado. Commits de restauración/eliminación: c26a77671e4d7ad3771ffb78aa65afafdf1722c3 / 6db520d089dd4d21648979134d9d338840221525.

### 353.4 Límite y trabajo que permanece abierto

El runner y la captura end-to-end target-only tienen evidencia técnica acotada EP-02. El executor de escenario sigue siendo una fábrica DGP específica suministrada por el llamador: todavía falta consolidar la fábrica canónica/configuración tipada del roster de cinco escenarios y ejecutar el plan completo N×M×R del quinto escenario mediante ella. No se ha generado banco de calibración ni banco de evaluación; no se ha ejecutado Monte Carlo ni calibración científica; no se ha congelado el roster. No cambia Gate 130, el estimando ni las autorizaciones científicas.


## 354. Captura end-to-end del caso benigno source-superset/target-subset — EP-02 Run 858 (2026-11-18)

Se completa la validación de captura para ambas fronteras de soporte fuente/objetivo:
- **Target-only:** §353 ya comprueba que la historia objetivo positiva sin soporte fuente genera la causa estructural esperada, y que la captura conserva la masa no soportada, los fingerprints realizados y el digest contractual.
- **Source-superset:** la regresión benigna ahora usa un perfil DGP tipado y captura el resultado real de la cadena completa. La fuente conserva sus ocho unidades/asignaciones y la población objetivo excluye una historia source-only; el Analyzer permanece identificado y la historia excluida no causa abstención. El registro captura los fingerprints q_X fuente/objetivo, el digest del contrato estructural y masa objetivo no soportada igual a cero.

**EP-02 Run 858:** GitHub Actions 44342781242, commit probado bfd9d34389b8431056d3914a3e44c88e9ced27ff; compilación PASS; 317/317 pruebas primarias PASS y 317/317 replay limpio PASS (8.923 s / 8.951 s). Payload 14444242558 (SHA-256 9e03e6ad35c05a72cfbddfcd7e3ccbb1662f3fb98598fa52da9288e578d988dd); manifiesto 14443598826 (SHA-256 f86670f93fb7d6ae9a078c596012927e85146dbc895d1073265fe67820fae441).

Workflow restaurado a workflow_dispatch con confirmación explícita y sentinel eliminado. Commits de restauración/eliminación: 5675b681ccadabfac73712d760d2403dd1713c8c / eb1d7ccaf93c1bf7c8c0cbbffb40392bc2155859.

**Alcance:** evidencia de contrato software y captura para ambos sentidos de diferencia de soporte. No acredita todavía una fábrica canónica de los cinco escenarios ni la ejecución completa N×M×R del quinto escenario a través de dicha fábrica. No se generó banco de calibración/evaluación, no se ejecutó Monte Carlo ni calibración científica, y el roster permanece NOT_FROZEN.


## 355. Fábrica DGP tipada para los cinco escenarios candidatos y mundos basales emparejados — implementación estática (2026-11-18)

Se implementa la siguiente capa de configuración/materialización reutilizando el roster candidato de §336 y su quinto escenario añadido en §348. No se crea un roster nuevo ni se congelan sus parámetros.

### 355.1 Roster candidato tipado

`build_theta_a_candidate_scenario_roster()` en `theta_a_calibration_protocol.py` devuelve exactamente cinco contratos:

| Escenario | Variante del generador | Truth analítica declarada | Identificación esperada |
|---|---|---:|---|
| `THETA_A_POSITIVE_V1` | positive | +0,5 | IDENTIFIED |
| `THETA_A_NULL_V1` | null | 0 | IDENTIFIED |
| `THETA_A_NEGATIVE_V1` | negative | −0,5 | IDENTIFIED |
| `THETA_A_ALTERNATIVE_COMMON_V1` | alternative | 0 | IDENTIFIED |
| `THETA_A_TARGET_SUPPORT_NONIDENTIFIED_V1` | positive + target-only | No se predeclara; la calcula el Evaluator reservado | NOT_IDENTIFIED |

El quinto perfil mantiene la masa target-only candidata de 0,5 y la causa exacta `TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT`. Su truth numérica no se fija artificialmente: la verdad reservada se materializa y registra desde el Evaluator. El perfil tipado vincula variante del generador, relación de soportes, contrato estructural, masas y causa esperada; el fingerprint del perfil participa en la identidad reproducible del escenario.

La regresión source-superset/target-subset sigue siendo un control benigno separado y no se convierte en un sexto escenario focal.

### 355.2 Fábrica DGP reutilizable y cadena completa

Se extraen los constructores existentes de la fixture de integración a `theta_a_calibration_dgp.py::ThetaACalibrationDGPFactory`. La fábrica acepta una asignación de semilla y un escenario declarado; materializa el mundo basal, D2, potenciales estructurales, Reach/trajectory, EventHistory funcional, observación S3, sellado, Analyzer y Evaluator. Para soporte igual crea el contrato estructural igual; para target-only materializa la historia objetivo tipada, sus políticas factibles, r_common y soporte estructural, sin incorporarla al roster fuente aleatorizado.

El runner existente `run_theta_a_calibration_replicates()` puede consumir ahora esta fábrica como executor común para los cinco escenarios y capturar cada resultado mediante `capture_theta_a_replicate()`. La captura contrasta las cuatro truths analíticas ya establecidas en §336 con el Evaluator; en el quinto escenario registra la truth independiente sin imponer un valor numérico no establecido por el contrato histórico.

### 355.3 Identidad de mundo basal compartido y streams separados

§336 establece que positivo y alternativa común comparten mundo/población basal; §348 añade target-only sobre la misma base positiva. La derivación anterior usaba scenario ID para generar también la identidad del mundo, por lo que no podía cumplir esa relación al pasar a N×M×R.

Se separan ahora:
- **Identidad basal:** `world_family_id`, N y M determinan `world_seed`, `world_id`, `roster_id` y `unit_id_prefix`. Positivo, alternativa común y target-only comparten `THETA_A_INTERACTION_BASE_V1`.
- **Identidad de escenario/R:** scenario ID/versión, fingerprint DGP y R determinan `run_id`, `randomization_salt` y `s3_seed`, que permanecen distintos entre escenarios y réplicas.

El cambio de semántica de derivación queda versionado como `TGCV-C10S-THETA-A-SEED-v2`. `ThetaASeedAssignment` conserva `world_family_id`; la validación comprueba identidad idéntica dentro de cada familia×N×M, distinción entre familias/M y unicidad de streams de asignación/S3. Los bancos de calibración y evaluación siguen separados por namespace de banco.

### 355.4 Métricas inaplicables y pruebas de integración

Cada registro de captura conserva además los tres resultados independientes del Evaluator: truth dentro de bounds, adjudicación correcta y disposition; el resumen agrega por separado las tasas de bounds y adjudicación. El agregador materializa como `NOT_EVALUABLE` las métricas propias de escenarios identificados que no aplican a `NOT_IDENTIFIED`: false-abstention, bias, MAE, RMSE, point-recovery, interval coverage y interval width. No se imputan ceros ni se omiten por complete-case. La disponibilidad de intervalos, la abstención correcta, la causa incorrecta, la identificación parcial y la falsa identificación conservan sus métricas diferenciadas.

Se añaden regresiones para: roster tipado de cinco escenarios; mundos compartidos con streams por escenario separados; captura target-only a través de la cadena real; ejecución de software N×M×R de los cinco escenarios mediante la fábrica; y métricas identificadas-only `NOT_EVALUABLE`.

### 355.5 Estado y límites

**Estado:** IMPLEMENTED / STATIC_REVIEW_ONLY / NOT_EXECUTED / ROSTER_NOT_FROZEN. La prueba N=32, M=2, R=2 es una fixture de regresión de software, no una propuesta de dimensionamiento ni una calibración. Las pruebas nuevas no se han compilado ni ejecutado: la autorización puntual de tests técnicos está consumida y no se ha solicitado otra. No se generaron seeds/bancos, no se invocó el runner, no se ejecutó calibración, evaluación, Monte Carlo ni experimento científico. Los valores N/M/R, objetivos MCSE, tolerancias, type-I error/potencia y el freeze del roster siguen abiertos conforme a §330/§336/§348. No se modifica Gate 130, el estimando, las decisiones científicas ni el estado de autorización. **Incidente operativo de rama:** durante la creación inicial de `theta_a_calibration_dgp.py` se omitió el argumento `branch` en una llamada GitHub y el archivo se creó brevemente en `main`; se eliminó inmediatamente. La comparación del `main` actual contra su SHA previo al incidente (`c48e5ad9b5d08c2e08c2fe3b4a4c71317827f3d8`) devuelve dos commits add/delete y cero archivos en la diferencia neta; el archivo no existe en el árbol actual de `main` y sí existe únicamente en la rama research. El árbol de contenido canónico quedó restaurado, pero el historial de commits de `main` sí registra ambos commits y no se afirma que la rama haya permanecido sin escrituras.


## 356. Reautorización técnica EP-02 para validar la fábrica DGP de cinco escenarios (2026-11-18)

La autorización técnica puntual anterior constaba como consumida (§329 y registros posteriores). El usuario ha concedido una nueva autorización explícita, limitada a la compilación, suite técnica EP-02 de dieciséis módulos y replay limpio del workflow manual. No cubre bancos de calibración/evaluación, runner de calibración, Monte Carlo ni ejecución científica.

Antes del dispatch se corrigió el source closure del workflow para incorporar `theta_a_calibration_dgp.py` en materialización primaria/replay, compilación y manifiesto. Commit: `40e1dcf2414de4285d79b777b30aa6fbd027cc8d`. La suite aún no se ha lanzado. El estado de ejecución permanece pendiente; el roster no se congela y `calibration_authorized=false`, `scientific_execution=false`.


## 357. Revisión estática de adecuación estadística del diseño focal N×M×R — posterior a EP-02 Run 862 (2026-11-18)

**Estado:** STATIC_REVIEW_COMPLETED / DESIGN_NOT_FROZEN / CALIBRATION_NOT_AUTHORIZED / SCIENTIFIC_EXECUTION_NOT_AUTHORIZED.  
**Ámbito:** benchmark focal de recuperación de `θ_A(q_X*,g_A0,g_A1,r_common;V_cont)` con la fábrica DGP de cinco escenarios.  
**No modifica:** estimando, verdades DGP, roster candidato, Analyzer, Evaluator, tolerancias existentes ni autorizaciones.

### 357.1 Cierre técnico EP-02 y precedencia documental

El registro operativo más reciente está en `03_EXPERIMENTS/C10-S/harness/README.md`: EP-02 Run 862, workflow `44351884258`, commit probado `cdd43c87c6dab61a9521ac78fa4f07109e177e7f`; compilación PASS, 319/319 pruebas primarias PASS y 319/319 replay limpio PASS; materializaciones primaria/replay idénticas. El workflow volvió a `workflow_dispatch` y el centinela temporal fue eliminado. Esto valida la suite de contratos software, incluida la fábrica de cinco escenarios y las expectativas corregidas del Evaluator.

La descripción pendiente de dispatch en §356 corresponde al estado anterior al Run 862 y queda supersedida por este registro posterior, sin reescribir el antecedente. Run 862 no generó bancos, no ejecutó el runner N×M×R, no realizó calibración ni Monte Carlo y no constituye evidencia de recuperación causal.

### 357.2 Identidad del diseño que se está revisando

Se distingue el protocolo focal `theta_a_calibration_protocol.py` del benchmark V_cont anterior de 13 escenarios × 4 estimandos. Para este protocolo focal:

- **N:** unidades independientes dentro de cada mundo sintético.
- **M:** mundos exteriores independientes, con semilla y world_id distintos.
- **R:** asignaciones conjuntas repetidas dentro de cada mundo M; el world_id y la verdad focal permanecen fijos y cambian los streams de asignación y observación.
- Cada banco contiene exactamente escenario × N × M × R registros. No se añade un RUN separado al R de este protocolo focal; la obligación de un RUN designado más R repeticiones del Gate 154 pertenece al contrato anterior y no debe importarse a este diseño.

La propuesta de §336, extendida en §348 y materializada estáticamente en §355, es N={32,64,128}, M=100, R=20, cinco escenarios: cuatro identificados (verdades +0,5; 0; −0,5; 0 con alternativa común) y uno estructuralmente no identificado por masa objetivo fuera del soporte fuente. El coste es 5 × 3 × 100 × 20 = **30.000 ejecuciones completas por banco**. Positivo, alternativa común y target-only comparten identidad de mundo basal por familia; null y negative tienen familias propias. El fixture N=32, M=2, R=2 probado en EP-02 es una regresión de software, no una calibración ni validación del dimensionamiento.

### 357.3 Dictamen sobre N, M y R

**N — insuficientemente justificado para inferencia/precisión del estimador.** El grid 32/64/128 es una cuadrícula piloto permitida por el Generator, pero no se deriva de un MDE, una anchura máxima de intervalo ni una potencia requerida. La regla de selección descrita en el protocolo de calibración se basa en MCSE de métricas de rendimiento; un MCSE pequeño de bias/MAE/RMSE no implica que esos errores sean pequeños. N debe satisfacer por separado criterios de rendimiento del estimador y criterios de precisión Monte Carlo de las métricas.

El Analyzer utiliza un intervalo conservador Hoeffding para el contraste HT de dos etapas. Bajo el fixture actual —q_X uniforme (1/N), asignación 0,5, resultado unitario acotado en [0,1], independencia entre unidades y sin intervalos ausentes— la suma de cuadrados de rangos es 16/N y el radio bilateral al 95% es:

`r_N = sqrt(8 × ln(40) / N) ≈ sqrt(29,511 / N)`.

| N | Radio aproximado | Anchura total aproximada |
|---:|---:|---:|
| 32 | 0,961 | 1,922 |
| 64 | 0,679 | 1,359 |
| 128 | 0,480 | 0,961 |
| 512 | 0,240 | 0,480 |

Por tanto, con N=32 y N=64 el radio conservador supera la magnitud focal 0,5; con N=128 apenas queda por debajo. Incluso con estimación puntual exactamente igual a 0,5, N=128 deja un margen muy estrecho para excluir cero. Esto no invalida el intervalo ni prueba falta de cobertura: muestra que el grid propuesto no demuestra por sí mismo precisión inferencial o potencia útil. N=512 aparece aquí solo como referencia matemática para un radio ≤0,25, no como decisión de dimensionamiento.

**M — razonable como candidato para tasas con objetivo 0,05; insuficiente para prometer 0,02 en el peor caso.** Si cada mundo aporta una contribución binaria en [0,1], el MCSE máximo es 0,5/sqrt(M). Con M=100 es 0,05; para garantizar ≤0,02 en el peor caso se necesitaría M≥625. Para métricas continuas, el M requerido depende de la desviación estándar de las contribuciones por mundo y debe estimarse en calibración. El valor M=100 no garantiza MCSE≤0,02.

**R — candidato sin dimensionamiento demostrado.** R=20 reduce el ruido de asignación dentro de cada mundo, pero no sustituye M ni crea mundos independientes. El resumen actual calcula primero una contribución por mundo promediando R y luego el MCSE entre M. No informa por separado la variación entre mundos y la variación dentro del mundo entre asignaciones. Sin esa descomposición no se puede justificar que R=20 sea suficiente ni saber si el coste adicional debe dirigirse a R o a M.

En la fábrica actual, el stream S3 cambia por R, pero el monitor continuo está configurado como benchmark ideal (`missing_probability=0.0`) y sin error de detección. En consecuencia, la primera ola evalúa el mejor caso de observación; no valida robustez frente a medición imperfecta o ausencia.

### 357.4 Adecuación de las métricas y problemas de interpretación

1. **Recuperación puntual:** bias, MAE y RMSE son métricas apropiadas y deben conservarse junto con las distribuciones por mundo. La tolerancia 0,25 usada por el Evaluator es actualmente una regla de adjudicación del harness, no un umbral científico de recuperación. `point_recovery_tolerance` sigue sin decisión científica y no debe heredarse de la prueba de integración.

2. **Tolerancias no enlazadas:** `ThetaACalibrationDesign.point_recovery_tolerance` y la tolerancia que recibe el Evaluator no quedan ligadas en el registro `ThetaAReplicateRecord`; este no conserva el valor de tolerancia utilizado. Si ambos valores difieren, `point_recovery_rate` y `evaluator_correct_adjudication_rate` pueden medir reglas distintas. Antes del freeze debe existir una identidad única/versionada de criterio o dos métricas explícitamente diferenciadas.

3. **Adjudicación no equivale a recuperación y hay una métrica tautológica:** `evaluator_truth_within_bounds_rate`, `evaluator_correct_adjudication_rate`, identificación y recuperación puntual son resultados distintos. El Evaluator compara los límites lógicos [-1,1], mientras que la verdad focal está contractualmente restringida a [-1,1]; por ello, `evaluator_truth_within_bounds_rate` será 1 para toda verdad válida y funciona como invariante de dominio, no como métrica discriminante de rendimiento. Además, para `IDENTIFIED`, `correct_adjudication` exige cobertura y error puntual ≤ tolerancia; para `NOT_IDENTIFIED/INDETERMINATE`, exige cobertura de límites. Dado que esos límites son [-1,1], la segunda rama no mide por sí sola la corrección de la abstención ni su causa. La tasa `evaluator_correct_adjudication_rate` mezcla, por tanto, recuperación puntual en escenarios identificados y cobertura lógica en escenarios no identificados; no debe compararse ni agregarse como una tasa homogénea entre clases. Mantener por separado disposition, estado/cause de identificación, error puntual y cobertura inferencial Hoeffding.

4. **Abstención agregada:** `abstention_rate = 1 - identification_rate` agrupa `NOT_IDENTIFIED`, `INDETERMINATE` y `PARTIALLY_IDENTIFIED`. Se requieren tasas separadas para cada estado y para sus causas. En el escenario target-only deben distinguirse abstención correcta por la causa prevista, abstención por causa incorrecta, indeterminación, identificación parcial y falsa identificación.

5. **Métricas continuas condicionadas:** si cualquier R de un mundo identificado se abstiene, el agregador marca como no evaluables las contribuciones numéricas de ese mundo; si ocurre en cualquier M, la métrica continua completa queda `NOT_EVALUABLE`. Este comportamiento evita el complete-case silencioso, pero puede ocultar la precisión condicional de las estimaciones que sí se produjeron. El informe debe conservar dos planos: rendimiento numérico entre resultados identificados con denominadores explícitos y rendimiento operacional del procedimiento sobre todos los M×R (abstención, indeterminación, falsa identificación y causas). La primera tasa debe etiquetarse como condicional y no reemplazar la segunda.

6. **Escenario no identificado:** bias, MAE, RMSE, recuperación puntual y cobertura inferencial de un efecto identificado deben ser `NOT_EVALUABLE`, no cero. Sí son evaluables la abstención correcta, falsa identificación, causa, cobertura de límites y adjudicación independiente. La separación implementada en §355 es adecuada y debe preservarse.

7. **Inferencia:** cobertura y anchura de intervalos son necesarias, pero no sustituyen una prueba de hipótesis. Type-I error y potencia continúan correctamente como `NOT_DEFINED_NO_TEST_PROCEDURE`. Si se desea una decisión confirmatoria, deben preespecificarse contraste, nulo, alternativas, alfa, MDE y potencia objetivo; los escenarios +0,5/0/−0,5 no describen por sí solos la curva de potencia para efectos pequeños.

8. **Targets de MCSE:** el contrato admite una lista vacía o parcial de `metric_targets`; por tanto, antes de calibrar debe exigirse cobertura completa de todas las métricas/escenarios/N que se declaren obligatorios. Las métricas sin target deben seguir como `NOT_TARGETED`, nunca presentarse como PASS.

### 357.5 Dictamen y trabajo mínimo antes de Design Freeze

**Dictamen:** la arquitectura N×M×R y la separación de bancos son conceptualmente coherentes para una calibración anidada de mundos y asignaciones. El dimensionamiento N={32,64,128}, M=100, R=20 es todavía una propuesta de capacidad, no una elección estadísticamente justificada. La primera ola solo cubre un historial basal, políticas conjuntas deterministas, independencia por unidad y medición S3 ideal; el quinto escenario prueba una causa estructural concreta de no identificación, no todas las causas adversariales.

Antes de congelar:

- definir si el objetivo es recuperación descriptiva, inferencia confirmatoria o ambos; fijar por separado criterios de error del estimador y MCSE de las métricas;
- justificar N mediante MDE/precisión inferencial y revisar el grid a la luz de la anchura Hoeffding; no asumir que el MCSE de bias/MAE/RMSE selecciona N suficiente;
- estimar en una calibración piloto la varianza entre mundos y dentro de mundo, y dimensionar M y R con una regla reproducible y conservadora que incorpore incertidumbre de esas varianzas;
- fijar targets por escenario × N × métrica, exigir cobertura completa de targets obligatorios y mantener calibración/evaluación disjuntas;
- separar estados de identificación, indeterminación, abstención y recuperación; conservar denominadores totales y condicionales;
- versionar y alinear la tolerancia del Evaluator con cualquier métrica de recuperación que la use;
- mantener explícito que la primera ola es un benchmark ideal. La extensión a error/ausencia S3, heterogeneidad de historias, vías directas diferenciales e interferencia requiere escenarios separados y no debe darse por cubierta por esta calibración.

**Siguiente operación recomendada:** cerrar documentalmente la especificación estadística (estimandos de rendimiento, targets, regla de dimensionamiento M/R, criterios de N y contrato de métricas) antes de generar el banco de calibración. La calibración, el banco de evaluación, Monte Carlo y la ejecución científica siguen sin autorización. No se modificó código, no se generaron seeds y no se ejecutó ningún runner.


## 358. Auditoría del estimando de rendimiento y del agregador anidado M×R — revisión estática (2026-11-18)

**Estado:** AGGREGATION_AUDIT_COMPLETED / METRIC_CONTRACT_OPEN / DESIGN_NOT_FROZEN / CALIBRATION_NOT_AUTHORIZED.  
**Fuente ejecutable inspeccionada:** `03_EXPERIMENTS/C10-S/harness/theta_a_calibration_protocol.py`, blob SHA-256 Git blob `9675b9f6805b11f1a1037a3e4b2f95af53038e4c`; Analyzer `theta_a_analyzer.py` inspeccionado en la misma rama.  
**Ámbito:** interpretación de las contribuciones por mundo y métricas del protocolo focal de cinco escenarios; no se importan las obligaciones RUN+R ni las 52 claves del benchmark V_cont anterior.

### 358.1 Dictamen sobre la jerarquía M×R

El agregador implementa correctamente la estructura básica para métricas con contribución definida en cada réplica:

1. valida exactamente una observación por cada clave del plan escenario × N × M × R;
2. verifica que R comparte world_id, configuración, diseño de políticas, perfil DGP, soporte, estimando y truth;
3. exige streams de asignación, evidencia y salida Analyzer distintos entre R;
4. calcula una contribución por mundo m promediando R;
5. calcula media y MCSE entre las M contribuciones independientes, sin tratar M×R como observaciones independientes.

Por tanto, **M es el denominador Monte Carlo externo** y R controla la precisión de la aproximación dentro de cada mundo. La estructura no debe sustituirse por un promedio plano de M×R ni por el MCSE calculado sobre las R asignaciones agrupadas.

Para una métrica replicable (Y_{mr}), la descomposición conceptual es:

`Var(\bar Y_m)=Var(E[Y_{mr}\mid m])+E[Var(Y_{mr}\mid m)]/R`.

La primera componente es heterogeneidad entre mundos; la segunda es ruido de asignación/observación dentro del mundo. Aumentar R reduce la segunda, no la primera. La elección de R=20 no queda justificada mientras el informe no estime ambas componentes por separado y no muestre la estabilidad de la decisión de dimensionamiento. La identidad y el orden de agregación ya están implementados; no hace falta recrear Gate 154/156 ni importar sus unidades RUN.

### 358.2 Hallazgo principal: la regla all-R-identifed cambia el estimando de rendimiento y puede invalidar la métrica

En escenarios cuya verdad es IDENTIFIED, el código calcula bias, MAE, MSE/RMSE y point-recovery de un mundo m solo si **todas** sus R réplicas están identificadas. Si una sola R se abstiene, la contribución numérica completa de ese mundo se convierte en `None`; si ocurre en cualquier M, la métrica agregada se convierte en `NOT_EVALUABLE`.

Esto evita el sesgo de un complete-case silencioso, pero también hace que la métrica de precisión condicional no pueda calcularse cuando existe cualquier abstención, por pequeña que sea. Mezcla dos preguntas diferentes:

- ¿Con qué frecuencia el procedimiento identifica y emite un resultado?
- Cuando emite un resultado identificado, ¿qué error comete?

No se debe resolver eliminando réplicas fallidas ni imputando error cero. Se deben definir **dos familias de estimandos operacionales**:

**A. Rendimiento total del procedimiento (denominador M×R, con agregación primero dentro de M):**
- tasa de identificación;
- tasa de no identificación, indeterminación y partial identification, separadas;
- tasa de abstención por causa prevista, causa incorrecta y causa ausente/no clasificable;
- tasa de falsa identificación en el escenario NOT_IDENTIFIED;
- disponibilidad de intervalo;
- proporción conjunta de réplica con intervalo emitido y verdad cubierta, si se decide expresamente como métrica operacional.

Estas métricas evalúan el procedimiento completo y nunca deben perder los M en los que el Analyzer no identifica.

**B. Rendimiento numérico condicional a estimación identificada:**
- bias condicional;
- MAE condicional;
- RMSE condicional;
- point-recovery condicional a identificación, con tolerancia δ explícita y versionada.

La definición natural de estas métricas es sobre todas las réplicas identificadas del conjunto M×R, manteniendo la agrupación por mundo para calcular incertidumbre. Una formulación de razón es:

`MAE_cond = Σ_{m,r} I_{mr} |e_{mr}| / Σ_{m,r} I_{mr}`

donde (I_{mr}=1) si Analyzer identifica y emite estimación finita. Bias condicional sustituye (|e|) por (e); RMSE condicional utiliza (e^2) y raíz al final; point-recovery utiliza (I(|e|≤δ)). Las réplicas no identificadas no reciben error numérico, pero sí permanecen en las métricas operacionales A.

El MCSE de estas razones debe estimarse con M como unidad independiente, conservando para cada mundo numerador y denominador y usando una varianza de tipo cluster/ratio (o un bootstrap por mundos preespecificado). No se permite calcular el MCSE sobre el conjunto de réplicas identificadas como si fueran independientes. Si el total de réplicas identificadas es cero, las métricas condicionales son `NOT_EVALUABLE` con denominador cero y causa explícita; no se oculta el resultado. Debe decidirse además si el objetivo científico pondera por réplica o por mundo; no son el mismo estimando si la probabilidad de identificación varía entre mundos.

### 358.3 Intervalos: separar disponibilidad, cobertura condicional y éxito conjunto

El código actual resume cobertura inferencial y anchura solo cuando las R réplicas del mundo tienen intervalo. Esto replica el problema all-R anterior. Además, cobertura de un intervalo emitido y disponibilidad de emitirlo son dimensiones diferentes.

El contrato debe separar:

- **Disponibilidad:** proporción de M×R para la que se emite un intervalo inferencial válido.
- **Cobertura condicional:** proporción de intervalos emitidos que contienen la truth reservada, indicando explícitamente el denominador de intervalos emitidos.
- **Éxito conjunto operacional:** proporción de todas las réplicas que emiten intervalo y cubren la truth, solo si se declara como tal.
- **Anchura:** distribución/estimando de anchura entre intervalos emitidos, con denominador y MCSE cluster por M.

No convertir abstenciones en intervalos fallidos para la métrica clásica de cobertura, ni excluirlas del rendimiento operacional. La cobertura condicional puede ser selectiva y no equivale a cobertura incondicional del procedimiento; ambas deben aparecer juntas.

### 358.4 Estados de identificación y causas actualmente colapsados

El agregador expone `identification_rate` y `abstention_rate = 1-identification_rate`. Para escenarios identificados, `false_abstention_rate` vuelve a contar todo estado distinto de IDENTIFIED. Para el escenario NOT_IDENTIFIED, `wrong_cause_abstention_rate` agrupa NOT_IDENTIFIED con causa incorrecta e INDETERMINATE; partial identification y false identification se reportan aparte.

Por ello todavía no existe una tabla completa de estados mutuamente excluyentes. Deben conservarse, por escenario y N, las frecuencias/tasas de:
- IDENTIFIED;
- NOT_IDENTIFIED con causa esperada;
- NOT_IDENTIFIED con causa distinta;
- INDETERMINATE;
- PARTIALLY_IDENTIFIED;
- output inválido;
- registro ausente.

Los dos últimos no pueden convertirse en estados del Analyzer ni confundirse con abstención. El contrato actual de captura exige el registro exacto del plan, por lo que la ausencia bloquea la agregación; debe seguir visible como fallo de integridad/coverage, no como resultado científico.

### 358.5 Evaluator: no usar la adjudicación compuesta como una única tasa de calidad

La revisión del código del Evaluator confirma que `correct_adjudication` en IDENTIFIED exige simultáneamente cobertura de bounds y error puntual dentro de la tolerancia; en NOT_IDENTIFIED/INDETERMINATE exige que la verdad esté dentro de bounds. Los bounds lógicos son [-1,1] y la truth focal válida está restringida al mismo dominio. Así, `truth_within_bounds` no discrimina rendimiento y la adjudicación compuesta no tiene el mismo significado entre clases.

Se mantienen como evidencia de auditoría/disposition, pero no se utilizarán como un único KPI comparativo entre escenarios. El contrato de métricas debe separar:
- recuperación puntual y su error, en identificados;
- cobertura inferencial Hoeffding, en identificados;
- corrección de clase/causa de abstención, en no identificados;
- cobertura de límites lógicos como invariante de dominio, no como evidencia de recuperación.

### 358.6 Precisión Monte Carlo y targets: reglas necesarias antes del freeze

La implementación calcula MCSE de una contribución por mundo entre M, lo cual es correcto cuando la contribución está definida y los mundos son independientes. Sin embargo:

1. `metric_targets` puede estar vacío o ser parcial; el diseño no exige la cobertura completa de las métricas obligatorias. Un resultado `NOT_TARGETED` no puede convertirse en PASS.
2. Para tasas binarias por mundo, MCSE≤0,05 con M=100 es un límite de peor caso válido porque cada contribución de mundo está en [0,1]. No garantiza ≤0,02; ese objetivo requiere hasta M=625 en el peor caso.
3. Para métricas continuas, M requerido depende de la varianza entre las contribuciones de mundo; debe estimarse en un piloto y ampliarse con regla versionada, sin fijar M por anticipado a partir del valor observado de una sola ola.
4. Para RMSE, el código calcula primero MSE por mundo y aplica una aproximación delta para MCSE de la raíz. Cerca de RMSE=0 la aproximación puede ser inestable; cuando RMSE=0 y MCSE(MSE)>0 devuelve MCSE no evaluable. Conservar MSE y su MCSE como resultado primario de precisión Monte Carlo y documentar RMSE/MCSE delta como derivado, o preespecificar un método cluster robusto alternativo.
5. El objetivo de MCSE≤0,02 para bias/MAE/RMSE/anchura media es candidato, no un umbral científico de error admisible. El MCSE pequeño significa que se conoce con precisión el rendimiento del estimador; no que el estimador tenga poco sesgo o error.
6. Los targets deben estar completos por escenario × versión × N × métrica, con clase de aplicabilidad explícita. Las métricas no aplicables al escenario NOT_IDENTIFIED son `NOT_APPLICABLE`, distintas de `NOT_TARGETED`, `NOT_EVALUABLE` y `FAIL_PRECISION`.

### 358.7 Tolerancia de recuperación y trazabilidad del criterio

`ThetaACalibrationDesign.point_recovery_tolerance` se utiliza para clasificar point-recovery, mientras que el Evaluator recibe su propia tolerancia en el executor. El registro `ThetaAReplicateRecord` no conserva el valor ni la identidad/version del criterio utilizado. La captura valida la adjudicación registrada, pero no permite reconstruir desde el registro qué umbral científico produjo `POINT_RECOVERED` o `POINT_RECOVERY_FAILED`.

Antes del freeze se requiere una única fuente de verdad para el umbral o dos criterios expresamente diferenciados:
- tolerancia de adjudicación técnica del Evaluator;
- tolerancia δ de recuperación científica.

En ambos casos el valor, versión, unidad, alcance por escenario y hash deben quedar en el diseño, la asignación/manifest, el registro por réplica y el resumen. No se adopta automáticamente 0,25 ni se altera el Evaluator en esta revisión.

### 358.8 Dictamen y siguiente cierre documental

**Dictamen:** la estructura M×R y el MCSE entre mundos están bien orientados; la regla all-R-identifed para métricas numéricas y de intervalo no representa adecuadamente un procedimiento que puede abstenerse en una parte de sus réplicas. No es un fallo de integración ni justifica cambiar Analyzer/Evaluator. Es una brecha de definición del estimando de rendimiento y del contrato de agregación.

Antes de modificar código, la especificación debe decidir:
1. ponderación de las métricas condicionales: por réplica identificada o por mundo con al menos una identificación;
2. método cluster/ratio para MCSE de métricas condicionales y método de incertidumbre para RMSE;
3. separación entre cobertura condicional, disponibilidad y éxito conjunto;
4. taxonomía mutuamente excluyente de estados y causas;
5. tolerancias técnica y científica, con identidades/versiones;
6. conjunto exhaustivo de targets por escenario × N × métrica y estados de aplicabilidad;
7. regla de dimensionamiento R basada en varianza intramundo y M basada en varianza entre mundos.

La revisión no cambia código, tests, roster, N/M/R, seeds, truth, Analyzer, Evaluator, tolerancias, bancos ni autorizaciones. No se ejecutó el runner ni calibración. `calibration_authorized=false`; `scientific_execution=false`; `execution_authorized=false`.

**Siguiente operación:** elaborar la especificación de estimandos de rendimiento y denominadores (documental, sin implementación), resolver la ponderación por réplica frente a mundo y fijar el método de MCSE cluster/ratio. Solo después se podrá redactar el contrato estadístico cuantitativo completo y valorar si necesita una decisión gobernada.


## 359. Especificación propuesta de estimandos de rendimiento y denominadores para el benchmark focal — revisión documental (2026-11-18)

**Estado:** PERFORMANCE_ESTIMANDS_SPECIFIED_AS_CANDIDATE / NOT_FROZEN / IMPLEMENTATION_NOT_AUTHORIZED / CALIBRATION_NOT_AUTHORIZED.  
**Base:** auditoría §358 y agregador existente `summarize_theta_a_calibration()`.  
**Propósito:** separar el rendimiento operacional del procedimiento completo de la precisión numérica condicional, sin borrar réplicas no identificadas ni convertir abstenciones en errores numéricos.

### 359.1 Unidad estadística y clave de agregación

La unidad independiente para incertidumbre Monte Carlo es el mundo exterior M. Las R asignaciones de un mundo son repeticiones condicionales al mismo mundo, no mundos independientes. La clave mínima de cada resumen es:

`(scenario_id, scenario_version, N, metric_id, metric_version, estimand_id, estimand_version, DGP_profile_sha256, design_config_sha256)`.

Cada mundo m conserva un vector de contadores/sumas por métrica; el resumen no se construye destruyendo la relación entre las R réplicas y su mundo.

### 359.2 Plano operacional primario — todas las R intentadas

Para cada mundo m y escenario/N, con R intentos previstos y validados:

- `identified_rate_m = n(IDENTIFIED)/R`;
- `not_identified_rate_m = n(NOT_IDENTIFIED)/R`;
- `indeterminate_rate_m = n(INDETERMINATE)/R`;
- `partial_identification_rate_m = n(PARTIALLY_IDENTIFIED)/R`;
- `invalid_output_rate_m` y `missing_record_rate_m`, si el sistema de captura permite observar esos fallos sin convertirlos en estados Analyzer. La ausencia de registro sigue siendo un fallo de integridad del plan y bloquea el PASS de cobertura;
- para el escenario estructuralmente NOT_IDENTIFIED: `correct_cause_abstention_rate_m`, `wrong_cause_abstention_rate_m` y `false_identification_rate_m`, con clasificación mutuamente excluyente;
- para escenarios IDENTIFIED: `false_abstention_rate_m = 1 - identified_rate_m`, desglosada por estado y causa.

El estimando agregado primario es la media no ponderada de las M contribuciones de mundo. El denominador de cada tasa es R por mundo y M mundos completos. La incertidumbre Monte Carlo se calcula entre las M contribuciones, no sobre M×R filas.

Los estados de salida válidos deben ser mutuamente excluyentes. Una taxonomía de implementación futura puede incluir además `OUTPUT_INVALID` y `RECORD_MISSING`, pero ambos son fallos técnicos/coverage y nunca deben atribuirse al comportamiento científico del Analyzer.

### 359.3 Plano numérico condicional — ponderación primaria por réplica identificada

Para los escenarios cuya verdad DGP es IDENTIFIED, la precisión numérica se define condicional a que el Analyzer haya producido una estimación puntual finita. La ponderación primaria propuesta es por réplica identificada, no por mundo con al menos una identificación:

`I_mr = 1[Analyzer_{mr}=IDENTIFIED y estimate_{mr} finita]`.

Para cada mundo se retienen numerador y denominador:
- bias: `A_m=Σ_r I_{mr} e_{mr}`;
- MAE: `A_m=Σ_r I_{mr}|e_{mr}|`;
- MSE: `A_m=Σ_r I_{mr}e_{mr}^2`;
- point recovery: `A_m=Σ_r I_{mr}1(|e_{mr}|≤δ)`;
- denominador común: `B_m=Σ_r I_{mr}`.

Los estimandos condicionales primarios se calculan como razones de sumas sobre mundos:

`Bias_cond = Σ_m A_m / Σ_m B_m`

con el numerador específico de bias, y análogamente para MAE, MSE y point-recovery. RMSE es `sqrt(MSE_cond)`. Esta definición responde: “entre todos los intentos de asignación en los mundos de la población DGP que el procedimiento identifica, ¿qué error produce?”. No afirma que la tasa de identificación sea alta; por eso siempre se presenta junto al plano operacional §359.2.

El MCSE se estima por clusters M. Para cada métrica razón `θ = Σ A_m / Σ B_m`, se conserva `u_m=A_m-θB_m` y se estima:

`MCSE_cluster(θ) = SD(u_1,…,u_M) / (sqrt(M) × mean(B_1,…,B_M))`.

La expresión presupone mundos independientes y una media de denominador positiva; si `Σ B_m=0`, la métrica condicional es `NOT_EVALUABLE` con denominador cero. No se calcula SD sobre las réplicas identificadas como si fueran independientes.

Como diagnóstico secundario se puede reportar la media no ponderada de las métricas condicionales por mundo con `B_m>0`, junto con el número de mundos elegibles y la distribución de `B_m/R`. Ese resultado es un estimando distinto, pondera por igual mundos con diferente número de identificaciones y no reemplaza el estimando primario por réplica.

### 359.4 Intervalos inferenciales

Para cada réplica identificada:
- `interval_issued_mr`: indicador de intervalo Hoeffding válido emitido;
- `covered_mr`: indicador de que el intervalo emitido contiene la truth reservada;
- `width_mr`: anchura del intervalo cuando está emitido.

Se proponen cuatro métricas distintas:

1. **Disponibilidad:** `Σ interval_issued/(M×R)`, media de disponibilidad por mundo.
2. **Cobertura condicional:** `Σ covered/Σ interval_issued`, estimada como razón por clusters M. Su denominador es el número de intervalos emitidos; se etiqueta expresamente como cobertura entre intervalos emitidos.
3. **Éxito conjunto:** `Σ 1(interval_issued AND covered)/(M×R)`, si se desea conocer la probabilidad de que un intento produzca un intervalo disponible y cubriente.
4. **Anchura condicional:** `Σ width/Σ interval_issued`, con MCSE cluster por M.

La cobertura condicional no se interpreta como cobertura incondicional del procedimiento cuando la emisión depende de identificación o ausencia de missingness. El éxito conjunto no se denomina “cobertura nominal” y no sustituye la cobertura condicional. El nivel 0,95 sigue siendo candidato del diseño, no una afirmación confirmatoria.

### 359.5 Evaluator y límites lógicos

Las métricas del Evaluator se mantienen en una capa de auditoría distinta:

- `evaluator_disposition` por réplica, con distribución de cada categoría;
- recuperación puntual del Evaluator en escenarios identificados, reportada con δ técnica explícita;
- corrección de clase/causa de abstención en el escenario NOT_IDENTIFIED;
- `truth_within_bounds` como control de dominio lógico [-1,1], no como métrica de rendimiento ni evidencia de recuperación.

No se agrega `evaluator_correct_adjudication_rate` entre escenarios identificados y no identificados como si fuese un KPI homogéneo. Tampoco se interpreta `POINT_RECOVERY_FAILED` como fallo de identificación estructural.

### 359.6 Tolerancias y targets

Se mantienen dos criterios distintos hasta decisión expresa:

- `δ_eval`: tolerancia técnica que utiliza el Evaluator para emitir `POINT_RECOVERED/POINT_RECOVERY_FAILED`;
- `δ_science`: tolerancia científica de recuperación para la métrica `point_recovery_rate`.

No se presupone que sean iguales. Cada criterio deberá tener valor, unidad, versión, justificación, ámbito de aplicación y fingerprint. Si se decide que son el mismo criterio, la identidad compartida debe quedar explícita y validada; si son distintos, sus métricas no se deben fusionar.

El manifiesto de targets debe enumerar el conjunto exacto de métricas obligatorias por escenario × versión × N. Debe distinguir:
- `TARGETED`: tiene objetivo MCSE preespecificado;
- `NOT_APPLICABLE`: métrica no definida para esa clase de verdad;
- `NOT_TARGETED`: métrica aplicable sin objetivo de precisión;
- `NOT_EVALUABLE`: faltan datos elegibles o denominador positivo;
- `FAIL_PRECISION`: MCSE supera el target;
- `PASS_PRECISION`: MCSE satisface el target y la cobertura/procedencia está completa.

No se permite PASS de calibración cuando cualquier target obligatorio está ausente, incompleto o no evaluable. Un PASS_PRECISION solo acredita precisión Monte Carlo de la estimación de la métrica; no acredita que el estimador tenga sesgo/error aceptable.

### 359.7 R y M: regla de dimensionamiento que debe acompañar a la implementación

La primera calibración no debe asumir que R=20 y M=100 son suficientes. Para cada métrica primaria se estimarán:
- varianza entre mundos de las contribuciones por mundo;
- componente de varianza dentro del mundo entre asignaciones;
- MCSE externo observado;
- sensibilidad de MCSE y del rendimiento a aumentar R manteniendo M, y a aumentar M manteniendo R.

R se seleccionará para que el componente intramundo no domine innecesariamente la varianza de la contribución por mundo. M se seleccionará para satisfacer los targets MCSE entre mundos. Cualquier extensión adaptativa del banco de calibración deberá tener una regla determinista/versionada de derivación de seeds, límite de presupuesto y regla de parada preespecificada; nunca se ampliará el banco de evaluación a partir de sus propios resultados.

### 359.8 Decisiones aún abiertas y disposición

Esta especificación es una propuesta coherente con la unidad M×R ya implementada, no una congelación. Antes de implementar se requiere decidir:
1. si se acepta la ponderación primaria por réplica identificada y se mantiene la ponderación por mundo como diagnóstico secundario;
2. el método definitivo de MCSE cluster para razones y el método para RMSE (MSE primario más delta, o bootstrap cluster preespecificado);
3. si el éxito conjunto de intervalo se requiere como target;
4. la taxonomía final de estados y códigos de causa;
5. valores/versiones y justificación de `δ_eval` y `δ_science`;
6. lista exhaustiva de targets y estados de aplicabilidad.

**No se cambia código ni tests.** No se crean seeds/bancos, no se ejecuta calibración ni evaluación, no se ejecuta Monte Carlo y no se autoriza ejecución científica. Se mantienen `calibration_authorized=false`, `execution_authorized=false`, `scientific_execution=false`.

**Siguiente operación:** reconciliar esta especificación con los contratos existentes de calibración, métricas y evaluación para comprobar que no contradice un criterio ya aceptado; resolver los seis puntos abiertos mediante propuesta de decisión, sin modificar implementación hasta que el contrato quede estable.


## 360. Reconciliación histórica de §358–359 con contratos C10-S vigentes — revisión documental (2026-11-18)

**Estado:** HISTORICAL_RECONCILIATION_COMPLETED / METRIC_SEMANTICS_DECISION_OPEN / NO_CONTRACT_FROZEN / NO_IMPLEMENTATION / CALIBRATION_NOT_AUTHORIZED.  
**Regla aplicada:** Historical Reconstruction Before New Work Rule v0.1.  
**Fuentes focales inspeccionadas:** §§328, 330, 336, 348, 355–357 del presente maestro; `theta_a_calibration_protocol.py` (blob `9675b9f6805b11f1a1037a3e4b2f95af53038e4c`); `harness/README.md`; contratos V_cont históricos indicados abajo.  
**Propósito:** distinguir qué está ya definido/implementado, qué es una convención provisional del scaffold y qué decisión nueva propone §359. No reabrir ni importar contratos de otro benchmark.

### 360.1 Identidad del experimento: θ_A focal, no benchmark V_cont de 13×52

La fuente rectora del alcance es §357.2 y la declaración anterior §328: el protocolo focal `theta_a_calibration_protocol.py` evalúa exclusivamente `THETA_A_QX_GA_RCOMMON_VCONT` sobre `V_CONT`, con jerarquía N×M×R y **sin RUN separado**. No reutiliza el seed bank ni las clases RUN/REPEATED_ASSIGNMENT del benchmark V_cont anterior.

Se inspeccionaron:
- `C10_S_VCONT_CALIBRATION_AND_SEED_BANK_PROTOCOL_DRAFT_001.md`;
- `C10_S_VCONT_SCENARIO_ESTIMAND_COVERAGE_MATRIX_DRAFT_001.md`;
- `C10_S_VCONT_MONTE_CARLO_OUTER_REPLICATION_CONTRACT_DRAFT_001.md`;
- `C10_S_VCONT_MONTE_CARLO_MATRIX_COVERAGE_CONTRACT_GATE_156_DRAFT_001.md`;
- `C10_S_THETA_A_IDENTIFICATION_AND_ANALYZER_RECOVERY_AUDIT_GATE_129_DRAFT_001.md`.

El protocolo/coverage de 13 escenarios × 4 estimandos = 52 pares corresponde a ITT-Z/ITT-G y sus niveles temporales. El Gate 154/155/156 conserva una fila RUN designada más R asignaciones repetidas dentro de cada M y sus obligaciones de ledger 52-pair. Gate 129 confirma que θ_A no es un alias de ITT-G ni del contraste del benchmark previo. Esos contratos son antecedentes relevantes para separación de estimandos, seed-bank disjointness, provenance, denominadores y estados fail-closed; **sus 52 pares, RUN extra y reglas de temporal contribution no se importan al protocolo focal θ_A**. Esta separación ya está expresamente documentada en §§328 y 357.2 y en el código de construcción de seed bank.

### 360.2 Reconciliación de estados históricos

| Elemento | Evidencia histórica | Estado correcto ahora |
|---|---|---|
| N/M/R e identidades de seed | §328 y `build_theta_a_seed_bank()` | IMPLEMENTED_SCAFFOLD; N/M/R numéricos no frozen |
| Cinco escenarios tipados | §§348 y 355; `build_theta_a_candidate_scenario_roster()` | CANDIDATE_ROSTER_IMPLEMENTED; no roster científico frozen |
| Fábrica/runner y captura | §355 y EP-02 Run 862 (§357.1) | SOFTWARE_CONFORMANCE_PASS; no calibration run |
| Orden de agregación | §328 y `summarize_theta_a_calibration()` | IMPLEMENTED: R dentro de M, MCSE entre M |
| Falta de una contribución | agregador actual exige cobertura exacta N×M×R; §328 | FAIL_CLOSED / NOT_EVALUABLE; no complete-case silencioso |
| Regla all-R para métricas condicionales | implementación actual del agregador | IMPLEMENTATION_CONVENTION, no decisión científica congelada |
| N={32,64,128}, M=100, R=20 | §§336/348/357 | CANDIDATE_ONLY |
| MCSE continuo ≤0,02 y tasas ≤0,05 | §§336/348/357 | CANDIDATE_TARGETS, no targets aprobados |
| Confianza 0,95 | §§336/357 y design field | CANDIDATE_ONLY |
| Tolerancia de recuperación | §357.4; design field nullable | OPEN; 0,25 del Evaluator no es criterio científico aprobado |
| Type-I error/potencia | §§328/330/357 | NOT_DEFINED_NO_TEST_PROCEDURE |
| Bancos, calibración y evaluación | harness README + §357 | NOT_GENERATED / NOT_EXECUTED / NOT_AUTHORIZED |

No se identifica un contrato de estimandos condicionales ya aprobado que obligue a ponderar por mundo o por réplica identificada. El scaffold actual usa una condición all-R para poder producir un valor por mundo; eso es una regla implementada para evitar denominadores selectivos, no una resolución formal del estimando científico condicional. Por tanto, §359 puede avanzar como propuesta de definición, pero no debe presentarse como mera documentación de una decisión ya aceptada.

### 360.3 Reconciliación de la ponderación condicional

§359 propone como estimando primario la razón agrupada por réplica identificada:

`θ_rep = Σ_m A_m / Σ_m B_m`,

donde `B_m` es el número de R identificadas en el mundo m. Esto estima el error esperado entre los intentos identificados de la distribución conjunta de mundos y asignaciones; mundos con más identificaciones aportan más peso. La incertidumbre se calcula por clusters M, no como si las filas M×R fueran independientes.

La alternativa es el promedio equiponderado de los cocientes de cada mundo elegible:

`θ_world = mean_m(A_m/B_m | B_m>0)`.

Esto responde a una pregunta distinta: rendimiento condicional medio del mundo, dando igual peso a mundos con distinta tasa de identificación. No debe confundirse con `θ_rep`.

**Propuesta para decisión, no congelada:** conservar `θ_rep` como estimando condicional primario porque corresponde a seleccionar al azar un intento de la población de intentos y condicionar a que el procedimiento lo identifique; conservar `θ_world` como diagnóstico secundario para revelar heterogeneidad/selección entre mundos. Presentar siempre ambas junto a la tasa operacional de identificación y a la distribución de `B_m/R`. Si la pregunta científica que se desea priorizar es “un mundo típico”, deberá elegirse `θ_world` como primario mediante decisión explícita. Ninguno sustituye al rendimiento operacional sobre todos los intentos.

El estimador cluster/ratio propuesto en §359 es algebraicamente apropiado para `θ_rep` bajo mundos independientes y denominador medio positivo. Debe implementarse con la corrección de varianza muestral y conservar `(A_m,B_m)` para auditoría. Para `θ_world`, el MCSE se calcula entre los cocientes de mundos elegibles, pero su incertidumbre y selección deben reportar el número de mundos con B_m>0; no se puede ocultar mundos sin identificaciones.

### 360.4 Intervalos y cobertura: refinamiento necesario

La regla actual exige que todas las R réplicas tengan intervalo para producir la contribución de cobertura/anchura del mundo. §359 separa disponibilidad, cobertura entre intervalos emitidos, éxito conjunto y anchura condicional, lo que es metodológicamente más informativo y compatible con la exigencia histórica de no descartar abstenciones.

Debe precisarse que:
- `interval_issued` se determina por presencia y validez de ambos límites, no por `inference_covered` solamente;
- cobertura condicional usa como denominador todos los intervalos válidos emitidos;
- disponibilidad usa todos los intentos planificados;
- éxito conjunto usa todos los intentos planificados y exige intervalo válido + cobertura;
- anchura condicional usa solo intervalos válidos emitidos.

El registro actual valida la consistencia de límites/cobertura/anchura y exige ausencia de intervalo en salidas no identificadas. El capture ledger estricto exige todos los registros N×M×R. Un registro ausente o inválido bloquea integridad/cobertura del plan y no se transforma en abstención ni en intervalo no cubriente. No debe prometerse una tasa de `missing_record`/salida inválida hasta que exista un ledger de intentos capaz de registrar esos fallos externos sin perder el plan esperado.

### 360.5 Estados y aplicabilidad: discrepancia real entre propuesta y código

El agregador actual representa varias métricas no aplicables a un escenario con una lista de contribuciones `None`, que termina en `NOT_EVALUABLE`. §359 propone distinguir correctamente `NOT_APPLICABLE` de `NOT_EVALUABLE`, `NOT_TARGETED`, `FAIL_PRECISION` y `PASS_PRECISION`. Esta es una mejora contractual pendiente, no una capacidad ya implementada.

La clasificación debe quedar así:
- `NOT_APPLICABLE`: métrica semánticamente no definida para la clase de truth/escenario;
- `NOT_TARGETED`: aplicable y calculable, pero sin target MCSE aprobado;
- `NOT_EVALUABLE`: aplicable pero sin denominador elegible, datos suficientes o incertidumbre calculable;
- `FAIL_PRECISION`: target aprobado, cobertura íntegra y MCSE por encima del límite;
- `PASS_PRECISION`: target aprobado, cobertura íntegra y MCSE dentro del límite.

El escenario estructuralmente NOT_IDENTIFIED no recibe bias/MAE/MSE/RMSE/point recovery ni cobertura condicional de intervalos como si hubiese estimación identificada; estas métricas son `NOT_APPLICABLE`, no `NOT_EVALUABLE`. La disponibilidad de intervalo, abstención correcta/causa incorrecta y falsa identificación sí son métricas aplicables. En escenarios IDENTIFIED, las tasas de falsa identificación/correct abstention propias de la clase no identificada son `NOT_APPLICABLE`.

La taxonomía de Analyzer debe mantener estados mutuamente excluyentes y la causa observada. `OUTPUT_INVALID` y `RECORD_MISSING` pertenecen a integridad técnica/coverage, no son estados Analyzer. La validación exacta actual fail-closed es conservadora; no debe relajarse para conseguir contadores de fallos.

### 360.6 Targets, tolerancias y MCSE: qué ya está y qué falta

El código valida cada target que recibe, pero no exige que el conjunto de targets cubra todas las métricas obligatorias de cada escenario × N. Si faltan targets, el resumen puede devolver `NOT_TARGETED`; esto no es suficiente para un PASS de calibración. §359 acierta al exigir un manifiesto exhaustivo, pero su schema debe especificar la aplicabilidad esperada y el target obligatorio por clave.

Se conserva la precedencia de §336/§348/§357:
- targets candidatos continuos ≤0,02;
- targets candidatos de tasas ≤0,05;
- M=100 solo alcanza el peor caso 0,05 para contribuciones binarias por mundo; no garantiza 0,02;
- N=32/64/128 es grid de calibración candidato y no demuestra precisión inferencial del Analyzer;
- R=20 es candidato sin análisis de componentes intra/intermundo;
- confianza 0,95 es candidata, no nivel congelado;
- no se fija MDE, type-I error, potencia ni tolerancia científica de recuperación.

Para RMSE, mantener MSE y su MCSE como resultados primarios evita depender de una aproximación delta inestable cerca de cero. RMSE puede mostrarse como transformación descriptiva; si se le asigna un target MCSE propio, deberá preespecificarse y validarse el método de incertidumbre (p. ej. bootstrap por mundos) antes del freeze. No convertir automáticamente el target de MSE en target de RMSE.

### 360.7 Tolerancias y procedencia

`point_recovery_tolerance` está en el design actual, pero no forma parte del registro de réplica como valor/version/hash; tampoco queda vinculada al umbral técnico de adjudicación del Evaluator. Se confirma la brecha de §357.4.

No se hereda el 0,25 de la adjudicación del Evaluator como tolerancia científica. Antes del freeze se requiere una de estas decisiones explícitas:
1. `δ_eval` y `δ_science` son el mismo criterio: identidad/version/fingerprint único, valor justificado y propagado a diseño, manifiesto, réplica y resumen; o
2. son criterios distintos: dos métricas etiquetadas por separado, cada una con valor, versión, justificación y ámbito.

La tolerancia no debe usarse para convertir recuperación puntual en condición de identificación estructural. `POINT_RECOVERY_FAILED` continúa siendo una salida identificada con recuperación puntual insuficiente según el criterio técnico, no una abstención.

### 360.8 Dictamen y trabajo mínimo restante

**Dictamen:** §359 es compatible con la arquitectura focal N×M×R y no contradice ningún contrato estadístico focal previamente congelado, porque las decisiones numéricas y el estimando de rendimiento condicional estaban explícitamente abiertos. Sí propone un cambio semántico respecto de la regla all-R implementada; ese cambio debe aprobarse como contrato antes de tocar el agregador. Los contratos V_cont 13×52 y RUN+R no se reabren ni se mezclan con θ_A.

**Cierres documentales pendientes antes de implementación:**
1. aprobar/rechazar `θ_rep` primario y `θ_world` secundario;
2. decidir cobertura condicional, disponibilidad y éxito conjunto como métricas obligatorias;
3. fijar taxonomía final de estados/códigos de causa y aplicabilidad;
4. cerrar target manifest exhaustivo por escenario × versión × N × métrica;
5. decidir `δ_eval` frente a `δ_science` y su trazabilidad;
6. seleccionar MSE como métrica de precisión primaria y método/estatus de RMSE;
7. establecer cómo se estima varianza intra/intermundo para dimensionar R/M sin reutilizar evaluación.

No se modifica `theta_a_calibration_protocol.py`, tests, DGP, roster, Analyzer, Evaluator, tolerancias, seeds, banks, workflows ni autorizaciones. No se ejecuta EP-02, calibración, Monte Carlo ni evaluación. `main`, RMA v3.38, Matrix v1.47, STATUS y TGCV Core permanecen sin modificación. PR #116 permanece Draft. `calibration_authorized=false`, `scientific_execution=false`, `execution_authorized=false`.

**Siguiente operación:** convertir los siete cierres en una propuesta de decisión breve, con recomendación y alternativas explícitas, y verificar que cada elección se refleje coherentemente en el manifiesto y en el contrato de agregación antes de cualquier implementación.

## 361. Propuesta de decisión metodológica sobre métricas y agregación θ_A — para resolución, no aprobada (2026-11-18)

**Estado:** DECISION_PROPOSAL_READY_FOR_REVIEW / NOT_APPROVED / NOT_FROZEN / NO_IMPLEMENTATION / NO_CALIBRATION.  
**Base reconciliada:** §§328, 330, 336, 348, 355–360.  
**Regla:** propuesta coordinadora; no crea ni presume aprobación del usuario, DR o freeze científico.

### 361.1 Decisiones recomendadas

| ID | Cuestión | Recomendación propuesta | Alternativa / coste de elegirla |
|---|---|---|---|
| MP-01 | Ponderación del error condicional | θ_rep: razón de sumas sobre todas las réplicas identificadas; MCSE cluster por M. Publicar siempre tasa de identificación y distribución de B_m/R. | θ_world: media equiponderada de cocientes por mundo elegible. Responde a mundo típico, pero excluye mundos con B=0 y selecciona por identificación; mantener solo como diagnóstico, claramente rotulado. |
| MP-02 | Métricas de intervalo | Obligatorias por separado: disponibilidad sobre todos los intentos, cobertura entre intervalos válidos emitidos, anchura condicional y éxito conjunto intervalo-válido-y-cubriente sobre todos los intentos. | Omitir éxito conjunto reduce redundancia, pero pierde una medida operacional directa que combina disponibilidad y cobertura; no debe sustituir a ninguna de las otras. |
| MP-03 | Estados y causas | Estados Analyzer mutuamente excluyentes: IDENTIFIED, NOT_IDENTIFIED, INDETERMINATE, PARTIALLY_IDENTIFIED. Para NOT_IDENTIFIED, clasificar causa esperada, causa distinta y causa ausente/no clasificable. OUTPUT_INVALID y RECORD_MISSING permanecen en ledger técnico/coverage, no en Analyzer. | Una tasa binaria abstain/identify es más simple, pero oculta error de causa, indeterminación y partial identification; no recomendada como única salida. |
| MP-04 | Aplicabilidad y targets | Manifiesto exhaustivo por escenario × versión × N × métrica, con NOT_APPLICABLE, TARGETED, NOT_TARGETED, NOT_EVALUABLE, FAIL_PRECISION, PASS_PRECISION. Todo target obligatorio debe existir y tener denominador/procedencia completos para permitir PASS. | Targets parciales permiten análisis exploratorio, pero no un PASS global ni selección de N/M/R. |
| MP-05 | Tolerancias | Separar δ_eval técnica y δ_science científica hasta que una decisión justifique explícitamente su identidad. No promover 0,25 del Evaluator a tolerancia científica. | Un único umbral simplifica trazabilidad, pero solo es aceptable si existe justificación científica independiente y la misma identidad/version queda propagada por todo el pipeline. |
| MP-06 | RMSE | Usar MSE y su MCSE como métrica primaria para dimensionamiento. Reportar RMSE=sqrt(MSE) como derivado descriptivo; no darle target MCSE propio hasta preespecificar/validar delta o bootstrap por mundos. | Bootstrap cluster por M puede proporcionar incertidumbre directa para RMSE, pero requiere algoritmo, número de remuestras, seed namespace y validación propios. |
| MP-07 | Dimensionamiento | Mantener N={32,64,128}, M=100, R=20 y targets ≤0,02 continuos / ≤0,05 tasas solo como grid y presupuesto piloto candidatos. En calibración autorizada, estimar componentes intra/intermundo: aumentar R solo si reduce materialmente el componente intramundo; aumentar M para precisión externa; elegir N con criterios separados de rendimiento inferencial y precisión MCSE. | Congelar ya N/M/R evita coste de diseño, pero no está respaldado por evidencia de precisión; no recomendado. |

### 361.2 Definiciones operacionales propuestas

Para cada mundo m:
- B_m = número de réplicas R con Analyzer IDENTIFIED y estimación puntual finita;
- A_m(metric) es la suma de la contribución de esa métrica sobre esas réplicas;
- θ_rep = Σ_m A_m / Σ_m B_m para bias, MAE, MSE y point-recovery, usando el numerador específico;
- MCSE_cluster(θ_rep) = SD(A_m - θ_rep B_m)/(sqrt(M) × mean(B_m)).

El resumen debe conservar A_m, B_m, B_m/R, world_id y los fingerprints del diseño. Si Σ B_m=0, el resultado es NOT_EVALUABLE, nunca cero. El diagnóstico θ_world debe mostrar cuántos mundos tienen B_m>0, cuántos tienen B_m=0 y la distribución de B_m/R; no se presenta como equivalente a θ_rep.

El estimador cluster/ratio propuesto es apropiado para θ_rep bajo mundos independientes y denominador medio positivo. Debe conservar (A_m,B_m) para auditoría. Para θ_world, el MCSE se calcula entre los cocientes de mundos elegibles, pero su incertidumbre y selección deben reportar el número de mundos con B_m>0; no se puede ocultar mundos sin identificaciones.

Para intervalos, se derivan por réplica tres indicadores independientes: issued, covered y width (width solo si issued). Se calculan disponibilidad y éxito conjunto con denominador M×R; cobertura y anchura condicionales con denominador de intervalos válidos emitidos. La inferencia Monte Carlo de las dos métricas condicionales usa clusters M y conserva sus numeradores/denominadores por mundo.

### 361.3 Reglas de interpretación y aceptación

1. La tasa de identificación y el error condicional se interpretan conjuntamente; un MAE condicional bajo no compensa una tasa de identificación baja.
2. PASS_PRECISION significa únicamente que la incertidumbre Monte Carlo de la métrica está dentro del target; no significa que el Analyzer tenga sesgo, RMSE o cobertura científicamente aceptables.
3. NOT_APPLICABLE no es fallo; NOT_EVALUABLE no es PASS; NOT_TARGETED no satisface un target obligatorio.
4. Cobertura condicional alta con disponibilidad baja no demuestra cobertura útil del procedimiento completo.
5. El éxito conjunto se presenta como métrica operacional y nunca se etiqueta como cobertura nominal.
6. Los targets de tasas se justifican sobre contribuciones por mundo acotadas en [0,1]; M=100 solo garantiza MCSE máximo 0,05 en peor caso. Un target 0,02 no se declara satisfecho por defecto.
7. N debe analizar por separado anchura/cobertura/potencia cuando exista un test válido; MCSE pequeño no sustituye criterio inferencial.
8. Ningún banco de evaluación puede utilizarse para ajustar N, M, R, tolerancias, roster, DGP, estimandos o reglas de análisis.

### 361.4 Dependencias antes de implementación

La aprobación de esta propuesta no bastaría por sí sola para ejecutar calibración. Antes de modificar el agregador deberán quedar cerrados:
- IDs/versiones y definiciones de cada métrica;
- manifiesto completo de aplicabilidad y targets;
- campos de réplica/manifiesto que fijan δ_eval y δ_science;
- ledger técnico para fallos externos sin recodificarlos como resultados Analyzer;
- fórmula y prueba independiente del MCSE cluster/ratio;
- método elegido para RMSE si se exige precisión Monte Carlo sobre RMSE;
- test de regresión que compare el agregador nuevo con cálculos independientes sobre fixtures que contengan abstenciones parciales, B_m=0, intervalos ausentes, causa incorrecta, INDETERMINATE, PARTIALLY_IDENTIFIED, OUTPUT_INVALID y RECORD_MISSING.

La implementación debe preservar el agregador histórico como referencia de regresión hasta demostrar equivalencia en los casos completos y la semántica nueva en los casos parciales. Esta comparación no autoriza modificar el Analyzer, Evaluator ni DGP.

**Disposición:** MP-01…MP-07 quedan como recomendaciones para decisión explícita. No se consideran aprobadas ni se registran como Decision Record aceptado. No se modifica código, tests, workflow, roster, N/M/R, targets, tolerancias, seeds o banks. No se ejecuta calibración, Monte Carlo, evaluación ni ejecución científica. main, RMA v3.38, Matrix v1.47, STATUS y TGCV Core permanecen intactos; PR #116 sigue Draft. Se mantienen calibration_authorized=false, execution_authorized=false, scientific_execution=false.

**Siguiente operación:** si las recomendaciones se aceptan, preparar el contrato de métricas y agregación implementable, más el test independiente del agregador; si alguna se rechaza, documentar la alternativa y su estimando antes de implementar.


## 362. Contrato implementable propuesto para el agregador θ_A y su manifiesto — diseño estático, no implementación (2026-11-18)

**Estado:** AGGREGATOR_CONTRACT_DRAFT / STATIC_DESIGN_ONLY / NOT_APPROVED / NOT_IMPLEMENTED / NO_CALIBRATION.  
**Base:** código fuente `theta_a_calibration_protocol.py` (blob `9675b9f6805b11f1a1037a3e4b2f95af53038e4c`), §§359–361 y EP-02 Run 862.  
**Ámbito:** exclusivamente benchmark focal `THETA_A_QX_GA_RCOMMON_VCONT`, cinco escenarios candidatos y jerarquía N×M×R; no incorpora el protocolo histórico V_cont 13×52 ni una fila RUN.

### 362.1 Principio de integridad: separar plan completo de elegibilidad métrica

Se mantienen dos validaciones diferentes:

**A. Integridad del plan (hard gate):** debe existir exactamente un registro válido para cada clave del seed plan N×M×R; sin duplicados, ausencias, claves extra, fingerprints inconsistentes, world/run discordantes o versiones mezcladas. El fallo de integridad invalida el resumen completo afectado y bloquea PASS. No se convierte `RECORD_MISSING` en estado Analyzer ni se aplica complete-case al plan.

**B. Elegibilidad de cada métrica (metric gate):** una vez validado el plan completo, cada réplica entra en el denominador que corresponde a la definición de esa métrica. La abstención Analyzer no invalida el registro ni borra las demás réplicas; simplemente excluye esa réplica de las métricas numéricas condicionales y permanece contada en las métricas operacionales.

Por tanto, el cambio propuesto no relaja la cobertura exacta del ledger N×M×R. Elimina únicamente la regla indebida de que todas las R deban estar identificadas para que un mundo contribuya a una métrica condicional.

### 362.2 Matriz de métricas y denominadores normativos propuestos

Para cada escenario/version/N y mundo m, R es el total de intentos planificados y validados. Defínanse:
- (I_{mr}=1) si Analyzer = IDENTIFIED y el punto es finito;
- (J_{mr}=1) si existe un intervalo con ambos límites finitos, ordenados, confidence level presente y cobertura/anchura internamente coherentes;
- (C_{mr}=1) si (J_{mr}=1) y el intervalo contiene la verdad reservada.

| Métrica | Numerador por mundo | Denominador por mundo | Agregación propuesta |
|---|---|---|---|
| identification_rate | Σ I | R | media no ponderada de M tasas |
| not_identified_rate | n(NOT_IDENTIFIED) | R | media no ponderada de M tasas |
| indeterminate_rate | n(INDETERMINATE) | R | media no ponderada de M tasas |
| partial_identification_rate | n(PARTIALLY_IDENTIFIED) | R | media no ponderada de M tasas |
| false_abstention_rate (truth IDENTIFIED) | n(Analyzer ≠ IDENTIFIED) | R | media no ponderada de M tasas; siempre desglosar estado |
| correct_cause_abstention_rate (truth NOT_IDENTIFIED) | n(NOT_IDENTIFIED con causa exacta) | R | media no ponderada de M tasas |
| wrong_or_unclassified_abstention_rate | n(NOT_IDENTIFIED/INDETERMINATE sin causa exacta) | R | media no ponderada de M tasas; desglosar causa |
| false_identification_rate (truth NOT_IDENTIFIED) | n(Analyzer = IDENTIFIED) | R | media no ponderada de M tasas |
| point_bias / MAE / MSE | Σ I·e / Σ I·|e| / Σ I·e² | B_m=ΣI | razón agrupada θ_rep sobre M; MCSE cluster ratio |
| point_recovery_rate | Σ I·1(|e|≤δ_science) | B_m=ΣI | razón agrupada θ_rep sobre M; MCSE cluster ratio |
| interval_availability_rate | Σ J | R | media no ponderada de M tasas |
| interval_conditional_coverage | Σ C | H_m=ΣJ | razón agrupada sobre M; MCSE cluster ratio |
| interval_joint_success_rate | Σ C | R | media no ponderada de M tasas |
| interval_conditional_width | Σ J·width | H_m=ΣJ | razón agrupada sobre M; MCSE cluster ratio |

Las tasas operacionales usan pesos iguales por mundo porque la unidad de población exterior es M; cada mundo aporta una proporción calculada sobre sus R intentos. Las métricas condicionales agrupadas ponderan por número de réplicas elegibles y contestan una pregunta por intento identificado/intervalo emitido. Ambas agregaciones son deliberadas y no intercambiables.

Para cada escenario de verdad NOT_IDENTIFIED, las métricas de punto/intervalo condicionales son `NOT_APPLICABLE`; no `NOT_EVALUABLE`. Para escenarios de verdad IDENTIFIED, las tasas de causa correcta de abstención y falsa identificación propias del escenario NOT_IDENTIFIED son `NOT_APPLICABLE`. La métrica de partial identification sigue siendo aplicable a ambos tipos de verdad.

### 362.3 MCSE por unidad exterior

**Tasas y medias de contribuciones por mundo.** Para una métrica con contribución (q_m) definida en cada mundo independiente:

`MCSE = s(q_1,…,q_M)/sqrt(M)`

con desviación estándar muestral (M−1). La salida conserva los M valores q_m y su identidad world_id.

**Estimandos ratio condicionales.** Para (θ=ΣA_m/ΣB_m), con (B_m≥0) y (ΣB_m>0), conservar pares ((A_m,B_m)) y calcular residuos de influencia (u_m=A_m-θB_m). La propuesta de MCSE es:

`MCSE_ratio = s(u_1,…,u_M)/(sqrt(M) × mean(B_1,…,B_M))`.

Se requiere M≥2, mundos independientes y denominador agregado positivo. La implementación deberá verificar mediante cálculo independiente que esta fórmula reproduce la varianza sandwich/cluster del estimador ratio para fixtures fijados. Si (ΣB_m=0), el resultado es `NOT_EVALUABLE`, con denominador cero y motivo explícito. No se calcula SD sobre filas M×R como si fueran independientes.

Para `θ_world` secundario, primero se calcula (a_m=A_m/B_m) solo cuando B_m>0 y luego la media y MCSE muestral entre mundos elegibles. Se reportan M elegibles, M con B=0 y su fracción; el resultado no se mezcla con θ_rep.

### 362.4 MSE/RMSE y tolerancia

El identificador primario de precisión es `point_mse`, no `point_rmse`. Se calcula θ_rep de errores cuadrados y su MCSE ratio. RMSE=(sqrt{MSE}) se emite como transformación descriptiva sin target MCSE ni PASS independiente. La salida no debe etiquetar como `point_rmse` un MCSE delta calculado sin contrato. Si más adelante se exige target RMSE, se añadirá un método cluster preespecificado y validado como métrica versionada.

La métrica point-recovery requiere `δ_science` no nula, finita, no negativa, versionada y con justificación. `δ_eval` pertenece al Evaluator y se conserva como campo independiente. Mientras no haya decisión explícita y fingerprint, point-recovery es `NOT_TARGETED` o `NOT_EVALUABLE` según aplicabilidad/datos; no se infiere `δ_science=0.25`.

### 362.5 Manifiesto exhaustivo de métricas y targets

El contrato futuro deberá incluir un manifiesto independiente de los registros calculados. Clave única:
`(scenario_id, scenario_version, N, metric_id, metric_version)`.

Campos mínimos:
- `estimand_id/version`, `outcome_id/version`;
- `applicability`: `APPLICABLE` o `NOT_APPLICABLE`, con razón tipada;
- `target_status`: `TARGETED` o `NOT_TARGETED`;
- `target_mcse` obligatorio y positivo cuando TARGETED; nulo cuando NOT_TARGETED/NOT_APPLICABLE;
- `metric_definition_sha256`, `target_manifest_sha256`;
- unidad de medida, dirección/escala y método MCSE;
- `delta_science_id/version/value/sha256` cuando la métrica lo requiera;
- procedencia de N/M/R y del DGP profile.

La validación compara el conjunto esperado de claves contra el manifiesto, no solo valida las filas que casualmente están presentes. Una métrica APPLICABLE + TARGETED sin valor/target válido, o una clave obligatoria ausente, bloquea el PASS global. Una métrica NOT_APPLICABLE debe incluir razón y no puede llevar target. Una métrica APPLICABLE + NOT_TARGETED se reporta, pero impide declarar completitud confirmatoria si el contrato la había marcado como obligatoria.

Estados de salida:
- `NOT_APPLICABLE`: semánticamente no definida;
- `NOT_TARGETED`: aplicable, sin objetivo MCSE aprobado;
- `NOT_EVALUABLE`: aplicable, pero sin denominador/datos/MCSE;
- `FAIL_PRECISION`: target válido y MCSE > target;
- `PASS_PRECISION`: target válido, ledger íntegro y MCSE ≤ target.

`PASS_PRECISION` nunca es PASS científico del estimador. El estado global de calibración solo podrá ser PASS si todas las métricas requeridas tienen estado permitido por el manifiesto, ningún target obligatorio está ausente, todos los ledgers son íntegros y todos los targets obligatorios resultan PASS_PRECISION. NOT_TARGETED y NOT_EVALUABLE no satisfacen un target obligatorio.

### 362.6 Ledger técnico y Evaluator

El seed plan es el denominador de cobertura de intentos. Debe permitir distinguir:
- intento esperado y registro válido;
- intento esperado con fallo técnico/output inválido;
- intento esperado sin registro;
- registro presente con resultado Analyzer válido.

La falta de registro y la salida inválida se almacenan como códigos del ledger técnico, fuera de los cuatro estados Analyzer. En el estado actual, el agregador recibe registros completos ya validados y no puede estimar tasas observadas de missing/invalid externos; hasta que se especifique ese ledger, cualquier discrepancia hard-fail y no se presenta como una tasa científica.

Las salidas Evaluator se reportan en auditoría separada por disposición y escenario/clase de verdad. `truth_within_bounds` verifica el dominio lógico; no es rendimiento. La corrección de adjudicación del Evaluator no se agrega en un único porcentaje a través de escenarios identificados y no identificados. `POINT_RECOVERY_FAILED` no cambia IDENTIFIED a NOT_IDENTIFIED.

### 362.7 Contrato de resumen y trazabilidad

Cada resumen debe exponer, como mínimo:
- clave completa escenario/version/N y hashes DGP/design/manifest/metric;
- M, R y lista ordenada de world_id;
- por métrica: numeradores y denominadores por mundo, contribuciones por mundo cuando correspondan, valor agregado, MCSE, target, estado y motivo;
- M elegibles, M no elegibles y denominador total para toda métrica ratio;
- método/version de MCSE y unidad independiente;
- δ_eval y δ_science identificadas separadamente cuando existan;
- resultado de integridad del ledger y del manifiesto.

No se debe guardar solo el valor final y perder los numeradores/denominadores que permiten auditar la ponderación.

### 362.8 Suite de validación independiente exigida antes de implementación

La futura prueba de agregador debe calcular resultados esperados mediante un oráculo independiente (sin invocar el agregador bajo prueba) y cubrir al menos:

1. todos identificados: equivalencia numérica con el agregador histórico en métricas que comparten estimando/denominador;
2. abstención parcial en un mundo: las tasas operacionales incluyen todos los R y métricas condicionales incluyen solo I=1;
3. mundo B_m=0 junto a otros mundos elegibles: ratio θ_rep sigue definido; θ_world excluye ese mundo pero declara M elegibles y M con B=0;
4. todos B_m=0: NOT_EVALUABLE y nunca cero/PASS;
5. verdad NOT_IDENTIFIED: métricas numéricas identificadas NOT_APPLICABLE; causa correcta/incorrecta y falsa identificación siguen evaluables;
6. INDETERMINATE y PARTIALLY_IDENTIFIED: estados separados, no colapsados en NOT_IDENTIFIED;
7. intervalos ausentes en parte de R: disponibilidad, cobertura condicional, éxito conjunto y anchura usan denominadores distintos correctos;
8. intervalo presente con límites inconsistentes: record validation falla;
9. target ausente, duplicado, extra, NOT_APPLICABLE con target o TARGETED sin target: manifiesto rechazado;
10. ledger ausente/duplicado/extra o fingerprint discordante: hard-fail de integridad;
11. cálculo MCSE ratio contrastado con un oráculo algebraico y una fixture con denominadores heterogéneos;
12. permutación del orden de registros: salida idéntica tras canonical ordering.

Se conserva la implementación histórica como referencia de regresión para casos completos. La nueva semántica se prueba con oráculo independiente, no mediante autoconsistencia del propio agregador.

### 362.9 Disposición y siguiente operación

Este contrato es un diseño técnico-metodológico propuesto; no aprueba MP-01…MP-07 ni cambia su estado. Hay dos cuestiones que deben resolverse antes de implementación:
1. aceptación explícita de θ_rep como estimando primario y θ_world como diagnóstico;
2. aprobación del manifiesto de targets y de la obligatoriedad del éxito conjunto de intervalo.

La especificación también deja preparada la estructura de ledger técnico, sin fingir que el código actual mide fallos externos que nunca llegan a `ThetaAReplicateRecord`.

No se modifica código, tests, DGP, roster, Analyzer, Evaluator, workflow, seeds ni bancos. No se ejecuta calibración, evaluación, Monte Carlo ni ejecución científica. No se altera main, RMA, Matrix, STATUS o TGCV Core. PR #116 permanece Draft. Se mantienen `calibration_authorized=false`, `execution_authorized=false`, `scientific_execution=false`.

**Siguiente operación:** revisión adversarial del contrato §362, en especial denominadores de intervalos, clasificación de abstenciones, fórmula MCSE ratio, target-manifest completeness y compatibilidad de la equivalencia histórica, antes de preparar cualquier cambio de código.


## 363. Revisión adversarial de §362 contra código, tests y contratos previos — hallazgos y correcciones requeridas (2026-11-18)

**Estado:** ADVERSARIAL_REVIEW_COMPLETED / CONTRACT_REVISION_REQUIRED / NO_IMPLEMENTATION / NO_CALIBRATION.  
**Fuentes inspeccionadas:** §357 (en particular §§357.2–357.5), §§336, 348 y 355; §362; `theta_a_calibration_protocol.py` blob `9675b9f6805b11f1a1037a3e4b2f95af53038e4c`; `test_theta_a_calibration_protocol.py` blob `a15454020c1043c1d5244193d8c8feb64d3442b9`; harness README; gobernanza `main` (README, Bootstrap, Canonical State, STATUS, RMA v3.38, Matrix v1.47, traceability v3.38 y workflows aplicables).  
**Límite:** revisión estática de definición/código/tests. No se ejecutaron tests ni workflows, no se generaron bancos y no se estimaron propiedades Monte Carlo.

### 363.1 Dictamen ejecutivo

El §362 **no está listo para implementación**. La separación integridad del plan/elegibilidad métrica es correcta y necesaria; el estimando ratio `θ_rep` es coherente para una pregunta condicional por intento; y la fórmula propuesta de MCSE ratio es una aproximación cluster-sandwich de primer orden válida bajo condiciones explícitas. Sin embargo, hay discrepancias de semántica, aplicabilidad, trazabilidad y cobertura de pruebas que impiden traducir el contrato directamente a código.

No se encontró evidencia de que §362 haya sido implementado. El código conserva el hash inspeccionado y las pruebas existentes no prueban la nueva semántica.

### 363.2 Hallazgos por cuestión adversarial

| ID | Severidad | Cuestión | Resultado de la revisión | Corrección exigida |
|---|---|---|---|---|
| AR-01 | CRÍTICA | Selección al condicionar por identificación | `θ_rep=ΣA/ΣB` define correctamente el rendimiento entre intentos identificados al muestrear primero mundo y después intento, pero es un estimando post-selección; no describe el rendimiento global del procedimiento ni una calidad incondicional del Analyzer. La ponderación mayor de mundos con más identificaciones es intencional para esa población condicional. | Rotularlo siempre como rendimiento condicional por intento identificado; presentar al lado identificación/abstención por estado, distribución de B_m/R y errores por mundo. Prohibido interpretar un MAE bajo como buen rendimiento global si la identificación es escasa. No construir un score combinado sin una función de coste explícita para abstención. |
| AR-02 | MAYOR | `θ_world` secundario | La media de A_m/B_m solo sobre B_m>0 es un diagnóstico descriptivo, pero su población elegible depende de R: al cambiar R cambia la probabilidad de que un mundo tenga al menos una identificación. No es un estimando estable de “mundo típico” comparable entre diseños R. | Mantenerlo solo como diagnóstico dependiente de R, rotulado con M elegibles, M con B=0 y distribución B_m/R. No usarlo para seleccionar N/M/R ni para comparar grids como si su población fuese constante. Si se desea un estimando de mundo típico, definir otro contrato basado en tasas/esperanzas condicionales por mundo y tratar B=0 como no estimable, no como mundo excluido sin más. |
| AR-03 | MAYOR | MCSE del estimador ratio | `s(A_m−θB_m)/(√M·mean(B_m))` es la forma plug-in de primer orden del error estándar cluster del estimador ratio cuando M mundos son IID, la independencia entre clusters es válida, R y el protocolo de muestreo son fijos y E[B_m]>0. No es una garantía exacta de cobertura para M finito ni valida por sí sola M=100. | Mantener la fórmula como MCSE asintótico versionado; validar contra un oráculo sandwich independiente y simulación de cobertura/estabilidad bajo denominadores heterogéneos, correlación A/B, B=0 y distribuciones asimétricas. La prueba algebraica no sustituye la evaluación de cobertura. No calcular SD sobre M×R filas. |
| AR-04 | MAYOR | Comparaciones entre escenarios emparejados | §355 comparte mundo basal y semillas entre positivo, alternativa común y target-only. Los MCSE marginales por escenario no bastan para incertidumbre de diferencias entre escenarios: los mundos emparejados inducen covarianza que debe conservarse. | Si se comparan escenarios de una misma world_family, calcular contrastes pareados por world_id y su MCSE sobre diferencias de contribuciones/influencias. No combinar MCSE marginales como si los escenarios fueran independientes. |
| AR-05 | CRÍTICA | Denominadores de intervalos | La definición J=intervalo válido emitido, C=J y cobertura, disponibilidad ΣJ/R, cobertura condicional ΣC/ΣJ, éxito conjunto ΣC/R y anchura ΣJ·width/ΣJ es coherente. El código actual usa `inference_covered is not None` como proxy de emisión, respaldado por `record.validate()`, que exige bounds, confidence level, anchura y cobertura coherentes. | Preservar esos cuatro estimandos distintos. Definir explícitamente que disponibilidad mide intervalos válidos emitidos, no outputs inválidos ni registros perdidos; estos últimos pertenecen al ledger técnico. El nivel de confianza y el método de intervalo deben quedar vinculados por versión/hash a diseño y registro. |
| AR-06 | CRÍTICA | Manifiesto exhaustivo | El código valida únicamente targets presentes y permite lista vacía/parcial; la ausencia se convierte en `NOT_TARGETED`. §362 exige comparar contra claves esperadas, pero no define el registro normativo que genera el universo esperado ni un campo `required_for_calibration`. Además, incluir `target_manifest_sha256` dentro de cada fila del propio manifiesto produce autorreferencia si el hash se calcula sobre el documento completo. | Crear un Metric Registry versionado con conjunto esperado por clase de verdad/escenario × N. Añadir obligatoriedad, aplicabilidad y motivo; validar igualdad exacta de claves (faltantes, duplicadas y extras). Calcular el hash del payload canónico excluyendo el campo de hash y guardarlo en un envelope externo, o definir equivalente no circular. `NOT_TARGETED` nunca puede satisfacer una métrica obligatoria. |
| AR-07 | CRÍTICA | Clases de verdad frente a estados Analyzer | `ThetaACalibrationScenario.expected_identification` admite IDENTIFIED, NOT_IDENTIFIED e INDETERMINATE, mientras que `ThetaAReplicateRecord` también admite PARTIALLY_IDENTIFIED como salida Analyzer. El agregador usa el campo de escenario para elegir la rama de métricas; una verdad/escenario INDETERMINATE cae actualmente en la rama de no identificado y se le aplican métricas de causa esperada que no necesariamente existen. Los tests construyen precisamente un escenario INDETERMINATE para un caso de missingness. Se están mezclando identificabilidad estructural del estimando y disposición esperada del Analyzer. | Separar en el contrato `truth_identification_class` (propiedad del DGP/estimando) de `expected_analyzer_disposition` (resultado esperado bajo la información/observación). Definir aplicabilidad para verdad IDENTIFIED, NOT_IDENTIFIED y cualquier verdad INDETERMINATE; las cuatro salidas Analyzer deben conservarse como estados observados distintos. No resolverlo colapsando INDETERMINATE en NOT_IDENTIFIED. |
| AR-08 | MAYOR | Identificación parcial | §362 dice que `partial_identification_rate` aplica a ambas clases de verdad, pero el código actual solo calcula esa tasa en la rama de escenario no identificado y la rellena como no evaluable para escenario identificado. Además, §336 declara PARTIALLY_IDENTIFIED un control de software, no uno de los cinco escenarios focales. | Definir si partial identification es una salida adversarial aplicable a todo escenario o solo a determinadas clases. Si es aplicable a todos, calcular su frecuencia sobre R en todas las clases y definirla en el Metric Registry; no dejarla implícitamente ausente en escenarios identificados. |
| AR-09 | MAYOR | Métricas Evaluator | El código genera y permite targets para `evaluator_truth_within_bounds_rate` y `evaluator_correct_adjudication_rate`. §357.4.3 ya demuestra que truth-within-bounds es un invariante de dominio y que correct-adjudication mezcla reglas distintas entre clases; no es una métrica homogénea del Analyzer. §362.6 lo explica parcialmente, pero no dice cómo salen esas métricas del resumen/target manifest. | Mantener un ledger/summary de auditoría Evaluator separado del Metric Registry de rendimiento Analyzer. Registrar disposition, truth-within-bounds y adjudicación por clase/causa, sin target de rendimiento común ni agregación transversal entre clases. |
| AR-10 | CRÍTICA | Identidad MSE/RMSE | El código almacena `point_rmse_mse`, consulta target `point_rmse`, emite RMSE y aplica una aproximación delta a su MCSE. `_ALLOWED_METRICS` no contiene `point_mse`. §362 propone MSE primario y RMSE descriptivo; no existe correspondencia implementada ni target histórico de MSE. | Introducir `point_mse` como métrica e ID/version distintos, con target propio aprobado; conservar RMSE como derivado descriptivo sin PASS/MCSE hasta método aprobado. No renombrar silenciosamente un target RMSE existente como target MSE. |
| AR-11 | MAYOR | Equivalencia histórica | Con todas las R identificadas y todos los intervalos válidos, los valores de bias, MAE, point recovery, cobertura y anchura coinciden con las medias por mundo anteriores (R fijo). El RMSE histórico equivale a sqrt del MSE medio, pero el MCSE delta del RMSE no es el MCSE de MSE. Con abstención parcial o intervalos ausentes, la nueva semántica debe divergir intencionadamente del `NOT_EVALUABLE` all-R anterior. | Definir equivalencia por métrica y condición de dominio, no exigir igualdad global. Mantener tests de regresión del agregador antiguo en casos completos y oráculo independiente para casos parciales. Documentar como cambio semántico, no como refactor numérico. |
| AR-12 | CRÍTICA | Aplicabilidad histórica | §357.4.6 dice que bias/MAE/RMSE/recuperación/cobertura inferencial del escenario no identificado son `NOT_EVALUABLE`; §360 y §362 cambian a `NOT_APPLICABLE` porque la métrica no está definida para esa clase. Es una mejora semántica defendible, pero es una diferencia explícita frente al dictamen anterior, no una mera implementación de una decisión congelada. | Resolverlo explícitamente: recomendar `NOT_APPLICABLE` cuando la métrica presupone una estimación identificada que el DGP declara no identificable; reservar `NOT_EVALUABLE` para métrica aplicable sin datos/denominador/MCSE suficiente. Actualizar la reconciliación §360/§362 para declarar que se corrige la convención de §357.4.6, sin reescribir el antecedente. |
| AR-13 | MAYOR | Cobertura lógica en no identificación | §348 exige que Evaluator compruebe la verdad dentro de límites lógicos para el caso target-only. Eso no es cobertura de un intervalo inferencial ni debe confundirse con `interval_conditional_coverage`. El código ya conserva `evaluator_truth_within_bounds`. | Mantener la comprobación de bounds como invariante/auditoría Evaluator separada. No clasificarla como intervalo emitido, cobertura nominal ni éxito conjunto. |
| AR-14 | MAYOR | Universo de tasas de abstención | §362 añade tasas por estado, pero `wrong_or_unclassified_abstention_rate` puede ocultar diferencias entre NOT_IDENTIFIED con causa equivocada, NOT_IDENTIFIED sin causa, e INDETERMINATE con causa propia. El código actual también usa una definición combinada. | Conservar denominador R y desglosar por estado Analyzer y por causa exacta/incorrecta/ausente. Definir una partición mutuamente excluyente cuya suma pueda auditarse; PARTIALLY_IDENTIFIED no se debe contar simultáneamente como abstención genérica y como causa incorrecta. |
| AR-15 | MAYOR | Métricas permitidas y salidas | `_ALLOWED_METRICS` contiene `abstention_rate`, métricas Evaluator y `point_rmse`, mientras §362 propone `not_identified_rate`, `indeterminate_rate`, `point_mse` y `interval_joint_success_rate`; estas nuevas métricas no tienen IDs/versions ni contrato completo en el código. | Cerrar el catálogo de métricas y sus IDs/versions antes del manifiesto. Mantener alias antiguos solo como compatibilidad explícita, nunca como equivalencias semánticas implícitas. |

### 363.3 Revisión específica de los cinco puntos anunciados

1. **Selección por identificación:** resuelta condicionalmente. `θ_rep` es un estimando legítimo para intentos identificados, no una medida incondicional de calidad. `θ_world` queda como diagnóstico dependiente de R, no como estimando primario comparable entre grids.
2. **MCSE ratio:** fórmula aceptable como estimador asintótico cluster bajo IID entre M, denominador esperado positivo y protocolo R fijo. Falta validación independiente algebraica y de cobertura; no hay evidencia para afirmar que M=100 basta.
3. **Intervalos:** denominadores propuestos correctos y no intercambiables. Falta contrato de método/nivel de confianza, éxito conjunto y separación explícita de outputs inválidos/missing del ledger técnico.
4. **Manifiesto:** no supera revisión. Falta universo normativo exhaustivo, obligatoriedad, separación Analyzer/Evaluator y solución al hash autorreferencial.
5. **Equivalencia:** solo se puede afirmar para valores y métricas compartidas bajo casos completos específicos. La semántica nueva para abstenciones parciales/intervalos ausentes es deliberadamente distinta; no existe aún oráculo independiente ni suite que la demuestre.

### 363.4 Reconciliación con decisiones históricas y recomendación

- Se conserva la arquitectura focal N×M×R de §357.2; no se importa RUN ni el benchmark V_cont 13×52.
- Se conserva la advertencia de §357.3: precisión Monte Carlo no equivale a calidad del estimador, y R no sustituye M.
- Se mantiene la separación entre recuperación, abstención, adjudicación Evaluator y cobertura lógica ya exigida en §357.4.3–6 y §355.4.
- Se propone corregir explícitamente la convención `NOT_EVALUABLE` de §357.4.6 a `NOT_APPLICABLE` cuando el estimando/métrica no está definido para la clase estructural; no se presenta como decisión histórica ya congelada.
- No se aprueba aún `θ_rep`, el Metric Registry, targets, tolerancia científica, N/M/R ni el cambio de aplicabilidad. Este informe es una revisión técnica; no sustituye una decisión científica del usuario.

**Recomendación:** no implementar todavía. La siguiente iteración debe revisar y corregir el propio contrato §362 incorporando AR-01…AR-15, con especial prioridad a separar clase de verdad y disposición Analyzer, definir el universo de métricas y targets sin autorreferencia, y cerrar el ledger Evaluator. Después se redactará una versión consolidada del contrato y su oráculo de pruebas; solo entonces se podrá plantear implementación.

### 363.5 Disposición de control

No se modificó `theta_a_calibration_protocol.py`, tests, DGP, Analyzer, Evaluator, workflow, seed plan, roster, targets ni tolerancias. No se ejecutaron tests, EP-02, calibración, Monte Carlo ni evaluación. No se generaron bancos. `main`, RMA v3.38, Matrix v1.47, STATUS y TGCV Core permanecen intactos; PR #116 sigue Draft. Se mantienen `calibration_authorized=false`, `execution_authorized=false`, `scientific_execution=false`.

**Siguiente operación:** producir §364 como revisión corregida de §362, sin código: separar truth/disposition, fijar el catálogo y el manifiesto no circular, completar métricas de intervalo/abstención/Evaluator y establecer el protocolo de contraste pareado entre escenarios de world_family.


## 364. Contrato estadístico corregido del agregador θ_A — revisión de diseño posterior a AR-01…AR-15 (2026-11-18)

**Estado:** REVISED_CONTRACT_PROPOSAL / STATIC_ONLY / NOT_APPROVED / NOT_IMPLEMENTED / NO_CALIBRATION.  
**Precedencia:** esta sección es una propuesta de sustitución conceptual de §362 tras la revisión §363. §362 y §363 se conservan como antecedentes auditables; no se reescriben. Ninguna decisión científica se considera aprobada por el mero hecho de formularse aquí.  
**Ámbito:** protocolo focal θ_A, cinco escenarios candidatos y estructura N×M×R. No se incorpora el benchmark V_cont 13×52 ni un RUN separado.

### 364.1 Principios que corrigen el contrato anterior

1. **Dos planos de resultado, nunca un score único implícito.** (A) rendimiento condicional entre intentos donde el Analyzer identifica y emite un punto válido; (B) comportamiento operacional sobre todos los intentos planificados: identificación, abstención, indeterminación, identificación parcial, salida inválida y fallos técnicos. No se permite presentar A como calidad global sin acompañarlo de B.
2. **Verdad DGP y salida del Analyzer son variables diferentes.** La primera describe la identificabilidad estructural del estimando bajo el contrato causal/DGP. La segunda describe qué hizo el Analyzer con la información efectivamente observada. No se deduce una de la otra.
3. **Integridad del ledger precede a cualquier métrica.** El universo de intentos esperados viene del seed plan firmado/versionado. La ausencia, duplicidad, fingerprint discordante o output inválido no se convierte en abstención estadística.
4. **Precisión Monte Carlo, calidad del estimador y corrección causal son juicios distintos.** MCSE pequeño no significa bias pequeño; recuperar la verdad del DGP sintético no valida por sí solo la identificación causal fuera de ese DGP.
5. **Métrica, aplicabilidad y target se definen antes de observar resultados.** Ningún resumen puede inventar su propio universo de métricas a partir de las filas disponibles.

### 364.2 Modelo de datos: verdad, régimen de información, disposición y ledger

Cada escenario versionado declara, como mínimo, cuatro campos independientes:

- `truth_identification_class`: propiedad del estimando bajo el DGP y población objetivo; valores admitidos inicialmente `IDENTIFIED`, `NOT_IDENTIFIED` y `PARTIALLY_IDENTIFIED`. El valor procede de un contrato estructural verificable y no de la salida Analyzer.
- `information_regime_id/version`: régimen de observación/medición/soporte realmente disponible al Analyzer. Puede ser completo, imperfecto o adversarial; no redefine retrospectivamente la clase de verdad.
- `expected_analyzer_disposition`: expectativa normativa del escenario/fixture, cuando exista; valores `IDENTIFIED`, `NOT_IDENTIFIED`, `INDETERMINATE`, `PARTIALLY_IDENTIFIED`. Es una expectativa de conformidad, no verdad del DGP ni un criterio para excluir observaciones.
- `expected_abstention_cause`: causa tipada exacta cuando la disposición esperada exige abstención; nula cuando no aplica. La causa observada se registra separadamente.

Cada réplica registra:
- `analyzer_disposition_observed` y `analyzer_cause_observed`;
- `point_estimate` si y solo si el Analyzer emite estimación puntual válida;
- intervalo inferencial con método, nivel, límites y estado de emisión/validez;
- adjudicación independiente del Evaluator, incluyendo disposition, bounds lógicos, cobertura del intervalo inferencial cuando corresponda y recuperación puntual;
- identidad completa de escenario, versión, N, M, R, world_id, run_id, seeds/fingerprints y versiones de Analyzer/Evaluator.

Los estados de ledger son una dimensión externa y mutuamente excluyente: `VALID_RESULT`, `TECHNICAL_FAILURE`, `OUTPUT_INVALID`, `RECORD_MISSING`. Un registro duplicado, inesperado o con identidad discordante es un fallo de integridad del banco, no una quinta categoría resumible. El estado Analyzer solo existe dentro de `VALID_RESULT`.

**Regla de población:** el análisis de conformidad del Analyzer compara `analyzer_disposition_observed` con `expected_analyzer_disposition`; el análisis de rendimiento compara la disposición observada con `truth_identification_class`. No se usa la expectativa del fixture como sustituto de la verdad ni se confunde una expectativa incumplida con un cambio de identificabilidad.

Para los cinco escenarios focales actuales, la clasificación candidata es cuatro `IDENTIFIED` y uno `NOT_IDENTIFIED`. `INDETERMINATE` y `PARTIALLY_IDENTIFIED` permanecen como salidas adversariales del Analyzer y controles de contrato; no se inventa un sexto escenario ni se les asigna verdad DGP sin un perfil tipado nuevo. Si un futuro DGP tiene verdad parcialmente identificada, deberá declararlo explícitamente y definir sus métricas de conjunto/cotas antes de incorporarse al roster.

### 364.3 Integridad del banco y denominadores operacionales

Para cada clave esperada del seed plan debe existir exactamente un estado ledger. Hard gate:
- cobertura exacta del conjunto de claves esperado;
- sin duplicados, extras ni ausencias;
- identidad y fingerprints coherentes;
- versiones homogéneas dentro del banco;
- todo resultado marcado VALID_RESULT pasa el esquema completo de réplica.

Si falla, el resumen científico del banco es `INVALID_LEDGER`; no se computan PASS ni métricas como si el banco estuviera completo. Puede emitirse un informe técnico de los fallos observados, pero no imputar una salida Analyzer a intentos sin resultado.

Se reportan por escenario×N las proporciones operacionales de ledger `VALID_RESULT`, `TECHNICAL_FAILURE`, `OUTPUT_INVALID` y `RECORD_MISSING`, siempre sobre el total de intentos esperados M×R, además de conteos absolutos. Estas tasas son métricas de integridad/ejecución del sistema, no de identificabilidad causal del Analyzer. Para resultados válidos, toda tasa de disposición Analyzer usa R por mundo como denominador y se agrega con igual peso por mundo.

### 364.4 Catálogo normativo de métricas

El catálogo se versiona independientemente del código y contiene para cada métrica: ID/version, fórmula, unidad, población objetivo, aplicabilidad por clase de verdad, agregación, método MCSE, dirección, target opcional/obligatorio y fuente de truth. No se permite que el agregador añada o elimine métricas dinámicamente.

**A. Tasas de disposición del Analyzer — aplicables a toda clase de verdad**

Para cada mundo m, cada estado observado es mutuamente excluyente:
- `analyzer_identified_rate`;
- `analyzer_not_identified_rate`;
- `analyzer_indeterminate_rate`;
- `analyzer_partially_identified_rate`.

Cada numerador es el número de réplicas válidas con ese estado y el denominador R. Las cuatro tasas suman 1. También se informa `point_emission_rate` y `valid_inference_interval_emission_rate`, que no se deducen automáticamente del estado si el contrato permite una salida sin punto/intervalo.

**B. Rendimiento puntual condicional — solo verdad IDENTIFIED**

Sea I_mr=1 si la réplica válida tiene disposición IDENTIFIED y estimación puntual finita; e_mr = estimación − verdad reservada; B_m=Σ_r I_mr.

- Bias condicional por intento identificado: θ_bias = Σ_mr I_mr e_mr / Σ_m B_m.
- MAE condicional: θ_MAE = Σ I|e| / Σ B.
- MSE condicional: θ_MSE = Σ I e² / Σ B.
- Point recovery condicional: Σ I·1(|e|≤δ_science) / Σ B, solo cuando δ_science está aprobado, versionado y vinculado al estimando.

Se reportan también distribuciones por mundo, B_m, B_m/R, errores por mundo y número de mundos con B_m=0. El primario propuesto es ratio agrupado por intento identificado, `θ_rep`; su nombre en los resultados debe incluir el calificativo `conditional_on_identification`. Es post-selección y no se interpreta como rendimiento operacional total.

`θ_world` = media de ratios por mundo con B_m>0 puede conservarse como diagnóstico exploratorio dependiente de R, acompañado por M elegibles, M con B_m=0 y distribución de B_m/R. No es target confirmatorio, no selecciona N/M/R y no se compara entre diseños R como si mantuviera la misma población.

**C. Rendimiento inferencial de intervalos — verdad IDENTIFIED y método inferencial definido**

Sea J_mr=1 si se emitió un intervalo inferencial válido, con método y nivel preespecificados, límites finitos y ordenados y metadatos coherentes. Sea C_mr=1 si J_mr=1 y el intervalo contiene la verdad reservada. H_m=ΣJ_mr.

- Disponibilidad de intervalo válido: ΣJ/R por mundo; igual peso por mundo.
- Cobertura condicional entre intervalos emitidos: ΣC/ΣH, ratio agrupado por intervalo válido.
- Éxito conjunto de intervalo: ΣC/R por mundo; igual peso por mundo. Es la probabilidad operacional de emitir un intervalo válido que cubra la verdad en un intento planificado.
- Anchura condicional: ΣJ·width/ΣH, ratio agrupado por intervalo válido.

Disponibilidad, cobertura condicional, éxito conjunto y anchura contestan preguntas distintas. Un intervalo ausente reduce disponibilidad y éxito conjunto, pero no entra en el denominador de cobertura condicional. Output inválido, registro ausente y fallo técnico no se clasifican como intervalo ausente válido: bloquean integridad o se contabilizan en ledger técnico. La cobertura lógica de bounds del Evaluator para verdad NOT_IDENTIFIED no es cobertura inferencial y no entra en J ni C.

Para verdad NOT_IDENTIFIED, las métricas de error puntual y cobertura inferencial de un efecto identificado son `NOT_APPLICABLE`; la auditoría de bounds lógicos y las métricas de disposición/falsa identificación sí aplican. Para verdad PARTIALLY_IDENTIFIED, no se computa cobertura puntual de un parámetro único: se requiere un contrato separado de conjunto identificado y cobertura de conjunto antes de activar esas métricas.

**D. Error de disposición frente a verdad DGP**

Las métricas se calculan por clase de verdad, con denominador R por mundo y agregación de igual peso entre M:
- verdad IDENTIFIED: tasas de falsa abstención, desglosadas por Analyzer NOT_IDENTIFIED, INDETERMINATE y PARTIALLY_IDENTIFIED; falsa identificación no aplica.
- verdad NOT_IDENTIFIED: falsa identificación (Analyzer IDENTIFIED); abstención correcta solo cuando el Analyzer declara NOT_IDENTIFIED con la causa exacta esperada; abstención por causa incorrecta; abstención sin causa; disposición INDETERMINATE; disposición PARTIALLY_IDENTIFIED, todas separadas.
- verdad PARTIALLY_IDENTIFIED: métricas de disposición y cobertura de conjunto solo tras contrato propio; no equiparar automáticamente PARTIALLY_IDENTIFIED con abstención correcta.

Las categorías observadas forman una partición; las métricas agregadas no pueden contar una misma réplica simultáneamente como falsa abstención y causa incorrecta. Se publican conteos y denominadores para permitir comprobar que la partición cierra.

**E. Auditoría Evaluator — registro separado**

No pertenece al Metric Registry de rendimiento Analyzer. Por escenario/clase se registran separadamente:
- `evaluator_disposition_correct` respecto de la regla independiente aplicable;
- `evaluator_truth_within_logical_bounds` como invariante de dominio;
- `evaluator_inference_interval_covers_truth` solo para verdad IDENTIFIED y cuando existe intervalo inferencial válido;
- `evaluator_point_recovery_within_delta_eval` con δ_eval versionado;
- disposition y causa adjudicadas, y discrepancias Analyzer/Evaluator.

No se agrega `truth_within_logical_bounds` como cobertura nominal ni se mezcla `correct_adjudication` en un único porcentaje entre clases. δ_eval y δ_science son parámetros diferentes; si se comparan sus resultados, se muestran como auditorías separadas.

### 364.5 Agregación y MCSE

Para tasas operacionales, ledger y contribuciones escalares definidas en cada mundo, primero se calcula q_m con denominador R y luego:
`estimate = mean(q_m)`; `MCSE = sd(q_m)/(sqrt(M))`.
La unidad independiente es el mundo exterior M, no cada una de las M×R filas.

Para ratios condicionales θ=ΣA_m/ΣB_m, con B_m≥0 y ΣB_m>0:
`u_m = A_m − θ B_m`;
`MCSE_ratio = sd(u_m)/(sqrt(M) × mean(B_m))`.
Es un estimador asintótico cluster de primer orden, condicionado a mundos IID, protocolo de generación fijo, M≥2 y denominador esperado positivo. No es una garantía exacta de cobertura para M finito. Debe validarse con oráculo algebraico independiente, escenarios de denominador heterogéneo, correlación A/B, B_m=0 y distribuciones asimétricas. Si ΣB=0, la métrica aplicable es `NOT_EVALUABLE`, nunca cero ni PASS.

Los M mundos deben ser IID de una distribución generadora explícita para usar la interpretación inferencial anterior. Si el roster representa mundos fijos/no IID, el MCSE se interpreta únicamente como dispersión Monte Carlo bajo el mecanismo de seeds declarado, no como incertidumbre poblacional general. Esta distinción debe estar en el diseño y el informe.

**Contrastes pareados por world_family:** si dos escenarios comparten world_id basal y el diseño declara emparejamiento, no se calculan contrastes suponiendo independencia. Para diferencia de ratios θ_1−θ_0, la contribución de influencia pareada por mundo es:
`ψ_m = (A_1m−θ_1 B_1m)/mean(B_1) − (A_0m−θ_0 B_0m)/mean(B_0)`.
El MCSE del contraste es sd(ψ_m)/sqrt(M), sobre los mismos world_id emparejados y elegibles según regla preespecificada. La elegibilidad y el tratamiento de B=0 deben declararse antes del cálculo; si no hay emparejamiento completo, no se presenta como contraste pareado. Para tasas, se calcula primero diferencia por world_id y luego SD de esas diferencias entre M. Se reportan contraste, MCSE, número de pares y hashes de ambos escenarios.

### 364.6 Metric Registry y manifiesto no circular

Se proponen dos artefactos independientes y versionados:
1. **Metric Registry:** catálogo normativo de métricas, definiciones, unidad, aplicabilidad, fórmula, método MCSE, versión, familia (Analyzer performance / operational / ledger / Evaluator audit), y reglas de obligatoriedad.
2. **Target Manifest:** instancia de targets para un design fingerprint concreto.

Clave esperada del manifiesto:
`(scenario_id, scenario_version, N, metric_id, metric_version)`.
Cada entrada añade `required_for_calibration`, `applicability`, razón tipada, `target_status` (`TARGETED` / `NOT_TARGETED`), target MCSE si corresponde, unidad, método MCSE, δ_science cuando la métrica lo requiera, y referencias a Registry, estimand, outcome, DGP y design versions. M, R, distribución de mundos, confianza y política de extensión se enlazan desde el design fingerprint común; si varían por celda, pasan a formar parte de la clave.

El universo esperado se genera desde el Registry y el roster aprobado, nunca desde las filas observadas ni desde el propio manifiesto. La validación exige igualdad exacta de claves: no faltantes, duplicados ni extras. `NOT_APPLICABLE` requiere razón y prohíbe target. `NOT_TARGETED` no satisface una entrada obligatoria. Una entrada TARGETED exige target finito, positivo y unidad/método coincidentes. No se permite que una métrica de auditoría Evaluator se convierta accidentalmente en target de rendimiento Analyzer.

**Hash no circular:** canonicalizar el payload del manifiesto sin ningún campo de hash; calcular SHA-256 de esos bytes; guardar el digest en un envelope separado que contiene además el identificador/version del manifiesto. Ninguna fila contiene el hash del documento que la contiene. Registry y roster conservan sus propios hashes, enlazados en el envelope.

Estados de resultado:
- `NOT_APPLICABLE`: la métrica no está definida para esa clase/estimando;
- `NOT_TARGETED`: aplicable, sin target aprobado;
- `NOT_EVALUABLE`: aplicable, pero sin denominador, datos válidos o MCSE calculable;
- `FAIL_PRECISION`: target válido y MCSE superior al target;
- `PASS_PRECISION`: ledger íntegro, target obligatorio válido y MCSE no superior al target.

`PASS_PRECISION` no significa bias pequeño, cobertura adecuada, potencia suficiente ni validez científica. El PASS de calibración solo puede referirse a cumplimiento de todos los targets de precisión obligatorios; la aceptación científica requiere criterios de rendimiento separados (bias/MSE, cobertura, disponibilidad, abstención, MDE/potencia si se define un test) y decisión explícita.

### 364.7 Equivalencia histórica y pruebas oráculo

La equivalencia con el agregador previo se define por dominios:
- cuando todas las R son IDENTIFIED, todos los puntos/intervalos son válidos, R es fijo y el mismo estimando/verdad se usa, las medias por mundo de bias, MAE, point recovery, disponibilidad, cobertura y anchura deben coincidir con los valores del contrato histórico;
- RMSE debe coincidir como raíz del MSE correspondiente, pero el MCSE de RMSE no se identifica con el MCSE de MSE;
- con abstención parcial o intervalos ausentes válidos, el contrato nuevo debe producir métricas condicionales y operacionales con denominadores explícitos; el antiguo `NOT_EVALUABLE` all-R no es el resultado de referencia para estas nuevas definiciones;
- `NOT_APPLICABLE` sustituye prospectivamente a `NOT_EVALUABLE` cuando la métrica presupone un parámetro puntual identificable que la verdad DGP declara estructuralmente no identificado. Esta es una corrección propuesta de §357.4.6, no una decisión histórica ya aprobada. `NOT_EVALUABLE` se reserva para una métrica aplicable sin información suficiente para calcularla.

Oráculo independiente exigido antes de implementar:
1. construir tablas pequeñas de réplica a mano y calcular todas las métricas sin reutilizar funciones del agregador;
2. comprobar cierre de la partición de estados y ledger;
3. verificar denominadores R, ΣI y ΣJ en fixtures con abstención parcial e intervalos ausentes;
4. contrastar ratio MCSE con fórmula sandwich independiente y una simulación de cobertura/estabilidad;
5. verificar invariancia a permutación de filas y sensibilidad a cambios en R;
6. comprobar equivalencia histórica solo en el dominio completo indicado;
7. contrastar escenarios emparejados por world_id frente a cálculo independiente para mostrar el efecto de covarianza;
8. rechazar manifiestos con clave faltante/duplicada/extra, target incompatible, hash circular o entrada obligatoria NOT_TARGETED;
9. comprobar que δ_eval nunca se sustituye por δ_science ni viceversa;
10. verificar que truth logical bounds nunca se etiqueta como cobertura inferencial.

### 364.8 Decisiones pendientes y límites de autorización

Esta sección recomienda, pero no aprueba:
- θ_rep como métrica primaria de error condicional por intento identificado;
- θ_world como diagnóstico no confirmatorio;
- catálogo y separación de familias de métricas;
- definición de éxito conjunto y cobertura condicional;
- estructura Registry + Target Manifest;
- MCSE ratio asintótico y contrastes pareados;
- cambio prospectivo NOT_EVALUABLE → NOT_APPLICABLE para no identificación estructural.

Siguen sin decidirse/aprobarse: δ_science, targets concretos, obligatoriedad de cada métrica, criterio científico de recuperación, MDE/alfa/potencia, N/M/R, distribución IID de mundos, política de extensión M, roster congelado y diseño de evaluación independiente. Ninguna cifra de §336/348/357 se convierte en decisión por esta revisión.

No se modifica código, tests, DGP, roster, Analyzer, Evaluator, workflow, seeds ni bancos. No se ejecutan tests, calibración, Monte Carlo ni evaluación. No se altera main, RMA, Matrix, STATUS o TGCV Core. PR #116 permanece Draft. Se mantienen `calibration_authorized=false`, `execution_authorized=false`, `scientific_execution=false`.

**Siguiente operación:** revisión adversarial interna de §364 contra los tipos/funciones concretos del protocolo y contra los contratos de estimando DGP, centrada en comprobar que cada campo propuesto puede derivarse sin ambigüedad y que la partición de estados, aplicabilidad y contrastes pareados no introduce supuestos nuevos inadvertidos. Después de esa revisión se podrá preparar el contrato de oráculo y tests, todavía sin ejecutar calibración.


## 365. Revisión de derivabilidad de §364 contra los tipos, seed plan, runner, captura y agregador existentes (2026-11-18)

**Estado:** STATIC_ADVERSARIAL_REVIEW_COMPLETED / PARTIAL_DERIVABILITY / CONTRACT_AMENDMENTS_REQUIRED / NO_CODE_CHANGE / NO_EXECUTION.  
**Fuentes:** §364; `theta_a_calibration_protocol.py` blob `9675b9f6805b11f1a1037a3e4b2f95af53038e4c`; `test_theta_a_calibration_protocol.py` blob `a15454020c1043c1d5244193d8c8feb64d3442b9`; harness README blob `4f8a9bd506f91245699c1023a6354fe8676b20e2`; gobernanza canónica de main (README, Bootstrap, Canonical State, RMA v3.38). Revisión exclusivamente estática; no se ejecutaron pruebas ni funciones de generación/runner.

### 365.1 Dictamen

§364 corrige la arquitectura conceptual en la dirección adecuada, pero **no es todavía un contrato directamente derivable del modelo de datos y de los resultados que produce el código actual**. Se identifican seis brechas principales: truth/disposition aún fusionados en el tipo de escenario y del registro; ausencia de ledger de fallos por intento; semántica de intervalos sin método/versionado explícito; métricas de estados parciales no calculadas de forma transversal; falta de resumen pareado; y ambigüedad sobre qué unidad de análisis independiente sustenta la inferencia M.

La distinción fundamental es que §364 es un contrato futuro que requiere una migración de esquema y agregador, no una descripción de capacidades ya existentes.

### 365.2 Matriz de derivabilidad

| ID | Estado | Evidencia estática | Implicación / corrección requerida |
|---|---|---|---|
| DR-01 | BLOCKED | El alias `Identification` del módulo contiene IDENTIFIED, NOT_IDENTIFIED e INDETERMINATE. `ThetaACalibrationScenario.expected_identification` utiliza ese alias y `ThetaAReplicateRecord.expected_identification` reutiliza el mismo concepto. `PARTIALLY_IDENTIFIED` solo se admite en el conjunto de estados observados Analyzer, no como clase de verdad. | Implementar dos enums/campos distintos: verdad estructural DGP y disposición Analyzer esperada/observada. La clase de verdad INDETERMINATE del fixture de missingness actual debe migrarse a una clase de verdad estructural identificada/no identificada más un information_regime que causa indeterminación, o justificarse como una tercera verdad epistemológica con definición propia. No se puede mapear automáticamente. |
| DR-02 | BLOCKED | El test `test_pipeline_inference_options_follow_explicit_independence_contract` construye un escenario con `expected_identification="INDETERMINATE"` para missingness, aunque afirma independencia a nivel unidad y mantiene el confidence level. El agregador actual cae en la rama `else` de no identificado y calcula `correct_abstention_rate` / `wrong_cause_abstention_rate` usando la causa del perfil (nula si no hay perfil). | Confirmación directa de la mezcla que AR-07 detectó. El nuevo modelo debe representar truth class e information regime por separado y definir qué se espera del Analyzer bajo missingness; el caso no debe ser tratado como NOT_IDENTIFIED por el mero hecho de no ser IDENTIFIED. |
| DR-03 | BLOCKED | `run_theta_a_calibration_replicates` exige autorización explícita, llama secuencialmente al world_executor y propaga excepciones; devuelve registros solo si todos se capturan. `summarize_theta_a_calibration` exige igualdad exacta entre claves del seed plan y registros; cualquier missing/duplicado invalida la operación. No existe objeto por intento con estados TECHNICAL_FAILURE/OUTPUT_INVALID/RECORD_MISSING. | El ledger de §364 necesita una capa de orquestación/captura adicional con un resultado tipado por cada clave esperada, preservando excepción, etapa y causa. No debe convertir excepción en registro Analyzer ficticio. Mientras no exista, solo se puede informar integridad hard-fail; no se pueden estimar las cuatro tasas de ledger propuestas. |
| DR-04 | CONDITIONAL | `ThetaAReplicateRecord` contiene bounds, coverage boolean, width y requested confidence level; valida coherencia matemática y exige que un intervalo corresponda a Analyzer IDENTIFIED. La captura además exige cobertura S3 continua para el roster y seed por unidad. | Se pueden derivar J y C de los campos actuales bajo la validación existente. No se deriva aún método inferencial, versión del algoritmo, definición de sidedness ni referencia explícita al contrato de intervalo; el nivel solicitado no identifica por sí solo el método. Añadir `interval_method_id/version`, `interval_contract_sha256` y `interval_status`/reason; diferenciar intervalo no emitido de salida inválida. |
| DR-05 | BLOCKED | El resumen actual produce `identification_rate` y `abstention_rate` global, `false_abstention_rate` solo para verdad IDENTIFIED y métricas `correct_abstention_rate`, `wrong_cause_abstention_rate`, `partial_identification_rate`, `false_identification_rate` solo en la rama no IDENTIFIED. | §364 exige las cuatro tasas observadas como partición para toda clase de verdad, además de métricas de error por clase. El catálogo debe especificar la partición y calcularla siempre para cada escenario; la aplicabilidad de métricas de error se decide por truth class, no por la rama del código actual. |
| DR-06 | BLOCKED | `ThetaAReplicateRecord` guarda `evaluator_truth_within_bounds`, `evaluator_correct_adjudication` y `evaluator_disposition` como tripleta opcional. El resumen actual los agrega en las mismas métricas por mundo que el resto, sin un artefacto/ledger separado de auditoría. | Crear `EvaluatorAuditRecord/Summary` o una sección tipada independiente, con regla de adjudicación versionada por clase y causa. No reutilizar el Metric Registry del Analyzer. |
| DR-07 | BLOCKED | El agregador resume cada escenario independientemente; el seed validator sí exige identidad compartida de world/roster/seed para escenarios con el mismo `world_family_id`. No existe contraste pareado por familia/world_id en el resumen. | La identidad necesaria para pareamiento ya existe en SeedAssignment, pero la agregación cruzada falta. Añadir un contrato de contraste que verifique la bijección de world_id y M entre escenarios y conserve la covarianza. |
| DR-08 | CONDITIONAL | El seed validator comprueba M mundos con world_id/roster/seed distintos dentro de escenario×N y exige compartir identidad para una misma world_family×N×M. El escenario declara `unit_independence_certified` y su base; no hay un campo explícito que certifique IID de los mundos exteriores ni la distribución generadora de la que proceden. | La independencia de unidades dentro del mundo y la independencia/IID entre mundos son niveles diferentes. Añadir `outer_world_sampling_design_id`, distribución objetivo, mecanismo de muestreo, versión y certificación de independencia entre M. Sin eso, la fórmula de MCSE es descriptiva del mecanismo de seeds, no inferencia poblacional general. |
| DR-09 | BLOCKED | El diseño actual tiene `metric_targets` como tuplas opcionales, sin catálogo normativo, `required_for_calibration`, applicability manifest, ni comparación con un universo esperado. El código permite targets vacíos/parciales. | El Metric Registry y Target Manifest de §364 son nuevos artefactos requeridos. No hay derivación posible desde `metric_targets` actuales sin un contrato normativo externo. |
| DR-10 | BLOCKED | `_ALLOWED_METRICS` conserva `point_rmse`, `interval_coverage`, `interval_width`, métricas de abstención y Evaluator. El resumen usa internamente `point_rmse_mse`, calcula RMSE y una MCSE delta, y no expone MSE como métrica separada. | La nueva identidad point_MSE debe ser nueva métrica/version y nuevo target; no renombrar el output histórico. Interval metrics deben recibir IDs nuevos si cambian población/denominador. |
| DR-11 | CONDITIONAL | La clave `world_family_id` se conserva en SeedAssignment y el validador comprueba identidad común de mundo para la familia. El generador deriva la semilla de mundo a partir de family, world/DGP/roster versions, N y M; R tiene randomization_salt y S3 seed distintos. | Base suficiente para pareamiento de escenarios candidatos de la misma familia, siempre que DGP/version/roster comunes y emparejamiento completo se mantengan. No autoriza por sí solo una interpretación causal del contraste: ésta depende de qué mecanismo varía entre escenarios y qué se mantiene fijo en la DGP. |
| DR-12 | CONDITIONAL | El resumen actual calcula tasas como contribuciones por mundo y luego media/SD entre M. El seed plan fija el mundo en R y aleatoriza assignment y S3 por R. | La unidad exterior M está clara; sin embargo, definir si la inferencia objetivo es sobre la distribución de mundos o sobre el conjunto fijo de mundos. Si M no es IID de una distribución declarada, reportar MCSE de Monte Carlo bajo seed mechanism, no incertidumbre poblacional. |
| DR-13 | BLOCKED | `ThetaAReplicateRecord.validate` exige que un intervalo presente solo exista con Analyzer IDENTIFIED; si no hay bounds, coverage/width deben ser None. No contiene estado explícito de intervalo no emitido frente a intervalo inválido. | La definición J de §364 puede implementarse solo tras decidir el contrato de salida inválida. El fallo de validación debe ser ledger OUTPUT_INVALID, no intervalo ausente. No inferir J exclusivamente del estado Analyzer. |
| DR-14 | CONDITIONAL | El código conserva expected/observed abstention reason y el perfil DGP fija causa esperada para verdad NOT_IDENTIFIED. El resumen actual combina NOT_IDENTIFIED e INDETERMINATE en wrong-cause si no coincide causa exacta; PARTIALLY_IDENTIFIED se contabiliza separadamente. | La nueva partición propuesta debe preservar causa exacta/incorrecta/ausente y separar estados. Definir qué causas se esperan bajo truth IDENTIFIED y cómo se clasifica una abstención estructural frente a falta de información. |
| DR-15 | PASS_STATIC | El seed bank ya verifica cobertura exacta de escenarios×N×M×R, unicidad de filas, identidad fija dentro de R, diversidad entre M, streams disjuntos y world-family pairing. El summary también verifica que los registros coincidan exactamente con el plan y que truth/perfiles/fingerprints no deriven dentro de R. | La base de integridad y procedencia del plan se puede conservar; el nuevo ledger extiende el modelo para fallos de ejecución, no reemplaza estos controles. |

### 365.3 Dos correcciones conceptuales obligatorias antes de tests

**A. No confundir tres niveles de independencia.**
- `unit_independence_certified`: independencia de unidades dentro de cada mundo, relevante para la validez del estimador individual/SE que emite Analyzer.
- `outer_world_iid_certified`: independencia y muestreo IID de los M mundos desde una distribución objetivo, necesaria para la interpretación inferencial del MCSE entre mundos.
- `paired_world_family`: dependencia deliberada entre escenarios que comparten el mismo mundo; se conserva en contrastes pareados, no se trata como independencia entre escenarios.

La actual certificación de unidades no prueba IID de mundos. La fórmula MCSE §364.5 requiere que esa segunda certificación exista para cada design.

**B. Distinguir ausencia de intervalo y output inválido.**
- Analyzer puede no emitir intervalo de forma válida (por abstención o por contrato de no inferencia): J=0, siempre que el output completo sea válido.
- Analyzer declara/produce intervalo y viola esquema, límites, método o metadatos: OUTPUT_INVALID y hard-fail de ledger.
- No llega resultado: TECHNICAL_FAILURE o RECORD_MISSING según etapa y evidencia.
- Intervalo válido emitido: J=1; C=1 si cubre truth.

La actual dataclass permite representar ausencia con None y valida intervalos presentes, pero no lleva el estado/motivo tipado ni método/versionado. La distinción requiere ampliación de esquema.

### 365.4 Matriz de alcance del trabajo requerido

| Componente | Estado actual | Trabajo requerido |
|---|---|---|
| Seed plan N×M×R | Implementado y validado estáticamente | Conservar; añadir world-distribution contract |
| World-family pairing | Identidad compartida implementada | Añadir contraste pareado a resumen |
| Truth / Analyzer disposition | Fusionados parcialmente | Migración de schema + tests |
| Ledger de intentos fallidos | No existe | Nuevo wrapper de ejecución y registros tipados |
| Interval method identity | Parcial | Añadir método/version/hash y status |
| Métricas de disposición | Parciales/condicionadas por rama | Partición exhaustiva y transversal |
| Evaluator audit | Campos presentes, summary mezclado | Artefacto independiente |
| Metric Registry / Target Manifest | No existe | Nuevo artefacto normativo y validador |
| MSE condicional y MCSE ratio | No implementado | Nuevo agregador/oráculo |
| Contrastes pareados | Seed pairing implementado, summary ausente | Nuevo resumen por world_family |
| IID exterior M | No certificado | Contrato de muestreo de mundos |

### 365.5 Disposición y siguiente operación

La revisión **no aprueba §364 para implementación**. Los bloques DR-01, DR-03, DR-05, DR-06, DR-07, DR-09, DR-10 y DR-13 impiden derivar el contrato desde el código actual. DR-04, DR-08, DR-11, DR-12 y DR-14 son condicionales a nuevas identidades/contracts. DR-15 confirma que el seed-plan existente es una base sólida que no debe rehacerse.

Siguiente operación recomendada: producir §366 como *data contract and oracle specification* independiente del código, que defina esquemas exactos para TruthClass, AnalyzerDisposition, AttemptLedger, IntervalRecord, EvaluatorAudit, OuterWorldSamplingContract, Metric Registry, Target Manifest y PairedContrast. Después se elaborará la tabla de mapeo desde los dataclasses actuales al nuevo esquema y los casos de oráculo. No escribir aún el código ni ejecutar tests/calibración.

**Control:** no se modificó ningún archivo de código ni tests. No se invocaron builders de seed bank, world executor ni summarizer; no se generaron datos. No se ejecutaron tests, workflows, EP-02, calibración, Monte Carlo ni evaluación. main, RMA v3.38, Matrix v1.47, STATUS y TGCV Core permanecen intactos. PR #116 continúa Draft. `calibration_authorized=false`, `execution_authorized=false`, `scientific_execution=false`.


## 366. Data contract y especificación de oráculos para θ_A — versión de diseño independiente del código (2026-11-18)

**Estado:** DATA_CONTRACT_DRAFT / ORACLE_SPEC_DRAFT / STATIC_ONLY / NOT_APPROVED / NOT_IMPLEMENTED.  
**Precedencia:** §366 operacionaliza propuestas de §364 y hallazgos DR-01…DR-15 de §365. No convierte esas propuestas en decisiones científicas ni altera los contratos vigentes. §362–§365 permanecen como historial auditable.  
**Base inspeccionada:** protocolo `theta_a_calibration_protocol.py` SHA-256/blob `9675b9f6805b11f1a1037a3e4b2f95af53038e4c`; tests `test_theta_a_calibration_protocol.py` SHA-256/blob `a15454020c1043c1d5244193d8c8feb64d3442b9`; seed plan/runner/summary existentes y canonical state de main (RMA v3.38, Matrix v1.47).  
**Límite:** especificación de tipos, invariantes, transformaciones y oráculos. No modifica código, tests, escenarios, roster, targets ni workflows. No genera datos ni ejecuta pruebas.

### 366.1 Reglas de diseño y compatibilidad

1. **No reutilizar el enum actual `Identification` para dos constructos.** La compatibilidad nominal del enum actual no justifica su semántica dual.
2. **No inferir verdad estructural a partir de Analyzer, Evaluator, intervalo, causa de abstención ni resultado de un test.**
3. **No reinterpretar automáticamente el fixture actual `expected_identification=INDETERMINATE`.** Es una categoría heredada que requiere decisión de dominio. El contrato nuevo debe preservar el valor legacy y marcarlo `UNMAPPED_LEGACY` hasta que una ficha de escenario determine si describe verdad estructural, régimen informativo o expectativa de Analyzer.
4. **No añadir escenarios ni declarar que el roster tiene ya una verdad DGP distinta.** El mapeo de los cinco escenarios actuales es una tarea de reconciliación explícita, no una inferencia de esta especificación.
5. **Separar el resultado de cada intento del estado de integridad del banco.** Un fallo de ejecución no es una abstención del Analyzer.
6. **No tratar un intervalo no emitido como inválido ni un intervalo inválido como no emitido.**
7. **No asumir IID exterior M a partir de seeds diferentes, independencia de unidades o world-family pairing.**
8. **No considerar los targets opcionales actuales equivalentes a un Target Manifest exhaustivo.**
9. Los contratos siguientes son esquemas lógicos/versionados. Los nombres de campos se proponen como nombres normativos futuros; no afirman que existan en el dataclass actual.

### 366.2 Tipos normativos propuestos

**A. TruthClass — propiedad del estimando/DGP**

Valores:
- `IDENTIFIED_POINT`: el contrato estructural establece un único valor puntual del estimando para la población/soporte declarados.
- `NOT_IDENTIFIED_POINT`: el contrato establece que no existe un único valor puntual identificado bajo la información/soporte definidos.
- `PARTIALLY_IDENTIFIED_SET`: el contrato identifica un conjunto/cotas no degenerado, con operador y cobertura de conjunto definidos.
- `UNMAPPED_LEGACY`: valor transitorio de migración; no elegible para análisis científico ni PASS.

No se admite `INDETERMINATE` como TruthClass por defecto: indeterminación del Analyzer es una disposición; indeterminación epistemológica de la clasificación de verdad debe registrarse como `truth_class_status=UNRESOLVED`, que bloquea el escenario. Si el equipo decide que un DGP requiere una clase epistemológica adicional, debe aprobar una definición separada, con consecuencias métricas, antes de extender el enum.

Campos obligatorios del `TruthContract`:
`truth_contract_id/version`, `scenario_id/version`, `estimand_id/version`, `outcome_id/version`, `truth_class`, `truth_class_status`, `truth_value` (solo para IDENTIFIED_POINT), `identified_set` (solo para PARTIALLY_IDENTIFIED_SET), `target_population_id/version`, `support_contract_sha256`, `dgp_profile_sha256`, `derivation_reference`, `review_status`.

Invariantes:
- IDENTIFIED_POINT exige valor finito dentro del dominio declarado y prohíbe conjunto no degenerado.
- NOT_IDENTIFIED_POINT prohíbe declarar un truth puntual como parámetro identificado; puede conservar un valor generador/oráculo interno solo en campo separado `latent_generator_parameter`, marcado no identificado y no usado como truth para error puntual.
- PARTIALLY_IDENTIFIED_SET exige límites/representación del conjunto, regla de pertenencia, fuente estructural y futura métrica de cobertura de conjunto. Hasta definirlas, métricas de punto e intervalo convencional quedan NOT_APPLICABLE.
- UNMAPPED_LEGACY o UNRESOLVED bloquea cualquier resumen confirmatorio.

**B. InformationRegime — información accesible al Analyzer**

Campos: `information_regime_id/version`, `observation_process_id/version`, `missingness_mechanism`, `measurement_contract_sha256`, `support_observed_sha256`, `information_available_to_analyzer_sha256`, `regime_status`.

Este objeto caracteriza observación, medición, disponibilidad, missingness y soporte entregados al Analyzer. No cambia por sí solo TruthClass. Su relación con la identificabilidad debe estar demostrada en el contrato causal del estimando: una limitación informativa puede hacer que el estimando no sea identificable bajo el régimen observado, pero esa conclusión se registra como resultado de una regla estructural explícita, no se infiere de que Analyzer se abstenga.

**C. AnalyzerDisposition — salida observada**

Valores mutuamente excluyentes:
- `IDENTIFIED`
- `NOT_IDENTIFIED`
- `INDETERMINATE`
- `PARTIALLY_IDENTIFIED`

Campos: `disposition`, `abstention_cause_code` (nullable solo si el contrato permite ausencia de causa), `abstention_cause_detail` (opcional), `point_output_status`, `interval_output_status`, `analyzer_version`, `analyzer_contract_sha256`, `output_sha256`.

La disposición no sustituye los estados de emisión del punto/intervalo. Un Analyzer puede producir una disposición y, separadamente, no emitir intervalo por una razón contractual válida. La validez completa del output se comprueba antes de crear este objeto.

**D. ExpectedAnalyzerDisposition — expectativa del fixture**

Campos: `expected_disposition`, `expected_cause_code`, `expectation_basis_id/version`, `expectation_status`. Se usa para conformidad del Analyzer, nunca como truth. Debe existir una regla explícita por escenario/régimen o declararse no especificada. Una expectativa no especificada no se puntúa como fallo ni se rellena copiando TruthClass.

### 366.3 AttemptLedger — resultado por clave esperada del plan

Clave primaria lógica: `(design_id, design_version, bank, scenario_id, scenario_version, N, outer_world_id, R)`. El universo esperado procede del seed plan inmutable y versionado.

Estados exclusivos:
- `VALID_RESULT`: ejecución terminada, captura y validación completas; contiene un ReplicateResult.
- `TECHNICAL_FAILURE`: ejecución iniciada y fallida con evidencia de excepción/etapa/causa.
- `OUTPUT_INVALID`: hubo output, pero incumple schema, identidad, fingerprints, límites o contrato.
- `RECORD_MISSING`: no existe evidencia suficiente para decidir si se inició/terminó; no se imputa como fallo conocido ni como abstención.

Campos comunes: clave, `attempt_id`, `ledger_status`, `started_at`/orden monotónico si la infraestructura lo soporta, `completed_at` si aplica, `stage`, `error_code`, `error_fingerprint`, `executor_version`, `environment_fingerprint`, `seed_assignment_sha256`, `capture_schema_version`, `provenance`.

Invariantes:
- exactamente una fila por clave esperada;
- duplicados, claves extra, claves ausentes o fingerprints discordantes invalidan el ledger completo;
- TECHNICAL_FAILURE requiere evidencia de intento y fallo; RECORD_MISSING se reserva para falta de evidencia;
- OUTPUT_INVALID conserva fingerprint y diagnóstico del output defectuoso, sin convertirlo en AnalyzerDisposition;
- solo VALID_RESULT contiene ReplicateResult;
- un ledger incompleto produce `INVALID_LEDGER`, no una tasa científica imputada. Las proporciones de estados ledger se calculan solo si el universo esperado está completo y las cuatro categorías forman una partición exacta.

La implementación actual, que propaga excepción y exige igualdad exacta de records y assignments, se mantiene como hard-fail hasta que exista wrapper/ledger nuevo. No se debe introducir captura silenciosa de excepciones en el runner actual.

### 366.4 ReplicateResult y PointRecord

`ReplicateResult` enlaza, por referencias/hashes, TruthContract, InformationRegime, ExpectedAnalyzerDisposition, AnalyzerDisposition, IntervalRecord, EvaluatorAudit y SeedAssignment.

Campos mínimos: `attempt_key`, `truth_contract_ref`, `information_regime_ref`, `expected_disposition_ref`, `observed_disposition`, `observed_cause`, `point_record`, `interval_record`, `evaluator_audit_ref`, `world_id`, `run_id`, `estimand/outcome IDs+versions`, y todos los fingerprints ya exigidos por ThetaAReplicateRecord.

`PointRecord`:
- `point_status`: `EMITTED_VALID`, `NOT_EMITTED_VALID`, `OUTPUT_INVALID`.
- `estimate`: finito si EMITTED_VALID; nulo en los otros estados.
- `point_method_id/version`, `point_contract_sha256`.
- EMITTED_VALID exige AnalyzerDisposition IDENTIFIED y TruthClass IDENTIFIED_POINT para evaluación de error puntual confirmatoria.
- NOT_EMITTED_VALID puede coexistir con una disposición distinta de IDENTIFIED solo si el contrato Analyzer lo permite; si IDENTIFIED requiere punto, la ausencia es OUTPUT_INVALID.
- OUTPUT_INVALID no se conserva dentro de ReplicateResult: se registra en AttemptLedger.

### 366.5 IntervalRecord — no emisión frente a invalidez

Estados:
- `EMITTED_VALID`
- `NOT_EMITTED_VALID`
- `OUTPUT_INVALID` (solo como diagnóstico de ledger, no como intervalo válido dentro de ReplicateResult).

Campos cuando EMITTED_VALID: `lower`, `upper`, `nominal_confidence_level`, `interval_method_id/version`, `interval_contract_sha256`, `sidedness`, `construction_inputs_sha256`, `coverage_against_reserved_truth` (derivado independientemente, no suministrado como autoridad por Analyzer).

Reglas:
- límites finitos, lower≤upper, nivel 0<α_conf<1, método/version y contrato presentes;
- un nivel solicitado sin método no identifica el procedimiento inferencial;
- NOT_EMITTED_VALID exige razón tipada (`ABSTENTION`, `NO_INTERVAL_BY_METHOD`, `CONTRACTUAL_NONINFERENCE`, `OTHER_PREDECLARED`) y no contiene límites/cobertura/anchura;
- si el Analyzer afirma emisión pero faltan límites, método, nivel o coherencia, el ledger es OUTPUT_INVALID;
- J=1 solo para EMITTED_VALID; C=1 solo si J=1 y el intervalo contiene el truth reservado aplicable;
- para TruthClass NOT_IDENTIFIED_POINT o PARTIALLY_IDENTIFIED_SET, la cobertura de intervalo puntual no aplica; la cobertura de conjunto requiere un contrato separado.
  
El campo histórico `inference_covered` puede migrarse a una observación derivada de Evaluator solo tras verificar que representa cobertura del intervalo inferencial y no truth-within-logical-bounds. No se asume equivalencia semántica por el nombre del campo.

### 366.6 EvaluatorAudit — evidencia independiente y separada

Campos: `audit_id/version`, `attempt_key`, `evaluator_version`, `evaluator_contract_sha256`, `adjudicated_disposition`, `adjudicated_cause`, `adjudication_correct` respecto de una regla versionada, `logical_bounds_contract_ref`, `truth_within_logical_bounds`, `inference_interval_covers_truth` (nullable/no aplicable), `point_error_within_delta_eval` (nullable/no aplicable), `delta_eval_id/version`, `audit_evidence_sha256`.

Separación obligatoria:
- `truth_within_logical_bounds` es una invariante de soporte/consistencia lógica; nunca se etiqueta cobertura nominal.
- `inference_interval_covers_truth` solo aplica a TruthClass IDENTIFIED_POINT con IntervalRecord EMITTED_VALID.
- `point_error_within_delta_eval` es auditoría técnica respecto de δ_eval; no reemplaza δ_science.
- `adjudication_correct` se evalúa contra una regla independiente, con expectativas tipadas; no se reduce a la coincidencia literal con la salida Analyzer.
- El Evaluator no se convierte en árbitro de TruthClass por su propio resultado; la verdad se obtiene del TruthContract reservado.
- EvaluatorAudit se almacena y resume en familia independiente, no en el Metric Registry de Analyzer.

### 366.7 OuterWorldSamplingContract y PairedContrast

**OuterWorldSamplingContract** campos:
`sampling_design_id/version`, `target_world_distribution_id/version`, `sampling_frame`, `world_generation_mechanism_id/version`, `outer_world_unit_definition`, `iid_claim_status`, `independence_evidence_ref`, `seed_mechanism_id/version`, `M`, `world_family_policy`.

Estados de claim IID: `CERTIFIED_IID`, `DEPENDENT`, `FIXED_FINITE_SET`, `UNVERIFIED`. CERTIFIED_IID requiere fundamento de diseño; seeds distintos no son prueba suficiente. La independencia de unidades dentro de cada mundo se mantiene en contrato distinto (`unit_independence_certified`) y no se hereda entre niveles.

**PairedContrast** campos:
`contrast_id/version`, `scenario_a_ref`, `scenario_b_ref`, `world_family_id`, `N`, `paired_world_ids`, `pairing_contract_sha256`, `contrast_estimand_id/version`, `contrast_method_id/version`, `pair_count`, `unmatched_worlds`, `result`, `mcse`, `status`.

Invariantes:
- el emparejamiento exige una correspondencia uno-a-uno de world_id para el mismo N, world-family y versiones compatibles;
- el contraste identifica explícitamente qué componente del DGP varía y qué permanece fijo;
- si hay mundos sin pareja, no se presenta el contraste como completamente pareado; se aplica la regla de elegibilidad preespecificada o se declara NOT_EVALUABLE;
- si `iid_claim_status=DEPENDENT` o `FIXED_FINITE_SET`, el MCSE no se interpreta como inferencia IID poblacional; su alcance se declara;
- la fórmula de influencia pareada de §364 es candidata asintótica, no oráculo universal. Antes de adoptarla, se debe demostrar que A/B y la población de pares corresponden al estimando del contraste y fijar cómo tratar denominadores nulos. No se descartan pares post hoc según resultados.

### 366.8 Metric Registry y Target Manifest — contratos exactos

**Metric Registry Entry**:
`metric_id/version`, `family` (`ANALYZER_OPERATIONAL`, `ANALYZER_POINT`, `ANALYZER_INTERVAL`, `ANALYZER_DISPOSITION`, `LEDGER`, `EVALUATOR_AUDIT`, `CONTRAST`), `definition`, `unit`, `population`, `truth_class_applicability`, `formula_id/version`, `aggregation_id/version`, `mcse_method_id/version`, `direction`, `requiredness_policy_id/version`, `scientific_target_policy_ref`.

**Target Manifest Entry**:
`scenario_id/version`, `N`, `metric_id/version`, `applicability`, `applicability_reason_code`, `required_for_precision`, `target_status`, `target_value`, `target_unit`, `mcse_method_ref`, `delta_science_ref`, `registry_ref`, `truth_contract_ref`, `design_fingerprint`.

Clave base: `(scenario_id, scenario_version, N, metric_id, metric_version)`. Si M, R, confidence level o sampling design varían entre celdas, se incorporan al design fingerprint y se comprueba igualdad antes de comparar targets. El universo esperado se genera desde roster aprobado × N grid × Metric Registry × regla de aplicabilidad; el manifiesto no define su propio universo.

Valores `applicability`: `APPLICABLE`, `NOT_APPLICABLE`, `UNRESOLVED`. Valores `target_status`: `TARGETED`, `NOT_TARGETED`. `UNRESOLVED` bloquea. NOT_APPLICABLE requiere razón y no puede tener target. APPLICABLE + required_for_precision=true exige TARGETED y target finito/positivo compatible con unidad/método. NOT_TARGETED no satisface un requisito. La obligatoriedad científica y la de precisión son políticas distintas: un target MCSE no define el umbral de aceptación científica.

Hash: canonical JSON/bytes del payload sin digest, hash SHA-256 externo en envelope; registry, roster, truth contracts y design tienen hashes independientes. No se permite autorreferencia ni confiar en hash que el mismo payload pueda redefinir.

### 366.9 Oráculos independientes y fixtures mínimos

Los oráculos son tablas explícitas calculadas a mano o por implementación independiente, sin invocar funciones del agregador que se pretende verificar. Los resultados se fijan en fixtures versionados antes de implementar.

**O-01 — separación de constructos.** Caso heredado INDETERMINATE debe producir UNMAPPED_LEGACY y bloquear el resumen; no debe convertirse a NOT_IDENTIFIED ni PARTIALLY_IDENTIFIED por default.

**O-02 — partición Analyzer.** Para cada mundo, cuatro conteos de disposición observada suman exactamente R. Ejemplo R=8: [IDENTIFIED=3, NOT_IDENTIFIED=2, INDETERMINATE=2, PARTIALLY_IDENTIFIED=1], tasas [3/8,2/8,2/8,1/8]. No se evalúa todavía su corrección frente a TruthClass.

**O-03 — ledger.** Universo 4 intentos: dos VALID_RESULT, uno TECHNICAL_FAILURE y uno OUTPUT_INVALID; conteos cierran 4. Si falta una clave esperada, el ledger es INVALID_LEDGER y no se calcula la proporción como si la población estuviera completa.

**O-04 — missing vs invalid interval.** Un resultado válido sin intervalo bajo razón permitida produce J=0; un output que declara intervalo pero omite upper produce OUTPUT_INVALID; un intento sin registro produce RECORD_MISSING/INVALID_LEDGER, nunca J=0.

**O-05 — métricas de intervalo.** R=5, J=[1,1,0,1,0], C=[1,0,0,1,0], anchuras=[0.2,0.4,—,0.3,—]. Disponibilidad=3/5; cobertura condicional=2/3; éxito conjunto=2/5; anchura condicional=0.3. Las cuatro cifras deben salir de denominadores explícitos.

**O-06 — verdad no identificada.** TruthClass NOT_IDENTIFIED_POINT: point bias/MAE/MSE/recovery e intervalo puntual = NOT_APPLICABLE; falsa identificación, disposiciones y auditoría de bounds lógicos siguen aplicando. No se usa un truth puntual generador para calcular error del Analyzer.

**O-07 — denominador puntual cero.** TruthClass IDENTIFIED_POINT con B_m=0 en todos los mundos: métricas condicionales NOT_EVALUABLE; tasas operacionales sí calculables. Si B_m=0 en algunos mundos, se reportan esos mundos y se conserva el ratio agrupado preespecificado; no se ocultan.

**O-08 — ratio MCSE.** Para mundos sintéticos pequeños con A_m/B_m fijados, comparar ratio, residuos u_m y MCSE contra cálculo sandwich independiente; incluir B_m=0, denominadores heterogéneos y covarianza A/B. Verificar por simulación su cobertura/estabilidad solo en fase de test autorizada; no convertir esta especificación en ejecución ahora.

**O-09 — IID exterior.** M mundos con seeds distintos pero sampling status UNVERIFIED no pueden producir etiqueta de inferencia poblacional IID. El resultado puede etiquetarse descriptivo bajo seed mechanism.

**O-10 — pareamiento.** Dos escenarios con tres world_id compartidos: calcular diferencias dentro de cada mundo y MCSE entre diferencias. Reordenar filas no cambia resultado. Romper una pareja cambia status a no pareado/NOT_EVALUABLE según regla previa, nunca emparejar por posición de fila.

**O-11 — manifest.** Rechazar clave omitida, duplicada, extra, target obligatorio ausente, unidad/método incompatible, applicability UNRESOLVED, hash circular o roster sin aprobación. La lista esperada debe generarse desde Registry y roster independientes.

**O-12 — Evaluator.** truth_within_logical_bounds=true no puede activar interval_coverage. δ_eval y δ_science deben permanecer separados; cambiar uno no modifica el otro.

**O-13 — equivalencia histórica.** En fixture completo all-R identified, mismos inputs, estimand, verdad y ponderación, el nuevo agregador debe reproducir outputs históricos para las métricas equivalentes. MSE se verifica contra RMSE²; MCSE de RMSE no se iguala al de MSE. En fixtures con abstención, no se exige equivalencia con el antiguo hard-gate all-R.

**O-14 — identidad/fingerprints.** Cualquier deriva de scenario/DGP/profile/estimand/outcome/world/seed/version dentro de una unidad declarada produce fallo de integridad, no diferencia métrica.

**O-15 — orden e invariancia.** Permutación de filas y serialización canónica no alteran resultados ni hashes; cambio de R o de población de intentos debe cambiar denominadores conforme al contrato.

### 366.10 Mapeo preliminar desde el esquema actual

| Campo/tipo actual | Destino propuesto | Disposición |
|---|---|---|
| `ThetaACalibrationScenario.expected_identification` | TruthContract + ExpectedAnalyzerDisposition, tras revisión de cada escenario | No mapear automáticamente; INDETERMINATE queda UNMAPPED_LEGACY |
| `ThetaAReplicateRecord.expected_identification` | Referencia a TruthContract + expectativa | Campo duplicado a retirar tras migración validada |
| `analyzer_identification` | AnalyzerDisposition.disposition | Mapear con tabla exhaustiva de enums y causa |
| `truth` | TruthContract.truth_value solo para IDENTIFIED_POINT | Para NOT_IDENTIFIED conservar parámetro generador solo en campo separado, nunca como truth de error |
| `point_estimate` | PointRecord.estimate/status | Status ausente no equivale a error cero |
| `inference_lower_bound/upper_bound` | IntervalRecord | Añadir método, contrato, status y razón |
| `inference_covered` | Candidato a derivación independiente de cobertura | Verificar semántica real antes de mapear |
| `inference_width` | Derivable de upper−lower si intervalo válido | No usar como fuente primaria si contradice límites |
| `requested_confidence_level` | Nominal level | No sustituye método/versión |
| `expected_abstention_reason` | ExpectedAnalyzerDisposition.expected_cause_code | Requiere separar verdad de expectativa |
| `observed_abstention_reason` | AnalyzerDisposition.abstention_cause_code | Conservar código literal y mapping versionado |
| tripleta `evaluator_*` | EvaluatorAudit | Migrar a registro/summary separado |
| `ThetaASeedAssignment` | Referencia de AttemptLedger y Pairing identity | Conservar el seed plan actual |
| `metric_targets` | Target Manifest | No asumir exhaustividad ni obligatoriedad actual |
| `ThetaAMetricSummary` | Métrica versionada con denominadores y estado | Nuevo schema; preservar outputs legacy para comparación |
| `world_family_id/world_id` | PairedContrast | Identidad existente; contrastes aún no implementados |

### 366.11 Puertas de decisión antes de implementación

No iniciar implementación hasta que se completen, en este orden:
1. Reconciliar los cinco escenarios actuales: TruthClass, information regime, expectation, cause y fundamento estructural, incluyendo decisión explícita para el caso legacy INDETERMINATE.
2. Aprobar la política de intervalo: método, sidedness, nivel, emisión y no emisión permitida por disposición.
3. Definir la unidad objetivo de inferencia M: distribución IID, conjunto fijo o mecanismo Monte Carlo descriptivo; no basta con seeds distintos.
4. Aprobar catálogo de métricas, aplicabilidad y targets obligatorios; δ_science y criterios científicos quedan en decisión separada.
5. Definir captura/ledger sin pérdida de excepción ni conversión de error técnico en salida Analyzer.
6. Validar fórmula MCSE ratio y contraste pareado con derivación independiente y población elegible preespecificada.
7. Aprobar fixtures/oráculos y equivalencia histórica antes de modificar agregador.

**Siguiente operación:** §367, reconciliación escenario por escenario de los cinco escenarios focales y su verdad DGP/régimen informativo/expectativa Analyzer, contrastando perfiles DGP, soporte, independencia y pruebas existentes. La prioridad es resolver la semántica legacy INDETERMINATE y evitar una migración de etiquetas que cambie el significado causal. No ejecutar tests ni calibración.

**Controles y autorización:** solo se modificará este documento en la rama de investigación. No se modifican código/tests/DGP/roster/seeds/targets/workflows ni main/RMA/Matrix/STATUS/Core. No se ejecutan tests, EP-02, world executor, seed builder, calibración, Monte Carlo ni evaluación. PR #116 permanece Draft. `scientific_execution=false`, `execution_authorized=false`, `calibration_authorized=false`.


## 367. Reconciliación semántica de los cinco escenarios focales θ_A — revisión estática contra roster, protocolo y materializador DGP (2026-11-18)

**Estado:** SCENARIO_RECONCILIATION_STATIC / CANDIDATE_MAPPING / NOT_APPROVED / NOT_FROZEN / NOT_EXECUTED.  
**Precedencia:** §367 desarrolla la siguiente operación indicada en §366. No modifica el roster, el perfil DGP, los estimandos, las verdades históricas ni el Analyzer. La reconciliación distingue lo que declara el protocolo de lo que demuestra el materializador y de lo que aún debe adjudicarse mediante la integración reservada.  
**Fuentes contrastadas:** §§336, 348, 355, 360–366; `theta_a_calibration_protocol.py` (blob `9675b9f6805b11f1a1037a3e4b2f95af53038e4c`); `theta_a_calibration_dgp.py` (blob `e334ee62502a9bb012512305075a8b071fd8efed`); `test_theta_a_calibration_protocol.py` (blob `a15454020c1043c1d5244193d8c8feb64d3442b9`); `harness/README.md`. Revisión solo de contenido GitHub; no se ejecutó código ni test.

### 367.1 Resultado de la reconciliación del roster

El roster devuelto por `build_theta_a_candidate_scenario_roster()` contiene exactamente cinco escenarios: cuatro con `expected_identification=IDENTIFIED` y uno con `NOT_IDENTIFIED`. Ninguno de los cinco tiene `expected_identification=INDETERMINATE`. Esta precisión corrige cualquier lectura de §366 que pudiera atribuir el legacy INDETERMINATE a uno de los cinco escenarios.

| Scenario ID | Variante DGP | TruthClass candidata | Truth focal declarada | Soporte | Disposición Analyzer esperada candidata | Fundamento y límite |
|---|---|---|---:|---|---|---|
| `THETA_A_POSITIVE_V1` | `positive` | `IDENTIFIED_POINT` | +0.5 | `EQUAL` | `IDENTIFIED` | Contraste focal positivo bajo soporte fuente/objetivo igual y régimen común sin vía alternativa activa. La verdad +0.5 procede del contrato histórico §336 y del perfil; aún requiere concordancia con la verdad reservada del pipeline completo. |
| `THETA_A_NULL_V1` | `null` | `IDENTIFIED_POINT` | 0.0 | `EQUAL` | `IDENTIFIED` | Control nulo bajo soporte igual. Cero es el valor del contraste focal, no ausencia de identificación. Debe permanecer distinguido del escenario de vía alternativa común. |
| `THETA_A_NEGATIVE_V1` | `negative` | `IDENTIFIED_POINT` | −0.5 | `EQUAL` | `IDENTIFIED` | Contraste focal negativo bajo soporte igual. Verificar verdad reservada y simetría del mecanismo respecto al positivo; no inferir simetría solo por los nombres. |
| `THETA_A_ALTERNATIVE_COMMON_V1` | `alternative` | `IDENTIFIED_POINT` | 0.0 | `EQUAL` | `IDENTIFIED` | El componente alternativo está activo en ambos brazos; la regla funcional alternativa actúa antes de la regla focal, que solo se activa cuando el componente alternativo está ausente. El contraste focal se enmascara sin retirar soporte. No equivale al DGP null: representa una vía funcional alternativa común. |
| `THETA_A_TARGET_SUPPORT_NONIDENTIFIED_V1` | `positive_target_only` (materializada reutilizando la base `positive`) | `NOT_IDENTIFIED_POINT` | No declarada en `expected_theta_a_truth` | `TARGET_HAS_UNSUPPORTED_HISTORIES` | `NOT_IDENTIFIED`, causa `TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT` | Añade historia objetivo de masa 0.5 fuera del soporte fuente; las intervenciones se mantienen definidas y factibles, pero no hay propensión fuente para esa historia. La no-identificación se refiere a identificar el contraste en la población objetivo desde la información fuente, no a que el generador carezca de un parámetro latente. La verdad generadora sobre el objetivo completo debe enlazarse y auditarse separadamente; no rellenar el campo de truth identificada ni puntuar error puntual. |

Las cuatro verdades puntuales y su rol se conservan como **contrato candidato histórico de §336**, no como una nueva demostración. El quinto escenario amplía el roster de cuatro a cinco conforme a §348; no es un sexto tipo de mecanismo ni un nuevo estimando.

### 367.2 Separación de cuatro objetos que el código actual aún fusiona

1. **TruthClass:** propiedad del estimando bajo población objetivo, soporte y régimen de información formalmente definidos. La tabla anterior es un mapeo candidato de las clases históricas; la etiqueta no se deriva de la respuesta del Analyzer.
2. **ExpectedAnalyzerDisposition:** expectativa de conformidad del fixture. Para los cinco escenarios, el protocolo actual la expresa indirectamente mediante `expected_identification` y, en el quinto, `expected_abstention_reason`; todavía no existe un objeto independiente.
3. **Observed AnalyzerDisposition:** resultado real producido por Analyzer para cada réplica. No está demostrado por el roster ni por los tests de agregación que fabrican registros.
4. **EvaluatorAudit:** adjudicación independiente frente a la verdad reservada. No convierte una abstención correcta en identificación ni redefine TruthClass.

El campo actual `ThetaACalibrationScenario.expected_identification` sigue siendo una representación heredada que mezcla al menos clase esperada y expectativa de disposición. La migración futura debe preservar su valor histórico y añadir los contratos separados; no renombrarlo silenciosamente como TruthClass.

### 367.3 Qué significa exactamente el escenario target-only

El perfil candidato fija una historia objetivo exclusiva `TARGET-ONLY-HISTORY-001` con masa 0.5. El materializador:
- construye la población fuente base del modo positivo;
- reescala sus masas a la fracción soportada restante;
- añade la historia objetivo exclusiva con masa 0.5 y masa fuente 0;
- añade las políticas `g_A0/g_A1` y el certificado `r_common` para esa historia;
- deja su probabilidad de asignación fuente como `None`;
- materializa un estado funcional objetivo usando covariables ancla de una unidad fuente, con referencia de procedencia sintética explícita.

Por tanto, la causa estructural de no-identificación es la ausencia de soporte fuente para una masa positiva de la población objetivo, no la ausencia de definición de políticas ni la falta de materialización de potenciales. La reutilización de covariables ancla es una convención de fixture y no prueba representatividad de la historia objetivo; debe permanecer declarada como tal y no generalizarse.

El perfil quinto deja `expected_theta_a_truth=None`, mientras que el materializador selecciona el modo base `positive`. Esto es coherente con no publicar una verdad puntual identificada al Analyzer, pero deja una obligación de auditoría: la verdad generadora reservada sobre el q_X* completo debe conservarse en el TruthBundle/Evaluator y verificarse contra una derivación independiente. Hasta entonces, la cifra latente exacta es **NOT_VERIFIABLE en esta reconciliación estática**. §348 permite afirmar que tal contraste DGP puede existir; no autoriza a copiar +0.5 en el campo de verdad identificada del escenario quinto.

### 367.4 Régimen informativo, independencia y límites de interpretación

- Los cuatro escenarios con soporte `EQUAL` declaran `unit_independence_certified=True` y documentan independencia de historias potenciales y draws de asignación por unidad, sin interferencia. Es una declaración del contrato del diseño que debe seguir vinculada al generador y a las dos etapas de asignación; no certifica por sí misma IID de mundos exteriores M.
- El quinto escenario declara independencia por unidad como no certificada. No debe usarse la opción de intervalo/SE que exige esa certificación; el protocolo retira el nivel de confianza solicitado para ese escenario.
- El canal de observación de intervalo de la fábrica es deliberadamente ideal, completo y de cobertura continua; la ruta point-S3 es un fixture adversarial distinto. La fábrica ideal no valida medición pasiva imperfecta ni sus propiedades de missingness.
- El escenario de vía alternativa común mantiene soporte igual. Su truth focal cero no debe clasificarse como no-identificación, ni su ruta alternativa como fallo de positividad.
- El escenario target-only no es el caso benigno fuente-superset/objetivo-subset. Este último sigue siendo una regresión separada y abierta en §348.2.

### 367.5 Reconciliación del legacy INDETERMINATE

El test de opciones de inferencia construye un escenario sintético adicional con `expected_identification=INDETERMINATE` para verificar que el protocolo aún puede pasar confianza 0.95 cuando `unit_independence_certified=True`. Ese objeto no forma parte del roster de cinco. También existen fixtures de point-S3 y N=1 para probar abstenciones por falta de continuidad o de brazo observado; §336.2 los excluye expresamente del roster numérico de primera ola.

Conclusión: `INDETERMINATE` debe permanecer como categoría legacy/observada del Analyzer en los contratos que ya la contienen. No hay base para convertirla en TruthClass ni para asignarla a ninguno de los cinco escenarios focales. Para esos fixtures auxiliares, la verdad estructural y la disposición esperada siguen sin estar reconciliadas individualmente: `UNMAPPED_LEGACY` hasta una decisión específica, sin bloquear por ello la clasificación ya tipada de los cinco escenarios candidatos.

### 367.6 Bloqueos residuales antes de implementación

1. Verificar la verdad focal reservada para los cuatro escenarios identificados contra una derivación analítica independiente del DGP, y registrar por separado ITT-D2 de paquete.
2. Exponer y auditar la verdad generadora latente del escenario target-only sin presentarla como parámetro identificado desde la fuente.
3. Separar formalmente TruthClass, ExpectedAnalyzerDisposition, Observed AnalyzerDisposition e EvaluatorAudit en el contrato de réplica.
4. Reconciliar la unidad ancla usada para materializar la historia objetivo exclusiva y justificar su papel en la población sintética, sin asumir que una covariable copiada equivale a muestreo independiente.
5. Mantener el test source-superset/target-subset como regresión independiente; no inferir que queda cubierto por el quinto escenario.
6. Vincular la certificación de independencia de unidades a los generadores y asignadores efectivos; definir aparte el contrato de muestreo de mundos M.
7. Mantener separados el canal ideal continuo y los fixtures point-S3/missingness; no usar los últimos como escenarios confirmatorios sin contrato de verdad/régimen.

**Dictamen:** el mapeo de las cinco filas a las clases candidatas queda **CONDITIONAL**. La semántica del legacy INDETERMINATE queda **NOT_MAPPED / NOT_REINTERPRETED**. La verdad latente del target-only queda **NOT_VERIFIABLE** con los campos estáticos del perfil actual. La implementación end-to-end de los cinco escenarios y la adjudicación real Analyzer/Evaluator no se han ejecutado. §367 no congela el roster ni autoriza implementación, calibración o evaluación.

**Siguiente operación conforme a la misión §325:** no abrir otra capa documental genérica. Cerrar en el código existente —sin ejecución— la trazabilidad de verdad reservada del target-only y la correspondencia de las cinco configuraciones DGP con el pipeline completo; después priorizar la integración y los tests de software ya definidos, manteniendo separadas las autorizaciones para tests, dispatch, calibración y ejecución científica. No reabrir §367 salvo discrepancia concreta de código/contrato.

**Controles:** solo se actualiza este documento en `research/c10-s-consolidation-draft`. No se modifican código, tests, roster, targets, seeds, workflows, main, RMA, Matrix, STATUS, Core ni claims. No se ejecutan tests, EP-02, builders, calibración, Monte Carlo ni experimento científico. PR #116 permanece Draft. `scientific_execution=false`, `execution_authorized=false`, `calibration_authorized=false`.


## 368. Auditoría estática de la ruta de verdad reservada target-only — linaje y brecha de validación numérica (2026-11-18)

**Estado:** STATIC_LINEAGE_AUDIT / TRUTH_PATH_PRESENT / NUMERIC_ORACLE_VALIDATION_OPEN / NOT_EXECUTED.  
**Relación con §367:** esta sección corrige y precisa §367.3. La frase «verdad latente exacta NOT_VERIFIABLE» no debe interpretarse como ausencia de generación de verdad reservada: el pipeline sí calcula una verdad V_CONT sobre el q_X* ampliado. Lo que no está verificado es que el valor numérico calculado para el perfil target-only coincida con una derivación analítica independiente y preespecificada.

**Fuentes y blobs revisados:**
- `c10s_world_pipeline.py`: `eee0b0e4148d7c4acb90a6c6c7c58b8d82800978`.
- `c10s_functional_history.py`: `003938b3113aef345cf2de5e7f0d50b58fd1d1be`.
- `c10s_synthetic_components.py`: `e1fcb152f2b1fd6ad3ea8ccd20c2163dc44c4666`.
- `theta_a_evaluator.py`: `43c6715219114eaf1e0ac9eeb7e304939c7ae99b`.
- `theta_a_calibration_dgp.py`: `e334ee62502a9bb012512305075a8b071fd8efed`.
- `theta_a_calibration_protocol.py`: `9675b9f6805b11f1a1037a3e4b2f95af53038e4c`.
- `test_c10s_world_pipeline_integration.py`: `0cf51e0cbf8e56a7dcbf7b37892b3f708161eeb2`.

### 368.1 Linaje efectivo de la verdad reservada

La revisión estática reconstruye la siguiente cadena:

1. `configure_target_only_support_fixture()` construye el q_X* objetivo: reduce proporcionalmente las masas fuente a 0.5 y añade `TARGET-ONLY-HISTORY-001` con masa objetivo 0.5 y masa fuente 0.
2. Añade para esa historia las dos políticas conjuntas `g_A0/g_A1`, su certificado `r_common`, los vectores factibles, el estado funcional inicial y un `SyntheticThetaATargetHistory` tipado.
3. `materialize_c10s_complete_world_from_dgp()` comprueba que hay exactamente una materialización para cada historia exclusivamente objetivo; valida sus anclas X/H0/C_c, la unidad potencial y el estado funcional inicial. La historia objetivo recibe el ID sintético `TARGET-ONLY-UNIT-001`, pero no se añade a `world.units`.
4. `generate_g_a_event_history_potentials()` genera las historias potenciales G_A para el soporte fuente más el soporte target-only, usando el mapa explícito de unidades y estados iniciales. El generador exige cobertura exacta de historias, políticas y certificados.
5. `materialize_c10s_complete_world()` restringe políticas, certificados, vectores factibles e historias potenciales al q_X* objetivo y llama a `compute_theta_a_vcont_truth_from_event_histories()`.
6. El oráculo valida las identidades historia/unidad, las políticas, el régimen común, el soporte temporal y la integridad de cada EventHistory; adjudica V_CONT por historia/política y calcula el contraste estandarizado con las masas q_X* explícitas. La verdad resultante se almacena en `ThetaAVContTruthBundle`, con `evaluator_only=True` y manifiesto de EventHistory.
7. El Analyzer recibe únicamente la evidencia S3 sellada y el contrato de análisis. El Evaluator recibe además `ThetaAVContTruthBundle`; comprueba su rol reservado, los fingerprints q_X*/políticas, la evidencia, el resultado del Analyzer y el soporte estructural.

**Conclusión de linaje:** la verdad numérica target-only sí se genera a partir de las EventHistory potenciales del soporte objetivo completo y llega al Evaluator. No se pasa el objeto de verdad al Analyzer. La separación de canal está implementada en la composición estática del pipeline; no se declara aquí una verificación dinámica de ausencia de filtración.

### 368.2 Qué demuestran y qué no demuestran los tests existentes

La integración existente contiene dos rutas útiles:
- Un fixture target-only que combina historia sin soporte objetivo con fallo de positividad en otra historia fuente.
- `test_target_only_support_without_assignment_failure_abstains_end_to_end`, que aísla la causa target-only.

En la segunda ruta, el contrato de prueba comprueba, entre otros:
- cuatro unidades fuente y cuatro asignaciones, sin incorporar la unidad target-only al roster aleatorizado;
- diez EventHistory en el manifiesto de verdad (cinco historias objetivo por dos políticas);
- Analyzer `NOT_IDENTIFIED`, causa `TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT`, una historia ausente y cobertura objetivo 0.5;
- Evaluator `CORRECT_ABSTENTION`.

Esto acredita una ruta de generación/adjudicación y una abstención estructural coherente en el fixture. Sin embargo, el test de captura solo comprueba `-1 ≤ record.truth ≤ 1`, y los tests end-to-end comprueban `truth_within_bounds=True` y `correct_adjudication=True`, no la igualdad de la verdad reservada con un valor analítico target-only independiente.

### 368.3 Hallazgo: adjudicación de abstención no equivale a validación de la verdad

El Analyzer devuelve para la no-identificación los límites lógicos `[-1,1]`. En el Evaluator, tanto `truth_within_bounds` como `correct_adjudication` para `NOT_IDENTIFIED`/`INDETERMINATE` dependen de que la verdad reservada esté dentro de esos límites. Dado que el propio Evaluator exige previamente que la verdad esté en `[-1,1]`, esta condición es necesaria pero no discriminante: por sí sola no detecta una verdad target-only numéricamente incorrecta.

Por ello:
- `CORRECT_ABSTENTION` acredita que el Analyzer no publicó un punto y que los límites reportados contienen la verdad reservada; no acredita la exactitud numérica de esa verdad.
- `evaluator_truth_within_bounds_rate=1` en este caso no constituye una validación del valor de θ_A.
- La adjudicación estructural de la causa (soporte objetivo no cubierto) sí es una comprobación separada y útil.

### 368.4 Oráculo numérico que falta

El perfil `positive_target_only` reutiliza el generador funcional `positive`, conserva las mismas reglas G_A y añade una historia con el mismo estado funcional inicial. La construcción sugiere homogeneidad del contraste focal por historia y, por tanto, una verdad agregada candidata de +0.5 pese a la masa target-only. Pero el perfil mantiene deliberadamente `expected_theta_a_truth=None`, y el test no afirma esa igualdad.

No se elevará +0.5 a verdad confirmatoria solo por reutilización del nombre `positive`. Antes hay que derivar la expectativa desde las reglas y la adjudicación V_CONT, de forma independiente al oráculo que se está probando, y fijar una prueba que:
1. calcule analíticamente el contraste por historia bajo ambas políticas y el régimen común;
2. agregue con las masas target q_X* (incluida la masa 0.5 target-only);
3. compare el resultado con `ThetaAVContTruthBundle.theta_a_truth.theta_a_truth` y con `Evaluator.truth`;
4. compruebe que cambiar la historia/masa target-only según una perturbación controlada cambia la verdad agregada según la fórmula, sin dar esa verdad al Analyzer;
5. mantenga separado el hecho de que el parámetro generador existe del hecho de que no sea identificable desde la distribución fuente observada.

La unidad target-only usa covariables ancla copiadas de una unidad fuente y un estado funcional inicial explícito. La revisión confirma que esa materialización se valida, pero la regla funcional G_A actual opera sobre el vector conjunto y el estado funcional, no sobre una distribución independiente de X/H0/C_c. La población objetivo sintética queda así definida por una convención de anclaje; no debe presentarse como muestreo independiente o representatividad empírica de una población externa.

### 368.5 Dictamen y siguiente paso

| Propiedad | Dictamen estático |
|---|---|
| Historia target-only generada | IMPLEMENTED / PATH PRESENT |
| Historia target-only incluida en q_X* y en la verdad reservada | IMPLEMENTED / PATH PRESENT |
| Unidad target-only excluida del roster de asignación fuente | IMPLEMENTED / PATH PRESENT |
| Separación Analyzer / Evaluator truth | IMPLEMENTED BY INTERFACE / DYNAMIC NON-LEAKAGE NOT EXECUTED |
| Abstención por soporte objetivo | TEST SPECIFIED / NOT EXECUTED |
| Valor exacto de verdad target-only | GENERATED / INDEPENDENT NUMERIC VALIDATION OPEN |
| Homogeneidad y expectativa +0.5 | CANDIDATE / NOT APPROVED |
| Representatividad de anclas X/H0/C_c | SYNTHETIC CONVENTION / NOT CLAIMED |

**Siguiente trabajo técnico:** cerrar el oráculo analítico independiente target-only y su test de regresión. El test debe comprobar el valor numérico, no limitarse a `[-1,1]` ni a `truth_within_bounds`. Después, auditar que los cinco escenarios del roster tienen la misma cobertura de verdad reservada y que sus expectativas analíticas se contrastan con ella.

**Autorización y alcance:** esta revisión fue estática; no se ejecutaron tests, Analyzer, Evaluator, DGP, workflows ni calibraciones. No se modifican código, tests, perfiles, seeds, roster, workflows, RMA, Evidence→Claim Matrix, STATUS, Core ni `main`. Solo se añade esta sección al documento maestro de la rama `research/c10-s-consolidation-draft`. PR #116 permanece Draft. `scientific_execution=false`, `execution_authorized=false`, `calibration_authorized=false`.


## 369. Derivación analítica independiente de V_CONT para los cinco escenarios y target-only (2026-11-18)

**Estado:** ANALYTIC_DGP_DERIVATION / STATICALLY_DERIVED / NOT_YET_ENCODED_AS_TEST / NOT_EXECUTED.  
**Objetivo:** fijar expectativas numéricas a partir de las reglas generadoras y de la semántica de adjudicación, sin llamar al oráculo `compute_theta_a_vcont_truth_from_event_histories` para obtenerlas. Esta sección proporciona el valor esperado independiente contra el que podrá probarse dicho oráculo. No modifica el DGP ni aprueba una ejecución científica.

**Fuentes revisadas:** `theta_a_calibration_dgp.py` blob `e334ee62502a9bb012512305075a8b071fd8efed`; `c10s_functional_history.py` blob `003938b3113aef345cf2de5e7f0d50b58fd1d1be`; `c10s_synthetic_components.py` blob `e1fcb152f2b1fd6ad3ea8ccd20c2163dc44c4666`; `c10s_world_pipeline.py` blob `eee0b0e4148d7c4acb90a6c6c7c58b8d82800978`; `test_c10s_world_pipeline_integration.py` blob `0cf51e0cbf8e56a7dcbf7b37892b3f708161eeb2`.

### 369.1 Reglas de adjudicación que determinan el resultado

La regla funcional de cumplimiento es:
`compliant = (admission_behavior == ("ADMIT" if enabled else "NO_ADMISSION"))`.

El estado inicial de cada historia del fixture es `(enabled=True, admission=ADMIT)`, por lo que es compliant. La rejilla V_CONT contiene dos intervalos: [0,1) y [1,2]. La adjudicación es estricta y temporal:
- Un evento en t=1 no afecta al intervalo [0,1).
- El evento en t=1 sí se aplica al intervalo [1,2].
- Un cambio a `NO_ADMISSION` manteniendo `enabled=True` hace que el estado posterior sea non-compliant.
- Un cambio a `enabled=False` manteniendo `admission=ADMIT` también hace que el estado posterior sea non-compliant.

V_CONT por historia es la media de los dos indicadores de cumplimiento. Por tanto, una historia compliant en el primer intervalo y non-compliant en el segundo tiene V_CONT=1/2; una historia compliant en ambos tiene 1; una historia non-compliant en ambos tiene 0.

### 369.2 Derivación por escenario

Las políticas focales son deterministas. En los escenarios positivo, nulo y negativo:
- `g_A0=(0,0,0,0)`
- `g_A1=(1,0,0,0))

En `alternative`:
- `g_A0=(0,1,0,0)`
- `g_A1=(1,1,0,0))

La regla D2 de interrupción de admisión no se activa en la generación de potenciales `G_A`: el generador selecciona las reglas cuya fuente es `G_A` y no infiere V_CONT desde D2. La regla D2 común se mantiene fuera de esta derivación focal.

| Escenario | Potencial bajo g_A0 | V_CONT(g_A0) | Potencial bajo g_A1 | V_CONT(g_A1) | θ_A = diferencia |
|---|---|---:|---|---:|---:|
| positive | Regla focal en t=1: admission pasa a NO_ADMISSION; [0,1) compliant, [1,2] no | 0,5 | No se activa regla G_A; ambos intervalos compliant | 1 | **+0,5** |
| null | No hay reglas G_A; ambos intervalos compliant | 1 | No hay reglas G_A; ambos intervalos compliant | 1 | **0** |
| negative | No se activa la regla (1,0) en g_A0; ambos intervalos compliant | 1 | Regla focal en t=1; [0,1) compliant, [1,2] no | 0,5 | **−0,5** |
| alternative | En t=0,5 se deshabilita ENABLED manteniendo ADMIT; ambos intervalos no compliant | 0 | La misma regla alternativa en t=0,5; la regla focal no se activa porque la segunda coordenada vale 1 | 0 | **0** |

Esta derivación distingue el escenario nulo del alternativo: ambos contrastes son cero, pero el primero mantiene ambos brazos compliant; el segundo produce incumplimiento funcional en ambos brazos por la vía alternativa común.

### 369.3 Derivación del perfil positive_target_only

El materializador:
- toma el generador `positive`;
- escala cada masa fuente por `1-u`, con u=0,5;
- añade la historia target-only con masa u=0,5;
- añade para esa historia las mismas políticas deterministas `g_A0/g_A1`;
- le asigna el mismo estado funcional inicial `(True, ADMIT)`;
- conserva las mismas reglas funcionales y el mismo régimen `r_common`.

Como las reglas G_A del modo positivo solo dependen del vector y el estado inicial, no de X/H0/C_c ni del identificador de historia, cada historia soportada y la historia target-only tienen el mismo contraste focal analítico +0,5.

Sea q_s la distribución fuente normalizada y q_t la distribución objetivo ampliada:
Con distribución fuente normalizada q_s y distribución objetivo ampliada q_t:

- Para cada historia fuente h: q_t(h) = (1-u) × q_s(h).
- Para la historia exclusivamente objetivo h*: q_t(h*) = u.
- Para todas las historias objetivo de esta construcción: delta(h) = V(g_A1 | h) - V(g_A0 | h) = 0.5.

Por tanto:

`theta_A(q_t) = sum_h [(1-u) × q_s(h) × 0.5] + u × 0.5 = 0.5 × (1-u) + 0.5 × u = +0.5.`

Para u=0,5, la mitad de la masa objetivo está fuera del soporte fuente, pero el contraste generador sobre la población objetivo completa sigue siendo +0,5. La no-identificación desde la fuente y la existencia de una verdad generadora conocida son compatibles: la primera es una propiedad de la información/soporte observado; la segunda, del DGP reservado.

**Alcance de la conclusión:** +0,5 queda ahora justificado como expectativa analítica del perfil sintético actual, condicionado a la identidad de reglas, vectores, estado inicial, rejilla y pesos descritos. No es evidencia de que un estimador pueda recuperarlo desde la fuente. Tampoco valida representatividad externa de las anclas copiadas.

### 369.4 Contrato del test de oráculo independiente (especificación, no implementación)

El test futuro debe construir la expectativa sin invocar `adjudicate_intervals`, `compute_theta_a_truth` ni `compute_theta_a_vcont_truth_from_event_histories` para calcular el valor esperado. Puede ejecutar el pipeline bajo autorización separada y leer sus salidas reservadas solo después de fijar la expectativa analítica.

Aserciones mínimas:
1. Para positive: `theta_a_truth=+0.5` y contribución por historia `V(g_A0)=0.5, V(g_A1)=1.0, contrast=+0.5`.
2. Para null: `theta_a_truth=0.0` y contribuciones `1.0,1.0,0.0`.
3. Para negative: `theta_a_truth=-0.5` y contribuciones `1.0,0.5,-0.5`.
4. Para alternative: `theta_a_truth=0.0` y contribuciones `0.0,0.0,0.0`.
5. Para positive_target_only: verificar que el manifiesto incluye exactamente las historias objetivo y sus potenciales bajo ambas políticas; la contribución de la historia target-only es +0,5; la suma ponderada q_X* es +0,5.
6. Comprobar la identidad de masas: soporte fuente total 0,5, target-only 0,5, total objetivo 1; no duplicar ni perder masa.
7. Perturbar solo u manteniendo constante el contraste homogéneo por historia: la verdad agregada debe permanecer +0,5. Como control adversarial adicional, una fixture analítica donde el contraste de la historia target-only difiera de +0,5 debe cambiar la verdad agregada en (u(delta_* - 0.5)); esta fixture prueba que el agregador pondera realmente la historia target-only y no la ignora.
8. Mantener la expectativa analítica y el TruthBundle fuera de la entrada Analyzer; el Analyzer debe seguir adjudicando `NOT_IDENTIFIED` por `TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT`.
9. Evaluator: verificar tanto la causa correcta de abstención como igualdad de la verdad reservada con +0,5. No aceptar `truth_within_bounds` como sustituto de igualdad numérica.

El punto 7 es un control del agregador y no implica modificar el roster confirmatorio de cinco escenarios. Las expectativas y el control deben quedar fijados antes de observar resultados de ejecución.

### 369.5 Dictamen y siguiente operación

| Elemento | Estado |
|---|---|
| Derivación analítica de los cuatro escenarios con soporte igual | STATICALLY DERIVED |
| Derivación analítica de positive_target_only | STATICALLY DERIVED, CONDICIONAL A REGLAS/ANCLAS DECLARADAS |
| Expectativa +0,5 target-only | CANDIDATE ORACLE VALUE, READY FOR TEST SPECIFICATION |
| Igualdad numérica del TruthBundle observada en ejecución | NOT EXECUTED |
| Test independiente de oráculo | SPECIFIED, NOT IMPLEMENTED |
| No-identificación del Analyzer por soporte | TEST EXISTS, NOT EXECUTED |
| No filtración dinámica de la verdad reservada | INTERFACE SEPARATION STATICALLY REVIEWED, NOT EXECUTED |

**Siguiente paso técnico:** implementar el test unitario independiente de la regla analítica, sin tocar la implementación del oráculo ni relajar los tests existentes. Después añadir la comparación exacta de la verdad target-only al test end-to-end reservado. Esta implementación requiere revisar la autorización vigente para cambios/tests; no autoriza ejecución de DGP, Analyzer/Evaluator, calibración o Monte Carlo.

**Controles:** solo se actualiza este documento en `research/c10-s-consolidation-draft`. No se modifican código, tests, perfiles, roster, seeds, workflows, RMA, Evidence→Claim Matrix, STATUS, Core ni `main`. No se ejecuta ningún test, pipeline, Analyzer, Evaluator ni experimento. PR #116 permanece Draft. `scientific_execution=false`, `execution_authorized=false`, `calibration_authorized=false`.


## 370. Reconciliación de reutilización de tests y autorización de implementación (2026-11-18)

**Estado:** HISTORICAL_TEST_REUSE_REVIEW / IMPLEMENTATION_NOT_AUTHORIZED / NO_CODE_CHANGE.  
**Propósito:** determinar si §369 requiere un test nuevo o si puede ampliarse un contrato existente, y comprobar la autorización antes de tocar código o tests.

### 370.1 Reconstrucción del contrato ya existente

La revisión estática de `test_c10s_world_pipeline_integration.py` confirma que ya existe una ruta end-to-end específica: `test_target_only_support_without_assignment_failure_abstains_end_to_end`. Comprueba:
- que la historia exclusivamente objetivo está materializada y no entra en el roster de asignación fuente;
- que el manifiesto reservado contiene diez EventHistory para cinco historias objetivo y dos políticas;
- que el Analyzer devuelve `NOT_IDENTIFIED` con `TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT`;
- que la masa objetivo no soportada es 0.5 y la cobertura q_X es 0.5;
- que el Evaluator adjudica `CORRECT_ABSTENTION`.

Pero la verdad capturada se comprueba solo con `-1 <= truth <= 1`; el test no afirma igualdad con +0.5 ni compara el valor por historia. No hace falta crear otro test end-to-end duplicado: el cambio mínimo futuro es reforzar este test existente con las aserciones numéricas independientes de §369, una vez autorizado.

La misma suite tiene un test de captura por roster que compara `row.truth` con `expected_theta_a_truth` solo cuando este último no es `None`. Para el escenario target-only, la expectativa sigue siendo `None`, por lo que la rama alternativa vuelve a comprobar únicamente los límites [-1,1]. Esta es la segunda ubicación que debe reconciliarse si se incorpora una expectativa aprobada al perfil; no debe cambiarse el perfil antes de resolver formalmente si `expected_theta_a_truth` es parámetro confirmatorio del roster o solo una expectativa del oráculo.

### 370.2 Reutilización recomendada, sin duplicación

El paquete mínimo de modificación futuro queda acotado a:
1. Añadir una función de expectativa analítica pura, independiente de `adjudicate_intervals` y de los oráculos V_CONT implementados, dentro del módulo de tests o de un módulo de referencia exclusivo de tests.
2. Reforzar `test_target_only_support_without_assignment_failure_abstains_end_to_end` para comparar la verdad del TruthBundle y la verdad observada por el Evaluator con +0.5, además de conservar las aserciones de abstención y causa.
3. Reforzar el test de captura del roster para no degradar silenciosamente el caso target-only a una mera comprobación de rango.
4. Añadir una comprobación de ponderación del agregador con una fixture analítica adversarial; mantenerla fuera del roster confirmatorio de cinco escenarios.

No se recomienda crear una nueva suite end-to-end paralela ni duplicar los contratos ya existentes. La expectativa analítica debe quedar en el lado de test, no convertirse automáticamente en una entrada del Analyzer ni en un parámetro productivo del DGP.

### 370.3 Límite de autorización

El artefacto `C10_S_INTEGRATED_DESIGN_CLOSURE_RECONCILIATION_AND_EXECUTION_READINESS_DRAFT_001.md` declara expresamente `IMPLEMENTATION_NOT_AUTHORIZED` y `SCIENTIFIC_EXECUTION_NOT_AUTHORIZED`; su §12 también declara `implementation_authorized=false`. El registro `C10_S_TEST_CONTRACT_REGISTER_DRAFT_001.md` establece que los contratos registrados no autorizan implementación ni validación ejecutable. La propuesta Gate 201, además, declara que no autoriza cambios de tests/workflows ni dispatch.

Por tanto, el trabajo de este turno se limita a revisión estática y reconciliación documental. No se modifican código, tests, perfiles, roster, workflows, locks ni parámetros; no se ejecutan tests, pipelines, Analyzer/Evaluator, DGP, CI, calibración o Monte Carlo. No se interpreta «Siguiente» como autorización implícita para superar una prohibición expresa.

### 370.4 Dictamen

| Elemento | Estado |
|---|---|
| Test end-to-end target-only existente | IMPLEMENTED / NOT EXECUTED |
| Comparación numérica target-only con +0.5 | MISSING |
| Captura por roster para target-only | RANGE-ONLY WHILE EXPECTATION IS NULL |
| Necesidad de duplicar test end-to-end | NO |
| Modificación mínima identificada | REUSE EXISTING TESTS / ADD INDEPENDENT ASSERTIONS |
| Implementación de esa modificación | BLOCKED — IMPLEMENTATION_NOT_AUTHORIZED |
| Ejecución de cualquier test | NOT AUTHORIZED |

**Siguiente operación permitida:** cerrar documentalmente la derivación de expectativa y el contrato de cambio mínimo, o recuperar una autorización vigente y explícita de implementación. Hasta entonces, mantener los artefactos ejecutables intactos.

**Controles:** únicamente documento maestro en `research/c10-s-consolidation-draft`; `main`, RMA v3.38, Evidence→Claim Matrix v1.47, STATUS y Core sin cambios; PR #116 permanece Draft.


## 371. Compatibilidad de la verdad analítica target-only con el contrato histórico del roster (2026-11-18)

**Estado:** HISTORICAL_CONTRACT_RECONCILED / ANALYTIC_EXPECTATION_TEST_ONLY / ROSTER_FIELD_UNCHANGED / IMPLEMENTATION_NOT_AUTHORIZED.  
**Propósito:** resolver la aparente tensión entre §369 (+0,5 como derivación analítica condicionada) y el contrato histórico que mantiene `expected_theta_a_truth=None` para `positive_target_only`. Esta sección no cambia el roster, su fingerprint, el DGP, el Evaluator ni las autorizaciones.

### 371.1 Precedencia histórica recuperada

La secuencia documental relevante es:

1. **§336.1–336.4:** define cuatro escenarios identificados y sus cuatro truths focales (+0,5; 0; −0,5; 0). Expresamente deja fuera una truth focal NOT_IDENTIFIED y la pérdida de soporte q_X* integrada.
2. **§348.1:** añade el quinto escenario target-only. Establece que la verdad reservada θ_A puede existir como contraste DGP sobre q_X* completo aunque no sea identificable desde la población fuente observada. No fija un valor numérico para ella.
3. **§355.1–355.2:** materializa la quinta variante como positive + target-only, pero declara que su truth numérica no se predeclara y que el Evaluator registra la verdad reservada sin imponer un valor no establecido por el contrato histórico.
4. **Implementación del roster:** `ThetaACalibrationDGPProfile.validate()` conserva una tabla histórica que asigna `None` a `positive_target_only` y rechaza cualquier `expected_theta_a_truth` distinto de ese valor. El perfil del quinto escenario declara `generator_variant="positive_target_only"` y omite `expected_theta_a_truth`.
5. **§369:** aporta una derivación manual nueva, basada en las reglas funcionales y el materializador target-only actuales, según la cual cada historia —incluida la target-only— tiene contraste focal +0,5 y la agregación sobre q_X* sigue dando +0,5.

La excepción histórica `None` no representa que la verdad generadora sea desconocida o inexistente. Representa que el contrato de §336/§348/§355 no había predeclarado una cifra para ese quinto escenario y que la captura no debía forzarla desde el perfil. §369 puede aportar ahora una expectativa analítica de referencia sin reescribir retroactivamente ese contrato.

### 371.2 Distinción obligatoria entre tres campos

| Objeto | Semántica | Estado/acción |
|---|---|---|
| `dgp_profile.expected_theta_a_truth` | Verdad predeclarada en el contrato tipado del roster; forma parte de su fingerprint | Mantener `None` para target-only hasta una decisión explícita que versionara el roster |
| Expectativa analítica de referencia de §369 | Resultado calculado a mano desde las reglas funcionales y la fórmula de agregación; independiente del código de adjudicación, aunque derivado de la misma especificación DGP | Puede usarse como oráculo esperado exclusivamente en tests |
| `ThetaAVContTruthBundle.theta_a_truth` / `Evaluator.truth` | Verdad reservada materializada por la cadena ejecutable para ese mundo | Debe compararse contra la expectativa analítica en una prueba futura autorizada |

Por tanto, no se debe cambiar el perfil del quinto escenario a `expected_theta_a_truth=0.5`, ni modificar su fingerprint, ni hacer que el Analyzer conozca esa expectativa. La comparación futura puede afirmar `TruthBundle.truth == 0.5` y `Evaluator.truth == 0.5` mediante una constante/oráculo analítico definido en el lado de tests, mientras el campo histórico del perfil continúa siendo `None`.

Esto preserva el significado original de `None`: ausencia de predeclaración en el contrato del roster, no una afirmación de que el valor no pueda derivarse posteriormente.

### 371.3 Condiciones que sostienen la derivación +0,5

La expectativa de §369 es válida para la fixture actual solo si se mantienen simultáneamente estas condiciones observadas en los blobs revisados:

- `execute_calibration_scenario()` traduce `positive_target_only` al generador `positive` y aplica el materializador target-only.
- El materializador escala las masas fuente por (1-u), añade la historia target-only con masa (u=0.5), y le asigna los mismos vectores focales, certificado `r_common` y estado inicial `(enabled=True, admission=ADMIT)`.
- La regla focal G_A positiva se activa para el vector con primera coordenada 0 y segunda coordenada 0; cambia admission a `NO_ADMISSION` en t=1. Para el vector con primera coordenada 1 no se activa.
- La regla D2 que interrumpe directamente admission no se selecciona al generar potenciales `G_A`; el adaptador selecciona las reglas de fuente `G_A` (y las familias explícitamente admitidas por su contrato), no convierte el potencial D2 observado en el potencial focal.
- La regla alternativa común de deshabilitación no está presente en el generador positivo.
- La rejilla y el adjudicador siguen la convención temporal aceptada en DEC-C10-104: el evento t=1 pertenece a [1,2], no a [0,1).

Bajo esas condiciones, para cada historia (h), (delta(h)=1-0.5=+0.5), incluida la historia target-only. Con masas fuente renormalizadas por (1-u) y masa target-only (u), (	heta_A(q_X^*)=(1-u)0.5+u0.5=+0.5).

**Límite epistemológico:** esto es una derivación analítica desde el DGP especificado y una expectativa de test independiente del código del oráculo/adjudicador. No es una segunda implementación ejecutable del generador, ni validación dinámica, ni evidencia de que el Analyzer pueda identificar el parámetro. La separación de canales Analyzer/Evaluator sigue pendiente de prueba dinámica autorizada.

### 371.4 Ajuste del contrato mínimo de test

La modificación futura, si se autoriza, debe:
1. Mantener intactos `ThetaACalibrationDGPProfile.expected_theta_a_truth=None`, el validador histórico del perfil y el fingerprint del quinto escenario.
2. Definir en el módulo de tests una expectativa analítica explícita `EXPECTED_TARGET_ONLY_THETA_A = 0.5`, derivada de la regla de cumplimiento por intervalos y de la ponderación de masas; no importarla desde el DGP ni desde el oráculo.
3. En el test end-to-end existente, comparar la verdad del TruthBundle y `Evaluator.truth` con +0,5, además de comprobar la abstención y su causa exacta.
4. En la captura por roster, conservar la semántica de `None`; añadir una aserción de test separada que compare `record.truth` con +0,5 para el escenario target-only, sin cambiar el dataclass ni su lógica de captura.
5. Mantener el control adversarial de ponderación de §369 separado de los cinco escenarios confirmatorios candidatos.

No se debe introducir un parámetro duplicado en producción ni cambiar el mapeo histórico de truths para facilitar una aserción. La prueba debe detectar divergencias entre la expectativa analítica, la verdad materializada y la adjudicación, no obligar a la implementación a repetir su propia salida.

### 371.5 Dictamen y autorización

| Elemento | Dictamen |
|---|---|
| Contrato histórico `None` para target-only | PRESERVED / NOT A CLAIM OF UNKNOWN TRUTH |
| Expectativa analítica +0,5 | DERIVED CONDITIONALLY / TEST-ONLY REFERENCE |
| Cambio del perfil/fingerprint | NOT REQUIRED / NOT AUTHORIZED |
| Comparación TruthBundle/Evaluator contra +0,5 | REQUIRED FUTURE TEST / NOT IMPLEMENTED |
| Verificación dinámica | NOT EXECUTED |
| Roster de cinco escenarios | CANDIDATE / NOT FROZEN |
| Implementación | BLOCKED — IMPLEMENTATION_NOT_AUTHORIZED |
| Ejecución EP-02 / Analyzer / Evaluator / DGP / calibración | NOT AUTHORIZED |

**Siguiente paso permitido:** revisar estáticamente la cobertura de verdad reservada y las expectativas de los cinco escenarios, verificando que los cuatro valores predeclarados del roster y el valor test-only derivado para target-only se mantienen separados y completos. No abrir un nuevo roster ni duplicar escenarios.

**Controles:** únicamente se actualiza el documento maestro de la rama `research/c10-s-consolidation-draft`; no se modifican código, tests, perfiles, roster, seeds, workflows, RMA, Evidence→Claim Matrix, STATUS, Core ni `main`. No se ejecutan tests, pipelines, Analyzer/Evaluator, DGP, CI, calibración, Monte Carlo ni experimento científico. PR #116 permanece Draft. `implementation_authorized=false`, `scientific_execution=false`, `execution_authorized=false`, `calibration_authorized=false`.


## 372. Matriz de cobertura de verdad reservada y expectativas del roster de cinco escenarios (2026-11-18)

**Estado:** STATIC_COVERAGE_AUDIT / FOUR_PREDECLARED_TRUTHS_RECONCILED / FIFTH_TEST_ONLY_EXPECTATION / ROSTER_NOT_FROZEN.  
**Objetivo:** comprobar que la derivación de §369/§371 cubre los cinco contratos candidatos sin alterar la separación entre verdad predeclarada del perfil, verdad reservada materializada y verdad de referencia del test.

### 372.1 Matriz de correspondencia

| ID de escenario | Variante ejecutada por la fábrica | Verdad del perfil | Verdad analítica de referencia | Identificación esperada | Evidencia de test revisada |
|---|---|---:|---:|---|---|
| `THETA_A_POSITIVE_V1` | `positive` | +0,5 | +0,5 | IDENTIFIED | Contrato del roster y pruebas del pipeline positivo |
| `THETA_A_NULL_V1` | `null` | 0 | 0 | IDENTIFIED | Contrato del roster y pruebas de los modos focales |
| `THETA_A_NEGATIVE_V1` | `negative` | −0,5 | −0,5 | IDENTIFIED | Contrato del roster y pruebas de los modos focales |
| `THETA_A_ALTERNATIVE_COMMON_V1` | `alternative` | 0 | 0 | IDENTIFIED | Contrato del roster y prueba de vía alternativa común |
| `THETA_A_TARGET_SUPPORT_NONIDENTIFIED_V1` | `positive` + materializador target-only | `None` | +0,5, solo como expectativa analítica test-only de §369/§371 | NOT_IDENTIFIED | Test end-to-end target-only; actualmente solo verifica bounds, causa y abstención |

### 372.2 Cobertura efectivamente presente

La revisión estática de `test_theta_a_calibration_protocol.py` encuentra:
- una aserción explícita del orden de los cinco IDs;
- una aserción explícita de las truths del perfil `[0.5, 0.0, -0.5, 0.0, None]`;
- una aserción de `NOT_IDENTIFIED` y de la causa exacta para el quinto escenario;
- un recorrido de captura por escenario que compara `row.truth` con la verdad del perfil cuando esta no es `None`, y para el quinto escenario comprueba únicamente `[-1,1]`.

La revisión de `test_c10s_world_pipeline_integration.py` encuentra:
- pruebas de verdad focal positiva y de la separación entre θ_A y el ITT-D2;
- prueba del régimen alternativo común, con verdad focal cero y soporte identificado;
- prueba end-to-end target-only sin fallo de positividad de asignación, que verifica la causa exacta `TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT`, la masa no soportada 0.5, cobertura 0.5, el roster fuente sin unidad sintética añadida y `CORRECT_ABSTENTION`;
- ausencia de una aserción de igualdad numérica con +0,5 en ese test target-only.

Las expectativas +0,5/0/−0,5/0 están vinculadas al contrato tipado del perfil y a pruebas del pipeline para los cuatro modos identificados. La expectativa target-only +0,5 todavía no está vinculada a una aserción de test. La verdad reservada se calcula y se captura, pero el test end-to-end no la contrasta con una derivación independiente.

### 372.3 Lo que esta matriz no debe colapsar

1. **Truth del perfil:** los cuatro valores declarados son parte del contrato tipado y su fingerprint; el quinto `None` es una omisión deliberada de predeclaración histórica. No cambiarlo en esta operación.
2. **Truth reservada:** el TruthBundle y el Evaluator calculan/reciben una verdad numérica en cada réplica, también para el quinto escenario. Su existencia no vuelve identificado el estimando.
3. **Identificación:** el quinto Analyzer debe abstenerse por soporte objetivo no cubierto aunque el DGP conozca la verdad. No se debe convertir +0,5 en punto estimado, bound más estrecho ni entrada visible al Analyzer.
4. **Métricas:** bias, MAE, RMSE, recuperación puntual, cobertura y anchura de intervalo continúan `NOT_EVALUABLE` para el escenario estructuralmente no identificado. Una comparación del oráculo con +0,5 valida la verdad reservada, no convierte esas métricas en evaluables.

### 372.4 Dictamen

La cobertura conceptual de los cinco escenarios está reconciliada. No hay una quinta verdad desconocida: hay una verdad reservada materializada cuya cifra no está predeclarada en el perfil histórico. La derivación de §369 ofrece una expectativa de referencia +0,5, condicionada a la configuración actual del generador y del materializador. El cambio futuro correcto es una aserción test-only; no un cambio de perfil, fingerprint, Analyzer, Evaluator, roster ni estimando.

| Componente | Estado |
|---|---|
| Cuatro truths predeclaradas del perfil | RECONCILED |
| Quinta truth reservada materializada | IMPLEMENTED PATH / NOT NUMERICALLY ASSERTED |
| Expectativa analítica +0,5 para target-only | DERIVED CONDITIONALLY / TEST-ONLY |
| Cobertura de abstención/causa target-only | TEST AUTHORED / HISTORICAL EP-02 EVIDENCE / NO NEW EXECUTION |
| Igualdad TruthBundle/Evaluator vs +0,5 | MISSING ASSERTION |
| Roster | FIVE CANDIDATES / NOT FROZEN |
| Implementación del cambio | NOT AUTHORIZED |
| Ejecución y calibración | NOT AUTHORIZED |

**Siguiente operación:** completar la auditoría de independencia de unidades y de mundos para el roster completo, con especial atención al quinto escenario: su unidad sintética target-only no pertenece al roster fuente aleatorizado, y la declaración `unit_independence_certified=False` debe interpretarse sin confundirla con dependencia entre las unidades fuente. La auditoría debe separar independencia de unidades dentro de M, independencia de mundos M e independencia/relación de asignaciones R.

**Controles:** solo documento maestro en `research/c10-s-consolidation-draft`; no se modifican código, tests, perfil, roster, seeds, workflows, decisiones fuente, RMA, Evidence→Claim Matrix, STATUS, Core ni `main`. No se ejecutan tests, DGP, Analyzer/Evaluator, runner, CI, calibración o Monte Carlo. PR #116 permanece Draft. `implementation_authorized=false`, `scientific_execution=false`, `execution_authorized=false`, `calibration_authorized=false`.


## 373. Auditoría de independencia N×M×R y emparejamiento entre escenarios (2026-11-18)

**Estado:** STATIC_DEPENDENCE_AUDIT / SEED_STREAM_SEPARATION_IMPLEMENTED / STATISTICAL_INDEPENDENCE_CONDITIONAL / TARGET_ONLY_UNIT_NOT_SAMPLED.  
**Objetivo:** separar la independencia postulada dentro de cada mundo, la generación de mundos exteriores M, las réplicas de asignación R y el emparejamiento deliberado entre escenarios. La unicidad de seeds/streams no se interpreta por sí sola como demostración matemática de independencia.

### 373.1 Unidades N dentro de un mundo M

`SyntheticWorldBuilder.generate()` usa un único `random.Random(config.seed)` por mundo y recorre secuencialmente las N unidades. Para cada unidad genera sus covariables basales, indicadores Bernoulli de componentes y un `d2_seed` propio mediante `getrandbits(64)`, con el que materializa sus potenciales D2. La identidad y el roster de cada unidad se generan por índice y se validan como parte del mundo.

La asignación focal usa `_dgp_uniform(world.seed_commitment_sha256, randomization_salt, unit_id, ...)`: separa por clave la extracción de brazo y la extracción del vector conjunto. Los potenciales funcionales G_A se generan por unidad/historia, vector y régimen común; no se reutiliza la asignación realizada como si fuera el potencial contrafactual.

**Dictamen N:** la arquitectura implementada es compatible con unidades generadas independientemente bajo el modelo de pseudoaleatoriedad de los generadores y sin interferencia. La declaración de `independence_basis` del roster es una justificación de diseño, no un certificado estadístico observado. La revisión estática no prueba independencia empírica ni excluye toda dependencia compartida no representada por el DGP.

Para los cuatro escenarios identificados, `unit_independence_certified=True` habilita el cálculo inferencial individual previsto por el protocolo. Esa bandera sigue siendo una premisa declarada del escenario, no una conclusión que el validador derive del código.

### 373.2 Mundos exteriores M

La derivación de semillas `TGCV-C10S-THETA-A-SEED-v2` construye `world_seed/world_id/roster_id/unit_id_prefix` a partir de namespace, banco, familia de mundo, versiones, N e identificador exterior M. La validación exige:
- identidad y seed constantes entre las R del mismo escenario×N×M;
- world_id, roster_id, seed y prefijo de unidades distintos entre M dentro de un diseño;
- identidad basal exactamente compartida entre escenarios de una misma `world_family_id`×N×M;
- identidad distinta entre familias×N×M.

Esto acredita separación y unicidad determinista de identidades/semillas, no independencia matemática por sí sola. La interpretación de mundos M como réplicas independientes descansa además en el supuesto de pseudoaleatoriedad de las semillas y del generador, y en que no haya estado global compartido entre ejecuciones. No hay ejecución ni diagnóstico de correlación entre mundos en esta revisión.

**Dictamen M:** `M` representa mundos exteriores distintos por construcción de streams y de identidad. Su independencia estadística es una hipótesis de diseño condicionada al mecanismo pseudoaleatorio, no un resultado probado por la validación de fingerprints.

### 373.3 Réplicas R dentro de M

Para un M dado, R conserva el mismo mundo, roster, DGP y verdad reservada. Cada R recibe:
- `run_id` distinto;
- `randomization_salt` distinto para la asignación de política conjunta;
- `s3_seed` distinto para la observación;
- separación explícita entre streams de mundo y S3.

El generador focal deriva los draws de asignación a partir del compromiso del mundo, salt de R, unidad y dominio de extracción. La validación exige unicidad global de `run_id`, salts y seeds S3 y su separación respecto a seeds de mundo.

**Dictamen R:** las R son repeticiones de asignación/observación condicionadas al mismo mundo M; no son mundos independientes ni deben aumentar el número efectivo de M para el MCSE entre mundos. Son streams diferenciados y reproducibles; su independencia condicional se apoya en el esquema hash/salt y en el supuesto pseudoaleatorio, no en la mera diferencia de cadenas.

### 373.4 Emparejamiento entre escenarios

La familia `THETA_A_INTERACTION_BASE_V1` agrupa positive, alternative y positive_target_only. Para cada N×M comparten exactamente world_seed, world_id, roster_id y prefijo de unidades. Los escenarios conservan run_id, salts y streams S3 propios. Positive y alternative son, por tanto, comparaciones emparejadas sobre el mismo mundo basal con regímenes funcionales distintos; target-only añade una extensión determinista del soporte objetivo sobre esa misma base.

Null y negative pertenecen a familias de mundo distintas. No deben presentarse como emparejados con positive/alternative ni usarse como si fueran contrastes pareados de la misma realización basal.

El emparejamiento positive/alternative/target-only es intencional y compatible con contrastes por mundo. No contradice la independencia entre mundos M, pero exige que el análisis preserve la estructura pareada por familia y no trate las observaciones de escenarios de una misma familia×N×M como independientes.

### 373.5 Particularidad del quinto escenario target-only

El quinto escenario declara `unit_independence_certified=False`. La revisión del materializador muestra que:
- las N unidades fuente siguen siendo las unidades del mundo generado;
- la historia `TARGET-ONLY-HISTORY-001` recibe una identidad sintética `TARGET-ONLY-UNIT-001`, pero no se incorpora a `world.units`;
- no recibe asignación focal ni observación S3 de una unidad fuente;
- sus covariables X/H0/C_c se anclan copiando las de la primera unidad fuente;
- su estado funcional inicial y sus potenciales G_A se materializan de forma determinista bajo las reglas positivas.

Por ello, `unit_independence_certified=False` no debe interpretarse como evidencia de dependencia entre las N unidades fuente. Es una negativa conservadora a certificar independencia individual para el estimando q_X* completo, que contiene masa target-only no muestreada ni aleatorizada. La historia añadida no es una unidad independiente extraída de la población fuente. El estimando objetivo sigue teniendo verdad sintética definida, pero no adquiere soporte observacional ni una muestra independiente para inferencia.

La consecuencia operativa correcta es la ya implementada: no suministrar confianza inferencial individual al Analyzer para el quinto escenario y mantener `NOT_IDENTIFIED / TARGET_HISTORY_OUTSIDE_SOURCE_SUPPORT`. No reinterpretar la flag como una refutación de independencia de las unidades fuente, ni elevarla a certificación de representatividad de la unidad anclada.

### 373.6 Implicaciones para la futura inferencia y el MCSE

1. N cuantifica unidades fuente dentro del mundo; no incluye la historia target-only sintética como unidad aleatorizada.
2. R cuantifica repeticiones de asignación/observación dentro del mismo M; no sustituye M.
3. M cuantifica mundos exteriores; su independencia requiere el supuesto pseudoaleatorio y ausencia de estado compartido, además de seeds/identidades distintas.
4. Los contrastes positive–alternative–target-only dentro de una misma familia×N×M deben preservar el emparejamiento; el análisis no debe inflar el tamaño muestral contando escenarios emparejados como mundos distintos.
5. Para target-only, las métricas de recuperación puntual e intervalar siguen `NOT_EVALUABLE`; una verdad reservada conocida no repara la ausencia de soporte.
6. Antes de congelar el protocolo debe quedar explícita la unidad de agregación del MCSE entre M y la forma de calcular contrastes emparejados por mundo. No basta con afirmar que las seeds son únicas.

### 373.7 Dictamen

| Dimensión | Resultado estático |
|---|---|
| Generación de unidades fuente N | IMPLEMENTED / PSEUDORANDOM DESIGN BASIS |
| Independencia N | CONDITIONAL DESIGN ASSUMPTION / NOT EMPIRICALLY VERIFIED |
| Separación de mundos M | IMPLEMENTED / UNIQUE DETERMINISTIC SEEDS AND IDENTITIES |
| Independencia M | CONDITIONAL PSEUDORANDOM-STREAM ASSUMPTION / NOT PROVEN BY UNIQUENESS |
| R dentro de M | IMPLEMENTED / DISTINCT ASSIGNMENT AND S3 STREAMS |
| Independencia condicional R | CONDITIONAL ON HASH/SALT PSEUDORANDOMNESS |
| Emparejamiento positive/alternative/target-only | IMPLEMENTED BY SHARED WORLD FAMILY |
| Null/negative pairing with interaction family | NOT DECLARED |
| Unidad target-only como muestra independiente | NOT PRESENT / NOT CLAIMED |
| Flag de independencia target-only | CONSERVATIVE FALSE FOR FULL TARGET ESTIMAND |
| MCSE paired-by-world specification | OPEN |

**Siguiente operación:** revisar si la especificación estadística del agregador (§361–§366) preserva de forma suficiente el emparejamiento positive/alternative/target-only y separa el nivel M del nivel R, sin contar R como mundos ni escenarios emparejados como réplicas independientes. Si el contrato actual no lo resuelve, registrar la brecha sin implementar el agregador.

**Controles:** auditoría estática únicamente; no se generan seeds, no se invoca el runner, no se ejecutan tests, DGP, Analyzer/Evaluator, workflows, calibración o Monte Carlo. No se modifican código, tests, perfiles, roster, locks, RMA, Evidence→Claim Matrix, STATUS, Core ni `main`. PR #116 permanece Draft. `implementation_authorized=false`, `scientific_execution=false`, `execution_authorized=false`, `calibration_authorized=false`.
