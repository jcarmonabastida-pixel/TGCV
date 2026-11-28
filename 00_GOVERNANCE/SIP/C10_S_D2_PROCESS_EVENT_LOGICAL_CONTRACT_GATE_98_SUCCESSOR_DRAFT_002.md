# C10-S — Gate 98: reconciliación correctiva del contrato lógico de eventos D2 (sucesor de Gate 96)

**Estado:** SUCCESSOR LOGICAL CONTRACT / CORRECTED AGAINST GATE 97 / OPTION B STILL NOT ACCEPTED / OPEN DECISIONS RETAINED / NO SCHEMA CHANGE / NO IMPLEMENTATION / NO EXECUTION / NO FREEZE  
**Fecha:** 2026-11-15  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft  
**Precedencia:** Gates 94–97; DEC-C10-060…071, 083, 088; DEC-C10-061 typed-target contract; DEC-C10-062 identity/version/supersession (solo cinco tablas de objetos); DEC-C10-063/064 Opción A; DEC-C10-065 snapshot exact pinning; DEC-C10-067 D2 material policy; DEC-C10-070 C0; DGP Temporal and Role Contract; U_G inventory template; IAM/FP crosswalk; evidence/provenance/adjudication protocol.  
**Relación histórica:** sucesor lógico de `C10_S_D2_PROCESS_EVENT_REGISTER_LOGICAL_CONTRACT_GATE_96_DRAFT_001.md`. Gate 96 permanece inmutable como antecedente; Gate 97 permanece como auditoría de compatibilidad.

---

## 1. Resultado y alcance

Gate 98 corrige el contrato candidato de Gate 96 usando los hallazgos G97-01…12. El resultado es un contrato lógico más preciso y una lista explícita de bloqueos que no pueden resolverse sin nuevas decisiones o fuentes de contrato.

**Dictamen:** Gate 96 queda parcialmente reconciliado; Gate 98 mejora su coherencia documental, pero **no declara el registro implementable, aceptado ni congelado**. La alternativa B de Gate 95 sigue siendo recomendación. Opción A estructural (DEC-C10-063/064/065) permanece intacta y es composable con B.

### Cambios correctivos principales

1. Separa identidad de ocurrencia, revisión del registro, evidencia y adjudicación; distingue corrección de identidad, retractación, duplicidad, split y merge.
2. Retira `coverage_scope_id` y `evidence_status` como atributos canónicos de PROCESS_EVENT/PROCESS_EVENT_RELATION: duplicaban o simplificaban indebidamente registros existentes.
3. Reubica bindings a unidad, política, artefacto, componente y predicado en referencias tipadas; las relaciones entre ocurrencias permanecen en PROCESS_EVENT_RELATION.
4. Mantiene snapshots en PROCESS_EVENT_SNAPSHOT_BINDING con pinning compuesto exacto DEC-C10-065.
5. No crea una FK de evento a NODE artificial para Z, ni presume que la definición B sea un NODE.
6. No amplía DEC-C10-061 ni DEC-C10-070. Deja explícitos los límites actuales de claims directos y cobertura C0.
7. Precisa event_type × event_result y las relaciones operativas, manteniendo abiertas las correspondencias que el DGP no determina.
8. Preserva el firewall truth/observación y no incorpora EID salvo cuando el acto satisfaga su contrato vigente.

## 2. Arquitectura lógica candidata y composición con Opción A

Se mantienen cuatro relaciones lógicas, sin aprobar todavía nombres físicos ni DDL:

| Relación lógica | Responsabilidad exclusiva |
|---|---|
| PROCESS_EVENT | Ocurrencia operativa observada y revisiones inmutables de su registro |
| PROCESS_EVENT_RELATION | Relaciones tipadas entre revisiones exactas de ocurrencias |
| PROCESS_EVENT_BINDING | Referencias tipadas desde una ocurrencia a objetos/contratos existentes |
| PROCESS_EVENT_SNAPSHOT_BINDING | Referencias a revisiones exactas de SNAPSHOT y papel contextual |

No se crea un quinto registro de evidencia, cobertura, adjudicación o identidad. EVIDENCE_REGISTER, COVERAGE_REGISTER, CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER conservan sus funciones.

**Composición no conflictiva:**
- Opción A: NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT y ROUTE_STEP representan estructura, objetos, relaciones y snapshots versionados.
- B (si se acepta): PROCESS_EVENT representa ocurrencias temporales fuera del grafo estructural.
- PROCESS_EVENT no es NODE, EDGE, ROUTE_STEP, transformación accesible ni nueva clase de semantic_role.
- PROCESS_EVENT_RELATION no es EDGE estructural y no participa automáticamente en T_acc/Reach.
- EID conserva el significado fijado por C10-S-ID-MATCH-001; no es ID genérico de evento.

## 3. Identidad de ocurrencia, revisión y ciclo de vida

### 3.1 Identidades no intercambiables

| Identidad | Significado | Registro canónico |
|---|---|---|
| event_id | Ocurrencia operativa observada concreta; estable y opaca | PROCESS_EVENT |
| event_record_id | Revisión inmutable exacta de la fila observacional | PROCESS_EVENT |
| event_revision | Secuencia de revisiones de un mismo event_id | PROCESS_EVENT |
| evidence_id | Artefacto/fuente que respalda una afirmación | EVIDENCE_REGISTER |
| adjudication_id | Resolución adjudicada de una discrepancia/afirmación | ADJUDICATION_REGISTER |
| EID | Identidad de transformación concreta solo si satisface C10-S-ID-MATCH-001 | Contrato vigente de identidad transformacional |

No se heredan object_record_id, object_version ni supersedes_record_id de DEC-C10-062. Se proponen nombres propios de evento porque DEC-C10-062 aplica únicamente a NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT.

### 3.2 Revisión append-only

Para cada event_id:
- event_record_id PK/UNIQUE dentro de PROCESS_EVENT.
- UNIQUE(event_id, event_revision).
- Una sola raíz con event_revision=1 y supersedes_event_record_id=NULL.
- Cada revisión posterior apunta al registro inmediatamente anterior del mismo event_id.
- Cada registro puede tener como máximo un sucesor inmediato.
- event_revision es entero positivo, contiguo y no reutilizable.
- No se permiten ciclos, huérfanos, bifurcaciones ni supersession cruzada entre event_id.
- Las filas históricas son inmutables; una corrección crea nueva revisión y conserva autoría, momento de registro y motivo.
- La identidad semántica del evento no se altera silenciosamente al revisar sus atributos.

Estas reglas son requisitos lógicos candidatos, no constraints físicos demostrados.

### 3.3 Qué genera revisión y qué no

| Situación nueva | Tratamiento |
|---|---|
| Corrección de un atributo capturado de la misma ocurrencia | Nueva revisión de event_id; indicar campo, motivo y fuente |
| Nueva fuente confirma la misma ocurrencia | Nuevo evidence_id; no nueva ocurrencia ni revisión automática |
| Nueva fuente contradice la ocurrencia | Nueva evidencia y adjudicación; no sobrescribir el evento |
| Cambio de adjudicación | Nueva adjudicación; no reescribir PROCESS_EVENT |
| Reintento operativo real | Nuevo event_id y relación RETRY_OF |
| Retransmisión técnica del mismo mensaje/acto | No crear nueva ocurrencia si fuente autoritativa confirma que es el mismo acto; conservar evidencia de deduplicación |
| Dos filas se juzgan duplicadas | Conservar ambas identidades; adjudicar duplicidad, sin borrar ni fusionar IDs |
| Una fila se divide en dos ocurrencias | Nuevos event_id; conservar la identidad previa como antecedente adjudicado |
| Varias filas se juzgan una ocurrencia | Conservarlas; adjudicar equivalencia/duplicidad y seleccionar representación canónica solo mediante regla explícita |
| Se concluye que el evento no ocurrió | Retractación adjudicada respaldada; no borrar la fila histórica ni codificar un evento ficticio NOT_OCCURRED |

Split, merge, duplicate y retractación no se codifican como supersession ordinaria. Requieren relaciones de identidad adjudicadas con evidencia y autoridad. Sus nombres físicos y si se materializan como tipos adicionales de PROCESS_EVENT_RELATION quedan abiertos; no se amplía ahora el enum.

## 4. Contrato mínimo de PROCESS_EVENT

Cada fila describe una ocurrencia observada o una revisión inmutable de su registro; no representa el universo completo de eventos potenciales.

| Campo lógico | Cardinalidad | Regla corregida |
|---|---:|---|
| event_id | 1 | Identidad opaca y estable de ocurrencia |
| event_record_id | 1 | Identidad única de revisión exacta |
| event_revision | 1 | Entero positivo, secuencial por event_id |
| supersedes_event_record_id | 0..1 | Revisión inmediatamente anterior de la misma ocurrencia |
| event_type | 1 | Catálogo candidato `5 |
| event_result | 0..1 | Resultado del acto solo donde el tipo lo permita; matriz `5.1 |
| dgp_instance_id | 1 | Identidad de instancia/unidad generadora según contrato DGP |
| run_id | 1 | Identidad de run dentro del contrato DGP |
| replicate_id | 1 | Réplica dentro de run |
| unit_id | 1 | Unidad DGP; no sustituye binding al NODE exacto |
| event_time | 0..1 | Instante atribuido a la ocurrencia; precisión de fuente |
| event_start_time / event_end_time | 0..1 | Ambos o ninguno; end no anterior a start bajo reloj comparable |
| scheduled_time | 0..1 | Tiempo previsto, no prueba ocurrencia |
| recorded_at | 1 | Momento de registro de esta revisión |
| clock_domain_id | 0..1 | Reloj fuente tipado/versionado si afecta a comparabilidad |
| clock_uncertainty | 0..1 | Incertidumbre + unidad; no inventar precisión |
| dgp_time_key | 0..1 | Eje temporal DGP, validado contra versión de contrato |
| stage_key | 0..1 | Solo vocabulario DEC-C10-071; no ampliar |
| stage_key_status | 1 | APPLICABLE / NOT_APPLICABLE / UNDETERMINED; no colapsar NA y desconocido |
| event_emitter_id | 0..1 | Emisor operativo identificado; no es provenance ni evidence_id |
| actor_ref | 0..1 | Referencia segura a actor/principal, sin credenciales |
| event_payload_ref | 0..1 | Referencia protegida a payload; no truth ni secretos |
| correction_reason | 0..1 | Obligatorio si event_revision>1 |
| recorded_by | 1 | Identidad/proceso y versión del registrador |
| schema_contract_version | 1 | Versión del contrato lógico aplicado |

**Retirados respecto a Gate 96:** evidence_status y coverage_scope_id no son columnas canónicas de PROCESS_EVENT. El primero se deriva de evidencia/adjudicación asociada y el segundo solo puede usarse bajo la tupla C0 exacta de DEC-C10-070; no es un atributo libre del evento. Tampoco se duplica observed_at, source_provenance, custodian, integrity, collection_method ni completeness_limitations.

### 4.1 Contexto DGP y claves físicas

dgp_instance_id/run_id/replicate_id/unit_id son claves de contexto del DGP. No se declara que exista ya una tabla U_G con PK/FK física para todas ellas. Hasta que el crosswalk DGP→U_G identifique una tabla y clave exactas, se tratan como claves tipadas del contrato de exportación, no como FKs inventadas.

El vínculo de una ocurrencia a la unidad estructural se realiza mediante PROCESS_EVENT_BINDING a la revisión exacta NODE LOGICAL_SERVICE_UNIT cuando el mapping de identidad unidad↔NODE esté verificado. No basta la coincidencia textual entre unit_id y node_id.

## 5. Catálogo de tipos y semántica

Se conserva el catálogo candidato de diez tipos de Gate 96, sujeto a estas precisiones. No se acepta como catálogo físico congelado.

| event_type | Ocurrencia que representa | No acredita |
|---|---|---|
| Z_ASSIGNED | Asignación Z efectivamente realizada | Instalación, recepción, acceso o EID |
| POLICY_BOUND | Acto de vinculación de versión B a unidad/asignación, solo si es un acto distinto y observable | Que B se haya ejecutado o recibido |
| PROVISION_SCHEDULED | Programación efectiva de un acto futuro | Inicio del intento |
| PROVISION_ATTEMPT_STARTED | Inicio de un intento efectivo concreto | Éxito, recepción o instalación |
| PROVISION_ATTEMPT_TERMINATED | Terminación de ese intento | Instalación o C_dep* |
| ARTIFACT_RECEIVED | Recepción efectiva en destino identificado | Instalación o integridad funcional |
| INSTALLATION_STARTED | Inicio de instalación | Instalación completada o C_dep* |
| INSTALLATION_TERMINATED | Terminación del acto de instalación | Verificación de C_dep* |
| ROLLBACK_STARTED | Inicio efectivo de reversión | Reversión completada |
| ROLLBACK_TERMINATED | Terminación del acto de reversión | Restauración verificada |

**Regla anti-duplicación Z/B:** Z_ASSIGNED representa la asignación; el binding de política puede ser un atributo tipado de esa asignación si no existe un acto independiente. POLICY_BOUND solo se registra como evento separado si el DGP y la fuente identifican una ocurrencia separada. No duplicar un mismo acto bajo ambos tipos. La correspondencia concreta entre Z y B_g0/B_g1 debe respetar DEC-C10-067 y el contrato DGP; N02/N03 son roles del crosswalk, no claves físicas.

**Regla de programación:** PROVISION_SCHEDULED se registra solo si existe una ocurrencia de programación individual identificable. Una probabilidad o regla de política de programación no genera filas de evento. Una política de control no programar bajo Z=0 no crea un evento de programación negativa.

**Regla de EID:** solo un evento que represente una aplicación/intento de transformación concreto y cumpla C10-S-ID-MATCH-001 puede referenciar EID. Z, POLICY_BOUND, programación, receipt y rollback no reciben EID por defecto.

### 5.1 Compatibilidad event_type × event_result

El resultado no es un estado global de la cadena ni un proxy de C_dep*, A_f*, D_f*, ΔT_acc, Reach, Outcome o Value.

| event_type | event_result |
|---|---|
| Z_ASSIGNED | No aplicable si la ocurrencia es la asignación efectivamente realizada; fallo de asignación no se registra como Z_ASSIGNED |
| POLICY_BOUND | No aplicable para binding declarado; un acto distinto de entrega/recepción requiere tipo/acto explícito |
| PROVISION_SCHEDULED | No aplicable para programación realizada; cancelación posterior no reescribe la programación |
| PROVISION_ATTEMPT_STARTED | No aplicable: el resultado pertenece a la terminación |
| PROVISION_ATTEMPT_TERMINATED | SUCCEEDED / FAILED / PARTIAL / UNKNOWN; CANCELLED solo si la terminación fue cancelación real |
| ARTIFACT_RECEIVED | SUCCEEDED / PARTIAL / UNKNOWN; FAILED solo si la fuente identifica un intento de recepción fallido como ocurrencia |
| INSTALLATION_STARTED | No aplicable: resultado pertenece a terminación |
| INSTALLATION_TERMINATED | SUCCEEDED / FAILED / PARTIAL / UNKNOWN; no implica C_dep* |
| ROLLBACK_STARTED | No aplicable |
| ROLLBACK_TERMINATED | SUCCEEDED / FAILED / PARTIAL / UNKNOWN; no prueba estado restaurado |

NOT_APPLICABLE se expresa como estado tipado explícito cuando el formato lo requiera, no como cadena vacía. CANCELLED no es un valor genérico para cualquier tipo. UNKNOWN permanece distinto de FAILED. Los casos de cancelación antes del inicio, desviación, fallo de asignación y eventos de control requieren crosswalk explícito antes de añadir tipos nuevos.

## 6. PROCESS_EVENT_RELATION: relaciones entre ocurrencias

La relación apunta a revisiones exactas source_event_record_id y target_event_record_id, no a event_id abstracto. Esto preserva qué observación/revisión sustentó la relación.

Campos lógicos:
- relation_record_id: identidad opaca e inmutable.
- source_event_record_id / target_event_record_id: FKs a event_record_id exactos.
- relation_type: enum candidato.
- relation_revision y supersedes_relation_record_id: versionado propio de la relación, pendiente de contrato completo.
- recorded_at / recorded_by.
- evidence_id solo como referencia opcional si EVIDENCE_REGISTER puede soportar la afirmación; no sustituye provenance.
- adjudication_id solo si la relación fue adjudicada y el enlace cumple el contrato vigente.

Relaciones candidatas:
- CAUSES: causalidad afirmada y sustentada por DGP/evidencia; nunca derivada solo de tiempo.
- PRECEDES: precedencia parcial, no causal.
- RETRY_OF: intento posterior del mismo acto lógico; ambos eventos son ocurrencias distintas y tipos compatibles.
- DERIVED_FROM: derivación documental/operativa cuyo significado y dirección deben declararse por caso; permanece bloqueada para uso general hasta definir semántica.

Reglas:
1. No autorreferencia.
2. CAUSES y PRECEDES no admiten ciclos.
3. PRECEDES no se deriva automáticamente de timestamps si relojes no son comparables.
4. RETRY_OF exige clave/acto lógico común y regla de orden; unit_id igual no basta.
5. No forzar orden total entre eventos concurrentes.
6. No resolver conflictos por ID, inserción o timestamp.
7. Relaciones de identidad (duplicate/split/merge/retract) no se confunden con CAUSES/PRECEDES/RETRY_OF. Su representación y adjudicación quedan abiertas; no se añaden silenciosamente al enum.
8. El versionado de PROCESS_EVENT_RELATION no hereda DEC-C10-062 y necesita contrato propio antes de implementación.

## 7. PROCESS_EVENT_BINDING: targets tipados

PROCESS_EVENT_BINDING no referencia otras ocurrencias ni snapshots. Las ocurrencias se relacionan mediante PROCESS_EVENT_RELATION; snapshots mediante PROCESS_EVENT_SNAPSHOT_BINDING.

Cada fila contiene binding_record_id, event_record_id exacto, binding_role, target_type cerrado, exactamente una FK tipada no nula y recorded_at/recorded_by.

Targets candidatos:
- NODE.object_record_id;
- EDGE.object_record_id;
- ROUTE.object_record_id;
- PREDICATE.object_record_id.

No hay target genérico target_type + target_id. La FK apunta al registro exacto, no solo al ID semántico. Cuando el contrato del objeto exija snapshot_id + snapshot_object_record_id para su integridad interobjeto, esa integridad se conserva; el binding al objeto no reemplaza el pinning propio de la tabla destino.

### 7.1 Roles y resolución

| binding_role | Target esperado | Regla |
|---|---|---|
| UNIT | NODE | Solo NODE semantic_role=LOGICAL_SERVICE_UNIT y revisión exacta; verificar mapping unit_id↔node |
| ARTIFACT | NODE | Solo si el artefacto está representado como NODE bajo crosswalk aprobado |
| COMPONENT | NODE | Solo si el componente está representado como NODE bajo crosswalk aprobado |
| POLICY_VERSION | NODE o referencia contractual externa tipada | No presumir que B_g0/B_g1 pertenece a NODE; el mapping debe resolverlo |
| PREDICATE_ASSESSMENT | PREDICATE | Referencia a predicado exacto; no copiar truth al evento |
| TRANSFORMATION_INSTANCE | NODE | Solo NODE semantic_role=TRANSFORMATION_EVENT y EID conforme al contrato; no por defecto |

Si B_g0/B_g1 se mantiene como objeto del contrato DGP y no como NODE, su referencia debe ser tipada por policy_contract_id + policy_version y su autoridad/versión declaradas en el mapping DGP. No se inventa una FK U_G ni se crea un NODE artificial. La materialización física de ese tipo externo queda abierta hasta identificar el registro contractual canónico.

Z no es un target de PROCESS_EVENT_BINDING: Z_ASSIGNED es la ocurrencia. El evento Z se vincula a UNIT y, cuando proceda, a la versión de política. POLICY_BOUND separada puede relacionarse con Z mediante PROCESS_EVENT_RELATION solo cuando ambos actos existan y la relación semántica esté definida; no se usa ASSIGNMENT como pseudo-target.

## 8. PROCESS_EVENT_SNAPSHOT_BINDING

Campos: event_record_id exacto; snapshot_id; snapshot_object_record_id; snapshot_relation_role (BEFORE / AFTER / CONTEXT / ROLLBACK_STATE); recorded_at/recorded_by.

Requisitos:
- FK compuesta exacta a SNAPSHOT(snapshot_id, object_record_id), conforme DEC-C10-065.
- snapshot_id y snapshot_object_record_id son obligatorios conjuntamente.
- No latest, timestamp matching, unit_id matching ni proximidad temporal.
- Un snapshot puede contextualizar una ocurrencia sin demostrar causalidad.
- La ausencia de snapshot no niega la ocurrencia.
- BEFORE/AFTER expresan papel contextual adjudicado; no demuestran por sí solos que el evento causó el cambio.
- Si el evento está entre dos snapshots, ambos bindings son filas separadas y exactas.

## 9. Evidencia y DEC-C10-061: dos caminos aún abiertos

EVIDENCE_REGISTER conserva provenance, método, custodian, integridad, observed_at, limitaciones y demás atributos de la fuente. No se copian a PROCESS_EVENT. event_emitter_id no es una fuente probatoria.

DEC-C10-061 mantiene seis destinos tipados: NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT y COVERAGE_SCOPE. Gate 98 **no añade PROCESS_EVENT como séptimo destino**.

**Camino A — destino directo PROCESS_EVENT.** Requeriría enmienda expresa de DEC-C10-061 para CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER, con FK a event_record_id, exclusividad, alcance, cardinalidad y revisión exacta.

**Camino B — destino indirecto existente.** Solo es válido si el objeto ya permitido (p. ej. PREDICATE) representa exactamente la proposición observacional sobre la ocurrencia y existe una relación normalizada, inequívoca y verificable con event_record_id. No es válido esconder una afirmación de evento en notes, texto libre, un NODE irrelevante o coincidencia de ID.

**Dictamen:** la documentación actual no demuestra que B sea suficiente en general ni justifica aún la enmienda global A. La decisión permanece OPEN. Antes de aceptarla se necesita inventariar claims/evaluaciones reales sobre eventos y comprobar caso por caso si ya están representados por PREDICATE u otro destino vigente. No crear tabla puente de evidencia en este gate.

## 10. Cobertura: límite explícito de DEC-C10-070/C0

Gate 96 vinculaba coverage_scope_id opcionalmente a PROCESS_EVENT y PROCESS_EVENT_RELATION. Gate 98 retira ese binding libre.

DEC-C10-070 exige que cada coverage_scope_id C10-S resuelva a una tupla única y exacta:
(contract_id, contract_version, instance_id, instance_version, snapshot_id, snapshot_object_record_id, stage_key, route/route_id, object_class),
con universe_definition/version, regla de enumeración y denominador. C0 es CONDITIONAL y no proporciona FK compuesta física.

Un universo de eventos por tipo/unidad/ventana/fuente no necesariamente posee snapshot exacto, ruta y object_class compatibles con esa tupla. Por ello:
- No se asigna coverage_scope_id a un evento por conveniencia.
- No se crea un scope sin snapshot exacto ni se fuerza SNAPSHOT inexistente.
- No se interpreta un scope estructural C0 como cobertura completa de captura de eventos.
- Si un evento pertenece legítimamente a un scope C0 ya definido, solo se enlaza cuando coincide toda la tupla, incluidos snapshot exacto, stage_key, route y object_class.
- La cobertura de eventos que no pueda expresarse mediante C0 queda NO REPRESENTABLE UNDER CURRENT DEC-C10-070 / OPEN. No se crea EVENT_COVERAGE_REGISTER ni se debilita DEC-C10-070 en este gate.
- La ausencia de fila sigue siendo ? salvo universo temporal, emisores, superficies de captura, retención, sensibilidad de detección y denominador cerrados; no se infiere 0 por silencio.

Se requiere un gate separado para decidir si la cobertura de proceso puede anclarse coherentemente a C0 o si necesita enmienda normativa a DEC-C10-070. No se resuelve por una columna nullable.

## 11. Temporalidad y mapping DGP

Se mantienen separados scheduled_time; event_time / event_start_time / event_end_time; observed_at (EVIDENCE_REGISTER); recorded_at; dgp_time_key; stage_key; SNAPSHOT.phase; k=1…H.

No se convierten unos en otros. stage_key se valida contra DEC-C10-071 y aplicabilidad DEC-C10-083. SNAPSHOT.phase no es stage_key. k=1…H no es reloj.

Cada tiempo conserva fuente, zona/offset o representación normalizada reversible, precisión, clock_domain e incertidumbre cuando sean relevantes. Sin comparabilidad de relojes no se afirma orden temporal.

El mapping event_type↔dgp_time_key↔stage_key↔SNAPSHOT.phase requiere versión, ámbito y fuente contractual. Gate 98 no asigna valores de stage_key a eventos por inferencia. APPLICABLE/NOT_APPLICABLE/UNDETERMINED permanecen distintos.

## 12. Truth, observación y firewalls

- Generator conserva truth completa y potenciales en canal restringido.
- Projector produce únicamente observaciones autorizadas; no completa huecos desde truth.
- Sealer valida allowlist, identidad, tipos, integridad, provenance y referencias; no adjudica causalidad ni repara semántica.
- Analyzer recibe solo eventos observados sellados, evidencia y contratos públicos; no recibe truth, mapping truth↔observación, potenciales ni metadatos reservados.
- Evaluator compara después del sellado truth protegida con salida observada/analizada; no modifica retroactivamente el paquete sellado ni filtra truth al Analyzer.

event_id observado se genera para una ocurrencia proyectada; no reutiliza automáticamente IDs internos del Generator si eso revela eventos no observados o contrafactuales. El mapping truth↔observación queda restringido al Evaluator.

Los estados 1/0/? se adjudican fuera del event log. Un evento observado se registra como ocurrencia; una no ocurrencia no se fabrica como fila. 0 requiere cobertura y evidencia suficientes; en otro caso ?.

## 13. Matriz de requisitos y estado tras Gate 98

| ID Gate 97 | Reconciliación Gate 98 | Estado |
|---|---|---|
| G97-01 | Opción A y B composables, no alternativas excluyentes | Resuelto documentalmente |
| G97-02 | Ciclo de vida de event_id/revisión/corrección/retractación y distinción split/merge | Parcial; relaciones de identidad/adjudicación abiertas |
| G97-03 | Z es ocurrencia; referencias a otras ocurrencias solo por relation exacta | Resuelto en contrato lógico |
| G97-04 | B/version no se presume NODE; binding condicionado a crosswalk DGP/U_G | Abierto hasta mapping |
| G97-05 | DEC-C10-061 sin cambios; caminos A/B explícitos y comparables | Abierto por decisión |
| G97-06 | Retirada cobertura libre; límite C0/DEC-C10-070 declarado | Bloqueado para cobertura de eventos sin snapshot compatible |
| G97-07 | FKs a registros exactos; snapshot FK compuesta | Resuelto a nivel lógico; validación física pendiente |
| G97-08 | Relojes, stage_key, phase y k separados | Parcial; mapping versionado pendiente |
| G97-09 | Matriz event_type × event_result | Parcial; cancelación/desviación requiere crosswalk |
| G97-10 | CAUSES/PRECEDES/RETRY_OF separados; DERIVED_FROM restringido | Parcial; DERIVED_FROM y relaciones de identidad pendientes |
| G97-11 | event_emitter_id separado de provenance/evidence | Resuelto documentalmente |
| G97-12 | Identidad/revisión propia sin heredar DEC-C10-062 | Parcial; constraints y relation revision pendientes |

## 14. Decisiones preservadas

Gate 98 no modifica DEC-C10-060 (16 semantic_role), DEC-C10-061 (seis destinos tipados), DEC-C10-062 (cinco tablas de objetos), DEC-C10-063/064 (Opción A), DEC-C10-065 (snapshot exact pinning), DEC-C10-067 (D2 material policy), DEC-C10-070 (C0 y tupla exacta), DEC-C10-071/083 (stage_key), DEC-C10-088 (ejes temporales/adjudicación), TID/SID/RID/EID, parámetros DGP, estimandos, población, soporte, interferencia, Core TGCV ni firewalls.

## 15. Próximos bloqueos y siguiente gate

1. Crosswalk físico de B_g0/B_g1 y su versión canónica.
2. Mapping de unit_id DGP a NODE LOGICAL_SERVICE_UNIT exacto.
3. Decisión de claims directos/indirectos frente a DEC-C10-061.
4. Representabilidad de cobertura de eventos bajo C0 o necesidad de enmienda DEC-C10-070.
5. Mapping temporal versionado para cada evento realmente usado en D2.
6. Reglas físicas y validador para identidad/revisión/relaciones y append-only.
7. Semántica de split/merge/duplicate/retractation adjudicada.
8. Crosswalk de cancelación, desviación, fallo de asignación y eventos que no llegaron a empezar.
9. Confirmar que las cuatro relaciones propuestas son necesarias y no duplican una relación existente en U_G.

**Siguiente gate propuesto — Gate 99:** resolver el crosswalk D2 de identidad de asignación Z, política B_g0/B_g1 y unidad, reutilizando DEC-C10-067, el DGP Temporal and Role Contract y los artefactos N02/N03 existentes. Determinar si POLICY_BOUND es evento independiente o solo binding de Z_ASSIGNED, y mapear cada target a una clave canónica real. No resolver aún DEC-C10-061 ni DEC-C10-070 por analogía.

## 16. Dictamen y límites

`GATE_98_SUCCESSOR_LOGICAL_CONTRACT_DRAFTED / GATE_96_RECONCILED_PARTIALLY / OPTION_B_NOT_ACCEPTED / DEC_C10_061_UNCHANGED / DEC_C10_062_NOT_INHERITED / DEC_C10_065_EXACT_SNAPSHOT_PINNING / DEC_C10_070_C0_NOT_WEAKENED / EVENT_COVERAGE_WITHOUT_SNAPSHOT_BLOCKED / POLICY_AND_UNIT_BINDINGS_REQUIRE_CANONICAL_CROSSWALK / NO_SCHEMA_CHANGE / NO_CODE_CHANGE / NO_TESTS / NO_EXECUTION / NO_DESIGN_FREEZE`

Auditoría documental asistida; no revisión independiente. No se ejecutaron validadores, parsers, tests, workflows, simulaciones ni experimentos. `scientific_execution=false`; `execution_authorized=false`.
