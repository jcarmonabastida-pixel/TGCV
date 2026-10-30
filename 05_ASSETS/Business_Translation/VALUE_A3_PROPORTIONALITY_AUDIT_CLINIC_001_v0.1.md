# VALUE — Auditoría de proporcionalidad de A3 en CLINIC-001

**Identificador:** VALUE-A3-PROP-CLINIC-001  
**Versión:** 0.1  
**Fecha:** 2026-10-30  
**Estado:** ACEPTADA Y APLICADA — consolidación documental de A3 verificada  
**Rama:** `docs/value-methodology-lifecycle-v0-1`  
**PR:** #114  
**Alcance:** revisión de la relación entre A3 (Value System Model), el caso ficticio CLINIC-001 y los hallazgos SR-001–SR-061; evaluación de SR-062 como escenario propuesto, aún no aprobado ni registrado.

> Esta auditoría es una revisión de proporcionalidad y ubicación documental. No valida empíricamente VALUE/TGCV, no convierte las propuestas funcionales del caso en procedimientos aprobados y no autoriza cambios clínicos u operativos.

## 1. Dictamen ejecutivo

Se confirma un **riesgo material de sobredimensionamiento de A3**.

El estándar define A3 como un modelo único del sistema que representa actores, necesidades, capacidades, conocimiento, relaciones, flujos, fricciones, restricciones, alternativas, decisiones, resultados y aprendizaje. También establece que sus distintas representaciones son vistas de un mismo modelo, no artefactos independientes.

En CLINIC-001, el A3 comienza con esa función de modelado, pero la autoevaluación fue derivando hacia la especificación detallada de reglas de operación, excepciones, contingencias, controles de seguimiento, tratamiento de registros históricos y comunicación de cambios. Esos temas pueden ser relevantes para comprender el sistema, pero su desarrollo exhaustivo no es necesario para que A3 cumpla su función.

**Conclusión:** no se recomienda seguir ampliando A3 con nuevos escenarios. Se recomienda cerrar la generación de escenarios, conservar en A3 únicamente la representación sistémica de alto nivel y reclasificar el detalle operativo según su función. La presente auditoría no elimina ni reescribe hallazgos ya aprobados: propone una reorganización posterior, sujeta a decisión expresa.

## 2. Criterio de proporcionalidad

Cada hallazgo se evalúa con cuatro preguntas:

1. **Aporte al modelo:** ¿identifica un actor, necesidad, capacidad, relación, flujo, fricción, restricción, dependencia o incertidumbre relevante?
2. **Nivel adecuado:** ¿basta con representarlo en A3 o exige especificar una regla, control, procedimiento, decisión o prueba?
3. **No duplicación:** ¿añade una dimensión sustancialmente distinta o desarrolla un caso particular ya cubierto por otro principio?
4. **Destino:** ¿debe permanecer en A3, resumirse como riesgo/dependencia, trasladarse a otro artefacto/futura especificación o aparcarse?

No se considera que un escenario sea innecesario por ser detallado. La cuestión es si ese detalle corresponde a A3 y si resulta necesario para la finalidad de esta autoevaluación.

## 3. Clasificación de los hallazgos

| Hallazgos | Contenido observado | Evaluación de proporcionalidad | Tratamiento propuesto |
|---|---|---|---|
| SR-001–SR-013 | Comprensión inicial, delimitación de oportunidad, preguntas y preparación de A2. | Son antecedentes de la revisión A1/A2, no nuevos requisitos de A3. | Conservar como historial de la autoevaluación; no trasladarlos al cuerpo de A3. |
| SR-014–SR-022 | Macroetapas, actores/roles, capacidad, continuidad del flujo, información de la solicitud, ownership y supervisión end-to-end. | Núcleo pertinente de A3. Algunos detalles sobre autoridad, frecuencia, escalado y confirmaciones exceden la representación del sistema. | Conservar en A3 los elementos, relaciones, flujos, capacidades, responsabilidades funcionales y lagunas; resumir los mecanismos no definidos como incertidumbres. |
| SR-023–SR-029 | Condiciones de cierre, rechazo, ausencia de respuesta, falta o contradicción de información y ambigüedad sobre el siguiente paso. | Las condiciones y fricciones son relevantes para el modelo; las reglas completas de tratamiento son especificación operativa. Algunas decisiones —por ejemplo, aceptación tácita— requieren especial cautela y no deben presentarse como reglas reales. | Representar en A3 los estados, decisiones y bloqueos principales; mantener las reglas detalladas como propuestas pendientes de autorización, fuera del modelo principal. |
| SR-030–SR-034 | Continuidad operativa, delegación, escalado ordinario/excepcional y cobertura alternativa. | Son dependencias y riesgos relevantes, pero el desarrollo de protocolos, activaciones y niveles concretos convierte A3 en diseño operativo. | Mantener en A3 la dependencia de cobertura efectiva y continuidad; aparcar la especificación detallada para diseño/planificación posterior. |
| SR-035–SR-046 | Cobertura de funciones críticas, ausencias, priorización clínica, comunicación, reprogramación, falta de respuesta y recuperación tras contingencias. | Parte de este bloque amplía el proceso hasta la prestación asistencial y contingencias clínicas, más allá del foco administrativo de citas programadas. No debe confundirse una dependencia clínica relevante con modelar el procedimiento clínico. | Conservar solo interfaces, dependencias y límites de alcance pertinentes para A3. Aparcar reglas clínicas y protocolos de contingencia; no inventar ni normalizar decisiones clínicas en este caso. |
| SR-047–SR-051 | Detección de solicitudes sin seguimiento, revisiones periódicas, incidencias vinculadas y ciclo de vida, persistencia y reincidencia. | Identifican una capacidad de monitorización y gestión de excepciones, pero la secuencia detallada de eventos, estados y controles es diseño funcional del proceso. Hay solapamiento entre los escenarios y sus precisiones. | Resumir en A3 la necesidad de seguimiento, detección de bloqueos y gestión de incidencias. Conservar el detalle como material de diseño futuro, no como expansión del modelo. |
| SR-052 | Reproducibilidad escalonada de la autoevaluación. | No es una característica del sistema de citas ni un hallazgo propio de A3; pertenece a la gobernanza del método de evaluación. | Mantener exclusivamente en el protocolo/registro de autoevaluación. No incluir en A3. |
| SR-053 | Gestión activa de bloqueos con responsable y siguiente actuación. | Es una capacidad funcional relevante, pero se solapa parcialmente con SR-019, SR-031 y SR-047–SR-051. | Consolidar el principio en el resumen de A3; aparcar el procedimiento detallado y evitar nuevas variantes del mismo control. |
| SR-054–SR-055 | Contradicciones entre fuentes y revisión del impacto de información corregida sobre actuaciones previas. | La calidad, procedencia y consistencia de la información son dimensiones válidas del modelo. La resolución autorizada y la revisión individual de actuaciones son reglas de control/operación. | Mantener en A3 la fricción de información inconsistente y la dependencia de trazabilidad; conservar el detalle como propuesta de control para una fase posterior. |
| SR-056 | Capacidad efectiva de la cobertura operativa del proceso de citas. | Aporta precisión útil a la capacidad real, evitando confundir designación nominal con disponibilidad. No necesita convertirse en una nueva rama de escenarios. | Integrar como una única dimensión de capacidad/recursos en A3 y evitar más escenarios derivados salvo evidencia nueva. |
| SR-057 | Incidencia común del proceso con varias solicitudes afectadas y efectos residuales/secundarios. | El patrón sistémico y sus efectos son relevantes; el ciclo completo de corrección, revisión individual y verificación es especificación de gestión de incidencias. | Representar en A3 causas comunes potenciales, alcance y efectos; aparcar el procedimiento detallado y mantener los efectos no previstos como riesgo general. |
| SR-058–SR-060 | Cambios de reglas con solicitudes en curso; incertidumbre sobre versión aplicada en solicitudes abiertas o cerradas. | La gobernanza de reglas y la trazabilidad temporal son restricciones sistémicas importantes. Los tratamientos diferenciados de cada caso son casuística operativa que no debe seguir multiplicando A3. | Conservar en A3 la existencia de reglas versionadas, transiciones autorizadas y trazabilidad como dependencias; consolidar las respuestas detalladas fuera del modelo principal. |
| SR-061 | Comunicación y aplicación efectiva de correcciones documentales en el sistema. | La actualización del conocimiento operativo y su adopción en el punto de uso son dimensiones relevantes. El análisis de destinatarios, notificación, recepción, lectura y actuaciones previas es diseño de control. | Mantener el principio de vigencia, acceso y adopción verificable como dimensión resumida; conservar el detalle en material operativo subordinado. |

## 4. Revisión específica de SR-062

**Escenario propuesto:** se envía una notificación sobre una corrección documental, pero no existe confirmación de lectura ni evidencia directa de que las personas destinatarias hayan empezado a utilizar la versión actualizada.

**Dictamen:** no justifica un SR independiente.

La distinción propuesta —el envío no demuestra lectura ni aplicación; la falta de confirmación tampoco demuestra que nadie haya leído— está sustancialmente cubierta por SR-061, que ya exige verificar la comunicación y aplicación mediante las evidencias que realmente ofrezca el sistema y prohíbe presumir funciones de confirmación o analítica.

**Tratamiento recomendado:** no crear SR-062. Si se considera útil conservar la precisión, integrarla en SR-061 como aclaración breve, sin añadir un nuevo escenario ni ampliar el protocolo de notificación. La precisión debe dejar claro que la ausencia de confirmación es una limitación de evidencia, no una prueba de falta de lectura o de falta de aplicación.

Estado: **propuesto; no aprobado ni incorporado**.

## 5. Qué debería contener A3 tras la simplificación

A3 debería permitir comprender el sistema sin convertirse en manual de procedimientos. Para CLINIC-001, su cuerpo principal debería limitarse a:

1. **Propósito y límites del sistema:** gestión de citas programadas; urgencias y decisiones clínicas fuera del alcance del modelo administrativo.
2. **Actores y funciones:** paciente/cuidador, recepción, administración de citas, coordinación, profesionales sanitarios cuando corresponda, sistema de registro y dirección de operaciones.
3. **Flujo principal:** recepción y registro → revisión/clasificación → asignación o derivación → comunicación y seguimiento → confirmación/resolución.
4. **Capacidades y recursos:** disponibilidad y adecuación de roles, capacidad operativa, información y herramientas.
5. **Relaciones y responsabilidades:** traspasos entre funciones, coordinación y responsabilidad end-to-end, sin inventar autoridades nominales.
6. **Fricciones y restricciones:** información incompleta/contradictoria, bloqueos, falta de capacidad, demoras, reglas no identificadas, trazabilidad y dependencias clínicas.
7. **Conocimiento e incertidumbre:** hechos del escenario ficticio, hipótesis, supuestos y datos que habría que verificar.
8. **Puntos de intervención:** aspectos que A4 puede convertir en hipótesis y alternativas contrastables.

Los escenarios de contingencia se utilizarían para comprobar que el modelo no omite una dimensión sistémica importante; no para incorporar en A3 el procedimiento completo de respuesta a cada contingencia.

## 6. Qué no debería seguir ocurriendo

- No crear un SR por cada variante de una contingencia ya representada.
- No convertir cada precisión aprobada en una nueva obligación independiente.
- No especificar en A3 plazos, umbrales, responsables nominales, permisos, canales o protocolos no aportados por el caso.
- No confundir propuesta funcional ficticia con procedimiento aprobado.
- No expandir el alcance administrativo hacia decisiones clínicas.
- No utilizar el número de escenarios o la longitud del documento como indicador de calidad o validación de VALUE.

## 7. Secuencia de cierre recomendada

1. **Cerrar la generación de nuevos escenarios A3**, dejando SR-062 sin aprobar y sin registrar como nuevo hallazgo.
2. **Confirmar la clasificación** de los bloques de SR de esta auditoría.
3. **Consolidar el cuerpo A3** en el caso ficticio, conservando la trazabilidad de los hallazgos originales y sin borrar el historial.
4. **Separar el material operativo detallado** en un anexo o registro de propuestas pendientes, solo si se considera útil para una fase posterior; no es necesario convertirlo ahora en un procedimiento completo.
5. **Revisar el log** para distinguir hallazgos del modelo, precisiones, propuestas operativas y decisiones de gobernanza de la autoevaluación.
6. **Actualizar el protocolo y la revisión global únicamente después** de aprobar esta consolidación y comprobar coherencia entre caso, log y estándar.
7. Congelar la versión documental resultante y continuar con la evaluación de los artefactos siguientes, sin interpretar el cierre de A3 como validación empírica.

## 8. Límites de esta auditoría

- La clasificación se basa en los documentos actuales de la rama de trabajo del PR #114.
- Se modificaron el caso ficticio y el registro de autoevaluación para aplicar la consolidación aceptada.
- No se eliminaron los hallazgos históricos del registro ni se revocaron decisiones aprobadas.
- No se modificaron el protocolo de usabilidad ni el estándar metodológico.
- El caso sigue siendo ficticio; esta auditoría no demuestra usabilidad independiente, validez, causalidad ni eficacia de VALUE/TGCV.

**Decisión del usuario:** aceptó la clasificación como base para consolidar A3. La consolidación se aplicó al caso ficticio y al registro de autoevaluación, y se verificó mediante relectura en la rama del PR #114.
