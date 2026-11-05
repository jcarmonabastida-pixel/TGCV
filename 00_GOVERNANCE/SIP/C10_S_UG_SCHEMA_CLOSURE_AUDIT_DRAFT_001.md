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

**Severidad:** MEDIA · **Estado:** CORRECTION_REQUIRED.

El encabezado identifica `unit_object_record_id` como “FK NODE.object_record_id”, pero DEC-C10-059 y el contrato asociado requieren la pareja compuesta:

`SNAPSHOT.(unit_object_record_id, unit_id) → NODE.(object_record_id, node_id)`

La columna está presente; la etiqueta del encabezado no expresa la restricción completa.

**Corrección requerida:** actualizar la descripción del campo para indicar explícitamente que forma parte de una FK compuesta junto con `unit_id`. Mantener la decisión DEC-C10-059 sin reabrirla.

### UG-SCH-03 — Vocabulario de semantic_role y rol raíz no formalizados

**Severidad:** ALTA · **Estado:** PROPOSAL_CREATED; pending acceptance.

El contrato de DEC-C10-059 exige que el NODE destino de SNAPSHOT tenga `semantic_role=LOGICAL_SERVICE_UNIT`. Sin embargo, la plantilla no presenta un dominio controlado completo para `semantic_role`, ni el crosswalk de roles U_G consultado define explícitamente cómo se incorpora ese rol raíz a los 23 roles existentes.

**Resolución propuesta:** se creó `C10_S_UG_SEMANTIC_ROLE_AND_LOGICAL_ROOT_CONTRACT_DRAFT_001.md`. Distingue semantic_role de parent_catalog_id y boundary_class; propone vocabulario controlado y crosswalk no uno-a-uno N01–N23; conserva DEC-C10-059 y fija exactamente un nodo raíz por combinación unidad/snapshot/scope. Pendiente aceptación del usuario y validación técnica.

### UG-SCH-04 — source_provenance: conflicto entre §10.6 y §12.7

**Severidad:** MEDIA · **Estado:** OPEN.

El §10.6 declara `source_provenance` obligatorio en todas las tablas de registro. El esquema normalizado §12.7 no lo incluye entre los campos comunes de las cinco tablas de objetos y §12.1 lo registra canónicamente en EVIDENCE_REGISTER.

**Corrección requerida:** elegir y documentar una sola regla. Recomendación: mantener la procedencia completa en EVIDENCE_REGISTER, enlazada mediante CLAIM_EVIDENCE_LINK; no duplicarla como texto libre en cada fila de objeto. Si se necesita una referencia de procedencia directa, definirla como campo de navegación tipado, no como segundo expediente. Esta aclaración no debe debilitar la obligación de procedencia de cada afirmación observada.

### UG-SCH-05 — CLAIM_EVIDENCE_LINK: destino de cobertura no resuelto

**Severidad:** ALTA · **Estado:** OPEN.

§12.10 atribuye a COVERAGE_REGISTER vínculos claim-evidence 0..n. Sin embargo, CLAIM_EVIDENCE_LINK.claim_target_id se define como `object_record_id`, mientras que COVERAGE_REGISTER tiene `coverage_scope_id` como clave y no contiene `object_record_id`.

**Corrección requerida:** definir cómo se enlazan afirmaciones de cobertura: o bien `claim_target_type=COVERAGE_SCOPE` con `claim_target_id=coverage_scope_id`, o bien mediante un objeto de registro versionado explícito. La elección debe ser consistente con el dominio de claim_target_type y con las reglas de integridad.

### UG-SCH-06 — FK polimórficas de CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER

**Severidad:** ALTA · **Estado:** OPEN.

Los registros de vínculo, evaluación y adjudicación utilizan `object_type + object_record_id` para identificar objetos de varias tablas. El contrato indica “FK tipada”, pero no especifica un mecanismo de integridad referencial que garantice que la pareja resuelva a una y solo una tabla/registro válido, ni los dominios cerrados de object_type/claim_target_type.

**Corrección requerida:** definir explícitamente una de estas estrategias: (a) FK específicas por tipo y restricciones de exclusividad; (b) registro/supertipo común de objetos con clave global; o (c) otro mecanismo formal equivalente. La solución debe incluir COVERAGE_REGISTER si se le atribuyen vínculos. No declarar integridad física resuelta antes de especificar el mecanismo.

### UG-SCH-07 — alcance de unicidad de object_record_id y supersedes_record_id

**Severidad:** MEDIA · **Estado:** OPEN.

El esquema declara object_record_id “único”, pero la matriz de claves usa pares `object_record_id + semantic_id` y el diccionario habla de unicidad por tabla. No queda totalmente explícito si object_record_id es global al inventario o único dentro de cada tabla. Tampoco se fija de forma suficiente si supersedes_record_id solo puede apuntar a una fila anterior de la misma tabla y del mismo objeto semántico.

**Corrección requerida:** fijar el ámbito de unicidad y las restricciones de supersedes: mismo tipo de objeto, misma identidad semántica, versión estrictamente anterior, sin ciclos y con trazabilidad de sustitución. Mantener la FK compuesta SNAPSHOT→NODE conforme a DEC-C10-059.

### UG-SCH-08 — estados de SNAPSHOT y boundary_class

**Severidad:** BAJA · **Estado:** CLARIFICATION_REQUIRED.

La fila de esquema de SNAPSHOT usa `observed_state=NA`, mientras que el contrato común describe estados trivalentes y NA por no aplicabilidad. NODE utiliza boundary_class=NA en su fila de esquema vacía. Ambas filas están rotuladas como filas de esquema, no como observaciones.

**Corrección requerida:** añadir una nota explícita de que esos NA son marcadores de plantilla y no valores asignados a registros reales. En filas reales, NA requiere justificación conforme al contrato. No cambiar la regla sustantiva de DEC-C10-059.

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
| FK compuesta SNAPSHOT→NODE | DEFINED_DOCUMENTALLY; etiqueta física por corregir |
| EDGE parent/atomic IDs y extremos | CORRECTED_DOCUMENTALLY; second pass pending |
| semantic_role / nodo raíz | ACCEPTED_DOCUMENTALLY (DEC-C10-060); physical validation pending |
| Procedencia y CLAIM_EVIDENCE_LINK | OPEN |
| FK polimórficas | OPEN |
| Unicidad/versionado/supersedes | OPEN |
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
