---
content_id: TV-CH-01
language_pair_id: TV-CH-01
title: "Pensar en sistemas"
language: es
content_type: chapter
status: draft
version: 1.10
created: 2026-11-27
updated: 2026-11-28
authors: []
reviewers: []
summary: "Introduce los fundamentos para comprender y describir sistemas como conjuntos organizados de elementos y relaciones."
part: TV-P1
chapter: TV-CH-01
parent_id: TV-P1-OV
tags:
  - systems-thinking
  - systems-engineering
concepts:
  - TV-TERM-002
  - TV-TERM-003
  - TV-TERM-004
  - TV-TERM-005
  - TV-TERM-006
  - TV-TERM-007
  - TV-TERM-008
  - TV-TERM-009
  - TV-TERM-010
  - TV-TERM-011
  - TV-TERM-012
  - TV-TERM-013
  - TV-TERM-014
  - TV-TERM-015
  - TV-TERM-016
prerequisites: []
related: []
references:
  - TV-REF-007
  - TV-REF-008
  - TV-REF-009
epistemic_status:
  - established_external_knowledge
source_assets:
  - 05_ASSETS/TRANSFORMATIONAL_VALUE/TRANSFORMATIONAL_VALUE_DETAILED_TOC_v0.1.md
  - 05_ASSETS/TRANSFORMATIONAL_VALUE/TRANSFORMATIONAL_VALUE_LEARNING_MASTER_ARCH_v0.1.md
license: null
---

# Pensar en sistemas

## Objetivos de aprendizaje

Al finalizar este capítulo, podrás:

1. **Definir y delimitar un sistema** en relación con el propósito del análisis, su frontera, entorno y contexto.
2. **Describir la composición y organización de un sistema**, identificando sus elementos, estados, propiedades, comportamientos, actores, capacidades, recursos, dependencias y relaciones.
3. **Interpretar el funcionamiento de sistemas abiertos en el tiempo**, considerando intercambios, condiciones cambiantes, respuestas y trayectorias.
4. **Construir y evaluar una descripción de un sistema** adecuada a una pregunta, identificando sus fuentes de información, supuestos, omisiones e incertidumbres y reconociendo sus límites.
5. **Razonar sobre intervenciones a escala de sistema**, considerando interdependencias, restricciones, efectos directos e indirectos, compromisos entre criterios y horizontes temporales.


## 1.1. ¿Qué entendemos por sistema?

### Mirar más allá de los componentes

Cuando observamos una instalación, un servicio o una organización, podemos empezar enumerando las partes que la componen. Ese inventario es útil, pero todavía no explica cómo funciona el conjunto. Para comprenderlo necesitamos examinar también cómo están organizadas esas partes, qué relaciones mantienen y bajo qué condiciones operan.

Pensemos en una red de suministro de agua. Podemos identificar la fuente de captación, las instalaciones de tratamiento, los depósitos, las estaciones de bombeo, las tuberías, las válvulas y los puntos de consumo. Sin embargo, enumerar esos elementos no explica cómo llega el agua a cada zona, cómo responde la red cuando cambia la demanda o cómo una avería puede provocar interrupciones en otros lugares. Para responder a esas preguntas debemos considerar la configuración de la red, sus conexiones, las condiciones de operación y las dependencias de energía y control.

Un sistema es, por tanto, algo más que una colección de elementos presentes en un mismo lugar. Lo reconocemos como un conjunto organizado porque sus elementos mantienen relaciones o dependencias relevantes y, al interactuar o condicionarse entre sí, contribuyen al comportamiento que queremos comprender.

### Una definición operativa

A efectos de este libro, utilizaremos la siguiente definición:

> Un sistema es un conjunto delimitable de elementos relacionados y organizados que interactúan o mantienen dependencias relevantes, y cuyo comportamiento puede comprenderse considerando tanto sus elementos como las relaciones entre ellos, dentro de un contexto y durante un periodo determinados.

Esta definición es una herramienta introductoria de trabajo, no una definición universal aplicable sin matices a todas las disciplinas. Nos permite orientar el análisis hacia cuatro aspectos:

- **Elementos:** las partes, entidades o componentes que distinguimos como relevantes para el sistema de interés.
- **Organización:** la configuración mediante la que esos elementos se disponen y coordinan.
- **Relaciones y dependencias:** los vínculos e interacciones que conectan los elementos o condicionan lo que pueden hacer.
- **Comportamiento:** lo que el sistema hace, cómo responde o cómo evoluciona bajo determinadas condiciones.

No es necesario que todos los elementos interactúen directamente ni que el sistema tenga un propósito explícito. Tampoco todo comportamiento del sistema es necesariamente emergente.

### Sistema de interés y perspectiva de análisis

Conviene distinguir el **sistema de interés** de la **unidad de análisis** y de la **perspectiva analítica**.

El sistema de interés es el sistema concreto que queremos comprender. La unidad de análisis indica sobre qué realizamos observaciones o análisis: puede ser el sistema completo, un subsistema, un actor o una interacción. La perspectiva analítica es el enfoque desde el que lo examinamos, por ejemplo, funcional, operativo, organizativo o temporal.

Así, podemos estudiar una red de agua como sistema de interés y centrar una investigación en una estación de bombeo como unidad de análisis. También podemos examinar esa misma red desde una perspectiva hidráulica, energética, organizativa o de continuidad del servicio. Estas elecciones no cambian necesariamente el sistema de interés, pero sí determinan qué aspectos observamos y qué conclusiones podemos sostener.

### Comportamiento del sistema y comportamiento emergente

El **comportamiento del sistema** comprende las pautas de funcionamiento, respuestas o cambios que podemos observar o inferir. El **comportamiento emergente** es un caso más específico: aparece como resultado de las interacciones y de la organización del conjunto, y no puede explicarse adecuadamente examinando cada elemento por separado.

Por ejemplo, una variación de presión en una tubería puede explicarse en gran medida por las condiciones locales. En cambio, la capacidad de una red para mantener el suministro en distintas zonas durante un aumento de demanda puede depender de la interacción entre depósitos, bombas, conexiones, controles y patrones de consumo. No debemos llamar emergente a cualquier comportamiento del sistema: el término resulta útil cuando la organización y las interacciones del conjunto son esenciales para explicar el fenómeno.

### El alcance del concepto de sistema

En este libro nos centraremos principalmente en sistemas físicos, sociales, organizativos y socio-técnicos. Algunos aspectos de su comportamiento pueden no ser directamente observables y, aun así, pueden estudiarse mediante evidencias pertinentes, como registros, mediciones, decisiones o patrones de actividad.

También podemos utilizar sistemas conceptuales como representaciones o construcciones analíticas. Sin embargo, no los equipararemos automáticamente a sistemas que operan en el mundo. Cuando hablemos de un sistema, el tipo de realidad al que nos referimos y la evidencia que permite estudiarlo deberán resultar claros en el contexto.

### Por qué importa el conjunto

Las propiedades de los componentes siguen siendo importantes, pero su contribución depende de la configuración en la que operan. En la red de agua, la capacidad nominal de una bomba o el diámetro de una tubería no bastan para determinar el servicio que recibe cada zona. También importan la topología de la red, la localización y el momento de la demanda, las condiciones de presión y caudal, las reglas de operación y las dependencias de energía y control.

Una descripción inicial debería responder, al menos, a tres preguntas:

1. ¿Qué elementos forman parte del sistema de interés?
2. ¿Cómo están organizados y relacionados?
3. ¿Qué comportamiento presentan bajo las condiciones que queremos comprender?

La primera pregunta ayuda a construir un inventario. Las otras dos permiten empezar a explicar el funcionamiento del conjunto.

Como lecturas complementarias para ampliar la perspectiva de pensamiento sistémico y su relación con la ingeniería de sistemas, pueden consultarse Meadows (2008) e INCOSE (2023).

### Idea clave

Comprender un sistema exige examinar sus elementos, su organización y las relaciones o dependencias relevantes entre ellos. El comportamiento del conjunto no siempre puede explicarse estudiando cada parte por separado.

### Pregunta de reflexión

Piensa en una instalación, un servicio o una organización que conozcas. ¿Qué parte considerarías el sistema de interés? ¿Podrías estudiarla utilizando distintas unidades de análisis o perspectivas? ¿Qué comportamientos pueden explicarse por las características de elementos concretos y cuáles dependen de la organización y las interacciones del conjunto?

## 1.2. Propósito, frontera, entorno y contexto

### Decidir qué sistema queremos comprender

Antes de analizar un sistema debemos establecer qué queremos comprender y qué vamos a considerar como parte del objeto de estudio. Los límites físicos de una máquina o un edificio pueden parecer evidentes, pero la frontera de un sistema de interés no siempre coincide con el perímetro de una instalación, una organización o un contrato. Depende de la pregunta que guía el análisis.

En una red de suministro de agua, un estudio del comportamiento hidráulico puede centrarse en depósitos, estaciones de bombeo, tuberías, válvulas y conexiones. Si queremos comprender la continuidad del servicio, también pueden ser relevantes los equipos de mantenimiento, los procedimientos de respuesta y los sistemas de control. Si investigamos cómo la demanda afecta a la disponibilidad, tendremos que considerar los puntos de consumo y los patrones de uso.

Son delimitaciones distintas de un mismo sistema de interés, seleccionadas para responder a preguntas diferentes.

### Propósito, función y objetivos

El **propósito del análisis** expresa qué queremos comprender, explicar o evaluar. Orienta la selección del sistema de interés, la frontera, el nivel de detalle y la información necesaria.

No debe confundirse con el **propósito del sistema**, que es la razón de existencia declarada o atribuida al sistema. Tampoco debemos utilizar como sinónimos propósito, función y objetivos:

- **Propósito:** razón de existencia declarada o atribuida al sistema.
- **Función:** actividad o contribución que realiza el sistema.
- **Objetivos:** resultados que se pretende alcanzar; pueden ser varios y entrar en conflicto.

Una organización que gestiona una red de agua puede declarar como propósito garantizar un suministro fiable. Entre sus funciones se encuentran captar, tratar, almacenar y distribuir agua. Sus objetivos pueden incluir continuidad del servicio, calidad, eficiencia energética y control de costes. Estos objetivos pueden reforzarse entre sí o exigir compromisos.

El propósito del análisis es otra cosa: podemos estudiar esa red para comprender su consumo energético, aunque su función principal sea distribuir agua. Mantener separadas estas nociones evita atribuir al sistema una intención que quizá no tenga o confundir la pregunta del análisis con los resultados que el sistema debe producir.

### La frontera y sus interfaces

La **frontera del sistema** establece qué elementos y relaciones se consideran dentro o fuera del sistema de interés. Es una decisión analítica que debe justificarse, no necesariamente un límite físico o administrativo.

La frontera también debe permitir identificar las **interfaces relevantes**: los puntos en los que el sistema se conecta o intercambia algo con otros elementos o sistemas. En una estación de bombeo, por ejemplo, pueden ser relevantes la conexión con el suministro eléctrico, los sistemas de control, la infraestructura que aporta el agua y las conducciones que la reciben.

La frontera puede tener dimensiones físicas, funcionales, operativas y temporales. Una instalación puede estar físicamente delimitada, pero su funcionamiento depender de servicios externos, reglas operativas o procesos que quedan fuera de ese perímetro.

Una frontera demasiado amplia puede hacer que el análisis resulte inmanejable; una demasiado estrecha puede excluir dependencias o interfaces necesarias para explicar el comportamiento. Por ello, debemos seleccionar una frontera adecuada a la pregunta, hacer explícitas las exclusiones relevantes y justificar el nivel de detalle elegido.

La frontera tampoco tiene por qué ser definitiva. Puede revisarse si el análisis o la evidencia revelan dependencias, interfaces o efectos relevantes que inicialmente quedaron fuera. Esa revisión debe justificarse por su relación con el problema, no convertirse en una ampliación arbitraria del sistema de interés.

### El entorno: elementos y condiciones externos relevantes

En este libro utilizaremos **entorno** para referirnos a los elementos, sistemas y condiciones externos a la frontera que interactúan con el sistema de interés o pueden verse afectados por él.

En una red de agua, el entorno puede incluir la disponibilidad de agua en las fuentes de captación, las condiciones meteorológicas, el suministro eléctrico, las normas aplicables y los cambios en la demanda. Estos factores pueden permanecer fuera de la frontera y, aun así, influir de forma significativa en el funcionamiento de la red.

La frontera no implica aislamiento. Parte del análisis consiste precisamente en identificar los intercambios, influencias e interfaces que la atraviesan: materia, energía, información, recursos, servicios, demandas, restricciones o efectos.

### El contexto: circunstancias desde las que interpretamos el sistema

Utilizaremos **contexto** para referirnos al conjunto de circunstancias, relaciones y condiciones desde las que se define e interpreta el problema y el sistema de interés. Puede incluir aspectos técnicos, económicos, sociales, institucionales, ambientales, históricos y temporales.

Entorno y contexto están relacionados, pero cumplen funciones distintas en esta convención editorial. El entorno identifica elementos, sistemas y condiciones externos que interactúan con el sistema o pueden verse afectados por él. El contexto sitúa la pregunta y ayuda a interpretar qué aspectos son relevantes y por qué.

Por ejemplo, la disponibilidad de agua en una fuente de captación puede ser una condición del entorno. Una sequía prolongada, un aumento estacional de la demanda y determinadas restricciones regulatorias conforman circunstancias contextuales importantes para interpretar la respuesta de la red.

Esta distinción es una convención de trabajo adoptada en este libro para facilitar el análisis; no pretende establecer una separación universal utilizada del mismo modo en todas las disciplinas.

### Estas decisiones condicionan lo que podemos concluir

Propósito, frontera, entorno y contexto están conectados. El propósito del análisis orienta la frontera; la frontera distingue el sistema de interés de los elementos y condiciones externos; y el contexto permite interpretar el problema y las condiciones bajo las que observamos el comportamiento.

Estas decisiones afectan a la evidencia que recogemos, las relaciones que examinamos y el alcance de nuestras conclusiones. Dos análisis pueden llegar a resultados diferentes porque han delimitado sistemas de interés distintos o han respondido a preguntas diferentes. Para interpretar sus conclusiones debemos conocer esas decisiones.

Una descripción rigurosa debería indicar:

- qué sistema de interés se estudia y cuál es el propósito del análisis;
- qué elementos y relaciones se incluyen en la frontera;
- qué interfaces e intercambios externos son relevantes;
- qué elementos, sistemas y condiciones se consideran parte del entorno;
- qué circunstancias forman el contexto de interpretación; y
- qué exclusiones pueden limitar el análisis o sus conclusiones.

No existe una frontera correcta para todas las preguntas. Existe una delimitación más o menos adecuada y defendible para un propósito concreto, que puede revisarse si aparecen razones relevantes para hacerlo.

La delimitación del sistema de interés y la identificación de sus interfaces también se abordan en INCOSE (2023) y en la guía de ingeniería de sistemas de NASA (2016).

### Idea clave

La comprensión de un sistema depende de cómo definimos el propósito del análisis, seleccionamos su frontera e interfaces y distinguimos el entorno del contexto. Estas decisiones deben ser explícitas porque condicionan la evidencia y las conclusiones.

### Pregunta de reflexión

Elige un servicio o una instalación que conozcas y formula una pregunta concreta sobre su funcionamiento. ¿Qué sistema de interés delimitarías para responderla? ¿Qué interfaces y dependencias incluirías en la descripción? ¿Qué factores pertenecen al entorno y qué circunstancias forman parte del contexto? ¿Qué evidencia podría llevarte a revisar la frontera inicial?

## 1.3. Elementos, estados, propiedades y comportamientos

### Describir qué forma un sistema y cómo funciona

Una vez definido el sistema de interés, necesitamos describir los elementos que lo forman y las características relevantes para la pregunta que queremos responder. No todos los elementos tienen la misma naturaleza ni necesitamos representarlos con el mismo nivel de detalle. La descripción debe ser selectiva y coherente con el propósito del análisis.

Una red de suministro de agua puede incluir depósitos, bombas, tuberías, válvulas, sensores, equipos de control y puntos de consumo. También depende de procedimientos, reglas de operación e información utilizada para tomar decisiones. En sistemas socio-técnicos, las personas, los equipos y las organizaciones deben formar parte de la descripción cuando sus acciones, decisiones o responsabilidades influyen en el comportamiento estudiado.

El objetivo no es elaborar un inventario exhaustivo de todo lo que existe, sino identificar las partes necesarias para comprender los aspectos relevantes del sistema.

### Elementos y componentes

Utilizaremos **elemento** como término general para cualquier parte o entidad relevante que distinguimos al analizar un sistema. Según el sistema y el nivel de análisis, puede tratarse de una persona, un grupo, una organización, un proceso, un recurso, información, un subsistema o una parte física.

El término **componente** puede utilizarse de forma más específica, especialmente en sistemas técnicos o de ingeniería, para referirse a una parte constituyente del sistema. La distinción no constituye una taxonomía rígida: cuando el contexto disciplinar no requiera diferenciarlos, ambos términos pueden aparecer próximos en su significado. En este capítulo, elemento será el término general.

La elección del nivel de descomposición importa. Una estación de bombeo puede tratarse como un único elemento al estudiar el funcionamiento general de la red. Si analizamos su consumo energético o su fiabilidad, quizá necesitemos distinguir motores, bombas, sensores, alimentación eléctrica y equipos de control. Una descripción útil ofrece el detalle necesario para responder a la pregunta sin ocultar las relaciones relevantes bajo un inventario excesivamente minucioso.

### Estados: la condición en un momento de referencia

El **estado** describe la condición de un sistema o de uno de sus elementos en un momento de referencia determinado, utilizando las variables pertinentes para el análisis.

En una red de agua, el estado de un depósito puede describirse mediante su nivel; el de una bomba, mediante su condición operativa y régimen de funcionamiento; y el de un tramo de red, mediante la presión y el caudal. Para describir el estado de la red en su conjunto seleccionamos las variables que representan los aspectos de su configuración y operación relevantes para la pregunta.

Un estado es una representación selectiva, no una descripción completa de todo lo que existe. Por ello debemos indicar qué variables utilizamos, cómo se observan o estiman y a qué momento se refieren.

Cuando recogemos observaciones durante un intervalo, obtenemos una secuencia o trayectoria de estados. Esa secuencia permite examinar la evolución del sistema y estudiar su comportamiento. El intervalo de observación no debe confundirse con un único estado.

### Propiedades y variables

Una **propiedad** es una característica que atribuimos a un elemento o sistema. Una **variable** es una cantidad o representación que utilizamos para describir o seguir una característica o condición relevante.

Por ejemplo, el diámetro de una tubería o la capacidad nominal de una bomba son propiedades del equipamiento. El caudal entregado en un momento determinado es una variable que permite describir una condición de funcionamiento. La capacidad nominal caracteriza la bomba bajo unas condiciones especificadas; no equivale al caudal que está suministrando en ese instante.

No todas las propiedades necesitan representarse mediante una variable. A su vez, una variable puede utilizarse para observar cómo cambia una propiedad o condición a lo largo del tiempo. La elección depende de la pregunta, la disponibilidad de información y la calidad de la evidencia. Cuando una variable se estima en lugar de medirse directamente, esa circunstancia debe quedar clara si afecta a la interpretación.

### Comportamientos: pautas, respuestas y cambios

El **comportamiento** describe las pautas de funcionamiento, respuestas o cambios de un sistema o de sus elementos bajo determinadas condiciones. Se caracteriza a partir de observaciones o inferencias sobre cómo evolucionan sus estados y variables.

En la red de agua, podemos examinar cómo cambia la presión cuando aumenta la demanda, cómo responde el control cuando desciende el nivel de un depósito o cómo se recupera el servicio después de una avería. Una lectura aislada de presión puede describir un estado, pero normalmente no basta por sí sola para establecer una pauta de comportamiento. Para caracterizarla suelen ser necesarias observaciones repetidas u otras evidencias adecuadas al fenómeno y a la pregunta.

Esto no constituye una regla absoluta: el tipo y la cantidad de evidencia dependen de lo que queremos comprender. Lo importante es no presentar una observación puntual como si demostrara por sí sola un patrón estable.

### Relacionar elementos, propiedades, estados y comportamientos

Estas dimensiones adquieren sentido cuando se consideran conjuntamente. Identificamos los elementos relevantes, describimos algunas de sus propiedades, utilizamos variables para representar condiciones y estados, y examinamos las pautas de funcionamiento que aparecen a lo largo del tiempo.

Supongamos que aumenta el consumo de agua en una zona. Podemos observar cambios en el caudal y la presión, identificar las bombas y válvulas que están operando y examinar la respuesta del sistema de control. Para explicar lo que sucede necesitamos relacionar las variables observadas con los elementos, las conexiones y las condiciones de operación de la red.

Una misma observación puede admitir explicaciones distintas si cambia la configuración o si falta información sobre elementos relevantes. Describir un sistema no consiste, por tanto, en reunir valores aislados, sino en organizarlos de modo que permitan interpretar su funcionamiento.

### Información disponible y aspectos omitidos

Una descripción rigurosa no necesita incluir todas las propiedades posibles, pero debe distinguir entre dos situaciones diferentes:

- **Información desconocida o no disponible:** no contamos con información suficiente o con evidencia accesible sobre un aspecto del sistema.
- **Omisiones deliberadas:** conocemos o reconocemos un aspecto, pero decidimos excluirlo por el propósito, el alcance o el nivel de detalle de la descripción.

La ausencia de un aspecto en una descripción no demuestra que ese aspecto no exista. Tampoco debemos presentar una dependencia desconocida como si la hubiéramos excluido deliberadamente. Cuando estas limitaciones puedan afectar a la interpretación o a las conclusiones, conviene documentarlas y explicar su relevancia.

### Elegir qué describir

Al preparar una descripción inicial, podemos preguntarnos:

- ¿Qué elementos o subsistemas necesitamos distinguir?
- ¿Qué nivel de detalle resulta adecuado para la pregunta?
- ¿Qué propiedades caracterizan a esos elementos?
- ¿Qué variables permiten representar los estados relevantes?
- ¿Qué observaciones o evidencias necesitamos para examinar su comportamiento?
- ¿Qué información no está disponible y qué aspectos hemos decidido omitir?

Estas preguntas ayudan a construir una representación coherente y a evitar que la información disponible se confunda con una descripción completa del sistema.

### Idea clave

Para describir un sistema identificamos elementos relevantes, atribuimos propiedades, utilizamos variables para representar estados y examinamos pautas de comportamiento. También debemos distinguir entre información que falta y aspectos que hemos decidido omitir.

### Pregunta de reflexión

Piensa en una instalación o un servicio que conozcas. Elige uno de sus elementos y distingue una propiedad del equipo de una variable que permita observar su condición. ¿Qué estado podrías describir en un momento concreto? ¿Qué observaciones necesitarías para caracterizar su comportamiento? ¿Qué información podría faltar y qué aspectos podrías decidir omitir por el propósito de tu análisis?

## 1.4. Actores, capacidades, recursos y dependencias

### Quién interviene y qué hace posible su intervención

Hasta ahora hemos descrito los elementos de un sistema, sus estados y comportamientos. En muchos sistemas reales, especialmente en los que combinan tecnología, personas y organizaciones, también necesitamos comprender quién interviene, qué puede hacer, con qué medios cuenta y de qué contribuciones depende.

Una red de suministro de agua lo ilustra bien. Su funcionamiento requiere infraestructuras y equipos, pero también operadores que supervisan la instalación, personal de mantenimiento que responde ante incidencias, responsables que toman decisiones y organizaciones que proporcionan energía, materiales o servicios especializados. La infraestructura física, por sí sola, no explica cómo se mantiene el servicio.

### Actores: personas, grupos y organizaciones que intervienen

En este capítulo utilizamos **actor** en sentido socio-organizativo: una persona, grupo u organización que participa en el sistema o influye de manera relevante en su funcionamiento. Sus papeles pueden ser operativos, técnicos, decisorios, reguladores, proveedores o usuarios, entre otros.

En la red de agua, los operadores supervisan alarmas y ajustan parámetros; el personal de mantenimiento inspecciona y repara equipos; los responsables establecen prioridades y autorizan intervenciones; los proveedores suministran equipos y repuestos; y los usuarios generan patrones de demanda y pueden comunicar incidencias.

Un actor puede encontrarse dentro o fuera de la frontera del sistema de interés. Su inclusión en la descripción depende de que mantenga una interacción, influencia o dependencia relevante para el problema analizado, no simplemente de su ubicación física u organizativa. Estar fuera de la frontera no convierte automáticamente a un actor en parte del entorno en cualquier modelo: esa clasificación depende de cómo se haya delimitado el sistema y del propósito del análisis.

Los sistemas autónomos, los agentes de software y otros elementos no humanos también pueden formar parte del sistema, realizar funciones y producir efectos, pero no se clasifican automáticamente como actores en el sentido adoptado aquí. Si se utiliza el término **agente** con un significado técnico más amplio, debe explicitarse.

### Capacidades: qué puede hacer cada elemento y qué puede lograr el sistema

Una **capacidad** expresa la posibilidad de realizar una actividad o desempeñar una función bajo determinadas condiciones. Puede corresponder a un actor, a un componente o al sistema organizado en su conjunto.

Conviene distinguir tres ideas relacionadas. La **competencia** se refiere a los conocimientos y habilidades que una persona u organización posee para realizar una actividad. La **capacidad** considera también los medios y las condiciones necesarios para poder realizarla. La **disponibilidad efectiva** indica si esa capacidad puede ejercerse realmente en un momento y contexto concretos, teniendo en cuenta factores como la autoridad, el acceso, los recursos, la carga de trabajo o el estado operativo.

Por ejemplo, un técnico puede tener los conocimientos y habilidades necesarios para reparar una bomba, pero carecer de autorización o de las herramientas requeridas. Tiene la competencia, pero no dispone de las condiciones para ejercer efectivamente esa capacidad en ese momento.

También debemos distinguir entre la capacidad de un elemento individual y la **capacidad del sistema**. Un operador puede interpretar señales, una bomba puede impulsar agua y un sistema de control puede regular su funcionamiento. Sin embargo, mantener la continuidad del servicio puede requerir que esas contribuciones se combinen y coordinen con procedimientos, interfaces, recursos y condiciones operativas adecuados. La capacidad del sistema no es una simple suma de capacidades individuales: depende de cómo se integran y coordinan sus elementos.

### Recursos: los medios que pueden movilizarse

Los **recursos** son los medios que pueden utilizarse para realizar actividades y sostener el funcionamiento del sistema. Pueden ser materiales, energéticos, financieros, informativos o temporales, entre otros.

En la red de agua encontramos recursos físicos como bombas, herramientas, repuestos e instalaciones; recursos energéticos como el suministro eléctrico; y recursos informativos como planos, registros de operación, mediciones y documentación técnica. Las personas son actores del sistema, no recursos intercambiables. No obstante, pueden aportar medios necesarios para una actividad mediante su tiempo, conocimientos, experiencia, habilidades o disponibilidad. Conviene identificar esas contribuciones concretas sin confundirlas con la condición de las personas como actores.

La existencia de un recurso no garantiza que esté disponible para cualquier uso. Puede estar comprometido en otra actividad, encontrarse fuera de servicio, no ser accesible cuando se necesita o requerir autorización. Por tanto, al describir los recursos conviene distinguir entre los que existen, los que están disponibles y los que pueden movilizarse para una tarea concreta.

Tampoco debemos confundir recursos y capacidades. Un equipo de diagnóstico es un recurso; saber utilizarlo e interpretar sus resultados forma parte de la competencia y capacidad necesarias para realizar la actividad. Una tarea puede requerir ambos.

### Dependencias y restricciones: qué se necesita y qué limita la actuación

Existe una **dependencia** cuando el funcionamiento, la disponibilidad o la capacidad de un elemento, proceso o sistema para alcanzar un resultado está condicionada por una contribución, servicio, estado o condición proporcionada por otro elemento.

Por ejemplo, una reparación puede depender de que haya repuestos disponibles, de que el equipo de mantenimiento tenga acceso a la instalación y de que se pueda interrumpir temporalmente el suministro. La operación de una estación de bombeo puede depender de la energía eléctrica, de la disponibilidad de agua y del funcionamiento de sus sistemas de control.

Una dependencia no es lo mismo que una relación genérica. Dos elementos pueden estar relacionados sin que uno necesite del otro para funcionar o alcanzar un resultado. Además, las dependencias pueden ser condicionales, sustituibles, recíprocas o sensibles al tiempo, y no todas tienen el mismo grado de criticidad.

También conviene distinguir una dependencia de una **restricción**. La dependencia identifica una contribución o condición necesaria; la restricción establece un límite o condición que reduce las opciones o formas en que puede realizarse una actividad. Ambas pueden coexistir: una estación puede depender del suministro eléctrico y, al mismo tiempo, estar sujeta a límites de consumo, requisitos regulatorios o condiciones de seguridad.

### Una visión integrada de la operación

Actores, capacidades, recursos y dependencias describen dimensiones complementarias de cómo se sostiene una actividad dentro del sistema. No basta con que cada elemento exista por separado: las contribuciones necesarias deben estar disponibles y coordinadas bajo las condiciones adecuadas.

Imaginemos una avería en una conducción principal. Detectarla puede requerir sensores y sistemas de supervisión; interpretarla, personas con conocimientos técnicos; planificar la intervención, responsables con autoridad para tomar decisiones; y repararla, herramientas, repuestos, acceso y tiempo. La respuesta depende de que las competencias y capacidades necesarias puedan ejercerse efectivamente, de que los recursos puedan movilizarse y de que las dependencias estén satisfechas.

Para comprender la capacidad operativa del sistema debemos preguntar qué actividades puede realizar, qué actores intervienen, qué capacidades individuales y colectivas requiere, con qué recursos cuenta, qué contribuciones necesita y qué restricciones condicionan su actuación.

### Cómo incorporar estas dimensiones a una descripción

Al analizar un sistema con participación humana u organizativa, puede resultar útil registrar:

- qué actores intervienen, dónde se sitúan respecto a la frontera y qué papel desempeñan;
- qué competencias y capacidades son relevantes para las actividades estudiadas;
- si esas capacidades están efectivamente disponibles en las condiciones de operación consideradas;
- qué recursos requieren las actividades, cuáles existen y cuáles pueden movilizarse;
- de qué contribuciones, servicios o condiciones dependen;
- qué restricciones, responsabilidades o autorizaciones condicionan su intervención.

No se trata de elaborar por defecto un organigrama o un inventario exhaustivo de recursos. Se trata de incluir la información necesaria para explicar cómo se realizan las actividades y dónde pueden aparecer limitaciones o dependencias críticas.

### Idea clave

El funcionamiento de un sistema puede depender de los actores que intervienen, de las competencias y capacidades que pueden movilizar, de los recursos disponibles y de las dependencias y restricciones que condicionan su actuación. La capacidad del sistema surge de la integración y coordinación de esas contribuciones, no de su mera suma.

### Pregunta de reflexión

Piensa en un servicio o una instalación que conozcas. Elige una actividad importante para su funcionamiento e identifica quién debe intervenir, qué competencias y capacidades necesita, qué recursos puede movilizar y de qué contribuciones o condiciones depende. ¿Qué restricciones podrían impedir que la actividad se realizara, aunque los actores y los elementos necesarios existieran por separado?


## 1.5. Relaciones, interacciones y estructura del sistema

### Un sistema no es solo un conjunto de elementos

Identificar los elementos de un sistema es necesario, pero no suficiente para comprender cómo funciona. También necesitamos describir cómo se relacionan, qué intercambios mantienen y cómo esas relaciones configuran el comportamiento del conjunto.

En una red de suministro de agua, los depósitos, las estaciones de tratamiento, las bombas, las conducciones y los puntos de consumo no operan de forma aislada. El agua circula entre ellos; los sensores transmiten información; los sistemas de control ajustan equipos; y las actividades de mantenimiento condicionan la disponibilidad de la infraestructura. El sistema se reconoce tanto por sus componentes como por la configuración de las relaciones que los conectan y coordinan.

La **estructura del sistema** es la configuración de las relaciones relevantes entre sus elementos. No se limita a su disposición física: incluye también conexiones funcionales, flujos de información, dependencias y mecanismos de coordinación. Puede ser relativamente estable, pero no es necesariamente fija o inmutable.

### Relaciones e interacciones

Una **relación** expresa un vínculo relevante entre dos o más elementos. Puede representar una conexión física, una dependencia, una relación de autoridad, un intercambio de información o cualquier otra asociación necesaria para describir el sistema.

Una **interacción** es una acción, intercambio o influencia que se produce entre elementos relacionados. Puede ser unidireccional, recíproca o asimétrica: no requiere que la influencia se ejerza de manera equivalente en ambas direcciones.

En la red de agua, una tubería conecta físicamente dos partes de la infraestructura y permite el flujo de agua. Un sensor transmite una medición a un sistema de supervisión; un sistema de control envía una orden a una bomba; y una decisión de un responsable puede modificar la actividad de un equipo. Son ejemplos de interacciones cuya dirección y naturaleza dependen de la relación considerada.

No toda relación implica una interacción continua. Una dependencia puede existir aunque solo se haga efectiva en determinadas circunstancias. Del mismo modo, una interacción puntual no siempre modifica de forma duradera la estructura del sistema.

### Flujos, conexiones y mecanismos de coordinación

Las relaciones pueden adoptar formas diferentes. Algunas de las más habituales son:

- **Flujos físicos:** circulación de agua, materiales, energía o productos entre elementos.
- **Flujos de información:** transmisión de mediciones, órdenes, avisos y registros.
- **Conexiones funcionales:** vínculos entre componentes que cooperan para realizar una función.
- **Dependencias:** relaciones estructurales en las que un elemento requiere una contribución o condición de otro. El significado operativo de dependencia se ha definido en el apartado 1.4.
- **Relaciones de coordinación y autoridad:** asignación de responsabilidades, permisos y decisiones entre actores.

Estas formas son perspectivas analíticas, no categorías mutuamente excluyentes. Una misma relación puede combinar, por ejemplo, una conexión funcional, un flujo físico y una dependencia. Una relación de autoridad puede incluir también intercambios de información. Lo importante es identificar qué significado tiene cada vínculo en la representación concreta.

Para evitar confusiones, conviene indicar qué representa cada conexión en un modelo. Una línea puede significar flujo físico, transferencia de información, dependencia o influencia; si no se explica, el lector puede atribuirle un significado que no se pretendía.

### La estructura y las interacciones condicionan el comportamiento

La estructura describe la configuración de las relaciones relevantes; las interacciones describen las acciones, intercambios e influencias que se producen a través de ellas. Ambas dimensiones están conectadas: las interacciones pueden reproducir las relaciones existentes o, en determinadas circunstancias, modificarlas. Por tanto, la estructura puede condicionar el comportamiento del sistema y también cambiar como consecuencia de su funcionamiento.

Imaginemos que una conducción principal queda fuera de servicio. El efecto no se limita al tramo averiado: puede cambiar la distribución de caudales, reducir la presión en determinadas zonas y exigir ajustes de bombeo o maniobras de válvulas. La magnitud y extensión de esos efectos dependen de la estructura de la red, de las conexiones alternativas y de las condiciones de operación.

También puede ocurrir que una modificación local mejore el funcionamiento de un componente y, sin embargo, perjudique el resultado del conjunto. Por ejemplo, aumentar el caudal impulsado por una estación puede elevar el consumo energético o superar límites de presión en otros tramos. Para comprender estas consecuencias hay que analizar las relaciones relevantes y no solo el componente intervenido.

### Bucles de realimentación

Un **bucle de realimentación** existe cuando una cadena cerrada de influencias hace que un resultado del sistema afecte a su funcionamiento posterior o a su regulación.

En una red de agua, un sensor puede detectar una caída de presión; el sistema de control interpreta la señal y ajusta el funcionamiento de una bomba; el cambio de bombeo modifica la presión, que vuelve a medirse. La información sobre el resultado influye así en una decisión o actuación posterior y cierra la cadena de influencias.

Una flecha que vuelve a un elemento anterior en un diagrama no basta, por sí sola, para identificar realimentación: debe existir una cadena de influencias que cierre el circuito. Los bucles de realimentación pueden ser reforzadores, cuando amplifican una tendencia o cambio, o compensadores, cuando contrarrestan una desviación o contribuyen a regular una variable. Su efecto depende de las relaciones, los retardos, las reglas de control y las condiciones de operación.

### Medir y representar la estructura sin perder el significado

Las mediciones ayudan a observar el funcionamiento del sistema, pero una lectura aislada no equivale a su estado completo. Una medición proporciona información sobre una variable o condición concreta. Combinada con otras mediciones, observaciones y conocimiento del funcionamiento, puede utilizarse para monitorizar o inferir las condiciones operativas de la red. Por sí sola no representa todas las dimensiones relevantes del estado del sistema.

Un diagrama puede ayudar a reconocer conexiones y distinguir tipos de relación, pero toda representación selecciona una parte de la realidad. Un esquema de infraestructura puede destacar flujos físicos y omitir responsabilidades; un diagrama de control puede mostrar señales y órdenes sin representar la distribución del agua; un mapa organizativo puede reflejar autoridad y coordinación, pero no las restricciones técnicas.

Por ello, el diagrama debe leerse junto con su propósito, alcance y leyenda. Es necesario aclarar qué representan los nodos y las conexiones, qué relaciones se han omitido y si las flechas indican dirección de flujo, transferencia de información o influencia.

El esquema de apoyo de este apartado utiliza una red de suministro simplificada para distinguir los flujos físicos, las señales de información y control, y algunas dependencias externas. No pretende ser un plano de ingeniería ni representar todas las relaciones posibles de una instalación real.

Para ampliar el tratamiento de las relaciones y la realimentación, véase Meadows (2008); INCOSE (2023) ofrece además una perspectiva de ingeniería de sistemas sobre estos conceptos.

### Idea clave

La estructura de un sistema es la configuración de las relaciones relevantes entre sus elementos; las interacciones son las acciones, intercambios e influencias que se producen a través de ellas. Comprender los flujos, las dependencias, la coordinación y la realimentación permite explicar mejor el comportamiento del conjunto.

### Pregunta de reflexión

Elige un sistema que conozcas y dibuja sus principales elementos y conexiones. Distingue los flujos físicos de los intercambios de información y de las dependencias. ¿Qué comportamiento sería difícil de explicar si ignoraras alguna de esas relaciones? ¿Qué conexiones importantes no aparecen en tu representación?

**Diagrama de apoyo:** [TV-DIA-002 — Relaciones y estructura de una red de suministro de agua](../../../assets/diagrams/TV-DIA-002/README.md)

## 1.6. Sistemas abiertos, entornos cambiantes y tiempo

### La apertura depende de la frontera y del propósito del análisis

Un sistema puede delimitarse para estudiarlo, pero eso no significa que esté aislado de todo lo que queda fuera de su frontera. Para comprender su relación con el entorno, conviene identificar los intercambios que resultan relevantes para la pregunta de análisis.

La apertura no es una propiedad absoluta, independiente de cómo se delimita el sistema. Los intercambios que consideramos relevantes dependen de la frontera seleccionada y del propósito del análisis. Por eso, en lugar de establecer una clasificación rígida entre sistemas abiertos y cerrados, nos centraremos en identificar qué cruza la frontera y por qué importa para el funcionamiento que queremos comprender.

Consideremos una organización que incluye varias instalaciones. Si la analizamos como un conjunto, los intercambios entre sus instalaciones son internos al sistema delimitado. Si después estudiamos una instalación concreta, algunos de esos mismos intercambios —por ejemplo, el suministro de energía, los servicios compartidos o las instrucciones operativas procedentes de otra unidad— pasan a cruzar la frontera del sistema de interés. No ha cambiado necesariamente el intercambio: ha cambiado la delimitación desde la que lo observamos.

### Entradas, salidas y tipos de intercambio

Para describir la relación entre un sistema y aquello que queda fuera de su frontera, debemos distinguir dos dimensiones:

- **Entradas:** aquello que cruza la frontera hacia el sistema de interés.
- **Salidas:** aquello que cruza la frontera desde el sistema de interés hacia su entorno.
- **Tipos de intercambio:** la naturaleza de lo que se intercambia, como materia, energía, información, recursos o servicios. Cualquiera de estos tipos puede constituir una entrada o una salida, según el sistema y la frontera seleccionada.

La siguiente tabla muestra esa distinción. No pretende ser una clasificación universal ni exhaustiva; los ejemplos dependen del propósito y del nivel de detalle del análisis.

| Tipo de intercambio | Posible entrada | Posible salida |
|---|---|---|
| Materia | Agua captada para su tratamiento | Agua distribuida, lodos o residuos |
| Energía | Electricidad suministrada a bombas y equipos | Energía disipada o transferida al entorno |
| Información | Datos de sensores, previsiones, instrucciones recibidas | Avisos, mediciones, informes o información de servicio |
| Recursos y servicios | Repuestos, asistencia técnica o servicios especializados | Servicios prestados o recursos transferidos a otros sistemas |

Esta forma de organizar los intercambios evita confundir la dirección con la naturaleza de lo intercambiado. En algunos sistemas también pueden ser relevantes los flujos financieros, normativos, biológicos o sociales. Su inclusión debe justificarse por la pregunta de análisis.

Tampoco debemos confundir la recepción de una entrada con la disponibilidad efectiva de las condiciones necesarias para utilizarla. Una instalación puede recibir suministro eléctrico y, sin embargo, no estar en condiciones de operar porque no hay personal disponible, el sistema de control está averiado o existe una restricción operativa que impide utilizarlo. La existencia de un intercambio no demuestra por sí sola que el sistema pueda acceder a él, integrarlo o aprovecharlo para realizar sus funciones.

### El entorno puede cambiar

El entorno de un sistema no es necesariamente estable. Pueden variar la demanda, la disponibilidad de recursos, las condiciones físicas, las tecnologías, las normas y las expectativas de quienes utilizan el sistema.

En una red de agua, una sequía prolongada puede reducir la disponibilidad de recursos hídricos; una ola de calor puede elevar la demanda; una modificación normativa puede exigir nuevos controles; y una interrupción del suministro eléctrico puede limitar temporalmente el bombeo. Estos cambios externos pueden alterar las condiciones en las que el sistema opera, incluso cuando su configuración interna no haya cambiado.

La influencia también puede producirse en sentido inverso. Las decisiones y operaciones del sistema pueden modificar su entorno: una infraestructura puede afectar a los usos del suelo, al consumo energético o a los ecosistemas próximos. Por tanto, la relación entre sistema y entorno no siempre es unidireccional.

### El tiempo forma parte de la descripción

Una descripción del sistema tomada en un momento concreto no explica necesariamente su funcionamiento a lo largo del tiempo. Los estados, las relaciones, los recursos disponibles y las condiciones del entorno pueden cambiar. Para comprender un sistema dinámico necesitamos observar no solo cómo está configurado, sino también cómo evoluciona.

Conviene distinguir tres referencias temporales que están relacionadas, pero no son intercambiables:

- **Momento de observación:** cuándo se obtiene una medición o se registra un estado.
- **Periodo cubierto por los datos:** intervalo temporal del que procede la evidencia utilizada en el análisis.
- **Horizonte de las conclusiones:** periodo al que se refieren las interpretaciones o conclusiones.

Una medición puntual puede describir una condición en el momento observado, pero no demuestra por sí sola que esa condición o un determinado comportamiento se mantenga durante meses. Las conclusiones deben ser proporcionales a la cobertura temporal y a la naturaleza de la evidencia disponible.

También puede ser útil distinguir escalas temporales para organizar el análisis:

- **Corto plazo:** variaciones operativas, ciclos diarios de demanda, respuesta a alarmas o interrupciones puntuales.
- **Medio plazo:** mantenimiento, cambios estacionales, renovación de equipos, ajustes de procedimientos y disponibilidad de recursos.
- **Largo plazo:** envejecimiento de infraestructuras, evolución demográfica, cambios climáticos, transformación tecnológica y modificaciones regulatorias.

Estas escalas no son universales ni tienen duraciones fijas. Una variación que es rápida para una infraestructura puede ser lenta para otro sistema. Lo importante es elegir una ventana temporal adecuada a la pregunta y no extender las conclusiones más allá de lo que permite la evidencia.

### Respuesta al cambio, adaptación y transformación

Los sistemas pueden responder de distintas maneras ante cambios del entorno o perturbaciones. Una **respuesta al cambio** es una modificación del estado o del comportamiento del sistema ante una variación interna o externa. Puede consistir en absorber una perturbación, ajustar el funcionamiento, reorganizar elementos o perder la capacidad de prestar el servicio esperado.

La **adaptación** implica una respuesta que modifica características, capacidades, relaciones o formas de funcionamiento para afrontar condiciones cambiantes. No toda respuesta constituye una adaptación, y esta no tiene por qué ser exitosa, beneficiosa o intencional. Puede resultar insuficiente, fallar o producir consecuencias no deseadas; también puede surgir de ajustes distribuidos o procesos no planificados.

Conviene distinguir, además, entre un **ajuste operativo** y una **transformación**. El criterio decisivo no es cuánto dura el cambio, sino su naturaleza y alcance:

- Un ajuste operativo modifica el estado, el comportamiento o los parámetros de funcionamiento sin alterar necesariamente la configuración fundamental del sistema.
- Una transformación modifica de manera relevante la configuración, organización, relaciones o capacidades del sistema y puede cambiar lo que este es capaz de hacer.

Por ejemplo, modificar temporalmente las consignas de una bomba puede ser un ajuste operativo. Rediseñar la red, reorganizar sus dependencias o incorporar capacidades que cambien las operaciones que puede realizar puede constituir una transformación. Un cambio breve puede desencadenar una transformación estructural, mientras que una modificación prolongada puede seguir siendo un ajuste operativo. Del mismo modo, una transformación no garantiza por sí sola una adaptación exitosa.

### Una fotografía y una trayectoria del sistema

Podemos describir un sistema mediante una representación de su configuración en un instante, o mediante otra que muestre cómo cambian sus condiciones y su comportamiento a lo largo del tiempo. Ambas perspectivas son útiles, pero responden a preguntas distintas.

Una descripción puntual de la red de agua puede mostrar qué depósitos, bombas y conducciones están disponibles en un momento determinado. Una descripción temporal puede mostrar cómo varían los niveles de los depósitos, la demanda, el consumo energético y las incidencias durante una semana o una estación.

La perspectiva temporal también obliga a declarar cuándo se recogieron los datos, qué periodo cubren y a qué horizonte se refieren las conclusiones. Sin esa información, podemos atribuir a la estructura del sistema lo que en realidad se debe a una condición temporal o a una perturbación externa.

### Idea clave

Para comprender cómo se relaciona un sistema con su entorno debemos identificar los intercambios que cruzan la frontera elegida y distinguir su dirección de su naturaleza. También debemos considerar las condiciones cambiantes, la cobertura temporal de la evidencia y la diferencia entre responder a un cambio, adaptarse y transformarse.

### Pregunta de reflexión

Elige un sistema que conozcas. Define primero la frontera y el propósito de tu análisis. ¿Qué entradas y salidas identificarías y de qué tipo son? ¿Qué condiciones podrían impedir que el sistema utilizara una entrada recibida? ¿Qué evidencia temporal necesitarías para distinguir una respuesta puntual, una adaptación y una transformación?

## 1.7. Las descripciones de sistemas son modelos: alcance, supuestos y omisiones

### Describir no es reproducir toda la realidad

Una descripción de un sistema no es el sistema mismo. Es una representación selectiva construida deliberadamente para comprender determinados aspectos de él, responder a una pregunta o apoyar una tarea. En este capítulo utilizamos el término **modelo** en este sentido amplio: puede adoptar la forma de un texto, un diagrama, una tabla, un conjunto de variables o un modelo matemático o computacional. No tiene que estar expresado mediante ecuaciones ni implementado en un programa para funcionar como modelo.

Toda representación selecciona qué mostrar y qué dejar fuera. Incluso una descripción muy detallada simplifica la realidad: no incluye todos los elementos, relaciones, estados, acontecimientos y condiciones posibles. Esto no la convierte automáticamente en una descripción deficiente. La cuestión es si las decisiones de simplificación son adecuadas para el propósito del análisis y si sus límites se hacen explícitos.

En una red de suministro de agua, por ejemplo, un esquema de tuberías puede ser suficiente para estudiar la conectividad entre depósitos y zonas de consumo. No bastará necesariamente para analizar la respuesta ante una interrupción eléctrica, la organización del mantenimiento o los efectos de una variación prolongada de la demanda.

### El propósito determina el alcance del modelo

Un modelo es una representación selectiva del sistema, construida para responder a una pregunta o apoyar una tarea. Para describir sus decisiones conviene distinguir tres aspectos relacionados, pero no equivalentes:

- **Alcance de la representación:** los aspectos del sistema que el modelo pretende cubrir para responder a la pregunta planteada.
- **Frontera del sistema:** qué se considera dentro y fuera del sistema de interés para el análisis.
- **Nivel de detalle:** con qué grado de desagregación se representan los elementos y relaciones incluidos.

Un modelo puede tener un alcance amplio y representar algunos aspectos con poco detalle, o estudiar un subsistema con gran detalle sin cubrir el sistema completo.

No existe un único modelo que resulte igualmente útil para todas las preguntas. Consideremos varias representaciones posibles de una misma red:

| Pregunta de análisis | Representación útil | Aspectos que prioriza | Aspectos que puede dejar fuera |
|---|---|---|---|
| ¿Cómo llega el agua a cada zona? | Esquema de la red | Tuberías, depósitos, conexiones y dirección del flujo | Consumo energético, mantenimiento y organización |
| ¿Cómo responde la red a cambios de demanda? | Modelo hidráulico u operativo | Caudales, presiones, niveles y condiciones de operación | Decisiones organizativas o impactos sociales no modelizados |
| ¿Qué ocurre si falla el suministro eléctrico? | Modelo de dependencias y escenarios | Alimentación eléctrica, bombeo, controles y consecuencias de la interrupción | Detalles hidráulicos que no afecten a la pregunta |
| ¿Cómo se mantiene la continuidad del servicio? | Modelo socio-técnico del servicio | Equipos, personal, procedimientos, repuestos y coordinación | Detalles de componentes que no condicionen la continuidad |

Las representaciones de la tabla no son intercambiables. Cada una hace visibles determinados aspectos y facilita un tipo de razonamiento. Una puede complementar a otra cuando la pregunta exige conectar dimensiones distintas.

### Supuestos: lo que damos por válido para poder analizar

Para construir un modelo podemos utilizar valores de entrada o parámetros cuyo origen no es siempre el mismo. Pueden proceder de mediciones, estimaciones, especificaciones técnicas o supuestos adoptados. Por tanto, un valor introducido en un modelo no es necesariamente un supuesto.

Por ejemplo, el caudal medido en un punto de la red es un valor observado; la demanda futura puede ser una estimación; la capacidad nominal de una bomba puede proceder de su especificación técnica; y considerar que la bomba estará disponible durante todo el periodo de análisis constituye un supuesto.

Los supuestos son condiciones que adoptamos para poder analizar. Algunos simplifican la complejidad; otros fijan condiciones de partida o establecen relaciones cuando no contamos con información suficiente. Deben distinguirse tanto de los hechos observados como de la incertidumbre cuantificada: esta última expresa un rango o distribución de valores posibles, no una condición que damos simplemente por válida.

Por ejemplo, un análisis de la red podría suponer que la demanda permanece constante durante un intervalo, que determinados equipos están disponibles o que las características de las tuberías no cambian durante el periodo estudiado. Estos supuestos pueden ser razonables para una pregunta concreta y un horizonte temporal limitado, pero dejarían de serlo en otras circunstancias.

Si no sabemos si una bomba estará disponible, debemos registrar esa condición como desconocida o formular explícitamente un supuesto. No podemos presentarla como un dato confirmado simplemente porque el modelo necesite una condición de partida.

Conviene registrar los supuestos que puedan influir en los resultados, explicar por qué se adoptan y señalar bajo qué condiciones dejarían de ser aceptables. Cuando sea posible, podemos comprobar cómo cambian las conclusiones al modificar los supuestos más relevantes.

### Omisiones: lo que el modelo no representa

Las omisiones son inevitables, pero conviene distinguir entre una **omisión deliberada** y la **información desconocida o no disponible**, como ya se explicó en el apartado 1.3. La primera corresponde a un aspecto conocido o reconocido que se excluye intencionadamente por razones de alcance, propósito o simplicidad. La segunda se refiere a un aspecto para el que no disponemos de información o evidencia suficiente.

No debemos presentar una dependencia desconocida como si se hubiera excluido deliberadamente. Del mismo modo, que un elemento o una relación no aparezca en el modelo no demuestra que no exista.

Dejar fuera deliberadamente un detalle irrelevante para la pregunta puede hacer que el modelo sea más claro y manejable. Excluir una dependencia crítica, en cambio, puede producir una explicación incompleta o una conclusión engañosa.

Imaginemos que un modelo representa las bombas, tuberías y depósitos de una red, pero no incluye la dependencia de las estaciones respecto al suministro eléctrico. Puede describir adecuadamente ciertos comportamientos hidráulicos en condiciones normales y, sin embargo, resultar insuficiente para analizar la continuidad del servicio durante un apagón.

Por eso, además de preguntar qué incluye una representación, debemos preguntar qué no incluye y qué consecuencias puede tener esa ausencia. Una omisión se vuelve especialmente relevante cuando podría cambiar la interpretación, las decisiones o las conclusiones del análisis.

### Adecuación y límites de uso

La calidad de un modelo no depende únicamente de su complejidad o del número de variables que contiene. Depende de su adecuación a la pregunta, de la calidad de la información utilizada y de la claridad con la que se declaran sus límites. Además, la evidencia que respalda los datos y las relaciones no demuestra por sí sola que el modelo sea adecuado: incluso con mediciones correctas, una representación puede omitir una dependencia importante o describir insuficientemente el comportamiento relevante. Una lista de comprobación ayuda a examinar estas cuestiones, pero no garantiza que el modelo sea correcto.

Antes de utilizar una representación, conviene comprobar:

- **Propósito:** ¿qué pregunta pretende responder?
- **Alcance:** ¿qué elementos, relaciones y condiciones incluye?
- **Nivel de detalle:** ¿es suficiente para la tarea sin introducir complejidad innecesaria?
- **Supuestos:** ¿qué condiciones se dan por válidas y con qué justificación?
- **Omisiones:** ¿qué aspectos relevantes no están representados?
- **Evidencia de los datos y las relaciones:** ¿qué mediciones, especificaciones, estimaciones u observaciones respaldan los valores y vínculos utilizados?
- **Adecuación del modelo:** ¿hay razones para considerar que la representación recoge los aspectos y comportamientos relevantes para la pregunta planteada?
- **Límites de uso:** ¿en qué situaciones no deberíamos utilizar este modelo para extraer conclusiones?

Estas comprobaciones no eliminan la incertidumbre ni garantizan que el modelo sea correcto. Ayudan a evitar que una representación útil para una tarea se utilice fuera de su ámbito sin justificación.

### Revisar el modelo cuando cambia la pregunta o el sistema

Un modelo no debe considerarse definitivo. Puede necesitar ajustes cuando cambia el propósito del análisis, aparece nueva información, se detecta una relación omitida o el propio sistema evoluciona.

Si el objetivo pasa de estudiar el flujo de agua a evaluar la resiliencia del servicio, quizá debamos incorporar dependencias energéticas, capacidades de recuperación, personal, procedimientos y coordinación con proveedores. No se trata simplemente de añadir detalle: cambia qué aspectos son relevantes para responder a la nueva pregunta.

También puede ser necesario mantener varias representaciones complementarias. Un modelo hidráulico y otro socio-técnico pueden describir dimensiones diferentes de la misma infraestructura. Antes de combinarlos conviene comprobar que sus fronteras, supuestos, horizontes temporales, terminología y niveles de detalle son compatibles. De lo contrario, la combinación puede crear una apariencia de coherencia entre representaciones que cubren alcances distintos o se apoyan en decisiones incompatibles.

### Idea clave

Toda descripción de un sistema es un modelo selectivo. Su utilidad depende de que el alcance, los supuestos y las omisiones sean adecuados y explícitos respecto a la pregunta que pretende responder.

### Pregunta de reflexión

Piensa en un sistema que conozcas y en una representación que se utilice para describirlo. ¿Qué pregunta permite responder? ¿Qué supuestos incorpora? ¿Qué aspecto importante deja fuera? ¿En qué situación podría conducir a una conclusión incompleta si se utilizara más allá de su propósito original?

## 1.8. De la optimización de componentes al razonamiento a escala de sistema

### Mejorar una parte no siempre mejora el conjunto

En muchos sistemas, el rendimiento del conjunto depende de la contribución coordinada de múltiples componentes. Por eso, una mejora local no garantiza una mejora del sistema. Un componente puede funcionar con mayor eficiencia y, aun así, trasladar costes, restricciones o problemas a otras partes.

En una red de suministro de agua, sustituir una bomba por otra de mayor capacidad puede aumentar el caudal disponible en una estación. Sin embargo, también puede elevar el consumo energético, modificar las presiones en determinados tramos o exigir cambios en válvulas, conducciones y controles. Evaluar únicamente la bomba podría llevarnos a considerar exitosa la intervención sin comprobar sus consecuencias sobre el servicio completo.

La optimización de componentes sigue siendo necesaria. El problema aparece cuando el rendimiento local se toma como sustituto del rendimiento del sistema.

### Optimización local y razonamiento a escala de sistema

La **optimización local** busca mejorar uno o varios criterios de un componente o subsistema. El **razonamiento a escala de sistema** examina las consecuencias de las decisiones para el conjunto relevante, sus dependencias y el entorno que resulte pertinente para la decisión.

Razonar a escala de sistema no significa necesariamente resolver un problema matemático de optimización global. Tampoco implica que todos los criterios puedan maximizarse simultáneamente: algunos pueden entrar en conflicto.

| Foco de la decisión | Pregunta principal | Riesgo si se analiza de forma aislada |
|---|---|---|
| Componente | ¿Cómo puede funcionar mejor este equipo? | Mejorar su rendimiento a costa de otras partes |
| Subsistema | ¿Cómo coordinamos los elementos que realizan una función? | Desplazar una limitación relevante a otro subsistema |
| Sistema | ¿Cómo alcanza el conjunto los resultados requeridos? | Ignorar dependencias, efectos externos o consecuencias posteriores |

No se trata de elegir siempre el nivel más amplio. Se trata de seleccionar el nivel de análisis adecuado para la decisión y examinar las consecuencias relevantes en los niveles conectados.

### Restricciones, cuellos de botella e interdependencias

Una **restricción** es una condición que limita las alternativas disponibles, el rendimiento o los resultados posibles. Un **cuello de botella** es un elemento, capacidad o proceso cuya limitación restringe de forma significativa el rendimiento del conjunto respecto a un resultado determinado. Puede haber restricciones que no sean el factor limitante dominante, y un cuello de botella puede desplazarse cuando cambia la configuración del sistema.

Las mejoras locales pueden modificar las condiciones de funcionamiento de otras partes, incluso si estas no se intervienen directamente. A través de las relaciones, interfaces y dependencias, pueden cambiar los flujos, las cargas, la distribución de recursos o las necesidades de coordinación. Estos efectos pueden generar beneficios, costes o nuevos compromisos; también pueden producir sinergias y no deben suponerse necesariamente negativos.

En la red de agua, aumentar la capacidad de bombeo puede aliviar una limitación en la estación y hacer más relevante la capacidad de una conducción, una válvula o un depósito. También puede mejorar el suministro en una zona y, al mismo tiempo, aumentar el consumo energético o las necesidades de mantenimiento. El efecto depende de la configuración y de las relaciones entre las partes.

Por ello, conviene identificar qué elementos y funciones pueden verse afectados, qué dependencias condicionan el resultado, qué recursos adicionales podrían necesitarse y qué efectos indirectos podrían aparecer. No toda mejora local desplaza necesariamente un cuello de botella ni toda interdependencia produce un efecto adverso.

### Requisitos, objetivos de rendimiento y preferencias

El rendimiento de un sistema rara vez se resume en una única medida. Una red de agua puede evaluarse por la continuidad del suministro, la calidad, la presión, el consumo energético, los costes de operación, el tiempo de recuperación y los efectos ambientales. Mejorar un criterio puede perjudicar otro.

Para comparar alternativas conviene distinguir:

- **Requisitos:** condiciones que deben cumplirse para que el sistema o la solución sean aceptables.
- **Objetivos de rendimiento:** resultados que se busca alcanzar o mejorar, con distintos grados posibles de consecución.
- **Preferencias:** criterios utilizados para comparar alternativas que cumplen los requisitos aplicables, pero presentan compromisos diferentes.

Estas categorías no son intercambiables. El incumplimiento de un requisito obligatorio aplicable no queda compensado simplemente por mejores resultados en otros indicadores. Que un requisito sea obligatorio depende del marco de decisión y de las condiciones pertinentes.

Por ejemplo, mantener presiones elevadas puede facilitar el suministro en determinadas zonas, pero aumentar las pérdidas por fugas y el consumo energético. Reducir los costes de mantenimiento puede mejorar un indicador financiero a corto plazo y elevar el riesgo de interrupciones futuras. La decisión exige hacer explícitos los resultados buscados, las restricciones que deben respetarse y los compromisos aceptables.

### Efectos directos, indirectos y no deseados

Al evaluar una intervención, es útil distinguir entre:

- **Efectos directos:** consecuencias que se producen en el elemento o subsistema modificado.
- **Efectos indirectos:** consecuencias que aparecen en otras partes del sistema a través de relaciones, interfaces o dependencias.
- **Efectos no deseados:** consecuencias que perjudican resultados relevantes o generan riesgos que no se habían previsto, sean directas o indirectas.

Estas categorías pueden solaparse. Un efecto no deseado puede ser directo o indirecto. El análisis permite identificar consecuencias plausibles, pero no garantiza que todas puedan anticiparse; la observación posterior puede revelar efectos adicionales.

### Horizonte temporal de evaluación

Los resultados de una intervención también dependen del horizonte temporal considerado:

- **Corto plazo:** efectos inmediatos de la intervención y de su puesta en funcionamiento.
- **Medio plazo:** consecuencias que aparecen durante la operación y el ajuste o adaptación de las partes afectadas.
- **Largo plazo:** efectos acumulados, cambios en las necesidades, desgaste, mantenimiento y evolución del entorno.

Estos horizontes son referencias analíticas, no intervalos universales. Su duración depende del sistema, de la intervención y de la decisión evaluada. Una mejora inicial no debe presentarse como una mejora sostenida sin evidencia suficiente sobre su comportamiento posterior.

### Alcance y proporcionalidad del análisis

Razonar a escala de sistema no exige analizar todos los elementos, relaciones y consecuencias posibles. Exige identificar y examinar aquellos que son relevantes para la decisión. Para determinar la profundidad y amplitud necesarias, conviene considerar la importancia de los resultados afectados, la magnitud y probabilidad de las consecuencias, la incertidumbre de la información disponible, la reversibilidad de la intervención y las consecuencias de una decisión equivocada.

El análisis debe ser proporcional a la importancia y al riesgo de la decisión. También debe hacer explícitos la frontera y el alcance considerados, así como las incertidumbres que permanecen abiertas. Una intervención menor puede requerir una comprobación sencilla; un cambio crítico puede exigir un análisis más amplio y pruebas más rigurosas. Ampliar la frontera no siempre mejora el análisis: debe hacerse cuando aporta información relevante para la decisión.

### Razonar a escala de sistema

Un razonamiento a escala de sistema sitúa el detalle técnico dentro de una configuración de relaciones, objetivos, restricciones y condiciones de operación. Como orientación, puede seguir estas preguntas:

1. **¿Qué resultado se busca y para quién?** Precisar los resultados relevantes y las condiciones de aceptabilidad.
2. **¿Qué se va a modificar?** Delimitar el componente o subsistema objeto de la intervención.
3. **¿Qué otras partes están conectadas?** Examinar interfaces, dependencias e interacciones que puedan condicionar o recibir los efectos del cambio.
4. **¿Qué criterios y compromisos importan?** Distinguir requisitos, objetivos y preferencias, e identificar posibles conflictos.
5. **¿Qué efectos pueden aparecer y cuándo?** Considerar efectos directos, indirectos y no deseados, junto con horizontes temporales adecuados.
6. **¿Qué profundidad de análisis es proporcionada?** Tener en cuenta importancia, consecuencias, incertidumbre y reversibilidad, y declarar los límites del análisis.
7. **¿Qué debe comprobarse después?** Observar si los resultados previstos se mantienen y si aparecen consecuencias adicionales.

Estas preguntas no constituyen un método exhaustivo ni garantizan que se identifiquen todos los efectos. Ayudan a organizar el análisis alrededor de las consecuencias relevantes para la decisión.

### El valor de una mejora depende de dónde y cómo se manifiesta

Una mejora técnica adquiere sentido cuando se relaciona con los resultados que el sistema debe producir. Reducir el consumo de una bomba puede ser positivo, pero su relevancia depende de si se mantiene el servicio requerido, de cómo afecta a otros equipos y de qué costes o riesgos introduce.

Del mismo modo, una mejora del conjunto no tiene por qué maximizar todos los indicadores. Puede consistir en alcanzar un equilibrio justificable entre resultados, restricciones y necesidades diferentes. Hacer explícitos esos compromisos permite comparar alternativas sin presentar una preferencia particular como si fuera una solución universal.

La evaluación de alternativas y el análisis de decisiones en ingeniería de sistemas se desarrollan, entre otras fuentes, en NASA (2016, §6.8).

### Idea clave

Optimizar un componente no equivale a mejorar necesariamente el sistema. El razonamiento a escala de sistema examina las interdependencias, los requisitos, los objetivos, las restricciones, los efectos y los horizontes temporales relevantes. Su alcance debe ser proporcional a la decisión y sus límites e incertidumbres deben quedar explícitos.

### Pregunta de reflexión

Piensa en una mejora realizada o propuesta en un componente de un sistema que conozcas. ¿Qué indicador local pretendía mejorar? ¿Qué otras partes podían verse afectadas y de qué manera? ¿Qué requisitos, objetivos, preferencias y horizontes temporales habría que considerar para determinar si la intervención mejoró realmente el funcionamiento del sistema?

## 1.9. Síntesis y preguntas de reflexión

### Comprender un sistema como una configuración relacionada

Comprender un sistema no consiste únicamente en identificar sus componentes. Requiere relacionar el propósito que orienta su análisis con los elementos, actores, recursos y capacidades que intervienen; con las relaciones, interacciones y dependencias que los conectan; y con las condiciones del entorno y del contexto en las que el sistema opera. Estas dimensiones se condicionan mutuamente: una capacidad depende de recursos y relaciones, mientras que una modificación en una parte puede alterar las condiciones de otras.

Esta comprensión siempre se construye desde una perspectiva y para una pregunta determinadas. Por eso, describir un sistema exige decidir qué queda dentro y fuera de la frontera, qué interfaces e intercambios son relevantes, qué periodo se considera y qué nivel de detalle resulta adecuado. La representación selecciona información y puede combinar observaciones, estimaciones, especificaciones y supuestos. Distinguir lo conocido de lo desconocido y de lo omitido deliberadamente permite interpretar sus resultados sin atribuirle más alcance del que tiene.

El comportamiento se entiende observando cómo cambian los estados y cómo las relaciones entre las partes condicionan esos cambios a lo largo del tiempo. Del mismo modo, evaluar una intervención requiere ir más allá del componente modificado: hay que considerar dependencias, restricciones, efectos directos e indirectos, posibles compromisos entre criterios y consecuencias que pueden aparecer en distintos horizontes temporales. La profundidad del análisis debe ser proporcionada a la decisión y sus límites deben quedar explícitos.

### Una visión integrada

La tabla reúne dimensiones que conviene mantener conectadas al describir y analizar un sistema. Las preguntas orientan la exploración; la última columna muestra vínculos relevantes entre dimensiones. No es una lista exhaustiva ni un procedimiento obligatorio: su utilidad depende del sistema y del propósito del análisis.

| Dimensión | Pregunta orientadora | Qué ayuda a observar | Relación con otras dimensiones |
|---|---|---|---|
| Propósito y contexto | ¿Qué resultados importan, para quién y bajo qué condiciones? | Propósito del análisis y del sistema, actores y condiciones contextuales | Orienta la frontera, los criterios de rendimiento y la selección de información del modelo |
| Composición y capacidades | ¿Qué elementos, actores, recursos y capacidades intervienen? | Qué existe, qué puede aportar cada parte y de qué depende | Las capacidades se apoyan en recursos, relaciones e interfaces |
| Organización e interacciones | ¿Cómo se relacionan y coordinan las partes? | Flujos, dependencias, interfaces, autoridad y efectos entre componentes | Configura el comportamiento y condiciona las capacidades disponibles |
| Frontera y entorno | ¿Qué incluimos en el análisis y qué intercambios cruzan sus límites? | Entradas, salidas, dependencias externas e impactos relevantes | Determina qué relaciones se consideran internas o externas y qué contexto resulta pertinente |
| Tiempo y cambio | ¿Qué varía, cómo responde el sistema y en qué horizonte? | Estados, trayectorias, perturbaciones, respuestas y tendencias | Permite interpretar comportamientos y evaluar efectos de intervenciones a lo largo del tiempo |
| Modelo y evidencia | ¿Qué representa la descripción, en qué se basa y qué deja fuera? | Adecuación al propósito, datos, estimaciones, supuestos, omisiones e incertidumbre | Hace explícitos los límites con los que deben interpretarse las demás dimensiones |
| Rendimiento del conjunto | ¿Cómo afectan las decisiones a los resultados del sistema y a sus partes conectadas? | Requisitos, objetivos, restricciones, cuellos de botella, compromisos y efectos indirectos | Integra capacidades, interdependencias, criterios de evaluación y horizontes temporales |

### Aplicar la perspectiva a un sistema conocido

Elige un sistema que conozcas —una instalación, un servicio, un proceso organizativo o una infraestructura— y prepara una descripción breve que permita a otra persona comprenderlo. No es necesario construir un modelo formal ni evaluar exhaustivamente el sistema. Explicita:

1. **Propósito y pregunta:** para qué elaboras la descripción y qué cuestión quieres responder.
2. **Frontera y contexto:** qué incluyes, qué dejas fuera y qué elementos, actores, relaciones o condiciones consideras relevantes.
3. **Conocimiento y supuestos:** qué información conoces, qué valores o relaciones estás suponiendo y qué información falta o todavía no has examinado.
4. **Alcance y límites:** qué permite comprender tu descripción y qué conclusiones no sería válido extraer de ella.

Lo importante es justificar las decisiones de análisis y distinguir lo observado o respaldado de lo estimado, supuesto o todavía desconocido.

### Preguntas de reflexión

1. **Propósito, actores y frontera:** Imagina un servicio utilizado por varios grupos con necesidades distintas. ¿Cómo podrían esas perspectivas cambiar la definición de sus resultados relevantes y la frontera que conviene adoptar para analizarlo?
2. **Capacidades y dependencias:** Si una organización dispone de personal cualificado y equipos adecuados, pero depende de un proveedor externo para un recurso crítico, ¿qué permite afirmar que puede prestar el servicio y qué condiciones podrían limitar esa capacidad?
3. **Modelo, evidencia y tiempo:** Una descripción de un sistema se ha elaborado a partir de mediciones tomadas durante una semana. ¿Qué aspectos de su comportamiento podría representar adecuadamente y cuáles podrían quedar ocultos por el periodo observado, los supuestos o la información ausente?
4. **Interdependencias y rendimiento:** En una red de agua se aumenta la capacidad de bombeo para mejorar el suministro de una zona. ¿Qué otras partes podrían verse afectadas y cómo compararías los beneficios con los cambios en presión, consumo energético, mantenimiento y restricciones operativas?
5. **Intervención y evaluación temporal:** Antes de concluir que una intervención ha mejorado el sistema, ¿qué resultados y criterios habría que observar, durante qué horizontes temporales y con qué incertidumbres o efectos indirectos? ¿Qué evidencia permitiría distinguir una mejora inicial de una mejora sostenida?

### Cierre del capítulo

Pensar en sistemas significa comprender los componentes en relación con las capacidades, las interacciones y las condiciones que hacen posible su funcionamiento. La configuración de elementos, recursos y relaciones condiciona lo que un sistema puede hacer, así como las opciones de cambio que tiene a su alcance. Una descripción útil permite razonar sobre esas posibilidades sin confundir lo que se conoce con lo que se supone ni ocultar los límites del análisis.

El capítulo siguiente examinará la transformación como una cuestión relacionada con la capacidad del sistema: cómo puede cambiar y qué determina las transformaciones que están realmente a su alcance. No todo cambio constituye necesariamente una transformación, ni toda transformación genera por sí misma valor.


## Fuentes y lecturas complementarias

- Meadows, D. H. (2008). *Thinking in Systems: A Primer* (D. Wright, Ed.). Chelsea Green Publishing. ISBN 978-1-60358-055-7. [TV-REF-007]
- International Council on Systems Engineering (INCOSE). (2023). *Systems Engineering Handbook: A Guide for System Life Cycle Processes and Activities* (5th ed.; D. D. Walden, T. M. Shortell, G. J. Roedler, B. A. Delicado, O. Mornas, Y. Yew-Seng, & D. Endler, Eds.). John Wiley & Sons. INCOSE-TP-2003-002-05. ISBN 978-1-119-81429-0. [TV-REF-008]
- Hirshorn, S. R., Voss, L. D., & Bromley, L. K. (2016). *NASA Systems Engineering Handbook* (NASA/SP-2016-6105 Rev 2). National Aeronautics and Space Administration. [TV-REF-009]

These sources provide complementary foundations and further reading. They do not imply that every working definition or editorial distinction in this chapter is prescribed by the cited publications.