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
| REC-CAUS-04 | Intervención | Intervenir componentes implementables; no asignar abstractamente T_acc; políticas factibles y versiones | Histórico: Z_A → C_auth → A_f* fue una modalidad propuesta de intervención sobre autorización. Para D2 primario candidato, DEC-C10-067 y maestro §§59.2/59.4/64.5 fijan C_auth,base=1 basal/común/invariante y B como provisión técnica focal; permisos técnicos B separados de autorización normativa funcional | La contradicción semántica de alcance queda delimitada: la modalidad Z_A→C_auth se conserva como alternativa histórica/adversarial y no pertenece al D2 actual sin decisión explícita. Sigue ABIERTO: q frente a g, legitimidad del comparador, fuente/alcance/vigencia de C_auth,base y prueba de que PROV-06 se cumple materialmente |
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
| G6 — Revisión externa/freeze técnico | XSYNC, auditoría cruzada y controles que requieran independencia | Se activa cuando se prepare freeze técnico o claims de reproducibilidad/validación; no bloquea autoauditoría ni apertura web as is |
| G7 — Freeze documental | Todos los gates anteriores | Aprobación explícita, versión congelada y manifiesto de artefactos |

Orden operativo recomendado:

1. Recuperar fuentes originales 165–183 y los textos XSYNC faltantes.
2. Construir decision log con decisiones propuestas/aceptadas/sustituidas y referencias.
3. Resolver AUD-001/002 y XAUD-001/002: objeto de intervención, política factible, q/g y estimando.
4. Armonizar C10-D1 y S4-R: ITT frente a θ_A(q), poblaciones, horizonte, Value y condiciones.
5. Cerrar XAUD-003…006 y el DGP temporal, snapshots, aplicabilidad y ejecución.
6. Resolver AUD-004…008 y convertir INT/S4R en contratos completos.
7. Recuperar y cerrar P182/P183, AUD-009…012 y XSYNC.
8. Continuar auditoría interna asistida y corregir notación/documentación; declarar siempre AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT. No exigir R1/R2 para continuar.
9. Preparar revisión externa cuando se plantee freeze técnico o publicación de claims de reproducibilidad/validación. La web germen as is sigue un gate independiente de transparencia y puede abrir antes del cierre científico, con límites y estados explícitos.
10. Decidir freeze documental/técnico solo para el alcance que realmente lo requiera. Cualquier implementación/ejecución requiere autorización separada.

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
| B0 sin provisión | D2 solamente | Verificar ausencia real de provisión focal de fondo; D2 es primario candidato por DEC-C10-066 |
| D1 como primario | SUPERSEDIDO POR DEC-C10-066 | D1 queda secundario; justificar el control ordinario para interpretar el contraste incremental |
| A_f*/D_f* | No inferidos desde C_dep | Calcular desde predicados completos |
| OPEN-C10-001/005 | ABIERTAS | Aprobación, materialización y revisión independiente |

La ambigüedad semántica entre «política probabilística» y «brazo determinista» queda aclarada: las políticas regulan la probabilidad de intento y el éxito técnico es posterior; los valores .20/.80 son probabilidades de estado final C_dep. No queda aprobado el comparador ni la tasa de éxito condicional.


## 27. Selección D1/D2 — estado de legitimidad y cierre

| Elemento | Estado | Evidencia/pendiente |
|---|---|---|
| D1 como contraste incremental | DEFINIDO | Provisión programada frente a provisión ordinaria |
| Justificación del régimen ordinario D1 | NO ACREDITADA | Fuente, frecuencia .25/.20, población y contexto |
| D2 como contraste mecanístico | DEFINIDO | Provisión programada frente a ausencia de intento focal |
| D2 como escenario primario candidato | ACEPTADO POR DEC-C10-066 | Verificar objetivo ausencia-vs-provisión y ausencia real de provisión focal de fondo |
| ITT_D1 / ITT_D2 | DISTINTOS | No agrupar ni promediar |
| Primera etapa | PENDIENTE POR VARIABLE Y ESCENARIO | C_dep, A_f,post*, D_f, ΔT_acc |
| LATE/Wald | PENDIENTE POR ESCENARIO | No asumir mismos cumplidores ni exclusión |
| Selección primaria | RESUELTA: D2 PRIMARIO CANDIDATO / D1 SECUNDARIO | No reabrir precedencia; legitimidad y parámetros siguen abiertos |
| OPEN-C10-001/005 | ABIERTAS | Política, mecanismo, calibración y revisión independiente |

La decisión DEC-C10-066 cambia la precedencia vigente, no los datos ni parámetros históricos. D1 no se descarta: queda como escenario secundario y su régimen ordinario debe justificarse para interpretar el contraste incremental. Las condiciones técnicas y causales de legitimidad de D2 siguen abiertas.


## 28. Primera etapa técnica y derivación de accesibilidad — reconciliación documental

| Elemento | Estado | Pendiente |
|---|---|---|
| C_install/C_integrity/C_compat/C_oper | DEFINICIÓN CONJUNTA PROPUESTA | Evidencia, versiones, protocolo, ventana y adjudicación por componente |
| C_dep* | CONJUNCIÓN DE CUATRO PREDICADOS | Distribución conjunta; no asumir independencia |
| s=.80 | PROBABILIDAD CONJUNTA CONDICIONAL CANDIDATA | No empírica; sensibilidad y justificación |
| A_f* | PREDICADO ESTRUCTURAL ID/REL/COND/AUTH/RES/DEP/¬BLOCK | Clasificación operativa, fuentes, cobertura y reglas por clase |
| VALID/cobertura | PROCESO EPISTÉMICO | No introducir en truth estructural; validar observación |
| Ruta única | ESTIPULACIÓN DEL DGP AISLADO | Inventario de rutas alternativas y prueba de cobertura |
| C_dep→A_f | EQUIVALENCIA CONDICIONAL | Solo si DEP=C_dep y demás predicados se satisfacen |
| FS_Cdep / FS_Af / FS_Df | ESTIMANDOS DISTINTOS | Calcular por D1/D2 y no transferir primeras etapas |
| .60 D1 / .80 D2 | PRIMERA ETAPA DE C_dep CANDIDATA | Coincide con A_f/D_f solo bajo condiciones explícitas |
| Fallo/indeterminado | REGLA 1/0/? PROPUESTA | Fixtures y validación de error diferencial |

**Dictamen:** avance documental sustantivo; no validación empírica ni cierre de OPEN-C10-001/007/008. No freeze, implementación, simulación ni ejecución.


## 29. Distribución conjunta y sensibilidad — reconciliación de cierre

| Elemento | Estado | Pendiente |
|---|---|---|
| p_abcd, 16 patrones | REQUISITO DE ESPECIFICACIÓN PROPUESTO | Tabla/generador confirmatorio |
| s=p1111 | UNA CELDA, NO DGP COMPLETO | Calibración y sensibilidad |
| Marginales m_i | NO IDENTIFICADAS POR s | Fuente/elección explícita |
| Dependencia | NO PRESUPUESTA | Familias y asociaciones |
| Fallos parciales | NO IDENTIFICADOS POR s | Conteos/patrones y medición |
| Fréchet | LÍMITES, NO IDENTIFICACIÓN | Marginales para estrechar límites |
| s=.60/.70/.80/.90 | MALLA EXPLORATORIA | Justificación de rango y resolución |
| D1/D2 | CALIBRACIÓN SEPARADA | No transferir distribuciones/estimandos |
| Heterogeneidad/versiones | PENDIENTE | Estratos basales y deriva temporal |
| Truth vs observación | SEPARACIÓN EXIGIDA | Pruebas de no filtración |

**Dictamen:** el éxito condicional no especifica el patrón de fallos. No cerrar calibración ni selección confirmatoria.


## 30. Fixtures y sensibilidad de primeras etapas

| Control | Estado propuesto | Criterio de cierre |
|---|---|---|
| FIX-01 | Cuatro tablas 16-celdas para s=.80 | Sumas=1, celdas no negativas, marginales verificadas |
| FIX-02 | Cuatro patrones de fallo diferenciados | Igual s no produce equivalencia artificial |
| FIX-03 | Escalado s-grid | p1111=s y masa residual=1−s |
| FIX-04 | D1 q0=.25, q1=1 | P0=.25s, P1=s, FS=.75s |
| FIX-05 | D2 q0=0, q1=1 | P0=0, P1=s, FS=s |
| FIX-06 | Consistencia de D1 control | .20 solo en s=.80 bajo q0=.25 |
| FIX-07 | A_f/D_f transfer | No transferir FS_Cdep sin supuestos §67.4 |
| FIX-08 | Intentos múltiples | Modelo secuencial explícito, no independencia automática |
| FIX-09 | Marginales fijas | Familia distinta y compatible con Fréchet |
| FIX-10 | Estado confirmatorio | Ningún fixture elegido sin revisión/decisión |

No se cierra calibración empírica ni selección primaria.


## 8. Seguimiento del Bloque 1 — arquitectura causal y estimandos (2026-11-04)

| ID | Punto | Evidencia incorporada | Estado | Criterio de cierre |
|---|---|---|---|---|
| CA-01 | Jerarquía C10-D1 / S4-R | Nuevo artefacto `C10_S_CAUSAL_ARCHITECTURE_RECONCILIATION_DRAFT_001.md`; DEC-C10-030 | PROPUESTA / ABIERTO | Aprobación expresa de θ_A(q), TE_Z/ITT_Z, ψ_B y LATE_f, con población/horizonte/Value. |
| CA-02 | q_X* / q_L* | Cotejo C10-D1 §§17, 25–26 y C10-S §44; DEC-C10-015 | PROPUESTA / ABIERTO | Variables basales, soporte, pesos y regla dinámica si q_L* fuera necesaria. |
| CA-03 | Intervención B y C_auth | Contraste de propuesta AUD-001/002 con DEC-C10-022/024 y DGP §§25–26 | CONTRADICCIÓN IDENTIFICADA / RESOLUCIÓN PROPUESTA | Decidir C_auth basal-invariante vs intervención conjunta; especificar si canal técnico cambia permisos. |
| CA-04 | D1/D2 | Fuente 165–183, DEC-C10-026, DGP §25, contratos CMP | NO RESUELTO | Justificar comparador para pregunta primaria y aceptar una jerarquía confirmatoria. |
| CA-05 | Vías directas/colaterales | C10-D1 §§26, 30; POL-01/02; XAUD-002 | ABIERTO | Aislamiento por diseño y escenarios adversariales con salida efecto paquete/no identificación. |
| CA-06 | Unidad/interferencia | DEC-C10-016/021; UNIT/BND contracts | PROPUESTA / ABIERTO | Frontera, recursos compartidos, asignación y mapa de exposición aprobados. |
| CA-07 | Value/horizonte/población | OPEN-C10-003/004; fuente 179–183 | ABIERTO | Regla Value, beneficiario, dimensiones, horizonte y población preespecificados. |

**Resultado del bloque:** arquitectura causal reconciliada a nivel de distinciones y propuesta candidata; no existe todavía contrato causal aprobado ni estimando final cerrado. No marcar AUD-001/002 o XAUD-001/002 como resueltos.


## 9. Seguimiento del Bloque 2 — población, F* y comparadores (2026-11-04)

| ID | Punto | Evidencia incorporada | Estado | Criterio de cierre |
|---|---|---|---|---|
| POP-01 | P*_τ2 | Maestro §§46/50/51/70 y nuevo artefacto de reconciliación | PROPUESTA / ABIERTO | Aprobación de regla pre-Z y definición observable de condiciones constitutivas. |
| POP-02 | P*_F | Maestro §§48–50/70; F_alt,0 y cobertura | PROPUESTA / ABIERTO | F* y universo/cobertura de rutas; ausencia respaldada y adjudicación. |
| POP-03 | Elegibilidad indeterminada | Maestro §47 y contrato nuevo | PARCIAL | Umbrales, instrumentos, adjudicación y sensibilidad de error conjunto. |
| POP-04 | D_f,0 vs C_dep,0 | Nuevo crosswalk de notación, maestro §70 y DGP §29 | CORRECCIÓN PROPUESTA | Búsqueda global, supersesión explícita y aprobación. |
| POP-05 | F* | Definición funcional recuperada en §48 | INCOMPLETA | S0/objetivo, aceptación, tolerancias, H/G/C0, recursos y validación. |
| POP-06 | D1/D2 | Fuente 165–168, DEC-C10-026, DGP §25, maestro §70 | PRECEDENCIA NO RESUELTA | Justificar comparador para pregunta primaria y aceptar decisión. |
| POP-07 | Unidad/interferencia | Maestro §45; DEC-C10-016/021 | CANDIDATA | Auditoría de frontera y recursos; aprobar UE/UA/exposición. |

**Resultado del Bloque 2:** se han reconciliado conceptualmente P*_τ2 y P*_F y se ha detectado una sobrecarga de notación basal. F* sigue incompleto y D1/D2 no se ha seleccionado. No cerrar OPEN-C10-001/003/005/007 ni afirmar elegibilidad operacionalizada.


## 10. Seguimiento del Bloque 3 — snapshots, ΔT_acc y evidencia (2026-11-04)

| ID | Punto | Hallazgo/propuesta | Estado | Criterio de cierre |
|---|---|---|---|---|
| SNAP-01 | ΔValidity mezclada en ΔT_acc* | §63.7 frente a §§64/67: evidencia/cobertura es epistémica | CONTRADICCIÓN DOCUMENTAL IDENTIFICADA; RESOLUCIÓN PROPUESTA | Aprobación de ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*) y ΔE_T separado; propagación global. |
| SNAP-02 | Snapshot estructural | S_T*=(U*,R*,C*,X*) | PROPUESTA | Definición de cada campo, frontera, unidad, tiempo y truth/observed. |
| SNAP-03 | Identidad y versiones | Mapping M previo a diff | ABIERTO | Catálogo, IDs canónicos, equivalencia/versionado y reglas de alta/baja. |
| SNAP-04 | Comparabilidad | Diff requiere G/frontera/catálogo compatibles | ABIERTO | Contrato y oráculo para comparabilidad y Match=?. |
| SNAP-05 | ΔT_acc y cambio focal | D_f* es proyección h_f, no sustituto de ΔT_acc | PROPUESTA | Pruebas metamórficas focal/no focal y revisión matemática. |
| SNAP-06 | Observación/filtración | Analizador ve E_T, no truth; devuelve 1/0/? | PARCIAL | Fixtures, error diferencial, cegamiento y auditoría independiente. |
| SNAP-07 | Reach/Value | Relación con Reach_possible, S5-F/S5-C y Value | ABIERTO | Reconciliación de estimandos, no circularidad y composición. |

**Resultado del subbloque:** inconsistencia detectada y propuesta de resolución persistida; no declarar AUD-004 cerrado. Las pruebas SNAP-01…15 son contratos documentales, no ejecutados.


## 11. Seguimiento del Bloque 3 — identidad, versionado y matching (2026-11-04)

| ID | Punto | Hallazgo/propuesta | Estado | Criterio de cierre |
|---|---|---|---|---|
| ID-01 | Identidad semántica vs versión técnica | TID/SID/RID/EID separados | PROPUESTA | Taxonomía mínima acordada con catálogo/Core |
| ID-02 | Continuidad de identidad | Firma semántica y tolerancias por clase | ABIERTO | Contratos, umbrales y adjudicación aprobados |
| ID-03 | IDs y provenance | IDs opacos persistentes; hash no define identidad | PROPUESTA | Esquema serializable, reglas alta/retirada/alias |
| ID-04 | Matching entre snapshots | Exact ID, alias, versión, candidato, adjudicación | ABIERTO | Regla reproducible, cegamiento y evaluación de error |
| ID-05 | Split/merge | Mapping 1:N/N:1 no equivale a 1:1 | ABIERTO | Reglas composicionales y mapping validado |
| ID-06 | Granularidad/frontera | Diff requiere G/b/catálogo compatibles | PARCIAL | Fijar G/frontera por DGP y fixtures de no comparabilidad |
| ID-07 | Eventos diff | ADD/REMOVE/MODIFY/VERSION/SPLIT/MERGE/REWIRE/STATE/UNKNOWN | PROPUESTA | Oráculos y reglas de evento por U/R/C/X |
| ID-08 | Identidad focal τ2 | Matching requisito de D_f* | PROPUESTA | Congelar identidad/versión focal ex ante y probar cambios |
| ID-09 | Error de matching | Falsos matches, misses, unresolved y diferencial | ABIERTO | Validación independiente y sensibilidad |
| ID-10 | Efectos sobre estimandos | No confundir continuidad semántica con equivalencia causal | ABIERTO | Crosswalk con IV, q, Reach, Value y C10-D1 |

**Dictamen:** contrato redactado, pero no operacionalizado para el DGP. No cerrar AUD-004 ni XSYNC-138-03/06. Los contratos ID-01…15 son documentales, no pruebas ejecutadas.


## 12. Seguimiento del Bloque 3 — Reach y trayectorias (2026-11-04)

| ID | Punto | Propuesta | Estado | Criterio de cierre |
|---|---|---|---|---|
| REACH-01 | Definición truth/obs | Separar Reach_H* y Reach_H,obs | PROPUESTA | Diccionario global armonizado |
| REACH-02 | Composición por ruta | T_acc*, App*, relaciones, recursos, temporalidad | PROPUESTA | Reglas por clase de transformación |
| REACH-03 | Lógica trivalente | Conjunción 1/0/? por ruta | PROPUESTA | Oráculos y pruebas |
| REACH-04 | Rutas alternativas | Disyunción; una ruta confirmada basta | PROPUESTA | Cobertura de alternativas validada |
| REACH-05 | No alcanzabilidad | Exige universo/cobertura exhaustivos | ABIERTO | Prueba de exhaustividad y límites |
| REACH-06 | Truncamiento | Nunca equivale a Reach=0 | PROPUESTA | Fixtures de límite computacional |
| REACH-07 | Horizonte y ciclos | H/G/temporalidad/terminación ex ante | ABIERTO | Parámetros DGP y regla de ciclos |
| REACH-08 | Snapshot dinámico | Actualizaciones inmutables dentro de H | ABIERTO | Contrato de eventos y reloj |
| REACH-09 | No filtración | Selección/ejecución/O/Value downstream | PROPUESTA | Auditoría global y pruebas adversariales |
| REACH-10 | Identificación/cobertura | ? ante catálogo o mapping incompleto | ABIERTO | Validación independiente de cobertura/error |

**Dictamen:** propuesta documental incorporada; AUD-005 y AUD-007 permanecen abiertos. No declarar cierre ni cobertura validada.


## 13. Seguimiento del Bloque 3 — inventario finito del DGP y cobertura Reach

| ID | Punto | Propuesta/hallazgo | Estado | Criterio de cierre |
|---|---|---|---|---|
| INV-01 | Estados S0/S1/S2/SF | Alfabeto abstracto de fixture | PROPUESTA | Definición operacional de estado inicial y F*/objetivo |
| INV-02 | Catálogo F1/F2/A1/A2 | Dos rutas de dos pasos, focal y alternativa | PROPUESTA | TID/SID/RID, contratos, mapping y catálogo cerrado |
| INV-03 | Escenarios R0–R3 | Exclusividad, alternativa basal, alternativa afectada y fallo | PROPUESTA | Correspondencia aprobada con población, política y estimando |
| INV-04 | G y H | G atómica; H=3 pasos; ciclos base prohibidos | PENDIENTE DE RATIFICACIÓN | Duraciones, ventanas, sensibilidad H, ciclos y terminación |
| INV-05 | Recursos/condiciones | Reserva por instancia; C_auth basal; bloqueos tipados | PARCIAL | Frontera, inventario, dependencia externa y concurrencia |
| INV-06 | Alternativas/exhaustividad | Ocho dimensiones de cobertura | ABIERTO | Evidencia de cobertura completa y adjudicación independiente |
| INV-07 | Truth/observed | Truth oculta; observación 1/0/? | PROPUESTA | Esquema, fuentes, cegamiento y validación de error |
| INV-08 | Implicación Reach | Abrir F1 no basta; A1→A2 puede mantener Reach(SF) | HALLAZGO LÓGICO DEL FIXTURE | Oráculos y revisión independiente |

**Dictamen:** se dispone de un inventario abstracto finito candidato, no de un catálogo confirmatorio. AUD-005 y AUD-007 siguen abiertos; no declarar exhaustividad ni Reach=0 para el DGP hasta validar universo y cobertura.


## 14. Seguimiento — integración temporal y escenarios S4-R

| ID | Punto | Estado | Criterio de cierre |
|---|---|---|---|
| TEMP-01 | H frente a t0–t9 | Propuesta: índices separados | Ratificar profundidad vs horizonte temporal |
| TEMP-02 | Reach en t4 sobre snapshot t3 | Propuesta | Contrato de filtración temporal y snapshots |
| TEMP-03 | App por estado hipotético | Abierto | Predicados por transformación/estado y oráculos |
| TEMP-04 | Dinámica por rama | Abierto | Regla de transición, snapshots y recursos temporales |
| TEMP-05 | R0–R3 ↔ S4R-A…D | Correspondencia propuesta | Revisión contra escenarios/estimandos originales |
| TEMP-06 | Duración/ventanas/caducidad | Abierto | Unidades, origen, restricciones y sensibilidad |

No se cierra AUD-005/007 ni se declara H confirmado.


## 15. Seguimiento — matriz operacional de predicados

| ID | Punto | Estado | Criterio de cierre |
|---|---|---|---|
| PMX-01 | ACC/T_acc fijada en t3 | Propuesta para fixture base | Ratificar frontera y reglas de cambio |
| PMX-02 | APP por estado de entrada | Especificado conceptualmente | Fichas de precondiciones para F1/F2/A1/A2 |
| PMX-03 | REL por arista | Especificado conceptualmente | Catálogo y versión de relaciones |
| PMX-04 | AUTH/BLOCK/WIN | Parcial | Política, ventanas, caducidad y fuentes |
| PMX-05 | RES por ruta | Abierto | Demanda, reserva, capacidad y liberación |
| PMX-06 | dinámica por rama | Abierto | Regla DGP y snapshots inmutables |
| PMX-07 | COV/evidencia | Parcial | Universo, E1–E4, adjudicación y error |
| PMX-08 | truth vs observed | Regla establecida documentalmente | Oráculo independiente y validación |

La matriz no asigna valores por escenario ni cierra AUD-004/005/007/010/011.


## 16. Seguimiento — fichas transformacionales

| ID | Punto | Estado | Criterio de cierre |
|---|---|---|---|
| TC-01 | F1 / τ2 | Parcialmente definido por §§62–63/67 | Ficha semántica/versionada y criterios técnicos completos |
| TC-02 | F2 | Solo transición topológica S2→SF | Función, entrada/salida verificables, precondiciones y recursos |
| TC-03 | A1 | Solo transición topológica S0→S1 | Mecanismo alternativo y precondiciones |
| TC-04 | A2 | Solo transición topológica S1→SF | Mecanismo de cierre y precondiciones |
| TC-05 | F* / SF | SF formal; F* operacional abierto | Objetivo observable, restricciones y tolerancias independientes de O/V |
| TC-06 | R0–R3 | Escenarios estructurales candidatos | Validar alternativas y substituibilidad con cobertura |
| TC-07 | Microdominio | No seleccionado | Propuesta neutral explícita y revisión/decisión |

La auditoría histórica de fichas no cierra las fichas sustantivas.


## 17. Seguimiento — selección de microdominio

| ID | Punto | Estado | Criterio de cierre |
|---|---|---|---|
| MD-01 | Comparación de microdominios | Completada como análisis documental | Revisión independiente de criterios y sesgos |
| MD-02 | Opción A: migración de configuración | Recomendada, no seleccionada | Decisión explícita del diseño |
| MD-03 | F* técnico | Borrador conceptual | Propiedades, tolerancias y oráculo independientes de O/V |
| MD-04 | Independencia A1/A2 | Hipótesis de diseño | Demostrar separación mecanística respecto de F1/F2 |
| MD-05 | B vs ejecución | Separación conceptual | Especificación de protocolo/tiempos sin ejecución de transformaciones por B |
| MD-06 | Recursos/ventanas/IDs | Abierto | Fichas versionadas y valores justificados |

La recomendación no aprueba el microdominio ni cierra las auditorías causales/medición.


## 18. Seguimiento — compatibilidad causal del microdominio

| ID | Punto | Estado | Criterio de cierre |
|---|---|---|---|
| MD-C1 | Manifiesto de B | Abierto | Cambios exhaustivos, reversibilidad, recursos, permisos y prueba de no ejecución de F1/F2 |
| MD-C2 | Primera etapa A_f* | Abierto | Medir A_f* por separado de C_dep y D_f* |
| MD-C3 | Identidad/roles F1/F2 | Reformulación requerida | B/provisión separada de F1/conversión; contratos entrada/salida |
| MD-C4 | Independencia A1/A2 | Abierto | Grafo de dependencias y prueba de no afectación en R0/R1 |
| MD-C5 | F* y oráculo | Abierto | Armonización con POP §5; criterios y oráculo ciegos, no circulares |
| MD-C6 | Estimandos/D1-D2 | Abierto | g0/g1, q, población, Value, horizonte y comparador justificados |
| MD-C7 | Vías colaterales | Abierto | Recursos, permisos, seguridad, coste, latencia, información, interferencia |

La auditoría concluye compatibilidad potencial, no identificación ni aprobación del microdominio.


## 19. Seguimiento — manifiesto de provisión y dependencias

| ID | Punto | Estado | Criterio de cierre |
|---|---|---|---|
| MD-B01 | Catálogo de cambios B-M01…15 | NO INVENTARIADO | Inventario real con evidencia por superficie; “no cambia” requiere diff/cobertura |
| MD-B02 | Arquitectura ARCH-B1 sidecar | Recomendada para evaluar | Factibilidad, frontera, versiones, hash y decisión explícita |
| MD-B03 | Grafo dependencias focal/alternativa | Abierto | Nodos/aristas, consumidores, relaciones, versiones y cobertura |
| MD-B04 | Recursos/contención | Abierto | Cuotas y medición por unidad/ruta; no degradación de A1/A2/F2 en R0/R1 |
| MD-B05 | Permisos/seguridad | Abierto | ACL mínima, sin cambio de C_auth funcional; auditoría de seguridad |
| MD-B06 | Snapshots/rollback | Abierto | S_preB/S_postB/S_rollback comparables y residuos caracterizados |
| MD-B07 | No-afectación A1/A2 | Abierto | Prueba funcional pre/post B con margen de equivalencia justificado |
| MD-B08 | Cobertura de universo | Abierto | Catálogo finito y cobertura; unknowns propagan Reach/F_alt=? |

El documento de manifiesto contiene PROV-01…12, contratos documentales no ejecutados.


## 20. Seguimiento — matriz de cobertura y estados trivalentes

| ID | Punto | Estado | Criterio de cierre |
|---|---|---|---|
| GC-01 | Inventario de nodos U_G | Parcial / no verificado | Inventario real con ID, rol, versión, hash, consumidor y evidencia |
| GC-02 | Grafo de aristas | NONE | Relaciones transitivas, dirección, ventana, cobertura y evidencia |
| GC-03 | Predicados A_f* | ? | ID/REL/COND/AUTH/RES/DEP/BLOCK evaluados independientemente |
| GC-04 | Ruta focal Rτ2 | ? | Secuencia completa e identidad/temporalidad verificadas |
| GC-05 | Alternativa RA12 | ? | Catálogo, contrato, dependencias y conformidad F* verificados |
| GC-06 | Universo de rutas | No exhaustivo | Frontera, granularidad, H y cobertura de Runknown justificados |
| GC-07 | Reach_H / F_alt,0 | ? | Reglas trivalentes con cobertura exhaustiva para declarar 0 |
| GC-08 | Evidencia y cegamiento | NONE | Proveniencia, hash, método, observer, cobertura y error registrados |

La matriz C10_S_GRAPH_COVERAGE_AND_TRIVALENT_EVIDENCE_MATRIX_DRAFT_001.md contiene 23 nodos, 23 aristas, 14 predicados y cinco rutas candidatas.


## 21. Seguimiento — plantilla de inventario U_G

| ID | Punto | Estado | Criterio de cierre |
|---|---|---|---|
| UGI-01 | Registro de nodos | Esquema creado; sin observaciones | Correspondencia completa con roles U_G y campos TID/SID/RID, versión, frontera, consumidores y evidencia |
| UGI-02 | Registro de aristas/dependencias | Esquema creado; sin observaciones | Correspondencia con catálogo de aristas; directas/transitivas, ciclos, compartidas y cobertura |
| UGI-03 | Registro de rutas | Esquema creado; sin rutas observadas | Mapear cinco clases U_G y registrar F*, G, H, C0, versiones, alternativas y substituibilidad |
| UGI-04 | Predicados por paso/tiempo | Esquema creado; truth restringida | Correspondencia con ID/REL/COND/AUTH/RES/DEP/BLOCK/APP/ALT/ORACLE/EXT y separación truth/observed |
| UGI-05 | Snapshots y fuentes | Esquema creado; no capturados | Procedencia, integridad, timestamps, hash y limitaciones |
| UGI-06 | Cobertura por dimensión | Esquema creado; cobertura NONE | Definir universo, fuentes examinadas, alcance cubierto, omisiones/opacidad y adjudicación |
| UGI-07 | Adjudicación/cegamiento | Parcialmente especificado | Protocolo de evaluadores, discrepancias, reglas y revisión independiente |

La plantilla es un artefacto documental vacío. No hay inventario técnico real ni evidencia para actualizar estados 1/0/?. No se cierra GC-01…12, MD-C1…6, AUD-005/007/010/011 ni OPEN-C10-001/003/005/007.


## 22. Seguimiento — reconciliación U_G/plantilla

| ID | Control | Estado | Criterio de cierre |
|---|---|---|---|
| UGC-01 | Correspondencia de nodos N01–N23 | 23/23 semántica | Resolver desagregaciones N05/N06/N07/N16/N18/N19/N20/N21/N23 y documentar reglas de identidad. |
| UGC-02 | Correspondencia de aristas E01–E23 | 23/23 IDs padre | Normalizar mult destino; E07 como regla lógica; resolver destinos E22; adjudicar las 39 filas candidatas. |
| UGC-03 | Predicados | 14/14 | Verificar tiempos, evidencia mínima, familia vs código y separación truth/observed. |
| UGC-04 | Clases de ruta | 5/5 | Preservar Rτ2/RA12/Rshared/Rexternal/Runknown y distinguir subtipos. |
| UGC-05 | Campos de evidencia/cobertura | Parcial | Incorporar procedencia, evidence_status, contract_intent, coverage_scope_id, adjudicación y unknown_reason en todas las tablas. |
| UGC-06 | N16/N23 y eventos | Abierto | Separar F*, oráculo, adjudicación; ejecución, Outcome, Value; definir selección/ejecución como eventos/variables. |

No se asignan estados técnicos ni cobertura efectiva. El esquema no se declara cerrado. UGC-01…06 son controles documentales pendientes de revisión; no pruebas ejecutadas.


## 23. Seguimiento — protocolo de procedencia y adjudicación U_G

| ID | Control | Estado | Criterio de cierre |
|---|---|---|---|
| UGE-01 | Taxonomía S1–S8 y ajuste fuente-afirmación | Propuesta definida | Revisar fuentes concretas y adecuación por afirmación/dimensión |
| UGE-02 | Campos de procedencia | Definidos documentalmente | Correspondencia campo-a-campo con plantilla y expediente evidence_id |
| UGE-03 | Evidencia mínima de nodos/aristas | Definida | Validar por microdominio; ausencia con cobertura negativa |
| UGE-04 | Predicados y rutas | Definidos | Criterios específicos por F*, ruta, tiempo y oráculo |
| UGE-05 | Cobertura y denominadores | Marco definido, denominadores abiertos | Fijar universo y denominadores por dimensión/versionado |
| UGE-06 | Doble evaluación/cegamiento | Procedimiento propuesto | Definir evaluadores, factibilidad, acuerdo y tercer adjudicador |
| UGE-07 | Propagación trivalente/parada | Reglas documentales | Auditar consistencia con contratos Reach, ALT y DGP |
| UGE-08 | Seguridad y custodia | Abierto | Ubicación de fuentes, secretos, acceso, retención y referencias seguras |

Protocolo no aplicado. No hay inventario ni cobertura técnica; no se cierran UGE ni GC/UGI/UGC, MD-C1…6 o auditorías relacionadas.


## 24. Seguimiento — auditoría campo-a-campo del esquema de evidencia U_G

| ID | Hallazgo | Estado | Criterio de cierre |
|---|---|---|---|
| FCM-01 | EVIDENCE_REGISTER separado | Definido en plantilla §12.1 | Validar tipos, unicidad, integridad y seguridad |
| FCM-02 | Vínculo afirmación-evidencia | Definido §12.2 y §12.8 | Comprobar referencias y alcance compatible |
| FCM-03 | Cobertura con denominador | Definida §12.3 | Validar denominadores/reglas por dimensión y microdominio |
| FCM-04 | Doble evaluación independiente | Definida §12.4 | Revisar independencia, cegamiento y flujo de captura |
| FCM-05 | Adjudicación/discrepancias | Definida §12.5 | Revisar trazabilidad y conservación de posición minoritaria |
| FCM-06 | Truth DGP separada | Retirada de tabla analítica; §12.6 | Validar segregación técnica y control de acceso antes de implementación |
| FCM-07 | Clases de ruta/subtipos | Separadas en esquema | Validar tipos/valores y correspondencia U_G |
| FCM-08 | Campos comunes | Definidos §12.7 | Validar presencia exacta en cada tabla de objeto |
| FCM-09 | Integridad referencial/versionado | Reglas §12.8 | Validar parser/constraints y supersession |

**Estado global:** corregido documentalmente, pendiente revisión independiente y validación ejecutable. No son tests ejecutados ni evidencia de cobertura.


## 25. Seguimiento — consistencia interna del esquema U_G

| ID | Hallazgo | Tratamiento documental | Cierre restante |
|---|---|---|---|
| FCM-10 | Campos comunes no materializados en tablas | Encabezados añadidos §§2–6 | Parser y revisión independiente |
| FCM-11 | SNAPSHOT observado ? sin aplicabilidad | Ejemplo NA | Verificar semántica por instancia |
| FCM-12 | Evaluador singular | evaluator_record_ids y filas E1/E2 separadas | Validar flujo |
| FCM-13 | Evidence refs multi valor | CLAIM_EVIDENCE_LINK 1:N | Validar integridad FK |
| FCM-14 | Cobertura §7 ambigua | Vista resumen; COVERAGE_REGISTER normativo | Revisar instancias |
| FCM-15 | Tipos/domínios ausentes | §§12.9–12.10 | Implementar/validar constraints cuando se autorice |
| FCM-16 | Destino claim_target_id ambiguo | object_record_id | Validar referencias |

FCM-01…16 están tratados documentalmente, no probados técnicamente. Esquema Draft; revisión independiente y validación ejecutable pendientes.


## 26. Seguimiento — tercera pasada de normalización relacional U_G

| ID | Hallazgo | Corrección documental | Cierre restante |
|---|---|---|---|
| FCM-17 | PK plural en EVALUATOR_ASSESSMENT | evaluator_record_id singular, una fila por E1/E2 | Validar unicidad/FK |
| FCM-18 | Evidencias serializadas en evaluaciones/adjudicaciones | CLAIM_EVIDENCE_LINK con evaluator_record_id/adjudication_id | Validar relaciones |
| FCM-19 | object_id ambiguo | object_record_id en evaluación/adjudicación | Validar integridad referencial |

Comprobación estática de alineación de columnas: PASS documental en diez tablas. No es validación ejecutable; FCM-01…19 siguen pendientes de revisión independiente y validación técnica.


## 27. Revisión independiente del esquema U_G — SR-01…20

| Grupo | Controles | Estado | Criterio de cierre |
|---|---|---|---|
| Identidad/relaciones | SR-01…04, SR-10, SR-18 | No revisados | Revisión R1 y validación de claves/FK/cardinalidad |
| Cobertura/evidencia | SR-05…07, SR-15 | No revisados | Revisión R2; evidencia negativa y propagación correctas |
| Grafo U_G | SR-08, SR-09, SR-16 | No revisados | Crosswalk y dependencias coherentes |
| Medición/causalidad | SR-12, SR-14 | No revisados | Cegamiento y no circularidad revisados |
| Truth/security | SR-13, SR-19 | No revisados | Revisión de segregación, permisos y custodia |
| Tipos/operación | SR-11, SR-17, SR-20 | No revisados | Tipos, timestamps, NA y aptitud operativa |
| Dictamen | Procedimiento §6 del checklist | No emitido | ACEPTABLE / CONDITIONAL / REVISE / NOT ASSESSABLE con evidencia |

Paquete preparado, revisión no iniciada, sin revisores designados. FCM-01…19 y XSYNC-138-01 siguen abiertos; no hay freeze ni autorización de ejecución.


## 28. Reconciliación de cardinalidad evidence_ref — FCM-20

| Hallazgo | Resolución documental | Estado |
|---|---|---|
| §12.7 permitía uno o varios evidence_ref; §§12.9/14 limitaban a un vínculo primario | evidence_ref = 0..1 navegación; CLAIM_EVIDENCE_LINK = relación completa 0..n | Tratado documentalmente |
| FCM-12 describía de forma ambigua la PK de evaluación | evaluator_record_id singular por fila E1/E2; evaluator_record_ids plural solo en objetos | Armonizado |

Pendiente revisión independiente SR-01…20 y validación ejecutable. FCM-01…20 no se declaran técnicamente cerrados.


## 12. Gate científico C10-S sin dependencia de revisión externa (2026-11-05)

La continuidad del trabajo científico se realiza mediante AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT. No se designan R1/R2 como condición de avance ni se simula independencia. Los controles se califican solo hasta donde llegue la evidencia disponible.

La preparación del experimento exige autocontención y auditabilidad: contrato causal y estimandos, DGP/truth versionados y ocultos al analizador, roles separados, reglas ex ante, pruebas negativas/adversariales, medición independiente, manifiestos, resultados brutos, auditoría de integridad y replay sujeto a autorización.

La revisión externa no es gate para continuar ni para concluir una prueba sintética correctamente ejecutada. El alcance de las conclusiones se limita al DGP, parámetros, población, horizonte, políticas y regla de Value definidos. Ninguna conclusión sintética se presenta como causalidad empírica general.


## 29. Reconciliación del plan Draft 004 y gate científico autocontenido (2026-11-05)

El plan operativo vigente pasa a ser C10_S_DESIGN_CLOSURE_AND_OPERATIONALIZATION_PLAN_DRAFT_004.md. Este addendum armoniza el estado de control sin reescribir matrices históricas.

1. La cobertura 130–183 se considera integrada en el maestro §§16–52 y los contratos auxiliares. No se abre recuperación histórica adicional.
2. La arquitectura de accesibilidad debe leerse con §§59–64 (condiciones y fórmula focal candidata), §60 (T_cap/T_acc relacional), §71 (S_T*/E_T y ΔT/ΔE), §§73–76 (Reach, temporalidad y predicados), §§77–81 (fichas, microdominio, B y cobertura), y §§82–130 (U_G y DEC).
3. La parte estadística comprende la fuente 165–183 y las familias P177/P178/P179/P182/P183. El cierre cuantitativo incluye potencia/precisión separadas, búsqueda de N, R según error Monte Carlo, heterogeneidad/compliers, sensibilidad δ/γ, medición y ausencia/censura.
4. Los valores N=2.000 y R=1.000 no son parámetros confirmatorios aceptados.
5. La mención histórica a revisión externa en G6 (§9) no es gate de continuidad ni de ejecución sintética. Prevalece §12: AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT; no se exige R1/R2. La revisión externa solo se activaría por decisión expresa para un alcance distinto, no como condición de progreso actual.
6. Los roles generador, analizador y evaluador deben estar separados por arquitectura de datos/permisos/proceso; ello no se denomina revisión humana independiente.
7. La implementación técnica, simulación y ejecución científica siguen sujetas a autorización separada.

**Estado:** reconciliación documental del control. No se cierran gates científicos ni se declara ejecución, validación técnica o revisión independiente.


## 30. Crosswalk de aceptación material de políticas D2 — DEC-C10-067 (2026-11-06)

Este addendum propaga al control de cierre la decisión registrada en 00_GOVERNANCE/SIP/DEC-C10-067_D2_MATERIAL_POLICY_CONTRACT_ACCEPTANCE.md (blob 2c3e1dbff4c83ded910a1fd8ca0a47a602df2213) y el contrato auxiliar del Test Contract Register §56 (D2POL-01…10). No reescribe los registros históricos de §6.2 ni las precedencias ya supersedidas por DEC-C10-066.

| Control de cierre | Condición reconciliada | Fuente/contrato | Estado actual | Evidencia pendiente |
|---|---|---|---|---|
| FCM-D2-01 | B_g0^D2: no programar/iniciar intento focal por política | DEC-C10-067 §§3–4; D2POL-01 | Definición conceptual aceptada | Política versionada y registros temporales; provisión de fondo medida |
| FCM-D2-02 | B_g1^D2: programar intento estandarizado de provisión focal | DEC-C10-067 §§3–4; D2POL-02 | Definición conceptual aceptada | Actor/rol, artefacto/version/hash, recepción y desviaciones |
| FCM-D2-03 | Separar Z, W_programmed, W_attempt, recepción y éxito | DEC-C10-067 §4; D2POL-03 | Criterio definido | Timestamps, cumplimiento, reintentos y fallos parciales |
| FCM-D2-04 | Verificar por separado instalación, integridad, compatibilidad y operatividad | DEC-C10-067 §4; D2POL-04 | Criterio definido | Evidencia independiente por componente y regla de adjudicación |
| FCM-D2-05 | No equiparar C_dep*, A_f* y D_f* | DEC-C10-067 §4; D2POL-05 | Distinción conceptual aceptada | Predicados completos y snapshots basal/post |
| FCM-D2-06 | Mantener C_auth,base=1 y condiciones no focales comunes en DGP aislado | DEC-C10-067 §4; D2POL-06 | Invariantes candidatas, no demostradas | Fichas operativas, evidencias y escenarios adversariales |
| FCM-D2-07 | Registrar cambios colaterales inducidos por la provisión | DEC-C10-067 §4; D2POL-07 | Obligación conceptual aceptada | Manifiesto de cambios y grafo de dependencias |
| FCM-D2-08 | Verificar ausencia de provisión focal de fondo/rutas equivalentes en control | DEC-C10-067 §§3–4; D2POL-08 | Requisito abierto | Inventario, cobertura y evidencia independiente |
| FCM-D2-09 | Mantener s=0.80 como hipótesis no validada | DEC-C10-067 §5; D2POL-09 | Estado reconciliado | Sensibilidad y eventual calibración, sin aprobación anticipada |
| FCM-D2-10 | Separar provisión técnica de ejecución F1/F2/A1/A2 | DEC-C10-067 §3; D2POL-10 | Restricción conceptual aceptada | Contratos/eventos y pruebas negativas |

### Dictamen de cierre

La definición conceptual de ambas políticas D2 está aceptada; la aceptación no convierte en invariantes demostradas las condiciones comunes ni acredita ausencia efectiva de provisión de fondo. Tampoco valida parámetros, población/soporte, unidad/interferencia, estimandos, exclusión o identificación. D2 sigue siendo primario candidato y D1 secundario por DEC-C10-066. El contrato documental no está implementado ni ejecutado; no se declara PASS técnico o científico.

**Estado de control:** crosswalk DEC-C10-067 incorporado; evidencias y operacionalización pendientes. scientific_execution=false; execution_authorized=false.


---

## 31. Crosswalk causal B-M01…15 → vías → estimandos — D2 (2026-11-06)

**Estado:** matriz de trazabilidad analítica candidata, derivada de los dominios ya definidos en el manifiesto §3/§12, contratos PROV-01…12 y decisión DEC-C10-067. **DRAFT / NO APROBADA / NO CONGELADA / NO EJECUTADA.** No constituye inventario de una implementación real ni adjudica que una vía haya ocurrido.

**Regla de lectura:** la columna U_G indica clases topológicas candidatas que deben comprobarse en el grafo real; no afirma pertenencia observada. La columna de mecanismo usa la taxonomía causal de manifiesto §12.3. Una superficie puede conectar varias rutas y activar varios mecanismos. La asignación final exige nodos, aristas, consumidores, frontera, unidad, versión y ventana evidenciados.

| Dominio | Variable/objeto a inspeccionar | U_G candidato (no observado) | Mecanismo causal si cambia por B | Evidencia/contrato rector | Consecuencia sobre cadena y estimandos | Control |
|---|---|---|---|---|---|---|
| B-M01 Artefacto/versión | Identidad, versión, hash, firma, SBOM; C_install, C_integrity, componente focal de C_dep* | Focal; compartida/desconocida si dependencias transitivas lo revelan | Focal; constitutivo adicional si el artefacto incluye funcionalidad/permiso no previsto | Manifiesto de componentes y procedencia; snapshots; PROV-03/04/12 | Puede cambiar C_dep* → A_f* → ΔT_acc*; si el artefacto cambia funcionalidad, seguridad o rutas, el ITT es efecto de paquete y no efecto puro de accesibilidad | FCM-D2-04/05/07/10 |
| B-M02 Runtime | Imagen/runtime/proceso, configuración, librerías, aislamiento y cuotas | Focal; compartida si runtime/host/servicios son comunes; externa si gestionado fuera de frontera | Focal y/o vía colateral por recursos, seguridad, rendimiento o dependencias compartidas | Grafo transitivo, imagen/hash, configuración y consumidores; PROV-03/04/05/09 | Alteración de capacidad/latencia/rutas puede afectar Reach, ejecución y Outcome por fuera de A_f*; revisar ITT de paquete e interferencia | FCM-D2-07/10 |
| B-M03 Host | Paquetes, SO, variables, servicios, configuración y dependencias del host | Compartida; alternativa si sirve A1/A2; externa si proveedor fuera de frontera | Cambio de condición constitutiva o vía colateral a alternativas/seguridad | Diff pre/post; grafo y consumidores; snapshots; PROV-03/04/08/09 | Puede afectar A1/A2, compatibilidad, seguridad y Reach; no atribuir cambios de resultados exclusivamente a ΔT_acc* | FCM-D2-07/08 |
| B-M04 Interfaz | Endpoint, API/schema, puertos, canal, ACL técnica, relación de invocación R/REL | Focal; compartida/alternativa si canal o servicio se reutiliza; externa si endpoint externo | Mecanismo focal; cambio constitutivo (relación/autorización); vía de latencia o ruta adicional | Especificación API, ACL, puertos, grafo de llamadas y pruebas; PROV-04/06/09/12 | Puede completar C_dep* o cambiar relaciones de otras rutas; primera etapa en C_dep* no implica primera etapa en A_f* | FCM-D2-04/05/07/10 |
| B-M05 Permisos | C_auth,base, permisos técnicos, roles, tokens, alcance, titular y vigencia | Focal; compartida si credenciales/roles afectan otros componentes | Cambio de condición constitutiva; vía B → C_auth → A_f* si se amplía autorización funcional | Registro normativo y diff de permisos; PROV-06; ficha D2-INV-AUTH-01 | Si cambia autorización funcional, D2 deja de aislar provisión técnica; ITT permanece efecto de política, atribución exclusiva a accesibilidad no demostrada | FCM-D2-06/07 |
| B-M06 Datos | Estado fuente/destino, configuración, metadatos, datos funcionales, estado X, aplicabilidad y F* | Focal/compartida; alternativa si modifica entradas o estado usado por A1/A2 | Cambio constitutivo o vía directa a aplicabilidad, ejecución, Outcome; posible cambio del objeto medido | Hashes y snapshots de datos/configuración; PROV-02/03/07 | Una vía B → X/App/F* → Execution/Outcome no mediada por A_f* convierte el contraste en paquete o exige estimando/identificación adicional | FCM-D2-07/10 |
| B-M07 Recursos | R_access*, C_resource como descriptor de disponibilidad, C_capacity descompuesta (instalada/disponible/reservada/consumida), cuotas, compromisos, colas y consumidores | Compartida; focal para cuota/capacidad del adaptador; alternativa si sirve A1/A2/F2 | Cambio constitutivo si capacidad/slots no focales necesarios para ofrecer τ2 cambian; vía colateral por saturación/desplazamiento/rendimiento; interferencia por pools/colas compartidos | Configuración y capacidad máxima/utilizable; K_required y ventana preespecificadas; reservas, compromisos, demanda concurrente, consumo B, consumidores y snapshots; PROV-03/04/05/09; D2-RES-01/D2-CAP-01 | Capacidad focal de B pertenece a C_dep*. Capacidad no focal solo entra en R_access* si necesaria, ex ante y no duplicada. Margen/consumo dependiente de S0 o ejecución va a App_f*/ejecución. ITT paquete si B cambia capacidad no focal; aleatorización individual no elimina interferencia. No crear CAP-τ2 ni factor separado sin justificación | FCM-D2-06/07/08 |
| B-M08 Red | DNS, proxy, firewall, rutas, puertos, conectividad y servicios compartidos | Compartida, externa, focal o alternativa según grafo | Cambio de relación/condición constitutiva, disponibilidad de ruta o seguridad | Diff topológico y reglas; dependencias/consumidores; PROV-03/04/09 | Puede abrir/cerrar rutas distintas de τ2 y cambiar Reach; si no hay cobertura, Reach=? y no ausencia | FCM-D2-07/08 |
| B-M09 Seguridad | Sandbox, políticas, certificados, superficie de ataque, bloqueos y controles | Compartida/focal/externa según componente | Cambio constitutivo (bloqueo/habilitación) o vía a riesgo, coste y Value | Revisión y configuración de seguridad pre/post; versiones y adjudicación; PROV-03/06 | Una alteración de bloqueos puede modificar A_f*; riesgo/coste puede afectar Outcome/Value por vía paralela | FCM-D2-06/07 |
| B-M10 Observabilidad | Logs, métricas, telemetría; acceso del agente y del evaluador; K y E_T | Compartida/externa/desconocida según productores, consumidores y repositorios | Cambio epistémico/informativo; posible vía B → K → consideración/selección → Execution; cambio separado de medición | Esquema, permisos, retención, destinatarios y timestamps; separación de E_T; contratos de evidencia | Conocimiento del agente puede mediar efectos de política; observabilidad del evaluador cambia clasificación observada, no necesariamente T_acc*; no ajustar mecánicamente por mediador post-B | FCM-D2-07 |
| B-M11 Estado | Cachés, registros, índices, estado persistente y residuos | Focal/compartida/alternativa según consumidores | Cambio de condición/estado, ruta alternativa o vía residual postprovisión | Inventario de estado y snapshots pre/post/rollback; PROV-03/07/10 | Puede cambiar App, relaciones o rutas sin pasar por la apertura focal; rollback incompleto deja exposición persistente y compromete consistencia de tratamiento | FCM-D2-07/08 |
| B-M12 Rendimiento | Latencia, throughput, prioridad, contención, disponibilidad y degradación | Compartida/focal/alternativa/externa según recurso o servicio | Vía colateral a factibilidad temporal, ejecución, calidad, coste y Outcome/Value | Medición comparable por brazo/unidad/ventana; perfil de carga y margen preespecificado; PROV-05/08/09 | Puede impedir recorridos temporales o degradar A1/A2; efecto paralelo al cambio de accesibilidad, posible interferencia | FCM-D2-07/08 |
| B-M13 Oráculo | F*, dataset de referencia, validador, reglas y versión | Común-medición/compartida; no debe formar parte de B | Cambio epistémico/de medición o modificación del criterio de resultado; intervención prohibida en B | Hash/version inmutable, ceguera y snapshots; PROV-02 | Si cambia el oráculo, cambia la definición/adjudicación de Outcome; comparación causal no válida bajo mismo resultado. No imputar a ΔT_acc* | FCM-D2-07/10 |
| B-M14 Alternativas | A1/A2, exportador/importador, formato, dependencias, permisos, recursos y conformidad funcional | Alternativa; compartida si dependencias/recursos comunes; externa si fuera de frontera | Vía colateral directa B → F_alt → Reach/Execution/Outcome | Catálogo/grafo y pruebas funcionales pre/post con margen de equivalencia; PROV-05/08/09 | Si B degrada, habilita o elimina alternativa, exclusión focal queda comprometida; ITT de paquete sigue interpretable, IV/LATE focal no por exclusión automática | FCM-D2-07/08 |
| B-M15 Reversibilidad | Rollback, residuos, dependencias, permisos, recursos y estado tras retirada | Cualquiera de focal/compartida/alternativa/externa; desconocida si cobertura incompleta | Vía residual persistente y posible contaminación de periodos/unidades | Snapshots S_preB/S_postB/S_rollback/S_routeA; diff y pruebas; PROV-03/10/11 | Residuos pueden alterar exposición, consistencia, carryover e interferencia; si no se observa, estado desconocido y atribución limitada | FCM-D2-07/08 |

### 31.1. Reglas transversales de adjudicación

1. **No confundir topología y mecanismo:** U_G clasifica posición de la ruta; el mecanismo describe cómo el cambio afecta variables/resultados. No deducir uno del otro.
2. **No confundir ausencia con falta de observación:** NO INVENTARIADO, ?, NONE y PARTIAL no prueban ausencia, invariancia o PASS. Si el universo/grafo no está cubierto, propagar desconocido conforme a la matriz temporal y contrato PROV-11.
3. **Separar tres invariancias:** (a) postulada por el DGP; (b) exigida por contrato; (c) demostrada con evidencia. Solo (c) permite afirmar no-afectación empírica en la frontera, unidad y ventana verificadas.
4. **ITT y atribución focal:** la aleatorización puede identificar el ITT de la política asignada bajo su diseño; si existen rutas colaterales, ese ITT es efecto del paquete material. La atribución exclusiva a ΔT_acc* requiere exclusión defendible o estrategia de identificación adicional; no se obtiene ajustando mecánicamente por mediadores postratamiento.
5. **Primera etapa:** evidencia de cambio en C_dep* no demuestra cambio en A_f*; y cambio en A_f* no demuestra por sí solo cambio en Reach, ejecución, Outcome o Value.
6. **B-M13/B-M14:** permanecen prohibidos como modificaciones funcionales por B según manifiesto §3; se inspeccionan para detectar desviaciones, no se autorizan como parte de la intervención.
7. **Estados y evidencia:** cada fila debe completarse para la implementación concreta con unidad, frontera, versión, tiempo, fuente, cobertura, grafo de consumidores y evidencia pre/post. Hasta entonces, la clase U_G y el mecanismo son hipótesis de auditoría, no hallazgos.

### 31.2. Dictamen y siguiente operación

El crosswalk conceptual B-M01…15 → variable/predicado → clase U_G → mecanismo → evidencia/PROV → cadena causal/estimando → FCM-D2 queda incorporado como instrumento de trazabilidad. **No** completa el manifiesto técnico real ni demuestra aislamiento. MD-C1 y MD-C4 siguen abiertos.

**Actualización de continuidad (2026-11-06):** la matriz de cobertura U_G y su crosswalk B-M01…15 están en C10_S_GRAPH_COVERAGE_AND_TRIVALENT_EVIDENCE_MATRIX_DRAFT_001.md, §§1–9; la aplicación del mapping a NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT y registros de evidencia/cobertura está en C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md, §17. La auditoría cruzada con el manifiesto §12 y las fichas temporales §13 se completó; resultado y correcciones en el plan de cierre §16.5. La siguiente operación es auditar la trazabilidad causal individual de las fichas de invariantes hacia predicados, contratos PROV, dominios B-M, U_G, vías y estimandos. Los estados técnicos permanecen desconocidos hasta que haya inventario y evidencia reales. No avanzar a ejecución ni a declaración de exhaustividad.
