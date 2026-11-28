# C10-S — Gate 134: conformidad temporal de V_cont y alcance admisible del benchmark integrado

**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** TEMPORAL_SEMANTICS_ALREADY_DECIDED / CURRENT_HARNESS_PARTIAL_CONFORMANCE / IDEAL_BASELINE_RETAINABLE_AS_BOUNDED_METHOD_TEST / FULL_VCONT_BENCHMARK_NOT_CONFORMANT / NO_NEW_DECISION_REQUIRED_FOR_SEMANTICS / NO_DESIGN_FREEZE / NO_EXECUTION.  
**Fuentes rectoras:** DEC-C10-099…102; C10-S Decision Log; contrato integrado `C10_S_INTEGRATED_VCONT_ANALYSIS_CONTRACT_DRAFT_001.md`; Gate 133; harness `vcont_integrated_harness.py`; benchmark protocol y tests.

## 1. Pregunta y dictamen

Gate 133 dejó dos opciones aparentes: (A) incorporar UNKNOWN y continuidad estricta al benchmark, o (B) aceptar un benchmark V_cont limitado a truth binaria intervalizada.

La reconstrucción de las decisiones muestra que **no existe una elección científica pendiente sobre la semántica de V_cont**. DEC-C10-100 y DEC-C10-102 ya la aceptaron expresamente. La opción B no puede elevarse a alcance confirmatorio de V_cont ni tratarse como excepción tácita a esas decisiones.

Dictamen:

1. La definición aceptada de V_cont exige verdad por intervalo en `{1,0,?}`, UNKNOWN propagado a bounds y continuidad estricta durante todo el intervalo.
2. El harness actual implementa solo una aproximación binaria intervalizada y no satisface esa semántica completa.
3. El benchmark ideal actual puede conservarse como baseline metodológico restringido para probar partes del Analyzer/estimandos de asignación, pero debe rotularse como **subconjunto de DGP / benchmark de medición ideal**, no como operacionalización completa ni validación confirmatoria de V_cont.
4. No hace falta emitir otra DEC para volver a aceptar lo ya decidido. Hace falta un crosswalk de conformidad entre esas decisiones y el DGP/harness, antes de poder declarar el benchmark completo implementado.

## 2. Autoridad y alcance de las decisiones aceptadas

### 2.1 DEC-C10-099 — constructo seleccionado

Selecciona provisionalmente V_cont como dimensión mínima unitaria de Value para la extensión sintética B. No fija por sí sola indicador, fórmula, ventana, resolución, baseline, horizonte, fuente o agregación. Mantiene abiertos los gates de validez, medición, identificación y discriminación.

### 2.2 DEC-C10-100 — truth temporal y UNKNOWN

Acepta:

`V_cont_truth(i) = (1/K) Σ_{k=1}^{K} A_B1(i,k)`

con intervalos de igual duración en una rejilla común y preespecificada, donde `A_B1(i,k) ∈ {1,0,?}`:

- `1`: cumplimiento funcional positivamente estipulado por el DGP;
- `0`: incumplimiento funcional positivamente estipulado por el DGP;
- `?`: truth no determinada para ese intervalo.

Si hay UNKNOWN, el Evaluator conserva bounds `[n1/K, (n1+n?)/K]`. No imputa cero, no elimina intervalos del denominador y no usa complete-case para fabricar una estimación puntual. La regla de agregación sí está aceptada; K, ventana, frecuencia, duración y demás parámetros siguen abiertos.

### 2.3 DEC-C10-101 — origen de la ventana

Acepta `t0` inmediatamente después de la asignación Z, incluyendo provisión e instalación. No condiciona el inicio a intento, recepción, instalación, verificación, C_dep, accesibilidad, Reach, selección o ejecución. La ventana es `[t0,T*]`; T* y la unidad/duración siguen abiertos.

### 2.4 DEC-C10-102 — continuidad estricta

Acepta, sin periodo de gracia ni tolerancia implícita:

- `1` solo si ENABLED/PROFILE se cumple durante todo el intervalo;
- `0` si ocurre al menos un incumplimiento funcional confirmado en cualquier instante del intervalo;
- `?` solo si el propio Generator no puede determinar la truth funcional del intervalo.

La ausencia, pérdida, lag o cobertura insuficiente de S3 es incertidumbre observacional, no UNKNOWN de truth. Los eventos exactamente en frontera requieren asignación determinista, única y versionada. Se recomienda reloj explícito, eventos fechados y rejilla regular; T*, Δ, K, resolución, regla de cierre y cobertura/calibración S3 permanecen OPEN.

## 3. Conformidad del harness actual

| Requisito aceptado | Implementación observada | Dictamen |
|---|---|---|
| V_cont por media no ponderada de K intervalos iguales | Media sobre `n_intervals` | PARCIALMENTE CONFORME |
| Estados de truth 1/0/? | `potential_interval_truth` binario 0/1 | NO CONFORME |
| UNKNOWN solo por indeterminación del Generator | No existe estado UNKNOWN de truth | NO IMPLEMENTADO |
| Bounds de truth `[n1/K,(n1+n?)/K]` | No materializados | NO IMPLEMENTADO |
| 1 exige cumplimiento durante todo el intervalo | Conjunción de ENABLED y PROFILE generada como estado binario por intervalo | NO ACREDITA CONTINUIDAD ESTRICTA |
| 0 ante cualquier incumplimiento confirmado intraintervalo | No hay secuencia de eventos/estado fechada que permita adjudicar cualquier instante | NO REPRESENTADO |
| Inicio t0 incluyendo provisión/instalación | Hay parámetros de ventana y soporte de transición, pero no mapping completo acreditado de todos los eventos causales a intervalos | PARCIAL / NO ACREDITADO |
| Eventos de frontera asignados una sola vez y versionados | No acreditado en el mapping temporal del harness | OPEN |
| S3 separado de truth | Sí; S3 missingness es observación, no truth | CONFORME EN ESTA DISTINCIÓN |
| Ausencia S3 no se convierte en UNKNOWN funcional | Se representa como `None` en observación | CONFORME EN ESTA DISTINCIÓN |

La conjunción binaria ENABLED∧PROFILE solo acredita el valor funcional que el DGP asignó a la celda/intervalo. No acredita por sí misma que el requisito “durante todo el intervalo” se haya evaluado frente a todos los eventos relevantes. La ausencia de un event log no demuestra que no haya eventos; demuestra que este harness no puede adjudicarlos.

## 4. Reconciliación con el contrato integrado

El contrato integrado V_cont se declara cerrado para implementación en la rama research, pero especifica estimandos de asignación, firewall, condiciones de identificación y restricción actual de medición puntual perfecta/completa. No modifica ni sustituye DEC-C10-100…102.

Por tanto, hay dos niveles que deben mantenerse separados:

**A. Benchmark integrado actualmente implementado.** Puede evaluar los estimandos ITT-Z/ITT-G bajo su DGP binario por intervalos, S3 perfecto/completo y las condiciones contractuales. Es un baseline metodológico limitado y no una validación de la semántica temporal completa de V_cont.

**B. V_cont conforme a las decisiones aceptadas.** Requiere que la truth del Generator/Evaluator preserve 1/0/? y la continuidad estricta por intervalo, con UNKNOWN/bounds y reglas temporales de eventos/fronteras. La evidencia S3 continúa separada y no puede sustituir la truth.

No hay contradicción en conservar A como benchmark parcial. Sí habría contradicción en declarar A como implementación completa de B o en cambiar silenciosamente el alcance de las DEC.

## 5. Consecuencias para Generator, Sealer, Analyzer y Evaluator

- **Generator:** deberá poder representar los eventos/estados sintéticos necesarios para determinar cumplimiento estricto durante el intervalo y producir UNKNOWN solo cuando la truth no pueda determinarse según el DGP. Los parámetros temporales concretos siguen sin seleccionarse.
- **TruthBundle/Evaluator:** deberán preservar el estado tri-valuado por unidad e intervalo y los bounds agregados. La verdad y sus potenciales permanecen fuera del Analyzer.
- **EvidenceCandidate/Sealer:** conservarán exclusivamente señales S3 y metadatos autorizados de observación, cobertura, tiempo e identidad. No se añade truth a la allowlist.
- **Analyzer:** no podrá inferir continuidad por ausencia de señal. Con S3 imperfecto/ausente sin modelo aprobado, debe abstenerse o aplicar bounds solo cuando exista método autorizado. No se presume calibración ni se elige ahora un método.
- **Evaluación del benchmark:** separar recuperación de estimandos de asignación bajo baseline ideal de conformidad temporal de la truth. Un PASS de la primera no implica PASS de la segunda.

## 6. Qué no se decide en Gate 134

No se eligen T*, Δ, K, unidad física, frecuencia, resolución, eventos mínimos, tratamiento numérico de lag, mecanismos de error/ausencia, Se/Sp, calibración, tolerancias, bounds de medición, tamaño muestral ni método de corrección. Tampoco se modifica DEC-C10-099…102 ni el contrato integrado.

No se crea una excepción que convierta la truth binaria actual en definición aceptada de V_cont. No se exige que el baseline parcial desaparezca ni se invalida el trabajo de Analyzer ya realizado.

## 7. Siguiente paso mínimo — Gate 135

Realizar un **crosswalk de conformidad temporal DEC → DGP → TruthBundle → Evaluator** sobre los contratos ya existentes, identificando:
1. el punto exacto donde el harness binariza ENABLED/PROFILE;
2. qué representación de eventos/estados permitiría adjudicar cumplimiento estricto sin fijar todavía granularidad no aprobada;
3. dónde preservar UNKNOWN de truth sin confundirlo con missingness S3;
4. cómo se calculan y sellan los bounds de truth en Evaluator;
5. qué parte puede mantenerse como baseline ideal independiente;
6. qué decisiones adicionales, si las hubiera, son realmente necesarias antes de implementación.

Gate 135 será documental y no alterará código, schemas, DEC, test register, workflows, main, RMA, Evidence→Claim Matrix o STATUS. No crear una nueva matriz ni parámetros. La implementación queda pendiente de contrato y autorización.

## 8. Límite de autorización

Auditoría estática de GitHub. No se importó ni ejecutó código; no se ejecutaron tests, validadores, workflows, generación, simulación, calibración, estimación, benchmark o experimento. No se modificó código ni se promovió ningún artefacto a main.

`scientific_execution=false`  
`execution_authorized=false`
