# C10-S — Auditoría de reconciliación del overlay IAM: FP y EDGE

**ID:** C10-S-IAM-FP-EDGE-AUDIT-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** auditoría documental asistida; no revisión independiente, no validación técnica, no ejecución.  
**Objeto:** comprobar el overlay IAM frente a los contratos y decisiones existentes, sin reabrir decisiones aceptadas.

## 1. Fuentes canónicas examinadas en la rama C10-S

- `C10_S_IAM_SERVICE_BOUNDARY_OVERLAY_AND_CROSSWALK_DRAFT_001.md`.
- `C10_S_SM_ATOMIC_PROPERTY_FP_RECONCILIATION_DRAFT_001.md` (DEC-C10-055).
- `C10_S_ABSTRACT_PARAMETER_AND_SOURCE_DESTINATION_MAPPING_MATRIX_DRAFT_001.md`.
- `C10_S_FP03_SEMANTIC_PRESERVATION_CONTRACT_DRAFT_001.md`.
- `C10_S_FSTAR_OPERATIONAL_PROPERTY_AND_ADJUDICATION_MATRIX_DRAFT_001.md`.
- `C10_S_PROPERTY_APPLICABILITY_AND_OBLIGATORINESS_MATRIX_DRAFT_001.md`.
- `C10_S_ABSTRACT_CONFIGURATION_INSTANCE_CONTRACT_DRAFT_001.md`.
- `C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md`.
- `C10_S_SYSTEM_BOUNDARY_AND_GRAPH_GRANULARITY_CONTRACT_DRAFT_001.md`.
- `C10_S_GRAPH_COVERAGE_AND_TRIVALENT_EVIDENCE_MATRIX_DRAFT_001.md`.

La reconstrucción confirma que los contratos especializados citados son artefactos de la rama/PR #116, no parte del árbol de `main`. No se atribuye a `main` la aceptación de estos borradores.

## 2. Resultado ejecutivo

**Dictamen:** el crosswalk general FP-01…FP-08 del overlay es compatible en su arquitectura de alto nivel, pero no suficientemente preciso para convertirse en esquema de inventario. Se requiere explicitar predicados primarios/secundarios, estado aplicado y anti-doble-conteo según DEC-C10-055. También se detecta una sugerencia de relación `CONTAINS_FIELD` que no figura en el catálogo mínimo de EDGE y no debe incorporarse tácitamente.

No se identifica contradicción que obligue a reabrir DEC-C10-055. La corrección consiste en alinear el overlay con decisiones y contratos existentes.

## 3. Crosswalk FP reconciliado

| Familia | Responsabilidad canónica | Reglas de overlay |
|---|---|---|
| FP-01 | Validez formal de esquema, tipos, AST, cardinalidades estructurales y representación/versionado contractual | Cobertura formal de componentes/claves, tipos/estados permitidos, AST well-formed y metadatos de contrato. No prueba equivalencia funcional. |
| FP-02 | Integridad estructural/relacional: extremos, dirección, multiplicidad, unicidad y consistencia | Resolver integridad de relaciones y referencias. No prueba por sí sola que los extremos tengan el significado correcto. |
| FP-03 | Preservación del significado funcional fuente→destino bajo mapping M | Evaluar significado de CMP/PAR/REF/RUL y POL solo si módulo condicional. No mezclar con seguridad efectiva ni compatibilidad ambiental. |
| FP-04 | Compatibilidad con entorno y versión destino | Runtime, capacidades, dependencias disponibles y reloj/entorno; disponibilidad real no se infiere de REF declarada. |
| FP-05 | Cumplimiento de seguridad y control efectivo | Permisos efectivos, secretos, exposición y política de seguridad. Preservar una POL declarada no prueba seguridad. |
| FP-06 | Aplicación efectiva | Acreditar que el paquete objetivo quedó realmente aplicado dentro de H. No basta C_dst declarada/preparada. |
| FP-07 | Verificación post-aplicación | Observar el estado realmente aplicado y verificar en él las propiedades FP-01…FP-05. No crear un segundo agregado semántico ni duplicar fallos ya adjudicados. |
| FP-08 | Procedencia, identidad de artefactos y reproducibilidad | Condición probatoria separada; no es una propiedad funcional del paquete ni compensa fallos FP-01…FP-07. |

### 3.1 Predicados primarios por familias de objeto

- **CMP-01/02:** FP-03 primario para identidad/clase funcional; FP-01 secundario para presencia y forma.
- **CMP-03:** FP-01/02 según cardinalidad estructural; FP-03 solo si la cardinalidad altera significado funcional.
- **PAR-01:** FP-03 para significado de clave; MAP-PAR-KEY-COVERAGE FP-01 es cobertura, no sustituto semántico.
- **PAR-02:** separar validez de tipo/esquema FP-01 y equivalencia de significado FP-03.
- **PAR-03/04/05:** FP-03 para dominio/valor/unidad/estado semántico; FP-01 valida representación y estados permitidos.
- **PAR-06:** FP-01 para requiredness estructural y FP-03 si cambia la opcionalidad contractual; son predicados distintos.
- **REF-01/02:** FP-03 para significado de extremo/rol/dirección; FP-02 para integridad formal.
- **REF-03/04:** FP-02 para multiplicidad/integridad; FP-03 solo si el cambio produce pérdida funcional.
- **REF-05:** FP-03 para dependencia declarada; disponibilidad/instalación efectiva corresponde a FP-04/C_dep.
- **RUL-01…05:** FP-03 para lógica, ámbito, efecto, precedencia y temporalidad; AST bien formado FP-01 y referencias de operandos FP-02.
- **POL-01…04:** FP-03 condicional cuando POL se incluya; permisos efectivos/seguridad FP-05. POL permanece fuera del núcleo confirmatorio mínimo por DEC-C10-053.
- **POL-05:** FP-05; excluir del agregado FP-03.
- **MET-01:** FP-01/FP-04 para validez de contrato/versión y compatibilidad.
- **MET-02/04:** FP-08 para procedencia e identidad de artefacto; hash/nombre no demuestra identidad funcional.
- **MET-03:** FP-03 condicional para semántica de extensión desconocida; FP-01 reconoce esquema/versión y FP-08 registra procedencia.

La misma observación puede vincularse a más de una familia, pero debe asignarse una causa/predicado primario. No contar un único defecto como varios fallos confirmatorios independientes.

### 3.2 Destino declarado y destino aplicado

Mantener separados:
- `C_src`: configuración fuente congelada.
- `C_dst^decl`: paquete destino declarado/preparado.
- `C_dst^applied`: estado realmente aplicado.
- `E_dst`: entorno destino, externo al paquete.
- `M`: mapping de evaluación versionado.

FP-01/02/03 se evalúan sobre la comparación fuente→estado aplicado mediante M; el paquete declarado no sustituye el estado aplicado. FP-06 acredita aplicación y FP-07 observa/verifica post-aplicación. No crear un predicado independiente `APPLIED-STATE-SEMANTICS` que duplique FP-03.

## 4. Catálogo EDGE existente y corrección

El contrato de frontera/granularidad ya define estos tipos mínimos de relación:

1. `depende_de`
2. `carga/ejecuta`
3. `invoca/expone`
4. `autoriza`
5. `asigna/consume_recurso`
6. `transforma/entrega`
7. `lee/escribe_estado`
8. `comparte`
9. `observa/mide`
10. `controla/valida`
11. `comunica_con`
12. `provisiona`
13. `afecta/puede_afectar`
14. `sustituye_funcionalmente`

El overlay no debe añadir `CONTAINS_FIELD` ni otra relación no recogida aquí sin una decisión y reconciliación del catálogo. Para descomponer un manifiesto/archivo mixto:
- crear registros NODE a granularidad campo/clave cuando la semántica lo exija;
- conservar referencia de agrupación mediante `parent_catalog_id`/metadatos de objeto donde corresponda;
- registrar aristas solo cuando una relación real y su tipo estén sustentados;
- no convertir contención documental en dependencia causal ficticia.

Los nombres de relación anteriores son vocabulario de contrato, no aristas observadas. La plantilla EDGE no contiene instancias verificadas.

## 5. Correspondencia con los diez registros U_G

La plantilla U_G ya contiene NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT, EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER. El overlay es una especialización de dominio y no debe crear tablas paralelas.

Brecha identificada: los atributos sugeridos en el overlay (`boundary_class`, `logical_service_id`, `object_scope`, `semantic_inclusion_rationale`, `sensitivity_class`) no son columnas nuevas automáticamente autorizadas. Antes de añadir columnas hay que decidir si se mapean a campos existentes (p. ej. `class`, `semantic_role`, `owner/boundary`, `notes/unknowns`, `parent_catalog_id`, `contract_intent`) o si existe una brecha real. No se debe duplicar `unit_id`, `object_record_id`, `parent_catalog_id` ni los campos de evidencia/cobertura.

P2 es una frontera analítica transversal, no una clase mutuamente excluyente ni una nueva tabla. Su presencia se representa mediante los objetos y relaciones pertinentes ya contemplados en U_G y el identificador de frontera del estudio cuando se defina; no mediante un tipo de arista inventado.

## 6. Hallazgos y tratamiento

| ID | Hallazgo | Severidad | Tratamiento |
|---|---|---|---|
| IAM-A01 | FP-07 descrito de forma demasiado genérica como verificación funcional; debe decir verificación post-aplicación de FP-01…05 | Media | Corregir texto y mantener FP-06 separado |
| IAM-A02 | Crosswalk no explicita asignación primaria/secundaria por propiedad atómica | Alta | Incorporar tabla resumida reconciliada con DEC-C10-055 |
| IAM-A03 | `CONTAINS_FIELD` no pertenece al catálogo mínimo EDGE | Alta | Retirar; usar descomposición NODE y parent_catalog_id sin inventar relación |
| IAM-A04 | Atributos overlay podrían interpretarse como columnas nuevas ya aprobadas | Alta | Marcar como atributos candidatos y exigir field-to-column mapping antes de schema |
| IAM-A05 | Debe hacerse explícita la separación C_dst^decl/C_dst^applied/E_dst/M y FP-06/FP-07 | Alta | Incorporar en overlay |
| IAM-A06 | FP-08 puede confundirse con resultado funcional | Media | Reportarlo como validez probatoria separada |

## 7. Dictamen de cierre de esta auditoría

- **PASS_DOCUMENTAL:** arquitectura general del overlay y reutilización de los diez registros U_G.
- **CORRECTION_REQUIRED:** detalle FP, estado aplicado, relación no catalogada y mapeo de atributos overlay.
- **OPEN:** schema final, cardinalidades/FK, field-to-column mapping, crosswalk de cada predicado a NODE/EDGE/PREDICATE/SNAPSHOT, IAM por instancia, unidad de aleatorización/interferencia.
- **NOT_ASSESSED:** integridad técnica, parser, claves/FK, seguridad, permisos, validador, inventario real, revisión independiente y ejecución.

La auditoría es `AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT`. No valida la verdad del inventario ni la viabilidad de un sistema real.

**Restricción de ejecución:** `scientific_execution=false`; `execution_authorized=false`. No se crearon nodos, aristas, truth, fixtures ni datos sintéticos.


## 8. Addendum DEC-C10-064 — referencias versionadas bajo Opción A

La aprobación de Opción A exige que el crosswalk de aristas distinga el ID padre E01–E23, la identidad atómica y las referencias a registros NODE concretos. EDGE.source_node_record_id/target_node_record_id fijan los extremos exactos dentro del mismo snapshot; source_node_id/target_node_id permanecen como IDs semánticos para trazabilidad. E07 continúa siendo regla lógica, no EDGE. E22 no autoriza inventar destinos. La nueva FK no convierte ninguna arista candidata en observada. IAM/FP debe reconciliar sus claves compuestas y snapshot_id antes del cierre.


## 9. Reconciliación estructural Opción A — DEC-C10-064 y OAS-01…07

EDGE conserva IDs semánticos edge_id/source_node_id/target_node_id y añade source_node_record_id/target_node_record_id para pinning exacto; PREDICATE conserva route_id y añade route_record_id. ROUTE_STEP sustituye ordered_node_edge_sequence como secuencia canónica. Todas las referencias interobjeto deben incorporar snapshot_id y resolver a claves candidatas explícitas.

**OAS-02 sigue bloqueante:** snapshot_id no selecciona una versión exacta de SNAPSHOT cuando SNAPSHOT tiene object_version por DEC-C10-062. El crosswalk IAM/FP no puede declarar completada la integridad de mismo snapshot hasta que exista pinning al object_record_id de SNAPSHOT o una decisión que elimine esa multiplicidad de versiones.


### 10. DEC-C10-065 — exact snapshot revision pinning

EDGE/PREDICATE/ROUTE_STEP y los restantes registros dependientes incorporan `snapshot_object_record_id` obligatorio además de `snapshot_id`. Toda referencia interobjeto debe fijar la misma revisión exacta de SNAPSHOT mediante FK compuesta a SNAPSHOT(`snapshot_id`, `object_record_id`). Los record IDs exactos de NODE/EDGE/ROUTE se mantienen en sus propias FKs; los IDs semánticos no sustituyen a las claves de registro.

OAS-02 queda resuelto documentalmente; compatibilidad física y orden exacto de claves/FKs siguen pendientes. No se declara cierre del crosswalk.
