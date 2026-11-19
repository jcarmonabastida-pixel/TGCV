# C10-S — Matriz de reconciliación P179/P182/P183 y núcleo mínimo Outcome/Value

**ID:** C10-S-VALUE-MIN-001  
**Versión:** Draft 001  
**Estado:** DRAFT / PROPUESTA DE RECONCILIACIÓN / NO ACEPTADA / NO CONGELADA  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116  
**Ámbito:** C10-S, paquete C-Value; no autoriza implementación ni ejecución.

## 1. Propósito y regla de precedencia

Esta matriz depura el contenido de P179, P182 y P183 frente al contrato histórico C-Value (§224), su especialización actual (§§264–265) y el crosswalk contra la instancia real `C10S-SVC-REQUEST-PROCESSOR v1.0.0` (§265; roster §232; DAG §233; superficies B-M01…15).

No crea una taxonomía adicional, no sustituye contratos fuente y no convierte dimensiones candidatas en variables obligatorias. La fuente normativa y sus decisiones aceptadas prevalecen; esta matriz es una propuesta de integración que debe cotejarse contra el texto íntegro de cada contrato antes de su aceptación.

Regla de no invención: ningún beneficiario, stakeholder, función de utilidad, indicador, escala, ponderación, umbral, horizonte ni estado terminal se presume por analogía. Un dato ausente se registra como OPEN/UNKNOWN, nunca como cero ni como evidencia de inexistencia.

## 2. Fuentes y alcance recuperado

| Fuente | Contenido contractual recuperado | Estado/limitación |
|---|---|---|
| P179-01…08 (§55.3 del Test Contract Register) | Separación A/O/V; vector por dimensión; independencia Outcome/Value; observador/beneficiario/contexto/criterio; baseline; trade-offs; estimación causal por dimensión; agregación justificada | Contrato definido; operacionalización abierta. El vector multidimensional es la opción metodológica recomendada durante identificación. |
| P182-01…12 (§13 del Test Contract Register) | Cobertura y circularidad de A; especificación O; separación O/V; reproducibilidad; acuerdo interevaluador; error en A y O/V; invariancia; sensibilidad de Value; firewall Generator/Analyzer; trazabilidad | Contratos definidos; pruebas/evidencia no ejecutadas. |
| P183-01…13 (§13 del Test Contract Register) | Taxonomía y mecanismo de ausencia; separación A/O/V; ITT; selección; mediación; censura; sensibilidad MAR/MNAR; cotas; dictamen por estimando; trazabilidad | Contratos definidos; parámetros y mecanismos concretos abiertos. Exige dictámenes separados por estimando y dimensión. |
| C-Value §224 (maestro; resumen en plan §16.102) | Fichas versionadas independientes para cada indicador O y dimensión V; constructo, evidencia y adjudicación; fuentes, unidades/escalas, cálculo, baseline, ventana/ancla, validez, error, acuerdo, ausencia/censura, cegamiento, trade-offs y provenance | Contrato operativo propuesto; fichas concretas e indicadores no seleccionados. |
| C-Value §§264–265 (plan §§16.138–16.139) | Crosswalk candidato para Opción A; familias O-MIG/O-CONF/O-SVC/O-REC/O-BUR; roles/dimensiones Value candidatos; crosswalk al roster y DAG reales | Candidato documentado; materialmente abierto. Beneficiarios, indicadores, fuentes, escalas, ventanas y reglas de valoración no confirmados. |
| §232 / §233 / B-M01…15 / E_T-U_G | Roster, DAG y superficies de observación de la instancia | Una superficie no equivale a indicador validado, beneficiario ni evidencia de valoración. |
| C10_S_RECOVERY_165_183_SOURCE_REGISTER_DRAFT_001 | Recuperación de la recomendación vectorial P179 y del alcance de P182/P183 | Fuente auxiliar de trazabilidad; no sustituye las fichas contractuales del Test Contract Register. |

## 3. Matriz de depuración de dimensiones candidatas

Las cinco dimensiones que aparecen en la recuperación histórica —eficiencia, calidad, acceso de destinatarios, robustez y sostenibilidad— son **candidatas provisionales**, no una lista aprobada ni cinco obligaciones de medición. P179 recomienda mantener Value como vector durante la fase de identificación, precisamente para no ocultar trade-offs mediante agregación prematura. Por tanto, no debemos sustituir esa recomendación por un escalar ni reducir de entrada el vector a un único V1.

| Dimensión candidata | Fundamento posible | Riesgo/laguna en Opción A | Dictamen propuesto |
|---|---|---|---|
| Eficiencia | Valoración de recursos, tiempo o esfuerzo desde una perspectiva identificada | Recursos/rendimiento técnicos no equivalen a coste económico ni esfuerzo de un beneficiario | CONDITIONAL |
| Calidad | Valoración de propiedades del servicio/resultado | F* y conformidad técnica no equivalen automáticamente a calidad valorada | CONDITIONAL |
| Acceso de destinatarios | Valor de que destinatarios reales puedan obtener/usar el servicio | No confundir acceso del destinatario con accesibilidad transformacional; destinatarios no confirmados | CONDITIONAL |
| Robustez | Valoración de estabilidad ante perturbaciones | Posible solapamiento con continuidad, recuperación y resiliencia como Outcomes; requiere constructo diferenciado | CONDITIONAL |
| Sostenibilidad | Valoración intertemporal | Dominio, perspectiva y horizonte no especificados | DEFER / CONDITIONAL |

**Resolución de precedencia:** mantener la representación vectorial como orientación metodológica de P179 durante identificación. No asumir que las cinco dimensiones son confirmatorias ni exhaustivas; tampoco asumir que una sola dimensión basta. La selección del conjunto dimensional requiere fundamento contextual, observador/beneficiario y criterio registrados (P179-04), fichas §224 completas y decisión previa a resultados. Si el dominio solo sostiene una dimensión, esa reducción debe justificarse explícitamente frente a la recomendación vectorial y no presentarse como regla general.

El crosswalk actual no confirma ninguna dimensión material de Value para esta instancia. Eso no invalida P179: identifica que falta la información de dominio necesaria para instanciar su contrato.

## 4. Crosswalk de Outcome: no confundir evidencia superficial con operacionalización

| Outcome candidato de §264 | Hallazgo del crosswalk de §265 | Clasificación | Trabajo mínimo pendiente |
|---|---|---|---|
| O-MIG — migración | No existe campo de estado terminal | NOT_GROUNDED como medida actual | Definir evento terminal, unidad, criterio de éxito/fallo, fuente y snapshot |
| O-CONF — conformidad | Anclaje conceptual en F*/FP-01…08 | CONDITIONAL; mejor anclaje actual | Predicados, mapping, tolerancias, oráculo, snapshots, cobertura y adjudicación |
| O-SVC — continuidad | Superficies observables, sin indicador definido | NOT_GROUNDED como indicador actual | Definir continuidad, denominador, ventana, interrupciones admisibles y fuente |
| O-REC — recuperación | Referencias a rollback/estado persistente, sin medida de recuperación | NOT_GROUNDED como indicador actual | Definir evento adverso, estado de referencia, recuperación terminal, tiempo y criterio |
| O-BUR — carga operativa | Recursos/rendimiento disponibles, sin medición de esfuerzo/coste | NOT_GROUNDED como indicador actual | Definir actor, esfuerzo/coste, unidad, instrumento y ventana |

O-CONF puede mantenerse como candidato prioritario de Outcome para el trabajo de operacionalización, pero no debe etiquetarse como operacionalizado ni como Value. Los demás candidatos no se eliminan del historial; permanecen fuera del núcleo hasta que exista un contrato medible.

## 5. Separaciones semánticas obligatorias

1. **T_acc / ΔT_acc ≠ Outcome ≠ Value.** Accesibilidad, Reach y trayectoria pertenecen a la cadena transformacional/causal; no constituyen por sí mismas una valoración.
2. **Outcome ≠ Value.** Outcome describe un resultado o consecuencia operativa; Value expresa valoración contextual para beneficiarios identificados.
3. **CMP.owner ≠ beneficiario.** §264 enumera roles posibles (propietario, operador, mantenedor, usuarios si existen, responsable de riesgo si procede), pero §265 confirma que el roster no permite identificar beneficiarios/roles de valoración. No convertir candidatos conceptuales en actores reales.
4. **Recurso consumido ≠ coste económico.** Hace falta perspectiva, coste/precio o proxy validado y regla de imputación.
5. **Disponibilidad de A1/A2 ≠ valor de portabilidad.** Capacidad técnica no acredita utilidad ni valoración.
6. **F* ≠ Outcome ≠ Value.** F* es criterio funcional técnico; Outcome es estado/consecuencia operativa; Value es valoración contextual. Seguridad/compliance puede ser restricción no compensatoria, no necesariamente dimensión compensable de V.
7. **No observado ≠ cero; Value no definido ≠ Value no medido.** P183-05 exige que ausencia dimensional no implique valoración nula. Preservar OBSERVED_VALID, OBSERVED_INVALID, NOT_OBSERVED, NOT_APPLICABLE, CENSORED, DISPUTED y UNKNOWN según §224.

## 6. Núcleo confirmatorio mínimo: especificación por capas

### 6.1 Crosswalk de cumplimiento de §224 contra Opción A

La clasificación se refiere al estado documental/material descrito en §§16.102 y 16.138–16.139 y al crosswalk §265. "Parcial" significa que existe un anclaje o superficie, no que el requisito esté satisfecho. "OPEN/UNKNOWN" no significa cero ni inexistencia.

| Campo exigido por §224 | Outcome (O) en Opción A | Value (V) en Opción A | Dictamen |
|---|---|---|---|
| Identidad/versionado de ficha | Cinco candidatos nombrados; ninguno tiene ficha completa | Vector conceptual y dimensiones candidatas; ninguna ficha V_j completa | OPEN |
| Constructo | O-CONF tiene anclaje parcial en F*/FP-01…08; otros O son candidatos sin criterio terminal definido | Cinco dimensiones históricas candidatas; no seleccionadas ni contextualizadas | PARCIAL / OPEN |
| Evidencia | F*/FP-01…08 y superficies B-M disponibles como referencias; no equivalen a medición validada | No hay registros de valoración poblados; telemetría no es valoración | PARCIAL para O-CONF; OPEN para V |
| Adjudicación/oráculo | Predicados, mapping, tolerancias, oráculo y snapshots de O-CONF pendientes; otros Outcomes sin regla terminal | No hay regla de adjudicación por dimensión V_j | OPEN |
| Fuente de datos | Superficies y roster identificados, pero fuente probatoria por indicador no cerrada | Fuente/observador/beneficiario de valoración no confirmado | OPEN |
| Unidad | Unidad de análisis/observación específica por Outcome no cerrada en ficha | Unidad de valoración y población de referencia no identificadas | OPEN |
| Escala/representación | Estados, categorías y tolerancias del Outcome no fijados por ficha | Escala/unidad por dimensión no definida | OPEN |
| Cálculo | No hay fórmula/predicado operacional completo para ningún O | No hay cálculo ni regla de valoración aceptados | OPEN |
| Baseline | No hay baseline/snapshot contractual completo para cada O | No hay baseline por dimensión V_j | OPEN |
| Ventana temporal/ancla | Horizonte/ventana y reglas de terminalidad pendientes | Horizonte y referencia temporal de valoración pendientes | OPEN |
| Validez | Anclaje conceptual no demuestra validez del indicador; P182 aplicable | No hay instrumento ni evidencia de validez contextual | OPEN |
| Error de medición | Error, tolerancias y adjudicación no determinados | Error de medición de cada V_j no determinado | OPEN |
| Acuerdo interevaluador | No hay protocolo ni resultados de concordancia | No hay evaluadores/observadores ni protocolo de acuerdo | OPEN |
| Ausencia/censura | Estados y mecanismo por Outcome no poblados; aplicar P183 | No observado, no aplicable, censurado, disputado y desconocido deben preservarse por dimensión; mecanismos no definidos | OPEN |
| Cegamiento | Contrato de separación Generator/Evaluator/Analyzer propuesto; procedimiento material no demostrado | Observador/valorador, cegamiento y aislamiento no definidos | OPEN |
| Trade-offs | No aplica como agregación de Outcomes por defecto; relaciones O–O deben declararse si afectan interpretación | P179 exige conservar el vector y no ocultar discordancias; dimensiones y trade-offs materiales aún no identificados | OPEN |
| Provenance/trazabilidad | Roster/DAG/superficies trazados; falta provenance completa de ficha, evidencia y adjudicación | No hay registros V_j ni cadena de provenance de valoración | PARCIAL en referencias; OPEN en ficha |

**Resultado del crosswalk:** no hay ninguna ficha O ni V que cumpla §224 íntegramente. O-CONF es el único Outcome con anclaje conceptual explícito relativamente desarrollado; no alcanza por ello estado operacionalizado. En Value, la arquitectura vectorial está preservada, pero no existe una dimensión materialmente instanciada.

### 6.2 Crosswalk específico por Outcome

| Candidato | Constructo | Evidencia | Adjudicación | Estado §224 |
|---|---|---|---|---|
| O-MIG | Evento de migración terminal no definido | No existe campo terminal en roster | No definida | NOT_OPERATIONALIZED |
| O-CONF | Anclaje funcional F*/FP-01…08 | Superficies de evaluación referenciadas | Predicados, mapping, tolerancias, oráculo y snapshots pendientes | PARTIAL / NOT_OPERATIONALIZED |
| O-SVC | Continuidad sin indicador definido | Superficies de observación disponibles | Denominador, ventana y regla pendientes | NOT_OPERATIONALIZED |
| O-REC | Recuperación sin constructo terminal medido | Referencias a rollback/estado persistente | Evento, baseline, tiempo y criterio pendientes | NOT_OPERATIONALIZED |
| O-BUR | Carga operativa sin unidad de esfuerzo/coste | Recursos y rendimiento observables | Actor, unidad, instrumento y regla pendientes | NOT_OPERATIONALIZED |

### 6.3 Crosswalk específico de Value

| Campo de instanciación V_j | Evidencia actual | Estado |
|---|---|---|
| Dimensión candidata | Cinco dimensiones históricas | CANDIDATE ONLY |
| Beneficiario/observador | Ninguno confirmado en roster | OPEN |
| Perspectiva de valoración | No determinada | OPEN |
| Contexto de valoración | Microdominio descrito, pero sin criterio valorativo por actor | OPEN |
| Criterio/dirección de valor | No definidos | OPEN |
| Indicador/fuente | No hay instrumentos ni registros de valoración poblados | OPEN |
| Unidad/escala/cálculo | No definidos | OPEN |
| Baseline/ventana | No definidos | OPEN |
| Validez/error/acuerdo | Contratos P182 disponibles, aplicación material pendiente | OPEN |
| Ausencia/censura | P183 disponible, clasificación por dimensión pendiente | OPEN |
| Trade-offs/agregación | Vector preservado; no hay dimensiones ni reglas de agregación justificadas | OPEN |
| Adjudicación/provenance | No hay ficha ni cadena de evidencia V_j | OPEN |

### 6.4 Estados de observación: regla de cumplimiento

Se preservan los siete estados contractuales:

- `OBSERVED_VALID`
- `OBSERVED_INVALID`
- `NOT_OBSERVED`
- `NOT_APPLICABLE`
- `CENSORED`
- `DISPUTED`
- `UNKNOWN`

No se permite:
- Imputar cero a una dimensión no observada.
- Interpretar NOT_APPLICABLE como valor nulo.
- Tratar OBSERVED_INVALID como medición válida.
- Convertir DISPUTED en consenso.
- Convertir UNKNOWN en ausencia demostrada.

La ausencia de una ficha o de un registro de valoración se declara como bloqueo documental/material, no como observación de Value.

### 6.5 Dictamen de cumplimiento

| Objeto | Dictamen |
|---|---|
| Estructura contractual §224 | DOCUMENTED |
| Separación constructo/evidencia/adjudicación | REQUIRED; aplicación incompleta |
| Fichas Outcome | NONE COMPLETE |
| Fichas Value | NONE COMPLETE |
| Estados de observación | DEFINED CONTRACTUALLY; NOT MATERIALIZED |
| P182/P183 | CONTRACTS AVAILABLE; APPLICATION OPEN |
| Firewall Generator/Evaluator/Analyzer | PROPOSED; NOT VERIFIED |
| Provenance integral | PARTIAL / OPEN |
| Cumplimiento material global | NOT SATISFIED |

Este dictamen no modifica el estado de aceptación de §224 ni declara incumplimiento empírico: constata que la instancia todavía no aporta los artefactos exigidos para demostrar cumplimiento.
 
### 6.6 Núcleo metodológico que sí puede fijarse documentalmente

- **A:** medida independiente de accesibilidad/ΔT_acc*, con temporalidad, versión, unidad y evidencia; no depende de O ni V.
- **O:** Outcomes operativos definidos mediante fichas §224; seleccionar un Outcome primario solo después de justificarlo y operacionalizarlo. No hay actualmente ninguno completo.
- **V:** conservar representación vectorial durante identificación (P179-02/06/07). El conjunto de dimensiones no está aprobado: las cinco históricas son candidatas, no requisitos. No seleccionar V1 ni pesos por defecto.
- **Agregación:** no producir índice escalar salvo que exista ponderación y regla de compensación justificadas y análisis de sensibilidad (P179-08).
- **Fichas:** una ficha versionada por indicador O y por dimensión V, con constructo, evidencia y adjudicación; fuentes, unidades/escalas, cálculo, baseline, ventana/ancla, validez, error, acuerdo, ausencia/censura, cegamiento, trade-offs y provenance (§224).
- **Estimandos:** dictámenes independientes para ITT sobre O, ITT por cada V_j, efecto mediado por A, LATE sobre V, efecto residual e índice agregado si se utiliza. No transferir identificación entre ellos (P179-07; P183-12).
- **Medición/ausencia:** P182 para validez, reproducibilidad, acuerdo, error, invariancia, sensibilidad y firewall; P183 para taxonomía/mecanismo de ausencia, selección, censura, sensibilidad, cotas y dictamen por estimando.
- **Evaluación:** Generator, Analyzer y Evaluator separados; truth/potenciales no accesibles al Analyzer.

### 6.7 Núcleo material actualmente disponible

| Componente | Estado actual | ¿Confirmatorio ejecutable? |
|---|---|---|
| A / ΔT_acc* | Arquitectura y crosswalk semánticos parciales; inputs materiales, fuentes y medición pendientes | NO |
| O primario | O-CONF mejor anclado, pero sin predicados/mapping/tolerancias/oráculo/snapshots completos; ningún O tiene ficha §224 completa | NO |
| Beneficiarios/perspectivas | Roles candidatos en §264; ninguno confirmado en roster §265 | NO |
| Vector V_j | Recomendación metodológica vigente, pero sin dimensiones materialmente confirmadas ni fichas pobladas | NO |
| Regla de valoración | No operacionalizada; sin observador/beneficiario, criterio ni contexto confirmado | NO |
| Función escalar/ponderaciones | No aceptadas; fórmula ilustrativa anterior no es decisión | NO |
| Missingness/selección | Contratos P183 disponibles; mecanismo y parámetros concretos pendientes | NO |
| Validez/error | Contratos P182 disponibles; instrumentos, tolerancias y validación pendientes | NO |

**Conclusión:** la arquitectura metodológica debe preservar Value vectorial durante identificación. No podemos todavía instanciar un vector confirmatorio en Opción A porque faltan beneficiarios, criterios y dimensiones justificadas. Tampoco podemos sustituirlo por un V1 arbitrario. Outcome tampoco está completamente operacionalizado.

## 7. Reglas de clasificación KEEP / REDUNDANT / CONDITIONAL / NOT_GROUNDED

| Objeto | Clasificación | Justificación |
|---|---|---|
| Separación A/O/V y no circularidad | KEEP | P179-01/03; P182-02/04 |
| Value vectorial durante identificación | KEEP | P179-02; P179-06/07; no ocultar trade-offs |
| Cinco dimensiones históricas | CONDITIONAL | Candidatas provisionales; no son lista confirmada ni cinco obligaciones |
| Selección contextual de dimensiones | CONDITIONAL | P179-04 y §224 requieren observador/beneficiario/contexto/criterio |
| Índice escalar y ponderaciones | NOT_GROUNDED hasta justificación | P179-08 permite agregación solo con regla y ponderaciones justificadas |
| P182 como contrato transversal de medición | KEEP | Validez, especificación, reproducibilidad, acuerdo, error, invariancia, sensibilidad y firewall |
| P183 como contrato transversal de ausencia/identificación | KEEP | Ausencia, ITT, selección, mediación, censura, cotas y dictamen por estimando |
| O-CONF | CONDITIONAL | Mejor anclaje actual, pero sin ficha §224 completa |
| O-MIG/O-SVC/O-REC/O-BUR como medidas actuales | NOT_GROUNDED | El crosswalk no acredita indicadores completos |
| Recursos = coste | NOT_GROUNDED | No es inferencia válida sin perspectiva y regla de valoración |
| Continuidad + recuperación + robustez como un único indicador | REDUNDANT si se fusionan sin teoría | No fusionar constructos distintos por compartir superficies observables |
| T_acc/Reach/trayectoria como Value | NOT_GROUNDED / circular | Son constructos de la cadena causal, no valoración |
| CMP.owner como beneficiario | NOT_GROUNDED | No existe equivalencia semántica acreditada |
| A1/A2 disponibles como valor de portabilidad | NOT_GROUNDED | Capacidad técnica no acredita utilidad/valor |
| Seguridad/compliance como dimensión compensable | NOT_GROUNDED | Puede operar como restricción no compensatoria; requiere decisión contextual |

## 8. Auditoría de roles y beneficiarios en el dominio sintético

### 8.1 Fuentes históricas y precedencia

Se contrastan los contratos y decisiones ya existentes, sin crear roles ni entidades:

- DEC-C10-068 y `C10_S_SYNTHETIC_LOGICAL_SERVICE_FUNCTIONAL_CONTRACT_DRAFT_001.md`: servicio lógico sintético de procesamiento de solicitudes, con función abstracta de aceptar solicitudes cuando está habilitado y exponer un perfil operativo declarado. No selecciona producto, proveedor, plataforma ni servicio real; tampoco identifica consumidor, usuario, cliente o beneficiario concreto.
- DEC-C10-069 y `C10_S_SERVICE_CMP_INSTANCE_IDENTITY_VERSIONING_PROPOSAL_DRAFT_001.md`: fija la identidad contractual, de instancia y CMP. `CMP-SERVICE-LOGIC-001` es un componente lógico de clase SERVICE_LOGIC; `CMP-SERVICE-LOGIC` es etiqueta provisional de owner lógico de regla/rol, no identidad de propietario del servicio ni beneficiario.
- DEC-C10-089: acepta `LOGICAL_SERVICE_UNIT` como NODE raíz conceptual, pero deja sin adjudicar su relación de identidad con `CMP-SERVICE-LOGIC-001`. No autoriza inferir que sean el mismo objeto o dos entidades distintas.
- `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`: t6 registra `actor` como campo de selección/inicio; t9 exige beneficiario, regla/version, horizonte y observación de Value. DGP-13 exige beneficiario, criterio, escala y horizonte fijados ex ante. El contrato sigue DRAFT / NO APROBADO / NO IMPLEMENTADO; los campos indican requisitos, no entidades materializadas.
- §264 / plan §16.138: propietario del servicio, operador, mantenedor, usuarios (si existen) y responsable de riesgo (si procede) se proponen expresamente como roles candidatos, sin seleccionar.
- §265 / plan §16.139: el roster no confirma beneficiarios/roles Value; no hay instrumentos ni registros de valoración poblados.

### 8.2 Crosswalk de rol candidato a evidencia del dominio

| Rol candidato de §264 | Evidencia concreta existente | Qué no demuestra | Dictamen |
|---|---|---|---|
| Propietario del servicio | Owner lógico provisional `CMP-SERVICE-LOGIC` para RUL; CMP concreto `CMP-SERVICE-LOGIC-001` | Propiedad organizativa, responsabilidad sobre el servicio, recepción de beneficios o autoridad para valorar | NOT_GROUNDED |
| Operador | El DGP contempla un actor que inicia/ejecuta el intento; DEC-C10-068 define una función lógica de servicio | Identidad, función organizativa, responsabilidad operativa o beneficio del actor | NOT_GROUNDED |
| Mantenedor | Ningún componente, parámetro, regla o decisión asigna mantenimiento | Existencia de equipo/persona/función de mantenimiento | NOT_GROUNDED |
| Usuario/destinatario/solicitante | La definición funcional dice que el servicio acepta solicitudes; la definición genérica de servicio lógico alude a consumidor o sistema | No hay entidad solicitante, población de usuarios, relación de consumo, registro de solicitudes ni perspectiva de valoración | NOT_GROUNDED |
| Responsable de riesgo | Seguridad/compliance aparecen como posibles restricciones y vías a considerar en P2 | No hay rol de riesgo identificado, mandato, criterio de tolerancia ni decisión de valoración | NOT_GROUNDED |
| Evaluador independiente | Rol metodológico del contrato Generator/Analyzer/Evaluator | No es usuario, beneficiario ni stakeholder del servicio; su función es adjudicar evidencia | EXCLUIDO COMO BENEFICIARIO POR FUNCIÓN |
| LOGICAL_SERVICE_UNIT | NODE raíz aceptado por DEC-C10-089 | No identifica persona/organización beneficiaria; su relación con CMP sigue sin adjudicar | NO ES ROL DE BENEFICIARIO |

**Resultado:** ninguno de los cinco roles candidatos de §264 puede derivarse como actor materialmente existente a partir del contrato funcional, las decisiones aceptadas o el roster descrito en §265. Los campos `actor` y `beneficiario` del DGP son requisitos de registro, no evidencia de que exista una identidad asociada.

### 8.3 Qué sí puede sostener el microdominio

1. **Objeto funcional sintético:** una instancia lógica de servicio software de procesamiento de solicitudes, con comportamiento declarado por ENABLED/PROFILE y RUL. Es un objeto del mundo sintético estipulado, no un servicio real ni una población de usuarios.
2. **Criterio técnico:** F*/FP-01…08 permite evaluar propiedades funcionales/de conformidad del paquete y de la ruta de migración, sujeto a predicados, mapping, tolerancias, oráculo y snapshots pendientes. Esto puede sostener un Outcome técnico cuando se operacionalice; no identifica por sí solo a quién beneficia ni cómo valora el resultado.
3. **Actor ejecutor:** el DGP necesita registrar quién inicia/ejecuta B/W_attempt y eventos posteriores. El rol ejecutor puede especificarse para reproducir el mecanismo técnico, pero no debe reutilizarse automáticamente como operador del servicio, consumidor o beneficiario.
4. **Consumidor abstracto:** la referencia semántica a un consumidor/sistema en la definición general de servicio lógico permite describir la finalidad funcional, pero no crea una entidad, población, preferencia ni medida de valor en esta instancia.
5. **Restricciones:** seguridad/compliance pueden permanecer como predicados o restricciones no compensatorias si el contrato lo justifica; no se convierten automáticamente en una dimensión de Value ni requieren inventar un responsable de riesgo.

### 8.4 Dictamen sobre posibilidad de instanciar Value

El microdominio actual puede sostener el diseño de Outcomes técnicos relacionados con la conformidad funcional y la migración, una vez completadas sus fichas §224. No sostiene actualmente Value contextual porque faltan, conjuntamente:

- identidad/rol real o sintético explícitamente estipulado del beneficiario/observador;
- relación de ese actor con el servicio y la unidad experimental;
- perspectiva desde la que valora;
- criterio y dirección de valoración;
- evidencia/indicador independiente del Outcome y de A/ΔT_acc;
- escala, baseline y horizonte;
- regla de adjudicación y provenance.

No se concluye que Value sea imposible en este microdominio. Se concluye que **no está definido por el dominio aceptado hasta ahora**. Añadir un solicitante, operador o beneficiario sintético sería una extensión sustantiva del DGP, que requeriría una propuesta y decisión explícitas, no una inferencia desde el nombre del servicio.

### 8.5 Decisión de diseño que no debe anticiparse

No seleccionar ahora entre:
- mantener Opción A solo como banco de pruebas de accesibilidad, conformidad y Outcomes técnicos, declarando Value no instanciado; o
- ampliar explícitamente el DGP para estipular un actor consumidor/beneficiario sintético, su relación con la unidad, su perspectiva y regla de valoración.

Ambas son rutas de diseño posibles, pero no equivalentes. La segunda modifica el mundo sintético y exige analizar nuevas vías causales, medición, interferencia y comparabilidad. No se adopta por conveniencia de completar §224.

### 8.6 Comparación de alternativas A/B y recomendación de arquitectura

La comparación no trata de completar §224 por conveniencia, sino de decidir qué afirmaciones científicas puede sostener cada variante del DGP.

| Criterio | A — Opción A sin extensión de Value | B — extensión explícita del DGP |
|---|---|---|
| Dominio | Conserva exactamente el servicio lógico aceptado | Añade un rol consumidor/beneficiario sintético y una relación explícita con el servicio |
| Outcome | Puede estudiar Outcomes técnicos una vez operacionalizados; O-CONF es el candidato mejor anclado | Conserva esos Outcomes y añade una consecuencia experimentada/valorada por el rol sintético |
| Value | No instanciado; no permite probar ΔT_acc→Value | Puede instanciar Value bajo preferencias/criterios estipulados ex ante |
| Pregunta causal | Recuperación de A/ΔT_acc, Reach, trayectorias y efectos sobre O | Además, si el cambio transformacional produce consecuencias valoradas para el beneficiario sintético |
| Validez externa | No permite inferir valor para usuarios reales | Tampoco; prueba únicamente recuperación causal dentro del mundo sintético estipulado |
| Riesgo principal | Que el programa C10-S no llegue a probar la atribución a Value | Circularidad, utilidad diseñada para favorecer la hipótesis, confusión entre Outcome y Value, nuevas vías directas y supuestos de preferencias arbitrarios |
| Coste de diseño | Menor; preserva el DGP aceptado | Mayor; exige ampliar unidad/relación, demanda, criterio, medición, DAG, ausencia, interferencia y contratos |
| Uso legítimo | Banco de pruebas transformacional y de Outcome técnico | Banco de pruebas causal-transformacional con Value sintético, además de los módulos de A |

**Conclusión comparativa:** A es adecuada para validar partes transformacionales y técnicas del Analyzer, pero no satisface el objetivo confirmatorio de atribución a Value. B es necesaria para probar esa capacidad dentro de un DGP sintético; no autoriza ninguna afirmación sobre valor real ni sustituye validación externa.

**Recomendación de arquitectura — PROPUESTA, NO ACEPTADA:** conservar A como variante base inalterada y crear B como variante/extensión versionada separada. No reescribir el contrato funcional aceptado DEC-C10-068 ni introducir silenciosamente actores en el roster actual. Esta separación permite comparar el mismo mecanismo técnico con y sin capa de beneficiario y evita que el resultado de la extensión se presente como propiedad del dominio base.

#### Requisitos mínimos para B antes de aprobarla

1. **Rol beneficiario sintético:** estipular una entidad/rol consumidor que origina una demanda de servicio y recibe sus consecuencias. Su relación con la unidad experimental y el servicio debe ser explícita. No reutilizar el actor ejecutor ni al evaluador independiente.
2. **Demanda preasignación:** definir una carga/solicitudes estandarizadas, su origen, elegibilidad, volumen, temporalidad y asignación a la unidad. Mantenerla exógena a Z, salvo que la demanda sea deliberadamente parte de otro estimando.
3. **Perspectiva y criterio:** declarar qué consecuencias cuentan como beneficios/cargas para ese rol y en qué dirección. La preferencia es una estipulación del DGP, no una verdad sobre usuarios reales.
4. **Separación O/V:** O registra estados/consecuencias operativas del servicio; V_j registra cómo se valoran esas consecuencias desde la perspectiva del beneficiario. Un mismo registro bruto no puede actuar como Outcome y Value sin una transformación/medición conceptualmente distinta, independiente y documentada.
5. **Vector, no escalar por defecto:** preservar dimensiones V_j y trade-offs según P179. No definir ponderaciones ni una función agregada hasta justificar regla, unidades y sensibilidad.
6. **Mecanismo causal:** especificar si la ruta focal es ΔT_acc→Reach→consideración/selección→ejecución→O→V_j, y declarar explícitamente las rutas directas B→V_j, provisión/instalación→V_j, coste/latencia/calidad/riesgo→V_j y cualquier vía mediada por conocimiento/selección. No imponer exclusión por definición.
7. **Temporalidad:** mantener baseline/demanda y perspectiva antes de Z; medir A/ΔT_acc antes de selección/ejecución; medir O y V en sus ventanas preespecificadas; no condicionar el análisis a solicitudes atendidas o ejecuciones completadas si son postratamiento.
8. **Medición §224/P182/P183:** ficha independiente por O y V_j; validez, error, acuerdo, cegamiento, invariancia, missingness/censura y dictamen por estimando. Mantener verdad DGP oculta al Analyzer.
9. **Unidad/interferencia:** establecer si el beneficiario es exclusivo de una UE o compartido entre instancias; si comparte demanda, recursos o resultados, cambiar UA/clúster y estimandos o estipular y probar escenarios de spillover.
10. **Contraste adversarial:** incluir al menos DGPs donde ΔT_acc aumenta sin aumentar Value, Value cambia por una vía no focal, Outcome permanece constante mientras Value cambia, y efectos/beneficios y cargas se mueven en direcciones opuestas. El Analyzer debe abstenerse cuando exclusión o identificación no estén demostradas.

#### Límite decisivo

B solo prueba que el Analyzer puede recuperar la relación causal codificada en un DGP transparente para el Evaluator y oculta para el Analyzer. No prueba que la perspectiva, preferencias ni dimensiones elegidas sean válidas para usuarios reales. Esa validez exigiría una investigación empírica externa y un dominio con actores/evidencia reales, fuera del alcance de esta extensión sintética.

**Estado:** A/B COMPARISON DOCUMENTED / B RECOMMENDED AS SEPARATE DGP VARIANT / USER ACCEPTANCE OPEN. No se crea actor, ID, variable, regla de Value, evento, fixture ni DAG aprobado.

## 9. Bloqueos exactos para pasar de arquitectura a operacionalización

1. **B1 — Perspectiva/beneficiario:** resolver si se mantiene Value no instanciado en Opción A o si se propone y acepta una extensión explícita del DGP que estipule consumidor/beneficiario sintético, su relación con la unidad y su perspectiva. No inferirlo desde CMP.owner, el actor ejecutor o el nombre del servicio.
2. **B2 — Criterio V:** documentar qué resultado se valora, por quién, en qué dirección y bajo qué regla; justificar si V es vectorial o si se requiere agregación.
3. **B3 — Outcome primario:** decidir si O-CONF es el Outcome primario y completar predicados, mapping, tolerancias, oráculo, snapshots y cobertura.
4. **B4 — Independencia A/O/V:** demostrar fuentes, tiempos, evaluadores y reglas que impiden circularidad y leakage.
5. **B5 — Medición y error:** instrumentos, unidades, validez, fiabilidad, acuerdo, error y tolerancias ex ante conforme P182.
6. **B6 — Ausencia/censura:** taxonomía por variable y tiempo, mecanismo plausible, selección y sensibilidad/cotas conforme P183.
7. **B7 — Horizonte y versiones:** fijar ventana/horizonte, versiones del servicio y tratamiento de trade-offs sin agrupar versiones causalmente distintas.
8. **B8 — Estimando y adjudicación:** mantener separado ITT_Z, efecto de política/paquete, efecto focal y mediación; dictamen por estimando × Outcome/Value × población × horizonte × versión conforme MAP-07.
9. **B9 — Evidencia y reproducibilidad:** snapshots, fuentes, cobertura, oráculo, provenance y artefactos evaluables sin dar por implementada la separación Generator/Analyzer/Evaluator.

No se añaden bloqueos genéricos ni se convierten en requisitos de dimensión. Cada bloqueo debe cerrarse con evidencia concreta o declararse no identificable/no disponible.

## 10. Consecuencias para los paquetes C/D/E y gates

- **C / C-Value:** puede avanzar en reconciliación documental y definición de criterios; permanece OPEN materialmente mientras B1–B6 no se resuelvan.
- **D:** debe consumir la especificación mínima y los estados OPEN/UNKNOWN sin inventar schema, indicador o regla de valoración.
- **E:** no puede aceptar integración confirmatoria mientras A/O/V, sus contratos de datos y adjudicación no estén materialmente definidos.
- **MED-02 y MED-03:** no se declaran cerrados por esta matriz.
- **Design Freeze:** no procede.
- **Implementación/ejecución:** no autorizadas.

## 11. Decisiones propuestas para revisión

| Propuesta | Contenido | Estado |
|---|---|---|
| PROP-VALUE-01 | Mantener Value vectorial durante identificación, conforme P179-02/06/07 | PROPUESTA DE CONFIRMACIÓN DE PRECEDENCIA |
| PROP-VALUE-02 | Mantener las cinco dimensiones como candidatas históricas, no como obligaciones confirmatorias ni lista exhaustiva | PROPUESTA |
| PROP-VALUE-03 | No definir índice escalar ni ponderaciones sin regla de valoración justificada y sensibilidad | PROPUESTA |
| PROP-VALUE-04 | Exigir observador/beneficiario, contexto y criterio explícitos antes de aceptar cualquier V_j confirmatorio | PROPUESTA |
| PROP-VALUE-05 | Seleccionar el conjunto dimensional solo tras fichas §224 y evidencia del dominio; no reducir a V1 por conveniencia analítica | PROPUESTA |
| PROP-VALUE-06 | Si no se operacionaliza Value, limitar las conclusiones a Outcomes/estimandos realmente evaluables y declarar no disponible la atribución a Value | PROPUESTA |

Estas propuestas no modifican DEC-C10 existentes ni constituyen aceptación por sí mismas. P179/P182/P183 y §224 conservan precedencia; la matriz solo especializa su lectura para el crosswalk de Opción A.

## 12. Estado y siguiente gate

**Dictamen de esta matriz:** DOCUMENTARY RECONCILIATION UPDATED AGAINST RECOVERED CONTRACT REGISTER / MATERIAL OUTCOME-VALUE OPEN.

Siguiente gate: revisar la recomendación de conservar A como variante base y desarrollar B como variante DGP separada. Solo tras aceptación expresa se elaborará su contrato de roles, demanda, criterio y DAG; después se resolverán B2–B3 (criterio V y Outcome primario) y sus fichas §224. No crear identidades ni reglas de valoración antes de esa aceptación.

No se ha modificado `main`; no se ha cerrado MED-02/MED-03; no hay Design Freeze, implementación ni ejecución científica.

`scientific_execution=false`  
`execution_authorized=false`


## 13. Aceptación de arquitectura A/B — DEC-C10-095 (2026-11-11)

El usuario acepta A como variante base inalterada y B como extensión sintética independiente/versionada. Esta aceptación resuelve la elección arquitectónica, no la especificación material de B.

- **A:** conserva contrato, roster y dominio aceptados. No se añade beneficiario ni Value contextual por inferencia. Puede estudiar accesibilidad/ΔT_acc, Reach, trayectorias y Outcomes técnicos una vez operacionalizados; no permite atribución confirmatoria a Value mientras este no esté instanciado.
- **B:** queda autorizada para diseño documental separado. Su rol beneficiario, relación servicio-unidad, demanda pre-Z, perspectiva/criterio, vector de dimensiones, DAG, medición, horizonte, interferencia y parámetros siguen OPEN y requieren propuestas y aceptación explícitas.
- P179 mantiene Value vectorial y trade-offs; no hay escalar ni ponderaciones por defecto. P182/P183 siguen transversales.
- B solo permitirá evaluar recuperación de la relación causal estipulada en su DGP, sin inferencia sobre usuarios reales ni validez externa.
- C/D/E deben mantener separados el alcance de A y B y su provenance. MED-02/03 OPEN.

No se modifica DEC-C10-068, no se altera el roster de A y no se crean roles, indicadores, reglas, fixtures o parámetros. No Design Freeze, implementación ni ejecución. Véase DEC-C10-095.


## 14. Contrato mínimo B-BEN/B-VAL — C10S-B-VALUE-MIN-001 (2026-11-11)

La variante B dispone ahora de un contrato de admisibilidad documental, no de una instancia de beneficiario. Requisitos OPEN: identidad/tipo sintético versionado; relación con servicio y unidad experimental; elegibilidad y demanda basal pre-Z; consecuencia valorada; perspectiva/autoridad; cardinalidad; población/horizonte; provenance. La unidad experimental, unidad lógica de servicio, beneficiario, actor ejecutor y evaluador son roles distintos hasta que una relación explícita justifique coincidencia. No inferir beneficiario de CMP.owner, CMP-SERVICE-LOGIC-001, LOGICAL_SERVICE_UNIT ni actor. Demanda no equivale a uso/selección/ejecución. V_j debe medir consecuencia para beneficiario, no ser recodificación de ΔT_acc, Reach o Outcome técnico. Regla de valoración estable entre brazos; vector y trade-offs P179 preservados; §224 y P182/P183 aplicables. No se elige tipo de entidad, dimensión, escala, regla, demanda ni parámetro. Véase C10S-B-VALUE-MIN-001. Estado: DRAFT; no aceptación de instancia B.


## 15. B1 — Entidad solicitante-beneficiaria (tipo candidato aceptado)

B1 queda aceptado como tipo candidato para desarrollo, no como instancia B cerrada. La entidad sintética presenta necesidad/objetivo pre-Z, mantiene relación explícita con el servicio, puede originar solicitud y experimentar una consecuencia valorable. Necesidad/demanda ≠ solicitud ≠ procesamiento técnico ≠ consecuencia para beneficiario. Outcome técnico/O-CONF no equivale a Value; no solicitud/no ejecución no demuestra ausencia de demanda ni Value cero. Solicitante y beneficiario coinciden solo por estipulación explícita B1. OPEN: instancia/cardinalidad, demanda, consecuencia operacional, perspectiva/autoridad, dimensiones, medición, DAG y estimandos. Véase C10S-B1-REQUESTER-CANDIDATE-001.


## 16. Demanda basal B1 vs demanda operativa del servicio (2026-11-11)

La reconciliación de B1 distingue Need_preZ (necesidad/objetivo basal del beneficiario), E_req_preZ (elegibilidad de la petición, OPEN), Request_event (petición efectivamente formulada/registrada, ventana temporal OPEN) y D_resource (demanda operativa de recursos/capacidad). Esta última ya estaba contemplada en el contrato DGP y no representa la necesidad del beneficiario. Need_preZ no es E_i ni pertenencia a P*_tau2/P*_F; la relación unidad experimental↔solicitante y cardinalidad permanecen OPEN. Request_event no se puede usar para definir población postratamiento ni ITT; no solicitud no implica no necesidad. Truth 1/0/? se distingue de evidencia observada. No se asigna Request_event a t5/t6/t7 sin reconciliar reloj/DAG. No se seleccionan instrumentos, escalas, parámetros ni dimensiones V_j. Véanse B1 spec §10, POP-CMP §10, DGP temporal §14.


## 17. Ciclo de solicitud y separación Outcome/Value (2026-11-11)

El ciclo B1 propuesto separa oportunidad, intento, recepción, admisión/rechazo, procesamiento, respuesta y consecuencia del beneficiario. Ningún evento de servicio equivale automáticamente a Outcome técnico ni a Value. La solicitud no es t5 conocimiento/consideración, admisión no es t6 selección/inicio, y procesamiento del servicio no es t7 ejecución transformacional. El enlace request↔trajectory permanece OPEN. La carga estandarizada ex ante mediante harness idéntico es recomendación no aceptada; constituye probe de carga, no demanda natural. El envío endógeno es candidato adversarial/secundario y no puede usarse para filtrar ITT. No se definen todavía consecuencia, perspectiva, dimensiones V_j, regla ni horizonte.


## 18. Efecto de la decisión de modalidad sobre C-Value

## Decisión DEC-C10S-B1-REQUEST-MODE-001 — modalidad de oportunidades estandarizadas y envío endógeno (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta la arquitectura de dos modalidades para C10-S:
1. **Modalidad primaria candidata:** oportunidades/peticiones estandarizadas, definidas ex ante antes de Z y presentadas mediante harness externo idéntico entre brazos después del snapshot de accesibilidad t3/t4. El harness registra Request_attempt aunque el servicio no reciba la petición. Esta modalidad permite comparar respuesta/capacidad bajo una carga de prueba común.
2. **Modalidad secundaria/adversarial:** envío endógeno de solicitudes, cuya ocurrencia puede depender de conocimiento, expectativas, accesibilidad percibida y otros estados post-Z. Se conserva para estudiar selección y vías causales, no para definir la población primaria ni filtrar el ITT.

**Límites de la aceptación.** La carga estandarizada es un probe experimental de servicio; no representa por sí sola demanda natural, preferencia revelada, beneficiario confirmado ni Value. Se mantienen separados intento, recepción, admisión/rechazo, procesamiento, respuesta, consecuencia del beneficiario, Outcome técnico y Value. Los eventos post-Z no se usan como criterio de inclusión o exclusión del ITT. Se conserva el reloj t−1/t0…t9 y no se equiparan eventos de petición con t5/t6/t7 ni con H.

**Pendiente de especificación:** calendario y ventana de presentación; unidad y cardinalidad de oportunidades; identidad y vínculo request_id↔trajectory_id; payload y reglas de admisión; repetición, timeout y errores; tratamiento de solicitudes no recibidas/pendientes; outcome técnico de respuesta; medida independiente de consecuencia B1 y su horizonte; población y soporte; relación exacta con los estimandos ITT/mediación. La modalidad secundaria no recibe estimando confirmatorio por esta decisión.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen scientific_execution=false y execution_authorized=false. No altera DEC-C10-066/067, D2 primario candidato/D1 secundario ni la rama base de PR #116.


## B1 — efecto sobre la interpretación mínima de Value (2026-11-11)

**Decisión:** `DEC-C10S-B1-UNIT-001` — **ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN**.

Se acepta provisionalmente una entidad B1 por unidad experimental (UE), vinculada de forma explícita, unívoca, versionada y trazable a una instancia lógica de servicio aislada. La UE sigue siendo la instancia sintética completa a la que se asigna Z y para la que se generan estados transformacionales, trayectorias, Outcome y Value. La entidad B1 es el referente sintético de necesidad/objetivo pre-Z y de la consecuencia potencialmente valorable; no se confunde con la UE, el servicio ni el actor ejecutor.

La instancia de servicio deberá ser aislada respecto de otras UE en recursos, agentes, información, infraestructura, estado y canales de transmisión. La condición de aislamiento es una hipótesis de diseño que deberá justificarse y auditarse, no una propiedad presumida por nombrar instancias distintas. Si no puede sostenerse, se deberá definir clúster/unidad de asignación, mapa de exposición e inferencia compatible con interferencia antes de confirmar el diseño.

El número de oportunidades estandarizadas por UE queda **OPEN**. Cuando se fije, deberá ser constante entre brazos, establecido ex ante y administrado por un harness externo común; no podrá depender de recepción, admisión, procesamiento, selección, ejecución ni variables post-Z. La ausencia de envío/recepción/admisión seguirá siendo un estado observable y no se codificará automáticamente como ausencia de necesidad o Value=0.

La decisión no fija aún la identidad concreta/versionado final de B1 o del servicio, el número de oportunidades, la ventana/calendario, el payload, las reglas del protocolo, la cardinalidad request↔trajectory, los outcomes técnicos, la consecuencia B1, la perspectiva/autoridad de valoración ni los estimandos. No altera la separación entre el ciclo de petición y el reloj t−1/t0…t9; tampoco convierte solicitud, respuesta o procesamiento en selección, ejecución, Outcome o Value.

**Alcance:** decisión arquitectónica para continuar la especificación; no selecciona beneficiarios empíricos ni valida preferencias reales. No modifica DEC-C10-066/067, D2 primario candidato/D1 secundario, ni la separación entre main y PR #116.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen `scientific_execution=false` y `execution_authorized=false`.


## DEC-C10S-B1-OPPORTUNITY-CARDINALITY-001 — una oportunidad estandarizada por UE (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta **N_opportunities = 1 por unidad experimental (UE)** como configuración primaria candidata del probe estandarizado de servicio en el núcleo confirmatorio mínimo de C10-S. La oportunidad se define ex ante antes de Z y se presenta después del snapshot de accesibilidad t3/t4 mediante el mismo harness externo y bajo las mismas reglas en ambos brazos. El harness registra Request_attempt aunque no exista recepción por el servicio.

La identidad y el contenido de la oportunidad deberán ser comunes, trazables y versionados entre brazos. No recepción, rechazo, error o estado pendiente permanecen como estados observables; no se recodifican automáticamente como ausencia de necesidad, fallo transformacional, Outcome negativo ni Value=0. La población ITT no se condiciona a intento, recepción, admisión, procesamiento o respuesta post-Z.

Las oportunidades repetidas o cargas de mayor intensidad quedan reservadas a escenarios secundarios/adversariales; si se estudian, sus observaciones se anidan en la UE y no incrementan el número de unidades experimentales independientes. Esta configuración de una oportunidad no demuestra capacidad bajo carga sostenida ni demanda natural, preferencia revelada o Value del beneficiario.

Se mantienen abiertos: ventana/calendario exacto; definición final del payload y protocolo; identidad/versionado de B1 y servicio; cardinalidad request_id↔trajectory_id; tratamiento técnico de timeout, errores y pendientes; outcome técnico de respuesta; consecuencia independiente de B1 y horizonte; perspectiva/autoridad de valoración; población/soporte e integración exacta con ITT y mediación. No se equiparan eventos de petición con t5/t6/t7, ejecución transformacional, Outcome o Value, ni se amplía el reloj t−1/t0…t9.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen scientific_execution=false y execution_authorized=false. No altera DEC-C10-066/067, D2 primario candidato/D1 secundario, ni la separación main/PR #116.

## DEC-C10S-B1-REQUEST-TRAJECTORY-LINK-001 — contrato semántico de enlace (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta como arquitectura candidata que la relación entre `request_id` y `trajectory_id` sea explícita, tipada y versionada, sin imponer una cardinalidad funcional 1:1. Se distinguen tres tipos no intercambiables:

1. `TEMPORAL_ASSOCIATION`: coexistencia temporal u orden compatible entre petición y trayectoria; no demuestra trazabilidad ni contribución causal.
2. `TRACEABILITY_LINK`: referencia técnica/documental verificable entre registros; no demuestra que la petición haya causado o modificado la trayectoria.
3. `CAUSAL_CONTRIBUTION`: relación causal definida por el DGP generador; debe distinguirse la verdad conocida por el generador de la evidencia observable y disponible para el analizador.

El modelo debe poder representar petición sin trayectoria atribuible, trayectoria sin petición atribuible, una petición que contribuya a varias trayectorias y, en escenarios con múltiples peticiones, varias peticiones que contribuyan a una trayectoria. La configuración primaria mantiene una oportunidad estandarizada por UE; por tanto, no genera múltiples request_id estandarizados dentro de esa UE, pero no impone que solo pueda existir una trayectoria ni que toda trayectoria tenga origen en esa petición. Las relaciones de escenarios secundarios con peticiones repetidas quedan anidadas en UE y no crean unidades experimentales independientes.

La existencia de cualquier enlace temporal o de trazabilidad no puede promoverse automáticamente a contribución causal. Las contribuciones causales se establecen por la verdad del DGP y se contrastan mediante los mecanismos/contrafactuales pertinentes; no se adjudican por proximidad temporal, coincidencia de IDs, respuesta del servicio o éxito técnico. Los registros observados no deben revelar al analizador la etiqueta de verdad del DGP salvo que ese conocimiento forme parte explícita del diseño de medición.

El enlace no define elegibilidad, inclusión poblacional, ITT, Outcome ni Value, y no puede usarse para excluir UE por eventos post-Z. No equipara petición con t5 Consider, t6 Sel/Start, t7 Exec, Outcome t8 o Value t9; tampoco amplía el reloj t−1/t0…t9 ni la profundidad H. Los eventos de petición y sus enlaces se mantienen en subledger con timestamps, identidad/versionado y procedencia.

**OPEN:** reglas de generación de contribuciones, mecanismo de adjudicación, unidad temporal de atribución, tratamiento de contribuciones concurrentes y colaterales, evidencia observable para el analizador, cardinalidad de enlaces por tipo en cada DGP, y relación exacta con los estimandos ITT/mediación. No se congela schema físico ni protocolo técnico.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen scientific_execution=false y execution_authorized=false. D2 continúa como escenario primario candidato y D1 secundario; DEC-C10-066/067 no se reabren; main no se modifica.

## DEC-C10S-B1-CAUSAL-ADJUDICATION-001 — contrato de contribución causal petición–trayectoria (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta como contrato causal candidato que una relación \`CAUSAL_CONTRIBUTION\` entre una petición y una trayectoria requiere un contraste contrafactual definido por el DGP: la presencia/intervención en una etapa concreta del ciclo de petición modifica una propiedad preespecificada de la trayectoria respecto del escenario contrafactual correspondiente, manteniendo explícitas las demás condiciones relevantes. La precedencia temporal, recepción, admisión, procesamiento, respuesta técnica, coincidencia de identificadores o éxito técnico no bastan por sí solos para adjudicar contribución causal.

Se distinguen, como clases potencialmente concurrentes y no necesariamente excluyentes:
- \`NECESSARY_CONTRIBUTION\`: sin la intervención/etapa considerada, la trayectoria definida no existiría bajo el contraste contrafactual especificado.
- \`ENABLING_CONTRIBUTION\`: la intervención hace factible la trayectoria o elimina una barrera relevante, sin implicar que sea causa única o suficiente.
- \`MODIFYING_CONTRIBUTION\`: la trayectoria también existiría, pero cambiaría una propiedad relevante bajo el contrafactual sin esa intervención.

Una contribución puede ser parcial, concurrente o colateral. Estas clases no implican signo positivo de Outcome ni creación de Value. La propiedad afectada debe identificarse en el DGP; no se presume que cualquier cambio de secuencia, factibilidad o atributo sea sustantivo sin regla de relevancia preespecificada.

La adjudicación debe referirse a una etapa concreta del ciclo —\`Request_opportunity\`, \`Request_attempt\`, \`Request_received\`, \`Request_admitted/rejected\`, \`Request_processing\` o \`Request_response\`— sin colapsar sus mecanismos. La oportunidad estandarizada común es una asignación/probe del harness; no se considera automáticamente una intervención realizada por el servicio ni una contribución causal. Cuando no se produce una etapa posterior, el DGP debe representar el mecanismo de no transición sin imputar una contribución de esa etapa.

Se mantiene segregación entre:
1. **Verdad del generador (\`truth_dgp\`)**: intervención/etapa, propiedad de trayectoria, contraste contrafactual, clase de contribución y procedencia de la etiqueta verdadera.
2. **Evidencia observada (\`observed_evidence\`)**: registros y mediciones permitidos al analizador, sin revelar etiquetas o potenciales contrafactuales reservados al generador.
3. **Adjudicación/evaluación**: comparación de inferencia del analizador con verdad segregada, reportando falsos positivos, falsos negativos y errores de clasificación; no convertir trazabilidad en prueba causal.

El registro conceptual de contribución deberá poder identificar etapa de petición, propiedad de trayectoria, contraste contrafactual, clase(s) de contribución, verdad DGP y evidencia observable, además de identidad/versionado/procedencia. Esto no congela un schema físico.

Esta adjudicación es mecanística y no modifica elegibilidad, población, unidad experimental, asignación ni estimando ITT; no se condiciona la inclusión a eventos post-Z. Tampoco define por sí sola Outcome o Value, ni equipara petición con t5 Consider, t6 Sel/Start, t7 Exec, Outcome t8 o Value t9. No amplía el reloj t−1/t0…t9 ni H. D2 sigue como escenario primario candidato y D1 secundario; DEC-C10-066/067 no se reabren.

**OPEN:** especificación de los contrastes concretos de D2; propiedades de trayectoria causalmente relevantes; control de causas concurrentes/colaterales e interacciones; definición de intervención por etapa; positividad/soporte y versiones de tratamiento; evidencia observable y medición; reglas de atribución para contribuciones múltiples; sensibilidad a contrafactuales alternativos; relación con estimandos total, directo e indirecto y mediación.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen \`scientific_execution=false\` y \`execution_authorized=false\`; \`main\` no se modifica.

## 9. Reconciliación de estados históricos tras decisiones B1 y arquitectura A/B (2026-11-11)

Las secciones anteriores conservan fielmente el estado de la matriz al redactarse. Las menciones allí a cardinalidad de oportunidades, modalidad estandarizada, identidad de B1 o existencia de beneficiario como OPEN deben interpretarse ahora con la precedencia temporal de las decisiones posteriores, no como estado vigente sin reconciliar.

| Tema | Referencia histórica de esta matriz | Decisión posterior vigente | Estado actualizado |
|---|---|---|---|
| Arquitectura A/B | Value no instanciado en Opción A; alcance de B aún no seleccionado | DEC-C10-095 acepta A como base y B como extensión sintética separada | ACCEPTED AS DESIGN ARCHITECTURE; B instance OPEN |
| Tipo B1 | Beneficiario no confirmado; no inferible desde CMP.owner/roster A | B1 aceptada como tipo candidato de entidad solicitante-beneficiaria | ACCEPTED AS CANDIDATE TYPE; not a materialized instance |
| Entidad B1 por UE | Cardinalidad/relación OPEN | DEC-C10S-B1-UNIT-001 acepta una B1 por UE y vínculo versionado a servicio lógico aislado | ACCEPTED AS DESIGN DECISION; isolation and concrete identities OPEN |
| Modalidad de petición | Harness estandarizado era recomendación aún no aceptada | DEC-C10S-B1-REQUEST-MODE-001 acepta modalidad estandarizada primaria candidata y envío endógeno secundario/adversarial | ACCEPTED AS DESIGN DECISION; not protocol-frozen |
| Cardinalidad | Número de oportunidades OPEN | DEC-C10S-B1-OPPORTUNITY-CARDINALITY-001 acepta N_opportunities=1 por UE como candidato primario | ACCEPTED AS DESIGN DECISION; window/payload/protocol OPEN |
| Enlace petición–trayectoria | Cardinalidad/tipos OPEN | DEC-C10S-B1-REQUEST-TRAJECTORY-LINK-001 acepta asociación temporal, trazabilidad y contribución causal como tipos distintos | ACCEPTED CONCEPTUALLY; material rules OPEN |
| Adjudicación causal petición–trayectoria | Contrastes y contribuciones OPEN | DEC-C10S-B1-CAUSAL-ADJUDICATION-001 exige contraste contrafactual por etapa y verdad DGP segregada | ACCEPTED AS DESIGN CONTRACT; D2-specific contrasts OPEN |
| Estimandos D2 | ITT/efecto focal/mediación no reconciliados en esta matriz | DEC-C10S-D2-ESTIMAND-SEPARATION-001 organiza C1–C5 | ACCEPTED AS DESIGN ARCHITECTURE; estimands and identification OPEN |

**Consecuencia para Outcome/Value:** las decisiones B1 y A/B resuelven el tipo candidato y ciertas cardinalidades de diseño, pero no crean por sí mismas una consecuencia valorable ni una dimensión V_j. B1 sigue sin instancia material completa: demanda/Need_preZ, relación concreta, consecuencia, perspectiva/autoridad, dimensiones, indicadores, fuentes, escalas, horizonte y reglas de valoración permanecen OPEN. O-CONF sigue siendo el Outcome con mejor anclaje conceptual en A, pero su ficha §224 continúa incompleta. No se declara ninguna ficha O/V operacionalizada.

**Regla de mantenimiento:** no volver a listar como OPEN la decisión ya aceptada de N_opportunities=1 o la modalidad estandarizada; listar únicamente los detalles materiales aún abiertos. Mantener el texto histórico y esta reconciliación como addendum, sin borrar trazabilidad. Véase también `C10_S_CLOSURE_SEQUENCE_AND_C1_ITT_WORKPLAN_001.md`.


## 10. Reconciliación PA — estado vigente de Outcome y Value (2026-11-11)

El paquete PA confirma que la arquitectura A/B debe preservarse sin transferencia de resultados:

- **A / Outcome técnico:** O-CONF conserva el mejor anclaje conceptual disponible por F*/FP-01…08, pero no es una medida operacional confirmatoria. Predicados, mapping, tolerancias, oráculo ciego/independiente, snapshots, cobertura y adjudicación siguen pendientes. O-MIG/O-SVC/O-REC/O-BUR tampoco están operacionalizados.
- **B / Value:** B1 por UE, modalidad de oportunidad estandarizada y N=1 por UE permanecen como decisiones de diseño aceptadas en su alcance. No hay instancia material completa del beneficiario/servicio ni consecuencia independiente, perspectiva/autoridad, dimensiones V_j, indicadores, fuentes, escalas, baseline, horizonte o regla de adjudicación.
- **P179:** se mantiene Value como vector durante identificación y se preservan trade-offs. No se seleccionan por defecto las cinco dimensiones candidatas, no se impone un escalar y no se introducen pesos.
- **No circularidad:** ningún V_j se define como recodificación de A_f, ΔT_acc, Reach, selección, ejecución u Outcome técnico; si se desea valorar uno de esos constructos, debe reformularse explícitamente la pregunta causal.
- **ITT:** C1 es una familia de contrastes por variante × población × resultado/dimensión × horizonte. Un ITT sobre O_k no identifica ITT sobre V_j ni demuestra ΔT_acc→ΔV. La especificación actual no permite un ITT confirmatorio completo para A ni para B.

**Dictamen:** `OUTCOME_NOT_OPERATIONALIZED / VALUE_NOT_INSTANTIATED`. No se inventa un beneficiario, una consecuencia, una dimensión, un indicador ni una regla de agregación. El detalle integrado está en §15 de `C10_S_C1_ITT_D2_RECONCILIATION_DRAFT_001.md`. Sin freeze, implementación o ejecución.


## 9. Reconciliación PC — alcance de Outcome/Value para C3/C4 (2026-11-11)

La reconciliación PC del maestro C10-S §268 confirma que los estimandos C3/C4 deben adjudicarse por resultado: cada Outcome técnico O_k y cada dimensión contextual V_j requieren dictamen propio. No se transfiere identificación de ITT sobre O a ITT sobre V_j ni a mediación sobre V_j.

La arquitectura de Value vectorial de P179 se mantiene. No se seleccionan las cinco dimensiones históricas ni se reduce a V1; no se inventan beneficiario, perspectiva, escala, regla, horizonte, pesos o agregación. La variante A puede sostener Outcomes técnicos cuando sus fichas se completen; no contiene Value contextual instanciado. La variante B sigue siendo extensión sintética separada, pero no dispone aún de beneficiario/perspectiva ni fichas V_j completas.

O-CONF conserva el mejor anclaje técnico candidato, pero no tiene todavía ficha §224 completa (predicados, mapping, tolerancias, oráculo, snapshots, cobertura y adjudicación). T_acc/ΔT_acc/Reach/trayectoria/F* no se reutilizan como Outcome ni Value por circularidad. Estados no observados, no aplicables, censurados, disputados y desconocidos no se convierten en cero.

Para C4, el mediador es ΔT_acc* completo; Reach/Π_H pueden integrar una secuencia transformacional explícita. La mediación sobre Value no es evaluable hasta disponer de V_j y un beneficiario/observador contextual. La mediación sobre O_k solo podrá evaluarse cuando O_k tenga ficha operacional y el contrato longitudinal/identificación esté cerrado. P179, P182 y P183 se mantienen como contratos, no como evidencia ejecutada. Véase maestro §268.


## 511. Reconciliación B2–B3 — consecuencia B1, Outcome técnico y Value contextual (2026-11-11)

El planteamiento aceptado como base de trabajo queda desarrollado en `C10_S_B2_B3_BENEFICIARY_OUTCOME_VALUE_RECONCILIATION_DRAFT_001.md`. La consecuencia valorable se refiere a B1 respecto de Need_preZ; Outcome técnico y Value contextual se miden separadamente. No se presupone una relación causal exclusiva Outcome→Value ni se define V_j como función mecánica de Outcome, accesibilidad, Reach, trayectoria o ejecución. Pueden existir vías directas/colaterales de la política hacia la consecuencia y Value.

Se mantienen B1 por UE, una oportunidad estandarizada por UE y las decisiones de identidad/enlace ya aceptadas. Need_preZ, Request_event, D_resource, procesamiento, Outcome, consecuencia B1 y V_j no se colapsan. Ausencia de petición/recepción/ejecución no equivale a ausencia de necesidad ni Value=0.

P179 mantiene Value como vector y trade-offs; las cinco dimensiones históricas son candidatas, no una lista confirmatoria. O-CONF es el mejor anclaje técnico candidato, pero su ficha §224 está incompleta. Ningún O_k ni V_j está operacionalizado. Cada uno requiere ficha independiente §224 y controles P182/P183, incluidos error, fiabilidad, acuerdo, ausencia, censura, disputa, unknown y sensibilidad. No se transfiere identificación ITT de Outcome a Value, ni entre dimensiones; C3/C4 permanecen no identificados en el D2 material actual.

**Dictamen:** B2–B3 reconciliado semánticamente; operacionalización, perspectiva, consecuencia, dimensiones, instrumentos, escalas, horizonte y adjudicación OPEN. Sin nueva decisión científica, Design Freeze o autorización de ejecución.


## 12. Actualización §224 — ficha O-CONF y separación de V_cont (2026-11-12)

La sección histórica §10 y los estados PA §§9–11 describen la ficha O-CONF antes del cierre documental N16. Se mantienen como registro histórico; la especificación posterior es el plan §16.184 y la matriz F* §22.

O-CONF queda especificado parcialmente como resultado terminal de adjudicar una instancia de configuración × ruta completa contra F*. F* es el criterio, no un Outcome duplicado. El ancla lógica son los estados post-aplicación/post-check F2_DST_APPLIED y A2_DST_APPLIED; no se han materializado snapshots, evento ni timestamp. Su escala lógica es 1/0/? con SCOPE_ERROR/NOT_EVALUABLE separado; FP-01…07 se agregan sin compensación bajo IAM y FP-08 permanece como gate probatorio separado. Los contratos PAR/RUL aceptados no completan el catálogo atómico global ni los predicados FP-04/05.

La ficha §224 sigue incompleta: fuente/oráculo implementado y validado, IAM poblado, predicados/mappings/tolerancias restantes, C0 ambiental, G/H, unidad material, cobertura, error, acuerdo, missingness, cegamiento efectivo y provenance material permanecen abiertos. O-CONF no está operacionalizado ni se selecciona como Outcome confirmatorio final.

La extensión B conserva la selección provisional de V_cont por DEC-C10-099. V_cont mide cumplimiento temporal de la función B1; O-CONF mide conformidad terminal de ruta. La distinción conceptual y los contrastes candidatos se documentan en §§16.183–16.184; validez discriminante aún CONDITIONAL/NOT_VERIFIABLE. No se transfieren resultados/identificación entre O-CONF y V_cont ni entre Outcome y Value.

Estado: O_CONF_FICHE_PARTIAL / O_CONF_NOT_OPERATIONALIZED / V_CONT_SELECTED_PROVISIONALLY / DISCRIMINATION_NOT_VERIFIED / NO_DESIGN_FREEZE / NO_EXECUTION_AUTHORIZED.
