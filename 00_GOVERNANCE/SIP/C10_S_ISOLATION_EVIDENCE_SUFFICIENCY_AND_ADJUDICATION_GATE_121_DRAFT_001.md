# C10-S — Gate 121: suficiencia de evidencia material y adjudicación del aislamiento entre UE

**ID:** C10-S-ISOLATION-EVIDENCE-121  
**Fecha:** 2026-11-15  
**Rama:** `research/c10-s-consolidation-draft` · PR #116 (Draft)  
**Estado:** HISTORICAL_REUSE_COMPLETED / ISOLATION_EVIDENCE_PROTOCOL_SPECIFIED / MATERIAL_INVENTORY_NONE / ISOLATION_NOT_DEMONSTRATED / NO_NEW_TEST_IDS / NO_SCHEMA_CHANGE / NOT_DESIGN_FROZEN / NO_IMPLEMENTATION / NO_EXECUTION  
**Precedencia:** DEC-C10-103; DEC-C10-066/067/068/069; DEC-C10-057…065/076/078/079…089; DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001; Gates 102, 109, 110, 111, 112, 113, 114, 116, 117, 119, 120; PB Material D2 Instance and Isolation Reconciliation; Adapter Provision Manifest and Dependency Graph; U_G Inventory Register Template; IAM overlays; PE Integrated Technical Specification; UNIT-01…14; PROV-01…12; B-M01…15; Path Predicate Temporal Evidence Matrix.

## 1. Propósito y dictamen

Gate 121 convierte los contratos de aislamiento e interferencia ya existentes en un **protocolo de suficiencia de evidencia material y adjudicación**, sin recrear inventarios, pruebas o esquemas.

**Dictamen:** los artefactos recuperados son suficientes para especificar qué debe inspeccionarse y cómo adjudicarlo; no contienen observaciones materiales suficientes para demostrar aislamiento entre UE. Se mantiene:

- `MATERIAL_INVENTORY_NONE`
- `ISOLATION_NOT_DEMONSTRATED`
- `INDIVIDUAL_ASSIGNMENT_CONDITIONAL`
- `NO_NEW_TEST_IDS`
- `NO_SCHEMA_CHANGE`
- `NOT_DESIGN_FROZEN`
- `NO_IMPLEMENTATION / NO_EXECUTION`

La recomendación aceptada por DEC-C10-103 —asignación individual por UE— sigue siendo la arquitectura confirmatoria preferida **solo si** el aislamiento material se demuestra dentro de una frontera, versión y ventana expresamente auditadas. Gate 121 no convierte esa recomendación en evidencia ni selecciona por anticipado una alternativa.

## 2. Reconstrucción histórica: qué ya existe y qué no se debe duplicar

| Artefacto histórico | Contenido reutilizable | Estado / límite |
|---|---|---|
| Gate 102 + D2 material inventory reconciliation | B-M01…15; grafo de dependencias/consumidores; U_G NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT; estados 1/0/? | Contrato de inventario recuperado; inventario material vacío; grafo transitivo no observado |
| Adapter Provision Manifest | Superficies de artefacto, runtime, host, interfaz, permisos, datos, recursos, red, seguridad, observabilidad, estado, rendimiento, oráculo, alternativas y rollback | B-M01…15; la mayoría NO INVENTARIADO; M13/M14 prohibidos como superficies modificadas por B según manifiesto |
| PROV-01…12 | No ejecución de transformaciones; invariancia de F*/dataset/oráculo; snapshots; dependencias; recursos; permisos; estado; alternativas; dependencias críticas; rollback; desconocidos; separación C_dep/A_f | Contratos documentales, no implementados ni ejecutados |
| U_G Inventory Register Template + IAM overlays | Registros tipados y versionados; NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT; cobertura; provenance; boundary_class P0/P1/DUAL/P2 | Plantilla vacía; captura C_SRC/IAM/snapshots NONE |
| DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001 | Una instancia lógica única por UE; instance_version independiente; plantilla funcional común | Identidad lógica aceptada; no demuestra independencia de recursos, estado, permisos, agentes, canales ni runtime |
| Gate 109 / 110 | UE, UA, cluster y UO separados; arquitecturas A–D; G_i(Z_-i); condiciones de identificación | Mapping material y exposición no especificados |
| Gate 111 + Test Contract Register §17 | UNIT-01…14 cubren independencia, correlación basal, spillover, cluster, exposición, positividad, abstención, asignación, tamaño efectivo y no-cluster retrospectivo | Contratos propuestos; no implementados ni ejecutados; no crear familia paralela |
| PE §15 y Gate 113 | Firewall lógico Generator/Sealer/Analyzer/Evaluator y responsabilidades | Separación lógica descrita; firewall técnico/ACL/custodia no probado |
| Gate 120 / DEC-C10-103 | Aislamiento como condición de entrada de asignación individual; cluster/mapa solo con contrato propio; interferencia no mapeada → bounds/abstención | Decisión aceptada; evidencia material sigue OPEN |

**Regla de no duplicación:** Gate 121 no crea otro inventario, IAM, manifiesto, grafo, contrato PE, familia UNIT ni ID PROV. Reutiliza los artefactos anteriores y define un criterio transversal de suficiencia y decisión.

## 3. Unidad correcta de adjudicación

La adjudicación de aislamiento se realiza sobre una relación potencial de transmisión entre unidades experimentales distintas, no sobre la mera igualdad o diferencia de nombres de instancias.

- UE: unidad de potenciales/resultados y población causal.
- UA: unidad realmente asignada; solo coincide con UE si el aislamiento y el contrato de asignación lo justifican.
- UO: unidad de observación/medición; no aumenta N de UE.
- instance_id: identidad lógica del servicio por UE; no sustituye UE ni UA.
- NODE/EDGE/ROUTE: objetos y relaciones del universo material; no son unidades experimentales.
- Cluster: unidad de asignación/inferencia solo si se define ex ante a partir de una arquitectura de dependencia/exposición defendible.

La unicidad de instance_id por UE no basta. Dos instancias distintas pueden compartir host, pool, dependencia, cola, endpoint, agente, canal, almacenamiento, credenciales o servicio externo. A la inversa, una plantilla contractual o artefacto inmutable compartido no implica por sí mismo interferencia.

## 4. Principio de evidencia: distinguir compartición, transmisión y consecuencia causal

Para cada objeto/recurso y cada relación entre UE deben adjudicarse tres preguntas separadas:

1. **Compartición:** ¿las unidades usan el mismo objeto, servicio, recurso, estado o canal?
2. **Transmisión:** ¿el uso, asignación, tratamiento o cambio de una UE puede alterar la disponibilidad, estado, información, comportamiento, resultado o medición de otra?
3. **Consecuencia causal:** ¿esa transmisión afecta el potencial relevante bajo Z, la exposición, ΔT_acc*, Reach, trayectoria, Outcome o V_cont?

La compartición no equivale automáticamente a interferencia. Sin embargo, si la evidencia de transmisión no está cubierta, no puede inferirse ausencia de interferencia. Una dependencia compartida solo es compatible con aislamiento si su inmutabilidad/read-only y la ausencia de contención, mutación, comunicación, side effects y carryover están respaldadas dentro del alcance auditado.

La existencia de una arista entre dos objetos tampoco prueba por sí sola spillover; y la ausencia de una arista registrada no prueba que no exista, si la cobertura es incompleta.

## 5. Dominios de aislamiento y evidencia mínima por vía

Se reutilizan B-M01…15 y PROV-01…12. La siguiente matriz especifica qué evidencia se necesita para declarar una vía cubierta; no afirma que exista.

| Dominio de vía | Cobertura histórica | Evidencia material mínima para adjudicar transmisión entre UE | Contratos existentes |
|---|---|---|---|
| Artefactos, librerías y dependencias | B-M01…03, B-M09; grafo transitivo | Identidad/version/hash/firma; SBOM o inventario equivalente; dependencias directas y transitivas; consumidores por instancia; estado mutable/read-only; snapshots/diffs | PROV-03/04/09; UNIT-02; BND-01/12 |
| Runtime, host y servicios | B-M02/03/09 | Host/runtime/namespace por UE; procesos/servicios compartidos; configuración y cambios pre/post; límites efectivos de aislamiento; consumidores | PROV-03/09; UNIT-02 |
| Recursos y capacidad | B-M07/12 | Pool y capacidad; reservas/cuotas/compromisos; demanda y consumo por UE/ventana; contención, colas, prioridad y desplazamiento a otras UE | PROV-05; UNIT-03/04; SYS-04/09 |
| Red, endpoints y canales | B-M04/08 | Topología, rutas, DNS/proxy/firewall, endpoints, ACL; productores/consumidores; tráfico/interacciones cruzadas y ventanas | PROV-03/06; UNIT-02/05/07 |
| Permisos, identidad y secretos | B-M05; IAM P1/P2 | Matriz efectiva de principal→acción→objeto→unidad→ventana; alcance, herencia, expiración; separación entre autorización funcional basal y permiso técnico | PROV-06; CLS-02; UNIT-02 |
| Estado y datos persistentes | B-M06/11 | Stores, cachés, índices, colas, archivos, bases y estado de sesión; owner, claves/namespace, lectura/escritura, snapshots y diffs | PROV-03/07/10; UNIT-02/04 |
| Agentes e información | B-M10; PE roles | Identidad/aislamiento de agentes; mensajes, prompts/instrucciones, telemetría visible, notificaciones, conocimiento transferido y acceso cruzado | UNIT-02/05/07; ACC-17; PE firewall |
| Medición, oráculo y adjudicación | B-M10/13; PE | Inmutabilidad de oráculo/dataset; acceso por rol; cegamiento; logs de lectura; ausencia de feedback desde Outcome/Value hacia Generator/Analyzer antes del sellado | PROV-02; ACC-17/18; PE; MEAS |
| Alternativas y rutas funcionales | B-M14; ROUTE/PREDICATE | Inventario y consumidores; estado, recursos, permisos, disponibilidad y conformidad F* pre/post; no degradación o activación diferencial | PROV-05/08; S4R-05/06/13; UNIT-04 |
| Tiempo, rollback y carryover | B-M15; SNAPSHOT | Orden temporal, ventanas, expiración, colas pendientes, residuos, cachés, estado persistente, rollback y periodo de arrastre | PROV-03/10; UNIT-02/04; TEMP |
| Dependencias externas | B-M02/04/08/09/12 y R_external | Proveedor/servicio/version/SLA/consumidores; límites de observabilidad; estado compartido, rate limits, contención y cambios fuera de control | BND-01/12; UNIT-08; PROV-11 |

Un dominio solo puede declararse cubierto si se conoce su universo relevante, se han fijado sus límites, existe evidencia ligada a la UE/instancia/versión/ventana correspondiente y la cobertura es suficiente para descartar vías plausibles. Un listado de paquetes, un diagrama conceptual o un hash común no bastan.

## 6. Representación y estados: no inventar semántica ni campos físicos

Se reutilizan los registros existentes:
- NODE para objetos/servicios/instancias según el contrato aplicable;
- EDGE para dependencias, uso, lectura/escritura, comunicación, autenticación, consumo o relación compartida;
- ROUTE/ROUTE_STEP para rutas focales, alternativas, compartidas, externas y desconocidas;
- PREDICATE para condiciones de aislamiento/transmisión y predicados temporales;
- SNAPSHOT para fijar exactamente la revisión y ventana;
- EVIDENCE_REGISTER, COVERAGE_REGISTER, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER para procedencia, alcance y adjudicación.

No se añade schema físico ni se crean columnas nuevas. El crosswalk analítico exige que cada afirmación de aislamiento pueda resolverse a registros existentes y a su evidencia. Si el contrato U_G no permite representar una relación necesaria, debe registrarse el gap y solicitar una decisión antes de cambiarlo.

Se preservan por separado:
- **Estado observado del objeto/arista/predicado:** 1 / 0 / ?.
- **Cobertura:** NONE / PARTIAL / COMPLETE.
- **Disponibilidad de evidencia:** AVAILABLE / MISSING / CONFLICTING.
- **Revisión/adjudicación:** NOT_REVIEWED hasta que exista evaluación con fuente y alcance.

Reglas obligatorias:
1. NONE o MISSING → ?; nunca 0.
2. Arista no encontrada con cobertura parcial → ?.
3. 0 solo si la búsqueda cubre exhaustivamente el universo, frontera, unidad, versión y ventana relevantes.
4. Compartición=1 no implica automáticamente transmisión=1; transmisión=? tampoco permite aislamiento PASS.
5. Evidencia contradictoria → CONFLICTING y adjudicación pendiente; no promediar ni escoger la fuente favorable.
6. La ausencia de cambios en una captura aislada no descarta contención, transmisión informativa ni carryover fuera de su ventana.

## 7. Criterio de suficiencia para declarar aislamiento individual

La arquitectura de asignación individual UE=UA solo puede pasar a `ISOLATION_DEMONSTRATED_WITHIN_SCOPE` si se satisfacen conjuntamente:

**IS-1 — Frontera cerrada:** sistema, servicios, entornos externos, dependencias, pools, unidades, versiones y ventanas están delimitados; cobertura COMPLETE para el universo relevante.

**IS-2 — Inventario trazable:** roster aprobado y binding UE↔B1↔instance_id; inventario NODE/EDGE/ROUTE/PREDICATE/SNAPSHOT completo y con provenance; dependencias transitivas y consumidores identificados.

**IS-3 — Sin transmisión cruzada relevante:** para toda vía plausible entre UE distintas, la transmisión causal está respaldada como 0 o se demuestra un aislamiento técnico/funcional equivalente. Los objetos read-only compartidos deben demostrar ausencia de mutación, contención y flujo informativo/side effect.

**IS-4 — Recursos no rivales o segregados:** reservas/cuotas/capacidad por unidad y ventanas muestran que el tratamiento/uso de una UE no reduce la disponibilidad ni altera el resultado de otra UE. La mera declaración de cuota no basta sin evidencia de aplicación/consumo y consumidores.

**IS-5 — Permisos y datos segregados:** no existe acceso cruzado efectivo a estado mutable, secretos, colas, archivos, bases, credenciales, endpoint o información relevante; se requieren pruebas negativas/evidencia efectiva, no solo configuración declarada.

**IS-6 — Alternativas y medición preservadas:** A1/A2/F2, F*, dataset, oráculo, medición y adjudicación permanecen independientes e invariantes en el alcance definido; PROV-02/05/08/09 se resuelven con evidencia, no por contrato nominal.

**IS-7 — Temporalidad y reversibilidad:** snapshots pre-B/post-B/post-rollback son comparables y cubren ventanas; residuos y carryover están descartados o incorporados explícitamente al modelo.

**IS-8 — Adjudicación independiente:** la evaluación de cobertura y evidencia se realiza sin que Generator o Analyzer accedan a la truth oculta; se conserva provenance y se aplica el firewall PE con controles efectivos.

**Regla de decisión:** un solo IS-* relevante OPEN, ?, PARTIAL, MISSING o CONFLICTING impide declarar aislamiento demostrado para la población/alcance afectados. La conclusión será `ISOLATION_NOT_DEMONSTRATED`, con delimitación de lo que sí está cubierto. Esto no demuestra que haya interferencia; demuestra que no se ha descartado.

No se fija aquí un umbral cuantitativo universal de “interferencia despreciable”. Cualquier tolerancia material, temporal o funcional deberá justificarse ex ante, antes de observar resultados y sin escogerla para favorecer el estimando.

## 8. Rutas de decisión si falla el aislamiento

| Evidencia | Arquitectura admisible | Consecuencia |
|---|---|---|
| Aislamiento individual demostrado dentro de alcance | UE=UA, asignación individual | ITT UE-promedio y θ_A solo tras cerrar además población, intervención, soporte, medición e identificación |
| Dependencia compartida con interferencia contenible por grupos pre-Z | Asignación por cluster, solo con cluster definido antes de Z | Reabrir UA, estimando, ponderación UE/cluster, número efectivo de clusters, correlación y potencia; UNIT-03/06/12/13/14 |
| Interferencia individual mapeable con soporte | Asignación individual + mapa versionado G_i(Z_-i) | Especificar exposición, probabilidades y soporte conjunto; efectos directos/indirectos/totales según estimando propio; UNIT-04/05/07/09 |
| Interferencia presente o plausible, pero no mapeable o sin soporte | Abstención o bounds | No informar ITT individual convencional ni θ_A identificado; UNIT-08/10 y contratos de adjudicación |
| Evidencia material insuficiente para saber si existe transmisión | No declarar aislamiento; mantener CONDITIONAL/INDETERMINATE | No cambiar a cluster por intuición ni asumir SUTVA; obtener evidencia faltante antes de elegir régimen |

No se forman clusters retrospectivamente a partir de Outcome/Value, ni se elige entre arquitecturas después de observar el resultado. El mapa de exposición no se inventa a partir de etiquetas de dependencia: debe corresponder a la red material, tratamiento y ventanas reales.

## 9. Vínculo exacto con UNIT y PROV existentes

No se crean IDs. Se reutilizan como sigue:

- UNIT-01: censo e identidad de UE/UA/UO; repetición no incrementa N.
- UNIT-02: independencia primaria; evidencia de ausencia de recursos/agentes/información/infraestructura/canales compartidos relevantes.
- UNIT-03: separar correlación basal de spillover inducido por Z.
- UNIT-04: spillover de recursos y rechazo de ITT individual simple.
- UNIT-05: spillover informacional y necesidad de exposición.
- UNIT-06: asignación por cluster.
- UNIT-07: mapa G_i y efectos directos/indirectos/totales.
- UNIT-08: exposición desconocida → INDETERMINATE/NO IDENTIFIED.
- UNIT-09: positividad de unidad y exposición.
- UNIT-10: no presentar Wald/LATE individual bajo interferencia incompatible.
- UNIT-11: RNG, algoritmo, estrato, probabilidades y desviaciones.
- UNIT-12: N de UE, UA/clusters y medidas repetidas.
- UNIT-13: prohibición de cluster retrospectivo.
- UNIT-14: cambio de UE/UA obliga a recalcular población, estimando, q_X*, soporte, N y protocolo.

PROV-01…12 siguen siendo contratos de verificación de la intervención D2. Para aislamiento son especialmente relevantes PROV-02/03/04/05/06/08/09/10/11/12. Ninguno se marca PASS en este gate.

## 10. Límites causales y relación con estimandos

1. Un aislamiento material demostrado es condición para la arquitectura individual; no basta por sí solo para identificar θ_A.
2. El ITT-D2 sigue siendo el efecto total de asignar el paquete; una vía colateral no lo borra, pero impide atribuirlo exclusivamente a ΔT_acc*.
3. θ_A requiere además g_A1/g_A0 bien definidas, intervención factible, soporte conjunto bajo q_X* y r_common, consistencia, medición válida y un tratamiento defendible de interferencia.
4. C4 requiere contrato longitudinal propio y control de confusión post-Z; aislamiento no resuelve automáticamente esos problemas.
5. La ausencia de interferencia no acredita que D2 modifique ΔT_acc*, ni que no existan vías directas/colaterales.
6. La no-afectación de A1/A2/F2 y el firewall del oráculo/evaluador son requisitos distintos del aislamiento entre UE.

## 11. Estado de evidencia al cierre de Gate 121

| Elemento | Estado |
|---|---|
| Contrato de instancia única por UE | ACCEPTED LOGICAL RULE |
| Roster causal B / P*_{τ2} material | OPEN / NOT MATERIALIZED |
| IAM/C_SRC y snapshots observados | NONE |
| Inventario NODE/EDGE/consumidores | NONE / NOT MATERIALIZED |
| Grafo transitivo y dependencias externas | NOT OBSERVED |
| Cuotas, contención y consumo por UE/ventana | NOT OBSERVED |
| ACL/permisos efectivos y acceso cruzado | NOT OBSERVED |
| Aislamiento de agentes/canales/información | NOT DEMONSTRATED |
| No-afectación A1/A2/F2 y oráculo | CONTRACTS EXIST; MATERIAL EVIDENCE OPEN |
| Carryover/rollback material | NOT OBSERVED |
| UNIT-01…14 | DOCUMENTED; NOT IMPLEMENTED / NOT EXECUTED |
| PROV-01…12 | DOCUMENTED; NOT IMPLEMENTED / NOT EXECUTED |
| Asignación individual UE=UA | CONDITIONAL |
| Cluster / G_i | NOT SELECTED / NOT SPECIFIED |

**Conclusión científica:** a fecha de este gate, no puede afirmarse ni ausencia ni presencia efectiva de interferencia entre las UE materiales, porque el sistema experimental aún no está materializado ni inventariado. Lo correcto es mantener la arquitectura individual como preferida pero condicional, no sustituirla por una arquitectura de cluster especulativa y no declarar identificación.

## 12. Siguiente operación

La siguiente operación debe ser **Gate 122 — expediente mínimo de materialización probatoria de aislamiento**, que convierta IS-1…IS-8 en un conjunto cerrado de fuentes, artefactos, responsables, cobertura y criterios de adjudicación para el sistema B1/D2 concreto. Antes de capturar o materializar registros se debe comprobar autorización, alcance, disponibilidad de fuentes y compatibilidad con el contrato U_G vigente. Gate 122 no debe implementar, poblar, probar ni ejecutar por sí mismo.

## 13. Gobernanza y autorización

- No se modifica DEC-C10-103 ni se crean nuevas decisiones científicas.
- No se modifican C0, U_G, RMA, Evidence→Claim Matrix, STATUS ni `main`.
- No se crean nuevos IDs de prueba, schemas, columnas, tablas, clusters, mapas G_i, fixtures o datos.
- No se modifica código, PE, Generator, Analyzer o Evaluator.
- No se ejecutan validadores, tests, workflows, simulaciones, estimaciones, calibraciones o experimentos.
- PR #116 permanece Draft.
- `scientific_execution=false`; `execution_authorized=false`.

**Resultado:** `GATE_121_ISOLATION_EVIDENCE_PROTOCOL_SPECIFIED / HISTORICAL_CONTRACTS_REUSED / MATERIAL_INVENTORY_NONE / ISOLATION_NOT_DEMONSTRATED / UE_ASSIGNMENT_CONDITIONAL / NO_NEW_TEST_IDS / NO_SCHEMA_CHANGE / NO_FREEZE / NO_IMPLEMENTATION / NO_EXECUTION`.
