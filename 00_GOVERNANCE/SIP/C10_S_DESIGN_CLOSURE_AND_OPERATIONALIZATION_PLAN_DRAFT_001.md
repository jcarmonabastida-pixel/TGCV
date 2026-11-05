# C10-S — Plan integral de cierre del diseño y operacionalización

**ID:** C10-S-PLAN-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-04
**Estado:** DRAFT / NO APROBADO / NO CONGELADO.

Este documento consolida el diagnóstico, los artefactos y el plan de cierre de C10-S. Se actualiza incrementalmente con cada bloque de trabajo y sus auditorías.


# I. Auditoría documental (corte 2026-11-04)

## 1. Alcance y método

Se consultaron directamente en GitHub: README.md y 00_GOVERNANCE/README.md en main; PR #116 y lista de archivos/reviews/threads; maestro C10-S; contrato DGP; Decision Log; matriz de cierre; registro de pruebas; recuperación 165–183; auditoría cruzada AUD-001/002; propuesta de resolución; auditorías integradas de consistencia y reconciliación; reconciliación C10-D1/S4-R; tracker XSYNC-138; PR #117 y artefactos bootstrap/IGRT.

La auditoría fue documental y de metadatos. No se ejecutaron validadores, código, pruebas, simulaciones ni experimentos. No constituye revisión matemática externa independiente.

## 2. Estado verificado de PR #116

| Campo | Estado observado |
|---|---|
| Estado | OPEN / Draft |
| Mergeable informado | Sí |
| Head | research/c10-s-consolidation-draft |
| HEAD (corte inicial de auditoría) | d007a877b25caec72643b2efbaca0f7cf8eb7ea5 |
| Base | research/c10-d1-protocol-draft |
| Commits (corte inicial) | 184 |
| Archivos (corte inicial) | 13 |
| Adiciones/eliminaciones | 10.639 / 0 |
| Reviews / threads / comentarios | 0 / 0 / 0 |

**AUD-PLAN-01 — Rama base:** PR #116 apunta a C10-D1 y no a main. Puede ser dependencia deliberada, pero requiere decisión explícita sobre motivo, secuencia de integración y conflictos. Mergeable no significa aprobación científica.

## 3. Hallazgos de auditoría

### P0 — bloqueantes

| ID | Hallazgo | Evidencia/efecto | Acción requerida |
|---|---|---|---|
| AUD-PLAN-02 | Intervención autónoma sobre accesibilidad no cerrada. | XAUD-001/002 abiertos; relación q, g0/g1 y C_auth no resuelta. Riesgo de atribuir a A el efecto de paquete B/Z. | Definir intervención, régimen, políticas, condiciones, vías y estimando. |
| AUD-PLAN-03 | Estimandos y comparador primario no aprobados. | Reconciliación C10-D1/S4-R es propuesta; OPEN-C10-001/005 y selección primaria abiertas. | Aprobar jerarquía TE, ITT, θ_A(q), LATE_f; población y horizonte. |
| AUD-PLAN-04 | Población y D1/D2 no cerrados. | P*_τ2/P*_F, elegibilidad, provisión ordinaria, intentos y alternativas pendientes. | Contrato de población, unidad y políticas completas. |
| AUD-PLAN-05 | DGP no completo extremo a extremo. | AUD-003…008, S5-C/S5-F y escenarios causales/transformacionales requieren integración. | Ecuaciones y reglas generadoras para todas las variables. |
| AUD-PLAN-06 | C_dep no implica en general A_f* ni D_f*. | §67 condiciona igualdad a inaccesibilidad basal, ruta única, predicados no técnicos invariantes y medición válida. | Escenarios de equivalencia/no equivalencia; primeras etapas separadas. |

### P1 — imprescindibles antes del freeze

| ID | Hallazgo | Evidencia/efecto | Acción requerida |
|---|---|---|---|
| AUD-PLAN-07 | Contratos de pruebas no ejecutados ni completos como suite. | ACC/JNT/FIX definidos documentalmente; AUD-003 exige entradas, salidas y aserciones inequívocas. | Completar contratos críticos; ejecutar solo con autorización. |
| AUD-PLAN-08 | Validez de constructo y error de medición abiertos. | AUD-004/005/007/008 y P182/P183; riesgo de circularidad/error diferencial. | Matriz constructo-indicador-fuente-evaluador-error-cegamiento. |
| AUD-PLAN-09 | Identificación, falsación y sensibilidad abiertas. | XSYNC-01…10 incluye exclusión, soporte, versiones, trayectorias y δ/ε. | Matriz de supuestos, amenazas, falsadores y salidas no identificadas. |
| AUD-PLAN-10 | Dimensionamiento provisional. | AUD-009; N, réplicas, potencia, precisión y umbrales pendientes. | Plan estadístico justificado antes de resultados. |
| AUD-PLAN-11 | Reconciliación 165–183 incompleta. | Fuente recuperada/examinada; integración con matriz, Decision Log y pruebas en curso; P181/P182/P183 no ejecutadas. | Cotejar decisiones y P182/P183 preservando procedencia. |

### Hallazgos de integración

- **AUD-PLAN-12 — XSYNC:** el texto XSYNC-138-01…10 está recuperado y mapeado; el tracker exige búsqueda global, revisión de contratos y disposición por ID. Recuperación no equivale a cierre.
- **AUD-PLAN-13 — AUD-001/002:** la auditoría cruzada indica que no deben fijarse ecuaciones definitivas de θ_A(q) antes de resolver q/g/C_auth e intervención autónoma. La resolución posterior es propuesta pendiente de revisión y armonización.
- **AUD-PLAN-14 — C10-D1/S4-R:** ITT de política, TE y contribución atribuible a accesibilidad deben seguir separados. El ITT de paquete no identifica por sí mismo el efecto de A_f*.
- **AUD-PLAN-15 — integración PR:** justificar la rama base C10-D1 y documentar el orden de integración.

## 4. Precedencia D1/D2 y fuente 165–183

Hay una evolución de recomendaciones:
1. La recomendación conversacional reciente favorecía D2 como candidato mecanístico limpio y D1 como política incremental.
2. La fuente histórica 165–183 y la reconciliación integrada recuperan D1 como principal **condicionado** a justificar la provisión ordinaria en control, y D2 como contraste sin provisión ordinaria.
3. La reconciliación propone esa precedencia, pero no la acepta: la selección primaria permanece ABIERTA.

No son necesariamente diseños incompatibles; representan comparadores distintos. La decisión debe fijar pregunta primaria, relevancia real de provisión ordinaria, jerarquía confirmatoria y población/estimando/horizonte de cada escenario. ITT_D1 e ITT_D2 no se agrupan; las primeras etapas C_dep, A_f*, D_f* y ΔT_acc se informan separadamente; Wald/LATE pueden referirse a poblaciones distintas.

## 5. Primera etapa técnica: resultado y límite

El maestro §§67–69 y DGP §§26–28 contienen:
- C_dep* = C_install* ∧ C_integrity* ∧ C_compat* ∧ C_oper*.
- A_f* requiere predicados adicionales de identidad, relaciones, condiciones, autorización, recursos, dependencias y ausencia de bloqueos.
- Accesibilidad, aplicabilidad, selección y ejecución son constructos distintos.
- s=p1111 es una celda de una distribución de 16 patrones, no un DGP completo.
- Cuatro fixtures analíticos comparten s=.80, pero tienen marginales y fallos distintos.
- Bajo una oportunidad y supuestos simplificadores: FS_Cdep,D1=.75s y FS_Cdep,D2=s.
- El .20 de control D1 se deriva de q0=.25 y s=.80; no permanece constante al variar s sin cambiar otro mecanismo.

Son derivaciones documentales, no calibración empírica ni resultados Monte Carlo. Siguen abiertas marginales fijas, dependencia variable, heterogeneidad, rutas alternativas y múltiples intentos. No se transfiere FS_Cdep a A_f*/D_f* sin condiciones de §67.

## 6. Contradicción IGRT en gobernanza

En main, CHATGPT_BOOTSTRAP.md declara IGRT no establecido/no requerido y que no se espera puntero ni gate. Sin embargo, 00_GOVERNANCE/README.md conserva una instrucción de resolver el estado IGRT en el paso de carga.

PR #117 propone corregir 00_GOVERNANCE/README.md; en el corte estaba abierto y Draft, de governance/igrt-bootstrap-reconciliation-draft a main. La contradicción no debe declararse resuelta en main hasta integrar y verificar PR #117. Es un hallazgo de continuidad operativa, no científico.



# II. Inventario de artefactos y resultados

## 7. Los 13 artefactos existentes en PR #116

| Artefacto | Función | Estado |
|---|---|---|
| Maestro C10-S draft 004 | Arquitectura y desarrollo §§66–69 | Draft; requiere decisiones/reconciliación |
| Contrato DGP temporal/roles | Variables, tiempos y reglas; §§26–28 | Parcial; DGP no completo |
| Decision Log | Decisiones propuestas y precedencia | No asumir aceptación |
| Matriz de cierre | Pendientes y criterios | Parcial |
| Registro de pruebas | Contratos ACC/JNT/FIX y previos | Documental; no ejecutado |
| Auditoría cruzada AUD-001/002 | XAUD-001…007 | AUD-001/002 abiertos |
| Resolución AUD-001/002 | Propuesta de resolución | Pendiente de revisión/armonización |
| Reconciliación C10-D1/S4-R | Estimandos y escenarios | Propuesta; primario abierto |
| Auditoría integrada de consistencia | AUD-001…012 | Hallazgos abiertos |
| Auditoría integrada de reconciliación | Reconciliación transversal | Arquitectura candidata; no aprobada |
| Auditoría recuperación 165–183 | Recuperación y trazabilidad | Parcial/verificada según alcance |
| Registro fuente 165–183 | Secciones y procedencia | Fuente recuperada; reconciliación en curso |
| Tracker XSYNC-138 | XSYNC-01…10 | Texto recuperado; cierre pendiente |

## 8. Bloques incorporados durante el desarrollo

| Bloque | Contenido | Propagación |
|---|---|---|
| §66 | Papel comparativo D1/D2 | DGP §25; reconciliación §18; CMP-01…14; matriz §27; DEC-C10-026 |
| §67 | Predicados técnicos y derivación A_f* | DGP §26; DEC-C10-027; matriz §28; ACC-01…20 |
| §68 | Distribución conjunta de 16 patrones y Fréchet | DGP §27; DEC-C10-028; matriz §29; JNT-01…15 |
| §69 | Cuatro fixtures y propagación analítica | DGP §28; DEC-C10-029; matriz §30; FIX-01…12 |

§66: D1/D2 son regímenes diferentes. D2 fue candidato mecanístico; D1 incremental si el control ordinario se justifica. La fuente histórica recuperada favorece D1 condicionado como principal y D2 como contraste. Selección abierta.

§67: dependencia técnica no equivale automáticamente a accesibilidad. s=.80 es candidato ilustrativo, no dato observado.

§68: s=p1111 no identifica las otras 15 celdas, marginales ni dependencia. Familias y malla .60/.70/.80/.90 son exploratorias.

§69: fixtures de choque común, fallos simples, bottleneck y fallos emparejados. FS_D1=.75s y FS_D2=s bajo una oportunidad y supuestos explícitos. No son simulaciones.



# III. Plan de trabajo: bloques 1–4

## 9. Bloque 1 — Arquitectura causal y estimandos (P0)

**Objetivo:** fijar qué efecto se estima y qué intervención lo identifica.

Distinguir TE (efecto total), ITT_Z (efecto de asignar una política), θ_A(q) (contribución atribuible a accesibilidad bajo régimen común q, solo si se define e identifica) y LATE_f/Wald (efecto local bajo supuestos instrumentales; no intercambiable con ITT ni necesariamente comparable entre D1/D2).

Tareas:
1. Resolver XAUD-001: relación q, g0/g1 y C_auth.
2. Resolver XAUD-002: intervención que induce accesibilidad sin ordenar ejecución ni ocultar vías colaterales.
3. Separar Z, política B, intento W_attempt, recepción/cumplimiento, C_dep, A_f*, A_f,obs y D_f*.
4. Clasificar condiciones por tiempo causal: basal, constitutiva, mediadora, postratamiento u observacional.
5. Definir consistencia, versiones, soporte, interferencia, población y horizonte por estimando.
6. Alinear con C10-D1 sin sustituir la pregunta por el ITT S4-R.

**Entregable:** contrato causal integrado, DAG temporal y diccionario.  
**Cierre:** cada estimando tiene población, política, régimen, outcome, horizonte, supuestos y límites; ningún efecto de paquete se atribuye indebidamente a A.

## 10. Bloque 2 — Población, elegibilidad y D1/D2 (P0)

Tareas:
1. Definir P*_τ2 y P*_F, elegibilidad basal y relación de subconjunto.
2. Cerrar F*, H, G, C0, universo/cobertura de alternativas y adjudicación.
3. Distinguir alternativa ausente respaldada (0), presente (1) e indeterminada (?); “no encontrado” no significa ausencia.
4. Especificar D1/D2: intento, recepción, éxito, reintentos, recursos, versiones y vías colaterales.
5. Resolver precedencia D2 conversacional vs D1 histórico condicionado.
6. Aclarar p0=.20 frente a C_dep,base=0 mediante variable/tiempo, no intuición.
7. Definir unidad experimental, asignación, análisis, resultado e interferencia.

**Entregable:** contrato de población, elegibilidad, comparadores y versiones.  
**Cierre:** población y contrafactual de cada brazo inequívocos.

## 11. Bloque 3 — Accesibilidad, alternativas y ΔT_acc (P0)

Cadena a preservar, sin implicación automática:
C_install/C_integrity/C_compat/C_oper → C_dep → A_f* → D_f* → ΔT_acc*.

Tareas:
1. Predicados de identidad/versiones, relaciones/canales, precondiciones, autorización, recursos, dependencias, bloqueos y evidencia.
2. Separar capacidad del sistema T_cap y accesibilidad sistema-unidad T_acc.
3. Inventariar rutas técnicas/funcionales alternativas y cobertura para declarar ausencia.
4. Formalizar snapshots, altas/bajas, cambios relacionales, condiciones, validez y contexto.
5. Separar A_f*, A_f,obs, aplicabilidad, conocimiento, consideración, selección, inicio y ejecución.
6. Definir fallos, indeterminación, verificación desconocida y ausencia de evidencia.
7. Especificar errores de clasificación y diferencialidad por brazo.

**Entregable:** contrato de medición transformacional y matriz predicado-evidencia.  
**Cierre:** evaluador independiente clasifica sin consultar Outcome/Value y puede abstenerse con ?.

## 12. Bloque 4 — DGP integrado y ecuaciones (P0)

Tareas:
1. Completar DGP basal, intervención, accesibilidad, alternativas, Reach, trayectorias, conocimiento, selección, ejecución, Outcome y Value.
2. Completar S5-F y separar truth estructural de identificabilidad observacional en S5-C.
3. Integrar S4-O/S4-R con estimandos y mecanismos.
4. Especificar interacciones, vías directas/colaterales, versiones y cambios de condiciones.
5. Modelar intentos múltiples y dependencia secuencial; no usar independencia ni 1−(1−s)^n sin contrato.
6. Completar distribuciones con marginales fijas, dependencia variable, heterogeneidad y alternativas.
7. Impedir que el analizador reciba truth o parámetros generadores.

**Entregable:** DGP integrado y contrato de generación/reporte.  
**Cierre:** toda variable tiene regla generadora, rol causal, tiempo, distribución y observación.



# IV. Plan de trabajo: bloques 5–8

## 13. Bloque 5 — Validez de constructo y medición (P1)

Tareas:
1. Validez de contenido, convergente/discriminante cuando proceda.
2. Indicadores y fuentes independientes para T_acc, ΔT_acc, Reach, trayectoria, Outcome y Value.
3. Adjudicación, cegamiento y fiabilidad intra/interevaluador.
4. Sensibilidad, especificidad, falsos positivos/negativos y error diferencial.
5. Invariancia entre brazos, escenarios, periodos y versiones.
6. Reconciliar P182/P183 con matriz, Decision Log y registro de pruebas.
7. Missingness MCAR/MAR/MNAR, censura y selección postratamiento.

**Entregable:** matriz constructo-indicador-fuente-error-validación.  
**Cierre:** no hay circularidad; errores e indeterminación están modelados.

## 14. Bloque 6 — Identificación, falsación y sensibilidad (P1)

Tareas:
1. Supuestos: relevancia, independencia, exclusión, monotonicidad, consistencia/versiones, positividad/soporte e interferencia.
2. Confusión inducida por tratamiento y mediadores postratamiento.
3. Sensibilidad a alternativas, rutas directas, recursos, autorización, conocimiento, costes y calidad de ejecución.
4. Primera etapa débil/nula y error de clasificación.
5. Escenarios adversariales: Outcome cambia sin A; A cambia sin Value; A y otra vía cambian; exclusión falla; alternativas existen; missingness informativa.
6. Reglas de salida: efecto paquete, atribución identificada/no identificada, evidencia adversa, equivalencia o insuficiencia.
7. Cierre por ID de XSYNC-138-01…10.

**Entregable:** matriz de identificación, amenazas, falsadores y resultados admisibles.  
**Cierre:** el diseño puede concluir no-identificación o evidencia adversa.



## 15. Bloque 7 — Dimensionamiento y reglas estadísticas (P1/P2)

Tareas:
1. Justificar N, asignación, escenarios y réplicas.
2. Potencia, precisión, cobertura y error Monte Carlo.
3. Primeras etapas débiles, heterogeneidad, missingness e interferencia.
4. Definir δ de relevancia y ε de equivalencia con fundamento sustantivo.
5. Reglas bilaterales/direccionales, intervalos, equivalencia e inconclusión.
6. Revisar N=2.000 y 1.000 réplicas como candidatos, no decisiones.

**Entregable:** plan estadístico preespecificado.  
**Cierre:** discrimina relevancia, equivalencia, daño e insuficiencia con precisión justificada.

## 16. Bloque 8 — Auditoría, contratos y gobernanza (transversal)

Tareas:
1. Disponer AUD-001…012, XAUD-001…007 y XSYNC-01…10 con evidencia por ID.
2. Reconciliar maestro, DGP, Decision Log, matriz y test register.
3. Integrar fuente 165–183 y P182/P183.
4. Revisión matemática y causal independiente registrada.
5. Resolver rama base PR #116 y secuencia de integración.
6. Verificar hashes, versiones, trazabilidad y regla de no propagación.
7. Convertir contratos críticos en pruebas ejecutables; preflight/replay/auditoría.
8. Mantener PR Draft hasta satisfacer gobernanza.

**Entregable:** expediente de cierre auditable.  
**Cierre:** ningún P0 sin disposición; cada aceptación tiene autoridad, evidencia y commit.



# V. Gates y secuencia

## 17. Cinco gates

| Gate | Evidencia mínima | Habilita |
|---|---|---|
| G1 — Conceptual | Constructos, población, unidad, intervención, estimandos, DAG y decisiones | Freeze conceptual |
| G2 — Causal | Supuestos, vías alternativas, identificación, falsadores y sensibilidad | Protocolo causal |
| G3 — Generativo | DGP completo, ecuaciones, parámetros, distribuciones y escenarios adversariales | Freeze de especificación |
| G4 — Medición/estadística | Validez, error, missingness, N, réplicas, precisión, δ/ε | Implementación autorizable |
| G5 — Técnico/reproducibilidad | Código, contratos, preflight, pruebas, replay, hashes y auditoría independiente | Solicitud de autorización de ejecución |

Los gates requieren evidencia, no volumen documental. Aprobar el diseño no autoriza ejecución; la autorización es una decisión separada.

## 18. Orden de trabajo

| Fase | Trabajo | Producto |
|---|---|---|
| 0 | Reconstrucción histórica, precedencia y rama base | Registro de decisiones/fuentes |
| 1 | Estimandos, q/g, intervención, población y D1/D2 | Contrato causal |
| 2 | Accesibilidad, alternativas, F*, ΔT_acc y medición | Contrato transformacional |
| 3 | DGP y ecuaciones completas | Especificación generativa |
| 4 | Validez, errores, missingness y Value | Matriz de medición |
| 5 | Identificación, falsación y sensibilidad | Matriz causal |
| 6 | N, réplicas, precisión y δ/ε | Plan estadístico |
| 7 | Revisión independiente y cierre documental | Dictamen de diseño |
| 8 | Implementación y pruebas | Paquete técnico |
| 9 | Preflight, replay, auditoría y G5 | Solicitud de autorización |
| 10 | Ejecución autorizada y auditoría científica | Resultados reproducibles |

No dimensionar definitivamente antes de cerrar DGP/estimandos. No implementar antes de cerrar truth/observación y medición. No ejecutar fixtures o simulaciones sin autorización.



## 19. Decisiones pendientes

| ID | Decisión | Estado |
|---|---|---|
| DEC-PLAN-01 | Estimando primario y jerarquía TE/ITT/θ_A(q)/LATE_f | ABIERTO |
| DEC-PLAN-02 | Intervención B/Z, q, g0/g1 y C_auth | ABIERTO |
| DEC-PLAN-03 | Comparador primario D1/D2 y escenario secundario | ABIERTO |
| DEC-PLAN-04 | Población P*_τ2/P*_F y unidad | PARCIAL |
| DEC-PLAN-05 | F*, H/G/C0, alternativas y cobertura | ABIERTO |
| DEC-PLAN-06 | Distribución conjunta de 16 patrones | ABIERTO |
| DEC-PLAN-07 | s y calibración | ABIERTO |
| DEC-PLAN-08 | Rutas alternativas y múltiples intentos | ABIERTO |
| DEC-PLAN-09 | Regla Value, beneficiario y horizonte | ABIERTO |
| DEC-PLAN-10 | δ/ε | ABIERTO |
| DEC-PLAN-11 | N/réplicas/precisión | PROVISIONAL |
| DEC-PLAN-12 | Rama base PR #116 e integración | ABIERTO |
| DEC-PLAN-13 | Revisión independiente | PENDIENTE |
| DEC-PLAN-14 | Autorización de implementación/ejecución | NO AUTORIZADA |

## 20. Contrato de trazabilidad requerido

Cada estimando debe enlazar con población, intervención, política/régimen, outcome, horizonte y supuestos. Cada variable debe enlazar con ecuación generadora, rol causal, tiempo, distribución, regla de observación y prueba. Cada resultado debe enlazar con fuente, hash/commit, evaluador, fecha y dictamen. La matriz completa aún debe construirse desde el diccionario DGP.

## 21. Criterios para operacionalizar

Para autorizar implementación: G1–G4 aprobados; P0 cerrados; decisiones primarias aceptadas; separación truth/observación; escenarios adversariales; validez/fiabilidad especificadas; plan estadístico justificado; C10-D1/S4-R reconciliados; revisión independiente documentada; autorización explícita de implementación.

Para autorizar ejecución, además: G5 aprobado; código, datos sintéticos, configuración y entorno identificados por versión/hash; preflight íntegro; pruebas críticas y replay superados; auditoría técnica/científica; autorización expresa de ejecución separada.



# VI. Mantenimiento y próxima operación

## 22. Reglas de mantenimiento

1. Actualizar este plan tras cada bloque sustantivo.
2. Registrar cada decisión en Decision Log como PROPUESTA/ACEPTADA/RECHAZADA/SUSTITUIDA.
3. No usar el maestro como sustituto de Decision Log, matriz o test register.
4. Cada hallazgo tendrá ID, severidad, evidencia, artefactos, criterio de cierre y estado.
5. Preservar formulaciones históricas y documentar precedencia/supersesión.
6. No marcar pruebas PASS sin ejecución identificada.
7. No presentar derivaciones como simulación ni parámetros candidatos como calibración.
8. No propagar resultados a Core/RMA/Matrix/STATUS sin decisión independiente.
9. Trabajar en rama/PR Draft conforme a gobernanza.
10. Revisar PR #116 y PR #117 antes de integrar.

## 23. Próxima operación recomendada

La siguiente operación debe cerrar la precedencia causal y de comparadores, no ampliar otra vez la sensibilidad técnica de s:

1. Cotejar fuente 165–183 con Decision Log, maestro §66, reconciliación C10-D1/S4-R y matrices.
2. Resolver D1 histórico principal condicionado frente a D2 conversacional preferente; registrar decisión, no inferirla.
3. Resolver q/g/C_auth e intervención autónoma (AUD-001/002; XAUD-001/002).
4. Fijar estimandos y población por escenario sin convertir ITT de paquete en efecto de accesibilidad.
5. Actualizar coordinadamente maestro, DGP, Decision Log, matriz y test register.
6. Someter el contrato a revisión causal independiente.

No comenzar dimensionamiento definitivo, implementación, simulación o ejecución antes de resolver esas dependencias.

## 24. Dictamen de auditoría (2026-11-04)

C10-S dispone de arquitectura conceptual y documentación sustancial, incluidos §§66–69, pero **no está listo para freeze ni operacionalización**.

- **P0:** intervención/estimandos; población/comparadores; accesibilidad/alternativas; DGP integrado y separación truth/observación.
- **P1:** validez de constructo; identificación/falsación; contratos ejecutables; revisión independiente.
- **P2:** dimensionamiento, precisión, potencia, δ/ε y paquete reproducible.
- **Gobernanza:** PR #116 Draft, sin reviews, con rama base C10-D1 que requiere justificación. Contradicción IGRT en main pendiente de integración/verificación PR #117.

No se declara G1–G5 superado. No se declara cierre científico. No se autoriza implementación, simulación ni ejecución.

## Anexo — Referencias de trabajo

Rutas del repositorio jcarmonabastida-pixel/TGCV:
- Maestro: `00_GOVERNANCE/SIP/C10_S_SYNTHETIC_EXPERIMENT_CONSOLIDATED_DRAFT_004.md`
- DGP: `00_GOVERNANCE/SIP/C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`
- Decision Log: `00_GOVERNANCE/SIP/C10_S_DECISION_LOG_DRAFT_001.md`
- Matriz: `00_GOVERNANCE/SIP/C10_S_CLOSURE_CONTROL_MATRIX_DRAFT_001.md`
- Tests: `00_GOVERNANCE/SIP/C10_S_TEST_CONTRACT_REGISTER_DRAFT_001.md`
- Auditoría cruzada: `00_GOVERNANCE/SIP/C10_S_AUD001_AUD002_CROSS_AUDIT_DRAFT_001.md`
- Resolución AUD-001/002: `00_GOVERNANCE/SIP/C10_S_AUD001_AUD002_RESOLUTION_DRAFT_001.md`
- Reconciliación: `00_GOVERNANCE/SIP/C10_S_C10D1_S4R_ESTIMAND_RECONCILIATION_DRAFT_001.md`
- Auditoría de consistencia: `00_GOVERNANCE/SIP/C10_S_INTEGRATED_CONSISTENCY_AUDIT_DRAFT_001.md`
- Auditoría de reconciliación: `00_GOVERNANCE/SIP/C10_S_INTEGRATED_RECONCILIATION_AUDIT_DRAFT_001.md`
- Recuperación: `00_GOVERNANCE/SIP/C10_S_RECOVERY_AND_TRACEABILITY_AUDIT_DRAFT_001.md`
- Registro 165–183: `00_GOVERNANCE/SIP/C10_S_RECOVERY_165_183_SOURCE_REGISTER_DRAFT_001.md`
- XSYNC: `00_GOVERNANCE/SIP/C10_S_XSYNC_138_CLOSURE_TRACKER_DRAFT_001.md`
- C10-D1: `00_GOVERNANCE/SIP/C10_D1_CAUSAL_ACCESSIBILITY_VALUE_PROTOCOL_DRAFT_001.md`
- PR #116: `research/c10-s-consolidation-draft` → `research/c10-d1-protocol-draft`.
- PR #117: `governance/igrt-bootstrap-reconciliation-draft` → `main`.

**Advertencia:** este plan es una instantánea documental. Repetir auditoría antes de integrar o ejecutar si cambian ramas, commits o artefactos.


# VII. Ejecución del plan — Fase 0 y Bloque 1 (2026-11-04)

## 25. Carga canónica y reconstrucción histórica

Se ha leído directamente desde GitHub `main`:
- `README.md` (blob `962ab503bf835b6e1a4f45c80a396f3eb2fe4c6c`);
- `00_GOVERNANCE/README.md` (blob `f4871301c70e98a0b1b91d2253d0e937768c75d8`);
- `HISTORICAL_RECONSTRUCTION_BEFORE_NEW_WORK_RULE_v0.1.md` (blob `c01b0cc3b2a7d6bcf56893a0665f09fd2c8ddba4`);
- `TECHNICAL_EXECUTION_WORKFLOW_v0.1.md` (blob `66810b5aad08be4667480b13382c019577f93790`).

Se han recuperado y cotejado C10-D1, C10-S §§43–51 y §§66–69, DGP §§1–28, Decision Log DEC-C10-015…029, la reconciliación C10-D1/S4-R, AUD-001/002, XAUD-001…007, la matriz y el registro de pruebas. Se ha respetado la regla de reutilizar trabajo compatible y no sustituir semántica histórica silenciosamente.

**Resultado Fase 0:** reconstrucción documental suficiente para continuar el Bloque 1; no se encontró un freeze o aceptación científica que cierre estos puntos. La contradicción/ambigüedad de intervención ya estaba reconocida en DEC-C10-024 y XAUD-001/002; no es un hallazgo nuevo.

## 26. Artefacto generado en Bloque 1

Nuevo documento:
`00_GOVERNANCE/SIP/C10_S_CAUSAL_ARCHITECTURE_RECONCILIATION_DRAFT_001.md`

Contiene:
- jerarquía de estimandos C10-D1 / S4-R;
- distinción TE_Z, ITT_Z, ψ_B, θ_A(q), θ_Af(q*) y LATE_f;
- interpretación de q_X* y q_L*;
- contraste entre intervención histórica sobre C_auth y provisión técnica B;
- candidata de intervención con C_auth basal e invariante;
- DAG temporal y diccionario de roles;
- criterios de cierre y discrepancias abiertas.

Se registró DEC-C10-030 como propuesta en el Decision Log, se añadieron CA-01…CA-07 a la matriz de cierre y CAUS-01…CAUS-10 al registro de contratos.

## 27. Resultado técnico-científico del Bloque 1

**Avance logrado:** las distinciones y la arquitectura candidata están reconciliadas documentalmente. No se han cerrado las decisiones de diseño.

Hallazgos críticos:
1. C10-D1 mantiene `θ_A(q)` como pregunta científica general; ITT de S4-R es efecto de política asignada, no sustituto.
2. `q_X*` es una distribución basal común candidata; `q_L*` solo se requiere si variables post-Z indispensables se gobiernan mediante régimen secuencial explícito. No ajustar mecánicamente por mediadores.
3. Hay dos propuestas históricas diferentes: intervenir `C_auth` (resolución AUD-001/002) y provisión técnica B (DEC-C10-022/DGP). DEC-C10-024 ya advierte la discrepancia.
4. Se recomienda para revisión una política B de provisión técnica con `C_auth` basal, elegible e invariante. Si B cambia autorización, recursos, información, costes, calidad, seguridad o alternativas, el ITT es efecto de paquete salvo identificación adicional.
5. D1/D2 permanece abierto: fuente 165–183 favorece D1 condicionado; DGP §25 y DEC-C10-026 favorecen D2 provisionalmente para el objetivo mecanístico. No se elige ninguno.
6. La unidad/interferencia, población, soporte, Value, horizonte y exclusión no están cerrados.

**Estado del Bloque 1:** AVANCE DOCUMENTAL / DECISIONES CIENTÍFICAS ABIERTAS. No declarar AUD-001/002 ni XAUD-001/002 cerrados. El entregable causal integrado existe como Draft, no como contrato aceptado.

## 28. Actualización de estado PR #116

Verificación posterior a las escrituras:
- PR #116: OPEN / Draft; no merged.
- Base: `research/c10-d1-protocol-draft`.
- Head: `research/c10-s-consolidation-draft`.
- HEAD: `7332694f3f54fd8f6ebb980aafb9a9e1192fe9f9`.
- Commits: 198.
- Archivos modificados: 15.
- Mergeable: true (metadato GitHub; no aprobación científica).
- Reviews/comentarios: ninguno observado en la consulta anterior al corte.

El PR contiene ahora el plan de cierre y el documento causal de Bloque 1, además de los artefactos anteriores. La descripción del PR no se ha reescrito en esta operación; su resumen de alcance puede necesitar actualización antes de revisión externa.

## 29. Próximo paso del plan

Continuar con **Bloque 2 — población, elegibilidad y D1/D2**, reutilizando:
- maestro §§46–51 y §§66;
- registro histórico 165–183;
- DEC-C10-017, DEC-C10-026 y DEC-C10-030;
- contratos CMP-01…14, F* y elegibilidad;
- reconciliación C10-D1/S4-R.

La operación siguiente debe cerrar la legitimidad del comparador para la pregunta primaria, la relación entre P*_τ2 y P*_F, la regla de elegibilidad pre-Z, el contrato F* y la cobertura de alternativas. La decisión D1/D2 seguirá requiriendo aprobación expresa. No iniciar dimensionamiento ni ejecución.


# VIII. Ejecución del plan — Bloque 2 (2026-11-04)

## 30. Artefacto de reconciliación generado

Nuevo documento:
`00_GOVERNANCE/SIP/C10_S_POPULATION_ELIGIBILITY_AND_COMPARATOR_RECONCILIATION_DRAFT_001.md`

Se incorporó:
- distinción formal P*_τ2 frente a P*_F y relación de subconjunto;
- regla de elegibilidad pre-Z y tratamiento de estados indeterminados;
- crosswalk C_dep,0 / A_f,0* / A_f,1* / D_f*;
- contrato pendiente de F* y Sub(π,F*,G,H,C0);
- cobertura de rutas alternativas y niveles E1–E4;
- precedencia D1 histórico condicionado frente a D2 mecanístico provisional;
- unidad/interferencia y criterios de cierre.

## 31. Hallazgo de consistencia adicional

Se detectó una sobrecarga de notación que puede inducir error causal:
- el maestro §48.2 usa D_f,0 como disponibilidad basal de dependencia;
- DGP §26 y decisiones posteriores usan D_f* como transición de apertura basal→post;
- C_dep,0 ya representa la dependencia técnica basal.

Se propone reservar C_dep,0 para dependencia técnica basal y D_f*=I(A_f,0*=0 ∧ A_f,1*=1) para apertura focal. No se reescribe el histórico; se requiere búsqueda global y nota de supersesión al armonizar el maestro. La primera etapa de C_dep, A_f,1* y D_f* debe reportarse separadamente.

## 32. Propagación documental

Se actualizó:
- maestro C10-S: §70;
- contrato DGP: §29;
- Decision Log: DEC-C10-031;
- matriz de cierre: §9, POP-01…07;
- registro de pruebas: §32, POP-11…18, FSTAR-01…06 y CMP-15…18.

Los contratos nuevos son documentales; no se han generado fixtures ni ejecutado pruebas.

## 33. Resultado del Bloque 2

**Avance logrado:** se reconciliaron los objetivos poblacionales y se hizo explícita la diferencia entre apertura de τ2 y apertura funcional exclusiva. Se identificó y registró la sobrecarga D_f,0. Se preservó la precedencia histórica de D1 y la recomendación provisional posterior de D2 sin forzar una selección.

**Pendientes bloqueantes:**
1. fichas operacionales y umbrales para cada condición constitutiva;
2. F* con S0, objetivo, criterio de aceptación, entradas/salidas, restricciones, tolerancias, H/G/C0 y recursos;
3. universo y cobertura de rutas alternativas, adjudicación y fiabilidad;
4. decisión explícita D1/D2;
5. verificación de C_dep,0 y A_f,0* por protocolos independientes;
6. auditoría de UE/UA, frontera y no interferencia;
7. revisión global de notación y aprobación científica.

**Estado del Bloque 2:** AVANCE DOCUMENTAL PARCIAL / NO CERRADO. OPEN-C10-001/003/005/007 continúan abiertas. No se declara elegibilidad operacionalizada ni F* validada.

## 34. Próxima operación

Continuar con **Bloque 3 — accesibilidad, alternativas y ΔT_acc**, reutilizando el contrato técnico de §§67–70 y DGP §§26–29. La operación deberá formalizar la matriz de predicados ID/REL/COND/AUTH/RES/DEP/BLOCK, estados 1/0/?, snapshots, versiones, cobertura, relación entre C_dep/A_f*/D_f*/ΔT_acc y errores de medición, sin volver a calibrar s=.80 como si fuera dato empírico.


# IX. Ejecución del plan — Bloque 3, subbloque de snapshots y ΔT_acc (2026-11-04)

## 35. Auditoría de reutilización previa

Antes de generar un artefacto nuevo se comprobó que el maestro ya contenía:
- §63.7: snapshot y ΔT_acc estructurado;
- §64.2–64.5: clasificación temporal-causal, reloj y no ajuste postratamiento;
- §67.3–67.6: predicados completos, VALID epistémico y no filtración;
- §§68–69: distribución conjunta de 16 patrones, fixtures y propagación analítica;
- DGP §§26–29 y contratos ACC/JNT/FIX.

Por tanto, no se recreó la matriz de predicados ni la calibración .80. Se realizó una auditoría de coherencia entre lo ya documentado.

## 36. Hallazgo crítico

La auditoría detectó una contradicción no resuelta: §63.7 incluía ΔValidity en la tupla causal ΔT_acc*, mientras §§64/67 y DEC-C10-023/027 declaran que VALID/cobertura es epistémico y no pertenece a la verdad estructural de A_f*.

Esto podía convertir un cambio de cobertura documental en un supuesto cambio real de accesibilidad. Ejemplo: descubrir en t1 una ruta que ya existía en t0 no significa que la política la haya creado.

## 37. Resolución propuesta y artefactos

Nuevo artefacto:
`00_GOVERNANCE/SIP/C10_S_TRANSFORMATIONAL_SNAPSHOT_AND_DELTA_RECONCILIATION_DRAFT_001.md`

Propuesta:
- snapshot estructural verdadero S_T*=(U*,R*,C*,X*);
- paquete de evidencia E_T separado;
- ΔT_acc*=(ΔU*,ΔR*,ΔC*,ΔX*);
- ΔE_T registra fuentes, cobertura, validez epistémica, procedencia, versión y adjudicación;
- validez estructural real permanece en condiciones/relaciones; validez de evidencia no entra en ΔT_acc*;
- identidad, versión, frontera, granularidad y mapping deben resolverse antes del diff;
- D_f* es proyección focal de ΔT_acc*, no equivalente al cambio completo.

La expresión de §63.7 se conserva como histórico, pero ΔValidity queda propuesta como supersedida para la definición causal. No se borró ni reescribió silenciosamente la fuente.

## 38. Propagación documental

Se incorporó:
- maestro C10-S: §71;
- contrato DGP: §30;
- Decision Log: DEC-C10-032;
- matriz de cierre: §10, SNAP-01…07;
- registro de pruebas: §33, SNAP-01…15.

Los contratos siguen siendo documentales; no hay fixtures ejecutables ni resultados de prueba.

## 39. Dictamen del subbloque

**Avance:** se identificó y resolvió en propuesta una conflación importante entre cambio estructural y cambio de evidencia. Esto mejora la validez de constructo de ΔT_acc y evita atribuir a la intervención cambios debidos únicamente a cobertura o descubrimiento.

**No cerrado:** AUD-004 continúa abierto; también AUD-001/005/007, XAUD-003/004/006 y XSYNC-138-03/06. Falta catálogo/IDs, reglas de equivalencia entre versiones, frontera/G, mapping, truth/observed por componente, oráculos, tolerancias y revisión independiente.

No hay aprobación, freeze, implementación, simulación ni ejecución.

## 40. Próxima operación del plan

Continuar Bloque 3 con **contrato de identidad, versionado y correspondencia de snapshots**:
1. catálogo y esquema de IDs para transformaciones, relaciones, condiciones y dependencias;
2. reglas de continuidad semántica frente a cambio de identidad;
3. mapping de versiones y granularidad;
4. reglas de diff para altas, bajas, reconfiguración y cambios de estado;
5. comparación basal/post y tratamiento de snapshots no comparables;
6. propagación a A_f*, D_f*, Reach_possible y pruebas SNAP.

Después, integrar la matriz predicado-evidencia con los contratos de Reach_possible y trayectorias (AUD-005), sin pasar aún al DGP completo ni a ejecución.


# X. Ejecución del plan — Bloque 3, identidad y correspondencia (2026-11-04)

## 41. Reconstrucción histórica y decisión de alcance

Se revisaron README.md y 00_GOVERNANCE/README.md en main, la regla HISTORICAL_RECONSTRUCTION_BEFORE_NEW_WORK_RULE_v0.1 y las secciones relevantes del maestro C10-S (§§43, 47–48, 57–58, 63–64, 70–71) y el contrato SNAP-DELTA-001.

La reconstrucción confirmó que ya existían reglas parciales sobre IDs canónicos, versiones, hash, comparabilidad, frontera, granularidad y estado indeterminado. No se duplicaron. La brecha nueva era el contrato completo para distinguir identidad semántica de especificación/implementación/evento y resolver mappings 1:1, 1:N y N:1.

## 42. Artefacto generado

`00_GOVERNANCE/SIP/C10_S_IDENTITY_VERSION_AND_SNAPSHOT_MATCHING_CONTRACT_DRAFT_001.md`

Contiene:
- niveles TID/SID/RID/EID;
- esquema de IDs opacos y persistentes;
- firma semántica y regla de continuidad;
- nueva identidad, continuidad o indeterminación;
- tratamiento de hash, plataforma, configuración, interfaz y recursos;
- matching jerárquico y adjudicación ciega;
- split/merge y correspondencia composicional;
- frontera, granularidad G y comparabilidad;
- eventos tipados de diff;
- implicaciones para τ2, A_f*, D_f* y ΔT_acc;
- no filtración y quince contratos adversariales ID-01…15.

## 43. Hallazgo de diseño que queda protegido

La continuidad de TID no implica equivalencia de accesibilidad, calidad, coste, riesgo, política causal ni Value. A la inversa, una misma TID puede volverse accesible/inaccesible por cambios de RID, compatibilidad, autorización, recursos, dependencias o relaciones. Si τ2 cambia de identidad entre baseline y post, no se calcula D_f* como transición de la misma transformación sin redefinir ex ante el objeto y el estimando.

## 44. Propagación documental

Se incorporó:
- maestro C10-S: §72;
- contrato DGP: §31;
- Decision Log: DEC-C10-033;
- matriz de cierre: §11, ID-01…10;
- registro de pruebas: §34, ID-01…15.

El contrato de prueba es documental; no se crearon fixtures ejecutables ni se ejecutaron pruebas.

## 45. Dictamen

**Avance:** la regla de correspondencia ya no depende de intuiciones ad hoc sobre nombres, hashes o versiones. Se dispone de una propuesta explícita para identidad semántica, realización técnica, mapping y comparabilidad.

**No cerrado:** faltan taxonomía aprobada, catálogo, serialización, firma/tolerancias por clase, G/frontera concretas del DGP, mapping focal τ2, oráculos, validación de errores y revisión independiente. AUD-004 y XSYNC-138-03/06 siguen abiertos.

No hay aprobación, freeze, implementación, simulación ni ejecución.

## 46. Próxima operación

Continuar con la **integración de los predicados de accesibilidad y la cobertura de rutas en Reach_possible y trayectorias**:
1. reutilizar los predicados constitutivos del §67 y los estados de evidencia 1/0/?;
2. definir propagación de indeterminación por ruta, composición y horizonte;
3. distinguir Reach_possible verdadero, observado y estimado;
4. impedir que la falta de evidencia se convierta en ausencia de ruta;
5. conectar T_acc/ΔT_acc y el contrato de matching con enumeración de trayectorias sin usar selección/ejecución/Outcome/Value para definir accesibilidad;
6. diseñar pruebas adversariales y criterios de no-identificación.

Este paso aborda AUD-005 y la parte correspondiente de AUD-007. No iniciar aún simulación ni ejecución.


# XI. Ejecución del plan — Bloque 3, Reach y trayectorias (2026-11-04)

## 47. Reconstrucción y alcance

Se revisaron README.md y 00_GOVERNANCE/README.md, la regla de reconstrucción histórica y el maestro §§43, 47–49, 58, 63–67 y 71–72, además de los contratos de snapshot, identidad y DGP.

La arquitectura previa ya distinguía T_acc, Reach_H, Π_H^cand, Π_H^sel y Π_H^exec, además de accesibilidad y aplicabilidad. No se duplicó esa definición: se formalizó la propagación de incertidumbre por rutas y el requisito de exhaustividad para afirmar no alcanzabilidad.

## 48. Artefacto generado

`00_GOVERNANCE/SIP/C10_S_REACHABILITY_AND_TRAJECTORY_PROPAGATION_CONTRACT_DRAFT_001.md`

Incluye:
- definición de Reach_H* (truth) y Reach_H,obs;
- secuencia admisible con identidad, accesibilidad, aplicabilidad, composición, recursos y temporalidad;
- lógica trivalente 1/0/? por ruta;
- disyunción entre rutas alternativas;
- conjuntos lógicos Reach_H^- y Reach_H^+;
- horizonte, ciclos, truncamiento y snapshots dinámicos;
- separación de selección/ejecución/Outcome/Value;
- criterios de no-identificación;
- veinte contratos adversariales REACH-01…20.

## 49. Regla crítica resultante

Una ruta confirmada basta para afirmar que un estado es alcanzable. La ausencia de rutas confirmadas no demuestra no alcanzabilidad. Para declarar Reach=0 deben estar exhaustivamente cubiertos el universo, catálogo, frontera, granularidad, horizonte y rutas posibles, y todas las rutas deben quedar refutadas. Si existe una ruta potencial con predicado desconocido, mapping no resuelto, cobertura incompleta o búsqueda truncada, el resultado es ?.

La aplicabilidad se evalúa desde el estado intermedio para recorrer la ruta, pero no se usa para redefinir T_acc. La selección y ejecución son downstream y no forman parte de Reach estructural.

## 50. Propagación documental

Se incorporó:
- maestro C10-S: §73;
- contrato DGP: §32;
- Decision Log: DEC-C10-034;
- matriz de cierre: §12, REACH-01…10;
- registro de pruebas: §35, REACH-01…20.

Los contratos son documentales; no hay fixtures ejecutables ni pruebas realizadas.

## 51. Dictamen

**Avance:** la lógica de alcanzabilidad y la propagación de indeterminación quedan especificadas documentalmente.

**No cerrado:** AUD-005 y AUD-007 siguen abiertos. Faltan catálogo finito DGP, estados iniciales/objetivo, G/H, duraciones, ciclos, reglas composicionales por clase, recursos, snapshots dinámicos, cobertura de rutas, oráculos, validación de error y revisión independiente.

No hay aprobación, freeze, implementación, simulación ni ejecución.

## 52. Próxima operación

El siguiente bloque no debe añadir más definiciones abstractas. Debe convertir los contratos en un **inventario finito del DGP y un mapa de cobertura**:
1. fijar estado inicial y estados objetivo del experimento sintético;
2. enumerar TID/SID/RID focales y no focales y relaciones permitidas;
3. fijar G, H, duración, ciclos y reglas de composición;
4. enumerar condiciones, recursos, autorizaciones, bloqueos y rutas alternativas;
5. construir la matriz ruta × predicados × tiempo × evidencia × cobertura;
6. clasificar qué estados/rutas son exhaustivamente enumerables y cuáles quedan ?;
7. alinear inventario con REACH-01…20, SNAP-01…15 e ID-01…15.

La operación será documental y de especificación. No ejecutar generador ni simulación sin autorización expresa.


# XII. Ejecución del plan — Bloque 3, inventario finito del DGP y cobertura Reach (2026-11-04)

## 53. Reconstrucción y artefacto

Se revisaron README.md y 00_GOVERNANCE/README.md en main, el maestro C10-S, el contrato DGP temporal/roles, el contrato Reach, el registro de pruebas, la matriz de cierre, el Decision Log y los metadatos/diff del PR #116.

Se creó C10_S_FINITE_DGP_INVENTORY_AND_REACH_COVERAGE_DRAFT_001.md. El documento define una topología abstracta candidata con estados S0/S1/S2/SF; transformaciones F1/F2/A1/A2; rutas F1→F2 y A1→A2; escenarios R0–R3; G atómica y H=3 candidato; recursos, condiciones, bloqueos y ocho dimensiones de cobertura.

## 54. Hallazgos de auditoría

1. El contrato temporal DGP ya separa t0–t9 y la verdad generadora de las observaciones; el inventario no debe redefinir ese reloj.
2. El historial del PR menciona G0/G1, H=3 y ramas dinámicas, pero esos elementos no bastan para aprobar el catálogo ni resolver la selección D1/D2.
3. Abrir τ2/F1 no garantiza alcanzar SF: la continuación F2 debe ser accesible, aplicable y componible.
4. Una ruta alternativa A1→A2 puede mantener Reach(SF)=1 antes y después de abrir F1; por tanto D_f* no es equivalente a apertura funcional exclusiva ni a cambio de Reach.
5. Si B afecta A1/A2 (R2), aparece una vía colateral; no se interpreta automáticamente como instrumento focal exclusivo.
6. Intento sin éxito (R3) conserva la asignación y no autoriza imputar C_dep/A_f*/D_f*.
7. La ausencia de alternativa exige cobertura exhaustiva del universo funcional, no una búsqueda sin hallazgos.

## 55. Estado de cierre

**Avance:** inventario finito conceptual candidato y matriz ruta×predicados×tiempo×evidencia×cobertura documentados.

**Pendiente:** ratificar frontera, G, H, duración, F*, identidad focal, catálogo, relaciones, recursos, condiciones, alternativas, D1/D2, cobertura y oráculos. AUD-005/007 siguen abiertos; INV-01…08 no están cerrados.

No hay fixtures ejecutables, implementación, generación de datos, simulación, ejecución, freeze ni autorización.

## 56. Próxima operación

Auditar la consistencia del inventario contra el DGP completo y la reconciliación causal: resolver el encaje de H=3 con t0–t9; concretar si las rutas representan accesibilidad o composición de ejecución potencial; definir qué predicados se evalúan en cada instante; comprobar las cuatro variantes R0–R3 frente a S4R-A…D; y cerrar el esquema de evidencia/cobertura antes de añadir más topología.


# XIII. Ejecución del plan — integración temporal y S4-R (2026-11-04)

Se auditó el inventario finito contra el contrato DGP t0–t9, el contrato Reach_H y la reconciliación causal. Se creó C10_S_TEMPORAL_HORIZON_AND_S4R_INTEGRATION_AUDIT_DRAFT_001.md y se propagó como §75, contrato DGP §34, DEC-C10-036, matriz §14 y registro de pruebas §37.

Hallazgo: la descripción previa de H=3 como tres pasos/unidades de tiempo era ambigua frente a Reach evaluado en t4. Se propone separar reloj de estudio, profundidad de trayectoria y tiempo/ventanas de factibilidad; H=3 queda como profundidad candidata, no duración temporal confirmada. Reach se calcula en t4 sobre snapshot t3; las rutas son potenciales y no ejecuciones. R0–R3 se corresponden provisionalmente con S4R-A…D.

Pendiente: ratificar H; duración y ventanas; predicados App por estado; snapshots dinámicos por rama; recursos/caducidades; F*; cobertura funcional; D1/D2 y oráculos. AUD-005/007 siguen abiertos. No se han creado fixtures ejecutables, simulado ni ejecutado el experimento.

Siguiente bloque: especificar la tabla por paso y por rama de predicados de accesibilidad, aplicabilidad, composición, autorización, recursos, ventana y bloqueo, con tiempos y evidencia requerida; resolver explícitamente qué condiciones permanecen constantes bajo el snapshot t3 y cuáles pueden variar en la trayectoria hipotética.


# XIV. Ejecución del plan — matriz operacional de predicados (2026-11-05)

Se crea C10_S_PATH_PREDICATE_TEMPORAL_EVIDENCE_MATRIX_DRAFT_001.md y se propaga a maestro §76, contrato DGP §35, DEC-C10-037, matriz de cierre §15 y registro de pruebas §38.

La matriz separa accesibilidad, aplicabilidad, composición, condiciones, autorización, recursos, dependencia técnica, bloqueos, ventanas y evidencia/cobertura. Se propone snapshot estructural fijo en t3 para el fixture base, APP por estado hipotético de entrada y evaluación de cada rama por separado. Cualquier dinámica intrarrama exige regla explícita y snapshot inmutable. Se distingue truth DGP de observación; COV no forma parte de la verdad causal. Se registran clases I/S/T/R/D/E y contratos PM-01…18.

Pendiente: completar fichas sustantivas por transformación, fijar qué predicados son state-dependent/temporales, recursos/demanda/reserva, autorización y ventanas, F*, cobertura de alternativas, E1–E4 y oráculos. No se cierran AUD-004/005/007/010/011 ni OPEN-C10-001/003/005/007. No se han generado datos, implementado fixtures, simulado ni ejecutado el experimento.

Siguiente bloque: construir fichas sustantivas de predicados para F1, F2, A1 y A2 y resolver, sin asignar todavía valores truth, el significado operacional de cada precondición, condición, recurso, autorización, dependencia, bloqueo y ventana.


# XV. Ejecución del plan — reconciliación de fichas transformacionales (2026-11-05)

Se recuperaron las especificaciones históricas §§47–51 y 57–69 antes de crear nuevas fichas. Se creó C10_S_TRANSFORMATION_CARDS_HISTORICAL_RECONCILIATION_DRAFT_001.md y se propagó a maestro §77, contrato DGP §36, DEC-C10-038, matriz de cierre §16 y registro de pruebas §39.

Resultado: F1/τ2 está parcialmente especificada por los contratos de provisión y accesibilidad; F2/A1/A2 solo están definidas topológicamente. SF es un marcador formal, no una definición operacional de F*. No se deben inventar semánticas, umbrales o recursos para llenar el hueco. El trabajo previo sobre F*, accesibilidad, C_dep, evidencia y condiciones se reutiliza, no se duplica.

Pendiente: formular y comparar una propuesta explícita de microdominio sintético neutral, con F* observable y no circular, una transformación focal τ2, su continuación F2 y una ruta alternativa A1→A2 genuina. La selección requiere decisión explícita antes de completar las fichas y asignar parámetros del DGP. AUD-004/005/007/010/011 y OPEN-C10-001/003/005/007 permanecen abiertos. No se han generado datos, implementado fixtures, simulado ni ejecutado el experimento.

Siguiente bloque: preparar alternativas de microdominio que satisfagan los contratos ya definidos, compararlas contra C10-S (mecanismo focal, ruta alternativa, F*, predicados, evidencia, recursos, riesgos de exclusión y observabilidad) y recomendar una sin tratarla como aprobada.


# XVI. Ejecución del plan — comparación y recomendación de microdominio (2026-11-05)

Se comparan tres microdominios para completar las fichas F1/F2/A1/A2: migración de configuración software, integración de datos y reconfiguración de flujo organizativo. Se recomienda Opción A como candidata por parsimonia, verificabilidad técnica, control de recursos/ventanas y menor interferencia. Se crea C10_S_SYNTHETIC_MICRODOMAIN_OPTIONS_AND_SELECTION_RECOMMENDATION_DRAFT_001.md y se propaga a maestro §78, contrato DGP §37, DEC-C10-039, matriz de cierre §17 y registro de pruebas §40.

La propuesta ilustra F1=conversión mediante adaptador focal; F2=aplicación y validación en destino; A1=exportación a formato neutral preexistente; A2=importación/aplicación por mecanismo nativo. F* sería conformidad técnica de esquema, integridad y compatibilidad. B solo provisiona el adaptador y no ejecuta conversiones. La ruta alternativa debe ser mecanísticamente independiente; R2 prueba el caso de afectación colateral.

La recomendación no es selección ni aprobación. Pendiente decisión de microdominio, definición de propiedades/tolerancias F*, identidades/versiones, independencia de la ruta alternativa, recursos, permisos, ventanas, fallos, cobertura, E1–E4, D1/D2 y revisión independiente. No se cierran AUD-004/005/007/010/011 ni OPEN-C10-001/003/005/007. No hay datos, implementación, fixtures ejecutables, simulación ni ejecución.

Siguiente bloque: someter la Opción A a una auditoría de consistencia contra las ecuaciones causales/estimandos, la definición de A_f*, el comparador D1/D2 y los escenarios R0–R3; identificar si el adaptador focal realmente constituye una intervención sobre la accesibilidad o si introduce vías adicionales. Solo después recomendar aceptación o reformulación.


# XVII. Ejecución del plan — auditoría causal de Opción A (2026-11-05)

Se creó C10_S_MICRODOMAIN_CAUSAL_COMPATIBILITY_AUDIT_DRAFT_001.md y se propagó a maestro §79, reconciliación causal §10, contrato DGP §38, DEC-C10-040, matriz de cierre §18 y registro de pruebas §41.

Dictamen: migración de configuración software es potencialmente compatible, pero la propuesta actual no demuestra una intervención autónoma sobre accesibilidad ni identifica θ_A(q). Z/B puede identificar el ITT de la política de provisión, no el efecto mediado por A_f*. Se corrige la mezcla de F1: B provisiona/habilita adaptador; F1 es la conversión ejecutada con él disponible; C_dep y A_f* son variables diferentes; F2 aplica/valida en destino. Deben separarse App, ejecución y F*.

Se identifican vías colaterales potenciales por permisos, recursos, estado/configuración, seguridad, coste, latencia, información, dependencias/librerías compartidas y afectación de A1/A2. Se requiere manifiesto de cambios y grafo de dependencias. A1/A2 deben permanecer no afectadas por B en R0/R1; si B las modifica, R2 es vía colateral/efecto de paquete. F* se armonizará con la definición histórica de la reconciliación poblacional, sin duplicarla. D1/D2 sigue abierto.

Se mantienen seis gates MD-C1…MD-C6 y los contratos MDC-01…10 como especificaciones no ejecutadas. Opción A sigue recomendación condicionada, NO seleccionada ni aprobada. AUD-001/002, AUD-004/005/007/010/011, OPEN-C10-001/003/005/007 y CA-01…07 permanecen abiertos. No se generan datos, no se implementa, simula ni ejecuta.

Siguiente bloque: concretar el manifiesto de provisión B y el grafo de dependencias compartidas del microdominio; empezar por el catálogo de cambios que introduce la instalación del adaptador y la auditoría de no afectación de A1/A2. No asignar todavía probabilidades ni decidir D1/D2.


# XVIII. Ejecución del plan — manifiesto de provisión B y dependencias (2026-11-05)

Se crea C10_S_ADAPTER_PROVISION_MANIFEST_AND_DEPENDENCY_GRAPH_DRAFT_001.md y se propaga al maestro §80, contrato DGP §39, DEC-C10-041, matriz de cierre §19 y registro de pruebas §42.

Se define el límite normativo de B: provisionar/configurar el adaptador, verificar el paquete y habilitar un canal restringido, sin ejecutar transformaciones ni modificar F*, oráculo, fuente/destino, permisos funcionales o A1/A2. Se compara ARCH-B1 (sidecar aislado), ARCH-B2 (host compartido) y ARCH-B3 (servicio externo); ARCH-B1 se recomienda para evaluación, no está aprobada ni instalada. El catálogo B-M01…15 sigue NO INVENTARIADO y se establecen snapshots, grafo de dependencias, recursos, permisos, rollback y pruebas de no-afectación.

MD-C1/MD-C4 y MD-B01…08 permanecen abiertos. No se ha demostrado no-afectación de la ruta alternativa ni primera etapa sobre A_f*. No se han elegido D1/D2 ni parámetros, ni se han generado datos o ejecutado pruebas. Siguiente bloque: construir matriz de cobertura de nodos/aristas/predicados y estados 1/0/? para delimitar el universo de rutas y propagar indeterminación a Reach/F_alt.


# XIX. Ejecución del plan — matriz de cobertura y evidencia trivalente (2026-11-05)

Se crea C10_S_GRAPH_COVERAGE_AND_TRIVALENT_EVIDENCE_MATRIX_DRAFT_001.md y se propaga al maestro §81, contrato DGP §40, DEC-C10-042, matriz de cierre §20 y registro de pruebas §43.

El catálogo U_G contiene 23 roles de nodos, 23 aristas, 14 predicados y cinco clases de ruta. Es un universo candidato de inspección, no inventario técnico real ni exhaustivo. La cobertura efectiva es NONE porque no hay manifiesto real, SBOM, runtime, snapshots ni grafo transitivo. Se formalizan reglas trivalentes: Reach=0 exige cobertura exhaustiva; F_alt,0=0 exige descarte de todas las rutas funcionalmente substituibles del universo definido; unknowns y Runknown mantienen ?. Estado actual: Reach_H=?, F_alt,0=?, A_f*=?; R0/R1 no clasificables; R2 posible pero no observado.

GC-01…12 y GC-01…08 quedan como contratos/controles documentales, no ejecutados. MD-C1/2/4, AUD-005/007 siguen abiertos. Siguiente bloque: contrato de frontera y granularidad de U_G (componentes, dependencias, ruta funcionalmente substituible, servicio externo, versión y recursos compartidos), seguido de protocolo de inventario y evidencia. No se genera DGP técnico final ni se ejecuta.


# XX. Ejecución del plan — contrato de frontera y granularidad de U_G (2026-11-05)

Se recuperaron desde GitHub main la operativa 00_GOVERNANCE/README.md, el bootstrap y la regla de reconstrucción histórica; y desde la rama C10-S los contratos de frontera, cobertura, inventario finito, DGP, matriz de cierre y documentos maestros. Se confirmó que el contrato de frontera y granularidad ya existía como Draft 001, pero sus integraciones de destino no estaban incorporadas físicamente.

Se integra el contrato en C10-S §82 y en el DGP §41. Se corrige la numeración de la nota anterior: el DGP ya contiene §§1–40, por lo que no corresponde escribir una nueva §9; el plan ya contiene bloques I–XIX, por lo que el siguiente es XX, no IX. La integración previa en la nota era una intención pendiente, no evidencia de que estuviera escrita.

El contrato fija criterios de separación/agregación de nodos, dependencias directas/transitivas/compartidas/críticas, substituibilidad respecto de F*, servicios externos/opacos, niveles de recursos, cambios materiales de versión, límites y dimensiones de cobertura y protocolo de inventario con adjudicación independiente.

**Resultado:** contrato documental integrado; inventario técnico real NO DISPONIBLE. U_G continúa como catálogo candidato. Cobertura efectiva NONE donde no hay evidencia; A_f*, F_alt,0 y Reach_H permanecen ?. No se cierra MD-C1…6, AUD-005/007/010/011 ni OPEN-C10-001/003/005/007. No se selecciona Opción A, D1/D2, G/H ni parámetros. No hay implementación, simulación, ejecución ni freeze.

**Siguiente operación:** crear y reconciliar la plantilla de inventario U_G (nodos, aristas, rutas y predicados), con procedencia, fuente, versión, evidencia, cobertura, evaluador, cegamiento y estado 1/0/?. La plantilla no se rellenará con componentes o valores técnicos no observados.


# XXI. Ejecución del plan — plantilla de inventario U_G (2026-11-05)

Se crea C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md y se incorpora su crosswalk al maestro §83 y al DGP §42. La plantilla contiene registros separados para nodos, dependencias/aristas, rutas funcionalmente substituibles, predicados por paso/tiempo, snapshots/fuentes y cobertura por dimensión. Incluye procedencia, identidad/versionado, estado observado 1/0/?, cobertura, evaluador/cegamiento, adjudicación y motivos de indeterminación.

**Auditoría:** plantilla estructural completa como esquema documental; no contiene inventario técnico real. Las filas de ejemplo no son entidades observadas. No se asignan truth, versiones, recursos, dependencias ni rutas. La truth del DGP permanece restringida al generador/evaluador independiente. Cobertura NONE; A_f*, F_alt,0 y Reach_H siguen ?. La plantilla no demuestra independencia A1/A2 respecto de B ni permite cerrar MD-C1…6, AUD-005/007/010/011 u OPEN-C10-001/003/005/007.

**Siguiente operación:** reconciliar el esquema de la plantilla con los 23 roles de nodo, 23 aristas, 14 predicados y cinco clases de ruta de U_G (§81), verificando correspondencia y campos faltantes sin rellenar estados técnicos. Después, definir el protocolo documental de fuentes y adjudicación por dimensión. No se autoriza inspección de sistemas reales, implementación, generación de datos, simulación ni experimento.


# XXII. Ejecución del plan — reconciliación del catálogo U_G con la plantilla (2026-11-05)

Se ha contrastado el catálogo de §81 línea por línea con C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md. Correspondencia semántica: 23/23 roles de nodo, 23/23 IDs padre de arista, 14/14 predicados y 5/5 clases de ruta.

La auditoría no se limita a comprobar conteos. Detecta que E07 es una relación lógica y no una arista técnica; E17–E23 incluyen relaciones mult destino que deben normalizarse; la normalización propuesta genera 39 filas binarias candidatas. E22 no identifica nodos/eventos destino. N16 y N23 agregan constructos/etapas que deben descomponerse cuando se formalicen. Las clases primarias de ruta deben permanecer diferenciadas de los subtipos descriptivos.

Se amplía la plantilla con el crosswalk y campos complementarios de procedencia, evidencia, intención contractual, cobertura y adjudicación. La correspondencia es semántica, no inventario ni cobertura.

**Resultado:** esquema mejorado, pero **no cerrado**. Debe revisarse la desagregación N16/N23, la representación de E22 y la atomicidad/semántica de las 39 relaciones candidatas. Estados técnicos ?, cobertura NONE, A_f*/F_alt,0/Reach_H indeterminados. No se cierran GC-01…12, MD-C1…6, AUD-005/007/010/011 ni OPEN-C10-001/003/005/007.

**Siguiente operación:** elaborar el protocolo de fuentes, procedencia y adjudicación por dimensión, fijando qué evidencia mínima permite clasificar nodos, aristas, predicados y rutas, qué cobertura puede declararse y cómo resolver discrepancias. No inspeccionar sistemas reales ni ejecutar pruebas sin autorización expresa.


# XXIII. Ejecución del plan — protocolo de fuentes, procedencia y adjudicación (2026-11-05)

Se crea el protocolo documental C10_S_UG_EVIDENCE_PROVENANCE_AND_ADJUDICATION_PROTOCOL_DRAFT_001.md. Especifica ocho clases contextuales de fuentes, contrato de procedencia, evidencia mínima por nodos/aristas/predicados/rutas, argumento de cobertura negativa, cobertura con denominadores, doble evaluación cegada, adjudicación y propagación de estados.

**Resultado de diseño:** protocolo elaborado e integrado; todavía no validado contra un microdominio ni aplicado a fuentes reales. Define cuándo una evidencia puede respaldar 1, 0 o ?, cuándo cobertura es NONE/PARTIAL/COMPLETE y qué discrepancias exigen tercer adjudicador. No transforma la plantilla en inventario ni demuestra exhaustividad.

**Pendientes:** auditoría campo-a-campo entre protocolo y plantilla; definición de denominadores por dimensión para el microdominio seleccionado; selección y aprobación de fuentes concretas; seguridad/acceso; tolerancias y fiabilidad del oráculo; número y selección de evaluadores; cegamiento; criterios operativos de cobertura; cierre de N16/N23 y E22. Mantener MD-C1…6, GC/UGI/UGC, AUD-005/007/010/011 y OPEN-C10 abiertos. Sin ejecución ni autorización.


# XXIV. Ejecución del plan — auditoría campo-a-campo del esquema U_G (2026-11-05)

Se compara el protocolo de evidencia con las columnas y registros de la plantilla. La auditoría detecta nueve brechas: falta de registro de evidencia, falta de vínculo afirmación-evidencia, cobertura sin denominador, ausencia de registros separados E1/E2, ausencia de expediente de adjudicación, truth DGP visible como columna analítica, mezcla de clases de ruta y subtipos, falta de campos comunes obligatorios y falta de integridad referencial/versionado.

Se corrige documentalmente en la plantilla §§12–13 y protocolo §13 mediante registros EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER; truth DGP segregada; parent_route_class separado de route_subtype; campos comunes y reglas de referencias/versionado.

**Resultado:** FCM-01…09 tratados en el diseño. El esquema no se declara cerrado: falta revisión independiente, validación de tipos/constraints y prueba de no exposición de truth. No se ha generado instancia real ni inventario. Cobertura NONE, A_f*/F_alt,0/Reach_H indeterminados. Sin inspección real ni ejecución.


# XXV. Ejecución del plan — consistencia interna y cierre documental del esquema U_G (2026-11-05)

La segunda pasada detecta FCM-10…16 y corrige físicamente los encabezados de NODE, EDGE, ROUTE, PREDICATE y SNAPSHOT; establece diccionario de tipos/dominios, obligatoriedad por tabla, cardinalidades, integridad referencial y semántica de NA. CLAIM_EVIDENCE_LINK se define como relación 1:N; COVERAGE_REGISTER como fuente normativa; §7 queda como vista resumen; evaluadores E1/E2 como filas separadas.

**Resultado:** FCM-01…16 tratados documentalmente. La consistencia estática de los artefactos ha sido revisada, pero no se ha ejecutado parser, validador, constraint check, prueba de seguridad o prueba de cegamiento. No se declara esquema validado/cerrado. Revisión independiente y validación ejecutable pendientes. No hay inventario técnico ni cobertura real; no se modifica la autorización.


# XXVI. Ejecución del plan — tercera pasada de normalización relacional U_G (2026-11-05)

Se corrigen FCM-17…19: clave primaria singular de evaluación; eliminación de listas de evidencias en evaluaciones/adjudicaciones; y destino de object_id fijado como object_record_id. CLAIM_EVIDENCE_LINK permite asociar evidencias con evaluación/adjudicación concreta. Se comprueba estáticamente la alineación de columnas en diez tablas, sin errores de conteo.

**Resultado:** FCM-01…19 tratados documentalmente. La comprobación no ejecuta parser, constraints ni validadores y no prueba integridad referencial real. Esquema Draft, pendiente revisión independiente y validación técnica autorizada. Sin inventario ni cobertura real.


# XXVII. Ejecución del plan — preparación de revisión independiente del esquema U_G (2026-11-05)

Se prepara C10_S_UG_SCHEMA_INDEPENDENT_REVIEW_CHECKLIST_DRAFT_001.md con controles SR-01…20, perfiles R1 (modelo de datos/ingeniería) y R2 (metodología/causalidad), reglas de independencia/cegamiento, procedimiento y dictámenes.

**Resultado:** paquete preparado, revisión NO INICIADA. No se han designado revisores ni ejecutado validadores. Los controles SR y FCM-01…19 no se cierran por preparación documental. El freeze del esquema, selección definitiva del microdominio e inventario permanecen posteriores a revisión independiente y validación ejecutable. No cambia la autorización científica.


# XXVIII. Ejecución del plan — cuarta pasada de reconciliación semántica U_G (2026-11-05)

La revisión cruzada de la plantilla detecta contradicción entre §12.7 y §§12.9/14 sobre cardinalidad de evidence_ref y una descripción histórica ambigua de FCM-12. Se corrige: evidence_ref es 0..1 referencia de navegación opcional; CLAIM_EVIDENCE_LINK conserva la relación completa 0..n. Se distingue evaluator_record_id singular por fila E1/E2 de evaluator_record_ids plural como referencia resumida en objetos. El protocolo incorpora §16.

**Resultado:** FCM-20 registrado y tratado documentalmente; FCM-12 armonizado. Esquema sigue Draft; revisión independiente y validación ejecutable pendientes. No hay inventario ni cobertura real.


# XXIX. Reconciliación de las dos líneas de trabajo y reanudación del cierre (2026-11-05)

Se crea `C10_S_TWO_WORKSTREAMS_SCIENTIFIC_CORE_AND_COMMUNITY_SEED_WEB_DRAFT_001.md` (C10-S-WORKSTREAMS-001), que registra la orientación planteada desde la condición de investigador único hasta la apertura pública *as is* de TGCV y la posible evolución comunitaria mediante una web germen y un playground interactivo.

## 1. Dos líneas complementarias

**Línea A — científica troncal:** C10-S conserva prioridad inmediata. Su finalidad es cerrar el diseño causal sintético y evaluar si la contribución atribuible a cambios de accesibilidad puede identificarse separadamente del efecto total de la intervención y de las vías residuales. Se mantiene como microdominio previsto la migración de configuración entre dos entornos software, sin considerarlo todavía aprobado u operacionalizado.

**Línea B — web germen y playground TGCV:** línea posterior y dependiente de los contratos científicos. La web presentará TGCV *as is*, no como producto terminado ni teoría validada; expondrá arquitectura, hipótesis, estado de desarrollo, evidencias, límites, cuestiones abiertas y agenda. Permitirá a la comunidad examinar, cuestionar, replicar y proponer desarrollos. El playground podrá visualizar escenarios modelados y recorrer la cadena TGCV, pero derivará de los mismos contratos, variables y reglas; no creará un modelo paralelo ni constituirá evidencia causal por sí mismo.

## 2. Revisión y gobernanza adaptadas a investigador único

La ausencia actual de revisores externos no bloquea la consolidación documental. Se adopta como orientación una autoauditoría estructurada asistida, declarada `AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT`. Para U_G, cada control deberá registrar PASS_STATIC, CONDITIONAL, FAIL o NOT_ASSESSED, fundamento, versión, alcance y acción pendiente. No se darán por superados controles que requieran parser, constraints, motor, pruebas de seguridad, inspección técnica o validación empírica. La autoauditoría no equivale a revisión independiente ni eleva el estado científico.

La revisión externa futura se organiza en dos momentos:
1. **Preparación previa a la apertura:** claridad intelectual, coherencia, trazabilidad, separación de estados de evidencia, falsabilidad, criticabilidad, honestidad sobre limitaciones, reproducibilidad posible y seguridad/privacidad/licencias.
2. **Después de la apertura:** crítica científica, replicación, discusión de supuestos, propuestas de experimentos/extensiones, contribuciones técnicas y evolución gobernada con procedencia, autoría, versiones, desacuerdos y decisiones preservados.

La revisión previa no será una certificación académica global ni un requisito para seguir diseñando C10-S. Su alcance se ajustará a los materiales y afirmaciones que se hagan públicos. La apertura *as is* no elimina la obligación de comunicar con rigor el estado real de cada afirmación.

## 3. Playground: límites de alcance

Se registran como capacidades candidatas la visualización de dos entornos/configuraciones, estados, componentes, dependencias, restricciones, snapshots, transformaciones accesibles, rutas alternativas, Reach, trayectorias, selección/ejecución, escenarios de intervención/contrafactuales y valoración contextual de Outcome/Value. Debe mantener las distinciones entre estado de sistema y espacio transformacional; accesibilidad, aplicabilidad, Reach, selección y ejecución; estados 1/0/?; y Outcome frente a Value. La lista no es especificación funcional aprobada. No se inicia ahora diseño visual detallado ni implementación.

## 4. Reanudación del plan científico: siguiente operación

Se mantiene el orden de cierre C10-S y se retoma desde la auditoría interna de U_G, sin convertir SR-01…20 en revisión independiente ficticia:

1. Ejecutar documentalmente la autoauditoría control-a-control SR-01…20 contra la plantilla, protocolo de evidencia, contrato de frontera/granularidad, matriz U_G, snapshots, identidad, Reach y contrato DGP.
2. Para cada control, registrar PASS_STATIC, CONDITIONAL, FAIL o NOT_ASSESSED. PASS_STATIC solo acredita comprobación documental/estática; no sustituye validación ejecutable.
3. Separar expresamente los controles que requieren revisión de modelo de datos, parser/constraints, seguridad, permisos, cegamiento o validación externa. Mantenerlos abiertos/no evaluados hasta disponer del mecanismo y autorización correspondiente.
4. Reconciliar hallazgos con maestro C10-S, DGP, Decision Log, matriz de cierre, registro de pruebas y este plan, preservando referencias y estados.
5. Tras la auditoría U_G, retomar DGP y arquitectura causal: intervención autónoma sobre accesibilidad, políticas/regímenes, estimandos, vías directas/colaterales y separación de ITT/TE/contribución atribuible.
6. Continuar con validez de constructo/medición, identificación y falsación, sensibilidad y dimensionamiento estadístico.

## 5. Estado y límites

La orientación de dos líneas queda registrada en Draft. No cambia TGCV Core, RMA, Evidence→Claim Matrix, STATUS, claims, autorizaciones ni decisiones experimentales. No autoriza implementación web, playground, inspección de sistemas, generación de datos, simulación o ejecución del experimento. C10-S sigue sin aprobar, congelar ni ejecutar. La web germen no está implementada y la comunidad todavía no está constituida.

**Siguiente operación de trabajo:** comenzar la autoauditoría documental SR-01…20 de U_G, dejando para cada control evidencia, dictamen provisional y brecha restante; no pasar todavía a implementación ni al playground.


# XXX. Resultado de autoauditoría documental U_G SR-01…20 (2026-11-05)

Se completa la primera pasada documental control-a-control y se registra el expediente `C10_S_UG_SR01_20_AUTHOR_SELF_AUDIT_DRAFT_001.md`.

- Dictámenes: 8 PASS_STATIC; 10 CONDITIONAL; 2 NOT_ASSESSED; 0 FAIL.
- Modalidad: `AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT`; no es revisión externa ni independiente.
- Hallazgo transversal UG-SR-A01: aclarar la diferencia entre la exigencia de evidencia por estado en el protocolo §10 y el carácter opcional de `evidence_ref` según §16/plantilla, manteniendo CLAIM_EVIDENCE_LINK como relación 0..n.
- SR-19/20 no evaluables sin arquitectura/controles de seguridad e instancia operativa. Los demás CONDITIONAL requieren evidencia/instancias, validación ejecutable o revisión externa según control.
- No se ejecutaron validadores, parser, constraints, fixtures, inspección técnica, seguridad, cegamiento, simulación ni experimento. No se declara freeze ni cierre de esquema.

## Siguiente operación

Resolver documentalmente UG-SR-A01 en plantilla, protocolo y Test Contract Register; después completar la reconciliación de contratos U_G y continuar con DGP/arquitectura causal. La resolución documental no autoriza inspección técnica, implementación, generación, simulación ni experimento.


# XXXI. Reconciliación ampliada UG-SR-A01 — propuesta documental (2026-11-05)

La revisión directa de protocolo y plantilla amplió el hallazgo: además de protocolo §10 y §16, la discrepancia alcanza protocolo §13 y plantilla §§11/12.8. Se han registrado propuestas coordinadas en:
- plantilla U_G §12.11;
- protocolo de evidencia §17;
- Test Contract Register §53;
- autoauditoría SR-01…20 (actualización del hallazgo).

**Regla propuesta, no aprobada:** `evidence_ref` opcional 0..1; CLAIM_EVIDENCE_LINK relación canónica 0..n; vínculo obligatorio para estados 1/0; estado ? sin vínculo solo con razón de indeterminación, MISSING y limitaciones documentadas; NA con justificación. Los casos T06…T12 amplían T01…T05.

**Estado:** UG-SR-A01 sigue abierto hasta aceptación explícita. SR-03 continúa CONDITIONAL. La propuesta no cierra FCM, no valida parser/FK, no acredita inventario/cobertura y no autoriza pruebas técnicas, simulación o experimento.

## Siguiente paso

Solicitar/registrar decisión explícita sobre la regla propuesta; después, si se acepta, hacer una reconciliación final de referencias cruzadas y mantener pendiente la validación técnica. Si no se acepta, documentar la alternativa sin borrar trazabilidad de la contradicción.


# XXXII. Aceptación de UG-SR-A01 y siguiente bloque (2026-11-05)

El usuario acepta explícitamente la regla de evidencia y cardinalidad. Se armonizan plantilla §11/§12.11, protocolo §§10/13/17, Test Contract Register §§52–53, autoauditoría y maestro (§93). UG-SR-A01 queda **resuelto documentalmente**; SR-03 permanece CONDITIONAL por validación técnica pendiente. No se han ejecutado parser, FK, constraints ni pruebas, y no hay freeze ni revisión independiente.

**Siguiente paso del plan:** iniciar reconciliación de los contratos de objeto y el catálogo U_G para F1/F2/A1/A2 y F*. Primero recuperar sus definiciones canónicas, requisitos funcionales, precondiciones, entradas/salidas, restricciones, horizonte, granularidad, contexto y reglas de identidad/versionado ya presentes en el maestro y contratos; contrastarlas con los campos de NODE/EDGE/ROUTE/PREDICATE y el inventario U_G. No inventariar componentes técnicos ni asignar estados 0/1/? sin evidencia. Mantener la distinción entre catálogo de inspección y sistema real. No ejecutar inspección, implementación, simulación ni experimento.


# XXXIII. Propuesta de F* y fichas F1/F2/A1/A2 (2026-11-05)

Se ha creado `C10_S_OPTION_A_FSTAR_AND_TRANSFORMATION_CARDS_PROPOSAL_DRAFT_001.md` a partir de la reconciliación histórica y la recomendación comparativa de microdominio. El documento convierte los aliases topológicos en semánticas funcionales candidatas para la Opción A: F1 conversión focal; F2 aplicación/verificación en destino; A1 exportación neutral; A2 importación/aplicación nativa; F* contrato funcional común de esquema, integridad, compatibilidad, preservación y seguridad.

La propuesta mantiene separadas accesibilidad, aplicabilidad, ejecución, Reach y substituibilidad; B no ejecuta ninguna transformación. No se asignan formatos, versiones, tolerancias, recursos, ventanas ni estados truth. No se presenta la Opción A como aprobada: el registro canónico de microdominio la sigue marcando como recomendación no seleccionada/no aprobada. La propuesta debe compararse con el historial y someterse a decisión explícita.

**Siguiente paso:** revisión crítica de la propuesta F*/fichas, fijación de la selección del microdominio y del contrato F*; después cerrar mappings, entradas/salidas, precondiciones, tolerancias y oráculo antes de generar valores del DGP. No ejecutar ni implementar.


# XXXIV. Decisión DEC-C10-051 y continuación del cierre (2026-11-05)

Se registra la decisión explícita del usuario: Opción A (migración de configuración entre dos entornos software) queda seleccionada como microdominio de diseño y operacionalización de C10-S. F* queda adoptado como contrato funcional de trabajo candidato: producir y aplicar la configuración en destino conforme a propiedades preespecificadas de esquema, integridad, compatibilidad, preservación funcional y seguridad.

La decisión queda registrada en el documento de opciones §13, DEC-C10-051, fichas Opción A §9, decision log §45 y maestro §95. Se actualiza el estado anterior «recomendada, no seleccionada». B/C se conservan como alternativas históricas.

**No se cierra:** lista de propiedades F*, mappings, tolerancias, casos frontera, oráculo, TID/SID/RID, C0/G/H, recursos/ventanas, cobertura de rutas, D1/D2, R0–R3, DGP, estimandos ni identificación. No hay aprobación de ejecución ni validación técnica/empírica/revisión independiente.

**Siguiente bloque:** completar el contrato de F* por propiedades observables y reglas de adjudicación; especificar para F1/F2/A1/A2 los contratos de entrada/salida, precondiciones, invariantes, fallos y mapping; definir un oráculo independiente ciego a Z/B y separado de Outcome/Value. Después reconciliar el catálogo de roles U_G con estas fichas y actualizar DGP/estimandos sin asignar truth no sustentada.


# XXXV. Matriz operacional de F* y reconciliación de estado (2026-11-05)

Se crea `C10_S_FSTAR_OPERATIONAL_PROPERTY_AND_ADJUDICATION_MATRIX_DRAFT_001.md`, con familias FP-01…FP-08, regla trivalente no compensatoria, evaluación diferenciada por etapa, requisitos del oráculo y condiciones de equivalencia funcional de rutas.

**Dictamen:** F* queda definido a nivel de familias de propiedades y lógica de adjudicación; no está cerrado a nivel de predicados atómicos ni validado. Permanecen abiertos dominio de entrada, invariantes exactas, mappings, contratos/versiones, tolerancias, H/G/C0, reglas NA, oráculo, error/cegamiento y cobertura de alternativas.

**Reconciliación de texto histórico:** el bloque XXXIII de este plan y el maestro §94 conservan la formulación previa a DEC-C10-051 («Opción A no seleccionada/no aprobada»). Se preservan como registro del estado en el momento de su redacción; para el estado vigente prevalecen el bloque XXXIV, el maestro §95 y DEC-C10-051. No hay contradicción decisional vigente: Opción A está seleccionada para diseño, no autorizada para ejecución.

**Siguiente paso:** cerrar el catálogo de propiedades atómicas y las reglas de mapping/preservación, empezando por FP-03 (semántica) y FP-01/FP-02 (estructura e integridad), y definir los criterios de seguridad FP-05. Después concretar los contratos de F1/F2/A1/A2 y el oráculo. No generar truth del DGP ni ejecutar.


# XXXVI. Desarrollo de FP-03 — preservación semántica (2026-11-05)

Se crea `C10_S_FP03_SEMANTIC_PRESERVATION_CONTRACT_DRAFT_001.md`, complementario a la matriz F*. La propuesta define diez dimensiones semánticas de inspección (SM-01…SM-10), tipos de correspondencia, diferencias representacionales frente a pérdidas, regla de adjudicación y requisitos de evidencia.

**Criterio:** preservar significado funcional declarado, no bytes/nombres/hashes; comparar origen y estado realmente aplicado en destino bajo contrato, C0, G y H preespecificados. El criterio es acotado al dominio, no equivalencia universal. No se crea una capa semántica persistida paralela.

**Cautela de alcance:** DEC-C10-051 selecciona el microdominio y adopta F* de trabajo, pero no aprueba por inferencia los mecanismos técnicos específicos de F1/F2/A1/A2. Sus fichas actuales conservan carácter de roles candidatos hasta reconciliación y decisión explícita.

**No cerrado:** dominio de configuración, invariantes atómicas, obligatoriedad de SM, mapping, excepciones, envolvente de observación, tolerancias, oráculo y fiabilidad. No hay ejecución ni evidencia empírica.

**Siguiente paso:** fijar el objeto/configuración y el dominio funcional mínimo del microdominio, para poder convertir SM-01…SM-10 en predicados atómicos sin inventar semánticas. A continuación, seleccionar qué propiedades son obligatorias y cerrar mappings/oráculo; después reconciliar contratos concretos F1/F2/A1/A2.


# XXXVII. Delimitación del objeto de configuración (2026-11-05)

Se crea `C10_S_CONFIGURATION_OBJECT_SCOPE_AND_MINIMUM_CONTRACT_PROPOSAL_DRAFT_001.md`, que compara tres clases de objeto para la Opción A y recomienda un paquete de configuración de servicio software. La propuesta define un contenido lógico mínimo (componente, parámetros tipados, referencias, reglas/restricciones, políticas asociadas y metadatos contractuales), separa el objeto de recursos/permisos/ventanas/estado del entorno y deriva un F* candidato.

**Estado:** propuesta pendiente de decisión explícita; no modifica DEC-C10-051 ni fija un sistema/producto/formato. No se aprueban todavía los mecanismos concretos F1/F2/A1/A2. No hay validación técnica ni evidencia.

**Siguiente paso:** decisión del usuario sobre la clase del objeto y, si acepta la candidata A, sobre el contenido lógico mínimo y las propiedades obligatorias. Tras esa decisión se especializarán SM-01…SM-10, se definirán mappings y predicados atómicos, y se reconciliarán las fichas de transformaciones con el historial sin inventar mecanismos.


# XXXVIII. DEC-C10-052 — selección del objeto de configuración (2026-11-05)

El usuario confirma adoptar la clase A, **paquete de configuración de un servicio software**, como objeto concreto de trabajo dentro de Opción A. Se adoptan como estructura conceptual inicial los seis elementos: componente; parámetros tipados; referencias; reglas/restricciones; políticas asociadas; metadatos contractuales.

La decisión se registra en `C10_S_CONFIGURATION_OBJECT_SCOPE_AND_MINIMUM_CONTRACT_PROPOSAL_DRAFT_001.md` y en el decision log §46. La propuesta pasa a ser objeto seleccionado para diseño documental, pero no se convierte en esquema final ni en contrato confirmatorio congelado.

**Siguiente bloque:** especializar SM-01…SM-10 para este objeto; decidir propiedades obligatorias/condicionales/NA; definir invariantes semánticas y estructurales atómicas, mappings y diferencias permitidas; mantener recursos, permisos efectivos, dependencias instaladas y estado de los entornos fuera del objeto migrado; reconciliar después F1/F2/A1/A2 con evidencia histórica. No asignar truth DGP ni ejecutar.


# XXXIX. Primera atomización del objeto de configuración (2026-11-05)

Se crea `C10_S_CONFIGURATION_OBJECT_ATOMIC_PROPERTY_CATALOG_DRAFT_001.md`, con propiedades candidatas para los seis elementos seleccionados por DEC-C10-052 y trazabilidad a SM-01…SM-10 y FP-01…FP-08.

**Resultado:** primera descomposición de CMP/PAR/REF/RUL/POL/MET; diferenciación de propiedades centrales y condicionales; regla trivalente y límites de no duplicación entre familias FP.

**No cerrado:** dominio abstracto concreto, contratos fuente/destino, taxonomías, semántica de parámetros/reglas, inclusión de políticas, obligatoriedad y NA por propiedad, mappings, tolerancias, cobertura y oráculo. No hay ejecución ni validación.

**Siguiente paso:** decidir el alcance mínimo del DGP base (qué dimensiones SM son constitutivas del paquete y cuáles quedan condicionales/adversariales) y definir un contrato abstracto fuente/destino que permita fijar predicados atómicos y mappings sin elegir tecnología real. Mantener la política de seguridad FP-05 diferenciada de la preservación FP-03.


# XL. Alcance del DGP base y contrato abstracto fuente/destino (2026-11-05)

Se crea `C10_S_BASE_DGP_SCOPE_AND_ABSTRACT_CONFIGURATION_CONTRACT_PROPOSAL_DRAFT_001.md` como siguiente derivación de DEC-C10-052 y del catálogo CMP/PAR/REF/RUL/POL/MET.

**Recomendación para deliberación:** cuatro familias constitutivas en el DGP base (componentes, parámetros tipados, referencias y reglas/restricciones con gramática mínima); políticas asociadas como módulo condicional; metadatos contractuales obligatorios para identidad/procedencia, con extensiones desconocidas en escenarios condicionales. La estructura conceptual de seis elementos permanece intacta: la propuesta no elimina políticas, sino que permite declarar ex ante su ausencia en el escenario base y examinarlas en escenarios secundarios.

Se estructuran C_src, C_dst y M y se proponen predicados base para correspondencia de componentes, tipos/valores/estados de parámetros, extremos/relaciones de referencias, lógica de reglas, cobertura del mapping y estado realmente aplicado. Son predicados candidatos, sin dominios ni truth.

**No cerrado:** decisión sobre la partición; gramática de reglas; cardinalidades; taxonomías; semántica de ausencia/null/default; mapping; propiedades obligatorias; oráculo; reconciliación F1/F2/A1/A2; DGP completo y parámetros. No hay validación técnica, revisión independiente, evidencia empírica ni ejecución.

**Siguiente paso:** deliberar y registrar explícitamente el alcance del DGP base. Solo después formalizar el contrato abstracto con dominios finitos y mappings permitidos, revisar los contratos de transformación y actualizar DGP/estimandos. No generar truth ni ejecutar.


# XLI. DEC-C10-053 — partición aprobada y siguiente formalización (2026-11-05)

El usuario aprueba la partición del DGP base: CMP/PAR/REF/RUL constitutivos; POL condicional, fuera del núcleo confirmatorio mínimo; metadatos contractuales obligatorios para identidad/versionado/procedencia, con extensiones desconocidas condicionales. Se conserva la estructura conceptual de seis elementos de DEC-C10-052; POL no se elimina, y su ausencia en el escenario base deberá declararse ex ante.

**Siguiente bloque:** definir gramática declarativa mínima y finita de reglas/restricciones y dominio abstracto de tipos/parámetros. No se fijan aún cardinalidades, semántica de null/default, mappings, tolerancias ni oráculo. No generar truth ni ejecutar.


# XLII. Gramática mínima y dominio de tipos (2026-11-05)

Se crea `C10_S_MINIMAL_RULE_GRAMMAR_AND_PARAMETER_TYPE_DOMAIN_PROPOSAL_DRAFT_001.md`, con propuesta de tipos abstractos BOOL/INT/DECIMAL/ENUM/STRING/REF, estados ABSENT/NULL/DEFAULT/VALUE, operadores declarativos y semántica TRUE/FALSE/UNKNOWN, diferenciada de la evidencia 1/0/?.

**No cerrado:** dominios y límites finitos, profundidad/tamaño de expresiones, efectos, precedencia, política UNKNOWN, conversiones y oráculo. No ejecutar ni generar truth.

**Siguiente paso:** deliberar la gramática y fijar un dominio mínimo de valores y límites para el escenario base; después especificar mapping y reconciliar FP-01/02/03.


# XLIII. Perfil de dominios finitos y complejidad de reglas (2026-11-05)

Se crea `C10_S_FINITE_DOMAIN_AND_RULE_COMPLEXITY_PROFILE_PROPOSAL_DRAFT_001.md` como desarrollo de §XLII y DEC-C10-053. La propuesta establece dominios finitos por clave de parámetro (sin rangos universales arbitrarios), representación decimal escalada, catálogos ENUM/REF cerrados, STRING acotado, separación de ABSENT/NULL/DEFAULT/VALUE y subtipos de DEFAULT. Propone AST declarativo acíclico, operadores tipados, profundidad 4, 16 átomos/regla y 16 reglas/paquete como presupuesto candidato; limita efectos del núcleo a REQUIRE/FORBID y excluye SELECT_ENUM_VALUE por su potencial mutativo. Define propagación de UNKNOWN a F* sin equipararlo a FALSE.

**Estado:** propuesta no aprobada ni congelada. Los límites 4/16/16 no están calibrados; dominios por clave, cadenas, escalas, reglas de conflicto, UNKNOWN, mapping y oráculo siguen abiertos. No se crean fixtures ni truth; no hay validación técnica, revisión independiente, evidencia empírica ni ejecución.

**Siguiente paso:** revisión crítica del perfil y decisión explícita sobre el presupuesto de complejidad y los efectos permitidos. Después, construir el contrato abstracto de parámetros por clave y la matriz de mapping fuente/destino, reconciliando FP-01/FP-02/FP-03 y evitando doble conteo. No elegir todavía valores concretos de configuración ni ejecutar.


# XLIV. DEC-C10-054 — perfil finito aprobado y transición a mapping (2026-11-05)

El usuario aprueba el perfil estructural de dominios finitos por clave, el presupuesto 4/16/16, el AST acíclico y declarativo, los operadores tipados, los efectos REQUIRE/FORBID y la exclusión de SELECT_ENUM_VALUE del núcleo. Se aprueba la distinción de estados/defaults y la regla de no convertir UNKNOWN silenciosamente en TRUE/FALSE.

La aprobación no fija valores concretos por parámetro ni calibra empíricamente los límites. Se actualiza el estado del perfil a APROBADO en su dimensión estructural; dominios concretos, mapping, conflictos, tolerancias y oráculo permanecen abiertos.

**Siguiente bloque:** matriz abstracta de parámetros y mapping C_src→C_dst/M, enlazando cada propiedad con FP-01/02/03 y asignando un predicado primario para evitar doble conteo. No generar valores, truth, fixtures ni ejecutar.


# XLV. Matriz abstracta de parámetros y mapping fuente/destino (2026-11-05)

Se crea `C10_S_ABSTRACT_PARAMETER_AND_SOURCE_DESTINATION_MAPPING_MATRIX_DRAFT_001.md`. La matriz define el contrato por clave de parámetro, la relación C_src→C_dst mediante M, la correspondencia por familias CMP/PAR/REF/RUL/POL/MET, el tratamiento de ABSENT/NULL/DEFAULT/VALUE, las conversiones tipadas y predicados candidatos separados por FP-01/02/03. Distingue C_dst declarado de C_dst realmente aplicado y mantiene E_dst fuera del objeto migrado.

**Estado:** propuesta documental; no fija claves, valores, dominios concretos, obligatoriedad/NA final ni mappings reales. Los predicados son candidatos sujetos a reconciliación con SM-01…SM-10 y el catálogo atómico. No hay truth, fixtures, validación, revisión independiente, evidencia empírica ni ejecución.

**Siguiente paso:** reconciliar matriz con SM-01…SM-10 y catálogo CMP/PAR/REF/RUL/POL/MET; producir tabla de correspondencia predicado→FP primario/secundario, identificar duplicidades y decidir obligatoriedad/NA ex ante. Después, especializar contratos F1/F2/A1/A2 y el oráculo F*. No elegir aún valores ni ejecutar.


# XLVI. Reconciliación SM-01…SM-10 y familias FP (2026-11-05)

Se crea `C10_S_SM_ATOMIC_PROPERTY_FP_RECONCILIATION_DRAFT_001.md`. La revisión detecta solapamientos entre la primera matriz C_src→C_dst/M y el catálogo atómico: propiedades compuestas se desdoblan entre validez formal FP-01, integridad FP-02 y preservación semántica FP-03. Se fijan además las fronteras FP-04 compatibilidad, FP-05 seguridad, FP-06 aplicación, FP-07 observación post-aplicación y FP-08 procedencia.

Hallazgos clave: CMP-01/02 y PAR-01 son semánticos FP-03; PAR-02 se divide entre esquema FP-01 y significado FP-03; REF-01/02 semánticos FP-03, REF-04 integridad FP-02; reglas RUL son semánticas FP-03 y validez AST FP-01; POL es condicional FP-03 y seguridad efectiva FP-05; MET-01 FP-01/04, MET-02/04 FP-08 y MET-03 condicional FP-03. C_dst^applied se evalúa mediante FP-06/07 sin crear doble conteo semántico.

**Estado:** reconciliación propuesta, no confirmatoria ni aprobada. Obligatoriedad/NA por instancia, cardinalidades, dominios, mapping, F1/F2/A1/A2 y oráculo siguen abiertos. Sin validación técnica, revisión independiente, evidencia empírica ni ejecución.

**Siguiente paso:** revisar la asignación de predicados primarios/secundarios y cerrar obligatoriedad/NA ex ante en el contrato abstracto antes de especializar F1/F2/A1/A2.


# XLVII. DEC-C10-055 y matriz de obligatoriedad/aplicabilidad ex ante (2026-11-05)

El usuario acepta la reconciliación SM/FP. Se registra DEC-C10-055: FP-01 estructura formal; FP-02 integridad relacional; FP-03 preservación semántica; FP-04 compatibilidad; FP-05 seguridad; FP-06 aplicación; FP-07 verificación post-aplicación; FP-08 procedencia/reproducibilidad. Se mantiene un predicado primario por discrepancia y se prohíbe el doble conteo.

Se crea `C10_S_PROPERTY_APPLICABILITY_AND_OBLIGATORINESS_MATRIX_DRAFT_001.md`. Propone un Instance Applicability Manifest (IAM) sellado antes de Z/B; reglas O/C/NA/? para cada propiedad atómica; declaración de cardinalidad y cobertura; criterios de scope error; separación F* funcional, gates FP-04/05/06 y FP-08 probatorio; controles contra decisiones post hoc.

**Estado:** DEC-C10-055 aceptada; matriz propuesta, no aprobada ni congelada. Abiertos: cardinalidad cero de REF/RUL, alcance FP-04/05/06 dentro de F*, activación de CMP-02/PAR-05, seguridad, conflictos RUL, diseño IAM y evidencia de cobertura. No hay instancia IAM, truth, fixtures, validación, revisión independiente, evidencia empírica ni ejecución.

**Siguiente paso recomendado:** revisión crítica de las reglas de cardinalidad y de la frontera F* frente a FP-04/05/06; resolverlas antes de especializar F1/F2/A1/A2 y el oráculo.


### XLVII-A. Precisión de frontera F* / FP-08

La matriz IAM se ha precisado para mantener F* como capacidad funcional de ruta completa, coherente con su contrato candidato de producción y aplicación en destino: FP-01…FP-07 pueden integrar su adjudicación por dimensiones separadas y no compensatorias. FP-08 es gate de validez probatoria separado. POL ausente por diseño no elimina requisitos de seguridad FP-05 que formen parte de F*; estos se declaran independientemente de POL. Esta precisión evita reducir F* a preservación interna del paquete.


# XLVIII. DEC-C10-056 y contrato abstracto de instancia (2026-11-05)

El usuario acepta la política de cardinalidad: CMP≥1, PAR≥1, REF≥0 solo con declaración ex ante y cobertura exhaustiva, RUL≥1, POL≥0 ausente por diseño en el núcleo mínimo y MET obligatorio. CMP/PAR/RUL vacíos son SCOPE_ERROR; REF vacío no se infiere de falta de evidencia.

Se registra DEC-C10-056 y se crea `C10_S_ABSTRACT_CONFIGURATION_INSTANCE_CONTRACT_DRAFT_001.md`, que formaliza estructura C=(ID_C,V_C,CMP,PAR,REF,RUL,POL?,MET), entidades abstractas, correspondencia C_src→M→C_dst_decl→C_dst_applied, invariantes y límites. No fija valores, claves concretas, topología, reglas sustantivas ni schema ejecutable.

**Estado:** cardinalidad aprobada; contrato abstracto Draft 001 no aprobado/congelado/implementado. Pendiente especializar frontera/unidad de servicio, clases CMP, claves PAR, tipos de REF, reglas RUL, mapping, cobertura REF=0 y oráculo. Sin IAM instanciado, truth, fixtures, validación técnica, revisión independiente, evidencia empírica ni ejecución.

**Siguiente paso:** definir la frontera de la unidad de configuración del servicio software y el criterio de inclusión/exclusión de componentes/dependencias, sin asignar todavía valores concretos.


# XLIX. Perfil de frontera del servicio software P0/P1/P2 (2026-11-05)

Se completa el paso de diseño documental de una primera propuesta de frontera para el objeto de Opción A. El documento `C10_S_SOFTWARE_SERVICE_CONFIGURATION_BOUNDARY_PROFILE_PROPOSAL_DRAFT_001.md` separa: P0 paquete declarativo migrable C; P1 envolvente técnica E_src/E_dst; P2 sistema causal de la unidad, que integra P0/P1, B, alternativas, dependencias compartidas, medición, ejecución y Outcomes/Value pertinentes.

La propuesta define criterios de inclusión/exclusión y casos límite (endpoints, secretos, políticas, permisos efectivos, runtime, datos persistentes, esquemas, mapping, sidecar, A1/A2 y oráculo). No sustituye el contrato genérico de frontera ni U_G §81–82; los especializa para decisión.

**Estado:** propuesta no aceptada ni congelada. Pendiente decisión P0/P1/P2 y concreción de servicio lógico, deployment manifests/variables, secretos, datos persistentes, servicios externos opacos, snapshots y unidad experimental. No hay inventario real, IAM instanciado, truth, fixtures, validación, instalación, simulación ni ejecución.

**Siguiente paso tras aceptación:** convertir la arquitectura de frontera en un contrato de clasificación por elemento y preparar el formulario de inventario para el dominio, manteniendo los registros técnicos en ?/NONE hasta disponer de evidencia autorizada.


# L. DEC-C10-057 y especialización de unidad lógica (2026-11-05)

Se acepta la arquitectura P0/P1/P2 y la regla de clasificación semántica (DEC-C10-057). P0 contiene la configuración declarativa migrable; P1 la realización/estado técnico de los entornos; P2 es la frontera causal transversal. La aceptación no clasifica automáticamente todos los elementos concretos ni implica inventario o freeze.

Se crea `C10_S_LOGICAL_SERVICE_UNIT_AND_BOUNDARY_CLASSIFICATION_PROPOSAL_DRAFT_001.md`, con definición candidata de servicio lógico, criterios de inclusión, clasificación campo a campo de deployment manifests y variables, tratamiento de secretos/datos persistentes/migraciones de esquema, servicios opacos, mapping, sidecar B y oráculo. Sigue pendiente de decisión y de reconciliación con unidad de aleatorización/interferencia.

**Siguiente paso:** revisar la definición de servicio lógico y resolver los casos de frontera para aprobar la unidad candidata antes de construir el IAM de inventario.


# LI. DEC-C10-058 — aceptación de unidad lógica y clasificación semántica (2026-11-05)

Se registra DEC-C10-058 como aceptación de la unidad de migración (instancia lógica de servicio software) y de las reglas de clasificación P0/P1/P2 del documento `C10_S_LOGICAL_SERVICE_UNIT_AND_BOUNDARY_CLASSIFICATION_PROPOSAL_DRAFT_001.md`.

Quedan resueltos a nivel conceptual: manifests y variables por campo/clave; secretos solo como referencia en P0 y material real fuera; datos persistentes fuera de P0 por defecto; migraciones de esquema separadas de F* base; servicios externos opacos retenidos en P2 con incertidumbre; unidad de migración lógica no equiparada a unidad de aleatorización.

**Siguiente bloque:** construir el contrato de inventario abstracto IAM a partir de la taxonomía U_G ya existente, reutilizando su estructura y evitando duplicar NODE/EDGE/ROUTE/PREDICATE/EVIDENCE/COVERAGE. Antes, realizar reconciliación histórica con IAM/plantilla y contratos existentes. No instanciar datos reales ni generar truth/fixtures.


# LI. DEC-C10-058 — aceptación de unidad lógica y clasificación semántica (2026-11-05)

Se registra DEC-C10-058 como aceptación de la unidad de migración (instancia lógica de servicio software) y de las reglas de clasificación P0/P1/P2 del documento `C10_S_LOGICAL_SERVICE_UNIT_AND_BOUNDARY_CLASSIFICATION_PROPOSAL_DRAFT_001.md`.

Quedan resueltos a nivel conceptual: manifests y variables por campo/clave; secretos solo como referencia en P0 y material real fuera; datos persistentes fuera de P0 por defecto; migraciones de esquema separadas de F* base; servicios externos opacos retenidos en P2 con incertidumbre; unidad de migración lógica no equiparada a unidad de aleatorización.

# LII. Reconstrucción histórica y overlay IAM (2026-11-05)

Tras DEC-C10-058 se realizó reconstrucción histórica obligatoria de la plantilla U_G, protocolo de evidencia/adjudicación, matriz de cobertura trivalente, contrato de frontera/granularidad, manifiesto B y contratos de identidad/snapshots. El trabajo previo es reutilizable y cubre los diez registros canónicos U_G.

No se recrea una plantilla ni se amplía el inventario por duplicado. Se crea `C10_S_IAM_SERVICE_BOUNDARY_OVERLAY_AND_CROSSWALK_DRAFT_001.md` como overlay específico del servicio lógico. Define clasificación P0/P1, pertenencia/relaciones P2, crosswalk con registros U_G y mapping funcional provisional FP-01…08.

**Pendiente:** revisar/aceptar el overlay; reconciliar FP-01…08 con contratos canónicos; validar los tipos EDGE frente al catálogo existente; fijar campos/cardinalidades/FK; después actualizar la plantilla existente solo si la brecha concreta lo exige. Sin instanciación ni ejecución.


# LIII. Auditoría FP/EDGE del overlay IAM (2026-11-05)

Se realiza auditoría documental contra contratos históricos. El overlay general es compatible con U_G y DEC-C10-055, pero requiere correcciones antes de modificar la plantilla: predicados primarios/secundarios por propiedad; FP-07 post-aplicación; FP-08 separado como procedencia/reproducibilidad; no introducir CONTAINS_FIELD; resolver atributos overlay frente a columnas existentes; separar C_dst^decl, C_dst^applied, E_dst y M.

Artefacto: `C10_S_IAM_FP_EDGE_CROSSWALK_AUDIT_DRAFT_001.md`. La auditoría es auto-revisión asistida no independiente. No se ejecutan validadores ni se instancian nodos/aristas. Próxima operación: aplicar correcciones al overlay y producir field-to-column crosswalk mínimo; solo después decidir si la plantilla U_G necesita cambios.


# LIV. Crosswalk de atributos IAM a esquema U_G (2026-11-05)

Tras la auditoría FP/EDGE se ha contrastado cada atributo propuesto del overlay con U_G §§2–6 y 10–12. La mayoría se representa mediante columnas/relaciones existentes: NODE raíz + SNAPSHOT.unit_id para unidad lógica; semantic_role para object_scope; notes/unknowns para rationale; confidentiality/access_ref en EVIDENCE_REGISTER para sensibilidad; parent_catalog_id para linaje de catálogo. P2 permanece como frontera causal transversal.

Se identifica una única extensión candidata clara: NODE.boundary_class (P0_CONFIG/P1_ENVIRONMENT/DUAL_P0_P1), sin sobrecargar NODE.class ni semantic_role. No se modifica la plantilla. Documento: `C10_S_IAM_FIELD_TO_COLUMN_CROSSWALK_PROPOSAL_DRAFT_001.md`.

**Decisión pendiente del usuario:** aceptar/rechazar la extensión NODE.boundary_class y su dominio/restricciones. También queda pendiente cerrar la FK entre SNAPSHOT.unit_id y NODE.node_id. No se ha añadido schema ni se han instanciado filas.
