# C10-S — Especificación candidata B1: entidad solicitante sintética

**ID:** C10S-B1-REQUESTER-CANDIDATE-001  
**Versión:** Draft 001  
**Estado:** DRAFT / CANDIDATO ACEPTADO PARA DESARROLLO / NO INSTANCIA CERRADA  
**Fecha:** 2026-11-11  
**Rama:** research/c10-s-consolidation-draft · **PR:** #116  
**Autoridad:** DEC-C10-095; C10S-B-VALUE-MIN-001; P179/P182/P183; §224.  
**Ámbito:** variante B exclusivamente.

## 1. Decisión de alcance

Se acepta **B1 — entidad solicitante sintética del servicio** como tipo candidato de beneficiario para continuar el diseño de B. La aceptación no identifica una persona real, organización, sistema concreto ni instancia empírica; tampoco cierra todavía la instancia B, la cardinalidad, la demanda, el criterio de valoración o las dimensiones de Value.

A permanece intacta. No se modifica DEC-C10-068 ni el roster de Opción A.

## 2. Definición candidata

Una entidad solicitante sintética es una entidad lógica estipulada en el DGP de B que:
1. tiene una necesidad, objetivo o propósito relacionado con una solicitud antes de la asignación Z;
2. mantiene una relación explícita y versionada con una unidad lógica de servicio;
3. puede originar o estar representada por una solicitud dirigida al servicio;
4. puede experimentar una consecuencia atribuible al procesamiento, no procesamiento o resultado de esa solicitud;
5. puede ser el referente de una perspectiva de valoración fijada ex ante.

La entidad es sintética: su existencia y propiedades pertenecen a la verdad del DGP. No se afirma que represente a un usuario real ni que sus preferencias estén validadas empíricamente.

## 3. Separaciones semánticas obligatorias

| Concepto | Definición en B1 | No debe confundirse con |
|---|---|---|
| Entidad solicitante-beneficiaria | Entidad cuya necesidad/objetivo basal da lugar a la solicitud y cuya consecuencia se valora | Operador, evaluador, propietario técnico |
| Demanda basal | Necesidad/objetivo existente antes de Z | Solicitud emitida, selección, ejecución |
| Solicitud | Expresión/registro de una petición al servicio | Totalidad de la demanda o prueba de valor |
| Unidad lógica de servicio | C10S-SVC-REQUEST-PROCESSOR, bajo versión declarada | Beneficiario |
| Unidad experimental | Unidad a la que se asigna Z | Entidad solicitante, salvo relación explícita |
| Actor ejecutor | Actor/entidad que realiza operaciones si el DGP lo estipula | Solicitante o beneficiario por defecto |
| Evaluador | Rol que adjudica mediciones frente a truth | Beneficiario o solicitante |

La entidad solicitante y la entidad beneficiaria pueden ser la misma entidad lógica **por estipulación explícita de B1**. Esta identidad de rol es una característica candidata de B1, no una inferencia sobre Opción A. Si el DGP futuro distingue solicitante y beneficiario, deberá justificarlo y registrar la relación.

## 4. Relación temporal mínima

La secuencia semántica que debe poder representar B1 es:

- **Pre-Z:** entidad, relación con el servicio, elegibilidad y necesidad/objetivo basal.
- **Z:** asignación de la política experimental.
- **Post-Z:** provisión/intento/instalación/dependencias y estados de accesibilidad conforme al contrato causal.
- **Posteriormente:** oportunidad de formular/considerar/enviar solicitud, procesamiento y consecuencia.
- **Horizonte de valoración:** observación/adjudicación de la consecuencia para la entidad.

La secuencia no presupone que toda demanda genere una solicitud ni que toda solicitud sea procesada, seleccionada o ejecutada. La demanda no atendida debe permanecer en la población elegible y en el denominador pertinente.

## 5. Consecuencia para la entidad: delimitación sin operacionalizar

La consecuencia candidata debe referirse a la situación de la entidad solicitante respecto de su necesidad u objetivo basal. Puede consistir en progreso, cumplimiento, resolución o no resolución del propósito que motivó la solicitud. Esta delimitación es semántica y no elige aún un constructo operacional.

No se aprueba ninguna de las siguientes equivalencias:
- procesamiento técnico correcto = Value;
- conformidad técnica O-CONF = Value;
- solicitud enviada = necesidad satisfecha;
- solicitud procesada = objetivo alcanzado;
- transformación accesible = beneficio recibido;
- ausencia de solicitud = ausencia de demanda;
- no ejecución = Value cero.

El resultado técnico del servicio y la consecuencia para el solicitante deben medirse separadamente. La segunda no puede ser una recodificación del primero.

## 6. No circularidad y vías alternativas

La entidad, su elegibilidad y su demanda basal se estipulan antes de Z y no se redefinen en función de A_f*, ΔT_acc, Reach, selección, ejecución o resultado observado.

La regla de valoración se fija antes de observar los brazos y se aplica simétricamente. No se define Value como una función mecánica de accesibilidad ni como "haber completado" la transformación. Si existen vías de Z/paquete a la consecuencia que no pasan por accesibilidad (coste, demora, riesgo, calidad u otras), el ITT_Z sobre Value es efecto de política/paquete y no identifica por sí solo el efecto focal de accesibilidad.

## 7. Contrato de instancia pendiente

Antes de admitir B1 como instancia confirmatoria, la especificación debe cerrar:
1. identidad lógica y tipo de entidad solicitante, versión y provenance;
2. relación cardinal con unidad experimental y unidad de servicio;
3. elegibilidad y demanda/objetivo pre-Z, incluidos los estados de ausencia;
4. relación entre demanda y solicitud emitida;
5. consecuencia candidata y horizonte, sin equipararla a Outcome técnico;
6. perspectiva y autoridad de valoración;
7. dimensión o dimensiones V_j justificadas por esa consecuencia;
8. unidad, escala, baseline, regla de adjudicación, error y ausencia conforme a §224/P182/P183;
9. DAG de vías mediadas y alternativas;
10. estimandos y supuestos de identificación por dimensión.

No se asignan valores, preferencias, distribuciones, pesos, escalas, umbrales, tiempos, tasas ni parámetros en este documento.

## 8. Consecuencias para C/D/E

- **C / C-Value:** B1 reduce la elección del tipo de entidad; C todavía debe justificar demanda, consecuencia, perspectiva y dimensiones. Las fichas §224 siguen pendientes.
- **D:** deberá representar por separado entidad, demanda pre-Z, solicitud, servicio, unidad experimental, consecuencia y medición; no se aprueba todavía ningún schema físico ni fixture.
- **E:** deberá comprobar que demanda no desaparece por no uso, que Outcome técnico y Value son distintos, que la regla es estable, y que el Analyzer puede abstenerse ante ausencia/no identificación.

## 9. Dictamen

**B1 ACEPTADO COMO TIPO CANDIDATO PARA DESARROLLO; NO COMO INSTANCIA B CERRADA.**

La entidad solicitante-beneficiaria es una simplificación semántica parsimoniosa para el microdominio, siempre que se mantenga explícita la diferencia entre necesidad basal, solicitud, procesamiento y consecuencia valorada.

Permanecen OPEN: instancia y cardinalidad, demanda, consecuencia operacional, perspectiva/autoridad, dimensiones V_j, medición, DAG definitivo, estimandos y parámetros.

No Design Freeze, implementación, fixtures, simulación ni ejecución científica.  
scientific_execution=false  
execution_authorized=false


## 10. Contrato candidato de necesidad/demanda basal B1 — reconciliación con P* y el reloj DGP (2026-11-11)

### 10.1 Definición semántica

Para B1, **necesidad/objetivo basal** es una condición, propósito o estado que la entidad solicitante pretende modificar y que existe en la verdad del DGP antes de la asignación Z. Su existencia no se define por haber emitido una solicitud, haber sido aceptada por el servicio, haber consumido recursos ni haber obtenido un resultado.

La necesidad puede ser conocida/declarada o permanecer no expresada; la modalidad de observación se especificará por separado. La entidad solicitante-beneficiaria puede tener una necesidad basal sin enviar solicitud durante el horizonte.

### 10.2 Distinciones obligatorias

| Constructo | Tiempo/rol | Definición | No equivale a |
|---|---|---|---|
| Need_preZ | Basal, verdad DGP | Existencia de necesidad/objetivo de la entidad antes de Z | Solicitud, uso o resultado |
| E_req_preZ | Basal, elegibilidad de solicitante | Condiciones para que una petición de esa entidad sea admisible según un contrato futuro | Elegibilidad experimental P* |
| Request_event | Evento posterior o temporalmente asignado por contrato pendiente | Petición efectivamente formulada/registrada | Necesidad basal ni demanda total |
| D_resource | Operación/servicio | Recursos/capacidad requeridos o demandados por procesamiento | Necesidad del beneficiario |
| Service_processing | Operación del servicio | Aceptación, rechazo, procesamiento, fallo o estado pendiente de petición | Consecuencia final para el beneficiario |
| Beneficiary_consequence | Resultado posterior | Cambio en la situación de la entidad respecto del objetivo basal | Éxito técnico por sí solo |

E_req_preZ no se identifica con E_i ni con la pertenencia a P*_{τ2}. La reconciliación de P* define elegibilidad de la unidad para el contraste de apertura transformacional; la elegibilidad de una entidad solicitante para formular una petición pertenece al contrato funcional del servicio y no está todavía especificada.

### 10.3 Relación con población experimental y unidad

La necesidad B1 no modifica ni sustituye las condiciones pre-Z de P*_{τ2} o P*_F. La relación entre entidad solicitante, unidad experimental y unidad lógica de servicio sigue abierta, incluida la cardinalidad 1:1/1:N y la posibilidad de múltiples necesidades o solicitudes. No se declara todavía una población confirmatoria B1 mediante una intersección algebraica con P*.

Cualquier población de Value condicionada a Need_preZ o E_req_preZ debe fijarse antes de Z y antes de observar resultados. No se define la población confirmatoria seleccionando solo entidades que enviaron una solicitud después de Z.

### 10.4 Estados y evidencia

La verdad del DGP debe distinguir Need_preZ=1, Need_preZ=0 y Need_preZ=?. El estado ? no se convierte en ausencia. El registro observado del Analyzer es distinto de la verdad generadora y puede contener evidencia suficiente, insuficiente, ausente o contradictoria. La regla de adjudicación y el instrumento para observar la necesidad no se seleccionan aquí.

- Need_preZ=1: existe una necesidad/objetivo basal estipulado; no implica solicitud ni satisfacción.
- Need_preZ=0: no existe la necesidad/objetivo focal definida para esa entidad/instancia; no equivale a ausencia de solicitudes por otros motivos.
- Need_preZ=?: la verdad o su clasificación no está determinada; no imputar cero.
- Request_event=0: no se formuló/registró solicitud en la ventana; no permite inferir Need_preZ=0.
- Request_event=1: se formuló/registró una petición; no demuestra que sea admisible, procesada ni satisfactoria.

Los escenarios sin necesidad focal pueden servir como controles negativos/adversariales para comprobar que el Analyzer no atribuye valor a una necesidad inexistente; no se incorporan automáticamente al estimando primario de Value.

### 10.5 Demanda de recursos y precedencia histórica

El contrato temporal DGP ya exige separar stock, disponibilidad/asignación, demanda y consumo de recursos, y separar capacidad instalada, slots, disponibilidad temporal y carga. Esa demanda es operativa del sistema/servicio; no sustituye Need_preZ del beneficiario. Los recursos requeridos por un procesamiento pueden depender de la solicitud y ser post-Z. No ajustar ITT por mediadores post-Z ni usar consumo como proxy automático de coste económico o Value.

La reconciliación histórica C10-S-POP-CMP-001 mantiene P*_{τ2} y P*_F como poblaciones técnicas pre-Z, con composición de elegibilidad pendiente y fórmula histórica retirada. Esta propuesta no reabre D2 primario candidato/D1 secundario ni altera DEC-C10-066/067.

### 10.6 Orden temporal y solicitud

Need_preZ y, si se justifica, E_req_preZ pertenecen a la caracterización basal anterior a Z. Request_event es un evento distinto cuya ventana y posición exacta en el reloj t−1/t0…t9 aún deben reconciliarse. No se lo equipara automáticamente a conocimiento/consideración (t5), selección/inicio (t6) o ejecución (t7). No se añade un nuevo tiempo ni se cambia el DAG por esta propuesta.

### 10.7 Dictamen

**DISTINCIÓN SEMÁNTICA PROPUESTA; CONTRATO DE DEMANDA PARCIALMENTE ESPECIFICADO.** Queda definido qué no debe confundirse y qué temporalidad debe respetarse. Permanecen OPEN: contenido concreto del objetivo/necesidad, elegibilidad del solicitante, observabilidad, cardinalidad, ventana/posición de solicitud, relación con procesamiento y población/estimando de Value. No se asignan distribuciones, escalas, tasas, parámetros ni valores.


## 11. Ciclo de vida de solicitud y separación del proceso transformacional — propuesta (2026-11-11)

### 11.1 Dos procesos, no una cadena única

B1 requiere distinguir el ciclo de vida de una petición al servicio del ciclo transformacional de migración de configuración. El primero describe interacción con C10S-SVC-REQUEST-PROCESSOR; el segundo conserva Z → provisión → C_dep → A_f* → ΔT_acc → Reach/Π_H → selección/inicio → ejecución → Outcome → Value. La solicitud no es por sí misma una transformación, y su recepción/admisión/procesamiento no se equipara a accesibilidad, selección, ejecución, Outcome ni Value.

### 11.2 Eventos candidatos del ciclo de solicitud

| Evento | Significado | Evidencia mínima a distinguir |
|---|---|---|
| Request_opportunity | Oportunidad/elemento de demanda previamente definido para la entidad | Identidad y elegibilidad basal; no implica envío |
| Request_attempt | Intento externo de transmitir una petición | Registro del emisor/harness y timestamp, incluso si el servicio no responde |
| Request_received | Petición efectivamente recibida en la frontera de ingreso del servicio | Acuse/registro de ingreso; no implica admisión |
| Request_admitted / rejected | Decisión funcional del servicio según contrato y estado aplicable | Decisión y motivo; rechazo no equivale a fallo de procesamiento |
| Request_processing | Trabajo iniciado sobre una petición admitida | Estado de procesamiento separado de admisión |
| Request_response | Respuesta terminal o no terminal al solicitante | Resultado técnico, estado y motivo |
| Beneficiary_consequence | Cambio respecto de Need_preZ | Medición/adjudicación independiente, no inferida del estado del servicio |

Estos nombres son etiquetas semánticas candidatas, no un schema ni una enumeración cerrada. Estados pending, timeout, duplicate, cancelled o unknown requerirán contrato explícito si se incorporan; no se imputan como rechazo, fallo o cero.

### 11.3 Relación con el contrato funcional ya aceptado

El contrato funcional de referencia establece la función lógica del servicio, los parámetros PAR-SVC-ENABLED y PAR-SVC-PROFILE, y la regla RUL-SVC-ENABLE-PROFILE-01. Por tanto, la admisión/aceptación debe respetar el estado funcional declarado y la regla vigente, sin inferir comportamiento adicional a partir de etiquetas de perfil. El contrato funcional no define todavía un protocolo completo de petición, payload, cola, respuesta, errores, SLA ni semántica de reintentos. Este addendum no los inventa.

Request_received no equivale a Request_admitted; Request_admitted no equivale a Request_processing; Request_processing no equivale a Request_response satisfactoria; y ninguna de ellas prueba Beneficiary_consequence.

### 11.4 Relación con t5–t7 sin forzar correspondencia

No se asigna una correspondencia uno-a-uno entre estos eventos y el reloj transformacional:
- t5 K/Consider describe conocimiento/consideración de posibilidades transformacionales; no es automáticamente el envío de una petición al servicio.
- t6 Sel/Start describe selección/inicio de una transformación o trayectoria; no es automáticamente la admisión de una petición.
- t7 Exec describe ejecución transformacional; no es automáticamente el procesamiento interno de una petición.

Una petición puede preceder, acompañar, desencadenar, agrupar o no desencadenar actividad transformacional; la cardinalidad y el enlace request↔transformación quedan OPEN. Se necesita una relación explícita por identidad y timestamp antes de extender el DAG o añadir eventos al reloj.

### 11.5 Protección frente a selección postratamiento

La conducta natural de enviar una petición puede depender de disponibilidad percibida, información, expectativas o tratamiento. Por ello Request_attempt, Request_received y Request_admitted no deben definir la población ITT ni ser criterios de inclusión post-Z. Los no enviados, no recibidos, rechazados, pendientes y no procesados permanecen visibles en el flujo/denominador que corresponda; no se codifican automáticamente como ausencia de necesidad ni Value=0.

Para una comparación sintética confirmatoria, se propone estudiar como opción primaria de control una carga de oportunidades/peticiones estandarizada ex ante, definida antes de Z y presentada mediante un mecanismo externo idéntico en ambos brazos después del snapshot de accesibilidad. El harness debe registrar el intento aunque el servicio no reciba la petición. Esta carga es un estímulo/probe experimental, no evidencia de demanda natural ni de preferencia real del beneficiario. La respuesta y la consecuencia se observan separadamente. Una rama con envío endógeno puede conservarse como escenario secundario/adversarial, sin condicionar el ITT al envío.

Esta recomendación no selecciona todavía el calendario, cardinalidad, payload, mecanismo de entrega, población, parámetro ni estimando.

### 11.6 Dictamen

CICLO DE SOLICITUD DESCOMPUESTO SEMÁNTICAMENTE; ENLACE TEMPORAL Y FUNCIONAL OPEN. Se distinguen oportunidad, intento, recepción, admisión/rechazo, procesamiento, respuesta y consecuencia. No se añade un tiempo al reloj t−1…t9, no se equipara la solicitud con t5/t6/t7 y no se cierra el contrato de petición. La carga estandarizada ex ante es una recomendación de diseño para proteger comparabilidad y evitar selección post-Z, pendiente de aceptación explícita.


## Decisión aceptada DEC-C10S-B1-REQUEST-MODE-001 (2026-11-11)

## Decisión DEC-C10S-B1-REQUEST-MODE-001 — modalidad de oportunidades estandarizadas y envío endógeno (2026-11-11)

**Estado: ACCEPTED AS DESIGN DECISION; NOT DESIGN-FROZEN.**

Se acepta la arquitectura de dos modalidades para C10-S:
1. **Modalidad primaria candidata:** oportunidades/peticiones estandarizadas, definidas ex ante antes de Z y presentadas mediante harness externo idéntico entre brazos después del snapshot de accesibilidad t3/t4. El harness registra Request_attempt aunque el servicio no reciba la petición. Esta modalidad permite comparar respuesta/capacidad bajo una carga de prueba común.
2. **Modalidad secundaria/adversarial:** envío endógeno de solicitudes, cuya ocurrencia puede depender de conocimiento, expectativas, accesibilidad percibida y otros estados post-Z. Se conserva para estudiar selección y vías causales, no para definir la población primaria ni filtrar el ITT.

**Límites de la aceptación.** La carga estandarizada es un probe experimental de servicio; no representa por sí sola demanda natural, preferencia revelada, beneficiario confirmado ni Value. Se mantienen separados intento, recepción, admisión/rechazo, procesamiento, respuesta, consecuencia del beneficiario, Outcome técnico y Value. Los eventos post-Z no se usan como criterio de inclusión o exclusión del ITT. Se conserva el reloj t−1/t0…t9 y no se equiparan eventos de petición con t5/t6/t7 ni con H.

**Pendiente de especificación:** calendario y ventana de presentación; unidad y cardinalidad de oportunidades; identidad y vínculo request_id↔trajectory_id; payload y reglas de admisión; repetición, timeout y errores; tratamiento de solicitudes no recibidas/pendientes; outcome técnico de respuesta; medida independiente de consecuencia B1 y su horizonte; población y soporte; relación exacta con los estimandos ITT/mediación. La modalidad secundaria no recibe estimando confirmatorio por esta decisión.

**No autorizado:** Design Freeze, implementación, fixtures, simulación o ejecución científica. Se mantienen scientific_execution=false y execution_authorized=false. No altera DEC-C10-066/067, D2 primario candidato/D1 secundario ni la rama base de PR #116.
