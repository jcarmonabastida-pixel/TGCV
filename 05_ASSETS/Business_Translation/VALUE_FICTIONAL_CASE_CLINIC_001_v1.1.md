# VALUE — Caso ficticio integral: mejora del acceso a citas en una clínica

**Identificador:** VALUE-CASE-CLINIC-001  
**Versión:** 1.1  
**Estado:** CASO FICTICIO CONSOLIDADO PARA REVISIÓN DOCUMENTAL — no validado en una organización real  
**Precedencia:** esta versión consolidada sustituye como referencia de trabajo al snapshot anterior `VALUE_FICTIONAL_CASE_CLINIC_001_v0.2.md` (presente en `main`); conserva y amplía la revisión A1–A8 y las correcciones registradas.  
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
**Estado:** modelo conceptual provisional, consolidado tras auditoría de proporcionalidad (2026-10-30)

### Propósito y límites del sistema

Representar el sistema administrativo de gestión de citas programadas de la clínica ficticia, desde la recepción de una solicitud hasta su asignación, comunicación, seguimiento y resolución. El modelo no describe un procedimiento real verificado. Las urgencias, el diagnóstico, el tratamiento y las decisiones clínicas quedan fuera del alcance administrativo; se representan únicamente las interfaces y dependencias clínicas que condicionan el proceso de citas.

### Actores y funciones

| Actor/elemento | Función sistémica representada | Incertidumbre o dependencia |
|---|---|---|
| Paciente/cuidador | Presenta la solicitud, aporta información, recibe comunicaciones y confirma o rechaza propuestas | Necesidades, disponibilidad y barreras diversas |
| Recepción | Recibe, clasifica y registra solicitudes | Criterios de clasificación y calidad de la entrada |
| Administración de citas | Revisa solicitudes, gestiona asignación y actualiza el estado | Capacidad, carga, reglas vigentes y competencias |
| Coordinación de citas | Coordina el flujo, supervisión y resolución de bloqueos | Autoridad y alcance formal pendientes de confirmar |
| Profesional sanitario | Aporta criterio clínico cuando la solicitud requiere valoración o priorización clínica | Disponibilidad y procedimiento clínico aplicable, fuera del alcance de este modelo |
| Sistema de registro/gestión | Conserva solicitudes, estados, fechas, reglas e historial disponible | Funciones reales, permisos, integridad y trazabilidad por comprobar |
| Dirección de operaciones | Interviene en decisiones de recursos y cambios operativos conforme a autoridad definida | Restricciones y competencias concretas pendientes de confirmar |

### Identificadores de elementos y relaciones del modelo

Los identificadores siguientes hacen explícita la estructura mínima del modelo y permiten enlazar A3 con A4 y A5. Son elementos y relaciones propuestos para el caso ficticio, no un mapa organizativo verificado.

| ID | Elemento | Tipo | Estado epistemológico | Base documental / validación pendiente |
|---|---|---|---|---|
| E01 | Paciente/cuidador | Actor / grupo afectado | Propuesto en el caso | Alcance y necesidades descritos en A1/A2; contrastar con participantes reales |
| E02 | Recepción | Actor / función | Propuesto en el caso | Flujo conceptual del caso; validar función y límites |
| E03 | Administración de citas | Actor / función | Propuesto en el caso | Flujo conceptual del caso; validar función, capacidad y competencias |
| E04 | Coordinación de citas | Actor / función | Necesidad funcional inferida | Confirmar existencia, autoridad y responsabilidad end-to-end |
| E05 | Profesional sanitario | Actor / interfaz clínica | Dependencia de alcance | Confirmar puntos de intervención clínica; decisiones clínicas fuera del modelo administrativo |
| E06 | Sistema de registro/gestión | Recurso / soporte de información | Supuesto de trabajo | Comprobar producto, funciones, permisos, registros e historial reales |
| E07 | Dirección de operaciones | Actor / función de gobernanza | Propuesto en el caso | Confirmar autoridad y responsabilidad sobre recursos y cambios |

| ID | Relación propuesta | Elementos conectados | Significado | Estado epistemológico |
|---|---|---|---|---|
| R01 | Presentación de solicitud | E01 → E02 | La persona solicitante inicia el flujo mediante recepción | Supuesto del flujo; validar canales reales |
| R02 | Registro y traspaso | E02 → E06 → E03 | La solicitud se registra y queda disponible para su revisión | Supuesto del flujo; validar sistemas y traspasos |
| R03 | Revisión y asignación | E03 ↔ E06 | Administración consulta/actualiza información y estado de la solicitud | Inferido; validar permisos y trazabilidad |
| R04 | Coordinación y desbloqueo | E04 ↔ E03 | Coordinación mantiene visibilidad del progreso y facilita la gestión de bloqueos | Necesidad funcional inferida; validar ownership real |
| R05 | Interfaz clínica | E03 ↔ E05 | Determinadas solicitudes pueden requerir valoración o criterio clínico | Dependencia de alcance; validar cuándo y cómo se deriva |
| R06 | Comunicación de estado | E03 → E01 | Se comunica a la persona solicitante el estado o resultado pertinente | Supuesto del flujo; validar canales y evidencias |
| R07 | Capacidad y recursos | E07 → E03/E04 | Las decisiones de recursos condicionan la capacidad operativa | Dependencia propuesta; validar autoridad y datos disponibles |

Las relaciones representan conexiones funcionales que A3 necesita hacer visibles; no afirman que los canales, sistemas, autoridades o secuencias estén implantados. No se añaden responsables nominales ni mecanismos técnicos no confirmados.

### Macroetapas y flujo principal

Las cuatro macroetapas funcionales propuestas durante la autoevaluación son:

1. Recepción, clasificación y registro de la solicitud.
2. Asignación y escalado de la solicitud.
3. Monitorización, supervisión y comunicación del estado y progreso durante el proceso.
4. Resolución, asignación y revisión de citas.

Como flujo conceptual de alto nivel:

**Recepción y registro → revisión de información y clasificación → asignación o derivación → comunicación y seguimiento → confirmación y resolución.**

La secuencia es una representación de trabajo, no un procedimiento verificado. La supervisión, comunicación, actualización de estado y coordinación atraviesan el flujo. Los traspasos, estados intermedios y condiciones exactas deben contrastarse antes de cualquier uso real.

### Capacidades, recursos y responsabilidades

El avance del proceso depende de que exista capacidad efectiva y adecuada en las funciones que intervienen, incluida la disponibilidad de los roles requeridos, sus competencias, carga de trabajo y medios. La designación nominal de una persona o función no demuestra por sí sola que exista cobertura operativa suficiente.

Se representa una función de coordinación/ownership end-to-end como necesidad sistémica: mantener visibilidad del estado y progreso, facilitar los traspasos, identificar bloqueos y asegurar que exista una siguiente actuación y un responsable operativo. Esto no implica que esa función ejecute todas las tareas, tenga autoridad clínica o disponga de facultades no confirmadas. Los roles concretos, competencias, niveles de cobertura y mecanismos de escalado son datos pendientes de verificación.

### Información, reglas y trazabilidad

Cada solicitud requiere información suficiente para comprender su estado, actuaciones y siguiente paso. El sistema de registro constituye el soporte de referencia propuesto para conservar la información y su historial, sujeto a comprobar sus capacidades reales.

Son dependencias relevantes para el modelo:

- integridad, actualidad, procedencia y consistencia de la información;
- identificación de las reglas aplicables y de sus versiones;
- trazabilidad de decisiones, cambios y actuaciones;
- identificación de bloqueos, solicitudes pendientes y traspasos;
- comunicación del estado pertinente a las funciones implicadas y a la persona solicitante;
- identificación de la versión vigente de las instrucciones operativas y acceso a ella en el punto de uso.

No se presupone que el sistema disponga de auditoría de consultas, notificaciones, confirmaciones de lectura, analítica, automatizaciones o permisos concretos. Esas capacidades deben comprobarse; las lagunas se mantienen como incertidumbres del modelo.

### Fricciones, restricciones y dependencias

El modelo recoge como fricciones o riesgos sistémicos potenciales:

- solicitudes incompletas o información contradictoria;
- capacidad insuficiente o desajustada entre funciones;
- bloqueos y demoras en los traspasos;
- ausencia de responsable o siguiente actuación identificable;
- reglas, criterios o versiones no suficientemente trazables;
- comunicación incompleta o falta de evidencia de adopción de una corrección;
- incidencias que pueden afectar a varias solicitudes;
- efectos residuales sobre actuaciones previas tras una corrección;
- dependencia de valoración o decisión clínica cuando corresponda.

Estos elementos describen dimensiones que el modelo debe permitir observar. No afirman que se hayan producido en una clínica real ni especifican el procedimiento para resolver cada contingencia. Las respuestas operativas, autorizaciones, plazos, umbrales y protocolos quedan fuera del nivel de detalle de A3 y requerirían diseño y aprobación propios.

### Conocimiento, evidencia e incertidumbre

El caso es ficticio. Se distinguen los elementos propuestos para representar el sistema de los hechos que habría que verificar en una organización real. Permanecen pendientes, entre otros, la estructura efectiva de roles, capacidad y carga, reglas y versiones vigentes, tiempos acordados, responsabilidades, traspasos, mecanismos de seguimiento, autoridad de escalado y funciones del sistema de gestión.

La ausencia de datos no se interpreta como prueba de ausencia de una capacidad ni como evidencia de un fallo. Cada incertidumbre deberá resolverse mediante fuentes autorizadas si el modelo se aplicara a un contexto real.

### Puntos de intervención para A4

A3 permite formular hipótesis y alternativas posteriores sobre:

- mejorar la visibilidad y continuidad end-to-end de las solicitudes;
- reducir bloqueos y pérdidas de información en los traspasos;
- ajustar capacidad y cobertura a las necesidades del flujo;
- mejorar la integridad, vigencia y trazabilidad de información y reglas;
- reforzar la comunicación y el seguimiento del estado;
- identificar y gestionar fricciones comunes sin presumir impacto individual.

Estas son áreas de exploración, no soluciones seleccionadas ni afirmaciones causales. A4 deberá formular alternativas contrastables y A5 registrar la evidencia y sus limitaciones.

### Trazabilidad de la autoevaluación A3

Los hallazgos SR-014–SR-061 y sus precisiones se conservan en el registro de autoevaluación. La auditoría de proporcionalidad clasifica su aportación al modelo y distingue entre dimensiones sistémicas que deben representarse aquí y especificaciones operativas que no deben expandir el cuerpo principal de A3. El detalle histórico no se elimina ni se interpreta como conjunto de procedimientos aprobados.

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

### Trazabilidad A3 → A4: necesidad y mecanismo de cada opción

| Opción | Referencia A3 | Fricción/capacidad que aborda | Mecanismo esperado | Estado |
|---|---|---|---|---|
| O0 — Mantener y medir | E06, R02–R03 | Incertidumbre sobre estados, tiempos y trazabilidad | Mejorar la línea base sin cambiar el flujo | Comparador; no presupone que exista un fallo |
| O1 — Revisión diaria de pendientes | E03, E04, E06; R03–R04 | Bloqueos, falta de visibilidad y siguiente actuación | Hacer visibles pendientes y excepciones y facilitar seguimiento | Hipótesis principal H-V1; requiere definir y autorizar la rutina |
| O2 — Mejorar completitud en la entrada | E01, E02, E06; R01–R02 | Solicitudes incompletas y retrabajo | Mejorar la información disponible al inicio | Alternativa distinta; no se atribuye a H-V1 |
| O3 — Aumentar capacidad | E03, E04, E07; R04, R07 | Desajuste entre demanda y capacidad | Ajustar recursos o franjas disponibles | Requiere evidencia de capacidad y decisión de recursos |
| O4 — Rediseño integral | E01–E07; R01–R07 | Fricciones potencialmente distribuidas por el flujo | Rediseñar relaciones y etapas de extremo a extremo | Opción amplia; no justificada solo por el caso ficticio |

La tabla explicita la conexión con A3 sin convertir sus relaciones en requisitos operativos. Las opciones son alternativas de diseño y no descripciones de actuaciones ya implantadas.

### Cadena de razonamiento y contraste de H-V1

- **Necesidad abordada:** mejorar la visibilidad y continuidad del seguimiento de solicitudes pendientes, sin deteriorar el acceso prioritario ni generar una carga inaceptable.
- **Cambio propuesto en O1:** revisión estructurada de pendientes, identificación de excepciones y de la siguiente actuación, y escalado conforme a reglas y autoridades que ya estén autorizadas. Esta descripción pertenece al diseño de la alternativa, no al modelo A3 ni a un procedimiento aprobado.
- **Mecanismo esperado:** mayor visibilidad de solicitudes y bloqueos → identificación más temprana de la siguiente actuación → posible reducción de solicitudes que superan el plazo de referencia.
- **Personas/funciones afectadas:** pacientes/cuidadores (E01), recepción y administración (E02–E03), coordinación (E04) y profesionales sanitarios cuando exista interfaz clínica (E05). La carga y las competencias de cada función deben comprobarse.
- **Supuestos críticos:** el registro permite identificar pendientes y fechas; existe una regla de plazo aplicable y vigente; la revisión es viable con la capacidad disponible; las funciones de coordinación y escalado tienen autoridad definida; las salvaguardas de prioridad se mantienen.
- **Evidencia favorable/contradictoria disponible:** A5 contiene una diferencia descriptiva simulada en solicitudes fuera del plazo de referencia; no mide directamente la ejecución del mecanismo. El reporte cualitativo de aumento de carga es una señal contraria que impide dar por aceptada la carga. El indicador de prioridad no varía en el ejemplo, pero no demuestra ausencia de daño.
- **Prueba posible:** piloto limitado y autorizado, con criterios previos definidos, registro de la realización de revisiones, solicitudes con responsable/siguiente actuación, excepciones escaladas, demora, acceso prioritario y carga comparable.
- **Criterio de revisión/descarte:** no continuar ni ampliar si no se observa mejora relevante según criterios acordados, se deteriora el acceso prioritario, la carga supera el límite acordado o los datos no permiten una conclusión. Los umbrales no están definidos en este caso y no se inventan.

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

### Cobertura de evidencia frente a hipótesis y opciones A4

| Afirmación u opción | Evidencia simulada disponible | Qué permite decir | Qué no permite decir / brecha |
|---|---|---|---|
| H-V1 / O1 — seguimiento estructurado de pendientes | Pendientes más allá del plazo: 28 % antes y 18 % después | Diferencia descriptiva ficticia en un indicador de resultado relacionado con demora | No mide directamente solicitudes bloqueadas sin siguiente actuación, cumplimiento de revisiones diarias ni escalados; no demuestra el mecanismo ni causalidad |
| Salvaguarda de acceso prioritario | 96 % antes y 96 % después | El ejemplo simulado no muestra variación en este indicador | No demuestra seguridad ni ausencia de daño; faltan datos reales, contexto y criterio de no deterioro aprobado |
| Carga de trabajo de O1 | Reporte cualitativo posterior de aumento, sin escala comparable | Señala una posible carga adicional que debe investigarse | No permite determinar si la carga es aceptable ni comparar magnitud |
| O2 — completitud en la entrada | Devoluciones por información incompleta: 15 % antes y 12 % después | Diferencia descriptiva ficticia pertinente a la hipótesis de O2 | No demuestra que O2 se aplicara ni que causara la diferencia |
| O3 — aumento de capacidad | No hay indicador específico de capacidad, dotación, disponibilidad o utilización | Ninguna conclusión sobre el efecto de O3 | Evidencia insuficiente para comparar esta opción |
| O4 — rediseño integral | No hay prueba específica | Ninguna conclusión sobre el efecto de O4 | No se ha diseñado ni evaluado una intervención integral |

**Conclusión de cobertura:** el dataset ficticio ilustra cálculos y trazabilidad, pero no constituye una prueba suficiente de H-V1 ni una comparación completa de O0–O4. No hay datos de fidelidad de implementación (revisiones realizadas, pendientes con responsable/siguiente actuación, excepciones escaladas), ni medida comparable de carga. No se añaden valores para cubrir esas lagunas. Si el caso se utilizara para preparar una prueba real, esas variables y sus definiciones deberían acordarse antes de recoger datos; mientras tanto, se mantienen como evidencia pendiente.

A5 es un registro transversal de evidencia y se usa especialmente en DESIGN y DECIDE; no constituye una fase adicional del ciclo.

## 9. DECIDE — A6 Value Decision Record

**ID:** CLINIC-001-A6  
**Estado:** selección de diseño ilustrativa; autorización de ejecución no concedida; no habilita el paso a ACT real

### Decisión del escenario

Seleccionar **O1 — Revisión diaria de pendientes**, como opción preferida para una posible prueba limitada, reversible y supervisada. La decisión es una **selección de diseño dentro del escenario ficticio**, no una autorización de ejecución. Su puesta en marcha queda condicionada a cerrar los criterios previos pendientes y obtener autorización formal.

### Registro de decisión y autorización (simulado)

- **ID de decisión:** `SIM-CLINIC-001-DEC-v0.1`.
- **Decisor en el escenario:** rol ficticio de responsable de operaciones, sujeto a confirmación de la autoridad real.
- **Fecha:** no especificada en el escenario; debe registrarse antes de una prueba.
- **Estado de la decisión:** opción seleccionada únicamente para desarrollar el diseño de una posible prueba; autorización de ejecución **NO CONCEDIDA / PENDIENTE**. Esta selección no autoriza preparación operativa, comunicación al equipo ni inicio de actividad real.
- **Condiciones de validez:** aprobación de criterios previos; confirmación de capacidad; validación de salvaguardas clínicas y privacidad; designación de responsables; definición de parada.
- **Trazabilidad:** decisión basada en la intención A1, las opciones A4 y el registro simulado A5; las condiciones se trasladan a A7.

Este bloque distingue la selección de diseño de una autorización formal. La decisión ilustrativa permite desarrollar A7 como propuesta documental, pero no iniciar preparativos operativos ni ejecutar la prueba. No representa una firma ni una aprobación real.

### Estado de la cadena de decisión y evidencia

| Estado | Situación en CLINIC-001 | ¿Acreditado? |
|---|---|---|
| Opción seleccionada para desarrollar | O1 seleccionada como preferencia de diseño | Sí, solo dentro del escenario ficticio |
| Criterios previos acordados | Umbrales de mejora, prioridad, carga y calidad de datos | No; pendientes |
| Autorización formal | Autoridad, alcance, recursos, salvaguardas y parada | No concedida |
| Plan A7 | Diseño documental hipotético | Sí, como propuesta |
| Ejecución real | Actividades realizadas por un equipo autorizado | No |
| Resultados observados | Datos procedentes de una ejecución real | No |
| Aprendizaje empírico A8 | Comparación de resultados observados con criterios previos | No |

**Regla de transición:** mientras los criterios previos y la autorización formal permanezcan pendientes, A6 no habilita el paso a ejecución real. A7 puede desarrollarse como diseño documental y A8 solo puede mostrar el ejercicio con datos inventados, sin presentar una ejecución o un resultado como observado.

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
**Estado:** diseño/plan hipotético; no autorizado ni ejecutado en una organización real

### Diseño propuesto de la prueba (no autorizado)

El contenido siguiente es una propuesta de diseño para evaluación y eventual autorización. No constituye instrucción operativa ni compromiso de ejecución.

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

### Secuencia contrafactual ilustrativa — `SIM-CLINIC-001-EXEC-v0.1`

**Aviso:** el registro siguiente no es un registro de ejecución, ni siquiera una ejecución observada dentro de una organización ficticia. Es una secuencia inventada para ilustrar cómo podrían enlazarse un plan, una supuesta actividad y un conjunto de datos simulado. No acredita que se obtuviera autorización, que se realizara preparación, que participara un equipo o que se ejecutara actividad alguna.

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
**Estado:** reconstrucción documental LEARN con datos inventados; no hay resultado observado ni aprendizaje empírico  
**Dataset evaluado:** `SIM-CLINIC-001-DATA-v0.1`  
**Registro de ejecución relacionado:** `SIM-CLINIC-001-EXEC-v0.1`

### Resultados inventados para el ejercicio documental (no observaciones)

Bajo los supuestos inventados de A5, y sin atribuirlos a una ejecución real:

- Las solicitudes pendientes más allá del plazo de referencia pasan del 28 % al 18 %.
- El indicador agregado de solicitudes prioritarias dentro de plazo permanece en el 96 %.
- Las devoluciones por información incompleta pasan del 15 % al 12 %.
- El personal comunica un aumento de carga administrativa, sin una medida cuantitativa comparable.

### Interpretación prudente

**[INTERPRETACIÓN DE DATOS INVENTADOS, NO INFERENCIA EMPÍRICA]** Los valores fabricados son compatibles, dentro del ejemplo, con una mejora descriptiva del indicador de demora y con un posible coste operativo. No son resultados observados, no prueban que se ejecutara la revisión diaria, no respaldan una inferencia causal y no permiten afirmar que el balance global sea positivo. Proceden exclusivamente del dataset ficticio `SIM-CLINIC-001-DATA-v0.1`. `SIM-CLINIC-001-EXEC-v0.1` es una secuencia contrafactual inventada, no una fuente de evidencia de ejecución.

### Aprendizajes documentados

1. No basta con medir el tiempo agregado: debe vigilarse por separado el acceso prioritario.
2. La mejora de un indicador puede coexistir con un coste de carga de trabajo.
3. El registro de causas de bloqueo ayudaría a decidir si el siguiente ciclo debe centrarse en completitud, coordinación o capacidad.
4. Las definiciones de indicadores y la comparabilidad de periodos son requisitos previos, no detalles posteriores.
5. La decisión de escalar exige evidencia real y participación de las personas afectadas.

### Separación entre Sprint, diseño, ejecución y resultados

Los porcentajes y el reporte de carga de este A8 son valores inventados para ilustrar una posible evaluación posterior de cuatro semanas. **No son resultados de una prueba operativa ni del Value Discovery Sprint de cinco días.** No hubo prueba real ni ejecución observada. El A8 presente es solo un ejercicio de reconstrucción documental para comprobar cómo se registrarían datos, interpretaciones y límites si existieran.

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

#### Rebloqueo de una solicitud durante la recuperación

Si una solicitud que se había considerado reincorporada vuelve a quedar bloqueada porque la actuación asignada no se ha completado:

- reactivar su seguimiento operativo y registrar el nuevo bloqueo, la actuación incumplida o pendiente, su causa conocida, el responsable y la siguiente actuación;
- conservar el historial de la reincorporación y de las actuaciones anteriores, sin borrar ni sustituir los registros;
- determinar si se trata de una incidencia que nunca llegó a resolverse o de una nueva ocurrencia después de haber cerrado la incidencia anterior; aplicar en este último caso la distinción y vinculación previstas en SR-051;
- revisar si la misma causa o fallo de ejecución puede afectar a otras solicitudes del lote, comprobándolas individualmente y ampliando las actuaciones solo cuando exista evidencia;
- mantener cada solicitud afectada abierta y bajo seguimiento hasta que se complete la actuación y se verifiquen de nuevo las condiciones de reincorporación.

La revisión del lote no implica declarar bloqueadas todas sus solicitudes ni cerrar automáticamente las incidencias o solicitudes. Esta precisión desarrolla SR-046 y se coordina con SR-045 y SR-051.

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


### SR-057 — Gestión de una incidencia común del proceso con múltiples solicitudes afectadas

Cuando la revisión de solicitudes bloqueadas o reincorporadas revele que varias incidencias comparten un mismo defecto o fallo del proceso, no deben tratarse exclusivamente como problemas aislados de cada solicitud.

- Registrar una incidencia común del proceso que describa el defecto observado, la evidencia disponible, cuándo y cómo se detectó y la persona o instancia responsable de su análisis.
- Vincular a esa incidencia común todas las solicitudes potencialmente afectadas, conservando también el registro y seguimiento individual de cada solicitud. La vinculación no implica asumir que todas están efectivamente afectadas: comprobar cada caso.
- Determinar el alcance conocido y potencial del defecto mediante revisión basada en evidencia; identificar otras solicitudes que puedan estar expuestas y documentar el criterio utilizado para incluirlas o descartarlas.
- Corregir la causa del proceso mediante el mecanismo de cambio y autorización que corresponda. No modificar unilateralmente procedimientos, responsabilidades ni controles, ni dar por corregida la causa por el mero hecho de aplicar una solución provisional.
- Tras la corrección, verificar tanto que el defecto del proceso ha sido tratado como que cada solicitud afectada ha retomado efectivamente su tramitación, con responsable y siguiente actuación definidos. Mantener abiertas y bajo seguimiento las solicitudes que sigan pendientes o bloqueadas.
- Registrar la causa confirmada o aún no confirmada, el alcance, las solicitudes vinculadas, las decisiones, las acciones correctivas, las verificaciones y los responsables. Si la causa no está demostrada, describirla como hipótesis y no como hecho.
- La resolución de la incidencia común no cierra automáticamente las incidencias individuales ni las solicitudes vinculadas.

Esta regla complementa SR-049 y SR-050 (registro y ciclo de vida de incidencias), SR-051 (persistencia y reincidencia) y SR-045/046 (identificación y recuperación individual de solicitudes). Se limita a la gestión operativa del proceso de concertación de citas; no sustituye la investigación de seguridad clínica ni la autoridad clínica cuando procedan. Es una propuesta para el caso ficticio, no un procedimiento aprobado ni validación empírica.


#### Efectos residuales después de corregir el defecto común

La corrección del defecto del proceso y la resolución de sus consecuencias sobre las solicitudes son comprobaciones distintas. Aunque la causa común se haya corregido, algunas solicitudes pueden conservar efectos pendientes que requieran actuaciones adicionales.

- Mantener el registro de la incidencia común hasta verificar que la corrección del defecto se ha implantado y funciona conforme a los criterios autorizados.
- Mantener vinculadas y bajo seguimiento individual las solicitudes que sigan afectadas, identificando para cada una el efecto residual, la actuación necesaria, el responsable y la siguiente actuación.
- Determinar y ejecutar las actuaciones adicionales mediante las competencias y procedimientos autorizados. Cuando las consecuencias impliquen valoración clínica, corresponde decidir a la autoridad clínica competente.
- Verificar individualmente que cada consecuencia relevante ha sido atendida y que se cumplen las condiciones de resolución de la solicitud. No cerrar una solicitud solo porque se haya corregido el defecto común.
- Registrar por separado la verificación de la corrección del proceso y la resolución de los efectos en cada solicitud. La incidencia común podrá cerrarse cuando se cumplan sus propios criterios autorizados, aunque permanezcan solicitudes individuales abiertas; estas deben conservar su seguimiento y vínculo.
- Si las actuaciones individuales revelan que la corrección común fue insuficiente o que el defecto persiste, reabrir o mantener la incidencia común conforme al ciclo autorizado y revisar el alcance potencial.

Esta precisión desarrolla SR-057 y mantiene la separación entre corrección de causa común y tratamiento de consecuencias individuales. No establece criterios de cierre, plazos ni competencias nuevos.


#### Efectos no previstos derivados de la corrección del defecto común

La corrección del defecto puede generar un efecto secundario no previsto en otra etapa del proceso. Por ello, su eficacia no se evalúa únicamente por la resolución del problema original.

- Registrar el efecto observado, cuándo se detectó, la etapa afectada y la evidencia disponible; distinguir hechos confirmados de hipótesis.
- Evaluar el alcance y comprobar qué solicitudes y controles están realmente afectados o potencialmente expuestos, sin asumir que el impacto alcanza a todo el proceso.
- Mantener el seguimiento individual de las solicitudes afectadas y determinar las actuaciones necesarias mediante las competencias y procedimientos autorizados.
- Someter cualquier modificación adicional del proceso al mecanismo de cambio y autorización correspondiente. No introducir ajustes unilaterales para compensar el efecto secundario.
- Verificar que la solución revisada trata el defecto original sin introducir efectos adversos relevantes en otras etapas. Si el efecto revela que la corrección es insuficiente o insegura, revisar la solución conforme al procedimiento autorizado.
- Registrar evaluación, alcance, decisiones, cambios autorizados, verificaciones y responsables.

Esta precisión complementa SR-057 y la regla de efectos residuales: la corrección del problema original no demuestra por sí sola que la solución global sea adecuada. No crea competencias ni autoriza cambios unilaterales.


### SR-058 — Gestión autorizada del cambio de reglas con solicitudes en curso

Cuando se proponga modificar una regla del proceso que ya se utiliza para tramitar varias solicitudes abiertas, el cambio no debe aplicarse de forma implícita ni retroactiva por el mero hecho de que la nueva regla haya sido aprobada.

- Identificar las solicitudes abiertas que utilizan la regla vigente y registrar la versión de regla aplicada, cuando esa información esté disponible. Determinar cuáles pueden verse afectadas por el cambio; no asumir que todas lo están ni limitar el análisis a una muestra sin justificación.
- Evaluar el impacto del cambio sobre cada solicitud afectada, incluidas las actuaciones ya realizadas, los compromisos o plazos aplicables y los controles que dependan de la regla. Cuando corresponda, coordinar la revisión con la instancia competente; las consecuencias clínicas corresponden a la autoridad clínica.
- Antes de aplicar el cambio, obtener la autorización de la instancia competente y dejar documentados el alcance, la fecha o condición de entrada en vigor y la regla de transición aplicable a las solicitudes en curso.
- La transición debe decidirse expresamente conforme a la autorización: mantener la regla anterior para los casos que se determinen, aplicar la nueva regla a los casos que se determinen o revisar individualmente cada solicitud antes de decidir. No se presume que una de estas opciones sea siempre la correcta ni que la regla nueva se aplique automáticamente a todos los casos abiertos.
- Registrar para cada solicitud qué regla se aplica durante la transición, la decisión adoptada, su fundamento, quién la autorizó y cuándo entra en vigor para ese caso. Conservar el historial de la regla anterior y de las actuaciones realizadas; no sobrescribirlo ni mezclar versiones sin trazabilidad.
- Comprobar que ninguna solicitud queda sin responsable, seguimiento o siguiente actuación como consecuencia del cambio. Si la transición revela efectos no previstos, discrepancias o riesgos, mantener la solicitud bajo control y activar la revisión y autorización que correspondan antes de introducir ajustes adicionales.

Esta regla complementa SR-054 y SR-055 cuando el cambio afecta a información o actuaciones previas, y SR-057 cuando la modificación responde a un defecto común del proceso. No crea competencias, plazos, criterios de transición ni autoridad de aprobación; deben estar definidos y autorizados antes de aplicar el cambio. Es una propuesta funcional para el caso ficticio, no un procedimiento aprobado ni validación empírica.


#### Aplicación incorrecta de una regla durante la transición

Si se detecta que una o varias solicitudes recibieron anticipadamente la nueva regla, aunque la transición autorizada establecía que debían continuar con la regla anterior, tratarlo como una desviación de implantación que requiere revisión y corrección controladas.

- Identificar las solicitudes potencialmente afectadas y comprobar individualmente qué regla se aplicó, cuándo, por quién o mediante qué mecanismo y qué transición estaba autorizada. Ampliar la revisión a otros casos potencialmente expuestos con base en evidencia, sin asumir que todo el conjunto está afectado.
- Mantener el historial de versiones, decisiones, actuaciones y registros originales. No sobrescribir la regla aplicada ni ocultar la desviación; registrar también la regla que debía haberse aplicado conforme a la transición autorizada.
- Evaluar por solicitud qué decisiones, comunicaciones o actuaciones se apoyaron en la aplicación anticipada y qué efectos pudieron producirse. Distinguir los hechos comprobados de las consecuencias aún inciertas.
- Someter la corrección de cada caso a la instancia competente. No revertir automáticamente actuaciones ni aplicar la regla anterior de forma mecánica: determinar y autorizar la rectificación adecuada según el caso y la naturaleza de sus efectos; las consecuencias clínicas corresponden a la autoridad clínica.
- Registrar la decisión correctiva, su fundamento, autorización, responsable, momento de aplicación y actuaciones realizadas. Verificar individualmente que cada solicitud queda sometida a la regla que corresponde y conserva responsable, seguimiento y siguiente actuación.
- Analizar si la desviación revela un fallo más amplio en la comunicación, configuración, control o implantación de la transición. Cualquier ajuste del proceso debe seguir el mecanismo de cambio y autorización correspondiente; comprobar después su eficacia y posibles efectos no previstos.

Esta precisión desarrolla SR-058: trata la aplicación incorrecta de una transición ya autorizada, mientras SR-058 establece cómo debe aprobarse y aplicarse el cambio. Se coordina con SR-055 para revisar actuaciones previas y con SR-057 si se identifica un defecto común de implantación. No autoriza rectificaciones automáticas ni crea competencias o criterios nuevos.


### SR-059 — Solicitud abierta sin trazabilidad de la versión de regla aplicada

- **Aprobación del usuario:** sí (2026-10-30).
- **Contexto:** durante una revisión se identifica una solicitud abierta cuyo registro no permite determinar qué versión de regla se aplicó ni si quedó comprendida en la transición autorizada a una regla nueva.
- **Continuidad y control:** mantener la solicitud abierta bajo seguimiento, con responsable y siguiente actuación identificados; no dejar que la incertidumbre de versionado la haga desaparecer del control operativo.
- **Reconstrucción basada en evidencia:** revisar los registros disponibles, fechas, decisiones, actuaciones, comunicaciones y evidencias de la transición. No inferir la versión aplicada ni la que correspondía por defecto. Conservar los datos y discrepancias existentes; documentar qué se ha podido reconstruir y qué información no se ha recuperado.
- **Determinación:** cuando la evidencia no permita resolver qué regla debía aplicarse, someter la cuestión a la instancia competente según el mecanismo de autorización aplicable. La decisión debe establecer qué regla corresponde a la solicitud y cómo proceder con las actuaciones pendientes, dejando constancia del fundamento, responsable/autoridad y momento.
- **Incertidumbre residual:** registrar expresamente cualquier aspecto que siga sin poder determinarse; no presentar una reconstrucción incompleta como certeza.
- **Incertidumbre irresoluble tras la revisión:** documentar qué evidencias se buscaron y revisaron, qué información sigue faltando y por qué no ha sido posible reconstruirla. Mantener la solicitud abierta bajo seguimiento y elevar la cuestión a la instancia competente; no desbloquearla artificialmente ni presentar una hipótesis como decisión.
- **Actuación provisional:** solo podrá realizarse si existe autorización expresa de la instancia competente y esta determina qué actuaciones son admisibles sin conocer la regla histórica. Registrar fundamento, autoridad, alcance, condiciones y límites de la autorización. No ejecutar actuaciones potencialmente perjudiciales o irreversibles sin esa determinación y autorización.
- **Ausencia de vía autorizada:** si no existe una vía autorizada para continuar, mantener la solicitud bajo seguimiento y escalado, con responsable y siguiente revisión/actuación identificados, sin inventar excepciones ni aplicar arbitrariamente una versión de la regla.
- **Reevaluación:** si aparecen nuevas evidencias, reabrir la reconstrucción y la determinación; comprobar asimismo, con evidencia, si la incertidumbre afecta a otras solicitudes.
- **Alcance y prevención:** comprobar, con evidencia, si la falta de trazabilidad afecta a otras solicitudes y si revela una deficiencia de registro, identificación o control de versiones. Cualquier corrección sistémica seguirá el mecanismo autorizado.
- **Relación:** complementa SR-058, que establece la transición autorizada y la trazabilidad por solicitud; se distingue de la aplicación incorrecta conocida de una regla durante la transición, porque en SR-059 la versión aplicada o la regla que correspondía no pueden determinarse con la información disponible. No crea una regla sustantiva nueva, competencias ni presunciones por defecto.
- **Límite:** propuesta funcional para el caso ficticio; no es un procedimiento aprobado ni validación empírica.
- **Estado:** aprobado por el usuario e incorporado documentalmente en la rama del PR #114.

### SR-060 — Revisión de solicitudes cerradas con trazabilidad insuficiente de la regla aplicada

- **Aprobación del usuario:** sí (2026-10-30).
- **Contexto:** durante la revisión de una transición de reglas se identifica una solicitud que figura como cerrada, pero cuyo registro no permite reconstruir qué versión de regla se aplicó ni comprobar si la solicitud quedó comprendida en la transición autorizada.
- **No presumir corrección ni error:** el estado «cerrada» no demuestra por sí solo que la solicitud se resolviera conforme a la regla aplicable; la falta de trazabilidad tampoco demuestra por sí sola que la decisión de cierre fuera incorrecta.
- **Conservación y reconstrucción:** preservar el registro original y su historial. Revisar evidencias disponibles sobre la solicitud, la regla y transición autorizadas, las decisiones, actuaciones, comunicaciones y condiciones de cierre. Documentar qué puede reconstruirse, qué falta y cualquier incertidumbre o discrepancia, sin completar lagunas mediante suposiciones.
- **Evaluación individual:** contrastar lo reconstruido con las condiciones de cierre y la regla que correspondía según la transición autorizada. Identificar si hay actuaciones previas o consecuencias que requieran revisión; no extender la conclusión a otras solicitudes sin evidencia.
- **Determinación competente:** si la evidencia no permite concluir si el cierre fue correcto o qué respuesta procede, elevar el caso a la instancia competente. Esta determinará y documentará si la solicitud permanece cerrada, debe reabrirse para revisión o requiere alguna actuación correctiva autorizada, con fundamento, autoridad/responsable y momento de la decisión.
- **Sin reapertura ni corrección automáticas:** no reabrir ni mantener cerrada por defecto, no borrar ni sustituir el cierre histórico y no ejecutar rectificaciones automáticamente. Toda reapertura o actuación correctiva debe estar justificada, autorizada y trazada; las decisiones clínicas corresponden a la autoridad clínica competente.
- **Alcance sistémico:** comprobar, con evidencia, si otras solicitudes cerradas presentan la misma falta de trazabilidad o si existe una deficiencia común de registro o control de versiones. La revisión de cada solicitud y cualquier corrección sistémica seguirán los mecanismos autorizados.
- **Patrón común en varias solicitudes cerradas:** cuando varias solicitudes cerradas presentan la misma falta de trazabilidad, identificarlas como conjunto potencialmente afectado y documentar el patrón observado, su evidencia y el criterio de inclusión. La pertenencia al conjunto no demuestra que todas aplicaran una regla incorrecta ni que sus cierres fueran inválidos.
- **Revisión individual dentro del conjunto:** conservar para cada solicitud su historial y estado; reconstruir y evaluar cada caso frente a la regla/transición autorizada y sus condiciones de cierre. Registrar por separado qué está confirmado, qué permanece incierto y qué decisión corresponde. No extrapolar el resultado de una solicitud a las demás.
- **Análisis de causa común:** investigar si el patrón deriva de una deficiencia compartida de registro, identificación de versiones o control del proceso. Mientras no se demuestre, describirla como hipótesis. Cualquier corrección del mecanismo común requiere autorización y verificación; no sustituye la determinación individual de los cierres ni implica reabrirlos automáticamente.

- **Relación con SR-055, SR-058 y SR-059:** SR-055 trata el impacto de información corregida sobre actuaciones previas; SR-058 regula la transición autorizada de reglas para solicitudes en curso; SR-059 aborda solicitudes que permanecen abiertas sin trazabilidad suficiente. SR-060 delimita la revisión de solicitudes ya cerradas con esa misma incertidumbre, sin crear una presunción de error, una reapertura automática ni competencias nuevas.
- **Límite:** propuesta funcional para el caso ficticio; no es un procedimiento aprobado ni validación empírica.
- **Estado:** aprobado por el usuario e incorporado documentalmente en la rama del PR #114.

### SR-061 — Comunicación y aplicación efectiva de una corrección documental en el sistema de gestión de citas

- **Aprobación del usuario:** sí (2026-10-30).
- **Escenario:** se corrige un registro o una instrucción del proceso de citas dentro del sistema de gestión, pero algunas personas que consultan o utilizan el proceso pueden seguir trabajando con la información anterior porque no han advertido la corrección.
- **Sistema como canal de referencia:** comprobar si el propio sistema permite identificar la versión vigente, conservar el historial de cambios, localizar a las personas/roles que consultaron o utilizaron la versión anterior y comunicarles la corrección. No exigir duplicar la información en canales externos si las funciones disponibles del sistema permiten una comunicación suficiente y trazable.
- **Identificación del alcance:** determinar, con los registros disponibles y conforme a los permisos aplicables, quién necesita conocer el cambio y qué solicitudes, decisiones o actuaciones pudieron apoyarse en la versión anterior. Diferenciar usuarios que solo pudieron consultar el registro de quienes efectivamente lo utilizaron; no presumir uso ni impacto sin evidencia.
- **Notificación trazable:** utilizar el mecanismo autorizado disponible en el sistema para comunicar la corrección a los destinatarios pertinentes. Registrar contenido o referencia de la corrección, destinatarios, fecha/hora, medio y resultado de la notificación. Si el sistema no permite identificar o notificar adecuadamente a los destinatarios, elevar la limitación y utilizar únicamente un canal alternativo autorizado, dejando constancia.
- **Versión vigente y continuidad:** asegurar que la versión corregida esté claramente identificada y accesible en el punto de uso, preservando el historial y evitando que el registro anterior se confunda con el vigente. No borrar ni sobrescribir la trazabilidad histórica.
- **Verificación de recepción y aplicación:** comprobar, mediante evidencias disponibles, que las personas destinatarias han recibido o consultado la actualización y que utilizan la versión vigente. Una notificación emitida o un indicador de envío no demuestra por sí solo lectura, comprensión ni aplicación efectiva; cuando no pueda acreditarse alguno de estos extremos, registrar la limitación y mantener el seguimiento correspondiente.
- **Impacto de la versión anterior:** revisar las solicitudes o actuaciones que efectivamente pudieron verse afectadas por el uso del registro anterior. Evaluar individualmente las consecuencias y determinar las correcciones mediante las instancias y procedimientos autorizados; no invalidar ni rectificar automáticamente actuaciones previas.
- **Criterio de implantación:** no considerar implantada ni eficaz la corrección por el mero hecho de editar el documento o actualizar el registro. La verificación debe cubrir, según la capacidad real del sistema, la identificación de destinatarios, comunicación, acceso a la versión vigente y aplicación efectiva; registrar las limitaciones pendientes.
- **Límites:** no se presupone que el sistema actual disponga de auditoría de consultas, notificaciones, confirmaciones de lectura o analítica de uso. Estas capacidades deben comprobarse; no inventar funciones, permisos, responsables, plazos ni canales. Si no existen, documentar la brecha y someter la alternativa a autorización. Propuesta funcional para el caso ficticio; no es un procedimiento aprobado ni validación empírica.
- **Relación:** complementa SR-055 cuando la corrección puede afectar actuaciones previas y SR-057 cuando el problema de comunicación/implantación alcanza a varias solicitudes. Se centra en asegurar que la corrección documental llega a quienes la necesitan y se aplica en el punto de uso; no crea una obligación de comunicación externa duplicada.

## Historial de cambios

- **v0.1:** primera reconstrucción integral del caso ficticio; incluye A1–A8, recorrido del Sprint, trazabilidad, resultados simulados, límites y preguntas de revisión.
- **v0.2:** añade identificadores de dataset y ejecución simulados, definiciones operativas y denominadores explícitos, supuestos de selección/ventanas y separación narrativa entre plan y ejecución ficticia. No añade datos reales ni validación empírica.
- **v0.3:** documenta criterios previos de decisión como pendientes cuando no hay umbrales aprobados; separa selección de opción y autorización de ejecución; distingue explícitamente el aprendizaje del Sprint de los resultados de la prueba operativa posterior. No añade datos reales ni validación empírica.
- **v0.4:** incorpora una precisión de SR-058 para detectar, revisar y corregir de forma autorizada la aplicación anticipada o incorrecta de una regla durante la transición; conserva la trazabilidad y evita reversiones automáticas. No añade datos reales ni validación empírica.
- **v0.5:** incorpora SR-059 para solicitudes abiertas cuya versión de regla aplicada no puede determinarse; establece reconstrucción basada en evidencia, decisión competente cuando persiste la incertidumbre y comprobación del alcance de la deficiencia de trazabilidad. No añade datos reales ni validación empírica.
- **v0.6:** precisa SR-059 para los casos en que la incertidumbre persiste tras revisar evidencias: documentación de la búsqueda, seguimiento y escalado, límites de cualquier actuación provisional expresamente autorizada y reevaluación ante nueva evidencia. No añade datos reales ni validación empírica.
- **v0.7:** incorpora SR-060 para revisar solicitudes ya cerradas cuya versión de regla aplicada no puede reconstruirse; exige evaluación individual y decisión competente, sin presumir error ni reabrir o corregir automáticamente. No añade datos reales ni validación empírica.
- **v0.8:** incorpora SR-061 para comprobar la comunicación y aplicación efectiva de correcciones documentales mediante el propio sistema de gestión de citas cuando sus funciones lo permitan; exige verificar capacidades reales y no presume notificaciones, auditoría de consultas ni confirmaciones de lectura. No añade datos reales ni validación empírica.
- **v0.9:** consolida A3 tras la auditoría de proporcionalidad: mantiene actores, macroetapas, flujo, capacidades, responsabilidades funcionales, información, reglas, fricciones, dependencias e incertidumbres; retira del cuerpo principal la especificación detallada de contingencias y controles, conservando los hallazgos y su trazabilidad en el registro de autoevaluación. No añade evidencia real ni validación empírica.
- **v1.0:** añade IDs estables de elementos y relaciones propuestos para A3, una correspondencia explícita de las opciones A4 con el modelo y una matriz de cobertura que identifica qué evidencia simulada informa cada hipótesis/opción y qué brechas permanecen. No se inventan datos adicionales ni se atribuye causalidad; el conjunto A5 sigue siendo ficticio.
- **v1.1:** refuerza la separación entre selección de diseño, criterios previos, autorización, plan, ejecución y resultados. A7 queda expresamente como propuesta no autorizada; el antiguo registro de ejecución se redefine como secuencia contrafactual ilustrativa, no evidencia; A8 se identifica como reconstrucción documental con datos inventados, sin resultados observados ni aprendizaje empírico. No se añaden datos ni se modifica el contenido numérico ficticio.


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
