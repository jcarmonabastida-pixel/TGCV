# C10-S — Gate 122: expediente mínimo de materialización probatoria del aislamiento

**ID:** C10-S-ISOLATION-MATERIALIZATION-DOCKET-122  
**Fecha:** 2026-11-15  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** HISTORICAL_RECONSTRUCTION_COMPLETED / EVIDENCE_SOURCE_CROSSWALK_SPECIFIED / SOURCE_AVAILABILITY_UNVERIFIED / MATERIAL_CAPTURE_NOT_AUTHORIZED / MATERIAL_INVENTORY_NONE / ISOLATION_NOT_DEMONSTRATED / NOT_DESIGN_FROZEN / NO_IMPLEMENTATION / NO_EXECUTION  
**Precedencia:** DEC-C10-103; Gate 121; U_G Inventory Register Template; U_G Evidence Provenance and Adjudication Protocol; IAM Service Boundary Overlay; C1 pre-Z IAM Crosswalk; Adapter Provision Manifest and Dependency Graph; PE Integrated Technical Specification; UNIT-01…14; PROV-01…12; B-M01…15.

## 1. Propósito y dictamen

Gate 122 convierte IS-1…IS-8 de Gate 121 en un expediente mínimo de fuentes, afirmaciones, alcance, evidencia y adjudicación para el futuro microdominio B1/D2.

**Dictamen:** los artefactos históricos permiten especificar un crosswalk de fuentes y un protocolo de adquisición, pero no permiten afirmar que las fuentes técnicas estén disponibles, que exista un sistema B1/D2 materializado o que el inventario haya sido poblado. No se ha accedido a entornos, repositorios técnicos del sistema experimental, IAM real, runtime, proveedores, logs ni snapshots. No se han creado credenciales, consultas, registros ni artefactos técnicos.

Se mantienen:
- `SOURCE_AVAILABILITY_UNVERIFIED`
- `MATERIAL_INVENTORY_NONE`
- `ISOLATION_NOT_DEMONSTRATED`
- `UE_ASSIGNMENT_CONDITIONAL`
- `NO_NEW_TEST_IDS`
- `NO_SCHEMA_CHANGE`
- `NO_MATERIAL_CAPTURE_AUTHORIZED`
- `NOT_DESIGN_FROZEN / NO_IMPLEMENTATION / NO_EXECUTION`

El expediente es una especificación de qué se necesitaría y cómo juzgarlo, no una solicitud de acceso ni una autorización implícita para recopilar datos.

## 2. Reconstrucción histórica y reutilización obligatoria

| Fuente histórica | Reutilización en Gate 122 | No se debe inferir |
|---|---|---|
| Gate 121, IS-1…IS-8 | Criterios de suficiencia acumulativos | Que exista evidencia material |
| Adapter Provision Manifest, B-M01…15 | Catálogo de superficies de B, impactos y evidencia esperada | Que las superficies estén inventariadas |
| U_G Inventory Register Template | NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT y registros normalizados de evidencia/cobertura/evaluación/adjudicación | Que la plantilla vacía sea inventario |
| U_G Evidence Provenance and Adjudication Protocol, S1…S8 | Clases de fuente, procedencia, triangulación, cegamiento, E1/E2 y adjudicación | Que las fuentes tengan disponibilidad o calidad suficiente |
| IAM Service Boundary Overlay + C1 pre-Z IAM Crosswalk | Clasificación P0/P1/P2, C_SRC y requisitos basales | Que exista IAM material o snapshots C_SRC sellados |
| PE Integrated Technical Specification | Roles Generator, Sealer, Analyzer, Evaluator y Artifact Store | Que el firewall lógico esté implementado técnicamente |
| UNIT-01…14 | Identidad, independencia, spillover, clusters, exposición, soporte, abstención, asignación y N efectivo | Que las pruebas estén ejecutadas |
| PROV-01…12 | Invariancia, recursos, permisos, alternativas, dependencias y rollback | Que las garantías estén demostradas |

No se crea inventario, registro, esquema, test ID, tipo de evidencia ni sistema paralelo. Los artefactos U_G existentes siguen siendo el destino normativo de cualquier futura captura autorizada.

## 3. Regla de mapeo fuente → afirmación

La fuente se elige por el claim que debe sostener, no por su nombre ni por disponibilidad conveniente. Se aplican las clases S1…S8 del protocolo:

- **S1 declarativa:** identidad/versiones declaradas, SBOM, lockfiles, manifiestos y digests.
- **S2 configuración/control:** configuración efectiva, IAM/ACL, cuotas, red, políticas y despliegue.
- **S3 runtime:** procesos, módulos cargados, llamadas, sockets, trazas, logs y métricas.
- **S4 snapshots/integridad:** snapshots inmutables, hashes y diffs pre/post/rollback.
- **S5 contrato/interfaz:** API, schemas, interfaces y documentación contractual.
- **S6 funcional independiente:** conformidad y oráculo cegado bajo pruebas autorizadas.
- **S7 documentación/entrevista:** manuales, tickets, diagramas y custodios; fuente de descubrimiento, no prueba primaria universal.
- **S8 inferencia analítica:** análisis estático, cierre transitivo, resolución de imports y correlación de trazas, con método y límites explícitos.

Una fuente puede ser primaria para una dimensión y secundaria para otra. S1 no acredita carga/uso runtime; S2 no acredita por sí sola el permiso efectivo ni la configuración observada; S3 no acredita ausencia si la ventana o el muestreo son incompletos; S5 no acredita comportamiento; S7 no cierra el universo; S8 conserva supuestos y error. Para claims críticos se exige triangulación de métodos/fuentes independientes cuando sea factible.

## 4. Crosswalk mínimo por condición IS

| Condición | Afirmación exacta a resolver | Fuentes esperadas (S1…S8) | Artefactos U_G destino | Cobertura que debe fijarse | Estado actual |
|---|---|---|---|---|---|
| IS-1 Frontera | Universo de UE, servicios, hosts, runtimes, dependencias, externos, pools, canales, versiones y ventanas está delimitado | S1/S2/S5/S7 para declaración; S3/S8 para descubrimiento y contraste; S4 para fijar versión/tiempo | NODE, EDGE, ROUTE, PREDICATE, SNAPSHOT, COVERAGE_REGISTER | Universo/denominador; superficies incluidas/excluidas/opacas; entornos; rutas; horizonte y límites de observabilidad | NO MATERIALIZADO |
| IS-2 Inventario | Cada objeto y relación pertinente tiene identidad, versión, consumidores y procedencia | S1/S2/S3/S4/S8 | NODE, EDGE, ROUTE, ROUTE_STEP, SNAPSHOT, EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK | UE/instance_id; CMP/PAR/REF/RUL; dependencias directas/transitivas; consumidores; externos | PLANTILLA VACÍA |
| IS-3 Transmisión | Uso/tratamiento de UE_i no altera información, estado, disponibilidad o resultado de UE_j, dentro del claim/ventana | S2/S3/S4/S5/S6/S8; S7 solo descubrimiento | EDGE, ROUTE, PREDICATE, SNAPSHOT, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER | Pares UE o mapa exhaustivo de exposición; vías, eventos, ventanas, fallos raros y límites de captura | NO OBSERVADO |
| IS-4 Recursos | Recursos compartidos no generan contención, prioridad, desplazamiento ni degradación cruzada | S2/S3/S4/S8 y S6 si requiere conformidad funcional | NODE/EDGE/PREDICATE/SNAPSHOT + registros de evidencia/cobertura | Pool, capacidad, cuota efectiva, demanda, consumo, cola, prioridad, ventana y consumidores | NO OBSERVADO |
| IS-5 Permisos/datos | No hay acceso cruzado efectivo a estado mutable, secretos, colas, stores, credenciales, endpoints o información | S2/S3/S4/S5/S8 | NODE/EDGE/PREDICATE/SNAPSHOT + IAM/C_SRC overlay y CLAIM_EVIDENCE_LINK | Principal×acción×objeto×UE×ventana; herencia, expiración, lectura/escritura y namespace | IAM MATERIAL NONE |
| IS-6 Alternativas/medición | A1/A2/F2, F*, dataset, oráculo y medición permanecen invariantes/no afectados por B dentro del alcance | S1/S2/S3/S4/S5/S6/S8 | ROUTE/PREDICATE/SNAPSHOT/EVIDENCE_REGISTER/CLAIM_EVIDENCE_LINK | Versiones, hashes, inputs/outputs, dependencias, accesos por rol, diffs y pruebas funcionales | SOLO CONTRATOS |
| IS-7 Tiempo/rollback | No queda carryover relevante, o está modelado y acotado | S3/S4/S6/S8 y S2 para configuración/rollback | SNAPSHOT/NODE/EDGE/PREDICATE/COVERAGE_REGISTER | Pre-B, post-B, rollback, colas/cachés/residuos, expiración y periodo de arrastre | NO OBSERVADO |
| IS-8 Adjudicación | Truth permanece restringida; Analyzer recibe solo observaciones selladas; Evaluator compara después de congelar salida | S2/S3/S4/S5/S8 + auditoría de permisos y logs de acceso | EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, EVALUATOR_ASSESSMENT, ADJUDICATION_REGISTER, COVERAGE_REGISTER | Roles, identidades, ACL efectivas, accesos/logs, sellado/hash, orden temporal y ruptura de cegamiento | FIREWALL LÓGICO; TÉCNICO NO VERIFICADO |

Esta tabla es un crosswalk de requisitos, no una lista de fuentes ya localizadas. Las fuentes concretas, ubicaciones, custodios, consultas y permisos se mantienen **TBD / UNVERIFIED** hasta que el sistema B1/D2 y sus responsables sean identificados y exista autorización de acceso.

## 5. Expediente de evidencia por claim

Cada futuro claim crítico deberá poder reconstruirse usando los registros U_G ya definidos:

`claim_target → CLAIM_EVIDENCE_LINK → EVIDENCE_REGISTER`

Y, cuando aplique:

`claim_target → COVERAGE_REGISTER → EVALUATOR_ASSESSMENT(E1,E2) → ADJUDICATION_REGISTER`

Se conservan los campos y reglas ya aprobados en la plantilla/protocolo; no se crea un formato nuevo. Como mínimo, cada vínculo debe resolver:

1. Afirmación exacta y objeto tipado al que se refiere.
2. Fuente S1…S8, tipo concreto, origen y autoridad/custodio.
3. Método de obtención, versión de herramienta/consulta y lineage.
4. Unidad, frontera, entorno, versión, rutas y ventana temporal.
5. Hash/digest/firma y resultado de integridad.
6. Denominador de cobertura, examinados, válidos, excluidos y opacos.
7. Limitaciones, muestreo, retención, no observables y errores.
8. Confidencialidad, ubicación segura y permisos de acceso.
9. Evaluación independiente y adjudicación cuando corresponda.

No almacenar en GitHub secretos, tokens, credenciales, datos personales innecesarios ni volcados sensibles. Conservar referencias seguras, hashes y metadatos suficientes para reproducibilidad autorizada.

## 6. Cobertura y regla para declarar 1, 0 o ?

Se mantienen ortogonales:
- `observed_state ∈ {1,0,?,NA}`
- `evidence_status ∈ {AVAILABLE,MISSING,CONFLICTING}`
- `coverage_status ∈ {NONE,PARTIAL,COMPLETE}`
- `review_adjudication_status` según el dominio U_G vigente.

Reglas:
- Una fuente encontrada puede apoyar 1 solo para el claim, unidad, versión y ventana que efectivamente cubre.
- 0 exige enumeración completa de superficies plausibles, control de alias/renombres/carga dinámica y sensibilidad suficiente del método de detección.
- NONE/MISSING, cobertura parcial, fuentes opacas, versiones incompatibles o integridad fallida producen ?; nunca 0.
- COMPLETE exige denominador, universo versionado, fuentes esperadas/examinadas/válidas, exclusiones/opacos y regla de cierre explícitos.
- La ausencia de evento en logs no demuestra ausencia si la captura es muestreada, incompleta o no cubre la ruta/ventana.
- Evidencia conflictiva mantiene ? hasta adjudicación; no se resuelve por mayoría automática.
- No extrapolar evidencia de una versión, instancia, entorno o ventana a otra sin regla de continuidad justificada.

## 7. Responsabilidades y separación de roles

| Rol lógico | Responsabilidad en este expediente | Restricción |
|---|---|---|
| Custodio técnico de cada fuente | Identificar sistema, autoridad, versión, retención, acceso y límites | No adjudica por sí solo ausencia universal |
| Evidence collector | Recuperación/captura autorizada, provenance, integridad y scope | No cambia truth ni evalúa causalidad |
| E1 | Primera evaluación independiente de claim y cobertura | Sin acceso a truth oculta ni Outcome/Value si no es necesario |
| E2 | Segunda evaluación independiente | No copia ni negocia la evaluación de E1 |
| Adjudicador | Resuelve discrepancias y conserva posición minoritaria | No fuerza PASS cuando la evidencia no discrimina |
| Generator | Mantiene truth DGP restringida | No suministra truth al Analyzer |
| Sealer | Filtra y sella el bundle observado | No altera truth ni adjudica causalidad |
| Analyzer | Consume observaciones permitidas | No accede a truth, potenciales ni parámetros secretos |
| Evaluator | Compara salida sellada con truth tras el sellado | No modifica retroactivamente la salida del Analyzer |

E1/E2/adjudicador son funciones de independencia del protocolo, no afirmaciones de que haya personas adicionales disponibles. No se simula revisión externa ni se declara independencia humana cuando no existe. Si no puede asegurarse separación efectiva de roles, el claim correspondiente queda OPEN/INDETERMINATE. El diseño no exige que el usuario obtenga revisión externa para continuar con análisis documental, pero tampoco permite presentarla como realizada.

## 8. Orden mínimo de adquisición futuro (sin ejecutarlo)

Una vez exista autorización y un sistema concreto, la adquisición deberá seguir este orden para no perder comparabilidad ni contaminar roles:

1. **Fijar alcance pre-Z:** roster/UE y binding B1↔instance; sistema, entornos, versiones, ventana y fuentes esperadas. No asignar Z ni consultar Outcome/Value.
2. **Baseline C_SRC/IAM:** capturar estado declarado basal, permisos efectivos relevantes, versiones, dependencias y snapshots inmutables antes de B/Z, conforme al contrato temporal y C1 pre-Z.
3. **Identidad y dependencias:** resolver artefactos, runtime, host, servicios, imports/dependencias transitivas, endpoints, externos y consumidores.
4. **Recursos y datos:** identificar pools, cuotas, consumo, colas, estado mutable, stores, cachés, credenciales y canales.
5. **Post-B y rollback:** solo dentro de una operación técnica autorizada y del protocolo de intervención; snapshots comparables y evidencia temporal, sin ejecutar B como parte de este gate.
6. **Sellado y adjudicación:** preparar bundle observed, controles de acceso, E1/E2, discrepancias y adjudicación; truth continúa segregada.
7. **Cierre de cobertura:** solo entonces evaluar IS-1…IS-8 y resolver individual / cluster / G_i / bounds-abstención antes de resultados confirmatorios.

Este orden es una secuencia futura de captura, no autorización para llevarla a cabo.

## 9. Precondiciones para pasar de expediente a captura material

Antes de cualquier captura técnica deben existir y verificarse:
- Sistema/entorno B1/D2 concreto e identidad del propietario/custodio.
- Roster causal B y población P*_{τ2} aprobados/materializados según sus contratos.
- Alcance de captura, fuentes, ventanas y retención definidos.
- Autorización explícita del propietario y del responsable científico para cada fuente/operación.
- Clasificación de datos, seguridad, privacidad y ubicación de almacenamiento aprobadas.
- Método de captura, integridad, herramientas/versiones y límites de observabilidad definidos.
- Compatibilidad del destino con U_G y los contratos IAM/C_SRC/snapshot; ningún cambio de esquema sin decisión.
- Separación de permisos/roles y plan de cegamiento, sin exponer truth al Analyzer.
- Plan de rollback y límites de impacto cuando la operación pueda modificar el sistema.
- Decisión explícita sobre si la operación es solo lectura o intervención; no confundir inspección con instalación/ejecución.

Si falta cualquiera de estas precondiciones, se mantiene el estado OPEN y no se captura.

## 10. Matriz de disponibilidad al cierre de Gate 122

| Recurso/fuente | Disponibilidad en este gate | Evidencia observada |
|---|---|---|
| GitHub: contratos y plantillas TGCV | AVAILABLE, documental | Versiones/commits recuperados; no son evidencia material del runtime |
| Sistema B1/D2 y entorno de ejecución | UNVERIFIED / NOT IDENTIFIED | Ninguna |
| Roster B / P*_{τ2} | NOT MATERIALIZED | Ninguna |
| SBOM/lockfiles/manifiestos reales | UNAVAILABLE TO THIS AUDIT | Ninguna |
| Configuración efectiva/IAM/ACL/red/cuotas | UNAVAILABLE TO THIS AUDIT | Ninguna |
| Runtime/trazas/logs/métricas | UNAVAILABLE TO THIS AUDIT | Ninguna |
| Snapshots pre-B/post-B/rollback | NONE | Ninguna |
| Servicios externos y contratos de proveedor concretos | NOT IDENTIFIED | Ninguna |
| Pruebas funcionales/oráculo cegado | CONTRACTS ONLY; NOT EXECUTED | Ninguna |
| Custodios técnicos y permisos de captura | NOT IDENTIFIED | Ninguna |
| E1/E2/adjudicación material | NOT PERFORMED | Ninguna |

“UNAVAILABLE TO THIS AUDIT” no significa que la fuente no exista; significa que no ha sido identificada, conectada ni consultada en este gate.

## 11. Decisión y consecuencia para C10-S

Gate 122 deja listo el expediente de qué debe localizarse y cómo se evaluará, pero no permite afirmar que el aislamiento esté más demostrado que al cierre de Gate 121.

- IS-1…IS-8: OPEN / NOT EVIDENCED.
- Material inventory: NONE.
- Source availability: UNVERIFIED.
- UE=UA individual assignment: CONDITIONAL.
- Cluster/G_i: NOT SELECTED; no evidencia para escogerlos.
- θ_A: no identificado por este expediente.
- ITT-D2: sigue siendo el efecto total del paquete, sin atribución automática a ΔT_acc*.
- C4: sigue secundario y condicionado a su contrato longitudinal.

No se debe abrir un gate de captura técnica hasta que se identifique un sistema material y exista autorización explícita. El siguiente trabajo admisible es resolver el bloqueo de identidad del sistema/roster y de custodios/fuentes mediante documentación existente; si esos datos no existen todavía, registrar el prerequisito como no satisfecho en vez de inventar ubicaciones o responsables.

## 12. Gobernanza

- No se modifica DEC-C10-103, DEC-C10-095/096 ni otras decisiones aceptadas.
- No se modifica C0, U_G, RMA, Evidence→Claim Matrix, STATUS ni `main`.
- No se crean registros físicos, filas IAM, NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT, evidence IDs, test IDs, schemas o columnas.
- No se consulta ningún entorno técnico, cuenta externa, servicio, runtime, red, IAM, logs o datos de sistema.
- No se ejecutan validadores, tests, workflows, simulaciones, estimaciones, calibraciones o experimentos.
- PR #116 permanece Draft.
- `scientific_execution=false`; `execution_authorized=false`.

**Resultado:** `GATE_122_EVIDENCE_SOURCE_CROSSWALK_SPECIFIED / SOURCE_AVAILABILITY_UNVERIFIED / MATERIAL_INVENTORY_NONE / ISOLATION_NOT_DEMONSTRATED / UE_ASSIGNMENT_CONDITIONAL / NO_MATERIAL_CAPTURE / NO_SCHEMA_CHANGE / NO_FREEZE / NO_IMPLEMENTATION / NO_EXECUTION`.
