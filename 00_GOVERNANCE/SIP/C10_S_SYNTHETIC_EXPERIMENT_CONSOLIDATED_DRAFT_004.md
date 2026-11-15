

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
