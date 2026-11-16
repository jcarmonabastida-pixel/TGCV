# C10-S — Propuesta de complemento normativo a DEC-C10-102: alcance temporal de A_B1 y V_cont

**Fecha:** 2026-11-16  
**Estado:** PROPOSED_FOR_EXPLICIT_ACCEPTANCE / NOT_AN_ACCEPTED_DECISION / NO_DESIGN_FREEZE.  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft).  
**Tipo:** propuesta de decisión complementaria; DEC-C10-102 y las decisiones históricas permanecen inalteradas.

## 1. Pregunta normativa

Resolver la composición de dos obligaciones ya aceptadas sin borrar ninguna:

- R150-A: B1 exige (i) comportamiento de admisión/no-admisión conforme a ENABLED y (ii) exposición del PROFILE declarado, tanto con ENABLED=true como con ENABLED=false.
- R151-A8: PROFILE exposure permanece obligación contractual, pero el DGP vigente no genera una trayectoria temporal independiente que permita adjudicar su continuidad; no puede inferirse de la admisión ni convertirse en UNKNOWN.
- Gate 154, aceptado expresamente: A_B1/V_cont adjudica temporalmente la función de admisión/no-admisión exigida por ENABLED, incluyendo la disponibilidad runtime que la hace posible; PROFILE exposure queda fuera de la dimensión temporal adjudicada por V_cont en el DGP vigente.
- R208-A1…A6, aceptada expresamente: PROFILE se conserva como configuración declarativa versionada; D_valid se evalúa separadamente; no se inventa una trayectoria de exposición; el runtime solo integra EventHistory si es constitutivo y puede alterar efectivamente la admisión.

La tensión no se resuelve modificando el operador estricto de DEC-C10-102, sino delimitando el predicado funcional temporal al que se aplica conforme a Gate 154.

## 2. Texto decisional propuesto

Se propone adoptar el siguiente complemento, sin modificar ni sustituir DEC-C10-102:

### C1 — Precedencia y alcance de la adjudicación temporal

Para el DGP sintético vigente, y a efectos exclusivos de DEC-C10-099…102 y de la medida V_cont, el predicado temporal A_B1 comprende el comportamiento efectivo de admisión/no-admisión requerido por el estado declarativo ENABLED, incluida la disponibilidad operativa y los mecanismos runtime constitutivos cuando su estado impide realizar ese comportamiento.

Esta delimitación aplica la aceptación posterior y expresa de Gate 154. No modifica el operador de continuidad estricta ni las reglas de intervalo de DEC-C10-100, DEC-C10-101, DEC-C10-102 y DEC-C10-104.

### C2 — Regla funcional de ENABLED

- Si ENABLED=true, el comportamiento requerido es admitir conforme al contrato B1. Una incapacidad runtime funcionalmente confirmada que impida esa admisión constituye incumplimiento durante el soporte temporal afectado.
- Si ENABLED=false, el comportamiento requerido es no admitir. La no-admisión es cumplimiento; la admisión efectiva constituye incumplimiento.
- No se presume que el valor declarativo ENABLED, por sí solo, demuestre disponibilidad operativa o admisión efectiva.

### C3 — PROFILE y D_valid

PROFILE continúa siendo configuración declarativa versionada y obligación contractual de B1, incluso cuando ENABLED=false. Su valor y sus cambios declarativos se preservan en EventHistory con identidad, versión y estado anterior/posterior según el contrato lógico aceptado.

PROFILE exposure no forma parte del predicado temporal A_B1 adjudicado por V_cont en el DGP actual, porque no existe una trayectoria truth independiente que permita evaluar su continuidad. No se inferirá su exposición a partir de la admisión, ni se declarará satisfecha por continuidad de V_cont, ni se convertirá su falta de representación en UNKNOWN funcional.

D_valid se evalúa separadamente sobre cada estado declarativo conforme a RUL-SVC-ENABLE-PROFILE-01. Una configuración no conforme es una no conformidad del Generator/DGP o un escenario negativo/adversarial separado y versionado; no se recodifica automáticamente como A_B1=0 ni como UNKNOWN funcional. El soporte confirmatorio primario deberá satisfacer la RUL en todos los estados declarativos generados.

### C4 — Runtime constitutivo y EventHistory

Solo se incorporan a EventHistory como transiciones funcionales los mecanismos ya contemplados en el DGP vigente que estén declarados/versionados en la instancia y cuyo estado pueda alterar efectivamente la admisión requerida, manteniendo explícitas las demás condiciones. Logs, telemetría, intentos, antecedentes y señales de observación no son por sí mismos truth funcional.

EventHistory representa la historia sintética generada, no PROCESS_EVENT ni el canal de evidencia. Se preservan R144-A, R146-A…D, la separación de roles y el versionado/completitud. No se crea una transición autónoma de PROFILE exposure.

### C5 — Operador estricto y estados de verdad

Se preservan íntegramente el operador estricto de DEC-C10-102 y los estados {1,0,?}:

- 1: el comportamiento temporal de admisión/no-admisión definido en C1–C2 se cumple durante todo el intervalo.
- 0: existe al menos un incumplimiento funcional confirmado de ese comportamiento en cualquier instante del intervalo.
- ?: únicamente cuando el Generator define explícitamente una indeterminación intrínseca de la truth funcional, bajo el contrato y provenance exigidos por DEC-C10-100/104.

S3 missingness, lag, error o cobertura insuficiente; defectos del harness/EventHistory; falta de observación; PROFILE exposure no representada; y no conformidad declarativa D_valid no se transforman en UNKNOWN funcional. El Analyzer deberá producir bounds o abstenerse cuando la observación no permita recuperar la truth.

### C6 — Límite de la afirmación

V_cont, bajo este alcance, representa exclusivamente continuidad temporal de la función efectiva de admisión B1 en el DGP sintético vigente. No representa cumplimiento íntegro de todas las obligaciones contractuales B1, continuidad de PROFILE exposure, disponibilidad bajo cargas no especificadas ni Value contextual general de TGCV.

La obligación contractual de PROFILE exposure permanece vigente, pero su adjudicación temporal queda fuera del soporte del experimento actual. Cualquier futura ampliación que pretenda medirla requerirá una modificación explícita y aprobada del DGP, mecanismo truth independiente y decisión normativa propia.

## 3. Justificación y alternativas descartadas

Esta propuesta:
- preserva el operador estricto ya aceptado; no introduce gracia, tolerancia ni promedio;
- aplica la delimitación de Gate 154 sin reinterpretarla como modificación retroactiva;
- preserva R150-A como obligación contractual y R151-A8 como límite de adjudicabilidad;
- aplica R208-A sin inventar mecanismos, endpoints, cargas o estados;
- evita inferir exposición de PROFILE a partir de admisión;
- evita usar UNKNOWN para cubrir missingness, defectos de historia o ausencia de mecanismo;
- mantiene la distinción entre configuración declarativa, habilitación, disponibilidad operativa, admisión efectiva, truth y observación.

Se descartan expresamente: (a) mantener PROFILE exposure dentro de V_cont sin trayectoria truth; (b) eliminar la obligación contractual; (c) inferir exposición desde ENABLED o admisión; (d) crear PROFILE_EXPOSURE runtime sin soporte DGP; (e) alterar el operador de DEC-C10-102; (f) convertir falta de observación o representación en UNKNOWN.

## 4. Dependencias y efecto sobre el cierre

Si se acepta, el crosswalk normativo DEC-C10-102/Gate 154/R150-A/R151-A8/R152-A/R208-A quedará **CLOSED_FOR_CURRENT_SYNTHETIC_DGP_SCOPE** en el plano lógico.

No cierra por sí mismo:
- §51, reloj, soporte, T*, Δ, K, resolución ni calibración S3;
- materialización y conformidad de EventHistory/IntervalAdjudication/TruthBundle;
- asignación, población, aislamiento, soporte causal, q_X*, g_A0/g_A1 o r_common;
- identificación/recuperación de θ_A;
- Outcome/Value, potencia, N/R, tests, firewall o ejecución.

## 5. Acto de aprobación requerido

Esta es una propuesta. No se crea ni registra DEC-C10-105 como aceptada. La aprobación requiere aceptación expresa del responsable científico de C1–C6 en conjunto. Si se acepta, se emitirá un registro decisional complementario con trazabilidad a esta propuesta y a los artefactos históricos, preservando íntegramente DEC-C10-102.

## 6. Límites

No modifica DEC-C10-068/099…104, el DGP original, §51, schemas, código, fixtures, tests, workflows, RMA, Evidence→Claim Matrix, STATUS o Core. No ejecuta validadores, generación, pruebas, calibración, estimación, simulación ni Monte Carlo. No declara Design Freeze ni autoriza implementación o ejecución.

`scientific_execution=false`  
`execution_authorized=false`  
`implementation_authorized=false`
