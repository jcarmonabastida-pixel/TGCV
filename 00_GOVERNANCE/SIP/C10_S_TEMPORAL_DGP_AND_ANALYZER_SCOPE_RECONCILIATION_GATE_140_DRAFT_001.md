# C10-S — Gate 140: reconciliación del DGP temporal, mapping post-Z y alcance inicial del Analyzer

**Fecha:** 2026-11-16  
**Rama:** research/c10-s-consolidation-draft · PR #116 (Draft)  
**Estado:** HISTORICAL_RECONCILIATION_COMPLETED / EXISTING_DGP_TEMPORAL_SPEC_REUSED / POST_Z_STAGE_MAPPING_DEFINED_AT_CONTRACT_LEVEL / INITIAL_ANALYZER_SCOPE_SUPPORTED / NO_NEW_DECISION_REQUIRED_FOR_THE_THREE_QUESTIONS / IMPLEMENTATION_NOT_AUTHORIZED / NO_EXECUTION / NO_GLOBAL_DESIGN_FREEZE.

## 1. Objeto y reconstrucción histórica

Gate 140 responde a las tres dependencias señaladas tras Gate 139. La inspección se hizo contra los artefactos existentes, no solo contra el resumen conversacional.

Fuentes revisadas:
- 00_GOVERNANCE/README.md (main), CHATGPT_BOOTSTRAP.md, CANONICAL_STATE.json, STATUS.md y HISTORICAL_RECONSTRUCTION_BEFORE_NEW_WORK_RULE_v0.1.md.
- DEC-C10-100…104 y Gate 135–139.
- DGP temporal y de roles §§49–55, más el mapping estructural posterior W_programmed → W_attempt → receipt → S_install → C_dep*.
- C10-S Integrated V_cont Analysis Contract, en particular §§1, 5, 6 y 7.
- vcont_integrated_harness.py (blob 88c6c7bd6f82353e64a4f12edbe2e2abc2cec002) y focal_harness.py (blob 8ff4e66f04cbd6f28e95313cf3b8250c29ebe9e2).
- Path Predicate Temporal Evidence Matrix y P182/P183/MEAS/MISS por referencias del contrato.

No se ejecutó código, tests, validadores, workflows, generación, simulación ni calibración.

## 2. Dictamen ejecutivo

Las tres preguntas de Gate 140 ya tienen respuesta suficiente en contratos existentes. No justifican una nueva semántica, otra DEC, un ledger, un escenario ni un schema:

1. El DGP temporal §§49–55 contiene la especificación lógica temporal necesaria y reutiliza el roster de perfiles y pruebas existentes. Su estado documental sigue siendo DRAFT/propuesto; Gate 140 no lo convierte en contrato aceptado o frozen.
2. El mapping post-Z de provisión e instalación está definido a nivel de etapas y efectos funcionales. La cadena W_programmed → W_attempt → receipt → S_install → C_dep* distingue programación, intento, recepción, instalación y éxito técnico. DEC-C10-101 fija la ventana desde inmediatamente después de Z e incluye el proceso. Las etapas de provisión/instalación no son por sí mismas fallos B1: solo cuentan los cambios efectivos de ENABLED/PROFILE y demás condiciones constitutivas de admisión.
3. El Analyzer inicial puede limitarse a la ruta puntual ideal y a abstención ante medición/missingness no resuelta. El contrato integrado exige S3 perfecto y completo para la identificación puntual actual; errores o ausencias no corregidos por un método aprobado llevan a INDETERMINATE. No existe un método de bounds aprobado para este Analyzer. Por tanto, no se implementan ni se reportan bounds como si estuvieran disponibles.

**Resultado:** no hace falta ampliar el diseño lógico para resolver estas tres cuestiones. Sí falta materializar en el harness el contrato temporal existente y verificar su conformidad en una fase futura autorizada.

## 3. Estado del DGP temporal §§49–55

La reconstrucción identifica cobertura documental ya existente:

| Sección | Contenido existente | Estado |
|---|---|---|
| §49 | Inventario B1, ENABLED/PROFILE, provisión/instalación, runtime, solicitudes y separación de relojes | Definido en DRAFT |
| §50 | Cinco familias de transición funcional y distinción truth/detectabilidad S3 | Definido en DRAFT |
| §51 | Coordenada temporal normalizada, canal S3 pasivo y curva de detección | Definido; calibración abierta |
| §52 | Horizonte común ex ante y censura terminal | Definido; soporte y parámetros abiertos |
| §53 | Reutilización de perfiles DGP y mapping P182/P183/MEAS/MISS | Definido; no ejecutado |
| §54 | Cobertura temporal adimensional y contrastes dirigidos | Definido; parámetros/criterios abiertos |
| §55 | Registro paramétrico y orden Generator → truth → S3 → Analyzer → Evaluator | Definido; no materializado íntegramente |

Las decisiones aceptadas DEC-C10-100…104 prevalecen donde fijan reglas normativas. El contrato DGP temporal puede conservar el detalle técnico restante como contrato de trabajo, pero debe pasar por una aceptación/versionado explícitos antes de ser tratado como baseline congelado. No es necesario aprobar cada subsección mediante una DEC separada. La aceptación del contrato no fija automáticamente K, Δ, T*, τ_follow, unidad, resolución, soporte, p* ni parámetros de calibración.

## 4. Mapping post-Z de provisión e instalación

La secuencia ya está representada conceptualmente en el contrato D2 y en el DGP:

W_programmed → W_attempt → receipt → S_install → C_dep* → A_f*/D_f*.

Las etapas no se colapsan:
- W_programmed es programación/prescripción, no ejecución ni cumplimiento.
- W_attempt es intento efectivo, no recepción ni instalación.
- receipt registra recepción/disponibilidad.
- S_install y sus componentes de instalación/verificación determinan el éxito técnico según el contrato.
- C_dep* deriva del conjunto de componentes técnicos, no de una etiqueta de instalación aislada.

Para V_cont, la ventana funcional comienza en t0 inmediatamente después de Z conforme DEC-C10-101. La provisión e instalación transcurren dentro de esa ventana. Sin embargo, no se infiere que una etapa incompleta produzca automáticamente A_B1=0: se registra su efecto sobre la capacidad funcional efectiva. A_B1 se adjudica desde ENABLED/PROFILE y las condiciones funcionales constitutivas de B1. Las transiciones de proceso, listener, dependencia o capacidad solo afectan la truth cuando cambian la función de admisión.

Por tanto, el vacío restante es de materialización: el harness actual usa provision_ok como variable binaria y no conserva la cronología diferenciada ni las transiciones funcionales fechadas. No falta una nueva regla causal para decidir qué significa cada etapa.

## 5. Alcance inicial admisible del Analyzer

El contrato integrado vigente establece:
- punto-identificación solo bajo S3 perfecto y completo;
- missingness o error no corregidos por un modelo aprobado llevan a INDETERMINATE;
- sin complete-case substitution silenciosa;
- el Analyzer no recibe TruthBundle, potenciales ni parámetros reservados;
- Evaluator abre truth después de finalizar Analyzer y valida identidad, versiones, hashes y abstención.

En consecuencia, la ruta inicial acotada es:

| Condición observacional | Salida Analyzer admisible en el alcance actual |
|---|---|
| S3 perfecto, completo, identificado y versiones coherentes | Estimación puntual para los estimandos implementados |
| Missingness/error/lag que impide identificación y no tiene corrección aprobada | INDETERMINATE / abstención |
| Bounds parciales | No habilitados: requieren contrato, método y garantías aprobados |

Esta ruta es suficiente para continuar con el benchmark ideal y los controles adversariales de abstención que ya existen. No acredita recuperación bajo S3 imperfecto, ni habilita un estimador general de V_cont temporal. Tampoco convierte ITT-Z o ITT-G en θ_A. Los bounds de V_cont y los bounds causales de θ_A permanecen fuera del alcance implementado.

## 6. Reconciliación con Gates 138–139

Gate 138 y Gate 139 siguen siendo correctos en el diagnóstico de la implementación: el harness no materializa EventHistory ni la adjudicación temporal estricta; TruthBundle actual conserva arrays binarios; Analyzer/Evaluator no implementan bounds V_cont.

La precisión que añade Gate 140 es que la semántica lógica de eventos, relojes, familias, ventana y orden de generación no está ausente del repositorio: ya figura en DGP §§49–55 y en el mapping estructural post-Z. Por tanto, no debe recrearse. Gate 139 queda como especificación lógica de correspondencia; Gate 140 identifica las fuentes existentes que deben reutilizarse y limita la salida inicial del Analyzer.

## 7. Decisión operativa y límites

**Recomendación de Gate 140:** no abrir otra decisión semántica para estas tres cuestiones. Reutilizar el DGP temporal existente, mantener la ruta Analyzer ideal + abstención y tratar la cronología post-Z como requisito de materialización del harness.

Esta recomendación no es una aceptación formal del DGP temporal ni una autorización de implementación. El siguiente paso de gobernanza es una revisión de aceptación/versionado del DGP temporal y un delta de implementación trazable contra los contratos existentes. Solo después, y mediante autorización independiente, podría modificarse código o tests.

El cierre de estas tres cuestiones tampoco cierra C10-S global: θ_A/q_X*/g_A/r_common, identificación causal, soporte/interferencia, calibración, N/R/MCSE, criterios de recuperación y relación causal con Value mantienen sus propios estados.

No se modifica DEC-C10-100…104, el Decision Log, el DGP, schemas, código, fixtures, tests, workflows, RMA, Evidence→Claim Matrix, STATUS, main ni PR base.

scientific_execution=false  
execution_authorized=false
