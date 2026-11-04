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
| SRC-02 | C10-S | `C10_S_SYNTHETIC_EXPERIMENT_CONSOLIDATED_DRAFT_004.md`, PR #116, blob actual `2b7834c23ff690c8dc5379b02486a0693b32a632` | Documento consolidado hasta sección conversacional 164 (51 secciones documentales) | Draft, no aprobado |
| SRC-03 | Auditoría integrada | `C10_S_INTEGRATED_CONSISTENCY_AUDIT_DRAFT_001.md`, blob `d3ffa9ed0670764c339dc390423f435e6da0fc9b` | AUD-C10S-001…012 | Hallazgos abiertos |
| SRC-04 | Propuesta de resolución | `C10_S_AUD001_AUD002_RESOLUTION_DRAFT_001.md`, blob `5a3a2fa061fe146d9df9d4cdfbb803c5ee274d65` | Propuesta A_f, T_acc, ΔT_acc y DGP integrado | No aceptada |
| SRC-05 | Auditoría cruzada | `C10_S_AUD001_AUD002_CROSS_AUDIT_DRAFT_001.md`, blob `ce53c902fb39820e976eed5cb2a87e5eacace31c` | XAUD-001…007 | Hallazgos abiertos |
| SRC-06 | Informe de recuperación | `C10_S_RECOVERY_AND_TRACEABILITY_AUDIT_DRAFT_001.md`, blob `2f77832076773c67711f55a3c0d6680b69c2c6d9` | Reconstrucción de fuentes y límites hasta sección 183 | Recuperación parcial |
| SRC-07 | PR #115 | `research/c10-d1-protocol-draft` → PR #115 | 23 commits; 1 archivo; abierto Draft | Sin comentarios/revisiones |
| SRC-08 | PR #116 | `research/c10-s-consolidation-draft` → PR #116 | Ocho archivos modificados; el número de commits es dinámico; abierto Draft | Sin comentarios/revisiones registradas |

| SRC-09 | Reconciliación C10-D1 ↔ S4-R | `C10_S_C10D1_S4R_ESTIMAND_RECONCILIATION_DRAFT_001.md`, PR #116 | Jerarquía `θ_A(q)` / ITT_Z / LATE_f; propuesta para `p0` y poblaciones | Propuesta, no aprobada |
| SRC-10 | Decision log C10 | `C10_S_DECISION_LOG_DRAFT_001.md`, PR #116 | DEC-C10-001…010, decisiones abiertas y alternativas no admisibles | Registro inicial, no aprobado |

### 2.1 Resultado de la búsqueda de fuentes posteriores a 164

Se revisaron las fuentes canónicas de C10-D1 y C10-S en sus ramas, el PR #116 y sus archivos (ocho en el corte de esta actualización), el historial de comentarios/revisiones/hilos del PR (cero registros), y búsquedas de código en el repositorio para referencias distintivas de las secciones posteriores (incluidos P182-01 y P183-01). No se encontró en el repositorio una fuente íntegra adicional de las secciones conversacionales 165–183.

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
- Se separan DGP limpio (sin acceso en control, `p0=0`) y DGP adversarial de contaminación (`p0>0` con mecanismo explícito), preservando `C_dep,base=0`.

Estas son propuestas de armonización, no decisiones científicas aceptadas. La referencia completa, las fórmulas y reglas de salida están en el documento enlazado; no cerrar AUD/XAUD ni S4-R hasta revisión y decisión explícita.

## 5. Registro maestro de auditorías y bloqueos

### 5.1 AUD-C10S-001…012

| ID | Hallazgo | Estado | Criterio de aceptación mínimo |
|---|---|---|---|
| AUD-001 | A focal frente a ΔT_acc completo | ABIERTO; existe propuesta A_f | Definir A_f, T_acc y ΔT_acc en todo el DGP; mostrar qué cambia y qué no; ningún estimando focal presentado como efecto de todo ΔT_acc sin justificación |
| AUD-002 | Integración DGP causal-transformacional | ABIERTO; existe contrato propuesto | Una misma unidad atraviesa asignación, condiciones, accesibilidad, Reach/Π_H, selección, ejecución, O y V; verdad oculta sin filtración |
| AUD-003 | Contratos de pruebas no ejecutables | ABIERTO | Todas las pruebas del gate C10-S→C10-P tienen fixture, versión, entradas, verdad oculta, salida, aserciones, tolerancia, códigos y artefactos |
| AUD-004 | ΔT_acc relacional incompleto | ABIERTO | Formalizar ΔU, ΔR, ΔC, identidad/versionado, cambios de validez y estados indeterminados |
| AUD-005 | Reach_possible y trayectorias indeterminadas | ABIERTO | Lógica de tres estados, composición, deduplicación y reglas definite/possible |
| AUD-006 | S5-F sin DGP completo | ABIERTO | Ecuaciones generadoras, asignaciones, independencia, interacción y estimandos declarados |
| AUD-007 | S5-C verdad estructural vs identificabilidad | ABIERTO | Separar verdad DGP, soporte observado, estimando y conclusión permitida al analizador |
| AUD-008 | No circularidad de Value | ABIERTO | Pruebas metamórficas T_acc/O/Value; V_real y V_potential separados |
| AUD-009 | N y réplicas sin justificación de precisión/potencia | ABIERTO | Métricas de sesgo, cobertura, error Monte Carlo, precisión y justificación por escenario |
| AUD-010 | Diccionario variable×rol×tiempo | ABIERTO | Matriz completa generador/analizadores/evaluador por momento; truth fields protegidos |
| AUD-011 | Clasificación C_c frente a L | ABIERTO | Clasificar cada condición por papel causal y temporal; no por etiqueta nominal |
| AUD-012 | Decision log incompleto | ABIERTO | ID, decisión, alternativas, justificación, estado, orden/fecha, fuente y commit para cada decisión |

### 5.2 XAUD-001…007

| ID | Hallazgo | Estado | Criterio de aceptación mínimo |
|---|---|---|---|
| XAUD-001 | Coherencia del régimen q con políticas g | ABIERTO / CRÍTICO | Separar variables fijadas por q de las manipuladas por g, o definir régimen conjunto coherente; mostrar contrafactuales factibles |
| XAUD-002 | Intervención autónoma sobre A_f no demostrada | ABIERTO | Separar ITT de política habilitadora y efecto atribuible a accesibilidad; no llamarlo efecto puro si hay vías colaterales |
| XAUD-003 | Accesibilidad, aplicabilidad y ejecución | ABIERTO | Predicados separados Acc_f, App_f, Exec_f; ninguna implicación automática |
| XAUD-004 | Asignación, provisión, verdad y medición | ABIERTO | Z_A, C_auth, A_f*, A_f_obs, App_f, Exec_f y estados indeterminados distintos |
| XAUD-005 | Régimen E1 podría forzar ejecución inválida | ABIERTO | E1 selecciona/ejecuta solo trayectorias válidas; si no existe ruta, registra no ejecución/fallo sin saltarse precondiciones |
| XAUD-006 | Orden temporal y snapshots | ABIERTO | Snapshot basal, post-provisión, evaluación por rama, pre-ejecución y post-ejecución; reglas de actualización/versionado |
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
| P182-01…12 | Solo IDs y resumen de contenido | Recuperar texto fuente y las 12 fichas originales |
| P183-01…13 | Solo IDs y resumen de contenido | Recuperar texto fuente y las 13 fichas originales |

Ficha mínima común obligatoria:

`test_id, objective, fixture_version, unit_id, initial_state, inputs_by_role, hidden_truth, expected_output, assertions, tolerance, failure_codes, evidence_artifacts, reproducibility_hash`.

Los campos `hidden_truth` solo son accesibles al generador y al evaluador independiente; nunca al módulo cuya capacidad se evalúa. Cada prueba termina en PASS, FAIL o INDETERMINATE, con justificación y evidencia archivada.

## 8. XSYNC y revisión independiente

La información persistida identifica XSYNC-138-01 como formalmente abierto y XSYNC-138-02…10 como hallazgos que siguen abiertos salvo cierre explícito posterior. No se ha recuperado en esta auditoría el texto íntegro de cada hallazgo XSYNC ni un acta independiente de resolución.

Por tanto:
- no se presume el contenido específico de XSYNC-02…10;
- no se marcan como cerrados por inferencia;
- se requiere recuperar la fuente exacta que los define;
- se requiere una revisión independiente que compruebe la coherencia de DGP, variables, estimandos, contratos, reglas de no filtración y casos límite;
- la revisión debe registrar autor/rol, fecha, versión auditada, hallazgos, evidencia y resolución.

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
