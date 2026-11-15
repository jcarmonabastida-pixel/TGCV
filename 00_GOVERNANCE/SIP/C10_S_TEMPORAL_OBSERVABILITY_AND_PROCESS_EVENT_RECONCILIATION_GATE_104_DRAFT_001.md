# C10-S — Gate 104: reconciliación de observabilidad temporal y eventos de proceso

**Estado:** DOCUMENTARY TEMPORAL RECONCILIATION / FOUR EVENT-TIME ROLES PRESERVED / AXIS SEPARATION CONSISTENT / NODE LIFECYCLE REPRESENTATION NOT ESTABLISHED / CLOCK-CAPTURE CROSSWALK OPEN / NO SCHEMA CHANGE / NO IMPLEMENTATION / NO EXECUTION / NO FREEZE  
**Fecha:** 2026-11-15  
**Rama:** research/c10-s-consolidation-draft · PR #116 Draft  
**Precedencia:** DEC-C10-065, DEC-C10-070, DEC-C10-071, DEC-C10-083, DEC-C10-088; Gates 93–103, especialmente Gate 98; DGP Temporal and Role Contract; U_G Inventory Register Template; U_G Evidence/Provenance and Adjudication Protocol; Transformational Snapshot and Delta Reconciliation; Temporal Horizon and S4R Integration Audit.

---

## 1. Objetivo y dictamen ejecutivo

Auditar si las observaciones S3, los eventos PROCESS_EVENT candidatos, el ciclo de vida de NODE, SNAPSHOT y los ejes temporales DGP/stage pueden alinearse sin colapsar relojes, inventar ocurrencias, inferir causalidad por precedencia ni debilitar C0.

**Dictamen principal:**
1. El contrato temporal de eventos conserva cuatro roles temporales independientes: scheduled_time, event_time (o intervalo event_start_time/event_end_time), observed_at y recorded_at. El intervalo start/end es una representación de duración del segundo rol, no un quinto reloj.
2. SNAPSHOT.timestamp y capture_time del protocolo S3 son tiempos adicionales de captura que requieren mapping semántico explícito; no deben igualarse automáticamente a observed_at ni a recorded_at.
3. stage_key, dgp_time_key/t−1…t9, SNAPSHOT.phase/timestamp y k=1…H son ejes distintos. DEC-C10-071, DEC-C10-083 y DEC-C10-088 son compatibles si se aplican sin inferencias por nombre, orden o timestamp.
4. La plantilla NODE no contiene seis estados de lifecycle explícitos ni un crosswalk aprobado para representarlos. Gate 103 confundió la distinción conceptual de estados con su representación canónica. Este punto queda corregido/condicionado por Gate 104.
5. El contrato de relojes/captura no permite todavía comparar universalmente event_time con capture_time/observed_at: la metadata de clock domain, incertidumbre y sincronización no está armonizada entre PROCESS_EVENT, EVIDENCE_REGISTER y SNAPSHOT.
6. No se identifica una razón para modificar ahora DEC-C10-065/070/071/083/088. Tampoco se autoriza crear columnas, tablas, eventos ni telemetría.

**Dictamen:** GATE_104_TEMPORAL_AXIS_SEPARATION_DOCUMENTARILY_CONSISTENT / FOUR_EVENT_TIME_ROLES_RETAINED / SNAPSHOT_AND_S3_CAPTURE_CROSSWALK_OPEN / NODE_LIFECYCLE_REPRESENTATION_NOT_ESTABLISHED / NO_DECISION_AMENDMENT / NO_SCHEMA_CHANGE / NO_IMPLEMENTATION / NO_EXECUTION / NO_FREEZE.

## 2. Fuentes recuperadas y precedencia

| Fuente | Contenido relevante | Disposición |
|---|---|---|
| Gate 98 successor Draft 002 §§4, 7–12 | PROCESS_EVENT fields, bindings, snapshots, four time roles, DGP/stage/phase/depth | Contrato lógico candidato; no aceptado ni implementado |
| Gate 96 §4/temporal rules | Define explícitamente los cuatro roles scheduled/event/observed/recorded | Antecedente preservado; Gate 98 successor gobierna correcciones |
| DGP Temporal and Role Contract §§2–4, 23–24 | t−1, t0…t9 y secuencia causal/analítica | DRAFT; no equivale a duración física |
| DEC-C10-071 | Siete valores exactos de stage_key; separación respecto a DGP, phase y timestamp | ACCEPTED documental |
| DEC-C10-083 | Aplicabilidad PAR-SVC-ENABLED/PROFILE en siete stages | ACCEPTED documental; no crea observaciones |
| DEC-C10-088 | Integración F/A y ejes temporales; prohibición de inferir mapping | ACCEPTED documental |
| DEC-C10-065 | FK compuesta exacta a SNAPSHOT | ACCEPTED documental; no matching por timestamp |
| DEC-C10-070 | Tupla C0 exacta y binding condicionado a snapshot/stage/route/object_class | ACCEPTED documental; cobertura de eventos sin snapshot no resuelta |
| U_G Inventory Register Template §§2, 6, 12 | NODE observed_state; SNAPSHOT phase/timestamp; EVIDENCE_REGISTER timestamp_start/end_tz | Plantilla Draft, vacía |
| U_G Evidence/Provenance Protocol §§3–6, 19–23 | S1–S8, captura, límites, trivalent evidence and coverage | Protocolo documental; sin fuentes reales |
| Temporal Horizon and S4R Integration Audit §§17–18 | S3 pasivo, capture_time−event_time, lag, pérdida, detección, censura | Cierre estructural; calibración numérica abierta |
| Gate 103 | Modelo U_G y observabilidad | Se conserva histórico; su afirmación sobre NODE lifecycle queda cualificada por este gate |

## 3. Reconciliación de los cuatro roles temporales del evento

La semántica heredada de Gate 96 y preservada por Gate 98 es:

| Rol | Campo/ubicación | Qué responde | Qué no significa |
|---|---|---|---|
| 1. Programación | PROCESS_EVENT.scheduled_time | ¿Cuándo estaba previsto el acto? | No prueba que ocurriera |
| 2. Ocurrencia | PROCESS_EVENT.event_time o event_start_time + event_end_time | ¿Cuándo ocurrió según la fuente? | No es captura ni incorporación al registro |
| 3. Observación/captura | EVIDENCE_REGISTER.observed_at (con timestamp_start/end_tz en la plantilla) | ¿Cuándo la fuente observó/capturó el hecho? | No sustituye el tiempo de ocurrencia |
| 4. Registro | PROCESS_EVENT.recorded_at | ¿Cuándo se incorporó esta revisión al registro? | No es tiempo del evento ni necesariamente el de captura |

### 3.1 Event time puntual o intervalar

- event_time representa el instante atribuido por la fuente.
- event_start_time/event_end_time representan un intervalo y deben aparecer ambos o ninguno.
- La regla end >= start solo es evaluable con relojes comparables.
- El contrato no cierra si event_time puede coexistir con start/end ni qué semántica tendría en ese caso. No se debe asumir que es el inicio, centro o fin del intervalo.
- scheduled_time es independiente; un evento reprogramado o tardío conserva la diferencia entre previsión y ocurrencia.
- Si la fuente no puede determinar event_time, se conserva NULL/indeterminado; no se copia observed_at.

### 3.2 Captura S3 y observed_at

El contrato S3 define capture_time−event_time para caracterizar retardo de captura/localización. Gate 98 sitúa observed_at en EVIDENCE_REGISTER y excluye su duplicación en PROCESS_EVENT.

**Correspondencia admisible solo como hipótesis de crosswalk:** capture_time podría ser el instante de captura/observación de la evidencia que se registra como observed_at, si la definición del método S3, la fuente y el timestamp lo demuestran. No es equivalencia aprobada en general.

Deben distinguirse:
- tiempo de emisión de la señal por el emisor;
- tiempo de captura/recepción por el colector;
- timestamp contenido en el artefacto fuente;
- observed_at adjudicado al expediente de evidencia;
- recorded_at de la revisión del evento.

La existencia de varios timestamps en un log no permite seleccionar uno por conveniencia. La regla de extracción debe fijar campo fuente, semántica, precisión, zona/offset, reloj y método. Si no se conoce, la localización temporal es ? y no se calcula lag puntual.

### 3.3 Registro tardío y correcciones

Una ocurrencia puede suceder, ser observada y registrarse después. Una corrección crea nueva event_revision con recorded_at propio; no reescribe event_time ni observed_at históricos. Nueva evidencia no crea por sí sola una nueva ocurrencia o revisión. La relación entre revisiones sigue el contrato append-only candidato de Gate 98.

## 4. SNAPSHOT: timestamp y binding contextual

La plantilla U_G define SNAPSHOT con snapshot_id y object_record_id; unit_id y unit_object_record_id; phase; timestamp; scope, source_artifacts, version/hash, method y coverage limitations; evidencia/procedencia según los registros vinculados.

DEC-C10-065 exige la referencia compuesta exacta (snapshot_id, snapshot_object_record_id) a SNAPSHOT(snapshot_id, object_record_id). Por tanto:

1. No se vincula un evento a un snapshot por proximidad temporal, timestamp, unit_id aislado o latest version.
2. PROCESS_EVENT_SNAPSHOT_BINDING (si se acepta en el futuro) puede expresar BEFORE / AFTER / CONTEXT / ROLLBACK_STATE con la revisión exacta.
3. BEFORE/AFTER es papel contextual adjudicado; no prueba que el evento causara el cambio observado.
4. Un evento puede existir sin snapshot asociado. La ausencia de snapshot no niega la ocurrencia.
5. SNAPSHOT.timestamp es instante efectivo de captura del snapshot; no es event_time, scheduled_time ni recorded_at.
6. SNAPSHOT.phase conserva únicamente su vocabulario existente: baseline / post-B / rollback / route-test. No se extiende con los siete stage_key.
7. El snapshot puede cubrir un estado estructural, pero no acredita automáticamente que el log/runtime de todo el intervalo esté capturado.

La correspondencia entre SNAPSHOT.timestamp y observed_at debe documentar si son la misma captura y misma fuente o si uno es la adquisición del snapshot y el otro el registro de evidencia. No se presupone igualdad.

## 5. Ejes temporales y de secuencia: crosswalk sin colapso

| Eje | Vocabulario | Función | Regla |
|---|---|---|---|
| Tiempo causal/analítico DGP | t−1, t0…t9 | Ordena roles y etapas del DGP | No expresa por sí solo duración física |
| Clave temporal DGP | dgp_time_key | Etiqueta contractual versionada de tiempo/rol DGP | No se deriva automáticamente de timestamp ni stage |
| Etapa de captura/configuración | stage_key | Uno de siete valores DEC-C10-071 | No se deriva del orden de eventos ni de SNAPSHOT.phase |
| Fase de snapshot | SNAPSHOT.phase | Contexto/tipo de captura | No sustituye stage_key ni tiempo DGP |
| Instante de snapshot | SNAPSHOT.timestamp | Captura efectiva de ese snapshot | No identifica por sí solo su stage ni evento |
| Profundidad de ruta | k=1…H | Paso transformacional hipotético | No es reloj, duración, número de evento ni cadencia S3 |
| Ruta/familia | route_id/route_record_id; F/A como metadato auxiliar si procede | Identidad exacta de ruta | F/A no sustituye route_id ni stage_key |
| Reloj fuente | clock_domain_id + incertidumbre cuando exista | Comparabilidad temporal | Sin comparabilidad, no hay orden temporal derivado |

### 5.1 stage_key

DEC-C10-071 acepta exactamente:
- C_SRC
- F1_S2
- A1_S1
- F2_DST_DECL
- A2_DST_DECL
- F2_DST_APPLIED
- A2_DST_APPLIED

DEC-C10-083 establece aplicabilidad de PAR-SVC-ENABLED y PAR-SVC-PROFILE en las siete etapas. La obligación documental no acredita una observación real.

Para eventos, Gate 98 mantiene stage_key opcional y stage_key_status obligatorio (APPLICABLE / NOT_APPLICABLE / UNDETERMINED). No se asigna stage por analogía con event_type, por proximidad a un snapshot o por el orden aparente. El mapping evento↔stage requiere versión, ámbito y fuente contractual.

### 5.2 DGP t−1…t9

El DGP ordena basal, asignación, política/intento, instalación, accesibilidad, Reach, conocimiento, selección/inicio, ejecución, Outcome y Value. Estos tiempos son roles causales/analíticos. El timestamp físico puede ser ausente, tardío, intervalar o no comparable sin alterar por ello la definición del rol DGP.

El mapping dgp_time_key debe seguir el contrato DGP versionado. No se infiere t7 porque un evento se llame EXECUTION, ni t2 porque el tipo sea INSTALLATION. Se requiere crosswalk semántico y temporal explícito.

### 5.3 k=1…H

k cuenta profundidad/paso de ruta transformacional hipotética. No cuenta eventos de provisión, solicitudes, recepción o procesamiento, intervalos de observación, snapshots, tiempo transcurrido ni eventos de selección/ejecución por sí mismos.

La relación de una ocurrencia con un paso k exige identidad de ruta/paso y regla explícita; no se deriva de secuencia temporal.

## 6. Comparabilidad de relojes y suficiencia de metadata

Gate 98 propone en PROCESS_EVENT clock_domain_id y clock_uncertainty. La plantilla U_G para EVIDENCE_REGISTER ofrece timestamp_start/end_tz; SNAPSHOT tiene timestamp. El protocolo exige origen, método, timestamp y limitaciones. El contrato S3 necesita lag, fase, pérdida y localización temporal.

No se ha demostrado un contrato común para:
- identidad/versionado de reloj de emisor, colector, registrador y snapshot;
- sincronización, offset estimado, deriva y precisión;
- unidad y distribución de incertidumbre;
- normalización reversible UTC/original timezone;
- timestamp de emisión frente a captura/recepción;
- reglas de correlación cuando clocks no son comparables;
- pérdida, buffering, duplicación y desorden del canal S3.

**Consecuencia:** el esquema conceptual de PROCESS_EVENT permite registrar parte de la metadata, pero la suficiencia transversal de reloj/captura no está cerrada. No se calcula capture_time−event_time ni se afirma PRECEDES por timestamp cuando faltan reloj comparable y error temporal. Una relación causal independiente puede respaldar una relación, pero no convierte timestamps incomparables en orden temporal medido.

No se añaden ahora campos a EVIDENCE_REGISTER o SNAPSHOT. El gap debe resolverse primero mediante crosswalk de fuente y contrato de medición; después se determina si el modelo existente basta.

## 7. NODE lifecycle: corrección de Gate 103

### 7.1 Hallazgo documental

La tabla NODE de U_G §2 contiene, entre otros:
- identidad/rol/clase/frontera;
- TID/SID/RID y versión/build/hash;
- owner/consumers/dependencies/permissions;
- evidence_ref;
- observed_state (1/0/?);
- coverage_status;
- timestamp y metadatos de revisión/snapshot.

No contiene campos explícitos independientes para declared, installed, deployed, loaded, invoked y executed. Tampoco se ha localizado un crosswalk aprobado que permita tratar observed_state como seis dimensiones de lifecycle.

La búsqueda de las seis etiquetas en la plantilla no encuentra un contrato de lifecycle; su única referencia genérica a lifecycle aparece en un criterio de identidad/frontera, no como definición de estados o campos.

### 7.2 No equivalencias

- observed_state 1/0/? es clasificación de una afirmación/objeto bajo evidencia y cobertura; no identifica por sí mismo cuál de los seis estados se está afirmando.
- NODE declarado en S1 no prueba instalado, desplegado, cargado, invocado o ejecutado.
- Una ocurrencia PROCESS_EVENT puede acreditar un acto observado concreto, no la totalidad del estado lifecycle ni la ausencia de otros actos.
- S3 es evidencia runtime en ventana y alcance; no es una etiqueta lifecycle exhaustiva.
- DEP/PREDICATE y EVALUATOR_ASSESSMENT podrían participar en un crosswalk por afirmación, pero no se ha demostrado que sus tipos/keys actuales representen de forma unívoca los seis estados.
- SNAPSHOT puede acreditar estado dentro de su alcance; no demuestra retrospectivamente toda la historia entre snapshots.

### 7.3 Corrección explícita

La frase de Gate 103 que presentaba el ciclo de vida NODE como ya contemplado por la plantilla queda CUALIFICADA / NO VERIFICADA. Gate 103 distinguió correctamente seis estados conceptuales y sus fuentes, pero atribuyó prematuramente esa separación al modelo NODE.

No se modifica el documento histórico Gate 103 ni se cambia el esquema en Gate 104. El resultado es un gap de representación/crosswalk OPEN, no una prueba de que se necesite una nueva tabla o seis columnas. Primero debe decidirse si los estados se representan como afirmaciones tipadas sobre NODE con evidencia/ventana, mediante predicados existentes, eventos, o combinación; solo si ninguno permite la semántica requerida podrá proponerse extensión mínima.

## 8. Relaciones temporales entre eventos y snapshots

- PRECEDES requiere clocks comparables o evidencia independiente de orden; no se deriva de insertion order, event_id, recorded_at o timestamp ambiguo.
- CAUSES no se infiere de PRECEDES ni de BEFORE/AFTER snapshot binding.
- RETRY_OF requiere acto lógico/clave común y regla de orden; unit_id común no basta.
- No se fuerza orden total entre eventos concurrentes.
- Los eventos sin event_time pueden seguir siendo ocurrencias observadas si otra evidencia acredita el acto; su posición temporal queda indeterminada.
- La falta de evento capturado no crea una fila NOT_OCCURRED ni un 0.
- Un cambio entre snapshots no permite fabricar eventos intermedios ni asignarles stage_key/t DGP retrospectivamente.

## 9. Cobertura, C0 y estados 1/0/?

Se mantiene DEC-C10-070 intacta. Su tupla C0 requiere, entre otros, snapshot exacto, stage_key, route/route_id y object_class, además de universo/denominador versionados.

Gate 98 ya reconoce que la cobertura de eventos puede no ser representable mediante C0 cuando no existe snapshot exacto. Gate 104 confirma:
- no asignar coverage_scope_id libre al evento;
- no crear snapshot ficticio para habilitar C0;
- no declarar cobertura completa de eventos desde un scope estructural;
- no inferir 0 desde ausencia de fila, log o traza;
- si universo temporal, emisores, superficies, retención, sensibilidad de detección o denominador no están cerrados, mantener ?;
- la cobertura de eventos sin snapshot sigue bloqueada/open hasta un gate específico, sin crear EVENT_COVERAGE_REGISTER ni debilitar C0.

La truth DGP y la observación S3 conservan resoluciones separadas. S3 ausente/perdido no cambia truth; el Analyzer puede emitir ?, bounds o abstención.

## 10. Matriz de suficiencia y estado

| Pregunta | Estado | Resultado |
|---|---|---|
| Cuatro roles temporales del evento | RESOLVED DOCUMENTARILY | Gate 96/98 coherentes; preservar los cuatro |
| event_time puntual vs intervalo | PARTIAL / OPEN | Coexistencia y semántica de event_time junto a start/end no cerradas |
| capture_time ↔ observed_at | OPEN | Correspondencia candidata, no aceptada |
| SNAPSHOT.timestamp ↔ captura evidencia | OPEN | No asumir igualdad; mapping por fuente |
| recorded_at de evento/revisión | RESOLVED CONCEPTUALLY | Registro append-only; reloj registrador aún requiere metadata si se compara |
| dgp_time_key ↔ t−1…t9 | OPEN BY VERSIONED CROSSWALK | No derivar por nombre ni timestamp |
| stage_key vocabulary | ACCEPTED | Siete valores exactos DEC-C10-071 |
| event ↔ stage_key | OPEN | Requiere fuente y ámbito contractual |
| stage_key ↔ SNAPSHOT.phase | SEPARATED | Nunca equivalentes |
| stage_key ↔ SNAPSHOT.timestamp | SEPARATED | Timestamp no identifica etapa |
| k ↔ event/time | SEPARATED | k es profundidad transformacional |
| clock domains/uncertainty across records | PARTIAL / OPEN | Metadata no armonizada |
| NODE six-state lifecycle | NOT ESTABLISHED | No fields/crosswalk canonical found |
| PROCESS_EVENT occurrence semantics | LOGICAL DRAFT | Option B not accepted; no implementation |
| PROCESS_EVENT ↔ SNAPSHOT | LOGICAL DRAFT | Exact composite pinning if bound; contextual only |
| S3 detection/lag | STRUCTURALLY SPECIFIED | Numeric calibration and mode selection open |
| Event coverage without snapshot | OPEN / NOT REPRESENTABLE UNDER CURRENT C0 | DEC-C10-070 unchanged |

## 11. Gaps que sobreviven y siguiente gate

**G104-01 — Lifecycle claims:** definir semántica, unidad de afirmación y representación de declared/installed/deployed/loaded/invoked/executed sin colapsar observed_state ni inventar seis columnas.

**G104-02 — Capture timestamp crosswalk:** definir cuándo capture_time de S3 se registra como observed_at, y cómo se distingue de emisión, recepción, timestamp fuente y recorded_at.

**G104-03 — Clock metadata:** determinar si el contrato común de clock_domain, incertidumbre, offset/deriva, precisión y sincronización puede representarse con los campos existentes y referencias a evidencia, o si se justifica una extensión mínima.

**G104-04 — Event interval semantics:** decidir cuándo event_time puntual coexiste con start/end, qué significa y cómo se adjudica si la fuente reporta valores incompatibles.

**G104-05 — DGP mapping:** crosswalk versionado event_type/event_time→dgp_time_key/t−1…t9, sin inferencia por nombre.

**G104-06 — Stage applicability for events:** regla para APPLICABLE/NOT_APPLICABLE/UNDETERMINED, respetando DEC-C10-071/083 y la no equivalencia con SNAPSHOT.phase.

**G104-07 — Snapshot capture relation:** correspondencia de SNAPSHOT.timestamp con captura S3/evidence, manteniendo pinning exacto DEC-C10-065.

**G104-08 — C0 event coverage:** permanece bloqueado para ocurrencias sin snapshot; no resolver aquí ni crear registro paralelo.

**Siguiente operación recomendada — Gate 105:** contrato de representación de afirmaciones lifecycle y crosswalk temporal de captura/reloj. Resolver G104-01…04 primero, reutilizando NODE/PREDICATE/EVALUATOR_ASSESSMENT, EVIDENCE_REGISTER/CLAIM_EVIDENCE_LINK, PROCESS_EVENT candidato y S3. El gate deberá concluir si el esquema existente es suficiente mediante una mapping table documental o si existe una carencia real que requiera propuesta de cambio. No modificar DEC-C10-061/065/070/071/083/088 por analogía; no implementar ni ejecutar.

## 12. Límites y control

Gate 104 es auditoría documental asistida, no revisión independiente. No se inspeccionó runtime, no se capturó telemetría, no se generaron eventos/snapshots, no se ejecutaron parsers, constraints, tests, workflows, simulaciones ni experimentos. No se autorizó la materialización de filas ni la modificación del esquema.

scientific_execution=false; execution_authorized=false.

**Dictamen final:** GATE_104_TEMPORAL_AXIS_SEPARATION_DOCUMENTARILY_CONSISTENT / FOUR_EVENT_TIME_ROLES_RETAINED / NODE_LIFECYCLE_MAPPING_OPEN / S3_CAPTURE_CLOCK_CROSSWALK_OPEN / EVENT_INTERVAL_SEMANTICS_OPEN / C0_UNCHANGED / NO_DECISION_AMENDMENT / NO_SCHEMA_CHANGE / NO_CODE_CHANGE / NO_EXECUTION / NO_DESIGN_FREEZE.
