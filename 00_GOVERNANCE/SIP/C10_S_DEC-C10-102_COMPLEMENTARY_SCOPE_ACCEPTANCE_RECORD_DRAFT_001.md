# C10-S — Registro de aceptación del complemento de alcance a DEC-C10-102

**Fecha:** 2026-11-16  
**Estado:** ACCEPTED_FOR_CURRENT_SYNTHETIC_DGP_LOGICAL_SCOPE.  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft.  
**Autoridad:** aceptación expresa del responsable científico en la conversación de trabajo, tras presentación íntegra de C1–C6.

## 1. Acto de aceptación

Se aceptan conjuntamente, sin reservas parciales, las seis cláusulas C1–C6 de:

`00_GOVERNANCE/SIP/C10_S_DEC-C10-102_COMPLEMENTARY_SCOPE_DECISION_PROPOSAL_DRAFT_001.md`.

La aceptación se limita al alcance lógico/normativo del DGP sintético vigente. No constituye aceptación de parámetros temporales, materialización, implementación, ejecución ni Design Freeze.

## 2. Efecto normativo

1. Para DEC-C10-099…102 y V_cont, A_B1 adjudica el comportamiento efectivo de admisión/no-admisión requerido por ENABLED, incluida disponibilidad operativa/runtime constitutiva cuando impide ese comportamiento.
2. ENABLED=true exige admisión efectiva; ENABLED=false exige no-admisión efectiva. El estado declarativo no prueba por sí mismo el comportamiento.
3. PROFILE sigue siendo configuración declarativa versionada y obligación contractual. PROFILE exposure no se adjudica temporalmente mediante V_cont en el DGP actual; no se infiere de la admisión ni se convierte en UNKNOWN.
4. D_valid se evalúa separadamente conforme a RUL-SVC-ENABLE-PROFILE-01. La no conformidad declarativa se trata como no conformidad del Generator/DGP o escenario negativo/adversarial versionado, no como A_B1=0/UNKNOWN automático. El soporte confirmatorio primario deberá ser conforme.
5. EventHistory incorpora solo transiciones truth del DGP vigente que puedan alterar la admisión requerida. No se crean eventos autónomos de PROFILE exposure ni se confunden logs/observaciones con truth.
6. Se preservan sin modificación el operador estricto de DEC-C10-102, las reglas temporales DEC-C10-100/101/104 y la semántica trivaluada {1,0,?}. UNKNOWN solo representa indeterminación funcional intrínseca expresamente generada; nunca falta de observación, defectos del harness, missingness S3, PROFILE no representado o D_valid no conforme.
7. V_cont se interpreta exclusivamente como continuidad temporal de la función efectiva de admisión B1 en el DGP sintético vigente; no como cumplimiento íntegro de todas las obligaciones B1 ni como Value contextual general.

## 3. Precedencia y conservación

Este registro formaliza la composición de Gate 154 con R150-A, R151-A8, R152-A y R208-A. No modifica ni sustituye DEC-C10-102 ni DEC-C10-099…104; no crea DEC-C10-105. Se conserva íntegra la historia y el texto de las decisiones previas. La aceptación no extiende el DGP más allá de sus mecanismos actuales.

## 4. Alcance de cierre

**CLOSED_FOR_CURRENT_SYNTHETIC_DGP_LOGICAL_SCOPE:** crosswalk normativo DEC-C10-102 / Gate 154 / R150-A / R151-A8 / R152-A / R208-A.

Permanecen abiertos: §51, reloj, soporte, T*, Δ, K, resolución, S3, EventHistory/IntervalAdjudication/TruthBundle materializados, D2, población, asignación, aislamiento, soporte causal, q_X*, g_A0/g_A1, r_common, θ_A, Outcome/Value, potencia, N/R, tests, firewall técnico y Design Freeze.

## 5. Autorizaciones

Esta aceptación **no** autoriza cambios de código/schema/fixtures/tests, validadores, generación de datos, simulación, estimación, calibración, Monte Carlo ni ejecución científica. Tampoco promueve artefactos a main.

`scientific_execution=false`  
`execution_authorized=false`  
`implementation_authorized=false`
