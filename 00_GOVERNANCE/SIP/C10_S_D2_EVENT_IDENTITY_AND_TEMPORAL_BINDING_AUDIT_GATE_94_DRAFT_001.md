# C10-S — Gate 94: límites de identidad y binding de eventos de provisión D2 en U_G

**Estado:** TRANSFORMATION-EVENT SCOPE BOUNDARY IDENTIFIED / GENERIC PROVISION EVENTS NOT FULLY REPRESENTABLE / EID NOT ASSIGNABLE BY DEFAULT / EVENT-TIME AND STAGE BINDING ABSENT FROM NODE TEMPLATE / MINIMAL EXTENSION REVIEW REQUIRED / NO CODE CHANGE / NO EXECUTION  
**Rama:** research/c10-s-consolidation-draft  
**Antecedente:** Gate 93, C10_S_D2_UG_EXISTING_SCHEMA_RECONCILIATION_GATE_93_DRAFT_001.md.  
**Fuentes:** DEC-C10-060…067; DEC-C10-088; U_G Inventory Register Template §§2, 6, 10.1–10.3, 12, 15; semantic_role/logical-root contract; identity/version/snapshot matching contract; DGP Temporal and Role Contract §§2–3; VIATRA immutable event schema.  
**Alcance:** determinar qué permite el esquema documental actual para identificar y enlazar eventos D2. No se crean roles, columnas, eventos, IDs, filas, tablas ni parámetros; no se modifica el contrato vigente.

## 1. Resultado ejecutivo

U_G permite representar objetos, transformaciones, snapshots y evidencia. No proporciona todavía un contrato completo para todos los eventos de proceso de provisión D2.

La frontera decisiva:

- EID no es un identificador genérico de cualquier suceso. C10-S-ID-MATCH-001 §2 lo define como una aplicación o intento concreto de una transformación sobre una unidad y tiempo, asociada a TID/SID/RID. Ese contrato sigue siendo propuesta/no aprobado.
- W_programmed, receipt y otros hitos de provisión no son automáticamente aplicaciones de una transformación. No se les asigna EID por conveniencia.
- W_attempt podría ser EID solo si el acto de provisión se especifica y acepta como transformación propia, con TID/SID/RID, firma semántica, unidad/contexto y contrato de intento. DEC-C10-067 no crea esa identidad.
- S_install podría tener EID solo si la instalación se define como transformación diferenciada. No basta con que modifique un estado.
- El NODE template no contiene EID, event_time ni stage_key explícitos. Sus campos TID/SID/RID no resuelven la identidad de eventos no transformacionales.
- EVIDENCE_REGISTER registra la fuente que respalda una afirmación sobre un evento; no representa el evento ni su secuencia causal.
- SNAPSHOT fija una captura y su revisión exacta; no sustituye event_time ni permite inferir cuándo ocurrió un evento.
- DEC-C10-088 exige binding explícito entre stage_key, t0…t9, SNAPSHOT.phase y k=1…H. Timestamp, orden o fase no son sustitutos.

Por tanto, no es correcto afirmar que NODE/TRANSFORMATION_EVENT/EID ya cubren toda la cadena D2. Existe una brecha acotada de eventos genéricos de proceso y binding temporal.

## 2. Clasificación evento por evento

| Objeto D2 | Naturaleza | ¿EID válido por defecto? | Representación U_G actual | Dictamen |
|---|---|---|---|---|
| Z assignment | Acto de asignación aleatoria/política, no ejecución de τ2 | No. N02 se mapea a TRANSFORMATION_EVENT en DEC-C10-060, pero EID se define para aplicación/intento de transformación | NODE, semantic_role, node_id, object_record_id; sin EID explícito | Mismatch de alcance N02 ↔ EID; no resolver unilateralmente |
| B_gZ policy definition | Especificación material de política | No, es definición | N03 / TRANSFORMATION_SPEC; AUTHORIZATION_POLICY solo si fuera política de autorización | Reutilizable documentalmente |
| B assignment/receipt | Asignación/recepción de política o artefacto | No por defecto | N03 distingue política asignada, intento y provisión recibida; no hay evento genérico tipado | Parcial |
| W_programmed | Programación/intención de iniciar provisión | No: programar no es iniciar ni ejecutar transformación | No hay campo/evento específico; no se deriva de Z ni B | Ausente como evento material |
| W_attempt | Inicio efectivo del intento de provisión | Solo si la provisión se define como transformación propia y se acepta TID/SID/RID | TRANSFORMATION_EVENT sería candidato condicionado | Condicional; no asignar EID aún |
| receipt | Recepción/disponibilidad efectiva del artefacto | No por defecto | EVIDENCE_REGISTER puede respaldar recepción, pero no es identidad del evento | Ausente como evento material |
| S_install | Aplicación/instalación técnica | Solo si instalación se define como transformación propia | NODE para componente/runtime; SNAPSHOT pre/post; PREDICATE para verificación | Estado observable parcial; evento no cerrado |
| C_install/integrity/compat/oper | Predicados de verificación técnica | No, son estados/juicios | PREDICATE y ANALYTIC_CONSTRUCT N08 | Reutilización documental |
| A_f*, App_f, D_f* | Constructos y predicados analíticos | No | N09, PREDICATE y snapshots comparables | Reutilización documental; derivación abierta |
| τ2 execution | Aplicación concreta de transformación focal | Sí, si TID/SID/RID y EID se instancian según contrato | TRANSFORMATION_SPEC/EVENT; ID-MATCH propone EID | EID aplicable a τ2, no a la provisión por asociación |

La clasificación no afirma que esos eventos hayan ocurrido ni que existan observaciones. D2 sigue siendo una política aceptada conceptualmente, no una secuencia ejecutada.

## 3. Hallazgos de integridad semántica

### 3.1 N02 y EID no están reconciliados

DEC-C10-060 acepta el vocabulario semantic_role y su crosswalk N01–N23, donde N02 (asignación Z) se mapea a TRANSFORMATION_EVENT. C10-S-ID-MATCH-001 define EID más estrechamente como aplicación/intento de una transformación.

Hay dos soluciones posibles, aún no decididas:
1. justificar que la asignación Z constituye una transformación en el sentido del contrato y definir su TID/SID/RID; o
2. conservar Z como evento de asignación no transformacional mediante una representación de evento de proceso distinta.

No se elige ninguna sin decisión expresa. No se cambia DEC-C10-060 ni se amplía EID por interpretación local.

### 3.2 W_attempt y S_install no heredan la identidad de τ2

La dependencia que se intenta instalar habilita τ2; no es por ello la misma transformación que τ2. Artefacto, realización técnica, proceso de provisión y transformación focal tienen identidades diferentes cuando sus contratos/ciclos de vida difieren.

Si instalación/provisión se modela como transformación propia, requiere TID/SID/RID y EID específicos. No puede reutilizar el TID de τ2 ni inferirse equivalencia por pertenecer a la misma cadena causal.

### 3.3 NODE no contiene hoy un event record completo

El NODE template contiene node_id, semantic_role, TID/SID/RID, timestamp, object_record_id, object_version, snapshot_id y snapshot_object_record_id. No contiene:
- EID explícito;
- event_time separado de timestamp/record-time;
- stage_key explícito;
- tipo/estado de evento de proceso;
- vínculo tipado explícito a evento padre, asignación Z, política B y artefacto recibido.

created_at es record-time conforme a DEC-C10-062, no event_time. El campo timestamp no debe reinterpretarse como event_time sin contrato específico. Tampoco se añade EID a NODE por analogía.

### 3.4 Evidencia no sustituye al evento

EVIDENCE_REGISTER conserva provenance, source, method, scope, timestamp, version identity, integrity y completeness limitations. CLAIM_EVIDENCE_LINK conecta esa evidencia con un objeto/afirmación tipados.

Un recibo, log o artefacto puede ser evidencia de receipt/W_attempt/S_install; el registro de evidencia no crea identidad de evento, no fija su stage ni establece causal order. La ausencia de artefacto no equivale a W_attempt=0 o receipt=0. Un 0 requiere evidencia válida y cobertura suficiente. No crear un segundo ledger de evidencia ni convertir EVIDENCE_REGISTER en event store.

## 4. Binding temporal: requisitos y ausencia actual

DEC-C10-067 distingue Z, B, W_programmed, W_attempt, receipt, S_install, C_dep*, A_f* y D_f*. El DGP sitúa política/intento en t1, verificación técnica en t2 y snapshot postintervención en t3. Esta secuencia conceptual no basta para instanciar registros.

DEC-C10-088 exige que cada registro material enlace expresamente:
- stage_key;
- reloj DGP t0…t9;
- SNAPSHOT.phase y revisión exacta (snapshot_id, snapshot_object_record_id);
- unidad/instancia;
- ruta/paso cuando aplique;
- mapping/versiones;
- event_time y tiempos de generación/observación.

No son equivalentes event_time y created_at; tiempo de evento y timestamp de captura; stage_key y SNAPSHOT.phase; t0…t9 y k=1…H; secuencia de registros y orden causal.

El NODE template no tiene stage_key/event_time explícitos. SNAPSHOT.phase admite fases de captura (baseline/post-B/rollback/route-test), no codifica por sí sola todos los hitos D2. No se deriva el stage por la fase ni se resuelve el snapshot por proximidad temporal.

## 5. Qué permite el esquema actual y qué no

**Reutilizable sin duplicación:** NODE para componentes y transformaciones que cumplan semantic_role; EDGE para relaciones reales entre objetos identificados y fijados al mismo snapshot; SNAPSHOT para capturas y pinning exacto; PREDICATE para estados por ruta/paso/tiempo; EVIDENCE_REGISTER y CLAIM_EVIDENCE_LINK para procedencia/respaldo; COVERAGE_REGISTER para universo/denominador; EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER para evaluación; DGP_TRUTH_SECURE para truth/potenciales restringidos.

**No representable de forma completa sin aclaración/extensión:** eventos genéricos de asignación, programación, recepción e hitos de provisión; identidad separada de esos eventos cuando no son transformaciones; event_time y stage_key como atributos explícitos del evento NODE; bindings tipados a unidad/Z/B/artefacto y snapshot sin inferencias.

La existencia de NODE y semantic_role no demuestra que cualquier evento pueda almacenarse en NODE. Forzar eventos no transformacionales dentro de TRANSFORMATION_EVENT ampliaría el significado del vocabulario y contaminaría EID.

## 6. Extensión mínima a evaluar en Gate 95 — propuesta, no aprobación

La opción de menor duplicación que debe evaluarse primero es extender U_G, no crear un event store paralelo:

1. Resolver mediante decisión el alcance de N02/TRANSFORMATION_EVENT frente a EID.
2. Si hay hitos no transformacionales que deben ser registros de primer nivel, evaluar un semantic_role específico de evento de proceso dentro de NODE; nombre y semántica pendientes. Los 16 roles aceptados no se alteran hasta aprobación.
3. Definir identidad de instancia con node_id + object_record_id/object_version o justificar un identificador tipado adicional; no reutilizar EID si no cumple su contrato.
4. Definir campos explícitos event_time y stage_key, separados de created_at, timestamp de captura y SNAPSHOT.phase.
5. Reutilizar EDGE u otro binding tipado ya aprobado para enlazar evento, unidad, Z, B/version, artefacto y snapshot exacto. No inventar relaciones ni FKs por conveniencia.
6. Preservar event_time y record-time, y fijar snapshot exacto según DEC-C10-065.
7. Usar EVIDENCE_REGISTER/CLAIM_EVIDENCE_LINK como evidencia y COVERAGE_REGISTER para cobertura, nunca como sustitutos del evento.
8. Mantener Generator truth/potenciales separados del canal observado y del Analyzer.

Es una hipótesis de diseño. No se aprueba un nuevo semantic_role, columna, FK, formato, regla de secuencia ni modificación de plantilla. Gate 95 comparará NODE extendido con un registro separado y justificará la alternativa más compatible con snapshot/versionado.

## 7. Dictamen y siguiente gate

**Gate 94 cerrado como auditoría de alcance y brecha del binding.**

Dictamen:
GATE_94_EVENT_IDENTITY_BOUNDARY_IDENTIFIED / N02_TRANSFORMATION_EVENT_VS_EID_SCOPE_MISMATCH / B_POLICY_SPEC_REUSABLE / W_PROGRAMMED_AND_RECEIPT_NOT_GENERIC_EID / W_ATTEMPT_AND_S_INSTALL_EID_CONDITIONAL_ON_SEPARATE_TRANSFORMATION_SPEC / NODE_EVENT_TIME_AND_STAGE_KEY_ABSENT / EVIDENCE_IS_NOT_EVENT_IDENTITY / DEC_C10_088_BINDING_NOT_MATERIALIZED / MINIMAL_UG_EXTENSION_REVIEW_REQUIRED / NO_SCHEMA_CHANGE / NO_CODE_CHANGE / NO_NEW_WORLDS / NO_EXECUTION / NO_DESIGN_FREEZE.

**Siguiente gate — 95:** comparar formalmente (A) extensión mínima de NODE/semantic_role para eventos de proceso, con event_time/stage_key y bindings tipados, y (B) registro de eventos separado. Evaluar identidad, inmutabilidad, snapshot pinning, integridad referencial, granularidad, orden causal, compatibilidad con DEC-C10-060…065/088 y firewalls Generator/Analyzer/Evaluator. Elegir solo una recomendación justificada; no modificar contratos ni implementar hasta autorización expresa.
