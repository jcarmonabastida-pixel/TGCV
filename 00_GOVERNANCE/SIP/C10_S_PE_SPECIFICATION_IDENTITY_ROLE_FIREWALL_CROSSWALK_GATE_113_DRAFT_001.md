# C10-S — Gate 113: recuperación de PE y auditoría de identidades, interfaces y firewall

**ID:** C10-S-GATE-113-PE-CROSSWALK-001  
**Fecha:** 2026-11-15  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 Draft  
**Estado:** PE_ARTIFACT_LOCATED_AND_RECOVERED / PE_LOGICAL_INTERFACES_RECONCILED / PHYSICAL_IDENTITY_CROSSWALK_PARTIAL / SERIALIZATION_PARTIAL / FIREWALL_CONCEPTUAL_NOT_VERIFIED / IMPLEMENTATION_NOT_READY / NO_EXECUTION / NO_FREEZE.  
**Precedencia:** gobernanza de `main`; decisiones aceptadas dentro de su alcance; PE integrated technical specification; DGP temporal/role contract; Gates 98–112; Gate 109/110; B1/Need PE interface crosswalk; U_G and identity/snapshot contracts.  
**Tipo:** reconstrucción documental asistida, no revisión independiente, no inspección de datos poblados, no auditoría técnica de permisos ni de código.

---

## 1. Pregunta y dictamen ejecutivo

Gate 113 verifica si existe una especificación PE recuperable y qué parte de la identidad, interfaces y separación Generator–Analyzer–Evaluator está realmente definida frente a lo que continúa abierto.

**Hallazgo correctivo:** el artefacto PE sí existe en la rama de trabajo y se recupera en la ruta exacta:

`00_GOVERNANCE/SIP/C10_S_PE_INTEGRATED_TECHNICAL_SPECIFICATION_AND_IMPLEMENTATION_CONTRACT_DRAFT_001.md`

ID interno `C10-S-PE-TECH-CONTRACT-001`, fecha 2026-11-11, blob SHA `5b3ba5256e42f388983cf408f5b51e0a4b9b86bb`.

Por tanto, la afirmación de Gate 112 `PE_STANDALONE_ARTIFACT_NOT_LOCATED` fue un falso negativo de recuperación y queda corregida por este gate. No era correcto mantener la ausencia como dependencia documental. La existencia del artefacto no significa que esté aprobado, implementado, físicamente completo ni listo para ejecución.

**Dictamen PE recuperado:** `PE_RECONCILED_DOCUMENTALLY / TECHNICAL_CONTRACT_PARTIAL / IMPLEMENTATION_NOT_READY / NOT_IMPLEMENTED / NOT_EXECUTED`.

La especificación sí contiene: arquitectura lógica de seis responsabilidades; interfaces Generator→Proyector/Sealer→Analyzer→Evaluator; categorías de identidad y versionado; reglas temporales y de snapshots; separación truth/observed; salida analítica por estimando; capas de validación y gates.

No contiene un crosswalk físico completo, serialización global, esquema ejecutable, prueba de integridad referencial, permisos efectivos ni evidencia de firewall. Los gates G-MAT, G-SCHEMA, G-ROLE, G-TEST, G-REPRO y G-AUTH siguen siendo bloqueos para implementación confirmatoria.

## 2. Fuentes recuperadas

| Artefacto | Alcance utilizado | Límite |
|---|---|---|
| PE Integrated Technical Specification, §§1–19/20 | Arquitectura lógica, identidades, tiempo, serialización, manifiestos, salida Analyzer, preparación y gates | Contrato parcial; no schema físico ni implementación |
| DGP Temporal and Role Contract, §§2–3, 15, 17 y 28 | UE/UA/UO, Z, tiempo, truth/observed y mecanismo de interferencia | Propuesta DGP; parámetros y mappings materiales abiertos |
| Gate 109 | Roles, no equivalencias y cardinalidades UE/UA/U_G/instancia/ruta | Mapping material OPEN |
| Gate 110 | Arquitecturas de interferencia, ITT-D2, g_A y C4 | Ninguna arquitectura seleccionada |
| B1/Need PE Generator–Analyzer–Evaluator Interface Crosswalk | Frontera entre E1/E2 y Analyzer PE | Crosswalk documental; no aprobación física |
| B1/Need Observation Model to PE Bundle Reconciliation | Proyección de observaciones por estimando | PE bundle mapping no aprobado |
| Gate 112 | Reconciliación G111-01…12 | Su afirmación de PE no localizado queda corregida aquí |

El documento PE aparece además en el inventario de ficheros modificados de PR #116. No se ha inferido su existencia por el título de un Gate anterior: se ha recuperado el contenido completo por la ruta anterior.

## 3. Arquitectura lógica e interfaces

PE define seis responsabilidades lógicas, no servicios desplegados:

1. **Orquestador:** selecciona contrato/escenario autorizado, fija identidad del run, ordena etapas y controla gates.
2. **Generator:** construye DGP, estados, mecanismos, potenciales y truth restringida.
3. **Proyector/Sealer:** aplica el modelo de observación, elimina campos reservados, verifica integridad y libera el bundle observado.
4. **Analyzer:** reconstruye constructos y estima únicamente con bundle y documentación permitidos.
5. **Evaluator/Adjudicator:** compara output sellado con truth después del sellado.
6. **Artifact/Provenance Store:** conserva artefactos inmutables, referencias, versiones, hashes, logs y reportes.

La secuencia lógica es:

`Generator → Proyector/Sealer → Analyzer → (sellado inmutable) → Evaluator`

El Orquestador no puede servir de canal de truth. El Sealer no adjudica resultados. El Analyzer no lee truth, potenciales, parámetros generadores ni semilla secreta. El Evaluator no modifica retroactivamente el output sellado.

**Distinción de estado:** la arquitectura y las reglas de intercambio están definidas documentalmente; la seguridad y aislamiento efectivos no están probados. La separación nominal de módulos no constituye un firewall.

## 4. Crosswalk de identidades: qué cubre PE y qué no

| Dominio | Identidad/objeto existente | Alcance documental PE | Estado del mapping físico |
|---|---|---|---|
| Contrato de prueba | `test_id + version` | Identifica contrato/familia | Campo físico/run binding no verificado |
| Fixture | `fixture_id + fixture_hash` | Identifica fixture y contenido | No es unidad ni asignación |
| Escenario | `scenario identity` | Identifica escenario | Evitar metadatos reveladores para Analyzer; clave física OPEN |
| Ejecución | `run identity` | Linaje con commit, versiones, configuración y referencias | Envelope y PK física OPEN |
| Unidad | `unit_id`, UE | Unidad experimental/potenciales y resultados | Relación con NODE y PK física OPEN |
| Asignación | `assignment_unit`, UA, Z | Separada de UE y UO | PK, cardinalidad, RNG/vector y mapping UA→Z OPEN |
| Clúster | Clave de cluster si procede | Previsto condicionalmente por DGP | Definición y mapping no fijados |
| Observación | UO | Medición repetida/longitudinal | UO→UE/instancia/ventana OPEN |
| Servicio/contrato | `contract_id/version` | Identidad de contrato de servicio | Alcance de decisión aplicable; no equivale a UE |
| Instancia CMP | `instance_id + instance_version` | Identidad de instancia de configuración/servicio | Cardinalidad UE↔instancia requiere armonización |
| Transformación | TID/SID/RID/EID | Especificación, versión, realización e instancia/ocurrencia separadas | Mapping del artefacto focal DEC-C10-067 a RID sigue candidato, no confirmado |
| U_G | `unit_id = NODE.node_id`; revisión por `object_record_id/object_version` | Inventario lógico versionado | FK física y mapping UE↔U_G OPEN |
| Snapshot | `snapshot_id + snapshot_object_record_id` | Pinning exacto; no resolver por latest | Validación física no ejecutada |
| Ruta | `route_id` versionada | Ruta funcional/transformacional, no unidad experimental | Roster y relación UE/instancia×ruta OPEN |
| Evidencia | `evidence_id`, `coverage_scope_id`, links/registers | Procedencia, cobertura y binding | Schema físico/perfiles de serialización OPEN |
| Output Analyzer | Resultado estructurado por estimando | Unidad, población, régimen, estimación, incertidumbre, supuestos, dictamen, cobertura, referencias y hash | Contrato lógico; formato/campos finales no congelados |

No se introduce ninguna identidad universal ni se convierten campos conceptuales en columnas. Los IDs de experimento, fixture, escenario, run, unidad, asignación, evento, instancia y ruta mantienen ámbitos distintos. Tampoco se declara que todos existan ya como columnas o registros poblados.

### 4.1 Ambigüedad específica: instancia CMP por UE

PE §15, en su cross-reference PB, dice que `instance_id/instance_version` son propios de cada UE. Gate 109, en cambio, mantiene abierta la cardinalidad UE→instancia CMP (1:1, 1:N o N:1 según replicación/instanciación).

No se debe resolver esta diferencia leyendo “propia de cada UE” como una cardinalidad física confirmada. La frase de PE expresa el scope de identidad de instancia, pero no aporta roster ni mapping material. Se registra como **AMBIGUITY PE-PB-01**: aclarar si la instancia se crea una por UE, si una instancia puede atender varias UE o si una UE puede contener varias instancias. No modificar DEC-C10-069 ni crear claves para resolverlo.

### 4.2 O-CONF y V_cont

Se mantiene el crosswalk de Gate 109/110:
- O-CONF se adjudica por instancia×ruta; mapping y agregación a UE requieren regla explícita.
- V_cont truth se calcula por UE×K intervalos; K es granularidad temporal, no N.
- No replicar V_cont por instancia ni agregar O-CONF por UE sin contrato explícito.

PE no elimina estas dependencias.

## 5. Truth firewall y frontera de roles

PE define la frontera lógica y el orden de acceso:

| Etapa | Truth disponible | Output/artefacto |
|---|---|---|
| Generator | Sí, truth/potenciales/parametrización reservados | Truth restringida + registros generados |
| Proyector/Sealer | No necesita adjudicar truth; recibe observaciones y reglas de medición | Bundle observado autorizado, sellado y con manifiesto |
| Analyzer | No | Resultado estructurado sellado por estimando |
| Evaluator | Sí, después del sello Analyzer | Comparación con oráculo, errores, abstención y cobertura |

El bundle Analyzer excluye truth, potenciales, parámetros del Generator, reglas secretas, semillas reconstructivas y metadatos que revelen escenario/clase adversarial. La documentación visible debe ser simétrica.

**Estado efectivo:** no probado. PE conserva SR-13 como CONDITIONAL y SR-19/SR-20 como NOT_ASSESSED. No se ha demostrado:
- ACL/permisos efectivos y deny-by-default;
- almacenamiento/custodia segregados;
- ausencia de acceso indirecto a truth por Orquestador/Store/logs;
- pruebas negativas de acceso/exfiltración;
- no filtración por nombres, orden, tamaños, tiempos, errores, hashes o metadatos;
- sellado inmutable y evidencia de auditoría de accesos.

La separación de responsabilidades es un contrato lógico, no un control de seguridad aceptado.

## 6. Serialización, hashes y salida del Analyzer

PE §6 restringe RFC 8785/JCS al envelope U1 de UDG-01 conforme a DEC-C10-074. Para otros registros, eventos, bundles, logs y outputs, el perfil físico de serialización/canonicalización sigue OPEN. No se declara hash reproducible antes de fijar bytes, codificación, normalización, campos, arrays y perfil de versión.

El hash prueba integridad de los bytes según el procedimiento declarado; no prueba verdad, semántica, independencia, causalidad ni autenticidad sin cadena de custodia.

PE §9 requiere output por estimando/dimensión, con población/unidad, régimen, estado de identificación, supuestos, estimación/intervalo cuando proceda, dictamen, cobertura, missingness, censura, soporte, interferencia, vías colaterales, sensibilidad y referencias exactas. Los literales de dictamen siguen conceptuales cuando no estén definidos por contratos vigentes. No se fuerza un resultado de Value aún no instanciado ni se interpreta ITT-D2 como efecto puro de accesibilidad.

## 7. B1/Need: interfaz separada, no extensión tácita de Analyzer

El crosswalk B1/Need confirma dos tareas:
- E1/E2 adjudican Need_preZ a partir de evidencia basal observable, con salidas independientes `need_observed_state ∈ {1,0,?}`.
- Analyzer PE estima/reconstruye constructos y emite resultados por estimando; no es un tercer adjudicador Need.

El bundle PE recibe variables B1/Need observadas solo si el contrato de un estimando lo requiere explícitamente, con semántica/tiempo/provenance/cobertura. No recibe Need_truth, truth_basis_ref, salidas E1/E2 ni su consenso por defecto. Los outputs E1/E2 y PE se evalúan por separado contra sus respectivos oráculos.

El crosswalk de bundle sigue propuesto/no aprobado; no se crea otro ledger ni se duplica el output PE dentro del paquete Need.

## 8. Matriz de hallazgos y disposición

| ID | Hallazgo | Estado | Disposición |
|---|---|---|---|
| G113-01 | Ruta PE y documento recuperados | CLOSED_DOCUMENTARY | Corregir falso negativo de Gate 112; reutilizar PE-TECH-CONTRACT-001 |
| G113-02 | Responsabilidades e interfaces lógicas | RECONCILED_DOCUMENTALLY | No duplicar arquitectura ni crear nuevos roles |
| G113-03 | Roles UE/UA/UO, U_G, instancia, ruta y run | PARTIAL | Reutilizar Gate 109/110; resolver mapping material/cardinalidades |
| G113-04 | CMP instance por UE | AMBIGUOUS | Resolver PE-PB-01 contra roster/contrato material; no asumir 1:1 |
| G113-05 | Artefacto focal B_g1 ↔ RID/TID/SID | OPEN | Gate 101; RID candidato, mapping no confirmado |
| G113-06 | Vector Z, RNG, π, semilla, cluster | OPEN | Gates 101/109/110; no inventar assignment_id/cluster_id |
| G113-07 | Snapshot y evidencia U_G | LOGICALLY_DEFINED / PHYSICAL_UNVERIFIED | Reutilizar DEC-065 y contratos U_G; no declarar FK validada |
| G113-08 | Truth firewall lógico | DEFINED_DOCUMENTALLY | Mantener frontera Generator/Sealer/Analyzer/Evaluator |
| G113-09 | Firewall técnico efectivo | NOT_VERIFIED | G-ROLE bloqueado; SR-13 conditional; SR-19/20 not assessed |
| G113-10 | Serialización | PARTIAL | JCS solo UDG-01/U1; demás perfiles OPEN |
| G113-11 | Analyzer output | LOGICAL_CONTRACT_PARTIAL | No congelar schema ni enums conceptuales |
| G113-12 | B1/Need bundle | PROPOSED_NOT_APPROVED | E1/E2 separados; inclusión condicional por estimando |
| G113-13 | Ejecución e implementación | NOT_AUTHORIZED / NOT_IMPLEMENTED | Mantener sin ejecución; gates PE pendientes |

## 9. Reconciliación de Gate 112

Gate 112 registró `PE_STANDALONE_ARTIFACT_NOT_LOCATED` porque no se había recuperado la ruta exacta. La inspección de los ficheros de PR #116 identifica y recupera el documento PE señalado en §1. La conclusión negativa era un límite de la búsqueda realizada, no ausencia del artefacto.

Esta corrección no altera los demás resultados de Gate 112: asignación, soporte, G_i, ponderación, O-CONF/V_cont y C4 permanecen abiertos según su alcance. Se actualiza el estado de trazabilidad PE, no las decisiones científicas.

## 10. Dictamen y siguientes dependencias

**GATE_113_PE_ARTIFACT_RECOVERED / PE_LOGICAL_ARCHITECTURE_RECONCILED / PHYSICAL_CROSSWALK_PARTIAL / CMP_INSTANCE_CARDINALITY_AMBIGUOUS / RANDOMIZATION_AND_EXPOSURE_OPEN / FIREWALL_NOT_VERIFIED / SERIALIZATION_PARTIAL / IMPLEMENTATION_NOT_READY / NO_SCHEMA_CHANGE / NO_NEW_TEST_IDS / NO_IMPLEMENTATION / NO_EXECUTION / NO_FREEZE.**

Orden de trabajo restante:
1. Resolver PE-PB-01 con el roster y el contrato material PB; aclarar cardinalidad UE↔CMP instance.
2. Completar crosswalk de identidades físicas únicamente desde contratos y registros existentes: UE/UA/cluster/UO/U_G/instance/EID/route/run/fixture/scenario.
3. Reconciliar vector Z/provenance y artefacto focal B_g1↔RID con Gates 99–102, sin crear claves por analogía.
4. Resolver perfiles de serialización y output Analyzer solo cuando el contrato lógico y los gates científicos permitan fijarlos.
5. Mantener G-ROLE bloqueado hasta pruebas de permisos y no filtración; la auditoría documental no puede otorgar PASS técnico.
6. Reanudar G-MAT/G-SCHEMA/G-TEST/G-REPRO/G-AUTH solo después de cerrar las dependencias científicas y materiales previas.

No se ejecutan validadores, código, tests, workflows, simulaciones, estimaciones, calibraciones ni experimentos. No se modifican main, RMA, Evidence→Claim Matrix, STATUS, DEC, C0, U_G ni schemas. PR #116 permanece Draft.  
`scientific_execution=false`; `execution_authorized=false`.


---

## Addendum de corrección — Gate 114: resolución de PE-PB-01 para B1 (2026-11-15)

Gate 113 §4.1/§8 G113-04 registró como ambigua la cardinalidad UE↔CMP instance. La recuperación de `DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001` (aceptada el 2026-11-11) y de PB material reconciliation permite corregir ese estado:

- Para la variante B1, cada UE tiene una instancia lógica de servicio propia, con `instance_id` único en el roster C10-S y `instance_version` monotónica e independiente.
- El contrato y plantilla funcional son comunes; la instancia ejemplar `C10S-SVC-REQUEST-PROCESSOR-001` de DEC-C10-069 no se reutiliza para todas las UE.
- Por tanto, PE-PB-01 pasa a **RESOLVED_DOCUMENTARILY_FOR_B1** y UE→instancia CMP servicio es 1:1 lógico.

La decisión no proporciona roster ni IDs concretos, no demuestra aislamiento material y no resuelve UE→U_G root, UE→UA/cluster, CMP→NODE material ni EID/route. DEC-C10-082 sigue fijando CMP→NODE anchor 1:1 por CMP y snapshot exacto; no iguala instance_id con node_id. El crosswalk completo y los límites están en Gate 114: `C10_S_UE_CMP_UG_EID_ROUTE_MATERIAL_CROSSWALK_GATE_114_DRAFT_001.md`.

Estado actualizado: **B1_INSTANCE_CARDINALITY_RESOLVED_LOGICALLY / MATERIAL_MAPPING_OPEN / FIREWALL_NOT_VERIFIED / NO_SCHEMA_CHANGE / NO_EXECUTION**. No se altera PE ni las decisiones aceptadas.
