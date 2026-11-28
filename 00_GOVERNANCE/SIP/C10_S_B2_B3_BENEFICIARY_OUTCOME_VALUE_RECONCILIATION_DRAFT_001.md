# C10-S — B2–B3: reconciliación integrada de beneficiario, Outcome técnico y Value contextual

**ID:** C10-S-B2-B3-RECON-001  
**Fecha:** 2026-11-11  
**Estado:** B2_B3_WORKING_BASIS_ACCEPTED / SEMANTIC_RECONCILIATION_DOCUMENTED / OUTCOME_NOT_OPERATIONALIZED / VALUE_NOT_INSTANTIATED / NOT_DESIGN_FROZEN  
**Rama:** `research/c10-s-consolidation-draft` · PR #116  
**Ámbito:** variante B y crosswalk con Outcome de A; no modifica A ni las decisiones de población/D2.  
**Autoridad y precedencia:** DEC-C10-095; C10S-B-VALUE-MIN-001; C10S-B1-REQUESTER-CANDIDATE-001; DEC-C10S-B1-UNIT-001; DEC-C10S-B1-REQUEST-MODE-001; DEC-C10S-B1-OPPORTUNITY-CARDINALITY-001; DEC-C10S-B1-REQUEST-TRAJECTORY-LINK-001; DEC-C10S-B1-CAUSAL-ADJUDICATION-001; DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001; PA §267; PB §§271–272; PC §268; PD §269; PE §270; C-Value §224; P179/P182/P183.

## 1. Dictamen ejecutivo

Se registra la aceptación expresa del usuario del siguiente planteamiento como **base de trabajo B2–B3**:

- B1 es la entidad sintética solicitante-beneficiaria cuyo objetivo/necesidad existe antes de Z.
- Outcome representa un resultado técnico del servicio/proceso, medido con un contrato independiente.
- Value representa la consecuencia valorada para B1 respecto de su objetivo basal, desde una perspectiva y regla de valoración estipuladas ex ante.

La aceptación es una orientación semántica para completar la especificación. **No es Design Freeze ni una nueva decisión científica**, y no selecciona dimensiones, indicadores, escalas, pesos, horizontes, parámetros o instancias materiales.

**Precisión causal incorporada:** Outcome y Value son constructos distintos, pero no se impone una relación causal exclusiva Outcome→Value. La consecuencia valorada puede depender del resultado técnico, de otras condiciones o de vías directas/colaterales de la política. No se define Value como una función mecánica de Outcome, accesibilidad, Reach, selección o ejecución. La relación entre esos constructos es una cuestión del DGP y de los estimandos, no una identidad semántica.

## 2. Reconstrucción histórica y reutilización

Este ciclo no crea una arquitectura de beneficiario o Value desde cero. Reutiliza:

- §224 y sus fichas versionadas independientes de Outcome y Value.
- DEC-C10-095: A como base técnica y B como extensión sintética separada para Value contextual.
- B1 como tipo candidato solicitante-beneficiario; una B1 por UE; contrato/plantilla de servicio común e instancia lógica de servicio única/versionada por UE.
- Need_preZ, E_req_preZ, Request_event, D_resource, procesamiento y consecuencia B1, ya separados en el contrato B1.
- Una oportunidad estandarizada por UE, modalidad primaria de probe y enlace request↔trajectory tipado.
- P179: Value vectorial durante identificación y preservación de trade-offs.
- P182/P183: validez, fiabilidad, error, acuerdo, ausencia, selección, censura, sensibilidad y dictamen por estimando/dimensión.
- PA §267, PC §268, PD §269 y PE §270: límites de Outcome/Value, estimandos, truth/evidence/evaluation y contratos técnicos.
- PB-MAT §§271–272: identidad lógica de servicio por UE y límites materiales.

Las menciones históricas a beneficiario, modalidad, cardinalidad o instancia que aparezcan como OPEN antes de las decisiones posteriores se interpretan con la precedencia de estas decisiones, sin borrar el registro histórico. No se duplican IDs de decisión ni de test.

## 3. Contrato B2 — entidad beneficiaria y necesidad basal

### 3.1 Identidad y relación

B1 sigue siendo una entidad lógica sintética; solicitante y beneficiario coinciden por estipulación explícita del modelo B1. No es la UE, el servicio, el actor ejecutor ni el Evaluator.

Se conserva:
- una B1 por UE, con identidad y provenance propias;
- relación explícita/versionada B1↔UE;
- relación explícita B1↔unidad lógica de servicio;
- contrato/plantilla CMP/PAR/RUL común e instancia de servicio única/versionada por UE;
- una oportunidad estandarizada por UE en el probe primario.

La identidad lógica está definida documentalmente. No hay roster material completo, IDs concretos por UE ni evidencia de aislamiento efectivo; el cierre de B2 no se confunde con materialización.

### 3.2 Need_preZ y estados

`Need_preZ` es la necesidad/objetivo focal de B1 existente en la verdad del DGP antes de Z. Su existencia no depende de haber formulado, enviado, recibido, admitido o procesado una petición.

Se mantienen estados:
- `1`: la necesidad/objetivo focal existe según la definición basal del DGP;
- `0`: no existe esa necesidad focal definida;
- `?`: verdad o clasificación no determinada.

La evidencia observada del Analyzer se mantiene separada de truth_dgp. La ausencia de evidencia no se convierte en Need_preZ=0.

### 3.3 Distinciones no intercambiables

| Objeto | Significado | No equivale a |
|---|---|---|
| Need_preZ | Necesidad/objetivo basal de B1 | Solicitud, uso o resultado |
| E_req_preZ | Elegibilidad basal de petición/solicitante, si el contrato la define | E_i o pertenencia a P*τ2 |
| Request_event | Oportunidad, intento o petición efectivamente registrada | Existencia de necesidad |
| D_resource | Demanda operativa de recursos/capacidad del servicio | Necesidad del beneficiario o coste económico |
| Service_processing | Admisión, rechazo, procesamiento, fallo o pendiente | Satisfacción de necesidad |
| Technical Outcome | Resultado técnico adjudicado | Consecuencia valorada o Value |
| Beneficiary_consequence | Cambio en la situación de B1 respecto de Need_preZ | Resultado técnico por sí solo |
| Value V_j | Valoración contextual de la consecuencia desde perspectiva estipulada | Outcome o accesibilidad recodificados |

Request_event=0 no demuestra Need_preZ=0. Request_event=1 no demuestra admisibilidad, procesamiento, éxito técnico ni satisfacción. La no recepción, rechazo, error, pendiente o no ejecución no se recodifican como ausencia de demanda ni como Value=0.

La población ITT no se condiciona a eventos post-Z. Las decisiones de cardinalidad y oportunidad aceptadas no se reabren.

## 4. Contrato B3 — Outcome técnico

### 4.1 Definición de clase

Outcome técnico es un resultado del servicio/proceso técnico, adjudicado con respecto a un criterio funcional u operativo independiente y versionado. Describe qué resultado técnico se produjo en la unidad/episodio/horizonte pertinente; no expresa por sí mismo cuánto valor tiene ese resultado para B1.

Outcome no es:
- intento, recepción, instalación o C_dep*;
- A_f*, D_f*, ΔT_acc*, Reach o trayectoria;
- selección o ejecución;
- Value o satisfacción del beneficiario.

### 4.2 Candidatos históricos y dictamen

| Candidato | Anclaje histórico | Estado vigente |
|---|---|---|
| O-CONF | F*/FP-01…08; conformidad funcional del destino | Mejor anclaje conceptual; ficha §224 incompleta |
| O-MIG | Estado terminal de migración | Sin evento/campo terminal ni regla adjudicativa |
| O-SVC | Continuidad/operación del servicio | Sin SLI/SLO, unidad/ventana o fuente validada |
| O-REC | Recuperación/restauración | Sin definición de fallo, inicio/fin y estado restaurado |
| O-BUR | Carga/esfuerzo/coste operativo | Sin medida validada de esfuerzo/coste ni perspectiva |

O-CONF se conserva como candidato prioritario para operacionalización, no se declara seleccionado confirmatoriamente ni operacionalizado. F* es el criterio técnico; el resultado observado/adjudicado debe distinguirse de la especificación objetivo y de truth_dgp. Las superficies de telemetría, provisión y recursos no constituyen automáticamente indicadores Outcome.

### 4.3 Ficha O_k

Cada Outcome que se pretenda usar requiere ficha §224 propia: identidad/versionado; constructo; unidad/episodio; criterio y dirección; predicados/terminalidad; fuente y evidencia; unidad/escala/cálculo; baseline; ventana/horizonte; oráculo/adjudicación; mapping/tolerancias justificadas; validez; error; acuerdo interevaluador; cegamiento; ausencia/censura/disputa/unknown; provenance. P182/P183 se aplican por Outcome.

No se fuerza una medida única ni se transfieren resultados entre Outcomes.

## 5. Contrato B3 — Value contextual para B1

### 5.1 Definición

Value expresa la valoración contextual de una o más consecuencias experimentadas por B1 respecto de Need_preZ, desde una perspectiva y autoridad de valoración estipuladas ex ante en el DGP.

La consecuencia debe poder describirse sin presuponer que el servicio la haya producido ni que el resultado técnico haya sido favorable. Puede haber progreso, cumplimiento, resolución parcial, no resolución o consecuencias adversas, según la definición que se justifique. No se selecciona aquí una consecuencia concreta.

### 5.2 Perspectiva y autoridad

La perspectiva debe ser atribuible a B1 o a una regla de valoración que represente explícitamente el interés de B1 dentro del mundo sintético. El Evaluator aplica la regla; no se convierte por ello en beneficiario. La autoridad que legitima la regla es una estipulación del DGP, no una preferencia real validada empíricamente.

No se infiere perspectiva desde CMP.owner, operador, mantenedor, actor ejecutor, servicio, telemetría o disponibilidad de recursos.

### 5.3 Vector y dimensiones

Se mantiene P179: Value se representa como vector `V=(V_1,…,V_k)` durante identificación, preservando trade-offs y dictámenes por dimensión.

No se seleccionan por defecto las cinco dimensiones históricas (eficiencia, calidad, acceso de destinatarios, robustez y sostenibilidad); no se declaran exhaustivas ni obligatorias. No se reduce Value a escalar, no se imponen pesos ni regla compensatoria. Una dimensión única, si finalmente se justifica, requerirá documentar por qué la reducción es adecuada al contexto.

Cada V_j necesita ficha §224 independiente.

## 6. Separación causal Outcome–consecuencia–Value

La arquitectura conceptual que se acepta no es una equivalencia ni una cadena exclusiva. Su representación mínima es:

`Z → política/paquete → proceso técnico → Outcome técnico`

y, en paralelo, con rutas potencialmente mediadas y no mediadas:

`Z/paquete → (ΔT_acc*, Reach, trayectoria, selección/ejecución, Outcome y vías colaterales) → consecuencia B1 → V_j`

Need_preZ y la perspectiva de B1 son basales. Outcome puede contribuir a la consecuencia valorada, pero no la agota. Coste, demora, riesgo, calidad, información, esfuerzo, alternativas u otras consecuencias pueden introducir vías adicionales, según truth_dgp y evidencia.

Reglas:
1. Outcome no se convierte automáticamente en Value.
2. Value no se calcula como función mecánica de Outcome, ΔT_acc*, Reach, trayectoria, selección o ejecución.
3. La relación causal Outcome→consecuencia→Value, si existe, se define y prueba en el DGP; no se presupone por definición.
4. Una vía directa/colateral Z→consecuencia/Value conserva el ITT como efecto de política/paquete y bloquea atribución exclusiva a accesibilidad si no se identifica por otro diseño.
5. La medición de Outcome y Value debe ser conceptualmente y operacionalmente separable, aunque puedan compartir fuentes si se justifica y se controlan dependencia y circularidad.
6. La regla de valoración y su aplicación son simétricas entre brazos, fijadas ex ante y cegadas a Z cuando sea viable.

## 7. Estimandos y no transferencia de identificación

Para cada variante, población, resultado/dimensión y horizonte se requiere un dictamen independiente:

- `ITT_Z^{D2}(O_k)`: efecto de asignación sobre Outcome técnico O_k.
- `ITT_Z^{D2}(V_j)`: efecto de asignación sobre cada dimensión Value V_j.
- `θ_A(q;O_k)` o `θ_A(q;V_j)`: efecto de accesibilidad solo con intervención/políticas, soporte, régimen común y supuestos correspondientes.
- Mediación C4 sobre O_k o V_j: estimando separado, con intervención mediadora, confusión longitudinal, soporte secuencial y supuestos explícitos.
- Efecto de paquete: interpretación válida del ITT cuando las vías colaterales no se excluyen/identifican.
- Agregación de V_j: solo mediante regla aceptada y justificada; no se deriva del vector.

No se transfiere identificación de ITT sobre O_k a ITT sobre V_j, de una V_j a otra, ni de un Outcome a C3/C4. La no-identificación o indeterminación es un resultado admisible.

## 8. Contratos de medición §224, P182 y P183

Para cada O_k y V_j, la ficha debe cerrar según aplicabilidad:

- constructo, perspectiva/beneficiario, unidad de análisis y población;
- evidencia/fuente, provenance, versión y mapping;
- unidad, escala, cálculo, baseline y horizonte/ventana;
- criterio/dirección y adjudicación, incluidos casos limítrofes;
- validez, fiabilidad, error y acuerdo interevaluador (P182);
- invariancia y sensibilidad de la medida/regla;
- cegamiento e independencia de adjudicación;
- estados OBSERVED_VALID, OBSERVED_INVALID, NOT_OBSERVED, NOT_APPLICABLE, CENSORED, DISPUTED y UNKNOWN según contrato aplicable;
- mecanismos de ausencia y selección, MCAR/MAR/MNAR, censura, cotas y sensibilidad (P183);
- trade-offs y relaciones con otras dimensiones cuando se trate de Value.

No observado, no aplicable, censurado, disputado y desconocido no se colapsan ni se recodifican como cero. El baseline Need_preZ no se redefine por observación post-Z.

## 9. Truth, observed_evidence y evaluation

La arquitectura PE/PD se conserva:
- **truth_dgp:** Need_preZ, potenciales, consecuencias, contribuciones causales, mecanismos, resultados verdaderos y versiones;
- **observed_evidence:** registros y mediciones permitidos al Analyzer, con error, cobertura, missingness y provenance; no contiene etiquetas contrafactuales reservadas;
- **evaluation/adjudication:** compara la inferencia sellada del Analyzer con truth, informa errores y recuperación, y no altera retrospectivamente las observaciones.

La medición de B1/Outcome/Value debe respetar el firewall Generator/Analyzer/Evaluator. La verdad del DGP no se presenta como dato observable.

## 10. Matriz integrada de estado

| Elemento | Estado |
|---|---|
| B1 como tipo solicitante-beneficiario | ACCEPTED CANDIDATE TYPE |
| Una B1 por UE | ACCEPTED DESIGN DECISION |
| Identidad lógica de servicio por UE | ACCEPTED DOCUMENTALLY; aislamiento material no probado |
| Need_preZ vs Request_event vs D_resource | Distinción conceptual definida; contenido/medición OPEN |
| Consecuencia B1 independiente | Delimitada semánticamente; no operacionalizada |
| Perspectiva/autoridad de valoración | OPEN |
| Outcome técnico como constructo distinto | Aceptado como base semántica |
| O-CONF | Mejor candidato técnico; ficha §224 incompleta |
| Otros O_k | Candidatos sin operacionalización |
| Value vectorial P179 | Regla metodológica conservada |
| Dimensiones V_j | No seleccionadas |
| Indicadores, escalas, fuentes, baseline, horizonte y adjudicación | OPEN |
| Relación causal Outcome–consecuencia–Value | No impuesta; verdad/mecanismos DGP OPEN |
| ITT sobre O_k y V_j | Familias separadas; no estimandos confirmatorios completos |
| C3/C4 sobre O/V | No identificados en D2 material actual |
| Implementación/fixtures/simulación/ejecución | NOT AUTHORIZED |

## 11. Criterios de cierre B2–B3 y bloqueos

El cierre semántico documental de este ciclo no satisface todavía el gate de instancia/medición. Para una especificación confirmatoria siguen siendo necesarios:

1. contenido y versión de Need_preZ y su evidencia;
2. instancia/provenance material B1 y su relación con UE/servicio;
3. perspectiva y autoridad de valoración;
4. consecuencia(s) B1 y horizonte;
5. selección justificada de O_k y V_j, sin imponer dimensiones históricas;
6. fichas §224 completas por indicador/dimensión;
7. fuentes, instrumentos, escalas, baseline, adjudicación y error;
8. mecanismos de ausencia/censura y sensibilidad P183;
9. DAG/contrastes por resultado, incluidas vías colaterales;
10. soporte, asignación, interferencia y mapping ya abiertos en PA–PC;
11. separación técnica de truth/evidence/evaluation y controles de rol PE.

Estos bloqueos son de definición y materialización; no requieren otra decisión de preferencia en este ciclo. No se inventan roster, dimensiones, valores, pesos, métricas, instrumentos, horizontes, N/R o parámetros.

## 12. Dictamen y autorización

**B2–B3: WORKING BASIS ACCEPTED / SEMANTIC RECONCILIATION DOCUMENTED / OPERATIONALIZATION OPEN.**

Se acepta B1 como referente de la necesidad y consecuencia valorable; Outcome técnico y Value contextual quedan diferenciados. La consecuencia de B1 no se reduce al Outcome ni se presupone que este sea su única causa. P179, P182, P183 y §224 se conservan como contratos rectores.

No se modifica DEC-C10-095, D2, población P*τ2/P*_F, A, Opción A, TGCV Core, RMA, Evidence→Claim Matrix, STATUS ni claims. No se crea una decisión científica nueva ni se declara Outcome/Value operacionalizado, C3/C4 identificado o Design Freeze.

`scientific_execution=false`; `execution_authorized=false`. No schema físico, fixtures, implementación, generación de datos, simulación, estimación o ejecución científica.


## 13. Reconciliación de operacionalización confirmatoria Outcome/Value (2026-11-11)

La operacionalización integrada se desarrolla en `C10_S_OUTCOME_VALUE_OPERATIONALIZATION_RECONCILIATION_DRAFT_001.md` y se incorpora al maestro §276. Se precisa que F* es criterio funcional y O-CONF el resultado adjudicado de conformidad del destino; no son dos endpoints técnicos independientes. O-CONF sigue candidato prioritario, no seleccionado ni operacionalizado: predicados, mapping/IAM, C0/G/H, snapshots, evento terminal y oráculo independiente validado siguen OPEN.

Value conserva vector P179. B1 es el referente y Need_preZ es basal; perspectiva B1 se mantiene como base aceptada, pero autoridad/criterio de valoración y consecuencia no están instanciados. No se seleccionan dimensiones, k, indicadores, escalas, pesos o agregación. Las cinco dimensiones históricas siguen siendo candidatas no exhaustivas; no se infiere Value desde Outcome, ΔT_acc*, accesibilidad, ejecución, telemetría o recursos.

Se reutilizan §224, P179-01…08, P182-01…12, P183-01…13 y MEAS/MISS existentes sin duplicar tests. ITT Outcome y Value permanecen separados; C3/C4 no identificados en diseño material actual. No Design Freeze ni autorización de captura/implementación/ejecución.

## 14. Caso de valoración B1 y consecuencia contextual (2026-11-11)

El caso semántico se desarrolla en `C10_S_B1_VALUATION_CASE_RECONCILIATION_DRAFT_001.md`. Reutiliza las decisiones aceptadas de B1/UE, servicio por UE y una oportunidad estandarizada por UE. Se aclara que el probe no representa demanda natural ni constituye Value. Need_preZ se formula como objetivo operativo basal relacionado con sostener una operación de servicio predeclarada en el entorno destino, pero la operación concreta sigue OPEN; no se fija truth ni se crea decisión. La consecuencia B1 es un cambio respecto de ese objetivo y se mantiene distinta del procesamiento, respuesta, F*, O-CONF y accesibilidad. La envolvente de consecuencias es analítica, no selección de V_j. Perspectiva B1 aceptada como base; autoridad, criterio, medidas, horizonte y dimensiones OPEN.


## 15. Aceptación de la clase de propósito basal B1 (2026-11-11)

Se acepta como base semántica de trabajo que B1 tiene un objetivo operativo basal consistente en mantener operativa una función de servicio que depende de la configuración migrada al entorno de destino. La aceptación fija la clase de propósito y su relación con B1/configuración/servicio, pero no nombra la operación concreta. En consecuencia, Need_preZ no está todavía instanciado como truth por UE ni la población de Value puede clasificarse materialmente.

Se conserva la definición pre-Z y la distinción 1/0/?: 1 cuando existe el objetivo concreto ya especificado; 0 cuando no existe según la definición del DGP; ? cuando no puede determinarse. La clase aceptada no asigna 1 automáticamente a todas las UE. La falta de Request_event/evidencia/procesamiento no demuestra 0. La clasificación no puede depender de Z, provisión, accesibilidad, Reach, oportunidad, petición, Outcome o ejecución; tampoco puede filtrarse la población ITT por eventos post-Z.

La consecuencia de B1 se define respecto del propósito basal concreto y permanece distinta del proceso técnico y O-CONF. La envolvente de consecuencias existente es analítica, no roster de V_j. Autoridad normativa, criterio, dimensión, fuente, instrumento, escala, baseline y horizonte siguen OPEN. No se selecciona Value confirmatorio ni se modifica la separación Outcome/Value.

Artefacto rector: `C10_S_B1_VALUATION_CASE_RECONCILIATION_DRAFT_001.md` §12. Estado: PURPOSE_CLASS_ACCEPTED / CONCRETE_OPERATION_OPEN / NEED_PREZ_NOT_MATERIALIZED / CONSEQUENCE_MEASUREMENT_OPEN. No Design Freeze ni autorización de implementación/ejecución.


## 16. Precedencia posterior: DEC-C10-099 y contrato sintético de V_cont (2026-11-12)

Las declaraciones históricas de §§13–15 que indicaban que no se seleccionaba ninguna dimensión V_j reflejan el estado anterior a la aceptación posterior registrada en DEC-C10-099. Para la extensión sintética B, V_cont queda seleccionada provisionalmente como dimensión mínima única, sin alterar la regla vectorial P179 ni las decisiones de A. Esa selección no instancia materialmente Value ni cierra la consecuencia/medición en el mundo real.

La especificación sintética de truth temporal y canal S3 se desarrolla en el plan C10-S §16.182. El Generator estipula la capacidad operativa por intervalo; S3 aporta indicadores runtime pasivos e imperfectos, no prueba funcional directa. La recuperación puntual requiere calibración/identificación accesible al Analyzer; de otro modo corresponde bounds o NOT_IDENTIFIED. No se aprueba una agregación, ventana, K, frecuencia, baseline, instrumento empírico ni regla de valoración final. O-CONF/F* sigue sin operacionalización terminal validada y la discriminación permanece CONDITIONAL/NOT_VERIFIABLE.

Estado reconciliado: `V_CONT_SELECTED_PROVISIONALLY / SYNTHETIC_MEASUREMENT_SPECIFIED_CONDITIONALLY / MATERIAL_VALUE_NOT_INSTANTIATED / O_CONF_NOT_OPERATIONALIZED / NO_DESIGN_FREEZE / NO_EXECUTION_AUTHORIZED`.


## 17. Precedencia funcional B1 y frontera temporal/terminal (2026-11-12)

La formulación histórica de §§14–15 que mantenía abierta la operación concreta queda precisada por el contrato funcional B1 §2: el objetivo es mantener disponible en destino un servicio capaz de admitir solicitudes conforme a ENABLED y exponer PROFILE. La función del servicio está especificada a nivel del contrato; el contenido material de solicitudes/perfiles puede seguir abstracto en el DGP sintético. No se solicita una nueva definición al usuario.

V_cont representa cumplimiento temporal de esa función, no Need_preZ ni el resultado de la oportunidad única. F* juzga la conformidad de la ruta/estado terminal aplicado; O-CONF es su adjudicación 1/0/? y no incluye actualmente una regla temporal para toda la ventana. Los contrastes candidatos y sus límites se documentan en el plan §16.183. La discriminación final sigue NOT_VERIFIABLE hasta cerrar predicados F*, evento terminal y oráculo O-CONF.

Estado: `B1_FUNCTIONAL_REFERENCE_SPECIFIED / V_CONT_TEMPORAL_SCOPE / O_CONF_TERMINAL_SCOPE / DISCRIMINATION_CONDITIONAL / NO_DESIGN_FREEZE`.
