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
| SRC-02 | C10-S | `C10_S_SYNTHETIC_EXPERIMENT_CONSOLIDATED_DRAFT_004.md`, PR #116, blob actual `e88df2d691f2389adf9ca70e949f20a22ee9b8bf` (incluye control §§0.5/213) | Base histórica hasta sección conversacional 164; recuperación resumida 165–183 en §§52–53; capítulos de reconciliación y medición §§54–60 | Draft, no aprobado |
| SRC-03 | Auditoría integrada | `C10_S_INTEGRATED_CONSISTENCY_AUDIT_DRAFT_001.md`, blob `d3ffa9ed0670764c339dc390423f435e6da0fc9b` | AUD-C10S-001…012 | Hallazgos abiertos |
| SRC-04 | Propuesta de resolución | `C10_S_AUD001_AUD002_RESOLUTION_DRAFT_001.md`, blob `5a3a2fa061fe146d9df9d4cdfbb803c5ee274d65` | Propuesta A_f, T_acc, ΔT_acc y DGP integrado | No aceptada |
| SRC-05 | Auditoría cruzada | `C10_S_AUD001_AUD002_CROSS_AUDIT_DRAFT_001.md`, blob `ce53c902fb39820e976eed5cb2a87e5eacace31c` | XAUD-001…007 | Hallazgos abiertos |
| SRC-06 | Informe de recuperación | `C10_S_RECOVERY_AND_TRACEABILITY_AUDIT_DRAFT_001.md`, blob `2f77832076773c67711f55a3c0d6680b69c2c6d9` | Reconstrucción de fuentes y límites hasta sección 183 | Recuperación parcial |
| SRC-07 | PR #115 | `research/c10-d1-protocol-draft` → PR #115 | 23 commits; 1 archivo; abierto Draft | Sin comentarios/revisiones |
| SRC-08 | PR #116 | `research/c10-s-consolidation-draft` → PR #116 | Trece archivos modificados en el corte de verificación 2026-11-04; el número de commits es dinámico; abierto Draft | Sin comentarios/revisiones registradas |

| SRC-09 | Reconciliación C10-D1 ↔ S4-R | `C10_S_C10D1_S4R_ESTIMAND_RECONCILIATION_DRAFT_001.md`, PR #116 | Contrato actualizado: D2 primario candidato; D1 secundario; ITT_Z^D2, LATE_f^D2 y θ_Af(q_X*) separados de θ_A(q) | DRAFT; jerarquía confirmatoria e identificación completas siguen abiertas |
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
| REC-CAUS-02 | TE / ITT | `ITT_Z` es efecto de asignación; `ψ_B(q_X*)` es contraste de versiones B recibidas y `ψ_policy(q)` el efecto del paquete de política. No atribuir ninguno automáticamente a accesibilidad (C10-D1 §§17.7, 26.1–26.2; C10-S §§44, 53) | D2: ITT_Z primario de asignación. `ψ_B` solo coincide con la instancia `ψ_policy` si versiones, población, resultado, Value, horizonte y régimen completo coinciden; recepción/cumplimiento y régimen permanecen abiertos | No igualar ITT_Z con ψ_B/ψ_policy bajo incumplimiento. D2 como escenario primario candidato está aceptado por DEC-C10-066; la jerarquía confirmatoria completa y la identificación focal siguen abiertas.
| REC-CAUS-03 | Efecto específico de accesibilidad | `θ_A(q)` es el estimando general C10-D1 sobre cambios estructurados `ΔT_acc`; `θ_Af(q_X*)` es focal sobre `D_f*`/apertura de `τ2`, no sustituto del general | D2: B_g0 no programa intento; B_g1 lo programa. La correspondencia con g^Af requiere distribución inducida de `ΔA_f` por historia, predicados completos, soporte y separación de vías. La ilustración 0,20→0,80 no es D2 | No transferir la primera etapa C_dep a A_f/D_f/ΔT_acc ni el valor 3,6 a D2. Ver maestro §131 y plan §16.12; θ_Af no identificado.
| REC-CAUS-04 | Intervención | La intervención D2 es la política material B sobre programación de provisión focal; g^Af es una política objetivo sobre la distribución de cambios de accesibilidad inducida por B (C10-D1 §26.1–26.2; maestro §131) | DEC-C10-067 acepta B_g0^D2 (no programar/iniciar intento focal) y B_g1^D2 (programarlo), manteniendo C_auth,base=1 y condiciones no focales comunes en el DGP aislado | No equivalencia automática B↔g. Recepción, cumplimiento, s, provisión de fondo, rutas alternativas y predicados de A_f abiertos. La antigua vía Z_A→C_auth permanece histórica/adversarial; PROV-06 material no verificado.
| REC-CAUS-05 | Variables y constructos | C_c constitutivas, L temporales, A/ΔT_acc, mecanismos, O, V separados | A_f*, A_f_obs, T_acc=(U,R,C), ΔT_acc, Reach, Π_H, selección, ejecución, O, V | PROPUESTA ÚTIL, NO ACEPTADA: consolidar diccionario único y temporal |
| REC-CAUS-06 | Población | Población, contexto, horizonte y régimen fijados antes de outcomes | P*_τ2 y P*_F; q_X* y q_L* en diseño S4-R | ABIERTO: definir población objetivo, inclusión, función F*, horizonte y cuándo P*_F es solo heterogeneidad |
| REC-CAUS-07 | Identificación | C10-D1 exige correspondencia implementable B→distribución g sobre cambios de accesibilidad, factibilidad/soporte por historia, consistencia/versiones, temporalidad y separación/identificación de vías (17.7, 26.1–26.2) | D2: ITT_Z por asignación; primeras etapas C_dep, A_f, D_f y ΔT_acc separadas; `LATE_f` solo bajo IV | Correspondencia B_g^D2→g^Af condicional/no demostrada. D2 no prueba exclusión, monotonicidad, relevancia, no interferencia, medición ni ausencia de colaterales. Ver maestro §131 y plan §16.12.
| REC-CAUS-08 | Outcome y Value | Medición separada; Value con regla independiente | O y V derivados tras ejecución; V_real separado de V_potential | PENDIENTE DE CONTRATO: regla, beneficiario, horizonte, costes/beneficios, incertidumbre y tests de no circularidad |
| REC-CAUS-09 | Temporalidad y datos incompletos | Snapshots longitudinales, medición, pérdidas, censura y selección | Secciones 130–164 contienen tratamientos parciales; 182/183 resumidas pero no verificadas | ABIERTO: recuperar 182/183 y construir matriz variable×momento×rol |
| REC-CAUS-10 | Conclusiones permitidas | Atribución identificada, evidencia adversa delimitada o identificación insuficiente | C10-S puede probar discriminación sintética y recuperación del DGP | COHERENTE: nunca traducir PASS sintético en prueba de hipótesis real |

### 4.1 Precedencia que debe respetarse

1. C10-D1 gobierna la interpretación causal y el alcance de estimandos.
2. C10-S especifica el entorno sintético y sus contratos transformacionales/causales.
3. Una decisión sintética no puede redefinir el estimando causal de C10-D1 por conveniencia de implementación.
4. Si una decisión de C10-S exige cambiar el estimando o el alcance de C10-D1, debe abrirse una decisión explícita y trazable; no se resuelve por armonización editorial.
5. ITT, θ_A(q), θ_Af(q), θ_{L,A}, IV/LATE y cualquier residual son objetos distintos. No se intercambian etiquetas ni interpretaciones.
6. La precedencia D2 primario candidato / D1 secundario está aceptada por DEC-C10-066; el contrato de estimandos actualizado distingue esa decisión de la jerarquía causal confirmatoria, que permanece DRAFT.


### 4.2 Reconciliación de estimandos y políticas (estado actualizado)

El documento `C10_S_C10D1_S4R_ESTIMAND_RECONCILIATION_DRAFT_001.md` se ha actualizado contra DEC-C10-066/067 y el maestro §§53, 131–132:
- `θ_A(q)` permanece como pregunta científica general C10-D1.
- D2 es el escenario primario candidato y D1 el secundario por DEC-C10-066.
- `B_g0^D2` no programa/inicia intento focal; `B_g1^D2` programa intento estandarizado de provisión técnica focal por DEC-C10-067.
- `ITT_Z^D2` es el efecto de asignación a esas políticas; no equivale automáticamente a efecto de accesibilidad ni a política recibida.
- `LATE_f^D2` es secundario, local y no está identificado/listo para Wald en el estado actual (§132).
- `θ_Af(q_X*)` requiere correspondencia B→g^Af y condiciones adicionales; sigue no identificado.
- Se separan las primeras etapas de C_dep, A_f, D_f y ΔT_acc. s=.80 sigue como hipótesis no validada.

La precedencia del escenario y las definiciones materiales D2 están aceptadas dentro del alcance de DEC-C10-066/067; la jerarquía confirmatoria completa, la identificación causal focal y los parámetros no quedan aprobados por esa aceptación.

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
| S4R-18 | XSYNC | PARCIAL / ABIERTO | XSYNC-138-01: la contradicción autorización-focal vs provisión técnica queda resuelta para D2 por DEC-C10-066/067; permanece abierto el mapping general B→g^Af, exclusión y revisión independiente. XSYNC-138-02…10 siguen abiertos según sus propios criterios |

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

La fuente recuperada contenía la recomendación histórica D1 principal condicionado / D2 contraste; DEC-C10-066 la supersede y establece D2 primario candidato / D1 secundario. DEC-C10-067 acepta las políticas materiales D2. Se mantienen como propuestas no aceptadas automáticamente: factorización de s=.80, mecanismos de éxito, δ/γ y vías alternativas; Value vectorial provisional; ausencia de A/O/V no se recodifica como cero. P181/P182/P183 siguen sin ejecución y requieren normalización/cotejo de contratos.

La sección 184 es solo una propuesta de siguiente paso y queda fuera de la fuente 165–183. No se declara cierre causal, aprobación del DGP, freeze ni autorización de ejecución.


## 13. Precisión de contratos P182/P183 tras recuperación de fuente (2026-11-04)

El registro de pruebas `C10_S_TEST_CONTRACT_REGISTER_DRAFT_001.md` incorpora ahora las tablas completas recuperadas P182-01…12 y P183-01…13, con sus criterios de aceptación textuales. Esto sustituye la descripción anterior de “solo IDs y resumen” en cuanto a la disponibilidad documental de esas fichas.

El cambio es documental: los criterios todavía deben convertirse en fixtures, entradas/salidas, tolerancias, códigos de fallo y evidencia reproducible. Todas las pruebas siguen propuestas y no ejecutadas. La sección 183 requiere además dictámenes separados para ITT-O, ITT por dimensión de V, mediación por A, LATE-V, efecto residual e índice agregado si existe.


## 14. Corrección de precedencia tras auditoría integral (2026-11-04)

La recomendación histórica de §6.2 S4R-08 se sustituyó para conservar dos escenarios diferenciados: D1 tiene C_dep,base=0, p0=.20 y p1=.80 postasignación, primera etapa .60; D2 tiene C_dep,base=0, p0=0 y p1=.80, primera etapa .80. La precedencia vigente es D2 primario candidato / D1 secundario por DEC-C10-066. D1 no es contaminación si la provisión ordinaria forma parte de la política asignada; no se presenta como escenario primario vigente.

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
| D2 como escenario primario candidato | ACEPTADO POR DEC-C10-066 | Provisión programada frente a ausencia de intento focal; ausencia real de provisión de fondo pendiente |
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
| B-M10 Observabilidad | K del agente; comunicaciones/manuales/formación; logs/métricas/telemetría; E_T, A_f_obs y ΔT_acc_obs | Compartida/externa/desconocida según productores, destinatarios, permisos, retención y consumidores | Cambio epistémico B→K→consideración/selección/Execution; cambio separado de medición/cobertura; no implica por sí mismo ΔT_acc* | Contenido, destinatarios, timestamps, permisos, esquema, retención, cobertura, reglas de adjudicación y acceso por brazo; N22/E22 (K); N16/E15 (evaluación funcional/oráculo); N23/E23 (endpoints Outcome/Value observados). E_T es un plano separado sin nodo/arista U_G explícitos; I-INFO-01…06; PROV-02/03/11 | No crear C_info autónomo. Información técnica imprescindible se asigna a C_dep* o R_access*/D_support* solo si necesaria/no duplicada. Conocimiento post-B puede mediar selección/ejecución; cambio E_T puede producir error/missingness diferencial. No ajustar automáticamente por mediadores postratamiento. Falta de cobertura → ?. FCM-D2-10 solo protege la separación entre provisión técnica y ejecución; no valida el proceso E_T ni la comparabilidad de medición. | FCM-D2-07/10 |
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


---

## 32. Auditoría IV de D2 — LATE_f y tratamiento focal D_f*

**Fuente:** `C10_S_D2_LATE_F_IV_VALIDITY_AUDIT_DRAFT_001.md`  
**Estado:** AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT · auditoría documental, no validación empírica.

| Componente | Estado | Hallazgo / condición de cierre |
|---|---|---|
| Tratamiento `D_f^*` / observación | PARCIAL | Separar verdad focal, registro observado y error; no inferir desde Z/B/W/C_dep. |
| Relevancia | OPEN | No hay primera etapa focal observada ni parámetros aprobados; separar C_dep, A_f, D_f y ΔT_acc. |
| Independencia | CONDITIONAL | Unidad, asignación, estratos, clústeres y elegibilidad pre-Z no cerrados. |
| Exclusión | OPEN / AMENAZA MATERIAL | Vías B-M01…15 hacia Outcome/Value fuera de D_f* no están descartadas; aleatorización no demuestra exclusión. |
| Monotonicidad | OPEN | No demostrada; crowding-out, alternativas y dependencias pueden producir defiers; crossover puede generar always-takers. |
| Consistencia/versiones | OPEN | Falta identidad/hash y trazabilidad de recepción, intento, instalación, verificación, fallos y rollback. |
| Interferencia | OPEN | Recursos/dependencias compartidas, spillovers y carryover no resueltos. |
| Medición Outcome/Value | OPEN | Adjudicación independiente, error diferencial, missingness, regla Value y horizonte pendientes. |
| Wald / `LATE_f` | BLOCKED / NOT READY | No seleccionar ni reportar como efecto causal hasta cerrar IV-G1…IV-G8. |

**Regla de interpretación:** `ITT_Z` puede conservar interpretación como efecto de asignación/política bajo el diseño. Si falla exclusión, el ITT es efecto de paquete; no atribuirlo a `D_f^*`. Un eventual `LATE_f` es local a compliers D2 y no equivale a `θ_Af(q_X^*)` poblacional ni a `θ_A(q)` general.

**Siguiente operación:** auditar la definición observacional de `D_f^*` y el protocolo de medición de `A_f^*`. No hay freeze, implementación, simulación ni ejecución.


---

## 33. Auditoría de medición de accesibilidad focal

**Fuente:** `C10_S_D2_FOCAL_ACCESSIBILITY_MEASUREMENT_AUDIT_DRAFT_001.md`  
**Estado:** AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT.

| Dimensión | Estado | Hallazgo / regla |
|---|---|---|
| Verdad vs observación | PARCIALMENTE ESTABILIZADA | Separar `S_T^*`, `E_T`, `A_f^*), `A_f^{obs}`, `D_f^*), `D_f^{obs}), `ΔT_acc^*) y `ΔE_T). |
| Composición de predicados | OPEN / MATERIAL | `C_info` y recursos/capacidad no están reconciliados con fichas; evitar duplicidad. |
| Identidad/comparabilidad | PARTIAL | τ2, frontera, contexto, G, catálogo y M deben fijarse; unresolved → ?. |
| Pinning/pertenencia | DEC-C10-065 ACCEPTED / UG-SCH-10 OPEN | Pinning no equivale a validación técnica del grafo/FKs/constraints. |
| Cobertura | NONE en plantilla | Rutas alternativas/compartidas/externas/desconocidas no inventariadas; no inferir ausencia. |
| Adjudicación/cegamiento | PROPOSED / NOT EXECUTED | Doble evaluación, ciego y truth oculta no demostrados operativamente. |
| Error/missingness | OPEN | Sin cuantificación/límites diferenciales por brazo, tiempo, versión, ruta y cobertura. |
| Temporalidad | PARTIAL | t0–t9 propuesto; ventanas, simultaneidad y vigencia pendientes. |
| Uso IV | BLOCKED | No usar `D_f^{obs}) como sustituto de `D_f^*) sin modelo de error defendible. |

**Gates MEAS-G1…G8:** composición; identidad/comparabilidad; pinning/pertenencia; cobertura; temporalidad; adjudicación; error/missingness; recuperación sintética con truth oculta. Su cierre no autoriza ejecución.

**Siguiente:** crosswalk exhaustivo de predicados de `A_f^*), sin alterar la fórmula ni crear símbolos, y luego regla trivalente de agregación. Wald/`LATE_f` permanece bloqueado.


---

## 34. Crosswalk causal de predicados de accesibilidad

**Fuente:** `C10_S_D2_AF_PREDICATE_CAUSAL_CROSSWALK_DRAFT_001.md`  
**Estado:** AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT.

| Dimensión | Estado | Dictamen |
|---|---|---|
| Fórmula de referencia | IDENTIFICADA / CANDIDATE | Maestro §67.3 / DGP §59.3; no es definición universal ni freeze. |
| C_auth_base | MAPPED → AUTH | Condición funcional basal; permisos técnicos de provisión separados. |
| C_resource/C_capacity | MAPPED CONDITIONALLY → RES/R_access | Solo disponibilidad ex ante necesaria y no duplicada; consumo/carga ejecución fuera. |
| C_info | NO AUTONOMOUS FACTOR | Técnica imprescindible dentro de condición existente; K/avisos colateral; E_T epistémico. |
| C_domain/D_support | MAPPING OPEN → ID/type or COND | No duplicar; separar dominio/tipo de precondición S0. |
| C_dep/C_install…C_oper | MAPPED → DEP | Ruta única en DGP aislado; generalización exige al menos una ruta válida. |
| C_other | EXCLUDED | Residual inadmisible. |
| VALID/cobertura/E_T | EPISTEMIC | Fuera de truth de A_f*. |
| App_f/K/selección/ejecución/O/V | DOWNSTREAM / OUTSIDE | No integrar en A_f*. |
| MEAS-G1 | PARTIAL | Fórmula candidata identificada; mapping/operacionalización de componentes y rutas pendientes. |

**Corrección de §33:** no describir C_info/C_resource/C_capacity/C_domain/C_other como factores vigentes autónomos; la fórmula histórica no prevalece sobre §§59.3/67.3. Siguiente: regla trivalente de agregación y rutas. `LATE_f` sigue bloqueado.


### 35. Regla trivalente de agregación A_f / DEP / D_f

**Fuente:** `C10_S_D2_FOCAL_ACCESSIBILITY_MEASUREMENT_AUDIT_DRAFT_001.md §10`.

| Objeto | Regla de 1 | Regla de 0 | Regla de ? |
|---|---|---|---|
| `A_f^{obs}` | Todos los términos necesarios 1, matching/comparabilidad y cobertura adecuados | Algún término necesario 0 con evidencia válida/suficiente | Resto; conflictos o cobertura insuficiente sin 0 suficiente |
| `DEP_f^{obs}` | Existe una ruta válida 1 | Todas las rutas del universo declarado 0 y cobertura COMPLETE, Runknown resuelto | No hay ruta 1 y queda unknown/cobertura incompleta |
| `D_f^{obs}` | Baseline 0 y post 1 | Baseline 1 o post 0 | Resto; no comparabilidad → NOT_COMPARABLE/? |

**Guardas:** MISSING/NONE/PARTIAL no equivalen a 0; C_dep=0 no implica DEP=0 con alternativa admisible; D_f observado no sustituye D_f verdadero para IV sin modelo de error defendible. Esta regla es documental, asistida/no independiente; no valida ejecución, cierra MEAS-G2…G8 ni IV, ni modifica DEC-C10-065/066/067.


## 36. Reconciliación de contratos adversariales y suite lógica TRI


**Fuente:** `C10_S_D2_FOCAL_ACCESSIBILITY_MEASUREMENT_AUDIT_DRAFT_001.md`, §11.

Registro de subcasos: `C10_S_TEST_CONTRACT_REGISTER_DRAFT_001.md`, §57. Los TRI son extensiones de MEAS-01…24, no una familia de pruebas independiente.

| Dimensión | Reutilización/cobertura | Estado tras reconciliación | Criterio aún pendiente |
|---|---|---|---|
| Identidad/matching | ID-01…15 | Contratos documentales existentes; no ejecutados | Fixtures/oráculos, error y adjudicación |
| Snapshots/diff | SNAP-01…15 | Contratos documentales existentes; no ejecutados | Validación de comparabilidad y matching |
| A_f trivalente | TRI-AF-01…05 | Especificación lógica propuesta | Evidencia por predicado, conflicto y cobertura |
| DEP/rutas | TRI-DEP-01…05 + U_G Rτ2/RA12/Rshared/Rexternal/Runknown | Especificación lógica propuesta | Inventario y cobertura completa para 0 |
| D_f basal/post | TRI-DF-01…06 | Tabla lógica de nueve combinaciones propuesta | Matching temporal y snapshots comparables |
| Separación/medición | TRI-OBS-01…03 | Contratos de no filtración/error propuestos | Doble evaluación, error diferencial y missingness |

**Dictamen:** cobertura documental mejorada por reutilización y crosswalk; MEAS-G8 OPEN, MEAS-G4/G6/G7 OPEN/PARTIAL según sus fuentes. No se declaran cerrados ID/SNAP, UG-SCH-10, XSYNC, PROV, MD-C1/MD-C4 ni IV. No hay fixtures serializados, ejecución ni autorización.



## 37. Cierre de validez IV de D2 — C10-S-IV-AUD-001

| Gate | Evidencia/condición requerida | Estado al corte | Consecuencia si no cierra |
|---|---|---|---|
| IV-G1 Tratamiento/población | `D_f^*` vs `D_f^{obs}`, elegibilidad pre-Z, unidad, versiones y snapshots comparables | PARCIAL / ABIERTO | No definir tratamiento IV observado ni población de compliers |
| IV-G2 Relevancia | Primeras etapas separadas para `C_dep^*`, `A_f,post^*`, `D_f^*`, `ΔT_acc^*`; incertidumbre y debilidad | ABIERTO / NO DEMOSTRADO | No Wald; no sustituir tratamiento focal por éxito técnico |
| IV-G3 Independencia/interferencia | Mecanismo/unidad de asignación, clúster, exposición compartida y carryover | ABIERTO | No inferencia IV estándar |
| IV-G4 Exclusión | Inventario y evidencia por rutas focales/alternativas/compartidas/externas/desconocidas; vías B→Outcome/Value | AMENAZA MATERIAL / NO DEMOSTRADA | Interpretar ITT como política/paquete o declarar no identificación |
| IV-G5 Monotonicidad | Justificación sustantiva y DGP con defiers/crowding-out | ABIERTO | No LATE estándar |
| IV-G6 Consistencia/medición | Pin de versiones, recepción/cumplimiento, adjudicación independiente, error diferencial | ABIERTO | No usar `D_f^{obs}` como `D_f^*` |
| IV-G7 Resultado | Outcome y Value separados, regla/beneficiario/horizonte, missingness/censura | ABIERTO | No interpretar un LATE como otro |
| IV-G8 Suite sintética | Truth oculta adversarial para instrumento débil, exclusión, defiers, interferencia, versiones y medición | ESPECIFICACIÓN PENDIENTE DE IMPLEMENTACIÓN | No validar capacidad del analizador para abstenerse |

**Dictamen agregado:** `LATE_f` = NO IDENTIFICADO / NO LISTO PARA WALD. Los gates son requisitos de diseño; su documentación no constituye validación empírica ni autorización de ejecución. `ITT_Z` conserva objeto de efecto de asignación de política y no atribuye automáticamente accesibilidad.



## 38. Crosswalk de dependencias entre identificación IV y medición trivalente

| Dependencia | Referencias reutilizadas | Criterio de aceptación | Estado |
|---|---|---|---|
| IV-G1 ↔ tratamiento/población observables | MEAS-G1…G5/G8; TRI-AF-01…05; TRI-DF-01…06; ID-01…15; SNAP-01…15 | Misma identidad τ2 y snapshots comparables; elegibilidad pre-Z; D_f* no sustituido por D_f_obs | OPEN / PARTIAL |
| IV-G4 ↔ exclusión | MEAS-G4; U_G; B-M01…15; fichas D2-RES/CAP/INFO e invariantes | Rutas y vías colaterales inventariadas por alcance; cobertura negativa suficiente; invariancia demostrada o vía separada/modelada; unknowns materiales no ocultos | MATERIAL THREAT / OPEN |
| IV-G6 ↔ consistencia/medición | MEAS-G2…G8; TRI-OBS-01…03; TRI-DF-01…06; protocolo de adjudicación | Versiones/eventos pinned; ciego y adjudicación; error diferencial/missingness cuantificados o acotados | OPEN |

**Regla de no equivalencia:** completar medición no demuestra exclusión, monotonicidad, independencia ni ausencia de interferencia. La regla trivalente evita falsos ceros; no convierte la cobertura documental en evidencia material. LATE_f permanece NO IDENTIFICADO / NO LISTO PARA WALD.



## 39. Seguimiento de exclusión por superficies B-M01…15

| Bloque | Superficies | Requisito de evidencia | Estado de cierre |
|---|---|---|---|
| Focal capturado | B-M01/B-M02/B-M04/B-M08/B-M09 | Contrato funcional limitado a τ2; diff/versiones; prueba de que funciones extra, seguridad, permisos, rutas y recursos no introducen vías paralelas | PARCIAL / NO DEMOSTRADO |
| Datos/aplicabilidad | B-M06 | Snapshots/hash, estado X, entradas/salidas, F*, App y Outcome separados; prueba de no cambio fuera de D_f* | ABIERTO |
| Recursos/capacidad | B-M07 | Disponibilidad, reservas, consumo, colas, consumidores y no desplazamiento de A1/A2/F2; unidad/ventana | ABIERTO |
| Autorización | B-M05 | Fuente normativa, ACL técnica separada y C_auth,base común pre-Z | ABIERTO |
| Conocimiento/medición | B-M10 | Comunicaciones/K por brazo; E_T, cobertura, missingness, cegamiento y adjudicación | ABIERTO |
| Integridad de Outcome | B-M13 | Oráculo, dataset, regla y versión inmutables; separación de B | ABIERTO |
| Seguridad/rendimiento/estado | B-M09/B-M11/B-M12 | Riesgo/coste, residuos/cachés, latencia/throughput, snapshots y métricas comparables | ABIERTO |
| Alternativas | B-M03/B-M08/B-M14 | Grafo y pruebas funcionales A1/A2/F2 pre/post, dependencias compartidas y margen de equivalencia | ABIERTO |
| Reversibilidad/interferencia | B-M02/B-M03/B-M07/B-M08/B-M11/B-M12/B-M14/B-M15 | Consumidores, recursos compartidos, unidades/periodos, rollback, spillover y carryover | ABIERTO |

**Dictamen agregado:** IV-G4 permanece ABIERTO; exclusión NO DEMOSTRADA. La ausencia de cambio debe probarse con cobertura completa relevante; inventario documental o invariancia postulada no son evidencia material. LATE_f no listo para Wald.

## 40. Control de aceptación de escenarios adversariales Opción A

| Control | Escenario discriminante | Criterio de aceptación documental | Estado |
|---|---|---|---|
| DGP-EXC-01 | R0 / EXC-F0 focal exclusiva | Solo D_f* cambia por B; ausencia de rutas colaterales estipulada y verificable dentro del DGP; gates IV restantes separados | OPEN |
| DGP-EXC-02 | R1 alternativa basal estable | A1→A2 permanece estable; no marcar violación de exclusión por mera existencia; permitir Reach constante y efecto heterogéneo/nulo | OPEN |
| DGP-EXC-03 | R2 alternativa afectada por B | A1/A2 cambia por B; clasificar ruta colateral y efecto de paquete/no LATE_f focal | OPEN |
| DGP-EXC-04 | R3 intento/provisión fallida | W_attempt separado de C_dep*/D_f*; distinguir primera etapa nula/débil y posibles costes/residuos | OPEN |
| DGP-EXC-05 | B→Outcome directo | Outcome verdadero cambia sin mediación por D_f*; exclusión focal falla | OPEN |
| DGP-EXC-06 | B→Value directo | Value verdadero cambia con Outcome constante; no asumir O→V completo | OPEN |
| DGP-EXC-07 | K/conocimiento diferencial | B cambia K/selección/ejecución fuera de D_f*; no ajustar por mediador post-Z | OPEN |
| DGP-EXC-08 | Medición/oráculo diferencial | Distinguir estado verdadero, observación y definición de resultado; no comparabilidad/missingness | OPEN |
| DGP-EXC-09 | Recursos compartidos/carryover | Mapa de exposición y unidad/clúster; rechazar SUTVA/Wald individual si procede | OPEN |

Los controles son especificaciones, no resultados PASS. Ningún escenario está serializado o ejecutado. La aceptación requiere correspondencia con variables/tiempos/roles y expected_output por Outcome y Value.



## 41. Control de cierre del crosswalk temporal y de roles Opción A

| Control | Criterio | Estado |
|---|---|---|
| DGP-TIME-01 | Reloj único t−1/t0–t9/t+1…; cada escenario mapea manipulación y resultado al momento correcto | DOCUMENTADO / NO VALIDADO |
| DGP-ROLE-01 | Generador, analizador y evaluador separados; truth/potenciales ocultos al analizador | DOCUMENTADO / NO IMPLEMENTADO |
| DGP-SEM-01 | Opción A seleccionada por DEC-C10-051; contrato funcional versionado de F1/τ2, adaptador, F2, A1/A2 y F* aún no cerrado | OPEN |
| DGP-OUT-01 | O*/O_obs y V*/V_obs, oráculos, regla Value, beneficiario/horizonte diferenciados | OPEN |
| DGP-INT-01 | Unidad de interferencia, pool, mapa de exposición y asignación/análisis cluster | OPEN |
| DGP-CARRY-01 | Snapshots t+1…, rollback y washout/carryover por unidad/periodo | OPEN |
| DGP-CROSS-01 | Crosswalk escenario×variable×tiempo×rol y controles invariantes completos | DOCUMENTADO / REQUIERE RECONCILIACIÓN |

El documento DGP §28 y la auditoría IV §13 son referencias de este control. Ningún estado DOCUMENTADO equivale a PASS de prueba; los escenarios no están parametrizados ni ejecutados.

**Dictamen agregado:** prerequisitos para parametrización abiertos; no Design Freeze ni implementación.



## 42. Control de reconciliación funcional Opción A

| Control | Criterio | Estado |
|---|---|---|
| FUNC-B-01 | B/adaptador provisiona dependencia; no ejecuta F1/F2/A1/A2 ni aplica configuración | DOCUMENTADO / NO VALIDADO |
| FUNC-DEP-01 | C_dep* se distingue de A_f*(τ2), DEP_f*, App_f y F* | DOCUMENTADO / NO IMPLEMENTADO |
| FUNC-F1-01 | F1/τ2 convierte S0→S2; S2 no equivale a estado aplicado | DEFINIDO A NIVEL FUNCIONAL / CONTRATO OPERACIONAL OPEN |
| FUNC-F2-01 | F2 aplica S2→SF y verifica destino, con condiciones propias | DEFINIDO A NIVEL FUNCIONAL / CONTRATO OPERACIONAL OPEN |
| FUNC-A-01 | A1/A2 componen ruta basal S0→S1→SF | DEFINIDO A NIVEL FUNCIONAL / NO-AFECTACIÓN POR B OPEN |
| FUNC-FSTAR-01 | F* se adjudica sobre ruta completa con FP-01…07; FP-08 probatorio separado | DOCUMENTADO / IAM Y ORÁCULO OPEN |
| FUNC-EQUIV-01 | Substituibilidad exige mismo F*, entrada, destino, IAM, C0/G/H y evidencia | DOCUMENTADO / NO VALIDADO |
| FUNC-ALT-01 | R1 alternativa basal estable distinta de R2 alternativa afectada por B | DOCUMENTADO / NO VALIDADO |

**Dictamen:** semántica funcional de alto nivel reconciliada; no implica cierre operacional, causal, empírico o técnico. Sin freeze ni implementación.


## 43. Crosswalk del objeto de configuración

OBJ-CARD-01: CMP≥1, PAR≥1, RUL≥1; REF≥0 con IAM/cobertura; POL condicional; MET obligatorio (DEC-C10-056, alcance cerrado). OBJ-MAP-01: M tipado/versionado por clase y etapa (estructura documentada, instancia abierta). OBJ-STATE-01: DEFAULT y subclases aún no reconciliadas (propuesta/decisión abierta). OBJ-RULE-01: AST acíclico 4/16/16 y REQUIRE/FORBID (perfil aceptado, no implementado). OBJ-IAM-01: O/C/NA/? sellado pre-Z/B (IAM abierto). OBJ-APPLIED-01: C_dst declarado distinto del aplicado (evidencia abierta). OBJ-FSTAR-01: mismo IAM/entrada/destino/C0/G/H/F* para ambas rutas (no validado). OBJ-ALT-01: equivalencia F* y no-afectación por B (no validado).

Dictamen: crosswalk documental parcial; sin freeze, fixtures, parser, oráculo validado ni ejecución.


## 44. Control de coherencia DEFAULT

| Control | Criterio | Estado |
|---|---|---|
| DEF-STATE-01 | PAR usa ABSENT/NULL/DEFAULT/VALUE | CONTRATO ABSTRACTO |
| DEF-KIND-01 | Si DEFAULT, distinguir DECLARED/INHERITED con regla y procedencia | DEC-C10-054 ACEPTADA / REPRESENTACIÓN DOCUMENTADA |
| DEF-ENV-01 | ENV_RESOLVED pertenece a snapshot E_dst, no a PAR/C_src/C_dst | DEC-C10-054 ACEPTADA / SEPARACIÓN DOCUMENTADA |
| DEF-UNK-01 | Fuente no distingue origen → UNKNOWN salvo evidencia independiente | REGLA DOCUMENTADA / ORÁCULO OPEN |
| DEF-EQ-01 | Igualdad de valor resuelto no prueba equivalencia de origen/contrato | REGLA DOCUMENTADA / FP OPEN |

No se abre DEC nueva ni se cierra la parametrización por clave, snapshot E_dst, evidencia u oráculo.

## 45. Control de especialización del roster PAR

| Control | Criterio | Estado |
|---|---|---|
| PAR-ROSTER-01 | Tres roles candidatos BOOL/ENUM/INT, sin claves reales | PROPUESTA DOCUMENTADA |
| PAR-ROSTER-02 | Pertinencia de cada slot dentro de P0 y owner CMP | OPEN |
| PAR-ROSTER-03 | D_profile finito y N_retry_max finito por fijar | OPEN |
| PAR-ROSTER-04 | Estados y defaults por clave coherentes con DEC-C10-054 | ESTRUCTURA DOCUMENTADA / DETALLE OPEN |
| PAR-ROSTER-05 | Mapping total ENUM y preservación BOOL/INT | OPEN |
| PAR-ROSTER-06 | RUL≥1 sustantiva y vinculada al contrato | OPEN |
| PAR-ROSTER-07 | IAM pre-Z/B, cobertura, oráculo y evidencia | OPEN |

El roster no es instancia, fixture, parámetro aprobado ni contrato congelado.

## 46. Controles de cierre sustantivo RUL

| Control | Criterio | Estado |
|---|---|---|
| RUL-SUB-01 | Fuente funcional y regla constitutiva P0 | ACEPTADO CONCEPTUALMENTE POR DEC-C10-068: contrato sintético interno al DGP |
| RUL-SUB-02 | Regla no tautológica con permitido y violador conocidos | ACEPTADO CONCEPTUALMENTE: ENABLED=true × STANDARD/READ_ONLY frente a DISABLED |
| RUL-SUB-03 | Owner CMP, scope, claves, dominios y versión de instancia | Scope/IDs lógicos aceptados; identidad/versionado concreto OPEN |
| RUL-SUB-04 | AST acíclico 4/16/16 y efecto REQUIRE/FORBID | Perfil de gramática aceptado; instancia RUL aceptada conceptualmente, serialización/verificación OPEN |
| RUL-SUB-05 | UNKNOWN trivalente, propagación y adjudicación | Regla general documentada; adjudicación/oráculo OPEN |
| RUL-SUB-06 | Mapping/preservación F1/A1 y aplicación F2/A2 | Invariantes especificados; mapping concreto y evidencia OPEN |
| RUL-SUB-07 | FP-03/06/07, oráculo independiente y falsadores | Contratos conceptuales; pruebas y oráculo OPEN |

DEC-C10-068 acepta ENABLED→PROFILE como regla constitutiva del mundo sintético. El cierre es conceptual, no operacional: RUL≥1 no se marca como implementado, probado ni congelado.

## 47. Control de cierre del contrato funcional sintético RUL

| Control | Criterio | Estado |
|---|---|---|
| SVC-RUL-01 | Unidad lógica coherente con DEC-C10-051/052/057/058 | Base decisional aceptada |
| SVC-RUL-02 | Contrato sintético ENABLED/PROFILE y dominios finitos | ACEPTADO CONCEPTUALMENTE — DEC-C10-068 |
| SVC-RUL-03 | RUL-SVC-ENABLE-PROFILE-01 con permitido y violador conocidos | ACEPTADA CONCEPTUALMENTE — DEC-C10-068 |
| SVC-RUL-04 | Owner CMP, scope, versión y procedencia | Owner lógico CMP-SERVICE-LOGIC y scope aceptados; identidad/versionado de instancia OPEN |
| SVC-RUL-05 | Mapping semántico F1/A1 y aplicación F2/A2 | Invariantes especificados; mapping concreto OPEN |
| SVC-RUL-06 | UNKNOWN, FP-03/06/07 y oráculo independiente | OPEN |
| SVC-RUL-07 | Contrastes adversariales y truth segregada | Contratos conceptuales; sin fixtures/pruebas |

DEC-C10-068 acepta el contrato como fuente constitutiva interna de verdad para el DGP. Su versionado/serialización final y congelación pre-generación siguen pendientes. No se presenta como norma externa. No freeze ni implementación.

## 48. Control de propagación de DEC-C10-068

| Control | Criterio | Estado |
|---|---|---|
| DEC068-01 | Servicio lógico sintético y unidad funcional de referencia | ACEPTADO CONCEPTUALMENTE |
| DEC068-02 | PAR-SVC-ENABLED BOOL y PAR-SVC-PROFILE ENUM con dominios declarados | ACEPTADOS CONCEPTUALMENTE |
| DEC068-03 | RUL-SVC-ENABLE-PROFILE-01, REQUIRE, implicación unidireccional | ACEPTADA CONCEPTUALMENTE |
| DEC068-04 | Fuente constitutiva interna al DGP y verdad fijada ex ante | ACEPTADA; no norma externa |
| DEC068-05 | CMP concreto, versión de instancia y serialización | OPEN |
| DEC068-06 | IAM detallado, mapping físico, tolerancias y oráculo | OPEN |
| DEC068-07 | Fixtures, pruebas, implementación y ejecución | NO AUTORIZADOS / NO EJECUTADOS |

Registro: `00_GOVERNANCE/decisions/DEC-C10-068_SYNTHETIC_SERVICE_FUNCTIONAL_CONTRACT_ACCEPTANCE.md`. No constituye Design Freeze.

## 49. Control de identidad y versionado CMP de la instancia sintética

| Control | Criterio | Estado |
|---|---|---|
| CMP-ID-01 | Separar contract_id, instance_id, component_id y component_class | Especificado en propuesta; pendiente de aceptación |
| CMP-ID-02 | Separar contract_version, instance_version y hash de artefacto | Política propuesta; pendiente de aceptación |
| CMP-ID-03 | Reutilizar contrato abstracto de instancia y matching snapshots | Crosswalk documentado; instanciación pendiente |
| CMP-ID-04 | Identidad candidata C10S-SVC-REQUEST-PROCESSOR / C10S-SVC-REQUEST-PROCESSOR-001 / CMP-SERVICE-LOGIC-001 | Propuesta, no canónica |
| CMP-ID-05 | Enlazar MET con C_src/C_dst, M, IAM y oráculo versionados | Campos heredados definidos; valores/serialización OPEN |
| CMP-ID-06 | Hash calculado solo sobre serialización canónica congelada | Regla propuesta; no hash generado |
| CMP-ID-07 | Matching de snapshots con identidad/frontera/granularidad/cobertura | Contrato existente; cierre por instancia OPEN |

Documento: `C10_S_SERVICE_CMP_INSTANCE_IDENTITY_VERSIONING_PROPOSAL_DRAFT_001.md`. No crea instancia ejecutable ni cierra F*. No Design Freeze ni autorización de implementación/ejecución.

## 45. Control de roster PAR y alcance aceptado por DEC-C10-068

| Control | Criterio | Estado |
|---|---|---|
| PAR-ROSTER-01 | ENABLED BOOL y PROFILE ENUM como núcleo de instancia | ACEPTADO CONCEPTUALMENTE — DEC-C10-068 |
| PAR-ROSTER-02 | RETRY-COUNT dentro del núcleo P0 | EXCLUIDO POR DEC-C10-068 |
| PAR-ROSTER-03 | Dominios ENABLED={false,true}; PROFILE={STANDARD,READ_ONLY,DISABLED} | ACEPTADOS CONCEPTUALMENTE |
| PAR-ROSTER-04 | Estados/defaults por clave y serialización | OPEN; estructura general DEC-C10-054 |
| PAR-ROSTER-05 | Mapping total/versionado y preservación semántica | INVARIANTES DOCUMENTADOS; MAPPING CONCRETO OPEN |
| PAR-ROSTER-06 | IAM por escenario, cobertura y oráculo | OPEN |
| PAR-ROSTER-07 | Identidad CMP/versionado de instancia | PROPUESTA PENDIENTE DE ACEPTACIÓN — §49 |

La tabla histórica de tres slots queda supersedida en cuanto a RETRY-COUNT. No se declara instancia serializada ni IAM sellado.

## 50. Estado de identidad/versionado tras DEC-C10-069

| Control | Criterio | Estado |
|---|---|---|
| CMP-ID-01 | Separar contract_id, instance_id, component_id y component_class | ACCEPTED — DEC-C10-069 |
| CMP-ID-02 | contract_version semver; instance_version entero positivo inmutable | ACCEPTED — DEC-C10-069 |
| CMP-ID-03 | IDs C10S-SVC-REQUEST-PROCESSOR / C10S-SVC-REQUEST-PROCESSOR-001 / CMP-SERVICE-LOGIC-001 | ACCEPTED — DEC-C10-069 |
| CMP-ID-04 | MET enlaza C_src/C_dst, M, IAM, oráculo y procedencia | Especificación documental; serialización/valores OPEN |
| CMP-ID-05 | Hash solo de serialización canónica congelada | Regla ACCEPTED; formato/hash OPEN |
| CMP-ID-06 | Matching de snapshots con identidad/frontera/granularidad/cobertura | Regla aceptada; aplicación/evidencia OPEN |
| CMP-ID-07 | Mapping semántico CMP/PAR/RUL entre F1/A1 y F2/A2 | NEXT GATE — OPEN |

Registro: `00_GOVERNANCE/decisions/DEC-C10-069_SERVICE_CMP_IDENTITY_AND_VERSIONING_ACCEPTANCE.md`. No instancia ejecutable, no Design Freeze ni autorización de implementación/ejecución.

## 50. Estado del gate CMP-ID-07 — mapping semántico CMP/PAR/RUL

| ID | Requisito | Estado |
|---|---|---|
| CMP-ID-07a | Identidad lógica CMP, clase, owner y cardinalidad de referencia | DOCUMENTED PROPOSAL — matriz §20.2; IAM/cobertura OPEN |
| CMP-ID-07b | Mapping semántico PAR-SVC-ENABLED BOOL | DOCUMENTED PROPOSAL — matriz §20.3 |
| CMP-ID-07c | Mapping semántico PAR-SVC-PROFILE ENUM total e inyectivo | DOCUMENTED PROPOSAL — matriz §20.3 |
| CMP-ID-07d | Mapping RUL-SVC-ENABLE-PROFILE-01: identidad, scope, AST, operandos y REQUIRE | DOCUMENTED PROPOSAL — matriz §20.4 |
| CMP-ID-07e | Separación F1/A1 preservación y F2/A2 aplicación; FP-06/07 | DOCUMENTED PROPOSAL — matriz §20.5 |
| CMP-ID-07f | Evidencia, truth/analyst/oracle y 1/0/?/NA | DOCUMENTED PROPOSAL — matriz §20.6 |
| CMP-ID-07g | Aceptación de mapping, IAM sellado, mapping físico y oráculo | OPEN |

Referencia: C10_S_ABSTRACT_PARAMETER_AND_SOURCE_DESTINATION_MAPPING_MATRIX_DRAFT_001.md §20. La propuesta no es freeze, validación ni autorización de implementación/ejecución.

## 51. Estado del gate IAM-ORACLE-08 — reconciliación de identidad y adjudicación

| ID | Requisito | Estado |
|---|---|---|
| IAM-ORACLE-08a | Reconciliar identidad contract/instance/CMP con DEC-C10-069 | DOCUMENTED / DECISION ACCEPTED |
| IAM-ORACLE-08b | Separar CMP focal de cardinalidad global e inventario P1 | DOCUMENTED REQUIREMENT |
| IAM-ORACLE-08c | IAM por ruta, etapa, objeto, propiedad y snapshot | DOCUMENTED REQUIREMENT; instanciación OPEN |
| IAM-ORACLE-08d | Distinguir C_src, S1/S2, C_dst declarado/aplicado y E_dst | DOCUMENTED REQUIREMENT |
| IAM-ORACLE-08e | Separar truth DGP, salida Analizador y adjudicación Evaluador | DOCUMENTED REQUIREMENT |
| IAM-ORACLE-08f | Adjudicación 1/0/?/NA/SCOPE_ERROR y suficiencia de cobertura | DOCUMENTED REQUIREMENT; criterios concretos OPEN |
| IAM-ORACLE-08g | Mapping_id, IAM_id, oracle_id/version, roster, snapshots y evidencia | OPEN |
| IAM-ORACLE-08h | Valores/defaults, mapping AST, UNKNOWN/conflicto, cegamiento y serialización | OPEN |

Referencia: C10_S_PROPERTY_APPLICABILITY_AND_OBLIGATORINESS_MATRIX_DRAFT_001.md §17. Requisitos documentales no equivalen a aceptación, freeze, validación ni autorización de implementación/ejecución.

## 52. Estado del gate ROSTER-IAM-09 — roster funcional mínimo

| ID | Requisito | Estado |
|---|---|---|
| ROSTER-IAM-09a | CMP focal y versión aceptados por DEC-C10-069 | ACCEPTED |
| ROSTER-IAM-09b | Dos PAR y RUL funcional aceptados por DEC-C10-068 | ACCEPTED |
| ROSTER-IAM-09c | MET obligatorio y POL fuera del núcleo mínimo | ACCEPTED / DECISION-BASED |
| ROSTER-IAM-09d | RETRY-COUNT excluido del roster confirmatorio | SUPERSEDED BY DEC-C10-068 |
| ROSTER-IAM-09e | Estados/defaults de PAR sin defaults inventados | DOCUMENTED REQUIREMENT |
| ROSTER-IAM-09f | Inventario exhaustivo CMP/PAR/RUL/REF por snapshot | OPEN |
| ROSTER-IAM-09g | Cobertura, REF=0, valores por escenario y mapping/IAM/oracle IDs | OPEN |
| ROSTER-IAM-09h | IAM O/C/NA/? sellado pre-Z/B | OPEN |

Referencia: matriz IAM §18. El roster funcional mínimo no equivale a inventario exhaustivo, IAM sellado, Design Freeze o autorización de ejecución.

## 53. Estado del gate SNAPSHOT-INVENTORY-10 — captura de configuración C10-S

| ID | Requisito | Estado |
|---|---|---|
| SNAPSHOT-INVENTORY-10a | Reutilizar plantilla U_G y esquema DEC-C10-064/065 | DOCUMENTED |
| SNAPSHOT-INVENTORY-10b | No duplicar NODE/PREDICATE con PAR/RUL | DOCUMENTED REQUIREMENT |
| SNAPSHOT-INVENTORY-10c | Crosswalk C_src, S2/S1, C_dst declarado/aplicado por ruta | DOCUMENTED PROPOSAL |
| SNAPSHOT-INVENTORY-10d | Manifiesto por objeto/propiedad enlazado a snapshot/evidencia | DOCUMENTED PROPOSAL; no schema físico |
| SNAPSHOT-INVENTORY-10e | Coverage scopes por snapshot×etapa×ruta×clase | DOCUMENTED REQUIREMENT |
| SNAPSHOT-INVENTORY-10f | Codificación textual determinista de etapa/ruta en SNAPSHOT.scope sin ampliar enum | DOCUMENTED PROPOSAL; ACCEPTANCE/COMPATIBILITY OPEN |
| SNAPSHOT-INVENTORY-10g | Snapshots y evidencia observados; inventario exhaustivo | OPEN / NONE |
| SNAPSHOT-INVENTORY-10h | REF=0 y COMPLETE con denominador/cobertura | OPEN |

Referencias: matriz IAM §19; plantilla U_G §18; contrato abstracto §16; catálogo atómico §15. Protocolo documental no equivale a captura, validación, freeze o autorización.
## 54. Estado del gate COVERAGE-SCOPE-11 — scopes C10-S

| ID | Requisito | Estado |
|---|---|---|
| COVERAGE-SCOPE-11a | Reutilizar COVERAGE_REGISTER §12.3 sin columnas nuevas | DOCUMENTED |
| COVERAGE-SCOPE-11b | Un scope por snapshot exacto×etapa×ruta×clase | DOCUMENTED PROPOSAL |
| COVERAGE-SCOPE-11c | coverage_scope_id opaco/único y dimension C10S_CONFIG_* | DOCUMENTED PROPOSAL |
| COVERAGE-SCOPE-11d | universe_definition/version fija snapshot, stage/route y enumeración | DOCUMENTED REQUIREMENT |
| COVERAGE-SCOPE-11e | Denominadores y COMPLETE diferenciados por CMP/PAR/REF/RUL/MET | DOCUMENTED REQUIREMENT |
| COVERAGE-SCOPE-11f | REF=0 y ausencia PAR REQUIRED solo con cobertura COMPLETE | DOCUMENTED REQUIREMENT |
| COVERAGE-SCOPE-11g | FK inversa COVERAGE_REGISTER→SNAPSHOT exacto | OPEN — esquema vigente no la contiene |
| COVERAGE-SCOPE-11h | Scopes y snapshots observados/poblados | OPEN / NONE |
| COVERAGE-SCOPE-11i | Compatibilidad de SNAPSHOT.scope | OPEN — aceptación y verificación pendientes |

Referencia histórica: IAM §19.7 y plantilla U_G §18.6. Estado actualizado por DEC-C10-070 y §56: C0 aceptada; control independiente OPEN/CONDITIONAL. No se ha alterado el esquema físico. U_G-SCH-10 conserva su gate de validación física separado.

## 55. Reconciliación de COVERAGE-SCOPE-11 y U_G-SCH-10

U_G-SCH-10 (pertenencia/referencias versionadas del grafo) no debe usarse como etiqueta para el vínculo de COVERAGE_REGISTER. Opción A fue aceptada semánticamente mediante DEC-C10-065; su verificación física permanece en el control de schema correspondiente.

| ID | Requisito | Estado |
|---|---|---|
| COVERAGE-SCOPE-11g | Binding coverage_scope_id↔snapshot exacto demostrable por FK compuesta | OPEN — COVERAGE_REGISTER no almacena snapshot_id/snapshot_object_record_id |
| COVERAGE-SCOPE-11g1 | C0: tupla exacta en universe_definition/version + control independiente | ACCEPTED — DEC-C10-070; control OPEN / CONDITIONAL |
| COVERAGE-SCOPE-11g2 | C1: extender COVERAGE_REGISTER y FKs compuestas | NOT ACCEPTED; requiere nueva decisión y análisis de ciclos/legacy/motor |
| COVERAGE-SCOPE-11g3 | C2: tabla puente | NOT ACCEPTED; reconsiderar solo si C1 no es viable |
| U_G-SCH-10 | Pertenencia/referencias de grafo a snapshot | SEMANTIC DESIGN ACCEPTED — DEC-C10-065/Opción A; physical validation OPEN |
| SNAPSHOT.scope | Codificación etapa/ruta C10-S | OPEN — propuesta no aceptada/compatibilidad pendiente |

No se ha cambiado el schema. C0 no equivale a FK ni a validación técnica; C1/C2 no se han aplicado.

## 56. Estado tras DEC-C10-070 — C0 aceptada

| ID | Requisito | Estado |
|---|---|---|
| COVERAGE-SCOPE-11g | Binding documental coverage_scope_id↔snapshot exacto mediante tupla pinneada | ACCEPTED — DEC-C10-070 |
| COVERAGE-SCOPE-11g1 | Esquema físico sin cambios (C0) | ACCEPTED |
| COVERAGE-SCOPE-11g2 | Control independiente: igualdad, unicidad, cardinalidad, huérfanos/no usados y conflictos | OPEN — necesario antes de Design Freeze |
| COVERAGE-SCOPE-11g3 | Control ejecutado y auditado | NOT EXECUTED |
| COVERAGE-SCOPE-11g4 | Enforcement FK compuesta (C1) | NOT ACCEPTED / NOT AUTHORIZED |
| COVERAGE-SCOPE-11g5 | Tabla puente (C2) | NOT ACCEPTED / NOT AUTHORIZED |
| U_G-SCH-10 | Pertenencia del grafo a snapshot (DEC-C10-065/Opción A) | SEMANTICALLY ACCEPTED; physical validation in separate gate |
| SNAPSHOT.scope | Codificación de etapa/ruta | OPEN — sin aceptación |

La aceptación de C0 no declara integridad relacional, no crea scopes ni modifica schema. CONDITIONAL hasta el control independiente auditado.


## 57. Descomposición del control C0 — estado documental y gates

| ID | Requisito | Estado |
|---|---|---|
| C0-SPEC-01 | Tupla canónica de nueve componentes contract/instance/snapshot/stage/route/class; dimension separada en COVERAGE_REGISTER | DOCUMENTED — protocolo §19.1; DEC-C10-070 |
| C0-SPEC-02 | Invariantes C0-I01…I11 | DOCUMENTED — protocolo §19.2 |
| C0-SPEC-03 | Reglas denominador/cobertura/REF=0 | DOCUMENTED — protocolo §19.3 |
| C0-SPEC-04 | Semántica trivalente y precedencia | DOCUMENTED — protocolo §19.4 |
| C0-SPEC-05 | Casos adversariales ADV-C0-01…15 | DOCUMENTED / NOT EXECUTED |
| C0-SPEC-06 | Run manifest, provenance y evidencia | DOCUMENTED — protocolo §19.6 |
| C0-GATE-01 | Reconciliar DDL completo y mapping de campos | OPEN |
| C0-GATE-02 | Implementación del control | NOT IMPLEMENTED / NOT AUTHORIZED |
| C0-GATE-03 | Ejecución de casos adversariales | NOT EXECUTED / NOT AUTHORIZED |
| C0-GATE-04 | Auditoría de resultados y falsos PASS/FAIL/UNKNOWN | NOT AUDITED |
| C0-GATE-05 | Cierre C0 para Design Freeze | CONDITIONAL / BLOCKED BY GATES |

La especificación documental no implica implementación, validación física ni ejecución científica. La autorización de C0 como diseño (DEC-C10-070) no autoriza estos gates técnicos.

## 58. Mapping C0↔U_G — gates de correspondencia

| ID | Campo C0 | Estado del esquema | Consecuencia |
|---|---|---|---|
| C0-MAP-01 | contract_id/version | Documental en universe_definition/version | Requiere identidad/versionado recuperable |
| C0-MAP-02 | instance_id/version | Documental en universe_definition/version | Requiere vínculo verificable |
| C0-MAP-03 | snapshot_id + snapshot_object_record_id | Representado por Opción A/DEC-C10-065 | Comparación exacta obligatoria |
| C0-MAP-04 | stage_key | Sin columna propia; phase no equivalente; scope no aceptado | OPEN — UNKNOWN |
| C0-MAP-05 | route_id | Directo en ROUTE/PREDICATE/ROUTE_STEP; no directo en NODE/EDGE | OPEN — crosswalk/exhaustividad |
| C0-MAP-06 | object_class CMP/PAR/REF/RUL/MET | Sin campo común tipado | OPEN — crosswalk semántico |
| C0-MAP-07 | dimension | COVERAGE_REGISTER; no común en consumidores | OPEN — asociación por mapping |
| C0-MAP-08 | universe_definition/version | Campo existente; gramática/hash no cerrados | OPEN — versionado/provenance |

No puede emitirse PASS completo del control C0 hasta resolver los mappings aplicables. UNKNOWN es obligatorio si falta correspondencia; contradicción demostrada es FAIL. No se infiere por nombre, phase, semantic_role ni texto libre.


## 59. Crosswalk semántico C0↔U_G — estado tras DEC-C10-071

| ID | Eje / correspondencia | Dictamen actual | Estado |
|---|---|---|---|
| C0-XW-01 | object_class C10 vs ug_record_type | Ejes distintos; mapping explícito 1:N/N:M | DOCUMENTED PROPOSAL |
| C0-XW-02 | ug_record_type vs NODE.semantic_role / boundary_class | No equivalencia; preservar DEC-C10-059/060 | ACCEPTED BASELINE |
| C0-XW-03 | stage_key C10-S | Siete valores cerrados por DEC-C10-071: C_SRC, F1_S2, A1_S1, F2_DST_DECL, A2_DST_DECL, F2_DST_APPLIED, A2_DST_APPLIED | ACCEPTED VOCABULARY |
| C0-XW-04 | DGP time t−1…t9 vs stage_key | Ejes distintos; mapping solo por regla explícita | NO EQUIVALENCE |
| C0-XW-05 | stage_key vs SNAPSHOT.phase | phase=baseline/post-B/rollback/route-test; no equivalencia | NO AUTOMATIC MAPPING |
| C0-XW-06 | SNAPSHOT.scope | Codificación de etapa/ruta no aceptada; DEC-C10-070/071 no la aprueban | NOT ACCEPTED |
| C0-XW-07 | route_family F/A vs route_id | F/A es etiqueta auxiliar; C0 exige route_id exacto o token global reservado | OPEN |
| C0-XW-08 | NODE/EDGE route membership | ROUTE_STEP y record IDs exactos | DOCUMENTED RULE; exhaustividad OPEN |
| C0-XW-09 | PREDICATE/ROUTE route membership | route_record_id exacto / propia revisión de ROUTE | DOCUMENTED RULE |
| C0-XW-10 | object_class=CONFIG de §18.2 | No satisface C0; C0 conserva CMP/PAR/REF/RUL/MET | NOT ADOPTED FOR C0 |
| C0-XW-11 | CMP/PAR/REF/RUL/MET | Mappings candidatos a NODE/propiedades/EDGE/PREDICATE/MET transversal | CANDIDATE |
| C0-XW-12 | dimension | COVERAGE_REGISTER.dimension; C10S_CONFIG_*; fuera de tupla | DOCUMENTED |
| C0-XW-13 | Tupla C0 | Nueve componentes conforme a DEC-C10-070 | RECONCILED |

DEC-C10-071 cierra únicamente el vocabulario stage_key. Permanecen OPEN el token global, route_id exacto por universo, gramática completa de universe_definition/version y mappings por propiedad. No se crean columnas, scopes ni snapshots; no se reabre Opción A ni se autoriza implementación/ejecución.


## 60. Scope global y route-specific — gate documental

| ID | Requisito | Criterio / límite | Estado |
|---|---|---|---|
| C0-RT-01 | route_id semántico | Debe resolver route_record_id y snapshot exactos en universe_definition/version | OPEN |
| C0-RT-02 | Token global | Candidato G1 `C10S_SCOPE_GLOBAL`; significa sin restricción a ruta, no ausencia/no pertenencia | PROPOSED — NOT ACCEPTED |
| C0-RT-03 | Alternativas | G2 NULL/vacío ambiguo; G3 scope_kind separado requiere reabrir estructura/tupla | COMPARED |
| C0-RT-04 | CMP/PAR/REF/RUL/MET | Crosswalk por clase/owner/propiedad; no inferir por nombre | DOCUMENTED PROPOSAL |
| C0-RT-05 | Multi-ruta | Scopes route-specific separados; scope global cuenta objeto una vez; no sumar denominadores | DOCUMENTED PROPOSAL |
| C0-RT-06 | Adjudicación | 1 exacto; 0 solo no pertenencia a ruta con universo/ROUTE_STEP completos; ? incompleto; NA IAM ex ante | DOCUMENTED PROPOSAL |

No se acepta el token ni se modifica schema. La gramática de universe_definition/version, el mapping físico por propiedad y el control C0 implementado/auditado siguen OPEN/CONDITIONAL. No scopes/snapshots ni ejecución autorizados.


## 61. DEC-C10-072 — actualización del gate de scope global

| ID | Requisito | Criterio / límite | Estado |
|---|---|---|---|
| C0-RT-01 | route_id route-specific | Resolver route_record_id y snapshot exactos en universe_definition/version | OPEN |
| C0-RT-02 | Token global | Literal reservado `C10S_SCOPE_GLOBAL`, “sin restricción a ruta concreta”; colisión con route_id real = FAIL | ACCEPTED — DEC-C10-072 |
| C0-RT-03 | Alternativas | G1 aceptada; G2 NULL/vacío descartada por ambigüedad; G3 scope_kind no adoptada | DECIDED |
| C0-RT-04 | CMP/PAR/REF/RUL/MET | Crosswalk físico por clase/owner/propiedad, sin inferencia nominal | OPEN |
| C0-RT-05 | Multi-ruta | Scope global cuenta una vez por identidad; scopes route-specific con denominadores separados | ACCEPTED SEMANTICS |
| C0-RT-06 | Adjudicación | 1 exacto; 0 solo no pertenencia a ruta con universo/ROUTE_STEP completos; ? incompleto; NA IAM ex ante | DOCUMENTED PROPOSAL |

La aceptación del token no cierra la gramática universe_definition/version ni el control C0 independiente implementado/auditado. No schema change ni ejecución autorizados.



## 62. UDG-01 — gates de gramática universe_definition

| ID | Requisito | Criterio | Estado |
|---|---|---|---|
| UDG-01 | Envelope | JSON autocontenido; scope replica tupla C0 de nueve componentes | PROPOSED |
| UDG-02 | Identidad | schema_id/version, universe_id/revision separados de contrato/instancia | PROPOSED |
| UDG-03 | Membership | EXPLICIT con member_refs tipados o RULE_DEFINED con regla/dependencias exactas | PROPOSED |
| UDG-04 | Exhaustividad | fuentes/manifiestos + declared_member_count; cero exige evidencia exhaustiva | PROPOSED |
| UDG-05 | Route binding | route-specific resuelve route_record_id; global usa C10S_SCOPE_GLOBAL | ALIGNED WITH DEC-C10-072 |
| UDG-06 | Canonicalización | UTF-8/NFC, orden determinista, SHA-256 candidato | PROPOSED |
| UDG-07 | Versionado | schema_version semver; universe_revision monotónica/inmutable | PROPOSED |
| UDG-08 | Integridad | igualdad scope externo/interno, referencias, cardinalidad, duplicados, provenance | PROPOSED |
| UDG-09 | Adjudicación | PASS solo exhaustivo; FAIL contradicción; UNKNOWN no resoluble | PROPOSED |

La aceptación del token global no acepta UDG-01. Gramática, canonicalización/hash y mapping físico permanecen abiertos. No parser/validator, schema change, fixtures ni ejecución autorizados.


## 63. DEC-C10-073 — actualización del gate UDG-01

| ID | Requisito | Criterio | Estado |
|---|---|---|---|
| UDG-01 | Arquitectura envelope | U1 JSON autocontenido/versionado | ACCEPTED — DEC-C10-073 |
| UDG-02 | Scope | Réplica exacta de tupla C0 de nueve componentes; dimension fuera | ACCEPTED |
| UDG-03 | Membership | EXPLICIT con referencias tipadas o RULE_DEFINED con regla/dependencias exactas | ACCEPTED — arquitectura |
| UDG-04 | Exhaustividad | Fuentes/manifiestos, cardinalidad; cero requiere prueba exhaustiva | ACCEPTED — criterio |
| UDG-05 | Route binding | Route-specific resuelve route_record_id; global usa C10S_SCOPE_GLOBAL | ALIGNED — DEC-C10-072 |
| UDG-06 | Canonicalización/hash | UTF-8/NFC, orden y SHA-256 son propuestas, no requisitos | OPEN |
| UDG-07 | Versionado | Separación schema_version/universe_revision aceptada; reglas completas abiertas | PARTIAL / OPEN |
| UDG-08 | Integridad | Igualdad scope, referencias, cardinalidad, duplicados y provenance | ACCEPTED — criterio documental |
| UDG-09 | Adjudicación | PASS exhaustivo; FAIL contradicción; UNKNOWN no resoluble | ACCEPTED — criterio documental |

No equivale a schema freeze ni autoriza parser, validator, fixtures, mapping físico, implementación o ejecución.


## 64. UDG-02 — gates de canonicalización e integridad

| ID | Requisito | Criterio | Estado |
|---|---|---|---|
| UDG-10 | Perfil | C1 RFC 8785 JCS + prevalidación TGCV vs C2 propio vs C3 raw bytes | COMPARED — C1 RECOMMENDED |
| UDG-11 | Unicode | JCS preserva strings; NFC previa solo en campos marcados, sin autocorrección | PROPOSED |
| UDG-12 | Arrays | Set-valued arrays ordenados por identidad antes de JCS; secuencias preservadas | PROPOSED |
| UDG-13 | Números/null | Enteros seguros no negativos; null prohibido; omisión ≠ [] | PROPOSED |
| UDG-14 | Hashes | source_artifact_hash separado de canonical_content_hash SHA-256 externo al envelope | PROPOSED |
| UDG-15 | Semántica | Igual hash/perfil = mismos bytes canónicos, no equivalencia semántica/exhaustividad | PROPOSED |
| UDG-16 | Perfil/versiones | Perfil identificado/versionado; perfiles distintos no comparables sin recanonicalización | PROPOSED |

UDG-02 no está aceptada. No hash de producción, parser/validator, fixtures, schema change ni ejecución autorizados.


## 65. DEC-C10-074 — estado de canonicalización UDG-02

| ID | Requisito | Criterio | Estado |
|---|---|---|---|
| UDG-10 | Perfil | RFC 8785 JCS + prevalidación TGCV; TGCV-C10S-JCS-1 | ACCEPTED — DEC-C10-074 |
| UDG-11 | Unicode | NFC previa solo en campos marcados; sin reescritura | ACCEPTED |
| UDG-12 | Arrays | Conjuntos ordenados por identidad antes de JCS; secuencias preservadas | ACCEPTED |
| UDG-13 | Números/null | Enteros seguros no negativos; null prohibido; omisión ≠ [] | ACCEPTED |
| UDG-14 | Hashes | SHA-256 canónico separado de hash de fuente; metadatos fuera del envelope | ACCEPTED — política documental |
| UDG-15 | Semántica | Igual hash/perfil ≠ equivalencia semántica/exhaustividad | ACCEPTED |
| UDG-16 | Perfil/versiones | Perfil identificado; perfiles diferentes requieren recanonicalización o UNKNOWN | ACCEPTED — principio |

No hash de producción, parser/validator, fixtures, schema change, Design Freeze ni ejecución autorizados.


## 66. UDG-03 — gates de comparación semántica de universos

| ID | Requisito | Criterio | Estado |
|---|---|---|---|
| UDG-17 | Niveles | Artefacto, canónico, identidad, revisión, extensional, definicional y compatibilidad separados | PROPOSED |
| UDG-18 | Scope comparability | C0 + stage_key + route/route_record + snapshot exactos o mapping explícito | PROPOSED |
| UDG-19 | Membership equality | Conjuntos completos de refs tipadas/versionadas idénticos | PROPOSED |
| UDG-20 | Definition equivalence | Reglas/AST/domínios/dependencias e inclusión/exclusión equivalentes | PROPOSED |
| UDG-21 | Result codes | EQUAL/DIFFERENT/UNKNOWN/NOT_COMPARABLE; FAIL integridad | PROPOSED |
| UDG-22 | Revision compatibility | Relación dirigida demostrada; no inferida por número/cardinalidad | PROPOSED |

No comparator/fingerprint semántico, fixtures, schema change, Design Freeze ni ejecución autorizados.


## 67. DEC-C10-075 — estado de comparación semántica UDG-03

| ID | Requisito | Criterio | Estado |
|---|---|---|---|
| UDG-17 | Niveles | Siete dimensiones de comparación separadas | ACCEPTED — DEC-C10-075 |
| UDG-18 | Scope comparability | C0 + stage_key + route/route_record + snapshot; mapping explícito si cambia contrato/instancia | ACCEPTED |
| UDG-19 | Membership equality | Conjuntos exhaustivos de refs tipadas/versionadas | ACCEPTED |
| UDG-20 | Definition equivalence | Inclusión/exclusión/reglas/AST/domínios/dependencias equivalentes | ACCEPTED |
| UDG-21 | Result codes | EQUAL/DIFFERENT/UNKNOWN/NOT_COMPARABLE; FAIL integridad | ACCEPTED |
| UDG-22 | Revision compatibility | Relación dirigida demostrada, no inferida por número/cardinalidad | ACCEPTED |

Aceptación documental; comparator/fingerprint, fixtures, parser/validator, schema change, Design Freeze e implementación/ejecución no autorizados. DEC-C10-075 prevalece sobre §66.


## 68. UDG-04 — gates de identidad y resolución de referencias

| ID | Requisito | Criterio | Estado |
|---|---|---|---|
| UDG-23 | Identidad lógica | object_class + object_id | PROPOSED |
| UDG-24 | Identidad de registro | object_class + object_id + object_record_id inmutable | PROPOSED |
| UDG-25 | Ref tipada | ref_role + target class/id/record_id exactos | PROPOSED |
| UDG-26 | Resolución | Registry versionado/scope explícito; sin latest/nombre/hash fallback | PROPOSED |
| UDG-27 | Estados | FAIL vs UNKNOWN vs NOT_COMPARABLE vs NOT_APPLICABLE separados | PROPOSED |
| UDG-28 | Ciclos/cardinalidad | Declarados por relación/clase; sin DAG universal asumido | PROPOSED |
| UDG-29 | Pertenencia | Resolución no implica membership/applicability/execution | PROPOSED |

UDG-04 NO ACEPTADA; schema/API/resolver/parser/validator/fixtures/implementación/ejecución no autorizados.


## 69. DEC-C10-076 — estado de identidad y resolución UDG-04

| ID | Requisito | Criterio | Estado |
|---|---|---|---|
| UDG-23 | Identidad lógica | object_class + object_id | ACCEPTED — DEC-C10-076 |
| UDG-24 | Identidad de registro | object_class + object_id + object_record_id inmutable | ACCEPTED |
| UDG-25 | Ref tipada | ref_role + target class/id/record_id | ACCEPTED |
| UDG-26 | Resolución | Registry versionado/scope explícito; sin latest/fallback | ACCEPTED |
| UDG-27 | Estados | FAIL/UNKNOWN/NOT_COMPARABLE/NOT_APPLICABLE separados | ACCEPTED |
| UDG-28 | Ciclos/cardinalidad | Por relación/contrato; sin DAG universal | ACCEPTED |
| UDG-29 | Pertenencia | Resolver no implica membership/applicability/preservation/execution | ACCEPTED |

Catálogo REF/schema/API/registry/resolver/parser/validator/comparator/fixtures y mapping CMP/PAR/RUL continúan abiertos. Sin Design Freeze ni ejecución. DEC-C10-076 prevalece sobre §68.

## 70. Reconciliación REF↔UDG-04 — control de cierre documental

| Control | Criterio | Estado |
|---|---|---|
| REF-UDG-01 | REF de configuración separado de referencia envelope y FK U_G | CONDITIONAL — propuesta |
| REF-UDG-02 | Ambos extremos tipados con record_id exacto | OPEN |
| REF-UDG-03 | Endpoint externo tiene namespace/tipo/versión y resolver declarado | OPEN |
| REF-UDG-04 | Mapping REF→EDGE versionado; split/merge/n-aria explícitos | OPEN |
| REF-UDG-05 | Roles MEMBER/OWNER/SOURCE/rules/DEPENDENCY/PROVENANCE no se tratan como enum aceptado | CONDITIONAL |
| REF-UDG-06 | IAM define obligatoriedad/cardinalidad/NA ex ante | OPEN |
| REF-UDG-07 | Dependencia declarada no equivale a instalada/disponible | REQUIRED — límite |
| REF-UDG-08 | FKs U_G y CLAIM_EVIDENCE_LINK no se cuentan como REF de dominio por defecto | REQUIRED — límite |
| REF-UDG-09 | Estados FAIL/UNKNOWN/NOT_COMPARABLE/NOT_APPLICABLE siguen DEC-C10-076 | REQUIRED — límite |

No se concede PASS de schema ni de integridad física. No hay roster observado, fixtures, validator ejecutado ni Design Freeze.

## 71. DEC-C10-077 — estado del gate conceptual REF↔UDG-04

| Control | Criterio | Estado |
|---|---|---|
| REF-UDG-01 | REF de dominio separado de UDG envelope y FK U_G | ACCEPTED — DEC-C10-077 |
| REF-UDG-02 | Identidad propia y extremos tipados | ACCEPTED — conceptual |
| REF-UDG-03 | REF→EDGE solo mediante M explícito/versionado | ACCEPTED — conceptual |
| REF-UDG-04 | No asumir 1:1; parent/group identity para split/merge/n-aria | ACCEPTED — conceptual |
| REF-UDG-05 | Roles UDG siguen ilustrativos, no enum cerrado | ACCEPTED — límite |
| REF-UDG-06 | IAM fija cardinalidad/obligatoriedad por clase×rol×extremo×etapa×scope | OPEN |
| REF-UDG-07 | Dependencia declarada no equivale a instalada/disponible | REQUIRED — límite |
| REF-UDG-08 | FKs U_G no se cuentan como REF por defecto | ACCEPTED — límite |
| REF-UDG-09 | Estados de resolución siguen DEC-C10-076 | ACCEPTED — límite |

No se concede PASS de schema/integridad física ni se autoriza implementación o ejecución.


## 72. DEC-C10-078 — cierre estructural del contrato lógico IAM

| Control | Criterio | Estado |
|---|---|---|
| IAM-LR-01 | Cuatro capas separadas: L1 membership, L2 referencias envelope UDG, L3 extremos funcionales REF, L4 FK/vínculos estructurales U_G | ACCEPTED — DEC-C10-078 |
| IAM-LR-02 | Contrato lógico de fila con identidad, capa, clase origen, regla de identidad, namespace/rol, extremo/dominio destino, cardinalidad, requiredness, trigger, stage/scope/binding, integridad, mapping, evidencia y adjudicación/procedencia | ACCEPTED — estructura documental |
| IAM-LR-03 | Aplicabilidad contextual de campos por capa; sin asumir que todos aplican a todas las capas | ACCEPTED — límite |
| IAM-LR-04 | Vocabulario final de roles UDG (L2) separado de roles funcionales REF (L3) | OPEN — siguiente gate |
| IAM-LR-05 | Dominios y cardinalidades numéricas por clase×rol×extremo×stage_key×scope | OPEN |
| IAM-LR-06 | Valores REQUIRED/OPTIONAL/CONDITIONAL y disparadores | OPEN |
| IAM-LR-07 | Endpoints externos y sus namespaces/tipos/versiones | OPEN |
| IAM-LR-08 | Mapping M concreto, directionality y split/merge/n-aria | OPEN |
| IAM-LR-09 | Reglas concretas de integridad, evidencia y adjudicación por capa | OPEN |

DEC-C10-078 no cierra el gate REF ni concede PASS de schema/integridad física. No crea roster/filas observadas, fixtures ni IAM de instancia. No autoriza DDL, API/registry/resolver, parser/validator, implementación, Design Freeze ni ejecución científica.


## 73. Propuesta de separación de vocabularios IAM L2/L3

| Control | Criterio | Estado |
|---|---|---|
| IAM-VOC-01 | Namespace L2 separado `UDG_ENVELOPE_ROLE`; roles ilustrativos MEMBER/OWNER/SOURCE/INCLUSION_RULE/EXCLUSION_RULE/DEPENDENCY/PROVENANCE con dominios/límites candidatos | PROPOSED — NOT ACCEPTED |
| IAM-VOC-02 | Namespace L3 separado `REF_FUNCTIONAL_ROLE`; role_key y relation_type siguen OPEN | PROPOSED — NOT ACCEPTED |
| IAM-VOC-03 | SOURCE/TARGET se interpreta como endpoint_position binario, no como role_key | ACCEPTED boundary from DEC-C10-078 |
| IAM-VOC-04 | Semántica de DEPENDENCY L2 (referencia a REF vs target directo) | OPEN |
| IAM-VOC-05 | Conjunto mínimo de relaciones REF L3 exigido por el DGP; binario/n-ario | OPEN |
| IAM-VOC-06 | Dominios/cardinalidades/requiredness por clase×rol×extremo×stage_key×scope | OPEN |

La propuesta no crea enums, filas de instancia, REF observados ni IAM poblado. No produce PASS de integridad ni autoriza schema, parser/validator, fixtures, Design Freeze o ejecución.

## 74. DEPENDENCY L2 — propuesta de resolución semántica

| Control | Criterio | Estado |
|---|---|---|
| IAM-DEP-01 | Una dependencia funcional declarada de configuración se representa mediante objeto REF con identidad propia | PROPOSED — NOT ACCEPTED |
| IAM-DEP-02 | L2 DEPENDENCY referencia el REF exacto; extremos de la relación permanecen en L3 | PROPOSED — NOT ACCEPTED |
| IAM-DEP-03 | Dependencias técnicas/ambientales C_dep/E_dst no crean REF automáticamente | PROPOSED — NOT ACCEPTED |
| IAM-DEP-04 | Dependencias de evaluación de universo RULE_DEFINED se mantienen como refs tipadas/versionadas de regla/envelope, no como REF por defecto | PROPOSED — NOT ACCEPTED |
| IAM-DEP-05 | Roster mínimo actual no declara por sí mismo una relación REF; REF=0 exige inventario/cobertura exhaustivos pre-Z/B | CONSISTENT WITH ACCEPTED ROSTER; INSTANCE ADJUDICATION OPEN |
| IAM-DEP-06 | Sin doble contabilización entre referencia L2, objeto REF y objetos endpoint | PROPOSED — NOT ACCEPTED |

Esta propuesta no acepta vocabulario final, cardinalidad ni requiredness; no declara REF presente/ausente y no autoriza schema, resolver, fixtures, parser/validator, implementación, Design Freeze ni ejecución.

## 75. Auditoría del conjunto mínimo REF L3

| Control | Criterio | Estado |
|---|---|---|
| IAM-REFMIN-01 | El roster CMP/PAR/RUL aceptado no exige por sí mismo REF funcional concreto | PROPOSED — DOCUMENTARY AUDIT |
| IAM-REFMIN-02 | Operandos de RUL no se elevan automáticamente a REF | PROPOSED — NO COLLAPSE |
| IAM-REFMIN-03 | R_acc/R* del espacio transformacional no se equiparan a REF del paquete | PROPOSED — NO COLLAPSE |
| IAM-REFMIN-04 | C_dep/E_dst y condiciones ambientales no crean REF automáticamente | PROPOSED — NO COLLAPSE |
| IAM-REFMIN-05 | Dependencias de evaluación RULE_DEFINED no son REF funcionales por defecto | PROPOSED — NO COLLAPSE |
| IAM-REFMIN-06 | REF=0 requiere inventario/cobertura exhaustivos por snapshot×stage_key×ruta×scope | OPEN — NO ADJUDICATED |

No se declara REF=0, no se sella IAM ni se crean filas observadas. Cualquier REF candidato requiere identidad propia de relación y extremos tipados, más semántica y procedencia explícitas.

## 76. Protocolo de auditoría REF por snapshot/etapa

| Control | Criterio | Estado |
|---|---|---|
| IAM-REF-AUD-01 | Unidad de auditoría exacta por contrato/instancia/snapshot/stage_key/ruta/scope/universo versionado | PROPOSED — NOT ACCEPTED |
| IAM-REF-AUD-02 | Reutiliza U_G y COVERAGE_REGISTER; no crea inventario paralelo | ALIGNED WITH EXISTING CONTRACT |
| IAM-REF-AUD-03 | Inspección independiente C_SRC, F1_S2, A1_S1, F2/A2_DECL y F2/A2_APPLIED | PROPOSED — NOT ACCEPTED |
| IAM-REF-AUD-04 | REF exige identidad propia, semántica, endpoints exactos, dirección/tipo/multiplicidad y procedencia | PROPOSED — NOT ACCEPTED |
| IAM-REF-AUD-05 | EDGE/FK/ROUTE_STEP, CLAIM_EVIDENCE_LINK, RUL operands, R_acc/R*, C_dep/E_dst y RULE_DEFINED refs no se elevan por defecto a REF | PROPOSED — NO COLLAPSE |
| IAM-REF-AUD-06 | ABSENT/REF=0 requiere universo/fuentes exhaustivos y COVERAGE COMPLETE en scope exacto | OPEN — NOT ADJUDICATED |
| IAM-REF-AUD-07 | C_DST_DECLARED no demuestra C_DST_APPLIED; A y F requieren evidencia independiente | ALIGNED WITH EXISTING CONTRACT |
| IAM-REF-AUD-08 | Sin snapshots reales no se crean filas observadas ni se sella IAM | OPEN — NO OBSERVATIONS |

El protocolo no produce REF=0 ni PASS de cobertura por sí mismo; no autoriza implementación, fixtures, parser/validator, Design Freeze o ejecución.

## 77 — Control de inspección por clase y etapa

**Estado:** PROPUESTA DOCUMENTAL DE INSPECCIÓN; no aceptada como cierre IAM, no implementada y sin observaciones reales. Deriva de DEC-C10-053/056/059/061/062/065/069/070/071/072/073/074/075/076/077 y de los contratos U_G y de instancia existentes. No altera cardinalidades, vocabularios ni obligatoriedad aprobados.

### Unidad de inspección
Cada observación se ancla a la tupla exacta de identidad de contrato/instancia y versión, snapshot y registro, `stage_key`, ruta o `NONE` justificado, scope y universo/versionado. Se reutilizan NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT, COVERAGE_REGISTER, EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER de U_G. No se crea un inventario paralelo ni se generan registros ficticios.

### Matriz de búsqueda por clase × etapa

| Clase | C_SRC | F1_S2 | A1_S1 | F2_DST_DECL | A2_DST_DECL | F2_DST_APPLIED | A2_DST_APPLIED |
|---|---|---|---|---|---|---|---|
| CMP | Inventario e identidad fuente | CMP afectado y mapping F1 | CMP exportado y preservación | CMP destino declarado | CMP que A2 declara importar/aplicar | CMP producido/materializado por F2 | CMP realmente presente/aplicado |
| PAR | key, owner, tipo, state y value | Conversión, defaults, pérdidas y cambios | Estados/valores exportados | PAR destino declarado y conversión | PAR que A2 declara importar | PAR materializado por F2 | Estado/valor efectivamente aplicado |
| RUL | rule_id, AST, scope, efecto | Reglas transformadas/preservadas/omitidas | Reglas exportadas | Reglas destino y mapping | Reglas que A2 declara importar | Reglas materializadas | Reglas efectivas tras aplicación |
| REF | Inventario, identidad propia, endpoints | Transformación/correspondencia de relación | Referencias exportadas e integridad | REF destino declarada y mapping | REF que A2 declara importar/resolver | REF materializada | Resolución e integridad efectiva de extremos |
| MET | Identidad/versiones contrato, instancia, fuente, snapshot y provenance | Versiones de transformación y artefactos | Identidad de export, formato y lineage | Identidad/versiones destino y mapping | Identidad de import declarado | Artefacto producido, hash y lineage | Registro de aplicación, snapshot y evidencia posterior |

La matriz es un **mapa de inspección**, no una declaración de presencia. F1/A1/F2/A2 no crean automáticamente objetos semánticos. La presencia en cada etapa requiere evidencia específica. `C_DST_DECLARED` no prueba `C_DST_APPLIED`; una diferencia de hash/nombre no prueba equivalencia funcional.

### Evidencia mínima y adjudicación
- **CMP:** identidad semántica y registro exacto, clase/rol, boundary_class cuando proceda, scope y pertenencia al snapshot; mapping explícito para correspondencias entre etapas.
- **PAR:** parameter_key, owner, tipo, estado ABSENT/NULL/DEFAULT/VALUE, valor cuando corresponda, requiredness y dominio/unidad activados; no colapsar estados.
- **RUL:** rule_id, AST tipado, scope explícito (incluido GLOBAL), efecto REQUIRE/FORBID y precedencia/temporalidad solo cuando aplique.
- **REF:** ref_id/registro propio, extremos tipados SOURCE/TARGET, dirección, tipo/rol, multiplicidad si procede, pertenencia al paquete y provenance. No elevar EDGE, FK, ROUTE_STEP, CLAIM_EVIDENCE_LINK, operandos RUL, R_acc/R*, C_dep/E_dst ni refs RULE_DEFINED a REF funcional automáticamente.
- **MET:** identidades/versiones exactas, IAM_id/version/hash, mapping_id/version, oráculo/versión, timestamps y provenance de artefactos/evidencias. El hash es control de artefacto, no prueba semántica.

Estados por predicado y unidad de cobertura:
- `1`: presencia/condición acreditada por evidencia suficiente y coherente.
- `0`: ausencia/incumplimiento solo con búsqueda exhaustiva y cobertura COMPLETE del universo, etapa, ruta/scope y versión pertinentes.
- `?`: evidencia, resolución, mapping o cobertura insuficiente/contradictoria.
- `NA`: no aplicabilidad declarada ex ante en IAM, con fundamento de dominio; nunca por falta de evidencia.
- `NOT_COMPARABLE`: versiones/identidades sin mapping aprobado; no sustituir por 0.
- `NOT_APPLICABLE` solo cuando lo autorice el contrato aplicable, distinto de desconocido.

Para REF=0 se requiere inventario exhaustivo del límite funcional y cobertura exacta. La cardinalidad base permanece CMP≥1, PAR≥1, RUL≥1, REF≥0 y MET obligatorio; no se cambia por esta matriz. La aplicabilidad de una clase/propiedad en una etapa se decide con el contrato y el stage_key, no por extrapolación desde otra etapa.

### Exclusiones y salvaguardas
La inspección de CMP/PAR/RUL/REF se refiere al paquete P0. Entorno destino, runtime, recursos, permisos efectivos, C_dep y estados técnicos P1 se registran en sus objetos/mediciones correspondientes; no se incorporan al paquete ni se convierten automáticamente en REF. Las relaciones estructurales U_G (FK) siguen siendo distintas de REF. REF→EDGE requiere mapping M explícito/versionado; EDGE→REF no se infiere. Split/merge/n-aria exige identidad/grupo y regla de conservación explícitos.

### Estado actual
No se han inspeccionado snapshots reales ni se han asignado valores a ninguna celda. No se declara REF=0, cobertura COMPLETE, IAM sellado, cardinalidades adicionales, implementación, validación, fixtures, simulación o ejecución. La siguiente operación tras aceptación será completar el protocolo de extracción/registro de observaciones usando los snapshots existentes; si no hay snapshots, primero habrá que resolver esa ausencia sin fabricar datos.

## 78 — Gate de disponibilidad y mapeo de clases U_G

**Estado:** HALLAZGO DOCUMENTAL / PROPUESTA DE GATE; sin datos observados ni decisión de implementación.

### Resultado de inspección
La plantilla canónica `C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md` declara expresamente `DRAFT / PLANTILLA VACÍA / NO INVENTARIADA / NO EJECUTADA`. Sus filas ilustrativas son marcadores de esquema, no registros. El registro de snapshots contiene una fila de plantilla con `No capturado`; la matriz de cobertura está en `NONE` para sus dimensiones. Por tanto, en los artefactos revisados no hay snapshots C10-S reales utilizables ni evidencia de cobertura que permita iniciar extracción de observaciones. Esto no demuestra que no existan fuentes externas; significa que no están incorporadas ni referenciadas como observaciones U_G en esta rama.

### Hallazgo de proyección de clases
U_G dispone de diez registros canónicos: NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT, EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER. No hay tablas físicas independientes CMP, PAR, RUL, REF o MET. No se permite asumir equivalencias nominales:
- CMP: candidatos de representación en NODE según `semantic_role` y frontera, pero NODE no equivale automáticamente a CMP.
- PAR: no existe tabla PAR dedicada; la representación/serialización de propiedades debe quedar mapeada explícitamente a campos/artefactos y a su identidad de owner.
- RUL: PREDICATE registra predicados observados/analíticos; no equivale automáticamente a una regla declarativa RUL con AST, scope y efecto.
- REF: DEC-C10-077 distingue el objeto REF de EDGE y de FK estructural U_G. EDGE no es REF; REF→EDGE requiere mapping M explícito y versionado.
- MET: identidad, versión, snapshot y provenance se distribuyen entre campos de objetos, SNAPSHOT y EVIDENCE_REGISTER/CLAIM_EVIDENCE_LINK; MET no es una tabla ni un objeto homogéneo por defecto.

### Protocolo de extracción — cuando existan fuentes
1. Localizar la fuente original y registrar custodio, método, timestamp, versión/hash, alcance y limitaciones en EVIDENCE_REGISTER; no copiar secretos.
2. Verificar que corresponde al contrato/instancia exactos y al snapshot/fase temporal declarados. No emparejar por nombre, hash aislado ni `latest`.
3. Resolver el mapping clase conceptual→representación U_G mediante contrato explícito/versionado. Si no existe o no conserva semántica, adjudicar `UNKNOWN` o `NOT_COMPARABLE`, no forzar una fila.
4. Crear/actualizar registros U_G solo mediante el procedimiento autorizado; fijar snapshot y record IDs exactos, `stage_key`, ruta/scope y universo.
5. Registrar cada afirmación con CLAIM_EVIDENCE_LINK y EVIDENCE_REGISTER; cobertura con COVERAGE_REGISTER; evaluación/adjudicación separadas.
6. Mantener por separado declarado, producido y aplicado. Una fuente C_DST_DECLARED nunca acredita A2_DST_APPLIED.
7. Adjudicar 0 solo con búsqueda exhaustiva y COVERAGE_REGISTER COMPLETE para el universo, versión, etapa y scope exactos; ? ante falta de fuente/mapping/cobertura; NA solo por regla ex ante IAM.

### Gate previo a cualquier extracción
- Identificar fuente(s) real(es) y snapshots existentes; si no existen, definir por separado cómo se obtendrán y autorizar su captura.
- Resolver el crosswalk CMP/PAR/RUL/REF/MET↔U_G sin colapsar REF/EDGE ni RUL/PREDICATE.
- Confirmar identidad/versionado, stage_key, route/scope y snapshot pinning.
- Definir cobertura, evidencia y adjudicación por clase/etapa.
- Solo entonces completar observaciones. La plantilla no se rellena con ejemplos sintéticos ni valores inferidos.

**Conclusión:** no procede todavía extraer ni adjudicar observaciones. El siguiente trabajo documental es cerrar el crosswalk semántico de representación y especificar qué fuentes/snapshots alimentarán cada etapa. No se declara ausencia de objetos, REF=0, IAM sellado, cobertura COMPLETE ni disponibilidad de datos externos. `scientific_execution=false`; `execution_authorized=false`.

## 79 — Control de representación y evidencia PAR

**Estado:** PROPUESTA DOCUMENTAL DE RECONCILIACIÓN; no aceptada como decisión nueva, no implementada, sin instancias ni observaciones reales. Reutiliza DEC-C10-053/054/056/068/069/070/073/074/075/076 y el contrato abstracto de instancia, la matriz de mapping PAR y el overlay U_G existente. No sustituye ni amplía el schema físico U_G.

### 1. Decisión de diseño propuesta
Representar PAR como **propiedad atómica tipada del CMP propietario**, no como NODE independiente y no como EDGE/REF. La identidad semántica de cada parámetro es `parameter_key` dentro del contrato/versión y el ámbito de `owner_component_id`; la instancia observada se distingue por la tupla exacta de contrato/instancia, snapshot/record, stage_key, ruta/scope y versión del CMP owner. Esta opción evita inventar un `semantic_role=PARAMETER` (no existe en el vocabulario aceptado de NODE), evita tratar una propiedad escalar como componente y preserva el ownership ya definido.

La representación es una **fila lógica de manifiesto IAM/inspección**, usando la estructura de referencia ya descrita en U_G §18.3 (manifest_record_id, contract/instance, snapshot exacto, stage_key, route, object_class=PAR, semantic_id/version, owner_component_id, property_key/type/state/value, mapping, declared_or_applied, evidence, claim-evidence, coverage y adjudicación). No se crea una tabla física PAR ni una nueva capa semántica persistida. La fila de manifiesto no recibe por ahora un object_record_id U_G ni una FK nueva: el contrato de identidad de esa fila sigue OPEN.

### 2. Campos semánticos por PAR
Cada entrada lógica debe resolver, sin inferencia:
- `parameter_key` estable y no reutilizable para otro significado;
- `owner_component_id` exacto y su CMP NODE/record/version en el mismo snapshot;
- `type`, dominio/escala/unidad cuando proceda;
- `requiredness` y disparador condicional, si lo hubiera;
- `allowed_states` y estado observado, diferenciando ABSENT, NULL, DEFAULT y VALUE;
- `value` solo si el estado lo permite y procede de la fuente observada;
- `default_contract` (kind, origen, scope, precedencia y versión) solo cuando exista declaración;
- mapping_id/version, estado MAPPED/UNMAPPED/AMBIGUOUS/NOT_APPLICABLE y regla de conversión;
- evidencia, cobertura, adjudicación y procedencia exactas.

No colapsar ausencia, null, default declarado/heredado y valor explícito. `DEFAULT_ENV_RESOLVED` es resolución de E_dst/P1, enlazada al parámetro y snapshot ambiental, no un estado adicional del paquete P0 ni una reescritura de DEFAULT.

### 3. Especialización ya aceptada para el servicio sintético
El roster nuclear se limita a:
- `PAR-SVC-ENABLED`: BOOL, dominio `{false,true}`, REQUIRED.
- `PAR-SVC-PROFILE`: ENUM, dominio `{STANDARD, READ_ONLY, DISABLED}`, REQUIRED.

`PAR-SVC-RETRY-COUNT` queda fuera del núcleo confirmatorio por DEC-C10-068. No debe incorporarse al universo base ni usarse como proxy de capacidad P1. Para ENABLED y PROFILE, ABSENT/NULL no son admisibles; DEFAULT no queda declarado por DEC-C10-068 y solo podría usarse tras declaración contractual explícita, versionada y previa al IAM. No se asignan valores de escenario en este contrato de representación.

### 4. Proyección y enlaces con U_G
- El CMP propietario se resuelve a NODE exacto mediante `component_id/node_id + object_record_id + snapshot_id`; no se resuelve por nombre, rol lógico ni hash.
- La fila lógica PAR referencia ese owner y conserva `parameter_key` como identidad de propiedad. No crea un NODE adicional ni una arista EDGE.
- `COVERAGE_REGISTER` conserva scopes independientes `C10S_CONFIG_PAR` por snapshot×stage_key×ruta/scope, con universo/denominador explícitos. No combinar cobertura PAR con CMP.
- Como CLAIM_EVIDENCE_LINK no admite target_type=PAR, la propuesta es vincular la afirmación a la revisión exacta del NODE owner y/o al COVERAGE_SCOPE correspondiente; `claim_statement` y `relevance_scope` deben identificar inequívocamente `parameter_key`, propiedad, estado y etapa. No se añade un nuevo FK ni se finge que la evidencia apunta a una tabla PAR.
- EVIDENCE_REGISTER conserva fuente, versión, método, integridad y límites; no copiar valores sensibles ni credenciales.
- M mantiene la correspondencia `parameter_key_src → parameter_key_dst`, owner, tipo, dominio, unidad, estado, valor/default y conversión. M es artefacto evaluativo versionado, no EDGE ni una capa semántica adicional.

### 5. Evaluación independiente y etapas
La comparación se realiza por parámetro y etapa, preservando la separación:
- C_SRC: contrato/propiedad fuente observada.
- F1_S2 y A1_S1: representación intermedia producida por cada ruta.
- F2_DST_DECL y A2_DST_DECL: propiedad destino declarada, no aplicada.
- F2_DST_APPLIED y A2_DST_APPLIED: propiedad efectivamente observada tras aplicación.

La evidencia de una etapa no se traslada a otra. El mismo `parameter_key` lógico no prueba por sí solo correspondencia; M debe resolver el owner y la transformación tipada. La equivalencia de valor no compensa una diferencia de tipo, dominio, unidad, estado o default. El analizador no accede a truth oculta ni a etiquetas del oráculo.

### 6. Adjudicación y límites
`1` exige predicado satisfecho con evidencia/cobertura suficiente; `0` exige incumplimiento confirmado o ausencia exhaustiva según el predicado; `?` ante falta de fuente, owner, mapping, snapshot o cobertura; `NA` solo por no aplicabilidad ex ante IAM. `NOT_COMPARABLE` cuando versiones/identidades no tengan mapping aprobado. Una propiedad ausente en el artefacto no equivale a ausencia de observación ni autoriza imputar valor/default.

La propuesta no fija cardinalidades adicionales, no asigna REQUIRED/OPTIONAL nuevos, no cambia DEC-C10-068, no aprueba el roster fuera del núcleo ya aceptado, no añade semantic_role, tabla PAR, FK, EDGE ni REF, no sella IAM, no define serialización ni hash, y no autoriza parser, validator, fixtures, implementación, Design Freeze o ejecución.

### 7. Cuestiones aún abiertas
1. Identidad/versionado de la fila lógica de manifiesto PAR y su relación exacta con el registro IAM sellado.
2. Regla formal para claim_statement/relevance_scope que haga inequívoca la referencia a parameter_key sin crear FK PAR.
3. Mapping concreto de owner y property_key entre representaciones fuente/destino e intermedias.
4. Evidencia disponible por etapa y cobertura real.
5. Defaults y sus reglas por clave, si alguna vez se incorporan; no se presuponen.

## 80 — Control de identidad y supersession de PAR

**Estado:** PROPUESTA DOCUMENTAL DE RECONCILIACIÓN; no aceptada como decisión, no implementada y sin filas/observaciones reales. Resuelve la laguna de identidad detectada en §§19.2/19.19 y §17, sin extender DEC-C10-062 ni modificar el schema U_G.

### 1. Separación de identidades
La fila lógica PAR del manifiesto no es una entidad U_G de las tablas NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT. Por tanto:
- `parameter_key` identifica la propiedad semántica en el ámbito de contrato/versión y owner CMP; no identifica una observación.
- `manifest_record_id` identifica una fila concreta e inmutable del manifiesto; es opaco, no vacío y único dentro del manifiesto/versionado IAM que la contiene. No reutilizar `object_record_id`, `node_id`, `component_id` ni IDs TID/SID/RID/EID.
- La clave lógica de captura PAR queda propuesta como la tupla exacta: contract_id/version + instance_id/version + snapshot_id/snapshot_object_record_id + stage_key + route_id/route_record_id o ausencia justificada + scope/universe revision + owner_component_id y revisión exacta del CMP + parameter_key/semantic_version. Esta clave delimita qué observación se está representando; no sustituye a manifest_record_id.
- `coverage_scope_id` sigue siendo identidad del scope de cobertura, independiente de la fila PAR.

### 2. Revisión y corrección
Se propone que cada fila sea inmutable. Una corrección de captura, adjudicación o metadato de la fila no sobrescribe el registro previo: crea un nuevo `manifest_record_id`, incrementa `manifest_record_revision` en uno para la misma clave lógica y señala el registro inmediatamente anterior mediante `supersedes_manifest_record_id`. La primera revisión es 1 y no tiene predecesor. Solo puede existir una cadena lineal por clave lógica; no se admiten bifurcaciones, ciclos, saltos, referencias cruzadas entre claves o snapshots ni reutilización de IDs. El historial se conserva.

Una nueva observación en otro snapshot, etapa, ruta/scope, versión de owner o versión contractual no es una revisión de la misma fila: constituye una nueva clave lógica y comienza revisión 1. Un cambio semántico de parameter_key o de significado exige nueva identidad de parámetro conforme al contrato, no supersession de captura.

Los campos `manifest_record_revision` y `supersedes_manifest_record_id` son nombres propuestos de contrato lógico, no columnas físicas aprobadas. La propuesta no fuerza un `object_version` ni `supersedes_record_id` U_G.

### 3. Límite de DEC-C10-062
DEC-C10-062 se aplica expresamente solo a NODE, EDGE, ROUTE, PREDICATE y SNAPSHOT; las demás tablas mantienen sus propias claves y contratos. No puede extenderse por analogía a filas de manifiesto. La mención histórica en §19.2 de que manifest_record_id sería versionado “conforme a DEC-C10-062 si se adopta” queda aclarada por esta propuesta: el manifiesto necesita contrato propio y no hereda object_version/supersedes_record_id de U_G. Esta aclaración no altera la decisión aceptada ni la reescribe; precisa el límite de su ámbito.

### 4. Unicidad y control
Para una misma clave lógica y revisión debe existir exactamente un manifest_record_id; un manifest_record_id no puede identificar dos claves/revisiones. Toda referencia a una fila debe resolver por ID exacto dentro de la versión de manifiesto/IAM fijada, nunca por latest, posición, nombre o hash aislado. La verificación documental deberá comprobar:
- no duplicidad de manifest_record_id;
- unicidad de clave lógica + manifest_record_revision;
- revisión inicial 1 sin predecesor;
- sucesión inmediata y misma clave lógica para revisiones posteriores;
- ausencia de ciclos, bifurcaciones, huérfanos y referencias futuras;
- pinning exacto del snapshot y del CMP owner;
- coherencia de coverage_scope_id con la misma tupla de etapa/ruta/clase/universo;
- preservación de múltiples evidencias como vínculos separados, no serializadas en la fila.

No se impone unicidad global entre distintas versiones de manifiesto/IAM; el namespace exacto y su versión forman parte de la resolución.

### 5. Estados de propiedad y ausencia
Una fila PAR representa una propiedad esperada/inspeccionada, no presupone que la propiedad esté presente en el artefacto. `state=ABSENT` puede registrarse solo con evidencia/cobertura según el predicado; no se elimina la fila por ausencia. `NULL`, `DEFAULT` y `VALUE` permanecen distintos. El registro de una revisión no convierte por sí mismo ? en 0 ni acredita COMPLETE.

### 6. Límites
No se crea tabla PAR, no se añaden columnas U_G, no se aprueba DDL/serialización/API/parser/validator/fixtures, no se asignan valores de escenario ni se instancia el manifiesto. La aceptación de esta propuesta, si se produce, será documental y no autorizará implementación ni ejecución. IAM permanece sin sellar; `scientific_execution=false`; `execution_authorized=false`.

### 7. Pendientes para aceptación
- Confirmar namespace de unicidad: por versión de manifiesto/IAM (propuesta) frente a global en toda la línea C10-S.
- Confirmar si la revisión de captura es necesaria o si bastaría append-only con IDs nuevos y relación de supersession.
- Confirmar nombre final de los campos de revisión y predecesor.

## 81 — Criterios propuestos de aceptación de identidad PAR

**Estado:** RECOMENDACIÓN PARA ACEPTACIÓN DEL USUARIO; no es DEC aceptada ni contrato congelado. Se propone resolver conjuntamente las tres cuestiones abiertas de §17.1/§19.20/§20/§16.62/§80/§207/§86.

### Recomendación única
1. **Unicidad de `manifest_record_id`: global en toda la línea C10-S**, independiente de versión IAM/manifest. El ID es opaco, inmutable y nunca se reutiliza. La versión IAM sigue formando parte de la resolución contextual de la fila, pero no limita la unicidad del identificador. Se recomienda unicidad global porque simplifica referencias, auditoría y detección de colisiones entre versiones; no implica que el registro sea una entidad U_G.
2. **Modelo append-only con revisión explícita.** Cada corrección/adjudicación posterior genera nuevo `manifest_record_id`; no se sobrescribe ni elimina la fila anterior. Para una misma clave lógica de observación, `manifest_record_revision` empieza en 1 y aumenta exactamente en uno. Las revisiones posteriores incluyen `supersedes_manifest_record_id` apuntando a la revisión inmediatamente anterior. Una sola cadena lineal por clave lógica; sin bifurcaciones, ciclos, saltos ni huérfanos. La revisión es metadato de secuencia de captura, no versión semántica del parámetro.
3. **Nombres recomendados:** `manifest_record_revision` y `supersedes_manifest_record_id`, exactamente así. `manifest_record_id` se mantiene como identificador del registro, distinto de `parameter_key`, CMP owner, `object_record_id` U_G y `coverage_scope_id`.

### Reglas para evitar revisiones falsas
- Nueva etapa, snapshot, ruta/scope, contrato/instancia o revisión del CMP owner = nueva clave lógica y revisión 1, no supersession.
- Cambio de significado de `parameter_key` = nueva identidad semántica; no se corrige como revisión de captura.
- Corrección de transcripción, evidencia, estado, mapping o adjudicación de la misma captura lógica = nueva revisión, conservando la anterior.
- Varias evidencias para una misma fila son vínculos independientes; no crean revisiones por sí solas.
- Un cambio de versión IAM que solo reempaqueta la misma fila no genera automáticamente una nueva observación. Si la identidad lógica de captura permanece idéntica, la política de migración/referencia deberá conservar el ID; si cambia una dimensión de la clave lógica, comienza una nueva cadena. La migración entre versiones IAM requiere mapping explícito y no se presume.

### Condición de aceptación
La aceptación confirmaría solo este contrato lógico documental de identidad/supersession. No crea columnas, tabla PAR, DDL, serialización, generador de IDs, API, parser, validator, fixtures ni registros reales; tampoco sella IAM, cierra el crosswalk PAR↔U_G, autoriza implementación o cambia `scientific_execution=false` / `execution_authorized=false`.

**Pendiente de aceptación expresa:** unicidad global; append-only + revisión explícita; nombres exactos indicados.

## 82 — Controles normativos de DEC-C10-079

**Estado:** ACEPTADO — DEC-C10-079. Esta sección propaga el contrato lógico aprobado; prevalece sobre cualquier recomendación previa que mantuviera abiertas estas cuestiones.

- `manifest_record_id`: globalmente único en toda la línea C10-S, opaco, inmutable y nunca reutilizado, independiente de la versión IAM.
- Append-only: ninguna fila se sobrescribe ni elimina. Toda corrección de la misma captura lógica crea un nuevo ID y conserva el anterior.
- `manifest_record_revision`: revisión secuencial por clave lógica, desde 1, sin saltos.
- `supersedes_manifest_record_id`: en revisiones posteriores, referencia a la revisión inmediatamente anterior de la misma clave lógica. Cadena lineal única, sin bifurcaciones, ciclos, huérfanos ni referencias cruzadas.
- Cambio de snapshot, etapa, ruta/scope, contrato/instancia o revisión del CMP owner inicia una nueva clave lógica y revisión 1. Cambio semántico de `parameter_key` exige nueva identidad semántica.
- Múltiples evidencias no crean revisiones por sí solas. Reempaquetar en nueva versión IAM no crea automáticamente nueva observación; migración exige mapping explícito.

**Límites:** decisión documental lógica. No crea tabla/columnas PAR o U_G, DDL, serialización, generador, API, parser, validator, fixtures ni registros reales; no sella IAM, no cierra PAR↔U_G, no autoriza Design Freeze, implementación o ejecución. `scientific_execution=false`; `execution_authorized=false`.

## 83 — Controles de trazabilidad probatoria PAR

**Estado:** PROPUESTA DOCUMENTAL; no aceptada como nueva DEC, no implementada, sin registros observados. Reutiliza DEC-C10-079 y el esquema U_G §12.2–12.3/§18.3–18.8. No amplía los dominios ni las FK de U_G.

### 1. Principio
CLAIM_EVIDENCE_LINK no tiene target_type PAR ni FK a manifest_record_id. No se simula una FK inexistente. La trazabilidad se compone de:
(a) FK real a COVERAGE_SCOPE (y, cuando la afirmación se refiere al owner CMP como objeto por derecho propio, un vínculo separado al NODE owner);
(b) localizador lógico exacto de la fila PAR en claim_statement/relevance_scope;
(c) control independiente que resuelve ese localizador contra el manifiesto IAM versionado y verifica su integridad.

### 2. Perfil normativo propuesto para una afirmación sobre una fila PAR
Una fila CLAIM_EVIDENCE_LINK por cada evidencia × afirmación × fila PAR:
- `claim_target_type=COVERAGE_SCOPE`;
- `target_coverage_scope_id` = scope PAR exacto, cuyo `dimension=C10S_CONFIG_PAR` y cuyo universe_definition/version fija contrato/instancia, snapshot+record, stage_key, route/scope, clase PAR y universo;
- todos los campos target_* no aplicables quedan vacíos; no se rellenan FK de NODE como sustituto de PAR;
- `claim_statement` identifica explícitamente el predicado y la fila: `PAR_ROW|manifest_record_id=<ID>|manifest_record_revision=<N>|parameter_key=<KEY>|owner_component_id=<CMP_ID>|predicate=<PREDICATE>`;
- `relevance_scope` identifica el contexto completo: `contract_id/version;instance_id/version;snapshot_id/snapshot_object_record_id;stage_key;route_id/route_record_id-or-justified-NONE;coverage_scope_id;owner_component_id/owner-record/version;parameter_key;manifest_record_id;manifest_record_revision`.
Los literales anteriores describen un perfil documental de campos textuales existentes, no una gramática física ni un parser aprobado. No se deben usar separadores/valores ambiguos; si algún identificador contiene delimitadores, la serialización futura tendrá que definir escaping/versionado antes de automatizar.

### 3. Resolución y controles independientes
El control debe resolver manifest_record_id globalmente (DEC-C10-079), verificar revision y supersession, y comprobar igualdad exacta entre la fila del manifiesto, su clave lógica, owner CMP, snapshot, stage_key, route/scope y coverage_scope_id. También verifica:
- dimension C10S_CONFIG_PAR y universe_definition/version compatibles;
- que el scope corresponde a la misma tupla y no está compartido entre snapshots/etapas/rutas/clases;
- que el CMP owner resuelve al NODE/object_record_id/snapshot exactos;
- que parameter_key y manifest_record_revision coinciden con el manifiesto;
- que la evidencia está en EVIDENCE_REGISTER y que la relación 1:N se conserva sin listas serializadas;
- que la evidencia realmente respalda el predicado y estado citados; un enlace FK correcto no prueba el contenido.
Un fallo de resolución, contradicción o colisión es FAIL; falta de manifiesto, snapshot, scope o fuente es UNKNOWN/?; incompatibilidad de versiones sin mapping es NOT_COMPARABLE; NA solo por inaplicabilidad ex ante. No inferir 0 desde falta de vínculo.

### 4. Owner CMP y cobertura
Si una misma evidencia respalda también una afirmación distinta sobre identidad/estado del CMP owner, se crea otro CLAIM_EVIDENCE_LINK con target NODE y su FK exacta. No se duplica ni se mezcla esa afirmación con la afirmación PAR. La afirmación PAR conserva COVERAGE_SCOPE como target FK y el localizador PAR en campos textuales.
COVERAGE_REGISTER permanece por clase PAR y por snapshot×stage_key×ruta/scope; COMPLETE exige denominador, fuentes, enumeración y excepciones conforme a §18.6. El link a un scope no convierte automáticamente el scope en COMPLETE.

### 5. Límites y decisiones abiertas
No se añade target_type PAR, FK, tabla PAR, columna U_G, tabla puente ni relación física nueva. No se crea CLAIM_EVIDENCE_LINK directo a manifest_record_id; su resolución es un control independiente contra el manifiesto. No se define todavía escaping/canonicalización del localizador, vocabulario de predicate ni automatización. No se sella IAM, no se declara cobertura, no se crean registros y no se autoriza parser, validator, fixtures, implementación o ejecución.
Pendiente de aceptación: perfil COVERAGE_SCOPE + localizador en claim_statement/relevance_scope; vínculo NODE separado solo para afirmaciones propias del CMP; control independiente de resolución.

## 84 — Controles aceptados de binding PAR (DEC-C10-080)

**Estado:** ACEPTADO — DEC-C10-080. Sustituye el estado pendiente de aceptación de §17.4/§19.23/§23/§16.65/§83/§210/§89.

- Afirmación sobre fila PAR: CLAIM_EVIDENCE_LINK usa `claim_target_type=COVERAGE_SCOPE` y FK `target_coverage_scope_id` al scope exacto `dimension=C10S_CONFIG_PAR`.
- `claim_statement` y `relevance_scope` contienen localizador lógico suficiente para resolver `manifest_record_id`, `manifest_record_revision`, `parameter_key`, owner CMP, snapshot/record, `stage_key`, ruta/scope y universo/version.
- Una fila CLAIM_EVIDENCE_LINK por evidencia×afirmación×fila PAR. Las evidencias múltiples se conservan como filas separadas, nunca como listas embebidas.
- Control independiente resuelve ID global y verifica revisión/supersession y coincidencia exacta de clave lógica, owner, snapshot, etapa, ruta/scope, coverage scope, universo, predicado y evidencia.
- Una afirmación separada sobre el CMP owner usa otro CLAIM_EVIDENCE_LINK con target NODE y FK exacta. No sustituye el target COVERAGE_SCOPE de la afirmación PAR.
- El enlace al scope no implica COVERAGE COMPLETE; se aplican U_G §12.3/§18.6.

**Restricciones:** no se añade target_type PAR, FK, tabla o puente. No se aprueban gramática, escaping, canonicalización, serialización, parser ni automatización. Los campos singulares `evidence_id`/`claim_evidence_id` del manifiesto no sustituyen el registro 1:N de CLAIM_EVIDENCE_LINK. No se crean observaciones, no se sella IAM, no se declara cobertura ni se autoriza implementación/ejecución. `scientific_execution=false`; `execution_authorized=false`.

## 85 — Control independiente PAR propuesto

**Estado:** PROPUESTA DOCUMENTAL; pendiente de aceptación. Desarrolla DEC-C10-080 reutilizando el C0 ya especificado en el protocolo de evidencia §19; no crea un segundo control genérico.

Se separan cinco capas: C0_SCOPE; PAR_ROW_BINDING; EVIDENCE_LINK_INTEGRITY; EVIDENCE_RELEVANCE; COVERAGE_COMPLETENESS. Se define una secuencia P0–P11 para aplicabilidad, target, resolución C0, dimensión/universo, identidad PAR global, clave lógica/pinning, supersession DEC-C10-079, evidencia, correspondencia de afirmación, pertinencia sustantiva, vínculo NODE separado solo si hay afirmación propia del owner y cobertura.

El control conserva resultados PASS/FAIL/UNKNOWN/NOT_COMPARABLE/NA por capa, sin colapsarlos. Un registro histórico superseded conserva validez histórica, pero no acredita estado actual sin justificación temporal. Una FK correcta no prueba pertinencia; un scope COMPLETE tampoco se infiere del vínculo.

Se añaden 18 casos adversariales documentales y requisitos de informe. Se reconocen expresamente las limitaciones ya detectadas en §20.1–20.5: mappings stage_key, clase y ruta aún abiertos producen UNKNOWN donde impiden resolución inequívoca.

No se amplía U_G ni se cierra gramática/escaping/canonicalización/predicate. No crea fixtures, parser, validator ni registros. No autoriza implementación, Design Freeze, validación técnica ni ejecución. `scientific_execution=false`; `execution_authorized=false`.

 
## 86 — Control independiente PAR aceptado (DEC-C10-081)

**Estado:** ACEPTADO — contrato lógico documental.

El protocolo §20.18 del protocolo de evidencia queda aceptado como control del binding PAR. Reutiliza C0 y exige cinco capas independientes: C0_SCOPE, PAR_ROW_BINDING, EVIDENCE_LINK_INTEGRITY, EVIDENCE_RELEVANCE y COVERAGE_COMPLETENESS. Aplica entradas mínimas y secuencia P0–P11, reglas DEC-C10-079 de identidad/supersession, resultados por capa PASS/FAIL/UNKNOWN/NOT_COMPARABLE/NA y 18 casos adversariales documentales.

No se colapsan capas ni se infiere pertinencia o COMPLETE desde una FK. Los mappings abiertos o la resolución ambigua producen UNKNOWN. No autoriza implementación, validator, fixtures, Design Freeze ni ejecución; `scientific_execution=false`; `execution_authorized=false`.


## 87 — Reconciliación temporal F/A y estado de cierre hasta DEC-C10-088

**Corte:** 2026-11-08. **Naturaleza:** reconciliación documental; no constituye nueva DEC ni cierre de evidencia.

DEC-C10-082…088 quedan incorporadas al registro de decisiones aceptadas de esta matriz. En particular, DEC-C10-088 integra sin compensación los tres tramos F/A: C_SRC→F1/A1 (085), destino declarado y transición (086), y aplicación efectiva/verificación (087). La matriz temporal, la matriz abstracta §15.9 y el crosswalk §10.19 contienen la integración aceptada. La aceptación de contratos no equivale a adjudicación de observaciones ni a cobertura completa.

### Clasificación consolidada de requisitos

| Estado | Requisitos / controles | Condición para avanzar |
|---|---|---|
| Cerrado documentalmente | Contratos lógicos DEC-C10-068…088 en el alcance expresamente aceptado; identidad/supersession PAR; binding probatorio; control lógico PAR; anclaje CMP↔NODE; aplicabilidad y equivalencia PAR; adjudicación temporal F/A | Mantener trazabilidad y no reabrir sin contradicción o nueva evidencia/decisión |
| Definido, pendiente de especificación | Mappings concretos/versionados CMP↔NODE, PAR↔U_G, REF↔EDGE y stage_key/clase/ruta; roster y cardinalidades IAM; gramática, escaping y canonicalización del localizador PAR; mapping M; oráculo/tolerancias; especificación de observación y de registros; contrato técnico del control independiente | Especificar identidades, dominios, cardinalidades, reglas y mappings sin inferencia nominal; someter cualquier decisión nueva a aceptación |
| Pendiente de evidencia | Cobertura C0/COVERAGE_REGISTER por snapshot×etapa×ruta×clase; resolución real de filas PAR y evidencia 1:N; invariantes y auditoría de vías colaterales D2 (incluida IV-G4); evidencia de exclusión de rutas alternativas/interferencia; evidencia de primeras etapas y mediciones independientes | Obtener evidencia autoritativa y exhaustiva; conservar UNKNOWN cuando falte cobertura o resolución |
| Bloqueante de implementación | Mappings y roster IAM no cerrados; contrato técnico/serialización del manifiesto y localizador; contrato de control independiente y fixtures de prueba aún no autorizados; operacionalización de oráculo, medidas y fuentes | No implementar el experimento D2 hasta que el conjunto mínimo necesario esté especificado y aprobado |
| Bloqueante de ejecución | Ausencia de autorización explícita; no hay Design Freeze; no se ha demostrado preflight de integridad, identidad de artefactos, entorno, configuración ni autorización de ejecución | Requiere autorización y workflow técnico completo; scientific_execution=false; execution_authorized=false |

### Dependencias y lectura causal

1. El cierre documental DEC-C10-088 elimina ambigüedad sobre la secuencia de adjudicación F/A, pero no sella IAM ni demuestra que existan observaciones o evidencia para cada celda.
2. La resolución IAM/U_G y la cobertura son prerrequisitos para adjudicar las observaciones de configuración y lineage sin falsos PASS/FAIL.
3. La exclusión de vías colaterales y la identificación de estimandos D2 son prerrequisitos científicos independientes del cierre de configuración F/A.
4. Ningún PASS de configuración, aplicación o procedencia implica por sí solo ACC, Reach, ΔT_acc ni un efecto causal sobre Value.
5. No se infiere FAIL ni ausencia desde un registro inexistente; UNKNOWN/? se mantiene cuando la cobertura no es exhaustiva.

Esta sección reconcilia el estado documental conocido; no declara cerrado ningún control de evidencia no observado, no modifica el estado de aprobación del documento y no autoriza implementación, Design Freeze, validación técnica ni ejecución.


## 88 — Estado de especificación del roster CMP y mapping IAM↔U_G

**Corte:** 2026-11-08. **Estado:** PROPUESTA DOCUMENTAL registrada en crosswalk §10.20; pendiente de aceptación.

La identidad del CMP de referencia está documentalmente fijada por DEC-C10-069: CMP-SERVICE-LOGIC-001, clase SERVICE_LOGIC, bajo contrato e instancia versionados. La etiqueta CMP-SERVICE-LOGIC es solo owner/rol lógico. DEC-C10-082 ya acepta el anclaje 1:1 CMP↔NODE por snapshot exacto.

No obstante, el roster total CMP no está demostrado exhaustivo y no se puede inferir CMP=1 de que solo haya un ID concreto identificado. La proyección propuesta reutiliza NODE, SNAPSHOT, EDGE, MET/provenance y los registros U_G de cobertura/evidencia/adjudicación; no autoriza columnas nuevas. La cardinalidad, resolución, evidencia y cobertura deben adjudicarse según DEC-C10-082, manteniendo UNKNOWN cuando la enumeración no sea exhaustiva.

**Clasificación:** contrato de anclaje 1:1 = cerrado documentalmente (DEC-C10-082); identidad CMP de referencia = cerrada documentalmente (DEC-C10-069); proyección field-to-column detallada y roster exhaustivo = definidos parcialmente / pendientes de aceptación y evidencia; mappings P1 y demás CMP = OPEN. No hay IAM sellado ni inventario observado.

No se autoriza implementar el mapping, poblar registros, ejecutar controles, Design Freeze ni ejecución científica. scientific_execution=false; execution_authorized=false.


## 89 — Reconciliación U_G N01–N23 con membership IAM y frontera

**Estado:** propuesta de clasificación registrada en crosswalk §10.21; pendiente de aceptación.

La reconciliación fija una distinción necesaria: NODE es una clase de registro del grafo U_G; CMP es una clase de objeto del dominio IAM. Por ello, el catálogo de 23 roles no equivale a 23 CMP ni permite declarar exhaustivo el roster. Cada CMP aplicable tendrá un único NODE anchor por snapshot (DEC-C10-082), pero NODE no implica CMP.

El crosswalk §10.21 clasifica los 23 roles en: no CMP por función; CMP candidato; y condicional a identidad contractual, granularidad y frontera. No asigna component_id ni afirma existencia técnica. Reutiliza P0_CONFIG/P1_ENVIRONMENT/DUAL_P0_P1/NA conforme DEC-C10-059 y mantiene P2 como perímetro transversal.

**Estado de cierre:** identidad CMP de referencia y regla 1:1 NODE anchor cerradas documentalmente; clasificación semántica de roles U_G propuesta; roster CMP exhaustivo, membership por objeto, mappings adicionales y cobertura permanecen OPEN/UNKNOWN hasta evidencia y aceptación. No hay inventario técnico ni IAM sellado.

No autoriza inspección, captura de snapshots, población IAM, implementación, Design Freeze ni ejecución científica. scientific_execution=false; execution_authorized=false.

## 90 — Desambiguación de N01: unidad lógica, host y S0

**Estado:** propuesta documental registrada en crosswalk §10.22; pendiente de aceptación.

N01 mezclaba la unidad lógica de servicio, el sistema anfitrión y el estado basal S0. La propuesta los separa: (i) NODE raíz LOGICAL_SERVICE_UNIT para identidad estable de la unidad migrada; (ii) host/entorno/runtime como contexto P1 y NODE independientes solo si satisfacen el criterio de granularidad; (iii) S0 como SNAPSHOT basal con pinning exacto, no como CMP ni como host.

La unidad raíz puede usar boundary_class=NA cuando solo actúa como contenedor de identidad, conforme DEC-C10-059. SNAPSHOT mantiene la FK compuesta a la revisión exacta del NODE raíz según DEC-C10-064/065. No se presupone que CMP-SERVICE-LOGIC-001 sea idéntico al NODE raíz: cualquier equivalencia requerirá mapping explícito y evidencia.

**Clasificación:** definición conceptual y regla de raíz aceptadas documentalmente; aplicación de N01 propuesta; identidades/instancias, host, snapshots y cobertura reales no observados. Estado de inventario: NONE donde no existe inspección; no inferir ausencia.

No autoriza acceso técnico, captura, población IAM, implementación, Design Freeze ni ejecución científica.
## 91 — DEC-C10-089: aceptación de N01 y relación CMP↔unidad raíz

**Estado:** ACCEPTED — DOCUMENTAL (2026-11-08).

Se acepta la unidad lógica de servicio como NODE raíz `LOGICAL_SERVICE_UNIT`, distinta conceptualmente del host/entorno y del estado basal S0 (SNAPSHOT). La relación entre NODE raíz y CMP-SERVICE-LOGIC-001 queda OPEN hasta mapping explícito, versionado y sustentado; no se infiere ni identidad ni separación.

**Cierre:** ambigüedad conceptual N01 = cerrada documentalmente. Mapping CMP↔raíz, identidad/registro raíz, host/entorno, snapshots y evidencia = OPEN/UNKNOWN. DEC-C10-082 permanece sin cambios.

No hay registros ni cobertura observados; no se sella IAM ni se autoriza captura, implementación, Design Freeze o ejecución científica. scientific_execution=false; execution_authorized=false.
## 92 — Reconciliación histórica del anchor CMP frente al NODE raíz

**Estado:** reconciliación documental conforme DEC-C10-089.

Se revisan §§10.6–10.7 del crosswalk: la regla aceptada DEC-C10-082 define un NODE anchor único por CMP y snapshot, pero no adjudica que ese anchor sea necesariamente el NODE raíz LOGICAL_SERVICE_UNIT. DEC-C10-089 deja abierta la identidad o separación entre ambos.

**Regla reconciliada:** NODE raíz identifica la unidad lógica; NODE anchor identifica al CMP contractual. Pueden coincidir solo con mapping explícito y evidencia. Si no coinciden, se mantienen separados. La cardinalidad 1:1 CMP↔NODE anchor se conserva sin cambios.

La ambigüedad textual queda reconciliada documentalmente; mapping, registros y evidencia siguen OPEN/UNKNOWN. No se sella IAM ni se autoriza captura, implementación o ejecución.
## 93 — Propuesta de clasificación de N07: endpoint/interfaz/servicio

**Estado:** PROPUESTA DOCUMENTAL pendiente de aceptación (crosswalk §10.25).

N07 se descompone en: endpoint técnico concreto; contrato/interfaz versionado; y servicio proveedor. El endpoint no es CMP por ser direccionable. La interfaz solo es REF si tiene identidad propia y extremos tipados conforme DEC-C10-077; de otro modo permanece atributo/artefacto contractual. El servicio solo es CMP si posee identidad contractual, lifecycle y frontera autónomos. Un servicio externo no entra en el roster CMP interno por el mero consumo.

No hay objetos técnicos observados ni IDs adjudicados. La clasificación por instancia, mappings, rutas, cobertura y evidencia permanecen OPEN/UNKNOWN. No autoriza inspección, llamadas de red, implementación, Design Freeze ni ejecución.
## 94 — DEC-C10-090: aceptación de la descomposición conceptual N07

**Estado:** ACCEPTED — DOCUMENTAL (2026-11-08).

Se acepta N07 como tres conceptos separables: endpoint técnico; contrato/interfaz; servicio proveedor. Endpoint no implica CMP/REF; interfaz solo es REF con identidad propia y extremos tipados; servicio solo es CMP con identidad contractual, lifecycle y frontera autónomos. Servicio externo no se incorpora al roster interno por consumo. EDGE y REF no se infieren entre sí.

**Cierre:** ambigüedad conceptual N07 = cerrada documentalmente. Instancias, identidades, topología, mappings, rutas, snapshots, cobertura y evidencia = OPEN/UNKNOWN. No hay IDs ni registros creados; IAM no sellado. No autoriza inspección, llamadas de red, implementación, Design Freeze ni ejecución científica.
## 95 — Propuesta N14: contrato/formato, payload y transferencia

**Estado:** PROPUESTA DOCUMENTAL pendiente de aceptación (crosswalk §10.27). Reutiliza N14, E12/E13 y B-M14 ya existentes.

El gate separa definición versionada del formato/contrato, payload concreto producido por A1 y consumido por A2, y eventos de transferencia/recepción/aplicación. Formato no es REF automáticamente; payload no es NODE automáticamente; evento no es CMP. N07 mantiene el canal/endpoint y M el mapping fuente→payload→destino. E12/E13 son relaciones candidatas, no observadas.

Quedan OPEN formato, codificación, payload, identidad/revisión, mapping, cardinalidades reales, lineage, etapas de transferencia, compatibilidad sintáctica/semántica, aplicación, F*, evidencia y cobertura. DEC-C10-074 JCS se limita a UDG-01, no al payload. Hash no prueba equivalencia semántica ni aplicación.

No se crean IDs/filas ni se autoriza captura, parser, validator, implementación, Design Freeze o ejecución científica.
## 96 — DEC-C10-091: aceptación de la descomposición semántica N14

**Estado:** ACCEPTED — DOCUMENTAL (2026-11-08).

Se acepta separar N14 en formato/contrato versionado, payload concreto y eventos de transferencia/recepción/parseo/validación/aplicación. Formato y payload conservan identidad/versionado separados; formato no implica REF; payload no implica NODE; N13/A1 produce, N15/A2 consume, N07 conserva canal/endpoint y M el mapping. E12/E13 siguen candidatas.

Hash de bytes no demuestra equivalencia semántica ni aplicación. JCS de DEC-C10-074 se limita al envelope UDG-01. La alternativa A1→N14→A2 exige demostración bajo el mismo F*, frontera, G y H.

**Cierre:** descomposición conceptual N14 = cerrada documentalmente. Formato, payload, identidades, mapping, lineage, eventos, compatibilidad, aplicación, evidencia y cobertura reales = OPEN/UNKNOWN. Sin IDs ni registros creados; IAM no sellado; sin autorización de captura, implementación, Design Freeze o ejecución.
## 97 — Propuesta N15: importador A2 y separación de procesamiento/aplicación

**Estado:** PROPUESTA DOCUMENTAL pendiente de aceptación (crosswalk §10.29). Reutiliza el N15 del inventario U_G y los contratos ya aceptados DEC-C10-071/086/087/088/090/091.

N15 no se presume CMP autónomo: separar capacidad/contrato A2, implementación concreta y ejecución temporal; CMP independiente solo si tiene identidad contractual, lifecycle y frontera autónomos. Distinguir entrada declarada A2_DST_DECL, recepción efectiva, parseo, validación estructural/semántica, resolución M, aplicación FP-06, post-check FP-07 y provenance FP-08.

Recepción ≠ parseo; parseo ≠ validación; validación ≠ mapping resuelto; mapping ≠ aplicación; aplicación ≠ post-check PASS. Los hitos internos no crean nuevos stage_key ni predicados confirmatorios. Se reutilizan los siete stage_key y FP-01…08; F/A independientes, sin herencia de evidencia.

Faltan implementación/protocolo A2, formato y parser reales, reglas de validación, mapping físico, destino, eventos, snapshots, cobertura y evidencia. No hay CMP N15 adjudicado, registros ni observaciones. IAM no sellado; no autoriza captura, pruebas, implementación, Design Freeze o ejecución.

## 98 — DEC-C10-092: aceptación conceptual N15, importador A2

**Estado:** ACCEPTED — DOCUMENTAL (2026-11-08). Se acepta la descomposición conceptual ya propuesta en §10.29 del crosswalk IAM↔U_G. N15 se analiza en tres planos: capacidad/contrato A2, implementación concreta y ejecución temporal. La cadena distingue A2_DST_DECL, recepción efectiva, parseo, validación estructural/semántica, resolución M, aplicación FP-06, post-check FP-07 y provenance FP-08.

Se reutilizan DEC-C10-071/086/087/088 y los siete stage_key; no se crean hitos confirmatorios nuevos. F/A se adjudican independientemente y no heredan evidencia. N15 solo será CMP si se demuestra identidad contractual, lifecycle y frontera autónomos. Recepción, parseo, validación, mapping, aplicación y post-check son estados distintos; ausencia de registro no demuestra ausencia de evento.

**Cerrado documentalmente:** descomposición conceptual N15. **Definido pero pendiente de especificación:** protocolo A2, formato/parser, reglas de validación, estrategia de errores/transacciones, mapping físico y destino. **Pendiente de evidencia:** eventos, snapshots, cobertura y estado realmente aplicado. **Bloqueante de implementación:** contrato técnico y mappings no cerrados. **Bloqueante de ejecución:** sin autorización ni Design Freeze. No se crean registros/IDs/columnas, no se sella IAM y no se autoriza captura, pruebas, implementación ni ejecución.


## 99 — Gate obligatorio de precedencia semántica y prevención de regresiones

**Fuente rectora:** maestro C10-S §§0.5 y 213; crosswalk D2 de predicados §0; DEC-C10-066/067.  
**Estado:** control documental incorporado; no es una nueva DEC científica, no congela la arquitectura y no autoriza ejecución.

### Riesgo que controla

La recuperación de secciones históricas o propuestas no aceptadas puede reintroducir formulaciones ya corregidas como si fueran vigentes. La existencia de una etiqueta «histórico/obsoleto» o una regla genérica de reconstrucción no basta si el análisis no resuelve la precedencia del asunto concreto.

### Control obligatorio antes de cada análisis o propuesta C10-S

1. Identificar el asunto exacto y evitar colapsar objetos semánticamente distintos.
2. Consultar primero las DEC aceptadas aplicables; después los addenda que declaran supersesión y su alcance; luego el maestro/crosswalk vigente; finalmente, tratar las formulaciones anteriores como antecedentes.
3. No inferir precedencia por cronología, numeración, longitud, detalle ni orden de resultados de búsqueda.
4. Registrar qué formulación rige, cuál queda sustituida, qué alcance tiene la sustitución y qué sigue abierto.
5. Ante contradicción no resuelta o fuente no verificable: detener la inferencia y clasificar UNKNOWN/OPEN. No completar desde memoria conversacional.

### Caso de control obligatorio: autorización y accesibilidad

- D2: `C_auth,base=1` común, pre-Z e invariante frente a B (DEC-C10-067).
- Predicado: `C_auth_base` se corresponde con `AUTH_f*`; no son factores independientes duplicados.
- Fórmula candidata: maestro §67.3 y crosswalk D2; la composición histórica de §30.1 no la sustituye.
- AUD-001/002: intervención focal sobre autorización no primaria en D2; solo alternativa/adversarial separada. No retirar ni obsoletar autorización basal ni `AUTH_f*`.
- D2 primario candidato / D1 secundario por DEC-C10-066; esto no resuelve por sí solo atribución causal a accesibilidad.

### Criterio de cierre de este control

El gate se considera aplicado en un análisis solo si el razonamiento cita las fuentes de precedencia relevantes y mantiene las distinciones anteriores. No se permite avanzar a la siguiente inferencia causal cuando se haya detectado una contradicción no resuelta. La verificación documental de este gate no equivale a una validación automatizada ni garantiza por sí sola que no aparezcan nuevos conflictos; cualquier conflicto nuevo debe incorporarse a la trazabilidad existente, sin crear una matriz paralela.

**Límites:** no cambia el estado científico de C10-S, no resuelve estimandos/identificación, no acepta la fórmula candidata, no modifica C10-D1/Core/RMA/Evidence→Claim Matrix/STATUS, no autoriza implementación, Design Freeze, simulación o ejecución. `scientific_execution=false`; `execution_authorized=false`.

## 100. Gate de conformidad semántica para generación y modificación de código C10-S

**Fuente rectora:** maestro C10-S §§0.5–0.6, 214–215; contrato de estimandos actualizado §§12, 17–19; DEC-C10-066/067; auditorías §§131–132.  
**Estado:** gate documental obligatorio; implementación y ejecución científica no autorizadas.

### Riesgo que controla

La generación de código puede recuperar nombres, fórmulas, decisiones o estructuras de secciones antiguas, aunque existan addenda posteriores. Compilar o superar pruebas técnicas no demuestra conformidad con la semántica científica vigente.

### Checklist previo a generar o modificar código

1. Recuperar el paquete vigente desde GitHub con rama y commit exactos: DEC aplicables, maestro, crosswalks, contrato de estimandos, estado de gates y código existente.
2. Resolver precedencia semántica por asunto según maestro §0.5. No tomar como autoridad fragmentos de conversaciones, snippets, ejemplos ni secciones históricas.
3. No generar código ejecutable que materialice DGP, estimandos, políticas, oráculo, Analyzer o Evaluator mientras no exista contrato de implementación aceptado y autorización explícita.
4. Trazar cada módulo/función/variable/fixture/aserción a requisito, fuente, versión y hash; los requisitos OPEN/UNKNOWN bloquean la implementación salvo parametrización expresamente autorizada.
5. Proteger distinciones críticas: D2 primario candidato/D1 secundario; ITT_Z^D2 ≠ efecto puro de accesibilidad; B_g^D2 ≠ g^Af; C_dep* ≠ A_f*/D_f*/ΔT_acc*; C_auth,base=1 y AUTH_f* vigentes; intervención focal antigua sobre autorización no primaria D2.
6. Mantener Generator/Analyzer/Evaluator separados y truth/potentials ocultos al Analyzer; el Evaluator compara solo después de congelar outputs.
7. Aplicar revisión semántica, pruebas negativas/adversariales y búsqueda de residuos históricos; lint/compilación/tests técnicos son controles distintos.
8. Registrar versiones, fuentes, requisitos, desviaciones y controles aplicados. Si hay contradicción o fuente no verificable, detener el trabajo.

### Criterio de cierre

PASS solo cuando el código y sus pruebas se vinculan a fuentes vigentes, no materializan formulaciones supersedidas y respetan el contrato de roles/datos. UNKNOWN/OPEN ante trazabilidad incompleta; FAIL ante contradicción semántica demostrada. Este gate no es una validación automatizada ya implementada, no crea una matriz paralela, no aprueba Design Freeze ni autoriza ejecución.

### Auditoría transversal de fuentes dependientes — 2026-11-09

**Referencia rectora:** maestro C10-S §215. **Alcance comprobado:** 100/100 archivos modificados por PR #116, recuperados y revisados documentalmente, más inspección de las secciones causales de referencia §§17/24–30 del protocolo C10-D1. No equivale a auditoría de todo el repositorio ni a revisión independiente.

**Controles de no-regresión que deben mantenerse:**
1. DEC-C10-066/067: D2 primario candidato / D1 secundario; políticas D2 de provisión técnica focal.
2. `C_auth,base=1` basal común e invariante; `C_auth_base`→`AUTH_f*`; intervención focal AUD-001/002 no primaria D2.
3. Fórmula candidata de `A_f*` según maestro §67.3/crosswalk D2; no reintroducir `C_info` autónomo ni `C_other`; no duplicar `C_auth_base` y `AUTH_f*`.
4. `ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*)` y `ΔE_T` epistémico separado.
5. `θ_A(q)`, `ITT_Z^D2`, `LATE_f^D2` y `θ_Af(q_X*)` permanecen diferenciados; ITT no equivale automáticamente a efecto puro de accesibilidad.

**Correcciones persistidas en esta auditoría:** auditoría integrada; reconciliación de arquitectura causal; auditoría de medición focal; reconciliación de población/comparadores; avisos en AUD-001/002 y auditoría integrada de consistencia; plan Draft 004; Test Contract Register; retirada de la ecuación intermedia de maestro §59.3 como representación operativa; corrección del crosswalk D2 y de los mappings de las fichas D2-RES/CAP/C_INFO/MEAS-G1 en plan Draft004; aviso de precedencia en la propuesta snapshot/delta; alineación de `C10_S_PATH_PREDICATE_TEMPORAL_EVIDENCE_MATRIX_DRAFT_001.md §13.4` con §67.3. Ver maestro §§215.2 y 215.5 para detalle, incluidas las correcciones de §§16.2/16.4, 30.1, 53.5, 58.4/58.6, 59.3, 63.7, 68.7/69.5 y el estado parcial de XSYNC-138-01 y su propagación al XSYNC Closure Tracker.

**Evidencia y límites:** `PASS_STATIC` en la revisión documental del conjunto PR #116; `CONDITIONAL` para referencias del resto del repositorio y para la futura generación de código. No se han ejecutado validadores, fixtures, parsers, generadores, simulaciones o experimentos. Sin revisión humana independiente. No se autoriza implementación, Design Freeze ni ejecución.


---
## 101. Reconciliación de precedencia de §33 y estado actual MEAS-G1 (2026-11-09)

**Aclaración de lectura obligatoria:** la fila de §33 que registraba «Composición de predicados — OPEN / MATERIAL» corresponde al corte anterior a la reconciliación del crosswalk D2. No debe leerse como estado operativo vigente ni como contradicción no resuelta sobre la existencia de una fórmula candidata.

El estado documental vigente es el siguiente:
- La fórmula candidata de referencia está identificada en el maestro §67.3 y reconciliada conceptualmente en C10_S_D2_AF_PREDICATE_CAUSAL_CROSSWALK_DRAFT_001.md.
- C_auth,base=1 permanece común, basal e invariante en D2; C_auth_base corresponde a AUTH_f*; no se duplican.
- C_info no es un factor autónomo; C_other queda excluido; recursos/capacidad solo pueden contribuir a RES_f* si son disponibilidad ex ante necesaria y no duplicada; D_support requiere mapping semántico a ID/tipo o COND.
- MEAS-G1 es **PARTIAL**: mappings, operacionalización material de RES_f*, REL_f*, COND_f*, BLOCK_f* y cobertura de rutas permanecen abiertos. La fórmula no está aprobada ni congelada.

La corrección de §33 ya estaba indicada en §34 y desarrollada en §35; este addendum elimina cualquier ambigüedad de precedencia para lectores que consulten la tabla anterior de forma aislada. No cierra LATE_f, XSYNC, exclusión, identificación, ni autoriza implementación o ejecución.



---
## 102. Gate de correspondencia D2→g y exclusión (2026-11-09)

| Gate | Objeto | Estado | Criterio de cierre |
|---|---|---|---|
| MAP-01 | Versiones, actor, alcance, tiempos y factibilidad de B_g0/B_g1 | OPEN | Contrato material por brazo, versión, historia y desviaciones |
| MAP-02 | B→W→C_dep*→A_f*/D_f*→ΔT_acc* | OPEN | Mapping temporal con medidas independientes y verdad/observación separadas |
| MAP-03 | Distribuciones inducidas g_j^ind(a|h;q) y soporte | NOT_IDENTIFIED | Distribuciones por historia/contexto y positividad demostrables |
| MAP-04 | Equivalencia de versiones y diferencias directas | OPEN | Versiones equivalentes o vías directas separadas mediante diseño/estimando |
| MAP-05 | Rutas alternativas/compartidas, recursos y residuos | OPEN | Cobertura suficiente por unidad, frontera, versión y ventana |
| MAP-06 | Exclusión Outcome/Value, medición, interferencia y carryover | NOT_DEMONSTRATED | Evidencia diferenciada por resultado y supuestos de diseño defendibles |
| MAP-07 | Separación LATE_f, θ_Af(q_X*) y θ_A(q) | DEFINED / NOT_IDENTIFIED | Contratos y condiciones de identificación propios para cada estimando |

**Regla de interpretación:** la definición conceptual de B_g^D2 no identifica las distribuciones inducidas g_j^ind. ITT_Z^D2 es efecto de asignación a la política D2; no es por sí mismo θ_A(q), θ_Af(q_X*) ni LATE_f. No se habilita Wald, implementación ni ejecución.



---
## 103. Cierre documental parcial MAP-01/MAP-02 (2026-11-09)

| Subgate | Estado | Resultado documental | Pendiente material |
|---|---|---|---|
| MAP-01a | CONTRACT_FIELDS_DEFINED | Esquema por unidad de asignación, actor, artefacto, runtime/canal y eventos de provisión | Identidades, roles, versiones, hashes y arquitectura real |
| MAP-01b | OPEN | Reglas de reintento, fallo parcial, rollback, desviación y registro de crossover especificadas | Protocolo operativo, ventanas y detección con cobertura suficiente |
| MAP-02a | TEMPORAL_SCHEMA_DEFINED | Anclas basal pre-Z, provisión, C_dep*, A_f*, D_f*/ΔT_acc* y resultados separados | Ventanas, relojes, fuentes e instrumentos |
| MAP-02b | OPEN | Estados 1/0/? y verdad/observación separados | Evidencia independiente, tolerancias, ceguera y cobertura |
| MAP-02c | OPEN | Orden lógico de eventos definido | Validación del mapping temporal con datos/evidencia |

**Regla:** el cierre de campos y esquema no es cierre de intervención, de medición, de primera etapa, de exclusión ni de identificación. No se autoriza implementación o ejecución.



---
## 104. Resultado MAP-05 — adjudicación documental de superficies y PROV (2026-11-09)

| Elemento | Estado | Dictamen |
|---|---|---|
| B-M01…15 | CLASSIFICATION_DEFINED | Vías y falsadores clasificados; evidencia material ? / NO INVENTARIADO |
| PROV-01…12 | CONTRACTS_DEFINED / NOT_EXECUTED | Contratos de control, no PASS |
| MD-C1 | OPEN | Manifiesto real y evidencias incompletos |
| MD-C4 | OPEN | Independencia funcional de alternativas no demostrada |
| IV-G4 | OPEN | Exclusión no demostrada |
| ITT_Z^D2 | CONDITIONAL | Solo efecto de asignación/política si diseño y observación lo permiten |
| LATE_f^D2 | NOT_IDENTIFIED | Gates IV y mapping focal abiertos |
| θ_Af(q_X*) / θ_A(q) | NOT_IDENTIFIED | Mapping a política de accesibilidad y supuestos propios abiertos |

**Prioridad de evidencia:** B-M06, B-M07, B-M09, B-M11, B-M12 y B-M14; B-M10/B-M13 para conocimiento y medición; B-M05 para autorización; B-M02/B-M03/B-M08/B-M15 para dependencias compartidas y residuos.

**Regla:** clasificación documental no equivale a observación, ausencia, invariancia, exclusión ni PASS. No se autoriza ejecución.



---
## 105. Roster probatorio MAP-05 — estado de preparación (2026-11-09)

| Control | Estado | Criterio |
|---|---|---|
| Reutilización de COV-D2-BM01…15 | DOCUMENTED | Scopes lógicos ya previstos en U_G §17.4; no crear duplicados |
| Afirmaciones y destinos por dominio | DOCUMENTED | U_G §26 distingue claim, destino, fuente y efecto de unknown |
| EVIDENCE_REGISTER / CLAIM_EVIDENCE_LINK | DOCUMENTED | Aplicar DEC-C10-080/081; no inventar fuente ni FK PAR |
| Denominadores y universos | OPEN | UNKNOWN; requieren frontera, unidad, versión, etapa, ruta y enumeración |
| Fuentes técnicas | NONE | 0 fuentes recibidas/examinadas; no es ausencia material |
| Filas U_G observadas | NONE | No crear NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT sin objeto identificado |
| Cobertura por B-M | NONE | No 0, no COMPLETE, no inferencia de no-afectación |
| MD-C1 / MD-C4 / IV-G4 | OPEN | Manifiesto, alternativas y exclusión no demostrados |

**Dictamen:** DOCUMENTARY_READY / NO_SOURCE_INVENTORY / COVERAGE_NONE. El siguiente gate es cerrar la legitimidad del universo/denominador y mappings de scope, no iniciar una inspección técnica ni una ejecución. scientific_execution=false; execution_authorized=false.



---
## 106. Legitimidad del universo y denominadores C0/UDG (2026-11-09)

| Control | Estado | Dictamen |
|---|---|---|
| C0 tuple (9 componentes) | DOCUMENTED | DEC-C10-070; dimension fuera de la identidad |
| Stage keys | ACCEPTED ENUM / NOT MAPPED TO SNAPSHOTS | DEC-C10-071; no equivale a SNAPSHOT.phase |
| Route global | ACCEPTED TOKEN | C10S_SCOPE_GLOBAL; no usar NONE/F/A |
| UDG-01 / JCS / UDG-03 / UDG-04 | ACCEPTED DOCUMENTALLY | DEC-C10-073…076; no implementación |
| B-M01…15 vs dimension | CONFLICT RESOLVED DOCUMENTALLY | B-M es dominio de auditoría; dimension=C10S_CONFIG_* |
| COV-D2-BM01…15 | PLANNING LABELS ONLY | No coverage_scope_id físico ni FK |
| Cuadrícula 7×5 | LOGICAL PLANNING GRID | Hasta 35 combinaciones, no denominador ni filas automáticas |
| Unidad raíz↔CMP anchor | OPEN | Mapping exacto pendiente |
| CMP/PAR/REF/RUL/MET | PARTIAL CROSSWALK | Unidades de denominador/mapping físico incompletos |
| Contract/instance/snapshot | NOT MATERIALIZED | Sin tupla C0 instanciable |
| C0 control | DOCUMENTED / NOT IMPLEMENTED / NOT AUDITED | No PASS |
| Denominador / cobertura | UNKNOWN / NONE | No emitir 0 ni COMPLETE |

**Dictamen:** DOCUMENTARY_RECONCILIATION_PARTIAL / NO_C0_INSTANCE / NO_SNAPSHOT / DENOMINATOR_UNKNOWN / COVERAGE_NONE. El siguiente gate es crosswalk de identidad/unidad por clase, no captura técnica.



---
## 107. Crosswalk de identidad y unidad de denominador por clase (2026-11-09)

| Clase | Unidad candidata | Mapping U_G | Estado |
|---|---|---|---|
| CMP | Componente contractual elegible por snapshot | NODE exacto + owner/version; EDGE solo relaciones | OPEN: root anchor y cardinalidad |
| PAR | Owner CMP × parameter_key × versión semántica × captura lógica | Manifiesto; target COVERAGE_SCOPE; DEC-C10-079/080 | ACCEPTED contract; no instance |
| REF | Relación tipada con endpoints/cardinalidad | EDGE mediante M versionado | PARTIAL: DEC-C10-077 conceptual; M/endpoints OPEN |
| RUL | Regla × versión × scope | PREDICATE solo si evaluable; operandos exactos | OPEN |
| MET | Campo metadata × owner/target × tiempo/alcance | Propiedad tipada o snapshot/evidence según función | OPEN |

PASS de mapping no equivale a COMPLETE. 0 requiere universo y enumeración exhaustivos; desconocido/no resuelto permanece ?. Estado global: CROSSWALK_TYPED / PAR_IDENTITY_ACCEPTED / CMP_REF_RUL_MET_MAPPING_PARTIAL / DENOMINATOR_UNKNOWN / COVERAGE_NONE. No member_refs, scopes ni evidencia material.



---
## 108. Mapping NODE raíz ↔ CMP anchor (2026-11-09)

| Control | Estado | Evidencia/criterio |
|---|---|---|
| Root NODE LOGICAL_SERVICE_UNIT | CONCEPTUALLY_ACCEPTED | DEC-C10-089 |
| CMP↔NODE mapping contract | ACCEPTED DOCUMENTALLY | DEC-C10-082; no mapping observado |
| SAME_ENTITY | UNKNOWN | Requiere identidad contractual 1:1 y mapping exacto |
| DISTINCT_ENTITIES | UNKNOWN | Requiere definiciones separadas y NODE distintos |
| CMP-SERVICE-LOGIC-001 | ACCEPTED CONTRACT ID (DEC-C10-069) | Identidad contractual aceptada; anchor U_G por snapshot y mapping material siguen OPEN |
| CMP roster/cardinality | UNKNOWN | Falta universo contractual completo |
| Denominator / coverage | UNKNOWN / NONE | Sin snapshot ni miembros enumerados |

El gate conceptual queda especificado; el mapping material sigue OPEN. No asignar IDs ni crear registros.


---

## 109. N16 — criterio F*, oráculo y adjudicación (2026-11-09)

| Capa/control | Estado | Alcance / límite |
|---|---|---|
| Opción A + F* contrato de trabajo | ACCEPTED | DEC-C10-051; no Design Freeze |
| Familias FP-01…FP-08 | ACCEPTED | DEC-C10-055; arquitectura de familias, no requiredness por instancia |
| Criterio funcional F* | DEFINED / PARTIAL | Ruta completa F1→F2 y A1→A2; predicados/mappings/tolerancias y C0/G/H abiertos |
| Regla no compensatoria | DOCUMENTED | FAIL obligatorio no se compensa; umbrales atómicos abiertos |
| Aplicabilidad O/C/NA/? | SPECIFIED / NOT SEALED | IAM por instancia/etapa pendiente; NA solo ex ante |
| Oráculo independiente versionado | NOT IMPLEMENTED / NOT VALIDATED | Matriz documental no equivale a implementación |
| Generator / Analyzer / Evaluator | ROLE SEPARATION SPECIFIED | Analyzer sin truth/potenciales; Evaluator después de congelar outputs; no probado |
| FP-08 | SEPARATE EVIDENCE GATE | No es propiedad funcional ni compensación |
| Adjudicación material | NOT MATERIALIZED | Sin instancia, snapshots, cobertura ni evidencia |
| Outcome / Value | OUTSIDE F* | No pueden definir ni adjudicar conformidad |

N16: RECONCILED_DOCUMENTARILY / PARTIAL. Siguiente gate: crosswalk atómico SM-01…SM-10 ↔ FP-01…FP-07 ↔ IAM, sin duplicar matrices ni elevar propuestas a decisiones. No código, fixtures, validadores ni ejecución.


---

## 110. Auditoría focalizada de readiness de implementación C10-S (2026-11-09)

**Dictamen:** NOT_READY / SPECIFICATION_INCOMPLETE. Auditoría documental asistida, autoauditoría, no independiente; no es validación de código.

| Dominio | Estado de readiness | Bloqueo real |
|---|---|---|
| Decisiones de arquitectura | REUSABLE / NO REOPEN | Opción A, D2/D1, servicio lógico, familias FP, cardinalidades y DEC-C10-068…092 dentro de sus alcances |
| Instancia funcional | PARTIAL | Especialización completa de CMP/PAR/REF/RUL/MET, C_src/C_dst/M, C0/G/H, F/A y SM↔FP↔IAM |
| DGP | PARTIAL | Ecuaciones, parámetros/distribuciones, versiones, ventanas, actor/recepción/fidelidad, truth y escenarios completos |
| Diseño causal | OPEN | Población/soporte, unidad/interferencia, correspondencia B→g^Af, vías colaterales, exclusión y jerarquía confirmatoria |
| Medición/estadística | OPEN | Medidas independientes A/D/ΔT/Reach/trayectoria/O/V, regla Value, error/missingness, sensibilidad, potencia y réplicas |
| Oráculo/software | NOT IMPLEMENTED | Interfaces, serialización, oráculo independiente, firewall efectivo, fixtures y aceptación por módulo |
| Evidencia U_G | NOT MATERIALIZED | IAM/snapshots/scopes/cobertura sin instancias ni evidencia; implementar solo el subconjunto necesario para el DGP sintético |
| Gate de implementación | BLOCKED | Contrato integrado no aceptado; sin Design Freeze ni autorización explícita |

### Paquetes mínimos de cierre

- **A — Instancia funcional y transformación:** un contrato funcional versionado y especializado, incluyendo F1/F2/A1/A2, C0/G/H, M, IAM, SM↔FP, requiredness, tolerancias y oráculo.
- **B — DGP y diseño causal:** unidad/población, asignación, políticas D2, reloj, mecanismo, soporte, escenarios limpio/adversariales, truth y potenciales.
- **C — Medición y estimandos:** A_f/D_f/ΔT/Reach/trayectoria/Outcome/Value, ITT, efecto de paquete, LATE/θ_Af/θ_A, identificación, error, sensibilidad y potencia.
- **D — Contrato computacional:** Generator/Analyzer/Evaluator, firewall, interfaces, serialización, evidencia, oráculo, fixtures y hashes.
- **E — Aceptación integrada:** trazabilidad requisito→fuente→módulo→test y aceptación del contrato; autorización de código separada de autorización de ejecución.

### Salvaguardas de alcance

No exigir sistema real para crear el fixture sintético; no implementar toda U_G como plataforma genérica; no crear otra matriz/oráculo; no elevar las clasificaciones B-M a evidencia de exclusión; no reutilizar N=2.000/R=1.000, s=.80 o .20/.80 como confirmatorios sin aprobación. No exigir revisión humana externa para continuar especificando.

PR #116: OPEN / DRAFT; base research/c10-d1-protocol-draft, head research/c10-s-consolidation-draft; 100 archivos cambiados y 1.411 commits ahead según comparación consultada. No promoción a main ni cambio de base en este gate.

**Siguiente trabajo:** ejecutar conjuntamente A+B sobre la misma instancia sintética. No código, validadores, fixtures ejecutables, simulación ni ejecución científica. scientific_execution=false; execution_authorized=false.


---

## 111. Regla operativa vinculante — cuatro paquetes C10-S (2026-11-09)

**Unidad de seguimiento:** cuatro paquetes sustantivos: **AB** (instancia funcional + DGP/diseño causal, resueltos conjuntamente), **C** (medición/Value/estimandos), **D** (contrato computacional) y **E** (gate final de aceptación). A y B no se gestionan como paquetes separados.

**Regla de trabajo:** trabajo agrupado de extremo a extremo; reutilizar maestro, decisiones, matrices y registros existentes; no crear documentos ni microgates por subtema; no reabrir decisiones aceptadas; cada requisito debe tener ID, definición operacional, fuente/DEC, estado, decisión pendiente, componente y criterio de aceptación. Clasificar ACCEPTED/DEFINED/OPEN/NOT_REQUIRED/BLOCKED; no inventar mappings, parámetros ni supuestos; explicitar no-identificación. Cerrar cada paquete con resultado integrado, pendientes residuales acotados y reconciliación documental releída. No declarar DONE si quedan contradicciones o requisitos críticos sin criterio de aceptación.

**Criterio DONE:** decisiones críticas aceptadas o NOT_REQUIRED justificado; dependencias resueltas o explicitadas; trazabilidad y criterio de aceptación por requisito; instrumentos actualizados y releídos; sin contradicciones conocidas.

**Secuencia:** AB → C → D → E. E acepta la especificación; no autoriza automáticamente generación de código ni ejecución científica. Código requiere autorización explícita posterior; ejecución científica requiere autorización independiente. Sin ejecución durante la especificación. Estado global: NOT_READY hasta superar E.


---

## 112. Paquete AB — estado integrado y bloqueos materiales (2026-11-09)

**Estado:** IN_PROGRESS / BASE_RECONCILED. El maestro §216 es la especificación integrada de trabajo; esta matriz registra el estado, no duplica el contrato.

| ID | Dominio | Estado | Condición de salida |
|---|---|---|---|
| AB-01 | Roster CMP/PAR/REF/RUL/MET y cobertura | OPEN | Universo/snapshots/scopes/denominador cerrados; REF=0 solo con cobertura exhaustiva |
| AB-02 | C_src/C_dst/M e IAM por etapa | OPEN | Mapping total para obligatorios, versionado y sin colapsos semánticos |
| AB-03 | Cards/identidades F1/F2/A1/A2/τ2 y adaptador | OPEN | Contratos de transición, actor, entradas/salidas, versiones y relaciones |
| AB-04 | Predicados ID/REL/COND/AUTH/RES/DEP/BLOCK | OPEN | Operacionalización material por unidad/tiempo y evidencia; DEP separado de alternativas F* |
| AB-05 | F*, C0, G, H, tolerancias y substituibilidad | OPEN | Oráculo funcional no compensatorio aplicable a F y A |
| AB-06 | Mecanismo D2 | OPEN | Asignación, programación, recepción, intento, éxito, fondo/crossover, rollback y actor |
| AB-07 | Distribución conjunta técnica | OPEN | DGP de cuatro componentes sin independencia asumida; sensibilidad de s |
| AB-08 | Población/q_X*/unidad/soporte/interferencia | PARTIAL | Algoritmo pre-Z, soporte, estratos, unidad y exposición |
| AB-09 | Alternativas y truth/observed R0–R3 | PARTIAL | Universo/cobertura, reglas generadoras y observacionales por predicado |

**Base aceptada reutilizada:** DEC-C10-051…056, 066…069, 071, 079…092; D2 y su precedencia; contrato funcional de servicio; fórmula candidata §67.3; reloj y separación de roles. No reabrir decisiones aceptadas dentro de su alcance.

**Regla:** AB no pasa a DONE por integración narrativa. Requiere especificación concreta, trazabilidad y criterios de aceptación de AB-01…AB-09, relectura y consistencia. No inventar parámetros ni usar s=.80 o .20/.80 como valores confirmatorios. No código, ejecución o simulación; autorizaciones permanecen false.


---

## 113. Paquete AB — especialización propuesta de instancia y rutas (2026-11-09)

**Estado:** PROPOSED / PENDING DECISION. Referencia normativa de trabajo: maestro §217; no duplicar su contenido.

| Dominio | Propuesta | Estado |
|---|---|---|
| Identidad instancia | DEC-C10-069, sin cambio | ACCEPTED |
| Roster | 1 CMP, 2 PAR, 1 RUL, MET; 2 REF si el contrato confirma operand bindings como REF | PROPOSED |
| Valores semánticos | ENABLED=true/PROFILE=STANDARD; casos adversariales true/DISABLED y false/DISABLED | PROPOSED DGP truth |
| Namespaces | C_src/C_dst/M sintéticos v1.0.0 | PROPOSED |
| Mapping ENUM | STD→STANDARD; RO→READ_ONLY; OFF→DISABLED, total/injectivo | PROPOSED |
| Rutas | F1/F2 focal y A1/A2 alternativa bajo mismo F* | DEFINED AT FUNCTIONAL LEVEL; MATERIAL CARDS OPEN |
| F* | FP-01…FP-07 no compensatorios; FP-08 gate probatorio | ACCEPTED ARCHITECTURE; INSTANCE PROFILE PROPOSED |
| C0/G/H | G propuesto como unidad lógica completa; C0/H incompletos | PARTIAL / OPEN |
| D2 | B_g0/B_g1 según DEC-C10-067; ARCH-B1 candidata | POLICY ACCEPTED; ISOLATION OPEN |

**Regla:** la propuesta no se convierte en DEC por persistencia. Aceptación expresa necesaria para los elementos marcados PROPOSED. H, distribución conjunta de C_dep*, cumplimiento, fondo/crossover, soporte, MD-C1/MD-C4 y oráculo siguen abiertos. No código, fixtures, simulación ni ejecución.


---

## 114. DEC-C10-093 — base AB aceptada; reservas abiertas

**Estado de la base:** ACCEPTED WORKING DESIGN BASE. **Estado del paquete:** IN_PROGRESS.

| Dominio | Estado tras DEC-C10-093 |
|---|---|
| Identidad de instancia DEC-C10-069 | ACCEPTED; no reabrir |
| Núcleo ENABLED/PROFILE/REQUIRE DEC-C10-068 | ACCEPTED; no reabrir |
| Rutas F1/F2 y A1/A2 bajo F* común | ACCEPTED AS WORKING BASE |
| Mapping semántico total/injectivo | ACCEPTED AS WORKING CANDIDATE; físico OPEN |
| B como provisión técnica D2; ARCH-B1 | Frontera conceptual ACCEPTED; arquitectura/aislamiento OPEN |
| REF vs AST; roster IAM/cobertura | OPEN |
| FP-05; G/C0/H | OPEN |
| Mecanismo y distribución conjunta D2; MD-C1/MD-C4 | OPEN |
| Población, q_X*, positividad, unidad, soporte/interferencia | OPEN |
| Oráculo, truth/observed, cegamiento/adjudicación | OPEN |

**Control:** no reabrir elecciones conceptuales aceptadas; resolver las reservas como una sola especificación integrada. No declarar AB DONE ni Design Freeze, y no generar código/fixtures ni ejecutar validaciones, simulaciones o experimentos. Autorizaciones false.


---

## 115. Paquete AB — especificación integrada y gates residuales (2026-11-09)

**Estado:** INTEGRATED SPECIFICATION PROPOSED / NOT DONE / NOT IMPLEMENTABLE. Fuente desarrollada: maestro §219; no duplicar el contrato.

| ID | Resultado integrado | Estado final de esta pasada | Gate residual |
|---|---|---|---|
| AB-01 | Inventario constitutivo por snapshot; CMP=1, PAR=2, RUL=1, dos operand bindings, POL=0, MET obligatorio | LOGICAL ROSTER DEFINED | Confirmar representación física REF/AST, roster material y cobertura exhaustiva |
| AB-02 | Namespaces sintéticos y mapping BOOL/ENUM total e inyectivo; serialización determinista exigida; IAM por rol/acción/objeto/etapa | SEMANTIC MAPPING DEFINED | Gramática, serialización/canonicalización y matriz IAM instanciada |
| AB-03 | F1→F2 y A1→A2 con fichas contractuales simétricas, entradas/salidas/snapshots/eventos | TRANSITION CONTRACT DEFINED | Artefactos/versiones, actor y runtime concretos |
| AB-04 | Predicados ID/REL/COND/AUTH/RES/DEP/BLOCK y lógica trivaluada 1/0/?; DEP focal no sustituye alternativas | SEMANTIC RULE DEFINED | Instrumentos, fuentes, cobertura y adjudicación material |
| AB-05 | F* no compensatorio FP-01…07; FP-08 probatorio; G y C0 definidos; H común | ACCEPTANCE LOGIC DEFINED | H* con unidad/valor/ancla; oráculo independiente; evidencia FP-08 |
| AB-06 | Máquina de eventos D2 y distinción Z/programación/recepción/intento/éxito/fondo/crossover/rollback | MECHANISM CONTRACT DEFINED | Parámetros, protocolo material y registro verificable |
| AB-07 | C_dep* como conjunción de cuatro estados con distribución conjunta condicional | JOINT-DGP FORM DEFINED | Probabilidades/parámetros y sensibilidad; no asumir independencia ni s=.80 |
| AB-08 | Población elegible pre-Z, P*_τ2/P*_F, q_X*, soporte, unidad e interferencia | POPULATION CONTRACT DEFINED | Algoritmo instanciado, q_X*, soporte y cluster según topología |
| AB-09 | R0–R3, adversariales, truth/observed separados y regla exhaustiva para 0 frente a ? | SCENARIO/TRUTH CONTRACT DEFINED | Truth tables y validación del oráculo/cegamiento/adjudicación |

**Regla de lectura:** “contract/logic defined” significa especificación documental, no objeto implementado ni evidencia observada. Los gates residuales no se consideran cerrados por esta pasada. No declarar AB DONE, Design Freeze ni readiness de implementación. scientific_execution=false; execution_authorized=false.

## 116. DEC-C10-094 — estado tras aceptación de resoluciones materiales AB (2026-11-09)

| Dominio | Resolución aceptada | Gate residual | Estado |
|---|---|---|---|
| AB-01/02 inventario, REF/AST, mapping, IAM | Inventario lógico, operand bindings únicos, mapping y matriz IAM definidos | Encoding físico/serialización y cobertura material | DESIGN RESOLVED / EVIDENCE OPEN |
| AB-03/04 rutas y accesibilidad | F1/F2 y A1/A2; predicados y lógica 1/0/? | Fichas instanciadas y medición/cobertura | DESIGN RESOLVED / EVIDENCE OPEN |
| AB-05 F*, FP, G/C0/H, oráculo | FP-05, F* no compensatorio, G/C0 y H común | Valor/unidad/ancla H; FP-08 y evidencia oráculo | DESIGN RESOLVED / EVIDENCE OPEN |
| AB-06/07 D2 y C_dep* | Event log por etapas y distribución conjunta condicional | Parámetros D2, sensibilidad, MD-C1/MD-C4 | DESIGN RESOLVED / EVIDENCE OPEN |
| AB-08 población/soporte | Elegibilidad pre-Z, q_X* pre-Z, positividad y unidad/interferencia explícitas | Algoritmo/roster, q_X*, soporte y cluster real | DESIGN RESOLVED / EVIDENCE OPEN |
| AB-09 escenarios/oráculo | R0–R3, truth/observed y Generator/Analyzer/Evaluator separados | Truth tables, validación, cegamiento y adjudicación | DESIGN RESOLVED / EVIDENCE OPEN |

**Dictamen:** resoluciones de diseño AB aceptadas; AB permanece IN_PROGRESS y NOT IMPLEMENTABLE. Ningún gate de evidencia se considera satisfecho por esta decisión. No Design Freeze ni autorización de ejecución.


## 117. Interfaz AB→C — contrato de transferencia (2026-11-09)

| Dominio | Contrato | Gate/resultado requerido | Estado |
|---|---|---|---|
| Estimandos | ITT_Z^D2, FS_Cdep/FS_Af/FS_Df, ψ_policy/ψ_B, LATE_f, θ_Af, θ_A, mediación y residual separados | Población, régimen, horizonte, versión y escala compatibles; no sustitución | CONTRACT DEFINED |
| Inputs AB | Unidad/población, Z/B event log, C0/G/H, C_dep conjunto, A_f/D_f/ΔT_acc, vías colaterales, Outcome/Value, truth/observed, soporte | Identidad, versión, cobertura y UNKNOWN explícitos | MATERIAL INPUTS OPEN |
| Outputs C | ITT Outcome/Value, primeras etapas, diagnóstico de diseño, dictamen IV, mapping B→g, recuperación DGP y abstención | Gates propios por conclusión y métricas/umbrales preespecificados | ANALYTIC CONTRACT DEFINED |
| Atribución ΔT_acc→Value | Variación de accesibilidad y medición independiente; soporte; separación de vías directas/alternativas/interacciones | No equiparar ITT o éxito del Analyzer a contribución causal general | NOT ESTABLISHED |
| Mediación/residual | Intervención mediadora y descomposición formal | Confusión postratamiento, régimen, escala y horizonte comunes | OPEN / NOT IDENTIFIED |

**Dictamen:** la interfaz contractual AB→C queda definida en maestro §221. C puede avanzar documentalmente; no puede tratar inputs AB como congelados ni declarar identificación. Sin Design Freeze ni ejecución.


## 118. Paquete C — identificación, Value y atribución causal (2026-11-09)

| Dominio | Especificación integrada | Gates pendientes | Estado |
|---|---|---|---|
| Jerarquía causal | ITT_Z^D2, primeras etapas, efecto paquete, LATE_f, θ_Af, θ_A, mediación y residual separados | Mapping B→g^Af, IV, población/soporte | CONTRACT RECONCILED |
| Outcome / Value | Medición independiente; Value vectorial primario durante identificación | Dimensiones, escalas, observadores, regla de ausencia/ponderación | DESIGN PROPOSED |
| ΔT_acc y mediación | Mediador transformacional completo; Reach/trayectoria como posibles mediadores secuenciales | Intervención mediadora, confusión post-Z, régimen y horizonte | OPEN / NOT IDENTIFIED |
| Identificación | ITT primero; primeras etapas separadas; IV solo tras gates; sensibilidad/cotas | Exclusión, monotonicidad, versiones, interferencia, medición | NOT ESTABLISHED |
| DGP / Analyzer | Truth oculta, Analyzer aislado, Evaluator separado; recovery y abstención por estimando | Escenarios, umbrales, leakage audit | CONTRACT REUSED / NOT EXECUTED |
| Estadística | P177/P178 y pérdidas/censura P183 | MDE, potencia, precisión, N, R, tolerancias | OPEN |
| Validez de constructo | P179/P182, fuentes/versiones y error por dimensión | Instrumentos, cegamiento, reproducibilidad | OPEN |

**Dictamen:** C dispone de arquitectura documental integrada; no está aprobado, congelado, implementable ni ejecutado. No hay cambio en claims ni en estado científico de TGCV. No autoriza simulación.


## 119. Paquete C — jerarquía y contratos operativos (2026-11-09)

| ID | Resolución / control | Estado | Dependencia |
|---|---|---|---|
| C-01 | θ_A(q) es pregunta científica primaria; ITT_Z^D2 es primario solo como estimando de asignación S4-R | PROPOSED | Aceptación y coherencia C10-D1/S4-R |
| C-02 | Value vectorial y Outcome separado, análisis por dimensión | PROPOSED | Fichas P179/P182 |
| C-03 | No selección de dimensiones/pesos/índice/MDE por default o post hoc | PROPOSED | Contexto de valoración y P178 |
| C-04 | Registro versionado de estimando con campos §223.2 | PROPOSED | Diccionario y población AB |
| C-05 | ITT sin ajuste post-Z; missingness y selección tratados explícitamente | PROPOSED | P177/P183 y diseño |
| C-06 | Dictamen por estimando y dimensión; abstención correcta | PROPOSED | P177/P183 |
| C-07 | Truth oculta al Analyzer; Evaluator separado | PROPOSED | Firewall y auditoría leakage |

**Gates materiales:** dimensiones/indicadores Value, Outcome, H, régimen de mediación, población/soporte, unidad/interferencia, mapping B→g^Af, exclusión, medición/cegamiento, multiplicidad, MDE, potencia, N, R y umbrales.

**Dictamen:** especialización operativa propuesta; no aceptada ni congelada. No cambia el estado científico ni autoriza implementación/ejecución.


## 120. Paquete C — contrato de medición Outcome/Value (2026-11-09)

| Control | Criterio de salida | Estado |
|---|---|---|
| O-FICHA | Cada indicador Outcome tiene constructo, unidad, fuente, cálculo, baseline, ventana y missingness | OPEN |
| V-FICHA | Cada dimensión Value tiene beneficiario/contexto, constructo, indicador, escala, dirección, baseline/ventana y trade-offs | OPEN |
| O/V-SEPARATION | Outcome y Value no se sustituyen ni se reutilizan circularmente | PROPOSED |
| ADJUDICATION | A/ΔT_acc se adjudican sin consultar O/V; desacuerdo y error registrados | OPEN |
| FIREWALL | Analyzer no recibe truth ni etiquetas ocultas; Evaluator separado | PROPOSED |
| OBS-STATE | Estados de observación y ausencia no se colapsan en cero/UNKNOWN | PROPOSED |
| PREFSPEC | Dimensiones confirmatorias, multiplicidad y reglas fijadas ex ante | OPEN |

**Gates:** microdominio/beneficiarios; indicadores y fuentes; escalas/unidades; horizonte H y ventanas; validez/error/acuerdo; cegamiento viable; ausencia/censura; trade-offs; multiplicidad y umbrales.

**Dictamen:** se define la estructura de medición, no sus valores materiales. No se declara operacionalización completada ni se autoriza implementación/ejecución.


## 121. Paquete C — identificación y evaluación estadística (2026-11-09)

| Control | Criterio de salida | Estado |
|---|---|---|
| C-ID-01 | ITT, primeras etapas, ψ_policy, ψ_B, LATE_f, θ_Af y θ_A diferenciados por resultado/población/horizonte | PROPOSED |
| C-ID-02 | D_f*, D_f^obs y primeras etapas independientes; ninguna etapa técnica sustituye accesibilidad | OPEN |
| C-ID-03 | DAG/temporalidad; confusores basales/postratamiento; mediadores y rutas colaterales | OPEN |
| C-ID-04 | Mediación con estimando/intervención propia; no ajuste post-Z ni resta de efectos incompatibles | PROPOSED |
| C-ID-05 | Población pre-Z, q_X*, positividad, overlap, soporte y transporte | OPEN |
| C-ID-06 | Unidad asignación/análisis/exposición e interferencia/carryover | OPEN |
| C-ID-07 | Missingness, censura, selección y error diferencial por brazo | OPEN |
| C-ID-08 | Sensibilidad, bounds y tipping points con rangos justificados | OPEN |
| C-ID-09 | Generator/Analyzer/Evaluator separados y firewall auditado | PROPOSED |
| C-ID-10 | Métricas por estimando×resultado×DGP; falsos positivos de identificación y abstención | OPEN |
| C-ID-11 | Potencia, precisión, N, multiplicidad y réplicas Monte Carlo justificadas | OPEN |
| C-ID-12 | Tolerancias y criterios recover/fail/partial/not identified fijados ex ante | OPEN |
| C-ID-13 | Crosswalk P177/P178/P179/P182/P183 y reconciliación C10-D1/S4-R | PROPOSED |

**Dictamen:** la estrategia metodológica queda especificada como propuesta; no hay parámetros, identificación, potencia, N, umbrales ni evaluación ejecutada cerrados. C permanece NOT APPROVED / NOT FROZEN / NOT IMPLEMENTABLE. Sin autorización de implementación o ejecución.


## 122. Auditoría de correspondencia contractual de mediación (2026-11-10)

| Control | Contrato/fuente correctamente aplicable | Estado verificado |
|---|---|---|
| No ajustar ITT por mediadores post-Z | P177-06 | DEFINED; no ejecutado |
| Separar política y atribución focal | P177-12; C10-D1/S4-R §18/§23 | DEFINED; mapping/identificación OPEN |
| Validez y adjudicación independiente de A | P182-01/02/06/07 | DEFINED; evidencia/operacionalización OPEN |
| Ausencia de A y efecto en identificación | P183-08 | DEFINED; no cubre toda la mediación |
| Outcome y Value independientes | P177-05; P179-01…03 | DEFINED; fichas concretas OPEN |
| Estimando/intervención mediadora y confusión inducida | Maestro §225.3 | PROPOSED; contrato específico incompleto |

**Corrección:** la referencia P177-05…08 como cobertura de mediación en Register §72 queda retirada. Esos IDs no tienen ese alcance. El gate C-MED permanece OPEN; no se declara cobertura contractual completa ni identificación.

**Dictamen:** auditoría documental PASS para detectar y corregir la referencia; C-MED OPEN; paquete C NOT APPROVED / NOT FROZEN / NOT IMPLEMENTABLE. Sin ejecución.


## 123. Auditoría ampliada de correspondencia P177–P183 (2026-11-10)

| Dominio | Referencia precisa | Estado |
|---|---|---|
| Primera etapa | P177-02 | DEFINED; no ejecutado |
| Wald/LATE e instrumento débil | P177-03/04 | DEFINED; supuestos IV OPEN |
| N, clúster, réplicas y error Monte Carlo | P178-SIM-02/03/04/05; SIM-01/09/10 para potencia/métricas/parámetros | DEFINED; parámetros OPEN |
| Censura, sensibilidad, bounds y dictamen | P183-09/10/11/12 | DEFINED; supuestos/rangos OPEN |
| Trade-offs y agregación Value | P179-06/08 | DEFINED; reglas y dimensiones OPEN |
| Recuperación, firewall y clasificación | P177-10/12; P182-11; P183-12 | Cobertura parcial; falsa identificación y abstención requieren criterios explícitos |

**Dictamen:** las referencias erróneas/incompletas se corrigen en el registro; no se interpreta la presencia de un ID como prueba de ejecución o cierre. Gates C-MED y C-ANALYZER permanecen OPEN.


## 124. Gates de mediación y evaluación del Analyzer — especialización candidata (2026-11-10)

| Gate | Criterio de cierre | Estado |
|---|---|---|
| C-MED-01 | Estimandos interventional indirect/direct, mediador completo/focal y población/horizonte versionados | OPEN |
| C-MED-02 | DAG longitudinal, orden temporal y confusores basales/postratamiento | OPEN |
| C-MED-03 | Método compatible con confusión inducida, soporte secuencial y positividad | OPEN |
| C-MED-04 | Rutas colaterales, interacción, mediadores múltiples y sensibilidad/bounds | OPEN |
| C-MED-05 | Criterio de recuperación/abstención por DGP y dimensión | OPEN |
| C-AN-01 | Truth/observed/firewall y Evaluator separados; leakage audit | PROPOSED |
| C-AN-02 | Recuperación puntual solo en DGP identificables; bounds en parciales | PROPOSED |
| C-AN-03 | Falsa identificación y falsa atribución focal medidas con denominador explícito | OPEN |
| C-AN-04 | Abstención correcta y falsa abstención adjudicadas | OPEN |
| C-AN-05 | Tolerancias, métricas, réplicas inválidas y reglas de aceptación preespecificadas | OPEN |

**Dictamen:** propuesta de especialización; no equivale a aceptación de los métodos, parámetros o umbrales. C-MED y C-ANALYZER no están cerrados. Sin implementación o ejecución.


## 125. Reconciliación de estimandos, temporalidad y gates C-MED/C-ANALYZER (2026-11-10)

| Control | Regla verificable | Estado |
|---|---|---|
| Separación θ_A(q) / mediación B-D2 | θ_A(q) es efecto de políticas factibles de accesibilidad; mediación B es secundaria y requiere estimando propio | PROPOSED |
| Objeto ΔT_acc | Crosswalk DGP↔C10-D1 §27.1 y separación de ΔE_T | OPEN |
| Confusión inducida | Variables post-B/pre-t3 que afectan ΔT_acc y Value deben modelarse longitudinalmente | OPEN |
| Downstream | Reach, trayectoria, K, selección, ejecución y O no se ajustan mecánicamente para efecto total | DEFINED |
| g0/g1 y q | Políticas implementables, factibles y con soporte común | OPEN |
| Mediación interventional B | Estimando/método longitudinal compatible si se conserva como pregunta secundaria | OPEN |
| Firewall | Generator truth / Analyzer observed / Evaluator truth tras sellado | PROPOSED |
| Clasificación de Analyzer | Identificación puntual/parcial/no identificación/indeterminación | PROPOSED |
| Falsos positivos/abstención | Denominadores conceptuales y adjudicación por DGP | DEFINED IN PRINCIPLE; thresholds OPEN |
| Parámetros de aceptación | Tolerancias, multiplicidad, N, réplicas y precisión MC | OPEN |

**Dictamen:** la estructura metodológica está reconciliada documentalmente; no hay identificación ni ejecución demostradas. C-MED y C-ANALYZER permanecen OPEN. No Design Freeze ni implementación.


## 126. Precedencia y correspondencia del objeto ΔT_acc

| Campo DGP vigente | Referencia de verdad | Crosswalk C10-D1 §27.1 | Estado |
|---|---|---|---|
| ΔU* | Cambios en unidades/transformaciones y estado estructural | A⁺/A⁻/A^reconf mediante matching de identidad | CANDIDATE; reglas completas OPEN |
| ΔR* | Relaciones/dependencias | ΔR | CANDIDATE; granularidad OPEN |
| ΔC* | Condiciones/configuraciones estructurales | ΔC | CANDIDATE; clasificación constitutiva/temporal OPEN |
| ΔX* | Estado/contexto estructural que altera accesibilidad | Sin equivalente automático; clasificar campo a campo como ΔC, historia q o fuera del mediador | OPEN |
| ΔValidity_e | Validez epistémica de evidencia | ΔE_T, no ΔT_acc | DEFINED BY DGP §30 |

**Precedencia:** DGP §30 gobierna sobre la expresión histórica de §3.3. MED-02 permanece OPEN; no se acepta equivalencia automática.


## 127. MED-02 — clasificación semántica de ΔX*

| Control | Regla | Estado |
|---|---|---|
| Precedencia | DGP §30 gobierna; ΔValidity_e pertenece a ΔE_T | DEFINED |
| X* | Estado/contexto efectivo constitutivo de accesibilidad en el tiempo; no transformación ni regla | DEFINED AT CONCEPTUAL LEVEL |
| Mapping C10-D1 | ΔX* se conserva como contexto DGP; sus consecuencias se reflejan en las coordenadas analíticas pertinentes, sin sumarlo dos veces | PROPOSED |
| Campo que es predicado | Reclasificar explícitamente en C* | PROPOSED |
| Historia no constitutiva | q solo si puede estandarizarse coherentemente y con soporte | CONDITIONAL |
| Campo fuera de frontera | Fuera del mediador, con registro si es covariable/contexto | PROPOSED |
| Campo no resuelto | UNKNOWN/?; no forzar equivalencia | DEFINED |
| Roster microdominio | Inventario y adjudicación campo a campo, event_id y truth/observed | OPEN |

**Dictamen:** MED-02 conceptual parcialmente resuelto; MED-02c/d permanecen OPEN. No Design Freeze, implementación ni ejecución.


## 128. MED-02c — roster de superficies del microdominio Opción A

El maestro §232 contiene el roster documental parcial y su clasificación semántica. Regla: el tipo deriva de la función del subcampo, no del dominio B-M ni de su nombre. U* transformación; R* relación/topología; C* regla, permiso, recurso o condición de realizabilidad; X* estado/contexto efectivo constitutivo; E_T evidencia/observación. Un mismo dominio B-M puede contener varios tipos y debe descomponerse.

Se reconocen como identidades contractuales de referencia las aceptadas por DEC-C10-069. ENABLED/PROFILE son PAR nucleares; RETRY-COUNT candidato; REF con cardinalidad/cobertura IAM pendiente. Contexto runtime/host y estado persistente son candidatos X* solo si alteran accesibilidad; logs, hashes, cobertura y oráculo son E_T; endpoint/red son R* y ACL/firewall son C*. Recursos, seguridad y rendimiento requieren regla funcional para clasificarse.

**Estado:** roster documental parcial DOCUMENTED; campos/valores reales, truth/observed, event_id y matching de snapshots OPEN. MED-02 no cerrado.


## 129. DAG Opción A/D2 — control de vías colaterales y mediación

| Control | Criterio de cierre | Estado |
|---|---|---|
| DAG-01 | Orden temporal t−1…t9 y snapshots inmutables; sin causalidad retrospectiva desde ejecución | DEFINED / CANDIDATE |
| DAG-02 | Separación Z, B, W_programmed, W_attempt, S_install, C_dep*, A_f*, D_f*, ΔT_acc* | DEFINED / CANDIDATE |
| DAG-03 | Aplicación campo a campo del roster U*/R*/C*/X*/E_T a B-M01…15 | PARTIAL; inventario efectivo OPEN |
| DAG-04 | Auditoría de vías colaterales B→recursos/capacidad, permisos/seguridad, A1/A2, coste/latencia/calidad, K/selección, medición y spillovers | OPEN |
| DAG-05 | D2 común en condiciones no focales conforme DEC-C10-067; evidencia de invariancia | OPEN |
| DAG-06 | Mediador conjunto ΔT_acc*; A_f* predicado/proyección y D_f* derivado, sin doble mediación | DEFINED / CANDIDATE |
| DAG-07 | Mapping B→g^Af, soporte y exclusión para interpretar ITT como θ_A(q) | OPEN |
| DAG-08 | Confusores mediador–Outcome inducidos por B: estrategia longitudinal o conclusión limitada a paquete | OPEN |
| DAG-09 | Truth/observed E_T separados; UNKNOWN/? no equivale a 0 | DEFINED |

**Dictamen:** DAG documental incorporado como candidato en maestro §233. No cierra C-MED, MED-02 ni gates de identificación; no autoriza implementación ni ejecución.

## 130. AB — ledger integrado de inputs residuales (2026-11-10)

Fuente operativa: `C10_S_AB_RESIDUAL_INPUT_CLOSURE_LEDGER_DRAFT_001.md`.

| Input | Gate | Estado | Regla de cierre |
|---|---|---|---|
| AB-M01 REF/AST | AB-01 | OPEN | Reconciliar gramática AST, catálogo REF y schema; cada binding exactamente una vez |
| AB-M02 schema/canonicalización | AB-02 | OPEN | Separar envelope UDG-01 de payload C_src/C_dst; mapping físico explícito |
| AB-M03 TID/SID/RID/cards | AB-03 | OPEN | Cuatro cards versionadas y contratos de transición compatibles |
| AB-M04 predicados/evidencia | AB-04 | OPEN | Crosswalk por campo, unidad, tiempo, truth, observación y cobertura |
| AB-M05 H* | AB-05 | OPEN | Ancla, valor y unidad comunes preespecificados |
| AB-M06 MD-C1/MD-C4 | AB-05/06 | OPEN | Manifiesto y evidencia pre/post/rollback y no-afectación A1/A2 |
| AB-M07 D2 joint DGP | AB-06/07 | OPEN | Event model y distribución conjunta condicional justificada |
| AB-M08 población/q_X* | AB-08 | OPEN | Algoritmo pre-Z, estratos, pesos, positividad y soporte |
| AB-M09 unidad/interferencia | AB-08 | OPEN | Asignación/análisis/exposición y cluster coherentes con topología |
| AB-M10 oráculo | AB-05/09 | OPEN | Independencia, versión, cegamiento y adjudicación validados |
| AB-M11 R0–R3 | AB-09 | OPEN | Universo, truth tables, observación y missingness explícitos |

**Dictamen:** diseño documental resuelto en parte; inputs materiales y evidencia OPEN. No AB DONE, Design Freeze ni readiness de implementación. `scientific_execution=false`; `execution_authorized=false`.

## 131. AB-M01/M02 — resultado de reconciliación (2026-11-10)

| Subgate | Estado | Dictamen |
|---|---|---|
| AB-01 roster lógico/operandos | DESIGN RESOLVED | DEC-C10-068/093/094 |
| AB-01 REF vs AST físico | OPEN | AST 4/16/16 no fija serialización; dos bindings una sola vez |
| AB-01 IAM por snapshot y cobertura | OPEN | DEC-C10-076/077/078 no instancia filas ni denominadores |
| AB-02 mapping BOOL/ENUM | DESIGN RESOLVED | ENABLED BOOL exacto; PROFILE STD/RO/OFF total e inyectivo |
| AB-02 schema/namespaces/payload | OPEN | No hay schema físico de configuración aceptado |
| AB-02 canonicalización payload | OPEN | DEC-C10-074 aplica a UDG-01, no extensible por analogía |
| AB-02 DEFAULT confirmatorio | NOT_IN_BASELINE | DEC-C10-068 no acepta DEFAULT para ENABLED/PROFILE |

Referencia: ledger AB §8. Sin nuevo Decision Record, schema, filas IAM, snapshots, hashes ni validación ejecutable.

## 132. AB-M03/M04 y AB-TIME-01 — resultados documentales (2026-11-10)

| Subgate | Estado | Dictamen |
|---|---|---|
| AB-03 composición de rutas | DESIGN RESOLVED | F1→F2 y A1→A2, mismo F* |
| AB-03 TID/SID/RID y cards materiales | OPEN | Funciones de F2/A1/A2 no concretadas; identidades y versiones faltan |
| AB-04 crosswalk A_f* y lógica trivalente | DESIGN RESOLVED / PARTIAL | Reutilizar crosswalk y MEAS-001, no duplicarlos |
| AB-04 inventario/captura por campo | OPEN / NONE | B-M01…15 son superficies; U_G no tiene snapshots reales |
| AB-TIME-01 índices numéricos | OPEN | DGP: baseline t−1/Z t0; Path Matrix: baseline t0/asignación t1 |

Regla provisional: usar nombres de eventos y precedencia, no índices numéricos intercambiables. Fuente: ledger AB §§9.1–9.4. Sin código ni ejecución.

## 133. AB-M05…M11 — inputs materiales y H_path/H_time (2026-11-10)

| Subgate | Estado | Dictamen |
|---|---|---|
| AB-05 C0/G/F* | DESIGN RESOLVED | H* temporal ancla/valor/unidad OPEN; oráculo no validado |
| AB-TIME-02 H | OPEN | H=3 de Path Matrix es profundidad candidata, no H_time |
| AB-06 D2 programming | DESIGN RESOLVED | W_programmed por política; W_attempt/receipt/fondo/retries/rollback OPEN |
| AB-07 C_dep joint | OPEN | 16 celdas/estrato o equivalente; sin probabilidades aprobadas |
| AB-08 población/q_X*/soporte | PARTIAL/OPEN | P*_τ2 ≠ P*_F; algoritmo, distribución y common support faltan |
| AB-08 unidad/interferencia | OPEN | Topología y exposure/cluster no materializados |
| AB-09 oracle/R0–R3 | DESIGN RESOLVED / EVIDENCE OPEN | Truth tables, observación, cegamiento, adjudicación y firewall no validados |

Referencia: ledger AB §10. No usar s=.80 ni .20/.80; no asignar H=3 como horizonte temporal.

## 134. Propuesta integrada de resolución AB para aceptación (2026-11-10)

| Bloque | Recomendación | Estado |
|---|---|---|
| REF/AST y payload | Reconciliar contra gramática/schema; una representación por binding; no extrapolar JCS UDG-01 | TECHNICAL OPEN |
| Cards F1/F2/A1/A2 | Completar como identidades sintéticas versionadas, sin producto/mecanismo real | USER ACCEPTANCE REQUIRED |
| Field roster A_f* | Reutilizar crosswalk y matriz; instanciar solo field_id sintéticos y 1/0/? | DESIGN PARTIAL / MATERIAL OPEN |
| H | Separar H_path y H_time; H_time tras Outcome/Value | USER ACCEPTANCE REQUIRED |
| D2 eventos | Especificar actor/artefacto/versiones sintéticas; separar programación, intento, receipt, instalación y C_dep | DESIGN PARTIAL |
| C_dep | Distribución conjunta por brazo/estrato y sensibilidad justificada; no usar .80 ni .20/.80 heredados | USER ACCEPTANCE REQUIRED |
| Población/q_X* | Elegibilidad C0 pre-Z, P*_τ2≠P*_F, soporte explícito | USER ACCEPTANCE REQUIRED |
| Interferencia | No interferencia solo como verdad estipulada de R0; adversarial compartido obligatorio | USER ACCEPTANCE REQUIRED |
| Oracle/R0–R3 | Reutilizar arquitectura y completar truth/observación, adjudicación y firewall | DESIGN PARTIAL / VALIDATION OPEN |
| MD-C1/MD-C4 | Mantener como evidencia probatoria abierta | OPEN / NONE |

La propuesta completa y sus límites constan en ledger AB §11. No constituye aceptación del usuario, Design Freeze ni autorización de implementación/ejecución.

## 135. Aceptación de la propuesta integrada AB (2026-11-10)

| Decisión | Estado tras aceptación | Límite explícito |
|---|---|---|
| AB-03-SYN: cards sintéticas F1/F2/A1/A2 | ACCEPTED DESIGN RULE | IDs/versiones sintéticos; sin producto, mecanismo real ni implementación |
| AB-05-H: H_path/H_time | ACCEPTED DESIGN RULE | H_time, ancla, valor y unidad OPEN hasta Outcome/Value |
| AB-08-POP: C0 pre-Z y poblaciones | ACCEPTED DESIGN RULE | P*_τ2 ≠ P*_F; q_X*, soporte, pesos y estratos concretos OPEN |
| AB-09-INT: interferencia | ACCEPTED DESIGN RULE | no interferencia solo en verdad R0; adversariales con interferencia |
| AB-06/07-PARAM: D2/C_dep | ACCEPTED METHOD | método de justificación/sensibilidad; parámetros numéricos OPEN |
| REF/AST y schema | TECHNICAL OPEN | reconciliar gramática y contratos; un binding, una representación |
| MD-C1/MD-C4 y cobertura | OPEN / NONE | no se sustituye evidencia material por estipulación DGP |

La aceptación no cierra AB, no aprueba causalidad empírica ni autoriza Design Freeze, implementación o ejecución. AB continúa IN_PROGRESS.

## 136. AB-M01 — resolución semántica REF/AST (2026-11-10)

| Subgate | Estado | Resolución |
|---|---|---|
| Naturaleza de los dos operand bindings | DESIGN RESOLVED | Referencias tipadas AST→PAR: ENABLED BOOL y PROFILE ENUM |
| Objetos REF por esos bindings | NOT APPLICABLE | No son relaciones/dependencias constitutivas; no duplicar |
| Encoding/schema AST físico | OPEN | No definido por el perfil AST 4/16/16 |
| Serialización/canonicalización | OPEN | JCS UDG-01 no se extrapola al payload |
| Integridad/versionado del binding | OPEN | Debe fijar clave/versión PAR del snapshot y tipo concordante |

Un REF separado requiere relación constitutiva independiente. Fuente: ledger AB §13. Sin parser, constraints, fixture ni validación.

## 137. Estado AB-03/04 tras especificación sintética abstracta (2026-11-10)

| Subgate | Resultado | Límite |
|---|---|---|
| AB-03 identidad/semántica de cards | DESIGN SPECIFIED — TID/SID sintéticos F1/F2/A1/A2 | No RID/EID, producto, formato, mecanismo físico ni ejecución |
| AB-03 contratos de card | DESIGN SPECIFIED — propósito, I/O lógico, pre/postcondiciones, APP, eventos y fallos | Mappings, valores, recursos, tolerancias, C0 y H_time OPEN |
| AB-03 rutas | DESIGN SPECIFIED — πF=(F1,F2), πA=(A1,A2) | Substituibilidad e independencia material no demostradas |
| AB-04 field roster | SEMANTIC CROSSWALK SPECIFIED — U*/R*/C*/X*/E_T | field_id semánticos, no columnas/schema físico |
| AB-04 temporal/evidencia | REUSED — snapshots, 1/0/?, truth/observed, PM-01…18 | Truth tables, cobertura y evidencia material OPEN |
| MD-C1/MD-C4 | OPEN / NONE | No se reemplazan por truth estipulada del DGP |

AB-03/04 no pasan a DONE ni autorizan Design Freeze, fixtures, implementación o ejecución científica.


## 138. Estado AB-01/02 tras reconciliación semántica (2026-11-10)

| Subgate | Estado | Límite |
|---|---|---|
| AB-01 operand bindings | DESIGN RESOLVED | AST→PAR tipado, exactamente dos; no REF duplicado |
| AB-01 encoding AST/payload | OPEN | schema, escaping, canonicalización y constraints no definidos |
| AB-02 PAR por etapa | ACCEPTED BY DEC-C10-083 | Siete stage_key; preservación F1/A1 y observación aplicada F2/A2 |
| AB-02 CMP | ACCEPTED BY DEC-C10-082 | Anclaje 1:1 a NODE por snapshot exacto; roster completo/evidencia OPEN |
| AB-02 RUL | SEMANTIC CROSSWALK RECONCILED | PREDICATE, owner/scope/AST/operands/effect; mapping y validación OPEN |
| AB-02 REF | OPEN | No declarar REF=0 sin inventario/cobertura exhaustivos |
| AB-02 MET/POL | PARTIALLY RESOLVED | MET reutiliza registros existentes; POL ausente por diseño; hash OPEN |
| M_F / M_A | SEMANTICALLY SPECIFIED | IDs/versiones y mappings materiales por etapa OPEN; independencia técnica no demostrada |

AB-01/02 no pasan a DONE ni habilitan Design Freeze, schema freeze, fixtures, parser, implementación o ejecución científica. scientific_execution=false; execution_authorized=false.


## 139. Gate de arquitectura A/B para C-Value — DEC-C10-095 (2026-11-11)

| Área | Estado | Criterio / límite |
|---|---|---|
| Arquitectura A/B | ACCEPTED — DESIGN ARCHITECTURE | A permanece base inalterada; B autorizada como extensión DGP separada y versionada |
| A / Value | NOT INSTANTIATED | No atribuir ΔT_acc→Value en A; no inferir beneficiario, preferencias ni medidas |
| B / especificación | OPEN — DOCUMENTARY DESIGN | Rol, relación servicio-unidad, demanda pre-Z, perspectiva, criterio, vector, DAG, medición, horizonte, interferencia y parámetros requieren especificación/aceptación |
| P179 | KEEP | Value vectorial y trade-offs; sin escalar/pesos por defecto |
| P182/P183 | KEEP | Contratos transversales de medición, error, invariancia, ausencia, censura e identificación |
| Paquete C | IN PROGRESS | Separar Outcome técnico A de Value sintético B; §224 pendiente |
| Paquete D | BLOCKED ON SEMANTIC CONTRACTS | Consumir A/B versionados; separar truth del generador, evidencia observada y salida Analyzer; no schema inferido |
| Paquete E | BLOCKED ON C/D ACCEPTANCE | No integración confirmatoria hasta contratos, estimandos, medición y provenance cerrados |
| MED-02 / MED-03 | OPEN | Esta aceptación no los cierra |
| Design Freeze / implementación / ejecución | NOT AUTHORIZED | scientific_execution=false; execution_authorized=false |

**Nota histórica supersedida (2026-11-11):** la lectura Contents devolvía longitud 0, pero el blob Git se recuperó íntegramente; el maestro recibió §274. La propagación al maestro está verificada mediante fetch_blob, aunque fetch_file/Contents siga devolviendo vacío por limitación de lectura. Nota histórica supersedida: DEC-C10-095, Decision Log, plan, matriz Value y reconciliación §§266–274 constan en esta rama; el maestro se verificó mediante blob Git, no mediante Contents.


## 140. Gate B-BEN/B-VAL — C10S-B-VALUE-MIN-001 (2026-11-11)

| Elemento | Estado | Criterio |
|---|---|---|
| Contrato mínimo beneficiario/Value B | DRAFT / DOCUMENTARY | Requisitos de admisibilidad definidos; ninguna identidad o regla seleccionada |
| Tipo/identidad beneficiario | OPEN | Requiere estipulación versionada y relación explícita con unidad/servicio |
| Demanda/eligibilidad pre-Z | OPEN | Basal, ex ante y no equivalente a uso/selección |
| Consecuencia/perspectiva/autoridad | OPEN | Debe ser distinta de A/Reach/O técnico y fijada ex ante |
| Dimensiones/fichas V_j | OPEN | P179 vectorial; §224; P182/P183; no pesos por defecto |
| DAG/estimandos B | CANDIDATE | Vías alternativas y efecto paquete separados; no aprobación causal |
| Paquete C | IN PROGRESS | Cerrar semántica antes de indicadores |
| Paquete D | BLOCKED ON SEMANTIC CONTRACT | No schema físico/fixtures hasta cierre |
| Paquete E | BLOCKED ON C/D | Verificar invariantes y abstención/no identificación |
| MED-02/MED-03 | OPEN | No se cierran |
| Design Freeze/implementación/ejecución | NOT AUTHORIZED | scientific_execution=false; execution_authorized=false |

Véase C10S-B-VALUE-MIN-001. No modifica A, DEC-C10-068, roster A ni Core.


## 141. Gate B1 — Entidad solicitante sintética (2026-11-11)

| Elemento | Estado | Criterio |
|---|---|---|
| Tipo candidato B1 | ACCEPTED FOR DEVELOPMENT | Entidad solicitante sintética con necesidad/objetivo basal y consecuencia potencial valorable |
| Instancia/cardinalidad | OPEN | No identidad ni relación concreta estipulada todavía |
| Demanda pre-Z | OPEN | No equivale a solicitud emitida o uso |
| Solicitud | SEMANTICALLY DISTINGUISHED | No demuestra satisfacción ni valor |
| Consecuencia/Value | OPEN | Debe distinguirse de procesamiento técnico/O-CONF |
| Perspectiva/dimensiones/medición | OPEN | §224, P179/P182/P183 |
| C/D/E | IN PROGRESS / BLOCKED | C semántica; D representación tras cierre; E aceptación tras contratos |
| MED-02/MED-03 | OPEN | No se cierran |
| Design Freeze/implementación/ejecución | NOT AUTHORIZED | scientific_execution=false; execution_authorized=false |

Véase C10S-B1-REQUESTER-CANDIDATE-001. No modifica A, DEC-C10-068 ni el roster A.


## 142. Gate B1 — necesidad basal, elegibilidad de petición y solicitud (2026-11-11)

| Elemento | Estado | Criterio / límite |
|---|---|---|
| Need_preZ | SEMANTICALLY DISTINGUISHED / MEASUREMENT OPEN | Necesidad/objetivo del beneficiario en truth pre-Z; no se define por solicitud ni resultado |
| E_req_preZ | OPEN | Elegibilidad de petición; no equivale a E_i/P*_tau2 |
| Request_event | OPEN | Evento de petición; ventana/posición en reloj no resuelta |
| D_resource | EXISTING DGP CONSTRUCT | Demanda operativa de recursos/capacidad, distinta de necesidad del beneficiario |
| P*_tau2 / P*_F | PRESERVED | Poblaciones técnicas pre-Z; no se redefinen por B1 |
| Observación/missingness | OPEN | Truth 1/0/? separada de evidencia observada; no imputar ? a 0 |
| ITT/population | DESIGN RULE | No filtrar por Request_event ni otras variables post-Z |
| DGP clock/DAG | UNCHANGED | No ubicar petición en t5/t6/t7 sin reconciliación explícita |
| C/D/E, MED-02/03 | OPEN / IN PROGRESS | No se cierran por esta distinción |
| Freeze/implementación/ejecución | NOT AUTHORIZED | scientific_execution=false; execution_authorized=false |

Véanse C10S-B1-REQUESTER-CANDIDATE-001 §10, C10-S-POP-CMP-001 §10 y contrato temporal §14.


## 143. Gate B1 — ciclo de solicitud y relación con trayectoria (2026-11-11)

| Elemento | Estado | Criterio / límite |
|---|---|---|
| Request_opportunity / attempt / received | SEMANTICALLY DISTINGUISHED | Oportunidad, intento externo y recepción en servicio son eventos distintos |
| Admitted/rejected / processing / response | SEMANTICALLY DISTINGUISHED | Admisión, procesamiento y respuesta no son equivalentes |
| Request ↔ trajectory | OPEN | Cardinalidad y causalidad 0:1/1:1/1:N no decididas |
| Relación con t5/t6/t7 | NOT EQUIVALENT | Consideración, selección/inicio y ejecución transformacional no son estados de petición |
| Subledger / timestamps | PROPOSED | Sin nuevo reloj ni profundidad H |
| Carga estandarizada por harness | RECOMMENDED / NOT ACCEPTED | Probe de carga, no demanda natural; aceptación pendiente |
| Envío endógeno | ADVERSARIAL / SECONDARY CANDIDATE | No condicionar ITT ni población por envío post-Z |
| Consecuencia / Value | OPEN | No inferir desde respuesta técnica |
| Design Freeze / implementación / ejecución | NOT AUTHORIZED | scientific_execution=false; execution_authorized=false |

Véanse B1 spec §11, DGP temporal §15, arquitectura causal §14 y contrato funcional §12.


## 144. Gate B1 — decisión de modalidad de petición aceptada

## Decisión DEC-C10S-B1-REQUEST-MODE-001 — modalidad de oportunidades estandarizadas y envío endógeno (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta la arquitectura de dos modalidades para C10-S:
1. **Modalidad primaria candidata:** oportunidades/peticiones estandarizadas, definidas ex ante antes de Z y presentadas mediante harness externo idéntico entre brazos después del snapshot de accesibilidad t3/t4. El harness registra Request_attempt aunque el servicio no reciba la petición. Esta modalidad permite comparar respuesta/capacidad bajo una carga de prueba común.
2. **Modalidad secundaria/adversarial:** envío endógeno de solicitudes, cuya ocurrencia puede depender de conocimiento, expectativas, accesibilidad percibida y otros estados post-Z. Se conserva para estudiar selección y vías causales, no para definir la población primaria ni filtrar el ITT.

**Límites de la aceptación.** La carga estandarizada es un probe experimental de servicio; no representa por sí sola demanda natural, preferencia revelada, beneficiario confirmado ni Value. Se mantienen separados intento, recepción, admisión/rechazo, procesamiento, respuesta, consecuencia del beneficiario, Outcome técnico y Value. Los eventos post-Z no se usan como criterio de inclusión o exclusión del ITT. Se conserva el reloj t−1/t0…t9 y no se equiparan eventos de petición con t5/t6/t7 ni con H.

**Pendiente de especificación:** calendario y ventana de presentación; unidad y cardinalidad de oportunidades; identidad y vínculo request_id↔trajectory_id; payload y reglas de admisión; repetición, timeout y errores; tratamiento de solicitudes no recibidas/pendientes; outcome técnico de respuesta; medida independiente de consecuencia B1 y su horizonte; población y soporte; relación exacta con los estimandos ITT/mediación. La modalidad secundaria no recibe estimando confirmatorio por esta decisión.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen scientific_execution=false y execution_authorized=false. No altera DEC-C10-066/067, D2 primario candidato/D1 secundario ni la rama base de PR #116.


## B1-UNIT-001 — control de cierre y dependencias (2026-11-11)

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

## DEC-C10S-D2-ESTIMAND-SEPARATION-001 — nuevo control de arquitectura de estimandos (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se registra la separación D2 en cinco carriles: C1 ITT/efecto total de asignación; C2 primeras etapas independientes `C_dep*`, `A_f*`, `D_f*`, `ΔT_acc*`; C3 efecto focal de accesibilidad bajo mapping B→g, q común y soporte; C4 mediación interventional vía `ΔT_acc*` con Reach/trayectoria como mediadores secuenciales o bloque explícito; C5 contribución mecanística petición–trayectoria con contrafactuales de etapa y truth DGP segregada. No residual por resta automática; ITT incluye vías de política/paquete; no inferencia de Value desde trayectoria; no selección ITT post-Z; reloj t−1/t0…t9 y H inalterados. P179 vectorial; P182/P183 transversales OPEN.

**Criterio de cierre pendiente:** formalizar para cada carril población, unidad/interferencia, intervención/versiones, resultado/horizonte, contrafactual, soporte, medición, supuestos de identificación, sensibilidad y conclusión permitida; para C4 resolver confusión mediador–resultado inducida por Z; para C5 especificar propiedades relevantes y mecanismos de no transición. Esta decisión no cierra MED-02/MED-03, P177/P178/P179/P182/P183 ni los gates de Outcome/Value.

No autoriza freeze, implementación, fixtures, simulación o ejecución. `scientific_execution=false`; `execution_authorized=false`. Registro autónomo: `DEC-C10S-D2-ESTIMAND-SEPARATION-001.md`.


## 16. — Secuencia de cierre y gate activo C1 (2026-11-11)

Se incorpora como referencia operativa `C10_S_CLOSURE_SEQUENCE_AND_C1_ITT_WORKPLAN_001.md`. Orden obligatorio: C1 ITT D2 → Outcome/Value → C2 primeras etapas → C3 accesibilidad → C4 mediación → C5/DGP → estadística/Analyzer → contrato integrado de implementación. La secuencia evita reabrir decisiones aceptadas y exige un entregable verificable por paquete.

**Gate activo C1.1:** reconciliar población y elegibilidad pre-Z, UE/interferencia, brazos/versiones D2, Outcome/Value y horizonte, reutilizando POP-CMP-001, C10D1/S4R estimand reconciliation, DGP temporal/roles, matriz Value y contrato B. C1 es ITT por asignación a B_g0^D2/B_g1^D2, conserva vías colaterales y no se interpreta como efecto focal de accesibilidad sin C3. Resultado técnico en variante A y Value contextual en variante B no se presumen intercambiables ni ya instanciados. No excluir por eventos post-Z.

**Estado:** SECUENCIA DOCUMENTADA; C1.1 OPEN. No se modifica main ni se autoriza freeze, schemas físicos, fixtures, implementación, simulación o ejecución. `scientific_execution=false`; `execution_authorized=false`.


## C1.1 — Reconciliación ITT D2 (2026-11-11)

**Registro:** `C10_S_C1_ITT_D2_RECONCILIATION_DRAFT_001.md`.

**Dictamen:** C1 OPEN. D2 como asignación a B_g0^D2/B_g1^D2 está definido por decisiones aceptadas, pero el estimando completo no está cerrado. `P*_{τ2}` permanece candidato, `P*_F` no es población primaria por defecto; UE=UA está condicionada a aislamiento/no interferencia; A carece de Outcome operacionalizado y B carece de Value instanciado; H=3 no es horizonte temporal.

**Siguiente gate:** C1.2 — cerrar composición de elegibilidad basal `E_i`, predicados constitutivos y evidencia/indeterminación, y recuperar contrato de aleatorización D2. No freeze ni ejecución.


## C1.2 — Elegibilidad basal y asignación D2 (2026-11-11)

**Registro:** §12 de `C10_S_C1_ITT_D2_RECONCILIATION_DRAFT_001.md`.

La fórmula histórica de `E_i` que agregaba `C_other` queda retirada como regla operativa; `C_auth,base=1` es común/invariante D2; `C_dep,0=0` no sustituye `A_f,0*=0); `E_req_preZ` no es elegibilidad experimental. No se ha encontrado ratio/probabilidades, estratos, algoritmo/semilla ni reglas de desviación de la asignación en los contratos revisados.

**Recomendación pendiente de confirmación:** `P*_{τ2}` población primaria candidata C1; `P*_F` subpoblación secundaria. Composición `E_i`, clasificación y soporte OPEN. C1 no está cerrado.


## C1.3 — Precedencia poblacional aceptada; composición E_i activa (2026-11-11)

**Decisión:** `DEC-C10S-C1-POPULATION-PRECEDENCE-001` — ACCEPTED AS DESIGN-ARCHITECTURE DECISION / NOT DESIGN-FROZEN.

P*τ2 se acepta como población objetivo primaria candidata C1; P*F como subpoblación secundaria para apertura funcional exclusiva. La alternativa basal no excluye de P*τ2. La pregunta de precedencia queda resuelta y no se vuelve a solicitar.

**Gate activo C1.3:** reconstruir E_i desde DGP/IAM y predicados constitutivos vigentes, sin fórmula histórica C_other y sin confundir validez de instancia, aplicabilidad τ2, inaccesibilidad A_f basal, Need_preZ o E_req_preZ. OPEN: composición material, evidencia, indeterminación, soporte, medición, interferencia, asignación, horizonte y resultados.


## C1.4 — Crosswalk material de E_i (activo)

**Base documental:** `C10_S_C1_BASELINE_ELIGIBILITY_CROSSWALK_DRAFT_001.md`.

C1.3 no cierra E_i. Propuesta candidata `E_scope∧App*(τ2,S0)`, no aceptada. La validez abstracta de la instancia DGP y la aplicabilidad de τ2 no son accesibilidad focal. CMP≥1/PAR≥1/RUL≥1 y roster mínimo de servicio no prueban roster completo ni pertenencia P* por UE.

**Gate C1.4:** crosswalk de cada predicado/registro IAM pre-Z de `C_SRC` con App, C_dep y A_f; clasificar boundary, obligatoriedad, aplicabilidad, papel, evidencia, estado 1/0/?/NA y regla de adjudicación. Si IAM material no existe, registrar vacíos y bloqueos; no materializarlo ni declarar E_i cerrada.


## C1.5 — Aplicabilidad, E_scope y asignación (activo)

**Registro:** `C10_S_C1_PREZ_IAM_CROSSWALK_C10S_001.md`.

C1.4: PARTIAL / MATERIAL BLOCKED BY ABSENT IAM AND SNAPSHOTS. No hay snapshots C10-S observados ni IAM/coverage por UE. `E_i=E_scope∧App*(τ2,S0)` sigue propuesta no aceptada; no clasificar unidades ni declarar REF=0.

**Gate C1.5:** cerrar definición de `App*(τ2,S0)` y frontera con A_f; decidir rol de E_scope (alcance DGP vs elegibilidad confirmatoria) y selección; regla pre-Z de unknowns; recuperar asignación D2 y dictaminar soporte/factibilidad. P*τ2/P*F ya aceptadas en precedencia; no pedir reconfirmación.


## PAQUETES INTEGRADOS — control de ciclo único (2026-11-11)

**Protocolo rector:** `C10_S_INTEGRATED_WORK_PACKAGES_AND_CYCLE_PROTOCOL_DRAFT_001.md`.

La unidad de trabajo es el paquete completo, resuelto en una única iteración/conversación. No se abrirán subgates conversacionales ni se solicitarán confirmaciones redundantes. Cada ciclo debe reconciliar fuentes y decisiones históricas, producir síntesis integrada, clasificar decisiones/bloqueos, persistir cambios coherentes y releer/verificar los artefactos modificados.

| Paquete | Alcance integrado | Salida exigida | Estado |
|---|---|---|---|
| PA | C1: población, E_i/App/E_scope/unknowns, unidad, asignación D2, ITT, comparador, interferencia/soporte, horizonte, Outcome, consecuencia B1 y Value | Contrato C1 o bloqueo material explícito y delimitado | CICLO COMPLETADO DOCUMENTALMENTE; BLOQUEOS MATERIALES |
| PB | D2 material, B1/servicio, provisión/instalación/dependencias, petición, request↔trajectory, C_dep/A_f/D_f/ΔT_acc y snapshots | Contrato D2/C2 o límites de factibilidad | CICLO COMPLETADO DOCUMENTALMENTE; BLOQUEOS MATERIALES + 1 DECISIÓN PENDIENTE |
| PC | C3/C4: estimando de accesibilidad, q/soporte, DAG, vías alternativas/interacciones, mediación interventional, sensibilidad | Contrato de atribución/mediación e identificación/no-identificación | CICLO COMPLETADO DOCUMENTALMENTE; C3/C4 NO IDENTIFICADOS EN D2 MATERIAL |
| PD | DGP truth/observed, C5, contrafactuales por etapa, alternativas/colaterales, P177–P183, medición/missingness/potencia y adversariales | DGP y contrato de evaluación trazables | SIGUIENTE PAQUETE ACTIVO |
| PE | schemas, interfaces Generator–Analyzer–Evaluator, IDs/eventos/snapshots/provenance, fixtures/oráculos/tests/manifests | Especificación técnica implementable y autorización separada | BLOQUEADO HASTA CIERRE CIENTÍFICO Y AUTORIZACIÓN |

**Regla de cierre:** una iteración completa no fuerza un PASS. Ausencia de IAM, snapshots, asignación, evidencia, Outcomes o regla de Value se registra como BLOCKED/NOT_VERIFIABLE con impacto y requisito mínimo para levantarlo. Las decisiones aceptadas no se reabren salvo contradicción material documentada. No se crean nuevos documentos si basta actualizar el maestro o contrato rector.

**Estado y límites:** PA activo. P*_{τ2}/P*_F ya aceptadas; no solicitar reconfirmación. El crosswalk IAM/C_SRC registra ausencia de filas IAM y snapshots observados; no clasificar unidades ni declarar REF=0. `scientific_execution=false`; `execution_authorized=false`; no código/fixtures/simulación/ejecución autorizados.


## PA — resultado del ciclo integral (2026-11-11)

**Dictamen:** `PA_RECONCILED_DOCUMENTALLY / C1_MATERIAL_BLOCKED / NOT_DESIGN_FROZEN`. Registro integrado: §15 de `C10_S_C1_ITT_D2_RECONCILIATION_DRAFT_001.md`; propagación en §16.155 del plan.

| Subdominio | Resultado de reconciliación | Bloqueo residual |
|---|---|---|
| D2/C1 | Efecto total de asignación a política D2; familia de ITT por variante/resultado/horizonte | Aleatorización material y versiones/entrega |
| Población | Precedencia P*τ2 primaria candidata y P*_F secundaria ya aceptada | E_i/IAM/snapshots y soporte |
| Unknowns | 1/0/?/NA; truth y observado separados; no exclusión silenciosa | Protocolo confirmatorio pre-Z para indeterminados |
| Unidad/interferencia | UE/UA/UO separados; B1 y una oportunidad/UE ya aceptadas | Aislamiento material o clúster/exposición |
| Horizonte | H=3 profundidad, no duración; reloj t−1/t0…t9 intacto | Ventanas y horizonte por Outcome/Value |
| Outcome A | O-CONF mejor anclado, no operacionalizado | Ficha §224, oráculo, tolerancias y evidencia |
| Value B | Vector P179 preservado; no dimensión ni beneficiario concretos asumidos | Instancia B1, consecuencia, perspectiva, V_j y medición |
| Identificación C1 | No adjudicable con la especificación material disponible | Asignación, consistencia, soporte, interferencia, medición y missingness |

No surgió una decisión nueva que requiera aprobación del usuario: las lagunas son materiales y no preferencias. No se reabren DEC-C10-066/067 ni DEC-C10S-C1-POPULATION-PRECEDENCE-001.

**Estado del control:** el ciclo PA está completado documentalmente; C1 permanece OPEN/BLOCKED en lo material. Siguiente paquete: **PB**. PA solo se reabrirá para incorporar evidencia/contratos materiales nuevos.


## PB — resultado del ciclo integral (2026-11-11)

**Dictamen:** PB_RECONCILED_DOCUMENTALLY / D2_C2_MATERIAL_BLOCKED / NOT_DESIGN_FROZEN. Registro: maestro C10-S §267.

| Subdominio | Resultado | Bloqueo |
|---|---|---|
| D2 B_g0/B_g1 | Contrato conceptual aceptado; no reabrir | Entrega material, versiones, actor, crossover y provisión de fondo |
| Servicio lógico B1 | DEC-C10-068/069 aceptadas | Identidad de instancia por UE vs instancia ejemplar |
| P0/P1/P2 | Frontera conceptual reconciliada; B focal en P1 | Inventario material B-M01…15 ausente |
| C_dep* | C_install∧C_integrity∧C_compat∧C_oper | Sin instalación ni verificación material |
| A_f* | Fórmula candidata depurada §67.3; sin duplicidad conceptual | Mapping y evidencia de REL/COND/AUTH/RES/DEP/BLOCK y alternativas |
| C2 | Vector W_programmed/W_attempt/S_install/C_dep/A_f/D_f/ΔT_acc | Primera etapa no establecida; s=.80 no validado |
| Snapshots | t−1/t0…t4 y S_T*/E_T/ΔT_T separados | IAM, snapshots materiales y UG-SCH-10 no cerrados |
| Aislamiento | Requisito explícito por UE | No verificado; recursos/servicios compartidos y carryover sin inventario |
| Petición B1 | Una oportunidad/UE después de t3/t4 | Payload, calendario, timeout/retries, estados y adjudicación |
| IV | D_f* verdadero distinto de D_f_obs | Medición/error/missingness abiertos; Wald/LATE bloqueado |

**Decisión pendiente:** instancia lógica de servicio única/versionada por UE, compartiendo contrato/versión y plantilla CMP; la ID DEC-C10-069 se conserva como instancia ejemplar, no se replica como ID de todas las UE. Recomendación favorable para mantener aislamiento aceptado. Requiere aceptación expresa antes de congelar. El resto son bloqueos materiales o de operacionalización.

PB completado documentalmente; siguiente paquete activo **PC**. No implementación ni ejecución autorizadas.


## PC — resultado del ciclo integral (2026-11-11)

**Dictamen:** PC_RECONCILED_DOCUMENTALLY / C3_C4_NOT_IDENTIFIED_IN_CURRENT_D2_MATERIAL / NOT_DESIGN_FROZEN. Registro rector: maestro C10-S §268; plan §16.157.

| Subdominio | Resultado | Bloqueo decisivo |
|---|---|---|
| Jerarquía estimandos | C1/ITT, θ_A(q), θ_Af(q_X*), LATE_f y C4 separados | No transferir identificación entre ellos |
| C3 general | Pregunta g1/g0 sobre ΔT_acc* bajo q común | D2 focal no implementa ni identifica g1/g0 |
| C3 focal | θ_Af(q_X*) definido como objetivo candidato | Mapping B_D2→g^Af, q_X*, soporte y vías colaterales abiertos |
| DAG | Vía transformacional y vías paralelas integradas | Inventario material B-M01…15 y aislamiento ausentes |
| C4 | Mediación interventional sobre ΔT_acc*; Reach/Π secuenciales o bloque explícito | Intervención mediadora, confusión post-Z y soporte longitudinal no cerrados |
| Outcome/Value | O-CONF candidato; Value vectorial preservado | Sin ficha O completa, V_j, beneficiario, perspectiva ni regla |
| Residual/directo | No se deriva por resta | Descomposición formal no definida |
| P177/P178/P179/P182/P183 | Reutilizados; DAG/CAUS existentes no duplicados | C-MED PARCIAL/OPEN; fixtures/tolerancias no ejecutados |
| Identificación actual | C3/C4 Value NOT IDENTIFIED/NOT EVALUABLE | Faltan contratos y evidencia material |

PC queda completado documentalmente; no se declara θ_A, θ_Af, IIE ni Value identificados. Siguiente paquete activo: **PD — DGP, mecanismos C5 y evaluación adversarial**. No implementación ni ejecución autorizadas.


## PD — resultado del ciclo integral (2026-11-11)

**Dictamen:** PD_RECONCILED_DOCUMENTALLY / DGP_QUANTITATIVE_SPECIFICATION_OPEN / NOT_DESIGN_FROZEN. Registro rector: C10_S_PD_DGP_MECHANISM_AND_ADVERSARIAL_EVALUATION_RECONCILIATION_DRAFT_001.md; plan §16.158; protocolo de paquetes §11.

| Subdominio | Resultado | Bloqueo decisivo |
|---|---|---|
| DGP integrado | Cadena temporal, potenciales, estados estructurales y consecuencias separados | Distribuciones conjuntas, parámetros, reglas y versiones no cerrados |
| Mecanismos C5 | Contrafactuales por etapa y clases necessary/enabling/modifying preservadas | Contrastes D2 concretos, propiedad relevante, soporte y causas concurrentes abiertos |
| Enlaces petición–trayectoria | Temporal, trazabilidad y contribución causal no intercambiables | Cardinalidades secundarias y evidencia observable por escenario abiertas |
| Truth/evidence/evaluation | Tres planos segregados; Analyzer sin truth; Evaluator compara tras sellado | Contrato técnico/roles y verificación computacional pendientes |
| Escenarios adversariales | Nulo, adverso, vías directas/colaterales, interacción, heterogeneidad, IV, interferencia, alternativas, medición, missingness y censura cubiertos documentalmente | Fixtures, parámetros y tolerancias no implementados |
| P177/P178/P179/P182/P183 | Reutilizados sin duplicar IDs | N/R, potencia, precisión, SE_MC y Value requieren cierre cuantitativo/material |
| Value/Outcome | Límites de PA preservados | Value no instanciado; Outcome no operacionalizado |
| Estado | Reconciliación documental cerrada | Maestro C10-S no recuperado íntegramente en esta sesión; no se declara propagación al maestro |

PD no está congelado, implementado ni ejecutado. No se autoriza código, fixtures confirmatorios, simulación, estimación ni ejecución científica. Siguiente paquete: **PE**, con preparación conceptual solamente y condicionado a los bloqueos científicos/materiales y a la recuperación del maestro. No se modifica main.


## PE — resultado del ciclo integral (2026-11-11)

**Dictamen:** PE_RECONCILED_DOCUMENTALLY / TECHNICAL_CONTRACT_PARTIAL / IMPLEMENTATION_NOT_READY / NOT_IMPLEMENTED / NOT_EXECUTED. Artefacto rector: C10_S_PE_INTEGRATED_TECHNICAL_SPECIFICATION_AND_IMPLEMENTATION_CONTRACT_DRAFT_001.md; maestro §270; plan §16.159; protocolo de paquetes §12.

| Subdominio | Resultado | Bloqueo decisivo |
|---|---|---|
| Arquitectura de roles | Responsabilidades lógicas Generator/Proyector-Sealer/Analyzer/Evaluator/Orquestador/Store reconciliadas | Permisos, almacenamiento y canales laterales no probados |
| Contratos de datos | Reutilizados DGP temporal/roles, U_G, identidades y registros de evidencia | Esquema físico, formatos y cardinalidades no congelados |
| Identidad/versionado | DEC-065/069/076/079 y contratos U_G preservados | Crosswalk completo y constraints ejecutables pendientes |
| Temporalidad | t−1/t0…t9, stage_key, SNAPSHOT.phase y step_k/H separados | Contrato físico de eventos/orden/timestamps abierto |
| Canonicalización | JCS aplicado solo a UDG-01/U1 | Otros bundles y registros sin perfil aprobado |
| Truth firewall | Contrato lógico definido | SR-13 CONDITIONAL; seguridad/custodia SR-19 NOT_ASSESSED |
| Validación | Pipeline V0–V8 definido; IDs existentes reutilizados | SR-20 NOT_ASSESSED; no parser/tests/replay |
| Preparación científica | Bloqueos PA–PD conservados | Value/Outcome, IAM/snapshots, mapping, soporte, parámetros y potencia |
| Autorización | No otorgada | G-SCI/G-MAT/G-SCHEMA/G-ROLE/G-TEST/G-REPRO/G-AUTH pendientes |

No se crea una decisión científica nueva. No se autoriza implementación, fixtures confirmatorios, datos, simulación, estimación ni ejecución. main/Core/RMA/Matrix/STATUS/claims permanecen fuera de alcance.


## Decisión PB aceptada — identidad de servicio por UE (2026-11-11)

**Decisión:** `DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001` — ACCEPTED.

| Elemento | Regla aceptada | Pendiente residual |
|---|---|---|
| Contrato funcional | `C10S-SVC-REQUEST-PROCESSOR` v`1.0.0`, común | Cambios semánticos futuros y versionado contractual |
| Plantilla CMP/PAR/RUL | Común, versionada por contrato | Roster/manifest concreto |
| Instancia | `instance_id` único por UE | Asignación al roster final |
| Versión de instancia | Monotónica e independiente por `instance_id` | Registro material de revisiones |
| Componente | `component_id` local; clave `(instance_id, component_id)` | Constraints y referencias ejecutables |
| Instancia DEC-C10-069 | Referencia ejemplar preservada | No reutilizar como ID común de UE |
| Aislamiento | Requisito lógico explícito | IAM/ACL, estado, recursos, infraestructura y pruebas siguen OPEN |

El cierre es de identidad lógica/documental. No demuestra aislamiento real, ausencia de interferencia ni independencia de recursos. No autoriza implementación o ejecución.


## PB-MAT — reconciliación material D2 e identidad B1 (2026-11-11)

**Artefacto rector:** `C10_S_PB_MATERIAL_D2_INSTANCE_AND_ISOLATION_RECONCILIATION_DRAFT_001.md`. **Dictamen:** PB_MATERIAL_CONTRACT_RECONCILED_DOCUMENTALLY / MATERIAL_INVENTORY_NONE / ISOLATION_NOT_DEMONSTRATED.

| Control | Resultado documental | Estado material |
|---|---|---|
| Identidad de servicio | Contrato/plantilla común; instancia única por UE; adaptador P1 separado | IDs/roster por UE OPEN |
| P0/P1/P2 | D2 focal en P1; P0 y alternativas invariantes por requisito; P2 transversal | Requiere snapshots y evidencia |
| IAM/C_SRC | Reutiliza U_G, boundary_class y FKs exactas | NONE; C1.4 bloqueado |
| B-M01…15 | Catálogo y vías tipadas reutilizados | M01–12/M15 no inventariados; M13/M14 prohibidos como cambios |
| Grafo/dependencias | Directas, transitivas, consumidores y externos requeridos | No materializado |
| Recursos/ACL | No reducción de alternativas; ACL técnicas no alteran C_auth | No medido/probado |
| A1/A2 | No-afectación funcional con margen ex ante | No probado; PROV-05/09 OPEN |
| C_dep/A_f/D_f | Constructos separados y evidencia independiente | No observados; C2 material bloqueado |
| D2 operativo | Actor, artefacto, recepción, ventana, reintentos, crossover | OPEN según DEC-C10-067 |
| Interferencia/soporte | UE/UA/UO, clúster y exposición a recursos compartidos | OPEN |

No se declara MD-C1/MD-C4, G-MAT, aislamiento, primera etapa focal ni IV. No captura, implementación o ejecución autorizada.

## B2–B3 — reconciliación de beneficiario, Outcome y Value (2026-11-11)

**Artefacto rector:** `C10_S_B2_B3_BENEFICIARY_OUTCOME_VALUE_RECONCILIATION_DRAFT_001.md`. **Dictamen:** B2_B3_WORKING_BASIS_ACCEPTED / SEMANTIC_RECONCILIATION_DOCUMENTED / OUTCOME_NOT_OPERATIONALIZED / VALUE_NOT_INSTANTIATED.

| Control | Resultado documental | Estado pendiente |
|---|---|---|
| B1/Need_preZ | B1 como entidad solicitante-beneficiaria; Need_preZ basal separado de uso/solicitud | Contenido, observabilidad y ficha material OPEN |
| Identidad B1 | Una B1 por UE; servicio lógico único/versionado por UE | Roster/IDs y aislamiento material OPEN |
| Outcome | Resultado técnico separado de proceso/accesibilidad/Value | O-CONF mejor anclado; ficha §224 incompleta; otros O_k OPEN |
| Consecuencia B1 | Cambio respecto de Need_preZ | Constructo/horizonte sin operacionalizar |
| Value | Valoración contextual de consecuencia desde perspectiva B1 | Perspectiva/autoridad y V_j no instanciadas |
| Causalidad | Outcome puede contribuir, no es causa exclusiva impuesta | Vías colaterales y DAG por resultado OPEN |
| Dimensionalidad | Vector P179 y trade-offs preservados | No dimensiones/pesos confirmatorios seleccionados |
| Medición | Fichas separadas por O_k y V_j; P182/P183 | Fuentes, escalas, error, ausencia/censura OPEN |
| Identificación | ITT Outcome y ITT Value separados | No transferencia; C3/C4 no identificados en D2 material actual |

No se declara Outcome/Value operacionalizado ni Design Freeze. No implementación, fixtures, simulación o ejecución autorizada.


## Reconciliación integrada de factibilidad confirmatoria — 2026-11-11

**Artefacto rector:** C10_S_INTEGRATED_CONFIRMATORY_FEASIBILITY_AND_DESIGN_FREEZE_RECONCILIATION_DRAFT_001.md.

| Control integrado | Dictamen | Evidencia/bloqueo decisivo |
|---|---|---|
| Asignación D2 | ARCHITECTURE ACCEPTED / MATERIAL OPEN | Faltan ratio/probabilidades, estratos, algoritmo/semilla, desviaciones y provenance |
| q_X*/q_L*, positividad y soporte | OPEN / NOT ASSESSED | No materializados por política, historia, población y resultado |
| UE/UA/UO | CONDITIONAL | UE=UA depende de aislamiento; UO no aumenta N independiente |
| Interferencia | NOT DEMONSTRATED | Roster, IAM, recursos/agentes/canales y grafo transitivo ausentes |
| IAM/C_SRC y snapshots | BLOCKED | NONE / no capturados; E_i y predicados basales no adjudicables |
| Provisión B / C_dep* | BLOCKED | B-M01…15 sin inventario; actor/artefacto/recepción/ventana/rollback OPEN |
| A_f*/D_f*/ΔT_acc* | NOT IDENTIFIED / NOT EVALUABLE | Sin evidencia material independiente ni snapshots comparables |
| Outcome O_k | NOT OPERATIONALIZED | O-CONF candidato; ninguna ficha §224 completa |
| Value V_j | NOT INSTANTIATED | B1/Need_preZ, perspectiva/autoridad, consecuencia, dimensiones y fichas incompletas |
| C1 ITT | NOT CONFIRMATORY / NOT IDENTIFIABLE NOW | Asignación, población material, Y_j y horizonte no cerrados |
| C2 primeras etapas | NOT ESTIMABLE NOW | No confundir C_dep* o s=.80 con apertura focal D_f* |
| C3 θ_A/θ_Af | NOT IDENTIFIED | Mapping D2→g^Af, q común, soporte y vías colaterales abiertos |
| LATE_f | NOT IDENTIFIED | IV/exclusión/monotonicidad/relevancia/no interferencia no demostrados |
| C4 IIE | NOT IDENTIFIED / NOT EVALUABLE | Intervención mediadora, confusión post-Z y soporte secuencial abiertos |
| Efecto directo/residual | NOT DEFINED / NOT IDENTIFIED | No se deriva por resta ad hoc |
| Cotas y sensibilidad | FUTURE OPTION ONLY | No hay cobertura, parámetros ni restricciones para cotas informativas actuales |
| Design Freeze | BLOCKED | G-SCI/G-MAT/G-SCHEMA/G-ROLE/G-TEST/G-REPRO bloqueados; G-AUTH no otorgado |
| Maestro C10-S | RECOVERED / §§266–274 + §274.1 PROPAGATED | Blob vigente `51dcd3b2c84d33c437292ce5883f5b70e3d9491c` verificado: 1,137,928 caracteres / 12,156 líneas; Contents devuelve vacío y no se usa para verificar |

No se autoriza captura, schema físico, fixtures, implementación, generación de datos, simulación, estimación o ejecución. scientific_execution=false; execution_authorized=false.

## Corrección de recuperación del maestro C10-S — 2026-11-11

La lectura inicial del maestro mediante Contents devolvía contenido vacío, pero el blob Git fue recuperado íntegramente (1,134,655 caracteres / 12,136 líneas) e inspeccionados sus §§266–273. La incidencia está **RESUELTA**; el documento no estaba perdido. Se ha añadido §274 al maestro con la reconciliación integrada de factibilidad y Design Freeze. No queda pendiente recuperar el maestro; permanecen los bloqueos científicos/materiales y los gates indicados en el artefacto rector. La limitación de concordancia línea por línea por inaccesibilidad del maestro queda superada para el contenido recuperado; no equivale a validación local ni CI.


## 141. Gate D2 — asignación, población y soporte (2026-11-11)

| Elemento | Estado | Criterio de cierre |
|---|---|---|
| Política D2 y programación W_programmed | ACCEPTED | DEC-C10-066/067; 0/1 condicional a Z |
| Aleatorización Z | OPEN / NOT SPECIFIED | UA, ratio, p_i por estrato, algoritmo, semilla/hash, provenance, desviaciones |
| Población P*τ2/P*_F | PRECEDENCE ACCEPTED | No reabrir; composición E_i y clasificación por unidad OPEN |
| App/E_scope/E_i | PARTIAL / OPEN | Mapping y truth pre-Z completos; no confundir con A_f/C_dep |
| UNKNOWN pre-Z | REQUIREMENT DEFINED / ANALYSIS OPEN | Resolver antes de Z o definir estimando observable/cotas/restricción ex ante |
| q_X* / positivity | OPEN / NOT MATERIALIZED | Distribución basal, pesos, cobertura y soporte de ambas políticas por historia |
| q_L* | CONDITIONAL / OPEN | Solo si historia secuencial post-Z es necesaria y está identificada |
| UE=UA / interference | CONDITIONAL / BLOCKED | Aislamiento demostrado o cluster/exposure model y estimando compatible |
| IAM/C_SRC/roster/snapshots | NONE / BLOCKED | Fuente aprobada, cobertura, versionado y provenance |
| Design Freeze / execution | BLOCKED / NOT AUTHORIZED | Gates conjuntos y autorización expresa |

El contrato detallado está en C10_S_D2_ASSIGNMENT_POPULATION_SUPPORT_RECONCILIATION_DRAFT_001.md. Este gate no autoriza captura, schema físico, fixtures, implementación, simulación, estimación o ejecución.


## 142. Gate de medición confirmatoria Outcome/Value (2026-11-11)

| Control | Estado | Criterio de cierre |
|---|---|---|
| Separación F* / O-CONF / Value | RECONCILED DOCUMENTALLY | F* criterio; O-CONF resultado adjudicado; Value consecuencia valorada B1 |
| O-CONF | PRIORITY CANDIDATE / OPEN | Predicados FP, mapping/IAM, C0/G/H, snapshots, evento terminal, oráculo independiente y ficha §224 |
| FP-08 | PROBATIVE GATE / OPEN | Provenance, cobertura, cegamiento, reproducibilidad; no mezclar con función |
| B1 / Need_preZ | SEMANTIC BASIS ACCEPTED | Contenido, medida y evidencia basal material OPEN |
| Perspectiva B1 | BASIS ACCEPTED | Autoridad y criterio de valoración en truth_dgp OPEN |
| Value vector P179 | PRESERVED | No reducir ni agregar por defecto |
| Dimensiones V_j / k | NOT SELECTED | Consecuencia, criterio, indicador, fuente, escala, baseline, horizonte y trade-offs por ficha §224 |
| P182/P183; MEAS/MISS | EXISTING CONTRACTS REUSED | Evidencia, parámetros y validación no ejecutados |
| ITT O vs ITT V | SEPARATE ESTIMANDS | No transferencia de identificación; población/asignación/soporte/medición OPEN |
| C3/C4 per O/V | NOT IDENTIFIED | DAG, intervención, soporte, vías colaterales y confusión longitudinal |
| Design Freeze / implementation | BLOCKED / NOT AUTHORIZED | Todos los gates conjuntos y autorización expresa |

Artefacto rector: `C10_S_OUTCOME_VALUE_OPERATIONALIZATION_RECONCILIATION_DRAFT_001.md`; maestro §276. No crea IDs de tests, dimensiones, escalas ni decisiones científicas.

## 143. Gate de caso de valoración B1 (2026-11-11)

| Control | Estado | Criterio de cierre |
|---|---|---|
| Caso contextual B1 | FRAMEWORK CANDIDATE / NOT INSTANTIATED | Operación basal focal nombrada y versionada; relación B1–UE–servicio explícita |
| Need_preZ | SEMANTIC FORMULATION CANDIDATE | Contenido concreto de la operación, estados 1/0/? y evidencia pre-Z |
| Consecuencia B1 | ENVELOPE CANDIDATE / NOT MEASURED | Consecuencia potencial definida respecto de Need_preZ, independiente de procesamiento/O-CONF |
| Probe estandarizado | DESIGN DECISION ACCEPTED | Una oportunidad/UE post-snapshot; no confundir con demanda natural ni Value |
| Perspectiva/autoridad | B1 BASIS ACCEPTED / AUTHORITY OPEN | Regla normativa ex ante, versionada y simétrica |
| V_j / fichas §224 | NOT SELECTED | Solo tras justificar constructo, fuente, unidad, escala, horizonte, validez y trade-offs |
| Horizonte | OPEN | Reconciliar con reloj t−1/t0…t9; no equiparar a H=3 |
| Materialización PB-MAT | BLOCKED | Roster, IAM/C_SRC, snapshots, manifiesto y aislamiento con evidencia aprobada |
| Design Freeze | BLOCKED / NOT AUTHORIZED | Cierre conjunto de G-SCI/G-MAT/G-TEST y autorización expresa |

Artefacto rector: `C10_S_B1_VALUATION_CASE_RECONCILIATION_DRAFT_001.md`. La envolvente de consecuencias no crea dimensiones ni tests.


## 144. Actualización tras aceptación de la clase de propósito basal B1 (2026-11-11)

| Control | Estado actualizado | Criterio pendiente |
|---|---|---|
| Propósito basal B1 | PURPOSE CLASS ACCEPTED | Nombrar y versionar la operación/función concreta dependiente de la configuración en destino |
| Need_preZ | STRUCTURE DEFINED / NOT MATERIALIZED | Clasificación truth 1/0/? por UE y evidencia basal pre-Z; no asignación automática |
| No circularidad | RULE DEFINED DOCUMENTALLY | Comprobar que Need_preZ no depende de Z, provisión, accesibilidad, petición, procesamiento, Outcome o ejecución |
| Consecuencia B1 | STRUCTURE DEFINED / NOT MEASURED | Consecuencia potencial respecto de la operación concreta; separar del proceso técnico/O-CONF |
| Población ITT | NO POST-Z FILTERING | No condicionar a oportunidad, Request_event, procesamiento, selección o ejecución |
| Value V_j | NOT SELECTED / NOT INSTANTIATED | Autoridad, criterio, dimensiones, fuente, escala, baseline, horizonte y fichas §224 |

Artefacto rector: `C10_S_B1_VALUATION_CASE_RECONCILIATION_DRAFT_001.md` §12. La aceptación no es instancia completa, no crea DEC ni autoriza roster, captura, schema, fixtures, implementación, simulación, estimación, Design Freeze o ejecución.

## 145. Resultado de reconstrucción histórica del servicio B1 (2026-11-11)

| Control | Resultado | Límite |
|---|---|---|
| Clase de servicio | RECOVERED: servicio lógico sintético de procesamiento de solicitudes (DEC-C10-068) | No define semántica de la solicitud |
| Configuración constitutiva | ENABLED BOOL, PROFILE ENUM y RUL-SVC-ENABLE-PROFILE-01 | Define habilitación/perfil, no operación de negocio |
| Operación concreta B1 | OPEN / NOT RECOVERED | Especificar tipo de solicitud, operación que realiza el servicio y dependencia de configuración destino |
| Need_preZ | PURPOSE CLASS ACCEPTED / NOT INSTANTIATED | No asignar truth 1/0/? por UE hasta especificar operación |
| Consecuencia B1 / Value | OPEN / NOT MEASURABLE | No derivar de F*, O-CONF, accesibilidad o ejecución |

Fuentes: DEC-C10-068/069, maestro §§174–178 y §216.2–216.3, contratos F* y servicio. Artefacto rector actualizado: C10_S_B1_VALUATION_CASE_RECONCILIATION_DRAFT_001.md §13 y maestro §279. No se inventa una operación ni se autoriza materialización o ejecución.
