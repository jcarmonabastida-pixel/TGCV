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
