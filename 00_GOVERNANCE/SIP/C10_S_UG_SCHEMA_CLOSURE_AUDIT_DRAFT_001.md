# C10-S — Auditoría de cierre documental del esquema U_G

**ID:** C10-S-UG-SCHEMA-CLOSURE-AUDIT-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Rama de revisión:** `research/c10-s-consolidation-draft`  
**PR:** #116 · HEAD observado durante la auditoría: `4d3138aaae44ab27e0841315af02783661177c14`  
**Estado:** AUTOAUDITORÍA DOCUMENTAL ASISTIDA / NO INDEPENDIENTE; esquema NO CERRADO, NO CONGELADO, NO IMPLEMENTADO.

## 1. Alcance y método

Se contrastaron la plantilla U_G, el contrato DEC-C10-059 de boundary_class/FK SNAPSHOT→NODE, el protocolo de evidencia y adjudicación, la matriz de cobertura trivalente, el crosswalk IAM, la auditoría FP/EDGE, la reconciliación SM/FP, la matriz operacional F* y el plan integral C10-S.

La revisión fue estática sobre los contenidos de GitHub. Se comprobaron los encabezados, separadores y filas de esquema de las diez tablas canónicas y se buscaron contradicciones entre el esquema físico descrito en §§2–6 y el esquema normalizado de §§12.7–12.10.

No se ejecutaron parser, validador, constraints, fixtures, pruebas, simulaciones ni experimentos. No se inspeccionó ningún sistema real ni se crearon instancias U_G. Esta revisión no equivale a revisión independiente.

## 2. Resultado ejecutivo

**Dictamen: CORRECTION_REQUIRED / SCHEMA_NOT_CLOSED.**

La estructura de diez registros canónicos está presente y no se justifica crear tablas paralelas. Los recuentos estáticos de columnas de las diez tablas coinciden entre encabezado, separador y fila de esquema:

| Tabla | Columnas |
|---|---:|
| NODE | 30 |
| EDGE | 29 |
| ROUTE | 29 |
| PREDICATE | 24 |
| SNAPSHOT | 26 |
| EVIDENCE_REGISTER | 18 |
| CLAIM_EVIDENCE_LINK | 10 |
| COVERAGE_REGISTER | 15 |
| EVALUATOR_ASSESSMENT | 13 |
| ADJUDICATION_REGISTER | 12 |

No se detectaron nombres de columna duplicados en esos encabezados ni discrepancias de anchura en las filas de esquema examinadas. Este resultado solo verifica la forma tabular; no valida tipos, dominios, claves, relaciones ni comportamiento.

La principal brecha no es el número de columnas, sino la falta de sincronización completa entre el contrato normalizado y los encabezados físicos, además de varias relaciones polimórficas todavía no implementables sin reglas adicionales.

## 3. Hallazgos

### UG-SCH-01 — EDGE: contrato normalizado no reflejado íntegramente en el encabezado físico

**Severidad:** ALTA · **Estado:** CORRECTED_DOCUMENTALLY; pending second-pass review.

El §12.7 declara para EDGE los campos `parent_edge_id` y `atomic_edge_id`, además de `source_node_id` y `target_node_id`. El encabezado físico actual utiliza `source_node` y `target_node`, y no contiene `parent_edge_id` ni `atomic_edge_id`.

El propio §10.6 ya declara `parent_edge_id` y `atomic_edge_id` necesarios para conservar el catálogo padre E01–E23 y atomizar relaciones mult destino. Por tanto, la omisión no puede tratarse como una preferencia de nomenclatura.

**Resolución documental (2026-11-05):** el encabezado EDGE ahora incluye `atomic_edge_id`, `parent_edge_id`, `source_node_id` y `target_node_id`; `source_node`/`target_node` se sustituyen por los nombres explícitos. Se conserva `edge_id` como identidad semántica local de la arista atómica. El encabezado, separador y fila de esquema tienen 31 columnas. Pendiente segunda pasada del crosswalk y de integridad referencial; no es validación física.

### UG-SCH-02 — SNAPSHOT: etiqueta de FK incompleta

**Severidad:** MEDIA · **Estado:** CORRECTED_DOCUMENTALLY; physical constraint pending.

El encabezado identifica `unit_object_record_id` como “FK NODE.object_record_id”, pero DEC-C10-059 y el contrato asociado requieren la pareja compuesta:

`SNAPSHOT.(unit_object_record_id, unit_id) → NODE.(object_record_id, node_id)`

La columna está presente; la etiqueta del encabezado no expresa la restricción completa.

**Resolución documental (2026-11-05):** la etiqueta del encabezado ahora declara que `unit_object_record_id` forma parte de la FK compuesta junto con `unit_id` hacia `(object_record_id,node_id)` de NODE. DEC-C10-059 se mantiene sin cambios. La constraint física sigue pendiente.

### UG-SCH-03 — Vocabulario de semantic_role y rol raíz no formalizados

**Severidad:** ALTA · **Estado:** PROPOSAL_CREATED; pending acceptance.

El contrato de DEC-C10-059 exige que el NODE destino de SNAPSHOT tenga `semantic_role=LOGICAL_SERVICE_UNIT`. Sin embargo, la plantilla no presenta un dominio controlado completo para `semantic_role`, ni el crosswalk de roles U_G consultado define explícitamente cómo se incorpora ese rol raíz a los 23 roles existentes.

**Resolución propuesta:** se creó `C10_S_UG_SEMANTIC_ROLE_AND_LOGICAL_ROOT_CONTRACT_DRAFT_001.md`. Distingue semantic_role de parent_catalog_id y boundary_class; propone vocabulario controlado y crosswalk no uno-a-uno N01–N23; conserva DEC-C10-059 y fija exactamente un nodo raíz por combinación unidad/snapshot/scope. Pendiente aceptación del usuario y validación técnica.

### UG-SCH-04 — source_provenance: conflicto entre §10.6 y §12.7

**Severidad:** MEDIA · **Estado:** ACCEPTED_DOCUMENTALLY (DEC-C10-061); physical validation pending.

El §10.6 lo declaraba como campo común, mientras §12.1 ya lo registra canónicamente en EVIDENCE_REGISTER. DEC-C10-061 resuelve la discrepancia: la procedencia se normaliza en EVIDENCE_REGISTER y se enlaza mediante CLAIM_EVIDENCE_LINK; no se duplica en las tablas de objetos.

**Resolución DEC-C10-061:** source_provenance es canónica en EVIDENCE_REGISTER; cada afirmación observada enlaza a evidencia mediante CLAIM_EVIDENCE_LINK. La procedencia no se elimina ni se debilita; se evita duplicación textual.

### UG-SCH-05 — CLAIM_EVIDENCE_LINK: destino de cobertura no resuelto

**Severidad:** ALTA · **Estado:** ACCEPTED_DOCUMENTALLY (DEC-C10-061); physical validation pending.

§12.10 atribuye a COVERAGE_REGISTER vínculos claim-evidence 0..n. Sin embargo, CLAIM_EVIDENCE_LINK.claim_target_id se define como `object_record_id`, mientras que COVERAGE_REGISTER tiene `coverage_scope_id` como clave y no contiene `object_record_id`.

**Resolución DEC-C10-061:** se incorpora `claim_target_type=COVERAGE_SCOPE` y la FK tipada `target_coverage_scope_id → COVERAGE_REGISTER.coverage_scope_id`, con exclusividad exactamente-una respecto de las otras cinco FKs.

### UG-SCH-06 — FK polimórficas de CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER

**Severidad:** ALTA · **Estado:** PROPOSAL_CREATED; acceptance pending.

Los registros de vínculo, evaluación y adjudicación utilizan `object_type + object_record_id` para identificar objetos de varias tablas. El contrato indica “FK tipada”, pero no especifica un mecanismo de integridad referencial que garantice que la pareja resuelva a una y solo una tabla/registro válido, ni los dominios cerrados de object_type/claim_target_type.

**Resolución DEC-C10-061:** se elige estrategia de seis FKs específicas por tipo y restricciones de exclusividad/coherencia enum en CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER. La integridad es definida documentalmente, no implementada ni validada físicamente.

### UG-SCH-07 — alcance de unicidad de object_record_id y supersedes_record_id

**Severidad:** MEDIA · **Estado:** ACCEPTED_DOCUMENTALLY — DEC-C10-062; physical validation pending.

DEC-C10-062 acepta el contrato `C10_S_UG_RECORD_ID_VERSION_AND_SUPERSESSION_CONTRACT_PROPOSAL_DRAFT_001.md`. La plantilla U_G incorpora el complemento normativo §12.12. Se fijan unicidad de `object_record_id` por tabla; `object_version` INT positivo, contiguo por identidad semántica; `supersedes_record_id` autorreferente al predecesor inmediato de la misma tabla/identidad; cadena lineal e historial inmutable; distinción record-time/observación; y SNAPSHOT→NODE fijado a versión exacta. Constraints, parser y validación física permanecen pendientes.

### UG-SCH-08 — estados de SNAPSHOT y boundary_class

**Severidad:** BAJA · **Estado:** CLARIFIED_DOCUMENTALLY; second-pass review pending.

La fila de esquema de SNAPSHOT usa `observed_state=NA`, mientras que el contrato común describe estados trivalentes y NA por no aplicabilidad. NODE utiliza boundary_class=NA en su fila de esquema vacía. Ambas filas están rotuladas como filas de esquema, no como observaciones.

**Resolución documental (2026-11-05):** las filas ilustrativas NODE y SNAPSHOT identifican NA como marcador de plantilla, no observación ni clasificación real. En registros reales, NA requiere justificación conforme al contrato. No cambia la regla sustantiva de DEC-C10-059.

## 4. Reconciliaciones que se mantienen válidas

1. Se conserva DEC-C10-059: boundary_class tiene tres clases sustantivas y NA solo como no aplicabilidad justificada; P2 sigue transversal.
2. Se conserva la FK compuesta SNAPSHOT→NODE; la etiqueta física debe reflejarla, no simplificarla.
3. Se mantiene evidence_ref como referencia opcional 0..1 y CLAIM_EVIDENCE_LINK como relación completa 0..n.
4. Para observed_state 1/0 se exige vínculo probatorio válido; para ? puede faltar evidencia solo con unknown_reason, MISSING y límites de cobertura; no se infiere 0 por silencio.
5. COVERAGE_REGISTER es el registro canónico de cobertura; la tabla de §7 es solo vista-resumen.
6. FP-08 sigue siendo validez probatoria/reproducibilidad separada de la conformidad funcional FP-01…07.
7. La reconciliación SM/FP de DEC-C10-055 se conserva; esta auditoría no reasigna responsabilidades FP ni crea aristas EDGE.

## 5. Estado por dimensión

| Dimensión | Dictamen |
|---|---|
| Diez tablas y anchuras de filas de esquema | PASS_STATIC |
| Nombres de columnas duplicados | No detectados en los diez encabezados |
| DEC-C10-059 / boundary_class conceptual | ACCEPTED; sin validación física |
| FK compuesta SNAPSHOT→NODE | DEFINED_DOCUMENTALLY; label corrected; physical constraint pending |
| EDGE parent/atomic IDs y extremos | CORRECTED_DOCUMENTALLY; second pass pending |
| semantic_role / nodo raíz | ACCEPTED_DOCUMENTALLY (DEC-C10-060); physical validation pending |
| Procedencia y CLAIM_EVIDENCE_LINK | ACCEPTED_DOCUMENTALLY (DEC-C10-061); physical validation pending |
| FK polimórficas | ACCEPTED_DOCUMENTALLY (DEC-C10-061); physical validation pending |
| Unicidad/versionado/supersedes | ACCEPTED_DOCUMENTALLY — DEC-C10-062; physical validation pending |
| Parser, tipos, dominios y constraints | NOT_ASSESSED |
| Seguridad, custodia y permisos | NOT_ASSESSED |
| Inventario real, evidencia y cobertura | NONE / NOT_STARTED |
| Revisión independiente | NOT_AVAILABLE / NOT_INDEPENDENT |

## 6. Secuencia mínima de cierre documental

1. Corregir EDGE para alinear encabezado, catálogo padre y aristas atómicas.
2. Formalizar semantic_role y el nodo raíz lógico sin duplicar roles U_G.
3. Resolver claim targets de cobertura y mecanismo de FK polimórfica.
4. Aclarar procedencia canónica, unicidad y supersedes.
5. Corregir la etiqueta de FK de SNAPSHOT y las notas de filas de esquema.
6. Ejecutar una segunda revisión estática documental del crosswalk completo.
7. Solo entonces preparar el gate técnico de parser/constraints. La ejecución del gate requiere disponibilidad del entorno local y autorización técnica separada; no queda autorizada por este documento.

## 7. Gobernanza y límites

Esta auditoría es `AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT`. No es revisión por pares ni validación externa.

No modifica TGCV Core, RMA, Evidence→Claim Matrix, STATUS, claims ni estimandos. No convierte el diseño en FROZEN. No genera instancias, truth, fixtures ni datos. No autoriza acceso a sistemas reales, parser, pruebas, simulación ni experimento.

`scientific_execution=false`; `execution_authorized=false`.


## 8. Actualización de seguimiento — 2026-11-05

UG-SCH-01 ha sido corregido documentalmente en la plantilla: EDGE pasa a 31 columnas e incorpora `atomic_edge_id`, `parent_edge_id`, `source_node_id` y `target_node_id`. Se conserva E07 como regla lógica no-arista y E22 sin inventar nodos destino. La anchura física estática coincide en encabezado, separador y fila de esquema.

Para UG-SCH-03 se creó `C10_S_UG_SEMANTIC_ROLE_AND_LOGICAL_ROOT_CONTRACT_DRAFT_001.md` y el usuario lo aceptó mediante DEC-C10-060. El crosswalk N01–N23 es de roles de catálogo a tipos semánticos, no una equivalencia uno-a-uno. La aceptación es documental; la implementación y validación física siguen pendientes.

Los demás hallazgos UG-SCH-02 y UG-SCH-04…08 permanecen abiertos. Dictamen global: SCHEMA_NOT_CLOSED.


## 9. Seguimiento — 2026-11-05

UG-SCH-03 queda aceptado documentalmente por DEC-C10-060; enum y constraints físicos pendientes. UG-SCH-02 queda corregido documentalmente al explicitar la FK compuesta en SNAPSHOT. UG-SCH-08 queda aclarado documentalmente: NA en filas de esquema es marcador, no dato observado. UG-SCH-04, UG-SCH-05, UG-SCH-06 y UG-SCH-07 permanecen OPEN. Dictamen global: SCHEMA_NOT_CLOSED.


## 10. Propuesta de resolución tipada — 2026-11-05

Se creó `C10_S_UG_TYPED_TARGET_REFERENTIAL_INTEGRITY_CONTRACT_PROPOSAL_DRAFT_001.md`. Propone FKs nullable específicas por tabla destino con exclusividad exactamente-una y coherencia con enum de tipo, incluyendo COVERAGE_REGISTER; aplica el patrón a CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER. Resuelve conceptualmente la procedencia al mantener source_provenance canónica en EVIDENCE_REGISTER y retirar su duplicación de las tablas de objetos. UG-SCH-04/05/06 quedan PROPOSAL_CREATED, pendientes de aceptación y de reconciliación física. No modificar la plantilla hasta decisión del usuario. UG-SCH-07 permanece OPEN. Dictamen global: SCHEMA_NOT_CLOSED.


## 11. Actualización — DEC-C10-061 (2026-11-05)

UG-SCH-04, UG-SCH-05 y UG-SCH-06 quedan ACCEPTED_DOCUMENTALLY por decisión explícita DEC-C10-061. La plantilla incorpora procedencia canónica en EVIDENCE_REGISTER y FKs tipadas exclusivas para CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER, incluyendo COVERAGE_SCOPE. Se requiere exactamente una FK de destino no nula y coherencia con el enum de tipo. object_record_id debe ser UNIQUE por tabla de objeto y coverage_scope_id PK/UNIQUE. La plantilla se modificó documentalmente; constraints, parser, unicidad y pruebas negativas no están implementados ni validados. UG-SCH-07 permanece OPEN. Dictamen global: SCHEMA_NOT_CLOSED.


## 12. Corrección de consistencia post-aceptación — 2026-11-05

La segunda pasada detectó y corrigió dos residuos editoriales: (1) §10.5 aún mencionaba source_provenance como columna de objeto, aunque DEC-C10-061 la normaliza en EVIDENCE_REGISTER; (2) la lista §12.8 conservaba una secuencia literal `\\n` que había concatenado las reglas SNAPSHOT/boundary_class. Se separaron las reglas y se renumeraron. También se igualaron las anchuras de las filas ilustrativas de CLAIM_EVIDENCE_LINK (15 columnas), EVALUATOR_ASSESSMENT (18) y ADJUDICATION_REGISTER (17). Esta es una comprobación estática de Markdown, no validación física.


## 12. Propuesta UG-SCH-07 — 2026-11-05

Se creó `C10_S_UG_RECORD_ID_VERSION_AND_SUPERSESSION_CONTRACT_PROPOSAL_DRAFT_001.md`. La propuesta distingue identidad semántica, identidad de registro y versión de registro; define unicidad por tabla, versión positiva secuencial y supersession inmediato dentro de la misma tabla/identidad. No hay aceptación, freeze ni validación física. UG-SCH-07 sigue abierto; el esquema global continúa SCHEMA_NOT_CLOSED.


## 13. Aplicación de DEC-C10-062 — 2026-11-05

DEC-C10-062 queda ACCEPTED DOCUMENTALLY. La plantilla U_G contiene §12.12 con las reglas de identidad de registro, secuencia de versiones, supersession lineal e inmutabilidad. UG-SCH-07 queda aceptado documentalmente; no validado físicamente. El dictamen global permanece SCHEMA_NOT_CLOSED hasta completar revisión integral y gate técnico. No hay freeze ni ejecución científica.


## 14. Segunda pasada documental — estado vigente tras DEC-C10-062 (2026-11-05)

Esta sección es el ledger vigente de la auditoría. Los apartados 8–13 anteriores conservan su valor como registro cronológico de hallazgos y decisiones en el momento en que se redactaron; sus estados intermedios no deben interpretarse como estado actual cuando contradigan esta actualización y las decisiones DEC-C10-059…062.

### 14.1. Ledger vigente de hallazgos

| Hallazgo | Estado vigente | Base documental / pendiente |
|---|---|---|
| UG-SCH-01 — EDGE parent/atomic IDs y extremos | CORRECTED_DOCUMENTALLY; second-pass crosswalk pending | Encabezado EDGE incorpora atomic_edge_id, parent_edge_id, source_node_id y target_node_id. Sin FK física. |
| UG-SCH-02 — SNAPSHOT→NODE | CORRECTED_DOCUMENTALLY; physical constraint pending | Etiqueta y contrato conservan FK compuesta (unit_object_record_id, unit_id) → (object_record_id, node_id). |
| UG-SCH-03 — semantic_role y nodo raíz | ACCEPTED_DOCUMENTALLY — DEC-C10-060 | Vocabulario controlado de 16 roles y raíz LOGICAL_SERVICE_UNIT; enum/FK/constraints físicos pendientes. |
| UG-SCH-04 — source_provenance | ACCEPTED_DOCUMENTALLY — DEC-C10-061 | Procedencia canónica en EVIDENCE_REGISTER, no duplicada en tablas de objeto. |
| UG-SCH-05 — destino COVERAGE_SCOPE | ACCEPTED_DOCUMENTALLY — DEC-C10-061 | target_coverage_scope_id y FK tipada a coverage_scope_id. |
| UG-SCH-06 — referencias polimórficas | ACCEPTED_DOCUMENTALLY — DEC-C10-061 | Seis FKs tipadas con exclusividad y coherencia enum en tres tablas relacionales; validación física pendiente. |
| UG-SCH-07 — unicidad/versionado/supersession | ACCEPTED_DOCUMENTALLY — DEC-C10-062 | Unicidad por tabla, versión secuencial y cadena de supersession lineal e inmutable. |
| UG-SCH-08 — NA en filas de esquema | CLARIFIED_DOCUMENTALLY | NA ilustrativo no es observación; NA real exige justificación. |
| UG-SCH-09 — matriz de obligatoriedad incompleta y claves/versionado no sincronizados | CORRECTED_DOCUMENTALLY; second-pass semantic review pending | §12.10 se amplía a los diez registros operativos y separa PK lógica, claves candidatas UNIQUE, FKs y cardinalidades conforme a DEC-C10-061/062. |
| UG-SCH-10 — vinculación de registros de grafo con snapshot y referencias versionadas | OPEN / DESIGN_RECONCILIATION_REQUIRED | NODE/EDGE/ROUTE/PREDICATE no contienen una FK explícita a snapshot_id; EDGE usa source_node_id/target_node_id y ROUTE/PREDICATE referencias semánticas sin pinning inequívoco a object_record_id/versiones. Los contratos de snapshot exigen comparabilidad y matching, pero la plantilla no define el mecanismo relacional de pertenencia y referencias exactas. |

### 14.2. Recuento estático actualizado de los diez registros operativos

Se han vuelto a contrastar encabezado, separador y primera fila de esquema en la plantilla vigente:

| Tabla | Columnas |
|---|---:|
| NODE | 30 |
| EDGE | 31 |
| ROUTE | 29 |
| PREDICATE | 24 |
| SNAPSHOT | 26 |
| EVIDENCE_REGISTER | 18 |
| CLAIM_EVIDENCE_LINK | 15 |
| COVERAGE_REGISTER | 15 |
| EVALUATOR_ASSESSMENT | 18 |
| ADJUDICATION_REGISTER | 17 |

No se detectaron nombres de columna duplicados en esos diez encabezados. Las anchuras actuales de CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER son 15, 18 y 17; los recuentos anteriores 10, 13 y 12 quedan como mediciones históricas anteriores a la ampliación documental, no como descripción del esquema vigente.

Este recuento verifica únicamente forma tabular estática. No prueba tipos, PK/FK, UNIQUE, cardinalidades, enum, CHECK, constraints, inmutabilidad, parser ni comportamiento.

### 14.3. Reconciliación de la matriz §12.10

La revisión detectó que la matriz anterior solo enumeraba siete registros y omitía CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER, pese a que los tres forman parte de los diez registros operativos. También resumía PK compuestas sin distinguirlas de las claves candidatas UNIQUE requeridas por las FKs tipadas y por DEC-C10-062.

La plantilla §12.10 se ha sustituido documentalmente por una matriz de diez filas que:
- conserva las PK lógicas compuestas previamente declaradas para las cinco tablas de objetos;
- declara por separado UNIQUE(object_record_id) por tabla, requerido por las FKs tipadas;
- declara UNIQUE(semantic_id, object_version) por tabla;
- incorpora las cinco tablas de evidencia, vínculo, cobertura, evaluación y adjudicación;
- mantiene DGP_TRUTH_SECURE segregada y fuera de los diez registros operativos.

La actualización es una reconciliación de decisiones ya aceptadas, no una nueva decisión científica. El significado físico de PK compuesta más UNIQUE(object_record_id) deberá implementarse y comprobarse en el formato/motor elegido.

### 14.4. Dictamen vigente

**Dictamen: CORRECTION_REQUIRED / SCHEMA_NOT_CLOSED.**

UG-SCH-01…08 tienen resoluciones documentales o aclaraciones aceptadas conforme al ledger §14.1. UG-SCH-09 se ha corregido documentalmente, pero requiere segunda pasada semántica de los diez contratos y crosswalk. Permanecen sin validar físicamente las claves, FKs compuestas/autorreferentes/tipadas, exclusividad, cardinalidades, enums, CHECK, secuencias, ciclos, inmutabilidad y seguridad/custodia.

No hay freeze, inventario real, instancias, truth accesible al analizador, fixtures, validación ejecutable, revisión independiente ni evidencia empírica nueva. Se mantienen `scientific_execution=false` y `execution_authorized=false`.


### 14.5. Nuevo hallazgo UG-SCH-10 — pertenencia a snapshot y pinning de referencias

**Severidad:** ALTA · **Estado:** OPEN / DESIGN_RECONCILIATION_REQUIRED.

La plantilla registra NODE, EDGE, ROUTE y PREDICATE con identidad semántica y versión de registro, pero no contiene una referencia explícita de esos registros al `snapshot_id` al que pertenecen. SNAPSHOT fija la versión exacta del NODE raíz, pero no la pertenencia del resto del grafo a esa captura.

Además:
- EDGE identifica extremos mediante `source_node_id/target_node_id`, sin referencias explícitas a los `object_record_id` concretos de NODE.
- ROUTE mantiene `ordered_node_edge_sequence` sin un contrato de serialización ni resolución a registros versionados exactos.
- PREDICATE usa `route_id` sin pinning explícito a la revisión de ROUTE.
- Timestamp y `coverage_scope_id` no sustituyen por sí solos una FK inequívoca a snapshot ni resuelven registros versionados.

Los contratos de identidad y snapshot exigen que los diffs se calculen sobre snapshots comparables, con identidad, granularidad y mapping explícitos; sin embargo, no definen aún cómo se resuelven físicamente la pertenencia al snapshot y las referencias entre versiones del grafo.

**Riesgo:** dos revisiones del mismo objeto semántico podrían ser seleccionadas para una arista/ruta/predicado sin una regla inequívoca de versión/snapshot. No se afirma que el sistema contenga ya una referencia errónea; se identifica que el contrato de captura no permite comprobarla todavía.

**Siguiente acción documental:** elaborar una reconciliación de alternativas para:
1. vincular cada registro de grafo a un snapshot exacto;
2. fijar los extremos de EDGE a revisiones concretas de NODE;
3. fijar la secuencia de ROUTE a revisiones concretas de NODE/EDGE;
4. vincular PREDICATE a la revisión exacta de ROUTE;
5. preservar identidad semántica, historial y snapshots inmutables sin inferir correspondencia por timestamp;
6. valorar si puede resolverse dentro de las diez tablas aceptadas o requiere una relación normalizada adicional.

No modificar todavía la plantilla para añadir columnas/relaciones en este punto: la solución puede afectar cardinalidades, claves y estructura del registro. Requiere una propuesta explícita y aceptación antes de su aplicación.

### 14.6. Revisión de segunda pasada — alcance actual

La revisión ha cubierto la matriz de diez tablas, claves declaradas, referencias tipadas, versionado, snapshots, contratos de identidad, frontera/granularidad, cobertura y crosswalk IAM/FP. UG-SCH-09 se corrigió documentalmente. UG-SCH-10 es un hallazgo nuevo y bloquea el cierre integral del esquema.

El dictamen global permanece **CORRECTION_REQUIRED / SCHEMA_NOT_CLOSED**. No se ha ejecutado ningún validador ni se han creado instancias, fixtures, truth, simulaciones o experimentos.


### 14.7. Comparación de alternativas UG-SCH-10

Se crea `C10_S_UG_SNAPSHOT_MEMBERSHIP_AND_VERSIONED_GRAPH_REFERENCES_OPTIONS_DRAFT_001.md`, sin alterar la plantilla ni las decisiones aceptadas.

Se comparan:
- **A — snapshot_id directo en cada registro de grafo**, con referencias exactas EDGE→NODE y PREDICATE→ROUTE y una relación normalizada ROUTE_STEP para secuenciar NODE/EDGE. Implica un nuevo registro observacional por objeto y snapshot; object_version debe interpretarse como versión del registro observacional, no como cambio material del objeto. Requiere resolver la dependencia circular SNAPSHOT↔NODE raíz.
- **B — SNAPSHOT_MEMBER normalizado**, que permite reutilizar registros inmutables entre snapshots, pero requiere además bindings de extremos y ROUTE_STEP, con mayor complejidad de FKs tipadas y coherencia de mismo-snapshot.
- **C — manifiesto serializado**, rechazado como fuente canónica por no proporcionar FKs ordinarias para cada elemento.
- **D — inferencia temporal/coverage/última versión**, rechazada por ambigua e incompatible con el pinning exacto.

Recomendación provisional: Opción A, condicionada a aceptar semántica observacional de object_version, resolver la circularidad de la FK raíz y definir ROUTE_STEP. Opción B queda abierta si reutilizar la misma fila en múltiples snapshots es requisito esencial. No se ha elegido ni aceptado ninguna opción.

UG-SCH-10 permanece OPEN / DESIGN_RECONCILIATION_REQUIRED. No modificar encabezados ni cardinalidades antes de aceptación expresa. No se ejecutan validadores, parser, constraints, fixtures, simulaciones ni experimentos.


### 14.8. DEC-C10-063 — aceptación de Opción A y resolución estructural propuesta

El usuario acepta Opción A como arquitectura de referencia. Se registra DEC-C10-063; la aceptación no congela ni autoriza implementación.

La propuesta `C10_S_UG_OPTION_A_STRUCTURAL_RESOLUTION_DRAFT_001.md` resuelve documentalmente:
- `object_version` como revisión del registro observacional por identidad semántica; una nueva captura produce una nueva fila/version incluso sin cambio material.
- SNAPSHOT↔NODE raíz mediante FKs compuestas diferibles y transacción atómica; la FK raíz comprueba mismo snapshot y conserva la versión exacta/semantic_role.
- EDGE→NODE y PREDICATE→ROUTE mediante FKs compuestas que fijan record ID, semantic ID y snapshot.
- ROUTE_STEP como relación ordenada tipada, con exactamente un destino NODE/EDGE, mismo snapshot, índices contiguos y verificación de continuidad entre aristas y nodos adyacentes.

**Dictamen UG-SCH-10:** arquitectura seleccionada; resolución de detalle propuesta y pendiente de aceptación. La condición de circularidad queda resuelta lógicamente, pero el gate físico exige comprobar soporte de FKs diferibles en el motor elegido. Si no existe soporte equivalente, implementación BLOCKED y nueva decisión arquitectónica obligatoria.

La plantilla U_G no se ha modificado. No hay validación física, parser, constraints, fixtures, inventario, truth, revisión independiente ni ejecución. El esquema global continúa SCHEMA_NOT_CLOSED.


### 14.9. DEC-C10-064 — detalle Opción A aprobado y plantilla aplicada

El usuario aprueba la resolución de detalle y queda registrada en `DEC-C10-064_OPTION_A_STRUCTURAL_RESOLUTION_ACCEPTANCE.md`. La plantilla U_G §13 incorpora snapshot_id y referencias exactas por mismo snapshot, FK raíz compuesta/diferible, ROUTE_STEP y contrato de diff observación/estructura/evidencia/accesibilidad.

**Estado de auditoría:** DESIGN_CONTRACT_ACCEPTED; TEMPLATE_ADDENDUM_APPLIED; HEADER_RECONCILIATION_PENDING; TECHNICAL_VALIDATION_NOT_RUN. La plantilla todavía contiene encabezados abreviados heredados en §§2–6 y formulaciones históricas incompatibles; §13 es normativa, pero no se declara aún reconciliación física completa. Es obligatorio alinear los encabezados y matrices para eliminar duplicidad/ambigüedad, verificar cada fila de esquema y actualizar crosswalk IAM/FP antes de cerrar UG-SCH-10.

La compatibilidad de FKs diferibles con el motor elegido y la integridad cross-row de ROUTE_STEP son gates técnicos. No se han ejecutado parser, constraints, fixtures ni experimentos. Esquema global SCHEMA_NOT_CLOSED.


### 14.10. Primer pase de reconciliación física de encabezados

Se aplican a los encabezados de §§2–5 los campos Opción A y se incorpora ROUTE_STEP como registro normalizado. SNAPSHOT conserva snapshot_id como PK y su referencia raíz se expresa ahora como FK compuesta con snapshot_id incluido. Un control mecánico de Markdown sobre las 19 tablas de la plantilla confirma que cada encabezado, separador y fila presente tiene igual número de columnas.

**Resultado limitado:** PASS_FORMAT_COLUMN_COUNT; no equivale a validación de nombres/tipos/dominos, constraints, claves, cardinalidades ni integridad referencial. La plantilla sigue Draft y vacía de observaciones. Pendiente reconciliar los encabezados de vistas §§2–6 con el esquema normalizado §§12.7–12.10, así como ROUTE_STEP en la matriz de claves y todos los crosswalks. No se ejecutó parser/validador de aplicación, DDL ni pruebas negativas. UG-SCH-10 continúa OPEN; esquema global SCHEMA_NOT_CLOSED.


### 14.11. ROUTE_STEP incorporado a matriz de claves

Se incorpora ROUTE_STEP a la matriz de claves de §12.10 como relación operativa de secuencia. No es una tabla adicional de objetos versionados: no recibe object_version ni supersedes_record_id. Su identidad se fija por route_record_id + step_index; todas sus referencias deben conservar snapshot_id y la continuidad NODE/EDGE exige validación cross-row. La matriz mantiene separados los registros de evidencia, cobertura, evaluación y adjudicación.

El control de forma de §§2–6 y la matriz se han actualizado, pero aún falta auditoría integral de nombres de columnas y correspondencia con todas las tablas normalizadas y crosswalks IAM/FP. UG-SCH-10 permanece OPEN.


### 14.12. Auditoría integral Opción A — OAS-01…07

Se registra el informe `C10_S_UG_OPTION_A_RECONCILIATION_AUDIT_DRAFT_001.md`. Control formal: 19 tablas, sin discrepancia de recuento de columnas ni nombres de encabezado duplicados; PASS_FORMAT_ONLY.

OAS-01 CRITICAL: §§12.7–12.10 heredados no estaban reconciliados con §§13–14. OAS-02 CRITICAL: SNAPSHOT está versionado, pero snapshot_id en registros hijos no identifica una revisión exacta. OAS-03 HIGH: matriz de claves candidatas compuestas incompleta. OAS-04 HIGH: ROUTE mantenía secuencia serializada además de ROUTE_STEP. OAS-05 HIGH: crosswalk IAM/FP sin mapping explícito de nuevas columnas/claves. OAS-06 MEDIUM: checklist y autoauditoría con alcance histórico. OAS-07: PR #116 tiene base research/c10-d1-protocol-draft, no main.

Se retiró ordered_node_edge_sequence del encabezado físico ROUTE; §15 de la plantilla declara el contrato normalizado reconciliado para las partes aprobadas; crosswalk y artefactos de revisión se actualizaron. OAS-02 permanece BLOCKING_PENDING_DECISION: se recomienda snapshot_object_record_id en los registros hijos y FK compuesta a la versión exacta de SNAPSHOT. No se aplica sin aprobación expresa.

**Dictamen:** FORMAT PASS limitado; SCHEMA COHERENCE FAIL / OPEN por OAS-02; TECHNICAL VALIDATION NOT RUN; INDEPENDENT REVIEW NOT STARTED. Esquema global SCHEMA_NOT_CLOSED. Sin experimento.


### OAS-10 — Reconciliación final de las vistas físicas ROUTE_STEP y SNAPSHOT (2026-11-05)

Se detectó que la plantilla mantenía dos descripciones heredadas incompatibles con DEC-C10-065, a pesar de que §15.2/§15.3 ya estaban corregidas: §4.1 mencionaba FKs ROUTE_STEP solo «con snapshot_id», y §6 describía la FK raíz SNAPSHOT→NODE sin el componente que fija la revisión SNAPSHOT exacta. Se corrigen ambas vistas. La formulación vigente de la FK raíz es `SNAPSHOT(snapshot_id,object_record_id,unit_object_record_id,unit_id) → NODE(snapshot_id,snapshot_object_record_id,object_record_id,node_id)`; la de ROUTE_STEP exige el par exacto `snapshot_id + snapshot_object_record_id` para SNAPSHOT, ROUTE, NODE y EDGE.

La corrección se propaga mediante addenda a los contratos especializados de FK de unidad lógica, semantic_role/nodo raíz e identidad/versionado. El control de forma no se interpreta como validación de constraints. OAS-10 queda RESOLVED_DOCUMENTARILY / TECHNICAL_VALIDATION_PENDING. UG-SCH-10 permanece OPEN; no schema freeze, no revisión independiente y no validación técnica.


### OAS-11 — Matriz física explícita para referencias tipadas y procedencia (2026-11-05)

Se amplía U_G §15.4 para enumerar columnas, destinos, cardinalidades y reglas de exclusividad de CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER, así como PK/UNIQUE de EVIDENCE_REGISTER/COVERAGE_REGISTER, FKs E1/E2, soporte evidence_id, navegación evidence_ref y la regla UG-SR-A01. El crosswalk IAM/FP añade §9.4.

Esta ampliación consolida DEC-C10-061 y UG-SR-A01; no crea nuevas decisiones ni modifica el contrato de Opción A. La integridad física, CHECK/FK, cardinalidades, seguridad/custodia y reconstrucción de evidencia siguen pendientes. OAS-11 queda RESOLVED_DOCUMENTARILY / TECHNICAL_VALIDATION_PENDING.
