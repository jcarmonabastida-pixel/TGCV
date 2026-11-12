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
