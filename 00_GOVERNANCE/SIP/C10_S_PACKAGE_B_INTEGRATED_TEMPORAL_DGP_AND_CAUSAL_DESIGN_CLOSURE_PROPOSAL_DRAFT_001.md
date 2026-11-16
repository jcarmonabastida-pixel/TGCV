# C10-S — Paquete B: propuesta integrada de cierre del DGP temporal y del diseño causal

**Fecha:** 2026-11-16  
**Estado:** B1_B6_ACCEPTED / SYNTHETIC_LANE_MATERIALIZATION_REQUIRED / MATERIAL_PARAMETERS_AND_CAUSAL_RECOVERY_OPEN / NOT_DESIGN_FROZEN.  
**Rama:** research/c10-s-consolidation-draft · PR #116 Draft.  
**Precedencia:** DEC-C10-066/067/068/069/095/099…104; DEC-C10-103; DEC-C10S population/estimand decisions; Package A accepted C1–C6; R144-A; R146-A…D; R147-A/B; R148-A; R150-A; R151-A/A8; R152-A1…A6; R208-A1…A6; Gates 121, 129, 130; DGP Temporal and Role Contract §§48–55; D2 Assignment/Population/Support Reconciliation; Path Predicate Temporal Evidence Matrix; UNIT-01…14, PROV-01…12, P177–P183, MEAS/MISS and S3 contracts.
**Tipo:** reconciliación integrada y propuesta de decisiones de diseño; no crea DEC ni modifica los contratos fuente.

## 1. Dictamen ejecutivo

El Paquete B puede cerrarse en una sola decisión lógica integrada si se separan tres capas que hasta ahora aparecían mezcladas:

1. **Contrato causal y temporal:** qué mundo genera el DGP, qué se asigna, qué constituye accesibilidad/admisión, cómo se define el tiempo y qué truth adjudica V_cont.
2. **Instancia material del diseño:** roster sintético versionado, unidad de asignación, asignación Z, historias basales, políticas factibles, soporte, aislamiento y certificados.
3. **Parámetros empíricos del benchmark:** soporte temporal, T*, Δ, K, resolución/cadencia S3, curva de detectabilidad y parámetros de error/captura.

La primera capa puede quedar normativamente reconciliada ahora. Las capas segunda y tercera no pueden darse por cerradas mediante prosa: requieren instancias aprobadas, materialización autorizada y calibración posterior. No se rellenan con cifras o supuestos inventados.

**Propuesta:** aceptar el contrato lógico integrado B1–B6 de este documento; mantener explícitamente MATERIALIZATION_OPEN, PARAMETER_CALIBRATION_OPEN y CAUSAL_IDENTIFICATION_NOT_ESTABLISHED. La aceptación cerraría el diseño lógico de Paquete B, no afirmaría que el experimento esté ya materialmente identificado o listo para ejecución.

## 2. Reconciliación temporal: §51, reloj y horizonte

### B1 — Coordenada contractual

Se ratifica la formulación ya contenida en §51 del DGP Temporal and Role Contract:

- W_c=t_c,max−t_0 es el soporte común de transiciones causales potenciales que pueden cambiar A_B1.
- x=(t−t_0)/W_c, con t_0=0 y t_c,max=1.
- Es un reloj adimensional de coordenadas, no tiempo físico, duración real, t9 ni profundidad H.
- Las duraciones de episodio se expresan d_e=δ_event/W_c.
- La cola común ρ_follow=τ_follow/W_c permanece como parámetro por determinar; T*=1+ρ_follow.
- t_last,i es la última transición efectiva de la unidad; t_last^max=t_c,max es el límite superior común ex ante. No se define una ventana retrospectiva distinta por unidad.

Esta ratificación no introduce una nueva coordenada: formaliza la ya especificada en §51 y reconciliada en Gates 142–144.

### B2 — Rejilla y continuidad

Se preservan DEC-C10-099…104:

- V_cont,truth(i)=K⁻¹ Σ(k=1…K) A_B1(i,k), media no ponderada de K intervalos iguales sobre [0,T*].
- Δ=T*/K=(1+ρ_follow)/K, con K entero.
- Intervalos semiabiertos [b_{k−1},b_k), salvo el último cerrado en T*.
- Un incumplimiento funcional confirmado en cualquier instante afecta a todos los intervalos que intersecta; no hay gracia ni duración mínima funcional.
- Truth trivaluada por intervalo: 1 si el contrato se cumple en todo el intervalo; 0 si existe incumplimiento confirmado; ? solo si el Generator define una indeterminación funcional intrínseca según DEC-C10-100/104.
- Bounds de truth: [n₁/K,(n₁+n?)/K]. No se imputan UNKNOWN como cero ni se eliminan del denominador.

K y Δ no se fijan por H, t0…t9, frecuencia de muestreo o conveniencia. Se derivan de resolución de fenómenos, aliasing, cruce de fronteras, estabilidad al refinar K y soporte común.

### B3 — Horizonte y censura

Se mantiene T*=t_last^max+τ_follow, equivalente a 1+ρ_follow en el reloj normalizado. El soporte causal máximo debe acotarse ex ante en todos los brazos y escenarios. Si no puede acotarse, T* permanece abierto y no hay cierre temporal confirmatorio.

Un episodio funcional activo en T* es terminal/censurado; no se considera recuperado por imputación. El seguimiento cubre el soporte de recuperación defendible, no una duración elegida tras observar resultados.

## 3. EventHistory y adjudicación temporal: contrato compuesto

### B4 — Historia funcional generada

EventHistory es una estructura de truth del Generator por unidad y potencial (z,g), separada de PROCESS_EVENT, S3 y adjudicación. Su contrato lógico ya aceptado por R144-A/R146-A…D se conserva:

- estado funcional inicial post-Z en t0;
- persistencia por tramos hasta transición truth explícita;
- transición con identidad propia, versión, familia causal, estado before/after, event_time y provenance;
- simultaneidad genuina atómica; suborden solo para representar estados intermedios reales y explícitos;
- completitud por unidad, potencial, ámbito de transición, generación e integridad;
- regeneración/versionado inmutable: corrección produce nueva generación, no mutación silenciosa;
- defectos de historia, integridad o harness son errores de representación/conformidad, nunca UNKNOWN funcional.

La historia registra cambios declarativos de PROFILE y ENABLED con versión, pero el alcance de A_B1/V_cont se rige por el Paquete A aceptado: PROFILE exposure permanece obligación contractual y no es una trayectoria temporal adjudicada en el DGP actual. D_valid es separado. Solo mecanismos del DGP vigente cuyo estado altere efectivamente la admisión exigida entran como transiciones funcionales A_B1. Logs, intentos, instalación, telemetría y observaciones no son truth por sí mismos.

### B5 — Predicado funcional y cadena de adjudicación

Para cada intervalo:
- ENABLED=true requiere admisión efectiva; incapacidad runtime constitutiva confirmada que la impida es incumplimiento.
- ENABLED=false requiere no-admisión; admisión efectiva es incumplimiento.
- A_B1 se adjudica sobre la función efectiva de admisión, no sobre la mera configuración.
- V_cont agrega los intervalos según DEC-C10-100…104.
- TruthBundle conserva EventHistory, versiones, reglas, bounds de truth y hashes exactos.

Orden de roles: Generator produce truth/EventHistory → projector S3 produce observaciones → Sealer sella evidencia permitida → Analyzer estima/abstiene sin acceso a truth → Evaluator abre TruthBundle después del sellado y adjudica. EventHistory/TruthBundle no se filtran al Analyzer.

## 4. S3: contrato de observación y calibración

S3 es un canal lógico único, pasivo, vectorial y no-mutante. Sus cinco dominios funcionales se conservan: proceso/módulo; listener/socket/superficie de ingreso; dependencias constitutivas; capacidad/recursos solo cuando alteren admisión; perfil runtime. Las modalidades snapshots/métricas, logs/trazas/eventos e híbrida son implementaciones candidatas de la fuente, no decisiones ya seleccionadas.

Por familia, versión y modalidad se modelan conjuntamente:
- fase y cadencia/resolución;
- lag y desorden;
- pérdida, duplicación y cobertura;
- falsos positivos y falsos negativos;
- dependencia/correlación entre señales;
- detectabilidad por duración y fase.

La detectabilidad se expresa como curva P_det,joint(d_e | θ_S3, familia, versión, fase). Un δ_det escalar solo puede derivarse después de aprobar umbral p* y calibrar la curva. Si no hay umbral aprobado, se conserva la curva y el Analyzer produce bounds/abstención cuando la observación no identifica truth.

No confundir duración funcional d_e; cadencia/resolución S3; Δ de adjudicación; umbral/dominio de detectabilidad δ_det; y seguimiento τ_follow.

S3 missingness/lag/error/cobertura insuficiente no se transforma en UNKNOWN funcional. Los bounds de truth DEC-C10-100 y los bounds de identificación parcial del Analyzer son objetos distintos.

## 5. Reconciliación causal D2 y población

### B6 — Diseño de asignación y población: reglas preservadas

Se mantienen sin reabrir:
- D2 como escenario primario candidato; D1 secundario.
- P*τ2 como población primaria candidata; P*_F como subpoblación secundaria.
- una B1 por UE y una oportunidad estandarizada por UE;
- UE (unidad de potenciales/resultados), UA (unidad asignada) y UO (observaciones repetidas) separadas;
- P(W_programmed=1 | Z=0,D2)=0 y P(W_programmed=1 | Z=1,D2)=1, reglas de programación de la política, no probabilidades de aleatorización;
- Z permanece ITT; no se sustituye por W_programmed, W_attempt, recepción, S_install, C_dep*, A_f*, D_f* o ΔT_acc*;
- el 0.80 de éxito técnico sigue siendo hipótesis no validada, no apertura focal ni primera etapa confirmada;
- no se condiciona ITT a variables post-Z, petición, procesamiento, selección o ejecución.

### Población pre-Z y estados desconocidos

Se preserva la precedencia de P*τ2 y P*_F, sin reabrirla. Sin embargo, la composición material de E_i, el mapping entre E_scope y App, los valores basales y el tratamiento operativo de unidades ? siguen sin resolver. Estados 1/0/? y NA solo por no aplicabilidad justificada ex ante; ausencia de registro, cobertura parcial o mapping ambiguo no equivalen a 0. La clasificación que determine asignación debe quedar sellada antes de Z.

Antes de generar la población confirmatoria se deberá escoger, con evidencia y justificación, una ruta: resolver ? con fuente independiente; usar un marco observable más amplio con estimando/cotas explícitos; o restringir ex ante a población pre-Z confirmada y reconocer que no representa automáticamente la población causal verdadera. No excluir ? silenciosamente.

### Asignación Z

La unidad UA, ratio/probabilidades π_h, estratos/bloques, algoritmo, semilla, hash, concealment, desviaciones y protocolo de crossover no están seleccionados. No se presume 1:1 ni se transfieren los parámetros de P178. Se seleccionarán en un contrato de aleatorización versionado después de fijar roster, unidad, estructura de estratos y N; P(Z_i=1 | S_i,UA_i) debe ser positiva en cada estrato/historia incluida y auditable. Las probabilidades de Z nunca son masas de q_X*.

## 6. Aislamiento e interferencia

Gate 121 ya define suficiencia y adjudicación; no hace falta otro inventario ni otra familia de tests. Se reutilizan B-M01…15, U_G NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT, IAM/C_SRC, Adapter Provision Manifest, PROV-01…12 y UNIT-01…14.

La arquitectura preferida UE=UA solo se habilita cuando IS-1…IS-8 estén satisfechos con evidencia material, versión, frontera y ventana auditadas. Un instance_id único por UE no prueba independencia. Se distingue compartición de un recurso, posibilidad de transmisión y consecuencia causal sobre otra UE. Un solo control IS-* relevante OPEN, ?, PARTIAL, MISSING o CONFLICTING mantiene ISOLATION_NOT_DEMONSTRATED.

Si hay interferencia:
- cluster solo si se define ex ante, con unidad de asignación, estimando, ponderación y potencia propios;
- mapa de exposición G_i(Z_-i) solo si está versionado, completo y con soporte;
- si no es mapeable/soportado, bounds o abstención; no ITT individual convencional ni θ_A identificado.

No se cambia a cluster por intuición ni se presume SUTVA.

## 7. q_X*, g_A0/g_A1, r_common y θ_A

Se preservan los contratos ya cerrados documentalmente en Gates 79/86/130:
- q_X*=Law(X,H0,C_c | i∈P*τ2), distribución conjunta de historias basales pre-Z con referencias versionadas, masas positivas y suma 1;
- g_A0/g_A1 son intervenciones conjuntas/versionadas sobre el vector completo ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*), factibles por historia;
- soporte conjunto requiere que ambas políticas sean factibles y tengan soporte para toda historia de masa positiva;
- r_common fija por historia las condiciones no focales comunes, con certificados explícitos; igualdad de etiquetas no acredita igualdad del régimen.

No se ratifican los extremos deterministas (0,0,0,0)/(1,1,1,1); no se inventan kernels, masas, suavizados ni políticas para conseguir positividad. G no sustituye g_A.

**Consecuencia:** θ_A está definido como estimando, pero sigue NOT_IDENTIFIED / NOT_MATERIALIZED; el Analyzer actual no lo estima. ITT-Z^D2 es efecto total del paquete si se completa el diseño y el resultado. ITT-G es un contraste separado. LATE_f requiere supuestos IV completos y primera etapa focal D_f*. C4 es mediación interventional longitudinal separada. No se calcula efecto directo/residual por resta.

## 8. Registro integrado de dependencias y estado

| Dependencia | Estado tras reconciliación | Qué falta realmente |
|---|---|---|
| Reloj normalizado §51 | LOGICAL_COORDINATE_RECONCILED | Cota material del soporte causal común y versión final |
| T*, ρ_follow | OPEN | Soporte ex ante de recuperación/persistencia |
| Δ,K | OPEN | Derivación desde resolución/aliasing y estabilidad |
| EventHistory | LOGICAL_CONTRACT_ACCEPTED | Materialización y conformidad por unidad/potencial |
| IntervalAdjudication/TruthBundle | CONTRACT_SPECIFIED_PARTIALLY | Implementación/versionado y tests de frontera |
| S3 | OBSERVATION_CONTRACT_DEFINED | Modalidad, parámetros y curva de detectabilidad calibrada |
| D2 programming | ACCEPTED BY DEC-C10-066/067 | No confundir con asignación Z |
| Población E_i | PRECEDENCE PARTIAL | Mapping E_scope/App, truth pre-Z y regla para ? |
| Roster/IAM/C_SRC/snapshots | NOT MATERIALIZED | Instancia sintética aprobada y provenance |
| Z / π_h | NOT SPECIFIED | Unidad, ratio, estratos, algoritmo, semilla/hash |
| UE=UA / aislamiento | CONDITIONAL / NOT DEMONSTRATED | Evidencia IS-1…8 |
| Cluster / exposure map | NOT SELECTED | Solo si evidencia muestra interferencia |
| q_X* | SCHEMA DEFINED / ROWS AND MASSES ABSENT | Historias basales y pesos |
| g_A0/g_A1 | FORM DEFINED / PAIR NOT SELECTED | Políticas conjuntas factibles y versionadas |
| r_common | SEMANTICS DEFINED / NOT CERTIFIED | Certificados por historia |
| θ_A / Analyzer | NOT IDENTIFIED / NOT RECOVERED | Soporte, políticas, evidencia y estimador |
| ITT-Z^D2 | POTENTIALLY IDENTIFIABLE / DESIGN NOT MATERIALIZED | Z, UA, población, resultado y aislamiento |
| 0.80 técnico | HYPOTHESIS ONLY | Calibración; no usar como hecho |
| P177–P183 / UNIT / PROV | CONTRACTS REUSABLE | Mapping a escenarios y ejecución posterior |

## 9. Borrador de decisiones lógicas B1–B6 para aceptación conjunta

**B1.** Adoptar el reloj adimensional de §51 (t0=0, t_c,max=1, x=(t−t0)/W_c) como coordenada contractual; no fijar duración física ni ρ_follow.

**B2.** Preservar la rejilla común K, Δ=(1+ρ_follow)/K, agregación igualitaria, intervalos y bounds DEC-C10-100/104; derivar K/Δ por calibración de resolución/aliasing, no por conveniencia.

**B3.** Adoptar EventHistory por unidad/potencial con semántica R144-A/R146-A…D y separación PROCESS_EVENT/S3/TruthBundle; A_B1/V_cont según Paquete A; defectos de historia nunca UNKNOWN funcional.

**B4.** Adoptar T*=1+ρ_follow, soporte causal común ex ante, censura de episodios activos y regla de última transición máxima; si el soporte no se acota, no cerrar temporalidad.

**B5.** Adoptar S3 como canal pasivo vectorial con cinco dominios y curva conjunta de detectabilidad; no seleccionar modalidad, umbral p*, errores ni cadencia antes de calibración.

**B6.** Adoptar como contrato causal D2 las distinciones Z/política/provisión/instalación/accesibilidad, población/UE-UA-UO, condición de aislamiento, q_X*/g_A/r_common y jerarquía de estimandos; mantener bloqueada la materialización/identificación donde faltan roster, políticas factibles, soporte y evidencia.

## 10. Qué cerraría y qué no cerraría la aceptación

Si se aceptan B1–B6:
- queda cerrado el contrato lógico integrado de Paquete B;
- §51 deja de estar abierto en su estructura conceptual: coordenada, relaciones temporales, operador, EventHistory, S3 y horizonte quedan delimitados;
- quedan preservadas las reglas existentes y se elimina la necesidad de nuevas auditorías narrativas sobre las mismas distinciones;
- las dependencias no materiales quedan convertidas en criterios explícitos de materialización/calibración y no en ambigüedades semánticas.

No se considerarán cerrados ni identificados por aceptación:
- valor de ρ_follow, T*, K, Δ, cadencia, lag, pérdidas, errores, umbral p*, curva S3;
- roster, E_i, IAM/C_SRC, snapshots y composición material de población;
- asignación Z, π_h, ratio, estratos, algoritmo/semilla;
- aislamiento material, cluster o mapa de exposición;
- masas q_X*, par operativo g_A0/g_A1, certificados r_common;
- identificación/recuperación de θ_A;
- Outcome/Value, potencia, N/R, implementación o ejecución.

La aceptación de B1–B6 no autoriza materializar roster/datos, crear schemas/fixtures, modificar código, ejecutar tests, calibrar, simular, estimar o ejecutar el experimento. Esas autorizaciones seguirán separadas y se solicitarán cuando los paquetes C y D hayan definido el contrato completo.

## 11. Registro de aceptación

B1–B6 han sido aceptadas conjuntamente por el usuario. La aceptación se registra en el maestro, Decision Log y Closure Control Matrix, y se complementa con C10_S_PACKAGE_B_ACCEPTANCE_AND_SYNTHETIC_MATERIALIZATION_RECONCILIATION_DRAFT_001.md. El alcance aceptado cierra el contrato lógico integrado; la materialización pendiente corresponde al carril sintético S y no exige una instancia real M. La implementación S queda autorizada en la rama research, pero no la ejecución de tests, calibración, Monte Carlo ni experimento científico.

scientific_execution=false  
execution_authorized=false  
implementation_authorized=false


## 12. Aceptación y precisión de materialización sintética (2026-11-16)

B1–B6 quedan **ACEPTADAS** por el usuario como contrato lógico integrado. La aceptación se complementa con C10_S_PACKAGE_B_ACCEPTANCE_AND_SYNTHETIC_MATERIALIZATION_RECONCILIATION_DRAFT_001.md: C10-S es el carril S sintético; roster real, IAM/C_SRC, snapshots productivos e IS-1…8 del carril M no son prerequisitos del experimento sintético. Se reutilizan §§16.188–16.223, matriz 13×52, harness integrado, seed-bank protocol y contratos existentes. Las brechas sintéticas reales son D2 por etapas, q_X*/g_A0/g_A1/r_common/θ_A, EventHistory/event_time/IntervalAdjudication, parámetros temporales y S3 completo. Se autoriza implementar estas piezas en el harness existente dentro de la rama research; no se autoriza ejecutar tests, calibración, Monte Carlo ni experimento.

**Estado:** B1_B6_ACCEPTED / SYNTHETIC_MATERIALIZATION_REQUIRED / SCOPE_S_ONLY / IMPLEMENTATION_AUTHORIZED_S_ONLY / EXECUTION_NOT_AUTHORIZED.
