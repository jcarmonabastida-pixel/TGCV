---
content_id: TV-CH-03
language_pair_id: TV-CH-03
title: "El espacio de transformaciones accesibles"
language: es
content_type: chapter
status: draft
version: 0.15
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
  - TV-LR-001
  - TV-LR-002
references:
  - TV-REF-001
  - TV-REF-002
  - TV-REF-003
  - TV-REF-006
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
  - 00_GOVERNANCE/rma/TGCV_RMA_v3.38.md
  - 00_GOVERNANCE/SIP/TGCV_C09_CLAIM_LEVEL_CONSOLIDATION_RECORD_001.md
  - 00_GOVERNANCE/SIP/C10C002_BOUNDED_CAUSAL_EXPERIMENT_CLOSURE_001.md
  - 00_GOVERNANCE/SIP/TGCV_MT5_DYNAMIC_TRANSFORMATION_SPACE_RECONSTRUCTION_RESULT_001.md
  - 03_EXPERIMENTS/EXT-1.1_Rust/execution/RUST-DYN-2_SCIENTIFIC_INTEGRATION_CLOSURE_v01.md
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

Imagina una organización que hasta ahora solo presta un servicio de forma presencial. En un momento dado incorpora una plataforma digital, forma a parte de su personal, obtiene autorización para operar en otro canal y adapta sus procesos. La organización todavía puede seguir atendiendo a sus clientes presencialmente. Sin embargo, estos cambios pueden ampliar las transformaciones a las que la organización tiene acceso. Por ejemplo, podrían hacer viable la atención a distancia, la coordinación de equipos distribuidos o la prestación de determinados servicios fuera del horario habitual. Que cada una de estas transformaciones sea realmente accesible dependerá de que se satisfagan las condiciones específicas necesarias para llevarla a cabo: no basta con disponer de una plataforma o de una autorización si faltan capacidades, recursos o integración operativa.

Si observáramos únicamente las actividades realizadas, podríamos describir qué ha hecho la organización. Pero no captaríamos por completo el cambio estructural que ha tenido lugar: algunas transformaciones han pasado a estar a su alcance.

La distinción es relevante en muchos tipos de sistemas. Una infraestructura puede habilitar nuevas formas de desplazamiento; una red de servicios puede hacer accesibles nuevas operaciones financieras; un sistema de software puede incorporar nuevas funciones; una persona puede adquirir capacidades que amplían las tareas que puede desempeñar.

En todos estos casos conviene separar dos preguntas:

1. ¿Qué transformaciones ha realizado el sistema?
2. ¿Qué transformaciones podía realizar bajo las condiciones consideradas, con independencia de que llegara a realizarlas?

La segunda pregunta no es una lista de deseos ni un catálogo ilimitado de posibilidades imaginables. Se refiere a transformaciones definidas con suficiente precisión y cuya accesibilidad puede analizarse atendiendo al sistema y a sus condiciones.

Estudiar ese espacio permite describir una dimensión del cambio que no queda reducida a la actividad observada. También ayuda a evitar un error frecuente: inferir lo que un sistema podía hacer a partir de lo que finalmente hizo. Una transformación realizada puede ser una evidencia relevante, pero no describe por sí sola todas las alternativas que estaban disponibles.

## 2. De las transformaciones candidatas a las accesibles

El punto de partida es un conjunto de transformaciones candidatas. Una transformación candidata, que representaremos por \(\tau\), describe un cambio identificable que podría producirse en el sistema. Su formulación debe ser suficientemente concreta para que podamos preguntar qué condiciones permitirían realizarla.

No toda transformación imaginable debe incorporarse al análisis. El universo de candidatas se delimita en función del sistema estudiado, la pregunta de investigación y el nivel de detalle necesario. También deben declararse la frontera del sistema, el horizonte temporal y la granularidad con la que se describe cada transformación, porque estos parámetros condicionan qué alternativas entran en el análisis y cómo se comparan. En algunos casos será posible enumerar las alternativas relevantes. En otros, bastará con definir una familia de transformaciones y un procedimiento explícito para identificar cuáles cumplen las condiciones de accesibilidad.

Una transformación es accesible cuando se satisfacen las condiciones relevantes para su realización. En el modelo analítico actual, el espacio se representa como una función del estado del sistema y de las condiciones y restricciones pertinentes:

\[
T_{acc}=F(S,C,L)
\]

Aquí, \(S\) representa el estado o configuración relevante del sistema; \(C\), las condiciones contextuales consideradas; y \(L\), las restricciones, los recursos y las condiciones operativas que intervienen en el análisis. El estado del sistema constituye el punto de partida ontológico. Las condiciones contextuales y los elementos recogidos en \(L\) se incorporan para evaluar la accesibilidad en cada caso; no se postulan como entidades ontológicas independientes ni deben confundirse con el propio espacio de transformaciones.

Para cada transformación candidata puede definirse un predicado de accesibilidad:

\[
\tau \in T_{acc} \quad \text{si y solo si} \quad P_{\tau}(S,C,L)=1
\]

El predicado debe establecerse de manera independiente de los resultados posteriores. No sería válido definir una transformación como accesible simplemente porque observamos que tuvo éxito, ni concluir que estaba disponible porque el sistema acabó obteniendo un resultado favorable. Eso introduciría razonamiento retrospectivo y confundiría las condiciones de partida con lo que ocurrió después.

El predicado expresa una condición de accesibilidad, pero la evidencia disponible puede no permitir evaluarla de forma concluyente. En la práctica, el análisis debe distinguir entre una transformación cuya accesibilidad se ha establecido, otra cuya falta de accesibilidad se ha establecido y una tercera cuya condición no puede determinarse con la información disponible. Esta última situación no equivale a asignar al predicado un valor de cero: indica que no se ha podido establecer si la condición se cumple. La ausencia de evidencia suficiente no debe interpretarse automáticamente como evidencia de ausencia de accesibilidad.

La accesibilidad puede depender de varias dimensiones:

- **Capacidad y conocimiento:** el sistema dispone de las competencias o del conocimiento necesarios.
- **Recursos:** existen los medios materiales, financieros, energéticos o informativos requeridos.
- **Permisos y autoridad:** las reglas e instituciones permiten realizar la transformación.
- **Condiciones técnicas:** los componentes, interfaces e infraestructuras necesarios funcionan conjuntamente.
- **Preparación operativa:** la transformación puede llevarse a cabo en las condiciones reales del caso, no solo en teoría.

Estas dimensiones no constituyen una lista universal ni una fórmula automática. Su relevancia depende de la transformación y del sistema. Una opción técnicamente viable puede no ser prácticamente accesible si faltan autorización, coordinación, recursos o disponibilidad temporal. A la inversa, una transformación puede estar disponible aunque el sistema no la haya elegido todavía.

Por eso es importante declarar el criterio de accesibilidad antes de examinar los resultados. El análisis debe explicar qué cuenta como transformación, qué condiciones son necesarias y cómo se determina que se cumplen.

## 3. El espacio de transformaciones accesibles

Una vez delimitadas las transformaciones candidatas y definido el criterio de accesibilidad, podemos representar el conjunto —o estructura— de transformaciones que están disponibles para su realización bajo las condiciones consideradas. A esa representación la llamamos **espacio de transformaciones accesibles**, y la expresamos como \\(T_{acc}\\).

La palabra *espacio* no implica necesariamente un espacio geométrico ni una colección que deba enumerarse por completo. Designa una estructura analítica de posibilidades delimitadas. Según el dominio, esa estructura podrá representarse mediante conjuntos, relaciones, funciones, estados de admisibilidad u otras formas adecuadas.

En las representaciones basadas en conjuntos, las transformaciones accesibles se tratan como elementos identificables de \\(T_{acc}\\). En otros dominios puede ser necesario representar también relaciones, dependencias o restricciones entre ellas. La elección depende de la estructura del sistema y de la pregunta analítica; no debe suponerse que una representación basada únicamente en la pertenencia a un conjunto recoge toda la información relevante.

Su contenido depende de tres decisiones metodológicas:

1. **Delimitación del sistema:** qué elementos y relaciones forman parte de la unidad analizada.
2. **Universo de transformaciones candidatas:** qué cambios se consideran relevantes para la pregunta.
3. **Regla de accesibilidad:** qué condiciones deben cumplirse para considerar disponible cada transformación.

Estas decisiones deben ser explícitas y justificables. No siempre será posible observar directamente todas las condiciones relevantes ni identificar todas las transformaciones concebibles. La ausencia de una enumeración exhaustiva no invalida automáticamente el análisis, pero obliga a declarar su alcance y las transformaciones que quedan fuera.

El espacio de transformaciones accesibles es una representación derivada del estado y de las condiciones relevantes. No es una fuerza adicional que actúe sobre el sistema ni un componente ontológico independiente. Su utilidad reside en hacer analíticamente visible qué cambios están disponibles bajo una configuración determinada.

Tampoco debe confundirse con una medida general de capacidad. Un sistema puede tener muchas transformaciones accesibles en un dominio y estar severamente limitado en otro. La cantidad, la diversidad, la importancia y la distribución de las transformaciones son cuestiones diferentes. Para interpretarlas necesitamos conocer el significado de cada transformación y el contexto en el que puede realizarse. Incluso la comparación del número de transformaciones requiere cautela: depende de cómo se haya delimitado el universo candidato y de cómo se identifiquen y agrupen las transformaciones. Una mayor cardinalidad bajo una representación no implica necesariamente una mayor capacidad del sistema.

## 4. Accesibilidad no significa ejecución

Consideremos un sistema que tiene disponibles cuatro transformaciones: \\(A\\), \\(B\\), \\(C\\) y \\(D\\). Que las cuatro formen parte de su espacio accesible no significa que vaya a realizar ninguna de ellas. Puede elegir \\(B\\), no actuar, posponer una decisión o seguir otra trayectoria.

Conviene mantener separados cinco niveles analíticos relacionados entre sí, pero no equivalentes:

1. **Accesibilidad:** qué transformaciones están disponibles bajo las condiciones especificadas.
2. **Realización:** qué transformación ocurre efectivamente.
3. **Trayectoria:** qué secuencia de transformaciones realizadas y estados sucesivos se observa.
4. **Resultado:** qué consecuencia específica aparece en el dominio considerado.
5. **Valor:** cómo se evalúa esa consecuencia atendiendo a criterios, actores y horizontes temporales pertinentes.

Ningún nivel debe definirse retrospectivamente a partir del siguiente. La realización observada de una transformación aporta evidencia de que pudo llevarse a cabo bajo las condiciones concretas de ese caso. Sin embargo, no permite reconstruir automáticamente todo el espacio de alternativas ni demuestra, por sí sola, que el criterio de accesibilidad se haya especificado correctamente. Del mismo modo, un resultado favorable no demuestra que todas las transformaciones previas fueran accesibles ni que una modificación concreta del espacio causara ese resultado.

La diferencia también opera en sentido inverso. Una transformación puede ser accesible y no realizarse por falta de demanda, por una decisión deliberada, por incertidumbre, por costes de oportunidad o porque el sistema prioriza otra trayectoria. La no realización no demuestra necesariamente que la transformación fuera inaccesible.

En algunos dominios también es necesario distinguir la **adopción o utilización** de un servicio o una capacidad de su disponibilidad estructural. Que una infraestructura o un servicio estén disponibles no significa que las personas u organizaciones los utilicen. La utilización observada puede ser relevante para estudiar una trayectoria o un resultado, pero no debe emplearse automáticamente para definir qué transformaciones eran accesibles.

Esta separación evita dos errores simétricos: tratar toda posibilidad como si fuera una acción y tratar toda acción observada como si agotara las posibilidades del sistema.

## 5. Cómo puede cambiar un espacio accesible

El espacio de transformaciones accesibles no tiene por qué permanecer constante. Puede cambiar cuando se modifica el estado del sistema o alguna de las condiciones relevantes. El cambio puede describirse atendiendo a distintas dimensiones, que no son necesariamente excluyentes:

- **Expansión:** se incorporan transformaciones que antes no eran accesibles.
- **Contracción:** algunas transformaciones dejan de estar disponibles.
- **Reconfiguración:** cambia la composición del espacio, con independencia de que su tamaño total aumente, disminuya o permanezca igual.
- **Sustitución:** unas transformaciones dejan de ser accesibles mientras otras se incorporan.

En ocasiones se habla de **posibilidades latentes** para referirse a transformaciones que ya forman parte del espacio accesible, pero todavía no se han realizado. El término debe utilizarse con cuidado: no designa una capacidad misteriosa ni una posibilidad meramente imaginable. Solo tiene sentido cuando las condiciones que hacen accesible la transformación pueden justificarse de forma independiente de su realización. Una transformación que se incorpora al espacio accesible puede describirse como recién habilitada; una que deja de cumplir las condiciones relevantes deja de formar parte de él.

Por ejemplo, supongamos que en un primer momento el sistema tiene accesibles las transformaciones \\(A\\), \\(B\\), \\(C\\) y \\(D\\). Más adelante, \\(C\\) y \\(D\\) dejan de estar disponibles, mientras que \\(E\\) y \\(F\\) pasan a ser accesibles:

\\[
T_{acc,t}=\\{A,B,C,D\\}
\\]
\\[
T_{acc,t+1}=\\{A,B,E,F\\}
\\]

Ambos espacios contienen cuatro transformaciones. Si comparáramos únicamente sus cardinalidades, concluiríamos que el tamaño del espacio no ha cambiado. Sin embargo, esa comparación ocultaría una modificación de su composición: dos transformaciones persisten, dos desaparecen y dos nuevas se incorporan. Ha habido reconfiguración con conservación de cardinalidad.

Esta observación introduce una distinción importante: **el número de transformaciones no describe por sí solo la identidad ni la estructura del espacio**. Dos espacios de igual tamaño pueden contener transformaciones diferentes. Un aumento del número de transformaciones accesibles tampoco permite concluir que el cambio sea favorable. Las nuevas opciones podrían tener escasa relevancia, exigir recursos adicionales o producir consecuencias desfavorables para determinados actores. Su valoración requiere un análisis posterior que no puede deducirse de la mera expansión del espacio.

En análisis donde las transformaciones pueden identificarse de forma consistente, es útil distinguir:

- transformaciones añadidas;
- transformaciones retiradas;
- transformaciones que persisten;
- cambio neto en el número de elementos;
- volumen de sustitución o rotación de identidades.

Estas son descripciones estructurales, no puntuaciones de calidad. La forma adecuada de compararlas depende de cómo se definan las identidades de transformación en cada dominio. No debe suponerse que dos etiquetas distintas representan necesariamente transformaciones distintas, ni que etiquetas iguales garantizan equivalencia semántica.

## 6. Observar la dinámica del espacio de transformaciones

Para estudiar la evolución temporal podemos comparar el espacio accesible en dos momentos sucesivos. Una secuencia analítica útil es:

\\[
(S_t,C_t,L_t)\\rightarrow T_{acc,t}
\\]

\\[
T_{acc,t}\\rightarrow T_{real,t}\\rightarrow S_{t+1}
\\]

\\[
(S_{t+1},C_{t+1},L_{t+1})\\rightarrow T_{acc,t+1}
\\]

Esta secuencia representa una organización analítica de las observaciones, no una dinámica universal ni una afirmación de que toda transición de estado proceda exclusivamente de una transformación realizada dentro del sistema. Los cambios contextuales y las condiciones externas también pueden modificar el espacio accesible.

Cuando las transformaciones pueden identificarse de forma consistente entre dos momentos, podemos describir el cambio mediante varios indicadores:

\\[
\\begin{aligned}
A_t &= |T_{acc,t}| \\
A_{t+1} &= |T_{acc,t+1}| \\
G_t &= |T_{acc,t+1} \\setminus T_{acc,t}| \\
L_t &= |T_{acc,t} \\setminus T_{acc,t+1}| \\
P_t &= |T_{acc,t} \\cap T_{acc,t+1}| \\
R_t &= G_t + L_t \\
D_t &= A_{t+1}-A_t = G_t-L_t
\\end{aligned}
\\]

Aquí, \\(A_t\\) y \\(A_{t+1}\\) son las cardinalidades inicial y sucesora; \\(G_t\\), las identidades incorporadas; \\(L_t\\), las retiradas; \\(P_t\\), las que persisten; \\(R_t\\), el volumen de identidades añadidas y retiradas; y \\(D_t\\), el cambio neto de cardinalidad. Estas operaciones presuponen que las transformaciones se han identificado con criterios compatibles en ambos momentos y que sus identidades pueden compararse. Si cambia la granularidad, la definición de transformación o el procedimiento de identificación, las diferencias observadas podrían reflejar cambios en la representación y no necesariamente cambios en el sistema.

Las cantidades están relacionadas por las identidades:

\\[
A_{t+1}=P_t+G_t
\\]
\\[
A_t=P_t+L_t
\\]

Estas relaciones permiten comprobar que la cardinalidad sucesora se compone de las transformaciones persistentes y las incorporadas, mientras que la cardinalidad inicial se compone de las persistentes y las retiradas. El volumen \\(R_t\\) no es una tasa normalizada de rotación: expresa el total de identidades añadidas y retiradas. Por ello, no debe compararse directamente entre espacios de tamaños muy distintos como si fuera una medida relativa.

Estas cantidades describen aspectos distintos: el cambio neto no revela por sí solo cuántas identidades se han sustituido, y el volumen de identidades añadidas y retiradas no indica si el espacio ha aumentado o disminuido en términos netos.

No es necesario reducir toda la dinámica a un único indicador. Un sistema puede mantener el mismo número de transformaciones y, aun así, experimentar una sustitución profunda. Otro puede ampliar el espacio incorporando opciones que apenas modifican las trayectorias que realmente puede seguir. La selección de descriptores debe responder a la pregunta analítica, a la calidad de los datos y a la semántica del dominio. Ninguno de estos descriptores constituye por sí mismo una puntuación de calidad, capacidad o valor.

En algunos análisis puede estudiarse también el **alcance potencial a un paso**: el conjunto de estados sucesores estructuralmente posibles desde un estado dado, bajo una representación y unas reglas de transición especificadas. Su composición y cardinalidad dependen de cómo se definan los estados y las transiciones en el modelo. Este objeto no equivale a la ejecución observada ni a la alcanzabilidad efectiva en tiempo de ejecución. La evidencia disponible muestra que el cambio del espacio accesible y el cambio de ese alcance potencial pueden distinguirse; por tanto, no deben tratarse como una misma magnitud.

La comparación entre dominios exige una precaución adicional. Puede ser posible utilizar una misma estructura analítica en sistemas diferentes sin asumir que sus transformaciones concretas, mecanismos o significados sean equivalentes. La consistencia debe buscarse en el papel que desempeñan los conceptos —estado, accesibilidad, realización y estado sucesor— y en la validez de las operaciones aplicadas, no en imponer etiquetas idénticas a fenómenos distintos. La equivalencia de los mecanismos o de los efectos debe establecerse mediante evidencia específica.

## 7. Qué muestra la evidencia acotada y qué no demuestra

La evidencia disponible procede de estudios y análisis distintos. No constituye una única prueba ni permite combinar sus tamaños muestrales o alcances. Cada resultado responde a una pregunta diferente.

**Evidencia temporal en un ecosistema de paquetes de software.** Un análisis de 516.061 pares temporales consecutivos de versiones de paquetes, construidos a partir de un conjunto histórico de datos de Rust, examinó los cambios en el espacio de transformaciones accesibles bajo una operacionalización de un solo paso. Se observaron 438.203 pares no persistentes (aproximadamente el 84,91 %): 77.858 casos de persistencia, 8.295 de expansión, 3.786 de contracción y 426.122 de reconfiguración. La comparación también distinguió cambios en el espacio accesible de cambios en el alcance potencial de estados sucesores a un paso (\\(Reach^{1}_{pot}\\)): en 159.921 pares cambió el espacio accesible sin cambiar el alcance potencial de un paso; en 278.282 cambiaron ambos. Además, 266.201 pares mantuvieron la misma cardinalidad del alcance potencial, pero no la misma composición. La ejecución principal y su repetición obligatoria produjeron resultados estructurados idénticos. El análisis respalda, dentro de esta representación congelada y del horizonte de un paso, que el cambio en el espacio accesible no es equivalente al cambio en el alcance potencial de estados sucesores y que la cardinalidad por sí sola no describe su composición. No demuestra alcanzabilidad en tiempo de ejecución, suficiencia de trayectorias a horizontes mayores, causalidad, capacidad predictiva, efectos sobre resultados o valor, ni validez universal. La [nota de investigación complementaria](../../../learning-resources/research-notes/es/analisis-temporal-de-un-ecosistema-de-paquetes-de-software.md) documenta la operacionalización, la procedencia y los límites del resultado.

**Una representación común en dos dominios computacionales.** Un estudio acotado reconstruyó 36 transiciones en dos dominios estructuralmente diferentes. La validación no encontró registros inválidos y una auditoría matemática independiente no encontró discrepancias en los descriptores calculados. En ambos dominios se observaron cambios en la identidad de las transformaciones accesibles. En el modelo de coordinación probabilística, las identidades cambiaron sin variar la cardinalidad; en el dominio de planificación en cuadrícula también hubo rotación de identidades y algunas reducciones netas. La auditoría específica de este último dominio mostró que sus cambios podían reconstruirse completamente a partir del modelo nativo de estados y acciones: no demostró una ganancia representacional distinta. En conjunto, el resultado respalda la posibilidad de operacionalizar una estructura común de transición en esos dos casos, no su superioridad ni su validez universal.

**Evidencia causal acotada sobre trayectorias posteriores.** En una evaluación experimental de expansión de servicios financieros rurales en el sur de India, la asignación aleatoria de aperturas de sucursales modificó la infraestructura local de acceso a servicios financieros formales. La intervención introdujo acceso estructural a un paquete de servicios que incluía préstamos, ahorro, seguros y asesoramiento financiero adaptado. La consolidación de la evidencia de TGCV interpreta esa intervención como una expansión estructural de la accesibilidad y reconoce apoyo causal acotado para su relación con cambios posteriores en las trayectorias de los hogares en el contexto estudiado. El efecto identificado corresponde a la intervención estructural de acceso tal como fue implementada; no permite atribuir efectos independientes a cada uno de los servicios que integraban el paquete. La interpretación mantiene separados el acceso estructural, la utilización posterior de productos financieros y los cambios observados en empleo, actividad económica e ingresos. Es evidencia de una relación acotada en un entorno concreto; no establece que cualquier cambio de accesibilidad produzca una modificación de trayectoria, ni que la accesibilidad sea su única causa.

**Un resultado causal no detectable en infraestructura urbana.** Un segundo análisis de TGCV utilizó los datos de replicación de un experimento de inversión en infraestructura en barrios urbanos de México. Sobre una operacionalización estructural acotada de factibilidad mínima —seis dimensiones de infraestructura y doce familias elementales de apertura o cierre— se estimó el efecto de la asignación del tratamiento sobre el cambio neto de cardinalidad de ese conjunto, no sobre una reconstrucción completa del espacio de transformaciones accesibles. La estimación no fue estadísticamente detectable: el efecto fue aproximadamente \\(-0,031\\) (error estándar agrupado: 0,165; valor p: 0,849), y el intervalo de confianza del 95 % incluyó efectos negativos y positivos. La inferencia robusta por remuestreo agrupado tampoco detectó un efecto. Por tanto, el resultado no demuestra que el efecto verdadero sea exactamente cero ni refuta la hipótesis general. La posible interferencia entre unidades permanece sin resolver y la factibilidad estructural mínima no equivale a una identificación mecanicista completa del predicado de accesibilidad. Este análisis de TGCV tiene un estimando propio y no debe confundirse con los resultados publicados por los autores del estudio original sobre acceso a infraestructura, inversión en vivienda o valor inmobiliario.

**Un caso de identificación parcial en pavimentación urbana.** En el estudio experimental de pavimentación de calles residenciales en Acayucan, México, fue posible especificar funciones candidatas —como facilitar desplazamientos de vehículos, peatones o bicicletas— y reconstruir cambios longitudinales de conectividad. Sin embargo, los datos no permitieron identificar de forma independiente el predicado completo de accesibilidad ni reconstruir todo el espacio de transformaciones accesibles. El caso muestra por qué una intervención física y un cambio observado de conectividad no equivalen automáticamente a una modificación identificada de \\(T_{acc}\\).

**Una ilustración sintética de no equivalencia.** En un entorno sintético controlado, una intervención modificó el espacio accesible mientras la trayectoria realizada especificada permanecía igual y el resultado de valor definido para ese ejercicio no cambiaba. Su función es mostrar que estos niveles pueden variar independientemente bajo una construcción especificada, no estimar la frecuencia con que ocurre esa situación en sistemas reales. No es evidencia de comportamiento real ni demuestra que las modificaciones de accesibilidad carezcan de efectos sobre trayectorias o valor en general.

En conjunto, estos resultados respaldan operaciones y relaciones delimitadas: la distinción empírica entre cambios en el espacio accesible y en el alcance potencial a un paso; la operacionalización de una estructura común en dos dominios computacionales; y una relación causal acotada con trayectorias posteriores en un contexto real. También muestran límites de identificación y resultados no detectables. No demuestran una teoría universal de la dinámica de transformaciones ni resuelven la relación entre accesibilidad y valor.

## 8. Límites, supuestos y preguntas abiertas

El análisis del espacio de transformaciones accesibles depende de decisiones de representación, de las condiciones en las que se observa el sistema y de los límites de la evidencia disponible. Conviene distinguir estos planos: una limitación de operacionalización no equivale a una refutación científica, y una pregunta todavía abierta no debe presentarse como un resultado ya establecido.

### Decisiones de representación y operacionalización

**Delimitación del sistema y del universo de candidatas.** Si los límites del sistema son inadecuados, pueden omitirse condiciones externas decisivas o atribuirse al sistema capacidades que dependen de otros actores e infraestructuras. El universo de transformaciones debe delimitarse de forma justificable para la pregunta estudiada. No siempre es posible enumerar todas las transformaciones concebibles; el análisis debe explicar qué incluye, qué deja fuera y por qué el cierre operacional adoptado resulta adecuado para la pregunta y el estimando declarados. Esa justificación no convierte el universo delimitado en una representación exhaustiva de todas las transformaciones posibles.

**Identidad y equivalencia de las transformaciones.** Para comparar espacios a lo largo del tiempo necesitamos saber cuándo una transformación persiste, cuándo cambia y cuándo debe considerarse distinta. Entre dominios, las etiquetas no pueden equipararse automáticamente: una estructura analítica común no implica identidad semántica de las transformaciones. La equivalencia debe justificarse atendiendo al significado y a la función de las transformaciones en cada sistema.

**Criterio de accesibilidad y evaluación de la evidencia.** El predicado debe definirse con independencia de la realización y de los resultados posteriores. Su especificación debe incluir qué condiciones se consideran necesarias, qué evidencia permite establecer que se cumplen y cómo se tratan los casos indeterminados. Estas reglas deben fijarse con independencia de las realizaciones y los resultados que posteriormente se observen. De otro modo, existe el riesgo de adaptar retrospectivamente la definición a los datos. También debe distinguirse la disponibilidad estructural de la adopción o utilización efectiva.

**Medición y escalarización.** La cardinalidad es solo un descriptor. Puede ocultar sustituciones, cambios de identidad y diferencias semánticas. Reducir el espacio a una cifra puede ser útil para un estimando concreto, pero no equivale a medir toda su estructura. Los resultados basados en una operacionalización escalar deben interpretarse dentro de esa delimitación y no extrapolarse automáticamente a dimensiones que no fueron medidas.

### Límites de observación e inferencia

**Dependencias externas e interferencia.** Las dependencias externas pueden formar parte de las condiciones que hacen accesible una transformación, aunque se encuentren fuera de la frontera analítica del sistema. Por otra parte, en estudios causales, la interferencia entre unidades puede comprometer la interpretación de los efectos si una intervención afecta a unidades distintas de aquellas a las que fue asignada. Ambos problemas requieren declarar la frontera del análisis, las dependencias relevantes y los supuestos utilizados; no son necesariamente el mismo problema ni se resuelven con una única estrategia.

**Heterogeneidad entre dominios.** Una estructura analítica común no implica que los mecanismos, las transformaciones o sus significados sean iguales en todos los sistemas. La generalidad debe probarse, no presuponerse. La transferencia de un criterio o de un resultado entre dominios requiere justificar qué aspectos son comparables y cuáles dependen del contexto.

**Alcance de la evidencia disponible.** Los estudios examinados tampoco permiten realizar el mismo tipo de inferencia. Los análisis computacionales aportan evidencia estructural y metodológica bajo operacionalizaciones delimitadas; el análisis temporal de un ecosistema de paquetes de software permite observar cambios y diferencias entre la composición de los espacios y el alcance potencial a un paso, pero no demuestra alcanzabilidad efectiva ni causalidad. La intervención de expansión de servicios financieros rurales aporta evidencia causal acotada sobre trayectorias posteriores en su contexto. El análisis de infraestructura urbana no detecta el efecto en el estimando estructural examinado, sin demostrar que el efecto sea universalmente nulo, mientras que el caso de pavimentación conserva una identificación parcial. El experimento sintético ilustra una posibilidad lógica bajo una construcción especificada, no una regularidad empírica. Estas diferencias deben mantenerse al valorar el conjunto de la evidencia.

### Preguntas científicas abiertas

**Relación con las trayectorias.** Existe evidencia causal acotada de que una expansión estructural de accesibilidad afectó trayectorias posteriores en un contexto estudiado. Otros análisis aportan evidencia estructural o metodológica, pero no todos identifican una relación causal. La generalidad de la relación, los mecanismos implicados y las condiciones bajo las cuales se mantiene siguen siendo cuestiones abiertas.

**Relación con el valor.** El valor requiere una evaluación adicional: qué resultados cuentan, para quién, con qué criterios y en qué horizonte temporal. Que una transformación sea accesible, o incluso que se realice, no determina por sí mismo el valor de sus consecuencias. La relación causal o predictiva entre cambios en el espacio accesible y cambios en el valor continúa abierta.

Estas limitaciones no hacen inútil el concepto. Definen las condiciones bajo las cuales puede utilizarse de forma rigurosa, delimitan qué inferencias permite la evidencia disponible y señalan qué investigación adicional sería necesaria.

## 9. Síntesis y reflexión

El espacio de transformaciones accesibles representa qué transformaciones puede realizar un sistema bajo un estado y unas condiciones especificadas. Se deriva de la configuración relevante del sistema y de un criterio explícito de accesibilidad; no es una causa independiente ni una lista ilimitada de posibilidades imaginables.

Su composición puede cambiar mediante expansión, contracción, reconfiguración o sustitución. Por eso, observar únicamente el número de transformaciones puede ser insuficiente: también importa qué transformaciones aparecen, cuáles desaparecen y cuáles permanecen. La dinámica del espacio accesible tampoco debe confundirse con el cambio en el alcance potencial de estados sucesores ni con la ejecución observada.

La evidencia disponible ofrece apoyo metodológico acotado para representar estos cambios y apoyo causal acotado para una relación con trayectorias posteriores en un contexto real. El análisis temporal del ecosistema de paquetes muestra, además, que los cambios en el espacio accesible y en el alcance potencial de un paso son empíricamente distinguibles en la operacionalización examinada. También hay resultados no detectables y casos en los que la accesibilidad solo puede identificarse parcialmente. Estas diferencias importan: no toda evidencia responde a la misma pregunta ni permite el mismo tipo de conclusión.

La distinción fundamental debe conservarse a lo largo de todo el análisis:

**accesibilidad no es realización; realización no es trayectoria; trayectoria no es resultado; resultado no es automáticamente valor.**

La relación entre cambios en el espacio accesible y creación de valor permanece abierta y requiere evidencia y evaluación adicionales.

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

- Field, E., & Pande, R. *Evaluating the economic impacts of rural banking: experimental evidence from southern India*. 3ie Impact Evaluation Report 85. https://doi.org/10.23846/OW3IE85
- McIntosh, C., Alegría, T., Ordóñez, G., & Zenteno, R. (2018). The Neighborhood Impacts of Local Infrastructure Investment: Evidence from Urban Mexico. *American Economic Journal: Applied Economics, 10*(3), 263–286. https://doi.org/10.1257/app.20160429
- Gonzalez-Navarro, M., & Quintana-Domeque, C. (2016). Paving Streets for the Poor: Experimental Analysis of Infrastructure Effects. *The Review of Economics and Statistics, 98*(2), 254–267. https://doi.org/10.1162/REST_a_00553. Replication data: https://doi.org/10.7910/DVN/6TC8RO
- Figshare. *Full dataset* [conjunto de datos histórico del ecosistema de paquetes de Rust]. https://springernature.figshare.com/articles/dataset/Full_dataset/21345990. Licencia declarada: CC0.

Los análisis computacionales propios de TGCV citados en este capítulo se documentan mediante notas de investigación complementarias que describen sus fuentes, métodos, resultados y límites. Estas notas son documentación de investigación del proyecto y no deben confundirse con publicaciones externas independientes.
