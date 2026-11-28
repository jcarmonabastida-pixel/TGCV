# C10-S — Gate 92: crosswalk de etapas D2 entre Generator, evidencia, Analyzer y Evaluator

**Estado:** D2 STAGE CROSSWALK COMPLETE / POLICY-TO-ACCESSIBILITY CHAIN NOT MATERIALIZED / CURRENT HARNESS IS V_CONT ASSIGNMENT SLICE / NO CODE CHANGE / NO EXECUTION  
**Rama:** `research/c10-s-consolidation-draft`  
**HEAD de referencia:** `8a93493d9692377611cdfdaa5c0533efe926d866` (Gate 91 integrado).  
**Fuentes:** DEC-C10-067; DGP Temporal and Role Contract; Generator `88c6c7bd6f82353e64a4f12edbe2e2abc2cec002`; README del harness `f835b92d06aec9693c24ce92d82e0d47de3be1cf`; tests `1933f9b17cedce919adb3d60ac138d18320ef35e`.  
**Alcance:** clasificar la correspondencia de cada etapa material D2 con campos y contratos actuales. No definir valores cuantitativos, no implementar, no modificar código, no ejecutar.

## 1. Regla de clasificación

- **EXISTENTE:** el objeto está representado explícitamente con identidad/semántica compatible.
- **PROXY NO VÁLIDO:** existe un campo/mecanismo cercano, pero no representa el objeto D2 por diferencia de intervención, etapa o constructo.
- **AUSENTE:** no existe campo, evento, potencial o salida que materialice el objeto.
- **PARCIAL:** existe una proyección restringida, pero falta mapping/semántica o parte del objeto.

Un nombre parecido, una variable interna o una declaración de contrato no equivale a evidencia de una etapa material.

## 2. Crosswalk de la cadena D2

| Etapa D2 | Generator / ScenarioConfig / TruthBundle | Evidencia Projector/Sealer | Analyzer / Evaluator | Dictamen |
|---|---|---|---|---|
| **Z — asignación** | `assignment_z`, potenciales `V(z,g)`, semillas y vector de asignación; Z aleatorizado | `assignment_z` y hash de vector en provenance | ITT-Z sobre V_cont; estado de identificación propio | **EXISTENTE**, como asignación aleatoria genérica. La política material asignada no está identificada por Z. |
| **B — política material (B_{gZ}^{D2})** | No hay campo/objeto versionado B_g0/B_g1, artefacto asignado, actor, recepción o desviación | No hay registro B ni versión/artefacto en filas; el `profile` no es la política D2 | No hay estimando/salida condicionado a identidad de B_D2 | **AUSENTE.** `z_assignment_mechanism_id=Z_BALANCED_INDEPENDENT` solo identifica la asignación Z, no B_gZ. |
| **W_programmed** | No existe evento/campo. DEC-C10-067 define probabilidades candidatas 0 bajo Z=0 y 1 bajo Z=1 | No se transporta | No se estima ni adjudica | **AUSENTE.** No puede inferirse de Z sin materializar la política y el evento. |
| **W_attempt** | `provision_ok` usa `u_provision`, pero no hay intento efectivo, recepción ni cumplimiento | No se registra | No hay primera etapa W_programmed→W_attempt | **PROXY NO VÁLIDO.** Es un sorteo genérico de provisión aplicado al vector G, no el evento de intento efectivo. |
| **S_install** | No hay instalación, actor, timestamps, recepción, rollback o desviaciones como objeto propio | No se registra | No se estima | **AUSENTE.** `provision_ok` no prueba instalación. |
| **C_dep*** | No existe conjunción explícita de C_install/C_integrity/C_compat/C_oper ni sus potenciales por Z | No se registran componentes ni evidencia técnica | No hay estado/estimando C_dep | **AUSENTE.** El éxito técnico no puede colapsarse en `provision_ok` ni en ΔT_acc. |
| **A_f*** | `focal_access=int(all(delta_vector))` es un agregado interno dependiente de G; no evalúa ID/REL/COND/AUTH/RES/DEP/¬BLOCK | No se publica como objeto distinto | No hay verdad/estimador/estado A_f | **PROXY NO VÁLIDO.** Conjunción de cuatro coordenadas no sustituye la fórmula candidata A_f*. |
| **D_f*** | No hay A_f basal y post separado ni indicador de apertura 0→1 | No se registra | No hay estimando D_f ni primera etapa ITT-D2 sobre D_f | **AUSENTE.** No inferir de G, C_dep o cambio de cuatro coordenadas. |
| **ΔT_acc*** | `potential_delta_t_acc` conserva cuatro coordenadas por potencial (z,g); el vector observado depende de G y provision_ok | `delta_t_acc_observed` se transporta y sella como cuatro bits | `first_stage_delta_t_acc` compara G=1 frente a G=0 dentro de Z=0 | **PARCIAL / PROXY PARA D2 NO VÁLIDO.** Hay vector sintético focal, pero su mapping a (ΔU*,ΔR*,ΔC*,ΔX*) no está cerrado y la primera etapa es G, no Z_D2. |
| **Reach_H / trayectoria** | `reach` y `trajectory` se calculan internamente para generar el resultado; no aparecen como campos completos de TruthBundle | No se transportan | No se reconstruyen ni adjudican | **PARCIAL INTERNO / AUSENTE COMO EVIDENCIA.** No hay universo/rutas/snapshots ni verdad observable de Reach. |
| **Outcome / V_cont** | `potential_v`, estados ENABLED/PROFILE e intervalos potenciales | S3 observado y estados de observación se sellan | ITT-Z/ITT-G y errores/recuperación para V_cont | **EXISTENTE EN ALCANCE LIMITADO.** No equivale a Outcome técnico completo ni a Value general de TGCV. |

## 3. Hallazgos transversales por rol

### 3.1 Generator y TruthBundle

- El Generator produce potenciales (V_i(z,g)) y potenciales de intervalos, ENABLED, PROFILE y cuatro coordenadas de (Delta T_{acc}).
- No produce la historia material D2 por etapas (B/W_{programmed}/W_{attempt}/S_{install}/C_{dep}/A_f/D_f).
- `itt_z_truth` es el contraste Z en el régimen G definido; `itt_g_z0_truth` es el contraste de asignación G bajo Z=0; `theta_a_truth=None`.
- La verdad de C1 puede usar el ITT-Z actual solo para el DGP realmente representado. No se puede denominar ITT-D2 material mientras Z no asigne B_g0/B_g1 y su cadena de provisión.
- La variable `provision_probability` no contiene una descomposición de intento/cumplimiento/recepción/instalación/éxito técnico.

### 3.2 Projector / Sealer

No existe una clase `Projector` separada en este módulo. El Generator devuelve directamente un `EvidenceCandidate` con filas ya proyectadas; el Sealer aplica una allowlist y sella:
`unit_id`, `cluster_id`, `assignment_z`, `assignment_g`, estrato basal, S3 ENABLED/PROFILE, sus estados de observación, cuatro bits `delta_t_acc_observed`, perfil y versión.

El Sealer rechaza campos adicionales. Esto preserva un firewall útil, pero actualmente impide transportar cualquier evidencia de B/W/S_install/C_dep/A_f/D_f porque esos campos no están en el contrato observado. No se deben añadir indiscriminadamente: primero debe definirse qué parte es observación admisible y qué parte permanece truth reservada.

### 3.3 Analyzer / AnalysisContract

El Analyzer estima:
- ITT-Z de V_cont;
- ITT-G bajo Z=0;
- ITT-Z bajo el régimen de referencia cuando se cumplen las condiciones de transporte;
- primera etapa descriptiva de las cuatro coordenadas G→ΔT_acc.

No estima la cadena de primeras etapas D2 (Z	o W_{programmed}	o W_{attempt}	o C_{dep}	o A_f	o D_f	oDelta T_{acc}). No estima θ_A, D_f ni mediación. El `AnalysisContract` identifica mecanismos de asignación Z/G y regímenes G, no políticas materiales B_g0/B_g1. `common_nonfocal_regime=True` se asigna en `contract_for`; es una declaración del contrato, no un certificado empírico de (r_{common}) por historia.

### 3.4 Evaluator

El Evaluator comprueba ITT-Z contra su verdad, ITT-G contra `itt_g_z0_truth`, y los estados de identificación/abstención correspondientes. No adjudica:
- fidelidad de B_gZ ni de W_programmed/W_attempt;
- C_dep, A_f o D_f;
- apertura focal y cambio completo de accesibilidad por Z;
- θ_A bajo políticas conjuntas;
- contribuciones causales intermedias o efectos por estrato para C1/C3.

## 4. Contrato mínimo de representación requerido — sin valores

Antes de cualquier implementación, el diseño debe definir el esquema semántico/versionado para:
1. **Asignación/política:** Z, policy_id/version, B_g0/B_g1, artefacto/versión y desviación/crossover.
2. **Intento:** W_programmed y W_attempt como eventos separados; recepción, actor, tiempo, cumplimiento, fallos y reintentos.
3. **Instalación/verificación:** S_install y evidencia separada de C_install, C_integrity, C_compat y C_oper.
4. **Accesibilidad:** A_f basal/post con ID/REL/COND/AUTH/RES/DEP/BLOCK; App_f separada; D_f como apertura basal→post.
5. **Cambio transformacional:** snapshot T_acc y ΔT_acc completo con mapping a ΔU/ΔR/ΔC/ΔX, identidad/versionado, truth y observed separados.
6. **Trayectoria/resultado:** Reach_H/Π_H derivado antes de selección/ejecución; trayectoria/Outcome/V_cont en etapas separadas.
7. **Evidencia:** fuente, cobertura, timestamp, versión, observador, adjudicación y estado 1/0/?; ausencia de evidencia no se convierte en 0.
8. **Roles/firewall:** Generator conserva truth/potenciales; Projector expone solo observaciones autorizadas; Sealer valida schema/digest; Analyzer no recibe truth; Evaluator compara después del sellado.

Este inventario no aprueba nombres de campos definitivos, valores de parámetros, probabilidades, estimandos nuevos ni código. Debe reconciliarse con el maestro §67.3, DEC-C10-067, el roster U_G, el contrato temporal y la arquitectura de roles ya existente.

## 5. Bloqueos cuantitativos y científicos que no deben rellenarse

- Probabilidad de intento efectivo/recepción bajo intento programado.
- Fallo parcial y reintentos.
- Distribución conjunta de los cuatro componentes técnicos de C_dep.
- Mapping de C_dep a A_f y de A_f a D_f/ΔT_acc.
- Identidad y versionado de TID/SID/RID, snapshots y fuentes.
- Soporte por historia, q_X*, políticas conjuntas g_A0/g_A1 y r_common.
- Heterogeneidad C1 por historia/estrato y masas.
- Medición/error/cobertura y adjudicación de Reach/A_f/D_f.

No se asigna (s=0.80) como verdad aprobada; DEC-C10-067 lo conserva como hipótesis no validada. No se usa G como sustituto de D2/Z o de g_A.

## 6. Dictamen y siguiente operación

**Gate 92 cerrado como crosswalk documental de etapas.** El harness actual es una implementación parcial de asignación Z/G y V_cont, no un Generator material D2 por etapas. La cadena causal central de provisión focal D2 permanece sin materializar entre Z y ΔT_acc.

Dictamen:
`GATE_92_D2_STAGE_CROSSWALK_COMPLETE / Z_ASSIGNMENT_PRESENT / B_POLICY_AND_W_PROGRAMMED_ABSENT / W_ATTEMPT_AND_S_INSTALL_ABSENT / C_DEP_AND_A_F_D_F_ABSENT / DELTA_T_ACC_G_ONLY_PARTIAL / REACH_TRAJECTORY_INTERNAL_ONLY / V_CONT_LIMITED_OUTCOME_PRESENT / ANALYZER_ITT_Z_AND_G_ONLY / THETA_A_NOT_MATERIALIZED / NO_CODE_CHANGE / NO_NEW_WORLDS / NO_EXECUTION / NO_DESIGN_FREEZE`.

**Siguiente operación — Gate 93:** reconciliar este contrato mínimo con el inventario de verdad/observación y el contrato de implementación vigente; identificar qué artefactos ya existentes pueden reutilizarse para cada etapa y producir un esquema de eventos/snapshots versionado sin duplicar objetos ni introducir un nuevo sistema paralelo. Mantener todos los parámetros cuantitativos abiertos y no implementar hasta autorización explícita.
