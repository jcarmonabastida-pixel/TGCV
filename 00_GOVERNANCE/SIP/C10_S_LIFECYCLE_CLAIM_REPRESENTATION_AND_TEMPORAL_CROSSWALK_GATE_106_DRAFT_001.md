# C10-S — Gate 106: comparación de representación claim-level y crosswalk temporal

**Estado:** HISTORICAL RECONSTRUCTION COMPLETED / THREE REPRESENTATION ALTERNATIVES COMPARED / NO OPTION FULLY ACCEPTED / CLAIM-LINK CAPABILITY QUALIFIED / TEMPORAL SEMANTICS SEPARATED / CLOCK CONTRACT OPEN / C0 UNCHANGED / NO SCHEMA CHANGE / NO IMPLEMENTATION / NO EXECUTION / NO FREEZE  
**Fecha:** 2026-11-15  
**Rama:** research/c10-s-consolidation-draft · PR #116 Draft  
**Precedencia:** Gate 98 successor; Gates 99–105; DEC-C10-061/065/067/070/071/083/088; U_G Inventory Register Template §§2, 5, 6, 12.1–12.10, 15.4–15.6, 17–20, 24, 26–28; U_G Evidence/Provenance/Adjudication Protocol §§4–10, 13–20; Temporal Horizon and S4R Integration Audit §§11–18; DGP Temporal and Role Contract. No se modifican decisiones aceptadas.

---

## 1. Pregunta y dictamen ejecutivo

Gate 106 compara las tres alternativas identificadas por Gate 105 para representar las seis dimensiones lifecycle de NODE y sus evidencias, y resuelve qué crosswalk temporal puede establecerse sin inventar campos ni colapsar relojes.

**Conclusión principal:** no hay una alternativa única que sea hoy plenamente suficiente, compatible con todas las decisiones vigentes y lista para aceptación. La comparación distingue:
- afirmaciones de estado sobre una revisión exacta de NODE;
- ocurrencias runtime individuales (carga, invocación, ejecución);
- afirmaciones/evidencias y evaluaciones;
- timestamps de ocurrencia, emisión, captura, observación, registro y snapshot.

La alternativa A (identidad claim-level sobre CLAIM_EVIDENCE_LINK) es la extensión más transversal para claims de estado, pero no crea por sí misma un registro normalizado de ocurrencias. La alternativa B (PREDICATE especializado) es reutilizable para afirmaciones ligadas a ruta/paso/tiempo, pero no es una representación general de lifecycle de NODE y requiere ampliar un catálogo semántico cerrado. La alternativa C (estado NODE + ocurrencia PROCESS_EVENT) es la separación ontológica más clara para eventos individuales, pero requiere aceptar/materializar Opción B de Gate 98, resolver el destino de evidencia frente a DEC-C10-061 y formalizar los campos de estado de NODE; no es actualmente autorizable.

**Matiz correctivo sobre Gate 105:** no es correcto afirmar que las evaluaciones/adjudicaciones carecen por completo de vínculo con CLAIM_EVIDENCE_LINK. U_G Protocol §15 y Template §15.4 permiten que cada CLAIM_EVIDENCE_LINK apunte opcionalmente a evaluator_record_id y adjudication_id. La carencia es más precisa: no existe una identidad independiente/versionada de la afirmación, ni una restricción que garantice agrupación y evaluación unívocas de múltiples evidencias para la misma afirmación. EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER siguen teniendo como target un objeto tipado, no un claim_id autónomo. Gate 105 queda cualificado en este punto; no se invalida su diagnóstico de necesidad de mayor precisión claim-level.

**Resultado:** GATE_106_ALTERNATIVES_COMPARED / CLAIM_EVIDENCE_LINK_HAS_EVALUATOR_AND_ADJUDICATION_REFERENCES / STABLE_CLAIM_IDENTITY_NOT_DEFINED / PREDICATE_SPECIALIZATION_NOT_GENERAL / PROCESS_EVENT_PATH_NOT_ACCEPTED / NO_SINGLE_OPTION_SELECTED / TEMPORAL_ROLES_NON_INTERCHANGEABLE / CLOCK_CROSSWALK_OPEN / C0_UNCHANGED / NO_SCHEMA_CHANGE / NO_IMPLEMENTATION / NO_EXECUTION / NO_FREEZE.

## 2. Reconstrucción histórica obligatoria

### 2.1. Gate 103 — suficiencia conceptual condicionada

Gate 103 concluyó que el modelo U_G puede registrar las principales clases de afirmación y procedencia sin crear tablas paralelas ni ampliar el esquema en ese momento. También declaró explícitamente:
- las seis dimensiones lifecycle están contempladas conceptualmente en NODE;
- CLAIM_EVIDENCE_LINK enlaza afirmaciones con fuentes y destinos tipados;
- EVALUATOR_ASSESSMENT/ADJUDICATION_REGISTER conservan evaluación E1/E2 y adjudicación;
- los gaps de Gate 103 son de evidencia, observabilidad, cobertura, definición o validación y no justifican por sí solos un cambio de esquema.

Ese dictamen es **suficiencia conceptual condicional**, no una demostración de que toda afirmación lifecycle tenga identidad claim-level estructurada o que cada ocurrencia runtime pueda almacenarse como registro consultable.

### 2.2. Gate 105 — precisión que se incorpora

Gate 105 identificó correctamente que:
- claim_statement y relevance_scope son texto, no identidad de claim tipada/versionada;
- claim_evidence_id identifica una relación claim-evidence, no necesariamente una afirmación estable compartida por varias evidencias;
- los seis destinos tipados de DEC-C10-061 no incluyen PROCESS_EVENT;
- el encabezado NODE tiene observed_state genérico y no seis atributos lifecycle independientes;
- PREDICATE tiene un catálogo y semántica existentes que no deben reutilizarse por parecido verbal.

Se precisa, no obstante, que Template §15.4 define FKs opcionales evaluator_record_id y adjudication_id en CLAIM_EVIDENCE_LINK. Por ello, existe una ruta relacional desde la evidencia/afirmación enlazada hacia las evaluaciones/adjudicaciones. Lo que no queda impuesto por el esquema es que una evaluación corresponda a exactamente una afirmación, que varias evidencias compartan una identidad de claim estable o que el target de la evaluación sea la afirmación y no el objeto al que esta se refiere.

### 2.3. Gate 98 y decisiones que limitan alternativas

- Gate 98 mantiene PROCESS_EVENT como contrato lógico candidato, con Opción B todavía no aceptada.
- Gate 98 §9 mantiene DEC-C10-061 intacta: los destinos directos de CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER son NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT y COVERAGE_SCOPE.
- Gate 98 §10 retira el binding libre de cobertura de eventos; eventos sin snapshot compatible siguen no representables bajo C0/DEC-C10-070.
- DEC-C10-065 exige pinning exacto de snapshot.
- DEC-C10-067 fija la semántica material de B_g0/B_g1, pero no autoriza redefinir eventos runtime ni extender destinos de evidencia.
- DEC-C10-071/083/088 mantienen separados stage_key, DGP time, SNAPSHOT.phase, reloj y adjudicación.

Ninguna alternativa puede resolver una carencia debilitando estos límites.

## 3. Requisitos de comparación

Toda alternativa debe conservar:

1. Identidad semántica de NODE y revisión exacta (node_id, object_record_id, object_version).
2. Pinning compuesto SNAPSHOT exacto conforme DEC-C10-065.
3. Distinción de las seis dimensiones sin inferir una a partir de otra.
4. Diferencia entre afirmación de estado y ocurrencia individual con multiplicidad.
5. Vínculo 0..n de evidencias, procedencia en EVIDENCE_REGISTER y alcance compatible.
6. Evaluaciones E1/E2 independientes, regla versionada, discrepancias y adjudicación, incluida posición minoritaria.
7. Estados observados 1/0/? separados de evidence_status y coverage_status; ningún 0 sin cobertura negativa suficiente.
8. Firewall Generator truth / Analyzer evidence / Evaluator truth.
9. Tiempo y reloj explícitos; no ordenar registros ni calcular lag sin comparabilidad defendible.
10. DEC-C10-061/070 intactas salvo una decisión expresa posterior.

## 4. Alternativa A — CLAIM_EVIDENCE_LINK enriquecido con identidad claim-level

### 4.1. Representación

Conservar la arquitectura actual de destinos tipados y la relación 1:N de CLAIM_EVIDENCE_LINK. Añadir, como propuesta de diseño y no como campos aprobados:
- identidad estable de afirmación (claim_id);
- tipo/dimensión de afirmación (claim_type o vocabulario equivalente);
- revisión de definición (claim_revision);
- naturaleza (STATE / OCCURRENCE);
- alcance temporal y contextual con semántica explícita;
- referencia inequívoca al target tipado y a su revisión exacta.

Una afirmación puede tener varias evidencias: cada evidencia conserva su fila CLAIM_EVIDENCE_LINK y todas las filas remiten al mismo claim_id/revisión. Las evaluaciones E1/E2 y adjudicación deberían poder referirse al mismo claim_id/revisión, no inferirse únicamente de texto o de la identidad del objeto.

### 4.2. Ventajas

- Reutiliza la relación probatoria canónica y los seis destinos tipados actuales.
- Conserva evidencia múltiple sin duplicar EVIDENCE_REGISTER.
- Permite identificar y versionar una afirmación separadamente de cada fuente.
- Es extensible a DECLARED, INSTALLED, DEPLOYED y claims sobre observaciones runtime, siempre que el target permitido sea semánticamente adecuado.
- No obliga a crear un nuevo registro de cobertura ni altera C0.

### 4.3. Límites

- Si el claim trata una ocurrencia individual (INVOCATION/EXECUTION), el target NODE identifica el componente, no la ocurrencia. claim_statement/relevance_scope y el artefacto fuente podrían localizar el episodio, pero no proporcionan por sí solos un event_id normalizado ni cardinalidad de relaciones entre ocurrencias.
- CLAIM_EVIDENCE_LINK no sustituye PROCESS_EVENT si se necesita ordenar, correlacionar, deduplicar o relacionar ocurrencias individuales.
- Añadir claim_id/type/revision y cambiar el target de EVALUATOR_ASSESSMENT/ADJUDICATION_REGISTER requiere reconciliación del contrato físico y de DEC-C10-061; no se puede declarar que sea solo una convención textual.
- Un claim_id no debe confundirse con claim_evidence_id, evidence_id, object_record_id ni event_id.

**Dictamen A:** mejor base transversal para identidad de afirmaciones; no suficiente por sí sola para modelar ocurrencias runtime como entidades consultables. **No aceptada; extensión no autorizada.**

## 5. Alternativa B — especialización de PREDICATE

### 5.1. Representación

Representar dimensiones lifecycle como predicados tipados y versionados, aprovechando predicate_id, predicate_type, observed_state, ruta/paso/tiempo/snapshot y el destino PREDICATE ya admitido por DEC-C10-061.

### 5.2. Ventajas

- PREDICATE ya posee identidad/revisión de objeto y observed_state 1/0/?.
- CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER ya admiten PREDICATE como destino.
- Es apropiado cuando la afirmación es realmente una condición evaluable de una ruta/paso/tiempo, con regla y efecto analítico explícitos.
- Puede preservar evidencia múltiple y adjudicación bajo el esquema actual.

### 5.3. Límites

- El catálogo de predicate_type es cerrado en la plantilla: ID/REL/COND/AUTH/RES/DEP/BLOCK/APP/ALT/ORACLE/EXT. No hay una familia lifecycle aceptada.
- PREDICATE está contextualizado por ruta/paso/tiempo y por sus efectos sobre A_f*/App/Reach/F_alt/IV. No toda afirmación DECLARED/INSTALLED/DEPLOYED de un NODE pertenece a una ruta.
- La tabla PREDICATE no es un registro genérico de eventos runtime. Invocaciones y ejecuciones múltiples no deben convertirse en una fila de predicado que pierda event_id, actor, multiplicidad, correlación y resultado.
- Añadir una familia lifecycle exige demostrar que no cambia el significado de las familias existentes, y que el binding a NODE/EDGE exacto es posible sin inventar target ni scope.
- La especialización podría duplicar una misma afirmación entre NODE y PREDICATE y producir dos observed_state no reconciliados si no se fija cuál es autoritativo.

**Dictamen B:** opción reutilizable solo para lifecycle claims que sean genuinamente predicados de ruta/paso/tiempo. No es solución general ni se aprueba la ampliación del catálogo. **No aceptada.**

## 6. Alternativa C — estados de NODE y ocurrencias PROCESS_EVENT

### 6.1. Representación

Separar:
- afirmaciones de estado sobre la revisión exacta de NODE (principalmente DECLARED, INSTALLED, DEPLOYED y LOADED cuando se defina como estado en ventana);
- ocurrencias individuales en PROCESS_EVENT (LOAD, INVOKE, EXECUTE u otros actos solo si el DGP/fuente los identifica y el catálogo se acepta).

Las ocurrencias deben tener identidad/revisión propia, target exacto, tiempo/intervalo, fuente, unidad/contexto, correlación y relaciones causales/temporales justificadas. Una invocación no demuestra ejecución completada; una ejecución no demuestra éxito funcional.

### 6.2. Ventajas

- Respeta la diferencia ontológica entre estado de objeto y ocurrencia.
- Preserva multiplicidad, orden, actor, resultado, reintentos y correlación.
- Permite enlazar una ocurrencia con NODE exacto sin crear un NODE artificial para cada evento.
- Es la opción más natural si el análisis necesita consultar eventos individuales y no solo claims sobre ellos.

### 6.3. Bloqueos

- PROCESS_EVENT Gate 98 sigue como Opción B no aceptada/no materializada.
- Su catálogo no contiene todavía una familia general de LOAD/INVOKE/EXECUTE runtime.
- DEC-C10-061 no admite PROCESS_EVENT como destino directo de CLAIM_EVIDENCE_LINK/EVALUATOR_ASSESSMENT/ADJUDICATION_REGISTER. Gate 98 exige decisión expresa para el camino directo; el indirecto solo es válido si PREDICATE u otro destino permitido representa exactamente la proposición y se vincula inequívocamente al event_record_id.
- NODE no tiene seis campos tipados; §12.7 declara intención conceptual, no el contrato físico.
- El mapping entre event_record_id, evidencia S3, NODE exacto, snapshot, cobertura y reloj sigue sin resolverse completamente.
- C0/DEC-C10-070 no se puede debilitar para cubrir eventos que no tengan snapshot compatible.

**Dictamen C:** mejor separación para ocurrencias individuales, pero la alternativa está bloqueada por decisiones y contratos pendientes. **No aceptada; no implementable.**

## 7. Matriz comparativa

| Criterio | A. CLAIM_EVIDENCE_LINK enriquecido | B. PREDICATE especializado | C. NODE + PROCESS_EVENT |
|---|---|---|---|
| Identidad de afirmación estable | Sí, si se incorpora claim_id/version | Predicate ID/revisión, solo para predicados | Parcial; claim de estado y event_id separados |
| Evidencia múltiple | Nativa 1:N | Nativa vía CLAIM_EVIDENCE_LINK | Requiere camino de evidencia aprobado |
| E1/E2 por afirmación | Requiere binding explícito a claim_id | Disponible para PREDICATE exacto | Requiere destino PROCESS_EVENT o ruta indirecta válida |
| DECLARED/INSTALLED/DEPLOYED | Adecuada | Solo si predicado contextualizado | Adecuada tras formalizar campos/claims NODE |
| LOADED | Claim de estado posible | Condicional a ruta/tiempo | Estado o evento según definición |
| INVOKED/EXECUTED múltiples | No como entidades normalizadas | No como entidades normalizadas | Adecuada con catálogo y bindings aprobados |
| Tiempo/ventana | Debe tiparse en claim | Ya tiene contexto temporal, pero ruta-bound | Event time/interval y record time; clock mapping abierto |
| Compatibilidad DEC-C10-061 | Mantiene targets; cambia identidad/evaluación | PREDICATE ya es target permitido; catálogo requiere cambio | Requiere resolver nuevo target PROCESS_EVENT |
| Compatibilidad C0 | Puede preservar C0 | Puede preservar C0 | No resuelve eventos sin snapshot; C0 intacto |
| Cambios de esquema | Sí, claim-level | Sí, catálogo/posible binding | Sí, NODE + PROCESS_EVENT + target evidence |
| Riesgo de duplicación | Claim/evidence/target si no se separan IDs | Doble representación NODE/PREDICATE | Doble estado/evento si no se define autoridad |
| Adecuación global | Media-alta para claims | Parcial y contextual | Alta para eventos, dependiente de aceptación |

**Control de baseline:** el esquema U_G actual sin extensión es suficiente para registrar documentalmente múltiples afirmaciones/evidencias y estados observados en los objetos permitidos, conforme Gate 103. No se demuestra que garantice identidad versionada de cada afirmación ni que normalice ocurrencias runtime. Su uso provisional es admisible solo cuando la afirmación pueda localizarse inequívocamente mediante target exacto, claim_statement, relevance_scope, evidence_id y vínculos de evaluación/adjudicación; si no, el resultado debe permanecer OPEN/UNKNOWN, no completarse por convención tácita.

## 8. Dictamen de representación y decisión de no selección

No se selecciona A, B o C como diseño canónico en Gate 106. La selección prematura introduciría al menos uno de estos errores:
- tratar una fila claim-evidence como identidad estable de la afirmación;
- convertir cualquier lifecycle claim en PREDICATE aunque no sea una condición de ruta;
- tratar INVOKED/EXECUTED como propiedades persistentes de NODE;
- materializar PROCESS_EVENT antes de aceptar Opción B y resolver DEC-C10-061;
- inferir cobertura de evento a partir de snapshot no compatible o debilitar C0.

**Regla provisional de uso documental (sin cambio de esquema):**
1. DECLARED/INSTALLED/DEPLOYED/LOADED: formular claims explícitos contra NODE exacto cuando exista identidad y scope; enlazar evidencia en CLAIM_EVIDENCE_LINK; preservar 1/0/? y cobertura por dimensión. No reutilizar un único observed_state global para seis dimensiones.
2. INVOKED/EXECUTED: conservar evidencia S3 original y su localizador/provenance; no fabricar filas PROCESS_EVENT ni codificar multiplicidad en NODE. CLAIM_EVIDENCE_LINK a NODE solo puede respaldar un claim sobre el componente y una ocurrencia identificada en la fuente, no sustituye un registro normalizado del evento.
3. PREDICATE: utilizar solo para condiciones de ruta/paso/tiempo ya pertenecientes a su semántica y catálogo vigente.
4. Si no puede distinguirse una afirmación o episodio, mantener ?/OPEN y registrar la limitación.

Esta regla es de no-confusión y no constituye aprobación de captura, schema freeze ni autorización de inventario.

## 9. Crosswalk temporal mínimo S3 → registros existentes

### 9.1. Roles que deben permanecer separados

| Rol temporal | Semántica | Artefacto/campo relacionado | Regla |
|---|---|---|---|
| event_time | Tiempo atribuido a la ocurrencia real por la fuente/DGP | PROCESS_EVENT.event_time o event_start_time/event_end_time; timestamp de evento en LOG_TRACE_EVENT | Ocurrencia, no emisión ni captura |
| emission_time | Momento en que el productor emite el registro/señal | Metadata del registro/log S3 | No se asume igual a event_time |
| capture_time | Momento en que el colector recibe/captura el registro | Metadata del canal S3; usado en métrica capture_time−event_time | No se asume igual a observed_at |
| observed_at | Momento de observación/adquisición que se atribuye al expediente de evidencia | Concepto referido por Gate 98; no existe columna literal en EVIDENCE_REGISTER §12.1 | Mapping a capture_time solo si método y fuente lo definen como el mismo instante |
| EVIDENCE_REGISTER.timestamp_start/end_tz | Ventana temporal cubierta/representada por la evidencia | Campos actuales EVIDENCE_REGISTER | No reinterpretar como capture_time ni como event_time |
| recorded_at | Momento en que se registra una revisión de PROCESS_EVENT | PROCESS_EVENT.recorded_at | Tiempo de persistencia del registro, no del acto |
| SNAPSHOT.timestamp | Tiempo de captura del estado estructural versionado | SNAPSHOT.timestamp | No equivale automáticamente a evento, emisión, captura S3 u observación |

### 9.2. Crosswalk de registro sin añadir campos

- EVIDENCE_REGISTER identifica fuente/artefacto, custodio, método, scope, integridad, lineage, limitaciones y ventana timestamp_start/end_tz.
- Los timestamps internos de LOG_TRACE_EVENT y su semántica (ocurrencia/emisión/captura) permanecen en el artefacto fuente y deben documentarse mediante localizador exacto, versión y método en el expediente de evidencia. No se proyectan a columnas inexistentes.
- PROCESS_EVENT conserva event_time/intervalo y recorded_at solo si Opción B se acepta y el evento satisface su catálogo/contrato. Gate 98 no recibe por inferencia nuevos tipos runtime.
- SNAPSHOT.timestamp se conserva como tiempo de snapshot. La relación de un evento con snapshot requiere binding explícito exacto conforme DEC-C10-065; proximidad temporal no crea binding.
- observed_at permanece concepto no materializado hasta que se decida si representa captura por colector, observación manual u otro momento. No se rellena con timestamp_start, capture_time o recorded_at por analogía.

### 9.3. Metadatos necesarios para comparar relojes

Antes de ordenar tiempos de registros distintos o estimar lag, la fuente/método debe identificar, cuando corresponda:
- clock domain del productor, colector, runtime, DGP y snapshot;
- semántica wall-clock/monotonic y origen del timestamp;
- zona/offset y preservación del valor original;
- resolución/precisión y redondeo;
- método/estado de sincronización, offset y deriva;
- incertidumbre o bound de error por reloj/intervalo;
- buffering, transporte, reordenamiento, pérdida y duplicación;
- versión del mecanismo de captura y de la metadata de reloj.

PROCESS_EVENT propone clock_domain_id y clock_uncertainty opcionales; no existe todavía contrato común que los armonice con EVIDENCE_REGISTER y SNAPSHOT. Estos elementos son requisitos semánticos para una comparación válida, no campos aceptados ni una nueva tabla de relojes.

**Regla:** si los relojes no son comparables o sus errores no permiten ordenar intervalos, no afirmar PRECEDES ni calcular capture_time−event_time como lag identificable. Se informa UNKNOWN/BOUNDS/NOT_COMPARABLE según el contrato aplicable. CAUSES nunca se deriva de precedencia. recorded_at solo ordena incorporación al registro.

### 9.4. Ejes que no son relojes de captura

Se mantienen separados:
- dgp_time_key y t−1…t9;
- stage_key aceptado por DEC-C10-071 y su aplicabilidad DEC-C10-083;
- SNAPSHOT.phase y SNAPSHOT.timestamp;
- profundidad transformacional k=1…H;
- route_id/step y event_type.

Ninguno se deriva del otro por nombre, orden, timestamp o proximidad. DEC-C10-088 prevalece.

## 10. Riesgos adversariales y condiciones de rechazo

| Caso | Inferencia inválida | Resultado exigido |
|---|---|---|
| Log emitido tarde para una ocurrencia anterior | emission_time = event_time | Conservar ambos roles; UNKNOWN si no hay source event time |
| Colector con reloj desfasado | capture_time − event_time es lag real | NOT_COMPARABLE/BOUNDS hasta calibración |
| Snapshot posterior a evento | SNAPSHOT.timestamp prueba el evento | No; snapshot solo captura estado |
| recorded_at posterior | El acto ocurrió al persistir registro | No; record-time no es event-time |
| Sin log de INVOKE | No hubo invocación | ? salvo cobertura negativa S3 adecuada |
| Varias trazas del mismo acto | Son eventos independientes | Deduplicar solo con identidad/correlación y regla versionada |
| Una invocación sin resultado | EXECUTED=1 | No; invocación no prueba ejecución |
| Ejecución con error | EXECUTED=0 | No necesariamente; ejecución y éxito son dimensiones distintas |
| E1/E2 coinciden sobre NODE | Todas las seis dimensiones están adjudicadas | No; evaluación debe tener scope/claim exacto |
| claim_evidence_id único | Identidad estable del claim con múltiples evidencias | No; identifica relación claim-evidence |
| Evento sin snapshot | Asignar scope C0 genérico | Prohibido; DEC-C10-070 intacta |

## 11. Gaps y estado tras Gate 106

| ID | Gap | Estado |
|---|---|---|
| G106-01 | Identidad estable/versionada de claim separada de claim-evidence | OPEN |
| G106-02 | Cardinalidad inequívoca claim↔evidence↔E1/E2↔adjudication | PARCIALMENTE REPRESENTABLE; restricciones de asociación no cerradas |
| G106-03 | Claims de estado lifecycle en NODE con seis observed_state separados | CONCEPTUALMENTE PRESENTES; estructura tipada no especificada |
| G106-04 | PREDICATE como familia lifecycle general | NO JUSTIFICADO; solo ruta/paso/tiempo cuando semántica encaje |
| G106-05 | PROCESS_EVENT runtime LOAD/INVOKE/EXECUTE | NO ACEPTADO; Opción B y catálogo abiertos |
| G106-06 | PROCESS_EVENT como destino de evidencia/adjudicación | OPEN bajo DEC-C10-061; camino indirecto requiere equivalencia exacta |
| G106-07 | observed_at en EVIDENCE_REGISTER | CONCEPTO REFERIDO; campo físico no localizado |
| G106-08 | Capture/emission/source timestamps crosswalk | DEFINIDO SEMÁNTICAMENTE; mapping por fuente pendiente |
| G106-09 | Clock domains/precision/uncertainty comunes | OPEN |
| G106-10 | SNAPSHOT.timestamp ↔ S3 capture | NO EQUIVALENCIA AUTOMÁTICA |
| G106-11 | C0 para eventos sin snapshot | BLOQUEO VIGENTE; DEC-C10-070 intacta |
| G106-12 | S3 detectability, lag, loss, duplicate, disorder y calibration | CONTRATO ESTRUCTURAL EXISTENTE; CALIBRACIÓN NUMÉRICA/EMPÍRICA OPEN |

## 12. Decisiones y continuidad

1. No seleccionar A/B/C ni combinar extensiones en un diseño canónico en Gate 106.
2. Reconocer que CLAIM_EVIDENCE_LINK sí puede referenciar evaluator_record_id/adjudication_id; corregir la lectura absoluta de Gate 105.
3. Mantener la distinción claim_id ≠ claim_evidence_id ≠ evidence_id ≠ object_record_id ≠ event_id.
4. No ampliar el catálogo PREDICATE ni el catálogo PROCESS_EVENT.
5. No aceptar Opción B de Gate 98 ni añadir PROCESS_EVENT a DEC-C10-061.
6. No añadir campos a EVIDENCE_REGISTER ni reinterpretar timestamp_start/end_tz.
7. Mantener C0/DEC-C10-070, DEC-C10-065, DEC-C10-071/083/088 y DEC-C10-061 sin cambios.
8. Mantener el baseline actual para registro documental cuando el target/claim/scope sean inequívocos; cualquier insuficiencia mantiene OPEN/? y no autoriza extensión automática.

**Siguiente operación recomendada — Gate 107:** resolver exclusivamente el contrato de identidad y granularidad de afirmación lifecycle: si la semántica puede cerrarse con convenciones verificables sobre CLAIM_EVIDENCE_LINK + EVALUATOR_ASSESSMENT + ADJUDICATION_REGISTER, o si necesita claim_id/type/revision y evaluación directa por claim. Separar dos subcasos: (i) afirmaciones de estado sobre NODE y (ii) ocurrencias INVOKED/EXECUTED que requieren event identity. Incluir crosswalk de NODE exacto, snapshot y scope; no abrir todavía DDL. El camino PROCESS_EVENT/DEC-C10-061 debe decidirse solo si la granularidad de ocurrencia resulta necesaria para el estimando/análisis.

## 13. Límites y control

Auditoría documental asistida, no revisión independiente. No se inspeccionaron runtime, logs reales, snapshots, fuentes externas ni artefactos de ejecución. No se generaron claims, eventos, evidencias, evaluaciones o adjudicaciones. No se ejecutaron parsers, constraints, tests, workflows, simulaciones, calibraciones ni experimentos.

scientific_execution=false; execution_authorized=false.

**Dictamen final:** GATE_106_ALTERNATIVES_COMPARED / CLAIM_EVIDENCE_LINK_RELATIONSHIP_CAPABILITY_QUALIFIED / STABLE_CLAIM_IDENTITY_OPEN / PREDICATE_SPECIALIZATION_CONTEXTUAL_ONLY / PROCESS_EVENT_PATH_NOT_ACCEPTED / NO_SINGLE_OPTION_SELECTED / TEMPORAL_ROLES_NON_INTERCHANGEABLE / CLOCK_CROSSWALK_OPEN / C0_UNCHANGED / NO_DECISION_AMENDMENT / NO_SCHEMA_CHANGE / NO_CODE_CHANGE / NO_EXECUTION / NO_DESIGN_FREEZE.
