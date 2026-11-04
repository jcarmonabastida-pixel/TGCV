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
