# C10-S — Gate 131: suficiencia de medición e identificación observacional de V_cont mediante S3

**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** TEMPORAL_TRUTH_RULE_ACCEPTED / S3_PASSIVE_CHANNEL_DEFINED / S3_MEASUREMENT_MODEL_NOT_IDENTIFIED_OR_VALIDATED / P182_P183_CONTRACT_FAMILIES_DEFINED_NOT_MATERIALIZED / ANALYZER_POINT_IDENTIFICATION_REQUIRES_PERFECT_COMPLETE_S3 / NO_DESIGN_FREEZE / NO_EXECUTION  
**Precedencia:** DEC-C10-099…102; Gate 128; Gate 129; Gate 130 y su corrigendum; contrato integrado V_cont §§5–6; matriz temporal de predicados; Test Contract Register P182-01…12, P183-01…13, MEAS-01…14, MISS-01…15; Gates 172, 176–183, 199–205.

## 1. Pregunta y dictamen ejecutivo

¿La arquitectura documental y técnica existente permite medir V_cont con S3 de forma que el Analyzer pueda identificar o acotar el resultado, sin acceder a la truth del Generator?

**Dictamen:** la regla de verdad temporal de V_cont está parcialmente aceptada y suficientemente definida en su semántica: dimensión unitaria, agregación igualitaria, ventana iniciada en t0 y continuidad estricta por intervalo. S3 está definido como canal pasivo, no-mutante, vectorial e imperfecto. Pero no existe todavía un modelo de medición S3 identificado/validado que permita recuperar puntualmente V_cont a partir de señales observadas. El contrato integrado mantiene como restricción actual de identificación puntual una medición S3 perfecta y completa; si hay error o ausencia no cubiertos por un modelo aprobado, Analyzer debe abstenerse/emitir INDETERMINATE, no tratar la ausencia de señal como continuidad.

**Resultado:** `VCONT_TRUTH_SEMANTICS_PARTIALLY_ACCEPTED / S3_CHANNEL_CONCEPTUALLY_DEFINED / SIGNAL_TO_TRUTH_MEASUREMENT_MODEL_OPEN / ERROR_AND_MISSINGNESS_NOT_CALIBRATED / POINT_IDENTIFICATION_NOT_ESTABLISHED / NO_NEW_TEST_FAMILY_REQUIRED / NO_FREEZE`.

## 2. Reconstrucción histórica: qué reutilizamos y qué no debemos volver a diseñar

| Artefacto | Cobertura ya existente | Límite que permanece |
|---|---|---|
| DEC-C10-099 | Selecciona V_cont como única dimensión mínima provisional para B | No fija indicador, horizonte ni validez |
| DEC-C10-100 | V_cont_truth=(1/K)Σ A_B1(i,k), intervalos iguales; UNKNOWN produce bounds | K, rejilla, duración, calibración y validez S3 abiertos |
| DEC-C10-101 | Ventana post-Z desde t0, incluye provisión/instalación | T*, unidad y resolución temporal abiertos |
| DEC-C10-102 | Continuidad estricta en cada intervalo; fallo confirmado afecta al intervalo | Detección temporal y capacidad S3 para detectar fallos breves abiertas |
| Gate 128 | VCONT-B1-MIN aceptada como regla ordinal acotada | No valida medida ni identificación |
| Gate 129 | S3 no validado para θ_A; Analyzer actual no estima θ_A | No sustituir el análisis de S3 por el estado de θ_A |
| Matriz temporal de predicados | Separa truth_dgp, observed_state, evidence_id, coverage y adjudicación por unidad/paso/rama/tiempo | No materializa señales S3 ni modelo de error/cobertura |
| P182-01…12 | Cobertura, circularidad, especificación, separación O/V, reproducibilidad, acuerdo, error, invariancia, sensibilidad, firewall y trazabilidad | Contratos documentales; sin calibración/oráculos completos ni evidencia de ejecución para S3 |
| P183-01…13 | Taxonomía y mecanismos de ausencia, selección, censura, bounds y dictamen por estimando | Mecanismos y parámetros S3 no materializados; no hay recuperación validada bajo MNAR |
| MEAS-01…14 / MISS-01…15 | Familias de casos adversariales reutilizables | No fixtures serializados, oráculos, tolerancias calibradas ni hashes de ejecución para esta medición |
| Gates 172, 176–183 | Captura de matriz, report snapshot, companions, serialización y verificación de paquetes | Integridad/provenance/export no equivale a validez de medida ni identificación de V_cont |
| Gates 199–205 | Materialización reproducible de fuentes, workflows, runtime y límites de autorización | Infraestructura de workflow; no cierra S3, no autoriza dispatch ni ejecución |

No se crea una nueva matriz ni una nueva familia de pruebas. La revisión distingue el contrato de medida del contrato de exportación: un paquete íntegro y verificable puede contener una medición inválida o insuficiente.

## 3. Verdad temporal y objeto que S3 debe observar

Se preserva la cadena conceptual existente:

- Generator conserva `A_B1(i,k) ∈ {1,0,?}` como truth funcional por unidad e intervalo.
- Evaluator calcula `V_cont_truth` sobre la rejilla común aceptada y aplica bounds cuando la truth del intervalo es desconocida.
- S3 captura señales runtime pasivas que pueden informar sobre el cumplimiento funcional, pero no es el predicado A_B1 ni su oráculo.
- Analyzer recibe únicamente señales S3 observadas y metadatos permitidos de identidad, tiempo y cobertura; no recibe A_B1, V_cont_truth, potenciales, semillas ni parámetros reservados.
- Evaluator compara la salida sellada del Analyzer con truth solo después de que el Analyzer haya terminado.

La ausencia, retraso o pérdida de señal pertenece al canal de observación: no convierte truth en 0, 1 o ?. La regla de continuidad estricta significa que una interrupción confirmada en cualquier instante afecta al intervalo; no implica que S3 tenga resolución suficiente para detectarla. Si la resolución/cobertura no puede detectar eventos relevantes, la salida puntual no está justificada.

S4 puede apoyar identidad, versión e integridad; S5 aporta el contrato ENABLED/PROFILE. Ninguno sustituye a S3 como canal observacional temporal.

## 4. Hallazgos sobre la identificación actual

### 4.1 La restricción de medición es más fuerte que la definición de truth

El contrato integrado V_cont §5 establece que la identificación puntual actual presupone medición S3 perfecta y completa. No presenta un modelo validado que transforme señales imperfectas en una estimación de A_B1/V_cont_truth ni un método aprobado de identificación parcial que corrija esa restricción.

Por tanto, no es correcto decir que la arquitectura actual ya identifica V_cont bajo error/lag/missingness solo porque el DGP conoce A_B1 y el Evaluator conserva truth.

### 4.2 Error y acuerdo

P182-07 y P182-08 proporcionan criterios generales para falsos positivos/negativos y error de O/V; P182-05/06 exigen reconstrucción y acuerdo. Sin embargo, no están fijados para S3:
- qué señales observadas constituyen evidencia de ENABLED/PROFILE funcional durante un intervalo;
- qué discrepancia temporal cuenta como falso positivo o falso negativo frente a A_B1;
- cómo se adjudican eventos concurrentes o fronterizos;
- cómo se cuantifican error diferencial, dependencia entre señales y acuerdo entre fuentes/evaluadores.

No se asignan tasas ni tolerancias en este gate.

### 4.3 Lag, resolución y cobertura

DEC-C10-101/102 requieren reloj y rejilla temporal comunes, pero dejan T*, Δ, K y resolución abiertos. Sin esos parámetros no se puede evaluar si S3 observa todos los eventos funcionales relevantes dentro del intervalo ni si un fallo breve puede ser detectado y asignado correctamente a una única frontera/intervalo.

No se infiere que un timestamp de telemetría sea el instante real del evento funcional; la semántica de event time, observation time, ingestion time y lag debe quedar diferenciada antes de materializar.

### 4.4 Ausencia y censura

P183-01…13 distingue ausencia, mecanismos MCAR/MAR/MNAR, selección, censura, bounds y abstención. El registro no aporta todavía un mecanismo generativo específico para la ausencia S3 ni una especificación de qué auxiliares están disponibles al Analyzer para justificar MAR. No puede asumirse MCAR/MAR por conveniencia. Ante ausencia no identificable o censura informativa sin sensibilidad aprobada, corresponden bounds o INDETERMINATE.

### 4.5 Integridad y provenance no son validez

Gates 176–183 y 199–205 desarrollan captura exacta, snapshots, companions, serialización, hashes, verificación y materialización reproducible. Estas garantías son necesarias para reconstruir qué se observó y con qué versión, pero no prueban que la señal mida A_B1 ni que el error sea suficientemente pequeño o identificable.

## 5. Qué está cerrado, qué falta y qué no puede afirmarse

| Componente | Estado |
|---|---|
| Constructo/dimensión V_cont | Selección provisional aceptada |
| Truth funcional A_B1 por intervalo | Definición semántica aceptada con 1/0/? |
| Agregación temporal | Media igualitaria aceptada |
| Inicio de ventana | t0 aceptado |
| Continuidad estricta | Aceptada |
| S3 como canal pasivo vectorial imperfecto | Definido conceptualmente |
| Indicadores/señales S3 y semántica de cada señal | OPEN |
| T*, unidad temporal, Δ, K, resolución | OPEN |
| Reglas de event-time/observation-time/ingestion-time y lag | OPEN |
| Cobertura y capacidad de detectar interrupciones | OPEN |
| Error, dependencia y acuerdo de medida S3 | OPEN |
| Modelo de medición y calibración independiente | OPEN |
| Mecanismos de ausencia/censura S3 y sensibilidad | OPEN |
| Identificación puntual V_cont bajo S3 imperfecto | NOT ESTABLISHED |
| Bounds/abstención implementados y validados | NOT ESTABLISHED |
| Recuperación de θ_A por Analyzer | NOT ESTABLISHED; además θ_A sigue sin materializar por los bloqueos Gate 129/130 |

La truth del Generator puede ser completa mientras la información del Analyzer sea insuficiente. Esa diferencia es precisamente el objeto metodológico que el diseño debe poder detectar y adjudicar.

## 6. Routing mínimo: Gate 132

El siguiente trabajo no debe abrir otra matriz ni crear nuevos IDs. Debe realizar un crosswalk dirigido, usando solo contratos existentes, entre:
1. campos observables y fuentes S3 disponibles en el contrato integrado y el harness;
2. A_B1/V_cont_truth y sus reglas temporales DEC-C10-100…102;
3. P182-05…08/11/12 y P183-01…13;
4. MEAS-01…14 y MISS-01…15;
5. entradas permitidas al Analyzer y verdad reservada del Generator/Evaluator.

Objetivo: determinar si existe ya un subconjunto de señales y reglas suficiente para un benchmark de medición ideal (sin confundirlo con robustez a error), y clasificar cada condición como definida, implementada, ejecutada, auditada, aceptada, condicional, abierta o bloqueada. Cualquier futura propuesta de error/calibración deberá ser explícita y no se añadirá al diseño actual sin decisión. No elegir señales, T*, Δ, K, tasas, tolerancias, mecanismos MAR/MNAR o tamaño de validación en este paso.

## 7. Límites de autorización

Este gate es una auditoría estática de artefactos y contratos. No importa ni ejecuta código, no inspecciona datos runtime, no construye fixtures, no genera señales, no calibra, no ejecuta tests/CI/workflows ni benchmark. No modifica DEC, schemas, test register, código, workflows, RMA, Evidence→Claim Matrix, STATUS, Core o main.

`scientific_execution=false`  
`execution_authorized=false`
