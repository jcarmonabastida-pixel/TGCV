# C10-S — Gate 96: contrato lógico del registro relacional de eventos de proceso D2

**Estado:** LOGICAL CONTRACT PROPOSED / OPTION B RETAINED AS RECOMMENDATION / NOT ACCEPTED / NOT FROZEN / NO IMPLEMENTATION / NO EXECUTION  
**Rama:** `research/c10-s-consolidation-draft`  
**Fecha:** 2026-11-15  
**Precedencia:** DEC-C10-060…067; DEC-C10-061 typed-target contract; DEC-C10-062 record identity/version/supersession; DEC-C10-065 exact snapshot pinning; DEC-C10-071 stage_key vocabulary; DEC-C10-083 stage applicability; DEC-C10-088 temporal adjudication; Gates 92–95; U_G inventory template §§2–15 and §17–18; U_G typed-target and identity contracts; DGP Temporal and Role Contract §§2–3.  
**Alcance:** desarrollar el contrato lógico de la alternativa B recomendada en Gate 95. Definir identidad de ocurrencia y corrección, catálogo candidato de tipos, temporalidad, causalidad, concurrencia, reintentos, referencias tipadas, snapshots, evidencia/cobertura y firewalls. No aceptar la arquitectura, no modificar decisiones vigentes, no congelar el esquema físico, no implementar ni ejecutar.

---

## 1. Dictamen ejecutivo

Gate 95 recomendó B: un registro relacional de eventos de proceso integrado en U_G, no una ampliación de NODE ni una plataforma/event store externa. Gate 96 desarrolla esa recomendación hasta un contrato lógico trazable.

**Propuesta de composición lógica:**

1. `PROCESS_EVENT`: una fila versionada por ocurrencia operativa.
2. `PROCESS_EVENT_RELATION`: relaciones explícitas entre ocurrencias, para causalidad, precedencia y reintentos.
3. `PROCESS_EVENT_BINDING`: referencias tipadas desde una ocurrencia hacia unidad, política B/version, artefactos, componentes y predicados existentes.
4. `PROCESS_EVENT_SNAPSHOT_BINDING`: referencias a revisiones exactas de SNAPSHOT, con papel temporal explícito.
5. Reutilización de `EVIDENCE_REGISTER`, `CLAIM_EVIDENCE_LINK`, `COVERAGE_REGISTER`, `EVALUATOR_ASSESSMENT` y `ADJUDICATION_REGISTER`; no crear un ledger de evidencia alternativo.

Los nombres anteriores son **identificadores lógicos propuestos**, no nombres físicos aceptados. Las cuatro relaciones forman una extensión interna de U_G. La necesidad y cardinalidad de cada relación se especifican aquí para evitar que la implementación tenga que inventar semánticas; la elección final de nombres, tipos físicos y serialización sigue abierta.

El registro representa ocurrencias observables y sus referencias. La truth de eventos potenciales o generados permanece fuera de U_G, en el canal restringido del Generator/Evaluator. No se admite una columna que mezcle truth y observación.

**No se propone** ampliar NODE, añadir semantic_role, reinterpretar EID, modificar SNAPSHOT, crear un reloj global ni convertir la secuencia de eventos en ROUTE/ROUTE_STEP.

## 2. Fronteras semánticas y reglas de no duplicación

| Concepto | Representación canónica | No debe confundirse con |
|---|---|---|
| Ocurrencia operativa | PROCESS_EVENT | NODE, EID genérico o evidencia |
| Definición/version de política B | Objeto versionado existente, referenciado tipadamente | Evento de asignación o de recepción |
| Asignación Z realizada | Ocurrencia de tipo Z_ASSIGNED, vinculada a su unidad y política asignada | Transformación accesible o EID |
| Programación W_programmed | Ocurrencia PROVISION_SCHEDULED | Intento efectivo |
| Intento W_attempt | Ocurrencia PROVISION_ATTEMPT_STARTED y su terminación | Recepción, instalación o éxito |
| Recepción | Ocurrencia ARTIFACT_RECEIVED y referencia al artefacto | Instalación |
| Instalación S_install | Ocurrencias de inicio/terminación de instalación, con artefacto y componente vinculados | C_dep* verificado |
| C_dep* | Constructo/predicados existentes, con evidencia y adjudicación | Evento de instalación |
| A_f*, App_f*, D_f* | Constructos y predicados existentes | Etiquetas de eventos |
| T_acc*, ΔT_acc*, Reach y trayectoria | Contratos transformacionales, snapshots, relaciones, rutas y reglas existentes | Grafo de proceso/eventos |
| Evidencia | EVIDENCE_REGISTER + CLAIM_EVIDENCE_LINK | Ocurrencia que la evidencia respalda |
| Cobertura | COVERAGE_REGISTER | Ausencia inferida por no encontrar una fila |

Reglas vinculantes:

1. Una ocurrencia no se convierte en NODE ni en vértice de EDGE/ROUTE por el mero hecho de tener identidad.
2. EID se utiliza únicamente cuando el acto concreto satisface el contrato de identidad de una aplicación/intento de transformación. El PROCESS_EVENT puede referenciar ese EID cuando corresponda; no lo sustituye ni lo genera automáticamente.
3. La versión de política B, la asignación Z, el evento de programación y el intento son entidades distintas.
4. La instalación y su verificación son distintas. La existencia de un evento de instalación no demuestra C_dep*=1.
5. La evaluación de C_dep*, A_f* o D_f* se registra en los objetos/predicados y mecanismos de evaluación ya existentes. No se crea un tipo de evento para almacenar el valor del constructo.
6. El orden de filas, el orden de inserción, los identificadores, los timestamps y el número de revisión nunca son por sí solos prueba de causalidad ni de cambio transformacional.
7. No se duplica en PROCESS_EVENT la procedencia extensa ya normalizada en EVIDENCE_REGISTER. Se conservan referencias a evidencia y los metadatos temporales propios de la ocurrencia.

## 3. Identidad de ocurrencia, revisión y corrección

### 3.1 Tres identidades distintas

Se proponen tres campos diferenciados:

- `event_id`: identidad semántica estable de **una ocurrencia concreta**. Es opaca, no reutilizable y no codifica tipo, resultado, brazo, unidad, tiempo ni número de intento.
- `event_record_id`: identidad opaca y única de una fila inmutable concreta del registro. Es el destino de referencias tipadas y de evidencia sobre esa revisión.
- `event_revision`: entero positivo secuencial por `event_id`. Ordena revisiones del registro de la misma ocurrencia; no es una versión de software, un número de reintento ni un contador causal.

Claves e invariantes propuestos:

1. PK/UNIQUE de `event_record_id`.
2. UNIQUE de `(event_id, event_revision)`.
3. Exactamente una revisión inicial por `event_id`, con `event_revision=1` y `supersedes_event_record_id=NULL`.
4. Toda revisión posterior tiene revisión anterior inmediata y `supersedes_event_record_id` apunta a su `event_record_id`.
5. La referencia de supersession debe permanecer dentro del mismo `event_id`; no se permiten ciclos, bifurcaciones ni cadenas discontinuas.
6. Las filas anteriores no se actualizan ni eliminan. Una corrección crea una nueva fila que explica el campo corregido, motivo, fuente y autoridad de corrección.
7. Una corrección no crea una nueva ocurrencia. Un evento distinto, incluso si repite tipo, actor, unidad, artefacto y timestamp, recibe otro `event_id`.

DEC-C10-062 regula actualmente NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT. Sus reglas no se declaran aplicables automáticamente a PROCESS_EVENT. Este gate propone una semántica análoga pero autónoma, pendiente de aceptación y de una ampliación expresa del contrato de identidad/versionado.

### 3.2 Reintentos, idempotencia y duplicados

- Cada intento efectivo tiene un `event_id` propio.
- Los reintentos no son revisiones del intento anterior.
- La relación entre intentos se expresa en PROCESS_EVENT_RELATION con `RETRY_OF`; el intento posterior apunta al intento previo, sin sustituirlo.
- `attempt_ordinal`, si se materializa, es un ordinal dentro de una operación lógica explícitamente identificada. No es PK ni reemplaza event_id.
- `idempotency_key` es opcional, limitado al emisor/operación y a su ámbito de unicidad. Detecta reenvíos técnicos; no prueba identidad semántica ni elimina eventos legítimos repetidos.
- Una recepción duplicada, una reentrega y un reintento de provisión son ocurrencias distintas salvo que la fuente autoritativa demuestre que se trata de una retransmisión del mismo mensaje/acto.
- Duplicados sospechados se conservan y adjudican; no se colapsan por igualdad de contenido, hash o timestamp.

### 3.3 Corrección frente a retractación

La corrección conserva el registro original y añade una revisión. Si la evidencia posterior concluye que la ocurrencia atribuida nunca tuvo lugar, la revisión nueva debe declarar la retractación/corrección y enlazar su fundamento. No se borra la ocurrencia histórica ni se reescribe como si nunca hubiese sido registrada.

No se introduce un estado `NOT_OCCURRED` como evento ocurrido. La ausencia de una ocurrencia se evalúa mediante el contrato de evidencia/cobertura y el predicado correspondiente; falta de registro equivale a desconocido, no a cero.

## 4. Tipología cerrada propuesta para eventos D2

Se propone el siguiente vocabulario de diez tipos. Es un catálogo cerrado **para la versión candidata de este contrato**, no una aceptación ni una extensión del semantic_role. No se permiten tipos libres; un tipo adicional exige nueva versión y decisión explícita.

| event_type | Significado | Correspondencia D2 |
|---|---|---|
| `Z_ASSIGNED` | Asignación efectivamente realizada y registrada | Z |
| `POLICY_BOUND` | Vinculación de la política B/version elegida a la asignación/unidad | B_gZ |
| `PROVISION_SCHEDULED` | Intento programado por la política/proceso | W_programmed |
| `PROVISION_ATTEMPT_STARTED` | Inicio efectivo de un intento concreto | W_attempt |
| `PROVISION_ATTEMPT_TERMINATED` | Terminación del intento, cualquiera que sea su resultado | W_attempt |
| `ARTIFACT_RECEIVED` | Recepción/entrega del artefacto en destino identificado | receipt |
| `INSTALLATION_STARTED` | Inicio efectivo de instalación | S_install |
| `INSTALLATION_TERMINATED` | Terminación del acto de instalación | S_install |
| `ROLLBACK_STARTED` | Inicio efectivo de reversión | rollback |
| `ROLLBACK_TERMINATED` | Terminación del acto de reversión | rollback |

La verificación de instalación/dependencia se representa como evidencia y evaluación de predicados existentes. No se convierte en un evento que equivalga a `C_dep*=1`. Si en una implementación se necesita registrar el acto de ejecutar una comprobación, puede representarse mediante un evento operativo solo tras justificar su utilidad y tipología; este gate no añade un undécimo tipo.

### 4.1 Resultado del evento

`event_type` describe qué ocurrió; no su éxito. Se propone un campo separado `event_result`, con dominio:

- `SUCCEEDED`
- `FAILED`
- `PARTIAL`
- `CANCELLED`
- `UNKNOWN`
- `NOT_APPLICABLE`

Reglas:
- El resultado se refiere al acto descrito, no a C_dep*, A_f*, D_f*, ΔT_acc*, Reach, Outcome o Value.
- `NOT_APPLICABLE` solo se admite para tipos cuyo contrato permita no tener resultado; requiere justificación. No significa ausencia.
- `UNKNOWN` no se sustituye por `FAILED` ni por `SUCCEEDED`.
- Un intento que falla sigue siendo una ocurrencia válida. Una programación sin intento efectivo no genera artificialmente PROVISION_ATTEMPT_STARTED.
- La ausencia de intento se clasifica fuera del event log mediante evidencia suficiente, cobertura y adjudicación; si la cobertura no permite demostrarla, se conserva ?.

## 5. Contrato lógico mínimo de PROCESS_EVENT

Cada fila representa una ocurrencia, o una revisión inmutable de su registro.

| Campo lógico | Cardinalidad | Regla |
|---|---:|---|
| event_id | 1 | Identidad estable de ocurrencia |
| event_record_id | 1 | Identidad de fila/revisión, UNIQUE |
| event_revision | 1 | Entero positivo, secuencial por event_id |
| supersedes_event_record_id | 0..1 | Revisión inmediatamente anterior de la misma ocurrencia |
| event_type | 1 | Enum cerrado §4 |
| event_result | 0..1 | Enum §4.1; requerido cuando el tipo/acto tenga resultado |
| unit_id | 1 | Unidad lógica del DGP, no ID de evento |
| run_id | 1 | Ejecución concreta; referencia a identidad de run ya existente |
| replicate_id | 1 | Réplica concreta dentro del run |
| event_time | 0..1 | Instante efectivo de ocurrencia; obligatorio para evento efectivamente ocurrido si la fuente puede determinarlo |
| event_start_time / event_end_time | 0..1 / 0..1 | Intervalo de acto cuando la fuente registra duración; ambos o ninguno y end ≥ start |
| scheduled_time | 0..1 | Tiempo previsto; solo para eventos programables |
| recorded_at | 1 | Tiempo de incorporación de esta revisión al registro; generado por el registrador |
| clock_domain_id | 0..1 | Identidad/version del reloj fuente cuando afecta a la comparabilidad |
| clock_uncertainty | 0..1 | Incertidumbre temporal y unidad; no inventar precisión |
| dgp_time_key | 0..1 | Clave del reloj causal/analítico según la versión DGP |
| stage_key | 0..1 | Solo uno de los siete valores DEC-C10-071; null si no aplica, con reason |
| stage_key_na_reason | 0..1 | Obligatorio si stage_key no aplica o no puede determinarse; distinguir ambos casos |
| event_source_id | 1 | Emisor/sistema/origen identificado, sin secretos |
| actor_ref | 0..1 | Actor/principal referenciado de forma segura; no almacenar credenciales |
| event_payload_ref | 0..1 | Referencia/hash a payload protegido; no volcar datos sensibles ni truth |
| correction_reason | 0..1 | Obligatorio para revisión >1 |
| recorded_by | 1 | Proceso/identidad de registro y versión |
| schema_contract_version | 1 | Versión de este contrato lógico |
| evidence_status | 1 | AVAILABLE / MISSING / CONFLICTING para la base de evidencia asociada, no para verdad del DGP |
| coverage_scope_id | 0..1 | FK a COVERAGE_REGISTER cuando el registro se incorpora a un scope definido |

Las cardinalidades se interpretan por fila de revisión. Los campos no aplicables no se rellenan con ceros, timestamps ficticios, cadenas vacías o valores inventados.

### 5.1 Campos deliberadamente no incluidos

- No se replica `observed_at` de EVIDENCE_REGISTER. La observación/captura de una fuente se registra allí; `event_time` es el tiempo atribuido a la ocurrencia.
- No se replica `source_provenance`, custodian, integrity ni collection_method de EVIDENCE_REGISTER.
- No se introduce `object_version`: la revisión del evento tiene su propio `event_revision`.
- No se incluye `snapshot.phase` ni un snapshot implícito «latest».
- No se incluye un campo genérico `target_type + target_id`.
- No se incluye verdad potencial, probabilidad de éxito, contrafactual, resultado potencial ni variables privadas del Generator.
- No se incluye `semantic_role`: los eventos no son NODE.

## 6. Temporalidad y orden causal

### 6.1 Cuatro tiempos no intercambiables

1. `scheduled_time`: cuándo estaba previsto que ocurriera el acto.
2. `event_time` o intervalo start/end: cuándo ocurrió efectivamente según la fuente y su precisión.
3. `observed_at`: cuándo la fuente/evidencia capturó u observó el hecho; reside en EVIDENCE_REGISTER.
4. `recorded_at`: cuándo la fila/revisión se incorporó al registro.

No se deriva uno de otro. Un evento puede registrarse tarde, observarse después de ocurrir o tener tiempo de ocurrencia desconocido. Una programación no prueba ocurrencia. La hora de captura de un snapshot no sustituye event_time.

Todos los instantes deben conservar offset/zona o normalización UTC acompañada de la información necesaria para recuperar la fuente temporal original. La precisión declarada no puede superar la precisión real del reloj. Si dos relojes no son comparables, el orden temporal queda indeterminado salvo evidencia causal independiente.

### 6.2 Ejes DGP y C10-S

Se mantienen cuatro ejes independientes:

- `dgp_time_key`: reloj causal del DGP, con la versión y vocabulario de la unidad generadora.
- `stage_key`: exclusivamente los siete valores aceptados por DEC-C10-071. No se amplía en Gate 96.
- `SNAPSHOT.phase`: fase del snapshot según su dominio vigente.
- `k=1…H`: profundidad de trayectoria hipotética, no tiempo de reloj ni secuencia de eventos.

La correspondencia entre ellos debe estar declarada en un mapping versionado, aplicable a la unidad/escenario. No se infiere del event_type, del nombre de la etapa, del orden de inserción ni del timestamp. Los eventos D2 que no correspondan a ninguna stage_key llevan null y reason explícito; no se crean alias ni nuevos stage_key.

### 6.3 Orden causal y concurrencia

El orden causal no se deduce del timestamp. Se registra mediante PROCESS_EVENT_RELATION.

Reglas:
- `CAUSES`: relación causal declarada y respaldada por el DGP o por evidencia/procedencia admisible.
- `PRECEDES`: orden parcial conocido sin afirmar causalidad.
- `RETRY_OF`: el evento posterior es un reintento del acto identificado.
- `DERIVED_FROM`: relación de derivación documental/operativa cuando sea necesaria y no equivalga a causalidad.

No se añade una relación si solo se conoce que A y B tienen timestamps distintos. Los eventos concurrentes permanecen sin relación de orden. Los empates temporales no se rompen mediante IDs o secuencia de inserción.

El grafo de relaciones debe:
1. permitir múltiples predecesores y sucesores;
2. prohibir autorreferencia;
3. prohibir ciclos en `CAUSES` y `PRECEDES`;
4. impedir que `RETRY_OF` apunte a un evento posterior o a una ocurrencia de tipo incompatible;
5. conservar la diferencia entre causalidad y precedencia;
6. declarar fuente/regla y evidencia de cada relación;
7. conservar relaciones contradictorias para adjudicación, sin resolverlas por orden lexical.

### 6.4 PROCESS_EVENT_RELATION

Campos lógicos propuestos:

| Campo | Regla |
|---|---|
| relation_record_id | PK opaca e inmutable |
| source_event_record_id | FK al registro exacto de origen |
| target_event_record_id | FK al registro exacto de destino |
| relation_type | CAUSES / PRECEDES / RETRY_OF / DERIVED_FROM |
| relation_revision | Revisión de la relación si se corrige; historial append-only |
| evidence_id | FK opcional a EVIDENCE_REGISTER |
| coverage_scope_id | FK opcional a COVERAGE_REGISTER |
| recorded_at / recorded_by | Procedencia del registro de relación |
| supersedes_relation_record_id | Revisión previa de la misma relación, si aplica |

La identidad de la relación debe distinguir el par dirigido y el tipo; no se presupone que una misma pareja pueda tener una única relación. Las restricciones de unicidad y revisión deben impedir duplicación exacta, pero permitir relaciones distintas justificadas. La corrección no sobrescribe la relación previa.

## 7. Referencias tipadas a objetos U_G

### 7.1 PROCESS_EVENT_BINDING

Una ocurrencia puede referenciar más de un objeto y más de un rol. Para evitar columnas polimórficas y permitir varios artefactos/componentes, se propone una relación normalizada de bindings. Esta relación no apunta a otras ocurrencias ni a SNAPSHOT: esas referencias tienen relaciones específicas.

Campos lógicos:

- `binding_record_id`: PK opaca/inmutable.
- `event_record_id`: FK al registro exacto de PROCESS_EVENT.
- `binding_role`: enum cerrado candidato.
- `target_type`: enum que coincide exactamente con una columna FK tipada.
- Columnas nullable: `target_node_record_id`, `target_edge_record_id`, `target_route_record_id` y `target_predicate_record_id`. Los snapshots se enlazan exclusivamente mediante PROCESS_EVENT_SNAPSHOT_BINDING; otras ocurrencias se enlazan exclusivamente mediante PROCESS_EVENT_RELATION.
- `recorded_at`, `recorded_by`, `evidence_id` y `coverage_scope_id` según proceda.

Invariante: exactamente una de las cuatro FKs destino no nula y concordante con target_type. No se acepta `target_id` sin tipo ni listas serializadas.

Roles candidatos para PROCESS_EVENT_BINDING, sujetos a reconciliación final con el crosswalk N01–N23:

- `UNIT`: NODE semantic_role=LOGICAL_SERVICE_UNIT.
- `ASSIGNMENT`: referencia al evento Z_ASSIGNED mediante relación de eventos, no un NODE artificial.
- `POLICY_VERSION`: NODE que identifica la definición/version exacta B_g0/B_g1.
- `ARTIFACT`: NODE de artefacto/paquete concreto.
- `COMPONENT`: NODE de componente/runtime/dependencia.
- `TRANSFORMATION_INSTANCE`: NODE TRANSFORMATION_EVENT con EID solo si cumple C10-S-ID-MATCH-001.
- `PREDICATE_ASSESSMENT`: PREDICATE exacto evaluado, sin incorporar su truth al evento.
- Los roles de snapshot no pertenecen a PROCESS_EVENT_BINDING; se expresan exclusivamente mediante snapshot_relation_role en §7.2.

El binding de unidad debe resolver una unidad lógica exacta. Si se usa el nodo raíz versionado, la referencia debe apuntar a su registro concreto conforme a DEC-C10-065; no se resolverá por «última versión». La relación entre el unit_id del DGP y el NODE LOGICAL_SERVICE_UNIT debe comprobarse, no asumirse por coincidencia textual.

### 7.2 PROCESS_EVENT_SNAPSHOT_BINDING

Los snapshots se enlazan en una relación específica, no mediante campos pre/post ambiguos dentro de PROCESS_EVENT:

- `event_record_id`
- `snapshot_id`
- `snapshot_object_record_id`
- `snapshot_relation_role`: BEFORE / AFTER / CONTEXT / ROLLBACK_STATE
- `recorded_at`, `evidence_id`, `coverage_scope_id` cuando proceda.

FK compuesta exacta a la revisión de SNAPSHOT conforme a DEC-C10-065. La pareja snapshot_id + snapshot_object_record_id es obligatoria; ambos componentes son nulos o ambos presentes. No se permite matching por timestamp, unit_id o latest.

Un evento puede no tener snapshot asociado. La ausencia de snapshot no invalida la ocurrencia, pero impide afirmaciones que requieran estado estructural pre/post no disponible. Un snapshot posterior no demuestra por sí solo qué evento lo causó.

### 7.3 Referencias a Z, B, unidad y artefactos

- Z se identifica por el evento Z_ASSIGNED, con su unidad/run/replicate y procedencia de asignación. No se convierte en EID.
- B_g0/B_g1 se identifica por la definición/version del objeto de política ya existente; la vinculación POLICY_BOUND debe apuntar a esa versión exacta y a la asignación correspondiente.
- La unidad se referencia como objeto lógico exacto, no por un nombre libre.
- Los artefactos recibidos/instalados se referencian por identidad y versión/hash del objeto NODE correspondiente; el hash acredita integridad del artefacto, no identidad semántica por sí solo.
- Las transformaciones efectivas se vinculan mediante TRANSFORMATION_INSTANCE/EID solo cuando el acto satisface su definición. Si no, el evento operativo conserva event_id propio sin inventar EID.

## 8. Integración con evidencia, cobertura y adjudicación

### 8.1 Evidencia

EVIDENCE_REGISTER sigue siendo la única fuente canónica de procedencia. Una fila PROCESS_EVENT no es evidencia autosuficiente. Toda afirmación observacional material sobre ocurrencia, resultado, tiempo, actor, política, recepción o instalación debe estar respaldada por evidence_id(s) con:
- origen y localizador;
- método/versión de captura;
- unidad, run, ventana y ámbito;
- timestamp de observación y record-time;
- integridad/hash;
- límites de completitud, filtros y retención;
- clasificación AVAILABLE / MISSING / CONFLICTING.

La relación de evidencia al evento debe fijar el event_record_id exacto, no solo event_id, para que una corrección posterior no reescriba qué revisión sustentó una evaluación histórica.

### 8.2 Extensión propuesta de DEC-C10-061

DEC-C10-061 limita actualmente los destinos tipados a NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT y COVERAGE_SCOPE. Si se requieren claims, evaluaciones o adjudicaciones **directamente sobre una ocurrencia**, se propone añadir PROCESS_EVENT como séptimo destino tipado:

- `target_process_event_record_id` nullable FK → PROCESS_EVENT.event_record_id.
- `claim_target_type=PROCESS_EVENT` si y solo si esa es la única FK no nula.
- Aplicar la misma regla de exclusividad y concordancia en CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER.
- Mantener evidence_id como FK obligatoria a EVIDENCE_REGISTER.
- Mantener COVERAGE_SCOPE como destino separado, sin convertir coverage_scope_id en event_id.

La extensión es una propuesta de enmienda a DEC-C10-061; Gate 96 no la aprueba. No se crea una segunda tabla de enlaces de evidencia. Si se decide no permitir claims directos sobre eventos, deberá especificarse un patrón indirecto explícito y auditable; no se permitirá ocultar una afirmación sobre un evento bajo un NODE que no la representa.

### 8.3 Cobertura

COVERAGE_REGISTER sigue siendo el único registro de cobertura. El universo debe declarar:
- población de unidades/run/replicates;
- catálogo de tipos de evento esperado por política/escenario;
- ventanas temporales y fuentes;
- superficies de captura, emisores y límites de detección;
- denominador y regla de inclusión/exclusión;
- versión del mapping event_type ↔ DGP stage/time;
- estados examinados, no disponibles, conflictivos, opacos y no resueltos.

La cobertura de eventos es por tipo, unidad y ventana; no se promedian dimensiones para producir un porcentaje global que oculte una dimensión crítica. La ausencia de una fila solo puede adjudicarse como 0 si el universo, la capacidad de detección y la cobertura son suficientes. En otro caso permanece ?.

No se añade EVENT_COVERAGE_REGISTER. Los eventos pueden referenciar coverage_scope_id cuando su pertenencia al universo esté establecida, pero la definición y denominador viven en COVERAGE_REGISTER.

### 8.4 Adjudicación

EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER conservan su función y su historial. Las evaluaciones se fijan a event_record_id y evidence_id exactos. Discrepancias de identidad, duplicidad, tipo, tiempo, causalidad, concurrencia, resultado o cobertura permanecen visibles hasta adjudicación.

La adjudicación no puede convertir:
- MISSING en 0 sin cobertura;
- programación en intento;
- intento en instalación;
- instalación en C_dep*=1;
- ausencia de evidencia en ausencia del evento;
- precedencia temporal en causalidad.

## 9. Separación de truth y observación; firewalls

### 9.1 Canales

| Componente | Puede producir/recibir | Prohibición |
|---|---|---|
| Generator | Truth completa de eventos/potenciales, IDs internos, mecanismo y mundo | No exponer truth/potenciales al registro observado |
| Projector | Proyección de observaciones permitidas de eventos y evidencia | No derivar observaciones no presentes ni completar huecos con truth |
| Sealer | Validación de allowlist, referencias, tipos, integridad, hashes y provenance | No inferir verdad ni reparar semántica |
| Analyzer | Eventos observados sellados, evidencia, cobertura y contratos públicos | No recibir truth, potenciales, resultados contrafactuales ni metadatos reservados |
| Evaluator | Comparación post-seal entre truth protegida y salida observada/analizada | No modificar retroactivamente el paquete sellado ni filtrar truth al Analyzer |

### 9.2 Separación de identidad entre truth y observación

Los identificadores internos de truth no se reutilizan automáticamente como event_id observado si esa reutilización revelase eventos no observados o contrafactuales. El Generator mantiene su propia identidad de ocurrencia verdadera en DGP_TRUTH_SECURE. El Projector crea la identidad observacional solo para registros efectivamente proyectados.

El Evaluator dispone de un mapping protegido truth↔observación después del sellado, con alcance mínimo y provenance. El mapping no se exporta al Analyzer ni se incluye en el paquete observable. No se comparte un event_id que permita al Analyzer enumerar eventos contrafactuales o ausentes.

### 9.3 Estados trivalentes

La observación de un evento debe distinguir:
- evidencia suficiente de ocurrencia;
- evidencia suficiente de no ocurrencia dentro del universo/ventana;
- unknown por ausencia, conflicto, cobertura insuficiente o relojes no comparables.

El registro de ocurrencias almacena eventos observados; la evaluación negativa de ocurrencia no se fabrica como evento. La verdad del generador puede contener 0/1 y potenciales, pero permanece restringida.

## 10. Invariantes y controles de integridad exigibles

Antes de implementar, el diseño físico deberá demostrar al menos:

1. PK/UNIQUE y FK de event_id/event_record_id/revision.
2. Cadena lineal de correcciones por event_id, sin ciclos ni bifurcaciones.
3. Append-only real: no UPDATE/DELETE destructivo de registros históricos.
4. Dominios cerrados event_type, event_result, relation_type, binding_role, target_type y snapshot_relation_role.
5. Exclusividad de exactamente una FK tipada por binding.
6. FKs de eventos a sus relaciones y de relaciones a registros exactos de eventos.
7. FKs tipadas de PROCESS_EVENT_BINDING a objetos U_G existentes.
8. FK compuesta exacta de snapshot binding según DEC-C10-065.
9. Compatibilidad de event_type con event_result y campos temporales aplicables.
10. Coherencia de run_id, replicate_id, unit_id, asignación Z y política B/version.
11. No duplicidad exacta de binding/relación, sin colapsar ocurrencias distintas.
12. Prohibición de ciclos en relaciones CAUSES/PRECEDES y validación de RETRY_OF.
13. stage_key dentro de los siete valores aceptados o null justificado; dgp_time_key validado contra versión DGP.
14. event_time, observed_at y recorded_at no intercambiables; offsets, precisión y reloj fuente conservados.
15. Toda corrección tiene razón, fuente, autoría y revisión previa.
16. Toda afirmación observacional material dispone de evidencia/procedencia y scope compatible.
17. No hay truth/potenciales en tablas, payloads, logs o exportaciones visibles al Analyzer.
18. Ninguna consulta del grafo estructural incorpora PROCESS_EVENT como NODE/EDGE/ROUTE/ROUTE_STEP por defecto.

CHECK/FK/trigger/parser o validador independiente son mecanismos de implementación posibles; su elección queda abierta. No se presume que Markdown, una fila de plantilla o una validación sintáctica demuestren estas invariantes.

## 11. Compatibilidad y decisiones que el gate no resuelve

| Tema | Tratamiento Gate 96 |
|---|---|
| Opción B | Sigue recomendada; no aceptada |
| Tabla/relaciones físicas | Contrato lógico propuesto; nombres finales abiertos |
| event_id/event_record_id/revision | Semántica propuesta; aceptación pendiente |
| Catálogo event_type | Diez tipos candidatos; cierre formal pendiente |
| event_result | Dominio candidato; compatibilidad por tipo pendiente |
| Causalidad/concurrencia/reintentos | Modelo DAG relacional propuesto; constraints físicas pendientes |
| DEC-C10-061 | Enmienda para destino PROCESS_EVENT propuesta; no aprobada |
| DEC-C10-062 | No se extiende automáticamente; contrato de evento propio requerido |
| DEC-C10-065 | Se conserva íntegramente para bindings exactos de SNAPSHOT |
| DEC-C10-071 | No se amplía stage_key; solo siete valores |
| DEC-C10-088 | Se mantienen ejes y binding explícito |
| U_G physical schema / motor | No elegido ni validado |
| Mapping N02/N03 y catálogo semántico | Reconciliación final pendiente; no alterar los 16 semantic_role |
| DGP quantitative parameters | No se modifican |
| Generator/Projector/Sealer/Analyzer/Evaluator | Sin cambios de código |
| Implementación, fixtures, tests, simulación | No autorizados por este gate |

Cuestiones que requieren decisión posterior:
1. Aceptar o rechazar B como extensión U_G.
2. Aceptar los nombres lógicos y el catálogo de diez tipos, o modificarlo con justificación.
3. Aceptar el contrato de identidad/revisión/supersession del evento.
4. Aprobar la enmienda a DEC-C10-061 para claims/evaluaciones directas de eventos.
5. Cerrar los bindings de N02/N03, política B, artefactos y unidad contra las claves reales de U_G.
6. Definir el mapping versionado event_type ↔ reloj DGP ↔ stage_key ↔ snapshot cuando aplique.
7. Elegir la forma física de PROCESS_EVENT_RELATION y PROCESS_EVENT_BINDING y demostrar integridad.
8. Determinar cómo el Generator conserva truth de eventos y cómo el Projector genera el subconjunto observable sin filtración.
9. Reconciliar el contrato con las matrices físicas U_G y los esquemas de exportación existentes antes de implementar.

## 12. Dictamen y siguiente operación

**Gate 96 se cierra como desarrollo de contrato lógico propuesto, no como aceptación de arquitectura ni freeze.**

Dictamen:

`GATE_96_LOGICAL_PROCESS_EVENT_CONTRACT_DRAFTED / OPTION_B_STILL_UNACCEPTED / EVENT_OCCURRENCE_IDENTITY_SEPARATED_FROM_RECORD_REVISION_AND_EID / TEN_CANDIDATE_EVENT_TYPES / TIME_AXES_EXPLICIT / CAUSAL_PARTIAL_ORDER_AND_CONCURRENCY_PRESERVED / RETRIES_AS_DISTINCT_OCCURRENCES / TYPED_BINDINGS_TO_UG / EXACT_SNAPSHOT_PINNING_PRESERVED / EVIDENCE_AND_COVERAGE_REUSED / DEC_C10_061_AMENDMENT_PROPOSED_NOT_ACCEPTED / TRUTH_OBSERVATION_FIREWALL_PRESERVED / NO_SCHEMA_CHANGE / NO_CODE_CHANGE / NO_TESTS / NO_EXECUTION / NO_DESIGN_FREEZE`

**Siguiente operación propuesta — Gate 97:** auditoría de compatibilidad y suficiencia del contrato lógico frente a la matriz física U_G, DEC-C10-061…065, los crosswalks N02/N03 y el contrato de identidad/versionado. Debe comprobar cada campo, FK, cardinalidad y regla contra las estructuras ya existentes; identificar duplicaciones, incompatibilidades y campos que puedan derivarse sin pérdida; y emitir una propuesta de enmienda mínima de DEC-C10-061 y del contrato de identidad. No implementar, no ejecutar y no congelar.

**Límites de evidencia:** revisión documental asistida sobre artefactos GitHub; no revisión independiente. No se ejecutaron validadores, parsers, tests, workflows ni simulaciones. `scientific_execution=false`; `execution_authorized=false`.
