---
content_id: TV-CH-01
language_pair_id: TV-CH-01
title: "Pensar en sistemas"
language: es
content_type: chapter
status: draft
version: 0.5
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


## 1.4. Actores, capacidades, recursos y dependencias

### Quién interviene y con qué medios

Hasta ahora hemos descrito los elementos de un sistema, sus estados y comportamientos. En muchos sistemas reales, especialmente en los que combinan tecnología, personas y organizaciones, necesitamos identificar además quién interviene, qué puede hacer y de qué medios depende para hacerlo.

Una red de suministro de agua ilustra bien esta dimensión. Su funcionamiento requiere infraestructuras y equipos, pero también operadores que supervisan la instalación, personal de mantenimiento que responde ante incidencias, responsables que toman decisiones y organizaciones que proporcionan energía, materiales o servicios especializados. La infraestructura física no explica por sí sola cómo se mantiene el servicio.

Esta perspectiva permite pasar de una descripción centrada en componentes a otra que también reconoce la contribución de los participantes y los medios que hacen posible la operación.

### Actores: participantes con capacidad de intervención

Llamaremos **actores** a las personas, grupos u organizaciones que pueden intervenir en el sistema o en aspectos relevantes de su funcionamiento. Su papel puede ser operativo, técnico, decisorio, regulador, proveedor o usuario, entre otros.

En la red de agua, los operadores pueden ajustar parámetros y supervisar alarmas; los equipos de mantenimiento inspeccionan y reparan componentes; la dirección establece prioridades y asigna presupuestos; los proveedores suministran equipos y repuestos; y los usuarios generan patrones de demanda y pueden comunicar incidencias.

No todos los actores tienen la misma autoridad, información o grado de intervención. Tampoco todos forman necesariamente parte de la frontera del sistema definida para un análisis concreto. Algunos pueden pertenecer al entorno y, aun así, influir de manera decisiva en el funcionamiento. Por eso conviene identificar su papel y explicar por qué se incluyen en la descripción.

En sistemas que no tienen actores humanos —por ejemplo, ciertos sistemas físicos o procesos automatizados— puede no ser útil forzar esta categoría. La noción de actor es especialmente relevante cuando existen agentes capaces de tomar decisiones o realizar intervenciones intencionales.

### Capacidades: qué puede hacer cada participante o componente

Una **capacidad** expresa la aptitud de un actor, componente o conjunto organizado para realizar una actividad o desempeñar una función bajo determinadas condiciones.

En una instalación de suministro, un operador puede tener capacidad para interpretar las señales del sistema de control y ejecutar procedimientos de ajuste. Un equipo de mantenimiento puede disponer de la capacidad técnica para diagnosticar determinados fallos. Una bomba tiene una capacidad de impulsión definida por sus características y condiciones de operación; el sistema de control puede regular su funcionamiento dentro de ciertos límites.

Conviene distinguir capacidad de actividad observada. Que un equipo o una persona tenga capacidad para realizar una tarea no significa que la esté realizando en este momento. Del mismo modo, una capacidad descrita en un procedimiento o en una especificación puede no estar disponible en la práctica si faltan formación, autorización, herramientas o condiciones adecuadas.

Las capacidades pueden residir en un elemento individual o depender de la combinación de varios. La continuidad del servicio, por ejemplo, puede requerir que los operadores sepan interpretar información, que los sistemas de supervisión la proporcionen y que existan procedimientos para coordinar una respuesta. Ningún participante aislado reúne necesariamente todo lo necesario.

### Recursos: con qué se cuenta para actuar

Los **recursos** son los medios que pueden utilizarse para realizar actividades y sostener el funcionamiento del sistema. Pueden ser materiales, energéticos, financieros, humanos, informativos o temporales.

En la red de agua encontramos recursos físicos como bombas, herramientas, repuestos e instalaciones; recursos energéticos como el suministro eléctrico; recursos humanos como el tiempo y la disponibilidad del personal; y recursos informativos como planos, registros de operación, sensores y documentación técnica.

La mera existencia de un recurso no garantiza que esté disponible para cualquier uso. Puede estar comprometido en otra actividad, encontrarse fuera de servicio, no ser accesible en el momento necesario o requerir autorización. Por tanto, al describir los recursos conviene distinguir entre los que existen, los que están disponibles y los que pueden movilizarse para una tarea concreta.

También debemos evitar confundir recursos con capacidades. Un equipo de diagnóstico es un recurso; saber utilizarlo e interpretar sus resultados es una capacidad. Para realizar una tarea pueden ser necesarios ambos.

### Dependencias: qué necesita una actividad de otras

Una **dependencia** expresa que una actividad, actor o componente necesita que otro elemento aporte algo, realice una tarea o mantenga una condición para que el primero pueda operar como se espera.

Por ejemplo, una reparación puede depender de que haya repuestos disponibles, de que el equipo de mantenimiento tenga acceso a la instalación y de que se pueda interrumpir temporalmente el suministro. La operación de una estación de bombeo puede depender de la energía eléctrica, de la disponibilidad de agua y de que los sistemas de control funcionen correctamente.

Las dependencias pueden ser técnicas, operativas, organizativas, informativas o externas. Algunas son directas y visibles; otras solo se hacen evidentes cuando se produce una incidencia. También pueden variar en importancia según la tarea y las circunstancias.

Identificarlas ayuda a comprender por qué disponer de un componente o de una capacidad no siempre basta para realizar una actividad. El funcionamiento puede depender de una combinación de aportaciones que deben estar disponibles de forma coordinada.

### Una visión integrada de la operación

Actores, capacidades, recursos y dependencias no son categorías independientes que deban estudiarse por separado. Describen dimensiones complementarias de cómo se sostiene una actividad dentro del sistema.

Imaginemos una avería en una conducción principal. Detectarla puede requerir sensores y sistemas de supervisión; interpretarla, personal con conocimiento técnico; planificar la intervención, autoridad para tomar decisiones y coordinar operaciones; y repararla, herramientas, repuestos, acceso y tiempo. La respuesta depende de que esas capacidades y recursos estén conectados mediante procedimientos y responsabilidades adecuados.

Este ejemplo muestra por qué no basta con afirmar que una organización dispone de personal cualificado o de equipamiento moderno. Para comprender su capacidad operativa debemos preguntar qué tareas puede realizar, con qué medios, bajo qué condiciones y de qué otras contribuciones depende.

### Cómo incorporar estas dimensiones a una descripción

Al analizar un sistema con participación humana u organizativa, puede resultar útil registrar:

- qué actores intervienen y qué papel desempeñan;
- qué capacidades son relevantes para las actividades estudiadas;
- qué recursos requieren y cuáles están realmente disponibles;
- de qué personas, componentes, servicios o condiciones dependen;
- qué responsabilidades, autorizaciones o límites condicionan su intervención.

No se trata de elaborar un organigrama o un inventario de recursos por defecto. Se trata de incluir la información necesaria para explicar cómo se realizan las actividades y dónde pueden aparecer limitaciones o dependencias críticas.

### Idea clave

El funcionamiento de un sistema puede depender tanto de sus componentes como de los actores que intervienen, las capacidades que reúnen, los recursos que pueden movilizar y las dependencias que condicionan su actuación.

### Pregunta de reflexión

Piensa en un servicio o una instalación que conozcas. Elige una actividad importante para su funcionamiento e identifica quién debe intervenir, qué capacidades necesita, qué recursos utiliza y de qué otras personas, componentes o condiciones depende. ¿Qué podría impedir que esa actividad se realizara, aunque cada elemento existiera por separado?


## 1.5. Relaciones, interacciones y estructura del sistema

### Un sistema no es solo un conjunto de elementos

Identificar los elementos de un sistema es necesario, pero no suficiente para comprender cómo funciona. También necesitamos describir cómo se relacionan, qué intercambios mantienen y cómo esas relaciones configuran el comportamiento del conjunto.

En una red de suministro de agua, los depósitos, las estaciones de tratamiento, las bombas, las conducciones y los puntos de consumo no operan de forma aislada. El agua circula entre ellos; los sensores transmiten información; los sistemas de control ajustan equipos; y las actividades de mantenimiento condicionan la disponibilidad de la infraestructura. El sistema se reconoce tanto por sus componentes como por la forma en que están conectados y coordinados.

La **estructura del sistema** es la organización de sus elementos y de las relaciones relevantes entre ellos. No es únicamente su disposición física: incluye también conexiones funcionales, flujos de información, dependencias operativas y mecanismos de coordinación.

### Relaciones e interacciones

Una **relación** expresa un vínculo relevante entre dos o más elementos. Puede representar una conexión física, una dependencia, una relación de autoridad, un intercambio de información o cualquier otra asociación necesaria para describir el sistema.

Una **interacción** se refiere a lo que ocurre cuando elementos relacionados actúan o influyen unos sobre otros. Puede consistir en transferir materia o energía, intercambiar información, modificar una condición o coordinar una actividad.

En la red de agua, una tubería conecta físicamente dos partes de la infraestructura y permite el flujo de agua. Un sensor y un sistema de supervisión mantienen una relación informativa: el primero proporciona mediciones que el segundo utiliza para representar el estado de la instalación. Cuando una lectura desencadena un ajuste de una bomba o una válvula, podemos observar una interacción operativa entre medición, decisión y actuación.

No toda relación implica una interacción continua. Una dependencia puede existir aunque solo se haga efectiva en determinadas circunstancias. Del mismo modo, una interacción puntual no siempre modifica de forma duradera la estructura del sistema.

### Flujos, conexiones y mecanismos de coordinación

Las relaciones pueden adoptar formas diferentes. Algunas de las más habituales son:

- **Flujos físicos:** circulación de agua, materiales, energía o productos entre elementos.
- **Flujos de información:** transmisión de mediciones, órdenes, avisos y registros.
- **Conexiones funcionales:** vínculos entre componentes que cooperan para realizar una función.
- **Dependencias operativas:** condiciones o aportaciones que un elemento necesita de otro.
- **Relaciones de coordinación y autoridad:** asignación de responsabilidades, permisos y decisiones entre actores.

En muchos sistemas estas relaciones se superponen. Una estación de bombeo puede estar conectada a la red mediante conducciones, recibir energía de una infraestructura externa, transmitir datos a un centro de control y depender de un equipo de mantenimiento. Cada vínculo describe una dimensión distinta de su integración en el conjunto.

Para evitar confusiones, conviene identificar qué representa cada conexión en un modelo. Una línea puede significar flujo físico, transferencia de información, dependencia o influencia; si no se explica, el lector puede atribuirle un significado que no se pretendía.

### La estructura condiciona el comportamiento

El comportamiento de un sistema depende no solo de las características de sus elementos, sino también de cómo están relacionados. Cambiar una conexión, interrumpir un flujo o modificar una regla de coordinación puede alterar la respuesta del conjunto, incluso cuando los componentes individuales permanecen iguales.

Imaginemos que una conducción principal queda fuera de servicio. El efecto no se limita al tramo averiado: puede cambiar la distribución de caudales, reducir la presión en determinadas zonas y exigir ajustes de bombeo o maniobras de válvulas. La magnitud y extensión de esos efectos dependen de la estructura de la red, de las conexiones alternativas y de las condiciones de operación.

También puede ocurrir que una modificación local mejore el funcionamiento de un componente y, sin embargo, perjudique el resultado del conjunto. Por ejemplo, aumentar el caudal impulsado por una estación puede elevar el consumo energético o superar límites de presión en otros tramos. Para comprender estas consecuencias hay que analizar las relaciones relevantes y no solo el componente intervenido.

### Bucles de realimentación

Algunas estructuras incluyen **bucles de realimentación**: secuencias de relaciones en las que el resultado de una actividad vuelve a influir en las condiciones de operación o en decisiones posteriores.

En una red de agua, un sensor puede detectar una caída de presión; el sistema de control interpreta la señal y ajusta el funcionamiento de una bomba; el cambio de bombeo modifica la presión, que vuelve a ser medida. La información sobre el resultado alimenta así una nueva decisión o ajuste.

La realimentación puede contribuir a mantener una variable dentro de ciertos límites o, en otras circunstancias, amplificar variaciones y producir respuestas inestables. No basta con identificar que existe un bucle: también importa conocer sus retardos, límites, reglas de control y condiciones de operación.

Este concepto no debe confundirse con cualquier conexión de retorno en un dibujo. Para hablar de realimentación, el resultado de un proceso debe volver a influir en ese proceso o en su regulación.

### Representar la estructura sin perder el significado

Un diagrama puede ayudar a reconocer conexiones y distinguir tipos de relación, pero toda representación selecciona una parte de la realidad. Un esquema de infraestructura puede destacar flujos físicos y omitir responsabilidades; un diagrama de control puede mostrar señales y órdenes sin representar la distribución del agua; un mapa organizativo puede reflejar autoridad y coordinación, pero no las restricciones técnicas.

Por ello, el diagrama debe leerse junto con su propósito, alcance y leyenda. Es necesario aclarar qué representan los nodos y las conexiones, qué relaciones se han omitido y si las flechas indican dirección de flujo, transferencia de información o influencia.

El esquema de apoyo de este apartado utiliza una red de suministro simplificada para distinguir los flujos físicos, las señales de información y control, y algunas dependencias externas. No pretende ser un plano de ingeniería ni representar todas las relaciones posibles de una instalación real.

### Idea clave

La estructura de un sistema está formada por sus elementos y por las relaciones que los conectan. Comprender esas relaciones —incluidos los flujos, las dependencias, la coordinación y la realimentación— es esencial para explicar el comportamiento del conjunto.

### Pregunta de reflexión

Elige un sistema que conozcas y dibuja sus principales elementos y conexiones. Distingue los flujos físicos de los intercambios de información y de las dependencias. ¿Qué comportamiento sería difícil de explicar si ignoraras alguna de esas relaciones? ¿Qué conexiones importantes no aparecen en tu representación?

**Diagrama de apoyo:** [TV-DIA-002 — Relaciones y estructura de una red de suministro de agua](../../../assets/diagrams/TV-DIA-002/README.md)
