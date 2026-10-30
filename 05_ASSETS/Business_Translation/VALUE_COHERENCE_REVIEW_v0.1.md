# VALUE — Revisión de coherencia entre maestro, artefactos y Value Discovery Sprint

**Identificador:** VALUE-COHERENCE-REVIEW-001  
**Versión:** 0.1  
**Estado:** REVISIÓN DOCUMENTAL INICIAL — no equivale a validación mediante aplicación  
**Alcance:** coherencia interna de tres borradores en la rama `docs/value-methodology-lifecycle-v0-1`.

## 1. Documentos revisados

- [Documento maestro VALUE v0.2](VALUE_METHODOLOGY_LIFECYCLE_001.md)
- [Fichas maestras A1–A8 v0.1](VALUE_ARTIFACT_MASTER_SPECS_v0.1.md)
- [Value Discovery Sprint v0.1](VALUE_DISCOVERY_SPRINT_v0.1.md)

## 2. Hallazgos y resolución

### H1 — A5 podía interpretarse como una fase adicional del VCF

**Hallazgo:** el catálogo del maestro describía A5 como «Fase: VALIDACIÓN transversal», lo que podía leerse como una fase operativa añadida a ALIGN, SENSE, CONNECT, DESIGN, DECIDE, ACT y LEARN.

**Resolución aplicada:** la redacción ahora declara que A5 tiene uso transversal, especialmente en DESIGN y DECIDE, y que «validación» describe una actividad, no una fase adicional del VCF.

**Estado:** corregido en el maestro. A5 no crea una octava fase.

### H2 — Posible solapamiento entre A1 Value Intent y A2 Value Opportunity Brief

**Hallazgo:** ambos pueden mencionar la oportunidad. Sin una frontera explícita, existe riesgo de duplicar el encuadre inicial y el análisis contextual.

**Resolución aplicada:** se añadió a los criterios de A1 que este mantiene la oportunidad en un nivel inicial de encuadre; la descripción contextual, observaciones, fuentes y preguntas abiertas se desarrollan en A2.

**Estado:** aclarado en las fichas. La prueba de uso deberá comprobar si esta distinción resulta natural en la práctica.

### H3 — El Sprint puede parecer que incluye ejecución y validación completas

**Hallazgo:** el Sprint usa el recorrido VCF y entrega A1–A8, pero su duración es breve. Debe distinguirse el aprendizaje producido durante el Sprint de los resultados de una ejecución posterior.

**Control presente:** el Sprint declara que A7 debe ser proporcional a la decisión autorizada; A8 es inicial; un piloto posterior y sus resultados ocurren después; cerrar el Sprint no valida la hipótesis de valor.

**Estado:** control documental presente. Mantener esta limitación visible en la presentación del servicio.

### H4 — Evidencia y VSM evolucionan a lo largo del ciclo

**Hallazgo:** no deben tratarse como productos que se completan una sola vez y quedan congelados. A3 evoluciona durante el ciclo y A5 puede informar varios artefactos.

**Control presente:** las fichas y el maestro describen explícitamente la evolución de A3 y el uso transversal de A5.

**Estado:** coherente a nivel documental; pendiente de comprobar en un caso.

### H5 — La decisión debe preceder a la ejecución comprometida

**Hallazgo:** la recomendación, el diseño y la ejecución no deben confundirse; A7 no autoriza por sí mismo el trabajo.

**Control presente:** A6 registra la decisión y autorización; A7 referencia A6 y diferencia propuesta, autorización y ejecución. El Sprint incluye una puerta de decisión explícita.

**Estado:** coherente a nivel documental.

## 3. Comprobación de cobertura del ciclo

| Fase VCF | Artefacto principal | Tratamiento en el Sprint |
|---|---|---|
| ALIGN | A1 Value Intent | Preparación y jornada 1 |
| SENSE | A2 Value Opportunity Brief | Jornada 1 |
| CONNECT | A3 Value System Model | Jornada 2 |
| DESIGN | A4 Value Hypothesis & Options Record; A5 Evidence Record | Jornada 3 |
| DECIDE | A6 Value Decision Record; A5 como apoyo | Jornada 4 |
| ACT | A7 Value Blueprint & Delivery Plan | Jornada 5: plan proporcional a la autorización, no ejecución completa obligatoria |
| LEARN | A8 Value Learning Record | Jornada 5: aprendizaje del Sprint; actualización posterior cuando existan resultados |

Esta tabla es una comprobación de cobertura documental, no un mapeo mnemónico alternativo ni una propuesta para cambiar los nombres del VCF.

## 4. Riesgos que siguen abiertos

1. **Esfuerzo real:** no se ha probado si un Sprint de cinco jornadas permite completar artefactos suficientes para un caso de complejidad real.
2. **Usabilidad de campos:** las fichas son borradores; los campos podrían ser excesivos, ambiguos o insuficientes en la aplicación.
3. **Tamaño del VSM:** falta comprobar qué reglas prácticas ayudan a limitar el modelo sin perder relaciones decisivas.
4. **Calidad de evidencia:** los criterios son deliberadamente cualitativos; no se ha definido una escala universal ni debe inferirse una.
5. **Adaptación del Sprint:** falta especificar ejemplos de cuándo abreviar, ampliar o detener una fase sin romper las puertas de decisión.

## 5. Criterio para el siguiente paso

Antes de estabilizar las fichas o construir el playground:

1. Elegir un caso de prueba acotado y describirlo sin presuponer la solución.
2. Recorrer el Sprint y rellenar A1–A8 con datos reales o, si se simula, marcar claramente los datos ficticios.
3. Registrar tiempo, campos que no aportan, información que falta, repeticiones y decisiones que no pueden tomarse.
4. Revisar las fichas y el Sprint en función de esos resultados.
5. Mantener el estándar y la implementación separados: una limitación del prototipo no redefine automáticamente el estándar.

## 6. Conclusión

Tras las dos aclaraciones documentales, no se detecta una contradicción estructural que impida preparar una prueba controlada. Esto **no** significa que las fichas estén validadas, que el Sprint sea eficaz o que VALUE/TGCV tenga validez empírica demostrada. El siguiente hito útil es una prueba de uso integral con un caso acotado, seguida de una revisión basada en observaciones.
