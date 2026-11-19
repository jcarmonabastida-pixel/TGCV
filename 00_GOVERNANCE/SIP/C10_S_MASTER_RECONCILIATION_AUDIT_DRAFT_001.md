> **INVALIDADA / SUPERSEDIDA (2026-11-05).** Esta auditoría partió de una lectura incorrecta del maestro y afirmó erróneamente que faltaban §§131–163 y que §§165–183 no estaban integradas. La correspondencia correcta está documentada en el maestro: conversación 130→§16; 131–137→ §§17–24; 138–163→ §§25–50; 164→§51; 165–183→síntesis §52. No usar este documento para dirigir trabajo. La auditoría corregida es `C10_S_MASTER_RECONCILIATION_AUDIT_DRAFT_002.md`; el plan vigente es Draft 003.

---

# C10-S — Auditoría profunda de sincronización del maestro y reconciliación del diseño

**ID:** C10-S-MRA-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** AUDITORÍA DOCUMENTAL ASISTIDA / NO INDEPENDIENTE · ABIERTA  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116  
**Propósito:** establecer qué arquitectura y qué formulaciones están realmente persistidas, detectar brechas de sincronización y fijar la precedencia documental antes de seguir diseñando.

## 1. Dictamen ejecutivo

La revisión confirma una no conformidad documental: el maestro C10-S terminaba en §130 aunque existía material posterior desarrollado en conversación y recuperado en `Notes_261104_163033.docx` (secciones 164–183). El propio registro `C10_S_RECOVERY_165_183_SOURCE_REGISTER_DRAFT_001.md` declara que la copia íntegra y la transcripción literal completa no estaban incorporadas a GitHub, y que la reconciliación con Decision Log y Test Register seguía en curso.

En consecuencia, no era correcto afirmar que el maestro recogía toda la evolución ni utilizar el plan anterior como hoja de ruta normativa. Se ha añadido al maestro §§131–132 para registrar esta brecha y establecer el gate de recuperación. Esto no equivale a integrar el contenido perdido ni cierra la auditoría.

## 2. Fuentes examinadas

| Artefacto | Función | Resultado de auditoría |
|---|---|---|
| `C10_S_SYNTHETIC_EXPERIMENT_CONSOLIDATED_DRAFT_004.md` | Maestro C10-S | Llegaba a §130; ahora incorpora §§131–132 de auditoría de sincronización y regla de recuperación |
| `C10_S_DECISION_LOG_DRAFT_001.md` | Registro de decisiones | Contiene propuestas desde §7 y decisiones aceptadas DEC-C10-051…065; no todas las propuestas equivalen a decisiones |
| `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md` | Contrato causal/DGP/roles | Integra B, q_X*, unidad/interferencia, medición de A_f*/D_f*/ΔT_acc*, escenarios, U_G; conserva secciones candidatas y abiertas |
| `C10_S_CLOSURE_CONTROL_MATRIX_DRAFT_001.md` | Matriz de cierre | Contiene seguimiento de bloques y gate científico sin revisión externa; requiere normalizar numeración repetida y estados |
| `C10_S_TEST_CONTRACT_REGISTER_DRAFT_001.md` | Contratos de aceptación | Catálogo propuesto; no ejecutado; debe reconciliarse con P181/P182/P183 y DGP |
| `C10_S_C10D1_S4R_ESTIMAND_RECONCILIATION_DRAFT_001.md` | Reconciliación de estimandos | ITT de política, LATE focal y θ_A(q) general son objetos distintos; selección D1/D2 y atribución siguen abiertas |
| `C10_S_RECOVERY_165_183_SOURCE_REGISTER_DRAFT_001.md` | Registro de recuperación | Reconoce §§165–183 como fuente recuperada no integrada por completo |
| `C10_S_RECOVERY_AND_TRACEABILITY_AUDIT_DRAFT_001.md` | Recuperación histórica | Mantiene recuperación e integración en curso; no declara freeze ni ejecución |
| `C10_S_INTEGRATED_CONSISTENCY_AUDIT_DRAFT_001.md` | Auditoría de consistencia | Dictamen de revisión mayor abierta |
| `C10_S_INTEGRATED_RECONCILIATION_AUDIT_DRAFT_001.md` | Auditoría causal-transformacional | Propuesta de armonización, no decisión científica |
| `C10_S_DESIGN_CLOSURE_AND_OPERATIONALIZATION_PLAN_DRAFT_001.md` | Plan anterior | Conserva secuencias/terminología anteriores y no integra de forma suficiente la evolución posterior |
| `PR #116` | Envolvente de cambios | Descripción desactualizada: declara cobertura hasta §164 y solo detalla incrementos hasta §69, mientras el maestro actual llega a §132 tras la auditoría |

## 3. Precedencia que debe regir la reconciliación

1. Operativa de gobernanza de `main` y estado canónico, para proceso y límites.
2. Decisiones explícitamente aceptadas y registradas en Decision Log y artefacto propio.
3. Maestro C10-S como integración normativa de la arquitectura y sus cambios.
4. Contratos especializados (DGP, estimandos, U_G, pruebas), que deben ser coherentes con el maestro y enlazados.
5. Auditorías y matrices de control, como detección de discrepancias; no crean decisiones por sí mismas.
6. Fuente conversacional/DOCX recuperada: evidencia histórica de formulaciones y propuestas, no fuente de aprobación automática.
7. Plan: documento derivado; nunca puede prevalecer sobre una decisión aceptada o el maestro.

Si dos fuentes discrepan, no elegir la formulación más reciente por fecha solamente: identificar decisión, estado, procedencia, compatibilidad y si hubo sustitución explícita.

## 4. Arquitectura de diseño que debe conservarse

### 4.1 Microdominio y unidad lógica

- Opción A: migración de configuración entre entornos software, seleccionada en DEC-C10-051.
- Unidad lógica de servicio identificada por contrato funcional y contrato de configuración versionado; no equivale automáticamente a proceso, microservicio, binario o despliegue (DEC-C10-058).
- Objeto de configuración y partición P0/P1/P2 conforme DEC-C10-052…058. P0 declarativo migrable; P1 envolvente técnica/estado de entorno; P2 frontera causal transversal.
- F* es contrato funcional de referencia, no una puntuación de valor ni garantía de equivalencia. Su matriz operacional y adjudicación siguen sujetas a los estados de los artefactos especializados.

### 4.2 Intervención y primeras etapas

No reducir la intervención a una intervención abstracta sobre A_f*. La arquitectura material distingue:

`Z → B0/B1 → B_received / W_attempt → (C_install, C_integrity, C_compat, C_oper) → C_dep* → A_f*(t) → D_f* `

La secuencia no es una cadena determinista universal: depende de predicados constitutivos, condiciones comunes, versiones, soporte, alternativas y tiempo. La primera etapa en provisión o dependencia no prueba la primera etapa en accesibilidad ni la apertura focal. `C_dep*` debe derivarse de la distribución conjunta de los cuatro componentes; no se sustituye por cuatro marginales independientes salvo escenario explícito.

### 4.3 Espacio transformacional y proceso

- Snapshots estructurales pre/post y correspondencia de identidades/versiones permiten derivar `ΔT_acc*`; `ΔE_T` (cambio epistémico de evidencia) no debe confundirse con cambio estructural.
- `D_f*` representa apertura focal bajo la definición de población basal elegible correspondiente; no es sinónimo de A_f*(t), C_dep* o ΔT_acc*.
- Reach y `Π_H` derivan de rutas/predicados temporales; los estados 1/0/? y la propagación de indeterminación deben conservarse.
- F1/F2 son rutas/transformaciones focales y A1/A2 alternativas en el microdominio; no presumir independencia de B ni equivalencia funcional sin evidencia del DGP.
- Aplicabilidad, selección, ejecución, Outcome y Value son objetos separados. Outcome no es Value; Value no se deriva mecánicamente de accesibilidad o ejecución.

### 4.4 U_G y evidencia

U_G es infraestructura de observación, procedencia, cobertura, evaluación y adjudicación; no es el generador de verdad. DEC-C10-059…065 y OAS-01…11 definen decisiones y reconciliaciones documentales del esquema, pero el esquema no está congelado ni validado técnicamente. La verdad del DGP debe permanecer separada de las observaciones y de los registros de evaluación.

## 5. Arquitectura de estimandos: no colapsar objetos

| Objeto | Interpretación | Estado |
|---|---|---|
| `ITT_Z` | Efecto de asignación a la política B concreta en la población/horizonte definidos | Objetivo de diseño propuesto; detalles de DGP y población abiertos |
| `ψ_policy` / efecto de paquete | Efecto total de la política cuando afecta accesibilidad y otras vías | Debe reportarse como paquete si no se sostiene aislamiento |
| `ITT_Df` | Primera etapa sobre apertura focal | Debe derivarse del DGP; no fijada como resultado observado |
| `LATE_f` / Wald | Efecto local entre compliers bajo supuestos IV | Secundario y condicionado; robustez a instrumento débil pendiente |
| `θ_Af(q*)` | Contraste de políticas focales bajo régimen común y condiciones de atribución | Propuesta de armonización; no aprobado |
| `θ_A(q)` | Pregunta científica general de C10-D1 sobre accesibilidad y Value | Permanece central; no sustituible por ITT/LATE de S4-R |
| `θ_{L,A}` | Efecto conjunto si no puede separarse la vía focal de otras dimensiones | Alternativa interpretativa, no estimando primario aprobado |

La aleatorización identifica el efecto de asignación bajo su diseño, no demuestra por sí sola exclusión ni mediación. Si B tiene vías directas/colaterales hacia Value, el ITT sigue siendo efecto de política/paquete, no atribución aislada a accesibilidad. LATE no es ATE ni efecto general de ΔT_acc.

## 6. D1/D2 y primera etapa: mantener la discrepancia abierta

La fuente recuperada §§165–168 propone D1 (provisión ordinaria en control; intento w0=.25; w1=1; éxito conjunto objetivo s=.80; p0=.20, p1=.80; primera etapa .60) como principal condicionado y D2 (sin provisión ordinaria en control; w0=0; w1=1; p0=0, p1=.80; primera etapa .80) como contraste. El maestro §§65–70 conserva gates y objetivos diferentes para la selección. No existe base para declarar uno aceptado sin resolver:

- qué objetivo científico gobierna la selección (mecanismo/realismo del comparador frente a contraste de política más fuerte);
- si la provisión ordinaria de control pertenece al régimen de comparación plausible;
- cómo se modelan componentes conjuntos y correlación;
- soporte/positividad, versiones y población compliers;
- efecto sobre alternativas y exclusión.

Los valores .20/.80/.60/.80 y s=.80 son ilustrativos/candidatos condicionados, no tasas empíricas ni valores confirmatorios.

## 7. Medición, Value y ausencia

La fuente recuperada §§179–183 amplía el diseño: Value vectorial como recomendación provisional, no índice escalar impuesto; separar A, O y V; validez de constructo, fiabilidad, error, invariancia y sensibilidad; temporalidad T0–T6; medición independiente y cegamiento; MCAR/MAR/MNAR, abandono, censura, selección postasignación, cotas y sensibilidad. P181/P182/P183 son contratos propuestos, no pruebas ejecutadas. Deben integrarse en maestro, test register y DGP con estado explícito.

## 8. Matriz de brechas y acciones

| ID | Brecha | Riesgo | Acción requerida | Gate |
|---|---|---|---|---|
| MRA-01 | §§131–163 sin fuente primaria localizada | reconstrucción desde memoria | localizar commits, PR, archivos y conversaciones exportadas; no inventar | recuperación histórica |
| MRA-02 | §§165–183 no integradas completamente en maestro | pérdida de formulaciones/decisiones | transcribir y reconciliar con estado; preservar fuente original | maestro |
| MRA-03 | Decision Log, maestro y contratos pueden divergir | decisión aceptada no reflejada o propuesta elevada | crosswalk por DEC, SHA, sección y estado | trazabilidad |
| MRA-04 | Plan 001 conserva lenguaje previo | dirigir trabajo desde arquitectura obsoleta | sustituir por Plan 002 y marcar Plan 001 histórico/supersedido | plan |
| MRA-05 | D1/D2 sin adjudicación definitiva | estimando/población incoherentes | comparar objetivo, plausibilidad, soporte, primeras etapas y IV | diseño causal |
| MRA-06 | DGP técnico conjunto sin distribución confirmatoria | primera etapa mal representada | cerrar distribución 16 celdas, dependencia y sensibilidad | DGP |
| MRA-07 | F*, alternativas y población P*_τ2/P*_F abiertos | atribución por exclusividad asumida | cerrar reglas, elegibilidad, predicados y cobertura | medición/identificación |
| MRA-08 | q_X*/q_L* y unidad/interferencia no aprobados | régimen imposible o sesgo | cerrar soporte, asignación, exposición y spillovers | identificación |
| MRA-09 | P181/P182/P183 no incorporadas de forma completa | sesgo de medición/selección | integrar y cruzar contratos A/O/V y datos ausentes | medición |
| MRA-10 | estadística sin justificación final | baja potencia, mala cobertura o falsos positivos | simulación de potencia/precisión/Monte Carlo tras DGP/estimandos | estadística |
| MRA-11 | PR #116 body desactualizado | descripción de alcance incorrecta | actualizar tras persistir documentos | gobernanza PR |
| MRA-12 | autoauditoría no independiente | sobreafirmación de validación | etiqueta AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT | gobernanza |

## 9. Reglas de no-regresión

1. No reintroducir `q/g0/g1/C_auth` como arquitectura material primaria del experimento sin reconciliación explícita con B0/B1, C_dep*, A_f*(t), D_f* y la decisión de intervención.
2. No equiparar provisión, intento, dependencia, accesibilidad, apertura focal, cambio completo de T_acc, Reach, trayectoria, aplicabilidad, ejecución, Outcome y Value.
3. No asumir independencia de componentes técnicos, rutas alternativas, unidades o evaluadores.
4. No imponer exclusión IV por definición ni presentar un control negativo como prueba de exclusión.
5. No convertir D1 o D2, q_X*/q_L*, N=2000, 1000 réplicas, δ/ε ni Value vectorial/escalar en decisiones sin registro explícito.
6. No elevar contenido conversacional recuperado a decisión aceptada.
7. No utilizar revisión externa como condición para el avance científico interno; declarar autoauditoría no independiente.
8. No ejecutar DDL, parser, validadores técnicos, fixtures, simulaciones ni experimento sin autorización expresa.

## 10. Estado y dictamen

**Dictamen:** revisión mayor necesaria; el plan 001 no debe seguir dirigiendo el trabajo. El maestro ahora registra la no conformidad y el gate de recuperación (§§131–132), pero la recuperación histórica y la reconciliación integral no están terminadas. No se ha aprobado ningún nuevo estimando, D1/D2, DGP confirmatorio, parámetro estadístico ni regla de Value. No hay freeze ni ejecución.

**Clasificación:** AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT.  
**Siguiente operación:** recuperar §§131–163 desde fuentes persistidas; transcribir y reconciliar §§165–183; actualizar maestro, Decision Log, DGP, matriz de cierre, test register y plan; luego ejecutar auditoría de no-regresión antes de volver a XAUD.
