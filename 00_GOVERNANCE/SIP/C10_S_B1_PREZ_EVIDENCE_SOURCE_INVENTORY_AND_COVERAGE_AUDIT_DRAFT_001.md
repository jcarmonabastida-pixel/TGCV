# C10-S — B1: inventario de fuentes pre-Z y auditoría de cobertura de Need_preZ

**ID:** C10-S-B1-PREZ-SOURCE-INVENTORY-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-11  
**Estado:** REPOSITORY_DESIGN_SOURCES_REVIEWED / UNIT_LEVEL_PREZ_EVIDENCE_NOT_FOUND_IN_REVIEWED_ARTIFACTS / COVERAGE_NONE / ADJUDICATION_BLOCKED  
**Rama:** research/c10-s-consolidation-draft · **PR de trabajo:** #116 (Draft; verificar metadatos de head/base antes de cualquier operación PR)  
**Alcance:** revisión documental read-only de artefactos C10-S ya existentes en la rama. No inspección de sistemas externos, conectores, sistemas reales, entornos runtime ni repositorios locales.

## 1. Pregunta y criterio de auditoría

¿Existen en el repositorio fuentes pre-Z que permitan, para cada unidad B1/UE, identificar la entidad, su servicio asociado, el objetivo funcional basal aceptado y la verdad/adjudicación de Need_preZ con fecha, versión, provenance y cobertura suficientes?

La auditoría distingue cuatro clases que no se sustituyen:
1. **Artefactos de diseño:** especifican qué deberá representar el DGP.
2. **Truth del DGP:** estipulación generadora pre-Z por unidad, segregada del Analyzer.
3. **Evidencia observada pre-Z:** fuentes que un adjudicador/Analyzer podría consultar sin acceder a truth reservada.
4. **Evidencia técnica del servicio/configuración:** contratos, IAM, snapshots, manifiestos y observaciones; puede respaldar características del servicio, pero no demuestra por sí sola que B1 tenga el objetivo basal.

La revisión de documentos de diseño no se cuenta como evidencia observada de una unidad sintética ni como materialización de truth.

## 2. Artefactos revisados y alcance probatorio

| Artefacto del repositorio | Clase de fuente aplicable | Qué respalda legítimamente | Qué no respalda |
|---|---|---|---|
| C10_S_B1_REQUESTING_ENTITY_CANDIDATE_SPEC_DRAFT_001.md §§1–10 y decisiones PB | S7 — especificación/diseño | Tipo candidato B1; distinción Need/demanda/solicitud; una B1 por UE como decisión de diseño; oportunidad estandarizada; límites de inferencia | Identidad/Need de una UE concreta; truth DGP material; declaración pre-Z individual |
| C10_S_B1_VALUATION_CASE_RECONCILIATION_DRAFT_001.md §§12–15 | S7 — reconciliación de diseño | Aceptación del propósito basal y especialización funcional de trabajo; límites de la definición | Evidencia natural o individual de necesidad; registro operativo pre-Z por UE |
| C10_S_B1_PREZ_ADJUDICATION_AND_CONSEQUENCE_RECONCILIATION_DRAFT_001.md | S7 — contrato de adjudicación | Reglas conceptuales truth/observed, 1/0/? y separación de consecuencias | Evidencia primaria; roster; adjudicaciones efectivas |
| DEC-C10-068 y C10_S_SYNTHETIC_LOGICAL_SERVICE_FUNCTIONAL_CONTRACT_DRAFT_001.md | S5 — contrato funcional | Servicio lógico, parámetros ENABLED/PROFILE y regla declarativa aceptada | Que B1 tenga una necesidad concreta; comportamiento implementado; admisión o procesamiento observados |
| DEC-C10-069 y decisión de identidad de servicio por UE reflejada en PB/maestro | S5/S7 — contrato e identidad de diseño | Requisito de instancia de servicio única/versionada por UE, con plantilla común | IDs concretos, instancias creadas, aislamiento efectivo o vínculo material B1–UE–servicio |
| C10_S_B2_B3_BENEFICIARY_OUTCOME_VALUE_RECONCILIATION_DRAFT_001.md | S7 — reconciliación de diseño | Separación Need, Outcome, consecuencia B1 y Value; perspectiva aún pendiente | Fuente basal individual, perspectiva/autoridad ya adjudicadas o medida observada |
| C10_S_UG_EVIDENCE_PROVENANCE_AND_ADJUDICATION_PROTOCOL_DRAFT_001.md | Protocolo metodológico S1–S8 | Taxonomía de fuentes, provenance, cegamiento, 1/0/? y cobertura | Existencia de una fuente concreta; inspección real; cobertura lograda |
| C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md §§2–7, 12 | Plantilla de captura | Campos requeridos para NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT/EVIDENCE/COVERAGE | Registros observados: la plantilla declara expresamente estar vacía y no inventariada |
| C10_S_GRAPH_COVERAGE_AND_TRIVALENT_EVIDENCE_MATRIX_DRAFT_001.md | Catálogo/cobertura de diseño | Universo candidato U_G, predicados y rutas que requerirán inspección | Universo real/exhaustivo, presencia/ausencia, evidencia por unidad |
| C10_S_RECOVERY_165_183_SOURCE_REGISTER_DRAFT_001.md | S7 — fuente metodológica histórica | Recuperación documental de propuestas P179–P183 y límites de su estado | Evidencia de B1, registros pre-Z o pruebas ejecutadas |

Los artefactos de diseño son evidencia de decisiones y contratos de diseño; no se promocionan a evidencia observada de necesidad por unidad. No se localizó en el conjunto revisado un registro de declaración basal individual, requisito funcional de una B1 concreta, roster material o expediente de evidencia enlazado a una unidad.

## 3. Crosswalk de fuentes candidatas para Need_preZ

La clasificación siguiente identifica fuentes que serían pertinentes si existieran y fueran autorizadas; no afirma que estén disponibles.

| Fuente candidata | Clase protocolo | Afirmación potencial | Condiciones para admisión | Estado en artefactos revisados |
|---|---|---|---|---|
| Declaración/objetivo operativo basal firmado o aprobado por B1 antes de Z | S7 | Existencia del propósito focal | Autoridad/rol, fecha pre-Z, identidad B1, versión, alcance y vínculo con servicio | No localizado por unidad |
| Especificación funcional/requisito operativo del servicio consumido por B1 | S5/S7 | Función concreta que B1 pretende mantener | Contrato versionado, trazabilidad B1–servicio y evidencia de vigencia pre-Z | Solo contrato lógico genérico; operación posterior no especificada |
| Catálogo/registro de B1 y relación B1–UE–service_instance_id | S1/S5/S7 | Identidad y relación de la unidad | Universo y cardinalidad cerrados, IDs versionados, provenance, timestamps | Decisión de cardinalidad documentada; roster e IDs no materializados |
| Registro de configuración declarada pre-Z, IAM/ACL y estado ENABLED/PROFILE | S2 | Estado declarativo de la instancia de servicio | Snapshot exacto, identidad/versión, autoridad, integridad, tiempo anterior a Z | No se localizó snapshot IAM/configuración por UE |
| Snapshot basal inmutable y su expediente de integridad | S4 | Estado de configuración/servicio en un instante basal | Hash, scope, método, custodio, cobertura y binding exacto a B1/UE/instancia | Plantilla vacía; sin snapshots capturados |
| Tickets, solicitudes históricas, manuales o entrevistas con custodios | S7 | Descubrimiento/contexto del objetivo y uso previsto | Fecha, autoría, vigencia, corroboración y control de sesgo/retrospección | No localizados por unidad; además, no usar ausencia de solicitudes para Need=0 |
| SBOM, lockfile, manifiesto o inventario de paquete | S1 | Identidad/dependencias declaradas del servicio | Digest/versionado y scope exacto | No localizado como artefacto técnico de instancia B1 |
| Logs, trazas, métricas o pruebas funcionales | S3/S6 | Uso, admisión, procesamiento o capacidad técnica | Ventana, muestreo, oráculo, integridad y cegamiento | No localizados ni autorizados; en todo caso son post-Z/funcionales y no prueban Need_preZ |
| Análisis estático/cierre transitivo | S8 | Dependencias inferidas | Método reproducible, versión, límites y corroboración | No ejecutado; no es fuente directa de Need basal |

### 3.1 Fuentes que no pueden sustituir Need_preZ

No se aceptan como sustitutos de la necesidad basal:
- Request_opportunity, Request_attempt, Request_received, Request_admitted/rejected, processing o response;
- éxito de migración, instalación de adaptador, F*, O-CONF, ΔT_acc*, Reach, selección o ejecución;
- consumo de recursos o demanda técnica del servicio;
- una oportunidad estandarizada post-snapshot;
- ausencia de logs, ausencia de solicitud o búsqueda sin resultados.

Pueden informar otros constructos o mecanismos, pero no redefinir la verdad basal.

## 4. Matriz de cobertura documental

| Dimensión crítica | Universo/denominador | Evidencia examinada | Cobertura | Dictamen |
|---|---|---|---|---|
| Identidad B1 por UE | Roster completo de UE/B1 | Contratos de diseño; no roster | NONE | IDs concretos no disponibles |
| Binding B1–UE–service instance | Todas las UE del universo | Decisión de identidad/cardinalidad; sin registros por unidad | NONE | Relación material no verificable |
| Declaración del objetivo basal | Todas las B1/UE | Aceptación conceptual global; sin declaraciones individuales | NONE | No permite truth/adjudicación por unidad |
| Contrato funcional específico aplicado a cada instancia | Todas las instancias versionadas | DEC-C10-068 y contrato lógico genérico | PARTIAL a nivel de definición de plantilla; NONE por unidad | Habilitación/perfil definidos; semántica de operación concreta y mapping por instancia abiertos |
| Configuración/IAM pre-Z | Todas las instancias y superficies relevantes | Reglas/plantillas, sin snapshot | NONE | No puede adjudicarse estado declarado por unidad |
| Snapshot basal e integridad | Todas las UE/instancias y ventanas pre-Z | Plantilla de snapshot sin filas reales | NONE | No hay artefacto inmutable ni hash |
| Provenance/custodia/autoridad | Todas las fuentes de las unidades | Protocolo y esquema documental | NONE a nivel de fuentes concretas | Campos definidos; expedientes no poblados |
| Cobertura negativa para Need=0 | Universo cerrado de fuentes por B1/UE | Sin denominador ni fuentes examinadas por unidad | NONE | No se puede adjudicar 0 |
| Truth DGP por unidad | Todas las UE del DGP | Definición conceptual y reglas; sin tabla/registro generador por unidad | NONE / NOT MATERIALIZED | No hay verdad individual que comparar |
| Evaluación independiente E1/E2 | Todas las unidades adjudicables | Protocolo y plantilla sin evaluaciones | NONE | No hay adjudicaciones ni concordancia |

**Interpretación:** NONE indica que no se ha cubierto ninguna unidad de la dimensión mediante una inspección material válida; no significa que el objeto o la necesidad no existan. PARTIAL en la definición de plantilla del servicio se limita al contrato genérico y no mejora la cobertura de unidad.

## 5. Resultado de adjudicabilidad por unidad

No existe roster material que permita enumerar UE y B1. Por tanto, no se emite una tabla ficticia de casos ni se asigna un estado a unidades inexistentes en el registro.

Para cualquier futura unidad que se pretendiera adjudicar con el material actualmente revisado:
- **Truth DGP:** NOT MATERIALIZED; no asignable a unidad.
- **Observed Need_preZ:** ? / BLOCKED por ausencia de fuente basal individual, identidad/versionado material y cobertura.
- **Observed 0:** no admisible, porque no hay universo de fuentes cerrado ni cobertura negativa.
- **Observed 1:** no admisible, porque la aceptación conceptual global no está vinculada a una B1/UE concreta con declaración/provenance pre-Z.
- **Observed ?:** dictamen correcto mientras falten esos elementos; no equivale a truth DGP ? ni a Need=0.

La truth del generador, cuando se especifique, debe ser segregada del Analyzer. La auditoría presente no solicita ni produce un registro secreto de truth.

## 6. Brechas y condiciones de desbloqueo

| Brecha | Evidencia mínima necesaria para resolverla | Estado |
|---|---|---|
| B1/UE/servicio sin IDs materiales | Roster de diseño autorizado y crosswalk versionado de identidades | OPEN |
| Objetivo basal global sin declaración por unidad | Regla DGP que estipule Need por unidad y, separadamente, fuente observada admisible | OPEN |
| Semántica funcional posterior no definida | Payload/operación y relación con el objetivo solo si son necesarios para distinguir la necesidad basal | OPEN; no bloquea el propósito mínimo aceptado |
| Sin fuentes observadas pre-Z | Inventario de documentos/registros por unidad con custodio, fecha, versión, integridad y alcance | OPEN |
| Sin universo/denominador de cobertura | Regla de enumeración y COVERAGE_REGISTER por dimensión y unidad | OPEN |
| Sin evaluación independiente | E1/E2 y adjudicación según protocolo, una vez existan fuentes válidas | OPEN |

El siguiente trabajo permitido sigue siendo documental: definir el catálogo de tipos de fuente y el criterio de cobertura por unidad; no generar roster ni fuentes. La materialización de unidades, truth, snapshots o evidencias exige autorización y contrato específico posteriores.

## 7. Dictamen

**REPOSITORY DESIGN ARTIFACTS REVIEWED; NO MATERIAL UNIT-LEVEL PRE-Z SOURCE EVIDENCE FOUND IN THE REVIEWED C10-S ARTIFACT SET.**

- Need_preZ está definido a nivel conceptual/funcional de trabajo.
- La arquitectura de provenance y adjudicación existe documentalmente.
- No existe evidencia suficiente para adjudicar Need_preZ=1 o 0 por B1/UE.
- La cobertura material para identidad, objetivo basal, IAM/configuración pre-Z, snapshots y adjudicación es NONE.
- La clasificación por unidad permanece ? / BLOCKED si se pretendiera aplicar hoy el procedimiento.
- No se infiere ausencia de necesidad ni se fuerza población ITT.

Este dictamen está limitado a los artefactos C10-S revisados en la rama indicada. No afirma que no existan documentos fuera del repositorio ni en sistemas externos no consultados.

## 8. Gobernanza y límites

No se cambia main, RMA, Evidence→Claim Matrix, STATUS, claims, DEC-C10-068/069 ni las decisiones B1 aceptadas. No se crea verdad por unidad, roster, snapshot, fixture, dataset ni fuente. No se ejecuta búsqueda en sistemas reales, inspección runtime, captura, simulación, estimación o experimento. No Design Freeze ni autorización de implementación/ejecución.

scientific_execution=false; execution_authorized=false.


## 9. Incorporación del modelo operativo de observación (DEC-C10-097)

DEC-C10-097 acepta las reglas de diseño para marco de fuentes, emisión, captura, contenido, admisibilidad, integridad, temporalidad, vinculación, adjudicación E1/E2 y cobertura por unidad×dimensión. Esta aceptación es normativa/documental: **no cambia el resultado material de esta auditoría**. La cobertura por unidad continúa siendo NONE en el conjunto de artefactos revisados; no hay roster, fuentes, truth, snapshots ni adjudicaciones materializados. No se convierte la aceptación del modelo en evidencia observada ni en PASS de adjudicabilidad.


## 10. Cierre propuesto del conjunto mínimo de clases de fuente y del universo esperado (2026-11-12)

### 10.1 Resultado de la reconstrucción histórica

La revisión conjunta de este inventario, del contrato del paquete analítico §6–§10 y de la reconciliación operativa DEC-C10-097 §2–§9 muestra que el problema no es la ausencia de una taxonomía general: ya existen las clases S1–S8 y las dimensiones del proceso de observación. Tampoco procede convertir cada candidato del inventario en una fuente obligatoria.

El cierre necesario es identificar qué clases cumplen una función indispensable para adjudicar el objetivo focal y cuáles solo aportan contexto técnico. Se conserva la taxonomía existente; esta sección no crea clases S nuevas ni sustituye U_G.

### 10.2 Clases funcionales mínimas

Se propone el siguiente perfil mínimo lógico, condicionado a que cada elemento exista y sea admisible en la instancia sintética:

| Función | Clase existente | Necesidad | Alcance probatorio y límite |
|---|---|---|---|
| Identidad y binding B1–UE–service instance | S1/S5/S7, según el tipo de registro | Obligatoria como control de referencia | Identifica el referente y su versión; no prueba Need |
| Declaración focal del objetivo basal | S7 | Obligatoria como oportunidad de evidencia semántica | Debe poder contener inclusión focal o exclusión focal explícita, con emisor/autoridad, alcance y vigencia pre-Z. Su contenido observado no es la truth reservada |
| Contexto funcional del servicio/objetivo | S5/S7 | Condicional, solo cuando sea necesario para interpretar alcance o correspondencia | Aclara qué servicio y función se declaran; no demuestra por sí mismo que B1 tenga el objetivo |
| Provenance, integridad y temporalidad de cada artefacto | Metadatos de control del EVIDENCE_LEDGER y protocolo existente | Obligatoria para admisibilidad, no una fuente semántica adicional | Autoría, versión, digest, event_time, capture_time, custodio y cadena de captura |
| Marco de fuentes esperadas y cierre de cobertura | COVERAGE_REGISTER / alcance declarado ex ante | Obligatorio para declarar cobertura | Define qué oportunidades pertenecen al alcance y cómo se enumeran; no constituye evidencia de Need |
| Snapshot técnico/IAM/configuración | S2/S4 | No obligatorio para adjudicar Need | Puede respaldar ENABLED/PROFILE, ACL, configuración o estado técnico. No sustituye la declaración focal |
| Logs, métricas, pruebas de operación, solicitudes y trazas | S3/S6/S7/S8 según origen | No obligatorios y, en general, no probatorios de Need_preZ | Informan operación, uso, capacidad o ejecución; no se promueven a evidencia del objetivo basal |

La configuración mínima no exige que todas las unidades tengan el mismo número de artefactos ni que se materialicen todas las clases técnicas. Exige que el alcance declarado para cada unidad/dimensión sea explícito, enumerable y evaluable. La clase S7 focal es la única clase semántica candidata indispensable para observar inclusión/exclusión de Need; identidad, provenance y cobertura son controles transversales de admisibilidad, no tres fuentes probatorias independientes.

### 10.3 Dos rutas probatorias, no una falsa simetría

El modelo debe poder representar al menos dos contenidos semánticos distintos en la clase focal:

- **Declaración de inclusión:** afirma el objetivo funcional basal aceptado para B1–servicio.
- **Declaración de exclusión:** niega explícitamente ese objetivo focal, dentro de un alcance y autoridad válidos.

No se exige que ambas declaraciones existan para cada unidad. La truth se genera por configuración explícita reservada conforme a DEC-C10-095; el mecanismo de observación genera, omite, pierde, captura, altera o vuelve ambiguo el artefacto observable conforme al modelo aprobado. No se copia la etiqueta truth ni se transforma la configuración reservada en el documento visible.

Una declaración no localizada, no emitida, perdida, opaca o no admisible produce insuficiencia/abstención; no una declaración de exclusión. La cobertura COMPLETE tampoco sustituye la afirmación negativa focal.

### 10.4 Cierre del universo esperado por unidad y dimensión

El universo esperado no será «todos los documentos que podrían existir» ni «todos los documentos encontrados». Se define como el conjunto versionado de oportunidades de fuente que el escenario DGP declara dentro del alcance para la afirmación focal de esa UE.

La unidad mínima de enumeración es:

`(package_version, UE_id, B1_id, service_instance_id, claim_dimension, source_opportunity_id, scope_version)`

Esta tupla es una clave lógica de control, no un schema físico aprobado. Cada oportunidad debe tener una regla reproducible de pertenencia al alcance. El universo se cierra antes de generar resultados de emisión/captura y antes de adjudicar; no puede ampliarse o reducirse después de observar qué fuentes favorecen una clasificación.

Se distinguen:
- `IN_SCOPE`: oportunidad incluida en el universo esperado;
- `OUT_OF_SCOPE`: excluida por regla ex ante, con motivo;
- `UNENUMERABLE/OPAQUE_SCOPE`: no se puede cerrar la superficie; impide COMPLETE;
- `ENUMERATED_CLOSED`: universo de oportunidades enumerado y sellado.

La emisión, captura, pérdida, contenido y admisibilidad son estados posteriores de cada oportunidad `IN_SCOPE`; no alteran retroactivamente su pertenencia. El denominador de cobertura se obtiene del universo `IN_SCOPE` sellado, nunca del número de artefactos encontrados.

No se fija cardinalidad de oportunidades ni se inventan source_opportunity_id. Su cardinalidad y regla de enumeración deberán derivarse del contrato de fuente que se apruebe para el microdominio; no se presupone una oportunidad por cada tipo S ni una fuente por cada UE.

### 10.5 Reglas de no redundancia y no contaminación

1. Un artefacto derivado, copia, export o representación de la misma declaración no cuenta como corroboración independiente.
2. Varios registros del mismo emisor/canal/plantilla pueden ser dependientes; la dependencia se conserva, no se infiere independencia por multiplicidad.
3. Los registros de identidad, servicio, IAM, snapshot y cobertura no se cuentan como fuentes semánticas de Need.
4. La truth ledger y cualquier referencia reservada permanecen fuera del expediente observable.
5. La selección y enumeración del marco no dependen de truth, emisión observada, Z, D2, instalación, accesibilidad, Reach, trayectoria, ejecución, Outcome, Value ni decisiones E1/E2.
6. La generación del contenido de una declaración sí puede depender de truth a través del modelo de observación aprobado; esto no autoriza a revelar la etiqueta o sus metadatos reconstructivos.
7. No se exige enumeración exhaustiva de todos los objetivos de B1: se conserva la exclusión focal explícita aceptada por DEC-C10-095.

### 10.6 Dictamen y estado

**RECOMMENDED MINIMUM PROFILE — DOCUMENTARY / NOT FROZEN.**

### 10.7 Corrección de autoridad probatoria S7 y contrato de declaración focal

La asignación de una fuente a S7 no la convierte por sí sola en evidencia primaria. Conforme al protocolo U_G §3, la jerarquía depende de la afirmación. Manuales, tickets, diagramas y entrevistas de custodios se tratan como fuentes de descubrimiento/contexto y no bastan por defecto para adjudicar el objetivo basal.

Para la afirmación específica «el objetivo focal forma/no forma parte de los objetivos basales declarados de esta B1 respecto de esta instancia de servicio en t−1», se admite como candidata directa una **declaración basal original y controlada**. Su admisibilidad depende del acto declarativo y de su autoridad, no de la etiqueta S7. La declaración deberá cumplir conjuntamente:

1. **Emisor identificable:** persona/rol o autoridad sintética emisora, con identidad y versión trazables; el generador no puede inventar autoridad implícita.
2. **Competencia declarativa:** regla explícita del DGP que atribuye al emisor autoridad para declarar el objetivo basal de la B1; ser custodio técnico del servicio no confiere por sí solo esa competencia.
3. **Referente inequívoco:** B1, UE, instancia lógica de servicio y versiones exactas, sin binding por proximidad o nombre libre.
4. **Tiempo:** declaración fijada en t−1; una captura posterior solo puede ser copia íntegra de un artefacto fijado antes de Z, con event_time y capture_time diferenciados.
5. **Proposición focal explícita:** inclusión o exclusión del objetivo funcional definido en el contrato B1; no basta una descripción general, una configuración ENABLED/PROFILE ni una inferencia del adjudicador.
6. **Alcance:** relación B1–servicio y ámbito al que se refiere la afirmación; la exclusión es focal, no una afirmación sobre todos los objetivos posibles de B1.
7. **Integridad/provenance:** versión, digest o control equivalente, custodio/canal de captura, lineage y evidencia de que el artefacto no es una copia derivada presentada como corroboración independiente.
8. **Accesibilidad observacional:** el expediente visible no contiene truth, truth_basis_ref, etiquetas internas, claves, semillas ni metadatos que permitan reconstruir directamente la estipulación reservada.

Se define el tipo lógico candidato S7_B1_BASELINE_OBJECTIVE_ATTESTATION para identificar este tipo de acto/artefacto dentro de S7. Es un nombre de tipo, no una nueva clase S, entidad U_G, tabla física, ID de prueba ni afirmación de que exista una fuente materializada.

**Contenido observable permitido:** la declaración expresa la proposición focal como afirmación de inclusión o exclusión, junto con referente, alcance, emisor/autoridad, vigencia y provenance. No contiene el campo interno need_truth_state ni referencias al registro reservado. La observación puede emitir, omitir, perder, capturar, volver ambigua o corromper la declaración, y puede generar contenido semánticamente erróneo según el modelo aprobado; no se fija aquí ninguna tasa. La salida observable no se obtiene copiando una fila de TRUTH_LEDGER.

**Independencia y corroboración:** copias, exports, transcripciones o documentos derivados de la misma declaración comparten un lineage y cuentan como una sola raíz probatoria. Fuentes S5/S7 adicionales solo corroboran si son genuinamente distintas en origen y autoridad; no se presupone independencia. Si no hay una declaración original admisible, E1/E2 no pueden inferir observed=1/0 a partir de snapshots técnicos, logs, solicitudes, ausencia de documentos o manuales genéricos: corresponde abstención/observed=? o bloqueo de integridad según el defecto.

Esta especialización no altera la taxonomía S1–S8 ni las reglas generales de evidencia negativa U_G. El tipo focal S7 no elimina la necesidad de cobertura: para observed=0 se requiere la exclusión focal afirmativa admisible; COMPLETE sin ella no basta.

- Taxonomía S1–S8: reutilizada, sin ampliación.
- Clase semántica focal mínima: S7, con inclusión/exclusión focal explícita.
- Identidad/binding, provenance/integridad/tiempo y marco de cobertura: controles obligatorios de referencia/admisibilidad; no evidencia semántica independiente.
- S5 funcional: condicional al contexto interpretativo.
- S2/S4 técnicos y S3/S6/S8 operativos: opcionales/no sustitutivos para Need.
- Universo esperado: oportunidades IN_SCOPE enumeradas y selladas ex ante por UE×dimensión; su cardinalidad y regla concreta siguen OPEN.
- Cobertura material: permanece NONE; no hay roster, oportunidades, fuentes ni adjudicaciones por unidad.
- No se han materializado registros, fijado parámetros/probabilidades, ejecutado pruebas, DGP, Analyzer, simulaciones o replay.

La propuesta requiere reconciliación final con el contrato fuente S1–S8 y con la representación lógica del COVERAGE_REGISTER antes de considerarse lista para implementación. Se mantienen `scientific_execution=false` y `execution_authorized=false`.



### 10.8 Reconciliación de señal y función emisora (DEC-C10-097)

La lectura conjunta de §§10.2–10.7 con el contrato de observación/cobertura y las secciones 7.7/14.6 de los contratos B1 resuelve la ambigüedad entre «emisor» y «señal»:

- La única clase semántica mínima sigue siendo S7: declaración focal original de inclusión o exclusión. S1/S5/S7 de identidad, provenance y binding son controles de referencia; S5 funcional contextual es condicional; S2/S4 y fuentes operativas no sustituyen Need.
- No se ha identificado una señal basal independiente que un actor deba recibir. Los candidatos técnicos ya descartados no pueden reintroducirse como conocimiento del emisor.
- El artefacto S7 lo produce el canal de observación. La autoridad/rol/mandato del emisor es atribución de provenance ex ante, no un modelo cognitivo ni un quinto rol PE. El estado interno del canal, si existe, no se exporta.
- El canal puede generar contenidos correctos o erróneos, ambiguos, conflictivos, omitidos o perdidos; no se fijan tasas ni parámetros. La truth influye a través del mecanismo de observación ya aceptado por DEC-C10-097, nunca por copia literal ni filtración lateral.
- Una sola clase S7 puede soportar las dos proposiciones focales (inclusión/exclusión); no se requieren dos clases distintas ni corroboración múltiple. La suficiencia real dependerá del alcance, integridad, autoridad, temporalidad y cobertura de cada oportunidad.

Esto no cierra el tipo concreto de fuente del microdominio ni la regla de autoridad, cardinalidad de oportunidades o sus parámetros. La selección del microdominio sigue rigiendo qué artefacto declarativo puede tener semántica plausible; no se inventa una fuente realista antes de esa decisión.

**Estado:** reconciliación documental; perfil mínimo recomendado, no congelado. Sin fuentes, roster ni oportunidades materializadas; sin implementación o ejecución.


### 10.9 Propuesta de enumeración mínima de oportunidades S7 por UE (2026-11-12)

Esta propuesta cierra el análisis de alternativas para el universo esperado, sin aceptar todavía un mandato emisor ni autorizar materialización.

#### 10.9.1 Restricciones históricas aplicables

La reconstrucción conjunta establece que:
- DEC-C10-051 selecciona Opción A (migración de configuración entre dos entornos software) como microdominio de trabajo, y adopta F* solo como contrato funcional candidato.
- La definición funcional B1/Need_preZ está aceptada documentalmente; su truth por unidad procede de estipulación reservada conforme a DEC-C10-095.
- DEC-C10-096 fija la cohorte de validación como censo de todas las UE del roster DGP/paquete B1 aprobado, no una subcohorte.
- DEC-C10-097 exige un marco de oportunidades enumerable ex ante por UE×dimensión, y prohíbe que COMPLETE equivalga automáticamente a observed=0.
- La oportunidad estandarizada de petición N_opportunities=1 pertenece al probe post-snapshot t3/t4. No es una oportunidad de fuente S7, no ocurre en t−1 y no puede reutilizarse para adjudicar Need_preZ.
- El inventario §10.2–10.8 identifica S7 como única clase semántica mínima para la declaración focal de inclusión/exclusión. S1/S5/S7 de identidad, binding y provenance son controles transversales; no son fuentes semánticas adicionales.

#### 10.9.2 Alternativas de enumeración

| Alternativa | Descripción | Evaluación |
|---|---|---|
| A. Una oportunidad S7 focal por UE | Un slot lógico versionado para una declaración basal de B1 sobre inclusión o exclusión del objetivo focal; puede emitirse, omitirse, perderse, resultar ambiguo o contener error | **Mínima y parsimoniosa**; permite ambas polaridades sin multiplicar fuentes |
| B. Varias oportunidades S7 por UE | Declaraciones separadas de B1, aprobación, requisito y/o registro histórico | No justificada aún; exige autoridades, dependencias, lineage y reglas de conflicto que no están especificadas |
| C. Fuente global compartida | Un contrato general del servicio común a todas las UE | No identifica por sí solo el objetivo basal de una B1 concreta; no sustituye la declaración individual |
| D. Petición estandarizada post-Z | El probe común de servicio ya aceptado | Inadmisible para Need_preZ: es posterior a Z y no prueba el objetivo basal |

#### 10.9.3 Perfil mínimo recomendado

Se recomienda que el universo esperado contenga **una oportunidad lógica S7 por cada UE incluida en el censo B1/Need**, con estas propiedades:

1. La oportunidad representa la posibilidad de producir una declaración focal basal atribuida a B1 sobre si el objetivo funcional aceptado forma parte de sus objetivos en t−1.
2. Su clave lógica se vincula a package_version, UE_id, B1_id, service_instance_id, claim_dimension=Need_preZ, source_opportunity_id y scope_version, conforme a la tupla lógica ya propuesta en §10.4. No se crean IDs concretos ni schema físico.
3. La oportunidad y su alcance se enumeran y sellan ex ante para todas las UE del roster aprobado, antes de generar el estado de emisión/contenido y antes de adjudicar. No se condiciona su existencia a need_truth_state, Z, evidencia encontrada o resultados.
4. La oportunidad puede producir una declaración de inclusión, una declaración de exclusión focal, una declaración ambigua/conflictiva o ninguna declaración capturada. La ausencia de emisión/captura produce insuficiencia, no exclusión.
5. observed=0 requiere que el artefacto contenga una exclusión focal afirmativa y admisible; que el universo de oportunidades esté COMPLETE no sustituye ese contenido.
6. Una copia o derivado de la misma declaración no constituye una segunda oportunidad ni corroboración independiente; conserva el mismo lineage.
7. El emisor propuesto es B1 como declarante de su propio objetivo basal, mediante una atribución ex ante de autodeclaración limitada a su propósito y alcance. Esto es una hipótesis de mandato, no una autoridad ya aceptada: B1 no adquiere competencia sobre configuración técnica, IAM, servicio ni objetivos de terceros. La autenticidad de origen no garantiza exactitud semántica.
8. El canal observacional, no una cognición simulada del emisor, genera el artefacto visible y puede introducir errores, ambigüedad, omisión o pérdida según escenarios y parámetros que deberán justificarse después. No se copia need_truth_state ni se exportan secretos o canales laterales.

#### 10.9.4 Qué resuelve y qué no

Si se acepta, esta propuesta cerraría únicamente la cardinalidad lógica mínima del marco de oportunidades: una oportunidad S7 por UE. No fijaría:
- roster, número de UE ni IDs;
- prevalencia o proporción de truth 1/0/?;
- probabilidad de emisión, error, ambigüedad o pérdida;
- dependencia entre oportunidades (la configuración mínima no presupone múltiples oportunidades);
- formato del artefacto, contenido físico, firma, almacenamiento o schema;
- parámetros del canal ni su estructura estadística;
- suficiencia estadística, potencia o precisión;
- autorización de materialización, implementación o ejecución.

El soporte de truth=1 y truth=0 continúa siendo un gate sobre el censo aprobado. La presencia de una oportunidad S7 por UE no garantiza soporte de clases ni una declaración observable en cada unidad.

**Recomendación sometida a aceptación:** adoptar una oportunidad lógica S7 de autodeclaración basal B1 por UE como universo mínimo cerrado, distinguiéndola expresamente de la oportunidad estandarizada de petición post-Z. Mantener abierta la aceptación del mandato de autodeclaración de B1 y la especificación del canal observacional.

**Estado:** propuesta de diseño; NO DECISION ACCEPTED / NO DESIGN FREEZE / NO MATERIALIZATION / NO EXECUTION.



### 10.10 Estado de §10.9 tras DEC-C10-098

La recomendación de §10.9 queda aceptada como diseño de trabajo por DEC-C10-098: una oportunidad lógica S7 por cada UE del censo B1/Need aprobado y versionado. Se retira la condición «recomendación sometida a aceptación» y la cardinalidad lógica deja de estar OPEN.

La aceptación no convierte la oportunidad esperada en documento emitido, fuente material, captura, evidencia admisible ni adjudicación. La cobertura material continúa NONE mientras no exista roster ni materialización autorizada.

El mandato se acota a autodeclaración de B1 sobre su propio objetivo operativo focal y su vínculo con UE/instancia lógica de servicio. No atribuye autoridad sobre configuración técnica, IAM, servicio ejecutor ni objetivos de terceros. Identidad concreta, versión de mandato y prueba de autoridad/provenance permanecen como requisitos de implementación.

Quedan OPEN: el mecanismo condicional de emisión/contenido, sus estados de error y dependencia, captura/pérdida, escenarios de sensibilidad, formato físico y parámetros justificados. La oportunidad se enumera antes de verdad observacional, emisión/captura y adjudicación; no se condiciona a Z, D2, resultados o evidencia encontrada.

**Estado:** cardinalidad lógica ACCEPTED WORKING DESIGN (DEC-C10-098); fuente material NONE; NO DESIGN FREEZE / NO MATERIALIZATION / NO EXECUTION.
