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


## 30. Compatibilidad de Value de objetivo único con el contrato B1: admisibilidad conceptual aceptada (2026-11-11)

**Estado:** B1_FUNCTIONAL_TARGET_COMPATIBLE / SINGLE_GOAL_VALUE_ADMISSIBLE_AS_SYNTHETIC_ENDPOINT / MEASUREMENT_MODEL_PARAMETERIZED_OPEN / NOT_DESIGN_FROZEN / NOT_IMPLEMENTED / NOT_EXECUTED.

### 30.1 Contraste con el contrato funcional aceptado

La especialización funcional B1 ya aceptada define un servicio lógico que:
- recibe solicitudes dirigidas a su instancia;
- comprueba el estado declarativo de habilitación en destino;
- puede admitir solicitudes cuando `PAR-SVC-ENABLED=true` y no las admite cuando está deshabilitado;
- expone `PAR-SVC-PROFILE`, sin atribuir semántica de negocio diferenciada a STANDARD y READ_ONLY.

Esto sí permite nombrar la función mínima que B1 pretende mantener operativa: **la disponibilidad operativa del servicio para admitir solicitudes conforme a su estado declarativo de habilitación**. No requiere inventar el contenido de la solicitud ni una operación de negocio posterior a la admisión.

La función valorada no es «tener ENABLED=true» como mero estado declarativo. Es que el servicio esté efectivamente disponible/capaz de admitir solicitudes durante el horizonte pertinente. El parámetro ENABLED es una condición contractual de configuración; no demuestra por sí solo disponibilidad operativa efectiva, admisión real, procesamiento, respuesta ni conformidad O-CONF.

### 30.2 Dictamen sobre la regla de valoración

Se acepta la regla de objetivo único de §29 como **admisible para la instancia sintética B1**, con esta precisión del objeto valorado:

- `G_B1`: mantener disponible la función de admisión de solicitudes del servicio B1 en destino;
- `Q_B1(W)`: proporción del horizonte común `W` durante la cual la función está efectivamente disponible/capaz de admitir solicitudes conforme al contrato funcional;
- `V_B1=v_B1(Q_B1mid G_B1)=Q_B1`: valoración normativa de cumplimiento del objetivo único, por estipulación ex ante del DGP.

La igualdad numérica es admisible porque la regla normativa del mundo sintético declara que el cumplimiento de este único objetivo constituye todo el criterio de valoración de B1 en esta instancia. La distinción entre consecuencia y valoración se conserva en sus definiciones, roles, provenance y adjudicación; no se exige añadir un segundo atributo numérico artificial.

Este dictamen no convierte ENABLED, una solicitud admitida, O-CONF, F*, Reach, trayectoria ni `ΔT_acc` en Value. Tampoco afirma que la regla represente preferencias humanas reales o una definición general de Value.

### 30.3 Contrato mínimo de verdad y observación de Q_B1

Para que la instancia sea evaluable en el experimento sintético:

1. **Truth:** el DGP genera el estado verdadero de disponibilidad operativa de la función de admisión a lo largo de `W`; `Q_B1(W)` se deriva de esa trayectoria de estado con una regla temporal versionada.
2. **Observed evidence:** el mecanismo de observación proyecta evidencia de disponibilidad con cobertura, error, latencia, ausencia y censura explícitos. La ausencia de registro no equivale a indisponibilidad.
3. **Independencia:** la evidencia de Q no se reconstruye desde `T_acc`, Reach, trayectoria, asignación, O-CONF, estado declarativo ENABLED aislado ni desde el éxito de una única petición.
4. **Separación:** O-CONF continúa adjudicando conformidad funcional terminal; Q mide disponibilidad efectiva durante W; V aplica la regla normativa de objetivo único a Q.
5. **Cegamiento y firewall:** Analyzer recibe solo evidencia observada y contratos/versiones permitidos; no recibe truth, potenciales ni parámetros secretos. Evaluator adjudica después del sellado.
6. **Simetría:** definición, regla de valoración y mecanismo de medición se fijan antes de asignar las políticas y se mantienen invariantes entre brazos y DGP, salvo que un escenario adversarial declare explícitamente error diferencial como mecanismo de prueba.

El harness puede generar la trayectoria verdadera y su evidencia observada sintética sin materializar fuentes reales ni ejecutar probes de negocio adicionales. La forma concreta del proyector de observación y sus parámetros será una configuración versionada del experimento, no una nueva dimensión de Value ni un nuevo contrato conceptual.

### 30.4 Qué queda cerrado y qué no

**Cerrado en el nivel conceptual de esta instancia:**
- función basal B1 nombrada a partir del contrato funcional aceptado;
- objetivo `G_B1` compatible con el contrato de admisión;
- regla normativa de objetivo único `V_B1=Q_B1(W)`;
- separación conceptual entre configuración declarativa, disponibilidad operativa, admisión puntual, O-CONF, consecuencia y valoración;
- independencia lógica de la regla respecto de la hipótesis causal y posibilidad de DGP positivo, nulo, negativo y adversarial.

**Permanece como parametrización necesaria del DGP/medición, no como bloqueo de la regla de Value:**
- duración y discretización de `W`;
- unidad temporal y regla exacta de cálculo de Q;
- modelo de observación, cobertura, error, latencia, missingness y censura;
- parámetros de DGP y criterios de precisión/sensibilidad;
- configuración de población/soporte y versiones concretas de las políticas `g_1/g_0`.

Estos parámetros deben declararse explícitamente antes de generar resultados. No reciben defaults ni se fijan retrospectivamente. Si una configuración no aporta lo necesario para generar truth y observed evidence válidas, el resultado de esa corrida será `NOT_INSTANTIATED`/`INDETERMINATE`, no una imputación arbitraria.

### 30.5 Dictamen final de este cierre

**Se acepta `V_B1` como endpoint sintético contextual de objetivo único para el experimento C10-S**, sujeto a la configuración explícita del horizonte y del modelo de observación descritos arriba. Esto cierra la objeción conceptual de Value para esta instancia y permite continuar con el cierre del DGP/estimando y la especificación parametrizada de la medición.

No equivale a:
- operacionalización universal de Value en TGCV;
- selección de un índice agregado P179;
- operacionalización de Outcome O-CONF;
- identificación causal demostrada de `ΔT_acc → Value`;
- Design Freeze, implementación, generación de datos, simulación o ejecución científica.

No se requiere otra iteración para volver a decidir si la regla directa de objetivo único es conceptualmente admisible. Las tareas pendientes son de parametrización y contrato de medición dentro del diseño experimental ya acordado.

**Estado:** VALUE_ENDPOINT_ACCEPTED_FOR_SYNTHETIC_B1 / VALUE_RULE_CONCEPTUALLY_CLOSED / Q_MEASUREMENT_CONFIGURATION_OPEN / NO_DESIGN_FREEZE / NO_IMPLEMENTATION / NO_SCIENTIFIC_EXECUTION.


## 31. Contrato temporal y de medición de Q_B1: regla de intervalo y separación de evidencia (2026-11-11)

**Estado:** Q_TEMPORAL_MEASURE_DEFINED_AT_CONTRACT_LEVEL / HORIZON_AND_OBSERVATION_PARAMETERS_OPEN / P179_SINGLE_DIMENSION_INSTANCE_JUSTIFIED / NOT_DESIGN_FROZEN / NOT_IMPLEMENTED / NOT_EXECUTED.

### 31.1 Reloj y horizonte

Se conserva sin cambios el reloj del estudio `t−1/t0…t9`. Sus índices identifican fases y precedencias, no unidades de duración. `H=3` sigue siendo profundidad transformacional candidata, no horizonte temporal de Value.

Para esta instancia, `W_B1` es un intervalo de evaluación funcional común a todas las UE y brazos:
- comienza después de que se haya sellado el snapshot estructural postintervención y calculado Reach (`t3/t4));
- termina antes de la adjudicación de Value (`t9));
- tiene duración, origen exacto, discretización y regla de inclusión de límites declarados en la configuración versionada del escenario;
- es idéntico entre brazos y escenarios comparables, salvo que un DGP adversarial declare expresamente una diferencia temporal como mecanismo causal que se desea probar.

Los eventos de solicitud, selección, inicio y ejecución conservan sus propios timestamps/subledgers. No definen por sí mismos los límites de `W_B1` ni convierten `t5`, `t6` o `t7` en una duración. La duración y discretización concretas no se fijan aquí porque no existe una unidad temporal sustantiva aceptada en el contrato funcional; serán parámetros obligatorios de cada configuración, sin defaults silenciosos. Una configuración sin ellos es inválida para generar `Q_B1`.

### 31.2 Truth de disponibilidad y cálculo de Q

Para cada UE y cada instante/slot de `W_B1`, el DGP genera una variable verdadera:

```
A_B1*(u,t) ∈ {0,1}
```

Su significado es: la instancia lógica del servicio está efectivamente disponible y es capaz de admitir una solicitud válida conforme al contrato funcional vigente en ese instante. No basta con que `PAR-SVC-ENABLED=true`; el estado verdadero debe representar capacidad operativa efectiva de admisión.

Con una partición temporal versionada en K intervalos de igual duración, la consecuencia se define como:

```
Q_B1*(W) = (1/K) · Σ[k=1..K] A_B1*(u,k)
```

Para una representación temporal continua, la misma regla corresponde a la fracción de duración del intervalo en que `A_B1*(u,t)=1`. El DGP debe elegir y versionar una de las dos representaciones; no puede mezclar discretización desigual con promedio simple. `Q_B1*` pertenece a [0,1] y expresa fracción de tiempo disponible, no número de solicitudes admitidas, tasa de respuestas, éxito técnico de una petición ni conformidad terminal.

La regla de valoración aceptada se aplica después:

```
V_B1*(u) = v_B1(Q_B1*(W) | G_B1) = Q_B1*(W)
```

La función generadora de `A_B1*` puede depender causalmente de accesibilidad, vías alternativas, condiciones externas y mecanismos colaterales definidos en cada DGP. La fórmula de Q y la regla de Value no dependen de esas causas y permanecen invariantes entre escenarios.

### 31.3 Evidencia observada de Q

La evidencia observada debe proceder de un canal de observación temporal del estado operativo, separado de:
- `T_acc`, `ΔT_acc`, Reach y trayectorias;
- configuración declarativa `PAR-SVC-ENABLED/PROFILE` considerada aisladamente;
- la oportunidad estandarizada única y sus eventos attempt/received/admitted/processing/response;
- F*, O-CONF, selección y ejecución.

El proyector de observación genera registros de estado con timestamp, unidad/servicio/versionado, cobertura del intervalo, procedencia y estado observado. Su contrato parametrizado debe declarar:
- frecuencia o regla de muestreo y latencia;
- sensibilidad y especificidad (o modelo de error equivalente);
- cobertura temporal y mecanismo de pérdida de registros;
- missingness/censura y recuperabilidad;
- reglas para estados contradictorios, intervalos no observados y cambios de versión.

La evidencia observada no se convierte automáticamente en `A_B1*`. El Analyzer calcula una medida observada o un conjunto/intervalo compatible con la evidencia y debe abstenerse o declarar identificación parcial cuando la cobertura/error no sostengan una estimación puntual. La ausencia de registro no equivale a indisponibilidad. El Evaluator, después del sellado, compara la salida con `Q_B1*` reservado.

El canal de observación debe ser no intrusivo respecto del servicio y no puede modificar su disponibilidad ni generar la oportunidad de negocio evaluada. Si el DGP modela un canal intrusivo, su efecto se declara como intervención/medición adicional y no se oculta dentro del error instrumental.

### 31.4 Separación respecto de Outcome y O-CONF

Se fijan tres objetos distintos:
- **Outcome de petición:** resultado técnico de la oportunidad estandarizada única, si se operacionaliza mediante su ficha propia; es puntual y no estima continuidad.
- **O-CONF:** adjudicación técnica terminal de conformidad frente a F*; no mide disponibilidad durante `W_B1`.
- **Q_B1:** consecuencia funcional temporal para B1, calculada a partir de la trayectoria de disponibilidad efectiva durante `W_B1`; es el objeto al que se aplica la regla normativa de Value.

No se declara operacionalizado un Outcome confirmatorio ni O-CONF por esta especificación. Si un Outcome futuro reutiliza la misma serie temporal de disponibilidad para medir continuidad, deberá justificarse la separabilidad exigida por §224 y B2–B3; no se admitirá duplicar la misma medida bajo dos etiquetas como si fueran endpoints independientes. La oportunidad única no sustituye la serie temporal.

### 31.5 P179 y alcance de la instancia

P179 conserva Value vectorial durante la identificación general de TGCV. La presente instancia sintética es deliberadamente unidimensional (`k=1)) porque el objetivo B1 aceptado se restringe explícitamente a mantener disponible la función de admisión del servicio y el DGP estipula que ese es el único criterio normativo considerado. Esta reducción se limita a este microdominio/escenario; no elimina trade-offs potenciales de otros beneficiarios, objetivos o dominios, ni autoriza agregar dimensiones en una medida global. Si el DGP introduce otra consecuencia valorada o un criterio en conflicto, deberá representar una dimensión adicional y preservar el vector, o declarar que la instancia de objetivo único ya no es adecuada. No se asignan pesos ni se compensa una dimensión con otra.

### 31.6 Parámetros obligatorios y criterio de validez

Antes de generar una corrida, la configuración versionada deberá proporcionar: duración y límites de `W_B1`; unidad temporal y partición o representación continua; regla de generación de `A_B1*`; versión del contrato del servicio; modelo de observación y sus parámetros; tratamiento de cobertura, missingness y censura; y regla de cálculo/adjudicación de `Q_B1`/`V_B1`.

La falta de cualquiera de estos elementos produce configuración inválida o resultado `NOT_INSTANTIATED/INDETERMINATE`, según la fase; nunca se rellena con un valor implícito. Los parámetros numéricos se justifican y fijan antes de inspeccionar resultados, y se someten a sensibilidad cuando proceda. No se crean ahora valores de K, duración, frecuencia, error, cobertura, N, repeticiones ni umbrales.

**Dictamen:** queda definida la estructura temporal y matemática de la medida de consecuencia y su canal de observación. La elección numérica de horizonte y parámetros de observación pertenece a la configuración experimental versionada, no requiere reabrir el significado de Value ni crear otro paquete conceptual. La instancia de `V_B1` sigue aceptada como endpoint sintético de objetivo único, condicionada a que cada configuración cumpla este contrato.

**Estado:** Q_B1_MEASUREMENT_CONTRACT_DEFINED / VALUE_RULE_CLOSED_FOR_B1_INSTANCE / SCENARIO_PARAMETERS_REQUIRED_BEFORE_GENERATION / NO_DESIGN_FREEZE / NO_IMPLEMENTATION / NO_SCIENTIFIC_EXECUTION.


## 32. Reconciliación crítica: disponibilidad técnica Q_B1 y consecuencia experimentada por B1 (2026-11-11)

**Estado:** Q_B1_TECHNICAL_AVAILABILITY_MEASURE_DEFINED / BENEFICIARY_CONSEQUENCE_BRIDGE_NOT_ESTABLISHED / VALUE_ENDPOINT_ADMISSIBILITY_CONDITIONAL / NO_DESIGN_FREEZE / NOT_IMPLEMENTED / NOT_EXECUTED.

### 32.1 Discrepancia identificada

La §31 define de forma útil y no circular respecto de accesibilidad la trayectoria verdadera de disponibilidad efectiva del servicio y su medida temporal:

`A_B1^*(u,t)` y `Q_B1^*(W)`.

Sin embargo, esa definición describe primariamente una propiedad funcional/operativa del servicio: que su instancia esté disponible y sea capaz de admitir solicitudes válidas. No demuestra por sí sola que `Q_B1` mida una consecuencia experimentada por la entidad beneficiaria B1. La atribución de la perspectiva B1 y la regla `V_B1=Q_B1` no resuelven esta diferencia semántica mediante renombrado.

B2–B3 exige que Outcome técnico, consecuencia de B1 y Value permanezcan diferenciados; admite compartir fuentes solo si la separabilidad conceptual y operacional queda justificada. La ficha histórica de B1 también distingue la disponibilidad/capacidad del servicio, la petición puntual, el resultado técnico y el cambio en la situación de B1 respecto de Need_preZ.

Por tanto, la §30 debe leerse con el límite siguiente: aceptó la regla normativa de objetivo único como forma posible de valoración, pero no basta para probar que el objeto actualmente medido por Q sea ya una consecuencia de B1. La §31 cierra la medición de disponibilidad técnica, no automáticamente el puente beneficiario→consecuencia.

### 32.2 Qué queda conservado

No se reabre ni se descarta:
- el propósito basal B1 previamente aceptado;
- la regla normativa de objetivo único como candidata admisible;
- la definición temporal y matemática de disponibilidad de §31;
- la separación entre verdad, evidencia observada y evaluación;
- la independencia de la medida respecto de `T_acc`, Reach, trayectoria, O-CONF y la petición puntual.

`Q_B1` queda conservada como medida de disponibilidad funcional del servicio. Puede ser antecedente o componente de una consecuencia para B1, pero no se etiquetará como consecuencia beneficiaria confirmatoria sin el mapping justificativo.

### 32.3 Criterio mínimo para resolver el puente sin ampliar el microdominio

Solo hay dos resultados admisibles:

1. **Puente defendible:** demostrar, a partir del propósito B1 ya aceptado y sin inventar una operación de negocio, que la disponibilidad medida representa directamente una capacidad/condición de servicio que constituye la consecuencia para B1; especificar la relación B1↔servicio y por qué esa condición es el objeto de interés de B1, distinguiéndola de una mera propiedad técnica del proveedor. Debe poder observarse/adjudicarse sin reconstruirla desde accesibilidad, Reach, O-CONF o el éxito de la oportunidad estandarizada. Si el mapping requiere un indicador distinto, debe definirse y justificarse, no presumirse.

2. **Puente no defendible con el contrato disponible:** conservar `Q_B1` como medida técnica/funcional y declarar `VALUE_NOT_INSTANTIATED` para esta instancia. El experimento podrá probar efectos sobre accesibilidad y resultados/medidas técnicas que estén operacionalizados, pero no afirmará haber probado `ΔT_acc → Value`.

No se introducirán solicitudes naturales, tasas de demanda, satisfacción, utilidad, costes, pesos ni dimensiones nuevas para forzar el primer resultado. La oportunidad estandarizada única no se convierte en medida de continuidad ni de consecuencia.

### 32.4 Dictamen de cierre y siguiente operación

La regla normativa `v_B1` no necesita otra discusión abstracta. La única cuestión abierta es si el objeto de §31 puede justificarse como consecuencia de B1 bajo B2–B3. Esta comprobación debe resolverse usando los contratos existentes, no mediante otra matriz ni auditoría general.

**Siguiente operación activa:** emitir un dictamen binario y trazable sobre el mapping `Q_B1 → consequence_B1`. Si es defendible, incorporar la justificación mínima al contrato integrado del DGP y pasar a parametrizar W/modelo de observación. Si no lo es, declarar `VALUE_NOT_INSTANTIATED` para B1 y continuar el experimento sin atribución a Value. No se abre una cadena adicional de subpaquetes.

No se autoriza implementación, generación de datos, simulación ni ejecución científica.



## 33. Dictamen del puente Q_B1 → consecuencia B1: defendible con frontera funcional explícita (2026-11-11)

**Estado:** BENEFICIARY_CONSEQUENCE_BRIDGE_DEFENDED_FOR_SYNTHETIC_B1 / Q_B1_ADMISSIBLE_AS_SINGLE_GOAL_CONSEQUENCE_MEASURE / VALUE_RULE_CONSISTENT / SCENARIO_PARAMETERS_OPEN / NO_DESIGN_FREEZE / NOT_IMPLEMENTED / NOT_EXECUTED.

### 33.1 Reconstrucción determinante

La revisión de la fuente histórica B1 permite resolver la cuestión planteada en §32 sin introducir una operación de negocio adicional. La §14.3 de `C10_S_B1_VALUATION_CASE_RECONCILIATION_DRAFT_001.md` establece expresamente que la consecuencia basal para B1 puede referirse a la **disponibilidad de la capacidad de admisión** que constituye su objetivo, y advierte que no debe confundirse una admisión puntual con el mantenimiento efectivo de la función ni con el logro completo del propósito.

La §14.1 define la función mínima de trabajo: una instancia lógica de servicio recibe solicitudes por o en representación de B1, comprueba la habilitación declarada en destino y puede admitirlas cuando `PAR-SVC-ENABLED=true`; expone el perfil declarado. La §14.2 mantiene separados admisión, procesamiento, respuesta, O-CONF/F*, consecuencia B1 y Value.

La ficha B1 de adjudicación pre-Z, §6, define la consecuencia inmediata como el cambio post-Z en la situación de B1 respecto de su objetivo basal: si puede contar con la función de servicio que pretende mantener disponible. Incluye disponibilidad funcional y continuidad entre las clases de consecuencia, sin convertirlas automáticamente en dimensiones o índices.

Por tanto, la relación no se infiere solo del nombre del servicio ni de la perspectiva asignada al evaluador: está respaldada por el propósito basal aceptado, la relación B1↔instancia lógica de servicio por UE y la especialización funcional mínima aceptada.

### 33.2 Correspondencia admisible y límite

Se acepta el siguiente mapping para esta instancia sintética de objetivo único:

- `A_B1^*(u,t)`: estado verdadero de disponibilidad efectiva de la capacidad de admisión del servicio en el entorno de destino.
- `Q_B1^*(W)`: fracción del horizonte común durante la que B1 puede contar con esa capacidad funcional disponible.
- `consequence_B1^*(W)`: grado de mantenimiento/disponibilidad de la función que constituye el objetivo basal de B1, representado por `Q_B1^*(W)`.
- `V_B1^*(W)=v_B1(Q_B1^*(W)\mid G_B1)=Q_B1^*(W)`: valoración estipulada del cumplimiento del objetivo único.

La identidad numérica entre consecuencia y Value es admisible en este DGP porque la regla normativa sintética declara que el único criterio valorativo considerado es el cumplimiento temporal del objetivo de disponibilidad funcional. La consecuencia conserva su interpretación descriptiva/funcional; Value es su valoración bajo esa regla. No se afirma que sean constructos universalmente idénticos ni se modifica P179.

Este mapping **no** afirma que B1 haya formulado una solicitud natural, que una solicitud concreta haya sido admitida, procesada o respondida, que se haya satisfecho una necesidad de negocio posterior, que O-CONF sea conforme, ni que el beneficiario haya experimentado satisfacción/utilidad humana. Es una instancia sintética de beneficiario y objetivo funcional, no una afirmación empírica sobre usuarios reales.

### 33.3 Condiciones de validez conservadas de §31

La admisibilidad del endpoint queda condicionada a cumplir íntegramente §31:
- horizonte común y duración/discretización explícitos;
- truth temporal de disponibilidad generada sin derivarla de `T_acc`, Reach, ejecución u O-CONF;
- canal de observación independiente, con cobertura, error, latencia, missingness y censura declarados;
- no equivalencia entre ENABLED declarativo y disponibilidad efectiva;
- no equivalencia entre probe puntual y continuidad;
- separación truth_dgp / observed_evidence / evaluation;
- regla normativa invariante entre DGP positivo, nulo, negativo y adversarial.

Si el escenario introduce procesamiento posterior, respuesta, satisfacción, demora, recuperación, riesgo u otra consecuencia distinta, `Q_B1` no la representa por sí sola. Esa extensión exigiría otra consecuencia/dimensión justificada; no se incorpora al núcleo mínimo actual.

### 33.4 Corrección de precedencia respecto de §32

El dictamen provisional de §32, `BENEFICIARY_CONSEQUENCE_BRIDGE_NOT_ESTABLISHED`, queda **SUPERSEDED** por esta reconstrucción histórica y el dictamen de §33. Se conserva §32 como registro de la objeción y del control de no circularidad que motivaron la comprobación; no constituye ya el estado vigente.

No se requiere una nueva decisión del usuario para reabrir el significado de Value: el puente se deriva de contratos de trabajo previamente aceptados. Tampoco se reabre la regla normativa de §30 ni la medida temporal de §31.

### 33.5 Siguiente cierre operativo

El endpoint sintético B1 queda semánticamente admisible. La siguiente operación es cerrar, en una sola especificación de escenario, los parámetros obligatorios de §31 y su justificación: horizonte/duración y discretización, proceso generador de disponibilidad, canal/modelo de observación, cobertura/error/missingness/censura y criterios de precisión/sensibilidad. No se fijan valores numéricos sin justificación y no se amplía el conjunto de consecuencias.

Después se integra `V_B1` en los escenarios de recuperación, nulo, vías alternativas/adversariales y no-identificación para evaluar si el Analyzer recupera o limita el efecto causal previsto. Esto no autoriza implementación, generación de datos, simulación ni ejecución científica.



## 34. Especificación integrada del DGP temporal de disponibilidad y medición de Q_B1 (2026-11-11)

**Estado:** TEMPORAL_DGP_FAMILY_SPECIFIED / IDEAL_MEASUREMENT_REFERENCE_SPECIFIED / ROBUSTNESS_MEASUREMENT_DESIGN_SPECIFIED / NUMERIC_CALIBRATION_PENDING / NOT_DESIGN_FROZEN / NOT_IMPLEMENTED / NOT_EXECUTED.

### 34.1 Horizonte común sin introducir tiempo sustantivo ficticio

Se adopta una representación discreta normalizada del horizonte:
- `W_B1=[0,1]` como escala interna adimensional del intervalo, no como una unidad de tiempo real.
- `K` slots consecutivos de igual duración, con `K` explícito y común a todas las UE y brazos dentro de una configuración.
- `A_B1^*(u,k)` se evalúa una vez por slot y `Q_B1^*(u)=K^{-1}\sum_{k=1}^{K}A_B1^*(u,k)`.
- El origen operativo de W es posterior al snapshot estructural y al cálculo de Reach (t3/t4); su cierre precede a la adjudicación de t9. Los timestamps de eventos siguen siendo propios y no determinan por sí mismos la escala normalizada.

Esta normalización permite especificar continuidad sin inventar minutos, horas o días que el contrato no proporciona. K no se fija por analogía con H=3 ni por conveniencia computacional. La selección de K debe cumplir una prueba de convergencia de discretización: aumentar la resolución no debe cambiar materialmente el valor verdadero de Q ni la clasificación del estimando más allá de la tolerancia numérica/Monte Carlo preregistrada. La tolerancia y la regla de selección de K se registran antes de generar corridas confirmatorias. No se mezclan slots desiguales con promedio simple.

### 34.2 Proceso generador de disponibilidad verdadera

El núcleo temporal utiliza un proceso binario de dos estados con dependencia temporal de primer orden (Markov de primer orden), explícito y falsable:
- estado 1: capacidad funcional efectiva de admisión disponible;
- estado 0: capacidad no disponible;
- estado inicial generado desde una distribución basal común, independiente de la asignación futura salvo que un DGP adversarial declare y parametrice expresamente otra vía.

Para cada slot posterior, el DGP genera transición `A_{k-1}→A_k` mediante dos probabilidades distintas:
- `p_01(k)=P(A_k=1 | A_{k-1}=0, H_k)`: recuperación/disponibilidad tras estado no disponible;
- `p_10(k)=P(A_k=0 | A_{k-1}=1, H_k)`: interrupción desde estado disponible.

`H_k` contiene exclusivamente covariables basales, shocks exógenos versionados, régimen de política asignado y la exposición focal definida en el DGP. El enlace de accesibilidad se especifica en términos de `ΔT_acc^*` medido independientemente; no se deriva A de Reach, trayectoria, ejecución, O-CONF, petición ni Value.

La familia funcional (p. ej., enlace logístico para p_01 y p_10) y sus coeficientes se parametrizan/versionan. El signo y magnitud de la contribución focal no se fijan como verdad universal: se configuran por escenario y el DGP reserva explícitamente coeficientes nulos, positivos y negativos. El proceso permite persistencia, interrupciones y recuperación sin equiparar una disponibilidad instantánea con continuidad del horizonte.

### 34.3 DGP mínimos para la prueba causal

Se reutilizan los escenarios de §26 y la arquitectura de mecanismos existente; no se crean familias paralelas:

1. **Focal no nulo:** políticas estocásticas versionadas `g1/g0` inducen distribuciones distintas de `ΔT_acc^*`; el mecanismo de disponibilidad depende de esa exposición bajo régimen externo común `q`; no hay vía directa diferencial desde la política a Q/Value. Se evalúa `θ_A(q;V_B1)=E[V_B1^{g1,q}]-E[V_B1^{g0,q}]`.
2. **Nulo:** las políticas pueden cambiar `ΔT_acc^*`, pero los coeficientes focales del proceso de disponibilidad son cero; `θ_A=0`. Es el control de falsos positivos.
3. **Vía directa/colateral:** se activa un mecanismo adicional de política/entorno que afecta disponibilidad o sus shocks sin pasar por la exposición focal. El contraste de política ya no se atribuye íntegramente a accesibilidad; el Analyzer debe detectar la violación, identificar solo bajo un estimando/ajuste justificable o abstenerse.
4. **No-identificación/soporte:** se configuran falta de positividad/solapamiento, exposición no observada o confusión no resuelta. El resultado correcto es parcial/no identificado, no una estimación causal forzada.

El DGP puede incluir heterogeneidad e interacciones como extensiones de estrés; no son requisitos para que el núcleo de cuatro escenarios exista. La verdad potencial de Q/Value se genera para los regímenes necesarios y se mantiene reservada en `truth_dgp`.

### 34.4 Canal de observación: referencia ideal y extensiones de estrés

La medición se separa en dos niveles para distinguir validez causal de degradación epistémica:

**Referencia ideal (primera prueba de recuperación):**
- cobertura temporal completa;
- observación sincronizada con los K slots;
- sensibilidad y especificidad iguales a 1;
- sin missingness ni censura;
- el canal no altera el estado del servicio.

Esta referencia no se presenta como supuesto realista ni como resultado empírico: es el control de referencia necesario para comprobar si el Analyzer recupera la verdad causal cuando la evidencia mide correctamente el objeto.

**Extensiones de medición (pruebas de robustez):**
- error de clasificación (sensibilidad/especificidad);
- cobertura incompleta y muestreo menos frecuente;
- latencia de registro;
- missingness MCAR, MAR y MNAR en escenarios diferenciados;
- censura temporal y pérdida de tramos;
- error diferencial por brazo/exposición como escenario adversarial.

Cada extensión declara su mecanismo generador, parámetros y si son conocidos por el Analyzer, estimables a partir de evidencia independiente o deliberadamente desconocidos. El Analyzer no recibe truth ni parámetros secretos. La ausencia de registro nunca se recodifica automáticamente como A=0. Si la cobertura/error no permiten recuperar Q puntualmente, debe producir intervalo compatible, identificación parcial o abstención.

### 34.5 Selección de parámetros, N y réplicas sin cifras arbitrarias

No se heredan como defaults los valores históricos ilustrativos (incluidos `.20/.80`, `N=2.000` o `R=1.000`). Tampoco se asignan valores numéricos por intuición.

La configuración numérica se obtiene mediante un procedimiento ex ante, versionado y reproducible:
1. definir el conjunto de mecanismos y rangos admisibles para transiciones, efecto focal, shocks, heterogeneidad y medición;
2. justificar el efecto mínimo relevante `δ_min` como umbral de recuperación del método, distinguiéndolo del valor verdadero de cada DGP;
3. seleccionar K mediante convergencia de discretización de Q y del estimando;
4. seleccionar N y número de réplicas R mediante error Monte Carlo, precisión de sesgo/RMSE/cobertura, error tipo I y potencia/clasificación, considerando clústeres si existe interferencia;
5. seleccionar niveles de error/cobertura/missingness mediante un rango de estrés explícito y justificar los puntos de evaluación;
6. preregistrar tolerancias, criterios de recuperación, abstención y clasificación antes de consultar resultados de las corridas confirmatorias.

Los valores finales deben ser concretos, versionados y cerrados antes de la ejecución confirmatoria. La configuración es inválida si omite cualquiera de esos parámetros o criterios. Un resultado no significativo no demuestra equivalencia ni ausencia de efecto; baja precisión no refuta la hipótesis.

### 34.6 Observación, análisis y evaluación

El Generator produce `A_B1^*`, `Q_B1^*`, `V_B1^*`, regímenes, potenciales y truth reservada. El proyector produce exclusivamente la evidencia observada según el canal configurado. El Analyzer recibe evidencia, políticas asignadas y variables permitidas, pero no verdad, potenciales ni semillas secretas. El Sealer sella su salida. Solo entonces el Evaluator contrasta estimaciones, intervalos, clasificación y abstención con truth.

Las métricas mínimas de evaluación incluyen sesgo, RMSE, cobertura de intervalos, error tipo I en el nulo, potencia/clasificación del efecto no nulo, detección de vías alternativas, tasa de abstención apropiada y falsos reclamos de identificación en escenarios no identificados. La evaluación de recuperación de `θ_A` se informa separada de ITT total de asignación y de cualquier estimando de mediación.

### 34.7 Dictamen y límite de cierre

Queda especificada la familia temporal generadora, la regla normalizada de horizonte, el canal ideal de referencia, las clases de degradación de observación y el procedimiento de calibración numérica. **No queda aprobada todavía una configuración numérica ejecutable ni se declara el experimento implementable/frozen.** El siguiente y único cierre de diseño es completar el registro de calibración con valores concretos y sus justificaciones a partir de los criterios de esta sección, integrándolo en la configuración del experimento; no se reabre el significado de B1, Q ni Value.

No se autoriza implementación, generación de datos, simulación, estimación ni ejecución científica. `scientific_execution=false`; `execution_authorized=false`.



## 35. Reconciliación de la calibración cuantitativa: verdad analítica del DGP y búsqueda posterior de precisión (2026-11-11)

**Estado:** CALIBRATION_ROUTE_RECONCILED / ANALYTIC_DGP_ORACLE_SPECIFIED_FOR_HOMOGENEOUS_REFERENCE / NUMERIC_CONFIRMATORY_CALIBRATION_NOT_RUN / NOT_DESIGN_FROZEN / NOT_IMPLEMENTED / NOT_EXECUTED.

### 35.1 Reutilización obligatoria de P178 y corrección de precedencia

No se crea un registro de calibración paralelo. Se reutiliza el procedimiento ya establecido en C10_S_PD_DGP_MECHANISM_AND_ADVERSARIAL_EVALUATION_RECONCILIATION_DRAFT_001.md §7 y P178-SIM-01…10: búsqueda de N por potencia/precisión para cada estimando reportable; ajuste por clúster/ICC cuando proceda; selección de R por error Monte Carlo; semillas jerárquicas y hashes; métricas de sesgo, RMSE, cobertura, error tipo I, potencia, calibración, convergencia, réplicas inválidas y clasificación de identificación.

La resolución de Value B1 en §33 supersede específicamente el bloqueo histórico de PD §8 que decía que Value no estaba instanciado por PA. No supersede los bloqueos independientes de Outcome técnico, mapping material D2, cumplimiento/recepción, provisión de fondo, soporte, interferencia, versiones ni exclusión. Esos límites deben reflejarse en el alcance del estimando y en los escenarios, no reabrir la semántica de Value.

### 35.2 Oráculo analítico para el DGP temporal de referencia

Para evitar que la verdad del endpoint dependa de una simulación opaca, el DGP de referencia homogéneo usa probabilidades de transición constantes dentro de cada régimen/política y slot:

- p01(d,g,q)=P(A_k=1 | A_(k-1)=0,d,g,q);
- p10(d,g,q)=P(A_k=0 | A_(k-1)=1,d,g,q),

donde d representa el objeto estructural completo ΔT_acc* (sus componentes y relaciones tipadas), o una firma íntegra de ese objeto en el soporte finito del DGP; no es un score escalar ni una reducción cardinal arbitraria. La política g induce una distribución sobre firmas factibles de ΔT_acc* y q mantiene constantes las condiciones externas comunes. Los parámetros pertenecen a [0,1], con restricciones declaradas para evitar combinaciones degeneradas no contempladas. La distribución inicial π_0=P(A_0=1) es explícita y común entre brazos en el DGP focal.

La probabilidad de disponibilidad se obtiene recursivamente, sin Monte Carlo:

π_k(d,g,q) = p01(d,g,q) + [1-p01(d,g,q)-p10(d,g,q)]·π_(k-1)(d,g,q).

Para K slots de igual duración, la esperanza exacta de la consecuencia/Value es:

μ_Q(d,g,q;K) = (1/K)·Σ[k=1..K] π_k(d,g,q),

con convención temporal de inclusión del estado inicial declarada una sola vez en la configuración (no se alterna entre escenarios). Si la política induce una distribución de accesibilidad P_g(d|q), entonces:

E[V_B1^(q,g)] = Σ_d μ_Q(d,g,q;K)·P_g(d|q)

para soporte discreto finito, o su integral equivalente para soporte continuo. Por tanto, la verdad del estimando primario es calculable analíticamente:

θ_A(q;V_B1) = E[V_B1^(q,g1)] - E[V_B1^(q,g0)].

El Generator conserva además las trayectorias individuales y potenciales para la evaluación posterior; el oráculo analítico no se entrega al Analyzer. La igualdad entre verdad analítica y esperanza Monte Carlo del generador se convierte en una comprobación de consistencia del harness, no en una estimación causal adicional.

### 35.3 Contraste focal, nulo y vías alternativas

- **Focal:** g1/g0 difieren en la distribución de d=ΔT_acc* dentro del soporte común; los parámetros p01/p10 dependen de d, y no existe otra vía diferencial desde g a A/Q/V. El contraste de política identifica el efecto de esas políticas factibles mediado por la diferencia de accesibilidad en este DGP aislado. No se interpreta como efecto universal por unidad de ΔT_acc.
- **Nulo:** g1/g0 pueden inducir distribuciones distintas de d, pero p01/p10 son invariantes a d; la verdad de θ_A es cero.
- **Vía directa/colateral:** se introduce un término separado de política/entorno en las transiciones o en los shocks. La diferencia entre políticas deja de ser atribuible exclusivamente a d; el resultado exigido es detección, estimando alternativo explícito o abstención.
- **No-identificación:** se altera soporte, observación de d o confusión de forma que el contraste no se identifica a partir de observed_evidence. La verdad sigue conocida para Evaluator, pero Analyzer debe devolver parcial/no identificado.

El signo negativo se obtiene invirtiendo el orden causal de las transiciones bajo d o haciendo que mayor accesibilidad incremente interrupción/reduzca recuperación en el DGP; no se presupone monotonicidad favorable.

### 35.4 Calibración paramétrica sin números arbitrarios

No se aprueba una combinación numérica única por intuición. La configuración se expresa mediante una cuadrícula versionada de: distribución basal π_0; probabilidades de transición de referencia; contraste de distribuciones de d inducidas por g0/g1; coeficientes de efecto de d sobre p01 y p10; magnitudes separadas de vías directas/colaterales; y parámetros del canal de observación.

La cuadrícula debe cubrir el caso nulo y ambos signos, además de niveles crecientes de magnitud dentro del rango factible de V∈[0,1]. Se eliminan por construcción combinaciones que produzcan probabilidades fuera de [0,1], falta de soporte inadvertida o efectos no distinguibles por la resolución K. Para cada punto, θ_A se obtiene primero con el oráculo analítico. El umbral δ_min no se define como un efecto verdadero conveniente: se justifica como mínimo de recuperación que el Analyzer debe distinguir con la precisión objetivo, y se informa como parámetro de rendimiento del método, no como propiedad de TGCV.

Solo después se aplica P178 para seleccionar N y R. N se busca por estimando y diseño de asignación; R se elige para que el error Monte Carlo de las métricas de evaluación quede por debajo de tolerancias preregistradas. La potencia, cobertura y error tipo I se calculan para el estimando focal; detección de colaterales y abstención se evalúan por separado. Si no existe un N/R factible que satisfaga criterios, se informa el límite de precisión/coste y no se rebajan los criterios tras observar resultados.

### 35.5 Alcance de la referencia homogénea y extensiones

La referencia homogénea sirve para verificar primero el oráculo y la recuperación en un DGP transparente. No sustituye las extensiones ya exigidas en §34: heterogeneidad, covariables temporales, shocks comunes/individuales, errores diferenciales, missingness, censura e interferencia. Estas extensiones se añaden después de demostrar la referencia y se mantienen como escenarios separados para identificar qué complejidad causa la pérdida de recuperación.

La configuración de referencia no fija el microdominio de migración ni sustituye el DGP estructural de accesibilidad/Reach. La distribución de d debe proceder de las políticas factibles y del generador estructural de T_acc; no se genera d directamente desde Value ni se construye accesibilidad desde la trayectoria de disponibilidad.

### 35.6 Dictamen y siguiente operación autorizable

Se cierra el método para obtener la verdad cuantitativa y calibrar el experimento sin escoger cifras arbitrarias: oráculo analítico primero, cuadrícula causal después, y P178 para N/R/precisión. No se han elegido aún puntos numéricos confirmatorios ni se ha ejecutado la búsqueda de potencia/Monte Carlo. Esas elecciones requieren un protocolo de calibración con criterios ex ante y autorización específica para la operación computacional de calibración; no equivalen a autorizar el experimento confirmatorio.

El siguiente cierre de diseño consiste en fijar el conjunto mínimo de parámetros libres y restricciones de la cuadrícula para la referencia homogénea, reutilizando los parámetros tipados y contratos existentes. No se vuelve a abrir Value, B1 ni el significado de Q. Se mantienen scientific_execution=false y execution_authorized=false.



## 36. Contrato mínimo de parámetros del DGP estructural y enlace con Q_B1 (2026-11-11)

**Estado:** MINIMUM_PARAMETER_PARTITION_SPECIFIED / REUSE_OF_ACCEPTED_SERVICE_ROSTER / VECTOR_PRESERVATION_REQUIRED / STRUCTURAL_SIGNATURE_MAPPING_OPEN / NUMERIC_CALIBRATION_BLOCKED_PENDING_SIGNATURES / NOT_DESIGN_FROZEN / NOT_IMPLEMENTED / NOT_EXECUTED.

### 36.1 Regla de parsimonia y precedencia

Esta sección no crea una nueva taxonomía ni reemplaza los contratos existentes. Especializa para el DGP de referencia las decisiones aceptadas DEC-C10-053, DEC-C10-054 y DEC-C10-068, el contrato abstracto C_src/C_dst/M, el inventario finito y la separación FP-01…FP-08. Se excluyen del núcleo confirmatorio inicial POL, políticas de seguridad, múltiples servicios, múltiples unidades lógicas por UE y extensiones de mapping split/merge. Su exclusión debe declararse en la configuración antes de generar el DGP; no se generaliza a escenarios adversariales.

### 36.2 Roster estructural mínimo reutilizable

El paquete funcional mínimo de referencia reutiliza la instancia de servicio ya aceptada:
- un CMP: una instancia lógica de servicio por UE, con identidad, clase/rol funcional y versión contractual;
- PAR BOOL PAR-SVC-ENABLED ∈ {false,true};
- PAR ENUM PAR-SVC-PROFILE ∈ {STANDARD, READ_ONLY, DISABLED};
- una RUL constitutiva RUL-SVC-ENABLE-PROFILE-01, con la expresión aceptada por DEC-C10-068: OR(NEQ(ENABLED,true),IN(PROFILE,{STANDARD,READ_ONLY})), efecto REQUIRE, AST acíclico dentro del límite 4/16/16;
- REF: universo declarado y cardinalidad explícita. En el fixture mínimo no se presupone ninguna referencia intercomponente; se registra REF_COUNT=0 solo si la frontera confirma que no existen relaciones funcionales internas necesarias. Si se identifica una relación necesaria, el fixture deja de ser esta instancia mínima y el extremo/tipo/dirección/multiplicidad se debe declarar antes de calibrar;
- MET: identidad de UE/servicio, versiones de C_src/C_dst/M, versión de regla y procedencia obligatorias.

El estado ENABLED=true, PROFILE=DISABLED es violación conocida de RUL; los estados ENABLED=true con perfiles STANDARD o READ_ONLY son permitidos por la regla. Un valor ausente/conflictivo mantiene UNKNOWN. Esta regla no se usa para definir Outcome, Q_B1 o Value.

Este roster reutiliza un contrato sintético ya aceptado; no afirma que el contrato completo de migración ni el mapping destino estén cerrados.

### 36.3 Parámetros estructurales y de transformación

La configuración debe declarar, sin defaults silenciosos:

1. C_src: identidad/versionado y tupla completa de componentes, parámetros (incluidos estados), referencias y reglas.
2. C_dst_decl y C_dst_applied: representaciones declarada y realmente aplicada, separadas.
3. M: correspondencias tipadas de CMP/PAR/REF/RUL/MET, conversión, pérdida permitida y cobertura.
4. ΔT_acc*=(ΔU,ΔR,ΔC,ΔX): delta vectorial completo entre snapshots basales y post, con identidad/versiones, altas, bajas, cambios, relaciones, configuraciones y estados indeterminados según el contrato vigente.
5. A_f* y D_f*: predicados focales derivados de sus condiciones constitutivas; no se asignan como sustitutos de ΔT_acc*.
6. Reach_H y trayectoria: derivados del catálogo, relaciones, condiciones, recursos, autorizaciones y cobertura del inventario; no se deducen de Q_B1.

Los parámetros de catálogo, dominios por clave, conversiones y mappings no se rellenan con valores inventados. La instancia BOOL/ENUM/RUL anterior cubre expresividad mínima del servicio, pero no resuelve por sí sola REF, C_dst_applied, F*, Reach ni el oráculo completo de preservación funcional.

### 36.4 Firma estructural completa y no reducción escalar

El soporte de accesibilidad que recibe el mecanismo de Q se define como un conjunto finito de firmas completas d_j, cada una identificando una realización tipada de ΔT_acc* (componentes, parámetros, relaciones, configuraciones, versiones y estados de evidencia relevantes). La firma es una clave de lookup del DGP, no una nueva variable causal ni un índice de magnitud.

Las políticas g0/g1 inducen distribuciones P_g(d_j|q) sobre esas firmas. Las transiciones p01(d_j,q) y p10(d_j,q) se parametrizan por firma completa y régimen común q. No se permite reemplazar d_j por una puntuación, una etiqueta binaria de instalación o un escalar de nivel de accesibilidad. Una reducción o agrupación de firmas solo se admite si preserva explícitamente todas las distinciones causales y transformacionales necesarias y se documenta antes del análisis.

El DGP focal de referencia exige como mínimo dos firmas completas distintas dentro del soporte común de g0/g1, de forma que el contraste no sea una mera comparación de etiquetas de política. Las firmas concretas deben proceder del contrato C_src/C_dst/M y del generador de T_acc; no se inventan en esta sección.

### 36.5 Partición mínima de parámetros generativos

Una vez resueltas las firmas, la configuración numérica se limita a estos bloques:

| Bloque | Parámetros mínimos | Restricción |
|---|---|---|
| Soporte estructural | firmas completas d_j; correspondencia con snapshots y ΔT_acc* | finito, versionado, tipado y derivado de C_src/C_dst/M |
| Política | P_g0(d_j|q), P_g1(d_j|q) | suma 1; soporte común para el contraste focal |
| Estado inicial | π_0=P(A_0=1) | común entre brazos en el DGP focal; especificar inclusión temporal |
| Disponibilidad | p01(d_j,q), p10(d_j,q) por firma | en [0,1]; no degeneradas salvo escenario que lo declare |
| Vía colateral | parámetro/tabla separada γ_direct o mecanismo equivalente | exactamente ausente/nulo en focal y nulo; activado solo en escenario adversarial |
| Horizonte | K slots iguales en W normalizado | común por UE/brazo; selección por convergencia |
| Observación | sensibilidad, especificidad, cobertura, latencia, missingness y censura | ideal perfecto en referencia; parámetros explícitos en cada estrés |

q se fija como régimen común versionado de condiciones externas; no se estima ni modifica diferencialmente entre g0/g1 en el escenario focal. No se añade un coeficiente lineal sobre un score de ΔT_acc. El lookup por firma completa es la forma mínima compatible con la estructura vectorial.

### 36.6 Restricciones cruzadas y pruebas de coherencia

Antes de aceptar cualquier punto de la cuadrícula:
- toda firma d_j debe corresponder a un par de snapshots y mapping adjudicable; una firma sin soporte material no puede recibir probabilidad positiva;
- P_g debe tener soporte común para identificar el contraste focal; violaciones se reservan para escenario explícito de no-identificación;
- los valores p01/p10 deben pertenecer a [0,1] y generar Q_B1 ∈ [0,1];
- la distribución inicial y la convención de slots deben ser idénticas entre brazos focales;
- γ_direct=0 en el escenario focal y nulo; su activación no puede confundirse con el efecto de ΔT_acc*;
- la verdad analítica de §35 y la esperanza del generador deben concordar dentro del error Monte Carlo preregistrado;
- el canal ideal no añade error ni altera disponibilidad; ausencia de observación en estrés no se codifica como indisponibilidad;
- ninguna regla estructural, Reach, Outcome o Value usa la truth de otro bloque como definición.

### 36.7 Dictamen: qué se ha cerrado y qué bloquea la calibración

Se cierra la partición mínima de parámetros, el roster de servicio que puede reutilizarse, la forma de representar el soporte vectorial de accesibilidad y la lista completa de bloques generativos necesarios. Se evita inventar una magnitud escalar o valores numéricos.

La calibración numérica sigue bloqueada por una dependencia concreta, no por una nueva lista abierta indefinidamente: instanciar al menos dos firmas completas ΔT_acc* a partir de C_src/C_dst_applied/M y del inventario de transformaciones, con su evidencia/oráculo de preservación y mapping. La matriz abstracta y el inventario actual reconocen expresamente que esos dominios, mappings y F*/Reach no están cerrados. Sin esas firmas no pueden definirse con significado las distribuciones P_g(d_j|q) ni los efectos de transición por firma.

El siguiente trabajo se limita a resolver esa instanciación estructural mínima reutilizando el roster BOOL/ENUM/RUL aceptado y el fixture finito existente. No se reabre Value, Q_B1, el horizonte ni el método P178. No se implementa, no se generan fixtures/datos, no se simula y no se ejecuta el experimento. scientific_execution=false; execution_authorized=false.



## 37. Instanciación de dos firmas semánticas completas de ΔT_acc* a partir de AB-03-SYN (2026-11-11)

**Estado:** TWO_ABSTRACT_STRUCTURAL_SIGNATURES_SPECIFIED / AB03_SYN_REUSED / R0_FOCAL_REFERENCE / PHYSICAL_MAPPING_NOT_REQUIRED_FOR_SYNTHETIC_TRUTH / NUMERIC_CALIBRATION_NEXT / NOT_DESIGN_FROZEN / NOT_IMPLEMENTED / NOT_EXECUTED.

### 37.1 Corrección de precedencia: no exigir mapping físico para la verdad del DGP sintético

La §36.7 identificó correctamente la necesidad de dos firmas completas, pero formuló como requisito previo que procedieran de C_src/C_dst_applied/M y de evidencia/oráculo de preservación material. Esa exigencia es excesiva para el objetivo acordado de C10-S: probar un método causal dentro de un DGP sintético cuya verdad se estipula y sella antes del análisis.

AB-03-SYN ya autorizó la instanciación semántica abstracta de las cuatro cards F1/F2/A1/A2 y sus TID/SID sintéticas. DEC-C10-068, DEC-C10-084…087 y el crosswalk de cards fijan sus funciones, invariantes y etapas a nivel lógico. Por tanto, las firmas de verdad del DGP pueden definirse sobre esos objetos semánticos y sus predicados de accesibilidad, sin fingir una realización física, mapping material observado, aplicación real o evidencia externa.

Se corrige la precedencia: C_src/C_dst_applied/M, IAM físico, mapping material y evidencia/oráculo de preservación siguen siendo necesarios para una implementación material o una afirmación empírica sobre migraciones reales; no son precondición para instanciar la truth semántica abstracta del experimento sintético. Esta sección no adjudica ni declara PASS de ningún mapping físico.

### 37.2 Frontera del DGP focal de referencia

Se reutiliza el catálogo semántico AB-03-SYN:
- F1 = tr:tgcv-c10s-syn:0001, conversión focal S0→S2;
- F2 = tr:tgcv-c10s-syn:0002, aplicación/verificación focal S2→SF;
- A1 = tr:tgcv-c10s-syn:0003, exportación alternativa S0→S1;
- A2 = tr:tgcv-c10s-syn:0004, importación/aplicación alternativa S1→SF;
- relaciones composicionales catalogadas F1→F2 y A1→A2, sin aristas cruzadas.

El DGP focal de referencia usa el régimen R0: la ruta alternativa A1→A2 está ausente/inaccesible en baseline y post, estipulado en la truth del generador dentro del catálogo finito declarado. No se afirma ausencia en sistemas reales. Los escenarios R1/R2 y las vías colaterales se conservan como escenarios separados; no se mezclan con el contraste focal aislado.

### 37.3 Dos firmas completas

Se define el objeto de firma como la tupla vectorial íntegra d=(ΔU*,ΔR*,ΔC*,ΔX*). Los nombres de las cuatro TID y sus relaciones proceden de AB-03-SYN; los estados siguientes son estipulaciones explícitas de la truth del DGP, no observaciones.

**Firma d0 — sin apertura focal (referencia nula de accesibilidad):**
- U*_baseline=U*_post: F1/F2 no pertenecen al conjunto accesible y A1/A2 permanecen fuera del conjunto accesible conforme al régimen R0; por tanto ΔU*=∅.
- R*_baseline=R*_post: no existe arista en el subgrafo accesible; por tanto ΔR*=∅.
- C*_baseline=C*_post: para F1 y F2, ID=1, REL=1, COND=0, AUTH=1, RES=1, DEP=1 y BLOCK=0. La conjunción constitutiva de accesibilidad es falsa y no hay cambio de condiciones, por tanto ΔC*=∅. Los predicados de aplicabilidad desde S0/S2 se mantienen separados y no se infieren.
- ΔX*=∅: no cambia el contexto externo ni el estado ambiental entre snapshots.

**Firma d1 — apertura de la ruta focal completa:**
- U*_baseline=∅ y U*_post={F1,F2}: ambas TID se incorporan al conjunto de transformaciones accesibles; por tanto ΔU*={F1,F2}.
- R*_baseline=∅ y R*_post={F1→F2}: la relación composicional catalogada queda incorporada al subgrafo accesible; la definición de la relación en el catálogo no cambia y ΔR*={F1→F2}.
- C*_baseline mantiene COND=0 y C*_post tiene COND=1 para F1 y F2; ID=1, REL=1, AUTH=1, RES=1, DEP=1 y BLOCK=0 permanecen constantes. Por tanto ΔC* registra exclusivamente COND: 0→1. La accesibilidad de cada transformación resulta de la conjunción completa de sus predicados, no de una etiqueta de apertura asignada directamente.
- ΔX*=∅: contexto externo y estado ambiental constantes.

En ambas firmas, A1/A2 permanecen inaccesibles bajo R0 y el universo transformacional declarado es el mismo. d0 y d1 son distintos en el objeto vectorial completo; no son un score ni un binario sustitutivo de ΔT_acc*. A_f* y D_f* se derivan de los predicados y snapshots; no reemplazan la firma.

### 37.4 Contraste de políticas y mecanismo de Value

Las políticas factibles g0/g1 inducen distribuciones distintas sobre el soporte común {d0,d1}. Se exige positividad en ambas firmas para el contraste focal y desigualdad entre las distribuciones; no se fijan todavía probabilidades numéricas. No se asigna abstractamente A ni se identifica la política con una etiqueta de instalación.

El Generator aplica después el mecanismo temporal de §35: las probabilidades de transición de disponibilidad p01(d,q) y p10(d,q) pueden diferir entre d0 y d1; el régimen externo q, la distribución inicial y la convención temporal son comunes. En el DGP focal, la firma de accesibilidad es la única vía diferencial entre política y disponibilidad/Value. La relación funcional entre firma y transiciones es una estipulación causal explícita del DGP que el Analyzer debe recuperar a partir de evidencia observada; no es un resultado empírico ni una afirmación universal de TGCV.

La truth del estimando se calcula con el oráculo analítico de §35, integrando sobre P_g(d|q). La cuadrícula incluirá:
- efecto: p01/p10 difieren entre d0 y d1, con signos/magnitudes a calibrar;
- nulo: las transiciones son invariantes entre firmas, aunque g0/g1 induzcan distribuciones distintas;
- adversarial: una vía directa/colateral se activa en un escenario separado, invalidando la atribución exclusiva;
- no identificación: se degrada soporte u observación en escenario separado, con truth conocida solo por Evaluator.

La hipótesis no presupone signo positivo. La calibración de parámetros de transición, distribuciones de política, K, N y R se realiza después, con P178 y criterios ex ante.

### 37.5 Alcance de la resolución y pendientes residuales

Queda cerrada la instancia semántica mínima de dos firmas completas para el DGP focal. Ya no bloquean la calibración los detalles de formato físico, nombres de plataforma, mapping material observado, serialización, IAM físico ni aplicación real: pertenecen a implementación/validación material y no a la truth sintética.

Antes de calibrar numéricamente solo se deben especificar y justificar los valores de P_g0(d0/d1|q), P_g1(d0/d1|q), p01(d0/q), p10(d0/q), p01(d1/q), p10(d1/q), π0, K y los criterios de precisión/potencia/Monte Carlo. No se añaden nuevos artefactos ni matrices.

**Dictamen:** STRUCTURAL_SIGNATURE_GATE_CLOSED_FOR_ABSTRACT_SYNTHETIC_DGP / NUMERIC_CALIBRATION_READY_AS_DESIGN_TASK / MATERIAL_MAPPING_OPEN_FOR_IMPLEMENTATION_ONLY. Se mantiene scientific_execution=false, execution_authorized=false; no se generan fixtures, no se simula y no se ejecuta experimento.



## 38. Cierre de la frontera R0 y parametrización mínima de políticas/transiciones (2026-11-11)

**Estado:** R0_FINITE_SYNTHETIC_UNIVERSE_CLOSED_BY_STIPULATION / POLICY_AND_TRANSITION_PARAMETERIZATION_SPECIFIED / NO_ARBITRARY_NUMERIC_VALUES / P178_CALIBRATION_CRITERIA_OPEN / NOT_DESIGN_FROZEN / NOT_IMPLEMENTED / NOT_EXECUTED.

### 38.1 R0: ausencia alternativa por frontera sintética exhaustiva, no por inferencia

Se aplica la regla de cobertura del inventario finito: no encontrar una ruta no demuestra su ausencia. Para este DGP sintético, R0 se define expresamente mediante una frontera cerrada y exhaustiva, limitada al catálogo AB-03-SYN de cuatro TID y dos relaciones permitidas: F1→F2 y A1→A2. No existen otras TID, SID ni relaciones en la verdad de este escenario. Esta es una estipulación de mundo sintético, no una afirmación sobre el microdominio real ni sobre migraciones observadas.

La relación A1→A2 permanece en el catálogo, pero sus pasos no son accesibles en R0. Para A1 y A2 se estipula en baseline y post: ID=1, REL=1, AUTH=1, RES=1, DEP=1, BLOCK=0 y COND=0; por tanto, la conjunción constitutiva de accesibilidad es falsa para ambos pasos y no existe ruta alternativa accesible. El evaluador conoce la verdad y el Analyzer solo recibe la evidencia observada que corresponda. Si la frontera se amplía o aparece una quinta transformación/relación, deja de ser R0 y debe declararse otro escenario antes de generar datos.

En F1/F2 se mantienen exactamente las dos firmas de §37: d0 conserva COND=0 en ambos snapshots; d1 cambia COND de 0 a 1 para ambos pasos, incorpora F1/F2 al conjunto accesible y activa la relación accesible F1→F2. La aplicabilidad, Reach, selección y ejecución siguen siendo variables distintas; la apertura de esta ruta no se usa como evidencia de que se haya ejecutado ni de que se haya alcanzado SF.

### 38.2 Parámetros de política: distribución sobre firmas completas

Con soporte {d0,d1}, la parametrización mínima de cada política es:

- λ0 = P(d1 | g0,q);
- λ1 = P(d1 | g1,q).

Las probabilidades complementarias son P(d0|g,q)=1−λg. Para el contraste focal se exige 0<λ0<λ1<1: ambas firmas tienen soporte positivo en ambos brazos y las políticas inducen distribuciones distintas. λ0 y λ1 son parámetros de la intervención estocástica sobre firmas estructurales completas; no son probabilidades de instalación, cumplimiento, ejecución ni éxito. No se asignan valores numéricos en esta resolución.

### 38.3 Parámetros de transición: tabla por firma, sin score de accesibilidad

Se parametriza el mecanismo temporal mediante la tabla de transición de referencia para d0 y dos contrastes logit:

- b01 = logit P(A_k=1 | A_(k−1)=0,d0,q);
- b10 = logit P(A_k=0 | A_(k−1)=1,d0,q);
- α01 = logit p01(d1,q) − b01;
- α10 = logit p10(d1,q) − b10.

Así, p01(d0,q)=logit⁻¹(b01), p10(d0,q)=logit⁻¹(b10), p01(d1,q)=logit⁻¹(b01+α01) y p10(d1,q)=logit⁻¹(b10+α10). Esta es una tabla de lookup entre firmas completas y transiciones; α01/α10 no son coeficientes de un score o de una magnitud escalar de ΔT_acc*. La transformación logit garantiza probabilidades estrictamente entre 0 y 1 para parámetros finitos.

El escenario nulo usa α01=α10=0. Los escenarios de efecto positivo y negativo se clasifican por el signo de θ_A calculado con el oráculo analítico, no solo por el signo aislado de un α: ambos procesos de entrada/salida pueden contribuir y la dirección neta depende de la combinación y de K. Se explora una cuadrícula de α01/α10 que incluya ambos signos netos y efectos próximos a cero. No se presupone monotonicidad favorable.

### 38.4 Estado inicial, régimen y resolución temporal

- π0=P(A0=1) es común a las dos firmas y a ambos brazos en el contraste focal. Se explora como parámetro basal; no se permite que dependa de g o d en el escenario focal.
- q es un régimen externo versionado, común y no diferencial entre políticas.
- K es el número de slots de igual duración que particiona W_B1. K≥2 para que el DGP represente al menos una transición temporal; K no es H, no es una duración física y no se fija aquí. La duración normalizada de W y su discretización se declaran en la configuración. Se examina la estabilidad de μ_Q y θ_A frente a refinamiento de K; la selección final debe ser compatible con la resolución temporal que el experimento pretende representar.

La esperanza de Q/V para cada firma se calcula con la recurrencia exacta de §35. El efecto de política es la mezcla por λg. Para el caso de dos firmas:

E[V^(q,g)] = (1−λg)·μ_Q(d0,q;K) + λg·μ_Q(d1,q;K)

y

θ_A(q;V_B1) = (λ1−λ0)·[μ_Q(d1,q;K)−μ_Q(d0,q;K)].

Esta identidad permite comprobar directamente el oráculo y muestra que el contraste de política es nulo si no hay primera etapa (λ1=λ0) o si la firma no modifica la disponibilidad (μ_Q(d1)=μ_Q(d0)). No implica que el efecto por unidad de ΔT_acc* esté identificado ni que sea universal.

### 38.5 Vías alternativas y canal de observación

El escenario focal y el nulo fijan en cero cualquier término directo/colateral diferencial por política. Los escenarios adversariales incorporan el término separado γ_direct o un mecanismo explícito equivalente, sin absorberlo en α ni atribuirlo a ΔT_acc*. La clasificación de identificación del Analyzer debe reflejar la vía alternativa.

La referencia de recuperación puede usar observación ideal y completa para aislar el rendimiento del estimador bajo identificación conocida. Errores de clasificación de firmas, sensibilidad/especificidad, cobertura imperfecta, latencia, missingness y censura se introducen como escenarios separados, con truth intacta y evidencia observada degradada. La ausencia de observación nunca se codifica como A=0 ni como indisponibilidad.

### 38.6 P178: regla de calibración y límite de lo que puede fijarse ahora

Se reutiliza P178-SIM-01…10 y §7 de PD. No se importan N=2.000, asignación 1:1 ni R=1.000 como defaults. La cuadrícula analítica produce θ_A verdadero para cada combinación factible de λ0, λ1, b01, b10, α01, α10, π0 y K. Se descartan combinaciones con soporte inválido o parámetros fuera del dominio.

Para este estudio de rendimiento metodológico, el MDE se informará como resultado de la curva potencia/precisión en función de N, bajo criterios de error tipo I, potencia y precisión fijados antes de observar las simulaciones; no se inventará un δ_min sustantivo de Value ni se usará un efecto elegido para hacer que el Analyzer pase. La recuperación de estimación continua se evalúa además mediante sesgo, RMSE y cobertura frente a la verdad analítica. Si se requiere una afirmación de relevancia sustantiva, su umbral necesita una justificación externa al DGP y no se deriva de TGCV.

La búsqueda de N y R es una operación computacional de calibración todavía no autorizada. Antes de ejecutarla deben quedar aprobados los criterios ex ante de error tipo I, potencia, cobertura/precisión y tolerancia SE_MC, así como el coste/alcance de la cuadrícula. Esta resolución no selecciona esos valores ni inicia dicha búsqueda.

### 38.7 Dictamen

Se cierra la frontera sintética R0, la asignación de políticas a las dos firmas, la parametrización de transiciones, el papel de π0/K y la descomposición exacta de θ_A. No se han asignado cifras arbitrarias ni se ha confundido H=3 con el horizonte temporal.

El trabajo restante para la calibración numérica ya no es una dependencia estructural o semántica: es una decisión metodológica acotada sobre criterios ex ante de rendimiento y coste de calibración P178. Value, Q_B1, las firmas d0/d1 y la frontera R0 no se reabren. Se mantienen scientific_execution=false y execution_authorized=false; no se generan fixtures, no se simula y no se ejecuta experimento.



## 39. Criterios ex ante P178 para evaluar recuperación causal y calibrar N/R (2026-11-11)

**Estado:** PRIMARY_METHOD_PERFORMANCE_CRITERIA_PROPOSED / NO_SUBSTANTIVE_MDE_ASSUMED / REPLICATION_RULE_DERIVED_FROM_MCSE / N_AS_POWER_PRECISION_CURVE / AWAITING_EXPLICIT_APPROVAL_BEFORE_CALIBRATION / NOT_DESIGN_FROZEN / NOT_IMPLEMENTED / NOT_EXECUTED.

### 39.1 Alcance: no importar al DGP sintético todos los estimandos del protocolo material

El experimento de referencia definido en §§35–38 tiene un único estimando causal primario: θ_A(q;V_B1), efecto de las políticas estocásticas g1/g0 sobre V_B1 a través de las dos firmas completas de ΔT_acc*. No es el D2 material y no pretende identificar ITT-V, LATE, mediación C4 ni efectos en poblaciones empíricas. Las métricas de primera etapa y la clasificación de escenarios adversariales se reportan como diagnósticos del diseño; no se elevan a estimandos confirmatorios adicionales.

Esta delimitación resuelve la tensión entre la lista genérica de PD §7 y la instancia sintética focal: la búsqueda primaria de N se refiere a θ_A; no se exige potencia para LATE/IV ni mediación que no forman parte de este DGP.

### 39.2 Criterios de error, potencia y cobertura

Se proponen, como convenciones metodológicas ex ante para evaluar rendimiento del procedimiento —no como constantes de TGCV ni umbrales sustantivos de Value—:
- nivel nominal bilateral α=0.05 para H0: θ_A=0;
- potencia objetivo ≥0.80 en cada punto no nulo de la cuadrícula de efectos que se etiquete como punto de diseño evaluable;
- cobertura nominal de 95% para los intervalos de confianza de θ_A;
- control del falso positivo en el DGP nulo: tasa empírica compatible con α=0.05 dentro de su incertidumbre Monte Carlo, sin declarar control solo porque la estimación puntual sea ≤0.05;
- sesgo y RMSE informados en escala original de V_B1, junto con error de calibración y frecuencia de intervalos no finitos/abstención.

No se introduce δ_min sustantivo ni se selecciona un efecto para hacer pasar el Analyzer. La cuadrícula incluye θ_A=0, valores no nulos positivos y negativos y una banda próxima a cero; se informa la curva potencia/precisión como función de θ_A y N. El MDE es una lectura derivada de esa curva para cada N, no un input normativo. No se resume la cuadrícula en un único N confirmatorio si no existe una justificación sustantiva para seleccionar un punto de efecto.

### 39.3 Precisión y selección de N

Para cada punto de la cuadrícula se informa:
1. potencia y su intervalo Monte Carlo;
2. sesgo, RMSE y cobertura de θ_A;
3. anchura media/mediana del intervalo de confianza y distribución de anchuras;
4. probabilidad de identificación correcta, identificación parcial y abstención;
5. N efectivo y, solo si la unidad de asignación/observación lo requiere, ICC, efecto de diseño y número de clústeres.

La salida de calibración será una curva/tabla N×θ_A, con el menor N que alcance potencia objetivo para cada punto, siempre que cobertura y precisión no fallen. La precisión se presenta mediante anchura de intervalo en la escala de V_B1; no se inventa un margen relativo de relevancia. La elección de un N operativo único requiere declarar qué zona de efectos de la cuadrícula debe cubrirse y justificar esa selección. Hasta entonces no hay un N universalmente recomendado para el experimento.

### 39.4 Réplicas R y tolerancia de error Monte Carlo

Se fija como criterio de estabilidad de las tasas de error tipo I, potencia, cobertura y clasificación una semiamplitud/SE Monte Carlo objetivo no superior a 0.005 en escala de proporción, comprobada por lote y con intervalo binomial. Para una proporción desconocida, el límite conservador de varianza p(1−p)≤0.25 implica R≥10,000 réplicas independientes por celda para SE_MC≤0.005. Si se usa un intervalo binomial exacto o Wilson, se informa su anchura y se mantiene la misma tolerancia objetivo; no se interpreta R=10,000 como cifra universal si el cálculo secuencial demuestra antes que el criterio está satisfecho.

Para sesgo y RMSE, R se incrementa por lotes hasta que el error Monte Carlo de la métrica sea ≤5% de su error estándar de referencia o, cuando esa razón no esté definida/cercana a cero, hasta una tolerancia absoluta preregistrada en unidades de V_B1. La regla de parada, el tamaño de lote, la semilla jerárquica y el tratamiento de réplicas inválidas se fijan en el manifiesto antes de calibrar. No se reemplazan fallos de convergencia por réplicas nuevas sin contabilizarlos.

### 39.5 Cuadrícula mínima y clasificación de escenarios

La cuadrícula se construye sobre parámetros ya definidos en §38, no sobre nuevas variables:
- política: λ0, λ1 con soporte común y λ1>λ0;
- proceso: b01, b10, α01, α10, π0 y K;
- verdad: θ_A calculado exactamente por el oráculo;
- observación: referencia ideal completa y, separadamente, estrés de clasificación/cobertura/missingness/censura;
- mecanismo alternativo: γ_direct=0 en focal/nulo y distinto de cero en el escenario adversarial;
- soporte: común en focal/efecto/nulo y degradado de forma declarada en no-identificación.

La clasificación positiva/negativa/nula se hace por θ_A exacto, no por el signo de α aislados. La cuadrícula debe contener casos de θ_A exactamente nulo por α01=α10=0 y controles de primera etapa nula cuando λ1=λ0, estos últimos fuera del contraste focal identificable y etiquetados como control de no-identificación del efecto de política. No se mezcla una vía directa con el escenario focal.

### 39.6 Dictamen y condición de avance

Quedan especificados los criterios metodológicos recomendados: α bilateral 0.05, potencia objetivo 0.80, cobertura nominal 95%, tolerancia SE_MC 0.005 para tasas, regla adaptativa de R y salida N×θ_A en vez de un N arbitrario. Son decisiones de diseño propuestas y justificadas, no valores de verdad de TGCV. Requieren aprobación explícita antes de iniciar la calibración computacional P178.

Una vez aprobados, la calibración podrá calcular N/R y los parámetros numéricos concretos de la cuadrícula. La calibración no es ejecución científica confirmatoria, pero sí es trabajo computacional/simulación y por tanto no se inicia con el estado actual de autorización. La siguiente transición tras la aprobación será producir el manifiesto cuantitativo y ejecutar únicamente la calibración autorizada; la ejecución confirmatoria seguirá siendo una autorización separada.

Se mantiene scientific_execution=false y execution_authorized=false. No se han generado datos, fixtures, simulaciones ni resultados.
