# TGCV — Selected Research Cases and Evidence Portfolio v0.1

**Identifier:** TGCV-WEB-EVIDENCE-PORTFOLIO-001  
**Version:** 0.1  
**Date:** 2026-11-25  
**Status:** EDITORIAL WORKING DRAFT — NOT APPROVED FOR PUBLICATION  
**Editorial basis:** Current Evidence-to-Claim Matrix v1.47 and its material-evidence records  
**Branch:** strategy/tgcv-web-master

# ESPAÑOL

## Una investigación desarrollada en distintos sistemas y métodos

Las fichas de evidencia de Research profundizan en algunas preguntas centrales de TGCV. Esta panorámica las complementa con una selección representativa de otros casos empíricos, industriales, computacionales y sintéticos registrados en la matriz de evidencia.

La selección muestra la amplitud de los sistemas estudiados y la variedad de métodos empleados: reconstrucción de sistemas en funcionamiento, análisis de datos longitudinales, experimentos de campo, pruebas controladas, simulaciones, reconstrucciones independientes y demostradores sintéticos.

No es un inventario exhaustivo ni un ranking de éxitos. Los casos no tienen todos el mismo objeto ni la misma fuerza probatoria. Algunos aportan evidencia empírica acotada; otros prueban métodos, reconstruyen variables, examinan límites de identificación o documentan resultados negativos. Su inclusión indica que el trabajo está documentado en el programa de investigación, no que todos validen TGCV o respalden las mismas afirmaciones.

## 1. Sistemas de software e ingeniería

### SWIM — adaptación de recursos en un sistema de software

A partir de registros de una ejecución de un sistema auto-adaptativo se reconstruyeron transformaciones como añadir o retirar servidores y modificar parámetros de iluminación. Se identificaron momentos en que esas transformaciones entraban o salían del conjunto accesible y se reconstruyeron acciones y transiciones de estado posteriores.

Un análisis complementario examinó la separación entre accesibilidad y la política nativa que selecciona acciones. La comparabilidad entre determinados estados quedó limitada, por lo que no se afirma una independencia general de la política.

**Aporta:** operacionalización acotada de transformaciones accesibles, cambios temporales y vínculo reconstruible con acciones y estados posteriores.

**Límite:** asociación y reconstrucción, no identificación causal de cambios de trayectoria, creación de valor ni utilidad industrial general.

### AWS — recuperación funcional de una instancia

Un caso industrial siguió una secuencia de recuperación de una instancia de computación. La reparación del estado interno de Windows no bastó para recuperar el acceso remoto: persistía una condición externa de conectividad en las reglas de entrada de red. Tras un diagnóstico de solo lectura y una autorización específica, se aplicó una modificación limitada y se verificó la recuperación funcional desde el mismo punto de observación.

**Aporta:** un ejemplo industrial concreto de la diferencia entre transformar el estado interno de un sistema y habilitar las condiciones externas necesarias para que la función sea efectiva.

**Límite:** es un caso acotado de recuperación funcional. No demuestra por sí mismo una reconstrucción completa de T_acc, causalidad general, creación de valor ni utilidad transversal.

### Ecosistema de paquetes de software

Un análisis longitudinal de **516.061 pares temporales adyacentes** de versiones de paquetes caracterizó persistencia, expansión, contracción y reconfiguración de transformaciones accesibles bajo una representación operacional delimitada. El 84,91 % de los pares presentó algún cambio en el espacio de transformaciones accesibles. El análisis también distinguió esos cambios de una medida acotada de alcance potencial a un paso.

**Aporta:** evidencia estructural cuantitativa a gran escala sobre la dinámica de posibilidades en el ecosistema estudiado.

**Límite:** el alcance se refiere a la representación congelada y a alcance potencial H=1; no equivale a ejecución real de paquetes ni a comportamiento en tiempo de ejecución.

### Sistemas 5G — reconstrucción de un evento de red

Un caso basado en un evento técnico de una red 5G reconstruyó el estado previo, la identidad de la transformación observada, la frontera temporal y la separación respecto de información posterior. Las ejecuciones independientes reprodujeron el evento y su trazabilidad.

**Aporta:** evidencia metodológica acotada para reconstruir un evento y mantener separadas accesibilidad, transformación observada y evidencia posterior.

**Límite:** no establece un conjunto completo de transformaciones accesibles, utilidad, causalidad, valor ni superioridad.

## 2. Intervenciones empíricas y contextos sociales

### Servicios financieros rurales — expansión estructural del acceso

Un experimento de campo en India evaluó la apertura temprana y aleatorizada de sucursales de servicios financieros en áreas rurales. La intervención amplió la infraestructura local disponible para acceder a préstamos, ahorro, seguros y asesoramiento. Se analizaron consecuencias posteriores para los hogares y se reconstruyeron las variables longitudinales utilizadas en el estudio.

**Aporta:** evidencia causal acotada de las consecuencias de una intervención estructural de expansión del acceso financiero, dentro de la población, intervención y periodo estudiados.

**Límite:** el efecto corresponde a la intervención como conjunto. No identifica automáticamente el efecto mediado por cada transformación accesible ni demuestra una relación universal o una creación de valor atribuible exclusivamente a T_acc.

### Infraestructura urbana en México — un contraste causal con resultado limitado

Un estudio de inversión local en infraestructura urbana permitió reconstruir cambios estructurales en seis dimensiones de infraestructura en 342 polígonos observados longitudinalmente. Se definió un conjunto acotado de transformaciones de apertura y cierre de esas dimensiones y se ejecutó un contraste causal previamente delimitado.

**Aporta:** reconstrucción empírica de cambios estructurales y experiencia metodológica al someter una hipótesis a un contraste causal acotado.

**Límite:** el resultado se cerró como negativo dentro del estimando y la operacionalización definidos. No debe presentarse como confirmación de un efecto positivo general ni como evidencia de creación de valor.

### Egipto e India — límites de reconstrucción de la accesibilidad

Dos investigaciones con datos longitudinales permitieron reconstruir aspectos del estado estructural, la intervención o los cambios observados, pero no identificar de forma independiente una regla de admisibilidad suficiente para reconstruir el conjunto de transformaciones accesibles.

**Aporta:** evidencia empírica de frontera: disponer de datos longitudinales, observar cambios o conocer la adopción de una intervención no basta necesariamente para identificar T_acc.

**Límite:** estos casos no son evidencia positiva de cambios en T_acc. Delimitan qué información falta para poder hacerlo.

### Marruecos — reconstrucción de un indicador social

Se reconstruyó de forma independiente un indicador histórico de empoderamiento de las mujeres a partir de los cuestionarios, variables físicas, reglas de codificación y procedimientos de cálculo documentados, sobre 5.551 observaciones.

**Aporta:** evidencia metodológica de trazabilidad y reproducibilidad entre el significado de un instrumento, sus variables y el indicador calculado.

**Límite:** no constituye una medida TGCV de accesibilidad, trayectoria o valor.

## 3. Demostradores y pruebas sintéticas

### EV–Grid — posibilidades de transformación en un sistema energético

Un demostrador sintético de red eléctrica y vehículos eléctricos representa estado y contexto, transformaciones candidatas, reglas de admisibilidad, transformaciones accesibles, transiciones y trayectorias posteriores. En uno de los escenarios se redujo el conjunto accesible de ocho a seis transformaciones bajo las reglas congeladas.

**Aporta:** una prueba ejecutable de la representación y de las distinciones metodológicas de TGCV en un dominio energético sintético.

**Límite:** no es un estudio real de redes eléctricas, no demuestra efectos sobre fiabilidad o movilidad, ni causalidad, valor, superioridad o preparación para despliegue industrial.

### VSL Paired — cuando ampliar posibilidades no cambia la trayectoria

Dos ejecuciones emparejadas, A y B, incluyeron 100 casos sintéticos cada una y fueron reconstruidas de forma independiente. En todos los casos aumentó en una unidad el conjunto de transformaciones accesibles, mientras que la trayectoria realizada y la medida de valor permanecieron sin cambios.

**Aporta:** evidencia sintética controlada de que ampliar el conjunto accesible no obliga a seleccionar la nueva transformación ni a modificar la trayectoria o el valor resultante bajo una política de realización determinada.

**Límite:** es un resultado metodológico dentro de una construcción sintética concreta. No demuestra que la accesibilidad nunca afecte al valor ni estima un efecto causal en sistemas reales.

### Pruebas de reconstrucción entre dominios

Se compararon registros de dos dominios sintéticos/analíticos diferentes: planificación en una cuadrícula y sincronización de liderazgo. Se procesaron 36 registros y una auditoría matemática independiente no encontró discrepancias en los descriptores calculados. Se mantuvieron separadas las identidades y semánticas de las transformaciones propias de cada dominio.

**Aporta:** evidencia metodológica acotada de que una representación de transición común puede instrumentarse en dos dominios heterogéneos.

**Límite:** no demuestra superioridad representacional, validez transversal general ni divergencia de trayectorias; el material disponible no contenía ramas divergentes para contrastar.

### Pruebas de aplicación sintética en varios dominios

Otros demostradores sintéticos examinaron si la cadena de representación podía instanciarse en contextos como orquestación técnica, agentes y permisos, recursos y restricciones. Su función fue comprobar coherencia, trazabilidad y ejecutabilidad de los elementos representados.

**Aporta:** evidencia de aplicación metodológica en escenarios controlados y de identificación de limitaciones de las propias implementaciones.

**Límite:** la ejecución satisfactoria de un demostrador no equivale a validación empírica, utilidad real, causalidad ni superioridad frente a otros métodos.

## 4. Experimentos sobre selección y Transformational Intelligence

Una línea de experimentación controlada examinó decisiones de agentes ante estructuras de posibilidades futuras. Incluye pruebas de selección, contrastes con controles negativos, análisis posteriores y simulaciones Monte Carlo para caracterizar la calibración y potencia de diseños estadísticos.

Los resultados son heterogéneos: algunos análisis permiten estudiar trazabilidad entre decisión y estructura de transformaciones; otros no ofrecen evidencia confirmatoria del mecanismo propuesto o permanecen en un nivel exploratorio. Las simulaciones Monte Carlo caracterizan el comportamiento de un diseño estadístico bajo datos generados, no el comportamiento de sistemas reales.

**Aporta:** desarrollo y prueba de operacionalizaciones experimentales, trazabilidad de decisiones, controles y evaluación de diseños antes de interpretar futuros resultados.

**Límite:** no constituye validación general de Transformational Intelligence, causalidad sobre valor, superioridad explicativa o predictiva ni confirmación de TGCV como teoría universal.

## 5. Reproducibilidad y contraste metodológico

Otras líneas documentadas incluyen ejecuciones con reconstrucción independiente, pruebas de integridad y comparación con referencias o representaciones alternativas. Por ejemplo, una ejecución de observación de transformaciones en un modelo de sistemas fue repetida de forma independiente y reprodujo la misma secuencia de eventos y los mismos estados resumidos.

También se han conservado resultados nulos, límites de identificación y casos en los que un estimador no permitía emitir una conclusión causal reportable. No se han convertido esos cierres en resultados positivos.

**Aporta:** trazabilidad, reproducibilidad acotada y disciplina para conservar resultados desfavorables o inconclusos.

**Límite:** la reproducibilidad técnica de una ejecución no demuestra por sí sola la validez de una hipótesis científica.

## Lectura conjunta

El conjunto de casos muestra un programa que ha trabajado con sistemas de software, infraestructura y servicios financieros, redes, energía, datos sociales, agentes y entornos sintéticos. También muestra variedad metodológica: análisis longitudinal, reconstrucción de eventos, experimentos aleatorizados, pruebas controladas, simulaciones, auditorías y reproducciones independientes.

La amplitud del trabajo no debe confundirse con una validación acumulativa automática. Cada caso responde a una pregunta específica y tiene un alcance propio. Algunos respaldan afirmaciones empíricas acotadas; otros son pruebas metodológicas; otros muestran límites, resultados nulos o variables que no pueden identificarse con los datos disponibles.

La matriz de evidencia organiza la relación entre casos y afirmaciones científicas. Esta panorámica ofrece una lectura pública y selectiva de ese trabajo; no sustituye a la matriz ni modifica sus estados.

---

# ENGLISH

## Research conducted across different systems and methods

The Research evidence briefs examine selected central questions in TGCV in depth. This overview complements them with a representative selection of other empirical, industrial, computational and synthetic cases recorded in the evidence matrix.

The selection illustrates the range of systems studied and methods used: reconstruction of operating systems, longitudinal data analysis, field experiments, controlled tests, simulations, independent reconstructions and synthetic demonstrators.

It is not an exhaustive inventory or a ranking of successes. The cases do not all have the same object or evidentiary strength. Some provide bounded empirical evidence; others test methods, reconstruct variables, examine identification limits or document negative results. Inclusion means that the work is documented within the research programme, not that every case validates TGCV or supports the same claims.

## 1. Software systems and engineering

### SWIM — resource adaptation in a software system

Records from an execution of a self-adaptive system were used to reconstruct transformations such as adding or removing servers and changing lighting parameters. The analysis identified moments when these transformations entered or left the accessible set and reconstructed subsequent actions and state transitions.

A complementary analysis examined the separation between accessibility and the native policy that selects actions. Comparability across some states was limited, so no general policy independence is claimed.

**Contribution:** bounded operationalisation of accessible transformations, their temporal changes and a reconstructable link to subsequent actions and states.

**Limit:** association and reconstruction, not causal identification of trajectory changes, value creation or general industrial utility.

### AWS — functional recovery of an instance

An industrial case followed the recovery of a computing instance. Repairing the internal Windows state was not sufficient to restore remote access: an external network-enabling condition remained blocked by inbound security rules. Following a read-only diagnosis and specific authorisation, a narrow change was applied and functional recovery was verified from the same observation point.

**Contribution:** a concrete industrial example of the difference between transforming a system's internal state and enabling the external conditions required for its function to become effective.

**Limit:** a bounded functional-recovery case. It does not by itself demonstrate complete reconstruction of T_acc, general causality, value creation or cross-domain utility.

### Software package ecosystem

A longitudinal analysis of **516,061 adjacent temporal package-version pairs** characterised persistence, expansion, contraction and reconfiguration of accessible transformations under a bounded operational representation. Some change in the accessible transformation space occurred in 84.91% of pairs. The analysis also distinguished these changes from a bounded one-step potential-reach measure.

**Contribution:** large-scale quantitative structural evidence about the dynamics of possibilities in the ecosystem studied.

**Limit:** the scope is the frozen representation and H=1 potential reach; it is not equivalent to actual package execution or runtime behaviour.

### 5G systems — reconstruction of a network event

A case based on a technical event in a 5G network reconstructed the prior state, the identity of the observed transformation, the temporal boundary and separation from downstream information. Independent executions reproduced the event and its traceability.

**Contribution:** bounded methodological evidence for reconstructing an event while keeping accessibility, observed transformation and downstream evidence separate.

**Limit:** it does not establish a complete set of accessible transformations, utility, causality, value or superiority.

## 2. Empirical interventions and social contexts

### Rural financial services — structural expansion of access

A field experiment in India evaluated the randomised early opening of financial-service branches in rural areas. The intervention expanded local infrastructure for access to loans, savings, insurance and advice. Subsequent household consequences were analysed, and the study's longitudinal variables were reconstructed.

**Contribution:** bounded causal evidence about the consequences of a structural financial-access intervention, within the population, intervention and period studied.

**Limit:** the effect concerns the intervention as a whole. It does not automatically identify the effect mediated by each accessible transformation or demonstrate a universal relationship or value creation attributable exclusively to T_acc.

### Urban infrastructure in Mexico — a bounded causal test

A study of local urban infrastructure investment made it possible to reconstruct structural changes across six infrastructure dimensions in 342 longitudinally observed polygons. A bounded set of opening and closing transformations was defined and a delimited causal contrast was executed.

**Contribution:** empirical reconstruction of structural changes and methodological experience from subjecting a hypothesis to a bounded causal test.

**Limit:** the result was closed as negative within the specified estimand and operationalisation. It should not be presented as confirmation of a general positive effect or as evidence of value creation.

### Egypt and India — limits of accessibility reconstruction

Two studies with longitudinal data made it possible to reconstruct aspects of structural state, intervention or observed change, but did not independently identify a sufficient admissibility rule for reconstructing the set of accessible transformations.

**Contribution:** empirical boundary evidence: longitudinal data, observed changes or knowledge of intervention adoption are not necessarily sufficient to identify T_acc.

**Limit:** these cases are not positive evidence of changes in T_acc. They delimit the information needed to make such a reconstruction.

### Morocco — reconstruction of a social indicator

A historical women's-empowerment indicator was independently reconstructed from questionnaires, physical variables, coding rules and documented calculation procedures, using 5,551 observations.

**Contribution:** methodological evidence of traceability and reproducibility between an instrument's meaning, its variables and the calculated indicator.

**Limit:** it is not a TGCV measure of accessibility, trajectory or value.

## 3. Demonstrators and synthetic tests

### EV–Grid — transformation possibilities in an energy system

A synthetic electric-grid and electric-vehicle demonstrator represents state and context, candidate transformations, admissibility rules, accessible transformations, transitions and subsequent trajectories. In one scenario, the accessible set was reduced from eight to six transformations under the frozen rules.

**Contribution:** an executable test of TGCV representation and methodological distinctions in a synthetic energy domain.

**Limit:** it is not a real-world electricity-grid study and does not demonstrate effects on reliability or mobility, causality, value, superiority or industrial deployment readiness.

### VSL Paired — when expanding possibilities does not change the trajectory

Two paired executions, A and B, each contained 100 synthetic cases and were independently reconstructed. In every case the accessible-transformation set increased by one, while the realised trajectory and value measure remained unchanged.

**Contribution:** controlled synthetic evidence that expanding the accessible set does not force selection of the new transformation or change the trajectory or resulting value under a specified realisation policy.

**Limit:** a methodological result within one specific synthetic construction. It does not show that accessibility never affects value or estimate a causal effect in real systems.

### Cross-domain reconstruction tests

Records from two different synthetic/analytical domains—grid-based planning and leadership synchronisation—were compared. The analysis processed 36 records, and an independent mathematical audit found no discrepancies in the calculated descriptors. Transformation identities and semantics native to each domain were kept separate.

**Contribution:** bounded methodological evidence that a common transition representation can be instrumented in two heterogeneous domains.

**Limit:** it does not demonstrate representational superiority, general cross-domain validity or trajectory divergence; the available material did not contain divergent branches to compare.

### Synthetic application tests across several domains

Other synthetic demonstrators examined whether the representational chain could be instantiated in contexts such as technical orchestration, agents and permissions, resources and constraints. Their purpose was to test consistency, traceability and executability of the represented elements.

**Contribution:** evidence of methodological application in controlled scenarios and identification of limitations in the implementations themselves.

**Limit:** successful execution of a demonstrator is not equivalent to empirical validation, real-world utility, causality or superiority over other methods.

## 4. Experiments on selection and Transformational Intelligence

A line of controlled experimentation examined agent decisions in the presence of future possibility structures. It includes selection tests, contrasts with negative controls, post-primary analyses and Monte Carlo simulations to characterise the calibration and power of statistical designs.

The results are heterogeneous: some analyses support the study of traceability between decisions and transformation structures; others do not provide confirmatory evidence for the proposed mechanism or remain exploratory. Monte Carlo simulations characterise the behaviour of a statistical design under generated data, not the behaviour of real systems.

**Contribution:** development and testing of experimental operationalisations, decision traceability, controls and design evaluation before interpreting future results.

**Limit:** this is not general validation of Transformational Intelligence, causal evidence about value, explanatory or predictive superiority, or confirmation of TGCV as a universal theory.

## 5. Reproducibility and methodological comparison

Other documented lines include executions with independent reconstruction, integrity tests and comparisons with references or alternative representations. For example, an execution observing transformations in a systems model was independently repeated and reproduced the same event sequence and summarised states.

Null results, identification limits and cases in which an estimator did not support a reportable causal conclusion have also been retained. These closures have not been converted into positive results.

**Contribution:** traceability, bounded reproducibility and discipline in preserving unfavourable or inconclusive findings.

**Limit:** technical reproducibility of an execution does not, by itself, demonstrate the validity of a scientific hypothesis.

## Overall interpretation

The portfolio shows a programme that has worked with software systems, infrastructure and financial services, networks, energy, social data, agents and synthetic environments. It also shows methodological variety: longitudinal analysis, event reconstruction, randomised experiments, controlled tests, simulations, audits and independent replications.

The breadth of the work should not be confused with automatic cumulative validation. Each case addresses a specific question and has its own scope. Some support bounded empirical claims; others are methodological tests; still others reveal limits, null results or variables that cannot be identified from the available data.

The evidence matrix organises the relationship between cases and scientific claims. This overview provides a selective public reading of that work; it does not replace the matrix or change its statuses.

---

## Editorial and publication checks — not visitor-facing

1. Reconcile every case summary with the latest canonical Evidence-to-Claim Matrix and material-evidence section before publication. The current pointer identifies v1.47; verify whether a later canonical version exists at publication time.
2. Confirm public-release permission and suitable public references for every case. Do not link internal matrix rows, raw data, run identifiers, governance records, private replication packages or operational security details.
3. Keep the AWS industrial case at the level of bounded functional recovery; do not expose IP addresses, security-group identifiers or ingress-rule details in public copy.
4. Preserve the distinction between the positive bounded KGFS causal contribution and the non-reportable/negative/conditional cases elsewhere in the portfolio.
5. Do not conflate SWIM temporal reconstruction with causal identification; do not describe EV–Grid or VSL Paired as real-world empirical studies.
6. The portfolio is representative, not exhaustive. Add or remove cases only after checking their claim-matrix classification, evidence status and publication permission.
