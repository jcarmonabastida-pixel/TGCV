# C10-S — Gate 112: reconciliación de G111-01…12 con DGP, asignación y arquitectura PE

**Fecha:** 2026-11-15 · **Rama:** research/c10-s-consolidation-draft · **PR:** #116 Draft  
**Estado:** DGP_INTERFERENCE_REQUIREMENTS_RECONCILED / ASSIGNMENT_SUPPORT_BLOCKERS_CONFIRMED / PE_STANDALONE_ARTIFACT_NOT_LOCATED / UNIT_SPECIALIZATION_REQUIRED / NO_NEW_TEST_IDS / NO_SCHEMA_CHANGE / NO_EXECUTION / NO_FREEZE.

## 1. Pregunta y alcance

Para cada gap G111-01…12 se determina si existe una regla documental reutilizable, si requiere especializar un contrato UNIT existente, si depende de una decisión/instanciación previa o si es una carencia de implementación/ejecución. No se reabren D2, población candidata, C1–C4, O-CONF/V_cont ni decisiones DEC. No se fijan parámetros, masas, tamaños, pesos, probabilidades o umbrales.

## 2. Fuentes y límites de recuperación

Recuperados en la rama research:
- DGP Temporal and Role Contract, en particular §§15, 28, 48 y 58–59.
- D2 Assignment, Population and Support Reconciliation, §§2–10.
- Outcome/Value Operationalization Reconciliation, especialmente O-CONF, V_cont y C4.
- Test Contract Register: §17 UNIT-01…14, QX, S4R, P177–P183, MEAS/MISS.
- Plan maestro §§16.188, 16.199–16.200, 16.259–16.261 y Gates 109–111.
- README, bootstrap, CANONICAL_STATE, STATUS y regla de reconstrucción histórica en main.

**Límite PE:** Gate 101/102 y el plan mencionan una “PE Integrated Technical Specification”, pero no se ha recuperado la ruta canónica exacta de un artefacto independiente con ese nombre. No se inventa ruta ni se declara auditada la especificación completa. Se reutilizan únicamente las fronteras Generator–Analyzer–Evaluator que sí están explícitas en el DGP y los contratos recuperados. Localizar el artefacto PE exacto queda como dependencia de trazabilidad.

## 3. Reconciliación de gaps

| Gap | Regla ya existente | Vacío real | Disposición |
|---|---|---|---|
| G111-01 aislamiento A | DGP §15: UE=UA solo sin recursos, agentes, información, infraestructura, estado, canales ni carryover compartidos; UNIT-02 | Sin roster/inventario material que demuestre aislamiento; el flag 'interference_absent' no lo prueba | OPEN material. Reutilizar UNIT-02 |
| G111-02 B intra/intercluster | DGP §15 y §28.2 EXC-B07: pool/mapa por unidad, cluster y tiempo; UNIT-03/06 | No separa contractualmente correlación basal, spillover intra-cluster y spillover entre clusters | Especializar UNIT-03/06, sin nuevo ID |
| G111-03 ponderación UE/cluster | UNIT-06/12 exige N/inferencia al nivel de asignación; DGP §15 indica N efectivo por clusters | Target/estimando UE frente a promedio cluster, pesos por tamaño y unidad de inferencia por resultado | Dependencia de estimando OPEN; no asumir equivalencia |
| G111-04 suficiencia de G_i | DGP §15 y §28.2/28.4: mapa previo, indexación i,j, cluster/pool y tiempo; UNIT-04/05/07 | Sin mapa versionado, regla de agregación, suficiencia, error o spillover residual | Especializar UNIT-04/05/07 |
| G111-05 probabilidades de exposición | UNIT-09/11; QX-06; D2 assignment separa p_i=P(Z_i=1|S_i,UA_i) de W_programmed | RNG, π, bloques y G_i no especificados; P(G_i=e) no derivable | Bloqueo previo: cerrar Z y G_i antes de probabilidades |
| G111-06 soporte conjunto | QX-05/06/07 y UNIT-09: ambas políticas factibles y ambos brazos positivos por historia | Sin roster/q_X*, soporte por (z,e), estrato/historia ni soporte longitudinal | Bloqueo de población/soporte. Separar asignación, exposición, g_A y C4 |
| G111-07 abstención D | UNIT-08/10; P177-10/12; P183-11/12; DGP define PASS/FAIL/INDETERMINATE | Sin denominadores para falsa identificación/atribución, abstención correcta/falsa abstención y bounds | Especializar P177-10/P183-11/12 con UNIT-08; umbrales OPEN |
| G111-08 aleatorización/provenance | UNIT-11 exige semilla, algoritmo, bloque/estrato, versión B, probabilidades/desviaciones; DGP §28.1 | RNG/versionado, derivación de semilla, vector Z inmutable/hash, mapping unidad→Z, PK y concealment OPEN | Dependencia de diseño OPEN; no inventar assignment_id ni reutilizar fixture/run/test IDs |
| G111-09 focal harness | README/harness: asignación individual y flag binario; no motor de clusters ni G_i | B/C/D no implementados en esa slice; UNIT no ejecutados | Límite de implementación confirmado; no se cierra documentalmente |
| G111-10 O-CONF/V_cont | OV reconciliation: O-CONF por instancia×ruta; V_cont truth por UE×K; DGP separa verdades | Mapping instancia/ruta→UE y estimandos/inferencia bajo cluster/exposición OPEN; K no es N | Regla de unidad reutilizada; crosswalk OPEN; no agregar por conveniencia |
| G111-11 C4 | D2 support §7 y OV §5: intervención mediadora, historia longitudinal, soporte y confusión mediador–resultado inducida por Z | Sin intervención mediadora bajo exposición ni estrategia longitudinal definida | Bloqueo de identificación; no derivar C4 de ITT/UNIT/G_i |
| G111-12 sensibilidad | DGP §28.2; P178-SIM-10/P183-10 | Sin clase de error de mapa, spillover residual, rangos defendibles ni robustez preespecificada | Especializar sensibilidad existente tras definir G_i; no fijar rangos |

## 4. Reglas reconciliadas documentalmente

1. UE, UA y UO son roles distintos; UE=UA solo bajo aislamiento completo demostrado. UO repetidas no aumentan N.
2. Si hay interferencia, no se conserva automáticamente ITT individual bajo SUTVA. Se requiere UA compatible o mapa de exposición previo; si el mapa es desconocido/incompleto, abstención o limitación interpretativa.
3. Correlación basal por cluster no equivale a spillover causado por Z.
4. Z no equivale a D2, W_programmed, intento, recepción, instalación, C_dep*, accesibilidad ni ΔT_acc*.
5. QX-06 (positividad de brazos por estrato/historia) no prueba positividad de G_i ni soporte de g_A.
6. O-CONF y V_cont conservan unidades/verdades separadas. V_cont es por UE a partir de K intervalos; K es granularidad temporal, no réplica experimental.
7. ITT-D2, θ_A/θ_Af y C4 son estimandos distintos. No hay resta residual automática ni mapping D2→g_A demostrado.
8. Generator conserva truth/potenciales; Analyzer recibe observación permitida; Evaluator accede a truth tras sellado. Un flag de no interferencia no demuestra aislamiento.

## 5. No duplicación

- UNIT-01…14 sigue siendo la familia primaria de interferencia.
- INT-01/02 no se reinterpretan como interferencia entre unidades.
- QX, P177, P178, P183, MEAS y MISS se reutilizan/especializan; no se duplican.
- unit_id, assignment_unit, fixture_id, run_id, scenario_id, cluster_id, event_id, instance_id, route_id y assignment_id no son sinónimos.
- No se define cluster retrospectivamente ni se infiere un mapa G_i desde una covariable individual.
- No se infiere positividad de exposición desde probabilidades marginales de Z.

## 6. Dependencias ordenadas

**D1. Unidades y asignación:** roster/UE, relación UE–UA–cluster, mecanismo Z, algoritmo/versión, π, semilla/provenance, vector inmutable y mapping UA→Z.  
**D2. Interferencia:** inventario de pools/recursos/canales/carryover; decisión justificada entre aislamiento, cluster o G_i; exposición y temporalidad.  
**D3. Población/soporte:** q_X* materializable, positividad de asignación, positividad de exposición y soporte conjunto; target UE vs cluster.  
**D4. Resultados/estimandos:** O-CONF instance×route→UE; V_cont UE×K; inferencia/ponderación; C4 solo con intervención mediadora y soporte longitudinal.  
**D5. Evaluación adversarial:** denominadores de falsa identificación/atribución y abstención; sensibilidad a mapa incorrecto y spillover residual.  
**D6. PE:** localizar el documento PE exacto y verificar interfaces, serialización, firewall y mapping de identidades/outputs. No inferir una especificación desde menciones históricas.

No se avanza a calibración, potencia, N/R ni implementación hasta resolver sus prerequisitos. No se materializa roster ni truth en este gate.

## 7. Dictamen

**GATE_112_RECONCILIATION_COMPLETED_WITH_EXPLICIT_DEPENDENCIES / DGP_INTERFERENCE_RULES_REUSED / UNIT_03_06_04_05_07_SPECIALIZATION_REQUIRED / P177_P183_ABSTENTION_SPECIALIZATION_REQUIRED / ASSIGNMENT_AND_EXPOSURE_PROBABILITIES_BLOCKED / UE_CLUSTER_WEIGHTING_OPEN / OCONF_VCONT_MAPPING_OPEN / C4_NOT_IDENTIFIED / PE_SPEC_PATH_NOT_VERIFIED / NO_NEW_TEST_IDS / NO_SCHEMA_CHANGE / NO_IMPLEMENTATION / NO_EXECUTION / NO_FREEZE.**

Los gaps no requieren una nueva familia de pruebas. La regla conceptual existe en parte; los vacíos pendientes son de instanciación del diseño, mecanismo Z, mapa/soporte de exposición, estimandos y evaluación del Analyzer. La especialización contractual solo debe hacerse después de recuperar PE y cerrar D1–D3.

## 8. Gobernanza

No se modifican main, RMA, Evidence→Claim Matrix, STATUS, DEC, C0, contratos fuente ni esquema U_G/PE. No se crean claves, tablas, fixtures, DDL o test IDs. No se ejecutan validadores, código, tests, workflows, simulaciones, estimaciones, calibraciones ni experimentos. PR #116 permanece Draft.  
scientific_execution=false; execution_authorized=false.

**Siguiente operación:** Gate 113 — localizar y recuperar la especificación PE exacta y verificar el crosswalk de identidades/roles y el firewall Generator–Analyzer–Evaluator. Si no existe o no es recuperable, registrar formalmente el límite de procedencia y no inferir una especificación desde menciones históricas.
