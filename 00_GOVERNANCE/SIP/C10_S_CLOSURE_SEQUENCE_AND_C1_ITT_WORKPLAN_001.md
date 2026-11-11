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
