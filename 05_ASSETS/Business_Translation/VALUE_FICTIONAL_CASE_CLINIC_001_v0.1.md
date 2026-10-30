# VALUE — Caso ficticio integral: mejora del acceso a citas en una clínica

**Identificador:** VALUE-CASE-CLINIC-001  
**Versión:** 0.3  
**Estado:** EJERCICIO DOCUMENTAL FICTICIO — pendiente de revisión; no validado en una organización real  
**Documento rector:** [VALUE — Diseño integrado del estándar metodológico](VALUE_METHODOLOGY_LIFECYCLE_001.md)  
**Fichas canónicas:** [Especificaciones maestras A1–A8](VALUE_ARTIFACT_MASTER_SPECS_v0.1.md)  
**Sprint de referencia:** [VALUE Discovery Sprint](VALUE_DISCOVERY_SPRINT_v0.1.md)  
**Tipo de material:** caso sintético de extremo a extremo para comprobar cobertura, trazabilidad y usabilidad documental del ciclo VALUE.

> **Aviso de integridad:** la clínica, las personas, las cifras, las observaciones, las decisiones y los resultados de este documento son inventados para ilustrar el método. No son datos sanitarios reales ni evidencia de eficacia. Las conclusiones solo son válidas dentro de este escenario simulado.

## 1. Resumen ejecutivo

Una clínica ambulatoria ficticia de tamaño medio recibe quejas por demoras en la asignación de citas. La dirección sospecha problemas de coordinación entre recepción, profesionales sanitarios y administración, pero no conoce la causa raíz.

El caso recorre el ciclo VALUE completo: delimita la oportunidad; crea un modelo provisional del sistema; registra hipótesis y opciones; separa evidencias simuladas de inferencias; documenta una decisión acotada; define una prueba operativa hipotética; y registra resultados y limitaciones.

**Decisión ilustrativa:** probar durante cuatro semanas un protocolo de revisión diaria de solicitudes pendientes y excepciones de prioridad, sin modificar las reglas clínicas de priorización. La prueba solo se autorizaría tras confirmar capacidad, responsables, salvaguardas y disponibilidad de datos.

**Resultado simulado:** el porcentaje de solicitudes pendientes más allá del plazo interno de referencia baja del 28 % al 18 % en la muestra hipotética; las solicitudes prioritarias atendidas dentro de plazo se mantienen en el 96 %; y el personal informa de un aumento de carga administrativa. Estas cifras son inventadas y no permiten atribuir causalidad ni afirmar que la intervención funciona en una clínica real.

## 2. Escenario y límites

### 2.1 Contexto ficticio

- Organización: clínica ambulatoria de tamaño medio.
- Proceso observado: recepción, registro, priorización según reglas clínicas existentes, asignación y comunicación de citas.
- Síntoma inicial: quejas por demoras y solicitudes que permanecen pendientes.
- Sospecha inicial de la dirección: coordinación insuficiente entre recepción, administración y profesionales.
- Causa real: desconocida al inicio y no presupuesta como cierta.

### 2.2 Pregunta de decisión

**¿Qué cambio debería probar la clínica para mejorar el acceso a las citas sin deteriorar la calidad asistencial, sobrecargar al personal ni perjudicar a los pacientes con mayores necesidades?**

### 2.3 Alcance incluido

- Delimitar y comprender las demoras de asignación.
- Representar actores, recursos, reglas y relaciones relevantes.
- Comparar opciones de intervención de bajo riesgo.
- Definir una prueba limitada, reversible y supervisada.
- Revisar indicadores de acceso, prioridad clínica y carga de trabajo.
- Documentar aprendizaje, incertidumbre y siguiente decisión.

### 2.4 Fuera de alcance

- Diagnosticar o tratar pacientes.
- Cambiar criterios clínicos de priorización.
- Automatizar decisiones clínicas.
- Afirmar una causa raíz antes de recoger evidencia.
- Presentar las cifras del ejemplo como datos reales o resultados validados.
- Establecer que el método VALUE o la teoría TGCV quedan validados por este ejercicio.

## 3. Convenciones de evidencia y trazabilidad

Se utilizan estas etiquetas durante todo el caso:

- **[FICCIÓN-ESCENARIO]:** dato de partida inventado para construir el caso.
- **[SIMULADO]:** observación o cifra inventada para mostrar cómo se documentaría la evidencia.
- **[INFERENCIA]:** interpretación razonada a partir de los datos ficticios.
- **[HIPÓTESIS]:** explicación o predicción que todavía debe contrastarse.
- **[DECISIÓN ILUSTRATIVA]:** decisión tomada solo dentro del ejemplo.
- **[PENDIENTE REAL]:** información que una organización real tendría que confirmar.

Una cifra simulada no se convierte en hecho real por estar registrada en un artefacto. La evidencia que apoya una afirmación debe poder rastrearse a su fuente; en este ejercicio, la fuente es siempre un supuesto o conjunto de datos inventado.

## 4. ALIGN — A1 Value Intent

**ID:** CLINIC-001-A1  
**Estado:** borrador ilustrativo

### Propósito

Mejorar el acceso oportuno a las citas preservando la calidad y seguridad asistencial, la equidad para pacientes con mayores necesidades y una carga de trabajo sostenible.

### Personas y grupos afectados

- Pacientes y cuidadores.
- Personal de recepción.
- Personal administrativo.
- Profesionales sanitarios.
- Dirección y responsables de operaciones.

### Criterios iniciales de valor

1. Reducir las solicitudes que superan el plazo interno de referencia.
2. No deteriorar el acceso de pacientes con prioridad clínica.
3. Mantener las reglas y salvaguardas de calidad y seguridad.
4. No generar una sobrecarga desproporcionada al personal.
5. Conseguir una práctica operativa sostenible y comprensible.

### Restricciones que deben confirmarse

- Capacidad y disponibilidad de profesionales.
- Reglas vigentes de priorización clínica.
- Sistemas de registro y calidad de los datos.
- Tiempo disponible del personal.
- Presupuesto y autoridad para autorizar una prueba.

### Decisión que debe apoyar VALUE

Elegir entre intervenir, probar una alternativa de forma limitada, investigar más o no cambiar todavía el proceso.

### Gobernanza mínima propuesta

- **Patrocinador:** responsable de operaciones (rol ficticio).
- **Responsable del proceso:** coordinación de citas (rol ficticio).
- **Responsable de salvaguardas clínicas:** profesional designado por la clínica (rol ficticio).
- **Personal participante:** representantes de recepción, administración y equipo asistencial.
- **Autoridad de autorización:** debe identificarse formalmente antes de cualquier piloto real.

### Revisión de ALIGN

El propósito está suficientemente definido para explorar la oportunidad, pero la autoridad decisora, los plazos de referencia reales, la capacidad y las salvaguardas deben confirmarse. En una implantación real no se avanzaría a ejecución sin esos acuerdos.

## 5. SENSE — A2 Value Opportunity Brief

**ID:** CLINIC-001-A2  
**Estado:** borrador ilustrativo revisado mediante autoevaluación guiada; no validado en una organización real

### Oportunidad delimitada

Comprender en qué puntos del proceso de citas programadas se acumulan las solicitudes pendientes y qué factores modificables contribuyen a las demoras, sin asumir que la coordinación sea necesariamente la causa. La investigación debe contrastar la demanda con la capacidad planificada y examinar si las demoras y sus efectos difieren según el tipo de solicitud y las necesidades de los pacientes.

### Síntomas iniciales y estado del conocimiento

- [FICCIÓN-ESCENARIO] Existen quejas por demoras en la asignación de citas.
- [FICCIÓN-ESCENARIO] La dirección sospecha problemas de coordinación.
- [PENDIENTE REAL] No se conoce la distribución de los tiempos por tipología, prioridad, criticidad o impacto asistencial, etapa del proceso ni periodo temporal.
- [PENDIENTE REAL] No se han comprobado la disponibilidad, integridad, consistencia ni fiabilidad de los registros necesarios.
- [PENDIENTE REAL] No se ha establecido si existe un camino crítico en el proceso ni qué evidencia permitiría identificarlo.

### Preguntas de descubrimiento

1. ¿Cuánto tiempo transcurre entre la recepción, las etapas intermedias relevantes y la asignación de cada solicitud?
2. ¿En qué etapas se acumulan solicitudes pendientes y qué volumen permanece en cada una?
3. ¿Cuáles son los motivos de bloqueo y cómo varían por tipo de solicitud?
4. ¿Cómo se identifican y escalan las solicitudes prioritarias conforme a las reglas existentes?
5. ¿Cómo se distribuyen los tiempos y las demoras por tipología, prioridad y criticidad o impacto asistencial? Estas dimensiones no se presuponen equivalentes.
6. ¿Hay diferencias entre grupos de pacientes en sus necesidades y en las consecuencias que las demoras tienen para ellos?
7. ¿Qué información falta con mayor frecuencia y qué tareas repetidas o interrupciones afectan a los equipos?
8. ¿Qué registros e indicadores existen, qué campos contienen y con qué calidad, consistencia y fiabilidad?
9. ¿Cómo varía el volumen de solicitudes a lo largo del tiempo? ¿Los datos permiten valorar una posible estacionalidad?
10. ¿Cómo se relacionan la demanda y su tipología con la capacidad planificada y registrada del servicio?
11. ¿Existe un camino crítico en el proceso? ¿Qué etapas, dependencias o esperas lo determinarían y qué evidencia permitiría confirmarlo?
12. ¿Qué fuentes de datos pueden consultarse legítimamente y con qué autorización, minimización y controles de privacidad?

### Alcance inicial del análisis de datos

- **Horizonte temporal propuesto:** histórico de doce meses, sujeto a disponibilidad, calidad y cobertura de los datos. Permite una primera valoración de posibles patrones anuales, pero un único año no demuestra por sí solo que exista una pauta estacional recurrente. Si existen históricos anteriores comparables, conviene considerarlos.
- **Granularidad:** registro de solicitudes al máximo nivel de detalle disponible y adecuado para reconstruir tiempos, etapas, estados, pendientes y motivos de bloqueo. El nivel de detalle queda condicionado por la calidad real de los registros y la protección de datos.
- **Análisis:** examinar tiempos, volumen de pendientes y motivos de bloqueo tanto agregados como desglosados por tipo; cuando los datos y definiciones lo permitan, incluir prioridad, criticidad/impacto asistencial y diferencias relevantes entre grupos de pacientes.
- **Capacidad:** para el primer análisis se utilizará la capacidad planificada y registrada, contrastada con el volumen y la tipología de la demanda. No se exige inicialmente reconstruir la capacidad efectiva minuto a minuto.
- **Supuesto explícito de capacidad:** el ejercicio asume una gestión adecuada por parte de la clínica de las ausencias planificadas y no planificadas. Es una condición de trabajo no verificada, no un hecho establecido. Si los resultados no explican las demoras o aparecen indicios relevantes en contra, el supuesto deberá revisarse.
- **Alcance asistencial:** se estudian citas programadas dentro del horario establecido; las urgencias quedan fuera de alcance. No se presupone una ampliación horaria.

### Hipótesis iniciales — no confirmadas

- **H1:** parte de las demoras podría relacionarse con solicitudes incompletas.
- **H2:** la ausencia de una revisión compartida de pendientes podría retrasar la detección de bloqueos.
- **H3:** la capacidad planificada podría no corresponderse con el volumen o la tipología de la demanda en determinados periodos.
- **H4:** algunos pasos administrativos podrían duplicarse.
- **H5:** las demoras podrían variar por tipología, prioridad, criticidad/impacto asistencial o grupo de pacientes.
- **H6:** el volumen de solicitudes podría mostrar variaciones temporales o estacionales.

Estas hipótesis son líneas de investigación, no causas demostradas. No se asignan categorías, umbrales ni puntuaciones clínicas inventadas.

### Datos necesarios y controles para un caso real

Como mínimo, se investigará la disponibilidad de fechas y estados de las solicitudes, tiempos entre etapas, tipología, prioridad conforme a reglas existentes, motivos de bloqueo, devoluciones por información incompleta, registros de pendientes, capacidad planificada y variables temporales pertinentes. La disponibilidad de campos para caracterizar criticidad/impacto y grupos de pacientes debe comprobarse; no se presume que estén registrados.

Antes de analizar datos reales habrá que confirmar definiciones, cobertura, integridad, consistencia, datos ausentes y posibles sesgos, además de la autorización de acceso y los controles adecuados de privacidad. La ausencia de un dato no debe interpretarse como evidencia de ausencia del problema.

### Relación con A1

A1 debe considerar desde el encuadre inicial la posible existencia de un camino crítico, la estacionalidad del volumen y la relación entre demanda, capacidad y restricciones del servicio. A2 investigará estas cuestiones con los datos y evidencias disponibles; no anticipa sus conclusiones ni sustituye la decisión de valor de A1.

### Criterio de salida de SENSE

A2 estará suficientemente delimitado para pasar a modelar el sistema cuando estén identificados el proceso y sus límites, los grupos afectados, las preguntas de descubrimiento, los datos y fuentes potencialmente disponibles, las principales incertidumbres y los supuestos de trabajo. Si no se dispone de información suficiente para responder las preguntas, esa carencia se documentará como resultado y podrá requerir investigación adicional.

Este ejercicio demuestra únicamente la estructura documental y el registro de una autoevaluación guiada. No demuestra que se hayan recogido datos reales, que exista estacionalidad o camino crítico, que la capacidad sea insuficiente ni que se haya identificado una causa raíz.

## 6. CONNECT — A3 Value System Model

**ID:** CLINIC-001-A3  
**Estado:** modelo conceptual provisional

### Elementos del sistema

| Elemento | Función en el proceso | Incertidumbre |
|---|---|---|
| Paciente/cuidador | Presenta solicitud y aporta información | Necesidades y barreras diversas |
| Recepción | Recibe y registra solicitudes | Calidad y completitud de la entrada |
| Administración de citas | Revisa pendientes y asigna según reglas | Carga, colas y criterios de escalado |
| Profesional sanitario | Aporta criterio clínico cuando procede | Disponibilidad y tiempos de respuesta |
| Sistema de registro | Conserva estados y fechas | Calidad y consistencia de los datos |
| Coordinación de citas | Supervisa el flujo y resuelve bloqueos | Autoridad y visibilidad del proceso |
| Dirección de operaciones | Autoriza recursos y cambios operativos | Restricciones presupuestarias y de capacidad |

### Macroetapas propuestas durante la autoevaluación guiada

La revisión identifica cuatro macroetapas funcionales propuestas por el usuario. Se incorporan como estructura provisional del modelo, sin afirmar que describan todavía el procedimiento real ni que cada macroetapa sea una única etapa operativa:

1. **Recepción, clasificación y registro de la solicitud.**
2. **Asignación y escalado de la solicitud.**
3. **Monitorización, supervisión y comunicación del estado y progreso de la solicitud a lo largo del proceso.**
4. **Resolución, asignación y revisión de citas.**

Estas macroetapas son una vista de alto nivel. Su secuencia exacta, los traspasos entre responsables, los estados intermedios, las condiciones de escalado y la relación entre asignación y resolución deben detallarse y contrastarse con información del proceso. La comunicación y la supervisión pueden atravesar varias macroetapas, por lo que no se presuponen como actividades aisladas de una sola fase.

### Flujo conceptual

1. Recepción de la solicitud.
2. Registro y comprobación de información.
3. Aplicación de las reglas vigentes de prioridad.
4. Si falta información, solicitud de aclaración y seguimiento.
5. Si hace falta criterio clínico, derivación al profesional correspondiente.
6. Asignación de cita conforme a las reglas y capacidad disponibles.
7. Comunicación al paciente y actualización del estado.
8. Revisión de pendientes y escalado de excepciones.

Este flujo es una representación de trabajo del escenario, no una descripción verificada de una clínica existente.

### Condición transversal de avance y atención: capacidad y roles

La aportación de la autoevaluación identifica una condición necesaria: **debe existir capacidad disponible y asignada a los roles adecuados para que la solicitud pueda tramitarse y atenderse**.

En el modelo provisional, esto se registra como una dependencia transversal del proceso, no como una causa única ni como garantía suficiente de avance. Quedan por aclarar y contrastar:
- qué roles intervienen en cada macroetapa y qué responsabilidad tiene cada uno;
- qué significa capacidad disponible para cada rol y cómo se registra;
- cómo se detecta que falta capacidad o que una solicitud está esperando a un rol;
- qué reglas autorizadas determinan el escalado o la reasignación, si procede.

No se presuponen cifras de capacidad, umbrales, reglas nuevas ni mecanismos de sustitución.

### Continuidad del flujo y escalado ante falta de capacidad

La orientación propuesta en la autoevaluación es mantener, en la medida de lo posible, la continuidad del flujo. Cuando la capacidad del rol requerido no esté disponible, la solicitud debería escalarse conforme a mecanismos y responsabilidades definidos, en lugar de asumir que debe permanecer indefinidamente en espera.

Esta orientación depende de un **supuesto que debe verificarse**: que el dimensionamiento del personal sea suficiente y adecuado por grupos o niveles de atención, soporte y resolución de solicitudes. No se da por probado que ese dimensionamiento exista ni que sea suficiente en el escenario real.

Queda pendiente precisar qué niveles y roles existen, qué criterios autorizados rigen el escalado, qué capacidad tiene cada nivel y cómo se gestionan los casos en que tampoco exista capacidad en el nivel receptor. No se presume que escalar garantice por sí solo una resolución más rápida.

### Información que debe acompañar a la solicitud

Como requisito funcional provisional del modelo, cada solicitud debería conservar durante todo el flujo:
- su estado actual;
- la información recibida;
- las actuaciones ya realizadas;
- el responsable actual;
- el motivo de cualquier bloqueo;
- los **tiempos de respuesta y de resolución acordados** aplicables.

Los tiempos acordados deben distinguirse de los tiempos observados: los primeros son referencias o compromisos que deben identificarse y confirmar; los segundos deben obtenerse de registros fiables. No se presuponen aquí valores, plazos ni compromisos concretos. Queda por confirmar dónde se documentan esos datos y cómo se actualizan y consultan durante los traspasos entre roles.

### Ownership transversal del proceso e integridad de la información

Se propone que un **rol o función asuma el ownership de extremo a extremo del proceso**, con responsabilidad de asegurar que la información de cada solicitud se mantenga actualizada durante todo su recorrido. Este ownership transversal no implica que esa función realice personalmente todas las tareas ni sustituya la responsabilidad operativa de cada rol que interviene.

Quedan por definir para el caso real o para una versión más detallada del modelo: el rol concreto que ejercerá ese ownership, su autoridad para pedir actualizaciones y resolver incumplimientos, cómo se coordinan las responsabilidades de actualización de cada etapa y qué mecanismo permite detectar información desactualizada. No se presume que el rol de coordinación de citas ya tenga formalmente esta responsabilidad.

### Responsabilidad transversal end-to-end del ownership

Además de mantener actualizada la información de las solicitudes, el rol o función propietaria del proceso asume las tareas transversales de **monitorización, supervisión y comunicación end-to-end**. Esto incluye seguir el estado y progreso de las solicitudes, vigilar los tiempos acordados de respuesta y resolución, identificar desviaciones y coordinar o activar el escalado conforme a las reglas autorizadas, y asegurar que el estado relevante se comunique a los roles implicados y, cuando corresponda, a la persona solicitante.

Esta responsabilidad transversal no sustituye la ejecución de las tareas propias de cada rol ni autoriza a cambiar criterios clínicos o reglas de prioridad. El rol concreto, su autoridad, los canales de comunicación, la frecuencia de supervisión y las reglas de escalado deben definirse y confirmarse antes de aplicar el modelo a una organización real.

### Escalado por incumplimiento de niveles de servicio y por excepciones

El ownership transversal debe activar el **escalado funcional y jerárquico** conforme a los umbrales de incumplimiento de los niveles de servicio acordados. También debe poder activar el escalado **bajo demanda explícita ante situaciones excepcionales**, entre ellas quejas o reclamaciones formales e insatisfacción general con el servicio.

Los umbrales, los niveles funcionales y jerárquicos, los destinatarios, los tiempos de actuación y el tratamiento de cada tipo de excepción deben estar definidos y autorizados; no se inventan valores ni una matriz de escalado para este caso. La insatisfacción general debe concretarse mediante señales o criterios acordados, sin asumir una medición que aún no se haya definido.

### Información mínima para una escalación accionable

En la medida de lo posible, la información remitida al nivel funcional o jerárquico al que se escala debe incluir, además del contexto e historial de la solicitud:
- **motivo del escalado** y regla o umbral que lo activa, cuando corresponda;
- **actuaciones requeridas** o siguiente acción pendiente;
- **decisión esperada** del responsable receptor.

Estos campos se incorporan como requisitos funcionales propuestos. Su formato, obligatoriedad según tipo de escalado y responsables de completarlos deben concretarse; no se presume que exista ya una plantilla o herramienta que los recoja.

### Confirmación de recepción y trazabilidad de la actuación escalada

El responsable que recibe una solicitud escalada debe **confirmar que la asume** y registrar la actuación realizada y/o la decisión adoptada. El ownership transversal utiliza esa confirmación para mantener el seguimiento end-to-end hasta el cierre, comprobar el progreso y comunicar el estado pertinente.

Quedan por definir el mecanismo y el plazo de confirmación, así como el tratamiento de una escalación no aceptada o no respondida. No se presuponen herramientas, automatizaciones ni tiempos concretos.

### Rechazo de cita sin capacidad para ofrecer una alternativa

Si el paciente rechaza la cita y no existe capacidad disponible para ofrecer otra alternativa adecuada, la solicitud **permanece abierta** y se activa el escalado conforme a las reglas funcionales y jerárquicas autorizadas. La falta de capacidad en el nivel receptor no equivale a una resolución: el responsable end-to-end mantiene el seguimiento, registra el bloqueo y las actuaciones/decisiones, y coordina la comunicación del estado hasta que exista una alternativa o una decisión autorizada.

Si no puede ofrecerse una alternativa, la solicitud permanece pendiente; no se cierra únicamente porque se haya escalado o porque no haya capacidad disponible. Si la demora pudiera comprometer la atención necesaria, debe aplicarse el procedimiento clínico de priorización y escalado que corresponda, sin esperar indefinidamente a que aparezca capacidad.

**Pendiente antes de uso real:** definir niveles y destinatarios de escalado, actuación cuando el nivel receptor tampoco tenga capacidad, criterios de decisión autorizada y procedimiento clínico aplicable ante riesgo por demora. No se inventan plazos, recursos ni reglas clínicas.

### Condiciones propuestas para el cierre de una solicitud

El registro de cierre solo debe realizarse cuando:
- la cita esté asignada y comunicada al paciente;
- el paciente haya **aceptado y confirmado la cita antes de registrar el cierre**;
- la información de la solicitud y las actuaciones relevantes esté actualizada;
- no queden actuaciones o escalados pendientes, o estos se hayan resuelto conforme a las reglas aplicables.

La aceptación expresa y confirmación por el paciente es una vía de cierre. Si el paciente **rechaza** la cita, la solicitud permanece abierta y vuelve al flujo de asignación/escalado para su gestión. Si no responde dentro de un **plazo predefinido**, se asume aceptación tácita y la solicitud puede avanzar hacia el cierre, siempre que se cumplan las demás condiciones de cierre y quede registrado el vencimiento del plazo y la regla aplicada. El plazo, la forma de comunicarlo al paciente, los intentos/canales de contacto y la validez de esta aceptación tácita deben definirse y autorizarse expresamente; no se inventan valores ni se presupone que esa regla esté actualmente aprobada.

### Rechazo de cita sin capacidad disponible para una alternativa

Si el paciente rechaza la cita ofrecida y no existe capacidad disponible para ofrecer una alternativa adecuada, la solicitud **permanece abierta** y no se registra como cerrada por el mero hecho de haber sido escalada o de no existir capacidad en ese momento.

- El rol propietario del proceso mantiene el seguimiento end-to-end, conserva actualizado el estado y el motivo del bloqueo y comunica la situación pertinente.
- Se activa el escalado funcional y/o jerárquico conforme a las reglas autorizadas, buscando una alternativa adecuada sin alterar las reglas clínicas de prioridad.
- Si el nivel receptor tampoco dispone de capacidad, la solicitud continúa abierta y bajo seguimiento; la escalación no se considera resuelta por sí misma.
- Si no puede ofrecerse una alternativa, se registra el bloqueo y la solicitud queda pendiente hasta que exista una solución o se adopte una decisión por la autoridad competente conforme a reglas previamente definidas.
- Si la demora pudiera comprometer la atención necesaria, debe activarse el procedimiento clínico apropiado de priorización/escalado, sin esperar indefinidamente a que aparezca capacidad ordinaria.

Esta es una regla funcional propuesta para el caso ficticio, no un procedimiento clínico aprobado. Quedan por definir la autoridad competente, los mecanismos de escalado cuando tampoco hay capacidad en el nivel receptor, las comunicaciones al paciente y los criterios para determinar cuándo una demora requiere activar salvaguardas clínicas. No se inventan plazos, umbrales ni soluciones de capacidad.


### Gestión del rechazo cuando no hay capacidad para una alternativa

Si el paciente rechaza la cita ofrecida y no existe capacidad disponible para ofrecer una alternativa adecuada, la solicitud **permanece abierta** y no se registra como cerrada por el mero hecho de haberse escalado o de no existir capacidad inmediata.

- El ownership end-to-end mantiene el seguimiento, conserva actualizado el estado y el motivo del bloqueo, y comunica el estado pertinente.
- La solicitud se escala al nivel funcional o jerárquico que corresponda conforme a las reglas autorizadas. Si el nivel receptor tampoco dispone de capacidad, la solicitud continúa abierta y bajo seguimiento; el escalado no se considera por sí mismo una solución.
- Si todavía no hay alternativa disponible, se registra el bloqueo y la solicitud permanece pendiente hasta que exista una solución adecuada o se adopte una decisión autorizada conforme a las reglas aplicables.
- Si la demora pudiera comprometer la atención necesaria, debe activarse el procedimiento autorizado de priorización o escalado clínico que corresponda, sin esperar indefinidamente a que aparezca capacidad ordinaria.

Esta es una regla funcional propuesta para el caso ficticio, no un procedimiento clínico u operativo aprobado. Antes de aplicarla en una organización real deben confirmarse los niveles y destinatarios de escalado, la autoridad para decidir, el tratamiento de la falta persistente de capacidad y las salvaguardas clínicas. No se inventan plazos ni se presume que el escalado garantice una alternativa.


### Bloqueo por falta de información entre etapas

Si la etapa siguiente no puede comenzar porque falta información necesaria, la solicitud permanece abierta y no avanza como si se cumplieran los requisitos. Se registra la información pendiente y, cuando sea posible, quién debe aportarla. El responsable end-to-end mantiene el seguimiento y el estado actualizado hasta que se complete la información o exista una decisión autorizada sobre cómo proceder.

Antes de un uso real deben definirse los requisitos mínimos de información por etapa, las responsabilidades para aportarla y el procedimiento de seguimiento cuando no esté disponible. Esta es una regla funcional propuesta para el caso ficticio; no establece plazos ni responsabilidades reales.

### Discrepancias entre fuentes de información

Si la información necesaria está disponible, pero existen contradicciones entre fuentes o registros, la solicitud permanece abierta y no se toman decisiones que dependan de ese dato como si fuera fiable.

- Se registra qué información discrepa y la procedencia de las fuentes implicadas.
- El responsable end-to-end mantiene el seguimiento hasta que la discrepancia se resuelva o una persona autorizada determine cómo proceder.
- No se presume que una fuente prevalece sobre otra: los criterios de autoridad, verificación y resolución deben definirse antes del uso real.

Esta es una regla funcional propuesta para el caso ficticio. No establece una jerarquía real de fuentes ni un procedimiento clínico aprobado.

### Información imprescindible no disponible ni recuperable

Si una información necesaria no está disponible y tampoco es posible obtenerla, se registra qué dato falta y por qué no se ha podido obtener. Si es imprescindible para avanzar con seguridad o cumplir los requisitos del proceso, la solicitud permanece abierta y no se sustituye el dato por una suposición no declarada.

Si existe una alternativa para proceder sin esa información, debe someterse a una decisión autorizada, dejando constancia de la justificación, las limitaciones y las condiciones aplicables. No se presume que la alternativa sea válida ni que la ausencia del dato pueda ignorarse.

Antes del uso real deben definirse los criterios para distinguir información imprescindible de información prescindible, quién puede autorizar una alternativa y cómo documentar sus límites. Esta es una regla funcional propuesta para el caso ficticio, no un procedimiento clínico aprobado.

### Ambigüedad de responsabilidad entre roles

Si dos roles consideran que el siguiente paso corresponde al otro y ninguno actúa, la solicitud no debe quedar sin seguimiento. Se registra la acción pendiente y la ambigüedad de responsabilidad. El responsable end-to-end mantiene el seguimiento y promueve que se determine quién debe actuar conforme a las responsabilidades autorizadas.

No se presume que el responsable end-to-end tenga autoridad para reasignar cualquier tarea. Si las reglas existentes no permiten resolver el desacuerdo, se eleva a la persona o instancia autorizada. Antes del uso real deben definirse las responsabilidades por etapa y el mecanismo para resolver estos casos.

Esta es una regla funcional propuesta para el caso ficticio, no una asignación real de responsabilidades.

### Continuidad operativa ante la indisponibilidad de una persona responsable

La continuidad de la solicitud no debe depender de la disponibilidad de una persona concreta. Para evitar bloqueos prolongados o solicitudes que queden en un limbo de responsabilidad, debe existir un procedimiento predefinido de continuidad operativa.

- Cuando la persona asignada a una tarea esté ausente o no pueda actuar, el responsable end-to-end podrá asumir temporalmente la responsabilidad delegada de esa tarea, ejecutándola si está autorizado y capacitado para ello, o asignándola a otra persona autorizada.
- Esta facultad debe estar expresamente prevista en el procedimiento y delimitada por las competencias, autorizaciones y salvaguardas aplicables; no se presume una autoridad ilimitada ni que el responsable end-to-end pueda ejecutar cualquier tarea.
- La tarea y la solicitud permanecen trazables, con responsable actual identificado, estado, motivo del bloqueo y acciones pendientes actualizados.
- En este caso, las funciones críticas que requieren respaldo de continuidad son las directamente vinculadas a garantizar la atención sanitaria al paciente en el día y hora de la cita. No se extiende automáticamente este requisito de cobertura crítica al proceso administrativo de concertación o gestión de la cita en sí mismo.
- Las funciones críticas de atención sanitaria deben disponer de una cobertura alternativa formalmente designada, respaldada por un protocolo de actuación predefinido que establezca cómo se activa y opera. La cobertura debe estar efectivamente disponible cuando se necesite, con personas autorizadas y competentes, responsabilidades y límites explícitos; no basta con una designación nominal.
- La capacidad de la cobertura debe dimensionarse para asumir la atención sanitaria prevista sin generar una sobrecarga que comprometa la continuidad o la calidad de la atención. La forma de dimensionarla y verificarla debe definirse con criterios operativos y clínicos autorizados; no se presuponen cifras ni umbrales.
- El protocolo debe contemplar también las ausencias imprevistas de profesionales sanitarios el mismo día de la cita. Debe prever un mecanismo de sustitución por un profesional autorizado y competente o, cuando no sea posible, una reprogramación que preserve la atención necesaria al paciente conforme a los criterios clínicos y de prioridad aplicables. La ausencia no debe traducirse en una cancelación sin seguimiento ni en una reprogramación automática que ignore las necesidades clínicas.
- Si no hay sustituto disponible, la decisión de reprogramar debe considerar la prioridad clínica y las consecuencias de la demora para cada paciente. Cuando la demora pueda comprometer la atención necesaria, el caso debe remitirse al profesional sanitario responsable o a la instancia clínica autorizada para que determine cómo proceder. La decisión y su justificación deben quedar registradas y comunicarse al paciente conforme al procedimiento aplicable; el personal administrativo no debe sustituir el criterio clínico.
- Cuando una ausencia imprevista implique reprogramar la cita, el paciente debe recibir una comunicación proactiva, sin tener que contactar por iniciativa propia para conocer la situación. La comunicación debe explicar, de forma adecuada y comprensible, la incidencia, la alternativa prevista o el estado de su gestión y los siguientes pasos, incluido cuándo y cómo recibirá nueva información si todavía no hay una solución confirmada. Debe mantenerse el seguimiento hasta que la situación quede resuelta y comunicada.
- Una cita reprogramada no se considera resuelta por el mero hecho de haber propuesto o asignado una nueva fecha. Debe constar que el paciente ha recibido la comunicación y que ha aceptado la nueva cita. Si no responde, solo podrá aplicarse el procedimiento de seguimiento previamente definido; la solicitud no se cerrará hasta que se cumpla el resultado y las condiciones establecidos en ese procedimiento. No se presume aceptación tácita ni se inventan plazos o reglas de cierre.
- Si, tras los intentos de contacto previstos en el procedimiento, el paciente no responde, la solicitud permanece abierta y se activa una revisión por el responsable end-to-end. No debe cerrarse automáticamente por falta de respuesta. La revisión debe determinar y registrar los siguientes pasos conforme a las reglas autorizadas y a la situación clínica, sin presumir que la ausencia de respuesta equivale a aceptación o renuncia a la atención.
- En esa revisión, el responsable end-to-end debe distinguir, conforme a la información disponible y sin hacer inferencias clínicas fuera de su competencia, entre una falta de respuesta asociada a cuestiones administrativas y una situación en la que la falta de contacto pueda ocultar una necesidad asistencial no atendida. Cuando existan indicios o incertidumbre relevante sobre una posible necesidad asistencial, debe solicitarse revisión por el profesional sanitario responsable o la instancia clínica autorizada. La clasificación, los indicios considerados, la derivación y los pasos acordados deben quedar registrados.
- Cuando la revisión clínica determine que el paciente necesita atención en un plazo que no puede garantizarse con la nueva cita propuesta, debe existir un mecanismo alternativo de priorización y respuesta asistencial, definido por la autoridad clínica. La decisión sobre ese mecanismo corresponde a dicha autoridad, no al personal administrativo ni al responsable end-to-end. Antes del uso real deben definirse y autorizarse el mecanismo, sus responsables, criterios, vías de activación y seguimiento; no se inventan umbrales ni reglas clínicas.

- El procedimiento debe definir también qué ocurre si el propio responsable end-to-end está indisponible, para que exista una continuidad alternativa previamente autorizada y no se genere un nuevo vacío de responsabilidad.
- La importancia de la cita y las posibles consecuencias de la demora deben seguir tratándose conforme a los criterios y procedimientos clínicos autorizados; no se presupone que toda cita sea urgente ni que una tarea administrativa pueda sustituir una decisión clínica.

Antes del uso real deben identificarse las funciones de atención sanitaria que requieren cobertura crítica, designar formalmente sus coberturas alternativas, definir y probar el protocolo de activación y actuación —incluido el tratamiento de ausencias imprevistas el mismo día, la derivación a criterio clínico cuando no haya sustituto o cuando la falta de respuesta pueda ocultar una necesidad asistencial, la comunicación proactiva y el seguimiento de la aceptación o falta de respuesta del paciente—, dimensionar y verificar la capacidad de respaldo, y concretar el alcance de la delegación, las tareas que pueden asumirse o reasignarse, los límites de competencia y los mecanismos de registro, seguimiento, comunicación y cierre. La continuidad del proceso de concertación de citas debe gestionarse con sus propias reglas operativas, sin confundirla con el respaldo crítico de la atención sanitaria en el momento de la cita. Esta es una propuesta funcional para el caso ficticio, no un procedimiento clínico u organizativo aprobado.

### Seguimiento temporal y revisión de solicitudes bloqueadas

Para evitar que una solicitud permanezca bloqueada durante un tiempo excesivo, incluso cuando tiene un responsable identificado, debe existir un mecanismo predefinido de seguimiento y revisión de bloqueos.

- El procedimiento debe establecer plazos autorizados para actuar, revisar el bloqueo y, cuando corresponda, escalarlo.
- El incumplimiento de un plazo debe activar una actuación definida y trazable; no basta con registrar que la demora continúa.
- La revisión debe comprobar el motivo del bloqueo, las acciones realizadas, la responsabilidad vigente y si procede activar la continuidad operativa o el escalado.
- Los plazos, prioridades y actuaciones deben estar definidos y autorizados conforme a criterios clínicos y organizativos aplicables. No se inventan umbrales ni se presupone que todas las citas tengan la misma prioridad.

Antes del uso real deben concretarse los plazos, responsables de revisión, disparadores de escalado y actuaciones asociadas. Esta es una propuesta funcional para el caso ficticio, no un protocolo clínico aprobado.

### Resolución operativa ordinaria y escalado jerárquico excepcional

La gestión ordinaria de citas debe resolverse mediante responsabilidades, sustituciones y delegaciones predefinidas, sin depender de intervenciones jerárquicas superiores para incidencias habituales.

- El responsable asignado ejecuta la tarea conforme a sus competencias; si no está disponible, se activa la sustitución o delegación prevista.
- El responsable end-to-end debe disponer de autoridad operativa suficiente para asegurar la continuidad: puede asumir temporalmente una tarea si está autorizado y capacitado, o asignarla a otra persona autorizada, dentro de los límites establecidos.
- Los bloqueos se revisan y resuelven en el nivel operativo correspondiente. El escalado funcional para desbloquear o coordinar una actuación no implica por sí mismo un escalado jerárquico.
- La intervención de una instancia jerárquica superior queda reservada a causas extraordinarias que excedan la capacidad o autoridad operativa disponible, o a circunstancias de especial gravedad.

Antes del uso real deben definirse las responsabilidades, sustituciones, delegaciones y límites de autoridad, así como qué circunstancias justifican la excepción. Esta es una regla funcional propuesta para el caso ficticio, no un procedimiento organizativo aprobado ni validación empírica.

### Contingencia ante indisponibilidad simultánea del responsable y de su cobertura

Si la persona responsable de una función crítica y la cobertura alternativa prevista están ambas indisponibles, se considera una **situación de contingencia**, no una incidencia ordinaria de cobertura.

- Debe activarse un procedimiento de contingencia predefinido, con un segundo nivel de respuesta y responsables o instancias competentes previamente identificados y autorizados.
- Si tampoco existe capacidad de respuesta en ese nivel, se activa la vía de contingencia que determine la autoridad competente, preservando la atención necesaria y sin asignar funciones a personas no autorizadas o no capacitadas.
- La activación, las decisiones, las responsabilidades asumidas y el seguimiento deben quedar registrados.
- No se presume que la mera escalación garantice la resolución ni que exista autoridad ilimitada para asumir tareas.

Antes del uso real deben definirse los niveles, responsables, competencias, límites y vías de activación de la contingencia, de acuerdo con las autoridades organizativas y clínicas correspondientes. Esta regla es una propuesta funcional para el caso ficticio, no un procedimiento aprobado ni validación empírica.

### Recuperación controlada tras una contingencia en el proceso evaluado

Una vez restablecidas las condiciones habituales, el retorno a la operativa ordinaria del **proceso de concertación y gestión de citas incluido en esta evaluación** debe realizarse de forma controlada, no automática.

- Confirmar que se han recuperado las condiciones necesarias para gestionar las solicitudes y citas afectadas.
- Revisar las solicitudes pendientes o bloqueadas durante la contingencia.
- Transferir formalmente las responsabilidades y la información a los responsables ordinarios.
- Comprobar que ninguna solicitud o paciente afectado queda sin seguimiento dentro del proceso evaluado.
- Registrar la recuperación y el cierre de la contingencia.

Este criterio no extiende el alcance de A3 a la continuidad general de la clínica ni a otros procesos clínicos u organizativos ajenos al proceso evaluado. La recuperación de la operativa tampoco significa que todas las solicitudes afectadas estén ya resueltas.

### Identificación y trazabilidad de solicitudes afectadas por la contingencia

Toda contingencia debe dejar identificadas las solicitudes de cita afectadas, de modo que puedan recuperarse sin pérdida de trazabilidad. El registro debe permitir conocer:

- qué solicitudes resultaron afectadas;
- en qué etapa del proceso se encontraban;
- qué actuaciones quedaron pendientes;
- quién debe retomarlas;
- qué prioridad o necesidad de seguimiento les corresponde, conforme a criterios autorizados;
- qué actuaciones se realizaron para recuperar su tramitación.

### Verificación de la reincorporación efectiva de las solicitudes al flujo

Antes de considerar recuperada la operativa del proceso evaluado, debe comprobarse, para cada solicitud afectada, que:

- tiene asignado un responsable efectivo;
- está identificada la siguiente actuación pendiente;
- conserva la información y el historial necesarios;
- mantiene las condiciones de prioridad y seguimiento que le correspondan, conforme a criterios autorizados;
- ha retomado efectivamente su tramitación o, si continúa bloqueada, tiene documentados el motivo, el responsable y la respuesta prevista.

La recuperación de la contingencia y la resolución de las solicitudes son resultados distintos. Una solicitud puede seguir pendiente después de recuperada la operativa, pero no debe quedar sin responsable ni seguimiento.

### Gestión activa de bloqueos con responsable asignado

La asignación de un responsable y de una siguiente actuación no demuestra por sí sola que una solicitud esté avanzando. Cuando la actuación dependa de información o respuesta de otro rol y el bloqueo persista, el responsable end-to-end debe gestionar activamente su desbloqueo:

- Identificar y registrar qué información o respuesta falta, qué rol debe proporcionarla y desde cuándo existe el bloqueo.
- Requerir la actuación al rol responsable y dejar constancia de la solicitud y su seguimiento.
- Controlar el cumplimiento del plazo previamente acordado para esa actuación.
- Si no se recibe respuesta o no se desbloquea la solicitud dentro del plazo, activar la vía de escalado correspondiente o una alternativa previamente autorizada.
- Registrar las actuaciones, su resultado, el responsable y el siguiente paso.
- Mantener abierta la solicitud hasta que se cumplan sus condiciones de resolución; la gestión administrativa del bloqueo no equivale a resolverla.

Los plazos, niveles de escalado, alternativas y facultades del responsable end-to-end deben estar definidos y autorizados. No se fijan aquí valores ni competencias nuevas. Esta es una regla funcional para el caso ficticio, no un procedimiento aprobado ni validación empírica.

### Relaciones y posibles puntos de bloqueo

- La información incompleta puede provocar devoluciones y trabajo repetido.
- La falta de visibilidad compartida puede retrasar el seguimiento de solicitudes bloqueadas.
- La capacidad disponible puede limitar la asignación aunque el proceso administrativo sea eficiente.
- Las reglas clínicas de prioridad condicionan el orden de atención y no deben sustituirse por criterios de conveniencia administrativa.
- Mejorar el tiempo medio global podría ocultar un empeoramiento para pacientes prioritarios; por ello se requiere seguimiento segmentado.

### Fronteras del modelo

El modelo cubre la asignación de citas, no la atención clínica posterior ni la eficacia de los tratamientos. Se ampliaría si los datos reales revelaran que las principales causas se encuentran fuera de esa frontera.

### Revisión del VSM

El modelo debe evolucionar al aprender. No se presenta como inventario completo de relaciones ni como mapa causal demostrado.

## 7. DESIGN — A4 Value Hypothesis & Options Record

**ID:** CLINIC-001-A4  
**Estado:** alternativas de diseño ilustrativas

### Hipótesis de valor principal

**H-V1:** si el equipo revisa de forma estructurada las solicitudes pendientes y escala excepciones según las reglas vigentes, podría reducirse el tiempo que solicitudes bloqueadas permanecen sin seguimiento, sin perjudicar a pacientes prioritarios y con una carga de trabajo aceptable.

La hipótesis es falsable: si no se reduce la demora, empeora el acceso prioritario o la carga resulta inaceptable, no debe considerarse exitosa.

### Opciones consideradas

| Opción | Descripción | Beneficio esperado | Riesgo o límite |
|---|---|---|---|
| O0 — Mantener y medir | No cambiar el proceso; mejorar la medición | Establece una referencia | No resuelve bloqueos si existen |
| O1 — Revisión diaria de pendientes | Revisión breve, responsable asignado y escalado de excepciones | Aumenta visibilidad y seguimiento | Puede añadir carga administrativa |
| O2 — Mejorar completitud en la entrada | Lista de comprobación para reducir solicitudes incompletas | Menos devoluciones y retrabajo | Puede alargar la recepción inicial |
| O3 — Aumentar capacidad | Ajustar recursos o franjas disponibles | Puede reducir colas por falta de capacidad | Requiere recursos y evidencia de necesidad |
| O4 — Rediseño integral | Rediseñar el flujo de extremo a extremo | Potencial de mejora amplia | Mayor coste, complejidad y riesgo |

### Criterios de comparación

- Acceso oportuno.
- Protección del acceso prioritario.
- Calidad y seguridad.
- Carga de trabajo.
- Coste y reversibilidad.
- Facilidad de evaluación.
- Capacidad de aprender antes de escalar.

No se asignan puntuaciones numéricas porque no hay datos reales ni preferencias acordadas. Cualquier ponderación debería acordarse con las partes afectadas y registrarse explícitamente.

## 8. DESIGN — A5 Evidence Record

**ID:** CLINIC-001-A5  
**Estado:** conjunto de evidencia completamente simulado  
**Dataset ficticio:** `SIM-CLINIC-001-DATA-v0.1`  
**Ventana de referencia simulada:** cuatro semanas antes y cuatro semanas después de la intervención hipotética.  
**Registro de ejecución vinculado:** `SIM-CLINIC-001-EXEC-v0.1` (véase A7).

### Conjunto ficticio para ilustrar una comparación

Supóngase, solo a efectos didácticos, que se revisan 200 solicitudes antes de una intervención y 200 después. Se supone que la definición de “más allá del plazo interno de referencia” se mantiene idéntica en ambos periodos.

| Indicador | Antes [SIMULADO] | Después [SIMULADO] |
|---|---:|---:|
| Solicitudes revisadas | 200 | 200 |
| Pendientes más allá del plazo interno | 56 (28 %) | 36 (18 %) |
| Solicitudes prioritarias dentro de plazo | 96 % | 96 % |
| Solicitudes devueltas por información incompleta | 30 (15 %) | 24 (12 %) |
| Percepción del personal de aumento de carga | No medida con escala comparable | Se reporta aumento cualitativo |

### Definiciones operativas simuladas

Estas definiciones se crean únicamente para que el ejemplo sea calculable; no son definiciones clínicas recomendadas.

- **Unidad de análisis:** una solicitud de cita recibida por el ámbito ficticio durante cada ventana de cuatro semanas.
- **Selección:** se supone que se incluyen todas las solicitudes recibidas en la ventana y con un estado registrable al cierre de esa ventana. No se representa cómo se tratarían en la realidad solicitudes duplicadas, reabiertas o aún sin resolución; esas reglas tendrían que acordarse antes de un piloto real.
- **Pendiente más allá del plazo interno:** numerador = solicitudes cuyo tiempo entre recepción y asignación supera el plazo de referencia ficticio vigente; denominador = las 200 solicitudes incluidas en la ventana. Antes: 56/200 = 28 %. Después: 36/200 = 18 %.
- **Solicitud prioritaria dentro de plazo:** numerador = solicitudes clasificadas como prioritarias según las reglas ficticias vigentes y asignadas dentro del plazo correspondiente; denominador = todas las solicitudes prioritarias incluidas en la ventana. Se supone, solo para ilustrar el cálculo, que hubo 50 solicitudes prioritarias en cada ventana: antes 48/50 = 96 % y después 48/50 = 96 %.
- **Devolución por información incompleta:** numerador = solicitudes devueltas al menos una vez para completar información; denominador = las 200 solicitudes incluidas en la ventana. Antes: 30/200 = 15 %. Después: 24/200 = 12 %.
- **Carga administrativa:** en el escenario no existe una escala cuantitativa comparable. El reporte cualitativo posterior es una señal de riesgo, no una medida de magnitud.
- **Datos ausentes:** para simplificar el ejemplo se supone que no hay datos ausentes en los campos necesarios para los indicadores. En una aplicación real se informarían los faltantes y se definiría cómo afectan a cada denominador.

### Registro de calidad

- **Fuente:** conjunto inventado para este documento, `SIM-CLINIC-001-DATA-v0.1`.
- **Método de obtención:** no se han extraído registros reales; los valores se han construido para ilustrar el registro y los cálculos.
- **Selección y ventana:** se supone un censo de 200 solicitudes por ventana de cuatro semanas, una ventana anterior y otra posterior. No se modelan estacionalidad, cambios de demanda ni composición por tipo de cita.
- **Comparabilidad:** se supone que periodos, definiciones y composición son comparables; el supuesto no está verificado.
- **Datos ausentes:** se supone que no hay faltantes en los campos requeridos; esta simplificación no representa un resultado observado.
- **Sesgos posibles:** variación en demanda, mezcla de tipos de cita, disponibilidad de profesionales, estacionalidad, cambios en el registro y otros factores externos.
- **Salvaguarda:** el porcentaje agregado no sustituye el análisis por prioridad y tipo de paciente.
- **Límite:** no se puede inferir que la intervención causó el cambio ni descartar explicaciones alternativas.

### Clasificación epistemológica

- La reducción del 28 % al 18 % es una **diferencia descriptiva simulada**.
- Que la revisión diaria haya contribuido a esa diferencia sería una **inferencia**, no un hecho establecido.
- Que el efecto se reproduzca en una clínica real sigue siendo una **hipótesis**.

A5 es un registro transversal de evidencia y se usa especialmente en DESIGN y DECIDE; no constituye una fase adicional del ciclo.

## 9. DECIDE — A6 Value Decision Record

**ID:** CLINIC-001-A6  
**Estado:** decisión ilustrativa; no autorizada para ejecución real

### Decisión del escenario

Seleccionar **O1 — Revisión diaria de pendientes**, como opción preferida para una posible prueba limitada, reversible y supervisada. La decisión es una **selección de diseño dentro del escenario ficticio**, no una autorización de ejecución. Su puesta en marcha queda condicionada a cerrar los criterios previos pendientes y obtener autorización formal.

### Registro de decisión y autorización (simulado)

- **ID de decisión:** `SIM-CLINIC-001-DEC-v0.1`.
- **Decisor en el escenario:** rol ficticio de responsable de operaciones, sujeto a confirmación de la autoridad real.
- **Fecha:** no especificada en el escenario; debe registrarse antes de una prueba.
- **Estado de la decisión:** opción seleccionada para preparar una prueba; autorización de ejecución **NO CONCEDIDA / PENDIENTE**.
- **Condiciones de validez:** aprobación de criterios previos; confirmación de capacidad; validación de salvaguardas clínicas y privacidad; designación de responsables; definición de parada.
- **Trazabilidad:** decisión basada en la intención A1, las opciones A4 y el registro simulado A5; las condiciones se trasladan a A7.

Este bloque distingue la decisión ilustrativa de seleccionar una opción de la autorización formal para ejecutarla. No representa una firma ni una aprobación real.

### Justificación

- Aborda una hipótesis modificable sin afirmar que sea la causa raíz.
- Puede probarse a pequeña escala.
- Permite medir tanto el acceso como los posibles efectos adversos en prioridad y carga de trabajo.
- Es más reversible que un rediseño integral o una ampliación de capacidad.
- Produce información útil para decidir si continuar, adaptar o detener la intervención.

### Condiciones previas

1. Nombrar a la persona responsable de la prueba.
2. Confirmar los plazos internos y la definición de cada indicador.
3. Acordar cómo se protegerán las prioridades clínicas.
4. Estimar el tiempo requerido y comprobar la capacidad del equipo.
5. Establecer un mecanismo de escalado y parada.
6. Validar acceso, privacidad y calidad de los datos.
7. Acordar los criterios de decisión con las personas responsables.

### Criterios previos de decisión — registro ilustrativo

Para evitar elegir retrospectivamente los criterios que mejor encajan con el resultado, el escenario debería fijarlos antes de iniciar la prueba. En este caso ficticio **no se han proporcionado umbrales cuantitativos aprobados**, por lo que quedan explícitamente pendientes y no se inventan como si fueran acuerdos de la clínica.

| Criterio previo | Regla que debe acordarse antes de empezar | Estado en este caso |
|---|---|---|
| Mejora de acceso | Definir la reducción mínima relevante de solicitudes fuera de plazo y la comparación que se utilizará | PENDIENTE; no hay umbral aprobado |
| Protección del acceso prioritario | Definir qué deterioro requiere detener o revisar de inmediato, respetando las reglas clínicas existentes | PENDIENTE; debe acordarlo el referente clínico autorizado |
| Carga de trabajo | Definir cómo medir tiempo/carga y cuál es el máximo tolerable | PENDIENTE; la percepción cualitativa no basta |
| Calidad de datos | Definir completitud mínima, tratamiento de faltantes y condiciones que invalidan la comparación | PENDIENTE |
| Duración y revisión | Confirmar ventana, revisiones intermedias y responsable de parada | Propuesta ficticia de cuatro semanas; requiere autorización |

### Reglas de decisión propuestas

- **Continuar o ampliar:** solo si se cumplen los criterios previos acordados, se mantienen las salvaguardas y la carga es aceptable.
- **Adaptar:** mejora parcial con problemas operativos corregibles y sin deterioro de salvaguardas.
- **Detener y revisar:** deterioro del acceso prioritario, riesgo asistencial, carga superior al límite acordado o datos insuficientes para evaluar.
- **No concluir:** si los datos no son comparables o cambian las condiciones externas de forma importante.

No se fijan umbrales clínicos universales ni se presentan criterios pendientes como acuerdos reales. En una organización real, los criterios se documentarían y aprobarían antes de iniciar.

## 10. ACT — A7 Value Blueprint & Delivery Plan

**ID:** CLINIC-001-A7  
**Estado:** plan hipotético, sujeto a autorización

### Diseño de la prueba

- **Duración de referencia:** cuatro semanas de operación, precedidas por preparación y medición de línea base.
- **Ámbito inicial:** un equipo o segmento acotado del proceso, elegido por responsables reales.
- **Rutina:** reunión breve diaria para revisar solicitudes pendientes, identificar bloqueos, asignar responsable de seguimiento y escalar excepciones según las reglas existentes.
- **Registro:** cada solicitud conserva estado, fecha, motivo de bloqueo y acción siguiente en el sistema autorizado.
- **No cambiar:** criterios clínicos de prioridad, decisiones clínicas ni reglas de seguridad.
- **Supervisión:** revisión periódica de indicadores y posibilidad de detener la prueba.

### Responsabilidades propuestas

| Rol | Responsabilidad |
|---|---|
| Patrocinador | Autorizar alcance, recursos y criterios de parada |
| Responsable del proceso | Coordinar la prueba y retirar bloqueos operativos |
| Recepción/administración | Registrar estados y ejecutar el seguimiento |
| Referente clínico | Vigilar que las reglas de prioridad se respeten |
| Responsable de evaluación | Revisar definiciones, calidad y resultados |
| Equipo participante | Comunicar efectos no previstos y carga de trabajo |

Los roles son funciones propuestas, no personas identificadas.

### Plan de trabajo hipotético

1. **Preparación:** validar definiciones, responsables, datos, salvaguardas y línea base.
2. **Inicio controlado:** explicar el procedimiento, probar el registro y corregir ambigüedades.
3. **Operación:** realizar revisión diaria y registrar bloqueos, acciones y excepciones.
4. **Seguimiento:** revisar acceso, prioridad, calidad y carga de trabajo.
5. **Cierre:** comparar resultados, documentar desviaciones y decidir si detener, adaptar o estudiar una extensión.

### Registro de ejecución simulada — `SIM-CLINIC-001-EXEC-v0.1`

**Aviso:** el registro siguiente es una narración ficticia creada para conectar el plan con el dataset simulado. No demuestra que una clínica haya ejecutado estas actividades.

| Momento relativo | Actividad supuestamente realizada | Registro ficticio / desviación |
|---|---|---|
| Antes de semana 1 | Revisión de definiciones, roles y salvaguardas | Se supone que las condiciones previas se aceptan en el escenario; no equivale a una autorización real. |
| Semana 1 | Inicio del repaso diario de pendientes | Se supone que el equipo utiliza el registro de estado y motivo de bloqueo. |
| Semanas 2–3 | Revisión diaria y escalado según reglas existentes | Se supone que no se cambian las reglas clínicas. No se inventan recuentos de reuniones ni de excepciones. |
| Semana 4 | Cierre de la ventana posterior y revisión de indicadores | Se genera el dataset ficticio `SIM-CLINIC-001-DATA-v0.1` con los valores ilustrativos de A5. |
| Cierre | Revisión de efectos no previstos | Se registra un reporte cualitativo ficticio de aumento de carga administrativa; su magnitud no se cuantifica. |

**Desviaciones y límites:** el ejemplo no aporta un registro granular por solicitud, marcas temporales, actas, incidencias ni datos de carga comparables. Por tanto, el registro conecta documentalmente A6–A7–A5–A8, pero no representa evidencia auditable de una ejecución real. Si estos datos fueran reales, deberían enlazarse registros fuente autorizados y verificables.

### Riesgos y mitigaciones

- **Sobrecarga:** limitar la duración de la reunión, medir tiempo invertido y parar o rediseñar si resulta excesivo.
- **Desplazamiento de prioridades:** mantener reglas clínicas y revisar por separado los resultados prioritarios.
- **Datos incompletos:** definir campos mínimos y registrar datos ausentes.
- **Mejora aparente por cambios externos:** documentar demanda, capacidad y otros cambios simultáneos.
- **Uso indebido de información:** emplear solo sistemas autorizados y datos mínimos necesarios.

### Criterios de aceptación del plan

El plan está preparado para una decisión de autorización cuando alcance, responsables, indicadores, salvaguardas, fuentes de datos, calendario y criterios de parada estén acordados. La existencia de este documento no autoriza por sí misma una prueba real.

## 11. LEARN — A8 Value Learning Record

**ID:** CLINIC-001-A8  
**Estado:** resultado de ejemplo simulado  
**Dataset evaluado:** `SIM-CLINIC-001-DATA-v0.1`  
**Registro de ejecución relacionado:** `SIM-CLINIC-001-EXEC-v0.1`

### Resultados ilustrativos

Bajo los supuestos inventados de A5:

- Las solicitudes pendientes más allá del plazo de referencia pasan del 28 % al 18 %.
- El indicador agregado de solicitudes prioritarias dentro de plazo permanece en el 96 %.
- Las devoluciones por información incompleta pasan del 15 % al 12 %.
- El personal comunica un aumento de carga administrativa, sin una medida cuantitativa comparable.

### Interpretación prudente

**[INFERENCIA]** En este escenario, los datos simulados serían compatibles con una mejora del seguimiento de pendientes, pero también revelan un coste operativo potencial. No prueban que la revisión diaria sea la causa de la mejora ni que el balance global sea positivo. Los resultados proceden exclusivamente del dataset ficticio `SIM-CLINIC-001-DATA-v0.1`; la secuencia de actividades supuestas está descrita en `SIM-CLINIC-001-EXEC-v0.1`.

### Aprendizajes documentados

1. No basta con medir el tiempo agregado: debe vigilarse por separado el acceso prioritario.
2. La mejora de un indicador puede coexistir con un coste de carga de trabajo.
3. El registro de causas de bloqueo ayudaría a decidir si el siguiente ciclo debe centrarse en completitud, coordinación o capacidad.
4. Las definiciones de indicadores y la comparabilidad de periodos son requisitos previos, no detalles posteriores.
5. La decisión de escalar exige evidencia real y participación de las personas afectadas.

### Separación entre el Sprint y los resultados operativos

Los porcentajes y el reporte de carga descritos en este A8 pertenecen exclusivamente al escenario de prueba operativa posterior de cuatro semanas y al dataset ficticio `SIM-CLINIC-001-DATA-v0.1`. **No son resultados producidos durante el Value Discovery Sprint de cinco días.**

El A8 que se cerraría al final del Sprint debe limitarse al aprendizaje de descubrimiento: qué se sabe y qué no, qué hipótesis siguen abiertas, si A3/A4 necesitan revisión, qué datos faltan, qué decisión se tomó y qué condiciones hacen falta antes de cualquier prueba. En este caso, como no hay participantes reales, ese aprendizaje del Sprint también es una reconstrucción documental ficticia.

### Siguiente decisión ilustrativa

No escalar automáticamente. Si se tratara de una prueba real, revisar primero la carga de trabajo, comprobar la calidad y comparabilidad de los datos y analizar resultados segmentados. Después, decidir entre adaptar el protocolo, extender la observación o estudiar otra hipótesis.

### Límites del aprendizaje

- No se dispone de observaciones reales.
- No hay grupo de comparación ni diseño causal.
- No se ha evaluado el impacto en todos los tipos de pacientes.
- No se han verificado costes, esfuerzo, sostenibilidad ni reproducibilidad.
- No se ha demostrado la eficacia del método VALUE ni de TGCV.

## 12. Cadena de trazabilidad A1–A8

| Artefacto | Pregunta que responde | Entrada principal | Salida conectada |
|---|---|---|---|
| A1 — Value Intent | ¿Qué valor buscamos y quién decide? | Contexto y propósito inicial | Criterios de oportunidad para A2 |
| A2 — Value Opportunity Brief | ¿Qué problema y preguntas vamos a investigar? | A1 y síntomas iniciales | Preguntas y límites para A3 |
| A3 — Value System Model | ¿Qué elementos y relaciones intervienen? | A2 y conocimiento del proceso | Puntos de intervención para A4 |
| A4 — Hypothesis & Options | ¿Qué explicaciones y opciones contrastamos? | A3 y criterios de A1 | Opciones que necesitan evidencia en A5 |
| A5 — Evidence Record | ¿Qué está observado, supuesto o todavía incierto? | Fuentes y métodos registrados | Base de decisión para A6; transversal |
| A6 — Value Decision Record | ¿Qué elegimos y por qué? | A1, A4 y A5 | Autorización/condiciones para A7 |
| A7 — Blueprint & Delivery Plan | ¿Cómo se probaría de forma controlada? | Decisión A6 y salvaguardas | Ejecución autorizada y registros para A8 |
| A8 — Value Learning Record | ¿Qué ocurrió y qué aprendimos? | Resultados de A7 y evidencia A5 | Revisión de A1–A4 para el siguiente ciclo |

La trazabilidad es bidireccional: el aprendizaje puede modificar el modelo del sistema, las hipótesis, los criterios de valor o incluso la definición de la oportunidad. No implica que los artefactos tengan que quedar cerrados para siempre.

## 13. Recorrido del Value Discovery Sprint

El caso podría trabajarse en un Sprint de referencia de cinco días laborables distribuidos en una o dos semanas. Esta duración es una hipótesis de diseño del servicio, no un estándar empíricamente validado.

- **Día 1 — ALIGN + SENSE:** A1 y borrador de A2; propósito, grupos afectados y preguntas.
- **Día 2 — CONNECT:** primer A3; flujo, actores, dependencias y vacíos de información.
- **Día 3 — DESIGN:** A4 y plan de evidencia A5; hipótesis y opciones comparables.
- **Día 4 — DECIDE:** A6; decisión sobre una prueba limitada o investigación adicional.
- **Día 5 — ACT + LEARN inicial:** A7 preparado y A8 con aprendizaje del Sprint, riesgos y siguientes pasos.

El Sprint puede concluir con una decisión de investigar más; no obliga a ejecutar una solución. La prueba operativa de cuatro semanas descrita en A7 es posterior y separada del Sprint.

## 14. Revisión crítica del caso

### Lo que el ejercicio permite comprobar

- Los ocho artefactos se pueden conectar en una cadena documental.
- Las hipótesis no se presentan automáticamente como causas.
- La evidencia, la inferencia, la decisión y el resultado están diferenciados.
- Las salvaguardas y los efectos adversos forman parte de la decisión.
- El aprendizaje puede reabrir decisiones anteriores.
- El Sprint de descubrimiento no se confunde con una prueba completa ni con validación empírica.

### Lo que el ejercicio no demuestra

- Que el ciclo sea fácil de utilizar por equipos reales.
- Que cinco días sean suficientes para un Sprint.
- Que los artefactos estén completos para todos los sectores.
- Que la opción elegida produzca valor.
- Que las métricas sean adecuadas para una clínica real.
- Que exista una relación causal entre la intervención y los resultados simulados.
- Que VALUE o TGCV hayan sido validados científicamente.

### Preguntas para revisión del estándar

1. ¿Se distinguen suficientemente A1 (intención) y A2 (oportunidad)?
2. ¿A3 representa las relaciones necesarias sin convertirse en un modelo excesivamente pesado?
3. ¿A5 permite registrar evidencia contradictoria, negativa o insuficiente?
4. ¿A6 hace visibles los criterios y condiciones que justifican la decisión?
5. ¿A7 separa autorización, planificación y ejecución real?
6. ¿A8 documenta resultados adversos y límites de atribución, además de mejoras?
7. ¿El recorrido de cinco días produce artefactos útiles sin incentivar conclusiones prematuras?

## 15. Estado final del caso

**Estado documental:** recorrido A1–A8 desarrollado para el escenario ficticio, con dataset y registro de ejecución simulada identificados.  
**Estado metodológico:** ejemplo para revisión de coherencia y preparación de un piloto; no es una validación práctica.  
**Estado de ejecución:** no se ha ejecutado ninguna intervención real.  
**Estado de evidencia:** todos los resultados numéricos son simulados.  
**Siguiente paso recomendado:** revisar el caso como prueba de cobertura del estándar y registrar defectos o ambigüedades antes de diseñar una prueba con datos reales autorizados.

---

### SR-047 — Detección de solicitudes sin seguimiento durante la operativa ordinaria

Se propone un mecanismo de control para detectar solicitudes que carecen de responsable actual o de siguiente actuación definida; permanecen sin actualización durante un periodo que requiere revisión; superan un plazo de respuesta o resolución acordado; o figuran activas sin progreso ni justificación documentada del bloqueo. El responsable end-to-end revisa estas situaciones y activa las actuaciones o escalados previstos. Los periodos y plazos deben estar previamente acordados y autorizados: no se inventan umbrales ni se sustituyen criterios clínicos.

Esta regla aborda la detección durante la operativa ordinaria y complementa, sin confundirse con ella, la recuperación de solicitudes afectadas por contingencias (SR-045 y SR-046). Es una propuesta funcional del caso ficticio, no un procedimiento aprobado ni validación empírica.

### SR-048 — Detección combinada por eventos y revisión periódica

Para detectar las situaciones contempladas en SR-047, se acuerda combinar dos mecanismos complementarios:

- **Detección por eventos:** identificar cuando una solicitud queda sin responsable o sin siguiente actuación, o cuando se produce el incumplimiento de un plazo acordado.
- **Revisión periódica:** identificar solicitudes que continúan activas, pero acumulan un periodo que requiere revisión sin actualización o progreso.

La revisión periódica actúa también como salvaguarda ante posibles fallos del mecanismo de detección por eventos. La periodicidad y los plazos deberán definirse y autorizarse antes de cualquier uso real; no se presuponen valores ni umbrales.

Criterio funcional para el caso ficticio; no constituye un procedimiento aprobado ni validación empírica.

### SR-049 — Registro de incidencias de seguimiento vinculadas a la solicitud

Cuando la detección por eventos o la revisión periódica identifique una solicitud que requiere seguimiento conforme a SR-047 y SR-048, se propone generar una incidencia de seguimiento vinculada a la solicitud original. El registro incluirá, como mínimo, la fecha de detección, el motivo, el responsable de revisar la incidencia y la actuación requerida.

La incidencia no sustituye ni cierra la solicitud original: permite hacer trazable la detección y gestionar su revisión. Deben definirse antes del uso real el mecanismo de registro, las reglas de asignación y actualización y la autoridad para determinar la actuación correspondiente. Criterio funcional para el caso ficticio; no constituye un procedimiento aprobado ni validación empírica.

### SR-050 — Ciclo de vida y resolución de la incidencia de seguimiento

Cada incidencia de seguimiento tendrá un ciclo propio que permita conocer su estado: **abierta**, **asignada**, **en revisión**, **con actuación pendiente** y **resuelta**. Al resolverla se dejará constancia de la actuación realizada y de la situación en que queda la solicitud original. La resolución de la incidencia no implica el cierre automático de la solicitud.

Antes del uso real deberán definirse las condiciones de entrada y salida de cada estado, los responsables de las transiciones y la evidencia mínima de resolución. Criterio funcional para el caso ficticio; no constituye un procedimiento aprobado ni validación empírica.

### SR-051 — Incidencias que no se resuelven o que reinciden

Cuando una incidencia de seguimiento permanezca sin actuación, supere un plazo de revisión o actuación previamente acordado, o el mismo problema vuelva a producirse después de haberse resuelto una incidencia anterior, se activará una revisión por el responsable end-to-end y, cuando corresponda, el escalado previsto.

La revisión deberá dejar registrados, como mínimo, el motivo por el que la incidencia no se ha resuelto o la causa/motivo conocido de la reincidencia, la evaluación realizada, la siguiente actuación prevista y el responsable de llevarla a cabo. Cuando exista un plazo aplicable, se registrará también el plazo acordado para esa siguiente actuación. No se presumirán plazos, responsables nominales ni niveles de escalado que todavía no hayan sido definidos y autorizados.

En caso de reincidencia, se conservará la incidencia anterior como antecedente y se registrará una nueva incidencia vinculada a ella y a la solicitud original. Esto permite distinguir una incidencia persistente de una nueva ocurrencia y mantener la trazabilidad de las actuaciones previas. La revisión o el escalado no resuelven ni cierran automáticamente la incidencia ni la solicitud original: la incidencia seguirá su ciclo conforme a SR-050 hasta que se cumplan sus condiciones de resolución.

Criterio funcional para el caso ficticio; no constituye un procedimiento aprobado ni validación empírica.

## Historial de cambios

- **v0.1:** primera reconstrucción integral del caso ficticio; incluye A1–A8, recorrido del Sprint, trazabilidad, resultados simulados, límites y preguntas de revisión.
- **v0.2:** añade identificadores de dataset y ejecución simulados, definiciones operativas y denominadores explícitos, supuestos de selección/ventanas y separación narrativa entre plan y ejecución ficticia. No añade datos reales ni validación empírica.
- **v0.3:** documenta criterios previos de decisión como pendientes cuando no hay umbrales aprobados; separa selección de opción y autorización de ejecución; distingue explícitamente el aprendizaje del Sprint de los resultados de la prueba operativa posterior. No añade datos reales ni validación empírica.


### SR-052 — Reproducibilidad escalonada de la autoevaluación

- **Aprobación del usuario:** sí.
- **Diseño acordado:** evaluar la reproducibilidad en etapas, sin presentar una modalidad como sustituta de otra:
  1. **Repetición intraevaluador:** la misma persona evaluadora volverá a aplicar la revisión al mismo caso en un momento separado. En la segunda pasada no consultará los resultados ni las anotaciones de la primera antes de completar y dejar registrada su evaluación independiente. Después se compararán interpretaciones, decisiones, omisiones, ambigüedades y diferencias detectadas.
  2. **Revisión auxiliar asistida por IA:** una instancia/modelo independiente revisará el caso y la documentación disponible sin recibir las conclusiones de la autoevaluación previa. Su resultado se registrará por separado y podrá ayudar a detectar omisiones o ambigüedades; no equivale a una segunda persona evaluadora ni acredita reproducibilidad interevaluador.
  3. **Reproducibilidad interevaluador humana:** queda diferida hasta que la investigación se abra a la comunidad a través de la web y puedan participar evaluadores externos independientes.
- **Registro y comparación:** conservar por separado las versiones de cada pasada, fecha, material consultado, observaciones y discrepancias; documentar posteriormente la comparación sin sobrescribir los registros originales.
- **Límites de interpretación:** las dos primeras etapas permiten examinar consistencia intraevaluador y detectar ambigüedades, pero no demuestran reproducibilidad interevaluador, validez empírica ni eficacia del método VALUE o de TGCV.
- **Condición de apertura comunitaria:** el protocolo de evaluación externa, selección/independencia de evaluadores y tratamiento de discrepancias deberá definirse antes de iniciar esa fase; no se presume ahora un número de evaluadores ni un procedimiento aún no acordado.
- **Estado:** aceptado por el usuario; incorporado documentalmente en la rama del PR #114. La repetición intraevaluador y la revisión auxiliar por IA quedan como actividades pendientes, no como pruebas ya realizadas.
