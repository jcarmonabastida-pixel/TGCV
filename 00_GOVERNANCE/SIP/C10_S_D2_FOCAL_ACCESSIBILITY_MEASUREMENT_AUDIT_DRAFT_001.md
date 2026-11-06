# C10-S — Auditoría de definición observacional de D_f* y medición de A_f*
**ID:** C10-S-MEAS-AUD-001 · **Versión:** Draft 001 · **Fecha:** 2026-11-06
**Estado:** AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT
**Rama:** `research/c10-s-consolidation-draft`
**Ámbito:** definición estructural, snapshots, predicados, observación, adjudicación y error de medición de la accesibilidad focal D2.
**No autoriza:** aceptación de nuevos predicados, freeze, implementación, simulación, estimación ni ejecución científica.

## 1. Dictamen ejecutivo

La definición conceptual de `A_f^*` y `D_f^*` está parcialmente estabilizada, pero su **contrato observacional no está cerrado**. La arquitectura ya separa (i) verdad estructural del sistema, (ii) paquete de evidencia/observación y (iii) clasificación del analizador. También establece que `D_f^*` es la apertura basal→post de la misma transformación focal, no un sustituto de `ΔT_acc^*`.

No obstante, todavía no es posible afirmar que una variable observada `D_f^{obs}` mida sin ambigüedad el tratamiento endógeno `D_f^*`. Persisten decisiones no resueltas sobre composición de predicados, comparabilidad y pertenencia exacta de snapshots, cobertura de rutas, reglas de adjudicación, cegamiento operativo, error diferencial y datos faltantes.

**Dictamen:** mantener `D_f^*` como tratamiento focal verdadero del DGP y `D_f^{obs}` como clasificación observacional separada. No calcular ni interpretar `LATE_f` usando una variable observada hasta cerrar los gates de §9 y demostrar desempeño de medición con truth oculta y escenarios adversariales. La auditoría no cambia el dictamen IV anterior: Wald sigue bloqueado.

## 2. Fuentes canónicas de la rama inspeccionadas

- `C10_S_DGP_TEMPORAL_AND_ROLE_CONTRACT_DRAFT_001.md`, §§3.3–4, 6–10.
- `C10_S_TRANSFORMATIONAL_SNAPSHOT_AND_DELTA_RECONCILIATION_DRAFT_001.md`, §§2–9.
- `C10_S_IDENTITY_VERSION_AND_SNAPSHOT_MATCHING_CONTRACT_DRAFT_001.md`, §§8–13.
- `C10_S_PATH_PREDICATE_TEMPORAL_EVIDENCE_MATRIX_DRAFT_001.md`, especialmente fichas D2-INV-AUTH-01, D2-RES-01 y crosswalks.
- `C10_S_GRAPH_COVERAGE_AND_TRIVALENT_EVIDENCE_MATRIX_DRAFT_001.md`, §§4–8.
- `C10_S_UG_INVENTORY_REGISTER_TEMPLATE_DRAFT_001.md`, §§1–9.
- `C10_S_UG_SNAPSHOT_MEMBERSHIP_AND_VERSIONED_GRAPH_REFERENCES_OPTIONS_DRAFT_001.md`, §§3–7.
- DEC-C10-065 — pinning exacto de revisión SNAPSHOT.
- Auditoría IV `C10_S_D2_LATE_F_IV_VALIDITY_AUDIT_DRAFT_001.md`.

Los contratos y plantillas citados son propuestas/contratos documentales en distintos estados; su presencia no demuestra inventario técnico, cobertura real ni validación.

## 3. Separación de objetos que debe preservarse

| Objeto | Significado | Regla |
|---|---|---|
| `S_T^*(i,b,c,t)` | Verdad estructural del sistema-unidad-frontera-contexto-tiempo | No observable directamente en sistema real; en DGP queda oculta al analizador |
| `E_T(i,b,c,t)` | Fuentes, cobertura, validez de evidencia, procedencia, versión, tiempo y adjudicación | Puede cambiar sin que cambie el sistema |
| `A_f^*(i,t)` | Accesibilidad focal verdadera de la misma identidad semántica `τ2` | Derivada de predicados estructurales constitutivos completos |
| `A_{f}^{obs}(i,t)` | Clasificación observada del estado focal | Debe ser 1/0/?; nunca se fuerza desde falta de evidencia |
| `D_f^*(i)` | `I(A_f^*(i,t0)=0 ∧ A_f^*(i,t1)=1)` | Tratamiento focal verdadero basal→post |
| `D_f^{obs}(i)` | Clasificación observada de apertura focal | Debe conservar indeterminación y errores; no sustituye automáticamente D_f* |
| `ΔT_{acc}^*` | Cambio estructural completo del espacio accesible | No queda resumido por el indicador focal |
| `ΔE_T` | Cambio de evidencia/observabilidad | No es cambio estructural de accesibilidad |

La regla de dos capas de snapshot y la separación entre `ΔT_acc^*` y `ΔE_T` son conceptualmente compatibles con el contrato de identidad/matching. Se deben conservar sin fusionar las etiquetas `Validity_struct` y `Validity_e`.

## 4. Hallazgos y discrepancias

### MEAS-01 — Composición de A_f* no reconciliada completamente
**Estado:** OPEN / MATERIAL.

El DGP §3.3 define `A_f,i1^*` mediante `C_dep`, `C_auth,base`, `C_resource`, `C_capacity`, `C_info`, `C_domain` y `C_other`. Sin embargo, el crosswalk de información advierte que no se debe crear `C_info` autónomo ni incorporarlo a `A_f^*` hasta resolver duplicidades; la ficha D2-RES-01 también separa disponibilidad estructural, capacidad instalada, consumo de ejecución y recursos usados por B. No está cerrado qué predicados son constitutivos, cuáles son condiciones ya incluidas en `C_dep^*` o `R_access^*`, cuáles son invariantes postulados y cuáles son mediciones.

**Riesgo:** doble contabilización, condición postratamiento mal clasificada o definición de tratamiento que varía según el documento consultado.

**Resolución necesaria:** crosswalk único por predicado con definición, rol causal, nivel, unidad, tiempo, evidencia y pertenencia a la conjunción; declarar expresamente duplicidades y exclusiones. No añadir símbolos ni cambiar la conjunción por inferencia editorial.

### MEAS-02 — El estado focal exige identidad semántica y comparabilidad pre/post
**Estado:** PRINCIPIO DEFINIDO / OPERACIONALIZACIÓN ABIERTA.

El contrato de matching establece que no se calcula `D_f^*` si `τ2` no corresponde como la misma identidad entre t0 y t1. Frontera, unidad, contexto, granularidad, catálogo, mapping y reglas de composición deben ser compatibles. Cambios de RID/SID no implican necesariamente cambio de TID; hash distinto tampoco prueba identidad nueva.

**Riesgo:** clasificar como apertura una sustitución de identidad, o declarar pérdida/alta por cambios de cobertura, granularidad o versionado.

**Resolución necesaria:** fijar antes de Z la identidad focal, contrato semántico, frontera, G, catálogo, mapping M y reglas de equivalencia/versionado. Si el matching es unresolved o snapshots no comparables, `D_f^{obs}=?` y el caso no se recodifica como 0/1.

### MEAS-03 — Pinning exacto aceptado, pertenencia completa del grafo pendiente
**Estado:** DECISIÓN ACEPTADA / VALIDACIÓN Y RECONCILIACIÓN ABIERTAS.

DEC-C10-065 acepta `snapshot_object_record_id` obligatorio en NODE, EDGE, ROUTE, PREDICATE y ROUTE_STEP, con FK compuesta a SNAPSHOT. La propuesta UG-SCH-10 aún registra como abierto el cierre integral de pertenencia, referencias exactas, secuencia ROUTE_STEP, claves/FKs y circularidad SNAPSHOT↔NODE raíz. El pinning exacto no acredita que los encabezados, constraints, relaciones y validadores estén reconciliados ni implementados.

**Riesgo:** una observación puede referir a registros de revisiones o snapshots distintos y parecer comparable sin serlo.

**Resolución necesaria:** propagar DEC-C10-065 a todas las tablas, contratos, crosswalks y esquema; verificar referencias exactas y coherencia de mismo snapshot; mantener estado documental/validación técnica separado. UG-SCH-10 no se cierra por esta auditoría.

### MEAS-04 — La cobertura de rutas determina cuándo 0 es admisible
**Estado:** PRINCIPIO DEFINIDO / INVENTARIO REAL NONE.

La matriz U_G distingue rutas focales, alternativas, compartidas, externas y desconocidas. Para declarar una ruta no factible se requiere al menos un predicado necesario observado 0 con evidencia válida y cobertura suficiente. La ausencia de ruta/alternativa solo se puede afirmar con universo operativo declarado y cubierto; Runknown impide inferir exhaustividad. La plantilla de inventario permanece vacía/no inventariada.

**Riesgo:** convertir `NONE`, `MISSING`, `PARTIAL`, no inventariado o falta de evidencia en inaccesibilidad. También puede haber una ruta alternativa para la misma τ2 aunque `C_dep^*=0`.

**Resolución necesaria:** cobertura por unidad, snapshot, ruta, predicado, fuente y versión; evidencia negativa específica y universo declarado; unknown explícito para rutas opacas/externas. Sin cobertura, resultado observado ?.

### MEAS-05 — Adjudicación independiente y cegamiento solo están definidos en papel
**Estado:** PROPUESTA / NO EJECUTADA.

Los contratos proponen que el analizador no reciba truth, Z/B ni Outcome/Value; que adjudicadores de matching no conozcan brazo ni resultados; y que evaluador independiente compare con truth después de congelar la salida. No existe evidencia de protocolo aplicado, separación de roles, independencia efectiva, registro de desacuerdos o doble evaluación.

**Riesgo:** filtración de brazo/resultados, adjudicación retrospectiva y sesgo de observación diferencial.

**Resolución necesaria:** protocolo operativo con roles/permisos, orden de congelación, ciego verificable, doble evaluación independiente, adjudicación conservando desacuerdos iniciales y audit trail inmutable.

### MEAS-06 — Error de medición diferencial y missingness no cuantificados
**Estado:** OPEN.

Los contratos prevén evaluar matching, falsos matches, matches omitidos, eventos ADD/REMOVE/MODIFY, unresolved, acuerdo entre evaluadores y sensibilidad a granularidad. El DGP contiene indicadores de observación por bloque y exige registrar motivo/tiempo/fuente/recuperabilidad. Sin embargo, no hay parámetros, estimadores, estratos ni límites aprobados para error diferencial de `A_f^{obs}`/`D_f^{obs}` por Z/B, tiempo, versión, cobertura o tipo de ruta.

**Riesgo:** una intervención que cambia logs, telemetría, permisos o cobertura puede alterar la clasificación observada aunque no cambie la accesibilidad verdadera; también puede ocultar cambios reales. La selección de casos completos puede romper la interpretación ITT y sesgar la muestra usada para IV.

**Resolución necesaria:** tabla de errores por brazo × tiempo × predicado/ruta × versión × cobertura; sensibilidad a falsos positivos/negativos y errores correlacionados; tasas y mecanismos de missingness; límites cuando error no sea identificable. No asumir error no diferencial ni missingness al azar.

### MEAS-07 — La secuencia temporal existe, pero requiere pinning de eventos y ventanas
**Estado:** PARCIAL.

El DGP ubica baseline antes de Z; política/recepción/intento en t1; instalación/verificación en t2; snapshot post y accesibilidad en t3; Reach en t4; conocimiento/selección/ejecución después. Prohíbe reconstruir accesibilidad retrospectivamente desde ejecución y exige snapshots posteriores nuevos si la ejecución altera el sistema. Falta fijar timestamps, tolerancias, simultaneidad, vigencia de permisos/recursos, ventanas de caducidad y regla de eventos concurrentes para el DGP definitivo.

**Riesgo:** clasificar como basal una condición posterior a Z, usar información posterior a selección/ejecución para determinar accesibilidad, o comparar snapshots temporalmente no equivalentes.

**Resolución necesaria:** protocolo temporal por unidad con zona/reloj, evento de referencia, ventanas, precedencia y reglas de simultaneidad; t3 sellado antes de K/Consider/Sel/Exec.

### MEAS-08 — Predicados desconocidos y lógica trivalente deben propagarse hasta D_f
**Estado:** PRINCIPIO DEFINIDO / REGLA COMPUESTA INCOMPLETA.

Los contratos prohíben convertir desconocido en cero. Para la conjunción, cualquier predicado constitutivo 0 con evidencia suficiente puede descartar accesibilidad; todos los predicados constitutivos 1 y cobertura adecuada pueden sostener 1; cualquier indeterminación material sin descarte suficiente debe mantener ?. Pero falta consolidar la regla completa para agregación de rutas alternativas, rutas compartidas, duplicidad de predicados y conflicto entre fuentes a nivel de `A_f^{obs}` y `D_f^{obs}`.

**Resolución necesaria:** una función de adjudicación versionada y reproducible, con reglas de conflicto, agregación de rutas, predicados necesarios/suficientes y tratamiento de evidencia contradictoria. No promediar estados categóricos.

## 5. Protocolo de medición que resulta exigible (propuesta, no aprobada)

1. **Congelación pre-Z:** fijar unidad/población, frontera, contexto, identidad TID de τ2, G, catálogo, mapping M, versiones, predicados y ventanas. Guardar snapshot basal y evidencia con hashes/procedencia.
2. **Captura post-B antes de K/selección/ejecución:** fijar recepción, intento, instalación/verificación y cambios de sistema; capturar snapshot post inmutable. No inferirlo de la ejecución.
3. **Matching y comparabilidad:** resolver identidad y referencias exactas; si no hay comparabilidad, registrar unresolved/?. No inferir pertenencia por timestamp o última versión.
4. **Adjudicación predicado a predicado:** registrar 1/0/? observado, evidencia, cobertura, fuente/version/hash, método, observador, regla/tolerancia, cegamiento, desacuerdo y razón de unknown. La truth del DGP permanece en canal separado.
5. **Agregación focal:** aplicar conjunción de predicados aprobada y rutas alternativas pertinentes; separar C_dep, A_f, D_f y ΔT_acc. No inferir A_f desde C_dep.
6. **Congelación de salida:** guardar `A_f^{obs}(t0)`, `A_f^{obs}(t1)`, `D_f^{obs}`, unresolved y cobertura antes de revelar Outcome/Value al adjudicador.
7. **Evaluación de error:** comparar después con truth oculta; cuantificar falsos positivos/negativos, unresolved, acuerdo, error por brazo/tiempo/version/ruta y sensibilidad a missingness.
8. **Uso causal:** conservar `D_f^*` como tratamiento verdadero del DGP. Si solo se dispone de `D_f^{obs}`, la inferencia IV requiere modelo/ajuste/identificación de error defendible; no sustituirlo sin más en Wald.

Este protocolo ordena requisitos ya dispersos. No fija parámetros, umbrales ni un algoritmo definitivo, y no se presenta como decisión aceptada.

## 6. Consecuencias para IV y estimandos

- La primera etapa relevante para `LATE_f` es la de `D_f^*`, no la de `C_dep^*` ni la mera clasificación observada.
- Una primera etapa estimada sobre `D_f^{obs}` puede estar sesgada si hay clasificación errónea diferencial por Z/B.
- La no observación o unresolved no puede tratarse como `D_f=0`; el análisis de casos completos cambia población y requiere supuestos.
- El error de medición no resuelve ni compensa exclusión, monotonicidad, independencia, consistencia o interferencia.
- La medición de `D_f^*` no identifica por sí sola `θ_{Af}(q_X^*)` ni el efecto general `θ_A(q)`.
- Si no puede identificarse el tratamiento verdadero o corregirse/limitarse el error con supuestos defendibles, `LATE_f` permanece no identificado; se informan ITT de política/paquete y/o límites según proceda.

## 7. Estado de documentos y decisiones

- DEC-C10-065 permanece ACCEPTED en su alcance de pinning exacto; no se amplía ni reinterpreta.
- UG-SCH-10 permanece OPEN; no se acepta Opción A ni se declara validación técnica por esta auditoría.
- Contratos de DGP, snapshot, matching, predicados e inventario permanecen propuestas/contratos documentales con estados propios; esta auditoría no los convierte en aceptados.
- No se modifica DEC-C10-066/067 ni se acepta REC-EST-01…09.
- No se cierran XSYNC, MD-C1, MD-C4 ni gates IV.
- No se modifica C10-D1, TGCV Core, RMA, Matrix, STATUS o claims.

## 8. Gates de medición

| Gate | Criterio de cierre |
|---|---|
| MEAS-G1 | Composición de predicados de A_f reconciliada, sin duplicidad ni símbolos ambiguos |
| MEAS-G2 | Identidad τ2, frontera, contexto, G, catálogo y mapping preespecificados |
| MEAS-G3 | Pinning y pertenencia de snapshots/referencias exactas reconciliados (incluida UG-SCH-10) |
| MEAS-G4 | Inventario/cobertura por rutas y predicados suficiente; UNKNOWN conservado |
| MEAS-G5 | Protocolo temporal y snapshots t0/t1 sellados antes de K/Sel/Exec |
| MEAS-G6 | Adjudicación, doble evaluación, ciego y control de conflictos especificados |
| MEAS-G7 | Error diferencial y missingness cuantificados o acotados por brazo/tiempo/version |
| MEAS-G8 | Recuperación con truth oculta y escenarios adversariales demuestra clasificación correcta de 1/0/? |

El cierre documental de estos gates no autoriza ejecución; la validación técnica y la autorización científica siguen siendo controles separados.

## 9. Siguiente operación documental

Resolver **MEAS-01** primero: construir un crosswalk exhaustivo de cada predicado que aparece en `A_f^*` frente a DGP, fichas de invariantes, contratos de recursos/capacidad/información, B-M01…15 y matriz de cobertura; clasificarlo como constitutivo, invariante postulada, vía colateral, epistémico o duplicado, sin alterar aún la fórmula aceptada ni crear símbolos. Después, reconciliar la regla trivalente de agregación de predicados/rutas. Mantener `LATE_f` bloqueado.


---

## Addendum de corrección y crosswalk (2026-11-06)

**Corrección de MEAS-01:** la auditoría original tomó la fórmula histórica de §30.1/§3.x como si fuera composición vigente. Se corrige expresamente. La precedencia documental del DGP §59.3 y del maestro §67.3 ya presenta una fórmula candidata depurada:
`A_f*=I(ID_f* AND REL_f* AND COND_f* AND AUTH_f* AND RES_f* AND DEP_f* AND NOT BLOCK_f*)`.
Por tanto, C_info no es factor autónomo; C_resource/C_capacity se canalizan a RES/R_access solo si son disponibilidad ex ante necesaria y no duplicada; C_domain/D_support se mapea a ID/tipo o COND; C_other es residual inadmisible; VALID/cobertura/E_T son epistémicos; App_f/K/selección/ejecución quedan fuera. El crosswalk completo está en `C10_S_D2_AF_PREDICATE_CAUSAL_CROSSWALK_DRAFT_001.md`.

MEAS-01 deja de describir una fórmula no reconciliada y pasa a **PARTIAL**: fórmula candidata identificada; mappings y operacionalización de RES, D_support↔ID/COND, REL/COND/BLOCK y rutas aún abiertos. Esta corrección no aprueba ni congela §67.3 y no altera DEC-C10-065/066/067. La auditoría sigue siendo asistida/no independiente.


---

## Addendum: regla trivalente de agregación (2026-11-06)

**Fuente:** `C10_S_AF_DF_TRIVALENT_AGGREGATION_RULE_DRAFT_001.md`.  
**Estado:** AUTHOR_SELF_REVIEW / ASSISTED / NOT_INDEPENDENT.

Se formaliza la propagación de `A_f^{obs}`, `DEP_f^{obs}` y `D_f^{obs}` reutilizando DGP §26/§32 y U_G §5 / protocolo de adjudicación. La conjunción de A_f observada da 0 ante cualquier término necesario con 0 válido/suficiente; da 1 solo si todos los términos son 1 con comparabilidad/cobertura adecuadas; en otro caso ?. DEP es disyunción de rutas: una ruta 1 basta; 0 exige universo exhaustivo COMPLETE y todas las rutas 0; en otro caso ?. D_f observado da 1 solo con baseline 0/post 1; da 0 si baseline 1 o post 0; en los demás casos ?. No comparabilidad de τ2/snapshots implica NOT_COMPARABLE/?.

Se distingue evidencia/conflicto/cobertura de estado observado y truth DGP. No se convierte MISSING/NONE/PARTIAL/unknown en 0. Una alternativa válida impide inferir DEP=0 desde C_dep=0. La elegibilidad verdadera basal no se sustituye por clasificación observada sin modelar error.

La regla no aprueba ni congela la fórmula, no valida error diferencial ni cierra IV. `LATE_f` sigue bloqueado. Documento formal: `C10_S_AF_DF_TRIVALENT_AGGREGATION_RULE_DRAFT_001.md`.


---

## 10. Regla trivalente de agregación de A_f*, DEP_f* y D_f observado

**ID lógico:** C10-S-AF-DF-TRI-001 · **Estado:** reconciliación documental asistida; no aprobada, no congelada, no ejecutada.  
**Crosswalk normativo:** DGP §§26, 30–32; matriz U_G §5; protocolo U_G §§2, 5–11, 14, 17–18; fórmula candidata del maestro §67.3 y crosswalk causal de predicados.

### 10.1 Dominios ortogonales

Para cada predicado/ruta se conservan por separado:
- `observed_state ∈ {1,0,?}`;
- `evidence_status ∈ {AVAILABLE,MISSING,CONFLICTING}`;
- `coverage_status ∈ {NONE,PARTIAL,COMPLETE}`;
- estado de revisión/adjudicación;
- `truth_dgp ∈ {0,1}), solo en generador/evaluador restringido y nunca en el paquete del analizador.

No existe conversión mecánica entre ellos. MISSING, NONE, PARTIAL, no inventariado, no observado o sin logs no significan 0. CONFLICTING no se resuelve por mayoría automática.

### 10.2 Conjunción de A_f observada

Se mantiene la fórmula candidata:
`A_f^*=I(ID_f^*∧REL_f^*∧COND_f^*∧AUTH_f^*∧RES_f^*∧DEP_f^*∧¬BLOCK_f^*)`.

Cada término debe referirse a la misma unidad, identidad τ2, frontera, contexto, snapshot/revisión y ventana compatibles.

| Regla | Resultado |
|---|---|
| Algún término necesario es 0 con evidencia válida, alcance compatible y cobertura suficiente para ese incumplimiento | `A_f^{obs}=0` |
| Todos los términos necesarios son 1, con matching/comparabilidad válidos y cobertura adecuada para cada afirmación | `A_f^{obs}=1` |
| No hay 0 suficiente y existe ?, conflicto no resuelto, falta de evidencia, identidad no comparable o cobertura insuficiente | `A_f^{obs}=?` |

Un 0 local basta para refutar la conjunción si el predicado es necesario y la evidencia demuestra su incumplimiento en el alcance focal. No es necesario completar los demás términos una vez establecido ese 0. En cambio, no encontrar una ruta, permiso, recurso o componente no basta para 0 sin cobertura negativa suficiente. Un 1 requiere respaldo de todos los términos; no se infiere de intención contractual, intento o éxito de un componente técnico.

Un conflicto impide adjudicar ese término como 1/0. Un 0 independiente, válido y suficiente en otro término necesario puede mantener la conjunción agregada en 0, dejando registrado el conflicto. Si el conflicto afecta identidad, frontera, unidad o comparabilidad global, el agregado queda ?.

### 10.3 DEP_f y rutas

Cada ruta es una conjunción:
- ruta=1 si todos sus predicados necesarios son 1 y secuencia, identidad, versiones y orden temporal son compatibles;
- ruta=0 si al menos un necesario es 0 con evidencia válida/suficiente para esa ruta;
- ruta=? en cualquier otro caso.

DEP en el contrato general es la existencia de al menos una ruta admisible válida para la misma τ2:

| Universo de rutas | `DEP_f^{obs}` |
|---|---|
| Existe al menos una ruta adjudicada 1 | 1 |
| Todas las rutas del universo operativo declarado son 0 y cobertura COMPLETE, con Runknown y rutas externas/compartidas/alternativas materiales resueltas | 0 |
| No hay ruta 1 y queda alguna ruta ?, Runknown, ruta material no inventariada o cobertura NONE/PARTIAL | ? |

Una ruta 1 basta aunque otras sigan ?. Una ruta alternativa válida impide declarar DEP=0 solo porque la ruta focal `C_dep` sea 0. C_dep=DEP únicamente bajo el supuesto explícito de ruta única del DGP aislado; no se generaliza sin inventario/cobertura.

### 10.4 Bloqueo

El término de la fórmula es `¬BLOCK_f^*`:
- bloqueo efectivo focal demostrado (`BLOCK_f^{obs}=1`) implica término negado=0 y puede hacer A_f=0;
- ausencia de bloqueo (`BLOCK_f^{obs}=0`) requiere cobertura suficiente del universo de bloqueos relevantes;
- bloqueo/cobertura desconocidos mantienen ?.

Un bloqueo de una ruta no bloquea necesariamente rutas alternativas. Falta de logs/conflicto no demuestra ausencia de bloqueo.

### 10.5 Derivación de D_f observado

La verdad sigue siendo `D_f^*=I(A_{f,base}^*=0 ∧ A_{f,post}^*=1)`. D_f observado se deriva solo de A_f observado basal y post:

| Baseline obs | Post obs | D_f obs |
|---|---|---|
| 0 | 1 | 1 |
| 0 | 0 | 0 |
| 1 | 0 | 0 |
| 1 | 1 | 0 |
| ? | 0 | 0 |
| ? | 1 | ? |
| 0 | ? | ? |
| ? | ? | ? |

Equivalente: D=1 solo si baseline=0 y post=1; D=0 si baseline=1 o post=0; resto ?. Si τ2, frontera, unidad/contexto, granularidad, catálogo, mapping o snapshots no son comparables, registrar `NOT_COMPARABLE/?`, nunca 0.

La elegibilidad verdadera exige `A_{f,base}^*=0` pre-Z. Una clasificación observada basal 0 no la sustituye automáticamente sin tratar el error de clasificación/selección.

### 10.6 Ejemplos lógicos de frontera

1. ID=1, REL=1, COND=1, AUTH=1, RES=1, DEP=?, ¬BLOCK=1 → A_f obs=?.
2. Si AUTH=0 válido y focal, A_f obs=0 aunque DEP=?.
3. Ruta focal=0 y alternativa equivalente=1 → DEP obs=1.
4. Runknown=? sin ruta confirmada → DEP obs=?.
5. Rutas inventariadas=0 con cobertura PARTIAL → DEP obs=?.
6. Baseline=0 y post=? → D_f obs=?.
7. Baseline=? y post=1 → D_f obs=?.
8. τ2/snapshot post no comparable → D_f obs=? / NOT_COMPARABLE.

### 10.7 Trazabilidad y consecuencias IV

Cada agregado enlaza unidad, frontera, contexto, τ2/TID, versiones/snapshots, predicados/rutas, regla versionada, evidencias/hashes/fuentes/tiempos, coverage scope/denominador, cegamiento, evaluaciones, conflictos, adjudicación, composición y razón explícita de 0/1/?. El analizador no recibe truth_dgp; el evaluador solo accede a truth tras congelar la salida observada.

La primera etapa focal causal se define sobre D_f verdadero, no D_f obs sin más. No convertir ? en 0, excluir indeterminados como si fueran aleatorios ni imputar sin modelo. Informar 1/0/? y error por brazo/tiempo/versión/ruta; si error diferencial/missingness no identificados, usar límites/sensibilidad o declarar no identificación. Esta regla no resuelve independencia, exclusión, monotonicidad, interferencia, consistencia ni relevancia IV. `LATE_f` permanece bloqueado.

**Pendiente:** armonizar dominios con plantilla U_G y matching/snapshots; resolver pertenencia exacta/UG-SCH-10; concretar rutas del microdominio; diseñar fixtures adversariales y medir error contra truth oculta bajo autorización futura. No cierra MEAS-G2…G8, XSYNC, PROV, MD-C1/MD-C4 ni gates IV. No modifica DEC-C10-065/066/067, fórmula, autorización o claims; no autoriza implementación, validación ejecutable, simulación ni experimento.
