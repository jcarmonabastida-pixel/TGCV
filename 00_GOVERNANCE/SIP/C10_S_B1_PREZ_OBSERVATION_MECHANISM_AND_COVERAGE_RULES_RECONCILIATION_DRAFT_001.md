# C10-S — Reconciliación operativa del modelo de observación y cobertura B1/Need_preZ

**ID:** C10-S-B1-PREZ-OBSERVATION-COVERAGE-RECON-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-12  
**Estado:** DOCUMENTARY_RECONCILIATION / OPERATIONAL_RULES_ACCEPTED_BY_DEC-C10-097 / ALIGNED_WITH_DEC-C10-095_AND_DEC-C10-096 / NOT_IMPLEMENTED / NOT_MATERIALIZED / NOT_EXECUTED  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)

## 1. Objeto y resultado de la revisión

Operacionalizar sin duplicar el modelo de observación ya definido en `C10_S_B1_PREZ_ANALYTICAL_PACKAGE_CONTRACT_DRAFT_001.md` §6–§10, el inventario de fuentes y el crosswalk PE.

El roster/cohorte queda delimitado por DEC-C10-096: censo de todas las UE del roster DGP/paquete aprobado al que aplica B1/Need. E1 y E2 son los adjudicadores Need; Analyzer PE queda fuera de la clasificación Need.

La revisión identifica el cierre que falta: separar de forma explícita (a) el marco de oportunidades de fuente declarado por el DGP, (b) el proceso de emisión/captura, (c) el contenido semántico de cada fuente, (d) su admisibilidad e integridad y (e) la decisión E1/E2. No se fija número de fuentes, distribución, tasa, prevalencia ni parámetro.

Las reglas operativas de este documento han sido aceptadas como diseño de trabajo por DEC-C10-097. Este documento especializa, pero no reemplaza ni modifica silenciosamente, el contrato del paquete.

## 2. Marco de fuentes: alcance antes de observación

Para cada UE y cada dimensión de afirmación pertinente al objetivo B1, el DGP deberá declarar ex ante el alcance documental/sintético que pretende representar. El alcance se identifica por unidad, dimensión, versión y regla de enumeración. No se presume que exista un catálogo universal de fuentes reales ni que todas las clases candidatas del inventario estén presentes en cada UE.

El marco de fuentes distingue:
- **fuentes esperadas dentro del alcance:** oportunidades de registro que el escenario declara pertinentes y enumerables;
- **fuentes examinadas:** registros efectivamente inspeccionados por el proceso de adjudicación;
- **fuentes disponibles y válidas:** registros capturados, íntegros, identificables, temporales y semánticamente admisibles;
- **fuentes excluidas:** registros localizados pero inadmisibles, con motivo;
- **fuentes opacas/no enumerables:** superficies que el alcance no permite inspeccionar o cerrar;
- **fuentes no emitidas o perdidas:** eventos del proceso de observación, distintos de una declaración negativa.

No se define un denominador de cobertura a partir de registros encontrados. El universo esperado procede del alcance ex ante; si no puede enumerarse, la cobertura no puede declararse COMPLETE.

## 3. Separación de mecanismos generativos

El modelo de observación debe conservar mecanismos lógicamente distintos. No se presume que sean independientes:

1. **Emisión:** si una oportunidad de fuente produce una declaración.
2. **Captura/retención:** si una fuente emitida llega al expediente accesible.
3. **Contenido semántico:** si la declaración es fiel, errónea, ambigua o contradictoria respecto del objetivo focal.
4. **Autoridad/vigencia:** si emisor, rol, alcance y versión permiten que la fuente respalde la afirmación.
5. **Integridad:** si el artefacto conserva identidad, contenido y digest verificables.
6. **Temporalidad:** si el event_time es pre-Z; capture_time posterior solo se admite cuando se acredita una copia íntegra de un registro fijado pre-Z.
7. **Vinculación:** si la fuente corresponde a la B1/UE/instancia/versionado correctos.
8. **Enumeración/cobertura:** si el universo pertinente fue cerrado y examinado conforme a la regla de alcance.

La truth puede influir en la probabilidad y contenido de una declaración auténtica. La observabilidad puede depender de propiedades basales de la fuente/canal/custodio si se especifican ex ante. Ningún mecanismo puede depender de Z, política D2, tratamiento recibido, accesibilidad post-Z, Reach, trayectoria, ejecución, Outcome, Value o adjudicaciones.

No se asignan probabilidades ni dependencias numéricas en este documento. La generación explícita de Need truth se mantiene separada y determinista conforme a DEC-C10-095.

## 4. Estados de fuente y transición al expediente observable

Los siguientes estados describen el proceso de observación, no el valor de Need:

| Estado de proceso | Interpretación | Consecuencia inicial |
|---|---|---|
| NOT_IN_SCOPE | La clase de fuente no pertenece al alcance declarado de esa unidad/dimensión | No se cuenta como fuente esperada; no demuestra ausencia del objetivo |
| NOT_ISSUED | Existía oportunidad de emisión, pero no se emitió declaración | Ausencia; no es afirmación negativa |
| ISSUED_NOT_CAPTURED / LOST | Fuente emitida pero no retenida/capturada | Pérdida; no es afirmación negativa |
| CAPTURED_OPAQUE | Registro localizado pero contenido/universo no inspeccionable | Cobertura parcial/opaca |
| CAPTURED_INVALID | Integridad, identidad, versión o temporalidad no verificables | Excluida de evidencia admisible; motivo preservado |
| CAPTURED_AMBIGUOUS | Contenido genuino pero semánticamente insuficiente para inclusión/exclusión focal | Puede contribuir a observed=? |
| CAPTURED_CONFLICTING | Afirmaciones incompatibles sin regla de autoridad/precedencia que las resuelva | observed=? hasta resolución válida |
| CAPTURED_VALID_POSITIVE | Afirmación afirmativa del objetivo focal, admisible y vinculada | Candidata a observed=1 |
| CAPTURED_VALID_NEGATIVE | Exclusión focal afirmativa, admisible y dentro del alcance cerrado B1–servicio | Candidata a observed=0 |

Estos estados no deben colapsarse en un único campo de disponibilidad. El contrato físico futuro deberá conservar estado de emisión/captura, integridad, admisibilidad y contenido por separado dentro de los artefactos existentes; no se añade un séptimo artefacto lógico.

## 5. Reglas de adjudicación E1/E2

Cada adjudicador recibe el mismo expediente observable autorizado y el alcance de fuentes no sensible, nunca truth ni metadatos reconstructivos.

- **Observed=1:** al menos una afirmación positiva semánticamente alineada, pre-Z, íntegra, autorizada, vigente y vinculada a B1/UE/servicio; no basta ENABLED/PROFILE, IAM, snapshot técnico ni contrato genérico sin adopción por B1.
- **Observed=0:** afirmación explícita de exclusión focal, íntegra, autorizada, vigente y vinculada, dentro del alcance B1–servicio cerrado. No se requiere enumerar todos los objetivos de B1; se aplica la exclusión focal aceptada. La mera ausencia de declaración, búsqueda sin resultados o cobertura COMPLETE sin afirmación negativa no basta.
- **Observed=?:** no existe evidencia afirmativa suficiente para 1 o 0; hay omisión/pérdida, ambigüedad, conflicto no resuelto, opacidad, cobertura insuficiente o fuentes no admisibles.
- **Error técnico/bloqueo:** fallo de identidad, binding, digest, schema o integridad que impide procesar el caso; no se disfraza como observed=? ni se convierte en resultado de clasificación.

E1 y E2 conservan salidas independientes, rationales, evidencia usada, motivos de unknown/abstention, sellos y errores. La concordancia no sustituye exactitud contra truth.

## 6. Falsos positivos, falsos negativos y abstención

Distinguir el error semántico del silencio:

- Truth=1 + ausencia, ambigüedad o pérdida de declaración positiva → normalmente observed=? (abstención), no falso negativo binario.
- Truth=1 + afirmación negativa explícita, admisible pero semánticamente errónea → observed=0; se cuenta como falso negativo.
- Truth=0 + ausencia de declaración positiva → observed=?; no es verdadero negativo.
- Truth=0 + afirmación positiva explícita, admisible pero semánticamente errónea → observed=1; se cuenta como falso positivo.
- Truth=? → se conserva fuera de la matriz binaria; la conducta E1/E2 se informa separadamente.
- Registro corrupto, identidad incorrecta o fuente post-Z no acreditada como copia pre-Z → inadmisible/bloqueo según la clase de fallo, no evidencia afirmativa para clasificar.

La distinción es esencial: la cobertura y la tasa de abstención son resultados del procedimiento, no se eliminan del denominador para mejorar sensibilidad/especificidad. Los denominadores de cada métrica deben mostrarse por E1 y E2.

## 7. Cobertura y denominadores

El censo de UE aprobado por DEC-C10-096 fija el denominador de unidades. Dentro de cada unidad, el marco de fuentes/dimensiones declarado ex ante fija el universo pertinente para cobertura. Se informan por separado:

- N roster;
- N con identidad/binding/truth-integrity válidos;
- N truth=1, N truth=0 y N truth=?;
- por unidad×dimensión: N fuentes esperadas, examinadas, válidas, excluidas, opacas, no emitidas y perdidas, cuando esos conteos tengan significado en el alcance declarado;
- estados NONE/PARTIAL/COMPLETE por unidad×dimensión;
- por E1 y E2: salida 1, 0, ?, abstención, error técnico y ausencia de salida;
- matriz de clasificación sobre truth=1/0 y denominadores por clase;
- bloqueos/no evaluables con causa.

No se promedia cobertura entre dimensiones para producir un porcentaje global que oculte huecos. No se declara COMPLETE porque se hayan inspeccionado todas las fuentes encontradas: se requiere que el universo declarado sea enumerado/cerrado y que todas las superficies pertinentes se hayan examinado conforme a la regla. COMPLETE no implica observed=0; para observed=0 sigue siendo necesaria la afirmación negativa focal.

## 8. Dependencia entre fuentes y errores

No se presupone independencia condicional de fuentes. Si varias declaraciones comparten emisor, custodio, plantilla, canal, sistema, regla de generación o proceso de captura, la dependencia debe estar representada o reconocida como limitación. Repetir una misma declaración por varios artefactos derivados no crea corroboración independiente.

Los errores se separan:
- error semántico de la afirmación;
- pérdida/no emisión;
- error de identidad/vinculación;
- error temporal;
- corrupción/integridad;
- error de autoridad/vigencia;
- ambigüedad/conflicto.

No se asignan tasas ni probabilidades hasta que el DGP maestro defina la estructura causal de observación, sus dependencias, soporte, parámetros justificados y análisis de sensibilidad. Si el DGP no identifica un mecanismo, se mantiene OPEN; no se inventa MCAR/MAR/MNAR ni independencia.

## 9. Crosswalk con contratos existentes (sin IDs nuevos)

| Regla/escenario | Contratos existentes reutilizables |
|---|---|
| Separación de truth y evidencia; export sin truth | PKG-05, PKG-07, PKG-13, PKG-14; P182-11 |
| Silencio/omisión no es observed=0 | PKG-08; MEAS-11 como control de no recodificar ? a 0 |
| Exclusión focal afirmativa y cobertura negativa | PKG-09; protocolo U_G de evidencia/provenance/cobertura |
| Estado técnico no prueba objetivo Need | PKG-10 |
| Conflicto, ambigüedad, identidad/temporalidad/versiones | PKG-11; MEAS-12 cuando aplique contaminación temporal |
| Independencia E1/E2 y desacuerdo preservado | PKG-12; P182-06 |
| Evaluación solo tras sellado | PKG-13 |
| Integridad, lineage, cardinalidades, versiones y digests | PKG-14 |
| Pérdida/captura diferencial y selección | MEAS-13, MISS-10/13/15, sin trasladar mecánicamente sus parámetros a Need |
| Cobertura por dimensión y limitación de generalización | P182-03/05/08 y P183 según el estimando de medición |

Este crosswalk es una propuesta de reutilización; no afirma que esos contratos estén implementados o ejecutados. No se crean IDs PREZ nuevos. Si una regla no queda cubierta por el contrato existente, se registra el gap antes de ampliar el registro.

## 10. Gates pendientes

1. Aceptación de estas reglas operativas de fuente/observación/cobertura.
2. Crosswalk detallado de cada regla con PKG-01…14 y pruebas existentes, comprobando si algún criterio necesita especialización versionada sin duplicar IDs.
3. Determinar el catálogo mínimo de clases de fuente que necesita el microdominio; las clases candidatas del inventario no se convierten automáticamente en fuentes presentes.
4. Especificar el grafo de dependencias del proceso de observación y el soporte de sus mecanismos en el DGP maestro.
5. Definir el universo de fuentes por unidad×dimensión y sus reglas de enumeración/cierre.
6. Justificar tamaños, precisión, potencia y cualquier parámetro de error antes de ejecución.
7. Verificar técnicamente el firewall y canales laterales.
8. Aprobar por separado implementación y ejecución.

## 11. Dictamen

La especificación existente ya contiene los mecanismos generales. Esta reconciliación propone reglas operativas para no confundir ausencia con exclusión, fuente técnica con afirmación semántica, error con abstención ni cobertura de hallazgos con cierre del universo.

El modelo operativo general de observación/cobertura queda aceptado como diseño de trabajo por DEC-C10-097. No se aprueban todavía fuentes concretas, probabilidades, tasas, parámetros, roster, schema físico, fixtures o código. No se materializa ningún dato ni se ejecuta ninguna prueba, DGP, simulación o replay.

`scientific_execution=false`; `execution_authorized=false`.



## 12. Reconciliación de señal y función emisora S7 (2026-11-12)

La clase semántica mínima del inventario B1/Need es S7: declaración focal de inclusión/exclusión. No se introduce una señal basal independiente ni un actor cognitivo porque los contratos revisados no identifican tal señal ni un modelo aprobado de conocimiento del emisor.

La función emisora se representa como atribución ex ante de autoridad/provenance asociada al artefacto S7. El artefacto es generado por el canal de observación, que mantiene separados:
- estipulación reservada y truth determinista;
- oportunidad y emisión;
- contenido semántico (correcto, erróneo, ambiguo o conflictivo);
- captura/retención/pérdida;
- autoridad/vigencia, integridad, temporalidad y binding;
- adjudicación E1/E2 y evaluación posterior.

La truth puede influir en la probabilidad y el contenido de la declaración a través de ese canal, conforme a DEC-C10-097. Esto no equivale a copiar la etiqueta truth: deben evitarse filtraciones por contenido, IDs, orden, timestamps, semillas, lineage, errores o metadatos. El estado interno del canal no se entrega al expediente.

Una S7 focal puede expresar inclusión o exclusión; no se necesitan clases diferentes para cada polaridad ni fuentes duplicadas que simulen corroboración. Las copias/derivados comparten lineage. La suficiencia de cobertura y la admisibilidad se evalúan por oportunidad/unidad×dimensión bajo el alcance ex ante.

No se fijan cardinalidad de oportunidades, dependencias, tasas, parámetros ni fuente concreta del microdominio. No se crean IDs de prueba ni se declara ejecución.



## 13. Mecanismo mínimo de oportunidad y emisión S7 tras DEC-C10-098

DEC-C10-098 cierra el marco esperado: una oportunidad lógica S7 por UE del censo B1/Need aprobado. La unidad de enumeración es UE × dimensión Need_preZ; no se enumeran múltiples fuentes semánticas para simular corroboración.

El proceso de observación se especifica conceptualmente en etapas separadas, sin fijar todavía una distribución ni parámetros:

1. **Oportunidad:** slot S7 esperado, identificado y sellado ex ante para la UE/B1/instancia de servicio y dimensión focal. Su existencia no depende de truth, Z/D2, evidencia encontrada o resultados.
2. **Mandato y alcance:** atribución preespecificada de autodeclaración de B1 sobre su propio objetivo focal; autoridad limitada a ese objeto y versión. No implica autoridad técnica sobre el servicio o configuración.
3. **Resultado de emisión/contenido:** el canal de medición produce uno de los estados semánticos compatibles con el contrato: inclusión afirmativa, exclusión focal afirmativa, ambigüedad/conflicto o no emisión. La relación con truth debe estar mediada por una regla explícita del canal; no se permite la copia directa de la etiqueta.
4. **Captura/retención:** el artefacto emitido puede ser capturado, retenido, perdido o quedar fuera de alcance. La pérdida no altera el contenido original ni convierte ausencia en exclusión.
5. **Admisibilidad/cobertura:** se aplican controles de autoridad, binding, event_time pre-Z, integridad, lineage y cierre del universo. COMPLETE significa examen de la oportunidad y superficies incluidas, no resultado negativo.
6. **Adjudicación:** E1/E2 reciben solo el expediente permitido; sus salidas independientes se sellan antes de abrir truth para evaluación.

Una declaración puede ser auténtica (origen/mandato/provenance válidos) y semánticamente errónea. Por ello la exactitud no se deduce de la firma ni de la autoridad. La evaluación debe distinguir errores de polaridad (falso positivo/falso negativo) de abstención, ambigüedad, pérdida y bloqueos técnicos.

No se impone independencia entre etapas ni se asignan probabilidades. En particular, la enumeración ex ante de la oportunidad es independiente de truth y de tratamiento, pero el contenido del canal puede depender del estado basal mediante un mecanismo explícito. Los parámetros, soporte de escenarios y sensibilidad permanecen OPEN.

La oportunidad única reduce la necesidad de modelar dependencias entre múltiples declaraciones S7, pero no elimina dependencia entre unidades si comparten proceso, plantilla, canal, versión o causa de error; esa posibilidad deberá declararse en el DGP.

**Estado:** cardinalidad lógica aceptada; mecanismo conceptual de etapas especificado; parámetros, dependencias, escenarios y materialización OPEN. No ejecución.


## 14. Estructura lógica del canal S7: estados, orden y fronteras (propuesta 2026-11-12)

**Estado:** propuesta de especificación lógica derivada de DEC-C10-097/098; no constituye aceptación de parámetros, distribución, grafo estadístico congelado ni autorización de implementación.

### 14.1 Principio: oportunidad fija, resultado observacional variable

La oportunidad S7 por UE es un elemento del marco esperado, enumerado ex ante. No es el resultado de emisión. Por tanto, el canal no debe representarse con un único campo agregado de disponibilidad que mezcle fenómenos distintos.

La secuencia lógica mínima es:

OPPORTUNITY_FIXED → EMISSION_OUTCOME → SEMANTIC_CONTENT (si emitida) → CAPTURE_OUTCOME → ADMISSIBILITY_AND_BINDING → E1/E2_ADJUDICATION → SEALED_EVALUATION

La secuencia define dependencias temporales y de disponibilidad; no presupone independencia estadística entre etapas.

### 14.2 Estados conceptuales separados

| Capa | Estados lógicos mínimos | Interpretación |
|---|---|---|
| Oportunidad | EXPECTED | La oportunidad S7 existe en el marco ex ante para UE × Need_preZ |
| Emisión | ISSUED, NOT_ISSUED | Se produjo o no una declaración atribuible al mandato B1 |
| Contenido (solo si ISSUED) | ASSERT_INCLUDE, ASSERT_EXCLUDE, AMBIGUOUS, INTERNALLY_CONFLICTING | Proposición visible de inclusión/exclusión focal, ambigüedad o contradicción dentro del propio artefacto |
| Captura/retención (solo si ISSUED) | CAPTURED, NOT_CAPTURED_OR_LOST | Si el artefacto emitido llegó al expediente accesible |
| Integridad/identidad/temporalidad/binding | VALID, INVALID_OR_UNVERIFIABLE por dimensión | Controles de admisibilidad, no resultados semánticos |
| Alcance/cobertura | NONE, PARTIAL, COMPLETE | Grado de examen del universo y superficies declaradas |
| Adjudicación por evaluador | 1, 0, ?, TECHNICAL_BLOCK | Dictamen E1 o E2 bajo reglas existentes; no es estado de la fuente |

NOT_ISSUED no tiene contenido ni captura; NOT_CAPTURED_OR_LOST solo puede ocurrir si hubo emisión. Los estados de integridad y cobertura no deben convertirse en contenido ni confundirse con ? de truth. TECHNICAL_BLOCK se mantiene fuera de la clasificación semántica observada.

### 14.3 Relación entre truth y contenido: matriz semántica, no etiqueta copiada

El canal puede producir contenido condicionado por la estipulación basal, pero el artefacto visible debe expresar una proposición declarativa y su alcance, nunca un campo/flag que revele need_truth_state.

| Truth reservada | ASSERT_INCLUDE | ASSERT_EXCLUDE | AMBIGUOUS / no emisión / pérdida |
|---|---|---|---|
| 1 | Declaración semánticamente concordante | Declaración semánticamente errónea (candidata a falso negativo si es admisible) | Abstención/insuficiencia; no falso negativo binario |
| 0 | Declaración semánticamente errónea (candidata a falso positivo si es admisible) | Declaración semánticamente concordante | Abstención/insuficiencia; no verdadero negativo binario |
| ? | Afirmación observable sin clase gold binaria para puntuar exactitud | Afirmación observable sin clase gold binaria para puntuar exactitud | Resultado no binario; se informa según su naturaleza |

La tabla describe concordancia semántica para evaluación posterior. No ordena que el canal produzca ambos contenidos en cada estado truth ni fija probabilidades, tasas o prevalencias. Para truth ?, no se fuerza ambigüedad del artefacto: ? es indeterminación de la estipulación de referencia, no una instrucción al canal ni un resultado de observación.

Una declaración positiva/negativa solo cuenta como error de clasificación cuando fue emitida, capturada, admisible, vinculada y adjudicada como 1/0. Una declaración errónea pero auténtica puede ser admisible; su error solo se conoce al abrir truth tras el sellado.

### 14.4 Factorización lógica sin supuesto de independencia

Para diseñar el DGP, la distribución conjunta puede describirse por una factorización condicional de cadena, por ejemplo:

P(E,C,K | T,X₀,V_ch) = P(E | T,X₀,V_ch) · P(C | E,T,X₀,V_ch) · P(K | E,C,T,X₀,V_ch)

donde E es emisión, C contenido, K captura/retención, T estipulación basal reservada, X₀ solo covariables/contexto basal explícitamente autorizados y V_ch la versión del canal. Esta escritura es una identidad de factorización conjunta, no tres hipótesis de independencia. Si el DGP finalmente usa mecanismos deterministas o variables latentes explícitas, deberá documentarlo de forma equivalente.

La enumeración de la oportunidad no entra como resultado aleatorio: EXPECTED queda fijado para cada UE del censo. La integridad, autoridad, temporalidad y binding se evalúan como atributos/controles de artefacto y de contrato; no se deben esconder dentro de una tasa agregada de observabilidad.

### 14.5 Mandato, autenticidad y conflicto con una única oportunidad

La atribución de B1 como declarante queda limitada al objetivo propio y a la versión B1–UE–service_instance en t−1. La autenticidad del origen/mandato no implica corrección semántica.

Con una sola oportunidad semántica S7 por UE:
- INTERNALLY_CONFLICTING solo describe contradicciones dentro del mismo artefacto/acto declarativo;
- copias, exports y transformaciones conservan el mismo lineage y no son nuevas declaraciones;
- un desacuerdo E1/E2 es desacuerdo entre adjudicadores, no conflicto entre fuentes;
- no se presupone una segunda fuente independiente que corrobore o contradiga S7;
- si un futuro microdominio exige múltiples actos declarativos independientes, deberá revisarse DEC-C10-098 mediante decisión explícita, no multiplicar oportunidades silenciosamente.

La autoridad/mandato se preespecifica ex ante y se comprueba por provenance. Una falla de autoridad, binding o versión conduce a inadmisibilidad/bloqueo según la regla aplicable, no a una declaración semántica negativa.

### 14.6 Reglas de no filtración y temporalidad

El canal y sus artefactos no pueden revelar truth mediante etiqueta o código directamente equivalente a 1/0/?, contenido auxiliar, nombre de archivo, ID, orden de filas, secuencia de emisión, timestamps, semillas, digests, lineage o patrones de error que permitan reconstrucción trivial. Tampoco se exportan truth_basis_ref, flags internos, estado del generador o variables de evaluación.

La truth puede ser una causa oculta del mecanismo de contenido/emisión, pero la implementación debe probar que el expediente observable no contiene un canal lateral determinista. Las claves técnicas para replay, si pudieran revelar truth, permanecen segregadas del bundle adjudicable.

El contenido declarativo se refiere a t−1. Una captura posterior solo se admite si preserva un artefacto inmutable creado antes de Z y su temporalidad puede verificarse. Un texto generado después de Z no se convierte en evidencia pre-Z por asignarle un event_time anterior.

### 14.7 Consecuencia para E1/E2 y Analyzer PE

E1 y E2 reciben el mismo expediente visible autorizado y realizan adjudicaciones Need independientes. La evaluación de su exactitud se efectúa tras sellado contra TRUTH_LEDGER.

El Analyzer PE no es un tercer adjudicador de Need ni recibe truth, contenido interno del canal, probabilidades generadoras o resultados E1/E2 antes de su propio sellado. Su evaluación de constructos/estimandos PE sigue su contrato separado y sus oráculos DGP. No se computa una métrica de exactitud Need para Analyzer PE salvo decisión futura que cambie explícitamente esa frontera.

### 14.8 Qué queda especificado y qué no

**Especificado como estructura lógica propuesta:** orden de etapas; estados no colapsables; relación semántica truth-contenido; distinción entre error y abstención; alcance de autodeclaración; unicidad S7; conflicto interno vs desacuerdo E1/E2; controles de firewall.

**OPEN:** si el mecanismo es determinista, probabilístico o mixto; variables basales autorizadas X₀; dependencia entre unidades por canal/plantilla/versión; soporte de escenarios; parámetros y rangos; tasas de emisión/error/ambigüedad/pérdida; calibración/sensibilidad; precisión/potencia; implementación y pruebas técnicas del firewall.

No se crea un nuevo artefacto lógico, una nueva clase de fuente, un rol PE, una variable causal, un test ID ni una tabla física. No se materializa ni ejecuta.
