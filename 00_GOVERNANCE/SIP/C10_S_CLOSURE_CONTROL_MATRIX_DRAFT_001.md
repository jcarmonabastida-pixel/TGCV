# C10-S — Matriz maestra de cierre, reconciliación y trazabilidad
**Documento de control metodológico — borrador 001**

**Estado:** DRAFT / CONTROL DE CIERRE — NO APROBADO / NO CONGELADO  
**Repositorio:** `jcarmonabastida-pixel/TGCV`  
**Rama:** `research/c10-s-consolidation-draft`  
**PR:** #116 (Draft), dependiente de PR #115 (C10-D1, Draft)  
**Corte documental:** 2026-11-04  
**Fuentes rectoras:** C10-D1 draft 001; C10-S consolidated draft 004; auditoría integrada AUD-001…012; propuesta de resolución AUD-001/002; auditoría cruzada XAUD-001…007; informe de recuperación histórica.

---

## 1. Propósito y regla de uso

Esta matriz convierte el material recuperado en un único instrumento de cierre. No reemplaza C10-D1, el documento consolidado C10-S, las auditorías ni sus fuentes. No declara aceptada ninguna propuesta que siga abierta. Cada fila distingue:

- **Evidencia documental:** lo que existe efectivamente en los artefactos consultados.
- **Estado:** cerrado documentalmente, propuesto, abierto, pendiente de validación o no recuperado.
- **Criterio de aceptación:** condición verificable para cerrar el asunto.
- **Acción siguiente:** operación documental necesaria, sin presuponer una decisión científica.

La numeración de las secciones conversacionales no constituye por sí sola una fuente primaria. Cuando no existe texto original o artefacto íntegro, se registra la laguna; no se inventa ni se reconstruye como si fuera literal.

**Límite operativo:** este documento no autoriza código, simulación, ejecución experimental, estimación, adquisición/procesamiento de datos, preregistro, selección definitiva de caso ni cambios en Core, RMA, Evidence→Claim Matrix, STATUS o claims.

## 2. Inventario de fuentes y cobertura comprobada

| ID | Fuente | Identidad/ubicación | Cobertura comprobada | Estado |
|---|---|---|---|---|
| SRC-01 | C10-D1 | `C10_D1_CAUSAL_ACCESSIBILITY_VALUE_PROTOCOL_DRAFT_001.md`, PR #115, blob `bf25f6ec8965166e5fa52ff18e6d07613bad0eb3` | Protocolo causal consolidado; 38 secciones principales según registro de recuperación | Draft, no aprobado |
| SRC-02 | C10-S | `C10_S_SYNTHETIC_EXPERIMENT_CONSOLIDATED_DRAFT_004.md`, PR #116, blob actual `87e3a3cb385fd3fb05f106dcdc0a5829431a5bc5` | Base histórica hasta sección conversacional 164; recuperación resumida 165–183 en §§52–53; capítulos de reconciliación y medición §§54–60 | Draft, no aprobado |
| SRC-03 | Auditoría integrada | `C10_S_INTEGRATED_CONSISTENCY_AUDIT_DRAFT_001.md`, blob `d3ffa9ed0670764c339dc390423f435e6da0fc9b` | AUD-C10S-001…012 | Hallazgos abiertos |
| SRC-04 | Propuesta de resolución | `C10_S_AUD001_AUD002_RESOLUTION_DRAFT_001.md`, blob `5a3a2fa061fe146d9df9d4cdfbb803c5ee274d65` | Propuesta A_f, T_acc, ΔT_acc y DGP integrado | No aceptada |
| SRC-05 | Auditoría cruzada | `C10_S_AUD001_AUD002_CROSS_AUDIT_DRAFT_001.md`, blob `ce53c902fb39820e976eed5cb2a87e5eacace31c` | XAUD-001…007 | Hallazgos abiertos |
| SRC-06 | Informe de recuperación | `C10_S_RECOVERY_AND_TRACEABILITY_AUDIT_DRAFT_001.md`, blob `2f77832076773c67711f55a3c0d6680b69c2c6d9` | Reconstrucción de fuentes y límites hasta sección 183 | Recuperación parcial |
| SRC-07 | PR #115 | `research/c10-d1-protocol-draft` → PR #115 | 23 commits; 1 archivo; abierto Draft | Sin comentarios/revisiones |
| SRC-08 | PR #116 | `research/c10-s-consolidation-draft` → PR #116 | Trece archivos modificados en el corte de verificación 2026-11-04; el número de commits es dinámico; abierto Draft | Sin comentarios/revisiones registradas |

| SRC-09 | Reconciliación C10-D1 ↔ S4-R | `C10_S_C10D1_S4R_ESTIMAND_RECONCILIATION_DRAFT_001.md`, PR #116 | Jerarquía `θ_A(q)` / ITT_Z / LATE_f; propuesta para `p0` y poblaciones | Propuesta, no aprobada |
| SRC-10 | Decision log C10 | `C10_S_DECISION_LOG_DRAFT_001.md`, PR #116 | DEC-C10-001…010, decisiones abiertas y alternativas no admisibles | Registro inicial, no aprobado |
| SRC-11 | XSYNC tracker | `C10_S_XSYNC_138_CLOSURE_TRACKER_DRAFT_001.md`, PR #116 | Recupera y clasifica XSYNC-138-01…10, respuesta documental y cierre pendiente | Texto recuperado; hallazgos abiertos |
| SRC-12 | Registro de contratos de prueba | `C10_S_TEST_CONTRACT_REGISTER_DRAFT_001.md`, PR #116 | Normaliza S4R-01…18, MEAS-01…14, MISS-01…15, VER/TRJ/INT, POL-01…10 y GEN | Especificación; fixtures y pruebas no ejecutados |
| SRC-13 | Contrato integrado DGP temporal/roles | `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`, PR #116 | Secuencia causal-transformacional, variable×tiempo×rol, verdad/observado, estimandos e invariantes DGP-01…16 | Propuesta; no aprobada ni implementada |

### 2.1 Resultado de la búsqueda de fuentes posteriores a 164

Se revisaron las fuentes canónicas de C10-D1 y C10-S en sus ramas, el PR #116 y sus diez archivos modificados en el corte de esta actualización, el historial de comentarios/revisiones/hilos del PR (cero registros), y búsquedas de código en el repositorio para referencias distintivas de las secciones posteriores (incluidos P182-01 y P183-01). No se encontró en el repositorio una fuente íntegra adicional de las secciones conversacionales 165–183.

Este resultado no demuestra que el material no exista en exportaciones de conversación, archivos locales u otras fuentes no conectadas. Significa que no se ha podido recuperar desde los artefactos GitHub consultados ni certificar su literalidad. Se necesita una exportación o fuente original adicional para cerrar esa brecha histórica.

## 3. Matriz de recuperación histórica 165–183

| ID | Secciones | Material disponible | Estado | Criterio de cierre | Acción |
|---|---|---|---|---|---|
| REC-165-173 | 165–173 | Resúmenes temáticos parciales en contexto de continuidad; no texto íntegro ni fuente primaria enlazada | NO RECUPERADO ÍNTEGRAMENTE | Fuente original identificada, fechada y cotejada; cada decisión vinculada a su pasaje y estado | Recuperar exportación/notas originales; no reconstruir prosa |
| REC-174-176 | 174–176 | Resúmenes de decisiones, fórmulas y protocolos; no texto íntegro | NO RECUPERADO ÍNTEGRAMENTE | Contraste literal con artefacto primario y registro de decisiones aceptadas/propuestas | Recuperar fuente y mapear decisiones |
| REC-177 | 177 | Resumen de arquitectura de estimación que separa ITT, LATE, Outcome, Value y mecanismos | RESUMEN SECUNDARIO | Fórmulas, población, supuestos y decisiones confirmados contra fuente primaria | Mantener como pista, no como contrato |
| REC-178-181 | 178–181 | Información insuficiente para atribución temática fiable | LAGUNA DOCUMENTAL | Recuperación de fuentes originales; no basta inferencia temática | No asignar contenido ni IDs de prueba por conjetura |
| REC-182 | 182 | Resumen: validez de constructo y sensibilidad; separación A/O/V, validez, fiabilidad, error de medición, invariancia, sensibilidad; IDs P182-01…P182-12 | RESUMEN NO VERIFICADO | Texto íntegro + 12 fichas de prueba cotejadas, versionadas y con entradas/salidas/aserciones | Recuperar fuente; después incorporar contrato completo |
| REC-183 | 183 | Resumen: datos ausentes, censura y mediciones incompletas de A/O/V; MCAR/MAR/MNAR, censura, selección postasignación, ITT/mediación/LATE, cotas; IDs P183-01…P183-13 | RESUMEN NO VERIFICADO | Texto íntegro + 13 fichas de prueba cotejadas, versionadas y con entradas/salidas/aserciones | Recuperar fuente; después incorporar contrato completo |

**Regla de integridad:** no se declarará “recuperado” el contenido de 165–183 hasta disponer de fuente original verificable. Las etiquetas P182/P183 son referencias conocidas, no evidencia de que sus contratos estén completos.

## 4. Reconciliación C10-D1 ↔ C10-S

| ID | Punto de reconciliación | C10-D1 (rector causal) | C10-S (sintético) | Estado / criterio de cierre |
|---|---|---|---|---|
| REC-CAUS-01 | Pregunta y alcance | Atribución específica de cambios de T_acc/ΔT_acc a Value, separada del efecto de intervención | Prueba sintética de arquitectura y recuperación de escenarios conocidos | COHERENTE EN PROPÓSITO; mantener límite: C10-S no prueba causalidad real |
| REC-CAUS-02 | TE / ITT | `TE`/`ITT` de Z no atribuye por sí mismo a accesibilidad; C10-D1 §§25.5–25.6 y 26.2 lo separan de `θ_A(q)` | S4-R §51 propone ITT_Z como objetivo primario del diseño de provisión | RECONCILIACIÓN PROPUESTA en `C10_S_C10D1_S4R_ESTIMAND_RECONCILIATION_DRAFT_001.md`: ITT_Z primario del diseño S4-R, no sustituto de la pregunta científica C10. Pendiente de revisión/aprobación.
| REC-CAUS-03 | Efecto específico de accesibilidad | `θ_A(q)` entre políticas factibles bajo régimen común; C10-D1 §§17.7, 25.3 y 30.1–30.3 | S4-R focaliza apertura de `τ2`; `LATE_f` local condicionado a IV; `θ_Af(q*)` poblacional permanece distinto y abierto (§43.4) | RECONCILIACIÓN PROPUESTA: `LATE_f` no equivale a `θ_A(q)` poblacional ni a efecto de todo `ΔT_acc`; S4-R no afirma identificar el estimando general. Ver documento de reconciliación.
| REC-CAUS-04 | Intervención | Intervenir componentes implementables; no asignar abstractamente T_acc; políticas factibles y versiones | Z_A → C_auth → A_f* propuesto | ABIERTO: resolver q frente a g y si la política cambia solo autorización o también otras vías |
| REC-CAUS-05 | Variables y constructos | C_c constitutivas, L temporales, A/ΔT_acc, mecanismos, O, V separados | A_f*, A_f_obs, T_acc=(U,R,C), ΔT_acc, Reach, Π_H, selección, ejecución, O, V | PROPUESTA ÚTIL, NO ACEPTADA: consolidar diccionario único y temporal |
| REC-CAUS-06 | Población | Población, contexto, horizonte y régimen fijados antes de outcomes | P*_τ2 y P*_F; q_X* y q_L* en diseño S4-R | ABIERTO: definir población objetivo, inclusión, función F*, horizonte y cuándo P*_F es solo heterogeneidad |
| REC-CAUS-07 | Identificación | C10-D1 exige política implementable, soporte, versiones, temporalidad y separación de vías alternativas; aleatorización de B solo identifica ITT de B salvo identificación adicional | S4-R: `ITT_Z` y primera etapa; Wald solo como `LATE_f` local si IV defendible | RECONCILIACIÓN PROPUESTA: reglas de salida para exclusión, monotonicidad, primera etapa débil/nula, medición, interferencia y pérdidas; no inferir exclusión de los datos observados.
| REC-CAUS-08 | Outcome y Value | Medición separada; Value con regla independiente | O y V derivados tras ejecución; V_real separado de V_potential | PENDIENTE DE CONTRATO: regla, beneficiario, horizonte, costes/beneficios, incertidumbre y tests de no circularidad |
| REC-CAUS-09 | Temporalidad y datos incompletos | Snapshots longitudinales, medición, pérdidas, censura y selección | Secciones 130–164 contienen tratamientos parciales; 182/183 resumidas pero no verificadas | ABIERTO: recuperar 182/183 y construir matriz variable×momento×rol |
| REC-CAUS-10 | Conclusiones permitidas | Atribución identificada, evidencia adversa delimitada o identificación insuficiente | C10-S puede probar discriminación sintética y recuperación del DGP | COHERENTE: nunca traducir PASS sintético en prueba de hipótesis real |

### 4.1 Precedencia que debe respetarse

1. C10-D1 gobierna la interpretación causal y el alcance de estimandos.
2. C10-S especifica el entorno sintético y sus contratos transformacionales/causales.
3. Una decisión sintética no puede redefinir el estimando causal de C10-D1 por conveniencia de implementación.
4. Si una decisión de C10-S exige cambiar el estimando o el alcance de C10-D1, debe abrirse una decisión explícita y trazable; no se resuelve por armonización editorial.
5. ITT, θ_A(q), θ_Af(q), θ_{L,A}, IV/LATE y cualquier residual son objetos distintos. No se intercambian etiquetas ni interpretaciones.
6. La propuesta de jerarquía dual (pregunta científica C10 vs. objetivo primario del diseño S4-R) queda documentada en `C10_S_C10D1_S4R_ESTIMAND_RECONCILIATION_DRAFT_001.md`; no se considera aprobada hasta revisión explícita.


### 4.2 Reconciliación de estimandos (propuesta incorporada, no aprobada)

Se ha añadido el documento `C10_S_C10D1_S4R_ESTIMAND_RECONCILIATION_DRAFT_001.md` a PR #116. Este documento contrasta C10-D1 §§17, 25–26 y 30–34 con C10-S §§43 y 51 y propone:
- `θ_A(q)` permanece como pregunta científica C10-D1.
- `ITT_Z` es el objetivo primario del diseño aleatorizado S4-R, no sustituto de `θ_A(q)`.
- `LATE_f` es una estimación local focal de apertura de `τ2`, solo bajo supuestos IV; no equivale a ATE, `θ_A(q)` poblacional ni efecto de todo `ΔT_acc`.
- `P*_τ2` y `P*_F` deben definirse preasignación; `A_f,base*=0` es condición de elegibilidad para estimar apertura basal→post.
- Se conserva el DGP aislado principal con `p0=.20` y `p1=.80` como probabilidades post-asignación bajo B_g0/B_g1, y se distingue del estado basal `C_dep,base=0`. Se exige separar intento, éxito y estado verificado; el escenario adversarial añade contaminación/vías colaterales explícitas.

Estas son propuestas de armonización, no decisiones científicas aceptadas. La referencia completa, las fórmulas y reglas de salida están en el documento enlazado; no cerrar AUD/XAUD ni S4-R hasta revisión y decisión explícita.

## 5. Registro maestro de auditorías y bloqueos

### 5.1 AUD-C10S-001…012

| ID | Hallazgo | Estado | Criterio de aceptación mínimo |
|---|---|---|---|
| AUD-001 | A focal frente a ΔT_acc completo | ABIERTO; existe propuesta A_f | Definir A_f, T_acc y ΔT_acc en todo el DGP; mostrar qué cambia y qué no; ningún estimando focal presentado como efecto de todo ΔT_acc sin justificación |
| AUD-002 | Integración DGP causal-transformacional | PROPUESTA INTEGRADA EN SRC-13; pendiente de auditoría | Revisar cadena única, orden temporal, correspondencia de ecuaciones, verdad oculta y no filtración; completar fixtures y aprobación |
| AUD-003 | Contratos de pruebas no ejecutables | ABIERTO | Todas las pruebas del gate C10-S→C10-P tienen fixture, versión, entradas, verdad oculta, salida, aserciones, tolerancia, códigos y artefactos |
| AUD-004 | ΔT_acc relacional incompleto | ABIERTO | Formalizar ΔU, ΔR, ΔC, identidad/versionado, cambios de validez y estados indeterminados |
| AUD-005 | Reach_possible y trayectorias indeterminadas | ABIERTO | Lógica de tres estados, composición, deduplicación y reglas definite/possible |
| AUD-006 | S5-F sin DGP completo | ABIERTO | Ecuaciones generadoras, asignaciones, independencia, interacción y estimandos declarados |
| AUD-007 | S5-C verdad estructural vs identificabilidad | ABIERTO | Separar verdad DGP, soporte observado, estimando y conclusión permitida al analizador |
| AUD-008 | No circularidad de Value | ABIERTO | Pruebas metamórficas T_acc/O/Value; V_real y V_potential separados |
| AUD-009 | N y réplicas sin justificación de precisión/potencia | ABIERTO | Métricas de sesgo, cobertura, error Monte Carlo, precisión y justificación por escenario |
| AUD-010 | Diccionario variable×rol×tiempo | PROPUESTA PARCIAL EN SRC-13 | Completar cada variable del diccionario maestro, estados de ausencia, unidad/cluster y fuentes; revisar no filtración |
| AUD-011 | Clasificación C_c frente a L | PROPUESTA EN SRC-13 | Clasificar cada condición concreta por momento, papel causal, factibilidad y evidencia; no por etiqueta nominal |
| AUD-012 | Decision log incompleto | ABIERTO | ID, decisión, alternativas, justificación, estado, orden/fecha, fuente y commit para cada decisión |

### 5.2 XAUD-001…007

| ID | Hallazgo | Estado | Criterio de aceptación mínimo |
|---|---|---|---|
| XAUD-001 | Coherencia del régimen q con políticas g | ABIERTO / CRÍTICO | Separar variables fijadas por q de las manipuladas por g, o definir régimen conjunto coherente; mostrar contrafactuales factibles |
| XAUD-002 | Intervención autónoma sobre A_f no demostrada | ABIERTO | Separar ITT de política habilitadora y efecto atribuible a accesibilidad; no llamarlo efecto puro si hay vías colaterales |
| XAUD-003 | Accesibilidad, aplicabilidad y ejecución | PROPUESTA EN SRC-13 | Verificar predicados separados Acc_f, App_f, Reach, K/Consider, Sel, Start, Exec y End; mapear pruebas por estado |
| XAUD-004 | Asignación, provisión, verdad y medición | PROPUESTA EN SRC-13 | Verificar Z, B, W_attempt, S_install, C_dep, A_f*, A_f_obs, ΔT_acc y estados indeterminados; completar validación |
| XAUD-005 | Régimen E1 podría forzar ejecución inválida | PROPUESTA EN SRC-13 | Verificar precondiciones y salidas no aplicable/no seleccionado/no iniciado/interrumpido; fixtures adversariales pendientes |
| XAUD-006 | Orden temporal y snapshots | PROPUESTA EN SRC-13 | Auditar reloj t−1…t9, snapshots inmutables y eventos posteriores; falta completar reglas de simultaneidad/versionado |
| XAUD-007 | Notación y delimitadores | ABIERTO / EDITORIAL | Notación canónica única; revisión matemática/Markdown/LaTeX automatizable |

**Dependencia:** no cerrar AUD-001/002 ni XAUD-001/002 por mera edición de símbolos. La intervención físicamente realizable y el objeto causal deben estar resueltos antes de aprobar el contrato integrado.

## 6. S4-R: matriz de decisiones pendientes

| ID | Elemento | Estado | Decisión/aceptación necesaria |
|---|---|---|---|
| S4R-01 | Jerarquía ITT / pregunta C10 | RECONCILIACIÓN PROPUESTA | Mantener `θ_A(q)` como pregunta científica C10-D1; `ITT_Z` primario del diseño aleatorizado S4-R; `LATE_f` como atribución focal local condicionada a IV. Requiere revisión/aprobación.
| S4R-02 | IV/LATE focal | CONDICIONAL | Relevancia, independencia, exclusión, monotonicidad, consistencia/versiones, no interferencia y medición; si falla, no calcular/interpretar Wald |
| S4R-03 | P*_F | PROPUESTO | Mantener como subpoblación funcional exclusiva/heterogeneidad salvo decisión justificada distinta; no filtro automático de P*_τ2 |
| S4R-04 | S4R-A | PROPUESTO | Sin alternativa basal; documentar universo cerrado y límites de exclusividad |
| S4R-05 | S4R-B | PROPUESTO | Alternativa basal no afectada; medir invariancia funcional, no solo identidad de catálogo |
| S4R-06 | S4R-C | PROPUESTO | Provisión modifica alternativa; tratar como paquete/violación de exclusión IV focal salvo diseño alternativo que identifique componentes |
| S4R-07 | S4R-D | PROPUESTO | No cumplimiento/fallo de provisión; mantener Z, C_auth, A_f*, A_f_obs separados |
| S4R-08 | p0=.20 frente a C_dep,base=0 | RECONCILIACIÓN PROPUESTA | Separar elegibilidad basal de probabilidad post-asignación. DGP limpio recomendado: p0=0, p1 ilustrativo=.80; DGP adversarial separado con p0>0 generado por provisión/contaminación explícita. Pendiente de aceptación.
| S4R-09 | Política B y versiones | ABIERTO | Definir acción física, intensidad, elegibilidad, cumplimiento, contaminación, control y versiones |
| S4R-10 | q_X* y q_L* | ABIERTO | Definir población/distribución objetivo y cuándo usar régimen común basal frente a política longitudinal secuencial |
| S4R-11 | F*, horizonte y Value | ABIERTO | Operacionalizar función focal, horizonte, regla de Value y costes/efectos colaterales |
| S4R-12 | Alternativas funcionales | ABIERTO | Medir identidades/versiones, accesibilidad, precondiciones, recursos, coste, latencia, calidad y seguridad |
| S4R-13 | Primera etapa nula/débil | ABIERTO | Regla explícita: no Wald con primera etapa nula; inferencia robusta y lenguaje de conclusión para primera etapa débil |
| S4R-14 | Población y elegibilidad | PROPUESTA PARCIAL | `P*_τ2` elegible antes de Z y con `A_f,base*=0` para apertura; `P*_F` subgrupo basal sin alternativa funcional substituible. F*, validación, indeterminados y regla de inclusión siguen abiertos.
| S4R-15 | No interferencia/unidades | PROPUESTO | UE=UA y ausencia de interferencia son estipulaciones sintéticas, no hechos generales; definir spillovers/recursos compartidos |
| S4R-16 | Heterogeneidad y efectos colaterales | ABIERTO | Definir análisis preespecificados; no reinterpretar exclusión después de ver resultados |
| S4R-17 | Tamaño y réplicas | PROVISIONAL | N=2000 total por réplica, 1:1 y 1000 réplicas son valores ilustrativos no justificados |
| S4R-18 | XSYNC | ABIERTO | Cierre independiente documentado; XSYNC-138-01 y XSYNC-138-02…10 no se consideran cerrados por este documento |

### 6.1 Pruebas S4-R identificadas

El documento C10-S incluye las pruebas S4R-01…S4R-18. La aceptación exige convertir cada ID en ficha normalizada y comprobar que discrimina su escenario, incluida la contradicción p0/C_dep,0, primera etapa nula/débil, no aplicabilidad, no selección, rutas alternativas, cambios de Value de alternativas, filtración por Outcome/Value y preservación de ΔT_acc completo. La lista existente no equivale a ejecución ni PASS.

## 7. Contratos y pruebas: inventario que debe cerrarse

| Familia | Estado documental | Contrato mínimo pendiente |
|---|---|---|
| EQ | Catálogo de pruebas en C10-S | Equivalencia/identidad, versiones, deduplicación y fixtures |
| EX | Catálogo de exclusividad | Universo cerrado, rutas alternativas, F*, cobertura y criterios de rechazo |
| TG | Generación transformacional | Estado, condiciones, precondiciones, composición, horizonte y salida exacta |
| SR | Escenarios causales/sintéticos | DGP completo, parámetros, asignación, estimandos y resultado esperado |
| CV | Validez/constructo | A_f/T_acc/ΔT_acc, medición ciega, fiabilidad, sensibilidad |
| V | Outcome/Value | Regla independiente, no circularidad, V_real/V_potential |
| INT-01…08 | Pruebas integradas propuestas | Unidad común, datos por rol, truth oculto, salida extremo a extremo |
| S4R-01…18 | Escenarios S4-R | Fichas de aceptación completas y reglas de inferencia |
| POL-01…10 | Atribución de política / cobertura XSYNC | Condiciones para interpretar ITT_Z como θ_Af(q*), detectar vías directas, soporte, Value, δ/ε y alcance sintético |
| P182-01…12 | Solo IDs y resumen de contenido | Recuperar texto fuente y las 12 fichas originales |
| P183-01…13 | Solo IDs y resumen de contenido | Recuperar texto fuente y las 13 fichas originales |

Ficha mínima común obligatoria:

`test_id, objective, fixture_version, unit_id, initial_state, inputs_by_role, hidden_truth, expected_output, assertions, tolerance, failure_codes, evidence_artifacts, reproducibility_hash`.

Los campos `hidden_truth` solo son accesibles al generador y al evaluador independiente; nunca al módulo cuya capacidad se evalúa. Cada prueba termina en PASS, FAIL o INDETERMINATE, con justificación y evidencia archivada.

## 8. XSYNC y revisión independiente

**Corrección de recuperación:** el texto íntegro de XSYNC-138-01…10 sí se encuentra en C10-S §25.2; sus estados y respuestas parciales aparecen en §§25.4, 26.10, 27.8 y 28.9. Se ha creado `C10_S_XSYNC_138_CLOSURE_TRACKER_DRAFT_001.md`, que registra hallazgo original, respuesta documental, pendientes y criterios de cierre.

Estado actual:
- XSYNC-01: respuesta documental en §§26–27, pero P0 y formalmente abierto hasta revisión independiente.
- XSYNC-02: separación q/Value propuesta; cierre global pendiente.
- XSYNC-03: A_f como proyección focal, ΔT_acc completo preservado; auditar globalmente y cerrar AUD-001.
- XSYNC-04: separación L_c/L_m y soporte por historia propuestos; q* y positividad aún abiertos.
- XSYNC-05: θ_A^dyn permanece marcador no estimable; verificar usos globales.
- XSYNC-06: distinción de equivalencia/versiones y VER-01…06 documentada; pruebas no ejecutadas.
- XSYNC-07: estados de trayectoria ampliados; cobertura no probada.
- XSYNC-08: separación entre dictamen metodológico y conclusión científica en curso; contrato de salida pendiente.
- XSYNC-09: regla δ/ε de clasificación incompleta como contrato de salida.
- XSYNC-10: ampliación documental de trayectoria, pero cobertura por pruebas pendiente.

No se declara cerrado ningún hallazgo. La recuperación del texto no equivale a resolución. La auditoría independiente debe comprobar DGP, variables, estimandos, contratos, no filtración, límites y casos adversariales, registrando autor/rol, fecha, versión, evidencia y resolución.

## 9. Puertas de cierre y secuencia de trabajo

| Gate | Requisito | Condición PASS |
|---|---|---|
| G0 — Integridad histórica | Recuperar fuentes y decisiones 165–183 | Trazabilidad primaria; lagunas restantes explícitas |
| G1 — Coherencia causal | C10-D1 ↔ C10-S | Estimandos, población, intervención, régimen y Value coherentes |
| G2 — Coherencia transformacional | A_f, T_acc, ΔT_acc, Reach, trayectorias | Definiciones y actualizaciones completas; sin sustitución de constructos |
| G3 — Identificación | ITT, θ_A(q), IV/LATE, q/g, vías alternativas | Cada afirmación ligada a estimando y supuestos defendibles |
| G4 — Contratos | AUD-003…008, INT, S4R, P182/P183 | Fichas completas con PASS/FAIL/INDETERMINATE determinables |
| G5 — Reproducibilidad cuantitativa | AUD-009…012 y trazabilidad | Parámetros justificados, precisión, hashes, roles y decisiones versionados |
| G6 — Revisión independiente | XSYNC y auditoría cruzada | Hallazgos resueltos o límites aceptados explícitamente |
| G7 — Freeze documental | Todos los gates anteriores | Aprobación explícita, versión congelada y manifiesto de artefactos |

Orden operativo recomendado:

1. Recuperar fuentes originales 165–183 y los textos XSYNC faltantes.
2. Construir decision log con decisiones propuestas/aceptadas/sustituidas y referencias.
3. Resolver AUD-001/002 y XAUD-001/002: objeto de intervención, política factible, q/g y estimando.
4. Armonizar C10-D1 y S4-R: ITT frente a θ_A(q), poblaciones, horizonte, Value y condiciones.
5. Cerrar XAUD-003…006 y el DGP temporal, snapshots, aplicabilidad y ejecución.
6. Resolver AUD-004…008 y convertir INT/S4R en contratos completos.
7. Recuperar y cerrar P182/P183, AUD-009…012 y XSYNC.
8. Realizar auditoría independiente; corregir notación y documentación.
9. Decidir freeze documental. Solo después, si se solicita expresamente, tramitar autorización separada de implementación/ejecución.

## 10. Criterios de decisión científica y límites

La matriz no predetermina que el experimento deba “demostrar” C10. Los resultados válidos siguen siendo:

- contribución causal específica identificada dentro de un ámbito delimitado;
- evidencia adversa que limite/refute una predicción preespecificada en ese ámbito;
- efecto de paquete/ITT identificado, pero atribución a accesibilidad no identificada;
- identificación insuficiente;
- fallo de validez/medición o de la propia arquitectura sintética.

Un PASS de C10-S solo acreditaría que el protocolo sintético discrimina los escenarios y recupera las verdades que el DGP de referencia permite recuperar. No demostraría que ΔT_acc causa Value en sistemas reales.

## 11. Dictamen de control

**ESTADO GLOBAL: CIERRE DOCUMENTAL NO ALCANZADO.**

Se dispone de una base integrada suficiente para trabajar sin reiniciar C10-D1/C10-S: fuentes rectoras identificadas, consolidación hasta la sección 164, auditorías AUD-001…012 y XAUD-001…007, matriz S4-R y límites de recuperación 165–183. Sin embargo, los bloqueos críticos permanecen abiertos; los contratos de prueba no están completos; las fuentes originales 165–183 y XSYNC no están íntegramente recuperadas; no hay revisión independiente ni ejecución.

Este documento consolida el control del trabajo y evita que se pierdan los pendientes. No declara el diseño listo para freeze, no cambia decisiones científicas y no sustituye la recuperación de fuentes primarias.


## 12. Recuperación de la fuente conversacional 165–183 (2026-11-04)

Se recibió y examinó el archivo `Notes_261104_163033.docx`, que contiene el intervalo desde la sección 165 hasta inmediatamente antes de la 184. La cobertura recuperada incluye DGP-S4R-D1/D2 (166–168), supuestos IV (169), exclusión y adversariales (170), sensibilidad δ/γ (171), LATE/heterogeneidad (172–173), perfiles y potenciales (174–175), DGP adversariales (176), estimación (177), protocolo sintético (178), Value (179–180), medición independiente (181), validez (182) y missingness/censura (183).

El registro de contenido y alertas se documenta en `C10_S_RECOVERY_165_183_SOURCE_REGISTER_DRAFT_001.md`. La fuente original fue recibida y leída; la copia íntegra DOCX y la transcripción literal completa todavía no están persistidas en GitHub. Por tanto, G0 pasa de “fuente no localizada” a “fuente recibida y cobertura recuperada”, pero **no** a “persistencia íntegra verificada”.

Decisiones que deben conservarse como propuestas, no aceptarse automáticamente: D1 principal condicionado y D2 contraste; D1 p0=.20/p1=.80 por provisión ordinaria posterior a la asignación con C_dep,base=0; Wald/LATE local, no ATE; δ/γ y vías alternativas pueden invalidar exclusión; Value vectorial provisional; ausencia de A/O/V no se recodifica como cero. P181/P182/P183 siguen sin ejecución y requieren normalización/cotejo de contratos.

La sección 184 es solo una propuesta de siguiente paso y queda fuera de la fuente 165–183. No se declara cierre causal, aprobación del DGP, freeze ni autorización de ejecución.


## 13. Precisión de contratos P182/P183 tras recuperación de fuente (2026-11-04)

El registro de pruebas `C10_S_TEST_CONTRACT_REGISTER_DRAFT_001.md` incorpora ahora las tablas completas recuperadas P182-01…12 y P183-01…13, con sus criterios de aceptación textuales. Esto sustituye la descripción anterior de “solo IDs y resumen” en cuanto a la disponibilidad documental de esas fichas.

El cambio es documental: los criterios todavía deben convertirse en fixtures, entradas/salidas, tolerancias, códigos de fallo y evidencia reproducible. Todas las pruebas siguen propuestas y no ejecutadas. La sección 183 requiere además dictámenes separados para ITT-O, ITT por dimensión de V, mediación por A, LATE-V, efecto residual e índice agregado si existe.


## 14. Corrección de precedencia tras auditoría integral (2026-11-04)

La recomendación de §6.2 S4R-08 (DGP limpio p0=0, p1=.80, relegando p0>0 a contaminación) queda sustituida para la especificación candidata, no borrada: D1 principal condicionado tiene C_dep,base=0, p0=.20 y p1=.80 postasignación, primera etapa .60; D2 contraste tiene p0=0 y p1=.80, primera etapa .80. D1 no es contaminación si la provisión ordinaria en control es parte del comparador preespecificado. Si no, no se acepta como principal.

G0: la fuente 165–183 fue recibida y examinada; persistencia íntegra del DOCX y transcripción literal completa siguen pendientes. P182-01…12 y P183-01…13: criterios recuperados e incorporados al registro; definidos documentalmente, no implementados ni ejecutados. XSYNC-138-01…10: contenido localizado en el documento maestro histórico; revisión independiente y resolución formal pendientes. El capítulo 53 y la auditoría integral armonizan la especificación candidata, pero no cierran automáticamente AUD/XAUD ni G1–G7.

Estado: especificación candidata armonizada; decisiones científicas no aprobadas; contratos incompletos; revisión independiente no realizada; no freeze, implementación ni ejecución.


## 15. Cierre parcial de diseño de B: propuesta operacional candidata

La recuperación de §52.2 del documento maestro permite concretar la estructura probabilística de B sin inventar una política de ausencia total para D1:

| Escenario | Intento control | Intento tratamiento | C_dep final control | C_dep final tratamiento |
|---|---:|---:|---:|---:|
| D1 | .25 | 1.00 | .20 | .80 |
| D2 | 0 | 1.00 | 0 | .80 |

Una tasa conjunta de éxito técnico de .80 condicionada al intento reconcilia los valores. Es una factorización derivada, no un parámetro original recuperado. Los componentes técnicos permanecen separados y no se presume independencia.

**Estado de OPEN-C10-001:** parcialmente operacionalizada documentalmente; sigue ABIERTA por falta de decisión sobre comparador D1, actor, recepción, versiones, protocolo de verificación, crossover, factibilidad y vías colaterales. No se declara cerrada.


## 16. Cierre parcial de q_X*: especificación y límites

**Especificado documentalmente:** q_X* como distribución basal (P^*(X,H_0,C_c\mid E=1,C_{dep,0}=0,A_{f,0}^*=0)); elegibilidad preasignación; separación entre C_c y C_dep; cuatro estados de condiciones constitutivas; soporte por historia para ambas políticas; reglas de restricción ex ante/no identificación; q_L* solo para variables postasignación indispensables bajo intervención secuencial.

**OPEN-C10-002 sigue ABIERTA:** faltan distribución concreta P*, composición y categorías de X/H0, inventario/umbrales C_c, unidad y posible interferencia, probabilidades de asignación, estratos/pesos, ventanas, rutas equivalentes y Value. No hay datos para calcular soporte numérico ni para afirmar positividad empírica.

No se cierra DEC-C10-012 ni se declara freeze.


## 17. Unidad experimental, asignación e interferencia

**Propuesta:** UE=UA=instancia sintética independiente; UO son snapshots repetidos. La independencia requiere ausencia de recursos, agentes, información, infraestructura y canales compartidos. Si hay agrupación, definir clúster y asignar por clúster o modelar exposición; inferencia y N efectivo respetan la UA real. Con spillover no modelado, no interpretar ITT/Wald individual convencional como efecto causal focal.

**OPEN-C10-005 permanece ABIERTA:** faltan inventario del entorno, mapa de recursos/agentes/red, decisión sobre asignación individual o por clúster, esquema de aleatorización y probabilidades. UE=UA no se presenta como hecho ni como decisión aprobada.


## 18. F*, equivalencia funcional y poblaciones

**Reconciliación candidata:** P*_τ2 estudia apertura de identidad transformacional y no excluye automáticamente alternativas funcionales; P*_F es subconjunto sin rutas alternativas substituibles respaldadas en universo/G/H/C0 especificados. La regla histórica §48.6 se interpreta para P*_F conforme a §50.7; no se elimina el texto original.

F* debe fijarse antes de Z con objetivo técnico, entrada/salida, restricciones, tolerancias, horizonte, granularidad, contexto y estándar de evidencia independientes de Outcome/Value. Cada ruta conserva juicios separados de accesibilidad, aplicabilidad y substituibilidad; identidad ≠ equivalencia funcional. F_alt,0=0/1/?; “no encontrado” no es ausencia sin cobertura suficiente. Alternativa basal estable no viola automáticamente exclusión; si B la altera/activa, se compromete LATE focal y queda ITT de paquete.

**OPEN-C10-003 sigue ABIERTA:** F*, umbrales, H/G/C0, universo/cobertura, recursos, E1–E4 por tipo, adjudicación, sensibilidad/error de clasificación y q_X,F*/pesos no están fijados. OPEN-C10-006 también permanece abierta.


## 19. Cierre parcial del contrato de medición A_f*, C_dep y ΔT_acc

**Propuesta incorporada documentalmente:** se separan verdad DGP y medición observada; C_dep se conserva como conjunción técnica verificable; A_f* requiere identidad válida, C_dep y predicados de acceso focal; App_f se mide aparte; D_f* es apertura basal→post; T_acc/ΔT_acc conserva identidades/versiones, relaciones, condiciones, validez/cobertura y estado. La clasificación observada usa 1/0/? y no fuerza indeterminados. Se fija orden basal pre-Z y snapshot post antes de conocimiento/selección/ejecución.

**No se cierra:** clasificación de condiciones, definición/versionado de τ2, estándar de evidencia, adjudicación, concordancia, validación, error diferencial, cobertura del universo y comparabilidad de snapshots.

| Hallazgo | Estado tras esta propuesta | Criterio aún necesario |
|---|---|---|
| AUD-004 ΔT_acc relacional | PROPUESTA PARCIAL; ABIERTO | Identidades/versiones, relaciones, condiciones, validez, estado, reglas de correspondencia y fixtures |
| XAUD-003 Acc/App/Reach/Exec | PROPUESTA PARCIAL; ABIERTO | Clasificación completa y validación de predicados/tiempos |
| XAUD-004 Z/B/W/S/C_dep/A_f truth-observed | PROPUESTA PARCIAL; ABIERTO | Evidencia, roles, errores, validación y casos adversariales |
| OPEN-C10-004 medición de accesibilidad/ΔT_acc | ABIERTA | Operacionalización técnica, umbrales, fuentes, cobertura y sensibilidad |

No se declara validez de constructo, aceptación científica, freeze ni autorización de implementación o ejecución.


## 20. Matriz de clasificación de condiciones — cierre parcial

**Resultado documental:** se incorpora una clasificación provisional de C_install, C_integrity, C_compat, C_oper, C_auth_base, C_resource, C_capacity, C_info, C_domain, C_other, S0 y eventos K/selección/ejecución. Se propone retirar C_other como comodín y separar acceso, aplicabilidad, provisión, conocimiento y ejecución.

| Hallazgo | Estado | Criterio pendiente |
|---|---|---|
| AUD-011 C_c vs L / rol causal | PROPUESTA PARCIAL; ABIERTO | Descomponer variables mixtas, validar tiempos, unidad, papel causal y evidencia |
| XAUD-003 Acc/App/Exec | PROPUESTA PARCIAL; ABIERTO | Aprobar semántica, completar estados y pruebas de transición |
| XAUD-004 Z/B/W/C_dep/A_f | PROPUESTA PARCIAL; ABIERTO | Resolver clasificación, escenarios de autorización y errores de medición |
| AUD-001/002 y XAUD-001/002 | ABIERTOS | Coherencia final de q/g y manipulación causal físicamente realizable |
| OPEN-C10-004 | ABIERTA | Definición empírica, estándares, cobertura, umbrales y validación |

La matriz no aprueba la ecuación depurada ni cierra constructos. La modalidad A continúa siendo la candidata preferida; cualquier manipulación de autorización, recursos, capacidad, información o conocimiento exige identificar vías adicionales o declarar efecto de paquete.


## 21. Nivel sistema/unidad — cierre parcial

| Hallazgo | Estado | Pendiente |
|---|---|---|
| AUD-010 unidad×variable×tiempo | PROPUESTA PARCIAL; ABIERTO | Fijar unidad, nivel Z/B, estructura jerárquica, interferencia y roles temporales |
| AUD-011 clasificación C_c/L | PROPUESTA PARCIAL; ABIERTO | Confirmar frontera, recursos, predicados mixtos y niveles |
| XAUD-001 régimen q/políticas g | ABIERTO / CRÍTICO | Definir si g cambia capacidad estructural, relación de acceso o ambas; contrafactuales factibles |
| XAUD-002 intervención autónoma A_f | ABIERTO | Precisar política físicamente realizable y vías colaterales |
| XAUD-003/004 | PROPUESTA PARCIAL; ABIERTO | Aplicar la distinción de niveles a Acc/App/Exec y Z/B/C_dep/A_f |
| OPEN-C10-004 | ABIERTA | Operacionalizar frontera, recursos, evidencia, cobertura y validación |

La distinción T_cap/T_acc(i) es auxiliar y no cambia el Core. No se aprueba todavía la ecuación de §59 ni se declara identificada la contribución causal.


## 22. Frontera, unidad e intervención — cierre parcial

| Elemento | Estado | Condición pendiente |
|---|---|---|
| UE=UA=instancia completa | PROPUESTA; NO APROBADA | Auditar mecanismo material de B y confirmar independencia entre instancias |
| UO longitudinal | PROPUESTA COHERENTE | Confirmar T0–T9 y no contar snapshots como unidades independientes |
| B_sys | PROPUESTA | Inventario de componentes/dependencias externas y recursos |
| T_cap/T_acc | DISTINCIÓN CONSERVADA | Coincidencia solo condicional si no hay subunidades diferenciadas |
| Z→B | PROPUESTA | Definir actor, acción, destinatario, versión y recepción |
| q_X* | PROPUESTA | Compatibilidad con intervención y soporte por historia |
| P*_τ2/P*_F | RECONCILIACIÓN PROPUESTA | Criterios basales y clasificación sin variables postratamiento |
| Interferencia | ESCENARIO PRIMARIO AISLADO + ADVERSARIAL | Verificar no compartir recursos/canales; modelar clúster/exposición en adversarial |

**OPEN-C10-005 permanece ABIERTA.** XAUD-001/002 y AUD-010/011 siguen abiertos. Este bloque no demuestra identificación causal ni autoriza freeze/ejecución.


## 23. Intervención material B — cierre parcial

| Elemento | Estado | Pendiente |
|---|---|---|
| B0/B1 | ESPECIFICACIÓN CANDIDATA | Identidad/versiones y parámetros concretos del artefacto sintético |
| Actor/destinatario | ROL SINTÉTICO PROPUESTO | Definir protocolo ejecutable solo tras autorización |
| C_dep* | CONJUNTO DE CUATRO COMPONENTES | Evidencias, fixtures, umbrales y adjudicación |
| B→A_f* | MECANISMO PROPUESTO | Validar que todos los predicados focal se satisfacen y no hay vía directa |
| Vías colaterales | INVARIANTES ENUMERADAS | Auditoría adversarial; si cambian, reclasificar paquete |
| Fallo/contaminación | REGLAS DOCUMENTALES | Definir tasas/escenarios del DGP sin inventar valores |
| ITT | ASIGNACIÓN DE POLÍTICA | No confundir con efecto mediado/efecto de A_f* |

OPEN-C10-005 y XAUD-001/002 permanecen ABIERTOS. La especificación no es un tratamiento congelado ni una prueba de exclusión.


## 24. Medición focal y ΔT_acc — cierre parcial

| Elemento | Estado | Pendiente |
|---|---|---|
| C_dep* | MECANISMO TÉCNICO | No es suficiente para declarar accesibilidad |
| A_f* | PREDICADO ESTRUCTURAL PROPUESTO | Fijar predicados por clase, fuentes y adjudicación |
| A_f,obs | MEDICIÓN SEPARADA | Validación, error diferencial, límites y sensibilidad |
| D_f* | TRANSICIÓN BASAL-POST | Baseline confirmado y ventanas temporales |
| ΔT_acc* | OBJETO ESTRUCTURADO | Catálogo, G, frontera, versionado y comparabilidad |
| h_f | PROYECCIÓN FOCAL | No confundir con el diff completo |
| App/Know/Select/Exec | SEPARADOS | Verificar en DGP y diccionario longitudinal |
| Verdad vs analizador | CANALES SEPARADOS | Pruebas de no filtración y validación |

**XSYNC-138-03 y AUD-001 permanecen abiertos formalmente.** AUD-004/005/007 y OPEN-C10-005 no quedan cerrados. Es una reconciliación de diseño propuesta, no evidencia de medición válida ni autorización de ejecución.


## 25. Clasificación temporal-causal — cierre parcial

| Elemento | Estado | Pendiente |
|---|---|---|
| Condiciones basales | CLASIFICACIÓN PROPUESTA | Inventario definitivo y evidencia/adjudicación |
| Condiciones constitutivas post-Z | MEDIADORES/CO-INTERVENCIONES POTENCIALES | Registrar cambios y vías alternativas |
| C_dep | MECANISMO TÉCNICO MANIPULABLE | Resolver semántica de brazos B y .20/.80 |
| C_auth | BASAL INVARIANTE EN PRIMARIO | Separar propuesta histórica de intervención sobre autorización |
| Recursos/capacidad/información | COMPONENTES DESCOMPUESTOS | Especificaciones y ventanas |
| App_f / K / Select / Exec | DOWNSTREAM SEPARADOS | Verificar diccionario longitudinal |
| VALID/cobertura | PROCESO EPISTÉMICO | Protocolo de missingness/error diferencial |
| Ajuste postratamiento | REGLA DE NO AJUSTE DOCUMENTADA | Definir análisis longitudinal si hay confusión inducida |

**AUD-011 y XAUD-003/004/006 permanecen abiertos.** La clasificación documental no cierra la identificación ni valida la medición.


## 26. Política B — reconciliación D1/D2 (cierre semántico parcial)

| Elemento | Estado | Pendiente |
|---|---|---|
| Distinción D1/D2 | RECONCILIADA DOCUMENTALMENTE | Aprobación del escenario |
| p0=.20 / p1=.80 | ESTADO FINAL C_dep | Calibración y verificación |
| W_attempt | D1: .25/1; D2: 0/1 | Actor, disparador y registro |
| S_success condicional | .80 propuesto | Especificación conjunta y validación |
| B0 sin provisión | D2 solamente | Confirmar D2 como contraste |
| D1 como primario | PRINCIPAL CONDICIONADO | Justificar control ordinario |
| A_f*/D_f* | No inferidos desde C_dep | Calcular desde predicados completos |
| OPEN-C10-001/005 | ABIERTAS | Aprobación, materialización y revisión independiente |

La ambigüedad semántica entre «política probabilística» y «brazo determinista» queda aclarada: las políticas regulan la probabilidad de intento y el éxito técnico es posterior; los valores .20/.80 son probabilidades de estado final C_dep. No queda aprobado el comparador ni la tasa de éxito condicional.


## 27. Selección D1/D2 — estado de legitimidad y cierre

| Elemento | Estado | Evidencia/pendiente |
|---|---|---|
| D1 como contraste incremental | DEFINIDO | Provisión programada frente a provisión ordinaria |
| Justificación del régimen ordinario D1 | NO ACREDITADA | Fuente, frecuencia .25/.20, población y contexto |
| D2 como contraste mecanístico | DEFINIDO | Provisión programada frente a ausencia de intento focal |
| D2 como candidato preferente provisional | RECOMENDADO, NO APROBADO | Depende de objetivo explícito y ausencia de provisión de fondo |
| ITT_D1 / ITT_D2 | DISTINTOS | No agrupar ni promediar |
| Primera etapa | PENDIENTE POR VARIABLE Y ESCENARIO | C_dep, A_f,post*, D_f, ΔT_acc |
| LATE/Wald | PENDIENTE POR ESCENARIO | No asumir mismos cumplidores ni exclusión |
| Selección primaria | ABIERTA | Aceptación científica explícita |
| OPEN-C10-001/005 | ABIERTAS | Política, mecanismo, calibración y revisión independiente |

La recomendación no cambia retrospectivamente los datos ni parámetros históricos. D1 no se descarta; se retira únicamente su presunción de primario mientras falte justificación del régimen ordinario.
