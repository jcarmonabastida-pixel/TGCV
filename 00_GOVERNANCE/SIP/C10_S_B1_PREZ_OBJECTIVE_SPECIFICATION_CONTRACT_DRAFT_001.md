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

El diseño confirmatorio del Analyzer deberá disponer de unidades con estipulación explícita de inclusión y de exclusión para evaluar su capacidad de distinguir truth=1 de truth=0. La posibilidad de truth=? se conserva para indeterminación real de la estipulación.

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
