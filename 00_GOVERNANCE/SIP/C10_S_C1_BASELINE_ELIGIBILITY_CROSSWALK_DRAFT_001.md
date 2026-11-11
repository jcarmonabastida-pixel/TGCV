# C10-S — C1.3: Crosswalk de elegibilidad basal E_i para P*_{τ2}

**ID:** C10-S-C1-ELIGIBILITY-CROSSWALK-001  
**Versión:** Draft 001 · **Fecha:** 2026-11-11  
**Estado:** RECONCILIACIÓN DOCUMENTAL / PROPUESTA DE COMPOSICIÓN MÍNIMA / NOT ACCEPTED / NOT DESIGN-FROZEN  
**Rama:** `research/c10-s-consolidation-draft` · **PR:** #116 (Draft)  
**No autoriza:** sellado IAM, schemas físicos, fixtures, implementación, simulación ni ejecución.

## 1. Resultado

La precedencia poblacional está aceptada por DEC-C10S-C1-POPULATION-PRECEDENCE-001. Este trabajo examina qué significa `E_i` en:

`P*_{τ2}={i:E_i=1, C_dep,i0=0, A_f,i0*=0}`.

La documentación permite identificar dos piezas que deben quedar conectadas, pero no confundidas:

1. **Admisibilidad de la instancia basal dentro del DGP**: que la configuración fuente y su evidencia satisfagan el contrato constitutivo de la unidad abstracta.
2. **Aplicabilidad de la transformación focal**: que `τ2` sea aplicable desde el estado basal `S0`, sin que ello implique accesibilidad.

La especificación actual no ha aprobado todavía el puente formal ni la lista de predicados de unidad que componen `E_i`. Por tanto, se presenta una composición mínima candidata para revisión; no se eleva a decisión aceptada.

## 2. Precedencia semántica obligatoria

| Objeto | Pregunta que responde | No equivale a |
|---|---|---|
| `E_i` | ¿La unidad/instancia basal pertenece al dominio experimental definido y satisface los requisitos constitutivos pre-Z para evaluar τ2? | Accesibilidad focal, éxito de provisión o elegibilidad de petición |
| `App*(τ2,S0)` | ¿La transformación focal es semánticamente aplicable desde el estado basal? | Que existan medios/ruta suficientes para ejecutarla |
| `C_dep,0=0` | ¿Está ausente y verificada la dependencia técnica focal basal? | Inaccesibilidad completa ni ausencia de rutas alternativas |
| `A_f,0*=0` | ¿La transformación focal τ2 no es accesible en baseline según sus predicados constitutivos completos? | Falta de evidencia observacional ni simple fallo de C_dep |
| `F_alt,0` | ¿Existe una ruta funcional alternativa substituible respecto de F*? | Elegibilidad general P*τ2 |
| `Need_preZ` | ¿Qué necesidad/objetivo basal tiene B1? | E_i o necesidad inferida de una petición |
| `E_req_preZ` | ¿La petición satisface la admisión contractual del servicio? | Elegibilidad experimental P*τ2 |

La separación entre `C_dep,0` y `A_f,0*` ya está establecida en POP-CMP-001 y en la auditoría MEAS. La fórmula candidata de accesibilidad se conserva sin alteración:

`A_f*=I(ID_f* ∧ REL_f* ∧ COND_f* ∧ AUTH_f* ∧ RES_f* ∧ DEP_f* ∧ ¬BLOCK_f*)`.

No se añaden `C_auth,base` y `AUTH_f*` como factores separados. `C_other` queda excluido. Los términos epistémicos de validez/cobertura no se convierten en truth estructural.

## 3. Qué aporta el contrato abstracto de configuración

El contrato de instancia abstracta define:

`C=(ID_C,V_C,CMP,PAR,REF,RUL,POL?,MET)`.

La partición constitutiva DEC-C10-053 y la cardinalidad DEC-C10-056 establecen, para el DGP base:
- CMP ≥ 1;
- PAR ≥ 1;
- RUL ≥ 1;
- REF ≥ 0, pero REF=0 solo con IAM pre-Z/B y cobertura exhaustiva;
- POL ausente por diseño en el núcleo confirmatorio mínimo, salvo módulo condicional predeclarado;
- MET obligatorio para identidad, versión, procedencia y sellado IAM.

Esto define requisitos de alcance/validez del objeto de configuración. No determina por sí solo que una transformación concreta sea aplicable desde S0 ni que esté accesible.

El contrato funcional mínimo de servicio conocido identifica `CMP-SERVICE-LOGIC-001`, `PAR-SVC-ENABLED`, `PAR-SVC-PROFILE` y `RUL-SVC-ENABLE-PROFILE-01`; DEC-C10-083 acepta ENABLED y PROFILE como P0 REQUIRED en las siete etapas contractuales. Sin embargo, el roster se declara mínimo y no exhaustivo. No prueba el inventario completo de `C_src`, no sella un IAM por UE y no puede tratarse automáticamente como la composición completa de E_i.

## 4. Qué aporta el inventario finito de DGP

El inventario finito candidato describe `S0` como configuración basal elegible en la que τ2 focal no es accesible. Define el paso focal F1 desde S0 con dos requisitos separados:

- `App*(τ2,S0)=1`;
- `A_f*(τ2)=1` en el estado/condición en que F1 pueda realizarse.

Esta formulación es coherente con que una transformación pueda ser aplicable desde S0 y, sin embargo, no ser accesible en baseline. El inventario es todavía propuesta no aprobada; por ello `App*(τ2,S0)=1` es un candidato documentado para la composición de E_i, no una regla confirmatoria congelada.

## 5. Crosswalk de requisitos candidatos

| Requisito | Fuente existente | Rol posible en C1 | Estado y límite |
|---|---|---|---|
| Identidad y versión de instancia/configuración basal | Contrato abstracto C; MET; DEC-C10-065 y U_G | Delimitar qué instancia y snapshot se evalúan | Requisito documental; IAM/snapshots materiales no sellados |
| CMP/PAR/RUL no vacíos | DEC-C10-056; contrato abstracto | Admisibilidad de alcance del objeto DGP | Cardinalidad de clase aceptada; roster exhaustivo por UE no demostrado |
| REF=0 solo con cobertura exhaustiva | DEC-C10-056; contrato IAM | Evitar que ausencia de referencias/dependencias se presuma por falta de inventario | Regla aceptada; cobertura material OPEN |
| POL ausente por diseño o módulo predeclarado | DEC-C10-053; contrato abstracto | Delimitar el alcance P0 del DGP base | Ausencia por diseño en núcleo mínimo; cualquier módulo secundario requiere declaración pre-Z |
| MET/provenance/IAM | Contrato abstracto; IAM | Identidad, versión y trazabilidad de la unidad basal | Obligación lógica aceptada; serialización/hash/sellado material OPEN |
| Predicados P0/P1/DUAL/NA | DEC-C10-059 y matriz IAM | Resolver qué condiciones pertenecen a configuración, entorno o ambos | Clasificación conceptual disponible; mapping por predicado/unidad OPEN |
| `App*(τ2,S0)=1` | Inventario finito candidato, §4 | Aplicabilidad semántica basal de τ2 | Candidato coherente; no aprobado como componente formal de E_i |
| `C_dep,0=0` | POP-CMP-001; DGP temporal | Ausencia basal de dependencia técnica focal | Requisito separado ya definido para P*τ2 |
| `A_f,0*=0` | POP-CMP-001; crosswalk A_f; MEAS audit | Inaccesibilidad basal verdadera focal | Requisito separado ya definido; verdad y observación no intercambiables |
| `F_alt,0` | POP-CMP-001; inventario finito | Solo clasificación de subpoblación P*F | No condiciona la inclusión en P*τ2 |

## 6. Composición mínima candidata de E_i

Se propone evaluar, sin duplicidades, esta estructura conceptual:

`E_i = E_{scope,i} ∧ App*(τ2,S0_i)`.

Donde:

- `E_scope,i` significa que la instancia/configuración basal está dentro del alcance del DGP y satisface las condiciones constitutivas pre-Z aplicables que el IAM declara para el snapshot fuente. Como mínimo debe respetar el contrato de clases CMP/PAR/RUL/MET y la regla de cobertura REF; los predicados atómicos concretos y su obligatoriedad se derivan del IAM versionado, no de una lista ad hoc.
- `App*(τ2,S0_i)` significa que τ2 es semánticamente aplicable desde S0 según su definición/versionado y condiciones de aplicabilidad, no que la ruta esté disponible.

Esta propuesta **no** incluye dentro de E_i:
- `C_dep,0=0`, porque POP-CMP-001 lo exige como condición separada;
- `A_f,0*=0`, porque es otra condición separada y requiere la conjunción focal completa;
- `F_alt,0=0`, porque solo define P*F;
- `Need_preZ` ni `E_req_preZ`;
- recepción, instalación, `C_dep*`, accesibilidad post, petición, selección, ejecución, Outcome o Value.

No se acepta que `E_scope` sea simplemente `CMP≥1 ∧ PAR≥1 ∧ RUL≥1` sin IAM por unidad: la cardinalidad de clase es necesaria para el contrato base, pero no acredita roster completo, obligatoriedad atómica, pertenencia de cada registro ni verdad de todos los predicados aplicables.

## 7. Regla pre-Z y estados

Para cada requisito de E_i:
- la aplicabilidad y obligatoriedad se declaran antes de Z en IAM versionado;
- los estados 1/0/? se respaldan con evidencia y cobertura específicas;
- NA solo se admite por regla de no aplicabilidad ex ante;
- un fallo confirmado de un requisito obligatorio excluye de P*τ2 según regla basal preespecificada;
- la ausencia de evidencia, roster incompleto, mapping ambiguo o cobertura insuficiente produce indeterminación, no cero;
- toda indeterminación y su adjudicación se resuelven antes de Z para el denominador confirmatorio, o se mantiene la unidad fuera del conjunto confirmado y se informa con análisis de sensibilidad;
- truth del Generator y clasificación observada del Analyzer se almacenan y evalúan separadamente.

La regla de exclusión de indeterminados debe ser explícita y previa a Z; no se debe presentar la población observada/confirmada como si fuese automáticamente la población verdadera P* sin modelar error de clasificación.

## 8. Límite P0/P1 y riesgo de duplicidad

La clasificación de cada requisito debe usar `NODE.boundary_class`:
- P0_CONFIG: condición interna de la configuración;
- P1_ENVIRONMENT: condición del entorno;
- DUAL_P0_P1: condición compartida con dos ubicaciones/roles explícitos;
- NA: no aplicable solo con justificación ex ante;
- P2 transversal no se usa como clase local de frontera.

No se debe incorporar automáticamente a E_i todo recurso, capacidad, permiso, endpoint o condición ambiental. Debe establecerse si es constitutivo para la aplicabilidad de τ2, término de `A_f*`, parte de `C_dep`, o vía colateral de la política. El mismo elemento no se duplica en E_i y A_f* sin declarar que una es guarda de población y la otra es medición de accesibilidad, y sin justificar el efecto de esa selección.

## 9. Dictamen y acción siguiente

**Dictamen C1.3:** la composición mínima `E_scope ∧ App*(τ2,S0)` es una propuesta coherente con las fuentes, pero **no está aprobada ni operacionalizada**. Los contratos disponibles no permiten cerrar hoy el roster de condiciones basales por UE, los mappings P0/P1, la aplicabilidad de τ2 ni la adjudicación de indeterminación. No se debe declarar E_i cerrada.

**Siguiente operación C1.4:** construir el crosswalk por predicado/registro del IAM pre-Z para el snapshot `C_SRC`, y cruzarlo con `App*(τ2,S0)`, `C_dep,0` y cada término de `A_f,0*`. El entregable debe identificar por cada condición: ID/version, objeto/campo, boundary_class, etapa/tiempo, obligatoriedad/aplicabilidad, papel causal (E_scope/App/C_dep/A_f/colateral/epistémico), evidencia, estados 1/0/?/NA y regla de adjudicación. Si los registros IAM no están materializados, el resultado será un crosswalk lógico de vacíos, no un IAM ficticio.

No se necesita reabrir la precedencia P*τ2/P*F. La única cuestión de aprobación posterior será si se acepta esta composición mínima E_scope∧App como contrato conceptual de E_i una vez completado el crosswalk y descartadas duplicidades. No hay Design Freeze ni autorización de implementación/ejecución.


## 10. Precedencia del ciclo PA — alcance DGP frente a elegibilidad experimental (2026-11-11)

La reconciliación integral PA (§15 de `C10_S_C1_ITT_D2_RECONCILIATION_DRAFT_001.md`) precisa la lectura de la propuesta de §6: `E_i=E_scope∧App*(τ2,S0)` permanece **NO ACEPTADA**. Se recomienda interpretar `E_scope` primariamente como gate de alcance/validez del universo DGP y no como filtro de selección adicional dentro de ese universo, salvo que el DGP incluya deliberadamente unidades fuera de alcance en el marco candidato. `App*(τ2,S0)` sigue siendo condición candidata de aplicabilidad semántica de τ2.

Esta precisión no cierra la composición de E_i ni permite clasificar unidades: IAM, C_SRC y snapshots materiales siguen ausentes. Se mantienen separadas `C_dep,0=0` y `A_f,0*=0` como condiciones de `P*_{τ2}`; `F_alt,0` solo afecta `P*_F`. No se recupera `C_other` ni se duplican términos de accesibilidad.

Para los estados pre-Z, `1/0/?` y `NA` justificado ex ante son obligatorios. UNKNOWN no equivale a cero ni puede excluirse silenciosamente; truth del Generator y clasificación observada del Analyzer permanecen separadas. La regla de estimación para unidades indeterminadas debe estar preespecificada antes de Z, y no puede usar información post-Z.

El siguiente paquete operativo es PB; no se abre una conversación C1.5 separada.
