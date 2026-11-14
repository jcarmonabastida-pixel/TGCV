

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
