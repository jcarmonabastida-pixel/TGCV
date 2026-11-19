# C10-S — Gate 125: auditoría de suficiencia del ledger DGP existente y dependencias reales de Design Freeze

**ID:** C10-S-EXISTING-DGP-LEDGER-SUFFICIENCY-125  
**Fecha:** 2026-11-16  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** EXISTING_LEDGER_REUSED / SCENARIO_ROSTER_CONCEPTUALLY_SUFFICIENT / PARAMETER_SCHEMA_DEFINED / STRUCTURAL_AND_SEMANTIC_BLOCKERS_OPEN / VALUE_ENDPOINT_NOT_CONFIRMATORY / NO_DESIGN_FREEZE / NO_IMPLEMENTATION / NO_EXECUTION  
**Precedencia:** decisiones aceptadas DEC-C10-095, DEC-C10-099…103; plan integrado §§16.188–16.229 y 16.235–16.270; DGP/PD/PE; Gates 90–93, 118–124; contratos Outcome/Value B2–B3 y B1.

## 1. Dictamen ejecutivo

La operación propuesta por Gate 124 —consolidar el ledger mínimo de escenarios y parámetros— ya cuenta con trabajo sustancial y específico en el plan y sus contratos. En particular:

- §§16.188–16.212 ya integran el universo finito candidato, los perfiles R0–R3, el roster dirigido de mecanismos, las funciones generadoras, los potenciales contrafactuales, truth/observed/evaluation y la separación Generator–Projector/Sealer–Analyzer–Evaluator.
- §16.223 (Gate 69) ya define el esquema único del ledger por celda, los campos de población, asignación, intervención, efecto, funciones activas, invariantes, régimen común, soporte, interferencia, observación, oráculo, información del Analyzer y criterio de aceptación.
- §§16.224–16.225 (Gates 70–71) ya auditan la cobertura conceptual del roster y definen doce roles de contraste C1/C3. Son roles de celda, no doce mundos adicionales.
- §§16.229–16.236 (Gates 76–86) ya distinguen representabilidad del Generator, la asignación G, las intervenciones g_A, q_X* y r_common. Concluyen que G no equivale a g_A y que θ_A no está materializado.
- Gates 90–93 y 118–120 detectan las brechas de cobertura C1/C3, la ausencia de la cadena generativa D2 en el harness actual y las decisiones P0; DEC-C10-103 acepta la arquitectura de trabajo, no sus condiciones de identificación.

**Conclusión:** no hace falta crear otro ledger, ampliar por defecto el roster ni inventar escenarios o parámetros. La brecha principal no es falta de una tabla paramétrica: son contratos estructurales, semánticos y de identificación que todavía no pueden rellenarse de forma válida. Gate 125 reutiliza y clasifica el ledger existente, corrige la ruta de Gate 124 y fija las dependencias reales de cierre.

Este Gate se refiere al carril S sintético. No adjudica el aislamiento material del carril M ni utiliza el paquete de procedencia/serialización como sustituto de la especificación causal.

## 2. Reconstrucción y reutilización obligatoria

| Fuente existente | Qué ya aporta | Estado que no debe exagerarse |
|---|---|---|
| Plan §§16.188–16.198 | Ledger estructural y temporal; familias de parámetros, dependencias, tiempos, observación y calibración | Estructura definida; valores, distribuciones y leyes conjuntas OPEN |
| Plan §§16.205–16.212 | DGP abstracto, universo finito candidato, roster dirigido, funciones y potenciales coherentes | No es DGP cuantitativo completo ni fixture materializado |
| Plan §16.218 | Criterios de recuperación, bounds, abstención y evaluación por estimando | Tolerancias y criterios cuantitativos finales OPEN; no demuestra recuperación |
| Plan §§16.219–16.220 | Marco para α, precisión, relevancia, potencia y dimensionamiento sin MDE arbitrario | Márgenes y valores normativos no fijados |
| Plan §16.223 / Gate 69 | Esquema del ledger por celda y regla r_common | Materialización celda a celda, soporte y parámetros numéricos OPEN |
| Plan §§16.224–16.225 / Gates 70–71 | Suficiencia conceptual del roster y doce roles C1/C3 | Cobertura efectiva y verdades por celda NOT_VERIFIED/NOT_MATERIALIZED |
| Plan §§16.226–16.229 / Gates 73–76 | Tres verdades, g_A, identificación observable y auditoría de factibilidad | La verdad θ_A no es recuperable desde el contraste G actual |
| Plan §§16.230–16.236 / Gates 77–86 | Contrato g_A, soporte, q_X*, r_common y no equivalencia G↔g_A | No existe par operativo g_A0/g_A1 ni soporte conjunto acreditado |
| Plan §§16.240–16.243 / Gates 90–93 | Cobertura del harness, mismatch D2/Z y crosswalk de etapas | La cadena causal D2 no está materializada en el harness |
| DEC-C10-099…102 | V_cont provisional y reglas iniciales de agregación/tiempo/continuidad | No cierran T*, Δ, K, S3, validez, calibración ni endpoint confirmatorio |
| DEC-C10-103 / Gate 118–120 | Arquitectura causal aceptada con condiciones | No materializa roster, asignación, soporte, mapping ni identificación |
| Gates 123–124 | Alcance sintético/material separado y auditoría IS-1…IS-8 por carril | No cierra los parámetros ni la arquitectura causal |

La secuencia anterior es acumulativa. Gate 125 no reemplaza sus artefactos ni los reabre; identifica qué dependencias siguen siendo bloqueantes y cuáles ya tienen contrato suficiente para no volver a redactarse.

## 3. Estado del roster y del ledger

### 3.1 Roster de escenarios

Se reutilizan los perfiles estructurales R0–R3 y las clases/mecanismos adversariales ya inventariados en §§16.188, 16.208 y 16.211: focal limpio, nulo, fallo por etapas, focal adverso, alternativa basal, alternativa afectada/colateral, vía directa, heterogeneidad, IV adversarial, interferencia, observación adversarial y soporte/ausencia/censura.

No se exige factorial completo. Cada clase debe cubrir un contraste o falsador identificable y justificar por qué no está ya cubierto por otra clase. La auditoría de cobertura de Gate 70 concluyó que el roster es conceptualmente suficiente para los falsadores principales C1/C3; Gate 90 y Gate 91 precisaron que la cobertura efectiva del harness no lo es.

### 3.2 Roles de celda

Los doce roles existentes de Gate 71 se conservan: seis para ITT-D2/C1 y seis para θ_A/C3 (positivo, nulo propio, negativo, desacoplamiento/vía directa o colateral, heterogeneidad y no-identificación/abstención). No son doce nuevos mundos y no se rellenan por analogía con etiquetas de escenario.

### 3.3 Esquema del ledger

El esquema de §16.223.2 ya exige, como mínimo: world_id/version, estimand_id, population_id, assignment_id, intervention_id, effect_cell, active_functions, held_fixed, r_common_status, support_status, interference_status, observation_profile, oracle_identification, analyzer_information y acceptance_target.

El esquema está **cerrado estructuralmente**. Sus registros por celda, historias q_X*, masas, probabilidades π_h, intervenciones g_A, valores de efecto, funciones activas, invariantes y perfiles de observación siguen sin materializarse. No debe confundirse «esquema de ledger definido» con «ledger poblado» ni con «cobertura confirmatoria demostrada».

## 4. Matriz de brechas reales: parámetro, contrato estructural o materialización

| Dominio | Qué existe | Brecha real | Clasificación |
|---|---|---|---|
| Universo y topología | R0–R3, S0/S1/S2/SF, F1/F2/A1/A2 y rutas candidatas | Frontera, cardinalidades, G/H, exhaustividad, F*, mappings y comparabilidad no cerrados | CONTRATO ESTRUCTURAL |
| Funciones D2 | DEC-C10-067 define la cadena de política D2 | El harness actual no representa B/W_programmed/W_attempt/receipt/S_install/C_dep*/A_f*/D_f* como etapas separadas; provision_ok no es sustituto válido | AUSENCIA ESTRUCTURAL |
| ΔT_acc* | Vector de cuatro coordenadas en el harness actual | Su generación actual depende de G; no representa la cadena D2→ΔT_acc* ni el mapping completo de D2 | MAPPING ESTRUCTURAL |
| θ_A | Estimando definido por DEC-C10-103 y contratos g_A | G es una asignación auxiliar distinta; no existe par operativo g_A0/g_A1, truth θ_A ni estimador focal | BLOQUEO DE IDENTIFICACIÓN/INTERVENCIÓN |
| Población y q_X* | Definición simbólica de q_X* y precedencia P*τ2 | Roster sintético versionado, historias basales, masas y soporte conjunto de g_A no materializados | MATERIALIZACIÓN DGP |
| Asignación/interferencia | Cuatro arquitecturas A–D descritas; DEC-C10-103 acepta individual solo bajo aislamiento | π_h, RNG/provenance, UE/UA/cluster y G_i por mundo no cerrados; el harness focal no implementa motor cluster/G_i | CONTRATO Y SOPORTE |
| V_cont | DEC-C10-099…102 aceptan selección provisional, agregación igualitaria, t0 y continuidad estricta | T*, Δ, K, resolución, soporte temporal y calibración/detectabilidad S3 siguen OPEN | MEDICIÓN |
| Outcome | O-CONF/F* conserva un anclaje técnico candidato | Oráculo, predicados, mapping, snapshots, ventana y validez no permiten Y confirmatorio completo | MEDICIÓN/ADJUDICACIÓN |
| Value contextual | B1/Need_preZ y la separación B2–B3 están descritos | Consecuencia concreta para B1, autoridad de valoración y puente validable entre V_cont y la consecuencia valorada no están cerrados | CONSTRUCTO/VALIDEZ |
| Observación | Projector/Sealer y canal S3 tienen contratos lógicos | Error, pérdida, lag, cobertura, dependencia, missingness/censura y calibración no fijados; el point identification del harness exige S3 perfecto/completo y no implementa corrección por error calibrado | MEDICIÓN/IDENTIFICACIÓN |
| Analyzer/Evaluator | ITT-Z y contraste G están separados; salida sellada y evaluación posterior | θ_A no estimado; bounds no implementados como salida validada; recuperación, heterogeneidad y abstención no acreditadas | CAPACIDAD ANALÍTICA |
| Criterios cuantitativos | P177/P178/P179/P182/P183 y §16.219 ofrecen marco | α, precisión, potencia mínima, MDE justificable, tolerancias, N, R y SE_MC no fijados | CUANTIFICACIÓN |
| Firewall | Separación lógica y allowlist a nivel aplicación | No equivale a frontera de seguridad efectiva; threat model, ACL/secretos, side-channel y pruebas de rol siguen pendientes | IMPLEMENTACIÓN/SEGURIDAD |

Los parámetros numéricos no pueden reparar una ausencia estructural. En particular, no se debe asignar una tasa de cumplimiento para simular D2 si falta la función que separa programación, intento, recepción, instalación y dependencia; tampoco se debe elegir un kernel numérico para g_A antes de que el dominio semántico conjunto, q_X* y el soporte estén definidos.

## 5. Hallazgo crítico: V_cont provisional no cierra por sí solo Value contextual

DEC-C10-099 acepta provisionalmente V_cont como dimensión mínima única de Value para la extensión sintética B; DEC-C10-100…102 fijan aspectos de su verdad temporal. Esas decisiones deben respetarse, pero sus propios límites mantienen abiertos medición, identificación y validez.

A la vez, B2–B3 y la reconciliación Outcome/Value definen Value como valoración contextual de una consecuencia para B1 respecto de Need_preZ, desde una perspectiva y autoridad estipuladas ex ante. V_cont describe continuidad temporal de la capacidad funcional del servicio B1. Para tratarlo como dimensión de Value confirmatoria debe existir un puente explícito y no circular entre:

1. la continuidad funcional del servicio (truth V_cont);
2. la consecuencia que esa continuidad produce —o no produce— para B1 respecto de su propósito basal;
3. la regla/perspectiva/autoridad que valora esa consecuencia.

La selección provisional de V_cont no demuestra por sí sola ese puente, no instancia Need_preZ por UE, no determina la consecuencia B1 y no valida el instrumento. Tampoco se debe descartar V_cont ni sustituirlo por O-CONF: la cuestión queda OPEN para reconciliación con DEC-C10-099 y B2–B3.

Por tanto, el objetivo focal aceptado por DEC-C10-103 es actualmente θ_A sobre V_cont, no una demostración general de ΔT_acc*→Value. La conexión con Value contextual permanece condicionada a la validez de V_cont y a su relación con la consecuencia valorada de B1.

## 6. Dos corrientes técnicas que no deben mezclarse con el cierre científico

El harness integrado `vcont_integrated_harness.py` (blob `88c6c7bd6f82353e64a4f12edbe2e2abc2cec002`) y su README (blob `f835b92d06aec9693c24ce92d82e0d47de3be1cf`) declaran una implementación parcial de V_cont, no ejecutada ni confirmatoria. El código distingue ITT-Z e ITT-G|Z=0 y mantiene `theta_a_truth=None`; no contiene aún la cadena D2 completa ni un estimador θ_A. La documentación del harness aún contiene etiquetas históricas que describen G como g_A; prevalecen Gate 86 y el contrato explícito de que G no equivale a g_A.

La secuencia Gates 181–199 trata captura, serialización, verifier, procedencia y materialización de evidencia del benchmark. Es una corriente de integridad del paquete/ejecución. Gate 199 deja como siguiente operación un registro de perfiles de ejecución y cierre de fuentes consumidas. Esa corriente no rellena el DGP causal, no acredita θ_A y no convierte pruebas de serialización en evidencia de recuperación científica. Debe continuar separada.

## 7. Dependencias mínimas antes de congelar el diseño científico

Se fija el siguiente orden de dependencias, reutilizando el trabajo existente:

1. **Admisibilidad de Value:** reconciliar el puente V_cont→consecuencia B1→valoración, respetando DEC-C10-099…102 y B2–B3. Si no puede justificarse, mantener V_cont como resultado sintético provisional y no denominarlo Value confirmatorio.
2. **Cadena causal D2:** especificar las funciones y potenciales separados desde Z/política hasta ΔT_acc*, sin colapsar programación, intento, recepción, instalación, C_dep*, A_f* y D_f*.
3. **Intervención focal:** definir g_A0/g_A1 sobre el vector completo ΔT_acc*, q_X* y soporte conjunto, manteniendo r_common; no sustituirlos por G ni por la primera etapa G→ΔT_acc*.
4. **Población/unidad/asignación/interferencia sintéticas:** versionar el roster DGP y la arquitectura por escenario; definir aislamiento por construcción o la unidad/mapa de exposición compatible. No inferir de ello aislamiento material M.
5. **Observación y adjudicación:** cerrar S3, error/cobertura/missingness, F*/O-CONF, T*/Δ/K, y las reglas Analyzer/Evaluator, bounds y abstención.
6. **Cobertura final del roster:** mapear los falsadores y los doce roles C1/C3 a clases existentes; solo justificar nuevas clases si se demuestra una ausencia irreducible.
7. **Criterios cuantitativos:** derivar márgenes, precisión, potencia, N/R y SE_MC de los estimandos y escalas ya definidos; no importar valores de P178 ni fijar defaults.
8. **Freeze:** solo después de que las dependencias anteriores estén cerradas y sus contratos sean coherentes. La autorización de implementación y la ejecución científica seguirán siendo decisiones separadas.

Este orden no implica que todo deba materializarse antes de una especificación documental completa; sí impide llamar confirmatorio, identificado o congelado a un diseño cuyas piezas esenciales no tienen definición suficiente.

## 8. Dictamen final y siguiente operación

**Gate 125 concluye:**

- El ledger paramétrico estructural ya existe y debe reutilizarse.
- El roster conceptual actual no justifica ampliación por defecto.
- Los doce roles C1/C3 ya están especificados, pero su cobertura efectiva no está verificada.
- La brecha prioritaria no es poblar cifras: es resolver la validez de V_cont como dimensión de Value contextual y cerrar las funciones D2/g_A que el Generator no representa todavía.
- No estamos cerca de Design Freeze para la pregunta causal ΔT_acc*→Value. Sí existe una arquitectura candidata suficientemente desarrollada para concentrar el trabajo en un conjunto reducido de dependencias estructurales y semánticas, sin reiniciar el diseño.

**Siguiente operación:** Gate 126 — auditoría de consistencia y admisibilidad del puente V_cont→consecuencia B1→Value, cotejando DEC-C10-099…102, B2–B3, B1 Valuation Case, Outcome/Value Operationalization y P179/P182/P183. Debe determinar qué parte del puente está ya aceptada, cuál solo está propuesta y qué decisión explícita o definición mínima falta. No elegir una dimensión sustituta, no alterar DEC, no inventar Need_preZ/autoridad/indicadores y no ejecutar.

**Límites:** no se modifica código, DGP, schemas, U_G, C0, DEC, RMA, Evidence→Claim Matrix, STATUS o main; no se crean test IDs ni mundos nuevos; no se ejecutan validadores, tests, workflows, simulaciones, estimaciones, calibraciones, productores ni benchmarks. PR #116 permanece Draft. `scientific_execution=false`; `execution_authorized=false`.

**Resultado:** EXISTING_LEDGER_SUFFICIENT_AS_SCHEMA / NO_NEW_ROSTER_REQUIRED / D2_CHAIN_NOT_REPRESENTED / G_NOT_G_A / THETA_A_NOT_MATERIALIZED / VCONT_VALUE_BRIDGE_OPEN / NO_DESIGN_FREEZE / NO_IMPLEMENTATION / NO_EXECUTION.
