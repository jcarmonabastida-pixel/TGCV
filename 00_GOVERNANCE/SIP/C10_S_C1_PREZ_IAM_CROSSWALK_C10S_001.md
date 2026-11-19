# C10-S — C1.4: Crosswalk pre-Z del IAM y snapshot C_SRC para E_i

**ID:** C10-S-C1-IAM-CROSSWALK-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-11  
**Estado:** RECONCILIACIÓN LÓGICA / CAPTURA MATERIAL NONE / E_i OPEN  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)  
**No autoriza:** crear filas IAM, capturar snapshots, poblar U_G, generar fixtures, implementar, simular ni ejecutar.

## 1. Dictamen

El crosswalk lógico puede definirse a nivel de contrato, pero **no existe todavía un IAM material sellado ni snapshots C10-S observados** sobre los que adjudicar pertenencia de unidades. El overlay IAM/U_G declara explícitamente captura NONE para C_SRC, S1/S2 y destinos declarados/aplicados. Las etiquetas de scopes y la matriz 7×5 son planificación lógica, no IDs ni filas físicas.

Por tanto, C1.4 no puede asignar valores de E_i a unidades ni cerrar su composición material. Sí puede especificar el conjunto mínimo de registros y relaciones que deberán examinarse y detectar qué afirmaciones están hoy respaldadas solo por contrato.

## 2. Unidad lógica y anclaje temporal

Se reutiliza la unidad candidata:

`U_i=(L_i,C_{src,i},E_{src,i},E_{dst,i},M_i,S_{0,i},P2_i)`.

La unidad experimental completa y la unidad de asignación siguen separadas hasta verificar aislamiento. Para elegibilidad basal:
- el snapshot de origen `C_SRC` representa la configuración declarada basal;
- `C_SRC` se asocia a `route=NONE`, no a F/A;
- el snapshot exacto se identifica por `snapshot_id + snapshot_object_record_id`;
- los registros NODE/EDGE/ROUTE/PREDICATE/ROUTE_STEP quedan fijados a la revisión exacta de SNAPSHOT conforme DEC-C10-065;
- `stage_key`, reloj DGP `t−1/t0…t9`, SNAPSHOT.phase y step_k son ejes distintos y no se infieren unos de otros.

No se usa F1_S2/A1_S1 ni destino declarado/aplicado para determinar elegibilidad basal: son etapas posteriores del flujo transformacional. Si un atributo del entorno es basal y necesario, debe figurar en su snapshot/contrato P1 correspondiente, no reconstruirse desde el destino post-Z.

## 3. Crosswalk por clase de objeto C_SRC

| Clase | Qué debe resolverse en C_SRC | Papel potencial en E_scope | Evidencia/estado requerido | Límite actual |
|---|---|---|---|---|
| CMP | Identidad contractual, component_id/version, component_class, inclusión en frontera, NODE anchor exacto y boundary_class | Determinar que el objeto fuente está dentro del alcance y roster basal declarado | Inventario, NODE exacto, mapping, provenance y coverage COMPLETE para universo | CMP mínimo conocido no es roster exhaustivo; no hay snapshot |
| PAR | parameter_key, owner CMP, type, state, value, domain, requiredness, IAM applicability y mapping | Comprobar parámetros P0 obligatorios aplicables en C_SRC | VALUE tipado donde el contrato lo exige; ausencia/NULL solo con cobertura que la demuestre; UNKNOWN si falta evidencia | PAR-SVC-ENABLED/PROFILE son P0 REQUIRED para instancia de servicio; no prueban todos los PAR de C_SRC por UE |
| REF | ref_id, extremos, relación, dirección, multiplicidad, ámbito interno/externo y estado de resolución | Delimitar dependencias/referencias constitutivas incluidas en el objeto basal | REF=0 solo con inventario/cobertura exhaustiva; referencias desconocidas permanecen ? | Universo REF no está materialmente inventariado |
| RUL | rule_id/version, owner/scope, AST, operadores, operandos PAR, effect y bindings | Comprobar reglas constitutivas basales y su aplicabilidad al objeto | RUL≥1; regla/AST y operandos identificados; UNKNOWN si mapping/cobertura falta | RUL-SVC-ENABLE-PROFILE-01 aceptada como regla de servicio, pero no hay snapshot de instancia |
| MET | contract/instance IDs y versiones, source/version, mapping, IAM/version/hash, provenance, timestamps | Identidad, versionado y trazabilidad de la unidad basal | MET obligatorio; hashes y referencias verificables | Obligación lógica aceptada; sellado material no ejecutado |

El roster mínimo actualmente conocido de la instancia de servicio es `CMP-SERVICE-LOGIC-001`, `PAR-SVC-ENABLED`, `PAR-SVC-PROFILE` y `RUL-SVC-ENABLE-PROFILE-01`. No debe presentarse como inventario exhaustivo de C_SRC ni como roster completo de cada UE.

## 4. Crosswalk de predicados causales que no deben colapsarse

| Predicado/objeto | Registro/canal esperado | Papel en elegibilidad | Regla de no sustitución |
|---|---|---|---|
| `E_scope` | IAM + CMP/PAR/REF/RUL/MET de C_SRC + coverage | Admisibilidad de instancia basal | No implica App, C_dep=0 ni A_f=0 |
| `App*(τ2,S0)` | PREDICATE/ROUTE y truth DGP de aplicabilidad, vinculado a S0 y τ2 exactos | Condición candidata de aplicabilidad semántica | No implica que exista ruta/medio accesible |
| `C_dep,0` | Predicados/inventario de dependencias técnicas basales | Condición separada P*τ2: dependencia focal ausente | No implica ausencia de dependencias alternativas ni A_f=0 |
| `A_f,0*` | Truth DGP de ID/REL/COND/AUTH/RES/DEP/¬BLOCK con rutas y snapshots comparables | Condición separada P*τ2: inaccesibilidad focal verdadera | No se deriva de C_dep=0, App=1 ni A_f_obs=0 |
| `F_alt,0` | Inventario exhaustivo de rutas alternativas y F* | Solo define P*F secundaria | ? no equivale a 0; no filtra P*τ2 |
| `E_req_preZ` | Contrato del servicio de admisión de petición | Ningún papel en elegibilidad experimental C1 | No confundir con E_i |
| `Need_preZ` | Ficha de B1 | Ningún papel en elegibilidad transformacional P* por defecto | No inferir desde ausencia/presencia de request |

El contrato de `A_f^*` conserva la fórmula candidata vigente:
`I(ID_f* ∧ REL_f* ∧ COND_f* ∧ AUTH_f* ∧ RES_f* ∧ DEP_f* ∧ ¬BLOCK_f*)`.
`C_auth,base` se corresponde con AUTH; no se duplica. Recursos/capacidad solo se asignan a RES/R_access cuando son disponibilidad ex ante necesaria, no duplicada y correctamente clasificada P0/P1/DUAL. Información, conocimiento, selección, ejecución, Outcome y Value no se añaden como términos de accesibilidad.

## 5. Boundary class y temporalidad

Cada NODE aplicable debe tener `boundary_class` conforme al contrato aceptado:
- `P0_CONFIG`: contenido/configuración;
- `P1_ENVIRONMENT`: entorno;
- `DUAL_P0_P1`: artefacto indivisible con contenido de ambas clases;
- `NA`: no aplicabilidad justificada, no una clase sustantiva ni un unknown.

P2 es perímetro causal transversal y no un valor de `boundary_class`.

Para cada condición candidata a E_i, el crosswalk deberá registrar si se ubica en P0, P1 o DUAL y si es constitutiva de alcance, condición de aplicabilidad, dependencia focal, término de A_f, vía colateral o variable epistémica. Un elemento P1 no se introduce automáticamente en E_i: debe justificarse que es basal, ex ante y necesario para la aplicabilidad/realizabilidad de τ2, y no una vía diferencial inducida por Z.

## 6. Estado de materialización y cobertura

Los contratos de IAM/U_G describen:
- hasta 35 scopes lógicos para 7 etapas × 5 clases, no 35 filas que deban crearse automáticamente;
- scopes únicos por contrato/instancia/snapshot/revisión/etapa/ruta/clase;
- `C_SRC` como snapshot de configuración fuente, sin ruta F/A;
- filas por objeto/propiedad y snapshot enlazadas a IAM, evidence y coverage;
- cobertura COMPLETE solo cuando universo, denominador, fuentes y regla de completitud están justificados.

El overlay actual indica que no hay snapshots C10-S observados ni captura de C_SRC, S1/S2, destino declarado o aplicado. En consecuencia:
- no hay registros IAM pre-Z por UE que permitan clasificar E_scope;
- no hay COVERAGE_REGISTER material que permita afirmar roster exhaustivo;
- no se puede declarar REF=0;
- no se puede adjudicar truth observada de App, C_dep o A_f por unidad;
- no se puede estimar proporción elegible ni soporte de P*τ2/P*F.

## 7. Composición de E_i: estado tras el crosswalk

La estructura candidata `E_i=E_scope,i ∧ App*(τ2,S0_i)` permanece **propuesta, no aceptada**.

El crosswalk confirma que:
- `E_scope` necesita IAM/C_SRC material y cobertura, no solo cardinalidades abstractas;
- `App*(τ2,S0)` tiene anclaje en el inventario finito, pero el inventario es una propuesta y requiere contrato de identidad/aplicabilidad;
- `C_dep,0=0` y `A_f,0*=0` son condiciones separadas ya definidas por POP-CMP-001;
- `F_alt,0` solo afecta P*F;
- no existe base para agregar una lista adicional de C_auth/C_resource/C_capacity/C_info/C_domain/C_other: esa fórmula histórica fue retirada; C_other inadmisible y duplicidades deben evitarse.

No se debe declarar `E_i` cerrada ni usar elegibilidad observada como sustituto de truth sin modelo de error.

## 8. Dictamen C1.4 y siguiente cierre

**C1.4: PARTIAL / MATERIAL BLOCKED BY ABSENT IAM AND SNAPSHOTS.** El contrato lógico de crosswalk queda especificado; la composición material de E_i y la clasificación de unidades no pueden completarse sin inventar registros o truth. Esto es una limitación de estado documental, no un fallo del diseño causal.

Siguiente trabajo C1.5:
1. cerrar, desde las fuentes de contrato, el predicado de aplicabilidad `App*(τ2,S0)` y su frontera con `A_f^*`;
2. decidir si `E_scope` es solo un gate de alcance DGP o forma parte de elegibilidad confirmatoria, y documentar el efecto de esa selección;
3. fijar la regla pre-Z para UNKNOWN en E_scope/App/A_f y cómo se informará la población confirmada frente a la población objetivo;
4. recuperar el contrato de asignación D2 (probabilidades, estratos, algoritmo/semilla, provenance) sin inventar 1:1;
5. emitir dictamen de factibilidad/soporte; sin IAM/snapshots reales del DGP, no declarar una población materializada ni simular su distribución.

No se necesita otra confirmación de precedencia P*τ2/P*F. La propuesta de composición E_i no se acepta en este documento. Sin Design Freeze ni autorización de implementación/ejecución.


## 9. Precedencia de la reconciliación integrada PA (2026-11-11)

El paquete PA (§15 de `C10_S_C1_ITT_D2_RECONCILIATION_DRAFT_001.md`) reutiliza este crosswalk sin reiniciarlo. `E_scope` se recomienda como gate de alcance del universo DGP, no como filtro de selección adicional dentro de ese universo, salvo que se generen deliberadamente unidades fuera de alcance. `App*(τ2,S0)` sigue como condición candidata de aplicabilidad; la fórmula `E_i=E_scope∧App` no se acepta ni se congela.

La ausencia material de IAM/C_SRC/snapshots continúa bloqueando la clasificación por unidad, la cobertura exhaustiva, `REF=0`, la adjudicación de truth observada y el soporte. UNKNOWN no se recodifica como cero ni se excluye sin regla pre-Z; truth DGP y evidencia observada siguen segregadas. El siguiente paquete es PB, no un gate conversacional C1.5 independiente.


## 10. Integración con identidad B1 por UE y PB material (2026-11-11)

La decisión `DEC-C10S-B1-SERVICE-INSTANCE-IDENTITY-001` fija contract/plantilla común e instancia única/versionada por UE. Esta regla no materializa roster ni IAM: `instance_id` concretos deben resolverse desde el roster aprobado y quedar vinculados a SNAPSHOT exacto/provenance. El servicio CMP lógico y el adaptador/dependencia focal P1 son objetos distintos.

El ciclo PB material integrado se registra en `C10_S_PB_MATERIAL_D2_INSTANCE_AND_ISOLATION_RECONCILIATION_DRAFT_001.md`. C_SRC/C1.4 sigue MATERIAL BLOCKED BY ABSENT IAM AND SNAPSHOTS; no se afirma cobertura COMPLETE, REF=0, población materializada ni soporte. boundary_class y las FKs exactas se aplican conforme a DEC-C10-059/065/082 y a U_G, sin añadir tablas ni columnas por esta reconciliación.

## 11. Integración del ciclo D2 asignación/población/soporte (2026-11-11)

El contrato C1.5/D2 se complementa con C10_S_D2_ASSIGNMENT_POPULATION_SUPPORT_RECONCILIATION_DRAFT_001.md. El crosswalk C1.4 conserva su dictamen: sin IAM/C_SRC/snapshots y coverage material no se clasifica E_scope ni se estima E_i/q_X*. No se recrean filas ni se convierte la matriz 7×5 en inventario físico.

Se aclara que App*(τ2,S0) es aplicabilidad semántica, no accesibilidad; la propuesta E_i=E_scope∧App sigue NO ACEPTADA. La regla UNKNOWN y la asignación Z deben quedar selladas pre-Z; no se confunde Pr(Z=1) con las probabilidades de programación D2 0/1 condicionales a Z. Sin fuente material aprobada no hay soporte ni positividad verificables.
