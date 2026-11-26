---
content_id: TV-CH-03
language_pair_id: TV-CH-03
title: "El espacio de transformaciones accesibles"
language: es
content_type: chapter
status: draft
version: 0.2
created: 2026-11-26
updated: 2026-11-26
authors: []
reviewers: []
summary: "Explica cómo representar las transformaciones que un sistema puede realizar bajo condiciones especificadas y por qué accesibilidad, ejecución, trayectoria, resultado y valor deben mantenerse diferenciados."
part: TV-P1
chapter: TV-CH-03
parent_id: TV-P1-OV
tags:
  - accessible-transformations
  - transformation-space
  - systems-engineering
concepts:
  - TV-TERM-001
prerequisites: []
related:
  - TV-CH-02
  - TV-CH-04
  - TV-CH-05
  - TV-CH-06
references: []
epistemic_status:
  - analytical_definition
  - bounded_empirical_evidence
  - open_hypothesis
source_assets:
  - 01_CORE/architecture/TGCV_CORE_v_current.md
  - 05_ASSETS/ARM/TGCV-EXT-ARM-001_v0.2.md
  - 03_EXPERIMENTS/TR-131/execution/TR131_TRANSFORMATION_SPACE_DYNAMICS_FORMAL_SPEC_001.md
  - 03_EXPERIMENTS/TR-131/execution/TR131_TRANSFORMATION_SPACE_DYNAMICS_ANALYSIS_001.md
  - 00_GOVERNANCE/EVIDENCE_TO_CLAIM_MATRIX_CURRENT.md
  - 00_GOVERNANCE/SIP/TGCV_CROSS_DOMAIN_END_TO_END_ACCESSIBILITY_OUTCOME_VALUE_MAP_001.md
license: null
---

# El espacio de transformaciones accesibles

## Propósito del capítulo

Un sistema no se define únicamente por lo que ha hecho. También importa qué transformaciones puede realizar bajo unas condiciones determinadas, aunque todavía no las haya realizado. Esta diferencia permite estudiar cómo cambian las posibilidades efectivas de un sistema y cómo esos cambios pueden relacionarse con sus trayectorias posteriores.

En este capítulo construiremos una representación analítica de esas posibilidades. Veremos cómo delimitar las transformaciones candidatas, qué significa que una transformación sea accesible, cómo puede cambiar el espacio de transformaciones y qué podemos —y qué no podemos— inferir de ese cambio.

La idea central es sencilla, pero sus consecuencias son importantes: **que una transformación sea accesible no significa que vaya a realizarse; que se realice no significa que produzca necesariamente un resultado valioso.**

### Objetivos de aprendizaje

Al terminar el capítulo podrás:

- distinguir transformaciones candidatas, accesibles y realizadas;
- explicar por qué la accesibilidad depende del estado del sistema y de condiciones relevantes;
- interpretar el espacio de transformaciones accesibles como una representación analítica, no como una causa independiente;
- describir cambios de composición, expansión, contracción y sustitución;
- separar evidencia de accesibilidad, realización, trayectoria, resultado y valor;
- reconocer los límites de las inferencias que pueden extraerse de estudios acotados.

## 1. ¿Por qué estudiar las transformaciones a las que puede acceder un sistema?

Imagina una organización que hasta ahora solo presta un servicio de forma presencial. En un momento dado incorpora una plataforma digital, forma a parte de su personal, obtiene autorización para operar en otro canal y adapta sus procesos. La organización todavía puede seguir atendiendo a sus clientes presencialmente. Sin embargo, ahora existen transformaciones que antes no estaban disponibles en las mismas condiciones: atender a distancia, coordinar equipos distribuidos o prestar determinados servicios fuera del horario habitual.

Si observáramos únicamente las actividades realizadas, podríamos describir qué ha hecho la organización. Pero no captaríamos por completo el cambio estructural que ha tenido lugar: algunas transformaciones han pasado a estar a su alcance.

La distinción es relevante en muchos tipos de sistemas. Una infraestructura puede habilitar nuevas formas de desplazamiento; una red de servicios puede hacer accesibles nuevas operaciones financieras; un sistema de software puede incorporar nuevas funciones; una persona puede adquirir capacidades que amplían las tareas que puede desempeñar.

En todos estos casos conviene separar dos preguntas:

1. ¿Qué transformaciones ha realizado el sistema?
2. ¿Qué transformaciones podía realizar bajo las condiciones consideradas, con independencia de que llegara a realizarlas?

La segunda pregunta no es una lista de deseos ni un catálogo ilimitado de posibilidades imaginables. Se refiere a transformaciones definidas con suficiente precisión y cuya accesibilidad puede analizarse atendiendo al sistema y a sus condiciones.

Estudiar ese espacio permite describir una dimensión del cambio que no queda reducida a la actividad observada. También ayuda a evitar un error frecuente: inferir lo que un sistema podía hacer a partir de lo que finalmente hizo. Una transformación realizada puede ser una evidencia relevante, pero no describe por sí sola todas las alternativas que estaban disponibles.

## 2. De las transformaciones candidatas a las accesibles

El punto de partida es un conjunto de transformaciones candidatas. Una transformación candidata, que representaremos por \(\tau\), describe un cambio identificable que podría producirse en el sistema. Su formulación debe ser suficientemente concreta para que podamos preguntar qué condiciones permitirían realizarla.

No toda transformación imaginable debe incorporarse al análisis. El universo de candidatas se delimita en función del sistema estudiado, la pregunta de investigación y el nivel de detalle necesario. En algunos casos será posible enumerar las alternativas relevantes. En otros, bastará con definir una familia de transformaciones y un procedimiento explícito para identificar cuáles cumplen las condiciones de accesibilidad.

Una transformación es accesible cuando se satisfacen las condiciones relevantes para su realización. En el modelo analítico actual, el espacio se representa como una función del estado del sistema y de las condiciones y restricciones pertinentes:

\[
T_{acc}=F(S,C,L)
\]

Aquí, (S) representa el estado o configuración relevante del sistema; (C), las condiciones contextuales consideradas; y (L), las restricciones, recursos y condiciones operativas que intervienen en el análisis. La notación no pretende convertir cada elemento en una entidad independiente: expresa que la accesibilidad se evalúa en relación con una configuración y unas condiciones especificadas.

Para cada transformación candidata puede definirse un predicado de accesibilidad:

\[
\tau \in T_{acc} \quad \text{si y solo si} \quad P_{\tau}(S,C,L)=1
\]

El predicado debe establecerse de manera independiente de los resultados posteriores. No sería válido definir una transformación como accesible simplemente porque observamos que tuvo éxito, ni concluir que estaba disponible porque el sistema acabó obteniendo un resultado favorable. Eso introduciría razonamiento retrospectivo y confundiría las condiciones de partida con lo que ocurrió después.

La accesibilidad puede depender de varias dimensiones:

- **Capacidad y conocimiento:** el sistema dispone de las competencias o del conocimiento necesarios.
- **Recursos:** existen los medios materiales, financieros, energéticos o informativos requeridos.
- **Permisos y autoridad:** las reglas e instituciones permiten realizar la transformación.
- **Condiciones técnicas:** los componentes, interfaces e infraestructuras necesarios funcionan conjuntamente.
- **Preparación operativa:** la transformación puede llevarse a cabo en las condiciones reales del caso, no solo en teoría.

Estas dimensiones no constituyen una lista universal ni una fórmula automática. Su relevancia depende de la transformación y del sistema. Una opción técnicamente viable puede no ser prácticamente accesible si faltan autorización, coordinación, recursos o disponibilidad temporal. A la inversa, una transformación puede estar disponible aunque el sistema no la haya elegido todavía.

Por eso es importante declarar el criterio de accesibilidad antes de examinar los resultados. El análisis debe explicar qué cuenta como transformación, qué condiciones son necesarias y cómo se determina que se cumplen.

## 3. El espacio de transformaciones accesibles

Una vez delimitadas las transformaciones candidatas y definido el criterio de accesibilidad, podemos representar el conjunto —o estructura— de transformaciones que el sistema puede realizar bajo las condiciones consideradas. A esa representación la llamamos **espacio de transformaciones accesibles**, y la expresamos como (T_{acc}).

La palabra *espacio* no implica necesariamente un espacio geométrico ni una colección que deba enumerarse por completo. Designa una estructura analítica de posibilidades delimitadas. Según el dominio, esa estructura podrá representarse mediante conjuntos, relaciones, funciones, estados de admisibilidad u otras formas adecuadas.

Su contenido depende de tres decisiones metodológicas:

1. **Delimitación del sistema:** qué elementos y relaciones forman parte de la unidad analizada.
2. **Universo de transformaciones candidatas:** qué cambios se consideran relevantes para la pregunta.
3. **Regla de accesibilidad:** qué condiciones deben cumplirse para considerar disponible cada transformación.

Estas decisiones deben ser explícitas y justificables. No siempre será posible observar directamente todas las condiciones relevantes ni identificar todas las transformaciones concebibles. La ausencia de una enumeración exhaustiva no invalida automáticamente el análisis, pero obliga a declarar su alcance y las transformaciones que quedan fuera.

El espacio de transformaciones accesibles es una representación derivada del estado y de las condiciones relevantes. No es una fuerza adicional que actúe sobre el sistema ni un componente ontológico independiente. Su utilidad reside en hacer analíticamente visible qué cambios están disponibles bajo una configuración determinada.

Tampoco debe confundirse con una medida general de capacidad. Un sistema puede tener muchas transformaciones accesibles en un dominio y estar severamente limitado en otro. La cantidad, la diversidad, la importancia y la distribución de las transformaciones son cuestiones diferentes. Para interpretarlas necesitamos conocer el significado de cada transformación y el contexto en el que puede realizarse.

## 4. Accesibilidad no significa ejecución

Consideremos un sistema que puede realizar cuatro transformaciones: (A), (B), (C) y (D). Que las cuatro formen parte de su espacio accesible no significa que vaya a realizar las cuatro. Puede elegir (B), no actuar, posponer una decisión o realizar una transformación distinta en otro momento.

Conviene mantener separados cinco niveles:

1. **Accesibilidad:** qué transformaciones están disponibles bajo las condiciones especificadas.
2. **Realización:** qué transformación ocurre efectivamente.
3. **Trayectoria:** qué secuencia de transformaciones realizadas y estados sucesivos se observa.
4. **Resultado:** qué consecuencia específica aparece en el dominio considerado.
5. **Valor:** cómo se evalúa esa consecuencia atendiendo a criterios, actores y horizontes temporales pertinentes.

Ningún nivel debe definirse retrospectivamente a partir del siguiente. La realización de una transformación puede confirmar que ciertas condiciones se dieron en ese caso, pero no permite reconstruir automáticamente todo el espacio de alternativas. Del mismo modo, un resultado favorable no demuestra por sí solo que todas las transformaciones previas fueran accesibles ni que una modificación concreta del espacio causara ese resultado.

La diferencia también opera en sentido inverso. Una transformación puede ser accesible y no realizarse por falta de demanda, por una decisión deliberada, por incertidumbre, por costes de oportunidad o porque el sistema prioriza otra trayectoria. La no realización no demuestra necesariamente que la transformación fuera inaccesible.

En algunos dominios también es necesario distinguir la **adopción o utilización** de un servicio o una capacidad de su disponibilidad estructural. Que una infraestructura o un servicio estén disponibles no significa que las personas u organizaciones los utilicen. La utilización observada puede ser relevante para estudiar una trayectoria o un resultado, pero no debe emplearse automáticamente para definir qué transformaciones eran accesibles.

Esta separación evita dos errores simétricos: tratar toda posibilidad como si fuera una acción y tratar toda acción observada como si agotara las posibilidades del sistema.

## 5. Cómo puede cambiar un espacio accesible

El espacio de transformaciones accesibles no tiene por qué permanecer constante. Puede cambiar cuando se modifica el estado del sistema o alguna de las condiciones relevantes. El cambio puede adoptar distintas formas:

- **Expansión:** aparecen transformaciones accesibles que antes no lo eran.
- **Contracción:** algunas transformaciones dejan de estar disponibles.
- **Reconfiguración:** cambia la composición del espacio, aunque su tamaño total permanezca igual.
- **Sustitución:** unas transformaciones dejan de ser accesibles y otras ocupan su lugar.

En ocasiones se habla de **posibilidades latentes** para referirse a transformaciones que ya son accesibles, pero todavía no se han realizado. El término debe usarse con cuidado: no designa una capacidad misteriosa ni una posibilidad meramente imaginable. Solo tiene sentido si las condiciones de accesibilidad pueden justificarse de forma independiente. Una transformación que se vuelve accesible por primera vez puede describirse como recién habilitada; una que deja de cumplir las condiciones relevantes deja de formar parte del espacio accesible.

Por ejemplo, supongamos que en un primer momento el sistema tiene accesibles las transformaciones (A), (B), (C) y (D). Más adelante, (C) y (D) dejan de estar disponibles, mientras que (E) y (F) pasan a ser accesibles:

\[
T_{acc,t}=\{A,B,C,D\}
\]
\[
T_{acc,t+1}=\{A,B,E,F\}
\]

Ambos espacios contienen cuatro transformaciones. Si observáramos únicamente su tamaño, concluiríamos que nada ha cambiado. Sin embargo, la composición es diferente: dos transformaciones persisten, dos desaparecen y dos nuevas se incorporan. Ha habido reconfiguración con conservación de cardinalidad.

Esta observación introduce una distinción importante: **el número de transformaciones no describe por sí solo la identidad ni la estructura del espacio**. Dos espacios de igual tamaño pueden contener transformaciones diferentes. Y un aumento del número no implica necesariamente una mejora: las nuevas transformaciones podrían ser irrelevantes, costosas, perjudiciales o menos valiosas para determinados actores.

En análisis donde las transformaciones pueden identificarse de forma consistente, es útil distinguir:

- transformaciones añadidas;
- transformaciones retiradas;
- transformaciones que persisten;
- cambio neto en el número de elementos;
- volumen de sustitución o rotación de identidades.

Estas son descripciones estructurales, no puntuaciones de calidad. La forma adecuada de compararlas depende de cómo se definan las identidades de transformación en cada dominio. No debe suponerse que dos etiquetas distintas representan necesariamente transformaciones distintas, ni que etiquetas iguales garantizan equivalencia semántica.

## 6. Observar la dinámica del espacio de transformaciones

Para estudiar la evolución temporal podemos comparar el espacio accesible en dos momentos sucesivos. Una secuencia analítica útil es:

\[
S_t \rightarrow T_{acc,t} \rightarrow T_{real,t}
\rightarrow S_{t+1} \rightarrow T_{acc,t+1}
\]

La secuencia distingue el estado inicial, las transformaciones accesibles, la transformación que efectivamente se realiza, el estado resultante y el espacio accesible bajo las nuevas condiciones.

Las flechas organizan la observación; no deben interpretarse como una ley causal universal. En particular, la relación entre una transformación realizada, el estado sucesor y la accesibilidad posterior debe examinarse en cada caso. La representación permite formular preguntas y contrastar relaciones, pero no sustituye la evidencia necesaria para responderlas.

Cuando las transformaciones pueden identificarse entre momentos, podemos describir el cambio mediante un pequeño conjunto de cantidades. Si (A_t) representa el número de transformaciones accesibles al inicio, (G_t) las identidades añadidas, (L_t) las retiradas y (P_t) las persistentes, entonces el cambio neto de tamaño es la diferencia entre el número de elementos del espacio sucesor y el inicial. La rotación de identidades, en cambio, recoge las incorporaciones y retiradas consideradas conjuntamente.

No es necesario reducir toda la dinámica a un único indicador. De hecho, hacerlo puede ocultar diferencias relevantes. Un sistema puede mantener el mismo número de transformaciones y, aun así, experimentar una sustitución profunda. Otro puede ampliar el espacio incorporando opciones que apenas modifican las trayectorias que realmente puede seguir. La selección de descriptores debe responder a la pregunta analítica, a la calidad de los datos y a la semántica del dominio.

La comparación entre dominios exige una precaución adicional. Puede ser posible utilizar la misma estructura analítica en sistemas diferentes sin asumir que sus transformaciones concretas son equivalentes. La consistencia debe buscarse en el papel que desempeñan los conceptos —estado, accesibilidad, realización, estado sucesor— y no en imponer etiquetas idénticas a fenómenos distintos.

## 7. Qué muestra la evidencia acotada y qué no demuestra

La evidencia disponible permite ilustrar distintos niveles de apoyo, que conviene no mezclar.

**Operacionalización en dos dominios computacionales.** Un estudio acotado reconstruyó 36 registros de transición en dos dominios estructuralmente diferentes. La validación no encontró registros inválidos y una auditoría matemática independiente no encontró discrepancias en los descriptores calculados. En ambos dominios se observaron cambios en la identidad de las transformaciones accesibles. En uno de ellos hubo sustitución de identidades sin cambio en el número total de transformaciones. Este resultado respalda que una representación común de transición puede operacionalizar cambios del espacio en esos casos examinados. No demuestra que la representación sea universal, superior a otras ni válida en cualquier dominio.

**Evidencia causal acotada sobre trayectorias posteriores.** En un estudio de expansión aleatorizada de una red de servicios financieros rurales, la intervención modificó la infraestructura local y el acceso estructural a determinados servicios. La evidencia consolidada ofrece apoyo causal acotado a que los cambios de accesibilidad pueden afectar trayectorias posteriores en ese contexto. El resultado debe mantenerse dentro de los límites del estudio: no establece una ley general ni demuestra que el cambio de accesibilidad produzca necesariamente valor.

**Un caso de identificación parcial.** En la reconstrucción de una intervención de pavimentación urbana se pudieron especificar de antemano funciones candidatas —como facilitar desplazamientos de vehículos, peatones o bicicletas— y reconstruir cambios longitudinales de conectividad. Sin embargo, los datos no permitieron identificar de forma independiente el predicado completo de accesibilidad ni reconstruir todo el espacio de transformaciones. El caso muestra por qué un cambio físico observado no equivale automáticamente a una modificación identificada de (T_{acc}).

**Una ilustración sintética de no equivalencia.** En un entorno sintético controlado, una intervención modificó el espacio accesible mientras la trayectoria realizada especificada permanecía igual y el resultado de valor definido para ese ejercicio no cambiaba. Esta ilustración sirve para mostrar que los niveles analíticos pueden variar de manera independiente bajo determinadas reglas. No es evidencia de comportamiento real ni demuestra que las modificaciones de accesibilidad carezcan de efectos sobre trayectorias o valor en general.

En conjunto, estos resultados respaldan algunas operaciones y relaciones delimitadas. No demuestran una teoría universal de la dinámica de transformaciones, ni establecen que todo cambio de accesibilidad modifique una trayectoria, ni resuelven la relación entre accesibilidad y valor.

## 8. Límites, supuestos y preguntas abiertas

El análisis del espacio de transformaciones accesibles depende de decisiones que deben hacerse visibles.

**Delimitación del sistema.** Si los límites del sistema son inadecuados, pueden omitirse condiciones externas decisivas o atribuirse al sistema capacidades que dependen de otros actores e infraestructuras.

**Identidad de las transformaciones.** Para comparar espacios a lo largo del tiempo necesitamos saber cuándo una transformación persiste, cuándo cambia y cuándo debe considerarse una transformación distinta. Esta decisión no siempre es trivial.

**Criterio de accesibilidad.** El predicado debe ser independiente de la realización y de los resultados posteriores. Si se construye a partir de lo que ocurrió, el análisis corre el riesgo de ser circular.

**Cierre operacional.** No siempre es posible enumerar todas las transformaciones concebibles. El análisis debe declarar qué universo se ha considerado, por qué resulta adecuado y qué queda fuera.

**Heterogeneidad entre dominios.** Una estructura analítica común no implica que los mecanismos, las transformaciones o sus significados sean iguales en todos los sistemas. La generalidad debe probarse, no presuponerse.

**Relación con las trayectorias.** Existe evidencia causal acotada de que cambios de accesibilidad pueden afectar trayectorias posteriores en un contexto estudiado. La generalidad de esa relación y las condiciones bajo las cuales se mantiene siguen siendo cuestiones abiertas.

**Relación con el valor.** El valor requiere una evaluación adicional: qué resultados cuentan, para quién, con qué criterios y en qué horizonte temporal. Que una transformación sea accesible, o incluso que se realice, no determina por sí mismo el valor de sus consecuencias. La relación causal o predictiva entre cambios en el espacio accesible y cambios en el valor continúa abierta.

Estas limitaciones no hacen inútil el concepto. Definen las condiciones bajo las cuales puede utilizarse de forma rigurosa y señalan qué evidencia adicional sería necesaria.

## 9. Síntesis y reflexión

El espacio de transformaciones accesibles representa qué transformaciones puede realizar un sistema bajo un estado y unas condiciones especificadas. Se deriva de la configuración relevante del sistema y de un criterio explícito de accesibilidad; no es una causa independiente ni una lista ilimitada de posibilidades imaginables.

Su composición puede cambiar mediante expansión, contracción, reconfiguración o sustitución. Por eso, observar únicamente el número de transformaciones puede ser insuficiente: también importa qué transformaciones aparecen, cuáles desaparecen y cuáles permanecen.

La distinción fundamental debe conservarse a lo largo de todo el análisis:

**accesibilidad no es realización; realización no es trayectoria; trayectoria no es resultado; resultado no es automáticamente valor.**

La evidencia disponible aporta apoyo acotado a la operacionalización del espacio y a determinadas relaciones con trayectorias posteriores. No autoriza a generalizar esos resultados a todos los sistemas ni a afirmar que la ampliación de posibilidades produce necesariamente valor.

### Preguntas para la reflexión

1. Piensa en un sistema que conozcas. ¿Qué transformaciones puede realizar hoy que no podía realizar hace un año? ¿Qué condiciones cambiaron?
2. ¿Cómo distinguirías una transformación técnicamente posible de una transformación realmente accesible en las condiciones del sistema?
3. ¿Podría cambiar profundamente el espacio accesible sin variar el número total de transformaciones? Construye un ejemplo.
4. ¿Qué información necesitarías para determinar si una transformación estaba accesible antes de que se realizara?
5. ¿Qué errores cometerías si utilizaras los resultados observados para definir retrospectivamente la accesibilidad?
6. ¿Qué evidencia adicional sería necesaria para afirmar que un cambio en el espacio accesible contribuyó a crear valor?

### Transición al siguiente capítulo

El espacio accesible depende de condiciones, recursos, relaciones y restricciones. El siguiente capítulo examina esos elementos con mayor detalle y muestra cómo interactúan para habilitar o limitar las transformaciones de un sistema.

## Referencias y lecturas adicionales

Las referencias bibliográficas completas de los estudios empíricos descritos y de los trabajos conceptuales de apoyo se incorporarán tras verificar sus registros primarios y su pertinencia para una edición pública. Esta versión es un borrador de trabajo, no una versión aprobada para publicación.
