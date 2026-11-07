# C10-S — IAM: overlay de frontera de servicio y crosswalk del inventario U_G

**ID:** C10-S-IAM-SERVICE-OVERLAY-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-05  
**Estado:** propuesta documental; no aprobada, no congelada, no instanciada ni validada.  
**Base aceptada:** DEC-C10-057 y DEC-C10-058.  
**Regla de continuidad:** reutilizar `C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md`; no crear un segundo inventario paralelo.

## 1. Propósito

Especializar la plantilla U_G ya existente para el microdominio de migración de configuración de una instancia lógica de servicio software. Este documento es un overlay/crosswalk: añade atributos de clasificación P0/P1/P2 y relaciones específicas del dominio sin duplicar los registros canónicos NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT, EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER.

No contiene inventario observado. La plantilla permanece vacía y los estados técnicos no se alteran: observed_state=?, coverage_status=NONE, evidence_status=MISSING cuando no hay fuente observada; no se infiere 0 por ausencia de documentación.

## 2. Reconstrucción histórica y decisión de reutilización

La reconstrucción confirma trabajo previo compatible:
- La plantilla U_G ya define diez registros relacionados y campos para identidad, versión, dependencias, evidencia, cobertura, evaluación y adjudicación.
- El protocolo de procedencia ya regula evidencia, triangulación, cegamiento, conflicto y adjudicación.
- La matriz de cobertura ya separa verdad estructural (1/0/?), cobertura (COMPLETE/PARTIAL/NONE), estado de evidencia (AVAILABLE/MISSING/CONFLICTING) e intención contractual.
- El contrato de frontera/granularidad ya regula cuándo separar/agregar nodos, dependencias directas/transitivas, recursos compartidos, servicios externos, rutas y universo.
- El contrato de identidad/snapshots ya separa TID/SID/RID/EID y correspondencias entre versiones.
- El perfil P0/P1/P2 y DEC-C10-058 aportan una clasificación específica de contenido declarativo, entorno y frontera causal.

Por tanto, no se justifica una plantilla de inventario nueva. La brecha real es un crosswalk de dominio y un conjunto mínimo de atributos/relaciones que permitan clasificar cada objeto existente sin alterar su semántica previa.

## 3. Regla de modelado

### 3.1 P0 y P1 son clases de objeto/contexto

Cada NODE del inventario U_G puede tener:
- `boundary_class`: `P0_CONFIG`, `P1_ENVIRONMENT`, `P2_CAUSAL_ONLY` o `DUAL_P0_P1` cuando un mismo artefacto físico contiene campos de ambas clases y no puede dividirse sin perder integridad;
- `logical_service_id`: servicio lógico al que pertenece o al que sirve;
- `object_scope`: `SERVICE_CONFIG`, `ENVIRONMENT`, `EXTERNAL_SERVICE`, `MAPPING`, `INTERVENTION`, `ALTERNATIVE_PATH`, `MEASUREMENT`, `OUTCOME_VALUE`, `OTHER`;
- `semantic_inclusion_rationale`: criterio por el que se incluye/excluye de P0;
- `sensitivity_class`: clasificación de sensibilidad sin incluir secretos en claro.

P2 no se asigna como una clase excluyente. Se representa mediante pertenencia/relación al `causal_boundary_id` y enlaces EDGE a intervención, rutas, recursos, agentes, medición y resultados. Un nodo P0/P1 puede estar en P2 si causalmente pertinente. `P2_CAUSAL_ONLY` se reserva a nodos analíticos que no son contenido P0 ni contexto P1 (por ejemplo, asignación Z, adjudicación u oráculo).

### 3.2 Descomposición semántica

Manifiestos y variables de entorno se dividen por campo/clave cuando su semántica difiere. No se crea un nodo único por fichero si contiene propiedades P0 y P1. Si la descomposición destruye integridad/versionado, registrar nodo padre y nodos/campos hijos relacionados por EDGE `CONTAINS_FIELD` o relación equivalente ya admitida por el catálogo, sin inventar una clase de arista nueva hasta reconciliar el catálogo.

Secretos: registrar referencia/identificador/versión en P0; material secreto nunca se copia al registro. La disponibilidad del secreto, ACL y proveedor se representan en P1/P2. Datos persistentes fuera de P0 por defecto. Servicios externos opacos conservan nodo/dependencia y predicados ? donde la observabilidad no alcance.

## 4. Crosswalk a los diez registros U_G

| Registro U_G existente | Aplicación en C10-S servicio | No duplicar / no inferir |
|---|---|---|
| NODE | Servicio lógico, paquete C, elementos CMP/PAR/REF/RUL, entornos, runtime, recursos, externos, adaptador B, alternativas, oráculo | No crear una tabla nueva para P0/P1 |
| EDGE | Contención, referencia, dependencia, provisión, invocación, compartición, fallback, mapping y afectación | No inferir aristas por proximidad o nombres |
| ROUTE | Ruta focal τ2/F*, A1/A2, manual, fallback, externa y recuperación | Ruta no observada queda ? |
| PREDICATE | Requisitos de identidad/versión, esquema, integridad, compatibilidad, permisos, disponibilidad, recursos, aplicación, seguridad | No confundir truth lógico con estado de evidencia |
| SNAPSHOT | Estado C_src, E_src/E_dst, provisión B, mapping, C_dst_decl, C_dst_applied y cambios | No comparar snapshots con frontera/versiones incompatibles |
| EVIDENCE_REGISTER | Fuentes/manifiestos, contratos, SBOM, logs, inventarios y procedencia permitida | Sin fuente no hay observación |
| CLAIM_EVIDENCE_LINK | Vínculos entre afirmación concreta y evidencia | Mantener cardinalidad 0..n; evidence_ref solo navegación opcional |
| COVERAGE_REGISTER | Universo declarado, sistemas/repositorios/entornos cubiertos, método, límites y Runknown | NONE/PARTIAL no son 0 |
| EVALUATOR_ASSESSMENT | Evaluación independiente/cegada de predicados y fuentes | Mantener roles y cegamiento del protocolo |
| ADJUDICATION_REGISTER | Resolución de conflicto, identidad, clasificación y evidencia | No resolver desacuerdo por conveniencia |

Los nombres de relaciones EDGE deben mapearse a los tipos ya definidos en U_G. Este overlay no amplía el catálogo de aristas ni crea códigos sin reconciliación.

## 5. Crosswalk funcional FP-01…FP-08

| Familia FP | Objeto principal | Contexto requerido | Resultado probatorio |
|---|---|---|---|
| FP-01 esquema/contrato | C / MET | versión del parser/validador de esquema | compatibilidad estructural del paquete |
| FP-02 integridad | C y mapping M | origen, hash, cadena de custodia | integridad verificable |
| FP-03 preservación semántica | C_src ↔ C_dst_decl | contrato funcional, mappings y reglas | preservación de propiedades declaradas |
| FP-04 compatibilidad destino | C_dst_decl × E_dst | runtime, versiones, dependencias | compatibilidad bajo entorno delimitado |
| FP-05 seguridad | C × E_dst | referencias, secretos, permisos efectivos, políticas aplicadas | evaluación separada de declaración y seguridad efectiva |
| FP-06 aplicación | C_dst_decl × mecanismo de aplicación × E_dst | logs/estado posterior | aplicación observada, no mera declaración |
| FP-07 verificación funcional | C_dst_applied × F* | entradas/salidas, tolerancias, horizonte y oráculo | cumplimiento funcional según criterio ex ante |
| FP-08 trazabilidad | C, M, E, snapshots y oráculo | IDs, versiones, hashes, procedencia, cobertura | cadena auditable completa |

FP-01/02/03 se centran en paquete/mapping; FP-04/05/06/07 cruzan el paquete con entorno y estado aplicado; FP-08 es gate de trazabilidad. Esta asignación es un crosswalk de trabajo: debe reconciliarse con las definiciones canónicas FP-01…08 antes de declarar cierre.

## 6. Atributos mínimos propuestos por elemento de inventario

Estos son campos de overlay, no una nueva tabla. Su ubicación concreta (NODE, EDGE, ROUTE o PREDICATE) se decide según la entidad representada:
1. ID persistente y tipo de objeto existente.
2. logical_service_id y versión del contrato del servicio.
3. boundary_class P0/P1/dual/P2-only.
4. object_scope.
5. parent/child y regla de descomposición si aplica.
6. versión/identidad TID/SID/RID/EID cuando proceda.
7. origen/custodio/owner y sistema/entorno.
8. dependencia directa/transitiva/compartida y relaciones EDGE.
9. sensibilidad y tratamiento de secretos.
10. temporalidad: baseline/pre-Z, post-B, post-transformación, post-aplicación.
11. evidence_status, coverage_status y observed_state separados.
12. rationale de inclusión/exclusión y unknown_reason.
13. relación con F*, FP y ruta focal/alternativa.
14. cambio respecto al snapshot previo y compatibilidad de granularidad.

No todos los campos son obligatorios en todas las entidades. El contrato de esquema debe especificar cardinalidad, dominios, claves y FK en una fase posterior, sin rellenar valores inventados.

## 7. Mapeo inicial de elementos del microdominio (tipos, no instancias)

| Familia conceptual | Clase por defecto | Registro canónico | Nota |
|---|---|---|---|
| Identidad/contrato de servicio lógico | P0 metadata + P2 frontera | NODE/MET, EDGE | Identidad estable del servicio en el estudio |
| Paquete declarativo C_src/C_dst_decl | P0 | NODE/SNAPSHOT | Distinguir declarado de aplicado |
| CMP/PAR/REF/RUL | P0 | NODE/PREDICATE/EDGE | Catálogo por definir |
| Manifiesto/variables | P0/P1 por campo | NODE/EDGE | No clasificar fichero entero |
| Runtime/binario/infraestructura | P1 | NODE/EDGE/SNAPSHOT | Versionado y dependencias |
| Permisos efectivos/ACL | P1 | NODE/PREDICATE/SNAPSHOT | POL declarada no equivale a permisos |
| Secreto material | P1, sensible | NODE con referencia protegida | No persistir valor secreto |
| Datos persistentes | P1/P2, fuera de P0 por defecto | NODE/EDGE/SNAPSHOT | Dependencia/estado externo |
| Servicio externo opaco | P1/P2 | NODE/EDGE/PREDICATE | Incertidumbre explícita |
| Mapping M/script | artefacto de transformación P2; entorno P1 si aplica | NODE/EDGE/SNAPSHOT | Separado de C_src |
| Adaptador/sidecar B | P1 técnico + P2 intervención | NODE/EDGE/SNAPSHOT | Dependencias transitivas obligatorias |
| A1/A2/fallback/manual | P2 y P1 donde haya componentes | ROUTE/NODE/EDGE | No asumir inexistencia |
| Logs/oráculo/adjudicación | P2-only | EVIDENCE_REGISTER/PREDICATE/ASSESSMENT | Cegamiento y filtración controlados |

La tabla define familias abstractas, no presencia real. Todas las instancias concretas comienzan sin evidencia y cobertura NONE hasta que una captura autorizada las sustente.

## 8. Reglas de integridad y estados

- No duplicar registros ni IDs ya definidos por la plantilla U_G.
- No redefinir observed_state, evidence_status, coverage_status ni contract_intent.
- No convertir ausencia de registro en ausencia estructural.
- No inferir completitud de grafo por haber completado las diez tablas.
- No inferir ausencia de ruta alternativa por no hallar implementación.
- Mantener Runknown y dependencias opacas.
- Preservar cardinalidad CLAIM_EVIDENCE_LINK 0..n y evidence_ref opcional 0..1 como referencia de navegación.
- No crear truth DGP ni valores de parámetros en este overlay.
- El overlay no autoriza inspección, captura, instalación, ejecución ni validación.

## 9. Brechas que sí requieren decisiones/contratos posteriores

1. Taxonomía CMP y descomposición de componentes.
2. Catálogo de claves PAR, tipos y dominios finitos ya propuestos.
3. Gramática y alcance de REF/RUL y correspondencia con FP-03.
4. Cardinalidades, unicidad, FK y normalización de relaciones.
5. Crosswalk definitivo de nombres de EDGE al catálogo U_G existente.
6. Contratos de snapshots por cada clase de objeto y momentos temporales.
7. Reconciliación exacta de FP-01…08 con sus contratos previos.
8. Unidad de aleatorización/analítica e interferencia.

## 10. Dictamen

Se reutiliza la plantilla U_G existente y se propone un overlay semántico específico para la unidad de servicio aceptada. No se justifica recrear el inventario ni ampliar U_G sin necesidad. La propuesta conserva la separación P0/P1/P2 y añade el crosswalk funcional necesario para preparar IAM.

**Estado:** DRAFT. No aceptado ni congelado; no instanciado, no validado, no ejecutado. Sin inventario observado, truth, fixtures, datos sintéticos ni evidencia empírica. `scientific_execution=false`; `execution_authorized=false`.


## 11. Reconciliación documental FP/EDGE — auditoría IAM-A01…A06

La revisión contra DEC-C10-055 y los contratos FP/U_G identificó precisiones obligatorias antes de schema:
- FP-07 es verificación post-aplicación de FP-01…FP-05 sobre C_dst^applied; FP-06 acredita aplicación efectiva.
- FP-08 es procedencia/reproducibilidad probatoria, reportada separadamente de la conformidad funcional.
- El mapping primario/secundario por propiedad atómica se rige por la tabla detallada en `C10_S_IAM_FP_EDGE_CROSSWALK_AUDIT_DRAFT_001.md`; no se simplifica a una familia única para propiedades compuestas.
- Se retira la sugerencia de relación `CONTAINS_FIELD`: no está en el catálogo EDGE. La descomposición se representa mediante NODE a granularidad adecuada y parent_catalog_id/metadatos cuando corresponda, sin inventar aristas.
- Los atributos overlay boundary_class/logical_service_id/object_scope/semantic_inclusion_rationale/sensitivity_class son candidatos, no columnas aprobadas. Requieren field-to-column mapping antes de cambiar la plantilla.
- Se explicitan C_src, C_dst^decl, C_dst^applied, E_dst y M. No se añade APPLIED-STATE-SEMANTICS como nuevo predicado que duplique FP-03.

**Estado:** corrección documental pendiente de aceptación; no se modifican DEC-C10-055 ni los contratos U_G. Véase auditoría IAM FP/EDGE.


## 12. Crosswalk de atributos IAM a columnas U_G

El detalle de correspondencia se desarrolla en `C10_S_IAM_FIELD_TO_COLUMN_CROSSWALK_PROPOSAL_DRAFT_001.md`. La plantilla U_G §12.7 ya define columnas comunes y extensiones por registro; los atributos overlay no se convierten automáticamente en nuevas columnas.

Conclusión provisional: logical_service_id se representa mediante NODE raíz y SNAPSHOT.unit_id; object_scope se mapea a semantic_role/vocabulario tipado; rationale a notes/unknowns; sensibilidad a confidentiality/access_ref del expediente de evidencia; parent/child mediante parent_catalog_id sin EDGE de contención. P2 sigue siendo perímetro transversal, no clase.

La única extensión candidata que parece justificar campo propio es NODE.boundary_class ∈ {P0_CONFIG, P1_ENVIRONMENT, DUAL_P0_P1}. No se añade a la plantilla hasta aceptación explícita y cierre de FK con unit_id/node_id.


## 13. Addendum DEC-C10-064 — compatibilidad con Opción A

El overlay IAM se conserva como capa de clasificación/crosswalk, no como mecanismo alternativo de pertenencia. Los registros NODE/EDGE/ROUTE/PREDICATE quedan ligados a snapshot; las referencias EDGE→NODE y PREDICATE→ROUTE deben fijar record IDs exactos del mismo snapshot. SNAPSHOT conserva la unidad lógica y su NODE raíz exacto. Los atributos IAM no sustituyen estas FKs ni crean aristas no catalogadas. La matriz field-to-column deberá actualizarse para incluir snapshot_id, record IDs tipados y ROUTE_STEP.
