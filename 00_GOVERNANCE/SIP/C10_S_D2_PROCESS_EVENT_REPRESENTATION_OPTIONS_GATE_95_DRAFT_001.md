# C10-S — Gate 95: comparación de alternativas para representar eventos de proceso D2 en U_G

**Estado:** OPTION B RECOMMENDED / INTEGRATED PROCESS-EVENT REGISTER PROPOSAL / NOT ACCEPTED / SCHEMA UNCHANGED / NO IMPLEMENTATION / NO EXECUTION  
**Rama:** research/c10-s-consolidation-draft  
**Precedencia:** DEC-C10-060…067; DEC-C10-061 typed-target contract; DEC-C10-062 record identity/version; DEC-C10-064 structural resolution; DEC-C10-065 exact snapshot pinning; DEC-C10-088 temporal adjudication; Gate 93; Gate 94; U_G inventory template §§2–15; semantic_role/logical-root contract; identity/version/snapshot matching contract; DGP Temporal and Role Contract; VIATRA immutable event schema.  
**Alcance:** comparar (A) ampliar NODE para eventos genéricos de proceso y (B) incorporar un registro relacional de eventos integrado en U_G. Recomendar una arquitectura documental mínima. No aprobar nombres/campos/keys definitivos, no modificar DEC, no cambiar la plantilla, no implementar ni ejecutar.

## 1. Pregunta y criterios de decisión

Gate 94 concluyó que EID no es un identificador genérico: identifica una aplicación/intento concreto de transformación. Z assignment, W_programmed y receipt no son automáticamente transformaciones; W_attempt y S_install solo podrían serlo bajo una especificación transformacional propia. El NODE template tampoco contiene event_time ni stage_key.

La decisión de Gate 95 debe resolver dónde registrar ocurrencias operativas que tienen identidad y tiempo propios, sin:
- redefinir TRANSFORMATION_EVENT/EID;
- contaminar el grafo estructural usado para T_acc/Reach con eventos de proceso;
- duplicar snapshots o el sistema de evidencia;
- inferir el orden o la fase de un evento por timestamps;
- exponer truth/potenciales al Analyzer.

Criterios: fidelidad semántica; identidad de ocurrencia; inmutabilidad/append-only; separación event-time/record-time/observed-time; binding stage_key/t0…t9/SNAPSHOT; pinning exacto DEC-C10-065; integridad referencial; compatibilidad con U_G y DEC-C10-061…065; evidencia/cobertura/adjudicación; firewalls de roles; complejidad y riesgo de duplicación.

## 2. Alternativa A — ampliar NODE con eventos operativos

**Descripción:** añadir un semantic_role de evento operativo no transformacional a NODE y campos específicos para identidad, tipo y temporalidad. Los eventos serían nodos versionados, miembros de un SNAPSHOT exacto, y sus relaciones se expresarían mediante EDGE.

**Ventajas**
- Reutiliza NODE, object_record_id/object_version/supersedes_record_id y las FKs tipadas ya definidas.
- Aprovecha el vocabulario y el grafo U_G sin introducir otra tabla.
- CLAIM_EVIDENCE_LINK puede apuntar a NODE sin ampliar sus destinos tipados.
- Los vínculos a artefactos/unidad podrían expresarse con EDGE si las relaciones y su semántica quedan definidas.
- No se crea un registro separado de ocurrencias.

**Costes y conflictos**
- DEC-C10-060 aceptó un vocabulario cerrado de 16 semantic_role. Un nuevo rol requiere decisión expresa; no se puede introducir silenciosamente.
- NODE es el inventario de objetos/entidades del grafo. Una ocurrencia temporal no es necesariamente un componente o entidad estructural persistente.
- NODE queda fijado a una revisión exacta de SNAPSHOT por DEC-C10-065. Un evento ocurre en event_time y puede preceder a la captura que lo documenta. Su inclusión en el snapshot no convierte el timestamp de captura en tiempo de evento.
- Cada evento pasaría a ser nodo candidato del grafo. Se necesitarían reglas explícitas que impidan tratar nodos/eventos como transformaciones accesibles o pasos de ROUTE, y que los excluyan de T_acc/Reach salvo que el modelo lo justifique.
- EDGE exige extremos del mismo snapshot/revisión. La cadena temporal puede atravesar capturas distintas; no se debe forzar todo el historial dentro de un único snapshot ni debilitar el pinning.
- Los campos de NODE no separan actualmente event_time, scheduled_time, observed_at y recorded_at. Añadirlos aumenta la complejidad condicional de NODE y del validador.
- La identidad NODE (node_id) y la identidad EID tienen semánticas diferentes. Un nuevo rol genérico no debe hacer que node_id se interprete como EID.
- El versionado de fila NODE no equivale a secuencia de ocurrencias: object_version es revisión observacional de la misma entidad, no número de intento/reintento.

**Resultado:** viable solo con una extensión amplia y reglas de exclusión/temporalidad adicionales; alto riesgo de mezclar inventario estructural con eventos.

## 3. Alternativa B — registro de eventos de proceso integrado en U_G

**Descripción:** añadir un registro relacional específico para ocurrencias operativas D2, como extensión normalizada de U_G. No es un segundo sistema de evidencia ni una ontología paralela: es el registro de ocurrencias que falta, conectado por referencias tipadas a NODE/SNAPSHOT/PREDICATE y a los registros existentes de evidencia/cobertura.

**Ventajas**
- Separa ocurrencia/evento de objeto estructural, definición de política, artefacto, transformación y estado observado.
- Conserva TID/SID/RID/EID exclusivamente para transformaciones que satisfagan su contrato.
- Permite identidad de evento para Z, W_programmed, receipt, intentos operativos y rollback sin reinterpretar node_id ni EID.
- Puede distinguir event_time, scheduled_time, observed_at y recorded_at, así como stage_key y t0…t9.
- No convierte eventos de provisión en vértices del grafo T_acc/Reach.
- Mantiene NODE/SNAPSHOT/EDGE/PREDICATE para los estados, artefactos, dependencias y condiciones estructurales.
- Puede enlazar evidencia y cobertura con las tablas existentes, conservando DGP_TRUTH_SECURE fuera del canal observado.

**Costes y conflictos**
- Es una nueva relación/registro dentro de U_G y requiere un contrato de identidad e inmutabilidad propio; DEC-C10-062 no se aplica automáticamente porque limita object_record_id/object_version a NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT.
- DEC-C10-061 define destinos tipados de CLAIM_EVIDENCE_LINK/EVALUATOR_ASSESSMENT/ADJUDICATION_REGISTER como NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT y COVERAGE_SCOPE. Para claims directos sobre eventos habría que ampliar esos destinos mediante decisión y FKs tipadas, o declarar un patrón de evidencia indirecta que no oculte la afirmación sobre el evento.
- Debe decidirse cómo se modelan vínculos tipados a unidad, Z, B/version, artefacto, snapshot pre/post y evento precedente. No basta una columna polimórfica sin integridad.
- El orden causal no puede depender solo de event_time si existen eventos concurrentes, empates, relojes distintos o reintentos; se necesita una regla de orden/causalidad adecuada al DGP.
- La nueva tabla no debe duplicar SNAPSHOT, EVIDENCE_REGISTER, COVERAGE_REGISTER ni ADJUDICATION_REGISTER.
- Debe existir un firewall claro entre truth de Generator, observaciones proyectadas y evaluación posterior.

**Resultado:** mayor explicitud semántica y mejor separación estructural/temporal, a cambio de una extensión de esquema y contratos referenciales explícita.

## 4. Comparación resumida

| Criterio | A — NODE ampliado | B — registro de eventos integrado |
|---|---|---|
| Identidad de ocurrencia no transformacional | Requiere nuevo semantic_role y node_id por ocurrencia; semántica mezclada | Identidad de evento propia |
| Conservación del significado EID | Riesgo de confundir node_id/EID | EID opcional solo para eventos transformacionales |
| Separación estructural vs. temporal | Baja: evento pasa a ser NODE del grafo | Alta: ocurrencia separada del inventario estructural |
| Snapshot exact pinning | Obligatorio para cada evento-node; puede forzar asociación artificial | Referencias exactas a snapshots pre/post cuando correspondan |
| event_time/stage_key | Añadidos condicionales a NODE | Campos nativos del registro de evento |
| Orden/reintentos | Mezclados con object_version, que no es secuencia de eventos | Identidad/orden de ocurrencia separados de revisión de registro |
| FKs a unidad/Z/B/artefacto | EDGE con mismos snapshot constraints; potencialmente forzado | Relaciones tipadas diseñadas para evento |
| Evidencia y claims | Reutiliza destinos NODE actuales | Requiere extender destinos tipados para claims directos sobre eventos |
| Cobertura | Riesgo de mezclar cobertura del grafo con eventos | Scope de cobertura de eventos separado |
| Riesgo de contaminar T_acc/Reach | Alto sin filtros y reglas adicionales | Bajo por separación de registros |
| Impacto en contratos aceptados | Cambia vocabulario cerrado DEC-C10-060 | Amplía U_G y posiblemente DEC-C10-061; no cambia semantic_role |
| Duplicación | No añade tabla, pero sobrecarga NODE | Una tabla nueva, pero con separación funcional explícita |

## 5. Recomendación

**Recomendar B: registro relacional de eventos de proceso integrado en U_G**, no un event store externo/paralelo.

Razón principal: los eventos D2 son ocurrencias temporales con identidad propia; no son necesariamente entidades estructurales versionadas ni transformaciones. U_G ya separa objetos estructurales (NODE/EDGE/ROUTE/PREDICATE), snapshots, evidencia y cobertura. Un registro de eventos completa esa arquitectura sin convertir cada intento/recepción/asignación en vértice del grafo.

La alternativa B preserva:
- semantic_role de 16 valores sin alteración;
- TID/SID/RID/EID para transformaciones reales;
- NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT para estructura y estado;
- EVIDENCE_REGISTER/CLAIM_EVIDENCE_LINK para evidencia;
- COVERAGE_REGISTER para universo/cobertura;
- DGP_TRUTH_SECURE para potenciales y truth restringida.

El nuevo registro debe integrarse en U_G como relación normalizada, con claves y FKs explícitas hacia los objetos existentes. No debe replicar ni absorber las funciones de los registros actuales. No se propone una plataforma de eventos externa, bus, cola, sistema de mensajería ni runtime de instrumentación.

## 6. Contrato mínimo que deberá definir el siguiente gate

Sin aprobar todavía nombres o tipos definitivos, el diseño del registro debe resolver:

1. **Identidad:** event_id opaco y único por ocurrencia; diferenciar identidad de ocurrencia, identidad de registro/corrección y EID transformacional opcional. Reintentos son eventos distintos; no usar object_version como attempt counter.
2. **Tipo y estado:** vocabulario finito para asignación, programación, inicio/fin de intento, recepción, instalación, verificación, rollback, desviación y fallo. Distinguir evento ocurrido, programado, observado, ausente y desconocido sin colapsar 0/?.
3. **Tiempo:** scheduled_time, event_time, observed_at y recorded_at; intervalos start/end si la operación los requiere. No usar timestamp único para todos.
4. **Causalidad/orden:** run_id/scenario_id, unidad, secuencia cuando proceda, referencias predecessor/caused_by y regla para concurrencia/empates; no inferir causalidad del orden de inserción.
5. **Binding DGP:** stage_key y t0…t9 como ejes distintos; política B/version, asignación Z y unidad exacta; no inferir la etapa por nombre del evento.
6. **Artefactos y transformaciones:** artefacto/version/hash, actor/recipient, RID y TID/SID/EID solo cuando el acto sea realmente una transformación.
7. **Snapshots:** referencias explícitas pre/post con (snapshot_id, snapshot_object_record_id) conforme a DEC-C10-065; ausencia de snapshot no se rellena con latest ni timestamp matching.
8. **Integridad:** FKs tipadas, cardinalidades, append-only, corrección/supersession, idempotencia, duplicados, reintentos y rollback.
9. **Evidencia/cobertura:** vínculo directo y tipado con EVIDENCE_REGISTER/CLAIM_EVIDENCE_LINK y COVERAGE_REGISTER; evaluar la ampliación de CLAIM_EVIDENCE_LINK/EVALUATOR_ASSESSMENT/ADJUDICATION_REGISTER conforme a DEC-C10-061.
10. **Firewalls:** truth/potenciales solo en DGP_TRUTH_SECURE; Projector produce observaciones autorizadas; Sealer valida; Analyzer no recibe truth ni potenciales; Evaluator compara después del sellado.

## 7. Implicaciones para D2 y para el harness

La separación de eventos permite distinguir sin ambigüedad:
- asignación Z;
- política B_gZ asignada/versionada;
- W_programmed;
- W_attempt efectivo, incluidos reintentos;
- receipt;
- S_install y rollback;
- evidencias de C_install/C_integrity/C_compat/C_oper;
- C_dep*, A_f*, D_f* como constructos/predicados, no eventos;
- snapshots estructurales basales/post;
- ΔT_acc*, Reach y trayectoria posteriores.

Esto no implementa la cadena ni determina parámetros. El Generator actual sigue sin materializar esos eventos; el Analyzer actual no estima las primeras etapas D2. No se cambian DGP, probabilities, cumplimiento, éxito técnico, soporte, estimandos ni tamaño muestral.

## 8. Decisiones que permanecen abiertas

- Aceptación del registro de eventos integrado en U_G.
- Nombre de tabla, columnas, PK/UK, FKs, tipos y vocabulario cerrado de event_type.
- Identidad y política de corrección/append-only.
- Integración de event claims/evaluations en DEC-C10-061.
- Reconciliación con U_G §12 y matrices físicas; compatibilidad del motor.
- Semántica exacta de orden/causalidad, event_time y temporalidad DGP.
- Mapeo de N02 y ajuste del crosswalk semantic_role bajo DEC-C10-060, sin alterar su vocabulario sin autorización.
- Integración en Generator/Projector/Sealer/Analyzer/Evaluator y pruebas de firewall.
- Cobertura, medición, observabilidad y adjudicación.
- Todos los parámetros cuantitativos y la identificación causal.

## 9. Dictamen y siguiente operación

**Gate 95 cerrado como comparación de alternativas y recomendación documental; no es aceptación ni diseño congelado.**

Dictamen:
GATE_95_OPTION_B_RECOMMENDED / PROCESS_EVENT_REGISTER_AS_U_G_EXTENSION_NOT_PARALLEL_PLATFORM / NODE_STRUCTURAL_GRAPH_CONTAMINATION_RISK_CONFIRMED / EID_SCOPE_PRESERVED / DEC_C10_060_VOCABULARY_UNCHANGED / DEC_C10_061_TYPED_TARGET_AMENDMENT_REQUIRED_FOR_DIRECT_EVENT_CLAIMS / DEC_C10_062_NOT_AUTOMATICALLY_APPLICABLE_TO_EVENT_REGISTER / SNAPSHOT_EXACT_PINNING_PRESERVED / EVENT_TIME_AND_CAUSAL_ORDER_CONTRACT_OPEN / NO_SCHEMA_CHANGE / NO_CODE_CHANGE / NO_EXECUTION / NO_DESIGN_FREEZE.

**Siguiente gate — 96:** desarrollar el contrato lógico del registro de eventos recomendado (B), incluidos identidad de ocurrencia y corrección, tipos de evento, tiempos, orden causal, referencias tipadas a Z/B/unidad/artefacto/snapshots, cobertura/evidencia y firewalls. Reconciliar explícitamente las extensiones necesarias de DEC-C10-061 y los contratos U_G; no modificar todavía el esquema físico ni implementar.
