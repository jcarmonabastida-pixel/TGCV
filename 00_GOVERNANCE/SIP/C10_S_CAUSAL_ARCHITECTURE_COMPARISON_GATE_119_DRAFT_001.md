# C10-S — Gate 119: comparación de arquitecturas causales y recomendación para D2/Value

**ID:** C10-S-GATE-119-CAUSAL-ARCHITECTURE-COMPARISON-001  
**Fecha:** 2026-11-15  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft  
**Estado:** HISTORICAL_DECISIONS_RECONCILED / FIVE_P0_OPTIONS_COMPARED / CONDITIONAL_ARCHITECTURE_RECOMMENDED / OWNER_APPROVAL_REQUIRED / MATERIAL_AND_QUANTITATIVE_GATES_OPEN / NOT_DESIGN_FROZEN / NOT_IMPLEMENTATION_READY / NO_EXECUTION.

---

## 1. Propósito y dictamen

Gate 119 compara las cinco decisiones P0 de Gate 118 con la pregunta científica C10-S: determinar si una intervención sobre la accesibilidad transformacional completa puede contribuir causalmente a Value, sin confundir ese efecto con el efecto total de asignar un paquete técnico.

**Dictamen:** existe una combinación de diseño preferible para desarrollar como propuesta, pero no puede aprobarse ni materializarse por inferencia documental. Se recomienda un DGP B versionado para la pregunta de Value, con A preservado como referencia técnica; asignación D2 individual bajo aislamiento material demostrado; target medio por UE; \(\theta_A\) como estimando focal de atribución; ITT-D2 como efecto de política separado; C4 como análisis mediador secundario condicionado a identificación; y continuidad UE acotada a cada roster/versionado, con matching entre variantes solo mediante crosswalk explícito.

Esta recomendación es condicional. Si el aislamiento no puede demostrarse, la arquitectura individual A no se considera válida por defecto: el resultado debe pasar a un régimen de interferencia mapeada/cluster formalmente especificado o a abstención/bounds.

## 2. Reconstrucción histórica y precedencia

Se reutilizan, sin reabrir ni sustituir:

- Gate 118 y §§16.185–16.218 del plan maestro.
- DEC-C10-066: D2 escenario primario candidato; D1 secundario.
- DEC-C10-067: políticas materiales D2 y separación Z → política → intento programado/efectivo → instalación → dependencia → accesibilidad.
- DEC-C10-095: A permanece como DGP de referencia; B se autoriza como extensión sintética separada y versionada para incorporar consumidor/beneficiario, demanda pre-Z y perspectiva/criterio de valoración explícitos. B no reescribe A; resultados B solo prueban recuperación de la relación causal estipulada en ese DGP.
- DEC-C10-096: Need_preZ es el censo de todas las UE del roster DGP/package aprobado al que aplica el paquete; no decide por sí sola roster A/B separado o conjunto.
- Gate 110: arquitecturas de asignación/interferencia A–D y sus consecuencias analíticas.
- Gates 111–112: UNIT-01…14 como familia contractual primaria; cobertura documental no equivale a implementación/ejecución.
- Gates 115–117: `ue_id` y manifest existen en contratos Draft; roster no aprobado/materializado; UE→U_G root sigue UNKNOWN.
- Contratos existentes de G, \(g_A\), q_X*, r_common, ITT-Z y \(\theta_A\), que mantienen separados el mecanismo de asignación y la intervención sobre accesibilidad.

**Corrección de alcance de M03 (Gate 118):** DEC-C10-095 ya exige que A y B permanezcan como variantes DGP separadas, identificables y comparables. La cuestión no es si se fusionan en un único DGP (eso está descartado), sino si sus rosters contienen unidades distintas o si existe un spine basal común con matching legítimo. DEC-C10-096 deja abierta esa cuestión de roster para el paquete B1/Need. Gate 119 la recomienda, pero no la decide.

## 3. Comparación de las cinco decisiones P0

### P0-1 — Población y variantes A/B

| Alternativa | Ventaja | Riesgo/límite |
|---|---|---|
| A/B como una sola población/roster indiferenciado | Facilita comparación nominal | Puede mezclar el DGP técnico A con los elementos de Value estipulados solo en B; contradice la separación de variantes |
| A/B como DGP y rosters separados, con matching explícito opcional | Preserva A, delimita B y permite comparaciones emparejadas solo cuando hay equivalencia basal real | Exige crosswalk y soporte para cualquier comparación entre variantes |
| A/B totalmente inconexos sin posibilidad de matching | Máxima separación | Pierde comparaciones emparejadas potencialmente útiles |

**Recomendación:** mantener A y B como DGP/paquetes versionados distintos y usar rosters separados por defecto. Permitir un spine o matching entre unidades únicamente si se demuestra que representan la misma unidad basal sintética bajo definiciones, elegibilidad y variables pre-Z compatibles. No tratar A como brazo control de B ni calcular un único ITT mezclando ambas variantes.

La población confirmatoria del vínculo Value debe residir en B, porque es donde DEC-C10-095 permite estipular consumidor/beneficiario, demanda y criterio de valoración. A permanece como referencia técnica y no recibe una Value no estipulada.

### P0-2 — Unidad de asignación e interferencia

| Arquitectura | Evaluación para el DGP confirmatorio |
|---|---|
| A. Asignación individual aislada | Más parsimoniosa y coherente con UE y servicio B1 propios por unidad; válida solo con aislamiento material demostrado |
| B. Asignación por cluster | Válida si el mecanismo real opera por cluster; requiere roster, suficientes clusters, estimando/peso e inferencia al nivel de asignación, además de tratar spillover entre clusters |
| C. Asignación individual con mapa G_i | Permite modelar spillover, pero exige mapa versionado suficiente, probabilidades de exposición y soporte conjunto |
| D. Interferencia relevante no mapeada | No identifica el contraste simple; debe producir abstención o bounds, no una estimación individual convencional |

**Recomendación:** desarrollar A como arquitectura confirmatoria primaria por construcción, con una condición de entrada estricta: demostrar aislamiento de pools, dependencias mutables, agentes, canales, recursos, estado compartido, side effects y carryover entre UE. Dependencias o artefactos compartidos solo son compatibles con aislamiento si son inmutables/read-only o si su uso no transmite efectos entre unidades; debe justificarse para cada vía plausible.

B y C se conservan como mundos alternativos/adversariales de UNIT-01…14 y no se implementan por anticipado. D debe conservarse como falsador de identificación: si la interferencia está presente y no se puede mapear suficientemente, Analyzer debe abstenerse o devolver bounds. No se debe cambiar de A a B/C después de observar resultados.

Esta elección es una recomendación de diseño, no evidencia de que el aislamiento exista. Hasta que el inventario y la evidencia material lo acrediten, el escenario A permanece CONDITIONAL.

### P0-3 — Unidad y target de inferencia

**Recomendación:** si se satisface la arquitectura A, definir como target principal el promedio por UE dentro de la población B pre-Z elegible. UE es la unidad de potenciales/resultados y, solo bajo aislamiento demostrado, coincide con la unidad de asignación. El tamaño de la muestra inferencial no se sustituye por recuentos de instancias, rutas, episodios o intervalos V_cont.

Si el diseño cambia a B, la ponderación por UE y el promedio por cluster son estimandos distintos cuando los tamaños de cluster varían. La decisión deberá reabrirse antes de fijar el mecanismo; no se conservará automáticamente el estimando individual. En C, la población y ponderación deben declararse junto con la distribución de exposición.

No se propone ahora un estimando de cluster como co-primario.

### P0-4 — Jerarquía de estimandos y atribución

La pregunta central de C10-S es la contribución causal de la accesibilidad a Value. Por ello se recomienda:

1. **Estimando focal de atribución:** \(\theta_A(q_X^*,r_{common};V_{cont})\), definido sobre la distribución conjunta factible del vector completo \(\Delta T_{acc}^*\), en la población B y bajo la historia basal y régimen no focal expresamente fijados. Es el objeto que responde directamente a la intervención sobre accesibilidad; no equivale a una coordenada aislada ni a Z.
2. **ITT-D2:** efecto total de asignar el paquete material D2 sobre cada resultado preespecificado, incluido V_cont cuando su contrato de medición esté cerrado. Es un efecto de política/paquete, no una atribución automática a accesibilidad.
3. **C4:** análisis secundario de mediación interventional longitudinal, solo si se especifican intervención, historia, confusores post-Z, soporte secuencial, exposición y medición suficientes. No es requisito para renombrar o identificar \(\theta_A\).
4. **Efecto directo/no mediado:** fuera del núcleo confirmatorio por ahora. Solo se añadirá si se formula un estimando directo interventional coherente y se justifican sus supuestos. No definir residual como ITT−\(\theta_A\) ni como complemento algebraico de C4.

La confirmación de una relación causal de accesibilidad con Value requiere identificación propia de \(\theta_A\) y recuperación correcta por Analyzer frente a mundos conocidos del DGP. Un ITT-D2 positivo por sí solo no basta.

### P0-5 — Identidad y continuidad UE

**Recomendación:** identidad UE única e inmutable dentro del roster/package versionado al que pertenece, con versión/digest del roster y binding pre-Z. No exigir continuidad global de una misma clave entre A y B, ni entre versiones del DGP, réplicas o ejecuciones distintas.

Cuando A/B compartan legítimamente una unidad basal, utilizar un crosswalk de matching explícito y versionado, sin colapsar sus identidades de variante. Replay de una misma ejecución conserva la identidad del roster y de las unidades; una réplica nueva constituye una nueva realización experimental salvo que el contrato de reproducibilidad defina expresamente lo contrario.

Esto no crea un nombre de clave nuevo, no aprueba el campo Draft `ue_id`, no materializa roster y no resuelve UE→U_G root. Ese mapping sigue UNKNOWN y solo se cerrará si PE/estimando demuestra que es necesario y existe snapshot exacto.

## 4. Arquitectura recomendada integrada

La combinación preferida para someter a aprobación es:

- **Variante:** B, versionada y separada de A; Value solo se interpreta en el ámbito estipulado de B.
- **Comparador de política:** D2 conforme a DEC-C10-066/067; D1 permanece secundario.
- **Población:** censo pre-Z de las UE elegibles del roster B aprobado, conforme a DEC-C10-096; P*_{τ2} conserva su precedencia como población causal candidata según los contratos existentes. No filtrar por cumplimiento, accesibilidad post-Z, ejecución, O o V.
- **Asignación:** individual por UE solo si UE=UA y aislamiento material están demostrados.
- **Target:** promedio por UE.
- **Interferencia:** A como condición confirmatoria; B/C como alternativas adversariales explícitas; D como condición de abstención/bounds.
- **Atribución:** \(\theta_A\) como objetivo focal; ITT-D2 como efecto total de paquete; C4 secundario condicionado; efecto directo no incluido hasta especificación independiente.
- **Identidad:** roster B versionado; identidad UE local al roster; matching A/B solo mediante crosswalk justificado.

No se aprueba ninguna de estas recomendaciones. La aprobación requiere al responsable científico y no se infiere de la persistencia del gate.

## 5. Condiciones de rechazo y fallback

La recomendación no debe convertirse en una ruta de escape que fuerce la identificación:

- Si no se demuestra aislamiento, no declarar ITT individual bajo A.
- Si se adopta cluster, no usar número de UE como sustituto del número de clusters independientes; fijar previamente target y varianza.
- Si se adopta G_i, no afirmar suficiencia ni positividad sin relaciones, probabilidades y soporte conjunto.
- Si hay interferencia relevante no mapeada, clasificar el estimando como BOUNDS_ONLY / NOT_IDENTIFIED / INDETERMINATE según los contratos existentes.
- Si \(g_{A1}\) y \(g_{A0}\) no son factibles en q_X* o carecen de soporte común, \(\theta_A\) no queda identificado por extrapolación.
- Si B no contiene variación/support de Value o el criterio de valoración no está estipulado pre-Z, no se formula una conclusión confirmatoria sobre \(\Delta T_{acc}\to Value\).
- Si las vías colaterales de D2 afectan Value, ITT-D2 conserva interpretación como efecto del paquete; no se atribuye a accesibilidad por exclusión asumida.

## 6. Decisiones y trabajos que permanecen abiertos

### Requieren aprobación científica explícita
- Aceptar o rechazar la recomendación de rosters A/B separados con matching opcional.
- Aceptar o rechazar aislamiento individual como arquitectura confirmatoria condicionada.
- Aceptar target medio por UE.
- Aceptar \(\theta_A\) como estimando focal de atribución en B, con ITT-D2 separado y C4 secundario.
- Aceptar identidad UE acotada al roster versionado con crosswalk opcional.

### Requieren cierre documental/material posterior
- Contrato de población/roster B y elegibilidad pre-Z.
- Inventario y evidencia de aislamiento, o rediseño formal a B/C/D.
- Mecanismo Z, probabilidades, RNG, vector y provenance.
- Factibilidad/soporte de q_X*, g_A y r_common.
- Definición/medición S3 de V_cont y sus parámetros temporales.
- Vías colaterales, versiones, missingness, precisión/potencia y sensibilidad.
- Crosswalk Analyzer/Evaluator y criterios de recuperación/abstención.
- Mapping UE→U_G solo si se justifica como requisito técnico.

No se asignan valores a RNG, semilla, N, R, K, p*, MDE, potencia, tolerancias o parámetros de Value.

## 7. Dictamen

**Resultado:** `GATE_119_CONDITIONAL_CAUSAL_ARCHITECTURE_RECOMMENDATION / A_B_VARIANTS_KEPT_SEPARATE / D2_RETAINED_PRIMARY_CANDIDATE / INDIVIDUAL_ISOLATION_CONDITIONAL / UE_WEIGHTED_TARGET_RECOMMENDED / THETA_A_FOCAL_ATTRIBUTION_RECOMMENDED / ITT_D2_SEPARATE / C4_SECONDARY_CONDITIONAL / DIRECT_EFFECT_NOT_IN_CONFIRMATORY_NUCLEUS / OWNER_APPROVAL_REQUIRED / NO_FREEZE / NO_IMPLEMENTATION / NO_EXECUTION`.

Gate 119 cierra la comparación general de alternativas a nivel de recomendación. No cierra las decisiones P0 ni acredita las condiciones materiales de la arquitectura recomendada.

## 8. Gobernanza y autorización

- No se modifican DEC-C10-066/067/095/096 ni otras decisiones fuente.
- No se modifica C0, U_G, RMA, Evidence→Claim Matrix, STATUS ni `main`.
- No se crean claves, roster, clusters, mapas G_i, schemas, tablas, DDL, fixtures o test IDs.
- No se modifica código, focal harness, Analyzer, Evaluator o PE.
- No se ejecutan validadores, tests, workflows, simulaciones, estimaciones, calibraciones o experimentos.
- PR #116 permanece Draft.
- `scientific_execution=false`; `execution_authorized=false`.

**Siguiente operación:** Gate 120 — preparar la resolución del responsable científico de las cinco recomendaciones P0 y reconciliar las respuestas aceptadas con DEC-C10-095/096 y los contratos existentes. No registrar como decisión aceptada ninguna opción hasta recibir aprobación explícita.
