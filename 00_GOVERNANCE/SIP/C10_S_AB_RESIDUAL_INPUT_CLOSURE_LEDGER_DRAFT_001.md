# C10-S — AB residual input and closure ledger

**ID:** C10-S-AB-RESIDUAL-LEDGER-001  
**Version:** Draft 001  
**Date:** 2026-11-10  
**Branch:** `research/c10-s-consolidation-draft`  
**Status:** INTEGRATED WORKING LEDGER / NOT APPROVED AS DESIGN FREEZE / NOT IMPLEMENTABLE.  
**Authority:** DEC-C10-093 and DEC-C10-094; master C10-S §§216–233; accepted DEC-C10-068/069/071–079/090–092; D2 policy DEC-C10-066/067.  
**Purpose:** identify, in one place, which AB requirements are resolved at the documentary-design level, which remain material inputs, what evidence would close them, and which inputs must transfer to C. This ledger does not create a new scientific decision or replace the governing contracts.

## 1. Governing interpretation

AB-01…AB-09 are one integrated package, not nine independent redesign exercises. DEC-C10-093 accepts the working specialization baseline; DEC-C10-094 accepts the integrated material design resolutions. These decisions settle the conceptual choices within their scope. They do **not** establish that the relevant inventories, snapshots, policies, probabilities, routes, oracle or evidence exist in a materialized instance.

Use the following status vocabulary:

- **DESIGN RESOLVED:** the documentary rule/architecture is accepted; no conceptual reopening absent a documented contradiction.
- **MATERIAL INPUT OPEN:** the design specifies what must be supplied, but the actual value, instance, source or evidence is missing.
- **EVIDENCE GATE OPEN:** a claim such as completeness, isolation, invariance, independence or correctness requires evidence not yet present.
- **TRANSFER TO C:** the input is handed to the causal/measurement/statistical package; AB retains its source identity, version, definition and uncertainty.
- **NOT AUTHORIZED:** no executable fixture, parser, validator, code, simulation or experiment is authorized by this ledger.

A design-resolved row is not IMPLEMENTED, EXECUTED, AUDITED or ACCEPTED as an empirical result.

## 2. Integrated AB-01…AB-09 disposition

| Gate | Accepted documentary resolution | Remaining material input / evidence | Closure evidence and acceptance rule | Handoff |
|---|---|---|---|---|
| **AB-01 — CMP/PAR/REF/RUL/MET roster** | Reference identity is fixed by DEC-C10-069. Logical nucleus: one CMP, ENABLED and PROFILE PARs, one REQUIRE RUL, two semantically mandatory typed operand bindings, MET mandatory; POL outside minimal confirmatory nucleus. REF objects are not inferred from UDG references, FKs or EDGE. | Snapshot-scoped physical roster; whether the two operand bindings serialize as typed REF objects or AST links; IAM applicability/cardinality rows; exact record identities and coverage denominators. | Reconcile the governing accepted AST profile/grammar with DEC-C10-076/077/078; represent each operand relation exactly once; enumerate all applicable rows by stage, route and snapshot; prove coverage. REF=0 only if exhaustive inventory and IAM support it. | C receives frozen roster IDs, snapshot bindings, applicability and UNKNOWN/coverage status. |
| **AB-02 — C_src/C_dst/M, states and IAM** | ENABLED is BOOL without coercion. PROFILE mapping is total/injective over the accepted finite symbols: STD→STANDARD, RO→READ_ONLY, OFF→DISABLED. Preserve ABSENT/NULL/DEFAULT/VALUE distinctions. IAM is a logical, layered applicability contract. | Physical source/destination schemas and namespaces; canonical serialization for configuration payloads; resolved DEFAULT semantics; complete IAM rows/cardinalities; actual source/destination values and mapping coverage. | Every mandatory field has an explicit typed mapping or explicit failure/NA rule; no implicit defaults, lossy collapse or orphan references. Apply JCS only within DEC-C10-074's accepted UDG-01 envelope scope; do not extend it automatically to configuration payloads. | C receives versioned M, states, mapping statuses and measurement error/unknowns. |
| **AB-03 — F1/F2/A1/A2 and transformation identity** | Route roles and composition are accepted: F1→F2 focal, A1→A2 baseline alternative; B does not execute any route. DEC-C10-090/091/092 separate endpoint/interface/service, format/payload/events and A2 capability/implementation/execution. | Concrete transformation TID/SID/RID, versions, actors, artifacts, source/destination formats, pre/postconditions, dependencies, windows, errors, reversibility and route-specific event contracts. | Four versioned cards must be mutually compatible with the same source, destination, C0/G/H, mapping, IAM and F*. No alias or conceptual capability is treated as an observed/implemented transformation. | C receives route/version identities and any common-support or route-comparability limits. |
| **AB-04 — ID/REL/COND/AUTH/RES/DEP/BLOCK** | Predicate families, trivalent logic and distinction between focal DEP and alternative routes are specified. C_dep is not A_f; A_f is not execution or success. Functional authorization, technical ACL/credentials and agent knowledge remain distinct. | Field-level operationalization by unit, stage, route and snapshot; actual evidence sources; resource/capacity values; endpoint/dependency topology; authorization truth; coverage and adjudication. | Each applicable predicate has a definition, unit, time, domain, truth rule, observable evidence, coverage denominator and adjudication rule. Missing evidence propagates ?; it is not 0 or NA. | C receives independently measured A_f/D_f/ΔT_acc and their observation status, not inferred values. |
| **AB-05 — F*, C0, G, H and oracle** | F* is common and non-compensatory across both routes; FP-01…07 are functional, FP-08 is a separate evidence gate. G is the complete logical service unit/accepted roster. C0 is a pre-Z/pre-B immutable baseline with the fields enumerated in DEC-C10-094. | Atomic FP property profile and applicability; concrete C0 snapshot; H* anchor, value and unit; common tolerances/windows where relevant; oracle implementation-independent specification, validation evidence, blinding feasibility and adjudication record. | All required properties have ex-ante rules; same F* and H apply to F/A; any FP-01…07 failure yields F*=0, unresolved required property yields ?, all required properties=1 yields F*=1. FP-08 cannot alter F*. Oracle must be route/outcome-independent and versioned before fixtures. | C receives outcome-independent F* and event timing; H and measurement limitations enter estimand definitions. |
| **AB-06 — D2 policy/event mechanism** | D2 assignment policy is accepted. Z, B assignment, programming, receipt, compliance, attempt, actor, artifact/version, installation, retries, partial failure, rollback, background provision and crossover are distinct events. B does not execute F1/F2/A1/A2. | Actual actor/role, adapter artifact/version/hash, receipt protocol, time window, retry/failure/rollback rules, background-provision detection and material event evidence. | Event log must preserve the entire sequence and deviations; Z=1 must not be equated with receipt/attempt/success; Z=0 must not be equated with no background provision. | C receives the complete assignment/receipt/attempt/install event history and policy versions. |
| **AB-07 — joint technical distribution** | C_dep* is the conjunction of installation, integrity, compatibility and operability. A conditional joint distribution (16 cells per relevant stratum or validated equivalent) is required; independence and s=.80 are not assumed. | Numerical joint probabilities by arm/history/stratum, structural zeros if any, calibration rationale or explicit synthetic stipulation, sensitivity ranges and parameter provenance. | Distribution normalized; each cell in [0,1]; margins and conditional dependencies reported; sensitivity justified; no historical .20/.80 or s=.80 inserted as fact. | Transfer full joint distribution and sensitivity scenarios to C; retain AB source/version. |
| **AB-08 — eligibility, q_X*, units and interference** | Eligibility uses C0 pre-Z variables only. P*_τ2, P*_F and q_X* are distinct. Assignment, analysis and interference units are separate. Shared infrastructure requires cluster/exposure modelling, not assumed independence. | Executable-in-principle eligibility algorithm (documentary first), target population and strata, q_X* distribution/weights, positivity/support table, assignment/analysis/cluster topology and exposure mapping. | Reproducible pre-Z rule; no post-Z exclusions; common support explicitly enumerated; unsupported cells not extrapolated silently; interference unit matches shared resources/dependencies. | Direct transfer to C with population, support, cluster and q_X* version. |
| **AB-09 — alternatives, R0–R3 and truth/observed** | Alternative-route logic, finite-universe coverage rule, R0–R3 reuse, truth/observed separation and Generator/Analyzer/Evaluator separation are specified. Reach=0 requires exhaustive coverage; otherwise ?. | Material alternative universe and route inventory; scenario truth tables; measurement/missingness process; oracle validation, blinding and adjudication; Analyzer firewall proof. | Truth and observed datasets remain separate; no scenario labels or truth leak to Analyzer; each 1/0/? generated from explicit rules; no absence from missing records; R0/R1/R2/R3 classifications have declared universe and evidence. | C receives truth-sealed DGP scenario metadata only through Evaluator; Analyzer receives observed variables. |

## 3. Cross-gate dependencies and no-double-counting rules

1. **AB-01 ↔ AB-02:** the roster and mapping must use the same object/record identities, version and snapshot. An AST operand link is not counted again as a REF object; a UDG reference or U_G FK is not a configuration REF by default.
2. **AB-02 ↔ AB-03:** M maps declared source/intermediate/destination semantics; it does not itself prove F1/F2/A1/A2 execution or applied state.
3. **AB-03 ↔ AB-04:** route existence/capability does not prove predicate satisfaction. DEP is focal-route dependency, not proof that no A1/A2 route exists.
4. **AB-04 ↔ AB-05:** A_f* is adjudicated from its necessary predicates; F* is the separate functional endpoint for the complete route. Neither is inferred from C_dep* alone.
5. **AB-05 ↔ AB-06:** B cannot alter the oracle, F*, C0, IAM, permissions or baseline conditions under the isolated D2 design. Any observed change is a collateral path, not silently absorbed into the focal mechanism.
6. **AB-06 ↔ AB-07:** the joint C_dep distribution is conditional on the actual event mechanism; it cannot be reduced to one “success rate” without a justified factorization.
7. **AB-07 ↔ AB-08:** technical success and accessibility may vary with baseline history/strata; marginal probabilities do not establish positivity or transport.
8. **AB-08 ↔ AB-09:** alternative-route truth and Reach depend on the closed universe, population, horizon and coverage. An unknown route keeps the relevant absence/Reach result unknown.
9. **All gates ↔ C:** preserve the distinction among ITT_Z(D2), package effect, first stages, LATE_f, θ_Af(q_X*), θ_A(q), and mediation. No AB result licenses causal attribution to ΔT_acc→Value.

## 4. Material input register — no invented defaults

The following are the current hard blockers. Each requires a sourced value, explicit synthetic stipulation, or justified NOT_APPLICABLE decision; absence of input is not permission to choose a conventional default.

| Input ID | Required input | Current status | Permitted resolution |
|---|---|---|---|
| AB-M01 | REF versus AST physical representation | OPEN | Grammar/schema reconciliation; choose one encoding per operand, never both |
| AB-M02 | C_src/C_dst/M physical schema and canonicalization | OPEN | Explicit schema/encoding decision; do not extend UDG-01 JCS by assumption |
| AB-M03 | TID/SID/RID and concrete transformation cards | OPEN | Source-backed identity/version contracts or explicitly bounded synthetic specification |
| AB-M04 | Predicate field roster and source/capture method | OPEN | Field-by-field mapping to U/R/C/X/E_T and evidence coverage |
| AB-M05 | H* common anchor, value and unit | OPEN | Explicit pre-specified protocol decision; same for F and A |
| AB-M06 | MD-C1/MD-C4 isolation and A1/A2 non-affectation | OPEN | Material manifests, before/after snapshots and functional equivalence evidence |
| AB-M07 | D2 event probabilities and joint C_dep distribution | OPEN | Calibration or explicit DGP stipulation plus sensitivity; no inherited .20/.80 or .80 |
| AB-M08 | Eligibility algorithm, q_X*, support and strata | OPEN | C0-only algorithm and explicit population distribution/support |
| AB-M09 | Assignment/analysis/interference units | OPEN | Topology-backed cluster/exposure definition |
| AB-M10 | Independent oracle, blinding and adjudication | OPEN | Pre-fixture versioned specification and validation plan/evidence |
| AB-M11 | R0–R3 truth tables and observation/missingness model | OPEN | Scenario-by-scenario truth and observation rules; keep truth sealed |

## 5. Handoff contract AB → C

C must consume, not recreate, the AB outputs below with their exact IDs and versions:

- instance/roster/M/IAM/C0/G/H and snapshot identities;
- transformation cards and route universe;
- predicate definitions and independent A_f/D_f/ΔT_acc measurement contracts;
- D2 event history and joint C_dep distribution;
- eligibility, population, q_X*, support and interference structure;
- R0–R3 truth/observed scenario definitions and oracle/adjudication provenance.

Any unresolved AB field enters C as OPEN/UNKNOWN with its source and scope. C may perform sensitivity or partial-identification analysis around it, but may not silently fill it.

## 6. Next integrated operation

The next operation remains within AB and should resolve, in one coordinated pass, the highest-dependency documentary items before requesting unavailable material values:

1. reconcile AB-M01/02 against the current accepted AST, REF, UDG and mapping contracts, including the limited scope of DEC-C10-074;
2. consolidate the four transformation cards and their source/destination contracts without inventing TID/SID/RID;
3. complete the predicate-to-field/evidence crosswalk for AB-04;
4. prepare the exact minimal decision set for H*, MD-C1/MD-C4, D2 joint probabilities, q_X*/population and cluster topology.

Only after this pass should remaining user decisions or external material inputs be requested. No implementation is implied.

## 7. Authorization and status

AB remains **IN_PROGRESS / DESIGN RESOLVED IN PART / MATERIAL INPUTS AND EVIDENCE OPEN**. This ledger is a documentary reconciliation, not Design Freeze, not implementation readiness and not scientific evidence.

`scientific_execution=false`; `execution_authorized=false`.

No code, parser, validator, executable fixture, simulation or experiment is created or authorized by this ledger.

## 8. Resultado de la reconciliación documental AB-M01/M02 (2026-11-10)

Esta pasada ha contrastado el catálogo atómico, contrato abstracto de instancia, gramática RUL, matriz M, plantilla U_G y DEC-C10-054/068/069/074/076/077/078/093/094.

### 8.1. AB-M01 — operand bindings: conclusión acotada

- DEC-C10-054 fija el perfil de AST declarativo acíclico (profundidad 4, máximo 16 átomos por regla y 16 reglas por paquete), con efectos nucleares REQUIRE/FORBID y UNKNOWN no convertido silenciosamente. No acepta una sintaxis física concreta ni un parser.
- DEC-C10-068 fija la regla RUL-SVC-ENABLE-PROFILE-01 y sus dos referencias semánticas a PAR-SVC-ENABLED y PAR-SVC-PROFILE; la expresión aceptada es OR(NEQ(ENABLED,true),IN(PROFILE,{STANDARD,READ_ONLY})).
- DEC-C10-094 exige que los dos operand bindings estén representados exactamente una vez, como dos REF tipados o dos enlaces AST tipados según la gramática canónica.
- DEC-C10-076/077 regulan referencias tipadas UDG y objetos REF de configuración, respectivamente; no autorizan a confundirlos. Una FK U_G, EDGE o referencia del envelope no crea por sí misma un objeto REF.
- La plantilla U_G es un registro de inventario/evidencia y no contiene tablas físicas dedicadas CMP/PAR/REF/RUL/MET. Sus filas son plantilla vacía; no hay snapshots C10-S materializados ni evidencia de cobertura en esa plantilla.

**Conclusión AB-M01:** quedan definidos el número y significado de los dos operand bindings; no es posible seleccionar responsablemente REF físico frente a enlaces AST tipados con las fuentes actuales. El gate permanece OPEN hasta reconciliar la gramática/sintaxis AST y el modelo de serialización del objeto. No se duplicarán los operandos como REF y AST a la vez.

### 8.2. AB-M02 — namespaces, mapping y canonicalización

- El mapping semántico de PROFILE es total e inyectivo para el dominio aceptado: STD→STANDARD, RO→READ_ONLY, OFF→DISABLED. ENABLED conserva BOOL con igualdad exacta y sin coerción.
- DEC-C10-068 no acepta DEFAULT contractual para ENABLED ni PROFILE. DEFAULT se mantiene como estado genérico del contrato abstracto, pero no se introduce en la instancia confirmatoria aceptada sin decisión expresa. ABSENT/NULL/DEFAULT/VALUE no se colapsan.
- La matriz M distingue C_src, C_dst declarado y C_dst aplicado; no existe todavía schema/payload físico de estos objetos, ni namespace físico completo/versionado para cada etapa.
- DEC-C10-074 acepta JCS únicamente para el envelope UDG-01 bajo el perfil TGCV-C10S-JCS-1. No se extiende automáticamente a payloads de configuración, S1/S2 ni C_src/C_dst. Los artefactos de intercambio/payload requieren un contrato propio o una decisión explícita de reutilización con alcance y compatibilidad justificados.
- MET debe fijar identidades y versiones independientes de contrato, instancia, esquemas fuente/destino, mapping, IAM y oráculo. Hashes no se calculan ni interpretan como equivalencia semántica antes de fijar la serialización aplicable.

**Conclusión AB-M02:** el mapping semántico BOOL/ENUM está resuelto a nivel documental; namespaces/códigos físicos, serialización, canonicalización de payload y filas IAM de instancia permanecen OPEN. No se adopta JCS para el payload por analogía ni se inventa un schema.

### 8.3. Cambios de estado permitidos por esta pasada

| Subgate | Estado tras reconciliación |
|---|---|
| AB-01: roster lógico y operandos | DESIGN RESOLVED |
| AB-01: encoding físico REF/AST | OPEN |
| AB-01: IAM por snapshot/etapa/ruta y cobertura | OPEN |
| AB-02: mapping semántico BOOL/ENUM | DESIGN RESOLVED |
| AB-02: namespaces/schema/serialización de payload | OPEN |
| AB-02: canonicalización de C_src/C_dst/M | OPEN |
| AB-02: DEFAULT en instancia confirmatoria | NOT_IN_BASELINE; no introducir sin decisión |

No se ha creado un nuevo Decision Record ni se ha alterado el alcance de DEC-C10-074/076/077/078. No se han generado registros, snapshots, filas IAM, hashes ni observaciones.

## 9. Resultado de la reconciliación documental AB-M03/M04 y hallazgo temporal (2026-11-10)

### 9.1. AB-M03 — las cuatro cards no son cuatro transformaciones ya especificadas

Se contrastaron la reconciliación histórica de transformation cards, la propuesta Opción A/F*, el crosswalk D2 de A_f*, DEC-C10-090/091/092 y el DAG §233.

- F1/τ2 tiene función candidata más desarrollada: conversión focal S0→S2, habilitada por la dependencia provisionada. Su TID/SID/RID, formato, contrato de conversión, precondiciones, recursos y evidencia no están cerrados.
- F2 solo tiene posición S2→SF y rol general de aplicación/verificación focal; su función técnica y contrato de aplicación concretos siguen OPEN.
- A1 solo tiene posición S0→S1 y rol general de exportación alternativa; formato/mecanismo baseline y su contrato siguen OPEN.
- A2 tiene la descomposición conceptual aceptada por DEC-C10-092 como importador/consumidor, con recepción, parseo, validación, mapping, aplicación, verificación y procedencia separados. Su implementación, formato, parser, mapping, eventos y evidencia siguen OPEN.
- DEC-C10-090/091/092 refinan descomposición conceptual; no proporcionan IDs transformacionales canónicos ni demuestran existencia/operación material.
- Las cards no deben rellenarse con un producto, formato, endpoint, versión, comando o TID inventado. Los aliases F1/F2/A1/A2 no se convierten en TID/SID/RID.

**Conclusión AB-M03:** contratos funcionales de ruta y obligaciones de transición están definidos a nivel conceptual, pero no hay cuatro cards materiales completas. AB-03 permanece OPEN en identidad y especificación material de las transformaciones. No se puede declarar A1/A2 no afectadas por B sin MD-C1/MD-C4.

### 9.2. AB-M04 — crosswalk causal y agregación existen; captura por campo no existe

El crosswalk D2 de A_f* ya reconcilia ID/REL/COND/AUTH/RES/DEP/BLOCK y evita duplicidades; la auditoría MEAS-001 y su regla trivalente §§10–11 distinguen truth, observed_state, evidence_status, coverage_status, matching y D_f basal→post. La Path Predicate Temporal Evidence Matrix proporciona la estructura por paso/rama/tiempo.

No obstante:
- el crosswalk es semántico, no un inventario de campos efectivos;
- B-M01…15 son superficies de inspección, no observaciones ni variables pobladas;
- el manifiesto B marca sus superficies como NO INVENTARIADO o evidencia no disponible;
- la plantilla U_G está vacía y sin snapshots C10-S reales;
- no hay por unidad/version/snapshot un field_id, valor/diff, fuente, event_id, truth, observed_state, denominador de cobertura y adjudicación que permita cerrar los predicados.

**Conclusión AB-M04:** definición y lógica de adjudicación documental PARTIAL/DESIGN RESOLVED; operacionalización material y evidencia NONE/OPEN. No asignar 1/0 ni afirmar invariancia; conservar ?.

### 9.3. Hallazgo AB-TIME-01 — discrepancia de indexación temporal entre contratos

El contrato temporal DGP §2 utiliza t−1 para baseline pre-Z, t0 para asignación Z, t1 para política/recepción/intento, t2 para instalación/verificación, t3 para snapshot de accesibilidad y t4 para Reach. La Path Predicate Temporal Evidence Matrix §2 utiliza t0 para baseline pre-Z, t1 para asignación/oferta/recepción/intento, t2 para verificación y t3 para snapshot; ambos llevan Reach en t4 y t5–t9 para mecanismos y resultados.

El orden causal sustantivo es compatible, pero los índices t−1/t0/t1 no están armonizados y el contrato de la matriz comprime asignación y política en un único índice. El DAG §233 adopta la convención del DGP temporal, pero esa precedencia aún debe registrarse explícitamente en un crosswalk temporal aceptado.

**Resolución provisional segura:** identificar eventos por nombre y precedencia (BASELINE_PRE_Z → ASSIGNMENT_Z → POLICY/PROVISION → INSTALL_VERIFICATION → ACCESSIBILITY_SNAPSHOT → REACH → KNOWLEDGE → SELECTION → EXECUTION → OUTCOME → VALUE), sin comparar ni reutilizar índices numéricos entre documentos hasta reconciliarlos. No se sobrescriben timestamps ni snapshots históricos.

**Estado:** AB-TIME-01 OPEN; afecta AB-03/04/05/06/08 y el handoff a C. No cambia el orden causal ya definido ni autoriza implementación.

### 9.4. Estado de subgates tras esta pasada

| Subgate | Estado |
|---|---|
| AB-03: composición F1→F2/A1→A2 | DESIGN RESOLVED |
| AB-03: identidad y cards materiales TID/SID/RID | OPEN |
| AB-04: semántica A_f* y lógica 1/0/? | DESIGN RESOLVED / PARTIAL |
| AB-04: inventario/captura/evidencia por campo | OPEN / NONE |
| AB-TIME-01: índices numéricos armonizados | OPEN |
| AB-M06: aislamiento y no-afectación A1/A2 | OPEN |

No se ha inventado ninguna función transformacional, TID, dato de campo, estado truth, timestamp ni cobertura.

## 10. Reconciliación AB-M05…M11 y precisión sobre H (2026-11-10)

### 10.1. AB-M05 — F*, C0, G, H y oráculo

DEC-C10-094 acepta G como unidad lógica de servicio y roster constitutivo; C0 como snapshot basal inmutable anterior a Z y programación B, con identidad/versiones, fuente/destino, runtime/host, permisos, recursos, estados F/A, rutas de fondo, unidad/cluster, reloj/ventana y versiones M/IAM/oráculo. F* es común y no compensatorio; FP-08 es probatorio y separado.

**AB-TIME-02 / H-01:** H* en DEC-C10-094 es horizonte temporal común, con ancla, valor y unidad por fijar. La Path Predicate Matrix §2 también usa H=3 como profundidad máxima candidata del grafo de transformaciones, con rutas de longitud 2. Profundidad de ruta y horizonte temporal no son el mismo objeto y no pueden compartir el símbolo/valor por inferencia. Se debe reservar, por ejemplo, H_path para profundidad y H_time para ventana temporal, sin alterar las decisiones hasta su aceptación formal.

El oráculo se define como independiente de ruta y de Outcome/Value, versionado antes de fixtures, con separación Generator/Analyzer/Evaluator y cegamiento cuando sea viable. Sigue sin implementación, validación, evidencia de independencia ni adjudicación aplicada.

### 10.2. AB-M06 — MD-C1/MD-C4

El manifiesto B-M01…15 y los contratos PROV-01…12 definen qué inspeccionar. Las superficies siguen NO INVENTARIADO/NONE; ARCH-B1 es candidata, no implementación. MD-C1 (manifiesto completo de cambios de B) y MD-C4 (no-afectación funcional de A1/A2) permanecen OPEN. No puede afirmarse aislamiento, invariancia ni exclusión IV. Si no se demuestra, el ITT se interpreta como efecto de política/paquete.

### 10.3. AB-M07 — mecanismo y distribución conjunta D2

DEC-C10-067 fija las probabilidades de programación por política como reglas de diseño: P(W_programmed=1|Z=0)=0 y P(W_programmed=1|Z=1)=1. No son probabilidades de intento efectivo ni de recepción/instalación. Cumplimiento/recepción, intento efectivo, provisión de fondo/crossover, fallos parciales, retries y rollback siguen OPEN. La distribución conjunta condicional de C_install/C_integrity/C_compat/C_oper debe sumar 1 en 16 celdas por estrato relevante (o parametrización conjunta validada); no hay probabilidades numéricas aprobadas. s=.80 y .20/.80 no son valores confirmatorios.

### 10.4. AB-M08/M09 — población, soporte y unidades

P*_τ2 y P*_F son poblaciones distintas; la segunda exige además ausencia respaldada de ruta funcional alternativa. La elegibilidad se fija con C0 pre-Z y no puede depender de variables postratamiento. Sin embargo, el algoritmo final, los valores/estratos de q_X*, la distribución objetivo, pesos, common support y positividad no están materializados. La unidad lógica de servicio no resuelve por sí sola unidad de asignación, análisis e interferencia. La topología de host/adaptador/permisos/recursos compartidos no está inventariada; no se asume independencia individual.

### 10.5. AB-M10/M11 — oráculo, escenarios y proceso de observación

La separación Generator/Analyzer/Evaluator, truth/observed, R0–R3 y las reglas 1/0/? están definidas documentalmente. El universo de rutas y el grafo candidato no son exhaustivos; la cobertura actual de nodos/aristas/predicados es NONE. No existen truth tables materiales completas ni un modelo de observación/missingness calibrado. La validación del oráculo, cegamiento operativo, adjudicación y firewall del Analyzer no se han ejecutado ni demostrado.

### 10.6. Disposición consolidada

| Input | Estado documental | Estado material/evidencia |
|---|---|---|
| H* temporal (ancla, valor, unidad) | Regla común definida | OPEN |
| H_path / profundidad | Candidato H=3 en Path Matrix | No confundir con H_time; reconciliación OPEN |
| MD-C1/MD-C4 | Criterios documentados | OPEN / NONE |
| Programación D2 | Regla determinista de política aceptada | DESIGN RESOLVED |
| W_attempt/receipt/background/crossover | Variables separadas | OPEN |
| C_dep joint distribution | Forma contractual definida | OPEN / sin probabilidades |
| P*_τ2/P*_F y elegibilidad | Poblaciones diferenciadas | Algoritmo/valores OPEN |
| q_X*, soporte y positividad | Régimen común basal exigido | OPEN |
| Unidad/interferencia | Distinciones definidas | Topología/exposure OPEN |
| Oracle/firewall/adjudication | Arquitectura definida | Validación/evidencia OPEN |
| R0–R3 | Familias descritas | Truth tables y observación OPEN |

No se asignan valores numéricos ni se promueven candidatos a parámetros aceptados.

## 11. Propuesta integrada de resolución AB-01…AB-09 — paquete para aceptación, no aprobado (2026-11-10)

### 11.1. Regla de decisión

Esta propuesta convierte el registro de inputs §§2–4 y las reconciliaciones §§8–10 en una ruta única de cierre. No crea DEC ni cambia DEC-C10-093/094. Separa:
- **decisiones de diseño sintético** que pueden aceptarse sin evidencia de un sistema real;
- **reconciliaciones técnicas documentales** que deben resolverse contra contratos ya aceptados;
- **inputs numéricos o topológicos** que necesitan justificación explícita;
- **evidencia material** que no puede sustituirse por una estipulación del DGP cuando el gate exige demostrar no-afectación o cobertura observada.

La meta de AB es una instancia sintética internamente completa y trazable, no simular que se ha inspeccionado una plataforma real. Una estipulación de verdad del DGP no se reportará como evidencia observada ni como prueba de invariancia empírica.

### 11.2. Disposición recomendada por gate

| Gate | Propuesta de resolución integrada | Qué se puede cerrar por diseño | Qué no se debe fingir cerrado |
|---|---|---|---|
| AB-01 | Mantener exactamente dos operand bindings semánticos. Resolver su representación una sola vez contra la gramática/serialización aceptada: AST tipado si la gramática define el binding como nodo del árbol; REF tipado si el contrato define objetos de referencia independientes. No duplicar. | Cardinalidad y significado de los dos operandos ya DESIGN RESOLVED. | Encoding físico, schema y roster IAM real; no elegir REF/AST por preferencia estética. |
| AB-02 | Conservar BOOL/ENUM y mapping ya resueltos. Definir schema y serialización específicos del payload de configuración solo después de cerrar el modelo físico; fijar canonicalización con alcance explícito y pruebas semánticas. | Mapping semántico ENABLED/PROFILE. | No extender JCS UDG-01 a C_src/C_dst/S1/S2 por analogía; no introducir DEFAULT en la instancia confirmatoria. |
| AB-03 | Definir cuatro cards sintéticas versionadas dentro del DGP, con IDs de instancia propios y contratos de entrada/salida, pre/postcondiciones y eventos. Describir F1 como conversión, F2 como aplicación/verificación, A1 como exportación y A2 como importación/aplicación; no elegir producto, formato o mecanismo real. | Roles, topología F1→F2 y A1→A2, F* común y obligaciones FP. | No declarar identidad real, independencia A1/A2, compatibilidad o ejecución. La no-afectación en R0 se estipula en truth DGP y se contrasta con R2 adversarial; no se llama evidencia empírica. |
| AB-04 | Reutilizar el crosswalk A_f*, la matriz temporal y la lógica 1/0/?. Añadir solo los field_id sintéticos necesarios para instanciar cada predicado y enlazarlos con U/R/C/X/E_T, snapshot, etapa y ruta. | Definiciones y regla de adjudicación trivalente. | No poblar como hechos reales B-M01…15; no asignar 0 ante cobertura ausente; no duplicar matrices. |
| AB-05 | Mantener F* no compensatorio y común. Separar H_path (profundidad de ruta candidata) de H_time (ventana temporal de evaluación). Proponer el valor/unidad de H_time solo después de fijar el horizonte de Outcome/Value en C. | Estructura C0/G/F* y distinción H_path/H_time. | No usar H=3 como duración; no inventar ancla/valor/unidad de H_time; oráculo aún no validado. |
| AB-06 | Especificar en el DGP el actor lógico, artefacto y versión como entidades sintéticas explícitas; conservar separados Z, B, W_programmed, W_attempt, receipt, S_install, componentes C_dep, retry y rollback. | Política D2 y secuencia de eventos conceptuales. | No atribuir recepción/éxito a programación; no declarar ausencia real de provisión de fondo ni completar hashes reales. |
| AB-07 | Parametrizar C_dep* como distribución conjunta de los cuatro componentes, condicional a brazo e historia/estrato; reportar márgenes, dependencias y sensibilidad. La distribución debe normalizarse por celda/estrato. | Forma del objeto conjunto y restricciones de probabilidad. | No fijar s=.80 ni .20/.80 como confirmatorios; valores solo tras justificación/sensibilidad y aceptación. |
| AB-08 | Definir elegibilidad exclusivamente desde C0 pre-Z. Mantener P*_τ2 y P*_F separados. Construir q_X* como distribución objetivo explícita y publicar soporte/positividad por estrato; no extrapolar fuera del soporte. | Regla temporal de elegibilidad y distinción de poblaciones. | No elegir población, pesos, estratos ni distribución objetivo por conveniencia; no confundir unidad lógica G con unidad de asignación/análisis. |
| AB-09 | Reutilizar R0–R3 y la segregación Generator/Analyzer/Evaluator. Completar truth tables y proceso observado separado: R0 aislado; R1 alternativa basal preservada; R2 vía colateral sobre alternativa/dependencia; R3 fallo/no éxito de provisión. Incluir missingness/medición diferencial sin alterar truth. | Arquitectura de roles, familias y regla de cobertura. | No afirmar universo exhaustivo, independencia del oráculo, cegamiento o firewall probado sin validación. |

### 11.3. Recomendación de diseño para el DGP base y los escenarios adversariales

Se recomienda que el DGP sintético contenga dos capas claramente etiquetadas:

1. **Base aislada R0:** D2 programa el intento según DEC-C10-067; los factores no focales requeridos por la decisión se mantienen invariantes por construcción; la única ruta causal pretendida hacia accesibilidad es la provisión técnica focal y sus componentes. Esto permite comprobar recuperación bajo una verdad conocida, pero no demuestra que un sistema real satisfaga exclusión.
2. **Adversariales R1–R3 y extensiones:** alternativa basal; modificación colateral de A1/A2/dependencias; fallo parcial/crossover/rollback; recursos compartidos/interferencia; información/conocimiento; medición/missingness diferencial. Cada intervención adversarial cambia una familia identificable, sin colapsar el efecto de paquete con el efecto focal.

La ausencia de interferencia solo puede asumirse en R0 como estipulación del DGP; debe existir al menos un escenario adversarial con interferencia/recursos compartidos para comprobar que el Analyzer no declara identificación individual cuando la verdad no la permite.

### 11.4. Decisiones que requieren aceptación expresa del usuario

La documentación permite recomendar, pero no aceptar unilateralmente, estas elecciones de diseño:

- **AB-03-SYN:** utilizar cuatro identidades transformacionales sintéticas versionadas, sin producto ni formato real, para que las cards sean completas como especificación de DGP.
- **AB-05-H:** reservar H_path para profundidad y H_time para horizonte; dejar H_time pendiente hasta completar Outcome/Value en C.
- **AB-08-POP:** fijar una población objetivo sintética mediante elegibilidad C0 pre-Z y q_X* explícito, sin seleccionar todavía valores o pesos no justificados.
- **AB-09-INT:** permitir no interferencia solo como verdad estipulada de R0 y exigir escenarios adversariales con interferencia; no convertirlo en supuesto general.
- **AB-06/07-PARAM:** autorizar que los parámetros D2 y la distribución conjunta C_dep se propongan como parámetros sintéticos justificables mediante análisis de sensibilidad, sin reutilizar los números históricos como hechos.

Las reconciliaciones REF/AST y schema/canonicalización son tareas técnicas contra contratos existentes, no elecciones científicas libres. La evidencia MD-C1/MD-C4 y la cobertura observada permanecen gates probatorios; no se cierran por esta propuesta.

### 11.5. Secuencia única de cierre y criterios de salida AB

1. Resolver REF/AST y payload schema/canonicalización contra la gramática y contratos vigentes, sin modificar su alcance.
2. Completar cards sintéticas F1/F2/A1/A2 y el crosswalk field-level usando la instancia aceptada; mantener UNKNOWN donde falten observaciones.
3. Definir C0, actor/artefacto/versiones sintéticas, H_time pendiente, población/q_X* y unidades; someter las elecciones enumeradas en §11.4 a aceptación.
4. Definir la distribución conjunta C_dep y escenarios R0–R3 más adversariales, con verdad y observación separadas.
5. Cerrar oráculo, adjudicación y firewall como especificación verificable, distinguiendo validación propuesta de validación ejecutada.
6. Actualizar y releer los instrumentos existentes y realizar una reconciliación cruzada única con DEC-C10-093/094 y los contratos AB.

**AB solo pasará a DONE** cuando la instancia/DGP sea autocontenida y versionada, todas las cards y mappings tengan criterios de aceptación, los inputs de población/horizonte/unidad/parámetros estén aceptados o explícitamente limitados, los escenarios y truth tables estén completos, y no quede contradicción temporal/semántica conocida. La ausencia de evidencia real puede permanecer como límite declarado de un experimento sintético, pero nunca se reportará como invariancia observada.

**Estado de esta propuesta:** NOT APPROVED / FOR USER ACCEPTANCE. AB permanece IN_PROGRESS; no hay Design Freeze, implementación, fixtures, validación ejecutada, simulación ni ejecución científica. scientific_execution=false; execution_authorized=false.

## 12. Registro de aceptación expresa del usuario — propuesta integrada AB (2026-11-10)

El usuario acepta expresamente la propuesta integrada de §11 como base de trabajo para continuar la concreción de AB, con la reserva explícita de mantener abiertos los valores numéricos y las decisiones de horizonte temporal que aún no estén justificadas.

**Decisiones aceptadas como reglas de diseño del DGP:**
- **AB-03-SYN — ACCEPTED:** completar cuatro identidades transformacionales sintéticas versionadas F1/F2/A1/A2, sin seleccionar producto, formato ni mecanismo real y sin declarar implementación.
- **AB-05-H — ACCEPTED:** separar H_path (profundidad de ruta) de H_time (horizonte temporal). H_time, su ancla, valor y unidad quedan OPEN hasta completar Outcome/Value y justificar la ventana.
- **AB-08-POP — ACCEPTED WITH BOUNDARY:** elegibilidad definida exclusivamente desde C0 pre-Z; mantener P*_τ2 y P*_F separados; q_X* debe ser explícito y compatible con soporte/positividad. No se aceptan todavía población numérica, pesos, estratos ni distribución objetivo concretos.
- **AB-09-INT — ACCEPTED WITH BOUNDARY:** ausencia de interferencia solo como verdad estipulada del escenario sintético R0; incorporar escenarios adversariales con interferencia/recursos compartidos. No es supuesto general ni evidencia empírica.
- **AB-06/07-PARAM — ACCEPTED AS METHOD, NOT VALUES:** se autoriza proponer parámetros sintéticos D2 y distribución conjunta C_dep mediante justificación y análisis de sensibilidad. No se aprueban valores numéricos ni se reutilizan s=.80 o .20/.80 como confirmatorios.

**Reconciliaciones técnicas que siguen siendo tareas, no decisiones científicas:** resolver REF/AST y schema/canonicalización contra la gramática y contratos vigentes; una única representación física por binding. No se extiende JCS UDG-01 al payload de configuración.

Esta aceptación no aprueba el DAG como identificación causal empírica, no satisface MD-C1/MD-C4, no demuestra cobertura, exclusión ni no-afectación real, no cierra AB y no constituye Design Freeze, autorización de implementación o autorización de ejecución.

**Estado actualizado:** AB-03-SYN, AB-05-H (regla de separación), AB-08-POP (regla de elegibilidad/separación), AB-09-INT (regla de escenarios) y AB-06/07-PARAM (método de parametrización) = ACCEPTED DESIGN RULES WITH OPEN MATERIAL INPUTS. AB permanece IN_PROGRESS. H_time, población/q_X* numéricos, soporte, unidad/interferencia real, parámetros, verdad/observación y evidencia material permanecen OPEN. scientific_execution=false; execution_authorized=false.

## 13. AB-M01 — reconciliación semántica de los operand bindings (2026-11-10)

**Resultado documental: AST_TYPED_PARAMETER_BINDINGS — DESIGN RESOLVED; physical serialization OPEN.**

La reconciliación entre el contrato abstracto de instancia §§3.4/6, la gramática mínima §§3/9/11/12, el perfil DEC-C10-054 y la instancia RUL-SVC-ENABLE-PROFILE-01 aceptada por DEC-C10-068 permite resolver la alternativa semántica:

1. Los dos operandos de la regla son referencias tipadas a claves PAR ya declaradas: ENABLED (BOOL) y PROFILE (ENUM).
2. Su función es enlazar hojas/operand positions del AST de RUL con parámetros de la misma instancia; no representan relaciones constitutivas entre componentes ni referencias a recursos/dependencias del paquete.
3. Por tanto, **no se crean dos objetos REF de configuración** para esos operandos. Se representan una sola vez como bindings tipados del AST a parameter_key, con tipo esperado y resolución contra el roster PAR.
4. Se conserva la cardinalidad semántica exactamente dos; un binding no puede duplicarse simultáneamente como REF y como AST operand.
5. Un REF de configuración solo se incorporará si el inventario revela una relación/dependencia constitutiva independiente, con sus propios extremos, tipo, dirección y cardinalidad; no por el mero hecho de que un AST consulte un parámetro.

La expresión de referencia documentada es OR(NEQ(ENABLED,true),IN(PROFILE,{STANDARD,READ_ONLY})) bajo REQUIRE. El binding debe resolver ENABLED→PAR-SVC-ENABLED/BOOL y PROFILE→PAR-SVC-PROFILE/ENUM; la gramática conserva operadores y dominios finitos. Esta resolución no introduce una sintaxis serializada concreta ni parser.

**Qué queda OPEN en AB-M01/M02:** nombres físicos de campos/nodos, encoding/schema del AST, serialización canónica del AST, namespace/versionado del parameter_key, constraints físicas y validación de integridad. No se extiende JCS UDG-01 a este payload. El contrato físico debe implementar la referencia tipada y verificar destino existente, tipo concordante y cardinalidad exactamente una.

**Criterio de cierre documental AB-M01:** binding AST tipado a PAR; dos operands y solo dos; no REF duplicado; referencia exacta a claves/versiones PAR del snapshot de instancia; UNKNOWN si el binding o destino no se resuelve. Estado: semántica DESIGN RESOLVED; encoding y validación técnica OPEN.

## 14. Resultado integrado AB-03/04 — especificación semántica sintética (2026-11-10)

AB-03 queda especificado a nivel abstracto sintético en la §12 de la propuesta de cards. Las cuatro TID/SID son DGP-locales: F1 conversión focal S0→S2; F2 aplicación/verificación S2→SF; A1 exportación alternativa S0→S1; A2 importación/aplicación/verificación S1→SF. La instancia común reutiliza IDs y versiones aceptados de servicio/CMP/PAR/RUL. No se asignan RID/EID ni mecanismo real.

AB-04 queda especificado como crosswalk de field_id semánticos hacia U*/R*/C*/X*/E_T, con índice unidad×escenario×rama×paso×TID/SID×snapshot×tiempo. Incluye estado de entrada/salida, predicados ID/REL/COND/AUTH/RES/DEP/¬BLOCK, APP separado, mapping, evidencia, cobertura y adjudicación. Truth_DGP y observed_state no se mezclan; se reutiliza PM-01…18 y la regla 1/0/? vigente.

**No cerrados:** schema físico y nombres de columnas; mapping M/M_A concreto; predicados FP atómicos/requiredness, tolerancias, C0, recursos y regla de reserva, C_dep conjunta, H_time, universo exhaustivo de alternativas, truth tables por escenario, MD-C1/MD-C4, evidencia, oráculo/fiabilidad/cegamiento/validación. AB sigue IN_PROGRESS; no fixtures ni ejecución.


## 15. AB-01/02 — cierre de reconciliación semántica (2026-11-10)

La reconstrucción histórica identifica trabajo ya aceptado que debe reutilizarse: DEC-C10-054 (AST 4/16/16), DEC-C10-068/069 (instancia y regla), DEC-C10-071/083 (siete stage_key y PAR), DEC-C10-079/080/081 (manifiesto/binding probatorio PAR) y DEC-C10-082 (anclaje CMP↔NODE por snapshot). No se recrean estas decisiones.

Se integra el mapping semántico de CMP/PAR/RUL/MET y la composición de mappings de F/A. Los dos PAR preservan clave/tipo/dominio/estado/valor en F1/A1 y se observan por separado en F2/A2; la regla conserva AST, owner, scope, operand bindings tipados y REQUIRE. PAR se mantiene como propiedad del CMP owner/registro de manifiesto; RUL se representa mediante PREDICATE; CMP por NODE anchor; REF solo por EDGE si se inventaría relación real; MET reutiliza metadatos/evidencia existentes. No se crean entidades ni columnas.

AB-01: binding AST→PAR DESIGN RESOLVED semánticamente; encoding, schema, escaping, canonicalización y constraints OPEN.

AB-02: crosswalk semántico reconciliado con DEC-C10-083 y U_G; mapping_id/version, mappings materiales por etapa, roster REF, snapshots/cobertura y evidencia OPEN. No se afirma REF=0 ni independencia técnica de A por igualdad semántica.

No hay IAM sellado, hash, parser, fixtures, implementación, simulación ni ejecución. scientific_execution=false; execution_authorized=false.


## 9. AB-06/07 — reconciliación integrada de secuencia D2 y dependencias de C_dep (2026-11-10)

**Estado:** reconciliación documental asistida sobre DEC-C10-066/067/094, el contrato de provisión B y el DAG/crosswalk temporal del maestro. No añade una decisión, no parametriza el DGP y no autoriza implementación o ejecución.

### 9.1 Secuencia causal y de eventos que ya está definida

| Orden | Evento/objeto | Dependencia o significado confirmado | Lo que NO permite inferir |
|---|---|---|---|
| t0 | Z: asignación de política D2 | Determina qué política B_g^D2 queda asignada. D2 es el candidato primario; D1 permanece secundario. | Z=1 no equivale a recepción, intento ni instalación; Z=0 no demuestra ausencia de provisión de fondo. |
| t1 | B_g^D2: política material | Control: no programa provisión focal. Tratamiento: programa provisión técnica focal de artefacto identificado/versionado. B provisiona; no ejecuta F1/F2/A1/A2 ni aplica la configuración. | B asignada/programada no demuestra que el actor reciba o inicie el intento, ni que la provisión tenga éxito. |
| t1 | W_programmed | Registro de que la política programó el intento. Las probabilidades candidatas deterministas de programación por brazo pertenecen al contrato D2, pero no convierten el evento en intento efectivo. | No equivale a W_attempt ni a cumplimiento. |
| t1 | Recepción / cumplimiento | Deben registrarse separadamente la recepción del artefacto/instrucción y el cumplimiento del protocolo. | No se consideran perfectos ni se derivan de Z o W_programmed. |
| t1 | W_attempt | Intento efectivamente iniciado, con actor, momento, artefacto y versión. | No implica instalación, integridad, compatibilidad, operabilidad ni accesibilidad. |
| t2 | S_install | Estado/evento de instalación técnica que debe quedar documentado, con versión/hash y evidencia temporal. | No es sinónimo del compuesto C_dep*, A_f*, D_f* ni éxito de la transformación funcional. |
| t2 | C_dep* | Predicado técnico compuesto: instalación ∧ integridad ∧ compatibilidad ∧ operabilidad, evaluado con evidencia por componente. | C_dep*=1 no implica A_f*=1: faltan los demás predicados constitutivos (ID, REL, COND, AUTH, RES, DEP y BLOCK). Tampoco implica F1/F2 ejecutadas. |
| t3 | A_f* y D_f* | A_f* evalúa la accesibilidad focal completa; D_f* es la apertura basal→post y exige inaccesibilidad focal basal. | No se infieren automáticamente de C_dep*, Z, B ni W. |
| t3 | T_acc*, ΔT_acc* | Resultado estructural de la evaluación completa de accesibilidad y su cambio; la evidencia/cobertura epistémica se registra separadamente en E_T. | No se sustituye por instalación, éxito técnico, ejecución, logs o cambios en observabilidad. |

**Regla temporal:** conservar por separado programación, recepción, intento, instalación y verificación de los cuatro componentes. Reintentos, fallos parciales, rollback, provisión de fondo, crossover y desviaciones se registran como eventos/historia, no se comprimen en un indicador binario de “éxito de B”.

### 9.2 Componentes de C_dep* y dependencias internas

| Componente | Contenido semántico mínimo | Evidencia material aún necesaria |
|---|---|---|
| INSTALLATION | El artefacto focal queda instalado en el entorno/unidad previstos y en la versión declarada. | Identidad del artefacto, actor, entorno, instante, estado final, hash/versión y registro de instalación. |
| INTEGRITY | El artefacto recibido/instalado conserva la integridad exigida respecto de la identidad declarada. | Fuente, firma/hash o mecanismo de integridad aceptado, resultado de verificación y cobertura. |
| COMPATIBILITY | El artefacto es compatible con el runtime, interfaz y condiciones técnicas declaradas para la unidad. | Versiones y restricciones de entorno/interfaz, matriz de compatibilidad y evidencia de comprobación. |
| OPERABILITY | El componente instalado puede iniciarse y operar técnicamente en el ámbito previsto, sin confundirlo con ejecutar la transformación funcional F1/F2. | Prueba/registro técnico de inicio y disponibilidad, ventana, errores y criterio de operabilidad predefinido. |

Las descripciones anteriores fijan el alcance semántico mínimo de los cuatro términos; no seleccionan herramientas, pruebas, umbrales, formatos, valores ni protocolos físicos. La aceptación de C_dep* como conjunción no implica que los cuatro componentes sean independientes ni que sus evidencias ya existan.

### 9.3 Distribución conjunta exigida y dependencias no resueltas

Para cada estrato/historia relevante h y brazo z, el DGP debe representar:

P(C_dep*=1 | Z=z, H=h) = P(I=1, G=1, C=1, O=1 | Z=z, H=h),

o una representación conjunta equivalente que preserve las 16 combinaciones posibles de los cuatro indicadores binarios. La distribución debe sumar uno y cada celda estar en [0,1]. Se informarán márgenes y dependencias condicionales; no se factorizará como producto de cuatro probabilidades marginales salvo que una justificación específica y verificable lo permita.

| Dimensión de parametrización | Estado |
|---|---|
| Cuatro componentes y regla AND | DESIGN RESOLVED |
| Unidad de condicionamiento por brazo e historia/estrato | DESIGN RESOLVED; roster concreto de estratos OPEN |
| 16 celdas conjuntas o equivalente validado | DESIGN RESOLVED |
| Probabilidades numéricas por celda | MATERIAL INPUT OPEN |
| Ceros estructurales y restricciones entre componentes | OPEN; no asumir |
| Dependencia entre recepción, intento, instalación y componentes | OPEN; requiere mecanismo/historia DGP explícitos |
| Heterogeneidad por historia, brazo, unidad o entorno | OPEN; depende de AB-08 y del soporte |
| Calibración empírica o estipulación sintética explícita | OPEN |
| Rangos/escenarios de sensibilidad y criterio de cobertura | OPEN |
| Provenance/versionado de parámetros | OPEN |

No se aprueban s=0.80, tasas históricas 0.20/0.80, cumplimiento perfecto, una única oportunidad, independencia de componentes ni probabilidades marginales como sustituto de la distribución conjunta. Los valores candidatos de programación D2 no rellenan los parámetros de recepción, intento o C_dep*.

### 9.4 Rutas colaterales y condiciones que deben permanecer comunes

El diseño aislado exige mantener comunes C_auth,base=1, elegibilidad, recursos no focales, capacidad, información técnica basal, configuración fuente/destino, F*, oráculo y condiciones constitutivas no focales. Cualquier cambio diferencial atribuible a B debe permanecer visible como vía colateral/cointervención, incluyendo:

- ACL/credenciales o autorización funcional; no confundirlas con permisos técnicos mínimos del adaptador;
- capacidad, recursos compartidos/reservados/consumidos y contención;
- dependencias transitivas, host, runtime, librerías, endpoint, red y seguridad;
- datos, configuración fuente/destino, mapping, aplicación o alteración de F*;
- estado de A1/A2, sus dependencias y su disponibilidad/equivalencia funcional;
- coste, riesgo, latencia, calidad, rendimiento o disponibilidad;
- información, formación, conocimiento y selección del agente;
- logs, observabilidad, cobertura, medición y adjudicación;
- rollback, residuos, carryover, crossover e interferencia entre unidades.

B-M01…15 y PROV-01…12 son superficies/contratos de inspección, no evidencia de invariancia. ARCH-B1 sigue siendo candidata para evaluar; MD-C1 y MD-C4 siguen abiertos. Si una vía colateral cambia, el ITT de Z conserva interpretación como efecto de política/paquete; no se transforma automáticamente en efecto puro de accesibilidad ni valida LATE_f.

### 9.5 Dictamen de cierre AB-06/07

- **Resuelto a nivel de diseño:** política D2 y sus roles; secuencia diferenciada de eventos; definición conjuntiva de C_dep*; exigencia de distribución conjunta condicional; separación C_dep*→A_f*→D_f*; catálogo de vías colaterales y regla de no inferencia.
- **Abierto como input material/evidencia:** actor, artefacto/hash, recepción, tiempos/ventanas, cumplimiento, reintentos, fallos parciales, rollback, provisión de fondo, evidencia por componente, estratos/historias, probabilidades conjuntas, calibración/sensibilidad, aislamiento de B y no-afectación A1/A2.
- **Handoff a C:** secuencia/eventos versionados, distribución conjunta con su incertidumbre, historial por brazo, soporte/estratos y clasificación de vías colaterales. Todo OPEN se transfiere como OPEN/UNKNOWN; C no lo rellena por defecto.

**Conclusión:** AB-06/07 quedan reconciliados en su arquitectura documental, pero no cerrados materialmente. AB continúa IN_PROGRESS; no hay Design Freeze, implementación, simulación ni ejecución autorizada.


## 10. AB-06/07 — estructura formal de parametrización D2 y C_dep* (2026-11-10)

**Naturaleza:** especificación matemática simbólica. No asigna probabilidades, valores, ceros estructurales, estratos ni parámetros físicos. No autoriza fixtures ni ejecución.

### 10.1 Secuencia D2: variables y mecanismo upstream

Para unidad i, brazo z e historia preasignación h0: Z=asignación; P=programación; R=recepción; Q=cumplimiento cuando sea distinguible; W=intento efectivo; S=instalación técnica; N=reintentos; K=fallos parciales, rollback, provisión de fondo, crossover y desviaciones.

La ley se representa mediante el kernel secuencial:

p(P,R,Q,W,S,N,K | Z=z,h0) =
p(P|z,h0) p(R|P,z,h0) p(Q|R,P,z,h0)
p(W|Q,R,P,z,h0) p(S|W,Q,R,P,z,h0)
p(N,K|S,W,Q,R,P,z,h0).

Es una factorización por regla de la cadena, no una hipótesis de independencia. Si Q no es un evento separable en el protocolo final, se documentará su absorción en R o W sin duplicarlo. La programación D2 no fija recepción, cumplimiento, intento ni instalación. Se permiten conceptualmente fallos, reintentos y provisión de fondo, sujetos a mecanismo y evidencia explícitos.

### 10.2 Vector C_dep* y orden canónico

Cuatro indicadores binarios para la misma unidad, snapshot, artefacto y ventana: I=INSTALLATION; G=INTEGRITY; C=COMPATIBILITY; O=OPERABILITY. Orden canónico: (I,G,C,O). En verdad DGP, 1=satisfecho y 0=no satisfecho; en observación se conserva además ?. C_dep*=I∧G∧C∧O. Solo 1111 da C_dep*=1; un 0 decisivo da 0; si no hay 0 decisivo y algún componente no es adjudicable, el compuesto es ?.

### 10.3 Roster de 16 celdas

Para cada combinación de brazo z e historia/estrato h, θ_{igco|z,h}=Pr(I=i,G=g,C=c,O=o | Z=z,H=h), con i,g,c,o∈{0,1}.

| Código | I | G | C | O | Interpretación |
|---|---:|---:|---:|---:|---|
| 0000 | 0 | 0 | 0 | 0 | Ninguno |
| 0001 | 0 | 0 | 0 | 1 | Solo operabilidad |
| 0010 | 0 | 0 | 1 | 0 | Solo compatibilidad |
| 0011 | 0 | 0 | 1 | 1 | Compatibilidad y operabilidad |
| 0100 | 0 | 1 | 0 | 0 | Solo integridad |
| 0101 | 0 | 1 | 0 | 1 | Integridad y operabilidad |
| 0110 | 0 | 1 | 1 | 0 | Integridad y compatibilidad |
| 0111 | 0 | 1 | 1 | 1 | Todo salvo instalación |
| 1000 | 1 | 0 | 0 | 0 | Solo instalación |
| 1001 | 1 | 0 | 0 | 1 | Instalación y operabilidad |
| 1010 | 1 | 0 | 1 | 0 | Instalación y compatibilidad |
| 1011 | 1 | 0 | 1 | 1 | Todo salvo integridad |
| 1100 | 1 | 1 | 0 | 0 | Instalación e integridad |
| 1101 | 1 | 1 | 0 | 1 | Todo salvo compatibilidad |
| 1110 | 1 | 1 | 1 | 0 | Todo salvo operabilidad |
| 1111 | 1 | 1 | 1 | 1 | C_dep*=1 |

Restricciones por cada z,h:
1. θ_{igco|z,h}≥0.
2. Σ_{i,g,c,o} θ_{igco|z,h}=1.
3. Pr(C_dep*=1|z,h)=θ_{1111|z,h}.
4. Pr(I=1|z,h)=Σ_{g,c,o}θ_{1gco|z,h}; los márgenes de G,C,O se obtienen análogamente.
5. Intersecciones y dependencias se calculan sumando las celdas correspondientes; no se sustituyen por productos de márgenes.
6. Una celda solo puede fijarse en cero con restricción constitutiva/material o estipulación sintética explícita, versionada y justificada. Falta de evidencia no crea cero estructural.
7. Combinaciones fuera de soporte se marcan como tales; no se extrapolan silenciosamente.

### 10.4 Condicionamiento y enlace upstream

H debe distinguir la historia relevante de programación, recepción, cumplimiento, intento, instalación, reintentos, fallos, rollback y provisión de fondo, además de C0 y modificadores pre-Z aceptados en AB-08. El roster operativo sigue OPEN y no puede redefinir elegibilidad post-Z.

La ley completa preservará la relación entre (P,R,Q,W,S,N,K) y (I,G,C,O); no se presume independencia entre intento/instalación y C_dep*. El evento S_install y el predicado I adjudicado no se igualan automáticamente: I puede depender de identidad, evidencia y ventana.

### 10.5 Familias de sensibilidad sin valores

- S0 referencia sintética: distribución conjunta explícita y versionada, aún sin baseline numérico aprobado.
- S1 dependencia positiva: componentes que tienden a satisfacerse conjuntamente, sin imponer independencia.
- S2 dependencia negativa/compensatoria: combinaciones mixtas y desacoplamiento.
- S3 cuello de botella: fallos concentrados en un componente necesario.
- S4 heterogeneidad: θ varía por brazo, historia, entorno o estrato dentro del soporte.
- S5 fallos de provisión: recepción/intento ausentes, tardíos, parciales o repetidos; rollback/no instalación.
- S6 provisión de fondo en control: intentos o instalaciones no focales registrados.
- S7 vías colaterales: cambios en recursos, permisos, dependencias, información, A1/A2, costes o medición.
- S8 evidencia incompleta: estados observados ?, cobertura diferencial y errores de medición/adjudicación.
- S9 interferencia/carryover: host, recursos, estado compartido, rollback o residuos temporales.

Cada escenario declarará truth DGP, parámetros modificados, invariantes, mecanismo afectado, observables y criterio de evaluación/falsificación. Las familias no presuponen identificación.

### 10.6 Inputs y gates

| Input | Estructura fijada | Material OPEN |
|---|---|---|
| P,R,Q,W,S,N,K | Kernel secuencial | Mecanismo, protocolo, probabilidades y evidencia |
| θ conjunta C_dep* | 16 celdas por z,h; simplex | Valores, soporte, estratos, restricciones y provenance |
| Ceros estructurales | Solo con justificación | Inventario de imposibilidades/estipulaciones |
| Sensibilidad | Familias S0–S9 | Rangos, amplitudes y criterio de suficiencia |
| Medición | Truth/observed y 1/0/? separados | Missingness, cobertura, oracle y adjudicación |
| Interferencia | No asumir independencia entre unidades | Cluster y mapa de exposición AB-08 |
| Vías colaterales | Registro obligatorio | Evidencia MD-C1/MD-C4 y no-afectación A1/A2 |

### 10.7 Dictamen

**Resuelto:** notación, orden de bits, 16 celdas, restricciones simplex, márgenes, kernel upstream y familias mínimas de sensibilidad.

**OPEN:** ley upstream y valores θ; definición operativa de H/estratos; ceros estructurales; soporte; dependencia; amplitudes de sensibilidad; calibración; medición/adjudicación; interferencia y aislamiento material de B.

No se declara parametrización numérica completa ni cierre AB-06/07. No se crean datos, fixtures ni simulaciones. scientific_execution=false; execution_authorized=false.


## 11. AB-07 — justificación semántica de dependencias entre los cuatro componentes de C_dep* (2026-11-10)

**Objeto:** reducir el espacio de parametrización solo donde la semántica y la frontera de medición impliquen restricciones lógicas. Esta sección no aprueba ceros estructurales empíricos ni una factorización probabilística.

### 11.1 Regla de análisis

Una dependencia solo se clasifica como **necesaria** si se deriva de las definiciones aceptadas y de compartir unidad, artefacto, entorno, snapshot y ventana. Una relación que dependa del protocolo, del entorno o de la implementación es **condicional al mecanismo**. Si ambas combinaciones son coherentes con las definiciones, la dependencia queda **libre en el DGP**. La asociación observada no basta para convertir una relación en necesidad lógica.

Antes de imponer cualquier restricción se debe comprobar que los predicados no duplican la misma propiedad ni usan ventanas/unidades distintas. Un cambio de unidad, artefacto, entorno o ventana invalida la implicación lógica salvo que se vuelva a justificar.

### 11.2 Dictamen por relación

| Relación | Dictamen | Justificación y límite |
|---|---|---|
| INSTALLATION → posibilidad de OPERABILITY | **Necesaria solo bajo definición acotada** | Si O significa inicio y operación técnica del mismo artefacto ya instalado, en el mismo entorno y ventana, O=1 implica I=1. No es una verdad universal si O admite ejecución efímera, remota, desde otro artefacto o fuera de la unidad de instalación. La definición operacional de O debe cerrar esa ambigüedad antes de imponer el cero estructural O=1,I=0. |
| COMPATIBILITY → OPERABILITY | **Condicional; no imponer implicación por defecto** | Si C es compatibilidad efectiva exhaustiva con el entorno/modos incluidos en la prueba O, O=1 puede implicar C=1. Si C es un dictamen ex ante, una matriz de soporte más amplia o una verificación independiente, puede observarse operación en un caso pese a C=0. Se requiere fijar alcance, modos y cobertura de ambas pruebas. |
| INTEGRITY → OPERABILITY | **No necesaria** | Un artefacto alterado o no autenticado puede arrancar y operar técnicamente; G=0 no impide por lógica O=1. Integridad es una condición de confianza/identidad, no necesariamente una condición física de arranque. Solo un contrato técnico concreto que bloquee la ejecución ante fallo de integridad podría imponer una dependencia condicional. |
| INTEGRITY → INSTALLATION | **No necesaria** | Un artefacto puede instalarse aunque su hash/firma no se verifique o falle la verificación posterior. G puede comprobarse antes, durante o después de S_install. El orden y el objeto de verificación deben fijarse; no convertir fallo de verificación en ausencia de instalación. |
| COMPATIBILITY → INSTALLATION | **No necesaria** | La instalación puede completarse en un entorno incompatible o sin evaluación previa de compatibilidad. Una política de despliegue que bloquee la instalación ante incompatibilidad generaría una restricción del mecanismo, no una necesidad semántica general. |
| INTEGRITY ↔ COMPATIBILITY | **Libre en el DGP** | Son propiedades distintas: identidad/conservación del artefacto y adecuación técnica al entorno. Puede existir cualquier combinación salvo restricción específica del artefacto/protocolo demostrada y versionada. |
| Dependencias entre I,G,C,O por causa común | **Condicionales** | Artefacto, runtime, entorno, agente, proveedor, política de verificación, fallos compartidos y condiciones de red pueden inducir asociación. Deben modelarse mediante historia/estratos o variables causales explícitas; no como independencia ni como restricción lógica automática. |

### 11.3 Restricciones admisibles en el roster de 16 celdas

1. **No se fija ahora ningún cero estructural** en θ_{igco|z,h}. La única candidata a restricción lógica es O=1 ⇒ I=1, y solo después de adoptar explícitamente la definición acotada de OPERABILITY de §11.2 y confirmar identidad de unidad/artefacto/entorno/ventana.
2. C=1 no se declara condición necesaria de O hasta que el contrato de COMPATIBILITY demuestre que cubre exactamente las condiciones y modos de OPERABILITY. G=1 no es condición necesaria de I ni de O por definición general.
3. La conjunción C_dep*=I∧G∧C∧O permanece inalterada. Una restricción en celdas del roster no altera el significado de cada componente ni autoriza eliminar componentes.
4. La factorización de θ en probabilidades condicionales podrá usarse como parametrización computacional de la distribución conjunta mediante la regla de la cadena, pero no como independencia. Cada condicional debe poder representar dependencias residuales y ceros justificados.
5. Una celda excluida debe registrar: regla semántica exacta, scope de unidad/artefacto/entorno/tiempo, contrato que la impone, versión, y evidencia de que no es solo ausencia de observación. Si la restricción es una estipulación sintética, identificarla como tal y someterla a escenario adversarial que la retire.

### 11.4 Implicaciones para el mecanismo D2 y la sensibilidad

- La secuencia upstream P/R/Q/W/S/N/K no determina por sí sola G,C,O: recepción e intento no garantizan integridad, compatibilidad ni operabilidad. S_install tampoco sustituye al predicado I adjudicado.
- La misma causa técnica puede afectar varios componentes; la distribución conjunta debe conservar esa dependencia. No se deben simular cuatro Bernoulli independientes como baseline por conveniencia.
- Mantener escenarios que separen fallos de provisión/instalación, corrupción o identidad, incompatibilidad ambiental y fallo de arranque/operación. Añadir contraste de sensibilidad para la posible implicación O⇒I: versión restringida solo si se cierra la definición, y versión no restringida como adversarial hasta entonces.
- No asignar magnitudes ni probabilidades a estos escenarios en esta fase. Las familias S0–S9 se conservan; la extensión solo precisa qué mecanismo altera cada escenario y qué restricción lógica se pone a prueba.
- Si se decide modelar C como condición necesaria de O o imponer O⇒I, la decisión debe preceder a la generación de fixtures y quedar registrada en el contrato semántico, no deducirse de resultados simulados.

### 11.5 Inputs que permanecen OPEN y criterio de cierre

**OPEN:** definición operacional de O (instalado/local/remoto/efímero; prueba y ventana); alcance de C (versiones, interfaces, modos y cobertura); objeto/momento de verificación de G; unidad común y snapshot; mecanismos de bloqueo por política; dependencias por historia/estrato; decisión explícita sobre O⇒I; parámetros conjuntos y sensibilidad.

**Cierre documental mínimo:** contratos de I/G/C/O con unidad, artefacto, entorno, snapshot, ventana, condición de verdad y evidencia; tabla de implicaciones revisada contra esos contratos; y roster θ actualizado solo con ceros demostrados o estipulaciones sintéticas identificadas. El cierre material exige además artefactos, protocolos, evidencias y cobertura; no se obtiene con esta especificación.

**Dictamen:** se descarta la independencia como supuesto por defecto. G y C no generan implicaciones lógicas generales entre sí ni con I/O. O⇒I es una implicación candidata dependiente de una definición operacional aún OPEN; C⇒O/O⇒C y las dependencias con G son condicionadas o libres. AB-07 queda más especificado conceptualmente, pero continúa OPEN en contrato operacional, parámetros, evidencia y sensibilidad. No hay Design Freeze, fixtures, implementación, simulación ni ejecución. scientific_execution=false; execution_authorized=false.


## 12. AB-07 — contrato mínimo de adjudicación para I/G/C/O y regla de admisibilidad de restricciones (2026-11-10)

**Propósito:** convertir el dictamen semántico de §11 en una plantilla verificable para cerrar los predicados sin decidir todavía un mecanismo tecnológico concreto ni asignar estados o probabilidades.

### 12.1 Contrato atómico obligatorio

Cada componente debe tener un contrato versionado con los siguientes campos. Un campo no aplicable debe marcarse explícitamente como N/A con justificación; no puede omitirse silenciosamente.

| Campo | Pregunta que debe resolver | Riesgo que evita |
|---|---|---|
| predicate_id / version | ¿Qué definición exacta se adjudica? | Deriva semántica entre escenarios |
| unit_id / unit_boundary | ¿Cuál es la unidad sobre la que se afirma 1/0? | Mezcla de unidad, agente, host o despliegue |
| artifact_id / artifact_hash | ¿Qué artefacto concreto se evalúa? | Sustitución por versión o artefacto distinto |
| environment_id / snapshot | ¿En qué entorno y snapshot? | Transferir resultados entre entornos |
| scope / modes | ¿Qué interfaces, modos y operaciones quedan cubiertos? | Confundir prueba parcial con cobertura exhaustiva |
| time_window / event_order | ¿Qué ventana y qué precedencias aplican? | Convertir orden de observación en causalidad |
| truth_rule | ¿Qué condición constitutiva hace verdadero el predicado? | Adjudicación circular o basada en proxy |
| evidence_rule | ¿Qué evidencia positiva y negativa basta? | Tratar ausencia de registro como 0 |
| unknown_rule | ¿Cuándo se asigna ? | Forzar 1/0 con cobertura incompleta |
| adjudicator / blinding | ¿Quién/qué adjudica y con qué cegamiento? | Sesgo diferencial entre brazos |
| failure_modes | ¿Qué fallos cuentan y cuáles no? | Colapsar fallo técnico, política y falta de evidencia |
| provenance | ¿Qué fuente, versión y hash respaldan el resultado? | Pérdida de trazabilidad |

### 12.2 Requisitos específicos por componente

- **I — INSTALLATION:** fijar si significa instalación material persistente del artefacto objetivo, en qué destino y bajo qué identidad. Distinguir evento S_install, estado instalado al cierre de ventana, instalación parcial, actualización, reinstalación y rollback. Un intento o evento de instalación no basta por sí solo para adjudicar I=1.
- **G — INTEGRITY:** fijar propiedad evaluada (identidad, integridad de contenido, firma/cadena de confianza u otra), objeto exacto y momento de verificación. Separar corrupción material, autenticidad no verificada, fallo del verificador y ausencia de evidencia; no equipararlos.
- **C — COMPATIBILITY:** fijar matriz de compatibilidad, versiones, interfaces, dependencias, modos y cobertura. Declarar si el juicio es ex ante o una prueba efectiva dentro del mismo entorno y ventana de O. Un resultado sobre una versión o modo no se extiende a otros sin regla explícita.
- **O — OPERABILITY:** fijar operación observada o demostrada, criterio de éxito, duración/estabilidad requerida, transacciones/modos cubiertos y si se permite operación efímera/remota. Precisar si el objeto debe ser el mismo artefacto instalado de I, en la misma unidad, entorno, snapshot y ventana.

### 12.3 Gate lógico antes de eliminar celdas θ

Una implicación X⇒Y solo será admisible cuando se cumplan conjuntamente:

1. X e Y comparten unidad, artefacto, entorno, snapshot y ventana relevantes, o el contrato demuestra formalmente cómo se enlazan;
2. la definición de X incluye necesariamente la condición constitutiva de Y (no solo una correlación o una política frecuente);
3. la regla de verdad y la evidencia permiten observar el caso contrario sin clasificarlo erróneamente como desconocido;
4. no existe ruta alternativa admitida por el contrato (ejecución remota, efímera, sustitución de artefacto, entorno distinto, etc.);
5. la implicación está escrita en el contrato versionado antes de generar fixtures y escenarios;
6. se conserva un escenario adversarial que retire la implicación cuando sea una estipulación del DGP y no una necesidad constitutiva.

**Aplicación actual:** O⇒I no pasa todavía el gate porque la definición de O y la correspondencia con I no están cerradas. C/O tampoco pasa el gate porque alcance y cobertura de C no están fijados. No se autoriza eliminar celdas del roster de 16. G no impone implicaciones generales sobre I, C u O.

### 12.4 Separación entre verdad, observación y mecanismo

Para cada unidad y componente se conservarán tres capas distintas:

- `truth_DGP`: estado que el mecanismo generador estipula;
- `observed_state`: 1/0/? según evidencia y cobertura;
- `mechanism_trace`: eventos, artefactos, versiones, entorno y fallos que explican cómo se produjo el estado.

No se adjudicará `observed_state=0` por ausencia de evento registrado si la cobertura no es exhaustiva. Tampoco se deducirá `truth_DGP` de un proxy observable. La concordancia truth/observed será evaluada posteriormente como parte del rendimiento del sistema de medición, no presupuesta.

### 12.5 Inputs y estado

**Resuelto a nivel de diseño:** campos mínimos del contrato; separación por componente; gate de implicación; separación truth/observed/mechanism; prohibición actual de ceros estructurales.

**OPEN:** contenido material de los cuatro contratos; unidad y artefacto; entorno/snapshot; ventanas; criterios de éxito; cobertura; protocolo de evidencia/adjudicación; versiones y hashes; definición de O; alcance de C; eventual regla O⇒I; distribución conjunta y sensibilidad.

**Dictamen:** AB-07 dispone ahora de una plantilla contractual y un gate de admisibilidad explícitos. Esto reduce ambigüedad documental, pero no cierra los contratos ni AB-07 materialmente. AB sigue IN_PROGRESS; no Design Freeze, fixtures, implementación, simulación ni ejecución. scientific_execution=false; execution_authorized=false.


## 13. AB-08 — algoritmo documental de elegibilidad, población objetivo y soporte (2026-11-10)

**Base histórica reutilizada:** maestro §§50.2–50.6 y 219.5–219.7; aceptación expresa AB-08-POP de §12; no se crea una tercera población ni se redefine q_X*. Esta sección operacionaliza el criterio aceptado sin introducir valores, pesos o tamaños muestrales.

### 13.1 Objetos que deben mantenerse separados

1. **P*_τ2:** población objetivo primaria para evaluar la apertura de accesibilidad de la transformación focal τ2. No exige ausencia de toda ruta funcional alternativa.
2. **P*_F:** subconjunto de P*_τ2 para el objetivo más restrictivo de apertura exclusiva de F*. Requiere ausencia respaldada de alternativas funcionalmente substituibles en el universo, granularidad, condiciones y horizonte aplicables.
3. **q_X*:** distribución objetivo, pre-Z y versionada de covariables/contextos X dentro de la población declarada. No es la regla de elegibilidad, no es una probabilidad de cumplimiento y no equivale a la distribución de C_dep*.
4. **Soporte común:** subconjunto de historias/estratos donde las políticas comparadas son ambas factibles y tienen probabilidad positiva bajo el mecanismo de asignación/provisión relevante.
5. **Muestra observada:** unidades efectivamente incorporadas y medidas. No redefine retrospectivamente P* ni q_X*.

### 13.2 Secuencia determinista pre-Z

El algoritmo documental de elegibilidad seguirá este orden, usando exclusivamente información disponible y congelada antes de Z y de cualquier programación B:

**Paso 0 — congelación:** fijar versión del protocolo, unidad de elegibilidad, instante pre-Z, catálogo de variables C0, snapshots, unidad de análisis prevista y población marco. Cada dato tendrá source/version/provenance y estado de cobertura.

**Paso 1 — condiciones constitutivas:** adjudicar cada condición constitutiva basal del sistema y la capacidad de evaluar ambas políticas. Resultado por condición: SATISFIED / NOT_SATISFIED / UNKNOWN. Una condición no satisfecha excluye según regla preespecificada; UNKNOWN no se convierte en falso ni en verdadero y deja elegibilidad indeterminada.

**Paso 2 — dependencia y accesibilidad focal basales:** adjudicar por protocolos independientes D_f,0 y A_f,0*. Para P*_τ2 se requiere D_f,0=0 y A_f,0*=0, ambos respaldados antes de Z. Discordancia entre ambos, o cualquiera UNKNOWN, no se resuelve por inferencia automática: pasa a auditoría o queda como elegibilidad indeterminada.

**Paso 3 — elegibilidad P*_τ2:** incluir solo unidades con condiciones constitutivas satisfechas, ambas políticas evaluables/factibles según C0, D_f,0=0 y A_f,0*=0, con evidencia/cobertura suficiente. La ruta alternativa basal F_alt,0 no es criterio de exclusión de P*_τ2; se registra como modificador/característica basal.

**Paso 4 — elegibilidad P*_F:** dentro de P*_τ2, adjudicar F_alt,0 sobre universo funcional cerrado, granularidad, condiciones y horizonte definidos. Incluir en P*_F únicamente si F_alt,0=0 está respaldado exhaustivamente. F_alt,0=1 excluye de P*_F, no de P*_τ2; F_alt,0=UNKNOWN mantiene pertenencia a P*_τ2 si los demás criterios se cumplen, pero no confirma P*_F.

**Paso 5 — congelación de q_X*:** definir X y la distribución objetivo q_X* sobre P*_τ2 (y, si procede, una distribución separada para P*_F), con regla y versión pre-Z. Sus pesos/proporciones requieren datos fuente o estipulación sintética expresa. No recalcular q_X* por brazo, recepción, intento, instalación, selección, ejecución, Outcome o Value.

**Paso 6 — soporte y positividad:** cruzar los estratos/historias con masa positiva bajo q_X* con la factibilidad de las dos políticas, la probabilidad de asignación y la posibilidad de observar los resultados requeridos. El soporte común se declara explícitamente. Una celda fuera de soporte no se extrapola; antes de Z se puede redefinir la población objetivo mediante regla explícita, o se conserva el objetivo y se informa que el contraste no está identificado en esa región. No se permite recortar después de observar resultados.

**Paso 7 — unidades e interferencia:** declarar separadamente unidad de asignación, unidad de análisis y unidad de interferencia. Si B, host, runtime, permisos, recursos o dependencias son compartidos, definir cluster o mapa de exposición/vecindad y registrar spillovers, crossover y carryover. La independencia individual no es un default.

### 13.3 Tabla de clasificación y datos desconocidos

| Condición basal | D_f,0 | A_f,0* | F_alt,0 | Resultado |
|---|---:|---:|---:|---|
| No satisfecha | cualquiera | cualquiera | cualquiera | Fuera de P*_τ2 y P*_F |
| UNKNOWN | cualquiera | cualquiera | cualquiera | Elegibilidad indeterminada |
| Satisfecha | 0 | 0 | 0 respaldado | P*_τ2 y P*_F |
| Satisfecha | 0 | 0 | 1 respaldado | P*_τ2; fuera de P*_F |
| Satisfecha | 0 | 0 | UNKNOWN | P*_τ2; P*_F no confirmado |
| Satisfecha | 1 | cualquiera | cualquiera | Fuera de población focal basal; discordancia con A_f,0* requiere auditoría |
| Satisfecha | cualquiera | 1 | cualquiera | Fuera de población de apertura basal; discordancia con D_f,0 requiere auditoría |
| Satisfecha | UNKNOWN | cualquiera | cualquiera | Elegibilidad P*_τ2 indeterminada |
| Satisfecha | cualquiera | UNKNOWN | cualquiera | Elegibilidad P*_τ2 indeterminada |

La tabla no sustituye el contrato de C0 ni los protocolos de medición de D_f,0, A_f,0* y F_alt,0. No se trata UNKNOWN como 0.

### 13.4 Soporte: dos niveles y límites

- **Soporte de asignación:** para cada estrato/historia relevante en q_X*, la asignación comparada debe tener probabilidad positiva bajo el diseño real. Aleatorización no se presume por la mera existencia de Z.
- **Soporte de políticas/mecanismos:** ambas políticas g0/g1 deben ser materialmente factibles y definidas en la misma historia/estrato. La disponibilidad teórica no basta si la política no puede implementarse en ese contexto.
- **Soporte de observación:** deben existir posibilidades no diferenciales o modelables de observar elegibilidad basal, estados técnicos y resultados. La falta de medición no se convierte en ausencia del fenómeno.
- **Soporte de transporte/estandarización:** q_X* solo puede asignar masa a estratos con soporte para el contraste que se pretende estandarizar. No se extrapola a regiones no observadas/no factibles.

Si se usa un estimando estandarizado, su dominio será el soporte común explícito. Cualquier cambio de dominio cambia la población/estimando y debe versionarse; no se presenta como el mismo efecto poblacional sin justificación.

### 13.5 Exclusiones, missingness y análisis

Todas las exclusiones deben registrar unit_id, criterio, valor basal, fuente, momento, estado de cobertura y versión de regla. La exclusión es anterior a Z. Las unidades UNKNOWN se conservan en el flujo de elegibilidad con su razón; no se borran del denominador de flujo. El análisis de sensibilidad a clasificación y missingness se transfiere a C, sin inventar tasas en AB.

No se excluye ni redefine la población por recepción, cumplimiento, intento, instalación, C_dep*, A_f, ΔT_acc, Reach, selección, ejecución, Outcome o Value post-Z. Estas variables pueden ser mediadores, resultados o mecanismos y su ajuste/exclusión requiere estimando causal explícito.

### 13.6 Inputs y dictamen

**Resuelto a nivel de diseño:** secuencia C0 pre-Z; criterios diferenciados P*_τ2/P*_F; rol no excluyente de F_alt,0 para P*_τ2; q_X* separado de elegibilidad y C_dep*; niveles de soporte; regla UNKNOWN; exclusión solo pre-Z; separación de unidades e interferencia.

**OPEN:** catálogo y contrato material de C0; unidad y población marco; protocolos y cobertura de D_f,0/A_f,0*/F_alt,0; definición de X y q_X* numérico; factibilidad por estrato de g0/g1; probabilidades de asignación; mapa real de clusters/exposición; missingness y tamaños muestrales (transferidos a C).

**Dictamen:** AB-08 tiene un algoritmo documental reproducible en principio y coherente con las reglas previamente aceptadas. No está materialmente cerrado: faltan la población y los datos/valores concretos, soporte, q_X*, topología e interferencia. AB permanece IN_PROGRESS; no Design Freeze, fixtures, implementación, simulación ni ejecución. scientific_execution=false; execution_authorized=false.


## 15. AB-09 — contrato integrado de escenarios R0–R3, truth tables y separación Generator/Analyzer/Evaluator (2026-11-10)

**Alcance y precedencia.** Esta sección integra, sin duplicar ni reemplazar, el contrato AB-09 de maestro §219.6, el contrato F* y alternativas de §57, la matriz temporal de predicados, las reglas trivalentes de §§1–13, la integración temporal de §14 de este ledger y el gate de generación de código del maestro §0.6. Reutiliza R0–R3, FSTAR-01…18, EXC/PM/IV, PM-01…18, B-M01…15 y PROV-01…12. No crea identificadores paralelos, no convierte escenarios candidatos en decisiones aceptadas y no acredita cobertura ni observación material.

### 15.1. Unidad de generación y estructura común de cada escenario

Cada réplica/unidad sintética debe declarar, antes de producir observaciones:

- `scenario_id` (R0, R1, R2 o R3, más identificador adversarial cuando corresponda), `dgp_version`, `unit_id`, `cluster_id/exposure_id` si aplica y versión de la instancia.
- Historia basal C0, brazo Z, versión de política D2, eventos P/R/Q/W/S/N/K y sus tiempos por nombre de evento. No traducir todavía estos nombres a índices temporales incompatibles: AB-TIME-01 sigue OPEN.
- Rutas `F=(F1,F2)` y `A=(A1,A2)`, universo U_G/alternativas, granularidad G, horizonte temporal H_time (OPEN), profundidad H_path (no confundir con H_time), F*, restricciones, recursos y cobertura.
- Truth DGP por predicado y etapa; eventos/mecanismo; proceso de observación; missingness/cobertura; y resultado que se entrega al Analyzer.
- Regla de evaluación y falsador específico. Los valores no determinados por las DEC o por contratos aceptados permanecen como parámetros explícitos OPEN, no como defaults.

La unidad de adjudicación mínima es `unit × scenario × route × step × predicate × snapshot/event`. Las tablas de escenario son reglas de verdad estipuladas por DGP, no observaciones empíricas ni probabilidades.

### 15.2. Matriz integrada de verdad esperada R0–R3

| Objeto/predicado | R0 — focal aislado | R1 — alternativa basal estable | R2 — vía colateral de B | R3 — intento sin C_dep* completo |
|---|---|---|---|---|
| `F_alt,0` | 0 solo si el universo declarado está cerrado y exhaustivamente cubierto; en otro caso ? | 1 si A satisface F* con evidencia y cobertura basales; no excluir de P*_τ2 | Baseline se adjudica pre-Z; después se registra si B altera la alternativa. No inferir estado post-Z desde el basal | Se adjudica independientemente; no se deduce del intento |
| Relación B→A1/A2/recursos/permisos/calidad/Outcome/Value | Truth del DGP estipula no-afectación en las superficies incluidas; no equivale a prueba material MD-C1/MD-C4 | La alternativa basal permanece estable y no afectada por B en la versión canónica R1; cualquier cambio reclasifica el caso como vía colateral/adversarial | Existe al menos una vía colateral estipulada y localizada; identificar superficie, tiempo y consecuencia | No se presupone aislamiento por el hecho de que el intento falle |
| `W_programmed`, `W_attempt`, `S_install` | Se generan conforme a la política D2 y al mecanismo de cumplimiento; no se fuerza cumplimiento perfecto | Igual que R0; la alternativa no sustituye ni determina los eventos focales | Igual, registrando además cambios de B fuera de la ruta focal | Puede haber intento efectivo; no equivale a recepción, instalación ni éxito |
| `C_dep* = I∧G∧C∧O` | Se deriva de cuatro verdades component-wise; no se presupone que sea 1 por Z=1 | Igual; éxito técnico focal y alternativa funcional son objetos distintos | Igual; registrar dependencias inducidas por las vías colaterales | El caso definitorio incluye al menos un componente constitutivo en 0 en truth DGP para afirmar `C_dep*=0`; si solo falta evidencia, `observed_state=?`, no 0 |
| `A_f*`, `D_f*`, `ΔT_acc*` | Se adjudican independientemente a partir de condiciones/rutas del sistema. Z, programación, intento o C_dep* no los sustituyen | La accesibilidad focal puede cambiar aunque F* ya sea alcanzable por A; no inferir que ΔT_acc*=0 ni que Reach/F* cambie | Se registran los cambios reales de estructura/accesibilidad, incluidos los causados por rutas no focales; no atribuirlos exclusivamente a la intervención focal | No inferir A_f*=0/1, D_f* ni ΔT_acc* desde el intento o desde C_dep* incompleto; adjudicar alternativas y provisión de fondo |
| `Reach_H`, `F*`, rutas | Reach/F* se evalúan sobre universo y horizonte declarados; R0 no demuestra ausencia fuera del universo | La ruta A puede sostener F*/Reach aunque cambie la accesibilidad de τ2; identidad y substituibilidad permanecen separadas | Reach/F* incorporan la vía afectada; el efecto puede ser de paquete | Una ruta alternativa o provisión de fondo puede mantener Reach/A_f* pese al fallo técnico focal |
| Interpretación de ITT | Efecto de asignación D2 bajo la verdad de aislamiento estipulada en R0; no demuestra exclusión empírica | ITT de política; la alternativa estable puede ser modificadora de efecto, no violación automática de exclusión | Efecto de política/paquete; no etiquetar como efecto exclusivo de ΔT_acc* | Efecto de política D2; no inferir primer estadio de accesibilidad a partir de intento/instalación |
| Estado de identificación focal | Candidato a aislamiento en el DGP; identificación solo tras satisfacer los demás requisitos de C | No se presume exclusividad funcional; P*_F separada de P*_τ2 | Exclusión focal comprometida por construcción salvo diseño adicional que separe la vía | La primera etapa técnica incompleta no identifica el efecto mediado por accesibilidad |

**Regla de consistencia:** R0–R3 no asignan por sí solos magnitudes de Outcome/Value, probabilidades de cumplimiento, θ conjunta, pesos q_X*, H_time, potencia o tasas de error. Cada uno pertenece a su contrato/gate específico. Un DGP puede fijar verdad distinta por unidad/historia; la tabla expresa únicamente las propiedades que definen cada familia.

### 15.3. Estados de verdad, observación y cobertura

Para cada predicado se conservarán al menos estos campos, enlazados por identificadores opacos:

1. `truth_DGP ∈ {1,0}`: valor estipulado por el mecanismo generador para la unidad/etapa/versión.
2. `observed_state ∈ {1,0,?}`: juicio derivado exclusivamente de datos observables y protocolo de adjudicación.
3. `measurement_status`: estado del proceso de medición (incluye fallo, no aplicación, censura o adjudicación pendiente sin colapsarlos).
4. `coverage`: alcance verificable de universo, pasos, modos, snapshots y ventana.
5. `mechanism_trace`: eventos y dependencias que producen la verdad DGP.
6. `adjudication_ref`: regla, versión, evaluador y evidencia que sustentan el observado.

Reglas obligatorias:

- Truth DGP es binaria para predicados constitutivos definidos; UNKNOWN es un estado epistémico/observacional, no un tercer valor físico añadido al DGP.
- `observed_state=1` requiere evidencia positiva suficiente y correspondencia de identidad/unidad/versión/ventana.
- `observed_state=0` requiere evidencia negativa y cobertura suficiente para descartar el predicado dentro del universo declarado.
- `observed_state=?` se mantiene ante cobertura incompleta, missingness, censura, desacuerdo no resuelto, identidad/mapping inciertos o prueba insuficiente.
- `F_alt=0` y `Reach=0` requieren universo cerrado y búsqueda/cobertura exhaustiva. “No encontrado” o una lista vacía no son prueba de inexistencia.
- Un predicado de ruta completa es 1 solo si todos sus requisitos necesarios son 1; es 0 si algún requisito necesario es 0; en otro caso ?. Reach es 1 si existe una ruta completa respaldada; es 0 solo si todas las rutas del universo están descartadas con cobertura exhaustiva; en otro caso ?.
- La conjunción `C_dep*=I∧G∧C∧O` conserva la regla existente: truth es 1 solo en 1111; truth es 0 si algún componente es 0; observed es ? si no hay cero observado decisivo y queda algún componente desconocido.
- No imputar truth desde observed, ni observed desde truth; no utilizar el identificador/etiqueta del escenario como predictor observable.

### 15.4. Contrato de separación Generator / Analyzer / Evaluator

| Rol | Acceso permitido | Acceso prohibido | Salida/control |
|---|---|---|---|
| **Generator** | DGP versionado, truth, potenciales, políticas, semillas internas, mecanismo y parámetros | Ninguna restricción de acceso interno dentro de su espacio privado; no puede escribir truth en el canal observable salvo que sea una variable legítimamente observable | Emite eventos y dataset observable separado; conserva truth y provenance en almacén/canal privado |
| **Analyzer** | Dataset observable permitido, covariables basales, Z observado cuando forme parte del diseño/dataset, historial/eventos medidos, documentación pública del protocolo y reglas analíticas | `truth_DGP`, resultados potenciales, seed/estado interno del generador, asignación oculta no observada, `scenario_id`/etiquetas que revelen la familia de verdad, parámetros generadores privados, claves o nombres que permitan reconstruirlos | Emite estimandos, clasificaciones, bounds, incertidumbre y abstenciones; congela outputs antes de cualquier acceso evaluativo |
| **Evaluator** | Outputs congelados del Analyzer, truth sellada, potenciales y metadatos de escenario necesarios para puntuar | No puede corregir retrospectivamente el Analyzer ni cambiar el output congelado; no puede convertir un PASS de software en validación científica | Calcula recuperación, error, cobertura, falsa identificación, falsa atribución, abstención y concordancia truth/observed |

El valor Z efectivamente asignado puede estar disponible al Analyzer como dato observado del diseño; lo que permanece oculto es el estado interno/semilla de aleatorización, las asignaciones potenciales/contrafactuales y cualquier etiqueta que revele truth. La distinción evita confundir el cegamiento a la verdad del DGP con ocultar una covariable observada necesaria para estimar ITT.

**Firewall mínimo:** canales/artefactos separados; IDs opacos no semánticos; validación de esquema que rechace campos privados; control de acceso; hash/versionado; log de acceso; prueba negativa de no-leakage; congelación inmutable de la salida Analyzer antes de abrir truth al Evaluator. Un simple cambio de nombre de columnas no demuestra separación.

### 15.5. Adversariales y falsadores reutilizados

Se reutilizan, sin duplicar IDs, las familias ya registradas: provisión de fondo/crossover; recepción o cumplimiento parcial; fallos parciales/reintentos/rollback; conocimiento/formación diferencial; medición/oráculo diferencial; truth leakage; pérdida/censura; recurso/host compartido; modificación de A1/A2; vía directa a Outcome/Value; interferencia y carryover.

| Familia adversarial existente | Inyección de verdad del DGP | Falsador/resultado que debe detectar el procedimiento |
|---|---|---|
| Provisión de fondo/crossover | Acceso focal también en control o cruce entre políticas | No atribuir la diferencia de primera etapa solo a Z; registrar exposición/versiones y degradar la interpretación focal |
| Fallo/reintento/rollback | Secuencia parcial con reintentos o reversión | No colapsar intento, instalación, C_dep y accesibilidad; conservar orden y estado final |
| Vía colateral (R2) | B modifica A1/A2, permisos, recursos, calidad, coste, latencia u Outcome/Value | Clasificar efecto como política/paquete o declarar no identificada la atribución focal |
| Medición/oráculo diferencial | La observabilidad/cobertura/adjudicación varía por brazo | Detectar missingness/error diferencial; no interpretar cambio observado como cambio estructural |
| Truth leakage | Se filtra escenario, truth, potenciales o seed al Analyzer | Fallo del firewall; salida Analyzer no admisible para evaluación confirmatoria |
| Censura/pérdida | Resultado o ruta no observable en parte de la ventana | Propagar ?/censura; no declarar ausencia ni éxito |
| Interferencia/carryover | Recursos/host compartidos o residuo tras rollback | Detectar unidad de exposición/cluster inadecuada; limitar el estimando individual |
| Alternativa estable (R1) | A satisface F* antes/después sin ser afectada por B | No confundir modificación de accesibilidad focal con apertura funcional exclusiva ni declarar violación IV automática |
| Intento sin éxito técnico (R3) | W_attempt=1 con C_dep* truth=0 | No inferir A_f*, D_f* o ΔT_acc* desde el intento |

Los falsadores son condiciones de clasificación metodológica, no resultados ya observados ni tests ejecutados.

### 15.6. Criterios de aceptación AB-09 y transferencia a C

AB-09 solo podrá pasar a DESIGN COMPLETE cuando:

1. R0–R3 tengan DGP versionado, reglas generadoras, invariantes declaradas y truth tables completas por predicado/etapa, incluyendo los campos N/A justificados.
2. Las reglas de observación/missingness, cobertura, adjudicación y UNKNOWN estén enlazadas a los contratos existentes y no creen otra matriz paralela.
3. F_alt, Reach, F* y C_dep respeten las reglas de universo cerrado, composición y trivalencia.
4. El Generator/Analyzer/Evaluator firewall tenga interfaces, artefactos, controles negativos y criterios de fallo verificables; no basta una declaración textual de separación.
5. Los adversariales reutilizados tengan un resultado esperado y un falsador inequívoco, sin asumir tasas o magnitudes.
6. Las interfaces de C distingan ITT_Z^D2, efecto de paquete, primeras etapas C_dep/A_f/D_f/ΔT_acc, LATE_f, θ_Af(q_X*) y θ_A(q), sin convertir una en proxy de otra.

**Inputs que siguen OPEN:** universo U_G realmente cerrado y cobertura; C0/F*/G/H_time; protocolo/oráculo y cegamiento; mapping y observación por campo/etapa; missingness y error de clasificación; mecanismo material D2 y distribución conjunta C_dep; población/q_X*/soporte/interferencia; parámetros de Outcome/Value; tolerancias y criterios cuantitativos de evaluación que corresponden al paquete C.

**Dictamen:** R0–R3, sus propiedades distintivas y el firewall quedan reconciliados a nivel contractual/documental. AB-09 pasa a DESIGN SPECIFIED / INTEGRATION RECONCILED, pero NO a DESIGN COMPLETE ni materialmente cerrado. No se rellenan truth tables unitarias con valores no derivados, no se generan fixtures, no se implementa, simula ni ejecuta. No Design Freeze; `scientific_execution=false`; `execution_authorized=false`.


## 16. AB-01…AB-09 — matriz integrada de dependencias, bloqueos y transferencia parcial AB→C (2026-11-10)

**Propósito.** Consolidar el estado real de AB tras §§8–15 y relacionarlo con los contratos C existentes en maestro §§221–229. Esta matriz no sustituye la tabla de gates §2, el registro de inputs §4 ni el contrato de transferencia §5; los hace operativamente legibles y evita declarar AB cerrado por completar especificaciones documentales o bloquear C por inputs que pueden permanecer OPEN.

### 16.1. Dependencias entre gates y orden de cierre

| Gate | Depende de | Habilita principalmente | Estado actual | Bloqueo material dominante |
|---|---|---|---|---|
| AB-01 | DEC/AST/roster CMP-PAR-RUL-MET y snapshots | Identidad de instancia, operandos, mappings | Semántica reconciliada; encoding físico OPEN | Schema/serialización, IAM instanciado, snapshots y cobertura |
| AB-02 | AB-01 + estados y mapping aceptados | C_src/C_dst/M y error/UNKNOWN de configuración | Crosswalk semántico reconciliado | Schema físico, namespaces, payload y mapping efectivo |
| AB-03 | AB-01/02 + contratos de rutas | Identidad y comparabilidad F1/F2/A1/A2 | Cards sintéticas abstractas especificadas | TID/SID/RID completos, mecanismos, versiones, pre/postcondiciones y eventos |
| AB-04 | AB-01/02/03 + matriz de predicados | A_f*, D_f*, ΔT_acc* y rutas con medición independiente | Crosswalk semántico definido parcialmente | Roster de campos, fuentes, captura, cobertura y adjudicación por unidad/etapa/snapshot |
| AB-05 | AB-03/04 + F* común | Función terminal, C0/G y medición temporal común | Reglas funcionales definidas; input temporal incompleto | H_time/H*, C0 concreto, G instanciado, FP profile y oráculo validado |
| AB-06 | AB-01…05 + política D2 | Historia de asignación/recepción/intento/instalación | Secuencia y kernel simbólico definidos | Artefactos/actores, timestamps, cumplimiento, fallos, rollback y provisión de fondo |
| AB-07 | AB-06 + contratos I/G/C/O | Distribución conjunta C_dep* y sensibilidad | Estructura de 16 celdas y reglas de dependencia definidas | θ numérica, soporte por historia/estrato, ceros justificados y calibración/sensibilidad |
| AB-08 | AB-01…07 + C0 | Población, q_X*, positividad y unidad de inferencia | Regla pre-Z y distinciones poblacionales especificadas | Población marco, C0 efectivo, q_X*, soporte, pesos/estratos y topología de interferencia |
| AB-09 | AB-03…08 + universo G/H + oráculo | R0–R3, truth/observed, evaluación sellada | Contrato de escenarios y firewall documental reconciliado | Universo alternativo cerrado, truth tables instanciadas, observación/missingness, oráculo y prueba técnica de no-leakage |

**Lectura del grafo:** AB no es una cadena estrictamente lineal. AB-01/02 y parte de AB-03/04 son contratos semánticos que pueden estabilizarse en paralelo; AB-05 aporta el marco común; AB-06/07 forman el bloque de mecanismo técnico; AB-08 define población/soporte/unidad; AB-09 integra escenarios, universo, observación y cegamiento. AB-09 no puede materializarse plenamente antes de instanciar sus inputs, aunque su contrato abstracto ya esté especificado.

### 16.2. Clasificación de los once inputs residuales

| Input | Estado reconciliado | Dependencias principales | ¿Transferible a C ahora? |
|---|---|---|---|
| AB-M01 | Semántica AST tipada a PAR resuelta; encoding físico OPEN | AB-01/02 | Sí, como regla semántica; no como schema físico |
| AB-M02 | Crosswalk BOOL/ENUM y mapping lógico resueltos; payload/schema/canonicalización OPEN | AB-01/02 | Sí, con OPEN explícito y sin extrapolar JCS |
| AB-M03 | Roles conceptuales de cuatro cards y composición definidos; TID/SID/RID/materialización OPEN | AB-03/05 | Sí, como contrato abstracto, no como identidad ejecutable |
| AB-M04 | Crosswalk semántico de predicados/campos definido parcialmente; fuentes y cobertura OPEN | AB-04/05/09 | Sí, como diccionario provisional y reglas UNKNOWN |
| AB-M05 | F*/C0/G estructurados; H_time/H* y unidad OPEN | AB-05/09 | Solo límites y requisitos; no horizonte operativo |
| AB-M06 | Vías colaterales y superficies de inspección inventariadas; MD-C1/MD-C4 no demostradas | AB-04/06/09 | Sí, como amenazas/hipótesis; no como evidencia de aislamiento |
| AB-M07 | Secuencia D2, kernel y roster θ definidos simbólicamente; probabilidades OPEN | AB-06/07 | Sí, como estructura; no como distribución parametrizada |
| AB-M08 | Elegibilidad pre-Z y P*_τ2/P*_F/q_X* diferenciados; población/soporte OPEN | AB-08 | Sí, como reglas; no como población/pesos efectivos |
| AB-M09 | Principio de unidades e interferencia definido; topología OPEN | AB-08 | Sí, como requisito; no como estructura de clúster/exposición |
| AB-M10 | Requisitos de independencia/oráculo/cegamiento definidos; validación y adjudicación OPEN | AB-05/09 | Sí, como contrato y gate; no como oráculo validado |
| AB-M11 | R0–R3, trivalencia y firewall definidos documentalmente; truth por unidad, missingness y no-leakage técnico OPEN | AB-09 | Sí, como contrato; no como verdad instanciada ni prueba superada |

### 16.3. Handoff AB→C: qué se puede consumir y qué no

**Transferible ahora, con versión y estado:** identidad semántica CMP/PAR/RUL/MET; regla AST→PAR sin doble conteo REF; crosswalk lógico de estados y mapping; composición conceptual F/A; definiciones y separaciones C_dep*/A_f*/D_f*/ΔT_acc*/F*/Reach; secuencia de eventos D2 y kernel simbólico; roster conjunto I/G/C/O de 16 estados; regla de elegibilidad pre-Z; separación P*_τ2/P*_F/q_X*; reglas de soporte y UNKNOWN; familias de vías colaterales; definiciones R0–R3; contrato truth/observed y frontera Generator/Analyzer/Evaluator.

**No transferible como valor resuelto:** schema físico/mappings instanciados, TID/SID/RID efectivos, C0/G/H_time, universo U_G y cobertura, valores de predicados y fuentes, evidencia MD-C1/MD-C4, eventos/timestamps y probabilidades D2, θ conjunta, población marco/q_X*/pesos/soporte, topología de clúster/exposición, oráculo validado, truth tables por unidad y modelo de missingness.

**Regla de C:** los contratos transferibles pueden usarse para especificar estimandos, escenarios de identificación, sensibilidad simbólica, bounds y reglas de abstención. Todo input no resuelto conserva ID AB-Mxx, procedencia, alcance y estado OPEN/UNKNOWN. No convertir un parámetro simbólico en valor numérico ni declarar identificación puntual por conveniencia.

### 16.4. Correspondencia con los contratos del paquete C

| Contrato C existente | Inputs AB requeridos | Estado de dependencia |
|---|---|---|
| §221 — interfaz AB→C y jerarquía de estimandos | AB-01…09 | Interfaz y jerarquía transferibles; parámetros/materialización OPEN |
| §§222–223 — estimandos, identificación y jerarquía confirmatoria | AB-04…09 + C10-D1 | Puede continuar especificación; identificación depende de soporte, DAG, intervención y medición |
| §224 — Outcome/Value y adjudicación | AB-04/05/09 + decisión propia de C | No bloqueado por completar todo AB; requiere definición independiente de dimensiones, unidad, escala y protocolo Outcome/Value |
| §225 — identificación, sensibilidad, bounds, evaluación y potencia | AB-06…09 + C10-D1 + §224 | Estructura metodológica existente; parametrización, mediación y umbrales OPEN |
| §§227–229 — crosswalk P177–P183, C-MED y C-ANALYZER | AB-05…09 | Auditoría/candidatos disponibles; mediación y métricas de falsa atribución/abstención con cobertura contractual parcial |

§221 es un contrato de handoff, no prueba de AB cerrado. §225 sigue siendo propuesta documentada no aprobada/no congelada; §§228–229 mantienen C-MED y C-ANALYZER parcialmente especificados.

### 16.5. Bloqueos reales y secuencia mínima recomendada

1. **Medición/identidad:** AB-M03/04/05/10 — identidades, campos, F*, C0/G/H_time y oráculo. Sin esto no se declaran medidos A_f*, D_f* ni ΔT_acc* ni comparabilidad temporal.
2. **Mecanismo/primeras etapas:** AB-M06/07 — separación de rutas colaterales, eventos D2 y distribución conjunta C_dep*. Sin esto no hay primera etapa técnica/focal parametrizada ni atribución exclusiva.
3. **Población/identificación:** AB-M08/09 — población, q_X*, soporte e interferencia. Sin esto no se define transporte ni identificación poblacional.
4. **Evaluación sellada:** AB-M11 + AB-M10 — truth por unidad, observación/missingness y prueba técnica del firewall. Sin esto no se puntúa recuperación ni falsa atribución del Analyzer.

**Orden operativo mínimo:** (a) preparar el registro de campos/artefactos/decisiones requeridas para M03/04/05/10 sin rellenar datos ausentes; (b) definir ficha de evidencia material MD-C1/MD-C4 y captura de eventos D2; (c) obtener o estipular explícitamente, con procedencia, C0/población/soporte/interferencia y θ; (d) instanciar R0–R3 y proceso de observación; (e) completar C-MED/C-ANALYZER y gates estadísticos con P177–P183; (f) revisar coherencia integral antes de proponer Design Freeze. No autoriza implementación ni ejecución.

### 16.6. Dictamen

AB-01…AB-09 están reconciliados a nivel de arquitectura documental en distintos grados, pero AB permanece **IN_PROGRESS / MATERIAL INPUTS OPEN / NOT DESIGN FROZEN / NOT IMPLEMENTABLE**. AB-01 semántico está resuelto; AB-02 tiene crosswalk semántico; AB-03/04 están especificados a nivel abstracto/semántico; AB-06/07 tienen estructura causal/simbólica; AB-08 tiene regla poblacional; AB-09 tiene contrato de escenarios y firewall. Ninguno equivale a evidencia material completa.

El paquete C puede avanzar documentalmente sobre §§221–229, consumiendo los elementos transferibles y manteniendo los demás OPEN. No se autoriza Design Freeze, implementación, simulación ni experimento. scientific_execution=false; execution_authorized=false.


## 17. C-MED — ficha de estimando interventional y gates de identificación (2026-11-10)

Se registra la especialización candidata del maestro §249, sin cambiar la jerarquía ni declarar MED-03/05 cerrados.

**Separación obligatoria:** (i) ITT de asignación Z a D2; (ii) efecto del régimen material recibido B; (iii) efecto interventional mediado por la distribución conjunta y factible M=ΔT_acc*; (iv) pregunta primaria C10-D1 θ_A(q) sobre políticas factibles bajo régimen común q. No son estimandos intercambiables. La aleatorización Z no identifica por sí sola B, M→Value ni la mediación.

Se define historia basal H, confusores/estados post-B pre-M L y mediador conjunto M. Si L afecta M y Value y está inducido por B, existe confusión mediador–resultado inducida por tratamiento; requiere DAG longitudinal y método g compatible, no ajuste convencional como si L fuera basal.

Estimando candidato con referencia b1:
IIE_M,j^(b1)(b1,b0;q)=E_q[V_j^(b1,G_M^b1)−V_j^(b1,G_M^b0)],
donde G_M^b(dm|L,H) es la distribución conjunta factible de M bajo b condicionada por la historia pre-M. La referencia y el orden forman parte del estimando; el mediador no se factoriza. El término complementario solo puede definirse con la misma q, escala, horizonte y régimen; no se llama efecto directo puro porque contiene vías restantes, incluidas L y rutas colaterales.

**No identificación:** historia L incompleta, confusión M–V no medida, falta de soporte secuencial, intervención M no factible, versiones incompatibles, interferencia no modelada o medición inválida obligan a NOT_IDENTIFIED/PARTIALLY_IDENTIFIED/INDETERMINATE según lo que pueda sostenerse. Un ITT identificable no implica mediación identificada; una mediación identificada bajo D2 no identifica automáticamente θ_A(q).

**Estado:** especificación candidata; MED-03 y MED-05 siguen OPEN; ningún supuesto ni estimando está validado empíricamente. Sin Design Freeze ni ejecución científica.


## 18. C-MED — registro causal H/L/M y rutas a Outcome/Value (2026-11-10)

Se operacionaliza el DAG existente de maestro §§229.3, 233 y 249 en un registro conceptual, sin crear una segunda matriz de predicados ni declarar inventario de campos completo.

**H basal:** roster ya presente X/H0/S0/C0/L0, unidad/frontera/soporte, identidades/versiones, C_auth,base, recursos0/capacidad0/información0, C_dep0, A_f,base*, T_acc,base, alternativas0, O0/V0. Sus valores, población y medición siguen OPEN.

**Z y exposición:** Z es asignación; B y su versión son régimen material; W_programmed, recepción/cumplimiento, W_attempt y S_install son eventos separados, no proxies intercambiables.

**L post-B pre-M candidata:** C_install*/C_integrity*/C_compat*/C_oper*, C_dep*, recursos/capacidad/permisos/ACL/dependencias/host/runtime/seguridad y cambios de entorno. Solo es confusor M–V inducido para un estimando/dimensión si B la afecta y causa tanto M como V_j por ruta pertinente. Puede ser causa de M, mediador técnico o colateral según el DAG; no etiquetar automáticamente todo postratamiento como confusor.

**M:** ΔT_acc* completo en t3, con componentes DGP y mapping/crosswalk de §30. A_f* es proyección/predicado focal y D_f* indicador; no son mediadores paralelos por defecto. E_T es canal de evidencia/observación y no parte de M.

**Downstream:** Reach/Π_H, K/Consider, Sel/Start, ejecución y O preceden a V_j según el reloj existente; forman parte de la evolución del efecto total y solo se separan con estimandos secuenciales propios. Cambios posteriores que alteren accesibilidad exigen nuevo snapshot.

Se registran rutas candidatas B→L→M→downstream→O→V, B→L→O/V, B→A1/A2/recursos/ACL/coste/seguridad→O/V, B/Z→E_T/missingness→observados e interferencia/carryover entre unidades. Son rutas a auditar, no flechas empíricamente demostradas. Sin definición de §224 por dimensión V_j no se adjudican efectos específicos.

**Regla de ficha:** reutilizar field_id existentes y registrar tiempo/valid-time, unidad/frontera, snapshot/versión, función U*/R*/C*/X*/E_T, truth/observed, papel causal relativo al estimando y V_j, relación con M y Outcome/Value, fuentes/cobertura/error, intervención, interferencia y provenance. Un mismo campo no se duplica en L y M; separar instancias temporales cuando proceda.

**Estado:** registro conceptual consolidado; inventario material y clasificación campo×V_j OPEN. No identifica confusores efectivos ni demuestra ausencia de rutas. MED-03/05 y §224 siguen OPEN. Sin Design Freeze ni ejecución.


## 19. MED-02c — crosswalk campo/subcampo del roster Opción A (2026-11-10)

Se descompone el roster documental de §232 a nivel de subcampo sin crear identificadores ni datos de instancia. Se han tipado condicionalmente: F1/τ2, F2, A1/A2 y TID/SID/RID como U*/identidad; adaptadores, endpoints y llamadas como R* o U* según función; contract/instance/component IDs como CMP/MET; ENABLED/PROFILE y RUL-SVC-ENABLE-PROFILE-01 como PAR/C*; RETRY-COUNT como slot candidato no nuclear; runtime/host/deployment como X* solo si constitutivo, con reglas como C* y hashes como E_T; recursos como C* o X* según disponibilidad/contexto; C_auth,base separado de ACL técnica; DNS/proxy/rutas como R*, firewall/bloqueos como C*; configuración/datos descompuestos en CMP/PAR/REF/RUL/C*; seguridad como C* o X* según función; estado persistente como X*/C*/U*/R* según función; logs/telemetría/oráculo como E_T; rendimiento fuera de M salvo regla de accesibilidad preespecificada; alternativas A1/A2 como U*/R* con no-afectación pendiente.

La tabla detallada y sus reglas quedan en maestro §251. No se han asignado field_id/event_id ni valores. Se conserva AB-TIME-01: usar nombres de eventos, timestamps fuente y snapshot, sin armonizar índices t por inferencia. NO INVENTARIADO/UNKNOWN/? no equivalen a cero. El papel de L como confusor inducido depende de B→L, L→M y L→V_j para estimando/horizonte concretos.

**Dictamen:** crosswalk documental de subcampos completado parcialmente sobre el roster existente; MED-02c3/c4/d OPEN. Inputs materiales, instancia, matching, cobertura, truth/observed, MD-C1/MD-C4, Outcome/Value dimensional y DAG por V_j siguen OPEN. Sin fixtures, implementación, ejecución ni Design Freeze.


## 20. MED-02d — crosswalk E_T, evidencia, cobertura y adjudicación (2026-11-10)

Se añade maestro §252, reutilizando EVIDENCE_REGISTER, CLAIM_EVIDENCE_LINK, COVERAGE_REGISTER, EVALUATOR_ASSESSMENT y ADJUDICATION_REGISTER existentes, junto con el manifiesto documental C10-S. No se crea tabla, FK, target PAR ni registro paralelo.

Quedan diferenciados: estado estructural S_T*, cambio ΔT_acc*, plano epistémico E_T, truth_DGP seguro y observed_state. Se documentan las clases funcionales de fuente (contrato/catálogo; artefacto/configuración; snapshot/runtime; logs/eventos; telemetría; alternativas/dependencias; oráculo/adjudicación; truth DGP), sin crear enum source_type.

Se fija el crosswalk de registros, las dimensiones de suficiencia (identidad, procedencia, integridad, tiempo, ámbito, método, cobertura, cegamiento, missingness/contradicción y adjudicación), la cadena de evaluación por etapa/ruta y las reglas 1/0/?/NA/NOT_COMPARABLE. Se preservan los límites: evidencia de contrato no prueba estado aplicado; intento/log no sustituye FP-06/07; FP-08 no compensa FP-01…07; truth no reemplaza observación ni se revela al Analyzer.

**Cerrado:** diseño documental de la interfaz E_T/U_G y controles de adjudicación.  
**OPEN:** fuentes/instancia/snapshots reales, field_id/event_id, scopes/denominadores, AB-TIME-01, serialización/hash, oráculo independiente/fiabilidad, evaluadores/cegamiento, missingness/error diferencial, R0–R3 y Outcome/Value dimensional. MED-02d no está materialmente cerrado. Sin registros, fixtures, implementación ni ejecución.


## 21. AB-TIME-01 — crosswalk temporal de event_key y alias históricos (2026-11-10)

Se añade maestro §253. La reconstrucción distingue: DGP §34.1 histórico (t0 baseline…t8 Value, con selección/ejecución agrupadas); Path Predicate Matrix §2 (t0 baseline, t1 asignación+provisión agrupadas, t2 verificación, t3 snapshot, t4 Reach, t5–t9 downstream); y reloj posterior §§64.3/168/216.7/233 (t−1 baseline, t0 Z, t1 provisión, t2 verificación, t3 snapshot, t4 Reach, t5 K, t6 selección/inicio, t7 ejecución, t8 Outcome, t9 Value, t+1 residuos).

Se corrige la referencia previa de §9.3: el §2 del maestro es arquitectura causal, no el contrato temporal histórico. La fuente antigua comprimida es §34.1. Se propone secuencia semántica BASELINE_PRE_Z → ASSIGNMENT_Z → POLICY_PROVISION → INSTALL_VERIFICATION → ACCESSIBILITY_SNAPSHOT → REACH_DERIVATION → KNOWLEDGE_CONSIDERATION → SELECTION_START → EXECUTION → OUTCOME → VALUE → POST_HORIZON_RESIDUAL. El t1 de Path Matrix no es unívoco porque agrupa asignación y provisión.

Se mantienen ortogonales stage_key, SNAPSHOT.phase/timestamp, route_id, branch_id/step_k y reloj de trayectoria. Los timestamps originales y valid-time no se reescriben; no se infiere simultaneidad ni se fabrican event_id.

**Dictamen:** orden semántico reconciliado; AB-TIME-01 parcialmente resuelto. La adopción formal del reloj numérico posterior y la declaración explícita de §34.1 como legado comprimido siguen OPEN. Sin instancia, event_id, snapshots, evidencia o ejecución.


## 22. MED-02c4 — correspondencia event_key/stage_key/SNAPSHOT/E_T (2026-11-10)

Se añade maestro §254. Reutiliza DEC-C10-065/070/071/072, U_G §§12–16 y 18–24, contratos de matching, E_T y reloj §253. Se fija la diferencia entre event_key semántico, source-native event ID, EID de invocación de transformación, stage_key, revisión SNAPSHOT y E_T. No se crea event_id ni tabla de eventos.

El crosswalk establece la precedencia funcional de C_SRC, F1_S2, A1_S1, F2_DST_DECL, A2_DST_DECL, F2_DST_APPLIED y A2_DST_APPLIED; mantiene su independencia respecto de SNAPSHOT.phase y del reloj t−1…t9. Reutiliza la tupla C0 de nueve componentes y C10S_SCOPE_GLOBAL; dimension sigue fuera de C0. Route-specific se resuelve por route_id/route_record_id y ROUTE_STEP; la relación evento→snapshot→evidencia se documenta con provenance, timestamp_start/end_tz, CLAIM_EVIDENCE_LINK y evaluaciones existentes, sin afirmar FK inexistente.

**Cerrado documentalmente:** reglas de precedencia, matching, cardinalidad, deduplicación, no retroacción y 15 casos adversariales C4-01…15.  
**OPEN material:** fuentes/event IDs, snapshots/revisiones, tiempos sincronizados/valid-time, route records, scopes/denominadores, mapping por clase y ejecución autorizada de C0/adjudicación. MED-02c4 permanece DOCUMENTED / MATERIAL OPEN. Sin implementación, registros ni ejecución.


## 23. AB-09 — truth tables estructurales R0–R3 y observación (2026-11-10)

Se desarrolla maestro §255 sobre el contrato ya integrado en §247 y el inventario finito histórico. No se recrean escenarios ni matrices paralelas. Se fija la diferencia entre invariantes de R0 focal exclusivo, R1 alternativa estable, R2 vía colateral de B y R3 intento fallido; se aclara que R3 se cruza con el régimen alternativo de fondo R0/R1, conforme al inventario finito, y no introduce una topología R4.

Se especifican reglas lógicas para C_dep*, rutas F/A, F_alt, A_f*, D_f*, ΔT_acc* y Reach; truth binaria del DGP frente a observed_state trivalente; y el firewall de roles sin filtrar etiquetas de escenario. Se añaden 12 contratos adversariales AB09-T01…T12. No se asignan probabilidades ni valores por unidad.

**Cerrado documentalmente:** lógica e invariantes de escenarios, derivaciones, truth/observed, roles y tests de diseño.  
**OPEN material/estadístico:** truth tables por unidad/snapshot/paso, parámetros D2 y distribución I/G/C/O, F*/G/H/ventanas, inventario alternativo y MD-C1/MD-C4, medición/missingness/oráculo, q_X*/soporte/interferencia, Outcome/Value V_j, firewall y criterios cuantitativos del Analyzer. AB-09 no es materialmente cerrado ni AB DONE.


## 24. C-ANALYZER — adjudicación de identificación, atribución y abstención (2026-11-10)

Se incorpora maestro §256, especializando §§225.7/225.9 y 229.5–229.7, sin duplicar P177/P178/P179/P182/P183 ni crear una batería de tests paralela.

Se definen clases truth y salidas admisibles; errores FI, FI-IND, FA, TARGET_MISMATCH, FALSE_BOUNDS y FALSE_ABSTENTION; recuperación puntual y abstención correcta; denominadores N_PI/N_PART/N_NI/N_IND/N_NA/N_PACKAGE/N_ASSIGNED; reglas de solapamiento; ficha de criterios/tolerancias ex ante; y orden Generator→Analyzer→freeze→Evaluator. Se incorporan 12 casos ANJ-01…12 como contratos documentales.

**Cerrado documentalmente:** lógica de adjudicación, denominadores y taxonomía de error.  
**OPEN:** umbrales/tolerancias, utilidad de bounds, multiplicidad, calibración, N/potencia, réplicas Monte Carlo y validación técnica del firewall. AN-03 DOCUMENTED / DENOMINATOR LOGIC SPECIFIED; AN-04 PARTIALLY SPECIFIED / NUMERIC THRESHOLDS OPEN; C-ANALYZER sigue OPEN. No ejecución.


## 25. C-MED / MAP-01–02 — reconciliación D2→g y jerarquía causal (2026-11-10)

Se reutilizan MAP-01/02 existentes en auditoría IV §14.6–14.7; no se crean contratos duplicados. MAP-01 ya define campos de identidad/versionado y registro de la política D2, pero sus valores materiales (actor, artefacto/hash, runtime, endpoint, ventanas, recepción, reintentos/rollback y detección de provisión de fondo) siguen abiertos. MAP-02 ya define el orden temporal y las mediciones separadas de W_programmed, W_attempt, receipt, S_install, C_dep*, A_f*, D_f* y ΔT_acc*, pero fuentes, ventanas, snapshots y evidencia siguen abiertos.

Se fija la frontera causal:
- ITT_Z^D2: efecto de asignar B_g0/B_g1; si hay vías colaterales, efecto de política/paquete.
- θ_A(q): contraste general C10-D1 entre políticas factibles g1/g0 sobre el ΔT_acc* completo bajo régimen común q.
- IIE_M candidato: mediación interventional secundaria por la distribución conjunta factible de M=ΔT_acc*, condicionada por H y L pre-M; no es efecto directo natural ni se obtiene por resta.

D2 solo podría informar θ_Af(q*) focal si se demuestra B→g^Af, q* común, versiones, soporte y ausencia/identificación de rutas no focales. No equivale automáticamente a g sobre el espacio transformacional completo. A_f* y D_f* son predicado/indicador focal; no sustituyen M. ΔE_T permanece epistémico y fuera de M. ΔX* requiere el crosswalk semántico campo a campo de §§230–231.

Se preservan los gates MAP-03…07 y MED-03/05. La clasificación de L depende de B→L, L→M y L→V_j por dimensión/horizonte. Sin población, q, soporte, interferencia, Value dimensional, fuentes y observación no se declara identificación.

**Estado:** reconciliación conceptual/documental completada; MAP-01/02 MATERIAL OPEN; B_D2→g^Af no demostrado; B_D2→g general no presumible; C-MED OPEN. Sin aprobación de estimando/método, Design Freeze, implementación ni ejecución.


## 26. MAP-03/04 y MED-03 — distribución inducida, soporte y clasificación de L

Se reutilizan MAP-01/02 de auditoría IV §§14.6–14.7, el roster causal de §§232/250, el crosswalk §§251–254 y la reconciliación §257. No se crean variables, field_id, event_id ni matriz paralela.

**MAP-03:** g_j^ind(m|h,l;q) representa la distribución conjunta inducida de M=ΔT_acc* bajo la política/version b_j, respecto de la misma población q_X* y régimen común q. L solo se incorpora como historia pre-M en un modelo longitudinal que modele B→L; no se condiciona ingenuamente en L postratamiento. Se requiere soporte estructural, de asignación/recepción, secuencial, de mediador y de resultado. El solapamiento marginal no basta. No se extrapola, trunca ni fusiona versiones para ocultar falta de soporte. Si solo una región tiene soporte, cualquier estimando restringido debe declarar el cambio de población objetivo.

**MAP-04:** versiones solo pueden agruparse si son equivalentes para el estimando, población, historia, horizonte y V_j. Igualdad de M, A_f*, D_f* o éxito técnico no prueba equivalencia si difieren rutas directas a Value, recursos, permisos, seguridad, rendimiento, información, alternativas, costes, observación o interferencia. En caso de duda se mantienen separadas o se estiman como políticas/paquetes distintos.

**MED-03:** cada campo/subcampo existente se clasifica por unidad, evento, snapshot, precedencia y dimensión V_j. “Confusor M–V inducido” exige conjuntamente B→L_k, L_k→M y L_k→V_j. Si solo B→L→M, es antecedente técnico; si B→L→V_j sin pasar íntegramente por M, es vía colateral; si ocurre después de M, es downstream. E_T sigue siendo evidencia, salvo que el proceso de observación altere conducta/información. Las familias de §251 son candidatas de inspección, no evidencia de flechas.

**Estado:** especificación documental integrada; MAP-03, MAP-04 y MED-03 continúan OPEN material/identificación. No hay umbrales, método, población, q, potencia o parámetros aprobados. Sin Design Freeze ni ejecución científica.

## 27. MAP-05/06 — auditoría de rutas y exclusión por Outcome/Value

Se reutilizan auditoría IV §§12.2–12.4 y 14.5–14.7, registro causal §§232/250, crosswalk §§251–254 y escenarios R0–R3/B-M. No se crean rutas ni variables paralelas.

**MAP-05:** cobertura del universo F/A y alternativas, componentes compartidos, modificaciones por B, recursos/runtime, permisos, red, seguridad, rendimiento/costes, datos, conocimiento y residuos/carryover. R1 (alternativa basal estable) no viola por sí sola exclusión; R2 (alternativa modificada por B) introduce ruta no focal. La ausencia requiere universo exhaustivo y cobertura; UNKNOWN no se convierte en 0.

**MAP-06:** dictámenes independientes EXCLUSION_O y EXCLUSION_Vj (SUPPORTED/CONTRADICTED/UNKNOWN). Una ruta directa a Value puede existir con Outcome constante. Se separan exclusión estructural, medición diferencial/oráculo e interferencia/carryover. ITT_Z^D2 puede conservar interpretación de asignación si diseño, consistencia, unidad/interferencia y medición son válidos; LATE_f/Wald no se interpreta causalmente si falla cualquier supuesto IV. Estos gates no identifican θ_A(q) ni mediación por sí solos.

**Estado:** contratos documentales integrados; MAP-05/06 MATERIAL OPEN. No hay dictamen empírico de exclusión. AB-M06/M09/M10 siguen OPEN. Sin Design Freeze ni ejecución científica.

## 28. MAP-07 — matriz de adjudicación y frontera entre estimandos

Se especializan maestro §260, C-MED §257 y auditoría IV §14.5, sin crear estimandos. La adjudicación se realiza por estimando × resultado/dimensión × población/unidad × horizonte × versión.

Se fijan las condiciones de admisibilidad y límites de transferencia para: ITT_Z^D2 (asignación/política), LATE_f^D2 (IV focal bajo IV-G1…G8), θ_Af(q_X*) (políticas focales), θ_A(q) (políticas sobre ΔT_acc* completo) e IIE_M (mediación interventional secundaria). Se explicita que ninguno sustituye automáticamente a otro; Outcome y cada V_j reciben dictámenes independientes; los estimandos no se suman ni se restan sin descomposición compatible previamente definida.

El Analyzer debe rechazar target mismatch, no acceder a truth/potenciales, comprobar cada supuesto, mantener UNKNOWN cuando falte evidencia y abstenerse cuando no se pueda distinguir vía focal de colateral. Se reutilizan las clases/denominadores/contratos de §256 y P177/P178/P179/P182/P183; no se inventan umbrales ni métricas.

**Cerrado documentalmente:** matriz lógica de adjudicación, límites de transferencia y regla de abstención MAP-07.  
**OPEN material/identificativo:** gates MAP-01…06, MED-02…06, C-Value, AN-04 y evidencia por resultado/dimensión. MAP-07 no identifica empíricamente ningún estimando. Sin Design Freeze, implementación ni ejecución; scientific_execution=false; execution_authorized=false.

## 29. MED-04 — contrato candidato g0/g1 y régimen común q

Se incorpora maestro §261, especializando C-MED §§249/257 y auditoría IV §§14.1–14.5. g0/g1 son políticas estocásticas factibles sobre el mediador conjunto M=ΔT_acc* completo, no asignaciones D2, instalaciones ni intervenciones sobre A_f*/D_f* aislados. Se preserva la dependencia de ΔU*/ΔR*/ΔC*/ΔX* y la estructura constitutiva; no se factoriza sin justificación. θ_A,j(q)=E_q[V_j^{g1}−V_j^{g0}] queda como notación candidata, no fórmula aprobada.

q debe fijar población/unidad, H, contexto/τ, condiciones upstream comunes, alternativas/recursos/permisos, interferencia/carryover, Outcome/Value por dimensión, horizonte y medición. L post-B no se trata como basal: debe justificarse L invariante, definir una distribución de referencia común q(L|H) factible, o reformular como régimen longitudinal conjunto. Esta elección sigue OPEN.

**Estado:** MED-04 DOCUMENTED / PARTIALLY SPECIFIED. Permanecen OPEN las políticas concretas, conjunto admisible M, población/H, contenido de q, tratamiento de L, V_j/horizonte, soporte, versiones e interferencia. No se equipara D2 con g ni se identifica θ_A(q). Sin Design Freeze, implementación o ejecución; scientific_execution=false; execution_authorized=false.

## 30. MED-05 — contrato de identificación del efecto interventional conjunto

Se incorpora maestro §262, especializando la propuesta ya existente en §249 y ledger §17; no se crea estimando nuevo. Se conserva el IIE_M,j candidato con referencia b1 y mediador conjunto M=ΔT_acc*. Se fijan nueve gates de identificación: consistencia/versiones; historia basal; intercambiabilidad de B; intercambiabilidad secuencial M–V; soporte/positividad condicional; factibilidad de la intervención M; medición/observación; interferencia/dinámica; y especificación del método.

Se precisa que L inducida por B no puede tratarse como basal ni omitirse; la distribución de L sigue el régimen de referencia b1 y G_M^b0 debe tener soporte en las historias relevantes bajo b1. Se identifican g-computation longitudinal, ponderación/densidades y TMLE longitudinal como familias candidatas, sin seleccionar una antes de conocer población, N, estructura de M, soporte y DGP. Downstream se integra para el contraste total; no se ajusta mecánicamente. Se fijan IDENTIFIED/PARTIALLY_IDENTIFIED/NOT_IDENTIFIED/INDETERMINATE y la regla de no transferencia a θ_A(q), ITT, LATE o dimensiones distintas.

**Estado:** MED-05 DOCUMENTED / CANDIDATE; gates y método no validados. MED-03/04/06, §224, inputs materiales AB/MAP y AN-04 permanecen OPEN. Sin Design Freeze, implementación ni ejecución; scientific_execution=false; execution_authorized=false.

## 31. MED-06 — sensibilidad, identificación parcial y bounds para C-MED

Se incorpora maestro §263, especializando §225.6–225.9, §§249.5–249.7 y §262, sin duplicar taxonomías ni crear estimandos. La unidad de sensibilidad es estimando×V_j/Outcome×población/unidad×horizonte×régimen/versión×soporte; el foco es IIE_M con M=ΔT_acc* conjunto. Se prohíbe transferir resultados a θ_A(q), ITT_Z^D2, ψ_policy^D2, LATE_f o θ_Af.

Se registran amenazas separadas: confusión B–resultado y M–V, L incompleta/error, error conjunto de M, error Outcome/Value, soporte cruzado, missingness/selección, interferencia/carryover, versiones/provisión de fondo y especificación/interacciones. Se exige sensibilidad univariada y conjunta cuando proceda, con tipping surfaces interpretadas frente a rangos justificados, no como prueba de plausibilidad.

Se delimitan bounds candidatos por outcome acotado/missingness, selección (Lee solo bajo monotonicidad defendible), confusión no medida bajo restricciones explícitas, error de medición acotado, soporte limitado y spillovers. Todo bound debe declarar supuestos, target, conjunto/anchura y separar incertidumbre muestral. Solo es informativo si reduce el rango trivial; no se presume que exista bound útil.

**Estado:** MED-06 DOCUMENTED / PARTIALLY SPECIFIED. Rangos, parámetros, escalas, soporte, historia L, errores, missingness, interferencia, método de bounds y AN-04 permanecen OPEN. Sin Design Freeze, implementación, fixtures, simulación o ejecución; scientific_execution=false; execution_authorized=false.

## 32. C-Value — crosswalk candidato Outcome/Value para Opción A

Se incorpora maestro §264, especializando §224 y reutilizando la frontera P0/P1/P2, F*, F1/F2, A1/A2 y MAP-05/06/07. Se separan F* (criterio técnico), Outcome (estado/consecuencia operativa) y Value (valoración contextual para beneficiario identificado). No se crean campos de roster ni se seleccionan dimensiones confirmatorias.

Se registran familias candidatas O-MIG (estado de migración), O-CONF (conformidad destino), O-SVC (continuidad), O-REC (recuperación) y O-BUR (carga operativa). Se registran roles y dimensiones Value candidatas: propietario del servicio (continuidad/fiabilidad), operador (carga/coste), mantenedor (portabilidad/flexibilidad), usuarios si existen (continuidad/calidad percibida) y responsable de riesgo si procede (riesgo/seguridad/compliance). Son hipótesis de diseño, no actores/dimensiones confirmados. Seguridad/compliance puede ser restricción no compensatoria.

Se establecen reglas anti-circularidad: no definir Value por ΔT_acc, A_f*, D_f*, Reach, trayectoria o ejecución; no equiparar telemetría con valoración; no inferir portabilidad futura de disponibilidad A1/A2; mantener pluralidad de beneficiarios y Value vectorial, sin índice/ponderaciones por defecto.

**Estado:** C-Value CANDIDATE CROSSWALK DOCUMENTED / MATERIAL OPEN. Beneficiarios, indicadores, fuentes, escalas, ventanas, trade-offs, instrumentos, error, missingness, cegamiento y multiplicidad siguen OPEN. No se identifica ΔT_acc→Value ni se aprueba implementación/ejecución; scientific_execution=false; execution_authorized=false.

## 33. C-Value ↔ roster: crosswalk de Outcomes/Value contra §232/§233

Se incorpora maestro §265. Se acota explícitamente la instancia a C10S-SVC-REQUEST-PROCESSOR v1.0.0 / instancia -001 rev1 / CMP-SERVICE-LOGIC-001 y a Opción A; no se asume un servicio genérico, usuarios, SLA, operador humano o métricas empresariales.

El crosswalk reutiliza el roster de §232, el DAG de §233, F*/FP-01…08, B-M01…15, snapshots y E_T/U_G. W_attempt, S_install, C_dep*, F1/F2/A1/A2, A_f*, ΔT_acc*, Reach y ejecución se mantienen como proceso/mecanismo, no Outcomes.

Resultado por familia:
- O-MIG: no existe campo terminal ni event_id; W_attempt/S_install/C_dep* no lo sustituyen.
- O-CONF: anclaje conceptual parcial en F*/FP-01…08 y C_dst, pero faltan predicados, mapping, tolerancias, oráculo y snapshots.
- O-SVC: B-M02/03/04/08/10/12/11/15 son superficies, no una medida de continuidad/calidad; no hay SLI/SLO, baseline o ventana.
- O-REC: B-M06/11/15 y E_T pueden aportar eventos/evidencia, pero rollback disponible no es recuperación lograda; faltan eventos y tiempos.
- O-BUR: B-M06/07/10/12 son superficies potenciales; no hay tiempo humano, coste, tarifa o ventana aprobados.

Ningún O tiene ficha §224 completa. CMP.owner no demuestra beneficiario. No hay beneficiarios/roles confirmados, instrumentos, source_id, instrument_version o adjudicación poblados. El término L_m y la forma ilustrativa V=3O+4L_m+epsilon_V no se heredan como Value; no se aprueban coeficientes ni ponderaciones.

**Estado:** C-VALUE↔ROSTER CROSSWALK DOCUMENTED / MATERIAL OPEN. No se crean field_id/event_id, snapshots, registros E_T, fixtures ni resultados. MED-02/03 continúan OPEN; no se identifica ΔT_acc→Value. Sin Design Freeze, implementación o ejecución; scientific_execution=false; execution_authorized=false.

 
## 34. C-Value — auditoría de roles/beneficiarios del dominio sintético

Se incorpora la auditoría de roles contra DEC-C10-068/069/089, el contrato funcional del servicio, el DGP temporal/roles y los crosswalks §§264–265. La función de referencia de `C10S-SVC-REQUEST-PROCESSOR v1.0.0` (aceptar solicitudes cuando está habilitado y exponer un perfil declarado) no instancia por sí sola solicitantes, consumidores, usuarios, propietario del servicio ni beneficiarios.

Se distingue `CMP-SERVICE-LOGIC-001` (componente lógico) del owner lógico provisional `CMP-SERVICE-LOGIC` de la RUL; ninguno demuestra propiedad organizativa ni beneficio. El actor de t6/ejecución es un campo/rol del DGP, no una identidad ni un beneficiario. El consumidor/sistema de la definición genérica de servicio lógico es una referencia conceptual, no una población observada. DEC-C10-089 mantiene sin adjudicar la relación NODE raíz `LOGICAL_SERVICE_UNIT`↔CMP.

Dictamen de los roles candidatos §264:
- propietario del servicio: NOT_GROUNDED;
- operador: NOT_GROUNDED;
- mantenedor: NOT_GROUNDED;
- usuario/destinatario: NOT_GROUNDED;
- responsable de riesgo: NOT_GROUNDED.
El evaluador independiente queda excluido como beneficiario por su función metodológica.

El DGP temporal incluye beneficiario/regla/horizonte en t9 y DGP-13 exige beneficiario, criterio, escala y horizonte ex ante, pero esos campos son requisitos pendientes, no evidencia de entidades materializadas. El microdominio sí sostiene el contrato funcional sintético y puede sostener Outcomes técnicos tras completar §224; no sostiene actualmente Value contextual. No se concluye imposibilidad: cualquier consumidor/beneficiario sintético deberá introducirse mediante extensión explícita y decisión del DGP, no por inferencia desde el nombre del servicio, CMP.owner o actor ejecutor.

**Estado:** ROLE/BENEFICIARY AUDIT DOCUMENTED / NO BENEFICIARY GROUNDED / VALUE MATERIAL OPEN. No se crean entidades, IDs, fields, eventos, snapshots ni instrumentos. Sin Design Freeze, implementación ni ejecución; scientific_execution=false; execution_authorized=false.

 
## 35. C-Value — comparación A/B y recomendación de extensión sintética separada

Se compara mantener Opción A sin Value instanciado frente a extender el DGP con un rol consumidor/beneficiario sintético. A preserva el dominio aceptado y permite pruebas transformacionales y Outcomes técnicos, pero no prueba ΔT_acc→Value. B podría probar recuperación causal de Value dentro de un mundo sintético estipulado, pero no valida preferencias/valor de usuarios reales y añade riesgos de circularidad, vías directas, confusión O/V, demanda postratamiento e interferencia.

**Recomendación propuesta:** mantener A como variante base inalterada y desarrollar B como variante DGP separada/versionada, no como modificación silenciosa del contrato funcional DEC-C10-068 ni del roster de Opción A. Requisitos de B: rol/relación beneficiario-servicio-unidad; demanda pre-Z; perspectiva/criterio; separación Outcome/Value; vector V_j y trade-offs conforme P179 sin escalar por defecto; DAG con rutas focales y directas; temporalidad; fichas independientes §224 y controles P182/P183; unidad/interferencia; truth oculta al Analyzer y adversariales que refuten asociaciones automáticas ΔT_acc→Value.

No se crea entidad, ID, variable, evento, regla, fixture ni estimando nuevo. La propuesta no está aceptada; no modifica DEC-C10 ni cierra MED-02/MED-03, C-Value o AB.

**Estado:** A/B COMPARISON DOCUMENTED / B RECOMMENDED AS SEPARATE DGP VARIANT / USER ACCEPTANCE OPEN. Sin Design Freeze, implementación, fixtures, simulación ni ejecución; scientific_execution=false; execution_authorized=false.
