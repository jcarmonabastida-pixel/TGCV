# VALUE — Revisión de coherencia A3 → A4 → A5 en CLINIC-001

**Identificador:** VALUE-CHAIN-COHERENCE-CLINIC-001  
**Versión:** 0.1  
**Fecha:** 2026-10-30  
**Estado:** REVISIÓN DOCUMENTAL REALIZADA — ajustes incorporados; brechas de evidencia explícitas  
**Rama:** `docs/value-methodology-lifecycle-v0-1`  
**PR:** #114

## 1. Objetivo y límites

Comprobar que A3 representa el sistema a un nivel proporcional, que A4 deriva de ese modelo las hipótesis y opciones de diseño y que A5 permite identificar qué evidencia informa cada hipótesis/opción.

La revisión es documental y se refiere a un caso completamente ficticio. No valida empíricamente VALUE/TGCV, no demuestra eficacia de ninguna alternativa ni autoriza una intervención real.

## 2. Criterio aplicado

- A3: elementos y relaciones relevantes, IDs estables, estado epistemológico, incertidumbres y límites; no un procedimiento operativo exhaustivo.
- A4: necesidad abordada, cambio y mecanismo esperado, personas/capacidades afectadas, supuestos, evidencia favorable/contradictoria, prueba posible y criterios de revisión.
- A5: trazabilidad entre afirmación y evidencia, fuente/método, contexto, calidad, sesgos, contradicciones y límites; no presentar datos simulados como observaciones.

## 3. Hallazgos antes del ajuste

1. **A3 demasiado narrativo para su especificación maestra:** describía actores y flujo, pero no proporcionaba IDs estables ni un registro explícito de relaciones con significado y estado epistemológico.
2. **Trazabilidad A3→A4 poco explícita:** O0–O4 estaban descritas, pero no indicaban qué elementos, relaciones o fricciones del modelo justificaban cada alternativa.
3. **Cadena de razonamiento A4 incompleta:** H-V1 describía el cambio y resultado esperado, pero no reunía en un mismo lugar todos los supuestos críticos, las personas/funciones afectadas, la evidencia contradictoria, el mecanismo y la prueba posible.
4. **Cobertura A4→A5 parcial:** el indicador de solicitudes fuera del plazo de referencia es relacionado con demora, pero no mide directamente la ejecución de la revisión diaria ni solicitudes bloqueadas sin siguiente actuación. La carga no tiene medida comparable.
5. **Evidencia de O2 no equivale a evidencia de O1:** la devolución por información incompleta informa principalmente la opción O2; no debe usarse como prueba de H-V1/O1.
6. **O3 y O4 no tienen evidencia específica:** no hay datos de capacidad o prueba de rediseño integral.

## 4. Ajustes incorporados

### A3
- Se añadieron IDs E01–E07 para actores/elementos y R01–R07 para relaciones propuestas.
- Se documentó el significado de cada relación y su estado epistemológico (propuesto, inferido, supuesto o dependencia pendiente).
- Se dejó explícito que los elementos y relaciones son un modelo conceptual del caso ficticio, no un mapa organizativo ni un flujo real verificado.
- No se añadieron protocolos, responsables nominales, plazos ni funciones técnicas presumidas.

### A4
- Se añadió correspondencia de cada opción O0–O4 con los IDs de A3, la fricción/capacidad que aborda y su mecanismo esperado.
- Se completó la cadena de razonamiento de H-V1: necesidad, cambio propuesto, mecanismo, personas/funciones afectadas, supuestos, evidencia favorable/contradictoria, prueba posible y criterio de revisión.
- Se mantiene explícito que los umbrales y criterios cuantitativos de decisión siguen pendientes y no se inventan.

### A5
- Se añadió una matriz de cobertura que distingue evidencia relacionada, conclusión admisible y brecha para H-V1/O1, protección de prioridad, carga, O2, O3 y O4.
- Se identifica que los datos son simulados y no permiten afirmar fidelidad de implementación, causalidad, seguridad ni eficacia.
- No se añadieron cifras ni se modificaron resultados ficticios para aparentar cobertura.

## 5. Dictamen

**La cadena documental es ahora más explícita y coherente en su estructura, pero la evidencia sigue siendo insuficiente para contrastar empíricamente H-V1.**

- A3 ofrece un modelo de alto nivel con elementos y relaciones identificables.
- A4 enlaza las alternativas con ese modelo y hace visible el razonamiento de la hipótesis principal.
- A5 diferencia qué indicadores simulados son pertinentes y cuáles son insuficientes o no aplicables a cada opción.
- El principal vacío de A5 para H-V1 es la ausencia de evidencia sobre fidelidad del mecanismo (revisiones realizadas, pendientes con responsable/siguiente actuación y excepciones escaladas) y una medida comparable de carga.
- Los datos ficticios solo ilustran cómo registrar y clasificar evidencia; no permiten validar la hipótesis ni seleccionar empíricamente O1.

No se recomienda generar más escenarios A3 para resolver estas brechas. Son cuestiones de especificación de evidencia y prueba de A4/A5, no motivos para volver a ampliar el modelo sistémico.

## 6. Siguiente paso metodológico

Mantener los límites y los datos actuales. Antes de cualquier prueba real, definir con las personas autorizadas los indicadores de fidelidad, demora, protección de prioridad y carga, sus fuentes, denominadores, ventanas y criterios de decisión. Si esos datos no están disponibles, registrar la limitación y no afirmar que H-V1 ha sido contrastada.

La revisión de usabilidad de VALUE y la repetición intraevaluador previstas en SR-052 son actividades distintas y continúan pendientes.

## 7. Referencias y cambios

- Caso actualizado a versión 1.0: `VALUE_FICTIONAL_CASE_CLINIC_001_v0.1.md`.
- Registro de autoevaluación: `VALUE_SELF_REVIEW_LOG_CLINIC_001_v0.1.md`.
- Especificación maestra: `VALUE_ARTIFACT_MASTER_SPECS_v0.1.md`.
- Auditoría de proporcionalidad A3: `VALUE_A3_PROPORTIONALITY_AUDIT_CLINIC_001_v0.1.md`.

**Límite final:** el cierre de esta revisión acredita coherencia documental mejorada, no validez empírica, causalidad ni eficacia de VALUE/TGCV.
