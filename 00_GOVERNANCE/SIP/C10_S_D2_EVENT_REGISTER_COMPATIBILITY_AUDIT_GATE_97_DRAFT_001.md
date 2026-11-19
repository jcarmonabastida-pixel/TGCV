# C10-S — Gate 97: auditoría de compatibilidad del registro de eventos D2 con U_G

**Estado:** DOCUMENTARY COMPATIBILITY AUDIT / GATE 96 PARTIALLY COMPATIBLE / MATERIAL CONTRACT GAPS IDENTIFIED / NO ACCEPTANCE / NO SCHEMA CHANGE / NO IMPLEMENTATION / NO EXECUTION  
**Rama:** `research/c10-s-consolidation-draft`  
**Fecha:** 2026-11-15  
**Precedencia:** DEC-C10-060…067; DEC-C10-061 typed-target and canonical provenance; DEC-C10-062 object identity/version/supersession; DEC-C10-063/064 U_G Option A; DEC-C10-065 exact snapshot pinning; DEC-C10-070 coverage-scope binding control; DEC-C10-071 stage_key vocabulary; DEC-C10-083 stage applicability; DEC-C10-088 temporal adjudication; Gates 92–96; U_G Inventory Register Template §§1–19; typed-target contract; record identity/version/supersession contract; evidence/provenance/adjudication protocol; DGP Temporal and Role Contract.
**Alcance:** auditar campo, identidad, cardinalidad, FK, relación temporal, evidencia, cobertura y firewall del contrato lógico de Gate 96 frente a los contratos existentes. Determinar compatibilidad, duplicación y brechas; proponer correcciones mínimas. No aceptar B, no reabrir decisiones aceptadas, no cambiar la plantilla física, no implementar, no ejecutar ni congelar.

---

## 1. Dictamen ejecutivo

Gate 96 desarrolló una propuesta lógica útil, pero **no es todavía directamente implementable sin correcciones**. Se confirma compatibilidad de su separación semántica principal con U_G, pero se identifican incompatibilidades y omisiones en la identidad/revisión, bindings, cobertura, evidencia directa, temporalidad y relación con el catálogo N02/N03.

**Hallazgo arquitectónico principal:** DEC-C10-063/064/065 (Opción A) y la alternativa B de Gate 95 no son alternativas mutuamente excluyentes. Opción A gobierna la representación/versionado de NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT y su grafo estructural. B propone un registro separado para ocurrencias de proceso. La combinación coherente es: mantener Opción A intacta y añadir, si se acepta posteriormente, un registro relacional de eventos fuera del inventario NODE y del grafo T_acc/Reach.

### Resultado por dimensión

| Dimensión | Dictamen |
|---|---|
| Separación evento/objeto estructural | COMPATIBLE |
| EID y semantic_role cerrado | COMPATIBLE CON CORRECCIÓN DE BINDINGS |
| Identidad event_id / record_id | PARCIAL; colisión conceptual con revisión no resuelta |
| Aplicación de DEC-C10-062 | INCOMPATIBLE SI SE HEREDA; Gate 96 evita correctamente herencia automática |
| Catálogo de diez event_type | PARCIAL; algunos tipos no separan programación, acto y resultado de forma suficiente |
| PROCESS_EVENT_RELATION | PARCIAL; modelo de relaciones necesita identidad/target exactos y reglas de causalidad |
| PROCESS_EVENT_BINDING | INCOMPATIBLE EN SU ESTADO ACTUAL con el crosswalk N02/N03 y sin targets para Z/eventos |
| Snapshot binding | COMPATIBLE CON DEC-C10-065 si se usa FK compuesta exacta |
| Evidencia directa de eventos | BLOQUEADO por DEC-C10-061 hasta decisión expresa |
| Cobertura | INCOMPATIBLE/INCOMPLETO respecto de DEC-C10-070 y C0 |
| Temporalidad | PARCIAL; ejes correctos, mapping y campos de reloj insuficientes |
| Truth/observación firewall | COMPATIBLE COMO PRINCIPIO; controles de proyección incompletos |
| Reutilización de U_G | COMPATIBLE si se corrigen bindings y se evita duplicar provenance/cobertura |

**Disposición:** Gate 96 no se acepta ni se descarta globalmente. Se conserva como contrato candidato sujeto a las correcciones de §10. B sigue siendo recomendación de Gate 95, no decisión adoptada.

## 2. Regla de reconciliación: Opción A y B se componen

DEC-C10-063 acepta Opción A para la pertenencia a snapshots y referencias versionadas de los objetos estructurales. DEC-C10-064 aprueba la resolución de relaciones entre NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT y ROUTE_STEP. DEC-C10-065 exige pinning exacto de la revisión de SNAPSHOT.

Estas decisiones no autorizan introducir ocurrencias de provisión como NODE. Tampoco impiden un registro de eventos separado.

La arquitectura compatible debe conservar:

- NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT y ROUTE_STEP para objetos estructurales, estados, relaciones, rutas y predicados.
- PROCESS_EVENT (si B se acepta) para ocurrencias temporales de proceso.
- PROCESS_EVENT_RELATION (si se acepta) para relaciones entre ocurrencias.
- Relaciones tipadas de binding a objetos estructurales, eventos y snapshots, con destino exacto.
- EVIDENCE_REGISTER y CLAIM_EVIDENCE_LINK para procedencia y soporte de afirmaciones.
- COVERAGE_REGISTER para universo y cobertura.
- DGP_TRUTH_SECURE segregado.

No se crea una segunda arquitectura de snapshots, evidencia o cobertura. No se modifica semantic_role ni se fuerza event_id a EID.

## 3. Auditoría de identidad y versionado

### 3.1 Identidades que no deben colapsarse

Gate 96 propone event_id, event_record_id y event_revision. Es correcto separar ocurrencia de fila de registro, pero falta reconciliar la terminología y el ciclo de vida con DEC-C10-062.

DEC-C10-062 limita expresamente object_record_id/object_version/supersedes_record_id a NODE, EDGE, ROUTE, PREDICATE y SNAPSHOT. No se extiende automáticamente a nuevos registros. Por tanto:

- No se denomina object_record_id al identificador de fila de PROCESS_EVENT.
- No se denomina object_version a la revisión de un evento.
- No se reutiliza supersedes_record_id como si la fila de evento fuera una de las cinco tablas de objetos.
- La revisión del registro de evento requiere contrato propio y explícito.
- event_id no puede ser event_record_id ni EID.
- EID permanece reservado a la identidad de una aplicación/intento concreto de transformación conforme a C10-S-ID-MATCH-001.

### 3.2 Brecha en Gate 96: identidad estable frente a revisión de observación

Gate 96 afirma que event_id es la identidad estable de una ocurrencia, y event_record_id/event_revision identifican revisiones inmutables. Pero no define con precisión si una revisión corrige:

(a) un error de captura/registro sobre la misma ocurrencia;  
(b) una nueva observación de la misma ocurrencia por una fuente distinta;  
(c) un cambio en la adjudicación del estado de esa ocurrencia; o  
(d) una corrección semántica que revela que eran dos ocurrencias distintas.

DEC-C10-062 separa revisión observacional de cambio semántico y exige que un cambio material de identidad no se disfrace como revisión. El contrato de eventos debe hacer lo mismo.

**Corrección mínima:** distinguir explícitamente:
- occurrence identity: event_id;
- event-record revision: event_record_id + event_revision + supersedes_event_record_id propio del registro de eventos;
- evidence identity: evidence_id, una o varias fuentes;
- adjudication identity: adjudication_id y sus evaluaciones;
- transformation identity: EID únicamente cuando aplique.

Una nueva fuente que confirma el mismo hecho no debe generar automáticamente nueva ocurrencia ni revisión del evento: puede generar nueva evidencia. Una adjudicación diferente no reescribe la ocurrencia; se registra en el mecanismo de adjudicación. Una corrección de los atributos capturados de la ocurrencia sí genera una nueva revisión append-only. Si se descubre que dos supuestos eventos eran uno, o uno eran dos, se requiere una relación explícita de identidad/duplicidad/retractación y adjudicación; no se fuerza una cadena de supersession.

### 3.3 Constraints pendientes

La cadena propuesta en Gate 96 necesita reglas ejecutables/documentales precisas para:
- una sola raíz de revisión;
- sucesor inmediato único;
- misma identidad event_id en la cadena;
- revisión contigua;
- ausencia de ciclos, huérfanos y bifurcaciones;
- inmutabilidad real de revisiones;
- corrección de un event_id que luego se demuestra erróneo sin borrar el historial.

No basta UNIQUE(event_id,event_revision) y FK de supersession. El contrato de eventos debe declarar además la política de duplicados, retractación y split/merge de ocurrencias.

**Dictamen identidad:** PARCIAL. Se conserva el diseño de tres identidades como candidato, sujeto a estas precisiones. No heredar DEC-C10-062.

## 4. Auditoría de N02/N03, Z y B

Gate 94 corrigió expresamente la lectura del crosswalk histórico: N02 identifica el rol causal de asignación Z, pero no demuestra que la asignación sea TRANSFORMATION_EVENT ni que deba recibir EID. N03 identifica política/proceso B; no permite colapsar política asignada, programación, intento y recepción.

Gate 96 introduce Z_ASSIGNED y POLICY_BOUND como tipos de PROCESS_EVENT, pero su PROCESS_EVENT_BINDING solo dispone de destinos NODE/EDGE/ROUTE/PREDICATE y sus roles candidatos incluyen UNIT, POLICY_VERSION, ARTIFACT, COMPONENT, TRANSFORMATION_INSTANCE y PREDICATE_ASSESSMENT. No define un binding físico suficiente para el evento de asignación Z ni para enlazar una ocurrencia con otra ocurrencia.

Consecuencias:

1. N02/N03 son roles del catálogo/crosswalk, no PK ni FK físicas por sí mismos.
2. La asignación Z es una ocurrencia de proceso si B se acepta; no se debe materializar como NODE artificial solo para hacer posible una FK.
3. B_g0/B_g1 es definición/version de política/proceso según el contrato de dominio; no se debe clasificar automáticamente como TRANSFORMATION_SPEC ni AUTHORIZATION_POLICY. Debe resolverse contra el tipo real y el crosswalk aprobado.
4. POLICY_BOUND no debe sustituir ni duplicar la asignación Z; expresa una vinculación de una versión exacta de política a una unidad/asignación cuando el DGP la requiere.
5. W_programmed, W_attempt, receipt, S_install y rollback son ocurrencias distintas cuando los actos se producen; no se derivan de la mera presencia de N03.
6. Un evento puede referenciar otro evento mediante PROCESS_EVENT_RELATION; no debe inventarse un NODE de asignación o un EDGE estructural para resolverlo.

**Corrección mínima:** reemplazar el binding ROLE=ASSIGNMENT como binding implícito no definido por un binding tipado a la ocurrencia Z (target_process_event_record_id) o por PROCESS_EVENT_RELATION cuando se trate de una relación entre ocurrencias. Añadir un target tipado para PROCESS_EVENT únicamente a la relación de binding de eventos si la tabla y el caso de uso lo requieren. No introducir event_id como target sin fijar una revisión exacta cuando la afirmación se refiere a una fila observada concreta.

## 5. Auditoría de PROCESS_EVENT_BINDING y snapshots

### 5.1 Bindings estructurales

La relación de bindings de Gate 96 propone cuatro destinos: NODE, EDGE, ROUTE y PREDICATE; los snapshots se separan en PROCESS_EVENT_SNAPSHOT_BINDING. Es una separación defendible, pero el contrato debe especificar si las FKs referencian:
- el ID semántico;
- object_record_id de la revisión concreta;
- o ambas identidades con clave compuesta.

Por coherencia con DEC-C10-061/062, un binding que afirma «este evento se refiere a este componente/artefacto/predicado concreto» debe apuntar a la revisión exacta del registro de destino, no a una identidad semántica ambigua ni a latest.

No se debe añadir una FK genérica target_type + target_id. Las FKs deben ser tipadas y cada fila debe poblar exactamente un destino cuando el binding sea de destino único. Si un evento se vincula a múltiples objetos, usa varias filas.

### 5.2 Snapshots

DEC-C10-065 requiere la pareja (snapshot_id, snapshot_object_record_id) y FK compuesta al registro exacto SNAPSHOT(snapshot_id, object_record_id). Gate 96 recoge esta regla.

Correcciones requeridas:
- PROCESS_EVENT_SNAPSHOT_BINDING debe referenciar ambos campos y la clave candidata compuesta exacta.
- La revisión de SNAPSHOT no se resuelve por timestamp, última versión, event_time ni proximidad.
- BEFORE/AFTER/CONTEXT/ROLLBACK_STATE son roles candidatos de relación, no valores que prueben por sí mismos una secuencia causal.
- Un snapshot puede documentar el estado antes/después de un evento, pero no demuestra que ese evento haya causado el cambio.
- Un evento puede carecer de snapshot; la falta de snapshot limita la afirmación estructural que puede sostenerse, no niega automáticamente la ocurrencia.

**Dictamen snapshots:** COMPATIBLE CON CORRECCIÓN DE CLAVE COMPUESTA Y REGLA NO CAUSAL.

## 6. Auditoría de DEC-C10-061 y evidencia

DEC-C10-061 acepta seis destinos tipados para CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER: NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT y COVERAGE_SCOPE. La evidencia se referencia por evidence_id y su procedencia canónica permanece en EVIDENCE_REGISTER. No hay un destino PROCESS_EVENT aceptado.

Gate 96 propone una séptima FK target_process_event_record_id y ampliar claim_target_type. Eso es una **enmienda normativa**, no una simple implementación técnica. No puede aplicarse por analogía ni por modificación unilateral del contrato.

Se detecta además que event_record_id no está bajo el contrato de unicidad de object_record_id por tabla. La enmienda debe fijar expresamente PK/UNIQUE de event_record_id y FK destino, sin llamarlo object_record_id ni ampliar el ámbito de DEC-C10-061 por implicación.

### 6.1 Dos caminos admisibles, decisión abierta

**Camino A — claims directos sobre eventos.** Enmendar expresamente DEC-C10-061 para añadir PROCESS_EVENT como séptimo destino tipado en CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER, con FK a event_record_id, exclusividad de destino, cardinalidad y alcance. El vínculo debe fijar una revisión concreta.

**Camino B — afirmación indirecta.** No ampliar destinos. Solo es admisible si el contrato identifica qué objeto ya permitido soporta la afirmación y establece una relación normalizada inequívoca desde ese objeto hasta event_record_id. No es admisible atribuir a un NODE/PREDICATE una afirmación sobre un evento que ese objeto no representa. Tampoco basta un campo notes o un event_id en texto libre.

La elección debe basarse en el uso real de afirmaciones y evaluaciones sobre eventos. Gate 96 propone A, pero no demuestra todavía que B sea insuficiente para todos los claims.

### 6.2 Procedencia

No copiar a PROCESS_EVENT source_provenance, custodian, collection_method, tool_version, integrity, access_lineage ni completeness_limitations. Esos datos pertenecen a EVIDENCE_REGISTER. event_source_id puede identificar el emisor/origen operativo de la ocurrencia, pero no sustituye la procedencia probatoria de la fuente que respalda una afirmación.

**Dictamen evidencia:** REUTILIZACIÓN CANÓNICA CONFIRMADA; destino directo PROCESS_EVENT bloqueado hasta decisión.

## 7. Auditoría de cobertura y DEC-C10-070

Gate 96 incluye coverage_scope_id opcional en PROCESS_EVENT y PROCESS_EVENT_RELATION. Esto no es suficiente para afirmar que el registro cumple el contrato de cobertura.

DEC-C10-070/C0 exige que un coverage_scope_id resuelva a una tupla versionada y no ambigua que incluye contract/version, instance/version, snapshot_id, snapshot_object_record_id, stage_key, route_id y object_class, además de coherencia de consumidores, universo y denominador.

La auditoría del protocolo C0 identifica expresamente que stage_key no es una columna canónica del esquema U_G y que SNAPSHOT.phase no es equivalente a stage_key. También exige crosswalk explícito de object_class y ruta; no se permite inferirlos de semantic_role, predicate_type o texto libre.

Un evento de proceso puede ocurrir entre snapshots, antes de la captura o sin snapshot asociado. Por tanto, no debe asignársele automáticamente un coverage_scope_id cuyo universo requiera un snapshot concreto, ni inventar snapshot_id para satisfacer C0.

**Brecha material:** Gate 96 no define una dimensión de cobertura de eventos, ni cómo un evento temporal se vincula a un scope C0 con snapshot exacto, ni cómo se expresa el universo esperado de eventos por unidad/ventana/fuente sin falsear la tupla.

Corrección mínima:
1. No asumir que cualquier coverage_scope_id es válido para eventos.
2. Reutilizar COVERAGE_REGISTER, pero definir un scope compatible y versionado para eventos, con dimensión y universo explícitos.
3. Resolver expresamente si DEC-C10-070/C0 se amplía para scopes de proceso/eventos sin snapshot, o si el scope de eventos requiere un anclaje de snapshot que tenga sentido para el universo.
4. No debilitar C0 ni usar snapshot latest.
5. Diferenciar cobertura de captura de eventos, cobertura de evidencias y cobertura de objetos estructurales.
6. La ausencia de fila solo puede representar 0 si el universo temporal, fuentes, capacidad de detección y denominador están cerrados; de lo contrario ?.

**Dictamen cobertura:** INCOMPLETO / BLOQUEO DE COMPATIBILIDAD HASTA DISEÑO DE SCOPE.

## 8. Auditoría temporal, stage_key y orden causal

Gate 96 distingue correctamente scheduled_time, event_time, observed_at y recorded_at. También conserva separados dgp_time_key, stage_key, SNAPSHOT.phase y k=1…H, como exige DEC-C10-088.

Sin embargo, faltan decisiones de materialización:
- event_time y start/end necesitan tipo, zona/offset, precisión, clock_domain y regla de incertidumbre compatibles con relojes del DGP.
- recorded_at de una revisión no debe confundirse con created_at de los objetos U_G.
- observed_at pertenece a EVIDENCE_REGISTER; no duplicarlo como columna del evento.
- dgp_time_key debe resolverse contra el vocabulario/version exacto del DGP, no ser texto libre.
- stage_key debe pertenecer al vocabulario cerrado DEC-C10-071 y aplicarse según DEC-C10-083; null requiere razón diferenciando no aplicable de no determinado.
- SNAPSHOT.phase no se convierte en stage_key.
- t0…t9 no son timestamps.
- k=1…H no es reloj de eventos.
- el mapping event_type ↔ dgp_time_key ↔ stage_key ↔ snapshot phase requiere versión, alcance y cardinalidad declarados.

### 8.1 Causalidad

PROCESS_EVENT_RELATION propone CAUSES, PRECEDES, RETRY_OF y DERIVED_FROM. No obstante:
- PRECEDES es orden parcial, no causalidad.
- CAUSES necesita fundamento de DGP o evidencia y no se deduce de timestamps.
- RETRY_OF requiere regla de identidad de operación lógica y compatibilidad de tipo; no basta «mismo unit_id».
- DERIVED_FROM es demasiado amplio si no se define qué objeto deriva de qué acto y con qué semántica.
- Las relaciones deben apuntar a event_record_id exactos, y su revisión/corrección debe conservarse.
- Prohibir ciclos en CAUSES y PRECEDES es razonable, pero el orden parcial y las relaciones concurrentes deben quedar explícitos.
- Un reloj no sincronizado no puede producir precedencia temporal cierta por comparación de timestamps.

**Dictamen temporal:** COMPATIBLE EN PRINCIPIO; mapping y contrato de reloj incompletos.

## 9. Auditoría del catálogo de diez eventos

El catálogo Gate 96 es cerrado como propuesta, pero no está aún reconciliado con el DGP y Gate 95.

| Tipo Gate 96 | Auditoría |
|---|---|
| Z_ASSIGNED | Semánticamente válido como ocurrencia; requiere identidad de asignación y unidad; no EID por defecto |
| POLICY_BOUND | Válido solo si se distingue selección/asignación de política y su binding exacto; no duplicar Z |
| PROVISION_SCHEDULED | Válido; scheduled_time no prueba ocurrencia de intento |
| PROVISION_ATTEMPT_STARTED | Válido; debe tener identidad por intento/reintento |
| PROVISION_ATTEMPT_TERMINATED | Válido; resultado del acto, no del constructo C_dep |
| ARTIFACT_RECEIVED | Válido; debe identificar artefacto/version y destino; no prueba instalación |
| INSTALLATION_STARTED | Válido; operación técnica, EID solo si satisface contrato transformacional |
| INSTALLATION_TERMINATED | Válido; no demuestra C_dep*=1 |
| ROLLBACK_STARTED | Válido como acto separado, si el DGP contempla rollback |
| ROLLBACK_TERMINATED | Válido; no revoca ni elimina los eventos previos |

Brechas:
1. Gate 95 contempla desviaciones/fallos y estado de eventos; Gate 96 los expresa en event_result, pero debe fijar compatibilidad event_type × event_result.
2. No existe un evento «verification succeeded» en el catálogo, lo cual es coherente si la verificación se almacena como predicado/evidencia. Debe declararse explícitamente para evitar que INSTALLATION_TERMINATED se interprete como verificación.
3. POLICY_BOUND y Z_ASSIGNED pueden resultar redundantes según la unidad causal real. Se necesita definir cuándo la asignación Z y la vinculación B son un solo acto, actos distintos o relación entre una asignación y una definición/version de política.
4. La programación puede ser una ocurrencia o un atributo de un plan/orden según el mecanismo del DGP. El catálogo debe representar la semántica real, no forzar un evento si no hay acto de programación individual.
5. Debe aclararse si eventos cancelados antes de empezar son PROVISION_SCHEDULED con resultado CANCELLED, o una ocurrencia de cancelación separada. No inferirlo.

**Dictamen catálogo:** PARCIALMENTE COMPATIBLE; mantener como candidato, no congelar.

## 10. Matriz de correcciones mínimas a Gate 96

| ID | Hallazgo | Corrección mínima | Severidad |
|---|---|---|---|
| G97-01 | Opción A y B pueden leerse como alternativas incompatibles | Declarar su composición: Opción A para grafo estructural, B para ocurrencias | Alta |
| G97-02 | event_id/revisión no cubre duplicidad, split/merge y adjudicación | Definir ciclo de vida y distinguir nueva evidencia, corrección, retractación y nueva ocurrencia | Alta |
| G97-03 | Binding no resuelve N02/Z ni referencia entre eventos | Añadir FK tipada a event_record_id en bindings/relaciones según rol; no crear NODE Z artificial | Alta |
| G97-04 | POLICY_VERSION y N03 no tienen crosswalk físico cerrado | Resolver tipo y clave real de B/version, sin asumir semantic_role | Alta |
| G97-05 | event claims amplían DEC-C10-061 sin decisión | Mantener bloqueado; comparar camino directo vs indirecto y redactar enmienda separada | Alta |
| G97-06 | coverage_scope_id no satisface por sí mismo C0/DEC-C10-070 | Definir universo/dimensión de cobertura de eventos y compatibilidad de snapshot | Alta |
| G97-07 | PROCESS_EVENT_BINDING no declara siempre target record exacto y cardinalidad compuesta | FKs tipadas a registros exactos; snapshot FK compuesta DEC-C10-065 | Alta |
| G97-08 | clock/domain precision y mapping DGP incompletos | Contrato de reloj versionado, stage applicability y mapping DEC-C10-088 | Media |
| G97-09 | event_type × event_result no está cerrado | Matriz de compatibilidad y reglas por tipo | Media |
| G97-10 | DERIVED_FROM ambiguo y RETRY_OF insuficientemente definido | Definir semántica/alcance y reglas de aciclicidad/compatibilidad | Media |
| G97-11 | event_source_id podría duplicar provenance | Separar emisor operativo de evidencia/procedencia | Media |
| G97-12 | event_record_id y event_revision carecen de contrato técnico completo | PK/UK, FK, append-only, revisión lineal, corrección y política de retractación | Alta |

## 11. Propuesta mínima de reconciliación

Se propone mantener las cuatro relaciones lógicas de Gate 96 como **candidatas**, con estos límites:

### PROCESS_EVENT
Solo identidad de ocurrencia, tipo, resultado del acto, unidad/run/replicate conforme a claves reales, tiempo de ocurrencia/programación, stage/time mapping versionado y metadatos mínimos del registro. No copiar procedencia completa ni observed_at.

### PROCESS_EVENT_RELATION
Relaciones entre revisiones exactas de eventos. Causalidad, precedencia y reintento permanecen separados. Las correcciones de relaciones tienen identidad y supersession propios. No convertirlas en EDGE estructural.

### PROCESS_EVENT_BINDING
Bindings tipados a NODE/EDGE/ROUTE/PREDICATE exactos y, si se justifica, a otra revisión de PROCESS_EVENT. Cada fila debe tener exactamente un destino tipado. El binding a unidad debe apuntar al NODE LOGICAL_SERVICE_UNIT exacto conforme al contrato de raíz/unidad; no usar unit_id libre como sustituto de FK.

### PROCESS_EVENT_SNAPSHOT_BINDING
Mantener separada la FK compuesta exacta (snapshot_id, snapshot_object_record_id) y rol temporal. No usar timestamp matching ni causalidad inferida.

### Registros existentes
- EVIDENCE_REGISTER: procedencia canónica.
- CLAIM_EVIDENCE_LINK: soporte de claims, sin ampliación hasta decisión.
- COVERAGE_REGISTER: cobertura; no introducir ledger paralelo.
- EVALUATOR_ASSESSMENT/ADJUDICATION_REGISTER: evaluación/adjudicación; no duplicar.
- DGP_TRUTH_SECURE: truth/potenciales segregados.

No se recomienda añadir ahora un quinto registro ni ampliar NODE/semantic_role.

## 12. Decisiones que NO deben modificarse en Gate 97

- DEC-C10-060: 16 semantic_role cerrados.
- DEC-C10-061: seis destinos tipados vigentes hasta una enmienda aceptada.
- DEC-C10-062: identidad/versionado de las cinco tablas de objetos; no extender automáticamente a PROCESS_EVENT.
- DEC-C10-063/064: Opción A estructural aceptada.
- DEC-C10-065: snapshot exact pinning.
- DEC-C10-070: cobertura C0 y su tupla.
- DEC-C10-071/083: vocabulario y aplicabilidad stage_key.
- DEC-C10-088: separación de relojes/etapas y adjudicación temporal.
- Semantic IDs TID/SID/RID/EID.
- Truth/observation firewall.
- DGP cuantitativo, estimandos, parámetros y Core TGCV.

## 13. Dictamen y siguiente gate

**Gate 97 se cierra como auditoría documental con compatibilidad parcial y brechas materiales identificadas.** No se declara que el contrato de Gate 96 sea implementable todavía.

Dictamen:

`GATE_97_DOCUMENTARY_COMPATIBILITY_AUDIT / GATE_96_PARTIALLY_COMPATIBLE / OPTION_A_STRUCTURAL_AND_OPTION_B_PROCESS_REGISTER_COMPOSABLE / DEC_C10_061_DIRECT_EVENT_TARGET_NOT_ACCEPTED / DEC_C10_062_NOT_INHERITED / DEC_C10_065_EXACT_SNAPSHOT_BINDING_REQUIRED / C0_EVENT_COVERAGE_SCOPE_OPEN / N02_N03_PHYSICAL_BINDING_OPEN / EVENT_IDENTITY_CORRECTION_POLICY_OPEN / NO_SCHEMA_CHANGE / NO_CODE_CHANGE / NO_TESTS / NO_EXECUTION / NO_DESIGN_FREEZE`

**Siguiente operación propuesta — Gate 98:** reconciliación correctiva del contrato lógico Gate 96 frente a Gate 97. Corregir únicamente el contrato lógico, sin crear decisiones ni modificar la plantilla U_G. Resolver primero (i) ciclo de vida event_id/event_record_id/revisión/retractación; (ii) bindings tipados de unidad, Z, B/version, artefacto y eventos; (iii) snapshot exact pinning; (iv) compatibilidad de event_type × event_result y relaciones causales; (v) cobertura de eventos compatible con DEC-C10-070; (vi) dos caminos de evidencia/claim frente a DEC-C10-061, manteniendo la elección abierta. El output debe ser un Gate 96 successor draft corregido y un delta de requisitos, no una aceptación de B.

**Límites:** auditoría documental asistida, no revisión independiente. No se han ejecutado parsers, validadores, tests, workflows, simulaciones ni experimentos. `scientific_execution=false`; `execution_authorized=false`.
