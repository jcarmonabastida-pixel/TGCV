# C10-S — Plan integral de cierre del diseño y operacionalización

**ID:** C10-S-PLAN-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-04
**Estado:** DRAFT / NO APROBADO / NO CONGELADO.

Este documento consolida el diagnóstico, los artefactos y el plan de cierre de C10-S. La auditoría y el plan detallado se incorporarán en actualizaciones sucesivas de este mismo archivo.


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
| HEAD | d007a877b25caec72643b2efbaca0f7cf8eb7ea5 |
| Base | research/c10-d1-protocol-draft |
| Commits | 184 |
| Archivos | 13 |
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

