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

- Taxonomía S1–S8: reutilizada, sin ampliación.
- Clase semántica focal mínima: S7, con inclusión/exclusión focal explícita.
- Identidad/binding, provenance/integridad/tiempo y marco de cobertura: controles obligatorios de referencia/admisibilidad; no evidencia semántica independiente.
- S5 funcional: condicional al contexto interpretativo.
- S2/S4 técnicos y S3/S6/S8 operativos: opcionales/no sustitutivos para Need.
- Universo esperado: oportunidades IN_SCOPE enumeradas y selladas ex ante por UE×dimensión; su cardinalidad y regla concreta siguen OPEN.
- Cobertura material: permanece NONE; no hay roster, oportunidades, fuentes ni adjudicaciones por unidad.
- No se han materializado registros, fijado parámetros/probabilidades, ejecutado pruebas, DGP, Analyzer, simulaciones o replay.

La propuesta requiere reconciliación final con el contrato fuente S1–S8 y con la representación lógica del COVERAGE_REGISTER antes de considerarse lista para implementación. Se mantienen `scientific_execution=false` y `execution_authorized=false`.
