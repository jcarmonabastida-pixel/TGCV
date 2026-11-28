# C10-S — Gate 94: binding de eventos D2, identidad EID y límite del esquema U_G

**Estado:** EVENT SEMANTICS DISAMBIGUATED / EID SCOPE RESTRICTED / EXISTING U_G INSUFFICIENT FOR ALL D2 PROCESS EVENTS / MINIMAL EXTENSION REQUIRED AS DESIGN PROPOSAL / NOT ACCEPTED OR IMPLEMENTED  
**Rama:** `research/c10-s-consolidation-draft`  
**Precedencia revisada:** DEC-C10-060 (aceptación documental del vocabulario semantic_role y raíz lógica); DEC-C10-061…065 (estructura, versionado y pinning); DEC-C10-067 (política D2); DEC-C10-088 (binding temporal); contratos U_G de identidad/matching y plantilla de inventario; DGP Temporal and Role Contract; Gate 93.  
**Alcance:** resolver la semántica de cada evento D2 y la correspondencia admisible con NODE, TRANSFORMATION_EVENT/EID, SNAPSHOT y registros de evidencia. Identificar la extensión mínima si el esquema no cubre eventos no transformacionales. No alterar DEC, no cambiar el vocabulario aceptado, no crear tablas ni implementar.

## 1. Dictamen ejecutivo

El esquema U_G actual **no permite representar de forma íntegra y no ambigua todos los eventos de proceso D2**.

Sí permite:
- representar B como definición/política versionada y su realización material como objeto de proceso, sin colapsar la política asignada con sus resultados;
- representar un intento efectivo de transformación mediante NODE semantic_role=TRANSFORMATION_EVENT y EID cuando el acto intentado sea realmente una transformación concreta conforme a C10-S-ID-MATCH-001;
- representar estados observados de recepción, instalación y verificación mediante SNAPSHOT/NODE/PREDICATE y evidencia enlazada.

No permite, sin ampliar o reinterpretar contratos:
- representar W_programmed como evento concreto de transformación: es programación/intención procedimental, no intento efectivo ni transformación;
- representar receipt como evento de recepción con identidad propia: recibir un artefacto no es necesariamente transformación;
- representar todo W_attempt bajo EID: algunos intentos de despliegue/configuración sí pueden ser intentos de transformación; otros son operaciones técnicas que no satisfacen automáticamente la definición de EID;
- representar de forma general el evento de asignación Z como TRANSFORMATION_EVENT: asignar una política no transforma por sí mismo el sistema.

Por tanto, **EID no debe ampliarse silenciosamente** para significar cualquier evento operativo. El crosswalk histórico N02→TRANSFORMATION_EVENT y la expresión de Gate 93 “N02/N03 distinguen Z y B” requieren esta precisión: N02 identifica la asignación Z como elemento del modelo causal, pero la asignación no es por ello una transformación. El semantic_role describe el tipo real del registro, no el nombre del rol de catálogo.

## 2. Criterios semánticos vinculantes

1. **Política no es evento:** B_g0/B_g1 es una definición/protocolo de política; la asignación de Z elige una política. La recepción o cumplimiento no redefine la política asignada.
2. **Programación no es intento:** W_programmed registra que la política programó un intento; W_attempt registra que el intento comenzó efectivamente. La primera no prueba la segunda.
3. **Intento no es éxito:** W_attempt no prueba recepción, instalación ni C_dep*.
4. **Recepción no es instalación:** receipt acredita disponibilidad/entrega del artefacto en un destino identificado; S_install acredita el acto/estado de instalación. Son etapas distintas.
5. **Instalación no es C_dep*:** C_dep* exige verificación separada de instalación, integridad, compatibilidad y operatividad.
6. **EID no es un ID genérico de evento:** según C10-S-ID-MATCH-001, EID identifica una aplicación o intento concreto de transformación sobre una unidad y tiempo. No se asigna a toda asignación, programación, entrega, medición o registro administrativo.
7. **Snapshot no es un event log:** SNAPSHOT fija estado observado y pertenencia exacta de objetos en una fase; no sustituye la identidad ni el timestamp del evento que produjo ese estado.
8. **Evidence no es el evento:** EVIDENCE_REGISTER describe la fuente/procedencia que respalda una afirmación. CLAIM_EVIDENCE_LINK enlaza la evidencia con la afirmación/objeto. No usar EVIDENCE_REGISTER como sustituto de un registro de evento.
9. **Tiempo:** event_time (ocurrencia efectiva), scheduled_time (programación prevista), observed_at (captura/observación), recorded_at/created_at (incorporación al registro) y valid-time no se colapsan. stage_key, t0…t9, SNAPSHOT.phase y k=1…H se enlazan explícitamente conforme a DEC-C10-088.
10. **Fallo/ausencia:** un evento programado sin intento efectivo se conserva como programación con intento ausente/negativo solo si existe evidencia suficiente; falta de registro mantiene ?. No convertir MISSING en 0.

## 3. Crosswalk evento por evento

| Objeto D2 | Naturaleza | Registro U_G actual admisible | Identidad/tiempo | Estado |
|---|---|---|---|---|
| Asignación Z | Decisión/asignación causal | NODE N02 solo como registro de asignación si el esquema físico admite ese tipo; no TRANSFORMATION_EVENT por defecto | Identidad de asignación distinta de TID/SID/RID/EID; tiempo de asignación explícito | PARCIAL: N02 existe en catálogo, tipo físico de evento no resuelto |
| B_gZ / policy version | Especificación de política/procedimiento | NODE TRANSFORMATION_SPEC solo si B define una transformación; en otro caso el registro de política/proceso N03 y su contract_intent; no AUTHORIZATION_POLICY salvo autorización real | policy_id/version + artefacto/version cuando aplique; no confundir con asignación ni cumplimiento | DOCUMENTAL; binding físico parcial |
| W_programmed | Programación de un intento | No encaja en TRANSFORMATION_EVENT/EID por sí sola. N03/contract_intent identifica política, no la ocurrencia individual programada | Requiere identidad de evento de proceso y scheduled_time; enlazado a Z/B/unidad/artefacto | AUSENTE COMO EVENTO |
| W_attempt | Inicio efectivo de intento | NODE TRANSFORMATION_EVENT/EID solo cuando el intento sea una aplicación concreta de una transformación identificada por TID/SID/RID; en otro caso no cabe sin evento de proceso genérico | event_time, unidad, run, Z/B, artefacto y etapa; identidad única de intento/reintento | CONDICIONAL; no materializado |
| receipt | Recepción/entrega del artefacto | SNAPSHOT puede evidenciar el estado recibido; EVIDENCE_REGISTER/CLAIM_EVIDENCE_LINK puede respaldar recepción. Ninguno representa por sí solo el evento de recepción | Requiere event identity y received_at separado de observed_at; artifact/version y destino | ESTADO EVIDENCIABLE; EVENTO AUSENTE |
| S_install | Operación/estado de instalación | TRANSFORMATION_EVENT/EID si la instalación es una transformación concreta; NODE técnico + SNAPSHOT post-B + PREDICATE para estado verificado | evento de instalación separado de snapshot de resultado; instalación parcial/fallida/rollback | CONDICIONAL; no materializado |
| C_install/C_integrity/C_compat/C_oper | Predicados/constructos de verificación | PREDICATE + EVIDENCE_REGISTER/CLAIM_EVIDENCE_LINK + COVERAGE_REGISTER | predicate_id, objeto/version, snapshot exacto, stage/time, regla y adjudicación | REUTILIZACIÓN DIRECTA DOCUMENTAL |
| C_dep* | Constructo compuesto | N08/ANALYTIC_CONSTRUCT y regla de derivación; no un evento ni componente | Potenciales en DGP_TRUTH_SECURE; observed_state por predicados visibles, agregación trivalente | REUTILIZACIÓN DOCUMENTAL; regla/instancias abiertas |
| A_f*, App_f, D_f* | Constructos/predicados analíticos | N09/ANALYTIC_CONSTRUCT + PREDICATE; D_f requiere snapshots basales/post comparables | Basal pre-Z y post-B con matching exacto; no se deduce de EID o C_dep | REUTILIZACIÓN DOCUMENTAL; mapping abierto |

## 4. Reconciliación de identidades

### 4.1 Identidades que se conservan

- TID/SID/RID/EID mantienen sus significados en C10-S-ID-MATCH-001.
- EID se asigna solo a una instancia/intent concreto de transformación, con TID/SID/RID aplicables y unidad/tiempo.
- object_record_id/object_version/supersedes_record_id conservan el ámbito definido para NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT. No convierten un registro versionado en identidad de evento.
- snapshot_id/snapshot_object_record_id fijan el snapshot semántico y su revisión exacta conforme a DEC-C10-065.
- policy_id/version, assignment_id, attempt_id y receipt_id son identidades de proceso propuestas para distinguir objetos que no son transformaciones; no se reutilizan TID/SID/RID/EID por conveniencia.

### 4.2 Repetición, reintentos y rollback

Cada intento efectivo tiene identidad distinta, aunque use el mismo artefacto/RID. Reintento no es una nueva política ni una nueva asignación Z. Rollback es un evento/operación posterior y un estado de snapshot diferenciado; no borra el intento previo. Si un evento es revisión/corrección del registro, object_version/supersedes_record_id se aplican según su contrato, no como sustituto de attempt_id.

## 5. Extensión mínima necesaria — propuesta, no decisión

La brecha no se resuelve creando un segundo catálogo de transformación ni ampliando EID indiscriminadamente. La opción de menor impacto a evaluar en el siguiente gate es **extender el modelo de registros U_G existente para admitir eventos de proceso no transformacionales**, manteniendo NODE/SNAPSHOT y los registros de evidencia actuales.

La extensión candidata deberá:
1. introducir un tipo semántico explícito para evento operativo/procedimental no transformacional (p. ej. `OPERATIONAL_EVENT`), sin modificar el significado de TRANSFORMATION_EVENT;
2. proporcionar una identidad de evento propia y opaca (p. ej. `process_event_id`), distinta de EID, object_record_id y snapshot_id;
3. registrar `event_type` en un vocabulario acotado (asignación, programación, intento operativo, recepción, instalación, rollback, etc.) y `event_time`/scheduled_time según corresponda;
4. enlazar cada evento a unit_id, run/scenario, assignment Z, policy_id/version, artefacto/RID y eventos predecesores cuando existan;
5. enlazar stage_key, t0…t9, SNAPSHOT exacto y ventana mediante referencias explícitas; no inferirlos;
6. conservar observed_state/evidence_status/coverage_status y provenance mediante los registros U_G existentes, sin insertar truth DGP en el registro visible;
7. conservar inmutabilidad, append-only, reintentos, eventos fallidos, desviaciones y rollback.

Esta extensión debe realizarse dentro de los registros/relaciones U_G ya gobernados, preferiblemente mediante ampliación acotada de NODE y sus claves/FKs solo si el análisis físico demuestra que la semántica de NODE admite eventos. Si NODE representa exclusivamente entidades versionadas dentro de SNAPSHOT y no admite ocurrencias temporales, el gate debe comparar una extensión relacional mínima frente a la creación de una tabla separada y justificar la opción. **No se selecciona todavía una de las dos alternativas.**

No se aprueba aquí el nombre OPERATIONAL_EVENT, process_event_id, event_type, columnas, claves, FKs, tabla, enum, DDL ni cambios al vocabulario. Son requisitos para la decisión de diseño, no un esquema aprobado.

## 6. Reglas de binding temporal D2

Cada ocurrencia, cuando el contrato esté aprobado, deberá llevar explícitamente:
- unit_id y unidad causal;
- scenario_id/run_id y versión del DGP;
- assignment_id, Z y policy_id/version;
- event identity/type;
- scheduled_time cuando exista;
- event_time cuando haya ocurrido;
- observed_at y recorded_at por separado;
- stage_key DGP;
- snapshot_id + snapshot_object_record_id de estado previo/posterior cuando corresponda;
- TID/SID/RID/EID solo si la ocurrencia es realmente una transformación;
- artifact_id/version/hash y actor/recipient cuando proceda;
- event_status y motivo de UNKNOWN/FAIL/PARTIAL;
- evidence_ref(s), coverage_scope_id y adjudication refs.

La correspondencia temporal se valida contra DEC-C10-088. t0…t9 no son timestamps; stage_key no sustituye event_time; SNAPSHOT.phase no prueba por sí sola el stage; k=1…H pertenece a la ruta hipotética, no al reloj del evento de provisión.

## 7. Consecuencias para Generator, Projector, Sealer, Analyzer y Evaluator

- **Generator:** debe producir la truth de asignación, programación, intento, recepción, instalación y potenciales/estados técnicos como objetos separados. Los parámetros permanecen abiertos.
- **Projector:** solo proyecta observaciones autorizadas; una fila de evento no expone potenciales ni resultados contrafactuales.
- **Sealer:** valida identidad, tipos, referencias exactas, temporalidad, inmutabilidad y procedencia. No convierte falta de evidencia en 0.
- **Analyzer:** recibe eventos/estados observados y predicados con UNKNOWN explícito; permanece ciego a Z/B si así lo exige el contrato de análisis.
- **Evaluator:** compara observaciones con truth segregada y adjudica cobertura/errores después del sellado.
- **Evidence/Coverage:** EVIDENCE_REGISTER y COVERAGE_REGISTER conservan su función epistémica; no sustituyen el ledger de eventos.

La cadena causal D2 y su first stage no se pueden estimar hasta que la representación y la generación de estos objetos estén implementadas y validadas.

## 8. Corrección de crosswalk anterior

El crosswalk de Gate 93 se conserva como reconstrucción de reutilización documental, pero se restringe su lectura:
- N02 representa el rol causal de asignación Z, no prueba que Z sea una transformación ni que deba recibir EID.
- N03 representa política/proceso B; no autoriza colapsar B asignada, W_programmed, W_attempt y receipt.
- El crosswalk N02→TRANSFORMATION_EVENT del contrato semantic_role es una correspondencia candidata que requiere corrección/decisión: entra en tensión con la definición de TRANSFORMATION_EVENT y de EID. No se modifica el contrato aceptado sin decisión explícita.
- La frase de Gate 93 “N02/N03 distinguen Z y B” se mantiene solo en el nivel de catálogo causal, no como binding físico resuelto.

## 9. Dictamen y siguiente gate

**Gate 94 cerrado como análisis semántico y de suficiencia del esquema; no cierra el diseño físico.**

Dictamen:
`GATE_94_D2_EVENT_SEMANTICS_DISAMBIGUATED / EID_RESTRICTED_TO_TRANSFORMATION_INSTANCE / W_PROGRAMMED_NOT_TRANSFORMATION_EVENT / RECEIPT_EVENT_NOT_REPRESENTED / W_ATTEMPT_EID_CONDITIONAL_ON_TRANSFORMATION_SEMANTICS / SNAPSHOT_AND_EVIDENCE_NOT_EVENT_SUBSTITUTES / U_G_INSUFFICIENT_FOR_ALL_PROCESS_EVENTS / MINIMAL_EVENT_EXTENSION_REQUIRED_AS_PROPOSAL / N02_TRANSFORMATION_EVENT_CROSSWALK_CONFLICT_RECORDED / NO_DECISION_CHANGE / NO_CODE_CHANGE / NO_EXECUTION / NO_DESIGN_FREEZE`.

**Siguiente operación — Gate 95:** comparar de forma cerrada las dos alternativas de extensión (NODE ampliado vs. relación/event register mínimo integrado en U_G), verificar la semántica de las claves y FKs existentes y decidir cuál conserva mejor identidad, temporalidad, snapshots y evidencia sin contaminar el inventario estructural. Preparar una propuesta de decisión explícita, sin modificar DEC-C10-060 ni el vocabulario aceptado y sin implementación.
