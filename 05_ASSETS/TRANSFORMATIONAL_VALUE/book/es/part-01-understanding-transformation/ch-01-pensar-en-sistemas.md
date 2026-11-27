---
content_id: TV-CH-01
language_pair_id: TV-CH-01
title: "Pensar en sistemas"
language: es
content_type: chapter
status: draft
version: 0.3
created: 2026-11-27
updated: 2026-11-27
authors: []
reviewers: []
summary: "Introduce los fundamentos para comprender y describir sistemas como conjuntos organizados de elementos y relaciones."
part: TV-P1
chapter: TV-CH-01
parent_id: TV-P1-OV
tags:
  - systems-thinking
  - systems-engineering
concepts: []
prerequisites: []
related: []
references: []
epistemic_status:
  - established_external_knowledge
source_assets:
  - 05_ASSETS/TRANSFORMATIONAL_VALUE/TRANSFORMATIONAL_VALUE_DETAILED_TOC_v0.1.md
  - 05_ASSETS/TRANSFORMATIONAL_VALUE/TRANSFORMATIONAL_VALUE_LEARNING_MASTER_ARCH_v0.1.md
license: null
---

# Pensar en sistemas

## 1.1. ¿Qué entendemos por sistema?

### Mirar más allá de los componentes

Un sistema no es simplemente una colección de componentes. Es una unidad que podemos estudiar a partir de sus elementos, de la organización que mantienen entre sí y de las relaciones que condicionan su funcionamiento.

Pensemos, por ejemplo, en una red de suministro de agua. Podemos identificar depósitos, estaciones de bombeo, tuberías, válvulas y puntos de consumo. Sin embargo, enumerar esos componentes no basta para comprender cómo se suministra el agua, cómo responde la red a los cambios de demanda o cómo puede propagarse una avería. Para entenderlo necesitamos observar también cómo están organizados y relacionados esos elementos.

Por tanto, para estudiar un sistema no basta con preguntar qué componentes lo forman. También debemos preguntarnos cómo se relacionan y qué comportamiento presenta el conjunto.

### Una definición operativa

A efectos de este libro, podemos utilizar la siguiente definición:

> Un sistema es una unidad de análisis formada por elementos organizados y relacionados, cuyo comportamiento se estudia en función de su configuración y de las condiciones en las que opera.

Esta definición destaca tres aspectos:

- **Elementos:** los componentes, entidades o partes que identificamos como integrantes del sistema.
- **Organización:** la forma en que esos elementos se disponen y articulan.
- **Relaciones:** los vínculos y dependencias que conectan los elementos y condicionan su funcionamiento.

La definición es deliberadamente operativa. No pretende resolver todas las discusiones teóricas sobre qué es un sistema, sino establecer una base de trabajo útil para analizar sistemas reales.

### El comportamiento del conjunto

El comportamiento de un sistema no siempre puede explicarse sumando las propiedades o los comportamientos aislados de sus componentes. La organización y las relaciones entre ellos pueden producir efectos que solo se aprecian al considerar el conjunto.

En la red de suministro de agua, por ejemplo, la capacidad de atender la demanda no depende únicamente de la capacidad individual de cada bomba o del diámetro de cada tubería. También depende de cómo se conectan los distintos tramos, de la distribución de la demanda y de cómo responde la red ante cambios o incidencias.

Esto no significa que los componentes dejen de ser importantes. Significa que su contribución debe entenderse dentro de la configuración en la que operan.

### Una distinción fundamental

Al describir un sistema conviene mantener separadas tres preguntas:

1. ¿Qué elementos o componentes lo forman?
2. ¿Cómo están organizados y relacionados?
3. ¿Qué comportamiento presenta el conjunto bajo determinadas condiciones?

Responder solo a la primera permite elaborar un inventario. Responder también a las otras dos permite empezar a construir una descripción del sistema.

### Idea clave

Un sistema debe estudiarse como un conjunto organizado de elementos y relaciones, no como una simple suma de componentes.

### Pregunta de reflexión

Piensa en un sistema que conozcas —una instalación, un servicio, una organización o una infraestructura— cuyo funcionamiento no pueda explicarse observando sus componentes por separado. ¿Qué relaciones y aspectos de su organización necesitas considerar para comprender su comportamiento?

## 1.2. Propósito, frontera, entorno y contexto

### Antes de analizar, hay que decidir qué estamos estudiando

No podemos analizar un sistema sin establecer primero qué unidad queremos comprender. En muchos casos, los límites físicos parecen evidentes: una máquina, un edificio o una instalación pueden identificarse a simple vista. Pero incluso entonces, decidir dónde termina el sistema y dónde empieza aquello que lo rodea depende de la pregunta que queremos responder.

Consideremos de nuevo una red de suministro de agua. Si queremos estudiar el funcionamiento hidráulico de una zona, podemos delimitar el análisis alrededor de depósitos, estaciones de bombeo, tuberías, válvulas y puntos de entrega. Si queremos estudiar la continuidad del servicio, quizá debamos incluir también los equipos de mantenimiento, los procedimientos de respuesta ante averías y los mecanismos de coordinación. Si la pregunta se refiere a la relación entre consumo y disponibilidad, los usuarios y sus patrones de demanda adquieren una relevancia directa.

No necesariamente estamos describiendo tres sistemas completamente distintos. Estamos estableciendo tres delimitaciones analíticas diferentes, cada una adecuada para una pregunta concreta.

### El propósito: ¿para qué estudiamos el sistema?

El propósito del análisis expresa qué queremos comprender, explicar o evaluar. Orienta la selección de los elementos relevantes, el nivel de detalle y la información que necesitamos recoger.

Conviene distinguir entre el propósito que se declara y el que se observa en la práctica. Una organización puede afirmar que su objetivo es garantizar un servicio continuo, mientras que sus decisiones operativas priorizan reducir costes o limitar determinados riesgos. Ambas dimensiones pueden coexistir, pero no son equivalentes.

En el análisis de sistemas, atribuir un propósito requiere cuidado. Algunos sistemas tienen objetivos explícitos, establecidos por personas u organizaciones. En otros casos, hablamos de funciones o efectos observados sin que exista necesariamente una intención unificada. Por eso debemos indicar si estamos describiendo un propósito declarado, una función asignada o un comportamiento que observamos.

El propósito del análisis tampoco debe confundirse con el propósito del propio sistema. Podemos estudiar una instalación para evaluar su consumo energético aunque su función principal sea suministrar agua. La pregunta del analista y la finalidad de la instalación son cosas distintas.

### La frontera: ¿qué incluimos en el sistema?

La frontera establece qué elementos y relaciones vamos a considerar como parte de la unidad analizada. No siempre coincide con un límite físico, administrativo o contractual.

En una red de agua, por ejemplo, podemos incluir las instalaciones de tratamiento y distribución, pero dejar fuera los hogares que reciben el suministro. Para estudiar la prestación completa del servicio, en cambio, puede ser necesario incorporar los puntos de consumo y determinados procesos que tienen lugar en ellos.

Una frontera útil no es necesariamente la más amplia. Si incluimos demasiados elementos, el análisis puede volverse inmanejable y perder precisión. Si incluimos demasiado pocos, podemos dejar fuera dependencias que explican el comportamiento que intentamos comprender.

La frontera debe justificarse por su relación con el propósito del análisis. También debe hacerse explícita: dos estudios pueden llegar a conclusiones diferentes porque han delimitado de forma distinta el sistema, no necesariamente porque uno de ellos sea incorrecto.

### El entorno: aquello con lo que el sistema se relaciona

El entorno comprende los elementos y condiciones externos a la frontera del sistema que pueden influir en él o verse afectados por su funcionamiento.

En el ejemplo de la red de agua, el entorno puede incluir las condiciones meteorológicas, la disponibilidad de agua en las fuentes de captación, el suministro eléctrico, las normas aplicables y la evolución de la demanda. Aunque estos factores queden fuera de la frontera elegida, pueden condicionar de forma decisiva el comportamiento de la red.

La distinción entre sistema y entorno no significa que ambos estén aislados. Precisamente, parte del análisis consiste en identificar qué intercambios, influencias o dependencias atraviesan la frontera: entradas de recursos, información, energía, demandas, restricciones o efectos sobre otros sistemas.

### El contexto: las circunstancias que dan sentido al análisis

El contexto reúne las circunstancias relevantes para interpretar el sistema y su comportamiento en una situación determinada. Puede incluir condiciones técnicas, económicas, sociales, institucionales, ambientales, históricas o temporales.

Entorno y contexto están relacionados, pero no significan exactamente lo mismo. El entorno se refiere a aquello que rodea al sistema delimitado y mantiene con él relaciones relevantes. El contexto es el marco de circunstancias desde el que interpretamos el sistema, formulamos la pregunta y valoramos qué aspectos son significativos.

Por ejemplo, una reducción de la disponibilidad de agua puede ser una condición del entorno. Que esa reducción se produzca durante una sequía prolongada, bajo determinadas restricciones regulatorias y con una demanda estacional elevada forma parte del contexto en el que debemos interpretar la respuesta de la red.

No todo lo que sucede alrededor de un sistema tiene la misma relevancia. El análisis debe identificar qué circunstancias afectan a la pregunta planteada y explicar por qué se consideran pertinentes.

### Las decisiones de delimitación condicionan las conclusiones

Propósito, frontera, entorno y contexto están conectados. El propósito orienta la frontera; la frontera permite distinguir el sistema de su entorno; y el contexto ayuda a interpretar las condiciones bajo las que se estudia su comportamiento.

Estas decisiones no son un trámite previo que podamos olvidar después. Condicionan qué datos recogemos, qué relaciones observamos y hasta dónde podemos extender nuestras conclusiones.

Por ello, una descripción rigurosa debería dejar claro:

- qué sistema se está analizando y con qué propósito;
- qué elementos y relaciones quedan dentro de la frontera;
- qué factores externos se consideran relevantes;
- en qué circunstancias y horizonte temporal se interpreta su comportamiento;
- qué aspectos se han dejado fuera y cómo podrían limitar las conclusiones.

No existe una única delimitación correcta para todas las preguntas. Existe una delimitación más o menos adecuada y justificable para cada propósito de análisis.

### Idea clave

Antes de explicar cómo funciona un sistema, debemos declarar qué estamos considerando como sistema, para qué lo estudiamos y bajo qué circunstancias interpretamos su comportamiento.

### Pregunta de reflexión

Elige una instalación o un servicio que conozcas. Define una pregunta concreta sobre su funcionamiento y establece una frontera de análisis adecuada. ¿Qué elementos incluirías? ¿Qué factores dejarías en el entorno? ¿Qué circunstancias del contexto podrían cambiar la interpretación de tus conclusiones?


## 1.3. Elementos, estados, propiedades y comportamientos

### De qué está compuesto un sistema y cómo podemos describirlo

Una vez delimitado el sistema que queremos estudiar, necesitamos describir qué lo compone y qué aspectos de sus elementos son relevantes para comprender su funcionamiento. No todos los elementos tienen la misma naturaleza ni necesitamos describirlos con el mismo nivel de detalle. La descripción depende de la pregunta de análisis.

En una red de suministro de agua podemos identificar depósitos, bombas, tuberías, válvulas, sensores, equipos de control y puntos de entrega. También podemos reconocer elementos no físicos, como procedimientos operativos, reglas de control o información utilizada para tomar decisiones. En un sistema socio-técnico, las personas y organizaciones que intervienen forman parte de la descripción cuando sus acciones, decisiones o responsabilidades son relevantes.

El objetivo no es elaborar un inventario exhaustivo de todo lo que existe. Es identificar los elementos que necesitamos para explicar el comportamiento que estamos estudiando.

### Elementos y componentes

Llamaremos **elementos** a las entidades o partes que distinguimos dentro del sistema para describirlo. Según el sistema y el nivel de análisis, pueden ser componentes físicos, personas, equipos, unidades organizativas, procesos, recursos, información o subsistemas.

La elección del nivel de detalle importa. Una estación de bombeo puede tratarse como un único elemento si analizamos la distribución general de la red. Si estudiamos su consumo energético o su fiabilidad, quizá necesitemos distinguir motores, bombas, sensores, sistemas de alimentación y controles.

No existe una descomposición única válida para cualquier análisis. Una descripción útil debe ser suficientemente detallada para responder a la pregunta, pero no tan minuciosa que oculte las relaciones y el comportamiento que queremos comprender.

### Estados: cómo se encuentra el sistema o uno de sus elementos

El **estado** describe cómo se encuentra un sistema o un elemento en un momento o intervalo determinado, atendiendo a las variables que resultan relevantes para el análisis.

En una red de agua, el estado de un depósito podría describirse mediante su nivel de llenado; el de una bomba, mediante su condición operativa y su régimen de funcionamiento; y el de un tramo de red, mediante variables como presión y caudal. Para describir el estado de la red en su conjunto necesitaríamos seleccionar un conjunto de variables que representase los aspectos relevantes de su configuración y operación.

Un estado no es necesariamente una descripción completa de todo lo que existe. Es una representación selectiva: incluye la información que necesitamos para distinguir situaciones que pueden tener consecuencias diferentes para la pregunta estudiada.

Por eso conviene especificar qué variables se utilizan, cómo se observan o estiman y en qué momento se refieren. Dos descripciones del mismo sistema pueden utilizar variables distintas porque responden a preguntas diferentes.

### Propiedades y variables

Las **propiedades** son características que atribuimos a un elemento o sistema y que ayudan a describirlo. Algunas pueden considerarse relativamente estables durante el análisis; otras varían con el tiempo o con las condiciones de operación.

Por ejemplo, el diámetro de una tubería y la capacidad nominal de una bomba describen características del equipamiento. La presión, la temperatura, el nivel de un depósito o el consumo eléctrico pueden variar durante la operación y utilizarse como variables de estado o de seguimiento, según el modelo y la pregunta.

Es útil no confundir una propiedad con el valor que observamos en un momento concreto. La capacidad nominal de una bomba no es lo mismo que el caudal que está entregando ahora. La primera caracteriza al equipo bajo unas condiciones especificadas; el segundo describe una condición de funcionamiento.

En la práctica, la selección de propiedades y variables debe atender a su relevancia, disponibilidad y calidad. Una variable que no podemos medir directamente quizá deba estimarse; una característica que parece importante puede resultar innecesaria para una pregunta concreta. Estas decisiones deben hacerse explícitas cuando condicionen las conclusiones.

### Comportamientos: qué hace y cómo cambia

El **comportamiento** describe cómo actúa o evoluciona el sistema, o alguno de sus elementos, bajo determinadas condiciones. Puede observarse como una pauta de funcionamiento, una respuesta ante una perturbación o una variación de las variables a lo largo del tiempo.

En la red de suministro, el comportamiento puede incluir la forma en que cambia la presión cuando aumenta la demanda, cómo responde el control al descender el nivel de un depósito o cómo se recupera el servicio después de una avería. Para comprenderlo no basta con conocer las propiedades nominales de los componentes: necesitamos observar cómo funcionan en su configuración y condiciones reales.

Conviene distinguir entre estado y comportamiento. El estado describe una situación; el comportamiento se refiere a lo que ocurre o a cómo evoluciona esa situación. Una lectura de presión en un instante informa sobre un estado. Una serie de lecturas durante un periodo puede mostrar cómo responde la red a cambios de demanda.

### Relacionar elementos, estados y comportamientos

Estos conceptos adquieren sentido cuando se utilizan conjuntamente. Los elementos nos dicen qué partes distinguimos; sus propiedades describen características relevantes; los estados representan cómo se encuentran; y los comportamientos muestran cómo actúan o evolucionan.

Consideremos una situación sencilla: aumenta el consumo de agua en una zona. La demanda constituye una condición relevante para el análisis. Podemos observar cambios en el caudal y la presión, identificar qué bombas y válvulas están operando y examinar cómo responde el sistema de control. La explicación requiere conectar las variables observadas con los elementos y las relaciones que forman parte de la red.

La misma observación puede tener explicaciones distintas si cambia la configuración o si faltan datos sobre determinados elementos. Por eso, describir un sistema no consiste en reunir valores aislados, sino en organizarlos de modo que permitan interpretar su funcionamiento.

### Elegir qué describir

Una descripción rigurosa no necesita incluir todas las propiedades posibles. Debe seleccionar las que permitan responder a la pregunta de análisis y dejar constancia de las omisiones relevantes.

Al preparar una descripción inicial, podemos preguntarnos:

- ¿Qué elementos o subsistemas necesitamos distinguir?
- ¿Qué nivel de detalle resulta adecuado?
- ¿Qué propiedades caracterizan a esos elementos?
- ¿Qué variables permiten describir los estados relevantes?
- ¿Qué comportamientos necesitamos observar y durante qué periodo?
- ¿Qué información no está disponible o queda fuera de la descripción?

Estas preguntas ayudan a construir una representación coherente y evitan confundir la información disponible con una descripción completa del sistema.

### Idea clave

Para describir un sistema necesitamos identificar sus elementos, seleccionar las propiedades y variables relevantes, representar sus estados y observar sus comportamientos. Ninguna de estas dimensiones, por sí sola, explica el funcionamiento del conjunto.

### Pregunta de reflexión

Elige una instalación o un servicio que conozcas. Identifica algunos de sus elementos y selecciona una propiedad y una variable relevante para cada uno. ¿Qué estados podrías describir? ¿Qué comportamiento necesitarías observar a lo largo del tiempo para comprender cómo funciona el sistema?
