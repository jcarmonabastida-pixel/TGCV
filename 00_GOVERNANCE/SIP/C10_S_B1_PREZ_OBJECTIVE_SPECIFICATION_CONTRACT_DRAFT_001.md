# C10-S — Contrato de estipulación basal del objetivo B1 para Need_preZ

**ID:** C10-S-B1-PREZ-OBJECTIVE-SPECIFICATION-CONTRACT-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** USER_ACCEPTED_DESIGN_PRINCIPLE / DEC-C10-095_ACCEPTED_WORKING_DESIGN / CONTRACT_DRAFT / NOT_DESIGN_FROZEN / NOT_IMPLEMENTED / NOT_MATERIALIZED / NOT_EXECUTED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)

## 1. Autoridad, alcance y antecedentes

Este contrato desarrolla el principio de diseño aceptado expresamente por el usuario el 2026-11-12: la truth de `Need_preZ` se genera a partir de una especificación sintética explícita del objetivo operativo basal de cada B1, independiente de las covariables causales basales y de la configuración técnica del servicio.

Se subordina a:
- `C10_S_B1_PREZ_ADJUDICATION_AND_CONSEQUENCE_RECONCILIATION_DRAFT_001.md`, especialmente §§3–5 y 9.
- `C10_S_B1_REQUESTING_ENTITY_CANDIDATE_SPEC_DRAFT_001.md`, especialmente §10 y las decisiones B1 posteriores.
- `C10_S_B1_PREZ_ANALYTICAL_PACKAGE_CONTRACT_DRAFT_001.md`.
- `C10_S_B1_PREZ_TEMPORAL_RECONCILIATION_DRAFT_001.md`.
- `C10_S_B1_PREZ_BASELINE_SOURCE_DIAGNOSTIC_DRAFT_001.md`.
- Contrato temporal/roles DGP y decisiones aceptadas B1/UE/servicio.

No sustituye ni reabre la definición funcional aceptada de Need_preZ, la cardinalidad B1–UE, la identidad de instancia de servicio, DEC-C10-061, la composición de población ITT ni los estimandos. El mecanismo de composición queda aceptado por DEC-C10-095: estipulación explícita, versionada y reservada por B1/UE; derivación determinista; sin generación estocástica de Need en el núcleo confirmatorio. La aceptación de ese mecanismo no equivale a aprobación del contrato completo ni a Design Freeze.

## 2. Constructo cuya truth se estipula

Se conserva literalmente la definición funcional de trabajo del contrato de adjudicación B1, §3:

> Antes de Z, B1 tiene el objetivo operativo de mantener disponible en el entorno de destino un servicio capaz de admitir solicitudes conforme al estado declarativo de habilitación de su configuración, exponiendo el perfil operativo declarado.

`Need_preZ` indica si ese objetivo pertenece a los objetivos basales de la B1 concreta antes de Z.

La estipulación no pregunta si el servicio está instalado, habilitado, accesible, operativo o si satisface el objetivo. Tampoco pregunta si existe una solicitud, si se produjo un déficit, si el objetivo es urgente o si es el único objetivo de B1.

La truth se refiere a la existencia/pertenencia del objetivo basal, no a su estado de cumplimiento.

## 3. Objeto generador: especificación basal del objetivo

El generador deberá disponer, en el espacio reservado del DGP, de una estipulación semántica explícita, versionada y configurada por unidad para cada B1/UE del roster que se autorice en el futuro. Esta decisión adopta configuración explícita como fuente de la estipulación; no se infiere desde covariables ni se genera mediante una distribución estocástica de Need.

Esta estipulación es la **especificación basal del objetivo B1**. Su función es determinar la truth del constructo; no es una covariable causal, una fuente observada ni una declaración accesible al adjudicador.

La especificación debe identificar semánticamente:
1. la B1/UE a la que se refiere, mediante los vínculos e identidades que apruebe el contrato de roster;
2. la definición funcional/versionado del objetivo a la que se refiere;
3. su alcance temporal basal, anterior a Z en t−1;
4. si el objetivo focal pertenece, está afirmativamente excluido o no queda determinado entre los objetivos basales de esa B1;
5. la regla y versión del generador que produjo la estipulación, con provenance reservada.

Estos son requisitos semánticos del contrato, no un esquema físico aprobado ni una autorización para crear columnas, tablas, IDs o registros. El nombre y la codificación técnica del objeto quedan abiertos.

## 4. Regla de derivación de truth

La regla de interpretación de la estipulación será:

| Estipulación basal reservada | Truth de Need_preZ | Interpretación |
|---|---|---|
| Inclusión explícita | 1 | El objetivo funcional focal pertenece a los objetivos basales de esa B1 antes de Z |
| Exclusión explícita | 0 | El objetivo funcional focal no pertenece a los objetivos basales de esa B1 dentro del alcance cerrado de la estipulación |
| Indeterminación explícita | ? | La propia estipulación generadora no determina pertenencia ni exclusión |

La regla no convierte una omisión de campo, ausencia de documento o fallo de materialización en exclusión. Un defecto técnico del paquete o la ausencia de un registro no constituye una estipulación válida de truth=0 ni truth=?; debe tratarse como error de integridad/materialización y bloquear el uso de esa unidad hasta resolverlo.

### 4.1 Condiciones de inclusión (truth=1)

La estipulación debe afirmar que el objetivo definido en §2 forma parte de los objetivos basales de B1 en t−1. No se requiere que:
- exista una solicitud natural;
- el servicio esté actualmente indisponible;
- haya un déficit técnico;
- la entidad haya declarado o comunicado el objetivo a un tercero;
- el objetivo sea exclusivo, prioritario o urgente.

### 4.2 Condiciones de exclusión (truth=0)

La estipulación debe afirmar que el objetivo definido en §2 no forma parte de los objetivos basales de esa B1, dentro del universo semántico cerrado que se defina para la unidad y el diseño.

No bastan:
- ausencia de solicitud;
- ausencia de actividad;
- ausencia de declaración observable;
- ausencia de una fuente en el expediente;
- ausencia de instancia de servicio;
- falta de instalación, habilitación o disponibilidad;
- no admisión, no procesamiento o falta de respuesta.

El alcance cerrado que hace interpretable la exclusión debe quedar especificado antes de generar truth. Su delimitación concreta permanece OPEN; no se presume que el silencio de un registro equivalga a una declaración exhaustiva de objetivos.

### 4.3 Indeterminación generadora (truth=?)

Solo procede cuando la estipulación basal del generador contiene una indeterminación semántica explícita o una regla de diseño que deja sin resolver la pertenencia del objetivo. No se utiliza para representar evidencia observacional ausente, cobertura insuficiente del expediente visible, desacuerdo E1/E2 ni error del Analyzer.

## 5. Independencia respecto de covariables y configuración técnica

La especificación basal del objetivo no se derivará automáticamente de:
- `X_i`, `H_{i0}`, `C_{c,i0}`, `L_{m,i0}`;
- `C_{dep,i0}`, `A_{f,i0}^*`, `T_{acc,i0}`, `F_{alt,i0}`;
- componentes `CMP/PAR/REF/RUL`, estados `ENABLED/PROFILE` o identidad de instancia de servicio;
- Z, política D2, provisión, intento/éxito de instalación o variables post-Z;
- solicitudes, recepción, admisión, procesamiento, respuesta, ejecución, Outcome o Value;
- oportunidad estandarizada `N_opportunities=1`.

Esta prohibición impide equivalencias deterministas y circularidad. No afirma que Need no pueda asociarse estadísticamente con características basales. Cualquier dependencia o mecanismo conjunto entre la estipulación y otras características requerirá una justificación de diseño explícita y una revisión de sus implicaciones para identificación, sin alterar la definición del constructo ni convertir un proxy en su verdad.

La especificación es un mecanismo de definición/estipulación del objeto medido, no una nueva covariable explicativa ni un mediador de la cadena causal focal.

## 6. Soporte de diseño sin parametrización prematura

La validación confirmatoria de E1 y E2 como adjudicadores de Need_preZ deberá disponer de unidades con estipulación explícita de inclusión y de exclusión para evaluar su capacidad de distinguir truth=1 de truth=0. Analyzer PE no es clasificador de Need y queda fuera de esta cohorte y de sus denominadores, conforme a DEC-C10-096. La posibilidad de truth=? se conserva para indeterminación real de la estipulación.

Este requisito de soporte no fija:
- prevalencia ni proporción de estados;
- número de unidades;
- asignación por brazo, estrato o combinación;
- correlaciones con covariables;
- distribución, semilla, generador aleatorio ni parámetros;
- tamaño muestral o potencia.

La composición del roster y el soporte binario se rigen por DEC-C10-095: el roster/cohorte se define ex ante por identidad/binding y reglas de población, sin selección por Need, observabilidad o resultados; después se comprueba soporte 1 y 0 sobre la cohorte completa. Si falta una clase, el diseño queda bloqueado, sin reparación post hoc. No se exige balance ni soporte por brazo/estrato. No se crearán unidades para satisfacer el requisito antes de aprobar roster y población.

## 7. Contrato de la declaración observable del objetivo basal

La truth se deriva de la estipulación explícita reservada conforme a DEC-C10-095. La declaración observable es un artefacto distinto, producido por el modelo de observación; no es la estipulación ni una exportación de TRUTH_LEDGER.

### 7.1 Tipo y función

Tipo lógico candidato: S7_B1_BASELINE_OBJECTIVE_ATTESTATION. Pertenece a la clase S7 ya existente y representa un acto declarativo original, controlado y específico sobre la pertenencia del objetivo focal a los objetivos basales declarados de una B1 respecto de su instancia de servicio en t−1. No crea una nueva clase de fuente, entidad U_G, tabla, prueba ni schema físico.

La fuente es directa para esta afirmación declarativa únicamente si el DGP define quién tiene competencia para emitirla y el artefacto conserva autoridad, referente, alcance, temporalidad e integridad. La clasificación S7 no confiere autoridad por sí sola. Manuales, entrevistas, tickets y diagramas genéricos siguen siendo fuentes de contexto/descubrimiento salvo que satisfagan de manera independiente el contrato de declaración original.

### 7.2 Contenido semántico admisible

El contenido observable debe expresar inequívocamente una de estas proposiciones focales:
- **Inclusión declarada:** el objetivo funcional definido en §2 forma parte de los objetivos basales de esta B1 respecto de la instancia de servicio vinculada.
- **Exclusión declarada:** ese objetivo focal no forma parte de los objetivos basales de esta B1 respecto de esa instancia.

La declaración no afirma el estado de cumplimiento del objetivo ni demanda, uso, déficit, solicitud, instalación, accesibilidad o resultado. La exclusión no pretende enumerar todos los objetivos posibles de B1.

Una declaración ambigua, genérica o sin proposición focal no soporta observed=1/0. La ausencia de declaración, la pérdida, la opacidad o la falta de cobertura tampoco equivalen a exclusión.

### 7.3 Condiciones de admisibilidad

Para ser candidata a evidencia directa, la declaración debe cumplir conjuntamente:

1. emisor/rol identificable y versionado;
2. competencia declarativa atribuida explícitamente por el DGP para la B1 pertinente;
3. binding inequívoco a B1, UE, instancia de servicio y versiones;
4. event_time fijado en t−1; capture_time separado si la copia se captura después;
5. alcance B1–servicio y versión de la definición funcional focal;
6. integridad verificable (digest/firma/control equivalente), custodia y lineage;
7. origen original identificable; copias/transcripciones/exports conservan la misma raíz y no cuentan como corroboración independiente;
8. ausencia de truth, truth_basis_ref, claves, semillas o metadatos que revelen/reconstruyan la estipulación reservada.

El hecho de que una persona sea custodio técnico, admin IAM o proveedor del servicio no le atribuye automáticamente autoridad para declarar el objetivo basal de B1. Esa competencia debe formar parte del contrato de roles del DGP.

### 7.4 Separación del proceso de observación

El modelo de observación gobierna si la oportunidad declarativa existe, si se emite, captura/retiene y qué contenido llega al expediente. Puede producir omisión, pérdida, ambigüedad, conflicto, corrupción o error semántico; los mecanismos y dependencias deben justificarse en el DGP maestro, sin tasas inventadas.

La declaración visible no se construye copiando el estado truth. El generador debe preservar dos procesos lógicos:
- estipulación reservada → truth determinista;
- proceso observacional → artefacto declarativo visible, con sus posibles errores y pérdidas.

La truth puede ser causa del contenido de una declaración auténtica dentro del modelo observacional, pero no se transmite su etiqueta ni metadatos internos. El firewall debe comprobar también canales laterales y lineage, no solo ausencia de una columna.

### 7.5 Consecuencia para E1/E2

E1 y E2 reciben el mismo expediente observable permitido, de forma independiente. observed=1 requiere una declaración de inclusión admisible; observed=0 requiere una declaración de exclusión focal admisible y cobertura conforme al alcance. Si falta la declaración o no satisface los requisitos, observed=? o bloqueo técnico según la naturaleza del defecto. No se promueven snapshots S2/S4, contratos S5 genéricos, logs S3/S6/S8 ni entrevistas/documentos secundarios a evidencia directa de Need por mera disponibilidad.

## 8. Separación de truth y observación

La estipulación basal y la truth derivada permanecen reservadas al generador y al evaluador tras el sellado de adjudicaciones. El modelo de observación será un mecanismo separado que producirá fuentes sintéticas visibles con provenance, temporalidad, autoridad, alcance y cobertura.

El modelo de observación podrá depender causalmente de la estipulación reservada para generar información pertinente, pero:
- no copiará la etiqueta truth a los documentos o metadatos visibles;
- no expondrá IDs, claves, semillas o referencias que permitan recuperar directamente truth;
- podrá omitir, degradar, volver ambigua o contradecir información conforme a un contrato de observación aún pendiente;
- mantendrá la distinción entre evidencia negativa afirmativa y ausencia de declaración.

E1 y E2 adjudicarán a partir del expediente observable y las reglas públicas, sin acceso a la estipulación ni a truth. Sus resultados se sellarán antes de abrir truth para evaluación.

Este contrato no especifica todavía los mecanismos, tipos de fuente, tasas de error, dependencias, cobertura ni parámetros del modelo de observación.

## 8. Ubicación temporal y relación con la población/estimandos

La estipulación pertenece a t−1, antes de Z en t0. Z y las variables posteriores no pueden modificarla retrospectivamente.

`Need_preZ` no sustituye `E_i`, `P^*_{τ2}`, `App^*(τ2,S0)`, `C_{dep,0}` ni `A_{f,0}^*`; tampoco es filtro automático de inclusión ITT. Cualquier uso para estratificación, heterogeneidad, población de Value o análisis de consecuencias requiere justificación y especificación ex ante en el contrato pertinente. No se autoriza condicionar el ITT a Need=1 ni a solicitudes/eventos post-Z.

## 9. Invariantes verificables antes de materialización

Antes de crear roster o truth, el diseño deberá poder verificar documentalmente que:

1. cada estipulación se refiere a una B1/UE inequívoca y al objetivo funcional versionado;
2. la referencia temporal es t−1, anterior a Z;
3. inclusión, exclusión e indeterminación son estados explícitos y no inferidos de ausencia;
4. truth=0 se apoya en una exclusión afirmativa dentro de un alcance cerrado;
5. truth=? no encubre fallos de integridad o ausencia de evidencia;
6. no se deriva truth de covariables causales, configuración técnica, Z o variables post-Z;
7. el mecanismo y los metadatos de truth no son accesibles a E1/E2;
8. la evidencia observable se genera por un proceso separado y no filtra la etiqueta;
9. el soporte de truth=1 y truth=0 está previsto en el diseño sin fijar prevalencias;
10. la apertura de truth ocurre solo después del sellado de las adjudicaciones.

Son condiciones de diseño propuestas; no se han ejecutado pruebas ni validadores.

## 10. Cuestiones todavía abiertas

| Cuestión | Estado |
|---|---|
| Definición funcional del objetivo focal | Definida en contrato de adjudicación B1 |
| Principio y mecanismo de especificación basal explícita por B1/UE | ACCEPTED BY USER AND DEC-C10-095 |
| Alcance semántico cerrado para afirmar exclusión | OPEN |
| Codificación/representación técnica de la estipulación | OPEN |
| Mecanismo de estipulación y derivación de truth | ACCEPTED BY DEC-C10-095: configuración explícita versionada + mapping determinista; sin generador estocástico de Need |
| Relación con covariables si se contempla dependencia estadística | OPEN; no autorizada por este contrato |
| Modelo de observación y fuentes | OPEN |
| Cobertura, mecanismos de error y parámetros de observación | OPEN |
| Permisos técnicos y segregación efectiva | OPEN |
| Crosswalk final con el maestro DGP y contratos de población/estimandos | OPEN |

## 11. Dictamen y siguiente gate

**DEC-C10-095 ACCEPTED WORKING DESIGN / EXPLICIT PER-UNIT STIPULATION + DETERMINISTIC TRUTH MAPPING / EXCLUSION SCOPE AND REPRESENTATION GATES TRACKED SEPARATELY / NO MATERIALIZATION OR EXECUTION AUTHORIZED.**

El siguiente gate no es generar unidades ni fuentes. Es cerrar el alcance semántico que permite una exclusión afirmativa (truth=0) y reconciliar la representación de la estipulación con el maestro DGP y el contrato del paquete analítico. El mecanismo de estipulación ya queda resuelto por DEC-C10-095. Permanecen como gates separados la representación técnica, la población/roster y el modelo de observación.

Este documento no modifica main, RMA, Evidence→Claim Matrix, STATUS, decisiones aceptadas, población, estimandos ni el DGP ejecutable. No crea roster, IDs, truth, fuentes, cobertura, fixtures o código. No ejecuta validadores, DGP, simulación ni replay.

`scientific_execution=false`; `execution_authorized=false`.



## 7.6 Autoridad declarativa sintética, asignación de competencia y no equivalencia Generator=emisor

Esta sección desarrolla el requisito de competencia de §7.3. Es una propuesta documental, no una decisión aceptada ni un Design Freeze.

### A. Separación de funciones

Se distinguen cuatro funciones lógicas, aunque una implementación futura pueda alojarlas en el mismo proceso técnico:

1. **Generator / truth custodian:** estipula y conserva la truth reservada conforme a DEC-C10-095. No actúa automáticamente como emisor visible ni puede exportar la estipulación como declaración.
2. **Role/authority specification:** define ex ante qué clase de actor sintético tiene competencia declarativa sobre el objetivo basal de B1, el alcance de esa competencia, su vigencia y las unidades a las que puede aplicarse.
3. **Issuer/source process:** representa el acto declarativo observable emitido bajo esa competencia. Su identidad, rol, mandato y versión son visibles al adjudicador; su contenido procede del proceso observacional, no de una copia de la etiqueta truth.
4. **E1/E2:** valoran la evidencia visible y adjudican independientemente. No consultan truth, metadatos reservados ni el proceso interno del Generator.

La separación es semántica y de acceso; no presupone microservicios, actores reales, firma criptográfica ni despliegue físico.

### B. Regla de atribución de competencia

La competencia no se deduce de que el actor sea propietario técnico, administrador IAM, custodio de infraestructura, proveedor, operador o Generator. Debe existir una regla pública/versionada del DGP que atribuya expresamente al rol emisor la facultad de declarar el objetivo basal de B1 en el ámbito B1–instancia de servicio.

La regla debe resolver antes de observar contenido:
- fundamento del mandato declarativo dentro del microdominio sintético;
- clase/identidad de rol competente y versión;
- alcance funcional y unidades cubiertas;
- inicio/fin de vigencia, sustitución y revocación;
- delegación, concurrencia o conflicto de competencias;
- cómo se verifica la competencia sin revelar truth.

No se selecciona aquí una clase concreta de actor ni se inventa un cargo. El nombre canónico del rol, su cardinalidad y el mecanismo de asignación quedan OPEN hasta reconciliar el catálogo de actores/roles del DGP y el contrato B1. La autoridad debe ser una propiedad del mandato preespecificado, no un atributo derivado del contenido que el actor emite.

### C. Asignación de la competencia

La asignación del mandato se determina ex ante mediante identidad, ámbito y regla de rol versionados. No puede asignarse o retirarse en función de:
- need_truth_state o truth_basis_ref;
- contenido emitido, capturado, perdido o adjudicado;
- Z, D2, instalación, accesibilidad, Reach, trayectoria, Outcome o Value;
- éxito esperado de E1/E2 o rendimiento del Analyzer.

La asignación puede ser común a todas las UE o variar por unidades/ámbitos si el contrato de actores lo justifica; no se presupone ninguna de las dos configuraciones. La variación, si existe, debe estar fijada antes de generar evidencia y su soporte debe ser auditable. No se exige un emisor distinto por UE ni se presupone independencia entre emisores.

### D. Autoridad no implica veracidad

Una declaración puede ser auténtica, emitida por un rol competente y correctamente vinculada, pero contener una afirmación semánticamente errónea, ambigua, incompleta o contradictoria. Por tanto:
- autenticidad/autoridad y corrección semántica son dimensiones distintas;
- la competencia no garantiza que el contenido coincida con truth;
- la firma/digest prueba integridad/origen según el mecanismo, no verdad semántica;
- las declaraciones de inclusión/exclusión se evalúan por contenido y admisibilidad, no por presunción de infalibilidad del emisor.

Este requisito es esencial para que la evaluación de E1/E2 no se reduzca a copiar una etiqueta infalible.

### E. Firewall contra la reproducción trivial de truth

El Generator conoce la truth por definición, pero el proceso que genera el artefacto observable no debe implementar una asignación directa del tipo need_truth_state → mismo valor en declaration.content. Debe existir un proceso observacional intermedio explícito que determine qué información llega al emisor/proceso de fuente y qué proposición acaba declarada.

Ese proceso podrá modelarse como canal de información, estado informativo/creencia del emisor o mecanismo equivalente, siempre que:
- sea distinto del registro reservado de truth;
- sus reglas y dependencias estén declaradas en el DGP;
- pueda producir omisión, ambigüedad, conflicto o error semántico cuando el escenario lo contemple;
- no introduzca tasas, probabilidades ni correlaciones sin parametrización justificada;
- no revele la etiqueta truth ni metadatos reconstructivos al expediente;
- preserve la posibilidad de una declaración auténtica pero errónea.

No se exige que la declaración sea independiente de truth: eso destruiría la función de una fuente que pretende informar sobre el objetivo. Se exige que la relación truth→información disponible→declaración sea explícita, mediada y evaluable, y que no sea una copia perfecta por construcción. Tampoco se presume que todo escenario deba contener errores; el catálogo de escenarios de observación y sus parámetros sigue OPEN.

### F. Pruebas de contrato requeridas (no ejecutadas)

Antes de implementación deberán poder verificarse, al menos:
- el emisor observable tiene competencia atribuida por una regla versionada;
- modificar truth sin cambiar la regla de rol no cambia automáticamente quién posee competencia;
- modificar Z/post-Z no cambia el mandato basal ni el contenido pre-Z ya fijado;
- el Generator no exporta truth, basis_ref, seed, flags o codificación lateral al expediente;
- un emisor competente puede producir contenido semánticamente erróneo sin perder por ello la autenticidad de origen;
- una fuente sin competencia no se convierte en directa por contenido coincidente con truth;
- copias y derivados conservan lineage y no simulan corroboración independiente;
- E1/E2 no acceden al registro truth ni al estado informativo interno del proceso de fuente.

Estas son obligaciones de diseño y futuras pruebas de contrato; no se crean IDs de prueba ni se declaran ejecutadas.

**Dictamen:** autoridad declarativa y proceso de emisión definidos a nivel de requisitos; rol concreto, regla de asignación, mecanismo de información del emisor y parametrización observacional permanecen OPEN. No se aprueba todavía la declaración S7 como implementable ni se autoriza materialización.



## 7.7 Reconciliación de señal del emisor: no introducir un agente cognitivo sin base DGP

Esta sección reconcilia §§7.4–7.6 con DEC-C10-095 y DEC-C10-097 y con el contrato operativo de observación/cobertura. Es una aclaración de diseño; no constituye aceptación de un nuevo mecanismo ni Design Freeze.

### 7.7.1 Resultado de la reconstrucción

No se ha identificado en los contratos basales una variable, registro o evento pre-Z que sea una señal independiente autorizada sobre la pertenencia del objetivo focal a B1. El diagnóstico de fuentes descarta expresamente como generadores o proxies automáticos X/H/C/L, ENABLED/PROFILE, IAM, snapshots técnicos, instalación, accesibilidad, solicitudes, logs y operación. Reutilizarlos como «información que conoce el emisor» no los convierte en evidencia semántica de Need.

Tampoco existe una especificación aprobada de un actor sintético con estado cognitivo, creencias o acceso a una fuente documental realista. No se inventa tal actor ni una señal adicional.

### 7.7.2 Solución mínima compatible con los contratos aceptados

La solución mínima es tratar la emisión de S7 como un **proceso de medición/declaración sintético del modelo de observación**, no como la acción de un agente cognitivo al que se entrega una señal basal independiente.

- La estipulación explícita reservada por B1/UE sigue siendo la única fuente de need_truth_state, derivado determinísticamente conforme a DEC-C10-095.
- El proceso de observación genera por separado la oportunidad, emisión, contenido semántico, captura/retención, autoridad, integridad, temporalidad y vinculación del artefacto.
- La identidad/rol/mandato del emisor, si el contrato de fuentes lo exige, es metadata de provenance y autoridad preespecificada ex ante; no prueba por sí misma la verdad ni exige simular una mente o un conocimiento privado.
- El contenido visible se produce mediante el canal de observación condicionado por el estado basal relevante y por los mecanismos aprobados. El canal puede producir declaración correcta, afirmación errónea, ambigüedad, conflicto, omisión o pérdida conforme al escenario; no se asignan probabilidades ni parámetros aquí.
- El proceso interno del canal puede conservar estado técnico para reproducibilidad, pero ese estado no se interpreta como conocimiento de un actor ni se exporta al expediente.

Esta solución es compatible con la regla ya aceptada de que la truth puede influir en la probabilidad y contenido de una declaración auténtica, siempre que no se copie mecánicamente la etiqueta ni se filtren claves o metadata reconstructiva. La mediación requerida es el mecanismo explícito de observación, no necesariamente un agente intermediario.

### 7.7.3 Qué significa «declaración auténtica pero errónea»

Autenticidad significa que el artefacto procede del proceso/rol sintético atribuido, dentro de su mandato y con lineage e integridad verificables. No significa que su proposición sea semánticamente correcta respecto de need_truth_state.

Por ello el DGP debe separar:
1. atribución ex ante de autoridad y alcance;
2. generación del contenido observable por el canal;
3. admisibilidad/integridad de lo capturado;
4. adjudicación E1/E2;
5. comparación con truth tras el sellado.

Una declaración positiva falsa o una exclusión focal falsa puede ser auténtica en origen y admisible, y contar como error de clasificación. Un artefacto fabricado por una fuente no autorizada no se vuelve admisible porque coincida con truth.

### 7.7.4 Alternativa aplazada

Solo si una futura especificación del microdominio identifica un proceso basal concreto que produce información declarativa (con semántica, autoridad, tiempo y provenance propios) podrá modelarse un emisor como actor con acceso a esa señal. Ese diseño deberá demostrar que la señal no es ENABLED/PROFILE, una proxy técnica, una copia de truth ni una variable post-Z. No es requisito del diseño mínimo actual.

**Dictamen:** no se requiere una señal basal independiente ni un emisor cognitivo para representar una observación imperfecta. Se recomienda conservar S7 como artefacto declarativo generado por el canal observacional, con autoridad/provenance asignada ex ante y contenido imperfecto modelado explícitamente. El catálogo de fuentes y el canal siguen pendientes de especificación y parámetros; no se autoriza materialización.



## 7.8 Mandato de autodeclaración S7 y canal sintético — DEC-C10-098

DEC-C10-098 acepta una oportunidad lógica S7 por UE y atribuye la declaración focal a B1 en modalidad de autodeclaración limitada a su propio objetivo operativo basal. Esta aceptación resuelve la hipótesis de mandato de §10.9.3 del inventario: no queda abierta la pregunta de si B1 puede declarar su propio objetivo dentro de ese alcance; sí quedan abiertos la identidad/representación concreta, versión y evidencia técnica del mandato.

La expresión «canal de observación» de §7.7 no debe interpretarse como un agente oculto ni como una señal privada que conoce truth. Es un mecanismo sintético de medición que genera el resultado observable a partir del estado basal mediante reglas explícitas, mediadas y auditables. Debe distinguir, al menos, oportunidad esperada, resultado de emisión/contenido, captura/retención y admisibilidad. No se fija aquí ninguna probabilidad ni se presupone independencia.

La enumeración de una oportunidad por UE se realiza ex ante y es independiente de truth, tratamiento y resultados. El contenido observable puede estar relacionado con el estado basal; de otro modo no mediría Need. Esa relación no puede ser una copia determinista de need_truth_state al campo declarativo ni una filtración por IDs, timestamps, orden, semillas, lineage o metadatos. El DGP deberá especificar el mecanismo de forma que permita errores semánticos, ambigüedad y no emisión en los escenarios que se definan y justifiquen.

La declaración auténtica pero errónea sigue siendo admisible como evidencia de lo que se declaró, no como verdad del objetivo. E1/E2 la clasifican según su contenido y criterios de admisibilidad; la evaluación posterior contra truth identifica el error. Autoridad no equivale a veracidad.

Esta sección especializa y armoniza §§7.4–7.7 y los requisitos A–F precedentes. Donde los textos anteriores parezcan exigir que un actor reciba una señal basal, prevalece esta interpretación de canal de medición sin actor cognitivo, salvo futura decisión explícita que incorpore una fuente/actor realista con base microdominio independiente.

**OPEN:** estructura matemática/causal del canal, estados conjuntos, parámetros, dependencias, escenarios, soporte, sensibilidad y verificación técnica del firewall. No se autoriza materialización, implementación ni ejecución.


### 7.6 Regla operativa de adjudicación para E1/E2

Esta regla operacionaliza §§7.2–7.5 y la definición de observed_evidence(Need_preZ) de C10_S_B1_PREZ_ADJUDICATION_AND_CONSEQUENCE_RECONCILIATION_DRAFT_001.md §4.2–4.3. No crea un nuevo rol, artefacto lógico, test ID ni schema físico.

E1 y E2 reciben por separado el mismo bundle observable autorizado y aplican, sin acceso a truth ni al resultado del otro, la siguiente secuencia:

1. **Integridad y binding:** comprobar que el expediente y sus referencias permiten resolver B1–UE–instancia de servicio, versiones, event_time pre-Z, lineage e integridad. Un defecto de identidad/binding/schema/digest/truth-integrity que impida evaluar bloquea la unidad/paquete conforme a DEC-C10-097; no se convierte en observed=? ni se elimina del censo.
2. **Admisibilidad de la declaración:** comprobar mandato/competencia declarativa, alcance focal, temporalidad, provenance y correspondencia con la definición funcional versionada. Una fuente no admisible sin defecto técnico bloqueante no sustenta polaridad y conduce a observed=?
3. **Inclusión focal inequívoca:** si una declaración S7 admisible afirma que el objetivo focal pertenece a los objetivos basales de esa B1 respecto del servicio vinculado, adjudicar observed=1.
4. **Exclusión focal inequívoca:** si una declaración S7 admisible afirma que el objetivo focal no pertenece a esos objetivos, adjudicar observed=0 solo cuando la cobertura del alcance B1–servicio sea suficiente y esté demostrada. No se exige enumerar todos los objetivos posibles de B1; la exclusión focal explícita es la afirmación negativa mínima aceptada por DEC-C10-095/097.
5. **Indeterminación observacional:** asignar observed=? cuando no hay declaración por no emisión/pérdida, el contenido es ambiguo o contradictorio, el alcance/versionado no se puede resolver sin constituir un bloqueo técnico, la fuente carece de autoridad admisible, o la cobertura requerida para sostener una exclusión es incompleta/opaca.
6. **Sellado y evaluación:** conservar las salidas individuales y su justificación/evidencia; sellar ambas antes de cualquier comparación con need_truth_state. El desacuerdo E1/E2 no se resuelve por consenso implícito ni se borra; se reporta separadamente de la exactitud de cada adjudicador frente a truth.

La prioridad es **bloqueo técnico de integridad/binding** cuando impide identificar o validar la unidad; en los demás casos de insuficiencia de contenido o evidencia se conserva observed=?. Una declaración afirmativa de inclusión no requiere inferir déficit, solicitud, uso o incumplimiento del servicio. Una exclusión afirmativa no puede derivarse de silencio, búsqueda fallida ni ausencia de actividad.

**Límite de inferencia:** esta regla hace operativa la interpretación normativa de inclusión/exclusión y la abstención. No demuestra que E1/E2 la ejecuten correctamente. La concordancia interevaluador, la exactitud de cada uno frente a truth y la atribución de errores al canal o al adjudicador son evaluaciones distintas. Para aislar empíricamente la interpretación del contenido de la discordancia truth–contenido se necesitaría una comprobación controlada separada, que permanece OPEN y no se crea aquí.
