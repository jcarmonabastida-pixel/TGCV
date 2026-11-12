# C10-S — Auditoría de integración temporal, horizonte H y escenarios S4-R

**ID:** C10-S-TEMP-INT-001 · **Draft 001** · 2026-11-04
**Estado:** propuesta documental no aprobada. No autoriza ejecución.

## 1. Dictamen

Se detecta una ambigüedad: el inventario finito describe H=3 como tres pasos, cada uno ocupando una unidad discreta de tiempo; el contrato DGP sitúa Reach_H en t4, tras el snapshot t3 y antes de conocimiento, selección y ejecución. Deben separarse el reloj del estudio t0–t9, la profundidad de ruta k=0…H y el tiempo/ventanas internas de factibilidad.

## 2. Reconciliación propuesta

H=3 se conserva solo como profundidad máxima candidata (máximo tres transformaciones atómicas), no como tres unidades temporales ni como intervalo t4–t7. Las rutas del fixture F1→F2 y A1→A2 tienen longitud 2; no se añade un paso ficticio para llenar H. Duración, ventanas, caducidad de permisos/recursos y precedencias son variables separadas que requieren especificación. Por ello H=3 no está confirmado como horizonte temporal científico.

## 3. Evaluación temporal

- t0: asignación Z.
- t1: política B, recepción e intento.
- t2: verificación técnica y condiciones.
- t3: snapshot estructural postintervención; A_f, T_acc, ΔT_acc y App desde S0.
- t4: cálculo estructural de Reach_H y trayectorias candidatas sobre el snapshot t3.
- t5: conocimiento/consideración.
- t6: selección/inicio.
- t7: ejecución real.
- t8: Outcome.
- t9: Value.

Reach en t4 no se construye a partir de ejecuciones observadas. Cada paso potencial se evalúa desde su estado hipotético de entrada: accesibilidad, aplicabilidad, relación de composición, autorización, recursos, ventanas y bloqueos. Si se modelan actualizaciones dinámicas, cada rama requiere snapshots hipotéticos inmutables; nunca se sobrescribe el snapshot observado t3. Sin reglas de transición explícitas, no se inventan actualizaciones.

## 4. Correspondencia de escenarios

| Inventario | S4-R | Interpretación |
|---|---|---|
| R0: alternativa funcional ausente | S4R-A | Solo con cobertura exhaustiva del universo funcional. |
| R1: alternativa basal estable | S4R-B | B no modifica la alternativa; Reach puede no cambiar al abrir τ2. |
| R2: B modifica alternativa | S4R-C | Vía colateral; no asumir exclusión IV focal. |
| R3: provisión fallida | S4R-D | Asignación/intento no implica C_dep, A_f ni D_f. |

R0 no implica automáticamente pertenencia a P*_F: F*, frontera, granularidad, horizonte y ausencia respaldada deben definirse ex ante. El crosswalk no selecciona D1/D2.

## 5. Separaciones que debe preservar el DGP

A_f* es accesibilidad focal; T_acc* es el espacio completo; App*(τ,s) es aplicabilidad desde un estado; Rel* es composición; Feas*(π) es factibilidad conjunta de recursos, autorización, ventanas y bloqueos; Reach_H* es existencia de una ruta completa admisible. Selección, inicio y ejecución son posteriores.

## 6. Cobertura y pendientes

Se añaden dos dimensiones a las ocho ya propuestas: (9) semántica de horizonte —profundidad frente a duración, unidad, origen, límites y sensibilidad—; (10) factibilidad por rama —App, recursos, ventanas, caducidades y snapshots hipotéticos por prefijo—. Sin ambas no puede declararse exhaustividad.

Pendiente: ratificar H como profundidad o definir duración científica; fijar ventanas y reglas de recursos; formalizar actualizaciones de ramas; definir F* y objetivo; validar cobertura de alternativas; elegir D1/D2; construir oráculos y revisar independientemente. AUD-005 y AUD-007 siguen abiertos; tampoco se cierran AUD-004 ni OPEN-C10-001/003/005/007.

**Dictamen:** se propone separar reloj del estudio, profundidad y tiempo de factibilidad. No hay fixtures ejecutables, generación de datos, simulación ni ejecución.

## 7. Solicitudes B1: subledger temporal y no equivalencia con profundidad H (2026-11-11)

El ciclo de solicitud B1 se registra como eventos del servicio con timestamps y referencias a snapshots, no como pasos adicionales de profundidad transformacional H. La profundidad H cuenta pasos de una ruta transformacional admisible; no cuenta intentos, recepción, admisión o procesamiento de peticiones. No se asigna un evento de solicitud a t5/t6/t7 por analogía nominal. El enlace request↔trajectory y su cardinalidad permanecen OPEN.

Una carga de peticiones estandarizada puede presentarse en una ventana de evaluación fijada ex ante y común a brazos, después del snapshot de accesibilidad t3/t4, registrando el intento en el harness aunque no haya recepción. La oportunidad/carga no equivale a demanda natural ni cambia H. La ventana, calendario, relación con selección y ejecución, y horizonte de consecuencia siguen OPEN. No se altera el análisis de factibilidad por rama, reservas o recursos de las transformaciones.


## Decisión aceptada DEC-C10S-B1-REQUEST-MODE-001 (2026-11-11)

## Decisión DEC-C10S-B1-REQUEST-MODE-001 — modalidad de oportunidades estandarizadas y envío endógeno (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta la arquitectura de dos modalidades para C10-S:
1. **Modalidad primaria candidata:** oportunidades/peticiones estandarizadas, definidas ex ante antes de Z y presentadas mediante harness externo idéntico entre brazos después del snapshot de accesibilidad t3/t4. El harness registra Request_attempt aunque el servicio no reciba la petición. Esta modalidad permite comparar respuesta/capacidad bajo una carga de prueba común.
2. **Modalidad secundaria/adversarial:** envío endógeno de solicitudes, cuya ocurrencia puede depender de conocimiento, expectativas, accesibilidad percibida y otros estados post-Z. Se conserva para estudiar selección y vías causales, no para definir la población primaria ni filtrar el ITT.

**Límites de la aceptación.** La carga estandarizada es un probe experimental de servicio; no representa por sí sola demanda natural, preferencia revelada, beneficiario confirmado ni Value. Se mantienen separados intento, recepción, admisión/rechazo, procesamiento, respuesta, consecuencia del beneficiario, Outcome técnico y Value. Los eventos post-Z no se usan como criterio de inclusión o exclusión del ITT. Se conserva el reloj t−1/t0…t9 y no se equiparan eventos de petición con t5/t6/t7 ni con H.

**Pendiente de especificación:** calendario y ventana de presentación; unidad y cardinalidad de oportunidades; identidad y vínculo request_id↔trajectory_id; payload y reglas de admisión; repetición, timeout y errores; tratamiento de solicitudes no recibidas/pendientes; outcome técnico de respuesta; medida independiente de consecuencia B1 y su horizonte; población y soporte; relación exacta con los estimandos ITT/mediación. La modalidad secundaria no recibe estimando confirmatorio por esta decisión.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen scientific_execution=false y execution_authorized=false. No altera DEC-C10-066/067, D2 primario candidato/D1 secundario ni la rama base de PR #116.


## DEC-C10S-B1-OPPORTUNITY-CARDINALITY-001 — una oportunidad estandarizada por UE (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta **N_opportunities = 1 por unidad experimental (UE)** como configuración primaria candidata del probe estandarizado de servicio en el núcleo confirmatorio mínimo de C10-S. La oportunidad se define ex ante antes de Z y se presenta después del snapshot de accesibilidad t3/t4 mediante el mismo harness externo y bajo las mismas reglas en ambos brazos. El harness registra Request_attempt aunque no exista recepción por el servicio.

La identidad y el contenido de la oportunidad deberán ser comunes, trazables y versionados entre brazos. No recepción, rechazo, error o estado pendiente permanecen como estados observables; no se recodifican automáticamente como ausencia de necesidad, fallo transformacional, Outcome negativo ni Value=0. La población ITT no se condiciona a intento, recepción, admisión, procesamiento o respuesta post-Z.

Las oportunidades repetidas o cargas de mayor intensidad quedan reservadas a escenarios secundarios/adversariales; si se estudian, sus observaciones se anidan en la UE y no incrementan el número de unidades experimentales independientes. Esta configuración de una oportunidad no demuestra capacidad bajo carga sostenida ni demanda natural, preferencia revelada o Value del beneficiario.

Se mantienen abiertos: ventana/calendario exacto; definición final del payload y protocolo; identidad/versionado de B1 y servicio; cardinalidad request_id↔trajectory_id; tratamiento técnico de timeout, errores y pendientes; outcome técnico de respuesta; consecuencia independiente de B1 y horizonte; perspectiva/autoridad de valoración; población/soporte e integración exacta con ITT y mediación. No se equiparan eventos de petición con t5/t6/t7, ejecución transformacional, Outcome o Value, ni se amplía el reloj t−1/t0…t9.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen scientific_execution=false y execution_authorized=false. No altera DEC-C10-066/067, D2 primario candidato/D1 secundario, ni la separación main/PR #116.
## 8. Aceptación del ancla V_cont en t0 y separación del horizonte (2026-11-12)

Se acepta el inicio de la ventana de continuidad inmediatamente después de Z en t0, incluyendo toda la provisión e instalación. Esto no modifica el reloj causal ni la profundidad H: los eventos t0…t9 siguen siendo etapas ordenadas; H=3 sigue siendo profundidad máxima candidata; la rejilla V_cont es un tercer eje de K intervalos iguales.

La ventana se representa [t0,T*], con T* común, fijo y preespecificado. No se equipara automáticamente con t9, porque el reloj causal no aporta duración física. K, unidad temporal, resolución, duración mínima relevante y eventos/transitorios en fronteras siguen abiertos. La regla DEC-C10-100 de igual peso por intervalo permanece aplicable.

S3 es el canal runtime pasivo candidato y no añade probes/solicitudes. S4 conserva identidad/versionado/snapshot; S5 define el contrato ENABLED/PROFILE; S3 aporta evidencia temporal imperfecta. El ciclo de petición B1 permanece en su cardinalidad y contrato propios; no se usa como monitor repetido. Las observaciones temporales se anidan en UE/cluster, no aumentan N experimental.

**Dictamen:** START_T0_ACCEPTED / TEMPORAL_HORIZON_NOT_FIXED / K_NOT_DERIVED / S3_PASSIVE_CANDIDATE / NO_DESIGN_FREEZE / NO_EXECUTION_AUTHORIZED.


## 9. DEC-C10-102: continuidad estricta y derivación del reloj de V_cont (2026-11-12)

Se acepta continuidad estricta dentro de cada intervalo: el servicio debe cumplir ENABLED/PROFILE durante todo el intervalo para truth=1; cualquier incumplimiento funcional confirmado produce truth=0 para ese intervalo; truth=? se reserva a indeterminación generadora. No hay periodo de gracia ni duración mínima de fallo aprobada. Ausencia/pérdida de S3 no es truth=0 ni truth=1.

La truth del Generator y la observación S3 deben mantener resoluciones distintas y explícitas. Si S3 no puede detectar el evento relevante, el Analyzer produce bounds/abstención. Los timestamps exactamente en frontera requieren asignación determinista a un único intervalo.

Se conserva el inicio t0 aceptado en DEC-C10-101. Se recomienda un reloj explícito de tiempo transcurrido, con unidad normalizada, eventos fechados y rejilla regular. t0…t9 es orden causal, no tiempo físico; H=3 es profundidad transformacional; S6/S7 no definen la frecuencia de monitorización. T* debe cubrir provisión/instalación y seguimiento hasta el último evento causal que pueda modificar el cumplimiento B1 dentro del estimando.

K=(T*−t0)/Δ, Δ constante y divisibilidad exacta preespecificada. Unidad, T*, Δ, K, mínimo evento relevante, regla de cierre y capacidad/cobertura S3 siguen OPEN; no se inventan valores.

**Dictamen:** STRICT_INTERVAL_RULE_ACCEPTED / ELAPSED_TIME_GRID_RECOMMENDED / NUMERIC_TEMPORAL_PARAMETERS_OPEN / NO_DESIGN_FREEZE / NO_EXECUTION_AUTHORIZED.

## 10. Inventario de eventos y corrección de escala (2026-11-12)

La función B1 se conserva: admitir solicitudes si ENABLED=true, no admitir si ENABLED=false y exponer PROFILE declarado. El inventario se clasifica así:

- Provisión/instalación (programación, intento, recepción, aplicación, verificación, integridad, compatibilidad, operabilidad, rollback): antecedentes que pueden cambiar el estado efectivo, no truth por sí mismos.
- Configuración (ENABLED/PROFILE efectivos, identidad/versión): determinantes funcionales o de binding.
- Runtime (proceso/módulo, listener/socket/superficie, dependencias, capacidad/recursos cuando afecten admisión, caída/reinicio/recuperación): posibles cambios de capacidad funcional, observados imperfectamente por S3.
- Peticiones (oportunidad, intento, recepción, admisión/rechazo, procesamiento/respuesta): eventos discretos; no son monitor continuo. La ausencia de petición no implica fallo.
- Reach/selección/ejecución/F*/O-CONF/Outcome/Value: no son indicadores de A_B1.

Se distinguen event_time de truth, intervalos de agregación V_cont y timestamps/cobertura S3. Δ no es frecuencia S3. La rejilla estricta mide proporción de intervalos completamente conformes, no fracción exacta de uptime; depende de Δ y alineación. Se conserva DEC-C10-100/102 sin alterar sus fórmulas.

Convención recomendada: intervalos internos [b_k,b_{k+1}); frontera asignada al intervalo que comienza allí; T* incluido en el último intervalo. T* debe seguir al último evento causal por un seguimiento común τ_follow: T*=t_last+τ_follow. Catálogo finito, duración mínima representada, τ_follow, T*, Δ, K y capacidad/cobertura S3 permanecen OPEN. No se ejecuta ni materializa.

## 11. Dominio de episodios, detectabilidad y cierre terminal (2026-11-12)

Se reutilizan las cinco familias causales del contrato B1: (1) ENABLED/PROFILE efectivos; (2) proceso/módulo; (3) listener/socket/superficie de ingreso; (4) dependencias solo cuando impiden/restauran admisión; (5) capacidad/recursos solo cuando impiden/restauran admisión. Provisión, instalación, verificación, rollback y reinicio no son fallos automáticos. La adjudicación se basa en la función B1 efectiva, no en el nombre técnico.

No existe duración mínima funcional ni gracia: DEC-C10-102 hace que cualquier incumplimiento confirmado afecte a los intervalos que intersecte. δ_det es distinto: dominio de duración para el que S3 pueda demostrar detección tras calibración; no modifica truth. Para episodios inferiores o no cubiertos, Analyzer debe producir bounds/abstención si no hay otra evidencia pasiva identificable.

No se presupone el mecanismo de captura S3 (periódico, continuo o event-driven), ni independencia, cobertura completa o tasa de detección. Se deben especificar/cuantificar captura, resolución, lag, pérdida, cobertura y dependencia por componente. Δ es la rejilla de adjudicación, no la cadencia S3.

t_last es la última transición causal capaz de cambiar A_B1, incluida la recuperación final. T*=t_last+τ_follow, con τ_follow común preespecificado. Un episodio activo en T* se conserva como terminal/censurado y no se recodifica como recuperado. τ_follow, δ_det, Δ, T* y K se derivarán conjuntamente tras fijar unidad normalizada y catálogo de escenarios.

**Dictamen:** EVENT_DOMAIN_BOUNDED / NO_GRACE / DETECTION_NOT_TRUTH / TERMINAL_CENSORING_EXPLICIT / TEMPORAL_PARAMETERS_OPEN.


## 12. Reloj adimensional y cierre temporal S3 (2026-11-12)

La escala de tiempo se normaliza sin atribución física: W_c=t_c,max−t0 cubre el soporte común de transiciones causales del DGP; x=(t−t0)/W_c, t0=0 y t_c,max=1. No se identifica con t9, H ni una duración real. La cola ρ_follow=τ_follow/W_c permanece abierta; T*=1+ρ_follow, común y preespecificado.

Las duraciones de episodios d_e=δ_event/W_c son positivas y se exploran en un soporte sintético declarado. Cualquier d_min,DGP limita solo ese benchmark y no introduce periodo de gracia ni mínimo funcional. DEC-C10-102 sigue adjudicando como 0 todo intervalo intersectado por un incumplimiento confirmado.

El canal S3 pasivo existente se evalúa bajo tres mecanismos: snapshots/métricas, logs/trazas/eventos runtime e híbrido. No se presupone captura event-driven, periodicidad, completitud ni independencia. Se estiman curvas conjuntas de detección por duración/fase/familia/versión, incluyendo lag, pérdida, cobertura, falsos positivos/negativos y dependencia. δ_det escalar requiere un umbral p* aprobado; antes se informa la curva y bounds/abstención.

Δ, cadencia S3, duración del episodio y cola de seguimiento no se identifican entre sí. K es entero y Δ=(1+ρ_follow)/K; K/Δ se eligen por recuperación de truth y análisis de aliasing, y ρ_follow por soporte de persistencia/recuperación. La regla de frontera [b_k,b_{k+1}) queda recomendada, pendiente de versionado previo a materialización.

**Estado:** NORMALIZED_COORDINATE_ONLY / NO_PHYSICAL_TIME_CLAIM / STRICT_TRUTH / S3_MODES_NOT_CALIBRATED / TEMPORAL_PARAMETERS_OPEN.


## 13. Horizonte común y reconciliación de t_last (2026-11-12)

Se distingue t_last,i (última transición efectiva de una unidad) de t_last^max=t_c,max (límite superior ex ante del soporte de transiciones posibles en todos los brazos/escenarios). La ventana confirmatoria común termina en T*=t_last^max+τ_follow, no en un extremo retrospectivo específico de cada unidad. Esto conserva seguimiento comparable y evita que el horizonte dependa de eventos post-Z observados. Un episodio activo en T* permanece terminal/censurado; si el soporte de transiciones no puede acotarse ex ante, T* sigue OPEN.


## 14. Crosswalk de escenarios temporales y contratos de medición (2026-11-12)

Los episodios temporales se alojan en los perfiles DGP ya existentes (§16.188.4), sin abrir una batería nueva: control de truth estable/señal espuria; fallo por etapas de provisión/instalación; interrupción B1 funcional; vía colateral de observabilidad diferencial; interacción por fase/duración/cobertura; medición adversarial con pérdida y dependencia; soporte/interferencia/versionado; y discriminación entre secuencia V_cont y O-CONF terminal.

S3 se contrasta bajo snapshots/métricas, logs/trazas/eventos e híbrido como mecanismos del mismo canal pasivo. Se conservan fase, retardo, pérdida, cobertura, validez, error y dependencia conjunta. No se presume independencia ni completitud.

Se reutilizan P182-07/08/11/12, P183-01/02/04/07/09/10/11 y P182-04/10, junto con MEAS/MISS existentes. No se crean IDs ni se afirma implementación/ejecución. La salida es estimación solo si identificada; si no, bounds o abstención. La verdad se abre únicamente tras sellado del Analyzer.

**Estado:** TEMPORAL_SCENARIOS_MAPPED_TO_EXISTING_PROFILES / NO_NEW_TESTS / NOT_EXECUTED.


## 15. Matriz adimensional de cobertura y selección temporal (2026-11-12)

La matriz de episodios usa r_c=d_e/c_j y r_Δ=d_e/Δ, con estratos menores/iguales/mayores que 1; fase alineada, desfavorable y aleatoria para snapshots; y captura, pérdida/no emisión o retardo para logs/trazas. Los canales híbridos conservan dependencia. La cobertura es dirigida, no factorial completa, y reutiliza los escenarios y P182/P183 ya existentes.

Se incluyen controles truth estable/señal espuria, episodio breve entre capturas, frontera de captura, episodio largo, fallo breve que afecta el bloque entero, cruce de frontera de rejilla, pérdida diferencial, errores correlacionados, recuperación y censura en T*, y discriminación O-CONF/V_cont.

Si el soporte de recuperación tiene máximo defendible, τ_follow debe cubrirlo; de lo contrario se informa censura. K/Δ se seleccionan por recuperación de truth, aliasing, fase, estabilidad al refinar K y criterios de error/cobertura aún pendientes. No se fija parámetro numérico ni se ejecuta.


## 16. Registro paramétrico temporal y corrección de V_cont (2026-11-12)

Se incorpora el registro del plan §16.198: inicio/fin de episodios, familia causal, soporte DGP, recurrencia, recuperación, horizonte común, rejilla, cadencia/fase/cobertura S3, emisión/captura, lag, pérdida, error y dependencia conjunta. No se asignan leyes ni cifras por defecto. La parametrización es condicional al escenario y versión; el canal híbrido conserva la dependencia conjunta.

Se corrige la interpretación: V_cont_truth es proporción de intervalos completamente conformes, no fracción exacta de tiempo disponible. Un incumplimiento confirmado afecta a cada intervalo que intersecta; la medida depende de Δ y de la alineación. DEC-C10-100/102 se conservan sin modificación. No se crean pruebas ni se ejecuta calibración.
