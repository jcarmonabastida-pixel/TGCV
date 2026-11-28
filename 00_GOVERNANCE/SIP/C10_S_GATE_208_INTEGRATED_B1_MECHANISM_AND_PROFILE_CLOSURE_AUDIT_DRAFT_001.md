# C10-S — Gate 208: cierre integrado de cobertura funcional B1 y resolución de L207-01…04

**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** INTEGRATED_DOCUMENTARY_RECONCILIATION / R208-A_PROPOSED_PENDING_OWNER_ACCEPTANCE / PROFILE_STATE_CROSSWALK_RESOLVED_IN_PROPOSAL / RUNTIME_CONSTITUTIVITY_CRITERION_DEFINED / CAPACITY_AND_REQUEST_INFERENCE_BOUNDED / §51_OPEN / NOT_DESIGN_FROZEN / NO_SCHEMA / NO_CODE / NO_TESTS / NO_EXECUTION.

## 1. Propósito y cambio de método

Gate 208 consolida en una sola operación los cuatro pendientes L207-01…04. No crea cuatro gates ni cuatro matrices. El objetivo es cerrar la semántica B1 que puede resolverse con el DGP y las decisiones aceptadas, separar lo que debe permanecer fuera del núcleo confirmatorio y preparar su integración posterior en los artefactos maestros.

La operación aplica la precedencia de `00_GOVERNANCE/README.md` y la regla `HISTORICAL_RECONSTRUCTION_BEFORE_NEW_WORK_RULE_v0.1.md`: reutilizar DEC-C10-068/099…104, §§49–52, Gates 145–154 y 206–207, sin reabrir decisiones aceptadas ni crear mecanismos no estipulados.

## 2. Fuentes y precedencia reconstruidas

Se han cotejado:
- `00_GOVERNANCE/README.md`, bootstrap y estado canónico de `main`;
- `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`, §§49–52;
- `C10_S_SYNTHETIC_LOGICAL_SERVICE_FUNCTIONAL_CONTRACT_DRAFT_001.md`;
- Gate 147-B (clasificación de familias);
- Gate 148/R148-A (D_valid, D_enabled, O y A);
- Gate 149 (crosswalk DEC-C10-099…104);
- Gate 150/R150-A (obligación contractual de PROFILE);
- Gate 151/R151-A8 (ausencia de trayectoria independiente de PROFILE exposure);
- Gate 152/R152-A1…A6;
- Gate 153 (tensión de composición);
- Gate 154 (aceptación de alcance temporal acotado de A_B1);
- Gate 206 (composición lógica) y Gate 207 (cobertura y L207-01…04);
- DEC-C10S-B1-OPPORTUNITY-CARDINALITY-001: una oportunidad estandarizada por UE como configuración primaria candidata aceptada, sin convertirla en monitor continuo.

No se ejecutaron validadores locales. La operación es documental; no declara PASS integral de bootstrap ni verifica materialmente todos los artefactos auxiliares.

## 3. Regla de precedencia aplicable después de Gate 154

Gate 154 delimita el predicado temporal adjudicado por A_B1/V_cont al comportamiento de admisión/no-admisión exigido por ENABLED, incluyendo disponibilidad runtime cuando impide efectivamente ese comportamiento.

Por tanto:
- PROFILE sigue siendo configuración declarada y obligación contractual de B1.
- PROFILE exposure no tiene trayectoria truth independiente en el DGP actual y queda fuera de la dimensión temporal adjudicada por V_cont.
- La validez declarativa D_valid de RUL-SVC-ENABLE-PROFILE-01, la habilitación declarada D_enabled, la disponibilidad runtime O y la capacidad efectiva A siguen siendo predicados distintos.
- D_valid no se transforma en uptime, y ni D_valid ni D_enabled aislados demuestran O/A.
- La aceptación de Gate 154 prevalece para el alcance temporal A_B1/V_cont frente a formulaciones anteriores que incluían PROFILE exposure en la continuidad compuesta. No se reescribe la historia de Gates 139–153.

## 4. Resolución integrada propuesta R208-A

### R208-A1 — PROFILE como estado declarativo versionado, no como trayectoria de exposición

Todo cambio efectivo de PROFILE se conserva en EventHistory como transición declarativa de configuración, con identidad/versión, estado anterior/posterior y event_time, conforme a R144-A y R146-A…D. Se conserva también la identidad de la configuración y la regla RUL aplicable.

No se crea una transición autónoma de PROFILE exposure. Un cambio de PROFILE, por sí solo, no cambia A_B1 ni V_cont bajo el alcance aceptado en Gate 154. La exposición sigue siendo obligación contractual, pero no adjudicable temporalmente en el DGP vigente.

D_valid se evalúa separadamente sobre cada estado declarativo versionado. No se fusiona con D_enabled, O, A ni A_B1.

### R208-A2 — Tratamiento de configuraciones que violan RUL

Para el núcleo confirmatorio primario, el soporte de configuraciones debe satisfacer RUL-SVC-ENABLE-PROFILE-01 en todos los estados declarativos generados. Una configuración que viole la RUL se clasifica como fallo de conformidad del Generator/DGP o, si se desea estudiar deliberadamente, como caso negativo/adversarial separado y explícitamente versionado.

Una violación de D_valid no se recodifica como A_B1=0, no genera UNKNOWN funcional y no se incluye silenciosamente en el estimando confirmatorio de V_cont. A_B1 sigue juzgando exclusivamente la función temporal de admisión delimitada por Gate 154. Esta es una regla propuesta para decisión expresa, no una modificación implícita de DEC-C10-068.

### R208-A3 — Criterio de constitutividad runtime

Un elemento de proceso/módulo, listener/superficie o dependencia ya comprendido en §§49–50 se representa como estado causal de EventHistory solo si se cumplen conjuntamente:

1. pertenece a una familia ya enumerada en §50;
2. está declarado como componente/mecanismo de la instancia sintética, con identidad y versión;
3. su estado es un determinante en la función generativa de disponibilidad/capacidad de admisión O/A;
4. un cambio de ese estado puede alterar el comportamiento de admisión requerido en al menos un estado admisible del DGP, manteniendo explícitas las demás condiciones.

Si no satisface estos criterios, es antecedente, telemetría o evidencia, no transición truth funcional. Si varios mecanismos/antecedentes producen un único cambio funcional, EventHistory conserva una transición funcional atómica y su provenance causal múltiple; no duplica eventos por cada log, retry o componente.

No se presumen redundancia, failover, sustitución, degradación parcial ni independencia de mecanismos. Si la instancia sintética no declara un mecanismo concreto, no se inventa para completar el catálogo.

### R208-A4 — Dependencias y capacidad/recursos: inclusión condicional, no expansión automática

Las dependencias y recursos permanecen como familias condicionales de §50. Solo se instancian en el núcleo confirmatorio si el DGP identifica de antemano:
- el elemento concreto y su versión;
- su papel causal no redundante o su interacción estipulada;
- el estado funcional relevante;
- la regla que conecta ese estado con O/A y la admisión.

Se preserva la separación de stock, instalación, disponibilidad/asignación, demanda y consumo. Una métrica de consumo, una reserva o la mera existencia de un recurso no crea por sí sola una transición de A_B1.

Si no existe una función de suficiencia/capacidad y un régimen de demanda explícitos en el DGP vigente, no se genera una transición autónoma de capacidad/recursos en el núcleo confirmatorio. Se mantiene como familia condicional para escenarios posteriores, que requerirán especificación/versionado antes de entrar en el estimando.

### R208-A5 — Solicitud individual no equivale a capacidad general ni a historia continua

El ciclo oportunidad → intento → recepción → admisión/rechazo → procesamiento/respuesta es discreto y separado de EventHistory funcional. La ausencia de oportunidad o intento no demuestra fallo; un resultado individual no adjudica por sí solo la capacidad general o continua A_B1.

La cardinalidad primaria aceptada de una oportunidad estandarizada por UE se conserva. Sirve para un contraste/probe individual bajo condiciones comunes, pero no demuestra capacidad bajo carga sostenida, demanda natural ni continuidad de admisión durante intervalos. No se añaden probes, cargas ni oportunidades repetidas al núcleo por inferencia.

La truth continua de A_B1 procede del estado funcional generado por el Generator y sus transiciones, no de extrapolar una solicitud aislada. El resultado de la solicitud puede ser evidencia observacional para Analyzer dentro de sus límites de identificación, nunca sustituto de EventHistory.

### R208-A6 — Semántica temporal, historia y UNKNOWN preservados

Se mantienen:
- estado inicial post-Z, persistencia, simultaneidad atómica y suborden explícito solo para estados intermedios funcionalmente relevantes (R144-A);
- identidad/versionado y completitud lógica de EventHistory (R146-A…D);
- separación EventHistory / PROCESS_EVENT / evidencia / TruthBundle / Analyzer / Evaluator;
- operador estricto DEC-C10-102 y estados {1,0,?};
- ? solo para indeterminación intrínseca de truth generada y explícitamente estipulada, nunca por falta de señal, petición, campo, mecanismo no especificado, defecto de historia/harness o incapacidad de observación;
- fronteras/ventana y agregación de DEC-C10-100/101/104, sujetas a los parámetros aún abiertos de §51.

No se seleccionan reloj físico, soporte, rejilla, T*, Δ, K, δ_event, δ_det, τ_follow ni calibración S3.

## 5. Matriz consolidada de cierre de L207

| Pendiente | Resolución propuesta | Estado tras aceptación de R208-A |
|---|---|---|
| L207-01 PROFILE → EventHistory/A_B1 | PROFILE se conserva como estado declarativo versionado; D_valid separado; no proyecta a A_B1/V_cont | Cerrable lógicamente |
| L207-02 Constitutividad runtime | Criterio de pertenencia causal a O/A; no añadir componentes no declarados | Criterio cerrable; roster concreto depende del DGP |
| L207-03 Capacidad/recursos | Solo si mecanismo, suficiencia y demanda están explícitos; de lo contrario fuera del núcleo confirmatorio | Cerrable por exclusión conservadora; extensión abierta |
| L207-04 Solicitud individual → capacidad | No inferencia; oportunidad única no es monitor continuo ni prueba de capacidad sostenida | Cerrable |
| Cobertura de cinco familias §50 | Se preservan; no se crea sexta familia | Cerrable en alcance |
| Completitud generativa | Requiere roster y función generativa concretos; no se demuestra por auditoría documental | Abierta para materialización/conformidad |

## 6. Consecuencia para el diseño confirmatorio mínimo

R208-A permite mantener un núcleo B1 pequeño y falsable:
- configuración declarativa ENABLED/PROFILE versionada;
- RUL declarativa evaluada separadamente;
- estados runtime solo para mecanismos constitutivos explícitos que puedan cambiar admisión;
- A_B1/V_cont limitado a admisión/no-admisión y disponibilidad runtime efectiva;
- una oportunidad estandarizada por UE como observación discreta, sin usarla como monitor;
- EventHistory como truth generada y completa para las transiciones funcionales incluidas.

No permite afirmar disponibilidad bajo carga arbitraria, uptime general de producción, cumplimiento íntegro de todas las obligaciones B1 ni continuidad de PROFILE exposure.

## 7. Estado global de diseño y trabajo que sigue siendo necesario

La aceptación de R208-A cerraría la cobertura lógica de B1 en el alcance actual, pero **no** implica Design Freeze ni readiness de implementación. Permanecen como dependencias de cierre del experimento sintético, reutilizando los contratos y registros ya existentes:

1. **Contrato temporal y S3:** resolver §51, soporte común, T*, Δ, K, τ_follow, episodio terminal/censura, mapping event_time→intervalos y curva de detección/cobertura S3.
2. **Arquitectura causal D2:** demostrar/definir la población P*_{τ2}, roster B, aislamiento material, unidad UE/UA, Z/provenance, factibilidad y soporte de q_X*/g_A/r_common; respetar DEC-C10-103 y Gate 121–122. Si aislamiento no se demuestra, no presumir asignación individual ni identificación.
3. **DGP transformacional:** cerrar mapping de condiciones REL/COND/RES/DEP/BLOCK, T_acc completo, F1/F2/A1/A2, F*, alternativas y Reach; reutilizar Gate 118–120 y contratos ya existentes, sin recrear matrices.
4. **Outcome/Value:** fijar medición independiente y regla/versión/horizonte/beneficiario; mantener V_cont como dimensión seleccionada acotada, no Value general.
5. **Identificación y estadística:** cerrar ITT-D2 como efecto de paquete, θ_A(q_X*,r_common;V_cont) como atribución focal condicionada, C4 secundario, vías directas/interacciones, missingness, sensibilidad, P177–P183, N/potencia/precisión y R/Monte Carlo; no inferir identificación por aleatorización sola.
6. **Truth/evidence/Analyzer/Evaluator:** cerrar diccionario y contratos de roles, firewall, TruthBundle, Analyzer bounds/abstención, evaluación independiente computacional y conformidad.
7. **Plan de validación:** reutilizar Test Contract Register, Closure Control Matrix y matrices existentes; mapear criterios a fixtures y pruebas futuras sin crear duplicados.

La secuencia debe minimizar operaciones separadas: tras aceptar este crosswalk, preparar **un único paquete integrado de cierre de diseño** que actualice el maestro y sus artefactos dependientes, presente las decisiones científicas aún no resueltas en un único docket agrupado por dependencias, y concluya con un contrato de implementación/preflight. No crear un Gate por cada parámetro ni por cada test.

## 8. Dictamen

**Recomendación:** aceptar R208-A1…A6 como delimitación lógica conservadora del B1 confirmatorio vigente. Resuelve conjuntamente L207-01…04 sin modificar las DEC existentes ni ampliar el DGP. Las extensiones de PROFILE exposure, capacidad bajo carga, mecanismos runtime no enumerados o protocolos de petición requieren una decisión y DGP versionados, y quedan fuera del núcleo actual.

La aceptación, si se produce, debe propagarse al maestro C10-S, Decision Log y contratos afectados conforme al plan Draft 004. Hasta entonces, las reglas anteriores son propuestas de reconciliación, no decisiones aceptadas.

## 9. Límites y no-autorizaciones

Este Gate no:
- modifica DEC-C10-068/099…104 ni crea una nueva DEC;
- altera el DGP original, §51 o las decisiones R144/R146/R147/R148/R150/R151/R152/R154;
- crea schema, EventHistory físico, ledger, código, harness, fixtures o test IDs;
- ejecuta validadores, pruebas, generación, simulación, calibración, estimación, Monte Carlo o experimento;
- declara completitud generativa material, aislamiento, positividad, identificación causal, potencia ni validez de Value;
- autoriza implementación, ejecución científica ni promoción a `main`.

`scientific_execution=false`  
`execution_authorized=false`  
`implementation_authorized=false`
