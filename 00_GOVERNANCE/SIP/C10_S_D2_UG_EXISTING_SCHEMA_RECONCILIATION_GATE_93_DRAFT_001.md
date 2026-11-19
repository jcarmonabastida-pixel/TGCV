# C10-S — Gate 93: reconciliación del contrato D2 con U_G, snapshots y evidencia existentes

**Estado:** HISTORICAL SCHEMA REUSE CONFIRMED / NO PARALLEL EVENT OR SNAPSHOT MODEL REQUIRED AT DOCUMENTARY LEVEL / PHYSICAL EVENT BINDING OPEN / HARNESS MATERIALIZATION ABSENT / NO CODE CHANGE / NO EXECUTION  
**Rama:** `research/c10-s-consolidation-draft`  
**HEAD de referencia:** `9901f4cbcabf11bb7ca25b4f89d49e0146c86ebb` (HEAD previo a este gate).  
**Precedencia:** DEC-C10-067; DEC-C10-059…065; DEC-C10-060/062; DEC-C10-088; U_G Inventory Register Template; semantic_role/logical-root contract; record ID/version/supersession contract; identity/version/snapshot matching contract; transformational snapshot/delta reconciliation; path/predicate temporal evidence matrix; DGP Temporal and Role Contract §§2–3, 56–59; master plan §§16.199–16.200, 16.205, 16.225–16.227 and Gate 92 §16.242.  
**Alcance:** reconstruir los objetos y registros existentes que pueden alojar la cadena D2, clasificar reutilización, proxy y ausencia, y aislar la única brecha residual de vinculación física de eventos. No crear una ontología, tabla universal, nuevo reloj, nuevo catálogo de predicados ni sistema paralelo. No implementar ni ejecutar.

## 1. Reconstrucción histórica: el esquema documental ya existe en gran medida

Gate 92 estableció correctamente que el harness integrado actual no materializa la cadena material D2. Sin embargo, su contrato mínimo debe leerse junto a los esquemas documentales anteriores: no todo lo ausente del código está ausente del diseño.

La reconstrucción confirma que ya existen, como contratos documentales y con distintos estados de aceptación:

1. **U_G:** registros NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT, ROUTE_STEP, EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER. La truth restringida DGP se mantiene segregada fuera de los registros visibles al Analyzer.
2. **Roles semánticos:** vocabulario controlado que distingue TRANSFORMATION_SPEC, TRANSFORMATION_EVENT, ANALYTIC_CONSTRUCT, DATA_STATE_SNAPSHOT, AUTHORIZATION_POLICY, SOFTWARE_COMPONENT, RUNTIME_ENVIRONMENT, LIBRARY_DEPENDENCY, INTERFACE_ENDPOINT, RESOURCE_CAPACITY y OUTCOME_VALUE_RECORD.
3. **Identidad:** TID/SID/RID/EID distinguen definición semántica, especificación, realización técnica y evento/instancia concreta. Los IDs semánticos se separan de object_record_id y object_version.
4. **Snapshots:** pertenencia versionada de NODE/EDGE/ROUTE/PREDICATE a SNAPSHOT, pinning exacto mediante snapshot_object_record_id, nodo raíz lógico y ROUTE_STEP normalizado.
5. **Evidencia:** EVIDENCE_REGISTER y CLAIM_EVIDENCE_LINK separan procedencia de afirmación; COVERAGE_REGISTER define universo/denominador; EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER conservan evaluación y desacuerdo.
6. **Temporalidad:** el DGP ya separa t−1/t0…t9, stage_key, SNAPSHOT.phase y paso hipotético k=1…H. DEC-C10-088 exige enlazarlos expresamente y prohíbe inferir correspondencia por orden, nombre o timestamp.
7. **D2:** DEC-C10-067 y el DGP §§3.1–3.3/56–57 ya separan programación, intento, recepción, instalación, C_dep*, A_f*, D_f*, snapshots y ΔT_acc*.

La plantilla U_G y los contratos relacionados siguen siendo, en lo pertinente, contratos documentales y no una base física validada o poblada. La existencia de sus campos no demuestra instancias ni observaciones.

## 2. Crosswalk D2 → registros existentes

Clasificación:
- **REUTILIZACIÓN DIRECTA:** existe un objeto/registro semánticamente compatible en el esquema documental.
- **REUTILIZACIÓN CON VINCULACIÓN PENDIENTE:** el objeto existe, pero su enlace exacto a eventos, etapas o versiones aún no está cerrado.
- **PROXY NO VÁLIDO:** hay un objeto cercano que no equivale al constructo.
- **AUSENTE EN HARNESS:** no se materializa en el código actual; no implica ausencia del contrato documental.

| Etapa | Contrato/objeto documental reutilizable | Registro o binding propuesto por contratos existentes | Estado de materialización en harness | Dictamen |
|---|---|---|---|---|
| **Z** | U_G N02; semantic_role TRANSFORMATION_EVENT; asignación Z del DGP | Evento de asignación con unidad, run, régimen, tiempo, asignación y provenance; no confundirlo con B | `assignment_z` existe, pero no se proyecta como registro U_G D2 | REUTILIZACIÓN DIRECTA DOCUMENTAL / BINDING AUSENTE |
| **B_g0/B_g1** | U_G N03; semantic_role TRANSFORMATION_SPEC para definición de política; TRANSFORMATION_EVENT solo para su aplicación concreta | Definición versionada, artefacto/versión, intención contractual, ámbito y vínculo a Z; AUTHORIZATION_POLICY solo para autorización real, no para toda política de provisión | No hay policy_id/version ni B_gZ en ScenarioConfig/TruthBundle | REUTILIZACIÓN DIRECTA DOCUMENTAL / NO MATERIALIZADA |
| **W_programmed** | N03 como proceso/evento B, separado de la especificación de política; EID solo si satisface la semántica del contrato de evento | Estado/evento programado ligado a unidad, asignación Z, B/version, actor/tiempo y resultado del acto de programación | No existe campo/evento | REUTILIZACIÓN CON VINCULACIÓN PENDIENTE |
| **W_attempt** | N03 proceso/evento; semantic_role TRANSFORMATION_EVENT si el intento concreto cumple el alcance de EID | Evento distinto de W_programmed, con identidad propia, timestamp, unidad, política/artefacto y estado; nunca inferirlo de programación | `provision_ok` no es intento efectivo D2 | PROXY NO VÁLIDO / EVENTO AUSENTE EN HARNESS |
| **receipt** | N03 proceso B y N04/N06/N07 para artefactos/componentes recibidos; EVIDENCE_REGISTER para prueba de recepción | Evidencia de recepción/disponibilidad ligada al artefacto, versión, unidad, evento de intento y tiempo | Ausente | REUTILIZACIÓN DE OBJETOS / EVENT BINDING OPEN |
| **S_install** | NODE N04–N07 (componentes/endpoint/runtime); SNAPSHOT.phase post-B/rollback; PREDICATE para instalación, integridad, compatibilidad y operatividad | Snapshot pre/post con identidad/versiones; predicados por componente/tiempo; evidencia independiente | Ausente | REUTILIZACIÓN DIRECTA DOCUMENTAL / NO MATERIALIZADA |
| **C_dep*** | N08 ANALYTIC_CONSTRUCT; PREDICATE por componente y ruta; EDGE/ROUTE para dependencias | Constructo derivado de C_install/C_integrity/C_compat/C_oper; truth restringida separada de clasificación observada | Ausente como objeto/verdad del harness | REUTILIZACIÓN DIRECTA DOCUMENTAL / NO MATERIALIZADA |
| **A_f*** | N09 ANALYTIC_CONSTRUCT; PREDICATE para ID/REL/COND/AUTH/RES/DEP/BLOCK; EDGE/ROUTE | Juicio derivado de predicados constitutivos y condiciones; C_auth,base no se colapsa en C_dep* | `focal_access` no implementa el contrato completo | PROXY NO VÁLIDO / CONTRATO DOCUMENTAL EXISTENTE |
| **App_f** | PREDICATE tipo APP, ligado a ruta/paso/estado de entrada | Aplicabilidad desde el estado concreto de cada paso; no equivale a accesibilidad global | Solo cálculo interno limitado; no evidencia adjudicable | REUTILIZACIÓN DIRECTA DOCUMENTAL / NO MATERIALIZADA COMO EVIDENCIA |
| **D_f*** | N09 ANALYTIC_CONSTRUCT y PREDICATEs A_f basal/post en snapshots comparables | Derivado de A_f*(t0)=0 y A_f*(t1)=1 con matching exacto; no es asignación ni simple diferencia de bits | Ausente | REUTILIZACIÓN CON VINCULACIÓN PENDIENTE |
| **T_acc*** | SNAPSHOT estructural con NODE/EDGE/ROUTE/PREDICATE versionados | S_T*=(U*,R*,C*,X*) por unidad/frontera/contexto/tiempo | No existe como snapshot completo en harness | REUTILIZACIÓN DIRECTA DOCUMENTAL / NO MATERIALIZADA |
| **ΔT_acc*** | Identity/version matching + diff entre snapshots comparables; ΔE_T separado | Diff_G,M=(ΔU*,ΔR*,ΔC*,ΔX*); no incorporar cobertura/validity_e | Vector actual de cuatro coordenadas depende de G; no implementa diff U_G | PROXY NO VÁLIDO PARA D2 / CONTRATO DOCUMENTAL EXISTENTE |
| **Reach_H / Π_H** | ROUTE, ROUTE_STEP, PREDICATE y COVERAGE_REGISTER; Reachability contract | Enumeración de rutas y composición bajo G/H, con lógica 1/0/? y cobertura exhaustiva para no-Reach | Cálculo interno parcial, sin grafo/rutas sellados | REUTILIZACIÓN DIRECTA DOCUMENTAL / MATERIALIZACIÓN AUSENTE |
| **K/Consider/Selection/Start/Exec** | DGP t5–t7; N22/N23; E22 conserva destinos como eventos/variables sin nodos/aristas inventados | Etapas downstream separadas, vinculadas a unidad, tiempo y trayectoria; ejecución no reconstruye accesibilidad | No son objeto adjudicable en este harness V_cont | CONTRATO TEMPORAL EXISTENTE / BINDING FÍSICO ABIERTO |
| **Outcome / O-CONF / V_cont / Value** | N23 TRANSFORMATION_EVENT y OUTCOME_VALUE_RECORD, con identidades/tiempos separados; contratos propios de O-CONF/V_cont/Value | Evaluación posterior independiente; Outcome y Value no se colapsan; ausencia no es cero | V_cont tiene alcance limitado; O-CONF/Value no se materializan aquí | REUTILIZACIÓN DOCUMENTAL / IMPLEMENTACIÓN PARCIAL O AUSENTE SEGÚN OBJETO |

## 3. Qué se reutiliza exactamente — no crear duplicados

### 3.1 Política y eventos

- N02 ya distingue la asignación Z como evento, no como componente técnico.
- N03 ya distingue política/proceso B, política asignada, intento de provisión y provisión recibida.
- El semantic_role contract permite distinguir la definición de B (TRANSFORMATION_SPEC) del evento de aplicación/intent (TRANSFORMATION_EVENT), sin convertir B en AUTHORIZATION_POLICY salvo cuando el objeto sea realmente una política de autorización.
- DEC-C10-067 ya fija qué pretende hacer B_g0/B_g1 y qué etapas no garantiza.
- El DGP §16.199 y §16.200 ya define potenciales separados por etapa y la regla W_programmed(z)=z para D2.

No se debe crear un nuevo catálogo B, un segundo catálogo de eventos o una tabla universal de etapas. El punto pendiente es determinar si las etapas W_programmed/W_attempt/receipt pueden representarse como NODE tipados TRANSFORMATION_EVENT con EID bajo el contrato existente, o si una extensión acotada del registro de objetos resulta necesaria. No se decide por anticipado que cualquier evento de provisión sea una transformación EID.

### 3.2 Componentes técnicos, predicados y snapshots

- N04–N07 ya cubren paquete, runtime/dependencias y endpoint/canal.
- NODE conserva identidad/semantic_role, frontera, versión/build/hash y referencias al snapshot exacto.
- SNAPSHOT conserva fase, timestamp, scope, artefactos/hash, método, cobertura y evidencia.
- PREDICATE ya contiene tipo, ruta/paso/tiempo, observed_state, regla, evidencia y razón de desconocimiento.
- C_dep* y A_f* son constructos analíticos N08/N09, no componentes físicos.
- EDGE y ROUTE conservan relaciones y rutas; ROUTE_STEP fija secuencia exacta.

No añadir campos o nodos nuevos para representar algo que ya es una instancia de estos roles. Las observaciones de instalación/verificación deben quedar ligadas a la revisión exacta de SNAPSHOT, componente y ventana.

### 3.3 Evidencia, cobertura y truth

Se reutilizan sin duplicar:
- EVIDENCE_REGISTER: fuente, provenance, método, scope, integridad, timestamp, versión y limitaciones.
- CLAIM_EVIDENCE_LINK: vínculo tipado entre evidencia y afirmación/objeto.
- COVERAGE_REGISTER: universo, denominador, fuentes esperadas/examinadas/válidas, exclusiones y regla COMPLETE.
- EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER: clasificación y discrepancia.
- DGP_TRUTH_SECURE: truth restringida del Generator/Evaluator, segregada del canal del Analyzer.

Reglas ya existentes: observed_state 1/0/? no es evidence_status ni coverage_status; MISSING no equivale a 0; 0 exige evidencia y cobertura negativa suficiente; conflictos sin resolver mantienen ?. No replicar estos estados en un ledger D2 nuevo.

### 3.4 Identidad y temporalidad

Se reutilizan:
- TID/SID/RID/EID para identidades semánticas/contractuales/técnicas/evento cuando corresponda;
- object_record_id/object_version/supersedes_record_id para filas inmutables/versionadas;
- snapshot_id/snapshot_object_record_id para fijar pertenencia exacta;
- valid-time/event_time y created_at/record-time como relojes distintos;
- DEC-C10-088 para enlazar stage_key, t0…t9, SNAPSHOT.phase y k=1…H.

No inferir un binding por coincidencia de timestamp, orden de filas, nombre, última versión o igualdad de hashes. No tratar un nuevo registro observacional en un snapshot como cambio estructural: el diff requiere matching semántico y de granularidad.

## 4. Límites: qué no queda resuelto por reutilizar el esquema

La existencia de tipos y registros no cierra automáticamente la serialización material. Persisten estas cuestiones concretas:

1. **Evento de provisión:** si W_programmed, W_attempt y receipt pueden representarse mediante registros NODE TRANSFORMATION_EVENT/EID sin ampliar el vocabulario o si el evento de recepción requiere un tipo/relación ya disponible. No hay una tabla EVENT independiente en la plantilla U_G actual.
2. **Identidad del evento:** cómo derivar event/EID, vincularlo a run, UE/UA, Z, B/version, etapa y artefacto, y mantener event_time distinto de record-time. El EID de transformación no debe extenderse silenciosamente a eventos que no satisfagan su definición.
3. **Vinculación temporal:** mapping exacto de cada evento a stage_key, t0…t9, SNAPSHOT.phase y ventana; DEC-C10-088 prohíbe inferirlo.
4. **C_dep/A_f/D_f:** regla de derivación, truth por potencial y observación sellada; D_f requiere matching basal/post y no dispone de una tabla/enum propio aprobado que autorice inventar un predicate_type.
5. **ΔT_acc:** catálogo finito, frontera, granularidad G, mapping M, identidad y reglas Diff_G,M; ΔE_T separado.
6. **Reach:** universo finito de rutas, G/H, exhaustividad, composición y cobertura; la plantilla no crea instancias por sí misma.
7. **Firewalls:** proyección exacta de observaciones permitidas hacia Analyzer; truth, potenciales y parámetros ocultos permanecen fuera.
8. **Harness:** no existe mapping implementado desde sus filas actuales a los registros U_G ni captura de estos eventos/snapshots.

La especificación VIATRA de eventos inmutables es un contrato de instrumentación de transformaciones ejecutadas, con su propio ámbito y estado. Puede servir como antecedente conceptual de provenance/secuencia/completitud, pero no se adopta automáticamente como esquema D2: sus TRANSFORMATION_BEGIN/END no representan por sí solos asignación, política, programación, recepción o instalación.

## 5. Corrección de alcance respecto de Gate 92

Gate 92 debe leerse en dos planos distintos:

- **Plano del harness actual:** las etapas B/W/receipt/S_install/C_dep/A_f/D_f y la evidencia U_G no están materializadas; este hallazgo se mantiene.
- **Plano de contratos históricos:** los tipos y registros de U_G, la separación de verdad/observación, los snapshots, los predicados y la temporalidad sí estaban definidos documentalmente antes de Gate 92. No deben volver a diseñarse como un esquema nuevo.

La frase “contrato mínimo de representación” de Gate 92 queda acotada a un crosswalk de materialización del harness y a los bindings todavía abiertos; no es autorización para sustituir ni duplicar los contratos U_G existentes.

## 6. Disposición

**Gate 93 cerrado como reconstrucción y crosswalk documental.**

- U_G existente reutilizable: confirmado.
- N02/N03 distinguen Z y B; semantic_role separa especificación de evento: confirmado documentalmente.
- SNAPSHOT/NODE/EDGE/ROUTE/PREDICATE/ROUTE_STEP: reutilización identificada.
- Evidencia/cobertura/adjudicación y DGP_TRUTH_SECURE: reutilización identificada.
- TID/SID/RID/EID y pinning de versiones: reutilización identificada.
- DEC-C10-088 y los relojes DGP: precedencia temporal confirmada.
- Tabla EVENT nueva, ontología paralela, nuevo reloj o catálogo de predicados: no requeridos ni creados.
- Binding físico de eventos de provisión y correspondencia stage/time/snapshot: OPEN.
- D_f y mapping físico de ΔT_acc: OPEN.
- Harness: sigue sin materializar la cadena D2.
- No se modifica código, DGP, roster, Decision Records ni parámetros.
- No se ejecutan tests, workflows, benchmark ni experimento.
- `scientific_execution=false`; `execution_authorized=false`.

**Dictamen:** `GATE_93_HISTORICAL_SCHEMA_REUSE_CONFIRMED / U_G_AND_TEMPORAL_CONTRACTS_PREEXIST / NO_PARALLEL_EVENT_SNAPSHOT_PREDICATE_SCHEMA / PROVISION_EVENT_BINDING_OPEN / STAGE_TIME_SNAPSHOT_BINDING_OPEN / D_F_AND_DELTA_T_ACC_PHYSICAL_MAPPING_OPEN / HARNESS_D2_CHAIN_NOT_MATERIALIZED / NO_CODE_CHANGE / NO_NEW_WORLDS / NO_EXECUTION / NO_DESIGN_FREEZE`.

**Siguiente operación — Gate 94:** cerrar el contrato de binding de eventos D2 dentro de los registros U_G existentes: determinar con precisión qué eventos de provisión caben en NODE/TRANSFORMATION_EVENT/EID, qué evidencias se enlazan mediante EVIDENCE_REGISTER/CLAIM_EVIDENCE_LINK y cómo se vinculan a Z/B, unidad, etapa DGP, SNAPSHOT y event_time sin inferencias temporales. Si el esquema actual no basta, especificar la extensión mínima sobre el modelo existente y justificarla frente a DEC-C10-061/064/065/088; no crear una tabla paralela ni implementar hasta autorización expresa.
