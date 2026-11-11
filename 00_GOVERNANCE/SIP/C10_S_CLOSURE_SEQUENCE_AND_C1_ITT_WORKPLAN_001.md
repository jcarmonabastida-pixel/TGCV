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
