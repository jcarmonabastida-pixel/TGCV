# C10-S — Comparación de mecanismos para estipular Need_preZ y recomendación de composición

**ID:** C10-S-B1-PREZ-STIPULATION-MECHANISM-COMPARISON-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** HISTORICAL_RECONCILIATION / DESIGN_COMPARISON / RECOMMENDATION_ACCEPTED_BY_USER / DEC-C10-095_ACCEPTED_WORKING_DESIGN / NOT_IMPLEMENTED / NOT_MATERIALIZED / NOT_EXECUTED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)

## 1. Pregunta y conclusión ejecutiva

Se comparan tres formas de producir la estipulación basal explícita de `Need_preZ` por unidad B1/UE:

1. configuración explícita por unidad;
2. regla determinista;
3. mecanismo estocástico.

**Recomendación:** utilizar configuración explícita, versionada y reservada por unidad como fuente de la estipulación; aplicar una regla determinista y trivial únicamente para traducir esa estipulación a `need_truth_state`. No usar una distribución estocástica para asignar Need en el diseño confirmatorio actual.

Esto no fija roster, número de unidades, prevalencia, proporciones, asignación por brazo, estratos, escenarios concretos, semillas ni parámetros. Tampoco autoriza materialización.

## 2. Reconstrucción histórica: qué ya está resuelto

Los contratos revisados ya establecen:

- La unidad semántica es B1/UE vinculada a una instancia lógica de servicio versionada.
- La truth deriva de una estipulación explícita en t−1: inclusión focal → 1; exclusión focal explícita dentro del alcance cerrado → 0; indeterminación semántica explícita → ?.
- Omisión, null, ausencia de registro, fallo de escritura o binding inválido son defectos de integridad/materialización, no estados truth.
- No existe un atributo basal aprobado que pueda sustituir la estipulación. `X_i`, `H_{i0}`, `C_{c,i0}`, `L_{m,i0}`, `C_{dep}`, `A_f`, `T_acc`, Reach, configuración CMP/PAR/REF/RUL y ENABLED/PROFILE no son generadores automáticos de Need.
- Se requiere soporte truth=1 y truth=0 en la cohorte de validación definida ex ante. No se exige balance ni soporte por brazo/estrato sin justificación adicional.
- La cohorte no se selecciona por Need, Z, observabilidad, adjudicación ni resultados; no se confunde con P* ni con denominadores ITT.
- Truth se fija en t−1, antes de Z; la observación se genera por separado y el Analyzer/E1/E2 no reciben truth.

Fuentes históricas principales:
- `C10_S_B1_PREZ_OBJECTIVE_SPECIFICATION_CONTRACT_DRAFT_001.md` §§4–8.
- `C10_S_B1_PREZ_TRUTH_COMPOSITION_AND_SUPPORT_REVIEW_DRAFT_001.md` §§2–8.
- `C10_S_B1_PREZ_VALIDATION_COHORT_POPULATION_CROSSWALK_DRAFT_001.md` §§3–7.
- `C10_S_B1_PREZ_BASELINE_SOURCE_DIAGNOSTIC_DRAFT_001.md` §§4–8.
- `C10_S_B1_PREZ_ANALYTICAL_PACKAGE_CONTRACT_DRAFT_001.md` §§3–9.

El gate pendiente no es inventar una variable explicativa de Need, sino decidir cómo se representa y gobierna la estipulación por unidad.

## 3. Comparación de alternativas

| Criterio | Configuración explícita por unidad | Regla determinista generadora | Mecanismo estocástico |
|---|---|---|---|
| Fundamento semántico | Directo: declara inclusión/exclusión/indeterminación del objetivo | Depende de predictores o etiquetas de escenario adicionales | Depende de una distribución de Need |
| Variables nuevas necesarias | Ninguna variable causal; solo el contenido estipulado ya requerido | Requiere entradas/reglas adicionales; si no existen, la regla codifica la configuración de forma indirecta | Requiere probabilidad, distribución, generador y semilla |
| Auditabilidad | Alta: cada estipulación puede inspeccionarse y versionarse | Media/alta si las entradas tienen semántica aprobada; baja si son etiquetas ad hoc | Reproducible con semillas, pero la razón semántica de cada valor puede quedar opaca |
| Control de circularidad | Alto si se mantiene aislada de Z y post-Z | Depende de todas las entradas; riesgo de usar proxies no autorizados | Alto frente a Z solo si se impone explícitamente; no resuelve el fundamento semántico |
| Riesgo de prevalencia arbitraria | Persiste al diseñar el roster; queda visible como decisión de composición, no escondida en una distribución | Puede ocultarse en reglas o frecuencias de etiquetas | Alto: la prevalencia queda incorporada en parámetros probabilísticos |
| Soporte 1/0 | Se comprueba sobre la cohorte completa; la falta de soporte bloquea | Puede producir ambos si la regla lo garantiza, pero esa garantía necesita justificar sus entradas | Probabilístico; no garantiza soporte en una realización finita |
| Reproducibilidad | Alta con configuración versionada y digest | Alta si regla/inputs están versionados | Alta con algoritmo, parámetros y semillas |
| Adecuación actual | **Alta** | No demostrada; no hay predictor basal autorizado | Prematura; no hay prevalencia ni distribución justificadas |

## 4. Evaluación de cada alternativa

### 4.1 Configuración explícita por unidad — recomendada

El diseño autoriza una estipulación semántica explícita por unidad B1/UE en el ámbito reservado. Esa estipulación es el objeto generador, no una covariable explicativa. Una regla versionada traduce únicamente su contenido semántico a 1/0/?.

Ventajas:
- respeta el contrato de objetivo focal ya definido;
- no inventa atributos basales ni introduce una ontología paralela;
- permite auditar inclusión, exclusión y alcance de cada unidad;
- mantiene separadas verdad, evidencia observada y adjudicación;
- permite bloquear el diseño si el roster no contiene ambos estados, sin reetiquetar ni añadir casos a posteriori.

Límite: no elimina la decisión de composición del roster. La selección de escenarios y la presencia de ambos estados deben justificarse como cobertura del dominio de validación, no presentarse como prevalencia natural ni estimación de la prevalencia poblacional.

### 4.2 Regla determinista — no recomendada como generador primario

Una regla del tipo `Need = f(X,H,C,L,...)` está expresamente descartada por falta de mapping semántico aprobado y por riesgo de circularidad.

Una regla basada en una etiqueta de escenario o un código de configuración tampoco resuelve el problema: si esa etiqueta se asigna manualmente, la fuente real sigue siendo una estipulación explícita, solo que codificada indirectamente. Si la etiqueta se deriva de otras variables, se necesitaría una justificación semántica y causal inexistente hoy.

Se conserva únicamente una transformación determinista y transparente de la estipulación a `need_truth_state`. Esa transformación no debe confundirse con un mecanismo que decide qué objetivo tiene cada B1.

### 4.3 Mecanismo estocástico — no recomendado en esta fase

Un generador Bernoulli/categórico exigiría prevalencias o probabilidades para 1/0/? y semillas. Ninguno de esos parámetros está justificado por la teoría, la población o un modelo empírico aprobado.

Además:
- una realización finita podría no contener una de las clases;
- una semilla fija no aporta fundamento semántico;
- fijar probabilidades solo para obtener soporte confundiría la necesidad de evaluar dos clases con una afirmación sobre su frecuencia;
- añadir aleatoriedad no mejora la validez de la estipulación.

Un mecanismo estocástico podría reconsiderarse para una pregunta distinta —por ejemplo, estudiar sensibilidad a diferentes composiciones de población— si se define una distribución objetivo y se justifica. No debe introducirse en el núcleo confirmatorio actual por conveniencia.

## 5. Cómo exigir soporte sin inventar prevalencia

La solución no es equilibrar clases ni imponer una proporción. Es separar tres decisiones:

1. **Marco de unidades:** aprobar el roster B1/UE y la cohorte de validación con reglas de pertenencia independientes de Need, Z, observabilidad y resultados.
2. **Cobertura semántica del diseño:** asegurar que el dominio de validación contiene ejemplos legítimos de inclusión y exclusión focal, sin etiquetar la composición como prevalencia poblacional. La justificación debe ser de cobertura del constructo y de la tarea de clasificación.
3. **Gate de soporte:** una vez fijados roster y estipulaciones, comprobar si existen unidades válidas truth=1 y truth=0. Si falta una clase, declarar `SUPPORT_FAILURE / DESIGN_BLOCKED`; no corregirlo mediante generación post hoc, reponderación, reetiquetado o alteración del roster tras observar resultados.

Este requisito no impone que cada brazo Z o estrato contenga ambas clases. Tampoco acredita positividad, soporte de q_X*, potencia ni identificación causal.

Las métricas de clasificación deben ser principalmente condicionales a clase (p. ej., sensibilidad y especificidad) y acompañarse de denominadores y cobertura. Métricas dependientes de prevalencia (p. ej., valor predictivo positivo/negativo y exactitud global) no deben interpretarse como rendimiento poblacional si la composición del roster fue diseñada para cobertura de clases y no representa una prevalencia objetivo. No se fija aquí un plan estadístico completo.

## 6. Regla operativa propuesta

Si la recomendación se acepta, el contrato de composición deberá adoptar estas reglas:

1. La estipulación explícita por B1/UE es el único input semántico autorizado para derivar Need_truth.
2. La estipulación se crea y versiona en t−1 dentro del ámbito reservado; el `TRUTH_LEDGER` conserva su referencia conforme al contrato existente.
3. La derivación 1/0/? es determinista, sin muestreo ni consulta de covariables, Z o variables post-Z.
4. El roster/cohorte se define antes de inspeccionar Need, evidencia o resultados; se incluye el marco completo que cumpla la regla de identidad/binding aprobada.
5. El soporte 1/0 se evalúa como gate después de cerrar el roster y las estipulaciones, nunca como regla de selección o reparación automática.
6. La cohorte mantiene truth=? y defectos de integridad en flujos distintos; no se imputan ni se eliminan silenciosamente.
7. La verdad y sus metadatos reconstructivos permanecen cegados a E1/E2 y Analyzer; la evidencia observable se genera por el mecanismo separado ya especificado.
8. Cualquier diseño de escenarios para asegurar cobertura semántica debe documentar por qué cada tipo de estipulación pertenece al dominio de validación, sin atribuirle frecuencia natural.

## 7. Qué no queda decidido por esta recomendación

Incluso aceptando configuración explícita, siguen abiertos:
- roster, población y cohorte exactos;
- definición del dominio de escenarios B1 y justificación de su cobertura;
- número de unidades y suficiencia estadística/potencia;
- si truth=? forma parte del objetivo confirmatorio o solo de diagnósticos;
- dependencias estadísticas de Need con covariables basales, si se plantean;
- modelo de observación y parámetros de error/cobertura;
- esquema físico, permisos, almacenamiento, sellado y firewall técnico;
- mapping final con pruebas existentes sin duplicarlas.

No se asignan valores, proporciones, prevalencias, unidades, IDs, parámetros ni semillas.

## 8. Recomendación sometida a aceptación

**RECOMMENDATION:** configuración explícita, versionada y reservada por B1/UE como fuente de estipulación; derivación determinista de truth desde esa estipulación; ningún generador estocástico de Need en el núcleo confirmatorio actual; soporte 1/0 comprobado como gate sobre la cohorte definida ex ante, con bloqueo si falta una clase.

La recomendación fue aceptada expresamente por el usuario y registrada en DEC-C10-095. La aceptación no autoriza materialización, construcción del roster, implementación ni ejecución.

## 9. Estado de decisión y ejecución

La alternativa recomendada ha sido aceptada y propagada a los contratos B1 rectores mediante DEC-C10-095. Las alternativas determinista-generadora y estocástica quedan descartadas para la asignación de Need en el núcleo confirmatorio; el mapping determinista desde la estipulación sí queda adoptado.



Este documento es una comparación y recomendación. No modifica el contrato de objetivo, el paquete analítico, el mapa temporal maestro, población/estimandos, RMA, Evidence→Claim Matrix, STATUS, decisiones aceptadas ni main. No crea roster, estipulaciones, truth, fuentes, fixtures, parámetros, schema físico o código.

`scientific_execution=false`; `execution_authorized=false`.
