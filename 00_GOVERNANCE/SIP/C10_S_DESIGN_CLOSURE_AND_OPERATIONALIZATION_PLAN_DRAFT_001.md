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

