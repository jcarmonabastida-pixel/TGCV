# C10-S — Paquete B: aceptación B1–B6 y reconciliación de materialización sintética

**Fecha:** 2026-11-16  
**Rama:** research/c10-s-consolidation-draft · PR #116 Draft  
**Estado:** B1_B6_ACCEPTED / SYNTHETIC_LANE_MATERIALIZATION_REQUIRED / HISTORICAL_ASSETS_REUSED / MATERIAL_LANE_NOT_APPLICABLE_TO_SYNTHETIC_CONFIRMATORY_CORE / IMPLEMENTATION_AUTHORIZED_SYNTHETIC_SCOPE_ONLY / SCIENTIFIC_EXECUTION_NOT_AUTHORIZED.

## 1. Aceptación y corrección de alcance

El usuario acepta conjuntamente B1–B6 del Paquete B. La aceptación comprende el cierre del contrato lógico temporal y causal, con esta precisión:

**C10-S es un experimento sintético. El carril S (Synthetic) es el objeto del experimento. El carril M (material/real-world) no es prerequisito para generar, identificar por construcción o evaluar mundos sintéticos.**

La propuesta base mezclaba dependencias del carril M —roster real, IAM/C_SRC, snapshots, inventario runtime y aislamiento material— con la materialización que sí necesita el carril S. Se corrige aquí: el Generator puede crear población, configuración, dependencias, recursos, historias, intervenciones y observaciones sintéticas con verdad conocida.

La aceptación B1–B6 cierra el contrato lógico integrado. No declara que el DGP completo esté materializado, que θ_A esté identificado por observaciones, que el Analyzer lo recupere o que el experimento esté ejecutado.

## 2. Separación S/M

| Dimensión | Carril S — experimento sintético | Carril M — instancia material real |
|---|---|---|
| Población | Roster finito generado por el DGP, con IDs sintéticos y reglas versionadas | Roster real y fuentes de elegibilidad |
| Configuración/servicio | CMP/PAR/RUL y runtime sintéticos | IAM/C_SRC, snapshots y runtime observados |
| Dependencias/recursos | Grafo, disponibilidad, capacidad y recursos simulados | Inventario y evidencia técnica externa |
| Aislamiento | Independencia por construcción en núcleo; interferencia inducida en escenarios adversariales con mapa conocido | IS-1…IS-8 y evidencia material |
| Asignación | Z aleatorizado por algoritmo sintético versionado; seeds/probabilidades conocidas por Generator/Evaluator | Asignación y protocolo material |
| q_X*, g_A, r_common | Distribuciones, políticas conjuntas y régimen común como objetos sintéticos explícitos | Contrapartes empíricas defendibles y soporte observado |
| Truth/EventHistory | Generados exhaustivamente y reservados al Evaluator | Sin oráculo de verdad generada equivalente |
| Observación S3 | Proyección sintética imperfecta de la verdad | Instrumentación/runtime reales |

Gate 121 y Gate 122 siguen siendo relevantes para la eventual ruta M. No bloquean el núcleo sintético S. En S no se exige inventario externo, acceso a proveedores, credenciales, entrevistas, runtime productivo ni snapshots reales. Los artefactos S no se presentarán como evidencia M.

## 3. Reconstrucción de activos existentes — reutilización obligatoria

| Activo existente | Estado verificable | Reutilización y límite |
|---|---|---|
| Maestro §§16.188–16.212 | Roster dirigido, familias de escenarios, funciones y potenciales definidos estructuralmente | Reutilizar; no crear otro roster conceptual. Falta poblar la instancia sintética y cerrar funciones cuantitativas |
| Maestro §16.223 y Gates 69–71 | Esquema de ledger por celda y doce roles C1/C3 | Reutilizar; no crear ledger ni roles paralelos. Faltan filas/valores y mapping al DGP materializado |
| Scenario–Estimand Coverage Matrix | 13 escenarios × 4 estimandos de asignación = 52 pares; VCONT-SYNTH-001 | Reutilizar; no generar segunda matriz. θ_A está fuera de esos cuatro contrastes y requiere su contrato focal |
| vcont_integrated_harness.py | Generator, TruthBundle, Projector/Sealer, Analyzer, Evaluator, potenciales comunes, ITT-Z e ITT-G; parámetros de medición, heterogeneidad e interferencia | Implementación parcial. theta_a_truth sigue None; G no equivale a g_A |
| focal_harness.py | Slice anterior focal B1/Q_B1, con truth y evidencia separadas | Mantener como slice histórico independiente; no tratarlo como D2 completo ni estimador de θ_A |
| Tests del harness | Suite fuente persistida | Existencia de tests no equivale a ejecución ni PASS |
| Calibration and Seed-Bank Protocol | Protocolo implementado para bancos separados, selección N/R y MCSE | Reutilizar. Objetivos numéricos y ejecución de calibración siguen abiertos |
| P178 calibration outputs | Resultados históricos P178 | No transferir N=700, R, tolerancias ni potencia a θ_A o al DGP temporal integrado |
| Gates 171–194I / package v2 | Captura, serialización, fingerprints, writer/verifier y contratos de paquete progresivamente implementados | Reutilizar para provenance y empaquetado; no prueban identificación causal |
| Gates 203–205 / EP-01–03 | Workflows de materialización de fuentes y ejecución/replay implementados en research; revisión estática parcial | Validación YAML/action completa sigue abierta; no se acredita ejecución científica |
| DGP temporal §51–52 | Reloj adimensional: t0=0, t_c,max=1, x=(t−t0)/W_c; T*=1+ρ_follow | La coordenada no se vuelve a diseñar. ρ_follow, T*, K, Δ y S3 requieren valores sintéticos versionados |
| EventHistory | Semántica R144-A y R146-A…D aceptada; composición lógica y alcance A_B1 avanzados por Gates 145–154 y 206–208 | Falta materialización ejecutable de EventHistory/event_time/IntervalAdjudication en el harness integrado |
| R208-A1…A6 | Aceptadas en plano lógico | Aplicar su alcance; no reabrir PROFILE, D_valid, runtime, recursos o solicitudes salvo incompatibilidad demostrada |

Reconstrucción estática de archivos y contratos. No atribuye PASS a tests, workflows, calibraciones o ejecuciones no realizadas.

## 4. Brechas sintéticas reales

### S-B1 — Cadena generativa D2

El harness integrado actual no representa la cadena D2 completa como variables/etapas diferenciadas. Deben materializarse con potenciales coherentes y provenance:

Z → B/policy → W_programmed → W_attempt → receipt → S_install → C_dep* → A_f* → D_f* → ΔT_acc* → Reach/Π → trajectory → Outcome → V_cont.

Cada etapa conserva su propio estado y mecanismo. No se hereda éxito de una etapa a la siguiente. Los valores históricos 0.20/0.80 y s=0.80 no se convierten en defaults: se elegirán valores de fixture sintético versionado y se cubrirán alternativas/sensibilidad.

### S-B2 — q_X*, g_A0/g_A1, r_common y θ_A

Es la brecha causal central. El código actual genera G e itt_g_z0_truth, pero mantiene theta_a_truth=None. Se materializarán en el Generator:
- roster sintético finito y distribución basal conjunta q_X* con historias/masas explícitas;
- políticas conjuntas g_A0/g_A1 sobre el vector completo ΔT_acc*=(ΔU*, ΔR*, ΔC*, ΔX*);
- factibilidad y soporte conjunto para cada historia de masa positiva;
- r_common por historia, con certificados generados y verificables;
- potenciales comunes y truth θ_A calculada desde la intervención definida, independiente de Z y G;
- salida Analyzer para θ_A solo cuando gates observables de identificación se cumplan; en otros escenarios, bounds/abstención/NOT_IDENTIFIED.

No se aceptan extremos deterministas ni kernels/masas arbitrarios para fabricar positividad. Los valores se escogerán para demostrar recuperación en mundos identificados y abstención correcta en mundos sin soporte, con vía directa o régimen común fallido.

### S-B3 — EventHistory y adjudicación temporal ejecutables

No basta con generar potential_interval_truth mediante una secuencia Markov por intervalos. El harness debe materializar:
- estado inicial post-Z en t0 por unidad y potencial;
- transiciones truth con identidad propia, versión de historia, familia causal, event_time, estado before/after y provenance;
- persistencia entre transiciones;
- simultaneidad atómica y suborden solo para estados intermedios reales;
- completitud de historia y regeneración/versionado inmutable;
- separación de antecedentes PROCESS_EVENT, EventHistory truth y observaciones S3;
- operador IntervalAdjudication conforme a DEC-C10-100…104, R144-A y Gate 154;
- cálculo de V_cont y bounds desde intervalos adjudicados, no desde observación ni desde aproximación Markov que omita tiempos de evento.

No se crea un segundo PROCESS_EVENT ni se transforma el registro observacional en truth.

### S-B4 — Temporalidad numérica del benchmark

§51 ya fija el sistema de coordenadas. Para el DGP sintético se seleccionarán y versionarán:
- soporte causal finito normalizado y distribución/familia de tiempos de transición;
- ρ_follow y T*;
- K y Δ;
- duraciones y recurrencias de episodios;
- escenarios de recuperación y episodios terminales/censurados.

La selección se hará por cobertura del soporte generativo, cruce de fronteras, aliasing, sensibilidad a fase y estabilidad al refinar K. No se necesita duración física ni calibración externa. Si el DGP estipula un soporte finito, ese soporte es conocido por construcción; su suficiencia se somete a sensibilidad y escenarios adversariales.

### S-B5 — S3 sintético completo

El harness ya incluye sensibilidad, especificidad, missingness e interferencia como parámetros, pero eso no materializa por sí solo el contrato temporal S3. Se completará la proyección de EventHistory a observaciones S3 con cadencia/fase, lag/desorden, pérdida/cobertura, falsos positivos/negativos y dependencia entre señales, por familia y versión.

S3 se genera después de la verdad. Sus fallos nunca modifican EventHistory ni se convierten en UNKNOWN funcional. Analyzer recibe solo evidencia proyectada y sellada.

### S-B6 — Población, asignación e interferencia sintéticas

No se buscará ni exigirá población real. Se materializarán unidades sintéticas con identidad/versionado, covariables basales, estratos, potenciales y semillas separadas. Se especificarán unidad de asignación y probabilidades π_h por escenario. El núcleo limpio tendrá independencia por construcción y pruebas del generador; escenarios adversariales introducirán interferencia conocida, con unidad de cluster/mapa de exposición y estimando compatible. Gate 121/122 no es prueba de aislamiento sintético ni se traslada un PASS S al carril M.

### S-B7 — Outcomes y puente a Value

V_cont tiene truth y selección provisional, pero no está probado el puente V_cont → consecuencia B1 → Value contextual. La operacionalización B2–B3/Outcome-Value se mantiene como dependencia del Paquete C: Need_preZ, consecuencia valorada, beneficiario, perspectiva/autoridad, horizonte y regla de valoración. No se sustituirá Value por V_cont ni se proclamará θ_A como efecto general sobre ΔValue sin ese puente.

## 5. Estrategia de materialización — un único ciclo integrado

1. Cerrar la instancia sintética del ledger existente: seleccionar roles/escenarios mínimos confirmatorios y adversariales de los doce roles C1/C3; fijar parámetros y relaciones conjuntas versionados; conservar matriz 13×52 y extenderla solo mediante su contrato rector si falta cobertura específica θ_A.
2. Extender el Generator integrado: representar D2 por etapas y generar q_X*, g_A0/g_A1, r_common, potenciales completos y truth θ_A.
3. Materializar EventHistory: transiciones con event_time, identidad, versión y completitud; conectar operador temporal y V_cont.
4. Completar S3: proyectar verdad a observación imperfecta con parámetros explícitos, sin fuga de truth.
5. Cerrar asignación e interferencia: independencia por construcción para núcleo; escenarios separados para spillovers/no-identificación.
6. Completar Outcome/Value en Paquete C: no bloquear la prueba de recuperación de θ_A sobre V_cont por una pretensión no sustentada de Value general.
7. Reutilizar tests/contracts existentes; añadir solo casos indispensables para D2, EventHistory, theta_A, firewall, fronteras temporales, soporte, missingness, interferencia y abstención.
8. Usar el protocolo de seed banks existente; no reutilizar P178 como evidencia de potencia para θ_A; congelar N/R y criterios antes del banco de evaluación.
9. Reutilizar Gates 164–205, completar validaciones pendientes y producir manifiestos/hashes para el artefacto ejecutado.

## 6. Criterio de suficiencia del núcleo sintético

El núcleo estará materializado cuando una ejecución técnica reproducible demuestre, sin acceso del Analyzer a truth:
- DGP y potenciales coherentes por unidad/escenario;
- EventHistory completa y adjudicación V_cont correcta en fronteras y simultaneidad;
- D2 por etapas sin colapsar asignación, provisión, instalación y accesibilidad;
- q_X*, g_A0/g_A1 y r_common operativos y con soporte verificable;
- truth θ_A independiente, calculada por Evaluator;
- Analyzer recupera θ_A en escenarios identificados y se abstiene en los no identificados;
- S3 imperfecto sin convertir missingness en UNKNOWN funcional;
- controles nulos, adversos, directos/colaterales, heterogéneos, interferentes y de falta de soporte;
- N/R y precisión Monte Carlo justificadas por escenario/estimando;
- fuente, configuración, seeds, runtime, outputs y replay identificados y auditables.

La salida científica puede ser PASS, CONDITIONAL, PARTIALLY_IDENTIFIED o NOT_IDENTIFIED. No se optimizará el DGP para obtener PASS.

## 7. Autorización y límites

La instrucción expresa del usuario de materializar lo que falta se interpreta como autorización para **implementar el carril sintético S** en research/c10-s-consolidation-draft: schemas/fixtures sintéticos, extensión del Generator/TruthBundle/EventHistory/IntervalAdjudication/S3/Analyzer/Evaluator y tests asociados, reutilizando artefactos existentes.

No autoriza materialización/captura M, acceso a sistemas externos, promoción a main, cierre/merge de PR #116, dispatch de workflows, ejecución de tests, calibración, generación de bancos, Monte Carlo, estimación o experimento científico.

- implementation_authorized=true — exclusivamente materialización sintética S;
- technical_test_execution_authorized=false;
- scientific_execution=false;
- execution_authorized=false;
- material_lane_authorized=false.

## 8. Siguiente operación

Preparar un único delta de implementación en el harness existente, empezando por S-B1/S-B2/S-B3 como bloque indivisible (D2 + q_X*/g_A/r_common/θ_A + EventHistory/IntervalAdjudication). No abrir Gates separados para cada campo. Después, completar S3 y calibración temporal; Outcome/Value contextual continúa en Paquete C.

No se crean escenarios por defecto, no se crea un roster conceptual nuevo, no se repite Gate 121/122 y no se reabren decisiones aceptadas.
