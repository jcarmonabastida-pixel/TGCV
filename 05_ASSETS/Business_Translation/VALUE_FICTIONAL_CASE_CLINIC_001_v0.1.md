# VALUE — Caso ficticio integral: mejora del acceso a citas en una clínica

**Identificador:** VALUE-CASE-CLINIC-001  
**Versión:** 0.1  
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
**Estado:** borrador ilustrativo

### Oportunidad delimitada

Entender en qué puntos del proceso se acumulan solicitudes de cita pendientes y qué factores modificables contribuyen a ello, sin asumir que la coordinación es necesariamente la causa.

### Síntomas iniciales

- [FICCIÓN-ESCENARIO] Existen quejas por demora.
- [FICCIÓN-ESCENARIO] La dirección sospecha problemas de coordinación.
- [PENDIENTE REAL] No se conoce la distribución de tiempos por tipo de solicitud, prioridad, día o etapa del proceso.

### Preguntas de descubrimiento

1. ¿Cuánto tiempo transcurre entre la recepción de una solicitud y su asignación?
2. ¿En qué etapa se acumulan las solicitudes pendientes?
3. ¿Cómo se identifican y escalan las solicitudes prioritarias?
4. ¿Qué información falta con mayor frecuencia?
5. ¿Qué tareas repetidas o interrupciones afectan a los equipos?
6. ¿Hay diferencias relevantes entre tipos de cita o grupos de pacientes?
7. ¿Qué indicadores y registros existen y con qué calidad?

### Hipótesis iniciales — no confirmadas

- **H1:** parte de las demoras podría estar relacionada con solicitudes incompletas.
- **H2:** la ausencia de una revisión compartida de pendientes podría retrasar la detección de bloqueos.
- **H3:** la capacidad disponible podría ser insuficiente en determinados periodos.
- **H4:** algunos pasos administrativos podrían duplicarse.
- **H5:** las demoras podrían variar según el tipo de cita o prioridad.

### Datos necesarios para un caso real

Tiempos de entrada y asignación, estados de solicitud, prioridad conforme a reglas existentes, motivo de pendiente, devoluciones por información incompleta, carga de trabajo y posibles efectos distributivos. El acceso a datos de pacientes requeriría autorización, minimización y controles de privacidad apropiados.

### Criterio de salida de SENSE

La oportunidad se considera suficientemente delimitada para modelar el sistema cuando el proceso, los grupos afectados, las preguntas abiertas y las fuentes de datos disponibles estén identificados. Este ejercicio solo demuestra la estructura documental; no demuestra que se hayan recogido datos reales.

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

Seleccionar **O1 — Revisión diaria de pendientes**, como prueba limitada, reversible y supervisada, condicionada a confirmar capacidad y salvaguardas antes de iniciar.

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

### Reglas de decisión propuestas

- **Continuar o ampliar:** mejora de acceso acompañada de mantenimiento de salvaguardas y carga aceptable.
- **Adaptar:** mejora parcial con problemas operativos corregibles y sin deterioro de salvaguardas.
- **Detener y revisar:** deterioro del acceso prioritario, riesgo asistencial, carga inaceptable o datos insuficientes para evaluar.
- **No concluir:** si los datos no son comparables o cambian las condiciones externas de forma importante.

No se fijan umbrales clínicos universales en este documento. La organización real tendría que acordarlos según su contexto, obligaciones y capacidad.

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

## Historial de cambios

- **v0.1:** primera reconstrucción integral del caso ficticio; incluye A1–A8, recorrido del Sprint, trazabilidad, resultados simulados, límites y preguntas de revisión.
- **v0.2:** añade identificadores de dataset y ejecución simulados, definiciones operativas y denominadores explícitos, supuestos de selección/ventanas y separación narrativa entre plan y ejecución ficticia. No añade datos reales ni validación empírica.
