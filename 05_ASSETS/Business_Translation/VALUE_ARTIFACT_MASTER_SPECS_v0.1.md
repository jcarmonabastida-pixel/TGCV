# VALUE — Fichas maestras de artefactos canónicos

**Identificador:** VALUE-ARTIFACT-SPECS-001  
**Versión:** 0.1  
**Estado:** BORRADOR DE TRABAJO — pendiente de revisión  
**Documento rector:** [VALUE Methodology Lifecycle v0.2](VALUE_METHODOLOGY_LIFECYCLE_001.md)  
**Alcance:** especificación operativa inicial de A1–A8; no constituye validación empírica de VALUE ni de TGCV.

## 1. Propósito y reglas

Este documento convierte el catálogo del maestro en fichas utilizables y revisables. No crea artefactos adicionales ni cambia las definiciones canónicas. Las plantillas, formularios, mapas y vistas son interfaces para producir o consultar estos registros, no fuentes paralelas de verdad.

Reglas comunes:

1. Cada instancia tiene un ID estable, versión, estado, responsable, fecha de creación/actualización y procedencia.
2. Cada instancia enlaza los IDs de artefactos relacionados; los enlaces no se sustituyen por copias de su contenido.
3. Se distinguen explícitamente observación, fuente, inferencia, hipótesis, supuesto, decisión y resultado observado.
4. Los campos no aplicables se marcan como tales; los datos ausentes no se interpretan como evidencia favorable.
5. Se preserva el historial de cambios relevantes. Las decisiones no se sobrescriben silenciosamente.
6. Un registro puede tener estado «borrador», «en revisión», «aceptado», «bloqueado» o «retirado». «Aceptado» significa aceptado para el caso, no validado universalmente.
7. La evidencia se puede añadir durante todo el ciclo; A5 no es una fase exclusiva.
8. La IA puede asistir en la elaboración, pero toda afirmación material debe conservar procedencia y revisión humana.

## 2. Campos comunes mínimos

- **ID del registro**
- **Versión**
- **Estado**
- **Caso / iniciativa**
- **Responsable**
- **Fecha de creación y última actualización**
- **Autoría y contribuciones**
- **Fuentes / procedencia**
- **Artefactos relacionados**
- **Cambios relevantes y motivo**
- **Cuestiones abiertas / limitaciones**

Los campos específicos siguientes se añaden a los comunes. Las fichas no prescriben todavía un formato de software ni un esquema JSON definitivo.

## 3. A1 — Value Intent

**Fase principal:** ALIGN  
**Propósito:** acordar qué se intenta conseguir, para quién, con qué criterios y bajo qué límites, antes de comprometerse con una solución.

### Campos específicos
- Contexto y patrocinador.
- Propósito y reto que motiva el trabajo.
- Personas/grupos afectados y partes interesadas relevantes.
- Resultados deseados y criterios de valor.
- Restricciones, límites de alcance y condiciones no negociables.
- Decisión que se pretende apoyar y autoridad responsable.
- Horizonte temporal y urgencia, si son pertinentes.
- Indicadores o señales que se observarán, sin imponer métricas universales.
- Desacuerdos, incertidumbres y supuestos iniciales.
- Condiciones para revisar la intención.

### Criterios de calidad
- El reto no presupone una solución concreta sin justificación.
- A1 mantiene la oportunidad en un nivel inicial de encuadre; la descripción contextual, las observaciones, las fuentes y las preguntas abiertas se desarrollan en A2, evitando duplicar el brief.
- Se identifica quién define el valor y quién puede verse afectado.
- Los criterios son suficientemente claros para orientar comparación posterior.
- Las restricciones y desacuerdos importantes son visibles.

### Salida / transición
Intención de valor revisable y criterios explícitos para orientar SENSE. Si no existe acuerdo mínimo sobre el propósito o la autoridad de decisión, se registra el bloqueo en lugar de fingir alineación.

## 4. A2 — Value Opportunity Brief

**Fase principal:** SENSE  
**Propósito:** describir una oportunidad en su contexto, separando lo observado de la interpretación y de la solución imaginada.

### Campos específicos
- Situación actual y contexto.
- Necesidad, problema o posibilidad investigada.
- Personas afectadas y trabajos/situaciones relevantes.
- Señales y observaciones disponibles, con fuentes.
- Consecuencias actuales y posibles consecuencias de no actuar.
- Alcance y límites de la oportunidad.
- Preguntas abiertas y lagunas de conocimiento.
- Hipótesis o supuestos iniciales, claramente etiquetados.
- Alternativas ya intentadas y aprendizaje conocido.
- Vínculo con A1 y con las vistas pertinentes del VSM.

### Criterios de calidad
- Distingue hechos observados, testimonios, inferencias y supuestos.
- Explicita a quién afecta y en qué contexto.
- No presenta impacto potencial como valor realizado.
- Las preguntas abiertas pueden guiar investigación adicional.

### Salida / transición
Oportunidad delimitada y conjunto visible de preguntas que CONNECT debe investigar. El brief puede revisarse si aparece evidencia nueva.

## 5. A3 — Value System Model (VSM)

**Fase principal:** CONNECT; evoluciona durante todo el ciclo.  
**Propósito:** representar el sistema de valor relevante para la oportunidad y las relaciones entre sus elementos.

### Componentes que pueden aplicar
- Actores y grupos afectados.
- Necesidades, objetivos, tensiones y criterios de valor.
- Capacidades, recursos y restricciones.
- Conocimiento, fuentes y evidencias.
- Relaciones de coordinación, intercambio y aprendizaje.
- Flujos de información, decisiones, recursos y trabajo.
- Fricciones, dependencias, retrasos y bloqueos.
- Hipótesis, opciones y cambios posibles.
- Decisiones, acciones, resultados y aprendizaje.

### Campos específicos
- Alcance y perspectiva del modelo.
- Leyenda, tipos de elemento y tipos de relación utilizados.
- Elementos y relaciones con IDs estables.
- Estado epistemológico de afirmaciones relevantes: observado, informado, inferido, supuesto o pendiente.
- Fuentes y responsable de validar cada elemento material.
- Vistas activas (red, capacidades, inteligencia colectiva, flujos u otras).
- Límites, conflictos entre fuentes y zonas no modeladas.
- Historial de cambios y razón de cada cambio material.

### Criterios de calidad
- El modelo responde a la oportunidad y no intenta representar indiscriminadamente toda la organización.
- Las relaciones tienen significado explícito; no son meras líneas decorativas.
- Las vistas reutilizan los mismos elementos subyacentes.
- Las incertidumbres y discrepancias no se ocultan.
- Se diferencia la situación actual de una situación deseada o propuesta.

### Salida / transición
Modelo contextual compartido, suficientemente útil para generar alternativas. «Suficiente» se determina por las preguntas de decisión del caso, no por completitud visual.

## 6. A4 — Value Hypothesis & Options Record

**Fase principal:** DESIGN  
**Propósito:** documentar alternativas comparables y las hipótesis bajo las cuales podrían generar valor.

### Campos específicos
- ID y descripción de cada alternativa.
- Necesidad/oportunidad que aborda.
- Cambio propuesto y mecanismo esperado.
- Personas afectadas y capacidades requeridas.
- Hipótesis de valor y cadena de razonamiento.
- Supuestos críticos y condiciones de validez.
- Evidencia a favor, evidencia contradictoria y lagunas.
- Riesgos, dependencias, efectos secundarios y reversibilidad.
- Costes/esfuerzos relevantes según el caso.
- Pruebas o experimentos posibles y resultados que apoyarían/refutarían la hipótesis.
- Criterios de descarte o revisión.
- Referencias a A2, A3 y A5.

### Criterios de calidad
- Las alternativas se describen con un nivel de detalle comparable.
- Las hipótesis pueden ponerse en cuestión; no son promesas.
- Los supuestos críticos y riesgos están visibles.
- Se consideran alternativas de no actuar o de realizar una prueba cuando proceda.

### Salida / transición
Opciones comparables y contrastables para DECIDE. No se declara ganadora una alternativa por el mero hecho de ser la más novedosa o tecnológicamente avanzada.

## 7. A5 — Evidence Record

**Uso:** transversal, con especial relevancia para DESIGN y DECIDE.  
**Propósito:** conservar trazabilidad de las afirmaciones y del grado de apoyo que reciben.

### Campos específicos por entrada de evidencia
- ID de evidencia.
- Afirmación/hipótesis a la que se refiere.
- Tipo: observación, testimonio, dato, documento, experimento, estimación u otro.
- Fuente, autoría, fecha y método de obtención.
- Contexto y condiciones de recogida.
- Resultado o extracto pertinente, respetando derechos y privacidad.
- Calidad, relevancia y limitaciones conocidas.
- Posibles sesgos, contradicciones y explicaciones alternativas.
- Estado de verificación y persona revisora.
- Decisiones o alternativas que esta evidencia informa.

### Criterios de calidad
- Puede reconstruirse de dónde procede una afirmación material.
- La evidencia contradictoria no se elimina para simplificar la narrativa.
- Se diferencia evidencia directa de inferencia o salida de IA no verificada.
- La ausencia de evidencia se registra como incertidumbre, no como confirmación.

### Salida / transición
Base trazable para comparar hipótesis y fundamentar decisiones. No existe una puntuación universal de calidad prescrita en esta versión.

## 8. A6 — Value Decision Record

**Fase principal:** DECIDE  
**Propósito:** dejar constancia de una decisión responsable, sus fundamentos y sus condiciones de revisión.

### Campos específicos
- Decisión requerida y autoridad responsable.
- Alternativas consideradas, incluida la opción de aplazar o no actuar.
- Criterios de A1 aplicados.
- Evidencia relevante y referencias a A5.
- Trade-offs, riesgos, incertidumbres y desacuerdos.
- Decisión adoptada y razones.
- Condiciones, límites y supuestos aceptados.
- Responsable y autorización para el siguiente paso.
- Requisitos de prueba, mitigación o seguimiento.
- Fecha o evento de revisión y condiciones para reabrir la decisión.

### Criterios de calidad
- Se identifica quién decide y con qué mandato.
- Las razones pueden reconstruirse desde los criterios y la evidencia.
- Las incertidumbres materiales no se presentan como resueltas.
- La autorización de ejecución tiene alcance explícito.

### Salida / transición
Decisión trazable: ejecutar, probar, investigar más, aplazar, cambiar de alternativa o detener. A7 no debe convertir una recomendación en compromiso de ejecución sin la autorización pertinente.

## 9. A7 — Value Blueprint & Delivery Plan

**Fases:** diseño de la solución y planificación en DESIGN; plan autorizado y ejecución en ACT. Se conserva un artefacto, con estados diferenciados.  
**Propósito:** traducir una alternativa autorizada a un diseño y a un plan realizable, sin confundir propuesta con ejecución completada.

### Campos específicos
- Decisión de A6 que autoriza el trabajo.
- Blueprint: componentes, cambios, capacidades y mecanismo previsto.
- Alcance incluido y excluido.
- Plan por entregables/hitos, dependencias y secuencia.
- Responsables, recursos y autoridad de escalado.
- Adopción, operación, formación y gestión del cambio.
- Riesgos, mitigaciones y contingencias.
- Medidas/observaciones previstas y fuente de datos.
- Estado de cada acción: propuesta, autorizada, en curso, bloqueada, completada o cancelada.
- Evidencia de aceptación y desviaciones respecto del plan.
- Criterios para detener, adaptar o revertir.

### Criterios de calidad
- Cada acción tiene responsable y resultado esperado.
- Se distinguen diseño, autorización, ejecución y aceptación.
- Los riesgos y dependencias tienen tratamiento visible.
- Los indicadores son apropiados al caso y no se confunden con validación causal automática.

### Salida / transición
Blueprint y plan autorizados; durante ACT, registro actualizado del trabajo realizado y de sus desviaciones. La finalización de tareas no equivale por sí sola a valor demostrado.

## 10. A8 — Value Learning Record

**Fase principal:** LEARN  
**Propósito:** comparar lo ocurrido con la intención y los criterios acordados, y decidir qué debe mantenerse o cambiarse.

### Campos específicos
- Referencias a A1, A6 y A7.
- Resultados observados y periodo de observación.
- Criterios previstos frente a resultados disponibles.
- Efectos previstos y no previstos, positivos o negativos.
- Calidad y limitaciones de los datos.
- Explicaciones alternativas y límites de atribución.
- Diferencias entre lo planificado y lo ejecutado.
- Aprendizajes, capacidades desarrolladas y cuestiones no resueltas.
- Decisión posterior: mantener, adaptar, ampliar, revertir, investigar o reiniciar.
- Cambios recomendados a A1, A2, A3 u otros artefactos.
- Responsable y fecha de seguimiento.

### Criterios de calidad
- Distingue resultado observado de interpretación causal.
- Incluye resultados adversos y efectos no previstos.
- Relaciona el aprendizaje con criterios iniciales sin forzar una conclusión favorable.
- Cada aprendizaje importante puede informar una decisión o cambio posterior.

### Salida / transición
Registro reutilizable y decisión explícita sobre el siguiente ciclo. Si no existen datos suficientes, se documenta la limitación y se define si merece la pena seguir observando.

## 11. Mapa mínimo de trazabilidad

La secuencia de referencia es:

**A1 → A2 → A3 → A4 ↔ A5 → A6 → A7 → A8**

- A5 puede alimentar y actualizar cualquier artefacto cuando aporta evidencia pertinente.
- A3 evoluciona durante todo el ciclo.
- A7 se inicia como diseño y se convierte en plan autorizado/registro de ejecución, manteniendo historial.
- A8 puede abrir una nueva iteración sobre A1, A2, A3 o una decisión previa.
- Los enlaces reflejan procedencia y dependencia; no implican causalidad.

## 12. Revisión y aceptación de una ficha

Una ficha se considera lista para pilotaje cuando:
1. Su propósito no se solapa de forma material con otro artefacto.
2. Los campos mínimos permiten producir su salida.
3. Sus criterios de calidad pueden ser revisados por un facilitador.
4. Los vínculos con artefactos previos y posteriores están definidos.
5. Se incluye un ejemplo completo y se han anotado límites conocidos.
6. La prueba de uso no requiere inventar campos esenciales durante la sesión.

Este documento es un borrador de especificación. Las fichas deben probarse con un caso antes de declararlas estables o convertirlas en un esquema de datos obligatorio.
