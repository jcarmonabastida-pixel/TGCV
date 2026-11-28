# C10-S — Paquete B: registro integrado de materialización de componentes sintéticos

**Fecha:** 2026-11-16  
**Rama:** research/c10-s-consolidation-draft · PR #116 (Draft)  
**Estado:** SOURCE_COMPONENTS_MATERIALIZED / D2_PARAMETERIZED_POTENTIALS_IMPLEMENTED / EVENTHISTORY_AND_INTERVAL_ENGINE_IMPLEMENTED / THETA_A_EVALUATOR_ORACLE_IMPLEMENTED / S3_JOINT_SEQUENCE_PROJECTOR_IMPLEMENTED / ANALYZER_THETA_A_NOT_IMPLEMENTED / SOURCE_ONLY_NOT_TESTED / SCIENTIFIC_EXECUTION_NOT_AUTHORIZED.  
**Precedencia:** README operativo en main; Paquete B aceptado; DEC-C10-066/067/099…104; DEC-C10-103; Gates 92, 129–132, 145–146, 154, 206, 208; R144-A; R146-A…D; DGP Temporal and Role Contract; Synthetic Harness Integrated Specification; P177–P183, MEAS/MISS.

## 1. Objeto y regla de materialización

Este registro documenta la primera materialización de software autorizada del carril sintético S, sobre los contratos y el harness existentes. No crea un segundo benchmark, no cambia DEC, no modifica main y no declara que el experimento esté listo para ejecución.

Se ha añadido una biblioteca de componentes reutilizables y un adaptador composicional que conserva intactos los objetos legacy del Generator, EvidenceCandidate, Sealer y Analyzer. La nueva verdad queda en una extensión separada del paquete observado.

## 2. Archivos materializados

| Archivo | Objeto | Estado |
|---|---|---|
| 03_EXPERIMENTS/C10-S/harness/c10s_synthetic_components.py | Componentes D2, EventHistory, IntervalAdjudication, oracle θ_A, Evaluator score, S3 y composer | SOURCE_MATERIALIZED |
| 03_EXPERIMENTS/C10-S/harness/test_c10s_synthetic_components.py | Tests de contrato para componentes nuevos | SOURCE_MATERIALIZED / NOT_EXECUTED |
| 03_EXPERIMENTS/C10-S/harness/README.md | Instrucciones, límites y crosswalk del nuevo componente | UPDATED |
| .github/workflows/c10-s-focal-harness-tests.yml | Allowlist explícita ampliada de ocho a nueve módulos, conservando workflow_dispatch, rama research y confirmación obligatoria | UPDATED / NOT_DISPATCHED |

No se modificó vcont_integrated_harness.py ni se alteró su comportamiento previo. El nuevo composer llama al Generator existente y conserva su EvidenceCandidate sin añadir campos truth a la allowlist. La extensión truth se devuelve por separado y no debe pasarse al Sealer ni al Analyzer.

## 3. D2 — cadena por etapas materializada como generador de potenciales parametrizado

Se implementan objetos tipados y versionados para:

Z → B/policy → W_programmed → W_attempt → receipt → S_install → C_dep* → A_f* → D_f*

La configuración exige explícitamente:
- identidad/versionado DGP y mecanismo;
- policy_id/version, artefacto y actor diferenciados para Z=0 y Z=1;
- probabilidades distintas por brazo para programación, intento condicionado a programación, intento de fondo, recepción e instalación;
- distribución conjunta de los cuatro predicados técnicos C_install/C_integrity/C_compat/C_oper.

El generador conserva los dos potenciales Z=0/Z=1 con draws exógenos comunes y registra provenance por potencial. C_dep* se calcula como conjunción de sus cuatro componentes; A_f* exige además C_auth,base, C_resource, C_capacity, C_info, C_domain y C_other; D_f* se calcula como apertura basal 0→post 1.

**Límites:** no se han elegido probabilidades ni distribuciones confirmatorias. No se adoptan los candidatos 0/1 de programación ni s=0.80 como parámetros aprobados. El módulo genera potenciales; no selecciona por sí mismo la asignación Z ni acredita un mecanismo de asignación D2. El intento de fondo, recepción, instalación y componentes permanecen separados. No se modelan todavía desviaciones/crossover, reintentos ni fallos parciales con recurrencia.

## 4. EventHistory y adjudicación temporal

Se implementan:
- ámbito explícito de historia: run, world, DGP, unidad, potencial y versiones;
- estado inicial post-Z;
- transición truth con ID propio, event_time Decimal, estado before/after, familia causal y provenance reservada;
- suborden únicamente para transiciones funcionalmente intermedias al mismo event_time;
- manifiesto Generator-side de IDs esperados, comparado exactamente con los IDs materializados;
- tres planos de completitud: scope, generación y representación;
- hash de contenido y objetos inmutables;
- adjudicación estricta A_B1 de admisión conforme a ENABLED, bajo el alcance Gate 154;
- rejilla explícita de intervalos iguales, intervalos internos semiabiertos y último cerrado en T*;
- V_cont como media igualitaria; en historias completas y determinadas, bounds coinciden con el punto adjudicado.

No se reutiliza PROCESS_EVENT ni S3 como verdad. PROFILE exposure permanece fuera del predicado temporal V_cont según Gate 154, sin eliminar su obligación contractual.

**Límite temporal:** event_time y las fronteras son Decimal para evitar ambigüedad numérica, pero no se elige unidad, origen físico, soporte, T*, Δ, K, ρ_follow ni resolución. R144-B y §51 permanecen abiertos. La función acepta el reloj/rejilla que suministre el diseño futuro; no los inventa.

## 5. q_X*, g_A0/g_A1, r_common y θ_A

Se implementa un oracle genérico del lado Evaluator que calcula:

θ_A(q_X*, r_common; V_cont) = Σ_h q_X*(h) · [E(V_cont | g_A1,h,r_common) − E(V_cont | g_A0,h,r_common)]

Controles incorporados:
- q_X* requiere filas explícitas X/H0/C_c, masa positiva por historia y suma de masas igual a uno;
- las masas no se estiman a partir de frecuencias de la muestra, asignación Z/G o roster de perfiles;
- g_A0 y g_A1 son distribuciones conjuntas sobre las cuatro coordenadas del vector completo ΔT_acc*;
- el soporte de cada política debe estar contenido en el conjunto factible declarado para cada historia positiva;
- se requiere un certificado por historia con estado COMMON_FIXED y fingerprint idéntico en ambos mundos;
- el resultado se etiqueta evaluator_only y nunca se deriva de ITT-G;
- se incluye un comparador Evaluator para recuperar dentro de tolerancia o comprobar abstención tras la salida sellada del Analyzer.

**Límite decisivo:** no se selecciona ni aprueba q_X*, roster/historias/masas, par operativo g_A0/g_A1, conjunto factible o certificados r_common. El oracle solo puede calcular truth cuando esos objetos se suministren de forma explícita y compatible con los contratos. El Analyzer actual no estima θ_A; no se ha añadido un estimador ni un campo de resultado θ_A al AnalyzerResult. Por tanto, θ_A sigue NOT_IDENTIFIED / NOT_RECOVERED en el harness actual.

## 6. S3 — proyección pasiva con dependencia conjunta

Se implementa un proyector S3 genérico que recibe:
- calendario explícito de observación;
- lag de captura y de ingestión por observación;
- kernel conjunto sobre la secuencia latente completa y una distribución conjunta sobre toda la secuencia observada.

El kernel conjunto permite dependencias entre señales y entre tiempos sin asumir independencia temporal o entre indicadores. La proyección genera únicamente filas observadas, conserva observation_time/capture_time/ingestion_time por separado y no modifica EventHistory.

No se eligen señales, calendario, tasas de error, cobertura, detectabilidad, missingness, censura o calibración. No existe aún un modelo de medición identificado/validado ni corrección de error o bounds aprobados. La restricción existente de identificación puntual del Analyzer —S3 perfecto y completo— permanece sin cambios. El nuevo proyector no está todavía conectado a la allowlist del Sealer ni al Analyzer legacy.

## 7. Composición y firewall

compose_existing_generation(...) conserva el Generator existente y añade:
1. potenciales D2 por unidad, con parámetros y seeds explícitos;
2. EventHistory creada por un factory explícito, ligado al run_id exacto;
3. IntervalGrid creada por un factory explícito, sin defaults temporales;
4. adjudicaciones ligadas por versión y hash a cada EventHistory;
5. truth θ_A opcional, solo si se proporcionan todos los inputs explícitos.

project_s3_batch(...) devuelve una proyección observacional separada. No se ha mezclado truth con EvidenceCandidate. La separación es una frontera de objetos/API en código fuente; no constituye por sí sola una garantía de seguridad de proceso/almacenamiento ni reemplaza el threat model y controles PE/G-ROLE.

## 8. Cobertura de tests y estado de ejecución

Se han añadido fixtures para:
- separación de etapas D2 y conjunción C_dep*;
- evento en frontera interna y en T*;
- suborden y estado intermedio simultáneo;
- fallo cerrado ante EventHistory incompleta;
- cálculo de θ_A sobre vector conjunto, y rechazo de r_common no común;
- evaluación de recuperación/abstención;
- secuencia S3 conjunta con ausencia sin mutar truth.

El workflow de harness queda configurado para compilar y ejecutar una allowlist explícita de nueve módulos, con primary y clean replay, únicamente tras dispatch manual en research y confirmación booleana expresa.

**No se ha ejecutado** py_compile, import, unittest, workflow, generación sintética, calibración, seed-bank, Monte Carlo, Analyzer, Evaluator, paquete ni experimento. No hay PASS técnico ni científico. La ampliación del workflow no es una autorización para despacharlo.

## 9. Brechas que permanecen para completar el experimento

1. Instanciar el roster sintético y las historias X/H0/C_c con procedencia y población objetivo coherentes con los contratos, sin sustituir q_X* por frecuencias.
2. Materializar una asignación D2 con unidad, π_h, mecanismo y provenance explícitos; no reutilizar automáticamente el Z legacy.
3. Seleccionar y justificar parámetros D2 y la distribución conjunta de C_dep*; incluir escenarios adversariales sin convertir candidatos no aprobados en defaults.
4. Conectar A_f*/D_f* con el mapping aprobado del vector ΔT_acc* completo, Reach/Π y trayectoria. Esa función no se inventa en este bloque.
5. Definir y versionar el outcome V_cont en el DGP integrado; EventHistory y el operador temporal están disponibles como componentes, pero no se genera automáticamente desde D2 sin la regla temporal aceptada y un factory completo.
6. Resolver §51/R144-B: soporte, T*, Δ, K, relación event_time/rejilla y suficiencia frente a eventos breves/fronteras.
7. Materializar y validar el modelo S3, sus señales, cobertura, error, lag, ausencia/censura y calibración; integrar la evidencia en Sealer/Analyzer.
8. Implementar ruta de identificación y estimador θ_A del Analyzer, bounds/abstención y validación por Evaluator; no confundir el oracle de truth con identificación observacional.
9. Completar Outcome/Value contextual del Paquete C; V_cont no se declara Value general.
10. Justificar N/R, precisión, sensibilidad, potencia y escenarios Monte Carlo antes de cualquier ejecución.

## 10. Autorización y límites preservados

La instrucción del usuario autoriza implementación de componentes del carril sintético S en esta rama research. Esta materialización no amplía el alcance de autorización.

- implementation_authorized=true — carril S, componentes fuente dentro del alcance aprobado;
- technical_test_execution_authorized=false;
- workflow_dispatch_authorized=false;
- calibration_authorized=false;
- scientific_execution=false;
- execution_authorized=false;
- material_lane_authorized=false;
- main_promotion_authorized=false.

No se creó ni modificó DEC-C10, RMA, Evidence→Claim Matrix, STATUS, TGCV Core o main. PR #116 sigue Draft.

## 11. Identidad de fuentes

Hashes de blobs GitHub de los componentes materializados:
- c10s_synthetic_components.py: dbe61a11777399c6a5d6a063f4ee12be73a83ea8.
- test_c10s_synthetic_components.py: cab1d9de936ed8b9e947f857bf507b0b85bbf3c7.
- c10-s-focal-harness-tests.yml: c925d60d3ca713a2d72bbd64fdc84215704cca4f.

Estos son hashes de blobs fuente, no hashes de una ejecución ni evidencia de conformidad.
