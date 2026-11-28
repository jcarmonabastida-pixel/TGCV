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



## 15. Admisibilidad de variables basales como condicionantes del canal S7 (propuesta, no freeze)

### 15.1 Hallazgo de reconstrucción histórica

El diagnóstico basal existente (§§2–7 de C10_S_B1_PREZ_BASELINE_SOURCE_DIAGNOSTIC_DRAFT_001.md) ya examinó las variables t−1 disponibles: X, H₀, C_c, L_m, C_dep, A_f*, T_acc y F_alt, además de CMP/PAR/REF/RUL, ENABLED/PROFILE y eventos de petición. Ninguna tiene un mapping semántico aprobado que justifique definir Need o condicionar la declaración S7. No se debe reabrir ese diagnóstico ni convertir la mera disponibilidad de una variable en autorización causal.

La composición de truth permanece explícita, versionada y reservada por B1/UE (DEC-C10-095). No se deriva de covariables. La oportunidad S7 es fija ex ante (DEC-C10-098). El contenido observable puede depender del estado basal oculto mediante un canal de medición explícito (DEC-C10-097/098), pero no copia la etiqueta.

### 15.2 Regla provisional de admisibilidad

En el diseño base actualmente documentado, **no se admite ninguna covariable basal del roster causal (X, H₀, C_c, L_m, C_dep, A_f*, T_acc, F_alt) como predictor/condicionante de la emisión o del contenido S7**. Esto no afirma independencia estadística entre esas variables y Need, ni niega que propiedades basales de fuente/canal/custodio puedan afectar a la observabilidad. Significa que no existe justificación contractual por variable para introducir aquellas covariables en el mecanismo de medición.

Deben distinguirse tres clases:
- **Estado objetivo reservado:** la estipulación explícita Need_preZ puede determinar semánticamente el contenido que intenta expresar S7, a través del mecanismo de medición; nunca se copia como etiqueta.
- **Condiciones de protocolo fijadas ex ante:** oportunidad, mandato, alcance, versión S7 y regla de emisión. No son covariables aleatorias.
- **Propiedades operativas del proceso observacional:** emisión, retención/captura, integridad, autoridad y custodia. DEC-C10-097 permite que propiedades basales de fuente/canal/custodio condicionen la observabilidad si se especifican y justifican ex ante. No están todavía identificadas ni parametrizadas para este microdominio.

La truth no es un campo del artefacto visible ni se entrega al emisor como etiqueta. Es el estado de referencia reservado que el canal de medición intenta representar, protegido por el firewall. No se introduce un agente cognitivo, creencia, predictor ni covariable causal nueva.

### 15.3 Qué dependencias se permiten conceptualmente

| Relación | Estado de diseño |
|---|---|
| Truth basal → emisión/contenido S7 a través del canal de medición | Permitida y necesaria para que la declaración mida el constructo; mecanismo no especificado |
| Versión/mandato S7 → reglas de emisión y formato | Permitida como condición de diseño fijada ex ante |
| Contenido emitido → captura/retención | Permitida como dependencia del proceso de captura; mecanismo no especificado |
| Covariables del roster causal X/H₀/C_c/L_m/C_dep/A_f*/T_acc/F_alt → emisión/contenido/captura | No admitidas en el DGP base; requieren mapping semántico y justificación específica por etapa |
| Propiedades propias del canal/custodio (p. ej., regla de retención o integridad) → captura/admisibilidad | Conceptualmente admisibles bajo DEC-C10-097; todavía no identificadas, definidas ni parametrizadas |
| ENABLED/PROFILE, configuración CMP/PAR/REF/RUL → contenido S7 | No acreditan el objetivo B1 ni son sustitutos de la estipulación |
| Reach/instalación/solicitudes/ejecución/Outcome/Value → canal basal | Excluidas por diferencia semántica, temporalidad o circularidad |
| Z/D2/asignación/cumplimiento/post-Z → oportunidad o contenido basal | Prohibida |
| Salidas E1/E2/Analyzer → canal | Prohibida (retroalimentación/filtración) |

La tabla es un límite de diseño, no una afirmación de independencia estadística universal. Las relaciones no admitidas quedan fuera del modelo base hasta que exista una decisión explícita y evidencia de que la variable es un determinante legítimo del proceso de medición, no un proxy del constructo.

### 15.4 Requisitos para admitir una covariable en una versión futura

Cada candidata deberá aportar, antes de incorporarse:
1. definición semántica exacta y referente (B1, UE, servicio, declarador o canal);
2. momento de medición y prueba de que existe en t−1;
3. mecanismo plausible que explique por qué afecta a emisión, contenido o captura, identificando cuál etapa;
4. distinción entre determinante del proceso de medición y determinante del propio Need;
5. evidencia de que no es consecuencia de Z, D2, accesibilidad, resultados ni decisiones de E1/E2;
6. regla de medición, missingness, integridad, versión y provenance;
7. consecuencias para dependencia entre unidades y para el estimando de validación;
8. análisis de sensibilidad o contraste adversarial que permita comprobar si su inclusión cambia el rendimiento/errores de forma relevante.

No basta una correlación, disponibilidad técnica, comodidad de programación ni mejorar artificialmente la dificultad del Analyzer. La incorporación requiere actualización del contrato y decisión de diseño; no se añade una lista abierta de covariables por defecto.

### 15.5 Implicación para la especificación estadística

Hasta que se justifique una covariable, el DGP no asignará probabilidades condicionales a X₀ ni supondrá independencia marginal de X₀. El canal se describirá mediante un mecanismo conjunto condicional al estado basal reservado y a la versión/mandato S7. La factorización de emisión, contenido y captura es una identidad de distribución conjunta, no un supuesto de independencia.

La dependencia entre UE por plantilla, canal compartido, versión, lote o causa común de error sigue OPEN: una oportunidad por UE no demuestra independencia entre unidades. No se introducen latentes compartidas ni se fijan tasas/probabilidades sin justificación.

**Dictamen provisional corregido:** ninguna covariable del roster causal está admitida como predictor del canal S7. No se concluye que todas las propiedades basales del proceso de observación sean irrelevantes: su admisión queda abierta bajo la distinción anterior y los requisitos de §15.4. La relación de medición entre Need basal y contenido observable debe permanecer explícita. No se materializa ni ejecuta.


## 16. Taxonomía cualitativa de modos de error S7 y contrastes de validación (propuesta, no freeze)

### 16.1 Dos niveles que no deben confundirse

El canal produce un artefacto y un estado de proceso; E1/E2 producen una adjudicación observed. Por tanto:
- **Error del canal:** el contenido emitido no representa correctamente la estipulación focal, o el proceso impide que una declaración pertinente llegue íntegra al expediente.
- **Error de adjudicación:** E1/E2 interpretan incorrectamente un expediente observable válido, o difieren/no pueden resolverlo.
- **Error de clasificación evaluado:** solo se establece después del sellado, comparando observed=1/0 con truth=1/0. La discordancia del artefacto por sí sola no basta para declarar un falso positivo/negativo del adjudicador.

### 16.2 Modos de error diferenciados

| Modo | Manifestación S7 | Consecuencia esperada según contratos | Qué permite evaluar |
|---|---|---|---|
| Inversión semántica positiva | Truth=1 y contenido afirmativo de exclusión | Si admisible y adjudicado 0, falso negativo de clasificación | Sensibilidad ante error de polaridad |
| Inversión semántica negativa | Truth=0 y contenido afirmativo de inclusión | Si admisible y adjudicado 1, falso positivo de clasificación | Especificidad ante error de polaridad |
| Ambigüedad genuina | Contenido emitido que no resuelve inclusión/exclusión | observed=? salvo resolución fundada en el propio expediente | Abstención y preservación de incertidumbre |
| No emisión | Oportunidad EXPECTED sin declaración emitida | No es exclusión; normalmente observed=? | Robustez ante silencio |
| Pérdida de captura/retención | Declaración emitida, pero no llega al expediente | No es exclusión; normalmente observed=? | Robustez ante pérdida |
| Opacidad/cobertura parcial | Artefacto o superficie no inspeccionable | observed=? o cobertura PARTIAL | Sensibilidad a cobertura insuficiente |
| Defecto de identidad/binding | Declaración asociada a B1/UE/servicio equivocado o no verificable | Inadmisibilidad o bloqueo según contrato; nunca evidencia focal positiva/negativa | Integridad del vínculo |
| Defecto temporal | Contenido creado después de Z presentado como basal | Inadmisible/bloqueo; no se rescata por timestamp retroactivo | Protección pre-Z |
| Defecto de autoridad/vigencia | Emisión auténtica en origen, pero sin mandato/alcance/versionado suficiente | No admisible para afirmar Need | Separación autenticidad/autoridad |
| Corrupción/integridad | Contenido o digest no verificable | Bloqueo/inadmisibilidad según contrato | Integridad del paquete |
| Conflicto interno | Afirmaciones incompatibles dentro del mismo acto S7 sin regla de resolución | observed=? mientras no se resuelva | Preservación de conflicto |
| Filtración lateral | ID, orden, metadata, semilla o lineage permite reconstruir truth | Incumplimiento crítico del firewall; invalida la evaluación ciega | Validez de la separación truth/evidence |

La tabla no asigna frecuencias, severidades numéricas ni obliga a que todos los modos ocurran en el escenario confirmatorio. No añade nuevas clases de fuente: todos son estados o defectos del único acto S7 y de su proceso de observación.

### 16.3 Contrastes mínimos a preservar en la futura especificación de escenarios

La matriz de escenarios deberá distinguir, como mínimo, las siguientes condiciones cualitativas, sin fijar tasas ni parámetros:

1. **Canal semánticamente concordante:** contenido afirmativo correcto y expediente íntegro/admisible. Es referencia de funcionamiento, no supuesto de perfección universal.
2. **Polaridad errónea:** contenido afirmativo opuesto a la estipulación; debe permitir evaluar FP/FN una vez adjudicado.
3. **Abstención semántica:** contenido ambiguo, sin contenido suficiente para 1/0.
4. **Silencio de emisión:** oportunidad existente pero no emitida.
5. **Pérdida de captura:** emitida pero no capturada/retendida.
6. **No evaluabilidad documental:** opacidad, cobertura incompleta o defecto de autoridad/identidad/tiempo/integridad, manteniendo separados los bloqueos técnicos de observed=?
7. **Prueba de firewall:** ninguna salida visible permite reconstruir truth ni acceder a truth_basis_ref o estado interno del generador.

Estos contrastes son una taxonomía de mecanismos y resultados, no un diseño factorial aprobado. No se exige combinarlos todos ni repetirlos por cada truth state. El soporte real de cada contraste, su asignación a unidades, posibles interacciones y el orden de ejecución siguen OPEN.

### 16.4 Regla contra el canal perfecto y contra errores artificiales

El contrato requiere que el diseño pueda evaluar errores semánticos y abstenciones; no exige que cada ejecución contenga necesariamente errores, ni autoriza imponer una tasa positiva arbitraria. Tampoco permite declarar el canal perfecto por construcción si el objetivo experimental es validar su capacidad para recuperar una truth bajo observación imperfecta.

Antes de elegir el mecanismo confirmatorio deberá justificarse qué contrastes pertenecen al DGP base, cuáles son escenarios adversariales de sensibilidad y cuáles son simples fallos técnicos. La selección no puede depender de resultados del Analyzer ni de métricas observadas.

### 16.5 OPEN explícitos

Permanecen sin decidir:
- si emisión, contenido y captura son deterministas, probabilísticos o mixtos;
- qué propiedades operativas basales de canal/custodio están presentes en el microdominio;
- si existen causas comunes entre unidades y cómo representarlas;
- qué modos de error forman parte del escenario confirmatorio y cuáles de sensibilidad;
- parámetros, rangos, tasas, soporte, tamaños, precisión y potencia;
- cómo verificar técnicamente el firewall y el sellado.

No se fijan probabilidades, prevalencias, tasas de error ni nuevas pruebas/IDs. No se crea un artefacto lógico, clase de fuente, variable causal o schema físico adicional. No se materializa ni ejecuta.


## 17. Asignación de modos de error: núcleo confirmatorio, sensibilidad y pruebas adversariales (propuesta)

### 17.1 Criterio de separación

La asignación no se realiza por conveniencia ni por la frecuencia esperada de un modo, sino por la pregunta que permite responder y por si el expediente resultante sigue siendo admisible para adjudicar Need.

Se distinguen tres familias:

- **Núcleo confirmatorio de medición:** casos en los que existe una oportunidad S7 emitida, capturada, íntegra, correctamente vinculada, pre-Z y con autoridad/alcance suficientes. El contenido puede ser semánticamente concordante o contener una inversión de polaridad. En ambos casos E1/E2 reciben un expediente formalmente admisible y su capacidad de interpretación puede evaluarse contra truth tras el sellado.
- **Sensibilidad de observación/cobertura:** casos en los que la información no llega, llega incompleta o no permite una decisión semántica. Evalúan cobertura, abstención y robustez del procedimiento; no deben mezclarse con la matriz binaria de clasificación como si fueran errores 1/0.
- **Pruebas adversariales de integridad y cegamiento:** casos con identidad, tiempo, autoridad, integridad o metadata defectuosos. Evalúan si el sistema detecta y bloquea evidencia inadmisible o filtraciones; no son observaciones válidas para estimar exactitud ordinaria de E1/E2.

### 17.2 Asignación recomendada de los doce modos

| Modo | Ubicación recomendada | Tratamiento confirmatorio |
|---|---|---|
| Declaración concordante | Núcleo confirmatorio | Incluir como referencia de adjudicación sobre evidencia válida; no asumir que agota el escenario |
| Inversión semántica positiva/negativa | Núcleo confirmatorio, como contraste de error semántico | Incluir como posibilidad explícita del mecanismo de medición, sin imponer frecuencia ni tasa |
| Ambigüedad genuina | Sensibilidad de observación/abstención | Informar observed=?, cobertura y abstención; no puntuar como FP/FN binario |
| No emisión | Sensibilidad de observación/cobertura | Oportunidad esperada sin artefacto; no es observed=0 |
| Pérdida de captura/retención | Sensibilidad de observación/cobertura | Distinguir de no emisión; no es observed=0 |
| Opacidad/cobertura parcial | Sensibilidad de observación/cobertura | Estado PARTIAL/no evaluable según alcance; no convertirlo en clasificación negativa |
| Defecto de identidad/binding | Prueba adversarial de integridad | Rechazar o bloquear el caso afectado; no adjudicar contenido como si fuera de la UE focal |
| Defecto temporal | Prueba adversarial de integridad | Rechazar contenido no acreditado como pre-Z; no retrofecharlo |
| Autoridad/vigencia insuficiente | Prueba adversarial de admisibilidad | Excluir la declaración como evidencia afirmativa; preservar el motivo |
| Corrupción/integridad | Prueba adversarial de integridad | Bloquear/excluir según contrato y conservar diagnóstico |
| Conflicto interno | Sensibilidad semántica, con prueba adversarial si se manipula la estructura | observed=? si el conflicto es genuino y no resoluble; corrupción o manipulación estructural se bloquea |
| Filtración lateral | Prueba adversarial crítica de firewall | Cualquier filtración invalida el cegamiento del paquete afectado; no se informa como simple error de clasificación |

### 17.3 Qué significa «núcleo confirmatorio»

El núcleo confirmatorio no es un canal perfecto ni presupone una tasa de error. Su dominio de evaluación se limita a expedientes S7 admisibles y contiene, como clases de contraste, contenido concordante y la posibilidad de polaridad semántica errónea para truth=1 y truth=0.

La comparación de adjudicación binaria se realiza solo en unidades con truth 1/0 y salida observed 1/0. Se informan además, sin ocultarlos:
- unidades truth 1/0 con observed=?;
- unidades sin salida o con error técnico;
- cobertura y estado de la oportunidad S7;
- denominadores por clase y por E1/E2.

La exactitud condicionada a los casos adjudicables no puede presentarse sola como rendimiento global. Sensibilidad, especificidad y tasas de abstención deben acompañarse de cobertura y de los denominadores que las definen. No se derivan valores predictivos poblacionales de una composición de truth configurada para validación sin justificar representatividad.

El dominio del DGP debe especificar concordancia y permitir discordancia semántica como posibilidades del canal, pero no exige que las cuatro combinaciones truth–contenido aparezcan forzosamente en el censo realizado. La truth 1/0 debe tener soporte en la cohorte conforme a DEC-C10-095; el soporte de cada celda cruzada se informa y se exige solo para la afirmación/contraste que la necesita, conforme a §18. Esto no autoriza fijar proporciones, balance, prevalencias ni asignación por brazo. Si falta soporte, se limita o bloquea el contraste correspondiente, sin añadir unidades post hoc.

### 17.4 Separación de denominadores y dictámenes

No se utilizará un único denominador para todas las preguntas:

1. **Censo de unidades B1/UE:** todas las unidades del roster aprobado al que aplica B1/Need, conforme a DEC-C10-096.
2. **Oportunidades S7 esperadas:** una por UE, conforme a DEC-C10-098; este es el marco para emisión/captura/cobertura.
3. **Casos con expediente admisible:** subconjunto con fuente válida para adjudicación; se informa su cobertura respecto del censo, sin redefinir la cohorte.
4. **Casos binariamente evaluables:** truth 1/0 y observed 1/0; denominador de métricas de clasificación, siempre acompañado de abstenciones y no evaluables.
5. **Casos de prueba adversarial:** paquetes/casos designados para verificar rechazo, bloqueo y firewall; no se mezclan con el estimador de exactitud confirmatoria.

El filtro de expediente admisible no modifica retrospectivamente la pertenencia al censo ni al ITT. La pérdida diferencial o la selección de casos adjudicables puede sesgar métricas condicionadas; deberá describirse y analizarse, no corregirse con una suposición automática de MCAR/MAR/MNAR.

### 17.5 Restricciones y cuestiones no resueltas

- La taxonomía asigna funciones a los modos; no define aún un factorial, secuencia, N, repetición, parámetro ni tasa.
- No se presupone que los errores semánticos sean independientes de truth, canal o unidades. El mecanismo conjunto y cualquier causa común deben justificarse en el DGP.
- La única oportunidad S7 por UE limita la corroboración dentro de la unidad; copias/derivados no aumentan el número de fuentes independientes.
- Los fallos adversariales deben estar aislados del flujo confirmatorio y etiquetados por el protocolo de prueba, sin que esa etiqueta revele truth a E1/E2.
- El firewall se evalúa antes de interpretar métricas de clasificación; si hay filtración, la evaluación ciega afectada queda INVALID.
- No se modifican DEC-C10-095/096/097/098 ni se crea una nueva decisión aceptada. Esta asignación es una propuesta para revisión, no un freeze ni autorización de materialización/ejecución.

**Dictamen provisional:** ERROR_MODES_CLASSIFIED_BY_EVALUATION_PURPOSE / CONFIRMATORY_DOMAIN_PROPOSED / SENSITIVITY_AND_ADVERSARIAL_SEPARATED / SUPPORT_AND_PARAMETERIZATION_OPEN / NOT_IMPLEMENTED / NOT_EXECUTED.


## 18. Soporte de las combinaciones truth–contenido S7 y alcance de los contrastes (propuesta)

### 18.1 Matriz semántica de cuatro combinaciones

La relación entre truth reservada y contenido declarativo debe examinarse como una matriz cruzada, sin confundir el contenido de la fuente con la adjudicación E1/E2:

| Truth reservada | Contenido S7 afirmativo de inclusión | Contenido S7 afirmativo de exclusión |
|---|---|---|
| Need_truth=1 | Concordancia semántica | Inversión positiva (discordancia) |
| Need_truth=0 | Inversión negativa (discordancia) | Concordancia semántica |

La matriz tiene cuatro celdas lógicas. No representa cuatro fuentes ni cuatro oportunidades por UE: DEC-C10-098 mantiene una única oportunidad S7 por UE. Tampoco representa cuatro estados de salida del adjudicador. E1 y E2 reciben el contenido visible y producen cada uno su propia salida observed=1/0/?; solo después del sellado se compara con truth.

Las declaraciones ambiguas, no emitidas, perdidas o inadmisibles no pertenecen a ninguna de las dos columnas afirmativas. Deben conservar sus estados propios y no imputarse a inclusión o exclusión.

### 18.2 Tres preguntas científicas diferentes

La matriz permite distinguir tres objetos que no deben colapsarse:

1. **Mecanismo de observación S7:** qué contenido produce el canal para cada estado basal y bajo qué condiciones de emisión/captura. La discordancia truth–contenido es un error semántico del canal, no todavía un error de E1/E2.
2. **Interpretación de E1/E2:** si cada adjudicador interpreta correctamente una declaración afirmativa admisible de inclusión o exclusión. La evaluación de esta capacidad requiere que ambas polaridades sean observables en los expedientes que se le presentan.
3. **Clasificación Need respecto de truth:** si la salida observada de cada adjudicador coincide con truth. Depende conjuntamente del canal y de la adjudicación; no identifica por sí sola cuál de ambos produjo la discordancia.

Un adjudicador puede interpretar correctamente una declaración de exclusión y aun así discrepar de truth=1 porque S7 produjo una declaración errónea. Inversamente, una declaración concordante no prueba por sí sola que el adjudicador haya aplicado correctamente las reglas: se debe conservar su salida individual y rationale.

### 18.3 Regla para el escenario confirmatorio censal

El escenario confirmatorio conserva el censo completo del roster B1/UE aprobado y una oportunidad S7 por UE. No se seleccionan unidades ni se altera la estipulación para llenar celdas.

El mecanismo generador podrá producir contenido concordante o discordante conforme a un modelo de observación explícito y justificado. La dependencia del contenido respecto de truth solo podrá operar a través del mecanismo S7 especificado; queda prohibido copiar directamente need_truth_state, exponer truth_basis_ref o utilizar metadatos que revelen la etiqueta reservada. No se presupone independencia estadística del canal respecto de truth ni se fija una tasa de error.

Después de generar y sellar el expediente, se informa el soporte realmente observado en las cuatro celdas, junto con:
- unidades truth=1 y truth=0 del censo;
- oportunidades S7 esperadas, emitidas y capturadas;
- contenido afirmativo de inclusión y de exclusión;
- expedientes admisibles, ambiguos, parciales, perdidos y bloqueados;
- salidas E1 y E2 por separado, incluyendo observed=? y ausencia de salida.

La ausencia de una celda se declara **CELL_SUPPORT_MISSING** para el contraste correspondiente. No se corrige añadiendo unidades, reetiquetando truth, reasignando contenido después de observar resultados, duplicando documentos ni seleccionando una subcohorte. El censo y el ITT permanecen intactos.

### 18.4 Qué soporte es necesario para cada afirmación

| Afirmación o contraste | Soporte mínimo que debe verificarse | Consecuencia si falta |
|---|---|---|
| E1/E2 interpretan inclusión | Expedientes admisibles con contenido afirmativo de inclusión | No evaluable para esa polaridad |
| E1/E2 interpretan exclusión | Expedientes admisibles con contenido afirmativo de exclusión | No evaluable para esa polaridad |
| El canal puede producir discordancia cuando truth=1 | Celda truth=1 / exclusión | No se evalúa inversión positiva en el confirmatorio |
| El canal puede producir discordancia cuando truth=0 | Celda truth=0 / inclusión | No se evalúa inversión negativa en el confirmatorio |
| Rendimiento binario E1/E2 frente a truth | Truth 1 y 0, salidas observed 1/0 y cobertura/abstención informadas | Bloqueo de métricas binarias si falta una clase; límites explícitos si faltan otras celdas |
| Recuperación conjunta del canal y adjudicador | Soporte de las cuatro celdas y trazabilidad separada de contenido y salidas | No atribuir la fuente de error ni afirmar recuperación completa |

La presencia de ambas polaridades permite estudiar la interpretación de contenido, pero no garantiza por sí sola soporte para las dos inversiones semánticas. A su vez, el soporte de las cuatro celdas no demuestra suficiencia estadística, potencia, precisión ni representatividad. Esos gates continúan bajo los contratos estadísticos existentes (P177/P178/P182/P183).

### 18.5 Pruebas controladas de interpretación: alcance y límites

Si el roster confirmatorio no contiene las cuatro celdas, puede considerarse en una fase posterior una comprobación controlada de interpretación semántica con casos de prueba explícitamente etiquetados por contenido visible, sin acceso del adjudicador a truth. Esa comprobación tendría un objetivo limitado: verificar que E1/E2 aplican correctamente la regla de inclusión/exclusión a expedientes válidos.

No se debe presentar esa comprobación como:
- soporte de prevalencia o frecuencia de errores del canal;
- estimación de sensibilidad/especificidad poblacional;
- sustituto del censo de validación B1/UE;
- evidencia de rendimiento confirmatorio conjunto;
- fuente adicional S7 ni segunda oportunidad por UE.

Su diseño, ubicación dentro del catálogo existente e independencia de los expedientes confirmatorios quedan OPEN. La revisión posterior del catálogo ha precisado que MEAS/P182 se refieren a medición de accesibilidad y constructos O/V, no a la adjudicación Need; por tanto, no deben citarse como cobertura directa de esta tarea. Los controles genéricos FCM de independencia, desacuerdo, cegamiento, vínculos y cobertura sí son reutilizables para sus respectivos objetivos, sin cubrir por sí solos la interpretación semántica de las dos polaridades. No se crean ahora fixtures, IDs, casos materiales ni una nueva familia de tests.

### 18.6 Dictamen provisional y gates pendientes

- La matriz de cuatro combinaciones queda definida como marco de diagnóstico semántico.
- El escenario confirmatorio no está obligado a contener artificialmente las cuatro celdas; debe reportar el soporte que efectivamente produzca el mecanismo justificado sobre el censo congelado.
- La falta de soporte bloquea únicamente la afirmación/contraste que requiere esa celda; no autoriza alterar roster, truth o contenido.
- Las pruebas controladas de interpretación, si se justifican, permanecen separadas de la estimación confirmatoria del canal y del rendimiento conjunto.
- No se fijan prevalencias, tasas, probabilidades, asignaciones, dependencias ni tamaños.
- No se modifica DEC-C10-095/096/097/098, la definición de cohorte, la oportunidad S7, los seis artefactos lógicos ni el catálogo de pruebas.
- No se materializa ni ejecuta.

**Dictamen provisional:** FOUR_CELL_SEMANTIC_CROSSWALK_DEFINED / CONFIRMATORY_SUPPORT_EMPIRICAL_TO_ROSTER / NO_POST_HOC_CELL_FILLING / CONTROLLED_INTERPRETATION_TESTING_OPEN / PARAMETERIZATION_OPEN / NOT_IMPLEMENTED / NOT_EXECUTED.


## 19. Auditoría de reutilización del catálogo para E1/E2 y polaridades S7

### 19.1 Alcance de la revisión

Se revisó el registro C10_S_TEST_CONTRACT_REGISTER_DRAFT_001.md en la rama de investigación y los contratos B1 de adjudicación, paquete analítico, materialización mínima e inventario de fuentes. La pregunta fue si algún contrato existente prueba directamente que E1 y E2 interpretan inclusión y exclusión focal de S7 para Need_preZ, sin acceso a truth.

**Resultado:** el contrato B1 sí contiene reglas normativas operativas para las dos polaridades (contrato de objetivo §7.2–7.5 y nueva regla secuencial §7.6), pero el catálogo no contiene una prueba que aísle directamente la interpretación semántica de inclusión y exclusión por E1/E2 frente a una clave de contenido, independientemente de la truth basal. Los controles PKG/FCM y el crosswalk aceptado por DEC-C10-097 cubren requisitos relacionados (admisibilidad, evidencia negativa, cobertura, independencia y sellado), no ese contraste aislado. Esta conclusión es documental y no equivale a ejecución ni a auditoría del código.

### 19.2 Contratos existentes reutilizables, con alcance limitado

| Contrato existente | Reutilización legítima en B1/Need | Lo que no demuestra |
|---|---|---|
| FCM-04 | Detectar que E1/E2 compartan clasificación antes de registrar; preservar independencia | Que interpreten correctamente inclusión/exclusión |
| FCM-05 | Preservar desacuerdo 1 vs 0, opinión minoritaria y escalado según regla | Exactitud frente a truth ni interpretación de cada polaridad |
| FCM-06 | Verificar que truth DGP no sea accesible al analizador/adjudicadores | Ausencia técnica real de filtraciones en implementación |
| FCM-12 / FCM-17 | Exigir una fila/registro separado por evaluación y evaluador | Validez semántica de las salidas |
| FCM-18 | Exigir vínculo entre evidencia revisada, evaluador y adjudicación | Suficiencia o corrección de la interpretación |
| FCM-02 | Controlar unidad, versión y temporalidad de evidencia | Comprensión del contenido declarativo |
| FCM-03 / FCM-14 | Rechazar COMPLETE sin denominador o cobertura no resuelta | Cobertura semántica suficiente por polaridad por sí sola |
| UG-SR-A01-T06/T07 | Impedir observed=1/0 sin vínculo probatorio; observed=0 requiere además evidencia afirmativa y cobertura negativa suficiente | Que la exclusión focal se haya interpretado correctamente |
| PKG-05…PKG-13 (contratos B1 del paquete) | Separación truth/evidencia, independencia E1/E2, ausencia≠0, evidencia afirmativa para 0 y evaluación posterior al sellado | Contraste aislado de interpretación de cada polaridad frente a una clave de contenido visible |

Los IDs FCM y UG-SR-A01 son controles del esquema/procedimiento de evidencia; PKG-05…13 son requisitos del contrato B1. Su estado sigue siendo documental: no se declara implementación, ejecución ni PASS.

### 19.3 Contratos que no deben reutilizarse como si fueran B1/Need

- **MEAS-01…24:** miden A_f, D_f, T_acc y sus errores/estados; la presencia de falsos positivos/negativos o tres estados en ese dominio no convierte esas pruebas en adjudicación de Need_preZ.
- **P182-01/03/05 y P183-13:** DEC-C10-097 los cruza con PKG-09 para apoyar requisitos de evidencia negativa afirmativa, alcance/cobertura y límites de observación. No son, por ello, una prueba aislada de comprensión semántica de la declaración por E1/E2.
- **P182-06/11/12:** DEC-C10-097 los reutiliza junto con PKG-12/13 para independencia, desacuerdo, cegamiento y sellado. No demuestran exactitud por polaridad frente a una clave de contenido.
- **P182-07, MEAS-01…24 y MEAS-13:** mantienen su alcance propio de medición de A_f/D_f/T_acc u observación/missingness; no son exactitud de E1/E2 sobre Need.
- **P183-01…13 / MISS-01…15:** cubren ausencia, selección, censura y sensibilidad del análisis causal/medición. Pueden informar el tratamiento de pérdida y cobertura, pero no validan por sí solos la interpretación semántica S7.
- El crosswalk de DEC-C10-097 es una decisión aceptada de reutilización documental; no demuestra que los contratos estén implementados o ejecutados.

### 19.4 Gap preciso y decisión de diseño pendiente

La regla normativa de adjudicación ya está definida en el contrato B1 y se ha operacionalizado en su §7.6. Lo que queda sin prueba directa aislada en el catálogo es la siguiente pregunta:

> Dado un expediente S7 afirmativo, admisible, correctamente vinculado y pre-Z, ¿E1 y E2 aplican la regla funcional de Need de forma correcta y separada cuando el contenido expresa inclusión focal y cuando expresa exclusión focal?

Para responderla sin contaminar la estimación del canal se deben distinguir dos dimensiones:

1. **Interpretación por polaridad:** desempeño de E1 y E2 sobre contenido afirmativo de inclusión y exclusión, evaluado contra una clave de contenido visible preespecificada y segregada de truth Need. Esto comprueba lectura/regla semántica, no concordancia del canal con la truth basal.
2. **Validez de Need observada:** comparación posterior de need_observed_state con need_truth_state en EVALUATION_LEDGER, que combina el mecanismo S7 y la adjudicación. No atribuye automáticamente un desacuerdo al adjudicador.

Un benchmark controlado de interpretación, si se aprueba, no debe revelar truth ni la etiqueta de concordancia/discordancia a E1/E2. La clave de contenido visible es distinta de TRUTH_LEDGER; su custodia, sellado y apertura posterior deben definirse para que el benchmark no filtre la truth por metadatos, nombres, orden o logs. Los casos de interpretación deben quedar separados del censo confirmatorio y no presentarse como una segunda oportunidad S7 por UE.

### 19.5 Recomendación operativa

- Reutilizar FCM-02/03/04/05/06/12/14/17/18 y UG-SR-A01-T06/T07 para los controles que ya cubren.
- Reutilizar PKG-05…13 y el crosswalk específico de DEC-C10-097 (incluidos P182-01/03/05/06/11/12 y P183-13 en sus alcances respectivos) para separación, admisibilidad, cobertura, independencia y sellado.
- No presentar esos contratos como prueba aislada de comprensión semántica por polaridad.
- No crear ahora un nuevo test ID, fixture, benchmark ni clave materializada. Solo si se necesita atribuir por separado un error al adjudicador y no al canal deberá justificarse una comprobación controlada independiente.
- Antes de proponer una ficha adicional, comprobar si el contrato B1 de adjudicación puede incorporar una regla de interpretación observable y si el catálogo admite una especialización sin duplicar FCM/PKG.
- Mantener como preguntas abiertas el número/variedad de casos controlados, la clave de contenido, la independencia entre benchmark y cohorte confirmatoria, la regla de scoring, el tratamiento de ambigüedad y la evaluación por adjudicador.

**Dictamen provisional:** EXISTING_CONTRACTS_PARTIALLY_REUSABLE / NO_DIRECT_B1_POLARITY_INTERPRETATION_TEST_FOUND / MEAS-P182-P183_NOT_DIRECT_COVERAGE / NO_NEW_TEST_ID / INTERPRETATION_BENCHMARK_DESIGN_OPEN / NOT_IMPLEMENTED / NOT_EXECUTED.


## 20. Auditoría de suficiencia operativa de la regla de adjudicación B1 para S7

### 20.1 Resultado de la reconstrucción contractual

La revisión conjunta de:
- C10_S_B1_PREZ_ADJUDICATION_AND_CONSEQUENCE_RECONCILIATION_DRAFT_001.md, §§3–4;
- C10_S_B1_PREZ_OBJECTIVE_SPECIFICATION_CONTRACT_DRAFT_001.md, §§7.4–7.5 y 8;
- C10_S_B1_PREZ_EXCLUSION_RECONCILIATION_DRAFT_001.md, §§1–4;
- C10_S_B1_PREZ_ANALYTICAL_PACKAGE_CONTRACT_DRAFT_001.md, §§7–11;
- las reglas S7 y la taxonomía de observación de este documento;

permite corregir la conclusión de §19.4: **la regla semántica básica para interpretar las dos polaridades ya está definida documentalmente**. No falta decidir qué significa una declaración afirmativa de inclusión o exclusión.

La regla existente es:
- declaración S7 afirmativa de inclusión focal, admisible y alineada con el objetivo funcional versionado → observed=1;
- declaración S7 afirmativa de exclusión focal, admisible, con alcance y cobertura negativa suficientes → observed=0;
- ausencia/no emisión/pérdida, ambigüedad no resuelta, conflicto no resuelto, binding o temporalidad inciertos, autoridad insuficiente, integridad fallida u otra insuficiencia → observed=? o bloqueo técnico, según la naturaleza del defecto.

Esta regla se aplica a lo que la fuente declara, no a lo que el adjudicador cree que debería declarar según la truth. Una declaración auténtica, admisible y semánticamente explícita puede ser errónea respecto de need_truth_state; no debe corregirse silenciosamente por E1/E2.

### 20.2 Matriz correcta para evaluar por separado canal y adjudicador

La matriz truth–contenido de §18 debe ampliarse analíticamente con la salida del adjudicador. La salida esperada de E1/E2, para un expediente afirmativo admisible, sigue la polaridad visible de S7:

| Truth reservada | Contenido S7 visible | Salida correcta de E1/E2 según contenido | Diagnóstico posterior |
|---|---|---|---|
| 1 | Inclusión | observed=1 | Canal concordante; adjudicación alineada |
| 1 | Exclusión | observed=0 | Canal discordante; adjudicación puede estar correctamente alineada con la fuente |
| 0 | Inclusión | observed=1 | Canal discordante; adjudicación puede estar correctamente alineada con la fuente |
| 0 | Exclusión | observed=0 | Canal concordante; adjudicación alineada |

Por tanto, **E1/E2 no deben adjudicar directamente la truth**. Deben clasificar la evidencia observable aplicando la regla pública. Si truth=1 y S7 declara exclusión, la respuesta correcta de E1/E2 es observed=0, aunque posteriormente difiera de truth. De otro modo se convertiría al adjudicador en un corrector omnisciente del canal y se destruiría la separación de funciones.

La evaluación debe conservar dos comparaciones distintas, sin confundirlas:
1. **Interpretación:** salida E1/E2 frente a la polaridad afirmativa efectivamente expresada en el contenido S7 admisible.
2. **Validez de la observación:** contenido S7 frente a need_truth_state, abierta solo después del sellado.

La comparación observed frente a truth sigue siendo necesaria para evaluar el paquete completo, pero no identifica por sí sola el origen del desacuerdo.

### 20.3 Suficiencia y límites del contrato actual

| Elemento | Estado reconstruido |
|---|---|
| Definición funcional focal que debe reconocerse | Definida en contrato B1 §3 |
| Regla de truth 1/0/? | Definida y gobernada por DEC-C10-095 |
| Regla semántica observed=1 por inclusión | Definida en Objective Specification §7.5 y adjudicación §4.2 |
| Regla semántica observed=0 por exclusión focal | Definida en los mismos contratos, con evidencia afirmativa y cobertura |
| Separación de truth y evidencia | Definida documentalmente; control técnico no implementado |
| Requisitos de identidad, versión, temporalidad, autoridad, integridad y binding | Definidos como criterios de admisibilidad |
| Tratamiento de ausencia, ambigüedad, conflicto y evidencia insuficiente | Definido a nivel de estados y reglas generales |
| Procedimiento explícito de evaluación observed-vs-contenido, separado de truth | No especificado de forma expresa |
| Formato del rationale de E1/E2 y registro de la polaridad interpretada | No cerrado como esquema físico |
| Implementación de permisos, cegamiento y sellado | No implementada |

El gap residual no justifica un nuevo benchmark ni una nueva familia de pruebas por ahora. Es, en primer lugar, una cuestión de **trazabilidad evaluativa**: el expediente ya contiene el contenido visible y las salidas individuales; el flujo de evaluación debe poder verificar si cada salida sigue la polaridad de ese contenido antes de compararla con truth.

### 20.4 Recomendación mínima de reconciliación, pendiente de aceptación

Se recomienda conservar los seis artefactos lógicos y no crear un séptimo:
- EVIDENCE_LEDGER conserva el contenido S7 capturado, su polaridad semántica visible (cuando sea afirmativa y admisible), binding, provenance y estado de admisibilidad.
- ADJUDICATION_LEDGER conserva para E1 y E2 por separado observed_state, la evidencia referenciada y un rationale que identifique la regla de inclusión/exclusión aplicada o el motivo de ?/bloqueo.
- EVALUATION_LEDGER realiza, después de sellar adjudicaciones, dos diagnósticos diferenciados: (a) concordancia de observed_state con la polaridad visible admisible del S7 referenciado; (b) concordancia de observed_state con need_truth_state. La apertura de truth solo se usa para (b), nunca para retrocorregir (a).

La polaridad visible no es una segunda truth ni una clave secreta: es una propiedad derivable del contenido observable. Su clasificación evaluativa debe poder reconstruirse desde la evidencia sellada. Si se conserva como campo derivado, se documenta su regla/versionado y no se exporta metadata reservada. Los casos sin contenido afirmativo admisible no entran en la comparación binaria de interpretación; se informan como abstención, no evaluabilidad o bloqueo según corresponda.

Esta reconciliación puede incorporarse en los contratos B1 existentes y en los campos lógicos de EVALUATION_LEDGER, sin crear test ID, fixture, fuente, oportunidad S7, artefacto lógico ni benchmark separado. No modifica las decisiones aceptadas ni autoriza materialización, implementación o ejecución.

### 20.5 Dictamen y próximo gate

**Dictamen:** POLARITY_INTERPRETATION_RULE_DEFINED / NO_NEW_SEMANTIC_TEST_REQUIRED_AT_THIS_STAGE / EVALUATION_TRACEABILITY_GAP_OPEN / TWO_COMPARISONS_REQUIRED / CONTRACT_PROPAGATION_PENDING_USER_ACCEPTANCE / NOT_IMPLEMENTED / NOT_EXECUTED.

El siguiente gate, si se acepta esta reconciliación, es propagar la distinción de las dos comparaciones a los contratos B1 de adjudicación y paquete analítico, comprobar consistencia con el maestro DGP y revisar que los seis artefactos lógicos pueden registrarla sin alterar su cardinalidad. Solo después se decidirá si hace falta una prueba contractual específica para verificar la regla; no se presupone ni se crea ahora.
