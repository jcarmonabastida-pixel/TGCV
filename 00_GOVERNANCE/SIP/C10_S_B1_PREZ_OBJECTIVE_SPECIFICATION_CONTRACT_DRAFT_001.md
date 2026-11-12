# C10-S — Contrato de estipulación basal del objetivo B1 para Need_preZ

**ID:** C10-S-B1-PREZ-OBJECTIVE-SPECIFICATION-CONTRACT-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** USER_ACCEPTED_DESIGN_PRINCIPLE / CONTRACT_DRAFT / NOT_DESIGN_FROZEN / NOT_IMPLEMENTED / NOT_MATERIALIZED / NOT_EXECUTED  
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

No sustituye ni reabre la definición funcional aceptada de Need_preZ, la cardinalidad B1–UE, la identidad de instancia de servicio, DEC-C10-061, la composición de población ITT ni los estimandos. La aceptación del principio no equivale a aprobación de este contrato completo ni a diseño congelado.

## 2. Constructo cuya truth se estipula

Se conserva literalmente la definición funcional de trabajo del contrato de adjudicación B1, §3:

> Antes de Z, B1 tiene el objetivo operativo de mantener disponible en el entorno de destino un servicio capaz de admitir solicitudes conforme al estado declarativo de habilitación de su configuración, exponiendo el perfil operativo declarado.

`Need_preZ` indica si ese objetivo pertenece a los objetivos basales de la B1 concreta antes de Z.

La estipulación no pregunta si el servicio está instalado, habilitado, accesible, operativo o si satisface el objetivo. Tampoco pregunta si existe una solicitud, si se produjo un déficit, si el objetivo es urgente o si es el único objetivo de B1.

La truth se refiere a la existencia/pertenencia del objetivo basal, no a su estado de cumplimiento.

## 3. Objeto generador: especificación basal del objetivo

El generador deberá disponer, en el espacio reservado del DGP, de una estipulación semántica explícita y versionada para cada unidad B1/UE del roster que se autorice en el futuro.

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

La composición del roster y el soporte por subgrupo deberán resolverse en el contrato de diseño/población correspondiente. No se crearán unidades para satisfacer este requisito antes de su aprobación.

## 7. Separación de truth y observación

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
| Principio de especificación basal explícita por B1 | Aceptado por el usuario; pendiente de incorporación formal al conjunto de decisiones |
| Alcance semántico cerrado para afirmar exclusión | OPEN |
| Codificación/representación técnica de la estipulación | OPEN |
| Regla concreta de composición de estados 1/0/? en el roster | OPEN; sin parámetros |
| Relación con covariables si se contempla dependencia estadística | OPEN; no autorizada por este contrato |
| Modelo de observación y fuentes | OPEN |
| Cobertura, mecanismos de error y parámetros de observación | OPEN |
| Permisos técnicos y segregación efectiva | OPEN |
| Crosswalk final con el maestro DGP y contratos de población/estimandos | OPEN |

## 11. Dictamen y siguiente gate

**DESIGN PRINCIPLE ACCEPTED BY USER / OBJECTIVE-STIPULATION CONTRACT PROPOSED / EXCLUSION SCOPE AND REPRESENTATION OPEN / NO MATERIALIZATION OR EXECUTION AUTHORIZED.**

El siguiente gate no es generar unidades ni fuentes. Es cerrar el alcance semántico que permite una exclusión afirmativa (truth=0) y reconciliar la representación de la estipulación con el maestro DGP y el contrato del paquete analítico. Solo después podrá especificarse el mecanismo de asignación de estados y, en una etapa posterior, el modelo de observación.

Este documento no modifica main, RMA, Evidence→Claim Matrix, STATUS, decisiones aceptadas, población, estimandos ni el DGP ejecutable. No crea roster, IDs, truth, fuentes, cobertura, fixtures o código. No ejecuta validadores, DGP, simulación ni replay.

`scientific_execution=false`; `execution_authorized=false`.
