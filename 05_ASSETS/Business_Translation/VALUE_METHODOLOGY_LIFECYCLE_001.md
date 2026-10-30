# VALUE — Diseño integrado del estándar metodológico

**Identificador:** VALUE-STANDARD-ARCH-001  
**Versión:** 0.4  
**Estado:** estándar metodológico de referencia en evolución; apto para implementación web de referencia, sujeto a revisión de integridad y gobernanza  
**Tipo:** arquitectura metodológica de referencia  
**Fuente principal:** *Conversación Investigación TGCV.pdf*, especialmente las formulaciones del VCF, Value Construction Loop, Value System Model, CCV e IVS (pp. 770–845 y referencias posteriores).  
**Repositorio canónico:** `jcarmonabastida-pixel/TGCV`; esta especificación se mantiene como activo de aplicación/consultoría, separado del Core científico TGCV.  
**Principio de implementación:** el estándar debe poder aplicarse sin software específico; el futuro playground lo demostrará, pero no definirá por sí solo el estándar.

---

## 1. Propósito

Establecer una arquitectura única para VALUE que reduzca duplicidades y normalice el lenguaje. Esta base permite desarrollar de forma coordinada las fichas maestras A1–A8, el servicio **Value Discovery Sprint** y un prototipo web de referencia del ciclo completo, sin exigir que el piloto del servicio esté completado antes de iniciar el prototipo.

Esta versión consolida la arquitectura metodológica. No es todavía un manual de facilitación completo, un instrumento psicométrico, una oferta comercial cerrada ni una especificación de software.

## 2. Qué es VALUE

VALUE es el nombre paraguas de trabajo para una metodología orientada a desarrollar la capacidad de un sistema para construir valor de forma deliberada, repetible y sostenible.

La conversación de origen distingue varias piezas que deben conservarse, pero no tratarse como sinónimos:

| Concepto canónico | Definición de trabajo | Función |
|---|---|---|
| **Value Construction** | Proceso por el que un sistema combina conocimiento, capacidades y oportunidades para producir resultados considerados valiosos en un contexto. | Concepto central. |
| **Value Construction Framework (VCF)** | Proceso operativo que guía la intervención desde la comprensión de una oportunidad hasta la acción y el aprendizaje. | Define fases, preguntas y puertas de decisión. |
| **Value System Model (VSM)** | Modelo del sistema que se estudia: propósito, actores, necesidades, capacidades, conocimiento, relaciones, flujos, restricciones y resultados. | Describe qué se analiza y cómo se relacionan sus elementos. |
| **Value Architecture** | Diseño de conjunto que conecta el propósito, el modelo del sistema, las decisiones, la intervención y los resultados esperados. | Integra el VSM con el proceso VCF. |
| **Value Opportunity** | Situación contextualizada en la que existe una posibilidad plausible de construir valor y que requiere comprensión, capacidades, hipótesis y contraste. | Unidad principal de trabajo de una intervención. |
| **Capacidad de Construcción de Valor (CCV)** | Capacidad de un sistema para construir valor repetidamente y renovar las capacidades que lo hacen posible. | Capacidad objetivo que la metodología pretende desarrollar. |
| **Índice de Valor Sistémico (IVS)** | Instrumento propuesto para evaluar aspectos de la capacidad de construcción de valor. | Línea de medición exploratoria; no forma parte del flujo obligatorio mientras no esté definido y validado. |

**Regla terminológica:** VCF no es el VSM; VSM no es Value Architecture; una Value Opportunity no es una solución; CCV es una capacidad objetivo y el IVS es una propuesta de medición, no el valor producido.

## 3. Principios metodológicos de referencia

Estos principios se conservan como compromisos de diseño de VALUE, derivados de la conversación de origen. Son principios metodológicos propuestos, no leyes científicas demostradas.

1. **Comprender antes de prescribir.** No elegir una solución antes de entender el contexto y la oportunidad.
2. **El valor es contextual.** Especificar quién considera valioso qué resultado, en qué horizonte y con qué restricciones.
3. **El sistema importa.** Analizar actores, conocimiento, capacidades, relaciones, flujos y bloqueos, no solo departamentos o tecnologías aisladas.
4. **El conocimiento debe conectarse.** Facilitar perspectivas complementarias y hacer visibles desacuerdos y lagunas.
5. **Las alternativas son hipótesis.** Explicitar qué tendría que ser cierto y qué evidencia podría confirmarlo o contradecirlo.
6. **La decisión debe ser trazable.** Registrar criterios, evidencia, incertidumbre, responsable y razones.
7. **La ejecución y la adopción cuentan.** Un diseño o recomendación no equivale a un resultado realizado.
8. **Aprender significa cambiar capacidad.** El aprendizaje organizativo debe poder modificar prácticas, criterios, herramientas o relaciones, no quedarse solo en información documentada.
9. **La tecnología y la IA apoyan el proceso.** No sustituyen la verificación, el juicio ni la responsabilidad humana.
10. **Las afirmaciones no exceden la evidencia.** No asumir que más datos, más alternativas o más capacidad producen automáticamente más valor ni atribuir causalidad sin evaluación adecuada.

## 4. Ciclo de vida canónico

### 4.1 Decisión de normalización

La conversación contiene dos representaciones operativas:

- El **Value Construction Loop** de cinco pasos: **SENSE → CONNECT → DESIGN → ACT → LEARN**.
- El **VCF** de seis capacidades: **Sensing → Understanding → Designing → Deciding → Executing → Learning**, además de una fase de alineamiento inicial denominada **ALIGN**.

Para evitar dos procesos paralelos, esta versión adopta como ciclo operativo el **VCF de seis fases**, con **ALIGN como condición de entrada y gobernanza**. El Loop de cinco pasos queda como resumen comunicativo de alto nivel, no como un segundo proceso ni como una lista adicional de entregables. La decisión explícita se conserva como fase propia entre diseño y ejecución.

### 4.2 Fases

| Orden | Fase canónica | Pregunta guía | Función y salida mínima |
|---|---|---|---|
| 0 | **ALIGN — Alinear valor** (entrada/gobernanza) | ¿Qué valor buscamos, para quién y qué decisión hay que apoyar? | Propósito, alcance, actores clave, criterios, restricciones y responsable de decisión. |
| 1 | **SENSE — Percibir y descubrir** | ¿Qué está ocurriendo y qué oportunidad merece atención? | Oportunidad contextualizada, señales, necesidades y preguntas abiertas. |
| 2 | **CONNECT — Comprender e integrar** | ¿Cómo funciona el sistema y qué conocimiento debe conectarse? | Modelo compartido del sistema actual, capacidades, relaciones, flujos, fricciones y lagunas de evidencia. |
| 3 | **DESIGN — Diseñar alternativas** | ¿Qué opciones plausibles podrían responder a la oportunidad? | Alternativas, hipótesis de valor, supuestos, riesgos y diseño preliminar. |
| 4 | **DECIDE — Decidir con evidencia** | ¿Qué opción o prueba está justificada ahora? | Decisión trazable: avanzar, probar, reformular, aplazar o no continuar. |
| 5 | **ACT — Ejecutar y adoptar** | ¿Qué hace falta para llevar la decisión a la práctica? | Plan y registro de ejecución, responsables, adopción y resultados observables. |
| 6 | **LEARN — Aprender y renovar** | ¿Qué hemos aprendido y qué debe cambiar en la capacidad del sistema? | Resultados revisados, lecciones, capacidades a renovar y decisión sobre el siguiente ciclo. |

El proceso es iterativo, no una cascada rígida. Una fase puede reabrirse si aparece evidencia nueva, cambia el contexto o deja de sostenerse un supuesto crítico.

### 4.3 ALIGN es una condición de entrada, no un artefacto duplicado

ALIGN produce un único registro de intención de valor. La fase no debe generar simultáneamente un Value Purpose Canvas, un Value Intent Canvas y un Value Intent Document independientes con la misma información. Puede existir una plantilla visual para facilitar el trabajo, pero el registro canónico es uno: **Value Intent**.

### 4.4 Puertas de decisión

- **G0 — Encargo aceptado:** reto, alcance, responsable, participantes y condiciones de trabajo acordados.
- **G1 — Oportunidad entendible:** la oportunidad describe contexto, personas afectadas y posible valor; no es solo una solución solicitada.
- **G2 — Sistema suficientemente comprendido:** el modelo distingue observaciones, hipótesis, desacuerdos y lagunas.
- **G3 — Alternativas contrastables:** las opciones y sus supuestos están explícitos; las hipótesis críticas pueden ponerse a prueba.
- **G4 — Decisión justificada:** la evidencia es suficiente para la decisión concreta o se declara qué incertidumbre impide decidir.
- **G5 — Ejecución registrada:** se sabe qué se hizo, en qué condiciones y qué resultados se observaron.
- **G6 — Aprendizaje convertido en acción:** se decide qué mantener, cambiar, ampliar, repetir o detener.

Una puerta puede concluir con “no continuar” o “evidencia insuficiente”; no obliga a avanzar.

### 4.5 Selección de alternativa y autorización para ejecutar son decisiones distintas

La decisión de seleccionar una alternativa o autorizar el desarrollo de su diseño no equivale a autorizar su ejecución. La autorización para ejecutar debe ser explícita, emitida por la autoridad competente y especificar alcance, recursos, condiciones, salvaguardas y límites.

Si no existe autorización explícita para ejecutar, A7 permanece en estado de propuesta y ACT no se inicia. Una autorización limitada solo habilita las actividades incluidas expresamente en su alcance; no debe ampliarse por inferencia a otras actividades, personas, recursos o periodos.

A6 debe registrar qué se autoriza exactamente como siguiente paso: continuar el diseño, realizar preparativos operativos expresamente autorizados o ejecutar la intervención. La selección de una opción, por sí sola, no autoriza ninguna de estas actividades posteriores.


## 5. Value System Model (VSM): modelo único del sistema

El VSM es el modelo de referencia para representar la realidad que se estudia. La conversación original propone componentes, mapas y vistas diferentes. Esta versión los integra como **vistas de un mismo modelo**, no como modelos independientes que cada uno tenga que mantenerse por separado.

### 5.1 Componentes canónicos

1. **Intención de valor:** propósito, oportunidad, grupos afectados, resultados esperados, criterios y restricciones.
2. **Actores:** personas, equipos y organizaciones pertinentes.
3. **Necesidades y tensiones:** problemas, expectativas, objetivos en conflicto y contexto.
4. **Capacidades y recursos:** conocimientos, habilidades, procesos, activos, tecnología y recursos existentes o requeridos.
5. **Conocimiento y evidencia:** datos, experiencia, observaciones, fuentes, supuestos y resultados de pruebas.
6. **Relaciones:** vínculos de coordinación, intercambio, aprendizaje o generación conjunta de capacidades.
7. **Flujos:** cómo señales, conocimiento y decisiones pasan a la acción y a los resultados.
8. **Fricciones y restricciones:** bloqueos, dependencias, silos, retrasos, límites de recursos y reglas.
9. **Alternativas e hipótesis:** cambios posibles, condiciones de éxito y efectos esperados.
10. **Decisiones y acciones:** elecciones, responsables, compromisos y secuencias de ejecución.
11. **Resultados y aprendizaje:** resultados observados, efectos no previstos, lecciones y cambios de capacidad.

### 5.2 Vistas, no artefactos redundantes

| Nombre previo | Normalización |
|---|---|
| Value System Map | **Vista principal del VSM**. |
| Value Network Map | Vista de actores, relaciones y conocimiento dentro del VSM. |
| Collective Intelligence Map | Vista de perspectivas, aportaciones, acuerdos, discrepancias y lagunas dentro del VSM. |
| Value Capability Map | Vista de capacidades actuales y requeridas dentro del VSM. |
| Value Flow Map / Value Flow | Vista de flujos, transiciones, bloqueos y pérdidas dentro del VSM. |
| Value Friction | Concepto para clasificar fricciones, no un mapa independiente. |
| Value Gap | Comparación contextual entre situación actual y situación deseada, no un modelo adicional. |

Estas vistas pueden presentarse como capas o filtros de una misma representación. En una aplicación futura, deben reutilizar un modelo de datos compartido y evitar mantener copias divergentes de actores, relaciones y capacidades.

### 5.3 Flujo de referencia

**Señales y necesidades → conocimiento y comprensión → hipótesis y decisiones → acción → resultados observados → aprendizaje y capacidad renovada.**

Es una secuencia conceptual, no una ley causal ni necesariamente lineal. El VSM debe permitir mostrar ciclos de retroalimentación, retrasos, dependencias y evidencia contradictoria.

## 6. Catálogo normalizado de artefactos

La regla de normalización es: **un artefacto canónico por función de gestión; distintas plantillas o vistas pueden facilitarlo, pero no crear versiones paralelas de la misma información**.

### A1. Value Intent

- **Fase:** ALIGN.
- **Función:** fijar propósito, oportunidad inicial, personas afectadas, criterios de valor, restricciones, alcance y decisión que se quiere apoyar.
- **Consolida:** Value Purpose Canvas, Value Intent Canvas, Value Intent Document y partes de Discovery Brief.
- **Salida:** intención de valor acordada y criterios de éxito revisables con control de versión.

### A2. Value Opportunity Brief

- **Fase:** SENSE.
- **Función:** describir la oportunidad en contexto: situación observada, necesidades, personas afectadas, impacto potencial, fuentes, preguntas abiertas y supuestos iniciales.
- **Consolida:** Value Opportunity Map, Value Opportunity Canvas y Value Discovery Canvas cuando cumplen la misma función de encuadre.
- **Salida:** oportunidad delimitada y preguntas que deben investigarse.

### A3. Value System Model

- **Fase principal:** CONNECT; evoluciona durante todo el ciclo.
- **Función:** representar el sistema actual y, cuando proceda, la situación deseada mediante los componentes y vistas definidos en la sección 5.
- **Consolida:** Value System Map, Value Network Map, Collective Intelligence Map, Value Capability Map y Value Flow Map como vistas.
- **Salida:** modelo trazable de actores, necesidades, capacidades, conocimiento, relaciones, flujos, fricciones y lagunas.

### A4. Value Hypothesis & Options Record

- **Fase:** DESIGN.
- **Función:** registrar alternativas, hipótesis de valor, supuestos, capacidades requeridas, riesgos, efectos esperados y condiciones que permitirían descartar una opción.
- **Consolida:** Value Hypothesis Map/Canvas y las fichas de alternativas del Value Opportunity Canvas.
- **Salida:** conjunto de alternativas comparables y sus hipótesis explícitas.

### A5. Evidence Record

- **Uso:** transversal a las fases; se utiliza especialmente en DESIGN y DECIDE. «Validación» describe una actividad, no una fase adicional del VCF.
- **Función:** vincular cada hipótesis con la evidencia disponible, fuente, método, fecha, calidad, limitaciones, contradicciones y estado.
- **Consolida:** Evidence Matrix y registros separados de evidencia que cubren el mismo propósito.
- **Salida:** trazabilidad de qué se sabe, qué no se sabe y con qué fundamento.

### A6. Value Decision Record

- **Fase:** DECIDE.
- **Función:** documentar criterios, alternativas consideradas, evidencia relevante, trade-offs, riesgos, decisión, responsable, condiciones y razones para revisar la decisión.
- **Consolida:** Decision Framework, Opportunity Prioritization Matrix y VALUE Decision Report en una única decisión trazable. Los informes ejecutivos pueden ser una presentación de esta información, no otra fuente canónica.
- **Salida:** decisión justificada y próximos pasos.

### A7. Value Blueprint & Delivery Plan

- **Fases:** DESIGN y ACT, con estados diferentes.
- **Función:** describir la alternativa seleccionada y traducirla a ejecución: componentes, cambios, capacidades, dependencias, hitos, responsables, adopción, riesgos y métricas.
- **Consolida:** Value Blueprint y Value Delivery Map. Se mantiene un único artefacto con dos secciones/estados para evitar rediseñar y volver a copiar la misma solución.
- **Salida:** diseño aprobado y plan ejecutable.

### A8. Value Learning Record

- **Fase:** LEARN.
- **Función:** comparar resultados con intención y criterios iniciales, registrar efectos previstos/no previstos, límites de atribución, lecciones y cambios de capacidad.
- **Consolida:** Value Learning System como registro de aprendizaje y los informes retrospectivos que repitan la misma información.
- **Salida:** aprendizaje reutilizable y decisión explícita sobre el siguiente ciclo.

### 6.1 Elementos que no son artefactos canónicos

- **Value Radar:** técnica de exploración y captura de señales que alimenta A2.
- **AI Value Simulator:** posible herramienta para explorar escenarios; no es un entregable obligatorio ni una simulación validada por su nombre.
- **Opportunity Prioritization Matrix:** vista o técnica para comparar opciones dentro de A6.
- **Executive Value Report:** formato de comunicación que se genera a partir de los artefactos canónicos; no es una segunda fuente de verdad.
- **Plantillas, canvas, tableros y vistas:** interfaces de trabajo para producir o consultar artefactos; no deben duplicar el registro canónico.

## 7. Reglas de trazabilidad entre artefactos

La cadena mínima de trazabilidad es:

**Value Intent → Value Opportunity Brief → Value System Model → Value Hypothesis & Options Record → Evidence Record → Value Decision Record → Value Blueprint & Delivery Plan → Value Learning Record.**

Reglas:

1. Cada artefacto tiene un identificador estable, versión, estado, responsable, fecha y procedencia.
2. Cada hipótesis debe poder vincularse con una oportunidad y con una o más entradas de evidencia.
3. Cada decisión debe citar los criterios y la evidencia utilizados, incluidos límites y desacuerdos relevantes.
4. La ejecución debe apuntar a la decisión que autoriza el trabajo.
5. El aprendizaje debe apuntar a los resultados observados y a los criterios acordados en ALIGN.
6. No sobrescribir silenciosamente decisiones anteriores: registrar cambio, motivo y responsable.
7. Una ausencia de dato no se registra como evidencia positiva.
8. Un resultado observado no se atribuye automáticamente a VALUE; la atribución depende del diseño de evaluación y del contexto.

## 8. Medición: CCV e IVS fuera del flujo obligatorio

### 8.1 CCV

La **Capacidad de Construcción de Valor** es la capacidad objetivo del método. La conversación propone que se desarrolle mediante integración de conocimiento, capacidades, relaciones, acción y aprendizaje.

En la fuente aparecen tanto tres niveles (reactivo, gestionado, adaptativo) como una escala posterior de cinco niveles (reactivo, coordinado, sistémico, adaptativo, generativo). No se adopta ninguna escala como canónica en esta versión: la divergencia necesita una decisión y validación específicas.

### 8.2 IVS

La fuente presenta el **Índice de Valor Sistémico** como una posible medida de la capacidad de una organización para transformar conocimiento distribuido en decisiones y acciones generadoras de valor. En distintos momentos menciona seis u ocho dimensiones y no mantiene una definición completa única.

Por tanto, en este estándar v0.2:
- IVS es una línea de trabajo de medición, no un KPI listo para uso.
- No hay fórmula, ponderaciones ni escala numérica canónicas.
- No se calculará un agregado ni se compararán organizaciones como si la medida estuviera validada.
- El Value Discovery Sprint no requiere IVS para funcionar.
- Una futura especificación de medición deberá definir dimensiones, indicadores, fuentes, anclajes, fiabilidad, sesgos y límites de comparación.

### 8.3 Evaluación de casos

Cada caso debe acordar criterios apropiados antes de empezar. Pueden observarse calidad de evidencia, cambios de comprensión o decisión, tiempo hasta una decisión útil, adopción, resultados acordados y aprendizaje reutilizable. La selección de indicadores depende del caso; más actividad, más ideas o más transformaciones posibles no equivalen automáticamente a más valor.

## 9. Roles mínimos

- **Patrocinador / responsable de decisión:** define el reto y responde por la decisión.
- **Facilitador VALUE:** guía el proceso, cuida el rigor del método y la trazabilidad.
- **Participantes de dominio y operación:** aportan conocimiento y contrastan el modelo.
- **Personas afectadas / usuarios / clientes:** contribuyen con necesidades y evidencia cuando procede.
- **Responsable de ejecución:** responde por el plan, adopción, riesgos y seguimiento.
- **Apoyo analítico o IA:** realiza tareas delimitadas, con revisión y verificación humanas.

Los roles pueden combinarse en equipos pequeños, pero las responsabilidades no deben quedar implícitas.

## 10. Gobernanza del estándar

VALUE se debe desarrollar como estándar agnóstico de herramienta, con definiciones, artefactos y reglas versionadas. La futura aplicación será una implementación de referencia, no la autoridad exclusiva sobre el significado de los conceptos.

### 10.1 Tipos de cambio

- **Editorial:** mejora de claridad sin cambiar significado.
- **Terminológico:** cambio o consolidación de nombre; requiere actualizar glosario y referencias.
- **Metodológico:** cambio de fase, puerta, actividad o regla.
- **Estructural:** cambio de componentes del VSM o de relaciones entre artefactos.
- **Medición:** cambio de CCV, IVS, indicadores o escalas.
- **Implementación:** cambio técnico del playground o producto que no altera el estándar.

Los cambios metodológicos, estructurales y de medición requieren justificación, impacto en artefactos y ejemplos; los cambios editoriales no deben alterar semántica de manera inadvertida.

### 10.2 Contribución abierta

La comunidad podrá proponer cambios mediante issues y pull requests con:
- problema observado y contexto;
- definición o regla afectada;
- alternativa propuesta;
- artefactos y fases impactados;
- ejemplo que demuestre la necesidad;
- riesgos, compatibilidad y criterios de aceptación.

Las propuestas se revisan antes de integrarse. Una implementación de software no cambia automáticamente el estándar; las decisiones aceptadas se documentan en la especificación y se versionan. La licencia del repositorio y los derechos de uso deben comprobarse explícitamente antes de anunciar condiciones de contribución o reutilización.

## 11. Camino desde el estándar al prototipo web y la comunidad

Las líneas de normalización, especificación de artefactos, diseño del servicio y prototipo web se coordinan, pero no deben convertirse en una secuencia rígida que impida aprender mediante la implementación. La promoción del prototipo no declara cerrado el diseño del servicio piloto ni valida empíricamente el estándar.

### Línea A — Base metodológica de referencia

1. Mantener una versión identificada del maestro, el ciclo canónico, las puertas y las distinciones metodológicas.
2. Conservar explícitas las decisiones pendientes, los supuestos y los límites.
3. Revisar la coherencia entre maestro, fichas A1–A8 y ejemplos antes de cada promoción relevante.

**Estado en v0.4:** base metodológica identificada para implementar un prototipo de referencia; no equivale a validación empírica.

### Línea B — Fichas maestras y Value Discovery Sprint

1. Desarrollar y revisar las fichas A1–A8: propósito, contenido, campos, relaciones, responsable, entradas/salidas, reglas de calidad y ejemplos.
2. Mantener el Value Discovery Sprint como diseño de servicio piloto, con recorrido, preparación, roles, entregables y criterios de aceptación.
3. Evaluar su esfuerzo y utilidad cuando pueda probarse en un caso apropiado y autorizado.

**Estado:** fichas y Sprint continúan como especificaciones de trabajo en evolución. No es necesario completar un piloto comercial para empezar a construir el prototipo web.

### Línea C — Prototipo web y apertura comunitaria

1. Implementar progresivamente el recorrido VALUE sobre la versión identificada del maestro y las fichas disponibles.
2. Permitir consultar y editar los artefactos y sus vínculos, mostrando qué partes están implementadas, provisionales o pendientes.
3. Mostrar trazabilidad desde intención y oportunidad hasta decisión, ejecución y aprendizaje, sin confundir accesibilidad, recomendación, autorización y ejecución.
4. Hacer visibles incertidumbres, evidencia insuficiente y puertas no superadas; no simular validación automática cuando no exista.
5. Exportar los datos en un formato documentado y portable.
6. Preparar guía de uso, contribución, decisiones metodológicas, ejemplos y límites conocidos.
7. Invitar a usuarios y comunidad a evaluar, proponer mejoras y contribuir mediante gobernanza explícita.

**Estado:** línea habilitada por la decisión de la sección 16. El prototipo será una implementación de referencia para aprender y evolucionar, no un producto completo ni una prueba de validez del método.

## 12. Decisiones explícitamente pendientes

No deben ocultarse ni resolverse por conveniencia de implementación:

1. Si VALUE será el nombre formal definitivo y si VCF queda como nombre del proceso operativo.
2. Si se mantiene Value Architecture como concepto paraguas o como nombre de la arquitectura integradora.
3. La ontología formal del VSM: tipos de relación, cardinalidades y reglas de consistencia.
4. La escala definitiva de CCV y el diseño/validación del IVS.
5. La relación entre el estándar VALUE y las hipótesis científicas de TGCV.
6. Las reglas detalladas de evaluación de evidencia y de resultados.
7. Licencia abierta, gobierno de contribuciones y política de propiedad intelectual.
8. Duración, precio, alcance y criterios comerciales del Value Discovery Sprint.

## 13. Límite de relación con TGCV

VALUE es una metodología aplicada propuesta; TGCV es un programa de investigación. El posible puente consiste en estudiar si modelar explícitamente las transformaciones accesibles, sus condiciones y restricciones aporta información adicional a la comprensión de oportunidades y a la decisión. Esa utilidad debe contrastarse en casos concretos frente a una referencia adecuada.

No se asume que VALUE sea una traducción validada de TGCV, que un mapa del VSM equivalga al modelo formal TGCV ni que ampliar las posibilidades de transformación produzca automáticamente más valor. Las decisiones de negocio y los resultados de un piloto no validan por sí solos las afirmaciones científicas de TGCV.

## 14. Procedencia

Esta normalización se apoya especialmente en la conversación de investigación donde se introducen el VCF y sus seis capacidades, ALIGN y los artefactos iniciales (pp. 770–801); se definen Value Construction, Value Opportunity, Value Architecture y el Value Construction Loop (pp. 802–820); se presentan los ocho axiomas como propuesta (pp. 824–836); y se introduce el VSM (pp. 838–845). Las divergencias posteriores de CCV, IVS y potencial generativo se mantienen como temas abiertos, no como decisiones consolidadas.

Esta especificación integra y normaliza propuestas históricas para facilitar revisión. No convierte las ideas de la fuente en hechos validados ni elimina la necesidad de contraste con usuarios y casos reales.

## 15. Nota de versión

- **v0.3 (2026-10-30):** aclara la separación entre selección de alternativa, autorización para desarrollar su diseño y autorización explícita para ejecutar. Se establece que, sin autorización de ejecución emitida por la autoridad competente y con alcance, recursos, condiciones, salvaguardas y límites definidos, A7 permanece como propuesta y ACT no se inicia. La aclaración responde a la revisión documental A1–A8 basada en CLINIC-001; no constituye validación empírica ni aprobación definitiva del estándar.
- **v0.4 (2026-10-30):** habilita el prototipo web de referencia sin esperar a una evaluación interevaluador humana ni a un piloto del servicio; sustituye la secuencia rígida de etapas por líneas coordinadas de trabajo. Las fichas A1–A8 y el Value Discovery Sprint siguen en evolución; el prototipo debe declarar la versión y los límites que implementa. No constituye validación empírica.


## 16. Decisión de promoción a prototipo web — 2026-10-30

VALUE puede implementarse en un prototipo web de referencia a partir de una versión identificada de este estándar, sin esperar a completar evaluación interevaluador humana ni pruebas comunitarias. La evaluación individual CLINIC-001 se cerró con cobertura parcial documentada en el protocolo de usabilidad v0.7; las actividades con evaluadores externos y comunidad se mantienen como parte del ciclo posterior de evaluación y evolución.

Esta decisión no equivale a declarar el estándar validado ni elimina los controles de integridad, consistencia documental, seguridad, privacidad, accesibilidad o gobernanza que correspondan al prototipo. La implementación debe:

1. identificar la versión de VALUE que implementa y mantener trazabilidad con sus artefactos y decisiones;
2. distinguir funciones implementadas, provisionales, incompletas y aún no soportadas;
3. evitar presentar resultados ilustrativos o datos ficticios como evidencia real;
4. permitir recoger observaciones, problemas, propuestas y contribuciones sin convertirlas automáticamente en cambios del estándar;
5. mantener un proceso explícito de revisión, versionado y aceptación de cambios;
6. comunicar que VALUE es una metodología propuesta y en evolución, abierta a evaluación por usuarios y comunidad.

El prototipo es un medio para hacer VALUE examinable y mejorable en uso; no es por sí mismo una prueba de eficacia, causalidad ni validez empírica. La evaluación posterior con usuarios y colaboradores podrá aportar evidencia adicional y motivar nuevas versiones, sin que su ausencia bloquee esta primera implementación de referencia.

**Alcance de la decisión:** habilita preparar y construir el prototipo web. No autoriza por sí sola la promoción a `main`: esta seguirá sujeta a revisión de integridad del PR, coherencia de los artefactos, controles de gobernanza y aprobación explícita de la promoción.
