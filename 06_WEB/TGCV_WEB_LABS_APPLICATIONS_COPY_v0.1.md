# TGCV — Labs & Applications Copy v0.6

**Identifier:** TGCV-WEB-P07-COPY-001  
**Version:** 0.6  
**Date:** 2026-11-25  
**Status:** BILINGUAL EDITORIAL DRAFT — PENDING REVIEW; NOT PUBLICATION APPROVAL  
**Branch:** strategy/tgcv-web-master  
**Authoritative Experience:** TGCV_WEB_LABS_APPLICATIONS_EXPERIENCE_v0.1.md v0.6  
**Content Blueprint:** TGCV_WEB_CONTENT_BLUEPRINT_v0.1.md v4.0

---

# ESPAÑOL

## Labs & Applications
### De las preguntas de investigación a la exploración de sistemas

En Labs & Applications hacemos tangibles algunas preguntas y perspectivas de TGCV mediante demostradores de alcance limitado, experimentos sintéticos y la exploración de posibles contextos de aplicación.

Aquí puedes conocer qué se ha construido o probado hasta ahora y descubrir problemas en distintos ámbitos en los que podría ser interesante investigar cómo cambian las transformaciones que un sistema tiene a su alcance.

Research desarrolla las preguntas, los conceptos, los métodos y la evidencia. Labs & Applications permite examinar algunas de esas ideas mediante modelos, demostradores y contextos concretos. Ambas áreas se alimentan mutuamente: un demostrador no confirma por sí mismo una hipótesis científica, y un contexto prometedor no constituye todavía una aplicación validada.

## Demostradores y experimentos

### Demostrador de cadena completa de TGCV
**Un prototipo de software desarrollado en torno a un sistema sintético.**

Demostrador de cadena completa de TGCV es un prototipo de software desarrollado en torno a un sistema sintético. El prototipo existe, pero no presentamos funciones concretas como disponibles en una versión descargable: todavía no se han verificado conjuntamente el paquete y la interfaz exactos. Por ello, no podemos asegurar que las funciones descritas en la documentación correspondan al artefacto que podría ponerse a disposición del público.

El prototipo utiliza sistemas sintéticos y reglas operativas propias. Su cálculo de accesibilidad es específico del demostrador: no constituye la función científica canónica de TGCV ni un predictor causal. Tampoco es un simulador de sistemas reales ni un producto listo para su despliegue.

**Estado del activo:** prototipo existente. Cuenta con un registro de aceptación funcional basado en un recorrido manual local. Esta aceptación se refiere al funcionamiento del paquete probado, no a su validez científica. El archivo utilizado en ese recorrido no se ha podido verificar como idéntico al paquete generado para su distribución. La disponibilidad de una versión pública descargable no está confirmada; por tanto, no presentamos un enlace de descarga ni afirmamos que exista una versión pública operativa.

### Demostrador de mapeo de transformaciones entre distintos tipos de sistemas
**Un demostrador metodológico basado en escenarios sintéticos.**

**Estado del activo y de la evidencia:** demostrador sintético existente, con una ejecución completada y auditada. Examina una pregunta acotada: si un mismo marco de análisis puede aplicarse a modelos sintéticos de distintos tipos de sistemas y representar sus estados y contexto, las transformaciones candidatas, su accesibilidad, las transiciones y las trayectorias posteriores.

La ejecución examinada incluyó tres escenarios sintéticos: coordinación de redes y servicios de computación en la nube; agentes de inteligencia artificial (IA) y permisos de herramientas; y restricciones de recursos en sistemas de energía y movilidad. Las comprobaciones posteriores confirmaron que los resultados respetaban el formato y las reglas definidos para la prueba, que los controles diseñados para detectar resultados espurios funcionaban y que las reglas de propagación entre escenarios se aplicaban según lo previsto. Las reconstrucciones independientes mediante representaciones convencionales obtuvieron conjuntos equivalentes de transformaciones factibles en los universos examinados.

Este resultado aporta evidencia metodológica limitada sobre la ejecución y comparación de representaciones en esos escenarios sintéticos. No demuestra causalidad empírica en sistemas reales, superioridad explicativa de TGCV, validez universal, creación de valor, retorno de inversión ni preparación para el despliegue industrial. La propagación observada sigue las reglas definidas para cada escenario; no representa efectos causales establecidos empíricamente.

## Explore the possibilities — Experiencias para descubrir y experimentar

Tres experiencias complementarias permiten acercarse a distintas partes del ecosistema TGCV. Se presentan como propuestas de exploración; su inclusión aquí no significa que estén disponibles como herramientas interactivas.

### TGCV Playground
**Explora cómo una condición puede cambiar lo que un sistema puede hacer.**

La experiencia propuesta parte de un ejemplo sencillo: migrar una configuración de software entre dos entornos diferentes. Permite comprender cómo una dependencia o condición de operación puede hacer que una transformación esté disponible en un entorno y no en otro. El ejemplo distingue el sistema, sus condiciones y dependencias, las transformaciones candidatas y las que resultan accesibles en cada escenario. También permite explicar qué significaría ejecutar una transformación y observar sus posibles consecuencias.

TGCV Playground es una experiencia educativa y exploratoria propuesta, no un servicio real de migración ni un simulador de propósito general. Es distinta de Demostrador de cadena completa de TGCV, que es un prototipo existente y no debe confundirse con la experiencia Playground.

### Value Explorer
**Descubre una forma estructurada de explorar oportunidades y construir valor.**

Value Explorer se plantea como una introducción al razonamiento aplicado organizado por VALUE: comprender el contexto y el sistema, conectar conocimientos, explorar alternativas, tomar decisiones, actuar y aprender.

Su propósito es acercar esa lógica mediante una experiencia introductoria. No es VALUE en sí mismo, no sustituye la sección Value Construction y no debe interpretarse como una herramienta operativa mientras no se verifique una implementación utilizable.

### ValueLabsOS Preview
**Una primera aproximación a un entorno digital y colaborativo propuesto.**

ValueLabOS es una propuesta de entorno que busca facilitar la aplicación de VALUE, la experimentación, la documentación de casos, la evaluación de resultados y el intercambio de aprendizajes.

ValueLabsOS Preview presenta la idea y el posible papel de ese entorno, sin dar a entender que exista ya una plataforma terminada. No presupone cuentas de usuario, integraciones, funciones de inteligencia artificial, persistencia de información ni flujos de colaboración operativos.

ValueLabOS es distinto de VALUE y de Labs & Applications. VALUE puede comprenderse y aplicarse sin ValueLabOS.

## Contextos de aplicación que estamos explorando

Los siguientes contextos ayudan a concretar dónde podrían investigarse las preguntas de TGCV. Son candidatos exploratorios, no proyectos de clientes, despliegues ni aplicaciones validadas.

### Agentes de IA, herramientas y permisos
¿Qué puede hacer realmente un agente cuando sus acciones dependen de herramientas externas, permisos, autenticación, persistencia de sesión y condiciones de la infraestructura?

Nos interesa explorar cómo los cambios en esas condiciones pueden abrir, limitar o modificar las acciones accesibles y las secuencias posteriores. La cuestión también exige comparar esta perspectiva con los modelos habituales de control de acceso, flujos de trabajo y orquestación de agentes.

**Estado:** contexto de aplicación candidato en exploración. No se ha demostrado una contribución diferencial de TGCV.

### Gemelos digitales y mantenimiento predictivo
¿Cómo se conectan el estado de un activo físico, los datos que lo describen, los modelos digitales, las capacidades de análisis y las acciones de mantenimiento?

Este contexto permite investigar si los cambios en el estado físico, la información disponible, los recursos o las condiciones de operación modifican las acciones de mantenimiento que pueden realizarse y las trayectorias posteriores del sistema.

**Estado:** contexto candidato en exploración. La monitorización, la predicción, las reglas de mantenimiento y la planificación convencional son referencias alternativas que deben considerarse.

### Coordinación entre vehículos eléctricos y red eléctrica (EV–Grid)
¿Cómo condicionan la capacidad de la red eléctrica, la demanda de recarga, los vehículos, las estaciones y las necesidades de movilidad las opciones factibles de carga y desplazamiento?

El interés está en examinar cómo las restricciones y los recursos compartidos pueden abrir, cerrar o modificar opciones entre los ámbitos de energía y movilidad.

Se ha ejecutado y auditado un demostrador sintético mínimo relacionado con este contexto. En esa prueba acotada se observó un cambio en las transformaciones que podían realizarse bajo una transición especificada. Sin embargo, el modelo utilizado para comparar los resultados aplicó la misma regla de admisibilidad que el recorrido TGCV; no fue, por tanto, una referencia independiente. El resultado no demuestra superioridad ni concordancia independiente con un método alternativo. El contexto de aplicación más amplio sigue siendo candidato.

**Estado:** contexto candidato en exploración; no es una aplicación desplegada ni validada.

## Otros contextos que merece la pena investigar

La búsqueda no se limita a los tres contextos destacados. También se han identificado problemas en los que distintas capacidades, reglas, recursos y trayectorias pueden depender unas de otras:

- **Orquestación multidominio de redes móviles de quinta generación (5G), servicios en la nube y procesamiento de datos cerca de donde se generan.** Coordinación de cambios entre redes, infraestructuras distribuidas, seguridad y servicios.
- **Ciberseguridad y redes autodefensivas.** Interacción entre identidad, estado de seguridad, telemetría, infraestructura y respuesta automatizada.
- **Servicios sociales integrados y gestión de casos ciudadanos.** Continuidad de los casos entre departamentos, datos interoperables, procesos y canales de atención.
- **Atención integrada sanitaria y social.** Coordinación entre atención primaria, hospitales, servicios sociales, sistemas de información y organizaciones.
- **Servicios públicos y justicia entre organismos.** Trayectorias de casos que atraviesan policía, fiscalía, tribunales y otras instituciones, con autoridades, procedimientos e información diferentes.

Estos contextos no tienen todos la misma profundidad de análisis. Algunos han pasado por una exploración estructural más detallada y otros siguen siendo candidatos iniciales. Ninguno está cualificado como aplicación TGCV.

## Ámbitos más amplios para descubrir oportunidades

Además de contextos concretos, estamos explorando cinco grandes familias de problemas. Pueden ayudar a reconocer situaciones en una organización, producto o sistema en las que tendría sentido investigar qué transformaciones están disponibles y qué cambios podrían habilitar otras.

### Transformación organizativa y nuevas formas de trabajo
¿Qué capacidades, relaciones o cambios previos permitirían organizar el trabajo de otra manera? ¿Qué dependencias habría que resolver para que una nueva configuración organizativa fuera viable?

**Hipótesis de valor que habría que investigar:** identificar alternativas organizativas más viables y comprender mejor las dependencias y trayectorias necesarias para llevarlas a cabo.

### Innovación de productos y servicios
¿Qué combinaciones de capacidades, recursos y relaciones podrían hacer posible una nueva oferta o transformar un producto o servicio existente?

**Hipótesis de valor que habría que investigar:** descubrir antes alternativas prometedoras y reducir el esfuerzo dedicado a conceptos cuyas condiciones necesarias no puedan alcanzarse.

### Operaciones y transformación de procesos
¿Qué opciones están bloqueadas por dependencias o restricciones? ¿Qué tendría que cambiar para habilitarlas y en qué secuencia podrían realizarse esos cambios?

**Hipótesis de valor que habría que investigar:** comparar alternativas operativas más viables y evitar comprometerse con secuencias de cambio que no puedan realizarse bajo las condiciones existentes.

### Evolución de sistemas de IA y tecnología
¿Cómo cambian las acciones y funciones disponibles cuando se modifican herramientas, permisos, datos, recursos, integraciones o condiciones de operación?

**Hipótesis de valor que habría que investigar:** fundamentar mejor las decisiones de evolución tecnológica haciendo explícitas las dependencias y las trayectorias técnicamente factibles.

### Alternativas de transformación y decisiones de inversión
¿Qué caminos de transformación existen? ¿De qué cambios previos depende cada uno y qué condiciones deberían cumplirse antes de comprometer recursos?

**Hipótesis de valor que habría que investigar:** comparar alternativas mejor fundamentadas, reducir inversiones en opciones que resulten inviables y mejorar la justificación de las decisiones.

Estas cinco familias son ámbitos amplios para reconocer y formular problemas. No son mercados validados, una cartera de servicios ni aplicaciones que hayan superado una evaluación de ajuste. Las hipótesis de valor requieren definiciones, medidas y evidencia independientes. Ampliar las posibilidades de transformación no garantiza mejores decisiones ni creación de valor.

Conviene distinguir tres niveles:
- **Ámbitos de oportunidad:** familias amplias en las que reconocer problemas.
- **Contextos de aplicación:** sistemas concretos que se investigan como candidatos.
- **Demostradores y experimentos:** activos acotados que permiten examinar preguntas específicas, sin validar automáticamente un ámbito o una aplicación más amplia.

## Cómo interpretar los estados y la evidencia

La madurez de un activo y el tipo de evidencia disponible son dimensiones diferentes. En esta página, por ejemplo, Demostrador de cadena completa de TGCV es un prototipo existente con aceptación funcional local comunicada por el usuario; el demostrador de mapeo entre distintos tipos de sistemas es un experimento sintético ejecutado y auditado; TGCV Playground, Value Explorer y ValueLabsOS Preview son experiencias propuestas, sin disponibilidad operativa verificada; y los contextos de aplicación siguen siendo candidatos exploratorios.

Un prototipo puede existir y funcionar con sistemas sintéticos sin estar validado científicamente. Un experimento sintético puede haberse ejecutado y auditado sin constituir evidencia empírica. Y una aplicación desplegada tampoco demostraría, por sí sola, que TGCV aporta una explicación o un resultado diferencial.

Por eso describimos cada trabajo según lo que realmente se ha construido, probado o documentado. No equiparamos existencia de software, disponibilidad pública, ejecución, auditoría, evidencia empírica, despliegue y creación de valor.

En el estado actual, esta página no ofrece un Playground profesional de propósito general, aplicaciones industriales validadas, servicios con resultados garantizados, una red de laboratorios físicos ni una plataforma abierta de colaboración. TGCV Playground, Value Explorer y ValueLabsOS Preview no se presentan como herramientas operativas disponibles.

## Descubrir nuevos problemas y oportunidades

Estamos explorando distintos contextos de aplicación de TGCV y queremos descubrir también otros problemas y oportunidades junto con personas y organizaciones interesadas en investigarlos.

Quizá tu organización, equipo o sistema se enfrenta a una transformación en la que las capacidades, las dependencias o las restricciones condicionan qué puede hacerse a continuación. Nos interesa conocer esos contextos y explorar si plantean preguntas relevantes para la investigación.

Esta invitación busca abrir una conversación y descubrir posibles casos. No constituye un programa formal de colaboración ni implica aceptación, financiación, análisis o trabajo comprometido.

**Para profundizar:** Research · Systems Engineering · Transformational Intelligence · Value Construction.

---

# ENGLISH

## Labs & Applications
### From research questions to the exploration of systems

Labs & Applications makes selected TGCV questions and perspectives tangible through bounded demonstrators, synthetic experiments and the exploration of potential application contexts.

Here you can discover what has been built or tested so far and identify problems in different fields where it may be worth investigating how the transformations available to a system can change.

Research develops the questions, concepts, methods and evidence. Labs & Applications allows selected ideas to be examined through models, demonstrators and specific contexts. The two areas inform one another: a demonstrator does not, by itself, confirm a scientific hypothesis, and a promising context is not yet a validated application.

## Demonstrators and experiments

### TGCV Full Chain Demo
**A software prototype built around a synthetic system.**

TGCV Full Chain Demo is a software prototype built around a synthetic system. The prototype exists, but we do not present specific functions as available in a downloadable release: the exact package and interface have not yet been verified together. We therefore cannot confirm that functions described in the documentation correspond to an artifact that could be made publicly available.

The prototype uses synthetic systems and its own operational rules. Its accessibility calculation is specific to the demonstrator: it is not TGCV's canonical scientific function or a causal predictor. Nor is it a simulator of real systems or a product ready for deployment.

**Asset status:** existing prototype. It has a software-functionality acceptance record based on a local manual walkthrough. This acceptance concerns the package that was tested, not scientific validity. The file used in that walkthrough has not been verified as identical to the package generated for distribution. The availability of a public downloadable release has not been verified; we therefore provide no download link and make no claim that a public operational version is available.

### Cross-domain transformation mapping demonstrator
**A methodological demonstrator based on synthetic scenarios.**

**Asset and evidence status:** existing synthetic demonstrator, with one completed and audited execution. It examines a bounded question: can a common analytical framework be applied to synthetic models of different types of systems, explicitly representing their states and context, candidate transformations, accessibility, transitions and subsequent trajectories?

The execution examined three synthetic scenarios: network and cloud-computing orchestration; artificial intelligence (AI) agents and tool permissions; and resource constraints in energy and mobility systems. Subsequent checks confirmed that outputs followed the format and rules defined for the test, that controls designed to detect spurious results worked as intended, and that the declared rules for propagation between scenarios were followed. Independent reconstructions using conventional representations produced equivalent feasible transformation sets in the tested universes.

This provides limited methodological evidence about executing and comparing representations in those synthetic scenarios. It does not demonstrate empirical causality in real systems, TGCV's explanatory superiority, universal validity, value creation, return on investment or readiness for industrial deployment. The observed propagation follows the rules defined for each scenario; it does not represent empirically established causal effects.

## Explore the possibilities — Experiences to discover and experiment

Three complementary experiences offer different ways to approach the TGCV ecosystem. They are presented as proposed explorations; their inclusion here does not mean that they are available as interactive tools.

### TGCV Playground
**Explore how a condition can change what a system can do.**

The proposed experience starts with a simple example: migrating a software configuration between two different environments. It helps explain how a dependency or operating condition can make a transformation available in one environment but not in another. The example distinguishes the system, its conditions and dependencies, candidate transformations, and those accessible in each scenario. It can also explain what it would mean to execute a transformation and examine its possible consequences.

TGCV Playground is a proposed educational and exploratory experience, not a real migration service or a general-purpose simulator. It is separate from TGCV Full Chain Demo, which is an existing prototype and should not be confused with the Playground experience.

### Value Explorer
**Discover a structured way to explore opportunities and build value.**

Value Explorer is conceived as an introduction to the applied reasoning organised by VALUE: understanding the context and system, connecting knowledge, exploring alternatives, making decisions, acting and learning.

Its purpose is to introduce this logic through an introductory experience. It is not VALUE itself, does not replace the Value Construction page, and should not be interpreted as an operational tool while no usable implementation has been verified.

### ValueLabsOS Preview
**A first look at a proposed digital and collaborative environment.**

ValueLabOS is a proposed environment intended to facilitate the application of VALUE, experimentation, case documentation, the evaluation of results and the sharing of learning.

ValueLabsOS Preview introduces the idea and possible role of this environment without suggesting that a finished platform already exists. It does not imply operational user accounts, integrations, AI capabilities, persistent information or collaboration workflows.

ValueLabOS is distinct from VALUE and from Labs & Applications. VALUE can be understood and applied without ValueLabOS.

## Application contexts under exploration

The following contexts help make concrete where TGCV questions might be worth investigating. They are exploratory candidates, not client projects, deployments or validated applications.

### AI agents, tools and permissions
What can an agent actually do when its actions depend on external tools, permissions, authentication, session persistence and infrastructure conditions?

We are interested in exploring how changes in these conditions may open, restrict or alter accessible actions and subsequent sequences. This question also requires comparison with established approaches to access control, workflows and agent orchestration.

**Status:** exploratory candidate application context. No differential contribution from TGCV has been demonstrated.

### Digital twins and predictive maintenance
How are the condition of a physical asset, the data describing it, digital models, analytical capabilities and maintenance actions connected?

This context offers an opportunity to investigate whether changes in physical condition, available information, resources or operating conditions alter the maintenance actions that can be carried out and the system's subsequent trajectories.

**Status:** exploratory candidate application context. Conventional monitoring, prediction, maintenance rules and scheduling are alternative approaches that must be considered.

### Electric-vehicle and electricity-grid coordination (EV–Grid)
How do grid capacity, charging demand, vehicles, charging stations and mobility needs shape feasible charging and travel options?

The focus is on examining how shared resources and constraints may open, close or alter options across energy and mobility.

A related minimum synthetic demonstrator has been executed and audited. In that bounded test, a change in the transformations that could be carried out was observed under a specified transition. However, the comparison model used the same admissibility rule as the TGCV path, so it was not an independent reference. The result therefore does not demonstrate superiority or independent agreement with an alternative method. The wider application context remains a candidate.

**Status:** exploratory candidate application context; not a deployed or validated application.

## Other contexts worth exploring

The search is not limited to the three featured contexts. Other problems have also been identified in which different capabilities, rules, resources and trajectories may depend on one another:

- **Multi-domain fifth-generation mobile networks (5G), cloud services and computing close to connected devices.** Coordinating changes across networks, distributed infrastructure, security and services.
- **Cybersecurity and self-defending networks.** Interactions between identity, security state, telemetry, infrastructure and automated response.
- **Integrated social services and citizen case management.** Continuity of cases across departments, interoperable data, workflows and service channels.
- **Integrated health and social care.** Coordination across primary care, hospitals, social services, information systems and organisations.
- **Cross-agency public services and justice.** Case trajectories spanning police, prosecution, courts and other institutions, each with distinct authorities, procedures and information.

These contexts have not all been analysed to the same depth. Some have undergone more detailed structural exploration, while others remain initial candidates. None is qualified as a TGCV application.

## Broader areas for discovering opportunities

Alongside specific contexts, we are exploring five broad families of problems. They may help identify situations in an organisation, product or system where it would be useful to investigate which transformations are available and what changes might enable others.

### Organisational transformation and new ways of working
What capabilities, relationships or prior changes could make different ways of organising work possible? Which dependencies would need to be addressed for a new organisational arrangement to become feasible?

**Value hypothesis to investigate:** identify more viable organisational alternatives and better understand the dependencies and trajectories required to pursue them.

### Product and service innovation
What combinations of capabilities, resources and relationships could make a new offering possible or transform an existing product or service?

**Value hypothesis to investigate:** discover promising alternatives earlier and reduce effort spent on concepts whose necessary enabling conditions cannot be met.

### Operations and process transformation
Which options are blocked by dependencies or constraints? What would need to change to enable them, and in what sequence could those changes take place?

**Value hypothesis to investigate:** compare more viable operational alternatives and avoid committing to change sequences that cannot be realised under current conditions.

### Evolution of AI and technology systems
How do available actions and functions change when tools, permissions, data, resources, integrations or operating conditions change?

**Value hypothesis to investigate:** make technology-evolution decisions better grounded by clarifying dependencies and technically feasible trajectories.

### Transformation alternatives and investment decisions
Which transformation paths are available? What prior changes does each depend on, and which conditions should be met before resources are committed?

**Value hypothesis to investigate:** compare better-grounded alternatives, reduce investment in options that prove infeasible and improve the justification of decisions.

These five families are broad areas for recognising and framing problems. They are not validated markets, a service portfolio or applications that have passed a fit assessment. The value hypotheses require independent definitions, measures and evidence. Expanding the available transformations does not guarantee better decisions or value creation.

Three levels should remain distinct:
- **Opportunity areas:** broad families in which to recognise problems.
- **Application contexts:** specific systems being explored as candidates.
- **Demonstrators and experiments:** bounded assets for examining particular questions; they do not automatically validate a wider area or application.

## How to interpret status and evidence

The maturity of an asset and the type of evidence available are two different dimensions. For example, TGCV Full Chain Demo is an existing prototype with user-reported local functional acceptance; the cross-domain mapping demonstrator is a synthetic experiment that has been executed and audited; TGCV Playground, Value Explorer and ValueLabsOS Preview are proposed experiences with no verified operational availability; and application contexts remain exploratory candidates.

A prototype may exist and work with synthetic systems without being scientifically validated. A synthetic experiment may have been executed and audited without constituting empirical evidence. And even a deployed application would not, by itself, demonstrate that TGCV provides a distinctive explanation or result.

We therefore describe each piece of work according to what has actually been built, tested or documented. We do not equate software existence, public availability, execution, audit, empirical evidence, deployment and value creation.

At this stage, this page does not offer a general-purpose professional Playground, validated industrial applications, services with guaranteed results, a network of physical laboratories or an open collaboration platform. TGCV Playground, Value Explorer and ValueLabsOS Preview are not presented as available operational tools.

## Discovering new problems and opportunities

We are exploring different TGCV application contexts and also want to discover other problems and opportunities together with people and organisations interested in investigating them.

Your organisation, team or system may be facing a transformation in which capabilities, dependencies or constraints shape what can happen next. We are interested in learning about such contexts and exploring whether they raise relevant research questions.

This invitation is intended to open a conversation and help discover potential cases. It is not a formal collaboration programme and does not imply acceptance, funding, analysis or a commitment to undertake work.

**Explore further:** Research · Systems Engineering · Transformational Intelligence · Value Construction.

---

## Editorial and evidence controls

- Subordinate to Labs & Applications Experience v0.6 and Content Blueprint v3.9.
- Spanish and English preserve the same inventory, statuses and caveats.
- TGCV Full Chain Demo, the cross-domain mapping demonstrator and TGCV Playground are separate.
- Value Explorer is not VALUE; ValueLabsOS Preview is not VALUE or Labs & Applications.
- The five Business Translation families are opportunity areas, not validated markets or services.
- The five additional Application-Fit contexts and three featured contexts remain exploratory candidates.
- No public download, live experience, product function or contact workflow is claimed without verification.
- No content from unrelated initiatives is incorporated.
- Public release remains subject to editorial review and source-by-source publication checks.


## v0.2 review corrections — 2026-11-25

- Clarifies the TGCV Full Chain Demo acceptance record: the user-reported local walkthrough was completed, but the downloaded archive was not independently verified as identical to the package generated by the software release process.
- Makes the cross-domain mapping demonstrator's asset/evidence status explicit without upgrading its bounded synthetic methodological contribution.
- Clarifies that the energy and mobility minimum demonstrator did not use an independent comparison model.
- Adds concrete examples to the explanation that asset maturity and evidence status are separate dimensions.
- Synchronises the document's Content Blueprint reference to v3.6. No scientific claim, application qualification or publication permission is changed.


## v0.3 integrated editorial review — 2026-11-25

- Removes specific functional claims about TGCV Full Chain Demo until the exact distributable package and interface have been verified together, as required by Experience v0.5.
- Preserves the user-reported local functional acceptance record and explicitly distinguishes it from package identity, public availability and scientific validity.
- Synchronises the Content Blueprint reference to v3.7.


## v0.4 reader-language and naming review — 2026-11-25

- Replaces the internal prototype codename with the public name **TGCV Full Chain Demo** throughout the current Spanish and English copy.
- Replaces the internal demonstrator acronym and execution/version identifiers with a plain-language description of the cross-domain synthetic demonstrator and its bounded result.
- Removes the internal case identifier and explains the limitation of the energy/mobility comparison in reader-facing terms.
- Retains EV–Grid as a recognised public-domain term, adding it parenthetically to the descriptive heading in Spanish and English for consistency with Research and the Evidence Portfolio.
- Removes unexplained software-delivery shorthand and repairs the accessibility-calculation sentence.
- Synchronises the parent Content Blueprint reference to v3.8.


## v0.5 naming corrections — 2026-11-25
- Uses **TGCV Playground** and **ValueLabsOS Preview** for the two proposed visitor experiences.
- Uses **Demostrador de cadena completa de TGCV** in the Spanish page text for the existing prototype; retains **TGCV Full Chain Demo** in the English page text.
- Preserves the distinction between the existing software prototype and the proposed TGCV Playground experience.

- **v0.5 — 2026-11-25:** applies the requested visitor-facing names and localises the existing prototype name in Spanish while retaining its English name in the English copy.

- **v0.6 — 2026-11-25:** removes Contact from the active visitor-route list until a real, monitored public channel and page are available.
