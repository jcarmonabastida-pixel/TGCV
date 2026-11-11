# C10-S — Secuencia de cierre y plan de trabajo C1 (ITT D2)

**ID:** C10-S-CLOSURE-SEQUENCE-001  
**Versión:** 001  
**Fecha:** 2026-11-11  
**Estado:** WORKING CONTROL RECORD / ACCEPTED SEQUENCE FOR CONTINUATION / NOT DESIGN-FROZEN  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)  
**Propósito:** fijar una secuencia estable de cierre y evitar reabrir decisiones aceptadas o crear ciclos de reconciliación sin entregable.  
**Límite:** trabajo documental y científico de diseño. No autoriza Design Freeze, schemas físicos, fixtures, código, simulación ni ejecución.

## 1. Regla de trabajo

La especificación se cerrará por paquetes dependientes, no mediante revisiones generales recurrentes. En cada paquete:

1. recuperar y reutilizar contratos y decisiones existentes;
2. registrar únicamente contradicciones reales, dependencias no resueltas o material nuevo;
3. producir un contrato integrado o un dictamen de no-identificación/limitación;
4. actualizar los documentos de control afectados y verificar la persistencia;
5. declarar qué queda cerrado documentalmente y qué permanece OPEN.

Una decisión aceptada no se vuelve a someter a aprobación por mera conveniencia editorial. Solo se reabre si aparece evidencia de contradicción, imposibilidad material, dependencia incompatible o una nueva pregunta científica. Los antecedentes históricos permanecen trazables y se marcan como supersedidos cuando corresponda; no se borran.

## 2. Secuencia de cierre adoptada

| Orden | Paquete | Resultado exigido | Dependencia principal |
|---|---|---|---|
| 1 | **C1 — ITT D2** | Contrato de efecto de asignación: unidad/población, brazos/versiones, resultado(s), horizonte, contrafactual, estimación, supuestos y límites interpretativos | Reconciliar población, UE/interferencia, políticas D2, Outcome/Value y seguimiento existentes |
| 2 | **Outcome y Value** | Instancias/fichas independientes de Outcome técnico y Value contextual; beneficiario, perspectiva, consecuencia, dimensiones, fuentes, escalas, horizonte y trade-offs | C1 identifica qué resultados se contrastan; no presupone que A y B compartan resultados |
| 3 | **C2 — Primeras etapas** | Efectos de asignación separados sobre `C_dep*`, `A_f*`, `D_f*` y `ΔT_acc*`, con medidas y denominadores propios | Política D2 material, unidad, población y medición |
| 4 | **C3 — Efecto de accesibilidad** | Mapping D2→g, régimen común q, población/soporte y dictamen de vías colaterales | C1/C2 y medición independiente de accesibilidad |
| 5 | **C4 — Mediación** | DAG longitudinal, confusión mediador–resultado inducida por Z, intervención mediadora, estimando interventional, método y sensibilidad | C1, C2, Outcome/Value y C3 |
| 6 | **C5 + DGP** | Contrastes contrafactuales por etapa petición–trayectoria, propiedades relevantes, escenarios y truth segregada | Contratos B1/request ya aceptados; Outcome/Value y arquitectura causal |
| 7 | **Estadística y Analyzer** | Aplicación de P177/P178/P179/P182/P183, identificación por estimando, precisión, sensibilidad, abstención y criterios ex ante | Paquetes anteriores |
| 8 | **Contrato integrado de implementación** | Modelo de datos, schemas, IDs, interfaces Generator–Analyzer–Evaluator, fixtures previstos, validadores, aceptación, reproducibilidad y trazabilidad | Cierre de los siete paquetes previos |

Se permiten tareas documentales auxiliares en paralelo, pero ningún paquete posterior puede utilizarse para declarar cerrado uno anterior ni se congelan schemas/fixtures antes de resolver sus dependencias científicas.

## 3. Condiciones de cierre comunes

La secuencia solo se considerará completada cuando concurran:

- **Semántica:** constructos, roles, eventos y relaciones definidos sin ambigüedad relevante.
- **Causalidad:** cada estimando tiene población, unidad, intervención, contrafactual, resultado, horizonte y supuestos explícitos.
- **Medición:** accesibilidad, Reach, trayectoria, Outcome y Value tienen medidas separadas, fuentes, errores y adjudicación.
- **Técnica:** interfaces y contratos implementables y versionados.
- **Verificación:** requisitos trazados a pruebas, oráculos, criterios de aceptación y estados de abstención.

La especificación completa será solo candidata a Design Freeze; no prueba causalidad ni autoriza ejecución.

## 4. C1 — ITT D2: alcance del siguiente trabajo

### 4.1 Objeto causal que no se debe alterar

C1 es el efecto total de asignación a las dos políticas D2 aceptadas como comparador primario candidato:
- `B_g0^D2`: no programar/iniciar el intento focal de provisión.
- `B_g1^D2`: programar un intento estandarizado de provisión técnica focal.

La asignación es Z. El contraste C1 es por asignación, no por provisión recibida, instalación lograda, accesibilidad alcanzada, petición recibida, selección o ejecución. La asignación no asigna directamente `C_dep*`, `A_f*`, `D_f*` ni `ΔT_acc*`.

C1 conserva interpretación de efecto de política/paquete si hay vías colaterales activadas diferencialmente por D2. No se denomina efecto puro de accesibilidad salvo que las condiciones de C3 se demuestren por separado. No se deriva un efecto residual/directo por resta automática de C1 y C3/C4.

### 4.2 Reconciliación de resultados A/B — límite de formulación

DEC-C10-095 acepta una arquitectura A/B:
- **Variante A:** DGP base aceptado. Puede evaluar accesibilidad, Reach, trayectorias y Outcomes técnicos; Value contextual no está instanciado y no puede sostener una afirmación `ΔT_acc → Value`.
- **Variante B:** extensión sintética independiente y versionada para instanciar beneficiario y Value. B1 está aceptada como tipo candidato; la instancia de beneficiario, demanda, consecuencia, perspectiva, dimensiones, escalas y regla de valoración siguen abiertas.

Por tanto, C1 no se escribirá como un único ITT sobre un Value ya definido. El contrato debe separar, al menos, el contraste ITT sobre Outcome(s) técnico(s) que A pueda operacionalizar y el contraste ITT por dimensión `V_j` cuando B disponga de fichas de Value admisibles. La separación no implica que ambos resultados estén hoy listos ni que sus estimandos compartan población/horizonte. No se inventarán dimensiones, indicadores, pesos ni un índice escalar.

### 4.3 Reutilización obligatoria

Antes de proponer una nueva fórmula o población, C1 debe reconciliar:
- `C10_S_POPULATION_ELIGIBILITY_AND_COMPARATOR_RECONCILIATION_DRAFT_001.md`: `P*_{τ2}`, `P*_F), elegibilidad pre-Z, D2 y requisitos de legitimidad;
- `C10_S_C10D1_S4R_ESTIMAND_RECONCILIATION_DRAFT_001.md`: distinción `ITT_Z^D2`, `LATE_f^D2`, `θ_Af(q_X*)` y `θ_A(q));
- `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`: unidad, roles, asignación, reloj y seguimiento;
- `C10_S_VALUE_MINIMUM_CORE_RECONCILIATION_MATRIX_DRAFT_001.md` y `C10_S_B_VARIANT_MINIMUM_BENEFICIARY_VALUE_CONTRACT_DRAFT_001.md`: Outcome/Value, B1 y separación A/B;
- DEC-C10-066/067/095 y decisiones B1 posteriores: no reabrir sus decisiones aceptadas; traducir sus límites al contrato C1.

### 4.4 Cuestiones que C1 debe resolver o dictaminar

1. **Población:** determinar si C1 usa `P*_{τ2}`, una población elegible B1 específica o poblaciones distintas por variante/resultado. La decisión debe ser pre-Z; no condicionar inclusión a eventos post-Z. `P*_F) no se convierte en población primaria por defecto.
2. **Unidad y asignación:** UE es la unidad a la que se asigna Z; B1 por UE y una oportunidad estandarizada por UE son decisiones aceptadas de diseño, pero aislamiento real y ausencia de interferencia siguen por demostrar. Si hay compartición, especificar clúster/exposición y estimando compatible.
3. **Brazos/versiones:** fijar qué versiones de `B_g0^D2`/`B_g1^D2` se contrastan y qué significa adherencia/recepción sin reemplazar ITT por tratamiento recibido.
4. **Resultados:** identificar Outcome(s) disponibles para A y, solo si B queda operacionalizada, dimensiones `V_j`. Mantener Outcome técnico y Value independientes.
5. **Horizonte:** recuperar la definición temporal existente y decidir qué seguimiento es común y factible; no inventar duración ni alterar el reloj `t−1/t0…t9` o H.
6. **Identificación:** aleatorización, consistencia/versiones, interferencia, observación, missingness/censura y selección; dictamen separado por resultado/dimensión.
7. **Interpretación:** ITT total de política/paquete; ninguna atribución a accesibilidad, mediación o efecto local sin los contratos C3/C4/IV correspondientes.

### 4.5 Entregable de C1

Un único contrato integrado C1 que incluya:
- definición formal del estimando por resultado/dimensión y población;
- estimando de asignación y contrafactuales potenciales;
- unidad, población, elegibilidad y asignación;
- brazos/versiones y política de tratamiento;
- baseline, horizonte y seguimiento;
- Outcome/Value y sus estados de observación;
- supuestos de identificación y análisis de sensibilidad;
- vías colaterales y alcance de interpretación;
- reglas de missingness/censura, denominadores y no exclusión post-Z;
- dictamen por estimando: IDENTIFIED / PARTIALLY_IDENTIFIED / NOT_IDENTIFIED / INDETERMINATE, según contratos estadísticos aplicables;
- trazabilidad a fuentes, decisiones y pruebas previstas.

No se fijan en este registro valores de población, N, horizonte, dimensiones, parámetros, umbrales ni método de estimación final.

## 5. Estado de partida y control de versiones

A fecha 2026-11-11:
- DEC-C10S-D2-ESTIMAND-SEPARATION-001 está registrada en el plan, la matriz de cierre y el Decision Log; es arquitectura aceptada, no contrato de estimación cerrado.
- DEC-C10-066/067 preservan D2 como comparador primario candidato y sus políticas materiales.
- DEC-C10-095 acepta A/B como arquitectura; B1 es tipo candidato, no instancia de Value.
- DEC-C10S-B1-UNIT-001, DEC-C10S-B1-OPPORTUNITY-CARDINALITY-001, DEC-C10S-B1-REQUEST-MODE-001, DEC-C10S-B1-REQUEST-TRAJECTORY-LINK-001 y DEC-C10S-B1-CAUSAL-ADJUDICATION-001 permanecen aceptadas como decisiones/contratos de diseño no congelados.
- Las referencias históricas que todavía describen cardinalidad de oportunidades o modalidad estandarizada como abiertas deben leerse con precedencia de las decisiones posteriores; no deben volver a presentarse como si no existieran.
- No hay autorización de implementación ni ejecución: `scientific_execution=false`; `execution_authorized=false`.

## 6. Siguiente operación

**Operación activa: C1.1 — reconciliación focal de población, UE/interferencia, brazos D2 y resultados Outcome/Value.**

No pedir al usuario que vuelva a aprobar decisiones ya aceptadas. Solo elevar una pregunta de decisión cuando la documentación existente no la resuelva y su resolución sea necesaria para especificar el estimando. Si hay incompatibilidad entre documentos, registrar la discrepancia y proponer el mínimo ajuste; no reescribir silenciosamente el contrato histórico.


## 7. Resultado de C1.1 (2026-11-11)

La reconciliación focal se documenta en `C10_S_C1_ITT_D2_RECONCILIATION_DRAFT_001.md`. Dictamen: C1 sigue OPEN; D2 está definido como contraste de políticas asignadas, pero población, unidad efectiva bajo interferencia, resultados y horizonte no están cerrados. `P*_{τ2}` se conserva como candidato histórico de población C1, no como población aprobada; `P*_F` permanece subpoblación para apertura funcional exclusiva, no población primaria por defecto. UE=UA sigue condicionado a demostrar aislamiento. A no tiene Value contextual instanciado; B requiere completar instancia B1 y fichas V_j. H=3 es profundidad transformacional candidata, no duración de seguimiento.

**Siguiente operación activa: C1.2 — reconciliar composición de elegibilidad basal `E_i`, predicados constitutivos y evidencia/indeterminación; recuperar el contrato exacto de aleatorización D2 (probabilidades, estratos, versión y provenance).** No introducir nueva población ni nueva política por conveniencia.


## 8. C1.2 — elegibilidad basal y asignación D2 (2026-11-11)

La auditoría queda incorporada como §12 de `C10_S_C1_ITT_D2_RECONCILIATION_DRAFT_001.md`. Se confirma que la fórmula histórica de E_i con C_other fue retirada como regla operativa; C_auth,base=1 es condición común/invariante D2; C_dep,0=0 no basta para inferir A_f,0*=0; E_req_preZ es distinta de elegibilidad experimental. El mecanismo material de aleatorización (ratio, estratos, algoritmo/semilla y manejo de desviaciones) no está especificado en los contratos revisados y no se inventa.

**Decisión de arquitectura pendiente:** confirmar P*_τ2 como población objetivo primaria candidata C1, manteniendo P*_F como subpoblación secundaria para apertura funcional exclusiva. La recomendación es conservar la precedencia ya propuesta en POP-CMP-001/DGP temporal, sujeta a cerrar E_i, predicados, indeterminación y soporte. C1 sigue OPEN.


## 9. Resolución de la decisión poblacional y siguiente operación C1.3 (2026-11-11)

La pregunta de §8 queda resuelta por aceptación explícita del usuario y por `DEC-C10S-C1-POPULATION-PRECEDENCE-001`: `P*_{τ2}` es la población objetivo primaria candidata de C1; `P*_F` es subpoblación secundaria de apertura funcional exclusiva. No volver a pedir esta confirmación.

**C1.3 — composición de E_i:** reconstruir el contrato de elegibilidad basal a partir del DGP/IAM y predicados constitutivos vigentes. No inventar predicados, no reutilizar la fórmula histórica con `C_other`, y no confundir validez de la instancia DGP, aplicabilidad de τ2, inaccesibilidad focal basal, Need_preZ ni admisión de la petición. El resultado puede ser una composición parcial y un dictamen de no operacionalización si los contratos materiales no permiten cerrarla; no forzar un cierre artificial.


## 10. Resultado C1.3 y activación C1.4 (2026-11-11)

El crosswalk `C10_S_C1_BASELINE_ELIGIBILITY_CROSSWALK_DRAFT_001.md` concluye que `E_i` no puede derivarse directamente de cardinalidades de clase ni del roster mínimo de servicio. Se propone conceptualmente `E_i=E_scope∧App*(τ2,S0)`, pero no está aceptado ni operacionalizado. `C_dep,0=0` y `A_f,0*=0` siguen siendo condiciones separadas; F_alt,0 solo determina P*F.

**Operación activa C1.4:** construir el crosswalk por predicado/registro IAM pre-Z para `C_SRC`, cruzado con `App*(τ2,S0)`, `C_dep,0` y términos de `A_f,0*`; clasificar boundary P0/P1/DUAL, obligatoriedad, aplicabilidad, papel causal, evidencia y 1/0/?/NA. Si no hay IAM material, documentar vacíos lógicos, no inventar registros. C1 permanece OPEN.


## 11. Resultado C1.4 y activación C1.5 (2026-11-11)

`C10_S_C1_PREZ_IAM_CROSSWALK_C10S_001.md` documenta el crosswalk lógico de C_SRC/IAM. Dictamen **PARTIAL / MATERIAL BLOCKED BY ABSENT IAM AND SNAPSHOTS**: no hay snapshots C10-S observados ni filas IAM/coverage por UE; las etiquetas de scopes 7×5 no son registros físicos. No se puede clasificar población ni declarar REF=0. `E_i=E_scope∧App*(τ2,S0)` sigue propuesta no aceptada.

**C1.5:** cerrar el predicado de aplicabilidad `App*(τ2,S0)` y su frontera con A_f; determinar si E_scope es gate de alcance DGP o elegibilidad confirmatoria y el efecto de selección; fijar regla pre-Z para unknowns; recuperar el mecanismo de asignación D2 y dictaminar soporte/factibilidad. No volver a solicitar confirmación de P*τ2/P*F.


## Actualización de secuencia — cierre del ciclo PA (2026-11-11)

PA se ha reconciliado integralmente en una única iteración. Véase §15 de `C10_S_C1_ITT_D2_RECONCILIATION_DRAFT_001.md` y §16.155 del plan integrado.

**Resultado:** `PA_RECONCILED_DOCUMENTALLY / C1_MATERIAL_BLOCKED / NOT_DESIGN_FROZEN`. No hay nueva decisión de usuario pendiente: las lagunas se deben a ausencia de IAM/snapshots, asignación material, aislamiento, Outcome/Value y horizonte. No se reinician C1.1–C1.4 ni se reabre la precedencia P*τ2/P*_F.

**Siguiente paquete:** PB — material D2, servicio B1, provisión/instalación/dependencias, protocolo de petición y primera etapa C2. Los bloqueos que dependan de B1/snapshots se resolverán allí; PA solo se reabrirá para integrar material nuevo.


## 12. Actualización de secuencia tras PB-MAT y B2–B3 (2026-11-11)

La secuencia histórica de §11 se actualiza por precedencia de los ciclos posteriores, sin borrar su trazabilidad:

- **PC:** reconciliación documental C3/C4 en maestro §268; C3 y mediación siguen no identificadas en el D2 material actual.
- **PD:** reconciliación documental del DGP, mecanismos C5 y evaluación adversarial en §269; cuantificación y parámetros siguen OPEN.
- **PE:** reconciliación documental técnica en §270; contrato técnico parcial, implementación no lista.
- **PB identidad:** DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001 aceptada y registrada en §271.
- **PB-MAT:** reconciliación material D2 en §272; inventario material ausente y aislamiento no demostrado.
- **B2–B3:** base de trabajo aceptada y reconciliación semántica en §273; Outcome no operacionalizado y Value no instanciado.

El siguiente trabajo no debe reiniciar PA–PE ni reabrir decisiones aceptadas. Debe integrar los bloqueos todavía abiertos en una sola reconciliación de factibilidad confirmatoria: asignación/probabilidades y soporte; unidad/interferencia; evidencia material IAM/snapshots/provisión; selección y fichas §224 de Outcome/Value; y estimandos por dimensión bajo PC. Si los artefactos materiales siguen ausentes, el dictamen correcto será bloqueo/no-identificación, no cierre por estipulación.

No se autoriza Design Freeze, schema físico, fixtures, implementación, generación de datos, simulación, estimación o ejecución científica. `scientific_execution=false`; `execution_authorized=false`.



## 13. Resultado integrado de factibilidad confirmatoria y siguiente operación

La reconciliación conjunta queda registrada en C10_S_INTEGRATED_CONFIRMATORY_FEASIBILITY_AND_DESIGN_FREEZE_RECONCILIATION_DRAFT_001.md. PA–PE, PB-MAT y B2–B3 se reutilizan sin reinicio. El diseño no es confirmatoriamente factible/materialmente identificable ni está listo para Design Freeze: faltan asignación material y soporte D2; aislamiento/interferencia; IAM/C_SRC, snapshots y provisión; Outcome y Value operacionalizados; y cuantificación del DGP/estadística.

C1 ITT, C2 primeras etapas, C3 efecto de accesibilidad/θ_A/θ_Af, LATE_f y C4 IIE no están identificados/evaluables con el estado actual. No hay cotas numéricas justificadas. ITT de política/paquete no se equipara al efecto de accesibilidad; el efecto mediado no se obtiene por ajuste convencional; el residual no se calcula por resta ad hoc. Outcome y Value son constructos distintos, sin imponer relación causal exclusiva Outcome→Value.

**Nota de secuencia supersedida (2026-11-11):** la recuperación íntegra del maestro se completó mediante blob Git y se añadió §274. La siguiente operación es reconciliar consistencia entre §§266–274 y los contratos especializados, corregir referencias cruzadas obsoletas y después abordar bloqueos materiales/medición bajo autorización específica. No Design Freeze, implementación ni ejecución autorizadas.

## Corrección de recuperación del maestro C10-S — 2026-11-11

La lectura inicial del maestro mediante Contents devolvía contenido vacío, pero el blob Git fue recuperado íntegramente (1,134,655 caracteres / 12,136 líneas) e inspeccionados sus §§266–273. La incidencia está **RESUELTA**; el documento no estaba perdido. Se ha añadido §274 al maestro con la reconciliación integrada de factibilidad y Design Freeze. No queda pendiente recuperar el maestro; permanecen los bloqueos científicos/materiales y los gates indicados en el artefacto rector. La limitación de concordancia línea por línea por inaccesibilidad del maestro queda superada para el contenido recuperado; no equivale a validación local ni CI.


## 14. Resultado del ciclo D2 — asignación, población y soporte (2026-11-11)

El ciclo integrado queda registrado en C10_S_D2_ASSIGNMENT_POPULATION_SUPPORT_RECONCILIATION_DRAFT_001.md y maestro §275. Se reutilizan PA/C1, C1.3–C1.4, PB-MAT, DEC-C10-066/067 y la precedencia poblacional aceptada.

**Resultado:** se aclara el contrato, pero no se inventan parámetros. La probabilidad de asignación Z, ratio, estratos, algoritmo/semilla y provenance siguen OPEN; las probabilidades de programación D2 condicionales a Z (0/1) ya estaban aceptadas y no son la aleatorización. c/b, s=0.80, composición E_i/App, q_X* y soporte, posible q_L*, aislamiento e interferencia siguen OPEN/BLOCKED. No se reabren PA/PB ni decisiones aceptadas.

**Siguiente dependencia:** disponer de una fuente aprobada/material autorizada para roster, IAM/C_SRC, snapshots y cobertura por UE. Sin esa base no puede adjudicarse E_i, estimarse q_X*, comprobar soporte ni demostrar aislamiento. No se autoriza captura, implementación, fixtures, simulación, estimación o ejecución.


## 15. Resultado del ciclo Outcome/Value (2026-11-11)

El paquete integrado queda reconciliado en `C10_S_OUTCOME_VALUE_OPERATIONALIZATION_RECONCILIATION_DRAFT_001.md` y maestro §276. Se reutilizan §§222–225, C-Value §§264–265, B2–B3, F*, P179/P182/P183, MEAS/MISS y PA–PE.

**Resultado:** F* criterio funcional; O-CONF resultado adjudicado, no endpoint duplicado; sigue candidato sin ficha §224 completa. Value permanece vectorial, sin dimensiones, autoridad/criterio, escalas o instrumentos seleccionados. ITT Outcome/Value separados; no identificación C3/C4. Próxima dependencia: resolver materialmente F*/O-CONF y el contrato de valoración B1, sin inventar roster ni medidas. No hay autorización para captura, schema, fixtures, implementación, simulación o ejecución.

## 16. Caso de valoración B1 — resultado y siguiente dependencia (2026-11-11)

El caso semántico se reconcilia en `C10_S_B1_VALUATION_CASE_RECONCILIATION_DRAFT_001.md`. Reutiliza el microdominio aceptado, B1/UE, servicio por UE y una oportunidad estandarizada por UE. El probe no equivale a demanda natural ni Value. Need_preZ se formula como objetivo operativo basal para sostener una operación de servicio predeclarada en destino, pero el contenido concreto de esa operación permanece OPEN. La consecuencia B1 se separa de procesamiento, respuesta, F*, O-CONF y accesibilidad. La envolvente de consecuencias no es roster V_j; no se eligen dimensiones ni medidas. La autoridad de valoración y el horizonte siguen OPEN.

**Siguiente dependencia:** nombrar/aceptar el contenido de la operación basal de B1 antes de completar el caso de valoración. En paralelo, el bloqueo material de PA/PB/D2 requiere una fuente aprobada para roster UE, IAM/C_SRC, snapshots y cobertura; este documento no sustituye esa fuente ni autoriza captura. No Design Freeze, schema físico, fixtures, implementación, simulación, estimación o ejecución.


## 17. Actualización del ciclo B1 — clase de propósito basal aceptada (2026-11-11)

Se registra la aceptación de que B1 tiene un objetivo operativo basal consistente en mantener operativa una función de servicio que depende de la configuración migrada al entorno destino. La clase de propósito y la relación B1–configuración–función quedan aceptadas como base semántica; la operación concreta sigue OPEN y debe nombrarse/versionarse antes de instanciar Need_preZ como truth por UE.

El cierre de Need_preZ es, por tanto, **estructural y parcial**: se conserva 1/0/? pre-Z, unknown no equivale a ausencia, truth_dgp no equivale a observed_evidence y no se infiere necesidad de Z, provisión, accesibilidad, Reach, oportunidad, petición, procesamiento, Outcome o ejecución. No se filtra la población ITT por eventos post-Z. La consecuencia B1 se deriva respecto de la operación concreta y permanece separada de F*/O-CONF; la envolvente analítica no selecciona V_j.

**Siguiente operación:** reconciliar el contrato funcional/servicio ya definido en el microdominio para identificar la operación concreta sin inventarla ni equipararla a un predicado técnico. Después, cerrar truth_preZ/adjudicación y consecuencia candidata, y solo entonces reconsiderar fichas §224/Value. No reabrir B1/UE, cardinalidad, servicio por UE, oportunidad estandarizada ni decisiones D2. No Design Freeze ni autorización de implementación/ejecución.

## 18. Reconstrucción del contrato de servicio B1 — siguiente definición sustantiva (2026-11-11)

La reconstrucción histórica de DEC-C10-068/069 y maestro §§174–178/216 confirma que el servicio es un servicio lógico sintético de procesamiento de solicitudes, con parámetros constitutivos ENABLED/PROFILE y regla de consistencia. El contrato no define el contenido de las solicitudes ni la operación que realiza el servicio sobre la configuración migrada. Por tanto, la operación concreta de B1 no se recupera de los artefactos existentes.

**Siguiente paso requerido:** especificar qué solicitud/operación necesita mantener operativa B1 y qué dependencia funcional tiene de la configuración en destino. No se equipara a F1/F2, instalación, aplicación técnica o SF. Hasta entonces Need_preZ solo tiene clase de propósito aceptada, sin truth concreta por UE; consecuencia B1 y Value siguen sin instanciar. No reabrir decisiones aceptadas ni inventar contenido de servicio. Sin Design Freeze ni autorización de implementación/ejecución.



## 19. Resultado del paquete B1 — especialización funcional mínima aceptada (2026-11-11)

El usuario acepta la especialización mínima del servicio como contrato funcional de trabajo, registrada en §14 de `C10_S_B1_VALUATION_CASE_RECONCILIATION_DRAFT_001.md`.

**Resultado:** el servicio recibe solicitudes dirigidas a su instancia lógica; comprueba la habilitación declarada en destino; puede admitirlas cuando `PAR-SVC-ENABLED=true`; y expone el perfil declarado por `PAR-SVC-PROFILE`. STANDARD y READ_ONLY siguen siendo perfiles permitidos con ENABLED=true, pero no se atribuyen diferencias semánticas adicionales. La admisión/no admisión es un evento propio y no equivale a procesamiento, respuesta, ejecución, satisfacción de necesidad, consecuencia B1 o Value.

Esta aceptación especializa el contrato de DEC-C10-068 sin modificar sus parámetros ni RUL, sin crear una regla constitutiva nueva y sin afirmar que el comportamiento esté implementado o probado.

**Efecto sobre Need_preZ:** queda disponible una formulación funcional de trabajo: mantener disponible en destino un servicio capaz de admitir solicitudes conforme a su estado declarativo de habilitación y exponer el perfil declarado. La clasificación truth por UE, los criterios de pertenencia y la adjudicación de evidencia siguen OPEN y deben fijarse pre-Z. Se mantienen 1/0/?; unknown no equivale a 0; truth_dgp no equivale a observed_evidence; no se filtra ITT por eventos post-Z.

**Siguiente paquete activo — B1-PREZ:** integrar en una sola reconciliación la ficha basal por UE (definición/versionado, verdad, evidencia admisible, regla 1/0/?, unknown y disputa), las consecuencias potenciales respecto de la capacidad de admisión y las fronteras frente a procesamiento, respuesta, F*/O-CONF, accesibilidad y Value. No seleccionar dimensiones V_j, indicadores, escalas, instrumentos ni horizonte. Si STANDARD/READ_ONLY o el procesamiento posterior requieren semántica adicional, mantenerlo como dependencia explícita.

No reabrir decisiones B1/UE, servicio por UE, oportunidad estandarizada, D2 ni DEC-C10-068. No modificar main, RMA, Evidence→Claim Matrix, STATUS o claims. No Design Freeze ni autorización de schema físico, fixtures, captura/materialización, implementación, generación de datos, simulación, estimación o ejecución científica. `scientific_execution=false`; `execution_authorized=false`.


## 20. Resultado del paquete B1-PREZ — adjudicación y consecuencias reconciliadas (2026-11-11)

El contrato integrado queda registrado en `C10_S_B1_PREZ_ADJUDICATION_AND_CONSEQUENCE_RECONCILIATION_DRAFT_001.md`.

**Resultado documental:** la definición funcional de trabajo de Need_preZ, la separación truth_dgp/observed_evidence, las reglas conceptuales 1/0/? y los requisitos de admisibilidad, temporalidad, provenance y cobertura quedan definidos. Se explicita que observed=0 exige evidencia afirmativa y universo de fuentes cerrado; ausencia de registro o búsqueda sin resultados no bastan. Need no se infiere de asignación, accesibilidad, oportunidad, petición, admisión, procesamiento, respuesta, F*/O-CONF o ejecución. No filtra población ITT.

**Consecuencias:** se reconcilia la estructura de disponibilidad funcional, continuidad, demora/oportunidad, recuperación y riesgo/reversibilidad, siempre como envolvente analítica no exhaustiva. Se mantienen separadas admisión, procesamiento, respuesta, Outcome técnico, Beneficiary_consequence y Value. No se elige V_j, medida, escala, instrumento, autoridad ni horizonte.

**Límite material:** no existe aún roster truth por UE ni evidencia observada con cobertura demostrada. Por tanto, la regla está cerrada documentalmente, pero la adjudicación unidad por unidad permanece OPEN/BLOCKED. STANDARD/READ_ONLY y procesamiento posterior siguen abiertos, sin bloquear la definición basal mínima aceptada.

**Siguiente operación:** comprobar el inventario real de fuentes pre-Z admisibles y su cobertura por B1/UE, usando solo material ya disponible/autorizado. Si falta, registrar el vacío y mantener ?. No generar roster, snapshots ni fixtures. No reabrir decisiones aceptadas ni autorizar implementación/ejecución.


## 21. Resultado del paquete B1-PREZ-SOURCE-INVENTORY — auditoría de fuentes y cobertura (2026-11-11)

Se incorpora `C10_S_B1_PREZ_EVIDENCE_SOURCE_INVENTORY_AND_COVERAGE_AUDIT_DRAFT_001.md`.

**Dictamen:** se revisaron los artefactos de diseño C10-S y el protocolo S1–S8. Existen contratos y especificaciones que respaldan la definición conceptual de B1, el servicio lógico, la separación Need/Request/Outcome/Value y las reglas de provenance/adjudicación. No se localizaron fuentes materiales pre-Z vinculadas a unidades B1/UE concretas, roster material, declaraciones basales por unidad, snapshots IAM/configuración, expedientes EVIDENCE_REGISTER/CLAIM_EVIDENCE_LINK poblados ni adjudicaciones E1/E2.

**Cobertura:** NONE para identidad material, binding B1–UE–service_instance, objetivo basal individual, configuración/IAM pre-Z, snapshots, provenance de fuentes concretas, cobertura negativa y truth DGP por unidad. El contrato genérico ENABLED/PROFILE está definido parcialmente como plantilla, pero no hay mapping ni evidencia por instancia. NONE no significa ausencia del objeto.

**Adjudicabilidad:** no se emiten filas ni etiquetas para unidades no materializadas. Con las fuentes revisadas, no se puede sostener observed Need_preZ=1 ni 0; el resultado procedimental sería ?/BLOCKED. No se infiere Need=0 de ausencia de solicitudes, logs o documentos sin universo cerrado. Truth DGP permanece NOT MATERIALIZED y segregada.

**Límite de la búsqueda:** el dictamen cubre los artefactos C10-S revisados en la rama de investigación; no afirma inexistencia de documentos externos o no consultados. No se inspeccionaron sistemas reales, conectores ni runtime.

**Siguiente paso documental:** precisar el catálogo de tipos de fuente y el criterio de cobertura por unidad, sin crear roster, truth, snapshots ni fixtures. Cualquier materialización o captura requiere autorización específica posterior. No se reabren decisiones B1 aceptadas ni se autoriza implementación/ejecución.

## 22. Reconciliación de la frontera de implementabilidad — 2026-11-11

Se incorpora el registro rector `C10_S_IMPLEMENTABILITY_BOUNDARY_AND_MINIMUM_SPEC_RECONCILIATION_DRAFT_001.md`.

**Corrección operativa:** los bloqueos de factibilidad confirmatoria material D2 (roster real, IAM/C_SRC, snapshots, inventario B, aislamiento y soporte empírico) no son automáticamente bloqueos para construir el harness metodológico sintético. El Generator puede generar unidades, asignaciones, dependencias, truth y evidencia sintéticas bajo un DGP explícito y versionado. Esto no acredita que las condiciones se cumplan en D2 material ni permite transferir resultados del harness a la instancia confirmatoria.

**Estado reconciliado:**
- La arquitectura y decisiones aceptadas de PA–PE, B1, D2, población, roles y JCS se reutilizan; no se reabren.
- El harness sintético aún no tiene especificación ejecutable completa.
- Los bloqueos de especificación se agrupan en tres cierres integrados: (A) DGP parametrizado y estimandos/identificación; (B) observación, Outcome/Value y contratos Analyzer/Evaluator; (C) schemas físicos, interfaces, roles, pruebas y reproducibilidad.
- Los bloqueos materiales de confirmación se conservan en un carril separado y no se usan para inflar el cierre del harness.
- No se autoriza implementación ni ejecución.

**Siguiente operación única:** reconciliación integrada A–B–C de cierre de especificación ejecutable, conforme al criterio de salida del nuevo registro. No reiniciar PA–PE ni crear paquetes independientes por cada subcomponente.

## 23. Regla vinculante de cierre hacia especificación implementable (2026-11-11)

Esta regla operacionaliza la reconciliación de §22 y rige las siguientes iteraciones de cierre C10-S.

### Objetivo único

Cerrar una **especificación ejecutable del harness metodológico sintético C10-S**. No ampliar el programa científico ni exigir que la instancia confirmatoria material D2 esté preparada para poder especificar e implementar el harness.

### Método de trabajo

1. Ejecutar una sola reconciliación integrada A–B–C:
   - **A — DGP y estimandos:** reglas generativas, temporalidad, asignación sintética, potenciales, parámetros por escenario y condiciones de identificación/abstención.
   - **B — observación y análisis:** proyección truth→evidence, cobertura/error/missingness/provenance, contratos genéricos Outcome/Value y salidas Analyzer/Evaluator.
   - **C — contrato técnico:** schemas físicos, IDs/cardinalidades/referencias, interfaces, serialización, roles y firewall verificables, tests/oráculos/tolerancias y reproducibilidad.
2. Reutilizar decisiones y contratos aceptados. No reabrirlos salvo contradicción material, fallo demostrado o dependencia lógica que impida cumplir un contrato.
3. Mantener un ledger acumulativo de estados. Un elemento CLOSED no reaparece como pendiente por descomponerlo en subcomponentes; solo puede reabrirse indicando evidencia concreta que invalida su cierre.
4. Cada cuestión abierta debe tener: decisión exacta pendiente, razón por la que impide el contrato implementable, alternativas mínimas y consecuencia de cada alternativa. No añadir requisitos de revisión externa ni nuevas auditorías exploratorias sin una necesidad contractual demostrada.
5. Clasificar cada requisito por destino: (i) especificación del harness; (ii) confirmación material D2; (iii) implementación/prueba técnica posterior; o (iv) ejecución/validación científica posterior. Solo (i) es objeto del cierre actual.
6. Cuando una decisión sustantiva de Outcome/Value no esté disponible, permitir contratos genéricos tipados y parametrizables únicamente si preservan semántica, procedencia, dimensiones y separación causal; no inventar constructos, indicadores, escalas, pesos ni resultados confirmatorios.

### Regla de no-expansión

No convertir la ausencia de materiales reales (roster, IAM/C_SRC, snapshots, inventario B, aislamiento, soporte empírico) en nuevos bloqueos para el harness sintético. El DGP debe representar sintéticamente los mecanismos y condiciones relevantes, pero sus resultados no acreditan la existencia de esas condiciones en D2 material.

No convertir tareas de ejecución o validación (captura, fixtures materializados, simulación, estimación, potencia empírica, replay, auditoría de resultados) en requisitos previos de especificación, salvo que una regla de generación, observación o evaluación no pueda definirse sin ellas. La especificación de cómo se ejecutarán esas pruebas sí pertenece al contrato; ejecutarlas no.

### Criterio único de terminación

La especificación se considerará implementable cuando una persona técnica pueda construir el harness sin inferir semántica ni decidir por su cuenta:
- qué genera cada componente y con qué reglas;
- qué información recibe y no recibe cada rol;
- cómo se representan las unidades, asignaciones, eventos, estados, verdad y evidencia;
- qué estimandos se calculan, bajo qué condiciones se identifican y cuándo se debe abstener;
- cómo se sellan y evalúan las salidas;
- qué pruebas, oráculos, tolerancias y controles verifican el comportamiento;
- cómo se reproduce un run y se conserva su provenance.

El cumplimiento de este criterio no equivale a Design Freeze, autorización de implementación, identificación causal confirmatoria ni autorización de ejecución científica.

### Próximo paso

Continuar directamente con la reconciliación integrada A–B–C, contrastando los artefactos existentes y resolviendo los huecos dentro del mismo ciclo. No volver a presentar PA–PE ni B1/D2 como paquetes por cerrar. Si al terminar persiste una decisión irreducible, elevar solo esa decisión concreta para adjudicación; no generar una nueva lista acumulativa de pendientes.

## 24. Ejecución de la reconciliación integrada A–B–C — 2026-11-11

**Artefacto rector:** `C10_S_SYNTHETIC_HARNESS_INTEGRATED_SPECIFICATION_DRAFT_001.md`.

**Resultado:** `A_B_C_RECONCILED / IMPLEMENTABLE_SPECIFICATION_CANDIDATE / NOT_DESIGN_FROZEN / NOT_IMPLEMENTED / NOT_EXECUTED`.

Se ha realizado la reconciliación integrada en un único artefacto, reutilizando DGP temporal/roles, base DGP, inventario finito/Reach, D2 assignment/population/support, PD, B1-PREZ, B2–B3, operacionalización Outcome/Value, PE y U_G. No se han reabierto decisiones aceptadas ni creado familias paralelas de datos o pruebas.

### A — DGP y estimandos

Quedan integrados el roster sintético y la unidad de asignación condicional a aislamiento, calendario t−1/t0…t9 y subledger de petición, configuración obligatoria de escenarios, secuencia generativa, separación programación/intento/provisión/C_dep/A_f*/D_f*/ΔT_acc*/Reach/trayectoria, potenciales, estimandos ITT/primeras etapas/θ_Af/LATE_f/C4 y reglas de identificación/abstención. Los parámetros sin decisión aprobada son inputs obligatorios de configuración; no reciben defaults. Los valores históricos .20/.80/s=.80 no se elevan a parámetros confirmatorios.

### B — observación y análisis

Quedan integrados truth_dgp / observed_evidence / evaluation_adjudication, proyección de evidencia con cobertura/error/missingness/censura, contenedor genérico de resultados OUTCOME_TECHNICAL y VALUE_CONTEXTUAL sin inventar V_j, contrato de salida por estimando×resultado×población×horizonte y evaluación posterior contra truth. O-CONF y Value conservan su estado no operacionalizado/no instanciado; un resultado no instanciado no se convierte en cero ni en missing ordinario. La no-identificación y abstención son salidas válidas.

### C — datos, interfaces y controles

Quedan definidos nueve tipos lógicos de artefacto, interfaces y precondiciones fail-closed de los seis componentes, identidades y referencias reutilizadas, reglas temporales/trivalentes, serialización por perfil de objeto, firewall por rol, manifiestos y criterios de prueba/reproducibilidad. JCS sigue limitado a UDG-01/U1. El contrato no selecciona tecnología de despliegue ni altera los contratos U_G existentes.

### Frontera y pendientes no bloqueantes del harness genérico

Se mantienen fuera de la especificación genérica, para la futura instancia confirmatoria material o escenarios sustantivos específicos: operación concreta de B1/Need_preZ por UE; ficha O-CONF; perspectiva/autoridad y dimensiones V_j; roster/IAM/snapshots/inventario/aislamiento/soporte D2 material; valores numéricos por escenario, N/R/tolerancias; y perfil físico/stack de despliegue. Los parámetros de escenario y métodos/tolerancias se proporcionan mediante configuración versionada. Si un estimando carece de semántica suficiente, el Analyzer devuelve NOT_IDENTIFIED/NOT_INSTANTIATED/INDETERMINATE en vez de inventarla.

Estas reservas no reabren PA–PE, B1, D2, población, cardinalidad, identidad de servicio ni decisiones JCS. No se añaden paquetes de cierre separados.

### Dictamen

La especificación del **motor/harness sintético parametrizado** queda reconciliada documentalmente y se considera candidata implementable bajo contratos de configuración explícitos. Esto no significa que una instancia confirmatoria D2 esté identificada, que Outcome/Value estén operacionalizados, que se haya concedido Design Freeze, ni que el código exista o haya sido probado.

**Siguiente estado de trabajo:** revisión/adjudicación de esta especificación integrada y, solo tras autorización expresa, implementación técnica del harness. La ejecución científica seguirá requiriendo autorización independiente. `scientific_execution=false`; `execution_authorized=false`.


## 25. Reorientación del cierre: experimento sintético causal como objetivo primario y secuencia experimento→playground (2026-11-11)

### 25.1 Objetivo rector

Se precisa y prevalece sobre cualquier lectura expansiva de §§22–24:

**El objetivo de C10-S es diseñar e implementar un experimento sintético capaz de someter a prueba una hipótesis causal sobre el puente entre accesibilidad transformacional (`ΔT_acc`) y Value.** El harness no es el fin científico; es la infraestructura experimental para generar escenarios con verdad conocida, producir evidencia observable y evaluar si el procedimiento causal recupera, limita, refuta o reconoce que no puede identificar el efecto.

La especificación integrada A–B–C se conserva como base contractual reutilizable. Su estado de candidata implementable se refiere al motor/harness parametrizado, no significa que el experimento causal principal esté ya suficientemente especificado, implementado o validado. No se declarará cerrado el objetivo por completar documentos, interfaces o schemas.

### 25.2 Criterio científico de suficiencia del experimento

El experimento mínimo debe permitir evaluar conjuntamente:

1. **Recuperación cuando existe el efecto:** en DGP donde una intervención bien definida sobre accesibilidad cambia Value, el diseño y Analyzer recuperan dirección y magnitud dentro de criterios ex ante justificados.
2. **Control de falsos positivos:** en DGP donde no existe efecto causal de accesibilidad sobre Value, no se atribuye espuriamente un efecto.
3. **Discriminación de mecanismos:** distinguir el efecto de asignación/política del efecto atribuible a accesibilidad, incluyendo vías directas/colaterales, mediación, interacciones y confusión inducida cuando sean parte del escenario.
4. **Robustez y límites:** evaluar heterogeneidad, errores de medida, interferencia, selección, missingness/censura y falta de soporte; producir identificación parcial, cotas o abstención cuando corresponda, sin forzar una estimación.
5. **Independencia semántica y de información:** generar y medir `ΔT_acc`, Reach/trayectoria, Outcome y Value como objetos diferenciados; Value se instancia explícitamente dentro del DGP sintético y no se define como función automática de accesibilidad, Outcome o éxito técnico. El Analyzer no accede a truth ni a potenciales.
6. **Reproducibilidad y evaluación:** mantener truth conocida y sellada, evidencia observada separada y evaluación posterior; justificar parámetros, población, estimandos, potencia/precisión, repeticiones y umbrales de aceptación antes de interpretar resultados.

Un resultado positivo solo demostraría recuperación bajo los DGP y supuestos ensayados; no probaría por sí mismo que el puente causal exista en sistemas reales ni que una operacionalización sintética de Value sea universal. Un resultado negativo o no identificado también es un resultado científico válido.

### 25.3 Reducción de alcance y regla contra el sobrediseño

No se exige completar la operacionalización de un caso real de migración para probar el método. El microdominio del servicio de migración y sus contratos ya desarrollados se reutilizan como fuente de estructura y como posible instancia sintética, pero solo se conserva en el experimento principal el detalle que sea necesario para:
- definir intervenciones y contrafactuales;
- generar la variación causal prevista;
- mantener separados los mecanismos transformacionales y las vías alternativas;
- construir una consecuencia/criterio de Value explícito, no circular y evaluable;
- generar evidencia observable con errores y limitaciones controlables.

Los detalles del caso que no afecten a esos requisitos no son gates del experimento principal. No se añaden nuevos contratos, auditorías, taxonomías o capas documentales sin demostrar qué amenaza causal o requisito de implementación resuelven. Las dimensiones y reglas de Value elegidas para un DGP son parámetros del experimento, no una definición universal de Value para TGCV.

### 25.4 Secuencia de producto y desarrollo: experimento primero, playground después

Se adopta como secuencia de trabajo recomendada:

**(1) cerrar el diseño experimental mínimo → (2) implementar el harness/experimento sintético → (3) verificar técnicamente y ejecutar, con las autorizaciones correspondientes, los escenarios de validación → (4) evaluar y documentar qué hipótesis, estimandos y condiciones quedan recuperados, refutados o no identificados → (5) construir el playground TGCV sobre el motor y contratos ya probados.**

No se construirá directamente el playground como sustituto de la implementación experimental. El playground es una capa de interacción, visualización y exploración que debe consumir un motor experimental estable; no debe decidir la semántica causal, generar sus propias reglas de Value ni convertirse en evidencia de validez por el hecho de funcionar visualmente.

Durante la especificación sí se podrán registrar requisitos de interfaz/API y necesidades de visualización para evitar bloquear la futura integración, pero no se desarrollará ahora una aplicación playground paralela. La arquitectura debe permitir que el harness funcione sin interfaz gráfica y que el playground lo invoque después mediante contratos estables.

### 25.5 Próxima operación y estado

La siguiente operación de cierre deja de ser una revisión documental general de A–B–C. Consiste en una **revisión científica focal de suficiencia del experimento sintético mínimo**, reutilizando A–B–C y los contratos previos para responder, sin reabrir decisiones aceptadas:

- cuál es la hipótesis causal primaria y qué estimando la representa;
- qué intervención/contraste identifica el efecto de accesibilidad y cómo se distingue del ITT de política;
- cuál es la instancia sintética mínima e independiente de Value;
- qué conjunto mínimo de DGP permite recuperación, nulo/falsación, vías alternativas y no-identificación;
- qué observaciones, análisis y criterios ex ante permiten juzgar recuperación, falsos positivos, precisión y abstención.

La salida será un diseño experimental mínimo integrado y una lista cerrada de decisiones verdaderamente irreducibles. Solo después de su aceptación se preparará la implementación técnica. La implementación no autoriza por sí misma la ejecución científica.

**Estado:** EXPERIMENT_FIRST / PLAYGROUND_AFTER_EXPERIMENTAL_ENGINE / SCIENTIFIC_EXECUTION_NOT_AUTHORIZED / NO_DESIGN_FREEZE.


## 26. Primera resolución de diseño: objeto causal primario del experimento sintético (2026-11-11)

**Estado:** WORKING DESIGN DIRECTION / PROPOSAL FOR INTEGRATED SPECIFICATION / NOT ACCEPTED AS DESIGN FREEZE / NOT IMPLEMENTED / NOT EXECUTED.

### 26.1 Distinción que gobierna el diseño

Se recupera y aplica la jerarquía del protocolo C10-D1 §§5 y 17 y de la reconciliación C10-S↔C10-D1:

- `θ_A(q)` es la pregunta científica de atribución específica a políticas factibles de accesibilidad bajo un régimen común.
- `ITT_Z^{D2}` es el efecto total de asignar las políticas materiales de provisión D2. No equivale por sí mismo a `θ_A(q)`, porque D2 puede activar vías directas/colaterales hacia Value.
- `LATE_f^{D2}` es un efecto local condicionado a supuestos IV; no es el efecto poblacional general de accesibilidad.
- El contraste focal de apertura de `τ2` no debe presentarse como efecto de todo `ΔT_acc`.

**Consecuencia para C10-S:** el experimento sintético principal debe estar diseñado alrededor de `θ_A(q)`, no alrededor de `ITT_Z^{D2}`. D2 se conserva como escenario secundario de mecanismo/política y como prueba de que el Analyzer no confunde un efecto de paquete con atribución específica a accesibilidad.

### 26.2 Tratamiento causal primario: políticas factibles de accesibilidad

No se asignará abstractamente un valor a `A` ni se tratará `ΔT_acc` como una variable binaria intercambiable con instalación, provisión o éxito técnico.

El tratamiento será un contraste entre dos políticas estocásticas/versionadas `g_1` y `g_0` que, dadas historias y condiciones relevantes, inducen distribuciones distintas de cambios estructurales de accesibilidad. Cada política:
- solo puede producir configuraciones pertenecientes al conjunto factible `A_fact(h)`;
- conserva identidad/versionado y reglas de transformación explícitas;
- actúa bajo un régimen común `q` de condiciones/historias compatible con ambas políticas;
- permite observar el cambio estructural de `T_acc` independientemente de Reach, trayectoria, ejecución, Outcome y Value;
- no introduce, en el escenario primario aislado, vías diferenciales directas a Value ajenas a la accesibilidad.

La intervención se define sobre políticas realizables que generan cambios de accesibilidad; no por fijación matemática de una variable que pueda producir estados imposibles.

### 26.3 Hipótesis y estimando primarios

La hipótesis primaria se formula para una dimensión sintética de Value `V_1`, seleccionada y operacionalizada exclusivamente como instancia explícita del DGP:

```
H0: θ_A(q; V1) = 0
H1: θ_A(q; V1) ≠ 0
θ_A(q; V1) = E[V1^(q,g1)] − E[V1^(q,g0)]
```

La alternativa es bilateral: TGCV no presupone que todo aumento de accesibilidad produzca necesariamente valor positivo. Los DGP de signo positivo y negativo permiten comprobar que el método recupera el signo verdadero; el DGP nulo permite comprobar que no fabrica un efecto.

Si una instancia posterior incluye varias dimensiones `V_j`, se reportarán efectos separados por dimensión. No se construirá un índice global ni se agregará el vector sin una regla de valoración independiente y justificada. El primer `V_1` no se elevará a definición universal de Value ni a dimensión obligatoria de TGCV.

El estimando es una diferencia entre resultados potenciales bajo dos políticas factibles de accesibilidad y el mismo régimen `q`. No es un efecto indirecto natural ni se obtiene sustituyendo `g_1/g_0` por distribuciones observadas condicionadas por D2.

### 26.4 Separación de asignación y atribución

Si las políticas `g_1/g_0` se asignan aleatoriamente y se implementan según sus versiones especificadas, el contraste por asignación identifica el efecto de esas políticas bajo consistencia, soporte e interferencia tratados por el diseño. No se necesita usar D2 como instrumento para el estimando primario.

El experimento incluirá, además, escenarios en los que:
- la política cambia accesibilidad y también una vía directa/colateral hacia Value;
- las políticas no tienen soporte común o no son factibles bajo ciertas historias;
- hay interferencia o exposición compartida;
- la medición de accesibilidad o Value es imperfecta/diferencial.

En esos escenarios el Analyzer debe distinguir el efecto de política/paquete del efecto atribuible a accesibilidad y, cuando proceda, declarar `PARTIALLY_IDENTIFIED`, `NOT_IDENTIFIED` o `INDETERMINATE`. La aleatorización de la política no autoriza por sí sola una etiqueta de efecto puro de accesibilidad.

### 26.5 Conjunto mínimo inicial de DGP para probar la hipótesis

La primera batería no será un factorial exhaustivo. Debe contener, como mínimo, estos contrastes lógicos:

1. **Focal con efecto no nulo:** `g_1/g_0` generan cambios diferentes de accesibilidad y `V_1` responde causalmente; sin vías diferenciales ajenas a accesibilidad. Prueba de recuperación de dirección, magnitud e incertidumbre.
2. **Nulo causal:** las políticas pueden variar accesibilidad, pero `V_1` no responde a esa variación. Prueba de control de falsos positivos.
3. **Vía directa/colateral:** la política afecta `V_1` por otra ruta además de accesibilidad. Prueba de no atribución espuria; el resultado admisible puede ser efecto de paquete/no identificación focal.
4. **No identificación:** falta de soporte/positividad, interferencia no resuelta o confusión relevante incompatible con el estimando. Prueba de abstención o límites en lugar de estimación forzada.

Los escenarios de signo contrario, heterogeneidad/interacción, error diferencial, missingness/censura y mediación se incorporarán como extensiones de robustez en la misma batería, reutilizando PD, P177/P178/P182/P183 y los IDs existentes. No se abrirán familias paralelas de tests.

### 26.6 Instancia sintética de Value: alcance y límite

La instancia primaria necesitará un `V_1` concreto con B1 como referente, `Need_preZ` basal, consecuencia para B1, perspectiva/autoridad, regla de valoración, unidad/escala, baseline y horizonte. Su regla se declarará en la configuración del DGP antes de generar los datos y será independiente de `ΔT_acc`, Reach, trayectoria, ejecución y O-CONF.

La regla sintética debe permitir que, manteniendo la misma accesibilidad, la consecuencia/Value pueda variar por otros mecanismos en los escenarios adversariales; y que, manteniendo constantes las vías ajenas, variar accesibilidad pueda producir efecto nulo, positivo o negativo según la verdad del DGP. Así se evita incorporar la hipótesis en la definición de Value.

La selección de la consecuencia y su regla concreta es una decisión de diseño pendiente del siguiente subpaso. No se rellenará el vacío con las cinco dimensiones históricas ni se presentará una escala sintética como operacionalización universal de TGCV.

### 26.7 Qué queda resuelto y qué no

**Resuelto como dirección de diseño:**
- estimando científico principal: `θ_A(q;V_1)`, dentro del alcance de una instancia sintética delimitada;
- intervención: políticas factibles/versionadas `g_1/g_0) sobre accesibilidad bajo régimen común `q);
- D2 ITT: efecto de política/paquete secundario, no sustituto de atribución a accesibilidad;
- hipótesis bilateral y escenarios mínimos de efecto, nulo, vía alternativa y no-identificación;
- Value sintético explícito, independiente y no universal.

**Sigue abierto para el cierre integrado mínimo:**
- definición concreta de la consecuencia B1 y ficha de `V_1);
- población/historias y régimen común `q) con soporte de ambas políticas;
- versiones realizables de `g_1/g_0) y regla de generación de `ΔT_acc);
- parámetros DGP y criterios ex ante de recuperación/error/abstención.

Estos cuatro puntos son las decisiones de especificación que hacen falta para instanciar y evaluar el experimento principal; no justifican reabrir toda la arquitectura B1/D2 ni completar el caso real de migración.

### 26.8 Próximo subpaso

Resolver en una única integración la instancia sintética mínima de B1/`V_1` y su vínculo causal con las políticas `g_1/g_0), comprobando no circularidad y posibilidad de efectos positivo, nulo y negativo. Después se fijarán el soporte/régimen común y los parámetros necesarios para los DGP mínimos.

**Estado:** PRIMARY_ESTIMAND_DIRECTION_SET / VALUE_INSTANCE_OPEN / ACCESS_POLICY_INSTANCE_OPEN / NO_DESIGN_FREEZE / NO_IMPLEMENTATION / NO_SCIENTIFIC_EXECUTION.


## 27. Instancia candidata mínima de consecuencia B1 y Value sintético (2026-11-11)

**Estado:** VALUE_INSTANCE_CANDIDATE / SEMANTIC_BOUNDARY_TESTED / NOT_ACCEPTED_AS_CONFIRMATORY_ENDPOINT / NOT_DESIGN_FROZEN / NOT_IMPLEMENTED / NOT_EXECUTED.

### 27.1 Reutilización de la función B1 ya aceptada

Se parte exclusivamente del contrato funcional aceptado:
- B1 pretende mantener disponible en destino un servicio capaz de admitir solicitudes conforme a `PAR-SVC-ENABLED`;
- el servicio expone el perfil declarado `PAR-SVC-PROFILE`;
- la admisión de una solicitud es distinta de procesamiento, respuesta, consecuencia B1 y Value;
- el contenido de la solicitud y la semántica diferenciada de STANDARD/READ_ONLY no se inventan.

No se amplía el servicio con una operación de negocio nueva.

### 27.2 Consecuencia candidata: continuidad funcional experimentada por B1

La consecuencia candidata es **la continuidad temporal de la función de servicio que B1 pretende mantener disponible**. No se define como el éxito de una petición concreta, sino como la proporción del intervalo de observación en que la función de admisión del servicio está efectivamente disponible para B1.

Sea (W) el intervalo común de valoración, fijado en el DGP antes de generar resultados, y sea (I_B(t)) el estado verdadero de disponibilidad de la función para B1 en el instante (t), definido por el contrato funcional aplicable. La consecuencia puede representarse como:

```
Q_B1(W) = (1 / |W|) ∫_W I_B(t) dt
```

En una implementación discreta, la integral se sustituye por la proporción de unidades temporales predefinidas en las que la función está disponible. El horizonte y la granularidad no se fijan aquí: serán parámetros explícitos y comunes del DGP, no valores escogidos tras observar resultados.

Esta variable describe continuidad funcional a lo largo de un intervalo; no es:
- el estado declarativo `ENABLED`;
- una única decisión `Request_admitted`;
- el procesamiento o respuesta de una solicitud;
- el snapshot terminal O-CONF/F*;
- accesibilidad, Reach, trayectoria o ejecución.

O-CONF sigue siendo una adjudicación técnica del estado de conformidad en su ancla/snapshot. `Q_B1(W)` caracteriza la continuidad de la función para B1 a lo largo del intervalo. La relación entre ambos puede ser imperfecta: un snapshot conforme no garantiza continuidad durante todo W, y una interrupción transitoria no determina por sí sola la conformidad terminal.

### 27.3 Regla valorativa candidata V1

Como primera instancia sintética acotada, se propone que B1 valore la continuidad de esa función, sin introducir una agregación de dimensiones ni pesos:

```
V1 = Q_B1(W)
```

- **Referente:** B1, una entidad sintética por UE.
- **Perspectiva:** interés funcional de B1, conforme a la perspectiva ya aceptada en B2–B3.
- **Autoridad:** regla normativa explícita del DGP; no se afirma que represente preferencias humanas observadas.
- **Interpretación:** proporción del intervalo común en que B1 dispone de la función que pretende mantener.
- **Escala:** [0,1], con 0 = función no disponible durante W y 1 = disponible durante todo W.
- **Dirección:** mayor valor representa mayor continuidad funcional.
- **Baseline:** estado/continuidad basal pre-Z, registrado separadamente si el estimando se expresa como cambio respecto del baseline. No se sustituye la definición del estimando `θ_A(q;V1)` por una diferencia de diferencias no especificada.
- **Horizonte:** W, común y versionado; duración y discretización pendientes de fijación en el DGP.
- **Agregación:** ninguna. V1 es una única dimensión contextual para este experimento sintético, no un escalar universal de Value ni una reducción del vector P179 para TGCV.

La regla es deliberadamente mínima: valora una consecuencia para B1 y no la accesibilidad estructural que podría contribuir a ella. La política de accesibilidad puede mejorar, no cambiar o empeorar Q_B1 según los mecanismos y condiciones del DGP. Por ello permite DGP de efecto positivo, nulo y negativo sin cambiar la definición de V1 entre escenarios.

### 27.4 Pruebas de no circularidad y discriminación

La instancia solo será admisible si el DGP puede producir y el diseño conserva, como mínimo, estos desacoplamientos:

1. **Accesibilidad mayor, continuidad igual:** `ΔT_acc` cambia, pero Reach o los mecanismos de servicio impiden que cambie Q_B1.
2. **Accesibilidad mayor, continuidad menor:** una vía adversa (p. ej. inestabilidad temporal o interrupciones inducidas) reduce Q_B1 pese a la expansión del espacio accesible.
3. **Misma accesibilidad, continuidad distinta:** una condición externa o vía colateral altera Q_B1 sin cambiar `T_acc`.
4. **Mismo O-CONF, continuidad distinta:** estados terminales equivalentes pueden tener historias temporales de disponibilidad diferentes.
5. **Continuidad igual, O-CONF distinto:** una ruta alternativa puede mantener la función durante W aunque el snapshot terminal difiera, si el contrato de conformidad así lo permite.
6. **Probe no equivalente a Value:** la oportunidad estandarizada sigue siendo un único estímulo/probe por UE; su admisión/no admisión no sustituye la medida temporal de Q_B1.

Estas son propiedades que debe permitir el DGP, no afirmaciones de que ocurran necesariamente en toda instancia.

### 27.5 Límite de validez y decisión pendiente

Esta propuesta hace explícita una regla sintética de valoración, pero su admisibilidad depende de una distinción que no debe ocultarse: continuidad funcional puede considerarse Value contextual para B1 solo bajo la estipulación normativa del DGP de que B1 valora disponer de esa función durante W. No demuestra que continuidad sea una dimensión universal, ni resuelve preferencias, costes, riesgos o trade-offs de un sistema real.

**Dictamen provisional:** `V1=Q_B1(W)` es una instancia mínima plausible para probar si el método recupera una contribución causal sobre una consecuencia valorada independiente de accesibilidad y de O-CONF. No se eleva todavía a endpoint confirmatorio: primero debe comprobarse que la ficha distingue suficientemente la consecuencia para B1 de un Outcome técnico y que la medición temporal es compatible con el reloj y la observación del harness. Si no supera esa comprobación, se descarta sin reabrir la arquitectura general de Value.

### 27.6 Qué se ha reducido

Para la primera prueba causal no es necesario completar:
- contenido de solicitudes de negocio ni semántica de STANDARD/READ_ONLY;
- roster material o evidencia real por UE;
- todas las dimensiones V_j o un índice global;
- operacionalización real de costes, riesgo, esfuerzo o satisfacción;
- un caso de migración completo.

Sí es necesario fijar en el siguiente cierre, conjuntamente, W y su discretización, la definición observable/verdadera de disponibilidad funcional, y cómo se mide Q_B1 independientemente de la reconstrucción de `T_acc` y del snapshot O-CONF.

**Estado:** CANDIDATE_V1_DEFINED / CONFIRMATORY_ADMISSIBILITY_PENDING / NO_DESIGN_FREEZE / NO_IMPLEMENTATION / NO_SCIENTIFIC_EXECUTION.


## 28. Dictamen de admisibilidad de V1=Q_B1(W): consecuencia retenida, Value confirmatorio no aceptado (2026-11-11)

**Estado:** Q_B1_RETAINED_AS_BENEFICIARY_CONSEQUENCE / V1_NOT_ADMISSIBLE_AS_CURRENTLY_DEFINED / VALUE_ENDPOINT_STILL_OPEN / NO_DESIGN_FREEZE / NO_IMPLEMENTATION / NO_SCIENTIFIC_EXECUTION.

### 28.1 Dictamen

La propuesta de §27 permite definir la continuidad temporal de la función de servicio como consecuencia relevante para B1. Sin embargo, la igualdad `V1=Q_B1(W)` no establece todavía una separación de constructo suficiente entre consecuencia/resultado funcional y Value.

El problema no es que una consecuencia funcional nunca pueda ser valorada. Es que, en la propuesta actual, la medida de Value coincide numéricamente y operacionalmente con la medida de disponibilidad/continuidad. La perspectiva B1 y la estipulación de que B1 valora esa continuidad aportan interpretación normativa, pero no especifican una regla de valoración diferenciada que permita comprobar qué añade Value respecto de la consecuencia funcional.

Por tanto:
- `Q_B1(W)` se conserva como **consecuencia contextual para B1** y variable intermedia potencial del DGP;
- `Q_B1(W)` no se acepta, en su formulación actual, como `V1` confirmatorio;
- no se declara operacionalizado Value ni se crea un resultado confirmatorio `Y_Value`;
- no se descarta la clase de consecuencia ni se reabre la arquitectura B1, Outcome/Value o P179.

### 28.2 Razón metodológica

La regla genérica de Value exige una valoración de consecuencias para B1 bajo perspectiva, autoridad y criterio ex ante, diferenciada de Outcome técnico, accesibilidad, trayectoria y ejecución. Una identidad `V1=Q_B1(W)` solo sería suficiente si el DGP justificara explícitamente que la propia continuidad es, por estipulación normativa, la magnitud valorada y además estableciera cómo se distingue su medida valorativa de la medida técnica de la consecuencia. Esa justificación y esa distinción no están presentes todavía.

No se resolverá la dificultad añadiendo un peso, coste o penalización arbitrarios. Una función de utilidad con varios componentes solo será admisible si sus componentes y trade-offs responden a una regla normativa explícita del mundo sintético, son independientes de la hipótesis causal y permiten pruebas de sensibilidad. No se introducen ahora tales componentes.

### 28.3 Consecuencia para el reloj y la medición

No se fija todavía una ventana W ni una granularidad. Hacerlo antes de saber qué resultado valorativo se medirá fijaría un instrumento temporal para una variable que no ha superado la distinción de constructo.

Se conserva el reloj existente t−1/t0…t9:
- la consecuencia funcional se genera/observa después de la apertura de accesibilidad y de los estados de Reach/posibilidades relevantes;
- la valoración contextual, si se especifica, se adjudica en el punto de consecuencia/Value ya previsto en t9;
- no se crea un segundo reloj ni se equipara la profundidad transformacional H con una duración temporal.

La disponibilidad verdadera y la evidencia observada deberán permanecer separadas. Una única oportunidad estandarizada por UE no permite estimar por sí sola continuidad durante un intervalo; si se conserva una medida temporal, su evidencia requerirá una fuente de estado/telemetría con cobertura y error explícitos, independiente de la reconstrucción de `T_acc` y de O-CONF. La falta de registro no se recodificará como indisponibilidad.

### 28.4 Próxima resolución sustantiva, acotada

El siguiente cierre debe decidir si existe una regla valorativa sintética mínima y no arbitraria para la consecuencia `Q_B1`, con:
1. autoridad normativa explícita del mundo sintético desde la perspectiva de B1;
2. regla de valoración diferenciada de la medida técnica de continuidad;
3. invariancia de la regla entre DGP nulo, positivo, negativo y adversarial;
4. independencia de la regla respecto de `ΔT_acc`, Reach, O-CONF y de los resultados observados;
5. capacidad de representar que una misma continuidad pueda recibir distinta valoración por un atributo contextual estipulado, y que una continuidad distinta pueda recibir igual valoración cuando la regla así lo determine.

Si no puede formularse sin inventar preferencias, pesos o trade-offs, se declarará `VALUE_NOT_INSTANTIATED` para esta instancia y el experimento podrá probar consecuencias/Outcome, pero no afirmar que ha probado `ΔT_acc → Value`. No se sustituirá silenciosamente Value por O-CONF ni por Q_B1.

### 28.5 Reducción de alcance y estado

Esta decisión cierra la evaluación de la propuesta actual: **Q_B1 se retiene como consecuencia; V1=Q_B1 se rechaza como endpoint confirmatorio en su forma actual**. No se requiere otra auditoría de los contratos ya reconciliados.

No se fijan W, granularidad, telemetría, instrumentos ni parámetros hasta resolver el criterio de valoración. No hay autorización para implementación, generación de datos, simulación o ejecución científica.

**Estado:** CONSEQUENCE_CANDIDATE_RETAINED / CURRENT_VALUE_IDENTITY_REJECTED / VALUE_RULE_OPEN / NO_DESIGN_FREEZE / NO_IMPLEMENTATION / NO_SCIENTIFIC_EXECUTION.


## 29. Regla candidata de valoración directa del objetivo B1: Value de objetivo único (2026-11-11)

**Estado:** DIRECT_GOAL_VALUATION_PROPOSED / CONCEPTUAL_SEPARATION_CLARIFIED / VALUE_INSTANCE_NOT_YET_ACCEPTED / NOT_DESIGN_FROZEN / NOT_IMPLEMENTED / NOT_EXECUTED.

### 29.1 Corrección del criterio de separación

La distinción entre Outcome, consecuencia B1 y Value es una distinción de constructo, función y autoridad; no exige que toda instancia de Value sea una segunda magnitud numérica independiente de la consecuencia valorada.

Una regla de valoración puede asignar directamente valor al grado de cumplimiento de un objetivo basal cuando:
- el objetivo y su titular están definidos antes de la intervención;
- la autoridad normativa del mundo sintético estipula que ese objetivo es el único criterio de valoración en la instancia focal;
- la regla se fija ex ante y se mantiene invariante entre brazos y DGP;
- la consecuencia se genera y mide sin usar accesibilidad, Reach, trayectoria, Outcome adjudicado ni la salida del Analyzer como sustitutos;
- se conserva la separación de objetos y provenance entre consecuencia observada y adjudicación de Value.

Por tanto, el requisito de §28.4.5 —que una misma consecuencia pueda recibir valores distintos por un atributo contextual, y consecuencias distintas puedan recibir el mismo valor— **no es un requisito general para toda instancia de Value**. Es pertinente cuando la instancia incluye varios criterios, preferencias o trade-offs. No debe imponerse a una instancia sintética deliberadamente unidimensional, pues forzaría a introducir atributos o ponderaciones que no forman parte del objetivo B1 aceptado.

### 29.2 Regla candidata

Se reutiliza el propósito basal aceptado de B1: mantener operativa una función de servicio dependiente de la configuración migrada al entorno destino.

Se propone una instancia de **valor de objetivo único**:
- `Q_B1`: grado de continuidad/disponibilidad de la función de servicio para B1 durante el horizonte común, generado como consecuencia verdadera y medido mediante evidencia propia;
- `G_B1): objetivo basal versionado de mantener operativa esa función;
- `V_B1): valoración del grado de cumplimiento de `G_B1` desde la perspectiva de B1, conforme a la autoridad normativa estipulada en el DGP.

Si el DGP normaliza `Q_B1` como grado de cumplimiento en [0,1] y estipula que la totalidad del criterio de valoración de B1 en esta instancia es el cumplimiento de `G_B1`, la regla directa es:

```
V_B1 = v_B1(Q_B1 | G_B1) = Q_B1
```

La igualdad numérica no elimina la distinción semántica:
- `Q_B1` es la consecuencia funcional verdadera/observada;
- `V_B1` es la valoración normativa de esa consecuencia por aplicación de una regla explícita;
- `O-CONF` continúa siendo la adjudicación técnica de conformidad terminal frente a F*, no la medida de continuidad ni la valoración de B1.

La regla no añade pesos, utilidad monetaria, costes ni preferencias ficticias. La autoridad normativa del DGP estipula que, para esta instancia y solo para ella, B1 tiene un objetivo focal no compensatorio: mayor cumplimiento de la continuidad funcional es preferido a menor cumplimiento. No se afirma que esta regla describa preferencias humanas reales ni que sea una definición universal de Value.

### 29.3 Independencia y no circularidad

La regla `v_B1` queda fijada antes de asignar `g_1/g_0` y no contiene `ΔT_acc`, Reach, trayectoria, selección, ejecución, O-CONF, Z ni parámetros reveladores de truth. La regla es idéntica en todos los DGP focales.

Los DGP pueden variar la relación causal entre accesibilidad y `Q_B1`:
- efecto positivo: mayor accesibilidad produce mayor continuidad;
- efecto nulo: cambia accesibilidad, pero la continuidad no responde;
- efecto negativo: una vía generativa adversa asociada a la política de accesibilidad reduce continuidad;
- vía alternativa: una condición no atribuible a accesibilidad cambia continuidad y, por la misma regla, cambia Value;
- no identificación: soporte o medición insuficientes impiden atribuir el cambio a la intervención de accesibilidad.

Así, el efecto sobre Value no está incorporado en la definición: lo determina el mecanismo causal del DGP. La regla de valoración permanece fija mientras la verdad causal cambia.

### 29.4 Relación con la población y Need_preZ

La instancia focal debe declarar el estado basal de `Need_preZ` en su configuración antes de generar datos. Si el DGP focal restringe por construcción todas las unidades a un mismo objetivo basal B1, ello define el universo sintético de esa instancia; no autoriza a filtrar unidades según eventos post-Z ni a redefinir Need a partir de resultados.

Los estados `Need_preZ=0` y `?` no se recodifican como `V_B1=0`. Se conservan para escenarios de extensión, límites o no-instanciación cuando el objetivo focal no exista o no pueda adjudicarse. La población y el estimando de cada escenario deben declararse; no se presenta una estimación condicionada a Need=1 como ITT de una población más amplia.

### 29.5 Admisibilidad y límites

La regla directa sería admisible como **una instancia sintética de Value contextual de objetivo único**, no como operacionalización universal de Value, si la configuración del DGP contiene:
1. identidad/versionado del objetivo `G_B1` y su titular B1;
2. autoridad normativa explícita que estipula el criterio único;
3. definición de `Q_B1`, horizonte y unidad, con truth y evidencia separadas;
4. adjudicación `V_B1` mediante la regla directa, con provenance y cegamiento a la asignación cuando corresponda;
5. invariancia de la regla entre los DGP de efecto, nulo, signo contrario y adversariales;
6. demostración de que `Q_B1` no es reconstruido desde `T_acc`, Reach, O-CONF ni eventos de petición aislados.

La igualdad numérica `V_B1=Q_B1` debe declararse como una propiedad de la regla normativa del escenario, no como evidencia de que Value y Outcome sean el mismo constructo. Si el DGP no puede sostener esta estipulación de objetivo único o la medición independiente de Q, la instancia se marca `VALUE_NOT_INSTANTIATED`.

### 29.6 Dictamen y siguiente cierre

Esta propuesta resuelve la objeción conceptual sin añadir dimensiones, costes, pesos ni trade-offs arbitrarios. **No se acepta todavía como endpoint confirmatorio**, porque falta verificar contra el contrato B1 que la función concreta de servicio y su continuidad pueden instanciarse en el DGP sin inventar semántica funcional, y especificar la medición de `Q_B1` con separación de truth/evidence.

El siguiente cierre se limita a esa comprobación de compatibilidad y a declarar si la instancia de objetivo único puede aceptarse como endpoint sintético. Si es admisible, se fijarán entonces horizonte y medición. Si no, se conservará `VALUE_NOT_INSTANTIATED` y no se afirmará haber probado `ΔT_acc → Value`.

**Estado:** SINGLE_GOAL_VALUE_RULE_FORMULATED / SEMANTICALLY_NONCIRCULAR_IF_DGP_CONTRACTED / CONFIRMATORY_ADMISSIBILITY_PENDING / NO_DESIGN_FREEZE / NO_IMPLEMENTATION / NO_SCIENTIFIC_EXECUTION.
